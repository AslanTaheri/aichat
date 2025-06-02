import streamlit as st


def get_chat_history():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    return st.session_state.chat_history


def add_to_chat(role, message):
    st.session_state.chat_history.append({"role": role, "content": message})
