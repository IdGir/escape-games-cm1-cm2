"""Aide guidée sur une erreur précise, en DEUX niveaux.

L'idée pédagogique : ne jamais donner la réponse toute faite. On accompagne
l'élève pour qu'il la trouve lui-même.

  · Niveau 1 — une QUESTION qui met sur la voie (« Singulier ou pluriel ? »,
    « Qui est-ce qui fait l'action ? »). Toujours affichée avec la mini-leçon.
  · Niveau 2 — un INDICE plus direct, révélé seulement si l'élève clique sur
    « Aide ». Exemple type : un mot de la même famille pour retrouver une
    lettre finale muette. C'est plus proche de la réponse, donc son usage est
    compté pour évaluer l'autonomie de l'élève.

Si une IA est configurée (aide_ia_active), on lui demande une question et un
indice adaptés au mot et à sa phrase. Sinon — et c'est le cas par défaut —
tout est fabriqué hors ligne par des règles fiables, catégorie par catégorie.
"""
import json
import unicodedata

import ia_client
from config_manager import config


def _sans_accent(m):
    return "".join(c for c in unicodedata.normalize("NFD", (m or "").lower())
                   if unicodedata.category(c) != "Mn")


# ---------------------------------------------------------------- Homophones
TESTS_HOMOPHONES = {
    "a": "Remplace par « avait » : si la phrase reste juste, c'est « a » (le verbe). Sinon, c'est « à ».",
    "à": "Remplace par « avait » : si ça ne marche pas, c'est « à » (pas le verbe).",
    "est": "Remplace par « était » : si ça marche, c'est « est » (le verbe).",
    "et": "Remplace par « était » : si ça NE marche PAS, c'est « et » (on peut dire « et puis »).",
    "sont": "Remplace par « étaient » : si ça marche, c'est « sont » (le verbe).",
    "son": "Remplace par « étaient » : si ça NE marche PAS, c'est « son » (le sien).",
    "ont": "Remplace par « avaient » : si ça marche, c'est « ont » (le verbe).",
    "on": "Remplace par « il » : si ça marche, c'est « on ».",
    "où": "« où » avec un accent indique le lieu (l'endroit où…).",
    "ou": "Remplace par « ou bien » : si ça marche, c'est « ou » sans accent.",
    "ces": "« ces » = je peux dire « ces …-là » (je montre plusieurs choses).",
    "ses": "« ses » = à lui ou à elle (ses affaires = les siennes).",
    "ce": "« ce » se met devant un nom (ce chien). « se » se met devant un verbe (il se lave).",
    "se": "« se » se met devant un verbe (il se lave).",
    "la": "« la » se met devant un nom (la maison). « là » avec accent indique le lieu.",
    "là": "« là » avec un accent indique le lieu (reste là).",
    "leur": "« leur » devant un verbe ne prend jamais de « s » (je leur parle).",
    "leurs": "« leurs » devant un nom au pluriel prend un « s » (leurs cahiers).",
}


# --------------------------------------------------------------------------
#  Ce qui se DÉDUIT / ce qui se SAIT
# --------------------------------------------------------------------------
# Certaines orthographes ne se raisonnent pas : le « t » de « souvent » ne se
# retrouve par aucune règle ni aucun mot de la même famille. Poser une question
# du type « connais-tu un mot de la même famille ? » est alors inutile et
# décourageant. On distingue donc trois cas, et on le DIT à l'élève.
#
#   · "famille"     → la lettre muette se retrouve par un mot de la famille
#   · "regle"       → une règle permet de trancher (accord, conjugaison…)
#   · "a_savoir"    → rien à déduire : ça s'apprend et ça se vérifie

# Mots invariables et adverbes courants : à savoir par cœur (leçon ORTH-12).
MOTS_A_SAVOIR = {
    "souvent", "toujours", "jamais", "beaucoup", "longtemps", "maintenant",
    "pourtant", "cependant", "vraiment", "tellement", "seulement", "également",
    "autrefois", "parfois", "quelquefois", "aussitôt", "bientôt", "plutôt",
    "tôt", "tard", "trop", "très", "assez", "moins", "plus", "puis", "depuis",
    "alors", "ainsi", "enfin", "hier", "aujourd'hui", "demain", "dedans",
    "dehors", "dessus", "dessous", "devant", "derrière", "auprès", "après",
    "avant", "pendant", "durant", "malgré", "parmi", "sans", "sous", "vers",
    "chez", "dans", "près", "loin", "ailleurs", "partout", "surtout", "d'abord",
    "peut-être", "quand", "comment", "pourquoi", "combien", "tandis",
    "néanmoins", "volontiers", "gentiment", "doucement", "lentement",
}

