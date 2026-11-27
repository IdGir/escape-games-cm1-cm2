# -*- coding: utf-8 -*-
"""Données de la version immersive de « Mission géographique » (Année A), au format des salles des jeux de la collection.

    python mission-geo/tests/donnees/gen_escales.py [dossier de sortie]
Sortie par défaut : vingt-mille-lieues/outils/immersif/sources/mission-geo/assets/data/ (enigmes.json, dialogues.json, lecons.json),
lue ensuite par migrer-jeu.py. La version classique (mission-geo/js/donnees/*.js) n'est ni lue ni modifiée par le jeu immersif :
ce script en reprend les activités, transformées en énigmes corrigeables (voir mission-geo/REFONTE-IMMERSIVE.md, § 2).
Une escale = une séance (séance N ↔ escale N). Étape P1 : séances 1 à 5 (période 1, « L'organisation du territoire français ») ; étape P2 : séances 6 à 8 (littoral touristique, inégalités dans le monde) ; étapes P3-P4 : séances 9 à 13 (se nourrir : pratiques alimentaires, produits, chaîne de production, kilomètres alimentaires ; fleuves et massifs).
Les phrases des fiches viennent de fiches.py (reprises mot pour mot par les justifications des grades Géographe et Chef de mission).
"""
import json, os, sys
import fiches as F
import schemas as S

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
SORTIE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RACINE, "vingt-mille-lieues", "outils", "immersif", "sources", "mission-geo", "assets", "data")
BO = "Programme d'histoire-géographie du cycle 3 (BO n° 22 du 28 mai 2026), « L'organisation du territoire français »"
LIVRET = "Livret « Mission géographique », Année A, séance {n}"


def E(id, titre, type, consigne, source, correction, indices, lecon, cm1=None, cm2=None, commun=None, niveaux=None):
    e = {"id": id, "titre": titre, "type": type}
    if niveaux:
        e["niveaux"] = niveaux
    e.update({"consigne": consigne, "source": source, "correction": correction, "indices": indices})
    for k, v in (("cm1", cm1), ("cm2", cm2), ("commun", commun)):
        if v is not None:
            e[k] = v
    e["lecon"] = lecon
    return e


def tri(cols, cartes, type_=None):
    d = {"colonnes": [{"id": i, "titre": t} for i, t in cols], "cartes": [{"txt": t, "col": c} for t, c in cartes]}
    if type_:
        d["type"] = type_
    return d


def qcm(qs, type_=None):
    d = {"questions": [{"q": q, "options": o, "bonne": b, "explication": x} for q, o, b, x in qs]}
    if type_:
        d["type"] = type_
    return d


def plan(titre, cases, etiquettes=None, colonnes=2):
    d = {"titre": titre, "colonnes": colonnes, "cases": [{"libelle": l, "reponse": r} for l, r in cases]}
    if etiquettes:
        d["etiquettes"] = etiquettes
    return d


def lettres(cible, texte):
    return {"cible": list(cible), "texte": "<p>" + texte + "</p>"}


def L(c):
    return f"<b data-l='{c.upper()}'>{c}</b>"


# ============================================================================ ESCALE 1 — Le grand départ
E1 = [
    E("1-1", "Les démarches de l'agent", "association",
      {"cm1": "Avant de partir, le Professeur Atlas te confie une liste de démarches. Relie chaque démarche au lieu de la commune où tu dois aller : clique sur une démarche, puis sur le bon lieu.",
       "cm2": "Le Professeur Atlas te confie sept démarches. Relie chacune au lieu de la commune où elle se fait. Réfléchis à ce que l'on vient chercher dans chaque bâtiment."},
      LIVRET.format(n=1) + " ; " + BO,
      "On demande une carte d'identité à la mairie, on obtient un certificat médical au cabinet médical, on emprunte un guide à la bibliothèque, "
      "on s'entraîne à courir au parc, on achète une trousse de secours à la pharmacie, un goûter à la boulangerie, et l'on récupère ses cahiers à l'école.",
      {"cm1": ["On ne se soigne pas à la boulangerie !", "Les papiers officiels se demandent à la mairie.", "On emprunte des livres sans les acheter."],
       "cm2": ["Demande-toi : qui travaille dans ce bâtiment ?", "La pharmacie vend des médicaments et du matériel de soin.", "Le parc est un lieu de loisirs : on peut y courir."]},
      "l01",
      cm1={"paires": [{"g": "Demander une carte d'identité", "d": "la mairie"}, {"g": "Faire un certificat médical", "d": "le cabinet médical"},
                      {"g": "Emprunter un guide de voyage", "d": "la bibliothèque"}, {"g": "Acheter un goûter", "d": "la boulangerie"},
                      {"g": "Récupérer ses cahiers", "d": "l'école"}]},
      cm2={"paires": [{"g": "Demander une carte d'identité", "d": "la mairie"}, {"g": "Faire un certificat médical", "d": "le cabinet médical"},
                      {"g": "Emprunter un guide de voyage", "d": "la bibliothèque"}, {"g": "S'entraîner à la course à pied", "d": "le parc"},
                      {"g": "Acheter une trousse de secours", "d": "la pharmacie"}, {"g": "Acheter un goûter", "d": "la boulangerie"},
                      {"g": "Récupérer ses devoirs et ses cahiers", "d": "l'école"}]}),
    E("1-2", "À quoi sert chaque lieu ?", "tri",
      {"cm1": "Sur le plan de la commune, chaque lieu a une fonction. Range chaque lieu dans la colonne de sa fonction : clique sur une carte, puis sur une colonne.",
       "cm2": "Range chaque lieu de la commune selon sa fonction. Attention : plusieurs lieux peuvent avoir la même fonction."},
      LIVRET.format(n=1) + " ; " + BO,
      "La mairie et la poste ont une fonction administrative ; l'école et la bibliothèque, une fonction éducative ; la boulangerie et le supermarché, "
      "une fonction commerciale ; le cabinet médical et la pharmacie, une fonction de santé ; le parc et le stade, une fonction de loisirs.",
      {"cm1": ["À la mairie, on fait des papiers officiels : c'est administratif.", "Deux lieux servent à se soigner.", "Le parc sert à se détendre : ce sont les loisirs."],
       "cm2": ["La poste rend un service officiel, comme la mairie.", "Éducatif : on y apprend.", "Commercial : on y achète quelque chose."]},
      "l01",
      cm1=tri([("adm", "Administrative"), ("edu", "Éducative"), ("com", "Commerciale"), ("san", "Santé"), ("loi", "Loisirs")],
              [("la mairie", "adm"), ("l'école", "edu"), ("la boulangerie", "com"), ("le cabinet médical", "san"), ("la pharmacie", "san"), ("le parc", "loi")]),
      cm2=tri([("adm", "Administrative"), ("edu", "Éducative"), ("com", "Commerciale"), ("san", "Santé"), ("loi", "Loisirs")],
              [("la mairie", "adm"), ("la poste", "adm"), ("l'école", "edu"), ("la bibliothèque", "edu"), ("la boulangerie", "com"), ("le supermarché", "com"),
               ("le cabinet médical", "san"), ("la pharmacie", "san"), ("le parc", "loi"), ("le stade", "loi")])),
    E("1-3", "Les lettres marquées", "lettres",
      {"cm1": "Le Professeur Atlas a marqué des lettres en couleur dans sa liste. Clique sur les bonnes lettres pour former, dans l'ordre, le nom de la ville où tu es attendu (5 lettres). Attention, deux lettres sont des pièges.",
       "cm2": "Dans le message du Professeur Atlas, des lettres sont en couleur. Forme le nom de la ville du rendez-vous (5 lettres, une préfecture de Bourgogne-Franche-Comté). Plusieurs lettres sont des pièges."},
      LIVRET.format(n=1),
      "Les lettres D, I, J, O et N forment DIJON : c'est là que les autres agents t'attendent. Dijon est la préfecture de la Côte-d'Or.",
      {"cm1": ["La ville commence par D.", "Elle est célèbre pour sa moutarde.", "D, I, J… il reste deux lettres."],
       "cm2": ["C'est la préfecture de la Côte-d'Or.", "La ville commence par D et finit par N.", "Les lettres M et A sont des pièges."]},
      "l01",
      cm1=lettres("DIJON", f"Liste des démarches : passer à l'éc{L('o')}le, puis à la {L('m')}airie. Aller au cabinet mé{L('d')}ical, puis à la boula{L('n')}gerie. "
                           f"Passer à la ph{L('a')}rmacie, à la b{L('i')}bliothèque, et finir par le parc, pour les {L('j')}eux et la course."),
      cm2=lettres("DIJON", f"Agent, votre mission commence ici, dans votre commune. Récupérez vos cahiers à l'éc{L('o')}le et vos papiers à la {L('m')}airie. "
                           f"Le cabinet mé{L('d')}ical vous remettra un certificat ; la boula{L('n')}gerie, votre goûter. Passez à la ph{L('a')}rmacie pour la trousse de secours, "
                           f"puis à la b{L('i')}bliothèque pour le guide. Entraînez-vous au parc : ses {L('j')}eux et ses allées sont parfaits. {L('r')}endez-vous ensuite à la gare.")),
    E("1-4", "Les services publics", "qcm",
      "Avant de fermer sa valise, le Professeur Atlas vérifie que tu connais bien ta commune. Réponds aux questions, puis vérifie.",
      LIVRET.format(n=1) + " ; DGCL, « Les structures territoriales au 1er janvier 2026 » ; " + BO,
      "Un service public rend un service à tous les habitants, sans que l'on paie ce que l'on vient chercher : c'est le cas de la mairie, de l'école publique "
      "et de la bibliothèque municipale. La commune est dirigée par un maire. On parle souvent de village en dessous de 2 000 habitants, de ville au-delà.",
      {"cm2": ["Un commerce vend quelque chose ; un service public rend un service à tous.", "Le maire est élu par le conseil municipal.", "Le seuil habituel est de 2 000 habitants."]},
      "l01", niveaux=["CM2"],
      commun=qcm([("Lequel de ces lieux est un service public de la commune ?", ["la bibliothèque municipale", "la boulangerie", "la pharmacie", "le supermarché"], 0,
                   "On y emprunte des livres sans les acheter : elle sert à tous les habitants."),
                  ("Qui dirige la commune ?", ["le maire", "le préfet", "le président de la région", "le directeur de l'école"], 0,
                   "Le maire est élu par le conseil municipal, lui-même élu par les habitants."),
                  ("Une commune de 8 000 habitants est plutôt…", ["une ville", "un village", "un hameau", "un département"], 0,
                   "Au-delà de 2 000 habitants, on parle souvent de ville."),
                  ("Combien y a-t-il de communes en France au 1er janvier 2026 ?", ["34 875", "101", "3 487", "348 750"], 0,
                   "La commune est le plus petit territoire administratif.")])),
]

# ============================================================================ ESCALE 2 — Direction Dijon !
E2 = [
    E("2-1", "Qui décide ?", "qcm",
      {"cm1": "Léna attend les agents à Dijon. Elle a noté des décisions à prendre. Range chaque décision chez celui qui décide : la commune, le département ou la région.",
       "cm2": "Léna t'attend au point de rendez-vous. Réponds à ses questions sur Dijon et sur le découpage du territoire, puis vérifie."},
      LIVRET.format(n=2) + " ; " + BO,
      "Les écoles dépendent de la commune, les collèges du département, les lycées et les TER de la région. Le rendez-vous a lieu au palais des ducs de Bourgogne, "
      "place de la Libération : il abrite aujourd'hui la mairie et le musée des Beaux-Arts. Dijon est la préfecture de la Côte-d'Or et le chef-lieu de la région.",
      {"cm1": ["L'école → la commune.", "Le collège → le département.", "Le lycée → la région : plus l'élève grandit, plus le territoire est grand."],
       "cm2": ["Le plus grand bâtiment de la place de la Libération.", "Une préfecture est la ville principale d'un département.", "Sept continents, treize régions en métropole."]},
      "l02",
      cm1=tri([("com", "La commune"), ("dep", "Le département"), ("reg", "La région")],
              [("Rénover une école élémentaire", "com"), ("Organiser la collecte des déchets", "com"), ("Construire un collège", "dep"),
               ("Agrandir un lycée", "reg"), ("Créer une ligne de TER", "reg")], type_="tri"),
      cm2=qcm([("Où les agents se retrouvent-ils, place de la Libération ?", ["au palais des ducs de Bourgogne", "dans les caves voûtées", "au musée Magnin", "à l'hôtel de Vogüé"], 0,
                "Le palais abrite aujourd'hui la mairie et le musée des Beaux-Arts."),
               ("Dijon est la préfecture de quel département ?", ["la Côte-d'Or", "le Doubs", "la Nièvre", "le Jura"], 0, "Le numéro de la Côte-d'Or est le 21."),
               ("Combien de régions compte la France métropolitaine ?", ["13", "18", "22", "96"], 0, "Avec l'outre-mer, on en compte 18."),
               ("Combien de continents compte-t-on habituellement ?", ["7", "5", "6", "13"], 0, "L'Antarctique compte parmi eux.")])),
    E("2-2", "La carte de Léna", "plan",
      {"cm1": "Léna déplie un planisphère. Place le nom de chaque continent sur le bon repère : clique sur une étiquette, puis sur la case du repère." + S.planisphere(range(7)),
       "cm2": "Léna déplie la carte des régions de France métropolitaine. Place chaque région sur son numéro. Commence par la région de ton école, puis par ses voisines." + S.regions()},
      LIVRET.format(n=2) + " ; " + BO + " ; fonds de carte dessinés par script (mission-geo/js/cartes.js)",
      "Les sept continents sont l'Amérique du Nord, l'Amérique du Sud, l'Europe, l'Afrique, l'Asie, l'Océanie et l'Antarctique. La France métropolitaine compte 13 régions ; "
      "Dijon est en Bourgogne-Franche-Comté.",
      {"cm1": ["L'Europe est au centre, en haut.", "L'Afrique est juste en dessous de l'Europe.", "L'Antarctique est tout en bas, autour du pôle Sud."],
       "cm2": ["Repère d'abord la Bretagne (à l'ouest) et la Corse (l'île).", "Les Hauts-de-France sont tout au nord.", "Dijon est dans la région numéro 8."]},
      "l02",
      cm1=plan("Le planisphère de Léna", [(f"Repère {i + 1}", c[0]) for i, c in enumerate(S.CONTINENTS)], colonnes=2),
      cm2=plan("Les régions de France métropolitaine", [(f"Repère {i + 1}", r) for i, r in enumerate(S.REGIONS)], colonnes=3)),
    E("2-3", "Le passeport de la France", "trous",
      {"cm1": "Complète la carte d'identité de la France : clique sur une étiquette, puis sur le trou où elle va. Deux étiquettes sont en trop.",
       "cm2": "Complète la carte d'identité de la France. Lis bien les nombres : plusieurs étiquettes sont des pièges."},
      LIVRET.format(n=2) + " ; Insee, bilan démographique 2025 ; IGN ; " + BO,
      "La France est un pays d'Europe. Sa capitale est Paris, sa langue le français, sa monnaie l'euro, son hymne La Marseillaise et sa devise « Liberté, Égalité, Fraternité ». "
      "La France métropolitaine mesure environ 552 000 km² ; la France compte environ 69 millions d'habitants.",
      {"cm1": ["La France est sur le même continent que l'Allemagne.", "Notre monnaie est aussi celle de l'Espagne.", "L'hymne national porte le nom d'une grande ville du sud."],
       "cm2": ["La capitale n'est pas la plus grande ville du sud.", "69 millions : des millions, pas des milliards.", "552 000 km² : des kilomètres carrés, pas des mètres carrés."]},
      "l02",
      cm1={"texte": "<p>Continent : [[Europe]]. Capitale : [[Paris]]. Monnaie : [[l'euro]]. Hymne : [[La Marseillaise]]. Devise : [[Liberté, Égalité, Fraternité]].</p>",
           "etiquettes": ["Europe", "Paris", "l'euro", "La Marseillaise", "Liberté, Égalité, Fraternité", "Asie", "le dollar"]},
      cm2={"texte": "<p>Continent : [[Europe]]. Capitale : [[Paris]]. Langue : [[français]]. Monnaie : [[l'euro]]. Superficie de la métropole : environ [[552 000 km²]]. "
                    "Population : environ [[69 millions]] d'habitants. Hymne : [[La Marseillaise]].</p>",
           "etiquettes": ["Europe", "Paris", "français", "l'euro", "552 000 km²", "69 millions", "La Marseillaise", "Marseille", "552 000 m²", "7 milliards", "le franc"]}),
    E("2-4", "Les décisions de Léna", "tri",
      "Léna a noté des décisions prises dans la région. Range chacune chez celui qui décide : la commune, le département ou la région.",
      LIVRET.format(n=2) + " ; " + BO,
      "La commune s'occupe des écoles, de l'eau et des déchets ; le département des collèges, de l'aide sociale et des routes départementales ; "
      "la région des lycées et des trains régionaux (TER).",
      {"cm2": ["Écoles = commune, collèges = département, lycées = région.", "Les trains régionaux s'appellent les TER.", "Les routes départementales portent bien leur nom."]},
      "l02", niveaux=["CM2"],
      commun=tri([("com", "La commune"), ("dep", "Le département"), ("reg", "La région")],
                 [("Rénover une école élémentaire", "com"), ("Organiser la collecte des déchets", "com"), ("Construire un collège", "dep"),
                  ("Entretenir une route départementale", "dep"), ("Agrandir un lycée", "reg"), ("Créer une ligne de TER", "reg")])),
]

