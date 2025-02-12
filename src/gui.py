import sys
import os
import streamlit as st

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from comment_generator import generate_comments


st.title("📝 AI Code Commenter")

st.write("Paste your Python code below, and Gemini AI will generate comments for you!")

# Text area for user input
code_input = st.text_area("Enter your Python code here", height=300)

if st.button("Generate Comments"):
    if not code_input.strip():
        st.warning("⚠️ Please enter some Python code first!")
    else:
        st.info("🔄 Generating AI-powered comments...")
        commented_code = generate_comments(code_input)
        st.success("✅ Code commented successfully!")
        st.code(commented_code, language="python")





