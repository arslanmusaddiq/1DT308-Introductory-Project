import pycom
# import _thread
from mqtt import MQTTClient
import sensor
pycom.heartbeat(False)

topic_sub = 'home_office/env1/control'
broker_url = 'iot-edu-lab.lnu.se'

def sub_cb(topic, msg):
   print(msg)

def interval_send(t_):
    while True:
        send_value()
        time.sleep(t_)

def blink_led():
    for n in range(1):
        pycom.rgbled(0xfcfc03)
        time.sleep(0.5)
        pycom.rgbled(0x000000)
        time.sleep(0.2)

def send_value():
    try:
        co2, voc, = sensor.value()
        client.publish(topic="home_office/env1/co2", msg=str(co2))
        client.publish(topic="home_office/env1/voc", msg=str(voc))
        if co2 < 500:
            client.publish(topic="home_office/light/color", msg='Green')
        if co2 > 500 and co2 < 800:
            client.publish(topic="home_office/light/color", msg='Yellow')
        if co2 > 800:
            client.publish(topic="home_office/light/color", msg='Red')
        print('Sensor data sent ...')
        blink_led()
    except (NameError, ValueError, TypeError):
        print('Failed to send!')

client = MQTTClient("fipy-1", broker_url,user="king",password="arthur", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic=topic_sub)

while True:
    send_value()
    client.check_msg()
    time.sleep(1)
