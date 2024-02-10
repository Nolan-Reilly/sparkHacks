from flask import Flask, render_template
from website import create_app
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

app = create_app()

# Matplotlib figure
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Data for each subplot
x_data = [[] for _ in range(3)]
y_data = [[] for _ in range(3)]
labels = ['Temperature', 'Soil Moisture', 'pH']

@app.route('/index')
def index():
    return render_template('index.html')

# Function to generate random data for each subplot
def generate_data():
    for i in range(3):
        x_data[i].append(len(x_data[i]) + 1)
        y_data[i].append(random.uniform(0, 1))

# Function to update plots
def update(frame):
    generate_data()
    for i in range(3):
        axs[i].clear()
        axs[i].plot(x_data[i], y_data[i])
        axs[i].set_title(labels[i])
        axs[i].set_xlabel('Time')
        axs[i].set_ylabel('Value')

def fix_phone_numbers(number):
    number.replace('-', '')
    number.replace('(', '')
    number.replace(')', '')
    number.replace(' ', '')

# Create animation
ani = FuncAnimation(fig, update, interval=1000)  # Update every 1 second

if __name__ == '__main__':
    app.run(debug=True)
