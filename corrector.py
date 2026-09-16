"""Le correcteur : produire le CORRIGÉ d'un texte, quel qu'il soit.

C'est la procédure de l'application d'origine, rétablie.

Pourquoi c'est central
----------------------
Le repérage des erreurs de l'application repose sur une comparaison avec un
corrigé (`verification.py`) : un mot identique au corrigé n'est JAMAIS signalé,
donc aucun faux positif n'est possible. Encore faut-il disposer d'un corrigé.

Pour un texte fabriqué par l'application, on l'a d'office. Mais pour un texte
que l'élève vient de taper, personne ne le connaît — sauf un correcteur.
D'où ce module : il corrige n'importe quel texte, et le reste de la chaîne
fonctionne alors à l'identique, avec la même garantie.

Trois moteurs, dans cet ordre de repli
--------------------------------------
  1. DeepSeek   — cloud, clé API requise
  2. Ollama     — local, aucune clé, aucune donnée ne sort de l'ordinateur
  3. Règles     — `correction_engine.py`, toujours disponible, jamais bloquant

Un garde-fou rejette tout corrigé qui reformule au lieu de corriger : mieux
vaut retomber sur les règles que renvoyer l'élève à un repérage faussé.
"""
import json
import urllib.request

import correction_engine as ce
import ia_client
import verification as vf
from config_manager import config
from theme import CATEGORIES, LIBELLES_CATEGORIES

TIMEOUT_CLOUD = 45
TIMEOUT_LOCAL = 180


class Resultat:
    """Ce que renvoie le correcteur."""

    def __init__(self, corrige, erreurs, moteur, message, fiable):
        self.corrige = corrige      # texte corrigé (jamais montré à l'élève)
        self.erreurs = erreurs      # [(fautif, correct, categorie), ...]
        self.moteur = moteur        # "deepseek" | "ollama" | "regles"
        self.message = message
        self.fiable = fiable        # True si un corrigé de référence est disponible

    def categories(self):
        return {(f.lower(), j.lower()): c for f, j, c in self.erreurs}


# ============================================================================
#  Le prompt
# ============================================================================
def _prompt(texte: str) -> str:
    cats = ", ".join(f"{c} ({LIBELLES_CATEGORIES[c]})" for c in CATEGORIES)
    return (
        "Tu es un enseignant de français à l'école primaire. Corrige le texte "
        "d'un élève ci-dessous.\n\n"
        "RÈGLES IMPÉRATIVES :\n"
        "1. Corrige UNIQUEMENT les fautes. Ne reformule rien, ne réécris rien, "
        "n'améliore pas le style. Garde exactement les mêmes phrases, les mêmes "
        "mots et le même ordre. Respecte le sens et le style de l'élève.\n"
        "2. Le texte corrigé doit avoir pratiquement le même nombre de mots que "
        "l'original.\n"
        f"3. Classe chaque erreur dans EXACTEMENT une de ces 8 catégories : {cats}.\n"
        "4. Réponds UNIQUEMENT par un objet JSON, sans aucun autre texte, sans "
        "balises Markdown.\n\n"
        'FORMAT : {"texte_corrige": "...", "erreurs": [{"fautif": "mot tel qu\'il '
        'est écrit", "correct": "mot juste", "categorie": "accord"}]}\n\n'
        f"TEXTE DE L'ÉLÈVE :\n{texte}"
    )


def _extraire_json(brut: str) -> dict:
    t = brut.strip().replace("```json", "").replace("```", "").strip()
    d, f = t.find("{"), t.rfind("}")
    if d == -1 or f == -1:
        raise ValueError("réponse illisible")
    return json.loads(t[d:f + 1])


