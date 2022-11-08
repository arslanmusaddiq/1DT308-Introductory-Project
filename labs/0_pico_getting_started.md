# Getting started and Hello World with LED

In this course, we are going to use microcontrollers programmed with MicroPython. The controllers are considered as an IoT device or 'IoT thing'.

In the labs for this course, we are first going to get started with the hardware, and then later on controlling some lights and reading digital inputs. Later on, you will also read a sensor value and transmit that to an online service. In the basic lab setup we are only going to use USB and WiFi as our interfaces. We are in the basic labs using the Raspberry Pi Pico Wireless, and it has WiFi, Bluetooth and is based on the RP2040 chipset. Later on in the course, or in your project we also are able to use the  MCU which is based on the Espressif ESP32-chipset and has both LoRaWAN and SigFox connectivity. The main advantage of using MicroPython compared to C++ and Arduino IDE is that we can quickly test and run our code without compiling and flashing. It makes the development much faster and easier.

### Reference:

**A really good guide on getting started with RPI Pico W: https://projects.raspberrypi.org/en/projects/get-started-pico-w**

You will need to flash the Pico W with MicroPython firmware. You can find the firmware here: https://micropython.org/download/rp2-pico/

The firmware is easily flashed to the microcontroller by holding the BOOTSEL button, the microcontroller will then show up as a USB drive. Copy the firmware to the drive and the microcontroller will reboot and start running MicroPython. There is also a possibility to flash firmware using the Thonny IDE, but that is not recommended as you will end up with the Pico firmware (not the Wireless).

If you're running a Mac and have problems with copying the UF2 file to the Pico W (*Error 100093*), you can use the following command in the terminal: `rsync /path/to/firmware.uf2 /Volumes/RPI-RP2/`

## Introduction

 * Upload files and run code on the microcontroller

## Rules
This task is going to be conducted individually.

## Ingredients

### Hardware
 * One Pico W board
 * One Micro-USB-Cable
 * Your computer

### Software
 * **Thonny** programming environment, https://thonny.org/
 
### Knowledge components

 * configure your IDE
 * run code in the REPL https://docs.micropython.org/en/latest/reference/repl.html
 * upload and run code in files
 * print() strings to console https://www.w3schools.com/python/ref_func_print.asp
 * import statements http://wiki.micropython.org/Importing-Modules
 * for-loops with `range()` https://www.w3schools.com/python/python_for_loops.asp
 * `time.sleep()` https://docs.micropython.org/en/latest/rp2/quickref.html#delay-and-timing

## Steps
Complete each step before progressing to the next.

### Step 1. Hardware setup

WARNING! "**Be gentle on hardware** when plugging and unplugging from the USB connector. Whilst the USB connector is soldered and is relatively strong, if it breaks  it can be very difficult to fix."

### Step 2. Software setup

### Step 3.
Make sure the board is connected to a computer with your IDE. When the board is properly setup you can run micropython code directly on it using the IDE. The output from the commands are sent to the computer so that you can interact with the board.

Write help() in the pycmkr console and press enter, this should give you output like in "Expected output 1"
```python
>>>help()
```

The help command prints some useful short-cuts you can use to for example interrupt a board that is stuck in a loop so that you can upload new code.

#### Expected output. Run help() on board
![Goal state 1](/images/pico-help.png)

### Step 4. Run custom code on the board
Create project folder in your IDE, with a main.py file and run it.

Using the IDE, create a new file (main.py) with the following content but replace "Name 1" and "Name 2" with group members usernames

```python
print("Hello, Name 1, Name 2!")
```

Press the green run button

![Run Button](/images/thonny-run.png)

When pressing the Run button you are executing the code in the text editor on the microcontroller. It's essentially the same as you would have written everything line by line in the REPL console. Make sure that you either edit the code on your computer and then upload the files to the device, or if you are working with editing files directly on the device.

When the microcontroller starts it first executes the file `boot.py` and then `main.py`. If you want to run other files you can do so by importing them in `main.py` or by running them directly in the REPL console.

When the has completed the code will run on the board and should produce the same output as in Expected output 2.

#### Expected output 2.
![Goal state 2](/images/hello-fredrik.png)

When you have completed this assignment you are expected to know:
 * How to flash firmware on your microcontroller.
 * How to setup your IDE.
 * How to run python commands using the REPL console.
 * How to upload and run code

