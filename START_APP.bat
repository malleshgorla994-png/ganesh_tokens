@echo off
setlocal
title Token Registration App - Running

echo ============================================================
echo   Token Registration App
echo   Gadi Maisamma Youth, Yerrambelly
echo ============================================================
echo.

REM ---- Check Python ----
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not found. Please run SETUP.bat first.
    pause
    exit /b 1
)

REM ---- Move to the folder where this script lives ----
cd /d "%~dp0"

echo Starting app...
echo.
echo Once the server starts, open your browser and go to:
echo   http://127.0.0.1:5000
echo.
echo Other devices on the same Wi-Fi can use the Network URL
echo shown below.
echo.
echo Press Ctrl+C (or close this window) to stop the app.
echo ============================================================
echo.

python token_webapp.py

pause
endlocal
