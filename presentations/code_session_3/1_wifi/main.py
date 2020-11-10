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
