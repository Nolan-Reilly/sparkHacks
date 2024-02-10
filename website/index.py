from flask import Blueprint, request, render_template, url_for, redirect, flash, Response
from flask_login import login_required
from .SMART import SMART
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.animation import FuncAnimation, PillowWriter
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
timer = time.time()
fig, axs = plt.subplots(3, 1, figsize=(10, 10))
def plot_data():
    global timer
    timer = time.time()
    # Plot soil moisture
    axs[0].set_ylim(SMARTObj.soil_low_moisture_threshold, SMARTObj.soil_high_moisture_threshold)
    axs[0].xaxis.set_major_formatter(FormatStrFormatter('%g'))
    axs[0].plot(time_stamps, soil_moisture_data, 'b-o')
    axs[0].set_title('Soil Moisture')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Moisture (%)')
    
    # Plot soil temperature
    axs[1].set_ylim(SMARTObj.soil_low_temp_threshold, SMARTObj.soil_high_temp_threshold)
    axs[1].xaxis.set_major_formatter(FormatStrFormatter('%g'))
    axs[1].plot(time_stamps, soil_temp_data, 'r-o')
    axs[1].set_title('Soil Temperature')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Temperature (°C)')
    
    # Plot soil pH
    axs[2].set_ylim(SMARTObj.soil_low_ph_threshold, SMARTObj.soil_high_ph_threshold)
    axs[2].xaxis.set_major_formatter(FormatStrFormatter('%g'))
    axs[2].plot(time_stamps, soil_ph_data, 'g-o')
    axs[2].set_title('Soil pH')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('pH')

    fig.tight_layout()

    ani = FuncAnimation(fig, update_data, frames=range(40), interval=10000000)
    #writer = PillowWriter(fps=1)
    #ani.save('website/static/soil_data.gif', writer=writer)
    plt.close(fig)
    return ani

@index_blueprint.route('/get_graph')
def get_graph():
    ani = plot_data()
    return Response(ani.to_jshtml(fps=2, default_mode='once'), mimetype='text/html')

def update_data(frame):
    global SMARTObj
    generate_random_data()
    
    # Plot soil moisture
    axs[0].plot(time_stamps, soil_moisture_data, 'b-')
    axs[0].set_title('Soil Moisture')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Moisture (%)')
    
    # Plot soil temperature
    axs[1].plot(time_stamps, soil_temp_data, 'r-')
    axs[1].set_title('Soil Temperature')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Temperature (°C)')
    
    # Plot soil pH
    axs[2].plot(time_stamps, soil_ph_data, 'g-')
    axs[2].set_title('Soil pH')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('pH')


def generate_random_data():
    global SMARTObj
    # Generate random values for soil moisture, temperature, and pH
    soil_moisture = random.uniform(SMARTObj.soil_low_moisture_threshold, SMARTObj.soil_high_moisture_threshold)
    soil_temp = random.uniform(SMARTObj.soil_low_temp_threshold, SMARTObj.soil_high_temp_threshold)
    soil_ph = random.uniform(SMARTObj.soil_low_ph_threshold, SMARTObj.soil_high_ph_threshold)
    
    # Update SMART instance with random data
    SMARTObj.soil_moisture = soil_moisture
    SMARTObj.soil_temp = soil_temp
    SMARTObj.soil_ph = soil_ph
    
    # Append data to lists for plotting
    current_time = time.time() - timer
    time_stamps.append(current_time)
    soil_moisture_data.append(soil_moisture)
    soil_temp_data.append(soil_temp)
    soil_ph_data.append(soil_ph)

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
        SMARTObj = SMART(name, id, email, int(highTemp), int(lowTemp), int(highMoisture), 
                         int(lowMoisture), int(highPh), int(lowPh))
        write_to_file(SMARTObj)
        return redirect(url_for('index.graphs'))
    return render_template('index.html')

@index_blueprint.route('/dashboard')
# @login_required
def graphs():
    global SMARTObj
    if(SMARTObj == None):
        flash("Initialize the SMART object first!")
        return redirect('index.index')
    #plot_data()
    return render_template('dashboard.html')

#  Write to file
def write_to_file(SMARTObj):
    with open('website/customer.txt', 'a') as file:
        file.write(SMARTObj.Name + ',')
        file.write(SMARTObj.deviceID + ',')
        file.write(SMARTObj.Email + ',')
        file.write(str(SMARTObj.soil_high_temp_threshold) + ',')
        file.write(str(SMARTObj.soil_low_temp_threshold) + ',')
        file.write(str(SMARTObj.soil_high_moisture_threshold) + ',')
        file.write(str(SMARTObj.soil_low_moisture_threshold) + ',')
        file.write(str(SMARTObj.soil_high_ph_threshold) + ',')
        file.write(str(SMARTObj.soil_low_ph_threshold) + ',')
