from setuptools import setup, find_packages

setup(
    name='macro-logger',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'google-cloud-storage'
    ],
    description='Uma biblioteca de logging para registro de logs em arquivos e envio automático para a GCP.',
    author='Felipe Gomes',
    author_email='seu-email@example.com',
    url='https://github.com/felipegomesflg/macro_logger',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)