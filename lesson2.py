import time
from gpiozero import LED

red = LED(18)
yellow = LED(23)
green = LED(24)

print('LEDs ON')
red.on()
yellow.on()
green.on()
print('Wait for 3 seconds')
time.sleep(3)
print('LEDs OFF')
red.off()
yellow.off()
green.off()