# -*- coding: utf-8 -*-
"""Génère electricite/assets/data/enigmes.json (La Centrale en panne). Lancer : python gen_enigmes.py <dossier data>
Vigilance : aucune expérience avec le secteur ; pas d'électrons ; chiffres de production : RTE, Bilan électrique 2025.
Personnages et ville inventés."""
import json, os, re, sys
from schemas import dessin_montage, schema_normalise

BO = "Programme de sciences et technologie, cycle 3 (arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), CM2, « Signaux » : électricité"
LAMAP = "Fondation La main à la pâte, « L'électricité au cycle 3 »"
EDUSCOL = "Eduscol, ressources d'accompagnement du programme de sciences et technologie au cycle 3"
ENEDIS = "Enedis, conseils de prévention des accidents électriques"
RTE = "RTE, Bilan électrique 2025 (d'après Connaissance des énergies)"
RTE_RES = "Connaissance des énergies, fiche pédagogique « RTE » (réseau de transport)"
LUMNI = "Lumni, vidéos « L'électricité » (cycle 3)"


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
# =================================================================== SALLE 1 — l'atelier du club sciences (Nour)
S.append({"num": 1, "titre": "L'atelier du club sciences — Le circuit électrique", "enigmes": [
    E("1-1", "Le montage de Nour", "plan",
      {"cm1": "Nour a préparé un montage pour rallumer sa lampe, mais les étiquettes sont tombées. Place chaque nom sur son repère : clique sur une étiquette, puis sur la case du repère." + dessin_montage(3, "Le montage de Nour"),
       "cm2": "Nour a préparé un montage, mais les étiquettes sont tombées. Place chaque nom sur son repère. Attention : il y a des étiquettes en trop." + dessin_montage(5, "Le montage de Nour")},
      BO + " ; " + LAMAP,
      "Sur ce dessin, la pile plate est le repère 1, la lampe sur sa douille le repère 2 et l'interrupteur le repère 3. En CM2, le repère 4 est un fil de connexion et le repère 5 une borne de la pile, la lame métallique où l'on branche le fil.",
      {"cm1": ["La pile est le bloc bleu et jaune.", "La lampe est en haut à droite.", "L'interrupteur est sur le fil du bas."],
       "cm2": ["Les fils sont les traits orange.", "Une borne est une lame métallique de la pile.", "Le moteur et l'ampoule de phare ne sont pas sur ce dessin."]},
      cm1={"titre": "Le montage de Nour", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "pile"}, {"libelle": "Repère 2", "reponse": "lampe"}, {"libelle": "Repère 3", "reponse": "interrupteur"}],
           "etiquettes": ["pile", "lampe", "interrupteur"]},
      cm2={"titre": "Le montage de Nour", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "pile"}, {"libelle": "Repère 2", "reponse": "lampe"}, {"libelle": "Repère 3", "reponse": "interrupteur"},
                     {"libelle": "Repère 4", "reponse": "fil de connexion"}, {"libelle": "Repère 5", "reponse": "borne de la pile"}],
           "etiquettes": ["pile", "lampe", "interrupteur", "fil de connexion", "borne de la pile", "moteur", "prise"]},
      lecon="circuit"),
    E("1-2", "Ouvert ou fermé ?", "vraifaux",
      {"cm1": "Nour a noté ce qu'elle a compris en essayant son montage. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Nour a écrit ses observations dans son cahier d'expériences. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + LAMAP + " ; " + LUMNI,
      "La lampe ne brille que si le courant fait une boucle complète, d'une borne de la pile à l'autre : le circuit est alors fermé. Si l'interrupteur est ouvert, la boucle est coupée et la lampe reste éteinte. En CM2 : un seul fil suffit à couper la boucle s'il est débranché ; le courant ne s'use pas dans la lampe, c'est la pile qui s'use ; deux lampes dans la même boucle s'éteignent ensemble si l'une est dévissée.",
      {"cm1": ["Le courant doit aller d'une borne de la pile à l'autre.", "Un interrupteur ouvert coupe le chemin.", "Une seule borne ne suffit pas."],
       "cm2": ["Un fil débranché, c'est une boucle coupée.", "Ce qui s'use, ce n'est pas le courant.", "Dans une seule boucle, tout s'arrête si on la coupe."]},
      cm1=vf([("Pour que la lampe brille, le courant doit faire une boucle complète.", True, "D'une borne de la pile à l'autre, sans interruption."),
              ("Si l'interrupteur est ouvert, la lampe brille quand même.", False, "La boucle est coupée : la lampe est éteinte."),
              ("Il suffit de relier la lampe à une seule borne de la pile.", False, "Il faut relier les deux bornes.")]),
      cm2=vf([("Quand la boucle est complète, on dit que le circuit est fermé.", True, "Le courant circule et la lampe brille."),
              ("Un seul fil débranché suffit à éteindre la lampe.", True, "La boucle est coupée : le circuit est ouvert."),
              ("Le courant s'use en traversant la lampe.", False, "Le courant ne s'use pas ; c'est la pile qui s'use peu à peu."),
              ("Avec deux lampes dans la même boucle, si l'on dévisse l'une, l'autre reste allumée.", False, "La boucle est coupée : les deux s'éteignent."),
              ("L'interrupteur sert à ouvrir ou fermer le circuit sans débrancher les fils.", True, "C'est son rôle.")]),
      lecon="circuit"),
    E("1-3", "Quelle lampe s'allume ?", "qcm",
      {"cm1": "Nour a fait plusieurs essais. Lis la description de chaque montage et choisis la bonne réponse.",
       "cm2": "Nour a fait plusieurs essais avec une pile, des fils et des lampes. Lis chaque montage et choisis la bonne réponse."},
      BO + " ; " + LAMAP,
      "Seul le montage où les deux bornes de la pile sont reliées à la lampe, avec l'interrupteur fermé, forme une boucle complète : la lampe brille. Un fil qui ne touche qu'une borne, ou un interrupteur ouvert, coupe la boucle. En CM2 : relier directement les deux bornes de la pile par un fil, sans lampe, est un court-circuit : le fil chauffe et la pile s'use très vite.",
      {"cm1": ["Il faut deux fils, un pour chaque borne.", "L'interrupteur doit être fermé.", "Une lampe toute seule ne s'allume pas."],
       "cm2": ["Cherche la boucle complète.", "Un fil seul entre les deux bornes : danger pour la pile.", "Une pile usée ne fait plus briller la lampe."]},
      cm1=qcm([("Dans quel montage la lampe brille-t-elle ?", ["un fil relie la borne + à la lampe, rien d'autre", "deux fils relient la lampe aux deux bornes de la pile", "la lampe est posée sur la pile, sans fil", "un fil relie les deux bornes de la pile"], 1, "Les deux bornes sont reliées : la boucle est complète."),
               ("Le montage est complet, mais la lampe ne brille pas. Que vérifier d'abord ?", ["la couleur des fils", "la taille de la table", "que l'interrupteur est bien fermé", "l'heure qu'il est"], 2, "Un interrupteur ouvert coupe la boucle."),
               ("Que faut-il au minimum pour allumer une lampe ?", ["une pile, une lampe et deux fils", "une prise et une lampe", "une lampe seulement", "trois piles"], 0, "Pile, lampe et fils forment la boucle.")]),
      cm2=qcm([("Quel montage forme une boucle complète ?", ["pile, fil, lampe, fil vers la même borne", "pile, fil, lampe, fil vers l'autre borne", "pile, fil, lampe, fil laissé libre", "lampe et fil, sans pile"], 1, "Le courant part d'une borne et revient à l'autre."),
               ("Un fil relie directement les deux bornes de la pile. Que se passe-t-il ?", ["la lampe brille plus fort", "rien du tout", "le fil chauffe et la pile s'use très vite", "la pile se recharge"], 2, "C'est un court-circuit."),
               ("La boucle est complète, l'interrupteur fermé, mais la lampe reste éteinte. Que peut-on soupçonner ?", ["la pile est usée ou la lampe est grillée", "les fils sont trop courts", "le courant s'est usé", "la table est en bois"], 0, "Une pile usée ou une lampe grillée empêchent la lampe de briller."),
               ("Combien de bornes possède une lampe ?", ["une", "deux", "trois", "aucune"], 1, "Deux bornes, sur son culot.")]),
      lecon="circuit"),
    E("1-4", "Le pas-à-pas de Nour", "ordre",
      "Nour veut écrire la fiche de montage pour le club. Remets les étapes dans l'ordre.",
      BO + " ; " + LAMAP,
      "On vérifie d'abord que l'interrupteur est ouvert, puis on relie la borne + de la pile à l'interrupteur, l'interrupteur à la lampe, et la lampe à la borne − : la boucle est complète. On ferme enfin l'interrupteur pour allumer la lampe, et on l'ouvre pour l'éteindre.",
      {"cm2": ["On prépare le matériel sans courant qui circule.", "On construit la boucle fil par fil.", "On ferme l'interrupteur en dernier."]},
      commun=ordre(["Poser l'interrupteur en position ouverte.", "Relier la borne + de la pile à l'interrupteur.", "Relier l'interrupteur à la lampe.",
                    "Relier la lampe à la borne − de la pile.", "Fermer l'interrupteur : la lampe s'allume."]),
      lecon="circuit", cm2_seul=True),
]})

