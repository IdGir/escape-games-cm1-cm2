# -*- coding: utf-8 -*-
"""Génère mouvement/assets/data/enigmes.json (Le Grand Prix de l'observatoire). Lancer : python gen_enigmes.py <dossier data>"""
import json, os, re, sys
from schemas import ruban, rubans_report, circuit, systeme_solaire

BO = "Programme de sciences et technologie, cycle 3 (arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026)"
MAP = "La main à la pâte, ressources « Mouvement » (cycle 3)"
EDU = "Eduscol, ressources d'accompagnement « Matière, mouvement, énergie, information » (cycle 3)"
INV = "données inventées pour le jeu"


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
    return {"items": [{"txt": t, "rang": i + 1} for i, t in enumerate(items)]}


def assoc(paires):
    return {"paires": [{"g": g, "d": d} for g, d in paires]}


def code(champs):
    return {"champs": [{"libelle": l, "valeur": v, "longueur": len(v)} for l, v in champs]}


def intrus(cartes):
    return {"cartes": [{"txt": t, "intrus": i} for t, i in cartes]}


def marque(t):
    return re.sub(r"\[([A-Za-z])\]", lambda m: f"<b data-l='{m.group(1).upper()}'>{m.group(1)}</b>", t)


def tableau(titre, entetes, lignes):
    h = "".join(f"<th>{x}</th>" for x in entetes)
    c = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in l) + "</tr>" for l in lignes)
    return f"<p><i>{titre}</i></p><table class='tab-releves'><tr>{h}</tr>{c}</table>"


