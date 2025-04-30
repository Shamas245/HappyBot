import streamlit as st
import os
import random
import requests  # To send HTTP requests to Piotrick's backend
from dotenv import load_dotenv
import streamlit.components.v1 as components

# ---- LOAD PIOTRICK API KEY ----
load_dotenv()
PIOTRICK_API_KEY = os.getenv("PIOTRICK_API_KEY")

# Piotrick's Chat API Link (example)
PIOTRICK_CHAT_API = "https://api.piotrick.com/chat"

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Ask AI - Kids Zone", page_icon="🎈", layout="wide")

# ---- STYLING ----
st.markdown("""
    <style>
    body {
        background-color: #FFEB3B;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .stTextInput>div>div>input {
        font-size: 24px;
        color: #FF6347;
        background-color: #FFF0F5;
        border: 2px solid #FF1493;
        border-radius: 12px;
        padding: 10px;
    }
    .stButton>button {
        font-size: 22px;
        background-color: #FF1493;
        color: white;
        border-radius: 15px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
    }
    .answer-box {
        font-size: 24px;
        color: #006400;
        background-color: #FFFACD;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .history-section {
        font-size: 22px;
        color: #FF6347;
    }
    h1, h3 {
        text-align: center;
        font-size: 40px;
        color: #FF1493;
    }
    .emoji {
        font-size: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.markdown("<h1>🎨 Welcome to HappyBot Fun Zone! 🎨</h1>", unsafe_allow_html=True)

# ---- FUN PROMPTS ----
fun_questions = [
    "How do I draw a cat?",
    "What is the biggest dinosaur?",
    "Why do stars twinkle?",
    "How do planes fly?",
    "Can animals talk?",
    "What makes popcorn pop?",
]

if "history" not in st.session_state:
    st.session_state.history = []

# ---- USER INPUT ----
col1, col2 = st.columns([3, 1])
with col1:
    question = st.text_input("Type your question here:", key="input", placeholder="Ask something fun!")
with col2:
    if st.button("🎲 Surprise!"):
        question = random.choice(fun_questions)
        st.session_state.input = question

# ---- CALL Piotrick CHAT API ----
def ask_piotrick_chat(question):
    try:
        headers = {'Authorization': f'Bearer {PIOTRICK_API_KEY}'}
        response = requests.post(PIOTRICK_CHAT_API, json={"question": question}, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Extract the answer from Piotrick's response
        answer = response.json().get("answer", "No answer provided")
        return answer
    except requests.exceptions.RequestException as e:
        return f"❌ Error: {e}"

# ---- HANDLE RESPONSE ----
if question:
    answer = ask_piotrick_chat(question)
    emoji = random.choice(["🐶", "🐱", "🦖", "🌟", "🎨", "🚀", "🧠", "🍿"])

    st.session_state.history.append((question, answer))

    st.markdown(
        f"<div class='answer-box'>"
        f"{emoji} <strong>{answer}</strong></div>", 
        unsafe_allow_html=True
    )

    components.html(f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{answer}");
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

# ---- HISTORY SECTION ----
if st.session_state.history:
    st.markdown("<h3 class='history-section'>🧠 Past Questions</h3>", unsafe_allow_html=True)
    for i, (q, a) in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.markdown(f"<b>{i}. Q:</b> {q}<br><b>→ A:</b> {a}", unsafe_allow_html=True)


        

    

       





 
