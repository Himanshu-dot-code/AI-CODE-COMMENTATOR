import sys
import os
import streamlit as st
import time
from comment_generator import generate_comments

# Add project root to Python path
current_directory = os.path.dirname(__file__)
parent_directory = os.path.join(current_directory, "..")
absolute_parent_directory = os.path.abspath(parent_directory)
sys.path.append(absolute_parent_directory)

# Streamlit UI Configuration
st.set_page_config(page_title="AI Code Commenter", page_icon="📝", layout="centered")

st.title("📝 AI Code Commenter")
st.write("Paste your Python code below or upload a `.py` file, and Gemini AI will generate comments for you!")

# File Upload Option
uploaded_file = st.file_uploader("📂 Upload a Python file (.py)", type=["py"])

# Text area for user input
code_input = ""

if uploaded_file is not None:
    # Read uploaded file content
    code_input = uploaded_file.read().decode("utf-8")
    st.success("✅ File uploaded successfully! You can proceed with generating comments.")
    st.text_area("📄 Uploaded File Content:", code_input, height=300, disabled=True)
else:
    code_input = st.text_area("✍️ Enter your Python code here:", height=300)

# Function to download commented code
def download_code(commented_code):
    st.download_button(label="📥 Download Commented Code",
                       data=commented_code,
                       file_name="commented_code.py",
                       mime="text/plain")

# Generate comments button
if st.button("🚀 Generate Comments"):
    if not code_input.strip():
        st.warning("⚠️ Please enter some Python code or upload a file first!")
    else:
        with st.spinner("🔄 Generating AI-powered comments..."):
            time.sleep(1)  # Simulating processing time
            commented_code = generate_comments(code_input)

            if commented_code:
                st.success("✅ Code commented successfully!")
                st.code(commented_code, language="python")
                download_code(commented_code)
            else:
                st.error("❌ Failed to generate comments. Please try again.")
