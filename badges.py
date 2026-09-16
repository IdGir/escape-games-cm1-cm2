"""badges.py — Les réussites de l'élève, par familles et par paliers.

Principe : un badge trop lointain ne motive personne, un badge déjà gagné non
plus. On organise donc les réussites en FAMILLES (écriture, lecture, dictée,
dictionnaire, mots, régularité), et chaque famille comporte plusieurs PALIERS
de difficulté croissante.

À un instant donné, l'élève voit :
  · tous les paliers qu'il a gagnés,
  · et seulement LE PALIER SUIVANT de chaque famille — celui qui est à sa
    portée. Quand il le décroche, le palier d'après apparaît.

C'est ce qui fait que « il s'en ajoute quand il monte d'un niveau » : la liste
grandit avec l'élève au lieu de l'écraser dès le premier jour.
"""

# --------------------------------------------------------------------------
#  Définition des familles
#
#  Chaque palier : (cle, emoji, titre, objectif affiché, cible)
#  La valeur atteinte est calculée plus bas, famille par famille.
# --------------------------------------------------------------------------
FAMILLES = {
    "ecriture": {
        "nom": "Je me corrige", "emoji": "📝", "couleur": "#2563EB",
        "unite": "texte(s) corrigé(s)",
        "paliers": [
            ("ecriture_1", "🌱", "Je me lance", "Corriger un premier texte", 1),
            ("ecriture_3", "📗", "Bien parti", "Corriger 3 textes", 3),
            ("ecriture_5", "📚", "Habitué", "Corriger 5 textes", 5),
            ("ecriture_10", "🏅", "Correcteur confirmé", "Corriger 10 textes", 10),
            ("ecriture_20", "🎖️", "Correcteur chevronné", "Corriger 20 textes", 20),
            ("ecriture_40", "👑", "Maître correcteur", "Corriger 40 textes", 40),
        ],
    },
    "parfait": {
        "nom": "Sans faute", "emoji": "✨", "couleur": "#15A34A",
        "unite": "texte(s) sans erreur",
        "paliers": [
            ("parfait_1", "✨", "Sans faute !", "Terminer un texte sans erreur", 1),
            ("parfait_3", "💎", "Trois sans faute", "Réussir 3 textes parfaits", 3),
            ("parfait_8", "🌟", "Orfèvre", "Réussir 8 textes parfaits", 8),
            ("parfait_15", "🏆", "Perfectionniste", "Réussir 15 textes parfaits", 15),
        ],
    },
    "autonomie": {
        "nom": "Tout seul", "emoji": "🎯", "couleur": "#7C3AED",
        "unite": "% corrigé sans aide",
        "paliers": [
            ("auto_40", "🎯", "Je cherche seul", "Corriger 4 erreurs sur 10 sans aide", 40),
            ("auto_60", "🎪", "Je me débrouille", "Corriger 6 erreurs sur 10 sans aide", 60),
            ("auto_75", "🦅", "Grande autonomie", "Corriger 3 erreurs sur 4 sans aide", 75),
            ("auto_90", "🛡️", "Presque sans aide", "Corriger 9 erreurs sur 10 sans aide", 90),
        ],
    },
    "lecture": {
        "nom": "Je lis à voix haute", "emoji": "📖", "couleur": "#0EA5E9",
        "unite": "lecture(s) chronométrée(s)",
        "paliers": [
            ("lecture_1", "📖", "Premier chrono", "Faire une lecture chronométrée", 1),
            ("lecture_5", "📘", "Lecteur régulier", "Faire 5 lectures", 5),
            ("lecture_12", "📙", "Grand lecteur", "Faire 12 lectures", 12),
            ("lecture_25", "📕", "Lecteur infatigable", "Faire 25 lectures", 25),
        ],
    },
    "vitesse": {
        "nom": "Ma vitesse de lecture", "emoji": "🚀", "couleur": "#D97706",
        "unite": "mots par minute",
        # Les cibles sont recalculées d'après le repère de la classe.
        "paliers": [
            ("vitesse_50", "🐢", "En route", "Lire {c} mots en une minute", 50),
            ("vitesse_75", "🚶", "Bon rythme", "Lire {c} mots en une minute", 75),
            ("vitesse_100", "🏆", "Objectif atteint", "Lire {c} mots en une minute", 100),
            ("vitesse_115", "🚀", "Au-delà de l'objectif", "Lire {c} mots en une minute", 115),
            ("vitesse_130", "⚡", "Lecteur rapide", "Lire {c} mots en une minute", 130),
        ],
    },
    "progres": {
        "nom": "Je progresse", "emoji": "📈", "couleur": "#15A34A",
        "unite": "mots gagnés depuis la 1re lecture",
        "paliers": [
            ("progres_5", "📈", "Je lis plus vite", "Gagner 5 mots par minute", 5),
            ("progres_15", "🎢", "Belle progression", "Gagner 15 mots par minute", 15),
            ("progres_30", "🌠", "Progrès spectaculaire", "Gagner 30 mots par minute", 30),
        ],
    },
    "dictee_mots": {
        "nom": "Dictée de mots", "emoji": "✍️", "couleur": "#E8890C",
        "unite": "dictée(s) de mots",
        "paliers": [
            ("dm_1", "✍️", "Première dictée de mots", "Faire une dictée de mots", 1),
            ("dm_5", "🖊️", "Dictée de mots : habitué", "Faire 5 dictées de mots", 5),
            ("dm_12", "🖋️", "Dictée de mots : expert", "Faire 12 dictées de mots", 12),
        ],
    },
    "dictee_expressions": {
        "nom": "Dictée d'expressions", "emoji": "🧩", "couleur": "#DB2777",
        "unite": "dictée(s) d'expressions",
        "paliers": [
            ("de_1", "🧩", "Première expression", "Faire une dictée d'expressions", 1),
            ("de_5", "🪢", "Accords maîtrisés", "Faire 5 dictées d'expressions", 5),
            ("de_12", "🎀", "Expert des groupes", "Faire 12 dictées d'expressions", 12),
        ],
    },
    "dictee_phrases": {
        "nom": "Dictée de phrases", "emoji": "📜", "couleur": "#0891B2",
        "unite": "dictée(s) de phrases",
        "paliers": [
            ("dp_1", "📜", "Première phrase dictée", "Faire une dictée de phrases", 1),
            ("dp_5", "📃", "Phrases : habitué", "Faire 5 dictées de phrases", 5),
            ("dp_12", "📰", "Phrases : expert", "Faire 12 dictées de phrases", 12),
        ],
    },
    "dictee_note": {
        "nom": "Réussite en dictée", "emoji": "🎖️", "couleur": "#DC2626",
        "unite": "% de mots justes (meilleur score)",
        "paliers": [
            ("dn_60", "🥉", "Dictée réussie", "Écrire 6 mots sur 10 justes", 60),
            ("dn_80", "🥈", "Belle dictée", "Écrire 8 mots sur 10 justes", 80),
            ("dn_100", "🥇", "Dictée sans faute", "Écrire tous les mots justes", 100),
        ],
    },
    "mots": {
        "nom": "Ma banque de mots", "emoji": "🎒", "couleur": "#B45309",
        "unite": "mot(s) appris",
        "paliers": [
            ("mots_5", "🎒", "Premiers mots appris", "Apprendre 5 mots difficiles", 5),
            ("mots_15", "🧳", "Collectionneur de mots", "Apprendre 15 mots", 15),
            ("mots_30", "🗄️", "Grande collection", "Apprendre 30 mots", 30),
            ("mots_60", "🏛️", "Trésor de mots", "Apprendre 60 mots", 60),
        ],
    },
    "dictionnaire": {
        "nom": "Mon dictionnaire", "emoji": "🔎", "couleur": "#4F46E5",
        "unite": "mot(s) cherché(s) et trouvé(s)",
        "paliers": [
            ("dico_3", "🔎", "Petit chercheur", "Trouver 3 mots au dictionnaire", 3),
            ("dico_10", "🔬", "Chercheur curieux", "Trouver 10 mots", 10),
            ("dico_25", "🗺️", "Explorateur de mots", "Trouver 25 mots", 25),
        ],
    },
    "regularite": {
        "nom": "Je m'entraîne souvent", "emoji": "🗓️", "couleur": "#059669",
        "unite": "jour(s) de travail",
        "paliers": [
            ("reg_3", "🗓️", "Trois jours", "Travailler 3 jours différents", 3),
            ("reg_8", "📆", "Huit jours", "Travailler 8 jours différents", 8),
            ("reg_20", "⭐", "Vingt jours", "Travailler 20 jours différents", 20),
        ],
    },
}

