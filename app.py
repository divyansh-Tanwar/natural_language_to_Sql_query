from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import sqlite3
from google import genai  # NEW SDK

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))  # recommends this name

def get_gemini_response(question, prompt):
    resp = client.models.generate_content(
        model="gemini-2.5-flash",          # fast & cheap; use "gemini-2.5-pro" for higher quality
        contents=[prompt, question]
    )
    return resp.text

def fetch_data(query, db_name='students.db'):
    query = query.strip().replace("```sql", "").replace("```", "")
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

PROMPT = """You are a helpful assistant that translates natural language to SQL queries.
The database has a table named 'students' with the following columns:
id, name, age, grade, Class, section
Generate only the SQL query without any additional text or explanation.
"""

st.set_page_config(page_title="Natural Language to SQL Query", page_icon=":guardsman:", layout="wide")
st.header("Natural Language to SQL Query :guardsman:")
st.title("Convert your natural language questions into SQL queries and fetch data from the database.")

question = st.text_input("Enter your question here:")
if st.button("Submit") and question:
    with st.spinner("Generating SQL query..."):
        sql_query = get_gemini_response(question, PROMPT)
        st.subheader("Generated SQL Query:")
        st.code(sql_query, language='sql')
    with st.spinner("Fetching data from the database..."):
        try:
            results = fetch_data(sql_query)
            st.subheader("Query Results:" if results else "No results found.")
            for row in results:
                st.write(row)
        except Exception as e:
            st.error(f"An error occurred: {e}")
