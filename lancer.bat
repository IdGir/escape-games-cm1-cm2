@echo off
chcp 65001 >nul
title Escape Games pedagogiques - Serveur local
cls
echo.
echo  ============================================================
echo    ESCAPE GAMES PEDAGOGIQUES - Lancement - CM1/CM2
echo      1. Le Secret de la Declaration  (Histoire - Revolution)
echo      2. Le Tour du Monde en 80 minutes  (Geographie - Jules Verne)
echo  ============================================================
echo.
echo  Verification de Python...
echo.

REM Tester python puis py (Windows)
python --version >nul 2>&1
if %errorlevel%==0 (
    set CMD=python
    goto :lancer
)
py --version >nul 2>&1
if %errorlevel%==0 (
    set CMD=py
    goto :lancer
)

echo  [ERREUR] Python n'est pas installe ou pas dans le PATH.
echo.
echo  Solutions :
echo    1. Installer Python : https://www.python.org/downloads/
echo    2. OU ouvrir directement index.html en double-clic (mode autonome)
echo       ATTENTION : les decors VIDEO exigent le serveur (double-clic = decors dessines)
echo.
pause
exit /b 1

:lancer
echo  Python detecte :
%CMD% --version
echo.
echo  Demarrage du serveur sur le port 8000...
echo.
echo  ^>^> POSTES ELEVES :
echo      Histoire     : http://127.0.0.1:8000/
echo      Geographie   : http://127.0.0.1:8000/tour-du-monde/
echo.
echo  ^>^> TABLEAUX DE BORD ENSEIGNANT :
echo      Histoire     : http://127.0.0.1:8000/prof.html
echo      Geographie   : http://127.0.0.1:8000/tour-du-monde/prof.html
echo.
echo  Fermez cette fenetre pour arreter le serveur.
echo.

REM Ouvrir le navigateur apres 2 secondes
start "" timeout /t 2 /nobreak >nul ^& start "" http://127.0.0.1:8000/

%CMD% serveur.py 8000
pause
