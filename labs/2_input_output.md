# Lab 2 - external input and outputs

---

## Use of this AI bot in this lab:

[AI bot lab 2](https://udify.app/chat/GAlMmwVESEyb1mlg)

---



In this assignment we are going to work with user-input through a button circuit and also introduce a new form of output (sound). 

 * Work with input
 * Work with sound
 * Work with temperature sensors

## Rules

During the assignment you may discuss the assignment with students outside the group. You may help other groups but you may NOT do all steps for them, or share any code. Note that these rules change between assignments.

## Knowledge Components

 * Buzzers (Svenska: Summer) https://en.wikipedia.org/wiki/Buzzer
    * Buzzer circuit https://www.instructables.com/id/How-to-use-a-Buzzer-Arduino-Tutorial/
    * Creating a PWM object https://docs.micropython.org/en/latest/library/machine.PWM.html
    * Setting the duty cycle of the channel https://docs.micropython.org/en/latest/library/machine.PWM.html
 * Button https://learn.sparkfun.com/tutorials/switch-basics/all
    * Button circuit with pull-down resistor https://learn.sparkfun.com/tutorials/pull-up-resistors
    * Defining callback function on events https://electrocredible.com/raspberry-pi-pico-external-interrupts-button-micropython/
    * Interrupts https://en.wikipedia.org/wiki/Interrupt
    * Taking a utime.ticks_ms() https://docs.micropython.org/en/v1.15/library/utime.html
    * Contact Bounce https://www.allaboutcircuits.com/textbook/digital/chpt-4/contact-bounce/
 
* Temperature sensors
    * Analog input
        * Thermistor https://learn.adafruit.com/thermistor
        * NTC Thermistor https://en.wikipedia.org/wiki/Thermistor
        * Read an analog value. https://docs.micropython.org/en/latest/rp2/quickref.html#adc-analog-to-digital-conversion

    * Digitial input
        * DHT sensors https://learn.adafruit.com/dht
        * 1-Wire. https://en.wikipedia.org/wiki/1-Wire
        *  Onewire driver: https://docs.micropython.org/en/latest/rp2/quickref.html?highlight=onewire#onewire-driver

 * Code
    * API: Reading time in ms. utime.ticks_ms()
    * event callback functions
    * global variables. https://www.programiz.com/python-programming/global-local-nonlocal-variables
    * API: Create PWM timer PWM(0, frequency=i)
    * timer duty cycle: duty_cycle(0.5) https://en.wikipedia.org/wiki/Duty_cycle
    * API: Make the microcontroller sleep. `time.sleep()`
    * declare function
  
## Ingredients

### Hardware
 * Everything from Task 2. (3 LED with resistors)
 * Button 
 * pull-down resistor 1k Ohm (Brown, Black, Red, Gold)
 * Buzzer 
 * Buzzer-resistor 1k Ohm (Brown, Black, Red, Gold) 
 * Temperature sensor
    - analog NTC
    - digital DHT-11 / 22
 
### Software 
 * Everything from Task 2.
 
## Circuits

### Breadboard circuit

Connect the breadboard power-rails to GND and 3V3.

 * GND <--> Black/Blue Power Rail (BPR)
 * 3V3 <--> Red Power Rail (RPR)
 
### The buzzer circuit
The buzzer is driven directly from the microcontroller's port but using a current reducing resistor. For higher volume it is adviceable to use a driver circuit.

Place the buzzer with one leg on each side of the breadboard ravine. Connect one side to the microcontroller port and the other through a resistor to GND. 

 * PIN <--> Buzzer <--> 1k Ohm resistor <--> BPR(GND)
 
### The button circuit
The button has two sides with two legs each (We call them A and B) that are connected when the button is pressed. The button is placed over the breadboard ravine. We connect the A-side to the input port of the microcontroller. We also connect the A side through a 1k Ohm resistor to GND, this pulls the input port voltage down to GND. GND counts as a LOW (or 0) when we read the input of the port through our code. The resistor is called a "pull-down resistor". We connect the B side of the button to 3v3. 

When the button is pressed the A and B-sides become connected the input becomes a HIGH (or 1) since we measure on the side now directly connected to 3v3. Please note that a current now runs through the 1k Ohm connector. 

  * PIN <--> Button side A <--> 1k Ohm resistor <--> BPR(GND)
  * Button side B <--> RPR(3v3)
  
![Pull down button circuit](/images/pull-down-button.jpg)
## Steps

### Step 1. Button

Run the following code with a button circuit on any PIN:

```python
from machine import Pin

count = 0

def buttonEventCallback(argument):
    global count
    print("button was pressed: " + str(count))
    count += 1

buttonPin = Pin('PXX', mode=Pin.IN, pull=None)
buttonPin.callback(Pin.IRQ_FALLING, buttonEventCallback)
```

Press the button a couple of times. Note that not all presses results in a single event being launched. Due to *contact bounces* we might end up with multiple button-presses even if the button was only pressed once.

Contact bounces are explained here: https://www.allaboutcircuits.com/textbook/digital/chpt-4/contact-bounce/

Rewrite the code so that at most one button press can happen each second. 
 * Use a variable to store the last time the button was pressed using utime.ticks_ms(). 
 * Ignore key-presses if the time since last press was less than a second.

The program output should look like the following when quickly pressing the button:
```
...
Button was pressed: 3 time(s). Time since last 1462ms
Button was pressed: 4 time(s). Time since last 1795ms
Button was pressed: 5 time(s). Time since last 1021ms
Ignored button press: Time left for next press is 809ms
Ignored button press: Time left for next press is 431ms
Button was pressed: 6 time(s). Time since last 1164ms
Ignored button press: Time left for next press is 789ms
Ignored button press: Time left for next press is 480ms
Ignored button press: Time left for next press is 475ms
Ignored button press: Time left for next press is 320ms
Ignored button press: Time left for next press is 261ms
Ignored button press: Time left for next press is 256ms
Ignored button press: Time left for next press is 184ms
Ignored button press: Time left for next press is 127ms
Button was pressed: 7 time(s). Time since last 2711ms
```


### Step 2. Press play for music

The following code is from https://forum.pycom.io/topic/802/example-pwm-mariobros

Rewrite the code so that the music is started when the button is pressed. Merge with code from step 1 so that button can still be pressed.
 * The playing of the tune should not be run in the event handler. The event handler interrupts the currently running code on the microcontroller and thus locks up the execution until its done. To many interrupts may cause the microcontroller to be unresponsive. 
 * Keypresses that happen during the playing of the tune should not result in cued up plays. 
 * You may reduce the length of the Tune, but it must be longer than the time for contact bounce. 


```python

from machine import Pin
from machine import PWM
import time

# define frequency for each tone
E7 = 2637
F7 = 2794
C7 = 2093
G7 = 3136
G6 = 1568
E6 = 1319
A6 = 1760
B6 = 1976
AS6 = 1865
A7 = 3520
D7 = 2349

# set up pin PWM timer for output to buzzer or speaker
p2 = Pin("PXX")  # Pin Y2 with timer 8 Channel 2
tim = PWM(0, frequency=300)
ch = tim.channel(2, duty_cycle=0.5, pin=p2)https://forum.pycom.io/topic/802/example-pwm-mariobros

mario = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0]

for i in mario:
    if i == 0:
        ch.duty_cycle(0)
    else:
        tim = PWM(0, frequency=i)
        ch.duty_cycle(0.5)

    time.sleep(0.15)
```

## Step 3. Blink lights to tune

Assign one LED for each tone (multiple tones can be attached to the same LED) turn on LED's in tune with the music.

## Step 4. Read an analog temperature sensor

Read the analog value from the NTC-sensor and present it in time intervals to the console with a `print()`-function. Note, depending on your sensor you might need to do a voltage divider. Read more about NTC thermistors and how to connect a voltage divider here: https://www.electronics-tutorials.ws/io/thermistors.html

You will have to think about how the voltage that is read using the analog input is translated to a temperature. There are both [equations](https://eepower.com/resistor-guide/resistor-types/ntc-thermistor/#) and [lookup tables](https://cdn-shop.adafruit.com/datasheets/103_3950_lookuptable.pdf) that can be used to write a function.


**NOTE** The NTC thermistor mounted on a PCB that is distributed from the lab can be incorrectly marked. The correct setup is shown in the Figure below. If that does not give you expected values, try to switch the wires around, some students have found units that are incorrectly marked in different ways. [Analog temperature sensor NTC Electrokit](https://www.electrokit.com/uploads/productfile/41015/41015732_-_Analog_Temperature_Sensor.pdf) Note. The schematics are wrong on this one.

![NTC Thermistor](../images/ntc-sensor-electrokit.jpg)

Discuss how accurate the reading is and the range of the temperature span that is presented.

- How many bits do you have for the value, and how does this affect your reading?

## Step 5. Read a digital temperature and humidity sensor

Connect a temperature and/or humidity (DHT11 / 22 or a DS18B20) sensor to the device. The sensor communicates using the 1-Wire protocol, you will need to use a library.

[Digital temp sensor DHT11 bought from Electrokit](https://www.electrokit.com/uploads/productfile/41016/DHT11.pdf)

![](../images/dht11_wiring.jpeg)

## Examination

This assignment should be examined by a teacher/TA. 

You should in this assignment make sure you have fulfilled all the described tasks above. That is, you must be able to demonstrate reading both analog and digital sensors as well as interacting with buzzers and buttons.

Prepare for that by checking yourself so that you know the answers to the following questions:

 * What is the difference between a pull-up and a pull-down button circuit?
 * What is contact bouncing and why would we be bothered?
 * What is a microcontroller interrupt?
 * Why should we keep the code in event-callbacks to a minimum?
 * How can the song continue while the event-callback prints out key-presses?

When completed you should ask a teacher/TA to check your setup and verify the questions above yourself.

### Test setup:
 * The time for key-presses should be printed as the example.
 * Test by "spamming" the button with lots of short presses. The song should start on the first press and continue without interruption until it ends. The buttonclicks do not stack and after the song is over id does not restart unless a new click is introduced afterwards. The printouts of times should continue while the song is played.
 * If lights blink in tune with music, make extra credit note. 
 
### Check Code:
 * Code should be DRY (no unnecessary repeated statements)
 * Code should be divided into methods
 * The song should not be played in the eventhandler function but started in a separate loop (or thread).
