# Lab 3 - Build Your Own IoT Dashboard and Logger

In this lab, you will create your own custom IoT dashboard and data logger system by integrating an MQTT broker, a Python MQTT client, and a simple web server.


You will collect, store, and visualize IoT sensor data from a Raspberry Pi Pico W using MQTT, CSV logging, and a Flask-based web dashboard.

Flask is a lightweight web framework for Python that allows you to build simple websites, web apps, and dashboards. It helps you easily create web servers that can display data, handle user input, and connect to databases or IoT devices. 

## Objectives

- Build a Python MQTT subscriber that saves incoming data to a CSV file.
- Build a Flask web application to visualize stored data.
- Stream live sensor values (Temperature & Humidity) to your web dashboard.

## Overview

The Raspberry Pi Pico W will publish sensor data (temperature and humidity) to an MQTT broker (Mosquitto).
A Python script will subscribe to these topics, log the data into a CSV file, and serve the data via a Flask web application with basic visualizations.

# Step 1: Set Up MQTT Broker (Mosquitto)

You should already have Mosquitto installed from Lab 2. If not, review Step 1 from Lab 2 to install and run Mosquitto on your machine.

start Mosquitto if installed:

```bash
brew services start mosquitto
```

# Step 2: Publish data from Pico to Mosquitto 

Use the same publishing code as in Lab 2, sending temperature and humidity readings to the following topics:
```bash
test/temperature
test/humidity
```

Make sure your Pico W is connected to the same network as your laptop. 

# Step 3: Create Python MQTT Subscriber and Logger, and Dashboard

Now, write a Python script that listens to the MQTT topics and logs the received data into a CSV file.

##  Install Required Python Packages (if not done already)

In your terminal or VSCode terminal:

```bash
pip install paho-mqtt
```
## Write Python script that listens to the MQTT topics

Write a Python script that listens to the MQTT topics and logs the received data into a CSV file.

In your script, you will need to give MQTT broker address. In this case, you are running Mosquitto on your laptop so you will need to use your laptop IP address. 

If your script is working fine, you will see an output like this: 

![Program output](../images/MQTT-Subscriber.png)

And you will see timestamp values in CSV file like this:

![Program output](../images/CSV-example.png)


## Build a Flask Web Dashboard

Now next step is to create a simple web dashboard that reads from the CSV file and shows the data.

## Create your webpage template 

Create a templates folder in the same directory and inside it, create index.html.

Make a fun dashboard ask you like. 

For example this is what I made: 

![Program output](../images/Dashboard-example.png)
