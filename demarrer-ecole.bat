@echo off
chcp 65001 >nul
REM ================================================================
REM  PC DE L'ECOLE : mise a jour puis serveur (lance a l'ouverture de
REM  session par installer-ecole.bat ; double-clic possible aussi).
REM  Journal : journal-ecole.txt (jamais publie).
REM ================================================================
REM La mise a jour peut remplacer ce fichier : on s'execute depuis une copie.
if /I not "%~1"=="--copie" (
    copy /y "%~f0" "%TEMP%\escape-games-demarrer.bat" >nul
    "%TEMP%\escape-games-demarrer.bat" --copie "%~dp0"
    exit /b
)
cd /d "%~2"
title Escape games - serveur de la classe
set "LOG=%CD%\journal-ecole.txt"
echo ==== %date% %time% : ouverture de session >> "%LOG%"

REM ---- Serveur deja lance ? (port 8000 occupe) ----
netstat -ano | findstr /R /C:":8000 .*LISTENING" >nul 2>&1
if %errorlevel%==0 (
    echo Serveur deja lance : rien a faire. >> "%LOG%"
    exit /b 0
)

REM ---- 1. Mise a jour ----
echo  Mise a jour des jeux...
where git >nul 2>&1
if errorlevel 1 goto :archive
if not exist ".git" goto :archive
git -c gc.auto=0 -c maintenance.auto=false fetch origin escape-games >> "%LOG%" 2>&1
if errorlevel 1 (
    echo Mise a jour git impossible ^(pas d'internet ?^) : version actuelle gardee. >> "%LOG%"
    goto :python
)
git -c gc.auto=0 -c maintenance.auto=false merge --ff-only origin/escape-games >> "%LOG%" 2>&1
if errorlevel 1 echo [!] Mise a jour refusee ^(modifications locales sur ce PC ?^) : version actuelle gardee. >> "%LOG%"
goto :python

:archive
powershell -NoProfile -ExecutionPolicy Bypass -File "%CD%\outils-ecole\maj-ecole.ps1" >> "%LOG%" 2>&1

REM ---- 2. Serveur ----
:python
python --version >nul 2>&1
if %errorlevel%==0 (set "PY=python" & goto :lancer)
py --version >nul 2>&1
if %errorlevel%==0 (set "PY=py" & goto :lancer)
echo [ERREUR] Python introuvable : installer Python ^(cocher "Add Python to PATH"^). >> "%LOG%"
echo.
echo  [ERREUR] Python n'est pas installe. Installez-le : https://www.python.org/downloads/
echo  (cocher "Add Python to PATH"), puis fermez et rouvrez la session.
pause
exit /b 1

:lancer
echo Serveur lance. >> "%LOG%"
%PY% serveur.py 8000
