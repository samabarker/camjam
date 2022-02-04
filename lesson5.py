import os
import time
from gpiozero import Button

button = Button(25)
print("---------------")
print("Button and GPIO")
print("---------------")


while True:
    if button.is_pressed:
        print("Button pressed")
        print(button)
        time.sleep(3)
    else:
        os.system("clear")
        print("Waiting for button press")
        print(button)
    time.sleep(0.1)