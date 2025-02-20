import requests
from src.config import EXCHANGE_RATE_URL, EXCHANGE_RATE_PROFIT_FACTOR

class TTExchangeAPI:
    def __init__(self):
        """初始化匯率API客戶端"""
        self.url = EXCHANGE_RATE_URL
        self.session = requests.Session()

    def get_thb_rate(self) -> float:
        """
        獲取當前美元兌泰銖匯率
        
        Returns:
            float: 當前美元兌泰銖匯率
            
        Raises:
            Exception: 當無法獲取匯率時拋出異常
        """
        try:
            response = self.session.get(self.url)
            response.raise_for_status()
            data = response.json()
            
            # 從API響應中獲取THB匯率並應用利潤係數
            thb_rate = data['rates']['THB']
            adjusted_rate = float(thb_rate) * EXCHANGE_RATE_PROFIT_FACTOR
            return adjusted_rate
            
        except requests.RequestException as e:
            raise Exception(f"獲取匯率失敗: {str(e)}")
        except (KeyError, ValueError) as e:
            raise Exception(f"解析匯率數據失敗: {str(e)}")
        except Exception as e:
            raise Exception(f"獲取匯率時發生錯誤: {str(e)}")

    def is_available(self) -> bool:
        """
        檢查匯率API服務是否可用
        
        Returns:
            bool: 服務是否可用
        """
        try:
            response = self.session.get(self.url)
            return response.status_code == 200
        except:
            return False
