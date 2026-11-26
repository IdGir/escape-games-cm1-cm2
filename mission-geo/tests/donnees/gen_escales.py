# -*- coding: utf-8 -*-
"""Données de la version immersive de « Mission géographique » (Année A), au format des salles des jeux de la collection.

    python mission-geo/tests/donnees/gen_escales.py [dossier de sortie]
Sortie par défaut : vingt-mille-lieues/outils/immersif/sources/mission-geo/assets/data/ (enigmes.json, dialogues.json, lecons.json),
lue ensuite par migrer-jeu.py. La version classique (mission-geo/js/donnees/*.js) n'est ni lue ni modifiée par le jeu immersif :
ce script en reprend les activités, transformées en énigmes corrigeables (voir mission-geo/REFONTE-IMMERSIVE.md, § 2).
Une escale = une séance (séance N ↔ escale N). Étape P1 : séances 1 à 5 (période 1, « L'organisation du territoire français »).
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

SALLES_E = [
    {"num": 1, "titre": "Le grand départ — Ma commune", "enigmes": E1},
    {"num": 2, "titre": "Direction Dijon ! — Des territoires emboîtés", "enigmes": E2},
    {"num": 3, "titre": "Vivre à Clamecy — L'espace rural", "enigmes": E3},
    {"num": 4, "titre": "Besançon — Travailler en ville", "enigmes": E4},
    {"num": 5, "titre": "Les Rousses — Les loisirs de la montagne", "enigmes": E5},
]

# ============================================================================ DIALOGUES
PERSONNAGES = {
    "atlas": {"nom": "Professeur Atlas", "role": "Géographe et chef de la mission, il dirige le bureau des agents depuis ta commune"},
    "lena": {"nom": "Léna", "role": "Agente de terrain, elle attend les recrues à Dijon"},
    "malik": {"nom": "Malik", "role": "Agent infiltré à Clamecy, spécialiste des chiffres"},
    "zoe": {"nom": "Zoé", "role": "Agente chargée de rencontrer les sources à Besançon"},
    "hugo": {"nom": "Hugo", "role": "Agent et moniteur de ski à la station des Rousses"},
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
]

METADATA = {"jeu": "Mission géographique", "auteur": "Escape game · cycle 3 · géographie", "version": 1,
            "differenciation": "Une escale par séance. CM1 : 3 énigmes par escale. CM2 : 4 énigmes par escale (la 4e : « niveaux »: [\"CM2\"]).",
            "sources": BO + " ; livret « Mission géographique » (Année A) ; Insee ; DGCL ; ministère de l'Agriculture (CEP) ; Office de tourisme des Rousses."}


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
