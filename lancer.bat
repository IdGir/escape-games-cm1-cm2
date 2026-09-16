@echo off
chcp 65001 >nul
title Correcteur Pedagogique
cd /d "%~dp0"

echo.
echo   ===========================================
echo     CORRECTEUR PEDAGOGIQUE
echo   ===========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
  echo   [!] Python n est pas installe sur cet ordinateur.
  echo.
  echo   Que faire :
  echo     1. Va sur https://www.python.org/downloads/
  echo     2. Clique sur le gros bouton jaune "Download Python"
  echo     3. Lance le fichier telecharge
  echo     4. IMPORTANT : coche la case "Add Python to PATH" en bas
  echo     5. Clique sur "Install Now"
  echo     6. Redemarre ce fichier lancer.bat
  echo.
  pause
  exit /b 1
)

echo   [1/2] Verification des composants...
python -m pip install --quiet flask pywebview qrcode
if errorlevel 1 (
  echo   [!] Impossible d installer les composants. Verifie ta connexion,
  echo       puis relance ce fichier. Une fois installes, ils ne seront
  echo       plus jamais retelecharges.
  pause
  exit /b 1
)

echo   [2/2] Lancement...
echo   Laisse cette fenetre noire ouverte pendant l utilisation.
echo.
python app.py

if errorlevel 1 (
  echo.
  echo   [!] L application s est arretee sur une erreur.
  echo   Recopie le message ci-dessus pour le signaler.
  pause
)
