#!/usr/bin/python
import RPi.GPIO as GPIO
import time

from constants import PINS, SLEEP_TIME, WORK_TIME

GPIO.setmode(GPIO.BCM)

def main():

    for i in PINS:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

    while True:
        for i in PINS:
            GPIO.output(i, GPIO.LOW)
        time.sleep(WORK_TIME)
        for i in PINS:
            GPIO.output(i, GPIO.HIGH)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
