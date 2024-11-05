import streamlit as st
import pandas as pd

st.title("Report")

if 'df' not in st.session_state:
    st.warning("No processed data available. Please process data first.")
else:
    df = st.session_state.df
    st.write("Here is the report of the captured data:")
    st.write(df.describe())
    st.download_button("Download CSV", df.to_csv().encode('utf-8'), "network_traffic_data.csv", "text/csv")
