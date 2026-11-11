# -*- coding: utf-8 -*-
"""Génère dialogues.json et evaluations.json (Les Archives du port). Lancer : python gen_dialogues_eval.py <dossier data>"""
import json, os, sys

MOTS = ["TRIANGLE", "CAPTIFS", "PLANTATIONS", "PORTS", "LIBERTÉ"]

DIALOGUES = {
    "metadata": {"jeu": "Les Archives du port",
                 "sujet": "La traite des esclaves entre l'Afrique et l'Amérique, la vie des esclaves dans les plantations, les échanges commerciaux avec les colonies, les résistances et les abolitions — histoire, cycle 3",
                 "niveaux": ["CM1", "CM2"],
                 "lien_autres_jeux": "Prépare le jeu n°13 « La Caravelle du capitaine » (explorations, premiers empires coloniaux) et le jeu n°16 « Le Testament de l'Empereur » (Napoléon rétablit l'esclavage en 1802) ; se relie à « De l'édit de Nantes à Versailles » (Louis XIV signe le Code noir en 1685) et au « Secret de la Déclaration » (1789).",
                 "sources": "Programme d'histoire-géographie du cycle 3 (BO n° 22 du 28 mai 2026) ; BnF France-Amériques ; académies de Bordeaux, de Martinique et de Guyane ; Sénat ; ministère de la Culture. Détail : README.md, section Sources.",
                 "vigilance": "Sujet sensible. Les élèves sont des enquêteurs d'archives, jamais des personnages réduits en esclavage. Aucune personne réelle ne parle."},
    "personnages": {"ines": {"nom": "Inès", "role": "Archiviste des Archives du port"},
                    "malik": {"nom": "Malik", "role": "Historien venu de Dakar"},
                    "celia": {"nom": "Célia", "role": "Historienne venue de Guadeloupe"},
                    "margot": {"nom": "Margot", "role": "Conservatrice du musée du port"},
                    "theo": {"nom": "Théo", "role": "Élève de l'atelier d'enquête"}},
    "intro_accueil": "Bonjour, et bienvenue aux Archives du port. Je suis Inès, l'archiviste. Ici, nous gardons les papiers des navires partis de nos côtes il y a plus de deux siècles. Cette nuit, l'humidité a décollé les pages d'un registre précieux : elles se sont mélangées dans cinq salles. Ce registre raconte une histoire grave, celle de la traite des esclaves. Vous êtes nos enquêtrices et nos enquêteurs : dans chaque salle, retrouvez un mot, notez-le bien, et nous pourrons reconstituer le registre.",
    "salles": [
        {"num": 1, "titre": "La salle des cartes", "decor": "cartes", "motCle": MOTS[0], "lieu": "La salle des cartes des Archives du port",
         "description": "De grands meubles à tiroirs plats, une table éclairée par une lampe verte et, au mur, une carte ancienne de l'océan Atlantique. Une page du registre est posée sur la table.",
         "sens": ["À voir : la grande carte de l'Atlantique", "À entendre : le froissement du papier ancien", "À sentir : l'odeur de la poussière et de l'encre"],
         "dialogue_intro": {"perso": "ines", "nom": "Inès", "texte": "La première page du registre est une carte. Les noms ont été effacés par l'humidité. Pour comprendre le voyage des navires, il faut d'abord savoir où ils allaient. Prenez les loupes, et regardez bien les flèches."},
         "dialogue_reussite": {"perso": "ines", "nom": "Inès", "texte": "Le premier mot est <b>TRIANGLE</b> : Europe, Afrique, Amériques. Malik vous attend dans le cabinet des registres."}},
        {"num": 2, "titre": "Le cabinet des registres", "decor": "registres", "motCle": MOTS[1], "lieu": "Le cabinet des registres de navires",
         "description": "Des étagères chargées de registres reliés de cuir. Sur un pupitre, un journal de bord ouvert et une maquette de navire sous verre.",
         "sens": ["À voir : les registres alignés et la maquette du navire", "À entendre : l'horloge du cabinet", "À sentir : le cuir des vieilles reliures"],
         "dialogue_intro": {"perso": "malik", "nom": "Malik", "texte": "Bonjour. Je suis Malik, historien. Je viens de Dakar pour étudier ces registres. Derrière chaque ligne, il y a des personnes : des femmes, des hommes et des enfants arrachés à l'Afrique. Les historiens comptent avec soin, pour mesurer l'ampleur de ce crime. Aidez-moi à remettre de l'ordre dans mes fiches."},
         "dialogue_reussite": {"perso": "malik", "nom": "Malik", "texte": "Le deuxième mot est <b>CAPTIFS</b> : des millions de personnes déportées de force. Célia vous attend dans le fonds des colonies."}},
        {"num": 3, "titre": "Le fonds des colonies", "decor": "colonies", "motCle": MOTS[2], "lieu": "Le fonds des colonies, au premier étage",
         "description": "Une salle de lecture calme. Sur la table, le plan d'une habitation sucrière des Antilles et un vieux livre de lois, ouvert sous une vitre.",
         "sens": ["À voir : le plan de l'habitation et le livre de lois", "À entendre : la pluie contre la fenêtre", "À sentir : le bois ciré des tables"],
         "dialogue_intro": {"perso": "celia", "nom": "Célia", "texte": "Bonjour, je suis Célia, historienne. Je viens de Guadeloupe. Mes recherches portent sur la vie des personnes réduites en esclavage dans les plantations. Elles ont subi un travail forcé et une loi injuste. Mais elles ont aussi résisté. Venez voir."},
         "dialogue_reussite": {"perso": "celia", "nom": "Célia", "texte": "Le troisième mot est <b>PLANTATIONS</b> : le travail forcé, le Code noir, mais aussi les résistances. Margot vous attend au musée du port."}},
        {"num": 4, "titre": "Le musée du port", "decor": "musee", "motCle": MOTS[3], "lieu": "Le musée du port, au rez-de-chaussée",
         "description": "Des vitrines éclairées, des sacs de toile, des barriques et des caisses de bois. Au mur, la carte de la côte atlantique et de la Manche.",
         "sens": ["À voir : les vitrines et les barriques", "À entendre : les pas des visiteurs sur le parquet", "À sentir : une légère odeur de café et de toile de jute"],
         "dialogue_intro": {"perso": "margot", "nom": "Margot", "texte": "Bienvenue au musée du port. Je suis Margot, la conservatrice. Ici, nous montrons ce que les navires emportaient et ce qu'ils rapportaient. Ces richesses venaient du travail forcé des esclaves : un musée doit le dire clairement. Aidez-moi à refaire mes vitrines."},
         "dialogue_reussite": {"perso": "margot", "nom": "Margot", "texte": "Le quatrième mot est <b>PORTS</b> : des villes qui se sont enrichies grâce à ce commerce. Théo vous attend dans la salle de lecture."}},
        {"num": 5, "titre": "La salle de lecture", "decor": "lecture", "motCle": MOTS[4], "lieu": "La salle de lecture des Archives",
         "description": "Une grande salle claire aux longues tables. Sur un chevalet, une frise inachevée. Au centre, le registre reconstitué, fermé par un fermoir à chiffres.",
         "sens": ["À voir : la frise et le registre fermé", "À entendre : le murmure des lecteurs", "À sentir : le papier neuf des fiches"],
         "dialogue_intro": {"perso": "theo", "nom": "Théo", "texte": "Salut ! Moi, c'est Théo, je suis dans l'atelier d'enquête de mon école. Ma frise est toute mélangée. Je voulais montrer que les esclaves ont résisté et que l'esclavage a été aboli. Vous m'aidez ?"},
         "dialogue_fin": {"perso": "ines", "nom": "Inès", "texte": "Le dernier mot est <b>LIBERTÉ</b> : conquise par les révoltes et inscrite dans la loi en 1848. Vous avez les cinq mots : refermons le registre."}},
    ]}


