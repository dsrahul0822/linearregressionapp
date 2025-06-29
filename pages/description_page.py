# pages/description_page.py

import streamlit as st

def app():
    st.title("📘 Application Overview")

    st.markdown("""
    ### 🧠 Welcome to the Linear Regression Application!
    
    This application allows you to perform **end-to-end linear regression modeling** in an interactive and user-friendly environment.  
    Whether you're a beginner in Machine Learning or a professional looking to speed up your workflow, this tool is for you.

    #### 📌 What You Can Do Here:
    - 🔐 Secure Login to access the app
    - 📂 Upload CSV or Excel data
    - 📊 Visualize data using **Scatter** and **Bar Plots**
    - 🧼 Preprocess data:
        - Handle missing values
        - Treat outliers using IQR method
        - Encode categorical variables
    - 🤖 Train a Linear Regression model by selecting features & target
    - 💾 Save and reuse the model and features for prediction
    - 🔮 Make predictions with new values using the saved model

    #### 🛠 Technologies Used:
    - **Streamlit** for Web UI
    - **Pandas, NumPy** for data handling
    - **Matplotlib, Seaborn** for visualization
    - **Scikit-learn** for modeling
    - **Pickle / Joblib** for model persistence

    ---
    👉 Use the sidebar to start uploading your dataset and exploring features.
    """)
