"""
FastAPI backend server for Prompt-to-JSON Enhancer
- Loads GEMINI_API_KEY from .env
- Exposes /health and /enhance endpoints
- Uses Gemini to enrich analysis; falls back to local heuristic if key missing
"""

import os
import json
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

try:
    from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover
    def load_dotenv():  # fallback if not installed
        return None

# Local analyzer
from prompt_to_json_enhancer import PromptToJSONEnhancer

# Try to import Gemini client
try:
    import google.generativeai as genai  # type: ignore
except Exception:  # pragma: no cover
    genai = None

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GEMINI_API_TOKEN")

app = FastAPI(title="Prompt-to-JSON Enhancer API", version="1.0.0")

# Allow extension and local dev origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

enhancer = PromptToJSONEnhancer(log_file="logs/backend_api.log")


class EnhanceRequest(BaseModel):
    prompt: str


class EnhanceResponse(BaseModel):
    original_prompt: str
    enhanced_prompt: Dict[str, Any]
    metadata: Dict[str, Any]


def call_gemini(prompt: str) -> Optional[Dict[str, Any]]:
    """Call Gemini to structure the prompt into our target schema.
    Returns None if unavailable or on error.
    """
    if not GEMINI_API_KEY or genai is None:
        return None
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        system = (
            "You are a prompt engineering assistant. Convert the user's plain prompt into a"
            " structured JSON with fields: context, problem, expected_solution, output_format."
            " Keep responses concise and accurate. Respond ONLY with JSON."
        )
        model = genai.GenerativeModel("gemini-1.5-flash")
        user_msg = (
            f"Plain prompt: {prompt}\nReturn JSON with keys: context, problem, expected_solution, output_format."
        )
        result = model.generate_content([system, user_msg])
        text = result.text.strip() if hasattr(result, "text") else ""
        # Attempt to parse JSON substring if wrapped
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1:
            text = text[start : end + 1]
        data = json.loads(text)
        # Validate minimal schema
        if not all(k in data for k in ["context", "problem", "expected_solution", "output_format"]):
            return None
        return {
            "original_prompt": prompt,
            "enhanced_prompt": data,
            "metadata": {
                "source": "gemini",
            },
        }
    except Exception:
        return None


@app.get("/")
async def root():
    return {
        "name": "Prompt-to-JSON Enhancer API",
        "version": "1.0.0",
        "status": "ok",
        "message": "Welcome! Use GET /health to check status and POST /enhance with {prompt} to transform prompts.",
        "docs": "/docs",
        "endpoints": {
            "GET /health": "Returns API and Gemini availability",
            "POST /enhance": "Body: { prompt: string } → { original_prompt, enhanced_prompt{context,problem,expected_solution,output_format}, metadata }"
        }
    }


@app.get("/health")
async def health():
    return {"status": "ok", "gemini": bool(GEMINI_API_KEY and genai is not None)}


@app.post("/enhance", response_model=EnhanceResponse)
async def enhance_endpoint(body: EnhanceRequest):
    if not body.prompt or not body.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is required")

    # Try Gemini first
    llm_result = call_gemini(body.prompt)
    if llm_result is None:
        # Fallback to local heuristic
        enhanced = enhancer.enhance_prompt(body.prompt)
        enhanced["metadata"]["source"] = "local"
        return enhanced  # type: ignore

    # Optionally merge with local hints to increase robustness
    local_hint = enhancer.analyze_prompt(body.prompt)
    merged = {
        "original_prompt": body.prompt,
        "enhanced_prompt": {
            "context": llm_result["enhanced_prompt"].get("context") or local_hint["context"],
            "problem": llm_result["enhanced_prompt"].get("problem") or local_hint["problem"],
            "expected_solution": llm_result["enhanced_prompt"].get("expected_solution")
            or local_hint["expected_solution"],
            "output_format": llm_result["enhanced_prompt"].get("output_format") or local_hint["output_format"],
        },
        "metadata": {"source": "gemini+local"},
    }
    return merged  # type: ignore


