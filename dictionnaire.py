"""dictionnaire.py — Le dictionnaire qui comprend l'orthographe approximative.

Un dictionnaire papier suppose qu'on sache déjà écrire le mot : c'est
exactement ce qui manque à l'élève qui le cherche. Ici, il écrit le mot comme
il l'entend — « éléfan », « oizo », « ortografe » — et l'application lui
propose les mots qui SONNENT pareil, du plus probable au moins probable.

Il clique alors sur un mot pour lire sa définition, et choisit lui-même.
C'est ce dernier geste qui fait tout l'intérêt pédagogique : l'élève n'est pas
corrigé, il tranche.

Trois sources de définition, dans cet ordre :
  1. la mémoire de l'application (définitions déjà obtenues, jamais redemandées)
  2. la banque intégrée (les mots que les enfants confondent le plus)
  3. l'IA, si l'enseignant en a activé une — et le résultat est mémorisé

Sans IA et hors banque, on affiche quand même la nature du mot et les mots de
sa famille : de quoi choisir entre « ver », « vers », « verre » et « vert ».
"""
import os
import threading

import phonetique as ph
from paths import dossier_ressources

_FICHIER = os.path.join(str(dossier_ressources()), "data_dictionnaire.txt")

# --------------------------------------------------------------------------
#  Chargement (une seule fois, à la première recherche)
# --------------------------------------------------------------------------
_MOTS = []            # [(mot, nature, [codes], rang)]
_PAR_CODE = {}        # code phonétique → [indices dans _MOTS]
_PAR_MOT = {}         # mot → indice
_charge = False
_verrou = threading.Lock()


def _charger():
    global _charge
    with _verrou:
        if _charge:
            return
        if os.path.exists(_FICHIER):
            with open(_FICHIER, encoding="utf-8") as f:
                for ligne in f:
                    if ligne.startswith("#"):
                        continue
                    parties = ligne.rstrip("\n").split("\t")
                    if len(parties) < 4:
                        continue
                    mot, nature, codes, rang = parties[0], parties[1], \
                        parties[2].split("|"), int(parties[3])
                    i = len(_MOTS)
                    _MOTS.append((mot, nature, codes, rang))
                    _PAR_MOT[mot] = i
                    for c in codes:
                        _PAR_CODE.setdefault(c, []).append(i)
        _charge = True


def disponible():
    _charger()
    return bool(_MOTS)


def nombre_de_mots():
    _charger()
    return len(_MOTS)


# --------------------------------------------------------------------------
#  Recherche par consonance
# --------------------------------------------------------------------------
def _codes_voisins(code):
    """Codes phonétiques à une petite retouche près du code cherché.

    On explore les confusions les plus courantes (E/I, O/U, S/Z…) plus les
    ajouts et suppressions d'un son. Cela suffit à rattraper l'immense
    majorité des essais d'un élève, sans parcourir les 70 000 mots.
    """
    voisins = {code}
    lettres = "AEIOUYQW123SZFVKGTDPBMNLRJCXH"
    for i in range(len(code)):
        voisins.add(code[:i] + code[i + 1:])                    # un son en trop
        for c in lettres:
            voisins.add(code[:i] + c + code[i + 1:])            # un son changé
            voisins.add(code[:i] + c + code[i:])                # un son oublié
    for c in lettres:
        voisins.add(code + c)
    return voisins


def chercher(essai, limite=12):
    """Les mots qui ressemblent le plus à ce que l'élève a écrit.

    Renvoie une liste de {mot, nature, score, exact, meme_son}.
    """
    _charger()
    essai = (essai or "").strip()
    if len(essai) < 2 or not _MOTS:
        return []

    code = ph.sons(essai)
    candidats = set()

    # 1. Le mot est peut-être déjà bien écrit.
    if essai.lower() in _PAR_MOT:
        candidats.add(_PAR_MOT[essai.lower()])

    # 2. Tous les mots qui se prononcent exactement pareil.
    for i in _PAR_CODE.get(code, []):
        candidats.add(i)

    # 3. Puis ceux qui s'en approchent à un son près.
    if len(candidats) < limite * 4:
        for c in _codes_voisins(code):
            for i in _PAR_CODE.get(c, []):
                candidats.add(i)
            if len(candidats) > 2500:      # garde-fou : on en a bien assez
                break

    if not candidats:
        return []

    resultats = []
    bas = essai.lower()
    for i in candidats:
        mot, nature, codes, rang = _MOTS[i]
        score = max(ph.ressemblance(essai, mot, sons_essai=code, sons_mot=c)
                    for c in codes)
        meme_son = code in codes
        # La fréquence départage : entre deux mots qui sonnent pareil, on
        # propose d'abord celui que l'enfant a une chance de connaître.
        bonus = {0: 9, 1: 6, 2: 1, 3: -6}[rang]
        resultats.append({
            "mot": mot, "nature": nature,
            "score": score, "tri": score + bonus,
            "exact": mot == bas, "meme_son": meme_son, "rang": rang,
        })

    resultats.sort(key=lambda r: (-r["tri"], r["rang"], len(r["mot"])))
    # On ne garde que des propositions crédibles : au-delà, ce serait du bruit.
    return [r for r in resultats if r["score"] >= 45][:limite]


