#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================
 ESCAPE GAMES PÉDAGOGIQUES — Serveur local · CM1-CM2
 Sert les jeux (declaration/, tour-du-monde/, mission-geo/,
 constitution/, station-meteo/, melanges/, moyen-age-abbaye/,
 objets-techniques/, chateau-fort/, versailles/, renaissance/,
 alimentation/, lumiere/, etats-matiere/, mouvement/),
 la page d'accueil et verifier.html, depuis la racine du projet.
============================================================
 Serveur HTTP stdlib + mini-API REST pour le pilotage prof.
 Aucune dépendance externe : Python 3.6+ suffit.

 Usage :
    python serveur.py            # port 8000
    python serveur.py 8080       # port personnalisé
============================================================
"""
import os
import re
import sys
import json
import time
import socket
import threading
import shutil
import csv
import io
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib.parse import urlparse, parse_qs, unquote

# Le serveur travaille TOUJOURS dans le dossier du projet, d'où qu'on le lance
# (raccourci, « Exécuter en tant qu'administrateur », autre dossier courant…).
DOSSIER_PROJET = os.path.dirname(os.path.abspath(__file__))
os.chdir(DOSSIER_PROJET)

# ---- État partagé des équipes (en mémoire) ----
ETATS_EQUIPES = {}        # { "Les Patriotes": {salle, score, fragments, ...} }
COMMANDES_PROF = {}       # { "equipe": {"pause":bool, "indice":"..."} }
LOCK = threading.Lock()
# Résultats des parties terminées, gardés toute l'année sur CET ordinateur (amélioration D5).
# Fichier jamais publié (.gitignore) : il contient les prénoms des élèves.
def dossier_donnees():
    """Dossier où sont gardés les fichiers de la classe (résultats, difficulté).
    Par défaut : le dossier du projet. Pour les retrouver ailleurs (ex. un dossier synchronisé OneDrive /
    Google Drive / Nextcloud, lu ensuite depuis la maison) : écrire le chemin sur la 1re ligne d'un fichier
    « dossier-donnees.txt » placé à côté de serveur.py (jamais publié, voir .gitignore), ou définir la variable
    d'environnement ESCAPE_DONNEES."""
    d = os.environ.get("ESCAPE_DONNEES", "").strip()
    if not d:
        ref = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dossier-donnees.txt")
        if os.path.exists(ref):
            with open(ref, encoding="utf-8-sig") as f:
                d = f.readline().strip().strip('"')
    if not d:
        return ""
    d = os.path.expanduser(os.path.expandvars(d))
    try:
        os.makedirs(d, exist_ok=True)
    except OSError as e:
        print("  ⚠️  Dossier de données inutilisable ({}) : {}. Le dossier du projet est utilisé.".format(d, e))
        return ""
    return d

DOSSIER_DONNEES = dossier_donnees() or DOSSIER_PROJET
# Résultats des élèves (jamais publiés, jamais servis par le réseau : ils contiennent les prénoms) :
#   resultats-classe.jsonl   une partie par ligne, enregistrée automatiquement (ajout seulement)
#   resultats-classe.csv     le même contenu pour Excel / LibreOffice, remis à jour à chaque partie
#   sauvegardes-resultats/   une copie de sécurité par jour (60 jours gardés)
FICHIER_RESULTATS = os.path.join(DOSSIER_DONNEES, "resultats-classe.jsonl")
FICHIER_RESULTATS_CSV = os.path.join(DOSSIER_DONNEES, "resultats-classe.csv")
DOSSIER_SAUVEGARDES = os.path.join(DOSSIER_DONNEES, "sauvegardes-resultats")
RESULTATS_LOCK = threading.RLock()
TAILLE_MAX_REQUETE = 5 * 1024 * 1024
FICHIER_DIFFICULTE = os.path.join(DOSSIER_DONNEES, "difficulte-classe.json")   # N20 : réglages de difficulté énigme par énigme
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

def get_ip_locale():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


# ---- Adresses de CET ordinateur : seul l'enseignant lit les résultats ----
_ADRESSES = {"t": 0, "v": set()}

def adresses_locales():
    """Adresses de cet ordinateur (boucle locale + IP du réseau), rafraîchies chaque minute."""
    if time.time() - _ADRESSES["t"] > 60:
        ad = {"127.0.0.1", "::1"}
        try:
            ad.add(get_ip_locale())
            for info in socket.getaddrinfo(socket.gethostname(), None):
                ad.add(info[4][0])
        except Exception:
            pass
        _ADRESSES["t"], _ADRESSES["v"] = time.time(), ad
    return _ADRESSES["v"]

def est_adresse_locale(ip):
    ip = str(ip or "")
    if ip.startswith("::ffff:"):
        ip = ip[7:]
    return ip in adresses_locales()


# ---- Résultats des parties (D5) : enregistrement automatique, sûr, sans doublon ----
def cle_resultat(r):
    """Une partie = jeu + équipe/élève + mode + début (même clé que resultats.html)."""
    return "|".join([str(r.get("jeu") or ""), str(r.get("eleve") or ""), str(r.get("mode") or ""),
                     str(r.get("partie") or r.get("date") or "")])

def resultat_valide(r):
    if not isinstance(r, dict) or r.get("type") != "escape-game-compte-rendu":
        return False
    if not isinstance(r.get("jeu", ""), str) or not isinstance(r.get("eleve", ""), str):
        return False
    try:
        return len(json.dumps(r, ensure_ascii=False)) < 200000
    except (TypeError, ValueError):
        return False

def lire_resultats():
    """Toutes les parties (dernière version de chacune). Une ligne abîmée est ignorée, jamais fatale."""
    index, ordre = {}, []
    with RESULTATS_LOCK:
        try:
            with open(FICHIER_RESULTATS, encoding="utf-8", errors="replace") as f:
                for ligne in f:
                    ligne = ligne.strip()
                    if not ligne:
                        continue
                    try:
                        r = json.loads(ligne)
                    except ValueError:
                        continue
                    if not resultat_valide(r):
                        continue
                    k = cle_resultat(r)
                    if k not in index:
                        ordre.append(k)
                    index[k] = r
        except OSError:
            pass
    return [index[k] for k in ordre]

def date_fr(s):
    s = str(s or "")
    try:
        return "{}/{}/{} {}".format(s[8:10], s[5:7], s[0:4], s[11:16]).strip() if len(s) >= 10 else s
    except Exception:
        return s

def texte_sur(v):
    """Neutralise les formules (=, +, -, @) : un prénom saisi par un élève ne doit pas s'exécuter dans Excel."""
    v = str(v if v is not None else "")
    return ("'" + v) if v[:1] in ("=", "+", "-", "@", "\t", "\r") else v

def ecrire_csv(liste):
    """resultats-classe.csv : même contenu que le .jsonl, ouvrable dans Excel (écriture atomique)."""
    try:
        lignes = [["Date", "Élève / équipe", "Mode", "Jeu", "Niveau", "Palier", "Score", "Score max", "Pourcentage",
                   "Énigmes réussies", "Énigmes", "Du premier coup", "Erreurs", "Indices", "Durée (min)", "Partie terminée"]]
        for r in sorted(liste, key=lambda x: str(x.get("date") or ""), reverse=True):
            sc, mx = r.get("score"), r.get("scoreMax")
            pct = round(100.0 * sc / mx) if isinstance(sc, (int, float)) and isinstance(mx, (int, float)) and mx else ""
            lignes.append([date_fr(r.get("date")), texte_sur(r.get("eleve")), "individuel" if r.get("mode") == "solo" else "équipe",
                           texte_sur(r.get("titre") or r.get("jeu")), texte_sur(r.get("niveau")), texte_sur(r.get("palier")),
                           sc if sc is not None else "", mx if mx is not None else "", pct,
                           r.get("enigmes", ""), r.get("total", ""), r.get("premierCoup", ""), r.get("erreurs", ""),
                           r.get("indices", ""), str(r.get("dureeMin", "")).replace(".", ","),
                           "oui" if r.get("termine") else "non"])
        tampon = io.StringIO(newline="")
        csv.writer(tampon, delimiter=";", lineterminator="\r\n").writerows(lignes)
        tmp = FICHIER_RESULTATS_CSV + ".tmp"
        with open(tmp, "w", encoding="utf-8-sig", newline="") as f:
            f.write(tampon.getvalue())
        os.replace(tmp, FICHIER_RESULTATS_CSV)
    except OSError:
        pass

