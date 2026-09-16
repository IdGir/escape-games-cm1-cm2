"""Données de démarrage : classes, élèves, banque de textes.

Tout est supprimable depuis le module Enseignant (bouton « Effacer les données
de démonstration »).
"""
import database as db

CLASSES_DEMO = [
    ("CM1 A", "CM1"),
    ("CM2 B", "CM2"),
]

ELEVES_DEMO = {
    "CM1 A": ["Lina", "Noah", "Emma", "Gabriel", "Jade", "Louis", "Chloé", "Adam"],
    "CM2 B": ["Sarah", "Ethan", "Manon", "Nathan", "Léa", "Hugo", "Camille", "Lucas"],
}

# (titre, niveau, texte_fautif, texte_corrigé)
#
# Le corrigé est INDISPENSABLE : c'est lui qui permet à l'application de savoir,
# sans aucune ambiguïté, quels mots sont réellement fautifs. Sans corrigé, on
# retombe sur des règles qui peuvent signaler des mots pourtant justes.
# Le corrigé n'est jamais montré à l'élève.
TEXTES_CORRECTION = [
    ("La récréation", 1,
     "les enfant joue dans la cour. il von au préau parceque il pleut. "
     "la maitresse surveille les élève",
     "Les enfants jouent dans la cour. Ils vont au préau parce qu'il pleut. "
     "La maîtresse surveille les élèves."),

    ("Le marché du samedi", 2,
     "Tous les samedi, ma mère va o marché. elle achète des légume frais est "
     "du pain. Les commerçant l'appelle par son prénom. je l'accompagne souven",
     "Tous les samedis, ma mère va au marché. Elle achète des légumes frais et "
     "du pain. Les commerçants l'appellent par son prénom. Je l'accompagne souvent."),

    ("Une sortie au musée", 3,
     "Hier, la classe a visité le musé de la ville. Les élève on découvert des "
     "tableaux très ancien. le guide nous à expliqué comment les peintres "
     "travaillait. Nous avon beaucoup aimé cette sortie",
     "Hier, la classe a visité le musée de la ville. Les élèves ont découvert des "
     "tableaux très anciens. Le guide nous a expliqué comment les peintres "
     "travaillaient. Nous avons beaucoup aimé cette sortie."),

    ("L'orage", 3,
     "le ciel est devenu tout noir. Des éclair ont déchiré les nuage , puis le "
     "tonnerre a grondé. les habitant se son réfugié dans leur maison. La pluie "
     "tombait très fort",
     "Le ciel est devenu tout noir. Des éclairs ont déchiré les nuages, puis le "
     "tonnerre a grondé. Les habitants se sont réfugiés dans leur maison. La pluie "
     "tombait très fort."),

    ("Le projet de la classe", 4,
     "Nous préparon une exposition sur les volcan. chaque groupe doit faire une "
     "affiche. Les élève de CM2 nous aide a chercher des information. le directeur "
     "a promis d'inviter les parent le jour de la présentation",
     "Nous préparons une exposition sur les volcans. Chaque groupe doit faire une "
     "affiche. Les élèves de CM2 nous aident à chercher des informations. Le "
     "directeur a promis d'inviter les parents le jour de la présentation."),

    # ---------------- CM1 (niveaux 1 à 2) ----------------
    ("Mon petit chien", 1,
     "mon chien s'appelle filou. il a de grande oreille et une queue tout blanche. "
     "le matin, il cour dans le jardin. je l'aime beaucou",
     "Mon chien s'appelle Filou. Il a de grandes oreilles et une queue toute blanche. "
     "Le matin, il court dans le jardin. Je l'aime beaucoup."),

    ("À la piscine", 2,
     "le mercredi, nous allon à la piscine avec la classe. les garçon plongent du "
     "petit plongeoir. moi, je nage avec une frite. le maitre nage nous surveille est "
     "nous encourage",
     "Le mercredi, nous allons à la piscine avec la classe. Les garçons plongent du "
     "petit plongeoir. Moi, je nage avec une frite. Le maître nageur nous surveille et "
     "nous encourage."),

    ("La cabane", 2,
     "Pendant les vacance, mon cousin et moi avons construit une cabane. nous avons "
     "utiliser des vieille planche. la cabane est caché derrière les arbre. nous y "
     "jouons tout les après-midi",
     "Pendant les vacances, mon cousin et moi avons construit une cabane. Nous avons "
     "utilisé de vieilles planches. La cabane est cachée derrière les arbres. Nous y "
     "jouons tous les après-midi."),

    # ---------------- CM2 (niveaux 3 à 5) ----------------
    ("La légende du château", 3,
     "on raconte qu'un chevalier habitai autrefois ce vieux château. les habitant du "
     "village disent qu'il protégai les pauvres. aujourd'hui, il ne reste que des ruine, "
     "mais la légende continue de vivre",
     "On raconte qu'un chevalier habitait autrefois ce vieux château. Les habitants du "
     "village disent qu'il protégeait les pauvres. Aujourd'hui, il ne reste que des ruines, "
     "mais la légende continue de vivre."),

    ("Une expérience en sciences", 4,
     "Ce matin, nous avons fait une expérience sur l'eau. la maitresse a versé du sel "
     "dans un verre est nous avons observé. le sel a disparu peu à peu : on dit qu'il "
     "c'est dissous. les élève on noté leurs observation dans le cahier",
     "Ce matin, nous avons fait une expérience sur l'eau. La maîtresse a versé du sel "
     "dans un verre et nous avons observé. Le sel a disparu peu à peu : on dit qu'il "
     "s'est dissous. Les élèves ont noté leurs observations dans le cahier."),

    ("Le voyage de fin d'année", 5,
     "la semaine prochaine, toute l'école partirat en voyage à la montagne. les "
     "enseignant on préparé un programme passionnant : randonné, visite d'une ferme est "
     "veillée. chaque élève doit emmener un sac à dos, des chaussure solide et un "
     "pique-nique. nous somme tous très impatient de découvrir ces paysage",
     "La semaine prochaine, toute l'école partira en voyage à la montagne. Les "
     "enseignants ont préparé un programme passionnant : randonnée, visite d'une ferme et "
     "veillée. Chaque élève doit emmener un sac à dos, des chaussures solides et un "
     "pique-nique. Nous sommes tous très impatients de découvrir ces paysages."),
]

