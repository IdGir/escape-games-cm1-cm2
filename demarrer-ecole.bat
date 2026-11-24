@echo off
REM ================================================================
REM  PC DE L'ECOLE : mise a jour puis serveur (lance a l'ouverture de
REM  session par installer-ecole.bat ; double-clic possible aussi).
REM   1. met les jeux a jour : git, sinon archive GitHub ; rien a faire
REM      pour une copie Nextcloud (copie-nextcloud.txt) ;
REM   2. ferme l'ancien serveur du port 8000 et ses fenetres ;
REM   3. controle les droits d'ecriture ; 4. affiche version et adresse.
REM  Journal : journal-ecole.txt (jamais publie). Aide : diagnostic.bat
REM ================================================================
setlocal
chcp 65001 >nul
REM La mise a jour peut remplacer ce fichier : on s'execute depuis une copie.
if /I "%~1"=="--copie" goto :depuis_copie
copy /y "%~f0" "%TEMP%\escape-games-demarrer.bat" >nul 2>&1
if errorlevel 1 goto :sur_place
"%TEMP%\escape-games-demarrer.bat" --copie "%~dp0"
exit /b

:sur_place
cd /d "%~dp0"
goto :suite
:depuis_copie
cd /d "%~2"
:suite
title EG - demarrage
set "PORT=8000"
set "LOG=%CD%\journal-ecole.txt"
>> "%LOG%" echo.
>> "%LOG%" echo ==== %date% %time% : ouverture de session, dossier %CD%
echo.
echo  ============================================================
echo    ESCAPE GAMES - PC DE L'ECOLE : mise a jour puis serveur
echo  ============================================================
echo.

REM ---- 1. Mise a jour ----
echo  1/4  Mise a jour des jeux...
if exist "copie-nextcloud.txt" goto :maj_nextcloud
where git >nul 2>&1
if errorlevel 1 goto :maj_archive
if not exist ".git" goto :maj_archive
git -c gc.auto=0 -c maintenance.auto=false fetch origin escape-games >> "%LOG%" 2>&1
if errorlevel 1 goto :maj_hors_ligne
git -c gc.auto=0 -c maintenance.auto=false merge --ff-only origin/escape-games >> "%LOG%" 2>&1
if errorlevel 1 goto :maj_refusee
echo       Jeux a jour.
>> "%LOG%" echo Mise a jour git : OK
goto :python

:maj_hors_ligne
echo       Pas d'internet : la version deja installee est gardee.
>> "%LOG%" echo Mise a jour git impossible, pas d'internet ? Version actuelle gardee.
goto :python

:maj_refusee
echo  [!] Mise a jour refusee : des fichiers des jeux ont ete modifies sur ce PC.
echo      La version deja installee est gardee. Aide : diagnostic.bat
>> "%LOG%" echo [!] Mise a jour refusee, modifications locales sur ce PC ? Version actuelle gardee.
goto :python

:maj_nextcloud
echo       Copie Nextcloud : la mise a jour arrive par Nextcloud, depuis le PC principal.
>> "%LOG%" echo Copie Nextcloud : mise a jour faite par Nextcloud.
goto :python

:maj_archive
powershell -NoProfile -ExecutionPolicy Bypass -File "%CD%\outils-ecole\maj-ecole.ps1" >> "%LOG%" 2>&1
if errorlevel 1 echo  [!] Mise a jour par archive incomplete : voir journal-ecole.txt.

REM ---- 2. Python, ancien serveur ----
:python
call :trouver_python
if not defined PY goto :sans_python
if not exist "outils-ecole\ecole.py" goto :ancienne_copie
echo  2/4  Fermeture de l'ancien serveur s'il tourne encore...
%PY% outils-ecole\ecole.py liberer-port --port %PORT%
if errorlevel 2 goto :port_pris
taskkill /F /FI "IMAGENAME eq cmd.exe" /FI "WINDOWTITLE eq Escape games*" >nul 2>&1
title Escape games - serveur de la classe

REM ---- 3. Controles ----
echo  3/4  Controles des droits d'ecriture et des dossiers...
%PY% outils-ecole\ecole.py verifier --port %PORT%
if errorlevel 1 goto :bloque

REM ---- 4. Serveur ----
echo  4/4  Lancement du serveur.
echo.
%PY% outils-ecole\ecole.py infos --port %PORT%
%PY% outils-ecole\ecole.py version >> "%LOG%" 2>&1
>> "%LOG%" echo Serveur lance.
echo.
%PY% serveur.py %PORT%
if errorlevel 1 goto :serveur_erreur
>> "%LOG%" echo Serveur arrete normalement.
exit /b 0

:ancienne_copie
>> "%LOG%" echo [!] outils-ecole\ecole.py absent : copie ancienne, lancement simple.
title Escape games - serveur de la classe
%PY% serveur.py %PORT%
exit /b 0

:serveur_erreur
echo.
echo  [!] Le serveur s'est arrete sur une erreur : lisez les lignes ci-dessus.
echo      Aide : double-clic sur diagnostic.bat, puis envoyez diagnostic.txt.
>> "%LOG%" echo [!] Serveur arrete sur une erreur.
pause
exit /b 1

:port_pris
echo.
echo  [!] Le port %PORT% est pris par un autre programme : le serveur ne peut pas demarrer.
echo      Fermez ce programme ou redemarrez le PC.
>> "%LOG%" echo [!] Port %PORT% pris par un autre programme.
pause
exit /b 1

:bloque
>> "%LOG%" echo [!] Controle bloquant : serveur non lance.
echo.
echo  [!] Probleme bloquant ci-dessus : le serveur n'est pas lance.
echo      Aide : double-clic sur diagnostic.bat, puis envoyez diagnostic.txt.
pause
exit /b 1

:sans_python
>> "%LOG%" echo [ERREUR] Python introuvable.
echo.
echo  [ERREUR] Python n'est pas installe. Installez-le : https://www.python.org/downloads/
echo  cocher "Add Python to PATH", puis fermez et rouvrez la session Windows.
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
