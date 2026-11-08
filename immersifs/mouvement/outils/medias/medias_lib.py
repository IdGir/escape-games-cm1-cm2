"""Bibliothèque commune de la production de médias (images, vidéos) : sources branchables, clés d'API, hébergement des images de départ.

Une SOURCE de production est décrite dans sources-medias.json (rien à programmer pour un service qui parle JSON sur HTTP) :
  - « cle » : nom de la variable d'environnement qui contient la clé (jamais la clé elle-même), en-tête et format à employer ;
  - « image » : une requête qui rend une image (en base64 ou par URL) ;
  - « video » : une requête de création, puis une requête de sondage jusqu'au fichier final ;
  - ou « adaptateur » : un petit fichier Python pour les services qui sortent de ce cadre (fichiers multipart, signatures…).
Les valeurs {prompt}, {modele}, {taille}, {ratio}, {refs}, {depart}, {fin}, {secondes}, {id}, {base_url}, {cle} sont remplacées dans les modèles.

Aucune dépendance externe : bibliothèque standard de Python 3.8+. La clé n'est JAMAIS écrite dans un fichier, un journal ou l'écran.
"""
import base64, copy, importlib.util, json, os, re, subprocess, sys, time, urllib.error, urllib.parse, urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(os.path.dirname(ICI))                       # dossier du jeu (contient assets/, medias.csv…)
SORTIE = os.path.join(JEU, "assets", "medias-proposes")
JOURNAL = os.path.join(SORTIE, "generation.log")
FICHIER_SOURCES = os.path.join(ICI, "sources-medias.json")
FICHIER_CLES = os.path.join(JEU, "cles-api.local")                # facultatif, JAMAIS commité (.gitignore) : lignes NOM=valeur
CODES_A_RETENTER = (429, 500, 502, 503, 504)
DELAI = float(os.environ.get("MEDIAS_DELAI_S", 20))               # attente entre deux reprises (secondes)


class ErreurSource(Exception):
    pass


# ------------------------------------------------------------------ clés d'API
def charger_cles_locales():
    """Lit cles-api.local (NOM=valeur) dans l'environnement, sans rien écraser."""
    if os.path.isfile(FICHIER_CLES):
        for ligne in open(FICHIER_CLES, encoding="utf-8"):
            ligne = ligne.strip()
            if ligne and not ligne.startswith("#") and "=" in ligne:
                k, v = ligne.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def cle_de(source):
    c = source.get("cle") or {}
    nom = c.get("env")
    if not nom:
        return None
    return os.environ.get(nom) or None


def masquer(texte, source=None):
    """Retire toute clé connue d'un texte avant de l'afficher ou de le journaliser."""
    t = str(texte)
    for nom, v in os.environ.items():
        if v and len(v) >= 8 and re.search(r"(KEY|TOKEN|SECRET|CLE|PASSWORD)", nom, re.I):
            t = t.replace(v, "***")
    return t


def journal(msg):
    os.makedirs(SORTIE, exist_ok=True)
    ligne = time.strftime("%Y-%m-%d %H:%M:%S ") + masquer(msg)
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    print(ligne)


# ------------------------------------------------------------------ sources
def lire_sources():
    with open(FICHIER_SOURCES, encoding="utf-8") as f:
        return json.load(f)


def source(nom, genre=None):
    d = lire_sources()
    nom = nom or (d.get("defaut") or {}).get(genre)
    s = (d.get("sources") or {}).get(nom)
    if not s:
        raise ErreurSource(f"Source inconnue : « {nom} ». Sources disponibles : {', '.join(sorted(d.get('sources', {})))}")
    s = copy.deepcopy(s)
    s["_nom"] = nom
    if s.get("base_url_env") and os.environ.get(s["base_url_env"]):
        s["base_url"] = os.environ[s["base_url_env"]]
    return s


