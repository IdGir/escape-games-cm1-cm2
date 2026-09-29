# ============================================================
#  Production des medias d'un escape game (script commun)
#  Usage : produire-medias.ps1 -Jeu <dossier du jeu>
#  Lit <jeu>\assets\medias\medias.json :
#   1. photos   : lieux reels, Wikimedia Commons (credits auto)
#   2. images   : personnages et scenes generiques, API Agnes
#   3. videos   : animees a partir des photos / images, API Agnes
#  Les fichiers deja presents ne sont jamais regeneres :
#  relancer le script reprend simplement ce qui manque.
# ============================================================
param([Parameter(Mandatory=$true)][string]$Jeu)

$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$UA = "EscapeGamesCM1CM2/1.0 (https://github.com/IdGir/escape-games-cm1-cm2)"

$Outils  = $PSScriptRoot
$Depot   = Resolve-Path (Join-Path $Outils "..")
$Racine  = Join-Path $Depot $Jeu
$Medias  = Join-Path $Racine "assets\medias"
$Manif   = Join-Path $Medias "medias.json"
$Journal = Join-Path $Medias "journal-medias.txt"
$EtatFic = Join-Path $Medias "etat-medias.json"
$Credits = Join-Path $Medias "CREDITS-medias.md"

if (-not (Test-Path $Manif)) { Write-Host "Pas de manifeste : $Manif" -ForegroundColor Red; exit 1 }
$M = Get-Content $Manif -Raw -Encoding UTF8 | ConvertFrom-Json

