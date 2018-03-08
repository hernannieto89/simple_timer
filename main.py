#!/usr/bin/python
import RPi.GPIO as GPIO
import time

from constants import PINS, SLEEP_TIME, WORK_TIME

GPIO.setmode(GPIO.BCM)

def main():
	
	for i in PINS:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.HIGH)

	try:
		while True:
			for i in PINS:
				GPIO.output(i, GPIO.LOW)
			time.sleep(WORK_TIME)
			for i in PINS:
				GPIO.output(i, GPIO.HIGH)
			time.sleep(SLEEP_TIME)
	except KeyboardInterrupt:
		# End program cleanly with keyboard
		print  "KeyboardInterrupt captured. Cleaning and exiting..."
		# Reset GPIO settings
		GPIO.cleanup()

if __name__ == "__main__":			
	main()
