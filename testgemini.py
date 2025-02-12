import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

try:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("Hello Gemini, how are you?")
    print("✅ API Test Successful!")
    print(response.text)
except Exception as e:
    print(f"❌ API Error: {e}")
