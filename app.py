import streamlit as st
from file_parser import parse_uploaded_file
from chat_memory import get_chat_history, add_to_chat
from llm_interface import get_llm_response

st.set_page_config(page_title="AI Chatbot with File Upload")

st.title("AI Chatbot")
uploaded_file = st.file_uploader(
    "Upload a file (PDF, DOCX, JSON)", type=["pdf", "docx", "json"]
)

if uploaded_file:
    file_text = parse_uploaded_file(uploaded_file)
    st.session_state.file_context = file_text

user_input = st.text_input("You:", key="input")
if user_input:
    messages = get_chat_history()
    context = st.session_state.get("file_context", "")
    if context:
        messages = [
            {
                "role": "system",
                "content": f"Use this file content for context:\n{context}",
            }
        ] + messages
    add_to_chat("user", user_input)
    response = get_llm_response(messages)
    add_to_chat("assistant", response)

# Display chat
for msg in get_chat_history():
    st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}")
