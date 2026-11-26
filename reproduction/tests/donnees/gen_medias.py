# -*- coding: utf-8 -*-
"""Complète les prompts de immersifs/reproduction/medias.csv (5 décors, 5 vidéos, 5 portraits) après une migration.
Lancer depuis la racine du dépôt : python reproduction/tests/donnees/gen_medias.py   (puis prompts-flow.py reproduction)
Aucun animal blessé, habillé ou qui parle ; aucun accouplement ni mise bas montrés ; jardin, ferme et personnages inventés ; schémas jamais générés par IA."""
import csv, io, json

P = "immersifs/reproduction/medias.csv"
STYLE = ("Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, au matin après un orage de nuit, "
         "lumière douce, gouttes de pluie sur les feuilles, aucune inscription lisible, grain fin.")
NEG = ("texte lisible, écriture lisible, chiffres lisibles, logo, filigrane, mains déformées, visage déformé, personne réelle, animal déformé, animal blessé, "
       "sang, accouplement, mise bas, animal habillé, animal qui parle, caricature, style dessin animé")
DESC = {1: "L'intérieur d'une serre vitrée de jardin botanique, pleine de fleurs colorées en pots, une table de dissection en bois avec des loupes et une pince, une grande planche illustrée d'une fleur tombée au pied de la table avec des étiquettes vierges éparpillées, une boîte à fiches ouverte, un carnet à spirale mouillé, une porte vitrée entrouverte, flaques sur le sol.",
        2: "Un rucher au fond d'un jardin, cinq ruches en bois peintes posées au bord d'un verger de pommiers et de cerisiers en fleurs, une petite cabane d'apicultrice avec une combinaison blanche accrochée, une ficelle de dessins décrochés sous l'auvent, un cahier taché posé sur une ruche, un grand panneau en bois vierge à moitié peint, quelques abeilles.",
        3: "Le potager d'une école, des carrés de légumes en bois avec de jeunes pousses, une table avec quatre pots en plastique garnis de coton et de haricots, des boîtes en carton renversées dans l'allée avec des graines et des fruits secs, une grande affiche ronde vierge dont les images sont tombées dans l'herbe, un arrosoir, une soucoupe avec une graine ouverte et une loupe.",
        4: "La cour d'une ferme pédagogique, un poulailler en bois avec des poules qui picorent, une étable ouverte avec une vache, un petit étang aux roseaux, un tableau noir vierge à l'entrée, un gros registre ouvert sur un tonneau, un panneau tombé devant un enclos, deux petits panneaux vierges plantés au bord de l'étang.",
        5: "Une bergerie lumineuse avec des brebis et leurs agneaux dans la paille, une couveuse vitrée avec des œufs, un aquarium avec des têtards, une trousse de vétérinaire et un carnet rouge sur une botte de paille, et au fond un grand portail en fer fermé par un cadenas, ouvrant sur un jardin."}
VID = {1: "Lent travelling avant vers la table de dissection ; des gouttes glissent sur les vitres, une fleur bouge doucement, la lumière du matin entre par la porte entrouverte.",
       2: "Lent travelling latéral le long des ruches ; quelques abeilles volent de fleur en fleur dans le verger, des pétales tombent doucement, la ficelle des dessins se balance.",
       3: "Lent travelling avant vers les pots d'expérience ; les jeunes pousses bougent légèrement dans la brise, une goutte tombe de l'arrosoir, un merle passe dans le fond.",
       4: "Lent travelling avant dans la cour ; les poules picorent, des ronds se forment à la surface de l'étang, les roseaux bougent dans le vent.",
       5: "Lent travelling avant vers le portail ; un agneau se blottit contre sa mère, la lumière de la couveuse brille doucement, le portail s'entrouvre sur le jardin en fleurs."}
PORT = {"basile": "homme d'une soixantaine d'années, cheveux gris courts, barbe grise taillée, lunettes rondes, tablier de jardinier vert sur une chemise claire, loupe à la main, expression posée et précise, regard vers l'objectif",
        "capucine": "femme d'une trentaine d'années, cheveux roux longs attachés, combinaison d'apicultrice blanche ouverte sur un pull jaune moutarde, voile relevé, expression chaleureuse, regard vers l'objectif",
        "tom": "garçon d'une dizaine d'années, cheveux bruns courts, peau mate, sweat vert et gants de jardinage, tenant un petit pot de haricot qui germe, expression enthousiaste, regard vers l'objectif",
        "yasmine": "femme d'une quarantaine d'années, cheveux noirs longs tressés, veste de travail marron et bottes, foulard, expression énergique et souriante, regard vers l'objectif",
        "nadia": "femme d'une cinquantaine d'années, cheveux noirs courts, peau foncée, lunettes, blouse de vétérinaire bordeaux, stéthoscope autour du cou, expression douce et rigoureuse, regard vers l'objectif"}

rows = list(csv.reader(open(P, encoding="utf-8"), delimiter=";"))
I = {k: i for i, k in enumerate(rows[0])}
nar = json.load(open("vingt-mille-lieues/outils/immersif/narration/reproduction.json", encoding="utf-8"))["enigmes"]
dia = json.load(open("reproduction/assets/data/dialogues.json", encoding="utf-8"))
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
        r[I["prompt_fr"]] = f"Portrait de référence, plan taille, cadrage vertical, fond flou de jardin et de ferme au printemps. {pe['nom']} : {pe['role']}. {PORT[k]}. Personnage inventé, visage non réel. {STYLE}"
    r[I["negatif"]] = NEG
buf = io.StringIO()
csv.writer(buf, delimiter=";", lineterminator="\n").writerows(rows)
open(P, "w", encoding="utf-8").write(buf.getvalue())
print("medias.csv : prompts complétés (5 décors, 5 vidéos, 5 portraits)")
