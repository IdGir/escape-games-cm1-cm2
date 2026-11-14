"""Salle 4 « La couveuse de la ferme » : grades mousse, lieutenant, second (fiche : Le développement avant la naissance)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "naissances-animaux", "tests", "donnees"))
from fiches import *
from gen_enigmes import DOC4_CM1, DOC4_CM2

FICHE = "« Le développement avant la naissance »"


def donnees(svg, bloc=None):
    d = {}
    o3, o5 = svg("e4-2", "matelot"), svg("e4-2", "timonier")
    d["e4-1"] = {
        "mousse": ordre(
            "Jeanne regarde dans l'œuf avec sa lampe. Remets les trois étapes dans l'ordre.",
            ["On ne voit que le jaune.", "On reconnaît la forme du poussin.", "Le poussin sort de l'œuf."],
            ["Ouvre la fiche " + FICHE + ".", "Au début, il n'y a presque rien à voir.", "La sortie de l'œuf est la fin."]),
        "lieutenant": ordre(
            "Remets les six moments de la couvaison dans l'ordre, puis choisis la phrase de la fiche qui décrit les étapes dans l'œuf.",
            ["La poule commence à couver ses œufs fécondés.", "L'œuf dépasse environ 27 °C : l'embryon commence à se développer.", "Le cœur bat ; des vaisseaux entourent le jaune.",
             "On reconnaît la forme du poussin.", "Les plumes sont bien visibles.", "Le poussin perce la coquille avec son diamant."],
            ["La chaleur vient avant tout le reste.", "Le cœur bat vers le 3e jour.", "Pour la justification : cherche « 7e jour »."],
            J("Quelle phrase de la fiche décrit les étapes dans l'œuf ?", D_ETAPES, [D_COUVE, D_ECLOS, D_CHAUD], pos=2)),
        "second": ordre(
            "Jeanne affiche les durées avant la naissance. Range ces animaux de la durée la plus courte à la plus longue, puis choisis la phrase de la fiche qui donne ces durées." + DOC4_CM2,
            [("la poule", "couvaison"), ("la lapine", "gestation"), ("la chatte", "gestation"), ("la vache", "gestation"), ("la jument", "gestation"), ("l'éléphante", "gestation")],
            ["21 jours, c'est 3 semaines.", "20 mois, c'est plus de 600 jours.", "Pour la justification : cherche « 336 jours »."],
            J("Quelle phrase de la fiche donne ces durées ?", D_DUREES, [D_GESTATION, D_TAILLE, D_COUVE], pos=1)),
    }
    d["e4-2"] = {
        "mousse": {"type": "plan", "titre": "L'œuf de Jeanne", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "coquille"}, {"libelle": "Repère 2", "reponse": "jaune"}, {"libelle": "Repère 3", "reponse": "blanc"}],
                   "etiquettes": ["coquille", "jaune", "blanc"],
                   "consigne": "Place chaque nom sur son repère." + o3,
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La coquille fait le tour de l'œuf.", "Le jaune est la boule jaune."]},
        "lieutenant": {"type": "plan", "titre": "L'œuf de Jeanne", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "coquille"}, {"libelle": "Repère 2", "reponse": "jaune"}, {"libelle": "Repère 3", "reponse": "blanc"},
                                 {"libelle": "Repère 4", "reponse": "chambre à air"}, {"libelle": "Repère 5", "reponse": "embryon"}],
                       "etiquettes": ["coquille", "jaune", "blanc", "chambre à air", "embryon", "placenta", "cordon ombilical", "utérus"],
                       "consigne": "Place chaque étiquette sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui donne le rôle de chaque partie." + o5,
                       "indices": ["Placenta, cordon et utérus : chez les mammifères.", "La chambre à air est au gros bout.", "Pour la justification : cherche « chambre à air »."],
                       "justification": J("Quelle phrase de la fiche donne le rôle de chaque partie ?", D_OEUF, [D_EMBRYON, D_COUVE, D_ECLOS], pos=3)},
        "second": assoc(
            "Relie chaque partie de l'œuf à son rôle, puis choisis la phrase de la fiche qui les décrit.",
            [("la coquille", "protège l'embryon"), ("le jaune", "nourrit l'embryon"), ("le blanc", "lui fournit de l'eau"),
             ("la chambre à air", "contient de l'air"), ("le diamant", "perce la coquille à l'éclosion")],
            ["Le jaune est une réserve de nourriture.", "Le diamant est au bout du bec.", "Pour la justification : cherche « fournit de l'eau »."],
            J("Quelle phrase de la fiche décrit les parties de l'œuf ?", D_OEUF, [D_ECLOS, D_ETAPES, D_APRES], pos=0)),
    }
    d["e4-3"] = {
        "mousse": code(
            "L'armoire des berceaux s'ouvre avec deux nombres, lus dans le tableau de Jeanne." + DOC4_CM1,
            [("Jours de couvaison de la poule", "21", 2, True), ("Jours de gestation de la lapine", "31", 2, True)],
            ["Ouvre la fiche " + FICHE + ".", "Cherche la ligne de la poule.", "Puis la ligne de la lapine."]),
        "lieutenant": code(
            "Pour ouvrir l'armoire des berceaux, calcule quatre nombres à partir du tableau, puis choisis la phrase de la fiche qui définit la gestation." + DOC4_CM2,
            [("Jours de gestation de la jument", "336", 3, True), ("Jours de plus pour la vache que pour la lapine", "249", 3, True),
             ("Semaines de couvaison de la poule", "3", 1, True), ("Mois de gestation au moins pour l'éléphante", "20", 2, True)],
            ["280 − 31.", "21 jours = 3 fois 7 jours.", "Pour la justification : cherche « s'appelle la gestation »."],
            J("Quelle phrase de la fiche définit la gestation ?", D_GESTATION, [D_DUREES, D_TAILLE, D_EMBRYON], pos=2)),
        "second": code(
            "Pour ouvrir l'armoire des berceaux, calcule quatre nombres à partir du tableau, puis choisis la phrase de la fiche qui relie la taille et la durée." + DOC4_CM2,
            [("Couvaisons complètes de poule pendant une gestation de vache", "13", 2, True), ("Semaines complètes de gestation de la lapine", "4", 1, True),
             ("Jours de plus pour la jument que pour la vache", "56", 2, True), ("Mois de différence entre l'éléphante (au plus) et la vache", "13", 2, True)],
            ["280 ÷ 21 : garde le nombre entier.", "31 ÷ 7 : garde le nombre entier.", "Pour la justification : cherche « plus un mammifère est grand »."],
            J("Quelle phrase de la fiche relie la taille et la durée ?", D_TAILLE, [D_DUREES, D_GESTATION, D_COUVE], pos=1)),
    }
    d["e4-4"] = {
        "lieutenant": vf(
            "La jument du zoo attend un poulain. Vrai ou faux ? Puis choisis la phrase de la fiche qui décrit l'éclosion du poussin, pour comparer.",
            [("Le poulain grandit dans l'utérus de la jument.", True, "C'est la gestation."),
             ("La gestation de la jument dure environ 336 jours.", True, "Environ 11 mois."),
             ("Le poulain sort d'un œuf à coquille.", False, "La jument est vivipare."),
             ("Le poussin perce la coquille avec le diamant de son bec.", True, "Le 21e jour."),
             ("Le poussin ne peut pas manger seul avant plusieurs semaines.", False, "Dès le lendemain de l'éclosion, il mange seul.")],
            ["La jument est un mammifère.", "Le diamant est une pointe du bec.", "Pour la justification : cherche « diamant »."],
            J("Quelle phrase de la fiche décrit l'éclosion ?", D_ECLOS, [D_ETAPES, D_APRES, D_OEUF], pos=0)),
        "second": vf(
            "Jeanne prépare la venue du poulain. Vrai ou faux ? Puis choisis la phrase de la fiche qui dit ce que forme l'embryon avant la naissance.",
            [("Avant la naissance, l'embryon forme peu à peu tous ses organes.", True, "Dans l'œuf comme dans le ventre."),
             ("Un œuf de poule fécondé laissé au frais donne quand même un poussin.", False, "Il faut la chaleur de la couvaison."),
             ("La gestation de l'éléphante dure plus d'un an et demi.", True, "20 à 22 mois."),
             ("La lapine porte ses petits plus longtemps que la chatte.", False, "31 jours contre 63 à 65 jours."),
             ("Le poussin prêt à éclore remplit presque tout l'œuf.", True, "Il ne reste que la chambre à air.")],
            ["Sans chaleur, l'embryon ne se développe pas.", "Un an et demi = 18 mois.", "Pour la justification : cherche « organes »."],
            J("Quelle phrase de la fiche dit ce que forme l'embryon ?", D_EMBRYON, [D_GESTATION, D_CHAUD, D_ETAPES], pos=3)),
    }
    return d