# ------------------------------------------------------------------ modèles de requête
def remplir(modele, valeurs):
    """Remplace {nom} dans les chaînes d'une structure ; une valeur « {nom} » seule garde son type (liste, nombre) ; None → champ retiré."""
    if isinstance(modele, str):
        m = re.fullmatch(r"\{(\w+)\}", modele)
        if m:
            return valeurs.get(m.group(1), None)
        return re.sub(r"\{(\w+)\}", lambda x: str(valeurs.get(x.group(1), "") if valeurs.get(x.group(1)) is not None else ""), modele)
    if isinstance(modele, list):
        r = [remplir(x, valeurs) for x in modele]
        return [x for x in r if x is not None]
    if isinstance(modele, dict):
        r = {k: remplir(v, valeurs) for k, v in modele.items()}
        return {k: v for k, v in r.items() if v is not None}
    return modele


def extraire(donnees, chemin):
    """Chemin pointé : « data.0.b64_json »."""
    cur = donnees
    for p in str(chemin).split("."):
        if isinstance(cur, list):
            cur = cur[int(p)] if p.lstrip("-").isdigit() and -len(cur) <= int(p) < len(cur) else None
        elif isinstance(cur, dict):
            cur = cur.get(p)
        else:
            return None
        if cur is None:
            return None
    return cur


def entetes(source):
    h = {"Content-Type": "application/json", "User-Agent": "escape-games-medias/1.0"}
    c = source.get("cle") or {}
    cle = cle_de(source)
    if cle:
        h[c.get("en_tete", "Authorization")] = (c.get("format") or "Bearer {cle}").replace("{cle}", cle)
    elif c.get("env") and not c.get("optionnelle"):
        raise ErreurSource(
            f"Aucune clé pour la source « {source['_nom']} » : définissez la variable d'environnement {c['env']} "
            f"(PowerShell : $env:{c['env']}='…' ; ou une ligne {c['env']}=… dans cles-api.local, fichier jamais publié). "
            "Si votre environnement injecte déjà l'authentification (proxy), marquez la clé « optionnelle » dans sources-medias.json.")
    return h


def requete(source, methode, url, corps=None, essais=6, delai=None):
    """Requête JSON avec reprises (429, 5xx), clé masquée dans les messages."""
    delai = DELAI if delai is None else delai
    donnees = json.dumps(corps).encode("utf-8") if corps is not None else None
    for k in range(essais):
        req = urllib.request.Request(url, data=donnees, method=methode, headers=entetes(source))
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                brut = r.read()
                return json.loads(brut.decode("utf-8")) if brut else {}
        except urllib.error.HTTPError as e:
            texte = e.read()[:400].decode("utf-8", "replace")
            if e.code in CODES_A_RETENTER and k < essais - 1:
                journal(f"{source['_nom']} : HTTP {e.code}, nouvel essai dans {delai} s")
                time.sleep(delai)
                continue
            if e.code in (401, 403):
                raise ErreurSource(f"Accès refusé (HTTP {e.code}) par « {source['_nom']} » : clé absente, expirée ou sans droit. {masquer(texte)}")
            raise ErreurSource(f"HTTP {e.code} : {masquer(texte)}")
        except urllib.error.URLError as e:
            if k < essais - 1:
                time.sleep(min(delai, 5))
                continue
            raise ErreurSource(f"Réseau : {masquer(e.reason)}")
    raise ErreurSource("trop d'échecs")


def telecharger(url, chemin, source=None):
    req = urllib.request.Request(url, headers={"User-Agent": "escape-games-medias/1.0"})
    with urllib.request.urlopen(req, timeout=600) as r, open(chemin, "wb") as f:
        f.write(r.read())


