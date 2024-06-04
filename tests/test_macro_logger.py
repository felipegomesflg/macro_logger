import unittest
from macro_logger.logger import LogManager

class TestLogManager(unittest.TestCase):

    def setUp(self):
        self.logger = LogManager(__name__, bucket='test-bucket')

    def test_info_log(self):
        self.logger.info("Test info message")
        # Adicionar verificações apropriadas aqui

    def test_warning_log(self):
        self.logger.warning("Test warning message")
        # Adicionar verificações apropriadas aqui

    def test_error_log(self):
        self.logger.error("Test error message")
        # Adicionar verificações apropriadas aqui

    def test_debug_log(self):
        self.logger.debug("Test debug message")
        # Adicionar verificações apropriadas aqui

if __name__ == '__main__':
    unittest.main()
