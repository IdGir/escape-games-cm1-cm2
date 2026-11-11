# -*- coding: utf-8 -*-
"""Génère traite-colonies/assets/data/enigmes.json (Les Archives du port). Lancer : python gen_enigmes.py <dossier data>
Sujet sensible : les élèves sont des enquêteurs d'archives ; aucun jeu de rôle d'esclave ; vocabulaire : personnes réduites
en esclavage, captifs, traite négrière ; aucune image choquante ; aucun point lié au profit de la traite."""
import json, os, re, sys
from schemas import carte_triangle, carte_ports

BO = "Programme d'histoire-géographie du cycle 3 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026), thème « Explorations et conquêtes »"
BNF = "BnF, France-Amériques, « La traite négrière » (Cécile Vidal, 2021, d'après la base Slave Voyages)"
BDX = "Académie de Bordeaux, « Bordeaux et le commerce triangulaire » (cargaison de La Licorne, 1787 ; d'après le musée d'Aquitaine)"
MART = "Académie de Martinique, « Le travail à l'habitation-sucrerie » (M. Descas-Ravoteur)"
GUY = "Académie de Guyane, livret « Le marronnage »"
SEN = "Sénat, rapport sur la proposition de loi d'abrogation du Code noir (2026)"
CULT = "Ministère de la Culture, « Mémoires de la traite, de l'esclavage et de leurs abolitions » (loi n° 2001-434 du 21 mai 2001 ; décret n° 2006-388)"
HAITI = "BnF, France-Amériques, « Toussaint Louverture » ; Hérodote, « 1er janvier 1804 »"
NANTES = "Musée d'histoire de Nantes (château des ducs de Bretagne), présentation de la traite atlantique"
DEC1848 = "Décret du 27 avril 1848 relatif à l'abolition de l'esclavage (texte : mjp.univ-perp.fr)"


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


def marque(t):
    return re.sub(r"\[([A-Za-z])\]", lambda m: f"<b data-l='{m.group(1).upper()}'>{m.group(1)}</b>", t)


def tableau(titre, entetes, lignes):
    h = "".join(f"<th>{x}</th>" for x in entetes)
    c = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in l) + "</tr>" for l in lignes)
    return f"<p><i>{titre}</i></p><table class='tab-releves'><tr>{h}</tr>{c}</table>"


