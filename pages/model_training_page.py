# pages/model_training_page.py

import streamlit as st
import pandas as pd
import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def app():
    st.title("🤖 Model Training - Linear Regression")

    if "cleaned_data" not in st.session_state:
        st.warning("⚠️ Please preprocess data before training.")
        return

    df = st.session_state["cleaned_data"]

    st.markdown("### 🎯 Select your Target (Y) column")
    y_col = st.selectbox("Target Variable (Y)", df.columns)

    st.markdown("### 📊 Select your Feature columns (X)")
    feature_cols = st.multiselect("Feature Variables (X)", [col for col in df.columns if col != y_col])

    if st.button("Train Model"):
        if not feature_cols:
            st.error("❌ Please select at least one feature.")
            return

        # Split data
        X = df[feature_cols]
        y = df[y_col]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Evaluate
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)

        st.success("✅ Model trained successfully!")
        st.write(f"**R² Score on Test Data:** {r2:.4f}")

        # Save model and features
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, "models/linear_model.pkl")
        joblib.dump(feature_cols, "models/selected_features.pkl")

        st.success("📦 Model and features saved to `models/` folder.")
