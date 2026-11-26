#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST DU SERVEUR — PARTIES EN COURS (Mission géo, session 4)
Depuis la racine du dépôt :  python commun/tests/test-parties-serveur.py
Un vrai serveur sur une copie temporaire : /api/parties (écriture, fusion sans perte, historique,
remplacement, liste, reprise), refus des données illisibles, dossier parties/ jamais servi.
"""
import json, os, shutil, subprocess, sys, tempfile, time, urllib.request, urllib.error

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PORT = 8798
verifs, echecs = 0, []


def ok(cond, msg):
    global verifs
    verifs += 1
    print(("  ✓ " if cond else "  ✗ ") + msg)
    if not cond:
        echecs.append(msg)


def requete(chemin, corps=None):
    req = urllib.request.Request("http://127.0.0.1:%d%s" % (PORT, chemin), data=None if corps is None else json.dumps(corps).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status, json.loads(r.read().decode("utf-8") or "null")
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode("utf-8") or "null")
        except ValueError:
            return e.code, None


def partie(equipe, seances, indices=None):
    return {"format": "mission-geo-partie", "version": 2, "equipe": equipe, "niveau": "CM1", "grade": "matelot",
            "seances": {str(n): {"id": "s%02d" % n, "numero": n, "reussie": r, "points": p, "date": "2026-11-%02dT10:00:00.000Z" % (10 + n)}
                        for n, (r, p) in seances.items()},
            "indices": indices or [], "final": {"resolu": False}, "debut": "2026-09-08T09:00:00.000Z"}


def main():
    tmp = tempfile.mkdtemp(prefix="test-parties-")
    d = os.path.join(tmp, "jeux")
    os.makedirs(d)
    for f in ("serveur.py", "index.html"):
        shutil.copy(os.path.join(RACINE, f), os.path.join(d, f))
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("ESCAPE_DONNEES", None)
    p = subprocess.Popen([sys.executable, os.path.join(d, "serveur.py"), str(PORT)], cwd=tmp, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(100):
            try:
                if requete("/api/info")[0] == 200:
                    break
            except Exception:
                time.sleep(0.1)
        print("\n== /api/parties ==")
        c, r = requete("/api/parties?jeu=mission-geo")
        ok(c == 200 and r["ok"] and r["parties"] == [], "liste vide au départ")
        c, r = requete("/api/parties", {"jeu": "mission-geo", "partie": partie("Les Lynx de Léa", {1: (True, 18), 2: (True, 15), 3: (False, 6)},
                                                                              [{"session": "s01", "numero": 1, "type": "nombre", "valeur": 5}])})
        ok(c == 200 and r["ok"] and r["ajoutees"] == [1, 2] and r["resume"]["slug"] == "les-lynx-de-lea", "nouvelle équipe enregistrée (séances 1 et 2)")
        fichier = os.path.join(d, "parties", "mission-geo", "les-lynx-de-lea.json")
        ok(os.path.exists(fichier), "rangée dans parties/mission-geo/ du dossier des résultats")
        c, r = requete("/api/parties", {"jeu": "mission-geo", "partie": partie("Les Lynx de Léa", {1: (False, 4), 3: (True, 14)},
                                                                              [{"session": "s03", "numero": 3, "type": "nombre", "valeur": 7}])})
        ok(c == 200 and r["ajoutees"] == [3], "fusion : seule la séance 3 est nouvelle")
        with open(fichier, encoding="utf-8") as f:
            x = json.load(f)
        ok(x["seances"]["1"]["reussie"] and x["seances"]["1"]["points"] == 18 and x["seances"]["3"]["reussie"] and len(x["indices"]) == 2,
           "fusion sans perte : séance 1 toujours réussie (18 points), indices réunis")
        hist = os.listdir(os.path.join(d, "parties", "mission-geo", "_historique"))
        ok(len(hist) == 1 and hist[0].startswith("les-lynx-de-lea-"), "état précédent gardé dans _historique/")
        c, r = requete("/api/parties", {"jeu": "mission-geo", "partie": partie("Les Lynx de Léa", {1: (False, 4), 3: (True, 14)})})
        ok(c == 200 and r["message"] == "déjà à jour" and len(os.listdir(os.path.join(d, "parties", "mission-geo", "_historique"))) == 1, "rien de nouveau : pas de réécriture inutile")
        c, r = requete("/api/parties", {"jeu": "mission-geo", "mode": "remplacer", "partie": partie("Les Lynx de Léa", {1: (True, 20)})})
        ok(c == 200 and r["ok"] and r["resume"]["reussies"] == [1], "remplacement possible depuis le PC de l'enseignant")
        c, r = requete("/api/parties?jeu=mission-geo&equipe=Les%20Lynx%20de%20L%C3%A9a")
        ok(c == 200 and r["partie"]["seances"]["1"]["points"] == 20, "reprise d'une équipe par son nom")
        requete("/api/parties", {"jeu": "mission-geo", "partie": partie("Les Hiboux", {1: (True, 10)})})
        c, r = requete("/api/parties?jeu=mission-geo")
        ok(c == 200 and [x["equipe"] for x in r["parties"]] == ["Les Hiboux", "Les Lynx de Léa"] and r["local"] is True, "liste des équipes (pour « Reprendre depuis le PC »)")
        print("\n== Refus ==")
        ok(requete("/api/parties", {"jeu": "mission-geo", "partie": {"equipe": "X"}})[0] == 400, "partie illisible : refusée (400)")
        ok(requete("/api/parties", {"jeu": "mission-geo", "partie": partie("", {1: (True, 1)})})[0] == 400, "sans nom d'équipe : refusée")
        ok(requete("/api/parties", {"jeu": "mission-geo", "partie": partie("Y", {17: (True, 1)})})[0] == 400, "séance hors 1-16 : refusée")
        ok(requete("/api/parties?jeu=autre")[0] == 400, "jeu inconnu : refusé")
        ok(requete("/api/parties?jeu=mission-geo&equipe=personne")[0] == 404, "équipe inconnue : 404")
        try:
            with urllib.request.urlopen("http://127.0.0.1:%d/parties/mission-geo/les-lynx-de-lea.json" % PORT, timeout=10) as rr:
                code = rr.status
        except urllib.error.HTTPError as e:
            code = e.code
        ok(code == 404, "dossier parties/ jamais servi en fichier")
    finally:
        p.terminate()
        try:
            p.wait(timeout=10)
        except subprocess.TimeoutExpired:
            p.kill()
        shutil.rmtree(tmp, ignore_errors=True)
    print("\nParties en cours (serveur) : {} vérifications, {} échec(s).".format(verifs, len(echecs)))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
