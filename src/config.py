import os
from dotenv import load_dotenv

# 加載環境變量
load_dotenv()

# Binance API配置
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY', '')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET', '')

# Exchange Rate API配置
EXCHANGE_RATE_URL = "https://api.exchangerate-api.com/v4/latest/USD"
EXCHANGE_RATE_PROFIT_FACTOR = 0.993  # 將API匯率乘以0.993，使33.67變為33.43

# 默認手續費配置
DEFAULT_USDT_FEE = 0.05  # 5%
DEFAULT_OTHER_CRYPTO_FEE = 0.08  # 8%

# 支持的加密貨幣列表
SUPPORTED_CRYPTOCURRENCIES = ['USDT', 'BTC', 'ETH', 'BNB', 'ADA', 'XRP', 'DOGE']

# GUI配置
WINDOW_TITLE = "Cannabis Hall Cryptocurrency Exchange"
WINDOW_SIZE = "800x800"
