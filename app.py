import streamlit as st
import requests
import pandas as pd

st.title("CSV Insights DashBoard")

file = st.file_uploader(label="Upload your csv file here")

if st.button(label="Upload"):
    
    with st.spinner("Analyzing...... "):
        response = requests.post("https://smart-csv-insights-dashboard.onrender.com/analyze-csv", files={"file": (file.name, file, "text/csv")})

        if response.status_code == 200:
            data = response.json()

            # Top Metrics
            col1, col2 = st.columns(2)
            col1.metric("Rows", data["rows"])
            col2.metric("Columns", data["columns"])

            # Column Names
            st.subheader("Column Names")
            st.write(data["column_names"])

            # Missing Values
            st.subheader("Missing Values")
            missing_df = pd.DataFrame(
                list(data["missing_values"].items()),
                columns=["Column", "Missing Count"]
            )
            st.dataframe(missing_df)

            # Statistics
            st.subheader("Statistics")
            stats_df = pd.DataFrame(data["statistics"])
            st.dataframe(stats_df)

        else:
            st.error("Error from API")