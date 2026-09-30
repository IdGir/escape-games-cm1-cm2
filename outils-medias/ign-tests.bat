@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo  Test IGN : cartes d'essai de la France
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0ign-tests.ps1"
echo.
pause
