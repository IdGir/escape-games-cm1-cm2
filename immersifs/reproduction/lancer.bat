@echo off
REM Ouvre ce jeu. Passe par lancer.bat a la racine : il ferme l'ancien serveur du port 8000,
REM affiche la version et l'adresse des eleves. Fichier genere par migrer-jeu.py.
setlocal
chcp 65001 >nul
cd /d "%~dp0..\..\"
if not exist "lancer.bat" goto :simple
if not exist "outils-ecole\ecole.py" goto :simple
call lancer.bat immersifs/reproduction/
exit /b

:simple
title Serveur local - reproduction
set "CMD="
python --version >nul 2>&1 && set "CMD=python"
if not defined CMD py -3 --version >nul 2>&1 && set "CMD=py -3"
if not defined CMD goto :sanspython
echo  Jeu : http://127.0.0.1:8000/immersifs/reproduction/
echo  Fermez cette fenetre pour arreter le serveur.
start "" /min cmd /c "ping -n 3 127.0.0.1 >nul & start http://127.0.0.1:8000/immersifs/reproduction/"
if exist "serveur.py" (%CMD% serveur.py 8000) else (%CMD% -m http.server 8000)
pause
exit /b 0

:sanspython
echo  [ERREUR] Python n'est pas installe ou pas dans le PATH.
pause
exit /b 1
