# test_gemini.py
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

st.title("API Test")

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv('GOOGLE_API_KEY')
st.write(f"API Key found: {'Yes' if api_key else 'No'}")

if not api_key:
    st.error("No API key found!")
else:
    try:
        # Configure API
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        # Test API
        response = model.generate_content("Say hello!")
        st.write("API Response:", response.text)
        
    except Exception as e:
        st.error(f"API Error: {str(e)}")