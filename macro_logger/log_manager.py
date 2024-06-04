import logging
from logging.handlers import RotatingFileHandler
from apscheduler.schedulers.background import BackgroundScheduler
from .connection import upload_to_gcp_bucket

class MacroLogger:
    def __init__(self, name=None, cron_time=60, log_threshold=1000, bucket=None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Configure file handler for log rotation
        log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = RotatingFileHandler('logs/logs.json', maxBytes=10000, backupCount=1)
        file_handler.setFormatter(log_formatter)
        self.logger.addHandler(file_handler)

        # Configure scheduler for log upload
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.check_and_upload_logs, 'interval', seconds=cron_time)
        self.scheduler.start()

        # Set custom log threshold
        self.log_threshold = log_threshold

        # Set custom bucket
        self.bucket = bucket

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def check_and_upload_logs(self):
        with open('logs/logs.json', 'r') as file:
            logs = file.readlines()
            if len(logs) >= self.log_threshold:
                upload_to_gcp_bucket(logs, self.bucket)
                open('logs/logs.json', 'w').close()
