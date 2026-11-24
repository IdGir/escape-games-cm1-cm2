@echo off
REM ================================================================
REM  ESCAPE GAMES - lancer le serveur de la classe (double-clic).
REM   1. ferme l'ancien serveur des jeux (port 8000) et ses fenetres ;
REM   2. controle le dossier, affiche la version et l'adresse des eleves ;
REM   3. ouvre l'espace enseignant dans le navigateur.
REM  Autre page : lancer.bat resultats.html
REM  Aide : diagnostic.bat (ecrit diagnostic.txt, a envoyer).
REM ================================================================
setlocal
chcp 65001 >nul
title EG - demarrage
cd /d "%~dp0"
set "PORT=8000"
set "PAGE=enseignant.html"
if not "%~1"=="" set "PAGE=%~1"
set "LOG=%~dp0journal-ecole.txt"
cls
echo.
echo  ============================================================
echo    ESCAPE GAMES PEDAGOGIQUES - CM1/CM2 - serveur de la classe
echo  ============================================================
echo.
call :trouver_python
if not defined PY goto :sans_python
if not exist "outils-ecole\ecole.py" goto :ancienne_copie

echo  1/3  Fermeture de l'ancien serveur s'il tourne encore...
%PY% outils-ecole\ecole.py liberer-port --port %PORT%
if errorlevel 2 goto :port_pris
taskkill /F /FI "IMAGENAME eq cmd.exe" /FI "WINDOWTITLE eq Escape games*" >nul 2>&1
title Escape games - serveur de la classe
echo.
echo  2/3  Controles du dossier des jeux...
%PY% outils-ecole\ecole.py verifier --port %PORT%
if errorlevel 1 goto :bloque
%PY% outils-ecole\ecole.py infos --port %PORT%
echo.
echo  3/3  L'espace enseignant va s'ouvrir dans le navigateur.
echo       Fermez cette fenetre pour arreter le serveur.
echo.
>> "%LOG%" echo ==== %date% %time% : lancer.bat, port %PORT%
start "" /b %PY% outils-ecole\ecole.py ouvrir --port %PORT% %PAGE%
%PY% serveur.py %PORT%
if errorlevel 1 goto :serveur_erreur
exit /b 0

:ancienne_copie
echo  [!] Copie incomplete : outils-ecole\ecole.py manque. Lancement simple du serveur.
title Escape games - serveur de la classe
start "" http://127.0.0.1:%PORT%/%PAGE%
%PY% serveur.py %PORT%
pause
exit /b 1

:serveur_erreur
echo.
echo  [!] Le serveur s'est arrete sur une erreur : lisez les lignes ci-dessus.
echo      Pour obtenir de l'aide : double-clic sur diagnostic.bat, puis envoyez diagnostic.txt.
>> "%LOG%" echo [!] lancer.bat : serveur arrete sur une erreur.
pause
exit /b 1

:port_pris
echo.
echo  [!] Le port %PORT% est pris par un autre programme : le serveur ne peut pas demarrer.
echo      Fermez ce programme ou redemarrez le PC, puis relancez lancer.bat.
>> "%LOG%" echo [!] lancer.bat : port %PORT% pris par un autre programme.
pause
exit /b 1

:bloque
echo.
echo  [!] Probleme bloquant ci-dessus : le serveur n'est pas lance.
echo      Pour obtenir de l'aide : double-clic sur diagnostic.bat, puis envoyez diagnostic.txt.
pause
exit /b 1

:sans_python
echo  [ERREUR] Python n'est pas installe ou pas dans le PATH.
echo.
echo  Solutions :
echo    1. Installer Python : https://www.python.org/downloads/
echo       cocher "Add Python to PATH" pendant l'installation, puis relancer lancer.bat.
echo    2. OU jouer en ligne : https://idgir.github.io/escape-games-cm1-cm2/
echo.
pause
exit /b 1

:trouver_python
set "PY="
python --version >nul 2>&1
if errorlevel 1 goto :essai_py
set "PY=python"
goto :eof
:essai_py
py -3 --version >nul 2>&1
if errorlevel 1 goto :eof
set "PY=py -3"
goto :eof
