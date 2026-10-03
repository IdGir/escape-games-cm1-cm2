#!/usr/bin/env python3
"""Génération FACULTATIVE des médias avec l'API Agnes AI (images et vidéos), d'après medias.csv.

Rien n'entre dans le jeu automatiquement : les propositions sont écrites dans assets/medias-proposes/
(<id>-v1.webp|.png, <id>-v1.mp4), exclues du dépôt par .gitignore. L'enseignant choisit ensuite dans
outils/choisir-medias.html et dépose le fichier retenu sous son nom définitif.

Documentation lue le 3 octobre 2026 (wiki.agnes-ai.com) — à revérifier avant usage :
  images : POST https://apihub.agnes-ai.com/v1/images/generations, modèle agnes-image-2.5-flash,
           size « 1K|2K|3K|4K », ratio « 16:9|3:4|… », extra_body.image = [URL ou data URI] (image→image),
           extra_body.response_format = « url » (ou return_base64: true) ;
  vidéos : POST https://apihub.agnes-ai.com/v1/videos, modèle agnes-video-2.5, mode « keyframe »,
           first_frame = URL PUBLIQUE, seconds « 4 »…« 12 », size « 720P », aspect_ratio « 16:9 » ;
           puis GET https://apihub.agnes-ai.com/agnesapi?video_id=…&model_name=agnes-video-2.5
           toutes les 2 s jusqu'à status « completed » (champ url) ou « failed ».

Clé : jamais écrite nulle part. Si l'environnement injecte lui-même l'authentification (proxy), le script
n'ajoute AUCUN en-tête ; en cas de 401/403 il réessaie avec la variable d'environnement AGNES_API_KEY si elle
existe, sinon il s'arrête proprement.

Exemples :
  python generer-medias.py --essai                       (affiche les appels prévus, n'appelle rien)
  python generer-medias.py --seulement portrait-nemo --variantes 2 --max-images 2
  python generer-medias.py --videos --seulement video-transition-e2 --depart-url https://… --max-videos 1
"""
import argparse, base64, csv, json, os, sys, time, urllib.request, urllib.error

ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)
SORTIE = os.path.join(JEU, "assets", "medias-proposes")
JOURNAL = os.path.join(SORTIE, "generation.log")
BASE = "https://apihub.agnes-ai.com"
MODELE_IMAGE, MODELE_IMAGE_REPLI = "agnes-image-2.5-flash", "agnes-image-2.1-flash"
MODELE_VIDEO = "agnes-video-2.5-flash"     # gratuit (promotion, octobre 2026), 720P seulement ; repli payant : agnes-video-2.5
# Références publiques (dépôt public) : l'API lit les images par URL, sans les renvoyer en base64
REFS_URL = "https://raw.githubusercontent.com/IdGir/escape-games-cm1-cm2/claude/tender-shannon-aq897z/vingt-mille-lieues/"
COUT_VIDEO_PAR_S = 0.0        # agnes-video-2.5-flash : 0 $/s (promotion) ; agnes-video-2.5 : 0,025 $/s en 720P
ORDRE = ["portrait-", "cadre-", "decor-", "video-"]


def journal(msg):
    os.makedirs(SORTIE, exist_ok=True)
    ligne = time.strftime("%Y-%m-%d %H:%M:%S ") + msg
    print(ligne)
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def appel(methode, url, corps=None, essai_cle=False):
    """Appel HTTP JSON. Sans clé d'abord ; avec AGNES_API_KEY seulement après 401/403. La clé n'est jamais journalisée."""
    entetes = {"Content-Type": "application/json"}
    cle = os.environ.get("AGNES_API_KEY") if essai_cle else None
    if cle:
        entetes["Authorization"] = "Bearer " + cle
    donnees = json.dumps(corps).encode("utf-8") if corps is not None else None
    req = urllib.request.Request(url, data=donnees, headers=entetes, method=methode)
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code in (401, 403) and not essai_cle and os.environ.get("AGNES_API_KEY"):
            return appel(methode, url, corps, essai_cle=True)
        if e.code in (401, 403):
            raise SystemExit("Accès refusé par l'API Agnes (401/403) : aucune clé utilisable. Arrêt sans rien générer de plus.")
        raise RuntimeError(f"HTTP {e.code} : {e.read()[:300].decode('utf-8', 'replace')}")


def telecharger(url, chemin):
    with urllib.request.urlopen(url, timeout=300) as r, open(chemin, "wb") as f:
        f.write(r.read())


