"""Salle 2 « Le pont de la caravelle » : grades mousse, lieutenant, second (fiche : Les progrès techniques)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grandes-explorations", "tests", "donnees"))
from fiches import *

FICHE = "« Les progrès techniques »"


def donnees(svg, bloc=None):
    d = {}
    plan3, plan5 = svg("e2-2", "matelot"), svg("e2-2", "timonier")
    d["e2-1"] = {
        "mousse": assoc(
            "Relie chaque instrument de Rosa à ce qu'il fait.",
            [("la boussole", "montre le nord"), ("l'astrolabe", "regarde la hauteur du Soleil"), ("la carte marine", "montre les côtes")],
            ["Ouvre la fiche " + FICHE + ".", "L'aiguille de la boussole est aimantée.", "Une carte se lit sur la table."]),
        "lieutenant": assoc(
            "Rosa a sorti tous ses instruments. Relie chaque instrument à son rôle, puis choisis la phrase de la fiche qui dit à quoi sert la boussole.",
            [("la boussole", "garder le cap même sans voir les étoiles"), ("l'astrolabe", "mesurer la hauteur du Soleil"), ("le quadrant", "mesurer la hauteur de l'étoile Polaire"),
             ("le portulan", "dessiner les côtes et les ports"), ("le sablier", "mesurer le temps passé")],
            ["Deux instruments mesurent la hauteur d'un astre.", "Le portulan est une carte.", "Pour la justification : cherche « aiguille aimantée »."],
            J("Quelle phrase de la fiche dit à quoi sert la boussole ?", T_BOUSSOLE, [T_ASTRO, T_CARTE, T_SABLIER], pos=1)),
        "second": tri(
            "Rosa classe ses instruments selon la question à laquelle ils répondent. Range chaque instrument, puis choisis la phrase de la fiche qui explique comment on estime la distance parcourue.",
            [("cap", "Dans quelle direction aller ?"), ("ou", "Où sommes-nous entre le nord et le sud ?"), ("combien", "Depuis combien de temps naviguons-nous ?")],
            [("la boussole", "cap"), ("le portulan", "cap"), ("l'astrolabe", "ou"), ("le quadrant", "ou"), ("les tables de calcul", "ou"), ("le sablier", "combien")],
            ["La latitude, c'est entre le nord et le sud.", "Le portulan donne les directions à suivre.", "Pour la justification : cherche « distance parcourue »."],
            J("Quelle phrase de la fiche explique comment on estime la distance ?", T_SABLIER, [T_LATI, T_BOUSSOLE, T_LARGE], pos=2)),
    }
    d["e2-2"] = {
        "mousse": {"type": "plan", "titre": "Le plan de la caravelle", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "voile triangulaire"}, {"libelle": "Repère 2", "reponse": "mât"}, {"libelle": "Repère 3", "reponse": "gouvernail"}],
                   "etiquettes": ["voile triangulaire", "mât", "gouvernail"],
                   "consigne": "Place chaque nom sur son repère du plan de la caravelle." + plan3,
                   "indices": ["Ouvre la fiche " + FICHE + " : regarde le schéma.", "La voile du repère 1 a trois côtés.", "Le gouvernail est à l'arrière, dans l'eau."]},
        "lieutenant": {"type": "plan", "titre": "Le plan de la caravelle", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "voile latine"}, {"libelle": "Repère 2", "reponse": "voile carrée"}, {"libelle": "Repère 3", "reponse": "gouvernail d'étambot"},
                                 {"libelle": "Repère 4", "reponse": "château arrière"}, {"libelle": "Repère 5", "reponse": "coque"}],
                       "etiquettes": ["voile latine", "voile carrée", "gouvernail d'étambot", "château arrière", "coque", "rame", "ancre", "hélice"],
                       "consigne": "Place chaque étiquette sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui explique l'intérêt du repère 1." + plan5,
                       "indices": ["Compte les côtés de chaque voile.", "Une caravelle n'a ni rames ni hélice.", "Pour la justification : cherche « triangulaires »."],
                       "justification": J("Quelle phrase de la fiche explique l'intérêt du repère 1 ?", T_LATINE, [T_CARREE, T_GOUV, T_CARA], pos=0)},
        "second": qcm(
            "Observe le plan de la caravelle. Réponds aux questions, puis choisis la phrase de la fiche qui décrit le repère 3." + plan5,
            [("Quel repère pousse le navire vite quand le vent vient de l'arrière ?", ["le repère 1", "le repère 2", "le repère 4", "le repère 5"], 1, "La voile carrée."),
             ("Quel repère permet d'avancer même quand le vent n'est pas dans le dos ?", ["le repère 1", "le repère 3", "le repère 4", "le repère 5"], 0, "La voile latine."),
             ("Où se trouve le gouvernail d'étambot ?", ["à l'avant", "au sommet du mât", "à l'arrière, dans l'axe du navire", "sur le côté"], 2, "Fixé dans l'axe, à l'arrière."),
             ("Qui a mis au point la caravelle ?", ["les Vikings", "les Portugais", "les Romains", "les Anglais"], 1, "Au XVe siècle.")],
            ["Une voile carrée a quatre côtés.", "La voile latine est triangulaire.", "Pour la justification : cherche « dans l'axe »."],
            J("Quelle phrase de la fiche décrit le repère 3 ?", T_GOUV, [T_LATINE, T_CARREE, T_CARA], pos=3)),
    }
    d["e2-3"] = {
        "mousse": qcm(
            "Rosa pose trois questions à son équipage. Réponds.",
            [("Une caravelle est...", ["un navire à voiles", "un bateau à moteur", "un avion"], 0, "Un navire léger à voiles."),
             ("La boussole montre...", ["l'heure", "le nord", "la profondeur"], 1, "Grâce à son aiguille aimantée."),
             ("Où la boussole a-t-elle été inventée ?", ["en France", "en Amérique", "en Chine"], 2, "Elle vient de Chine.")],
            ["Ouvre la fiche " + FICHE + ".", "L'aiguille de la boussole est aimantée.", "La boussole vient d'Asie."]),
        "lieutenant": vf(
            "Rosa corrige le carnet d'un apprenti. Vrai ou faux ? Puis choisis la phrase de la fiche qui définit la latitude.",
            [("La caravelle est un navire léger d'une vingtaine de mètres.", True, "Mis au point par les Portugais."),
             ("Avec l'astrolabe, on mesure la hauteur du Soleil.", True, "Au-dessus de l'horizon."),
             ("La latitude est la position entre l'est et l'ouest.", False, "C'est la position entre le nord et le sud."),
             ("Une caravelle embarque environ deux cents marins.", False, "Une vingtaine."),
             ("L'astrolabe a été transmis aux Européens par les savants du monde arabe.", True, "Comme beaucoup de savoirs.")],
            ["Une vingtaine de mètres, une vingtaine de marins.", "Nord-sud, c'est la latitude.", "Pour la justification : cherche « c'est-à-dire »."],
            J("Quelle phrase de la fiche définit la latitude ?", T_LATI, [T_ASTRO, T_BOUSSOLE, T_ARABE], pos=2)),
        "second": vf(
            "Rosa relit des cartels d'exposition écrits trop vite. Vrai ou faux ? Puis choisis la phrase de la fiche qui dit d'où viennent ces savoirs.",
            [("La boussole a été inventée en Europe au XVe siècle.", False, "Elle a été inventée en Chine."),
             ("L'astrolabe est arrivé en Europe grâce aux savants du monde arabe.", True, "Comme beaucoup de savoirs."),
             ("Le quadrant mesure la hauteur de l'étoile Polaire.", True, "Comme l'astrolabe, il mesure la hauteur d'un astre."),
             ("Avec la boussole seule, le pilote connaît sa latitude.", False, "La boussole donne le cap ; la latitude se calcule avec l'astrolabe et des tables."),
             ("Les voiles carrées avancent bien quand le vent vient de l'arrière.", True, "Elles poussent vite le navire.")],
            ["La boussole vient d'Asie.", "Cap et latitude, ce n'est pas la même chose.", "Pour la justification : cherche « monde arabe »."],
            J("Quelle phrase de la fiche dit d'où viennent ces savoirs ?", T_ARABE, [T_LARGE, T_BOUSSOLE, T_CARA], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": ordre(
            "Rosa explique comment le pilote fait le point à midi. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui dit à quoi sert la mesure.",
            ["Attendre midi, quand le Soleil est au plus haut.", "Viser le Soleil avec l'astrolabe.", "Lire l'angle sur le cercle gradué.",
             "Chercher la latitude dans les tables de calcul.", "Reporter la latitude sur la carte marine."],
            ["On observe avant de calculer.", "La carte vient en dernier.", "Pour la justification : cherche « tables de calcul »."],
            J("Quelle phrase de la fiche dit à quoi sert la mesure ?", T_LATI, [T_ASTRO, T_CARTE, T_SABLIER], pos=1)),
        "second": ordre(
            "Rosa prépare une traversée de plusieurs semaines. Remets les étapes dans l'ordre, du port au retour à terre, puis choisis la phrase de la fiche qui décrit le chargement.",
            ["Charger l'eau douce, le biscuit et les tonneaux de vivres.", "Quitter le port en longeant les côtes dessinées sur le portulan.",
             "S'éloigner des côtes et garder le cap avec la boussole.", "Apercevoir une côte inconnue à l'horizon.",
             "Mesurer la hauteur du Soleil pour connaître la latitude de cette côte.", "Dessiner la nouvelle côte sur la carte."],
            ["On charge avant de partir.", "On ne dessine une côte qu'après l'avoir vue et située.", "Pour la justification : cherche « biscuit »."],
            J("Quelle phrase de la fiche décrit le chargement ?", T_EQUIP, [T_CARA, T_LARGE, T_CARTE], pos=2)),
    }
    return d
