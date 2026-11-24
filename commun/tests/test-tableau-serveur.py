#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST DU SERVEUR POUR LE TABLEAU DE BORD (session 2, chantier 3)
Depuis la racine du dépôt :  python commun/tests/test-tableau-serveur.py
Un vrai serveur sur une copie temporaire (dépôt git factice + copie Nextcloud factice) :
  /api/production (état des jeux, recalculé en direct), /api/installations (ce PC, copie Nextcloud,
  fiche du PC de l'école remontée par Nextcloud), fiche installations/<machine>.json jamais servie,
  /api/sante (5e voyant : sauvegarde), /api/mettre-a-jour (PC principal : copie Nextcloud, journal),
  repère « PC de l'école » (installer-ecole.bat) reconnu.
"""
import json, os, shutil, subprocess, sys, tempfile, time, urllib.request, urllib.error

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PORT = 8797
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
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def git(d, *a):
    env = dict(os.environ, GIT_AUTHOR_NAME="T", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="T", GIT_COMMITTER_EMAIL="t@t")
    return subprocess.run(["git", "-c", "init.defaultBranch=escape-games"] + list(a), cwd=d, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).returncode


def preparer(tmp):
    d = os.path.join(tmp, "PROJET ESCAPE GAMES")
    for f in ("serveur.py", "index.html", "outils-docs/etat-production.py", "outils-ecole/ecole.py", "commun/donnees/catalogue.js"):
        os.makedirs(os.path.dirname(os.path.join(d, f)), exist_ok=True)
        shutil.copy(os.path.join(RACINE, f), os.path.join(d, f))
    # un jeu factice complet du catalogue : lumiere
    os.makedirs(os.path.join(d, "immersifs", "lumiere", "assets", "data"))
    with open(os.path.join(d, "immersifs", "lumiere", "index.html"), "w") as f:
        f.write("<p>jeu</p>")
    with open(os.path.join(d, "immersifs", "lumiere", "assets", "data", "enigmes.json"), "w") as f:
        json.dump({"niveaux": [{"id": g} for g in "abcde"]}, f)
    with open(os.path.join(d, "immersifs", "lumiere", "medias.csv"), "w", encoding="utf-8") as f:
        f.write("fichier;type\nassets/images/decors/a.webp;decor\nassets/videos/t.mp4;video\n")
    os.makedirs(os.path.join(d, "lumiere"))
    with open(os.path.join(d, "lumiere", "A-VERIFIER.md"), "w", encoding="utf-8") as f:
        f.write("# À vérifier\n\n1. **Date du phare** : à relire.\n2. ~~Réglé~~\n- [x] fait\n- **Chiffre** du BO\n")
    with open(os.path.join(d, "version.json"), "w") as f:
        json.dump({"numero": 42, "date": "2026-11-24T10:00:00+0100", "branche": "escape-games", "commit_precedent": "x"}, f)
    git(d, "init", "-q")
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "depart")
    # copie Nextcloud factice, avec la fiche du PC de l'école remontée par Nextcloud
    nc = os.path.join(tmp, "Nextcloud", "copie")
    os.makedirs(os.path.join(nc, "installations"))
    with open(os.path.join(nc, "index.html"), "w") as f:
        f.write("ancien")
    with open(os.path.join(nc, "serveur.py"), "w") as f:
        f.write("# ancien")
    with open(os.path.join(nc, "version.json"), "w") as f:
        json.dump({"numero": 40, "date": "2026-11-22T10:00:00+0100"}, f)
    with open(os.path.join(nc, "installations", "PC-ECOLE.json"), "w") as f:
        json.dump({"machine": "PC-ECOLE", "role": "ecole", "ecole": True, "nextcloud": True, "numero": 39, "vu": "2026-11-23T08:30"}, f)
    with open(os.path.join(d, "outils-ecole", "dossier-nextcloud.txt"), "w", encoding="utf-8") as f:
        f.write(nc + "\n")
    return d, nc


def demarrer(d, env_sup=None):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", ESCAPE_DONNEES=os.path.join(os.path.dirname(d), "donnees"))
    env.pop("APPDATA", None)
    env.update(env_sup or {})
    p = subprocess.Popen([sys.executable, os.path.join(d, "serveur.py"), str(PORT)], cwd=tempfile.gettempdir(), env=env,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(100):
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
        p.wait(timeout=10)
    except subprocess.TimeoutExpired:
        p.kill()


def main():
    tmp = tempfile.mkdtemp(prefix="test-tdb-")
    try:
        d, nc = preparer(tmp)
        p = demarrer(d)
        try:
            print("\n== /api/production ==")
            c, t = requete("/api/production")
            P = json.loads(t) if c == 200 else {}
            ok(c == 200 and P.get("ok") and P.get("direct"), "état de production calculé en direct")
            lum = next((j for j in P.get("jeux", []) if j["id"] == "lumiere"), {})
            ok(lum.get("grades") == 5 and lum.get("medias", {}).get("images") == 1 and lum.get("medias", {}).get("videos") == 1, "lumiere : 5 grades, 1 image et 1 vidéo manquantes")
            ok(lum.get("a_verifier") == 2 and lum.get("points", [])[:1] == ["Date du phare"], "A-VERIFIER : 2 points ouverts (barrés et cochés ignorés)")
            ok(lum.get("etat") == "en-cours" and "voix" in lum.get("manque", []), "pas fini : il manque la voix, les leçons...")
            ok(any(x["jeu"] == "traite-colonies" and x["priorite"] == 1 for x in P.get("a_relire", [])), "file « À relire » : jeux sensibles en tête")
            print("\n== /api/installations ==")
            c, t = requete("/api/installations")
            I = json.loads(t) if c == 200 else {}
            ok(c == 200 and I.get("ici", {}).get("role") == "principal" and I["ici"].get("numero") == 42, "ce PC : PC principal (dépôt git), version n° 42")
            ok((I.get("nextcloud") or {}).get("existe") and I["nextcloud"]["version"].get("numero") == 40, "copie Nextcloud trouvée (dossier-nextcloud.txt), version n° 40")
            ok(any(f.get("machine") == "PC-ECOLE" and f.get("ecole") and f.get("numero") == 39 for f in I.get("fiches", [])), "fiche du PC de l'école remontée par Nextcloud (n° 39)")
            fiches = os.listdir(os.path.join(d, "installations")) if os.path.isdir(os.path.join(d, "installations")) else []
            ok(len(fiches) == 1 and fiches[0].endswith(".json"), "fiche de ce PC écrite dans installations/")
            ok(requete("/installations/" + (fiches[0] if fiches else "x.json"))[0] == 404, "installations/ jamais servi par le réseau")
            print("\n== /api/sante : sauvegarde ==")
            c, t = requete("/api/sante")
            v = {x["id"]: x for x in json.loads(t).get("voyants", [])} if c == 200 else {}
            ok("sauvegarde" in v and v["sauvegarde"]["etat"] in ("vert", "orange") and v["sauvegarde"]["message"], "5e voyant : sauvegarde (" + v.get("sauvegarde", {}).get("message", "")[:60] + "…)")
            print("\n== /api/mettre-a-jour (PC principal → copie Nextcloud) ==")
            c, t = requete("/api/mettre-a-jour", {})
            ok(c == 200 and json.loads(t).get("en_cours") is True, "mise à jour lancée (POST)")
            M = {}
            for _ in range(150):
                M = json.loads(requete("/api/mettre-a-jour")[1])
                if not M.get("en_cours"):
                    break
                time.sleep(0.2)
            texte = "\n".join(M.get("lignes", []))
            ok(M.get("en_cours") is False and M.get("ok") is True, "mise à jour terminée sans erreur")
            ok("Copie Nextcloud :" in texte and "git push origin escape-games" in texte, "journal : copie Nextcloud faite, commande de publication donnée (jamais lancée)")
            with open(os.path.join(nc, "index.html"), encoding="utf-8") as f:
                ok(f.read() != "ancien", "la copie Nextcloud a reçu la version commitée")
            ok(os.path.exists(os.path.join(nc, "installations", "PC-ECOLE.json")), "la fiche du PC de l'école n'est pas touchée par la copie")
        finally:
            arreter(p)
        print("\n== PC de l'école (repère d'installer-ecole.bat) ==")
        appdata = os.path.join(tmp, "AppData")
        os.makedirs(os.path.join(appdata, "EscapeGames"))
        with open(os.path.join(appdata, "EscapeGames", "poste-ecole.txt"), "w") as f:
            f.write("PC de l'ecole")
        p = demarrer(d, {"APPDATA": appdata})
        try:
            I = json.loads(requete("/api/installations")[1])
            ok(I["ici"]["role"] == "ecole" and I["ici"]["ecole"] is True and I.get("nextcloud") is None, "repère trouvé : ce PC est le PC de l'école")
        finally:
            arreter(p)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("\nTableau de bord (serveur) : {} vérifications, {} échec(s).".format(verifs, len(echecs)))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