# ============================================================================
#  Appels aux moteurs
# ============================================================================
def _deepseek(prompt: str) -> str:
    cle = (config.get("ia_cle_api") or "").strip()
    if not cle:
        raise RuntimeError("aucune clé API DeepSeek renseignée")
    corps = json.dumps({
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,          # correction : on ne veut aucune fantaisie
        "max_tokens": 2000,
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.deepseek.com/chat/completions", data=corps,
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {cle}"})
    with urllib.request.urlopen(req, timeout=TIMEOUT_CLOUD) as r:
        d = json.loads(r.read().decode("utf-8"))
    return d["choices"][0]["message"]["content"]


def _ollama(prompt: str) -> str:
    url = (config.get("ia_url_ollama") or "").rstrip("/") + "/api/generate"
    corps = json.dumps({
        "model": config.get("ia_modele_ollama"),
        "prompt": prompt, "stream": False,
        "options": {"temperature": 0.0},
    }).encode("utf-8")
    req = urllib.request.Request(url, data=corps,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT_LOCAL) as r:
        return json.loads(r.read().decode("utf-8")).get("response", "")


# ============================================================================
#  Garde-fou
# ============================================================================
def corrige_plausible(original: str, corrige: str) -> bool:
    """Le corrigé doit être le MÊME texte, seulement réparé.

    Si le modèle a reformulé, la comparaison mot à mot n'a plus de sens : on
    préfère alors les règles, qui sont modestes mais honnêtes.
    """
    a, b = len(original.split()), len(corrige.split())
    if not a or not b:
        return False
    if not 0.80 <= b / a <= 1.25:
        return False
    # Au moins la moitié des mots doivent être communs.
    ma, mb = set(original.lower().split()), set(corrige.lower().split())
    return len(ma & mb) >= 0.5 * len(ma)


def _nettoyer_erreurs(brutes):
    out = []
    for e in brutes or []:
        if not isinstance(e, dict):
            continue
        f = (e.get("fautif") or "").strip()
        j = (e.get("correct") or "").strip()
        c = (e.get("categorie") or "").strip().lower()
        if not f or not j:
            continue
        if c not in CATEGORIES:
            c = vf.categoriser(f, j)      # catégorie fantaisiste : on redéduit
        out.append((f, j, c))
    return out


# ============================================================================
#  Point d'entrée
# ============================================================================
def corriger(texte: str) -> Resultat:
    """Corrige un texte. Ne lève jamais d'exception : renvoie toujours un Resultat."""
    texte = (texte or "").strip()
    if not texte:
        return Resultat("", [], "regles", "Texte vide.", False)

    if config.get("ia_active"):
        moteur = config.get("ia_moteur", "deepseek")
        try:
            brut = ia_client.appeler(_prompt(texte), temperature=0.0, max_tokens=2000,
                                     tache="correction")
            d = _extraire_json(brut)
            corrige = (d.get("texte_corrige") or "").strip()
            erreurs = _nettoyer_erreurs(d.get("erreurs"))

            if corrige and corrige_plausible(texte, corrige):
                return Resultat(corrige, erreurs, moteur,
                                f"Texte corrigé par {ia_client.nom_moteur(moteur)}.", True)
            raise ValueError("le corrigé reformule au lieu de corriger")

        except Exception as e:
            r = _par_regles(texte)
            r.message = (f"Correcteur IA indisponible ({type(e).__name__}) — "
                         f"repérage par règles.")
            return r

    return _par_regles(texte)


def _par_regles(texte: str) -> Resultat:
    """Repli hors ligne : aucun corrigé complet, mais des erreurs sûres."""
    sigs = ce.analyser(texte)
    erreurs = [(s.mot, s.suggestion, s.categorie)
               for s in ce.certaines(sigs) if s.suggestion]
    return Resultat("", erreurs, "regles",
                    "Repérage hors ligne (aucune IA active).", False)


def analyser(texte: str, reference: str = "", categories: dict | None = None):
    """Le repérage utilisé par le module élève.

    · Si un corrigé de référence est fourni → comparaison, zéro faux positif.
    · Sinon → règles, avec la distinction erreur certaine / point de vigilance.
    """
    if reference and reference.strip():
        return vf.analyser_avec_reference(texte, reference, categories or {})

    sigs = ce.analyser(texte)
    if not config.get("vigilance_active", True):
        sigs = ce.certaines(sigs)
    return sigs


def tester_moteur():
    """Vérifie le moteur configuré. Renvoie (ok, message)."""
    essai = "Les enfant joue dans la cour et il son content."
    if not config.get("ia_active"):
        return False, "Aucune IA active : l'application utilise ses règles hors ligne."
    r = corriger(essai)
    if r.fiable:
        return True, (f"{r.message}\n\nEssai : « {essai} »\n"
                      f"→ « {r.corrige} »\n{len(r.erreurs)} erreur(s) classée(s).")
    return False, r.message
