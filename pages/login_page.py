# pages/1_Login.py

import streamlit as st
from config.credentials import VALID_USERS

def app():
    st.title("🔐 Login Page")

    st.write("Please log in to access the application.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in VALID_USERS and VALID_USERS[username] == password:
            st.success(f"Welcome, {username}! Use the sidebar to navigate.")
            st.session_state["authenticated"] = True
        else:
            st.error("Invalid credentials. Please try again.")
