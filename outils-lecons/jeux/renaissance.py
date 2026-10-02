# -*- coding: utf-8 -*-
"""Leçons imprimables — L'Atelier de Léonard à Amboise (renaissance)."""
from graphiques import etapes, tableau

JEU = {
    "titre": "L'Atelier de Léonard à Amboise",
    "matiere": "Histoire",
    "theme": "La Renaissance : François Ier, protecteur des arts et des lettres, et Léonard de Vinci",
    "couleur": "#8a4b1e", "accent": "#b8860b",
    "couleur_pale": "#f6ebe0", "accent_pale": "#fbf4dd",
}

SIENNE, OR, VERT, BLEU, GRIS = "#8a4b1e", "#b8860b", "#2f5d5a", "#2f4f8a", "#5e5e5e"

LEONARD = etapes([
    ("Peintre", "portraits : la Joconde", SIENNE),
    ("Dessinateur et savant", "l'Homme de Vitruve, l'anatomie", OR),
    ("Observateur", "oiseaux, eau, plantes", VERT),
    ("Ingénieur", "machines, canaux, palais (projets)", BLEU),
], label="Les talents de Léonard de Vinci")

DEUX_CHATEAUX = tableau(["", "Château fort", "Château Renaissance"], [
    ["Rôle", "se défendre", "vivre et éblouir"],
    ["Fenêtres", "étroites, meurtrières", "grandes, à meneaux"],
    ["Plan", "selon le terrain", "symétrique"],
    ["Décor", "peu de décor", "sculptures, salamandres"],
    ["Exemple", "Guédelon (jeu n°02)", "Chambord (1519)"],
], label="Du château fort au château de la Renaissance", largeurs=[1, 1.4, 1.4], couleur=SIENNE)

LECONS = {
    "renaissance-humanisme": {
        "competence": "François Ier, un protecteur des arts et des lettres à la Renaissance (la Renaissance venue d'Italie, l'humanisme, l'imprimerie).",
        "visuels": [
            {"type": "carte", "titre": "De l'Italie à la Loire",
             "legende": "La Renaissance naît à Florence ; l'imprimerie est mise au point à Mayence ; elle gagne la France, jusqu'aux châteaux de la Loire. Frontières actuelles, pour se repérer.",
             "spec": {"titre": "De l'Italie à la Loire", "largeur": 360, "cible_mm": 66,
                      "etendue": [[-3.0, 40.5], [15.5, 51.5]], "pays_mis_en_avant": ["France", "Italy"],
                      "fleuves": ["Loire", "Seine", "Rhône", "Rhne", "Pô", "Po", "Rhin", "Rhein"],
                      "points": [
                          {"lonlat": [11.25, 43.77], "nom": "Florence", "style": "etoile", "couleur": SIENNE, "pos": "e"},
                          {"lonlat": [9.19, 45.46], "nom": "Milan (Marignan, 1515)", "pos": "e"},
                          {"lonlat": [12.48, 41.90], "nom": "Rome", "pos": "e"},
                          {"lonlat": [8.27, 50.00], "nom": "Mayence (Gutenberg)", "pos": "e"},
                          {"lonlat": [0.98, 47.41], "nom": "Amboise", "style": "etoile", "couleur": OR, "pos": "w"},
                          {"lonlat": [2.35, 48.86], "nom": "Paris", "style": "capitale", "pos": "n"}],
                      "echelle_km": 300}},
        ],
    },
    "francois-mecene": {
        "competence": "François Ier, un protecteur des arts et des lettres à la Renaissance (le roi mécène : les arts, les lettres, la langue française).",
        "visuels": [{"type": "schema"}],
    },
    "leonard-de-vinci": {
        "competence": "François Ier, un protecteur des arts et des lettres à la Renaissance, grâce à l'aide de Léonard de Vinci (peintre, ingénieur, observateur).",
        "visuels": [
            {"type": "svg", "etiquette": "Schéma", "titre": "Les talents de Léonard", "svg": LEONARD,
             "legende": "Ses machines sont restées des dessins : les maquettes que l'on voit aujourd'hui ont été construites récemment."},
        ],
    },
    "chateaux-renaissance": {
        "competence": "François Ier, un protecteur des arts et des lettres à la Renaissance (les châteaux : Amboise, Blois, Chambord ; la salamandre).",
        "visuels": [
            {"type": "carte", "titre": "Les châteaux du roi sur la Loire",
             "legende": "Amboise (et le Clos Lucé, tout près), Blois et Chambord se trouvent près de la Loire, à moins de 60 km les uns des autres.",
             "spec": {"titre": "Les châteaux du roi sur la Loire", "largeur": 360, "cible_mm": 66,
                      "etendue": [[0.35, 47.15], [2.15, 48.05]], "fleuves": ["Loire", "Cher", "Indre", "Loir"],
                      "points": [
                          {"lonlat": [0.983, 47.413], "nom": "Amboise", "style": "etoile", "couleur": OR, "pos": "s"},
                          {"lonlat": [1.331, 47.586], "nom": "Blois", "pos": "w"},
                          {"lonlat": [1.517, 47.616], "nom": "Chambord", "style": "etoile", "couleur": SIENNE, "pos": "e"},
                          {"lonlat": [0.689, 47.394], "nom": "Tours", "pos": "w"},
                          {"lonlat": [1.909, 47.902], "nom": "Orléans", "pos": "e"}],
                      "echelle_km": 20}},
            {"type": "svg", "etiquette": "Tableau", "titre": "Deux châteaux, deux époques", "svg": DEUX_CHATEAUX},
        ],
    },
    "art-renaissance": {
        "competence": "François Ier, un protecteur des arts et des lettres à la Renaissance, grâce à l'aide de Léonard de Vinci (l'art : perspective, proportions, portrait).",
        "visuels": [{"type": "schema"}],
    },
}
