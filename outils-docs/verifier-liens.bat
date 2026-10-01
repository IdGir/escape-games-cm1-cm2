@echo off
chcp 65001 >nul
cd /d "%~dp0.."
echo Verification des liens externes cites dans les jeux (quelques minutes)...
python outils-docs\verifier-liens.py
echo.
echo Rapport : outils-docs\rapport-liens.md
pause
