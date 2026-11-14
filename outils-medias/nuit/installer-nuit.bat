@echo off
chcp 65001 >nul
title Installer la fabrique de nuit des medias
cd /d "%~dp0\..\.."
echo.
echo  ============================================================
echo    FABRIQUE DE NUIT DES MEDIAS - installation (une seule fois)
echo  ============================================================
echo.
python --version >nul 2>&1 && (set PY=python) || (set PY=py)
%PY% --version >nul 2>&1 || (echo  [ERREUR] Python est introuvable. Installez-le depuis python.org en cochant "Add Python to PATH". & pause & exit /b 1)
echo  1/3  Outils Python (voix Edge, images)...
%PY% -m pip install --quiet --upgrade edge-tts pillow
echo  2/3  Tache planifiee chaque soir a 23 h 00 (reveille l'ordinateur, rattrape si eteint)...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$a = New-ScheduledTaskAction -Execute '%~dp0nuit-medias.bat';" ^
  "$t = New-ScheduledTaskTrigger -Daily -At 23:00;" ^
  "$s = New-ScheduledTaskSettingsSet -WakeToRun -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 5);" ^
  "Register-ScheduledTask -TaskName 'EscapeGames-Medias-Nuit' -Action $a -Trigger $t -Settings $s -Description 'Escape games : voix, images et videos des jeux immersifs (une nuit, un jeu)' -Force | Out-Null"
if errorlevel 1 (echo  [ERREUR] La tache n'a pas pu etre creee. Faites clic droit sur ce fichier, "Executer en tant qu'administrateur". & pause & exit /b 1)
echo  3/3  Essai a blanc (rien n'est appele)...
%PY% outils-medias\nuit\nuit-medias.py --essai --max-images 2 --max-videos 1
echo.
echo  C'est installe. Chaque soir a 23 h, l'ordinateur fabrique les medias du jeu en tete de file.
echo  Laissez-le branche, en veille plutot qu'eteint. Compte rendu : outils-medias\nuit\journal.txt
echo  Pour arreter : desinstaller-nuit.bat
echo.
pause
