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
    GPIO.setmode(GPIO.BCM)
    for i in pins:
        GPIO.cleanup(i)
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)


def teardown(pins):
    """
    Performs GPIO cleanup
    :return: None
    """
    for i in pins:
        GPIO.output(i, GPIO.HIGH)
        GPIO.cleanup(i)


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
        GPIO.setup(i, GPIO.IN)
        if GPIO.input(i) != GPIO.LOW:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)
    time.sleep(work_time)
    for i in pins:
        GPIO.setup(i, GPIO.IN)
        if GPIO.input(i) != GPIO.HIGH:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
    time.sleep(sleep_time)


def continuous_work(remaining_time, pins, on_time):
    """
    Performs job if needed and waits for remaining time.
    :param remaining_time:
    :param on_time:
    :param pins:
    :return: None
    """
    if on_time:
        for i in pins:
            GPIO.setup(i, GPIO.IN)
            if GPIO.input(i) != GPIO.LOW:
                GPIO.setup(i, GPIO.OUT)
                GPIO.output(i, GPIO.LOW)
    else:
        for i in pins:
            GPIO.setup(i, GPIO.IN)
            if GPIO.input(i) != GPIO.HIGH:
                GPIO.setup(i, GPIO.OUT)
                GPIO.output(i, GPIO.HIGH)
    time.sleep(remaining_time)


def get_remaining_time(time_goal):
    """
    Returns remaining time in seconds between current time and specified goal.
    :param time_goal:
    :return: remaining_time
    """
    now = datetime.datetime.now()
    return (datetime.timedelta(hours=24) - (now - now.replace(hour=time_goal,
                                                              minute=0,
                                                              second=0,
                                                              microsecond=0)
                                            )
            ).total_seconds() % (24 * 3600)


def get_time_goal(start, end, on_time):
    """
    Gets current time goal.
    :param start:
    :param end:
    :param on_time:
    :return time_goal:
    """
    if on_time:
        time_goal = end
    else:
        time_goal = start

    return time_goal


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
