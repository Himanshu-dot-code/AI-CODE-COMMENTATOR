import sys
import os
import streamlit as st
import time

# Add project root to Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Get the directory where the current script is located
current_directory = os.path.dirname(__file__)

# Move one level up to the parent directory
parent_directory = os.path.join(current_directory, "..")

# Convert the parent directory path to an absolute path
absolute_parent_directory = os.path.abspath(parent_directory)

# Add the absolute parent directory path to Python's module search path
sys.path.append(absolute_parent_directory)


from comment_generator import generate_comments

# Streamlit UI
st.set_page_config(page_title="AI Code Commenter", page_icon="📝", layout="centered")

st.title("📝 AI Code Commenter")
st.write("Paste your Python code below, and Gemini AI will generate comments for you!")

# Text area for user input
code_input = st.text_area("Enter your Python code here:", height=300)

# Function to download commented code
def download_code(commented_code):
    st.download_button(label="📥 Download Commented Code",
                       data=commented_code,
                       file_name="commented_code.py",
                       mime="text/plain")

# Generate comments button
if st.button("🚀 Generate Comments"):
    if not code_input.strip():
        st.warning("⚠️ Please enter some Python code first!")
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
