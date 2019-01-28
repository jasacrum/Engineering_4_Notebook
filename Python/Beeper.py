import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(17, GPIO.IN)
GPIO.setup(23, GPIO.OUT)

while True:
    button_state = GPIO.input(27)
    if button_state == False:
        GPIO.output(23, True)
        print('Button Pressed...')
        time.sleep(0.2)

    else:
        GPIO.output(23, False)
        print("Button not Pressed...")
