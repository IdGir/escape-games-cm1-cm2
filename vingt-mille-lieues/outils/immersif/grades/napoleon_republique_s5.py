"""Salle 5 « La mairie » (aujourd'hui) : grades mousse, lieutenant, second (fiche : Lieux, symboles et rites de la République)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "napoleon-republique", "tests", "donnees"))
from fiches import *
from schemas import place

FICHE = "« Lieux, symboles et rites de la République »"
CASES5 = ["la mairie", "l'école", "le monument aux morts", "la devise au fronton de la mairie", "le drapeau tricolore"]


def _cases(n):
    return [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(CASES5[:n])]


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": tri(
            "Range chaque objet : symbole de l'Empire ou symbole de la République ?",
            [("empire", "L'Empire"), ("rep", "La République")],
            [("l'aigle", "empire"), ("Marianne", "rep"), ("la devise « Liberté, Égalité, Fraternité »", "rep")],
            ["Ouvre la fiche " + FICHE + ".", "L'empereur a choisi l'aigle.", "Marianne représente la République."]),
        "lieutenant": tri(
            "Range chaque carte, puis choisis la phrase de la fiche qui décrit Marianne.",
            [("empire", "L'Empire"), ("rep", "La République")],
            [("l'aigle", "empire"), ("les abeilles d'or", "empire"), ("la couronne de lauriers", "empire"),
             ("Marianne au bonnet phrygien", "rep"), ("la Marseillaise, hymne national", "rep"), ("le 14 juillet, fête nationale", "rep")],
            ["Les abeilles sont sur le manteau du sacre.", "La fête nationale est républicaine.", "Pour la justification : cherche « bonnet phrygien »."],
            J("Quelle phrase de la fiche décrit Marianne ?", R_MARIANNE, [R_DEVISE, R_DRAPEAU, R_14], pos=1)),
        "second": tri(
            "Range chaque élément : il appartient à l'Empire seulement, ou à la République d'aujourd'hui ? Puis choisis la phrase de la fiche qui explique ce que rappelle le 14 juillet.",
            [("empire", "L'Empire seulement"), ("rep", "La République d'aujourd'hui")],
            [("le sacre par le pape", "empire"), ("un pouvoir héréditaire", "empire"), ("la noblesse d'Empire", "empire"),
             ("l'élection des représentants", "rep"), ("la fête nationale du 14 juillet", "rep"), ("la devise inscrite au fronton des mairies", "rep")],
            ["Un pouvoir héréditaire passe au fils.", "En République, on élit.", "Pour la justification : cherche « Fédération »."],
            J("Quelle phrase de la fiche explique ce que rappelle le 14 juillet ?", R_14, [R_MARSEIL, R_VOTE, R_ART2], pos=3)),
    }
    d["e5-2"] = {
        "mousse": assoc(
            "Relie chaque symbole à sa description.",
            [("le drapeau", "bleu, blanc, rouge"), ("la devise", "Liberté, Égalité, Fraternité"), ("la Marseillaise", "l'hymne national")],
            ["Ouvre la fiche " + FICHE + ".", "Le drapeau a trois couleurs.", "L'hymne se chante."]),
        "lieutenant": assoc(
            "Relie chaque symbole ou rite à son explication, puis choisis la phrase de la fiche qui raconte la naissance de la Marseillaise.",
            [("la Marseillaise", "écrite par Rouget de Lisle en 1792"), ("le 14 juillet", "la fête nationale"),
             ("l'écharpe tricolore", "portée par le maire pour un mariage"), ("le vote", "choisir ses représentants")],
            ["Rouget de Lisle est à Strasbourg en 1792.", "Le maire célèbre les mariages.", "Pour la justification : cherche « Rouget de Lisle »."],
            J("Quelle phrase de la fiche raconte la naissance de la Marseillaise ?", R_MARSEIL, [R_14, R_ART2, R_DRAPEAU], pos=0)),
        "second": assoc(
            "Relie chaque lieu de la République au rite qui s'y déroule, puis choisis la phrase de la fiche qui décrit le rôle du maire.",
            [("la mairie", "le mariage civil et le vote"), ("le monument aux morts", "les cérémonies du 8 Mai et du 11 Novembre"),
             ("l'Assemblée nationale", "le vote des lois par les députés"), ("l'école", "apprendre à devenir citoyen")],
            ["On vote souvent à la mairie.", "Les députés siègent à l'Assemblée nationale.", "Pour la justification : cherche « écharpe »."],
            J("Quelle phrase de la fiche décrit le rôle du maire ?", R_MAIRE, [R_LIEUX, R_VOTE, R_CEREMONIES], pos=2)),
    }
    d["e5-3"] = {
        "mousse": {"type": "plan", "titre": "La place de la commune", "colonnes": 3, "cases": _cases(3), "etiquettes": CASES5[:3],
                   "consigne": "Place chaque nom sur son repère." + place(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La mairie est au centre.", "Le monument aux morts est une stèle de pierre."]},
        "lieutenant": {"type": "plan", "titre": "La place de la commune", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["l'aigle impérial", "la couronne de lauriers"],
                       "consigne": "Place chaque nom sur son repère (deux sont en trop), puis choisis la phrase de la fiche qui dit où l'on lit la devise." + place(5),
                       "indices": ["La devise est écrite en haut de la façade.", "Le drapeau flotte sur le toit.", "Pour la justification : cherche « fronton »."],
                       "justification": J("Quelle phrase de la fiche dit où l'on lit la devise ?", R_DEVISE, [R_DRAPEAU, R_ART2, R_MARIANNE], pos=1)},
        "second": {"type": "plan", "titre": "La place de la commune", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["l'aigle impérial", "la couronne de lauriers", "le Panthéon"],
                   "consigne": "Place chaque nom sur son repère (trois sont en trop : le Panthéon est un lieu de la République, mais il est à Paris), puis choisis la phrase de la fiche qui explique le rôle du monument aux morts." + place(5),
                   "indices": ["Le Panthéon n'est pas sur la place d'une commune de Bourgogne.", "Le monument aux morts est une stèle.", "Pour la justification : cherche « 11 Novembre »."],
                   "justification": J("Quelle phrase de la fiche explique le rôle du monument aux morts ?", R_CEREMONIES, [R_LIEUX, R_MAIRE, R_VOTE], pos=0)},
    }
    d["e5-4"] = {
        "lieutenant": code(
            "Ouvre le coffre du testament : le numéro de l'article de la Constitution qui fixe nos symboles, l'année de cette Constitution, puis le jour de juillet de la fête nationale. Choisis ensuite la phrase de la fiche qui cite cet article.",
            [("Article", "2", 1, True), ("Année", "1958", 4, True), ("Jour de la fête nationale", "14", 2, True)],
            ["Cherche « article » dans la fiche.", "La Constitution actuelle date de 1958.", "Pour la justification : cherche « article 2 »."],
            J("Quelle phrase de la fiche cite l'article de la Constitution qui fixe les symboles ?", R_ART2, [R_LOIS, R_DEVISE, R_14], pos=2)),
        "second": code(
            "Le coffre demande trois nombres : le numéro de l'article de la Constitution qui fixe nos symboles, le nombre d'années entre la Déclaration des droits de l'homme (1789) et la Constitution de 1958, puis l'année où la Marseillaise devient chant national. Choisis ensuite la phrase de la fiche sur les textes qui protègent nos droits.",
            [("Article", "2", 1, True), ("Années de 1789 à 1958", "169", 3, True), ("Chant national en", "1795", 4, True)],
            ["Article 2.", "1958 - 1789.", "Pour la justification : cherche « Déclaration »."],
            J("Quelle phrase de la fiche cite les textes qui protègent nos droits et nos libertés ?", R_LOIS, [R_ART2, R_LIEUX, R_VOTE], pos=3)),
    }
    return d
