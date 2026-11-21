# -*- coding: utf-8 -*-
"""Génère seconde-guerre/assets/data/enigmes.json (Radio Londres). Lancer : python gen_enigmes.py <dossier data>
SUJET TRÈS SENSIBLE : aucune énigme notée sur les persécutions (leçon 3 et discussion seulement) ; élèves jamais en position de victime
ni de bourreau ; aucune image de camp ; Vichy et collaboration nuancent la résistance ; chiffres officiels avec source.
Village (Saint-Aubin-en-Morvan), familles et personnages : inventés. Les personnes réelles ne parlent jamais."""
import json, os, sys
from schemas import carte_1940, carte_1944

BO = "Programme d'histoire du cycle 3 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026), Seconde Guerre mondiale (niveau à confirmer, cf. A-VERIFIER.md) ; progression de l'enseignant : thème 6 « La France des guerres mondiales à l'Union européenne », année A, période 5"
CDM = "Ministère des Armées, Chemins de mémoire (Seconde Guerre mondiale, Occupation, Libération)"
USHMM = "USHMM, Encyclopédie multimédia de la Shoah, article « France » ; ministère des Armées, « Hommage national aux Justes » (2026)"
UNIV = "Encyclopædia Universalis, « Service du travail obligatoire (STO) »"
OL = "Ordre de la Libération (biographies du général de Gaulle et de Jean Moulin)"
FR = "Fondation de la Résistance et Musée de la Résistance en ligne"
MC = "Mémorial de Caen (débarquement et Libération)"
MRM = "Musée de la Résistance en Morvan (Saint-Brisson, Nièvre)"
LUMNI = "Lumni et Eduscol, ressources sur la Seconde Guerre mondiale à l'école"


def E(id, titre, type_, consigne, source, correction, indices, cm1=None, cm2=None, commun=None, lecon="", cm2_seul=False):
    e = {"id": id, "titre": titre, "type": type_}
    if cm2_seul:
        e["niveaux"] = ["CM2"]
    e["consigne"] = consigne
    e["source"] = source
    e["correction"] = correction
    e["indices"] = indices
    if cm1 is not None: e["cm1"] = cm1
    if cm2 is not None: e["cm2"] = cm2
    if commun is not None: e["commun"] = commun
    e["lecon"] = lecon
    return e


def tri(cols, cartes):
    return {"colonnes": [{"id": i, "titre": t} for i, t in cols], "cartes": [{"txt": t, "col": c} for t, c in cartes]}


def qcm(qs):
    return {"questions": [{"q": q, "options": o, "bonne": b, "explication": x} for q, o, b, x in qs]}


def vf(affs):
    return {"affirmations": [{"txt": t, "vrai": v, "explication": x} for t, v, x in affs]}


def ordre(items):
    out = []
    for i, t in enumerate(items):
        d = {"txt": t[0] if isinstance(t, tuple) else t, "rang": i + 1}
        if isinstance(t, tuple):
            d["sous"] = t[1]
        out.append(d)
    return {"items": out}


def assoc(paires):
    return {"paires": [{"g": g, "d": d} for g, d in paires]}


def code(champs):
    return {"champs": [{"libelle": l, "valeur": v, "longueur": len(v)} for l, v in champs]}


def intrus(cartes):
    return {"cartes": [{"txt": t, "intrus": i} for t, i in cartes]}


def trous(texte, etiq):
    return {"texte": "<p>" + texte + "</p>", "etiquettes": etiq}


def plan(titre, col, cases, etiq):
    return {"titre": titre, "colonnes": col, "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(cases)], "etiquettes": etiq}


def tableau(titre, entetes, lignes):
    h = "".join(f"<th>{x}</th>" for x in entetes)
    c = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in l) + "</tr>" for l in lignes)
    return f"<div class='doc-titre'><i>{titre}</i></div><table class='tableau-releves'><tr>{h}</tr>{c}</table>"


CATEGORIES = tableau("Les catégories de la carte d'alimentation (barème simplifié de 1942)", ["Lettre", "Qui ?"],
                     [["E", "enfants de moins de 3 ans"], ["J1", "enfants de 3 à 6 ans"], ["J2", "enfants de 6 à 13 ans"],
                      ["J3", "jeunes de 13 à 21 ans"], ["A", "adultes de 21 à 70 ans"], ["V", "personnes de plus de 70 ans"]])
ALPHA = "<div class='doc-titre'><i>L'alphabet de Marc</i></div><p style='font-family:monospace;letter-spacing:.2em'>A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</p>"

