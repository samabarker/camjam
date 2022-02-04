import time
from gpiozero import LED

choices = [18,23,24] #red, yellow, green

print('Choose LED to flash.')
print('1 = RED')
print('2 = GREEN')
print('3 = YELLOW')
choice = int(input('Choice: '))
number_blinks = int(input('Number of Blinks: '))

LEDChoice = LED(choices[choice-1])

for i in range(number_blinks, 0, -1):
    LEDChoice.on()
    time.sleep(1)
    LEDChoice.off()
    time.sleep(1)
