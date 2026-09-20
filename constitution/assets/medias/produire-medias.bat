@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo  Production des medias du jeu Le Sceau de la Republique
echo  (photos des lieux + images et videos Agnes)
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0produire-medias.ps1"
echo.
pause
