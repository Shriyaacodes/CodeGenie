import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from genie_utils2 import (
    format_code_prompt,
    format_explanation_prompt,
    format_debug_prompt,
    format_optimize_prompt,
    format_complexity_prompt,
    get_language_config,
    get_basic_syntax
)
import time

# Page config
st.set_page_config(
    page_title="CodeGenie 🧞‍♂️",
    page_icon="🧞‍♂️",
    layout="wide"
)

# Custom CSS for animations and background color
st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideIn {
        from { transform: translateX(-100%); }
        to { transform: translateX(0); }
    }

    .fade-in {
        animation: fadeIn 1s ease-in;
    }

    .slide-in {
        animation: slideIn 0.5s ease-out;
    }

    .stButton>button {
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: scale(1.05);
    }

    body {
        background: linear-gradient(135deg, #6B73FF 0%, #000DFF 100%);
        color: white;
    }

    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1E1E1E;
        color: white;
    }

    .stSelectbox>div>div>select {
        background-color: #1E1E1E;
        color: white;
    }

    .stSidebar {
        background-color: #1E1E1E;
    }

    .stMarkdown {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Configure API
def setup_gemini_api():
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        st.error("❌ No Google API key found. Please check your .env file")
        st.stop()

    try:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-pro')
    except Exception as e:
        st.error(f"❌ Error configuring Gemini API: {str(e)}")
        st.stop()

# Initialize model
model = setup_gemini_api()

# AI Functions
def generate_code(prompt, language):
    try:
        formatted_prompt = format_code_prompt(prompt, language)
        response = model.generate_content(formatted_prompt)
        return response.text
    except Exception as e:
        return f"Error generating code: {str(e)}"

def explain_code(code, language):
    try:
        formatted_prompt = format_explanation_prompt(code, language)
        response = model.generate_content(formatted_prompt)
        return response.text
    except Exception as e:
        return f"Error explaining code: {str(e)}"

def debug_code(code, language):
    try:
        formatted_prompt = format_debug_prompt(code, language)
        response = model.generate_content(formatted_prompt)
        return response.text
    except Exception as e:
        return f"Error debugging code: {str(e)}"

def optimize_code(code, language):
    try:
        formatted_prompt = format_optimize_prompt(code, language)
        response = model.generate_content(formatted_prompt)
        return response.text
    except Exception as e:
        return f"Error optimizing code: {str(e)}"

def estimate_complexity(code, language):
    try:
        formatted_prompt = format_complexity_prompt(code, language)
        response = model.generate_content(formatted_prompt)
        return response.text
    except Exception as e:
        return f"Error estimating complexity: {str(e)}"

# Loading animation
def show_loading_animation():
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    progress_bar.empty()

# UI Layout
def main():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.title("CodeGenie 🧞‍♂️")
    st.title("TeamName:Llamacoders")
    st.write("Your AI-powered coding assistant")
    st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown('<div class="slide-in">', unsafe_allow_html=True)
        st.header("Settings")
        mode = st.selectbox(
            "Choose Mode",
            ["Code Generation", "Code Explanation", "Code Debugging", "Code Optimization", "Basic Syntax", "Complexity Estimation"]
        )

        language = st.selectbox(
            "Select Language",
            ["Python", "Java", "C++", "C"]
        )

        # Show language-specific information
        config = get_language_config(language)
        with st.expander(f"{language} Information"):
            st.write(f"File extension: {config['file_ext']}")
            st.write("Common imports/includes:")
            for imp in config['common_imports']:
                st.code(imp, language=language.lower())

        st.markdown('</div>', unsafe_allow_html=True)

    # Main content
    if mode == "Code Generation":
        st.header("Code Generation")
        prompt = st.text_area(
            f"Describe the {language} code you want to generate:",
            height=150,
            placeholder=f"E.g., Create a function to calculate the Fibonacci sequence in {language}"
        )

        if st.button("Generate Code", type="primary"):
            if prompt:
                with st.spinner("🧞‍♂️ Generating code..."):
                    show_loading_animation()
                    generated_code = generate_code(prompt, language)
                    st.code(generated_code, language=language.lower())
            else:
                st.warning("Please enter a description first.")

    elif mode == "Code Explanation":
        st.header("Code Explanation")
        code = st.text_area(
            f"Paste the {language} code you want to explain:",
            height=150,
            placeholder=f"Paste your {language} code here..."
        )

        if st.button("Explain Code", type="primary"):
            if code:
                with st.spinner("🔍 Analyzing code..."):
                    show_loading_animation()
                    explanation = explain_code(code, language)
                    st.markdown(explanation)
            else:
                st.warning("Please enter some code first.")

    elif mode == "Code Debugging":
        st.header("Code Debugging")
        code = st.text_area(
            f"Paste the {language} code you want to debug:",
            height=150,
            placeholder=f"Paste your {language} code here..."
        )

        if st.button("Debug Code", type="primary"):
            if code:
                with st.spinner("🔧 Debugging code..."):
                    show_loading_animation()
                    debug_result = debug_code(code, language)
                    st.markdown(debug_result)
            else:
                st.warning("Please enter some code first.")

    elif mode == "Code Optimization":
        st.header("Code Optimization")
        code = st.text_area(
            f"Paste the {language} code you want to optimize:",
            height=150,
            placeholder=f"Paste your {language} code here..."
        )

        if st.button("Optimize Code", type="primary"):
            if code:
                with st.spinner("🔧 Optimizing code..."):
                    show_loading_animation()
                    optimized_code = optimize_code(code, language)
                    st.code(optimized_code, language=language.lower())
            else:
                st.warning("Please enter some code first.")

    elif mode == "Basic Syntax":
        st.header("Basic Syntax")
        basic_syntax = get_basic_syntax(language)
        st.code(basic_syntax, language=language.lower())

    elif mode == "Complexity Estimation":
        st.header("Complexity Estimation")
        code = st.text_area(
            f"Paste the {language} code you want to estimate complexity for:",
            height=150,
            placeholder=f"Paste your {language} code here..."
        )

        if st.button("Estimate Complexity", type="primary"):
            if code:
                with st.spinner("🔍 Estimating complexity..."):
                    show_loading_animation()
                    complexity_estimation = estimate_complexity(code, language)
                    st.markdown(complexity_estimation)
            else:
                st.warning("Please enter some code first.")

if __name__ == "__main__":
    main()
