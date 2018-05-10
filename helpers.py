#!/usr/bin/python
"""
Simple timer - Helpers module.
"""
import os
import sys
import datetime
import time
import RPi.GPIO as GPIO


def setup(pins):
    """
    GPIO setup.
    :param pins:
    :return: None
    """

    GPIO.setwarnings(False)
    #GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    for i in pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)


def teardown(pins):
    """
    Performs GPIO cleanup
    :return: None
    """
    for i in pins:
        GPIO.output(i, GPIO.HIGH)
    GPIO.cleanup()


def got_to_work(start, end):
    """
    Ask if actual hour is within start - end range.
    :param start:
    :param end:
    :return: Boolean
    """
    now = datetime.datetime.now()
    now_time = now.time()
    start_time = datetime.time(start)
    end_time = datetime.time(end)

    if start_time < end_time:
        return now_time >= start_time and now_time <= end_time
    # Over midnight
    return now_time >= start_time or now_time <= end_time


def work(work_time, sleep_time, pins):
    """
    Performs job for work_time, sleeps for sleep_time.
    :param work_time:
    :param sleep_time:
    :param pins:
    :return: None
    """
    for i in pins:
        GPIO.output(i, GPIO.LOW)
    time.sleep(work_time)
    for i in pins:
        GPIO.output(i, GPIO.HIGH)
    time.sleep(sleep_time)


def continuous_work(work_time, pins, on_time):
    """
    Performs job for work_time.
    :param work_time:
    :param on_time:
    :param pins:
    :return: None
    """
    if on_time:
        for i in pins:
            GPIO.output(i, GPIO.LOW)
        time.sleep(work_time)
    else:
        for i in pins:
            GPIO.output(i, GPIO.HIGH)


def sanitize(args):
    """
    Sanitizes start_time and end_time parameters.
    :param args
    :return: None
    """
    datetime.time(args.start_time)
    datetime.time(args.end_time)


def check_sudo():
    """
    Checks for superuser privileges.
    :return: None
    """
    if os.getuid() != 0:
        print >> sys.stderr, "You need to have root privileges to run this script.\n" \
                             "Please try again, this time using 'sudo'. Exiting."
        sys.exit(1)