# Lettre finale muette qui SE RETROUVE par un mot de la même famille.
# (La leçon ORTH-07 du classeur enseigne exactement ce geste.)
FAMILLES = {
    "grand": "grandeur", "petit": "petite", "chaud": "chaleur", "froid": "froide",
    "bruit": "bruitage", "chant": "chanter", "lait": "laitier", "dent": "dentiste",
    "vent": "venteux", "sang": "sanglant", "long": "longueur", "gros": "grosse",
    "haut": "hauteur", "bas": "basse", "plat": "platine", "tard": "tarder",
    "bond": "bondir", "champ": "champêtre", "drap": "draperie", "fruit": "fruitier",
    "gout": "gouter", "goût": "goûter", "lourd": "lourdeur", "mort": "mortel",
    "nid": "nidifier", "part": "partir", "point": "pointu", "port": "portuaire",
    "pot": "poterie", "rang": "ranger", "refus": "refuser", "regard": "regarder",
    "renard": "renarde", "repos": "reposer", "retard": "retarder", "saut": "sauter",
    "sourd": "sourde", "tapis": "tapisser", "tricot": "tricoter", "vert": "verdure",
    "blanc": "blanche", "franc": "franche", "flanc": "flanquer", "banc": "bancal",
    "accord": "accorder", "bord": "border", "corps": "corporel", "cout": "couter",
    "début": "débuter", "défaut": "défectueux", "délit": "délinquant",
    "dépôt": "déposer", "égout": "égoutier", "fort": "forte", "gris": "grise",
    "mépris": "mépriser", "outil": "outillage", "permis": "permettre",
    "pied": "piéton", "plomb": "plomberie", "poids": "peser", "profit": "profiter",
    "rebond": "rebondir", "récit": "réciter", "respect": "respecter",
    "sursaut": "sursauter", "toit": "toiture", "univers": "universel",
}


def nature_mot(correct: str, mot: str = "") -> str:
    """« famille », « a_savoir » ou « " » (rien de particulier)."""
    c = (correct or "").lower().strip(".,;:!?»«\"'")
    if not c:
        return ""
    f = (mot or "").lower().strip(".,;:!?»«\"'")
    # Seuls les accents changent : c'est une règle, et elle a sa leçon.
    if f and _sans_accent(f) == _sans_accent(c) and f != c:
        return "accent"
    if c in FAMILLES:
        return "famille"
    if c in MOTS_A_SAVOIR:
        return "a_savoir"
    # Lettre finale muette non répertoriée : on ne promet pas une famille
    # qu'on est incapable de fournir.
    if len(c) > 3 and c[-1] in "tdsxzgp" and c[-2] not in "aeiouy":
        return "a_savoir"
    return ""


def _diff_lettres(mot, correct):
    """Décrit brièvement ce qui change entre le mot fautif et la forme correcte."""
    f, j = (mot or ""), (correct or "")
    if not j:
        return ""
    # Différence d'accent uniquement
    if _sans_accent(f) == _sans_accent(j) and f.lower() != j.lower():
        return "C'est une histoire d'accent : regarde les é, è, ê, à…"
    # Lettre finale muette en plus dans le corrigé
    if len(j) == len(f) + 1 and j[:-1].lower() == f.lower() and j[-1].lower() not in "aeiouy":
        return ("Il manque une lettre à la fin, qu'on n'entend pas. Cherche un mot "
                "de la même famille pour l'entendre (ex. « grand » → « grandeur »).")
    # Pluriel
    if j.lower().rstrip("sx") == f.lower() and j.lower() != f.lower():
        return "Il faut la marque du pluriel à la fin : ajoute la lettre qui manque."
    return ""


