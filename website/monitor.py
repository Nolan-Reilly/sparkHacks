import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from threading import Thread
import time
from website.SMART import SMART

def send_notification(message):
    # send email to customer
    smtp_server = "smtp.gmail.com"
    sender_email= ""
    reciver_email= ""
    password = ""

    subject = "SMART Notification- Soil Condition Warning!"
    body = message

    email_message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, reciver_email, email_message)

def monitor_soil_condition(smart_device):
    while True:
        if smart_device.soil_temp > smart_device.soil_high_temp_threshold:
            message = f"{smart_device.Name} soil temperature is above the threshold value of {smart_device.soil_high_temp_threshold}!"
            send_notification(message)
        if smart_device.soil_temp < smart_device.soil_low_temp_threshold:
            message = f"{smart_device.Name} soil temperature is below the threshold value of {smart_device.soil_low_temp_threshold}!"
            send_notification(message)
        if smart_device.soil_moisture > smart_device.soil_high_moisture_threshold:
            message = f"{smart_device.Name} soil moisture is above the threshold value of {smart_device.soil_high_moisture_threshold}!"
            send_notification(message)
        if smart_device.soil_moisture < smart_device.soil_low_moisture_threshold:
            message = f"{smart_device.Name} soil moisture is below the threshold value of {smart_device.soil_low_moisture_threshold}!"
            send_notification(message)
        if smart_device.soil_ph > smart_device.soil_high_ph_threshold:
            message = f"{smart_device.Name} soil pH is above the threshold value of {smart_device.soil_high_ph_threshold}!"
            send_notification(message)
        if smart_device.soil_ph < smart_device.soil_low_ph_threshold:
            message = f"{smart_device.Name} soil pH is below the threshold value of {smart_device.soil_low_ph_threshold}!"
            send_notification(message)
        time.sleep(60)

def main():
    # Create SMART device
    smart_device = SMART("SMART-1", "1234", 70, 40, 50, 20, 7, 5)
    # Monitor soil condition
    monitor_thread = Thread(target=monitor_soil_condition, args=(smart_device,))
    monitor_thread.daemon = True
    monitor_thread.start()




if __name__ == "__main__":
    main()