# ============================================================================ ESCALE 3 — Clamecy
E3 = [
    E("3-1", "Vivre à Clamecy", "tri",
      {"cm1": "Malik s'est installé à Clamecy pour passer inaperçu. Il a noté ce qu'il pense de la vie à la campagne. Range chaque carte : avantage ou inconvénient ?",
       "cm2": "Malik t'envoie une vue aérienne d'un bourg, redessinée en plan. Place chaque élément sur le bon repère. Une étiquette est en trop." + S.village(range(7))},
      LIVRET.format(n=3) + " ; " + BO + " ; banatic.interieur.gouv.fr (Clamecy)",
      "Vivre à la campagne, c'est profiter de la nature, du calme, de logements plus grands et moins chers. Mais il y a peu de commerces, de services et d'emplois, "
      "peu de transports en commun, et la voiture est souvent indispensable. Dans un bourg, les maisons se serrent autour de l'église, de la mairie et des commerces.",
      {"cm1": ["Un avantage, c'est quelque chose d'agréable.", "Sans bus, il faut une voiture.", "Il y a 3 avantages et 3 inconvénients."],
       "cm2": ["Le centre-bourg est là où les maisons sont les plus serrées.", "L'église a un clocher, au cœur du bourg.", "Le lotissement est un quartier de maisons récentes, à l'écart."]},
      "l03",
      cm1=tri([("a", "Avantages"), ("i", "Inconvénients")],
              [("la proximité de la nature", "a"), ("des logements moins chers", "a"), ("peu de bruit", "a"),
               ("peu de commerces", "i"), ("peu de bus et de trains", "i"), ("une voiture indispensable", "i")]),
      cm2=dict(plan("Le bourg vu du ciel", [(f"Repère {i + 1}", v[0]) for i, v in enumerate(S.VILLAGE)],
                    [v[0] for v in S.VILLAGE] + ["La gare TGV"], colonnes=2), type="plan")),
    E("3-2", "La définition de Malik", "trous",
      {"cm1": "Complète la définition d'une commune rurale. Un mot de la liste est un intrus.",
       "cm2": "Complète la définition d'une commune rurale. Deux mots de la liste sont des intrus."},
      LIVRET.format(n=3) + " ; " + BO,
      "Une commune rurale a une faible densité de population ; elle est marquée par les activités agricoles. Moins de 2 000 habitants : c'est un village ; "
      "une commune rurale plus grande, avec des commerces et des services, est un bourg.",
      {"cm1": ["Rural : peu d'habitants sur beaucoup d'espace.", "La densité y est donc faible.", "L'intrus est le contraire de « faible »."],
       "cm2": ["« Élevée » est le contraire de « faible ».", "À la campagne, on cultive et on élève : ce sont les activités agricoles.", "Le bourg est plus grand que le village."]},
      "l03",
      cm1={"texte": "<p>Une commune rurale est une commune où la [[densité]] de population est [[faible]]. Elle est marquée par les activités [[agricoles]]. "
                    "Avec moins de 2 000 habitants, c'est un [[village]].</p>",
           "etiquettes": ["densité", "faible", "agricoles", "village", "élevée"]},
      cm2={"texte": "<p>Une commune rurale est une commune où la [[densité]] de population est [[faible]]. Elle est marquée par les activités [[agricoles]]. "
                    "Avec moins de 2 000 habitants, c'est un [[village]] ; plus grande, avec des commerces et des services utiles aux villages voisins, c'est un [[bourg]].</p>",
           "etiquettes": ["densité", "faible", "agricoles", "village", "bourg", "élevée", "industrielles"]}),
    E("3-3", "Le calcul des densités", "code",
      {"cm1": "Pour passer inaperçu, Malik doit comprendre combien de personnes vivent ici. Calcule la densité de chaque espace (habitants ÷ km²), puis le total des trois. Écris les nombres, puis ouvre."
              + S.densites(),
       "cm2": "Calcule la densité de chaque espace, le total des trois, puis celle de la ville B : 60 000 habitants sur 40 km². Écris les nombres, puis ouvre."
              + S.densites()},
      LIVRET.format(n=3) + " (espaces A, B, C ; ville B imaginaire)",
      "Espace A : 2 habitants sur 1 km², soit 2 hab/km². Espace B : 4 ÷ 1 = 4 hab/km². Espace C : 2 km sur 2 km font 4 km², et 4 ÷ 4 = 1 hab/km². "
      "Le total vaut 7. Ville B : 60 000 ÷ 40 = 1 500 hab/km², bien plus dense que nos espaces ruraux.",
      {"cm1": ["Densité = habitants ÷ surface en km².", "Espace C : 2 km × 2 km = 4 km².", "Additionne les trois densités : 2 + 4 + 1."],
       "cm2": ["Attention à l'espace C : sa surface est de 4 km².", "60 000 ÷ 40 : commence par 60 000 ÷ 10.", "Le total des trois densités est un nombre à un chiffre."]},
      "l03",
      cm1={"champs": [{"libelle": "Densité de l'espace A (hab/km²)", "valeur": "2", "longueur": 1}, {"libelle": "Densité de l'espace B (hab/km²)", "valeur": "4", "longueur": 1},
                      {"libelle": "Densité de l'espace C (hab/km²)", "valeur": "1", "longueur": 1}, {"libelle": "Total des trois densités", "valeur": "7", "longueur": 1}]},
      cm2={"champs": [{"libelle": "Densité de l'espace A (hab/km²)", "valeur": "2", "longueur": 1}, {"libelle": "Densité de l'espace B (hab/km²)", "valeur": "4", "longueur": 1},
                      {"libelle": "Densité de l'espace C (hab/km²)", "valeur": "1", "longueur": 1}, {"libelle": "Total des trois densités", "valeur": "7", "longueur": 1},
                      {"libelle": "Densité de la ville B (hab/km²)", "valeur": "1500", "longueur": 4}]}),
    E("3-4", "Le carnet de Malik", "vraifaux",
      "Malik relit son carnet avant de quitter Clamecy. Pour chaque phrase, choisis « Vrai » ou « Faux », puis vérifie.",
      LIVRET.format(n=3) + " ; " + BO + " ; banatic.interieur.gouv.fr (Clamecy)",
      "La densité se calcule en divisant le nombre d'habitants par la superficie. Un village de 600 habitants sur 30 km² a une densité de 20 hab/km². "
      "À la campagne, on trouve peu de commerces et la voiture est souvent indispensable. Clamecy est un bourg de la Nièvre, au bord de l'Yonne.",
      {"cm2": ["600 ÷ 30 = 20.", "Une forte densité, c'est beaucoup d'habitants sur peu d'espace.", "Clamecy est dans la Nièvre."]},
      "l03", niveaux=["CM2"],
      commun={"affirmations": [
          {"txt": "Un village de 600 habitants sur 30 km² a une densité de 20 habitants par km².", "vrai": True, "explication": "600 ÷ 30 = 20."},
          {"txt": "Un espace rural a une forte densité de population.", "vrai": False, "explication": "La densité y est faible."},
          {"txt": "Pour calculer une densité, on multiplie les habitants par la superficie.", "vrai": False, "explication": "On divise les habitants par la superficie en km²."},
          {"txt": "À la campagne, la voiture est souvent indispensable.", "vrai": True, "explication": "Les transports en commun y sont rares."},
          {"txt": "Clamecy est un bourg de la Nièvre, au bord de l'Yonne.", "vrai": True, "explication": "Et du canal du Nivernais."}]}),
]

# ============================================================================ ESCALE 4 — Besançon
E4 = [
    E("4-1", "Le métier caché", "lettres",
      {"cm1": "Zoé doit trouver une source qui travaille à Besançon. Le nom de son métier est caché dans le message : clique sur les lettres en couleur pour l'écrire (7 lettres). Trois lettres sont des pièges.",
       "cm2": "Le message de Zoé cache le métier de la source (11 lettres) : clique sur les lettres en couleur pour l'écrire dans l'ordre. Attention aux lettres pièges."},
      LIVRET.format(n=4) + " ; " + BO,
      "La source est un serveur, puis un ambulancier : deux métiers du secteur tertiaire, qui rendent un service aux personnes.",
      {"cm1": ["Ce métier se fait au café ou au restaurant.", "Il commence par S.", "Il apporte les plats et les boissons."],
       "cm2": ["Ce métier conduit des malades à l'hôpital.", "Il commence par A et finit par R.", "Am-bu-lan-cier."]},
      "l04",
      cm1=lettres("SERVEUR", f"La source m'attend près du Doubs, au centre-ville, dans un café. Elle a {L('r')}angé son tablier noir sur une chaise. "
                             f"Elle a déjà tra{L('v')}aillé ce matin : comman{L('d')}es, boiss{L('o')}ns, plats. Elle {L('s')}ourit aux clients, puis {L('e')}ssuie les tables. "
                             f"Elle aime son trav{L('a')}il, même quand il y a beaucoup de bruit. Ce soir, elle r{L('e')}nt{L('r')}era chez elle à pied, sans se presser, par la r{L('u')}e du port."),
      cm2=lettres("AMBULANCIER", f"Changement de plan : la source a changé de métier. Elle conduit les malades vers le CHU. Notez bien : "
                                 f"{L('c')}ouloir, {L('a')}ccueil, {L('n')}uit, {L('i')}nfirmerie, {L('b')}rancard, {L('e')}ntrée, {L('u')}rgences, {L('l')}it, "
                                 f"{L('m')}édecin, {L('r')}adio, {L('a')}nnonce, {L('i')}ci, {L('p')}ortail, {L('t')}rajet.")),
    E("4-2", "Les trois secteurs", "tri",
      {"cm1": "Zoé a rencontré des professionnels de Besançon. Range chaque métier dans son secteur d'activité.",
       "cm2": "Range chaque métier dans son secteur d'activité. Pense à ce que fait vraiment la personne : exploiter la nature, transformer, ou rendre un service."},
      LIVRET.format(n=4) + " ; " + BO,
      "Le secteur primaire exploite la nature (agriculteur, bûcheron), le secondaire transforme (soudeur, boulanger, glacier qui fabrique ses glaces), "
      "le tertiaire rend un service (caissier, infirmier, guide, serveur, consultant).",
      {"cm1": ["Primaire : on exploite la nature.", "Secondaire : on fabrique, on transforme.", "Tertiaire : on rend un service."],
       "cm2": ["Le glacier fabrique ses glaces : il transforme du lait et des fruits.", "Le bûcheron coupe les arbres de la forêt.", "Le consultant conseille des entreprises : c'est un service."]},
      "l04",
      cm1=tri([("p", "Primaire"), ("s", "Secondaire"), ("t", "Tertiaire")],
              [("agriculteur", "p"), ("soudeur", "s"), ("boulanger", "s"), ("caissier", "t"), ("infirmier", "t"), ("guide", "t")]),
      cm2=tri([("p", "Primaire"), ("s", "Secondaire"), ("t", "Tertiaire")],
              [("agriculteur", "p"), ("bûcheron", "p"), ("soudeur", "s"), ("glacier (il fabrique ses glaces)", "s"), ("maçon", "s"),
               ("caissier", "t"), ("infirmier", "t"), ("pédiatre", "t"), ("serveur", "t"), ("consultant", "t")])),
    E("4-3", "Les confidences de la source", "qcm",
      {"cm1": "La source accepte de parler. Réponds à ses deux questions, puis vérifie.",
       "cm2": "La source accepte de parler si tu sais lire son document : « En 1911, près de 40 % des actifs travaillaient dans l'agriculture. En 2024, le tertiaire regroupe 76,6 % des emplois. » Réponds, puis vérifie."},
      LIVRET.format(n=4) + " ; Insee, enquête Emploi 2024 ; ministère de l'Agriculture, CEP (recensement de 1911)",
      "Aujourd'hui, plus de 3 emplois sur 4 sont dans le secteur tertiaire. En 1911, près de 40 % des actifs travaillaient dans l'agriculture. "
      "La phrase de la source, « Ce que vous cherchez n'est plus en Europe », indique que la valise a quitté le continent européen.",
      {"cm1": ["Pense aux métiers rencontrés : la plupart rendent un service.", "« N'est plus en Europe » : elle est sur un autre continent.", "Relis la fiche « La ville »."],
       "cm2": ["76,6 % : plus de 3 sur 4.", "40 % en 1911, environ 2 % aujourd'hui.", "La source parle d'un continent."]},
      "l04",
      cm1=qcm([("Quel secteur emploie le plus de personnes en France aujourd'hui ?", ["le tertiaire", "le primaire", "le secondaire"], 0, "Plus de 3 emplois sur 4."),
               ("La source dit : « Ce que vous cherchez n'est plus en Europe. » Que peux-tu en déduire ?", ["la valise est sur un autre continent", "la valise est à Besançon", "la valise est en France"], 0,
                "Il faut chercher hors d'Europe.")]),
      cm2=qcm([("Quel secteur emploie le plus de personnes en France en 2024 ?", ["le tertiaire", "le primaire", "le secondaire", "aucun : ils sont égaux"], 0, "76,6 % des emplois."),
               ("Comment la part de l'agriculture a-t-elle changé depuis 1911 ?", ["elle a beaucoup baissé", "elle a beaucoup augmenté", "elle n'a pas changé", "elle a doublé"], 0,
                "De près de 40 % à un peu plus de 2 %."),
               ("« Ce que vous cherchez n'est plus en Europe. » Que peux-tu en déduire ?", ["la valise a quitté le continent européen", "la valise est à Dijon", "la valise est en Suisse", "la valise a été détruite"], 0,
                "Il faut chercher sur un autre continent.")])),
    E("4-4", "Où travaille chacun ?", "association",
      "Zoé doit retrouver chaque professionnel sur son lieu de travail. Relie chaque métier au lieu où il s'exerce.",
      LIVRET.format(n=4) + " ; " + BO,
      "Le caissier travaille au centre commercial, l'infirmier au CHU (l'hôpital), le guide dans le centre-ville historique, le consultant dans le quartier d'affaires "
      "et le soudeur à l'atelier de maintenance des trains.",
      {"cm2": ["Le CHU est un grand hôpital.", "Le guide fait visiter les monuments.", "Le consultant travaille dans des bureaux."]},
      "l04", niveaux=["CM2"],
      commun={"paires": [{"g": "le caissier", "d": "le centre commercial"}, {"g": "l'infirmier", "d": "le CHU (l'hôpital)"},
                         {"g": "le guide", "d": "le centre-ville historique"}, {"g": "le consultant", "d": "le quartier d'affaires"},
                         {"g": "le soudeur", "d": "l'atelier de maintenance des trains"}]}),
]

# ============================================================================ ESCALE 5 — La montagne
E5 = [
    E("5-1", "Les mots de la montagne", "association",
      {"cm1": "Hugo, moniteur de ski, t'apprend les mots de la montagne. Relie chaque mot à sa définition.",
       "cm2": "Hugo te teste sur le vocabulaire de la montagne. Relie chaque mot à sa définition."},
      LIVRET.format(n=5) + " ; " + BO,
      "Une piste est un chemin balisé pour descendre à ski ; un chalet, une maison de montagne en bois ; un télésiège, une remontée mécanique où l'on monte assis ; "
      "un torrent, un cours d'eau rapide ; le sommet, le point le plus haut ; une station, un lieu aménagé pour accueillir les touristes.",
      {"cm1": ["Le chalet est en bois.", "On s'assoit sur le télésiège.", "Le sommet est tout en haut."],
       "cm2": ["Le torrent dévale la pente.", "Une station est aménagée pour les touristes.", "La piste est balisée."]},
      "l05",
      cm1={"paires": [{"g": "une piste", "d": "chemin balisé pour descendre à ski"}, {"g": "un chalet", "d": "maison de montagne en bois"},
                      {"g": "un télésiège", "d": "remontée mécanique où l'on monte assis"}, {"g": "le sommet", "d": "point le plus haut d'une montagne"}]},
      cm2={"paires": [{"g": "une piste", "d": "chemin balisé pour descendre à ski"}, {"g": "un chalet", "d": "maison de montagne en bois"},
                      {"g": "un télésiège", "d": "remontée mécanique où l'on monte assis"}, {"g": "un torrent", "d": "cours d'eau rapide qui dévale la montagne"},
                      {"g": "le sommet", "d": "point le plus haut d'une montagne"}, {"g": "une station", "d": "lieu aménagé pour accueillir les touristes"}]}),
    E("5-2", "Avec ou sans neige", "tri",
      {"cm1": "Hugo prépare le programme de la semaine. Range chaque loisir : se pratique-t-il sur la neige ou sans neige ?",
       "cm2": "Range les dix loisirs de la montagne : sur la neige, ou sans neige ?"},
      LIVRET.format(n=5) + " ; " + BO,
      "Le ski, le snowboard, la raquette et le biathlon se pratiquent sur la neige ; la randonnée, l'escalade, le trail, le parapente, le rafting et le paddle, sans neige. "
      "La montagne est un espace de loisirs été comme hiver.",
      {"cm1": ["Le ski a besoin de neige.", "La randonnée se fait sur un sentier.", "Le rafting se fait sur une rivière."],
       "cm2": ["Le biathlon associe ski de fond et tir.", "Le parapente vole au-dessus des pentes.", "Le paddle se pratique sur un lac."]},
      "l05",
      cm1=tri([("n", "Sur la neige"), ("s", "Sans neige")],
              [("le ski", "n"), ("le snowboard", "n"), ("la raquette", "n"), ("la randonnée", "s"), ("l'escalade", "s"), ("le rafting", "s")]),
      cm2=tri([("n", "Sur la neige"), ("s", "Sans neige")],
              [("le ski", "n"), ("le snowboard", "n"), ("la raquette", "n"), ("le biathlon", "n"), ("la randonnée", "s"), ("l'escalade", "s"),
               ("le trail", "s"), ("le parapente", "s"), ("le rafting", "s"), ("le paddle", "s")])),
    E("5-3", "Les photos du séjour", "trous",
      {"cm1": "Hugo a pris des photos dans la station. Complète la légende de chacune. Un mot ne sert à rien : c'est l'intrus.",
       "cm2": "Complète la légende de chaque photo prise dans la station. Un mot de la liste est un intrus."},
      LIVRET.format(n=5) + " ; " + BO,
      "Les files de voitures polluent l'air ; les constructions sur les forêts réduisent la biodiversité ; les mégots polluent les sols ; les canons à neige prélèvent de l'eau ; "
      "les remontées mécaniques consomment de l'énergie. Le mot « écologie », qui désigne une science, est l'intrus.",
      {"cm1": ["Les voitures rejettent des gaz dans l'air.", "Le canon à neige a besoin d'eau.", "Le télésiège fonctionne à l'électricité."],
       "cm2": ["Atmosphérique : qui concerne l'air.", "Biodiversité : l'ensemble des êtres vivants d'un milieu.", "L'intrus désigne une science, pas un effet."]},
      "l05",
      cm1={"texte": "<p>Photo 1 : une file de voitures à l'entrée de la station pollue l'[[air]]. Photo 2 : un canon à neige prélève de l'[[eau]]. "
                    "Photo 3 : le télésiège consomme de l'[[énergie]]. Photo 4 : des mégots polluent les [[sols]].</p>",
           "etiquettes": ["air", "eau", "énergie", "sols", "écologie"]},
      cm2={"texte": "<p>Photo 1 : file de voitures à l'entrée de la station : pollution [[atmosphérique]]. Photo 2 : nouvelle résidence sur un versant boisé : réduction de la [[biodiversité]]. "
                    "Photo 3 : mégots sur les rochers : [[pollution]] des sols. Photo 4 : canon à neige en action : prélèvement d'[[eau]]. "
                    "Photo 5 : télésiège en marche toute la journée : consommation d'[[énergie]].</p>",
           "etiquettes": ["atmosphérique", "biodiversité", "pollution", "eau", "énergie", "écologie"]}),
    E("5-4", "La remarque du skieur", "vraifaux",
      "Au refuge, un skieur montre une carte du monde : « Là où va votre valise, c'est l'hiver quand c'est l'hiver ici. » Pour chaque phrase, choisis « Vrai » ou « Faux ».",
      LIVRET.format(n=5) + " ; " + BO + " ; Office de tourisme de la station des Rousses",
      "Les saisons sont inversées entre les deux hémisphères : si c'est l'hiver au même moment qu'en France, le pays est dans l'hémisphère nord. "
      "Le tourisme crée des emplois, mais les canons à neige prélèvent beaucoup d'eau. La Dôle est un sommet suisse de 1 677 mètres.",
      {"cm2": ["En décembre, c'est l'été en Australie.", "Même saison qu'en France : même hémisphère.", "Le tourisme a des effets positifs et négatifs."]},
      "l05", niveaux=["CM2"],
      commun={"affirmations": [
          {"txt": "Les saisons sont les mêmes dans les deux hémisphères.", "vrai": False, "explication": "Elles sont inversées : en décembre, c'est l'été dans l'hémisphère sud."},
          {"txt": "Si c'est l'hiver là-bas quand c'est l'hiver en France, le pays est dans l'hémisphère nord.", "vrai": True, "explication": "Il a les mêmes saisons que nous."},
          {"txt": "Le tourisme apporte des emplois aux habitants de la montagne.", "vrai": True, "explication": "Moniteurs, saisonniers, hôtels, restaurants."},
          {"txt": "Les canons à neige ne consomment pas d'eau.", "vrai": False, "explication": "Ils prélèvent beaucoup d'eau."},
          {"txt": "Le sommet de la Dôle, à 1 677 mètres, se trouve en Suisse.", "vrai": True, "explication": "Son domaine skiable est relié à la station des Rousses."}]}),
]

