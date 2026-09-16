"""transcription.py — Compter automatiquement les mots correctement lus.

L'élève lit à voix haute, l'ordinateur enregistre, un service de
reconnaissance vocale transcrit, et l'application compare la transcription au
texte d'origine. On obtient le nombre de mots lus, les mots oubliés et les
mots remplacés — donc le MCLM — sans que personne n'ait à compter à la main.

CE QUE ÇA FAIT BIEN
  · repérer les mots SAUTÉS (une ligne oubliée se voit immédiatement)
  · repérer les mots REMPLACÉS par un autre mot
  · savoir où l'élève s'est arrêté dans le texte
  · calculer le temps et la vitesse

CE QUE ÇA NE FAIT PAS
  Les moteurs de transcription « réparent » ce qu'ils entendent : ils écrivent
  le mot qu'ils comprennent, pas les hésitations. Une lecture hachée, une
  syllabe reprise, un mot déchiffré péniblement seront transcrits comme un mot
  juste. La mesure est donc OPTIMISTE sur la qualité du déchiffrage.

  C'est pourquoi le résultat est présenté comme une PROPOSITION que
  l'enseignant peut corriger — jamais comme une note définitive.

Service utilisé : n'importe quelle API compatible OpenAI
(`/v1/audio/transcriptions`), dont Albert (DINUM). Rien n'est envoyé si
l'enseignant n'a pas explicitement activé la fonction.
"""
import difflib
import json
import mimetypes
import re
import unicodedata
import urllib.request
import uuid

import cles_partagees
from config_manager import config

TIMEOUT = 120


def _cle_effective():
    """La clé saisie ici, sinon celle du fichier partagé entre les applications.

    Le service de transcription par défaut est Albert (DINUM) : si la clé Albert
    a déjà été renseignée pour le Cahier Journal, inutile de la recoller ici.
    """
    locale = (config.get("stt_cle") or "").strip()
    if locale:
        return locale
    url_stt = (config.get("stt_url") or "").lower()
    for service in ("albert", "openai", "openrouter", "mistral"):
        if service in url_stt or (service == "openai" and "openai.com" in url_stt):
            try:
                partagee = cles_partagees.cle(service)
            except Exception:
                partagee = ""
            if partagee:
                return partagee
    return ""


def disponible():
    """La transcription est-elle activée ET réglée ?"""
    return bool(config.get("stt_active")
                and (config.get("stt_url") or "").strip()
                and _cle_effective())


def etat():
    return {
        "active": bool(config.get("stt_active")),
        "reglee": disponible(),
        "service": config.get("stt_nom") or "Service de transcription",
        "modele": config.get("stt_modele") or "",
        "url": config.get("stt_url") or "",
        # Vrai si la clé utilisée vient du fichier partagé entre applications
        # (rien n'a été saisi ici) — affiché dans les réglages pour éviter
        # « le champ est vide, pourtant ça marche ».
        "cle_partagee": bool(_cle_effective()) and not (config.get("stt_cle") or "").strip(),
    }


# --------------------------------------------------------------------------
#  Envoi de l'audio (multipart, sans aucune dépendance externe)
# --------------------------------------------------------------------------
def _multipart(champs, fichier_nom, fichier_octets):
    limite = "----correcteur" + uuid.uuid4().hex
    corps = b""
    for cle, valeur in champs.items():
        corps += (f"--{limite}\r\n"
                  f'Content-Disposition: form-data; name="{cle}"\r\n\r\n'
                  f"{valeur}\r\n").encode("utf-8")
    ctype = mimetypes.guess_type(fichier_nom)[0] or "application/octet-stream"
    corps += (f"--{limite}\r\n"
              f'Content-Disposition: form-data; name="file"; '
              f'filename="{fichier_nom}"\r\n'
              f"Content-Type: {ctype}\r\n\r\n").encode("utf-8")
    corps += fichier_octets + b"\r\n"
    corps += f"--{limite}--\r\n".encode("utf-8")
    return corps, f"multipart/form-data; boundary={limite}"


def _adresse(url_brute):
    """Accepte aussi bien « …/v1 » que « …/v1/audio/transcriptions »."""
    base = (url_brute or "").strip().rstrip("/")
    if base.endswith("/audio/transcriptions"):
        return base
    for suffixe in ("/chat/completions", "/models"):
        if base.endswith(suffixe):
            base = base[: -len(suffixe)]
    return base + "/audio/transcriptions"


