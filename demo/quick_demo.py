"""
Quick Demonstration Script
Shows a basic pipeline utilizing both the LLM and Visual engines.
"""
import sys
import os

# Ensure the parent directory is in the path so we can import 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import LLMEngine, VisualEngine

def run_showcase():
    print("\n" + "="*40)
    print("   MULTIMODAL AI DEMO INITIALIZED")
    print("="*40 + "\n")
    
    # 1. Vision Task
    print("[*] Starting Visual Engine...")
    vision = VisualEngine(model_name="yolo-v8-demo")
    vision_result = vision.process_image("../docs/screenshots/sample.png")
    print(f" -> Vision Output: {vision_result}\n")
    
    # 2. LLM Task
    print("[*] Starting LLM Engine...")
    llm = LLMEngine(model_name="gpt-demo")
    prompt = f"Analyze these detected objects: {vision_result.get('detected_objects', [])}"
    llm_result = llm.generate_response(prompt)
    print(f" -> LLM Output: {llm_result}\n")
    
    print("="*40)
    print("        DEMO COMPLETED")
    print("="*40 + "\n")

if __name__ == "__main__":
    run_showcase()
