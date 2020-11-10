import network
import time
import pycom

pycom.heartbeat(False)


# setup as a station

def connect_wifi():
    pycom.rgbled(0xFF0000)  # Red
    wlan = network.WLAN(mode=network.WLAN.STA)
    wlan.connect('iot-lab', auth=(network.WLAN.WPA2, 'kingarthur'))
    while not wlan.isconnected():
        pycom.rgbled(0x0000FF)  # Blue
        time.sleep_ms(100)
        pycom.rgbled(0x000000)
        time.sleep_ms(20)

    pycom.rgbled(0x00FF00)  # Green
    print(wlan.ifconfig())

connect_wifi()
