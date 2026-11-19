# -*- coding: utf-8 -*-
"""Génère grande-guerre/assets/data/enigmes.json (Les Lettres du poilu). Lancer : python gen_enigmes.py <dossier data>
SUJET SENSIBLE : ton du souvenir, aucun détail violent, aucun « gagner la guerre » ; chiffres officiels avec source.
Village (Vaux-les-Tilleuls, Côte-d'Or), famille Garnier et tous les personnages : inventés. Les personnes réelles ne parlent jamais."""
import json, os, sys
from schemas import tranchee, monument

BO = "Programme d'histoire du cycle 3 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026), Première Guerre mondiale (CM2) ; progression de l'enseignant : thème 6 « La France des guerres mondiales à l'Union européenne », année A, période 5"
CDM = "Ministère des Armées, Chemins de mémoire (« Un deuil national » ; « 1916. Les batailles de Verdun et de la Somme » ; « 11 novembre, journée nationale de commémoration »)"
MA = "Musée de l'Armée, fiche objet « L'affiche de mobilisation » (2025)"
UNIV = "Encyclopædia Universalis, « Guerre mondiale (Première) : le rôle des colonies » et « Grande Guerre et société »"
MDH = "Mémoire des hommes, base des morts pour la France (ministère des Armées)"
GOUV = "info.gouv.fr, « Pourquoi le 11 novembre est-il férié en France ? » ; loi du 24 octobre 1922"
ONAC = "ONACVG et Eduscol, « Commémorer le 11 novembre »"

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


def plan(titre, col, cases, etiq):
    return {"titre": titre, "colonnes": col, "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(cases)], "etiquettes": etiq}


def tableau(titre, entetes, lignes):
    h = "".join(f"<th>{x}</th>" for x in entetes)
    c = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in l) + "</tr>" for l in lignes)
    return f"<div class='doc-titre'><i>{titre}</i></div><table class='tableau-releves'><tr>{h}</tr>{c}</table>"


AFFICHE = ("<div class='doc-titre'><i>L'affiche collée sur la porte de la mairie (extrait simplifié, recopié par Jeanne)</i></div>"
           "<blockquote>ORDRE DE MOBILISATION GÉNÉRALE. Par décret du Président de la République, la mobilisation des armées de terre et de mer est ordonnée. "
           "Le premier jour de la mobilisation est le dimanche 2 août 1914. Tout Français soumis aux obligations militaires doit obéir.</blockquote>")

REGISTRE = tableau("Le registre de la mairie : les noms à graver sur le monument (soldats inventés)",
                   ["N°", "Nom", "Né en", "Mort pour la France en", "Lieu"],
                   [["1", "Paul Bernard", "1894", "1914", "la Marne"], ["2", "Henri Colin", "1890", "1915", "l'Artois"],
                    ["3", "Lucien Dubois", "1896", "1916", "Verdun"], ["4", "Marcel Fabre", "1897", "1916", "la Somme"],
                    ["5", "Joseph Garnier", "1888", "1917", "le Chemin des Dames"], ["6", "René Masson", "1899", "1918", "la Champagne"],
                    ["7", "Albert Petit", "1885", "1918", "l'Aisne"]])