def doc(titre, corps):
    """Encadré de document (témoignage, dépliant)."""
    return f"<div class='doc-carnet'><b>{titre}</b> {corps}</div>"


def ordre(items):
    return {"items": [{"txt": t, "rang": i} for i, t in enumerate(items, 1)]}


OT = "Office de tourisme Le Havre Étretat (Clos Lupin, château des Aygues, marché couvert, parc des Roches)"
BO2 = "Programme d'histoire-géographie du cycle 3 (BO n° 22 du 28 mai 2026)"

# ============================================================================ ESCALE 6 — Étretat, station balnéaire
DOC_ETRETAT = doc("Étretat, mode d'emploi.", "Randonnée sur le sentier GR21, en haut des falaises ; paddle ou kayak au pied des arches ; balade en vélo-rail. "
                  "À visiter : le Clos Lupin, maison de l'écrivain Maurice Leblanc ; le château des Aygues, ancienne résidence d'été des reines d'Espagne ; "
                  "le marché couvert et ses boutiques ; le parc des Roches, espace de loisirs pour les familles.")
DOC_FREQ = doc("Témoignage recueilli par Inès.", "« L'été, le front de mer est noir de monde et des kilomètres de voitures cherchent une place. "
               "Nous sommes environ 1 100 habitants, et nous recevons plus d'un million de visiteurs par an. Des familles sont parties, car les logements coûtent trop cher. »")
E6 = [
    E("6-1", "Le guide d'un jour", "association",
      {"cm1": "Inès t'a trouvé une couverture : tu es guide touristique à Étretat. Lis le dépliant, puis propose à chaque visiteur l'activité qui lui plaira : clique sur un visiteur, puis sur une activité." + DOC_ETRETAT,
       "cm2": "Pour gagner la confiance de la source, tu joues au guide. Lis le dépliant, puis relie chaque visiteur à l'activité qui correspond à ses goûts." + DOC_ETRETAT},
      LIVRET.format(n=6) + " ; " + OT,
      "Elena, sportive, randonne sur le GR21 ; Tom, qui aime les boutiques, va au marché couvert ; Zac se promène en famille au parc des Roches ; "
      "Isabelle, passionnée de littérature, visite le Clos Lupin, la maison de Maurice Leblanc ; Richard, passionné d'histoire, visite le château des Aygues, "
      "ancienne résidence d'été des reines d'Espagne.",
      {"cm1": ["« Amo lo sport » : Elena aime le sport.", "« I love shopping » : Tom aime les boutiques.", "Maurice Leblanc était écrivain : sa maison plaira à une lectrice."],
       "cm2": ["Elena parle italien, Tom anglais : traduis d'abord leurs phrases.", "Un château où ont séjourné des reines plaira à un passionné d'histoire.", "Le parc des Roches est un espace de loisirs pour les familles."]},
      "l06",
      cm1={"paires": [{"g": "Elena : « Mi chiamo Elena, amo lo sport ! »", "d": "le sentier GR21"}, {"g": "Tom : « I'm Tom, I love shopping! »", "d": "le marché couvert"},
                      {"g": "Zac : « J'aime me balader en famille. »", "d": "le parc des Roches"}, {"g": "Isabelle : « J'adore la littérature ! »", "d": "le Clos Lupin"}]},
      cm2={"paires": [{"g": "Elena : « Mi chiamo Elena, amo lo sport ! »", "d": "le sentier GR21"}, {"g": "Tom : « I'm Tom, I love shopping! »", "d": "le marché couvert"},
                      {"g": "Zac : « J'aime me balader en famille. »", "d": "le parc des Roches"}, {"g": "Isabelle : « Je suis une grande fan de littérature ! »", "d": "le Clos Lupin"},
                      {"g": "Richard : « Je suis passionné d'histoire. »", "d": "le château des Aygues"}]}),
    E("6-2", "La définition du guide", "ordre",
      {"cm1": "Le guide officiel d'Étretat a fait tomber ses fiches. Remets les morceaux dans l'ordre pour retrouver la définition d'une station balnéaire. Retiens bien le premier mot !",
       "cm2": "Remets les morceaux dans l'ordre pour reconstituer la définition complète d'une station balnéaire. Compte ensuite les lettres du premier mot : c'est l'indice de la séance."},
      LIVRET.format(n=6) + " ; " + BO2,
      "Une station balnéaire est un « lieu de séjour situé en bord de mer », aménagé pour accueillir des touristes. Le premier mot, « lieu », compte 4 lettres : c'est l'indice de la séance.",
      {"cm1": ["La définition commence par « Lieu », avec une majuscule.", "On séjourne… en bord de mer.", "Lieu de séjour situé…"],
       "cm2": ["La majuscule montre le début de la définition.", "Le lieu est d'abord situé, puis aménagé.", "… aménagé pour accueillir des touristes."]},
      "l06",
      cm1=ordre(["Lieu", "de séjour", "situé", "en bord", "de mer"]),
      cm2=ordre(["Lieu", "de séjour", "situé en bord de mer,", "aménagé", "pour accueillir", "des touristes"])),
    E("6-3", "Le revers de la carte postale", "tri",
      {"cm1": "Une habitante confie à Inès ce que vivent les habitants l'été. Lis son témoignage, puis range chaque conséquence du tourisme : positive ou négative pour les habitants ?" + DOC_FREQ,
       "cm2": "Lis le témoignage, puis range chaque conséquence de la fréquentation touristique : positive ou négative pour les habitants ?" + DOC_FREQ},
      LIVRET.format(n=6) + " (d'après Francetvinfo, août 2022) ; Insee (Étretat, population en vigueur au 1er janvier 2026)",
      "Le tourisme crée des emplois dans les restaurants et les commerces, apporte des animations et de nouveaux aménagements comme les sentiers et les promenades. "
      "Mais il provoque des embouteillages, des déchets sur le front de mer et une hausse du prix des logements, qui pousse des habitants à partir.",
      {"cm1": ["Positif : ce qui aide les habitants.", "Les voitures garées partout : c'est négatif.", "Il y a 3 points positifs et 3 points négatifs."],
       "cm2": ["Quand les logements coûtent plus cher, les habitants ont du mal à se loger.", "Les touristes dépensent de l'argent chez les commerçants.", "Il y a 4 points positifs et 4 points négatifs."]},
      "l06",
      cm1=tri([("p", "Positif pour les habitants"), ("n", "Négatif pour les habitants")],
              [("des emplois dans les restaurants", "p"), ("des animations et des fêtes", "p"), ("de nouveaux sentiers et promenades", "p"),
               ("des embouteillages et pas de place pour se garer", "n"), ("des déchets sur le front de mer", "n"), ("des logements de plus en plus chers", "n")]),
      cm2=tri([("p", "Positif pour les habitants"), ("n", "Négatif pour les habitants")],
              [("des emplois dans les restaurants et les hôtels", "p"), ("des recettes pour les commerçants", "p"), ("des animations et des fêtes", "p"),
               ("de nouveaux sentiers et promenades", "p"), ("des embouteillages et pas de place pour se garer", "n"), ("des déchets sur le front de mer", "n"),
               ("des logements de plus en plus chers", "n"), ("des habitants qui quittent la ville", "n")])),
    E("6-4", "Étretat saturée ?", "qcm",
      "Inès fait le point avant de quitter Étretat. Réponds à ses questions, puis vérifie.",
      "Insee (Étretat : 1 469 habitants en 2011, 1 102 en 2023) ; Francetvinfo, août 2022 ; " + LIVRET.format(n=6),
      "Un million de visiteurs pour environ 1 100 habitants, cela fait à peu près 900 visiteurs par habitant et par an. Étretat a perdu 367 habitants entre 2011 et 2023. "
      "Un panneau « ville saturée » servirait à étaler les visites et à limiter les embouteillages, au risque de faire perdre des clients aux commerçants.",
      {"cm2": ["1 000 000 ÷ 1 000 = 1 000 : la réponse est un peu moins.", "1 469 − 1 102 : pose la soustraction.", "Trop de visiteurs à la fois : c'est la surfréquentation."]},
      "l06", niveaux=["CM2"],
      commun=qcm([("Étretat compte environ 1 100 habitants et reçoit environ 1 000 000 de visiteurs par an. Cela fait environ combien de visiteurs par habitant ?",
                   ["environ 900", "environ 90", "environ 9 000", "environ 9"], 0, "1 000 000 ÷ 1 100, c'est environ 909."),
                  ("En 2011, Étretat comptait 1 469 habitants ; en 2023, 1 102. Combien d'habitants a-t-elle perdus ?", ["367", "467", "2 571", "1 102"], 0, "1 469 − 1 102 = 367."),
                  ("Imagine que la mairie affiche : « Étretat saturée pendant deux heures ». À quoi servirait ce panneau ?",
                   ["à étaler les visites dans la journée et à limiter les embouteillages", "à attirer encore plus de voitures", "à fermer la plage pour toujours", "à annoncer une fête"], 0,
                   "Quand il y a trop de visiteurs, on cherche à mieux les répartir."),
                  ("Quel risque ce panneau ferait-il courir aux commerçants ?", ["avoir moins de clients pendant ces deux heures", "avoir trop de clients", "devoir déménager", "aucun risque"], 0,
                   "Moins de visiteurs, c'est aussi moins de recettes.")])),
]

# ============================================================================ ESCALE 7 — Biarritz, le littoral atlantique
E7 = [
    E("7-1", "La carte de Théo", "plan",
      {"cm1": "Théo, l'agent qui t'attend à Biarritz, déplie une carte de France. Place le nom de chaque mer ou océan sur son repère : clique sur une étiquette, puis sur la case du repère." + S.mers(range(4)),
       "cm2": "Théo déplie une carte de France. Place chaque mer ou océan, puis les trois stations du littoral, sur le bon repère. Une étiquette est en trop." + S.mers(range(7))},
      LIVRET.format(n=7) + " ; " + BO2 + " ; fond de carte dessiné par script (mission-geo/js/cartes.js)",
      "La mer du Nord est tout au nord, la Manche au nord-ouest, entre la France et le Royaume-Uni, l'océan Atlantique à l'ouest et la mer Méditerranée au sud. "
      "Étretat est au bord de la Manche, Biarritz au bord de l'océan Atlantique, Marseille au bord de la Méditerranée.",
      {"cm1": ["La Méditerranée est au sud, là où se trouve la Corse.", "L'océan Atlantique est à l'ouest : c'est le plus vaste.", "La mer du Nord est tout en haut ; la Manche juste à sa gauche."],
       "cm2": ["Étretat est en Normandie, au bord de la Manche.", "Biarritz est tout au sud-ouest, près de l'Espagne.", "Marseille est au bord de la Méditerranée ; Dunkerque est l'étiquette en trop."]},
      "l07",
      cm1=plan("La France et ses mers", [(f"Repère {i + 1}", S.MERS[i][0]) for i in range(4)], colonnes=2),
      cm2=plan("La France, ses mers et ses stations", [(f"Repère {i + 1}", S.MERS[i][0]) for i in range(7)], [m[0] for m in S.MERS] + ["Dunkerque"], colonnes=2)),
    E("7-2", "Quelle mer ?", "tri",
      {"cm1": "Avant de choisir la destination, Théo te teste. Range chaque phrase sous la mer ou l'océan dont elle parle.",
       "cm2": "Théo te teste avant le départ. Range chaque phrase sous la mer ou l'océan dont elle parle. Plusieurs phrases peuvent parler de la même étendue d'eau."},
      LIVRET.format(n=7) + " ; " + BO2,
      "On se baigne dans la Méditerranée à Marseille, et la Corse en est entourée ; l'océan Atlantique borde l'ouest et mène en Amérique ; "
      "la Manche sépare la France du Royaume-Uni et borde la Normandie ; la mer du Nord borde le nord de la France, vers la Belgique.",
      {"cm1": ["Marseille et la Corse sont au sud.", "Un océan est bien plus vaste qu'une mer : il mène à un autre continent.", "La Normandie est au bord de la Manche."],
       "cm2": ["La Manche est entre la France et le Royaume-Uni.", "Biarritz est au bord de l'océan.", "La Méditerranée a trois phrases, l'Atlantique trois."]},
      "l07",
      cm1=tri([("nord", "La mer du Nord"), ("manche", "La Manche"), ("atl", "L'océan Atlantique"), ("med", "La mer Méditerranée")],
              [("On s'y baigne à Marseille.", "med"), ("En le traversant, on arrive en Amérique.", "atl"), ("On s'y baigne en Normandie.", "manche"),
               ("Elle borde le nord de la France, vers la Belgique.", "nord"), ("La Corse en est entourée.", "med"), ("On s'y baigne à Biarritz.", "atl")]),
      cm2=tri([("nord", "La mer du Nord"), ("manche", "La Manche"), ("atl", "L'océan Atlantique"), ("med", "La mer Méditerranée")],
              [("On s'y baigne à Marseille.", "med"), ("En le traversant, on arrive en Amérique.", "atl"), ("On s'y baigne en Normandie.", "manche"),
               ("Elle borde le nord de la France, vers la Belgique.", "nord"), ("La Corse en est entourée.", "med"), ("On s'y baigne à Biarritz.", "atl"),
               ("En la traversant, on arrive au Royaume-Uni.", "manche"), ("C'est la mer qui borde le sud de la France.", "med"), ("Il borde l'ouest de la France.", "atl")])),
    E("7-3", "Où dormir ?", "association",
      {"cm1": "En été, Biarritz accueille beaucoup de vacanciers. Théo doit loger les agents : relie chaque description au type d'hébergement.",
       "cm2": "Théo cherche où loger les agents pendant la saison. Relie chaque description au type d'hébergement. Lis bien : certains se ressemblent."},
      LIVRET.format(n=7) + " ; " + BO2,
      "Une tente est une toile que l'on plante soi-même ; une caravane, un véhicule aménagé tiré par une voiture ; un hôtel a une réception et des chambres numérotées ; "
      "un camping est un terrain aménagé pour les tentes et les caravanes ; un gîte, une maison de vacances louée entièrement ; un mobil-home, une maison préfabriquée posée sur un camping ; "
      "une chambre d'hôtes, une chambre chez l'habitant ; une auberge de jeunesse, un hébergement bon marché pour jeunes voyageurs.",
      {"cm1": ["La tente se plante, la caravane se tire.", "Le camping est un terrain.", "Le gîte est une maison entière."],
       "cm2": ["Le mobil-home ne roule pas : il reste posé sur le camping.", "Chez l'habitant, c'est la chambre d'hôtes.", "L'auberge de jeunesse accueille les jeunes voyageurs."]},
      "l07",
      cm1={"paires": [{"g": "une toile que l'on plante soi-même", "d": "une tente"}, {"g": "un véhicule aménagé, tiré par une voiture", "d": "une caravane"},
                      {"g": "un établissement avec une réception et des chambres numérotées", "d": "un hôtel"}, {"g": "un terrain aménagé pour les tentes et les caravanes", "d": "un camping"},
                      {"g": "une maison de vacances louée entièrement", "d": "un gîte"}]},
      cm2={"paires": [{"g": "une toile que l'on plante soi-même", "d": "une tente"}, {"g": "un véhicule aménagé, tiré par une voiture", "d": "une caravane"},
                      {"g": "un établissement avec une réception et des chambres numérotées", "d": "un hôtel"}, {"g": "un terrain aménagé pour les tentes et les caravanes", "d": "un camping"},
                      {"g": "une maison de vacances louée entièrement", "d": "un gîte"}, {"g": "une maison préfabriquée posée sur un terrain de camping", "d": "un mobil-home"},
                      {"g": "une chambre chez l'habitant, petit-déjeuner compris", "d": "une chambre d'hôtes"}, {"g": "un hébergement bon marché pour jeunes voyageurs", "d": "une auberge de jeunesse"}]}),
    E("7-4", "L'été, combien sont-ils ?", "code",
      "Théo compare avec Étretat. Étretat mesure environ 4 km² et compte environ 1 100 habitants. Imagine un jour d'été où 15 000 visiteurs s'ajoutent aux habitants. Calcule, puis ouvre.",
      "Insee (Étretat : 4,07 km², 1 102 habitants, population en vigueur au 1er janvier 2026) ; " + LIVRET.format(n=7),
      "Hors vacances : 1 100 ÷ 4 = 275 habitants par km². Ce jour d'été : (1 100 + 15 000) ÷ 4 = 16 100 ÷ 4 = 4 025 habitants par km². "
      "4 025 ÷ 275 donne environ 14,6 : la densité est environ multipliée par 15.",
      {"cm2": ["Densité = nombre de personnes ÷ surface en km².", "D'abord 1 100 + 15 000 = 16 100.", "Compare : 4 025 ÷ 275, arrondi à l'unité."]},
      "l07", niveaux=["CM2"],
      commun={"champs": [{"libelle": "Densité hors vacances (hab/km²)", "valeur": "275", "longueur": 3},
                         {"libelle": "Densité ce jour d'été (hab/km²)", "valeur": "4025", "longueur": 4},
                         {"libelle": "La densité est multipliée par environ", "valeur": "15", "longueur": 2}]}),
]

