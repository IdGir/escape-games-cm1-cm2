# ============================================================
#  Production des medias du jeu "Le Sceau de la Republique"
#  - 1re partie : photos libres de droits (Wikimedia Commons)
#  - 2e partie  : images generees par l'API Agnes AI
#  - 3e partie  : videos generees par l'API Agnes AI
#  Les fichiers deja presents ne sont jamais regeneres.
#  Journal detaille : journal-medias.txt
# ============================================================

$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$Ici      = $PSScriptRoot
$Racine   = Resolve-Path (Join-Path $Ici "..\..")      # dossier constitution/
$Manifeste= Join-Path $Ici "medias.json"
$Journal  = Join-Path $Ici "journal-medias.txt"
$EtatFic  = Join-Path $Ici "etat-medias.json"

function Note($texte) {
  $ligne = "{0}  {1}" -f (Get-Date -Format "HH:mm:ss"), $texte
  Add-Content -Path $Journal -Value $ligne -Encoding UTF8
}
function Dire($texte, $couleur = "Gray") { Write-Host $texte -ForegroundColor $couleur; Note $texte }

if (-not (Test-Path $Manifeste)) { Write-Host "medias.json introuvable." -ForegroundColor Red; exit 1 }
$M = Get-Content $Manifeste -Raw -Encoding UTF8 | ConvertFrom-Json

# ---- Cle API -------------------------------------------------
$Cle = $env:AGNES_API_KEY
if (-not $Cle) {
  $ficCle = Join-Path $Ici "cle-agnes.txt"
  if (Test-Path $ficCle) { $Cle = (Get-Content $ficCle -Raw).Trim() }
}
$FaireIA = $true
if (-not $Cle) {
  Write-Host ""
  Write-Host "Aucune cle API Agnes trouvee." -ForegroundColor Yellow
  Write-Host "  -> Les photos des lieux seront quand meme telechargees."
  Write-Host "  -> Pour les personnages et les videos, creez le fichier :"
  Write-Host "     $Ici\cle-agnes.txt   (il contient uniquement votre cle)"
  Write-Host ""
  $FaireIA = $false
}

# ---- Etat (URL des images generees, pour l'image-to-video) ----
$Etat = @{}
if (Test-Path $EtatFic) {
  try { (Get-Content $EtatFic -Raw -Encoding UTF8 | ConvertFrom-Json).PSObject.Properties |
          ForEach-Object { $Etat[$_.Name] = $_.Value } } catch { $Etat = @{} }
}
function SauverEtat { ($Etat | ConvertTo-Json -Depth 4) | Set-Content $EtatFic -Encoding UTF8 }

function CheminCible($relatif) {
  $p = Join-Path $Racine $relatif
  $dossier = Split-Path $p -Parent
  if (-not (Test-Path $dossier)) { New-Item -ItemType Directory -Path $dossier -Force | Out-Null }
  return $p
}

$ok = 0; $saute = 0; $echec = 0

# ============================================================
#  1. PHOTOS DES LIEUX REELS
# ============================================================
Write-Host ""
Write-Host "=== 1/3  Photos des lieux reels (Wikimedia Commons) ===" -ForegroundColor Cyan
foreach ($p in $M.photos) {
  $cible = CheminCible $p.cible
  $nom = Split-Path $p.cible -Leaf
  if (Test-Path $cible) { Dire "  = $nom deja present"; $saute++; continue }
  try {
    Invoke-WebRequest -Uri $p.url -OutFile $cible -UseBasicParsing
    $ko = [math]::Round((Get-Item $cible).Length / 1KB)
    Dire "  + $nom  ($($p.titre), $ko Ko)" "Green"; $ok++
  } catch {
    Dire "  ! $nom : echec ($($_.Exception.Message))" "Red"; $echec++
  }
}

