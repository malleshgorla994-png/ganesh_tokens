@echo off
setlocal
title Token App - Setup

echo ============================================================
echo   Token Registration App - Setup
echo   Gadi Maisamma Youth, Yerrambelly
echo ============================================================
echo.

REM ---- Check Python ----
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is NOT installed or not in PATH.
    echo.
    echo Please install Python from:
    echo   https://www.python.org/downloads/
    echo.
    echo IMPORTANT: During install, check the box
    echo   "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo [OK] Python found:
python --version
echo.

REM ---- Install required packages ----
echo Installing required packages (flask, pillow)...
echo.
pip install flask pillow

if errorlevel 1 (
    echo.
    echo [ERROR] pip install failed. Check your internet connection.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   Setup complete!
echo.
echo   To START the app, double-click: START_APP.bat
echo ============================================================
echo.
pause
endlocal
