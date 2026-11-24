@echo off
REM ================================================================
REM  PC PRINCIPAL : met a jour la copie Nextcloud des jeux (double-clic).
REM  Copie la version COMMITEE de ce depot ; ne touche jamais aux
REM  resultats, sauvegardes, reglages ni journaux de la classe ; les
REM  fichiers devenus inutiles vont dans _a-supprimer, jamais effaces.
REM  Dossier de la copie : 1re ligne de outils-ecole\dossier-nextcloud.txt,
REM  sinon Nextcloud\Escape games\escape-games-cm1-cm2-escape-games
REM  dans le dossier de l'utilisateur.
REM ================================================================
setlocal
chcp 65001 >nul
title EG - mise a jour de la copie Nextcloud
cd /d "%~dp0"
echo.
echo  ============================================================
echo    ESCAPE GAMES - MISE A JOUR DE LA COPIE NEXTCLOUD
echo  ============================================================
echo.
call :trouver_python
if not defined PY goto :sans_python
echo  Essai d'abord : rien n'est encore modifie.
echo.
%PY% outils-ecole\ecole.py nextcloud --essai
if errorlevel 1 goto :erreur
echo.
choice /C ON /M "  Faire la copie maintenant (O = oui, N = non) "
if errorlevel 2 goto :fin
echo.
%PY% outils-ecole\ecole.py nextcloud
if errorlevel 1 goto :erreur
:fin
echo.
pause
exit /b 0

:erreur
echo.
echo  [!] Copie non faite : lisez le message ci-dessus.
pause
exit /b 1

:sans_python
echo  [ERREUR] Python est introuvable sur ce PC.
pause
exit /b 1

:trouver_python
set "PY="
python --version >nul 2>&1
if errorlevel 1 goto :essai_py
set "PY=python"
goto :eof
:essai_py
py -3 --version >nul 2>&1
if errorlevel 1 goto :eof
set "PY=py -3"
goto :eof
