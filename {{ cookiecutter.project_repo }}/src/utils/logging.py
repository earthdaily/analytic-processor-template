import logging
import os


class LogFilter(logging.Filter):

    def __init__(self):
        pass

def get_logger():
    return logger

class ContextFilter:
    context = None
    def __init__(self, context: dict):
        self.context = context

    def filter(self, record):
        pass

logger = get_logger('processors')
