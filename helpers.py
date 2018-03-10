#!/usr/bin/python
import RPi.GPIO as GPIO
from datetime import datetime, time

def setup(pins):

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    for i in pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

def teardown():
    GPIO.cleanup()

def got_to_work(start, end):
    now = datetime.now()
    now_time = now.time()
    start_time = time(start)
    end_time = time(end)

    if start_time < end_time:
        return now_time >= start_time and now_time <= end_time
    else: #Over midnight
        return now_time >= start_time or now_time <= end_time

def work(work_time, sleep_time, pins):
    for i in pins:
        GPIO.output(i, GPIO.LOW)
    time.sleep(work_time)
    for i in pins:
        GPIO.output(i, GPIO.HIGH)
    time.sleep(sleep_time)

def sanitize(args):
    time(args.start_time)
    time(args.end_time)
