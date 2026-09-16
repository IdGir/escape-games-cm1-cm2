"""Génération d'un texte à corriger.

Trois moteurs, dans l'ordre de repli :
  1. DeepSeek (API cloud, clé requise)
  2. Ollama (modèle local, aucune clé)
  3. Hors ligne : fabrication d'un texte fautif à partir de phrases modèles
     — TOUJOURS disponible, aucune connexion requise.

Le repli hors-ligne garantit que le bouton « Générer un texte » fonctionne
même sans internet : l'application n'est jamais bloquée.
"""
import json
import random
import urllib.request
import urllib.error

import ia_client
from config_manager import config
from theme import CATEGORIES

TIMEOUT = 30


# ------------------------------------------------------------------ Hors ligne
PHRASES_MODELES = [
    "Les élèves rangent leurs cahiers avant la récréation.",
    "Le chat de la voisine dort sur le muret du jardin.",
    "Nous partons en voyage scolaire au mois de mai.",
    "Les enfants jouent au ballon dans la cour de l'école.",
    "Ma sœur prépare un gâteau au chocolat pour son anniversaire.",
    "Le maître explique la leçon de géographie à toute la classe.",
    "Pendant les vacances, nous avons visité un très beau château.",
    "Les oiseaux construisent leur nid dans le grand arbre.",
    "Tous les matins, je prends mon vélo pour aller à l'école.",
    "La bibliothèque ouvre ses portes le mercredi après-midi.",
    "Les parents attendent leurs enfants devant le portail.",
    "Il pleut souvent en automne, alors nous restons à l'intérieur.",
    "Le boulanger sort des baguettes chaudes de son four.",
    "Mes camarades et moi préparons une exposition sur les volcans.",
    "Le vent souffle fort et fait tomber les feuilles mortes.",
    "Nous avons planté des fleurs dans le jardin de l'école.",
    "Le train entre en gare avec quelques minutes de retard.",
    "Les pompiers sont arrivés très vite sur les lieux.",
]

# Transformations fautives : substitutions contrôlées (jamais de regex hasardeuse),
# pour que la faute injectée soit toujours une vraie faute repérable.
SUBS = {
    "accord": [("élèves", "élève"), ("cahiers", "cahier"), ("enfants", "enfant"),
               ("oiseaux", "oiseau"), ("baguettes", "baguette"), ("fleurs", "fleur"),
               ("parents", "parent"), ("feuilles mortes", "feuille morte"),
               ("portes", "porte"), ("camarades", "camarade"), ("pompiers", "pompier"),
               ("minutes", "minute"), ("volcans", "volcan"), ("lieux", "lieu")],
    "conjugaison": [("rangent", "range"), ("jouent", "joue"), ("construisent", "construise"),
                    ("attendent", "attende"), ("partons", "parton"), ("prenons", "prenon"),
                    ("préparons", "préparon"), ("avons", "avon"), ("restons", "reston"),
                    ("prépare", "préparent"), ("explique", "expliquent"),
                    ("ouvre", "ouvrent"), ("souffle", "soufflent"), ("dort", "dorment")],
    "homophone": [(" est ", " et "), (" et ", " est "), (" a ", " à "),
                  (" sont ", " son "), (" ont ", " on "), (" où ", " ou ")],
    "orthographe": [("très", "tres"), ("après", "apres"), ("école", "ecole"),
                    ("château", "chateau"), ("élèves", "eleves"), ("récréation", "recreation"),
                    ("bibliothèque", "bibliotheque"), ("mère", "mere"), ("sœur", "soeur"),
                    ("beaucoup", "beacoup"), ("géographie", "geographie")],
    "segmentation": [("il y a", "ilya"), ("parce que", "parceque"), ("d'abord", "dabord"),
                     ("tout de suite", "toutdesuite"), ("à l'école", "alecole"),
                     ("l'école", "lecole"), ("l'intérieur", "linterieur"),
                     ("d'anniversaire", "danniversaire"), ("quelqu'un", "quelquun")],
    "lexique": [("prépare", "fait"), ("construisent", "font"), ("explique", "fait"),
                ("baguettes chaudes", "trucs chauds"), ("château", "truc"),
                ("exposition", "chose")],
}