def q(qq, opts, b, pts=1):
    return {"q": qq, "options": opts, "bonne": b, "pts": pts}


EVAL = {
    "metadata": {"sujet": "Le commerce triangulaire, la traite atlantique, les plantations et le Code noir, les échanges avec les colonies, les résistances et les abolitions",
                 "niveaux": ["CM1", "CM2"],
                 "programme": "Histoire, cycle 3 — thème « Explorations et conquêtes » (BO n° 22 du 28 mai 2026). Progression de l'enseignant : année A, période 3 (« La traite des esclaves entre l'Afrique et l'Amérique et la vie des esclaves dans les plantations. Les échanges commerciaux avec les colonies. »).",
                 "sources": "Voir README.md du jeu, section Sources."},
    "quizz_final": {
        "CM1": [{"q": "Le commerce triangulaire relie...", "options": ["l'Europe, l'Afrique et les Amériques", "la France, l'Italie et l'Espagne", "l'Asie, l'Afrique et l'Europe"], "bonne": 0},
                {"q": "La traite négrière est...", "options": ["un voyage d'exploration", "le commerce de captifs africains vendus comme esclaves", "une fête dans les ports"], "bonne": 1},
                {"q": "Dans les plantations des Antilles, les esclaves cultivaient surtout...", "options": ["le blé", "la vigne", "la canne à sucre"], "bonne": 2},
                {"q": "Un esclave qui s'enfuyait était appelé...", "options": ["un marron", "un armateur", "un capitaine"], "bonne": 0},
                {"q": "L'esclavage a été aboli définitivement en France en...", "options": ["1685", "1848", "1802"], "bonne": 1}],
        "CM2": [{"q": "La traite atlantique a déporté plus de...", "options": ["12,5 millions de personnes", "12 500 personnes", "125 000 personnes"], "bonne": 0},
                {"q": "Le premier port négrier français est...", "options": ["Marseille", "Lyon", "Nantes"], "bonne": 2},
                {"q": "Le Code noir a été signé en 1685 par...", "options": ["Napoléon Bonaparte", "Louis XIV", "Victor Schœlcher"], "bonne": 1},
                {"q": "En 1802, Napoléon Bonaparte...", "options": ["rétablit l'esclavage", "abolit l'esclavage", "fonde Haïti"], "bonne": 0},
                {"q": "La loi du 21 mai 2001 reconnaît la traite et l'esclavage comme...", "options": ["un commerce utile", "une erreur sans importance", "un crime contre l'humanité"], "bonne": 2}]},
    "fiches_preparatoires": [
        {"salle": 1, "titre": "La salle des cartes — le commerce triangulaire", "objectifs": ["Situer les trois continents", "Décrire les trois trajets d'un navire"],
         "vocabulaire": [{"mot": "commerce triangulaire", "def": "Europe, Afrique, Amériques : trois trajets"}, {"mot": "captif", "def": "personne privée de liberté"}, {"mot": "armateur", "def": "négociant qui finance le navire"}],
         "contexte": "Trajet 1 : marchandises vers l'Afrique. Trajet 2 : captifs vers les Amériques. Trajet 3 : sucre et café vers l'Europe."},
        {"salle": 2, "titre": "Le cabinet des registres — la traite atlantique", "objectifs": ["Mesurer l'ampleur de la traite", "Citer des ports français"],
         "vocabulaire": [{"mot": "traite négrière", "def": "commerce de captifs vendus comme esclaves"}, {"mot": "déporter", "def": "emmener de force loin de son pays"}],
         "contexte": "Plus de 12,5 millions de personnes déportées du XVIe au XIXe siècle. Nantes : 44 % des expéditions françaises."},
        {"salle": 3, "titre": "Le fonds des colonies — les plantations", "objectifs": ["Décrire le travail forcé", "Savoir ce qu'est le Code noir", "Connaître le marronnage"],
         "vocabulaire": [{"mot": "habitation", "def": "plantation aux Antilles"}, {"mot": "Code noir", "def": "édit de Louis XIV (1685) sur l'esclavage"}, {"mot": "marron", "def": "esclave en fuite"}],
         "contexte": "Le Code noir traite l'esclave comme un bien. Les esclaves résistent : fuite, révoltes, chants et contes."},
        {"salle": 4, "titre": "Le musée du port — les échanges avec les colonies", "objectifs": ["Nommer les produits échangés", "Situer des ports sur une carte"],
         "vocabulaire": [{"mot": "colonie", "def": "territoire dominé et exploité par un pays lointain"}, {"mot": "denrée coloniale", "def": "sucre, café, cacao..."}],
         "contexte": "Ces richesses viennent du travail forcé des esclaves. On ne généralise pas l'histoire d'un port à toute la France."},
        {"salle": 5, "titre": "La salle de lecture — résistances et abolitions", "objectifs": ["Ranger des dates sur une frise", "Connaître Toussaint Louverture et Victor Schœlcher"],
         "vocabulaire": [{"mot": "abolir", "def": "supprimer par une loi"}, {"mot": "mémoire", "def": "souvenir que l'on transmet"}],
         "contexte": "1791 révolte de Saint-Domingue ; 1794 abolition ; 1802 rétablissement ; 1804 Haïti ; 1848 abolition définitive ; 10 mai."}],
    "qcm": {
        "CM1": [q("Sur la carte, le commerce triangulaire dessine...", ["un cercle", "un triangle", "une ligne droite"], 1),
                q("Au premier trajet, le navire emporte vers l'Afrique...", ["des tissus et des armes", "du sucre", "des captifs"], 0),
                q("Au troisième trajet, le navire rapporte en Europe...", ["des fusils", "des captifs", "du sucre et du café"], 2),
                q("Les captifs étaient achetés...", ["en Afrique", "en Asie", "en France"], 0),
                q("La traversée de l'Atlantique durait environ...", ["deux jours", "deux mois", "deux ans"], 1),
                q("Nantes est...", ["une ville de montagne", "une île des Antilles", "un port français de la traite"], 2),
                q("Le Code noir est...", ["une loi de 1685 sur l'esclavage", "un journal de bord", "un tableau"], 0),
                q("Le moulin de la plantation sert à...", ["moudre du blé", "broyer la canne à sucre", "fabriquer des tissus"], 1),
                q("En 1791, à Saint-Domingue...", ["Louis XIV est couronné", "Haïti est fondée", "les esclaves se révoltent"], 2),
                q("Chaque 10 mai, la France...", ["se souvient de la traite et de l'esclavage", "fête la fin de la guerre", "fête le roi"], 0)],
        "CM2": [q("Les navires français ont transporté environ ... des captifs de la traite atlantique.", ["50 %", "11 %", "1 %"], 1),
                q("Quelle part des expéditions françaises est partie de Nantes ?", ["44 %", "4 %", "94 %"], 0),
                q("Saint-Domingue est aujourd'hui...", ["la Martinique", "la Guadeloupe", "Haïti"], 2),
                q("Un « bien meuble », dans le Code noir, désigne...", ["un esclave considéré comme une chose", "un meuble du roi", "une maison"], 0),
                q("Le vesou est...", ["une prison", "le jus de la canne", "un navire"], 1),
                q("Le grand marronnage est...", ["une fuite de quelques heures", "une fête", "une fuite sans retour"], 2),
                q("L'indigo sert à...", ["teindre en bleu", "sucrer", "faire du chocolat"], 0),
                q("Lequel n'est pas un port de la traite ?", ["Le Havre", "Lyon", "La Rochelle"], 1),
                q("La première abolition de l'esclavage date du...", ["14 juillet 1789", "27 avril 1848", "4 février 1794"], 2),
                q("Qui a présidé la commission qui prépara le décret de 1848 ?", ["Victor Schœlcher", "Toussaint Louverture", "Napoléon Bonaparte"], 0),
                q("Haïti devient indépendante le...", ["20 mai 1802", "1er janvier 1804", "10 mai 2006"], 1),
                q("Depuis quand le 10 mai est-il une journée nationale de mémoire ?", ["1848", "2001", "2006"], 2)]},
    "questions_fermees": {
        "CM1": [{"q": "Les captifs partaient de leur plein gré vers les Amériques.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Les esclaves des plantations travaillaient sans salaire.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Le Code noir a été signé par Louis XIV.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "L'esclavage n'a jamais été rétabli après 1794.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Cite les trois continents du commerce triangulaire.", "type": "court", "rep": "l'Europe, l'Afrique et les Amériques", "pts": 1},
                {"q": "Cite deux produits rapportés des colonies d'Amérique.", "type": "court", "rep": "le sucre, le café, le coton, le cacao...", "pts": 1},
                {"q": "Comment appelle-t-on un esclave qui s'est enfui ?", "type": "court", "rep": "un marron", "pts": 1},
                {"q": "En quelle année l'esclavage a-t-il été aboli définitivement ?", "type": "court", "rep": "en 1848", "pts": 1}],
        "CM2": [{"q": "Les captifs débarquaient en France avant d'aller aux Antilles.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Nantes a armé près de la moitié des expéditions négrières françaises.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Toussaint Louverture est né esclave à Saint-Domingue.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "La loi du 21 mai 2001 reconnaît la traite comme un crime contre l'humanité.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Qu'est-ce que le marronnage ?", "type": "court", "rep": "la fuite des esclaves hors de la plantation", "pts": 1},
                {"q": "Qui rétablit l'esclavage en 1802 ?", "type": "court", "rep": "Napoléon Bonaparte, Premier consul", "pts": 1},
                {"q": "Que devient Saint-Domingue le 1er janvier 1804 ?", "type": "court", "rep": "Haïti, un pays indépendant", "pts": 1},
                {"q": "Pourquoi un musée doit-il dire d'où venaient les richesses des ports ?", "type": "court", "rep": "parce qu'elles venaient du travail forcé des esclaves et de la traite", "pts": 1}]},
    "etudes_documents": {
        "CM1": [{"titre": "La cargaison de La Licorne", "document": {"contenu": "Le 8 janvier 1787, La Licorne quitte Bordeaux. Dans ses cales : du vin, de l'eau-de-vie, du fer en barre, des fusils, de la poudre et des toiles. En août 1788, le navire revient à Bordeaux.", "source": "D'après le journal de bord de La Licorne, cité par l'académie de Bordeaux."},
                 "questions": [{"q": "De quel port part La Licorne ?", "type": "court", "rep": "de Bordeaux", "pts": 1},
                               {"q": "Vers quel continent ces marchandises sont-elles emportées ?", "type": "court", "rep": "vers l'Afrique", "pts": 1},
                               {"q": "À quoi servent ces marchandises ?", "type": "court", "rep": "à acheter des captifs", "pts": 1}]},
                {"titre": "La frise de Théo", "document": {"contenu": "1685 : le Code noir. 1791 : révolte des esclaves de Saint-Domingue. 1794 : première abolition. 1802 : rétablissement. 1848 : abolition définitive.", "source": "Frise du jeu, d'après la BnF et le décret du 27 avril 1848."},
                 "questions": [{"q": "Combien d'années séparent la première abolition du rétablissement ?", "type": "court", "rep": "8 ans (1802 − 1794)", "pts": 1},
                               {"q": "Quel événement a lieu avant la première abolition ?", "type": "court", "rep": "la révolte de Saint-Domingue (1791)", "pts": 1},
                               {"q": "En quelle année l'esclavage est-il aboli définitivement ?", "type": "court", "rep": "en 1848", "pts": 1}]}],
        "CM2": [{"titre": "L'article 1er du décret du 27 avril 1848", "document": {"contenu": "« L'esclavage sera entièrement aboli dans toutes les colonies et possessions françaises, deux mois après la promulgation du présent décret dans chacune d'elles. »", "source": "Décret du gouvernement provisoire, 27 avril 1848."},
                 "questions": [{"q": "Que décide ce texte ?", "type": "court", "rep": "l'abolition de l'esclavage dans toutes les colonies françaises", "pts": 1},
                               {"q": "Quand l'abolition prend-elle effet dans chaque colonie ?", "type": "court", "rep": "deux mois après la promulgation du décret dans cette colonie", "pts": 1},
                               {"q": "Qui a présidé la commission qui a préparé ce décret ?", "type": "court", "rep": "Victor Schœlcher", "pts": 1}]},
                {"titre": "Les chiffres de la traite française", "document": {"contenu": "Entre 1551 et 1875, les navires français ont mené 4 118 expéditions et transporté 1 381 404 captifs, soit environ 11 % de la traite atlantique. Nantes a armé 44 % de ces expéditions.", "source": "BnF, France-Amériques, d'après la base Slave Voyages."},
                 "questions": [{"q": "Combien de captifs les navires français ont-ils transportés ?", "type": "court", "rep": "1 381 404, soit plus de 1,3 million", "pts": 1},
                               {"q": "Quel port a armé le plus d'expéditions ?", "type": "court", "rep": "Nantes (44 %)", "pts": 1},
                               {"q": "Pourquoi les historiens comptent-ils avec tant de soin ?", "type": "court", "rep": "pour mesurer l'ampleur du crime et ne pas oublier les victimes", "pts": 1}]}]},
}


def main(dest):
    json.dump(DIALOGUES, open(os.path.join(dest, "dialogues.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(EVAL, open(os.path.join(dest, "evaluations.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
