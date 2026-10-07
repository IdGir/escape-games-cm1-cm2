@echo off
chcp 65001 >nul
title Serveur local - objets-techniques
cd /d "%~dp0..\..\"
cls
set CMD=
python --version >nul 2>&1 && set CMD=python
if not defined CMD py --version >nul 2>&1 && set CMD=py
if not defined CMD goto :sanspython
echo  Jeu : http://127.0.0.1:8000/immersifs/objets-techniques/
echo  Fermez cette fenetre pour arreter le serveur.
start "" cmd /c "timeout /t 2 /nobreak >nul & start http://127.0.0.1:8000/immersifs/objets-techniques/"
if exist serveur.py (%CMD% serveur.py 8000) else (%CMD% -m http.server 8000)
pause
exit /b 0

:sanspython
echo  [ERREUR] Python n'est pas installe ou pas dans le PATH.
pause
exit /b 1
