@echo off
chcp 65001 >nul
title Resultats de la classe
cd /d "%~dp0"
REM Si le serveur tourne deja : on ouvre seulement la page des resultats.
powershell -NoProfile -Command "try { Invoke-WebRequest -UseBasicParsing -TimeoutSec 2 http://127.0.0.1:8000/api/info | Out-Null; exit 0 } catch { exit 1 }" >nul 2>&1
if %errorlevel%==0 (
    start "" http://127.0.0.1:8000/resultats.html
    exit /b 0
)
echo.
echo  Le serveur n'est pas lance : demarrage en cours.
echo  La page des resultats s'ouvrira toute seule.
echo.
call lancer.bat
