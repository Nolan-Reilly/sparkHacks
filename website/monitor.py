
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
def monitor_soil_condition(smart_device):
    while True:
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
    smart_device = SMART("SMART-1", "1234", "aolugbamila@gmail.com", 70, 40, 50, 20, 7, 5)
    # Monitor soil condition

    # test the monitor_soil_condition function
    #smart_device.soil_moisture = 70
    monitor_thread = Thread(target=monitor_soil_condition, args=(smart_device,))
    monitor_thread.daemon = False
    monitor_thread.start()

    #print("Monitoring soil condition...")

if __name__ == "__main__":
    main()