# ============================================================================ ESCALE 8 — Dhaka, les inégalités dans le monde
RICHES8 = ["la Norvège", "les États-Unis", "la France", "le Japon", "Haïti", "le Mali", "le Tchad", "Madagascar"]
E8 = [
    E("8-1", "Le planisphère de Nour", "plan",
      {"cm1": "Nour, l'agente qui t'attend à Dhaka, compare la vie au Bangladesh avec celle d'autres pays. Elle a épinglé des pays sur son planisphère : replace chaque nom sur son repère." + S.pays(range(5)),
       "cm2": "Nour a épinglé sept pays sur son planisphère. Replace chaque nom sur son repère, en t'aidant des continents." + S.pays(range(7))},
      LIVRET.format(n=8) + " ; " + BO2 + " ; fond de carte dessiné par script (mission-geo/js/cartes.js)",
      "Les États-Unis sont en Amérique du Nord, la Norvège en Europe, le Tchad et le Mali en Afrique, le Bangladesh et le Japon en Asie, l'Australie en Océanie.",
      {"cm1": ["Le Bangladesh, où tu te trouves, est au sud de l'Asie.", "L'Australie est en Océanie, en bas à droite.", "Le Tchad est en Afrique ; la Norvège, au nord de l'Europe."],
       "cm2": ["Le Japon est tout à l'est de l'Asie.", "Le Mali est à l'ouest du Tchad.", "Les États-Unis sont en Amérique du Nord."]},
      "l08",
      cm1=plan("Le planisphère de Nour", [(f"Repère {i + 1}", S.PAYS[i][0]) for i in range(5)], colonnes=2),
      cm2=plan("Le planisphère de Nour", [(f"Repère {i + 1}", S.PAYS[i][0]) for i in range(7)], colonnes=2)),
    E("8-2", "Riches ou pauvres ?", "tri",
      {"cm1": "Nour te montre le revenu moyen d'un habitant dans plusieurs pays. Lis le diagramme, puis range chaque pays : plus de 40 000 dollars par habitant, ou moins de 3 000 ?" + S.revenus(RICHES8),
       "cm2": "Lis le diagramme du revenu moyen par habitant, puis range chaque pays dans sa colonne." + S.revenus(RICHES8 + ["la Guinée équatoriale", "le Bangladesh"])},
      S.SOURCE_PNUD + " ; " + LIVRET.format(n=8),
      "Avec plus de 40 000 dollars par habitant, la Norvège, les États-Unis, la France et le Japon sont des pays riches. Avec moins de 3 000 dollars, Haïti, le Mali, le Tchad et Madagascar "
      "sont des pays pauvres. Le Bangladesh (8 498 dollars) et la Guinée équatoriale (12 762 dollars) se situent entre les deux.",
      {"cm1": ["Regarde la longueur des barres.", "Une barre très courte : un pays pauvre.", "Il y a 4 pays dans chaque colonne."],
       "cm2": ["Lis les nombres écrits au bout des barres.", "Le Bangladesh : 8 498 dollars, entre 3 000 et 40 000.", "4 pays riches, 2 entre les deux, 4 pays pauvres."]},
      "l08",
      cm1=tri([("r", "Plus de 40 000 $ : pays riches"), ("p", "Moins de 3 000 $ : pays pauvres")],
              [("la Norvège", "r"), ("les États-Unis", "r"), ("la France", "r"), ("le Japon", "r"), ("Haïti", "p"), ("le Mali", "p"), ("le Tchad", "p"), ("Madagascar", "p")]),
      cm2=tri([("r", "Plus de 40 000 $"), ("m", "De 3 000 à 40 000 $"), ("p", "Moins de 3 000 $")],
              [("la Norvège", "r"), ("les États-Unis", "r"), ("la France", "r"), ("le Japon", "r"), ("le Bangladesh", "m"), ("la Guinée équatoriale", "m"),
               ("Haïti", "p"), ("le Mali", "p"), ("le Tchad", "p"), ("Madagascar", "p")])),
    E("8-3", "Ce que Nour a vu", "qcm",
      {"cm1": "Nour te raconte ce qu'elle a vu à Dhaka et ce qu'elle a appris. Réponds à ses questions, puis vérifie.",
       "cm2": "Nour te raconte ce qu'elle a vu à Dhaka. Réponds à ses questions, puis vérifie."},
      LIVRET.format(n=8) + " ; " + S.SOURCE_PNUD + " ; World Inequality Lab, Rapport sur les inégalités mondiales 2022 ; OIT et UNICEF, juin 2025",
      "On compare les pays avec le revenu par habitant, l'espérance de vie et la durée de la scolarisation. Le gâteau du dessin représente les richesses du monde : "
      "les 10 % les plus riches possèdent environ les trois quarts du patrimoine. Un enfant qui travaille au lieu d'aller à l'école met sa santé en danger et aura plus de mal "
      "à sortir de la pauvreté ; en 2024, près de 138 millions d'enfants travaillaient dans le monde.",
      {"cm1": ["Trois indicateurs : l'argent, la santé, l'école.", "Une énorme part pour quelques-uns, des miettes pour les autres.", "L'école aide à sortir de la pauvreté."],
       "cm2": ["L'espérance de vie dit si l'on vit longtemps.", "Le gâteau, ce sont les richesses.", "138 millions : relis la fiche « Les inégalités de niveau de vie »."]},
      "l08",
      cm1=qcm([("Pour comparer le niveau de vie des pays, on regarde le revenu par habitant, mais aussi…", ["l'espérance de vie et la durée de la scolarisation", "la couleur du drapeau", "le nombre de montagnes"], 0,
                "Trois indicateurs : le revenu, la santé et l'école."),
               ("Sur un dessin de presse, quelques convives se servent une énorme part de gâteau et la foule se partage les miettes. Que représente le gâteau ?",
                ["les richesses du monde, très mal partagées", "la nourriture d'une fête", "la population de la Terre"], 0, "Une petite partie de la population possède la plus grande partie des richesses."),
               ("Nour a vu un enfant trier des déchets au lieu d'aller à l'école. Que lui fait perdre la pauvreté ?", ["l'école, et sa santé est en danger", "rien du tout", "ses vacances seulement"], 0,
                "Sans école, il sera plus difficile pour lui de sortir de la pauvreté.")]),
      cm2=qcm([("Pour comparer le niveau de vie des pays, on regarde le revenu par habitant, mais aussi…",
                ["l'espérance de vie et la durée de la scolarisation", "la couleur du drapeau", "le nombre de montagnes", "la taille de la capitale"], 0, "Trois indicateurs : le revenu, la santé et l'école."),
               ("Sur un dessin de presse, quelques convives se servent une énorme part de gâteau et la foule se partage les miettes. Que représente le gâteau ?",
                ["les richesses du monde, très mal partagées", "la nourriture d'une fête", "la population de la Terre", "les pays du monde"], 0,
                "Les 10 % les plus riches possèdent environ les trois quarts du patrimoine mondial."),
               ("Nour a vu un enfant trier des déchets et un autre porter des briques. Quelle conséquence la pauvreté a-t-elle pour eux ?",
                ["ils ne vont pas à l'école et leur santé est en danger", "ils apprennent un métier sans danger", "ils gagnent assez pour être riches", "aucune conséquence"], 0,
                "Sans école, il est plus difficile de sortir de la pauvreté."),
               ("Selon l'OIT et l'UNICEF, combien d'enfants travaillaient dans le monde en 2024 ?", ["près de 138 millions", "près de 138 000", "près de 13 800", "aucun"], 0,
                "Le travail des enfants a presque diminué de moitié depuis 2000, mais il reste très répandu.")])),
    E("8-4", "La richesse suffit-elle ?", "vraifaux",
      "Nour compare quatre pays dans un tableau du PNUD. Lis-le, puis choisis « Vrai » ou « Faux » pour chaque phrase." + S.tableau_pnud(["la Norvège", "le Koweït", "la Guinée équatoriale", "le Bangladesh"]),
      S.SOURCE_PNUD + " ; " + LIVRET.format(n=8),
      "La Norvège a le revenu le plus élevé du tableau, plus de 13 fois celui du Bangladesh. Le Bangladesh est moins riche que la Guinée équatoriale, mais on y vit plus longtemps : "
      "la richesse ne suffit pas, à elle seule, à mesurer le développement.",
      {"cm2": ["Compare les nombres ligne par ligne.", "74,7 ans, c'est plus que 63,7 ans.", "112 710 ÷ 8 498 : un peu plus de 13."]},
      "l08", niveaux=["CM2"],
      commun={"affirmations": [
          {"txt": "La Norvège a le revenu par habitant le plus élevé du tableau.", "vrai": True, "explication": "112 710 dollars."},
          {"txt": "Le Bangladesh a un revenu par habitant plus faible que la Guinée équatoriale.", "vrai": True, "explication": "8 498 dollars contre 12 762 dollars."},
          {"txt": "On vit moins longtemps au Bangladesh qu'en Guinée équatoriale.", "vrai": False, "explication": "74,7 ans contre 63,7 ans : on y vit plus longtemps."},
          {"txt": "Dans ce tableau, plus un pays est riche, plus on y vit longtemps, sans exception.", "vrai": False, "explication": "Le Bangladesh, moins riche, a une espérance de vie plus longue que la Guinée équatoriale."},
          {"txt": "Le revenu d'un habitant de la Norvège est plus de 13 fois celui d'un habitant du Bangladesh.", "vrai": True, "explication": "112 710 ÷ 8 498, c'est environ 13,3."}]}),
]

# ============================================================================ ESCALES 9 à 13 (périodes 3 et 4 : se nourrir, relief et fleuves)
def tab(titre, entetes, lignes):
    """Document : titre en italique et tableau de relevés (classes du moteur)."""
    th = "".join(f"<th>{h}</th>" for h in entetes)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in lignes)
    return f'<div class="doc-titre"><i>{titre}</i></div><table class="tableau-releves"><tr>{th}</tr>{tr}</table>'


PRIX9 = tab("Les prix au marché de Bamako (en euros)", ["Produit local", "Prix", "Produit importé", "Prix"],
            [["Millet (1 kg)", "0,76", "Pain (1 pièce)", "0,46"], ["Riz (1 kg)", "0,91", "Pâtes importées (1 kg)", "3,81"],
             ["Arachides (1 kg)", "1,52", "Fromage importé (100 g)", "2,29"], ["Haricots (1 kg)", "1,37", "Yaourt importé (1 pot)", "1,22"],
             ["Gombo (1 kg)", "1,22", "Pomme importée (1 pièce)", "1,52"], ["Mangue (1 kg)", "1,06", "Carotte (1 kg)", "1,06"]])
SRC9 = LIVRET.format(n=9) + " ; " + BO2 + " ; FAO, SOFI 2025"
E9 = [
    E("9-1", "Les deux frigos", "tri",
      {"cm1": "Aminata t'emmène chez deux familles : une en France, une au Mali. Elle a mélangé le contenu de leurs frigos. Range chaque aliment dans le frigo où on le trouve le plus souvent.",
       "cm2": "Aminata a mélangé le contenu de deux frigos, un en France, un au Mali. Au Mali, on consomme surtout ce qui est produit sur place ; les produits importés sont rares et chers. Range chaque aliment dans son frigo."},
      SRC9,
      "En France, on trouve du pain de mie, des pâtes, du fromage, des yaourts, des pommes et des carottes. Au Mali, on mange surtout ce qui est produit sur place : "
      "le millet, le riz, les arachides, les haricots rouges, le gombo et la mangue.",
      {"cm1": ["Au Mali, on mange ce qui pousse sur place.", "Le fromage et le yaourt sont importés au Mali.", "Le millet, le gombo et la mangue sont des produits maliens."],
       "cm2": ["Un produit importé coûte très cher au Mali : il est rare dans un frigo.", "Le riz, le millet et les arachides poussent en Afrique de l'Ouest.", "Six aliments dans chaque frigo."]},
      "l09",
      cm1=tri([("fr", "Le frigo en France"), ("ml", "Le frigo au Mali")],
              [("Pain de mie", "fr"), ("Fromage", "fr"), ("Yaourt", "fr"), ("Pomme", "fr"), ("Millet", "ml"), ("Arachides", "ml"), ("Gombo", "ml"), ("Mangue", "ml")]),
      cm2=tri([("fr", "Le frigo en France"), ("ml", "Le frigo au Mali")],
              [("Pain de mie", "fr"), ("Pâtes", "fr"), ("Fromage", "fr"), ("Yaourt", "fr"), ("Pomme", "fr"), ("Carotte", "fr"),
               ("Millet", "ml"), ("Riz", "ml"), ("Arachides", "ml"), ("Haricots rouges", "ml"), ("Gombo", "ml"), ("Mangue", "ml")])),
    E("9-2", "Pourquoi si peu de poisson ?", "qcm",
      {"cm1": "Aminata s'étonne : sur le marché, il y a peu de poisson, peu de bœuf et peu de variété de fruits et de légumes. Aide-la à comprendre pourquoi.",
       "cm2": "Aminata te demande d'expliquer ce que tu vois sur le marché : peu de poisson, peu de bœuf, peu de variété de fruits et de légumes. Cherche les causes, une par question."},
      SRC9,
      "Le Mali est un pays enclavé, sans accès à la mer : le poisson de mer y est rare et cher. Le climat est chaud et sec et la saison des pluies est courte : les cultures sont peu variées. "
      "Peu de familles possèdent un réfrigérateur, ce qui limite la conservation de la viande et du poisson. Les produits importés coûtent très cher.",
      {"cm1": ["Regarde une carte : le Mali est loin de toute mer.", "Sans frigo, la viande ne se garde pas.", "Relis ce que dit Aminata sur le marché."],
       "cm2": ["Le Mali n'a pas de côte.", "Un climat très sec limite les cultures.", "Les importations coûtent cher ; peu de familles ont un frigo."]},
      "l09",
      cm1=qcm([("Il y a peu de poisson de mer sur le marché de Bamako. Pourquoi ?", ["le Mali est un pays enclavé, sans accès à la mer", "les Maliens n'aiment pas le poisson", "il n'y a pas de marché pour le poisson"], 0,
                "Le Mali n'a pas de côte : le poisson de mer y est rare et cher."),
               ("Pourquoi les pâtes importées sont-elles rares sur les étals ?", ["elles coûtent très cher pour une famille malienne", "elles sont interdites au Mali", "elles poussent seulement en France"], 0,
                "Un kilo de pâtes importées vaut environ cinq fois le prix d'un kilo de millet."),
               ("Pourquoi est-il difficile de garder la viande et le poisson ?", ["peu de familles ont un réfrigérateur", "il fait trop froid", "on les mange toujours crus"], 0,
                "Sans réfrigérateur, ils se conservent mal.")]),
      cm2=qcm([("Il y a peu de poisson de mer sur le marché de Bamako. Pourquoi ?", ["le Mali est un pays enclavé, sans accès à la mer", "les Maliens n'aiment pas le poisson", "il n'y a pas de marché pour le poisson", "la pêche est interdite"], 0,
                "Le Mali n'a pas de côte : le poisson de mer y est rare et cher."),
               ("Pourquoi y a-t-il peu de variété de fruits et de légumes ?", ["le climat est chaud et sec, la saison des pluies est courte", "le sol est gelé toute l'année", "les fruits y sont interdits", "on n'y cultive rien"], 0,
                "Les cultures y sont peu variées."),
               ("Pourquoi la viande et le poisson se conservent-ils mal ?", ["peu de familles possèdent un réfrigérateur", "ils ne se mangent jamais cuits", "il fait trop froid", "ils sont trop salés"], 0,
                "Sans froid, la viande et le poisson se gâtent vite."),
               ("Pourquoi les familles achètent-elles surtout des produits locaux ?", ["les produits importés coûtent très cher", "les produits locaux sont gratuits", "les produits importés sont interdits", "elles n'aiment pas le fromage"], 0,
                "Les revenus sont faibles : un kilo de pâtes importées vaut environ cinq fois un kilo de millet.")])),
    E("9-3", "Le budget de la famille C", "code",
      {"cm1": "La famille C, au Mali, dispose de 8 €. Elle achète 1 kg de pâtes importées, 100 g de fromage importé et 1 yaourt importé. Calcule en centimes (1 € = 100 centimes), puis ouvre le cadenas." + PRIX9,
       "cm2": "La famille C (Mali) dispose de 8 €, la famille A (France) de 25 €. La famille C achète 1 kg de pâtes importées, 100 g de fromage importé et 1 yaourt importé. Calcule en centimes (1 € = 100 centimes), puis ouvre le cadenas." + PRIX9},
      SRC9,
      "La famille C dépense 3,81 + 2,29 + 1,22 = 7,32 €, soit 732 centimes. Il lui reste 8 − 7,32 = 0,68 €, soit 68 centimes. Avec 8 € (800 centimes), elle aurait pu acheter 10 kg de millet "
      "(800 ÷ 76 ≈ 10,5, donc 10 kilos entiers). La famille A est environ 3 fois plus riche (25 ÷ 8 ≈ 3,1).",
      {"cm1": ["3,81 € = 381 centimes ; 2,29 € = 229 centimes ; 1,22 € = 122 centimes.", "800 − le total des dépenses.", "Un kilo de millet coûte 76 centimes : 800 ÷ 76, en gardant les kilos entiers."],
       "cm2": ["Additionne 381 + 229 + 122.", "Le reste : 800 centimes moins la dépense.", "25 ÷ 8 donne un peu plus de 3 : arrondis à l'unité."]},
      "l09",
      cm1={"champs": [{"libelle": "Dépense de la famille C (centimes)", "valeur": "732", "longueur": 3}, {"libelle": "Il lui reste (centimes)", "valeur": "68", "longueur": 2},
                      {"libelle": "Kilos de millet pour 8 € (nombre entier)", "valeur": "10", "longueur": 2}]},
      cm2={"champs": [{"libelle": "Dépense de la famille C (centimes)", "valeur": "732", "longueur": 3}, {"libelle": "Il lui reste (centimes)", "valeur": "68", "longueur": 2},
                      {"libelle": "Kilos de millet pour 8 € (nombre entier)", "valeur": "10", "longueur": 2},
                      {"libelle": "La famille A est environ … fois plus riche (arrondi à l'unité)", "valeur": "3", "longueur": 1}]}),
    E("9-4", "Qui ne mange pas assez ?", "vraifaux",
      "Aminata te montre la carte de la sous-alimentation, qui indique la part de la population qui ne mange pas assez. Pour chaque phrase, choisis « Vrai » ou « Faux ».",
      SRC9,
      "La sous-alimentation touche surtout l'Afrique subsaharienne (Tchad, Soudan, Madagascar) et certains pays comme Haïti, une île des Caraïbes qui appartient à l'Amérique du Nord. "
      "En France et aux États-Unis, elle concerne moins de 2,5 % de la population. Au Mali, on mange surtout ce qui est produit sur place.",
      {"cm2": ["Haïti est une île des Caraïbes.", "Le Tchad est en Afrique, pas en Europe.", "Relis ce que dit Aminata sur la France."]},
      "l09", niveaux=["CM2"],
      commun={"affirmations": [
          {"txt": "En France, la sous-alimentation concerne moins de 2,5 % de la population.", "vrai": True, "explication": "C'est aussi le cas aux États-Unis."},
          {"txt": "Haïti est un pays d'Amérique du Sud.", "vrai": False, "explication": "Haïti est une île des Caraïbes : elle appartient à l'Amérique du Nord."},
          {"txt": "La sous-alimentation touche surtout l'Afrique subsaharienne.", "vrai": True, "explication": "Le Tchad, le Soudan et Madagascar en font partie."},
          {"txt": "Le Tchad est un pays d'Europe.", "vrai": False, "explication": "Le Tchad est en Afrique."},
          {"txt": "Au Mali, on mange surtout des produits importés.", "vrai": False, "explication": "On y mange surtout ce qui est produit sur place."}]}),
]

