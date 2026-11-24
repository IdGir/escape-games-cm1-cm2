# -*- coding: utf-8 -*-
"""Génère terre-active/assets/data/enigmes.json (L'Observatoire des volcans). Lancer : python gen_enigmes.py <dossier data>
Programme : BO n° 24 du 11 juin 2026, annexe 2, CM2 « L'activité terrestre » (manifestations de l'activité interne et externe ;
risque naturel, prévention et protection ; modélisation). Ton rassurant ; on ne prévoit pas le jour d'un séisme ; la catastrophe de 1902
est traitée avec sobriété. Station d'observation, village de Bois-Clair et personnages inventés."""
import json, os, sys
from schemas import terre, plaques, volcan, seisme, carte_risques

BO = "Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2) : « La Terre, une planète active », CM2 « L'activité terrestre » (progression de l'enseignant : année A, période 5)"
STRUCT = "Futura-Sciences, « Structure de la Terre » (2018)"
PUYS = "Ministère de la Culture, « Patrimoine mondial de l'Unesco : une victoire volcanique » (6 juillet 2018)"
PELEE = "Espace des sciences, Sciences Ouest n° 416, « L'éruption de la montagne Pelée, détonateur de la volcanologie » (2024) ; Futura-Sciences, « Il y a 120 ans, la plus grande catastrophe volcanique du XXe siècle » (2022)"
FOURN = "Futura-Sciences, « Le Piton de la Fournaise s'est réveillé » (2020) ; Institut de physique du globe de Paris (IPGP), observatoires volcanologiques"
SOUF = "IPGP, communiqué « Soufrière 50 » (juin 2026)"
SDES = "Service des données et études statistiques (SDES), Chiffres clés des risques naturels, « Séismes en métropole et en outre-mer » (2023)"
CONSIGNES = "Préfecture du Puy-de-Dôme, « Les bons réflexes en cas de séisme » ; préfecture de la Nièvre, DDRM 2019, « Consignes risque sismique » ; ministère de l'Europe et des Affaires étrangères, « Que faire en cas de séisme » et « Que faire en cas d'éruption volcanique » (2026)"


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


def plan(titre, col, cases, etiq):
    return {"titre": titre, "colonnes": col, "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(cases)], "etiquettes": etiq}


def tableau(titre, entetes, lignes):
    h = "".join(f"<th>{x}</th>" for x in entetes)
    c = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in l) + "</tr>" for l in lignes)
    return f"<div class='doc-titre'><i>{titre}</i></div><table class='tableau-releves'><tr>{h}</tr>{c}</table>"


CARNET_ADELE = tableau("Le carnet d'Adèle : trois nombres pour le message d'information",
                       ["Ce que dit le carnet", "Nombre"],
                       [["Nombre de zones de sismicité en France depuis 2011", "?"],
                        ["Nombre de volcans de la Chaîne des Puys", "?"],
                        ["Année du séisme du Teil, en Ardèche", "?"]]) + \
    "<p><i>Aide-toi des fiches : elles contiennent ces trois nombres.</i></p>"