def _injecter(phrase, categorie):
    """Injecte une faute de la catégorie demandée. Renvoie la phrase ou None."""
    if categorie == "majuscule":
        if phrase and phrase[0].isupper():
            return phrase[0].lower() + phrase[1:]
        return None
    if categorie == "ponctuation":
        if "," in phrase:
            return phrase.replace(",", " ,", 1)
        if phrase.endswith("."):
            return phrase[:-1] + " ."
        return None
    for avant, apres in SUBS.get(categorie, []):
        if avant in phrase:
            return phrase.replace(avant, apres, 1)
    return None


def generer_hors_ligne(nb_phrases=5, categories=None):
    """Fabrique un texte fautif À PARTIR de phrases correctes.

    Comme on part du texte juste, on connaît EXACTEMENT le corrigé et la
    catégorie de chaque faute injectée. C'est ce qui permet ensuite de ne
    signaler à l'élève que de vraies erreurs.

    Renvoie (texte_fautif, texte_corrige, erreurs, plan) où
    erreurs = [(forme_fautive, forme_correcte, categorie), ...]
    """
    cats = list(categories or CATEGORIES) or CATEGORIES
    phrases = random.sample(PHRASES_MODELES, min(nb_phrases, len(PHRASES_MODELES)))
    while len(phrases) < nb_phrases:
        phrases.append(random.choice(PHRASES_MODELES))

    plan, erreurs, sortie = {}, [], []
    for p_juste in phrases:
        p = p_juste
        objectif = random.choice([1, 1, 2])
        placees = 0
        for cat in random.sample(cats, len(cats)):
            if placees >= objectif:
                break
            res = _injecter_trace(p, cat)
            if res:
                p, faux, juste = res
                erreurs.append((faux, juste, cat))
                plan[cat] = plan.get(cat, 0) + 1
                placees += 1
        sortie.append(p)
        # le corrigé est reconstruit à partir des phrases d'origine
    texte = " ".join(sortie)
    corrige = " ".join(phrases)
    return texte, corrige, erreurs, plan


def _injecter_trace(phrase, categorie):
    """Comme _injecter, mais renvoie aussi ce qui a été remplacé.

    Renvoie (phrase_modifiee, forme_fautive, forme_correcte) ou None.
    """
    if categorie == "majuscule":
        if phrase and phrase[0].isupper():
            mot = phrase.split()[0]
            return (phrase[0].lower() + phrase[1:], mot[0].lower() + mot[1:], mot)
        return None

    if categorie == "ponctuation":
        if "," in phrase:
            return (phrase.replace(",", " ,", 1), ",", ",")
        if phrase.endswith("."):
            return (phrase[:-1] + " .", ".", ".")
        return None

    for avant, apres in SUBS.get(categorie, []):
        if avant in phrase:
            return (phrase.replace(avant, apres, 1), apres, avant)
    return None


# ------------------------------------------------------------------ DeepSeek
def _prompt(nb_phrases, niveau, theme_, categories):
    cats = ", ".join(categories) if categories else "toutes catégories"
    return (
        f"Tu es enseignant de français à l'école primaire. Écris un texte de "
        f"EXACTEMENT {nb_phrases} phrases sur le thème : {theme_}. "
        f"Niveau de difficulté : {niveau}/5. "
        f"Ce texte doit contenir des ERREURS VOLONTAIRES que l'élève devra corriger, "
        f"portant uniquement sur ces catégories : {cats}. "
        f"Environ une à deux erreurs par phrase, ni plus ni moins. "
        f"Le texte doit rester compréhensible et adapté à des enfants de 9 à 11 ans. "
        f"Réponds UNIQUEMENT par un objet JSON, sans aucun autre texte, sans balises "
        f"Markdown, au format : "
        f'{{"texte_fautif": "...", "texte_corrige": "...", '
        f'"erreurs": [{{"fautif": "mot fautif", "correct": "mot correct", '
        f'"categorie": "accord"}}]}}\n'
        f"IMPÉRATIF : « texte_corrige » doit être le texte fautif où SEULES les "
        f"erreurs listées ont été réparées — même longueur, mêmes phrases, même "
        f"ordre des mots. Ne reformule rien."
    )


