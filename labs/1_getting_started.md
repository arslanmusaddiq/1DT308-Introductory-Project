# Getting started

In this course, we are going to use microcontrollers programmed with MicroPython. The controllers are considered as an IoT-device or 'IoT-thing'.

In the labs for this course, we are first going to get started with the hardware, and then later on controlling some lights and reading digital inputs. Later on, you will also read a sensor value and transmit that to an online service. In the basic lab setup we are only going to use USB and WiFi as our interfaces. The Pycom LoPy4 device has WiFi, Bluetooth, LoRa and SigFox and is based on the Espressif ESP32-chipset. The main advantage of using MicroPython compared to C++ and Arduino IDE is that we can quickly test and run our code without compiling and flashing. It makes the development much faster.

Reference:
https://docs.pycom.io/gettingstarted/

## Introduction

This assignment is all about getting to know the Atom development environment and to be able to run code on the pycom LoPy4 boards.

 * Install Atom and PyMakr plugin
 * Connect LoPy4 to a computer
 * Connect to board in Atom and run code in console (on the hardware)
 * Upload files and run code on the microcontroller

## Rules
This task is going to be conducted individually.

## Ingredients

### Hardware
 * One LoPy4 board
 * One expansion board
 * One LoRa Antenna
 * One Micro-USB-Cable
 * One computer

### Software
 * **Atom.io** programming environment, https://atom.io/
 * **NodeJS** (current 15+), https://nodejs.org
 * **PyMakr** plugin is found via the extension tab in either IDE

