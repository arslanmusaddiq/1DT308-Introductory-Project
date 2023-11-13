# Lab 3 - The IoT Traffic Light

---

## The use of AI in this lab:

[Hybrid learning bot](https://udify.app/chat/OCbFbncOAUXXherd)

---


In this assignment we aim to work with more code and components. We apply the things we have learned so far, more of the same but with less instructions and guidance.

## Rules

The task is to create a traffic light with buttons, that is not connected to the internet.

This assignment is done individually.

ALERT! DURING THIS ASSIGNMENT NONE OF THE ARTIFACTS FROM THIS ASSIGNMENT MAY BE SHARED WITH OTHER STUDENTS. YOU MAY NOT ASK FOR HELP FROM OTHER STUDENS, THINK OF THIS AS AN EXAM. 
YOU MAY GET HELP FROM A TEACHING ASSISTANT OR THE TEACHER.

## Knowledge Components
 * Apply knowledge components from previous assignments. 

## Ingredients

### Hardware
 * Six LED's with resistors (2 x Red, 2 x yellow, 2 x green)
 * Buzzer with resistor
 * Button with resistor
 
## Steps

### Step 1. Build Check all components

We are going to build a traffic light that can sit next to a pedestrian crossing. Thus, it has three LEDs for traffic, two LEDs for the pedestrian crossing, and a button circuit used by pedestrians to ask for green light. 

Build one circuit at a time and test before continuing to the next
* a traffic light (Red, Yellow, Green - LEDs with resistors), 
* a pedestrian crossing light (Red, Green - LEDs with resistors) and a Buzzer
* a pedestrian button (button circuit and Yellow LED with resistors). The LED is ON when the button has been pressed and is turned off when green LED is ON for the pedestrians.

To test all components: 
When all hardware has been set-up, write a routine that waits for a button press, then turn ON each LED, and finally beeps the buzzer before waiting again. Note that all pins cannot be used for output. 

### Step 2. Traffic light with pedestrian crossing

We are now going to model a pedestrian crossing light with Python code. The traffic light is normally Green.
The button should represent a pedestrian looking to cross the street. When pressed, the Yellow button-LED should light up, traffic is given Red light (after a while), and pedestrians should be allowed passage before the traffic light turns Green again.

We can model this by defining different states, each defined in its own function:

#### States:

 * TRAFFIC GO: Traffic Green LED, Pedestrian Red LED, lasts for at minimum of 4 seconds, but continue longer if not interrupted by button presses.
 * TRAFFIC SOON STOP: Traffic Yellow LED, Pedestrian Red LED, lasts 2 seconds
 * ALL STOP: Traffic Red LED, Pedestrian Red LED, lasts 1 second
 * PEDESTRIAN GO: Traffic Red LED, Pedestrian Green LED, Buzzer speedy Tick sounds, lasts 3 seconds
 * PEDESTRIAN SOON STOP: Traffic Red LED, Pedestrian Green LED, Slower Tick Sounds, lasts 1 second
 * TRAFFIC GET READY: Traffic Red LED + Traffic Yellow LED, Pedestrian Red LED, lasts 1 second

 ![State transitions](../images/states.png)

You can now write a main loop that normally runs the TRAFFIC GO state-function if nothing happens. If the button is pressed a boolean variable is set and the main loops starts calling the different state-methods in order.

#### Check code
 * Code should be DRY (no unnecessary repeated statements)
 * Code should be divided into methods / functions
 * Method names should represent the content (for example state names)
 * Code should be readable and easy to understand
 * Code should be easy to extend
 * Code should be easy to test

## Examination

This assignment should be examined by a teacher/TA. 

Prepare for that by checking yourself so that you know the answers to the following questions:

 * Does the traffic light work?
 * What happens if you press the button repeatedly?
 * Why should we keep the code in event-callbacks to a minimum?
 * How is the event-callback handled?
 * The time for key-presses should be printed as the example.
 
### Check knowledge: 
 * Ask the student two of the above questions.

When completed you should ask a teacher/TA to check your setup and verify the questions above yourself.
