import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.OUT)

for i in range(0,5):
	GPIO.output(4,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(4,GPIO.LOW)
	time.sleep(5)

GPIO.cleanup()
