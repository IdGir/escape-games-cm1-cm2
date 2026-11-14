@echo off
chcp 65001 >nul
powershell -NoProfile -Command "Unregister-ScheduledTask -TaskName 'EscapeGames-Medias-Nuit' -Confirm:$false" && echo  Fabrique de nuit arretee. || echo  Aucune tache a supprimer.
pause
