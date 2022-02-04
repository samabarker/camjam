import time
from gpiozero import Buzzer, LED

buzzer = Buzzer(22)
red = LED(18)
unit = 0.1

def dot():
    buzzer.on()
    red.on()
    time.sleep(unit)
    buzzer.off()
    red.off()
    time.sleep(unit)

def dash():
    buzzer.on()
    red.on()
    time.sleep(3 * unit)
    buzzer.off()
    red.off()
    time.sleep(unit)

def letterSpace():
    time.sleep(unit * 2)

def wordSpace():
    time.sleep(unit * 6)

def A():
    dot()
    dash()

def B():
    dash()
    dot()
    dot()
    dot()

def C():
    dash()
    dot()
    dash()
    dot()

def D():
    dash()
    dot()
    dot()

def E():
    dot()

def F():
    dot()
    dot()
    dash()
    dot()

def G():
    dash()
    dash()
    dot()

def H():
    dot()
    dot()
    dot()
    dot()

def I():
    dot()
    dot()

def J():
    dot()
    dash()
    dash()
    dash()

def K():
    dash()
    dot()
    dash()

def L():
    dot()
    dash()
    dot()
    dot()

def M():
    dash()
    dash()

def N():
    dash()
    dot()

def O():
    dash()
    dash()
    dash()

def P():
    dot()
    dash()
    dash()
    dot()

def Q():
    dash()
    dash()
    dot()
    dash()

def R():
    dot()
    dash()
    dot()

def S():
    dot()
    dot()
    dot()

def T():
    dash()

def U():
    dot()
    dot()
    dash()

def V():
    dot()
    dot()
    dot()
    dash()

def W():
    dot()
    dash()
    dash()

def X():
    dash()
    dot()
    dot()
    dash()

def Y():
    dash()
    dot()
    dash()
    dash()

def Z():
    dash()
    dash()
    dot()
    dot()

#HELLO MY NAME IS SAM
H()
letterSpace()
E()
letterSpace()
L()
letterSpace()
L()
letterSpace()
O()
wordSpace()
M()
letterSpace()
Y()
wordSpace()
N()
letterSpace()
A()
letterSpace()
M()
letterSpace()
E()
wordSpace()
I()
letterSpace()
S()
wordSpace()
S()
letterSpace()
A()
letterSpace()
M()