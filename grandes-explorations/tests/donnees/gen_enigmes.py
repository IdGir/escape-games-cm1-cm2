# -*- coding: utf-8 -*-
"""Génère grandes-explorations/assets/data/enigmes.json (La Caravelle du capitaine). Lancer : python gen_enigmes.py <dossier data>
Vigilance : on écrit « arrivée des Européens » à côté des repères classiques ; ton sobre sur les violences de la conquête ;
les habitants d'Amérique ont une voix propre (Itzel) ; personnages inventés ; les personnes réelles ne parlent jamais."""
import json, os, re, sys
from schemas import carte_monde_1450, schema_caravelle, carte_routes, carte_tordesillas

BO = "Programme d'histoire-géographie du cycle 3 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026), thème « Explorations et conquêtes »"
BNF = "BnF, exposition « L'âge d'or des cartes marines »"
MARINE = "Musée national de la Marine (instruments de navigation)"
HERO_COLOMB = "Hérodote, « La vérité sur les bateaux de Colomb »"
HERO_GAMA = "Hérodote, « 20 mai 1498 : Vasco de Gama à Calicut »"
HERO_CARTIER = "Hérodote, « 24 juillet 1534 : Jacques Cartier à Gaspé »"
NATGEO = "National Geographic, « Juan Sebastián Elcano, premier à faire le tour du monde »"
WHE_TORDE = "World History Encyclopedia, « Le traité de Tordesillas » ; UNESCO, Mémoire du monde"
WHE_CONQ = "World History Encyclopedia, « La conquête ibérique des Amériques » ; Schoolmouv, « Siège de Tenochtitlán (1521) »"
BANQ = "Bibliothèque et Archives nationales du Québec (Nouvelle-France)"
LUMNI = "Lumni, « Les grandes découvertes »"


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


