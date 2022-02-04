import time
from gpiozero import LED

red = LED(18)
yellow = LED(23)
green = LED(24)

while True:
    print('LEDs ON')
    red.on()
    yellow.on()
    green.on()
    print('Wait for 1 seconds')
    time.sleep(1)
    print('LEDs OFF')
    red.off()
    yellow.off()
    green.off()
    time.sleep(1)