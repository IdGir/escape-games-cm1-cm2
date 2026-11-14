# -*- coding: utf-8 -*-
"""Génère naissances-animaux/assets/data/enigmes.json (La Nurserie du zoo). Lancer : python gen_enigmes.py <dossier data>
Vigilance : pas de reproduction humaine ; les exceptions (ornithorynque, vipère, requins) restent des exceptions ; pas de vidéo de naissance.
Zoo et personnages inventés."""
import json, os, sys
from schemas import schema_fecondation, coupe_oeuf

BO = "Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026), CM1, « Les êtres vivants dans leur environnement » : reproduction, croissance et développement (progression de l'enseignant : année B, période 3)"
LAMAP = "Fondation La main à la pâte, « Biologie animale : fonctions de reproduction »"
LAMAP_SEQ = "Fondation La main à la pâte, séquence « Et ils eurent beaucoup d'enfants »"
MNHN = "Muséum national d'histoire naturelle et INPN (fiches espèces)"
POUSSIN = "Écolothèque de Montpellier Méditerranée Métropole, « Naissance d'un poussin »"
GESTA = "Techno-Science, glossaire « Gestation » (durées moyennes)"
REQUINS = "Futura Sciences, « Pourquoi certains requins pondent-ils des œufs ? »"
LUMNI = "Lumni, vidéos « La reproduction des animaux » (cycle 3)"

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


def tableau(titre, entetes, lignes):
    h = "".join(f"<th>{x}</th>" for x in entetes)
    c = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in l) + "</tr>" for l in lignes)
    return f"<div class='doc-titre'><i>{titre}</i></div><table class='tableau-releves'><tr>{h}</tr>{c}</table>"