S = []
# =================================================================== SALLE 1 — la cale aux épices (Amaury, négociant)
S.append({"num": 1, "titre": "La cale aux épices — Pourquoi partir ?", "enigmes": [
    E("1-1", "La carte du monde connu", "plan",
      {"cm1": "Amaury, le négociant, déroule une carte du monde tel que les Européens le connaissaient vers 1450. L'eau a effacé les noms. Place chaque étiquette sur le bon repère : clique sur une étiquette, puis sur la case du repère." + carte_monde_1450(3, "La carte d'Amaury (vers 1450)"),
       "cm2": "Amaury déroule une carte du monde connu des Européens vers 1450. Les noms ont été effacés. Place chaque étiquette sur son repère. Attention : il y a des étiquettes en trop." + carte_monde_1450(5, "La carte d'Amaury (vers 1450)")},
      BO + " ; " + BNF + " ; " + LUMNI,
      "Sur cette carte, l'Europe est le repère 1, l'Afrique le repère 2 et l'Asie le repère 3. Les terres en pointillés, à gauche, sont celles que les Européens ne connaissaient pas encore : les Amériques. En CM2, le repère 4 est la mer Méditerranée et le repère 5 la route des épices, qui traverse l'Asie par la terre.",
      {"cm1": ["L'Europe est la plus petite des trois terres du milieu, en haut.", "L'Afrique est sous l'Europe.", "L'Asie est la grande terre à droite."],
       "cm2": ["Les Amériques sont dessinées en pointillés : les Européens ne les connaissent pas.", "Le repère 4 est une mer fermée entre l'Europe et l'Afrique.", "La ligne marron qui vient de l'Asie est celle des épices."]},
      cm1={"titre": "La carte d'Amaury", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "Europe"}, {"libelle": "Repère 2", "reponse": "Afrique"}, {"libelle": "Repère 3", "reponse": "Asie"}],
           "etiquettes": ["Europe", "Afrique", "Asie"]},
      cm2={"titre": "La carte d'Amaury", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "Europe"}, {"libelle": "Repère 2", "reponse": "Afrique"}, {"libelle": "Repère 3", "reponse": "Asie"},
                     {"libelle": "Repère 4", "reponse": "mer Méditerranée"}, {"libelle": "Repère 5", "reponse": "route des épices"}],
           "etiquettes": ["Europe", "Afrique", "Asie", "mer Méditerranée", "route des épices", "Amériques", "océan Pacifique"]},
      lecon="epices"),
    E("1-2", "Les sacs de la cale", "association",
      {"cm1": "Dans la cale, des sacs et des coffres ont perdu leurs étiquettes. Relie chaque produit à ce qu'on en fait.",
       "cm2": "Amaury a noté sur des fiches les raisons de partir explorer. Relie chaque raison à ce que les voyageurs espèrent."},
      BO + " ; " + LUMNI,
      "Les épices, comme le poivre, parfument et conservent les aliments. L'or sert à fabriquer des pièces de monnaie. La soie est un tissu précieux venu de Chine. En CM2 : les marchands espèrent acheter les épices moins cher, les rois veulent de l'or et de nouvelles terres, l'Église veut répandre la religion chrétienne, les marins veulent la gloire et les savants mieux connaître le monde.",
      {"cm1": ["Le poivre se met dans la nourriture.", "Avec l'or, on frappe des pièces.", "La soie est un tissu très doux."],
       "cm2": ["Les marchands pensent à l'argent qu'ils vont gagner.", "Répandre une religion, c'est une raison religieuse.", "Les savants veulent apprendre."]},
      cm1=assoc([("le poivre et la cannelle", "parfument et conservent les aliments"), ("l'or", "sert à fabriquer des pièces de monnaie"), ("la soie", "est un tissu précieux venu de Chine")]),
      cm2=assoc([("les marchands", "acheter les épices moins cher, directement en Asie"), ("les rois", "trouver de l'or et de nouvelles terres"),
                 ("l'Église", "répandre la religion chrétienne"), ("les marins", "gagner la gloire et des récompenses"), ("les savants", "mieux connaître le monde")]),
      lecon="epices"),
    E("1-3", "Vrai ou légende ?", "vraifaux",
      {"cm1": "Amaury entend beaucoup d'histoires sur le port. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Amaury trie les histoires du port : certaines sont des légendes. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + LUMNI + " ; " + BNF,
      "Le poivre venait bien d'Asie, de très loin, et coûtait très cher. Les savants savaient déjà que la Terre est ronde : la Terre plate est une légende. Les Européens ne connaissaient pas les Amériques. En CM2 : en 1453, les Turcs ottomans prennent Constantinople, et les Portugais longent déjà les côtes d'Afrique au XVe siècle.",
      {"cm1": ["Le poivre fait un très long voyage.", "Les savants de l'époque avaient étudié la forme de la Terre.", "Les Amériques étaient inconnues des Européens."],
       "cm2": ["Constantinople est prise au milieu du XVe siècle.", "La Terre plate est une légende inventée bien plus tard.", "Les Portugais explorent l'Afrique avant Colomb."]},
      cm1=vf([("Le poivre venait d'Asie et coûtait très cher.", True, "Il passait par de nombreux marchands."),
              ("Vers 1450, les savants pensaient que la Terre était plate.", False, "Ils savaient qu'elle est ronde."),
              ("Vers 1450, les Européens connaissaient déjà les Amériques.", False, "Ils ignoraient leur existence.")]),
      cm2=vf([("En 1453, les Turcs ottomans prennent Constantinople.", True, "Ils contrôlent une partie des routes vers l'Asie."),
              ("Les savants de 1450 pensaient que la Terre était plate.", False, "Ils savaient qu'elle est ronde, mais la croyaient plus petite."),
              ("Les épices passaient par de nombreux marchands, ce qui augmentait leur prix.", True, "D'où l'idée d'aller les chercher soi-même."),
              ("Au XVe siècle, les marins portugais longent les côtes d'Afrique.", True, "Ils cherchent un passage vers l'Asie."),
              ("Vers 1450, l'Amérique figurait sur les cartes européennes.", False, "Elle était inconnue des Européens.")]),
      lecon="epices"),
    E("1-4", "Les caisses du négociant", "tri",
      "Amaury range ses caisses de documents selon la raison du voyage. Place chaque carte dans la bonne colonne.",
      BO + " ; " + LUMNI,
      "Acheter du poivre moins cher et trouver de l'or sont des raisons de richesse. Répandre la religion chrétienne est une raison religieuse. Mieux connaître le monde et dessiner de nouvelles cartes sont des raisons de savoir, comme gagner la gloire auprès du roi pour les marins.",
      {"cm2": ["Tout ce qui rapporte de l'argent va dans la richesse.", "La religion chrétienne : colonne religion.", "Les cartes et les découvertes : colonne savoir et gloire."]},
      commun=tri([("richesse", "Richesse"), ("religion", "Religion"), ("savoir", "Savoir et gloire")],
                 [("acheter le poivre moins cher", "richesse"), ("trouver de l'or", "richesse"), ("répandre la religion chrétienne", "religion"),
                  ("baptiser les peuples rencontrés", "religion"), ("dessiner de nouvelles cartes", "savoir"), ("être récompensé par le roi", "savoir")]),
      lecon="epices", cm2_seul=True),
]})