def copie_de_securite():
    """Copie du jour dans sauvegardes-resultats/ (remise à jour à chaque écriture, 60 jours gardés)."""
    try:
        if not os.path.exists(FICHIER_RESULTATS):
            return
        os.makedirs(DOSSIER_SAUVEGARDES, exist_ok=True)
        cible = os.path.join(DOSSIER_SAUVEGARDES, "resultats-classe-%s.jsonl" % time.strftime("%Y-%m-%d"))
        shutil.copyfile(FICHIER_RESULTATS, cible + ".tmp")
        os.replace(cible + ".tmp", cible)
        anciennes = sorted(f for f in os.listdir(DOSSIER_SAUVEGARDES) if f.startswith("resultats-classe-") and f.endswith(".jsonl"))
        for ancienne in anciennes[:-60]:
            os.remove(os.path.join(DOSSIER_SAUVEGARDES, ancienne))
    except OSError:
        pass

def enregistrer_resultats(liste):
    """Ajoute les parties nouvelles ou modifiées. Retourne (nombre écrit, nombre total). Jamais d'effacement."""
    with RESULTATS_LOCK:
        existants = {}
        for r in lire_resultats():
            existants[cle_resultat(r)] = r
        a_ecrire = []
        for r in liste:
            if not resultat_valide(r):
                continue
            r = {k: v for k, v in r.items() if not str(k).startswith("_")}   # marques internes de la page, pas des données
            k = cle_resultat(r)
            if existants.get(k) == r:
                continue                                                    # déjà enregistrée à l'identique
            existants[k] = r
            a_ecrire.append(r)
        if a_ecrire:
            try:
                debut_de_ligne = True
                if os.path.exists(FICHIER_RESULTATS) and os.path.getsize(FICHIER_RESULTATS) > 0:
                    with open(FICHIER_RESULTATS, "rb") as f:
                        f.seek(-1, os.SEEK_END)
                        debut_de_ligne = f.read(1) == b"\n"           # dernière ligne coupée (arrêt brutal) : on repart à la ligne
                with open(FICHIER_RESULTATS, "a", encoding="utf-8", newline="\n") as f:
                    if not debut_de_ligne:
                        f.write("\n")
                    for r in a_ecrire:
                        f.write(json.dumps(r, ensure_ascii=False) + "\n")
                    f.flush()
                    os.fsync(f.fileno())
            except OSError as e:
                print("  ⚠️  Résultats NON enregistrés (" + str(e) + ")")
                return -1, len(existants)
            ecrire_csv(list(existants.values()))
            copie_de_securite()
        return len(a_ecrire), len(existants)

def infos_stockage():
    liste = lire_resultats()
    try:
        nb_copies = len([f for f in os.listdir(DOSSIER_SAUVEGARDES) if f.endswith(".jsonl")])
    except OSError:
        nb_copies = 0
    ip = get_ip_locale()
    return {"ok": True, "nbParties": len(liste), "fichier": FICHIER_RESULTATS, "csv": FICHIER_RESULTATS_CSV,
            "dossierSauvegardes": DOSSIER_SAUVEGARDES, "nbCopies": nb_copies,
            "derniere": max([str(r.get("date") or "") for r in liste] or [""]),
            "ip": ip, "port": PORT, "adresseEleves": "http://{}:{}/".format(ip, PORT)}

def chemin_prive(chemin_relatif):
    """Fichiers qu'on ne sert jamais par le réseau : résultats des élèves, copies, clés, dépôt git."""
    segments = [x for x in chemin_relatif.replace("\\", "/").split("/") if x]
    if not segments:
        return False
    nom = segments[-1].lower()
    return (".git" in [x.lower() for x in segments] or segments[0].lower() in ("sauvegardes-resultats", "installations")
            or nom.startswith("resultats-classe") or nom.startswith("difficulte-classe") or nom.startswith("dossier-donnees") or nom.startswith("seance-du-jour")
            or nom.startswith("journal-ecole") or nom in ("version-installee.txt", "diagnostic.txt", "copie-nextcloud.txt", ".copie-escape-games.json")
            or (nom.startswith("cle-") and nom.endswith(".txt")))


# ---- Séance du jour (A1) et feu vert avant la séance (A4) ----
# Le jeu du jour choisi par l'enseignant est gardé dans le dossier de données (jamais publié) :
# l'accueil servi aux élèves n'affiche alors qu'un grand bouton « Jouer » vers ce jeu.
FICHIER_SEANCE = os.path.join(DOSSIER_DONNEES, "seance-du-jour.json")
GRADES_IMMERSIFS = ("mousse", "matelot", "timonier", "lieutenant", "second")
DEPOT_GITHUB = "IdGir/escape-games-cm1-cm2"
BRANCHE_GITHUB = "escape-games"

def id_jeu_valide(jeu):
    """Un identifiant de jeu : lettres, chiffres, tirets, et un dossier qui existe (variante immersive ou classique)."""
    jeu = str(jeu or "").strip().lower()
    if not jeu or len(jeu) > 60 or not all(c.isalnum() or c == "-" for c in jeu):
        return ""
    return jeu if (os.path.isdir(os.path.join("immersifs", jeu)) or os.path.isdir(jeu)) else ""

def lire_seance():
    try:
        with open(FICHIER_SEANCE, encoding="utf-8") as f:
            s = json.load(f)
        return s if isinstance(s, dict) and id_jeu_valide(s.get("jeu")) else None
    except (OSError, ValueError):
        return None

def ecrire_seance(seance):
    """seance = None : plus de séance (l'accueil redevient normal)."""
    if seance is None:
        try:
            os.remove(FICHIER_SEANCE)
        except OSError:
            pass
        return True
    try:
        tmp = FICHIER_SEANCE + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(seance, f, ensure_ascii=False, indent=1)
        os.replace(tmp, FICHIER_SEANCE)
        return True
    except OSError:
        return False

# ---- Relectures validées (page « À relire » de l'espace enseignant) ----
# Un point validé ou à corriger est gardé dans le dossier de données (jamais publié) : relectures-validees.json.
FICHIER_RELECTURES = os.path.join(DOSSIER_DONNEES, "relectures-validees.json")

def lire_relectures():
    try:
        with open(FICHIER_RELECTURES, encoding="utf-8") as f:
            r = json.load(f)
        return r if isinstance(r, dict) else {}
    except (OSError, ValueError):
        return {}

def noter_relecture(ident, etat, note):
    """etat : « ok », « corriger » ou « » (remettre à relire). Renvoie True si le fichier est écrit."""
    ident = str(ident or "")
    if not re.match(r"^[a-z0-9-]{1,60}:\d{1,4}:[0-9a-f]{6}$", ident) or etat not in ("ok", "corriger", ""):
        return False
    r = lire_relectures()
    if etat:
        r[ident] = {"e": etat, "n": str(note or "")[:300], "d": time.strftime("%Y-%m-%d")}
    else:
        r.pop(ident, None)
    if len(r) > 3000:
        return False
    try:
        tmp = FICHIER_RELECTURES + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(r, f, ensure_ascii=False, indent=1)
        os.replace(tmp, FICHIER_RELECTURES)
        return True
    except OSError:
        return False

def adresse_jeu(jeu):
    return "immersifs/{}/".format(jeu) if os.path.isdir(os.path.join("immersifs", jeu)) else "{}/".format(jeu)

