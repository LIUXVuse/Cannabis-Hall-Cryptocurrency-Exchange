@echo off
chcp 65001 > nul
echo Starting cryptocurrency exchange rate calculator...

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

REM Check for virtual environment
if not exist venv (
    echo Warning: Virtual environment not found
    echo Please run setup.bat first to create the virtual environment
    pause
    exit /b 1
)

REM Try to run the application
echo Running application...
cd /d %~dp0
call venv\Scripts\activate && python -c "import sys; sys.path.insert(0, '.'); from src.main import main; main()"
if errorlevel 1 (
    echo ============================================
    echo             Runtime Error
    echo ============================================
    echo.
    echo An error occurred while running the application.
    echo Check the error message above for details.
    echo.
    echo If dependency issues persist, try:
    echo 1. Deleting the venv directory
    echo 2. Running setup.bat again
    echo 3. Running run.bat
    echo ============================================
    pause
    exit /b 1
)

pause