S = []
# =================================================================== SALLE 1 — la salle des cartes (Inès, archiviste)
S.append({"num": 1, "titre": "La salle des cartes — Le commerce triangulaire", "enigmes": [
    E("1-1", "La carte de l'Atlantique", "plan",
      {"cm1": "Inès, l'archiviste, a retrouvé la carte qui ouvrait le registre déchiré. Les noms des continents ont été effacés. Place chaque étiquette sur le bon repère. Clique sur une étiquette, puis sur la case du repère." + carte_triangle(3, "La carte du registre"),
       "cm2": "Inès a retrouvé la carte qui ouvrait le registre déchiré. Les noms ont été effacés. Place chaque étiquette sur le bon repère. Attention : il y a des étiquettes en trop." + carte_triangle(5, "La carte du registre")},
      BO + " ; " + BNF,
      "Le commerce triangulaire relie trois continents autour de l'océan Atlantique. L'Europe est au nord-est de la carte (repère 1), l'Afrique au sud-est (repère 2) et les Amériques à l'ouest (repère 3). En CM2, le repère 4 est posé sur l'océan Atlantique et le repère 5 sur le deuxième trajet, celui des captifs, de l'Afrique vers les Amériques.",
      {"cm1": ["L'Europe est en haut à droite de la carte.", "L'Afrique est juste en dessous de l'Europe.", "Les Amériques sont de l'autre côté de l'océan, à gauche."],
       "cm2": ["Repère d'abord les trois continents.", "Le repère 4 est posé sur la mer.", "Le repère 5 est sur la flèche qui part d'Afrique."]},
      cm1={"titre": "La carte du registre", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "Europe"}, {"libelle": "Repère 2", "reponse": "Afrique"}, {"libelle": "Repère 3", "reponse": "Amériques"}],
           "etiquettes": ["Europe", "Afrique", "Amériques"]},
      cm2={"titre": "La carte du registre", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "Europe"}, {"libelle": "Repère 2", "reponse": "Afrique"}, {"libelle": "Repère 3", "reponse": "Amériques"},
                     {"libelle": "Repère 4", "reponse": "océan Atlantique"}, {"libelle": "Repère 5", "reponse": "trajet des captifs"}],
           "etiquettes": ["Europe", "Afrique", "Amériques", "océan Atlantique", "trajet des captifs", "Asie", "océan Indien"]},
      lecon="triangle"),
    E("1-2", "Les trois trajets", "association",
      {"cm1": "Sur la carte, trois flèches dessinent un triangle. Relie chaque trajet à ce que transportait le navire.",
       "cm2": "Inès a retrouvé des fiches sur les trajets des navires. Relie chaque début de phrase à sa fin."},
      BO + " ; " + BDX + " ; " + BNF,
      "Au premier trajet, le navire part d'un port d'Europe chargé de marchandises : tissus, armes, alcool. Au deuxième trajet, il transporte des captifs africains vers les Amériques. Au troisième trajet, il revient en Europe chargé de sucre, de café ou de coton. En CM2 : la traversée avec les captifs durait en moyenne environ deux mois et Saint-Domingue recevait les trois quarts des expéditions françaises.",
      {"cm1": ["Le premier trajet part d'Europe.", "Le deuxième trajet traverse l'océan avec des personnes.", "Le sucre pousse aux Amériques : il revient en Europe."],
       "cm2": ["Suis les flèches dans l'ordre : 1, 2, 3.", "Les marchandises chargées en France servent à acheter des captifs.", "Saint-Domingue est une colonie française des Antilles."]},
      cm1=assoc([("1er trajet : de l'Europe vers l'Afrique", "des tissus, des armes et de l'alcool"),
                 ("2e trajet : de l'Afrique vers les Amériques", "des captifs africains"),
                 ("3e trajet : des Amériques vers l'Europe", "du sucre, du café et du coton")]),
      cm2=assoc([("Au départ de France, le navire emporte", "des tissus, des fusils et de l'eau-de-vie"),
                 ("Sur les côtes d'Afrique, ces marchandises sont échangées contre", "des captifs"),
                 ("La traversée de l'Atlantique avec les captifs dure en moyenne", "environ deux mois"),
                 ("Aux Antilles, les captifs sont vendus comme esclaves à", "des propriétaires de plantations"),
                 ("La principale destination des navires français est", "Saint-Domingue")]),
      lecon="triangle"),
    E("1-3", "Le voyage d'un navire", "ordre",
      {"cm1": "Les pages du journal de bord sont mélangées. Remets les étapes du voyage dans l'ordre.",
       "cm2": "Les pages du journal de bord sont mélangées. Remets les six étapes du voyage dans l'ordre, du départ au retour."},
      BO + " ; " + BNF + " ; " + BDX,
      "Le navire quitte d'abord un port français, chargé de marchandises. Sur les côtes d'Afrique, ces marchandises sont échangées contre des captifs. Puis vient la traversée de l'Atlantique, qui dure environ deux mois. Aux Antilles, les captifs sont vendus et le capitaine achète du sucre ou du café. Enfin, le navire rentre en Europe, où ces produits sont vendus. En CM2, le voyage commence par l'armateur, qui finance et équipe le navire.",
      {"cm1": ["Le voyage commence et finit dans le même port.", "On échange les marchandises avant de traverser l'océan.", "Le sucre est chargé aux Antilles, juste avant le retour."],
       "cm2": ["L'armateur intervient avant le départ.", "Suis le triangle : Europe, Afrique, Amériques, Europe.", "Les produits des colonies sont vendus à la fin, en Europe."]},
      cm1=ordre(["Le navire quitte un port français, chargé de marchandises.", "Sur les côtes d'Afrique, les marchandises sont échangées contre des captifs.",
                 "Le navire traverse l'océan Atlantique.", "Aux Antilles, les captifs sont vendus ; on charge du sucre.", "Le navire rentre en France."]),
      cm2=ordre(["Un armateur finance le navire et le fait charger de marchandises.", "Le navire quitte un port français, comme Nantes.",
                 "Sur les côtes d'Afrique, les marchandises sont échangées contre des captifs.", "Le navire traverse l'Atlantique : environ deux mois.",
                 "Aux Antilles, les captifs sont vendus comme esclaves ; on charge du sucre et du café.", "De retour en France, le sucre et le café sont vendus."]),
      lecon="triangle"),
    E("1-4", "Les questions d'Inès", "qcm",
      "Inès vérifie que vous avez bien lu la carte et le journal de bord. Réponds à chaque question.",
      BO + " ; " + BNF,
      "On parle de commerce « triangulaire » parce que les trois trajets du navire dessinent un triangle sur la carte. Le navire traverse l'océan Atlantique. L'armateur est celui qui finance et organise l'expédition. Les trois quarts des expéditions françaises allaient à Saint-Domingue, l'actuelle Haïti.",
      {"cm2": ["Regarde la forme des trois flèches.", "Un armateur ne navigue pas forcément : il paie et organise.", "Saint-Domingue est l'ancien nom d'Haïti."]},
      commun=qcm([("Pourquoi parle-t-on de commerce « triangulaire » ?", ["parce que les navires avaient trois mâts", "parce que les trois trajets dessinent un triangle", "parce qu'il durait trois ans"], 1, "Europe, Afrique, Amériques : trois trajets."),
                  ("Quel océan les navires traversent-ils ?", ["l'océan Indien", "l'océan Pacifique", "l'océan Atlantique"], 2, "D'où le nom de traite atlantique."),
                  ("Qui finance et organise l'expédition ?", ["l'armateur", "le roi seul", "les captifs"], 0, "L'armateur est un négociant qui arme le navire."),
                  ("Quelle colonie recevait la plupart des navires français ?", ["le Canada", "Saint-Domingue", "l'Inde"], 1, "Saint-Domingue recevait environ les trois quarts des expéditions.")]),
      lecon="triangle", cm2_seul=True),
]})

