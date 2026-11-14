#!/usr/bin/env python3
"""Fabrique de nuit des médias des jeux immersifs (stratégie du 14/11/2026, carte C3).

Lancé chaque soir par le Planificateur de tâches de Windows (installer-nuit.bat), sans Claude et sans vous :
  1. choisit le jeu en tête de file : le premier jeu immersif dont il manque une voix, une image ou une vidéo,
     dans l'ordre des besoins de la classe (FILE ci-dessous ; un nouveau jeu s'ajoute tout seul à la fin) ;
  2. voix des personnages (Edge, gratuites) : tout ce qui manque ;
  3. images Agnes (décors, portraits) : au plus --max-images par nuit, déposées aussitôt dans le jeu ;
  4. vidéos Agnes (transitions, depuis le décor de la salle) : au plus --max-videos par nuit ;
  5. arrêt de la partie Agnes au deuxième refus (clé, quota, panne) ;
  6. compte rendu : outils-medias/nuit/derniere-nuit.json (lu par Claude le lendemain matin) et journal.txt.
Rien n'est commité ni publié : la finition (Claude) vérifie, intègre et vous présente le jeu à valider.

    python outils-medias/nuit/nuit-medias.py                 la nuit normale
    python outils-medias/nuit/nuit-medias.py --essai         montre ce qui serait fait, sans rien appeler
    python outils-medias/nuit/nuit-medias.py --jeu lumiere   force un jeu
Clé Agnes : variable AGNES_API_KEY, sinon outils-medias/cle-agnes.txt (jamais affichée).
"""
import argparse, csv, datetime, glob, json, os, subprocess, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
IMM = os.path.join(RACINE, "immersifs")
JOURNAL = os.path.join(ICI, "journal.txt")
BILAN = os.path.join(ICI, "derniere-nuit.json")
# Ordre des besoins de la classe (Année A en 2026-2027) : période en cours d'abord, puis P1 reportés, puis P3.
FILE = ["lumiere", "versailles", "alimentation", "moyen-age-abbaye", "station-meteo", "objets-techniques",
        "traite-colonies", "electricite", "etats-matiere", "mouvement", "naissances-animaux", "grandes-explorations",
        "melanges", "chateau-fort", "renaissance", "constitution"]
SOURCE_CREDIT, LICENCE = "Agnes AI (génération de nuit)", "Image générée par IA"
ENV = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")


def log(msg):
    ligne = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ") + msg
    print(ligne, flush=True)
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def cle_agnes():
    if ENV.get("AGNES_API_KEY"):
        return True
    for p in (os.path.join(RACINE, "outils-medias", "cle-agnes.txt"), os.path.join(RACINE, "constitution", "assets", "medias", "cle-agnes.txt")):
        if os.path.isfile(p):
            k = open(p, encoding="utf-8-sig").read().strip()
            if k:
                ENV["AGNES_API_KEY"] = k
                return True
    return False


def jeux_en_file():
    presents = sorted(d for d in os.listdir(IMM) if os.path.isfile(os.path.join(IMM, d, "medias.csv")))
    return [j for j in FILE if j in presents] + [j for j in presents if j not in FILE]


