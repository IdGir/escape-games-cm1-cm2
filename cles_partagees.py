"""cles_partagees.py — Clés API communes aux applications de l'écosystème.

LE PROBLÈME
Cahier Journal, Correcteur Pédagogique et Notes & Suivi savent chacun parler à
une IA, et chacun demandait sa propre clé : une seule clé DeepSeek ou Albert
devait être collée dans trois écrans de réglages différents, puis re-collée
dans les trois à chaque changement.

LA SOLUTION
Un fichier unique, hors des dossiers d'application (il survit donc aux mises à
jour), lu par les trois. Emplacement par défaut :
  Windows : %APPDATA%\\EcosystemeEnseignant\\cles-ia.json
  macOS   : ~/Library/Application Support/EcosystemeEnseignant/cles-ia.json
  Linux   : ~/.config/ecosysteme-enseignant/cles-ia.json
Variable d'environnement ECOLE_CLES_IA pour imposer un autre chemin.

RÈGLE DE PRIORITÉ
  1. la clé saisie dans CETTE application (elle gagne toujours) ;
  2. le fichier partagé ;
  3. rien — l'application bascule sur ses règles hors ligne, comme avant.
Aucune configuration existante n'est donc cassée : ce fichier ne sert que de
repli quand le Correcteur n'a pas sa propre clé.

CE MODULE NE FAIT QUE LIRE. C'est le Cahier Journal (qui a un backend et un
écran de réglages complet) qui écrit le fichier.
"""
import json
import os

NOM_FICHIER = "cles-ia.json"


def chemin():
    """Emplacement du fichier partagé, selon le système."""
    force = os.environ.get("ECOLE_CLES_IA")
    if force:
        return force
    if os.name == "nt":
        base = os.environ.get("APPDATA") or os.path.expanduser(r"~\AppData\Roaming")
        return os.path.join(base, "EcosystemeEnseignant", NOM_FICHIER)
    maison = os.path.expanduser("~")
    mac = os.path.join(maison, "Library", "Application Support")
    if os.path.isdir(mac):
        return os.path.join(mac, "EcosystemeEnseignant", NOM_FICHIER)
    return os.path.join(maison, ".config", "ecosysteme-enseignant", NOM_FICHIER)


def _services():
    """Contenu du fichier. Toujours un dictionnaire, jamais d'exception."""
    try:
        with open(chemin(), "r", encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        # Fichier absent (cas normal tant que rien n'est réglé) ou illisible :
        # on se tait, l'appelant retombera sur son propre réglage.
        return {}
    if not isinstance(d, dict):
        return {}
    s = d.get("services", d)
    return s if isinstance(s, dict) else {}


def _champ(service, nom):
    s = _services().get(service)
    if not s:
        return ""
    if isinstance(s, str):
        return s.strip() if nom == "cle" else ""
    return str(s.get(nom) or "").strip()


def cle(service):
    """Clé partagée d'un service ('deepseek', 'albert', 'openrouter'…) ou ""."""
    return _champ(service, "cle")


def url(service):
    """Adresse de base partagée d'un service, ou ""."""
    return _champ(service, "url")


def modele(service):
    """Modèle par défaut partagé pour un service, ou ""."""
    return _champ(service, "modele")


def existe():
    try:
        return os.path.isfile(chemin())
    except Exception:
        return False


def etat():
    """Résumé pour l'écran Réglages : quels services ont une clé, sans la révéler."""
    s = _services()
    return {
        "chemin": chemin(),
        "existe": existe(),
        "services": {
            k: {"a_une_cle": bool(cle(k)), "url": url(k)}
            for k in s
        },
    }
