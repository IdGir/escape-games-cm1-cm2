"""Détection des erreurs par comparaison avec un texte de référence.

Quand on CONNAÎT la version correcte du texte (texte généré par l'application,
ou texte de la banque dont l'enseignant a fourni le corrigé), il est inutile de
deviner les erreurs avec des règles : il suffit de comparer.

C'est la méthode la plus sûre — elle ne peut produire AUCUN faux positif :
un mot identique au corrigé n'est jamais signalé.

Le rapprochement se fait au niveau du mot (difflib), ce qui tolère qu'un élève
ajoute ou supprime des mots sans que tout se décale.
"""
import difflib
import re
import unicodedata

from correction_engine import Signalement

# On découpe en gardant TOUT (mots, ponctuation, espaces) pour pouvoir
# retrouver les positions exactes dans le texte.
JETON = re.compile(r"\w+|[^\w\s]|\s+", re.UNICODE)
MOT = re.compile(r"\w", re.UNICODE)


def _jetons(texte):
    """Renvoie [(texte_du_jeton, debut, fin), ...]"""
    return [(m.group(0), m.start(), m.end()) for m in JETON.finditer(texte)]


def _cle(j):
    """Clé de comparaison.

    La CASSE est conservée : sinon « le boulanger » et « Le boulanger » seraient
    jugés identiques, et la faute de majuscule passerait inaperçue.
    Les espaces multiples sont ramenés à une seule espace.
    """
    t = j[0]
    return " " if t.isspace() else t


def _sans_accent(m):
    return "".join(c for c in unicodedata.normalize("NFD", m.lower())
                   if unicodedata.category(c) != "Mn")


# ---------------------------------------------------------------- Catégorisation
HOMOPHONES_PAIRES = {
    frozenset(("a", "à")), frozenset(("et", "est")), frozenset(("son", "sont")),
    frozenset(("on", "ont")), frozenset(("ou", "où")), frozenset(("ce", "se")),
    frozenset(("ces", "ses")), frozenset(("la", "là")), frozenset(("l'a", "la")),
    frozenset(("mes", "mais")), frozenset(("peu", "peut")), frozenset(("ni", "n'y")),
    frozenset(("sa", "ça")), frozenset(("ma", "m'a")), frozenset(("leur", "leurs")),
    frozenset(("c'est", "s'est")), frozenset(("cest", "c'est")),
}

# --------------------------------------------------------------------------
#  Verbe ou groupe nominal ?
#
#  C'est LA distinction délicate. « prend → prends » et « feuille → feuilles »
#  se ressemblent : dans les deux cas, seul un « s » final change. Pourtant
#  l'un est une erreur de conjugaison et l'autre un accord du groupe nominal.
#  Les confondre fausse tout le suivi et envoie l'élève vers la mauvaise leçon.
#
#  On tranche en trois temps :
#    1. terminaison exclusivement verbale  → conjugaison, sans hésiter
#    2. terminaison exclusivement nominale → accord
#    3. terminaison ambiguë (s, e, t…)     → on regarde le MOT D'AVANT dans la
#       phrase : après « ils », c'est un verbe ; après « les », c'est un nom.
# --------------------------------------------------------------------------

# Terminaisons qu'aucun nom ni adjectif ne porte : elles suffisent à conclure.
SUFFIXES_VERBE = {
    # présent
    "ent", "nt", "ons", "ez", "ont", "issent", "issons", "issez", "is", "it",
    # imparfait
    "ais", "ait", "aient", "ions", "iez",
    # futur et conditionnel
    "era", "eras", "erez", "erons", "eront", "erai", "erais", "erait",
    "eraient", "rai", "ras", "ra", "rez", "rons", "ront", "rait", "raient",
    # passé simple et subjonctif
    "èrent", "âmes", "âtes", "asse", "assent", "isse", "issions",
    # infinitif / participe
    "er", "ir", "re", "é", "és", "ée", "ées", "ant",
}

# Terminaisons typiques du groupe nominal, jamais verbales.
SUFFIXES_NOM = {"aux", "eaux", "eux", "ux", "ale", "ales", "elle", "elles",
                "euse", "euses", "ive", "ives", "ère", "ères", "trice",
                "ales", "ales", "ails", "als"}