def lignes(jeu):
    with open(os.path.join(IMM, jeu, "medias.csv"), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def manque(jeu, l):
    return not os.path.isfile(os.path.join(IMM, jeu, l["fichier"]))


def voix_manquantes(jeu):
    """Nombre de répliques sans mp3 (selon generer-voix.py --essai), ou None si l'outil n'est pas là."""
    outil = os.path.join(IMM, jeu, "outils", "voix", "generer-voix.py")
    if not os.path.isfile(outil):
        return None
    idx = os.path.join(IMM, jeu, "assets", "audio", "voix", "index.json")
    return 0 if os.path.isfile(idx) else -1      # -1 : jamais générées


def a_faire(jeu):
    L = lignes(jeu)
    img = [l for l in L if l["type"] == "image" and manque(jeu, l) and l["id"].startswith(("decor-", "portrait-"))]
    vid = [l for l in L if l["type"].startswith("vid") and manque(jeu, l)]
    return img, vid, voix_manquantes(jeu)


def lancer(jeu, args, essai, limite=900):
    cmd = [sys.executable] + args
    if essai:
        log("   (essai) " + " ".join(os.path.relpath(a, os.path.join(IMM, jeu)) if os.path.isabs(a) else a for a in args))
        return 0, ""
    try:
        r = subprocess.run(cmd, cwd=os.path.join(IMM, jeu), env=ENV, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=limite)
    except subprocess.TimeoutExpired:
        return 99, "délai dépassé"
    sortie = (r.stdout or "") + (r.stderr or "")
    return r.returncode, sortie[-600:]


def proposition(jeu, ident, exts):
    fichiers = []
    for e in exts:
        fichiers += glob.glob(os.path.join(IMM, jeu, "assets", "medias-proposes", f"{ident}-v*.{e}"))
    return max(fichiers, key=os.path.getmtime) if fichiers else None


def assurer_depart_data_uri(jeu, essai):
    """Agnes accepte l'image de départ en data URI : aucune publication préalable n'est nécessaire."""
    p = os.path.join(IMM, jeu, "outils", "medias", "sources-medias.json")
    if not os.path.isfile(p):
        return
    cfg = json.load(open(p, encoding="utf-8"))
    v = ((cfg.get("sources") or {}).get("agnes") or {}).get("video") or {}
    if (v.get("depart") or {}).get("mode") != "data-uri":
        log(f"   {jeu} : image de départ des vidéos envoyée en data URI (sources-medias.json)")
        if not essai:
            v["depart"] = {"mode": "data-uri"}
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                json.dump(cfg, f, ensure_ascii=False, indent=2)
                f.write("\n")


def main():
    a = argparse.ArgumentParser(description="Fabrique de nuit des médias des jeux immersifs")
    a.add_argument("--essai", action="store_true")
    a.add_argument("--jeu")
    a.add_argument("--max-images", type=int, default=10)
    a.add_argument("--max-videos", type=int, default=5)
    a.add_argument("--refus-max", type=int, default=2)
    o = a.parse_args()
    debut = time.time()
    bilan = {"date": datetime.date.today().isoformat(), "debut": datetime.datetime.now().isoformat(timespec="seconds"),
             "jeux": {}, "images": 0, "videos": 0, "refus": 0, "arret": "", "reste": {}}
    log("==== Nuit des médias" + (" (essai)" if o.essai else ""))
    agnes = cle_agnes()
    if not agnes:
        log("   Pas de clé Agnes : seules les voix sont produites cette nuit.")
        bilan["arret"] = "clé Agnes absente"
    file = [o.jeu] if o.jeu else jeux_en_file()
    imax, vmax, refus = o.max_images, o.max_videos, 0
    for jeu in file:
        img, vid, voix = a_faire(jeu)
        if not img and not vid and voix != -1:
            continue
        b = bilan["jeux"].setdefault(jeu, {"images": [], "videos": [], "voix": "", "erreurs": []})
        log(f"-- {jeu} : {len(img)} image(s), {len(vid)} vidéo(s) manquantes" + (", voix à générer" if voix == -1 else ""))
        # 1. voix (gratuites, sans Agnes)
        if voix is not None:
            rc, s = lancer(jeu, [os.path.join("outils", "voix", "generer-voix.py")], o.essai, limite=1800)
            b["voix"] = "ok" if rc == 0 else "échec : " + s.strip().splitlines()[-1][:200] if s.strip() else "échec"
            log("   voix : " + b["voix"])
        if not agnes or refus >= o.refus_max:
            continue
        assurer_depart_data_uri(jeu, o.essai)
        # 2. images : décors d'abord (ils servent de départ aux vidéos), puis portraits
        img.sort(key=lambda l: (not l["id"].startswith("decor-"), l["id"]))
        for l in img:
            if imax <= 0 or refus >= o.refus_max:
                break
            rc, s = lancer(jeu, [os.path.join("outils", "medias", "produire.py"), "--id", l["id"], "--variantes", "1", "--max-images", "1"], o.essai)
            prop = None if o.essai else proposition(jeu, l["id"], ("webp", "png", "jpg"))
            if rc != 0 or (not o.essai and not prop):
                refus += 1; b["erreurs"].append(f"{l['id']} : {s.strip()[-200:]}")
                log(f"   ✖ {l['id']} refusé ({refus}/{o.refus_max})")
                continue
            imax -= 1
            nom = l["id"].split("-", 1)[1]
            opts = ["--decor", nom] if l["id"].startswith("decor-") else ["--portrait", nom]
            if l["id"].startswith("decor-"):      # le décor sert aussi d'image de départ à la vidéo de sa salle
                for v in lignes(jeu):
                    dep = v.get("reference_ou_depart") or ""
                    if v["type"].startswith("vid") and v.get("escale") == l.get("escale") and dep.startswith("assets/medias-depart/"):
                        opts += ["--depart", os.path.splitext(os.path.basename(dep))[0]]
            rc, s = lancer(jeu, [os.path.join("outils", "medias", "importer-image.py"), prop or "PROPOSITION", *opts, "--source", SOURCE_CREDIT, "--licence", LICENCE], o.essai)
            if rc == 0:
                b["images"].append(l["id"]); bilan["images"] += 1; log(f"   ✔ {l['id']}")
            else:
                b["erreurs"].append(f"import {l['id']} : {s.strip()[-200:]}"); log(f"   ✖ import {l['id']}")
        # 3. vidéos : image de départ tirée du décor déjà déposé si elle manque, puis seulement les vidéos qui ont leur départ
        decors = {d["escale"]: d for d in lignes(jeu) if d["id"].startswith("decor-")}
        for v in vid:
            dep = v.get("reference_ou_depart") or ""
            d = decors.get(v.get("escale"))
            if dep.startswith("assets/medias-depart/") and not os.path.isfile(os.path.join(IMM, jeu, dep)) and d and not manque(jeu, d):
                lancer(jeu, [os.path.join("outils", "medias", "importer-image.py"), os.path.join(IMM, jeu, d["fichier"]),
                             "--depart", os.path.splitext(os.path.basename(dep))[0], "--source", SOURCE_CREDIT, "--licence", LICENCE], o.essai)
        #    vidéos : seulement si leur image de départ existe
        for l in [v for v in vid if os.path.isfile(os.path.join(IMM, jeu, v.get("reference_ou_depart") or "~")) or o.essai]:
            if vmax <= 0 or refus >= o.refus_max:
                break
            rc, s = lancer(jeu, [os.path.join("outils", "medias", "produire.py"), "--types", "video", "--id", l["id"], "--max-videos", "1",
                                 "--depart", l["reference_ou_depart"]], o.essai, limite=1800)
            prop = None if o.essai else proposition(jeu, l["id"], ("mp4",))
            if rc != 0 or (not o.essai and not prop):
                refus += 1; b["erreurs"].append(f"{l['id']} : {s.strip()[-200:]}")
                log(f"   ✖ {l['id']} refusé ({refus}/{o.refus_max})")
                continue
            vmax -= 1
            nom = os.path.splitext(os.path.basename(l["fichier"]))[0]
            rc, s = lancer(jeu, [os.path.join("outils", "medias", "importer-image.py"), prop or "PROPOSITION", "--video", nom, "--source", SOURCE_CREDIT, "--licence", "Vidéo générée par IA"], o.essai)
            if rc == 0:
                b["videos"].append(l["id"]); bilan["videos"] += 1; log(f"   ✔ {l['id']}")
            else:
                b["erreurs"].append(f"import {l['id']} : {s.strip()[-200:]}"); log(f"   ✖ import {l['id']}")
        if b["images"] or b["videos"]:
            lancer(jeu, [os.path.join("outils", "embarquer-donnees.py")], o.essai)
        if imax <= 0 and vmax <= 0:
            break
    if refus >= o.refus_max:
        bilan["arret"] = f"arrêt de la partie Agnes après {refus} refus (clé, quota ou panne : voir les erreurs)"
    bilan["refus"] = refus
    for jeu in jeux_en_file():
        img, vid, voix = a_faire(jeu)
        if img or vid or voix == -1:
            bilan["reste"][jeu] = {"images": len(img), "videos": len(vid), "voix": voix == -1}
    bilan["fin"] = datetime.datetime.now().isoformat(timespec="seconds")
    bilan["duree_min"] = round((time.time() - debut) / 60, 1)
    if not o.essai:
        with open(BILAN, "w", encoding="utf-8") as f:
            json.dump(bilan, f, ensure_ascii=False, indent=2)
    log(f"==== Fin : {bilan['images']} image(s), {bilan['videos']} vidéo(s), {refus} refus ; jeux restants : {len(bilan['reste'])}")


if __name__ == "__main__":
    main()
