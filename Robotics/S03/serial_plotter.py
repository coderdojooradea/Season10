import serial
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# Configuration
com_port = "COM3"  # Update this to the COM port your Arduino is connected to
baud_rate = 115200  # Update this to the baud rate you've set in your Arduino sketch

# Streamlit setup
st.title("Live MPU6050 Data")

# Create a pandas dataframe to hold the sensor values
data = pd.DataFrame(columns=["Ax", "Ay", "Az", "Gx", "Gy", "Gz"])

# Set up the plot
fig, ax = plt.subplots(2, 1, figsize=(5, 5))

# Streamlit component to display the plot
plot = st.pyplot(fig)

# Connect to the serial port
ser = serial.Serial(com_port, baud_rate, timeout=1)

# Main loop
while True:
    # Read a line from the serial port
    line = ser.readline().decode("utf-8").strip()
    
    # Split the line into individual values
    values = line.split(",")
    
    # Check if we have the correct number of values
    if len(values) == 6:
        # Convert the values to floats
        values = [float(v) for v in values]
        
        # Add the values to the dataframe
        data = data.append(pd.Series(values, index=data.columns), ignore_index=True)
        
        # Keep only the last 50 rows of data
        if len(data) > 50:
            data = data.iloc[-50:]
        
        # Update the plot
        for i in range(2):
            ax[i].cla()
            ax[i].plot(data.iloc[:, i * 3:i * 3 + 3])
            ax[i].legend(data.columns[i * 3:i * 3 + 3])
        
        plot.pyplot(fig)
        
    # Sleep for a short while to avoid overwhelming the serial port
    sleep(0.01)