# =================================================================== SALLE 2 — le pont de la caravelle (Rosa, cartographe)
S.append({"num": 2, "titre": "Le pont de la caravelle — Les progrès techniques", "enigmes": [
    E("2-1", "Les instruments de Rosa", "association",
      {"cm1": "Rosa, la cartographe, a sorti ses instruments de leur coffre. Relie chaque instrument à ce qu'il permet de faire.",
       "cm2": "Rosa, la cartographe, a sorti tous ses instruments. Relie chaque instrument à son rôle à bord."},
      BO + " ; " + MARINE + " ; " + BNF,
      "La boussole indique le nord grâce à son aiguille aimantée. L'astrolabe mesure la hauteur du Soleil ou d'une étoile. La carte marine montre les côtes et les ports. En CM2 : le quadrant mesure aussi la hauteur d'un astre, comme l'étoile Polaire, et le sablier mesure le temps passé.",
      {"cm1": ["L'aiguille de la boussole est aimantée.", "L'astrolabe regarde vers le ciel.", "La carte se lit sur une table."],
       "cm2": ["Deux instruments mesurent la hauteur d'un astre : lis bien la fin de chaque phrase.", "Le sablier coule pendant un temps fixe.", "Un portulan est une carte."]},
      cm1=assoc([("la boussole", "indique le nord"), ("l'astrolabe", "mesure la hauteur du Soleil ou d'une étoile"), ("la carte marine", "montre les côtes et les ports")]),
      cm2=assoc([("la boussole", "indique le nord grâce à une aiguille aimantée"), ("l'astrolabe", "mesure la hauteur du Soleil à midi"),
                 ("le quadrant", "mesure la hauteur de l'étoile Polaire"), ("le portulan", "dessine les côtes, les ports et les directions"),
                 ("le sablier", "mesure le temps passé")]),
      lecon="techniques"),
    E("2-2", "Le plan de la caravelle", "plan",
      {"cm1": "Rosa montre le plan de la caravelle. Les noms ont été arrachés par le vent. Place chaque étiquette sur son repère." + schema_caravelle(3, "Le plan de la caravelle"),
       "cm2": "Rosa montre le plan de la caravelle. Place chaque étiquette sur son repère. Attention : il y a des étiquettes en trop." + schema_caravelle(5, "Le plan de la caravelle")},
      BO + " ; " + HERO_COLOMB + " ; " + MARINE,
      "Le repère 1 est une voile triangulaire, appelée voile latine : elle permet d'avancer même quand le vent n'est pas dans le dos. Le repère 2 est un mât et le repère 3 le gouvernail, à l'arrière. En CM2 : le repère 2 est une voile carrée, le repère 3 le gouvernail d'étambot, le repère 4 le château arrière et le repère 5 la coque.",
      {"cm1": ["La voile du repère 1 a trois côtés.", "Le mât est le grand poteau qui tient les voiles.", "Le gouvernail est à l'arrière, dans l'eau."],
       "cm2": ["Compte les côtés de chaque voile.", "Le château arrière est la partie surélevée à l'arrière du navire.", "La coque est le corps du navire, qui flotte."]},
      cm1={"titre": "Le plan de la caravelle", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "voile triangulaire"}, {"libelle": "Repère 2", "reponse": "mât"}, {"libelle": "Repère 3", "reponse": "gouvernail"}],
           "etiquettes": ["voile triangulaire", "mât", "gouvernail"]},
      cm2={"titre": "Le plan de la caravelle", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "voile latine"}, {"libelle": "Repère 2", "reponse": "voile carrée"}, {"libelle": "Repère 3", "reponse": "gouvernail d'étambot"},
                     {"libelle": "Repère 4", "reponse": "château arrière"}, {"libelle": "Repère 5", "reponse": "coque"}],
           "etiquettes": ["voile latine", "voile carrée", "gouvernail d'étambot", "château arrière", "coque", "rame", "moteur"]},
      lecon="techniques"),
    E("2-3", "Les questions de la cartographe", "qcm",
      {"cm1": "Avant de lever l'ancre, Rosa vérifie que l'équipage a compris. Réponds à chaque question.",
       "cm2": "Avant de lever l'ancre, Rosa interroge l'équipage. Réponds à chaque question."},
      BO + " ; " + HERO_COLOMB + " ; " + MARINE,
      "Une caravelle est un navire léger, d'une vingtaine de mètres, avec une vingtaine de marins. Ses voiles latines l'aident à avancer même contre le vent. La boussole a été inventée en Chine. En CM2 : la latitude est la position entre le nord et le sud ; ce sont les Portugais qui ont mis au point la caravelle au XVe siècle.",
      {"cm1": ["Une caravelle est un petit navire.", "Les voiles triangulaires aident quand le vent n'est pas dans le dos.", "La boussole vient d'Asie."],
       "cm2": ["La latitude se lit du nord au sud.", "La caravelle naît au Portugal.", "Une vingtaine de mètres, c'est la longueur d'une piscine de quartier."]},
      cm1=qcm([("Une caravelle est...", ["un navire léger à voiles", "un grand navire à rames", "un bateau à moteur"], 0, "Un navire léger d'une vingtaine de mètres."),
               ("À quoi servent les voiles triangulaires ?", ["à décorer le navire", "à avancer même quand le vent n'est pas dans le dos", "à pêcher"], 1, "Ce sont les voiles latines."),
               ("Où la boussole a-t-elle été inventée ?", ["en France", "en Amérique", "en Chine"], 2, "Elle est arrivée ensuite en Europe.")]),
      cm2=qcm([("Quel pays a mis au point la caravelle au XVe siècle ?", ["l'Angleterre", "le Portugal", "la France"], 1, "Les Portugais l'ont mise au point pour explorer."),
               ("La latitude, c'est...", ["la position entre le nord et le sud", "la vitesse du navire", "la profondeur de la mer"], 0, "On la trouve en mesurant la hauteur d'un astre."),
               ("Quel instrument donne le nord ?", ["le sablier", "l'astrolabe", "la boussole"], 2, "Grâce à son aiguille aimantée."),
               ("Combien de marins embarque environ une caravelle ?", ["une vingtaine", "deux cents", "trois"], 0, "Une vingtaine d'hommes.")]),
      lecon="techniques"),
    E("2-4", "Faire le point à midi", "ordre",
      "Rosa explique comment le pilote trouve sa position. Remets les étapes dans l'ordre.",
      BO + " ; " + MARINE,
      "À midi, quand le Soleil est au plus haut, le pilote vise le Soleil avec l'astrolabe. Il lit l'angle sur le cercle gradué. Il cherche dans ses tables la latitude qui correspond à cet angle et à la date. Il reporte enfin cette latitude sur la carte marine pour savoir où se trouve le navire.",
      {"cm2": ["Tout commence par une observation du ciel.", "On mesure avant de calculer.", "La carte vient en dernier."]},
      commun=ordre(["Attendre midi, quand le Soleil est au plus haut.", "Viser le Soleil avec l'astrolabe.", "Lire l'angle sur le cercle gradué.",
                    "Chercher la latitude dans les tables de calcul.", "Reporter la latitude sur la carte marine."]),
      lecon="techniques", cm2_seul=True),
]})

