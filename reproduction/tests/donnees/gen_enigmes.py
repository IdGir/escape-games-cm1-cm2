# -*- coding: utf-8 -*-
"""Génère reproduction/assets/data/enigmes.json (Le Jardin de la vie). Lancer : python gen_enigmes.py <dossier data>
Programme : BO n° 24 du 11 juin 2026, annexe 2 (voir fiches.py). Pas de reproduction humaine ni de puberté ; pas d'anthropomorphisme.
Jardin botanique et ferme des Coteaux (Bourgogne) et personnages inventés."""
import json, os, sys
from schemas import fleur

BO = "Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2) : « Les êtres vivants dans leur environnement », CM1 « Reproduction, croissance et développement » et « Unité et diversité du vivant », 6e « Reproduction, croissance et développement » (progression de l'enseignant : année A, période 5)"
CYCLE2 = "Programme du cycle 2, CE2, « Reproduction, croissance et développement » (BO n° 24 du 11 juin 2026, annexe 1) : étapes de la vie d'une plante à fleurs"
LAMAP_CYCLE = "La main à la pâte, séquence « Le cycle de vie des végétaux » (cycle 3)"
LAMAP_GERME = "La main à la pâte, « De quoi a besoin une graine pour germer ? »"
FLEUR = "Encyclopædia Universalis, « Fleur : les fleurs, organes reproducteurs »"
POLLIN = "Muséum national d'histoire naturelle (MNHN) et Office français de la biodiversité (OFB), Spipoll et pages « Les pollinisateurs »"
FAO = "FAO, « Incubation naturelle » (élevage des poules)"
LUMNI = "Lumni, vidéos « La reproduction des animaux » (ovipares et vivipares)"


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


def intrus(cartes):
    return {"cartes": [{"txt": t, "intrus": i} for t, i in cartes]}


def trous(texte, etiq):
    return {"texte": "<p>" + texte + "</p>", "etiquettes": etiq}


def code(champs):
    return {"champs": [{"libelle": l, "valeur": v, "longueur": len(v)} for l, v in champs]}


def plan(titre, col, cases, etiq):
    return {"titre": titre, "colonnes": col, "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(cases)], "etiquettes": etiq}


def tableau(titre, entetes, lignes):
    h = "".join(f"<th>{x}</th>" for x in entetes)
    c = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in l) + "</tr>" for l in lignes)
    return f"<div class='doc-titre'><i>{titre}</i></div><table class='tableau-releves'><tr>{h}</tr>{c}</table>"


POTS = tableau("L'expérience de Tom : quatre pots de haricots, une semaine plus tard",
               ["Pot", "Ce que Tom a fait", "Résultat"],
               [["A", "coton sec, dans la classe", "rien ne pousse"],
                ["B", "coton mouillé, dans la classe", "les graines ont germé"],
                ["C", "coton mouillé, dans le réfrigérateur", "rien ne pousse"],
                ["D", "coton mouillé, dans un placard noir, dans la classe", "les graines ont germé"]])

CARNET_NADIA = tableau("Le carnet de Nadia : trois nombres pour ouvrir le portail du jardin",
                       ["Ce que dit le carnet", "Nombre"],
                       [["Nombre de jours de couvaison d'un œuf de poule (environ)", "?"],
                        ["Nombre de mois avant la naissance d'un veau (environ)", "?"],
                        ["Nombre de mois avant la naissance d'un agneau (environ)", "?"]]) + \
    "<p><i>Aide-toi de la fiche « Naître ou éclore » : elle contient ces trois nombres.</i></p>"