S = []
# =================================================================== SALLE 1 — la ligne de départ (Margaux)
S.append({"num": 1, "titre": "La ligne de départ — Mesurer une distance", "enigmes": [
    E("1-1", "Le bon instrument", "tri",
      {"cm1": "Margaux, la commissaire de course, doit tout remesurer avant midi. Range chaque longueur à mesurer sous l'instrument le plus adapté. Clique sur une carte, puis sur une colonne.",
       "cm2": "Margaux prépare le matériel de mesure. Range chaque longueur à mesurer sous l'instrument le plus adapté : on choisit l'instrument selon la longueur à mesurer."},
      BO + " (« mesurer une distance lors du déplacement d'un objet ») ; " + MAP,
      "Pour une petite longueur, comme un crayon ou une feuille, la règle graduée suffit. Pour quelques mètres, comme une caisse à savon ou une porte, on prend un mètre ruban. Pour plusieurs dizaines de mètres, comme une piste ou l'écart entre deux plots, on déroule un décamètre. Pour une très longue distance, comme une route ou un tour de piste, on pousse une roue de mesure qui compte les mètres.",
      {"cm1": ["Une règle d'écolier mesure 20 ou 30 cm.", "Un mètre ruban se déroule sur quelques mètres.", "Le décamètre est un long ruban d'au moins 10 m."],
       "cm2": ["Compare la longueur à mesurer avec la longueur de chaque instrument.", "La roue de mesure compte les mètres en roulant : elle sert pour les très longues distances.", "Le décamètre sert pour quelques dizaines de mètres."]},
      cm1=tri([("regle", "Règle graduée"), ("metre", "Mètre ruban"), ("deca", "Décamètre")],
              [("la longueur d'un crayon", "regle"), ("la largeur d'une feuille", "regle"), ("la longueur d'une caisse à savon", "metre"),
               ("la hauteur de la porte du garage", "metre"), ("la longueur de la piste (50 m)", "deca"), ("l'écart entre deux plots (15 m)", "deca")]),
      cm2=tri([("regle", "Règle graduée"), ("metre", "Mètre ruban"), ("deca", "Décamètre"), ("roue", "Roue de mesure")],
              [("la longueur d'une gomme", "regle"), ("la largeur du volant d'une caisse à savon", "regle"), ("la longueur d'un vélo", "metre"),
               ("la hauteur d'un panneau", "metre"), ("la longueur de la ligne droite (30 m)", "deca"), ("l'écart entre deux plots (15 m)", "deca"),
               ("la route d'accès à l'observatoire (2 km)", "roue"), ("un tour complet du circuit (400 m)", "roue")]),
      lecon="distance"),
    E("1-2", "Départ et arrivée", "qcm",
      {"cm1": "Margaux interroge ses commissaires débutants avant la course. Réponds à chaque question.",
       "cm2": "Margaux vérifie que ses commissaires savent mesurer et convertir. Réponds à chaque question."},
      BO + " ; " + EDU,
      "La distance parcourue se mesure entre la ligne de départ et la ligne d'arrivée. On l'écrit toujours avec son unité : le mètre (m) pour une piste, le kilomètre (km) pour une route, le centimètre (cm) pour un petit objet. Un mètre vaut 100 centimètres et un kilomètre vaut 1 000 mètres.",
      {"cm1": ["La distance parcourue va d'un point à un autre point.", "Le kilogramme mesure une masse, la seconde une durée.", "Sur la règle, il y a 100 petits centimètres dans un mètre."],
       "cm2": ["1 km = 1 000 m.", "Convertis toutes les longueurs dans la même unité avant de comparer.", "Un nombre sans unité ne dit pas de quelle longueur on parle."]},
      cm1=qcm([("Pour connaître la distance parcourue par une caisse à savon, on mesure entre...",
                ["la ligne de départ et le public", "la ligne de départ et la ligne d'arrivée", "le pilote et le chronomètre"], 1, "La distance parcourue va du point de départ au point d'arrivée."),
               ("Quelle unité choisir pour la longueur de la piste ?", ["le mètre (m)", "le kilogramme (kg)", "la seconde (s)"], 0, "Une longueur s'exprime en mètres, centimètres ou kilomètres."),
               ("Un mètre, c'est...", ["10 centimètres", "1 000 centimètres", "100 centimètres"], 2, "1 m = 100 cm.")]),
      cm2=qcm([("La route de l'observatoire mesure 2 km. Cela fait...", ["200 m", "2 000 m", "20 000 m"], 1, "1 km = 1 000 m, donc 2 km = 2 000 m."),
               ("La piste mesure 1 250 m. Cela fait...", ["1 km et 250 m", "12 km et 50 m", "125 km"], 0, "1 250 m = 1 000 m + 250 m."),
               ("Quelle distance est la plus longue ?", ["950 m", "1 010 m", "1 km et 20 m"], 2, "1 km et 20 m = 1 020 m."),
               ("Un commissaire note « la piste fait 50 ». Pourquoi est-ce insuffisant ?", ["Parce que 50 est trop petit", "Parce qu'il faut l'écrire en lettres",
                "Parce qu'on ne sait pas si ce sont des mètres ou des kilomètres"], 2, "Une mesure s'écrit toujours avec son unité.")]),
      lecon="distance"),
    E("1-3", "Le décamètre de Margaux", "code",
      {"cm1": "Margaux a déroulé son décamètre le long de la piste des petites voitures. Lis la graduation de la ligne de départ et celle de la ligne d'arrivée, puis calcule la distance parcourue." + ruban(3, 18),
       "cm2": "La ligne droite est plus longue que le décamètre (10 m). Margaux le déroule plusieurs fois bout à bout, puis il reste 6 m jusqu'à l'arrivée. Calcule la longueur de la ligne droite, en mètres puis en centimètres." + rubans_report(4, 6)},
      BO + " (CM2 : « effectuer des conversions d'unités de distance ») ; " + MAP + " ; mesures " + INV,
      "Sur le ruban, la ligne de départ est à 3 m et la ligne d'arrivée à 18 m : la petite voiture a parcouru 18 − 3 = 15 m. Pour la ligne droite, quatre reports de 10 m font 40 m, plus les 6 m restants : 46 m, soit 4 600 cm, car 1 m = 100 cm.",
      {"cm1": ["Le drapeau vert montre le départ, le damier l'arrivée.", "Le départ n'est pas au zéro du ruban.", "Fais une soustraction : arrivée moins départ."],
       "cm2": ["Compte les reports entiers de 10 m.", "Ajoute les mètres qui restent après le dernier report.", "Pour passer des mètres aux centimètres, multiplie par 100."]},
      cm1=code([("Graduation du départ (en m)", "3"), ("Graduation de l'arrivée (en m)", "18"), ("Distance parcourue (en m)", "15")]),
      cm2=code([("Longueur de la ligne droite (en m)", "46"), ("La même longueur (en cm)", "4600")]),
      lecon="distance"),
    E("1-4", "Les conversions du carnet", "association",
      "Le vent a mélangé les fiches du carnet de Margaux. Relie chaque longueur à la longueur égale.",
      BO + " (CM2 : « effectuer des conversions d'unités de distance »)",
      "Dans le carnet, 1 kilomètre égale 1 000 mètres, 1 mètre égale 100 centimètres, 1 centimètre égale 10 millimètres et 1 décamètre égale 10 mètres. Enfin, 3 km et 500 m font 3 000 m + 500 m, c'est-à-dire 3 500 m.",
      {"cm2": ["Le préfixe « kilo » veut dire mille.", "Le préfixe « déca » veut dire dix.", "3 km et 500 m : convertis d'abord les kilomètres en mètres."]},
      commun=assoc([("1 km", "1 000 m"), ("1 m", "100 cm"), ("1 cm", "10 mm"), ("1 dam", "10 m"), ("3 km et 500 m", "3 500 m")]),
      lecon="distance", cm2_seul=True),
]})

