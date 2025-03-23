#!/usr/bin/env python3
import os
import sys
import traceback
from pathlib import Path

# 簡單的測試函數
def test_print():
    print("測試打印 - 如果你能看到這個信息，則表明程序可以正常啟動")
    print(f"當前工作目錄: {os.getcwd()}")
    print(f"Python版本: {sys.version}")
    print("Python路徑:")
    for path in sys.path:
        print(f"  - {path}")
        
test_print()  # 立即執行測試

# 先捕獲所有導入錯誤
try:
    from src.gui.main_window import MainWindow
except Exception as e:
    print("導入錯誤:")
    print(f"錯誤類型: {type(e).__name__}")
    print(f"錯誤信息: {str(e)}")
    traceback.print_exc()
    sys.exit(1)

def main():
    """主程序入口"""
    try:
        print("正在啟動加密貨幣匯率計算工具...")
        
        # 測試導入其他必要模塊
        print("測試導入必要模塊...")
        try:
            import tkinter
            print("tkinter 導入成功")
        except ImportError as e:
            print(f"tkinter 導入失敗: {str(e)}")
            raise
            
        try:
            from binance.client import Client
            print("binance API 導入成功")
        except ImportError as e:
            print(f"binance API 導入失敗: {str(e)}")
            raise
            
        try:
            import requests
            print("requests 導入成功")
        except ImportError as e:
            print(f"requests 導入失敗: {str(e)}")
            raise
            
        try:
            from dotenv import load_dotenv
            print("dotenv 導入成功")
        except ImportError as e:
            print(f"dotenv 導入失敗: {str(e)}")
            raise
        
        # 創建並運行主窗口
        print("正在初始化主窗口...")
        window = MainWindow()
        print("主窗口初始化完成，開始運行程序")
        window.run()
        
    except Exception as e:
        print(f"程序運行錯誤: {str(e)}")
        print(f"錯誤類型: {type(e).__name__}")
        print("詳細錯誤信息:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
