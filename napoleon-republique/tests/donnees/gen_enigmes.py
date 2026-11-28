# -*- coding: utf-8 -*-
"""Génère napoleon-republique/assets/data/enigmes.json (Le Testament de l'Empereur). Lancer : python gen_enigmes.py <dossier data>
Bilan nuancé de l'Empire (réformes, mais guerres, autoritarisme, rétablissement de l'esclavage en 1802) ; aucune scène de combat ;
personnages inventés ; les personnes réelles ne parlent jamais. Salle 5 : symboles, lieux et rites de la République ; les lois
protectrices des droits sont traitées dans les jeux « Le Secret de la Déclaration » et « Le Sceau de la République » (renvoi)."""
import json, os, sys
from schemas import carte_europe, sacre, place

BO = "Programme d'histoire du cycle 3 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026), le temps de la Révolution et de l'Empire (niveau à confirmer, cf. A-VERIFIER.md) ; progression de l'enseignant : thème 4, année B, période 4"
FN = "Fondation Napoléon, napoleon.org (chronologies, dossiers « Masses de granit » et « Le Sacre »)"
MA = "Musée de l'Armée, Hôtel national des Invalides"
LOUVRE = "Musée du Louvre, Jacques-Louis David, « Sacre de l'empereur Napoléon Ier et couronnement de l'impératrice Joséphine »"
BDF = "Banque de France, « Histoire de la Banque de France »"
ELY = "Présidence de la République (elysee.fr), « La Marseillaise de Rouget de Lisle » et « Les symboles de la République »"
CONST = "Constitution du 4 octobre 1958, article 2 (Légifrance) ; vie-publique.fr, « Quels sont les symboles de la Ve République ? »"
HPI = "Histoire par l'image (Réunion des musées nationaux) et Eduscol, ressources sur le Consulat et l'Empire"

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



