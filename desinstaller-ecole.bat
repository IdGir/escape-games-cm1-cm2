@echo off
chcp 65001 >nul
title Escape games - retirer le demarrage automatique
cd /d "%~dp0"
echo.
schtasks /Delete /F /TN "EscapeGames-Ecole" >nul 2>&1
if %errorlevel%==0 (echo  [OK] Tache Windows "EscapeGames-Ecole" supprimee.) else (echo  [--] Pas de tache Windows "EscapeGames-Ecole".)
set "LANCEUR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\EscapeGames-Ecole.cmd"
if exist "%LANCEUR%" (del "%LANCEUR%" & echo  [OK] Lanceur du dossier Demarrage supprime.) else (echo  [--] Pas de lanceur dans le dossier Demarrage.)
echo.
echo  Le PC ne lancera plus le serveur tout seul. Les jeux et les resultats de la classe sont gardes.
echo  Pour lancer le serveur a la main : double-clic sur lancer.bat
echo.
pause
