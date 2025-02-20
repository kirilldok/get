from RPi import GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN)
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, GPIO.input(21))
# GPIO.output(24, GPIO.input(21))

# GPIO.cleanup()