S = []
# =================================================================== SALLE 1 — le laboratoire de la vétérinaire (Inès)
S.append({"num": 1, "titre": "Le laboratoire de la vétérinaire — La fécondation", "enigmes": [
    E("1-1", "Le schéma du microscope", "plan",
      {"cm1": "Inès a dessiné au tableau ce qui se passe avant qu'un petit commence à grandir, mais les étiquettes sont tombées. Place chaque nom sur son repère : clique sur une étiquette, puis sur la case du repère." + schema_fecondation(3, "Le schéma d'Inès"),
       "cm2": "Inès a dessiné au tableau comment commence la vie d'un animal. Place chaque nom sur son repère. Attention : il y a des étiquettes en trop." + schema_fecondation(5, "Le schéma d'Inès")},
      BO + " ; " + LAMAP,
      "Sur ce dessin, la petite cellule qui nage est la cellule du mâle (repère 1) et la grosse cellule est celle de la femelle (repère 2) ; leur union donne la cellule-œuf (repère 3). En CM2, on emploie les mots spermatozoïde et ovule ; la cellule-œuf se divise et devient un embryon (repère 4) ; le repère 5 montre le flagelle qui fait avancer le spermatozoïde.",
      {"cm1": ["La cellule du mâle est la plus petite : elle a une queue.", "La cellule de la femelle est grosse et ronde.", "L'œuf est la toute première cellule du petit."],
       "cm2": ["Le spermatozoïde est minuscule et mobile.", "L'embryon est fait de plusieurs cellules.", "Le placenta et la coquille ne sont pas sur ce dessin."]},
      cm1={"titre": "Le schéma d'Inès", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "cellule du mâle"}, {"libelle": "Repère 2", "reponse": "cellule de la femelle"}, {"libelle": "Repère 3", "reponse": "œuf"}],
           "etiquettes": ["cellule du mâle", "cellule de la femelle", "œuf"]},
      cm2={"titre": "Le schéma d'Inès", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "spermatozoïde"}, {"libelle": "Repère 2", "reponse": "ovule"}, {"libelle": "Repère 3", "reponse": "cellule-œuf"},
                     {"libelle": "Repère 4", "reponse": "embryon"}, {"libelle": "Repère 5", "reponse": "flagelle"}],
           "etiquettes": ["spermatozoïde", "ovule", "cellule-œuf", "embryon", "flagelle", "placenta", "coquille"]},
      lecon="fecondation"),
    E("1-2", "Les notes d'Inès", "vraifaux",
      {"cm1": "Inès a écrit des phrases sur ses fiches, mais un stagiaire en a recopié certaines de travers. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Inès relit les notes d'un stagiaire. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + LAMAP + " ; " + LUMNI,
      "Un petit commence avec la rencontre d'une cellule du mâle et d'une cellule de la femelle : c'est la fécondation, qui donne l'œuf, première cellule du petit. Il faut donc un mâle et une femelle. En CM2 : les spermatozoïdes sont produits par les testicules et les ovules par les ovaires ; l'ovule est bien plus gros que le spermatozoïde ; un œuf de poule acheté au magasin n'a pas été fécondé.",
      {"cm1": ["Il faut deux cellules différentes.", "La fécondation donne l'œuf.", "Un mâle seul ne suffit pas."],
       "cm2": ["Les ovules viennent des ovaires.", "Compare la taille des deux gamètes.", "Les œufs du magasin ne donnent pas de poussin."]},
      cm1=vf([("Un petit commence avec la rencontre d'une cellule du mâle et d'une cellule de la femelle.", True, "C'est la fécondation."),
              ("La fécondation donne un œuf, la première cellule du petit.", True, "Cet œuf grandit ensuite."),
              ("Un mâle peut avoir un petit tout seul, sans femelle.", False, "Il faut les deux cellules.")]),
      cm2=vf([("Les spermatozoïdes sont produits par les testicules du mâle.", True, "Les ovules, eux, viennent des ovaires."),
              ("L'ovule est beaucoup plus petit que le spermatozoïde.", False, "C'est l'inverse : l'ovule est une grosse cellule."),
              ("La cellule-œuf se divise et devient un embryon.", True, "Deux, quatre, puis des milliers de cellules."),
              ("Un œuf de poule acheté au magasin donnera un poussin si on le garde au chaud.", False, "Il n'a pas été fécondé."),
              ("Le spermatozoïde avance grâce à son flagelle.", True, "C'est sa « queue ».")]),
      lecon="fecondation"),
    E("1-3", "Les bocaux étiquetés", "association",
      {"cm1": "Dans l'armoire d'Inès, les étiquettes des bocaux se sont décollées. Relie chaque mot à sa définition.",
       "cm2": "Dans l'armoire d'Inès, les étiquettes des bocaux se sont décollées. Relie chaque mot à sa définition."},
      BO + " ; " + LAMAP,
      "La fécondation est la rencontre des deux cellules ; l'œuf est la première cellule du petit ; le mâle apporte une cellule minuscule et la femelle une grosse cellule. En CM2 : gamètes est le nom des cellules reproductrices, l'ovaire produit les ovules, le testicule les spermatozoïdes, et l'embryon est le petit qui commence à se former.",
      {"cm1": ["La fécondation, c'est une rencontre.", "L'œuf est la première cellule.", "La cellule du mâle est minuscule."],
       "cm2": ["Gamète est le nom commun aux deux cellules reproductrices.", "L'ovaire, c'est chez la femelle.", "L'embryon a déjà beaucoup de cellules."]},
      cm1=assoc([("la fécondation", "la rencontre de la cellule du mâle et de celle de la femelle"), ("l'œuf", "la première cellule du petit"),
                 ("la cellule du mâle", "une cellule minuscule qui nage")]),
      cm2=assoc([("les gamètes", "les cellules reproductrices"), ("l'ovaire", "produit les ovules"), ("le testicule", "produit les spermatozoïdes"),
                 ("la cellule-œuf", "la première cellule du futur animal"), ("l'embryon", "le petit qui commence à se former")]),
      lecon="fecondation"),
    E("1-4", "Du gamète à l'embryon", "ordre",
      "Inès prépare une affiche pour les visiteurs. Remets les étapes dans l'ordre.",
      BO + " ; " + LAMAP,
      "Le mâle produit des spermatozoïdes et la femelle des ovules ; un spermatozoïde rencontre un ovule et s'unit à lui : c'est la fécondation ; elle donne une cellule-œuf, qui se divise en deux, puis en quatre, puis en des milliers de cellules : c'est un embryon.",
      {"cm2": ["On commence par la fabrication des gamètes.", "La rencontre vient avant la cellule-œuf.", "L'embryon arrive en dernier."]},
      commun=ordre(["Le mâle produit des spermatozoïdes, la femelle des ovules.", "Un spermatozoïde rencontre un ovule.", "Ils s'unissent : c'est la fécondation.",
                    "Une cellule-œuf est formée.", "La cellule-œuf se divise : elle devient un embryon."]),
      lecon="fecondation", cm2_seul=True),
]})

