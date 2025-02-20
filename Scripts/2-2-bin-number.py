import RPi.GPIO as GPIO
import time

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
number = [1,  1, 0, 0, 0, 0,  1, 1]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

for j in range(8):
    GPIO.output(dac[j], number[j])
    
time.sleep(15)
GPIO.output(dac, 0)