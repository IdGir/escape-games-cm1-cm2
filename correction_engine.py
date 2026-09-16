"""Moteur de correction hors-ligne, à base de règles. Aucune connexion requise.

Il ne prétend pas être exhaustif : son rôle pédagogique est de REPÉRER des zones
suspectes et de les rattacher à l'une des 8 catégories, pour que l'élève réfléchisse.
"""
import re
import unicodedata
from theme import CATEGORIES

MOT = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ\-]+")


def sans_accent(m: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", m.lower())
                   if unicodedata.category(c) != "Mn")


# ---------------------------------------------------------------- Comptages
def compter_mots(texte: str) -> int:
    return len(MOT.findall(texte))


def compter_phrases(texte: str) -> int:
    t = texte.strip()
    if not t:
        return 0
    parties = [p for p in re.split(r"[.!?…]+", t) if p.strip()]
    return max(1, len(parties))


# ---------------------------------------------------------------- Listes de référence
DETERMINANTS_PLURIEL = {"les", "des", "ces", "mes", "tes", "ses", "nos", "vos", "leurs",
                        "plusieurs", "quelques", "certains", "certaines", "deux", "trois",
                        "quatre", "cinq", "six", "sept", "huit", "neuf", "dix"}
DETERMINANTS_SINGULIER = {"le", "la", "un", "une", "ce", "cet", "cette", "mon", "ma",
                          "ton", "ta", "son", "sa", "notre", "votre", "leur", "chaque"}

INVARIABLES = {"puis", "pas", "plus", "moins", "très", "trop", "assez", "jamais",
               "toujours", "souvent", "bien", "mal", "temps", "corps", "fois", "prix",
               "pays", "mois", "souris", "tapis", "repas", "bras", "cas", "gros", "gris",
               "français", "anglais", "vers", "dans", "sans", "sous", "avec", "chez",
               "alors", "depuis", "après", "avant", "pendant", "beaucoup", "aussi"}

PRONOMS_SUJETS = {"je": "1s", "j": "1s", "tu": "2s", "il": "3s", "elle": "3s", "on": "3s",
                  "nous": "1p", "vous": "2p", "ils": "3p", "elles": "3p"}

# Terminaisons attendues (présent, verbes du 1er groupe et auxiliaires courants)
TERMINAISONS_PRESENT = {
    "1s": ("e", "s", "x", "ai"),
    "2s": ("es", "s", "x"),
    "3s": ("e", "t", "d", "a"),
    "1p": ("ons", "mes"),
    "2p": ("ez", "tes"),
    "3p": ("ent", "ont"),
}

# ----------------------------------------------------------------------------
#  HOMOPHONES — le point le plus délicat.
#
#  Signaler « et », « son », « la »… à chaque occurrence était une ERREUR DE
#  CONCEPTION : dans un texte juste, ces mots sont justes, et l'élève se
#  retrouvait avec des « erreurs » impossibles à corriger.
#
#  Désormais, un homophone n'est compté comme erreur QUE si le contexte le
#  prouve (règles ci-dessous). Sinon, au mieux, c'est un point de vigilance.
# ----------------------------------------------------------------------------

# Règles sûres : (mot_fautif, mots_precedents_declencheurs, correction, explication)
REGLES_HOMOPHONES = [
    # « il à mangé » → « il a mangé »
    ("à", {"il", "elle", "on", "qui", "ça", "cela"}, "a",
     "Après « {prec} », c'est le verbe avoir : « a », sans accent. "
     "Remplace par « avait » pour vérifier."),
    # « il et parti » → « il est parti »
    ("et", {"il", "elle", "on", "ce", "qui", "ça", "cela"}, "est",
     "Ici on peut dire « était » : il faut donc « est », le verbe être."),
    # « ils son partis » → « ils sont partis »
    ("son", {"ils", "elles", "se", "ne"}, "sont",
     "Ici on peut dire « étaient » : il faut donc « sont »."),
    # « ils on mangé » → « ils ont mangé »
    ("on", {"ils", "elles"}, "ont",
     "Ici on peut dire « avaient » : il faut donc « ont »."),
    # « il peu venir » → « il peut venir »
    ("peu", {"il", "elle", "on"}, "peut",
     "Après « {prec} », c'est le verbe pouvoir : « peut »."),
    # « il ce lève » → « il se lève »
    ("ce", {"il", "elle", "on", "je", "tu", "nous", "vous", "ils", "elles"}, "se",
     "Devant un verbe, c'est le pronom « se »."),
]