# =================================================================== SALLE 2 — le stand des chronométreurs (Yanis)
S.append({"num": 2, "titre": "Le stand des chronométreurs — Mesurer une durée", "enigmes": [
    E("2-1", "Chronométrer une descente", "ordre",
      {"cm1": "Yanis, le pilote de la caisse à savon, explique comment on chronomètre sa descente. Remets les étapes dans l'ordre.",
       "cm2": "Yanis rédige le protocole de chronométrage du Grand Prix. Remets les étapes dans l'ordre."},
      BO + " (« l'élève utilise un chronomètre ou tout autre instrument de mesure adapté pour déterminer la durée du déplacement ») ; " + MAP,
      "On remet d'abord le chronomètre à zéro. On le déclenche au signal du départ et on l'arrête quand la caisse franchit la ligne d'arrivée. On lit ensuite la durée affichée et on la note avec son unité. Refaire la mesure permet de vérifier qu'on ne s'est pas trompé.",
      {"cm1": ["Avant tout, l'écran du chronomètre doit afficher zéro.", "On déclenche au départ, on arrête à l'arrivée.", "On note la durée à la fin."],
       "cm2": ["On commence par fixer où la course commence et où elle finit.", "Le chronomètre est déclenché au moment exact du départ.", "Une deuxième mesure permet de vérifier la première."]},
      cm1=ordre(["Remettre le chronomètre à zéro.", "Déclencher le chronomètre au signal du départ.",
                 "Arrêter le chronomètre quand la caisse franchit la ligne d'arrivée.", "Lire la durée affichée et la noter avec son unité."]),
      cm2=ordre(["Repérer la ligne de départ et la ligne d'arrivée.", "Remettre le chronomètre à zéro.", "Déclencher le chronomètre au moment exact du départ.",
                 "L'arrêter quand l'avant de la caisse franchit la ligne d'arrivée.", "Lire la durée affichée et la noter avec son unité.",
                 "Recommencer la mesure sur une autre descente pour vérifier."]),
      lecon="duree"),
    E("2-2", "Instant ou durée ?", "vraifaux",
      {"cm1": "Yanis a noté des phrases sur le tableau du stand. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Yanis a noté des phrases sur le tableau du stand. Pour chaque phrase, choisis vrai ou faux. Attention aux unités."},
      BO + " (« mesurer une durée, comme intervalle entre deux instants ») ; " + EDU,
      "Un instant est un moment précis, comme 10 h 15. Une durée est le temps écoulé entre deux instants : pour la connaître, il faut l'instant du départ et l'instant de l'arrivée. Le chronomètre et le sablier mesurent des durées, l'horloge donne l'instant. Une minute vaut 60 secondes et une heure vaut 60 minutes.",
      {"cm1": ["Un instant répond à la question « à quelle heure ? ».", "Une durée répond à la question « combien de temps ? ».", "Avec seulement l'heure d'arrivée, on ne sait pas quand la course a commencé."],
       "cm2": ["Une minute, ce n'est pas cent secondes.", "Sur un chronomètre, 01:30 se lit une minute et trente secondes.", "Un sablier ne donne pas l'heure."]},
      cm1=vf([("« La course commence à 10 h » : cette phrase donne un instant.", True, "10 h est un moment précis : c'est un instant."),
              ("Une durée, c'est le temps qui passe entre deux instants.", True, "Par exemple entre le départ et l'arrivée."),
              ("Un sablier sert à mesurer une durée.", True, "Il mesure toujours la même durée."),
              ("Pour connaître la durée d'une course, il suffit de connaître l'heure d'arrivée.", False, "Il faut aussi l'heure de départ.")]),
      cm2=vf([("Une minute vaut 100 secondes.", False, "Une minute vaut 60 secondes."),
              ("Une heure vaut 60 minutes.", True, "1 h = 60 min."),
              ("Un chronomètre affiche 01:30 : la durée est d'une minute et trente secondes.", True, "Soit 90 secondes."),
              ("Un sablier indique l'heure qu'il est.", False, "Il mesure une durée, pas un instant."),
              ("Pour calculer une durée, on a besoin de deux instants.", True, "L'instant du départ et celui de l'arrivée.")]),
      lecon="duree"),
    E("2-3", "Le registre des départs", "code",
      {"cm1": tableau("Registre des départs (horaires inventés pour le jeu)", ["Pilote", "Départ", "Arrivée"],
                      [["Yanis", "10 h 15 min", "10 h 40 min"], ["Salomé", "10 h 50 min", "11 h 05 min"]])
       + "<p>Calcule la durée de chaque essai, en minutes.</p>",
       "cm2": tableau("Registre des essais (durées inventées pour le jeu)", ["Essai", "Mesure"],
                      [["Descente de Yanis", "2 min 30 s"], ["Séance d'essais du matin", "1 h 15 min"], ["Tour de Salomé", "de 9 h 50 min à 10 h 25 min"]])
       + "<p>Convertis ou calcule chaque durée dans l'unité demandée.</p>"},
      BO + " (CM2 : « effectuer des conversions d'unités de […] temps ») ; horaires " + INV,
      "L'essai de Yanis va de 10 h 15 à 10 h 40 : 25 minutes. Celui de Salomé va de 10 h 50 à 11 h 05 : 10 minutes pour arriver à 11 h, puis 5 minutes, soit 15 minutes. En CM2, 2 min 30 s = 120 s + 30 s = 150 s ; 1 h 15 min = 60 min + 15 min = 75 min ; de 9 h 50 à 10 h 25, il y a 10 min puis 25 min, soit 35 min.",
      {"cm1": ["Compte les minutes de 15 jusqu'à 40.", "Pour Salomé, passe par 11 h.", "De 10 h 50 à 11 h, il y a 10 minutes."],
       "cm2": ["1 min = 60 s.", "1 h = 60 min.", "Pour le tour de Salomé, passe par 10 h."]},
      cm1=code([("Durée de l'essai de Yanis (en min)", "25"), ("Durée de l'essai de Salomé (en min)", "15")]),
      cm2=code([("Descente de Yanis (en s)", "150"), ("Séance d'essais (en min)", "75"), ("Tour de Salomé (en min)", "35")]),
      lecon="duree"),
    E("2-4", "Les étiquettes du stand", "tri",
      "Les étiquettes du tableau d'affichage sont tombées. Range chaque étiquette : est-ce un instant ou une durée ?",
      BO + " (« la durée […] comme intervalle entre deux instants »)",
      "Les heures lues sur l'horloge, comme 10 h 15 ou midi, sont des instants. Le temps écoulé pendant une course, mesuré au chronomètre ou au sablier, comme 25 minutes ou 2 min 30 s, est une durée.",
      {"cm2": ["Un instant se lit sur une horloge.", "Une durée se mesure avec un chronomètre ou un sablier.", "« Midi, heure limite » : est-ce un moment ou un temps écoulé ?"]},
      commun=tri([("instant", "Un instant"), ("duree", "Une durée")],
                 [("10 h 15 min, heure du départ", "instant"), ("midi, heure limite des résultats", "instant"), ("11 h 05 min, arrivée de Salomé", "instant"),
                  ("25 minutes de course", "duree"), ("le sablier de 3 minutes", "duree"), ("2 min 30 s au chronomètre", "duree")]),
      lecon="duree", cm2_seul=True),
]})

