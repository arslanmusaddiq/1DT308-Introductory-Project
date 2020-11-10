# The IoT Traffic Light

The previous tasks has been a single LoPy4 device (on its own) without any communication. In this final lab, we connect our LoPy4 to the Internet over the WiFi and push information to an online server.

 * Simple Internet Of Things (IoT) scenario
 * Connect LoPy4 on WiFi https://docs.pycom.io/tutorials/networkprotocols/wifisniffer/
 * Synchronize with the Cloud using MQTT

**Requirement**: The IoT traffic light should be connected to another light, and they should communicate.

This means that your two lights should communicate over the network, if one light is green the other should react accordingly.

## Rules

This task is going to be conducted in a group of TWO students. The group can be same as in Lab 3 and Lab 4. All students must be active during all steps of the assignment.

During the assignment you may discuss the assignment with students outside the group. You may help other groups but you may NOT do all steps for them, or share any code. Note that these rules change between assignments.

## Knowledge Components

 * MQTT wikipedia https://en.wikipedia.org/wiki/MQTT
 * MQTT pycom https://docs.pycom.io/tutorials/networkprotocols/mqtt/
 
## Ingredients

### Hardware

- One LoPy4 + Pycom Expansion board
- LEDs, resistors etc.

 
## Steps

### Step 1. Simple communication from Pycom over WiFi

To be able to communicate to io.adafruit.com we need a WiFi connection. The amount of data sent is very little; thus, easiest is to share network from a smartphone, or use a guest WiFi-network. Replace WIFI_NETWORK_ID with the sid of your network and YOUR_WIFI_PASSWORD with the passkey in the  code and make sure you can connect to your WIFI before continuing. Link https://docs.pycom.io/tutorials/networkprotocols/wifisniffer/
The script should eventually connect to WiFi and show "Connected to WiFi".

### Step 2. Connect to a MQTT server.

Either use the LNU MQTT server (iot-edu-lab.lnu.se), a local instance or a service online (example eclipse.org or Adafruit). 

#### LNU MQTT test-server

We are running a development setup Mosquitto MQTT server on LNU CSCloud. Note, the information will be accessible by all your peers that are using the same server.

- mqtt://iot-edu-lab.lnu.se, user=king,pass=arthur, port=1883

#### Run your own MQTT server with Docker

https://hub.docker.com/_/eclipse-mosquitto

Using Docker locally, default config. Note, this will only be accessible within your own subnet if you don't open up ports in your router.


```bash
docker run -p 1883:1883 eclipse-mosquitto
```

#### Public Eclipse.org

Eclipse has an open mqtt.eclipse.org server that can be used for testing. Recommended if you just want to play around and see if things work. NOTE, this is open.

#### Flespi.com

Free MQTT broker.

https://flespi.com/mqtt-broker

#### Adafruit IO account

Go to https://io.adafruit.com/  and sign up for a free account. Make note of your ADAFRUIT_USER_NAME since you need to use it in the following. When logged in, get the YOUR_AIO_KEY from https://io.adafruit.com/, click on "AIO Key"

 * ADAFRUIT_USER_NAME
 * YOUR_AIO_KEY

Note that you get the following in a free account.

 * 30 data points per minute
 * 30 days of data storage
 * 10 feeds
 * 5 dashboards

When exceeding the data points, you may get ECONNRESET.

### Step 3. subscription and publishing

Now its time to communicate using a mqtt-library to adafruit.io through the WiFi network. First step is to verify that we got communication going in both directions.

On https://io.adafruit.com/
* Create a feed "myfeed" at https://io.adafruit.com/ADAFRUIT_USER_NAME/feeds (replace ADAFRUIT_USER_NAME with your username )
* Create a dashboard:  https://io.adafruit.com/ADAFRUIT_USER_NAME/dashboards/pycom
 * Add a simple Toggle item to the dashboard that you connect to your feed.
* Import the mqtt library. Download [mqtt.py](https://github.com/pycom/pycom-libraries/blob/master/examples/mqtt/mqtt.py) and upload it to the LoPy4 device. 

Then combine the following code with the WLAN code. Dont forget to change the needed string constants so that it uses your own account.


### Step 4. Resilient connections

We suggest writing your code so that it can reset connections in case of errors. Thus, we want you to be able to be disconnected from both WiFi and Adafruit IO and automatically reconnect again.

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

