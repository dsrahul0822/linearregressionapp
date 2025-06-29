# pages/preprocessing_page.py

import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def app():
    st.title("🛠️ Data Preprocessing")

    if "raw_data" not in st.session_state:
        st.warning("⚠️ Please upload data first on the 'Upload Data' page.")
        return

    df = st.session_state["raw_data"].copy()
    st.dataframe(df.head())

    st.markdown("## 1️⃣ Missing Value Treatment")

    missing_option = st.radio("Choose strategy for numeric missing values", ["Mean", "Median"])
    cat_fill = st.checkbox("Fill missing values in categorical columns with mode")

    if st.button("Handle Missing Values"):
        # Numerical Columns
        num_cols = df.select_dtypes(include="number").columns
        for col in num_cols:
            if df[col].isnull().sum() > 0:
                if missing_option == "Mean":
                    df[col].fillna(df[col].mean(), inplace=True)
                else:
                    df[col].fillna(df[col].median(), inplace=True)

        # Categorical Columns
        if cat_fill:
            cat_cols = df.select_dtypes(include="object").columns
            for col in cat_cols:
                if df[col].isnull().sum() > 0:
                    df[col].fillna(df[col].mode()[0], inplace=True)

        st.success("✅ Missing values handled.")

    st.markdown("## 2️⃣ Outlier Treatment (Numerical Only)")

    if st.button("Remove Outliers Using IQR"):
        num_cols = df.select_dtypes(include="number").columns
        for col in num_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower) & (df[col] <= upper)]
        st.success("✅ Outliers removed using IQR.")

    st.markdown("## 3️⃣ Encoding")

    encoding_option = st.radio("Choose encoding method", ["Label Encoding (Ordinal)", "One-Hot Encoding (Nominal)"])

    if st.button("Apply Encoding"):
        cat_cols = df.select_dtypes(include="object").columns
        if encoding_option == "Label Encoding (Ordinal)":
            le = LabelEncoder()
            for col in cat_cols:
                df[col] = le.fit_transform(df[col])
            st.success("✅ Label Encoding applied.")
        else:
            df = pd.get_dummies(df, columns=cat_cols,dtype=int, drop_first=True)
            st.success("✅ One-Hot Encoding applied.")

    # Save cleaned data to session_state
    st.session_state["cleaned_data"] = df
    st.markdown("### ✅ Final Preprocessed Data Preview")
    st.dataframe(df.head())