def version_locale():
    """Version installée : le commit de la branche (dépôt git) ou version-installee.txt (installation par archive)."""
    try:
        with open(os.path.join(".git", "HEAD"), encoding="utf-8") as f:
            tete = f.read().strip()
        if tete.startswith("ref:"):
            ref = tete[4:].strip()
            chemin = os.path.join(".git", *ref.split("/"))
            if os.path.exists(chemin):
                with open(chemin, encoding="utf-8") as f:
                    return f.read().strip()
            with open(os.path.join(".git", "packed-refs"), encoding="utf-8") as f:
                for ligne in f:
                    if ligne.strip().endswith(" " + ref):
                        return ligne.split()[0]
        elif len(tete) >= 40:
            return tete[:40]
    except OSError:
        pass
    try:
        with open("version-installee.txt", encoding="utf-8") as f:
            return f.readline().strip()
    except OSError:
        return ""

_VERSION_DISTANTE = {"t": 0, "v": None}
_VERSION_EN_LIGNE = {"t": 0, "v": None}

def lire_version_json():
    """version.json (écrit à chaque commit par outils-tests/hooks/pre-commit) : {numero, date, branche, commit_precedent}."""
    try:
        with open(os.path.join(DOSSIER_PROJET, "version.json"), encoding="utf-8-sig") as f:
            v = json.load(f)
        return v if isinstance(v, dict) else {}
    except (OSError, ValueError):
        return {}

def texte_numero(v):
    """« n° 412 du 23/11/2026 » (ou '' sans version.json)."""
    if not v or not v.get("numero"):
        return ""
    d = str(v.get("date") or "")
    return "n° {}{}".format(v["numero"], " du {}/{}/{}".format(d[8:10], d[5:7], d[0:4]) if len(d) >= 10 else "")