# =================================================================== SALLE 3 — la chambre des cartes (capitaine Bastien)
S.append({"num": 3, "titre": "La chambre des cartes — Les grands voyages", "enigmes": [
    E("3-1", "La frise des voyages", "ordre",
      {"cm1": "Le capitaine Bastien a accroché les pages du journal sur une corde, mais elles sont mélangées. Range les voyages du plus ancien au plus récent. La date est écrite sous chaque carte.",
       "cm2": "Le capitaine Bastien a mélangé les pages de son journal. Range les voyages du plus ancien au plus récent. Les dates ne sont pas écrites."},
      BO + " ; " + HERO_GAMA + " ; " + NATGEO + " ; " + HERO_CARTIER,
      "Le premier voyage est celui de Christophe Colomb, arrivé aux Antilles en 1492. Vasco de Gama arrive en Inde en 1498. L'expédition de Magellan part en 1519 et revient avec Elcano en 1522. Jacques Cartier arrive au Canada en 1534. En CM2, on ajoute le Portugais Cabral, arrivé au Brésil en 1500.",
      {"cm1": ["Lis les dates sous les cartes.", "La plus petite date est la plus ancienne.", "1519 vient avant 1534."],
       "cm2": ["Colomb est le premier, à la fin du XVe siècle.", "Le Brésil est atteint juste après l'Inde.", "Cartier est le seul Français : il vient en dernier."]},
      cm1=ordre([("Christophe Colomb arrive aux Antilles.", "1492"), ("Vasco de Gama arrive en Inde.", "1498"),
                 ("L'expédition de Magellan et Elcano fait le tour du monde.", "1519-1522"), ("Jacques Cartier arrive au Canada.", "1534")]),
      cm2=ordre(["Christophe Colomb traverse l'Atlantique et arrive aux Antilles.", "Vasco de Gama contourne l'Afrique et arrive à Calicut, en Inde.",
                 "Le Portugais Cabral arrive au Brésil.", "L'expédition de Magellan quitte l'Espagne.",
                 "Elcano ramène la Victoria en Espagne.", "Jacques Cartier plante une croix à Gaspé."]),
      lecon="voyages"),
    E("3-2", "Qui est allé où ?", "association",
      {"cm1": "Le capitaine Bastien a écrit le nom des explorateurs sur des cartons. Relie chaque explorateur à son voyage.",
       "cm2": "Le capitaine Bastien relit son journal. Relie chaque explorateur à ce qu'il a fait."},
      BO + " ; " + HERO_COLOMB + " ; " + HERO_GAMA + " ; " + NATGEO + " ; " + HERO_CARTIER,
      "Christophe Colomb a traversé l'Atlantique vers l'ouest et atteint les Antilles. Vasco de Gama a fait le tour de l'Afrique pour arriver en Inde. Jacques Cartier a remonté le Saint-Laurent, au Canada. En CM2 : Magellan cherchait un passage vers l'Asie par l'ouest et a été tué aux Philippines, et Elcano a terminé le premier tour du monde.",
      {"cm1": ["Colomb part vers l'ouest.", "Vasco de Gama passe au sud de l'Afrique.", "Cartier est envoyé par le roi de France."],
       "cm2": ["Magellan ne revient pas en Espagne.", "Elcano termine le voyage commencé par Magellan.", "Cartier part de Saint-Malo."]},
      cm1=assoc([("Christophe Colomb", "traverse l'Atlantique et arrive aux Antilles"), ("Vasco de Gama", "fait le tour de l'Afrique pour aller en Inde"),
                 ("Jacques Cartier", "arrive au Canada pour le roi de France")]),
      cm2=assoc([("Christophe Colomb", "croit être arrivé en Asie, aux Indes"), ("Vasco de Gama", "ouvre la route maritime des épices"),
                 ("Fernand de Magellan", "est tué aux Philippines en 1521"), ("Juan Sebastián Elcano", "ramène la Victoria en Espagne"),
                 ("Jacques Cartier", "plante une croix à Gaspé")]),
      lecon="voyages"),
    E("3-3", "La carte des routes", "plan",
      {"cm1": "Sur la grande carte du capitaine, trois routes sont tracées, mais leurs étiquettes sont tombées. Place chaque explorateur sur le repère de sa route." + carte_routes(3, "La carte du capitaine"),
       "cm2": "Sur la grande carte du capitaine, les routes ont perdu leurs étiquettes. Place chaque étiquette sur son repère. Attention : il y a des étiquettes en trop." + carte_routes(5, "La carte du capitaine")},
      BO + " ; " + HERO_GAMA + " ; " + NATGEO + " ; " + HERO_CARTIER,
      "Le repère 1 est sur la route de Colomb, vers les Antilles. Le repère 2 est sur la route de Vasco de Gama, qui contourne l'Afrique vers l'Inde. Le repère 3 est sur la route de Cartier, au nord, vers le Canada. En CM2, le repère 4 est sur la route de Magellan et Elcano, au sud de l'Amérique, et le repère 5 est le cap de Bonne-Espérance, au sud de l'Afrique.",
      {"cm1": ["La route de Colomb va tout droit vers l'ouest.", "La route qui fait le tour de l'Afrique est celle de Vasco de Gama.", "La route du nord mène au Canada."],
       "cm2": ["La route en pointillés passe au sud de l'Amérique.", "Le repère 5 est une pointe de terre.", "Le détroit de Gibraltar n'est pas sur un repère."]},
      cm1={"titre": "La carte du capitaine", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "Colomb"}, {"libelle": "Repère 2", "reponse": "Vasco de Gama"}, {"libelle": "Repère 3", "reponse": "Cartier"}],
           "etiquettes": ["Colomb", "Vasco de Gama", "Cartier"]},
      cm2={"titre": "La carte du capitaine", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "Colomb"}, {"libelle": "Repère 2", "reponse": "Vasco de Gama"}, {"libelle": "Repère 3", "reponse": "Cartier"},
                     {"libelle": "Repère 4", "reponse": "Magellan et Elcano"}, {"libelle": "Repère 5", "reponse": "cap de Bonne-Espérance"}],
           "etiquettes": ["Colomb", "Vasco de Gama", "Cartier", "Magellan et Elcano", "cap de Bonne-Espérance", "détroit de Gibraltar", "Marco Polo"]},
      lecon="voyages"),
    E("3-4", "La page mouillée", "trous",
      "Une page du journal a pris l'eau : des mots ont disparu. Complète le récit du premier tour du monde. Attention : il y a des étiquettes en trop.",
      BO + " ; " + NATGEO,
      "L'expédition part d'Espagne en 1519 avec cinq navires et environ 250 hommes. Magellan est tué aux Philippines en 1521. Elcano rentre en Espagne le 6 septembre 1522 sur la Victoria, avec seulement 18 hommes : c'est le premier tour du monde.",
      {"cm2": ["Le départ a lieu trois ans avant le retour.", "Il ne reste qu'un seul navire à la fin.", "Les survivants sont moins de vingt."]},
      commun={"texte": "<p>En [[1519]], Magellan quitte l'Espagne avec [[cinq]] navires et environ 250 hommes. Il est tué aux [[Philippines]] en 1521. Le 6 septembre [[1522]], Elcano rentre en Espagne sur la [[Victoria]], avec seulement [[18]] hommes.</p>",
              "etiquettes": ["1519", "cinq", "Philippines", "1522", "Victoria", "18", "1492", "Antilles", "180", "Santa Maria"]},
      lecon="voyages", cm2_seul=True),
]})