# Mots qui, juste APRÈS « a », prouvent qu'il fallait « à » (préposition).
VERBES_AVANT_A = {"va", "vais", "vas", "allons", "allez", "vont", "aller",
                  "part", "pars", "partons", "partez", "partent", "partir",
                  "viens", "vient", "venons", "venez", "viennent", "venir",
                  "retourne", "retournons", "arrive", "arrivons", "arrivent",
                  "pense", "penses", "pensons", "commence", "commencent",
                  "reste", "restons", "restent", "monte", "descend"}

# Points de vigilance : paires qu'aucune règle simple ne tranche.
# Ils sont MONTRÉS (si l'enseignant le souhaite) mais JAMAIS COMPTÉS.
VIGILANCE = {
    "ces": "« ces » (je montre) ou « ses » (à lui, à elle) ?",
    "ses": "« ses » (à lui, à elle) ou « ces » (je montre) ?",
    "ou": "« ou » (= ou bien) ou « où » (le lieu) ?",
    "où": "« où » (le lieu) ou « ou » (= ou bien) ?",
    "la": "« la » (déterminant), « là » (le lieu) ou « l'a » (verbe avoir) ?",
    "là": "« là » (le lieu) ou « la » (déterminant) ?",
    "mes": "« mes » (à moi) ou « mais » (opposition) ?",
    "mais": "« mais » (opposition) ou « mes » (à moi) ?",
    "sa": "« sa » (à elle) ou « ça » (= cela) ?",
    "leur": "« leur » (à eux) ou « leurs » (plusieurs) ?",
}

# Conservé pour mémoire, plus utilisé pour signaler.
HOMOPHONES = {
    "a": "« a » (verbe avoir) ou « à » (préposition) ? Remplace par « avait » pour vérifier.",
    "à": "« à » (préposition) ou « a » (verbe avoir) ? Remplace par « avait » pour vérifier.",
    "et": "« et » (= et puis) ou « est » (= était) ? Remplace par « était ».",
    "est": "« est » (= était) ou « et » (= et puis) ?",
    "son": "« son » (le sien) ou « sont » (= étaient) ?",
    "sont": "« sont » (= étaient) ou « son » (le sien) ?",
    "ou": "« ou » (= ou bien) ou « où » (le lieu) ?",
    "où": "« où » (le lieu) ou « ou » (= ou bien) ?",
    "ces": "« ces » (montrer) / « ses » (à lui) / « c'est » / « s'est » ?",
    "ses": "« ses » (à lui) / « ces » (montrer) / « c'est » / « s'est » ?",
    "cest": "Écrire « c'est » avec l'apostrophe.",
    "on": "« on » (= il) ou « ont » (= avaient) ?",
    "ont": "« ont » (= avaient) ou « on » (= il) ?",
    "la": "« la » (déterminant) / « là » (le lieu) / « l'a » (verbe avoir) ?",
    "là": "« là » (le lieu) ou « la » (déterminant) ?",
    "se": "« se » (pronom) ou « ce » (montrer) ?",
    "ce": "« ce » (montrer) ou « se » (pronom) ?",
    "mais": "« mais » (opposition) ou « mes » (à moi) ?",
    "mes": "« mes » (à moi) ou « mais » (opposition) ?",
    "peu": "« peu » (quantité) ou « peut » (verbe pouvoir) ?",
    "peut": "« peut » (verbe pouvoir) ou « peu » (quantité) ?",
}

# Erreurs orthographiques fréquentes : forme fautive -> forme correcte
ORTHO_FREQUENTES = {
    "malgres": "malgré", "parceque": "parce que", "biensur": "bien sûr",
    "aujourdhui": "aujourd'hui", "quelquefois": "quelquefois", "beacoup": "beaucoup",
    "beaucous": "beaucoup", "toujour": "toujours", "apres": "après", "tres": "très",
    "etre": "être", "meme": "même", "deja": "déjà", "voila": "voilà", "ou": None,
    "language": "langage", "developpement": "développement", "different": "différent",
    "exemple": None, "connaitre": "connaître", "ecole": "école", "eleve": "élève",
    "enfin": None, "enfant": None, "je suit": "je suis", "sa va": "ça va",
    "quand meme": "quand même", "tous les jour": "tous les jours",
}

# Mots collés à séparer (segmentation)
SEGMENTATION = {
    "parceque": "parce que", "aumoins": "au moins", "toutdesuite": "tout de suite",
    "toutefois": None, "biensur": "bien sûr", "apeuprès": "à peu près",
    "beaucoupde": "beaucoup de", "ilya": "il y a", "cestadire": "c'est-à-dire",
    "amoi": "à moi", "atoi": "à toi", "surtout": None, "enplus": "en plus",
    "quelquun": "quelqu'un", "dabord": "d'abord", "acote": "à côté",
}