# =================================================================== SALLE 3 — le tableau des temps (Salomé)
T100 = tableau("Tableau des temps : course de 100 m (durées inventées pour le jeu)", ["Concurrent", "Durée pour 100 m"],
               [["Salomé à vélo", "20 s"], ["Yanis en caisse à savon", "25 s"], ["Mila à pied", "70 s"]])
T10 = tableau("Tableau des distances : chacun roule pendant 10 s (distances inventées pour le jeu)", ["Concurrent", "Distance en 10 s"],
              [["Salomé à vélo", "50 m"], ["Yanis en caisse à savon", "40 m"], ["Léo à trottinette", "30 m"], ["Mila à pied", "15 m"]])
S.append({"num": 3, "titre": "Le tableau des temps — Comparer des déplacements", "enigmes": [
    E("3-1", "Qui est le plus rapide ?", "qcm",
      {"cm1": "Salomé, la cycliste, lit le tableau des temps de la course de 100 m." + T100 + "<p>Réponds à chaque question.</p>",
       "cm2": "Salomé compare les concurrents d'une autre manière : chacun roule pendant 10 secondes." + T10 + "<p>Réponds à chaque question.</p>"},
      BO + " (sixième : « constater que pendant une même durée, un objet peut parcourir des distances différentes ») ; " + MAP + " ; " + INV,
      "Sur une même distance de 100 m, Salomé met 20 s : c'est la durée la plus courte, elle est la plus rapide ; Mila, avec 70 s, est la plus lente. Quand tous roulent pendant la même durée de 10 s, le plus rapide est celui qui va le plus loin : Salomé, avec 50 m. Pour comparer, on garde toujours une grandeur identique : la distance ou la durée.",
      {"cm1": ["Tout le monde a parcouru la même distance : 100 m.", "Le plus rapide met le moins de temps.", "Le plus lent met le plus de temps."],
       "cm2": ["Cette fois, tout le monde roule pendant la même durée.", "Le plus rapide va le plus loin.", "Pour comparer, une des deux grandeurs doit être la même pour tous."]},
      cm1=qcm([("Qui est le plus rapide sur 100 m ?", ["Yanis", "Salomé", "Mila"], 1, "Salomé met la durée la plus courte : 20 s."),
               ("Qui est le plus lent ?", ["Mila", "Yanis", "Salomé"], 0, "Mila met 70 s, la durée la plus longue."),
               ("Pour comparer ces trois concurrents, ils ont tous parcouru...", ["la même durée", "des distances différentes", "la même distance"], 2, "La même distance : 100 m.")]),
      cm2=qcm([("Pendant 10 s, qui parcourt la plus grande distance ?", ["Yanis", "Salomé", "Léo"], 1, "Salomé parcourt 50 m."),
               ("Qui est le moins rapide ?", ["Léo", "Yanis", "Mila"], 2, "Mila ne parcourt que 15 m en 10 s."),
               ("Pendant une même durée, le plus rapide est celui qui...", ["va le plus loin", "met le plus de temps", "part le premier"], 0, "Même durée : plus grande distance, plus rapide."),
               ("Yanis parcourt 40 m en 10 s et Léo 30 m en 10 s. Que peut-on dire ?", ["Léo est plus rapide", "Ils vont aussi vite", "Yanis est plus rapide"], 2, "En une même durée, Yanis va plus loin.")]),
      lecon="comparer"),
    E("3-2", "Le classement de la descente", "ordre",
      {"cm1": "Voici les durées de cinq concurrents sur la même descente de 200 m (durées inventées pour le jeu). Range-les du plus rapide au plus lent.",
       "cm2": "Voici les durées de cinq concurrents sur la même descente de 200 m (durées inventées pour le jeu), notées dans des unités différentes. Range-les du plus rapide au plus lent."},
      BO + " (sixième : « constater qu'un objet peut parcourir une même distance pendant des durées différentes ») ; " + INV,
      "Sur la même descente de 200 m, le classement suit les durées, de la plus courte à la plus longue : Salomé (40 s), Yanis (55 s), le petit train (70 s), Léo (90 s), puis Mila (150 s). En CM2, il faut d'abord convertir : 1 min 05 s = 65 s, 1 min 20 s = 80 s, 2 min 30 s = 150 s.",
      {"cm1": ["Tous ont parcouru la même distance.", "Le plus rapide a la durée la plus petite.", "Commence par la plus petite durée."],
       "cm2": ["Convertis toutes les durées en secondes.", "1 min = 60 s : 1 min 05 s = 65 s.", "Du plus rapide au plus lent : de la plus petite durée à la plus grande."]},
      cm1=ordre(["Salomé à vélo : 40 s", "Yanis en caisse à savon : 55 s", "Le petit train : 70 s", "Léo à trottinette : 90 s", "Mila à pied : 150 s"]),
      cm2=ordre(["Salomé à vélo : 38 s", "Yanis en caisse à savon : 52 s", "Le petit train : 1 min 05 s", "Léo à trottinette : 1 min 20 s", "Mila à pied : 2 min 30 s"]),
      lecon="comparer"),
    E("3-3", "La règle de Salomé", "trous",
      {"cm1": "Salomé écrit sa règle pour comparer les concurrents. Complète son texte avec les bonnes étiquettes. Attention : il y a des étiquettes en trop.",
       "cm2": "Salomé écrit sa règle pour comparer les concurrents. Complète son texte avec les bonnes étiquettes. Attention : il y a des étiquettes en trop."},
      MAP + " ; " + EDU,
      "Pour comparer deux déplacements, on garde une grandeur identique. Sur une même distance, le plus rapide met la durée la plus courte. Pendant une même durée, le plus rapide parcourt la plus grande distance. On peut exprimer la vitesse en kilomètres par heure (km/h).",
      {"cm1": ["Il y a deux façons de comparer : même distance ou même durée.", "Le plus rapide met le moins de temps.", "Le plus rapide va le plus loin."],
       "cm2": ["On ne peut comparer que si une grandeur reste la même pour tous.", "km/h se lit « kilomètres par heure ».", "Les étiquettes en trop parlent de masse ou de grandeurs qui ne mesurent pas un déplacement."]},
      cm1={"texte": "<p>Sur une même [[distance]], le plus rapide met la durée la plus [[courte]]. Pendant une même [[durée]], le plus rapide va le plus [[loin]].</p>",
           "etiquettes": ["distance", "courte", "durée", "loin", "longue", "près"]},
      cm2={"texte": "<p>Pour comparer deux déplacements, on garde une grandeur [[identique]]. Sur une même [[distance]], le plus rapide met la durée la plus [[courte]]. Pendant une même [[durée]], le plus rapide parcourt la plus grande distance. On peut exprimer la vitesse en [[kilomètres]] par heure.</p>",
           "etiquettes": ["identique", "distance", "courte", "durée", "kilomètres", "kilogrammes", "longue", "différente"]},
      lecon="comparer"),
    E("3-4", "Le panneau des records", "association",
      "Sur le panneau du Grand Prix, Salomé affiche des vitesses de la vie réelle, en ordres de grandeur. Relie chaque animal ou véhicule à sa vitesse.",
      "Vikidia, « Vitesse des animaux » (escargot, guépard) et « TGV » (vitesse commerciale de 320 km/h) ; Fédération française de randonnée, « À quelle vitesse marche un piéton en ville ? » (4 km/h utilisés par les aménageurs) ; Club des villes et territoires cyclables, « Comment ça roule ? » (vitesse moyenne des cyclistes : 15 km/h)",
      "Ce sont des ordres de grandeur. L'escargot avance à moins d'un kilomètre par heure. Un piéton marche à environ 4 km/h et un cycliste en ville roule en moyenne à 15 km/h. Le guépard peut dépasser 100 km/h, mais seulement pendant quelques centaines de mètres. Le TGV roule jusqu'à 320 km/h.",
      {"cm2": ["Range d'abord les cinq du plus lent au plus rapide.", "Un piéton va moins vite qu'un cycliste.", "Le plus rapide de tous est un train."]},
      commun=assoc([("un escargot", "moins de 1 km/h"), ("un piéton", "environ 4 km/h"), ("un cycliste en ville", "environ 15 km/h"),
                    ("un guépard lancé", "plus de 100 km/h"), ("un TGV", "jusqu'à 320 km/h")]),
      lecon="comparer", cm2_seul=True),
]})

