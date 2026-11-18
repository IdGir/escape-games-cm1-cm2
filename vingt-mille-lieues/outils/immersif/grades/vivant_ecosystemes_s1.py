"""Salle 1 « La tente-laboratoire » : grades mousse, lieutenant, second (fiche : Observer le vivant, l'espèce)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "vivant-ecosystemes", "tests", "donnees"))
from fiches import *
from schemas import oiseau, cellule

FICHE = "« Observer le vivant, l'espèce »"


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": {"type": "plan", "titre": "Le carnet de Lina", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "le bec"}, {"libelle": "Repère 2", "reponse": "l'œil"}, {"libelle": "Repère 3", "reponse": "l'aile"}],
                   "etiquettes": ["le bec", "l'œil", "l'aile"],
                   "consigne": "Place chaque mot sur son repère." + oiseau(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Le bec est pointu, au bout de la tête.", "L'aile est au milieu du corps."]},
        "lieutenant": {"type": "plan", "titre": "La cellule de Lina", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "la paroi"}, {"libelle": "Repère 2", "reponse": "la membrane"},
                                 {"libelle": "Repère 3", "reponse": "le cytoplasme"}, {"libelle": "Repère 4", "reponse": "le noyau"}],
                       "etiquettes": ["la paroi", "la membrane", "le cytoplasme", "le noyau", "la coquille", "le poil"],
                       "consigne": "Lina observe une feuille de la mare au microscope. Place chaque mot sur son repère (deux sont en trop), puis choisis la phrase de la fiche qui décrit une cellule." + cellule(4),
                       "indices": ["La paroi est l'épaisse bordure extérieure des cellules de plantes.", "Le noyau est la grosse boule.", "Pour la justification : cherche « membrane »."],
                       "justification": J("Quelle phrase de la fiche décrit les parties d'une cellule ?", A_PARTIES, [A_CELLULE, A_UNI, A_ORGANES], pos=1)},
        "second": tri(
            "Lina compare une cellule de feuille et une cellule de peau de grenouille. Range chaque partie : seulement chez la plante, ou chez les deux. Puis choisis la phrase de la fiche qui le dit.",
            [("plante", "Seulement dans la cellule de la plante"), ("deux", "Dans les deux cellules")],
            [("la paroi", "plante"), ("la membrane", "deux"), ("le cytoplasme", "deux"), ("le noyau", "deux")],
            ["La paroi est en plus chez les plantes.", "Toutes les cellules ont une membrane.", "Pour la justification : cherche « en plus »."],
            J("Quelle phrase de la fiche dit ce que les cellules des plantes ont en plus ?", A_PARTIES, [A_CELLULE, A_ORGANES, A_UNI], pos=2)),
    }
    d["e1-2"] = {
        "mousse": vf(
            "Lina a écrit trois phrases. Pour chacune, choisis vrai ou faux.",
            [("Une mésange a des plumes.", True, "C'est un oiseau."),
             ("Un caniche et un berger allemand sont deux chiens.", True, "Ils sont de la même espèce."),
             ("Un escargot a six pattes.", False, "Il n'a pas de pattes : il glisse sur son pied.")],
            ["Ouvre la fiche " + FICHE + ".", "Les oiseaux ont des plumes.", "L'escargot glisse."]),
        "lieutenant": vf(
            "Lina relit les notes d'un stagiaire. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui explique le cas du mulet.",
            [("Le mulet ne peut pas avoir de petits.", True, "L'âne et le cheval sont deux espèces."),
             ("Tous les êtres vivants sont faits de cellules.", True, "C'est l'unité commune du vivant."),
             ("Une paramécie est faite de milliards de cellules.", False, "Elle n'a qu'une seule cellule."),
             ("Les feuilles et les racines sont des organes.", True, "Faits de nombreuses cellules."),
             ("Ce qu'un animal mange est un de ses attributs.", False, "Un attribut se voit sur l'être vivant.")],
            ["La paramécie se voit au microscope.", "Un organe est fait de cellules.", "Pour la justification : cherche « mulet »."],
            J("Quelle phrase de la fiche explique le cas du mulet ?", A_MULET, [A_ESPECE, A_RACES, A_NOM], pos=2)),
        "second": vf(
            "Lina prépare un quiz pour les guides de la réserve. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur le nom scientifique.",
            [("Le héron cendré s'appelle Ardea cinerea dans tous les pays.", True, "C'est son nom scientifique."),
             ("Deux êtres vivants qui se ressemblent beaucoup sont toujours de la même espèce.", False, "Ils doivent aussi pouvoir avoir des petits capables de se reproduire."),
             ("Faire l'inventaire d'un lieu permet de mesurer sa biodiversité.", True, "On note toutes ses espèces."),
             ("La levure est un être vivant d'une seule cellule.", True, "On ne la voit qu'au microscope."),
             ("L'endroit où vit un animal est un de ses attributs.", False, "Ce n'est pas une chose que l'on voit sur lui.")],
            ["Se ressembler ne suffit pas.", "La levure fait gonfler la pâte à pain.", "Pour la justification : cherche « deux mots »."],
            J("Quelle phrase de la fiche parle du nom scientifique ?", A_NOM, [A_INVENTAIRE, A_ESPECE, A_COMPTER], pos=0)),
    }
    d["e1-3"] = {
        "mousse": assoc(
            "Relie chaque animal à ce qu'il possède.",
            [("la mésange", "des plumes"), ("le renard", "des poils"), ("l'escargot", "une coquille")],
            ["Ouvre la fiche " + FICHE + ".", "Les oiseaux ont des plumes.", "L'escargot porte sa maison."]),
        "lieutenant": assoc(
            "Relie chaque être vivant à ce que Lina a vu au microscope ou à la loupe, puis choisis la phrase de la fiche sur les êtres vivants d'une seule cellule.",
            [("la paramécie", "une seule cellule qui nage dans la mare"), ("la levure", "une seule cellule qui fait gonfler la pâte"),
             ("la feuille de nénuphar", "un organe fait de nombreuses cellules à paroi"), ("le cœur de la grenouille", "un organe fait de nombreuses cellules sans paroi"),
             ("l'araignée", "huit pattes")],
            ["Une seule cellule : paramécie et levure.", "Les cellules de plantes ont une paroi.", "Pour la justification : cherche « paramécie »."],
            J("Quelle phrase de la fiche parle des êtres vivants d'une seule cellule ?", A_UNI, [A_CELLULE, A_ORGANES, A_PARTIES], pos=3)),
        "second": assoc(
            "Relie chaque observation de Lina à ce qu'elle décrit, puis choisis la phrase de la fiche qui dit ce qui n'est pas un attribut.",
            [("des plumes sur les ailes", "un attribut"), ("il mange des graines", "un régime alimentaire, pas un attribut"),
             ("il vit près de l'étang", "un lieu de vie, pas un attribut"), ("six pattes et quatre ailes", "des attributs comptés avec précision"),
             ("ses petits auront des petits", "un critère de l'espèce")],
            ["Un attribut se voit sur l'être vivant.", "Manger et habiter ne se voient pas sur lui.", "Pour la justification : cherche « ne sont pas »."],
            J("Quelle phrase de la fiche dit ce qui n'est pas un attribut ?", A_PAS_FAIT, [A_OBSERVER, A_COMPTER, A_ESPECE], pos=1)),
    }
    d["e1-4"] = {
        "lieutenant": tri(
            "Les visiteurs demandent : « Même espèce ou pas ? » Range chaque paire, puis choisis la phrase de la fiche qui définit l'espèce.",
            [("meme", "Même espèce"), ("diff", "Deux espèces")],
            [("un caniche et un berger allemand", "meme"), ("une poule rousse et un coq blanc", "meme"), ("un chat roux et un chat noir", "meme"),
             ("un âne et une jument", "diff"), ("un loup et un renard", "diff"), ("une grenouille verte et un crapaud", "diff")],
            ["Les races de chiens sont une seule espèce.", "Le mulet n'a pas de petits.", "Pour la justification : cherche « à leur tour »."],
            J("Quelle phrase de la fiche définit l'espèce ?", A_ESPECE, [A_RACES, A_MULET, A_INVENTAIRE], pos=0)),
        "second": ordre(
            "Lina range du plus petit au plus grand ce qu'elle étudie, puis choisis la phrase de la fiche sur les organes.",
            [("une cellule de feuille", "visible seulement au microscope"), ("une feuille", "un organe"), ("un chêne", "un être vivant"),
             ("tous les chênes pédonculés de la réserve", "des êtres vivants de la même espèce")],
            ["La cellule est la plus petite.", "Un organe est fait de cellules.", "Pour la justification : cherche « organes »."],
            J("Quelle phrase de la fiche relie cellules et organes ?", A_ORGANES, [A_CELLULE, A_PARTIES, A_UNI], pos=3)),
    }
    return d
