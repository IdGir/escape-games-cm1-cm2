"""Salle 2 « La salle des cartes » : grades mousse, lieutenant, second (fiche : Les plaques)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "terre-active", "tests", "donnees"))
from fiches import *
from schemas import plaques

FICHE = "« Les plaques »"


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": {"type": "plan", "titre": "La maquette de Noé", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "une plaque"}, {"libelle": "Repère 2", "reponse": "le manteau"}, {"libelle": "Repère 3", "reponse": "un volcan"}],
                   "etiquettes": ["une plaque", "le manteau", "un volcan"],
                   "consigne": "Place chaque mot sur son repère." + plaques(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Le volcan a de la fumée.", "Le manteau est en bas."]},
        "lieutenant": {"type": "plan", "titre": "La maquette de Noé", "colonnes": 2,
                       "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(["une plaque", "le manteau", "un volcan", "le foyer d'un séisme", "la plaque qui s'enfonce"])],
                       "etiquettes": ["une plaque", "le manteau", "un volcan", "le foyer d'un séisme", "la plaque qui s'enfonce", "le noyau", "une plaque qui s'écarte"],
                       "consigne": "Replace les étiquettes de la maquette (deux sont en trop), puis choisis la phrase de la fiche qui explique ce que montre cette maquette." + plaques(5),
                       "indices": ["Ici, les plaques se rapprochent.", "Une plaque plonge sous l'autre.", "Pour la justification : cherche « s'enfoncer »."],
                       "justification": J("Quelle phrase de la fiche explique ce que montre la maquette ?", P_RAPPROCHENT, [P_ECARTENT, P_MONTAGNES, P_DECOUPE], pos=1)},
        "second": qcm(
            "Noé fait calculer ses visiteurs. Choisis la bonne réponse, puis la phrase de la fiche sur la vitesse des plaques.",
            [("Imagine une plaque qui avance de 5 cm par an. De combien avance-t-elle en 100 ans ?", ["5 cm", "50 cm", "5 m", "500 m"], 2, "100 × 5 cm = 500 cm = 5 m."),
             ("Et en 1 million d'années, à la même vitesse ?", ["5 km", "50 km", "500 m", "5 m"], 1, "1 000 000 × 5 cm = 5 000 000 cm = 50 km."),
             ("Pourquoi ne sent-on pas les plaques bouger ?", ["elles ne bougent pas", "leur mouvement est trop lent", "elles bougent la nuit", "on dort"], 1, "Quelques centimètres par an."),
             ("Que montre ce calcul ?", ["un mouvement lent peut produire de grands effets sur des millions d'années", "les plaques vont s'arrêter", "les continents ne bougent pas", "les plaques reculent"], 0, "C'est ainsi que se forment les montagnes.")],
            ["1 m = 100 cm.", "1 km = 100 000 cm.", "Pour la justification : cherche « centimètres »."],
            J("Quelle phrase de la fiche donne la vitesse des plaques ?", P_LENT, [P_DECOUPE, P_MONTAGNES, P_FRONTIERE], pos=2)),
    }
    d["e2-2"] = {
        "mousse": vf(
            "Noé a écrit trois phrases. Pour chacune, choisis vrai ou faux.",
            [("La surface de la Terre est faite de grandes plaques.", True, "Comme un puzzle."),
             ("On sent les plaques bouger tous les jours.", False, "Elles bougent bien trop lentement."),
             ("Il y a souvent des volcans là où deux plaques se touchent.", True, "Aux frontières des plaques.")],
            ["Ouvre la fiche " + FICHE + ".", "Les plaques sont très lentes.", "Pense aux frontières."]),
        "lieutenant": vf(
            "Noé relit les fiches d'un stagiaire. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur la vitesse des plaques.",
            [("Les plaques bougent de quelques centimètres par an.", True, "C'est très lent."),
             ("À certaines frontières, les plaques s'écartent.", True, "Du magma monte entre elles."),
             ("Une montagne se forme en quelques jours.", False, "Il faut des millions d'années."),
             ("Les séismes sont rares près des frontières de plaques.", False, "Ils y sont fréquents."),
             ("Une maquette aide à comprendre un phénomène trop lent pour être vu.", True, "C'est un modèle.")],
            ["Les montagnes sont très lentes à se former.", "Les frontières sont agitées.", "Pour la justification : cherche « par an »."],
            J("Quelle phrase de la fiche donne la vitesse des plaques ?", P_LENT, [P_DECOUPE, P_MAQUETTE, P_FRONTIERE], pos=0)),
        "second": tri(
            "Noé discute de sa maquette : que peut-elle montrer, et que ne montre-t-elle pas bien ? Range chaque phrase, puis choisis la phrase de la fiche qui dit ce qu'est une maquette.",
            [("oui", "La maquette le montre"), ("non", "La maquette ne le montre pas bien")],
            [("deux plaques qui se rapprochent", "oui"), ("une plaque qui passe sous l'autre", "oui"), ("le plissement qui forme un relief", "oui"),
             ("la vraie vitesse : quelques centimètres par an", "non"), ("la vraie taille des plaques", "non"), ("la chaleur du manteau", "non")],
            ["Une maquette va plus vite que la réalité.", "Elle est bien plus petite.", "Pour la justification : cherche « modèle »."],
            J("Quelle phrase de la fiche dit ce qu'est une maquette ?", P_MAQUETTE, [P_RAPPROCHENT, P_MONTAGNES, P_LENT], pos=3)),
    }
    d["e2-3"] = {
        "mousse": assoc(
            "Relie chaque morceau de la maquette à ce qu'il représente.",
            [("le polystyrène", "une plaque"), ("la pâte molle", "le manteau"), ("la main qui pousse", "le mouvement des plaques")],
            ["Ouvre la fiche " + FICHE + ".", "Le polystyrène est dur.", "La pâte est en dessous."]),
        "lieutenant": assoc(
            "Relie chaque type de frontière à ce qui s'y passe, puis choisis la phrase de la fiche sur les plaques qui s'écartent.",
            [("des plaques qui s'écartent", "du magma monte et forme une nouvelle croûte"), ("des plaques qui se rapprochent", "une plaque s'enfonce : séismes et volcans"),
             ("deux plaques qui se poussent longtemps", "des montagnes se forment"), ("le milieu d'une plaque", "des séismes plus rares"),
             ("une maquette", "un modèle pour comprendre")],
            ["S'écarter : il y a de la place pour le magma.", "Se rapprocher : l'une passe dessous.", "Pour la justification : cherche « nouvelle croûte »."],
            J("Quelle phrase de la fiche décrit les plaques qui s'écartent ?", P_ECARTENT, [P_RAPPROCHENT, P_MONTAGNES, P_LENT], pos=2)),
        "second": ordre(
            "Noé fait la démonstration de la montagne avec sa maquette. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche sur la formation des montagnes.",
            [("On pose deux plaques sur la pâte molle.", "le début"), ("On pousse lentement une plaque vers l'autre.", "le mouvement"),
             ("Les deux plaques se touchent et se poussent.", "la frontière"), ("La pâte se plisse et se soulève.", "le plissement"), ("Un relief apparaît : une montagne.", "le résultat")],
            ["On commence par installer la maquette.", "Le plissement vient après la poussée.", "Pour la justification : cherche « se plissent »."],
            J("Quelle phrase de la fiche explique la formation des montagnes ?", P_MONTAGNES, [P_RAPPROCHENT, P_ECARTENT, P_MAQUETTE], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": tri(
            "Replace les punaises : près d'une frontière de plaques, ou loin ? Puis choisis la phrase de la fiche qui explique où se trouvent les volcans.",
            [("pres", "Près d'une frontière"), ("loin", "Loin d'une frontière")],
            [("la Guadeloupe", "pres"), ("la Martinique", "pres"), ("l'Islande", "pres"), ("le Japon", "pres"), ("la Bourgogne", "loin"), ("le Bassin parisien", "loin")],
            ["Les Antilles sont entre plusieurs plaques.", "L'Islande est coupée par une frontière.", "Pour la justification : cherche « la plupart »."],
            J("Quelle phrase de la fiche explique où se trouvent la plupart des volcans ?", P_FRONTIERE, [P_DECOUPE, P_LENT, P_MAQUETTE], pos=1)),
        "second": vf(
            "Noé prépare la carte « Les Antilles, une terre active ». Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les Antilles.",
            [("Les Antilles sont à la frontière de plusieurs plaques.", True, "D'où les volcans et les séismes."),
             ("La Guadeloupe n'a jamais de séismes.", False, "Elle est en zone de sismicité forte."),
             ("La Martinique a un volcan surveillé, la montagne Pelée.", True, "Il est surveillé par un observatoire."),
             ("La Bourgogne est sur une frontière de plaques.", False, "Elle en est loin."),
             ("Une frontière de plaques est une zone où la Terre est très active.", True, "Séismes et volcans y sont fréquents.")],
            ["Les Antilles : plusieurs plaques.", "La métropole est loin des frontières.", "Pour la justification : cherche « Guadeloupe »."],
            J("Quelle phrase de la fiche explique les volcans et les séismes des Antilles ?", P_ANTILLES, [P_FRONTIERE, P_RAPPROCHENT, P_DECOUPE], pos=3)),
    }
    return d