# =================================================================== SALLE 2 — le cabinet des registres (Malik, historien)
S.append({"num": 2, "titre": "Le cabinet des registres — La traite atlantique", "enigmes": [
    E("2-1", "Les fiches de Malik", "vraifaux",
      {"cm1": "Malik, historien venu de Dakar, relit les fiches des enquêteurs. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Malik, historien venu de Dakar, relit les fiches des enquêteurs. Pour chaque phrase, choisis vrai ou faux. Attention aux chiffres."},
      BO + " ; " + BNF + " ; " + NANTES,
      "La traite atlantique a déporté plus de 12,5 millions de personnes d'Afrique vers les Amériques, du XVIe au XIXe siècle. Les captifs ne partaient pas de leur plein gré : ils étaient achetés, enchaînés et transportés de force. Des ports français, comme Nantes, armaient des navires négriers. La traversée durait environ deux mois, et non deux jours. En CM2 : la France a transporté environ 11 % des captifs, Nantes a armé 44 % des expéditions françaises, environ 13 % des captifs mouraient pendant la traversée et environ 27 % étaient des enfants.",
      {"cm1": ["Une traversée de l'océan à la voile dure longtemps.", "Les captifs n'avaient pas choisi de partir.", "Nantes est un port sur la Loire, près de l'océan."],
       "cm2": ["11 % : un peu plus d'un sur dix.", "44 % : un peu moins de la moitié.", "Les captifs ne passaient pas par la France : relis le trajet 2."]},
      cm1=vf([("Des millions d'Africains ont été déportés vers les Amériques.", True, "Plus de 12,5 millions de personnes."),
              ("Les captifs montaient sur les navires de leur plein gré.", False, "Ils étaient emmenés de force."),
              ("Des navires négriers partaient de ports français, comme Nantes.", True, "Nantes était le premier port négrier français."),
              ("La traversée de l'Atlantique durait environ deux jours.", False, "Elle durait environ deux mois.")]),
      cm2=vf([("Plus de 12,5 millions de personnes ont été déportées par la traite atlantique.", True, "C'est l'estimation des historiens (base Slave Voyages)."),
              ("Les navires français ont transporté environ un captif sur dix.", True, "Environ 11 % de la traite atlantique."),
              ("Nantes a armé près de la moitié des expéditions négrières françaises.", True, "44 % des expéditions françaises."),
              ("Tous les captifs arrivaient vivants aux Amériques.", False, "Environ 13 % mouraient pendant la traversée."),
              ("Les captifs débarquaient à Nantes avant d'être envoyés aux Antilles.", False, "Ils étaient conduits directement d'Afrique aux Amériques.")]),
      lecon="traite"),
    E("2-2", "Trois continents, trois rangements", "tri",
      {"cm1": "Les fiches de lieux du registre sont tombées par terre. Range chaque lieu sur le bon continent.",
       "cm2": "Les fiches de lieux du registre sont tombées par terre. Range chaque lieu sur le bon continent. Les lieux d'Afrique sont les côtes où les navires français achetaient des captifs."},
      BO + " ; " + BNF,
      "Nantes, La Rochelle et Le Havre sont des ports français, en Europe. Le Sénégal et le golfe du Bénin sont des côtes d'Afrique où l'on achetait des captifs ; en CM2, on ajoute la côte de Loango, en Afrique centrale. Saint-Domingue, la Martinique et la Guadeloupe sont des îles des Antilles, en Amérique.",
      {"cm1": ["Les ports qui arment les navires sont en France.", "Le Sénégal est un pays d'Afrique.", "Les Antilles sont des îles d'Amérique."],
       "cm2": ["Le golfe du Bénin et Loango sont sur la côte ouest de l'Afrique.", "La Guadeloupe et la Martinique sont aujourd'hui des départements français d'Amérique.", "Saint-Domingue est aujourd'hui Haïti."]},
      cm1=tri([("europe", "Europe"), ("afrique", "Afrique"), ("amerique", "Amériques")],
              [("Nantes", "europe"), ("La Rochelle", "europe"), ("la côte du Sénégal", "afrique"), ("le golfe du Bénin", "afrique"),
               ("Saint-Domingue", "amerique"), ("la Martinique", "amerique")]),
      cm2=tri([("europe", "Europe"), ("afrique", "Afrique"), ("amerique", "Amériques")],
              [("Nantes", "europe"), ("La Rochelle", "europe"), ("Le Havre", "europe"), ("la côte du Sénégal", "afrique"), ("le golfe du Bénin", "afrique"),
               ("la côte de Loango", "afrique"), ("Saint-Domingue", "amerique"), ("la Martinique", "amerique"), ("la Guadeloupe", "amerique")]),
      lecon="traite"),
    E("2-3", "La page déchirée", "trous",
      {"cm1": "Une page du registre est déchirée. Complète le texte avec les bonnes étiquettes. Attention : il y a des étiquettes en trop.",
       "cm2": "Une page du registre est déchirée. Complète le texte avec les bonnes étiquettes. Attention : il y a des étiquettes en trop."},
      BO + " ; " + BNF,
      "On appelle traite négrière le commerce de captifs achetés en Afrique et vendus comme esclaves en Amérique ; des navires partaient de ports français comme Nantes. En CM2 : elle a duré du XVIe au XIXe siècle et a déporté plus de 12,5 millions de personnes ; en moyenne, un navire français transportait environ 320 captifs.",
      {"cm1": ["Les captifs sont achetés sur un continent et vendus sur un autre.", "Les captifs sont achetés en Afrique.", "Le port cité est sur la Loire."],
       "cm2": ["La traite dure plus de trois siècles.", "Le nombre de personnes déportées se compte en millions.", "Un navire transportait quelques centaines de captifs, pas des milliers."]},
      cm1={"texte": "<p>La traite négrière est le commerce de [[captifs]] achetés en [[Afrique]] et vendus comme esclaves en [[Amérique]]. Des navires partaient de ports français comme [[Nantes]].</p>",
           "etiquettes": ["captifs", "Afrique", "Amérique", "Nantes", "Asie", "Dijon", "marins"]},
      cm2={"texte": "<p>La traite atlantique a duré du [[XVIe]] au [[XIXe]] siècle. Elle a déporté plus de 12,5 [[millions]] de personnes d'Afrique vers les Amériques. En moyenne, un navire français transportait environ [[320]] captifs, entassés pendant une traversée d'environ deux [[mois]].</p>",
           "etiquettes": ["XVIe", "XIXe", "millions", "320", "mois", "XIIe", "milliers", "3 200", "jours"]},
      lecon="traite"),
    E("2-4", "Le cadenas des chiffres", "code",
      "Malik range ses chiffres pour mesurer l'ampleur de la traite française. Le tiroir du registre ne s'ouvre qu'avec trois nombres de sa fiche." + tableau("Fiche de Malik (d'après la BnF et la base Slave Voyages)", ["Ce que l'on mesure", "Résultat"],
        [["part de la France dans la traite atlantique", "environ 11 %"], ["part de Nantes dans les expéditions françaises", "44 %"], ["durée moyenne de la traversée", "environ deux mois"],
         ["captifs moyens par navire français", "environ 320"]]),
      BNF,
      "Le premier nombre est 11 : la France a transporté environ 11 captifs sur 100. Le deuxième est 44 : sur 100 expéditions françaises, 44 partaient de Nantes. Le troisième est 2 : la traversée durait environ deux mois.",
      {"cm2": ["« Sur 100 », c'est le pourcentage.", "Nantes : un peu moins de la moitié.", "La durée est en mois, pas en jours."]},
      commun=code([("Captifs transportés par la France (sur 100)", "11"), ("Expéditions françaises parties de Nantes (sur 100)", "44"), ("Durée moyenne de la traversée (en mois)", "2")]),
      lecon="traite", cm2_seul=True),
]})

