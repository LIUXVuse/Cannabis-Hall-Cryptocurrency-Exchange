from binance.client import Client
from src.config import BINANCE_API_KEY, BINANCE_API_SECRET

class BinanceAPI:
    def __init__(self):
        """初始化Binance API客戶端"""
        self.client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

    def get_price(self, symbol: str) -> float:
        """
        獲取指定交易對的當前價格
        
        Args:
            symbol: 交易對符號（例如：'BTCUSDT'）
            
        Returns:
            float: 當前價格
            
        Raises:
            Exception: 當API調用失敗時拋出異常
        """
        try:
            ticker = self.client.get_symbol_ticker(symbol=f"{symbol}USDT")
            return float(ticker['price'])
        except Exception as e:
            raise Exception(f"獲取{symbol}價格失敗: {str(e)}")

    def get_all_prices(self) -> dict:
        """
        獲取所有支持的加密貨幣價格
        
        Returns:
            dict: 包含所有支持的加密貨幣價格的字典
        """
        prices = {}
        try:
            from src.config import SUPPORTED_CRYPTOCURRENCIES
            for symbol in SUPPORTED_CRYPTOCURRENCIES:
                if symbol != 'USDT':  # 跳過USDT，因為它的價格固定為1
                    try:
                        prices[symbol] = self.get_price(symbol)
                    except Exception as e:
                        print(f"無法獲取{symbol}價格: {str(e)}")
                        prices[symbol] = None  # 設置為None表示無法獲取價格
            prices['USDT'] = 1.0  # USDT固定為1美元
            return prices
        except Exception as e:
            raise Exception(f"獲取價格失敗: {str(e)}")
