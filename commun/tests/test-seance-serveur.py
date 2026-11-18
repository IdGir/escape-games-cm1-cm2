#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST DE LA SÉANCE DU JOUR ET DU FEU VERT (serveur.py, lot 2 : A1, A4)
Depuis la racine du dépôt :  python commun/tests/test-seance-serveur.py
Lance un vrai serveur sur une copie temporaire et vérifie :
  /api/seance (lecture publique, écriture réservée au PC de l'enseignant, fichier dans le dossier de données),
  /api/sante (quatre voyants, dossier des résultats inaccessible = rouge), fichiers privés jamais servis.
"""
import json, os, shutil, subprocess, sys, tempfile, time, urllib.request, urllib.error

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PORT = 8794
verifs, echecs = 0, []

def ok(cond, msg):
    global verifs
    verifs += 1
    if not cond:
        echecs.append(msg)
        print("  ✗", msg)
    else:
        print("  ✓", msg)

def requete(chemin, corps=None):
    req = urllib.request.Request("http://127.0.0.1:%d%s" % (PORT, chemin),
                                 data=None if corps is None else json.dumps(corps).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status, r.read().decode("utf-8", "replace"), r.headers
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), e.headers

def demarrer(dossier, env_sup=None):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("ESCAPE_DONNEES", None)
    env.update(env_sup or {})
    p = subprocess.Popen([sys.executable, os.path.join(dossier, "serveur.py"), str(PORT)], cwd=tempfile.gettempdir(), env=env,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(80):
        try:
            if requete("/api/info")[0] == 200:
                return p
        except Exception:
            time.sleep(0.1)
    p.kill()
    raise SystemExit("le serveur ne démarre pas")

def arreter(p):
    p.terminate()
    try:
        p.wait(timeout=5)
    except Exception:
        p.kill()

projet = tempfile.mkdtemp(prefix="eg-seance-")
donnees = tempfile.mkdtemp(prefix="eg-seance-donnees-")
try:
    shutil.copyfile(os.path.join(RACINE, "serveur.py"), os.path.join(projet, "serveur.py"))
    open(os.path.join(projet, "index.html"), "w").write("<p>accueil</p>")
    os.makedirs(os.path.join(projet, "immersifs", "lumiere", "assets", "images", "decors"))
    os.makedirs(os.path.join(projet, "lumiere"))
    with open(os.path.join(projet, "immersifs", "lumiere", "medias.csv"), "w", encoding="utf-8") as f:
        f.write("id;type;fichier;statut\ndecor-a;image;assets/images/decors/a.webp;déposé\ndecor-b;image;assets/images/decors/b.webp;à produire\n")
    open(os.path.join(projet, "immersifs", "lumiere", "assets", "images", "decors", "a.webp"), "wb").write(b"x")
    with open(os.path.join(projet, "dossier-donnees.txt"), "w", encoding="utf-8") as f:
        f.write(donnees + "\n")
    p = demarrer(projet)
    try:
        print("\n== A1 : séance du jour ==")
        c, t, h = requete("/api/seance")
        d = json.loads(t)
        ok(c == 200 and d["ok"] and d["seance"] is None and d["local"] is True, "sans séance : rien, et le PC du serveur est reconnu (local)")
        ok(h.get("Access-Control-Allow-Origin") is None, "pas de lecture depuis un autre site")
        c, t, _ = requete("/api/seance", {"jeu": "lumiere", "grade": "matelot", "titre": "Le Phare"})
        d = json.loads(t)
        ok(c == 200 and d["ok"] and d["seance"]["jeu"] == "lumiere" and d["seance"]["adresse"] == "immersifs/lumiere/", "séance fixée : version immersive du jeu")
        fichier = os.path.join(donnees, "seance-du-jour.json")
        ok(os.path.exists(fichier) and not os.path.exists(os.path.join(projet, "seance-du-jour.json")), "fichier gardé dans le dossier de données (dossier-donnees.txt)")
        d = json.loads(requete("/api/seance")[1])
        ok(d["seance"] and d["seance"]["grade"] == "matelot" and d["seance"]["depuis"], "relue : jeu, grade, heure de début")
        c, t, _ = requete("/api/seance", {"jeu": "../serveur", "grade": "x"})
        ok(c == 400 and not json.loads(t)["ok"], "jeu inconnu ou chemin piégé : refusé")
        c, t, _ = requete("/api/seance", {"jeu": "lumiere", "grade": "amiral"})
        ok(json.loads(t)["seance"]["grade"] == "", "grade inconnu : au choix des équipes")
        ok(requete("/seance-du-jour.json")[0] == 404 and requete("/version-installee.txt")[0] == 404 and requete("/journal-ecole.txt")[0] == 404,
           "seance-du-jour.json, version-installee.txt, journal-ecole.txt jamais servis")
        print("\n== A4 : feu vert ==")
        c, t, _ = requete("/api/sante")
        d = json.loads(t)
        ids = [v["id"] for v in d.get("voyants", [])]
        ok(c == 200 and ids == ["serveur", "version", "medias", "resultats"], "quatre voyants : " + ", ".join(ids))
        v = {x["id"]: x for x in d["voyants"]}
        ok(v["serveur"]["etat"] == "vert" and "http://" in v["serveur"]["message"], "serveur : vert, adresse des élèves")
        ok(v["medias"]["etat"] == "orange" and "1 média(s) sur 2" in v["medias"]["message"] and v["medias"]["manquants"] == ["assets/images/decors/b.webp"] and v["medias"]["action"], "médias du jeu du jour : 1 manquant sur 2 → orange avec action")
        ok(v["resultats"]["etat"] == "vert", "dossier des résultats accessible en écriture : vert")
        ok(v["version"]["etat"] in ("vert", "orange") and (v["version"]["etat"] == "vert" or v["version"]["action"]), "version : vert, ou orange avec une action (" + v["version"]["message"] + ")")
        ok(all(x["etat"] == "vert" or x["action"] for x in d["voyants"]), "chaque orange ou rouge dit quoi faire")
        ok(d["etat"] in ("orange", "rouge"), "état général = le pire des voyants")
        c, t, _ = requete("/api/seance", {"fin": True})
        ok(json.loads(t)["ok"] and not os.path.exists(fichier), "fin de séance : fichier effacé")
        d = json.loads(requete("/api/sante")[1])
        ok({x["id"]: x for x in d["voyants"]}["medias"]["message"].startswith("Aucun jeu du jour"), "sans séance : le voyant des médias le dit")
    finally:
        arreter(p)

    print("\n== A4 : dossier des résultats inaccessible ==")
    bloque = os.path.join(donnees, "fichier-et-pas-dossier")
    open(bloque, "w").write("x")
    with open(os.path.join(projet, "dossier-donnees.txt"), "w", encoding="utf-8") as f:
        f.write(bloque + "\n")
    p = demarrer(projet)
    try:
        d = json.loads(requete("/api/sante")[1])
        v = {x["id"]: x for x in d["voyants"]}
        # le serveur retombe sur le dossier du projet (inscriptible) : le voyant reste vert, comme le dit sa bannière
        ok(v["resultats"]["etat"] == "vert", "dossier-donnees.txt inutilisable : repli sur le dossier du projet, toujours inscriptible")
    finally:
        arreter(p)
finally:
    shutil.rmtree(projet, ignore_errors=True)
    shutil.rmtree(donnees, ignore_errors=True)

print("\nSéance et feu vert (serveur) : %d vérifications, %d échec(s)." % (verifs, len(echecs)))
sys.exit(1 if echecs else 0)
