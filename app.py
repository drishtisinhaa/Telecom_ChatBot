import streamlit as st
import requests

st.title("Dify Chatbot 🤖")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Ask something")

if st.button("Send") and query:
    st.session_state.chat_history.append(("You", query))

    headers = {
        "Authorization": "Bearer app-kQQrqwZPbPzE3uESrTdx2HBZ",  # Replace with your API key
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": {},
        "query": query,
        "response_mode": "blocking",
        "user": "user-123"
    }

    response = requests.post("https://api.dify.ai/v1/chat-messages", headers=headers, json=payload)
    answer = response.json().get("answer", "Error occurred.")
    st.session_state.chat_history.append(("Bot", answer))

for speaker, msg in st.session_state.chat_history:
    st.write(f"**{speaker}:** {msg}")