# =================================================================== SALLE 3 — le fonds des colonies (Célia, historienne guadeloupéenne)
S.append({"num": 3, "titre": "Le fonds des colonies — Les plantations", "enigmes": [
    E("3-1", "Du champ au sucre", "ordre",
      {"cm1": "Célia, historienne venue de Guadeloupe, étudie le plan d'une habitation sucrière. Remets dans l'ordre le travail que les esclaves étaient forcés de faire.",
       "cm2": "Célia étudie le plan d'une habitation sucrière. Remets dans l'ordre les étapes du travail forcé des esclaves, de la canne au navire."},
      BO + " ; " + MART,
      "Les esclaves coupent d'abord la canne à sucre dans les champs, pendant la récolte. La canne est portée au moulin, où elle est broyée : on en tire un jus, le vesou. Dans la sucrerie, ce jus est transformé en sucre. Le sucre est ensuite mis en barriques et chargé sur les navires. En CM2, on ajoute le dépaillage et la mise en paquets de la canne, et le passage par la purgerie.",
      {"cm1": ["Tout commence dans les champs.", "Le moulin broie la canne.", "Le navire emporte le sucre à la fin."],
       "cm2": ["On coupe avant de dépailler.", "Le vesou est le jus de la canne : il sort du moulin.", "La purgerie vient après la sucrerie."]},
      cm1=ordre(["Couper la canne à sucre dans les champs.", "Porter la canne au moulin et la broyer pour en tirer le jus.",
                 "Transformer le jus en sucre dans la sucrerie.", "Mettre le sucre en barriques et le charger sur les navires."]),
      cm2=ordre(["Couper la canne à sucre pendant la récolte.", "Enlever les feuilles (dépailler) et mettre la canne en paquets.",
                 "Broyer la canne au moulin pour récolter le vesou, le jus de canne.", "Transformer le vesou en sucre dans la sucrerie.",
                 "Faire sécher et blanchir le sucre dans la purgerie.", "Mettre le sucre en barriques et le charger sur les navires vers l'Europe."]),
      lecon="plantations"),
    E("3-2", "Ce que dit le Code noir", "qcm",
      {"cm1": "Célia a ouvert un vieux livre de lois : le Code noir. Elle l'explique avec des mots simples. Réponds à chaque question.",
       "cm2": "Célia a ouvert le Code noir. Elle l'explique avec des mots simples. Réponds à chaque question."},
      BO + " ; " + SEN + " ; " + MART,
      "Dans les plantations, ce sont des esclaves qui travaillent, de force et sans salaire. Le Code noir est un édit du roi Louis XIV, de mars 1685, qui fixe les règles de l'esclavage dans les colonies. Pour cette loi, l'esclave est considéré comme un « bien meuble » : on peut le vendre comme un objet. Il punit sévèrement les esclaves. Pendant la récolte, la journée de travail pouvait dépasser 18 heures. En 2026, une loi l'a officiellement abrogé.",
      {"cm1": ["Le Code noir est une loi.", "Il date du règne de Louis XIV.", "Un « bien » est une chose que l'on possède."],
       "cm2": ["1685 : fin du XVIIe siècle.", "Un « bien meuble » peut être déplacé et vendu.", "Pendant la récolte, les journées étaient extrêmement longues."]},
      cm1=qcm([("Qui travaillait de force dans les champs de canne ?", ["des esclaves", "des ouvriers payés", "des machines"], 0, "Des personnes réduites en esclavage, sans salaire."),
               ("Le Code noir, c'est...", ["un livre de cuisine", "une loi du roi sur l'esclavage dans les colonies", "un journal de bord"], 1, "Un édit de Louis XIV, en 1685."),
               ("Pour le Code noir, un esclave était...", ["un citoyen libre", "un soldat du roi", "considéré comme un bien que l'on pouvait vendre"], 2, "Il le traitait comme un « bien meuble ».")]),
      cm2=qcm([("En quelle année le Code noir a-t-il été signé ?", ["1492", "1685", "1789"], 1, "En mars 1685."),
               ("Sous le règne de quel roi ?", ["Louis XIV", "François Ier", "Henri IV"], 0, "Louis XIV, le roi de Versailles."),
               ("Pour le Code noir, l'esclave était un « bien meuble ». Cela veut dire...", ["qu'il fabriquait des meubles", "qu'il était considéré comme une chose que l'on pouvait vendre", "qu'il était libre de déménager"], 1, "La loi niait qu'il soit une personne libre."),
               ("Pendant la récolte, la journée de travail pouvait dépasser...", ["8 heures", "4 heures", "18 heures"], 2, "Pendant la roulaison, plus de 18 heures.")]),
      lecon="plantations"),
    E("3-3", "Résister", "tri",
      {"cm1": "Célia montre que les esclaves n'ont jamais accepté leur sort. Range chaque carte : est-ce une forme de résistance des esclaves, ou une règle imposée par les maîtres et le Code noir ?",
       "cm2": "Célia classe les formes de résistance. Range chaque carte dans la bonne colonne."},
      BO + " ; " + GUY + " ; " + SEN,
      "S'enfuir de la plantation (le marronnage), se révolter et garder ses chants et ses contes sont des formes de résistance. Être vendu comme un bien, travailler sans salaire et être puni sévèrement sont des règles imposées par les maîtres et par le Code noir. En CM2 : le petit marronnage est une fuite de quelques jours ; le grand marronnage est une fuite définitive, en groupe, dans la forêt ou les montagnes ; la révolte est une autre forme de résistance.",
      {"cm1": ["Résister, c'est refuser ce que l'on vous impose.", "Un esclave en fuite est appelé un « marron ».", "Les règles du Code noir sont imposées aux esclaves."],
       "cm2": ["Le petit marronnage dure quelques jours.", "Le grand marronnage est sans retour.", "Une révolte rassemble beaucoup de personnes contre les maîtres."]},
      cm1=tri([("resiste", "Une forme de résistance"), ("impose", "Une règle imposée par les maîtres")],
              [("s'enfuir de la plantation", "resiste"), ("se révolter", "resiste"), ("garder ses chants et ses contes", "resiste"),
               ("être vendu comme un bien", "impose"), ("travailler sans salaire", "impose"), ("être puni sévèrement", "impose")]),
      cm2=tri([("petit", "Petit marronnage"), ("grand", "Grand marronnage"), ("autre", "Révolte")],
              [("fuir quelques jours, puis revenir", "petit"), ("se cacher près de la plantation un moment", "petit"),
               ("fuir sans retour dans la forêt", "grand"), ("vivre en groupe dans les montagnes, de chasse et de pêche", "grand"),
               ("se soulever à plusieurs contre les maîtres", "autre"), ("l'insurrection de Saint-Domingue en août 1791", "autre")]),
      lecon="plantations"),
    E("3-4", "Le lexique des archives", "association",
      "Célia prépare le lexique pour les autres enquêteurs. Relie chaque mot à sa définition.",
      GUY + " ; " + MART + " ; " + SEN,
      "Un édit est une loi signée par le roi. L'habitation est le nom donné à la plantation aux Antilles. Le vesou est le jus de la canne. Un marron est un esclave qui s'est enfui. Le mot vient de l'espagnol cimarrón. Un affranchi est un esclave devenu libre.",
      {"cm2": ["« Habitation » ne veut pas dire ici une simple maison.", "Le vesou sort du moulin.", "Affranchir, c'est rendre libre."]},
      commun=assoc([("un édit", "une loi signée par le roi"), ("une habitation", "le nom de la plantation aux Antilles"), ("le vesou", "le jus de la canne à sucre"),
                    ("un marron", "un esclave qui s'est enfui"), ("un affranchi", "un esclave devenu libre")]),
      lecon="plantations", cm2_seul=True),
]})

