"""
Setup script for Prompt-to-JSON Enhancer Chrome Extension Backend
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="prompt-to-json-enhancer",
    version="1.0.0",
    author="AI Assistant",
    author_email="ai@example.com",
    description="Backend system for transforming plain text prompts into structured JSON format",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/prompt-to-json-enhancer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.991",
        ],
        "api": [
            "fastapi>=0.85.0",
            "uvicorn>=0.18.0",
            "pydantic>=1.10.0",
        ],
        "nlp": [
            "nltk>=3.7",
            "spacy>=3.4.0",
            "textblob>=0.17.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "prompt-enhancer=prompt_to_json_enhancer:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.md", "*.txt"],
    },
    keywords="prompt, json, enhancement, ai, chrome-extension, nlp, text-processing",
    project_urls={
        "Bug Reports": "https://github.com/username/prompt-to-json-enhancer/issues",
        "Source": "https://github.com/username/prompt-to-json-enhancer",
        "Documentation": "https://github.com/username/prompt-to-json-enhancer#readme",
    },
)
