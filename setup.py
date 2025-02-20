from setuptools import setup, find_packages

setup(
    name="exchagne",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests==2.31.0',
        'python-binance==1.0.19',
        'python-dotenv==1.0.0',
        'beautifulsoup4==4.12.2',
    ],
)
