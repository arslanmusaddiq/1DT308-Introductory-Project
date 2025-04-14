# Lab 2 - Visualizing IoT Sensor Data using TIG Stack

In this lab, you will build a local or networked IoT data pipeline using the **TIG stack**:

- **Telegraf** to collect and parse MQTT data  
- **InfluxDB** to store the time-series data  
- **Grafana** to visualize the sensor values (Temperature & Humidity)

We will publish data using **Raspberry Pi Pico W** over MQTT, and then collect, store, and visualize it.

## Objectives

- Set up a TIG stack on your local machine or on a server.
- Connect Telegraf to your MQTT broker and configure it to collect sensor data.
- Store incoming temperature and humidity readings in InfluxDB.
- Use Grafana to build a real-time dashboard to display the data.

## Overview

The Raspberry Pi Pico W will read values from a **DHT11 sensor** and send them over MQTT.  
Telegraf will act as the MQTT subscriber and forward the readings to InfluxDB.  
Grafana will pull the time-series data from InfluxDB and visualize it in a dashboard.

# Step 1: Set Up MQTT Broker (Mosquitto)

In this first step, we will set up our own local MQTT broker using **Mosquitto**, which will facilitate communication between the Raspberry Pi Pico W (with the DHT11 sensor) and our local network.

## What is Mosquitto?
**Mosquitto** is an open-source MQTT broker that enables devices to communicate using the MQTT protocol. It allows devices (like your Raspberry Pi Pico W) to publish sensor data, and other applications (like Telegraf) to subscribe to those data streams.

## Why Use Mosquitto?
- **Full Control**: By setting up Mosquitto locally, you have full control over your MQTT communication.
- **Local Setup**: No need to rely on external cloud services (e.g., Adafruit IO) for communication.
- **TIG Stack Compatibility**: Mosquitto integrates seamlessly with Telegraf to collect and send data to InfluxDB.

## Instructions to Install Mosquitto

### Instructions to Install Mosquitto on macOS

### Option 1: Install Mosquitto Using Homebrew (macOS)
If you're using **macOS**, you can install Mosquitto using **Homebrew**:

1. **Install Homebrew**:
   If you don't already have Homebrew installed, open the Terminal and run the following command to install it:
  
```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. **Install Mosquitto**:

After Homebrew is installed, run the following command in your terminal to install Mosquitto:

```bash
brew install mosquitto
```

3. **Start Mosquitto**:
Once installed, you can start the Mosquitto broker by running:

```bash
brew services start mosquitto
```

This will start Mosquitto as a background service. To ensure it's running, use:

```bash
brew services list
```

This should show that Mosquitto is running.

3. **Test**:

Subscribe to a Topic (Terminal 1):


```bash
mosquitto_sub -t "test/topic" -v
```

Publish a Message to a Topic (Terminal 2):

```bash
mosquitto_pub -t 'test/topic' -m 'Hello from Mosquitto!'
```

If everything is set up correctly, Terminal 1 should display the message "test/topic Hello from Mosquitto!".

![Program output](../images/test-mosquitto.png)



# Step 2: Set up MQTT client for Mosquitto on Raspberry Pi Pico W

Instead of using Adafruit IO, you will use the Mosquitto broker you set up on your MacBook.

1. **Install the MQTT library (umqtt.simple) on your Raspberry Pi Pico W using**:

from umqtt.simple import MQTTClient

2. **Configure MQTT Credentials**:

You need to use the Mosquitto broker's address and port (usually localhost and 1883), but since your Raspberry Pi Pico W is on a different network, you will need to use the IP address of the MacBook where Mosquitto is running.

Update your MQTT credentials:

# Mosquitto broker details
MQTT_BROKER = "192.168.x.x"  # Replace with your MacBook IP address
MQTT_PORT = 1883  # Default MQTT port
MQTT_CLIENT_ID = "pico_w_sensor"  # Unique ID for the client
MQTT_TEMP_TOPIC = "test/temperature"  # Topic for temperature data
MQTT_HUMIDITY_TOPIC = "test/humidity"  # Topic for humidity data

You need to edit the Mosquitto configuration to allow remote devices (like Pico W) to connect.

By default, Mosquitto doesn’t load any config unless specified'

run 

```bash
nano ~/mosquitto.conf
```

Paste this into the file:

```bash
listener 1883
allow_anonymous true
```

Now run Mosquitto using your new config:

```bash
mosquitto -c ~/mosquitto.conf -v
```
You should see something like:

![Program output](../images/mosquitto-running.png)


Find your Mac’s IP address:

```bash
ipconfig getifaddr en0
```

Update Pico W Code

Open a new terminal and run:

```bash
mosquitto_sub -h localhost -t "test/temperature"

```
You will see temperature values like this: 


![Program output](../images/mosquitto-temp.png)

In another terminal:

```bash
mosquitto_sub -h localhost -t "test/humidity"

```
You will see humidity values like this: 

![Program output](../images/mosquitto-humidity.png)

Or you can subscribe to all topics with:

```bash
mosquitto_sub -h localhost -t "test/#"

```

you will see this output


![Program output](../images/mosquitto-all.png)

# Step 3: Set up a TIG Stack

I will continue from here...

