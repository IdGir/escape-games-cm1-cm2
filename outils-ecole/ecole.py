#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================
 OUTILS D'INSTALLATION ET DE MISE À JOUR (chantier « distribution »)
 Appelés par les scripts à double-cliquer ; aucune dépendance, Python 3.6+.

   python outils-ecole/ecole.py infos [--port 8000]
        Affiche la version installée et l'adresse à donner aux élèves.
   python outils-ecole/ecole.py verifier [--port 8000]
        Contrôles avant de lancer le serveur (droits d'écriture, dossiers) ; code 1 si bloquant.
   python outils-ecole/ecole.py liberer-port [--port 8000]
        Arrête proprement l'ancien serveur des jeux qui occupe le port (code 0),
        code 2 si le port est pris par un AUTRE programme (rien n'est arrêté).
   python outils-ecole/ecole.py ouvrir [--port 8000] [page]
        Attend que le serveur réponde puis ouvre la page dans le navigateur.
   python outils-ecole/ecole.py diagnostic [--port 8000]
        Écrit diagnostic.txt (versions, port, dossiers, git, python) : le fichier à envoyer.
   python outils-ecole/ecole.py nextcloud [dossier] [--essai]
        Copie la version commitée du dépôt dans la copie Nextcloud, sans jamais toucher
        aux fichiers de la classe (résultats, sauvegardes, réglages).
   python outils-ecole/ecole.py version
        Affiche une ligne : « n° 412 du 23/11/2026 (commit 1a2b3c4) ».
============================================================
"""
import datetime
import hashlib
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import time
import urllib.request

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT_DEFAUT = 8000
SITE = "https://idgir.github.io/escape-games-cm1-cm2/"

# Fichiers de la classe : jamais copiés, jamais remplacés, jamais déplacés ni effacés.
PROTEGES_NOMS = ("dossier-donnees.txt", "seance-du-jour.json", "version-installee.txt",
                 "diagnostic.txt", "copie-nextcloud.txt", ".copie-escape-games.json",
                 "dossier-nextcloud.txt", "desktop.ini", "thumbs.db", ".ds_store")
PROTEGES_DEBUTS = ("resultats-classe", "difficulte-classe", ".essai-ecriture", ".~lock")
PROTEGES_TXT = ("journal-", "cle-", "cles-")   # journaux et clés d'API : fichiers .txt seulement
PROTEGES_DOSSIERS = ("sauvegardes-resultats", "_a-supprimer", ".git", "node_modules", ".sync")
# Mêmes règles que .gitattributes : ces scripts Windows sont écrits avec des fins de ligne CRLF.
EXT_CRLF = (".bat", ".cmd", ".ps1")
MARQUEUR_NEXTCLOUD = "copie-nextcloud.txt"
MANIFESTE = ".copie-escape-games.json"


def preparer_console():
    for flux in (sys.stdout, sys.stderr):
        try:
            flux.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def lancer(cmd, cwd=RACINE, timeout=20, entree=None):
    """Lance une commande ; renvoie (code, sortie texte). Jamais d'exception (code -1 si introuvable)."""
    try:
        r = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           input=entree, timeout=timeout)
        return r.returncode, r.stdout.decode("utf-8", "replace") if isinstance(r.stdout, bytes) else r.stdout
    except (OSError, subprocess.SubprocessError) as e:
        return -1, str(e)


# ------------------------------------------------------------------ version
def lire_version(dossier=RACINE):
    """Contenu de version.json (dict vide s'il manque ou s'il est abîmé)."""
    try:
        with open(os.path.join(dossier, "version.json"), encoding="utf-8-sig") as f:
            v = json.load(f)
        return v if isinstance(v, dict) else {}
    except (OSError, ValueError):
        return {}


def commit_exact(dossier=RACINE):
    """Commit installé : dépôt git, sinon version-installee.txt (installation par archive), sinon ''."""
    code, sortie = lancer(["git", "rev-parse", "HEAD"], cwd=dossier, timeout=10)
    if code == 0 and re.match(r"^[0-9a-f]{40}$", sortie.strip()):
        return sortie.strip()
    try:
        with open(os.path.join(dossier, "version-installee.txt"), encoding="utf-8") as f:
            return f.readline().strip()
    except OSError:
        return ""


def date_courte(iso):
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}))?", str(iso or ""))
    if not m:
        return ""
    texte = "{}/{}/{}".format(m.group(3), m.group(2), m.group(1))
    return texte + (" à {}h{}".format(m.group(4), m.group(5)) if m.group(4) else "")


