 
import sys
import os

# Ensure 'src' is recognized as a package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.code_parser import extract_code_info
from src.comment_generator import generate_comments

print("✅ AI Code Commenter is Running...")

def main():
    if len(sys.argv) < 2:
        print("❌ Error: No file provided. Run with: python -m src.main sample.py")
        return

    file_path = sys.argv[1]
    
    with open(file_path, "r") as f:
        code = f.read()

    print("🔍 Extracting code details...")
    functions, classes = extract_code_info(code)
    print(f"📌 Functions: {functions}, Classes: {classes}")

    print("🚀 AI Generating Comments...")
    commented_code = generate_comments(code)

    print("\n🎯 AI-Generated Comments:\n")
    print(commented_code)

if __name__ == "__main__":
    main()