# =================================================================== SALLE 2 — le magasin de matériel (Maëlle)
S.append({"num": 2, "titre": "Le magasin de matériel — Conducteurs et isolants", "enigmes": [
    E("2-1", "Le bac renversé", "tri",
      {"cm1": "Maëlle a testé chaque objet du bac avec son circuit testeur. Range chaque objet : conducteur (la lampe s'allume) ou isolant (la lampe reste éteinte).",
       "cm2": "Maëlle a testé chaque objet du bac avec son circuit testeur. Range chaque objet dans la bonne colonne. Attention aux pièges."},
      BO + " ; " + LAMAP,
      "Les objets en métal (clé en fer, trombone, papier d'aluminium, pièce de monnaie) sont conducteurs. Les objets en plastique, en bois, en verre, en caoutchouc ou en papier sont isolants. En CM2, la mine du crayon à papier, en graphite, est conductrice alors que ce n'est pas un métal.",
      {"cm1": ["Les métaux sont conducteurs.", "Le plastique et le bois sont isolants.", "Le papier d'aluminium est un métal."],
       "cm2": ["La mine du crayon conduit le courant.", "Le bois du crayon, lui, est isolant.", "Le verre et le caoutchouc sont isolants."]},
      cm1=tri([("cond", "Conducteur"), ("isol", "Isolant")],
              [("une clé en fer", "cond"), ("un trombone", "cond"), ("du papier d'aluminium", "cond"),
               ("une règle en plastique", "isol"), ("un crayon de couleur en bois", "isol"), ("une gomme", "isol")]),
      cm2=tri([("cond", "Conducteur"), ("isol", "Isolant")],
              [("une pièce de monnaie", "cond"), ("un trombone", "cond"), ("la mine d'un crayon à papier", "cond"), ("une vis en acier", "cond"),
               ("un bouchon en liège", "isol"), ("une bille en verre", "isol"), ("un élastique en caoutchouc", "isol"), ("une feuille de papier", "isol")]),
      lecon="conducteurs"),
    E("2-2", "L'intrus de la boîte", "intrus",
      {"cm1": "Maëlle a rangé dans une boîte les objets qui font briller la lampe du testeur. Un objet s'est glissé là par erreur. Trouve l'intrus.",
       "cm2": "Maëlle a rangé dans une boîte des objets conducteurs. L'un d'eux ne laisse pas passer le courant. Trouve l'intrus."},
      BO + " ; " + LAMAP,
      "La cuillère en bois est l'intrus en CM1 : le bois est isolant, alors que la fourchette, le clou et la canette sont en métal. En CM2, l'intrus est le gant en caoutchouc : il est isolant, c'est même pour cela que les électriciens en portent ; la mine de crayon en graphite, elle, est conductrice.",
      {"cm1": ["Cherche l'objet qui n'est pas en métal.", "Une cuillère peut être en métal ou en bois.", "Le bois est isolant."],
       "cm2": ["Le graphite de la mine conduit le courant.", "Que portent les électriciens pour se protéger ?", "Le caoutchouc est isolant."]},
      cm1=intrus([("une fourchette en métal", False), ("un clou", False), ("une canette en aluminium", False), ("une cuillère en bois", True)]),
      cm2=intrus([("un fil de cuivre dénudé", False), ("la mine d'un crayon à papier", False), ("une clé en laiton", False), ("une barrette en aluminium", False), ("un gant en caoutchouc", True)]),
      lecon="conducteurs"),
    E("2-3", "Les étiquettes des bobines", "association",
      {"cm1": "Les étiquettes des bobines et des outils se sont décollées. Relie chaque objet à ce qu'il fait.",
       "cm2": "Maëlle explique à quoi sert chaque matériau du magasin. Relie chaque élément à son rôle."},
      BO + " ; " + LAMAP + " ; " + ENEDIS,
      "Le cœur en cuivre du fil conduit le courant ; la gaine en plastique isole et protège les doigts ; le circuit testeur dit si un objet est conducteur. En CM2 : les poignées des outils et les prises sont en plastique pour protéger les personnes ; l'air sec, entre les lames d'un interrupteur ouvert, coupe la boucle ; le corps humain conduit le courant, d'où le danger du secteur.",
      {"cm1": ["Le cuivre est un métal.", "Le plastique arrête le courant.", "Le testeur a une lampe."],
       "cm2": ["L'air est isolant.", "Les poignées doivent protéger la main.", "Le corps humain n'est pas isolant."]},
      cm1=assoc([("le cœur en cuivre du fil", "conduit le courant"), ("la gaine en plastique du fil", "isole et protège les doigts"), ("le circuit testeur", "dit si un objet est conducteur")]),
      cm2=assoc([("le cœur en cuivre du fil", "laisse passer le courant"), ("la gaine en plastique", "empêche le courant de sortir du fil"),
                 ("la poignée en plastique d'un tournevis", "protège la main de l'électricien"), ("l'air entre les lames d'un interrupteur ouvert", "coupe la boucle"),
                 ("le corps humain", "conduit le courant : le secteur est dangereux")]),
      lecon="conducteurs"),
    E("2-4", "La notice du testeur", "trous",
      "La notice du circuit testeur a pris l'eau : des mots ont disparu. Complète-la. Attention : il y a des étiquettes en trop.",
      BO + " ; " + LAMAP,
      "On place l'objet dans la boucle du circuit testeur. Si la lampe s'allume, l'objet est conducteur ; si elle reste éteinte, il est isolant. Les métaux, comme le cuivre, sont conducteurs ; le plastique est isolant.",
      {"cm2": ["L'objet doit faire partie de la boucle.", "Lampe allumée : le courant passe.", "Le cuivre est un métal."]},
      commun={"texte": "<p>Pour tester un objet, on le place dans la [[boucle]] du circuit. Si la lampe [[s'allume]], l'objet est [[conducteur]]. Si elle reste éteinte, il est [[isolant]]. Le [[cuivre]] des fils est conducteur ; le [[plastique]] des gaines est isolant.</p>",
              "etiquettes": ["boucle", "s'allume", "conducteur", "isolant", "cuivre", "plastique", "s'use", "bois", "électron"]},
      lecon="conducteurs", cm2_seul=True),
]})

