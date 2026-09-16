"""Client IA unifié : un seul endroit pour parler aux différents moteurs.

Trois moteurs possibles, tous appelés de la même façon par le reste du code :
  · "deepseek" — API cloud DeepSeek (clé requise)
  · "ollama"   — modèle local (aucune clé, rien ne sort de l'ordinateur)
  · "api"      — N'IMPORTE QUEL service compatible OpenAI (OpenAI, Mistral,
                 Groq, OpenRouter, LM Studio, un serveur maison…). On règle
                 l'adresse, la clé et le nom du modèle dans les réglages.

Ce module NE décide de rien : il exécute l'appel demandé et renvoie le texte
brut de la réponse. La logique (génération, correction, aide) reste ailleurs.
"""
import json
import urllib.request

import cles_partagees
from config_manager import config

TIMEOUT_CLOUD = 45
TIMEOUT_LOCAL = 180


def _post_json(url, corps, entetes, timeout):
    req = urllib.request.Request(url, data=json.dumps(corps).encode("utf-8"),
                                 headers=entetes)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


# --------------------------------------------------------------------------
#  Messages d'erreur compréhensibles
#
#  « HTTP Error 401: Unauthorized » ne dit rien à un enseignant. On traduit
#  chaque code en une phrase qui indique QUOI corriger.
# --------------------------------------------------------------------------
def expliquer_erreur(e):
    import urllib.error
    if isinstance(e, urllib.error.HTTPError):
        detail = ""
        try:
            brut = e.read().decode("utf-8", "replace")[:300]
            d = json.loads(brut)
            detail = (d.get("error") or {}).get("message") if isinstance(
                d.get("error"), dict) else (d.get("detail") or d.get("message") or "")
            detail = str(detail or "")[:200]
        except Exception:
            pass
        messages = {
            401: "Clé d'accès refusée. Vérifiez que la clé est complète, sans "
                 "espace au début ou à la fin, et qu'elle est bien active.",
            403: "Clé valide mais accès refusé : ce compte n'a peut-être pas "
                 "le droit d'utiliser ce modèle.",
            404: "Adresse ou modèle introuvable. Vérifiez l'adresse de l'API "
                 "et le nom exact du modèle.",
            422: "Le service a refusé la demande : le nom du modèle est "
                 "probablement incorrect.",
            429: "Trop de demandes d'un coup. Réessayez dans une minute.",
        }
        base = messages.get(e.code, f"Le service a répondu par une erreur {e.code}.")
        return base + (f" — {detail}" if detail else "")
    if isinstance(e, urllib.error.URLError):
        return ("Impossible de joindre le service. Vérifiez l'adresse et la "
                "connexion internet.")
    if isinstance(e, TimeoutError):
        return "Le service met trop de temps à répondre."
    return f"Échec ({type(e).__name__}) : {e}"


def tester(url, cle, modele, timeout=25):
    """Teste un service compatible OpenAI avec des valeurs DONNÉES.

    On ne lit pas la configuration enregistrée : on teste exactement ce que
    l'enseignant vient de saisir à l'écran. Sinon il faudrait enregistrer
    avant de pouvoir tester, ce qui n'a aucun sens.
    """
    if not (url or "").strip():
        return False, "Renseignez l'adresse de l'API."
    if not (cle or "").strip():
        return False, "Renseignez la clé d'accès."
    try:
        _chat_openai(url, cle.strip(), (modele or "").strip() or "gpt-4o-mini",
                     "Réponds uniquement par : ok", 0.0, 20, timeout)
        return True, "Connexion réussie."
    except Exception as e:
        return False, expliquer_erreur(e)


