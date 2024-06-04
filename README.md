# Macro Logger

[![PyPI](https://img.shields.io/badge/PyPI-PyPI-red.svg)](https://github.com/felipegomesflg/macro_logger)
[![GitHub repo](https://img.shields.io/badge/GitHub-Repo-green.svg)](https://github.com/felipegomesflg/macro_logger)
[![GitHub liscense](https://img.shields.io/badge/GitHub-Liscense-blue.svg)](https://github.com/felipegomesflg/macro_logger/blob/master/LICENSE)
![GitHub last commit](https://img.shields.io/github/last-commit/felipegomesflg/macro_logger)

### Utilização da Biblioteca Macro Logger
Uma biblioteca de logging para registro de logs em arquivos e envio automático para a GCP.

### Instalação

Você pode instalar a biblioteca usando pip:

```bash
pip install macro-logger
```


### Exemplo Prático
#### Estrutura
```lua
my_project/
|-- app.py
|-- config.env
|-- requirements.txt
|-- Dockerfile
```

### Conteúdop dos Arquivos
1. config.env
```plaintext
CRON_TIME=60
LOG_THRESHOLD=1000
BUCKET_NAME=seu-bucket-gcp
```

2. app.py

```python
import os
from dotenv import load_dotenv
from macro_logger.logger import LogManager

# Carregar variáveis de ambiente do arquivo .env
load_dotenv('config.env')

# Recuperar configurações das variáveis de ambiente
cron_time = int(os.getenv('CRON_TIME', 60))
log_threshold = int(os.getenv('LOG_THRESHOLD', 1000))
bucket_name = os.getenv('BUCKET_NAME')

# Criar uma instância do logger com as configurações
logger = LogManager(__name__, cron_time=cron_time, log_threshold=log_threshold, bucket=bucket_name)

def main():
    # Registrar mensagens de log
    logger.info("Iniciando o meu projeto...")
    logger.warning("Este é um aviso importante!")
    logger.error("Ocorreu um erro no meu projeto.")
    logger.debug("Informações de depuração...")

if __name__ == "__main__":
    main()

```

3. requirements.txt
```plaintext
macro-logger
python-dotenv
```
5. Dockerfile
```dockerfile
    # Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . .

# Instalar as dependências
RUN pip install -r requirements.txt

# Definir a variável de ambiente para o Google Cloud Storage
ENV GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"

# Executar o aplicativo
CMD ["python", "app.py"]
```

### Passos para configuração

1. **Instalar Dependências**
No terminal, navegue até o diretório do projeto e execute:
    ```bash
    pip install -r requirements.txt
    ```

2. **Configurar Credenciais do GCP**
Certifique-se de que o caminho para o arquivo de credenciais do Google Cloud Storage seja configurado corretamente no Dockerfile. Substitua "/path/to/your/credentials.json" pelo caminho real do arquivo de credenciais.

3. **Construir e Executar o Contêiner Docker**
Navegue até o diretório do projeto e execute os seguintes comandos para construir e executar o contêiner Docker:
    ```bash
    docker build -t my_project .
    docker run --env-file config.env my_project
    ```
#### Explicação do Código
* config.env: Contém as configurações que serão carregadas como variáveis de ambiente.
* app.py: Carrega as variáveis de ambiente usando dotenv, configura o logger com os valores carregados e registra algumas mensagens de log.
* requirements.txt: Lista as dependências do projeto, incluindo macro-logger e python-dotenv.
* Dockerfile: Define a configuração do contêiner Docker, incluindo a instalação das dependências e a definição das variáveis de ambiente necessárias para o Google Cloud Storage.