# =================================================================== SALLE 4 — le rivage (Itzel, conteuse venue de Mexico)
S.append({"num": 4, "titre": "Le rivage — Rencontres et conquêtes", "enigmes": [
    E("4-1", "Trois peuples d'Amérique", "tri",
      {"cm1": "Itzel, conteuse venue de Mexico, raconte l'Amérique d'avant l'arrivée des Européens. Range chaque carte sous le peuple qu'elle décrit.",
       "cm2": "Itzel, conteuse venue de Mexico, présente trois peuples d'Amérique vers 1500. Range chaque carte sous le bon peuple."},
      BO + " ; " + WHE_CONQ + " ; " + HERO_CARTIER,
      "Les Aztèques vivent au Mexique ; leur capitale, Tenochtitlan, est bâtie sur un lac. Les Incas vivent dans la cordillère des Andes ; leur capitale est Cuzco. Les Iroquoiens du Saint-Laurent, au Canada, cultivent le maïs et vivent dans des maisons longues. En CM2 : Hernán Cortés prend Tenochtitlan en 1521 ; Francisco Pizarro capture l'empereur inca Atahualpa en 1532 ; Cartier rencontre le chef iroquoien Donnacona en 1534.",
      {"cm1": ["Tenochtitlan est la ville des Aztèques.", "Les Andes sont de hautes montagnes d'Amérique du Sud.", "Le Saint-Laurent est un fleuve du Canada."],
       "cm2": ["Cortés conquiert le Mexique.", "Atahualpa est un empereur des Andes.", "Donnacona vit près du Saint-Laurent."]},
      cm1=tri([("azteques", "Aztèques"), ("incas", "Incas"), ("iroquoiens", "Iroquoiens")],
              [("une capitale bâtie sur un lac", "azteques"), ("le Mexique", "azteques"), ("la cordillère des Andes", "incas"), ("la capitale Cuzco", "incas"),
               ("des maisons longues", "iroquoiens"), ("le fleuve Saint-Laurent", "iroquoiens")]),
      cm2=tri([("azteques", "Aztèques"), ("incas", "Incas"), ("iroquoiens", "Iroquoiens")],
              [("Tenochtitlan, bâtie sur un lac", "azteques"), ("prise par Cortés et ses alliés en 1521", "azteques"), ("Cuzco, dans les Andes", "incas"),
               ("un immense réseau de routes", "incas"), ("l'empereur Atahualpa, capturé en 1532", "incas"), ("des villages de maisons longues", "iroquoiens"),
               ("le chef Donnacona, rencontré par Cartier", "iroquoiens")]),
      lecon="rencontres"),
    E("4-2", "Le récit d'Itzel", "qcm",
      {"cm1": "Itzel lit un texte adapté pour les élèves : « Vers 1500, des millions de personnes vivent en Amérique. Les Espagnols arrivent avec des chevaux et des armes à feu. Ils apportent aussi, sans le savoir, des maladies comme la variole. Beaucoup d'Amérindiens en meurent. » Réponds aux questions.",
       "cm2": "Itzel lit un texte adapté pour les élèves : « Tenochtitlan, bâtie sur un lac, compte des dizaines de milliers d'habitants. En 1521, Cortés et ses alliés amérindiens la prennent. Les chevaux, l'acier et les armes à feu sont inconnus des Aztèques. La variole, venue d'Europe, tue un très grand nombre d'habitants. » Réponds aux questions."},
      BO + " ; " + WHE_CONQ,
      "D'après le texte, l'Amérique était peuplée de millions de personnes : elle n'était pas vide. Les Espagnols avaient des chevaux et des armes à feu, que les Amérindiens ne connaissaient pas. Les maladies comme la variole ont tué un très grand nombre d'Amérindiens. En CM2 : Cortés n'était pas seul, il avait des alliés amérindiens, ennemis des Aztèques.",
      {"cm1": ["Relis la première phrase du texte.", "Un cheval était un animal inconnu en Amérique à cette époque.", "La variole est une maladie."],
       "cm2": ["Relis la phrase qui donne l'année.", "Cortés n'est pas seul : relis qui l'accompagne.", "La variole vient d'Europe."]},
      cm1=qcm([("Vers 1500, l'Amérique est...", ["vide", "peuplée de millions de personnes", "habitée seulement par des Européens"], 1, "Des millions de personnes y vivent."),
               ("Qu'apportent les Espagnols, sans le savoir ?", ["des maladies comme la variole", "des remèdes", "des épices"], 0, "Les Amérindiens n'étaient pas protégés contre ces maladies."),
               ("Quels animaux les Espagnols amènent-ils ?", ["des lamas", "des dindons", "des chevaux"], 2, "Le cheval était inconnu en Amérique à cette époque.")]),
      cm2=qcm([("En quelle année Tenochtitlan est-elle prise ?", ["1492", "1521", "1608"], 1, "En 1521."),
               ("Qui aide Cortés à prendre la ville ?", ["des alliés amérindiens, ennemis des Aztèques", "l'armée du roi de France", "les Incas"], 0, "Plusieurs peuples se sont alliés aux Espagnols."),
               ("Qu'est-ce qui est inconnu des Aztèques ?", ["le maïs", "les canaux", "les chevaux et les armes à feu"], 2, "Ils arrivent avec les Espagnols."),
               ("Quelle est la principale cause de mort des Amérindiens ?", ["les maladies venues d'Europe", "le froid", "la famine seulement"], 0, "La variole notamment.")]),
      lecon="rencontres"),
    E("4-3", "Ce qu'il faut dire juste", "vraifaux",
      {"cm1": "Itzel corrige les phrases écrites sur le sable. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Itzel corrige les phrases écrites sur le sable. Pour chaque phrase, choisis vrai ou faux. Attention aux mots."},
      BO + " ; " + WHE_CONQ + " ; " + LUMNI,
      "L'Amérique était habitée depuis des milliers d'années : on dit aujourd'hui « arrivée des Européens ». Le maïs et la tomate viennent d'Amérique. Les chevaux n'existaient pas en Amérique à cette époque : les Espagnols les ont amenés. En CM2 : les Européens donnent des noms nouveaux à des lieux qui en avaient déjà, et le cacao, le chocolat des Aztèques, arrive en Europe.",
      {"cm1": ["Des peuples vivaient en Amérique bien avant Colomb.", "Le maïs pousse en Amérique depuis très longtemps.", "Les chevaux sont arrivés par bateau."],
       "cm2": ["Les lieux d'Amérique avaient déjà des noms.", "Le cacao vient d'Amérique.", "Le blé est venu d'Europe."]},
      cm1=vf([("L'Amérique était vide quand les Européens sont arrivés.", False, "Elle était habitée depuis des milliers d'années."),
              ("Le maïs et la tomate viennent d'Amérique.", True, "Ils arrivent ensuite en Europe."),
              ("Les chevaux existaient déjà en Amérique vers 1500.", False, "Les Espagnols les ont amenés.")]),
      cm2=vf([("On peut dire « arrivée des Européens en Amérique » plutôt que « découverte ».", True, "Car le continent était habité."),
              ("Les lieux d'Amérique n'avaient pas de nom avant l'arrivée des Européens.", False, "Ils avaient des noms dans les langues de leurs habitants."),
              ("Le cacao est arrivé en Europe grâce aux échanges avec l'Amérique.", True, "Les Aztèques en faisaient une boisson."),
              ("Le blé poussait en Amérique avant 1492.", False, "Il est arrivé avec les Européens."),
              ("La conquête a été rapide partout, sans aucune résistance.", False, "Certains peuples ont résisté longtemps.")]),
      lecon="rencontres"),
    E("4-4", "L'intrus du panier", "intrus",
      "Itzel a rempli un panier de produits venus d'Amérique vers l'Europe. L'un d'eux n'a rien à faire là : il a fait le chemin inverse. Trouve l'intrus.",
      BO + " ; " + WHE_CONQ,
      "Le maïs, la pomme de terre, la tomate et le cacao viennent d'Amérique et ont traversé l'Atlantique vers l'Europe. Le blé est l'intrus : il a fait le chemin inverse, de l'Europe vers l'Amérique, comme le cheval et la vache.",
      {"cm2": ["Cherche une plante cultivée en Europe depuis très longtemps.", "Avec quoi fait-on le pain en France ?", "Le cacao, lui, vient des Aztèques."]},
      commun=intrus([("le maïs", False), ("la pomme de terre", False), ("la tomate", False), ("le cacao", False), ("le blé", True)]),
      lecon="rencontres", cm2_seul=True),
]})