# =================================================================== SALLE 4 — le musée du port (Margot, conservatrice)
S.append({"num": 4, "titre": "Le musée du port — Les échanges avec les colonies", "enigmes": [
    E("4-1", "Les produits des colonies", "association",
      {"cm1": "Margot, conservatrice du musée du port, a vidé une vitrine pour la nettoyer. Relie chaque produit venu des colonies à ce que l'on en fait.",
       "cm2": "Margot, conservatrice du musée du port, a vidé une vitrine. Relie chaque produit des colonies d'Amérique à la plante dont il vient ou à son usage."},
      BO + " ; " + BDX,
      "Le sucre vient de la canne à sucre et sucre les desserts. Le café se boit chaud. Le coton sert à fabriquer des tissus. En CM2 : le cacao donne le chocolat et l'indigo est une teinture bleue tirée d'une plante. Ces produits, cultivés par des esclaves, étaient vendus très cher en Europe.",
      {"cm1": ["Le sucre vient d'une grande plante, la canne.", "On boit le café.", "Le coton est une fibre."],
       "cm2": ["Le chocolat se fabrique avec du cacao.", "L'indigo colore en bleu.", "Le sucre de cette époque vient de la canne, pas de la betterave."]},
      cm1=assoc([("le sucre", "sert à sucrer les desserts"), ("le café", "se boit chaud"), ("le coton", "sert à fabriquer des tissus")]),
      cm2=assoc([("le sucre", "tiré de la canne à sucre"), ("le café", "tiré des grains du caféier"), ("le cacao", "sert à faire le chocolat"),
                 ("le coton", "sert à tisser des étoffes"), ("l'indigo", "donne une teinture bleue")]),
      lecon="ports"),
    E("4-2", "L'intrus de la vitrine", "intrus",
      {"cm1": "Margot remet les objets dans la vitrine « Ports de la traite ». Trouve l'intrus : la seule ville qui n'est pas un port de l'Atlantique ou de la Manche.",
       "cm2": "Margot prépare la vitrine « Ports de la traite ». Trouve l'intrus : la seule ville qui n'a pas armé de navires négriers, parce qu'elle n'est pas un port de mer."},
      BO + " ; " + BNF,
      "Nantes, La Rochelle et Le Havre sont des ports d'où partaient des navires négriers. Dijon est une ville de l'intérieur des terres : c'est l'intrus. En CM2, Saint-Malo et Honfleur sont aussi des ports de la traite ; Lyon, loin de la mer, est l'intrus. Attention : on ne généralise pas l'histoire d'un port à toute la France.",
      {"cm1": ["Un navire part d'un port, au bord de la mer.", "Cherche la ville qui est loin de la mer.", "Dijon est en Bourgogne."],
       "cm2": ["Les ports cités par la BnF sont sur la Manche ou l'Atlantique.", "Saint-Malo est en Bretagne, Honfleur en Normandie.", "Lyon est sur le Rhône, loin de l'océan."]},
      cm1=intrus([("Nantes", False), ("La Rochelle", False), ("Le Havre", False), ("Dijon", True)]),
      cm2=intrus([("Nantes", False), ("Le Havre", False), ("La Rochelle", False), ("Saint-Malo", False), ("Honfleur", False), ("Lyon", True)]),
      lecon="ports"),
    E("4-3", "Le départ et le retour", "tri",
      {"cm1": "Dans la réserve du musée, Margot trie les copies de documents de bord. Range chaque marchandise : part-elle de France pour l'Afrique, ou revient-elle des colonies d'Amérique ?",
       "cm2": "Margot reconstitue la cargaison d'un navire parti de Bordeaux en 1787. Range chaque marchandise : chargée en France pour l'Afrique, ou rapportée des colonies d'Amérique ?"},
      BO + " ; " + BDX,
      "Pour l'Afrique, les navires emportent des tissus, des fusils, de la poudre, de l'eau-de-vie et du fer en barre. Des colonies d'Amérique, ils rapportent du sucre, du café, du cacao, du coton et de l'indigo. La Licorne, partie de Bordeaux en janvier 1787, emportait aussi du vin et des liqueurs.",
      {"cm1": ["Les marchandises du départ servent à acheter des captifs.", "Le sucre pousse aux Antilles.", "Les armes sont fabriquées en Europe."],
       "cm2": ["Regarde ce qui se cultive dans les plantations.", "L'eau-de-vie et le vin viennent de France.", "Le fer en barre est un produit européen."]},
      cm1=tri([("depart", "Part de France pour l'Afrique"), ("retour", "Revient des colonies d'Amérique")],
              [("des tissus", "depart"), ("des fusils", "depart"), ("de l'eau-de-vie", "depart"),
               ("du sucre", "retour"), ("du café", "retour"), ("du coton", "retour")]),
      cm2=tri([("depart", "Chargé en France pour l'Afrique"), ("retour", "Rapporté des colonies d'Amérique")],
              [("des toiles et des draperies", "depart"), ("des fusils et de la poudre", "depart"), ("de l'eau-de-vie et du vin", "depart"), ("du fer en barre", "depart"),
               ("du sucre", "retour"), ("du café", "retour"), ("du cacao", "retour"), ("de l'indigo", "retour")]),
      lecon="ports"),
    E("4-4", "La carte des ports", "plan",
      "Margot accroche au mur une carte des ports. Les noms ont disparu. Place chaque étiquette sur le bon repère. Attention : il y a des étiquettes en trop." + carte_ports(),
      BO + " ; " + BNF + " ; " + BDX + " ; " + NANTES,
      "Le repère 1, au bord de la Manche, à l'embouchure de la Seine, est Le Havre. Le repère 2, sur l'estuaire de la Loire, est Nantes, le premier port négrier français. Le repère 3, sur la côte atlantique, est La Rochelle. Le repère 4, sur la Garonne, est Bordeaux, port du commerce avec les colonies. Marseille et Lyon ne sont pas sur cette façade.",
      {"cm2": ["Le Havre est sur la Manche, tout au nord.", "Nantes est sur la Loire, Bordeaux sur la Garonne.", "La Rochelle est entre les deux."]},
      commun={"titre": "Ports de l'Atlantique et de la Manche", "colonnes": 2,
              "cases": [{"libelle": "Repère 1", "reponse": "Le Havre"}, {"libelle": "Repère 2", "reponse": "Nantes"},
                        {"libelle": "Repère 3", "reponse": "La Rochelle"}, {"libelle": "Repère 4", "reponse": "Bordeaux"}],
              "etiquettes": ["Le Havre", "Nantes", "La Rochelle", "Bordeaux", "Marseille", "Lyon"]},
      lecon="ports", cm2_seul=True),
]})

