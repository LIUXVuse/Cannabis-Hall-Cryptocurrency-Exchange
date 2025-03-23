@echo off
chcp 65001 > nul
echo 打包加密貨幣匯率計算工具...

REM 創建臨時目錄
mkdir temp_package

REM 複製必要的文件
echo 正在複製必要文件...
xcopy src temp_package\src\ /E /I /H /Y
copy README.md temp_package\
copy requirements.txt temp_package\
copy run.bat temp_package\
copy setup.bat temp_package\
copy setup.py temp_package\
copy 開啟說明.txt temp_package\

REM 創建壓縮包 (使用WinRAR進行壓縮)
echo 正在創建壓縮包...
IF EXIST "C:\Program Files\WinRAR\WinRAR.exe" (
    "C:\Program Files\WinRAR\WinRAR.exe" a -r -ep1 "加密貨幣匯率計算工具.rar" "temp_package\*"
) ELSE IF EXIST "C:\Program Files (x86)\WinRAR\WinRAR.exe" (
    "C:\Program Files (x86)\WinRAR\WinRAR.exe" a -r -ep1 "加密貨幣匯率計算工具.rar" "temp_package\*"
) ELSE (
    echo WinRAR未找到，使用PowerShell創建7z壓縮包...
    IF EXIST "C:\Program Files\7-Zip\7z.exe" (
        "C:\Program Files\7-Zip\7z.exe" a "加密貨幣匯率計算工具.7z" "temp_package\*"
    ) ELSE (
        echo 7-Zip未找到，使用PowerShell創建ZIP壓縮包...
        powershell -command "Compress-Archive -Path 'temp_package\*' -DestinationPath '加密貨幣匯率計算工具.zip' -Force"
    )
)

REM 清理臨時文件
echo 清理臨時文件...
rmdir /S /Q temp_package

echo 打包完成！
echo 成功創建加密貨幣匯率計算工具壓縮包
pause 