SRC10 = LIVRET.format(n=10) + " ; " + BO2
PLATEAU = [("Pomme", "agri"), ("Haricots verts", "agri"), ("Carottes", "agri"), ("Poulet", "agri"), ("Salade", "agri"), ("Yaourt", "trans"), ("Pain", "trans"), ("Cookie", "trans")]
E10 = [
    E("10-1", "Le plateau de la cantine", "tri",
      {"cm1": "Camille, la cheffe de la cantine, te présente le plateau du jour. Range chaque aliment : vient-il directement de la nature, ou a-t-il été fabriqué ?",
       "cm2": "Observe le plateau du jour et range chaque aliment dans le bon panier. Un produit transformé a été fabriqué à partir d'autre chose : le pain vient du blé."},
      SRC10,
      "La pomme, les haricots verts, les carottes, le poulet et la salade sont des produits agricoles : ils viennent directement de la nature. Le yaourt, le pain et le cookie sont des produits transformés, "
      "fabriqués à partir de produits agricoles.",
      {"cm1": ["Une pomme se cueille sur un arbre.", "Le pain est fabriqué à partir du blé.", "Il y a 5 produits agricoles et 3 produits transformés."],
       "cm2": ["Un produit transformé a été fabriqué par quelqu'un, dans un atelier ou une usine.", "Le yaourt vient du lait.", "Le cookie est fabriqué avec de la farine, du sucre, du beurre…"]},
      "l10",
      cm1=tri([("agri", "Produits agricoles (viennent directement de la nature)"), ("trans", "Produits transformés (fabriqués)")], PLATEAU),
      cm2=tri([("agri", "Produits agricoles (viennent directement de la nature)"), ("trans", "Produits transformés (fabriqués à partir de produits agricoles)")], PLATEAU)),
    E("10-2", "De la nature à l'assiette", "association",
      {"cm1": "Camille te demande de relier chaque produit agricole au produit transformé fabriqué à partir de lui : clique sur l'un, puis sur l'autre.",
       "cm2": "Relie chaque produit agricole au produit transformé fabriqué à partir de lui. Réfléchis à la matière première de chaque produit."},
      SRC10,
      "Le raisin donne le jus de raisin, le lait le fromage, la tomate la sauce tomate, le blé le pain, le cacao le chocolat, la canne à sucre le sucre.",
      {"cm1": ["Le pain est fabriqué avec de la farine de blé.", "Le fromage est fabriqué avec du lait.", "Le chocolat vient des fèves d'un arbre tropical."],
       "cm2": ["Le sucre vient d'une plante : la canne à sucre (ou la betterave).", "Le cacao est la matière première du chocolat.", "Le jus de raisin est du raisin pressé."]},
      "l10",
      cm1={"paires": [{"g": "Raisin", "d": "Jus de raisin"}, {"g": "Lait", "d": "Fromage"}, {"g": "Tomate", "d": "Sauce tomate"}, {"g": "Blé", "d": "Pain"}, {"g": "Cacao", "d": "Chocolat"}]},
      cm2={"paires": [{"g": "Raisin", "d": "Jus de raisin"}, {"g": "Lait", "d": "Fromage"}, {"g": "Tomate", "d": "Sauce tomate"}, {"g": "Canne à sucre", "d": "Sucre"},
                      {"g": "Blé", "d": "Pain"}, {"g": "Cacao", "d": "Chocolat"}]}),
    E("10-3", "Qui produit quoi ?", "qcm",
      {"cm1": "Camille visite la ferme de Bray avec toi. Chaque aliment du plateau vient d'un espace de production et d'un métier. Réponds à ses questions.",
       "cm2": "À la ferme de Bray, chaque aliment du plateau vient d'un espace de production et d'un métier. Réponds aux questions de Camille."},
      SRC10,
      "L'éleveur produit le poulet dans un élevage ; le maraîcher cultive les carottes et les haricots verts ; les pommes poussent dans un verger, qui est le domaine de l'arboriculteur ; "
      "le céréalier cultive le blé, dont on fait le pain. Un produit transformé est fabriqué à partir d'un ou de plusieurs produits agricoles.",
      {"cm1": ["Le poulet vient d'un élevage.", "Un maraîcher cultive des légumes.", "Les pommes poussent sur des arbres, dans un verger."],
       "cm2": ["Le céréalier cultive le blé et le maïs.", "L'arboriculteur s'occupe d'un verger.", "Un produit transformé a besoin d'un produit agricole pour être fabriqué."]},
      "l10",
      cm1=qcm([("Qui s'occupe de l'élevage des poulets ?", ["l'éleveur", "le maraîcher", "le céréalier"], 0, "L'éleveur travaille dans un élevage."),
               ("Qui cultive les carottes et les haricots verts ?", ["le maraîcher", "l'éleveur", "le céréalier"], 0, "Le maraîcher cultive les légumes."),
               ("Où poussent les pommes ?", ["dans un verger", "dans un élevage", "dans un champ de blé"], 0, "Un verger est un terrain planté d'arbres fruitiers.")]),
      cm2=qcm([("Qui s'occupe de l'élevage des poulets ?", ["l'éleveur", "le maraîcher", "le céréalier", "l'arboriculteur"], 0, "L'éleveur travaille dans un élevage."),
               ("Qui cultive les carottes et les haricots verts ?", ["le maraîcher", "l'éleveur", "le céréalier", "l'arboriculteur"], 0, "Le maraîcher cultive les légumes."),
               ("Quel métier s'occupe d'un verger ?", ["l'arboriculteur", "le maraîcher", "le céréalier", "l'éleveur"], 0, "Les pommes, les poires et les cerises poussent dans un verger."),
               ("Quelle affirmation est exacte ?", ["un produit transformé est fabriqué à partir d'un ou de plusieurs produits agricoles", "un produit transformé vient directement de la nature",
                                                      "un produit agricole est toujours fabriqué dans une usine", "le fromage est un produit agricole"], 0, "Le fromage est fabriqué à partir du lait : c'est un produit transformé.")])),
    E("10-4", "Le décompte de Camille", "code",
      "Camille doit remplir son registre. Sur le plateau du jour : une pomme, des haricots verts, des carottes, du poulet, de la salade, un yaourt, du pain et un cookie. Compte, puis ouvre le cadenas.",
      SRC10,
      "Cinq produits agricoles (pomme, haricots verts, carottes, poulet, salade) et trois produits transformés (yaourt, pain, cookie) : huit aliments en tout.",
      {"cm2": ["Reprends le tri du plateau.", "Un yaourt, du pain et un cookie sont transformés.", "5 + 3 pour le total."]},
      "l10", niveaux=["CM2"],
      commun={"champs": [{"libelle": "Produits agricoles sur le plateau", "valeur": "5", "longueur": 1}, {"libelle": "Produits transformés sur le plateau", "valeur": "3", "longueur": 1},
                         {"libelle": "Aliments en tout", "valeur": "8", "longueur": 1}]}),
]

SRC11 = LIVRET.format(n=11) + " ; " + BO2
E11 = [
    E("11-1", "Le trajet du lait", "ordre",
      {"cm1": "Manon, éleveuse à la ferme de Bray, te montre le trajet du lait jusqu'au yaourt. Remets les étapes dans l'ordre, de la ferme au magasin.",
       "cm2": "Remets le trajet du lait dans l'ordre, des vaches au rayon frais du supermarché."},
      SRC11,
      "Les vaches pâturent au pré ; le lait est recueilli à la traite puis refroidi ; un camion-citerne réfrigéré le collecte ; à l'usine, il est analysé ; il est chauffé, ensemencé de ferments et il repose ; "
      "le yaourt est versé dans des pots ; un camion frigorifique livre les magasins ; le yaourt est vendu au rayon frais.",
      {"cm1": ["Tout commence à la ferme.", "Le lait voyage dans un camion avant d'arriver à l'usine.", "Le yaourt finit au magasin."],
       "cm2": ["Les vaches sont dans le pré avant la traite.", "Le lait est analysé avant d'être transformé.", "Le yaourt est mis en pots avant d'être livré."]},
      "l11",
      cm1=ordre(["La traite : le lait est recueilli, puis refroidi", "Le camion-citerne réfrigéré collecte le lait", "À l'usine, le lait est analysé",
                 "Le yaourt est fabriqué, puis versé dans des pots", "Un camion frigorifique livre les magasins", "Le yaourt est vendu au rayon frais"]),
      cm2=ordre(["Les vaches pâturent au pré", "La traite : le lait est recueilli, puis refroidi", "Le camion-citerne réfrigéré collecte le lait", "Le lait arrive à l'usine et il est analysé",
                 "Le lait est chauffé, ensemencé de ferments, puis il repose", "Le yaourt est versé dans des pots, qui sont operculés", "Un camion frigorifique livre les magasins",
                 "Le yaourt est vendu au rayon frais du supermarché"])),
    E("11-2", "Le texte du directeur", "trous",
      {"cm1": "Avant de te laisser entrer à l'usine d'Issenheim, le directeur te donne un texte à compléter : clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
       "cm2": "Avant de te laisser entrer, le directeur te donne ce texte à trous. Deux mots de la liste ne servent à rien."},
      SRC11,
      "Le lait est trait puis refroidi, transporté dans un camion-citerne réfrigéré jusqu'à l'usine, où il est analysé, chauffé et ensemencé de ferments : le yaourt fermente. "
      "Il est versé dans des pots, puis livré aux supermarchés et vendu en magasin. Le lait n'est jamais congelé ni cuit.",
      {"cm1": ["Le lait est refroidi, jamais congelé.", "Un camion réfrigéré transporte le lait à l'usine.", "Le yaourt fermente grâce aux ferments."],
       "cm2": ["Le lait n'est jamais congelé ni cuit : il est refroidi, transporté au frais, puis chauffé doucement.", "À l'usine, le lait est analysé.", "Le yaourt est versé dans des pots."]},
      "l11",
      cm1={"texte": "<p>Tout commence à la [[ferme]]. Le lait est [[trait]], puis refroidi. Un camion-citerne [[réfrigéré]] le porte à l'[[usine]]. Là, il est [[analysé]], puis le yaourt [[fermente]]. "
                    "Il est versé dans des [[pots]] et livré aux [[supermarchés]].</p>",
           "etiquettes": ["ferme", "trait", "réfrigéré", "usine", "analysé", "fermente", "pots", "supermarchés", "congelé"]},
      cm2={"texte": "<p>Tout commence à la [[ferme]]. Le lait est [[trait]] puis immédiatement refroidi. Il est ensuite transporté dans un camion-citerne [[réfrigéré]] jusqu'à l'[[usine]]. "
                    "À l'usine, le lait est [[analysé]] et stocké dans de grands réservoirs. Le lait est alors chauffé, des ferments sont ajoutés et le mélange repose : le yaourt [[fermente]]. "
                    "Le yaourt est versé dans des [[pots]] et fermé avec un couvercle. Il est ensuite transporté jusqu'aux [[supermarchés]]. Enfin, il est vendu en [[magasin]] et arrive dans ton frigo !</p>",
           "etiquettes": ["ferme", "trait", "réfrigéré", "usine", "analysé", "fermente", "pots", "supermarchés", "magasin", "congelé", "cuit"]}),
    E("11-3", "Et si le lait tournait ?", "qcm",
      {"cm1": "Manon te pose deux questions pour vérifier que tu as bien suivi le lait.",
       "cm2": "Manon vérifie que tu as bien suivi le lait. Réponds à ses trois questions."},
      SRC11,
      "Sans réfrigération, des microbes se développent dans le lait, qui tourne et devient impropre à la consommation : la chaîne du froid ne doit jamais être interrompue. "
      "L'usine de yaourts transforme une matière première : elle relève du secteur secondaire. La ferme relève du secteur primaire, le supermarché du secteur tertiaire.",
      {"cm1": ["Sans froid, le lait se gâte.", "Transformer, c'est du secteur secondaire.", "Relis le trajet du lait."],
       "cm2": ["Les microbes se développent quand il fait trop chaud.", "Souviens-toi de la séance de Besançon : transformer, c'est du secondaire.", "La ferme exploite directement la nature."]},
      "l11",
      cm1=qcm([("Que se passerait-il si le lait n'était pas transporté au frais jusqu'à l'usine ?", ["il tournerait et deviendrait impropre à la consommation", "il deviendrait plus sucré", "il se transformerait en fromage tout seul"], 0,
                "Des microbes se développeraient dans le lait."),
               ("Dans quel secteur classe-t-on l'usine de yaourts ?", ["le secteur secondaire : elle transforme une matière première", "le secteur primaire : elle exploite la nature", "le secteur tertiaire : elle rend un service"], 0,
                "Elle transforme le lait en yaourt.")]),
      cm2=qcm([("Que se passerait-il si le lait n'était pas transporté au frais jusqu'à l'usine ?", ["des microbes s'y développeraient : il tournerait et deviendrait impropre à la consommation", "il deviendrait plus sucré",
                                                                                                  "il se transformerait en fromage tout seul", "rien du tout"], 0, "La chaîne du froid protège la santé des consommateurs."),
               ("Dans quel secteur classe-t-on l'usine de yaourts ?", ["le secteur secondaire : elle transforme une matière première", "le secteur primaire : elle exploite la nature", "le secteur tertiaire : elle rend un service",
                                                                         "aucun secteur"], 0, "Elle transforme le lait en yaourt."),
               ("Dans quel secteur classe-t-on la ferme de Bray ?", ["le secteur primaire : elle exploite directement la nature", "le secteur secondaire", "le secteur tertiaire", "aucun secteur"], 0,
                "L'éleveur produit le lait.")])),
    E("11-4", "Dans l'usine", "code",
      "Dans l'usine d'Issenheim, le directeur te fait compter. Les étapes du trajet : 1. les vaches pâturent ; 2. la traite ; 3. le camion-citerne collecte le lait ; 4. le lait arrive à l'usine et il est analysé ; "
      "5. le lait est chauffé et ensemencé de ferments ; 6. le yaourt est versé dans des pots ; 7. un camion frigorifique livre les magasins ; 8. le yaourt est vendu au rayon frais. Compte, puis ouvre le cadenas.",
      SRC11,
      "Trois étapes se déroulent à l'intérieur de l'usine (l'analyse, la transformation et la mise en pots), sur huit étapes en tout ; deux étapes sont des transports en camion (le camion-citerne et le camion frigorifique).",
      {"cm2": ["L'analyse, la transformation et la mise en pots ont lieu à l'usine.", "Compte toutes les étapes de la liste.", "Cherche les mots « camion » dans la liste."]},
      "l11", niveaux=["CM2"],
      commun={"champs": [{"libelle": "Étapes à l'intérieur de l'usine", "valeur": "3", "longueur": 1}, {"libelle": "Étapes en tout", "valeur": "8", "longueur": 1},
                         {"libelle": "Transports en camion", "valeur": "2", "longueur": 1}]}),
]

