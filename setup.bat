@echo off
chcp 65001 > nul
echo Starting cryptocurrency exchange rate calculator setup...

REM Use official Python path
set PYTHON_PATH=C:\Users\PONY\AppData\Local\Programs\Python\Python313\python.exe

REM Check if Python exists
if not exist "%PYTHON_PATH%" (
    echo Error: Official Python installation not found
    echo Please verify Python is installed at %PYTHON_PATH%
    echo If installed in a different location, edit this batch file to modify the PYTHON_PATH variable
    pause
    exit /b 1
)

REM Display Python version info
echo Using Python path: %PYTHON_PATH%
"%PYTHON_PATH%" --version
echo.

REM Create virtual environment
echo Creating Python virtual environment...
"%PYTHON_PATH%" -m venv venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment and install dependencies
echo Installing dependencies...
call venv\Scripts\activate
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo Setup complete!
echo You can now run run.bat to start the application
pause
