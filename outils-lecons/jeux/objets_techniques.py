# -*- coding: utf-8 -*-
"""Leçons imprimables — L'Atelier de l'inventeur (objets-techniques)."""
import math
from graphiques import ouvrir, texte, taille, tableau, etapes

JEU = {
    "titre": "L'Atelier de l'inventeur",
    "matiere": "Sciences et technologie",
    "theme": "Les objets techniques : fonctionnement et constitution",
    "couleur": "#123f4f", "accent": "#c0501d",
    "couleur_pale": "#e8f1f3", "accent_pale": "#fcefe7",
}
C1, C2, VERT, OR = "#1e5a6e", "#c0501d", "#3d7a3a", "#b8860b"


def bete_a_cornes():
    W, H = 360, 230
    fs = taille(W, 66)
    s = [ouvrir(W, H, "La bête à cornes de la lampe torche")]
    # deux « cornes »
    s.append(f'<ellipse cx="80" cy="46" rx="72" ry="28" fill="#fff" stroke="{C1}" stroke-width="1.6"/>')
    s.append(f'<ellipse cx="280" cy="46" rx="72" ry="28" fill="#fff" stroke="{C1}" stroke-width="1.6"/>')
    s.append(texte(80, 40, "À qui rend-il\nservice ?", fs * 0.75, fill="#5b6470", italique=True))
    s.append(texte(80, 66, "à l'utilisateur", fs * 0.9, fill=C1, poids=700))
    s.append(texte(280, 40, "Sur quoi\nagit-il ?", fs * 0.75, fill="#5b6470", italique=True))
    s.append(texte(280, 66, "sur l'obscurité", fs * 0.9, fill=C1, poids=700))
    s.append(f'<ellipse cx="180" cy="128" rx="70" ry="26" fill="{C1}"/>')
    s.append(texte(180, 133, "LA LAMPE TORCHE", fs * 0.95, fill="#fff", poids=800))
    s.append(f'<path d="M110,62 Q150,110 180,102" fill="none" stroke="{C1}" stroke-width="1.6"/>')
    s.append(f'<path d="M250,62 Q210,110 180,102" fill="none" stroke="{C1}" stroke-width="1.6"/>')
    s.append(f'<path d="M180,154 L180,178" stroke="{C2}" stroke-width="2"/>')
    s.append(f'<rect x="40" y="180" width="280" height="44" rx="8" fill="#fff" stroke="{C2}" stroke-width="1.8"/>')
    s.append(texte(180, 196, "Dans quel but ? (fonction d'usage)", fs * 0.75, fill="#5b6470", italique=True))
    s.append(texte(180, 216, "éclairer loin d'une prise", fs, fill=C2, poids=800))
    s.append("</svg>")
    return "".join(s)


def engrenage(cx, cy, r, dents, couleur):
    pts = []
    for k in range(dents * 2):
        a = math.pi * k / dents
        rr = r if k % 2 == 0 else r * 0.82
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return (f'<polygon points="{" ".join(pts)}" fill="{couleur}" stroke="#333" stroke-width="0.8"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.18:.1f}" fill="#fff" stroke="#333" stroke-width="0.8"/>')


def transmissions():
    W, H = 360, 170
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Trois systèmes de transmission du mouvement")]
    s.append('<defs><marker id="rt" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#c0501d"/></marker></defs>')
    # engrenage
    s.append(engrenage(40, 70, 26, 10, "#9fc3cf"))
    s.append(engrenage(84, 70, 20, 8, "#f0c49f"))
    s.append(f'<path d="M22,36 A30,30 0 0 1 58,36" fill="none" stroke="{C2}" stroke-width="1.5" marker-end="url(#rt)"/>')
    s.append(f'<path d="M100,98 A24,24 0 0 1 68,98" fill="none" stroke="{C2}" stroke-width="1.5" marker-end="url(#rt)"/>')
    s.append(texte(62, 130, "Engrenage", fs, fill=C1, poids=800))
    s.append(texte(62, 146, "roues dentées en contact :\nsens contraire", fs * 0.72))
    # poulies et courroie
    s.append(f'<line x1="150" y1="{70-22}" x2="210" y2="{70-14}" stroke="#333" stroke-width="2.4"/>')
    s.append(f'<line x1="150" y1="{70+22}" x2="210" y2="{70+14}" stroke="#333" stroke-width="2.4"/>')
    s.append(f'<circle cx="150" cy="70" r="22" fill="#9fc3cf" stroke="#333"/><circle cx="210" cy="70" r="14" fill="#f0c49f" stroke="#333"/>')
    s.append(texte(180, 130, "Poulies et courroie", fs, fill=C1, poids=800))
    s.append(texte(180, 146, "roues éloignées :\nmême sens", fs * 0.72))
    # levier
    s.append(f'<polygon points="300,92 290,110 310,110" fill="{OR}" stroke="#333"/>')
    s.append(f'<line x1="252" y1="100" x2="352" y2="80" stroke="#6b4a2b" stroke-width="5" stroke-linecap="round"/>')
    s.append(f'<line x1="258" y1="70" x2="258" y2="92" stroke="{C2}" stroke-width="1.5" marker-end="url(#rt)"/>')
    s.append(f'<line x1="346" y1="74" x2="346" y2="54" stroke="{C2}" stroke-width="1.5" marker-end="url(#rt)"/>')
    s.append(texte(300, 130, "Levier", fs, fill=C1, poids=800))
    s.append(texte(300, 146, "barre qui pivote\nsur un point d'appui", fs * 0.72))
    s.append("</svg>")
    return "".join(s)


