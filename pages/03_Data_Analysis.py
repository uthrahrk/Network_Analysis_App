import streamlit as st
import pandas as pd

st.title("Data Analysis")

if 'df' not in st.session_state:
    st.warning("No processed data available. Please process data first.")
else:
    df = st.session_state.df
    st.write("Here is the processed data:")
    st.write(df)
    
    # Example analysis (packet count)
    st.write("Packet count by protocol:")
    packet_count = df['proto'].value_counts()
    st.bar_chart(packet_count)
