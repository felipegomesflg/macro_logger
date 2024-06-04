import os
import logging
from logging.handlers import RotatingFileHandler

class FileHandler:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        log_file = os.path.join(log_directory, "logs.json")

        handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