# --- Mots courants qui portent un accent : leur version sans accent est fautive.
ACCENTUES = {
    "ecole": "école", "eleve": "élève", "eleves": "élèves", "tres": "très",
    "apres": "après", "mere": "mère", "pere": "père", "frere": "frère",
    "eleve": "élève", "recre": "récré", "recreation": "récréation",
    "reponse": "réponse", "problem": "problème", "probleme": "problème",
    "modele": "modèle", "college": "collège", "eleve": "élève",
    "cafe": "café", "ete": "été", "deja": "déjà", "voila": "voilà",
    "cle": "clé", "the": "thé", "fete": "fête", "tete": "tête", "foret": "forêt",
    "meme": "même", "etre": "être", "arret": "arrêt", "gout": "goût",
    "cout": "coût", "ile": "île", "hopital": "hôpital", "theatre": "théâtre",
    "prefere": "préfère", "espere": "espère", "achete": "achète",
    "premiere": "première", "derniere": "dernière", "lumiere": "lumière",
    "riviere": "rivière", "maniere": "manière", "colere": "colère",
    "bibliotheque": "bibliothèque", "geographie": "géographie",
    "mathematiques": "mathématiques", "recreations": "récréations",
    "elephant": "éléphant", "etudier": "étudier", "ecrire": "écrire",
    "ecouter": "écouter", "epoque": "époque", "energie": "énergie",
    "numero": "numéro", "idee": "idée", "annee": "année", "journee": "journée",
    "matinee": "matinée", "soiree": "soirée", "entree": "entrée",
    "chateau": "château", "foret": "forêt", "pate": "pâte", "age": "âge",
}

# --- Auxiliaires : après « a / ont / est / sont / avez… », un verbe du 1er groupe
#     se met au PARTICIPE (-é), jamais à l'infinitif (-er). C'est LA faute
#     la plus fréquente de l'école primaire.
AUXILIAIRES = {"a", "as", "ai", "avons", "avez", "ont", "avait", "avaient",
               "est", "es", "suis", "sommes", "êtes", "sont", "était", "étaient",
               "sera", "serai", "seront"}

# --- Devant ces mots, c'est au contraire l'INFINITIF (-er) qu'il faut.
AVANT_INFINITIF = {"pour", "de", "à", "sans", "peut", "peux", "veut", "veux",
                   "doit", "dois", "va", "vais", "vas", "vont", "allons",
                   "faut", "aime", "aimes", "sait", "sais", "commence", "finit"}

# Lexique : répétitions / mots trop vagues
MOTS_VAGUES = {"truc", "machin", "chose", "faire", "mettre", "avoir", "bien", "super",
               "trop", "genre"}


def _ressemble_verbe(mot: str) -> bool:
    """Heuristique simple : ce mot pourrait-il être un verbe conjugué ?"""
    if not mot or len(mot) < 3:
        return False
    return mot.endswith(("e", "es", "ent", "ons", "ez", "it", "is", "ait",
                         "aient", "era", "ait", "t", "a"))


class Signalement:
    """Un repérage dans le texte.

    certain = True  → c'est une VRAIE erreur. Elle est comptée dans le score.
    certain = False → simple point de vigilance (« vérifie ce mot »).
                      Il est montré autrement et n'est JAMAIS compté comme une
                      erreur : sans quoi un élève qui a juste serait pénalisé.
    """

    def __init__(self, debut, fin, mot, categorie, message, suggestion="",
                 certain=True):
        self.debut = debut
        self.fin = fin
        self.mot = mot
        self.categorie = categorie
        self.message = message
        self.suggestion = suggestion
        self.certain = certain

    def __repr__(self):
        return f"<{self.categorie} '{self.mot}' @{self.debut}>"


