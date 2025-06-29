# app.py

import streamlit as st

# Import all pages
from pages import (
    login_page,
    description_page,
    data_upload_page,
    data_analysis_page,
    preprocessing_page,
    model_training_page,
    prediction_page
)

# Streamlit app config
st.set_page_config(page_title="Linear Regression App", layout="wide")

# Initialize session state for login
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Sidebar title
st.sidebar.title("📊 Linear Regression App")

# Show login if not authenticated
if not st.session_state["authenticated"]:
    login_page.app()

# Navigation after login
else:
    page = st.sidebar.selectbox(
        "Navigation",
        (
            "Description",
            "Upload Data",
            "Analyze Data",
            "Preprocessing",
            "Train Model",
            "Predict"
        )
    )

    # Page routing
    if page == "Description":
        description_page.app()

    elif page == "Upload Data":
        data_upload_page.app()

    elif page == "Analyze Data":
        data_analysis_page.app()

    elif page == "Preprocessing":
        preprocessing_page.app()

    elif page == "Train Model":
        model_training_page.app()

    elif page == "Predict":
        prediction_page.app()
