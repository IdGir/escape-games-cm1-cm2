@echo off
chcp 65001 >nul
REM Fabrique de nuit des medias (lancee par le Planificateur de taches). Ne rien changer ici.
cd /d "%~dp0\..\.."
set PY=python
python --version >nul 2>&1 || set PY=py
%PY% outils-medias\nuit\nuit-medias.py %* >> outils-medias\nuit\sortie-console.txt 2>&1
