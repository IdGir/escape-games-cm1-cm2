# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons CM2) du jeu « La Centrale en panne ».
Utilisées mot pour mot : (1) dans lecons.json (gen_lecons.py), (2) dans les justifications des grades lieutenant et second
(vingt-mille-lieues/outils/immersif/grades/electricite_s*.py). Ne modifier une phrase qu'ici."""

# ---------------------------------------------------------------- Leçon 1 : le circuit électrique
C_ELEM = "Un circuit électrique simple comprend un générateur, comme une pile, un ou plusieurs récepteurs, comme une lampe ou un moteur, et des fils de connexion."
C_BORNES = "La pile a deux bornes, la borne + et la borne − ; une lampe a elle aussi deux bornes, sur son culot."
C_BOUCLE = "Pour qu'une lampe s'allume, il faut une boucle ininterrompue de conducteurs et de récepteurs, qui part d'une borne de la pile et revient à l'autre borne."
C_FERME = "Quand la boucle est complète, on dit que le circuit est fermé : le courant circule et la lampe brille."
C_OUVERT = "Si un fil est débranché ou si l'interrupteur est ouvert, la boucle est coupée : le circuit est ouvert et la lampe s'éteint."
C_INTER = "L'interrupteur sert à ouvrir ou à fermer le circuit sans débrancher les fils."
C_DEUX = "On peut placer deux lampes dans la même boucle : si l'une est dévissée, la boucle est coupée et l'autre s'éteint aussi."
C_USE = "Le courant ne s'use pas en traversant la lampe : c'est la pile qui s'use peu à peu et finit par ne plus faire briller la lampe."
C_DERIV = "En dérivation, chaque lampe a sa propre boucle reliée à la pile : si l'une est dévissée, l'autre reste allumée."
C_COURT = "Relier directement les deux bornes de la pile par un fil, sans récepteur, provoque un court-circuit : le fil chauffe et la pile s'use très vite."
LECON_CIRCUIT = [("Les éléments d'un circuit", [C_ELEM, C_BORNES]),
                 ("Une boucle sans interruption", [C_BOUCLE, C_FERME, C_OUVERT, C_INTER]),
                 ("Deux récepteurs", [C_DEUX, C_DERIV]),
                 ("Ce qui s'use", [C_USE, C_COURT])]

# ---------------------------------------------------------------- Leçon 2 : conducteurs et isolants
I_COND = "Un conducteur est un matériau qui laisse passer le courant électrique."
I_METAL = "Les métaux, comme le cuivre, le fer, l'aluminium ou l'or, sont de bons conducteurs."
I_ISOL = "Un isolant est un matériau qui ne laisse pas passer le courant : le plastique, le verre, le bois sec, le caoutchouc, le papier ou le tissu sont isolants."
I_TEST = "Pour savoir si un objet est conducteur, on le place dans la boucle d'un circuit testeur : si la lampe s'allume, l'objet est conducteur."
I_GRAPHITE = "La mine d'un crayon à papier, faite de graphite, conduit le courant même si ce n'est pas un métal."
I_FIL = "Un fil électrique est fait d'un cœur en cuivre qui conduit le courant, entouré d'une gaine en plastique qui isole."
I_MEME = "Un même objet peut être fabriqué dans un matériau conducteur ou isolant : une cuillère en métal conduit, une cuillère en bois ne conduit pas."
I_EAU = "L'eau du robinet conduit le courant du secteur : c'est pourquoi il ne faut jamais toucher un appareil électrique avec les mains mouillées."
I_AIR = "L'air sec est isolant : quand l'interrupteur est ouvert, c'est une couche d'air qui coupe la boucle."
I_CORPS = "Le corps humain conduit lui aussi le courant : c'est pour cela que le courant du secteur est dangereux pour nous."
I_PROTEGE = "On utilise des isolants pour protéger les personnes : les prises, les interrupteurs et les poignées des outils d'électricien sont en plastique."
LECON_COND = [("Conducteurs et isolants", [I_COND, I_METAL, I_ISOL, I_AIR]),
              ("Tester un objet", [I_TEST, I_GRAPHITE, I_MEME]),
              ("Dans la vie de tous les jours", [I_FIL, I_PROTEGE, I_CORPS, I_EAU])]

# ---------------------------------------------------------------- Leçon 3 : le schéma normalisé
S_SCHEMA = "Un schéma électrique représente un circuit avec des symboles normalisés, les mêmes partout dans le monde."
S_FILS = "Les fils de connexion sont dessinés par des traits droits, et le circuit forme souvent un rectangle."
S_PILE = "La pile est représentée par un grand trait et un petit trait parallèles : le grand trait est la borne +."
S_LAMPE = "La lampe est représentée par un cercle barré d'une croix."
S_MOTEUR = "Le moteur est représenté par un cercle contenant la lettre M."
S_INTER = "L'interrupteur ouvert est dessiné par un trait levé, l'interrupteur fermé par un trait couché qui ferme le passage."
S_LIRE = "Pour lire un schéma, on suit le trajet du courant avec le doigt, de la borne + de la pile jusqu'à la borne −, en passant par chaque appareil."
S_POURQUOI = "Un schéma est plus rapide à dessiner qu'un dessin réaliste, et tout le monde peut le comprendre."
S_DESSIN = "Sur un dessin réaliste, on reconnaît la forme des objets ; sur un schéma, on ne garde que l'essentiel : les appareils et la façon dont ils sont reliés."
S_REGLE = "Pour dessiner un schéma, on trace les fils à la règle et on place les symboles sur les fils, sans laisser de trou dans la boucle."
S_COUPE = "Si l'interrupteur dessiné est ouvert, la boucle est coupée : sur ce schéma, aucun appareil de la boucle ne fonctionne."
S_POSITION = "On peut dessiner les appareils à des places différentes : deux schémas sont équivalents si les appareils sont reliés de la même façon."
LECON_SCHEMA = [("Pourquoi un schéma ?", [S_SCHEMA, S_DESSIN, S_POURQUOI]),
                ("Les symboles", [S_PILE, S_LAMPE, S_MOTEUR, S_INTER]),
                ("Dessiner et lire un schéma", [S_FILS, S_REGLE, S_LIRE, S_COUPE, S_POSITION])]

