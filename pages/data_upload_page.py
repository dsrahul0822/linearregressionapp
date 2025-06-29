# pages/data_upload_page.py

import streamlit as st
import pandas as pd

def app():
    st.title("📂 Upload Your Dataset")

    st.markdown("""
    Upload your dataset in either `.csv` or `.xlsx` format.  
    The uploaded data will be used for visualization, preprocessing, and model training.
    """)

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            
            st.session_state["raw_data"] = df  # Store in session state
            st.success("✅ File uploaded successfully!")
            st.dataframe(df.head())  # Show preview

        except Exception as e:
            st.error(f"❌ Error reading file: {e}")
    else:
        st.info("Please upload a file to begin.")
