import pycom
from mqtt import MQTTClient
pycom.heartbeat(False)

topic_sub = 'home_office/light/color'
broker_url = 'iot-edu-lab.lnu.se'


def sub_cb(topic, msg):
    if msg == b'Red': pycom.rgbled(0xff0000)
    if msg == b'Blue': pycom.rgbled(0x0004ff)
    if msg == b'Green': pycom.rgbled(0x00ff04)
    if msg == b'Yellow': pycom.rgbled(0xe5ff00)
    if msg == b'White': pycom.rgbled(0xe5ff00)
    if msg == b'Off': pycom.rgbled(0x000000)
    print((topic, msg))

client = MQTTClient("fipy-2", broker_url,user="king",password="arthur", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic=topic_sub)

while True:
    client.check_msg()
    time.sleep(0.5)
