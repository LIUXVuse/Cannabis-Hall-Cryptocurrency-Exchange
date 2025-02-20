import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
import threading
import time
from src.services.exchange_service import ExchangeService
from src.config import WINDOW_TITLE, WINDOW_SIZE, SUPPORTED_CRYPTOCURRENCIES

class MainWindow:
    def __init__(self):
        """初始化主窗口"""
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry("1200x900")  # 增加寬度和高度以適應更大的顯示
        
        # 設置默認字體
        default_font = ('Microsoft YaHei UI', 10)  # 使用支援中文和泰文的字體
        self.root.option_add('*Font', default_font)
        
        self.exchange_service = ExchangeService()
        
        # 創建左右主框架
        self.left_frame = ttk.Frame(self.root, padding="10")
        self.left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.right_frame = ttk.Frame(self.root, padding="10")
        self.right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置列權重，使右側框架占據更多空間
        self.root.grid_columnconfigure(1, weight=2)
        
        self._setup_ui()
        self._setup_auto_refresh()

    def _setup_ui(self):
        """設置用戶界面"""
        # 左側 - 輸入區域
        input_frame = ttk.LabelFrame(self.left_frame, text="輸入", padding="5")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(input_frame, text="泰銖金額:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(input_frame, width=30)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="選擇加密貨幣:").grid(row=1, column=0, padx=5, pady=5)
        self.crypto_var = tk.StringVar(value=SUPPORTED_CRYPTOCURRENCIES[0])
        crypto_combo = ttk.Combobox(input_frame, textvariable=self.crypto_var, width=27)
        crypto_combo['values'] = SUPPORTED_CRYPTOCURRENCIES
        crypto_combo.grid(row=1, column=1, padx=5, pady=5)
        
        # 計算按鈕
        ttk.Button(input_frame, text="計算", command=self._calculate).grid(row=2, column=0, columnspan=2, pady=10)
        
        # 左側 - 計算詳情
        result_frame = ttk.LabelFrame(self.left_frame, text="計算詳情", padding="5")
        result_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.result_label = ttk.Label(result_frame, text="等待計算...", font=('Microsoft YaHei UI', 10))
        self.result_label.grid(row=0, column=0, padx=5, pady=5)
        
        # 左側 - 匯率信息
        rates_frame = ttk.LabelFrame(self.left_frame, text="當前匯率", padding="5")
        rates_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.rates_label = ttk.Label(rates_frame, text="正在獲取匯率...", font=('Microsoft YaHei UI', 10))
        self.rates_label.grid(row=0, column=0, padx=5, pady=5)
        
        # 左側 - 設置
        settings_frame = ttk.LabelFrame(self.left_frame, text="設置", padding="5")
        settings_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(settings_frame, text="USDT手續費率(%):").grid(row=0, column=0, padx=5, pady=5)
        self.usdt_fee_entry = ttk.Entry(settings_frame)
        self.usdt_fee_entry.insert(0, str(self.exchange_service.fees['USDT'] * 100))
        self.usdt_fee_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(settings_frame, text="其他幣種手續費率(%):").grid(row=1, column=0, padx=5, pady=5)
        self.other_fee_entry = ttk.Entry(settings_frame)
        self.other_fee_entry.insert(0, str(self.exchange_service.fees['OTHER'] * 100))
        self.other_fee_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(settings_frame, text="保存設置", command=self._save_settings).grid(row=2, column=0, columnspan=2, pady=10)
        
        # 右側 - 最終價格顯示（置中且更大）
        self.right_frame.grid_rowconfigure(0, weight=1)  # 使內容垂直置中
        self.right_frame.grid_columnconfigure(0, weight=1)  # 使內容水平置中
        
        final_price_frame = ttk.LabelFrame(self.right_frame, text="最終價格", padding="30")
        final_price_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W), padx=20, pady=20)
        
        final_price_frame.grid_rowconfigure(0, weight=1)  # 使標籤垂直置中
        final_price_frame.grid_columnconfigure(0, weight=1)  # 使標籤水平置中
        
        self.final_price_label = ttk.Label(
            final_price_frame, 
            text="等待計算...", 
            font=('Microsoft YaHei UI', 48, 'bold'),  # 使用更大字體
            wraplength=500,  # 增加換行寬度
            justify='center'  # 文字置中對齊
        )
        self.final_price_label.grid(row=0, column=0, padx=30, pady=30, sticky=(tk.N, tk.S, tk.E, tk.W))

    def _setup_auto_refresh(self):
        """設置自動刷新"""
        def refresh_rates():
            while True:
                try:
                    self.rates_label.config(text="正在更新匯率數據...")
                    self.exchange_service.update_rates()
                    rates = self.exchange_service.get_current_rates()
                    
                    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    rates_text = f"最後更新時間: {current_time}\n\n"
                    rates_text += f"THB/USD: {rates['THB_RATE']:.2f}\n"
                    rates_text += f"當前手續費率:\n"
                    rates_text += f"- USDT: {self.exchange_service.fees['USDT']*100:.1f}%\n"
                    rates_text += f"- 其他: {self.exchange_service.fees['OTHER']*100:.1f}%\n\n"
                    
                    rates_text += "加密貨幣價格:\n"
                    for crypto in SUPPORTED_CRYPTOCURRENCIES:
                        if crypto != 'USDT':
                            if rates[crypto] is None:
                                rates_text += f"- {crypto}/USDT: 無法獲取價格\n"
                            else:
                                rates_text += f"- {crypto}/USDT: {rates[crypto]:,.2f}\n"
                    
                    self.rates_label.config(text=rates_text)
                    
                except Exception as e:
                    error_text = f"更新失敗: {str(e)}\n"
                    error_text += "將在30秒後重試..."
                    self.rates_label.config(text=error_text)
                    print(f"匯率更新錯誤: {str(e)}")
                
                time.sleep(30)  # 每30秒更新一次
        
        # 在後台線程中運行更新
        thread = threading.Thread(target=refresh_rates, daemon=True)
        thread.start()

    def _calculate(self):
        """執行計算"""
        try:
            amount = float(self.amount_entry.get())
            crypto = self.crypto_var.get()
            
            # 檢查是否選擇了無法獲取價格的加密貨幣
            rates = self.exchange_service.get_current_rates()
            if crypto != 'USDT' and rates[crypto] is None:
                raise Exception(f"無法獲取{crypto}的價格，請選擇其他加密貨幣")
            
            crypto_amount, rate, fee = self.exchange_service.calculate_exchange(amount, crypto)
            
            # 獲取手續費率
            fee_rate = self.exchange_service.fees['USDT'] if crypto == 'USDT' else self.exchange_service.fees['OTHER']
            
            # 計算總金額（泰銖）
            total_thb = amount + (fee * rate)
            
            # 更新詳細結果
            result_text = f"計算詳情:\n"
            result_text += f"輸入金額: {amount:,.2f} THB\n"
            result_text += f"手續費({fee_rate*100:.1f}%): {fee:,.2f} USD (約 {fee*rate:,.2f} THB)\n"
            result_text += f"總支付金額: {total_thb:,.2f} THB\n"
            result_text += f"當前匯率: {rate:,.2f} THB/USD"
            
            self.result_label.config(text=result_text)
            
            # 更新最終價格顯示
            final_price_text = f"您將獲得:\n\n{crypto_amount:,.8f}\n{crypto}"
            self.final_price_label.config(text=final_price_text)
            
        except ValueError as e:
            messagebox.showerror("輸入錯誤", "請輸入有效的數字金額")
        except Exception as e:
            messagebox.showerror("計算錯誤", str(e))

    def _save_settings(self):
        """保存設置"""
        try:
            usdt_fee = float(self.usdt_fee_entry.get()) / 100  # 轉換百分比為小數
            other_fee = float(self.other_fee_entry.get()) / 100  # 轉換百分比為小數
            
            if not (0 <= usdt_fee <= 1 and 0 <= other_fee <= 1):
                raise ValueError("手續費率必須在0-100之間")
            
            self.exchange_service.set_fee('USDT', usdt_fee)
            self.exchange_service.set_fee('OTHER', other_fee)
            
            messagebox.showinfo("成功", "設置已保存")
        except ValueError as e:
            messagebox.showerror("錯誤", str(e))

    def run(self):
        """運行主窗口"""
        self.root.mainloop()
