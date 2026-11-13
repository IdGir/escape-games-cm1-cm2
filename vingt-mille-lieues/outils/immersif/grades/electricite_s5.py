"""Salle 5 « Le poste de conduite du réseau » : grades mousse, lieutenant, second (fiche : Produire et transporter l'électricité).
Chiffres : RTE, Bilan électrique 2025 (production 547,5 TWh ; nucléaire 373 ; hydraulique 62,4 ; éolien 49,6 ; solaire 32,9 ; fossile ≈ 18,7)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "electricite", "tests", "donnees"))
from fiches import *

FICHE = "« Produire et transporter l'électricité »"
DOC = tableau("Production d'électricité en France en 2025 (en milliards de kilowattheures) — total : 547,5", ["Centrales", "Production"],
              [["nucléaires", "373"], ["hydrauliques", "62,4"], ["éoliennes", "49,6"], ["solaires", "32,9"], ["au gaz, au charbon, au fioul", "environ 18,7"]])
DOC_SIMPLE = tableau("Production d'électricité en France en 2025 (en milliards de kilowattheures, arrondis)", ["Centrales", "Production"],
                     [["nucléaires", "373"], ["hydrauliques", "62"], ["éoliennes", "50"], ["solaires", "33"]])


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": ordre(
            "Remets dans l'ordre le voyage de l'électricité, de la centrale à la maison.",
            ["la centrale", "les grandes lignes sur les pylônes", "le poste près de la ville", "la lampe de la maison"],
            ["Ouvre la fiche " + FICHE + ".", "Tout commence à la centrale.", "La maison est en dernier."]),
        "lieutenant": ordre(
            "Karim rallume le trajet complet sur la carte lumineuse. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit le début du voyage.",
            ["la centrale produit le courant", "un transformateur élève la tension", "les lignes à très haute tension le transportent",
             "un poste abaisse la tension près de la ville", "le réseau de distribution l'amène au compteur", "la prise de la maison"],
            ["Le transformateur est à la sortie de la centrale.", "Le poste est près de la ville.", "Pour la justification : cherche « élève la tension »."],
            J("Quelle phrase de la fiche décrit le début du voyage ?", P_TRANSPORT, [P_POSTE, P_RTE, P_CENTRALE], pos=0)),
        "second": qcm(
            "Karim présente le réseau du pays. Réponds aux questions, puis choisis la phrase de la fiche qui donne la longueur du réseau de transport.",
            [("Environ combien de kilomètres de lignes compte le réseau de transport français ?", ["1 060 km", "10 600 km", "106 000 km", "1 060 000 km"], 2, "Environ 106 000 km."),
             ("Où la tension est-elle abaissée ?", ["dans la centrale", "dans les postes près des villes", "dans les pylônes", "dans la lampe"], 1, "Dans les postes de transformation."),
             ("Jusqu'où le réseau de distribution amène-t-il l'électricité ?", ["jusqu'au compteur de chaque maison", "jusqu'à la centrale", "jusqu'aux pylônes seulement", "jusqu'au barrage"], 0, "Puis jusqu'aux prises.")],
            ["Le réseau fait plus de deux fois le tour de la Terre.", "Les postes sont près des villes.", "Pour la justification : cherche « 106 000 km »."],
            J("Quelle phrase de la fiche donne la longueur du réseau ?", P_RTE, [P_TRANSPORT, P_POSTE, P_EQUILIBRE], pos=1)),
    }
    d["e5-2"] = {
        "mousse": tri(
            "Range chaque centrale : elle utilise une source qui revient toujours, ou une source qui s'épuise.",
            [("renouv", "Revient toujours"), ("epuise", "S'épuise")],
            [("l'éolienne (le vent)", "renouv"), ("le barrage (l'eau)", "renouv"), ("les panneaux solaires (le Soleil)", "renouv"), ("la centrale au gaz", "epuise")],
            ["Ouvre la fiche " + FICHE + ".", "Le vent souffle encore demain.", "Le gaz brûlé ne revient pas."]),
        "lieutenant": assoc(
            "Karim montre les centrales de la vallée. Relie chaque centrale à ce qui fait tourner sa turbine, puis choisis la phrase de la fiche qui explique le rôle de la turbine.",
            [("la centrale nucléaire", "la vapeur chauffée par l'uranium"), ("la centrale hydraulique", "l'eau qui descend du barrage"),
             ("l'éolienne", "le vent sur les pales"), ("la centrale thermique", "la vapeur produite en brûlant du gaz ou du charbon"),
             ("le panneau solaire", "rien : il transforme directement la lumière")],
            ["Nucléaire et thermique font toutes deux de la vapeur.", "Le panneau solaire ne fait rien tourner.", "Pour la justification : cherche « alternateur »."],
            J("Quelle phrase de la fiche explique le rôle de la turbine ?", P_ALTERN, [P_CENTRALE, P_NUCL, P_SOL], pos=2)),
        "second": tri(
            "Karim classe les moyens de production. Range chacun : il fait tourner une turbine, ou il ne fait rien tourner. Puis choisis la phrase de la fiche qui explique l'exception.",
            [("turbine", "Fait tourner une turbine"), ("rien", "Ne fait rien tourner")],
            [("la centrale nucléaire", "turbine"), ("le barrage", "turbine"), ("l'éolienne", "turbine"), ("la centrale au gaz", "turbine"),
             ("le panneau photovoltaïque", "rien"), ("la pile plate de la classe", "rien")],
            ["Le panneau transforme directement la lumière.", "La pile non plus ne tourne pas.", "Pour la justification : cherche « sans rien faire tourner »."],
            J("Quelle phrase de la fiche explique l'exception ?", P_SOL, [P_ALTERN, P_EOL, P_HYDRO], pos=3)),
    }
    d["e5-3"] = {
        "mousse": code(
            "Le pupitre demande deux codes, lus dans le tableau de Karim." + DOC_SIMPLE,
            [("Production des centrales nucléaires", "373", 3, True), ("Production des centrales hydrauliques", "62", 2, True)],
            ["Ouvre la fiche " + FICHE + ".", "Lis la ligne « nucléaires ».", "Lis la ligne « hydrauliques »."]),
        "lieutenant": code(
            "Pour rebrancher les quatre quartiers, le pupitre demande quatre codes lus ou calculés dans le tableau de Karim (arrondis à l'unité). Choisis ensuite la phrase de la fiche qui résume ces chiffres." + DOC,
            [("Quartier de la gare : part du nucléaire, en %", "68", 2, True), ("Quartier du port : production hydraulique arrondie", "62", 2, True),
             ("Quartier des écoles : production éolienne arrondie", "50", 2, True), ("Quartier du marché : production solaire arrondie", "33", 2, True)],
            ["49,6 s'arrondit à 50 ; 32,9 à 33.", "373 divisé par 547,5 fait un peu plus de 0,68.", "Pour la justification : cherche « 547,5 »."],
            J("Quelle phrase de la fiche résume ces chiffres ?", P_2025, [P_RENOUV, P_CENTRALE, P_EQUILIBRE], pos=1)),
        "second": code(
            "Le dernier contrôle du pupitre demande des calculs sur le tableau de Karim. Arrondis à l'unité. Choisis ensuite la phrase de la fiche qui classe les sources." + DOC,
            [("Production totale des centrales à l'eau, au vent et au Soleil", "145", 3, True), ("Part du nucléaire, en %", "68", 2, True),
             ("Part du gaz, du charbon et du fioul, en %", "3", 1, True), ("Part du nucléaire, de l'eau, du vent et du Soleil réunis, en %", "95", 2, True)],
            ["62,4 + 49,6 + 32,9 = 144,9.", "Une part en % : production divisée par 547,5, multipliée par 100.", "Pour la justification : cherche « renouvelables »."],
            J("Quelle phrase de la fiche classe les sources ?", P_RENOUV, [P_2025, P_THERM, P_SOL], pos=0)),
    }
    d["e5-4"] = {
        "lieutenant": vf(
            "Karim explique pourquoi il rallume les quartiers un par un. Vrai ou faux ? Puis choisis la phrase de la fiche qui explique sa prudence.",
            [("On peut facilement stocker toute l'électricité d'une centrale dans de grosses piles.", False, "L'électricité se stocke très mal."),
             ("À chaque instant, il faut produire autant que l'on consomme.", True, "Sinon le réseau disjoncte."),
             ("Rallumer tous les quartiers d'un coup ferait grimper brutalement la consommation.", True, "D'où la reconnexion un par un."),
             ("Les éoliennes produisent la même quantité d'électricité à chaque instant.", False, "Cela dépend du vent.")],
            ["La production doit suivre la consommation.", "Le vent ne souffle pas toujours de la même façon.", "Pour la justification : cherche « se stocke »."],
            J("Quelle phrase de la fiche explique la prudence de Karim ?", P_EQUILIBRE, [P_POSTE, P_RTE, P_2025], pos=2)),
        "second": ordre(
            "Karim décrit le fonctionnement d'une centrale nucléaire. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui le résume.",
            ["L'uranium produit de la chaleur.", "La chaleur transforme de l'eau en vapeur.", "La vapeur fait tourner la turbine.", "La turbine entraîne l'alternateur.", "L'alternateur produit le courant."],
            ["Tout commence par la chaleur.", "L'alternateur est en dernier.", "Pour la justification : cherche « uranium »."],
            J("Quelle phrase de la fiche le résume ?", P_NUCL, [P_THERM, P_ALTERN, P_HYDRO], pos=3)),
    }
    return d