# ------------------------------------------------------------------ images de départ (référence d'une image ou d'une vidéo)
def url_publique(chemin_relatif, config=None):
    """URL publique d'un fichier du jeu, pour les services qui lisent les images par adresse (vidéo « keyframe » notamment).
    Mode « raw-github » (défaut) : le fichier doit être poussé (git push) sur la branche ; mode « url-base » : <url>/<chemin>."""
    config = config or (lire_sources().get("hebergement_images") or {})
    rel = chemin_relatif.replace("\\", "/")
    if config.get("mode") == "url-base":
        return config["url_base"].rstrip("/") + "/" + rel
    remote = subprocess.run(["git", "-C", JEU, "remote", "get-url", "origin"], capture_output=True, text=True).stdout.strip()
    m = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", remote)
    branche = subprocess.run(["git", "-C", JEU, "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True).stdout.strip()
    if not m or not branche:
        raise ErreurSource("Hébergement « raw-github » impossible (dépôt GitHub introuvable) : configurez « hebergement_images » dans sources-medias.json.")
    prefixe = subprocess.run(["git", "-C", JEU, "rev-parse", "--show-prefix"], capture_output=True, text=True).stdout.strip()
    return f"https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}/{branche}/{prefixe}{rel}"


def verifier_url(url):
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "escape-games-medias/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 200
    except Exception:
        return False


def en_data_uri(chemin):
    ext = os.path.splitext(chemin)[1].lower().lstrip(".") or "png"
    with open(chemin, "rb") as f:
        return f"data:image/{'jpeg' if ext == 'jpg' else ext};base64," + base64.b64encode(f.read()).decode("ascii")


def url_publique_verifiee(chemin_fichier):
    url = url_publique(os.path.relpath(chemin_fichier, JEU))
    if not verifier_url(url):
        raise ErreurSource(f"L'image n'est pas encore publique : {url}\n  → poussez d'abord le fichier (git add / commit / push), ou configurez « hebergement_images » dans sources-medias.json.")
    return url


def image_de_depart(source, chemin_fichier):
    """Renvoie la valeur à mettre dans {depart} selon ce que la source accepte : URL publique, base64 ou data-URI."""
    mode = ((source.get("video") or {}).get("depart") or {}).get("mode", "url")
    rel = os.path.relpath(chemin_fichier, JEU)
    if mode == "base64":
        return base64.b64encode(open(chemin_fichier, "rb").read()).decode("ascii")
    if mode == "data-uri":
        return en_data_uri(chemin_fichier)
    url = url_publique(rel)
    if not verifier_url(url):
        raise ErreurSource(f"L'image de départ n'est pas encore publique : {url}\n  → poussez d'abord le fichier (git add / commit / push), ou configurez « hebergement_images ».")
    return url


# ------------------------------------------------------------------ conversion d'images (ImageMagick ou Pillow)
def convertir_image(entree, sortie, largeur, hauteur, qualite=86):
    """Recadre au centre au format exact puis redimensionne ; le format de sortie vient de l'extension."""
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    try:
        from PIL import Image
        im = Image.open(entree).convert("RGB")
        r = largeur / hauteur
        if im.width / im.height > r:
            nw = int(im.height * r)
            im = im.crop(((im.width - nw) // 2, 0, (im.width - nw) // 2 + nw, im.height))
        else:
            nh = int(im.width / r)
            im = im.crop((0, (im.height - nh) // 2, im.width, (im.height - nh) // 2 + nh))
        im.resize((largeur, hauteur), Image.LANCZOS).save(sortie, quality=qualite)
        return sortie
    except ImportError:
        pass
    for exe in (["magick"], ["convert"]):
        try:
            subprocess.run(exe + [entree, "-resize", f"{largeur}x{hauteur}^", "-gravity", "center", "-extent", f"{largeur}x{hauteur}", "-quality", str(qualite), sortie],
                           check=True, capture_output=True)
            return sortie
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue
    raise ErreurSource("Ni Pillow (pip install pillow) ni ImageMagick (convert/magick) ne sont disponibles pour convertir l'image.")


# ------------------------------------------------------------------ production
def adaptateur(source):
    chemin = source.get("adaptateur")
    if not chemin:
        return None
    p = chemin if os.path.isabs(chemin) else os.path.join(ICI, chemin)
    spec = importlib.util.spec_from_file_location("adaptateur_" + source["_nom"], p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def produire_image(source, prompt, ratio, taille, refs, modele=None, negatif=""):
    """Rend les octets d'une image (PNG/JPEG/WebP) ; essaie les modèles de la liste dans l'ordre."""
    ad = adaptateur(source)
    if ad and hasattr(ad, "produire_image"):
        return ad.produire_image(source, prompt=prompt, ratio=ratio, taille=taille, refs=refs, negatif=negatif)
    spec = source.get("image")
    if not spec:
        raise ErreurSource(f"La source « {source['_nom']} » ne produit pas d'images.")
    dernier = None
    for m in ([modele] if modele else spec.get("modeles") or [None]):
        t = (spec.get("tailles_par_ratio") or {}).get(ratio) or ((spec.get("tailles") or {}).get(taille, taille) if taille else spec.get("taille_defaut"))
        valeurs = {"prompt": prompt, "negatif": negatif, "modele": m, "ratio": ratio, "taille": t,
                   "refs": refs or None, "base_url": source.get("base_url", "")}
        try:
            r = requete(source, spec.get("methode", "POST"), remplir(spec["url"], valeurs), remplir(spec.get("corps"), valeurs))
        except ErreurSource as e:
            dernier = e
            journal(f"{source['_nom']} : échec avec {m} ({e})")
            if "Accès refusé" in str(e):
                raise
            continue
        b64 = extraire(r, (spec.get("reponse") or {}).get("b64", ""))
        if b64:
            return base64.b64decode(re.sub(r"^data:[^,]+,", "", b64))
        url = extraire(r, (spec.get("reponse") or {}).get("url", ""))
        if url:
            tmp = os.path.join(SORTIE, "_tmp_telechargement")
            os.makedirs(SORTIE, exist_ok=True)
            telecharger(url, tmp)
            data = open(tmp, "rb").read()
            os.remove(tmp)
            return data
        dernier = ErreurSource("réponse sans image (champs « reponse.b64 »/« reponse.url » à vérifier dans sources-medias.json)")
    raise dernier or ErreurSource("aucun modèle disponible")


def produire_video(source, prompt, depart, fin, secondes, modele=None, id_travail=None, reprise=None):
    """Crée un travail vidéo, sonde jusqu'à la fin et rend (url_finale, id_travail). `reprise` : identifiant d'un travail déjà créé."""
    ad = adaptateur(source)
    if ad and hasattr(ad, "produire_video"):
        return ad.produire_video(source, prompt=prompt, depart=depart, fin=fin, secondes=secondes)
    spec = source.get("video")
    if not spec:
        raise ErreurSource(f"La source « {source['_nom']} » ne produit pas de vidéos.")
    m = modele or (spec.get("modeles") or [None])[0]
    valeurs = {"prompt": prompt, "modele": m, "depart": depart, "fin": fin, "secondes": str(secondes), "base_url": source.get("base_url", "")}
    creer = spec["creer"]
    ident = reprise
    if not ident:
        r = requete(source, creer.get("methode", "POST"), remplir(creer["url"], valeurs), remplir(creer.get("corps"), valeurs), essais=spec.get("essais_file", 30), delai=min(spec.get("attente_file_s", 60), DELAI * 3) if "MEDIAS_DELAI_S" in os.environ else spec.get("attente_file_s", 60))
        ident = extraire(r, (creer.get("reponse") or {}).get("id", "id"))
        if not ident:
            raise ErreurSource("création refusée : " + masquer(json.dumps(r)[:200]))
        journal(f"{source['_nom']} : travail vidéo {ident} créé")
    so = spec["sonder"]
    valeurs["id"] = ident
    fini = set(so.get("termine", ["completed"]))
    echec = set(so.get("echec", ["failed"]))
    for _ in range(spec.get("sondages_max", 200)):
        time.sleep(so.get("intervalle_s", 10))
        try:
            r = requete(source, so.get("methode", "GET"), remplir(so["url"], valeurs), remplir(so.get("corps"), valeurs) if so.get("corps") else None, essais=4, delai=DELAI)
        except ErreurSource as e:
            if "HTTP 429" in str(e):
                time.sleep(DELAI)
                continue
            raise
        statut = extraire(r, so.get("statut", "status"))
        if statut in fini:
            url = extraire(r, so.get("url_video", "url"))
            if url:
                return url, ident
        if statut in echec:
            raise ErreurSource(f"génération échouée ({masquer(json.dumps(extraire(r, so.get('erreur', 'error'))))})")
    raise ErreurSource("délai dépassé en attendant la vidéo (reprendre plus tard avec --reprendre)")
