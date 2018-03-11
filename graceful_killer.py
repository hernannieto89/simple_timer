#!/usr/bin/python
"""
Simple timer - Graceful killer module.
"""
import signal


class GracefulKiller(object):  # pylint: disable=too-few-public-methods
    """
    Credits: https://stackoverflow.com/questions/18499497/
                    how-to-process-sigterm-signal-gracefully
    """
    def __init__(self):
        self.kill_now = False
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self):
        """
        Sets kill_now attribute to true. Allowing main module to break infinite loop.
        :return: None
        """
        self.kill_now = True
