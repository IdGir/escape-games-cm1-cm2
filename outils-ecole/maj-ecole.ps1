# ================================================================
#  MISE A JOUR SANS GIT (PC de l'ecole) - appele par demarrer-ecole.bat
#  Compare la version installee (version-installee.txt) au dernier commit
#  de la branche escape-games sur GitHub ; si elle a change, telecharge
#  l'archive de la branche et la copie dans le dossier des jeux, SANS
#  toucher aux donnees de la classe (resultats, dossier-donnees.txt...).
#  Sans internet : on garde la version installee, sans erreur.
# ================================================================
$ErrorActionPreference = 'Stop'
$racine  = Split-Path -Parent $PSScriptRoot
$depot   = 'IdGir/escape-games-cm1-cm2'
$branche = 'escape-games'
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}

try {
    $sha = (Invoke-RestMethod -Uri "https://api.github.com/repos/$depot/commits/$branche" -Headers @{ 'User-Agent' = 'escape-games-ecole' } -TimeoutSec 20).sha
} catch {
    Write-Output "GitHub injoignable (pas d'internet ?) : version installee gardee."
    exit 0
}
$fichierVersion = Join-Path $racine 'version-installee.txt'
$actuelle = ''
if (Test-Path $fichierVersion) { $actuelle = (Get-Content $fichierVersion -TotalCount 1).Trim() }
if ($actuelle -eq $sha) { Write-Output "Deja a jour ($($sha.Substring(0,7)))."; exit 0 }

$tmp = Join-Path $env:TEMP 'escape-games-maj'
Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $tmp | Out-Null
$zip = Join-Path $tmp 'depot.zip'
Write-Output "Telechargement de la version $($sha.Substring(0,7)) (plusieurs minutes la premiere fois)..."
try {
    Invoke-WebRequest -Uri "https://github.com/$depot/archive/refs/heads/$branche.zip" -OutFile $zip -UseBasicParsing -TimeoutSec 3600
    Expand-Archive -Path $zip -DestinationPath $tmp -Force
} catch {
    Write-Output "Telechargement interrompu : version installee gardee. ($($_.Exception.Message))"
    Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
    exit 0
}
$src = Get-ChildItem $tmp -Directory | Select-Object -First 1
# Copie : les fichiers de la classe ne sont jamais remplaces ni effaces.
robocopy $src.FullName $racine /E /NFL /NDL /NJH /NJS /NP /R:1 /W:1 `
    /XF resultats-classe.jsonl resultats-classe.csv dossier-donnees.txt seance-du-jour.json difficulte-classe.json version-installee.txt journal-ecole.txt diagnostic.txt copie-nextcloud.txt 'cle-*.txt' `
    /XD sauvegardes-resultats .git | Out-Null
if ($LASTEXITCODE -ge 8) {
    Write-Output "Copie incomplete (code robocopy $LASTEXITCODE) : relancer demarrer-ecole.bat."
    exit 1
}
Set-Content -Path $fichierVersion -Value $sha -Encoding ASCII
Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
Write-Output "Mise a jour installee : $($sha.Substring(0,7))."
exit 0