(Note: The PyMakr plug-in exists also for Visual Studio Code https://code.visualstudio.com/. Atom.io is recommended due to better functionality.)

### Knowledge components

 * configure your IDE
 * run code in the REPL https://docs.micropython.org/en/latest/reference/repl.html
 * upload and run code in files
 * print() strings to console https://www.w3schools.com/python/ref_func_print.asp
 * import statements http://wiki.micropython.org/Importing-Modules
 * for-loops with `range()` https://www.w3schools.com/python/python_for_loops.asp
 * `pycom.rgbled()` https://docs.pycom.io/tutorials/basic/rgbled/
 * `time.sleep()` https://docs.pycom.io/firmwareapi/micropython/utime/

## Steps
Complete each step before progressing to the next.

### Step 1. Hardware setup

![Setup for Getting Started](/images/1_hardware.png)
* Connect the LoPy4 on the expansion board. **Double check the direction, the LED should be in the same direction as the micro-USB connection.**
* Do not connect the expansion board to USB without the LoPy4 connected!
* Connect the Antenna to the Lopy 868MHz/915MHz (LoRa & Sigfox) antenna port. Be careful, and note that there are three connectors. Check this: https://docs.pycom.io/gettingstarted/connection/lopy4/
* Connect the usb-cable to both computer and expansion board


WARNING! "**Be gentle on hardware** when plugging and unplugging from the USB connector. Whilst the USB connector is soldered and is relatively strong, if it breaks  it can be very difficult to fix."

### Step 2. Software setup
 * Download and install Atom.io
 * Install PyMakr plugin in Atom.io (using the package manager, settings Packages)

### Step 3.
Make sure the LoPy board is connected to a computer with Atom and PyMkr installed.

When the board is properly setup you can run micropython code directly on it using the pymakr-console. The output from the commands are sent to the computer so that you can interact with the board.

Write help() in the pycmkr console and press enter, this should give you output like in "Expected output 1"
```python
>>>help()
```

The help command prints some useful short-cuts you can use to for example interrupt a board that is stuck in a loop so that you can upload new code.

HINT! To reset the device
 * Click inside the PyMkr console then press CTRL+F
 * Press the reset-button on the LoPy4 device, next to the RGB LED!


#### Expected output. Run help() on board
![Goal state 1](/images/1_goal_state_1.png)

### Step 4. Run custom code on the board
Create project folder in Atom, with a main.py file and run it.

Using Atom, create a new file (main.py) with the following content but replace "Name 1" and "Name 2" with group members usernames

```python
print("Hello, Name 1, Name 2!")
```

Press upload ![PyMkr Upload Button](/images/upload.png)

When the upload has completed the code willrun on the board and should produce the same output as in Expected output 2

#### Expected output 2.
![Goal state 2](/images/1_goal_state_2.png)

### Step 5. Follow a tutorial and modify code, blink a light.
Use the built in RGB-LED-light to blink in different colors.

Read and complete this tutorial [https://docs.pycom.io/tutorials/basic/rgbled/](https://docs.pycom.io/tutorials/basic/rgbled/)

Then rewrite the code so that the RGB-LED flashes in two second interval but also prints the name of the color(red, green, yellow) to the console.

### Expected output 3. :

 * The color of the built-in LED on the LoPy4 board switches between red, green, yellow every second.
 * The color-name is also written on the console at the same time.

```
Red
Green
Yellow
Red
Green
Yellow
Red
```

# Blink External LEDs

## Introduction
In this assignment, we connect basic circuits with LED's on a breadbord and write python code that turns these on and off.

 * Get LED-lights to blink.
 * Work with GPIO ports.
 * Python loops
 

## Rules

This task is going to be conducted individually.

## Ingredients

### Hardware
 * Everything from Task 1.
 * 1 breadboard
 * 1 Red LED
 * 1 Yellow LED
 * 1 Green LED
 * 3 Resistors \~400 Ohm (Green, Blue, Brown, Gold) or higher
 
### Software 
 * Everything from Task 1.
 * Atom with pymakr plugin

### Knowledge components
 * Breadboards (kopplingsdäck) https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all
 * Basic LED circuit https://en.wikipedia.org/wiki/LED_circuit
  * Light Emitting Diodes (LEDs) https://en.wikipedia.org/wiki/Light-emitting_diode
  * Resistors (motstånd) https://en.wikipedia.org/wiki/Resistor
 * Microcontroller GPIO https://en.wikipedia.org/wiki/General-purpose_input/output
  * LoPy4 Datasheet https://docs.pycom.io/gitbook/assets/specsheets/Pycom_002_Specsheets_LoPy4_v2.pdf 
  * Make a GPIO port an output https://docs.pycom.io/firmwareapi/pycom/machine/pin/
  * Turn GPIO output on and off. ```python pin.value([value]) ```
 * Make the thread sleep for a second  ```python  time.sleep(seconds) ```
 * Loops. ```python  while Condition: ``` and/or ```python  for element in array: ```

 
## Steps


### Step. Connect Three LED circuits
We are going to connect three LED circuits on the breadboard and power these from the GND(-) and 3V3(+) connections on the LoPy4 board. See breadboard tutorial if needed.
**WARNING! When changing components on the breadboard, always have the USB disconnected!**

 * Disconnect the USB cable. 
 * Connect the GND on LOPY4 to the black/blue power rail(BPR) on the breadboard. Also connect 3V3 to the red power rail(RPR). 
 * Connect the three LED circuits as in this video https://www.youtube.com/watch?v=yQ2-yVXFMeE but use the power rails as + and - of the battery and use a 560 Ohm resistor. 
 * Make sure each LED lights up when you connect the USB-cable. 
 
#### Connections 
Summary of connections. "<-->" means a cable or connection
 * LOPY4 GND <--> Black/Blue Power Rail (BPR)
 * LOPY4 3V3 <--> Red Power Rail (RPR)
 * RPR(3V3) <--> [ Anode - LED - Cathode ] <--> [ resistor ] <--> BPR(GND)
 
 ![LED Circuit, Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/LED_circuit.svg/1200px-LED_circuit.svg.png)


### Step. Driving LED with GPIO  
IMPORTANT: We are going to connect external LED's to the microcontroller. The LoPy4 microcontroller provides "General Purpose Input Output"-ports also called GPIO-ports that can be used to communicate with external components. The ports are a bit sensitive and should not be used to directly drive heavy loads (like a motor). The Datasheet for LOPY4 says "Absolute MAX per pin 12mA, recommended 6mA" which means we must reduce current by using resistors. If more current is needed, additional components (eg. transistors, or drivers) can be used. Thankfully this assignment does not require high current and we can reduce the current flow by having a resistor in series with each LED we connect.

 * Disconnect the USB cable again
 * For each of the LEDs, remove the wire going from the red power rail to the anode (but keep the GND cable and resistor).
 * Introduce new cables going from the P8-10 port on the LoPy4 to the LED anodes as in connections below.
 
 #### Connections 
 * LoPy4 GND <--> Black Power Rail (BPR)
 * LoPy4 P8 <--> [ Anode - Red LED - Cathode ] <--> [ 560 Ohm resistor ] <--> BPR(GND)
 * LoPy4 P9 <--> [ Anode - Yellow LED - Cathode ] <--> [ 560 Ohm resistor ] <--> BPR(GND)
 * LoPy4 P10 <--> [ Anode - Green LED - Cathode ] <--> [ 560 Ohm resistor ] <--> BPR(GND)
 
 When done! connect USB again and upload the following code in the main.py file.

```python
import time
from machine import Pin
redLED = Pin("P8", mode=Pin.OUT) #Make GPIO P8 an output
redLED.value(1) # Send a 1 to GPIO to turn the LED on
time.sleep(1) # Sleep for a second
redLED.value(0) # Send a 0 to the GPIO to turn the LED off
```

#### Expected output

The Red LED should be ON after the LOPY4 has booted, should stay ON one second, and turn off. The behaviour is repeated if the board is reset by pressing the reset button on the LoPy4 board (next to the RGB-LED on the side of the micro-USB.

### Driving multiple LED's with GPIO

Now adjust the code so that all three LED's blink like this:
 * RED lights up for 1 second. Other LEDs are unlit.
 * GREEN lights up for 1 second. Other LEDs are unlit.
 * YELLOW lights up for 1 second. Other LEDs are unlit.
 * Repeat forever with RED again

#### Expected output
[![](http://img.youtube.com/vi/Wtd8pp-DW3w/0.jpg)](http://www.youtube.com/watch?v=Wtd8pp-DW3w "")

## Examination

This assignment should be examined by a teacher/TA. 

Prepare for that by checking yourself so that you know the answers to the following questions:

 * Which leg (pin) of the LED is longer, the cathode or the anode?
 * Why do we need a resistor?
 * How can we make the LEDs blink faster?
 * Where can you find information about the different hardware limits in the LoPy4 board?
 * What are the components of a basic LED-circuit and how do we connect them in order for the LED to be ON?



## Examination

When you have completed this assignment you are expected to know:
 * How to setup a pycom-development environment with Atom and the PyMakr plugin.
 * How to run python commands using the REPL console.
 * How to upload and run code in files using PyMakr
 * How to blink the built-in LED

This task is examined using self-examination. Make sure you understand every step before you proceed.
