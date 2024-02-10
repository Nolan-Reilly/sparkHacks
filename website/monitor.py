# Description: This file contains the code for monitoring the soil condition 
#of the SMART device and sending notification to the customer 
#if the soil condition is not within the threshold value.
from flask import Flask, render_template, request, redirect, url_for
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from threading import Thread
import time
from SMART import SMART

app = Flask(__name__)

@app.route('/monitor')
def send_notification(mail, body):
    # send email to customer
    
    message = Mail(
        from_email='micahbotbot@gmail.com',
        to_emails=mail,
        subject='SMART Notification- Soil Condition Warning!',
        html_content=f'<strong> {body} </strong>'
    )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

# Monitor soil condition
def monitor_soil_condition(SMART_Objs):
    while True:
        for smart_device in SMART_Objs:
            if smart_device.soil_temp > smart_device.soil_high_temp_threshold:
                message = f"{smart_device.Name} soil temperature is above the threshold value of {smart_device.soil_high_temp_threshold}!"
                send_notification(smart_device.Email,message)
            if smart_device.soil_temp < smart_device.soil_low_temp_threshold:
                message = f"{smart_device.Name} soil temperature is below the threshold value of {smart_device.soil_low_temp_threshold}!"
                send_notification(smart_device.Email,message)
            if smart_device.soil_moisture > smart_device.soil_high_moisture_threshold:
                message = f"{smart_device.Name} soil moisture is above the threshold value of {smart_device.soil_high_moisture_threshold}!"
                print("Monitoring soil condition...")
                print(message)
                send_notification(smart_device.Email,message)
            if smart_device.soil_moisture < smart_device.soil_low_moisture_threshold:
                message = f"{smart_device.Name} soil moisture is below the threshold value of {smart_device.soil_low_moisture_threshold}!"
                send_notification(smart_device.Email,message)
            if smart_device.soil_ph > smart_device.soil_high_ph_threshold:
                message = f"{smart_device.Name} soil pH is above the threshold value of {smart_device.soil_high_ph_threshold}!"
                send_notification(smart_device.Email,message)
            if smart_device.soil_ph < smart_device.soil_low_ph_threshold:
                message = f"{smart_device.Name} soil pH is below the threshold value of {smart_device.soil_low_ph_threshold}!"
                send_notification(smart_device.Email,message)
            time.sleep(3600)

def main():
    # Create SMART device
    f = open("/Users/pappi/VsCodes/sparkHacks/website/customer.txt", "r")
    str = f.read()
    list = []
    list = str.split('\n')

    SMART_Objs = []
    for i in list:
        if i != '':
            obj = i.split(',')
            smart_device = SMART(obj[0], obj[1], obj[2], int(obj[3]), int(obj[4]), int(obj[5]), int(obj[6]), int(obj[7]), int(obj[8]))
            SMART_Objs.append(smart_device)
    
    # Monitor soil condition

    # test the monitor_soil_condition function
    #smart_device.soil_moisture = 70
    monitor_thread = Thread(target=monitor_soil_condition, args=(SMART_Objs,))
    monitor_thread.daemon = False
    monitor_thread.start()

    #print("Monitoring soil condition...")

if __name__ == "__main__":
    main()