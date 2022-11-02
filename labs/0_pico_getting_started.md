# Getting started

In this course, we are going to use microcontrollers programmed with MicroPython. The controllers are considered as an IoT device or 'IoT thing'.

In the labs for this course, we are first going to get started with the hardware, and then later on controlling some lights and reading digital inputs. Later on, you will also read a sensor value and transmit that to an online service. In the basic lab setup we are only going to use USB and WiFi as our interfaces. We are in the basic labs using the Raspberry Pi Pico Wireless, and it has WiFi, Bluetooth and is based on the RP2040 chipset. Later on in the course, or in your project we also are able to use the Pycom LoPy4 which is based on the Espressif ESP32-chipset and has both LoRaWAN and SigFox connectivity. The main advantage of using MicroPython compared to C++ and Arduino IDE is that we can quickly test and run our code without compiling and flashing. It makes the development much faster and easier.




Reference:

Getting started with RPI Pico W: https://projects.raspberrypi.org/en/projects/get-started-pico-w

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
 * `pycom.rgbled()` https://docs.pycom.io/tutorials/basic/rgbled/
 * `time.sleep()` https://docs.pycom.io/firmwareapi/micropython/utime/

## Steps
Complete each step before progressing to the next.

### Step 1. Hardware setup

WARNING! "**Be gentle on hardware** when plugging and unplugging from the USB connector. Whilst the USB connector is soldered and is relatively strong, if it breaks  it can be very difficult to fix."

### Step 2. Software setup


### Step 3.
Make sure the board is connected to a computer with your IDE. When the board is properly setup you can run micropython code directly on it using the pymakr-console. The output from the commands are sent to the computer so that you can interact with the board.

Write help() in the pycmkr console and press enter, this should give you output like in "Expected output 1"
```python
>>>help()
```

The help command prints some useful short-cuts you can use to for example interrupt a board that is stuck in a loop so that you can upload new code.

#### Expected output. Run help() on board
![Goal state 1](/images/pico-help.png)

### Step 4. Run custom code on the board
Create project folder in your IDE, with a main.py file and run it.

Using Atom, create a new file (main.py) with the following content but replace "Name 1" and "Name 2" with group members usernames

```python
print("Hello, Name 1, Name 2!")
```

Press upload ![Upload Button](/images/vscode-upload.png)

When the upload has completed the code willrun on the board and should produce the same output as in Expected output 2

#### Expected output 2.
![Goal state 2](/images/vscode-hello-world.png)

When you have completed this assignment you are expected to know:
 * How to setup a pycom-development environment with your IDE and the PyMakr plugin.
 * How to run python commands using the REPL console.
 * How to upload and run code in files using PyMakr

This task is examined using self-examination. Make sure you understand every step before you proceed.