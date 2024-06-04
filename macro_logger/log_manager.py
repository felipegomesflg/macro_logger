from .file_handler import FileHandler
from .gcp_sender import GCPSender

class LogManager:
    def __init__(self, name, cron_time=60, log_threshold=1000, bucket=None):
        self.name = name
        self.file_handler = FileHandler(name)
        self.gcp_sender = GCPSender(bucket)

        self.cron_time = cron_time
        self.log_threshold = log_threshold

    def info(self, message):
        logger = self.file_handler.get_logger()
        logger.info(message)
        self._schedule_upload_logs()

    def warning(self, message):
        logger = self.file_handler.get_logger()
        logger.warning(message)
        self._schedule_upload_logs()

    def error(self, message):
        logger = self.file_handler.get_logger()
        logger.error(message)
        self._schedule_upload_logs()

    def debug(self, message):
        logger = self.file_handler.get_logger()
        logger.debug(message)
        self._schedule_upload_logs()

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
            storage_client = storage.Client()
            bucket = storage_client.bucket(self.bucket)
            blob = bucket.blob(f"logs/logs_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json")
            blob.upload_from_filename(log_file)

    def _schedule_upload_logs(self):
        if self._should_upload_logs():
            self._upload_logs_to_gcp()

    def start_scheduler(self):
        # Implemente a lógica de agendamento aqui
        print(f"Agendamento iniciado a cada {self.cron_time} segundos.")

    def stop_scheduler(self):
        # Implemente a lógica para parar o agendamento aqui
        print("Agendamento parado.")