S = []
# =================================================================== SALLE 1 — la galerie de la Terre (Inès)
S.append({"num": 1, "titre": "La galerie de la Terre — Une planète active", "enigmes": [
    E("1-1", "Les panneaux renversés", "tri",
      {"cm1": "La secousse de cette nuit a fait tomber les panneaux de la galerie. Range chaque phénomène : vient-il de l'intérieur de la Terre ou de l'air et de l'eau, à la surface ?",
       "cm2": "Range chaque phénomène selon son origine : activité interne (sous nos pieds) ou activité externe (l'air et l'eau, à la surface)."},
      BO + " ; " + STRUCT,
      "Les éruptions volcaniques, les coulées de lave et les séismes viennent de l'intérieur de la Terre : ce sont des manifestations de l'activité interne. Les tempêtes, les inondations et l'érosion des falaises par les vagues viennent de l'air et de l'eau : activité externe. En CM2 : un tsunami est le plus souvent provoqué par un séisme sous la mer (interne) ; un cyclone et un glissement de terrain après de fortes pluies sont externes.",
      {"cm1": ["Sous nos pieds : la chaleur de la Terre.", "Le vent et la pluie viennent de l'air.", "Un séisme fait trembler le sol depuis l'intérieur."],
       "cm2": ["Un tsunami suit souvent un séisme sous la mer.", "Un cyclone est un vent très violent.", "Le glissement vient ici des fortes pluies."]},
      cm1=tri([("int", "Vient de l'intérieur de la Terre"), ("ext", "Vient de l'air et de l'eau")],
              [("une éruption volcanique", "int"), ("un séisme", "int"), ("une coulée de lave", "int"),
               ("une tempête", "ext"), ("une inondation", "ext"), ("une falaise rongée par les vagues", "ext")]),
      cm2=tri([("int", "Activité interne"), ("ext", "Activité externe")],
              [("une éruption volcanique", "int"), ("un séisme", "int"), ("un tsunami après un séisme sous la mer", "int"), ("une coulée de lave", "int"),
               ("un cyclone", "ext"), ("une inondation", "ext"), ("un glissement de terrain après de fortes pluies", "ext"), ("une falaise rongée par les vagues", "ext")]),
      lecon="activite"),
    E("1-2", "La maquette coupée", "plan",
      {"cm1": "Au milieu de la galerie, la grande maquette de la Terre est coupée en deux. Ses étiquettes sont tombées. Place chaque mot sur son repère : clique sur une étiquette, puis sur la case du repère." + terre(3),
       "cm2": "Replace les étiquettes de la maquette de la Terre sur leurs repères. Attention : il y a des étiquettes en trop." + terre(5)},
      BO + " ; " + STRUCT,
      "Le repère 1 montre la croûte, la mince enveloppe où nous vivons ; le repère 2 le manteau, très épais ; le repère 3 le noyau, au centre. En CM2 : le repère 4 marque la limite entre le manteau et le noyau, vers 2 900 km de profondeur, et le repère 5 le centre de la Terre, à environ 6 400 km. L'atmosphère et l'océan ne sont pas des enveloppes de l'intérieur du globe.",
      {"cm1": ["La croûte est la fine bordure extérieure.", "Le manteau est la couche la plus épaisse.", "Le noyau est au centre."],
       "cm2": ["Le centre est le point le plus profond.", "2 900 km : la limite entre deux enveloppes.", "L'air et l'eau sont au-dessus de la croûte."]},
      cm1=plan("La maquette d'Inès", 3, ["la croûte", "le manteau", "le noyau"], ["la croûte", "le manteau", "le noyau"]),
      cm2=plan("La maquette d'Inès", 2, ["la croûte", "le manteau", "le noyau", "environ 2 900 km", "le centre, à environ 6 400 km"],
               ["la croûte", "le manteau", "le noyau", "environ 2 900 km", "le centre, à environ 6 400 km", "l'atmosphère", "l'océan"]),
      lecon="activite"),
    E("1-3", "Le quiz de la galerie", "qcm",
      {"cm1": "Inès prépare le quiz des visiteurs de la galerie. Réponds à ses questions.",
       "cm2": "Inès vérifie les réponses du quiz de la galerie. Choisis la bonne réponse."},
      BO + " ; " + STRUCT + " ; " + PUYS,
      "La Terre est une planète active : sa surface change, parfois lentement, parfois brusquement. La croûte est l'enveloppe la plus fine, le noyau est au centre. En CM2 : sous les continents, la croûte mesure en moyenne environ 30 km ; le manteau descend jusqu'à environ 2 900 km ; personne n'est allé dans le manteau, on l'étudie grâce aux ondes des séismes.",
      {"cm1": ["Une planète active change.", "La croûte est fine comme une peau.", "Le noyau est au milieu."],
       "cm2": ["30 km, c'est très peu à côté de 6 400 km.", "2 900 km : la fin du manteau.", "Les ondes des séismes traversent la Terre."]},
      cm1=qcm([("Que veut dire « la Terre est une planète active » ?", ["sa surface ne change jamais", "sa surface change, parfois brusquement", "elle tourne plus vite chaque année", "elle n'a pas d'intérieur"], 1, "Volcans et séismes en sont des signes."),
               ("Quelle est l'enveloppe la plus fine ?", ["le noyau", "le manteau", "la croûte", "le centre"], 2, "Nous vivons sur la croûte."),
               ("Où se trouve le noyau ?", ["à la surface", "au centre de la Terre", "dans les nuages", "au fond de la mer"], 1, "C'est la partie la plus profonde.")]),
      cm2=qcm([("Sous les continents, quelle est l'épaisseur moyenne de la croûte ?", ["environ 3 km", "environ 30 km", "environ 3 000 km", "environ 6 400 km"], 1, "C'est très mince par rapport au rayon de la Terre."),
               ("Jusqu'à quelle profondeur descend le manteau ?", ["environ 30 km", "environ 290 km", "environ 2 900 km", "environ 29 000 km"], 2, "Ensuite commence le noyau."),
               ("Comment les scientifiques étudient-ils l'intérieur de la Terre ?", ["en y descendant en ascenseur", "grâce aux ondes des séismes", "en creusant jusqu'au noyau", "avec un télescope"], 1, "Personne n'est jamais allé dans le manteau."),
               ("Pourquoi dit-on que la Terre est une planète active ?", ["parce qu'elle a des océans", "parce que sa surface change, parfois brusquement", "parce qu'elle a une Lune", "parce qu'il y pleut"], 1, "Les volcans et les séismes le montrent.")]),
      lecon="activite"),
    E("1-4", "Le voyage vers le centre", "ordre",
      "Inès imagine un voyage de la surface jusqu'au centre de la Terre. Remets les étapes dans l'ordre, de la surface au centre.",
      BO + " ; " + STRUCT,
      "On part de la surface (montagnes et océans), on traverse la croûte (environ 30 km sous les continents), puis le manteau jusqu'à environ 2 900 km, puis le noyau, et l'on arrive au centre, à environ 6 400 km de profondeur.",
      {"cm2": ["On commence là où nous vivons.", "Le manteau est sous la croûte.", "6 400 km, c'est le plus profond."]},
      commun=ordre([("La surface : montagnes et océans", "0 km"), ("La croûte", "jusqu'à environ 30 km sous les continents"),
                    ("Le manteau", "jusqu'à environ 2 900 km"), ("Le noyau", "au-delà de 2 900 km"), ("Le centre de la Terre", "à environ 6 400 km")]),
      lecon="activite", cm2_seul=True),
]})

