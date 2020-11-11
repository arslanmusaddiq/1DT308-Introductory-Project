# Connectivity


## Agenda

1. Connect to WiFi
2. Connect to MQTT
3. Sensor setup (Env. sensor, serial bus I2C)
4. Pub/sub to another device


## Basics ...


- Official homepage: http://micropython.org/
- Documentation: http://docs.micropython.org/en/latest/
- PyCom docs: https://docs.pycom.io/ (MicroPython + Pycoms libs)
- Adafruit has CircuitPython (a fork of MicroPython)
- Firmware to the PyCom device.
    - Legacy, not containing Pybytes library. Older.
    - Flash with Pybytes, even not using Pybytes.
    - Contains `pybytes_config.json`.
    - Provisioning from Pybytes homepage. May interfere with you own code.

Disable Pybytes on boot!

```
pybytes_on_boot(False)
```

- MicroPython is designed to work on small micro-controller platforms.
- There are learning material out there. [MicroPython series by unexpected maker](https://youtu.be/5W3WvXAmDJc)
- You must first write your code and load it onto the board.
- Boards have a flash drive storage. You can copy your Python file(s) to this drive for execution at boot time. `boot.py` and `main.py`
- The MicroPython console is called the run, evaluate, print loop, or **REPL**. Makes it easy to get started and to debug (remove errors).
- **R**un, **E**valuate, **P**rint, **L**oop (REPL)
![REPL](https://i.imgur.com/vBZcjG5.png)
REPL Interface in Atom.io

#### Projects Atom/VSCode and PyMakr, USB, WiFi, 

- **Projects**, you need to work in projects.
- Do not use PyBytes **for coding**! No debug. Inconsistent connection.
- FW of Expansion board. If you have no problems uploading, it should be OK.



### WiFi

https://docs.pycom.io/firmwareapi/pycom/network/wlan/

Code examples:

- Scan networks
- Connect, dynamic IP + static
- `boot.py` / `main.py`
- WiFi-sniffer


## MQTT Basics

- MQTT
	- MQTT Servers
		- MQTT test-server. `iot-edu-lab.lnu.se`, user=king,pass=arthur, port=1883 (poor security)
		- mqtt.eclipse.org (note, public no security!)
		- Local installation with Docker
		- Adafruit, https://learn.adafruit.com/adafruit-io/mqtt-api
		- Adafruit dashboard, https://io.adafruit.com/frahlg/dashboards
	- MQTT Explorer (Mac, Win, Linux), several alt. available.
	- http://mqtt-explorer.com
- Pub/sub


https://www.hivemq.com/mqtt-essentials/
https://mqtt.org/faq/

![](https://pycom.io/wp-content/uploads/2020/03/mqtt_publisher_subscriber-hackster_zPsybZXuck.png-Fj6teRB8V7yljpeg)

The MQTT protocol was invented in 1999. They needed a protocol for minimal battery loss and minimal bandwidth to connect with oil pipelines via satellite. The two inventors specified several requirements for the future protocol.

- Simple implementation
- Quality of Service data delivery
- Lightweight and bandwidth efficient
- Data agnostic
- Continuous session awareness


#### What is MQTT

MQTT stands for **MQ Telemetry Transport**. It is a publish/subscribe, extremely simple and lightweight messaging protocol, designed for **constrained** devices and **low-bandwidth, high-latency or unreliable networks**. The design principles are to minimise network bandwidth and device resource requirements whilst also attempting to ensure reliability and some degree of assurance of delivery. These principles also turn out to make the protocol ideal of the emerging “machine-to-machine” (M2M) or “Internet of Things” world of connected devices, and for mobile applications where bandwidth and battery power are at a premium.

#### MQTT security
You can pass a user name and password with an MQTT packet in V3.1 of the protocol. Encryption across the network can be handled with **SSL**, independently of the MQTT protocol itself. Additional security can be added by an application encrypting data that it sends and receives, but this is not something built-in to the protocol, in order to keep it simple and lightweight.


- Please use `iot-edu-lab.lnu.se` for testing.
- List of [public MQTT brokers](https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/). No need of starting one on your own computer.


### Publish/Subscribe

A device can publish a message on a topic, or it can be subscribed to a particular topic.

The most important aspect of pub/sub is the decoupling of the publisher of the message from the recipient (subscriber). This decoupling has several dimensions:

- Space decoupling: Publisher and subscriber do not need to know each other (for example, no exchange of IP address and port).
- Time decoupling: Publisher and subscriber do not need to run at the same time.
- Synchronization decoupling: Operations on both components do not need to be interrupted during publishing or receiving.

### Topics


### Topics

Represented with strings separated by a forward slash

- at least 1 character and that the topic string permits empty spaces. Topics are case-sensitive. 

 Wildcards:

- Single Level: +
 	- factory_floor_1/+/sensor (that would catch all sensors on floor one... )
- Multi level: #
 	- factory_floor_1/# (catches all .)
- $ symbol for internal statistics (broker)
	- $SYS/broker/clients/connected
	- $SYS/broker/clients/disconnected
	- $SYS/broker/clients/total
	- $SYS/broker/messages/sent
	- $SYS/broker/uptime


- + can be used as a wildcard for a single level of hierarchy. It could be used with the topic above to get information on all computers and hard drives as follows:

`sensors/+/temperature/+`

As another example, for a topic of "a/b/c/d", the following example subscriptions will match:

```
a/b/c/d
+/b/c/d
a/+/c/d
a/+/+/d
+/+/+/+
```

'#' can be used as a wildcard for all remaining levels of hierarchy. This means that it must be the final character in a subscription. With a topic of "a/b/c/d", the following example subscriptions will match:

```
a/b/c/d
#
a/#
a/b/#
a/b/c/#
+/b/c/#
```


#### Quality of Service
MQTT defines three levels of Quality of Service (QoS). The QoS defines how hard the broker/client will try to ensure that a message is received. Messages may be sent at any QoS level, and clients may attempt to subscribe to topics at any QoS level. This means that the client chooses the maximum QoS it will receive. For example, if a message is published at QoS 2 and a client is subscribed with QoS 0, the message will be delivered to that client with QoS 0. If a second client is also subscribed to the same topic, but with QoS 2, then it will receive the same message but with QoS 2. For a second example, if a client is subscribed with QoS 2 and a message is published on QoS 0, the client will receive it on QoS 0.

**Higher levels of QoS are more reliable, but involve higher latency and have higher bandwidth requirements.**

**0:** The broker/client will deliver the message once, with no confirmation.
**1:** The broker/client will deliver the message at least once, with confirmation required.
**2:** The broker/client will deliver the message exactly once by using a four step handshake.

[https://mosquitto.org/man/mqtt-7.html
](https://mosquitto.org/man/mqtt-7.html)

**Retain**

The broker stores the last retained message and the corresponding QoS for that topic.
A retained message makes sense when you want newly-connected subscribers to receive messages immediately

Last Will and Testament
-  feature to notify other clients about an ungracefully disconnected client

#### JSON (JavaScript Object Notation)

JSON is a lightweight data-interchange format. It is easy for humans to read and write.


```python
c.publish(topic_pub,'{"office_sensor": {"co2":' + str(co2) +
                          ',"voc":'+ str(voc) +
                          ',"bmp P":' + str(bmp_P) +
                          ',"bmp temp":' + str(bmp_T) +
                          ',"dht temp":' + str(dht_T) +
                          ',"dht RH":' + str(dht_RH) +
                          '}}')
```

```json
{"office_sensor": {"co2": 412,
                   "voc": 30,
                   "bmp P": 1012,
                   "bmp temp": 23,
                   "dht temp": 24,
                   "dht RH": 42}}
```


### Best practices (Cred: HiveMQ)

- Never use a leading forward slash
A leading forward slash is permitted in MQTT. For example, /myhome/groundfloor/livingroom. However, the leading forward slash introduces an unnecessary topic level with a zero character at the front. The zero does not provide any benefit and often leads to confusion.
 
- Never use spaces in a topic
- Keep the topic short and concise
- Use only ASCII characters, avoid non printable characters
- Embed a unique identifier or the Client Id into the topic
- Don’t subscribe to #
- Use specific topics, not general ones

### Broker

The server that recieves and publishes the messages between all devices. The broker is primarily responsible for receiving all messages, filtering the messages, decide who is interested in them and then publishing the message to all subscribed clients. Several servers exists, Eclipse MQTT, HiveMQ. 

### I2C and CCS811 sensor

- Sensor setup Environmental CS811
	- Sensor communication. I2C, library CCS811.

https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol

![](https://www.circuitbasics.com/wp-content/uploads/2016/01/Introduction-to-I2C-Single-Master-Single-Slave.png)

Many sensors communicate with a serial communication protocol.

- SDA (Serial Data) – The line for the master and slave to send and receive data.
- SCL (Serial Clock) – The line that carries the clock signal.

I2C is a serial communication protocol, so data is transferred bit by bit along a single wire (the SDA line).

- Only uses two wires
- Supports multiple masters and multiple slaves

Not to be confused with 
[SPI (Serial Peripheral Interface)](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol). 



### If time permits ..


### Webhooks REST

- User-defined callback over HTTP
    - https://requestbin.com/
    - cURL or Postman (Chrome)
- Because webhooks use HTTP, they can be integrated into web services without adding new infrastructure.
- A POST request being the method that allows the transfer of information in the body of the request through HTTP.
- Include a body to the request, it's usually a simple JSON object.
- JSON, https://www.json.org/json-en.html

### Pybytes

- PyBytes intro



## Additional material

- HTTP requests. https://www.codecademy.com/articles/http-requests

### Pybytes
Basic setup https://youtu.be/2THov7819GA

### Intro to IoT
https://youtu.be/7s19AwCSNmg

### MQTT
https://youtu.be/Kq0OLK08tqQ

### REST API
https://youtu.be/RQX3m0xtlaM

## TTN Ubidots
https://youtu.be/pgO7M18xgB0

#### Online services Platforms

https://hackmd.io/@lnu-iot/cloud-platforms

- [Pybytes](https://pybytes.pycom.io/)
- [Adafriut IO](https://io.adafruit.com/frahlg/dashboards/welcome-dashboard)
- [Cayenne MyDevices](https://cayenne.mydevices.com)
- [Blynk IoT](https://github.com/vshymanskyy/blynk-library-python)
Libraries for MicroPython exist.
- [Ubidots (STEM edition)](https://ubidots.com/stem/). Seems to have good support for Pycom.
- [Thingsboard](https://thingsboard.io/), can be run locally with [Docker](https://thingsboard.io/docs/user-guide/install/docker/).
- [Thingsspeak](https://thingsspeak.com), Matlabs cloud
- [Thinger.io](hhttps://thinger.io/)
- [Iottweet.com](https://iottweet.com/) Not tested, seems to be free.
- [https://freeboard.io/](https://freeboard.io/) Freeboard. Used to be free, not anymore ...
- [AWS IoT Things Graph](https://aws.amazon.com/iot-things-graph/)
- [Azure IoT](https://azure.microsoft.com/en-us/overview/iot/)
- [Google Cloud IoT](https://cloud.google.com/solutions/iot)