def version_en_ligne():
    """version.json du site GitHub Pages (gardé 10 minutes ; None si injoignable ou pas encore publié)."""
    if time.time() - _VERSION_EN_LIGNE["t"] < 600:
        return _VERSION_EN_LIGNE["v"]
    v = None
    try:
        import urllib.request
        req = urllib.request.Request("https://idgir.github.io/escape-games-cm1-cm2/version.json?t={}".format(int(time.time())),
                                     headers={"User-Agent": "escape-games-serveur", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(req, timeout=4) as r:
            v = json.loads(r.read(20000).decode("utf-8", "replace"))
        v = v if isinstance(v, dict) and isinstance(v.get("numero"), int) else None
    except Exception:
        v = None
    _VERSION_EN_LIGNE["t"], _VERSION_EN_LIGNE["v"] = time.time(), v
    return v

def version_distante():
    """Dernier commit publié sur GitHub (gardé 10 minutes ; None si internet ne répond pas)."""
    if time.time() - _VERSION_DISTANTE["t"] < 600:
        return _VERSION_DISTANTE["v"]
    v = None
    try:
        import urllib.request
        req = urllib.request.Request("https://api.github.com/repos/{}/commits/{}".format(DEPOT_GITHUB, BRANCHE_GITHUB),
                                     headers={"Accept": "application/vnd.github.sha", "User-Agent": "escape-games-serveur"})
        with urllib.request.urlopen(req, timeout=4) as r:
            v = r.read(100).decode("ascii", "replace").strip()[:40] or None
    except Exception:
        v = None
    _VERSION_DISTANTE["t"], _VERSION_DISTANTE["v"] = time.time(), v
    return v

def est_ancetre(ancien, recent):
    """Vrai si le commit « ancien » est dans l'historique de « recent » (git requis ; None si on ne sait pas)."""
    try:
        import subprocess
        r = subprocess.run(["git", "merge-base", "--is-ancestor", ancien, recent], cwd=DOSSIER_PROJET,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        return {0: True, 1: False}.get(r.returncode)
    except Exception:
        return None

def medias_du_jeu(jeu):
    """Médias attendus (medias.csv de la variante immersive) : (présents, attendus, exemples manquants)."""
    base = os.path.join("immersifs", jeu)
    csv_medias = os.path.join(base, "medias.csv")
    if not os.path.exists(csv_medias):
        return None
    presents, attendus, manquants = 0, 0, []
    try:
        with open(csv_medias, encoding="utf-8-sig", newline="") as f:
            for ligne in csv.DictReader(f, delimiter=";"):
                fichier = (ligne.get("fichier") or "").strip()
                if not fichier:
                    continue
                attendus += 1
                if os.path.exists(os.path.join(base, *fichier.split("/"))):
                    presents += 1
                else:
                    manquants.append(fichier)
    except (OSError, csv.Error):
        return None
    return presents, attendus, manquants

def etat_sante():
    """Feu vert avant la séance (A4) : un voyant par point, avec l'action à faire pour chaque orange ou rouge."""
    voyants = [{"id": "serveur", "nom": "Serveur", "etat": "vert",
                "message": "Le serveur répond. Adresse des élèves : http://{}:{}/".format(get_ip_locale(), PORT), "action": ""}]
    # Version à jour par rapport à GitHub
    loc, dist = version_locale(), version_distante()
    vj = lire_version_json()
    num = texte_numero(vj)
    en_ligne = version_en_ligne() if (vj.get("numero") and (not loc or not dist)) else None
    if en_ligne and isinstance(vj.get("numero"), int):
        # Copie sans git (Nextcloud, archive) : on compare les numéros de version.json
        if vj["numero"] == en_ligne["numero"]:
            v = ("vert", "Version à jour ({}, identique au site en ligne).".format(num), "")
        elif vj["numero"] > en_ligne["numero"]:
            v = ("orange", "Cette copie ({}) est plus récente que le site en ligne ({}).".format(num, texte_numero(en_ligne)),
                 "Publiez depuis le PC principal (git push origin escape-games) si les Chromebooks jouent aussi en ligne.")
        else:
            v = ("orange", "Une version plus récente existe ({} en ligne, {} ici).".format(texte_numero(en_ligne), num),
                 "Copie Nextcloud : lancez mettre-a-jour-nextcloud.bat sur le PC principal. PC de l'école : fermez puis rouvrez la session Windows.")
    elif not loc and num:
        v = ("orange", "Version installée : {} (site en ligne injoignable, non comparée).".format(num),
             "Rien à faire si le jeu marche.")
    elif not loc:
        v = ("orange", "Version installée inconnue (ni dépôt git, ni version-installee.txt).",
             "Installez la mise à jour automatique : double-clic sur installer-ecole.bat (une seule fois).")
    elif not dist:
        v = ("orange", "GitHub injoignable : version non comparée.",
             "Rien à faire si le jeu marche (sinon : connexion internet du PC).")
    elif loc == dist:
        v = ("vert", "Version à jour (identique à GitHub, {}{}).".format(num + ", " if num else "", loc[:7]), "")
    elif est_ancetre(dist, loc):
        v = ("orange", "Ce PC a des modifications pas encore publiées sur GitHub ({} ici, {} en ligne).".format(loc[:7], dist[:7]),
             "Publiez-les (git push) si les Chromebooks jouent aussi depuis le site en ligne.")
    else:
        v = ("orange", "Une version plus récente existe sur GitHub ({} en ligne, {} ici).".format(dist[:7], loc[:7]),
             "Fermez la session Windows puis rouvrez-la (mise à jour automatique), ou double-clic sur demarrer-ecole.bat.")
    voyants.append({"id": "version", "nom": "Version", "etat": v[0], "message": v[1], "action": v[2],
                    "numero": vj.get("numero"), "date": vj.get("date"), "commit": loc[:40]})
    # Médias du jeu du jour
    s = lire_seance()
    if not s:
        voyants.append({"id": "medias", "nom": "Médias du jeu du jour", "etat": "orange",
                        "message": "Aucun jeu du jour choisi.", "action": "Choisissez le jeu en haut de l'espace enseignant, puis « Lancer »."})
    else:
        m = medias_du_jeu(s["jeu"])
        if not os.path.isdir(os.path.join("immersifs", s["jeu"])) and not os.path.isdir(s["jeu"]):
            voyants.append({"id": "medias", "nom": "Médias du jeu du jour", "etat": "rouge", "message": "Le dossier du jeu est introuvable.",
                            "action": "Mettez le dépôt à jour (demarrer-ecole.bat) ou choisissez un autre jeu."})
        elif m is None:
            voyants.append({"id": "medias", "nom": "Médias du jeu du jour", "etat": "vert", "message": "Jeu sans liste de médias : rien à vérifier.", "action": ""})
        elif m[0] >= m[1]:
            voyants.append({"id": "medias", "nom": "Médias du jeu du jour", "etat": "vert", "message": "Tous les médias sont là ({}/{}).".format(m[0], m[1]), "action": ""})
        else:
            voyants.append({"id": "medias", "nom": "Médias du jeu du jour", "etat": "orange",
                            "message": "{} média(s) sur {} pas encore produits. Le jeu marche quand même (décors dessinés).".format(m[1] - m[0], m[1]),
                            "action": "Rien d'obligatoire ; liste dans verifier.html.", "manquants": m[2][:20]})
    # Dossier des résultats accessible en écriture
    try:
        os.makedirs(DOSSIER_DONNEES, exist_ok=True)
        essai = os.path.join(DOSSIER_DONNEES, ".essai-ecriture.tmp")
        with open(essai, "w", encoding="utf-8") as f:
            f.write("ok")
        os.remove(essai)
        voyants.append({"id": "resultats", "nom": "Dossier des résultats", "etat": "vert", "message": "Les résultats seront bien enregistrés.", "action": ""})
    except OSError as e:
        voyants.append({"id": "resultats", "nom": "Dossier des résultats", "etat": "rouge",
                        "message": "Impossible d'écrire dans le dossier des résultats ({}).".format(e.__class__.__name__),
                        "action": "Vérifiez dossier-donnees.txt (chemin du dossier) et que ce dossier existe (clé USB, Nextcloud…), puis relancez le serveur."})
    voyants.append(voyant_sauvegarde())
    pire = "rouge" if any(x["etat"] == "rouge" for x in voyants) else "orange" if any(x["etat"] == "orange" for x in voyants) else "vert"
    return {"ok": True, "etat": pire, "voyants": voyants, "seance": s}


def voyant_sauvegarde():
    """Sauvegardes : copie du jour des résultats (sauvegardes-resultats/) et sauvegarde complète du projet (lot 3, D2)."""
    v = {"id": "sauvegarde", "nom": "Sauvegarde", "etat": "vert", "message": "", "action": ""}
    try:
        copies = sorted(f for f in os.listdir(DOSSIER_SAUVEGARDES) if f.startswith("resultats-classe-") and f.endswith(".jsonl"))
    except OSError:
        copies = []
    if os.path.exists(FICHIER_RESULTATS) and not copies:
        v.update(etat="orange", message="Aucune copie de sécurité des résultats pour l'instant.",
                 action="Elle se fait toute seule à la prochaine partie enregistrée ; rien à faire.")
        return v
    texte = "Copie des résultats du {}.".format(copies[-1][17:27]) if copies else "Pas encore de résultats à sauvegarder."
    reglage = os.path.join(DOSSIER_PROJET, "outils-medias", "nuit", "dossier-sauvegarde.txt")
    try:
        with open(reglage, encoding="utf-8-sig") as f:
            dest = f.readline().strip().strip('"')
    except OSError:
        dest = ""
    if not dest:
        v.update(message=texte + " Sauvegarde complète du projet : non installée sur ce PC.")
        return v
    try:
        age = (time.time() - os.path.getmtime(dest)) / 86400
    except OSError:
        v.update(etat="orange", message=texte + " Dossier de sauvegarde complète introuvable : " + dest,
                 action="Branchez le disque de sauvegarde, ou corrigez outils-medias\\nuit\\dossier-sauvegarde.txt.")
        return v
    if age > 8:
        v.update(etat="orange", message=texte + " Dernière sauvegarde complète il y a {} jours.".format(int(age)),
                 action="Laissez le PC allumé (ou en veille) le dimanche soir, ou relancez outils-medias\\nuit\\installer-nuit.bat.")
    else:
        v.update(message=texte + " Sauvegarde complète à jour (il y a {} jour{}).".format(int(age), "s" if int(age) > 1 else ""))
    return v


# ---- Tableau de bord (enseignant.html) : production, installations, mise à jour ----
_MODULES = {}

def module_outil(nom, chemin_relatif):
    """Charge une seule fois un outil Python du dépôt (outils-docs/etat-production.py, outils-ecole/ecole.py)."""
    if nom not in _MODULES:
        import importlib.util
        spec = importlib.util.spec_from_file_location(nom, os.path.join(DOSSIER_PROJET, *chemin_relatif.split("/")))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _MODULES[nom] = m
    return _MODULES[nom]

_PRODUCTION = {"t": 0, "v": None}

def etat_production():
    """État de production des jeux, recalculé au plus une fois par minute (rien de personnel)."""
    if _PRODUCTION["v"] is not None and time.time() - _PRODUCTION["t"] < 60:
        return _PRODUCTION["v"]
    try:
        v = module_outil("etat_production", "outils-docs/etat-production.py").etat()
        v["ok"], v["direct"] = True, True
    except Exception as e:
        v = {"ok": False, "erreur": "état de production illisible ({})".format(e.__class__.__name__)}
    _PRODUCTION["t"], _PRODUCTION["v"] = time.time(), v
    return v

def role_installation():
    """principal (dépôt git du PC où l'on modifie les jeux), ecole (PC de l'école), nextcloud (copie Nextcloud), archive."""
    nextcloud = os.path.exists(os.path.join(DOSSIER_PROJET, "copie-nextcloud.txt"))
    appdata = os.environ.get("APPDATA", "")
    ecole = bool(appdata) and os.path.exists(os.path.join(appdata, "EscapeGames", "poste-ecole.txt"))
    git = os.path.isdir(os.path.join(DOSSIER_PROJET, ".git"))
    role = "ecole" if ecole else "nextcloud" if nextcloud else "principal" if git else \
        "archive" if os.path.exists(os.path.join(DOSSIER_PROJET, "version-installee.txt")) else "copie"
    return {"role": role, "ecole": ecole, "nextcloud": nextcloud, "git": git}

def nom_machine():
    return "".join(c if c.isalnum() or c in "-_" else "-" for c in (socket.gethostname() or "pc"))[:40] or "pc"

def fiche_installation():
    vj = lire_version_json()
    f = dict(role_installation(), machine=nom_machine(), numero=vj.get("numero"), date=vj.get("date"),
             texte=texte_numero(vj), commit=version_locale()[:12], vu=time.strftime("%Y-%m-%dT%H:%M"), dossier=DOSSIER_PROJET)
    return f

def noter_installation():
    """installations/<machine>.json dans le dossier des jeux (jamais publié) : sur une copie Nextcloud, cette fiche
    remonte jusqu'au PC principal, qui voit ainsi la version du PC de l'école."""
    try:
        d = os.path.join(DOSSIER_PROJET, "installations")
        os.makedirs(d, exist_ok=True)
        f = fiche_installation()
        f.pop("dossier", None)
        with open(os.path.join(d, f["machine"] + ".json.tmp"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump(f, fh, ensure_ascii=False)
        os.replace(os.path.join(d, f["machine"] + ".json.tmp"), os.path.join(d, f["machine"] + ".json"))
    except OSError:
        pass

def lire_fiches(dossier):
    fiches = []
    try:
        noms = sorted(n for n in os.listdir(os.path.join(dossier, "installations")) if n.endswith(".json"))
    except OSError:
        return fiches
    for n in noms[:20]:
        try:
            with open(os.path.join(dossier, "installations", n), encoding="utf-8") as fh:
                x = json.load(fh)
            if isinstance(x, dict):
                fiches.append({k: x.get(k) for k in ("machine", "role", "ecole", "nextcloud", "numero", "date", "texte", "commit", "vu")})
        except (OSError, ValueError):
            pass
    return fiches

def etat_installations():
    noter_installation()
    ici = fiche_installation()
    res = {"ok": True, "ici": ici, "fiches": [f for f in lire_fiches(DOSSIER_PROJET) if f.get("machine") != ici["machine"]],
           "nextcloud": None, "en_ligne": version_en_ligne()}
    if ici["role"] == "principal":
        try:
            E = module_outil("ecole", "outils-ecole/ecole.py")
            dest = E.dossier_nextcloud_par_defaut()
            nc = {"dossier": dest, "existe": os.path.isdir(dest), "version": E.lire_version(dest) if os.path.isdir(dest) else {}}
            try:
                with open(os.path.join(dest, ".copie-escape-games.json"), encoding="utf-8") as fh:
                    nc["copie_du"] = json.load(fh).get("date")
            except (OSError, ValueError):
                nc["copie_du"] = None
            nc["texte"] = texte_numero(nc["version"])
            res["nextcloud"] = nc
            res["fiches"] += [dict(f, via="nextcloud") for f in lire_fiches(dest) if f.get("machine") != ici["machine"]]
        except Exception:
            pass
    return res

MAJ = {"en_cours": False, "ok": None, "debut": "", "fin": "", "lignes": []}
MAJ_LOCK = threading.Lock()

def mettre_a_jour():
    """Met à jour CETTE installation (thread) ; le journal est lu par GET /api/mettre-a-jour."""
    import subprocess
    def dire(t):
        MAJ["lignes"].append(t)
    def git(*args):
        r = subprocess.run(["git", "-c", "gc.auto=0", "-c", "maintenance.auto=false"] + list(args), cwd=DOSSIER_PROJET,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=900)
        return r.returncode, r.stdout.decode("utf-8", "replace").strip()
    ok = False
    try:
        r = role_installation()
        if r["role"] == "principal":
            dire("PC principal : c'est la source des jeux. Je mets à jour la copie Nextcloud (version commitée).")
            E = module_outil("ecole", "outils-ecole/ecole.py")
            dest = E.dossier_nextcloud_par_defaut()
            if not os.path.isdir(dest):
                dire("Copie Nextcloud introuvable : " + dest)
                dire("Écrivez son chemin sur la 1re ligne de outils-ecole\\dossier-nextcloud.txt (Bloc-notes), puis recommencez.")
            else:
                c = E.synchroniser(DOSSIER_PROJET, dest, journal=lambda t: dire(t.strip()) if len(MAJ["lignes"]) < 60 else None)
                dire("Copie Nextcloud : {ecrits} fichier(s) copié(s), {identiques} identique(s), {deplaces} rangé(s) dans _a-supprimer.".format(**c))
                ok = not c.get("erreurs")
            dire("Site en ligne (GitHub Pages) : à publier vous-même, après relecture des jeux sensibles. Invite de commandes :")
            dire('cd /d "{}"  puis  git push origin escape-games'.format(DOSSIER_PROJET))
        elif r["nextcloud"]:
            dire("Copie Nextcloud : la mise à jour arrive par Nextcloud. Sur le PC principal, lancez mettre-a-jour-nextcloud.bat")
            dire("(ou ce même bouton dans son tableau de bord). Ensuite, relancez lancer.bat ici.")
            ok = True
        elif r["git"]:
            dire("Récupération de la dernière version (git fetch)...")
            c, t = git("fetch", "origin", "escape-games")
            if c != 0:
                dire("Pas de connexion à GitHub : version actuelle gardée. " + t[-300:])
            else:
                c, t = git("merge", "--ff-only", "origin/escape-games")
                dire(t[-600:] or "Déjà à jour.")
                ok = c == 0
                dire("Mise à jour faite : fermez la fenêtre noire du serveur puis double-clic sur lancer.bat." if ok
                     else "Mise à jour refusée (fichiers modifiés sur ce PC) : lancez diagnostic.bat et envoyez diagnostic.txt.")
        elif os.name == "nt" and os.path.exists(os.path.join(DOSSIER_PROJET, "outils-ecole", "maj-ecole.ps1")):
            dire("Téléchargement de la dernière version depuis GitHub (plusieurs minutes la première fois)...")
            p = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                                os.path.join(DOSSIER_PROJET, "outils-ecole", "maj-ecole.ps1")], cwd=DOSSIER_PROJET,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=3600)
            dire(p.stdout.decode("utf-8", "replace").strip()[-600:])
            ok = p.returncode == 0
            if ok:
                dire("Fermez la fenêtre noire du serveur puis double-clic sur lancer.bat pour utiliser la nouvelle version.")
        else:
            dire("Cette copie ne sait pas se mettre à jour seule : remplacez-la par une copie récente, ou installez git.")
    except Exception as e:
        dire("Erreur pendant la mise à jour : {}".format(e))
    _PRODUCTION["v"] = None
    MAJ.update(en_cours=False, ok=ok, fin=time.strftime("%H:%M:%S"))


class Handler(BaseHTTPRequestHandler):
    """Sert les fichiers statiques + expose /api/* pour la synchro."""

    def log_message(self, format, *args):
        # Log minimal
        pass

    # ---- Routage ----
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path.startswith("/api/"):
            self.router_api("GET", path, {})
        else:
            self.servir_fichier(path)

    def do_HEAD(self):
        # Utilisé par verifier.html pour savoir si un média existe,
        # et combien il pèse, sans le télécharger.
        self.servir_fichier(urlparse(self.path).path, corps=False)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            longueur = int(self.headers.get("Content-Length", 0))
        except ValueError:
            longueur = 0
        if longueur > TAILLE_MAX_REQUETE:
            self.send_error(413, "Requête trop volumineuse")
            return
        corps = self.rfile.read(longueur).decode("utf-8", errors="replace") if longueur else ""
        try:
            data = json.loads(corps) if corps else {}
        except Exception:
            data = {}
        if path.startswith("/api/"):
            self.router_api("POST", path, data)
        else:
            self.send_error(404)

    # ---- Fichiers statiques ----
    TYPES = {
        ".html": "text/html; charset=utf-8",
        ".css":  "text/css; charset=utf-8",
        ".js":   "application/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".webmanifest": "application/manifest+json; charset=utf-8",
        ".png":  "image/png",
        ".jpg":  "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif":  "image/gif",
        ".svg":  "image/svg+xml",
        ".ico":  "image/x-icon",
        ".wav":  "audio/wav",
        ".mp3":  "audio/mpeg",
        ".ogg":  "audio/ogg",
        # ---- Vidéo (décors filmés et cinématiques) ----
        ".mp4":  "video/mp4",
        ".webm": "video/webm",
        ".ogv":  "video/ogg",
        ".m4v":  "video/mp4",
        # ---- Sous-titres ----
        ".vtt":  "text/vtt; charset=utf-8",
        ".srt":  "application/x-subrip; charset=utf-8",
        # ---- Polices ----
        ".woff":  "font/woff",
        ".woff2": "font/woff2",
        ".ttf":   "font/ttf",
    }

    # Les vidéos sont envoyées par morceaux plutôt qu'en un bloc :
    # cela évite de charger un fichier de plusieurs centaines de Mo en mémoire.
    TAILLE_MORCEAU = 256 * 1024

    def servir_fichier(self, path, corps=True):
        if path == "/" or path == "":
            path = "/index.html"

        # Décodage des URL (les dossiers peuvent contenir des espaces)
        path = unquote(path).lstrip("/")
        if chemin_prive(path):
            self.send_error(404, "Fichier non trouvé")
            return

        # Sécurité : interdire toute remontée hors du dossier du projet
        racine = os.path.abspath(".")
        chemin = os.path.abspath(os.path.join(racine, path))
        if not chemin.startswith(racine + os.sep) and chemin != racine:
            self.send_error(403, "Accès refusé")
            return
        if os.path.isdir(chemin):
            chemin = os.path.join(chemin, "index.html")

        try:
            taille = os.path.getsize(chemin)
        except OSError:
            self.send_error(404, "Fichier non trouvé : " + path)
            return

        ext = os.path.splitext(chemin)[1].lower()
        ctype = self.TYPES.get(ext, "application/octet-stream")

        # ---- Requête partielle (Range) ----
        # Indispensable pour la vidéo : sans elle, le navigateur ne peut
        # ni se positionner dans le film, ni démarrer la lecture avant
        # d'avoir tout téléchargé.
        debut, fin = 0, taille - 1
        partiel = False
        entete_range = self.headers.get("Range")
        if entete_range and entete_range.startswith("bytes="):
            plage = entete_range[6:].split(",")[0].strip()
            try:
                d, _, f = plage.partition("-")
                if d:
                    debut = int(d)
                    if f:
                        fin = min(int(f), taille - 1)
                else:
                    # Forme « bytes=-500 » : les 500 derniers octets
                    debut = max(0, taille - int(f))
                if debut > fin or debut >= taille:
                    self.send_response(416)
                    self.send_header("Content-Range", "bytes */%d" % taille)
                    self.end_headers()
                    return
                partiel = True
            except ValueError:
                debut, fin, partiel = 0, taille - 1, False

        longueur = fin - debut + 1
        self.send_response(206 if partiel else 200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(longueur))
        self.send_header("Accept-Ranges", "bytes")
        if partiel:
            self.send_header("Content-Range", "bytes %d-%d/%d" % (debut, fin, taille))
        # Les médias sont volumineux et ne changent pas : on les met en cache.
        if ctype.startswith(("video/", "audio/", "image/", "font/")):
            self.send_header("Cache-Control", "public, max-age=3600")
        else:
            self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        if not corps:
            return

        try:
            with open(chemin, "rb") as f:
                f.seek(debut)
                restant = longueur
                while restant > 0:
                    morceau = f.read(min(self.TAILLE_MORCEAU, restant))
                    if not morceau:
                        break
                    self.wfile.write(morceau)
                    restant -= len(morceau)
        except (BrokenPipeError, ConnectionResetError):
            # L'élève a changé de page en cours de lecture : normal.
            pass
        except Exception:
            pass

    def lire_difficulte(self):
        try:
            with open(FICHIER_DIFFICULTE, encoding="utf-8") as f:
                d = json.load(f)
            return d if isinstance(d, dict) else {}
        except (OSError, ValueError):
            return {}

    # ---- API REST ----
    def router_api(self, methode, path, data):
        if path == "/api/etat" and methode == "POST":
            # L'élève envoie son état
            equipe = data.get("equipe", "Anonyme")
            with LOCK:
                ETATS_EQUIPES[equipe] = {
                    "equipe": equipe,
                    # Quel escape game ? "declaration" (défaut) ou "tour-du-monde".
                    # Permet à chaque tableau de bord de n'afficher que ses équipes.
                    "jeu": data.get("jeu", "declaration"),
                    "niveau": data.get("niveau"),
                    "salle": data.get("salle"),
                    "score": data.get("score"),
                    "fragments": data.get("fragments", []),
                    "msEcoules": data.get("msEcoules"),
                    "enPause": data.get("enPause", False),
                    "fini": data.get("fini", False),
                    # Champs facultatifs envoyés par le tronc commun (commun/js/sync.js)
                    "enigme": data.get("enigme"),
                    "palier": data.get("palier"),
                    "delaiMin": data.get("delaiMin", 0),
                    "enigmesReussies": data.get("enigmesReussies"),
                    "indicesTotal": data.get("indicesTotal"),
                    "pouces": data.get("pouces", 0),      # N13 : coups de pouce de l'enseignant reçus
                    "passees": data.get("passees", 0),    # N15 : énigmes passées avec le joker
                    "timestamp": time.time()
                }
                # Récupérer d'éventuelles commandes prof en attente
                cmd = COMMANDES_PROF.pop(equipe, None)
            self.json_reponse({"ok": True, "commande": cmd})
        elif path == "/api/resultat" and methode == "POST":
            # Compte-rendu d'une partie (commun/js/compte-rendu.js et journal.js des jeux immersifs).
            # Ouvert aux ordinateurs des élèves : c'est ce qui rend l'enregistrement automatique.
            valide = resultat_valide(data)
            ecrites, total = enregistrer_resultats([data]) if valide else (0, len(lire_resultats()))
            self.json_reponse({"ok": valide and ecrites >= 0, "ajoutees": max(ecrites, 0), "total": total})
        elif path == "/api/difficulte" and methode == "GET":
            # N20 : réglages de difficulté énigme par énigme, posés depuis prof.html : {"jeu": {"1-2": 1, ...}}
            jeu = (parse_qs(urlparse(self.path).query).get("jeu") or [""])[0]
            with LOCK:
                tout = self.lire_difficulte()
            self.json_reponse({"jeu": jeu, "valeurs": tout.get(jeu, {}) if jeu else tout})
        elif path == "/api/difficulte" and methode == "POST":
            # Réservé à l'ordinateur de l'enseignant (comme l'éditeur d'énigmes)
            jeu = str(data.get("jeu", ""))
            valeurs = data.get("valeurs", {})
            if self.client_address[0] not in ("127.0.0.1", "::1"):
                self.json_reponse({"ok": False, "erreur": "réglage réservé à l'ordinateur qui a lancé le serveur"})
            elif not jeu or not isinstance(valeurs, dict):
                self.json_reponse({"ok": False, "erreur": "demande incomplète"})
            else:
                propres = {}
                for cle, v in valeurs.items():
                    try:
                        n = int(v)
                    except (TypeError, ValueError):
                        continue
                    if n != 0 and -2 <= n <= 2:
                        propres[str(cle)] = n
                with LOCK:
                    tout = self.lire_difficulte()
                    if propres:
                        tout[jeu] = propres
                    else:
                        tout.pop(jeu, None)
                    with open(FICHIER_DIFFICULTE, "w", encoding="utf-8") as f:
                        json.dump(tout, f, ensure_ascii=False, indent=1)
                self.json_reponse({"ok": True, "valeurs": propres})
        elif path == "/api/enigmes" and methode == "POST":
            # Éditeur d'énigmes (editeur.html, D4) : écrit <jeu>/assets/data/enigmes.json.
            # Réservé à l'ordinateur de l'enseignant (127.0.0.1) : les postes élèves ne peuvent rien écrire.
            jeu = data.get("jeu", "")
            if self.client_address[0] not in ("127.0.0.1", "::1"):
                self.json_reponse({"ok": False, "erreur": "enregistrement réservé à l'ordinateur qui a lancé le serveur"})
            elif jeu not in ("melanges", "objets-techniques", "station-meteo", "chateau-fort", "moyen-age-abbaye", "constitution", "versailles", "renaissance", "alimentation", "lumiere", "etats-matiere", "mouvement", "traite-colonies"):
                self.json_reponse({"ok": False, "erreur": "jeu inconnu"})
            else:
                try:
                    contenu = data.get("contenu", "")
                    if not isinstance(json.loads(contenu).get("salles"), list):
                        raise ValueError("pas de salles")
                    cible = os.path.join(jeu, "assets", "data", "enigmes.json")
                    sauvegarde = cible + ".avant-" + time.strftime("%Y%m%d-%H%M%S")
                    with open(cible, encoding="utf-8") as f:
                        ancien = f.read()
                    with open(sauvegarde, "w", encoding="utf-8", newline="\n") as f:
                        f.write(ancien)
                    with open(cible, "w", encoding="utf-8", newline="\n") as f:
                        f.write(contenu)
                    self.json_reponse({"ok": True, "sauvegarde": os.path.basename(sauvegarde)})
                except (ValueError, AttributeError, OSError) as e:
                    self.json_reponse({"ok": False, "erreur": "fichier refusé : " + str(e)})
        elif path == "/api/resultats" and methode == "GET":
            # Toutes les parties gardées sur cet ordinateur (lues par resultats.html) : réservé à l'enseignant
            if not self.reserve_enseignant():
                return
            liste = lire_resultats()
            self.json_prive({"resultats": liste, "total": len(liste)})
        elif path == "/api/resultats" and methode == "POST":
            # Parties importées (fichiers des Chromebooks, texte collé…) : gardées dans le même fichier
            if not self.reserve_enseignant():
                return
            lot = data.get("resultats") if isinstance(data, dict) else None
            if not isinstance(lot, list):
                self.json_prive({"ok": False, "erreur": "liste « resultats » attendue"}, 400)
                return
            ecrites, total = enregistrer_resultats(lot[:5000])
            self.json_prive({"ok": ecrites >= 0, "ajoutees": max(ecrites, 0), "total": total})
        elif path == "/api/stockage" and methode == "GET":
            if not self.reserve_enseignant():
                return
            self.json_prive(infos_stockage())
        elif path == "/api/seance" and methode == "GET":
            # Jeu du jour (A1) : lu par l'accueil des élèves ; « local » = c'est l'ordinateur de l'enseignant
            s = lire_seance()
            if s:
                s = dict(s, adresse=adresse_jeu(s["jeu"]))
            self.json_prive({"ok": True, "seance": s, "local": est_adresse_locale(self.client_address[0])})
        elif path == "/api/seance" and methode == "POST":
            # Fixer ou terminer la séance : réservé à l'enseignant (ordinateur du serveur)
            if not self.reserve_enseignant():
                return
            if not isinstance(data, dict) or data.get("fin") or not data.get("jeu"):
                self.json_prive({"ok": ecrire_seance(None), "seance": None})
                return
            jeu = id_jeu_valide(data.get("jeu"))
            if not jeu:
                self.json_prive({"ok": False, "erreur": "jeu inconnu"}, 400)
                return
            grade = str(data.get("grade") or "").strip().lower()
            if grade not in GRADES_IMMERSIFS:
                grade = ""
            s = {"jeu": jeu, "grade": grade, "titre": str(data.get("titre") or "")[:120],
                 "depuis": time.strftime("%Y-%m-%dT%H:%M:%S")}
            ok = ecrire_seance(s)
            self.json_prive({"ok": ok, "seance": dict(s, adresse=adresse_jeu(jeu))} if ok else {"ok": False, "erreur": "écriture impossible dans " + DOSSIER_DONNEES}, 200 if ok else 500)
        elif path == "/api/relectures" and methode == "GET":
            if not self.reserve_enseignant():
                return
            self.json_prive({"ok": True, "relectures": lire_relectures()})
        elif path == "/api/relectures" and methode == "POST":
            if not self.reserve_enseignant():
                return
            d = data if isinstance(data, dict) else {}
            ok = noter_relecture(d.get("id"), str(d.get("e") or ""), d.get("n"))
            self.json_prive({"ok": ok}, 200 if ok else 400)
        elif path == "/api/sante" and methode == "GET":
            # Feu vert avant la séance (A4) : réservé à l'enseignant
            if not self.reserve_enseignant():
                return
            self.json_prive(etat_sante())
        elif path == "/api/equipes" and methode == "GET":
            # Le prof récupère tous les états
            with LOCK:
                self.json_reponse({"equipes": list(ETATS_EQUIPES.values())})
        elif path == "/api/commande" and methode == "POST":
            # Le prof envoie une commande à une équipe (ou toutes)
            equipe = data.get("equipe", "*")
            cmd = data.get("commande", {})
            with LOCK:
                if equipe == "*":
                    for eq in list(ETATS_EQUIPES.keys()):
                        COMMANDES_PROF[eq] = cmd
                else:
                    COMMANDES_PROF[equipe] = cmd
            self.json_reponse({"ok": True})
        elif path == "/api/fichiers" and methode == "GET":
            # Inventaire des médias déposés, lu par verifier.html :
            # { "declaration/assets/videos/salle4.mp4": taille, ... }
            fichiers = {}
            for jeu in ("declaration", "tour-du-monde", "mission-geo", "constitution", "station-meteo", "melanges", "moyen-age-abbaye", "objets-techniques", "chateau-fort", "versailles", "renaissance", "alimentation", "lumiere", "etats-matiere", "mouvement", "traite-colonies"):
                for racine, _, noms in os.walk(os.path.join(jeu, "assets")):
                    for nom in noms:
                        chemin = os.path.join(racine, nom)
                        fichiers[chemin.replace(os.sep, "/")] = os.path.getsize(chemin)
            self.json_reponse({"fichiers": fichiers})
        elif path == "/api/production" and methode == "GET":
            # État de production des jeux (tableau de bord) : aucune donnée d'élève
            self.json_prive(etat_production())
        elif path == "/api/installations" and methode == "GET":
            if not self.reserve_enseignant():
                return
            self.json_prive(etat_installations())
        elif path == "/api/mettre-a-jour":
            # Bouton « Mettre à jour cette installation » : réservé à ce PC ; GET = où en est la mise à jour
            if not self.reserve_enseignant():
                return
            if methode == "POST":
                with MAJ_LOCK:
                    if not MAJ["en_cours"]:
                        MAJ.update(en_cours=True, ok=None, debut=time.strftime("%H:%M:%S"), fin="", lignes=[])
                        threading.Thread(target=mettre_a_jour, daemon=True).start()
            self.json_prive(dict(MAJ, ok_requete=True, role=role_installation()["role"]))
        elif path == "/api/version" and methode == "GET":
            # Version installée (lue par le tableau de bord, diagnostic.bat, le lanceur)
            vj = lire_version_json()
            self.json_prive({"ok": True, "numero": vj.get("numero"), "date": vj.get("date"), "texte": texte_numero(vj),
                             "commit": version_locale()[:40], "commit_precedent": vj.get("commit_precedent", ""),
                             "nextcloud": os.path.exists(os.path.join(DOSSIER_PROJET, "copie-nextcloud.txt"))})
        elif path == "/api/arreter" and methode == "POST":
            # Arrêt propre, demandé par lancer.bat / demarrer-ecole.bat avant de relancer : réservé à ce PC
            if not self.reserve_enseignant():
                return
            self.json_prive({"ok": True})
            threading.Thread(target=arreter_serveur, daemon=True).start()
        elif path == "/api/info" and methode == "GET":
            self.json_reponse({
                "serveur": "Escape games pédagogiques CM1-CM2",
                "ip": get_ip_locale(),
                "port": PORT,
                "equipes_connectees": len(ETATS_EQUIPES),
                "local": est_adresse_locale(self.client_address[0])
            })
        elif path == "/api/export" and methode == "GET":
            # Export CSV simplifié
            with LOCK:
                lignes = ["jeu,equipe,niveau,salle,score,fragments,temps_min,fini"]
                for e in ETATS_EQUIPES.values():
                    lignes.append('{},"{}",{},{},{},{},{},{}'.format(
                        e.get("jeu",""),
                        e.get("equipe",""),
                        e.get("niveau",""),
                        e.get("salle",""),
                        e.get("score",0),
                        len(e.get("fragments",[])),
                        round((e.get("msEcoules",0) or 0)/60000, 1),
                        "oui" if e.get("fini") else "non"
                    ))
            csv = "\n".join(lignes)
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="scores_equipes.csv"')
            self.end_headers()
            self.wfile.write(csv.encode("utf-8"))
        else:
            self.send_error(404, "API inconnue : " + path)

    def reserve_enseignant(self):
        """Résultats des élèves : lisibles seulement depuis l'ordinateur qui fait tourner le serveur."""
        if est_adresse_locale(self.client_address[0]):
            return True
        self.json_prive({"ok": False, "erreur": "réservé à l'ordinateur de l'enseignant (ouvrez http://127.0.0.1:{}/resultats.html sur ce PC)".format(PORT)}, 403)
        return False

    def json_prive(self, obj, code=200):
        """Données personnelles : pas d'en-tête « Access-Control-Allow-Origin », jamais mises en cache."""
        corps = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corps)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corps)

    def json_reponse(self, obj):
        corps = json.dumps(obj).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corps)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(corps)


