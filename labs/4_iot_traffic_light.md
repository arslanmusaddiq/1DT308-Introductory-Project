# The Traffic Light

In this assignment we aim to work with more code and components. We apply the things we have learned so far, more of the same but with less instructions and guidance.

## Rules

This task is going to be conducted in a group of TWO students. The group can be the same for Lab 3 (previous project). Both students must be active during all steps of the assignment.

ALERT! DURING THIS ASSIGNMENT NONE OF THE ARTIFACTS FROM THIS ASSIGNMENT MAY BE SHARED WITH OTHER STUDENT GROUPS. YOU MAY NOT ASK FOR HELP FROM OTHER STUDENT GROUPS, THINK OF THIS AS AN EXAM. 
YOU MAY GET HELP FROM A TEACHING ASSISTANT OR THE TEACHER.

## Knowledge Components
 * Apply knowledge components from previous assignments. 

## Ingredients

### Hardware
 * Six LED's with resistors (2 x Red, 2 x yellow, 2 x green)
 * Buzzer with resistor
 * Button with resistor
 
## Steps

### Step 1. Build Check all components

We are going to build a traffic light that can sit next to a pedestrian crossing. Thus, it has three LEDs for traffic, two LEDs for the pedestrian crossing, and a button circuit used by pedestrians to ask for green light. 

Build one circuit at a time and test before continuing to the next
* a traffic light (Red, Yellow, Green - LEDs with resistors), 
* a pedestrian crossing light (Red, Green - LEDs with resistors) and a Buzzer
* a pedestrian button (button circuit and Yellow LED with resistors). The LED is ON when the button has been pressed and is turned off when green LED is ON for the pedestrians.

To test all components: 
When all hardware has been set-up, write a routine that waits for a button press, then turn ON each LED, and finally beeps the buzzer before waiting again. Note that all pins cannot be used for output. 

### Step 2. Traffic light with pedestrian crossing

We are now going to model a pedestrian crossing light with Python code. The traffic light is normally Green.
The button should represent a pedestrian looking to cross the street. When pressed, the Yellow button-LED should light up, traffic is given Red light (after a while), and pedestrians should be allowed passage before the traffic light turns Green again.

We can model this by defining different states, each defined in its own function:

#### States:

 * TRAFFIC GO: Traffic Green LED, Pedestrian Red LED, lasts for at minimum of 4 seconds, but continue longer if not interrupted by button presses.
 * TRAFFIC SOON STOP: Traffic Yellow LED, Pedestrian Red LED, lasts 2 seconds
 * ALL STOP: Traffic Red LED, Pedestrian Red LED, lasts 1 second
 * PEDESTRIAN GO: Traffic Red LED, Pedestrian Green LED, Buzzer speedy Tick sounds, lasts 3 seconds
 * PEDESTRIAN SOON STOP: Traffic Red LED, Pedestrian Green LED, Slower Tick Sounds, lasts 1 second
 * TRAFFIC GET READY: Traffic Red LED + Traffic Yellow LED, Pedestrian Red LED, lasts 1 second

 ![State transitions](../images/states.png)

You can now write a main loop that normally runs the TRAFFIC GO state-function if nothing happens. If the button is pressed a boolean variable is set and the main loops starts calling the different state-methods in order.

### Examination
The traffic light should work like described above and go back to Green after having stepped through all the states. The exact waiting time is not as important as each of the states being reached and this should be repeatable.

#### Check code
 * Code should be DRY (no unnecessary repeated statements)
 * Code should be divided into methods / functions
 * Method names should represent the content (for example state names)
 


The previous tasks has been a single LoPy4 device (on its own) without any communication. In this final lab, we connect our LoPy4 to the Internet over the WiFi and push information to an online server.

 * Simple Internet Of Things (IoT) scenario
 * Connect LoPy4 on WiFi https://docs.pycom.io/firmwareapi/pycom/network/wlan/
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

To be able to communicate to io.adafruit.com we need a WiFi connection. The amount of data sent is very little; thus, easiest is to share network from a smartphone, or use a guest WiFi-network. 

To sniff for Wifi: Link https://docs.pycom.io/tutorials/networkprotocols/wifisniffer/

#### Script
Replace WIFI_NETWORK_ID with the sid of your network and YOUR_WIFI_PASSWORD with the passkey in the  code and make sure you can connect to your WIFI before continuing. 

```python
from network import WLAN
wlan = WLAN(mode=WLAN.STA)
wlan.connect("WIFI_NETWORK_ID", auth=(WLAN.WPA2, "YOUR_WIFI_PASSWORD"), timeout=5000)
while not wlan.isconnected():
    machine.idle()
print("Connected to WiFi")
```


The script should eventually connect to WiFi and show "Connected to WiFi".



### Step 2. Connect to a MQTT server.

Either use the LNU MQTT server (iot-edu-lab.lnu.se), a local instance or a service online (example eclipse.org or Adafruit). 

#### Option 1. LNU MQTT test-server

We are running a development setup Mosquitto MQTT server on LNU CSCloud. Note, the information will be accessible by all your peers that are using the same server.

- mqtt://iot-edu-lab.lnu.se, user=king,pass=arthur, port=1883

#### Option 2. Run your own MQTT server with Docker

https://hub.docker.com/_/eclipse-mosquitto

Using Docker locally, default config. Note, this will only be accessible within your own subnet if you don't open up ports in your router.


```bash
docker run -p 1883:1883 eclipse-mosquitto
```

#### Option 3. Public Eclipse.org

Eclipse has an open mqtt.eclipse.org server that can be used for testing. Recommended if you just want to play around and see if things work. NOTE, this is open.

#### Option 4. Flespi.com

Free MQTT broker.

https://flespi.com/mqtt-broker

#### Option 5. Adafruit IO account

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
Assumes Option 5, but works similarly for other Options but you need to find out how yourself.

Now its time to communicate using a mqtt-library to adafruit.io through the WiFi network. First step is to verify that we got communication going in both directions.

On https://io.adafruit.com/
* Create a feed "myfeed" at https://io.adafruit.com/ADAFRUIT_USER_NAME/feeds (replace ADAFRUIT_USER_NAME with your username )
* Create a dashboard:  https://io.adafruit.com/ADAFRUIT_USER_NAME/dashboards/pycom
 * Add a simple Toggle item to the dashboard that you connect to your feed.
* Import the mqtt library. Download [mqtt.py](https://github.com/pycom/pycom-libraries/blob/master/examples/mqtt/mqtt.py) and upload it to the LoPy4 device. 

Then combine the following code with the WLAN code. Dont forget to change the needed string constants so that it uses your own account on your mqqt server.
```python
#Before WLAN
from mqtt import MQTTClient
import machine
import time
#After WLAN connection
def sub_cb(topic, msg):
   print(msg)
client = MQTTClient("device_id", "io.adafruit.com",user="ADAFRUIT_USER_NAME", password="YOUR_AIO_KEY", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="ADAFRUIT_USER_NAME/feeds/myfeed")
while True:
    print("Sending ON")
    client.publish(topic="ADAFRUIT_USER_NAME/feeds/myfeed", msg="ON")
    time.sleep(3)
    print("Sending OFF")
    client.publish(topic="ADAFRUIT_USER_NAME/feeds/myfeed", msg="OFF")
    client.check_msg()
    time.sleep(3)
```

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


 