def existe(mot):
    _charger()
    return (mot or "").strip().lower() in _PAR_MOT


def infos(mot):
    _charger()
    i = _PAR_MOT.get((mot or "").strip().lower())
    if i is None:
        return None
    m, nature, codes, rang = _MOTS[i]
    return {"mot": m, "nature": nature, "codes": codes, "rang": rang}


# --------------------------------------------------------------------------
#  Famille de mots — utile pour choisir, et pour les lettres muettes
# --------------------------------------------------------------------------
# Suffixes qui construisent réellement un mot dérivé en français. Un mot qui
# partage un début avec un autre n'est de sa famille que s'il s'en distingue
# par l'un de ces suffixes — sans quoi « écureuil » et « écureur » seraient
# donnés comme parents, ce qui n'a aucun sens.
SUFFIXES_DERIVES = {
    "", "e", "s", "es", "x",
    # noms d'action, d'agent, de lieu, de qualité
    "age", "ages", "ment", "ments", "ure", "ures", "tion", "ations", "ation",
    "sion", "ance", "ence", "ise", "esse", "eur", "eure", "eurs", "euse",
    "euses", "teur", "trice", "erie", "eries", "ier", "iers", "ière", "ières",
    "iste", "istes", "isme", "ette", "ettes", "elle", "ade", "aille",
    # adjectifs
    "eux", "euse", "al", "ale", "aux", "ales", "if", "ive", "ible", "able",
    "ables", "ain", "aine", "ien", "ienne", "ois", "oise", "u", "ue", "us",
    # verbes
    "er", "ir", "re", "ier", "iser", "ifier", "oyer", "eter", "iller",
    "é", "ée", "és", "ées", "ant", "ante", "ants", "issement",
}

# Préfixes qui construisent aussi une famille (re-dire, dé-faire…).
PREFIXES_DERIVES = ("re", "ré", "dé", "dés", "in", "im", "mal", "sur",
                    "sous", "pré", "entre")


def _radicaux(base):
    """Les débuts de mot qui peuvent servir de radical à une famille."""
    formes = {base}
    # On retire la terminaison propre du mot pour retrouver son radical :
    # « chanter » → « chant », « grande » → « grand », « poterie » → « pot ».
    for fin in sorted(SUFFIXES_DERIVES, key=len, reverse=True):
        if fin and base.endswith(fin) and len(base) - len(fin) >= 3:
            formes.add(base[: -len(fin)])
    # Un radical de trois lettres ne prouve rien : « ois » rapprocherait
    # « oiseau » de « oisif ». On exige quatre lettres au minimum.
    return {f for f in formes if len(f) >= 4}


def famille(mot, limite=8):
    """Mots vraiment construits sur le même radical (dent → dentiste, dentaire).

    On ne se contente PAS d'un début commun : le mot candidat doit se former à
    partir d'un radical du mot de départ, suivi d'un vrai suffixe de
    dérivation. C'est plus sévère, donc la liste est parfois vide — et c'est
    préférable : mieux vaut ne rien proposer qu'une fausse famille, puisque
    l'élève s'en sert pour retrouver une lettre muette.
    """
    _charger()
    base = (mot or "").strip().lower()
    if len(base) < 4:
        return []

    rads = _radicaux(base)
    plus_long = max(len(r) for r in rads)
    sortie = []
    for m, nature, codes, rang in _MOTS:
        if m == base or rang > 2 or len(m) < 4:
            continue
        for r in rads:
            if not m.startswith(r):
                continue
            reste = m[len(r):]
            if reste in SUFFIXES_DERIVES:
                # Un radical long est un indice bien plus sûr qu'un radical
                # de trois lettres : on trie là-dessus en premier.
                sortie.append((-len(r), rang, len(m), m, nature))
                break
        else:
            # Dérivation par préfixe : « dire » → « redire », « faire » → « défaire ».
            for p in PREFIXES_DERIVES:
                if not m.startswith(p):
                    continue
                apres = m[len(p):]
                for r in rads:
                    if apres.startswith(r) and apres[len(r):] in SUFFIXES_DERIVES:
                        sortie.append((-len(r), rang, len(m), m, nature))
                        break
                else:
                    continue
                break

    sortie.sort()
    # Les mots courants d'abord : un parent que l'élève ne connaît pas ne
    # l'aide en rien. On n'élargit aux mots ordinaires que si besoin.
    courants = [x for x in sortie if x[1] <= 1]
    if len(courants) >= 3:
        sortie = courants
    vus, propres = set(), []
    for _, rang, _l, m, n in sortie:
        if m in vus:
            continue
        vus.add(m)
        propres.append({"mot": m, "nature": n})
        if len(propres) >= limite:
            break
    return propres