# ---------------------------------------------------------------- Leçon 4 : la sécurité
D_PILE = "Les piles utilisées en classe, comme la pile plate de 4,5 volts, ne présentent pas de danger pour le corps."
D_SECTEUR = "Le courant du secteur, celui des prises de la maison, a une tension de 230 volts : il est dangereux et peut tuer."
D_ELECTRO = "Si le courant traverse le corps, il provoque une électrisation qui peut brûler et arrêter le cœur ; quand elle est mortelle, on parle d'électrocution."
D_PRISE = "Il ne faut jamais introduire un objet dans une prise, ni démonter un appareil branché."
D_EAU = "Il ne faut jamais utiliser un appareil électrique avec les mains mouillées ou près d'une baignoire."
D_LIGNES = "Il ne faut jamais faire voler un cerf-volant ou un drone près des lignes électriques, ni grimper sur un pylône ou entrer dans un poste électrique."
D_FIL = "Pour débrancher un appareil, on tire sur la fiche et non sur le fil ; un fil abîmé doit être remplacé."
D_SECOURS = "Si une personne est électrisée, on ne la touche pas : on coupe d'abord le courant au disjoncteur, puis on appelle les secours au 18 ou au 112."
D_ECO = "Éteindre la lumière en quittant une pièce et ne pas laisser les appareils en veille permettent d'économiser l'électricité."
D_LED = "Une lampe à LED éclaire autant qu'une ancienne lampe à incandescence en consommant beaucoup moins d'électricité."
LECON_SECU = [("Pile ou secteur ?", [D_PILE, D_SECTEUR, D_ELECTRO]),
              ("Les règles à la maison", [D_PRISE, D_EAU, D_FIL]),
              ("Dehors et en cas d'accident", [D_LIGNES, D_SECOURS]),
              ("Économiser l'électricité", [D_ECO, D_LED])]

# ---------------------------------------------------------------- Leçon 5 : produire et transporter
P_CENTRALE = "L'électricité du secteur est produite dans des centrales électriques."
P_ALTERN = "Dans la plupart des centrales, quelque chose fait tourner une turbine reliée à un alternateur, qui produit le courant."
P_NUCL = "Dans une centrale nucléaire, la chaleur produite par l'uranium transforme de l'eau en vapeur, qui fait tourner la turbine."
P_HYDRO = "Dans une centrale hydraulique, c'est l'eau retenue par un barrage qui fait tourner la turbine en descendant."
P_EOL = "Dans une éolienne, c'est le vent qui fait tourner les pales."
P_SOL = "Les panneaux solaires photovoltaïques transforment directement la lumière du Soleil en électricité, sans rien faire tourner."
P_THERM = "Dans une centrale thermique, on brûle du gaz, du charbon ou du fioul pour produire de la vapeur."
P_RENOUV = "L'eau, le vent et le Soleil sont des sources d'énergie renouvelables ; l'uranium, le gaz, le charbon et le fioul ne se renouvellent pas."
P_2025 = "En 2025, la France a produit 547,5 milliards de kilowattheures d'électricité : environ 68 % venaient du nucléaire, 11 % de l'hydraulique, 9 % de l'éolien, 6 % du solaire et 3 % du gaz."
P_TRANSPORT = "À la sortie de la centrale, un transformateur élève la tension, puis les lignes à très haute tension portées par des pylônes transportent l'électricité sur de longues distances."
P_RTE = "Le réseau de transport français compte environ 106 000 km de lignes à haute et très haute tension."
P_POSTE = "Près des villes, des postes de transformation abaissent la tension ; le réseau de distribution amène ensuite l'électricité jusqu'au compteur et aux prises de chaque maison."
P_EQUILIBRE = "L'électricité se stocke très mal : à chaque instant, il faut produire autant d'électricité que l'on en consomme."
LECON_PROD = [("Les centrales", [P_CENTRALE, P_ALTERN, P_NUCL, P_HYDRO, P_EOL, P_SOL, P_THERM]),
              ("Des sources renouvelables ou non", [P_RENOUV, P_2025]),
              ("De la centrale à la prise", [P_TRANSPORT, P_RTE, P_POSTE, P_EQUILIBRE])]


def html(sections):
    return "".join(f"<h4>{h}</h4><p>{' '.join(ps)}</p>" for h, ps in sections)
