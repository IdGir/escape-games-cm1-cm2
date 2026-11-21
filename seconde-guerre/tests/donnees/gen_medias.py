# -*- coding: utf-8 -*-
"""Complète les prompts de immersifs/seconde-guerre/medias.csv (5 décors, 5 vidéos, 5 portraits) après une migration.
Lancer depuis la racine du dépôt : python seconde-guerre/tests/donnees/gen_medias.py   (puis prompts-flow.py seconde-guerre)
SUJET TRÈS SENSIBLE : aucun uniforme allemand, aucun symbole nazi, aucun combat, aucune image de camp ; personnages inventés."""
import csv, io, json

P = "immersifs/seconde-guerre/medias.csv"
STYLE = ("Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, "
         "couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin.")
NEG = ("texte lisible, écriture lisible, logo, filigrane, mains déformées, visage déformé, personne réelle, uniforme allemand, croix gammée, symbole nazi, "
       "arme pointée, blessure, sang, cadavre, combat, explosion, camp, barbelés, caricature, style dessin animé")
DESC = {1: "Une salle de classe de village de 1938, pupitres en bois alignés, poêle en fonte, grande carte de l'Europe au mur (sans nom lisible), tableau noir avec une frise à la craie effacée, bureau du maître avec un journal plié et un encrier, fenêtres sur des collines boisées.",
        2: "Le quai d'une petite gare de campagne en juin 1940, valises, paniers et bicyclettes entassés, grande horloge de quai, bureau du chef de gare avec une carte de France au mur barrée d'une ligne rouge et un poste de radio en bois sur le guichet, lumière d'été voilée ; silhouettes lointaines de dos.",
        3: "Une petite épicerie de village en hiver 1942, étagères presque vides avec quelques bocaux, comptoir en bois avec une balance à plateaux et un cahier de comptes, petits tickets de papier dans une boîte en fer, une feuille officielle sous un poids, un cahier d'écolière sur une caisse, givre sur la vitrine.",
        4: "Une cabane de bûcherons cachée sous les grands arbres de la forêt du Morvan au printemps 1944, table rustique avec une valise ouverte contenant un poste émetteur et un casque, un petit carnet, une carte roulée, une machine à écrire et des feuilles tapées, une lampe tempête allumée.",
        5: "La place d'un village du Morvan le 8 mai 1945, mairie pavoisée de drapeaux tricolores, grand calendrier affiché près de la porte, carte de France dessinée à la main épinglée sur un panneau, caisse de drapeaux au pied d'un mât, table avec un vieux poste de radio en bois à cadran ; silhouettes lointaines de dos, joie retenue."}
VID = {1: "Lent travelling avant vers la carte de l'Europe ; la poussière danse dans un rayon de soleil, la flamme du poêle vacille, une page du journal se soulève doucement.",
       2: "Lent travelling latéral le long du quai ; de la vapeur passe au loin, l'aiguille de l'horloge avance, la lumière du poste de radio clignote faiblement.",
       3: "Lent travelling avant vers le comptoir ; la clochette de la porte oscille, le givre scintille sur la vitrine, la lumière froide d'hiver se déplace sur les étagères.",
       4: "Lent travelling avant vers le poste émetteur ; la flamme de la lampe tempête vacille, les feuilles des arbres bougent derrière la fenêtre, un voyant du poste s'allume doucement. Calme, aucun combat.",
       5: "Lent travelling avant vers le vieux poste de radio ; les drapeaux tricolores ondulent dans la brise, des pétales de fleurs passent dans l'air, la lumière de printemps s'éclaircit."}
PORT = {"bastien": "homme d'une quarantaine d'années, cheveux bruns courts, petites lunettes rondes, blouse grise d'instituteur de 1938 sur une chemise blanche, expression calme et soucieuse, regard vers l'objectif",
        "paul": "homme d'une cinquantaine d'années, cheveux noirs grisonnants, moustache et barbe courte, veste bleu foncé et casquette de cheminot de 1940, expression chaleureuse et fatiguée, regard vers l'objectif",
        "madeleine": "femme d'une quarantaine d'années, cheveux châtains courts ondulés, robe sombre et tablier d'épicière, gilet de laine bordeaux, expression discrète et courageuse, regard vers l'objectif",
        "marc": "jeune homme d'une vingtaine d'années, cheveux blonds en bataille, chemise à carreaux et veste de toile kaki, sans arme, casque d'écoute autour du cou, expression attentive et prudente, regard vers l'objectif",
        "lucie": "jeune fille de dix-sept ans, cheveux bruns longs attachés, béret et manteau bleu marine des années 1940, écharpe tricotée, expression vive et émue, regard vers l'objectif"}

rows = list(csv.reader(open(P, encoding="utf-8"), delimiter=";"))
I = {k: i for i, k in enumerate(rows[0])}
nar = json.load(open("vingt-mille-lieues/outils/immersif/narration/seconde-guerre.json", encoding="utf-8"))["enigmes"]
dia = json.load(open("seconde-guerre/assets/data/dialogues.json", encoding="utf-8"))
for r in rows[1:]:
    rid = r[I["id"]]
    if rid.startswith("decor-"):
        n = int(r[I["escale"]])
        objs = "; ".join(f"{nar[f'e{n}-{k}']['objet']} ({nar[f'e{n}-{k}']['description'].rstrip('.')})" for k in range(1, 5))
        r[I["prompt_fr"]] = (f"Décor en plan large, 16:9 : {dia['salles'][n - 1]['lieu']}. {DESC[n]} Composition lisible avec 4 objets distincts bien séparés : {objs}. "
                             f"Espace sombre et dégagé en bas de l'image pour la plaque de dialogue. {STYLE} Aucun texte lisible, aucun personnage au premier plan, aucun uniforme, aucun symbole politique.")
    elif rid.startswith("video-transition-e"):
        n = int(rid[-1])
        r[I["prompt_fr"]] = f"Image de départ : le décor de la fréquence {n}. {VID[n]} Caméra stable, aucun personnage qui parle, aucun texte lisible. 8 secondes."
    elif rid.startswith("portrait-"):
        k = rid.split("-", 1)[1]
        pe = dia["personnages"][k]
        r[I["prompt_fr"]] = f"Portrait de référence, plan taille, cadrage vertical, fond flou. {pe['nom']} : {pe['role']}. {PORT[k]}. Personnage inventé, visage non réel. {STYLE}"
    r[I["negatif"]] = NEG
buf = io.StringIO()
csv.writer(buf, delimiter=";", lineterminator="\n").writerows(rows)
open(P, "w", encoding="utf-8").write(buf.getvalue())
print("medias.csv : prompts complétés (5 décors, 5 vidéos, 5 portraits)")
