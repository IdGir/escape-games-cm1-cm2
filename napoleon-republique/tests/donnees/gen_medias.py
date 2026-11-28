# -*- coding: utf-8 -*-
"""Complète les prompts de immersifs/napoleon-republique/medias.csv (5 décors, 5 vidéos, 5 portraits) après une migration.
Lancer depuis la racine du dépôt : python napoleon-republique/tests/donnees/gen_medias.py   (puis prompts-flow.py napoleon-republique)
Aucune personne réelle (jamais Napoléon, Joséphine ni le pape en personne), aucun combat, aucune blessure ; personnages inventés.
Le dôme des Invalides et la salle des mariages sont des lieux réels d'aujourd'hui : une photo Wikimedia Commons du dôme peut remplacer le décor 4."""
import csv, io, json

P = "immersifs/napoleon-republique/medias.csv"
STYLE = ("Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée, couleurs chaudes et dorées, "
         "lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin.")
NEG = ("texte lisible, écriture lisible, logo, filigrane, mains déformées, visage déformé, personne réelle, portrait de Napoléon, sosie de Napoléon, "
       "bicorne au premier plan, arme pointée, blessure, sang, cadavre, combat, explosion, caricature, style dessin animé")
DESC = {1: "Une antichambre du palais des Tuileries en 1800, boiseries claires et dorures discrètes, grandes fenêtres sur une cour, cartes anciennes d'Italie et d'Égypte épinglées au mur (sans nom lisible), pupitre avec un carnet de cuir, giberne de soldat sur une chaise, bureau couvert de lettres cachetées et d'une plume.",
        2: "La nef de la cathédrale Notre-Dame de Paris le 2 décembre 1804, décorée de tentures rouges et or, tribunes garnies d'invités vus de loin et de dos, autel illuminé de cierges, au premier plan la table de travail d'une brodeuse avec du fil d'or, un registre ouvert, un carton de motifs d'abeilles dorées et un tapis rouge déroulé vers l'autel.",
        3: "L'intérieur d'une tente de toile de la Grande Armée la nuit, éclairée par une lanterne, table pliante avec une grande carte de l'Europe tracée à la main (sans nom lisible), malle de bois fermée par un cadenas à rouleaux, gourde et tonnelet de cantinière, ouverture de la tente sur un feu de camp au loin ; calme, aucun combat.",
        4: "Sous le dôme des Invalides à Paris aujourd'hui, grande coupole dorée et galerie circulaire autour de la crypte vue de haut, au premier plan une salle d'exposition en préparation avec une vitrine éclairée, un chariot de petits cartels vierges, deux grands panneaux vides et une boîte de fiches cartonnées ; lumière de musée.",
        5: "Une salle des mariages lumineuse d'une mairie de Bourgogne aujourd'hui, buste de Marianne sur un socle, drapeau tricolore, table avec une écharpe tricolore pliée, un vieux coffre de voyage en bois et cuir, un plan de la place dessiné à la main, un placard ouvert plein d'objets anciens, urne de vote transparente rangée dans un coin ; aucune inscription lisible."}
VID = {1: "Lent travelling avant vers les cartes épinglées ; le soleil d'hiver traverse la fenêtre, une lettre se soulève doucement, la poussière danse dans la lumière.",
       2: "Lent travelling avant le long de la nef vers l'autel ; les flammes des cierges vacillent, les tentures ondulent légèrement, le fil d'or scintille sur la table.",
       3: "Lent travelling avant vers la carte de l'Europe ; la flamme de la lanterne vacille, la toile de la tente bouge dans le vent, le feu de camp crépite au loin. Calme, aucun combat.",
       4: "Lente montée de la caméra vers la coupole dorée ; la lumière glisse sur l'or, les reflets bougent dans la vitrine.",
       5: "Lent travelling avant vers le coffre de voyage ; le drapeau tricolore ondule doucement à la fenêtre ouverte, la lumière de printemps s'éclaircit."}
PORT = {"antoine": "homme d'une trentaine d'années, cheveux bruns courts et favoris, uniforme bleu à revers blancs de grenadier du début du XIXe siècle, sans arme, expression franche et fière, regard vers l'objectif",
        "rose": "jeune femme d'une vingtaine d'années, cheveux châtains relevés en chignon, robe simple de 1804 couleur bordeaux et tablier de travail, aiguille et fil d'or à la main, expression attentive et émerveillée, regard vers l'objectif",
        "jeanne": "femme d'une quarantaine d'années, cheveux bruns courts sous un chapeau à cocarde, veste de cantinière du début du XIXe siècle vert foncé, tonnelet en bandoulière, expression chaleureuse et grave, regard vers l'objectif",
        "hugo": "homme d'une cinquantaine d'années, cheveux noirs courts, lunettes, costume sombre et badge de musée, gants blancs de conservateur, expression posée et bienveillante, regard vers l'objectif",
        "ines": "femme d'une quarantaine d'années, longs cheveux noirs, tailleur bleu marine, écharpe tricolore de maire en bandoulière, expression accueillante, regard vers l'objectif"}

rows = list(csv.reader(open(P, encoding="utf-8"), delimiter=";"))
I = {k: i for i, k in enumerate(rows[0])}
nar = json.load(open("vingt-mille-lieues/outils/immersif/narration/napoleon-republique.json", encoding="utf-8"))["enigmes"]
dia = json.load(open("napoleon-republique/assets/data/dialogues.json", encoding="utf-8"))
for r in rows[1:]:
    rid = r[I["id"]]
    if rid.startswith("decor-"):
        n = int(r[I["escale"]])
        objs = "; ".join(f"{nar[f'e{n}-{k}']['objet']} ({nar[f'e{n}-{k}']['description'].rstrip('.')})" for k in range(1, 5))
        r[I["prompt_fr"]] = (f"Décor en plan large, 16:9 : {dia['salles'][n - 1]['lieu']}. {DESC[n]} Composition lisible avec 4 objets distincts bien séparés : {objs}. "
                             f"Espace sombre et dégagé en bas de l'image pour la plaque de dialogue. {STYLE} Aucun texte lisible, aucun personnage au premier plan, aucune personne réelle.")
    elif rid.startswith("video-transition-e"):
        n = int(rid[-1])
        r[I["prompt_fr"]] = f"Image de départ : le décor de la salle {n}. {VID[n]} Caméra stable, aucun personnage qui parle, aucun texte lisible. 8 secondes."
    elif rid.startswith("portrait-"):
        k = rid.split("-", 1)[1]
        pe = dia["personnages"][k]
        r[I["prompt_fr"]] = f"Portrait de référence, plan taille, cadrage vertical, fond flou. {pe['nom']} : {pe['role']}. {PORT[k]}. Personnage inventé, visage non réel. {STYLE}"
    r[I["negatif"]] = NEG
buf = io.StringIO()
csv.writer(buf, delimiter=";", lineterminator="\n").writerows(rows)
open(P, "w", encoding="utf-8").write(buf.getvalue())
print("medias.csv : prompts complétés (5 décors, 5 vidéos, 5 portraits)")
