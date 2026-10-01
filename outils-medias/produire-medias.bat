@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo  Medias des escape games (photos Commons + images et videos Agnes)
echo  Ordre de la progression. Relancer ce fichier reprend ce qui manque.
echo.
if not "%~1"=="" (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0produire-medias.ps1" -Jeu "%~1"
  goto fin
)
for %%J in (moyen-age-abbaye chateau-fort station-meteo objets-techniques melanges declaration constitution tour-du-monde mission-geo) do (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0produire-medias.ps1" -Jeu %%J
)
:fin
echo.
echo  Termine. Verifier le rendu : lancer.bat puis verifier.html
pause