# =================================================================== SALLE 4 — la coupole de l'observatoire (Léonie)
S.append({"num": 4, "titre": "La coupole de l'observatoire — Trajectoires", "enigmes": [
    E("4-1", "Droite ou cercle ?", "tri",
      {"cm1": "Depuis la coupole, Léonie, l'astronome, observe le parc. Pour une personne immobile au sol, chaque objet se déplace-t-il en ligne droite ou en cercle ? Range chaque carte.",
       "cm2": "Depuis la coupole, Léonie observe le parc. Pour une personne immobile au sol, range chaque mouvement selon sa trajectoire : rectiligne, circulaire ou curviligne."},
      BO + " (CM2 : « observer et identifier le mouvement rectiligne ou circulaire d'un objet, en fonction de l'observateur ») ; " + EDU,
      "Pour une personne immobile au sol, la bille qui tombe, l'ascenseur et la caisse à savon dans la descente droite vont en ligne droite : leur mouvement est rectiligne. La nacelle de la grande roue, le cheval de bois du manège et le bout de l'aiguille de l'horloge tournent en rond : leur mouvement est circulaire. Le ballon lancé vers le panier et la caisse à savon dans le virage en S suivent une ligne courbe qui n'est pas un cercle : leur mouvement est curviligne.",
      {"cm1": ["Imagine le chemin que dessine l'objet.", "Ce qui tourne autour d'un centre dessine un cercle.", "Une bille lâchée tombe tout droit vers le sol."],
       "cm2": ["Rectiligne : une droite ; circulaire : un cercle.", "Curviligne : une courbe qui n'est pas un cercle.", "Un ballon lancé monte puis redescend en dessinant une courbe."]},
      cm1=tri([("droite", "En ligne droite"), ("cercle", "En cercle")],
              [("une bille lâchée qui tombe", "droite"), ("la caisse à savon dans la descente droite", "droite"), ("l'ascenseur de l'observatoire", "droite"),
               ("la nacelle de la grande roue", "cercle"), ("un cheval de bois du manège", "cercle"), ("le bout de l'aiguille de l'horloge", "cercle")]),
      cm2=tri([("rect", "Rectiligne"), ("circ", "Circulaire"), ("curv", "Curviligne")],
              [("une bille lâchée qui tombe", "rect"), ("l'ascenseur de l'observatoire", "rect"), ("la nacelle de la grande roue", "circ"),
               ("le bout de l'aiguille de l'horloge", "circ"), ("un cheval de bois du manège", "circ"), ("un ballon lancé vers le panier", "curv"),
               ("la caisse à savon dans le virage en S", "curv")]),
      lecon="trajectoires"),
    E("4-2", "Le plan de la coupole", "plan",
      {"cm1": "Léonie a dessiné le circuit vu du haut de la coupole. Place chaque étiquette sur le bon repère. Clique sur une étiquette, puis sur la case du repère." + circuit(),
       "cm2": "Sur le grand écran de la coupole, Léonie montre le Soleil et les trois premières planètes. Place chaque étiquette sur le bon repère. Attention : il y a des étiquettes en trop." + systeme_solaire()},
      BO + " (CM2 : « décrire le mouvement de la Terre par rapport au Soleil et la situer dans le système solaire ») ; Vikidia, « Terre » (troisième planète du système solaire, tour du Soleil en environ 365 jours)",
      "Sur le circuit, le repère 1 marque la ligne droite (trajectoire rectiligne), le repère 2 le virage (trajectoire courbe) et le repère 3 le manège (trajectoire circulaire). Sur l'écran, le repère 1 est le Soleil, au centre. Le repère 2 est Mercure, la planète la plus proche du Soleil. Le repère 3 est la Terre, troisième planète à partir du Soleil. Le repère 4 montre la trajectoire de la Terre : presque un cercle, parcouru en environ un an.",
      {"cm1": ["Le repère 1 est sur la portion toute droite.", "Le repère 2 est dans le virage.", "Le cheval de bois du manège tourne en rond."],
       "cm2": ["Le Soleil est au centre.", "Compte les planètes à partir du Soleil : Mercure, Vénus, puis la Terre.", "Le repère 4 est posé sur une ligne, pas sur une planète."]},
      cm1={"titre": "Le circuit vu du haut de l'observatoire", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "ligne droite"}, {"libelle": "Repère 2", "reponse": "virage"}, {"libelle": "Repère 3", "reponse": "cercle du manège"}],
           "etiquettes": ["ligne droite", "virage", "cercle du manège"]},
      cm2={"titre": "Le Soleil et les trois premières planètes", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "le Soleil"}, {"libelle": "Repère 2", "reponse": "Mercure"},
                     {"libelle": "Repère 3", "reponse": "la Terre"}, {"libelle": "Repère 4", "reponse": "trajectoire de la Terre"}],
           "etiquettes": ["le Soleil", "Mercure", "la Terre", "trajectoire de la Terre", "la Lune", "trajectoire d'une comète"]},
      lecon="trajectoires"),
    E("4-3", "L'intrus du parc", "intrus",
      {"cm1": "Léonie a noté des objets qui tournent en rond. Trouve l'intrus : le seul qui se déplace en ligne droite.",
       "cm2": "Léonie a noté des mouvements circulaires. Trouve l'intrus : le seul mouvement qui n'est pas circulaire pour une personne immobile au sol."},
      BO + " ; " + EDU,
      "La grande roue, le manège et l'aiguille de l'horloge tournent autour d'un centre : leur mouvement est circulaire. L'ascenseur monte et descend tout droit : c'est l'intrus. En CM2, la Terre autour du Soleil, la pointe d'une pale d'éolienne, la nacelle et le cheval de bois décrivent des cercles ; le petit train sur la voie droite va en ligne droite.",
      {"cm1": ["Cherche ce qui tourne autour d'un centre.", "Un ascenseur monte et descend.", "L'intrus ne dessine pas de cercle."],
       "cm2": ["La Terre tourne autour du Soleil.", "La pale d'une éolienne tourne autour de son axe.", "Une voie droite donne une trajectoire rectiligne."]},
      cm1=intrus([("la grande roue", False), ("le manège", False), ("l'aiguille de l'horloge", False), ("l'ascenseur de l'observatoire", True)]),
      cm2=intrus([("la Terre autour du Soleil", False), ("la pointe d'une pale d'éolienne", False), ("la nacelle de la grande roue", False),
                  ("le cheval de bois du manège", False), ("le petit train sur la voie droite", True)]),
      lecon="trajectoires"),
    E("4-4", "Les notes de Léonie", "qcm",
      "Léonie a préparé quelques questions sur les mouvements du ciel et du circuit. Réponds à chaque question.",
      "Vikidia, « Terre » (troisième planète ; tour du Soleil en environ 365 jours et 6 heures) ; " + BO,
      "La Terre est la troisième planète à partir du Soleil ; elle en fait le tour en environ un an, soit à peu près 365 jours. Dans la descente, la caisse à savon prend de plus en plus de vitesse : son mouvement est accéléré. Au freinage, sa vitesse diminue : le mouvement est ralenti.",
      {"cm2": ["Un tour complet de la Terre autour du Soleil donne une année.", "Mercure, Vénus, puis...", "Accéléré : la vitesse augmente ; ralenti : elle diminue."]},
      commun=qcm([("En combien de temps la Terre fait-elle le tour du Soleil ?", ["En environ un jour", "En environ un mois", "En environ un an (365 jours)"], 2, "Un tour complet dure environ 365 jours."),
                  ("À partir du Soleil, la Terre est la...", ["troisième planète", "première planète", "dixième planète"], 0, "Mercure, Vénus, puis la Terre."),
                  ("Dans la descente, la caisse à savon va de plus en plus vite. Son mouvement est...", ["ralenti", "accéléré", "immobile"], 1, "Sa vitesse augmente."),
                  ("Avant l'arrivée, Yanis freine. Son mouvement est...", ["accéléré", "circulaire", "ralenti"], 2, "Sa vitesse diminue.")]),
      lecon="trajectoires", cm2_seul=True),
]})