S = []
# =================================================================== SALLE 1 — la place du village, août 1914 (Jeanne)
S.append({"num": 1, "titre": "Lettre n°1, août 1914 — La place du village : l'entrée en guerre", "enigmes": [
    E("1-1", "La frise de l'été 1914", "ordre",
      {"cm1": "La première lettre de Louis est tachée : les événements de l'été 1914 sont mélangés. Remets-les dans l'ordre, du plus ancien au plus récent.",
       "cm2": "Jeanne a noté dans son cahier les événements de l'été 1914, dans le désordre. Remets-les dans l'ordre chronologique."},
      BO + " ; " + MA + " ; " + CDM,
      "D'abord l'attentat de Sarajevo (28 juin 1914), puis l'affiche de la mobilisation générale (1er août 1914), puis la déclaration de guerre de l'Allemagne à la France (3 août 1914). En CM2 : la perte de l'Alsace et de la Moselle date de la guerre de 1870 ; l'Autriche-Hongrie déclare la guerre à la Serbie le 28 juillet 1914, un mois après l'attentat.",
      {"cm1": ["Tout commence par un attentat, en juin.", "L'affiche est collée au début du mois d'août.", "La déclaration de guerre arrive deux jours après l'affiche."],
       "cm2": ["La guerre de 1870 est la plus ancienne.", "Sarajevo : 28 juin 1914.", "Mobilisation le 1er août, déclaration de guerre le 3 août."]},
      cm1=ordre([("l'attentat de Sarajevo", "fin juin 1914"), ("l'affiche de la mobilisation générale", "début août 1914"), ("l'Allemagne déclare la guerre à la France", "début août 1914")]),
      cm2=ordre([("l'Alsace et la Moselle deviennent allemandes", "après la guerre de 1870"), ("l'attentat de Sarajevo", "28 juin 1914"),
                 ("l'Autriche-Hongrie déclare la guerre à la Serbie", "28 juillet 1914"), ("l'affiche de la mobilisation générale", "1er août 1914"),
                 ("l'Allemagne déclare la guerre à la France", "3 août 1914")]),
      lecon="causes"),
    E("1-2", "L'affiche de la mairie", "qcm",
      {"cm1": "Jeanne a recopié l'affiche collée sur la porte de la mairie. Lis-la, puis réponds aux questions." + AFFICHE,
       "cm2": "Jeanne a recopié l'affiche collée sur la porte de la mairie. Lis-la, puis réponds aux questions." + AFFICHE},
      BO + " ; " + MA,
      "L'affiche ordonne la mobilisation générale : les hommes soumis aux obligations militaires doivent rejoindre l'armée. Le premier jour de la mobilisation est le dimanche 2 août 1914 ; l'affiche est collée le 1er août dans toutes les communes. En CM2 : l'armée passe de 800 000 hommes à près de 3,6 millions ; tout le monde croit à une guerre courte.",
      {"cm1": ["Mobiliser, c'est appeler les soldats.", "Cherche « premier jour » dans l'affiche.", "Toutes les communes reçoivent l'affiche."],
       "cm2": ["« Mobilisation des armées » : on appelle les hommes.", "De 800 000 à près de 3,6 millions.", "On croit la guerre courte."]},
      cm1=qcm([("Que demande l'affiche ?", ["de fêter le 14 Juillet", "aux hommes mobilisables de rejoindre l'armée", "de fermer les écoles", "de partir en vacances"], 1, "C'est l'ordre de mobilisation générale."),
               ("Quel est le premier jour de la mobilisation ?", ["le 28 juin 1914", "le 2 août 1914", "le 11 novembre 1918", "le 14 juillet 1914"], 1, "C'est écrit sur l'affiche."),
               ("Où l'affiche est-elle collée ?", ["seulement à Paris", "dans toutes les communes de France", "seulement dans les casernes", "dans les journaux"], 1, "Chaque mairie la reçoit.")]),
      cm2=qcm([("Que veut dire « mobilisation générale » ?", ["une fête nationale", "l'appel de tous les hommes soumis aux obligations militaires", "la fermeture des frontières", "une élection"], 1, "Les hommes rejoignent l'armée."),
               ("Quel est le premier jour de la mobilisation ?", ["le 1er août 1914", "le 2 août 1914", "le 3 août 1914", "le 28 juin 1914"], 1, "Le dimanche 2 août 1914 ; l'affiche est collée la veille."),
               ("Combien d'hommes compte l'armée française après la mobilisation de 1914 ?", ["environ 80 000", "environ 800 000", "près de 3,6 millions", "près de 40 millions"], 2, "Elle passe de 800 000 à près de 3,6 millions d'hommes."),
               ("Que pensent la plupart des gens en août 1914 ?", ["que la guerre durera dix ans", "que la guerre sera courte", "qu'il n'y aura pas de guerre", "que la guerre est déjà finie"], 1, "Elle durera plus de quatre ans.")]),
      lecon="causes"),
    E("1-3", "Les deux camps", "tri",
      {"cm1": "Louis a dessiné une carte des alliances, mais les noms sont tombés. Range chaque pays dans son camp.",
       "cm2": "Louis a dessiné une carte des alliances de 1914. Range chaque pays dans son camp."},
      BO + " ; " + CDM,
      "La France, le Royaume-Uni et la Russie forment la Triple-Entente ; l'Allemagne et l'Autriche-Hongrie sont dans l'autre camp. En CM2 : la Serbie et la Belgique, envahie en août 1914, combattent avec la France ; l'Empire ottoman rejoint l'Allemagne à l'automne 1914. À cause des alliances, une crise locale devient une guerre européenne.",
      {"cm1": ["La France a deux grands alliés.", "L'Allemagne et l'Autriche-Hongrie sont ensemble.", "Le Royaume-Uni est le voisin de la France."],
       "cm2": ["La Serbie est attaquée par l'Autriche-Hongrie.", "La Belgique est envahie par l'Allemagne.", "L'Empire ottoman rejoint l'Allemagne."]},
      cm1=tri([("entente", "Le camp de la France (Triple-Entente)"), ("allem", "Le camp de l'Allemagne")],
              [("la France", "entente"), ("le Royaume-Uni", "entente"), ("la Russie", "entente"), ("l'Allemagne", "allem"), ("l'Autriche-Hongrie", "allem")]),
      cm2=tri([("entente", "Le camp de la France"), ("allem", "Le camp de l'Allemagne")],
              [("la France", "entente"), ("le Royaume-Uni", "entente"), ("la Russie", "entente"), ("la Serbie", "entente"), ("la Belgique", "entente"),
               ("l'Allemagne", "allem"), ("l'Autriche-Hongrie", "allem"), ("l'Empire ottoman", "allem")]),
      lecon="causes"),
    E("1-4", "La fleur au fusil ?", "vraifaux",
      "Sur une vieille carte postale, des soldats partent en souriant, une fleur au bout du fusil. Légende ou réalité ? Pour chaque phrase, choisis vrai ou faux.",
      BO + " ; " + MA + " ; " + CDM,
      "La plupart des mobilisés partent avec résignation et sens du devoir, pas dans la joie : la « fleur au fusil » est surtout une image de propagande et de cartes postales. Tout le monde croit à une guerre courte ; elle dure plus de quatre ans. Beaucoup de Français veulent retrouver l'Alsace et la Moselle, perdues en 1871.",
      {"cm2": ["Une carte postale peut embellir la réalité.", "On pensait rentrer vite.", "L'Alsace et la Moselle étaient allemandes depuis 1871."]},
      commun=vf([("Tous les soldats partent en chantant de joie.", False, "La plupart partent avec résignation et sens du devoir."),
                 ("La « fleur au fusil » est surtout une image de cartes postales.", True, "Elle embellit la réalité."),
                 ("En août 1914, presque tout le monde croit que la guerre sera courte.", True, "Elle durera plus de quatre ans."),
                 ("Beaucoup de Français veulent retrouver l'Alsace et la Moselle.", True, "Elles sont allemandes depuis la guerre de 1870."),
                 ("Les soldats savent qu'ils partent pour quatre ans.", False, "Personne ne l'imagine en 1914.")]),
      lecon="causes", cm2_seul=True),
]})

