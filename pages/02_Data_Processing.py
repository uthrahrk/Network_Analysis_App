import streamlit as st
import pandas as pd

st.title("Data Processing")
if 'packet_data' not in st.session_state:
    st.session_state.packet_data = []

if st.button("Process Data"):
    if not st.session_state.packet_data:
        st.warning("No packet data to process. Please capture packets first.")
    else:
        df = pd.DataFrame(st.session_state.packet_data)
        st.session_state.df = df
        st.success("Data processed successfully!")
        st.write(df.head())