SRC12 = LIVRET.format(n=12) + " ; " + BO2
KM = tab("Distance jusqu'en France (en kilomètres)", ["Chili", "Grèce", "Espagne", "Turquie", "Maroc"], [["11 702", "2 585", "1 013", "3 422", "2 292"]])
RECETTE = "Recette de la salade fraîcheur : 1 poire (Chili), 100 g de feta (Grèce), 1 salade (Espagne), 100 g de noisettes (Turquie), 200 g de tomates (Maroc)."
E12 = [
    E("12-1", "D'où viennent les étiquettes ?", "tri",
      {"cm1": "Sur le marché de Marseille, Yanis te montre les étiquettes d'origine des produits. Range chaque produit selon le continent d'où il vient.",
       "cm2": "Classe chaque produit du marché selon le continent d'où il vient. Le Maroc est en Afrique du Nord ; la Turquie se trouve surtout en Asie."},
      SRC12,
      "L'Espagne, la Grèce, le Portugal et l'Italie sont en Europe ; le Cameroun, l'Afrique du Sud et le Maroc en Afrique ; l'Argentine, le Chili et le Brésil en Amérique du Sud ; "
      "la Turquie est surtout en Asie ; la Nouvelle-Zélande est en Océanie.",
      {"cm1": ["L'Espagne et la Grèce sont en Europe.", "Le Cameroun et le Maroc sont en Afrique.", "Le Chili et le Brésil sont en Amérique du Sud."],
       "cm2": ["Le Maroc est au nord de l'Afrique.", "La Turquie se trouve surtout en Asie.", "La Nouvelle-Zélande est en Océanie."]},
      "l12",
      cm1=tri([("eu", "Europe"), ("af", "Afrique"), ("as", "Amérique du Sud"), ("oc", "Océanie")],
              [("Fraises (Espagne)", "eu"), ("Feta (Grèce)", "eu"), ("Bananes (Cameroun)", "af"), ("Tomates (Maroc)", "af"), ("Oranges (Afrique du Sud)", "af"),
               ("Poires (Chili)", "as"), ("Mangues (Brésil)", "as"), ("Kiwis (Nouvelle-Zélande)", "oc")]),
      cm2=tri([("eu", "Europe"), ("af", "Afrique"), ("as", "Amérique du Sud"), ("asie", "Asie"), ("oc", "Océanie")],
              [("Fraises (Espagne)", "eu"), ("Avocats (Espagne)", "eu"), ("Salade (Espagne)", "eu"), ("Feta (Grèce)", "eu"), ("Myrtilles (Portugal)", "eu"), ("Figues (Italie)", "eu"),
               ("Bananes (Cameroun)", "af"), ("Oranges (Afrique du Sud)", "af"), ("Tomates (Maroc)", "af"), ("Citrons (Argentine)", "as"), ("Poires (Chili)", "as"),
               ("Mangues (Brésil)", "as"), ("Noisettes (Turquie)", "asie"), ("Kiwis (Nouvelle-Zélande)", "oc")])),
    E("12-2", "La salade fraîcheur", "code",
      {"cm1": "Yanis prépare une salade avec des produits du monde entier. Calcule les kilomètres alimentaires de la recette, puis ouvre le cadenas. " + RECETTE + KM,
       "cm2": "Calcule les kilomètres alimentaires nécessaires pour réaliser cette salade, puis ouvre le cadenas. " + RECETTE + KM},
      SRC12 + " ; distances du livret",
      "11 702 + 2 585 + 1 013 + 3 422 + 2 292 = 21 014 km. Le chiffre des unités est 4. Deux produits (la feta de Grèce et la salade d'Espagne) viennent d'Europe.",
      {"cm1": ["Additionne les cinq distances, une par produit.", "Pose l'addition en colonnes.", "Le chiffre des unités est le dernier chiffre du résultat."],
       "cm2": ["11 702 + 2 585 + 1 013 + 3 422 + 2 292.", "Pose l'addition en colonnes !", "La Grèce et l'Espagne sont des pays d'Europe."]},
      "l12",
      cm1={"champs": [{"libelle": "Total des kilomètres alimentaires de la recette", "valeur": "21014", "longueur": 5}, {"libelle": "Chiffre des unités de ce total", "valeur": "4", "longueur": 1}]},
      cm2={"champs": [{"libelle": "Total des kilomètres alimentaires de la recette", "valeur": "21014", "longueur": 5}, {"libelle": "Chiffre des unités de ce total", "valeur": "4", "longueur": 1},
                      {"libelle": "Produits de la recette venus d'Europe", "valeur": "2", "longueur": 1}]}),
    E("12-3", "Moins de kilomètres", "qcm",
      {"cm1": "Yanis cherche comment réduire les kilomètres alimentaires. Réponds à ses questions.",
       "cm2": "Pour réduire les kilomètres alimentaires, Yanis te demande de distinguer ce qui sert de ce qui ne sert à rien. Réponds à ses questions."},
      SRC12,
      "Plus la distance est grande, plus le transport rejette de CO₂. Pour réduire les kilomètres alimentaires, on peut acheter en circuit court, privilégier les produits locaux, choisir des fruits et des légumes de saison "
      "et manger moins de viande. Manger moins salé ou ne pas laver ses fruits n'a aucun effet.",
      {"cm1": ["Le circuit court est une vente directe du producteur au consommateur.", "Le transport rejette du CO₂.", "Le sel et le lavage n'ont rien à voir avec la distance."],
       "cm2": ["Produits locaux et de saison : moins de transport.", "Manger moins salé n'a aucun rapport avec la distance parcourue.", "Circuit court : un seul intermédiaire au plus."]},
      "l12",
      cm1=qcm([("Quel geste réduit les kilomètres alimentaires ?", ["acheter en circuit court, directement au producteur", "acheter des produits venus de l'autre bout du monde", "laver ses fruits plus longtemps"], 0,
                "Moins de distance, moins de transport."),
               ("Pourquoi les kilomètres alimentaires posent-ils un problème ?", ["le transport rejette du CO₂", "les aliments perdent leur couleur", "les étiquettes deviennent illisibles"], 0,
                "Le CO₂ contribue au réchauffement climatique."),
               ("Lequel de ces gestes n'a aucun effet sur les kilomètres alimentaires ?", ["manger moins salé", "acheter local", "choisir des produits de saison"], 0, "Le sel n'a aucun rapport avec la distance.")]),
      cm2=qcm([("Quel geste réduit les kilomètres alimentaires ?", ["acheter en circuit court, directement au producteur", "acheter des produits venus de l'autre bout du monde", "laver ses fruits plus longtemps", "manger plus salé"], 0,
                "Moins de distance, moins de transport."),
               ("Pourquoi les kilomètres alimentaires posent-ils un problème ?", ["le transport rejette du CO₂ et contribue au réchauffement climatique", "les aliments perdent leur couleur", "les étiquettes deviennent illisibles", "les camions sont trop lents"], 0,
                "Plus la distance est grande, plus il y a de CO₂."),
               ("Lequel de ces gestes n'a aucun effet sur les kilomètres alimentaires ?", ["manger moins salé", "acheter local", "choisir des produits de saison", "acheter en circuit court"], 0, "Le sel n'a aucun rapport avec la distance."),
               ("Que veut dire « circuit court » ?", ["une vente directe, ou avec un seul intermédiaire, entre le producteur et le consommateur", "un trajet de moins d'un kilomètre", "un petit supermarché", "un camion plus rapide"], 0,
                "Moins d'intermédiaires, moins de transport.")])),
    E("12-4", "Du plus près au plus loin", "ordre",
      "Yanis veut savoir quel ingrédient de la salade vient de plus près. Range les ingrédients du plus proche au plus lointain, d'après les distances jusqu'en France." + KM,
      SRC12 + " ; distances du livret",
      "Dans l'ordre : la salade d'Espagne (1 013 km), les tomates du Maroc (2 292 km), la feta de Grèce (2 585 km), les noisettes de Turquie (3 422 km), puis la poire du Chili (11 702 km).",
      {"cm2": ["Compare les nombres de kilomètres.", "L'Espagne est le pays le plus proche.", "Le Chili est de l'autre côté de l'Atlantique : c'est le plus lointain."]},
      "l12", niveaux=["CM2"],
      commun=ordre(["La salade (Espagne)", "Les tomates (Maroc)", "La feta (Grèce)", "Les noisettes (Turquie)", "La poire (Chili)"])),
]

SRC13 = LIVRET.format(n=13) + " ; " + BO2 + " ; fond de carte dessiné par script (mission-geo/js/cartes.js) ; Sandre ; géomètres-experts de la Haute-Savoie (2026)"
E13 = [
    E("13-1", "La carte du relief", "plan",
      {"cm1": "Rémi, guide de haute montagne, te tend une carte de France. Place le nom de chaque fleuve et de chaque massif sur son repère : clique sur une étiquette, puis sur la case du repère." + S.fleuves(range(6)),
       "cm2": "Replace les noms des cinq fleuves, des cinq massifs montagneux de la France continentale et de la Corse sur leurs repères. Les fleuves sont en bleu sur la carte, les massifs en brun." + S.fleuves(range(11))},
      SRC13,
      "La Seine traverse Paris, au nord ; la Loire coule vers l'ouest, la Garonne vers le sud-ouest, le Rhône vers le sud et le Rhin est à l'est, à la frontière avec l'Allemagne. "
      "Les Alpes sont à l'est, les Pyrénées au sud, le Massif central au centre, le Jura et les Vosges à l'est, et la Corse est une île.",
      {"cm1": ["La Seine passe à Paris, au nord.", "Le Rhône descend vers le sud.", "Les Alpes sont à l'est, près de l'Italie."],
       "cm2": ["La Garonne descend des Pyrénées vers l'Atlantique.", "Le Jura est au nord des Alpes, le long de la frontière avec la Suisse.", "Le Massif central est au centre du pays."]},
      "l13",
      cm1=plan("La carte du relief de Rémi", [(f"Repère {i + 1}", S.FLEUVES[i][0]) for i in range(6)], colonnes=2),
      cm2=plan("La carte du relief de Rémi", [(f"Repère {i + 1}", S.FLEUVES[i][0]) for i in range(11)], colonnes=3)),
    E("13-2", "Fleuve ou rivière ?", "qcm",
      {"cm1": "Rémi te pose trois questions avant de t'emmener au bord du torrent.",
       "cm2": "Avant de remonter le torrent, Rémi te teste sur les fleuves et les massifs."},
      SRC13,
      "Un fleuve se jette dans la mer ou l'océan ; une rivière se jette dans un autre cours d'eau. La Loire est le plus long fleuve de France, avec environ 1 006 km. "
      "La Garonne descend des Pyrénées. La France compte six grands massifs montagneux.",
      {"cm1": ["Ce n'est pas une question de taille, mais de destination.", "La Loire est le plus long fleuve de France.", "Les Pyrénées sont au sud, à la frontière avec l'Espagne."],
       "cm2": ["Un fleuve se jette dans la mer ou l'océan.", "Alpes, Pyrénées, Massif central, Jura, Vosges, Corse.", "La Loire mesure environ 1 000 km."]},
      "l13",
      cm1=qcm([("Quelle est la différence entre un fleuve et une rivière ?", ["un fleuve se jette dans la mer ou l'océan ; une rivière se jette dans un autre cours d'eau", "un fleuve est plus long qu'une rivière",
                                                                              "un fleuve est plus large qu'une rivière"], 0, "Ce n'est pas une question de taille, mais de destination."),
               ("Quel est le plus long fleuve de France ?", ["la Loire", "la Seine", "le Rhône"], 0, "Environ 1 006 km."),
               ("De quel massif descend la Garonne ?", ["les Pyrénées", "les Vosges", "le Jura"], 0, "Elle descend des Pyrénées vers l'océan Atlantique.")]),
      cm2=qcm([("Quelle est la différence entre un fleuve et une rivière ?", ["un fleuve se jette dans la mer ou l'océan ; une rivière se jette dans un autre cours d'eau", "un fleuve est plus long qu'une rivière",
                                                                              "un fleuve prend sa source en montagne, une rivière en plaine", "un fleuve est plus large qu'une rivière"], 0, "Ce n'est pas une question de taille, mais de destination."),
               ("Quel est le plus long fleuve de France ?", ["la Loire", "la Seine", "le Rhône", "la Garonne"], 0, "Environ 1 006 km."),
               ("Combien de grands massifs montagneux compte la France ?", ["six", "trois", "huit", "douze"], 0, "Alpes, Pyrénées, Massif central, Jura, Vosges, Corse."),
               ("Quel massif forme la frontière avec l'Espagne ?", ["les Pyrénées", "les Alpes", "les Vosges", "le Jura"], 0, "La Garonne y prend sa source.")])),
    E("13-3", "Où se jettent les fleuves ?", "association",
      {"cm1": "Rémi veut savoir où l'eau des fleuves finit sa course. Relie chaque fleuve à la mer ou à l'océan dans lequel il se jette.",
       "cm2": "Relie chaque fleuve à la mer ou à l'océan dans lequel il se jette. Attention : deux fleuves se jettent dans l'océan Atlantique, par des estuaires différents."},
      SRC13,
      "La Seine se jette dans la Manche, la Loire dans l'océan Atlantique par son estuaire, la Garonne dans l'océan Atlantique par l'estuaire de la Gironde, le Rhône dans la mer Méditerranée et le Rhin dans la mer du Nord.",
      {"cm1": ["Le Rhône descend vers le sud : il se jette dans la Méditerranée.", "La Seine se jette près du Havre, en Normandie.", "Le Rhin coule vers le nord."],
       "cm2": ["La Loire coule vers l'ouest.", "La Garonne forme l'estuaire de la Gironde.", "Le Rhin longe l'Allemagne avant de rejoindre la mer du Nord."]},
      "l13",
      cm1={"paires": [{"g": "La Seine", "d": "La Manche"}, {"g": "La Loire", "d": "L'océan Atlantique (estuaire de la Loire)"}, {"g": "La Garonne", "d": "L'océan Atlantique (estuaire de la Gironde)"},
                      {"g": "Le Rhône", "d": "La mer Méditerranée"}, {"g": "Le Rhin", "d": "La mer du Nord"}]},
      cm2={"paires": [{"g": "La Seine", "d": "La Manche"}, {"g": "La Loire", "d": "L'océan Atlantique (estuaire de la Loire)"}, {"g": "La Garonne", "d": "L'océan Atlantique (estuaire de la Gironde)"},
                      {"g": "Le Rhône", "d": "La mer Méditerranée"}, {"g": "Le Rhin", "d": "La mer du Nord"}]}),
    E("13-4", "Les repères à connaître", "code",
      "Rémi te rappelle quelques repères à connaître par cœur. Réponds, puis ouvre le cadenas.",
      SRC13,
      "La France compte six grands massifs montagneux et cinq grands fleuves ; le mont Blanc, dans les Alpes, culmine à environ 4 807 mètres (4 807,47 m en septembre 2026).",
      {"cm2": ["Alpes, Pyrénées, Massif central, Jura, Vosges, Corse : compte-les.", "Seine, Loire, Garonne, Rhône, Rhin.", "Le mont Blanc est le plus haut sommet d'Europe occidentale : environ 4 800 m."]},
      "l13", niveaux=["CM2"],
      commun={"champs": [{"libelle": "Nombre de grands massifs montagneux", "valeur": "6", "longueur": 1}, {"libelle": "Nombre de grands fleuves", "valeur": "5", "longueur": 1},
                         {"libelle": "Altitude du mont Blanc, en mètres (arrondie)", "valeur": "4807", "longueur": 4}]}),
]


SALLES_E = [
    {"num": 1, "titre": "Le grand départ — Ma commune", "enigmes": E1},
    {"num": 2, "titre": "Direction Dijon ! — Des territoires emboîtés", "enigmes": E2},
    {"num": 3, "titre": "Vivre à Clamecy — L'espace rural", "enigmes": E3},
    {"num": 4, "titre": "Besançon — Travailler en ville", "enigmes": E4},
    {"num": 5, "titre": "Les Rousses — Les loisirs de la montagne", "enigmes": E5},
    {"num": 6, "titre": "Étretat — La station balnéaire", "enigmes": E6},
    {"num": 7, "titre": "Biarritz — Le littoral atlantique", "enigmes": E7},
    {"num": 8, "titre": "Dhaka — Les inégalités dans le monde", "enigmes": E8},
    {"num": 9, "titre": "Bamako — Les pratiques alimentaires", "enigmes": E9},
    {"num": 10, "titre": "La cantine — Produits agricoles et transformés", "enigmes": E10},
    {"num": 11, "titre": "Issenheim — Du lait au yaourt", "enigmes": E11},
    {"num": 12, "titre": "Marseille — D'où vient ce que l'on mange ?", "enigmes": E12},
    {"num": 13, "titre": "Les Alpes — Fleuves et massifs", "enigmes": E13},
]

