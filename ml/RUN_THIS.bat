@echo off
taskkill /F /IM python.exe >nul 2>&1
timeout /t 3 >nul
cls
cd /d "%~dp0"
python verify_fix.py
pause
