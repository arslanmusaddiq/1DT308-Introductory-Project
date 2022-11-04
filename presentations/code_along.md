Planning along. All code...

1. First . Playing with the RGBLED.



```python
import pycom
import time

pycom.heartbeat(False)

while True:
    #colors in hexadecimal (0xRRGGBB)
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    pycom.rgbled(0x0000FF)  # Blue
    time.sleep(1)


```

## Connecting

https://docs.pycom.io/firmwareapi/pycom/network/wlan/



## List SSID:s

```python


from network import WLAN

nets = wlan.scan()

for net in nets:
    print(net.ssid)



```

Quick start


```python
import network
import time
# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('iot-lab', auth=(network.WLAN.WPA2, 'kingarthur'))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())
```

Another example.

```python

import machine
from network import WLAN

# configure the WLAN subsystem in station mode (the default is AP)
wlan = WLAN(mode=WLAN.STA)
# go for fixed IP settings (IP, Subnet, Gateway, DNS)
wlan.ifconfig(config=('192.168.3.40', '255.255.255.0', '192.168.3.1', '1.1.1.1'))
wlan.scan()     # scan for available networks

wlan.connect(ssid='iot-lab', auth=(WLAN.WPA2, 'kingarthur'))
while not wlan.isconnected():
    pass
print(wlan.ifconfig())

```


https://docs.pycom.io/tutorials/networkprotocols/wifisniffer/


```python

from network import WLAN
import ubinascii


def pack_cb(pack):
    mac = bytearray(6)
    pk = wlan.wifi_packet()
    control = pk.data[0]
    subtype = (0xF0 & control) >> 4
    type = 0x0C & control
    #print("Control:{}, subtype:{}, type:{}".format(control, subtype, type))
    if subtype == 4:
        for i in range (0,6):
            mac[i] = pk.data[10 + i]
        print ("Wifi Node with MAC: {}".format(ubinascii.hexlify(mac)))

wlan = WLAN(mode=WLAN.STA, antenna=WLAN.EXT_ANT)
wlan.callback(trigger=WLAN.EVENT_PKT_MGMT, handler=pack_cb)
wlan.promiscuous(True) #pass all to CPU


```




### MQTT



- Install MQTT Explorer

Using Docker locally, default config.

https://hub.docker.com/_/eclipse-mosquitto

```bash
docker run -p 1883:1883 eclipse-mosquitto
```


### Using Adafruit



Note.





```
def callback(topic, msg): 
    print((topic, msg))
    if topic == b"username/feeds/Temperature control":
        sub_cb_temp(topic, msg)
    else
        sub_cb_weight(topic, msg)


```






