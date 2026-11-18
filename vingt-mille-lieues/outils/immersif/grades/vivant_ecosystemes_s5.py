"""Salle 5 « Le ponton de l'étang » : grades mousse, lieutenant, second (fiche : Le réseau alimentaire)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "vivant-ecosystemes", "tests", "donnees"))
from fiches import *
from schemas import reseau

FICHE = "« Le réseau alimentaire »"

CARNET = tableau("Le carnet d'Élio : les espèces de l'étang, numérotées", ["N°", "Espèce", "Elle mange…"],
                 [["1", "algues", "(fabriquent leur matière avec la lumière)"], ["2", "héron cendré", "des perches et des grenouilles"],
                  ["3", "perche", "des têtards et des larves de libellule"], ["4", "têtard", "des algues"],
                  ["5", "larve de libellule", "des têtards"], ["6", "grenouille verte", "des insectes, dont les libellules adultes"]])


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": ordre(
            "Remets dans l'ordre : qui est mangé en premier, qui mange en dernier ?",
            ["les algues", "le têtard", "la larve de libellule"],
            ["Ouvre la fiche " + FICHE + ".", "On commence par une algue.", "La larve de libellule mange les têtards."]),
        "lieutenant": ordre(
            "Élio montre une autre chaîne de l'étang. Remets-la dans l'ordre, du premier mangé au dernier mangeur, puis choisis la phrase de la fiche qui dit ce qu'on trouve au départ.",
            ["les algues", "le têtard", "la larve de libellule", "la grenouille verte (qui mange la libellule devenue adulte)", "le héron cendré"],
            ["Au départ : une algue.", "La grenouille mange les libellules adultes.", "Pour la justification : cherche « au départ »."],
            J("Quelle phrase de la fiche dit ce qu'on trouve au départ de chaque chaîne ?", R_PLANTE, [R_MANGER, R_RESEAU, R_FLECHE], pos=2)),
        "second": tri(
            "Une année, on a pêché presque toutes les perches de l'étang. Range chaque être vivant selon ce qui lui arrive, puis choisis la phrase de la fiche qui décrit ce cas." + reseau(),
            [("plus", "Devient trop nombreux"), ("moins", "Manque de nourriture"), ("rien", "Pas relié aux perches dans ce réseau")],
            [("la larve de libellule", "plus"), ("le héron cendré", "moins"), ("le ragondin", "rien"), ("le roseau", "rien")],
            ["Qui était mangé par les perches ?", "Qui mangeait les perches ?", "Pour la justification : cherche « pêche trop »."],
            J("Quelle phrase de la fiche décrit ce qui arrive si l'on pêche trop de perches ?", R_SURPECHE, [R_VARIATION, R_INVASIVE, R_RESEAU], pos=1)),
    }
    d["e5-2"] = {
        "mousse": vf(
            "Élio a écrit trois phrases. Pour chacune, choisis vrai ou faux.",
            [("Le têtard mange des algues.", True, "Les algues sont mangées par le têtard."),
             ("Le héron est mangé par la perche.", False, "C'est le héron qui mange la perche."),
             ("La flèche va vers celui qui mange.", True, "Elle veut dire « est mangé par ».")],
            ["Ouvre la fiche " + FICHE + ".", "Le héron est le plus grand.", "La flèche montre celui qui mange."]),
        "lieutenant": vf(
            "Élio vérifie son réseau. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les variations.",
            [("Si le nombre d'individus d'une espèce change beaucoup, tout le réseau est touché.", True, "Les espèces sont liées."),
             ("Les végétaux fabriquent leur matière grâce à la lumière.", True, "Ils sont au départ des chaînes."),
             ("Le ragondin et le roseau ne sont reliés à rien dans l'étang.", False, "Le roseau est mangé par le ragondin."),
             ("Une flèche « perche → héron » veut dire que la perche mange le héron.", False, "La perche est mangée par le héron."),
             ("La perche mange des têtards et des larves de libellule.", True, "Deux flèches arrivent à la perche.")],
            ["Une flèche relie le roseau au ragondin.", "La flèche va vers celui qui mange.", "Pour la justification : cherche « tout le réseau »."],
            J("Quelle phrase de la fiche parle des variations du nombre d'individus ?", R_VARIATION, [R_SURPECHE, R_RESEAU, R_PLANTE], pos=0)),
        "second": qcm(
            "Élio discute des espèces venues d'ailleurs. Choisis la bonne réponse, puis la phrase de la fiche sur l'écrevisse de Louisiane.",
            [("D'où vient l'écrevisse de Louisiane ?", ["d'Amérique", "d'Asie", "d'Australie", "de la mer du Nord"], 0, "Du sud des États-Unis et du nord du Mexique."),
             ("En quelle année a-t-elle été introduite en France ?", ["1789", "1976", "2004", "2026"], 1, "Pour être élevée et mangée."),
             ("Pourquoi touche-t-elle tout le réseau de la mare ?", ["elle détruit les plantes de l'eau et mange les petits animaux", "elle chante la nuit", "elle boit toute l'eau", "elle ne mange rien"], 0, "Plantes et petits animaux sont à la base du réseau."),
             ("Quel geste protège la mare ?", ["relâcher ses écrevisses dans la mare", "ne jamais relâcher un animal exotique", "remplir la mare de sable", "couper toutes les haies"], 1, "Un animal relâché peut devenir envahissant.")],
            ["Louisiane est un État des États-Unis.", "1976.", "Pour la justification : cherche « 1976 »."],
            J("Quelle phrase de la fiche parle de l'écrevisse de Louisiane ?", R_INVASIVE, [R_FRELON, R_PROTEGER, R_VARIATION], pos=3)),
    }
    d["e5-3"] = {
        "mousse": trous(
            "Complète l'affiche avec les bonnes étiquettes.",
            "L'écrevisse de Louisiane vient d'[[Amérique]]. Elle mange les [[plantes]] de la mare. Il ne faut jamais la [[relâcher]] dans la nature.",
            ["Amérique", "plantes", "relâcher"],
            ["Ouvre la fiche " + FICHE + ".", "Elle vient d'un autre continent.", "On ne relâche pas un animal exotique."]),
        "lieutenant": trous(
            "Élio montre le tas de feuilles mortes au bord de l'étang. Complète sa fiche (trois étiquettes sont en trop), puis choisis la phrase de la fiche sur la décomposition.",
            "Les feuilles mortes, les cadavres et les excréments sont [[décomposés]] par des [[champignons]], des [[vers]] et des êtres vivants [[microscopiques]] : leur matière retourne au [[sol]]. Sans eux, les restes s'accumuleraient.",
            ["décomposés", "champignons", "vers", "microscopiques", "sol", "hérons", "nuages", "fossiles"],
            ["Le ver de terre mange les feuilles mortes.", "Certains sont invisibles à l'œil nu.", "Pour la justification : cherche « retourne au sol »."],
            J("Quelle phrase de la fiche décrit la décomposition ?", R_DECOMPOSE, [R_PLANTE, R_MANGER, R_PROTEGER], pos=2)),
        "second": vf(
            "Élio prépare un atelier pour la Fête de la nature. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les gestes qui protègent.",
            [("Creuser une mare peut aider les grenouilles et les libellules.", True, "Elles y pondent."),
             ("Le frelon asiatique est observé en France depuis 2004.", True, "Il chasse surtout les abeilles près des ruches."),
             ("Couper toutes les haies aide les êtres vivants de la réserve.", False, "Les haies les abritent."),
             ("Relâcher un poisson rouge dans l'étang est sans risque.", False, "On ne relâche jamais un animal exotique."),
             ("Éviter les pesticides protège les insectes, et donc ceux qui les mangent.", True, "Tout le réseau en profite.")],
            ["Les haies servent d'abri.", "Un animal exotique peut devenir envahissant.", "Pour la justification : cherche « haies »."],
            J("Quelle phrase de la fiche cite des gestes qui protègent les écosystèmes ?", R_PROTEGER, [R_FRELON, R_INVASIVE, R_VARIATION], pos=1)),
    }
    d["e5-4"] = {
        "lieutenant": code(
            "Il manque trois maillons à la carte d'Élio. Trouve le numéro de chaque espèce manquante dans le carnet, puis choisis la phrase de la fiche qui explique les flèches." +
            reseau(3, "Les trois maillons manquants", ("larve de libellule", "grenouille", "perche")) + CARNET,
            [("Maillon 1", "5", 1, True), ("Maillon 2", "6", 1, True), ("Maillon 3", "3", 1, True)],
            ["Le maillon 1 mange les têtards.", "Le maillon 2 est mangé par le héron et mange des libellules.", "Pour la justification : cherche « de la proie vers »."],
            J("Quelle phrase de la fiche explique le sens des flèches ?", R_FLECHE, [R_RESEAU, R_MANGER, R_PLANTE], pos=0)),
        "second": code(
            "Dernier défi d'Élio : trois maillons manquent, dont celui du départ. Trouve leurs numéros dans le carnet, puis choisis la phrase de la fiche qui explique pourquoi on parle de réseau." +
            reseau(3, "Les trois maillons manquants", ("algues", "larve de libellule", "grenouille")) + CARNET,
            [("Maillon 1", "1", 1, True), ("Maillon 2", "5", 1, True), ("Maillon 3", "6", 1, True)],
            ["Le maillon 1 n'a aucune flèche qui arrive vers lui.", "Le maillon 3 est mangé par le héron.", "Pour la justification : cherche « se croisent »."],
            J("Quelle phrase de la fiche explique ce qu'est un réseau ?", R_RESEAU, [R_FLECHE, R_EXEMPLE, R_VARIATION], pos=2)),
    }
    return d
