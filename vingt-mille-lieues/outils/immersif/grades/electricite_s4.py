"""Salle 4 « La maison témoin » : grades mousse, lieutenant, second (fiche : La sécurité électrique)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "electricite", "tests", "donnees"))
from fiches import *

FICHE = "« La sécurité électrique »"


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": qcm(
            "Marius pose ses questions. Choisis la bonne réponse.",
            [("Avec quoi fait-on des expériences en classe ?", ["avec une prise", "avec une pile", "avec une rallonge", "avec un grille-pain"], 1, "La pile de la classe est sans danger."),
             ("Le courant des prises est…", ["sans danger", "dangereux", "froid", "le même que celui d'une pile"], 1, "Il peut tuer."),
             ("Que met-on dans une prise ?", ["un crayon", "seulement la fiche d'un appareil", "un doigt", "une clé"], 1, "Jamais d'objet.")],
            ["Ouvre la fiche " + FICHE + ".", "Les piles de la classe : sans danger.", "Les prises : danger."]),
        "lieutenant": qcm(
            "Dans la cuisine de la maison témoin, Marius joue une scène : quelqu'un vient d'être électrisé par un grille-pain. Réponds, puis choisis la phrase de la fiche qui dit quoi faire.",
            [("Que fais-tu d'abord ?", ["je tire la personne par le bras", "je coupe le courant au disjoncteur", "je débranche avec les mains mouillées", "je lui donne à boire"], 1, "On ne touche pas la personne tant que le courant passe."),
             ("Pourquoi ne pas la toucher tout de suite ?", ["parce que le courant pourrait me traverser aussi", "parce qu'elle va se relever seule", "parce que c'est interdit par l'école", "parce qu'elle est isolante"], 0, "Le corps humain conduit le courant."),
             ("Qui appeler ensuite ?", ["le 18 ou le 112", "un camarade", "le 36 30", "personne"], 0, "Pompiers ou numéro d'urgence européen.")],
            ["Couper d'abord, secourir ensuite.", "Le corps conduit le courant.", "Pour la justification : cherche « disjoncteur »."],
            J("Quelle phrase de la fiche dit quoi faire ?", D_SECOURS, [D_ELECTRO, D_PRISE, D_FIL], pos=3)),
        "second": ordre(
            "Marius fait répéter la conduite à tenir face à une personne électrisée. Remets les gestes dans l'ordre, puis choisis la phrase de la fiche qui les résume.",
            ["Ne pas toucher la personne.", "Couper le courant au disjoncteur.", "Appeler le 18 ou le 112.", "Dire où l'on est et ce qui s'est passé.", "Rester près de la personne en attendant les secours."],
            ["La première règle protège le sauveteur.", "On coupe avant d'appeler.", "Pour la justification : cherche « électrisée »."],
            J("Quelle phrase de la fiche résume ces gestes ?", D_SECOURS, [D_ELECTRO, D_SECTEUR, D_LIGNES], pos=1)),
    }
    d["e4-2"] = {
        "mousse": tri(
            "Range chaque affiche : danger ou sans danger.",
            [("danger", "Danger"), ("sans", "Sans danger")],
            [("mettre une épingle dans une prise", "danger"), ("toucher un appareil branché avec les mains mouillées", "danger"),
             ("monter un circuit avec une pile", "sans"), ("allumer une lampe de poche", "sans")],
            ["Ouvre la fiche " + FICHE + ".", "Les prises sont dangereuses.", "Les piles de la classe ne le sont pas."]),
        "lieutenant": tri(
            "Marius raccroche les affiches : à la maison, dehors, ou bon réflexe. Range chaque situation, puis choisis la phrase de la fiche sur les dangers du dehors.",
            [("maison", "Danger à la maison"), ("dehors", "Danger dehors"), ("bon", "Bon réflexe")],
            [("glisser un objet dans une prise", "maison"), ("utiliser un sèche-cheveux près de la baignoire", "maison"),
             ("faire voler un cerf-volant près d'une ligne électrique", "dehors"), ("grimper sur un pylône", "dehors"), ("entrer dans un poste électrique", "dehors"),
             ("tirer sur la fiche pour débrancher", "bon"), ("faire remplacer un fil abîmé", "bon")],
            ["Les pylônes et les postes sont dehors.", "La baignoire est dans la maison.", "Pour la justification : cherche « cerf-volant »."],
            J("Quelle phrase de la fiche parle des dangers du dehors ?", D_LIGNES, [D_PRISE, D_EAU, D_SECOURS], pos=0)),
        "second": qcm(
            "Marius explique ce que fait le courant du secteur dans le corps. Réponds, puis choisis la phrase de la fiche qui distingue électrisation et électrocution.",
            [("Comment appelle-t-on le passage du courant dans le corps ?", ["une électrisation", "une isolation", "une dérivation", "une évaporation"], 0, "Électrisation."),
             ("Quand elle est mortelle, on parle…", ["d'électrocution", "de court-circuit", "de disjonction", "de conduction"], 0, "Électrocution."),
             ("Que peut provoquer le courant du secteur dans le corps ?", ["des brûlures et un arrêt du cœur", "seulement des chatouilles", "rien du tout", "une recharge du corps"], 0, "Il peut brûler et arrêter le cœur.")],
            ["Électrisation : le courant traverse le corps.", "Électrocution : elle est mortelle.", "Pour la justification : cherche « électrocution »."],
            J("Quelle phrase de la fiche distingue les deux mots ?", D_ELECTRO, [D_SECTEUR, D_SECOURS, D_PILE], pos=2)),
    }
    d["e4-3"] = {
        "mousse": vf(
            "Marius lit les idées des visiteurs. Vrai ou faux ?",
            [("On peut jouer avec les prises si l'on fait attention.", False, "Jamais."),
             ("Il faut éteindre la lumière en quittant une pièce.", True, "On économise l'électricité."),
             ("La pile de la classe est sans danger.", True, "Elle ne fait pas de mal au corps.")],
            ["Ouvre la fiche " + FICHE + ".", "Les prises : jamais.", "Une lampe éteinte ne consomme pas."]),
        "lieutenant": vf(
            "Marius corrige les idées reçues sur les économies d'électricité. Vrai ou faux ? Puis choisis la phrase de la fiche sur les lampes à LED.",
            [("Une lampe à LED consomme beaucoup moins qu'une lampe à incandescence.", True, "Pour la même lumière."),
             ("Un appareil en veille ne consomme rien.", False, "Il consomme encore un peu."),
             ("Éteindre la lumière en quittant une pièce économise l'électricité.", True, "Une lampe éteinte ne consomme pas."),
             ("Une lampe à LED éclaire moins qu'une ancienne lampe.", False, "Elle éclaire autant.")],
            ["La LED chauffe très peu.", "Le voyant de veille reste allumé.", "Pour la justification : cherche « LED »."],
            J("Quelle phrase de la fiche parle des lampes à LED ?", D_LED, [D_ECO, D_PILE, D_FIL], pos=1)),
        "second": tri(
            "Marius fait la chasse au gaspillage dans la maison témoin. Range chaque geste : il économise ou il gaspille l'électricité. Puis choisis la phrase de la fiche sur les économies.",
            [("eco", "Économise"), ("gaspi", "Gaspille")],
            [("éteindre la lumière en quittant une pièce", "eco"), ("éteindre complètement la télévision au lieu de la laisser en veille", "eco"),
             ("remplacer une vieille lampe par une lampe à LED", "eco"), ("laisser la console en veille toute la nuit", "gaspi"),
             ("laisser la lumière allumée dans une pièce vide", "gaspi"), ("garder un chargeur branché sans téléphone", "gaspi")],
            ["La veille consomme encore.", "Une lampe allumée dans une pièce vide ne sert à rien.", "Pour la justification : cherche « veille »."],
            J("Quelle phrase de la fiche parle des économies ?", D_ECO, [D_LED, D_FIL, D_PRISE], pos=0)),
    }
    d["e4-4"] = {
        "lieutenant": assoc(
            "Marius montre chaque pièce de la maison témoin. Relie chaque situation au bon réflexe, puis choisis la phrase de la fiche qui parle de débrancher.",
            [("une lampe à débrancher", "tirer sur la fiche, pas sur le fil"), ("un fil dont on voit le cuivre", "le faire remplacer"),
             ("la salle de bain", "aucun appareil branché près de la baignoire"), ("un ballon dans un poste électrique", "ne pas entrer et prévenir un adulte"),
             ("une pièce que l'on quitte", "éteindre la lumière")],
            ["Un fil abîmé laisse voir le cuivre.", "Un poste électrique est toujours fermé à clé pour une bonne raison.", "Pour la justification : cherche « fiche »."],
            J("Quelle phrase de la fiche parle de débrancher ?", D_FIL, [D_PRISE, D_EAU, D_ECO], pos=2)),
        "second": vf(
            "Marius compare la pile de la classe et la prise de la maison. Vrai ou faux ? Puis choisis la phrase de la fiche sur le courant du secteur.",
            [("La prise de la maison a une tension de 230 volts.", True, "C'est le courant du secteur."),
             ("La pile plate de la classe a une tension de 4,5 volts.", True, "Elle est sans danger pour le corps."),
             ("On peut refaire à la maison, avec une prise, les montages de la classe.", False, "Jamais : le secteur peut tuer."),
             ("Le courant du secteur peut arrêter le cœur.", True, "C'est pour cela qu'il est dangereux.")],
            ["230 contre 4,5.", "Les montages se font seulement avec des piles.", "Pour la justification : cherche « 230 volts »."],
            J("Quelle phrase de la fiche parle du secteur ?", D_SECTEUR, [D_PILE, D_ELECTRO, D_PRISE], pos=3)),
    }
    return d
