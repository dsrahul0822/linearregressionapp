# pages/data_analysis_page.py

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("📊 Data Analysis")

    if "raw_data" not in st.session_state:
        st.warning("⚠️ Please upload data first on the 'Upload Data' page.")
        return

    df = st.session_state["raw_data"]
    st.markdown("### 👇 Select chart type and columns to visualize")

    plot_type = st.selectbox("Choose chart type", ["Scatter Plot", "Bar Plot"])

    if plot_type == "Scatter Plot":
        num_cols = df.select_dtypes(include="number").columns.tolist()
        if len(num_cols) < 2:
            st.error("Need at least two numerical columns for scatter plot.")
            return
        
        x_axis = st.selectbox("X-axis", num_cols)
        y_axis = st.selectbox("Y-axis", [col for col in num_cols if col != x_axis])

        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Bar Plot":
        cat_cols = df.select_dtypes(include="object").columns.tolist()
        num_cols = df.select_dtypes(include="number").columns.tolist()

        if not cat_cols or not num_cols:
            st.error("Need at least one categorical and one numerical column.")
            return

        category = st.selectbox("Categorical (X-axis)", cat_cols)
        value = st.selectbox("Numerical (Y-axis)", num_cols)

        fig, ax = plt.subplots()
        sns.barplot(x=category, y=value, data=df, ax=ax)
        st.pyplot(fig)
