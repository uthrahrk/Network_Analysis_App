import streamlit as st

st.set_page_config(page_title="Network Traffic Analysis", layout="wide")

st.title("Network Traffic Analysis Web Application")
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- **[Packet Capture](./pages/01_Packet_Capture.py)**
- **[Data Processing](./pages/02_Data_Processing.py)**
- **[Data Analysis](./pages/03_Data_Analysis.py)**
- **[Data Visualization](./pages/04_Data_Visualization.py)**
- **[Report](./pages/05_Report.py)**
""")
