# Lab 4 - Connect traffic light to the internet
This assignment is a direct continuation of lab 2


---

## The use of AI in this lab:

[Hybrid learning bot](https://udify.app/chat/OCbFbncOAUXXherd)

---



## Rules
The task is to create a connected traffic light. This task task is done in groups of TWO students. Both students must be active during all steps of the assignment. You will need to collaborate with one other student and show that your IoT traffic light is communicating over the internet.

This assignment is done with a partner. 

ALERT! DURING THIS ASSIGNMENT NONE OF THE ARTIFACTS FROM THIS ASSIGNMENT MAY BE SHARED WITH OTHER STUDENT GROUPS. YOU MAY NOT ASK FOR HELP FROM OTHER STUDENT GROUPS, THINK OF THIS AS AN EXAM. 
YOU MAY GET HELP FROM A TEACHING ASSISTANT OR THE TEACHER.

# Task

Lab 2 has been a single MCU device (on its own) without any communication. In this assignment, we connect our MCU to the Internet over the WiFi and push information to an online server.

 * Simple Internet Of Things (IoT) scenario
 * Connect MCU to WiFi
 * Synchronize with the Cloud using MQTT

**Requirement**: The IoT traffic light should be connected to another light, and they should communicate.

This means that your two lights should communicate over the network, if one light is green the other should react accordingly.

## Knowledge Components

 * MQTT wikipedia https://en.wikipedia.org/wiki/MQTT
 * MQTT lib (there are others also) https://github.com/peterhinch/micropython-mqtt
 * alternative way of getting started with MQTT in micropython: https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

You may use the MQTT server in our own LNU server hosted at Digital Ocean, or `mqtt.iotlab.dev`, the DNS should point to `64.225.110.253`. Note, port 1883 and no encryption (TLS) is needed, username: `king`, password `arthur`.

* Use the MQTT Explorer to visualise and connect to the MQTT-server. [MQTT Explorer](http://mqtt-explorer.com/)

A good introduction to the MQTT protocol and usage is found here: https://youtu.be/3VXDPiDmSog

## Ingredients

### Hardware

- Microcontroller
- LEDs, resistors etc.
 
## Steps

### Step 1. Simple communication from the MCU over WiFi

To be able to communicate to the internet we need a WiFi connection. The amount of data sent is very little. You will need to use a network without a certificate, that means you cannot use EDUROAM. Use the `LNU-iot` LNU network or share your own from your phone. Note that the `LNU-iot` network is capped at 50 kb/s, so you will need to be patient and not send too much data. The password is `modermodemet`.

#### Script

Replace `WIFI_NETWORK_ID` with the sid of your network and `YOUR_WIFI_PASSWORD` with the passkey in the  code and make sure you can connect to your WIFI before continuing. 

Read the documentation on how to connect to WiFi. There are also some good guides on the [internet](https://www.cnx-software.com/2022/07/03/getting-started-with-wifi-on-raspberry-pi-pico-w-board/)

The script should eventually connect to WiFi and show "Connected to WiFi".

### Step 2. Connect to a MQTT server.

Use the LNU MQTT server (mqtt.iotlab.dev:1883). Optional is to use your own hosted local instance or a service online (example HiveMQ, eclipse.org or Adafruit, etc.). You can use any public MQTT server. Preferable you can use our own hosted MQTT server that we are running a VM at Digitalocean, that is running a Mosquitto MQTT. Note, the information will be accessible by all your peers that are using the same server (that applies to all public servers as well).

- `mqtt.iotlab.dev the DNS should point to 64.225.110.253, user=king, pass=arthur, port=1883`

Use the MQTT Explorer to visualise and connect to the MQTT-server. [MQTT Explorer](http://mqtt-explorer.com/)

#### Optional. Run your own MQTT server with Docker

*This setup is optional and considered as an advanced option.* You will need to install Docker.

https://hub.docker.com/_/eclipse-mosquitto

Using Docker locally, default config. Note, this will only be accessible within your own subnet if you don't open up ports in your router.

```bash
docker run -p 1883:1883 eclipse-mosquitto
```

#### Optional. Public Eclipse.org

Eclipse has an open mqtt.eclipse.org server that can be used for testing. Recommended if you just want to play around and see if things work. NOTE, this is open.

#### Optional. Adafruit IO account

Go to https://io.adafruit.com/  and sign up for a free account. Make note of your ADAFRUIT_USER_NAME since you need to use it in the following. When logged in, get the YOUR_AIO_KEY from https://io.adafruit.com/, click on "AIO Key"

 * `ADAFRUIT_USER_NAME`
 * `YOUR_AIO_KEY`

Note that you get the following in a free account.

 * 30 data points per minute
 * 30 days of data storage
 * 10 feeds
 * 5 dashboards

When exceeding the data points, you may get ECONNRESET.

### Step 3. subscription and publishing

Now its time to communicate using a mqtt-library through the WiFi network. First step is to verify that we got communication going in both directions.

Name your device and topic. `YOUR_GROUP/YOUR_DEVICE_NAME`

* Import the mqtt library.

![Thonny install MQTT](images/thonny-mqtt.png)

Then combine the following code with the WLAN code. Dont forget to change the needed string constants so that it uses your own account on your mqqt server.

Read the documentation on how to connect to a MQTT. https://github.com/peterhinch/micropython-mqtt/blob/master/mqtt_as/README.md#18-rp2-pico-w

*Note: There are other MQTT libraries available, but this one is popular and well documented. For instance, you can also find a micropython-mqtt lib when searching in the Thonny IDE for packages.*

### Step 4. Resilient connections

We suggest writing your code so that it can reset connections in case of errors. Thus, we want you to be able to be disconnected from both WiFi and the MQTT server and automatically reconnect again.

To accomplish this we suggest writing most of your code inside a while-True loop and have a branching statement (if-elif-else) that directs the application to different actions. 

Consider the following pseudocode:

```
Repeat Forever
 if WIFI is not connected
   connect to wifi
 else if adafruit IO is not connected
   connect to adafruit IO
 else if we have something to "publish"
   publish something
 else
    check for incomming messages from adafruit IO
```

Sometimes things may go wrong, thus, you need to add one or more try-except statements. In the following case, it has only one try-except that catches OSError inside the loop statement:


```python
while True:
    try:
        ... all the if-statements in pseudo code...
    except OSError as er:
        print("failed: " + str(er)) # give us some idea on what went wrong
        client.disconnect() # disconnect from adafruit IO to free resources
        adafruit_connected = False # mark us disconnected so we know that we should connect again 
        
```

## Examination

This assignment should be examined by a teacher/TA. 

Prepare for that by checking yourself so that you know the answers to the following questions:

* Explain how the traffic lights function, and how they communicate.
* How do you utilise the MQTT interrupt?
* What happens if the device loses connection to the MQTT server?
* What happens if the MQTT server is down?
* What is synchronised between the MQTT server and the device?
* Code should be DRY (no unnecessary repeated statements)
* Code should be divided into methods
 
### Check knowledge: 
 * Ask the group members individually two questions each of the above questions.

When completed you should ask a teacher/TA to check your setup and verify the questions above yourself.