# ---------------------------------------------------------------- Règles hors ligne
#
# On ne renvoie QUE ce qui est utile au cas précis examiné par l'élève :
#   · question : la question à se poser pour ce mot ;
#   · pistes   : une ou deux indications ciblées (niveau intermédiaire) ;
#   · indice   : l'aide directe (niveau 2), révélée seulement à la demande.
# --------------------------------------------------------------------------
#  Questions ancrées dans LA phrase de l'élève
#
#  Une question générique (« ce mot est-il au pluriel ? ») ne dit pas à l'élève
#  OÙ regarder. On repère donc les mots voisins dans sa propre phrase et on les
#  cite : la question devient un geste précis, pas une récitation de règle.
# --------------------------------------------------------------------------
DETERMINANTS_PLURIEL = {"les", "des", "mes", "tes", "ses", "nos", "vos", "leurs",
                        "ces", "certains", "plusieurs", "quelques", "deux",
                        "trois", "quatre", "cinq", "six", "sept", "huit", "neuf",
                        "dix", "beaucoup", "tous", "toutes"}
DETERMINANTS_SINGULIER = {"le", "la", "l'", "un", "une", "mon", "ma", "ton", "ta",
                          "son", "sa", "notre", "votre", "leur", "ce", "cet",
                          "cette", "chaque"}
PRONOMS = {"je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"}


def _mots(phrase):
    import re
    return re.findall(r"[A-Za-zÀ-ÿ'’-]+", phrase or "")


def _voisins(contexte, mot):
    """(mot d'avant, mot d'après) dans la phrase de l'élève."""
    liste = _mots(contexte)
    cible = (mot or "").strip().lower()
    for i, m in enumerate(liste):
        if m.lower() == cible:
            return (liste[i - 1] if i > 0 else "",
                    liste[i + 1] if i + 1 < len(liste) else "")
    return "", ""


def _determinant_du_groupe(contexte, mot):
    """Le déterminant qui commande le groupe où se trouve « mot ».

    On remonte de quelques mots : dans « des pommes rouge », c'est « des » qui
    décide, pas « pommes ».
    """
    liste = _mots(contexte)
    cible = (mot or "").strip().lower()
    for i, m in enumerate(liste):
        if m.lower() == cible:
            for k in range(i - 1, max(-1, i - 4), -1):
                bas = liste[k].lower()
                if bas in DETERMINANTS_PLURIEL or bas in DETERMINANTS_SINGULIER:
                    return liste[k]
            return liste[i - 1] if i > 0 else ""
    return ""


def _sujet_probable(contexte, verbe):
    """Le groupe qui précède le verbe : le candidat sujet le plus évident."""
    liste = _mots(contexte)
    cible = (verbe or "").strip().lower()
    for i, m in enumerate(liste):
        if m.lower() == cible and i > 0:
            debut = max(0, i - 3)
            avant = liste[debut:i]
            # On remonte jusqu'au déterminant ou au pronom qui ouvre le groupe.
            for k in range(len(avant) - 1, -1, -1):
                bas = avant[k].lower()
                if bas in DETERMINANTS_PLURIEL or bas in DETERMINANTS_SINGULIER \
                        or bas in PRONOMS:
                    return " ".join(avant[k:])
            return avant[-1]
    return ""