def analyser(texte: str):
    """Renvoie la liste des signalements détectés dans le texte."""
    sigs = []
    if not texte or not texte.strip():
        return sigs

    mots = list(MOT.finditer(texte))
    formes = [m.group(0).lower() for m in mots]
    formes_sa = [sans_accent(f) for f in formes]

    # ---------- MAJUSCULES : début de phrase ----------
    for m in re.finditer(r"(^|[.!?…]\s+)([a-zà-öø-ÿ])", texte):
        pos = m.start(2)
        sigs.append(Signalement(pos, pos + 1, m.group(2), "majuscule",
                                "Une phrase commence par une majuscule.",
                                m.group(2).upper()))

    # ---------- PONCTUATION ----------
    t = texte.rstrip()
    if t and t[-1] not in ".!?…":
        sigs.append(Signalement(len(t) - 1, len(t), t[-1], "ponctuation",
                                "La dernière phrase ne se termine pas par un point."))
    for m in re.finditer(r"\s+([,.;:!?])", texte):   # espace avant , ou .
        if m.group(1) in ",.":
            sigs.append(Signalement(m.start(), m.end(), m.group(0), "ponctuation",
                                    "Pas d'espace avant la virgule ni avant le point.",
                                    m.group(1)))
    for m in re.finditer(r"[,.;:](?=[A-Za-zÀ-ÿ])", texte):  # pas d'espace après
        sigs.append(Signalement(m.start(), m.end(), m.group(0), "ponctuation",
                                "Il manque une espace après le signe de ponctuation."))

    # ---------- Analyse mot à mot ----------
    for i, m in enumerate(mots):
        forme = formes[i]
        forme_sa = formes_sa[i]
        d, f = m.start(), m.end()

        # SEGMENTATION
        if forme_sa in SEGMENTATION and SEGMENTATION[forme_sa]:
            sigs.append(Signalement(d, f, m.group(0), "segmentation",
                                    f"Ce mot s'écrit en plusieurs mots.",
                                    SEGMENTATION[forme_sa]))
            continue

        # ORTHOGRAPHE fréquente
        if forme_sa in ORTHO_FREQUENTES and ORTHO_FREQUENTES[forme_sa] \
                and forme != ORTHO_FREQUENTES[forme_sa]:
            sigs.append(Signalement(d, f, m.group(0), "orthographe",
                                    "Orthographe à vérifier.",
                                    ORTHO_FREQUENTES[forme_sa]))
            continue

        # HOMOPHONES — uniquement si le contexte le prouve.
        prec = formes[i - 1] if i > 0 else ""
        suiv_f = formes[i + 1] if i + 1 < len(mots) else ""

        for fautif, declencheurs, correct, expl in REGLES_HOMOPHONES:
            if forme == fautif and prec in declencheurs:
                # « ce » ne devient « se » que devant un verbe
                if fautif == "ce" and not _ressemble_verbe(suiv_f):
                    continue
                sigs.append(Signalement(
                    d, f, m.group(0), "homophone",
                    expl.format(prec=prec), correct))
                break
        else:
            # « il va a l'école » → « à » (préposition)
            if forme == "a" and prec in VERBES_AVANT_A:
                sigs.append(Signalement(
                    d, f, m.group(0), "homophone",
                    f"Après « {prec} », c'est la préposition « à », avec l'accent.",
                    "à"))
            # Points de vigilance : montrés, jamais comptés.
            elif forme in VIGILANCE:
                sigs.append(Signalement(d, f, m.group(0), "homophone",
                                        VIGILANCE[forme], "", certain=False))

        # ACCORD dans le groupe nominal : déterminant pluriel + mot sans -s/-x
        if i + 1 < len(mots) and forme in DETERMINANTS_PLURIEL:
            suiv = mots[i + 1]
            sf = formes[i + 1]
            if (len(sf) > 3 and not sf.endswith(("s", "x", "z"))
                    and sf not in INVARIABLES and sf not in PRONOMS_SUJETS):
                sigs.append(Signalement(suiv.start(), suiv.end(), suiv.group(0), "accord",
                                        f"Après « {forme} » (pluriel), le nom se met "
                                        f"souvent au pluriel.", sf + "s"))
        # déterminant singulier + mot en -s
        if i + 1 < len(mots) and forme in DETERMINANTS_SINGULIER:
            suiv = mots[i + 1]
            sf = formes[i + 1]
            if (len(sf) > 4 and sf.endswith("s") and sans_accent(sf) not in INVARIABLES):
                sigs.append(Signalement(suiv.start(), suiv.end(), suiv.group(0), "accord",
                                        f"Après « {forme} » (singulier), pourquoi un « s » ?",
                                        sf[:-1]))

        # CONJUGAISON : pronom sujet + verbe à terminaison douteuse
        if forme in PRONOMS_SUJETS and i + 1 < len(mots):
            pers = PRONOMS_SUJETS[forme]
            suiv = mots[i + 1]
            sf = formes[i + 1]
            if sf in PRONOMS_SUJETS or sf in ("ne", "n", "se", "s", "me", "te", "le",
                                              "la", "les", "lui", "y", "en"):
                continue
            if len(sf) < 3:
                continue
            attendues = TERMINAISONS_PRESENT[pers]
            if not any(sf.endswith(t) for t in attendues):
                # Filtrage : on ignore les participes/infinitifs évidents
                if not sf.endswith(("er", "ir", "re", "é", "ée", "és", "ées", "i", "u")):
                    sigs.append(Signalement(
                        suiv.start(), suiv.end(), suiv.group(0), "conjugaison",
                        f"Avec « {forme} », la terminaison attendue est "
                        f"« -{ ' » ou « -'.join(attendues) } »."))
            # cas classiques
            if pers == "3p" and sf.endswith("e") and not sf.endswith("ent"):
                sigs.append(Signalement(suiv.start(), suiv.end(), suiv.group(0),
                                        "conjugaison",
                                        "Avec « ils/elles », le verbe se termine par « -ent ».",
                                        sf + "nt"))

        # ORTHOGRAPHE : accent manquant sur un mot courant
        if forme in ACCENTUES and forme != ACCENTUES[forme]:
            sigs.append(Signalement(d, f, m.group(0), "orthographe",
                                    "Il manque un accent.", ACCENTUES[forme]))

        # CONJUGAISON : « -er » / « -é », la confusion la plus fréquente
        if forme.endswith("er") and len(forme) > 3 and i > 0:
            prec2 = formes[i - 1]
            if prec2 in AUXILIAIRES:
                sigs.append(Signalement(
                    d, f, m.group(0), "conjugaison",
                    f"Après « {prec2} », c'est le participe passé : essaie de "
                    f"remplacer par « vendu » — si ça marche, écris « -é ».",
                    forme[:-2] + "é"))
        if forme.endswith("é") and len(forme) > 2 and i > 0:
            prec2 = formes[i - 1]
            if prec2 in AVANT_INFINITIF and prec2 not in AUXILIAIRES:
                sigs.append(Signalement(
                    d, f, m.group(0), "conjugaison",
                    f"Après « {prec2} », c'est l'infinitif : essaie de remplacer "
                    f"par « vendre » — si ça marche, écris « -er ».",
                    forme[:-1] + "er"))

        # ACCORD : adjectif après un nom pluriel (« les fleurs rouge »)
        if (i >= 2 and formes[i - 2] in DETERMINANTS_PLURIEL
                and formes[i - 1].endswith(("s", "x"))
                and len(forme) > 3 and not forme.endswith(("s", "x"))
                and forme_sa not in INVARIABLES
                and forme not in PRONOMS_SUJETS
                and not forme.endswith(("er", "ir", "re", "ez", "ons", "ent"))):
            sigs.append(Signalement(
                d, f, m.group(0), "accord",
                f"« {formes[i - 1]} » est au pluriel : l'adjectif qui le décrit "
                f"se met aussi au pluriel.", forme + "s"))

        # LEXIQUE : mots vagues
        if forme_sa in {"truc", "machin", "genre"}:
            sigs.append(Signalement(d, f, m.group(0), "lexique",
                                    "Mot trop vague : trouve un mot plus précis.",
                                    certain=False))

    # LEXIQUE : répétition d'un même mot long dans une même phrase
    for phrase in re.finditer(r"[^.!?…]+", texte):
        seg = phrase.group(0)
        offset = phrase.start()
        vus = {}
        for m in MOT.finditer(seg):
            w = m.group(0).lower()
            if len(w) < 5 or w in INVARIABLES:
                continue
            if w in vus:
                sigs.append(Signalement(offset + m.start(), offset + m.end(),
                                        m.group(0), "lexique",
                                        f"« {w} » est répété dans la phrase. "
                                        f"Cherche un synonyme.",
                                        certain=False))
            vus[w] = True

    # Dédoublonnage sur (debut, categorie)
    uniques, vus = [], set()
    for s in sorted(sigs, key=lambda x: x.debut):
        cle = (s.debut, s.categorie)
        if cle not in vus:
            vus.add(cle)
            uniques.append(s)
    return uniques


def certaines(sigs):
    """Les vraies erreurs — les seules qui comptent dans le score."""
    return [s for s in sigs if getattr(s, "certain", True)]


def vigilances(sigs):
    """Les points à vérifier — montrés, jamais comptés."""
    return [s for s in sigs if not getattr(s, "certain", True)]


def compter_par_categorie(sigs):
    """Ne compte QUE les erreurs certaines."""
    d = {}
    for s in certaines(sigs):
        d[s.categorie] = d.get(s.categorie, 0) + 1
    return d
