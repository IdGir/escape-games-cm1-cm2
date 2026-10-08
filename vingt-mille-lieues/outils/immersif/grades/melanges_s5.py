"""Salle 5 « La saline » (fiche : separer-liquide)."""
from aide import *

F = "« Séparer un solide d'un liquide »"
L1 = "Décantation : au repos, le solide non dissous se dépose au fond ; on verse doucement le liquide (on le transvase)."
L2 = "Filtration : le papier filtre retient les grains solides non dissous ; le liquide s'écoule dans le bécher."
L3 = "Évaporation : l'eau passe à l'état de vapeur ; le solide dissous reste."
L4 = "Un solide dissous traverse le filtre : on ne peut pas retirer le sel de l'eau salée en la filtrant. Seule l'évaporation le permet."
L5 = "L'eau de mer contient en moyenne 35 g de sel par litre."
L6 = "Dans les bassins du marais, le soleil et le vent font évaporer l'eau : le paludier récolte le gros sel, et la fleur de sel qui se forme à la surface."
L7 = "Pour séparer plusieurs constituants, on enchaîne les méthodes dans un ordre logique. Exemple, pour de l'eau salée avec de la limaille de fer : peser, observer, aimanter, évaporer, comparer."
L8 = "La masse de fer et de sel retrouvée est égale à celle du départ."
L9 = "Une eau filtrée peut contenir des substances dissoutes : elle ne se boit pas pour autant."


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": trous(
            "Yann sépare du sable de l'eau. Clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
            "Pour séparer le sable de l'eau, on peut verser le mélange dans un [[filtre]] : l'eau passe, le sable [[reste]] dans le filtre. Pour récupérer le sel dissous, on laisse l'eau s'[[évaporer]].",
            ["filtre", "reste", "évaporer", "aimant"],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Le filtre retient le sable.", "Pour récupérer le sel, l'eau doit partir."]),
        "lieutenant": qcm(
            carnet("Carnet de Yann", "(d'après la fiche). L'eau de mer contient en moyenne 35 g de sel par litre. Yann laisse évaporer 4 litres d'eau de mer dans un bassin.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Combien de sel Yann récolte-t-il environ ?", ["140 g", "35 g", "70 g", "4 g"], 0, "4 × 35 = 140."),
             ("Pourquoi le sel reste-t-il dans le bassin ?", ["L'eau s'évapore, le sel dissous reste", "Le sel s'évapore aussi", "Le sel fond", "Le sel coule au fond de la mer"], 0, "L'eau passe à l'état de vapeur."),
             ("Peut-on récupérer ce sel en filtrant l'eau de mer ?", ["Non : le sel dissous traverse le filtre", "Oui : le filtre retient le sel", "Oui : avec un tamis", "Oui : avec un aimant"], 0, "Seule l'évaporation le permet.")],
            ["Multiplie 4 litres par 35 g.", "Seule l'eau s'évapore.", "Un solide dissous traverse le filtre."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", L5, [L3, L6, L2], pos=0)),
        "second": vf(
            "Yann a noté six phrases sur l'eau et le sel. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui rappelle qu'une eau filtrée n'est pas forcément potable.",
            [("Une eau filtrée est forcément potable.", False, "Elle peut contenir des substances dissoutes."), ("Le sel dissous traverse le filtre.", True, "Seule l'évaporation le récupère."), ("La décantation sépare un solide non dissous qui se dépose.", True, "On verse doucement le liquide."),
             ("Le sel s'évapore avec l'eau.", False, "L'eau part, le sel reste."), ("L'eau de mer contient environ 35 g de sel par litre.", True, "Ordre de grandeur."), ("La filtration retient un solide dissous.", False, "Elle retient les grains non dissous.")],
            ["Un solide dissous passe à travers le filtre.", "L'eau s'évapore, pas le sel.", "Pour la justification : cherche la phrase qui parle de boire."],
            J("Quelle phrase de la fiche dit qu'une eau filtrée ne se boit pas forcément ?", L9, [L4, L2, L5], pos=1)),
    }
    d["e5-2"] = {
        "lieutenant": {
            "type": "plan", "titre": "Quelle méthode pour quel mélange ?", "colonnes": 2,
            "cases": [{"libelle": "Eau boueuse : on laisse reposer", "reponse": "décantation"}, {"libelle": "Eau et sable : on verse dans un entonnoir garni de papier", "reponse": "filtration"},
                      {"libelle": "Eau salée : on laisse partir l'eau", "reponse": "évaporation"}, {"libelle": "Ce que retient le papier filtre", "reponse": "les grains de sable"},
                      {"libelle": "Ce qui traverse le filtre avec l'eau", "reponse": "le sel dissous"}, {"libelle": "Ce qui reste quand l'eau s'est évaporée", "reponse": "le sel"}],
            "etiquettes": ["décantation", "filtration", "évaporation", "les grains de sable", "le sel dissous", "le sel", "aimantation", "tamisage"],
            "consigne": "Yann associe chaque situation à la méthode ou au résultat. Place chaque étiquette dans la bonne case. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie la filtration.",
            "indices": ["La filtration retient les grains non dissous.", "Un solide dissous passe à travers.", "Seule l'évaporation sépare un solide dissous."],
            "justification": J("Quelle phrase de la fiche justifie la filtration ?", L2, [L1, L3, L4], pos=1)},
        "second": {
            "type": "plan", "titre": "Le sel de la saline", "colonnes": 2,
            "cases": [{"libelle": "1 litre d'eau de mer contient en moyenne", "reponse": "35 g de sel"}, {"libelle": "2 litres d'eau de mer contiennent", "reponse": "70 g de sel"}, {"libelle": "10 litres d'eau de mer contiennent", "reponse": "350 g de sel"},
                      {"libelle": "Le sel dissous, après filtration, est", "reponse": "dans l'eau filtrée"}, {"libelle": "Pour le récupérer, on utilise", "reponse": "l'évaporation"}],
            "etiquettes": ["35 g de sel", "70 g de sel", "350 g de sel", "dans l'eau filtrée", "l'évaporation", "3,5 g de sel", "dans le filtre", "la décantation"],
            "consigne": "Yann calcule le sel de ses bassins. Place chaque étiquette dans la bonne case. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui donne la quantité de sel par litre.",
            "indices": ["2 fois 35, puis 10 fois 35.", "Un solide dissous traverse le filtre.", "Seule l'évaporation le permet."],
            "justification": J("Quelle phrase de la fiche donne la quantité de sel par litre ?", L5, [L6, L3, L4], pos=2)},
    }
    d["e5-3"] = {
        "mousse": lettres(
            "Trouve le mot qui correspond à cette définition : « Papier en forme de cône qui retient les grains de sable. » Ses lettres sont cachées en couleur dans le texte de Yann, dans le désordre. Clique-les dans l'ordre qui forme le mot (6 lettres). Deux lettres sont des pièges.",
            ["F", "I", "L", "T", "R", "E"],
            marque("Yann [r]entre ses seaux. Il [l]ave l'entonnoir, y [f]orme un cône de papier, puis verse le mélange : [i]l faut un bon [t]our de main. L'eau [e]st claire ; il [s]ourit, [m]ais ses mains sont mouillées."),
            ["Ouvre la fiche " + F + ".", "Le mot commence par F.", "Il finit par E."]),
        "lieutenant": lettres(
            "Trouve le mot qui correspond à cette définition : « Laisser reposer pour que le solide tombe au fond, puis verser doucement le liquide. » Ses lettres sont cachées en couleur dans le texte de Yann, dans le désordre. Clique-les dans l'ordre qui forme le mot (8 lettres). Deux lettres sont des pièges. Puis choisis la phrase de la fiche qui définit ce mot.",
            ["D", "E", "C", "A", "N", "T", "E", "R"],
            marque("Yann laisse le seau [r]eposer : la terre va au fond. Il [t]ourne le seau, verse doucement l'eau, [e]t surveille [c]haque goutte. Au cou[d]e à coude avec Lila, il [a]ttend. [n]i trop vite, [e]n suivant le fil de l'eau, [s]ans [p]ersonne pour le gêner."),
            ["Le mot a huit lettres.", "Il commence par D et finit par R.", "C'est la méthode où l'on verse doucement le liquide."],
            J("Quelle phrase de la fiche définit ce mot ?", L1, [L2, L3, L7], pos=1)),
        "second": qcm(
            carnet("Récolte de Yann", "(inventée pour le jeu). Yann a fait évaporer 40 litres d'eau de mer dans un bassin et a récolté 1 400 g de sel. L'eau de mer contient en moyenne 35 g de sel par litre.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui explique le rôle du soleil et du vent.",
            [("Combien de grammes de sel Yann a-t-il récoltés par litre d'eau évaporée ?", ["35 g", "40 g", "14 g", "1 400 g"], 0, "1 400 ÷ 40 = 35."),
             ("Combien de litres faut-il faire évaporer pour récolter 700 g de sel ?", ["20 litres", "35 litres", "70 litres", "10 litres"], 0, "700 ÷ 35 = 20."),
             ("Pourquoi le soleil et le vent sont-ils utiles au paludier ?", ["Ils font évaporer l'eau, le sel reste", "Ils fabriquent le sel", "Ils filtrent l'eau", "Ils aimantent le sel"], 0, "L'eau passe à l'état de vapeur.")],
            ["Divise la masse de sel par le nombre de litres.", "700 divisé par 35.", "Le sel dissous reste quand l'eau part."],
            J("Quelle phrase de la fiche explique le rôle du soleil et du vent ?", L6, [L3, L5, L9], pos=1)),
    }
    d["e5-4"] = {
        "mousse": ordre(
            "Voici le testament de Madame Mélange. Remets les trois opérations dans l'ordre avec ▲ et ▼, puis vérifie. « Dans mon bocal, il y a de l'eau salée. Avant de toucher à quoi que ce soit, note sa masse. Ensuite, laisse l'eau s'en aller : le sel restera. »",
            [("PESER", "noter la masse du bocal"), ("ÉVAPORER", "laisser partir l'eau"), ("COMPARER", "vérifier que rien ne manque")],
            ["Ouvre la fiche " + F + ".", "On pèse avant de toucher au bocal.", "On compare à la fin."]),
        "lieutenant": ordre(
            "Madame Mélange a laissé un autre protocole. Dans le bocal : de l'eau, du sel dissous et du gravier. Remets les cinq opérations dans l'ordre, puis choisis la phrase de la fiche qui justifie qu'on enchaîne les méthodes.",
            [("PESER", "masse de départ"), ("OBSERVER", "le gravier se voit, l'eau salée est homogène"), ("FILTRER", "le gravier reste dans le filtre"), ("ÉVAPORER", "l'eau part, le sel reste"), ("COMPARER", "la masse des solides est conservée")],
            ["On pèse et on observe avant d'agir.", "Filtre avant d'évaporer : sinon le gravier resterait mêlé au sel.", "La dernière opération prouve que rien ne manque."],
            J("Quelle phrase de la fiche justifie qu'on enchaîne les méthodes ?", L7, [L8, L3, L2], pos=0)),
        "second": ordre(
            "Madame Mélange a laissé un dernier protocole : un bocal de 600 g contenant de l'eau, du sel dissous et de la limaille de fer. Remets les cinq opérations dans l'ordre, puis choisis la phrase de la fiche qui garantit le bon résultat final.",
            [("PESER", "masse de départ : 600 g"), ("OBSERVER", "limaille visible ; eau salée homogène"), ("AIMANTER", "on récupère 15 g de limaille"), ("ÉVAPORER", "la vapeur emporte l'eau ; il reste 25 g de sel"), ("COMPARER", "15 g + 25 g = 40 g de solides conservés")],
            ["Ce que la balance sait faire d'abord.", "L'aimant avant l'évaporation.", "La dernière opération compare avec le départ."],
            J("Quelle phrase de la fiche garantit le bon résultat final ?", L8, [L7, L3, L5], pos=1)),
    }
    return d
