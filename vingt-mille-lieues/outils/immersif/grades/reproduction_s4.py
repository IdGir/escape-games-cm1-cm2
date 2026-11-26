"""Salle 4 « La ferme des Coteaux » : grades mousse, lieutenant, second (fiche : La fécondation chez les animaux)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "reproduction", "tests", "donnees"))
from fiches import *

FICHE = "« La fécondation chez les animaux »"


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": qcm(
            "Yasmine répond aux plus jeunes visiteurs. Choisis la bonne réponse.",
            [("Pour avoir des poussins, il faut…", ["un coq et une poule", "deux coqs", "une poule et un canard", "une seule poule"], 0, "Un mâle et une femelle."),
             ("Le petit de la vache s'appelle…", ["l'agneau", "le veau", "le poussin", "le chevreau"], 1, "L'agneau est le petit de la brebis."),
             ("Le mâle de la poule s'appelle…", ["le coq", "le taureau", "le bélier", "le jars"], 0, "Le jars est le mâle de l'oie.")],
            ["Ouvre la fiche " + FICHE + ".", "Il faut un mâle et une femelle.", "Pense au chant du matin."]),
        "lieutenant": assoc(
            "Yasmine fabrique un lexique pour son panneau. Relie chaque mot à sa définition, puis choisis la phrase de la fiche qui définit la fécondation.",
            [("un gamète", "une cellule reproductrice"), ("la fécondation", "la rencontre d'un gamète mâle et d'un gamète femelle"),
             ("la fécondation interne", "dans le corps de la femelle"), ("la fécondation externe", "dans l'eau, hors du corps"), ("l'embryon", "le tout début du petit")],
            ["Gamète : cellule reproductrice.", "Externe : dehors.", "Pour la justification : cherche « première cellule »."],
            J("Quelle phrase de la fiche définit la fécondation ?", A_FECONDATION, [A_CELLULES, A_SEXES, A_INTERNE], pos=2)),
        "second": vf(
            "Yasmine vérifie les fiches de son stagiaire. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les gamètes.",
            [("Le mâle et la femelle produisent chacun des cellules reproductrices.", True, "Les gamètes mâles et femelles."),
             ("Les gamètes sont des petits déjà formés.", False, "Ce sont des cellules."),
             ("Après la fécondation, il y a une seule première cellule.", True, "Elle donnera l'embryon."),
             ("Un bouc et une brebis peuvent avoir un agneau.", False, "Ils ne sont pas de la même espèce."),
             ("La fécondation est le début de la vie d'un nouvel animal.", True, "C'est la première étape du développement.")],
            ["Une cellule, ce n'est pas un petit.", "Bouc et brebis : deux espèces.", "Pour la justification : cherche « gamètes »."],
            J("Quelle phrase de la fiche définit les gamètes ?", A_CELLULES, [A_FECONDATION, A_SEXES, A_EAU], pos=0)),
    }
    d["e4-2"] = {
        "mousse": tri(
            "Range chaque animal : ses œufs sont fécondés dans le corps de la mère, ou dans l'eau ?",
            [("int", "Dans le corps de la mère"), ("ext", "Dans l'eau")],
            [("la poule", "int"), ("la vache", "int"), ("la grenouille", "ext"), ("la truite", "ext")],
            ["Ouvre la fiche " + FICHE + ".", "La grenouille pond dans la mare.", "La vache vit dans le pré."]),
        "lieutenant": tri(
            "Range chaque animal du registre selon son type de fécondation, puis choisis la phrase de la fiche sur la fécondation interne.",
            [("int", "Fécondation interne"), ("ext", "Fécondation externe")],
            [("la poule", "int"), ("la tortue", "int"), ("le lapin", "int"), ("la chèvre", "int"),
             ("la grenouille", "ext"), ("le crapaud", "ext"), ("la truite", "ext"), ("le saumon", "ext")],
            ["Oiseaux, reptiles, mammifères : interne.", "Amphibiens et beaucoup de poissons : externe.", "Pour la justification : cherche « oiseaux »."],
            J("Quelle phrase de la fiche décrit la fécondation interne ?", A_INTERNE, [A_EXTERNE, A_FECONDATION, A_NOMBRE], pos=3)),
        "second": qcm(
            "Yasmine propose des énigmes aux futurs éleveurs. Choisis la bonne réponse, puis la phrase de la fiche sur la fécondation externe.",
            [("Une femelle pond des milliers d'ovules dans un torrent ; le mâle passe au-dessus et les féconde. C'est…", ["une fécondation interne", "une fécondation externe", "une germination", "une pollinisation"], 1, "C'est le cas de la truite."),
             ("Une cane pond des œufs dans un nid. Sa fécondation est…", ["externe, car elle pond", "interne, comme chez tous les oiseaux", "impossible à savoir", "faite par le vent"], 1, "Pondre ne veut pas dire fécondation externe."),
             ("Pourquoi la grenouille va-t-elle pondre dans la mare ?", ["parce que la fécondation externe se fait dans l'eau", "pour se laver", "parce qu'elle a froid", "pour chercher du nectar"], 0, "Les cellules reproductrices sècheraient à l'air."),
             ("Chez quel animal la fécondation est-elle externe ?", ["le lapin", "la brebis", "le crapaud", "la poule"], 2, "Il pond dans les mares.")],
            ["Les ovules sont dehors avant d'être fécondés.", "Tous les oiseaux : interne.", "Pour la justification : cherche « truite »."],
            J("Quelle phrase de la fiche décrit la fécondation externe ?", A_EXTERNE, [A_INTERNE, A_EAU, A_NOMBRE], pos=1)),
    }
    d["e4-3"] = {
        "mousse": vf(
            "Yasmine a écrit trois phrases. Pour chacune, choisis vrai ou faux.",
            [("Il faut un mâle et une femelle de la même espèce pour avoir des petits.", True, "Coq et poule, taureau et vache."),
             ("Les œufs de la grenouille sont fécondés dans l'eau.", True, "Dans la mare."),
             ("Un coq et une vache peuvent avoir des petits.", False, "Ils ne sont pas de la même espèce.")],
            ["Ouvre la fiche " + FICHE + ".", "La grenouille pond dans la mare.", "Même espèce."]),
        "lieutenant": qcm(
            "Yasmine interroge les visiteurs sur l'étang. Choisis la bonne réponse, puis la phrase de la fiche qui explique pourquoi la fécondation externe se fait dans l'eau.",
            [("Pourquoi la fécondation externe se fait-elle dans l'eau ?", ["parce que les cellules reproductrices ne survivraient pas à l'air", "parce que l'eau est chaude", "parce que les poissons ont soif", "par hasard"], 0, "Elles sècheraient."),
             ("Chez la grenouille, qui féconde les ovules ?", ["le mâle, dans l'eau", "les abeilles", "le vent", "la femelle seule"], 0, "Juste après la ponte."),
             ("Chez la chèvre, la fécondation est…", ["externe", "interne", "dans l'eau", "par le pollen"], 1, "C'est un mammifère.")],
            ["Une cellule sèche à l'air libre.", "Le mâle est là au moment de la ponte.", "Pour la justification : cherche « air libre »."],
            J("Quelle phrase de la fiche explique pourquoi la fécondation externe se fait dans l'eau ?", A_EAU, [A_EXTERNE, A_INTERNE, A_SEXES], pos=2)),
        "second": tri(
            "Yasmine reçoit des descriptions d'animaux inconnus. Range chaque indice : il fait penser à une fécondation interne, ou externe ? Puis choisis la phrase de la fiche sur le nombre d'œufs.",
            [("int", "Plutôt fécondation interne"), ("ext", "Plutôt fécondation externe")],
            [("la femelle pond des milliers d'ovules dans l'eau", "ext"), ("le mâle féconde les ovules juste après la ponte", "ext"), ("beaucoup d'œufs ne seront jamais fécondés", "ext"),
             ("le petit se développe dans le ventre de sa mère", "int"), ("c'est un oiseau qui pond quelques œufs dans un nid", "int"), ("c'est un mammifère", "int")],
            ["Des milliers d'œufs dans l'eau : dehors.", "Oiseaux et mammifères : dedans.", "Pour la justification : cherche « très grand nombre »."],
            J("Quelle phrase de la fiche parle du nombre d'œufs ?", A_NOMBRE, [A_EXTERNE, A_EAU, A_FECONDATION], pos=3)),
    }
    d["e4-4"] = {
        "lieutenant": vf(
            "Yasmine relit les panneaux de l'étang. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur le nombre d'œufs.",
            [("La grenouille pond un très grand nombre d'œufs.", True, "Beaucoup ne deviendront pas des grenouilles."),
             ("Tous les œufs pondus dans l'eau sont fécondés.", False, "Beaucoup ne le sont pas."),
             ("Beaucoup d'œufs de grenouille sont mangés par d'autres animaux.", True, "Les poissons, les insectes d'eau."),
             ("Chez la poule, la fécondation a lieu dans l'eau.", False, "Elle est interne."),
             ("La truite a une fécondation externe.", True, "Comme beaucoup de poissons.")],
            ["Beaucoup d'œufs, car beaucoup sont perdus.", "La poule est un oiseau.", "Pour la justification : cherche « mangés »."],
            J("Quelle phrase de la fiche parle du nombre d'œufs ?", A_NOMBRE, [A_EAU, A_EXTERNE, A_INTERNE], pos=0)),
        "second": assoc(
            "Yasmine prépare les couples de la ferme pour le printemps. Relie chaque femelle au mâle de la même espèce, puis choisis la phrase de la fiche sur le mâle et la femelle.",
            [("la brebis", "le bélier"), ("la chèvre", "le bouc"), ("la vache", "le taureau"), ("la poule", "le coq"), ("l'oie", "le jars")],
            ["Bouc et brebis ne vont pas ensemble.", "Le jars a un long cou.", "Pour la justification : cherche « même espèce »."],
            J("Quelle phrase de la fiche dit ce qu'il faut pour avoir des petits ?", A_SEXES, [A_FECONDATION, A_CELLULES, A_INTERNE], pos=2)),
    }
    return d
