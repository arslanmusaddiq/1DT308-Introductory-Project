import network
import time
# setup as a station

def connect_wifi():
    wlan = network.WLAN(mode=network.WLAN.STA)
    wlan.connect('iot-lab', auth=(network.WLAN.WPA2, 'kingarthur'))
    while not wlan.isconnected():
        time.sleep_ms(50)
    print(wlan.ifconfig())

connect_wifi()

def sub_cb(topic, msg):
   print(msg)

def connect_mqtt():
    from mqtt import MQTTClient
    client = MQTTClient("fipy-1", "iot-edu-lab.lnu.se",user="king",password="arthur", port=1883)

    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic="home_office/env1/control")

    while True:
        print("Sending ON")
        client.publish(topic="home_office/env1/switch", msg="ON")
        time.sleep(1)
        print("Sending OFF")
        client.publish(topic="home_office/env1/switch", msg="OFF")
        client.check_msg()
        time.sleep(1)

connect_mqtt()