# ============================================================================ DIALOGUES
PERSONNAGES = {
    "atlas": {"nom": "Professeur Atlas", "role": "Géographe et chef de la mission, il dirige le bureau des agents depuis ta commune"},
    "lena": {"nom": "Léna", "role": "Agente de terrain, elle attend les recrues à Dijon"},
    "malik": {"nom": "Malik", "role": "Agent infiltré à Clamecy, spécialiste des chiffres"},
    "zoe": {"nom": "Zoé", "role": "Agente chargée de rencontrer les sources à Besançon"},
    "hugo": {"nom": "Hugo", "role": "Agent et moniteur de ski à la station des Rousses"},
    "ines": {"nom": "Inès", "role": "Agente de la côte normande, elle fournit aux recrues leurs couvertures"},
    "theo": {"nom": "Théo", "role": "Agent et sauveteur sur la Grande Plage de Biarritz"},
    "nour": {"nom": "Nour", "role": "Agente envoyée à Dhaka, elle enquête au milieu des marchés"},
    "aminata": {"nom": "Aminata", "role": "Agente de Bamako, elle t'emmène au marché pour comprendre comment on se nourrit au Mali"},
    "camille": {"nom": "Camille", "role": "Cheffe de la cantine de l'école, elle t'a engagé comme aide pour quelques jours"},
    "manon": {"nom": "Manon", "role": "Éleveuse à la ferme de Bray, elle te fait suivre le lait jusqu'à l'usine"},
    "yanis": {"nom": "Yanis", "role": "Agent de Marseille, il lit les étiquettes d'origine sur les marchés"},
    "remi": {"nom": "Rémi", "role": "Guide de haute montagne dans les Alpes, il lit les cartes du relief et des cours d'eau"},
}
SALLES_D = [
    {"num": 1, "titre": "Le grand départ", "decor": "bureau-atlas", "motCle": "COMMUNE",
     "lieu": "Le bureau du Professeur Atlas, dans ta commune",
     "description": "Un bureau rempli de cartes : un grand plan de la commune au mur, un globe, une valise vide ouverte sur la table, des tampons et des dossiers.",
     "sens": ["À voir : le plan de la commune punaisé au mur", "À entendre : le tic-tac de la pendule et le froissement des cartes", "À sentir : le vieux papier et l'encre des tampons"],
     "dialogue_intro": {"perso": "atlas", "nom": "Professeur Atlas", "texte": "Agents, une valise pleine d'informations secrètes a été volée cette nuit. Je vous ai choisis pour la retrouver. "
                        "Mais un bon agent connaît d'abord son propre terrain : avant de partir, faites vos démarches dans la commune. Chaque lieu a son rôle."},
     "dialogue_reussite": {"perso": "atlas", "nom": "Professeur Atlas", "texte": "Parfait. Vos démarches sont faites et vous savez à quoi sert chaque lieu de la <b>COMMUNE</b>. "
                           "Notez ce mot. Les lettres marquées ont parlé : on vous attend à Dijon. Léna vous y retrouvera."}},
    {"num": 2, "titre": "Direction Dijon !", "decor": "dijon-palais", "motCle": "EMBOÎTÉS",
     "lieu": "Dijon, place de la Libération, devant le palais des ducs de Bourgogne",
     "description": "Une place en demi-cercle bordée de façades claires ; au fond, le palais et sa haute tour. Des fontaines au ras du sol, des passants, des pigeons.",
     "sens": ["À voir : la tour du palais qui domine la place", "À entendre : l'eau des fontaines et les pas des passants", "À sentir : l'air frais du matin et le pain chaud d'une boulangerie"],
     "dialogue_intro": {"perso": "lena", "nom": "Léna", "texte": "Bienvenue à Dijon, chef-lieu de la région Bourgogne-Franche-Comté. Je suis Léna. Avant de vous confier la suite, "
                        "je dois être sûre que vous savez vous présenter : votre commune, votre département, votre région, votre pays, votre continent."},
     "dialogue_reussite": {"perso": "lena", "nom": "Léna", "texte": "Vous voilà avec un vrai passeport géographique : commune, département, région, pays, continent, tous <b>EMBOÎTÉS</b>. "
                           "Notez ce mot. Sur le planisphère, sept continents : sept pistes possibles. Malik a une piste à Clamecy."}},
    {"num": 3, "titre": "Vivre à Clamecy", "decor": "clamecy-bourg", "motCle": "DENSITÉ",
     "lieu": "Clamecy, un bourg de la Nièvre, au bord de l'Yonne",
     "description": "Des toits serrés autour d'une église, un pont de pierre sur la rivière, le canal et ses péniches, puis des champs et des forêts à perte de vue.",
     "sens": ["À voir : les toits serrés autour du clocher", "À entendre : la rivière sous le pont et un tracteur au loin", "À sentir : l'herbe coupée et la terre humide"],
     "dialogue_intro": {"perso": "malik", "nom": "Malik", "texte": "Salut, c'est Malik. On m'a dit qu'un informaticien lié au vol se cachait ici, à Clamecy. "
                        "Pour passer inaperçu, il faut vivre comme les habitants : savoir combien ils sont, ce qu'on trouve ici, et comment on se déplace."},
     "dialogue_reussite": {"perso": "malik", "nom": "Malik", "texte": "Fausse piste : l'informaticien est parti depuis longtemps. Mais vos calculs de <b>DENSITÉ</b> valent de l'or. "
                           "Notez ce mot. Prochaine étape : Besançon, où Zoé attend une source."}},
    {"num": 4, "titre": "Besançon, travailler en ville", "decor": "besancon-ville", "motCle": "TERTIAIRE",
     "lieu": "Besançon, préfecture du Doubs, dans la boucle de la rivière",
     "description": "Une ville serrée dans la boucle du Doubs, dominée par une citadelle. Des rues commerçantes, des tramways, des bureaux et, au loin, l'hôpital.",
     "sens": ["À voir : la citadelle sur la colline et la rivière qui fait une boucle", "À entendre : la sonnerie du tramway et le bruit des terrasses", "À sentir : le café des terrasses et l'air de la rivière"],
     "dialogue_intro": {"perso": "zoe", "nom": "Zoé", "texte": "Je suis Zoé. Une source a promis de parler, mais elle n'a pas dit où elle travaille. "
                        "En ville, des milliers de personnes exercent des métiers très différents. Aidez-moi à les reconnaître : nous la trouverons."},
     "dialogue_reussite": {"perso": "zoe", "nom": "Zoé", "texte": "La source a parlé. Ici, presque tout le monde travaille dans le secteur <b>TERTIAIRE</b> : notez ce mot. "
                           "Et retenez sa confidence : la valise n'est plus en Europe. Hugo vous attend à la montagne, pour souffler un peu."}},
    {"num": 5, "titre": "Les loisirs de la montagne", "decor": "rousses-station", "motCle": "TOURISME",
     "lieu": "La station des Rousses, dans le Haut-Jura, au pied de la Dôle",
     "description": "Des pistes enneigées, des télésièges, des chalets de bois ; au sommet de la Dôle, une grosse boule blanche ; à l'horizon, les Alpes.",
     "sens": ["À voir : les télésièges et la boule blanche au sommet de la Dôle", "À entendre : le crissement de la neige et le moteur des canons à neige", "À sentir : le froid sec et le bois des chalets"],
     "dialogue_intro": {"perso": "hugo", "nom": "Hugo", "texte": "Salut, je suis Hugo, moniteur ici. Une pause bien méritée, mais gardez l'œil ouvert : "
                        "la montagne attire beaucoup de monde, et tout ce monde laisse des traces."},
     "dialogue_reussite": {"perso": "hugo", "nom": "Hugo", "texte": "Bravo : vous savez ce que le <b>TOURISME</b> apporte à la montagne, et ce qu'il lui coûte. Notez ce mot. "
                           "Et souvenez-vous de la remarque du skieur : là où va la valise, c'est l'hiver en même temps qu'ici."}},
    {"num": 6, "titre": "Étretat, station balnéaire", "decor": "etretat-falaises", "motCle": "BALNÉAIRE",
     "lieu": "Étretat, en Normandie, sur la promenade du front de mer",
     "description": "Une plage de galets au pied de hautes falaises blanches ; à gauche, une arche et une aiguille de craie plantée dans la mer. Sur la promenade, la foule et les voitures.",
     "sens": ["À voir : l'arche et l'aiguille de craie au pied de la falaise", "À entendre : les galets roulés par les vagues et les klaxons des voitures", "À sentir : l'air salé et les frites des kiosques"],
     "dialogue_intro": {"perso": "ines", "nom": "Inès", "texte": "Je suis Inès. La valise a quitté l'Europe, mais le voleur est passé par ici, à Étretat, et une source l'a vu. "
                        "Elle ne parle qu'aux gens du coin : pour l'approcher, tu vas te faire passer pour un guide touristique. Il faudra connaître la ville, et ce que vivent ses habitants."},
     "dialogue_reussite": {"perso": "ines", "nom": "Inès", "texte": "Ta couverture a tenu : la source t'a pris pour un vrai guide de station <b>BALNÉAIRE</b>. Notez ce mot. "
                           "Elle a parlé : le voleur a longé la côte jusqu'à l'océan Atlantique. Théo vous attend à Biarritz."}},
    {"num": 7, "titre": "Le littoral atlantique", "decor": "biarritz-plage", "motCle": "LITTORAL",
     "lieu": "Biarritz, sur la Grande Plage, au bord de l'océan Atlantique",
     "description": "Une longue plage de sable au pied de villas et d'hôtels ; des surfeurs dans les rouleaux, un phare sur la pointe, des parasols serrés jusqu'à l'eau.",
     "sens": ["À voir : les rouleaux de l'océan et les surfeurs", "À entendre : le fracas des vagues et le sifflet du sauveteur", "À sentir : la crème solaire et le sable chaud"],
     "dialogue_intro": {"perso": "theo", "nom": "Théo", "texte": "Salut, je suis Théo, sauveteur sur cette plage. Le voleur a laissé un message à un loueur de planches, mais il parle de mers et d'océans. "
                        "Avant de le lire, il faut savoir nommer les eaux qui bordent la France, et comprendre qui vient ici chaque été."},
     "dialogue_reussite": {"perso": "theo", "nom": "Théo", "texte": "Bien joué : vous savez lire le <b>LITTORAL</b> comme un vrai sauveteur. Notez ce mot. "
                           "Le message du voleur est clair maintenant : une escale lointaine, à Dhaka, au Bangladesh. Nour y est déjà."}},
    {"num": 8, "titre": "Niveaux de vie dans le monde", "decor": "dhaka-marche", "motCle": "INÉGALITÉS",
     "lieu": "Dhaka, capitale du Bangladesh, dans un marché très animé",
     "description": "Une rue étroite pleine de monde : des étals de tissus et de fruits, des pousse-pousse à vélo, des fils électriques emmêlés au-dessus des têtes, des immeubles neufs au loin.",
     "sens": ["À voir : les pousse-pousse colorés et les étals de tissus", "À entendre : les sonnettes des vélos et les voix des marchands", "À sentir : les épices et la poussière chaude"],
     "dialogue_intro": {"perso": "nour", "nom": "Nour", "texte": "Bienvenue à Dhaka. Je suis Nour. Ici, tu vas voir des immeubles neufs, et juste à côté, des enfants qui travaillent au lieu d'aller à l'école. "
                        "Pour comprendre la suite de la piste, il faut d'abord comprendre pourquoi tout le monde n'a pas le même niveau de vie."},
     "dialogue_reussite": {"perso": "nour", "nom": "Nour", "texte": "Vous avez compris les <b>INÉGALITÉS</b> qui séparent les pays du monde. Notez ce mot. "
                           "Et regardez ce qu'un marchand m'a tendu : une photo froissée d'un drapeau. On n'en voit que deux couleurs."}},
    {"num": 9, "titre": "Au marché de Bamako", "decor": "bamako-marche", "motCle": "PRATIQUES",
     "lieu": "Bamako, capitale du Mali, dans un marché en plein air",
     "description": "Un marché animé : des étals de millet, d'arachides et de mangues sous des parasols, des vendeuses qui discutent, des motos qui passent et, accrochée à un poteau, une ardoise couverte de prix.",
     "sens": ["À voir : les tas de millet, d'arachides et de mangues sous les parasols", "À entendre : les voix des vendeuses et le moteur des motos", "À sentir : les épices, la mangue mûre et la poussière chaude"],
     "dialogue_intro": {"perso": "aminata", "nom": "Aminata", "texte": "Bienvenue à Bamako, au Mali. Je suis Aminata. Pour te remettre de ton long voyage, viens faire un tour au marché : "
                        "tu y verras des aliments que tu ne connais pas, et beaucoup de ceux que tu connais coûtent ici une fortune. Regardons pourquoi."},
     "dialogue_reussite": {"perso": "aminata", "nom": "Aminata", "texte": "Tu as compris que les <b>PRATIQUES</b> alimentaires dépendent du climat, des habitudes et surtout des revenus. Notez ce mot. "
                           "Regarde : une marchande a reconnu le drapeau de ta photographie froissée, et elle a quelque chose à ajouter."}},
    {"num": 10, "titre": "Les produits consommés", "decor": "cantine-ecole", "motCle": "TRANSFORMÉS",
     "lieu": "La cantine de l'école, à l'heure du déjeuner",
     "description": "Un réfectoire lumineux : de longues tables, des plateaux alignés, un comptoir en inox et, derrière, la cuisine où l'on voit des casseroles fumer.",
     "sens": ["À voir : les plateaux alignés sur le comptoir en inox", "À entendre : le bruit des couverts et les voix des enfants", "À sentir : la soupe chaude et le pain frais"],
     "dialogue_intro": {"perso": "camille", "nom": "Camille", "texte": "Salut, je suis Camille, la cheffe de la cantine. On t'a placé ici comme aide pour quelques jours : "
                        "le temps de réfléchir aux indices déjà récupérés. En cuisine, on se pose toujours la même question : d'où vient chaque aliment du plateau ?"},
     "dialogue_reussite": {"perso": "camille", "nom": "Camille", "texte": "Plateau trié ! Un produit agricole vient de la nature ; un produit <b>TRANSFORMÉ</b> est fabriqué à partir de lui. "
                           "Notez ce mot. Et une question me trotte dans la tête : par où passe donc un yaourt avant d'arriver dans ton assiette ?"}},
    {"num": 11, "titre": "Chaînes de production", "decor": "issenheim-usine", "motCle": "CHAÎNE",
     "lieu": "La ferme de Bray, puis l'usine de yaourts d'Issenheim, en Alsace",
     "description": "Un pré où paissent des vaches et, plus loin, une usine blanche : de grands réservoirs en inox, des tuyaux, une chaîne qui remplit des pots à la file, des camions frigorifiques à quai.",
     "sens": ["À voir : les réservoirs en inox et la chaîne qui remplit les pots", "À entendre : le ronronnement des machines et le bip des chariots", "À sentir : le lait tiède et l'air frais de la chambre froide"],
     "dialogue_intro": {"perso": "manon", "nom": "Manon", "texte": "Je suis Manon, éleveuse à la ferme de Bray. Les malfaiteurs sont partout en France : pour t'approcher d'eux, "
                        "tu te fais passer pour un producteur et tu suis notre lait jusqu'à l'usine de yaourts d'Issenheim, en Alsace. Suis bien chaque étape."},
     "dialogue_reussite": {"perso": "manon", "nom": "Manon", "texte": "Tu connais maintenant toute la <b>CHAÎNE</b> de production du yaourt, du pré au frigo. Notez ce mot. "
                           "Écoute : dans le vestiaire, une radio grésille dans une langue que tu ne comprends pas… mais que tu reconnais."}},
    {"num": 12, "titre": "L'heure du ravitaillement", "decor": "marseille-marche", "motCle": "KILOMÈTRES",
     "lieu": "Marseille, sur un marché de quartier",
     "description": "Un marché ensoleillé : des cageots de fruits et de légumes, des étiquettes d'origine piquées dans les étals, des paniers qui se remplissent et, au loin, la mer.",
     "sens": ["À voir : les cageots de fruits et leurs étiquettes d'origine", "À entendre : les marchands qui crient leurs prix", "À sentir : les agrumes, les herbes et l'air salé"],
     "dialogue_intro": {"perso": "yanis", "nom": "Yanis", "texte": "Salut, c'est Yanis, de Marseille. Chez nous, la nourriture est abondante, mais regarde les étiquettes : "
                        "d'où viennent vraiment ces fruits et ces légumes ? Combien de kilomètres ont-ils parcourus avant d'arriver dans ton panier ?"},
     "dialogue_reussite": {"perso": "yanis", "nom": "Yanis", "texte": "21 014 kilomètres pour une seule salade ! Tu sais maintenant compter les <b>KILOMÈTRES</b> alimentaires. Notez ce mot. "
                           "Le chiffre des unités de ce total rejoint ton carnet : il te servira plus tard."}},
    {"num": 13, "titre": "L'eau en France : fleuves et massifs", "decor": "alpes-torrent", "motCle": "MASSIFS",
     "lieu": "Les Alpes, au bord d'un torrent de montagne",
     "description": "Un torrent clair qui dévale entre des rochers, des sapins, des névés accrochés aux pentes et, tout en haut, des sommets enneigés baignés de lumière.",
     "sens": ["À voir : le torrent qui dévale et les sommets enneigés", "À entendre : le grondement de l'eau sur les rochers", "À sentir : la résine des sapins et l'air froid"],
     "dialogue_intro": {"perso": "remi", "nom": "Rémi", "texte": "Je suis Rémi, guide de haute montagne. La piste des produits agricoles n'a rien donné : il te reste la piste de l'eau. "
                        "Pour comprendre d'où elle vient, il faut savoir lire une carte du relief et des cours d'eau."},
     "dialogue_reussite": {"perso": "remi", "nom": "Rémi", "texte": "Cinq fleuves, six <b>MASSIFS</b> : la carte de France n'a plus de secret pour toi. Notez ce mot. "
                           "Le nombre de massifs rejoint ton carnet. Le chemin de l'eau, lui, continue : la mission aussi."}},
]
INTRO = ("Bienvenue au bureau du Professeur Atlas. Une valise contenant des informations secrètes a été volée. Séance après séance, "
         "vous allez suivre sa trace à travers la France, puis le monde. Chaque séance réussie vous donne un mot pour le coffre et un indice pour votre carnet de mission.")