# Couples infinitif / participe : l'erreur la plus fréquente du cycle 3.
COUPLES_VERBE = {frozenset(("er", "é")), frozenset(("er", "ée")),
                 frozenset(("er", "és")), frozenset(("er", "ées")),
                 frozenset(("é", "ait")), frozenset(("i", "it")),
                 frozenset(("is", "it")), frozenset(("s", "t"))}

# Ce qui annonce un VERBE juste après.
PRONOMS_SUJETS = {"je", "j'", "tu", "il", "elle", "on", "nous", "vous",
                  "ils", "elles", "ce", "c'", "qui", "se", "s'", "me", "m'",
                  "te", "t'", "le", "la", "les", "lui", "leur", "y", "en",
                  "ne", "n'"}
# Attention : le/la/les sont ambigus (déterminant OU pronom complément).
# On ne les retient donc que s'ils ne peuvent pas être des déterminants,
# ce que la liste ci-dessous permet de trancher.
DETERMINANTS = {"le", "la", "les", "un", "une", "des", "du", "de", "au", "aux",
                "mon", "ma", "mes", "ton", "ta", "tes", "son", "sa", "ses",
                "notre", "nos", "votre", "vos", "leur", "leurs", "ce", "cet",
                "cette", "ces", "quel", "quelle", "quels", "quelles",
                "plusieurs", "quelques", "certains", "chaque", "tout", "tous",
                "toute", "toutes", "deux", "trois", "quatre", "cinq"}
# Auxiliaires : ce qui suit est un participe passé, donc de la conjugaison.
AUXILIAIRES = {"ai", "as", "a", "avons", "avez", "ont", "avais", "avait",
               "avaient", "suis", "es", "est", "sommes", "êtes", "sont",
               "étais", "était", "étaient", "serai", "sera", "seront"}


# Attention : MOT vaut « \w » (UN caractère). Il faut donc notre propre motif
# pour découper une phrase en mots entiers.
MOT_ENTIER = re.compile(r"[\wÀ-ÿ]+['’]?", re.UNICODE)


def _nature_probable(mot: str) -> str:
    """« verbe », « nom », « adjectif » ou « » d'après le dictionnaire embarqué.

    Le dictionnaire ne contient que les formes de base : on essaie donc aussi
    le singulier, le masculin et l'infinitif avant de renoncer. C'est bien plus
    fiable que de deviner d'après la phrase.
    """
    try:
        import dictionnaire as dico
    except Exception:
        return ""
    m = (mot or "").lower().strip()
    if not m:
        return ""

    essais = [m]
    if m.endswith(("s", "x")):
        essais.append(m[:-1])                 # pluriel → singulier
    if m.endswith("es"):
        essais.append(m[:-2])
    if m.endswith("e"):
        essais.append(m[:-1])                 # féminin → masculin
    if m.endswith("aux"):
        essais.append(m[:-3] + "al")          # journaux → journal

    for e in essais:
        infos = dico.infos(e)
        if infos:
            nature = infos["nature"]
            if nature.startswith("nom"):
                return "nom"
            if nature.startswith("adjectif"):
                return "adjectif"
            if nature.startswith("verbe"):
                return "verbe"

    # Aucune forme trouvée : le mot est peut-être une forme conjuguée. On
    # tente de reconstruire son infinitif.
    for radical in (m, m.rstrip("aeiouszxt")):
        if len(radical) < 2:
            continue
        for fin in ("er", "ir", "re"):
            infos = dico.infos(radical + fin)
            if infos and infos["nature"].startswith("verbe"):
                return "verbe"
    return ""


def _indice_contexte(contexte_avant: str) -> str:
    """« verbe », « nom » ou « » d'après le mot qui précède l'erreur."""
    if not contexte_avant:
        return ""
    mots = MOT_ENTIER.findall(contexte_avant.lower())
    if not mots:
        return ""
    precedent = mots[-1].rstrip("'’")
    # « Les enfants joue » : le déterminant est deux mots plus tôt, mais le
    # mot juste avant (« enfants ») est un nom au pluriel — donc ce qui suit
    # est bien un verbe. On regarde donc aussi l'avant-dernier mot.
    if precedent not in PRONOMS_SUJETS and precedent not in DETERMINANTS \
            and precedent not in AUXILIAIRES and len(mots) >= 2:
        avant = mots[-2].rstrip("'’")
        if avant in DETERMINANTS:
            return "verbe"      # déterminant + nom + X → X est un verbe
    if precedent in AUXILIAIRES:
        return "verbe"
    # Un pronom sujet non ambigu annonce un verbe.
    if precedent in PRONOMS_SUJETS and precedent not in DETERMINANTS:
        return "verbe"
    if precedent in DETERMINANTS:
        return "nom"
    return ""


