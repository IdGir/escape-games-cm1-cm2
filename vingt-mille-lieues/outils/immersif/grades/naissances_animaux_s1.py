"""Salle 1 « Le laboratoire de la vétérinaire » : grades mousse, lieutenant, second (fiche : La fécondation)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "naissances-animaux", "tests", "donnees"))
from fiches import *

FICHE = "« La fécondation »"


def donnees(svg, bloc=None):
    d = {}
    s3, s5 = svg("e1-1", "matelot"), svg("e1-1", "timonier")
    d["e1-1"] = {
        "mousse": {"type": "plan", "titre": "Le schéma d'Inès", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "cellule du mâle"}, {"libelle": "Repère 2", "reponse": "cellule de la femelle"}, {"libelle": "Repère 3", "reponse": "œuf"}],
                   "etiquettes": ["cellule du mâle", "cellule de la femelle", "œuf"],
                   "consigne": "Place chaque nom sur son repère." + s3,
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La cellule du mâle est la petite qui a une queue.", "L'œuf est à droite de la flèche."]},
        "lieutenant": {"type": "plan", "titre": "Le schéma d'Inès", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "spermatozoïde"}, {"libelle": "Repère 2", "reponse": "ovule"}, {"libelle": "Repère 3", "reponse": "cellule-œuf"},
                                 {"libelle": "Repère 4", "reponse": "embryon"}, {"libelle": "Repère 5", "reponse": "flagelle"}],
                       "etiquettes": ["spermatozoïde", "ovule", "cellule-œuf", "embryon", "flagelle", "placenta", "ovaire", "coquille"],
                       "consigne": "Place chaque étiquette sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui compare les deux gamètes." + s5,
                       "indices": ["L'ovaire produit l'ovule, il n'est pas sur le dessin.", "L'embryon a plusieurs cellules.", "Pour la justification : cherche « immobile »."],
                       "justification": J("Quelle phrase de la fiche compare les deux gamètes ?", F_TAILLE, [F_GAMETES, F_FECOND, F_MICRO], pos=2)},
        "second": tri(
            "Inès a noté huit descriptions. Range chacune : elle décrit le spermatozoïde, l'ovule, ou ni l'un ni l'autre. Puis choisis la phrase de la fiche qui dit où sont produits les gamètes.",
            [("sp", "Spermatozoïde"), ("ov", "Ovule"), ("ni", "Ni l'un ni l'autre")],
            [("cellule minuscule et mobile", "sp"), ("produit par les testicules", "sp"), ("avance grâce à un flagelle", "sp"),
             ("grosse cellule immobile", "ov"), ("contient des réserves", "ov"), ("produit par les ovaires", "ov"),
             ("résultat de la fécondation", "ni"), ("formé de milliers de cellules", "ni")],
            ["La cellule-œuf et l'embryon ne sont pas des gamètes.", "Les testicules sont chez le mâle.", "Pour la justification : cherche « testicules »."],
            J("Quelle phrase de la fiche dit où sont produits les gamètes ?", F_ORGANES, [F_GAMETES, F_TAILLE, F_ESPECE], pos=1)),
    }
    d["e1-2"] = {
        "mousse": vf(
            "Inès a écrit trois phrases. Pour chacune, choisis vrai ou faux.",
            [("Un petit commence avec deux cellules : une du mâle et une de la femelle.", True, "C'est la fécondation."),
             ("Ces cellules se voient à l'œil nu.", False, "Il faut un microscope."),
             ("La fécondation donne un œuf.", True, "C'est la première cellule du petit.")],
            ["Ouvre la fiche " + FICHE + ".", "Inès utilise un microscope.", "Deux cellules donnent un œuf."]),
        "lieutenant": vf(
            "Inès relit les notes d'un stagiaire. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui parle des œufs du magasin.",
            [("Un œuf de poule du magasin n'a pas été fécondé.", True, "Il ne donnera pas de poussin."),
             ("Le spermatozoïde est la grosse cellule qui contient des réserves.", False, "C'est l'ovule."),
             ("Un chat et une lapine peuvent avoir un petit ensemble.", False, "Il faut la même espèce."),
             ("La cellule-œuf se divise en deux, puis en quatre.", True, "Elle devient un embryon."),
             ("Les gamètes se voient seulement au microscope.", True, "Ils sont minuscules.")],
            ["Ce qui contient des réserves est gros.", "Mâle et femelle de la même espèce.", "Pour la justification : cherche « magasin »."],
            J("Quelle phrase de la fiche parle des œufs du magasin ?", F_SANS, [F_OEUF, F_EMBRYON, F_SEXUEE], pos=3)),
        "second": vf(
            "Inès prépare un quiz pour les soigneurs. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui dit combien de spermatozoïdes s'unissent à l'ovule.",
            [("Des milliers de spermatozoïdes peuvent s'approcher d'un ovule.", True, "Mais un seul s'unit à lui."),
             ("Deux spermatozoïdes s'unissent à l'ovule pour former la cellule-œuf.", False, "Un seul."),
             ("Le petit ressemble à ses deux parents.", True, "La cellule-œuf réunit une part de chacun."),
             ("L'ovule se déplace grâce à son flagelle.", False, "L'ovule est immobile."),
             ("Sans fécondation, l'œuf ne peut pas devenir un embryon.", True, "Il n'y a pas de cellule-œuf.")],
            ["Un seul gagne la course.", "C'est le spermatozoïde qui a un flagelle.", "Pour la justification : cherche « un seul »."],
            J("Quelle phrase de la fiche dit combien de spermatozoïdes s'unissent à l'ovule ?", F_UN, [F_FECOND, F_TAILLE, F_PARENTS], pos=0)),
    }
    d["e1-3"] = {
        "mousse": assoc(
            "Relie chaque mot à ce qu'il veut dire.",
            [("la fécondation", "la rencontre de deux cellules"), ("l'œuf", "la première cellule du petit"), ("le microscope", "permet de voir les cellules")],
            ["Ouvre la fiche " + FICHE + ".", "Une rencontre : la fécondation.", "Le microscope grossit ce qui est minuscule."]),
        "lieutenant": assoc(
            "Relie chaque mot à sa définition, puis choisis la phrase de la fiche qui nomme les gamètes.",
            [("le gamète mâle", "le spermatozoïde"), ("le gamète femelle", "l'ovule"), ("la fécondation", "l'union d'un spermatozoïde et d'un ovule"),
             ("la cellule-œuf", "la première cellule du futur animal"), ("le flagelle", "fait avancer le spermatozoïde")],
            ["Les gamètes sont les cellules reproductrices.", "Le flagelle est une sorte de queue.", "Pour la justification : cherche « reproductrices »."],
            J("Quelle phrase de la fiche nomme les gamètes ?", F_GAMETES, [F_ORGANES, F_FECOND, F_SEXUEE], pos=1)),
        "second": assoc(
            "Relie chaque étape à ce qui se passe, puis choisis la phrase de la fiche qui dit ce que donne la fécondation.",
            [("avant la fécondation", "le mâle et la femelle produisent leurs gamètes"), ("la fécondation", "un spermatozoïde s'unit à l'ovule"),
             ("juste après", "il y a une seule cellule, la cellule-œuf"), ("ensuite", "la cellule-œuf se divise"), ("plus tard", "un embryon de milliers de cellules")],
            ["Une seule cellule juste après l'union.", "Les divisions viennent ensuite.", "Pour la justification : cherche « toute première »."],
            J("Quelle phrase de la fiche dit ce que donne la fécondation ?", F_OEUF, [F_EMBRYON, F_FECOND, F_UN], pos=2)),
    }
    d["e1-4"] = {
        "lieutenant": ordre(
            "Inès prépare l'affiche des visiteurs. Remets les six étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit la naissance de l'embryon.",
            ["Le mâle produit des spermatozoïdes, la femelle des ovules.", "Des spermatozoïdes s'approchent de l'ovule.", "Un seul spermatozoïde s'unit à l'ovule.",
             "Une cellule-œuf est formée.", "La cellule-œuf se divise en deux, puis en quatre.", "Des milliers de cellules forment un embryon."],
            ["Les gamètes sont fabriqués en premier.", "Plusieurs approchent, un seul s'unit.", "Pour la justification : cherche « divise »."],
            J("Quelle phrase de la fiche décrit la formation de l'embryon ?", F_EMBRYON, [F_OEUF, F_UN, F_GAMETES], pos=3)),
        "second": ordre(
            "Range du plus petit au plus grand, puis choisis la phrase de la fiche qui explique pourquoi le petit ressemble à ses deux parents.",
            [("le spermatozoïde", "minuscule, mobile"), ("l'ovule", "une seule grosse cellule avec des réserves"),
             ("l'embryon", "des milliers de cellules"), ("le poussin qui sort de l'œuf", "des milliards de cellules")],
            ["Le spermatozoïde est le plus petit.", "Une cellule, puis des milliers, puis des milliards.", "Pour la justification : cherche « ressemble »."],
            J("Quelle phrase de la fiche explique la ressemblance avec les deux parents ?", F_PARENTS, [F_SEXUEE, F_TAILLE, F_ESPECE], pos=1)),
    }
    return d
