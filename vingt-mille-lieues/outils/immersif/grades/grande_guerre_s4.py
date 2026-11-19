"""Lettre 4 « L'hôpital de l'école » (11 novembre 1918) : grades mousse, lieutenant, second (fiche : 1918, l'armistice et la paix)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grande-guerre", "tests", "donnees"))
from fiches import *

FICHE = "« 1918 : l'armistice et la paix »"


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": ordre(
            "Remets les grandes étapes dans l'ordre : avant, pendant, après la guerre.",
            [("le départ des soldats", "1914"), ("la vie dans les tranchées", "1914 à 1918"), ("l'armistice", "11 novembre 1918")],
            ["Ouvre la fiche " + FICHE + ".", "Les soldats partent en 1914.", "L'armistice arrive à la fin."]),
        "lieutenant": ordre(
            "Odette affiche les étapes de la fin de la guerre. Remets-les dans l'ordre chronologique, puis choisis la phrase de la fiche sur l'entrée en guerre des États-Unis.",
            [("la bataille de Verdun", "1916"), ("les États-Unis entrent en guerre", "avril 1917"), ("l'armistice est signé à Rethondes", "11 novembre 1918, 5 h 15"),
             ("les cloches annoncent la fin des combats", "11 novembre 1918, 11 h"), ("le traité de Versailles", "28 juin 1919")],
            ["Les États-Unis arrivent en 1917.", "Signature à 5 h 15, cloches à 11 h.", "Pour la justification : cherche « avril 1917 »."],
            J("Quelle phrase de la fiche parle de l'entrée en guerre des États-Unis ?", R_USA, [R_RUSSIE, R_ARMI, R_VERSAILLES], pos=0)),
        "second": ordre(
            "Remets dans l'ordre ces événements de 1914 à 1922, puis choisis la phrase de la fiche sur la Russie.",
            [("l'attentat de Sarajevo", "28 juin 1914"), ("la révolution en Russie", "1917"), ("l'armistice", "11 novembre 1918"),
             ("le traité de Versailles", "28 juin 1919"), ("le Soldat inconnu est conduit à l'Arc de Triomphe", "11 novembre 1920"), ("le 11 novembre devient un jour férié", "1922")],
            ["Sarajevo et Versailles : le même jour de l'année, à cinq ans d'écart.", "La révolution russe a lieu avant l'armistice.", "Pour la justification : cherche « révolution »."],
            J("Quelle phrase de la fiche parle de la Russie ?", R_RUSSIE, [R_USA, R_DEF, R_TRAITE], pos=3)),
    }
    d["e4-2"] = {
        "mousse": qcm(
            "Les cloches sonnent. Réponds aux questions d'Odette.",
            [("Qu'est-ce qu'un armistice ?", ["l'arrêt des combats", "une grande bataille", "une fête d'école"], 0, "Les soldats arrêtent de se battre."),
             ("Quel jour ?", ["le 11 novembre 1918", "le 14 juillet 1914", "le 1er janvier 1920"], 0, "C'est écrit au tableau.")],
            ["Ouvre la fiche " + FICHE + ".", "Les combats s'arrêtent.", "La date est au tableau noir."]),
        "lieutenant": qcm(
            "Un blessé demande si la guerre est vraiment finie. Réponds, puis choisis la phrase de la fiche qui définit un armistice.",
            [("Où l'armistice est-il signé ?", ["à Versailles", "dans la clairière de Rethondes, en forêt de Compiègne", "à Verdun", "à Paris"], 1, "Dans l'Oise."),
             ("À quelle heure les combats s'arrêtent-ils ?", ["à 5 h 15", "à 11 h", "à 15 h", "à minuit"], 1, "La signature a lieu à 5 h 15, la fin des combats à 11 h."),
             ("L'armistice, est-ce la paix ?", ["oui", "non, il arrête les combats ; la paix est signée en 1919", "non, la guerre reprend", "oui, c'est le traité de Versailles"], 1, "La paix : Versailles, 28 juin 1919."),
             ("Pour la France, combien de temps a duré la guerre ?", ["un an", "deux ans", "plus de quatre ans", "dix ans"], 2, "Du 3 août 1914 au 11 novembre 1918.")],
            ["Rethondes : forêt de Compiègne.", "Armistice ≠ paix.", "Pour la justification : cherche « ce n'est pas encore »."],
            J("Quelle phrase de la fiche définit un armistice ?", R_DEF, [R_ARMI, R_ONZE, R_VERSAILLES], pos=1)),
        "second": vf(
            "Odette lit les nouvelles aux blessés. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur la démobilisation.",
            [("L'armistice est signé à 5 h 15 et les combats s'arrêtent à 11 heures.", True, "Le 11 novembre 1918."),
             ("Le 11 novembre 1918, tous les soldats rentrent chez eux le soir même.", False, "La démobilisation dure de longs mois."),
             ("Le traité de paix est signé dans la galerie des Glaces du château de Versailles.", True, "Le 28 juin 1919."),
             ("L'armistice est signé à Verdun.", False, "À Rethondes, en forêt de Compiègne."),
             ("Beaucoup de soldats gardent toute leur vie les traces de leurs blessures.", True, "Le bilan est très lourd.")],
            ["Signature à l'aube, fin des combats en fin de matinée.", "Rentrer prend du temps.", "Pour la justification : cherche « démobilisation »."],
            J("Quelle phrase de la fiche parle du retour des soldats ?", R_RETOUR, [R_BLESSES, R_DUREE, R_ONZE], pos=0)),
    }
    d["e4-3"] = {
        "mousse": assoc(
            "Relie chaque nombre à ce qu'il veut dire.",
            [("11 heures", "la fin des combats"), ("plus de 4 ans", "la durée de la guerre"), ("1918", "l'année de l'armistice")],
            ["Ouvre la fiche " + FICHE + ".", "Les cloches sonnent à 11 heures.", "De 1914 à 1918."]),
        "lieutenant": assoc(
            "Odette recopie les chiffres officiels. Relie chaque nombre à ce qu'il compte, puis choisis la phrase de la fiche qui donne le nombre de soldats français morts.",
            [("8,7 millions", "Français mobilisés pendant la guerre"), ("près de 1,4 million", "soldats français morts"), ("près de 600 000", "veuves de guerre en France"),
             ("5 h 15", "signature de l'armistice"), ("28 juin 1919", "signature du traité de Versailles")],
            ["Le plus grand nombre : tous les mobilisés.", "600 000 : des femmes dont le mari est mort.", "Pour la justification : cherche « 1,4 million »."],
            J("Quelle phrase de la fiche donne le nombre de soldats français morts ?", R_MORTS, [R_VEUVES, R_DUREE, R_BLESSES], pos=2)),
        "second": qcm(
            "Odette fait des calculs pour son registre. Réponds, puis choisis la phrase de la fiche qui donne la durée de la guerre.",
            [("Combien d'années séparent l'attentat de Sarajevo (28 juin 1914) et le traité de Versailles (28 juin 1919) ?", ["3 ans", "4 ans", "5 ans, jour pour jour", "10 ans"], 2, "Le même jour, cinq ans plus tard."),
             ("Pour la France, combien de temps séparent l'entrée en guerre (3 août 1914) et l'armistice (11 novembre 1918) ?", ["un peu plus de 2 ans", "un peu plus de 4 ans et 3 mois", "exactement 5 ans", "6 mois"], 1, "Plus de quatre ans."),
             ("Sur 8,7 millions de mobilisés, près de 1,4 million sont morts. C'est environ…", ["1 sur 2", "1 sur 6", "1 sur 50", "1 sur 100"], 1, "8,7 ÷ 1,4 ≈ 6."),
             ("Combien de temps entre la signature de l'armistice (5 h 15) et l'arrêt des combats (11 h) ?", ["moins d'une heure", "5 h 45", "11 h", "24 h"], 1, "De 5 h 15 à 11 h 00.")],
            ["De 1914 à 1919 : compte les années.", "8,7 est environ six fois 1,4.", "Pour la justification : cherche « du 3 août 1914 »."],
            J("Quelle phrase de la fiche donne la durée de la guerre pour la France ?", R_DUREE, [R_ARMI, R_ONZE, R_MORTS], pos=1)),
    }
    d["e4-4"] = {
        "lieutenant": trous(
            "Odette colle dans son cahier un article sur le traité. Complète-le (des étiquettes sont en trop), puis choisis la phrase de la fiche sur le contenu du traité.",
            "La paix est signée le 28 juin 1919 à [[Versailles]]. L'[[Allemagne]] est déclarée responsable de la guerre. Elle rend l'Alsace et la [[Moselle]] à la France, doit payer des [[réparations]] et réduire son [[armée]].",
            ["Versailles", "Allemagne", "Moselle", "réparations", "armée", "Verdun", "Serbie"],
            ["Le traité porte le nom d'un château.", "Les réparations sont de l'argent.", "Pour la justification : cherche « responsable »."],
            J("Quelle phrase de la fiche décrit le contenu du traité ?", R_TRAITE, [R_VERSAILLES, R_DEF, R_ARMI], pos=3)),
        "second": trous(
            "Complète ce texte sur la paix de 1919 (des étiquettes sont en trop), puis choisis la phrase de la fiche qui situe la signature de la paix.",
            "Un [[armistice]] arrête les combats, mais ce n'est pas encore la paix. La paix est signée le [[28 juin 1919]], dans la galerie des [[Glaces]]. L'Allemagne, déclarée [[responsable]] de la guerre, doit payer des [[réparations]]. Beaucoup d'Allemands vivent ce traité avec [[colère]] : la paix reste fragile.",
            ["armistice", "28 juin 1919", "Glaces", "responsable", "réparations", "colère", "11 novembre 1918", "joie", "Batailles"],
            ["Armistice d'abord, paix ensuite.", "Cinq ans après Sarajevo, jour pour jour.", "Pour la justification : cherche « galerie »."],
            J("Quelle phrase de la fiche situe la signature de la paix ?", R_VERSAILLES, [R_TRAITE, R_ARMI, R_DEF], pos=2)),
    }
    return d