def categoriser(faux: str, juste: str, contexte_avant: str = "") -> str:
    """Déduit la catégorie d'erreur en comparant la forme fautive et la correcte.

    `contexte_avant` : le texte qui précède l'erreur. Il sert à trancher les
    cas ambigus — sans lui, « tu prend » serait rangé dans les accords.
    """
    if not faux:
        return "orthographe"
    if not juste:
        return "lexique"

    f, j = faux.lower(), juste.lower()

    # Majuscule : mêmes lettres, casse différente
    if f == j and faux != juste:
        return "majuscule"

    # Ponctuation
    if not MOT.search(faux) or not MOT.search(juste):
        return "ponctuation"

    # Segmentation : le corrigé contient une espace ou une apostrophe en plus
    if (" " in juste and " " not in faux) or \
       (juste.replace(" ", "").replace("'", "") == faux.replace("'", "")
            and juste != faux):
        return "segmentation"

    # Homophone : paire connue
    if frozenset((f, j)) in HOMOPHONES_PAIRES:
        return "homophone"

    # Radical commun aux deux formes
    racine = min(len(f), len(j))
    commun = 0
    while commun < racine and f[commun] == j[commun]:
        commun += 1
    suf_f, suf_j = f[commun:], j[commun:]

    indice = _indice_contexte(contexte_avant)

    # 1. Terminaison exclusivement verbale : c'est de la conjugaison, point.
    #    (« souffle → soufflent » n'est pas un accord du groupe nominal.)
    if commun >= 2 and (suf_f in SUFFIXES_VERBE or suf_j in SUFFIXES_VERBE):
        return "conjugaison"

    # Même chose quand le radical change un peu : « dort → dorment ».
    # Les terminaisons -ent, -ons, -ez, -ont n'existent que sur des verbes.
    if commun >= 2 and any(s.endswith(("ent", "ons", "ez", "ont"))
                           for s in (suf_f, suf_j) if s):
        return "conjugaison"

    # 2. Couple infinitif / participe : « je suis aller → allé ».
    if commun >= 2 and frozenset((suf_f, suf_j)) in COUPLES_VERBE:
        return "conjugaison"

    # 3. Terminaison exclusivement nominale : accord du groupe nominal.
    if commun >= 2 and (suf_f in SUFFIXES_NOM or suf_j in SUFFIXES_NOM):
        return "accord"

    # 4. Cas ambigu : seul un e / s / x / t final change. « prend → prends »
    #    et « feuille → feuilles » ont ici exactement la même forme. Seule la
    #    phrase permet de décider, alors on la regarde.
    if f.rstrip("esxt") == j.rstrip("esxt") and f != j:
        # On demande d'abord au dictionnaire ce qu'est ce mot : c'est un fait,
        # pas une supposition. « rouges » est un adjectif, « prends » un verbe.
        nature = _nature_probable(j) or _nature_probable(f)
        if nature == "verbe":
            return "conjugaison"
        if nature in ("nom", "adjectif"):
            return "accord"
        # Le dictionnaire ne connaît pas ce mot : on se rabat sur la phrase.
        if indice == "verbe":
            return "conjugaison"
        if indice == "nom":
            return "accord"
        # Sans rien : l'accord reste le cas le plus fréquent à l'écrit.
        return "accord"

    # Orthographe : mêmes lettres à l'accent près
    if _sans_accent(f) == _sans_accent(j):
        return "orthographe"

    # Même début, longueur voisine : faute d'orthographe lexicale
    if commun >= 3 and abs(len(f) - len(j)) <= 3:
        return "orthographe"

    # Dernier filet : les deux mots se prononcent-ils pareil ? « fotes » et
    # « fautes » n'ont qu'une lettre en commun au début, mais l'élève a bien
    # écrit ce qu'il entendait — c'est de l'orthographe, pas du vocabulaire.
    try:
        import phonetique as ph
        sf, sj = ph.sons(f), ph.sons(j)
        if sf and sj:
            if sf == sj:
                return "orthographe"
            if ph.distance_sons(sf, sj) / max(len(sf), len(sj)) <= 0.34:
                return "orthographe"
    except Exception:
        pass

    return "lexique"


