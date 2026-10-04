@echo off
chcp 65001 >nul
title Le Journal du Nautilus - serveur local
cd /d "%~dp0.."
cls
echo.
echo  ============================================================
echo    VINGT MILLE LIEUES SOUS LES MERS - Le Journal du Nautilus
echo  ============================================================
echo.
set CMD=
python --version >nul 2>&1 && set CMD=python
if not defined CMD py --version >nul 2>&1 && set CMD=py
if not defined CMD goto :sanspython
echo  Python detecte :
%CMD% --version
echo.
echo  Jeu : http://127.0.0.1:8000/vingt-mille-lieues/
echo  Tableau de bord enseignant : http://127.0.0.1:8000/vingt-mille-lieues/prof.html
echo.
echo  Fermez cette fenetre pour arreter le serveur.
echo.
start "" cmd /c "timeout /t 2 /nobreak >nul & start http://127.0.0.1:8000/vingt-mille-lieues/"
if exist serveur.py (%CMD% serveur.py 8000) else (%CMD% -m http.server 8000)
pause
exit /b 0

:sanspython
echo  [ERREUR] Python n'est pas installe ou pas dans le PATH.
echo  Installez-le : https://www.python.org/downloads/ (cocher "Add Python to PATH").
pause
exit /b 1
