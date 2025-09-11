#!/usr/bin/env python3
"""
Quick Test Script for Prompt-to-JSON Enhancer
==============================================

This script demonstrates the basic functionality of the Prompt-to-JSON Enhancer
without requiring Jupyter Notebook. Run this to quickly test the system.

Usage:
    python quick_test.py

Author: AI Assistant
Version: 1.0.0
"""

import json
import sys
from datetime import datetime
from prompt_to_json_enhancer import PromptToJSONEnhancer


def print_separator(title: str):
    """Print a formatted separator with title."""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


def print_json_pretty(data: dict, title: str = ""):
    """Print JSON data in a formatted way."""
    if title:
        print(f"\n{title}:")
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    """Main function to run quick tests."""
    print_separator("Prompt-to-JSON Enhancer - Quick Test")
    print(f"🚀 Starting test at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Initialize the enhancer
        print("\n📋 Initializing Prompt-to-JSON Enhancer...")
        enhancer = PromptToJSONEnhancer(log_file="logs/quick_test.log")
        print("✅ Enhancer initialized successfully!")
        
        # Test prompts
        test_prompts = [
            "Explain blockchain technology",
            "How to write a Python function?",
            "Compare React and Vue.js",
            "Write a creative story about a robot",
            "Create a marketing strategy for a startup"
        ]
        
        print_separator("Testing Prompt Enhancement")
        print(f"📝 Testing {len(test_prompts)} sample prompts...")
        
        enhanced_prompts = []
        
        for i, prompt in enumerate(test_prompts, 1):
            print(f"\n🔍 Test {i}: '{prompt}'")
            print("-" * 40)
            
            try:
                # Enhance the prompt
                enhanced = enhancer.enhance_prompt(prompt)
                enhanced_prompts.append(enhanced)
                
                # Display results
                print(f"✅ Success! Context: {enhanced['enhanced_prompt']['context']}")
                print(f"📋 Output Format: {enhanced['enhanced_prompt']['output_format']}")
                print(f"🎯 Problem: {enhanced['enhanced_prompt']['problem']}")
                
            except Exception as e:
                print(f"❌ Error: {str(e)}")
        
        # Show detailed results for first prompt
        if enhanced_prompts:
            print_separator("Detailed Example")
            first_enhanced = enhanced_prompts[0]
            print(f"Original Prompt: {first_enhanced['original_prompt']}")
            print_json_pretty(first_enhanced['enhanced_prompt'], "Enhanced JSON Structure")
            
            # Save sample result
            sample_file = "enhanced_prompts/quick_test_result.json"
            enhancer.save_enhanced_prompt(first_enhanced, sample_file)
            print(f"💾 Sample result saved to: {sample_file}")
        
        # Performance summary
        print_separator("Performance Summary")
        print(f"✅ Successfully processed: {len(enhanced_prompts)}/{len(test_prompts)} prompts")
        print(f"📊 Success rate: {len(enhanced_prompts)/len(test_prompts)*100:.1f}%")
        
        # Context distribution
        contexts = [ep['enhanced_prompt']['context'] for ep in enhanced_prompts]
        context_counts = {}
        for context in contexts:
            context_counts[context] = context_counts.get(context, 0) + 1
        
        print(f"🎯 Context Distribution:")
        for context, count in context_counts.items():
            print(f"   - {context}: {count}")
        
        # Output format distribution
        formats = [ep['enhanced_prompt']['output_format'] for ep in enhanced_prompts]
        format_counts = {}
        for format_type in formats:
            format_counts[format_type] = format_counts.get(format_type, 0) + 1
        
        print(f"📋 Output Format Distribution:")
        for format_type, count in format_counts.items():
            print(f"   - {format_type}: {count}")
        
        print_separator("Test Completed Successfully!")
        print("🎉 All tests passed! The Prompt-to-JSON Enhancer is working correctly.")
        print("📁 Check the following directories for outputs:")
        print("   - enhanced_prompts/ (enhanced prompt examples)")
        print("   - logs/ (processing logs)")
        print("\n💡 Next steps:")
        print("   1. Run 'jupyter notebook test_prompt_enhancer.ipynb' for comprehensive testing")
        print("   2. Check the README.md for detailed usage instructions")
        print("   3. Explore the sample_data/ directory for more examples")
        
    except ImportError as e:
        print(f"❌ Import Error: {str(e)}")
        print("💡 Make sure you've installed all requirements:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")
        print("💡 Check the logs/ directory for more details")
        sys.exit(1)


if __name__ == "__main__":
    main()
