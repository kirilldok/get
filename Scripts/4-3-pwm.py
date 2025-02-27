import RPi.GPIO as gpio
import sys
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)

n=10
pwm=gpio.PWM(21, 1000)
pwm.start(0)

try:
        while True:
                DutyCicle=int(input())
                pwm.ChangeDutyCycle(DutyCicle)
                print("{:.2f}".format(DutyCicle*3.3/100))
finally:
    pwm.stop()
    gpio.output(21, 0)
    gpio.cleanup()   