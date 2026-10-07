"""Salle 2 « Le mât du vent » (fiche : vent)."""
from aide import *

F = "« Mesurer le vent : direction et vitesse »"
V1 = "La girouette indique la direction d'où vient le vent : un vent de nord-ouest vient du nord-ouest."
V2 = "L'anémomètre mesure sa vitesse, en km/h ou en mètres par seconde (1 m/s = 3,6 km/h, car une heure compte 3 600 secondes)."
V3 = "Elle porte les quatre points cardinaux (N, E, S, O) et les quatre directions intermédiaires (NE, SE, SO, NO)."
V4 = "Chaque direction intermédiaire prend le nom de ses deux voisines, en commençant par nord ou sud."
V5 = "L'Organisation météorologique mondiale demande de mesurer le vent à 10 m au-dessus d'un terrain dégagé, loin des obstacles, et de retenir la vitesse moyenne sur dix minutes."
V6 = "Une pointe brève et plus forte s'appelle une rafale."
V7 = "Elle classe le vent de la force 0 (calme, moins de 1 km/h) à la force 12 (ouragan, 118 km/h et plus), d'après sa vitesse et ses effets : force 2 (6 à 11 km/h), on sent le vent sur le visage ; force 4 (20 à 28 km/h), la poussière se soulève ; force 6 (39 à 49 km/h), les grosses branches s'agitent."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": {
            "type": "plan", "titre": "Rose des vents de la station", "colonnes": 2,
            "cases": [{"libelle": "Là où le soleil se lève le matin", "reponse": "Est"}, {"libelle": "Là où le soleil se couche le soir", "reponse": "Ouest"}, {"libelle": "Là où se trouve le soleil à midi, en France", "reponse": "Sud"}],
            "etiquettes": ["Est", "Ouest", "Sud", "Nord"],
            "consigne": "L'orage a fait tourner la croix des points cardinaux. Replace les points cardinaux : clique sur une étiquette, puis sur la case qui lui correspond. Une étiquette est en trop.",
            "indices": ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Le matin, le soleil se lève à l'est.", "En France, le soleil de midi est au sud."]},
        "lieutenant": qcm(
            carnet("Relevés du mât", "(inventés pour le jeu). Lundi : la girouette pointe vers le nord-ouest ; l'anémomètre indique 20 km/h. Mardi : la girouette pointe vers le sud ; l'anémomètre indique 6 km/h.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("D'où vient le vent de lundi ?", ["Du nord-ouest", "Du sud-est", "Du nord-est", "Du sud-ouest"], 0, "La girouette indique d'où vient le vent."),
             ("Quelle est la force de Beaufort du vent de lundi (20 km/h) ?", ["Force 4", "Force 2", "Force 6", "Force 0"], 0, "20 à 28 km/h : force 4."),
             ("Que ressent-on pour le vent de mardi (6 km/h, force 2) ?", ["On sent le vent sur le visage, les feuilles frémissent", "La fumée monte tout droit", "Les grosses branches s'agitent", "Des dégâts importants"], 0, "Force 2.")],
            ["La girouette indique d'où vient le vent.", "20 à 28 km/h : force 4.", "Force 2 : on sent le vent sur le visage."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", V1, [V2, V4, V6], pos=2)),
        "second": vf(
            "Keïta a noté six phrases sur la rose des vents et le vent. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui donne le nom des directions intermédiaires.",
            [("La rose des vents porte quatre points cardinaux.", True, "N, E, S, O."), ("La rose des vents porte aussi quatre directions intermédiaires.", True, "NE, SE, SO, NO."), ("Un vent de sud-ouest vient du nord-est.", False, "Il vient du sud-ouest."),
             ("La direction intermédiaire entre le nord et l'est s'appelle nord-est.", True, "On commence par nord ou sud."), ("La girouette mesure la vitesse du vent.", False, "L'anémomètre."), ("L'anémomètre est placé à 1,50 m du sol.", False, "À 10 m, en terrain dégagé.")],
            ["La girouette indique la direction, l'anémomètre la vitesse.", "On nomme un vent d'après sa provenance.", "Le nom commence par nord ou sud."],
            J("Quelle phrase de la fiche donne le nom des directions intermédiaires ?", V4, [V3, V1, V5], pos=1)),
    }
    d["e2-2"] = {
        "mousse": vf(
            "Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("La girouette indique d'où vient le vent.", True, "Sa flèche pointe vers la direction d'où arrive le vent."), ("L'anémomètre mesure la vitesse du vent.", True, "Plus ses coupelles tournent vite, plus le vent est fort."), ("La vitesse du vent se mesure en degrés.", False, "En kilomètres par heure.")],
            ["Ouvre la fiche " + F + ".", "La girouette montre la direction.", "L'anémomètre mesure la vitesse."]),
        "lieutenant": tri(
            "Keïta classe des vents selon leur force de Beaufort. Range chaque observation dans la bonne colonne, puis choisis la phrase de la fiche qui donne l'échelle de Beaufort.",
            [("f2", "Force 2 (6 à 11 km/h)"), ("f4", "Force 4 (20 à 28 km/h)"), ("f6", "Force 6 (39 à 49 km/h)")],
            [("On sent le vent sur le visage", "f2"), ("Les feuilles frémissent", "f2"), ("La poussière se soulève", "f4"), ("Les petites branches bougent sans arrêt", "f4"), ("Les grosses branches s'agitent", "f6"), ("Le parapluie se tient mal", "f6")],
            ["Plus le vent est fort, plus les objets bougent.", "Force 2 : sur le visage. Force 4 : la poussière. Force 6 : les grosses branches.", "Relis l'échelle de la fiche."],
            J("Quelle phrase de la fiche donne l'échelle de Beaufort ?", V7, [V5, V2, V3], pos=1)),
        "second": ordre(
            "Keïta range des vents du plus faible au plus fort (le plus faible en haut), puis choisis la phrase de la fiche qui explique la conversion des mètres par seconde en km/h.",
            [("Calme : moins de 1 km/h", "force 0"), ("Une brise de 5 m/s", "environ 18 km/h"), ("Un vent de 10 m/s", "36 km/h"), ("Un vent de 40 km/h", "force 6"), ("Un ouragan", "118 km/h et plus")],
            ["1 m/s = 3,6 km/h.", "5 m/s = 18 km/h ; 10 m/s = 36 km/h.", "Force 6 : 39 à 49 km/h."],
            J("Quelle phrase de la fiche explique la conversion des m/s en km/h ?", V2, [V7, V5, V1], pos=2)),
    }
    d["e2-3"] = {
        "mousse": assoc(
            "Le capitaine Keïta observe la nature. Relie chaque vent à ce que l'on observe. Clique à gauche, puis à droite.",
            [("Calme", "la fumée monte tout droit"), ("Légère brise", "on sent le vent sur le visage"), ("Vent frais", "les grosses branches s'agitent")],
            ["Ouvre la fiche " + F + ".", "Plus le vent est rapide, plus les objets bougent.", "Sans vent, la fumée monte tout droit."]),
        "lieutenant": vf(
            "Keïta affirme cinq choses sur la mesure du vent. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui définit la rafale.",
            [("On mesure le vent à 10 m, en terrain dégagé.", True, "Loin des obstacles."), ("On retient la vitesse moyenne sur dix minutes.", True, "Pour les mesures comparables."), ("Une rafale est une pointe de vent brève et plus forte.", True, "Plus forte que la moyenne."),
             ("1 m/s vaut 10 km/h.", False, "1 m/s = 3,6 km/h."), ("L'échelle de Beaufort va de 0 à 6.", False, "De 0 à 12.")],
            ["10 m, terrain dégagé.", "1 m/s = 3,6 km/h.", "La rafale est brève."],
            J("Quelle phrase de la fiche définit la rafale ?", V6, [V5, V2, V7], pos=1)),
        "second": qcm(
            carnet("Relevé de Keïta", "(inventé pour le jeu). L'anémomètre indique 5 m/s, puis 14 m/s en rafale. Rappel : 1 m/s = 3,6 km/h.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Combien font 5 m/s en km/h ?", ["18 km/h", "5 km/h", "8,6 km/h", "50 km/h"], 0, "5 × 3,6 = 18."),
             ("Combien font 14 m/s en km/h ?", ["50,4 km/h", "14 km/h", "17,6 km/h", "140 km/h"], 0, "14 × 3,6 = 50,4."),
             ("Pourquoi 14 m/s est-ce une rafale et pas la vitesse moyenne ?", ["C'est une pointe brève plus forte que la moyenne", "C'est une vitesse constante", "C'est la vitesse du son", "Elle est mesurée au sol"], 0, "Une rafale est brève.")],
            ["Multiplie par 3,6.", "14 × 3,6 : 14 × 3 = 42, puis 14 × 0,6 = 8,4.", "La vitesse moyenne se calcule sur dix minutes."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", V2, [V5, V6, V1], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": trous(
            "Keïta a rédigé son carnet, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « 10 m ».",
            "La girouette indique la [[direction]] d'où vient le vent ; l'anémomètre mesure sa [[vitesse]]. On installe les instruments à [[10 m]] de haut, en terrain [[dégagé]]. Une pointe brève et plus forte s'appelle une [[rafale]].",
            ["direction", "vitesse", "10 m", "dégagé", "rafale", "1,50 m", "pluviomètre", "température"],
            ["Deux instruments : l'un pour la direction, l'autre pour la vitesse.", "1,50 m est la hauteur du thermomètre.", "Un coup de vent bref s'appelle une rafale."],
            J("Quelle phrase de la fiche justifie le mot « 10 m » ?", V5, [V1, V6, V2], pos=1)),
        "second": trous(
            "Keïta résume l'échelle de Beaufort, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Cinq étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « ouragan ».",
            "L'échelle de Beaufort classe le vent de la force [[0]] (calme) à la force [[12]] (ouragan, 118 km/h et plus). À la force 4, la [[poussière]] se soulève ; à la force 6, les grosses [[branches]] s'agitent.",
            ["0", "12", "poussière", "branches", "ouragan", "9", "pluie", "feuilles", "neige"],
            ["Les deux extrémités de l'échelle : 0 et 12.", "Force 4 : la poussière.", "Force 6 : les grosses branches."],
            J("Quelle phrase de la fiche justifie le mot « ouragan » ?", V7, [V2, V5, V3], pos=2)),
    }
    return d
