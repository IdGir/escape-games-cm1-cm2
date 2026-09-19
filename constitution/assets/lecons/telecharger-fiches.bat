@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
echo.
echo ============================================================
echo  Telechargement des 16 fiches officielles
echo  Source : Conseil constitutionnel / Decouvrons notre Constitution
echo  Les fichiers deja presents ne sont pas retelecharges.
echo ============================================================
echo.
set OK=0
set KO=0
set SAUTES=0

echo [1/16] La Constitution francaise
if exist "c3-la-constitution-francaise.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2025-10/C3_La_Constitution_francaise_2025.pdf' -OutFile 'c3-la-constitution-francaise.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [2/16] Qu'est-ce qu'une Constitution ? (dossier)
if exist "c3-theme1-qu-est-ce-qu-une-constitution.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-02/Cycle%%203%%20-%%20Th%%C3%%A8me%%201.pdf' -OutFile 'c3-theme1-qu-est-ce-qu-une-constitution.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [3/16] Jeu : Sais-tu ce qu'est une Constitution ?
if exist "jeu-sais-tu-ce-qu-est-une-constitution.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/Sais-tu%%20ce%%20qu%%27est%%20une%%20Constitution%%20%%288-10%%20ans%%29.pdf' -OutFile 'jeu-sais-tu-ce-qu-est-une-constitution.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [4/16] Les textes de notre Constitution
if exist "c3-les-textes-de-notre-constitution.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-07/C3_textes_Constitution.pdf' -OutFile 'c3-les-textes-de-notre-constitution.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [5/16] Le texte de la Constitution de la Ve Republique (dossier)
if exist "c3-theme2-le-texte-de-la-constitution.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-02/Cycle%%203%%20-%%20Th%%C3%%A8me%%202.pdf' -OutFile 'c3-theme2-le-texte-de-la-constitution.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [6/16] Jeu : Es-tu incollable sur la Constitution de la Ve Republique ?
if exist "jeu-es-tu-incollable-constitution-ve-republique.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/jeu-es-tu-incollable-sur-la-Constitution-de-la-Ve-Republique-8-10_ans.pdf' -OutFile 'jeu-es-tu-incollable-constitution-ve-republique.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [7/16] Comment la Constitution organise la vie democratique
if exist "c3-theme4-vie-democratique.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-02/Cycle%%203%%20-%%20Th%%C3%%A8me%%204.pdf' -OutFile 'c3-theme4-vie-democratique.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [8/16] Le president de la Republique
if exist "c3-le-president-de-la-republique.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-07/C3_President_Republique.pdf' -OutFile 'c3-le-president-de-la-republique.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [9/16] Le parcours d'une loi
if exist "le-parcours-d-une-loi.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/Parcours_Loi_8-10_ans.pdf' -OutFile 'le-parcours-d-une-loi.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [10/16] La procedure d'elaboration des lois (dossier 2025)
if exist "c3-theme5-elaboration-des-lois.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2025-10/V3_T5-Cycle_3-nouveau-bureau-2.pdf' -OutFile 'c3-theme5-elaboration-des-lois.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [11/16] Jeu : Que sais-tu sur la procedure d'elaboration des lois ?
if exist "jeu-que-sais-tu-elaboration-des-lois.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/jeu-que%%20sais-tu-sur-la-procedure-d-elaboration-des-lois-8-10_ans_0.pdf' -OutFile 'jeu-que-sais-tu-elaboration-des-lois.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [12/16] Les valeurs et principes de la Republique francaise
if exist "valeurs-et-principes-de-la-republique.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/Valeur_Principe_republique_8-10_ans.pdf' -OutFile 'valeurs-et-principes-de-la-republique.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [13/16] Les symboles de la Republique francaise
if exist "c3-les-symboles-de-la-republique.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-07/C3_Symbole_Republique.pdf' -OutFile 'c3-les-symboles-de-la-republique.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [14/16] Les libertes en France
if exist "les-libertes-en-france.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/Libertes_en_France_8-10_ans.pdf' -OutFile 'les-libertes-en-france.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [15/16] La Constitution au quotidien
if exist "la-constitution-au-quotidien.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/la_constitution_dans_quotidien_8-10_ans.pdf' -OutFile 'la-constitution-au-quotidien.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo [16/16] La Constitution dans ta vie quotidienne (dossier)
if exist "c3-theme8-la-constitution-dans-ta-vie-quotidienne.pdf" (
  echo        deja present, ignore.
  set /a SAUTES+=1
) else (
  powershell -NoProfile -Command "try{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;Invoke-WebRequest -Uri 'https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-02/Cycle%%203%%20-%%20Th%%C3%%A8me%%208_0.pdf' -OutFile 'c3-theme8-la-constitution-dans-ta-vie-quotidienne.pdf' -UseBasicParsing;exit 0}catch{exit 1}"
  if errorlevel 1 ( echo        ECHEC & set /a KO+=1 ) else ( echo        telecharge. & set /a OK+=1 )
)

echo.
echo ============================================================
echo  Termine : %OK% telecharge(s), %SAUTES% deja present(s), %KO% en echec.
echo ============================================================
echo.
echo Les fiches sont dans : %cd%
echo Relancez ce script pour reessayer les fichiers en echec.
echo.
pause
endlocal
