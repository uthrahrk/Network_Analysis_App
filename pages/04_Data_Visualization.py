import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

st.title("Data Visualization")

if 'df' not in st.session_state:
    st.warning("No processed data available. Please process data first.")
else:
    df = st.session_state.df

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='proto', order=df['proto'].value_counts().index)
    plt.title('Packet Protocol Distribution')
    plt.xlabel('Protocol')
    plt.ylabel('Count')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    st.image(buf, caption='Packet Protocol Distribution')
