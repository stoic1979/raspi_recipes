#
# A quick test to read from push button
#
# Refer the wiring diagram - wiring.png
# Connect jumper cables pin 3 GND and
# GPIO 18 to push button
#

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