# =================================================================== SALLE 5 — la salle de lecture (Théo, élève de l'atelier d'enquête)
S.append({"num": 5, "titre": "La salle de lecture — Résistances et abolitions", "enigmes": [
    E("5-1", "La frise de la liberté", "ordre",
      {"cm1": "Théo, un élève de l'atelier d'enquête, a écrit chaque événement sur une carte, mais les cartes sont mélangées. Range-les de la plus ancienne à la plus récente. La date est écrite sous chaque carte.",
       "cm2": "Théo a écrit chaque événement sur une carte, sans la date. Range-les de la plus ancienne à la plus récente."},
      BO + " ; " + BNF + " ; " + HAITI + " ; " + DEC1848 + " ; " + CULT,
      "Le Code noir date de 1685. Les esclaves de Saint-Domingue se révoltent en août 1791. La Convention abolit l'esclavage le 4 février 1794. Napoléon Bonaparte le rétablit le 20 mai 1802. Haïti devient indépendante le 1er janvier 1804. L'esclavage est aboli définitivement par le décret du 27 avril 1848. En 2001, une loi reconnaît la traite et l'esclavage comme un crime contre l'humanité.",
      {"cm1": ["Lis les dates sous les cartes.", "La plus petite date est la plus ancienne.", "1794 vient avant 1802."],
       "cm2": ["Le Code noir est sous Louis XIV.", "La révolte de Saint-Domingue précède la première abolition.", "L'indépendance d'Haïti suit le rétablissement de l'esclavage."]},
      cm1=ordre([("Le Code noir fixe les règles de l'esclavage.", "1685"), ("Les esclaves de Saint-Domingue se révoltent.", "1791"),
                 ("Première abolition de l'esclavage.", "1794"), ("Napoléon Bonaparte rétablit l'esclavage.", "1802"),
                 ("Abolition définitive de l'esclavage.", "1848")]),
      cm2=ordre(["Le Code noir fixe les règles de l'esclavage dans les colonies.", "Les esclaves de Saint-Domingue se révoltent.",
                 "La Convention abolit l'esclavage.", "Napoléon Bonaparte, Premier consul, rétablit l'esclavage.",
                 "Saint-Domingue devient Haïti, un pays indépendant.", "Le décret du gouvernement provisoire abolit définitivement l'esclavage.",
                 "Une loi reconnaît la traite et l'esclavage comme un crime contre l'humanité."]),
      lecon="abolitions"),
    E("5-2", "Les fiches des personnages", "qcm",
      {"cm1": "Théo prépare des fiches sur des personnes réelles de cette histoire. Réponds à chaque question.",
       "cm2": "Théo prépare des fiches sur des personnes réelles et des dates de mémoire. Réponds à chaque question."},
      BO + " ; " + HAITI + " ; " + DEC1848 + " ; " + CULT,
      "Toussaint Louverture, né esclave à Saint-Domingue, est devenu l'un des chefs de la révolte de 1791 puis gouverneur de la colonie. Victor Schœlcher a présidé la commission qui a préparé le décret d'abolition de 1848. Le 10 mai est la journée nationale des mémoires de la traite, de l'esclavage et de leurs abolitions, commémorée depuis 2006. En CM2 : c'est Napoléon Bonaparte, Premier consul, qui rétablit l'esclavage en 1802 ; la loi du 21 mai 2001 reconnaît la traite et l'esclavage comme un crime contre l'humanité.",
      {"cm1": ["Toussaint Louverture est né à Saint-Domingue.", "Schœlcher est lié à l'année 1848.", "Le 10 mai est une journée de mémoire."],
       "cm2": ["Le rétablissement de 1802 est l'œuvre du Premier consul.", "Un crime contre l'humanité ne peut pas être oublié.", "La journée du 10 mai existe depuis 2006."]},
      cm1=qcm([("Toussaint Louverture était...", ["un roi de France", "un ancien esclave devenu chef de la révolte de Saint-Domingue", "un armateur de Nantes"], 1, "Né esclave, il devient un chef de la révolte."),
               ("Victor Schœlcher est connu pour...", ["l'abolition de l'esclavage en 1848", "le Code noir", "la découverte de l'Amérique"], 0, "Il a préparé le décret de 1848."),
               ("Le 10 mai, en France, c'est...", ["la fête nationale", "le jour de la rentrée", "la journée des mémoires de la traite et de l'esclavage"], 2, "Journée nationale depuis 2006.")]),
      cm2=qcm([("Qui rétablit l'esclavage en 1802 ?", ["Louis XIV", "Napoléon Bonaparte, Premier consul", "Victor Schœlcher"], 1, "Le 20 mai 1802."),
               ("Toussaint Louverture devient...", ["gouverneur de Saint-Domingue", "roi de France", "armateur à Bordeaux"], 0, "En 1798, il est gouverneur de la colonie."),
               ("Que reconnaît la loi du 21 mai 2001 ?", ["que la traite était utile", "que le Code noir est toujours valable", "que la traite et l'esclavage sont un crime contre l'humanité"], 2, "C'est la loi n° 2001-434."),
               ("Depuis quand le 10 mai est-il la journée nationale des mémoires de la traite ?", ["1848", "2006", "1685"], 1, "Depuis 2006.")]),
      lecon="abolitions"),
    E("5-3", "Le fermoir du registre", "code",
      {"cm1": "Le registre reconstitué est fermé par un fermoir à chiffres. Il s'ouvre avec les années des deux abolitions de l'esclavage en France : la première, puis l'abolition définitive.",
       "cm2": "Le registre reconstitué est fermé par un fermoir à chiffres. Il s'ouvre avec quatre années : la première abolition, le rétablissement, l'indépendance d'Haïti et l'abolition définitive."},
      BNF + " ; " + HAITI + " ; " + DEC1848,
      "L'esclavage est aboli une première fois le 4 février 1794, puis définitivement par le décret du 27 avril 1848 : le code CM1 est 1794 puis 1848. En CM2, il faut aussi 1802, l'année du rétablissement par Napoléon Bonaparte, et 1804, l'année de l'indépendance d'Haïti.",
      {"cm1": ["Relis la frise de Théo.", "La première abolition est à la fin du XVIIIe siècle.", "L'abolition définitive est au milieu du XIXe siècle."],
       "cm2": ["Les trois premières années sont très proches.", "Le rétablissement a lieu huit ans après la première abolition.", "Haïti devient indépendante deux ans après le rétablissement."]},
      cm1=code([("Première abolition", "1794"), ("Abolition définitive", "1848")]),
      cm2=code([("Première abolition", "1794"), ("Rétablissement", "1802"), ("Indépendance d'Haïti", "1804"), ("Abolition définitive", "1848")]),
      lecon="abolitions"),
    E("5-4", "Le mot de la dernière page", "lettres",
      "Sur la dernière page du registre, Inès a recopié un message. Certaines lettres sont marquées : retrouve, avec elles, le mot qui résume le devoir des enquêteurs. Range les lettres dans les cases. Attention aux lettres pièges.",
      BO + " ; " + CULT,
      "Le mot caché est MEMOIRE. Se souvenir de la traite et de l'esclavage, de leurs victimes, des résistances et des abolitions est un devoir reconnu par la loi du 21 mai 2001 et par la journée nationale du 10 mai.",
      {"cm2": ["Le mot a sept lettres.", "C'est ce que l'on garde du passé pour ne pas l'oublier.", "On le retrouve dans le nom de la journée du 10 mai."]},
      commun={"cible": list("MEMOIRE"),
              "texte": marque("<p>Chers enquêteurs, le registre est complet. Vous avez suivi le t[r]ajet des navires, ét[u]dié les chiffres, les p[o]rts, les plantations et les lois. Des millions de personnes ont été arrachées à l'Afr[i]que. Elles ont résisté, se sont ré[v]oltées, ont conquis leur li[b]erté. Les archives gardent leurs trac[e]s : à nous de les lire, de les transmettre et de ne ja[m]ais les oubli[e]r. [M]erci pour votre enquête.</p>")},
      lecon="abolitions", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "Les Archives du port", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": BO + " ; " + BNF + " ; " + BDX + " ; " + MART + " ; " + GUY + " ; " + SEN + " ; " + CULT + " ; " + HAITI + " ; " + NANTES + " ; " + DEC1848 + ". Détail : README.md, section Sources.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-1\",\"legende\":\"…\",\"source\":\"…\"}. Déposez alors e3-1.jpg dans assets/images/cartes/. Sans fichier, l'énigme reste jouable. Les cartes sont dessinées en SVG par script : ne jamais les remplacer par des images générées par IA. Sujet sensible : aucune image de violence."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