ORDRE = ["ecriture", "parfait", "autonomie", "lecture", "vitesse", "progres",
         "dictee_mots", "dictee_expressions", "dictee_phrases", "dictee_note",
         "mots", "dictionnaire", "regularite"]


def _jours_distincts(*listes):
    jours = set()
    for liste in listes:
        for s in liste:
            d = (s.get("date_seance") or "")[:10]
            if d:
                jours.add(d)
    return len(jours)


def calculer(corr, flu, dictees, repere, mots_appris, autonomie,
             nb_dico_trouves=0):
    """Renvoie la liste complète des badges, avec leur état.

    Chaque badge porte : famille, palier (rang dans la famille), obtenu,
    valeur atteinte, cible, et « visible » — un badge non obtenu n'est montré
    que s'il est le PROCHAIN de sa famille.
    """
    nb_parfaits = sum(1 for s in corr
                      if s.get("erreurs_avant") and not s.get("erreurs_apres"))
    mclm_meilleur = max((s["mclm"] for s in flu), default=0)
    gain = (flu[0]["mclm"] - flu[-1]["mclm"]) if len(flu) >= 2 else 0
    dictee_meilleur = max((d["score"] for d in dictees), default=0)
    par_genre = {}
    for d in dictees:
        g = d.get("genre") or "mots"
        par_genre[g] = par_genre.get(g, 0) + 1

    valeurs = {
        "ecriture": len(corr),
        "parfait": nb_parfaits,
        "autonomie": round(autonomie or 0),
        "lecture": len(flu),
        "vitesse": round(mclm_meilleur),
        "progres": round(max(0, gain)),
        "dictee_mots": par_genre.get("mots", 0),
        "dictee_expressions": par_genre.get("expressions", 0),
        "dictee_phrases": par_genre.get("phrases", 0),
        "dictee_note": round(dictee_meilleur),
        "mots": mots_appris,
        "dictionnaire": nb_dico_trouves,
        "regularite": _jours_distincts(corr, flu, dictees),
    }

    sortie = []
    for famille in ORDRE:
        f = FAMILLES[famille]
        # La famille « vitesse » se règle sur le repère de la classe : viser
        # 100 % du repère n'a pas le même sens en CM1 et en CM2.
        prochain_montre = False
        for rang, (cle, emoji, titre, objectif, cible) in enumerate(f["paliers"]):
            reelle = cible
            if famille == "vitesse":
                reelle = round(repere * cible / 100)
                objectif = objectif.format(c=reelle)
            valeur = valeurs[famille]
            obtenu = valeur >= reelle
            visible = obtenu
            if not obtenu and not prochain_montre:
                visible = True          # le prochain palier, celui à viser
                prochain_montre = True
            sortie.append({
                "cle": cle, "famille": famille,
                "famille_nom": f["nom"], "couleur": f["couleur"],
                "palier": rang + 1, "nb_paliers": len(f["paliers"]),
                "emoji": emoji, "titre": titre, "objectif": objectif,
                "obtenu": obtenu, "visible": visible,
                "valeur": valeur, "cible": reelle, "unite": f["unite"],
            })
    return sortie


def resume(badges):
    """Compte des badges obtenus, et le prochain à portée."""
    obtenus = [b for b in badges if b["obtenu"]]
    a_venir = [b for b in badges if b["visible"] and not b["obtenu"]]
    # Le plus proche du but en pourcentage : c'est celui qu'on met en avant.
    a_venir.sort(key=lambda b: -(b["valeur"] / b["cible"]) if b["cible"] else 0)
    return {
        "obtenus": len(obtenus),
        "total": len(badges),
        "prochain": a_venir[0] if a_venir else None,
    }
