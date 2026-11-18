# -*- coding: utf-8 -*-
"""Leçons imprimables — La Caravelle du capitaine (grandes explorations, jeu n°13, version immersive seule).
Compétences : histoire, cycle 3, thème « Explorations et conquêtes » (programme 2026), d'après le tableau
« Compétences du programme » du README du jeu.
Visuels : schémas du jeu (lecons.json), une carte dessinée à partir de Natural Earth (route des épices,
simplifiés), tableaux. Aucun visuel généré par IA. La page est écrite dans grandes-explorations/."""
from graphiques import tableau, etapes

JEU = {
    "titre": "La Caravelle du capitaine",
    "matiere": "Histoire",
    "theme": "Les raisons des explorations, les progrès techniques, les grands voyages, la rencontre avec les peuples d'Amérique et la conquête, les premiers empires coloniaux",
    "couleur": "#6b4a2b", "accent": "#c9a227",
    "couleur_pale": "#f1e9df", "accent_pale": "#f8f0d4",
}
BRUN, OR, ROUGE, BLEU, VERT = "#6b4a2b", "#b8860b", "#b3261e", "#2f6690", "#2e7d32"
SIMPLIFIE = "Tracés simplifiés ; frontières actuelles des pays, pour se repérer."

INSTRUMENTS = tableau(["Instrument", "À quoi sert-il ?"], [
    ["la boussole", "indiquer le nord, garder le cap"],
    ["l'astrolabe, le quadrant", "mesurer la hauteur du Soleil ou de l'étoile Polaire : trouver la latitude"],
    ["la carte marine (portulan)", "voir les côtes, les ports, les directions"],
    ["le sablier", "mesurer le temps passé, estimer la distance parcourue"]],
    couleur=BRUN, largeurs=[1, 2], label="Tableau : les instruments de navigation et leur usage")

VOYAGES = etapes([("1492", "Christophe Colomb (Espagne) arrive aux Antilles"),
                  ("1498", "Vasco de Gama (Portugal) arrive en Inde"),
                  ("1519-1522", "Magellan puis Elcano : premier tour du monde"),
                  ("1534", "Jacques Cartier (France) arrive au Canada")],
                 sens="v", couleur=BRUN, label="Frise des quatre grands voyages : 1492, 1498, 1519-1522, 1534")

ECHANGES = tableau(["De l'Amérique vers l'Europe", "De l'Europe vers l'Amérique"], [
    ["le maïs, la pomme de terre", "le cheval, la vache"],
    ["la tomate, le cacao", "le blé"],
    ["l'or et l'argent des mines", "des maladies, comme la variole"]],
    couleur=BRUN, largeurs=[1, 1], label="Tableau des échanges entre l'Amérique et l'Europe après 1492")

COLONIES = tableau(["Pays", "Colonie", "Ce qu'on y exploite"], [
    ["Espagne", "Mexique, Pérou", "mines d'argent"],
    ["Portugal", "Brésil", "canne à sucre"],
    ["France", "Québec (1608)", "fourrures"],
    ["Angleterre", "Virginie (1607)", "terres à cultiver"]],
    couleur=BRUN, largeurs=[1, 1.2, 1.2], label="Tableau des premiers empires coloniaux : pays, colonie, richesse exploitée")

LECONS = {
    "epices": {
        "competence": "Les raisons des explorations : connaître le monde connu des Européens vers 1450 ; expliquer la recherche des épices et d'une route maritime vers l'Asie ; citer d'autres raisons (or, religion, gloire, savoir).",
        "visuels": [
            {"type": "schema", "titre": "Le monde connu des Européens vers 1450"},
            {"type": "carte", "titre": "La route des épices vers 1450",
             "legende": "Les épices viennent d'Asie et passent par de nombreux marchands avant d'arriver en Europe. " + SIMPLIFIE,
             "spec": {"titre": "La route des épices vers 1450", "largeur": 380, "cible_mm": 70, "projection": "equirect", "resolution": "110m",
                      "etendue": [[-22, -14], [146, 58]],
                      "lignes": [{"coords": [[124, -2], [100, 4], [76, 10], [57, 22], [44, 13], [35, 28], [29, 41], [12.3, 45.4]],
                                  "couleur": OR, "fleches": True, "pointille": True}],
                      "points": [
                          {"lonlat": [127.5, 0.8], "nom": "îles aux\népices", "style": "etoile", "couleur": OR, "pos": "n"},
                          {"lonlat": [75.8, 11.25], "nom": "Calicut (Inde)", "pos": "s"},
                          {"lonlat": [28.98, 41.01], "nom": "Constantinople", "pos": "n", "couleur": ROUGE},
                          {"lonlat": [12.33, 45.44], "nom": "Venise", "pos": "w"},
                          {"lonlat": [-9.14, 38.72], "nom": "Lisbonne", "style": "capitale", "pos": "e"}],
                      "textes": [{"lonlat": [70, 0], "texte": "océan Indien"}, {"lonlat": [18, 8], "texte": "AFRIQUE", "style": "region"},
                                 {"lonlat": [90, 45], "texte": "ASIE", "style": "region"}, {"lonlat": [15, 52], "texte": "EUROPE", "style": "region"}]}},
        ],
    },
    "techniques": {
        "competence": "Les progrès techniques qui ont permis aux Européens de s'aventurer vers de nouveaux territoires : la caravelle et ses voiles, la boussole, l'astrolabe, les cartes marines.",
        "visuels": [
            {"type": "schema", "titre": "Une caravelle"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Les instruments du pilote", "svg": INSTRUMENTS,
             "legende": "Beaucoup de ces savoirs, comme l'astrolabe, ont été transmis par les savants du monde arabe."},
        ],
    },
    "voyages": {
        "competence": "Les grands voyages d'exploration (Colomb 1492, Vasco de Gama 1498, Magellan et Elcano 1519-1522, Cartier 1534) : les situer dans le temps et dans l'espace.",
        "visuels": [
            {"type": "svg", "etiquette": "Frise", "titre": "Quatre voyages, quatre dates", "svg": VOYAGES,
             "legende": "L'Amérique était habitée : on parle de l'arrivée des Européens en Amérique."},
        ],
    },
    "rencontres": {
        "competence": "La rencontre avec les peuples d'Amérique et la conquête : connaître des peuples d'Amérique (Aztèques, Incas, Iroquoiens), les conquistadors, le rôle des maladies, les échanges entre les deux continents.",
        "visuels": [
            {"type": "schema", "titre": "Trois peuples d'Amérique vers 1500"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Ce qui traverse l'océan", "svg": ECHANGES,
             "legende": "Les échanges vont dans les deux sens ; la variole fait s'effondrer la population amérindienne."},
        ],
    },
    "empires": {
        "competence": "La constitution des premiers empires coloniaux en Amérique : le partage de Tordesillas (1494), les colonies de l'Espagne, du Portugal, de la France et de l'Angleterre, l'exploitation des colonies.",
        "visuels": [
            {"type": "svg", "etiquette": "Tableau", "titre": "Les premiers empires coloniaux", "svg": COLONIES,
             "legende": "Dans les mines et les plantations, les colons font travailler de force des Amérindiens, puis des Africains réduits en esclavage."},
        ],
    },
}