def data_uri(chemin):
    ext = os.path.splitext(chemin)[1].lower().lstrip(".") or "png"
    with open(chemin, "rb") as f:
        return f"data:image/{'jpeg' if ext == 'jpg' else ext};base64," + base64.b64encode(f.read()).decode("ascii")


def references(ligne, base_url):
    """Images de référence : URL publique pour les fichiers déjà publiés (references/), sinon data URI."""
    refs = []
    for r in (ligne.get("reference_ou_depart") or "").replace(";", ",").split(","):
        r = r.strip().split(" ")[0]
        p = os.path.join(JEU, r)
        if os.path.isfile(p) and (r.startswith("references/") or r.startswith("assets/")):
            refs.append(base_url + r if (base_url and r.startswith("references/")) else data_uri(p))
    return refs[:4]


def recadrer(chemin, dims):
    """Recadre au format exact (centre) puis redimensionne, en WebP : Pillow, sinon ImageMagick."""
    try:
        w, h = [int(x) for x in dims.split(" ")[0].replace("×", "x").split("x")]
    except ValueError:
        return chemin
    sortie = chemin.rsplit(".", 1)[0] + ".webp"
    try:
        from PIL import Image
        im = Image.open(chemin).convert("RGB")
        r = w / h
        if im.width / im.height > r:
            nw = int(im.height * r); im = im.crop(((im.width - nw) // 2, 0, (im.width - nw) // 2 + nw, im.height))
        else:
            nh = int(im.width / r); im = im.crop((0, (im.height - nh) // 2, im.width, (im.height - nh) // 2 + nh))
        im.resize((w, h), Image.LANCZOS).save(sortie, "WEBP", quality=86)
    except ImportError:
        import subprocess
        subprocess.run(["convert", chemin, "-resize", f"{w}x{h}^", "-gravity", "center", "-extent", f"{w}x{h}", "-quality", "86", sortie], check=True)
    os.remove(chemin)
    return sortie


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--essai", action="store_true", help="afficher les appels sans les faire")
    a.add_argument("--seulement", action="append", help="identifiant(s) de medias.csv")
    a.add_argument("--variantes", type=int, default=1, help="propositions par média (1 à 4)")
    a.add_argument("--max-images", type=int, default=4, help="plafond d'images générées (défaut 4)")
    a.add_argument("--max-videos", type=int, default=0, help="plafond de vidéos générées (défaut 0 : aucune)")
    a.add_argument("--videos", action="store_true", help="traiter aussi les lignes vidéo")
    a.add_argument("--depart-url", help="URL PUBLIQUE de l'image de départ (vidéo keyframe)")
    a.add_argument("--fin-url", help="URL PUBLIQUE de l'image de fin (vidéo keyframe, facultatif)")
    a.add_argument("--refs-url", default=REFS_URL, help="adresse publique du dossier du jeu (références lues par URL)")
    a.add_argument("--prompt-supplement", default="", help="texte ajouté au prompt (consigne de composition…)")
    o = a.parse_args()
    o.variantes = max(1, min(4, o.variantes))
    with open(os.path.join(JEU, "medias.csv"), encoding="utf-8") as f:
        lignes = [l for l in csv.DictReader(f, delimiter=";") if l["prompt_en"] or l["type"] == "vidéo"]
    lignes = [l for l in lignes if (not o.seulement or l["id"] in o.seulement)]
    lignes = [l for l in lignes if l["type"] == "image" or o.videos]
    lignes = [l for l in lignes if l["prompt_fr"] and not l["prompt_fr"].startswith("À rédiger")]
    lignes.sort(key=lambda l: next((i for i, p in enumerate(ORDRE) if l["id"].startswith(p)), 9))
    n_img = sum(o.variantes for l in lignes if l["type"] == "image")
    n_vid = sum(o.variantes for l in lignes if l["type"] == "vidéo")
    print(f"Prévu : {min(n_img, o.max_images)} image(s) (plafond {o.max_images}), {min(n_vid, o.max_videos)} vidéo(s) (plafond {o.max_videos}).")
    print(f"Coût estimé : images {MODELE_IMAGE} 0 $ au tarif promotionnel affiché ; vidéos ≈ {min(n_vid, o.max_videos) * 8 * COUT_VIDEO_PAR_S:.2f} $ (8 s, 720P). Vérifiez les tarifs du jour.")
    faites_i = faites_v = 0
    for l in lignes:
        for v in range(1, o.variantes + 1):
            ext = "mp4" if l["type"] == "vidéo" else "png"
            cible = os.path.join(SORTIE, f"{l['id']}-v{v}.{ext}")
            if os.path.exists(cible) or os.path.exists(cible.rsplit(".", 1)[0] + ".webp"):
                print(f"= {l['id']}-v{v} existe déjà : rien à refaire"); continue
            if l["type"] == "image":
                if faites_i >= o.max_images: print("Plafond d'images atteint."); break
                refs = references(l, o.refs_url)
                corps = {"model": MODELE_IMAGE, "prompt": (l["prompt_fr"] + " " + o.prompt_supplement).strip(), "size": "2K",
                         "ratio": l["ratio"] if l["ratio"] in ("1:1", "3:4", "4:3", "16:9", "9:16", "2:3", "3:2", "21:9") else "16:9",
                         "extra_body": {"response_format": "b64_json"}}
                if refs:
                    corps["extra_body"]["image"] = [r if r.startswith("http") else "<data URI>" for r in refs] if o.essai else refs
                if o.essai:
                    print(f"[essai] POST {BASE}/v1/images/generations → {os.path.relpath(cible, JEU)}\n        " + json.dumps(corps, ensure_ascii=False)[:400] + "…"); faites_i += 1; continue
                try:
                    r = appel("POST", BASE + "/v1/images/generations", corps)
                except RuntimeError as e:
                    journal(f"{l['id']} : échec avec {MODELE_IMAGE} ({e}) ; essai avec {MODELE_IMAGE_REPLI}")
                    corps["model"] = MODELE_IMAGE_REPLI
                    try: r = appel("POST", BASE + "/v1/images/generations", corps)
                    except RuntimeError as e2: journal(f"{l['id']} : échec ({e2}) — on passe"); continue
                d = (r.get("data") or [{}])[0]
                os.makedirs(SORTIE, exist_ok=True)
                if d.get("b64_json"):
                    with open(cible, "wb") as f: f.write(base64.b64decode(d["b64_json"]))
                elif d.get("url"):
                    try: telecharger(d["url"], cible)
                    except Exception as e: journal(f"{l['id']} : téléchargement impossible ({e})"); continue
                else: journal(f"{l['id']} : réponse sans image"); continue
                final = recadrer(cible, l["dimensions"]); faites_i += 1
                journal(f"{l['id']}-v{v} : image reçue → {os.path.relpath(final, JEU)}")
            else:
                if faites_v >= o.max_videos: print("Plafond de vidéos atteint (0 par défaut : --max-videos N pour autoriser)."); break
                if not o.depart_url:
                    print(f"! {l['id']} : il faut l'URL PUBLIQUE du décor validé (--depart-url). Hébergement public temporaire nécessaire."); break
                corps = {"model": MODELE_VIDEO, "prompt": (l["prompt_fr"] + " " + o.prompt_supplement).strip(), "mode": "keyframe", "first_frame": o.depart_url,
                         "seconds": "8", "size": "720P", "aspect_ratio": "16:9"}
                if o.fin_url: corps["last_frame"] = o.fin_url
                if o.essai:
                    print(f"[essai] POST {BASE}/v1/videos → {os.path.relpath(cible, JEU)}\n        " + json.dumps(corps, ensure_ascii=False)[:400]); faites_v += 1; continue
                r = {}
                for essai_file in range(30):
                    try:
                        r = appel("POST", BASE + "/v1/videos", corps)
                    except RuntimeError as e:
                        if "video_queue_full" in str(e) or "HTTP 503" in str(e) or "HTTP 502" in str(e):
                            journal(f"{l['id']} : file d'attente pleine, nouvel essai dans 60 s"); time.sleep(60); continue
                        raise
                    if r.get("code") != "video_queue_full": break
                    journal(f"{l['id']} : file d'attente pleine, nouvel essai dans 60 s"); time.sleep(60)
                vid = r.get("video_id")
                if not vid:
                    journal(f"{l['id']} : création refusée ({json.dumps(r)[:200]})"); continue
                journal(f"{l['id']} : tâche vidéo {vid} créée")
                for _ in range(200):
                    time.sleep(10)
                    try:
                        s = appel("GET", f"{BASE}/agnesapi?video_id={vid}&model_name={MODELE_VIDEO}")
                    except RuntimeError as e:
                        if "HTTP 429" in str(e): time.sleep(30); continue
                        raise
                    if s.get("status") == "completed" and s.get("url"):
                        telecharger(s["url"], cible); journal(f"{l['id']}-v{v} : vidéo reçue"); break
                    if s.get("status") == "failed":
                        journal(f"{l['id']} : génération échouée ({s.get('error')})"); break
                faites_v += 1
    print("Terminé. Propositions :", os.path.relpath(SORTIE, JEU), "— à comparer dans outils/choisir-medias.html")


if __name__ == "__main__":
    main()
