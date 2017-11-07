from gpiozero import LED
import time

class leds():
#    def __init__(self):
    red    = LED(17)
    yellow = LED(23)
    green  = LED(25)
    
    def redOn(red = red):
        red.on()

    def redOff(red = red):
        red.off()

    def yellowOn(yellow = yellow):
        yellow.on()

    def yellowOff(yellow = yellow):
        yellow.off()

    def greenOn(green = green):
        green.on()

    def greenOff(green = green):
        green.off()

while True:
    leds.redOn()
    leds.greenOff()
    time.sleep(5)
    leds.redOff()
    leds.greenOn()
    time.sleep(5)
    leds.yellowOn()
    time.sleep(1)
    leds.yellowOff()