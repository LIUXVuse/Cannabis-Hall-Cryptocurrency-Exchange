from typing import Dict, Tuple
from src.api.binance_client import BinanceAPI
from src.api.tt_exchange_client import TTExchangeAPI
from src.config import DEFAULT_USDT_FEE, DEFAULT_OTHER_CRYPTO_FEE, SUPPORTED_CRYPTOCURRENCIES

class ExchangeService:
    def __init__(self):
        """初始化匯率計算服務"""
        self.binance_api = BinanceAPI()
        self.tt_exchange_api = TTExchangeAPI()
        self.crypto_prices: Dict[str, float] = {}
        self.thb_rate: float = 0.0
        self.fees = {
            'USDT': DEFAULT_USDT_FEE,
            'OTHER': DEFAULT_OTHER_CRYPTO_FEE
        }

    def update_rates(self) -> None:
        """
        更新所有匯率數據
        
        Raises:
            Exception: 當更新失敗時拋出異常
        """
        try:
            # 更新加密貨幣價格
            self.crypto_prices = self.binance_api.get_all_prices()
            # 更新泰銖匯率
            self.thb_rate = self.tt_exchange_api.get_thb_rate()
        except Exception as e:
            raise Exception(f"更新匯率失敗: {str(e)}")

    def set_fee(self, crypto: str, fee: float) -> None:
        """
        設置特定加密貨幣的手續費率
        
        Args:
            crypto: 加密貨幣代碼
            fee: 手續費率（0-1之間的小數）
        
        Raises:
            ValueError: 當手續費率無效時拋出異常
        """
        if not 0 <= fee <= 1:
            raise ValueError("手續費率必須在0到1之間")
        
        if crypto == 'USDT':
            self.fees['USDT'] = fee
        else:
            self.fees['OTHER'] = fee

    def calculate_exchange(self, thb_amount: float, target_crypto: str) -> Tuple[float, float, float]:
        """
        計算泰銖兌換成加密貨幣的數量
        
        Args:
            thb_amount: 泰銖金額
            target_crypto: 目標加密貨幣代碼
            
        Returns:
            Tuple[float, float, float]: (加密貨幣數量, 使用的匯率, 手續費金額)
            
        Raises:
            ValueError: 當輸入參數無效時拋出異常
        """
        if target_crypto not in SUPPORTED_CRYPTOCURRENCIES:
            raise ValueError(f"不支持的加密貨幣: {target_crypto}")
        
        if thb_amount <= 0:
            raise ValueError("金額必須大於0")
        
        # 確保有最新匯率
        if not self.crypto_prices or self.thb_rate == 0:
            self.update_rates()
        
        # 計算美元金額
        usd_amount = thb_amount / self.thb_rate
        
        # 獲取適用的手續費率
        fee_rate = self.fees['USDT'] if target_crypto == 'USDT' else self.fees['OTHER']
        
        # 計算手續費（加到總額上）
        fee_amount = usd_amount * fee_rate
        
        # 計算實際需要支付的金額（原金額 + 手續費）
        total_amount = usd_amount + fee_amount
        
        # 計算加密貨幣數量
        crypto_price = self.crypto_prices[target_crypto]
        crypto_amount = usd_amount * (1 + fee_rate) / crypto_price
        
        return crypto_amount, self.thb_rate, fee_amount

    def get_current_rates(self) -> Dict[str, float]:
        """
        獲取當前所有匯率信息
        
        Returns:
            Dict[str, float]: 包含所有匯率信息的字典
        """
        return {
            'THB_RATE': self.thb_rate,
            **self.crypto_prices
        }
