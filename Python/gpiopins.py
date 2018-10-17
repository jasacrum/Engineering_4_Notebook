import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

def Blink(blinks, speed):
    for i in range(0, blinks):
        GPIO.output(11, True)
        sleep(.2)
        GPIO.output(11, False)
        sleep(.2)
        GPIO.output(12, True)
        sleep(.2)
        GPIO.output(12, False)
        sleep(.2) 
    GPIO.cleanup()

iterations = input("How many times would you like the LEDs to blink mate?")
Blink(int(iterations),float(1))
