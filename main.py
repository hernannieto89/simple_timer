#!/usr/bin/python
import argparse
from helpers import teardown, got_to_work, setup, work, sanitize

def main():

    parser = argparse.ArgumentParser(description='Simple timer.')
    parser.add_argument('--pins',
                        action='store',
                        nargs='+',
                        type=int,
                        required=True,
                        help='raspberry pins GPIO.BCM mode')
    parser.add_argument('--start_time',
                        type=int,
                        required=True,
                        help='start time for timer (between 0 and 23)')
    parser.add_argument('--end_time',
                        type=int,
                        required=True,
                        help='end time for timer (between 0 and 23)')
    parser.add_argument('--work_time',
                        type=int,
                        required=True,
                        help='work time for timer (in seconds)')
    parser.add_argument('--sleep_time',
                        type=int,
                        required=True,
                        help='sleep time for timer (in seconds)')

    args = parser.parse_args()
    #sanitizes args
    sanitize(args)
    start = args.start_time
    end = args.end_time
    pins = args.pins
    work_time = args.work_time
    sleep_time = args.sleep_time
    # Cleanup in case power shutdowm
    teardown()
    # setup GPIO
    setup(pins)

    try:
        while True:
            if got_to_work(start, end):
                work(work_time, sleep_time, pins)
    except KeyboardInterrupt:
		# End program cleanly with keyboard
        print  "KeyboardInterrupt captured. Cleaning and exiting..."
		# Reset GPIO settings
		teardown()

if __name__ == "__main__":
	main()