# ============================================================================ LEÇONS
LECONS = [
    {"id": "l01", "salle": 1, "icone": "1", "titre": "La commune, le premier territoire", "duree": "3 min", "niveau": "CM1-CM2",
     "objectifs": ["Savoir ce qu'est une commune et qui la dirige", "Identifier la fonction des principaux lieux d'une commune", "Distinguer un commerce et un service public"],
     "contenu": {"cm1": "<h4>Ma commune</h4><p>La <b>commune</b> est le plus petit territoire de France. Elle est dirigée par un <b>maire</b>. "
                        "Dans la commune, chaque lieu a une <b>fonction</b> : la mairie est <b>administrative</b>, l'école est <b>éducative</b>, la boulangerie est <b>commerciale</b>, "
                        "le cabinet médical sert à la <b>santé</b>, le parc aux <b>loisirs</b>.</p>",
                 "cm2": F.html(F.LECON_COMMUNE)},
     "lexique": [{"mot": "commune", "def": "le plus petit territoire administratif français, dirigé par un maire"}, {"mot": "maire", "def": "personne élue qui dirige la commune"},
                 {"mot": "fonction d'un lieu", "def": "ce à quoi ce lieu sert : se soigner, apprendre, acheter, se distraire…"},
                 {"mot": "service public", "def": "service rendu à tous les habitants"}],
     "sources": BO + " ; DGCL, « Les structures territoriales au 1er janvier 2026 »."},
    {"id": "l02", "salle": 2, "icone": "2", "titre": "Des territoires emboîtés", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Emboîter commune, département, région, pays, continent", "Nommer et situer sa région et son département", "Savoir qui décide : commune, département, région"],
     "contenu": {"cm1": "<h4>Du plus petit au plus grand</h4><p>J'habite une <b>commune</b>, dans un <b>département</b>, dans une <b>région</b>, dans un <b>pays</b> (la France), "
                        "sur un <b>continent</b> (l'Europe). La France métropolitaine compte <b>13 régions</b>. Il y a <b>7 continents</b>.</p>"
                        "<h4>Qui décide ?</h4><p>L'école → la commune ; le collège → le département ; le lycée → la région.</p>",
                 "cm2": F.html(F.LECON_EMBOITE)},
     "lexique": [{"mot": "département", "def": "territoire dirigé par un conseil départemental ; il porte un numéro"}, {"mot": "région", "def": "grand territoire regroupant plusieurs départements"},
                 {"mot": "préfecture", "def": "ville principale d'un département"}, {"mot": "continent", "def": "très grande étendue de terre"}],
     "sources": BO + " ; Insee (population au 1er janvier 2026)."},
    {"id": "l03", "salle": 3, "icone": "3", "titre": "L'espace rural et la densité", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Reconnaître un espace rural", "Calculer une densité de population", "Dire les avantages et les inconvénients de la vie à la campagne"],
     "contenu": {"cm1": "<h4>La campagne</h4><p>Dans un <b>espace rural</b>, il y a peu d'habitants et beaucoup de champs, de prairies et de forêts : la <b>densité</b> est faible.</p>"
                        "<h4>Calculer une densité</h4><p>Densité = nombre d'habitants ÷ superficie en km². 4 habitants sur 4 km², c'est 1 habitant par km².</p>",
                 "cm2": F.html(F.LECON_RURAL)},
     "lexique": [{"mot": "espace rural", "def": "espace peu peuplé, marqué par l'agriculture et les paysages naturels"}, {"mot": "densité de population", "def": "nombre d'habitants par km²"},
                 {"mot": "village", "def": "commune rurale de moins de 2 000 habitants"}, {"mot": "bourg", "def": "commune rurale plus grande, avec commerces et services"}],
     "sources": BO + " ; banatic.interieur.gouv.fr (Clamecy)."},
    {"id": "l04", "salle": 4, "icone": "4", "titre": "Travailler en ville : les trois secteurs", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Identifier les grands espaces d'une ville", "Classer un métier dans le secteur primaire, secondaire ou tertiaire", "Comprendre l'évolution des emplois en France"],
     "contenu": {"cm1": "<h4>La ville</h4><p>En ville, beaucoup de personnes vivent sur peu d'espace : la densité est forte. On y trouve le centre-ville, des bureaux, l'hôpital, des centres commerciaux.</p>"
                        "<h4>Trois secteurs</h4><p><b>Primaire</b> : on exploite la nature. <b>Secondaire</b> : on transforme. <b>Tertiaire</b> : on rend un service. "
                        "Aujourd'hui, plus de 3 emplois sur 4 sont dans le tertiaire.</p>",
                 "cm2": F.html(F.LECON_VILLE)},
     "lexique": [{"mot": "secteur primaire", "def": "activités qui exploitent les ressources naturelles"}, {"mot": "secteur secondaire", "def": "activités qui transforment les matières premières"},
                 {"mot": "secteur tertiaire", "def": "activités de services"}, {"mot": "quartier d'affaires", "def": "quartier de bureaux et d'entreprises"}],
     "sources": BO + " ; Insee, enquête Emploi 2024 ; ministère de l'Agriculture, CEP, « La population paysanne, repères historiques » (2016)."},
    {"id": "l05", "salle": 5, "icone": "5", "titre": "La montagne, un espace de loisirs à ménager", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Nommer les loisirs pratiqués en montagne", "Décrire une station de montagne", "Identifier les effets du tourisme sur l'environnement"],
     "contenu": {"cm1": "<h4>Les loisirs de la montagne</h4><p>On y fait du ski, du snowboard, de la raquette, mais aussi de la randonnée, de l'escalade ou du rafting. "
                        "Une <b>station</b> accueille les touristes : remontées mécaniques, pistes, chalets.</p>"
                        "<h4>Le prix du tourisme</h4><p>Les voitures polluent l'air, les canons à neige prélèvent de l'eau, les télésièges consomment de l'énergie, "
                        "les constructions réduisent la biodiversité. Mais le tourisme apporte aussi des emplois.</p>",
                 "cm2": F.html(F.LECON_MONTAGNE)},
     "lexique": [{"mot": "station de montagne", "def": "lieu aménagé pour accueillir des touristes en montagne"}, {"mot": "remontée mécanique", "def": "installation qui monte les skieurs en haut des pistes"},
                 {"mot": "neige de culture", "def": "neige fabriquée par des canons à neige, avec beaucoup d'eau"}, {"mot": "biodiversité", "def": "ensemble des êtres vivants d'un milieu"}],
     "sources": BO + " ; Office de tourisme de la station des Rousses (La Dôle, 1 677 m)."},
    {"id": "l06", "salle": 6, "icone": "6", "titre": "Le littoral touristique : la station balnéaire", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Définir une station balnéaire", "Identifier les activités proposées aux touristes", "Peser les effets positifs et négatifs de la fréquentation touristique"],
     "contenu": {"cm1": "<h4>La station balnéaire</h4><p>Une <b>station balnéaire</b> est un lieu de séjour situé en bord de mer, aménagé pour accueillir des touristes. "
                        "À Étretat, en Normandie, on randonne sur les falaises, on fait du kayak, on visite des maisons célèbres.</p>"
                        "<h4>Le prix du succès</h4><p>Le tourisme crée des <b>emplois</b> et des <b>animations</b>. Mais il apporte aussi des <b>embouteillages</b>, des <b>déchets</b> "
                        "et des <b>logements plus chers</b> : des habitants partent.</p>",
                 "cm2": F.html(F.LECON_BALNEAIRE)},
     "lexique": [{"mot": "station balnéaire", "def": "lieu de séjour situé en bord de mer, aménagé pour le tourisme"},
                 {"mot": "surfréquentation", "def": "présence de trop de visiteurs pour la capacité d'un lieu"},
                 {"mot": "saisonnier", "def": "qui ne dure qu'une partie de l'année, l'été par exemple"},
                 {"mot": "patrimoine", "def": "richesses naturelles et culturelles héritées du passé"}],
     "sources": BO2 + " ; Insee (Étretat) ; " + OT + " ; Francetvinfo, août 2022."},
    {"id": "l07", "salle": 7, "icone": "7", "titre": "Les mers et l'océan qui bordent la France", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Nommer et situer les mers et l'océan qui bordent la France", "Nommer différents types d'hébergements touristiques", "Mesurer l'effet des touristes sur la densité"],
     "contenu": {"cm1": "<h4>Quatre étendues d'eau</h4><p>La France est bordée par la <b>mer du Nord</b> (au nord), la <b>Manche</b> (entre la France et le Royaume-Uni), "
                        "l'<b>océan Atlantique</b> (à l'ouest) et la <b>mer Méditerranée</b> (au sud, autour de la Corse).</p>"
                        "<h4>Le littoral en été</h4><p>Le <b>littoral</b>, c'est le bord de mer. L'été, les vacanciers dorment à l'hôtel, au camping, dans un gîte… "
                        "La population des communes du littoral peut être multipliée par dix ou plus.</p>",
                 "cm2": F.html(F.LECON_LITTORAL)},
     "lexique": [{"mot": "littoral", "def": "zone de contact entre la terre et la mer"}, {"mot": "océan", "def": "très vaste étendue d'eau salée qui sépare des continents"},
                 {"mot": "hébergement", "def": "lieu où l'on dort pendant un séjour"}, {"mot": "population saisonnière", "def": "population présente seulement pendant une partie de l'année"}],
     "sources": BO2 + " ; Insee (Étretat : 4,07 km², 1 102 habitants)."},
    {"id": "l08", "salle": 8, "icone": "8", "titre": "Les inégalités de niveau de vie", "duree": "5 min", "niveau": "CM1-CM2",
     "objectifs": ["Identifier les manifestations des inégalités de niveau de vie", "Localiser sur un planisphère des pays riches et des pays pauvres", "Lire un tableau d'indicateurs de développement"],
     "contenu": {"cm1": "<h4>Tout le monde n'a pas le même niveau de vie</h4><p>Pour comparer les pays, on regarde le <b>revenu par habitant</b>, l'<b>espérance de vie</b> "
                        "et la <b>durée de la scolarisation</b>. Les pays riches sont surtout en Amérique du Nord, en Europe et en Océanie ; les pays pauvres, surtout en Afrique.</p>"
                        "<h4>Les enfants et la pauvreté</h4><p>Dans les pays pauvres, des enfants <b>travaillent</b> au lieu d'aller à l'école. "
                        "La Convention internationale des droits de l'enfant les protège.</p>",
                 "cm2": F.html(F.LECON_INEGALITES)},
     "lexique": [{"mot": "niveau de vie", "def": "ce que les habitants peuvent se procurer avec leurs revenus"}, {"mot": "espérance de vie", "def": "nombre moyen d'années que l'on peut espérer vivre"},
                 {"mot": "indicateur", "def": "nombre qui permet de mesurer et de comparer"}, {"mot": "pays développé", "def": "pays où le niveau de vie, la santé et l'école sont élevés"}],
     "sources": BO2 + " ; " + S.SOURCE_PNUD + " ; OIT et UNICEF, « Travail des enfants : estimations mondiales 2024 » (2025) ; World Inequality Lab, Rapport sur les inégalités mondiales 2022."},
    {"id": "l09", "salle": 9, "icone": "9", "titre": "Se nourrir ici et ailleurs", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Comparer l'alimentation dans un pays riche et dans un pays pauvre", "Comprendre le lien entre revenus et alimentation", "Situer les pays où la sous-alimentation est forte"],
     "contenu": {"cm1": "<h4>On ne mange pas la même chose partout</h4><p>Les <b>pratiques alimentaires</b> dépendent du climat, des habitudes et surtout des <b>revenus</b>. "
                        "Au <b>Mali</b>, on mange surtout ce qui est produit sur place : millet, riz, arachides, gombo, mangue. Les aliments <b>importés</b> coûtent très cher.</p>"
                        "<h4>La sous-alimentation</h4><p>Quand on ne mange pas assez pour couvrir ses besoins, on parle de <b>sous-alimentation</b>. Elle touche surtout l'Afrique subsaharienne et Haïti.</p>",
                 "cm2": F.html(F.LECON_ALIM)},
     "lexique": [{"mot": "pratique alimentaire", "def": "manière de se nourrir propre à un pays ou à une région"}, {"mot": "sous-alimentation", "def": "le fait de ne pas manger assez pour couvrir ses besoins"},
                 {"mot": "importer", "def": "faire venir un produit depuis un autre pays"}, {"mot": "enclavé", "def": "qui n'a pas d'accès à la mer"}],
     "sources": BO2 + " ; FAO, « L'état de la sécurité alimentaire et de la nutrition dans le monde » (SOFI 2025) ; livret « Mission géographique », séance 9."},
    {"id": "l10", "salle": 10, "icone": "10", "titre": "Produits agricoles et produits transformés", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Distinguer un produit agricole d'un produit transformé", "Relier un produit transformé à son produit agricole d'origine", "Nommer les espaces de production et les métiers"],
     "contenu": {"cm1": "<h4>Deux sortes de produits</h4><p>Un <b>produit agricole</b> vient directement de la nature : pomme, carotte, œuf, lait. "
                        "Un <b>produit transformé</b> est fabriqué <b>à partir</b> d'un produit agricole : le pain vient du blé, le fromage du lait, le chocolat du cacao.</p>"
                        "<h4>Des métiers</h4><p>L'<b>éleveur</b>, le <b>céréalier</b>, le <b>maraîcher</b> et l'<b>arboriculteur</b> produisent nos aliments.</p>",
                 "cm2": F.html(F.LECON_PRODUITS)},
     "lexique": [{"mot": "produit agricole", "def": "produit qui vient directement de la culture ou de l'élevage"}, {"mot": "produit transformé", "def": "produit fabriqué à partir d'un ou de plusieurs produits agricoles"},
                 {"mot": "maraîcher", "def": "agriculteur qui cultive des légumes"}, {"mot": "verger", "def": "terrain planté d'arbres fruitiers"}],
     "sources": BO2 + " ; livret « Mission géographique », séance 10."},
    {"id": "l11", "salle": 11, "icone": "11", "titre": "La chaîne de production d'un aliment : du lait au yaourt", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Remettre dans l'ordre les étapes de la production d'un yaourt", "Identifier ce qui se passe à la ferme, à l'usine et au magasin", "Comprendre le rôle de la chaîne du froid"],
     "contenu": {"cm1": "<h4>Du pré au frigo</h4><p>La <b>chaîne de production</b> regroupe les étapes qui séparent le lait du yaourt : la <b>traite</b> à la ferme, le <b>camion-citerne</b>, "
                        "l'<b>usine</b> (analyse, ferments, pots), les <b>camions frigorifiques</b> et le <b>magasin</b>.</p>"
                        "<h4>Le froid</h4><p>La <b>chaîne du froid</b> ne doit jamais être interrompue : sans froid, le lait tourne.</p>",
                 "cm2": F.html(F.LECON_YAOURT)},
     "lexique": [{"mot": "chaîne de production", "def": "suite des étapes de la matière première au produit consommé"}, {"mot": "traite", "def": "action de recueillir le lait de la vache"},
                 {"mot": "ferment", "def": "micro-organisme ajouté au lait pour le transformer en yaourt"}, {"mot": "chaîne du froid", "def": "maintien du froid tout au long du transport et du stockage"}],
     "sources": BO2 + " ; livret « Mission géographique », séance 11."},
    {"id": "l12", "salle": 12, "icone": "12", "titre": "Les kilomètres alimentaires et la consommation responsable", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Calculer les kilomètres alimentaires d'un repas", "Localiser l'origine des produits consommés", "Proposer des gestes pour réduire l'impact de son alimentation"],
     "contenu": {"cm1": "<h4>Combien de kilomètres ?</h4><p>Les <b>kilomètres alimentaires</b> sont la distance parcourue par un aliment avant d'arriver dans l'assiette. Plus elle est grande, plus le transport rejette de <b>CO₂</b>.</p>"
                        "<h4>Que faire ?</h4><p>Acheter en <b>circuit court</b>, choisir des produits <b>locaux</b> et de <b>saison</b>.</p>",
                 "cm2": F.html(F.LECON_KM)},
     "lexique": [{"mot": "kilomètres alimentaires", "def": "distance totale parcourue par un aliment jusqu'au consommateur"}, {"mot": "circuit court", "def": "vente directe, ou avec un seul intermédiaire, entre producteur et consommateur"},
                 {"mot": "produit de saison", "def": "produit récolté au moment naturel de sa production"}, {"mot": "CO₂", "def": "gaz rejeté par les transports, qui contribue au réchauffement climatique"}],
     "sources": BO2 + " ; livret « Mission géographique », séance 12 (distances)."},
    {"id": "l13", "salle": 13, "icone": "13", "titre": "Les principaux fleuves et massifs montagneux de France", "duree": "4 min", "niveau": "CM1-CM2",
     "objectifs": ["Situer et nommer les cinq principaux fleuves français", "Situer et nommer les six grands massifs montagneux", "Distinguer un fleuve d'une rivière"],
     "contenu": {"cm1": "<h4>Fleuves et rivières</h4><p>Un <b>fleuve</b> se jette dans la mer ou l'océan ; une <b>rivière</b> se jette dans un autre cours d'eau. "
                        "Cinq grands fleuves : la <b>Seine</b>, la <b>Loire</b>, la <b>Garonne</b>, le <b>Rhône</b> et le <b>Rhin</b>.</p>"
                        "<h4>Six massifs</h4><p>Les <b>Alpes</b>, les <b>Pyrénées</b>, le <b>Massif central</b>, le <b>Jura</b>, les <b>Vosges</b> et la <b>Corse</b>.</p>",
                 "cm2": F.html(F.LECON_FLEUVES)},
     "lexique": [{"mot": "fleuve", "def": "cours d'eau qui se jette dans la mer ou dans l'océan"}, {"mot": "rivière", "def": "cours d'eau qui se jette dans un autre cours d'eau"},
                 {"mot": "massif montagneux", "def": "ensemble de montagnes formant un même relief"}, {"mot": "sommet", "def": "point le plus élevé d'une montagne"}],
     "sources": BO2 + " ; Sandre (Loire : 1 005,93 km) ; Chambre départementale des géomètres-experts de la Haute-Savoie (mont Blanc : 4 807,47 m, septembre 2026) ; livret « Mission géographique », séance 13."},
]

METADATA = {"jeu": "Mission géographique", "auteur": "Escape game · cycle 3 · géographie", "version": 1,
            "differenciation": "Une escale par séance. CM1 : 3 énigmes par escale. CM2 : 4 énigmes par escale (la 4e : « niveaux »: [\"CM2\"]).",
            "sources": BO + " ; livret « Mission géographique » (Année A) ; Insee ; DGCL ; ministère de l'Agriculture (CEP) ; Office de tourisme des Rousses ; PNUD (RDH 2025) ; OIT et UNICEF (2025) ; FAO (SOFI 2025) ; Sandre ; géomètres-experts de la Haute-Savoie (2026)."}


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ecr = lambda n, o: json.dump(o, open(os.path.join(SORTIE, n), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    ecr("enigmes.json", {"metadata": METADATA, "salles": SALLES_E})
    ecr("dialogues.json", {"metadata": {"jeu": METADATA["jeu"]}, "personnages": PERSONNAGES, "intro_accueil": INTRO, "salles": SALLES_D})
    ecr("lecons.json", {"lecons": LECONS})
    n = sum(len(s["enigmes"]) for s in SALLES_E)
    print(f"{len(SALLES_E)} escales, {n} énigmes, {len(LECONS)} leçons → {os.path.relpath(SORTIE, RACINE)}")


if __name__ == "__main__":
    main()
