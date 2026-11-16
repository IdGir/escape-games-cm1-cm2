# -*- coding: utf-8 -*-
"""Leçons imprimables — La Centrale en panne (électricité, jeu n°14, version immersive seule).
Visuels : schémas dessinés de lecons.json (circuit fermé, circuit testeur, symboles normalisés, pile ou secteur,
de la centrale à la prise), tableaux, étapes et barres de la production française 2025 (RTE).
Aucun visuel généré par IA. La page est écrite dans electricite/ (données sources du jeu)."""
from graphiques import barres, tableau, etapes

JEU = {
    "titre": "La Centrale en panne",
    "matiere": "Sciences et technologie",
    "theme": "Le circuit électrique, conducteurs et isolants, le schéma normalisé, la sécurité électrique, produire et transporter l'électricité",
    "couleur": "#1f3b57", "accent": "#d18a12",
    "couleur_pale": "#e5edf5", "accent_pale": "#fbf0dc",
}
BLEU, AMBRE = "#1f3b57", "#d18a12"

OUVERT_FERME = tableau(["Circuit", "La boucle", "La lampe"], [
    ["fermé", "complète, sans trou", "brille"],
    ["ouvert", "coupée (fil débranché, interrupteur ouvert)", "éteinte"]],
    couleur=BLEU, largeurs=[1, 2, 1], label="Tableau : circuit fermé, la lampe brille ; circuit ouvert, la lampe est éteinte")

MATERIAUX = tableau(["Conducteurs", "Isolants"], [
    ["cuivre, fer, aluminium, or", "plastique, verre, bois sec"],
    ["mine de crayon (graphite)", "caoutchouc, papier, tissu, air sec"]],
    couleur=BLEU, largeurs=[1, 1], label="Tableau : matériaux conducteurs et matériaux isolants")

LIRE_SCHEMA = etapes([("Départ", "poser le doigt sur la borne + de la pile"),
                      ("Suivre", "passer par chaque appareil, le long des fils"),
                      ("Vérifier", "chercher un trou ou un interrupteur ouvert"),
                      ("Arrivée", "revenir à la borne − : la boucle est complète")],
                     sens="v", couleur=BLEU, label="Étapes pour lire un schéma électrique : de la borne + à la borne −")

REGLES = tableau(["Je ne fais jamais…", "Je fais…"], [
    ["mettre un objet dans une prise", "tirer sur la fiche, pas sur le fil"],
    ["toucher un appareil les mains mouillées", "éteindre la lumière en sortant"],
    ["jouer près des lignes électriques", "en cas d'accident : couper le courant, appeler le 18 ou le 112"]],
    couleur=BLEU, largeurs=[1, 1], label="Tableau des règles de sécurité électrique")

PRODUCTION = barres([("nucléaire", 68), ("hydraulique", 11), ("éolien", 9), ("solaire", 6), ("gaz", 3)],
                    unite="%", titre_y="", W=430, couleur=AMBRE,
                    label="Barres : production d'électricité en France en 2025, nucléaire 68 %, hydraulique 11 %, éolien 9 %, solaire 6 %, gaz 3 %")

LECONS = {
    "circuit": {
        "competence": "Réaliser un circuit électrique à une boucle (pile, interrupteur, un ou deux récepteurs) ; distinguer circuit ouvert et circuit fermé.",
        "visuels": [
            {"type": "schema", "titre": "Un circuit fermé"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Ouvert ou fermé ?", "svg": OUVERT_FERME,
             "legende": "Ne jamais relier directement les deux bornes de la pile : c'est un court-circuit."},
        ],
    },
    "conducteurs": {
        "competence": "Identifier des matériaux conducteurs et isolants ; savoir qu'un même objet peut être fabriqué dans l'un ou l'autre type de matériau.",
        "visuels": [
            {"type": "schema", "titre": "Le circuit testeur"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Laisser passer ou non le courant", "svg": MATERIAUX,
             "legende": "Un fil électrique : un cœur en cuivre (conducteur) dans une gaine en plastique (isolant)."},
        ],
    },
    "schema": {
        "competence": "Réaliser et schématiser un circuit ; lire et utiliser des schémas normalisés ; justifier le fonctionnement par une boucle ininterrompue de récepteurs et de conducteurs.",
        "visuels": [
            {"type": "schema", "titre": "Les symboles normalisés"},
            {"type": "svg", "etiquette": "Schéma", "titre": "Lire un schéma avec le doigt", "svg": LIRE_SCHEMA,
             "legende": "Deux schémas sont équivalents si les appareils sont reliés de la même façon."},
        ],
    },
    "securite": {
        "competence": "Connaître et appliquer les règles de sécurité électrique (pile sans danger, secteur dangereux) ; citer des gestes pour économiser l'électricité.",
        "visuels": [
            {"type": "schema", "titre": "Pile ou secteur ?"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Les bons gestes", "svg": REGLES,
             "legende": "Pile plate de la classe : 4,5 V, sans danger. Prise de la maison : 230 V, dangereuse."},
        ],
    },
    "production": {
        "competence": "Décrire la production et le transport de l'électricité : centrales, sources renouvelables ou non, trajet de la centrale à la prise.",
        "visuels": [
            {"type": "schema", "titre": "De la centrale à la prise"},
            {"type": "svg", "etiquette": "Graphique", "titre": "D'où vient l'électricité en France (2025)", "svg": PRODUCTION,
             "legende": "Part de chaque source dans la production : 547,5 TWh au total. Source : RTE, Bilan électrique 2025."},
        ],
    },
}
