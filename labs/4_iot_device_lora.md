# IoT device and LoRaWAN

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

There are several ready to use IoT-platforms to use to visualise data. We recommend that you start working with one of the following which are free to use for students and also have a direct integration with The Things Console.