S = []
# =================================================================== SALLE 1 — Les Tuileries, 1800 (Antoine)
S.append({"num": 1, "titre": "Salle n°1, 1793-1802 — Du général au Premier consul", "enigmes": [
    E("1-1", "La frise du grenadier", "ordre",
      {"cm1": "Antoine a noté sur un carnet les grandes étapes de la vie du général Bonaparte, mais les pages sont mélangées. Remets-les dans l'ordre, de la plus ancienne à la plus récente.",
       "cm2": "Antoine a fabriqué une frise de la vie de Bonaparte, de sa naissance à sa prise de pouvoir. Remets les événements dans l'ordre chronologique."},
      BO + " ; " + FN + " ; " + HPI,
      "Bonaparte aide d'abord à reprendre Toulon (1793), puis il commande l'armée d'Italie (1796-1797), part en Égypte (1798) et prend le pouvoir à Paris par un coup d'État (1799). En CM2 : il est né le 15 août 1769 à Ajaccio ; Toulon est repris en décembre 1793 ; il gagne la bataille des Pyramides le 21 juillet 1798 ; le coup d'État a lieu le 18 brumaire an VIII, c'est-à-dire le 9 novembre 1799.",
      {"cm1": ["Toulon est la première victoire du jeune Bonaparte.", "L'Italie avant l'Égypte.", "Le coup d'État est en 1799, la dernière date."],
       "cm2": ["La naissance est la date la plus ancienne.", "1796 avant 1798.", "Brumaire an VIII = novembre 1799."]},
      cm1=ordre([("Bonaparte aide à reprendre le port de Toulon", "1793"), ("il commande l'armée d'Italie", "1796-1797"),
                 ("il part en Égypte", "1798"), ("il prend le pouvoir à Paris", "1799")]),
      cm2=ordre([("naissance de Napoléon Bonaparte à Ajaccio", "15 août 1769"), ("reprise du port de Toulon", "décembre 1793"),
                 ("victoires d'Arcole et de Rivoli en Italie", "1796-1797"), ("bataille des Pyramides en Égypte", "21 juillet 1798"),
                 ("coup d'État du 18 brumaire", "9 novembre 1799")]),
      lecon="general"),
    E("1-2", "Les souvenirs de campagne", "association",
      {"cm1": "Dans sa giberne, Antoine garde un souvenir de chaque lieu où il a suivi Bonaparte. Relie chaque lieu à ce qui s'y est passé.",
       "cm2": "Antoine explique les mots nouveaux de l'époque à un jeune soldat. Relie chaque mot à sa définition."},
      BO + " ; " + FN,
      "À Toulon, Bonaparte aide à reprendre le port aux Anglais ; en Italie, il remporte des victoires contre l'Autriche ; en Égypte, il est accompagné de savants qui étudient le pays ; à Paris, il prend le pouvoir. En CM2 : un coup d'État est une prise du pouvoir par la force ; le Consulat est le régime né en 1799 ; le Premier consul a presque tous les pouvoirs ; le Concordat est l'accord de 1801 avec le pape ; un plébiscite est un vote où l'on répond par oui ou par non.",
      {"cm1": ["Toulon est un port.", "Les savants étudient les pyramides.", "Le pouvoir se trouve dans la capitale."],
       "cm2": ["« Consul » est un mot de la Rome antique.", "Le Concordat concerne l'Église.", "Un coup d'État se fait par la force."]},
      cm1=assoc([("Toulon", "un port repris aux Anglais"), ("l'Italie", "des victoires contre l'Autriche"),
                 ("l'Égypte", "une expédition avec des savants"), ("Paris", "la prise du pouvoir")]),
      cm2=assoc([("un coup d'État", "une prise du pouvoir par la force"), ("le Consulat", "le régime qui commence en 1799"),
                 ("le Premier consul", "celui des trois consuls qui a presque tous les pouvoirs"), ("le Concordat", "l'accord signé avec le pape en 1801"),
                 ("un plébiscite", "un vote où l'on répond par oui ou par non")]),
      lecon="general"),
    E("1-3", "Les rumeurs du palais", "vraifaux",
      {"cm1": "Dans les couloirs du palais des Tuileries, on entend beaucoup de choses sur le Premier consul. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Antoine trie les rumeurs qui circulent au palais des Tuileries en 1802. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + FN,
      "Bonaparte est né en Corse, à Ajaccio, en 1769. Il prend le pouvoir par un coup d'État en 1799 : ce n'est pas une élection. Sous le Consulat, trois consuls gouvernent, mais le Premier consul a presque tous les pouvoirs. En CM2 : il devient général à 24 ans après Toulon ; il signe le Concordat avec le pape en 1801 et il est nommé consul à vie en 1802 ; la pierre de Rosette est découverte en Égypte en 1799.",
      {"cm1": ["Ajaccio est en Corse.", "Un coup d'État n'est pas une élection.", "Le Premier consul décide presque de tout."],
       "cm2": ["Après Toulon, il devient général.", "Le Concordat est signé avec le pape.", "Consul à vie : en 1802."]},
      cm1=vf([("Napoléon Bonaparte est né en Corse.", True, "À Ajaccio, en 1769."),
              ("Bonaparte a été élu par tous les Français en 1799.", False, "Il prend le pouvoir par un coup d'État."),
              ("Sous le Consulat, le Premier consul a presque tous les pouvoirs.", True, "Les deux autres consuls ne font que donner leur avis.")]),
      cm2=vf([("Après le siège de Toulon, Bonaparte est nommé général à 24 ans.", True, "En décembre 1793."),
              ("Le coup d'État du 18 brumaire a lieu le 9 novembre 1799.", True, "C'est la même date dans deux calendriers."),
              ("En Égypte, Bonaparte voyage seulement avec des soldats.", False, "Des savants l'accompagnent ; ils étudient le pays."),
              ("En 1801, Bonaparte signe le Concordat avec le pape.", True, "Il fait la paix avec l'Église catholique."),
              ("En 1802, Bonaparte devient roi de France.", False, "Il est nommé consul à vie ; il deviendra empereur en 1804.")]),
      lecon="general"),
    E("1-4", "L'interrogatoire du Premier consul", "qcm",
      "Antoine doit répondre aux questions d'un officier avant de devenir grenadier de la garde. Aide-le.",
      BO + " ; " + FN + " ; " + HPI,
      "Bonaparte fait raconter ses victoires d'Italie dans des journaux et des tableaux : il devient très populaire. Il prend le pouvoir le 18 brumaire an VIII (9 novembre 1799) par un coup d'État. Le Consulat compte trois consuls, mais le Premier consul a presque tous les pouvoirs. La pierre de Rosette, découverte en 1799, aidera plus tard à lire les hiéroglyphes.",
      {"cm2": ["Les tableaux et les journaux font sa gloire.", "Trois consuls, un seul vrai chef.", "La pierre de Rosette sert à lire une écriture."]},
      commun=qcm([("Comment Bonaparte devient-il célèbre en France ?", ["il gagne une élection", "il fait raconter ses victoires dans des journaux et des tableaux", "il écrit des romans", "il devient pape"], 1, "Ses victoires d'Italie sont racontées partout."),
                  ("Combien y a-t-il de consuls sous le Consulat ?", ["un", "deux", "trois", "cinq"], 2, "Mais le Premier consul a presque tous les pouvoirs."),
                  ("Quel jour correspond au 18 brumaire an VIII ?", ["le 14 juillet 1789", "le 9 novembre 1799", "le 2 décembre 1804", "le 18 juin 1815"], 1, "Le calendrier républicain compte à partir de 1792."),
                  ("À quoi a servi plus tard la pierre de Rosette ?", ["à construire les pyramides", "à lire les hiéroglyphes", "à fabriquer des canons", "à couronner l'empereur"], 1, "Elle porte le même texte en trois écritures.")]),
      lecon="general", cm2_seul=True),
]})

# =================================================================== SALLE 2 — Notre-Dame, 2 décembre 1804 (Rose)
S.append({"num": 2, "titre": "Salle n°2, 1804 — Le sacre à Notre-Dame", "enigmes": [
    E("2-1", "Le registre de l'atelier", "trous",
      {"cm1": "Rose, la brodeuse, a taché d'encre son registre. Complète le texte avec les bonnes étiquettes.",
       "cm2": "Rose a recopié dans son registre les nouvelles de l'année 1804, mais des mots se sont effacés. Complète le texte."},
      BO + " ; " + FN,
      "En 1804, Bonaparte devient empereur des Français sous le nom de Napoléon Ier. Il est sacré dans la cathédrale Notre-Dame de Paris, en présence du pape. En CM2 : il est proclamé empereur le 18 mai 1804 et les Français approuvent ce changement par un plébiscite ; le sacre a lieu le 2 décembre 1804, en présence du pape Pie VII ; l'Empire est héréditaire.",
      {"cm1": ["Napoléon devient empereur.", "La cérémonie a lieu dans une cathédrale.", "Le chef de l'Église catholique est le pape."],
       "cm2": ["Mai avant décembre.", "Un vote par oui ou par non : un plébiscite.", "Héréditaire : le pouvoir passe au fils."]},
      cm1=trous("En 1804, Bonaparte devient [[empereur]] des Français. Il est sacré dans la cathédrale [[Notre-Dame]] de Paris, en présence du [[pape]].",
                ["empereur", "Notre-Dame", "pape", "roi", "Versailles"]),
      cm2=trous("Le 18 [[mai]] 1804, Bonaparte est proclamé empereur sous le nom de [[Napoléon Ier]]. Les Français l'approuvent par un [[plébiscite]]. Le 2 [[décembre]] 1804, il est sacré à Notre-Dame en présence du pape [[Pie VII]]. L'Empire est [[héréditaire]].",
                ["mai", "Napoléon Ier", "plébiscite", "décembre", "Pie VII", "héréditaire", "Louis XVI", "juillet", "élu"]),
      lecon="sacre"),
    E("2-2", "Le grand tableau", "plan",
      {"cm1": "Rose a assisté au sacre. Elle te montre un schéma du grand tableau de David. Place chaque nom sur son repère : clique sur une étiquette, puis sur la case du repère." + sacre(3),
       "cm2": "Rose te montre un schéma du tableau de David. Place chaque nom sur son repère. Attention : il y a des étiquettes en trop." + sacre(5)},
      BO + " ; " + LOUVRE + " ; " + FN,
      "Au centre, debout, Napoléon (repère 1) lève une couronne ; à genoux devant lui, Joséphine (repère 2) va être couronnée impératrice ; assis derrière, le pape Pie VII (repère 3) bénit la cérémonie. En CM2 : le repère 4 est la couronne de l'impératrice, que Napoléon tient dans ses mains ; le repère 5 est la tribune où David a peint la famille de l'empereur. David a choisi de peindre le moment où Napoléon couronne Joséphine. Louis XVI et Marianne ne sont pas dans le tableau.",
      {"cm1": ["Celui qui tient la couronne est debout.", "L'impératrice est à genoux.", "Le pape est assis, en blanc."],
       "cm2": ["La couronne est levée au-dessus de Joséphine.", "La tribune est en haut, au fond.", "Louis XVI est mort en 1793."]},
      cm1=plan("Le tableau du Sacre", 3, ["Napoléon", "Joséphine", "le pape Pie VII"], ["Napoléon", "Joséphine", "le pape Pie VII"]),
      cm2=plan("Le tableau du Sacre", 2, ["Napoléon", "Joséphine", "le pape Pie VII", "la couronne de l'impératrice", "la tribune de la famille"],
               ["Napoléon", "Joséphine", "le pape Pie VII", "la couronne de l'impératrice", "la tribune de la famille", "Louis XVI", "Marianne"]),
      lecon="sacre"),
    E("2-3", "Les motifs de la broderie", "intrus",
      {"cm1": "Rose brode les symboles de l'Empire sur un manteau. Un motif n'a rien à faire là : trouve l'intrus.",
       "cm2": "Rose prépare un carton de motifs pour la cour impériale. Un motif est le symbole d'un autre régime : trouve l'intrus."},
      BO + " ; " + FN + " ; " + LOUVRE,
      "L'aigle, les abeilles d'or et la couronne de lauriers sont des symboles de l'Empire. Le bonnet phrygien est un symbole de la Révolution et de la République : Marianne le porte. En CM2 : la fleur de lys est le symbole des rois ; Napoléon choisit les abeilles pour la remplacer.",
      {"cm1": ["L'aigle est l'emblème de l'Empire.", "Les abeilles sont brodées sur le manteau du sacre.", "Marianne porte un bonnet : quel régime ?"],
       "cm2": ["Les abeilles remplacent un ancien symbole.", "Les rois de France avaient un symbole de fleur.", "Le sceptre et la main de justice sont tenus par l'empereur."]},
      cm1=intrus([("l'aigle", False), ("les abeilles d'or", False), ("la couronne de lauriers", False), ("le bonnet phrygien", True)]),
      cm2=intrus([("l'aigle", False), ("les abeilles d'or", False), ("la couronne de lauriers d'or", False), ("le sceptre et la main de justice", False), ("la fleur de lys", True)]),
      lecon="sacre"),
    E("2-4", "Le chemin vers la couronne", "ordre",
      "Rose explique à son apprentie comment le Premier consul est devenu empereur. Remets les étapes dans l'ordre.",
      BO + " ; " + FN,
      "Bonaparte prend le pouvoir le 9 novembre 1799 (18 brumaire) ; il signe le Concordat le 15 juillet 1801 ; il est nommé consul à vie en 1802 ; il est proclamé empereur le 18 mai 1804 et sacré à Notre-Dame le 2 décembre 1804.",
      {"cm2": ["Le coup d'État est la première étape.", "Le Concordat précède le consulat à vie.", "Proclamé en mai, sacré en décembre."]},
      commun=ordre([("le coup d'État du 18 brumaire", "9 novembre 1799"), ("la signature du Concordat avec le pape", "15 juillet 1801"),
                    ("Bonaparte nommé consul à vie", "1802"), ("Bonaparte proclamé empereur", "18 mai 1804"), ("le sacre à Notre-Dame", "2 décembre 1804")]),
      lecon="sacre", cm2_seul=True),
]})

# =================================================================== SALLE 3 — le bivouac de la Grande Armée (Jeanne)
S.append({"num": 3, "titre": "Salle n°3, 1805-1821 — Les conquêtes et la chute", "enigmes": [
    E("3-1", "La carte de la cantinière", "plan",
      {"cm1": "Jeanne, la cantinière, a suivi la Grande Armée à travers l'Europe. Sur sa carte, les noms se sont effacés. Place chaque nom sur son repère." + carte_europe(3),
       "cm2": "Jeanne a marqué sur sa carte les lieux de l'épopée de l'Empire. Place chaque nom sur son repère. Attention : il y a des étiquettes en trop." + carte_europe(5)},
      BO + " ; " + MA + " ; " + FN,
      "Le repère 1 est Paris, la capitale ; le repère 2 Austerlitz, en Europe centrale, où Napoléon remporte une grande victoire en 1805 ; le repère 3 Moscou, en Russie, très loin à l'est, où il entre en 1812. En CM2 : le repère 4 est Iéna, en Allemagne (victoire contre la Prusse en 1806) ; le repère 5 est Waterloo, en Belgique, où il est battu le 18 juin 1815. Londres et Rome ne sont pas des repères numérotés.",
      {"cm1": ["Paris est en France.", "Moscou est la ville la plus à l'est.", "Austerlitz est au centre de l'Europe."],
       "cm2": ["Waterloo est en Belgique, tout près de la France.", "Iéna est entre Paris et Austerlitz.", "Londres est sur une île."]},
      cm1=plan("La carte de Jeanne", 3, ["Paris", "Austerlitz", "Moscou"], ["Paris", "Austerlitz", "Moscou"]),
      cm2=plan("La carte de Jeanne", 2, ["Paris", "Austerlitz", "Moscou", "Iéna", "Waterloo"], ["Paris", "Austerlitz", "Moscou", "Iéna", "Waterloo", "Londres", "Rome"]),
      lecon="conquetes"),
    E("3-2", "Le carnet de route", "ordre",
      {"cm1": "Jeanne a noté les grands moments de l'Empire dans son carnet, mais les pages sont mélangées. Remets-les dans l'ordre.",
       "cm2": "Jeanne a noté les victoires et les défaites de l'Empire. Remets les événements dans l'ordre chronologique."},
      BO + " ; " + MA + " ; " + FN,
      "La victoire d'Austerlitz a lieu en 1805 ; la campagne de Russie en 1812 ; la défaite de Waterloo en 1815. En CM2 : Austerlitz le 2 décembre 1805 ; Iéna le 14 octobre 1806 ; Wagram en juillet 1809 ; l'entrée dans Moscou en septembre 1812 ; la première abdication en avril 1814 ; Waterloo le 18 juin 1815.",
      {"cm1": ["Austerlitz est la plus ancienne.", "La Russie avant Waterloo.", "Waterloo est la dernière bataille."],
       "cm2": ["1805, 1806, 1809 : trois victoires.", "Moscou en 1812.", "L'abdication de 1814 précède les Cent-Jours et Waterloo."]},
      cm1=ordre([("la victoire d'Austerlitz", "1805"), ("la campagne de Russie", "1812"), ("la défaite de Waterloo", "1815")]),
      cm2=ordre([("la victoire d'Austerlitz", "2 décembre 1805"), ("la victoire d'Iéna", "14 octobre 1806"), ("la victoire de Wagram", "juillet 1809"),
                 ("l'entrée dans Moscou", "septembre 1812"), ("la première abdication", "avril 1814"), ("la défaite de Waterloo", "18 juin 1815")]),
      lecon="conquetes"),
    E("3-3", "Les questions des jeunes soldats", "qcm",
      {"cm1": "Autour du feu de camp, les jeunes soldats posent des questions à Jeanne. Aide-la à répondre.",
       "cm2": "Autour du feu de camp, Jeanne fait le bilan des années de guerre. Réponds aux questions."},
      BO + " ; " + MA + " ; " + FN,
      "La Grande Armée réunit des soldats français et des soldats venus des pays alliés ou conquis. En Russie, le froid, la faim et les combats font disparaître la plus grande partie de la Grande Armée. Battu à Waterloo, Napoléon est exilé sur l'île de Sainte-Hélène, où il meurt en 1821. En CM2 : il avait déjà été exilé une première fois sur l'île d'Elbe en 1814 ; les guerres de l'Empire ont fait des centaines de milliers de morts en France et en Europe.",
      {"cm1": ["L'hiver russe est terrible.", "Sainte-Hélène est une île.", "Une cantinière nourrit les soldats."],
       "cm2": ["Elbe est en Méditerranée.", "Les Cent-Jours : en 1815.", "Pense à toutes les victimes des guerres."]},
      cm1=qcm([("Qu'est-ce que la Grande Armée ?", ["l'armée de Napoléon", "l'armée des Anglais", "une armée de chevaliers", "la flotte du roi"], 0, "Elle réunit des soldats de toute l'Europe."),
               ("Pourquoi la campagne de Russie est-elle un désastre ?", ["à cause du froid et de la faim", "parce qu'il fait trop chaud", "parce que l'armée est restée à Paris", "parce que Napoléon a gagné"], 0, "La plus grande partie de l'armée disparaît."),
               ("Où Napoléon est-il exilé après Waterloo ?", ["à Versailles", "sur l'île de Sainte-Hélène", "à Moscou", "en Corse"], 1, "Une île au milieu de l'océan Atlantique.")]),
      cm2=qcm([("D'où viennent les soldats de la Grande Armée ?", ["seulement de Paris", "de France et des pays alliés ou conquis", "seulement de Russie", "d'Amérique"], 1, "Elle compte beaucoup de soldats étrangers."),
               ("Où Napoléon est-il exilé la première fois, en 1814 ?", ["à Sainte-Hélène", "sur l'île d'Elbe", "en Égypte", "à Londres"], 1, "Il s'en échappe en 1815."),
               ("Comment appelle-t-on son retour au pouvoir en 1815 ?", ["les Cent-Jours", "la Terreur", "le Consulat", "le Directoire"], 0, "Il reprend le pouvoir pendant environ cent jours."),
               ("Quel est le bilan humain des guerres de l'Empire ?", ["aucun mort", "quelques dizaines de morts", "des centaines de milliers de morts", "seulement des blessés anglais"], 2, "En France et dans toute l'Europe.")]),
      lecon="conquetes"),
    E("3-4", "Le cadenas de la malle", "code",
      "La malle de Jeanne est fermée par un cadenas à trois rouleaux. Sur l'étiquette, on lit : « Le jour et l'année de la dernière bataille, puis l'année où l'Empereur s'est éteint sur son île. » Trouve les trois nombres.",
      BO + " ; " + MA + " ; " + FN,
      "La dernière bataille de Napoléon est Waterloo, le 18 juin 1815 : le jour est 18 et l'année 1815. Exilé sur l'île de Sainte-Hélène, il y meurt le 5 mai 1821 : l'année est 1821.",
      {"cm2": ["La dernière bataille est Waterloo.", "Waterloo : le 18 juin 1815.", "Il meurt à Sainte-Hélène six ans plus tard."]},
      commun=code([("Jour de Waterloo", "18"), ("Année de Waterloo", "1815"), ("Année de sa mort", "1821")]),
      lecon="conquetes", cm2_seul=True),
]})

# =================================================================== SALLE 4 — le dôme des Invalides, aujourd'hui (Hugo)
S.append({"num": 4, "titre": "Salle n°4, aujourd'hui — Ce qui reste de l'Empire", "enigmes": [
    E("4-1", "Les cartels du musée", "association",
      {"cm1": "Hugo, le conservateur, prépare les étiquettes des monuments de Paris pour une exposition. Relie chaque monument à ce qu'il rappelle.",
       "cm2": "Hugo a mélangé les cartels (les étiquettes) de l'exposition « Paris impérial ». Relie chaque monument à son histoire."},
      BO + " ; " + MA + " ; " + FN,
      "L'Arc de triomphe célèbre les victoires de la Grande Armée ; la colonne Vendôme est recouverte du bronze de canons pris à Austerlitz ; le dôme des Invalides abrite le tombeau de Napoléon. En CM2 : l'Arc de triomphe, décidé en 1806, est achevé en 1836 et le Soldat inconnu y repose depuis 1921 ; les cendres de Napoléon sont ramenées de Sainte-Hélène en 1840 ; la cathédrale Notre-Dame est le lieu du sacre.",
      {"cm1": ["Un arc de triomphe célèbre des victoires.", "Une colonne de bronze.", "Un tombeau est le lieu où repose un mort."],
       "cm2": ["Le Soldat inconnu est un soldat de 1914-1918.", "Les cendres reviennent en 1840.", "Le sacre a eu lieu dans une cathédrale."]},
      cm1=assoc([("l'Arc de triomphe", "les victoires de la Grande Armée"), ("la colonne Vendôme", "le bronze des canons d'Austerlitz"),
                 ("le dôme des Invalides", "le tombeau de Napoléon")]),
      cm2=assoc([("l'Arc de triomphe de l'Étoile", "décidé en 1806, il abrite le Soldat inconnu depuis 1921"), ("la colonne Vendôme", "recouverte du bronze de canons pris à Austerlitz"),
                 ("le dôme des Invalides", "le tombeau où reposent les cendres ramenées en 1840"), ("la cathédrale Notre-Dame", "le lieu du sacre du 2 décembre 1804")]),
      lecon="heritage"),
    E("4-2", "La vitrine des créations", "intrus",
      {"cm1": "Dans la vitrine « Créé par Napoléon », un objet a été rangé par erreur. Trouve l'intrus.",
       "cm2": "Hugo vérifie la vitrine « Les masses de granit » : les institutions créées entre 1800 et 1804. Une carte n'est pas à sa place : trouve l'intruse."},
      BO + " ; " + FN + " ; " + BDF,
      "Le Code civil, les préfets, les lycées, la Banque de France et la Légion d'honneur ont été créés par Bonaparte entre 1800 et 1804 ; ils existent toujours. En CM1 : le droit de vote des femmes date de 1944, bien après l'Empire. En CM2 : l'école gratuite, laïque et obligatoire date des lois de Jules Ferry, en 1881 et 1882, sous la République.",
      {"cm1": ["Napoléon a créé des lois et des écoles.", "Les femmes votent bien plus tard.", "Cherche ce qui date du XXe siècle."],
       "cm2": ["La Banque de France date de 1800.", "La Légion d'honneur date de 1802.", "L'école obligatoire pour tous vient plus tard."]},
      cm1=intrus([("le Code civil", False), ("les lycées", False), ("la Légion d'honneur", False), ("le droit de vote des femmes", True)]),
      cm2=intrus([("la Banque de France", False), ("les préfets", False), ("la Légion d'honneur", False), ("le Code civil", False), ("l'école gratuite et obligatoire pour tous", True)]),
      lecon="heritage"),
    E("4-3", "Héritage ou part d'ombre ?", "tri",
      {"cm1": "Hugo veut une exposition honnête, qui montre tout. Range chaque carte : ce qui reste de l'Empire, ou sa part d'ombre ?",
       "cm2": "Hugo prépare deux panneaux pour l'exposition : « Un héritage durable » et « Une part d'ombre ». Range chaque carte."},
      BO + " ; " + FN + " ; " + MA,
      "Le Code civil, les préfets et les lycées existent encore aujourd'hui : c'est un héritage durable. Mais l'Empire a aussi une part d'ombre : des guerres qui font des centaines de milliers de morts, des journaux censurés, et, en 1802, le rétablissement de l'esclavage dans les colonies (il ne sera aboli définitivement qu'en 1848). En CM2 : le Code civil soumet aussi la femme mariée à l'autorité de son mari ; les opposants sont arrêtés.",
      {"cm1": ["Ce qui existe encore aujourd'hui est un héritage.", "Les guerres font beaucoup de morts.", "L'esclavage avait été aboli par la Révolution."],
       "cm2": ["Un régime autoritaire ne laisse pas critiquer.", "Le Code civil a deux faces.", "Pense à la loi de 1802."]},
      cm1=tri([("heritage", "Ce qui reste aujourd'hui"), ("ombre", "La part d'ombre")],
              [("le Code civil", "heritage"), ("les lycées", "heritage"), ("des guerres qui font beaucoup de morts", "ombre"), ("le rétablissement de l'esclavage", "ombre")]),
      cm2=tri([("heritage", "Un héritage durable"), ("ombre", "Une part d'ombre")],
              [("l'égalité de tous devant la loi dans le Code civil", "heritage"), ("les préfets dans chaque département", "heritage"), ("la Banque de France", "heritage"),
               ("le rétablissement de l'esclavage dans les colonies en 1802", "ombre"), ("la censure des journaux", "ombre"), ("la femme mariée soumise à son mari", "ombre")]),
      lecon="heritage"),
    E("4-4", "Les dates des réserves", "vraifaux",
      "Dans les réserves du musée, Hugo relit les fiches des objets. Certaines dates sont fausses. Pour chaque phrase, choisis vrai ou faux.",
      BO + " ; " + FN + " ; " + BDF,
      "La Banque de France est créée le 18 janvier 1800 et les préfets le 17 février 1800. La Légion d'honneur est créée le 19 mai 1802. Le Code civil est promulgué le 21 mars 1804, avant le sacre. Les cendres de Napoléon reviennent en France en 1840, et non en 1821, l'année de sa mort à Sainte-Hélène.",
      {"cm2": ["Les préfets et la Banque datent de 1800.", "Le Code civil est de 1804.", "Il meurt en 1821 ; ses cendres reviennent bien plus tard."]},
      commun=vf([("La Banque de France est créée le 18 janvier 1800.", True, "Sous le Consulat."),
                 ("Les préfets sont créés en 1900.", False, "Ils sont créés le 17 février 1800."),
                 ("La Légion d'honneur est créée le 19 mai 1802.", True, "Elle récompense les mérites militaires et civils."),
                 ("Le Code civil est promulgué le 21 mars 1804.", True, "Quelques mois avant le sacre."),
                 ("Les cendres de Napoléon sont ramenées aux Invalides dès 1821.", False, "Elles reviennent en 1840.")]),
      lecon="heritage", cm2_seul=True),
]})

# =================================================================== SALLE 5 — la salle des mariages de la mairie, aujourd'hui (Inès)
S.append({"num": 5, "titre": "Salle n°5, aujourd'hui — Lieux, symboles et rites de la République", "enigmes": [
    E("5-1", "Empire ou République ?", "tri",
      {"cm1": "Inès, la maire, a trouvé dans un placard de la mairie des objets de toutes les époques. Range chaque objet : symbole de l'Empire ou symbole de la République ?",
       "cm2": "Inès prépare une exposition pour la fête de l'école. Range chaque carte : symbole de l'Empire ou symbole de la République ?"},
      BO + " ; " + CONST + " ; " + ELY + " ; " + FN,
      "L'aigle, les abeilles d'or et la couronne de lauriers sont des symboles de l'Empire. Marianne, la devise « Liberté, Égalité, Fraternité » et la Marseillaise sont des symboles de la République. En CM2 : le 14 juillet, fête nationale, est aussi un symbole de la République ; le drapeau tricolore, né pendant la Révolution, a été utilisé par l'Empire comme par la République : c'est pour cela qu'il n'est pas dans ce tri.",
      {"cm1": ["L'empereur a choisi l'aigle.", "Marianne représente la République.", "La devise est écrite sur la mairie."],
       "cm2": ["Les abeilles sont brodées sur le manteau du sacre.", "La fête nationale est un symbole républicain.", "La Marseillaise est l'hymne de la République."]},
      cm1=tri([("empire", "L'Empire"), ("rep", "La République")],
              [("l'aigle", "empire"), ("les abeilles d'or", "empire"), ("Marianne", "rep"), ("la devise « Liberté, Égalité, Fraternité »", "rep")]),
      cm2=tri([("empire", "L'Empire"), ("rep", "La République")],
              [("l'aigle", "empire"), ("les abeilles d'or", "empire"), ("la couronne de lauriers", "empire"),
               ("Marianne au bonnet phrygien", "rep"), ("la Marseillaise, hymne national", "rep"), ("le 14 juillet, fête nationale", "rep")]),
      lecon="republique"),
    E("5-2", "Le livret de la mairie", "association",
      {"cm1": "Inès explique les symboles de la République aux enfants du conseil municipal des jeunes. Relie chaque symbole à sa description.",
       "cm2": "Inès rédige le livret d'accueil de la mairie. Relie chaque symbole ou chaque rite à son explication."},
      BO + " ; " + CONST + " ; " + ELY,
      "Le drapeau est bleu, blanc, rouge ; la devise est « Liberté, Égalité, Fraternité » ; Marianne est une femme qui représente la République ; la Marseillaise est l'hymne national. En CM2 : la Marseillaise est écrite par Rouget de Lisle en 1792 ; le 14 juillet rappelle la prise de la Bastille (1789) et la fête de la Fédération (1790) ; l'article 2 de la Constitution de 1958 fixe le drapeau, l'hymne et la devise ; le maire porte une écharpe tricolore pour célébrer les mariages ; le vote permet de choisir ses représentants.",
      {"cm1": ["Le drapeau a trois couleurs.", "La devise a trois mots.", "L'hymne se chante."],
       "cm2": ["Rouget de Lisle écrit un chant de guerre en 1792.", "La Bastille est prise le 14 juillet 1789.", "Le maire porte une écharpe pendant le mariage."]},
      cm1=assoc([("le drapeau", "bleu, blanc, rouge"), ("la devise", "Liberté, Égalité, Fraternité"), ("Marianne", "une femme qui représente la République"),
                 ("la Marseillaise", "l'hymne national")]),
      cm2=assoc([("la Marseillaise", "écrite par Rouget de Lisle en 1792"), ("le 14 juillet", "rappelle la prise de la Bastille et la fête de la Fédération"),
                 ("l'article 2 de la Constitution", "fixe le drapeau, l'hymne et la devise"), ("l'écharpe tricolore", "portée par le maire pour célébrer un mariage"),
                 ("le vote", "permet aux citoyens de choisir leurs représentants")]),
      lecon="republique"),
    E("5-3", "Le plan de la place", "plan",
      {"cm1": "Inès a dessiné la place de la commune pour les nouveaux habitants, mais les noms se sont effacés. Place chaque nom sur son repère." + place(3),
       "cm2": "Inès a dessiné la place de la commune. Place chaque nom sur son repère. Attention : il y a des étiquettes en trop." + place(5)},
      BO + " ; " + CONST,
      "Le repère 1 est la mairie, où l'on se marie et où l'on vote ; le repère 2 l'école de la République ; le repère 3 le monument aux morts, où ont lieu les cérémonies du 8 Mai et du 11 Novembre. En CM2 : le repère 4 est la devise, inscrite au fronton de la mairie, et le repère 5 le drapeau tricolore. L'aigle et la couronne sont des symboles de l'Empire : ils ne sont pas sur la place.",
      {"cm1": ["La mairie est le plus grand bâtiment, au centre.", "L'école est à droite.", "Le monument aux morts est une stèle de pierre."],
       "cm2": ["La devise est écrite en haut de la façade.", "Le drapeau flotte sur le toit.", "Deux étiquettes viennent de l'Empire."]},
      cm1=plan("La place de la commune", 3, ["la mairie", "l'école", "le monument aux morts"], ["la mairie", "l'école", "le monument aux morts"]),
      cm2=plan("La place de la commune", 2, ["la mairie", "l'école", "le monument aux morts", "la devise au fronton de la mairie", "le drapeau tricolore"],
               ["la mairie", "l'école", "le monument aux morts", "la devise au fronton de la mairie", "le drapeau tricolore", "l'aigle impérial", "la couronne de lauriers"]),
      lecon="republique"),
    E("5-4", "Le coffre du testament", "code",
      "Le coffre du testament s'ouvre avec trois nombres. Inès a laissé un indice : « Le numéro de l'article de la Constitution qui fixe nos symboles, l'année de cette Constitution, puis le jour du mois de juillet où nous fêtons la nation. » Trouve les trois nombres.",
      BO + " ; " + CONST,
      "L'article 2 de la Constitution de 1958 fixe le drapeau tricolore, l'hymne national (la Marseillaise) et la devise « Liberté, Égalité, Fraternité ». La fête nationale est le 14 juillet. Le code est donc 2, 1958, 14. Les droits et les libertés sont protégés par la Déclaration de 1789 et par la Constitution de 1958 : voir les jeux « Le Secret de la Déclaration » et « Le Sceau de la République ».",
      {"cm2": ["Cherche « article 2 » dans la fiche.", "La Constitution actuelle date de 1958.", "La fête nationale : le 14 juillet."]},
      commun=code([("Article", "2"), ("Année", "1958"), ("Jour de la fête nationale", "14")]),
      lecon="republique", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "Le Testament de l'Empereur", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données. Repères en CM1, dates exactes en CM2.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": " ; ".join([BO, FN, MA, LOUVRE, BDF, ELY, CONST, HPI]) + ". Détail : README.md, section Sources.",
            "vigilance": "Bilan nuancé, sans hagiographie ni caricature : réformes durables, mais guerres et morts, régime autoritaire (censure), rétablissement de l'esclavage en 1802 ; aucune scène de combat ; personnages inventés ; les personnes réelles ne parlent jamais. Lois protectrices des droits : renvoi aux jeux « Le Secret de la Déclaration » et « Le Sceau de la République ».",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e2-1\",\"legende\":\"…\",\"source\":\"…\"}. La carte, la frise, le schéma du tableau du Sacre et la place de la commune sont dessinés en SVG par script : ne jamais les remplacer par des images générées par IA. Œuvres réelles (tableau de David, monuments) : photographies Wikimedia Commons uniquement."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
