"""Salle 3 « La galerie des surprises » : grades mousse, lieutenant, second (fiche : Ovipares et vivipares)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "naissances-animaux", "tests", "donnees"))
from fiches import *

FICHE = "« Ovipares et vivipares »"


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": intrus(
            "Dans la vitrine des animaux qui pondent, une fiche s'est glissée par erreur. Trouve-la.",
            [("la poule", False), ("la cane", False), ("la vache", True)],
            ["Ouvre la fiche " + FICHE + ".", "Lequel ne pond pas d'œufs ?", "Le veau naît vivant."]),
        "lieutenant": intrus(
            "Dans la vitrine des mammifères vivipares, Malo a placé un animal qui ne fait pas comme les autres. Trouve-le, puis choisis la phrase de la fiche qui le décrit.",
            [("le chat", False), ("le lapin", False), ("l'ornithorynque", True), ("la girafe", False), ("le dauphin", False)],
            ["Tous sont des mammifères.", "L'un d'eux pond des œufs.", "Pour la justification : cherche « Australie »."],
            J("Quelle phrase de la fiche décrit cet animal ?", O_ORNITHO, [O_EX_VIVI, O_PLACENTA, O_VIPERE], pos=2)),
        "second": intrus(
            "Dans la vitrine « fécondation interne et ponte », un animal s'est glissé par erreur. Trouve-le, puis choisis la phrase de la fiche qui relie fécondation et mode de reproduction.",
            [("la poule", False), ("la tortue", False), ("le papillon", False), ("la grenouille", True), ("le crocodile", False)],
            ["Tous pondent des œufs.", "Lequel a une fécondation dans l'eau ?", "Pour la justification : cherche « ovipare ou vivipare »."],
            J("Quelle phrase de la fiche relie fécondation et mode de reproduction ?", O_LIEN, [O_OVIPARE, O_EX_OVI, O_REQUINS], pos=0)),
    }
    d["e3-2"] = {
        "mousse": tri(
            "Malo range les animaux : ceux qui pondent des œufs et ceux dont le petit naît vivant.",
            [("ovi", "Il pond des œufs"), ("vivi", "Le petit naît vivant")],
            [("la poule", "ovi"), ("le crocodile", "ovi"), ("la vache", "vivi"), ("le lapin", "vivi"), ("le chat", "vivi")],
            ["Ouvre la fiche " + FICHE + ".", "Les oiseaux pondent.", "Les mammifères : le petit naît vivant."]),
        "lieutenant": tri(
            "Malo complète le tableau à deux entrées avec neuf animaux. Place chacun dans la bonne case, puis choisis la phrase de la fiche qui cite des vivipares.",
            [("ext-ovi", "Fécondation externe, ovipare"), ("int-ovi", "Fécondation interne, ovipare"), ("int-vivi", "Fécondation interne, vivipare")],
            [("le crapaud", "ext-ovi"), ("le saumon", "ext-ovi"), ("l'autruche", "int-ovi"), ("la coccinelle", "int-ovi"), ("la couleuvre", "int-ovi"),
             ("l'éléphant", "int-vivi"), ("le dauphin", "int-vivi"), ("la chauve-souris", "int-vivi"), ("le lapin", "int-vivi")],
            ["La couleuvre est un serpent qui pond.", "La chauve-souris est un mammifère.", "Pour la justification : cherche « Presque tous »."],
            J("Quelle phrase de la fiche cite des vivipares ?", O_EX_VIVI, [O_EX_OVI, O_VIVIPARE, O_LAIT], pos=1)),
        "second": tri(
            "Malo prépare une vitrine sur les requins et les serpents. Range chaque animal : il pond des œufs, ses œufs éclosent dans le ventre de la mère, ou ses petits se développent nourris par la mère. Puis choisis la phrase de la fiche sur les requins.",
            [("ovi", "Ovipare : il pond"), ("ovovivi", "Ovovivipare : œufs éclos dans le ventre"), ("vivi", "Vivipare : nourri par la mère")],
            [("la roussette", "ovi"), ("la couleuvre", "ovi"), ("la poule", "ovi"), ("la vipère aspic", "ovovivi"), ("le grand requin blanc", "ovovivi"),
             ("le requin-marteau", "vivi"), ("la vache", "vivi"), ("le dauphin", "vivi")],
            ["La roussette pond des capsules.", "La vipère aspic garde ses œufs dans son ventre.", "Pour la justification : cherche « roussette »."],
            J("Quelle phrase de la fiche parle des requins ?", O_REQUINS, [O_VIPERE, O_LIEN, O_ORNITHO], pos=3)),
    }
    d["e3-3"] = {
        "mousse": vf(
            "Malo raconte des surprises. Vrai ou faux ?",
            [("L'ornithorynque pond des œufs.", True, "C'est une exception chez les mammifères."),
             ("Tous les animaux pondent des œufs.", False, "Le chat et la vache ne pondent pas."),
             ("Le poussin sort d'un œuf.", True, "La poule est ovipare.")],
            ["Ouvre la fiche " + FICHE + ".", "Pense au chat.", "L'ornithorynque a un bec."]),
        "lieutenant": vf(
            "Malo vérifie le panneau des mammifères. Vrai ou faux ? Puis choisis la phrase de la fiche qui dit comment le petit d'un mammifère est nourri avant de naître.",
            [("Avant de naître, le veau reçoit sa nourriture par le placenta et le cordon ombilical.", True, "Il ne mange pas par la bouche."),
             ("Le chaton grandit dans un œuf pondu dans un panier.", False, "La chatte est vivipare."),
             ("Après la naissance, la lapine nourrit ses petits avec son lait.", True, "Comme tous les mammifères."),
             ("L'ornithorynque n'a pas de lait.", False, "Il nourrit ses petits avec son lait."),
             ("Le dauphin est un mammifère vivipare.", True, "Son petit naît vivant dans la mer.")],
            ["Placenta et cordon relient le petit à sa mère.", "Même l'ornithorynque donne du lait.", "Pour la justification : cherche « cordon ombilical »."],
            J("Quelle phrase de la fiche dit comment le petit est nourri avant de naître ?", O_PLACENTA, [O_VIVIPARE, O_LAIT, O_EX_VIVI], pos=0)),
        "second": vf(
            "Malo a reçu des panneaux d'un autre zoo, avec des erreurs. Vrai ou faux ? Puis choisis la phrase de la fiche sur la vipère aspic.",
            [("Les petits de la vipère aspic naissent déjà formés.", True, "Les œufs éclosent dans le ventre de la mère."),
             ("La vipère aspic est vivipare comme la vache, avec un placenta.", False, "Elle est ovovivipare : l'embryon vit des réserves de l'œuf."),
             ("La roussette pond des œufs protégés par une capsule.", True, "On l'appelle aussi « bourse de sirène »."),
             ("Tous les requins sont vivipares.", False, "La roussette pond."),
             ("Les exceptions montrent que le vivant est très divers.", True, "Elles ne changent pas la règle.")],
            ["Ovovivipare n'est pas vivipare.", "Les requins ne font pas tous pareil.", "Pour la justification : cherche « éclosion »."],
            J("Quelle phrase de la fiche parle de la vipère aspic ?", O_VIPERE, [O_REQUINS, O_ORNITHO, O_VIVIPARE], pos=2)),
    }
    d["e3-4"] = {
        "lieutenant": assoc(
            "Relie chaque œuf ou petit à ce qui le protège ou le nourrit, puis choisis la phrase de la fiche sur les œufs à coquille.",
            [("l'œuf de poule", "une coquille dure, sur la terre ferme"), ("l'œuf de grenouille", "une gelée, dans l'eau"), ("l'œuf de roussette", "une capsule, dans la mer"),
             ("le veau avant la naissance", "le placenta et le cordon"), ("le petit ornithorynque", "le lait de sa mère, après l'éclosion")],
            ["Coquille : oiseaux et reptiles.", "La grenouille pond dans la mare.", "Pour la justification : cherche « terre ferme »."],
            J("Quelle phrase de la fiche parle des œufs à coquille ?", O_COQUILLE, [O_OVIPARE, O_EX_OVI, O_PLACENTA], pos=1)),
        "second": assoc(
            "Relie chaque animal à sa façon de naître et d'être nourri, puis choisis la phrase de la fiche qui dit ce que font toutes les femelles mammifères après la naissance.",
            [("l'ornithorynque", "sort d'un œuf, puis boit le lait de sa mère"), ("le chaton", "nourri par le placenta, puis par le lait"),
             ("le petit de la vipère aspic", "nourri par les réserves de l'œuf, naît formé"), ("le poussin", "nourri par le jaune, sort de l'œuf"),
             ("le têtard", "sort d'un œuf pondu dans l'eau")],
            ["L'ornithorynque : œuf, puis lait.", "La vipère : les réserves de l'œuf.", "Pour la justification : cherche « lait »."],
            J("Quelle phrase de la fiche parle du lait ?", O_LAIT, [O_ORNITHO, O_PLACENTA, O_VIVIPARE], pos=3)),
    }
    return d