def lister_modeles(url, cle, timeout=25):
    """Les modèles auxquels cette clé donne accès (route /models du standard).

    Très utile : cela vérifie la clé ET donne les noms exacts à recopier.
    """
    base = (url or "").strip().rstrip("/")
    if not base:
        return [], "Renseignez l'adresse de l'API."
    # On accepte qu'on ait collé une adresse complète (…/chat/completions).
    for suffixe in ("/chat/completions", "/audio/transcriptions", "/models"):
        if base.endswith(suffixe):
            base = base[: -len(suffixe)]
    req = urllib.request.Request(base + "/models", headers={
        "Authorization": f"Bearer {(cle or '').strip()}"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        return [], expliquer_erreur(e)
    donnees = d.get("data") if isinstance(d, dict) else None
    if not isinstance(donnees, list):
        return [], "Le service n'a pas renvoyé de liste de modèles."
    noms = []
    for m in donnees:
        nom = m.get("id") if isinstance(m, dict) else str(m)
        genre = (m.get("type") or "") if isinstance(m, dict) else ""
        if nom:
            noms.append({"id": nom, "type": genre})
    return noms, ""


def _chat_openai(base_url, cle, modele, prompt, temperature, max_tokens, timeout):
    """Appel au format OpenAI /chat/completions (le standard le plus répandu)."""
    base = (base_url or "").strip().rstrip("/")
    if not base:
        raise RuntimeError("Aucune adresse d'API renseignée.")
    url = base if base.endswith("/chat/completions") else base + "/chat/completions"
    entetes = {"Content-Type": "application/json"}
    if cle:
        entetes["Authorization"] = f"Bearer {cle}"
    d = _post_json(url, {
        "model": modele,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }, entetes, timeout)
    return d["choices"][0]["message"]["content"]


def _cle_effective(reglage, service_partage):
    """La clé saisie ici, sinon celle du fichier partagé entre les applications.

    Évite de recoller la même clé DeepSeek/Albert dans les trois applications :
    voir cles_partagees.py. Le réglage local reste prioritaire, donc rien ne
    change pour une installation déjà configurée.
    """
    locale = (config.get(reglage) or "").strip()
    if locale:
        return locale
    try:
        return cles_partagees.cle(service_partage)
    except Exception:
        return ""


def _deepseek(prompt, temperature, max_tokens):
    cle = _cle_effective("ia_cle_api", "deepseek")
    if not cle:
        raise RuntimeError(
            "Aucune clé API DeepSeek renseignée (ni dans les réglages, ni dans le "
            "fichier de clés partagées).")
    return _chat_openai("https://api.deepseek.com", cle, "deepseek-chat",
                        prompt, temperature, max_tokens, TIMEOUT_CLOUD)


def _service_partage_pour(url_api):
    """Devine à quel service partagé correspond une adresse d'API.

    L'utilisateur règle « une adresse + une clé » ; le fichier partagé, lui,
    range les clés par service. On fait le rapprochement sur le nom de domaine.
    """
    u = (url_api or "").lower()
    for service, marqueur in (
        ("albert", "albert"),
        ("openrouter", "openrouter"),
        ("deepseek", "deepseek"),
        ("mistral", "mistral"),
        ("gemini", "generativelanguage.googleapis.com"),
        ("openai", "openai.com"),
        ("anthropic", "anthropic"),
    ):
        if marqueur in u:
            return service
    return ""


def _api_perso(prompt, temperature, max_tokens):
    url_api = config.get("ia_url_api")
    cle = _cle_effective("ia_cle_api_perso", _service_partage_pour(url_api))
    return _chat_openai(url_api, cle,
                        config.get("ia_modele_api") or "gpt-4o-mini",
                        prompt, temperature, max_tokens, TIMEOUT_CLOUD)


def _api_secondaire(prompt, temperature, max_tokens):
    """Le SECOND moteur, réglé indépendamment du premier.

    Sert quand un moteur est meilleur sur une tâche et l'autre sur une autre :
    par exemple un modèle solide en correction, et un service français pour
    tout ce qui touche aux textes des élèves.
    """
    url_api = config.get("ia_url_api2")
    cle = _cle_effective("ia_cle_api2", _service_partage_pour(url_api))
    return _chat_openai(url_api, cle,
                        config.get("ia_modele_api2") or "",
                        prompt, temperature, max_tokens, TIMEOUT_CLOUD)


# Réglages tout prêts pour les services les plus utiles à l'école.
PRESETS = {
    "gemini": {
        "nom": "Google AI Studio (Gemini) — gratuit",
        "url": "https://generativelanguage.googleapis.com/v1beta/openai",
        "modele": "gemini-3-flash",
        "aide": "Clé GRATUITE sur aistudio.google.com/apikey, sans carte "
                "bancaire — le plus simple pour démarrer. Les modèles Flash et "
                "Flash-Lite restent gratuits (quotas par minute et par jour). "
                "⚠️ Sur l'offre gratuite, Google peut utiliser les données "
                "envoyées pour améliorer ses produits : à réserver à la "
                "génération de textes et d'exercices, PAS aux productions "
                "d'élèves. Pour celles-ci, préférez Albert ou Ollama (local).",
    },
    "albert": {
        "nom": "Albert (service public français)",
        "url": "https://albert.api.etalab.gouv.fr/v1",
        "modele": "albert-large",
        "aide": "Service de l'État, réservé aux agents publics. La demande de "
                "clé se fait auprès de la DINUM. Les données restent en France.",
    },
    "openai": {
        "nom": "OpenAI", "url": "https://api.openai.com/v1",
        "modele": "gpt-4o-mini", "aide": "Clé sur platform.openai.com.",
    },
    "mistral": {
        "nom": "Mistral (France)", "url": "https://api.mistral.ai/v1",
        "modele": "mistral-small-latest", "aide": "Clé sur console.mistral.ai.",
    },
}


# Les tâches pour lesquelles on peut choisir un moteur plutôt que l'autre.
TACHES = {
    "correction": "Corriger les textes des élèves",
    "aide": "Formuler les questions et les indices",
    "generation": "Fabriquer les textes et les titres",
    "definitions": "Écrire les définitions du dictionnaire",
}


def moteur_pour(tache):
    """Quel moteur utiliser pour cette tâche : le principal ou le second."""
    if not tache:
        return config.get("ia_moteur", "deepseek")
    choix = (config.get("ia_taches", {}) or {}).get(tache, "principal")
    if choix == "secondaire" and config.get("ia_moteur_secondaire", "aucun") != "aucun":
        return config.get("ia_moteur_secondaire")
    return config.get("ia_moteur", "deepseek")


def _ollama(prompt, temperature):
    url = (config.get("ia_url_ollama") or "").rstrip("/") + "/api/generate"
    d = _post_json(url, {"model": config.get("ia_modele_ollama"),
                         "prompt": prompt, "stream": False,
                         "options": {"temperature": temperature}},
                   {"Content-Type": "application/json"}, TIMEOUT_LOCAL)
    return d.get("response", "")


def appeler(prompt, temperature=0.0, max_tokens=1200, moteur=None, tache=None):
    """Envoie `prompt` au moteur voulu et renvoie le texte brut.

    `tache` permet de laisser l'application choisir entre le moteur principal
    et le second, selon le réglage de l'enseignant.
    """
    moteur = moteur or moteur_pour(tache)
    if moteur == "deepseek":
        return _deepseek(prompt, temperature, max_tokens)
    if moteur == "api":
        return _api_perso(prompt, temperature, max_tokens)
    if moteur == "api2":
        return _api_secondaire(prompt, temperature, max_tokens)
    return _ollama(prompt, temperature)


def nom_moteur(moteur=None):
    moteur = moteur or config.get("ia_moteur", "deepseek")
    if moteur == "deepseek":
        return "DeepSeek (cloud)"
    if moteur == "api":
        return config.get("ia_nom_api") or "API personnalisée"
    if moteur == "api2":
        return config.get("ia_nom_api2") or "Second moteur"
    if moteur == "ollama":
        return f"Ollama — {config.get('ia_modele_ollama')}"
    return "hors ligne"


def extraire_json(brut):
    """Isole le premier objet JSON d'une réponse (les modèles ajoutent parfois
    du texte ou des balises Markdown autour)."""
    t = (brut or "").strip().replace("```json", "").replace("```", "").strip()
    d, f = t.find("{"), t.rfind("}")
    if d == -1 or f == -1:
        raise ValueError("Réponse IA illisible.")
    return json.loads(t[d:f + 1])
