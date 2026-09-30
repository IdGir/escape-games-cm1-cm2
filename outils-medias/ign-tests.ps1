# Test IGN (Geoplateforme) : telecharge la liste des couches et quelques cartes d'essai
# de la France, calees sur le dessin de mission-geo (projection lineaire, voir journal).
$ErrorActionPreference = "Continue"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$UA = "EscapeGamesCM1CM2/1.0 (https://github.com/IdGir/escape-games-cm1-cm2)"
$Dossier = Join-Path $PSScriptRoot "ign-tests"
New-Item -ItemType Directory -Path $Dossier -Force | Out-Null
$Log = Join-Path $Dossier "log.txt"
"Test IGN " + (Get-Date -Format "yyyy-MM-dd HH:mm:ss") | Set-Content $Log -Encoding UTF8

$Base = "https://data.geopf.fr/wms-r"
Write-Host "1/2  Liste des couches disponibles..." -ForegroundColor Cyan
try {
  Invoke-WebRequest -Uri ($Base + "?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities") -OutFile (Join-Path $Dossier "capabilities.xml") -UseBasicParsing -UserAgent $UA
  Write-Host "   OK : capabilities.xml" -ForegroundColor Green
} catch { Write-Host "   ECHEC : $($_.Exception.Message)" -ForegroundColor Red; Add-Content $Log ("capabilities : " + $_.Exception.Message) }

# France : longitude -5.456 a 10.096, latitude 40.87 a 51.38 (ordre WMS 1.3.0 : lat,lon)
$Bbox = "40.87,-5.456,51.38,10.096"
$Couches = @("GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2", "ADMINEXPRESS-COG-CARTO.LATEST", "ADMINEXPRESS-COG.LATEST", "LIMITES_ADMINISTRATIVES_EXPRESS.LATEST", "ORTHOIMAGERY.ORTHOPHOTOS")
Write-Host "2/2  Cartes d'essai..." -ForegroundColor Cyan
foreach ($c in $Couches) {
  $fic = Join-Path $Dossier ("france-" + ($c -replace '[^A-Za-z0-9]+', '-') + ".png")
  $u = $Base + "?LAYERS=$c&FORMAT=image/png&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&STYLES=&CRS=EPSG:4326&BBOX=$Bbox&WIDTH=1240&HEIGHT=1040&TRANSPARENT=false"
  try {
    Invoke-WebRequest -Uri $u -OutFile $fic -UseBasicParsing -UserAgent $UA
    $t = (Get-Item $fic).Length
    if ($t -lt 3000) { Write-Host ("   ? $c : fichier tres petit ({0} o), couche sans doute absente" -f $t) -ForegroundColor Yellow; Add-Content $Log "$c : petit fichier ($t octets)" }
    else { Write-Host ("   + $c  ({0} Ko)" -f [int]($t/1024)) -ForegroundColor Green }
  } catch { Write-Host "   ! $c : $($_.Exception.Message)" -ForegroundColor Red; Add-Content $Log ("$c : " + $_.Exception.Message) }
}
Write-Host ""
Write-Host "Termine. Resultats dans outils-medias\ign-tests" -ForegroundColor Cyan
