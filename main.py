import streamlit as st
import time
from datetime import datetime

st.title("Simple Streamlit Clock")

# Create a placeholder for the clock
clock_placeholder = st.empty()

# Continuous update loop
while True:
    # Get the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Update the clock placeholder with the current time
    clock_placeholder.header(f"Current Time: {current_time}")
    
    # Wait for 1 second before updating again
    time.sleep(1)