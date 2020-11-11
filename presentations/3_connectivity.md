# Connectivity


Agenda

1. Connect to WiFi
2. Connect to MQTT
3. Sensor setup (Env. sensor, serial bus I2C)
4. Pub/sub to another device

## WiFi

https://docs.pycom.io/firmwareapi/pycom/network/wlan/

- Scan networks
- MQTT
	- MQTT Servers
		- mqtt.eclipse.org (note, open!)
		- Local installation with Docker
		- MQTT test-server. iot-edu-lab.lnu.se, user=king,pass=arthur, port=1883

		- Adafruit, https://learn.adafruit.com/adafruit-io/mqtt-api
		- Adafruit dashboard, https://io.adafruit.com/frahlg/dashboards
	- MQTT Explorer
- Sensor setup Environmental CS811
	- Sensor communication. I2C, library CCS811.
- Pub/sub


- HTTP requests. https://www.codecademy.com/articles/http-requests


## MQTT Basics

https://www.hivemq.com/mqtt-essentials/
https://mqtt.org/faq/

![](https://pycom.io/wp-content/uploads/2020/03/mqtt_publisher_subscriber-hackster_zPsybZXuck.png-Fj6teRB8V7yljpeg)



The MQTT protocol was invented in 1999. They needed a protocol for minimal battery loss and minimal bandwidth to connect with oil pipelines via satellite. The two inventors specified several requirements for the future protocol.

- Simple implementation
- Quality of Service data delivery
- Lightweight and bandwidth efficient
- Data agnostic
- Continuous session awareness


### Publish/Subscribe

A device can publish a message on a topic, or it can be subscribed to a particular topic.

The most important aspect of pub/sub is the decoupling of the publisher of the message from the recipient (subscriber). This decoupling has several dimensions:

- Space decoupling: Publisher and subscriber do not need to know each other (for example, no exchange of IP address and port).
- Time decoupling: Publisher and subscriber do not need to run at the same time.
- Synchronization decoupling: Operations on both components do not need to be interrupted during publishing or receiving.

### Messages

Information that is shared (published)

The Quality of Service (QoS) level defines the guarantee of delivery for a specific message. There are 3 QoS levels in MQTT:

- At most once (0)
- At least once (1) (puback, client broker acknowledges)
- Exactly once (2) (safest and slowest)

Retain

The broker stores the last retained message and the corresponding QoS for that topic.
A retained message makes sense when you want newly-connected subscribers to receive messages immediately

Last Will and Testament
-  feature to notify other clients about an ungracefully disconnected client


### Topics

represented with strings separated by a forward slash

 at least 1 character and that the topic string permits empty spaces. Topics are case-sensitive. 

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







## Additional video material


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