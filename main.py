#!/usr/bin/python
"""
Simple timer - Main module.
"""
import argparse
from graceful_killer import GracefulKiller
from helpers import teardown, got_to_work, setup, work, sanitize


def main():
    """
    Simple timer.
    """

    parser = argparse.ArgumentParser(description='Simple timer.')
    parser.add_argument('--pins',
                        action='store',
                        dest='pins',
                        nargs='+',
                        type=int,
                        required=True,
                        help='raspberry pins GPIO.BCM mode')
    parser.add_argument('--start_time',
                        action='store',
                        dest='start_time',
                        type=int,
                        required=True,
                        help='start time for timer (between 0 and 23)')
    parser.add_argument('--end_time',
                        action='store',
                        dest='end_time',
                        type=int,
                        required=True,
                        help='end time for timer (between 0 and 23)')
    parser.add_argument('--work_time',
                        action='store',
                        dest='work_time',
                        type=int,
                        required=True,
                        help='work time for job (in seconds)')
    parser.add_argument('--sleep_time',
                        action='store',
                        dest='sleep_time',
                        type=int,
                        required=True,
                        help='sleep time for job (in seconds)')

    args = parser.parse_args()
    # sanitizes args
    sanitize(args)
    start = args.start_time
    end = args.end_time
    pins = args.pins
    work_time = args.work_time
    sleep_time = args.sleep_time
    # setup GPIO
    setup(pins)
    try:
        killer = GracefulKiller()
        while True:
            if killer.kill_now:
                break
            if got_to_work(start, end):
                work(work_time, sleep_time, pins)
        print "Program killed gracefully. Cleaning and exiting..."
    except KeyboardInterrupt:
        # End program cleanly with keyboard
        print "KeyboardInterrupt captured. Cleaning and exiting..."
    # Reset GPIO settings
    teardown()


if __name__ == "__main__":
    main()
