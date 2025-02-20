@echo off
chcp 65001 > nul
echo 正在設置加密貨幣匯率計算工具環境...

REM 檢查Python是否安裝
python --version > nul 2>&1
if errorlevel 1 (
    echo 錯誤：未檢測到Python安裝
    echo 請先安裝Python 3.x，然後重新運行此腳本
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

REM 創建虛擬環境
echo 正在創建Python虛擬環境...
python -m venv venv
if errorlevel 1 (
    echo 錯誤：創建虛擬環境失敗
    pause
    exit /b 1
)

REM 啟動虛擬環境並安裝依賴
echo 正在安裝依賴包...
call venv\Scripts\activate
if errorlevel 1 (
    echo 錯誤：啟動虛擬環境失敗
    pause
    exit /b 1
)

pip install -r requirements.txt
if errorlevel 1 (
    echo 錯誤：安裝依賴包失敗
    pause
    exit /b 1
)

echo 環境設置完成！
echo 您現在可以運行 run.bat 來啟動應用程序
pause