S = []
# =================================================================== SALLE 1 — la salle de classe, 1938 (Bastien)
S.append({"num": 1, "titre": "Fréquence n°1, 1938 — La salle de classe : la montée des dictatures", "enigmes": [
    E("1-1", "La frise du tableau noir", "ordre",
      {"cm1": "Monsieur Morel a écrit au tableau les événements qui inquiètent l'Europe, mais ils sont mélangés. Remets-les dans l'ordre, du plus ancien au plus récent.",
       "cm2": "Monsieur Morel a préparé une frise des années 1922-1939, mais les cartes sont tombées. Remets les événements dans l'ordre chronologique."},
      BO + " ; " + CDM + " ; " + LUMNI,
      "D'abord Mussolini prend le pouvoir en Italie (1922), puis la crise commence (1929), puis Hitler devient chef du gouvernement en Allemagne (1933). En CM2 : le krach de la Bourse de New York a lieu en octobre 1929, Hitler devient chancelier le 30 janvier 1933, il annexe l'Autriche en 1938 et l'armée allemande envahit la Pologne le 1er septembre 1939.",
      {"cm1": ["L'Italie est la première touchée.", "La crise commence en 1929.", "Hitler arrive au pouvoir après la crise."],
       "cm2": ["1922 est la date la plus ancienne.", "Hitler devient chancelier en 1933.", "La Pologne est envahie en septembre 1939."]},
      cm1=ordre([("Mussolini prend le pouvoir en Italie", "1922"), ("la grande crise économique commence", "1929"), ("Hitler prend le pouvoir en Allemagne", "1933")]),
      cm2=ordre([("Mussolini prend le pouvoir en Italie", "1922"), ("la Bourse de New York s'effondre", "octobre 1929"),
                 ("Hitler devient chancelier", "30 janvier 1933"), ("Hitler annexe l'Autriche", "1938"), ("l'armée allemande envahit la Pologne", "1er septembre 1939")]),
      lecon="montee"),
    E("1-2", "Les cartes de géographie", "association",
      {"cm1": "Sur la carte de l'Europe accrochée au mur, Monsieur Morel a punaisé le nom de trois dictateurs. Relie chaque chef à son pays.",
       "cm2": "Sur la carte de l'Europe accrochée au mur, Monsieur Morel a punaisé des étiquettes. Relie chaque pays au régime qui le gouverne en 1938."},
      BO + " ; " + CDM + " ; " + LUMNI,
      "Mussolini dirige l'Italie, Hitler l'Allemagne, Staline l'Union soviétique (URSS) : ce sont trois dictatures. En CM2 : l'Italie est fasciste, l'Allemagne est nazie, l'URSS est communiste ; la France et le Royaume-Uni restent des démocraties où l'on vote librement.",
      {"cm1": ["Mussolini est italien.", "Hitler dirige l'Allemagne.", "Staline dirige l'URSS."],
       "cm2": ["Fasciste : le parti de Mussolini.", "Nazi : le parti de Hitler.", "En France, on vote encore librement."]},
      cm1=assoc([("Mussolini", "l'Italie"), ("Hitler", "l'Allemagne"), ("Staline", "l'Union soviétique (URSS)")]),
      cm2=assoc([("l'Italie de Mussolini", "une dictature fasciste"), ("l'Allemagne de Hitler", "une dictature nazie"), ("l'URSS de Staline", "une dictature communiste"),
                 ("la France", "une démocratie : la République"), ("le Royaume-Uni", "une démocratie avec un roi")]),
      lecon="montee"),
    E("1-3", "Dictature ou démocratie ?", "tri",
      {"cm1": "Les élèves de 1938 ont écrit des phrases sur des cartons. Range chaque carton : vivre en démocratie, ou vivre en dictature ?",
       "cm2": "Les élèves de 1938 ont écrit des phrases sur des cartons. Range chaque carton : démocratie, ou dictature totalitaire ?"},
      BO + " ; " + LUMNI,
      "En démocratie, on vote librement, les journaux sont libres et on peut critiquer le gouvernement. Dans une dictature, un seul chef et un seul parti décident ; les opposants sont arrêtés. En CM2 : un régime totalitaire veut tout contrôler, même la vie privée et ce que pensent les enfants, avec la propagande et une police politique.",
      {"cm1": ["En démocratie, on peut choisir.", "Dans une dictature, on ne peut pas critiquer le chef.", "Un seul parti : c'est une dictature."],
       "cm2": ["La propagande sert la dictature.", "Plusieurs partis : démocratie.", "La police politique surveille les opposants."]},
      cm1=tri([("demo", "Démocratie"), ("dicta", "Dictature")],
              [("on vote librement", "demo"), ("les journaux sont libres", "demo"), ("un seul chef décide de tout", "dicta"), ("critiquer le chef est interdit", "dicta")]),
      cm2=tri([("demo", "Démocratie"), ("dicta", "Dictature totalitaire")],
              [("plusieurs partis se présentent aux élections", "demo"), ("les journaux peuvent critiquer le gouvernement", "demo"), ("les citoyens élisent leurs députés", "demo"),
               ("un parti unique", "dicta"), ("la propagande contrôle les journaux et la radio", "dicta"), ("une police politique arrête les opposants", "dicta")]),
      lecon="montee"),
    E("1-4", "Le journal de 1938", "qcm",
      "Monsieur Morel lit à la classe un article sur la crise et sur l'Allemagne. Réponds aux questions.",
      BO + " ; " + CDM + " ; " + LUMNI,
      "La crise commence en octobre 1929 par l'effondrement de la Bourse de New York ; des usines ferment et des millions de personnes perdent leur travail. Hitler, chef du parti nazi, devient chancelier le 30 janvier 1933 ; le nazisme repose sur le racisme et l'antisémitisme, la haine des Juifs. En 1938, Hitler annexe l'Autriche : il veut agrandir l'Allemagne par la force.",
      {"cm2": ["New York, octobre 1929.", "L'antisémitisme est la haine des Juifs.", "L'Autriche est annexée en 1938."]},
      commun=qcm([("Où commence la crise de 1929 ?", ["à Paris", "à New York", "à Berlin", "à Rome"], 1, "La Bourse de New York s'effondre en octobre 1929."),
                  ("Que provoque la crise ?", ["des fêtes", "la fermeture d'usines et le chômage", "la fin des dictatures", "une hausse des salaires"], 1, "Des millions de personnes perdent leur travail."),
                  ("Sur quelle idée repose le nazisme ?", ["l'égalité de tous", "le racisme et l'antisémitisme", "la liberté de la presse", "la paix entre les peuples"], 1, "L'antisémitisme est la haine des Juifs."),
                  ("Que fait Hitler en 1938 ?", ["il quitte le pouvoir", "il annexe l'Autriche", "il signe la paix avec la France", "il organise des élections libres"], 1, "Il veut agrandir l'Allemagne par la force.")]),
      lecon="montee", cm2_seul=True),
]})

