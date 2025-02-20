@echo off
chcp 65001 > nul
echo 正在啟動加密貨幣匯率計算工具...

REM 檢查虛擬環境是否存在
if not exist venv (
    echo 錯誤：未找到Python虛擬環境
    echo 請先運行 setup.bat 進行環境設置
    pause
    exit /b 1
)

REM 檢查.env文件
if not exist .env (
    echo 錯誤：未找到.env文件
    echo 請根據.env.example創建.env文件並配置必要的API密鑰
    pause
    exit /b 1
)

REM 啟動虛擬環境
call venv\Scripts\activate
if errorlevel 1 (
    echo 錯誤：啟動虛擬環境失敗
    pause
    exit /b 1
)

REM 運行應用程序
python src/main.py
if errorlevel 1 (
    echo 程序運行出錯，請檢查錯誤信息
    pause
    exit /b 1
)

pause