def _hors_ligne(cat, mot, correct, message, contexte=""):
    mot = (mot or "").strip()
    correct = (correct or "").strip()
    m = mot or "ce mot"

    if cat == "accord":
        # Le mot fautif est souvent un adjectif : le déterminant qui commande
        # tout le groupe peut être deux ou trois mots plus tôt.
        avant = _determinant_du_groupe(contexte, mot)
        bas = avant.lower()
        if bas in DETERMINANTS_PLURIEL:
            q = (f"Dans ce groupe, il y a « {avant} » : c'est du pluriel. "
                 f"Alors, comment doit s'écrire « {m} » ?")
            pistes = [f"« {avant} » annonce plusieurs : tout le groupe suit.",
                      "Le nom et son adjectif prennent la même marque."]
        elif bas in DETERMINANTS_SINGULIER:
            q = (f"Dans ce groupe, il y a « {avant} » : on parle d'un seul. "
                 f"« {m} » doit-il vraiment porter la marque du pluriel ?")
            pistes = [f"« {avant} » annonce une seule chose.",
                      "Un seul → pas de -s au nom ni à l'adjectif."]
        else:
            q = (f"« {m} » : cherche le mot chef de ce groupe, puis demande-toi "
                 f"s'il y en a un seul ou plusieurs.")
            pistes = ["Repère le petit mot du début (le, les, des, ma, mes…).",
                      "Le nom ET l'adjectif prennent la même marque que lui."]
        i = _diff_lettres(mot, correct) or \
            "Un seul ou plusieurs ? Écris la marque du pluriel (souvent -s) sur tout le groupe."
        return q, pistes, i

    if cat == "conjugaison":
        sujet = _sujet_probable(contexte, mot)
        if sujet:
            mots_sujet = _mots(sujet)
            est_pronom = len(mots_sujet) == 1 and mots_sujet[0].lower() in PRONOMS
            pluriel = any(x.lower() in DETERMINANTS_PLURIEL
                          or x.lower() in ("ils", "elles", "nous", "vous")
                          for x in mots_sujet)
            if est_pronom:
                # Le sujet est déjà un pronom : lui demander de le remplacer
                # par un pronom n'aurait aucun sens.
                q = (f"Le sujet de « {m} », c'est « {sujet} ». Quelle terminaison "
                     f"le verbe prend-il avec « {sujet.lower()} » ?")
                pistes = ["je → -e ou -s · tu → -s · il/elle → -e ou -t",
                          "nous → -ons · vous → -ez · ils/elles → -ent"]
            elif pluriel:
                q = (f"Qui est-ce qui « {m} » ? C'est « {sujet} » : ils sont "
                     f"plusieurs. Quelle terminaison faut-il ?")
                pistes = [f"« {sujet} », c'est comme « ils » ou « elles ».",
                          "Avec ils/elles, la terminaison -ent ne s'entend pas "
                          "mais s'écrit."]
            else:
                q = (f"Qui est-ce qui « {m} » ? C'est « {sujet} ». Par quel "
                     f"pronom peux-tu le remplacer ?")
                pistes = [f"Remplace « {sujet} » par il, elle, ils ou elles.",
                          "C'est le pronom qui décide de la terminaison."]
        else:
            q = f"Qui est-ce qui « {m} » ? Trouve le sujet, il commande la terminaison."
            pistes = ["Pose la question « qui est-ce qui… ? » juste avant le verbe.",
                      "Remplace le sujet par il, elle, ils ou elles."]
        i = _diff_lettres(mot, correct) or \
            "Regarde la terminaison : elle doit correspondre au pronom qui remplace le sujet."
        return q, pistes, i

    if cat == "homophone":
        # On nomme les deux formes en présence : la question devient un choix
        # net, pas une invitation vague à « réfléchir ».
        test = TESTS_HOMOPHONES.get(mot.lower()) or TESTS_HOMOPHONES.get(correct.lower())
        if correct and correct.lower() != mot.lower():
            q = f"Ici, faut-il écrire « {mot} » ou « {correct} » ? Comment le vérifier ?"
        else:
            q = f"« {m} » : quel autre mot s'écrit autrement mais se prononce pareil ?"
        pistes = [test] if test else [
            "Essaie un remplacement : si la phrase reste juste, c'est le bon."]
        i = test or "Fais le test de remplacement à voix basse : c'est lui qui décide, pas l'oreille."
        return q, pistes, i

    if cat == "orthographe":
        nature = nature_mot(correct, mot)
        c = (correct or "").lower().strip(".,;:!?»«\"'")

        if nature == "famille":
            # Ici, la lettre muette SE RETROUVE : la question a du sens.
            parent = FAMILLES.get(c, "")
            q = (f"Ce mot cache une lettre à la fin qu'on n'entend pas. "
                 f"Connais-tu un mot de la même famille que « {m} » ?")
            pistes = ["Un mot de la même famille fait entendre la lettre muette.",
                      "Essaie le féminin, ou un verbe formé sur ce mot."]
            i = (f"Pense à « {parent} » : tu entends la lettre qui manque à la fin."
                 if parent else
                 "Cherche un mot de la même famille : tu entendras la lettre muette.")
            return q, pistes, i

        if nature == "a_savoir":
            # Ici, AUCUNE règle ne permet de deviner. On le dit franchement :
            # c'est un mot qui s'apprend, pas un mot qui se raisonne.
            q = (f"« {m} » : celui-là ne se devine pas. Es-tu sûr(e) de savoir "
                 f"comment il s'écrit, ou faut-il aller le vérifier ?")
            pistes = ["Ce mot ne suit aucune règle : on le sait, ou on le cherche.",
                      "Regarde dans ton classeur, ton cahier ou le dictionnaire.",
                      "Une fois vérifié, note-le : il reviendra souvent."]
            i = ("Il manque une lettre qu'on n'entend pas à la fin. Tu ne peux pas "
                 "la déduire : va la vérifier, puis retiens ce mot.")
            return q, pistes, i

        # Cas restants : accent, syllabe, consonne double… là, on peut raisonner.
        d = _diff_lettres(mot, correct)
        if "accent" in d:
            q = f"« {m} » : les accents sont-ils bien placés ?"
            pistes = ["Prononce lentement : é (fermé) ou è (ouvert) ?",
                      "Un accent change parfois complètement le mot (a / à, ou / où)."]
            return q, pistes, d
        q = f"« {m} » : découpe-le en syllabes. Laquelle te fait hésiter ?"
        pistes = ["Prononce chaque syllabe séparément.",
                  "Un son peut s'écrire de plusieurs façons (o / au / eau, f / ph).",
                  "Attention aux consonnes doubles."]
        i = d or ("Compare avec un mot que tu sais écrire et qui contient le même "
                  "son : c'est souvent la même graphie.")
        return q, pistes, i

    if cat == "segmentation":
        n = len([p for p in correct.split() if p]) or 2
        q = (f"Lis « {m} » lentement, à voix basse : combien de mots "
             f"entends-tu ?")
        pistes = ["Marque une petite pause entre chaque morceau.",
                  "Chaque morceau existe-t-il tout seul ?"]
        i = f"Il faut le séparer en {n} mots. Pense aussi à l'apostrophe (l', d', qu')."
        return q, pistes, i

    if cat == "ponctuation":
        q = "À cet endroit, quel signe de ponctuation manque ou est mal placé ?"
        pistes = ["Lis à voix haute : une pause = souvent une virgule.",
                  "Une phrase se termine par . ! ou ?"]
        i = "Pas d'espace AVANT la virgule ni le point ; une espace APRÈS."
        return q, pistes, i

    if cat == "majuscule":
        # Début de phrase ou nom propre : ce ne sont pas les mêmes raisons,
        # donc pas la même question.
        debut = bool(contexte) and _mots(contexte)[:1] == [mot]
        if debut:
            q = (f"« {m} » ouvre la phrase. Par quoi commence toujours une "
                 f"phrase ?")
            pistes = ["Après un point, on repart avec une majuscule."]
        else:
            q = (f"« {m} » : est-ce le nom d'une personne, d'une ville ou d'un "
                 f"pays ?")
            pistes = ["Prénoms, villes, pays, fleuves : toujours une majuscule.",
                      "Un nom commun (chien, école) n'en prend pas."]
        i = "Réécris la première lettre en grand (majuscule)."
        return q, pistes, i

    # lexique
    if "manque" in (message or "").lower():
        q = "À cet endroit, un mot a-t-il été oublié ?"
        pistes = ["Relis la phrase à voix haute, lentement."]
        i = "Il manque un petit mot ici (souvent « et », « le », « à »…)."
        return q, pistes, i
    q = f"« {m} » est-il bien le mot le plus précis ? Est-il répété ?"
    pistes = ["Évite les mots « valises » : truc, chose, faire, bien.",
              "Cherche un synonyme plus précis."]
    i = "Remplace-le par un mot plus précis, qui dit exactement ce que tu veux."
    return q, pistes, i


