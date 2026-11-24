#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST DES OUTILS DE DISTRIBUTION (chantier « distribution » : outils-ecole/ecole.py, version.json, serveur.py)
Depuis la racine du dépôt :  python commun/tests/test-ecole-outils.py
Tout se passe dans des dossiers temporaires (dépôts git factices) :
  1. crochet pre-commit : version.json écrit et commité, numéro qui monte, commit précédent ;
  2. copie Nextcloud : version commitée seulement, CRLF des .bat, fichiers de la classe jamais touchés,
     fichiers obsolètes rangés (jamais effacés), deuxième passage sans rien recopier, garde-fous ;
  3. lecture de « netstat -ano » (anglais et français) ;
  4. diagnostic.txt : sections attendues, AUCUN prénom d'élève ;
  5. vérifications avant lancement ;
  6. serveur : /api/version, fichiers privés jamais servis, port déjà pris = refus net,
     arrêt propre par « ecole.py liberer-port » (l'ancien serveur ne reste plus en place).
"""
import importlib.util, json, os, shutil, socket, subprocess, sys, tempfile, time, urllib.request, urllib.error

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ECOLE = os.path.join(RACINE, "outils-ecole", "ecole.py")
PORT = 8796
verifs, echecs = 0, []


def ok(cond, msg):
    global verifs
    verifs += 1
    print(("  ✓ " if cond else "  ✗ ") + msg)
    if not cond:
        echecs.append(msg)


def charger():
    spec = importlib.util.spec_from_file_location("ecole", ECOLE)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def git(depot, *args, env=None):
    e = dict(os.environ, GIT_AUTHOR_NAME="Test", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="Test", GIT_COMMITTER_EMAIL="t@t")
    e.update(env or {})
    r = subprocess.run(["git", "-c", "init.defaultBranch=escape-games", "-c", "core.autocrlf=false"] + list(args),
                       cwd=depot, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=e)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def ecrire(chemin, contenu, mode="w"):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, mode, **({} if "b" in mode else {"encoding": "utf-8", "newline": ""})) as f:
        f.write(contenu)


def lire(chemin, mode="r"):
    with open(chemin, mode, **({} if "b" in mode else {"encoding": "utf-8-sig"})) as f:
        return f.read()


def depot_factice(tmp, crochet=True):
    d = os.path.join(tmp, "depot")
    os.makedirs(d)
    git(d, "init", "-q")
    if crochet:
        os.makedirs(os.path.join(d, "outils-tests", "hooks"))
        shutil.copy(os.path.join(RACINE, "outils-tests", "hooks", "pre-commit"), os.path.join(d, "outils-tests", "hooks", "pre-commit"))
        os.chmod(os.path.join(d, "outils-tests", "hooks", "pre-commit"), 0o755)
        git(d, "config", "core.hooksPath", "outils-tests/hooks")
    ecrire(os.path.join(d, ".gitattributes"), "* text=auto eol=lf\n*.bat text eol=crlf\n*.png binary\n")
    ecrire(os.path.join(d, "index.html"), "<!doctype html><title>Accueil</title>\n")
    ecrire(os.path.join(d, "serveur.py"), "# serveur factice\n")
    ecrire(os.path.join(d, "lancer.bat"), "@echo off\r\necho bonjour\r\n")
    ecrire(os.path.join(d, "immersifs", "jeu-a", "index.html"), "<p>jeu A</p>\n")
    ecrire(os.path.join(d, "immersifs", "jeu-a", "cle-finale.webp"), b"RIFF\x00\x01\x02binaire", "wb")
    ecrire(os.path.join(d, "dossier avec espaces", "page.html"), "<p>espaces</p>\n")
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "premier")
    return d


def test_crochet(tmp):
    print("\n== 1. Crochet pre-commit : version.json ==")
    d = depot_factice(tmp)
    code, sortie = git(d, "show", "HEAD:version.json")
    ok(code == 0, "version.json est dans le premier commit")
    v1 = json.loads(sortie) if code == 0 else {}
    ok(v1.get("numero") == 1, "numéro 1 au premier commit")
    ok(v1.get("branche") == "escape-games", "branche notée")
    ok(len(str(v1.get("date", ""))) >= 19 and str(v1["date"])[4] == "-", "date au format AAAA-MM-JJTHH:MM:SS")
    premier = git(d, "rev-parse", "--short=12", "HEAD")[1].strip()
    ecrire(os.path.join(d, "index.html"), "<!doctype html><title>Accueil v2</title>\n")
    git(d, "add", "index.html")
    git(d, "commit", "-q", "-m", "deuxieme")
    v2 = json.loads(git(d, "show", "HEAD:version.json")[1])
    ok(v2.get("numero") == 2, "numéro 2 au deuxième commit")
    ok(v2.get("commit_precedent") == premier, "commit_precedent = le commit d'avant")
    ok(git(d, "status", "--porcelain")[1].strip() == "", "rien ne reste à commiter après le commit")
    git(d, "commit", "-q", "--allow-empty", "-m", "sans version", env={"ESCAPE_SANS_VERSION": "1"})
    v3 = json.loads(git(d, "show", "HEAD:version.json")[1])
    ok(v3.get("numero") == 2, "ESCAPE_SANS_VERSION=1 : version.json laissé tel quel")
    return d


def test_nextcloud(tmp, E):
    print("\n== 2. Copie Nextcloud ==")
    d = depot_factice(os.path.join(tmp, "nc"))
    dest = os.path.join(tmp, "nc", "Nextcloud", "Escape games", "copie")
    # Une ancienne copie : jeux anciens + fichiers de la classe
    ecrire(os.path.join(dest, "index.html"), "<p>ancien accueil</p>\n")
    ecrire(os.path.join(dest, "serveur.py"), "# ancien serveur\n")
    ecrire(os.path.join(dest, "ancien-jeu", "index.html"), "<p>jeu supprimé du dépôt</p>\n")
    ecrire(os.path.join(dest, "resultats-classe.jsonl"), '{"eleve":"Zoé","jeu":"x"}\n')
    ecrire(os.path.join(dest, "resultats-classe.csv"), "eleve\nZoé\n")
    ecrire(os.path.join(dest, "sauvegardes-resultats", "2026-11-20.jsonl"), '{"eleve":"Zoé"}\n')
    ecrire(os.path.join(dest, "dossier-donnees.txt"), "D:\\classe\n")
    ecrire(os.path.join(dest, "journal-ecole.txt"), "journal\n")
    ecrire(os.path.join(dest, "immersifs", "jeu-a", "index.html"), "<p>jeu A</p>\r\n")   # identique, CRLF
    ecrire(os.path.join(dest, ".sync_4f2a.db"), b"base du client Nextcloud", "wb")
    ecrire(os.path.join(dest, ".nextcloudsync.log"), "journal du client\n")
    # Travail non commité : ne doit pas partir
    ecrire(os.path.join(d, "brouillon.html"), "<p>pas commité</p>\n")
    ecrire(os.path.join(d, "index.html"), "<p>modifié mais pas commité</p>\n")
    avant = {p: lire(os.path.join(dest, p), "rb") for p in (".sync_4f2a.db", ".nextcloudsync.log", "resultats-classe.jsonl", "resultats-classe.csv",
                                                             "sauvegardes-resultats/2026-11-20.jsonl", "dossier-donnees.txt", "journal-ecole.txt")}
    journal = []
    c = E.synchroniser(d, dest, essai=True, journal=journal.append)
    ok(c["ecrits"] >= 4 and c["deplaces"] == 1, "essai : fichiers à copier et à ranger comptés ({ecrits}, {deplaces})".format(**c))
    ok(lire(os.path.join(dest, "index.html")) == "<p>ancien accueil</p>\n", "essai : rien n'est modifié")
    c = E.synchroniser(d, dest, journal=journal.append)
    ok(c["ecrits"] >= 4, "copie : {} fichiers écrits".format(c["ecrits"]))
    ok(c["identiques"] >= 1, "copie : le fichier déjà identique (CRLF) n'est pas recopié")
    ok(lire(os.path.join(dest, "index.html")) == "<!doctype html><title>Accueil</title>\n", "copie : version COMMITÉE (pas les modifications locales)")
    ok(not os.path.exists(os.path.join(dest, "brouillon.html")), "copie : fichier non commité jamais copié")
    ok(lire(os.path.join(dest, "lancer.bat"), "rb") == b"@echo off\r\necho bonjour\r\n", "copie : .bat écrit avec des fins de ligne CRLF")
    ok(lire(os.path.join(dest, "immersifs", "jeu-a", "cle-finale.webp"), "rb") == b"RIFF\x00\x01\x02binaire", "copie : fichier binaire intact (cle-*.webp n'est pas une clé)")
    ok(os.path.exists(os.path.join(dest, "dossier avec espaces", "page.html")), "copie : dossier avec espaces")
    ok(os.path.exists(os.path.join(dest, "version.json")), "copie : version.json présent")
    for p, contenu in avant.items():
        ok(lire(os.path.join(dest, *p.split("/")), "rb") == contenu, "fichier de la classe intact : " + p)
    rangement = os.path.join(dest, "_a-supprimer")
    ranges = [os.path.join(r, f) for r, _, fs in os.walk(rangement) for f in fs]
    ok(not os.path.exists(os.path.join(dest, "ancien-jeu", "index.html")) and any(x.endswith(os.path.join("ancien-jeu", "index.html")) for x in ranges),
       "fichier supprimé du dépôt : rangé dans _a-supprimer, pas effacé")
    ok(os.path.exists(os.path.join(dest, E.MARQUEUR_NEXTCLOUD)) and os.path.exists(os.path.join(dest, E.MANIFESTE)), "marqueur copie-nextcloud.txt et manifeste écrits")
    c = E.synchroniser(d, dest, journal=journal.append)
    ok(c["ecrits"] == 0 and c["deplaces"] == 0, "deuxième passage : rien à recopier ni à ranger")
    git(d, "checkout", "-q", "--", "index.html")
    ecrire(os.path.join(d, "immersifs", "jeu-a", "index.html"), "<p>jeu A v2</p>\n")
    git(d, "add", "immersifs/jeu-a/index.html")
    git(d, "commit", "-q", "-m", "v2")
    c = E.synchroniser(d, dest, journal=journal.append)
    ok(c["ecrits"] == 2, "après un commit : seuls les fichiers changés sont copiés (jeu + version.json) : {}".format(c["ecrits"]))
    ok(lire(os.path.join(dest, "immersifs", "jeu-a", "index.html")) == "<p>jeu A v2</p>\n", "nouvelle version copiée")
    # Garde-fous
    inconnu = os.path.join(tmp, "nc", "Mes documents")
    ecrire(os.path.join(inconnu, "lettre.docx"), b"PK", "wb")
    try:
        E.synchroniser(d, inconnu)
        ok(False, "refus d'un dossier qui n'est pas une copie des jeux")
    except RuntimeError:
        ok(os.listdir(inconnu) == ["lettre.docx"], "refus d'un dossier qui n'est pas une copie des jeux (rien touché)")
    try:
        E.synchroniser(d, os.path.join(d, "copie"))
        ok(False, "refus d'une copie DANS le dépôt")
    except RuntimeError:
        ok(True, "refus d'une copie DANS le dépôt")
    for chemin, attendu in (("resultats-classe.jsonl", True), ("sauvegardes-resultats/a.jsonl", True), ("outils-medias/cle-agnes.txt", True),
                            ("immersifs/x/assets/cle-or.png", False), ("journal-ecole.txt", True), ("x/_a-supprimer/y.html", True),
                            ("immersifs/jeu/index.html", False), ("seance-du-jour.json", True), ("journal.html", False)):
        ok(E.est_protege(chemin) == attendu, "est_protege({}) = {}".format(chemin, attendu))


def test_netstat(E):
    print("\n== 3. Lecture de netstat -ano ==")
    anglais = """
Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       1032
  TCP    0.0.0.0:8000           0.0.0.0:0              LISTENING       4242
  TCP    0.0.0.0:8000           0.0.0.0:0              LISTENING       5151
  TCP    127.0.0.1:8000         127.0.0.1:50122        ESTABLISHED     4242
  TCP    0.0.0.0:18000          0.0.0.0:0              LISTENING       777
  TCP    [::]:8000              [::]:0                 LISTENING       4242
"""
    ok(E.pids_a_l_ecoute(anglais, 8000) == ["4242", "5151"], "deux serveurs à l'écoute sur 8000 trouvés (pas 18000, pas les connexions)")
    francais = "  TCP    0.0.0.0:8000           0.0.0.0:0              ÉCOUTE          3030\n"
    ok(E.pids_a_l_ecoute(francais, 8000) == ["3030"], "Windows en français (ÉCOUTE)")
    ok(E.pids_a_l_ecoute(anglais, 9000) == [], "port libre : aucun PID")
    ok(E.est_python("python.exe") and E.est_python("py.exe") and E.est_python("python3.12.exe") and not E.est_python("chrome.exe"),
       "reconnaît Python, jamais un autre programme")
    ok(E.date_courte("2026-11-23T21:40:05+0100") == "23/11/2026 à 21h40", "date affichée à la française")


def copie_serveur(tmp):
    d = os.path.join(tmp, "jeux avec espaces")
    os.makedirs(os.path.join(d, "outils-ecole"))
    os.makedirs(os.path.join(d, "immersifs", "jeu-a"))
    for f in ("serveur.py", "index.html"):
        shutil.copy(os.path.join(RACINE, f), os.path.join(d, f))
    shutil.copy(ECOLE, os.path.join(d, "outils-ecole", "ecole.py"))
    ecrire(os.path.join(d, "version.json"), json.dumps({"numero": 321, "date": "2026-11-23T21:40:05+0100", "branche": "escape-games", "commit_precedent": "abc"}))
    ecrire(os.path.join(d, "diagnostic.txt"), "privé\n")
    ecrire(os.path.join(d, "copie-nextcloud.txt"), "copie\n")
    return d


def lancer_ecole(d, *args, timeout=60):
    env = dict(os.environ, ESCAPE_HORS_LIGNE="1", PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([sys.executable, os.path.join(d, "outils-ecole", "ecole.py")] + list(args), cwd=tempfile.gettempdir(),
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env, timeout=timeout)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def test_diagnostic_verifier(tmp):
    print("\n== 4-5. Diagnostic et vérifications ==")
    d = copie_serveur(os.path.join(tmp, "diag"))
    ecrire(os.path.join(d, "resultats-classe.jsonl"), '{"eleve":"Zoé Martin","jeu":"x"}\n{"eleve":"Léo","jeu":"y"}\n')
    ecrire(os.path.join(d, "journal-ecole.txt"), "==== ouverture de session\nServeur lancé.\n")
    code, sortie = lancer_ecole(d, "diagnostic", "--port", str(PORT + 1))
    ok(code == 0, "diagnostic : se termine sans erreur")
    texte = lire(os.path.join(d, "diagnostic.txt"))
    for attendu in ("== Version ==", "\"numero\": 321", "== Logiciels ==", "Python :", "== Dépôt git ==", "immersifs/ : 1 jeux",
                    "Parties enregistrées : 2", "Port {} : libre".format(PORT + 1), "Serveur des jeux : ne répond pas",
                    "Copie Nextcloud : oui", "Serveur lancé."):
        ok(attendu in texte, "diagnostic contient « {} »".format(attendu))
    ok("Zoé" not in texte and "Léo" not in texte, "diagnostic : AUCUN prénom d'élève")
    ok("\r\n" in lire(os.path.join(d, "diagnostic.txt"), "rb").decode("utf-8-sig"), "diagnostic : fins de ligne Windows (Bloc-notes)")
    code, sortie = lancer_ecole(d, "verifier")
    ok(code == 0, "verifier : dossier complet → OK")
    code, sortie = lancer_ecole(d, "infos", "--port", "8000")
    ok(code == 0 and "n° 321 du 23/11/2026" in sortie and ":8000/" in sortie, "infos : version et adresse des élèves affichées")
    os.remove(os.path.join(d, "index.html"))
    shutil.rmtree(os.path.join(d, "immersifs"))
    code, sortie = lancer_ecole(d, "verifier")
    ok(code == 1 and "index.html est introuvable" in sortie and "immersifs" in sortie, "verifier : copie incomplète → bloquant, message en français")


def requete(chemin, corps=None, timeout=10):
    req = urllib.request.Request("http://127.0.0.1:%d%s" % (PORT, chemin), data=None if corps is None else json.dumps(corps).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def demarrer(d, donnees):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", ESCAPE_DONNEES=donnees)
    p = subprocess.Popen([sys.executable, os.path.join(d, "serveur.py"), str(PORT)], cwd=tempfile.gettempdir(), env=env,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for _ in range(100):
        try:
            if requete("/api/info", timeout=2)[0] == 200:
                return p
        except Exception:
            time.sleep(0.1)
        if p.poll() is not None:
            break
    return p


def test_serveur(tmp):
    print("\n== 6. Serveur : version, fichiers privés, port, arrêt propre ==")
    d = copie_serveur(os.path.join(tmp, "srv"))
    donnees = os.path.join(tmp, "srv", "donnees")
    p = demarrer(d, donnees)
    try:
        code, corps = requete("/api/version")
        v = json.loads(corps) if code == 200 else {}
        ok(code == 200 and v.get("numero") == 321 and v.get("texte") == "n° 321 du 23/11/2026", "/api/version : numéro et date")
        ok(v.get("nextcloud") is True, "/api/version : copie Nextcloud reconnue")
        ok(requete("/version.json")[0] == 200, "version.json servi (lu par le tableau de bord et le site)")
        for prive in ("/diagnostic.txt", "/copie-nextcloud.txt"):
            ok(requete(prive)[0] == 404, prive + " jamais servi")
        # Un second serveur sur le même port doit échouer franchement (plus de double serveur)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", ESCAPE_DONNEES=donnees)
        r = subprocess.run([sys.executable, os.path.join(d, "serveur.py"), str(PORT)], cwd=tempfile.gettempdir(), env=env,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30)
        sortie = r.stdout.decode("utf-8", "replace")
        ok(r.returncode == 3 and "déjà utilisé" in sortie, "second serveur sur le même port : refus net (code 3, message en français)")
        code, sortie = lancer_ecole(d, "liberer-port", "--port", str(PORT))
        ok(code == 0 and "fermé" in sortie, "liberer-port : l'ancien serveur des jeux est fermé")
        try:
            p.wait(timeout=10)
        except subprocess.TimeoutExpired:
            pass
        ok(p.poll() == 0, "ancien serveur arrêté proprement (code 0 : sa fenêtre se ferme)")
        s = socket.socket()
        libre = s.connect_ex(("127.0.0.1", PORT)) != 0
        s.close()
        ok(libre, "port libéré")
        code, sortie = lancer_ecole(d, "liberer-port", "--port", str(PORT))
        ok(code == 0 and "libre" in sortie, "liberer-port sur un port libre : rien à faire")
    finally:
        if p.poll() is None:
            p.kill()
            p.wait()


def main():
    E = charger()
    tmp = tempfile.mkdtemp(prefix="test-ecole-")
    try:
        test_crochet(os.path.join(tmp, "c"))
        test_nextcloud(tmp, E)
        test_netstat(E)
        test_diagnostic_verifier(tmp)
        test_serveur(tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("\n  {} vérifications, {} échec(s)".format(verifs, len(echecs)))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
