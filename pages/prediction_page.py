# pages/prediction_page.py

import streamlit as st
import pandas as pd
import joblib
import os

def app():
    st.title("🔮 Predict Using Trained Model")

    model_path = "models/linear_model.pkl"
    feature_path = "models/selected_features.pkl"

    if not os.path.exists(model_path) or not os.path.exists(feature_path):
        st.error("❌ Model or feature file not found. Please train the model first.")
        return

    # Load model and features
    model = joblib.load(model_path)
    features = joblib.load(feature_path)

    st.markdown("### 🧾 Enter values for each input feature:")
    input_data = {}

    for feature in features:
        input_data[feature] = st.number_input(f"{feature}", step=1.0)

    if st.button("Predict"):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
        st.success(f"📈 Predicted Value: **{prediction:.2f}**")
