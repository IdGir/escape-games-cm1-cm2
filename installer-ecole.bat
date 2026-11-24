@echo off
chcp 65001 >nul
title EG - installation du PC de l'ecole (une seule fois)
cd /d "%~dp0"
cls
echo.
echo  ============================================================
echo    ESCAPE GAMES - PC DE L'ECOLE : DEMARRAGE AUTOMATIQUE
echo  ============================================================
echo.
echo  A chaque ouverture de session Windows, ce PC va :
echo    1. recuperer la derniere version des jeux (git, ou archive GitHub) ;
echo    2. lancer le serveur de la classe (fenetre reduite en bas de l'ecran).
echo.
echo  Dossier des jeux : %~dp0
echo.
set "DEMARRER=%~dp0demarrer-ecole.bat"
if not exist "%DEMARRER%" (
    echo  [ERREUR] demarrer-ecole.bat est introuvable a cote de ce fichier.
    pause
    exit /b 1
)

REM Repere de ce PC pour le tableau de bord : "PC de l'ecole" (dans le profil Windows, jamais synchronise)
if not exist "%APPDATA%\EscapeGames" mkdir "%APPDATA%\EscapeGames"
> "%APPDATA%\EscapeGames\poste-ecole.txt" echo PC de l'ecole : demarrage automatique installe par installer-ecole.bat

REM 1er essai : une tache Windows "a l'ouverture de session" (demande parfois les droits administrateur)
schtasks /Create /F /SC ONLOGON /TN "EscapeGames-Ecole" /TR "\"%DEMARRER%\"" /RU "%USERNAME%" /IT >nul 2>&1
if %errorlevel%==0 (
    echo  [OK] Tache Windows "EscapeGames-Ecole" creee : elle se lance a chaque ouverture de session.
    goto :essai
)

REM 2e essai, sans droits administrateur : un lanceur dans le dossier Demarrage de l'utilisateur
set "STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
if not exist "%STARTUP%" mkdir "%STARTUP%"
> "%STARTUP%\EscapeGames-Ecole.cmd" echo @start "EG" /min "%DEMARRER%"
if exist "%STARTUP%\EscapeGames-Ecole.cmd" (
    echo  [OK] Lanceur place dans le dossier Demarrage de Windows : il se lance a chaque ouverture de session.
    goto :essai
)
echo  [ERREUR] Impossible de creer le demarrage automatique.
echo  Solution : clic droit sur installer-ecole.bat, "Executer en tant qu'administrateur".
pause
exit /b 1

:essai
echo.
echo  Pour l'enlever plus tard : double-clic sur desinstaller-ecole.bat
echo.
choice /C ON /M "  Lancer la mise a jour et le serveur maintenant (O = oui, N = non) "
if errorlevel 2 goto :fin
start "EG" /min "%DEMARRER%"
echo.
echo  Serveur en cours de lancement (fenetre reduite). Espace enseignant :
echo     http://127.0.0.1:8000/enseignant.html
:fin
echo.
pause
