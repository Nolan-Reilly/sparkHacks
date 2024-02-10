import matplotlib.pyplot as plt
from datetime import datetime
import random
import threading
import time

# Import your SMART class
from website.SMART import SMART

# Function to generate random data for demonstration
def generate_random_data():
    while True:
        # Generate random values for soil moisture, temperature, and pH
        soil_moisture = random.uniform(0, 100)
        soil_temp = random.uniform(0, 50)
        soil_ph = random.uniform(4, 9)
        
        # Update SMART instance with random data
        smart_device.soil_moisture = soil_moisture
        smart_device.soil_temp = soil_temp
        smart_device.soil_ph = soil_ph
        
        # Append data to lists for plotting
        current_time = datetime.now()
        time_stamps.append(current_time)
        soil_moisture_data.append(soil_moisture)
        soil_temp_data.append(soil_temp)
        soil_ph_data.append(soil_ph)
        
        # Delay for demonstration purposes
        time.sleep(1)

# Create an instance of the SMART class
smart_device = SMART("DEMO", "device1", 50, 25, 6)

# Lists to store data for plotting
time_stamps = []
soil_moisture_data = []
soil_temp_data = []
soil_ph_data = []

# Start a thread to generate random data
data_thread = threading.Thread(target=generate_random_data)
data_thread.daemon = True
data_thread.start()

# Plotting function
def plot_data():
    while True:
        plt.figure(figsize=(10, 6))
        
        # Plot soil moisture
        plt.subplot(3, 1, 1)
        plt.plot(time_stamps, soil_moisture_data, 'b-')
        plt.title('Soil Moisture')
        plt.xlabel('Time')
        plt.ylabel('Moisture (%)')
        
        # Plot soil temperature
        plt.subplot(3, 1, 2)
        plt.plot(time_stamps, soil_temp_data, 'r-')
        plt.title('Soil Temperature')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')
        
        # Plot soil pH
        plt.subplot(3, 1, 3)
        plt.plot(time_stamps, soil_ph_data, 'g-')
        plt.title('Soil pH')
        plt.xlabel('Time')
        plt.ylabel('pH')
        
        plt.tight_layout()
        plt.show()
        
        # Update the plots every 10 seconds
        time.sleep(10)

# Start a thread to continuously plot data
plot_thread = threading.Thread(target=plot_data)
plot_thread.daemon = True
plot_thread.start()

# Keep the main thread alive
while True:
    time.sleep(1)