# (titre, niveau, contenu) — le nombre de mots est calculé automatiquement.
TEXTES_FLUENCE = [
    # ---------------- Niveau 1 (phrases courtes, mots fréquents) ----------------
    ("Le chat de Lila", 1,
     "Lila a un chat. Il est tout noir. Le chat dort sur le lit. "
     "Il aime le lait. Lila lui donne à manger. Le chat ronronne. "
     "Il est très doux. Lila le caresse. Le soir, le chat sort. "
     "Il revient le matin. Lila est contente."),
    ("À l'école", 1,
     "Je vais à l'école. Je prends mon sac. Dans mon sac, il y a mon cahier. "
     "La maîtresse dit bonjour. Nous chantons une chanson. Puis nous écrivons. "
     "À midi, nous mangeons. Après, nous jouons dans la cour. "
     "Le soir, je rentre chez moi."),
    ("Le jardin", 1,
     "Papi a un jardin. Il y a des fleurs. Il y a aussi des carottes. "
     "Papi arrose les plantes. Un oiseau chante. Le soleil brille. "
     "Je ramasse une pomme. Elle est rouge. Je la mange. Elle est bonne."),

    # ---------------- Niveau 2 ----------------
    ("La rentrée de Tom", 2,
     "Ce matin, Tom se lève très tôt. C'est le jour de la rentrée. "
     "Il enfile son pantalon neuf et prend son cartable. Sa mère l'accompagne "
     "jusqu'au portail de l'école. Dans la cour, Tom cherche ses copains. "
     "Il aperçoit Sami près du grand marronnier. Les deux garçons se sourient. "
     "La cloche sonne et tout le monde se range en silence. "
     "La nouvelle maîtresse les attend devant la porte de la classe."),
    ("Une journée de pluie", 2,
     "Depuis le matin, la pluie tombe sans arrêt sur le village. "
     "Les gouttes glissent le long des vitres et forment de petites rivières. "
     "Dans la maison, Léa a sorti ses crayons de couleur. "
     "Elle dessine un immense arc-en-ciel au-dessus des toits. "
     "Son petit frère construit une cabane avec des coussins. "
     "Maman prépare un chocolat chaud dans la cuisine. "
     "Finalement, cette journée grise devient très agréable."),
    ("Le marché", 2,
     "Chaque samedi, le marché s'installe sur la place du village. "
     "Les marchands déballent leurs cageots de fruits et de légumes. "
     "Une bonne odeur de pain chaud flotte dans l'air. "
     "Mamie choisit des tomates bien mûres et un morceau de fromage. "
     "Le poissonnier crie très fort pour attirer les clients. "
     "Je porte le panier, qui devient de plus en plus lourd. "
     "Sur le chemin du retour, nous croisons notre voisine."),

    # ---------------- Niveau 3 ----------------
    ("La sortie au musée", 3,
     "Mardi dernier, notre classe s'est rendue au musée d'histoire naturelle. "
     "Dès l'entrée, un immense squelette de dinosaure nous a stupéfaits. "
     "Le guide nous a expliqué que cet animal vivait il y a des millions d'années. "
     "Nous avons ensuite observé des insectes minuscules à travers une loupe. "
     "Dans la salle suivante, des minéraux scintillaient sous les projecteurs. "
     "Chacun devait remplir un questionnaire tout au long de la visite. "
     "Au moment de repartir, personne n'avait envie de quitter les lieux. "
     "Dans le car, nous avons comparé nos réponses en riant."),
    ("L'orage sur la colline", 3,
     "Le ciel s'assombrissait rapidement au-dessus de la colline. "
     "Un vent violent secouait les branches des vieux chênes. "
     "Soudain, un éclair déchira les nuages et illumina toute la vallée. "
     "Le tonnerre gronda quelques secondes plus tard, effrayant les animaux. "
     "Les randonneurs pressèrent le pas pour rejoindre le refuge. "
     "La pluie se mit à tomber avec une force impressionnante. "
     "Trempés mais soulagés, ils poussèrent enfin la porte du chalet. "
     "Autour du feu, chacun raconta sa version de l'aventure."),
    ("Le potager de l'école", 3,
     "Depuis le mois de mars, les élèves entretiennent un potager derrière l'école. "
     "Ils ont d'abord retourné la terre avec des bêches et des râteaux. "
     "Ensuite, ils ont semé des radis, des salades et quelques plants de tomates. "
     "Chaque matin, deux volontaires viennent arroser les cultures. "
     "La directrice a installé un composteur près de la clôture. "
     "Les vers de terre y transforment les épluchures en engrais naturel. "
     "En juin, la récolte sera partagée entre toutes les familles."),

    # ---------------- Niveau 4 ----------------
    ("Le phare du bout du monde", 4,
     "Perché sur un rocher battu par les vagues, le phare veillait depuis un siècle. "
     "Son faisceau tournait inlassablement, perçant la brume épaisse de l'automne. "
     "Le gardien, un homme taciturne, connaissait chaque marche de l'escalier "
     "en colimaçon. Il notait consciencieusement, dans un carnet jauni, la "
     "direction du vent et la hauteur des marées. Les pêcheurs du port assuraient "
     "que cette lumière leur avait sauvé la vie plus d'une fois. "
     "Pourtant, l'administration envisageait désormais d'automatiser l'installation. "
     "Le vieil homme redoutait ce jour où le silence remplacerait le grincement "
     "familier des mécanismes."),
    ("Une découverte scientifique", 4,
     "Les chercheurs travaillaient depuis plusieurs années sur cette hypothèse "
     "audacieuse. Leurs expériences, répétées inlassablement, n'avaient jusqu'ici "
     "donné aucun résultat convaincant. Un matin pourtant, une jeune doctorante "
     "remarqua une anomalie sur l'un des relevés. La courbe présentait une "
     "irrégularité que personne n'avait su expliquer auparavant. "
     "L'équipe entière se pencha sur ce phénomène inattendu. "
     "Après des semaines de vérifications rigoureuses, la conclusion s'imposa : "
     "la théorie initiale devait être entièrement reconsidérée. "
     "La publication de leurs travaux bouleversa la communauté scientifique."),
    ("La cité engloutie", 4,
     "Les plongeurs descendaient lentement le long de la paroi rocheuse. "
     "À mesure qu'ils s'enfonçaient, la lumière du soleil devenait bleutée, "
     "presque irréelle. Soudain, des formes géométriques apparurent dans la pénombre. "
     "Il s'agissait manifestement de colonnes taillées par la main de l'homme. "
     "L'archéologue de l'expédition sentit son cœur s'emballer d'excitation. "
     "Cette cité, mentionnée dans quelques manuscrits anciens, existait donc vraiment. "
     "Il faudrait des années de fouilles minutieuses pour percer ses secrets."),

    # ---------------- Niveau 5 ----------------
    ("Le procès du perroquet", 5,
     "L'affaire, aussi saugrenue qu'inextricable, occupait le tribunal depuis l'aube. "
     "Un perroquet, unique témoin d'un cambriolage nocturne, répétait inlassablement "
     "une phrase incompréhensible que nul n'était parvenu à déchiffrer. "
     "L'avocat de la défense, homme d'une éloquence redoutable, plaidait "
     "l'irrecevabilité d'un tel témoignage. Le procureur, imperturbable, "
     "rétorquait que la justice ne saurait négliger le moindre indice. "
     "Dans la salle bondée, les murmures enflaient à chaque intervention. "
     "Le juge, excédé par ce tumulte incessant, menaça de faire évacuer l'assistance. "
     "C'est alors que l'oiseau, dans un silence enfin revenu, prononça distinctement "
     "le nom du coupable."),
    ("L'horloger de la rue étroite", 5,
     "Dans son échoppe encombrée d'engrenages et de balanciers, l'horloger "
     "poursuivait une œuvre obstinée. Depuis quarante ans, il s'efforçait de "
     "concevoir un mécanisme capable de mesurer non pas les heures, mais les "
     "hésitations. Ses contemporains le tenaient pour un excentrique inoffensif, "
     "voire pour un illuminé irrécupérable. Lui persistait, courbé sous sa loupe, "
     "ajustant des rouages d'une finesse extraordinaire. "
     "Chaque soir, la lueur vacillante de sa lampe témoignait de son acharnement. "
     "Nul ne sut jamais s'il était parvenu à ses fins, car l'échoppe ferma "
     "brusquement un matin d'hiver, sans explication ni adieu."),
    ("La bibliothèque infinie", 5,
     "On racontait que cette bibliothèque contenait tous les livres qui avaient "
     "été écrits, ainsi que ceux qui ne le seraient jamais. Ses couloirs "
     "s'enfonçaient dans une obscurité vertigineuse, sans que nul n'en eût "
     "jamais atteint l'extrémité. Les rares visiteurs revenaient bouleversés, "
     "incapables de décrire précisément ce qu'ils y avaient contemplé. "
     "Certains prétendaient y avoir lu le récit exact de leur propre existence, "
     "jusqu'à sa dernière ligne. D'autres, plus prudents, refusaient d'ouvrir "
     "le moindre volume, redoutant une révélation insoutenable. "
     "Le bibliothécaire, quant à lui, souriait de ces légendes sans jamais "
     "les démentir tout à fait."),
]