This task is examined using self-examination. Make sure you understand every step before you proceed.

# Lab 0. Blink Lights. Hello World of IoT

### Follow a tutorial and modify code, blink a light.

Blink the on board LED.

### Expected output:

Read the documentation: https://projects.raspberrypi.org/en/projects/get-started-pico-w

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
 * 1 breadboard
 * 1 Red LED
 * 1 Yellow LED
 * 1 Green LED
 * 3 Resistors \~400 Ohm (Green, Blue, Brown, Gold) or higher
 
### Software 
 * IDE of your choice (preferably Thonny)

### Knowledge components
 * Breadboards (kopplingsdäck) https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all
* Basic LED circuit https://en.wikipedia.org/wiki/LED_circuit
* Light Emitting Diodes (LEDs) https://en.wikipedia.org/wiki/Light-emitting_diode
* Resistors (motstånd) https://en.wikipedia.org/wiki/Resistor
 * Microcontroller GPIO https://en.wikipedia.org/wiki/General-purpose_input/output
* Make a GPIO port an output https://docs.micropython.org/en/latest/rp2/quickref.html#pins-and-gpio
* Turn GPIO output on and off. ```python pin.value([value]) ```
* Make the thread sleep for a second  ```python  time.sleep(seconds) ```
* Loops. ```python  while Condition: ``` and/or ```python  for element in array: ```

## Steps

### Step. Connect Three LED circuits

We are going to connect three LED circuits on the breadboard and power these from the GND(-) and 3V3(+) connections on the MCU. See breadboard tutorial if needed.
**WARNING! When changing components on the breadboard, always have the USB disconnected!**

 * Disconnect the USB cable. 
 * Connect the GND to the black/blue power rail (BPR) on the breadboard. Also connect 3V3 to the red power rail (RPR). 
 * Connect the three LED circuits but use the power rails as + and - of the battery and use a 560 Ohm resistor. 
 * Make sure each LED lights up when you connect the USB-cable. 
 * Make sure you use suitable GPIO pins. Read the documentation for the Pico W. https://datasheets.raspberrypi.org/pico/pico-datasheet.pdf
 
#### Connections 
Summary of connections. "<-->" means a cable or connection
 * MCU GND <--> Black/Blue Power Rail (BPR)
 * MCU 3V3 <--> Red Power Rail (RPR)
 * RPR(3V3) <--> [ Anode - LED - Cathode ] <--> [ resistor ] <--> BPR(GND)
 
 ![LED Circuit, Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/LED_circuit.svg/1200px-LED_circuit.svg.png)


### Step. Driving LED with GPIO  

IMPORTANT: We are going to connect external LED's to the microcontroller. The MCU microcontroller provides "General Purpose Input Output"-ports also called GPIO-ports that can be used to communicate with external components. The ports are a bit sensitive and should not be used to directly drive heavy loads (like a motor). The Datasheet for MCU says "Absolute MAX per pin 16 mA" which means we must reduce current by using resistors. If more current is needed, additional components (eg. transistors, or drivers) can be used. Thankfully this assignment does not require high current and we can reduce the current flow by having a resistor in series with each LED we connect.

 * Disconnect the USB cable again
 * For each of the LEDs, remove the wire going from the red power rail to the anode (but keep the GND cable and resistor).
 * Introduce new cables going from GPIO ports on the MCU to the LED anodes as in connections below.
 
 #### Connections 
 * MCU GND <--> Black Power Rail (BPR)
 * MCU P8 <--> [ Anode - Red LED - Cathode ] <--> [ 560 Ohm resistor ] <--> BPR(GND)
 * MCU P9 <--> [ Anode - Yellow LED - Cathode ] <--> [ 560 Ohm resistor ] <--> BPR(GND)
 * MCU P10 <--> [ Anode - Green LED - Cathode ] <--> [ 560 Ohm resistor ] <--> BPR(GND)
 
#### Expected output

The Red LED should be ON after the MCU has booted, should stay ON one second, and turn off. The behaviour is repeated if the board is reset by pressing the reset button on the MCU board (next to the RGB-LED on the side of the micro-USB.

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
 * How to blink the built-in LED?
 * Why do we need a resistor in series with each LED?
 * How can we make the LEDs blink faster?
 * Where can you find information about the different hardware limits in the MCU board?
 * What are the components of a basic LED-circuit and how do we connect them in order for the LED to be ON?