# =================================================================== SALLE 2 — l'aquarium et la mare (Théo)
S.append({"num": 2, "titre": "L'aquarium et la mare — Fécondation externe et interne", "enigmes": [
    E("2-1", "Les fiches de la mare", "tri",
      {"cm1": "Théo range les fiches des animaux. Pour chacun, où se rencontrent les cellules du mâle et de la femelle : dans l'eau, ou dans le corps de la femelle ?",
       "cm2": "Théo range les fiches des animaux selon leur type de fécondation. Place chaque animal dans la bonne colonne. Attention aux pièges."},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "La grenouille, le crapaud, la truite et le saumon ont une fécondation externe : les cellules se rencontrent dans l'eau. La poule, le chat, la vache, le canard, le crocodile et le requin ont une fécondation interne, dans le corps de la femelle. En CM2, le canard et le requin vivent dans l'eau mais leur fécondation est interne.",
      {"cm1": ["La grenouille pond dans la mare.", "Les mammifères : dans le corps.", "Les oiseaux aussi : dans le corps."],
       "cm2": ["Vivre dans l'eau ne suffit pas.", "Le requin s'accouple.", "Le canard est un oiseau."]},
      cm1=tri([("ext", "Dans l'eau (fécondation externe)"), ("int", "Dans le corps de la femelle (fécondation interne)")],
              [("la grenouille", "ext"), ("la truite", "ext"), ("la poule", "int"), ("le chat", "int"), ("la vache", "int")]),
      cm2=tri([("ext", "Fécondation externe"), ("int", "Fécondation interne")],
              [("la grenouille", "ext"), ("le crapaud", "ext"), ("la truite", "ext"), ("le saumon", "ext"),
               ("le canard", "int"), ("le requin", "int"), ("le crocodile", "int"), ("la chatte", "int")]),
      lecon="externe"),
    E("2-2", "Les questions de Théo", "qcm",
      {"cm1": "Théo montre l'aquarium et la mare aux visiteurs. Réponds à ses questions.",
       "cm2": "Théo interroge les apprentis soigneurs devant l'aquarium. Choisis la bonne réponse."},
      BO + " ; " + LAMAP,
      "Chez la grenouille, la femelle pond ses ovules dans l'eau et le mâle y libère ses cellules : la fécondation est externe. Chez la poule, elle a lieu dans son corps : elle est interne. En CM2 : beaucoup de cellules se perdent dans l'eau, c'est pourquoi les femelles pondent des centaines d'ovules ; une fécondation interne suit un accouplement.",
      {"cm1": ["La grenouille pond dans la mare.", "La poule pond un œuf déjà fécondé.", "Externe veut dire dehors."],
       "cm2": ["Dans l'eau, beaucoup de cellules se perdent.", "Un accouplement, c'est quand le mâle et la femelle s'unissent.", "La tortue marine pond sur la plage."]},
      cm1=qcm([("Où a lieu la fécondation chez la grenouille ?", ["dans la mare", "dans le corps de la femelle", "dans un nid", "sur une feuille sèche"], 0, "Les cellules se rencontrent dans l'eau."),
               ("Chez la poule, la fécondation a lieu…", ["dans l'eau", "dans le corps de la poule", "dans le nid", "dans la coquille, après la ponte"], 1, "Elle est interne."),
               ("Que veut dire « fécondation externe » ?", ["à l'intérieur du corps", "hors du corps de la femelle", "dans un œuf", "la nuit"], 1, "Externe : dehors.")]),
      cm2=qcm([("Pourquoi une truite pond-elle des milliers d'ovules ?", ["pour les manger", "parce que beaucoup de gamètes se perdent dans l'eau", "parce qu'elle vit longtemps", "parce que l'eau est froide"], 1, "En fécondation externe, beaucoup de gamètes sont perdus."),
               ("Que se passe-t-il avant une fécondation interne ?", ["la ponte", "un accouplement", "une éclosion", "une mue"], 1, "Le mâle dépose ses spermatozoïdes dans le corps de la femelle."),
               ("La tortue marine vit dans la mer. Sa fécondation est…", ["externe", "interne", "impossible à savoir", "faite par le Soleil"], 1, "Vivre dans l'eau ne suffit pas."),
               ("Où se rencontrent les gamètes lors d'une fécondation externe ?", ["dans l'eau", "dans le ventre du mâle", "dans l'air", "dans la terre"], 0, "Le plus souvent dans l'eau.")]),
      lecon="externe"),
    E("2-3", "Le panneau de la mare", "trous",
      {"cm1": "Le panneau de la mare a été éclaboussé. Complète-le avec les bonnes étiquettes.",
       "cm2": "Le panneau de la mare a été éclaboussé. Complète-le. Attention : il y a des étiquettes en trop."},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "Au printemps, la grenouille femelle pond ses ovules dans l'eau ; le mâle y libère ses cellules : la fécondation est externe. Chez les oiseaux et les mammifères, elle a lieu dans le corps de la femelle : elle est interne. En CM2 : les gamètes perdus dans l'eau expliquent les pontes nombreuses ; les reptiles, les requins et les insectes ont aussi une fécondation interne.",
      {"cm1": ["La grenouille pond dans l'eau.", "Externe : dehors ; interne : dedans.", "Les mammifères : dans le corps."],
       "cm2": ["Les gamètes femelles sont les ovules.", "Beaucoup se perdent : il en faut beaucoup.", "Le requin s'accouple."]},
      cm1={"texte": "<p>Au printemps, la grenouille femelle pond ses ovules dans l'[[eau]]. Le mâle y libère ses cellules : la fécondation est [[externe]]. Chez le chat, la fécondation a lieu dans le [[corps]] de la femelle : elle est [[interne]].</p>",
           "etiquettes": ["eau", "externe", "corps", "interne"]},
      cm2={"texte": "<p>Au printemps, la grenouille femelle pond ses [[ovules]] dans l'eau, où le mâle libère ses [[spermatozoïdes]] : la fécondation est [[externe]]. Beaucoup de gamètes sont [[perdus]] : la femelle pond donc des centaines d'ovules. Chez les oiseaux, les mammifères et les [[requins]], les gamètes se rencontrent dans le corps de la femelle, après un [[accouplement]] : la fécondation est interne.</p>",
           "etiquettes": ["ovules", "spermatozoïdes", "externe", "perdus", "requins", "accouplement", "grenouilles", "placenta", "éclosion"]},
      lecon="externe"),
    E("2-4", "Le grand bassin", "intrus",
      "Théo a mis ensemble les fiches des animaux du grand bassin qui ont une fécondation externe. Une fiche n'a rien à faire là. Trouve l'intrus.",
      BO + " ; " + LAMAP + " ; " + MNHN,
      "La grenouille, la truite et le saumon ont une fécondation externe, dans l'eau. La tortue marine vit dans la mer, mais le mâle et la femelle s'accouplent : sa fécondation est interne, et elle va pondre sur une plage.",
      {"cm2": ["Tous ces animaux vivent dans l'eau.", "Cherche celui qui s'accouple.", "Il pond ses œufs sur le sable."]},
      commun=intrus([("la grenouille", False), ("la truite", False), ("la tortue marine", True), ("le saumon", False)]),
      lecon="externe", cm2_seul=True),
]})

