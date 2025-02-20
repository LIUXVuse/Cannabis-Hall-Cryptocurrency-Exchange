@echo off
chcp 65001 > nul
echo 正在創建發布包...

REM 創建發布目錄
set RELEASE_DIR=release
set RELEASE_NAME=Cannabis-Hall-Cryptocurrency-Exchange-v1.0.0
set RELEASE_PATH=%RELEASE_DIR%\%RELEASE_NAME%

REM 清理舊的發布目錄
if exist %RELEASE_DIR% rd /s /q %RELEASE_DIR%
mkdir %RELEASE_PATH%

REM 複製必要文件
xcopy /E /I src %RELEASE_PATH%\src
copy requirements.txt %RELEASE_PATH%
copy .env.example %RELEASE_PATH%
copy setup.bat %RELEASE_PATH%
copy run.bat %RELEASE_PATH%
copy run.vbs %RELEASE_PATH%
copy README.md %RELEASE_PATH%

REM 創建zip文件
powershell Compress-Archive -Path %RELEASE_PATH% -DestinationPath %RELEASE_DIR%\%RELEASE_NAME%.zip

echo 發布包創建完成：%RELEASE_DIR%\%RELEASE_NAME%.zip
pause
