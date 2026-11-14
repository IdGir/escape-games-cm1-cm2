#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST DU STOCKAGE DES RÉSULTATS (serveur.py)
Depuis la racine du dépôt :  python commun/tests/test-resultats-serveur.py
Lance un vrai serveur sur une copie temporaire (autre dossier courant, autre port)
et vérifie : enregistrement automatique, aucun doublon, reprise après arrêt,
ligne abîmée, copie de sécurité, CSV sans formule, fichiers jamais servis,
dossier de données ailleurs (dossier-donnees.txt).
"""
import json, os, shutil, subprocess, sys, tempfile, time, urllib.request, urllib.error

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PORT = 8791
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
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, r.read().decode("utf-8", "replace"), r.headers
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), e.headers

def partie(eleve="Les Lynx", jeu="melanges", debut="2026-11-13T09:00", score=100, **extra):
    r = {"type": "escape-game-compte-rendu", "version": 1, "jeu": jeu, "titre": "Le Laboratoire", "eleve": eleve, "mode": "equipe",
         "niveau": "CM2", "date": debut, "partie": debut, "termine": True, "dureeMin": 41.5, "score": score, "scoreMax": 125,
         "enigmes": 20, "total": 20, "premierCoup": 15, "erreurs": 3, "indices": 1, "code": "AAAA-BBBB"}
    r.update(extra)
    return r

def demarrer(dossier):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("ESCAPE_DONNEES", None)
    p = subprocess.Popen([sys.executable, os.path.join(dossier, "serveur.py"), str(PORT)], cwd=tempfile.gettempdir(), env=env,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(50):
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

projet = tempfile.mkdtemp(prefix="eg-test-")
donnees = tempfile.mkdtemp(prefix="eg-donnees-")
try:
    shutil.copyfile(os.path.join(RACINE, "serveur.py"), os.path.join(projet, "serveur.py"))
    open(os.path.join(projet, "index.html"), "w").write("<p>accueil</p>")
    fichier = os.path.join(projet, "resultats-classe.jsonl")
    print("\n== Résultats : enregistrement automatique (serveur lancé depuis un AUTRE dossier courant) ==")
    p = demarrer(projet)
    try:
        c, t, _ = requete("/api/resultat", partie())
        d = json.loads(t)
        ok(c == 200 and d["ok"] and d["ajoutees"] == 1 and d["total"] == 1, "une partie envoyée par un élève est enregistrée : " + t)
        ok(os.path.exists(fichier), "le fichier est créé dans le dossier du projet, pas dans le dossier courant")
        d = json.loads(requete("/api/resultat", partie())[1])
        ok(d["ok"] and d["ajoutees"] == 0 and d["total"] == 1, "même partie renvoyée : aucun doublon")
        d = json.loads(requete("/api/resultat", partie(score=110, quiz=4))[1])
        ok(d["ajoutees"] == 1 and d["total"] == 1, "partie complétée (même clé) : mise à jour, toujours 1 partie")
        ok(not json.loads(requete("/api/resultat", {"type": "autre"})[1])["ok"], "donnée qui n'est pas un compte-rendu : refusée")
        ok(not json.loads(requete("/api/resultat", {"type": "escape-game-compte-rendu", "jeu": 5, "eleve": []})[1])["ok"], "compte-rendu mal formé : refusé")
        lot = [partie("Tom", debut="2026-11-13T10:00", _source="fichier", _valide=True), partie("=cmd|' /C calc'!A0", debut="2026-11-13T10:05"), {"x": 1}]
        d = json.loads(requete("/api/resultats", {"resultats": lot})[1])
        ok(d["ok"] and d["ajoutees"] == 2 and d["total"] == 3, "import par lot (enseignant) : 2 parties ajoutées, la donnée étrangère ignorée")
        c, t, h = requete("/api/resultats")
        liste = json.loads(t)["resultats"]
        ok(c == 200 and len(liste) == 3 and not any(k.startswith("_") for r in liste for k in r), "lecture : 3 parties, sans marques internes de la page")
        ok(h.get("Access-Control-Allow-Origin") is None and h.get("Cache-Control") == "no-store", "résultats : pas de lecture depuis un autre site, pas de cache")
        info = json.loads(requete("/api/stockage")[1])
        ok(info["nbParties"] == 3 and info["adresseEleves"].startswith("http://") and info["nbCopies"] >= 1, "/api/stockage : 3 parties, adresse élèves, copie de sécurité")
        ok(os.path.exists(os.path.join(projet, "sauvegardes-resultats")), "copie de sécurité du jour créée")
        csvt = open(os.path.join(projet, "resultats-classe.csv"), encoding="utf-8-sig", newline="").read()
        ok(csvt.startswith("Date;Élève / équipe;") and csvt.count("\r\n") == 4, "resultats-classe.csv à jour (en-tête + 3 parties)")
        ok("'=cmd" in csvt and ";=cmd" not in csvt, "CSV : un prénom commençant par « = » ne s'exécute pas dans Excel")
        print("\n== Fichiers privés jamais servis par le réseau ==")
        for ch in ("/resultats-classe.jsonl", "/resultats-classe.csv", "/sauvegardes-resultats/", "/difficulte-classe.json", "/dossier-donnees.txt",
                   "/cle-agnes.txt", "/outils-medias/cle-agnes.txt", "/.git/config", "/Resultats-Classe.JSONL"):
            ok(requete(ch)[0] == 404, "404 pour " + ch)
        ok(requete("/")[0] == 200 and "accueil" in requete("/")[1], "le reste du site est servi normalement")
    finally:
        arreter(p)

    print("\n== Reprise après arrêt, ligne abîmée, arrêt brutal ==")
    with open(fichier, "a", encoding="utf-8") as f:
        f.write("ligne abîmée\n{\"type\": \"escape-game-compte-rendu\", \"jeu\": \"coupé")   # dernière ligne coupée, sans retour
    p = demarrer(projet)
    try:
        liste = json.loads(requete("/api/resultats")[1])["resultats"]
        ok(len(liste) == 3, "après redémarrage et fichier abîmé : les 3 parties sont là (%d)" % len(liste))
        d = json.loads(requete("/api/resultat", partie("Nina", debut="2026-11-13T11:00"))[1])
        ok(d["ajoutees"] == 1 and d["total"] == 4, "nouvelle partie après une ligne coupée : bien enregistrée")
        lignes = [l for l in open(fichier, encoding="utf-8").read().split("\n") if l.strip()]
        valides = 0
        for l in lignes:
            try:
                json.loads(l); valides += 1
            except ValueError:
                pass
        ok(valides == len(lignes) - 2, "la ligne coupée reste isolée : la nouvelle partie n'est pas collée dessus")
    finally:
        arreter(p)

    print("\n== Dossier de données ailleurs (dossier-donnees.txt : ex. dossier Nextcloud) ==")
    open(os.path.join(projet, "dossier-donnees.txt"), "w", encoding="utf-8").write(donnees + "\n")
    p = demarrer(projet)
    try:
        ok(json.loads(requete("/api/resultat", partie("Léo", debut="2026-11-13T12:00"))[1])["ok"], "une partie est enregistrée")
        ok(os.path.exists(os.path.join(donnees, "resultats-classe.jsonl")) and os.path.exists(os.path.join(donnees, "resultats-classe.csv"))
           and os.path.isdir(os.path.join(donnees, "sauvegardes-resultats")), "fichiers, Excel et copies rangés dans le dossier choisi")
        ok(len(json.loads(requete("/api/resultats")[1])["resultats"]) == 1, "le dossier choisi est lu (le projet n'est plus utilisé)")
    finally:
        arreter(p)

    print("\n== Accès réservé à l'ordinateur de l'enseignant ==")
    sys.argv = ["serveur.py", str(PORT)]
    sys.dont_write_bytecode = True
    os.remove(os.path.join(projet, "dossier-donnees.txt"))
    sys.path.insert(0, projet)
    import serveur
    ok(serveur.est_adresse_locale("127.0.0.1") and serveur.est_adresse_locale("::ffff:127.0.0.1"), "127.0.0.1 : enseignant")
    ok(not serveur.est_adresse_locale("192.0.2.77") and not serveur.est_adresse_locale("10.99.99.99"), "un autre appareil du réseau : refusé")
    ok(serveur.chemin_prive("resultats-classe.jsonl") and not serveur.chemin_prive("melanges/index.html"), "liste des fichiers privés")
finally:
    os.chdir(tempfile.gettempdir())
    shutil.rmtree(projet, ignore_errors=True)
    shutil.rmtree(donnees, ignore_errors=True)

print("\n%d vérifications, %d échec(s)" % (verifs, len(echecs)))
sys.exit(1 if echecs else 0)
