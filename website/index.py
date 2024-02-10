from flask import Blueprint, request, render_template, url_for, redirect, flash
from flask_login import login_required
from .SMART import SMART
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from datetime import datetime
import random
import threading
import time
import base64
from io import BytesIO

index_blueprint = Blueprint('index', __name__)

# Lists to store data for plotting
time_stamps = []
soil_moisture_data = []
soil_temp_data = []
soil_ph_data = []
SMARTObj = None

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
        plt.savefig('website/static/plot.png')
        plt.close()
        
        
        # Update the plots every 10 seconds
        time.sleep(3)

def generate_random_data():
    global SMARTObj

    while True:
        # Generate random values for soil moisture, temperature, and pH
        soil_moisture = random.uniform(SMARTObj.soil_low_moisture_threshold, SMARTObj.soil_high_moisture_threshold)
        soil_temp = random.uniform(SMARTObj.soil_low_temp_threshold, SMARTObj.soil_high_temp_threshold)
        soil_ph = random.uniform(SMARTObj.soil_low_ph_threshold, SMARTObj.soil_high_ph_threshold)
        
        # Update SMART instance with random data
        SMARTObj.soil_moisture = soil_moisture
        SMARTObj.soil_temp = soil_temp
        SMARTObj.soil_ph = soil_ph
        
        # Append data to lists for plotting
        current_time = datetime.now()
        time_stamps.append(current_time)
        soil_moisture_data.append(soil_moisture)
        soil_temp_data.append(soil_temp)
        soil_ph_data.append(soil_ph)
        
        # Delay for demonstration purposes
        time.sleep(1)

@index_blueprint.route('/index', methods = ['GET', 'POST'])
# @login_required
def index():
    global SMARTObj
    if request.method == 'POST':
        name = request.form.get('deviceName')
        id = request.form.get('deviceId')
        email = request.form.get('email')
        highPh = request.form.get('highPH')
        lowPh = request.form.get('lowPH')
        highTemp = request.form.get('highTemp')
        lowTemp = request.form.get('lowTemp')
        highMoisture = request.form.get('highMoisture')
        lowMoisture = request.form.get('lowMoisture')
        SMARTObj = SMART(name, id, int(highTemp), int(lowTemp), int(highMoisture), 
                         int(lowMoisture), int(highPh), int(lowPh))
        print(SMARTObj._soil_low_moisture_threshold, SMARTObj._soil_high_moisture_threshold, 
              SMARTObj._soil_low_temp_threshold, SMARTObj._soil_high_temp_threshold, 
              SMARTObj._soil_low_ph_threshold, SMARTObj._soil_high_ph_threshold)
        return redirect(url_for('index.graphs'))
    return render_template('index.html')

@index_blueprint.route('/dashboard')
# @login_required
def graphs():
    global SMARTObj
    print(SMARTObj._soil_low_moisture_threshold, SMARTObj._soil_high_moisture_threshold, 
              SMARTObj._soil_low_temp_threshold, SMARTObj._soil_high_temp_threshold, 
              SMARTObj._soil_low_ph_threshold, SMARTObj._soil_high_ph_threshold)
    if(SMARTObj == None):
        flash("Initialize the SMART object first!")
        return redirect('index.index')
    data_thread = threading.Thread(target=generate_random_data)
    data_thread.daemon = True
    data_thread.start()
    plot_thread = threading.Thread(target=plot_data)
    plot_thread.daemon = True
    plot_thread.start()
    return render_template('dashboard.html')