# =================================================================== SALLE 3 — la salle de contrôle (Hélène)
S.append({"num": 3, "titre": "La salle de contrôle — Le schéma électrique", "enigmes": [
    E("3-1", "La légende des symboles", "association",
      {"cm1": "La légende du tableau mural s'est effacée. Relie chaque symbole décrit à l'appareil qu'il représente.",
       "cm2": "Hélène a besoin de la légende complète du tableau mural. Relie chaque symbole décrit à ce qu'il représente."},
      BO + " ; " + EDUSCOL + " ; " + LAMAP,
      "Un grand trait et un petit trait parallèles représentent la pile ; un cercle barré d'une croix, la lampe ; un cercle avec un M, le moteur. En CM2 : le trait levé est un interrupteur ouvert, le trait couché qui ferme le passage un interrupteur fermé, et le trait droit un fil de connexion.",
      {"cm1": ["La pile a deux bornes : deux traits.", "La lampe ressemble à une croix dans un rond.", "M comme moteur."],
       "cm2": ["Un passage coupé, c'est un interrupteur ouvert.", "Le grand trait de la pile est la borne +.", "Le fil est le plus simple des symboles."]},
      cm1=assoc([("un grand trait et un petit trait parallèles", "la pile"), ("un cercle barré d'une croix", "la lampe"), ("un cercle avec la lettre M", "le moteur")]),
      cm2=assoc([("un grand trait et un petit trait parallèles", "la pile"), ("un cercle barré d'une croix", "la lampe"), ("un cercle avec la lettre M", "le moteur"),
                 ("un trait levé entre deux points", "l'interrupteur ouvert"), ("un trait droit", "le fil de connexion")]),
      lecon="schema"),
    E("3-2", "Le schéma du pupitre", "plan",
      {"cm1": "Sur le pupitre, le schéma de la lampe de secours a perdu ses étiquettes. Place chaque nom sur son repère." + schema_normalise(3, "Le schéma du pupitre"),
       "cm2": "Sur le pupitre, le schéma du circuit de secours a perdu ses étiquettes. Place chaque nom sur son repère. Attention : il y a des étiquettes en trop." + schema_normalise(5, "Le schéma du pupitre")},
      BO + " ; " + EDUSCOL,
      "Le repère 1, à gauche, est la pile : un grand trait et un petit trait. Le repère 2, en haut, est l'interrupteur, ici ouvert. Le repère 3, à droite, est la lampe. En CM2, le repère 4 est le moteur, le cercle avec un M, et le repère 5 un fil de connexion.",
      {"cm1": ["Ouvre la fiche « Le schéma électrique ».", "La croix dans le cercle, c'est la lampe.", "Le trait levé, c'est l'interrupteur."],
       "cm2": ["Le M désigne le moteur.", "Le repère 5 est sur un trait droit.", "Il n'y a ni prise ni buzzer sur ce schéma."]},
      cm1={"titre": "Le schéma du pupitre", "colonnes": 3,
           "cases": [{"libelle": "Repère 1", "reponse": "pile"}, {"libelle": "Repère 2", "reponse": "interrupteur"}, {"libelle": "Repère 3", "reponse": "lampe"}],
           "etiquettes": ["pile", "interrupteur", "lampe"]},
      cm2={"titre": "Le schéma du pupitre", "colonnes": 2,
           "cases": [{"libelle": "Repère 1", "reponse": "pile"}, {"libelle": "Repère 2", "reponse": "interrupteur"}, {"libelle": "Repère 3", "reponse": "lampe"},
                     {"libelle": "Repère 4", "reponse": "moteur"}, {"libelle": "Repère 5", "reponse": "fil de connexion"}],
           "etiquettes": ["pile", "interrupteur", "lampe", "moteur", "fil de connexion", "prise", "buzzer"]},
      lecon="schema"),
    E("3-3", "Ce que dit le schéma", "vraifaux",
      {"cm1": "Hélène te demande de lire le schéma du pupitre. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Hélène vérifie que tu sais lire le schéma du pupitre. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + EDUSCOL,
      "Sur ce schéma, l'interrupteur est ouvert : la boucle est coupée, la lampe est éteinte et le moteur à l'arrêt. Un schéma utilise des symboles, pas des dessins ressemblants. En CM2 : la lampe, le moteur et l'interrupteur sont dans une seule boucle, donc l'interrupteur commande les deux ; et le grand trait de la pile est la borne +.",
      {"cm1": ["Regarde la forme de l'interrupteur.", "Interrupteur ouvert : boucle coupée.", "Un schéma n'est pas une photo."],
       "cm2": ["Il n'y a qu'une seule boucle.", "Qui est le grand trait de la pile ?", "Un interrupteur ouvert coupe tout ce qui est dans sa boucle."]},
      cm1=vf([("Sur ce schéma, l'interrupteur est ouvert.", True, "Le trait est levé."),
              ("Sur ce schéma, la lampe est allumée.", False, "La boucle est coupée : elle est éteinte."),
              ("Un schéma dessine les objets avec des symboles.", True, "Les mêmes pour tout le monde.")]),
      cm2=vf([("Sur ce schéma, la lampe et le moteur sont dans la même boucle.", True, "Il n'y a qu'un seul chemin."),
              ("Si l'on ferme l'interrupteur, seule la lampe fonctionnera.", False, "La lampe et le moteur fonctionneront tous les deux."),
              ("Le grand trait de la pile représente la borne +.", True, "Le petit trait est la borne −."),
              ("Pour lire un schéma, on suit le courant de la borne + à la borne −.", True, "En passant par chaque appareil."),
              ("Un schéma doit ressembler le plus possible aux vrais objets.", False, "Il ne garde que l'essentiel : les appareils et leurs liaisons.")]),
      lecon="schema"),
    E("3-4", "Suivre le courant", "ordre",
      "Hélène pose le doigt sur la borne + de la pile du schéma. Range les éléments dans l'ordre où le courant les traverse, jusqu'à la borne −.",
      BO + " ; " + EDUSCOL,
      "En partant du grand trait de la pile, la borne +, le courant traverse d'abord l'interrupteur, en haut, puis la lampe, à droite, puis le moteur, en bas, avant de revenir à la borne −, le petit trait.",
      {"cm2": ["La borne + est en haut de la pile.", "On fait le tour du rectangle dans le sens des aiguilles d'une montre.", "La borne − est en dernier."]},
      commun=ordre(["la borne + de la pile", "l'interrupteur", "la lampe", "le moteur", "la borne − de la pile"]),
      lecon="schema", cm2_seul=True),
]})

# =================================================================== SALLE 4 — la maison témoin (Marius)
S.append({"num": 4, "titre": "La maison témoin — La sécurité électrique", "enigmes": [
    E("4-1", "Le quiz de Marius", "qcm",
      {"cm1": "Avant de rallumer les maisons, Marius pose ses questions. Choisis la bonne réponse.",
       "cm2": "Avant de rallumer Clairval, Marius vérifie que tu connais les dangers. Choisis la bonne réponse."},
      BO + " ; " + ENEDIS + " ; " + LAMAP,
      "La pile plate de la classe, de 4,5 volts, est sans danger ; le courant des prises, de 230 volts, est dangereux et peut tuer. On ne met jamais d'objet dans une prise. En CM2 : en cas d'accident, on ne touche pas la personne, on coupe le courant au disjoncteur, puis on appelle le 18 ou le 112 ; on débranche en tirant sur la fiche, pas sur le fil.",
      {"cm1": ["Ouvre la fiche « La sécurité électrique ».", "Les prises sont dangereuses, les piles de la classe non.", "Rien ne doit entrer dans une prise, sauf une fiche."],
       "cm2": ["Il faut d'abord couper le courant.", "Les numéros d'urgence ont deux ou trois chiffres.", "La fiche est faite pour être tenue."]},
      cm1=qcm([("Avec quoi a-t-on le droit de faire des expériences en classe ?", ["avec la prise de la classe", "avec une pile plate", "avec une rallonge", "avec un grille-pain"], 1, "La pile de la classe est sans danger."),
               ("Le courant des prises de la maison est…", ["sans danger", "dangereux, il peut tuer", "le même que celui d'une pile", "seulement chaud"], 1, "Il a une tension de 230 volts."),
               ("Que ne faut-il jamais mettre dans une prise ?", ["la fiche d'une lampe", "un objet, comme un clou ou une épingle", "la fiche d'un chargeur", "la fiche d'un aspirateur"], 1, "Seules les fiches vont dans les prises.")]),
      cm2=qcm([("Quelle est la tension des prises de la maison ?", ["4,5 volts", "12 volts", "230 volts", "400 000 volts"], 2, "230 volts : c'est dangereux."),
               ("Une personne est électrisée par un appareil. Que fais-tu d'abord ?", ["je la tire par le bras", "je coupe le courant au disjoncteur", "je lui jette de l'eau", "j'attends qu'elle se relève"], 1, "On ne la touche pas tant que le courant passe."),
               ("Quel numéro appeler ensuite ?", ["le 18 ou le 112", "le 36 30", "le 3615", "le numéro de l'école"], 0, "Pompiers (18) ou numéro d'urgence européen (112)."),
               ("Comment débrancher un appareil ?", ["en tirant sur le fil", "en tirant sur la fiche", "avec les mains mouillées", "en coupant le fil"], 1, "Tirer sur le fil l'abîme.")]),
      lecon="securite"),
    E("4-2", "Les affiches tombées", "tri",
      {"cm1": "Les affiches de prévention de la maison témoin sont tombées. Range chaque situation : danger ou sans danger.",
       "cm2": "Marius veut raccrocher les affiches de prévention. Range chaque situation dans la bonne colonne."},
      BO + " ; " + ENEDIS,
      "Une pile plate, une lampe de poche ou un jouet à piles sont sans danger. Mettre un objet dans une prise, toucher un sèche-cheveux branché avec les mains mouillées ou jouer près d'un pylône sont dangereux. En CM2 : faire voler un cerf-volant près des lignes, entrer dans un poste électrique, utiliser un fil abîmé sont dangereux ; débrancher par la fiche, éteindre la lumière en partant et laisser un adulte changer une ampoule appareil débranché sont de bons réflexes.",
      {"cm1": ["Les piles de la classe : sans danger.", "L'eau et le secteur ne vont pas ensemble.", "Les pylônes portent des lignes très dangereuses."],
       "cm2": ["Les lignes électriques sont dangereuses même sans les toucher.", "Un fil abîmé laisse voir le cuivre.", "Un bon réflexe protège."]},
      cm1=tri([("danger", "Danger"), ("sans", "Sans danger")],
              [("glisser une épingle dans une prise", "danger"), ("toucher un sèche-cheveux branché avec les mains mouillées", "danger"), ("jouer au pied d'un pylône", "danger"),
               ("monter un circuit avec une pile plate", "sans"), ("allumer une lampe de poche", "sans"), ("jouer avec une petite voiture à piles", "sans")]),
      cm2=tri([("danger", "Danger"), ("bon", "Bon réflexe")],
              [("faire voler un cerf-volant près des lignes électriques", "danger"), ("entrer dans un poste électrique pour récupérer un ballon", "danger"),
               ("utiliser une rallonge dont le fil est abîmé", "danger"), ("téléphoner en charge dans le bain", "danger"),
               ("débrancher en tirant sur la fiche", "bon"), ("couper le courant avant de secourir une personne électrisée", "bon"),
               ("éteindre la lumière en quittant une pièce", "bon"), ("demander à un adulte de changer une ampoule, lampe débranchée", "bon")]),
      lecon="securite"),
    E("4-3", "Les idées reçues", "vraifaux",
      {"cm1": "Des visiteurs ont écrit leurs idées sur le tableau de la maison témoin. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Marius corrige les idées reçues des visiteurs. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + ENEDIS + " ; " + LAMAP,
      "On peut faire des expériences avec une pile plate, mais jamais avec le secteur. L'eau et l'électricité du secteur ensemble sont très dangereuses. Éteindre la lumière en quittant une pièce économise l'électricité. En CM2 : une lampe à LED consomme beaucoup moins qu'une lampe à incandescence ; un appareil en veille consomme encore ; une ligne électrique peut être dangereuse même sans la toucher.",
      {"cm1": ["Pile : oui ; prise : jamais.", "L'eau conduit le courant du secteur.", "Une lampe éteinte ne consomme pas."],
       "cm2": ["Une LED chauffe très peu.", "Le petit voyant rouge d'un appareil en veille est allumé.", "Le courant d'une ligne peut sauter vers un objet proche."]},
      cm1=vf([("On peut faire des expériences avec les prises de la classe si l'on fait attention.", False, "Jamais : seulement avec des piles."),
              ("Il ne faut jamais toucher un appareil électrique avec les mains mouillées.", True, "L'eau conduit le courant du secteur."),
              ("Éteindre la lumière en quittant une pièce permet d'économiser l'électricité.", True, "Une lampe éteinte ne consomme rien.")]),
      cm2=vf([("Une lampe à LED consomme beaucoup moins qu'une ancienne lampe à incandescence.", True, "Elle éclaire autant en consommant beaucoup moins."),
              ("Un téléviseur en veille ne consomme rien du tout.", False, "Il consomme encore un peu."),
              ("Une ligne à haute tension n'est dangereuse que si on la touche.", False, "Le courant peut sauter vers un objet très proche, comme un cerf-volant."),
              ("La pile plate de 4,5 volts ne présente pas de danger pour le corps.", True, "C'est pour cela qu'on l'utilise en classe."),
              ("Le disjoncteur permet de couper le courant de toute la maison.", True, "On le coupe avant de secourir une personne électrisée.")]),
      lecon="securite"),
    E("4-4", "Les bons réflexes", "association",
      "Marius montre les pièces de la maison témoin. Relie chaque situation au bon réflexe.",
      BO + " ; " + ENEDIS,
      "Dans la salle de bain, on n'utilise pas d'appareil électrique près de l'eau. Pour débrancher, on tire sur la fiche. Face à une personne électrisée, on coupe le courant avant de la toucher. Un ballon dans un poste électrique : on appelle un adulte, qui préviendra le gestionnaire du réseau. En quittant la pièce, on éteint la lumière.",
      {"cm2": ["L'eau et le secteur ne se mélangent pas.", "On ne touche jamais une personne électrisée tant que le courant passe.", "Un poste électrique est fermé pour une bonne raison."]},
      commun=assoc([("la salle de bain", "aucun appareil branché près de la baignoire"), ("une lampe à débrancher", "tirer sur la fiche, pas sur le fil"),
                    ("une personne électrisée", "couper le courant, puis appeler le 18 ou le 112"), ("un ballon tombé dans un poste électrique", "ne pas entrer et prévenir un adulte"),
                    ("une pièce que l'on quitte", "éteindre la lumière")]),
      lecon="securite", cm2_seul=True),
]})

# =================================================================== SALLE 5 — le poste de conduite du réseau (Karim)
DOC_CM1 = tableau("Production d'électricité en France en 2025 (en milliards de kilowattheures, arrondis)", ["Centrales", "Production"],
                  [["nucléaires", "373"], ["hydrauliques", "62"], ["éoliennes", "50"], ["solaires", "33"], ["au gaz, au charbon, au fioul", "19"]])
DOC_CM2 = tableau("Production d'électricité en France en 2025 (en milliards de kilowattheures) — total : 547,5", ["Centrales", "Production"],
                  [["nucléaires", "373"], ["hydrauliques", "62,4"], ["éoliennes", "49,6"], ["solaires", "32,9"], ["au gaz, au charbon, au fioul", "environ 18,7"]])
S.append({"num": 5, "titre": "Le poste de conduite du réseau — Produire et transporter l'électricité", "enigmes": [
    E("5-1", "De la centrale à la prise", "ordre",
      {"cm1": "Sur la carte lumineuse, le trajet de l'électricité est effacé. Remets les étapes dans l'ordre, de la centrale jusqu'à la lampe de la maison.",
       "cm2": "Karim doit rallumer le trajet complet de l'électricité sur la carte. Remets les étapes dans l'ordre, de la centrale jusqu'à la prise."},
      BO + " ; " + RTE_RES,
      "L'électricité part de la centrale, voyage sur les lignes à très haute tension portées par des pylônes, arrive dans un poste près de la ville, puis passe par les câbles du quartier jusqu'à la maison. En CM2 : un transformateur élève la tension à la sortie de la centrale ; le poste l'abaisse ; le réseau de distribution va jusqu'au compteur, puis aux prises.",
      {"cm1": ["Tout commence là où l'électricité est produite.", "Les pylônes portent les grandes lignes.", "La maison est en dernier."],
       "cm2": ["Le transformateur est juste à la sortie de la centrale.", "Le poste est près de la ville.", "Le compteur est à l'entrée de la maison."]},
      cm1=ordre(["la centrale", "les lignes à très haute tension sur les pylônes", "le poste près de la ville", "la lampe de la maison"]),
      cm2=ordre(["la centrale produit le courant", "un transformateur élève la tension", "les lignes à très haute tension le transportent",
                 "un poste abaisse la tension près de la ville", "le réseau de distribution l'amène au compteur", "la prise de la maison"]),
      lecon="production"),
    E("5-2", "Les centrales de la vallée", "tri",
      {"cm1": "Sur la carte de la vallée, Karim a placé les centrales qui alimentent Clairval. Range chacune selon ce qu'elle utilise : une source qui se renouvelle ou une source qui s'épuise.",
       "cm2": "Karim range les centrales du pays selon leur source d'énergie. Place chaque carte dans la bonne colonne."},
      BO + " ; " + RTE + " ; " + LUMNI,
      "Les centrales hydrauliques (l'eau d'un barrage), les éoliennes (le vent) et les panneaux solaires (la lumière du Soleil) utilisent des sources renouvelables. Les centrales nucléaires (l'uranium) et les centrales thermiques (gaz, charbon, fioul) utilisent des sources qui ne se renouvellent pas.",
      {"cm1": ["Le vent, l'eau et le Soleil reviennent toujours.", "L'uranium est extrait du sol.", "Le gaz brûlé ne revient pas."],
       "cm2": ["Regarde ce qui fait tourner la turbine.", "Le panneau solaire ne fait rien tourner.", "Le charbon est un combustible fossile."]},
      cm1=tri([("renouv", "Source renouvelable"), ("epuise", "Source qui s'épuise")],
              [("le barrage hydraulique", "renouv"), ("le parc d'éoliennes", "renouv"), ("les panneaux solaires", "renouv"),
               ("la centrale nucléaire", "epuise"), ("la centrale au gaz", "epuise")]),
      cm2=tri([("renouv", "Renouvelable"), ("epuise", "Non renouvelable")],
              [("l'eau retenue par un barrage", "renouv"), ("le vent qui fait tourner les pales", "renouv"), ("la lumière du Soleil sur les panneaux", "renouv"),
               ("la marée dans une usine marémotrice", "renouv"), ("l'uranium d'une centrale nucléaire", "epuise"), ("le gaz d'une centrale thermique", "epuise"),
               ("le charbon", "epuise"), ("le fioul", "epuise")]),
      lecon="production"),
    E("5-3", "Le pupitre de reconnexion", "code",
      {"cm1": "Pour rebrancher les quatre quartiers de Clairval un par un, le pupitre demande quatre codes. Chaque code est la production d'un type de centrale en 2025, lue dans le tableau de Karim." + DOC_CM1,
       "cm2": "Pour rebrancher les quatre quartiers un par un, le pupitre demande quatre codes, lus ou calculés dans le tableau de Karim. Arrondis à l'unité." + DOC_CM2},
      BO + " ; " + RTE,
      "Le quartier de la gare se rallume avec 373, la production nucléaire ; le quartier du port avec 62, l'hydraulique ; le quartier des écoles avec 50, l'éolien ; le quartier du marché avec 33, le solaire. En CM2, il fallait arrondir 62,4 à 62, 49,6 à 50 et 32,9 à 33, et calculer la part du nucléaire : 373 sur 547,5, soit environ 68 %.",
      {"cm1": ["Lis la ligne de chaque type de centrale.", "Le nucléaire a le plus grand nombre.", "Les éoliennes : la ligne du milieu."],
       "cm2": ["49,6 s'arrondit à 50.", "Pour la part du nucléaire, divise 373 par 547,5.", "Le résultat est un peu plus de deux tiers."]},
      cm1=code([("Quartier de la gare : production nucléaire", "373"), ("Quartier du port : production hydraulique", "62"),
                ("Quartier des écoles : production éolienne", "50"), ("Quartier du marché : production solaire", "33")]),
      cm2=code([("Quartier de la gare : part du nucléaire, en %", "68"), ("Quartier du port : production hydraulique arrondie", "62"),
                ("Quartier des écoles : production éolienne arrondie", "50"), ("Quartier du marché : production solaire arrondie", "33")]),
      lecon="production"),
    E("5-4", "Le carnet de Karim", "trous",
      "Karim a noté comment on produit l'électricité, mais l'orage a mouillé son carnet. Complète-le. Attention : il y a des étiquettes en trop.",
      BO + " ; " + RTE + " ; " + LUMNI,
      "Dans la plupart des centrales, une turbine reliée à un alternateur tourne pour produire le courant : la vapeur dans une centrale nucléaire, l'eau d'un barrage dans une centrale hydraulique, le vent dans une éolienne. Les panneaux solaires, eux, transforment directement la lumière. L'électricité se stocke très mal : il faut produire à chaque instant autant que l'on consomme.",
      {"cm2": ["La turbine fait tourner une autre machine.", "Dans le nucléaire, la chaleur fait de la vapeur.", "Ce qui ne se garde pas bien, c'est l'électricité."]},
      commun={"texte": "<p>Dans la plupart des centrales, une [[turbine]] reliée à un [[alternateur]] tourne pour produire le courant. Dans une centrale nucléaire, c'est la [[vapeur]] qui la fait tourner ; dans une éolienne, c'est le [[vent]]. Les panneaux solaires transforment directement la [[lumière]] en électricité. L'électricité se [[stocke]] très mal : il faut produire à chaque instant autant que l'on consomme.</p>",
              "etiquettes": ["turbine", "alternateur", "vapeur", "vent", "lumière", "stocke", "pile", "fumée", "use"]},
      lecon="production", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "La Centrale en panne", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": " ; ".join([BO, LAMAP, EDUSCOL, ENEDIS, RTE, RTE_RES, LUMNI]) + ". Détail : README.md, section Sources.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-1\",\"legende\":\"…\",\"source\":\"…\"}. Les montages et les schémas sont dessinés en SVG par script : ne jamais les remplacer par des images générées par IA."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
