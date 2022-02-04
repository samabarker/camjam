#Import libraries
import time
from gpiozero import Buzzer, LED, Button

#Import GPIO and define some variables
red = LED(18)
yellow = LED(23)
green = LED(24)
buzzer = Buzzer(22)
button = Button(25)
button_pressed = False

#Define some functions for changing light status
#Put the green light on
def start_green():
    green.on()

#Change from green to amber (hold for 3s) to red
def green_to_red():
    green.off()
    yellow.on()
    time.sleep(3)
    yellow.off()
    red.on()
    time.sleep(1)

#Hold red for 5s whilst beeping, then a further 2s
def red_hold():
    for i in range(0,20):
        buzzer.on()
        time.sleep(0.2)
        buzzer.off()
        time.sleep(0.2)
    time.sleep(2)

#Change frp, red to amber, flash for 6s, then change to green
def red_to_green():
    red.off()
    for i in range(0,6):
        yellow.on()
        time.sleep(0.5)
        yellow.off()
        time.sleep(0.5)
    yellow.off()
    green.on()


#Running loop for traffic lights
while True:
    start_green()
    if button.is_pressed or button_pressed:
        button_pressed = False
        green_to_red()
        red_hold()
        red_to_green()
        start = time.time()
        #Wait 20s before changing again, but allow button push to be registered
        while time.time() - start < 20:
            if button.is_pressed:
                button_pressed = True

