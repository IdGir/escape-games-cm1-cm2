# -*- coding: utf-8 -*-
"""Complète les prompts de immersifs/grande-guerre/medias.csv (5 décors, 5 vidéos, 5 portraits) après une migration.
Lancer depuis la racine du dépôt : python grande-guerre/tests/donnees/gen_medias.py   (puis prompts-flow.py grande-guerre)
SUJET SENSIBLE : aucun blessé, aucun combat, aucune explosion ; personnages inventés."""
import csv, io, json

P = "immersifs/grande-guerre/medias.csv"
STYLE = ("Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, "
         "couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin.")
NEG = ("texte lisible, écriture lisible, logo, filigrane, mains déformées, visage déformé, personne réelle, blessure, sang, cadavre, combat, explosion, "
       "arme pointée, drapeau nazi, caricature, style dessin animé")
DESC = {1: "Une place de village de Bourgogne un matin d'été, l'église et son clocher, la mairie avec une grande affiche blanche sur sa porte (sans texte lisible), un grand tilleul, une fontaine de pierre avec des valises posées à son pied, quelques silhouettes lointaines vues de dos.",
        2: "Un abri étroit creusé sous la terre et étayé de planches, calme et propre, une bougie dans une boîte de conserve, une couverture pliée, une boîte de masque à gaz fermée, des lettres et un colis ouvert sur une caisse en bois, la lumière du jour qui tombe d'une ouverture en haut.",
        3: "Un grand atelier d'usine de 1917 sous une verrière lumineuse, des rangées de machines-outils, des caisses de douilles d'obus vides bien rangées, un établi avec un carnet et des photos épinglées au mur, un tableau noir à deux colonnes.",
        4: "Une salle de classe de village transformée en hôpital, pupitres poussés contre le mur, lits blancs vides et bien faits, un tableau noir, des étiquettes épinglées au mur, un registre relié sur une table, une fenêtre ouverte sur le clocher.",
        5: "La place du village en novembre, un monument aux morts neuf en pierre claire surmonté d'une statue de soldat, une liste de noms gravés illisibles, une gerbe de fleurs bleues, blanches et rouges à son pied, une table avec un plan roulé, un registre et une enveloppe fermée par un petit cadenas ; silhouettes lointaines de dos, en silence."}
VID = {1: "Lent travelling avant vers la fontaine et l'affiche de la mairie ; les feuilles du tilleul bougent dans la brise, un pigeon s'envole, la lumière du matin glisse sur les pavés.",
       2: "Lent travelling avant vers la caisse aux lettres ; la flamme de la bougie vacille, de fines gouttes de pluie tombent de l'ouverture, la poussière danse dans la lumière. Calme, aucun combat.",
       3: "Lent travelling latéral le long des machines ; les poulies tournent doucement, la lumière de la verrière se déplace, un peu de vapeur s'élève.",
       4: "Lent travelling avant vers la fenêtre ouverte ; les rideaux bougent, la lumière d'automne entre dans la classe, le clocher se dessine au loin.",
       5: "Lent travelling avant vers le monument ; quelques feuilles mortes tombent, les rubans de la gerbe bougent dans le vent, la lumière grise de novembre s'éclaircit doucement."}
PORT = {"jeanne": "fillette d'environ dix ans en 1914, cheveux châtains tressés, robe bleu foncé et tablier d'écolière, expression grave et curieuse, regard vers l'objectif",
        "louis": "jeune homme d'une vingtaine d'années, cheveux bruns courts, uniforme bleu horizon de soldat français de 1916 propre, sans arme, calot sur la tête, sourire doux et fatigué, regard vers l'objectif",
        "marcelle": "jeune femme d'une vingtaine d'années, cheveux noirs relevés sous un foulard, blouse d'ouvrière brune de 1917, mains propres, expression fière et souriante, regard vers l'objectif",
        "odette": "femme d'une trentaine d'années, cheveux blond foncé courts sous une coiffe blanche d'infirmière, tablier blanc à petite croix rouge, petites lunettes rondes, expression douce et calme, regard vers l'objectif",
        "emile": "homme d'une soixantaine d'années, cheveux et barbe gris, lunettes, costume sombre de 1922 et écharpe tricolore de maire, expression grave et bienveillante, regard vers l'objectif"}

rows = list(csv.reader(open(P, encoding="utf-8"), delimiter=";"))
I = {k: i for i, k in enumerate(rows[0])}
nar = json.load(open("vingt-mille-lieues/outils/immersif/narration/grande-guerre.json", encoding="utf-8"))["enigmes"]
dia = json.load(open("grande-guerre/assets/data/dialogues.json", encoding="utf-8"))
for r in rows[1:]:
    rid = r[I["id"]]
    if rid.startswith("decor-"):
        n = int(r[I["escale"]])
        objs = "; ".join(f"{nar[f'e{n}-{k}']['objet']} ({nar[f'e{n}-{k}']['description'].rstrip('.')})" for k in range(1, 5))
        r[I["prompt_fr"]] = (f"Décor en plan large, 16:9 : {dia['salles'][n - 1]['lieu']}. {DESC[n]} Composition lisible avec 4 objets distincts bien séparés : {objs}. "
                             f"Espace sombre et dégagé en bas de l'image pour la plaque de dialogue. {STYLE} Aucun texte lisible, aucun personnage au premier plan, aucun blessé.")
    elif rid.startswith("video-transition-e"):
        n = int(rid[-1])
        r[I["prompt_fr"]] = f"Image de départ : le décor de la lettre {n}. {VID[n]} Caméra stable, aucun personnage qui parle, aucun texte lisible. 8 secondes."
    elif rid.startswith("portrait-"):
        k = rid.split("-", 1)[1]
        pe = dia["personnages"][k]
        r[I["prompt_fr"]] = f"Portrait de référence, plan taille, cadrage vertical, fond flou. {pe['nom']} : {pe['role']}. {PORT[k]}. Personnage inventé, visage non réel. {STYLE}"
    r[I["negatif"]] = NEG
buf = io.StringIO()
csv.writer(buf, delimiter=";", lineterminator="\n").writerows(rows)
open(P, "w", encoding="utf-8").write(buf.getvalue())
print("medias.csv : prompts complétés (5 décors, 5 vidéos, 5 portraits)")