# ---------------------------------------------------------------- IA
_CONSIGNE_NATURE = {
    "a_savoir": (
        "IMPORTANT : ce mot NE PEUT PAS être deviné. Aucune règle, aucun mot de "
        "la même famille ne permet de retrouver son orthographe (comme le « t » "
        "de « souvent »). Ne demande donc SURTOUT PAS de chercher un mot de la "
        "même famille ni d'appliquer une règle : ce serait une impasse. "
        "Ta question doit amener l'élève à se demander honnêtement s'il SAIT "
        "écrire ce mot ou s'il doit aller le VÉRIFIER (classeur, cahier, "
        "dictionnaire). Dis-lui clairement que ce mot s'apprend et se retient.\n"),
    "famille": (
        "IMPORTANT : ce mot a une lettre finale muette qui SE RETROUVE grâce à un "
        "mot de la même famille. Oriente l'élève vers cette recherche précise.\n"),
}


def _prompt_ia(cat, mot, correct, contexte, nature=""):
    return (
        "Tu es un enseignant de français bienveillant à l'école primaire (CM1-CM2). "
        "Un élève a fait une erreur et tu veux l'AIDER À TROUVER SEUL, sans jamais "
        "lui donner la réponse écrite. Ne donne QUE ce qui est utile à CE cas précis "
        "(pas de règle générale récitée, pas d'exemples hors-sujet). "
        "Ne pose JAMAIS une question dont la réponse ne peut pas mener l'élève à "
        "corriger : une question inutile décourage.\n"
        f"Catégorie de l'erreur : {cat}.\n"
        f"Mot ou passage concerné : « {mot} ».\n"
        f"Phrase de l'élève : « {contexte} ».\n"
        + _CONSIGNE_NATURE.get(nature, "") + "\n"
        "Donne, du plus doux au plus direct :\n"
        "1. \"question\" : UNE question courte et simple, portant sur CE mot, qui met "
        "l'élève sur la voie (ex. « Ce nom est-il au singulier ou au pluriel ? »).\n"
        "2. \"pistes\" : une ou deux indications courtes et ciblées sur ce cas "
        "(le geste à faire ici). Liste de chaînes.\n"
        "3. \"indice\" : un indice plus direct mais SANS écrire le mot corrigé — par "
        "exemple un mot de la même famille pour une lettre muette, ou un test de "
        "remplacement. L'élève doit encore faire le dernier pas lui-même.\n\n"
        "Langage adapté à un enfant de 9-11 ans, phrases courtes, tutoiement. "
        "Réponds UNIQUEMENT par un objet JSON, sans texte autour, au format : "
        '{"question": "...", "pistes": ["...", "..."], "indice": "..."}'
    )


