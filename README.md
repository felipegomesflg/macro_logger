# Macro Logger

![PyPI](https://img.shields.io/pypi/v/macro-logger)
![GitHub last commit](https://img.shields.io/github/last-commit/username/repository)

### Utilização da Biblioteca Macro Logger
Uma biblioteca de logging para registro de logs em arquivos e envio automático para a GCP.

### Instalação

Você pode instalar a biblioteca usando pip:

```bash
pip install macro-logger
```


### Utilização
#### Enviando Variáveis de Configuração
Você pode enviar variáveis de configuração, como o tempo do cron, o limiar de logs e o endereço do bucket, ao criar uma instância da classe MacroLogger. Veja um exemplo de como fazer isso:

```python
from macro_logger.log_manager import MacroLogger

# Definindo variáveis de configuração
cron_time = 30  # segundos
log_threshold = 500
bucket_name = "meu-bucket"

# Criando uma instância do logger com variáveis de configuração
logger = MacroLogger(__name__, cron_time=cron_time, log_threshold=log_threshold, bucket=bucket_name)

def main():
    # Registra mensagens de log
    logger.info("Iniciando o meu projeto...")
    logger.warning("Este é um aviso importante!")
    logger.error("Ocorreu um erro no meu projeto.")
    logger.debug("Informações de depuração...")

if __name__ == "__main__":
    main()
```

Neste exemplo, definimos as variáveis ``cron_time``. ``log_threshold`` e ``bucket_name`` com os valores desejados e, em seguida, passamos essas variáveis ao criar uma instância da classe MacroLogger. Isso permite que você personalize as configurações de tempo do cron, limiar de logs e endereço do bucket conforme necessário para o seu projeto específico.

Certifique-se de ajustar os valores das variáveis de configuração de acordo com suas necessidades.
