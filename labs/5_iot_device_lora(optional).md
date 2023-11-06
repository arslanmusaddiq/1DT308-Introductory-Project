# Optional - Getting started with the Pycom LoPy4

Note: This lab requires more allocated time than previous labs. You're using new hardware and there are many new integrations that is complex. Make sure you start as early as possible with this lab. **It might require an good amount of time.**

## Introduction

This assignment is all about getting to know the Atom development environment and to be able to run code on the pycom LoPy4 boards.

 * Install VSCode and PyMakr plugin
 * Connect LoPy4 to a computer
 * Connect to board in Atom and run code in console (on the hardware)
 * Upload files and run code on the microcontroller

## Rules
This task is going to be conducted individually.

## Ingredients

### Hardware
 * One LoPy4 board
 * One expansion board
 * One LoRa Antenna
 * One Micro-USB-Cable
 * One computer

### Software
 * **VSCode** programming environment, https://code.visualstudio.com/
 * **NodeJS** (current 15+), https://nodejs.org
 * **PyMakr** plugin is found via the extension tab in either IDE

(Note: The PyMakr plug-in exists also for Atom.io https://atom.io, if you get problems with VSCode this might be an option.)

### Knowledge components

 * configure your IDE
 * run code in the REPL https://docs.micropython.org/en/latest/reference/repl.html
 * upload and run code in files
 * print() strings to console https://www.w3schools.com/python/ref_func_print.asp
 * import statements http://wiki.micropython.org/Importing-Modules
 * for-loops with `range()` https://www.w3schools.com/python/python_for_loops.asp
 * `pycom.rgbled()` https://docs.pycom.io/tutorials/basic/rgbled/
 * `time.sleep()` https://docs.pycom.io/firmwareapi/micropython/utime/

## Steps
Complete each step before progressing to the next.

### Step 1. Hardware setup

![Setup for Getting Started](/images/1_hardware.png)
* Connect the LoPy4 on the expansion board. **Double check the direction, the LED should be in the same direction as the micro-USB connection.**
* Do not connect the expansion board to USB without the LoPy4 connected!
* Connect the Antenna to the Lopy 868MHz/915MHz (LoRa & Sigfox) antenna port. Be careful, and note that there are three connectors. Check this: https://docs.pycom.io/gettingstarted/connection/lopy4/
* Connect the usb-cable to both computer and expansion board


WARNING! "**Be gentle on hardware** when plugging and unplugging from the USB connector. Whilst the USB connector is soldered and is relatively strong, if it breaks  it can be very difficult to fix."

### Step 2. Software setup
 * Download and install VSCode
 * Install PyMakr plugin in VScode (using the Extensions manager)

### Step 3.
Make sure the LoPy board is connected to a computer with your IDE and PyMkr installed.

When the board is properly setup you can run micropython code directly on it using the pymakr-console. The output from the commands are sent to the computer so that you can interact with the board.

Write help() in the pycmkr console and press enter, this should give you output like in "Expected output 1"
```python
>>>help()
```

The help command prints some useful short-cuts you can use to for example interrupt a board that is stuck in a loop so that you can upload new code.

HINT! To reset the device
 * Click inside the PyMkr console then press CTRL+F
 * Press the reset-button on the LoPy4 device, next to the RGB LED!


#### Expected output. Run help() on board
![Goal state 1](/images/vscode-help.png)

### Step 4. Run custom code on the board
Create project folder in your IDE, with a main.py file and run it.

Using Atom, create a new file (main.py) with the following content but replace "Name 1" and "Name 2" with group members usernames

```python
print("Hello, Name 1, Name 2!")
```

Press upload ![Upload Button](/images/vscode-upload.png)

When the upload has completed the code willrun on the board and should produce the same output as in Expected output 2

#### Expected output 2.
![Goal state 2](/images/vscode-hello-world.png)

When you have completed this assignment you are expected to know:
 * How to setup a pycom-development environment with your IDE and the PyMakr plugin.
 * How to run python commands using the REPL console.
 * How to upload and run code in files using PyMakr

This task is examined using self-examination. Make sure you understand every step before you proceed.

# IoT device and LoRaWAN. Pycom.

Note: This lab requires more allocated time than previous labs. You're using new hardware and there are many new integrations that is complex. Make sure you start as early as possible with this lab. **It might require an good amount of time.**

The goal is to send sensor data from your IoT-device to the cloud over LoRaWAN. The data should be presented on an online dashboard.

In this assignment you may choose any sensors you like, a minumum of two different sensors are required. There are many to choose from, and this is a good opportunity to explore a range of different sensors that are provided in the lab.

## Knowledge

In this exercise you will learn the following.

- Find and read documentation for a specific sensor.
- Connect the sensor to a Microcontroller.
- Handle the data from the sensor.
- Send the data to the cloud over LoRaWAN.
- Visualise the data in a dashboard.

## Prerequisites

In this lab you will need to have a LoRaWAN compatible device. You will also need access to a LoRaWAN network. In both Växjö and Kalmar you have access to a LoRaWAN networks, The Things Network and Helium (not i Växjö at the moment). Both are free to use for students. Preferably you will start working with The Things Network as we have an indoor gateway in both our labs. 

- [LoRaWAN](https://www.thethingsnetwork.org/docs/lorawan/lorawan-overview.html)
- [Pybytes getting started](https://docs.pycom.io/pybytes/gettingstarted/)

*NOTE: Make sure you check that the sensor is utilising the correct voltage, either 3.3V or 5V.*

## Step 1, connecting sensors.

- Connect the sensors to the Microcontroller and display the data within the console.

# Step 2. Connecting to Cloud over LoRaWAN/TTN

Make sure you are in close range of the LoRaWAN Gateway (preferably in the same room).

**IMPORTANT The LoRaWAN protocol is not suitable for sending to much data, maximum 54 bytes per package. And not to often, no more than 1 message/minute. If you send too much data, the gateway will drop the data.**

In the first step you will need to connect your device to the cloud. There is a ready to use library and instructions for using the Pycom platform [Pybytes](https://docs.pycom.io/pybytes/gettingstarted/), that is a good starting point for this step.

Note, you will need to flash the correct firmware for utilising the Pybytes platform. Make sure you have updated your device with the latest Pybytes Firmware, instruction are found at the Pycom website, https://docs.pycom.io/updatefirmware/device/.

# Step 3. Visualising your signals

- Create a dashboard in the Pybytes platform visualising the sensor data from your device.
- The visualisation needs to be with graphical plots, and you need to put correct labels on the data.

Make sure you read the instructions on the platform, and make sure you understand the data. 

# Step 4. Register your device directly on The Things Network.

In steps 2-3 the backend of The Things Network is handled by the Pybytes platform, thus there is no insight from the user perspective on how the data is transferred over the network. In this exercise you will register your application directly on The Things Network and from there you will be able to see the data from your device in the TTN Console and push the data to another webservice.

In this step, the recommended approach is to start sending some dummy data manually. Prefereably using the REPL console. When sending data over LoRa you will need to take into account that you are actually sending binary data. That is, it is important that you encode the data in a binary format and are able to decode the data when recieved by your cloud application. In the tutorials below you will find an example of how to do this. Note, you are restricted to sending a maximum of 54 bytes due to the limitations of the protocol. Make sure you send as little data as possible, and not more often than once per minute.

An example as follows. If you have a temperature sensor that is measuring temperature between -50 and 50 degrees Celsius (or 0-3.3V). You will only need one byte to send the temperature. One byte represents eight bits, that is you have 256 combinations of values. So if you have a temperature of -50 degrees, you will send the value 0. If you have a temperature of 50 degrees, you will send the value 255. This needs to be implemented in your code on both the sending and the recieving side. But, start with just sending integers in the range of a byte. Also note that the standard way in programming is to represent a byte with Hexadecimals.

Tip: Use the IPhython terminal (or any Python interpreter REPL) to convert between different bases. `0b11111111` is the same as `255` in decimal. `0xFF` is the same as `255` in hexadecimal. When sending data over LoRaWAN using the LORA module, you will need to encode the data in a binary format.

You can find instructions on how to write your own Encoder and Decoder on this website: https://core-electronics.com.au/tutorials/encoding-and-decoding-payloads-on-the-things-network.html

A tutorial written by TA:s in the Applied IoT summer course: https://hackmd.io/5RbTAtCxTPu-hRi3k4p3dQ

The decoder on The Things Network is using JavaScript as the programming language. The decoder is a little script that converts the input to to be used by your application. Even without an encoder in The Things Network you will be able to see the binary data in the TTN Console.

Note that the European Freqency is 868 MHz, and the TTN server you are supposed to use is the European server, https://eu1.cloud.thethings.network/console/

- Open an account on The Things Network. https://www.thethingsnetwork.org/
- Register your device on the TTN Console. https://eu1.cloud.thethings.network/console/

You are going to use the LoRaWAN OTAA (Over the Air Authentication) method as this is the standard practice. Follow the instructions on the Pycom website for manually registering your device on the TTN console.

NOTE. Follow the instructions very carefully. You will need to extract the Device ID and the App ID from the TTN Console and put that in the code.

- https://docs.pycom.io/tutorials/networks/lora/lorawan-otaa/

In this first assignment you will be able to see the data that is sent to the TTN Console.

### Part 5. Visualising your data to an online platform

There are several ready to use IoT-platforms to use to visualise data. We recommend that you start working with one of the following which are free to use for students and also have a direct integration with The Things Console, for example Datacake, UBIDOTS STEM or Cayenne.

- https://www.thethingsindustries.com/docs/integrations/cloud-integrations/cayenne/
- https://www.thethingsindustries.com/docs/integrations/cloud-integrations/datacake/
- https://datacake.co/
- https://ubidots.com/stem/

## Examination

This assignment should be examined by a teacher/TA. 

Prepare for that by checking yourself so that you know the answers to the following questions:

- A graph of your data from the sensor. With correct labels.
- You should be able to change the value from your device by manipulating the physical sensor (that is, changing the temperature, or distance, etc). This should be reflected on the online platform.
- You should be able to explain the steps in the tutorial in a way that is understandable by a beginner.