# =================================================================== SALLE 5 — le quai du petit train (Hugo)
TCLAS = lambda cm2: tableau("Résultats officiels de la descente de 200 m (durées inventées pour le jeu)", ["Dossard", "Véhicule", "Durée"],
                            [["2", "le petit train", "1 min 15 s" if cm2 else "75 s"], ["4", "le vélo de Salomé", "41 s"], ["5", "la voiture solaire de l'école", "1 min 30 s" if cm2 else "90 s"],
                             ["7", "la caisse à savon de Yanis", "48 s"], ["9", "la trottinette de Léo", "1 min 03 s" if cm2 else "63 s"]])
S.append({"num": 5, "titre": "Le quai du petit train — Tout dépend de l'observateur", "enigmes": [
    E("5-1", "Les remarques des voyageurs", "vraifaux",
      {"cm1": "Hugo, le contrôleur du petit train, écoute les voyageurs. Le train roule ; Margaux est restée sur le quai. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Hugo, le contrôleur du petit train, écoute les voyageurs. Le train roule tout droit, à vitesse constante ; Margaux est restée sur le quai. Pour chaque phrase, choisis vrai ou faux."},
      BO + " (CM2 : « le mouvement d'un objet est toujours décrit par rapport à un observateur » ; « un objet qu'on lâche décrit une droite verticale par rapport à la personne qui le lâche ») ; " + EDU,
      "Un même voyageur peut être immobile et en mouvement : immobile pour Hugo, assis dans le même wagon, et en mouvement pour Margaux, restée sur le quai. On doit donc toujours dire par rapport à qui on décrit un mouvement. Dans le train qui roule tout droit à vitesse constante, le stylo lâché par Hugo tombe en ligne droite verticale par rapport à Hugo. Pour les voyageurs du train, c'est le quai qui défile.",
      {"cm1": ["Hugo et le voyageur sont assis dans le même wagon.", "Margaux, elle, ne monte pas dans le train.", "Un mouvement se décrit toujours « par rapport à » quelqu'un."],
       "cm2": ["Demande-toi toujours : qui regarde ?", "Pour le voyageur assis, le quai s'éloigne.", "Celui qui lâche un objet le voit tomber tout droit vers le bas."]},
      cm1=vf([("Pour Hugo, assis en face de lui, le voyageur est immobile.", True, "Ils roulent ensemble : pour Hugo, le voyageur ne bouge pas."),
              ("Pour Margaux, restée sur le quai, ce voyageur est en mouvement.", True, "Il s'éloigne d'elle avec le train."),
              ("Un objet est immobile ou en mouvement de la même façon pour tout le monde.", False, "Cela dépend de l'observateur."),
              ("Pour décrire un mouvement, il faut dire par rapport à qui.", True, "On choisit toujours un observateur.")]),
      cm2=vf([("Le voyageur assis est à la fois immobile pour Hugo et en mouvement pour Margaux.", True, "Les deux sont vrais : l'observateur n'est pas le même."),
              ("Le quai est immobile pour tous les observateurs.", False, "Pour les voyageurs du train, le quai défile."),
              ("Hugo lâche son stylo : par rapport à Hugo, le stylo tombe en ligne droite verticale.", True, "C'est ce que dit le programme pour la personne qui lâche l'objet."),
              ("Un objet immobile pour un observateur est immobile pour tous les autres.", False, "Un autre observateur peut le voir bouger."),
              ("Pour Margaux, le petit train a une trajectoire rectiligne sur la voie droite.", True, "La voie est droite.")]),
      lecon="observateur"),
    E("5-2", "Immobile ou en mouvement ?", "tri",
      {"cm1": "Hugo est assis dans le petit train qui roule. Pour Hugo, chaque chose est-elle immobile ou en mouvement ? Range chaque carte.",
       "cm2": "Range chaque situation : l'objet est-il immobile ou en mouvement pour l'observateur indiqué ? Le petit train roule ; Margaux est sur le quai."},
      BO + " (CM2 : « en fonction de l'observateur ») ; " + EDU,
      "Pour Hugo, assis dans le train, tout ce qui roule avec lui reste à la même place : son voisin, son sac et la fenêtre du wagon sont immobiles. L'arbre, la gare et la vache couchée dans le pré défilent : pour lui, ils sont en mouvement. Pour Margaux sur le quai, c'est l'inverse : le quai est immobile et le voyageur assis bouge.",
      {"cm1": ["Pour Hugo, ce qui roule avec lui ne bouge pas.", "Regarde par la fenêtre : qu'est-ce qui défile ?", "La vache ne bouge pas dans le pré, mais Hugo la voit passer."],
       "cm2": ["Lis bien qui est l'observateur sur chaque carte.", "Le même voyageur peut aller dans les deux colonnes.", "Un objet qui tombe est en mouvement."]},
      cm1=tri([("immobile", "Immobile pour Hugo"), ("mouvement", "En mouvement pour Hugo")],
              [("son voisin assis", "immobile"), ("son sac posé sur le siège", "immobile"), ("la fenêtre du wagon", "immobile"),
               ("l'arbre au bord de la voie", "mouvement"), ("la gare", "mouvement"), ("la vache couchée dans le pré", "mouvement")]),
      cm2=tri([("immobile", "Immobile pour l'observateur"), ("mouvement", "En mouvement pour l'observateur")],
              [("le voyageur assis, pour Hugo assis dans le wagon", "immobile"), ("le quai, pour Margaux", "immobile"), ("la locomotive, pour le conducteur assis dedans", "immobile"),
               ("le voyageur assis, pour Margaux sur le quai", "mouvement"), ("le quai, pour Hugo", "mouvement"), ("le stylo que Hugo vient de lâcher, pour Hugo", "mouvement")]),
      lecon="observateur"),
    E("5-3", "Le chronomètre officiel", "code",
      {"cm1": "Il est presque midi. Le chronomètre officiel ne s'ouvre qu'avec le classement de la descente : écris les numéros de dossard, du premier arrivé au dernier." + TCLAS(False),
       "cm2": "Il est presque midi. Le chronomètre officiel ne s'ouvre qu'avec le classement de la descente : écris les numéros de dossard, du plus rapide au plus lent, puis l'écart entre le premier et le dernier." + TCLAS(True)},
      BO + " (mesure de durées ; CM2 : conversions d'unités de temps) ; " + INV,
      "Sur la même descente de 200 m, on classe par durée croissante : dossard 4 (41 s), 7 (48 s), 9 (63 s), 2 (75 s), puis 5 (90 s). Le code est 47925. En CM2, il faut d'abord convertir : 1 min 03 s = 63 s, 1 min 15 s = 75 s et 1 min 30 s = 90 s. L'écart entre le premier et le dernier est de 90 − 41 = 49 s.",
      {"cm1": ["Même distance pour tous : le plus rapide a la plus petite durée.", "Le premier arrivé est le dossard 4.", "Écris les cinq dossards à la suite, sans espace."],
       "cm2": ["Convertis d'abord toutes les durées en secondes.", "1 min 03 s = 63 s.", "L'écart : durée du dernier moins durée du premier."]},
      cm1=code([("Code du chronomètre officiel", "47925")]),
      cm2=code([("Code du chronomètre officiel", "47925"), ("Écart entre le premier et le dernier (en s)", "49")]),
      lecon="observateur"),
    E("5-4", "Le message de la coupole", "lettres",
      "Léonie a envoyé un message au quai. Certaines lettres sont marquées : clique dans l'ordre celles qui forment le verbe qui résume le Grand Prix. Attention aux lettres pièges.",
      BO + " (« le mouvement d'un objet est toujours décrit par rapport à un observateur »)",
      "Avant de dire qu'un objet bouge ou ne bouge pas, il faut choisir qui le regarde : le mouvement se décrit toujours par rapport à un observateur. Le mot caché est OBSERVER.",
      {"cm2": ["Le mot a huit lettres.", "C'est ce que fait l'astronome avec sa lunette.", "Il commence par O et finit par R."]},
      commun={"cible": list("OBSERVER"),
              "texte": marque("<p>Bravo, commissaires ! Depuis ma c[o]upole, j'ai tout vu : le train qui ro[u]le, le vélo, la caisse à savon. Mais n'ou[b]liez pa[s] : pour le voyageur assis, son voisin ne bouge pas. Pour la p[e]rsonne sur le quai, il s'éloigne. Avant de dire qui bouge, il faut toujou[r]s choisir qui regarde. C'est la règle de tous les ast[r]onomes, ici [c]omme dans le ciel. Bonne route à [v]ous tous, et rendez-vous l'an proch[a]in pour un nouv[e]au Grand Prix !</p>")},
      lecon="observateur", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "Le Grand Prix de l'observatoire", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": BO + " ; Eduscol ; La main à la pâte ; Vikidia (Terre, TGV, vitesse des animaux) ; Fédération française de randonnée (vitesse d'un piéton) ; Club des villes et territoires cyclables (vitesse d'un cycliste). Mesures, durées et classements du Grand Prix : inventés pour le jeu. Détail : README.md, section Sources.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-1\",\"legende\":\"…\",\"source\":\"…\"}. Déposez alors e3-1.jpg dans assets/images/cartes/. Sans fichier, l'énigme reste jouable. Les schémas (décamètre, circuit, système solaire) sont dessinés en SVG par script : ne pas les remplacer par des images générées par IA."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