# =================================================================== SALLE 2 — la salle des cartes (Noé)
S.append({"num": 2, "titre": "La salle des cartes — Les plaques", "enigmes": [
    E("2-1", "La maquette de Noé", "plan",
      {"cm1": "Noé a construit une maquette de deux plaques qui se rapprochent. La secousse a fait tomber ses étiquettes. Place chaque mot sur son repère." + plaques(3),
       "cm2": "Replace les étiquettes de la maquette de Noé. Attention : il y a des étiquettes en trop." + plaques(5)},
      BO + " ; " + STRUCT,
      "Le repère 1 montre une plaque, posée sur le repère 2, le manteau ; le repère 3 montre un volcan, près de la frontière des deux plaques. En CM2 : le repère 4 est le foyer d'un séisme, là où la roche casse, et le repère 5 la plaque qui s'enfonce sous l'autre. Le noyau est bien plus profond, et un glacier n'a rien à faire sur cette maquette.",
      {"cm1": ["La plaque est la couche dure du dessus.", "Le manteau est en dessous.", "Le volcan a un panache de fumée."],
       "cm2": ["Le foyer est l'étoile jaune.", "Une plaque plonge vers le bas.", "Le noyau n'est pas sur la maquette."]},
      cm1=plan("La maquette de Noé", 3, ["une plaque", "le manteau", "un volcan"], ["une plaque", "le manteau", "un volcan"]),
      cm2=plan("La maquette de Noé", 2, ["une plaque", "le manteau", "un volcan", "le foyer d'un séisme", "la plaque qui s'enfonce"],
               ["une plaque", "le manteau", "un volcan", "le foyer d'un séisme", "la plaque qui s'enfonce", "le noyau", "un glacier"]),
      lecon="plaques"),
    E("2-2", "Les notes de Noé", "vraifaux",
      {"cm1": "Noé a écrit des phrases sur les plaques, mais la secousse a mélangé ses fiches. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Noé relit ses notes avant de les afficher. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + SDES,
      "La surface de la Terre est découpée en grandes plaques qui bougent très lentement, de quelques centimètres par an : on ne sent pas ce mouvement. La plupart des volcans et des séismes sont près des frontières entre les plaques. En CM2 : les Antilles sont à la frontière de plusieurs plaques, d'où les volcans et les séismes de Guadeloupe et de Martinique ; une maquette est un modèle, pas la réalité.",
      {"cm1": ["Pense aux morceaux d'un puzzle.", "Quelques centimètres par an, c'est très lent.", "Les frontières sont les zones agitées."],
       "cm2": ["Les Antilles : plusieurs plaques se rencontrent.", "Une maquette simplifie.", "On ne sent pas bouger les plaques."]},
      cm1=vf([("La surface de la Terre est découpée en grandes plaques.", True, "Comme les morceaux d'un puzzle."),
              ("Les plaques bougent de plusieurs mètres chaque jour.", False, "Elles bougent de quelques centimètres par an."),
              ("Beaucoup de volcans se trouvent près des frontières entre les plaques.", True, "C'est là que la Terre est la plus active.")]),
      cm2=vf([("Les plaques bougent de quelques centimètres par an.", True, "On ne sent pas ce mouvement."),
              ("La plupart des séismes ont lieu au milieu des plaques, loin des frontières.", False, "La plupart sont près des frontières."),
              ("La Guadeloupe et la Martinique sont à la frontière de plusieurs plaques.", True, "D'où leurs volcans et leurs séismes."),
              ("Une maquette montre exactement la réalité, à la bonne taille.", False, "C'est un modèle simplifié."),
              ("On sent les plaques bouger quand on marche.", False, "Leur mouvement est bien trop lent.")]),
      lecon="plaques"),
    E("2-3", "Ce que représente la maquette", "association",
      {"cm1": "Noé explique sa maquette aux visiteurs. Relie chaque élément de la maquette à ce qu'il représente dans la réalité.",
       "cm2": "Relie chaque élément de la maquette de Noé à ce qu'il représente dans la réalité."},
      BO,
      "Les plaques de polystyrène représentent les plaques de la surface ; la pâte molle en dessous, le manteau ; la main qui pousse lentement, le mouvement des plaques. En CM2 : la pâte qui se plisse représente une montagne qui se forme ; la fente qui s'ouvre, une frontière où les plaques s'écartent ; le craquement brusque, un séisme.",
      {"cm1": ["Le polystyrène est dur, comme les plaques.", "Le dessous est mou et chaud dans la réalité.", "La main pousse lentement."],
       "cm2": ["Un pli de pâte, c'est un relief.", "Une fente, c'est un écartement.", "Un craquement brusque, c'est une roche qui casse."]},
      cm1=assoc([("deux plaques de polystyrène", "deux plaques de la surface"), ("la pâte molle en dessous", "le manteau"), ("la main qui pousse lentement", "le mouvement des plaques")]),
      cm2=assoc([("deux plaques de polystyrène", "deux plaques de la surface"), ("la pâte molle en dessous", "le manteau"),
                 ("la pâte qui se plisse", "une montagne qui se forme"), ("la fente qui s'ouvre", "une frontière où les plaques s'écartent"),
                 ("le craquement brusque du bâton", "un séisme")]),
      lecon="plaques"),
    E("2-4", "Le planisphère des alertes", "tri",
      "Sur le planisphère de Noé, les punaises sont tombées. Range chaque lieu : près d'une frontière de plaques, où volcans et séismes sont fréquents, ou loin d'une frontière, où ils sont rares et faibles.",
      BO + " ; " + SDES,
      "La Guadeloupe et la Martinique, aux Antilles, l'Islande et le Japon sont près de frontières de plaques. La Bourgogne, le Bassin parisien et la Bretagne en sont loin : les séismes y sont rares et faibles.",
      {"cm2": ["Les Antilles : plusieurs plaques s'y rencontrent.", "L'Islande est coupée en deux par une frontière.", "La métropole est loin des frontières."]},
      commun=tri([("pres", "Près d'une frontière de plaques"), ("loin", "Loin d'une frontière")],
                 [("la Guadeloupe", "pres"), ("la Martinique", "pres"), ("l'Islande", "pres"), ("le Japon", "pres"),
                  ("la Bourgogne", "loin"), ("le Bassin parisien", "loin"), ("la Bretagne", "loin")]),
      lecon="plaques", cm2_seul=True),
]})

# =================================================================== SALLE 3 — le sentier du cratère (Maëva)
S.append({"num": 3, "titre": "Le sentier du cratère — Les volcans", "enigmes": [
    E("3-1", "Le carnet de Maëva", "plan",
      {"cm1": "Au bord du sentier, Maëva montre son carnet : le volcan dessiné a perdu ses étiquettes. Place chaque mot sur son repère." + volcan(3),
       "cm2": "Replace les étiquettes du volcan dessiné par Maëva. Attention : il y a des étiquettes en trop." + volcan(5)},
      BO + " ; " + FOURN,
      "Le repère 1 montre le cratère, l'ouverture au sommet ; le repère 2 la cheminée, par où monte le magma ; le repère 3 la chambre magmatique, où le magma s'accumule. En CM2 : le repère 4 est une coulée de lave et le repère 5 le nuage de cendres et de gaz. Le noyau est bien plus profond et une source d'eau n'est pas une partie du volcan.",
      {"cm1": ["Le cratère est tout en haut.", "La cheminée est un long tuyau.", "Le magma attend dans une poche, en bas."],
       "cm2": ["La lave coule sur le flanc.", "Le nuage gris s'élève au-dessus.", "Le noyau est au centre de la Terre."]},
      cm1=plan("Le carnet de Maëva", 3, ["le cratère", "la cheminée", "la chambre magmatique"], ["le cratère", "la cheminée", "la chambre magmatique"]),
      cm2=plan("Le carnet de Maëva", 2, ["le cratère", "la cheminée", "la chambre magmatique", "une coulée de lave", "le nuage de cendres et de gaz"],
               ["le cratère", "la cheminée", "la chambre magmatique", "une coulée de lave", "le nuage de cendres et de gaz", "le noyau", "une source d'eau"]),
      lecon="volcans"),
    E("3-2", "L'éruption pas à pas", "ordre",
      {"cm1": "Maëva raconte une éruption aux visiteurs, mais ses cartes sont mélangées. Remets les étapes dans l'ordre.",
       "cm2": "Maëva prépare le panneau « Une éruption pas à pas ». Remets les étapes dans l'ordre."},
      BO + " ; " + FOURN,
      "Le magma s'accumule dans la chambre magmatique, il monte par la cheminée, il sort par le cratère, puis la lave coule et refroidit en roche dure. En CM2 : avant l'éruption, l'observatoire enregistre souvent de petits séismes, signe que le magma monte ; à la fin, la lave refroidie forme une roche dure.",
      {"cm1": ["Tout commence sous le volcan.", "Le magma monte avant de sortir.", "La lave refroidit à la fin."],
       "cm2": ["Les capteurs sentent le magma monter.", "Sortir par le cratère vient après la montée.", "La roche dure est la dernière étape."]},
      cm1=ordre(["Le magma s'accumule dans la chambre magmatique.", "Le magma monte par la cheminée.", "Le magma sort par le cratère : c'est l'éruption.", "La lave coule, refroidit et devient une roche dure."]),
      cm2=ordre([("Le magma s'accumule dans la chambre magmatique.", "sous le volcan"), ("De petits séismes sont enregistrés par l'observatoire.", "le magma pousse les roches"),
                 ("Le magma monte par la cheminée.", "il s'approche de la surface"), ("La lave sort par le cratère ou par des fissures.", "c'est l'éruption"),
                 ("La lave refroidit et devient une roche dure.", "après l'éruption")]),
      lecon="volcans"),
    E("3-3", "Les volcans de France", "association",
      {"cm1": "Maëva a rapporté trois échantillons. Relie chaque produit du volcan à sa description.",
       "cm2": "Sur la carte des volcans de France, les fiches sont tombées. Relie chaque volcan à ce que l'on sait de lui."},
      BO + " ; " + FOURN + " ; " + PELEE + " ; " + SOUF + " ; " + PUYS,
      "La lave est une roche fondue qui coule puis durcit ; les cendres sont de fines poussières projetées dans l'air ; les gaz s'échappent du cratère. En CM2 : le Piton de la Fournaise, à La Réunion, est l'un des volcans les plus actifs du monde ; la montagne Pelée, en Martinique, a détruit Saint-Pierre le 8 mai 1902 ; la Soufrière, en Guadeloupe, a entraîné l'évacuation de dizaines de milliers d'habitants en 1976 ; la Chaîne des Puys, en Auvergne, compte 80 volcans endormis depuis au moins 8 000 ans.",
      {"cm1": ["La lave est liquide et brûlante.", "Les cendres ressemblent à de la poussière grise.", "Les gaz sont invisibles ou forment une fumée."],
       "cm2": ["La Réunion est dans l'océan Indien.", "1902 : Saint-Pierre, en Martinique.", "L'Auvergne : des volcans endormis."]},
      cm1=assoc([("la lave", "une roche fondue qui coule, puis durcit"), ("les cendres", "de fines poussières projetées dans l'air"), ("les gaz", "ils s'échappent du cratère en fumées")]),
      cm2=assoc([("le Piton de la Fournaise", "La Réunion : l'un des volcans les plus actifs du monde"), ("la montagne Pelée", "Martinique : Saint-Pierre détruite le 8 mai 1902"),
                 ("la Soufrière", "Guadeloupe : des dizaines de milliers d'habitants évacués en 1976"), ("la Chaîne des Puys", "Auvergne : 80 volcans endormis depuis au moins 8 000 ans"),
                 ("le magma", "roche fondue qui s'accumule sous le volcan")]),
      lecon="volcans"),
    E("3-4", "Deux éruptions, deux caractères", "qcm",
      "Maëva compare deux éruptions célèbres. Choisis la bonne réponse.",
      BO + " ; " + FOURN + " ; " + PELEE,
      "Quand la lave est fluide, elle coule en longues coulées : l'éruption est effusive, comme souvent au Piton de la Fournaise. Quand le magma est épais et riche en gaz, il explose en cendres et en nuées ardentes : l'éruption est explosive, comme à la montagne Pelée en 1902. Une nuée ardente est un nuage brûlant de gaz et de cendres qui dévale la pente.",
      {"cm2": ["Effusive : la lave coule.", "Explosive : cendres et nuées ardentes.", "1902 : la montagne Pelée."]},
      commun=qcm([("Au Piton de la Fournaise, la lave est souvent fluide et coule en longues coulées. L'éruption est…", ["explosive", "effusive", "glaciaire", "souterraine"], 1, "La lave coule doucement."),
                  ("Qu'est-ce qu'une nuée ardente ?", ["un nuage de pluie", "un nuage brûlant de gaz et de cendres qui dévale la pente", "une coulée d'eau froide", "un arc-en-ciel au-dessus du cratère"], 1, "C'est ce qui a frappé Saint-Pierre en 1902."),
                  ("En 1902, l'éruption de la montagne Pelée était…", ["effusive", "explosive", "sans danger", "sous la mer"], 1, "Magma épais et riche en gaz."),
                  ("Un volcan endormi depuis 8 000 ans, comme ceux de la Chaîne des Puys…", ["est forcément éteint pour toujours", "est surveillé, car un volcan endormi peut se réveiller", "n'a jamais eu d'éruption", "n'est pas un volcan"], 1, "Les scientifiques les surveillent.")]),
      lecon="volcans", cm2_seul=True),
]})

# =================================================================== SALLE 4 — la salle des sismographes (Samuel)
S.append({"num": 4, "titre": "La salle des sismographes — Les séismes", "enigmes": [
    E("4-1", "Le lexique du sismologue", "association",
      {"cm1": "Les étiquettes du lexique de Samuel sont tombées des tiroirs. Relie chaque mot à sa définition.",
       "cm2": "Relie chaque mot du lexique de Samuel à sa définition."},
      BO + " ; " + SDES,
      "Le foyer est l'endroit sous terre où la roche casse ; l'épicentre est le point de la surface juste au-dessus ; le sismographe enregistre les vibrations du sol. En CM2 : les ondes sismiques sont les vibrations qui partent du foyer ; la magnitude mesure l'énergie libérée ; les répliques sont des secousses plus faibles qui suivent le séisme.",
      {"cm1": ["Le foyer est en profondeur.", "L'épicentre est à la surface.", "Un « graphe » écrit."],
       "cm2": ["Les ondes voyagent.", "La magnitude est un nombre.", "Une réplique vient après."]},
      cm1=assoc([("le foyer", "l'endroit sous terre où la roche casse"), ("l'épicentre", "le point de la surface juste au-dessus du foyer"), ("le sismographe", "l'appareil qui enregistre les vibrations du sol")]),
      cm2=assoc([("le foyer", "l'endroit sous terre où la roche casse"), ("l'épicentre", "le point de la surface juste au-dessus du foyer"),
                 ("les ondes sismiques", "les vibrations qui partent du foyer"), ("la magnitude", "le nombre qui mesure l'énergie libérée"),
                 ("une réplique", "une secousse plus faible qui suit le séisme")]),
      lecon="seismes"),
    E("4-2", "Le tableau du séisme", "plan",
      {"cm1": "Sur le grand tableau de Samuel, le schéma du séisme a perdu ses étiquettes. Place chaque mot sur son repère." + seisme(3),
       "cm2": "Replace les étiquettes du schéma de Samuel. Attention : il y a des étiquettes en trop." + seisme(5)},
      BO + " ; " + SDES,
      "Le repère 1 montre le foyer, où la roche casse ; le repère 2 l'épicentre, juste au-dessus, à la surface ; le repère 3 la faille, la cassure dans les roches. En CM2 : le repère 4 montre les ondes sismiques qui partent du foyer et le repère 5 un sismographe, qui les enregistre. Le cratère et la cheminée appartiennent à un volcan.",
      {"cm1": ["Le foyer est l'étoile jaune.", "L'épicentre est sur le sol, au-dessus.", "La faille est le grand trait marron."],
       "cm2": ["Les cercles en pointillés : les ondes.", "La petite boîte enregistre.", "Il n'y a pas de volcan ici."]},
      cm1=plan("Le tableau de Samuel", 3, ["le foyer", "l'épicentre", "la faille"], ["le foyer", "l'épicentre", "la faille"]),
      cm2=plan("Le tableau de Samuel", 2, ["le foyer", "l'épicentre", "la faille", "les ondes sismiques", "un sismographe"],
               ["le foyer", "l'épicentre", "la faille", "les ondes sismiques", "un sismographe", "le cratère", "la cheminée"]),
      lecon="seismes"),
    E("4-3", "Les questions des habitants", "qcm",
      {"cm1": "Les habitants de Bois-Clair ont téléphoné à l'observatoire. Aide Samuel à leur répondre.",
       "cm2": "Samuel prépare les réponses aux questions des habitants. Choisis la bonne réponse."},
      BO + " ; " + SDES,
      "Un séisme se produit quand les roches cassent brusquement le long d'une faille. Personne ne sait prévoir le jour et l'heure d'un séisme, mais on sait où ils sont probables. En CM2 : la magnitude mesure l'énergie libérée ; depuis 2011, la France compte cinq zones de sismicité, et la Guadeloupe et la Martinique sont entièrement en zone forte ; le 11 novembre 2019, un séisme de magnitude 4,8 a endommagé Le Teil, en Ardèche.",
      {"cm1": ["La roche casse d'un coup.", "On ne connaît pas le jour à l'avance.", "Les Antilles sont près des frontières de plaques."],
       "cm2": ["Cinq zones, de « très faible » à « forte ».", "Le Teil : 2019, en Ardèche.", "La magnitude est une mesure d'énergie."]},
      cm1=qcm([("Que se passe-t-il lors d'un séisme ?", ["les roches cassent brusquement sous terre", "il pleut très fort", "la mer gèle", "le volcan s'éteint"], 0, "La cassure fait vibrer le sol."),
               ("Peut-on savoir le jour exact du prochain séisme ?", ["oui, toujours", "non, personne ne sait le prévoir", "oui, grâce à la météo", "oui, il arrive chaque lundi"], 1, "On sait où, pas quand."),
               ("Où les séismes sont-ils les plus forts en France ?", ["en Bourgogne", "aux Antilles", "à Paris", "en Bretagne"], 1, "La Guadeloupe et la Martinique sont en zone forte.")]),
      cm2=qcm([("Que mesure la magnitude ?", ["la durée du séisme", "l'énergie libérée par le séisme", "la profondeur de la mer", "le nombre de maisons"], 1, "Plus elle est grande, plus le séisme est fort."),
               ("Combien de zones de sismicité compte la France depuis 2011 ?", ["deux", "trois", "cinq", "dix"], 2, "De « très faible » à « forte »."),
               ("Quelle commune a été endommagée par un séisme de magnitude 4,8 le 11 novembre 2019 ?", ["Le Teil, en Ardèche", "Saint-Pierre, en Martinique", "Dijon", "Clermont-Ferrand"], 0, "Un séisme peu profond, en métropole."),
               ("Que savent faire les scientifiques ?", ["prévoir l'heure exacte d'un séisme", "dire où les séismes sont probables", "empêcher les séismes", "arrêter les plaques"], 1, "D'où les cartes des risques.")]),
      lecon="seismes"),
    E("4-4", "La consigne du bord de mer", "trous",
      "Samuel rédige la consigne « tsunami » pour le panneau de la plage de Bois-Clair. Complète-la. Attention : il y a des étiquettes en trop.",
      BO + " ; " + CONSIGNES,
      "Un tsunami est une série de vagues géantes, souvent provoquée par un séisme sous la mer. Si le sol tremble fort au bord de la mer, il faut s'éloigner de la côte et monter sur une hauteur, puis écouter les consignes des autorités.",
      {"cm2": ["Le tsunami suit souvent un séisme.", "On s'éloigne de l'eau.", "On monte, on ne descend pas."]},
      commun={"texte": "<p>Un tsunami est une série de vagues géantes, souvent provoquée par un [[séisme]] sous la mer. Si le sol tremble fort au bord de la mer, il faut s'éloigner de la [[côte]] et monter sur une [[hauteur]]. Ensuite, on écoute les [[consignes]] des autorités.</p>",
              "etiquettes": ["séisme", "côte", "hauteur", "consignes", "tempête", "plage", "cave"]},
      lecon="seismes", cm2_seul=True),
]})

# =================================================================== SALLE 5 — le centre de secours de Bois-Clair (Adèle)
S.append({"num": 5, "titre": "Le centre de secours — Prévenir et se protéger", "enigmes": [
    E("5-1", "Les bons réflexes", "tri",
      {"cm1": "Adèle prépare une affiche pour l'école de Bois-Clair. Range chaque geste : bon réflexe pendant un séisme, ou geste à ne pas faire.",
       "cm2": "Adèle range les consignes officielles « séisme » : avant, pendant ou après les secousses ?"},
      BO + " ; " + CONSIGNES,
      "Pendant les secousses, on s'abrite sous un meuble solide ou près d'un mur porteur, on protège sa tête avec les bras et on s'éloigne des fenêtres ; on ne court pas dehors et on ne prend pas l'ascenseur. En CM2 : avant, on fixe les meubles lourds et on repère où s'abriter ; pendant, on reste où l'on est et on s'abrite ; après, on sort par les escaliers, sans ascenseur, on écoute les consignes des autorités et on ne va pas chercher les enfants à l'école.",
      {"cm1": ["Une table solide protège des chutes d'objets.", "Une vitre peut se briser.", "Pendant les secousses, on ne court pas."],
       "cm2": ["Fixer et repérer : on le fait à l'avance.", "S'abriter : pendant.", "Sortir par l'escalier : après."]},
      cm1=tri([("bon", "Bon réflexe"), ("non", "À ne pas faire")],
              [("se mettre sous une table solide", "bon"), ("protéger sa tête avec les bras", "bon"), ("s'éloigner des fenêtres", "bon"),
               ("courir dehors pendant les secousses", "non"), ("prendre l'ascenseur", "non"), ("se coller contre une vitre", "non")]),
      cm2=tri([("avant", "Avant"), ("pendant", "Pendant"), ("apres", "Après")],
              [("fixer les meubles lourds", "avant"), ("repérer les endroits où s'abriter", "avant"),
               ("s'abriter sous un meuble solide", "pendant"), ("rester où l'on est et protéger sa tête", "pendant"),
               ("sortir par les escaliers, sans ascenseur", "apres"), ("écouter les consignes des autorités", "apres"), ("laisser l'école garder les enfants", "apres")]),
      lecon="prevention"),
    E("5-2", "La carte des risques", "vraifaux",
      {"cm1": "Adèle montre la carte des risques de Bois-Clair. Pour chaque phrase, choisis vrai ou faux." + carte_risques(),
       "cm2": "Adèle vérifie les phrases du dossier « risques » de la mairie. Pour chaque phrase, choisis vrai ou faux." + carte_risques()},
      BO + " ; Géorisques (georisques.gouv.fr) ; " + CONSIGNES,
      "Un risque naturel existe quand un phénomène naturel peut toucher des personnes, des maisons ou des routes. La carte des risques montre les zones où le danger est fort : ici, la zone A, près du volcan ; l'école est en zone C. Les observatoires surveillent les volcans et les séismes jour et nuit. En CM2 : la prévention, c'est ce que l'on fait avant (surveiller, informer, construire solidement, s'entraîner) ; la protection met les personnes à l'abri pendant et après ; on ne sait pas prévoir le jour d'un séisme.",
      {"cm1": ["Regarde où se trouve l'école sur la carte.", "La zone A touche le volcan.", "Un observatoire surveille sans arrêt."],
       "cm2": ["Prévenir, c'est agir avant.", "Protéger, c'est mettre à l'abri.", "On sait où, pas quand."]},
      cm1=vf([("Sur la carte, l'école est dans la zone où le danger est le plus fort.", False, "L'école est en zone C, danger faible."),
              ("Un observatoire surveille le volcan jour et nuit.", True, "Avec des sismographes et d'autres capteurs."),
              ("La carte des risques aide à choisir où construire.", True, "On évite la zone A.")]),
      cm2=vf([("Un risque naturel existe quand un phénomène naturel peut toucher des personnes ou des biens.", True, "Sans habitants, pas de risque pour eux."),
              ("La prévention, c'est ce que l'on fait seulement après la catastrophe.", False, "La prévention se fait avant."),
              ("Construire des bâtiments solides est une mesure de prévention.", True, "Ils résistent mieux aux secousses."),
              ("Grâce aux capteurs, on connaît le jour exact du prochain séisme.", False, "Personne ne sait le prévoir."),
              ("Évacuer les habitants sur ordre des autorités est une mesure de protection.", True, "On les met à l'abri.")]),
      lecon="prevention"),
    E("5-3", "L'exercice de l'école", "ordre",
      {"cm1": "Demain, l'école de Bois-Clair fait un exercice « séisme ». Remets les étapes dans l'ordre pour la fiche d'Adèle.",
       "cm2": "Adèle prépare la fiche de l'exercice « séisme » de l'école. Remets les étapes dans l'ordre."},
      BO + " ; " + CONSIGNES,
      "On reconnaît le signal de l'exercice, on s'abrite sous sa table en protégeant sa tête, on attend la fin des secousses, on sort calmement par l'escalier, puis on se rassemble au point de rassemblement, loin des bâtiments. En CM2 : avant de sortir, on vérifie que le chemin est sûr et l'on écoute la maîtresse ou le maître ; dehors, on s'éloigne des bâtiments et des fils électriques.",
      {"cm1": ["D'abord se protéger.", "On ne sort pas pendant les secousses.", "Le rassemblement est la fin."],
       "cm2": ["S'abriter vient tout de suite.", "On attend avant de bouger.", "Dehors : loin des bâtiments."]},
      cm1=ordre(["Le signal de l'exercice retentit.", "Je m'abrite sous ma table et je protège ma tête.", "J'attends la fin des secousses.", "Je sors calmement par l'escalier.", "Je rejoins le point de rassemblement."]),
      cm2=ordre([("Le signal de l'exercice retentit.", "on reste où l'on est"), ("Chacun s'abrite sous sa table et protège sa tête avec les bras.", "loin des fenêtres"),
                 ("On attend la fin des secousses.", "on écoute l'adulte"), ("On sort calmement par l'escalier, sans ascenseur.", "le chemin est vérifié"),
                 ("On se rassemble loin des bâtiments et des fils électriques.", "au point de rassemblement")]),
      lecon="prevention"),
    E("5-4", "Le message d'information", "code",
      "Le message d'information pour les habitants est prêt, mais il est verrouillé : il faut trois nombres pour l'ouvrir. Retrouve-les dans les fiches de l'observatoire." + CARNET_ADELE,
      BO + " ; " + SDES + " ; " + PUYS,
      "Depuis 2011, la France est découpée en 5 zones de sismicité ; la Chaîne des Puys compte 80 volcans ; le séisme du Teil a eu lieu en 2019. Le code est 5, 80, 2019.",
      {"cm2": ["Fiche « Les séismes » : les zones.", "Fiche « Les volcans » : l'Auvergne.", "Le Teil : un 11 novembre."]},
      commun=code([("Zones de sismicité", "5"), ("Volcans de la Chaîne des Puys", "80"), ("Année du séisme du Teil", "2019")]),
      lecon="prevention", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "L'Observatoire des volcans", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": " ; ".join([BO, STRUCT, PUYS, PELEE, FOURN, SOUF, SDES, CONSIGNES, "Géorisques (georisques.gouv.fr)"]) + ". Détail : README.md, section Sources.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-1\",\"legende\":\"…\",\"source\":\"…\"}. Les schémas (coupe de la Terre, maquette des plaques, volcan, séisme, carte des risques) sont dessinés en SVG par script : ne jamais les remplacer par des images générées par IA. Volcans réels : photos Wikimedia Commons."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
