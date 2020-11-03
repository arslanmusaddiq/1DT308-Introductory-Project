# Read an analog input
# https://docs.pycom.io/firmwareapi/pycom/machine/adc/

import machine
import time


adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P16',attn=adc.ATTN_11DB)   # create an analog pin on P16

# Valid pins are P13 to P20.

def ThermistorNTC(raw_adc):
    # https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation
    r1 = 10000.
    vref = 3.3
    measure = (raw_adc / 4096 ) * vref
    ntc_ohm = ( (r1 * vref) / measure ) - r1
    return str(ntc_ohm) + ' Ohm'

while True:
    val = apin()                    # read an analog value
    print(ThermistorNTC(val))
    #print(str(val/4096*3.3)+'V .......... counter ....... ' + str(time.time()%10))
    time.sleep(1)
