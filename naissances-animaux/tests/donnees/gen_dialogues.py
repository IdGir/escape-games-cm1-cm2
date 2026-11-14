# -*- coding: utf-8 -*-
"""Génère dialogues.json (La Nurserie du zoo). Lancer : python gen_dialogues.py <dossier data>
Personnages et zoo inventés (le zoo des Trois-Sources) ; pas de reproduction humaine ; aucune scène de naissance montrée."""
import json, os, sys

MOTS = ["CELLULE", "EAU", "VIVIPARE", "EMBRYON", "NAISSANCE"]
PHRASE = "Une CELLULE de chaque parent forme l'œuf ; dans l'EAU ou dans le corps a lieu la fécondation ; l'ovipare pond, le VIVIPARE porte son petit ; l'EMBRYON grandit jusqu'à la NAISSANCE."

DIALOGUES = {
    "metadata": {"jeu": "La Nurserie du zoo",
                 "sujet": "Le développement des animaux de la fécondation à la naissance ; fécondation externe ou interne ; animaux ovipares et vivipares — sciences, cycle 3",
                 "niveaux": ["CM1", "CM2"],
                 "phrase_bilan": PHRASE,
                 "lien_autres_jeux": "Prépare « Le Jardin de la vie » (reproduction sexuée chez les plantes et les animaux, année A) et « L'Expédition biodiversité ».",
                 "sources": "Programme de sciences et technologie du cycle 3 ; La main à la pâte ; Muséum national d'histoire naturelle et INPN ; Écolothèque de Montpellier ; Lumni. Détail : README.md, section Sources.",
                 "vigilance": "Pas de reproduction humaine (laissée à l'enseignant, dans le cadre de l'éducation à la sexualité) ; les exceptions (ornithorynque, vipère aspic, requins) sont présentées comme des exceptions ; aucune vidéo ni image de naissance. Personnages et zoo inventés."},
    "personnages": {"ines": {"nom": "Inès", "role": "Vétérinaire du zoo"},
                    "theo": {"nom": "Théo", "role": "Soigneur de l'aquarium et de la mare"},
                    "malo": {"nom": "Malo", "role": "Soigneur de la galerie des animaux étonnants"},
                    "jeanne": {"nom": "Jeanne", "role": "Éleveuse de poules de la ferme du zoo"},
                    "sacha": {"nom": "Sacha", "role": "Élève de CM2 en visite scolaire"}},
    "intro_accueil": "Bonjour, je suis Inès, la vétérinaire du zoo des Trois-Sources. Cette nuit, une tempête a ouvert les fenêtres de la nurserie. Les fiches de naissance se sont envolées et toutes les étiquettes des œufs et des berceaux sont mélangées. Demain matin, les familles des petits attendent leurs nouveau-nés, et le carnet de naissance du zoo est verrouillé. Vous êtes nos apprentis soigneurs. Dans chaque salle, retrouvez comment naît chaque animal et notez le mot que vous donnera le responsable. Avec les cinq mots, nous ouvrirons le carnet et rendrons chaque petit à sa famille.",
    "salles": [
        {"num": 1, "titre": "Le laboratoire de la vétérinaire", "decor": "laboratoire", "motCle": MOTS[0], "lieu": "Le laboratoire de la vétérinaire, à côté de la nurserie",
         "description": "Une salle blanche avec un microscope, des bocaux étiquetés et un tableau couvert de dessins de cellules. Une fenêtre bat encore au vent.",
         "sens": ["À voir : les dessins de cellules au tableau", "À entendre : la fenêtre qui claque", "À toucher : la molette froide du microscope"],
         "dialogue_intro": {"perso": "ines", "nom": "Inès", "texte": "Entrez ! Avant de rendre les petits à leur famille, il faut comprendre comment commence la vie d'un animal. Tout part de deux cellules, si petites qu'on ne les voit qu'au microscope. Le vent a mélangé mon schéma et les étiquettes de mes bocaux. Vous m'aidez à tout remettre en ordre ?"},
         "dialogue_reussite": {"perso": "ines", "nom": "Inès", "texte": "Parfait. Le premier mot est <b>CELLULE</b> : chaque petit commence par une seule cellule, l'œuf. Théo vous attend à l'aquarium, de l'autre côté de l'allée."}},
        {"num": 2, "titre": "L'aquarium et la mare", "decor": "aquarium", "motCle": MOTS[1], "lieu": "L'aquarium et la mare pédagogique",
         "description": "De grands bassins éclairés en bleu, une mare avec des pontes de grenouille accrochées aux plantes. Les fiches des animaux flottent sur l'eau.",
         "sens": ["À voir : les pontes en gelée au bord de la mare", "À entendre : le glouglou des pompes", "À toucher : la vitre fraîche de l'aquarium"],
         "dialogue_intro": {"perso": "theo", "nom": "Théo", "texte": "Salut, je suis Théo. Je soigne les poissons et les grenouilles. Regardez ces petites boules de gelée dans la mare : ce sont des œufs. Mais tous les animaux ne font pas comme la grenouille. La tempête a jeté mes fiches à l'eau : il faut savoir, pour chaque animal, où se rencontrent les cellules du mâle et de la femelle."},
         "dialogue_reussite": {"perso": "theo", "nom": "Théo", "texte": "Fiches sauvées ! Le deuxième mot est <b>EAU</b> : c'est là que se fait la fécondation externe. Malo vous attend dans la galerie des surprises."}},
        {"num": 3, "titre": "La galerie des surprises", "decor": "galerie", "motCle": MOTS[2], "lieu": "La galerie des animaux étonnants",
         "description": "Un long couloir de vitrines : des œufs de toutes les tailles, une capsule de roussette, des panneaux sur l'ornithorynque et la vipère. Plusieurs panneaux sont tombés.",
         "sens": ["À voir : la rangée d'œufs, du plus petit au plus gros", "À entendre : l'écho des pas dans la galerie", "À toucher : la coquille épaisse d'un œuf d'autruche"],
         "dialogue_intro": {"perso": "malo", "nom": "Malo", "texte": "Bonjour, je suis Malo. Ma galerie, c'est celle des surprises ! Certains animaux pondent des œufs, d'autres donnent naissance à des petits vivants. Et puis il y a ceux qui ne font rien comme les autres. Les panneaux sont tombés : remettons chaque animal dans la bonne vitrine."},
         "dialogue_reussite": {"perso": "malo", "nom": "Malo", "texte": "Toutes les vitrines sont justes. Le troisième mot est <b>VIVIPARE</b> : le petit grandit dans le ventre de sa mère et naît vivant. Jeanne vous attend à la couveuse de la ferme."}},
        {"num": 4, "titre": "La couveuse de la ferme", "decor": "couveuse", "motCle": MOTS[3], "lieu": "La couveuse de la ferme du zoo",
         "description": "Une salle tiède où ronronne une couveuse vitrée remplie d'œufs. Au mur, un calendrier de 21 cases et un tableau des durées. Une lampe permet de regarder dans les œufs.",
         "sens": ["À voir : les œufs alignés dans la couveuse", "À entendre : le petit ventilateur de la couveuse", "À toucher : la chaleur douce de la vitre"],
         "dialogue_intro": {"perso": "jeanne", "nom": "Jeanne", "texte": "Bonjour les apprentis, moi c'est Jeanne. J'élève les poules de la ferme du zoo. Ici, on regarde grandir les poussins dans leur œuf, jour après jour. Et dans l'écurie, la jument attend son poulain. Mon calendrier et mon tableau ont été mélangés par la tempête. Aidez-moi à savoir ce qui se passe avant la naissance."},
         "dialogue_reussite": {"perso": "jeanne", "nom": "Jeanne", "texte": "Les berceaux sont prêts. Le quatrième mot est <b>EMBRYON</b> : c'est le petit qui grandit avant de naître. Sacha vous attend au bureau du carnet de naissance."}},
        {"num": 5, "titre": "Le bureau du carnet de naissance", "decor": "bureau", "motCle": MOTS[4], "lieu": "Le bureau du carnet de naissance",
         "description": "Un petit bureau en bois avec le grand registre du zoo, une carte des enclos et un carnet fermé par un cadenas. Sur la table, des étiquettes d'enclos à remettre.",
         "sens": ["À voir : la carte des enclos et le carnet cadenassé", "À entendre : le froissement des pages du registre", "À toucher : la couverture de cuir du carnet"],
         "dialogue_intro": {"perso": "sacha", "nom": "Sacha", "texte": "Bonjour ! Je suis Sacha, je suis en CM2 et ma classe visite le zoo aujourd'hui. Inès m'a confié une mission : remettre les panneaux des enclos et ouvrir le carnet de naissance. Mais je n'y arriverai pas tout seul. On fait équipe ?"},
         "dialogue_fin": {"perso": "ines", "nom": "Inès", "texte": "Le dernier mot est <b>NAISSANCE</b>. Vous avez les cinq mots : ouvrons le carnet et rendons chaque petit à sa famille."}},
    ]}


def main(dest):
    json.dump(DIALOGUES, open(os.path.join(dest, "dialogues.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
