@echo off
chcp 65001 >nul
title Escape Games pedagogiques - Serveur local
cd /d "%~dp0"
cls
echo.
echo  ============================================================
echo    ESCAPE GAMES PEDAGOGIQUES - CM1/CM2 - Serveur local
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
echo       (cocher "Add Python to PATH" pendant l'installation)
echo    2. OU jouer en ligne : https://idgir.github.io/escape-games-cm1-cm2/
echo.
pause
exit /b 1

:lancer
echo  Python detecte :
%CMD% --version
echo.
echo  ^>^> RESULTATS DES ELEVES : enregistres AUTOMATIQUEMENT
echo      (fichiers resultats-classe.jsonl et resultats-classe.csv pour Excel,
echo       copie de securite chaque jour dans sauvegardes-resultats)
echo      Les voir : http://127.0.0.1:8000/resultats.html  (s'ouvre tout seul)
echo.
echo  ^>^> ELEVES : ils doivent jouer depuis l'adresse "http://192.168...."
echo      affichee plus bas (ADRESSES A DONNER AUX ELEVES).
echo      Depuis GitHub, le resultat reste dans le Chromebook.
echo.
echo  ^>^> ESPACE ENSEIGNANT (tout au meme endroit) :
echo      http://127.0.0.1:8000/enseignant.html
echo.
echo  ^>^> ACCUEIL DES JEUX : http://127.0.0.1:8000/
echo  ^>^> VERIFICATION (medias, acces direct aux enigmes) :
echo      http://127.0.0.1:8000/verifier.html
echo.
echo  Fermez cette fenetre pour arreter le serveur.
echo.

REM Ouvrir la page des resultats apres 2 secondes
start "" timeout /t 2 /nobreak >nul ^& start "" http://127.0.0.1:8000/resultats.html

%CMD% serveur.py 8000
pause
