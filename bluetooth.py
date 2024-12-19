import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Settings
x_data = []  # Time data
y_data = []  # Value data
start_time = time.time()  # Record start time for time axis

# Serial setup
ser = serial.Serial('COM7', baudrate=9600, timeout=1)
time.sleep(1)

# Create the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 10)  # Show the last 10 seconds of data
ax.set_ylim(0, 1000)  # Adjust value range based on your input

# Update function for animation
def update(frame):
    # Update plot with latest data
    line.set_data(x_data, y_data)
    ax.set_xlim(max(0, x_data[-1] - 10) if x_data else 0, x_data[-1] if x_data else 10)
    return line,

# Animate the plot (with manual triggering)
ani = FuncAnimation(fig, update, interval=50)

# Function to read and process serial data
while True:
    try:
        res = ser.readline()
        decoded = res.decode('utf-8').strip()  # Remove newline characters
        # Extract numerical value from the string
        numeric_part = ''.join(filter(str.isdigit, decoded))
        if numeric_part.isdigit():  # Ensure it's a valid number
            value = int(numeric_part)
            print(f"Value: {value}")  # Debugging print
            # Append new data
            current_time = time.time() - start_time
            x_data.append(current_time)
            y_data.append(value)
            # Remove old data to keep the graph within 10 seconds
            if current_time > 10:
                x_data.pop(0)
                y_data.pop(0)
    except Exception as e:
        print(f"Error: {e}")
        continue

    # Update the graph manually
    plt.pause(0.001)  # Short pause to allow graph to refresh

# Close the serial connection
ser.close()