# =================================================================== SALLE 3 — la galerie des surprises (Malo)
S.append({"num": 3, "titre": "La galerie des surprises — Ovipares et vivipares", "enigmes": [
    E("3-1", "La vitrine des pondeurs", "intrus",
      {"cm1": "Dans la vitrine des animaux qui pondent des œufs, Malo a glissé une fiche par erreur. Trouve l'intrus.",
       "cm2": "Dans la vitrine des mammifères, Malo a placé un animal qui étonne tous les visiteurs. Trouve celui qui ne fait pas comme les autres."},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "La poule, le crocodile et la tortue pondent des œufs : ils sont ovipares. Le chat ne pond pas : ses petits naissent vivants, il est vivipare. En CM2 : le lapin, la girafe et le dauphin sont des mammifères vivipares ; l'ornithorynque est un mammifère qui pond des œufs, une exception.",
      {"cm1": ["Ces animaux pondent des œufs.", "Un chaton naît-il d'un œuf ?", "Le crocodile pond sur la berge."],
       "cm2": ["Tous sont des mammifères.", "Lequel pond des œufs ?", "Il vit en Australie et a un bec."]},
      cm1=intrus([("la poule", False), ("le crocodile", False), ("le chat", True), ("la tortue", False)]),
      cm2=intrus([("le lapin", False), ("la girafe", False), ("l'ornithorynque", True), ("le dauphin", False), ("la vache", False)]),
      lecon="ovipares"),
    E("3-2", "Le tableau de la galerie", "tri",
      {"cm1": "Malo range les animaux de la galerie : ceux qui pondent des œufs (ovipares) et ceux dont le petit naît vivant (vivipares).",
       "cm2": "Malo complète le tableau à deux entrées de la galerie : type de fécondation et mode de reproduction. Place chaque animal dans la bonne case."},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "La poule, la grenouille, le papillon et le crocodile pondent : ils sont ovipares. La vache, le lapin et la girafe sont vivipares. En CM2 : la grenouille et la truite ont une fécondation externe et pondent ; la poule, le crocodile et le papillon ont une fécondation interne et pondent ; la girafe, le kangourou et le lion ont une fécondation interne et sont vivipares. Aucun animal n'a une fécondation externe et un petit qui grandit dans le ventre de sa mère.",
      {"cm1": ["Ovipare : qui pond des œufs.", "Les mammifères sont presque tous vivipares.", "Le papillon pond sur les feuilles."],
       "cm2": ["Commence par la fécondation : dans l'eau ou dans le corps ?", "Puis : ponte ou petit vivant ?", "La case « externe et vivipare » reste vide."]},
      cm1=tri([("ovi", "Ovipare (pond des œufs)"), ("vivi", "Vivipare (le petit naît vivant)")],
              [("la poule", "ovi"), ("la grenouille", "ovi"), ("le papillon", "ovi"), ("le crocodile", "ovi"),
               ("la vache", "vivi"), ("le lapin", "vivi"), ("la girafe", "vivi")]),
      cm2=tri([("ext-ovi", "Fécondation externe, ovipare"), ("int-ovi", "Fécondation interne, ovipare"), ("int-vivi", "Fécondation interne, vivipare")],
              [("la grenouille", "ext-ovi"), ("la truite", "ext-ovi"), ("la poule", "int-ovi"), ("le crocodile", "int-ovi"), ("le papillon", "int-ovi"),
               ("la girafe", "int-vivi"), ("le kangourou", "int-vivi"), ("le lion", "int-vivi")]),
      lecon="ovipares"),
    E("3-3", "Les surprises de Malo", "vraifaux",
      {"cm1": "Malo raconte les animaux étonnants de sa galerie. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Malo vérifie les panneaux des animaux étonnants. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + LAMAP + " ; " + MNHN + " ; " + REQUINS,
      "L'ornithorynque est un mammifère qui pond des œufs et nourrit ses petits avec son lait. Tous les poissons ne pondent pas de la même façon : certains requins pondent, d'autres donnent naissance à des petits vivants. En CM2 : la vipère aspic garde ses œufs dans son ventre jusqu'à l'éclosion, ses petits naissent formés ; la roussette pond des œufs protégés par une capsule ; le requin-marteau donne naissance à des petits vivants ; ces exceptions ne changent pas la règle.",
      {"cm1": ["L'ornithorynque a un bec et pond.", "Il donne pourtant du lait.", "Les requins ne font pas tous pareil."],
       "cm2": ["La vipère ne pond pas d'œufs dehors.", "La roussette est un petit requin.", "Une exception reste une exception."]},
      cm1=vf([("L'ornithorynque est un mammifère qui pond des œufs.", True, "C'est une exception."),
              ("L'ornithorynque nourrit ses petits avec son lait.", True, "Comme les autres mammifères."),
              ("Tous les requins pondent des œufs.", False, "Certains donnent naissance à des petits vivants.")]),
      cm2=vf([("Chez la vipère aspic, les petits naissent déjà formés : les œufs ont éclos dans le ventre de la mère.", True, "On dit qu'elle est ovovivipare."),
              ("La roussette, un petit requin, pond des œufs protégés par une capsule.", True, "On l'appelle parfois « bourse de sirène »."),
              ("Le requin-marteau pond des œufs sur le sable.", False, "Il donne naissance à des petits vivants."),
              ("Parce que l'ornithorynque pond, tous les mammifères pondent.", False, "Une exception ne change pas la règle."),
              ("L'ornithorynque vit en Australie.", True, "Dans l'est de l'Australie et en Tasmanie.")]),
      lecon="ovipares"),
    E("3-4", "Les panneaux des exceptions", "association",
      "Les panneaux des animaux étonnants se sont mélangés. Relie chaque animal à ce qui le rend surprenant.",
      BO + " ; " + LAMAP + " ; " + MNHN + " ; " + REQUINS,
      "L'ornithorynque est un mammifère qui pond ; la vipère aspic garde ses œufs dans son ventre jusqu'à l'éclosion ; la roussette pond des œufs dans une capsule ; le requin-marteau donne naissance à des petits vivants ; la tortue marine vit dans la mer mais pond sur une plage.",
      {"cm2": ["Un seul de ces animaux est un mammifère.", "La vipère ne pond pas d'œufs dehors.", "Deux sont des requins."]},
      commun=assoc([("l'ornithorynque", "un mammifère qui pond des œufs"), ("la vipère aspic", "ses œufs éclosent dans le ventre de la mère"),
                    ("la roussette", "un requin qui pond des œufs dans une capsule"), ("le requin-marteau", "un requin dont les petits naissent vivants"),
                    ("la tortue marine", "vit dans la mer mais pond sur une plage")]),
      lecon="ovipares", cm2_seul=True),
]})

# =================================================================== SALLE 4 — la couveuse de la ferme (Jeanne)
DOC4_CM1 = tableau("Le tableau de la nurserie", ["Animal", "Durée avant la naissance"],
                   [["la poule (couvaison)", "21 jours"], ["la lapine (gestation)", "31 jours"], ["la vache (gestation)", "9 mois"]])
DOC4_CM2 = tableau("Le tableau de la nurserie (durées moyennes)", ["Animal", "Durée avant la naissance"],
                   [["la poule (couvaison)", "21 jours"], ["la lapine (gestation)", "31 jours"], ["la chatte (gestation)", "63 à 65 jours"],
                    ["la vache (gestation)", "280 jours"], ["la jument (gestation)", "336 jours"], ["l'éléphante (gestation)", "20 à 22 mois"]])
S.append({"num": 4, "titre": "La couveuse de la ferme — Le développement avant la naissance", "enigmes": [
    E("4-1", "Le calendrier de la couveuse", "ordre",
      {"cm1": "Jeanne a noté sur son calendrier ce qu'elle voit dans l'œuf, à la lampe, pendant la couvaison. Remets les étapes dans l'ordre.",
       "cm2": "Jeanne a noté sur son calendrier ce qu'elle voit dans l'œuf, à la lampe, pendant les 21 jours de couvaison. Remets les étapes dans l'ordre."},
      BO + " ; " + POUSSIN,
      "Au début, on ne voit que le jaune ; vers le 3e jour, le cœur bat et des vaisseaux sanguins entourent le jaune ; vers le 7e jour, on reconnaît la forme du poussin ; vers le 18e jour, les plumes sont bien visibles ; le 21e jour, le poussin perce la coquille avec le diamant de son bec.",
      {"cm1": ["Au début, l'œuf ne montre que le jaune.", "Le cœur apparaît avant les plumes.", "L'éclosion est la dernière étape."],
       "cm2": ["Le cœur bat très tôt.", "Les plumes viennent tard.", "Le diamant sert le dernier jour."]},
      cm1=ordre(["On ne voit que le jaune.", "Le cœur bat.", "On reconnaît la forme du poussin.", "Le poussin sort de l'œuf."]),
      cm2=ordre([("jour 1 : on ne voit que le jaune", "aucun embryon visible"), ("jour 3 : le cœur bat", "des vaisseaux entourent le jaune"),
                 ("jour 7 : la forme du poussin", "les yeux sont bien visibles"), ("jour 18 : les plumes", "le jaune entre dans le ventre du poussin"),
                 ("jour 20 : le poussin perce la chambre à air", "il commence à respirer l'air"), ("jour 21 : l'éclosion", "il casse la coquille avec son diamant")]),
      lecon="developpement"),
    E("4-2", "L'œuf à la loupe", "plan",
      {"cm1": "Jeanne a dessiné l'intérieur d'un œuf fécondé pour les visiteurs. Place chaque nom sur son repère." + coupe_oeuf(3, "L'œuf de Jeanne"),
       "cm2": "Jeanne a dessiné l'intérieur d'un œuf fécondé. Place chaque nom sur son repère. Attention : il y a des étiquettes en trop." + coupe_oeuf(5, "L'œuf de Jeanne")},
      BO + " ; " + POUSSIN,
      "La coquille (repère 1) protège ; le jaune (repère 2) nourrit l'embryon ; le blanc (repère 3) l'entoure, le protège et lui fournit de l'eau. En CM2 : la chambre à air (repère 4) est du côté arrondi de l'œuf ; l'embryon (repère 5) est la petite tache posée sur le jaune.",
      {"cm1": ["La coquille est tout autour.", "Le jaune est au centre.", "Le blanc entoure le jaune."],
       "cm2": ["La chambre à air est dans le gros bout.", "L'embryon est posé sur le jaune.", "Le placenta n'existe pas dans un œuf de poule."]},
      cm1={"titre": "L'œuf de Jeanne", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "coquille"}, {"libelle": "Repère 2", "reponse": "jaune"}, {"libelle": "Repère 3", "reponse": "blanc"}],
           "etiquettes": ["coquille", "jaune", "blanc"]},
      cm2={"titre": "L'œuf de Jeanne", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "coquille"}, {"libelle": "Repère 2", "reponse": "jaune"}, {"libelle": "Repère 3", "reponse": "blanc"},
                     {"libelle": "Repère 4", "reponse": "chambre à air"}, {"libelle": "Repère 5", "reponse": "embryon"}],
           "etiquettes": ["coquille", "jaune", "blanc", "chambre à air", "embryon", "placenta", "cordon ombilical"]},
      lecon="developpement"),
    E("4-3", "Le cadenas des berceaux", "code",
      {"cm1": "Pour ouvrir l'armoire des berceaux, il faut trois nombres, lus dans le tableau de Jeanne." + DOC4_CM1,
       "cm2": "Pour ouvrir l'armoire des berceaux, il faut quatre nombres, lus ou calculés dans le tableau de Jeanne." + DOC4_CM2},
      BO + " ; " + POUSSIN + " ; " + GESTA,
      "La poule couve 21 jours, la gestation de la lapine dure 31 jours et celle de la vache 9 mois. En CM2 : la vache porte son veau 280 jours ; la jument porte son poulain 336 − 280 = 56 jours de plus que la vache ; la couvaison de la poule dure 21 jours, soit 3 semaines ; l'éléphante peut porter son petit jusqu'à 22 mois.",
      {"cm1": ["Lis la ligne de chaque animal.", "La poule : couvaison.", "La vache : regarde les mois."],
       "cm2": ["336 − 280.", "Une semaine = 7 jours.", "Pour l'éléphante, prends le plus grand nombre."]},
      cm1=code([("Jours de couvaison de la poule", "21"), ("Jours de gestation de la lapine", "31"), ("Mois de gestation de la vache", "9")]),
      cm2=code([("Jours de gestation de la vache", "280"), ("Jours de plus pour la jument que pour la vache", "56"),
                ("Semaines de couvaison de la poule", "3"), ("Mois de gestation au plus pour l'éléphante", "22")]),
      lecon="developpement"),
    E("4-4", "Le ventre de la jument", "vraifaux",
      "Une jument du zoo attend un poulain. Jeanne explique ce qui se passe avant la naissance. Pour chaque phrase, choisis vrai ou faux.",
      BO + " ; " + LAMAP + " ; " + GESTA,
      "Le poulain se développe dans l'utérus de la jument ; il reçoit nourriture et oxygène par le placenta et le cordon ombilical. Cette durée s'appelle la gestation : 336 jours environ chez la jument, bien plus longue que chez la lapine (31 jours). En général, plus un mammifère est grand, plus sa gestation est longue.",
      {"cm2": ["Le petit ne mange pas par la bouche avant de naître.", "Compare la jument et la lapine.", "Gestation : le temps passé dans le ventre."]},
      commun=vf([("Le poulain reçoit sa nourriture par le placenta et le cordon ombilical.", True, "Avant la naissance, il ne mange pas par la bouche."),
                 ("La gestation de la jument est plus courte que celle de la lapine.", False, "336 jours contre 31 jours."),
                 ("En général, plus un mammifère est grand, plus sa gestation est longue.", True, "L'éléphante détient le record du tableau."),
                 ("La gestation, c'est le temps que le petit passe dans le ventre de sa mère.", True, "Chez les mammifères vivipares."),
                 ("Le poulain grandit dans un œuf pondu dans la paille.", False, "La jument est vivipare.")]),
      lecon="developpement", cm2_seul=True),
]})

