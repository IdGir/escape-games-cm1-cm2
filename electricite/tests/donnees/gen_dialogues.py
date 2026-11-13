# -*- coding: utf-8 -*-
"""Génère dialogues.json (La Centrale en panne). Lancer : python gen_dialogues.py <dossier data>
Personnages inventés ; ville inventée (Clairval) ; aucune expérience avec le secteur."""
import json, os, sys

MOTS = ["BOUCLE", "CONDUCTEUR", "SCHÉMA", "SÉCURITÉ", "CENTRALE"]
PHRASE = "Une BOUCLE sans trou, un CONDUCTEUR pour la fermer, un SCHÉMA pour la dessiner, la SÉCURITÉ toujours, et la CENTRALE rallume la ville."

DIALOGUES = {
    "metadata": {"jeu": "La Centrale en panne",
                 "sujet": "L'électricité : circuit simple, conducteurs et isolants, schéma normalisé, sécurité, production et transport — sciences, cycle 3",
                 "niveaux": ["CM1", "CM2"],
                 "phrase_bilan": PHRASE,
                 "lien_autres_jeux": "Suite de « L'Atelier de l'inventeur » (objets techniques) et de « La lumière » ; prépare les jeux sur le climat et les énergies et sur la programmation.",
                 "sources": "Programme de sciences et technologie du cycle 3 (BO n° 24 du 11 juin 2026) ; La main à la pâte ; RTE, Bilan électrique 2025 ; Connaissance des énergies ; Enedis ; Lumni. Détail : README.md, section Sources.",
                 "vigilance": "Aucune expérience ni manipulation avec le secteur ; seules les piles de la classe sont utilisées. Pas d'« électrons » ; le mot « tension » n'apparaît que pour les volts de la pile et de la prise et pour les lignes. Personnages et ville inventés."},
    "personnages": {"nour": {"nom": "Nour", "role": "Élève du club sciences de la centrale"},
                    "maelle": {"nom": "Maëlle", "role": "Magasinière du matériel électrique"},
                    "helene": {"nom": "Hélène", "role": "Ingénieure de la centrale"},
                    "marius": {"nom": "Marius", "role": "Électricien de la ville"},
                    "karim": {"nom": "Karim", "role": "Technicien du réseau"}},
    "intro_accueil": "Bonsoir, je suis Hélène, ingénieure à la centrale de Clairval. Un violent orage a frappé la vallée : la foudre a fait disjoncter le réseau, et toute la ville est plongée dans le noir. Nos ordinateurs sont arrêtés, il faut tout vérifier à la main, pièce par pièce. Vous êtes nos apprentis électriciens. Dans chaque salle, réparez ce qui doit l'être et notez le mot que vous donnera le responsable. Avec les cinq mots, nous pourrons rebrancher les quartiers un par un. Une seule règle, et elle ne se discute pas : ici, on travaille avec des piles, jamais avec les prises.",
    "salles": [
        {"num": 1, "titre": "L'atelier du club sciences", "decor": "atelier", "motCle": MOTS[0], "lieu": "L'atelier du club sciences, au rez-de-chaussée de la centrale",
         "description": "Une petite salle éclairée par une lampe torche. Sur la table, des piles plates, des lampes sur leurs douilles, des fils à pinces et un interrupteur. La lampe de secours du couloir est éteinte.",
         "sens": ["À voir : le montage à moitié fini sur la table", "À entendre : la pluie sur les vitres", "À toucher : les pinces crocodiles froides"],
         "dialogue_intro": {"perso": "nour", "nom": "Nour", "texte": "Salut ! Moi, c'est Nour. Je suis au club sciences de la centrale. Avec la panne, la lampe de secours du couloir s'est éteinte, et ma lampe de poche aussi est presque vide. J'ai des piles neuves, des lampes et des fils, mais mon montage ne marche pas. Vous m'aidez à comprendre pourquoi ?"},
         "dialogue_reussite": {"perso": "nour", "nom": "Nour", "texte": "La lampe brille ! Le premier mot est <b>BOUCLE</b> : sans boucle complète, pas de lumière. Maëlle vous attend au magasin, au fond du couloir."}},
        {"num": 2, "titre": "Le magasin de matériel", "decor": "magasin", "motCle": MOTS[1], "lieu": "Le magasin de matériel électrique",
         "description": "Des étagères pleines de bobines de fil, de boîtes de vis, de gants et d'outils. Un bac de pièces renversé par l'orage. Sur l'établi, un circuit testeur.",
         "sens": ["À voir : les bobines de fil de cuivre", "À entendre : le cliquetis des vis dans le bac", "À toucher : la gaine souple des fils"],
         "dialogue_intro": {"perso": "maelle", "nom": "Maëlle", "texte": "Bonjour, je suis Maëlle, je m'occupe du matériel. L'orage a renversé mon bac de pièces, et tout est mélangé. Pour réparer les lignes, les électriciens ont besoin de ce qui laisse passer le courant ; pour se protéger, de ce qui l'arrête. On trie ensemble ?"},
         "dialogue_reussite": {"perso": "maelle", "nom": "Maëlle", "texte": "Bien triés ! Le deuxième mot est <b>CONDUCTEUR</b> : c'est lui qui laisse passer le courant. Hélène vous attend dans la salle de contrôle."}},
        {"num": 3, "titre": "La salle de contrôle", "decor": "controle", "motCle": MOTS[2], "lieu": "La salle de contrôle de la centrale",
         "description": "Un grand pupitre couvert de boutons éteints. Au mur, un tableau où sont dessinés des schémas. Des feuilles de plans tombées par terre.",
         "sens": ["À voir : les schémas au mur et les voyants éteints", "À entendre : le bourdonnement du groupe de secours", "À toucher : les boutons froids du pupitre"],
         "dialogue_intro": {"perso": "helene", "nom": "Hélène", "texte": "Voici la salle de contrôle. Ici, on ne dessine pas les appareils comme dans un livre d'images : on utilise des symboles, les mêmes dans le monde entier. Le pupitre ne redémarrera que si vous savez lire ses schémas. Les étiquettes sont tombées pendant l'orage."},
         "dialogue_reussite": {"perso": "helene", "nom": "Hélène", "texte": "Les voyants s'allument un à un. Le troisième mot est <b>SCHÉMA</b>. Marius a ramené de la ville la maison témoin de nos visites : il vous attend."}},
        {"num": 4, "titre": "La maison témoin", "decor": "maison", "motCle": MOTS[3], "lieu": "La maison témoin, dans le hall des visites",
         "description": "Une petite maison en bois grandeur nature, montée dans le hall : une cuisine, une salle de bain, un salon, un tableau électrique avec son disjoncteur. Des affiches de prévention sont tombées au sol.",
         "sens": ["À voir : les prises, le disjoncteur et les affiches", "À entendre : le tic-tac de l'horloge de la cuisine", "À toucher : rien sans l'accord de Marius"],
         "dialogue_intro": {"perso": "marius", "nom": "Marius", "texte": "Salut, je suis Marius, électricien de la ville. Quand le courant va revenir, chaque maison de Clairval sera de nouveau sous tension. Avant de rallumer, je veux être sûr que vous connaissez les règles de sécurité. Les piles de l'atelier, ce n'est pas la même chose que les prises de la maison. Montrez-moi ce que vous savez."},
         "dialogue_reussite": {"perso": "marius", "nom": "Marius", "texte": "Vous pouvez rallumer sans danger. Le quatrième mot est <b>SÉCURITÉ</b>. Karim vous attend au poste de conduite du réseau."}},
        {"num": 5, "titre": "Le poste de conduite du réseau", "decor": "reseau", "motCle": MOTS[4], "lieu": "Le poste de conduite du réseau",
         "description": "Une salle sombre avec une grande carte lumineuse de la vallée : la centrale, les lignes, les postes et les quatre quartiers de Clairval, tous éteints. Devant la carte, le pupitre de reconnexion.",
         "sens": ["À voir : la carte de la vallée et les quatre quartiers éteints", "À entendre : le grésillement du haut-parleur", "À toucher : les quatre leviers du pupitre"],
         "dialogue_intro": {"perso": "karim", "nom": "Karim", "texte": "Bonsoir, je suis Karim, technicien du réseau. La centrale est prête. Mais il faut amener l'électricité jusqu'aux maisons, et rebrancher les quartiers un par un : si on les rallume tous d'un coup, le réseau disjoncte à nouveau. Le pupitre demande des codes. Vous êtes prêts ?"},
         "dialogue_fin": {"perso": "helene", "nom": "Hélène", "texte": "Le dernier mot est <b>CENTRALE</b> : c'est là que l'électricité est produite. Vous avez les cinq mots : fermons le dernier circuit et rallumons Clairval."}},
    ]}


def main(dest):
    json.dump(DIALOGUES, open(os.path.join(dest, "dialogues.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