# =================================================================== SALLE 2 — la gare, juin 1940 (Paul)
S.append({"num": 2, "titre": "Fréquence n°2, juin 1940 — La gare : la défaite et l'appel", "enigmes": [
    E("2-1", "Les nouvelles du quai", "vraifaux",
      {"cm1": "Sur le quai de la gare, des familles qui fuient parlent toutes en même temps. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Sur le quai de la gare, Paul note ce que disent les familles qui fuient. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + CDM,
      "La guerre commence en septembre 1939 après l'invasion de la Pologne. En mai-juin 1940, l'armée allemande attaque et l'armée française est battue en quelques semaines ; des millions de personnes fuient sur les routes : c'est l'exode. En CM2 : pendant huit mois, il y a eu peu de combats (la « drôle de guerre ») ; l'armée allemande entre dans Paris le 14 juin 1940.",
      {"cm1": ["L'exode, c'est la fuite sur les routes.", "La défaite est très rapide.", "La guerre a commencé en 1939."],
       "cm2": ["« Drôle de guerre » : peu de combats.", "La défaite dure six semaines.", "Paris : 14 juin 1940."]},
      cm1=vf([("Des millions de personnes fuient sur les routes devant l'armée allemande.", True, "C'est l'exode."),
              ("L'armée française est battue en quelques semaines.", True, "En mai et juin 1940."),
              ("La guerre a commencé en 1945.", False, "Elle commence en septembre 1939.")]),
      cm2=vf([("La France et le Royaume-Uni déclarent la guerre à l'Allemagne en septembre 1939.", True, "Après l'invasion de la Pologne."),
              ("Pendant la « drôle de guerre », les combats sont très violents à l'ouest.", False, "Il y a peu de combats pendant huit mois."),
              ("L'armée allemande attaque à l'ouest le 10 mai 1940.", True, "La défaite française suit en six semaines."),
              ("L'armée allemande entre dans Paris le 14 juin 1940.", True, "La capitale est occupée."),
              ("L'exode ne concerne que quelques dizaines de familles.", False, "Des millions de personnes fuient.")]),
      lecon="defaite"),
    E("2-2", "Les deux voix de la radio", "ordre",
      {"cm1": "Dans le bureau du chef de gare, le poste de radio grésille. Paul a noté ce qu'il a entendu en juin 1940, dans le désordre. Remets les événements dans l'ordre.",
       "cm2": "Paul a recopié dans son carnet les nouvelles de juin et juillet 1940, dans le désordre. Remets-les dans l'ordre chronologique."},
      BO + " ; " + CDM + " ; " + OL,
      "Le 17 juin 1940, le maréchal Pétain annonce qu'il faut cesser le combat ; le 18 juin, depuis Londres, le général de Gaulle appelle à continuer ; le 22 juin, l'armistice est signé. En CM2 : l'armée allemande entre dans Paris le 14 juin ; le 10 juillet 1940, les pleins pouvoirs sont donnés à Pétain et la République est remplacée par l'État français de Vichy.",
      {"cm1": ["Pétain parle le premier, le 17 juin.", "De Gaulle répond le lendemain.", "L'armistice est signé après les deux discours."],
       "cm2": ["Paris est occupé avant les discours.", "17, 18, puis 22 juin.", "Vichy arrive en juillet."]},
      cm1=ordre([("Pétain annonce qu'il faut cesser le combat", "17 juin 1940"), ("de Gaulle appelle depuis Londres à continuer le combat", "18 juin 1940"), ("l'armistice est signé", "22 juin 1940")]),
      cm2=ordre([("l'armée allemande entre dans Paris", "14 juin 1940"), ("Pétain annonce à la radio qu'il faut cesser le combat", "17 juin 1940"),
                 ("de Gaulle lance l'appel du 18 Juin", "18 juin 1940"), ("l'armistice est signé à Rethondes", "22 juin 1940"), ("Pétain reçoit les pleins pouvoirs", "10 juillet 1940")]),
      lecon="defaite"),
    E("2-3", "La carte du chef de gare", "plan",
      {"cm1": "Sur le mur de la gare, une carte montre la France coupée en deux par l'armistice. Les étiquettes sont tombées. Place chaque mot sur son repère : clique sur une étiquette, puis sur la case du repère." + carte_1940(3),
       "cm2": "Sur le mur de la gare, une carte montre la France coupée en deux par l'armistice. Place chaque mot sur son repère. Attention : il y a des étiquettes en trop." + carte_1940(5)},
      BO + " ; " + CDM,
      "Le repère 1 est la zone occupée par l'armée allemande (le nord et l'ouest, en gris), le repère 2 la zone non occupée, dite « zone libre » (le sud), le repère 3 la ligne de démarcation qui les sépare. En CM2 : le repère 4 est Paris, occupé ; le repère 5 est Vichy, où s'installe le gouvernement de Pétain, en zone non occupée. Londres et Berlin ne sont pas sur cette carte de France.",
      {"cm1": ["La zone occupée est en gris, au nord.", "La zone non occupée est au sud.", "La ligne en pointillés rouges sépare les deux zones."],
       "cm2": ["Paris est en zone occupée.", "Vichy est une ville du centre, au sud de la ligne.", "Londres est au Royaume-Uni : étiquette en trop."]},
      cm1=plan("La France coupée en deux", 3, ["la zone occupée", "la zone non occupée", "la ligne de démarcation"], ["la zone occupée", "la zone non occupée", "la ligne de démarcation"]),
      cm2=plan("La France coupée en deux", 2, ["la zone occupée", "la zone non occupée", "la ligne de démarcation", "Paris", "Vichy"],
               ["la zone occupée", "la zone non occupée", "la ligne de démarcation", "Paris", "Vichy", "Londres", "Berlin"]),
      lecon="defaite"),
    E("2-4", "Deux chemins en 1940", "trous",
      "Paul compare les deux voix entendues à la radio. Remets les mots à leur place dans son carnet.",
      BO + " ; " + CDM + " ; " + OL,
      "Le maréchal Pétain demande l'armistice ; il installe à Vichy un régime qui supprime la République et choisit la collaboration avec l'Allemagne nazie après l'entrevue de Montoire (octobre 1940). Le général de Gaulle, depuis Londres, refuse la défaite et appelle à la résistance ; il fonde la France libre. Il ne faut pas réduire la France de 1940 à l'un ou l'autre : la plupart des Français essaient d'abord de survivre.",
      {"cm2": ["Pétain est à Vichy.", "De Gaulle parle depuis Londres.", "Montoire : la collaboration."]},
      commun=trous("Le 17 juin, le maréchal [[Pétain]] demande l'arrêt des combats ; il s'installe à [[Vichy]] et, après sa rencontre avec Hitler à Montoire, choisit la [[collaboration]]. "
                   "Le 18 juin, depuis [[Londres]], le général [[de Gaulle]] refuse la défaite : il fonde la France [[libre]].",
                   ["Pétain", "Vichy", "collaboration", "Londres", "de Gaulle", "libre", "Berlin", "victoire"]),
      lecon="defaite", cm2_seul=True),
]})

# =================================================================== SALLE 3 — l'épicerie, 1942-1943 (Madeleine)
S.append({"num": 3, "titre": "Fréquence n°3, hiver 1942 — L'épicerie : la vie sous l'Occupation", "enigmes": [
    E("3-1", "Les cartes d'alimentation", "code",
      {"cm1": "Madeleine, l'épicière, doit noter sur son cahier la catégorie de chaque carte d'alimentation de sa famille. Lis le tableau, puis écris la lettre de chaque personne." + CATEGORIES,
       "cm2": "Madeleine, l'épicière, doit noter sur son cahier la catégorie de chaque carte d'alimentation de sa famille. Lis le tableau, puis écris la lettre de chaque personne." + CATEGORIES},
      BO + " ; " + CDM,
      "Madeleine a 42 ans : catégorie A ; Robert, 19 ans : J3 ; Lucienne, 8 ans : J2. En CM2 : le grand-père Firmin, 74 ans : V ; le petit Jean, 2 ans : E. Chaque catégorie donne droit à des rations différentes : sans ticket, on ne peut pas acheter de pain, de viande ou de sucre. La famille et les âges sont inventés ; les catégories sont simplifiées.",
      {"cm1": ["Cherche l'âge de chaque personne dans le tableau.", "Robert a entre 13 et 21 ans.", "Lucienne a entre 6 et 13 ans."],
       "cm2": ["Plus de 70 ans : une seule lettre.", "Moins de 3 ans : E.", "Vérifie bien les bornes de chaque catégorie."]},
      cm1=code([("Madeleine, 42 ans", "A"), ("Robert, son fils, 19 ans", "J3"), ("Lucienne, sa fille, 8 ans", "J2")]),
      cm2=code([("Madeleine, 42 ans", "A"), ("Robert, son fils, 19 ans", "J3"), ("Lucienne, sa fille, 8 ans", "J2"), ("Firmin, le grand-père, 74 ans", "V"), ("Jean, le petit dernier, 2 ans", "E")]),
      lecon="occupation"),
    E("3-2", "Les étagères vides", "tri",
      {"cm1": "Sur les étagères de l'épicerie, il manque presque tout. Range chaque produit : ce qui est rationné, ou ce qui le remplace.",
       "cm2": "Madeleine range ses étiquettes : les produits rationnés, et les ersatz qui les remplacent. Range chaque étiquette dans la bonne colonne."},
      BO + " ; " + CDM,
      "Le pain, la viande, le sucre, le café, le charbon et les vêtements sont rationnés : on les achète avec des tickets. Pour remplacer ce qui manque, on invente des ersatz : de l'orge grillée à la place du café, des semelles de bois pour les chaussures, des topinambours et des rutabagas à la place des pommes de terre. En CM2 : certains achètent très cher au marché noir.",
      {"cm1": ["Le pain s'achète avec un ticket.", "Une semelle de bois remplace le cuir.", "L'orge grillée remplace le café."],
       "cm2": ["Un ersatz remplace un produit qui manque.", "Le charbon est rationné.", "Le rutabaga remplace la pomme de terre."]},
      cm1=tri([("ration", "Rationné (avec tickets)"), ("ersatz", "Ce qui le remplace")],
              [("le pain", "ration"), ("le sucre", "ration"), ("l'orge grillée à la place du café", "ersatz"), ("des semelles de bois", "ersatz")]),
      cm2=tri([("ration", "Produit rationné"), ("ersatz", "Ersatz (produit de remplacement)")],
              [("le pain", "ration"), ("la viande", "ration"), ("le charbon", "ration"), ("l'orge grillée à la place du café", "ersatz"),
               ("des semelles de bois à la place du cuir", "ersatz"), ("le rutabaga à la place de la pomme de terre", "ersatz")]),
      lecon="occupation"),
    E("3-3", "La lettre de Robert", "vraifaux",
      {"cm1": "Robert, le fils de Madeleine, a reçu une convocation : il doit partir travailler en Allemagne. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Robert, le fils de Madeleine, a reçu une convocation du Service du travail obligatoire. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + UNIV,
      "Le Service du travail obligatoire (STO) est créé par une loi du 16 février 1943 : des jeunes Français doivent partir travailler en Allemagne, dans les usines qui servent la guerre allemande. Beaucoup refusent : ces réfractaires se cachent, et certains rejoignent les maquis. En CM2 : la loi vise d'abord les jeunes nés en 1920, 1921 et 1922.",
      {"cm1": ["STO veut dire Service du travail obligatoire.", "Obligatoire : on n'a pas le choix.", "Certains se cachent."],
       "cm2": ["La loi date de février 1943.", "Les jeunes nés en 1920, 1921 et 1922.", "Un réfractaire refuse de partir."]},
      cm1=vf([("Des jeunes Français doivent partir travailler en Allemagne.", True, "C'est le STO."),
              ("Les jeunes peuvent choisir librement de ne pas partir, sans risque.", False, "Ceux qui refusent doivent se cacher."),
              ("Certains jeunes refusent et se cachent dans les forêts.", True, "Certains rejoignent les maquis.")]),
      cm2=vf([("Le STO est créé par une loi du 16 février 1943.", True, "Sous le régime de Vichy."),
              ("Le STO vise d'abord les jeunes nés en 1920, 1921 et 1922.", True, "Robert est né en 1923 : il est appelé plus tard."),
              ("Les jeunes du STO travaillent dans les champs de leur village.", False, "Ils partent en Allemagne."),
              ("Les réfractaires sont ceux qui refusent de partir.", True, "Ils se cachent."),
              ("Le STO est décidé par la Résistance.", False, "Il est créé par le régime de Vichy, à la demande de l'Allemagne.")]),
      lecon="occupation"),
    E("3-4", "Le lexique de l'Occupation", "association",
      "Lucienne apprend les mots de l'Occupation pour l'école. Relie chaque mot à sa définition.",
      BO + " ; " + CDM + " ; " + UNIV,
      "Le rationnement limite ce que chacun peut acheter ; le marché noir est le commerce caché, très cher ; un ersatz remplace un produit qui manque ; la ligne de démarcation sépare les deux zones ; un réfractaire refuse de partir au STO ; la collaboration, c'est aider l'occupant.",
      {"cm2": ["Noir : caché.", "Réfractaire : qui refuse.", "Collaborer : travailler avec."]},
      commun=assoc([("le rationnement", "chacun n'a droit qu'à une petite quantité"), ("le marché noir", "le commerce caché, à des prix très élevés"),
                    ("un ersatz", "un produit qui en remplace un autre"), ("un réfractaire", "un jeune qui refuse de partir au STO"),
                    ("la collaboration", "aider l'Allemagne nazie qui occupe le pays")]),
      lecon="occupation", cm2_seul=True),
]})

# =================================================================== SALLE 4 — le maquis du Morvan, printemps 1944 (Marc)
S.append({"num": 4, "titre": "Fréquence n°4, printemps 1944 — Le maquis : la Résistance", "enigmes": [
    E("4-1", "Le message chiffré", "code",
      {"cm1": "Marc, l'opérateur radio du maquis, a reçu un mot chiffré : <b>M P O E S F T</b>. Chaque lettre a été remplacée par la <b>lettre suivante</b> de l'alphabet (A devient B, B devient C…). Retrouve le mot en clair." + ALPHA,
       "cm2": "Marc a reçu deux mots chiffrés : <b>O L E H U W H</b> et <b>H V S R L U</b>. Chaque lettre a été remplacée par la lettre située <b>trois places plus loin</b> dans l'alphabet (A devient D, B devient E…). Retrouve les deux mots en clair." + ALPHA},
      BO + " ; " + FR,
      "En CM1, on recule chaque lettre d'une place : M devient L, P devient O… le mot est LONDRES, la ville d'où parle la radio de la France libre. En CM2, on recule de trois places : OLEHUWH donne LIBERTE et HVSRLU donne ESPOIR. Les résistants chiffrent leurs messages pour que l'occupant ne puisse pas les lire ; ce code très simple s'appelle le code de César.",
      {"cm1": ["Pour déchiffrer, recule d'une lettre : M devient L.", "P devient O, O devient N.", "C'est la ville où parle de Gaulle."],
       "cm2": ["Recule de trois lettres : O devient L.", "Le premier mot est une valeur de la République.", "H devient E : le second mot commence par E."]},
      cm1=code([("Le mot en clair", "LONDRES")]),
      cm2=code([("Premier mot", "LIBERTE"), ("Second mot", "ESPOIR")]),
      lecon="resistance"),
    E("4-2", "Le carnet de liaison", "association",
      {"cm1": "Dans la cabane du maquis, Marc explique aux nouveaux venus les mots de la Résistance. Relie chaque mot à sa définition.",
       "cm2": "Dans la cabane du maquis, Marc explique aux nouveaux venus comment la Résistance est organisée. Relie chaque mot à son rôle."},
      BO + " ; " + FR + " ; " + OL + " ; " + MRM,
      "Un maquis est un groupe de résistants cachés dans la forêt ou la montagne ; un journal clandestin est imprimé en cachette ; Radio Londres est la radio de la France libre diffusée par la BBC. En CM2 : un réseau de renseignement observe l'occupant et informe les Alliés ; une agente de liaison transporte les messages ; le Conseil national de la Résistance (CNR), réuni par Jean Moulin le 27 mai 1943, unit les mouvements.",
      {"cm1": ["Le maquis est caché dans la forêt.", "Clandestin : en cachette.", "La radio parle depuis Londres."],
       "cm2": ["Renseigner : donner des informations.", "La liaison relie les groupes.", "Le CNR unit les mouvements."]},
      cm1=assoc([("un maquis", "un groupe de résistants cachés dans la forêt"), ("un journal clandestin", "un journal imprimé en cachette"), ("Radio Londres", "la radio de la France libre, depuis Londres")]),
      cm2=assoc([("un maquis", "un groupe de résistants cachés dans la forêt"), ("un journal clandestin", "un journal imprimé en cachette pour dire la vérité"),
                 ("un réseau de renseignement", "observe l'occupant et informe les Alliés"), ("une agente de liaison", "transporte les messages entre les groupes"),
                 ("le CNR", "unit les mouvements de résistance à partir de mai 1943")]),
      lecon="resistance"),
    E("4-3", "Résister ou collaborer ?", "tri",
      {"cm1": "Marc a écrit sur des fiches ce que font des Français en 1943. Range chaque fiche : est-ce résister, ou collaborer avec l'occupant ?",
       "cm2": "Marc a écrit sur des fiches ce que font des Français en 1943. Range chaque fiche : résistance, ou collaboration avec l'occupant ?"},
      BO + " ; " + FR + " ; " + CDM,
      "Écouter Radio Londres, cacher un réfractaire, imprimer des tracts, transmettre des renseignements aux Alliés : c'est résister. Le gouvernement de Vichy et ceux qui aident l'occupant, par exemple la Milice qui pourchasse les résistants, collaborent. En CM2 : les résistants sont une minorité qui grandit à partir de 1943 ; beaucoup de Français ne sont ni résistants ni collaborateurs : ils essaient de vivre.",
      {"cm1": ["Écouter Londres est interdit : c'est résister.", "Aider l'occupant, c'est collaborer.", "Cacher quelqu'un qui refuse le STO, c'est résister."],
       "cm2": ["La Milice aide l'occupant.", "Un tract dit la vérité.", "Pétain a choisi la collaboration à Montoire."]},
      cm1=tri([("res", "Résister"), ("col", "Collaborer")],
              [("écouter Radio Londres en cachette", "res"), ("cacher un jeune réfractaire", "res"), ("dénoncer un voisin à l'occupant", "col"), ("travailler pour la police allemande", "col")]),
      cm2=tri([("res", "Résistance"), ("col", "Collaboration")],
              [("imprimer des tracts clandestins", "res"), ("transmettre des renseignements aux Alliés", "res"), ("cacher un réfractaire au STO", "res"),
               ("la rencontre de Montoire entre Pétain et Hitler", "col"), ("la Milice qui pourchasse les résistants", "col"), ("dénoncer un voisin à l'occupant", "col")]),
      lecon="resistance"),
    E("4-4", "Les voix de Londres", "qcm",
      "Le soir, Marc colle son oreille au poste. Réponds aux questions sur la Résistance.",
      BO + " ; " + OL + " ; " + FR,
      "Chaque soir, la BBC diffuse « Les Français parlent aux Français » ; en France, l'écouter est interdit. Les messages personnels sont des ordres codés. Envoyé par de Gaulle, Jean Moulin réunit le Conseil national de la Résistance le 27 mai 1943 à Paris ; il est arrêté le 21 juin 1943 près de Lyon et meurt quelques semaines plus tard, sans avoir parlé.",
      {"cm2": ["L'émission a un nom célèbre.", "Les messages personnels cachent des ordres.", "Le CNR : 27 mai 1943."]},
      commun=qcm([("Comment s'appelle l'émission de la BBC en français ?", ["« Ici Paris »", "« Les Français parlent aux Français »", "« Radio Vichy »", "« La voix de Berlin »"], 1, "Elle est diffusée depuis Londres."),
                  ("À quoi servent les « messages personnels » ?", ["à souhaiter les anniversaires", "à donner des ordres codés aux résistants", "à annoncer la météo", "à vendre des produits"], 1, "Des phrases étranges qui cachent des ordres."),
                  ("Qui unifie les mouvements de résistance à la demande de de Gaulle ?", ["Pétain", "Jean Moulin", "Mussolini", "Leclerc"], 1, "Il réunit le CNR."),
                  ("Quand le Conseil national de la Résistance se réunit-il pour la première fois ?", ["le 18 juin 1940", "le 27 mai 1943", "le 6 juin 1944", "le 8 mai 1945"], 1, "À Paris, en cachette.")]),
      lecon="resistance", cm2_seul=True),
]})

# =================================================================== SALLE 5 — la place de la mairie, 8 mai 1945 (Lucie)
S.append({"num": 5, "titre": "Fréquence n°5, 1944-1945 — La place de la mairie : la Libération", "enigmes": [
    E("5-1", "La carte de la Libération", "plan",
      {"cm1": "Lucie a dessiné sur une carte les grandes étapes de la Libération, mais les noms se sont effacés. Place chaque nom sur son repère : clique sur une étiquette, puis sur la case du repère." + carte_1944(3),
       "cm2": "Lucie a dessiné sur une carte les grandes étapes de la Libération. Place chaque nom sur son repère. Attention : il y a des étiquettes en trop." + carte_1944(5)},
      BO + " ; " + MC + " ; " + MRM,
      "Le repère 1 montre les plages de Normandie, où les Alliés débarquent le 6 juin 1944 ; le repère 2 Paris, libéré le 25 août 1944 ; le repère 3 les côtes de Provence, où d'autres troupes débarquent le 15 août 1944. En CM2 : le repère 4 est Dijon, libérée le 11 septembre 1944 ; le repère 5 les forêts du Morvan, où les maquis aident les Alliés. Berlin et Londres ne sont pas sur la carte.",
      {"cm1": ["La Normandie est au nord-ouest, face au Royaume-Uni.", "Paris est au centre-nord.", "La Provence est au sud-est, au bord de la Méditerranée."],
       "cm2": ["Dijon est en Bourgogne, à l'est.", "Le Morvan est une forêt de Bourgogne.", "Deux étiquettes sont des villes étrangères."]},
      cm1=plan("La carte de Lucie", 3, ["les plages de Normandie", "Paris", "les côtes de Provence"], ["les plages de Normandie", "Paris", "les côtes de Provence"]),
      cm2=plan("La carte de Lucie", 2, ["les plages de Normandie", "Paris", "les côtes de Provence", "Dijon", "les forêts du Morvan"],
               ["les plages de Normandie", "Paris", "les côtes de Provence", "Dijon", "les forêts du Morvan", "Berlin", "Londres"]),
      lecon="liberation"),
    E("5-2", "Le calendrier de la mairie", "ordre",
      {"cm1": "Sur le calendrier de la mairie, Lucie a entouré les grandes dates de la Libération, mais les feuilles sont tombées. Remets-les dans l'ordre.",
       "cm2": "Sur le calendrier de la mairie, Lucie a entouré les grandes dates de 1944 et 1945. Remets les événements dans l'ordre chronologique."},
      BO + " ; " + MC + " ; " + CDM,
      "Le débarquement de Normandie a lieu le 6 juin 1944, Paris est libéré le 25 août 1944 et l'Allemagne nazie capitule le 8 mai 1945. En CM2 : le débarquement de Provence a lieu le 15 août 1944, Dijon est libérée le 11 septembre 1944 et les Françaises votent pour la première fois au printemps 1945, quelques jours avant la capitulation.",
      {"cm1": ["Le débarquement est le premier.", "Paris est libéré en été 1944.", "La guerre finit en Europe en 1945."],
       "cm2": ["Juin, puis août 1944.", "La Provence avant Paris, de dix jours.", "Le premier vote des femmes précède de peu le 8 mai."]},
      cm1=ordre([("le débarquement de Normandie", "6 juin 1944"), ("la libération de Paris", "25 août 1944"), ("l'Allemagne nazie capitule", "8 mai 1945")]),
      cm2=ordre([("le débarquement de Normandie", "6 juin 1944"), ("le débarquement de Provence", "15 août 1944"), ("la libération de Paris", "25 août 1944"),
                 ("la libération de Dijon", "11 septembre 1944"), ("les Françaises votent pour la première fois", "avril 1945"), ("l'Allemagne nazie capitule", "8 mai 1945")]),
      lecon="liberation"),
    E("5-3", "Les drapeaux de la fête", "intrus",
      {"cm1": "Pour la fête de la victoire, Lucie accroche les drapeaux des Alliés. Un drapeau ne devrait pas être là : trouve l'intrus.",
       "cm2": "Pour la fête de la victoire, Lucie prépare une banderole avec les Alliés qui ont vaincu l'Allemagne nazie. Une carte ne va pas : trouve l'intruse."},
      BO + " ; " + MC + " ; " + CDM,
      "Les Alliés sont notamment le Royaume-Uni, l'Union soviétique, les États-Unis (entrés en guerre en décembre 1941) et la France libre. L'Italie de Mussolini, alliée de Hitler, faisait partie du camp vaincu. En CM2 : le Japon aussi combattait aux côtés de l'Allemagne ; il capitule le 2 septembre 1945.",
      {"cm1": ["Les Alliés combattent l'Allemagne nazie.", "Mussolini était l'allié de Hitler.", "Cherche le pays de Mussolini."],
       "cm2": ["Les États-Unis entrent en guerre en 1941.", "Le Japon combat avec l'Allemagne.", "Un seul camp a gagné."]},
      cm1=intrus([("le Royaume-Uni", False), ("les États-Unis", False), ("l'Union soviétique", False), ("l'Italie de Mussolini", True)]),
      cm2=intrus([("le Royaume-Uni", False), ("les États-Unis", False), ("l'Union soviétique", False), ("la France libre", False), ("le Japon", True)]),
      lecon="liberation"),
    E("5-4", "La fréquence du poste", "code",
      "Le vieux poste de radio de la cave ne s'allume qu'avec une fréquence secrète : la date de la victoire en Europe. Lucie a écrit : « Le jour où l'Allemagne nazie a capitulé, onze mois après le débarquement de Normandie. » Trouve le jour, le mois (en chiffres) et l'année.",
      BO + " ; " + CDM + " ; " + MC,
      "L'Allemagne nazie capitule le 8 mai 1945 : le jour est 8, le mois est 5 (mai est le cinquième mois), l'année est 1945. Le débarquement de Normandie a eu lieu le 6 juin 1944, onze mois plus tôt. Le 8 mai est aujourd'hui un jour férié de commémoration.",
      {"cm2": ["Le débarquement : juin 1944.", "Onze mois après juin 1944 : mai 1945.", "Mai est le cinquième mois."]},
      commun=code([("Jour", "8"), ("Mois", "5"), ("Année", "1945")]),
      lecon="liberation", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "Radio Londres", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données. Repères en CM1, dates exactes et chiffres officiels en CM2.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": " ; ".join([BO, CDM, USHMM, UNIV, OL, FR, MC, MRM, LUMNI]) + ". Détail : README.md, section Sources.",
            "vigilance": "SUJET TRÈS SENSIBLE : aucune énigme notée sur les persécutions (leçon 3 et discussion seulement) ; élèves jamais en position de victime ni de bourreau ; aucune image de camp ni symbole nazi ; vocabulaire exact (Shoah, génocide des Juifs) ; Vichy et la collaboration sont présentés à côté de la Résistance ; village, familles et personnages inventés ; les personnes réelles ne parlent jamais.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e2-1\",\"legende\":\"…\",\"source\":\"…\"}. Les cartes et la frise sont dessinées en SVG par script : ne jamais les remplacer par des images générées par IA. Documents d'époque réels : seulement des archives libres (Wikimedia Commons, Gallica), jamais d'image de camp."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