LECONS = {
    "besoin-fonction": {
        "competence": "Décrire le fonctionnement d'un objet technique : sa fonction d'usage (à quoi il sert).",
        "visuels": [
            {"type": "schema", "titre": "Du besoin à l'objet"},
            {"type": "svg", "titre": "La « bête à cornes » d'un objet", "svg": bete_a_cornes(),
             "legende": "Trois questions pour décrire la fonction d'usage d'un objet."},
            {"type": "svg", "titre": "Les objets évoluent : s'éclairer",
             "svg": etapes([("Bougie", "depuis\nl'Antiquité", OR), ("Lampe à pétrole", "XIXe siècle", "#8e6b3a"),
                            ("Ampoule", "électrique\n(1879)", C1), ("Lampe à LED", "XXIe siècle", VERT)], sens="h", numeros=False),
             "legende": "Le besoin reste le même, les solutions changent."},
        ],
    },
    "constituants": {
        "competence": "Décrire la constitution d'un objet technique : ses pièces (schéma).",
        "visuels": [
            {"type": "schema", "titre": "Les constituants d'une lampe torche"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Chaque pièce a une fonction technique",
             "svg": tableau(["Constituant", "Fonction technique"], [
                 ["pile", "fournir l'énergie électrique"],
                 ["interrupteur", "ouvrir ou fermer le circuit"],
                 ["ampoule (ou LED)", "produire la lumière"],
                 ["réflecteur, lentille", "renvoyer la lumière\nvers l'avant"],
                 ["boîtier", "contenir et protéger\nles pièces"],
             ], couleur=C1, largeurs=[1, 1.4])},
        ],
    },
    "materiaux": {
        "competence": "Décrire la constitution d'un objet technique : les matériaux.",
        "visuels": [
            {"type": "schema", "titre": "Les familles de matériaux"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Choisir un matériau pour sa propriété",
             "svg": tableau(["Matériau", "Propriété utile", "Exemple"], [
                 ["bois", "conduit mal la chaleur", "poignée de casserole"],
                 ["cuivre (métal)", "conduit le courant", "fil électrique"],
                 ["plastique", "isolant, léger", "gaine d'un fil"],
                 ["verre", "transparent", "vitre, lentille"],
                 ["acier (métal)", "dur, résistant", "outil, clou"],
             ], couleur=C1, largeurs=[1, 1.25, 1.15])},
        ],
    },
    "energie-mouvement": {
        "competence": "Décrire le fonctionnement d'un objet technique : la chaîne d'énergie, la transmission du mouvement.",
        "visuels": [
            {"type": "schema", "titre": "La chaîne d'énergie"},
            {"type": "svg", "titre": "La chaîne d'énergie du vélo",
             "svg": etapes([("Source", "muscles\ndes jambes", C2), ("Commande", "pédalier", OR),
                            ("Transmission", "chaîne et\npignon", C1), ("Effet utile", "la roue tourne,\nle vélo avance", VERT)], sens="h", numeros=False)},
            {"type": "svg", "titre": "Transmettre un mouvement", "svg": transmissions()},
        ],
    },
    "notice-montage": {
        "competence": "Décrire la constitution d'un objet technique : le montage, la fabrication.",
        "visuels": [
            {"type": "schema", "titre": "Les étapes d'un montage"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Comparer deux solutions : l'ouvre-boîte",
             "svg": tableau(["", "à manivelle", "électrique"], [
                 ["Énergie", "muscles", "électricité"],
                 ["Pile ou prise", "non", "oui"],
                 ["Effort", "plus important", "faible"],
                 ["Fonction d'usage", "ouvrir une boîte", "ouvrir une boîte"],
             ], couleur=C1, largeurs=[1.1, 1, 1]),
             "legende": "Même besoin, même fonction d'usage : deux solutions techniques différentes."},
        ],
    },
}
