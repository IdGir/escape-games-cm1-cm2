"""Salle 4 « La mare et le pré fleuri » : grades mousse, lieutenant, second (fiche : L'écosystème)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "vivant-ecosystemes", "tests", "donnees"))
from fiches import *
from schemas import mare

FICHE = "« L'écosystème »"


def _plan_mare(n, cases, etiq, consigne, indices, j=None):
    b = {"type": "plan", "titre": "La mare de Rose", "colonnes": 2 if n > 3 else 3,
         "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(cases)], "etiquettes": etiq,
         "consigne": consigne + mare(n), "indices": indices}
    if j:
        b["justification"] = j
    return b


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": _plan_mare(3, ["le soleil", "l'eau", "un roseau"], ["le soleil", "l'eau", "un roseau"],
                             "Place chaque mot sur son repère.",
                             ["Ouvre la fiche " + FICHE + ".", "Le soleil est en haut à droite.", "Le roseau est une grande herbe de la berge."]),
        "lieutenant": _plan_mare(5, ["la lumière", "l'eau", "un roseau", "une grenouille", "la vase"],
                                 ["la lumière", "l'eau", "un roseau", "une grenouille", "la vase", "l'altitude", "un sapin"],
                                 "Place chaque mot sur son repère (deux sont en trop), puis choisis la phrase de la fiche qui dit comment on décrit un milieu de vie.",
                                 ["La vase est au fond de la mare.", "L'altitude ne se dessine pas sur une coupe.", "Pour la justification : cherche « caractéristiques physiques »."],
                                 J("Quelle phrase de la fiche dit comment on décrit un milieu de vie ?", E_MILIEU, [E_DEF, E_PRESENCE, E_AQUA], pos=1)),
        "second": tri(
            "Rose compare la mare et la forêt de chênes. Range chaque être vivant dans l'écosystème où Rose l'a observé, puis choisis la phrase de la fiche sur l'écosystème aquatique.",
            [("mare", "La mare (écosystème aquatique)"), ("foret", "La forêt (écosystème terrestre)")],
            [("le nénuphar", "mare"), ("la larve de libellule", "mare"), ("la paramécie", "mare"), ("la perche", "mare"),
             ("le chêne", "foret"), ("le pic épeiche", "foret"), ("le chevreuil", "foret")],
            ["La larve de libellule vit sous l'eau.", "Le pic tambourine sur les troncs.", "Pour la justification : cherche « oxygène dissous »."],
            J("Quelle phrase de la fiche décrit la vie dans un écosystème aquatique ?", E_AQUA, [E_DEF, E_EXEMPLES, E_MILIEU], pos=3)),
    }
    d["e4-2"] = {
        "mousse": tri(
            "Range chaque chose : est-elle vivante ou non ?",
            [("vivant", "Vivant"), ("non", "Non vivant")],
            [("la grenouille", "vivant"), ("le roseau", "vivant"), ("la pluie", "non"), ("la lumière", "non")],
            ["Ouvre la fiche " + FICHE + ".", "Un être vivant naît et grandit.", "La pluie ne grandit pas."]),
        "lieutenant": tri(
            "Rose a noté des relations entre êtres vivants. Range chacune : prédation ou coopération. Puis choisis la phrase de la fiche qui définit la coopération.",
            [("pred", "Prédation"), ("coop", "Coopération")],
            [("le héron et la grenouille", "pred"), ("la larve de libellule et le têtard", "pred"), ("l'épervier et la mésange", "pred"),
             ("l'abeille et la fleur de trèfle", "coop"), ("le papillon et la fleur de sauge", "coop")],
            ["Le prédateur mange sa proie.", "Le papillon boit le nectar et transporte le pollen.", "Pour la justification : cherche « chacun gagne »."],
            J("Quelle phrase de la fiche définit la coopération ?", E_COOPERATION, [E_PREDATION, E_DEF, E_PRESENCE], pos=0)),
        "second": vf(
            "Rose discute avec le garde de l'avenir de la mare. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les écosystèmes qui changent.",
            [("Un écosystème peut se rétablir après une perturbation, mais pas sans limites.", True, "Il est dynamique."),
             ("Un écosystème ne change jamais au fil des saisons.", False, "La mare change de l'été à l'hiver."),
             ("Une vigne de Bourgogne est aussi un écosystème.", True, "Un milieu, des êtres vivants, des relations."),
             ("Un écosystème, ce sont seulement les animaux d'un lieu.", False, "Il y a aussi le milieu, les plantes et les relations."),
             ("L'humidité d'un lieu influe sur les êtres vivants qu'on y trouve.", True, "Les mousses aiment l'humidité.")],
            ["Après une crue, la mare se remet peu à peu.", "Un écosystème a trois parties.", "Pour la justification : cherche « certaines limites »."],
            J("Quelle phrase de la fiche dit qu'un écosystème change ?", E_CHANGE, [E_SAISON, E_DEF, E_EXEMPLES], pos=2)),
    }
    d["e4-3"] = {
        "mousse": qcm(
            "Rose pose deux questions. Choisis la bonne réponse.",
            [("Le héron attrape une grenouille. Le héron est…", ["la proie", "le prédateur", "une plante", "le milieu"], 1, "Il mange la grenouille."),
             ("L'abeille butine la fleur. Qui y gagne ?", ["l'abeille seulement", "les deux", "personne", "la fleur seulement"], 1, "C'est une coopération.")],
            ["Ouvre la fiche " + FICHE + ".", "Le prédateur mange.", "L'abeille boit le nectar et transporte le pollen."]),
        "lieutenant": qcm(
            "L'hiver approche. Rose explique comment la mare change. Choisis la bonne réponse, puis la phrase de la fiche sur la mauvaise saison.",
            [("Que fait la grenouille en hiver ?", ["elle part en Afrique", "elle s'enfouit dans la vase", "elle pond", "elle chasse les abeilles"], 1, "Elle ralentit."),
             ("Que fait le chêne à la mauvaise saison ?", ["il perd ses feuilles", "il fleurit", "il grandit plus vite", "il pond des glands"], 0, "Il ralentit lui aussi."),
             ("Comment respirent la plupart des êtres vivants sous l'eau de la mare ?", ["ils ne respirent pas", "avec l'oxygène dissous dans l'eau ou en remontant à la surface", "seulement la nuit", "avec la vase"], 1, "Écosystème aquatique."),
             ("Pourquoi la grenouille vit-elle près d'une mare ET d'une prairie ?", ["pour pondre dans l'eau et chasser les insectes", "pour fuir la pluie", "pour manger de l'herbe", "pour dormir au soleil"], 0, "Elle a besoin des deux.")],
            ["En hiver, beaucoup d'êtres vivants ralentissent.", "La grenouille pond dans l'eau.", "Pour la justification : cherche « mauvaise saison »."],
            J("Quelle phrase de la fiche décrit la mauvaise saison ?", E_SAISON, [E_CHANGE, E_AQUA, E_GRENOUILLE], pos=3)),
        "second": assoc(
            "Rose explique où vit chaque être vivant de la réserve. Relie chacun à ce dont il a besoin, puis choisis la phrase de la fiche sur la grenouille.",
            [("la grenouille", "de la mare pour pondre et de la prairie pour chasser"), ("le nénuphar", "une eau calme et ensoleillée"),
             ("la mousse", "un endroit humide et ombragé"), ("l'abeille", "des fleurs pour leur nectar"), ("le héron cendré", "une eau peu profonde pour pêcher")],
            ["La grenouille a besoin de deux milieux.", "La mousse fuit le plein soleil.", "Pour la justification : cherche « prairie voisine »."],
            J("Quelle phrase de la fiche explique les besoins de la grenouille ?", E_GRENOUILLE, [E_PRESENCE, E_PREDATION, E_SAISON], pos=1)),
    }
    d["e4-4"] = {
        "lieutenant": assoc(
            "Rose prépare les panneaux du sentier. Relie chaque être vivant à ce qui explique sa présence, puis choisis la phrase de la fiche qui relie êtres vivants et milieu.",
            [("le nénuphar au milieu de la mare", "une eau calme et ensoleillée"), ("la mousse au pied des chênes", "un endroit humide et ombragé"),
             ("les ruches dans le pré", "beaucoup de fleurs au printemps"), ("le héron au bord de l'eau", "une eau peu profonde"),
             ("la larve de libellule sous l'eau", "de l'oxygène dissous dans l'eau")],
            ["Les ruches sont là où il y a des fleurs.", "La larve vit dans l'eau.", "Pour la justification : cherche « dépendent »."],
            J("Quelle phrase de la fiche relie les êtres vivants à leur milieu ?", E_PRESENCE, [E_MILIEU, E_DEF, E_COOPERATION], pos=2)),
        "second": qcm(
            "Le conservateur de la réserve te fait passer son examen. Choisis la bonne réponse, puis la phrase de la fiche qui définit l'écosystème.",
            [("Quelles sont les trois parties d'un écosystème ?", ["un milieu de vie, des êtres vivants, leurs relations", "des animaux, des plantes, des pierres", "l'eau, l'air, le sol", "un prédateur, une proie, un arbitre"], 0, "Il ne faut pas oublier les relations."),
             ("Le héron mange des perches. Si toutes les perches disparaissaient, que ferait le héron ?", ["rien ne changerait", "il chercherait d'autres proies ou partirait", "il mangerait des nénuphars", "il pondrait plus d'œufs"], 1, "Les relations relient les êtres vivants."),
             ("Lequel n'est pas une caractéristique physique du milieu ?", ["la température", "la lumière", "le nombre de hérons", "la quantité de pluie"], 2, "Les hérons sont des êtres vivants."),
             ("Lequel est un écosystème ?", ["une mare", "un caillou", "une ruche vide", "un thermomètre"], 0, "Un milieu et des êtres vivants en relation.")],
            ["Trois parties.", "Les hérons sont vivants.", "Pour la justification : cherche « toutes les relations »."],
            J("Quelle phrase de la fiche définit l'écosystème ?", E_DEF, [E_MILIEU, E_EXEMPLES, E_CHANGE], pos=0)),
    }
    return d