# --------------------------------------------------------------------------
#  Définitions
# --------------------------------------------------------------------------
# Banque intégrée : les mots que les enfants confondent le plus. Ce sont
# précisément ceux pour lesquels une définition est indispensable au choix.
DEFINITIONS = {
    "ver": "Petit animal au corps mou et allongé, sans pattes. Le ver de terre creuse des galeries.",
    "vers": "1. En direction de. Il court vers la maison. — 2. Une ligne d'un poème.",
    "verre": "Matière transparente, ou récipient pour boire. Un verre d'eau.",
    "vert": "La couleur de l'herbe et des feuilles.",
    "vair": "Fourrure grise et blanche. La pantoufle de vair de Cendrillon.",
    "sang": "Le liquide rouge qui circule dans le corps.",
    "sans": "Le contraire de « avec ». Il est parti sans son manteau.",
    "cent": "Le nombre 100.",
    "sent": "Du verbe sentir. Il sent une bonne odeur.",
    "conte": "Une histoire imaginaire. Le conte du Petit Chaperon rouge.",
    "compte": "Un calcul, un total. Le compte est bon.",
    "comte": "Un titre de noblesse, comme un duc ou un baron.",
    "mer": "La grande étendue d'eau salée.",
    "mère": "La maman.",
    "maire": "La personne élue qui dirige une commune.",
    "père": "Le papa.",
    "paire": "Deux choses qui vont ensemble. Une paire de chaussures.",
    "pair": "Un nombre qui peut se diviser en deux parts égales : 2, 4, 6…",
    "cour": "L'espace de l'école où l'on joue pendant la récréation.",
    "cours": "1. Une leçon. — 2. Du verbe courir.",
    "court": "1. Le contraire de long. — 2. Du verbe courir.",
    "chant": "Ce qu'on chante, une mélodie avec des paroles.",
    "champ": "Un terrain cultivé. Un champ de blé.",
    "temps": "1. Les heures qui passent. — 2. La pluie, le soleil : la météo.",
    "tant": "Tellement, une si grande quantité. Il a tant travaillé.",
    "tante": "La sœur de ton père ou de ta mère.",
    "tente": "L'abri en toile qu'on monte pour camper.",
    "fin": "Le moment où quelque chose se termine.",
    "faim": "L'envie de manger.",
    "foi": "Le fait de croire en quelque chose.",
    "fois": "Une occasion, un moment. Je l'ai vu trois fois.",
    "foie": "L'organe du corps qui nettoie le sang.",
    "voie": "Un chemin, une route. La voie ferrée du train.",
    "voix": "Le son qui sort de la bouche quand on parle ou qu'on chante.",
    "point": "1. Le signe qui termine une phrase. — 2. Un endroit précis.",
    "poing": "La main fermée.",
    "pain": "L'aliment fait avec de la farine, cuit au four.",
    "pin": "Un arbre qui garde ses aiguilles vertes toute l'année.",
    "peau": "Ce qui recouvre le corps.",
    "pot": "Un récipient. Un pot de confiture.",
    "seau": "Un récipient avec une anse, pour porter de l'eau.",
    "saut": "L'action de sauter.",
    "sot": "Qui n'est pas intelligent, un peu bête.",
    "sceau": "Un cachet officiel qu'on imprime dans la cire.",
    "cane": "La femelle du canard.",
    "canne": "Le bâton sur lequel on s'appuie pour marcher.",
    "date": "Le jour, le mois et l'année.",
    "datte": "Le fruit sucré du palmier dattier.",
    "coup": "Un choc. Il a reçu un coup sur la tête.",
    "cou": "La partie du corps entre la tête et les épaules.",
    "coût": "Ce que quelque chose coûte, son prix.",
    "loup": "Un animal sauvage de la famille du chien.",
    "sur": "1. Au-dessus de. Le livre est sur la table. — 2. Un goût acide.",
    "sûr": "Certain. Je suis sûr de moi.",
    "dans": "À l'intérieur de. Le chat est dans la maison.",
    "dent": "Ce qui sert à mâcher dans la bouche.",
    "quand": "À quel moment. Quand arrives-tu ?",
    "quant": "Employé dans « quant à », qui veut dire « en ce qui concerne ».",
    "camp": "Un endroit où l'on installe des tentes.",
    "lait": "La boisson blanche donnée par la vache.",
    "laid": "Le contraire de beau.",
    "mai": "Le cinquième mois de l'année.",
    "mais": "Marque une opposition. Il pleut, mais je sors.",
    "mes": "Qui sont à moi. Mes chaussures.",
    "met": "Du verbe mettre. Il met son manteau.",
    "mets": "Un plat, ce qu'on mange.",
    "ses": "Qui sont à lui ou à elle. Ses affaires.",
    "ces": "Ceux-là, que je montre. Ces livres-là.",
    "sait": "Du verbe savoir. Il sait sa leçon.",
    "sais": "Du verbe savoir. Je sais nager.",
    "c'est": "Cela est. C'est mon frère.",
    "s'est": "Employé avec un verbe. Il s'est levé tôt.",
    "ou": "Marque un choix. Du thé ou du café ?",
    "où": "Marque le lieu. Où vas-tu ?",
    "a": "Du verbe avoir. Il a un vélo.",
    "à": "Marque le lieu ou le moment. Il va à l'école.",
    "et": "Ajoute une chose à une autre. Le pain et le beurre.",
    "est": "Du verbe être. Il est content.",
    "son": "1. Qui est à lui. Son cahier. — 2. Un bruit qu'on entend.",
    "sont": "Du verbe être. Ils sont partis.",
    "on": "Quelqu'un, les gens. On frappe à la porte.",
    "ont": "Du verbe avoir. Ils ont faim.",
    "la": "1. Devant un nom féminin. La maison. — 2. Une note de musique.",
    "là": "Marque le lieu. Reste là.",
    "leur": "1. Qui est à eux. Leur maison. — 2. À eux. Je leur parle.",
    "près": "À côté, pas loin. Il habite près de l'école.",
    "prêt": "Préparé, qui peut commencer. Je suis prêt.",
    "plus": "En plus grande quantité.",
    "plut": "Du verbe pleuvoir ou plaire.",
    "peu": "En petite quantité. Il mange peu.",
    "peut": "Du verbe pouvoir. Il peut venir.",
    "eau": "Le liquide transparent qu'on boit.",
    "haut": "Le contraire de bas.",
    "au": "Contraction de « à le ». Je vais au cinéma.",
    "os": "La partie dure du squelette.",
    "ancre": "La lourde pièce de métal qui retient un bateau au fond de l'eau.",
    "encre": "Le liquide coloré qui sert à écrire.",
    "amande": "Le fruit sec de l'amandier.",
    "amende": "Une somme d'argent à payer quand on n'a pas respecté une règle.",
    "balai": "L'objet qui sert à nettoyer le sol.",
    "ballet": "Un spectacle de danse.",
    "chaîne": "Une suite d'anneaux de métal.",
    "chêne": "Un grand arbre qui donne des glands.",
    "colle": "Ce qui sert à faire tenir deux choses ensemble.",
    "col": "1. Le haut d'un vêtement, autour du cou. — 2. Un passage en montagne.",
    "cygne": "Un grand oiseau blanc au long cou.",
    "signe": "Une marque, un geste qui veut dire quelque chose.",
    "poids": "Ce que pèse une chose.",
    "pois": "Un petit légume rond et vert.",
    "reine": "La femme d'un roi, ou celle qui règne.",
    "renne": "Un grand cerf des pays froids.",
    "rêne": "La courroie qui sert à guider un cheval.",
    "sel": "Ce qu'on met dans les plats pour les saler.",
    "selle": "Le siège posé sur le dos d'un cheval ou sur un vélo.",
    "tache": "Une marque de saleté.",
    "tâche": "Un travail à faire.",
}


def definition_hors_ligne(mot):
    return DEFINITIONS.get((mot or "").strip().lower())


def definition_ia(mot, nature=""):
    """Demande une définition d'enfant à l'IA. Renvoie None si indisponible."""
    try:
        import ia_client
        from config_manager import config
        if not config.get("ia_active"):
            return None
        brut = ia_client.appeler(
            "Tu écris un dictionnaire pour des élèves de 9 à 11 ans. "
            f"Donne la définition du mot « {mot} »"
            + (f" ({nature})" if nature else "") + ". "
            "Deux phrases maximum, un vocabulaire simple, et un exemple "
            "d'emploi court. N'emploie pas le mot lui-même dans sa définition. "
            "Réponds UNIQUEMENT par la définition, sans le mot en tête, "
            "sans guillemets.",
            temperature=0.3, max_tokens=140, tache="definitions")
        texte = (brut or "").strip().strip('"«»').split("\n")[0].strip()
        return texte if 10 < len(texte) < 400 else None
    except Exception:
        return None
