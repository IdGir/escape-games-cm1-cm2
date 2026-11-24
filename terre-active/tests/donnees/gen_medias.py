# -*- coding: utf-8 -*-
"""Complète les prompts de immersifs/terre-active/medias.csv (5 décors, 5 vidéos, 5 portraits) après une migration.
Lancer depuis la racine du dépôt : python terre-active/tests/donnees/gen_medias.py   (puis prompts-flow.py terre-active)
Ton rassurant : aucune catastrophe, aucun blessé, aucune ruine ; station, village et personnages inventés ; les schémas ne sont jamais générés par IA."""
import csv, io, json

P = "immersifs/terre-active/medias.csv"
STYLE = ("Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation "
         "scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin.")
NEG = ("texte lisible, écriture lisible, chiffres lisibles, logo, filigrane, mains déformées, visage déformé, personne réelle, blessé, sang, ruines, panique, "
       "catastrophe, explosion, maison détruite, foule qui fuit, caricature, style dessin animé")
DESC = {1: "Une galerie d'exposition lumineuse au sol de béton ciré, une grande maquette de la Terre coupée en deux montrant des couches orange et jaunes, des panneaux d'exposition tombés au sol, des vitrines de roches volcaniques sombres, une borne à écran, une longue bande verticale suspendue au plafond, une baie vitrée sur un volcan lointain.",
        2: "Une salle des cartes de station scientifique, un grand planisphère au mur sans aucun nom lisible avec des punaises tombées au sol, une table avec une maquette de deux plaques de polystyrène blanc posées sur de la pâte à modeler orange et un petit volcan en carton, des fiches cartonnées éparpillées, un panneau à flèches.",
        3: "Un sentier balisé de cordes sur une ancienne coulée de lave noire, une table d'orientation en pierre, des capteurs gris sur trépied avec un petit écran, une boîte à compartiments avec des échantillons de lave et de cendre, un carnet ouvert sur un rocher, et au loin un cratère d'où monte une fine fumée blanche, ciel bleu.",
        4: "Une salle des sismographes, plusieurs écrans affichant des tracés en zigzag, un vieux sismographe à tambour en laiton, un grand tableau blanc avec un schéma en coupe, des tiroirs d'étiquettes ouverts, un téléphone de bureau avec un voyant, un panneau de consignes à moitié rédigé, lumière douce du matin.",
        5: "Le bureau d'un centre de secours de sapeurs-pompiers, une carte en trois zones de couleur épinglée au mur sans nom lisible, une grande affiche vierge avec des vignettes posées à côté, un poste de radio, des casques rouges rangés sur une étagère, un ordinateur dont l'écran affiche un cadenas, une fenêtre sur un village tropical paisible."}
VID = {1: "Lent travelling avant vers la maquette de la Terre ; les couches de la maquette s'illuminent doucement, la poussière danse dans la lumière de la baie vitrée, un écran clignote.",
       2: "Lent travelling latéral le long du planisphère ; une fiche glisse doucement sur la table, la lumière du matin avance sur la maquette des plaques.",
       3: "Lent travelling avant sur le sentier ; la fine fumée blanche monte du cratère lointain, les herbes bougent dans le vent, le voyant d'un capteur clignote. Calme, aucune éruption violente.",
       4: "Lent travelling avant vers les écrans ; les tracés en zigzag défilent doucement, l'aiguille du vieux sismographe gratte le papier, le voyant du téléphone s'allume.",
       5: "Lent travelling avant vers l'ordinateur ; le cadenas de l'écran s'ouvre doucement, la lumière du matin entre par la fenêtre, le poste de radio s'allume."}
PORT = {"ines": "femme d'une quarantaine d'années, cheveux bruns longs attachés, lunettes fines, gilet bleu marine sur un tee-shirt clair, badge de station sans inscription lisible, expression posée et chaleureuse, regard vers l'objectif",
        "noe": "homme d'une trentaine d'années, cheveux châtain clair courts, chemise verte aux manches retroussées, expression enthousiaste, regard vers l'objectif",
        "maeva": "femme d'une trentaine d'années, cheveux noirs longs, peau mate, veste de terrain orange avec bandes réfléchissantes, casque de sécurité à la main, expression calme et précise, regard vers l'objectif",
        "samuel": "homme d'une cinquantaine d'années, peau noire, barbe courte grisonnante, lunettes, chemise brune, expression méthodique et rassurante, regard vers l'objectif",
        "adele": "femme d'une trentaine d'années, cheveux châtains courts, tenue de sapeur-pompier bleu marine avec bandes rouges, sans écusson lisible, expression énergique et bienveillante, regard vers l'objectif"}

rows = list(csv.reader(open(P, encoding="utf-8"), delimiter=";"))
I = {k: i for i, k in enumerate(rows[0])}
nar = json.load(open("vingt-mille-lieues/outils/immersif/narration/terre-active.json", encoding="utf-8"))["enigmes"]
dia = json.load(open("terre-active/assets/data/dialogues.json", encoding="utf-8"))
for r in rows[1:]:
    rid = r[I["id"]]
    if rid.startswith("decor-"):
        n = int(r[I["escale"]])
        objs = "; ".join(f"{nar[f'e{n}-{k}']['objet']} ({nar[f'e{n}-{k}']['description'].rstrip('.')})" for k in range(1, 5))
        r[I["prompt_fr"]] = (f"Décor en plan large, 16:9 : {dia['salles'][n - 1]['lieu']}. {DESC[n]} Composition lisible avec 4 objets distincts bien séparés : {objs}. "
                             f"Espace sombre et dégagé en bas de l'image pour la plaque de dialogue. {STYLE} Aucun texte lisible, aucun personnage au premier plan.")
    elif rid.startswith("video-transition-e"):
        n = int(rid[-1])
        r[I["prompt_fr"]] = f"Image de départ : le décor de la salle {n}. {VID[n]} Caméra stable, aucun personnage qui parle, aucun texte lisible. 8 secondes."
    elif rid.startswith("portrait-"):
        k = rid.split("-", 1)[1]
        pe = dia["personnages"][k]
        r[I["prompt_fr"]] = f"Portrait de référence, plan taille, cadrage vertical, fond flou de station scientifique. {pe['nom']} : {pe['role']}. {PORT[k]}. Personnage inventé, visage non réel. {STYLE}"
    r[I["negatif"]] = NEG
buf = io.StringIO()
csv.writer(buf, delimiter=";", lineterminator="\n").writerows(rows)
open(P, "w", encoding="utf-8").write(buf.getvalue())
print("medias.csv : prompts complétés (5 décors, 5 vidéos, 5 portraits)")