function Note($t) { Add-Content -Path $Journal -Value ("{0}  {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $t) -Encoding UTF8 }
function Dire($t, $c = "Gray") { Write-Host $t -ForegroundColor $c; Note $t }

# ---- Cle API Agnes ------------------------------------------
$Cle = $null; $SourceCle = $null
$f0 = Join-Path $Outils "cle-agnes.txt"
if (Test-Path $f0) { $Cle = (Get-Content $f0 -Raw).Trim(); $SourceCle = $f0 }
if (-not $Cle -and $env:AGNES_API_KEY) { $Cle = $env:AGNES_API_KEY.Trim(); $SourceCle = "variable Windows AGNES_API_KEY" }
foreach ($f in @((Join-Path $Medias "cle-agnes.txt"), (Join-Path $Depot "constitution\assets\medias\cle-agnes.txt"))) {
  if (-not $Cle -and (Test-Path $f)) { $Cle = (Get-Content $f -Raw).Trim(); $SourceCle = $f }
}
if ($Cle) { Note ("Cle Agnes lue depuis : $SourceCle (" + $Cle.Length + " caracteres)") }
$script:CleAgnesAPI = $Cle
$FaireIA = [bool]$Cle
if (-not $FaireIA) { Dire "Aucune cle Agnes (outils-medias\cle-agnes.txt) : seules les photos seront telechargees." "Yellow" }

# ---- Etat : URL en ligne de chaque photo / image ------------
$Etat = @{}; $Cred = @{}
if (Test-Path $EtatFic) {
  try {
    $e = Get-Content $EtatFic -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($e.urls)    { $e.urls.PSObject.Properties    | ForEach-Object { $Etat[$_.Name] = $_.Value } }
    if ($e.credits) { $e.credits.PSObject.Properties | ForEach-Object { $Cred[$_.Name] = $_.Value } }
  } catch { }
}
function SauverEtat { (@{ urls = $Etat; credits = $Cred } | ConvertTo-Json -Depth 6) | Set-Content $EtatFic -Encoding UTF8 }

function Cible($rel) {
  $p = Join-Path $Racine ($rel -replace '/', '\')
  $d = Split-Path $p -Parent
  if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
  return $p
}
function SansHtml($s) { if (-not $s) { return "" }; return (($s -replace '<[^>]+>', '') -replace '\s+', ' ').Trim() }

# Convertit une image en vrai JPEG (Windows uniquement)
function VersJpeg($src, $dst) {
  Add-Type -AssemblyName System.Drawing
  $img = [System.Drawing.Image]::FromFile($src)
  $img.Save($dst, [System.Drawing.Imaging.ImageFormat]::Jpeg); $img.Dispose()
}
# Enregistre un fichier telecharge ; convertit en JPEG si la cible est .jpg
function Enregistrer($url, $cible) {
  $tmp = "$cible.tmp"
  Invoke-WebRequest -Uri $url -OutFile $tmp -UseBasicParsing -UserAgent $UA
  if ($cible -match '\.jpe?g$' -and $env:OS -eq 'Windows_NT') {
    try { VersJpeg $tmp $cible; Remove-Item $tmp -Force; return } catch { }
  }
  Move-Item $tmp $cible -Force
}

# Image locale -> data URI JPEG recadree au format de la video (Agnes ne peut pas
# telecharger les photos de Wikimedia : erreur 400)
function RecadrerJpeg($chemin, $l, $h) {
  Add-Type -AssemblyName System.Drawing
  $src = [System.Drawing.Image]::FromFile($chemin)
  $rc = $l / [double]$h; $rs = $src.Width / [double]$src.Height
  if ($rs -gt $rc) { $ch = $src.Height; $cw = [int]($ch * $rc); $cx = [int](($src.Width - $cw) / 2); $cy = 0 }
  else { $cw = $src.Width; $ch = [int]($cw / $rc); $cx = 0; $cy = [int](($src.Height - $ch) / 2) }
  $bmp = New-Object System.Drawing.Bitmap($l, $h)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $g.DrawImage($src, (New-Object System.Drawing.Rectangle(0, 0, $l, $h)), (New-Object System.Drawing.Rectangle($cx, $cy, $cw, $ch)), [System.Drawing.GraphicsUnit]::Pixel)
  $ms = New-Object IO.MemoryStream
  $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
  $ep = New-Object System.Drawing.Imaging.EncoderParameters(1)
  $ep.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]88)
  $bmp.Save($ms, $codec, $ep)
  $g.Dispose(); $bmp.Dispose(); $src.Dispose()
  return $ms.ToArray()
}
function DataUriLocale($chemin, $l, $h) {
  $octets = $null
  if ($env:OS -eq 'Windows_NT') {
    try { $octets = RecadrerJpeg $chemin $l $h } catch { Note "    recadrage impossible : $($_.Exception.Message)" }
  }
  if (-not $octets) { $octets = [IO.File]::ReadAllBytes($chemin) }
  return "data:image/jpeg;base64," + [Convert]::ToBase64String($octets)
}

# ---- Wikimedia Commons --------------------------------------
function InfosCommons($requete) {
  $r = Invoke-RestMethod -Uri $requete -UserAgent $UA
  if (-not $r.query -or -not $r.query.pages) { return @() }
  $liste = @()
  foreach ($p in $r.query.pages.PSObject.Properties) {
    $v = $p.Value; if (-not $v.imageinfo) { continue }
    $ii = $v.imageinfo[0]; $idx = 0; if ($v.index) { $idx = [int]$v.index }
    $liste += [pscustomobject]@{ idx = $idx; titre = $v.title; l = [int]$ii.width; h = [int]$ii.height;
      url = $(if ($ii.thumburl) { $ii.thumburl } else { $ii.url }); page = $ii.descriptionurl;
      auteur = SansHtml $ii.extmetadata.Artist.value; licence = SansHtml $ii.extmetadata.LicenseShortName.value }
  }
  return $liste | Sort-Object idx
}
$BaseC = "https://commons.wikimedia.org/w/api.php"; if ($env:COMMONS_API) { $BaseC = $env:COMMONS_API }
$ApiC = $BaseC + "?action=query&format=json&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=1920"
function ParNom($nom) { return InfosCommons ($ApiC + "&titles=" + [uri]::EscapeDataString("File:" + $nom)) | Select-Object -First 1 }
function ParRecherche($q, $paysage, $rang) {
  $l = InfosCommons ($ApiC + "&generator=search&gsrnamespace=6&gsrlimit=20&gsrsearch=" + [uri]::EscapeDataString("$q filetype:bitmap"))
  $ok = @($l | Where-Object { $_.l -ge 1000 -and ((-not $paysage) -or ($_.l / [double]$_.h -ge 1.25)) })
  if ($ok.Count -eq 0) { return $null }
  $i = [math]::Min([math]::Max(1, [int]$rang), $ok.Count) - 1
  return $ok[$i]
}


# ---- Appels Agnes freines (compte gratuit : 10 requetes/minute) ----
$script:DernierAppel = [datetime]::MinValue
$script:EchecsCle = 0
function AppelAgnes($uri, $methode, $corps) {
  for ($t = 1; $t -le 4; $t++) {
    $ecart = ((Get-Date) - $script:DernierAppel).TotalSeconds
    if ($ecart -lt 8) { Start-Sleep -Seconds ([math]::Ceiling(8 - $ecart)) }
    $script:DernierAppel = Get-Date
    try {
      $p = @{ Uri = $uri; Method = $methode; Headers = @{ Authorization = "Bearer $script:CleAgnesAPI" } }
      if ($corps) { $p.ContentType = "application/json; charset=utf-8"; $p.Body = [Text.Encoding]::UTF8.GetBytes(($corps | ConvertTo-Json -Depth 4 -Compress)) }
      $r = Invoke-RestMethod @p
      $script:EchecsCle = 0
      return $r
    } catch {
      $code = 0; try { $code = [int]$_.Exception.Response.StatusCode } catch { }
      if (($code -eq 401 -or $code -eq 429) -and $t -lt 4) {
        $pause = 60 * [math]::Pow(2, $t - 1)
        Dire ("    Agnes refuse ({0}) : pause de {1} s puis nouvel essai ({2}/3)" -f $code, $pause, $t) "Yellow"
        Start-Sleep -Seconds $pause; continue
      }
      if ($code -eq 401 -or $code -eq 429) { $script:EchecsCle++ }
      throw
    }
  }
}
function CleBloquee {
  if ($script:EchecsCle -ge 2) { Dire "  Agnes refuse la cle de facon repetee : arret de la partie IA (relancer plus tard)." "Red"; return $true }
  return $false
}

$ok = 0; $saute = 0; $echec = 0
Write-Host ""; Write-Host "############  $($M.titre)  ($Jeu)" -ForegroundColor White

# ============================================================
Write-Host "=== 1/3  Photos des lieux reels (Wikimedia Commons) ===" -ForegroundColor Cyan
foreach ($p in $M.photos) {
  $cible = Cible $p.cible
  $clePhoto = $p.cle; if (-not $clePhoto) { $clePhoto = [IO.Path]::GetFileNameWithoutExtension($p.cible) }
  $nom = Split-Path $p.cible -Leaf
  if ((Test-Path $cible) -and $Etat.ContainsKey($clePhoto)) { Dire "  = $nom deja present"; $saute++; continue }
  try {
    $info = $null
    if ($p.fichier_commons) { $info = ParNom $p.fichier_commons }
    elseif ($p.recherche)   { $rang = 1; if ($p.rang) { $rang = $p.rang }; $info = ParRecherche $p.recherche ([bool]$p.paysage) $rang }
    if (-not $info) { throw "aucune photo trouvee pour : $($p.recherche)" }
    if (-not (Test-Path $cible)) { Enregistrer $info.url $cible }
    $Etat[$clePhoto] = $info.url
    $Cred[$nom + "|" + $p.cible] = @{ fichier = $p.cible; lieu = $p.lieu; titre = $info.titre; page = $info.page; auteur = $info.auteur; licence = $info.licence }
    SauverEtat
    Dire "  + $nom  ($($info.titre) - $($info.licence))" "Green"; $ok++
  } catch { Dire "  ! $nom : echec ($($_.Exception.Message))" "Red"; $echec++ }
}

# ============================================================
Write-Host "=== 2/3  Images generees par Agnes ===" -ForegroundColor Cyan
if (-not $FaireIA) { Dire "  (ignore : aucune cle API)" "Yellow" } else {
  foreach ($im in $M.images) {
    if (CleBloquee) { break }
    $cible = Cible $im.cible; $nom = Split-Path $im.cible -Leaf
    if (Test-Path $cible) { Dire "  = $nom deja present"; $saute++; continue }
    Write-Host "  . $nom  ($($im.nom))"
    $corps = @{ model = $M.api.modele_image; prompt = $im.prompt; size = $im.taille; n = 1 }
    try {
      $r = AppelAgnes ($M.api.base + "/v1/images/generations") "Post" $corps
      Note ("    reponse : " + ($r | ConvertTo-Json -Depth 6 -Compress))
      $d = $r; if ($r.data) { $d = $r.data[0] } elseif ($r.images) { $d = $r.images[0] }
      $url = $null; foreach ($c in @("url","image_url","output_url")) { if (-not $url -and $d.$c) { $url = $d.$c } }
      $b64 = $null; foreach ($c in @("b64_json","b64","image_base64","base64")) { if (-not $b64 -and $d.$c) { $b64 = $d.$c } }
      if ($url) { Enregistrer $url $cible; $Etat[$im.cle] = $url; SauverEtat }
      elseif ($b64) { [IO.File]::WriteAllBytes($cible, [Convert]::FromBase64String(($b64 -replace '^data:image/\w+;base64,', ''))) }
      else { throw "ni URL ni base64 dans la reponse (voir journal)" }
      Dire "  + $nom" "Green"; $ok++
    } catch {
      $det = $_.Exception.Message
      try { $det += " " + (New-Object IO.StreamReader($_.Exception.Response.GetResponseStream())).ReadToEnd() } catch { }
      if ($_.ErrorDetails -and $_.ErrorDetails.Message) { $det += " " + $_.ErrorDetails.Message }
      Dire "  ! $nom : echec ($det)" "Red"; $echec++
    }
  }
}

# ============================================================
Write-Host "=== 3/3  Videos generees par Agnes ===" -ForegroundColor Cyan
if (-not $FaireIA) { Dire "  (ignore : aucune cle API)" "Yellow" } else {
  foreach ($v in $M.videos) {
    if (CleBloquee) { break }
    $cible = Cible $v.cible; $nom = Split-Path $v.cible -Leaf
    if (Test-Path $cible) { Dire "  = $nom deja present"; $saute++; continue }
    # image de depart : cle d'une photo / image produite plus haut (ou anciens champs)
    $src = $v.depuis
    if (-not $src -and $v.depuis_image) { $src = [IO.Path]::GetFileNameWithoutExtension($v.depuis_image) }
    $imgUrl = $null
    if ($src -and $Etat.ContainsKey($src)) { $imgUrl = $Etat[$src] }
    elseif ($v.depuis_url) {
      $imgUrl = $v.depuis_url
      if ($imgUrl -match 'Special:FilePath/([^?]+)') { $i = ParNom ([uri]::UnescapeDataString($Matches[1]) -replace '_', ' '); if ($i) { $imgUrl = $i.url } }
    }
    if (-not $imgUrl) { Dire "  ! $nom : image de depart absente (relancer apres les images), video ignoree" "Yellow"; $echec++; continue }

    Write-Host "  . $nom  ($($v.nom))"
    $l = 1152; $h = 768; if ($v.largeur) { $l = $v.largeur; $h = $v.hauteur }
    # photo Wikimedia (ou lien externe) : on envoie le fichier local, recadre
    $photoSrc = @($M.photos | Where-Object { $_.cle -eq $src }) | Select-Object -First 1
    if ($photoSrc -or ($imgUrl -notmatch 'agnes-ai')) {
      $local = $null
      if ($photoSrc) { $local = Join-Path $Racine ($photoSrc.cible -replace '/', '\') }
      if ($local -and (Test-Path $local)) { $imgUrl = DataUriLocale $local $l $h; Note "    image de depart : fichier local $($photoSrc.cible) ($([math]::Round($imgUrl.Length/1KB)) Ko en base64)" }
    }
    $corps = @{ model = $M.api.modele_video; prompt = $v.prompt; width = $l; height = $h; num_frames = 121; frame_rate = 24;
                negative_prompt = $M.negatif; image = $imgUrl }
    try {
      $r = AppelAgnes ($M.api.base + "/v1/videos") "Post" $corps
      Note ("    creation : " + ($r | ConvertTo-Json -Depth 6 -Compress))
      $id = $null
      foreach ($c in @("video_id","id","task_id","request_id")) { if (-not $id -and $r.$c) { $id = $r.$c } }
      if (-not $id -and $r.data) { foreach ($c in @("video_id","id","task_id")) { if (-not $id -and $r.data.$c) { $id = $r.data.$c } } }
      if (-not $id) { throw "aucun identifiant de tache dans la reponse" }
      $lien = $null
      for ($n = 1; $n -le 40; $n++) {
        Start-Sleep -Seconds 12
        $s = AppelAgnes ($M.api.base + "/agnesapi?video_id=" + $id) "Get" $null
        $brut = ($s | ConvertTo-Json -Depth 8 -Compress)
        if ($brut -match '"(https?://[^"]+\.mp4)"') { $lien = $Matches[1]; break }
        if ($brut -match '"status"\s*:\s*"(failed|error)"') { Note "    statut : $brut"; throw "generation en echec cote serveur" }
        Write-Host ("    ... en cours (" + ($n * 12) + " s)") -ForegroundColor DarkGray
      }
      if (-not $lien) { throw "delai depasse (10 min)" }
      Enregistrer $lien $cible
      Dire ("  + $nom  ({0} Mo)" -f [math]::Round((Get-Item $cible).Length / 1MB, 1)) "Green"; $ok++
    } catch {
      $det = $_.Exception.Message
      try { $det += " " + (New-Object IO.StreamReader($_.Exception.Response.GetResponseStream())).ReadToEnd() } catch { }
      if ($_.ErrorDetails -and $_.ErrorDetails.Message) { $det += " " + $_.ErrorDetails.Message }
      Dire "  ! $nom : echec ($det)" "Red"; $echec++
    }
  }
}

# ---- Credits des photos -------------------------------------
if ($Cred.Count -gt 0) {
  $t = @("# Credits des photographies - $($M.titre)", "",
         "Photos de lieux et d'oeuvres reels, Wikimedia Commons (licences libres). Les videos animees a partir d'une photo",
         "sous licence CC BY-SA heritent de cette licence. Personnages et scenes generiques : images creees avec Agnes AI,",
         "personnages entierement fictifs.", "",
         "| Fichier | Sujet | Source | Auteur | Licence |", "|---|---|---|---|---|")
  foreach ($c in ($Cred.Values | Sort-Object { $_.fichier })) {
    $t += "| ``$($c.fichier)`` | $($c.lieu) | [$($c.titre)]($($c.page)) | $($c.auteur) | $($c.licence) |"
  }
  $t | Set-Content $Credits -Encoding UTF8
}

Write-Host ""
Write-Host ("  {0} : {1} produit(s), {2} deja present(s), {3} en echec." -f $Jeu, $ok, $saute, $echec) -ForegroundColor Cyan
Write-Host "  Journal : $Jeu\assets\medias\journal-medias.txt   (relancer pour reprendre)"
Write-Host ""
