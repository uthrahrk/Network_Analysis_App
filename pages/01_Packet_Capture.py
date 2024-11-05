import streamlit as st
from scapy.all import sniff
import threading

packet_data = []

def process_packet(packet):
    if IP in packet:
        packet_info = {
            'time': packet.time,
            'src': packet[IP].src,
            'dst': packet[IP].dst,
            'proto': packet[IP].proto,
        }
        packet_data.append(packet_info)

def start_capture():
    sniff(prn=process_packet, store=0, timeout=10)

st.title("Packet Capture")
st.write("Press the button below to start capturing packets.")

if st.button("Start Packet Capture"):
    st.write("Starting packet capture... Please wait.")
    threading.Thread(target=start_capture).start()
    st.success("Packet capture started! Click again to stop.")
