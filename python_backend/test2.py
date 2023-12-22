import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)

while True:
	GPIO.output(9, 0)
	time.sleep(10)
	GPIO.output(9, 1)
	time.sleep(10)