def texte_version(dossier=RACINE, avec_commit=True):
    v = lire_version(dossier)
    if not v.get("numero"):
        base = "version inconnue (pas de version.json)"
    else:
        base = "n° {}".format(v["numero"])
        if date_courte(v.get("date")):
            base += " du " + date_courte(v.get("date"))
    if avec_commit:
        c = commit_exact(dossier)
        if c:
            base += " (commit {})".format(c[:7])
    return base


def version_en_ligne(timeout=5):
    """version.json du site GitHub Pages (None si internet ne répond pas ou si le fichier n'est pas encore publié)."""
    if os.environ.get("ESCAPE_HORS_LIGNE"):
        return None
    try:
        req = urllib.request.Request(SITE + "version.json?t={}".format(int(time.time())),
                                     headers={"User-Agent": "escape-games-ecole", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            v = json.loads(r.read(20000).decode("utf-8", "replace"))
        return v if isinstance(v, dict) and v.get("numero") else None
    except Exception:
        return None


# ------------------------------------------------------------------ réseau
def ip_locale():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "127.0.0.1"


def repond(port, chemin="/api/info", timeout=2):
    """Le serveur des jeux répond-il sur ce port ? Renvoie le JSON (dict) ou None."""
    try:
        with urllib.request.urlopen("http://127.0.0.1:{}{}".format(port, chemin), timeout=timeout) as r:
            return json.loads(r.read(200000).decode("utf-8", "replace"))
    except Exception:
        return None


def port_occupe(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        return s.connect_ex(("127.0.0.1", port)) == 0
    finally:
        s.close()


def pids_a_l_ecoute(texte_netstat, port):
    """Lit la sortie de « netstat -ano » (Windows) : PID des programmes À L'ÉCOUTE sur ce port."""
    pids = []
    for ligne in texte_netstat.splitlines():
        champs = ligne.split()
        if len(champs) < 5 or champs[0].upper() != "TCP":
            continue
        local, etat, pid = champs[1], champs[3].upper(), champs[-1]
        if not local.endswith(":{}".format(port)) or etat not in ("LISTENING", "ÉCOUTE", "ECOUTE", "LISTEN"):
            continue
        if pid.isdigit() and pid != "0" and pid not in pids:
            pids.append(pid)
    return pids


def nom_programme(pid):
    """Nom du programme d'un PID (Windows, tasklist) ; '' si inconnu."""
    code, sortie = lancer(["tasklist", "/FI", "PID eq {}".format(pid), "/FO", "CSV", "/NH"], timeout=10)
    if code != 0:
        return ""
    m = re.match(r'^"([^"]+)"', sortie.strip())
    return m.group(1) if m else ""


def est_python(nom):
    nom = (nom or "").lower()
    return nom.startswith("python") or nom in ("py.exe", "pyw.exe", "pythonw.exe")


def liberer_port(port):
    """0 : port libre (ancien serveur arrêté s'il y en avait un) ; 2 : pris par un autre programme ; 1 : échec."""
    if not port_occupe(port):
        print("  Port {} libre : aucun ancien serveur à fermer.".format(port))
        return 0
    if repond(port) is not None:
        print("  Un ancien serveur des jeux tourne déjà sur le port {} : je le ferme.".format(port))
        try:
            req = urllib.request.Request("http://127.0.0.1:{}/api/arreter".format(port), data=b"{}",
                                         headers={"Content-Type": "application/json"})
            urllib.request.urlopen(req, timeout=3).read()
        except Exception:
            pass   # anciennes versions du serveur : pas d'arrêt propre, on passe à taskkill
        for _ in range(30):
            if not port_occupe(port):
                print("  Ancien serveur fermé.")
                return 0
            time.sleep(0.2)
    if os.name != "nt":
        print("  [!] Le port {} est occupé et ce n'est pas un serveur des jeux.".format(port))
        return 2
    code, sortie = lancer(["netstat", "-ano", "-p", "TCP"], timeout=20)
    pids = pids_a_l_ecoute(sortie, port) if code == 0 else []
    autres = []
    for pid in pids:
        nom = nom_programme(pid)
        if est_python(nom):
            c, _ = lancer(["taskkill", "/PID", pid, "/F"], timeout=15)
            print("  Ancien serveur Python (PID {}) {}.".format(pid, "fermé" if c == 0 else "impossible à fermer"))
        else:
            autres.append(nom or "PID " + pid)
    for _ in range(25):
        if not port_occupe(port):
            return 0
        time.sleep(0.2)
    if autres:
        print("  [!] Le port {} est pris par un autre programme : {}.".format(port, ", ".join(autres)))
        print("      Fermez ce programme (ou redémarrez le PC), puis relancez.")
        return 2
    print("  [!] Le port {} est encore occupé. Redémarrez le PC, puis relancez.".format(port))
    return 1


def ouvrir(port, page):
    """Attend (30 s au plus) que le serveur réponde, puis ouvre la page dans le navigateur par défaut."""
    import webbrowser
    for _ in range(60):
        if repond(port, timeout=1) is not None:
            break
        time.sleep(0.5)
    webbrowser.open("http://127.0.0.1:{}/{}".format(port, page.lstrip("/")))
    return 0


# ------------------------------------------------------------------ contrôles avant lancement
def dossier_donnees(dossier=RACINE):
    d = os.environ.get("ESCAPE_DONNEES", "").strip()
    ref = os.path.join(dossier, "dossier-donnees.txt")
    if not d and os.path.exists(ref):
        try:
            with open(ref, encoding="utf-8-sig") as f:
                d = f.readline().strip().strip('"')
        except OSError:
            d = ""
    return os.path.expanduser(os.path.expandvars(d)) if d else dossier


def peut_ecrire(dossier):
    try:
        os.makedirs(dossier, exist_ok=True)
        essai = os.path.join(dossier, ".essai-ecriture-{}.tmp".format(os.getpid()))
        with open(essai, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(essai)
        return True
    except OSError:
        return False


def verifier(port):
    """Contrôles bloquants (code 1) ou simples avertissements, en français."""
    bloquant = False
    if sys.version_info < (3, 6):
        print("  [ERREUR] Python {} est trop ancien : installez Python 3 depuis python.org.".format(platform.python_version()))
        bloquant = True
    for indispensable in ("serveur.py", "index.html"):
        if not os.path.exists(os.path.join(RACINE, indispensable)):
            print("  [ERREUR] {} est introuvable : ce dossier n'est pas un dossier des jeux complet.".format(indispensable))
            bloquant = True
    if not os.path.isdir(os.path.join(RACINE, "immersifs")):
        print("  [!] Dossier immersifs\\ absent : cette copie des jeux est ancienne. Mettez-la à jour.")
    donnees = dossier_donnees()
    if not peut_ecrire(donnees):
        print("  [ERREUR] Impossible d'écrire dans le dossier des résultats : {}".format(donnees))
        print("           Déplacez le dossier des jeux dans Documents, ou corrigez dossier-donnees.txt.")
        bloquant = True
    return 1 if bloquant else 0


def infos(port):
    print("  Version des jeux : " + texte_version())
    ip = ip_locale()
    print("  Adresse à donner aux élèves : http://{}:{}/".format(ip, port))
    print("  Espace enseignant (sur ce PC) : http://127.0.0.1:{}/enseignant.html".format(port))
    if ip.startswith("127."):
        print("  [!] Pas de réseau détecté : les Chromebooks ne pourront pas joindre ce PC.")
    v, en_ligne = lire_version(), version_en_ligne(timeout=3)
    if v.get("numero") and en_ligne and int(en_ligne["numero"]) > int(v["numero"]):
        print("  [!] Une version plus récente existe en ligne (n° {}).".format(en_ligne["numero"]))
        if os.path.exists(os.path.join(RACINE, MARQUEUR_NEXTCLOUD)):
            print("      Copie Nextcloud : sur le PC principal, double-clic sur mettre-a-jour-nextcloud.bat.")
        else:
            print("      Mise à jour : double-clic sur demarrer-ecole.bat (PC de l'école).")
    return 0


# ------------------------------------------------------------------ diagnostic
def queue_fichier(chemin, n=30):
    try:
        with open(chemin, encoding="utf-8", errors="replace") as f:
            return [l.rstrip("\n") for l in f.readlines()[-n:]]
    except OSError:
        return []


def diagnostic(port, sortie=None):
    """Écrit diagnostic.txt. Ne contient AUCUN résultat d'élève (seulement des nombres de lignes)."""
    sortie = sortie or os.path.join(RACINE, "diagnostic.txt")
    L = []
    def titre(t):
        L.append("")
        L.append("== " + t + " ==")
    L.append("DIAGNOSTIC ESCAPE GAMES - " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    L.append("Dossier des jeux : " + RACINE)
    L.append("Ordinateur : {} ({} {}, {})".format(platform.node(), platform.system(), platform.release(), platform.machine()))
    titre("Version")
    v = lire_version()
    L.append("version.json : " + (json.dumps(v, ensure_ascii=False) if v else "ABSENT"))
    L.append("Commit installé : " + (commit_exact() or "inconnu"))
    en_ligne = version_en_ligne()
    L.append("version.json en ligne : " + (json.dumps(en_ligne, ensure_ascii=False) if en_ligne else "injoignable ou pas encore publié"))
    if v.get("numero") and en_ligne:
        ecart = int(en_ligne["numero"]) - int(v["numero"])
        L.append("Comparaison : " + ("à jour" if ecart == 0 else "{} version(s) de retard".format(ecart) if ecart > 0
                                     else "en avance de {} (pas encore publié)".format(-ecart)))
    L.append("Copie Nextcloud : " + ("oui ({})".format(MARQUEUR_NEXTCLOUD) if os.path.exists(os.path.join(RACINE, MARQUEUR_NEXTCLOUD)) else "non"))
    titre("Logiciels")
    L.append("Python : {} ({})".format(platform.python_version(), sys.executable))
    for nom, cmd in (("git", ["git", "--version"]), ("node", ["node", "--version"])):
        code, s = lancer(cmd, timeout=10)
        L.append("{} : {}".format(nom, s.strip() if code == 0 else "absent"))
    titre("Dépôt git")
    if os.path.isdir(os.path.join(RACINE, ".git")):
        for etiquette, cmd in (("Branche", ["git", "rev-parse", "--abbrev-ref", "HEAD"]),
                               ("Dernier commit", ["git", "log", "-1", "--format=%h %ad %s", "--date=format:%d/%m/%Y %H:%M"]),
                               ("Non publiés (origin..HEAD)", ["git", "rev-list", "--count", "origin/escape-games..HEAD"]),
                               ("En retard (HEAD..origin)", ["git", "rev-list", "--count", "HEAD..origin/escape-games"])):
            code, s = lancer(cmd, timeout=20)
            L.append("{} : {}".format(etiquette, s.strip() if code == 0 else "?"))
        code, s = lancer(["git", "status", "--porcelain"], timeout=60)
        lignes = [l for l in s.splitlines() if l.strip()] if code == 0 else []
        L.append("Fichiers modifiés ou non suivis : {}".format(len(lignes) if code == 0 else "?"))
        L.extend("   " + l for l in lignes[:15])
    else:
        L.append("Pas de dépôt git (installation par archive ou copie Nextcloud).")
    titre("Dossiers")
    jeux_imm = sorted(d for d in os.listdir(os.path.join(RACINE, "immersifs"))) if os.path.isdir(os.path.join(RACINE, "immersifs")) else []
    L.append("immersifs/ : " + ("{} jeux ({})".format(len(jeux_imm), ", ".join(jeux_imm)) if jeux_imm else "ABSENT (copie ancienne)"))
    for d in ("mission-geo", "commun", "outils-ecole"):
        L.append("{}/ : {}".format(d, "présent" if os.path.isdir(os.path.join(RACINE, d)) else "ABSENT"))
    donnees = dossier_donnees()
    L.append("Dossier des résultats : {} ({})".format(donnees, "écriture OK" if peut_ecrire(donnees) else "ÉCRITURE IMPOSSIBLE"))
    try:
        with open(os.path.join(donnees, "resultats-classe.jsonl"), encoding="utf-8", errors="replace") as f:
            n = sum(1 for l in f if l.strip())
        L.append("Parties enregistrées : {} (contenu non copié ici)".format(n))
    except OSError:
        L.append("Parties enregistrées : aucun fichier")
    try:
        libre = shutil.disk_usage(RACINE).free
        L.append("Espace libre sur le disque : {:.1f} Go".format(libre / 1e9))
    except OSError:
        pass
    titre("Réseau et serveur")
    L.append("Adresse IP de ce PC : " + ip_locale())
    L.append("Port {} : {}".format(port, "occupé" if port_occupe(port) else "libre (serveur arrêté)"))
    if os.name == "nt":
        code, s = lancer(["netstat", "-ano", "-p", "TCP"], timeout=20)
        for pid in (pids_a_l_ecoute(s, port) if code == 0 else []):
            L.append("   à l'écoute : PID {} ({})".format(pid, nom_programme(pid) or "?"))
    info = repond(port)
    L.append("Serveur des jeux : " + ("répond ({})".format(info.get("serveur", "")) if info else "ne répond pas"))
    sante = repond(port, "/api/sante", timeout=8) if info else None
    if sante:
        for voyant in sante.get("voyants", []):
            L.append("   [{}] {} : {}".format(voyant.get("etat"), voyant.get("nom"), voyant.get("message")))
    titre("Journal du PC de l'école (30 dernières lignes)")
    L.extend(queue_fichier(os.path.join(RACINE, "journal-ecole.txt")) or ["(pas de journal-ecole.txt)"])
    L.append("")
    L.append("Fin du diagnostic. Envoyez ce fichier tel quel : il ne contient aucun prénom d'élève.")
    with open(sortie, "w", encoding="utf-8-sig", newline="\r\n") as f:
        f.write("\n".join(L) + "\n")
    print("  Diagnostic écrit : " + sortie)
    return 0


# ------------------------------------------------------------------ copie Nextcloud
def est_protege(chemin):
    """chemin relatif (séparateur /) : fichier de la classe à ne jamais toucher."""
    parties = [p for p in chemin.split("/") if p]
    if not parties:
        return True
    if any(p.lower() in PROTEGES_DOSSIERS for p in parties[:-1]) or parties[0].lower() in PROTEGES_DOSSIERS:
        return True
    nom = parties[-1].lower()
    return (nom in PROTEGES_NOMS or nom.startswith(PROTEGES_DEBUTS) or nom.endswith((".tmp", ".part"))
            or (nom.startswith(PROTEGES_TXT) and nom.endswith(".txt")))


def hash_blob(donnees):
    return hashlib.sha1(b"blob %d\0" % len(donnees) + donnees).hexdigest()


def contenu_disque(chemin_rel, donnees_depot):
    """Contenu tel qu'il doit être écrit sur le disque (CRLF pour les scripts Windows, comme git)."""
    if chemin_rel.lower().endswith(EXT_CRLF) and b"\0" not in donnees_depot:
        return donnees_depot.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    return donnees_depot


def identique_sur_disque(chemin, sha, taille_depot):
    """Le fichier du disque correspond-il à l'objet git sha (fins de ligne CRLF ou LF acceptées) ?"""
    try:
        taille = os.path.getsize(chemin)
        if taille < taille_depot or taille > taille_depot * 2 + 16:
            return False
        with open(chemin, "rb") as f:
            d = f.read()
    except OSError:
        return False
    if hash_blob(d) == sha:
        return True
    return b"\0" not in d[:8000] and b"\r\n" in d and hash_blob(d.replace(b"\r\n", b"\n")) == sha


def arbre_git(depot, rev="HEAD"):
    """{chemin: (sha, taille)} des fichiers de la révision (version commitée, rien de local)."""
    code, sortie = lancer(["git", "-c", "core.quotepath=off", "ls-tree", "-r", "-l", "-z", rev], cwd=depot, timeout=120)
    if code != 0:
        raise RuntimeError("git ls-tree a échoué : " + sortie.strip()[:300])
    arbre = {}
    for entree in sortie.split("\0"):
        if not entree.strip():
            continue
        meta, chemin = entree.split("\t", 1)
        mode, typ, sha, taille = meta.split()
        if typ == "blob" and mode != "120000":   # pas de liens symboliques
            arbre[chemin] = (sha, int(taille))
    return arbre


class LecteurBlobs:
    """git cat-file --batch : lit le contenu de nombreux objets avec un seul processus."""
    def __init__(self, depot):
        self.p = subprocess.Popen(["git", "cat-file", "--batch"], cwd=depot, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def lire(self, sha):
        self.p.stdin.write((sha + "\n").encode("ascii"))
        self.p.stdin.flush()
        entete = self.p.stdout.readline().decode("ascii", "replace").split()
        if len(entete) < 3 or entete[1] != "blob":
            raise RuntimeError("objet git illisible : " + sha)
        taille = int(entete[2])
        donnees = self.p.stdout.read(taille)
        self.p.stdout.read(1)
        return donnees

    def fermer(self):
        try:
            self.p.stdin.close()
            self.p.wait(timeout=10)
        except Exception:
            self.p.kill()


def ecrire_fichier(chemin, donnees):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    tmp = chemin + ".part"
    with open(tmp, "wb") as f:
        f.write(donnees)
    os.replace(tmp, chemin)


def dossier_nextcloud_par_defaut():
    ref = os.path.join(RACINE, "outils-ecole", "dossier-nextcloud.txt")
    if os.path.exists(ref):
        with open(ref, encoding="utf-8-sig") as f:
            d = f.readline().strip().strip('"')
        if d:
            return os.path.expanduser(os.path.expandvars(d))
    return os.path.join(os.path.expanduser("~"), "Nextcloud", "Escape games", "escape-games-cm1-cm2-escape-games")


def ressemble_a_une_copie(dest):
    """Garde-fou : on ne travaille que dans un dossier vide, une copie des jeux, ou une copie déjà faite par ce script."""
    if not os.path.isdir(dest):
        return True
    noms = set(os.listdir(dest))
    if not noms - {"desktop.ini", "Thumbs.db", ".DS_Store"}:
        return True
    return MANIFESTE in noms or MARQUEUR_NEXTCLOUD in noms or {"index.html", "serveur.py"} <= noms


def synchroniser(depot, dest, essai=False, journal=print):
    """Copie la version commitée (HEAD) de depot dans dest.
    - nouveaux fichiers et fichiers modifiés : écrits ;
    - fichiers identiques : laissés (rien n'est renvoyé à Nextcloud) ;
    - fichiers qui n'existent plus dans le dépôt : déplacés dans dest/_a-supprimer/AAAA-MM-JJ/ (jamais effacés) ;
    - fichiers de la classe (résultats, sauvegardes, réglages, journaux) : jamais touchés.
    Renvoie un dict de comptes."""
    depot, dest = os.path.abspath(depot), os.path.abspath(dest)
    if os.path.normcase(dest).startswith(os.path.normcase(depot + os.sep)) or os.path.normcase(dest) == os.path.normcase(depot):
        raise RuntimeError("le dossier Nextcloud ne peut pas être dans le dossier du dépôt")
    if not ressemble_a_une_copie(dest):
        raise RuntimeError("le dossier {} ne ressemble pas à une copie des jeux (ni index.html ni serveur.py) : "
                           "rien n'est fait. Indiquez le bon dossier dans outils-ecole\\dossier-nextcloud.txt.".format(dest))
    arbre = arbre_git(depot)
    try:
        with open(os.path.join(dest, MANIFESTE), encoding="utf-8") as f:
            ancien = json.load(f).get("fichiers", {})
    except (OSError, ValueError, AttributeError):
        ancien = {}
    comptes = {"ecrits": 0, "identiques": 0, "deplaces": 0, "proteges": 0, "erreurs": 0}
    a_ecrire = []
    for chemin, (sha, taille) in sorted(arbre.items()):
        if est_protege(chemin):
            comptes["proteges"] += 1
            continue
        cible = os.path.join(dest, *chemin.split("/"))
        if ancien.get(chemin) == sha and os.path.exists(cible):
            comptes["identiques"] += 1
        elif identique_sur_disque(cible, sha, taille):
            comptes["identiques"] += 1
        else:
            a_ecrire.append((chemin, sha))
    lecteur = None if essai or not a_ecrire else LecteurBlobs(depot)
    try:
        for chemin, sha in a_ecrire:
            if not essai:
                donnees = contenu_disque(chemin, lecteur.lire(sha))
                try:
                    ecrire_fichier(os.path.join(dest, *chemin.split("/")), donnees)
                except OSError as e:
                    comptes["erreurs"] += 1
                    journal("  [!] impossible d'écrire {} ({}) : relancez plus tard".format(chemin, e.__class__.__name__))
                    continue
            comptes["ecrits"] += 1
            if comptes["ecrits"] <= 20 or comptes["ecrits"] % 200 == 0:
                journal("  {} {}".format("à copier :" if essai else "copié :", chemin))
    finally:
        if lecteur:
            lecteur.fermer()
    # Fichiers devenus inutiles : déplacés, jamais effacés.
    corbeille = os.path.join(dest, "_a-supprimer", datetime.date.today().isoformat())
    if os.path.isdir(dest):
        for base, dossiers, fichiers in os.walk(dest):
            rel_base = os.path.relpath(base, dest).replace(os.sep, "/")
            rel_base = "" if rel_base == "." else rel_base + "/"
            # dossiers et fichiers cachés (.sync_*.db, .nextcloudsync.log du client Nextcloud...) : jamais touchés
            dossiers[:] = [d for d in dossiers if not est_protege(rel_base + d + "/x") and not d.startswith(".")]
            for nom in fichiers:
                rel = rel_base + nom
                if rel in arbre or est_protege(rel) or nom.startswith((".", "~$")):
                    continue
                comptes["deplaces"] += 1
                journal("  {} {}".format("à ranger dans _a-supprimer :" if essai else "rangé dans _a-supprimer :", rel))
                if not essai:
                    ecrire_dossier = os.path.join(corbeille, *rel.split("/")[:-1])
                    try:
                        os.makedirs(ecrire_dossier, exist_ok=True)
                        shutil.move(os.path.join(base, nom), os.path.join(ecrire_dossier, nom))
                    except OSError:
                        comptes["erreurs"] += 1
    if not essai:
        os.makedirs(dest, exist_ok=True)
        v = lire_version_depot(depot)
        with open(os.path.join(dest, MANIFESTE), "w", encoding="utf-8", newline="\n") as f:
            json.dump({"source": depot, "date": datetime.datetime.now().isoformat(timespec="seconds"),
                       "version": v, "fichiers": {c: s for c, (s, _) in arbre.items() if not est_protege(c)}}, f)
        with open(os.path.join(dest, MARQUEUR_NEXTCLOUD), "w", encoding="utf-8", newline="\r\n") as f:
            f.write("Copie Nextcloud des escape games, mise à jour depuis le PC principal\n"
                    "(mettre-a-jour-nextcloud.bat). Ne pas modifier les jeux ici : les changements seraient remplacés.\n"
                    "Derniere copie : {} - version {}\n".format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                                                                v.get("numero", "?")))
    return comptes


def lire_version_depot(depot):
    code, sortie = lancer(["git", "show", "HEAD:version.json"], cwd=depot, timeout=20)
    try:
        return json.loads(sortie) if code == 0 else {}
    except ValueError:
        return {}


def nextcloud(dest, essai):
    if not os.path.isdir(os.path.join(RACINE, ".git")):
        print("  [ERREUR] Ce dossier n'est pas le dépôt git du PC principal : lancez ce script depuis")
        print("           E:\\IDRISS\\PROJET ESCAPE GAMES (pas depuis la copie Nextcloud).")
        return 1
    dest = dest or dossier_nextcloud_par_defaut()
    if not os.path.isdir(dest):
        print("  [ERREUR] Dossier de la copie Nextcloud introuvable : " + dest)
        print("           1. Ouvrez l'Explorateur de fichiers et trouvez la copie des jeux dans Nextcloud.")
        print("           2. Clic dans la barre d'adresse, Ctrl+C pour copier son chemin.")
        print("           3. Ouvrez avec le Bloc-notes outils-ecole\\dossier-nextcloud.txt (créez-le s'il manque),")
        print("              collez le chemin sur la première ligne, enregistrez, relancez.")
        return 1
    print("  Dépôt   : " + RACINE)
    print("  Copie   : " + dest)
    print("  Version : " + texte_version(avec_commit=True))
    code, s = lancer(["git", "status", "--porcelain", "--untracked-files=no"], timeout=60)
    if code == 0 and s.strip():
        print("  [i] Des modifications ne sont pas encore commitées : elles ne sont PAS copiées (seule la version commitée l'est).")
    try:
        c = synchroniser(RACINE, dest, essai=essai)
    except RuntimeError as e:
        print("  [ERREUR] " + str(e))
        return 1
    print("")
    print("  {} : {} fichier(s) {}, {} identique(s), {} rangé(s) dans _a-supprimer, fichiers de la classe jamais touchés."
          .format("ESSAI" if essai else "TERMINÉ", c["ecrits"], "à copier" if essai else "copié(s)", c["identiques"], c["deplaces"]))
    if c["erreurs"]:
        print("  [!] {} fichier(s) n'ont pas pu être écrits ou rangés (ouverts ailleurs ?) : relancez la mise à jour.".format(c["erreurs"]))
        return 1
    if not essai:
        print("  Nextcloud envoie maintenant les changements ; le PC de l'école les reçoit tout seul.")
    return 0


# ------------------------------------------------------------------ entrée
def main(argv):
    preparer_console()
    args = list(argv)
    port = PORT_DEFAUT
    if "--port" in args:
        i = args.index("--port")
        try:
            port = int(args[i + 1])
        except (IndexError, ValueError):
            print("  --port doit être suivi d'un numéro")
            return 1
        del args[i:i + 2]
    essai = "--essai" in args
    args = [a for a in args if a != "--essai"]
    if not args:
        print(__doc__)
        return 1
    cmd, reste = args[0], args[1:]
    if cmd == "infos":
        return infos(port)
    if cmd == "version":
        print(texte_version())
        return 0
    if cmd == "verifier":
        return verifier(port)
    if cmd == "liberer-port":
        return liberer_port(port)
    if cmd == "ouvrir":
        return ouvrir(port, reste[0] if reste else "enseignant.html")
    if cmd == "diagnostic":
        return diagnostic(port)
    if cmd == "nextcloud":
        return nextcloud(reste[0] if reste else "", essai)
    print("  Commande inconnue : " + cmd)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
