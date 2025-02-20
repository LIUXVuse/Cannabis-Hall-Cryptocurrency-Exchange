#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from src.gui.main_window import MainWindow

def check_environment():
    """檢查環境配置"""
    env_file = Path('.env')
    if not env_file.exists():
        print("錯誤: 未找到.env文件")
        print("請根據.env.example創建.env文件並配置必要的API密鑰")
        sys.exit(1)

def main():
    """主程序入口"""
    try:
        print("正在啟動加密貨幣匯率計算工具...")
        
        # 檢查環境配置
        print("檢查環境配置...")
        check_environment()
        print("環境配置檢查完成")
        
        # 創建並運行主窗口
        print("正在初始化主窗口...")
        window = MainWindow()
        print("主窗口初始化完成，開始運行程序")
        window.run()
        
    except Exception as e:
        print(f"程序運行錯誤: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
