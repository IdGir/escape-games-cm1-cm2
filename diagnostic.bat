@echo off
REM ================================================================
REM  ESCAPE GAMES - DIAGNOSTIC (double-clic). Ecrit diagnostic.txt :
REM  versions, port 8000, dossier immersifs, git, python, journal.
REM  Aucun prenom d'eleve dedans. Fichier a envoyer en cas de probleme.
REM ================================================================
setlocal
chcp 65001 >nul
title EG - diagnostic
cd /d "%~dp0"
set "SORTIE=%~dp0diagnostic.txt"
echo.
echo  Diagnostic en cours, 30 secondes au plus...
echo.
call :trouver_python
if not defined PY goto :sans_python
if not exist "outils-ecole\ecole.py" goto :sans_python
%PY% outils-ecole\ecole.py diagnostic --port 8000
if errorlevel 1 goto :sans_python
goto :windows

:sans_python
> "%SORTIE%" echo DIAGNOSTIC ESCAPE GAMES, partie Windows seulement - %date% %time%
>> "%SORTIE%" echo Dossier des jeux : %CD%
>> "%SORTIE%" echo Python : introuvable, ou outils-ecole\ecole.py absent.

:windows
>> "%SORTIE%" echo.
>> "%SORTIE%" echo == Informations Windows ==
ver >> "%SORTIE%" 2>&1
>> "%SORTIE%" echo -- Programmes trouves :
where python >> "%SORTIE%" 2>&1
where py >> "%SORTIE%" 2>&1
where git >> "%SORTIE%" 2>&1
>> "%SORTIE%" echo -- Port 8000 :
netstat -ano | findstr /C:":8000 " >> "%SORTIE%" 2>&1
>> "%SORTIE%" echo -- Demarrage automatique :
schtasks /Query /TN "EscapeGames-Ecole" >> "%SORTIE%" 2>&1
if exist "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\EscapeGames-Ecole.cmd" (>> "%SORTIE%" echo Lanceur du dossier Demarrage : present) else (>> "%SORTIE%" echo Lanceur du dossier Demarrage : absent)
>> "%SORTIE%" echo -- Dossier immersifs :
if exist "immersifs\" (dir /b "immersifs" >> "%SORTIE%" 2>&1) else (>> "%SORTIE%" echo ABSENT : copie ancienne)
>> "%SORTIE%" echo -- version.json :
if exist "version.json" (type "version.json" >> "%SORTIE%" 2>&1) else (>> "%SORTIE%" echo ABSENT)
>> "%SORTIE%" echo.
>> "%SORTIE%" echo Fin du diagnostic.

echo.
echo  Termine. Le fichier diagnostic.txt va s'ouvrir dans le Bloc-notes.
echo  Envoyez-le tel quel, par mail ou dans la conversation avec Claude.
echo  Il est ici : %SORTIE%
echo.
start "" notepad "%SORTIE%"
pause
exit /b 0

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
