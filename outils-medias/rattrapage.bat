@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo  Rattrapage : abbaye, chateau fort, station meteo
echo.
for %%J in (moyen-age-abbaye chateau-fort station-meteo) do (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0produire-medias.ps1" -Jeu %%J
)
echo.
pause
