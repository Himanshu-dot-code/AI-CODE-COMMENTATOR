import os
import google.generativeai as genai
import logging 
from dotenv import load_dotenv 

# Completely disable gRPC logging
os.environ["GRPC_ENABLE_FORK_SUPPORT"] = "0"
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_TRACE"] = ""

logging.getLogger("google").setLevel(logging.ERROR)

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def generate_comments(code_snippet):
    """Uses Google Gemini AI to generate comments for Python code."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"Analyze the given Python code and generate clear, beginner-friendly comments. - Use concise comments for simple code. - Provide detailed docstrings for functions and classes. - Explain complex logic with clarity. - Avoid redundancy and ensure readability.- Maintain comment density proportional to code complexity.Follow best coding practices and provide comments that add real value to code understanding.\n\n{code_snippet}")
    return response.text