def _appel_deepseek(prompt_):
    cle = config.get("ia_cle_api", "").strip()
    if not cle:
        raise RuntimeError("Aucune clé API DeepSeek renseignée.")
    corps = json.dumps({
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt_}],
        "temperature": 1.0,
        "max_tokens": 1200,
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.deepseek.com/chat/completions", data=corps,
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {cle}"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        d = json.loads(r.read().decode("utf-8"))
    return d["choices"][0]["message"]["content"]


def _appel_ollama(prompt_):
    url = config.get("ia_url_ollama").rstrip("/") + "/api/generate"
    corps = json.dumps({
        "model": config.get("ia_modele_ollama"),
        "prompt": prompt_, "stream": False,
    }).encode("utf-8")
    req = urllib.request.Request(url, data=corps,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.loads(r.read().decode("utf-8"))
    return d.get("response", "")


def _extraire_json(brut):
    t = brut.strip()
    t = t.replace("```json", "").replace("```", "").strip()
    d = t.find("{")
    f = t.rfind("}")
    if d == -1 or f == -1:
        raise ValueError("Réponse IA illisible.")
    return json.loads(t[d:f + 1])


def generer(nb_phrases=None, niveau=None, theme_=None, categories=None):
    """Point d'entrée unique.

    Renvoie (texte_fautif, texte_corrige, erreurs, moteur_utilise, message).
    Le corrigé n'est JAMAIS montré à l'élève : il ne sert qu'à savoir, sans
    aucun doute possible, quels mots sont réellement fautifs.
    """
    nb_phrases = nb_phrases or config.get("ia_nb_phrases", 5)
    niveau = niveau or config.get("ia_niveau", 2)
    # L'enseignant peut cocher plusieurs thèmes : on en tire un au hasard à
    # chaque texte. Sans cela, dix textes d'affilée parlaient tous de la même
    # chose — et l'IA leur donnait le même titre.
    theme_ = theme_ or theme_au_hasard()
    categories = categories or config.get("ia_categories_ciblees", CATEGORIES)

    if config.get("ia_active"):
        moteur = config.get("ia_moteur", "deepseek")
        prompt_ = _prompt(nb_phrases, niveau, theme_, categories)
        try:
            brut = ia_client.appeler(prompt_, temperature=1.0, max_tokens=1200,
                                     tache="generation")
            d = _extraire_json(brut)
            texte = (d.get("texte_fautif") or "").strip()
            corrige = (d.get("texte_corrige") or "").strip()
            erreurs = [(e.get("fautif", ""), e.get("correct", ""),
                        e.get("categorie", "orthographe"))
                       for e in d.get("erreurs", []) if isinstance(e, dict)]
            # Garde-fou : sans corrigé exploitable, on refuse le texte de l'IA
            # plutôt que de renvoyer l'élève à un repérage hasardeux.
            if texte and corrige and _corrige_plausible(texte, corrige):
                return texte, corrige, erreurs, moteur, "Texte généré par l'IA."
            raise ValueError("corrigé absent ou incohérent")
        except Exception as e:
            texte, corrige, erreurs, _ = generer_hors_ligne(nb_phrases, categories)
            return (texte, corrige, erreurs, "hors_ligne",
                    f"IA indisponible ({type(e).__name__}) — texte fabriqué hors ligne.")

    texte, corrige, erreurs, _ = generer_hors_ligne(nb_phrases, categories)
    return texte, corrige, erreurs, "hors_ligne", "Texte fabriqué hors ligne."


def _corrige_plausible(fautif: str, corrige: str) -> bool:
    """Le corrigé doit être le MÊME texte, seulement réparé.

    Si l'IA a reformulé (longueurs très différentes), on ne peut plus comparer
    mot à mot : on préfère alors le générateur hors ligne, qui est fiable.
    """
    a, b = len(fautif.split()), len(corrige.split())
    if not a or not b:
        return False
    return 0.75 <= a / b <= 1.35


# ==========================================================================
#  Titre automatique — tout texte fabriqué arrive avec un titre modifiable
# ==========================================================================
# Mots vides : ils ne portent pas le sens, on ne les met jamais dans un titre.
_VIDES = {
    "le", "la", "les", "un", "une", "des", "du", "de", "d", "au", "aux", "à",
    "et", "ou", "mais", "donc", "or", "ni", "car", "que", "qui", "quoi", "dont",
    "où", "ce", "cet", "cette", "ces", "son", "sa", "ses", "leur", "leurs",
    "mon", "ma", "mes", "ton", "ta", "tes", "notre", "nos", "votre", "vos",
    "il", "elle", "ils", "elles", "je", "tu", "nous", "vous", "on", "se", "s",
    "en", "y", "dans", "sur", "sous", "avec", "sans", "pour", "par", "chez",
    "est", "sont", "a", "ont", "été", "être", "avoir", "fait", "très", "plus",
    "tout", "tous", "toute", "toutes", "bien", "aussi", "alors", "puis", "quand",
    "pendant", "après", "avant", "leurs", "lui", "me", "te", "ne", "pas", "l",
}


def _titre_hors_ligne(texte: str) -> str:
    """Fabrique un titre court à partir des mots porteurs de sens du texte.

    Aucune connexion nécessaire : on prend la première phrase, on retire les
    petits mots, et on garde les deux ou trois mots les plus significatifs.
    """
    import re
    propre = (texte or "").strip()
    if not propre:
        return "Texte à corriger"
    premiere = re.split(r"[.!?]", propre)[0]
    # œ et æ font partie des mots : sans eux, « sœur » devenait « s ur ».
    mots = re.findall(r"[A-Za-zÀ-ÿœŒæÆ'’-]+", premiere)
    if not mots:
        return "Texte à corriger"
    # On garde le début de la première phrase : c'est naturel à lire, et cela
    # évite les titres télégraphiques du type « Enfants jouent ballon ».
    choix = mots[:5]
    # On ne termine jamais sur un petit mot (« des », « au », « et »…).
    while len(choix) > 2 and choix[-1].lower().strip("'’") in _VIDES:
        choix.pop()
    titre = " ".join(choix)
    titre = titre[0].upper() + titre[1:]
    return titre[:60]


def themes_actifs():
    """Les thèmes cochés par l'enseignant (au moins un, toujours)."""
    liste = config.get("ia_themes") or []
    liste = [t for t in liste if str(t).strip()]
    if liste:
        return liste
    unique = (config.get("ia_theme") or "").strip()
    return [unique] if unique else ["la vie quotidienne à l'école"]


def theme_au_hasard():
    return random.choice(themes_actifs())


def titre_auto(texte: str) -> str:
    """Titre du texte : proposé par l'IA si elle est active, sinon hors ligne.

    Le titre reste toujours modifiable par l'enseignant dans l'application.
    """
    texte = (texte or "").strip()
    if not texte:
        return "Texte à corriger"
    if config.get("ia_active"):
        try:
            brut = ia_client.appeler(
                "Donne un titre court (2 à 5 mots, sans guillemets, sans point "
                "final) pour ce texte destiné à des élèves de 9 à 11 ans. "
                "Réponds UNIQUEMENT par le titre.\n\n" + texte[:1200],
                temperature=0.6, max_tokens=30, tache="generation")
            t = (brut or "").strip().strip('"«»').split("\n")[0].strip(" .")
            if 2 <= len(t) <= 70:
                return t
        except Exception:
            pass
    return _titre_hors_ligne(texte)


# ==========================================================================
#  Textes de fluence : invention IA, ou extraits littéraires pour enfants
# ==========================================================================
# Banque hors ligne : extraits du DOMAINE PUBLIC, adaptés au cycle 3. Elle
# garantit que la fonction marche même sans IA et sans internet.
EXTRAITS_LITTERAIRES = [
    ("Le loup et l'agneau", "Jean de La Fontaine", 2,
     "Un agneau se désaltérait dans le courant d'une onde pure. Un loup survient "
     "à jeun, qui cherchait aventure, et que la faim en ces lieux attirait. "
     "« Qui te rend si hardi de troubler mon breuvage ? » dit cet animal plein "
     "de rage. « Tu seras châtié de ta témérité. »"),
    ("Le Petit Chaperon rouge", "Charles Perrault", 1,
     "Il était une fois une petite fille de village, la plus jolie qu'on eût su "
     "voir. Sa mère en était folle, et sa grand-mère plus folle encore. Cette "
     "bonne femme lui fit faire un petit chaperon rouge, qui lui seyait si bien "
     "que partout on l'appelait le Petit Chaperon rouge."),
    ("Les malheurs de Sophie", "Comtesse de Ségur", 2,
     "Sophie était une petite fille de quatre ans. Elle avait de beaux cheveux "
     "blonds et des yeux gris. Elle était vive, gaie, mais très étourdie. Un "
     "matin, elle entra dans la salle à manger et vit sur la table une belle "
     "poupée de cire, avec des joues roses et des souliers noirs."),
    ("Sans famille", "Hector Malot", 3,
     "Je suis un enfant trouvé. Mais jusqu'à huit ans j'ai cru que, comme tous "
     "les autres enfants, j'avais une mère, car lorsque je pleurais il y avait "
     "une femme qui me serrait si doucement entre ses bras en me berçant que "
     "mes larmes s'arrêtaient de couler."),
    ("Vingt mille lieues sous les mers", "Jules Verne", 4,
     "La mer est tout ! Elle couvre les sept dixièmes du globe terrestre. Son "
     "souffle est pur et sain. C'est l'immense désert où l'homme n'est jamais "
     "seul, car il sent frémir la vie à ses côtés. La mer n'est que le véhicule "
     "d'une surnaturelle et prodigieuse existence."),
    ("La petite fille aux allumettes", "Hans Christian Andersen", 2,
     "Il faisait effroyablement froid ; il neigeait depuis le matin ; il faisait "
     "déjà sombre. Dans cette obscurité et par ce froid, une pauvre petite fille "
     "marchait dans la rue. Elle était tête nue, les pieds nus. Elle avait des "
     "pantoufles en quittant la maison, mais elles étaient bien trop grandes."),
    ("Le tour du monde en quatre-vingts jours", "Jules Verne", 4,
     "Phileas Fogg était un de ces personnages mathématiquement exacts, qui, "
     "jamais pressés et toujours prêts, sont économes de leurs pas et de leurs "
     "mouvements. Il ne faisait jamais une enjambée de trop, allant toujours par "
     "le plus court. Il ne perdait pas un regard au plafond."),
    ("Le corbeau et le renard", "Jean de La Fontaine", 1,
     "Maître Corbeau, sur un arbre perché, tenait en son bec un fromage. Maître "
     "Renard, par l'odeur alléché, lui tint à peu près ce langage : « Hé ! "
     "bonjour, Monsieur du Corbeau. Que vous êtes joli ! que vous me semblez "
     "beau ! »"),
    ("Contes de ma mère l'Oye — Le chat botté", "Charles Perrault", 2,
     "Un meunier ne laissa pour tous biens, à trois enfants qu'il avait, que son "
     "moulin, son âne et son chat. Les partages furent bientôt faits. Le plus "
     "jeune n'eut que le chat, et il ne pouvait se consoler d'avoir un si "
     "pauvre lot."),
    ("Le voyage de Nils Holgersson", "Selma Lagerlöf", 3,
     "Le garçon regarda autour de lui. La chambre était la même, et pourtant "
     "tout y semblait démesuré. La table, tout à l'heure à hauteur de sa main, "
     "s'élevait maintenant très haut au-dessus de sa tête. Il courut jusqu'au "
     "miroir accroché au mur et s'y regarda longuement."),
]


def _prompt_fluence(nombre, niveau, litteraire):
    if litteraire:
        return (
            f"Tu es professeur des écoles en France. Propose {nombre} EXTRAITS "
            f"courts d'œuvres de littérature de jeunesse du DOMAINE PUBLIC "
            f"(auteurs décédés depuis plus de 70 ans : La Fontaine, Perrault, "
            f"Comtesse de Ségur, Hector Malot, Jules Verne, Andersen, Grimm, "
            f"Daudet, Selma Lagerlöf…), adaptés à des élèves de 9 à 11 ans, "
            f"pour un exercice de LECTURE À VOIX HAUTE chronométrée. "
            f"Chaque extrait fait 60 à 110 mots, se suffit à lui-même, et ne "
            f"contient AUCUNE erreur d'orthographe. "
            f"Niveau de difficulté visé : {niveau}/5. "
            f"Réponds UNIQUEMENT par un tableau JSON, sans balises Markdown : "
            f'[{{"titre": "...", "auteur": "...", "oeuvre": "...", '
            f'"niveau": {niveau}, "texte": "..."}}]'
        )
    return (
        f"Tu es professeur des écoles en France. Écris {nombre} textes courts et "
        f"variés pour un exercice de LECTURE À VOIX HAUTE chronométrée, destinés "
        f"à des élèves de 9 à 11 ans. Chaque texte fait 60 à 110 mots, est "
        f"vivant, et ne contient AUCUNE erreur d'orthographe ni de grammaire. "
        f"Niveau de difficulté : {niveau}/5. "
        f"Réponds UNIQUEMENT par un tableau JSON, sans balises Markdown : "
        f'[{{"titre": "...", "niveau": {niveau}, "texte": "..."}}]'
    )


def _extraire_liste_json(brut):
    t = (brut or "").replace("```json", "").replace("```", "").strip()
    d, f = t.find("["), t.rfind("]")
    if d == -1 or f == -1:
        raise ValueError("Réponse IA illisible.")
    return json.loads(t[d:f + 1])


def proposer_textes_fluence(nombre=3, niveau=2, litteraire=False):
    """Propose des textes de fluence, SANS les enregistrer.

    L'enseignant valide chaque texte avant qu'il n'entre dans la banque.
    Renvoie (propositions, moteur, message).
    """
    nombre = max(1, min(int(nombre or 3), 10))
    if config.get("ia_active"):
        try:
            brut = ia_client.appeler(_prompt_fluence(nombre, niveau, litteraire),
                                     temperature=0.9, max_tokens=2200,
                                     tache="generation")
            liste = _extraire_liste_json(brut)
            props = []
            for x in liste:
                if not isinstance(x, dict):
                    continue
                texte = (x.get("texte") or "").strip()
                if len(texte.split()) < 25:
                    continue
                source = ""
                if x.get("auteur") or x.get("oeuvre"):
                    source = " — ".join(
                        s for s in [x.get("oeuvre", ""), x.get("auteur", "")] if s)
                props.append({
                    "titre": (x.get("titre") or titre_auto(texte)).strip()[:70],
                    "texte": texte,
                    "niveau": int(x.get("niveau") or niveau),
                    "source": source,
                    "nb_mots": len(texte.split()),
                })
            if props:
                moteur = config.get("ia_moteur", "deepseek")
                return (props[:nombre], moteur,
                        "Propositions de l'IA — à relire avant de les ajouter.")
        except Exception as e:
            pass  # on retombe sur la banque hors ligne, jamais d'échec sec

    # Repli hors ligne : la banque d'extraits du domaine public.
    banque = EXTRAITS_LITTERAIRES[:]
    random.shuffle(banque)
    props = [{
        "titre": t, "texte": txt, "niveau": n,
        "source": f"{t} — {auteur} (domaine public)",
        "nb_mots": len(txt.split()),
    } for (t, auteur, n, txt) in banque[:nombre]]
    return (props, "hors_ligne",
            "Extraits classiques du domaine public (aucune IA active).")


def tester_connexion():
    """Vérifie le moteur IA configuré. Renvoie (ok: bool, message: str)."""
    moteur = config.get("ia_moteur", "deepseek")
    try:
        ia_client.appeler("Réponds uniquement par : ok", temperature=0.0, max_tokens=20,
                          moteur=moteur)
        return True, f"Connexion réussie ({ia_client.nom_moteur(moteur)})."
    except Exception as e:
        return False, f"Échec : {e}"
