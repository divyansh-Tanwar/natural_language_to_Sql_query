from dotenv import load_dotenv
load_dotenv () # take environment variables from .env.

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#configure the API key
genai.configure(api_key=os.getenv("API_KEY"))

#function to load google gemini model and provide sql query as response to the user input
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-1.5-turbo")
    response=model.generate_content([prompt,question])
    return response.text