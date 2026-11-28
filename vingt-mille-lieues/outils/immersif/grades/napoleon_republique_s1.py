"""Salle 1 « Le palais des Tuileries » (1793-1802) : grades mousse, lieutenant, second (fiche : Du général au Premier consul)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "napoleon-republique", "tests", "donnees"))
from fiches import *

FICHE = "« Du général au Premier consul »"


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": ordre(
            "Les pages du carnet d'Antoine sont mélangées. Remets-les dans l'ordre, de la plus ancienne à la plus récente.",
            [("Bonaparte devient général à Toulon", "1793"), ("il gagne des batailles en Italie", "1796"), ("il prend le pouvoir", "1799")],
            ["Ouvre la fiche " + FICHE + ".", "Regarde les années : la plus petite d'abord.", "1793, puis 1796, puis 1799."]),
        "lieutenant": ordre(
            "Remets la vie de Bonaparte dans l'ordre chronologique, puis choisis la phrase de la fiche qui explique comment il devient général.",
            [("naissance à Ajaccio", "15 août 1769"), ("reprise du port de Toulon", "décembre 1793"), ("victoires d'Arcole et de Rivoli", "1796-1797"),
             ("bataille des Pyramides", "21 juillet 1798"), ("coup d'État du 18 brumaire", "9 novembre 1799")],
            ["La naissance d'abord.", "L'Italie avant l'Égypte.", "Pour la justification : cherche « Toulon »."],
            J("Quelle phrase de la fiche explique comment Bonaparte devient général ?", G_TOULON, [G_OFFICIER, G_ITALIE, G_NAISS], pos=1)),
        "second": ordre(
            "Remets dans l'ordre les étapes qui mènent Bonaparte au pouvoir à vie, puis choisis la phrase de la fiche qui définit le Consulat.",
            [("reprise de Toulon", "décembre 1793"), ("campagne d'Italie", "1796-1797"), ("coup d'État du 18 brumaire", "9 novembre 1799"),
             ("signature du Concordat", "15 juillet 1801"), ("Bonaparte consul à vie", "1802")],
            ["Le Concordat vient après le coup d'État.", "« À vie » : la dernière étape.", "Pour la justification : cherche « trois consuls »."],
            J("Quelle phrase de la fiche définit le Consulat ?", G_CONSULAT, [G_BRUMAIRE, G_VIE, G_CONCORDAT], pos=3)),
    }
    d["e1-2"] = {
        "mousse": assoc(
            "Relie chaque lieu à ce qui s'y est passé.",
            [("Toulon", "un port repris aux Anglais"), ("l'Égypte", "les pyramides et les savants"), ("Paris", "la prise du pouvoir")],
            ["Ouvre la fiche " + FICHE + ".", "Toulon est un port.", "Les pyramides sont en Égypte."]),
        "lieutenant": assoc(
            "Relie chaque mot à sa définition, puis choisis la phrase de la fiche qui parle des savants d'Égypte.",
            [("un coup d'État", "une prise du pouvoir par la force"), ("le Consulat", "le régime qui commence en 1799"),
             ("le Concordat", "l'accord signé avec le pape en 1801"), ("la pierre de Rosette", "une pierre qui aidera à lire les hiéroglyphes")],
            ["Le Concordat concerne l'Église.", "Rosette : une écriture à déchiffrer.", "Pour la justification : cherche « hiéroglyphes »."],
            J("Quelle phrase de la fiche parle du travail des savants en Égypte ?", G_SAVANTS, [G_EGYPTE, G_GLOIRE, G_CONCORDAT], pos=0)),
        "second": assoc(
            "Relie chaque moyen utilisé par Bonaparte à son but, puis choisis la phrase de la fiche qui montre comment il soigne sa popularité.",
            [("raconter ses victoires dans les journaux et les tableaux", "devenir populaire en France"), ("emmener des savants en Égypte", "étudier un pays lointain"),
             ("signer le Concordat", "faire la paix avec l'Église catholique"), ("devenir consul à vie", "garder le pouvoir jusqu'à sa mort")],
            ["Les tableaux servent la gloire du général.", "Le Concordat apaise les catholiques.", "Pour la justification : cherche « populaire »."],
            J("Quelle phrase de la fiche montre comment Bonaparte soigne sa popularité ?", G_GLOIRE, [G_ITALIE, G_VIE, G_SAVANTS], pos=2)),
    }
    d["e1-3"] = {
        "mousse": vf(
            "Pour chaque phrase, choisis vrai ou faux.",
            [("Bonaparte est né en Corse.", True, "À Ajaccio."), ("Bonaparte a été élu par tous les Français en 1799.", False, "Il prend le pouvoir par la force."),
             ("Sous le Consulat, Bonaparte décide de presque tout.", True, "C'est le Premier consul.")],
            ["Ouvre la fiche " + FICHE + ".", "Ajaccio est en Corse.", "Un coup d'État n'est pas une élection."]),
        "lieutenant": vf(
            "Trie les rumeurs du palais, puis choisis la phrase de la fiche qui date le coup d'État.",
            [("Bonaparte est nommé général à 24 ans.", True, "Après Toulon, en 1793."), ("Le 18 brumaire an VIII correspond au 9 novembre 1799.", True, "Deux calendriers, une même date."),
             ("En Égypte, Bonaparte voyage sans savants.", False, "Des savants l'accompagnent."), ("En 1802, Bonaparte devient roi.", False, "Il devient consul à vie.")],
            ["Toulon : décembre 1793.", "Le roi Louis XVI est mort en 1793.", "Pour la justification : cherche « brumaire »."],
            J("Quelle phrase de la fiche date le coup d'État ?", G_BRUMAIRE, [G_CONSULAT, G_VIE, G_TOULON], pos=2)),
        "second": vf(
            "Vérifie ces affirmations d'un visiteur, puis choisis la phrase de la fiche qui montre que Bonaparte garde le pouvoir pour toujours.",
            [("Le Consulat est une démocratie où tous les consuls ont le même pouvoir.", False, "Le Premier consul a presque tous les pouvoirs."),
             ("La Corse est devenue française un an avant la naissance de Bonaparte.", True, "En 1768."),
             ("Le Concordat fait la paix avec l'Église catholique.", True, "Signé le 15 juillet 1801."),
             ("Bonaparte arrive au pouvoir par des élections libres.", False, "Par le coup d'État du 18 brumaire.")],
            ["Trois consuls, mais un seul vrai chef.", "1769 - 1 = 1768.", "Pour la justification : cherche « à vie »."],
            J("Quelle phrase de la fiche montre que Bonaparte garde le pouvoir jusqu'à sa mort ?", G_VIE, [G_CONSULAT, G_CONCORDAT, G_BRUMAIRE], pos=0)),
    }
    d["e1-4"] = {
        "lieutenant": qcm(
            "Réponds aux questions de l'officier, puis choisis la phrase de la fiche sur les victoires d'Italie.",
            [("Contre quel pays Bonaparte se bat-il en Italie ?", ["l'Angleterre", "l'Autriche", "l'Espagne", "la Russie"], 1, "Arcole et Rivoli."),
             ("Combien y a-t-il de consuls ?", ["un", "deux", "trois", "cinq"], 2, "Le Premier consul domine."),
             ("Quel jour correspond au 18 brumaire an VIII ?", ["le 9 novembre 1799", "le 14 juillet 1789", "le 2 décembre 1804", "le 18 juin 1815"], 0, "Calendrier républicain."),
             ("Avec qui Bonaparte signe-t-il le Concordat ?", ["le roi d'Angleterre", "le pape", "le sultan d'Égypte", "le tsar"], 1, "En 1801.")],
            ["Arcole et Rivoli : contre l'Autriche.", "Le Concordat : avec l'Église.", "Pour la justification : cherche « Arcole »."],
            J("Quelle phrase de la fiche parle des victoires d'Italie ?", G_ITALIE, [G_TOULON, G_EGYPTE, G_GLOIRE], pos=3)),
        "second": qcm(
            "L'officier pose des questions de réflexion. Réponds, puis choisis la phrase de la fiche sur la bataille des Pyramides.",
            [("Pourquoi Bonaparte fait-il peindre et raconter ses victoires ?", ["pour devenir populaire et préparer son pouvoir", "pour vendre des tableaux", "parce qu'il est peintre", "pour cacher ses victoires"], 0, "C'est de la propagande."),
             ("Pourquoi le coup d'État n'est-il pas démocratique ?", ["parce que le pouvoir est pris par la force, sans élection", "parce qu'il a lieu en novembre", "parce que Bonaparte est corse", "parce qu'il y a trois consuls"], 0, "Le peuple n'a pas choisi."),
             ("Quel régime commence après le 18 brumaire ?", ["la monarchie", "le Consulat", "l'Empire", "la Ve République"], 1, "Il dure de 1799 à 1804."),
             ("Pourquoi la pierre de Rosette est-elle précieuse ?", ["elle est en or", "elle aidera à lire les hiéroglyphes", "c'est une arme", "elle montre une carte"], 1, "Le même texte en plusieurs écritures.")],
            ["La propagande sert la gloire du chef.", "Un coup d'État se fait sans vote.", "Pour la justification : cherche « Pyramides »."],
            J("Quelle phrase de la fiche date la bataille des Pyramides ?", G_EGYPTE, [G_SAVANTS, G_ITALIE, G_BRUMAIRE], pos=1)),
    }
    return d
