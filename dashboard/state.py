import streamlit as st

def init_state():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"  # default

def toggle_theme():
    st.session_state.theme = (
        "light" if st.session_state.theme == "dark" else "dark"
    )