def transcrire(octets_audio, nom_fichier="lecture.webm",
               url=None, cle=None, modele=None):
    """Renvoie (texte, message). `texte` vaut "" si la transcription a échoué.

    Les paramètres permettent de tester des valeurs non encore enregistrées.
    """
    url = url if url is not None else config.get("stt_url")
    cle = cle if cle is not None else _cle_effective()
    modele = modele if modele is not None else config.get("stt_modele")
    if not (url or "").strip() or not (cle or "").strip():
        return "", "Le service de transcription n'est pas réglé."

    champs = {
        "model": (modele or "").strip() or "whisper-large-v3-turbo",
        "language": "fr",
        "response_format": "json",
        "temperature": "0",
    }
    corps, ctype = _multipart(champs, nom_fichier, octets_audio)
    req = urllib.request.Request(_adresse(url), data=corps, headers={
        "Content-Type": ctype,
        "Authorization": f"Bearer {(cle or '').strip()}",
    })
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            brut = r.read().decode("utf-8", "replace")
    except Exception as e:
        try:
            import ia_client
            return "", ia_client.expliquer_erreur(e)
        except Exception:
            return "", f"Le service n'a pas répondu ({type(e).__name__})."

    try:
        d = json.loads(brut)
        texte = d.get("text") or d.get("transcription") or ""
    except Exception:
        texte = brut                       # certains services renvoient du texte nu
    texte = (texte or "").strip()
    if not texte:
        return "", "La transcription est revenue vide (micro trop faible ?)."
    return texte, ""


# --------------------------------------------------------------------------
#  Comparaison texte lu / texte attendu
# --------------------------------------------------------------------------
def _normaliser(mot):
    """Pour comparer : sans accent, sans ponctuation, en minuscules.

    On ne pénalise pas un élève parce que le moteur a écrit « eleve » sans
    accent, ni parce qu'il a mis une virgule ailleurs.
    """
    m = unicodedata.normalize("NFD", (mot or "").lower())
    m = "".join(c for c in m if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9']", "", m)


def _mots(texte):
    bruts = re.findall(r"[A-Za-zÀ-ÿ0-9'’-]+", texte or "")
    return [(b, _normaliser(b)) for b in bruts if _normaliser(b)]


def aligner(texte_reference, texte_lu):
    """Compare mot à mot et renvoie un compte rendu détaillé.

    Chaque mot du texte d'origine reçoit un état :
      · "lu"       — reconnu à sa place
      · "remplace" — un autre mot a été entendu à la place
      · "oublie"   — rien n'a été entendu à cet endroit
      · "non_lu"   — au-delà de l'endroit où l'élève s'est arrêté
    """
    ref = _mots(texte_reference)
    lu = _mots(texte_lu)
    a = [x[1] for x in ref]
    b = [x[1] for x in lu]

    etats = ["oublie"] * len(ref)
    remplacements = {}
    ajouts = []
    dernier_reconnu = -1

    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i1, i2):
                etats[k] = "lu"
            dernier_reconnu = max(dernier_reconnu, i2 - 1)
        elif op == "replace":
            for k in range(i1, i2):
                etats[k] = "remplace"
                pos = j1 + (k - i1)
                if pos < j2 and pos < len(lu):
                    remplacements[k] = lu[pos][0]
            dernier_reconnu = max(dernier_reconnu, i2 - 1)
        elif op == "insert":
            ajouts += [lu[k][0] for k in range(j1, j2)]
        # "delete" : les mots restent en "oublie"

    # Où l'élève s'est-il arrêté ? Si toute la fin du texte est absente, ce
    # n'est pas une suite d'erreurs : c'est simplement qu'il n'y est pas allé.
    fin = len(ref)
    while fin > 0 and etats[fin - 1] == "oublie":
        fin -= 1
    for k in range(fin, len(ref)):
        etats[k] = "non_lu"

    mots_lus = fin
    justes = sum(1 for e in etats if e == "lu")
    erreurs = sum(1 for e in etats[:fin] if e in ("remplace", "oublie"))

    return {
        "mots": [{"mot": ref[k][0], "etat": etats[k],
                  "entendu": remplacements.get(k, "")} for k in range(len(ref))],
        "nb_total": len(ref),
        "mots_lus": mots_lus,
        "justes": justes,
        "erreurs": erreurs,
        "ajouts": ajouts[:20],
        "nb_ajouts": len(ajouts),
        "texte_lu": texte_lu,
        "precision": round(justes / mots_lus * 100) if mots_lus else 0,
        "termine": fin >= len(ref),
    }


def analyser(texte_reference, octets_audio, secondes, nom_fichier="lecture.webm"):
    """Transcrit puis aligne. Renvoie le compte rendu prêt à afficher."""
    texte_lu, message = transcrire(octets_audio, nom_fichier)
    if not texte_lu:
        return {"ok": False, "message": message}

    r = aligner(texte_reference, texte_lu)
    minutes = max(0.05, (secondes or 0) / 60)
    r["mclm"] = round(r["justes"] / minutes, 1)
    r["ok"] = True
    r["message"] = ""
    # Avertissement systématique : la machine ne perçoit pas les hésitations.
    r["avertissement"] = (
        "Ce comptage est une proposition. L'ordinateur reconnaît les mots "
        "sautés ou remplacés, mais il n'entend pas les hésitations ni les "
        "syllabes reprises : le résultat est plutôt optimiste. "
        "Corrigez-le si besoin avant d'enregistrer."
    )
    return r