def peupler_si_vide():
    """Insère les données de démonstration uniquement si la base est vide."""
    if not db.liste_classes():
        for nom, niveau in CLASSES_DEMO:
            cid = db.ajouter_classe(nom, niveau)
            for prenom in ELEVES_DEMO.get(nom, []):
                db.ajouter_eleve(prenom, "", cid)

    if not db.liste_textes_correction(actifs_seulement=False):
        for titre, niveau, contenu, corrige in TEXTES_CORRECTION:
            db.ajouter_texte_correction(titre, contenu, niveau, corrige)

    if not db.liste_textes_fluence(actifs_seulement=False):
        for titre, niveau, contenu in TEXTES_FLUENCE:
            db.ajouter_texte_fluence(titre, contenu, niveau)


def reinstaller_textes():
    """Réinstalle uniquement les banques de textes (sans toucher aux élèves)."""
    for titre, niveau, contenu, corrige in TEXTES_CORRECTION:
        db.ajouter_texte_correction(titre, contenu, niveau, corrige)
    for titre, niveau, contenu in TEXTES_FLUENCE:
        db.ajouter_texte_fluence(titre, contenu, niveau)


def completer_textes_correction():
    """Ajoute les textes de correction fournis qui manquent (comparaison par titre).

    Utile pour un enseignant qui utilise déjà l'application : il récupère les
    nouveaux textes tout prêts, AVEC leur corrigé, sans créer de doublon.
    Renvoie le nombre de textes ajoutés.
    """
    existants = {t["titre"].strip().lower()
                 for t in db.liste_textes_correction(actifs_seulement=False)}
    ajoutes = 0
    for titre, niveau, contenu, corrige in TEXTES_CORRECTION:
        if titre.strip().lower() not in existants:
            db.ajouter_texte_correction(titre, contenu, niveau, corrige)
            ajoutes += 1
    return ajoutes
