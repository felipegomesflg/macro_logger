from setuptools import setup, find_packages

setup(
    name='macro_logger',
    version='0.1',
    description='A logging library for macro level logging',
    packages=find_packages(),
    install_requires=[
        'google-cloud-storage>=1.38.0',
        'APScheduler>=3.8.0',
    ],
)
