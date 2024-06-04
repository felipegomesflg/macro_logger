import os
import json
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

class MacroLogger:
    def __init__(self, name, cron_time=60, log_threshold=1000, bucket=None):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Configuração do handler de arquivo de log
        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        log_file = os.path.join(log_directory, "logs.json")

        handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

        self.cron_time = cron_time
        self.log_threshold = log_threshold
        self.bucket = bucket

    def _should_upload_logs(self):
        if len(self.logger.handlers) > 0:
            log_file_handler = self.logger.handlers[0]
            if hasattr(log_file_handler, 'stream'):
                log_file = log_file_handler.stream.name
                if os.path.exists(log_file):
                    with open(log_file, 'r') as f:
                        line_count = sum(1 for line in f)
                        return line_count >= self.log_threshold
        return False

    def _upload_logs_to_gcp(self):
        if self.bucket:
            # Implemente a lógica de upload para o bucket na GCP aqui
            print("Logs enviados para o bucket na GCP.")

    def _schedule_upload_logs(self):
        if self._should_upload_logs():
            self._upload_logs_to_gcp()

    def _start_schedule(self):
        # Implemente a lógica de agendamento aqui
        print(f"Agendamento iniciado a cada {self.cron_time} segundos.")

    def _stop_schedule(self):
        # Implemente a lógica para parar o agendamento aqui
        print("Agendamento parado.")

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
