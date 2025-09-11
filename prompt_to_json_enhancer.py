"""
Prompt-to-JSON Enhancer Core Module
====================================

This module contains the core functionality for transforming plain text prompts
into structured JSON format for better AI interactions.

Author: AI Assistant
Version: 1.0.0
"""

import json
import logging
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class PromptToJSONEnhancer:
    """
    Main class for transforming plain text prompts into structured JSON format.
    
    This class handles the core logic of analyzing input prompts and converting
    them into a structured format that improves AI response quality.
    """
    
    def __init__(self, log_file: str = "logs/prompt_enhancer.log"):
        """
        Initialize the Prompt-to-JSON Enhancer.
        
        Args:
            log_file (str): Path to the log file for tracking operations
        """
        self.log_file = log_file
        self.setup_logging()
        
        # Define default JSON template structure
        self.json_template = {
            "context": "",
            "problem": "",
            "expected_solution": "",
            "output_format": ""
        }
        
        # Common output formats for better AI responses
        self.output_formats = [
            "detailed explanation",
            "bullet points",
            "step-by-step guide",
            "comparative analysis",
            "summary",
            "code example",
            "table format",
            "essay format"
        ]
        
        # Keywords to help determine context
        self.context_keywords = {
            "technical": ["code", "programming", "algorithm", "software", "development"],
            "educational": ["explain", "teach", "learn", "understand", "concept"],
            "creative": ["write", "story", "poem", "creative", "imagine"],
            "analytical": ["analyze", "compare", "evaluate", "assess", "critique"],
            "business": ["strategy", "business", "marketing", "finance", "management"]
        }
        
        self.logger.info("Prompt-to-JSON Enhancer initialized successfully")
    
    def setup_logging(self):
        """Set up logging configuration for tracking operations and errors."""
        # Create logs directory if it doesn't exist
        log_dir = Path(self.log_file).parent
        log_dir.mkdir(exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()  # Also log to console
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def analyze_prompt(self, prompt: str) -> Dict[str, str]:
        """
        Analyze a plain text prompt to extract key components.
        
        Args:
            prompt (str): The input prompt to analyze
            
        Returns:
            Dict[str, str]: Dictionary containing extracted components
        """
        self.logger.info(f"Analyzing prompt: {prompt[:50]}...")
        
        # Clean and normalize the prompt
        cleaned_prompt = self.clean_prompt(prompt)
        
        # Extract context based on keywords
        context = self.detect_context(cleaned_prompt)
        
        # Identify the main problem/question
        problem = self.extract_problem(cleaned_prompt)
        
        # Determine expected solution approach
        expected_solution = self.determine_solution_approach(cleaned_prompt, context)
        
        # Suggest appropriate output format
        output_format = self.suggest_output_format(cleaned_prompt, context)
        
        result = {
            "context": context,
            "problem": problem,
            "expected_solution": expected_solution,
            "output_format": output_format
        }
        
        self.logger.info(f"Analysis complete. Context: {context}, Format: {output_format}")
        return result
    
    def clean_prompt(self, prompt: str) -> str:
        """
        Clean and normalize the input prompt.
        
        Args:
            prompt (str): Raw input prompt
            
        Returns:
            str: Cleaned prompt
        """
        # Remove extra whitespace and normalize
        cleaned = re.sub(r'\s+', ' ', prompt.strip())
        
        # Remove common filler words that don't add value
        filler_words = ["please", "can you", "could you", "i need", "i want"]
        for word in filler_words:
            cleaned = re.sub(f'^{word}\\s+', '', cleaned, flags=re.IGNORECASE)
        
        self.logger.debug(f"Cleaned prompt: {cleaned}")
        return cleaned
    
    def detect_context(self, prompt: str) -> str:
        """
        Detect the context/category of the prompt based on keywords.
        
        Args:
            prompt (str): Cleaned prompt text
            
        Returns:
            str: Detected context category
        """
        prompt_lower = prompt.lower()
        
        # Count keyword matches for each context
        context_scores = {}
        for context, keywords in self.context_keywords.items():
            score = sum(1 for keyword in keywords if keyword in prompt_lower)
            context_scores[context] = score
        
        # Return the context with highest score, or 'general' if no clear match
        if context_scores:
            best_context = max(context_scores, key=context_scores.get)
            if context_scores[best_context] > 0:
                return best_context
        
        return "general"
    
    def extract_problem(self, prompt: str) -> str:
        """
        Extract the main problem or question from the prompt.
        
        Args:
            prompt (str): Cleaned prompt text
            
        Returns:
            str: Extracted problem statement
        """
        # Look for question patterns
        question_patterns = [
            r'what (?:is|are|was|were) (.+?)(?:\?|$)',
            r'how (?:do|does|can|should) (.+?)(?:\?|$)',
            r'why (?:is|are|does) (.+?)(?:\?|$)',
            r'explain (.+?)(?:\?|$)',
            r'describe (.+?)(?:\?|$)',
            r'compare (.+?)(?:\?|$)',
            r'analyze (.+?)(?:\?|$)'
        ]
        
        for pattern in question_patterns:
            match = re.search(pattern, prompt, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        # If no specific pattern found, return the original prompt
        return prompt
    
    def determine_solution_approach(self, prompt: str, context: str) -> str:
        """
        Determine the expected solution approach based on prompt and context.
        
        Args:
            prompt (str): Cleaned prompt text
            prompt (str): Detected context
            
        Returns:
            str: Expected solution approach
        """
        context_approaches = {
            "technical": "Provide technical explanation with examples and best practices",
            "educational": "Give clear, step-by-step explanation suitable for learning",
            "creative": "Offer creative suggestions and examples",
            "analytical": "Present detailed analysis with pros/cons and conclusions",
            "business": "Focus on practical applications and business value",
            "general": "Provide comprehensive information covering key aspects"
        }
        
        return context_approaches.get(context, context_approaches["general"])
    
    def suggest_output_format(self, prompt: str, context: str) -> str:
        """
        Suggest appropriate output format based on prompt and context.
        
        Args:
            prompt (str): Cleaned prompt text
            context (str): Detected context
            
        Returns:
            str: Suggested output format
        """
        # Check for specific format requests
        format_keywords = {
            "bullet": "bullet points",
            "list": "bullet points",
            "step": "step-by-step guide",
            "table": "table format",
            "compare": "comparative analysis",
            "summary": "summary",
            "code": "code example",
            "essay": "essay format"
        }
        
        prompt_lower = prompt.lower()
        for keyword, format_type in format_keywords.items():
            if keyword in prompt_lower:
                return format_type
        
        # Default formats based on context
        context_formats = {
            "technical": "detailed explanation",
            "educational": "step-by-step guide",
            "creative": "essay format",
            "analytical": "comparative analysis",
            "business": "summary",
            "general": "detailed explanation"
        }
        
        return context_formats.get(context, "detailed explanation")
    
    def enhance_prompt(self, prompt: str) -> Dict[str, any]:
        """
        Main method to enhance a plain text prompt into structured JSON.
        
        Args:
            prompt (str): Input prompt to enhance
            
        Returns:
            Dict[str, any]: Enhanced prompt in JSON format
        """
        self.logger.info("Starting prompt enhancement process")
        
        try:
            # Analyze the prompt
            analysis = self.analyze_prompt(prompt)
            
            # Create enhanced JSON structure
            enhanced_prompt = {
                "original_prompt": prompt,
                "enhanced_prompt": {
                    "context": analysis["context"],
                    "problem": analysis["problem"],
                    "expected_solution": analysis["expected_solution"],
                    "output_format": analysis["output_format"]
                },
                "metadata": {
                    "timestamp": datetime.now().isoformat(),
                    "enhancement_version": "1.0.0",
                    "processing_time": "N/A"  # Could add timing if needed
                }
            }
            
            self.logger.info("Prompt enhancement completed successfully")
            return enhanced_prompt
            
        except Exception as e:
            self.logger.error(f"Error enhancing prompt: {str(e)}")
            raise
    
    def format_json_output(self, enhanced_prompt: Dict[str, any], pretty: bool = True) -> str:
        """
        Format the enhanced prompt as JSON string.
        
        Args:
            enhanced_prompt (Dict[str, any]): Enhanced prompt dictionary
            pretty (bool): Whether to format with indentation
            
        Returns:
            str: Formatted JSON string
        """
        if pretty:
            return json.dumps(enhanced_prompt, indent=2, ensure_ascii=False)
        else:
            return json.dumps(enhanced_prompt, ensure_ascii=False)
    
    def save_enhanced_prompt(self, enhanced_prompt: Dict[str, any], filename: str = None) -> str:
        """
        Save enhanced prompt to a JSON file.
        
        Args:
            enhanced_prompt (Dict[str, any]): Enhanced prompt to save
            filename (str): Optional custom filename
            
        Returns:
            str: Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"enhanced_prompts/enhanced_prompt_{timestamp}.json"
        
        # Create directory if it doesn't exist
        file_path = Path(filename)
        file_path.parent.mkdir(exist_ok=True)
        
        # Save the file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(enhanced_prompt, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"Enhanced prompt saved to: {filename}")
        return str(file_path)


def main():
    """
    Main function for testing the Prompt-to-JSON Enhancer.
    """
    print("Prompt-to-JSON Enhancer - Test Run")
    print("=" * 50)
    
    # Initialize the enhancer
    enhancer = PromptToJSONEnhancer()
    
    # Test prompts
    test_prompts = [
        "Explain blockchain technology",
        "How do I write a Python function?",
        "Compare React and Vue.js",
        "Write a creative story about a robot",
        "Analyze the pros and cons of remote work",
        "What is machine learning?",
        "Create a marketing strategy for a startup"
    ]
    
    print(f"\nTesting with {len(test_prompts)} sample prompts...")
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n{i}. Testing: '{prompt}'")
        print("-" * 30)
        
        try:
            # Enhance the prompt
            enhanced = enhancer.enhance_prompt(prompt)
            
            # Display results
            print("Enhanced JSON:")
            print(enhancer.format_json_output(enhanced))
            
            # Save to file
            filename = f"enhanced_prompts/test_prompt_{i}.json"
            enhancer.save_enhanced_prompt(enhanced, filename)
            print(f"Saved to: {filename}")
            
        except Exception as e:
            print(f"Error processing prompt: {str(e)}")
    
    print("\n" + "=" * 50)
    print("Test run completed!")
    print("Check the 'enhanced_prompts' and 'logs' directories for results.")


if __name__ == "__main__":
    main()