# ============================================================
#  2. IMAGES GENEREES (Agnes)
# ============================================================
Write-Host ""
Write-Host "=== 2/3  Images generees par Agnes ===" -ForegroundColor Cyan
if (-not $FaireIA) { Dire "  (ignore : aucune cle API)" "Yellow" }
else {
  $urlImg = $M.api.base + "/v1/images/generations"
  foreach ($im in $M.images) {
    $cible = CheminCible $im.cible
    $nom = Split-Path $im.cible -Leaf
    if (Test-Path $cible) { Dire "  = $nom deja present"; $saute++; continue }
    Write-Host "  . $nom  ($($im.nom))"
    $corps = @{ model = $M.api.modele_image; prompt = $im.prompt; size = $im.taille; n = 1 }
    try {
      $r = Invoke-RestMethod -Uri $urlImg -Method Post -ContentType "application/json" `
            -Headers @{ Authorization = "Bearer $Cle" } `
            -Body ($corps | ConvertTo-Json -Depth 4 -Compress)
      Note ("    reponse : " + ($r | ConvertTo-Json -Depth 6 -Compress))
      $d = $null
      if ($r.data) { $d = $r.data[0] } elseif ($r.images) { $d = $r.images[0] } else { $d = $r }
      $url = $null; $b64 = $null
      foreach ($champ in @("url","image_url","output_url")) { if (-not $url -and $d.$champ) { $url = $d.$champ } }
      foreach ($champ in @("b64_json","b64","image_base64","base64")) { if (-not $b64 -and $d.$champ) { $b64 = $d.$champ } }
      if ($url) {
        Invoke-WebRequest -Uri $url -OutFile $cible -UseBasicParsing
        $Etat[$im.cle] = $url; SauverEtat
      } elseif ($b64) {
        [IO.File]::WriteAllBytes($cible, [Convert]::FromBase64String(($b64 -replace '^data:image/\w+;base64,', '')))
      } else { throw "ni URL ni base64 dans la reponse (voir journal-medias.txt)" }
      $ko = [math]::Round((Get-Item $cible).Length / 1KB)
      Dire "  + $nom  ($ko Ko)" "Green"; $ok++
    } catch {
      Dire "  ! $nom : echec ($($_.Exception.Message))" "Red"; $echec++
    }
  }
}

# ============================================================
#  3. VIDEOS GENEREES (Agnes, asynchrone)
# ============================================================
Write-Host ""
Write-Host "=== 3/3  Videos generees par Agnes ===" -ForegroundColor Cyan
if (-not $FaireIA) { Dire "  (ignore : aucune cle API)" "Yellow" }
else {
  $urlVid = $M.api.base + "/v1/videos"
  foreach ($v in $M.videos) {
    $cible = CheminCible $v.cible
    $nom = Split-Path $v.cible -Leaf
    if (Test-Path $cible) { Dire "  = $nom deja present"; $saute++; continue }

    # Image de depart : URL Commons, ou URL de l'image generee a l'etape 2
    $imgUrl = $null
    if ($v.depuis_url) { $imgUrl = $v.depuis_url }
    elseif ($v.depuis_image) {
      $cleSource = [IO.Path]::GetFileNameWithoutExtension($v.depuis_image)
      if ($Etat.ContainsKey($cleSource)) { $imgUrl = $Etat[$cleSource] }
    }
    if ($v.depuis_image -and -not $imgUrl) {
      Dire "  ! $nom : image de depart non disponible en ligne, video ignoree" "Yellow"; $echec++; continue
    }

    Write-Host "  . $nom  ($($v.nom))"
    $corps = @{ model = $M.api.modele_video; prompt = $v.prompt; width = $v.largeur; height = $v.hauteur;
                num_frames = $v.images; frame_rate = $v.fps; negative_prompt = $M.negatif }
    if ($imgUrl) { $corps.image = $imgUrl }
    try {
      $r = Invoke-RestMethod -Uri $urlVid -Method Post -ContentType "application/json" `
            -Headers @{ Authorization = "Bearer $Cle" } `
            -Body ($corps | ConvertTo-Json -Depth 4 -Compress)
      Note ("    creation : " + ($r | ConvertTo-Json -Depth 6 -Compress))
      $id = $null
      foreach ($champ in @("video_id","id","task_id","request_id")) { if (-not $id -and $r.$champ) { $id = $r.$champ } }
      if (-not $id -and $r.data) { foreach ($champ in @("video_id","id","task_id")) { if (-not $id -and $r.data.$champ) { $id = $r.data.$champ } } }
      if (-not $id) { throw "aucun identifiant de tache dans la reponse" }

      $lien = $null
      for ($essai = 1; $essai -le 60; $essai++) {
        Start-Sleep -Seconds 10
        $s = Invoke-RestMethod -Uri ($M.api.base + "/agnesapi?video_id=" + $id) -Method Get `
               -Headers @{ Authorization = "Bearer $Cle" }
        $brut = ($s | ConvertTo-Json -Depth 8 -Compress)
        if ($brut -match '"(https?://[^"]+\.mp4)"') { $lien = $Matches[1]; break }
        if ($brut -match '"status"\s*:\s*"(failed|error)"') { throw "generation en echec cote serveur" }
        Write-Host ("    ... en cours (" + ($essai * 10) + " s)") -ForegroundColor DarkGray
      }
      if (-not $lien) { throw "delai depasse (10 min)" }
      Invoke-WebRequest -Uri $lien -OutFile $cible -UseBasicParsing
      $mo = [math]::Round((Get-Item $cible).Length / 1MB, 1)
      Dire "  + $nom  ($mo Mo)" "Green"; $ok++
    } catch {
      Dire "  ! $nom : echec ($($_.Exception.Message))" "Red"; $echec++
    }
  }
}

# ============================================================
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ("  Termine : {0} produit(s), {1} deja present(s), {2} en echec." -f $ok, $saute, $echec)
Write-Host "  Detail complet : journal-medias.txt"
Write-Host "  Relancez ce script pour reprendre les fichiers manquants."
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