MESSAGES = {
    "accord":       "Vérifie l'accord (singulier ou pluriel ? masculin ou féminin ?).",
    "conjugaison":  "Vérifie la terminaison du verbe : qui est-ce qui fait l'action ?",
    "homophone":    "Deux mots se prononcent pareil ici. Lequel convient ?",
    "orthographe":  "L'orthographe de ce mot n'est pas la bonne.",
    "segmentation": "Ce mot est mal découpé.",
    "ponctuation":  "Problème de ponctuation.",
    "majuscule":    "Problème de majuscule.",
    "lexique":      "Ce mot ne convient pas ici.",
}


# ---------------------------------------------------------------- Comparaison
def analyser_avec_reference(texte_actuel: str, texte_reference: str,
                            categories: dict | None = None):
    """Signale UNIQUEMENT ce qui diffère réellement du corrigé.

    `categories` : quand l'application a elle-même fabriqué le texte, elle sait
    quelle catégorie elle a injectée pour chaque mot. On l'utilise en priorité,
    et on ne retombe sur la déduction que pour les écarts inattendus.

    Renvoie une liste de Signalement, tous certains : aucun faux positif possible.
    """
    if not texte_reference or not texte_reference.strip():
        return []

    ja = _jetons(texte_actuel)
    jr = _jetons(texte_reference)
    a = [_cle(x) for x in ja]
    b = [_cle(x) for x in jr]

    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    sigs = []

    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue

        faux = "".join(x[0] for x in ja[i1:i2])
        juste = "".join(x[0] for x in jr[j1:j2])

        # --- Écarts qui ne portent que sur des espaces : ce sont des fautes
        #     de ponctuation (espace avant la virgule, espace manquante…).
        if not faux.strip() and not juste.strip():
            if faux and not juste:          # une espace en trop chez l'élève
                debut, fin = ja[i1][1], ja[i2 - 1][2]
                voisin = texte_actuel[fin:fin + 1]
                msg = ("Pas d'espace avant une virgule ni avant un point."
                       if voisin in ",.;:!?" else "Espace en trop.")
                sigs.append(Signalement(debut, fin, " ", "ponctuation", msg, ""))
            elif juste and not faux:        # une espace manque
                pos = ja[i1][1] if i1 < len(ja) else len(texte_actuel)
                sigs.append(Signalement(
                    max(0, pos - 1), min(len(texte_actuel), pos + 1), "",
                    "ponctuation", "Il manque une espace ici.", " "))
            continue

        if op == "insert":
            # Un mot du corrigé manque : on marque la jointure.
            if not juste.strip():
                continue
            pos = ja[i1][1] if i1 < len(ja) else len(texte_actuel)
            sigs.append(Signalement(
                max(0, pos - 1), min(len(texte_actuel), pos + 1), "",
                "lexique", f"Il manque quelque chose ici : « {juste.strip()} ».",
                juste.strip()))
            continue

        if op == "delete":
            debut, fin = ja[i1][1], ja[i2 - 1][2]
            sigs.append(Signalement(
                debut, fin, faux.strip(), "lexique",
                "Ce mot est en trop.", ""))
            continue

        # remplacement
        debut, fin = ja[i1][1], ja[i2 - 1][2]
        # on recadre sur la partie non-espace
        while debut < fin and texte_actuel[debut].isspace():
            debut += 1
        while fin > debut and texte_actuel[fin - 1].isspace():
            fin -= 1
        if fin <= debut:
            continue

        f_net, j_net = faux.strip(), juste.strip()
        cat = None
        if categories:
            cat = categories.get((f_net.lower(), j_net.lower()))
        if not cat:
            # Les 40 caractères qui précèdent suffisent à savoir si le mot
            # suit un pronom sujet (verbe) ou un déterminant (nom).
            cat = categoriser(f_net, j_net, texte_actuel[max(0, debut - 40):debut])
        sigs.append(Signalement(debut, fin, f_net, cat, MESSAGES[cat], j_net))

    return sorted(sigs, key=lambda s: s.debut)


def a_une_reference(origine: str, reference: str) -> bool:
    return bool(reference and reference.strip())
