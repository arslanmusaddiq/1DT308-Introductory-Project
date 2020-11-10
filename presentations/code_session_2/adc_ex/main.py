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
    A,B,C = 0.001129148, 0.000234125, 0.0000000876741 # Variables from manufact. Steinhart
    temp = 1/(A + B*(log(ntc_ohm))+ C*(log(ntc_ohm))**3) - 273.15
    return temp

while True:
    val = apin()                    # read an analog value
    print(ThermistorNTC(val))
    time.sleep(1)