# =================================================================== SALLE 5 — le cabinet du cartographe (Simon, le mousse)
S.append({"num": 5, "titre": "Le cabinet du cartographe — Les premiers empires coloniaux", "enigmes": [
    E("5-1", "La carte du partage", "plan",
      {"cm1": "Simon, le mousse, a retrouvé dans le cabinet une carte du partage du monde. Les noms ont disparu. Place chaque étiquette sur son repère." + carte_tordesillas(3, "La carte du partage (1494)"),
       "cm2": "Simon a retrouvé la carte du partage du monde. Place chaque étiquette sur son repère. Attention : il y a des étiquettes en trop." + carte_tordesillas(5, "La carte du partage (1494)")},
      BO + " ; " + WHE_TORDE,
      "Le repère 1 est la ligne de Tordesillas, tracée en 1494. Le repère 2, à l'ouest de la ligne, montre les terres attribuées à l'Espagne ; le repère 3, à l'est, celles attribuées au Portugal. En CM2, le repère 4 est le Brésil, qui dépasse la ligne vers l'est et devient portugais ; le repère 5 est la Nouvelle-France, où la France s'installe malgré le partage.",
      {"cm1": ["Le repère 1 est sur la ligne en pointillés.", "L'Espagne reçoit l'ouest, à gauche.", "Le Portugal reçoit l'est, à droite."],
       "cm2": ["Le Brésil est la partie de l'Amérique du Sud du côté est de la ligne.", "La Nouvelle-France est au nord de l'Amérique.", "L'Angleterre n'a pas de repère ici."]},
      cm1={"titre": "La carte du partage", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "ligne de partage"}, {"libelle": "Repère 2", "reponse": "terres pour l'Espagne"}, {"libelle": "Repère 3", "reponse": "terres pour le Portugal"}],
           "etiquettes": ["ligne de partage", "terres pour l'Espagne", "terres pour le Portugal"]},
      cm2={"titre": "La carte du partage", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "ligne de Tordesillas"}, {"libelle": "Repère 2", "reponse": "terres pour l'Espagne"}, {"libelle": "Repère 3", "reponse": "terres pour le Portugal"},
                     {"libelle": "Repère 4", "reponse": "Brésil"}, {"libelle": "Repère 5", "reponse": "Nouvelle-France"}],
           "etiquettes": ["ligne de Tordesillas", "terres pour l'Espagne", "terres pour le Portugal", "Brésil", "Nouvelle-France", "Virginie anglaise", "Inde"]},
      lecon="empires"),
    E("5-2", "Les pavillons des colonies", "association",
      {"cm1": "Simon range les pavillons du cabinet. Relie chaque colonie au pays européen qui la domine.",
       "cm2": "Simon range les pavillons et les fiches des colonies. Relie chaque colonie à ce qui la décrit."},
      BO + " ; " + WHE_TORDE + " ; " + BANQ,
      "Le Mexique et le Pérou sont dominés par l'Espagne. Le Brésil est une colonie du Portugal. La Nouvelle-France, autour de Québec, est une colonie de la France. En CM2 : Québec est fondée par Champlain en 1608 ; la Virginie, colonie anglaise, en 1607 ; le Brésil cultive la canne à sucre ; l'Espagne exploite les mines d'argent.",
      {"cm1": ["Cortés et Pizarro sont espagnols.", "Cabral est portugais.", "Cartier est envoyé par le roi de France."],
       "cm2": ["Champlain est français.", "La Virginie est sur la côte est de l'Amérique du Nord.", "La canne à sucre pousse au Brésil."]},
      cm1=assoc([("le Mexique et le Pérou", "l'Espagne"), ("le Brésil", "le Portugal"), ("la Nouvelle-France", "la France")]),
      cm2=assoc([("la Nouvelle-Espagne (Mexique)", "colonie espagnole, riche en mines d'argent"), ("le Brésil", "colonie portugaise de plantations de sucre"),
                 ("Québec", "fondée par Champlain en 1608"), ("la Virginie", "première colonie anglaise durable, en 1607"),
                 ("la Nouvelle-France", "commerce des fourrures avec les Amérindiens")]),
      lecon="empires"),
    E("5-3", "Le cadenas du coffre de bord", "code",
      {"cm1": "Le coffre de bord ne s'ouvre qu'en reliant chaque grand voyage à sa date. Écris l'année de chaque voyage.",
       "cm2": "Le coffre de bord ne s'ouvre qu'en reliant chaque grand événement à sa date. Écris l'année de chacun."},
      BO + " ; " + HERO_GAMA + " ; " + NATGEO + " ; " + HERO_CARTIER + " ; " + WHE_TORDE,
      "Colomb arrive aux Antilles en 1492, Vasco de Gama en Inde en 1498 et Cartier au Canada en 1534. En CM2, il faut aussi 1494, l'année du traité de Tordesillas, et 1522, l'année du retour d'Elcano.",
      {"cm1": ["Relis la frise du capitaine.", "Colomb : fin du XVe siècle.", "Cartier : XVIe siècle."],
       "cm2": ["Le traité est signé deux ans après le voyage de Colomb.", "Le tour du monde dure de 1519 à 1522.", "Cartier arrive à Gaspé en juillet."]},
      cm1=code([("Arrivée de Colomb aux Antilles", "1492"), ("Arrivée de Vasco de Gama en Inde", "1498"), ("Arrivée de Cartier au Canada", "1534")]),
      cm2=code([("Arrivée de Colomb aux Antilles", "1492"), ("Traité de Tordesillas", "1494"), ("Arrivée de Vasco de Gama en Inde", "1498"),
                ("Retour d'Elcano en Espagne", "1522"), ("Arrivée de Cartier à Gaspé", "1534")]),
      lecon="empires"),
    E("5-4", "Les richesses des colonies", "tri",
      "Simon trie les registres de marchandises des colonies. Range chaque carte sous le pays qui l'exploite.",
      BO + " ; " + BANQ + " ; " + WHE_CONQ,
      "L'Espagne exploite l'or et surtout l'argent des mines du Mexique et du Pérou. Le Portugal crée au Brésil des plantations de canne à sucre. La France fait en Nouvelle-France le commerce des fourrures avec les Amérindiens. Dans les mines et les plantations, les colons font travailler de force des Amérindiens, puis des Africains réduits en esclavage : c'est le lien avec le jeu « Les Archives du port ».",
      {"cm2": ["Les mines d'argent sont au Mexique et au Pérou.", "Le sucre vient du Brésil.", "Les fourrures viennent du nord de l'Amérique."]},
      commun=tri([("espagne", "Espagne"), ("portugal", "Portugal"), ("france", "France")],
                 [("l'argent des mines du Pérou", "espagne"), ("l'or du Mexique", "espagne"), ("le sucre des plantations du Brésil", "portugal"),
                  ("le bois brésil, qui donne une teinture rouge", "portugal"), ("les fourrures de castor", "france"), ("la pêche à la morue près de Terre-Neuve", "france")]),
      lecon="empires", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "La Caravelle du capitaine", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": " ; ".join([BO, BNF, MARINE, HERO_COLOMB, HERO_GAMA, HERO_CARTIER, NATGEO, WHE_TORDE, WHE_CONQ, BANQ, LUMNI]) + ". Détail : README.md, section Sources.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-1\",\"legende\":\"…\",\"source\":\"…\"}. Les cartes et le plan de la caravelle sont dessinés en SVG par script : ne jamais les remplacer par des images générées par IA."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
