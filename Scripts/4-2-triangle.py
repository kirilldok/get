import RPi.GPIO as gpio
import sys
from time import sleep
dac=[8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def perev(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]

try:
    while (True):
        T=input()
        if not T.isdigit():
            print('input digit')
        t= float(T)/256/2
        for i in range(256):
            gpio.output(dac, perev(i, 8))
            
        for i in range(255, -1, -1):
            gpio.output(dac, perev(i, 8))
            
finally:
    gpio.output(dac, 1)
    gpio.cleanup()
  