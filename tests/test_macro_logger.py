import unittest
from unittest.mock import MagicMock, patch
from macro_logger.log_manager import MacroLogger

class TestMacroLogger(unittest.TestCase):
    def setUp(self):
        self.logger = MacroLogger(__name__)

    def test_log_messages(self):
        # Verifica se as mensagens são registradas corretamente
        self.logger.info("Teste de info")
        self.logger.warning("Teste de warning")
        self.logger.error("Teste de erro")
        self.logger.debug("Teste de debug")

        # Verifica se as mensagens foram registradas no logger
        self.assertIn("Teste de info", self.logger.logger.handlers[0].stream.getvalue())
        self.assertIn("Teste de warning", self.logger.logger.handlers[0].stream.getvalue())
        self.assertIn("Teste de erro", self.logger.logger.handlers[0].stream.getvalue())
        self.assertIn("Teste de debug", self.logger.logger.handlers[0].stream.getvalue())

    @patch("macro_logger.log_manager.upload_to_gcp_bucket")
    def test_upload_logs(self, mock_upload):
        # Define um limite pequeno para os logs
        logger = MacroLogger(__name__, cron_time=1, log_threshold=2, bucket="test-bucket")

        # Registra três mensagens de log
        logger.info("Teste de info 1")
        logger.warning("Teste de warning 1")
        logger.error("Teste de erro 1")

        # Verifica se o envio para o bucket não ocorreu
        mock_upload.assert_not_called()

        # Registra mais uma mensagem de log, ultrapassando o limite
        logger.info("Teste de info 2")

        # Verifica se o envio para o bucket ocorreu após ultrapassar o limite
        mock_upload.assert_called_once()

if __name__ == "__main__":
    unittest.main()
