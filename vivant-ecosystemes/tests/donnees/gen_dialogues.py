# -*- coding: utf-8 -*-
"""Génère dialogues.json (L'Expédition biodiversité). Lancer : python gen_dialogues.py <dossier data>
Réserve naturelle du Val-des-Saules (Bourgogne) et personnages inventés ; ton non alarmiste."""
import json, os, sys

MOTS = ["ESPÈCE", "GROUPES", "FOSSILES", "MILIEU", "RÉSEAU"]
PHRASE = "Chaque ESPÈCE se range dans des GROUPES emboîtés ; les FOSSILES racontent le vivant d'autrefois ; chaque MILIEU abrite des êtres vivants liés en RÉSEAU."

DIALOGUES = {
    "metadata": {"jeu": "L'Expédition biodiversité",
                 "sujet": "Panorama du vivant : observer, espèce, classification en groupes emboîtés, clé de détermination, biodiversité passée (fossiles, extinction), écosystème et réseau alimentaire — sciences, cycle 3",
                 "niveaux": ["CM1", "CM2"],
                 "phrase_bilan": PHRASE,
                 "lien_autres_jeux": "Fait suite à « La Nurserie du zoo » (n°15) ; prépare « Mission Climat » (n°26) et « Le Jardin de la vie » (n°24).",
                 "sources": "Programme de sciences et technologie du cycle 3 (BO n° 24 du 11 juin 2026) ; MNHN et INPN ; La main à la pâte ; OFB ; Centre de ressources Espèces exotiques envahissantes. Détail : README.md, section Sources.",
                 "vigilance": "Vocabulaire du programme (milieu de vie, êtres vivants ; pas de biotope ni de biocénose) ; pas de groupe « invertébrés » (on ne classe pas sur une absence) ; ton non alarmiste ; réserve et personnages inventés."},
    "personnages": {"lina": {"nom": "Lina", "role": "Biologiste de terrain, cheffe de l'expédition"},
                    "hugo": {"nom": "Hugo", "role": "Garde de la réserve naturelle"},
                    "amara": {"nom": "Amara", "role": "Paléontologue"},
                    "rose": {"nom": "Rose", "role": "Apicultrice du pré de la réserve"},
                    "elio": {"nom": "Élio", "role": "Pêcheur de l'étang"}},
    "intro_accueil": "Bonjour, je suis Lina, biologiste. Bienvenue dans la réserve naturelle du Val-des-Saules. Samedi, pour la Fête de la nature, nous devons présenter la grande carte du vivant de la réserve. Mais cette nuit, le ruisseau a débordé : notre campement a pris l'eau, et toutes les fiches de l'expédition sont mélangées. Vous êtes nos jeunes naturalistes. Dans chaque lieu de la réserve, aidez l'expert qui vous attend et notez le mot qu'il vous donnera. Avec les cinq mots, nous ouvrirons la boîte de la carte du vivant.",
    "salles": [
        {"num": 1, "titre": "La tente-laboratoire", "decor": "tente", "motCle": MOTS[0], "lieu": "La tente-laboratoire de l'expédition, au bord du ruisseau",
         "description": "Une grande tente de toile avec une table pliante, des loupes, un microscope de terrain, des boîtes d'observation et des carnets qui sèchent sur un fil.",
         "sens": ["À voir : les carnets qui sèchent sur un fil", "À entendre : le ruisseau qui coule encore fort", "À toucher : la toile humide de la tente"],
         "dialogue_intro": {"perso": "lina", "nom": "Lina", "texte": "Entrez ! Un naturaliste commence toujours par bien observer. Mes carnets ont pris l'eau, et le dessin de ma mésange a perdu ses étiquettes. Il faut décrire chaque être vivant par ce qu'il possède, et savoir qui appartient à la même espèce. Vous m'aidez ?"},
         "dialogue_reussite": {"perso": "lina", "nom": "Lina", "texte": "Bravo. Le premier mot est <b>ESPÈCE</b> : des êtres vivants qui se ressemblent et peuvent avoir des petits ensemble. Hugo, le garde, vous attend à sa cabane, à l'entrée de la forêt."}},
        {"num": 2, "titre": "La cabane du garde", "decor": "cabane", "motCle": MOTS[1], "lieu": "La cabane du garde, à l'entrée de la forêt",
         "description": "Une cabane en bois avec des caisses de rangement, des fiches d'animaux, une grande clé de détermination punaisée au mur et un bac de feuilles mortes plein de petites bêtes.",
         "sens": ["À voir : la clé de détermination au mur", "À entendre : un pic qui tambourine sur un tronc", "À toucher : les feuilles mortes humides du bac"],
         "dialogue_intro": {"perso": "hugo", "nom": "Hugo", "texte": "Salut, moi c'est Hugo, le garde de la réserve. L'eau a renversé mes caisses : toutes les fiches sont mélangées. Ici, on range les êtres vivants selon ce qu'ils possèdent, jamais selon ce qui leur manque. Et pour trouver le nom d'une petite bête, on suit ma clé."},
         "dialogue_reussite": {"perso": "hugo", "nom": "Hugo", "texte": "Tout est rangé. Le deuxième mot est <b>GROUPES</b> : des groupes emboîtés, comme des boîtes dans des boîtes. Amara, la paléontologue, vous attend à l'ancienne carrière."}},
        {"num": 3, "titre": "L'ancienne carrière", "decor": "carriere", "motCle": MOTS[2], "lieu": "L'ancienne carrière de calcaire de la réserve",
         "description": "Une paroi de roche en couches, des bacs de fossiles, un tamis, une grande frise du temps et une vitrine fermée par un cadenas.",
         "sens": ["À voir : les couches de roche de la paroi", "À entendre : le petit marteau qui tinte sur la pierre", "À toucher : la spirale d'une ammonite"],
         "dialogue_intro": {"perso": "amara", "nom": "Amara", "texte": "Bonjour, je suis Amara, paléontologue. Ici, la roche garde la mémoire du vivant d'autrefois : des coquilles, des os, des empreintes. Mes étiquettes sont tombées dans les flaques. Remettons de l'ordre dans des millions d'années d'histoire !"},
         "dialogue_reussite": {"perso": "amara", "nom": "Amara", "texte": "Magnifique. Le troisième mot est <b>FOSSILES</b> : ils racontent le vivant d'autrefois. Rose vous attend près des ruches, au bord de la mare."}},
        {"num": 4, "titre": "La mare et le pré fleuri", "decor": "mare", "motCle": MOTS[3], "lieu": "La mare de la réserve et le pré fleuri où sont les ruches",
         "description": "Une mare entourée de roseaux, des nénuphars, des libellules au-dessus de l'eau, et plus loin un pré plein de fleurs avec trois ruches en bois.",
         "sens": ["À voir : un héron immobile dans l'eau peu profonde", "À entendre : le bourdonnement des abeilles", "À toucher : l'eau fraîche de la mare"],
         "dialogue_intro": {"perso": "rose", "nom": "Rose", "texte": "Bonjour les naturalistes ! Je suis Rose, je m'occupe des ruches du pré. Mes abeilles ont besoin des fleurs, et les fleurs ont besoin de mes abeilles. Autour de cette mare, tout est lié. Mes relevés ont été mouillés : aidez-moi à décrire cet écosystème."},
         "dialogue_reussite": {"perso": "rose", "nom": "Rose", "texte": "Merci ! Le quatrième mot est <b>MILIEU</b> : chaque être vivant vit là où le milieu lui convient. Élio vous attend sur le ponton de l'étang."}},
        {"num": 5, "titre": "Le ponton de l'étang", "decor": "etang", "motCle": MOTS[4], "lieu": "Le ponton du grand étang de la réserve",
         "description": "Un ponton de bois au-dessus de l'eau, une barque, un carnet de pêche, et sur une table la boîte fermée de la carte du vivant.",
         "sens": ["À voir : les ronds dans l'eau des perches qui chassent", "À entendre : le clapotis contre la barque", "À toucher : le bois tiède du ponton"],
         "dialogue_intro": {"perso": "elio", "nom": "Élio", "texte": "Salut ! Moi, c'est Élio. Je pêche dans cet étang depuis longtemps, et je sais qui mange qui. Ma carte du réseau de l'étang a perdu des morceaux. Si on la refait, on pourra ouvrir la boîte de la carte du vivant."},
         "dialogue_fin": {"perso": "lina", "nom": "Lina", "texte": "Le dernier mot est <b>RÉSEAU</b>. Vous avez les cinq mots : ouvrons la boîte et terminons la carte du vivant de la réserve."}},
    ]}


def main(dest):
    json.dump(DIALOGUES, open(os.path.join(dest, "dialogues.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
