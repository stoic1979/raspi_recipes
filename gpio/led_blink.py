#
# LED blink test on GPIO 13
#

import RPi.GPIO as GPIO
import time

def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

pin = 13

print "Running blink test..."

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channels
GPIO.setup(pin, GPIO.OUT)

print "GPIO setup done"

for i in range(0, 5):
    print "blinking", i
    blink(pin)

print "cleanup"
GPIO.cleanup() 

print "-- done --"
