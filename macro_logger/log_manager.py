import os
import logging
from logging.handlers import RotatingFileHandler
from google.cloud import storage
from datetime import datetime

class LogManager:
    def __init__(self, name, cron_time=60, log_threshold=1000, bucket=None):
        self.name = name
        self.bucket = bucket
        self.cron_time = cron_time
        self.log_threshold = log_threshold
        self.logger = self._setup_logger(name)

    def _setup_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        log_file = os.path.join(log_directory, "logs.json")

        handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger

    def info(self, message):
        self.logger.info(message)
        self._schedule_upload_logs()

    def warning(self, message):
        self.logger.warning(message)
        self._schedule_upload_logs()

    def error(self, message):
        self.logger.error(message)
        self._schedule_upload_logs()

    def debug(self, message):
        self.logger.debug(message)
        self._schedule_upload_logs()

    def _should_upload_logs(self):
        log_file_handler = self.logger.handlers[0]
        log_file = log_file_handler.stream.name
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                line_count = sum(1 for line in f)
                print(line_count)
                print(self.log_threshold)
                return line_count >= self.log_threshold
        return False

    def _upload_logs_to_gcp(self):
        if self.bucket and os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
            log_file_handler = self.logger.handlers[0]
            log_file = log_file_handler.stream.name
            gcp_file_path = f"logs/logs_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
            self._send_to_gcp(log_file, gcp_file_path)

    def _send_to_gcp(self, local_file_path, gcp_file_path):
        storage_client = storage.Client()
        bucket = storage_client.bucket(self.bucket)
        blob = bucket.blob(gcp_file_path)
        blob.upload_from_filename(local_file_path)

    def _schedule_upload_logs(self):
        if self._should_upload_logs():
            if os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
                self._upload_logs_to_gcp()
            else:
                print("Arquivo não pode ser enviado para a GCP pois sua variável de ambiente 'GOOGLE_APPLICATION_CREDENTIALS' não foi setada corretamente.")
