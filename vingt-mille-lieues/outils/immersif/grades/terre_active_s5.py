"""Salle 5 « Le centre de secours » : grades mousse, lieutenant, second (fiche : Prévenir et se protéger)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "terre-active", "tests", "donnees"))
from fiches import *
from schemas import carte_risques

FICHE = "« Prévenir et se protéger »"


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": tri(
            "Range chaque geste : bon réflexe pendant un séisme, ou geste à ne pas faire ?",
            [("bon", "Bon réflexe"), ("non", "À ne pas faire")],
            [("me mettre sous une table solide", "bon"), ("protéger ma tête avec mes bras", "bon"), ("courir dehors pendant les secousses", "non"), ("prendre l'ascenseur", "non")],
            ["Ouvre la fiche " + FICHE + ".", "La table me protège.", "Pendant les secousses, je ne cours pas."]),
        "lieutenant": tri(
            "Range chaque consigne officielle : avant, pendant ou après les secousses ? Puis choisis la phrase de la fiche qui dit quoi faire pendant les secousses.",
            [("avant", "Avant"), ("pendant", "Pendant"), ("apres", "Après")],
            [("fixer les meubles lourds", "avant"), ("repérer où s'abriter, loin des fenêtres", "avant"), ("rester où l'on est", "pendant"),
             ("s'abriter près d'un mur porteur", "pendant"), ("sortir par les escaliers", "apres"), ("écouter les consignes des autorités", "apres")],
            ["Fixer, repérer : à l'avance.", "S'abriter : pendant.", "Pour la justification : cherche « mur porteur »."],
            J("Quelle phrase de la fiche dit quoi faire pendant les secousses ?", R_PENDANT, [R_AVANT, R_APRES, R_ECOLE], pos=1)),
        "second": tri(
            "Adèle classe les mesures du plan de la commune : prévention (avant) ou protection (pendant et après) ? Puis choisis la phrase de la fiche qui définit la protection.",
            [("prev", "Prévention"), ("prot", "Protection")],
            [("surveiller le volcan avec des capteurs", "prev"), ("dessiner la carte des risques", "prev"), ("construire des bâtiments solides", "prev"), ("faire un exercice à l'école", "prev"),
             ("évacuer les habitants sur ordre des autorités", "prot"), ("s'abriter pendant les secousses", "prot"), ("porter secours aux personnes", "prot")],
            ["La prévention se fait avant.", "La protection met à l'abri au moment du danger.", "Pour la justification : cherche « à l'abri »."],
            J("Quelle phrase de la fiche définit la protection ?", R_PROTECTION, [R_PREVENTION, R_RISQUE, R_OBSERVATOIRE], pos=3)),
    }
    d["e5-2"] = {
        "mousse": qcm(
            "Adèle pose deux questions. Choisis la bonne réponse.",
            [("Qui surveille le volcan ?", ["les scientifiques de l'observatoire", "personne", "les oiseaux", "la météo"], 0, "Jour et nuit."),
             ("Pendant un exercice « séisme », que fais-tu d'abord ?", ["je cours dehors", "je m'abrite sous ma table", "je prends l'ascenseur", "je téléphone"], 1, "Je me protège.")],
            ["Ouvre la fiche " + FICHE + ".", "Un observatoire surveille.", "D'abord, se protéger."]),
        "lieutenant": vf(
            "Adèle relit le dossier « risques » de la mairie. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui définit la prévention.",
            [("La prévention, c'est ce que l'on fait avant pour limiter les dégâts.", True, "Surveiller, informer, construire, s'entraîner."),
             ("S'entraîner lors d'un exercice est une mesure de prévention.", True, "On apprend les bons gestes."),
             ("Construire solidement ne sert à rien contre les séismes.", False, "Les bâtiments solides résistent mieux."),
             ("Un risque naturel existe même là où personne ne vit ni ne passe.", False, "Il faut des personnes ou des biens exposés."),
             ("Informer les habitants fait partie de la prévention.", True, "Avec la carte des risques, par exemple.")],
            ["Prévenir, c'est agir avant.", "Risque = phénomène + personnes ou biens.", "Pour la justification : cherche « limiter les dégâts »."],
            J("Quelle phrase de la fiche définit la prévention ?", R_PREVENTION, [R_PROTECTION, R_RISQUE, R_CARTE], pos=0)),
        "second": qcm(
            "La mairie de Bois-Clair hésite pour ses projets. Aide-la avec la carte des risques, puis choisis la phrase de la fiche sur la carte des risques." + carte_risques(),
            [("Où vaut-il mieux construire la nouvelle salle des fêtes ?", ["en zone A", "en zone B", "en zone C", "au bord du cratère"], 2, "La zone C a le danger le plus faible."),
             ("L'école est en zone C. Faut-il quand même y faire des exercices ?", ["non, jamais", "oui, car un séisme peut toucher toute la commune", "seulement les adultes", "seulement s'il pleut"], 1, "On s'entraîne partout."),
             ("Pourquoi le point de rassemblement est-il loin du volcan ?", ["pour être loin de la zone de danger fort", "pour la vue", "par hasard", "pour être près de la mer"], 0, "On s'éloigne de la zone A."),
             ("À quoi sert surtout cette carte ?", ["à décider où construire et comment protéger", "à prévoir le jour d'une éruption", "à empêcher le volcan d'entrer en éruption", "à mesurer la magnitude"], 0, "C'est un outil de prévention.")],
            ["Le danger diminue de A vers C.", "Une carte ne prévoit pas le jour.", "Pour la justification : cherche « où construire »."],
            J("Quelle phrase de la fiche parle de la carte des risques ?", R_CARTE, [R_RISQUE, R_OBSERVATOIRE, R_PREVENTION], pos=2)),
    }
    d["e5-3"] = {
        "mousse": ordre(
            "Remets l'exercice dans l'ordre.",
            ["Je m'abrite sous ma table.", "J'attends la fin des secousses.", "Je sors calmement avec la classe."],
            ["Ouvre la fiche " + FICHE + ".", "D'abord, se protéger.", "On sort à la fin."]),
        "lieutenant": ordre(
            "Remets les étapes de l'exercice dans l'ordre, puis choisis la phrase de la fiche qui dit quoi faire après les secousses.",
            [("Le signal retentit : je reste où je suis.", "début"), ("Je m'abrite sous ma table et je protège ma tête.", "pendant"),
             ("J'attends la fin des secousses.", "pendant"), ("Je sors calmement par l'escalier, sans ascenseur.", "après"), ("Je rejoins le point de rassemblement et j'écoute l'adulte.", "fin")],
            ["On ne bouge pas tout de suite.", "L'escalier, jamais l'ascenseur.", "Pour la justification : cherche « par les escaliers »."],
            J("Quelle phrase de la fiche dit quoi faire après les secousses ?", R_APRES, [R_PENDANT, R_ECOLE, R_AVANT], pos=2)),
        "second": ordre(
            "Adèle explique la chaîne d'alerte en cas d'éruption. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche sur l'éruption.",
            [("Les capteurs de l'observatoire enregistrent de petits séismes.", "surveiller"), ("Les scientifiques informent les autorités.", "informer"),
             ("Les autorités décident d'évacuer les zones proches du volcan.", "décider"), ("Les habitants suivent les ordres d'évacuation.", "se protéger"),
             ("Si des cendres tombent, chacun reste à l'intérieur, fenêtres fermées.", "se protéger")],
            ["Tout commence par la surveillance.", "Les autorités décident, les habitants suivent.", "Pour la justification : cherche « ordres d'évacuation »."],
            J("Quelle phrase de la fiche dit quoi faire pendant une éruption ?", R_VOLCAN, [R_PROTECTION, R_APRES, R_OBSERVATOIRE], pos=1)),
    }
    d["e5-4"] = {
        "lieutenant": assoc(
            "Relie chaque mesure à son but, puis choisis la phrase de la fiche sur les observatoires.",
            [("les sismographes de l'observatoire", "surveiller jour et nuit"), ("la carte des risques", "décider où construire"),
             ("les bâtiments solides", "résister aux secousses"), ("l'exercice à l'école", "s'entraîner aux bons gestes"), ("l'évacuation", "mettre les habitants à l'abri")],
            ["Surveiller : avec des capteurs.", "S'entraîner : à l'école.", "Pour la justification : cherche « jour et nuit »."],
            J("Quelle phrase de la fiche parle des observatoires ?", R_OBSERVATOIRE, [R_CARTE, R_PREVENTION, R_RISQUE], pos=0)),
        "second": code(
            "Le message d'information est verrouillé par trois nombres. Retrouve-les dans les fiches, puis choisis la phrase de la fiche qui définit le risque naturel.",
            [("Année de l'éruption de la montagne Pelée", "1902", 4, True), ("Année de l'évacuation lors de l'éruption de la Soufrière", "1976", 4, True), ("Volcans de la Chaîne des Puys", "80", 2, True)],
            ["Fiche « Les volcans » : la Martinique.", "Fiche « Les volcans » : la Guadeloupe.", "Pour la justification : cherche « peut toucher »."],
            J("Quelle phrase de la fiche définit le risque naturel ?", R_RISQUE, [R_PREVENTION, R_PROTECTION, R_CARTE], pos=3)),
    }
    return d