S = []
# =================================================================== SALLE 1 — la serre (Basile, botaniste)
S.append({"num": 1, "titre": "La serre du botaniste — La fleur", "enigmes": [
    E("1-1", "La planche tombée", "plan",
      {"cm1": "Cette nuit, le vent a ouvert la porte de la serre et la grande planche de Basile est tombée : ses étiquettes se sont détachées. Place chaque mot sur son repère : clique sur une étiquette, puis sur la case du repère." + fleur(3),
       "cm2": "Replace les étiquettes de la planche « Une fleur coupée en deux ». Attention : il y a des étiquettes en trop." + fleur(5)},
      BO + " ; " + FLEUR,
      "Le repère 1 montre un pétale, coloré ; le repère 2 une étamine, dont le bout fabrique le pollen ; le repère 3 le pistil, au centre de la fleur. En CM2 : le repère 4 est un sépale, vert, sous les pétales ; le repère 5 est l'ovaire, la partie renflée du pistil, qui contient les ovules. Une racine et une graine ne sont pas des pièces de la fleur.",
      {"cm1": ["Le pétale est la grande pièce rose.", "L'étamine porte une petite boule jaune.", "Le pistil est tout au centre."],
       "cm2": ["Le sépale est vert, sous les pétales.", "L'ovaire est en bas du pistil, gonflé.", "Les racines sont sous la terre."]},
      cm1=plan("La planche de Basile", 3, ["un pétale", "une étamine", "le pistil"], ["un pétale", "une étamine", "le pistil"]),
      cm2=plan("La planche de Basile", 2, ["un pétale", "une étamine", "le pistil", "un sépale", "l'ovaire et ses ovules"],
               ["un pétale", "une étamine", "le pistil", "un sépale", "l'ovaire et ses ovules", "une racine", "une graine"]),
      lecon="fleur"),
    E("1-2", "Les fiches des pièces de la fleur", "association",
      {"cm1": "Basile range ses fiches. Relie chaque pièce de la fleur à son rôle.",
       "cm2": "Relie chaque pièce de la fleur à son rôle, pour les fiches de Basile."},
      BO + " ; " + FLEUR,
      "Les pétales, souvent colorés, attirent les insectes ; les étamines, organes mâles, fabriquent le pollen ; le pistil, organe femelle, contient les ovules dans son ovaire. En CM2 : les sépales protègent le bouton avant qu'il s'ouvre ; le stigmate, en haut du pistil, est collant et retient le pollen.",
      {"cm1": ["Une couleur vive se voit de loin.", "La poudre jaune vient des étamines.", "Les ovules sont cachés au centre."],
       "cm2": ["Le bouton fermé est entouré de vert.", "Collant comme de la colle : le stigmate.", "Mâle : étamines ; femelle : pistil."]},
      cm1=assoc([("les pétales", "attirent les insectes"), ("les étamines", "fabriquent le pollen"), ("le pistil", "contient les ovules")]),
      cm2=assoc([("les pétales", "attirent les insectes"), ("les sépales", "protègent le bouton"), ("les étamines", "fabriquent le pollen : organes mâles"),
                 ("le pistil", "contient les ovules : organe femelle"), ("le stigmate", "retient le pollen, car il est collant")]),
      lecon="fleur"),
    E("1-3", "Le carnet d'observation", "vraifaux",
      {"cm1": "Basile relit le carnet d'observation de la serre. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Basile corrige les phrases du carnet avant la visite des écoles. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + FLEUR,
      "La fleur sert à la reproduction de la plante. Le pollen est fabriqué par les étamines, pas par les pétales. Les ovules sont dans le pistil. En CM2 : beaucoup de fleurs ont à la fois des étamines et un pistil, mais le noisetier a des fleurs mâles et des fleurs femelles séparées ; pour observer une fleur, on la dissèque de l'extérieur vers le centre.",
      {"cm1": ["À quoi sert une fleur pour la plante ?", "Le pollen vient d'une pièce mâle.", "Le centre de la fleur cache les ovules."],
       "cm2": ["Pense au noisetier.", "Disséquer : de l'extérieur vers le centre.", "Mâle : étamines."]},
      cm1=vf([("La fleur sert à la reproduction de la plante.", True, "C'est son organe de reproduction."),
              ("Le pollen est fabriqué par les pétales.", False, "Il est fabriqué par les étamines."),
              ("Les ovules se trouvent dans le pistil.", True, "Dans l'ovaire, en bas du pistil.")]),
      cm2=vf([("Les étamines sont les organes femelles de la fleur.", False, "Ce sont les organes mâles."),
              ("L'ovaire est la partie renflée du pistil.", True, "Il contient les ovules."),
              ("Toutes les fleurs ont à la fois des étamines et un pistil.", False, "Le noisetier a des fleurs mâles et des fleurs femelles séparées."),
              ("Pour disséquer une fleur, on détache ses pièces de l'extérieur vers le centre.", True, "Sépales, pétales, étamines, puis pistil."),
              ("Le stigmate est collant.", True, "Il retient le pollen.")]),
      lecon="fleur"),
    E("1-4", "L'étiquette égarée", "intrus",
      "Sur la table de dissection, Basile a regroupé les pièces femelles de la fleur. Une étiquette s'est glissée par erreur dans le groupe : trouve l'intrus.",
      BO + " ; " + FLEUR,
      "Le pistil, l'ovaire, les ovules et le stigmate appartiennent à l'organe femelle de la fleur. L'étamine est un organe mâle : elle fabrique le pollen.",
      {"cm2": ["Les ovules sont dans l'organe femelle.", "Le stigmate est le haut du pistil.", "Qui fabrique le pollen ?"]},
      commun=intrus([("le pistil", False), ("l'ovaire", False), ("les ovules", False), ("le stigmate", False), ("l'étamine", True)]),
      lecon="fleur", cm2_seul=True),
]})

# =================================================================== SALLE 2 — le rucher (Capucine, apicultrice)
S.append({"num": 2, "titre": "Le rucher — Pollinisation et fécondation", "enigmes": [
    E("2-1", "Le voyage du pollen", "ordre",
      {"cm1": "Capucine a dessiné le voyage du pollen pour les visiteurs, mais ses cartes sont mélangées. Remets les étapes dans l'ordre.",
       "cm2": "Capucine prépare le panneau « De la fleur au fruit » du rucher. Remets les étapes dans l'ordre."},
      BO + " ; " + LAMAP_CYCLE,
      "Une abeille vient boire le nectar d'une fleur et se couvre de pollen ; elle vole vers une autre fleur de la même espèce ; le pollen se dépose sur le pistil ; l'ovaire grossit et devient un fruit qui contient des graines. En CM2 : le pollen déposé sur le stigmate permet de féconder les ovules ; après la fécondation, les pétales fanent, l'ovaire devient le fruit et les ovules deviennent les graines.",
      {"cm1": ["Tout commence par la visite d'une abeille.", "Le pollen voyage avant de se déposer.", "Le fruit arrive à la fin."],
       "cm2": ["La fécondation suit la pollinisation.", "Les pétales fanent après la fécondation.", "Ovaire : fruit ; ovules : graines."]},
      cm1=ordre(["Une abeille boit le nectar d'une fleur et se couvre de pollen.", "L'abeille vole vers une autre fleur de la même espèce.",
                 "Le pollen se dépose sur le pistil.", "L'ovaire grossit et devient un fruit qui contient des graines."]),
      cm2=ordre([("Une abeille se couvre du pollen des étamines.", "en buvant le nectar"), ("Elle dépose ce pollen sur le stigmate d'une autre fleur.", "c'est la pollinisation"),
                 ("Le pollen permet de féconder les ovules.", "c'est la fécondation"), ("Les pétales et les étamines fanent et tombent.", "ils ne servent plus"),
                 ("L'ovaire devient le fruit, les ovules deviennent les graines.", "le fruit mûrit")]),
      lecon="pollen"),
    E("2-2", "Le cahier du rucher", "trous",
      {"cm1": "La pluie a effacé des mots dans le cahier de Capucine. Remets chaque mot à sa place.",
       "cm2": "Complète la page du cahier du rucher avec les mots qui manquent."},
      BO + " ; " + POLLIN,
      "La pollinisation est le transport du pollen des étamines jusqu'au pistil. Les abeilles viennent boire le nectar et transportent le pollen. Après la fécondation, l'ovaire devient le fruit et les ovules deviennent les graines.",
      {"cm1": ["Le pollen part des étamines.", "Les abeilles boivent un liquide sucré.", "Que devient l'ovaire ?"],
       "cm2": ["Pollinisation, puis fécondation.", "Le fruit vient de l'ovaire.", "Les graines viennent des ovules."]},
      cm1=trous("La [[pollinisation]] est le transport du pollen jusqu'au pistil. Les abeilles viennent boire le [[nectar]] des fleurs. Plus tard, la fleur devient un [[fruit]].",
                ["pollinisation", "nectar", "fruit"]),
      cm2=trous("La pollinisation est le transport du [[pollen]] des [[étamines]] jusqu'au pistil d'une fleur de la même espèce. Le pollen permet ensuite de [[féconder]] les ovules. Après la fécondation, l'[[ovaire]] grossit et devient le fruit, et les [[ovules]] deviennent les graines.",
                ["pollen", "étamines", "féconder", "ovaire", "ovules"]),
      lecon="pollen"),
    E("2-3", "Les ruches et le vent", "tri",
      {"cm1": "Capucine veut poser ses ruches près des plantes qui ont besoin des insectes. Range chaque plante : pollinisée par les insectes ou par le vent ?",
       "cm2": "Range chaque plante selon la façon dont son pollen voyage : par les insectes ou par le vent."},
      BO + " ; " + POLLIN,
      "Le pommier, le cerisier et le tournesol ont de grandes fleurs colorées et du nectar : les insectes les pollinisent. Le maïs, le noisetier et les graminées des prairies ont des fleurs discrètes et beaucoup de pollen : le vent les pollinise. En CM2 : le fraisier et la courgette sont pollinisés par les insectes ; le bouleau, par le vent.",
      {"cm1": ["Des fleurs colorées attirent les insectes.", "Le noisetier lâche des nuages de pollen.", "Le maïs n'a pas de pétales colorés."],
       "cm2": ["Pétales colorés et nectar : insectes.", "Fleurs discrètes, pollen abondant : vent.", "Le bouleau fait éternuer au printemps."]},
      cm1=tri([("ins", "Pollinisée par les insectes"), ("vent", "Pollinisée par le vent")],
              [("le pommier", "ins"), ("le cerisier", "ins"), ("le tournesol", "ins"), ("le maïs", "vent"), ("le noisetier", "vent"), ("les graminées des prairies", "vent")]),
      cm2=tri([("ins", "Pollinisée par les insectes"), ("vent", "Pollinisée par le vent")],
              [("le pommier", "ins"), ("le cerisier", "ins"), ("le fraisier", "ins"), ("la courgette", "ins"),
               ("le maïs", "vent"), ("le noisetier", "vent"), ("le bouleau", "vent"), ("les graminées des prairies", "vent")]),
      lecon="pollen"),
    E("2-4", "Le panneau des pollinisateurs", "qcm",
      "Capucine écrit un panneau pour expliquer aux agriculteurs voisins pourquoi il faut protéger les abeilles. Choisis la bonne réponse.",
      BO + " ; " + POLLIN,
      "La pollinisation est une coopération : l'insecte se nourrit de nectar et de pollen, et la plante est fécondée. Après la fécondation, l'ovaire devient le fruit. Quand on utilise beaucoup d'insecticides, les pollinisateurs deviennent moins nombreux et certaines cultures donnent moins de fruits et de graines.",
      {"cm2": ["Chacun y gagne quelque chose.", "Moins d'abeilles, moins de pollinisation.", "Le fruit vient de l'ovaire."]},
      commun=qcm([("Pourquoi dit-on que la pollinisation est une coopération ?", ["l'abeille et la fleur y gagnent toutes les deux", "seule l'abeille y gagne", "seule la fleur y gagne", "aucune des deux n'y gagne"], 0, "Nourriture pour l'insecte, fécondation pour la plante."),
                  ("Que se passe-t-il si les pollinisateurs deviennent rares dans un verger ?", ["il y a plus de fruits", "il y a moins de fruits", "rien ne change", "les arbres fleurissent davantage"], 1, "Moins de fleurs sont pollinisées."),
                  ("Quel produit peut rendre les pollinisateurs moins nombreux ?", ["l'eau de pluie", "le compost", "les insecticides", "le paillage"], 2, "Ils tuent aussi les insectes utiles."),
                  ("Que devient l'ovaire après la fécondation ?", ["une feuille", "le fruit", "une racine", "un pétale"], 1, "Et les ovules deviennent les graines.")]),
      lecon="pollen", cm2_seul=True),
]})

# =================================================================== SALLE 3 — le potager (Tom, jeune jardinier)
S.append({"num": 3, "titre": "Le potager de l'école — Graines et germination", "enigmes": [
    E("3-1", "Les graines voyageuses", "tri",
      {"cm1": "Dans le potager, Tom a ramassé des graines qui viennent de loin. Range chaque graine selon ce qui l'a transportée.",
       "cm2": "Tom classe sa collection de fruits et de graines selon leur moyen de dispersion. Range chaque carte."},
      BO + " ; " + CYCLE2 + " ; " + LAMAP_CYCLE,
      "Les graines du pissenlit (aigrettes) et de l'érable (ailes) sont emportées par le vent. Les fruits de la bardane s'accrochent aux poils des animaux ; les glands sont cachés par le geai et parfois oubliés. La noix de coco flotte sur l'eau. En CM2 : le tilleul a des fruits munis d'une aile (vent) ; les oiseaux mangent les cerises et rejettent le noyau plus loin (animaux) ; les graines de l'aulne flottent sur l'eau.",
      {"cm1": ["Une aigrette, c'est un petit parachute.", "Un crochet s'accroche aux poils.", "La noix de coco flotte."],
       "cm2": ["Une aile tourne dans le vent.", "Un fruit mangé voyage dans un oiseau.", "L'aulne pousse au bord des rivières."]},
      cm1=tri([("vent", "Le vent"), ("ani", "Les animaux"), ("eau", "L'eau")],
              [("le pissenlit", "vent"), ("l'érable", "vent"), ("la bardane", "ani"), ("le gland du chêne", "ani"), ("la noix de coco", "eau")]),
      cm2=tri([("vent", "Le vent"), ("ani", "Les animaux"), ("eau", "L'eau")],
              [("le pissenlit", "vent"), ("l'érable", "vent"), ("le tilleul", "vent"), ("la bardane", "ani"), ("le gland du chêne", "ani"),
               ("la cerise", "ani"), ("la noix de coco", "eau"), ("l'aulne", "eau")]),
      lecon="graines"),
    E("3-2", "L'expérience des quatre pots", "qcm",
      {"cm1": "Tom a fait une expérience avec des haricots. Lis son tableau, puis réponds aux questions." + POTS,
       "cm2": "Lis le tableau de l'expérience de Tom, puis réponds aux questions." + POTS},
      BO + " ; " + LAMAP_GERME + " ; " + CYCLE2,
      "Seuls les pots B et D ont germé : ils avaient de l'eau et une température douce. Le pot A (sans eau) et le pot C (trop froid) n'ont pas germé. Le pot D, dans le noir, a germé : la plupart des graines n'ont pas besoin de lumière pour germer. En CM2 : une bonne expérience ne change qu'une seule chose à la fois ; après la germination, la jeune plante aura besoin de lumière pour grandir.",
      {"cm1": ["Compare A et B : qu'est-ce qui change ?", "Le réfrigérateur est très froid.", "Le placard noir n'a pas de lumière."],
       "cm2": ["Une seule différence entre deux pots.", "D a germé sans lumière.", "Pour grandir ensuite, il faut de la lumière."]},
      cm1=qcm([("Pourquoi le pot A n'a-t-il pas germé ?", ["il manquait de l'eau", "il manquait de la lumière", "il faisait trop chaud", "les graines étaient trop grosses"], 0, "Le coton était sec."),
               ("Pourquoi le pot C n'a-t-il pas germé ?", ["il avait trop d'eau", "il faisait trop froid", "il était dans le noir", "il n'avait pas de terre"], 1, "Le réfrigérateur est trop froid."),
               ("Le pot D, dans le noir, a germé. Qu'en conclut Tom ?", ["la graine a besoin de lumière pour germer", "la graine n'a pas besoin de lumière pour germer", "le noir tue les graines", "la graine a besoin de terre"], 1, "Elle a germé sans lumière.")]),
      cm2=qcm([("Quels pots montrent que la graine a besoin d'eau ?", ["A et B", "B et D", "C et D", "A et C"], 0, "Seule l'eau change entre A et B."),
               ("Quels pots montrent qu'il faut une température douce ?", ["A et D", "B et C", "A et B", "B et D"], 1, "Seule la température change entre B et C."),
               ("Que montrent les pots B et D ?", ["la lumière est indispensable pour germer", "la plupart des graines germent même dans le noir", "le placard fait pousser plus vite", "il faut de la terre"], 1, "D a germé dans le noir."),
               ("Après la germination, de quoi la jeune plante aura-t-elle besoin pour grandir ?", ["de lumière", "de froid", "de noir complet", "de rien du tout"], 0, "La plante fabrique sa nourriture à la lumière.")]),
      lecon="graines"),
    E("3-3", "Le cycle du haricot", "ordre",
      {"cm1": "Tom raconte la vie de son haricot sur une grande affiche. Remets les étapes dans l'ordre.",
       "cm2": "Tom affiche le cycle de vie complet d'une plante à fleurs. Remets les étapes dans l'ordre, en partant de la graine."},
      BO + " ; " + CYCLE2 + " ; " + LAMAP_CYCLE,
      "La graine germe, la jeune plante grandit, elle fleurit, la fleur devient un fruit qui contient des graines. En CM2 : entre la floraison et le fruit, il faut la pollinisation et la fécondation ; à la fin, les graines sont dispersées et le cycle recommence.",
      {"cm1": ["On part de la graine.", "Les fleurs viennent avant les fruits.", "Le fruit contient de nouvelles graines."],
       "cm2": ["La germination vient juste après la graine.", "Pollinisation avant fruit.", "La dispersion termine le cycle."]},
      cm1=ordre(["La graine germe.", "La jeune plante grandit.", "La plante fleurit.", "La fleur devient un fruit qui contient des graines."]),
      cm2=ordre([("La graine germe.", "racine, puis tige et feuilles"), ("La plante grandit à la lumière.", "elle fabrique sa nourriture"),
                 ("La plante fleurit.", "étamines et pistil"), ("Les fleurs sont pollinisées et fécondées.", "grâce aux insectes ou au vent"),
                 ("Les fruits mûrissent.", "ils contiennent des graines"), ("Les graines sont dispersées.", "le cycle recommence")]),
      lecon="graines"),
    E("3-4", "La graine ouverte", "association",
      "Tom a ouvert une graine de haricot trempée dans l'eau. Relie chaque partie de la graine, ou chaque besoin, à son rôle.",
      BO + " ; " + LAMAP_GERME,
      "L'enveloppe protège la graine ; l'embryon est la future plante ; les réserves nourrissent la jeune plante au début ; l'eau réveille la graine ; la lumière servira ensuite à la jeune plante pour grandir.",
      {"cm2": ["L'embryon est une plante miniature.", "Les réserves sont comme un goûter.", "La lumière sert après la germination."]},
      commun=assoc([("l'enveloppe", "protège la graine"), ("l'embryon", "est la future plante"), ("les réserves", "nourrissent la jeune plante au début"),
                    ("l'eau", "réveille la graine pour la germination"), ("la lumière", "sert ensuite à la jeune plante pour grandir")]),
      lecon="graines", cm2_seul=True),
]})

# =================================================================== SALLE 4 — la basse-cour (Yasmine, éleveuse)
S.append({"num": 4, "titre": "La ferme des Coteaux — La fécondation chez les animaux", "enigmes": [
    E("4-1", "Les questions de la ferme", "qcm",
      {"cm1": "À la ferme voisine, Yasmine répond aux questions des visiteurs. Aide-la à choisir la bonne réponse.",
       "cm2": "Yasmine prépare le quiz de la ferme pédagogique. Choisis la bonne réponse."},
      BO + " ; " + LUMNI,
      "Chez les animaux, pour avoir des petits, il faut en général un mâle et une femelle de la même espèce. La fécondation est la rencontre d'une cellule reproductrice mâle et d'une cellule reproductrice femelle. En CM2 : ces cellules s'appellent les gamètes ; chez les oiseaux et les mammifères, la fécondation est interne ; chez la grenouille, elle est externe, dans l'eau.",
      {"cm1": ["Il faut deux parents.", "Mâle et femelle de la même espèce.", "Fécondation : une rencontre."],
       "cm2": ["Les gamètes sont des cellules reproductrices.", "Oiseaux et mammifères : interne.", "La grenouille pond dans l'eau."]},
      cm1=qcm([("Pour que la poule ait des poussins, il faut…", ["seulement une poule", "un coq et une poule", "un coq et une cane", "deux poules"], 1, "Un mâle et une femelle de la même espèce."),
               ("Qu'est-ce que la fécondation ?", ["la naissance du petit", "la rencontre d'une cellule mâle et d'une cellule femelle", "la ponte de l'œuf", "la croissance du petit"], 1, "Elle donne la première cellule du petit."),
               ("Le mâle de la brebis s'appelle…", ["le bouc", "le bélier", "le taureau", "le jars"], 1, "Le bouc est le mâle de la chèvre.")]),
      cm2=qcm([("Comment appelle-t-on les cellules reproductrices ?", ["les gamètes", "les graines", "les embryons", "les larves"], 0, "Gamète mâle et gamète femelle."),
               ("Que donne la fécondation ?", ["un adulte", "la première cellule d'un nouvel être vivant", "un œuf dur", "deux parents"], 1, "C'est le début de l'embryon."),
               ("Chez la vache, la fécondation est…", ["externe, dans l'eau", "interne, dans le corps de la femelle", "faite par les abeilles", "inutile"], 1, "C'est un mammifère."),
               ("Chez la grenouille, la fécondation a lieu…", ["dans le corps de la femelle", "dans l'eau, hors du corps", "dans un nid sec", "dans la terre"], 1, "Elle est externe.")]),
      lecon="fecondation"),
    E("4-2", "Le registre de la ferme", "tri",
      {"cm1": "Yasmine remplit le registre des animaux de la ferme et de l'étang. Range chaque animal : fécondation dans le corps de la femelle, ou dehors, dans l'eau ?",
       "cm2": "Range chaque animal du registre selon son type de fécondation : interne ou externe."},
      BO + " ; " + LUMNI,
      "La poule, la vache et le lapin ont une fécondation interne, dans le corps de la femelle. La grenouille et la truite ont une fécondation externe, dans l'eau. En CM2 : la tortue et la cane, qui pondent pourtant des œufs, ont une fécondation interne ; le crapaud et le saumon ont une fécondation externe.",
      {"cm1": ["Les oiseaux : dans le corps.", "Les mammifères : dans le corps.", "Dans l'étang, les œufs sont fécondés dans l'eau."],
       "cm2": ["Pondre des œufs ne veut pas dire fécondation externe.", "La tortue est un reptile.", "Le crapaud pond dans les mares."]},
      cm1=tri([("int", "Dans le corps de la femelle"), ("ext", "Dehors, dans l'eau")],
              [("la poule", "int"), ("la vache", "int"), ("le lapin", "int"), ("la grenouille", "ext"), ("la truite", "ext")]),
      cm2=tri([("int", "Fécondation interne"), ("ext", "Fécondation externe")],
              [("la poule", "int"), ("la vache", "int"), ("la tortue", "int"), ("la cane", "int"),
               ("la grenouille", "ext"), ("la truite", "ext"), ("le crapaud", "ext"), ("le saumon", "ext")]),
      lecon="fecondation"),
    E("4-3", "L'intrus de l'enclos", "intrus",
      {"cm1": "Yasmine a regroupé les animaux dont la fécondation a lieu dans le corps de la femelle. Un animal s'est glissé dans le groupe : trouve l'intrus.",
       "cm2": "Toutes ces phrases parlent de la fécondation interne, sauf une. Trouve l'intrus."},
      BO + " ; " + LUMNI,
      "La poule, la chèvre, le cheval et la lapine ont une fécondation interne. La grenouille a une fécondation externe : ses ovules sont fécondés dans l'eau. En CM2 : la phrase « Les ovules sont pondus dans l'eau avant d'être fécondés » décrit une fécondation externe.",
      {"cm1": ["Quel animal vit dans la mare ?", "Les mammifères : fécondation interne.", "La poule aussi."],
       "cm2": ["Interne : dans le corps.", "Une phrase parle de l'eau.", "Pondre avant de féconder : dehors."]},
      cm1=intrus([("la poule", False), ("la chèvre", False), ("le cheval", False), ("la lapine", False), ("la grenouille", True)]),
      cm2=intrus([("Le gamète mâle rejoint le gamète femelle dans le corps de la femelle.", False), ("Elle existe chez les oiseaux.", False),
                  ("Elle existe chez les mammifères.", False), ("Elle existe aussi chez les tortues.", False),
                  ("Les ovules sont pondus dans l'eau avant d'être fécondés.", True)]),
      lecon="fecondation"),
    E("4-4", "Les panneaux de l'étang", "vraifaux",
      "Yasmine relit les panneaux de l'étang de la ferme. Pour chaque phrase, choisis vrai ou faux.",
      BO + " ; " + LUMNI,
      "La fécondation externe se fait dans l'eau, car les cellules reproductrices ne survivraient pas à l'air libre. Les animaux à fécondation externe pondent souvent un très grand nombre d'œufs. Un mâle et une femelle d'espèces différentes, comme un coq et une cane, n'ont pas de petits ensemble.",
      {"cm2": ["Les cellules reproductrices sèchent à l'air.", "Beaucoup d'œufs, car beaucoup seront mangés.", "Même espèce pour avoir des petits."]},
      commun=vf([("La fécondation externe se fait dans l'eau.", True, "Les cellules reproductrices ne survivraient pas à l'air libre."),
                 ("Une grenouille pond seulement un ou deux œufs.", False, "Elle en pond un très grand nombre."),
                 ("Un coq et une cane peuvent avoir des petits ensemble.", False, "Ils ne sont pas de la même espèce."),
                 ("Chez le canard, la fécondation est interne.", True, "Comme chez tous les oiseaux."),
                 ("La fécondation donne la première cellule d'un nouvel être vivant.", True, "C'est le début de l'embryon.")]),
      lecon="fecondation", cm2_seul=True),
]})

# =================================================================== SALLE 5 — la mare et la bergerie (Nadia, vétérinaire)
S.append({"num": 5, "titre": "La bergerie et la mare — Naître ou éclore", "enigmes": [
    E("5-1", "Les nids et la bergerie", "tri",
      {"cm1": "Nadia, la vétérinaire, fait sa tournée du printemps. Range chaque animal : ses petits sortent d'un œuf pondu, ou naissent du ventre de leur mère ?",
       "cm2": "Range chaque animal de la tournée de Nadia : ovipare ou vivipare ?"},
      BO + " ; " + LUMNI,
      "La poule, la tortue et la grenouille pondent des œufs : elles sont ovipares. La vache, la brebis et la lapine portent leur petit dans leur ventre : elles sont vivipares. En CM2 : la truite et le papillon sont ovipares ; le dauphin et la chauve-souris sont des mammifères vivipares, même si l'un vit dans l'eau et l'autre vole.",
      {"cm1": ["Un nid, c'est pour des œufs.", "L'agneau naît du ventre de la brebis.", "La grenouille pond dans la mare."],
       "cm2": ["Ovipare : qui pond des œufs.", "Le dauphin allaite son petit.", "La chauve-souris est un mammifère."]},
      cm1=tri([("ovi", "Sort d'un œuf pondu"), ("vivi", "Naît du ventre de sa mère")],
              [("la poule", "ovi"), ("la tortue", "ovi"), ("la grenouille", "ovi"), ("la vache", "vivi"), ("la brebis", "vivi"), ("la lapine", "vivi")]),
      cm2=tri([("ovi", "Ovipare"), ("vivi", "Vivipare")],
              [("la poule", "ovi"), ("la tortue", "ovi"), ("la truite", "ovi"), ("le papillon", "ovi"),
               ("la vache", "vivi"), ("la brebis", "vivi"), ("le dauphin", "vivi"), ("la chauve-souris", "vivi")]),
      lecon="naitre"),
    E("5-2", "Le carnet de la vétérinaire", "vraifaux",
      {"cm1": "Nadia relit les phrases de son carnet. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Nadia vérifie les fiches de la ferme. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + LUMNI,
      "Un petit appartient toujours à la même espèce que ses parents. Les petits ressemblent à leurs parents sans être identiques. L'œuf de poule contient un embryon et des réserves. En CM2 : une fécondation externe va toujours avec la ponte d'œufs ; une fécondation interne peut aller avec la ponte (poule) ou avec la naissance (vache) ; une espèce est un ensemble d'êtres vivants qui peuvent se reproduire entre eux.",
      {"cm1": ["Un agneau naît d'une brebis.", "Regarde les agneaux du troupeau.", "Le jaune nourrit l'embryon."],
       "cm2": ["Interne ne veut pas dire vivipare.", "Externe : toujours des œufs.", "Espèce : qui peuvent se reproduire entre eux."]},
      cm1=vf([("Un agneau appartient à la même espèce que ses parents.", True, "Il naît d'une brebis et d'un bélier."),
              ("Les agneaux sont tous exactement identiques à leurs parents.", False, "Ils se ressemblent, mais chacun est unique."),
              ("Dans l'œuf fécondé de la poule, l'embryon trouve des réserves de nourriture.", True, "Le jaune.")]),
      cm2=vf([("Tous les animaux à fécondation interne sont vivipares.", False, "La poule a une fécondation interne et pond des œufs."),
              ("Une fécondation externe va toujours avec la ponte d'œufs.", True, "Les ovules sont pondus puis fécondés dans l'eau."),
              ("Une espèce est un ensemble d'êtres vivants qui peuvent se reproduire entre eux.", True, "C'est la définition du programme."),
              ("Deux agneaux des mêmes parents sont toujours identiques.", False, "Chaque individu est unique."),
              ("Une partie des différences entre individus est héritée des parents.", True, "C'est une richesse pour l'espèce.")]),
      lecon="naitre"),
    E("5-3", "De l'œuf au petit", "ordre",
      {"cm1": "Nadia montre aux élèves comment naît un poussin. Remets les étapes dans l'ordre.",
       "cm2": "À la mare, Nadia observe le développement des grenouilles. Remets les étapes dans l'ordre."},
      BO + " ; " + FAO + " ; " + LUMNI,
      "Chez la poule : la fécondation a lieu dans le corps de la poule, elle pond l'œuf, elle le couve pendant que l'embryon se développe (environ 21 jours), le poussin sort de l'œuf (éclosion), puis il grandit. En CM2, chez la grenouille : les ovules sont pondus dans l'eau et fécondés par le mâle, l'embryon se développe dans l'œuf, une larve, le têtard, sort de l'œuf, des pattes lui poussent, puis il devient une jeune grenouille qui quitte l'eau.",
      {"cm1": ["La fécondation vient en premier.", "Pendant la couvaison, l'embryon grandit.", "L'éclosion vient avant la croissance."],
       "cm2": ["Tout commence dans l'eau.", "Le têtard est la larve.", "Les pattes poussent avant de quitter l'eau."]},
      cm1=ordre(["La fécondation a lieu dans le corps de la poule.", "La poule pond l'œuf.", "La poule couve : l'embryon se développe dans l'œuf.",
                 "Le poussin sort de l'œuf : c'est l'éclosion.", "Le poussin grandit et devient une poule ou un coq."]),
      cm2=ordre([("Les ovules sont pondus dans l'eau et fécondés par le mâle.", "fécondation externe"), ("L'embryon se développe dans l'œuf.", "dans la mare"),
                 ("Le têtard sort de l'œuf.", "c'est une larve"), ("Des pattes poussent au têtard.", "sa queue raccourcit"),
                 ("La jeune grenouille quitte l'eau.", "elle grandira jusqu'à l'âge adulte")]),
      lecon="naitre"),
    E("5-4", "Le portail du jardin", "code",
      "Le portail entre la ferme et le jardin est fermé par un cadenas à trois nombres. Retrouve-les dans les fiches, et le jardin refleurira." + CARNET_NADIA,
      BO + " ; " + FAO,
      "L'œuf de poule éclot après environ 21 jours de couvaison ; le veau naît après environ 9 mois ; l'agneau après environ 5 mois. Le code est 21, 9, 5.",
      {"cm2": ["Fiche « Naître ou éclore » : « Combien de temps ? ».", "La poule couve trois semaines.", "La brebis porte son agneau moins longtemps que la vache."]},
      commun=code([("Jours de couvaison", "21"), ("Mois pour un veau", "9"), ("Mois pour un agneau", "5")]),
      lecon="naitre", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "Le Jardin de la vie", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": " ; ".join([BO, CYCLE2, LAMAP_CYCLE, LAMAP_GERME, FLEUR, POLLIN, FAO, LUMNI]) + ". Détail : README.md, section Sources.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-1\",\"legende\":\"…\",\"source\":\"…\"}. Les schémas (fleur en coupe, de la fleur au fruit, cycle de vie, fécondation, œuf, grenouille) sont dessinés en SVG par script : ne jamais les remplacer par des images générées par IA. Plantes et animaux réels : photos Wikimedia Commons."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
