# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons CM2) du jeu « Le Jardin de la vie ».
Utilisées mot pour mot : (1) dans lecons.json (gen_lecons.py), (2) dans les justifications des grades Botaniste et Directeur du jardin
(vingt-mille-lieues/outils/immersif/grades/reproduction_s*.py). Ne modifier une phrase qu'ici.
Programme : BO n° 24 du 11 juin 2026, annexe 2, « Les êtres vivants dans leur environnement ».
- CM1, « Reproduction, croissance et développement », cycle de vie : décrire les étapes du développement des animaux de la fécondation
  à la naissance ; mettre en relation le type de fécondation (interne ou externe) avec le mode de reproduction ovipare et vivipare.
- CM1, « Unité et diversité du vivant » : définir une espèce comme un ensemble d'individus interféconds.
- 6e, « Reproduction, croissance et développement » : rôle de la pollinisation dans la transformation de la fleur en fruit et des ovules
  en graines ; coopération (pollinisation) ; insecticides et pollinisateurs. 6e, diversité des individus et variation héréditaire.
- Cycle 2 (CE2), rappel : étapes de la vie d'une plante à fleurs (germination, croissance, fleur, fruit, dispersion des graines).
La reproduction humaine et la puberté ne sont pas traitées ici (séquence à part, conduite par l'enseignant).
Sources : La main à la pâte (« Le cycle de vie des végétaux », « De quoi a besoin une graine pour germer ») ; Universalis (« Fleur ») ;
FAO (incubation naturelle) ; MNHN, INPN, OFB (pollinisateurs)."""

# ---------------------------------------------------------------- Leçon 1 : la fleur
F_ORGANE = "La fleur est l'organe de la reproduction des plantes à fleurs."
F_ENVELOPPES = "Les sépales, souvent verts, protègent le bouton ; les pétales, souvent colorés, attirent les insectes."
F_ETAMINES = "Les étamines sont les organes mâles de la fleur : elles fabriquent le pollen, une poudre souvent jaune."
F_PISTIL = "Le pistil, au centre de la fleur, est l'organe femelle : sa partie renflée, l'ovaire, contient les ovules."
F_STIGMATE = "Le haut du pistil, le stigmate, est collant : c'est là que le pollen doit se déposer."
F_DEUX = "Beaucoup de fleurs ont à la fois des étamines et un pistil ; chez certaines plantes, comme le noisetier, il y a des fleurs mâles et des fleurs femelles séparées."
F_OBSERVER = "Pour observer une fleur, on la dissèque : on détache ses pièces une à une, de l'extérieur vers le centre, et on les colle sur une feuille."
LECON_FLEUR = [("Une fleur pour se reproduire", [F_ORGANE, F_ENVELOPPES]),
               ("Les organes mâles et femelles", [F_ETAMINES, F_PISTIL, F_STIGMATE, F_DEUX]),
               ("Observer une fleur", [F_OBSERVER])]

# ---------------------------------------------------------------- Leçon 2 : pollinisation et fécondation
P_POLLINISATION = "La pollinisation est le transport du pollen des étamines jusqu'au pistil d'une fleur de la même espèce."
P_INSECTES = "La plupart des fleurs sont pollinisées par des insectes, comme les abeilles, les bourdons ou les papillons, qui viennent boire le nectar."
P_VENT = "Certaines plantes, comme le maïs, les graminées des prairies ou le noisetier, sont pollinisées par le vent : leurs fleurs sont discrètes et leur pollen très abondant."
P_FECONDATION = "Après la pollinisation, le pollen permet de féconder les ovules cachés dans l'ovaire."
P_FRUIT = "Après la fécondation, l'ovaire grossit et devient le fruit, et les ovules deviennent les graines."
P_FANER = "Pendant ce temps, les pétales et les étamines fanent et tombent : ils ne servent plus."
P_COOPERATION = "La pollinisation est une coopération : l'insecte se nourrit de nectar et de pollen, et la plante est fécondée."
P_INSECTICIDES = "Quand on utilise beaucoup d'insecticides, les pollinisateurs deviennent moins nombreux, et certaines cultures donnent moins de fruits et de graines."
LECON_POLLEN = [("Le voyage du pollen", [P_POLLINISATION, P_INSECTES, P_VENT]),
                ("De la fleur au fruit", [P_FECONDATION, P_FRUIT, P_FANER]),
                ("Pour aller plus loin (6e) : protéger les pollinisateurs", [P_COOPERATION, P_INSECTICIDES])]

# ---------------------------------------------------------------- Leçon 3 : graines, dispersion, germination
G_CONTIENT = "Une graine contient une future plante, l'embryon, et des réserves de nourriture, protégés par une enveloppe."
G_DISPERSION = "Les graines s'éloignent de la plante mère : c'est la dispersion, qui permet à l'espèce de s'installer dans de nouveaux lieux."
G_VENT = "Certaines graines sont emportées par le vent grâce à des aigrettes, comme celles du pissenlit, ou à des ailes, comme celles de l'érable."
G_ANIMAUX = "D'autres voyagent grâce aux animaux : accrochées à leurs poils, comme celles de la bardane, ou cachées et oubliées, comme les glands par le geai."
G_EAU = "D'autres encore flottent et voyagent sur l'eau, comme la noix de coco."
G_GERMINATION = "La germination est le moment où la graine se réveille : la racine sort, puis la tige et les premières feuilles."
G_BESOINS = "Pour germer, une graine a besoin d'eau, d'air et d'une température douce ; la plupart des graines n'ont pas besoin de lumière pour germer."
G_LUMIERE = "Après la germination, la jeune plante a besoin de lumière pour grandir et fabriquer sa nourriture."
G_CYCLE = "Le cycle de vie d'une plante à fleurs : la graine germe, la plante grandit, fleurit, ses fleurs deviennent des fruits qui contiennent de nouvelles graines."
LECON_GRAINES = [("Ce que contient une graine", [G_CONTIENT]),
                 ("Le voyage des graines", [G_DISPERSION, G_VENT, G_ANIMAUX, G_EAU]),
                 ("La germination", [G_GERMINATION, G_BESOINS, G_LUMIERE, G_CYCLE])]

# ---------------------------------------------------------------- Leçon 4 : la fécondation chez les animaux
A_SEXES = "Chez les animaux, pour avoir des petits, il faut en général un mâle et une femelle de la même espèce."
A_CELLULES = "Le mâle produit des cellules reproductrices mâles, la femelle des cellules reproductrices femelles : on les appelle les gamètes."
A_FECONDATION = "La fécondation est la rencontre d'une cellule reproductrice mâle et d'une cellule reproductrice femelle : elle donne la première cellule d'un nouvel être vivant."
A_INTERNE = "Chez les oiseaux et les mammifères, la fécondation a lieu à l'intérieur du corps de la femelle : elle est interne."
A_EXTERNE = "Chez la grenouille et chez beaucoup de poissons, comme la truite, la femelle pond ses ovules dans l'eau et le mâle les féconde dehors : la fécondation est externe."
A_EAU = "La fécondation externe se fait dans l'eau : les cellules reproductrices ne survivraient pas à l'air libre."
A_NOMBRE = "Les animaux à fécondation externe pondent souvent un très grand nombre d'œufs, car beaucoup ne seront pas fécondés ou seront mangés."
LECON_FECONDATION = [("Un mâle et une femelle", [A_SEXES, A_CELLULES, A_FECONDATION]),
                     ("Dedans ou dehors", [A_INTERNE, A_EXTERNE, A_EAU]),
                     ("Pour aller plus loin", [A_NOMBRE])]

# ---------------------------------------------------------------- Leçon 5 : naître ou éclore, la même espèce
N_EMBRYON = "Après la fécondation, l'embryon se développe : il grandit et ses organes se forment."
N_OVIPARE = "Chez les animaux ovipares, comme la poule, la tortue ou la grenouille, l'embryon se développe dans un œuf pondu, puis le petit sort de l'œuf : c'est l'éclosion."
N_VIVIPARE = "Chez les animaux vivipares, comme la vache, la brebis ou la lapine, l'embryon se développe dans le ventre de sa mère, puis le petit naît."
N_LIEN = "Une fécondation externe va toujours avec la ponte d'œufs ; une fécondation interne peut aller avec la ponte d'œufs, comme chez la poule, ou avec une naissance, comme chez la vache."
N_LARVE = "Certains animaux sortent de l'œuf sous la forme d'une larve, très différente de l'adulte : le têtard devient grenouille, la chenille devient papillon."
N_DUREES = "L'œuf de poule éclot après environ 21 jours de couvaison ; le veau naît après environ 9 mois, et l'agneau après environ 5 mois."
N_ESPECE = "Une espèce est un ensemble d'êtres vivants qui peuvent se reproduire entre eux : un petit appartient toujours à la même espèce que ses parents."
N_DIFFERENTS = "Les petits ressemblent à leurs parents, mais ne sont pas identiques à eux ni entre eux : chaque individu est unique."
N_DIVERSITE = "Ces petites différences entre les individus d'une même espèce sont en partie héritées des parents : c'est une richesse pour l'espèce."
LECON_NAITRE = [("Dans un œuf ou dans le ventre", [N_EMBRYON, N_OVIPARE, N_VIVIPARE, N_LIEN, N_LARVE]),
                ("Combien de temps ?", [N_DUREES]),
                ("La même espèce, mais chacun est unique", [N_ESPECE, N_DIFFERENTS, N_DIVERSITE])]


def html(sections):
    return "".join(f"<h4>{h}</h4><p>{' '.join(ps)}</p>" for h, ps in sections)
