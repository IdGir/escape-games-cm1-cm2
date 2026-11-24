"""Salle 1 « La galerie de la Terre » : grades mousse, lieutenant, second (fiche : Une planète active)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "terre-active", "tests", "donnees"))
from fiches import *
from schemas import terre

FICHE = "« Une planète active »"


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": tri(
            "Range chaque image : elle vient de l'intérieur de la Terre, ou du ciel et de l'eau ?",
            [("int", "De l'intérieur de la Terre"), ("ext", "Du ciel et de l'eau")],
            [("un volcan en éruption", "int"), ("le sol qui tremble", "int"), ("une tempête", "ext"), ("une inondation", "ext")],
            ["Ouvre la fiche " + FICHE + ".", "La lave vient d'en dessous.", "La pluie et le vent viennent du ciel."]),
        "lieutenant": tri(
            "Range chaque phénomène selon son origine, puis choisis la phrase de la fiche qui explique le cas du tsunami.",
            [("int", "Activité interne"), ("ext", "Activité externe")],
            [("un tsunami après un séisme sous la mer", "int"), ("une coulée de lave", "int"), ("un séisme", "int"),
             ("un cyclone", "ext"), ("une falaise rongée par les vagues", "ext"), ("une inondation après un orage", "ext")],
            ["Le tsunami a une cause cachée sous la mer.", "Le cyclone est un vent violent.", "Pour la justification : cherche « vagues géantes »."],
            J("Quelle phrase de la fiche explique le cas du tsunami ?", T_TSUNAMI, [T_EXTERNE, T_ACTIVE, T_INTERNE], pos=2)),
        "second": qcm(
            "Inès teste les guides de la station avec des cas difficiles. Choisis la bonne réponse, puis la phrase de la fiche qui définit l'activité interne.",
            [("Une vague géante frappe une côte, sans tempête, juste après une secousse sous la mer. Son origine est…", ["externe : c'est une vague", "interne : elle est provoquée par un séisme", "inconnue", "liée à la Lune"], 1, "La cause est sous la mer."),
             ("Une falaise recule de quelques mètres en un hiver de tempêtes. C'est…", ["une manifestation de l'activité interne", "une manifestation de l'activité externe", "un séisme", "une éruption"], 1, "Les vagues et le vent rongent la falaise."),
             ("Un nuage de cendres sort d'un volcan. Son origine est…", ["interne", "externe", "météorologique", "humaine"], 0, "Le magma vient de l'intérieur."),
             ("Pourquoi dit-on que la Terre est active ?", ["parce que sa surface change, parfois brusquement", "parce qu'elle tourne", "parce qu'il y a des océans", "parce qu'elle est ronde"], 0, "Volcans, séismes, érosion.")],
            ["Cherche toujours où se trouve la cause.", "L'air et l'eau : externe.", "Pour la justification : cherche « sous nos pieds »."],
            J("Quelle phrase de la fiche définit l'activité interne ?", T_INTERNE, [T_ACTIVE, T_EXTERNE, T_TSUNAMI], pos=1)),
    }
    d["e1-2"] = {
        "mousse": {"type": "plan", "titre": "La maquette d'Inès", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "la croûte"}, {"libelle": "Repère 2", "reponse": "le manteau"}, {"libelle": "Repère 3", "reponse": "le noyau"}],
                   "etiquettes": ["la croûte", "le manteau", "le noyau"],
                   "consigne": "Place chaque mot sur son repère." + terre(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La croûte est la fine bordure.", "Le noyau est au centre."]},
        "lieutenant": assoc(
            "Relie chaque enveloppe de la Terre à sa description, puis choisis la phrase de la fiche sur le manteau.",
            [("la croûte", "la plus fine : environ 30 km sous les continents"), ("le manteau", "des roches très chaudes, jusqu'à environ 2 900 km"),
             ("le noyau", "au centre de la Terre"), ("le centre", "à environ 6 400 km sous nos pieds"), ("l'activité interne", "sa cause est à l'intérieur de la Terre")],
            ["30 km : c'est très fin.", "2 900 km : la fin du manteau.", "Pour la justification : cherche « roches très chaudes »."],
            J("Quelle phrase de la fiche décrit le manteau ?", T_MANTEAU, [T_CROUTE, T_NOYAU, T_COUCHES], pos=0)),
        "second": ordre(
            "Range ces profondeurs de la plus petite à la plus grande, puis choisis la phrase de la fiche sur le manteau.",
            [("la base de la croûte sous les continents", "environ 30 km"), ("le milieu du manteau", "environ 1 500 km"),
             ("la limite entre le manteau et le noyau", "environ 2 900 km"), ("le centre de la Terre", "environ 6 400 km")],
            ["Compare les nombres.", "Le centre est le plus profond.", "Pour la justification : cherche « 2 900 »."],
            J("Quelle phrase de la fiche donne la profondeur de la limite du manteau ?", T_MANTEAU, [T_NOYAU, T_CROUTE, T_CHALEUR], pos=3)),
    }
    d["e1-3"] = {
        "mousse": vf(
            "Inès a écrit trois phrases. Pour chacune, choisis vrai ou faux.",
            [("Un volcan vient de l'intérieur de la Terre.", True, "Le magma monte d'en dessous."),
             ("Nous vivons sur le noyau de la Terre.", False, "Nous vivons sur la croûte."),
             ("La Terre a plusieurs couches, comme un fruit.", True, "La croûte, le manteau et le noyau.")],
            ["Ouvre la fiche " + FICHE + ".", "Le noyau est au centre.", "Pense à une pêche coupée."]),
        "lieutenant": qcm(
            "Inès prépare les questions des étudiants. Choisis la bonne réponse, puis la phrase de la fiche qui dit comment on étudie l'intérieur de la Terre.",
            [("Comment connaît-on l'intérieur de la Terre ?", ["on y est allé", "grâce aux ondes des séismes", "grâce aux nuages", "on ne le connaît pas du tout"], 1, "Personne n'est allé dans le manteau."),
             ("Plus on descend dans la Terre…", ["plus il fait froid", "plus il fait chaud", "plus il fait sombre et froid", "rien ne change"], 1, "C'est la chaleur interne."),
             ("Qu'est-ce que la chaleur interne fait bouger lentement ?", ["les nuages", "les roches du manteau", "la Lune", "les océans"], 1, "Ce mouvement entraîne les plaques.")],
            ["Les séismes envoient des ondes.", "Il fait de plus en plus chaud.", "Pour la justification : cherche « personne »."],
            J("Quelle phrase de la fiche explique comment on étudie l'intérieur de la Terre ?", T_PERSONNE, [T_CHALEUR, T_COUCHES, T_INTERNE], pos=1)),
        "second": vf(
            "Inès corrige le texte d'un nouveau panneau. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur la chaleur interne.",
            [("La chaleur interne fait bouger lentement les roches du manteau.", True, "C'est le moteur de l'activité interne."),
             ("La croûte est plus épaisse que le manteau.", False, "La croûte est l'enveloppe la plus fine."),
             ("Des mineurs sont déjà descendus jusqu'au manteau.", False, "Personne n'y est jamais allé."),
             ("Les ondes des séismes renseignent sur l'intérieur de la Terre.", True, "Elles traversent les enveloppes."),
             ("Le noyau est l'enveloppe la plus profonde.", True, "Il occupe le centre.")],
            ["Le manteau est très épais.", "Personne n'est allé dans le manteau.", "Pour la justification : cherche « plus on descend »."],
            J("Quelle phrase de la fiche parle de la chaleur interne ?", T_CHALEUR, [T_MANTEAU, T_PERSONNE, T_ACTIVE], pos=2)),
    }
    d["e1-4"] = {
        "lieutenant": {"type": "plan", "titre": "La maquette d'Inès", "colonnes": 2,
                       "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(["la croûte", "le manteau", "le noyau", "environ 2 900 km", "le centre, à environ 6 400 km"])],
                       "etiquettes": ["la croûte", "le manteau", "le noyau", "environ 2 900 km", "le centre, à environ 6 400 km", "environ 30 000 km", "l'atmosphère"],
                       "consigne": "Replace toutes les étiquettes de la maquette (deux sont en trop), puis choisis la phrase de la fiche sur le noyau." + terre(5),
                       "indices": ["Le centre est le point le plus profond.", "30 000 km : bien plus que le rayon de la Terre.", "Pour la justification : cherche « 6 400 »."],
                       "justification": J("Quelle phrase de la fiche situe le centre de la Terre ?", T_NOYAU, [T_MANTEAU, T_CROUTE, T_COUCHES], pos=0)},
        "second": assoc(
            "Inès explique d'où vient chaque phénomène. Relie chaque phénomène à sa cause, puis choisis la phrase de la fiche sur l'activité externe.",
            [("une éruption", "le magma qui monte de l'intérieur"), ("un séisme", "des roches qui cassent sous terre"),
             ("une falaise qui recule", "les vagues qui rongent la roche"), ("une inondation", "des pluies très abondantes"),
             ("un tsunami", "un séisme sous la mer")],
            ["Deux causes sont dans l'air et l'eau.", "Le tsunami a une cause interne.", "Pour la justification : cherche « falaises »."],
            J("Quelle phrase de la fiche décrit l'activité externe ?", T_EXTERNE, [T_INTERNE, T_TSUNAMI, T_ACTIVE], pos=3)),
    }
    return d