# =================================================================== SALLE 2 — l'abri de la tranchée, 1916 (Louis)
S.append({"num": 2, "titre": "Lettre n°2, printemps 1916 — La tranchée : la vie des poilus", "enigmes": [
    E("2-1", "Le croquis de Louis", "plan",
      {"cm1": "Dans sa lettre, Louis a dessiné la coupe de sa tranchée, mais il n'a pas eu le temps d'écrire les mots. Place chaque mot sur son repère : clique sur une étiquette, puis sur la case du repère." + tranchee(3),
       "cm2": "Louis a dessiné la coupe de sa tranchée. Place chaque mot sur son repère. Attention : il y a des étiquettes en trop." + tranchee(5)},
      BO + " ; " + CDM,
      "Le repère 1 montre les sacs de sable qui protègent le haut de la tranchée, le repère 2 les barbelés, le repère 3 l'abri creusé sous terre. En CM2 : le repère 4 est la banquette de tir, la marche où le soldat monte pour guetter ; le repère 5 est le no man's land, la terre de personne entre les deux lignes. Le boyau, qui relie la tranchée à l'arrière, et la mairie ne sont pas sur ce dessin.",
      {"cm1": ["Les sacs de sable sont empilés en haut.", "Les barbelés sont devant, côté ennemi.", "L'abri est sous terre, au fond."],
       "cm2": ["La banquette de tir est une marche.", "Le no man's land est entre les lignes.", "Le boyau n'est pas visible sur une coupe."]},
      cm1=plan("Le croquis de Louis", 3, ["les sacs de sable", "les barbelés", "l'abri"], ["les sacs de sable", "les barbelés", "l'abri"]),
      cm2=plan("Le croquis de Louis", 2, ["les sacs de sable", "les barbelés", "l'abri", "la banquette de tir", "le no man's land"],
               ["les sacs de sable", "les barbelés", "l'abri", "la banquette de tir", "le no man's land", "le boyau", "la mairie"]),
      lecon="front"),
    E("2-2", "La vie dans la tranchée", "vraifaux",
      {"cm1": "Louis raconte sa vie de poilu. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Louis raconte sa vie de poilu, mais une partie de sa lettre a été barrée par la censure. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + CDM,
      "Les poilus vivent dans la boue et le froid, avec les rats et les poux ; pour tenir, ils écrivent et reçoivent des lettres et des colis. « Poilu » est le surnom des soldats français. En CM2 : la censure lit le courrier ; les soldats ne peuvent pas écrire où ils sont ; la camaraderie les aide à tenir.",
      {"cm1": ["Pense à la pluie dans un trou de terre.", "Les colis viennent de la famille.", "« Poilu » est un surnom."],
       "cm2": ["La censure surveille les lettres.", "Louis ne peut pas écrire le nom du lieu.", "Les camarades s'entraident."]},
      cm1=vf([("Dans la tranchée, les soldats vivent souvent dans la boue et le froid.", True, "La pluie remplit les tranchées."),
              ("Les poilus reçoivent des lettres et des colis de leur famille.", True, "Cela les aide à tenir."),
              ("Les soldats dorment dans des hôtels près du front.", False, "Ils dorment dans des abris creusés sous terre.")]),
      cm2=vf([("On appelle « poilus » les soldats français de la Grande Guerre.", True, "C'est leur surnom."),
              ("Les soldats peuvent écrire dans leurs lettres le lieu exact où ils se trouvent.", False, "La censure l'interdit."),
              ("Les rats et les poux font partie de la vie dans les tranchées.", True, "Les conditions de vie sont très dures."),
              ("La camaraderie aide les soldats à tenir.", True, "Ils partagent les colis et les nouvelles."),
              ("Le courrier des soldats n'est jamais lu par personne.", False, "La censure surveille le courrier.")]),
      lecon="front"),
    E("2-3", "Verdun ou la Somme ?", "tri",
      {"cm1": "Louis a mélangé ses notes sur deux grandes batailles de 1916. Range chaque carte sous la bonne bataille.",
       "cm2": "Louis a mélangé ses notes sur les deux grandes batailles de 1916. Range chaque carte sous la bonne bataille."},
      BO + " ; " + CDM,
      "Verdun commence le 21 février 1916 et se termine le 18 décembre 1916 : l'armée française y résiste aux attaques allemandes. La Somme commence le 1er juillet 1916 : les Britanniques et les Français y attaquent ensemble, jusqu'au 18 novembre ; les premiers chars britanniques y apparaissent.",
      {"cm1": ["Verdun commence en février.", "À la Somme, les Britanniques sont là.", "Les deux batailles ont lieu en 1916."],
       "cm2": ["Verdun : de février à décembre.", "Somme : de juillet à novembre.", "Les premiers chars sont britanniques."]},
      cm1=tri([("verdun", "Verdun"), ("somme", "La Somme")],
              [("commence en février 1916", "verdun"), ("l'armée française résiste aux attaques allemandes", "verdun"),
               ("commence en juillet 1916", "somme"), ("Britanniques et Français attaquent ensemble", "somme")]),
      cm2=tri([("verdun", "Verdun"), ("somme", "La Somme")],
              [("du 21 février au 18 décembre 1916", "verdun"), ("l'armée française résiste aux attaques allemandes", "verdun"), ("près de la Meuse", "verdun"),
               ("du 1er juillet au 18 novembre 1916", "somme"), ("Britanniques et Français attaquent ensemble", "somme"), ("apparition des premiers chars britanniques", "somme")]),
      lecon="front"),
    E("2-4", "Les camarades de Louis", "qcm",
      "Louis parle de ses camarades et des armes qu'il découvre. Réponds aux questions.",
      BO + " ; " + CDM + " ; " + UNIV,
      "La guerre utilise des armes nouvelles ou bien plus nombreuses : mitrailleuses, canons lourds, gaz (à partir de 1915), avions, chars (1916). Environ 600 000 soldats venus des colonies (Afrique du Nord, Afrique de l'Ouest, Madagascar, Indochine) combattent dans l'armée française. Le masque protège des gaz.",
      {"cm2": ["Les chars apparaissent en 1916.", "Environ 600 000 soldats des colonies.", "Le masque protège des gaz."]},
      commun=qcm([("Quelle arme apparaît pour la première fois pendant cette guerre ?", ["l'épée", "le char d'assaut", "l'arc", "le canon à boulets de pierre"], 1, "Les premiers chars sont britanniques, en 1916."),
                  ("Pourquoi Louis porte-t-il un masque ?", ["pour se déguiser", "pour se protéger des gaz de combat", "pour avoir chaud", "pour ne pas être reconnu"], 1, "Les gaz sont employés à partir de 1915."),
                  ("Amadou, le camarade de Louis, vient du Sénégal. Combien de soldats venus des colonies combattent dans l'armée française ?", ["environ 6 000", "environ 60 000", "environ 600 000", "environ 6 millions"], 2, "D'Afrique du Nord, d'Afrique de l'Ouest, de Madagascar, d'Indochine."),
                  ("Laquelle de ces armes est utilisée en grand nombre ?", ["la catapulte", "la mitrailleuse", "l'arbalète", "le bélier"], 1, "Avec les canons lourds.")]),
      lecon="front", cm2_seul=True),
]})

# =================================================================== SALLE 3 — l'usine d'obus, 1917 (Marcelle)
S.append({"num": 3, "titre": "Lettre n°3, 1917 — L'usine et les champs : l'arrière", "enigmes": [
    E("3-1", "Les photos du journal", "intrus",
      {"cm1": "Marcelle a découpé des photos dans le journal pour montrer à Louis ce que font les femmes pendant la guerre. Une carte ne va pas : trouve l'intruse.",
       "cm2": "Marcelle a découpé des légendes de photos dans le journal pour montrer ce que font les femmes pendant la guerre. Une légende est fausse : trouve l'intruse."},
      BO + " ; " + UNIV,
      "Pendant la guerre, les femmes remplacent les hommes : elles moissonnent, fabriquent des obus, conduisent les tramways, soignent les blessés. Mais elles ne votent pas encore : en France, elles n'obtiendront le droit de vote qu'en 1944.",
      {"cm1": ["Toutes les cartes sauf une montrent un travail.", "Les femmes ne votent pas encore en 1917.", "Le droit de vote des femmes arrive bien plus tard."],
       "cm2": ["Une seule légende est fausse.", "Pense au droit de vote.", "Les femmes votent en France à partir de 1944."]},
      cm1=intrus([("Une femme fait la moisson.", False), ("Une ouvrière fabrique des obus.", False), ("Une infirmière soigne un blessé.", False), ("Des femmes votent aux élections de 1917.", True)]),
      cm2=intrus([("Des paysannes font les vendanges à la place des hommes.", False), ("Une munitionnette remplit des obus à l'usine.", False),
                  ("Une conductrice de tramway fait sa tournée.", False), ("Une factrice distribue le courrier.", False),
                  ("Une femme est élue députée en 1917.", True)]),
      lecon="arriere"),
    E("3-2", "Le front ou l'arrière ?", "tri",
      {"cm1": "Marcelle explique à Jeanne la différence entre le front et l'arrière. Range chaque carte dans la bonne colonne.",
       "cm2": "Marcelle range les nouvelles reçues cette semaine. Range chaque carte : sur le front, ou à l'arrière."},
      BO + " ; " + UNIV + " ; " + CDM,
      "Le front, c'est la ligne des tranchées et des combats. L'arrière, c'est tout le reste du pays : les usines, les champs, les écoles, les familles qui attendent les lettres. En CM2 : l'hôpital installé dans une école de l'arrière accueille les blessés ; les colis partent de l'arrière vers le front.",
      {"cm1": ["Le front : les tranchées.", "L'arrière : le village, l'usine, l'école.", "Les familles sont à l'arrière."],
       "cm2": ["Où vit Marcelle ?", "Où sont les barbelés ?", "Les colis sont préparés à l'arrière."]},
      cm1=tri([("front", "Sur le front"), ("arriere", "À l'arrière")],
              [("les tranchées", "front"), ("les barbelés", "front"), ("l'usine d'obus", "arriere"), ("l'école du village", "arriere"), ("les champs de blé", "arriere")]),
      cm2=tri([("front", "Sur le front"), ("arriere", "À l'arrière")],
              [("la banquette de tir", "front"), ("le no man's land", "front"), ("les abris creusés sous terre", "front"),
               ("l'usine d'obus", "arriere"), ("les vendanges", "arriere"), ("l'hôpital installé dans une école", "arriere"), ("la préparation des colis", "arriere")]),
      lecon="arriere"),
    E("3-3", "Le carnet de l'usine", "trous",
      {"cm1": "Le carnet de Marcelle a pris l'eau. Complète-le avec les bonnes étiquettes.",
       "cm2": "Le carnet de Marcelle a pris l'eau. Complète-le. Attention : il y a des étiquettes en trop."},
      BO + " ; " + UNIV,
      "Les femmes remplacent les hommes partis au front ; celles qui fabriquent des obus sont appelées munitionnettes. Toute l'économie travaille pour la guerre : c'est l'économie de guerre. En CM2 : environ 430 000 femmes travaillent dans les usines d'armement en 1918 ; des travailleurs venus des colonies et de pays étrangers, comme environ 40 000 ouvriers chinois, travaillent aussi en France.",
      {"cm1": ["Les hommes sont partis au front.", "Elles fabriquent des munitions.", "Les usines fabriquent des obus."],
       "cm2": ["430 000 en 1918.", "Environ 40 000 ouvriers venus de Chine.", "L'économie travaille pour la guerre."]},
      cm1={"texte": "<p>Les hommes sont partis au [[front]]. À l'usine, les femmes les [[remplacent]]. Celles qui fabriquent des obus s'appellent les [[munitionnettes]].</p>",
           "etiquettes": ["front", "remplacent", "munitionnettes"]},
      cm2={"texte": "<p>Toute l'[[économie]] travaille pour la guerre : l'usine fabrique des [[obus]] au lieu de vélos. En 1918, environ [[430 000]] femmes travaillent dans les usines d'armement : on les appelle les [[munitionnettes]]. Des travailleurs venus des [[colonies]] et de l'étranger, comme environ [[40 000]] ouvriers chinois, travaillent aussi en France.</p>",
           "etiquettes": ["économie", "obus", "430 000", "munitionnettes", "colonies", "40 000", "4 300", "infirmières", "tranchées"]},
      lecon="arriere"),
    E("3-4", "Qui fait quoi à l'arrière ?", "association",
      "Marcelle présente à Louis les personnes qu'elle croise chaque jour. Relie chaque personne à ce qu'elle fait pendant la guerre.",
      BO + " ; " + UNIV,
      "La munitionnette remplit des obus à l'usine ; la paysanne moissonne à la place des hommes ; l'infirmière soigne les blessés à l'hôpital ; l'écolier écrit aux soldats et collecte des vêtements ; l'ouvrier venu de Chine travaille à l'usine ou au port.",
      {"cm2": ["L'infirmière est à l'hôpital.", "L'écolier écrit des lettres.", "Les ouvriers venus de loin travaillent aux usines et aux ports."]},
      commun=assoc([("la munitionnette", "remplit des obus à l'usine"), ("la paysanne", "moissonne à la place des hommes"),
                    ("l'infirmière", "soigne les blessés"), ("l'écolier", "écrit aux soldats et collecte des vêtements"),
                    ("l'ouvrier venu de Chine", "travaille à l'usine ou au port")]),
      lecon="arriere", cm2_seul=True),
]})

# =================================================================== SALLE 4 — l'hôpital de l'école, 11 novembre 1918 (Odette)
S.append({"num": 4, "titre": "Lettre n°4, 11 novembre 1918 — L'hôpital de l'école : l'armistice", "enigmes": [
    E("4-1", "Les dates de la guerre", "ordre",
      {"cm1": "Odette a écrit les grandes dates de la guerre sur des étiquettes de pansements, qui se sont mélangées. Remets-les dans l'ordre.",
       "cm2": "Odette affiche au mur de l'hôpital les grandes étapes de la guerre. Remets-les dans l'ordre chronologique."},
      BO + " ; " + CDM,
      "La guerre commence en août 1914 ; Verdun a lieu en 1916 ; l'armistice est signé le 11 novembre 1918 ; le traité de Versailles est signé le 28 juin 1919. En CM2 : l'attentat de Sarajevo (28 juin 1914) est le point de départ ; les États-Unis entrent en guerre en avril 1917.",
      {"cm1": ["La guerre commence en 1914.", "Verdun, c'est en 1916.", "La paix est signée après l'armistice."],
       "cm2": ["Sarajevo : 1914.", "Les États-Unis : avril 1917.", "Versailles : 28 juin 1919."]},
      cm1=ordre([("le début de la guerre", "1914"), ("la bataille de Verdun", "1916"), ("l'armistice", "1918"), ("le traité de Versailles", "1919")]),
      cm2=ordre([("l'attentat de Sarajevo", "28 juin 1914"), ("la bataille de Verdun", "21 février 1916"), ("l'entrée en guerre des États-Unis", "avril 1917"),
                 ("l'armistice", "11 novembre 1918"), ("le traité de Versailles", "28 juin 1919")]),
      lecon="armistice"),
    E("4-2", "Les cloches du 11 novembre", "qcm",
      {"cm1": "Ce matin, les cloches sonnent. Odette explique aux blessés ce qui se passe. Réponds aux questions.",
       "cm2": "Odette lit aux blessés le journal du 11 novembre 1918. Réponds aux questions."},
      BO + " ; " + CDM,
      "Un armistice est un accord qui arrête les combats ; ce n'est pas encore la paix. Il est signé le 11 novembre 1918 à 5 h 15 dans la clairière de Rethondes, en forêt de Compiègne ; à 11 heures, les clairons et les cloches annoncent la fin des combats. En CM2 : la paix sera signée à Versailles le 28 juin 1919.",
      {"cm1": ["Armistice : on arrête de se battre.", "La date est dans le titre de la lettre.", "Les cloches sonnent à 11 heures."],
       "cm2": ["Rethondes est dans la forêt de Compiègne.", "5 h 15 pour la signature, 11 h pour la fin des combats.", "La paix vient plus tard, à Versailles."]},
      cm1=qcm([("Qu'est-ce qu'un armistice ?", ["un accord qui arrête les combats", "une grande bataille", "une fête de village", "une nouvelle arme"], 0, "Ce n'est pas encore la paix."),
               ("Quel jour l'armistice est-il signé ?", ["le 14 juillet 1914", "le 11 novembre 1918", "le 28 juin 1919", "le 1er août 1914"], 1, "Le 11 novembre 1918."),
               ("À quelle heure les combats s'arrêtent-ils ?", ["à minuit", "à 11 heures", "à 5 heures du soir", "à midi le lendemain"], 1, "Les cloches sonnent à 11 heures.")]),
      cm2=qcm([("Où l'armistice est-il signé ?", ["à Versailles", "dans la clairière de Rethondes, en forêt de Compiègne", "à Verdun", "à Sarajevo"], 1, "En forêt de Compiègne, dans l'Oise."),
               ("À quelle heure est-il signé ?", ["à 5 h 15", "à 11 h", "à midi", "à 20 h"], 0, "Les combats s'arrêtent à 11 heures."),
               ("L'armistice, est-ce la paix ?", ["oui, la guerre est finie pour toujours", "non, il arrête les combats ; la paix est signée en 1919", "non, la guerre reprend en 1919", "oui, c'est le traité de Versailles"], 1, "La paix : traité de Versailles, 28 juin 1919."),
               ("Quel pays est entré en guerre en 1917 aux côtés de la France ?", ["la Russie", "les États-Unis", "l'Autriche-Hongrie", "l'Allemagne"], 1, "En avril 1917 ; la même année, la Russie arrête bientôt de combattre.")]),
      lecon="armistice"),
    E("4-3", "Les chiffres du registre", "association",
      {"cm1": "Dans le registre de l'hôpital, Odette a noté des nombres. Relie chaque nombre à ce qu'il compte.",
       "cm2": "Odette recopie les chiffres officiels publiés après la guerre. Relie chaque nombre à ce qu'il compte."},
      BO + " ; " + CDM + " ; " + MA,
      "Près de 1,4 million de soldats français sont morts ; la guerre a duré plus de quatre ans ; les combats s'arrêtent à 11 heures le 11 novembre 1918. En CM2 : 8,7 millions de Français ont été mobilisés pendant toute la guerre ; la guerre laisse près de 600 000 veuves ; la paix est signée le 28 juin 1919.",
      {"cm1": ["Le plus grand nombre : les soldats morts.", "1914 à 1918 : compte les années.", "Les cloches sonnent à cette heure-là."],
       "cm2": ["8,7 millions : tous les mobilisés.", "1,4 million : les soldats français morts.", "600 000 : les veuves."]},
      cm1=assoc([("près de 1,4 million", "soldats français morts"), ("plus de 4 ans", "la durée de la guerre"), ("11 heures", "l'heure où les combats s'arrêtent")]),
      cm2=assoc([("8,7 millions", "Français mobilisés pendant la guerre"), ("près de 1,4 million", "soldats français morts"), ("près de 600 000", "veuves de guerre en France"),
                 ("5 h 15", "l'heure de la signature de l'armistice"), ("28 juin 1919", "la signature du traité de Versailles")]),
      lecon="armistice"),
    E("4-4", "Le journal de 1919", "trous",
      "Un an plus tard, Odette colle dans son cahier un article sur le traité de paix. Complète-le. Attention : il y a des étiquettes en trop.",
      BO + " ; " + CDM,
      "La paix est signée le 28 juin 1919 à Versailles, dans la galerie des Glaces. L'Allemagne est déclarée responsable de la guerre : elle rend l'Alsace et la Moselle à la France, doit payer des réparations et réduire son armée. Beaucoup d'Allemands vivent ce traité avec colère.",
      {"cm2": ["Le traité porte le nom d'un château.", "L'Alsace et la Moselle reviennent à la France.", "Les vaincus sont en colère."]},
      commun={"texte": "<p>Le traité de paix est signé le 28 juin 1919 à [[Versailles]], dans la galerie des Glaces. L'[[Allemagne]] est déclarée responsable de la guerre. Elle rend l'Alsace et la [[Moselle]] à la France, doit payer des [[réparations]] et réduire son [[armée]]. Beaucoup d'Allemands vivent ce traité avec [[colère]].</p>",
              "etiquettes": ["Versailles", "Allemagne", "Moselle", "réparations", "armée", "colère", "Verdun", "Russie", "joie"]},
      lecon="armistice", cm2_seul=True),
]})

# =================================================================== SALLE 5 — le monument aux morts, 11 novembre 1922 (le maire)
S.append({"num": 5, "titre": "Lettre n°5, 1922 — Le monument aux morts : se souvenir", "enigmes": [
    E("5-1", "Le plan du monument", "plan",
      {"cm1": "Le maire montre le plan du monument aux morts que l'on inaugure aujourd'hui. Place chaque mot sur son repère." + monument(3),
       "cm2": "Le maire montre le plan du monument aux morts. Place chaque mot sur son repère. Attention : il y a des étiquettes en trop." + monument(5)},
      BO + " ; " + CDM + " ; " + ONAC,
      "Le repère 1 montre la statue du poilu, le repère 2 la liste des noms des soldats de la commune morts pour la France, le repère 3 les dates de la guerre (1914-1918). En CM2 : le repère 4 est la croix de guerre, une décoration ; le repère 5 est la gerbe de fleurs déposée le 11 novembre. Les barbelés et l'affiche de mobilisation n'ont pas leur place sur un monument.",
      {"cm1": ["La statue est en haut.", "Les noms sont gravés sur la face du monument.", "Les dates sont au-dessus des noms."],
       "cm2": ["La croix de guerre est une décoration.", "La gerbe est au pied du monument.", "Deux étiquettes ne vont pas sur un monument."]},
      cm1=plan("Le monument de Vaux-les-Tilleuls", 3, ["la statue du poilu", "la liste des noms", "les dates de la guerre"], ["la statue du poilu", "la liste des noms", "les dates de la guerre"]),
      cm2=plan("Le monument de Vaux-les-Tilleuls", 2, ["la statue du poilu", "la liste des noms", "les dates de la guerre", "la croix de guerre", "la gerbe de fleurs"],
               ["la statue du poilu", "la liste des noms", "les dates de la guerre", "la croix de guerre", "la gerbe de fleurs", "les barbelés", "l'affiche de mobilisation"]),
      lecon="memoire"),
    E("5-2", "Le discours du maire", "vraifaux",
      {"cm1": "Le maire prépare son discours pour l'inauguration. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Le maire prépare son discours. Il parle du souvenir, mais aussi de l'inquiétude pour l'avenir. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + CDM + " ; " + GOUV + " ; " + MDH,
      "Presque chaque commune de France construit un monument aux morts, surtout au début des années 1920 ; on y grave les noms des soldats morts pour la France. Le 11 novembre devient un jour férié par la loi du 24 octobre 1922. En CM2 : le Soldat inconnu repose sous l'Arc de Triomphe depuis 1920 ; la guerre laisse colère et difficultés, et des partis extrémistes en profitent : en Italie, Mussolini prend le pouvoir en 1922 et supprime peu à peu les libertés.",
      {"cm1": ["Presque chaque village a son monument.", "On y grave les noms.", "Le 11 novembre, on se rassemble."],
       "cm2": ["Le Soldat inconnu est à Paris.", "La loi de 1922 rend le 11 novembre férié.", "En Italie, la démocratie recule."]},
      cm1=vf([("Presque chaque commune de France a construit un monument aux morts.", True, "Surtout au début des années 1920."),
              ("Sur le monument, on grave les noms des soldats de la commune morts pour la France.", True, "Pour ne pas les oublier."),
              ("Le 11 novembre, on se rassemble devant le monument aux morts.", True, "C'est un jour de souvenir."),
              ("On a construit les monuments pour fêter la guerre.", False, "Ils servent à se souvenir des morts.")]),
      cm2=vf([("Le 11 novembre est devenu un jour férié avec la loi du 24 octobre 1922.", True, "On se rassemble devant le monument."),
              ("Le Soldat inconnu repose sous l'Arc de Triomphe, à Paris.", True, "Il représente tous les morts de la guerre."),
              ("Après la guerre, la paix est solide et tous les pays sont satisfaits.", False, "La colère des vaincus et les difficultés rendent la paix fragile."),
              ("En Italie, en 1922, Mussolini prend le pouvoir et supprime peu à peu les libertés.", True, "Des partis extrémistes profitent de la colère."),
              ("Aujourd'hui, on ne peut plus rien savoir des soldats morts en 1914-1918.", False, "La base « Mémoire des hommes » garde la fiche de chacun.")]),
      lecon="memoire"),
    E("5-3", "Le registre des noms", "qcm",
      {"cm1": "Le maire a recopié les noms à graver sur le monument. Lis le registre, puis réponds aux questions." + REGISTRE,
       "cm2": "Le maire a recopié les noms à graver sur le monument. Mène l'enquête dans le registre, puis réponds aux questions." + REGISTRE},
      BO + " ; " + MDH,
      "Le registre compte 7 noms ; deux soldats sont morts en 1916 (à Verdun et dans la Somme) ; René Masson, né en 1899 et mort en 1918, était le plus jeune (environ 19 ans). En CM2 : Albert Petit (1885-1918) était le plus âgé (environ 33 ans) ; Paul Bernard est mort en 1914, la première année de la guerre ; Lucien Dubois est mort à Verdun, la bataille qui dure de février à décembre 1916. Les noms du registre sont inventés ; pour une vraie enquête, on consulte Mémoire des hommes.",
      {"cm1": ["Compte les lignes du tableau.", "Cherche 1916 dans la colonne « Mort pour la France en ».", "Calcule : année de la mort moins année de naissance."],
       "cm2": ["Le plus âgé est né le plus tôt.", "1914 est la première année de la guerre.", "Cherche la bataille dans la colonne « Lieu »."]},
      cm1=qcm([("Combien de noms le registre compte-t-il ?", ["5", "6", "7", "8"], 2, "Sept soldats de la commune."),
               ("Combien de soldats du registre sont morts en 1916 ?", ["1", "2", "3", "aucun"], 1, "Lucien Dubois et Marcel Fabre."),
               ("Qui était le plus jeune au moment de sa mort ?", ["Paul Bernard", "René Masson", "Albert Petit", "Henri Colin"], 1, "Né en 1899, mort en 1918 : environ 19 ans.")]),
      cm2=qcm([("Qui était le plus âgé au moment de sa mort ?", ["Joseph Garnier", "Albert Petit", "Henri Colin", "Paul Bernard"], 1, "Né en 1885, mort en 1918 : environ 33 ans."),
               ("Quel soldat est mort la première année de la guerre ?", ["Paul Bernard", "Henri Colin", "René Masson", "Marcel Fabre"], 0, "En 1914, dans la Marne."),
               ("Lucien Dubois est mort pendant une bataille de 1916 qui a duré de février à décembre. Laquelle ?", ["la Somme", "Verdun", "la Marne", "l'Artois"], 1, "Du 21 février au 18 décembre 1916."),
               ("Pour retrouver la fiche d'un vrai soldat mort pour la France, quelle base consulter ?", ["Mémoire des hommes", "le cadastre", "l'annuaire", "le dictionnaire"], 0, "Base du ministère des Armées.")]),
      lecon="memoire"),
    E("5-4", "La date de la dernière lettre", "code",
      "La dernière lettre est fermée par un cadenas à date. Jeanne a écrit : « J'ai écrit cette lettre le jour de l'inauguration du monument : le même jour et le même mois que l'armistice, l'année où une loi a fait de ce jour un jour férié. » Trouve le jour, le mois (en chiffres) et l'année.",
      BO + " ; " + GOUV + " ; " + CDM,
      "L'armistice est signé le 11 novembre 1918 : le jour est 11 et le mois est 11 (novembre est le onzième mois). La loi qui fait du 11 novembre un jour férié date du 24 octobre 1922 : l'année est 1922. La lettre est datée du 11 novembre 1922.",
      {"cm2": ["Le jour de l'armistice : 11.", "Novembre est le onzième mois.", "La loi du 24 octobre 1922."]},
      commun=code([("Jour", "11"), ("Mois", "11"), ("Année", "1922")]),
      lecon="memoire", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "Les Lettres du poilu", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données. Repères en CM1, dates exactes et chiffres officiels en CM2.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": " ; ".join([BO, CDM, MA, UNIV, MDH, GOUV, ONAC]) + ". Détail : README.md, section Sources.",
            "vigilance": "SUJET SENSIBLE : ton du souvenir, aucun détail violent, aucune photo de blessé, aucun « gagner la guerre » comme mécanisme ; village, famille Garnier, registre et personnages inventés ; les personnes réelles ne parlent jamais.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e2-1\",\"legende\":\"…\",\"source\":\"…\"}. Les schémas (tranchée, monument, frise) sont dessinés en SVG par script : ne jamais les remplacer par des images générées par IA. Documents d'époque réels : seulement des photos d'archives libres (Wikimedia Commons, Europeana), jamais de blessés."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
