@echo off
chcp 65001 >nul
title Creation du fichier EXE
cd /d "%~dp0"

echo.
echo   ===========================================
echo     CREATION DU FICHIER .EXE
echo   ===========================================
echo.
echo   Duree : 3 a 6 minutes. Ne ferme pas cette fenetre.
echo.

python --version >nul 2>&1
if errorlevel 1 (
  echo   [!] Python n est pas installe.
  echo       https://www.python.org/downloads/
  echo       Coche "Add Python to PATH" pendant l installation.
  pause
  exit /b 1
)

echo   [1/3] Installation des outils...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install flask pywebview qrcode pyinstaller
if errorlevel 1 (
  echo   [!] Echec de l installation.
  pause
  exit /b 1
)

echo.
echo   [2/3] Construction de l application...
python -m PyInstaller --noconfirm --clean --onefile --windowed ^
  --name "CorrecteurPedagogique" ^
  --add-data "web;web" ^
  --add-data "data_lecons_manuel.json;." ^
  --add-data "data_lecons_manuel.css;." ^
  --add-data "data_dictionnaire.txt;." ^
  --hidden-import "webview.platforms.edgechromium" ^
  --hidden-import "qrcode.image.svg" ^
  --collect-submodules "qrcode" ^
  --hidden-import "webview.platforms.winforms" ^
  --collect-all "webview" ^
  app.py

if errorlevel 1 (
  echo.
  echo   [!] La construction a echoue. Recopie le message ci-dessus.
  pause
  exit /b 1
)

echo.
echo   [3/3] TERMINE !
echo.
echo   Ton fichier se trouve ici :
echo       %~dp0dist\CorrecteurPedagogique.exe
echo.
echo   Copie-le sur une cle USB ou sur les ordinateurs de la classe :
echo   il fonctionne seul, sans installer Python.
echo.
pause