class ServeurMultiThread(ThreadingMixIn, HTTPServer):
    """Un thread par requête.

    Indispensable depuis l'ajout de la vidéo : une classe entière peut
    télécharger des décors filmés en même temps, sans jamais bloquer les
    petites requêtes /api/etat qui font vivre le tableau de bord du prof.
    """
    daemon_threads = True
    # Windows : SO_REUSEADDR y permet à DEUX serveurs d'écouter le même port (l'ancien continuait alors
    # à servir une vieille version). On le réserve à Linux/Mac et on demande l'usage exclusif sous Windows.
    allow_reuse_address = os.name != "nt"

    def server_bind(self):
        if os.name == "nt" and hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            try:
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
            except OSError:
                pass
        HTTPServer.server_bind(self)


SERVEUR = {"v": None}

def arreter_serveur():
    time.sleep(0.3)   # laisse partir la réponse
    s = SERVEUR["v"]
    if s is not None:
        s.shutdown()


def preparer_console():
    """Autorise les emojis dans la console Windows.

    Sans cela, une console configurée en cp1252 (ou une sortie redirigée
    vers un fichier) fait planter le serveur au démarrage sur le premier
    caractère accentué ou emoji de la bannière.
    """
    for flux in (sys.stdout, sys.stderr):
        try:
            flux.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def main():
    preparer_console()
    ip = get_ip_locale()
    print("=" * 62)
    print("  ESCAPE GAMES PÉDAGOGIQUES — Serveur local · CM1-CM2")
    print("=" * 62)
    print()
    print("  ✅ Serveur démarré sur le port {} (multi-thread, vidéo activée)".format(PORT))
    print("  🏷️  Version des jeux : {}".format(texte_numero(lire_version_json()) or "inconnue (pas de version.json)"))
    print("  🗂️  Résultats de la classe : {}".format(os.path.abspath(FICHIER_RESULTATS)))
    print()
    print("  🏠 ACCUEIL (tous les jeux)  →  http://{}:{}/".format(ip, PORT))
    print("  📺 CLASSEMENT À PROJETER   →  http://{}:{}/classement.html".format(ip, PORT))
    print("  🔳 QR CODE DES ÉLÈVES       →  http://127.0.0.1:{}/tableau.html  (à projeter)".format(PORT))
    print("  👩‍🏫 TABLEAU DE BORD         →  http://127.0.0.1:{}/enseignant.html  (séance, équipes, mises à jour)".format(PORT))
    print()
    print("  📱 ADRESSES À DONNER AUX ÉLÈVES :")
    print("     Révolution française  →  http://{}:{}/declaration/".format(ip, PORT))
    print("     Tour du Monde (géo.)  →  http://{}:{}/tour-du-monde/".format(ip, PORT))
    print("     Mission géographique  →  http://{}:{}/mission-geo/".format(ip, PORT))
    print("     Constitution (EMC)    →  http://{}:{}/constitution/".format(ip, PORT))
    print("     Moyen Âge (histoire)  →  http://{}:{}/moyen-age-abbaye/".format(ip, PORT))
    print("     Station météo (sc.)   →  http://{}:{}/station-meteo/".format(ip, PORT))
    print("     Mélanges (sciences)   →  http://{}:{}/melanges/".format(ip, PORT))
    print("     Objets techniques     →  http://{}:{}/objets-techniques/".format(ip, PORT))
    print("     Château fort (hist.)  →  http://{}:{}/chateau-fort/".format(ip, PORT))
    print("     Versailles (hist.)    →  http://{}:{}/versailles/".format(ip, PORT))
    print("     Renaissance (hist.)   →  http://{}:{}/renaissance/".format(ip, PORT))
    print("     Alimentation (sc.)    →  http://{}:{}/alimentation/".format(ip, PORT))
    print("     Lumière (sciences)    →  http://{}:{}/lumiere/".format(ip, PORT))
    print("     États de la matière   →  http://{}:{}/etats-matiere/".format(ip, PORT))
    print("     Mouvement (sciences)  →  http://{}:{}/mouvement/".format(ip, PORT))
    print("     Archives du port      →  http://{}:{}/traite-colonies/".format(ip, PORT))
    print("     Immersifs n°13 à 15   →  http://{}:{}/immersifs/grandes-explorations/ , electricite/ , naissances-animaux/".format(ip, PORT))
    print("     Immersif n°17        →  http://{}:{}/immersifs/vivant-ecosystemes/".format(ip, PORT))
    print("     Immersif n°19        →  http://{}:{}/immersifs/grande-guerre/".format(ip, PORT))
    print("     Immersif n°20        →  http://{}:{}/immersifs/seconde-guerre/".format(ip, PORT))
    print("     Immersif n°23        →  http://{}:{}/immersifs/terre-active/".format(ip, PORT))
    print()
    print("  👨‍🏫 TABLEAUX DE BORD ENSEIGNANT :")
    print("     http://127.0.0.1:{}/declaration/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/tour-du-monde/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/constitution/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/moyen-age-abbaye/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/station-meteo/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/melanges/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/objets-techniques/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/chateau-fort/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/versailles/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/renaissance/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/alimentation/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/lumiere/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/etats-matiere/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/mouvement/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/traite-colonies/prof.html".format(PORT))
    print()
    print("  🔍 VÉRIFICATION (médias, accès direct aux énigmes) :")
    print("     http://127.0.0.1:{}/verifier.html".format(PORT))
    print()
    print("  💾 RÉSULTATS DES ÉLÈVES — enregistrés automatiquement, rien à faire :")
    print("     {} partie(s) déjà gardée(s)".format(len(lire_resultats())))
    print("     Excel   : {}".format(FICHIER_RESULTATS_CSV))
    print("     Copies  : {} (une par jour)".format(DOSSIER_SAUVEGARDES))
    print("     📊 Voir les résultats  →  http://127.0.0.1:{}/resultats.html".format(PORT))
    print()
    print("  ⚠️  Pour être enregistrés ici, les élèves doivent jouer depuis :")
    print("        http://{}:{}/".format(ip, PORT))
    print("     (jouer depuis GitHub : le résultat reste dans le Chromebook ; voir resultats.html)")
    print()
    print("  ⌨️  Ctrl+C pour arrêter le serveur.")
    print()
    print("-" * 62)
    copie_de_securite()
    try:
        serveur = ServeurMultiThread(("0.0.0.0", PORT), Handler)
    except OSError as e:
        print("\n  ❌ Impossible d'ouvrir le port {} : il est déjà utilisé ({}).".format(PORT, e))
        print("     Un autre serveur des jeux tourne sans doute déjà : fermez sa fenêtre,")
        print("     ou relancez lancer.bat (il ferme l'ancien serveur tout seul).\n")
        sys.exit(3)
    SERVEUR["v"] = serveur
    noter_installation()
    try:
        serveur.serve_forever()
        print("\n  Serveur arrêté (un nouveau lancement l'a remplacé).\n")
    except KeyboardInterrupt:
        print("\n\nServeur arrêté. À bientôt !\n")
    serveur.server_close()


if __name__ == "__main__":
    main()
