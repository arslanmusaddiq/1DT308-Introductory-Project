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
    client = MQTTClient("gizella_1", "mqtt.eclipse.org", port=1883)

    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic="frahlg_lab/feeds/lights")

    while True:
        print("Sending ON")
        client.publish(topic="frahlg_lab/feeds/lights", msg="ON")
        time.sleep(1)
        print("Sending OFF")
        client.publish(topic="frahlg_lab/feeds/lights", msg="OFF")
        client.check_msg()
        time.sleep(1)

connect_mqtt()