# =================================================================== SALLE 5 — le bureau du carnet de naissance (Sacha)
DOC5 = tableau("Le registre du zoo", ["Animal", "Fécondation", "Le petit…"],
               [["la grenouille", "dans l'eau", "sort d'un œuf"], ["le saumon", "dans l'eau", "sort d'un œuf"], ["l'autruche", "dans le corps", "sort d'un œuf"],
                ["le manchot", "dans le corps", "sort d'un œuf"], ["la tortue", "dans le corps", "sort d'un œuf"], ["le papillon", "dans le corps", "sort d'un œuf"],
                ["le zèbre", "dans le corps", "naît vivant"], ["le kangourou", "dans le corps", "naît vivant"], ["le dauphin", "dans le corps", "naît vivant"],
                ["la chauve-souris", "dans le corps", "naît vivant"]])
S.append({"num": 5, "titre": "Le bureau du carnet de naissance — La grande classification", "enigmes": [
    E("5-1", "Les enclos du zoo", "tri",
      {"cm1": "Sacha aide à refaire les panneaux des enclos. Pour chaque animal, choisis la bonne case : fécondation dans l'eau et ponte, fécondation dans le corps et ponte, fécondation dans le corps et petit qui naît vivant.",
       "cm2": "Sacha refait le grand tableau du zoo. Pour chaque animal, choisis le type de fécondation et le mode de reproduction."},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "La grenouille et la truite : fécondation externe, ovipares. La poule, le crocodile et la tortue : fécondation interne, ovipares. La girafe, le lion et le dauphin : fécondation interne, vivipares. En CM2 : le crapaud et le saumon sont dans la première case ; l'autruche, le papillon, le manchot et la tortue dans la deuxième ; le kangourou, le zèbre, le dauphin et la chauve-souris dans la troisième.",
      {"cm1": ["Deux questions : où se rencontrent les cellules ? comment naît le petit ?", "Le dauphin est un mammifère.", "La tortue pond sur la plage."],
       "cm2": ["Le manchot est un oiseau.", "La chauve-souris est un mammifère.", "Le kangourou porte son petit dans sa poche après la naissance."]},
      cm1=tri([("ext-ovi", "Dans l'eau, puis ponte"), ("int-ovi", "Dans le corps, puis ponte"), ("int-vivi", "Dans le corps, petit vivant")],
              [("la grenouille", "ext-ovi"), ("la truite", "ext-ovi"), ("la poule", "int-ovi"), ("le crocodile", "int-ovi"), ("la tortue", "int-ovi"),
               ("la girafe", "int-vivi"), ("le lion", "int-vivi"), ("le dauphin", "int-vivi")]),
      cm2=tri([("ext-ovi", "Fécondation externe, ovipare"), ("int-ovi", "Fécondation interne, ovipare"), ("int-vivi", "Fécondation interne, vivipare")],
              [("le crapaud", "ext-ovi"), ("le saumon", "ext-ovi"), ("l'autruche", "int-ovi"), ("le papillon", "int-ovi"), ("le manchot", "int-ovi"), ("la tortue", "int-ovi"),
               ("le kangourou", "int-vivi"), ("le zèbre", "int-vivi"), ("le dauphin", "int-vivi"), ("la chauve-souris", "int-vivi")]),
      lecon="classification"),
    E("5-2", "Les berceaux de la nurserie", "association",
      {"cm1": "Dans la nurserie, chaque petit attend de retrouver sa famille. Relie chaque petit à la façon dont il est né.",
       "cm2": "Dans la nurserie, chaque petit attend de retrouver sa famille. Relie chaque petit à la façon dont il est né."},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "Le têtard sort d'un œuf pondu dans la mare ; le poussin sort d'un œuf couvé 21 jours ; le chaton a grandi dans le ventre de sa mère. En CM2 : le girafon naît vivant après une longue gestation ; le crocodile sort d'un œuf pondu sur la berge ; le petit de la vipère aspic naît déjà formé, l'œuf ayant éclos dans le ventre de sa mère.",
      {"cm1": ["Le têtard deviendra une grenouille.", "Le poussin sort d'un œuf de poule.", "Le chaton est un mammifère."],
       "cm2": ["Le girafon : un mammifère.", "Le crocodile pond sur la terre ferme.", "La vipère : l'œuf éclôt dans le ventre."]},
      cm1=assoc([("le têtard", "sort d'un œuf pondu dans la mare"), ("le poussin", "sort d'un œuf couvé par sa mère"), ("le chaton", "a grandi dans le ventre de sa mère")]),
      cm2=assoc([("le têtard", "sort d'un œuf fécondé dans l'eau"), ("le poussin", "sort d'un œuf couvé pendant 21 jours"), ("le girafon", "naît vivant après une longue gestation"),
                 ("le petit crocodile", "sort d'un œuf pondu sur la berge"), ("le petit de la vipère aspic", "naît formé : l'œuf a éclos dans le ventre de sa mère")]),
      lecon="classification"),
    E("5-3", "Le carnet de naissance", "qcm",
      {"cm1": "Le carnet de naissance du zoo est presque complet. Réponds aux dernières questions de Sacha.",
       "cm2": "Le carnet de naissance du zoo est presque complet. Réponds aux dernières questions de Sacha."},
      BO + " ; " + LAMAP,
      "Pour classer un animal, on se demande où a lieu la fécondation et comment naît le petit. Un animal à fécondation externe pond des œufs. En CM2 : aucune femelle ne porte dans son ventre un œuf fécondé dans l'eau ; une fécondation interne peut donner un animal ovipare (la poule) ou vivipare (le chat) ; une exception comme l'ornithorynque ne change pas la règle.",
      {"cm1": ["Deux questions suffisent.", "Dans l'eau : le petit sort d'un œuf.", "Les mammifères : presque tous vivipares."],
       "cm2": ["La case « externe et vivipare » est vide.", "Interne : les deux sont possibles.", "Une exception reste une exception."]},
      cm1=qcm([("Quelles deux questions faut-il se poser pour classer un animal ?", ["sa couleur et sa taille", "où a lieu la fécondation et comment naît le petit", "ce qu'il mange et où il dort", "son âge et son poids"], 1, "Fécondation, puis naissance."),
               ("Un animal dont la fécondation a lieu dans l'eau…", ["pond des œufs", "naît toujours vivant", "n'a pas de petits", "vit sur terre"], 0, "Il est ovipare."),
               ("Presque tous les mammifères sont…", ["ovipares", "vivipares", "des poissons", "sans petits"], 1, "Le petit naît vivant.")]),
      cm2=qcm([("Quelle case du tableau reste vide ?", ["fécondation interne et ovipare", "fécondation interne et vivipare", "fécondation externe et vivipare", "fécondation externe et ovipare"], 2, "Un œuf fécondé dans l'eau ne grandit pas dans le ventre de la mère."),
               ("Une fécondation interne donne…", ["toujours un ovipare", "toujours un vivipare", "un ovipare ou un vivipare", "jamais de petit"], 2, "La poule et le chat ont tous deux une fécondation interne."),
               ("L'ornithorynque pond des œufs. Que faut-il en conclure ?", ["que les mammifères pondent", "que c'est une exception", "que ce n'est pas un animal", "que ce n'est pas vrai"], 1, "Le vivant est très divers."),
               ("Quel animal a une fécondation externe ?", ["le dauphin", "la truite", "la tortue", "l'autruche"], 1, "Ses gamètes se rencontrent dans l'eau.")]),
      lecon="classification"),
    E("5-4", "Les clés des enclos", "code",
      "Pour ouvrir le carnet de naissance, il faut trois nombres. Compte-les dans le registre du zoo." + DOC5,
      BO + " ; " + LAMAP + " ; " + MNHN,
      "Dans le registre, 2 animaux ont une fécondation externe (la grenouille et le saumon) ; 6 sont ovipares (la grenouille, le saumon, l'autruche, le manchot, la tortue et le papillon) ; 4 sont vivipares (le zèbre, le kangourou, le dauphin et la chauve-souris).",
      {"cm2": ["Fécondation dans l'eau = externe.", "« Sort d'un œuf » = ovipare.", "Vérifie : 6 + 4 = 10 animaux."]},
      commun=code([("Animaux à fécondation externe", "2"), ("Animaux ovipares", "6"), ("Animaux vivipares", "4")]),
      lecon="classification", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "La Nurserie du zoo", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": " ; ".join([BO, LAMAP, LAMAP_SEQ, MNHN, POUSSIN, GESTA, REQUINS, LUMNI]) + ". Détail : README.md, section Sources.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-1\",\"legende\":\"…\",\"source\":\"…\"}. Les schémas (cellules, œuf) sont dessinés en SVG par script : ne jamais les remplacer par des images générées par IA. Aucune vidéo de naissance."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
