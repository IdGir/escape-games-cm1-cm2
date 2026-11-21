"""Message 1 « La salle de classe » (1938) : grades mousse, lieutenant, second (fiche : La montée des dictatures)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "seconde-guerre", "tests", "donnees"))
from fiches import *

FICHE = "« La montée des dictatures (1919-1939) »"


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": ordre(
            "Les cartes de la frise sont mélangées. Remets-les dans l'ordre, de la plus ancienne à la plus récente.",
            [("Mussolini prend le pouvoir", "1922"), ("la crise commence", "1929"), ("Hitler prend le pouvoir", "1933")],
            ["Ouvre la fiche " + FICHE + ".", "Regarde les années : la plus petite d'abord.", "1922, puis 1929, puis 1933."]),
        "lieutenant": ordre(
            "Remets la frise dans l'ordre chronologique, puis choisis la phrase de la fiche qui date l'arrivée de Hitler au pouvoir.",
            [("Mussolini prend le pouvoir en Italie", "1922"), ("la Bourse de New York s'effondre", "octobre 1929"), ("Hitler devient chancelier", "30 janvier 1933"),
             ("Hitler annexe l'Autriche", "1938"), ("l'armée allemande envahit la Pologne", "1er septembre 1939")],
            ["La crise précède l'arrivée de Hitler.", "L'Autriche avant la Pologne.", "Pour la justification : cherche « chancelier »."],
            J("Quelle phrase de la fiche date l'arrivée de Hitler au pouvoir ?", R_HITLER, [R_MUSSO, R_CRISE, R_CONQUETE], pos=1)),
        "second": ordre(
            "Remets dans l'ordre cette chaîne de causes, de la plus ancienne à la plus récente, puis choisis la phrase de la fiche qui explique pourquoi la paix est menacée.",
            [("la crise économique commence aux États-Unis", "octobre 1929"), ("des millions de chômeurs en Europe", "début des années 1930"),
             ("Hitler devient chancelier", "30 janvier 1933"), ("Hitler annexe l'Autriche, puis une partie de la Tchécoslovaquie", "1938"),
             ("la France et le Royaume-Uni déclarent la guerre à l'Allemagne", "3 septembre 1939")],
            ["La crise provoque le chômage.", "Le chômage aide Hitler à prendre le pouvoir.", "Pour la justification : cherche « par la force »."],
            J("Quelle phrase de la fiche explique pourquoi la paix est menacée avant 1939 ?", R_CONQUETE, [R_DEMO, R_CHOMAGE, R_TOTAL], pos=2)),
    }
    d["e1-2"] = {
        "mousse": assoc(
            "Relie chaque chef à son pays.",
            [("Mussolini", "l'Italie"), ("Hitler", "l'Allemagne"), ("Staline", "l'URSS")],
            ["Ouvre la fiche " + FICHE + ".", "Mussolini est italien.", "Hitler dirige l'Allemagne."]),
        "lieutenant": assoc(
            "Relie chaque chef à son parti ou à son régime, puis choisis la phrase de la fiche qui décrit le régime de l'URSS.",
            [("Mussolini", "le parti fasciste"), ("Hitler", "le parti nazi"), ("Staline", "une dictature communiste"), ("la France", "une démocratie")],
            ["Fasciste : Italie.", "Nazi : Allemagne.", "Pour la justification : cherche « Union soviétique »."],
            J("Quelle phrase de la fiche décrit le régime de l'URSS ?", R_STALINE, [R_MUSSO, R_HITLER, R_TOTAL], pos=0)),
        "second": assoc(
            "Relie chaque idée à son régime, puis choisis la phrase de la fiche qui définit l'idée la plus dangereuse du nazisme.",
            [("la haine des Juifs et le racisme", "le nazisme"), ("le parti fasciste de Mussolini, au pouvoir dès 1922", "le fascisme italien"),
             ("des millions d'opposants envoyés dans des camps de travail", "la dictature de Staline"), ("des élections libres et des journaux libres", "la démocratie française")],
            ["L'antisémitisme est au cœur du nazisme.", "Le fascisme est le plus ancien.", "Pour la justification : cherche « antisémitisme »."],
            J("Quelle phrase de la fiche dit sur quoi repose le nazisme ?", R_RACISME, [R_HITLER, R_TOTAL, R_STALINE], pos=3)),
    }
    d["e1-3"] = {
        "mousse": tri(
            "Range chaque carton : démocratie ou dictature ?",
            [("demo", "Démocratie"), ("dicta", "Dictature")],
            [("on vote librement", "demo"), ("un seul chef décide", "dicta"), ("on ne peut pas critiquer le chef", "dicta")],
            ["Ouvre la fiche " + FICHE + ".", "En démocratie, on choisit.", "Dans une dictature, un seul chef décide."]),
        "lieutenant": tri(
            "Range chaque carton : démocratie ou dictature totalitaire ? Puis choisis la phrase de la fiche qui définit un régime totalitaire.",
            [("demo", "Démocratie"), ("dicta", "Dictature totalitaire")],
            [("plusieurs partis aux élections", "demo"), ("les journaux critiquent le gouvernement", "demo"), ("on élit ses députés", "demo"),
             ("un parti unique", "dicta"), ("la propagande à la radio", "dicta"), ("une police politique", "dicta")],
            ["Un seul parti : dictature.", "La propagande sert le chef.", "Pour la justification : cherche « contrôler toute la vie »."],
            J("Quelle phrase de la fiche définit un régime totalitaire ?", R_TOTAL, [R_DEMO, R_MUSSO, R_RACISME], pos=2)),
        "second": tri(
            "En 1938, chaque pays est-il une démocratie ou une dictature ? Range les cartes, puis choisis la phrase de la fiche sur la France et le Royaume-Uni.",
            [("demo", "Démocratie"), ("dicta", "Dictature")],
            [("la France", "demo"), ("le Royaume-Uni", "demo"), ("un pays où l'on peut critiquer le gouvernement", "demo"),
             ("l'Italie", "dicta"), ("l'Allemagne", "dicta"), ("l'Union soviétique", "dicta")],
            ["Trois dictateurs : trois dictatures.", "La France est une République.", "Pour la justification : cherche « restent des démocraties »."],
            J("Quelle phrase de la fiche décrit la France et le Royaume-Uni en 1938 ?", R_DEMO, [R_CONQUETE, R_TOTAL, R_CHOMAGE], pos=0)),
    }
    d["e1-4"] = {
        "lieutenant": qcm(
            "Le maître lit le journal. Réponds, puis choisis la phrase de la fiche qui décrit les effets de la crise.",
            [("Où commence la crise de 1929 ?", ["à Londres", "à New York", "à Rome", "à Moscou"], 1, "La Bourse de New York s'effondre."),
             ("Quel est l'effet de la crise sur les ouvriers ?", ["ils gagnent plus", "beaucoup perdent leur travail", "ils partent en vacances", "rien ne change"], 1, "Des usines ferment."),
             ("Qui devient chancelier en Allemagne le 30 janvier 1933 ?", ["Mussolini", "Staline", "Hitler", "Pétain"], 2, "Le chef du parti nazi."),
             ("Que fait Hitler en 1938 ?", ["il annexe l'Autriche", "il organise des élections libres", "il signe la paix", "il quitte l'Allemagne"], 0, "Puis une partie de la Tchécoslovaquie.")],
            ["Wall Street est à New York.", "Le chômage augmente.", "Pour la justification : cherche « perdent leur travail »."],
            J("Quelle phrase de la fiche décrit les effets de la crise ?", R_CHOMAGE, [R_CRISE, R_DEMO, R_CONQUETE], pos=1)),
        "second": qcm(
            "Le maître demande aux grands élèves de réfléchir. Réponds, puis choisis la phrase de la fiche qui date la prise de pouvoir de Mussolini.",
            [("Pourquoi la crise aide-t-elle les partis extrémistes ?", ["parce que les gens ont peur et cherchent un chef qui promet l'ordre", "parce que tout le monde est riche", "parce que les élections sont interdites partout", "parce que la crise touche seulement l'Italie"], 0, "La peur de l'avenir profite aux extrémistes."),
             ("Quel dictateur est arrivé au pouvoir avant la crise de 1929 ?", ["Hitler", "Mussolini", "aucun", "de Gaulle"], 1, "En 1922."),
             ("Que n'existe-t-il pas dans une dictature ?", ["un chef", "la propagande", "la liberté de critiquer le gouvernement", "une police"], 2, "Les opposants sont arrêtés."),
             ("Pourquoi la paix est-elle menacée en 1938 ?", ["Hitler veut agrandir l'Allemagne par la force", "la France envahit l'Allemagne", "l'Italie devient une démocratie", "les dictatures disparaissent"], 0, "Autriche, puis Tchécoslovaquie.")],
            ["Peur et chômage aident les extrémistes.", "Mussolini : 1922.", "Pour la justification : cherche « fasciste »."],
            J("Quelle phrase de la fiche date la prise de pouvoir de Mussolini ?", R_MUSSO, [R_HITLER, R_STALINE, R_CRISE], pos=2)),
    }
    return d