def _lecon_liee(cat, nature):
    """La fiche du classeur à proposer pour ce cas précis (ou None).

    Pour un mot qui ne se déduit pas, on renvoie vers la leçon des mots
    invariables plutôt que vers une règle qui ne s'applique pas.
    """
    try:
        import lecons_manuel as lm
        if not lm.disponible():
            return None
        lecon_id = None
        if nature == "a_savoir":
            lecon_id = "ORTH-12"          # Les mots invariables
        elif nature == "famille":
            lecon_id = "ORTH-07"          # Les lettres finales muettes
        elif nature == "accent":
            lecon_id = "ORTH-11"          # Les accents
        fiche = lm.LECONS_MANUEL.get(lecon_id) if lecon_id else None
        if not fiche:
            fiche = lm.fiche_principale(cat)
        if not fiche:
            return None
        return {"lecon_id": fiche["lecon_id"],
                "titre": fiche.get("titre", ""),
                "sous_domaine": fiche.get("sous_domaine", "")}
    except Exception:
        return None


def aide(cat, mot="", correct="", contexte="", message=""):
    """Renvoie {"question", "pistes", "indice", "nature", "lecon", "source"}.

    Uniquement des questions utiles au cas examiné. « nature » indique si
    l'orthographe se déduit (famille / règle) ou si elle doit être sue
    (a_savoir) : l'élève ne cherche pas en vain.
    """
    cat = cat or "orthographe"
    nature = nature_mot(correct, mot) if cat == "orthographe" else ""
    lecon = _lecon_liee(cat, nature)

    if config.get("ia_active") and config.get("aide_ia_active", True):
        try:
            brut = ia_client.appeler(_prompt_ia(cat, mot, correct, contexte, nature),
                                     temperature=0.4, max_tokens=320,
                                     tache="aide")
            d = ia_client.extraire_json(brut)
            q = (d.get("question") or "").strip()
            i = (d.get("indice") or "").strip()
            pistes = [str(p).strip() for p in (d.get("pistes") or []) if str(p).strip()]
            if q and i:
                return {"question": q, "pistes": pistes, "indice": i,
                        "nature": nature, "lecon": lecon, "source": "ia"}
        except Exception:
            pass  # repli hors ligne : jamais bloquant
    q, pistes, i = _hors_ligne(cat, mot, correct, message, contexte)
    return {"question": q, "pistes": pistes, "indice": i,
            "nature": nature, "lecon": lecon, "source": "regles"}
