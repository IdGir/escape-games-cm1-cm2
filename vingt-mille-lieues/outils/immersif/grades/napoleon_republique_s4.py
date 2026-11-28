"""Salle 4 « Le dôme des Invalides » (aujourd'hui) : grades mousse, lieutenant, second (fiche : Ce qui reste de l'Empire)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "napoleon-republique", "tests", "donnees"))
from fiches import *

FICHE = "« Ce qui reste de l'Empire »"


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": assoc(
            "Relie chaque monument à ce qu'il rappelle.",
            [("l'Arc de triomphe", "les victoires de l'armée"), ("la colonne Vendôme", "le bronze des canons"), ("les Invalides", "le tombeau de Napoléon")],
            ["Ouvre la fiche " + FICHE + ".", "Un arc de triomphe célèbre des victoires.", "Un tombeau : le lieu où repose un mort."]),
        "lieutenant": assoc(
            "Relie chaque monument à son histoire, puis choisis la phrase de la fiche qui parle de l'Arc de triomphe aujourd'hui.",
            [("l'Arc de triomphe de l'Étoile", "décidé en 1806, achevé en 1836"), ("la colonne Vendôme", "recouverte du bronze de canons d'Austerlitz"),
             ("le dôme des Invalides", "le tombeau de Napoléon"), ("la cathédrale Notre-Dame", "le lieu du sacre")],
            ["L'Arc a mis trente ans à être construit.", "Austerlitz a fourni des canons.", "Pour la justification : cherche « Soldat inconnu »."],
            J("Quelle phrase de la fiche dit qui repose sous l'Arc de triomphe aujourd'hui ?", H_SOLDAT, [H_ARC, H_VENDOME, H_INVAL], pos=1)),
        "second": assoc(
            "Relie chaque date à l'histoire d'un monument, puis choisis la phrase de la fiche sur le retour des cendres.",
            [("1806", "Napoléon décide la construction de l'Arc de triomphe"), ("1836", "l'Arc de triomphe est achevé"),
             ("1840", "les cendres de Napoléon reviennent de Sainte-Hélène"), ("1921", "le Soldat inconnu est inhumé sous l'Arc")],
            ["L'Arc est achevé après la mort de Napoléon.", "Le Soldat inconnu est un soldat de 1914-1918.", "Pour la justification : cherche « cendres »."],
            J("Quelle phrase de la fiche parle du retour des cendres de Napoléon ?", H_INVAL, [H_ARC, H_SOLDAT, H_VENDOME], pos=3)),
    }
    d["e4-2"] = {
        "mousse": intrus(
            "Un objet n'a pas été créé par Napoléon : trouve l'intrus.",
            [("le Code civil", False), ("les lycées", False), ("le droit de vote des femmes", True)],
            ["Ouvre la fiche " + FICHE + ".", "Le Code civil date de 1804.", "Les femmes votent bien plus tard."]),
        "lieutenant": intrus(
            "Trouve l'institution qui n'a pas été créée par Bonaparte, puis choisis la phrase de la fiche qui définit le rôle des préfets.",
            [("la Banque de France", False), ("les préfets", False), ("la Légion d'honneur", False), ("les lycées", False), ("l'école gratuite et obligatoire pour tous", True)],
            ["Toutes les vraies créations datent de 1800 à 1804.", "L'école obligatoire date des années 1880.", "Pour la justification : cherche « département »."],
            J("Quelle phrase de la fiche définit le rôle des préfets ?", H_PREFETS, [H_BANQUE, H_LYCEES, H_LEGION], pos=0)),
        "second": intrus(
            "Une seule carte décrit une décision de la Révolution, et non de Bonaparte : trouve-la. Puis choisis la phrase de la fiche qui explique à quoi servent les lycées.",
            [("créer la Banque de France", False), ("créer les préfets", False), ("créer la Légion d'honneur", False), ("promulguer le Code civil", False), ("abolir l'esclavage en 1794", True)],
            ["Bonaparte rétablit l'esclavage, il ne l'abolit pas.", "L'abolition de 1794 date de la Révolution.", "Pour la justification : cherche « officiers, ingénieurs »."],
            J("Quelle phrase de la fiche explique à quoi servent les lycées ?", H_LYCEES, [H_LEGION, H_PREFETS, H_CODE], pos=2)),
    }
    d["e4-3"] = {
        "mousse": tri(
            "Range chaque carte : ce qui reste aujourd'hui, ou la part d'ombre de l'Empire ?",
            [("heritage", "Ce qui reste"), ("ombre", "La part d'ombre")],
            [("le Code civil", "heritage"), ("les lycées", "heritage"), ("des guerres et beaucoup de morts", "ombre")],
            ["Ouvre la fiche " + FICHE + ".", "Ce qui existe encore est un héritage.", "Les guerres font beaucoup de victimes."]),
        "lieutenant": tri(
            "Range chaque carte, puis choisis la phrase de la fiche qui montre que l'Empire est un régime autoritaire.",
            [("heritage", "Un héritage durable"), ("ombre", "Une part d'ombre")],
            [("l'égalité de tous devant la loi", "heritage"), ("les préfets", "heritage"), ("la Banque de France", "heritage"),
             ("le rétablissement de l'esclavage en 1802", "ombre"), ("la censure des journaux", "ombre"), ("l'arrestation des opposants", "ombre")],
            ["La censure empêche de critiquer.", "L'égalité devant la loi vient de la Révolution.", "Pour la justification : cherche « autoritaire »."],
            J("Quelle phrase de la fiche montre que l'Empire est un régime autoritaire ?", H_OMBRES, [H_ESCLAV, H_FEMMES, H_EGALITE], pos=1)),
        "second": tri(
            "Le Code civil a deux faces. Range chaque article : idée héritée de la Révolution, ou inégalité ? Puis choisis la phrase de la fiche qui montre l'inégalité.",
            [("heritage", "Une idée de la Révolution"), ("ombre", "Une inégalité")],
            [("tous les Français sont égaux devant la loi", "heritage"), ("chacun peut choisir son travail", "heritage"), ("le droit de propriété est protégé", "heritage"),
             ("la femme mariée doit obéir à son mari", "ombre"), ("l'esclavage est rétabli dans les colonies", "ombre")],
            ["Égalité, liberté, propriété : des idées de 1789.", "Le mari a l'autorité sur sa femme.", "Pour la justification : cherche « femme mariée »."],
            J("Quelle phrase de la fiche montre une inégalité du Code civil ?", H_FEMMES, [H_EGALITE, H_CODE, H_OMBRES], pos=0)),
    }
    d["e4-4"] = {
        "lieutenant": vf(
            "Vérifie les dates des fiches du musée, puis choisis la phrase de la fiche qui date le Code civil.",
            [("La Banque de France est créée le 18 janvier 1800.", True, "Sous le Consulat."), ("Les préfets sont créés en 1900.", False, "Le 17 février 1800."),
             ("La Légion d'honneur est créée le 19 mai 1802.", True, "Elle récompense les mérites."), ("Les cendres de Napoléon reviennent dès 1821.", False, "En 1840.")],
            ["Tout est créé entre 1800 et 1804.", "Il meurt en 1821 à Sainte-Hélène.", "Pour la justification : cherche « 21 mars »."],
            J("Quelle phrase de la fiche date le Code civil ?", H_CODE, [H_EGALITE, H_LEGION, H_BANQUE], pos=3)),
        "second": vf(
            "Vérifie ces phrases d'un guide pressé, puis choisis la phrase de la fiche sur le rétablissement de l'esclavage.",
            [("Le Code civil est promulgué avant le sacre.", True, "Le 21 mars 1804, le sacre a lieu le 2 décembre."),
             ("L'esclavage rétabli en 1802 est aboli définitivement dès 1804.", False, "En 1848."),
             ("Les lycées et la Légion d'honneur sont créés la même année.", True, "En 1802."),
             ("La Banque de France est créée après le Code civil.", False, "En 1800, quatre ans avant.")],
            ["Mars avant décembre.", "L'abolition définitive vient sous la IIe République.", "Pour la justification : cherche « 1848 »."],
            J("Quelle phrase de la fiche parle du rétablissement de l'esclavage ?", H_ESCLAV, [H_OMBRES, H_FEMMES, H_CODE], pos=2)),
    }
    return d
