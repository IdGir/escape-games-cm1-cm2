# -*- coding: utf-8 -*-
"""Génère dialogues.json (La Caravelle du capitaine). Lancer : python gen_dialogues.py <dossier data>
Personnages inventés ; aucune personne réelle ne parle."""
import json, os, sys

MOTS = ["ÉPICES", "ASTROLABE", "OCÉAN", "RENCONTRE", "EMPIRES"]
PHRASE = "Pour les ÉPICES, guidés par l'ASTROLABE, les Européens traversent l'OCÉAN ; la RENCONTRE devient conquête et fonde des EMPIRES."

DIALOGUES = {
    "metadata": {"jeu": "La Caravelle du capitaine",
                 "sujet": "Les progrès techniques qui ont permis aux Européens de s'aventurer vers de nouveaux territoires ; la constitution des premiers empires coloniaux en Amérique — histoire, cycle 3",
                 "niveaux": ["CM1", "CM2"],
                 "phrase_bilan": PHRASE,
                 "lien_autres_jeux": "Précède le jeu n°12 « Les Archives du port » (la traite atlantique naît du besoin de main-d'œuvre dans les mines et les plantations des colonies) ; complète « Le Tour du monde » (géographie) et « L'Atelier de Léonard à Amboise » (François Ier, qui envoie Cartier).",
                 "sources": "Programme d'histoire-géographie du cycle 3 (BO n° 22 du 28 mai 2026) ; Musée national de la Marine ; BnF ; Hérodote ; National Geographic ; World History Encyclopedia ; UNESCO ; BAnQ ; Lumni. Détail : README.md, section Sources.",
                 "vigilance": "On écrit « arrivée des Européens » à côté des repères classiques : l'Amérique était habitée. Ton sobre sur les violences de la conquête. Les habitants d'Amérique ont une voix propre (Itzel). Personnages inventés."},
    "personnages": {"amaury": {"nom": "Amaury", "role": "Guide du festival, spécialiste du commerce des épices"},
                    "rosa": {"nom": "Rosa", "role": "Cartographe, restauratrice de cartes anciennes"},
                    "bastien": {"nom": "Bastien", "role": "Capitaine de la caravelle"},
                    "itzel": {"nom": "Itzel", "role": "Conteuse venue de Mexico"},
                    "simon": {"nom": "Simon", "role": "Mousse de la caravelle"}},
    "intro_accueil": "Bienvenue à bord de la Rose des vents, la copie d'une caravelle amarrée au port de Saint-Malo pour le festival de la mer. Je suis Bastien, le capitaine. Cette nuit, une tempête a ouvert le coffre où je gardais le journal de bord que nous lisons aux visiteurs : ses pages se sont envolées dans tout le navire. Ce journal raconte comment les Européens sont partis sur les océans, il y a plus de cinq cents ans, et ce qui s'est passé en arrivant. Il raconte aussi une rencontre, puis une conquête. Vous êtes mes nouveaux mousses : retrouvez les pages, remettez-les dans l'ordre et notez les cinq mots qui ouvriront le coffre de bord.",
    "salles": [
        {"num": 1, "titre": "La cale aux épices", "decor": "cale", "motCle": MOTS[0], "lieu": "La cale de la Rose des vents",
         "description": "Une cale basse, éclairée par des lanternes. Des sacs de toile, des coffres et des tonneaux. Une carte roulée dépasse d'un coffre ouvert.",
         "sens": ["À voir : les sacs de toile et la carte roulée", "À entendre : le bois de la coque qui craque", "À sentir : le poivre et la cannelle"],
         "dialogue_intro": {"perso": "amaury", "nom": "Amaury", "texte": "Bonjour, moussaillons ! Je suis Amaury. Pendant le festival, je raconte aux visiteurs le commerce des épices. Respirez : ce parfum de poivre a fait rêver toute l'Europe. Mais pourquoi traverser des océans inconnus pour quelques graines ? Les premières pages du journal le disent. Aidez-moi à les retrouver dans la cale."},
         "dialogue_reussite": {"perso": "amaury", "nom": "Amaury", "texte": "Le premier mot est <b>ÉPICES</b> : c'est d'abord pour elles que l'on part. Rosa vous attend sur le pont, avec ses instruments."}},
        {"num": 2, "titre": "Le pont de la caravelle", "decor": "pont", "motCle": MOTS[1], "lieu": "Le pont de la Rose des vents",
         "description": "Le pont en bois, les mâts, les voiles repliées. Près de la barre, un coffre d'instruments en laiton est ouvert : une boussole, un astrolabe, un sablier.",
         "sens": ["À voir : les voiles et le coffre d'instruments", "À entendre : les cordages qui claquent au vent", "À sentir : l'air salé du large"],
         "dialogue_intro": {"perso": "rosa", "nom": "Rosa", "texte": "Bonjour, je suis Rosa, cartographe. Je restaure des cartes anciennes. Partir, c'est bien ; revenir, c'est mieux ! Pour oser quitter les côtes, les marins avaient besoin d'un bon navire et d'instruments pour savoir où ils étaient. Le vent a mélangé mes étiquettes : à vous de jouer."},
         "dialogue_reussite": {"perso": "rosa", "nom": "Rosa", "texte": "Le deuxième mot est <b>ASTROLABE</b> : grâce à lui, le pilote trouve sa route en pleine mer. Le capitaine vous attend dans la chambre des cartes."}},
        {"num": 3, "titre": "La chambre des cartes", "decor": "cartes", "motCle": MOTS[2], "lieu": "La chambre des cartes, sous le château arrière",
         "description": "Une petite pièce sous le château arrière. Sur la table, une grande carte du monde, un compas à pointes sèches et une corde où pendent les pages du journal.",
         "sens": ["À voir : la grande carte et les pages suspendues", "À entendre : les vagues contre la coque", "À sentir : l'encre et le vieux papier"],
         "dialogue_intro": {"perso": "bastien", "nom": "Bastien", "texte": "Entrez dans ma chambre des cartes. Ici, le journal raconte les grands voyages : vers l'ouest, vers l'est, et même autour du monde. Mais attention : les terres où ces navires arrivaient étaient habitées depuis des milliers d'années. Remettez mes pages dans l'ordre et retrouvez les routes."},
         "dialogue_reussite": {"perso": "bastien", "nom": "Bastien", "texte": "Le troisième mot est <b>OCÉAN</b> : Atlantique, Indien, Pacifique, ces marins les ont tous traversés. Descendez sur le quai : Itzel vous attend."}},
        {"num": 4, "titre": "Le rivage", "decor": "rivage", "motCle": MOTS[3], "lieu": "La tente des conteurs, sur le quai",
         "description": "Sur le quai, une grande tente de toile. À l'intérieur, des tapis, un panier de maïs, de cacao et de tomates, et des dessins de Tenochtitlan accrochés aux piquets.",
         "sens": ["À voir : le panier et les dessins de la grande ville sur le lac", "À entendre : la voix d'Itzel et les mouettes", "À sentir : le cacao chaud"],
         "dialogue_intro": {"perso": "itzel", "nom": "Itzel", "texte": "Bonjour. Je m'appelle Itzel, je viens de Mexico. Mes ancêtres parlaient le nahuatl, la langue des Aztèques. Dans vos livres, on lit souvent que l'Amérique a été découverte. Mais nous étions là ! Je vais vous raconter cette rencontre, de l'autre côté de l'océan. Elle a été belle parfois, et très dure souvent."},
         "dialogue_reussite": {"perso": "itzel", "nom": "Itzel", "texte": "Le quatrième mot est <b>RENCONTRE</b> : une rencontre qui est vite devenue une conquête. Simon vous attend dans le cabinet du cartographe."}},
        {"num": 5, "titre": "Le cabinet du cartographe", "decor": "cabinet", "motCle": MOTS[4], "lieu": "Le cabinet du cartographe, au fond du navire",
         "description": "Un réduit éclairé par une lampe. Au mur, une carte partagée par une ligne en pointillés. Des pavillons pliés sur une étagère. Au centre, le coffre de bord, fermé par un cadenas à chiffres.",
         "sens": ["À voir : la carte du partage et le coffre de bord", "À entendre : la lampe qui grésille", "À sentir : la cire des bougies"],
         "dialogue_intro": {"perso": "simon", "nom": "Simon", "texte": "Salut ! Moi, c'est Simon, le mousse. J'ai retrouvé les dernières pages : elles parlent de pays d'Europe qui se partagent des terres qui n'étaient pas à eux. Et le coffre de bord est fermé ! Il faut relier chaque grand voyage à sa date. On s'y met ?"},
         "dialogue_fin": {"perso": "bastien", "nom": "Bastien", "texte": "Le dernier mot est <b>EMPIRES</b> : l'Espagne, le Portugal, puis la France et l'Angleterre se sont construit des empires coloniaux. Vous avez les cinq mots : ouvrons le coffre de bord."}},
    ]}


def main(dest):
    json.dump(DIALOGUES, open(os.path.join(dest, "dialogues.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
