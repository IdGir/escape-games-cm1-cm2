# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons CM2) du jeu « La Nurserie du zoo ».
Utilisées mot pour mot : (1) dans lecons.json (gen_lecons.py), (2) dans les justifications des grades lieutenant et second
(vingt-mille-lieues/outils/immersif/grades/naissances_animaux_s*.py). Ne modifier une phrase qu'ici.
Sources : Fondation La main à la pâte, « Biologie animale : fonctions de reproduction » et séquence « Et ils eurent beaucoup d'enfants » ;
Muséum national d'histoire naturelle et INPN ; Lumni. Pas de reproduction humaine dans ce jeu (laissée à l'enseignant)."""

# ---------------------------------------------------------------- Leçon 1 : la fécondation
F_SEXUEE = "Chez la plupart des animaux, un petit naît de la rencontre de deux cellules : une cellule du mâle et une cellule de la femelle."
F_GAMETES = "Ces deux cellules reproductrices s'appellent des gamètes : le gamète mâle est le spermatozoïde, le gamète femelle est l'ovule."
F_ORGANES = "Le mâle produit des spermatozoïdes dans ses testicules ; la femelle produit des ovules dans ses ovaires."
F_TAILLE = "L'ovule est une grosse cellule immobile qui contient des réserves ; le spermatozoïde est une cellule minuscule qui se déplace grâce à son flagelle."
F_FECOND = "La fécondation est la rencontre et l'union d'un spermatozoïde et d'un ovule."
F_OEUF = "La fécondation donne une cellule-œuf : c'est la toute première cellule du futur animal."
F_EMBRYON = "La cellule-œuf se divise en deux, puis en quatre, puis en des milliers de cellules : elle devient un embryon."
F_SANS = "Sans fécondation, il n'y a pas de petit : un œuf de poule acheté au magasin n'a pas été fécondé et ne donnera jamais de poussin."
F_MICRO = "Les gamètes sont si petits qu'on ne les voit qu'au microscope."
F_UN = "Des milliers de spermatozoïdes peuvent s'approcher de l'ovule, mais un seul s'unit à lui."
F_PARENTS = "Le petit ressemble à ses deux parents, car la cellule-œuf réunit une part du mâle et une part de la femelle."
F_ESPECE = "Pour qu'une fécondation donne un petit, le mâle et la femelle doivent être de la même espèce."
LECON_FECOND = [("Deux cellules", [F_SEXUEE, F_GAMETES, F_ORGANES, F_TAILLE, F_MICRO, F_ESPECE]),
                ("La fécondation", [F_FECOND, F_UN, F_OEUF, F_PARENTS, F_EMBRYON, F_SANS])]

# ---------------------------------------------------------------- Leçon 2 : fécondation externe et interne
X_LIEU = "La fécondation peut avoir lieu hors du corps de la femelle ou à l'intérieur de son corps."
X_EXTERNE = "Lors d'une fécondation externe, la femelle pond ses ovules dans l'eau et le mâle y libère ses spermatozoïdes : les gamètes se rencontrent dans l'eau."
X_EX_EXT = "La grenouille, le crapaud, la truite et le saumon ont une fécondation externe."
X_NOMBRE = "En fécondation externe, beaucoup de gamètes sont perdus : c'est pourquoi une femelle grenouille ou une truite pond des centaines, voire des milliers d'ovules."
X_INTERNE = "Lors d'une fécondation interne, le mâle dépose ses spermatozoïdes dans le corps de la femelle, après un accouplement : les gamètes se rencontrent dans le corps de la femelle."
X_EX_INT = "Les oiseaux, les reptiles, les mammifères, les requins et les insectes ont une fécondation interne."
X_EAU = "Vivre dans l'eau ne suffit pas pour avoir une fécondation externe : la tortue marine et le dauphin vivent dans la mer, mais leur fécondation est interne."
X_TRUITE = "Chez la truite, la femelle pond ses ovules dans un creux du gravier de la rivière et le mâle les arrose de ses spermatozoïdes."
X_GELEE = "Les œufs de grenouille sont entourés d'une gelée ; on les trouve au printemps, accrochés aux plantes des mares."
X_RISQUE = "Les œufs pondus dans l'eau ne sont pas gardés : beaucoup sont mangés par d'autres animaux avant d'éclore."
LECON_EXT = [("Où se rencontrent les gamètes ?", [X_LIEU]),
             ("Dans l'eau", [X_EXTERNE, X_EX_EXT, X_TRUITE, X_GELEE, X_NOMBRE, X_RISQUE]),
             ("Dans le corps de la femelle", [X_INTERNE, X_EX_INT, X_EAU])]

# ---------------------------------------------------------------- Leçon 3 : ovipares et vivipares
O_OVIPARE = "Un animal ovipare pond des œufs : le petit se développe dans l'œuf, hors du corps de sa mère, grâce aux réserves de l'œuf."
O_EX_OVI = "Les oiseaux, la plupart des reptiles, des amphibiens, des poissons et des insectes sont ovipares."
O_VIVIPARE = "Un animal vivipare ne pond pas : le petit se développe dans le ventre de sa mère, qui le nourrit, et il naît vivant."
O_EX_VIVI = "Presque tous les mammifères sont vivipares : le chat, la vache, le lapin, l'éléphant, le dauphin."
O_PLACENTA = "Chez les mammifères vivipares, le petit reçoit la nourriture et l'oxygène de sa mère par le placenta et le cordon ombilical."
O_LIEN = "Avec une fécondation externe, les œufs se développent hors du corps de la mère : l'animal est ovipare ; une fécondation interne peut donner un animal ovipare ou vivipare."
O_ORNITHO = "L'ornithorynque est un mammifère d'Australie qui pond des œufs : c'est une exception, car il nourrit pourtant ses petits avec son lait."
O_VIPERE = "Chez la vipère aspic, les œufs restent dans le ventre de la mère jusqu'à l'éclosion : les petits naissent déjà formés, on dit qu'elle est ovovivipare."
O_REQUINS = "Les requins ne font pas tous pareil : la roussette pond des œufs protégés par une capsule, alors que le requin-marteau donne naissance à des petits vivants."
O_COQUILLE = "Les œufs des oiseaux et des reptiles ont une coquille qui les protège et leur permet de se développer sur la terre ferme."
O_LAIT = "Après la naissance, les femelles des mammifères nourrissent leurs petits avec leur lait."
LECON_OVI = [("Pondre ou mettre au monde", [O_OVIPARE, O_EX_OVI, O_COQUILLE, O_VIVIPARE, O_EX_VIVI, O_PLACENTA, O_LAIT]),
             ("Fécondation et mode de reproduction", [O_LIEN]),
             ("Des exceptions", [O_ORNITHO, O_VIPERE, O_REQUINS])]

# ---------------------------------------------------------------- Leçon 4 : le développement avant la naissance
D_EMBRYON = "Avant la naissance ou l'éclosion, l'embryon grandit et forme peu à peu tous ses organes."
D_OEUF = "Dans l'œuf de poule, la coquille protège l'embryon, la chambre à air contient de l'air, le blanc protège l'embryon et lui fournit de l'eau, et le jaune le nourrit."
D_COUVE = "La poule couve ses œufs fécondés pendant 21 jours : sa chaleur permet à l'embryon de se développer."
D_ETAPES = "Vers le 3e jour, le cœur bat et des vaisseaux sanguins entourent le jaune ; vers le 7e jour, on reconnaît la forme du poussin ; vers le 18e jour, ses plumes sont bien visibles."
D_ECLOS = "Le 21e jour, le poussin perce la coquille avec le diamant, une petite pointe au bout de son bec : c'est l'éclosion."
D_GESTATION = "Chez les mammifères, le petit se développe dans l'utérus de sa mère : la durée de ce développement s'appelle la gestation."
D_DUREES = "La gestation dure environ 31 jours chez la lapine, 63 à 65 jours chez la chatte, 280 jours chez la vache, 336 jours chez la jument et 20 à 22 mois chez l'éléphante."
D_TAILLE = "En général, plus un mammifère est grand, plus sa gestation est longue."
D_CHAUD = "Le développement de l'embryon de poule commence quand l'œuf dépasse environ 27 °C."
D_APRES = "Dès le lendemain de l'éclosion, le poussin peut marcher, boire et manger seul, mais il a besoin d'un endroit chaud et abrité."
LECON_DEV = [("Dans l'œuf", [D_EMBRYON, D_OEUF, D_COUVE, D_CHAUD, D_ETAPES, D_ECLOS, D_APRES]),
             ("Dans le ventre de la mère", [D_GESTATION, D_DUREES, D_TAILLE])]

# ---------------------------------------------------------------- Leçon 5 : classer les animaux du zoo
K_DEUX = "Pour décrire la reproduction d'un animal, on se pose deux questions : où a lieu la fécondation, et comment naît le petit."
K_TROIS = "On obtient trois grands cas : fécondation externe et ponte, fécondation interne et ponte, fécondation interne et naissance d'un petit vivant."
K_EXT_OVI = "La grenouille et la truite ont une fécondation externe et sont ovipares."
K_INT_OVI = "La poule, le crocodile, la tortue et le papillon ont une fécondation interne et sont ovipares."
K_INT_VIVI = "La girafe, le lion, le kangourou et le dauphin ont une fécondation interne et sont vivipares."
K_IMPOSSIBLE = "Une femelle ne peut pas porter dans son ventre un œuf fécondé dans l'eau : une fécondation externe ne donne donc jamais un petit qui grandit dans le ventre de sa mère."
K_REGLE = "Une exception, comme l'ornithorynque, ne change pas la règle : elle montre que le vivant est très divers."
K_METHODE = "Pour placer un animal dans le tableau, on cherche d'abord la ligne de sa fécondation, puis la colonne de son mode de reproduction."
K_KANGOUROU = "Le kangourou est vivipare : son petit naît tout petit, puis finit de grandir dans la poche de sa mère."
K_OISEAUX = "Tous les oiseaux sont ovipares ; chez les poissons et les reptiles, la plupart pondent, mais quelques-uns ont des petits qui naissent formés."
K_SOINS = "Connaître le mode de reproduction d'un animal aide les soigneurs à préparer la naissance : une couveuse pour des œufs, un enclos calme pour une mère qui porte son petit."
LECON_CLASSE = [("Deux questions", [K_DEUX, K_TROIS, K_METHODE]),
                ("Des exemples", [K_EXT_OVI, K_INT_OVI, K_INT_VIVI, K_KANGOUROU, K_OISEAUX]),
                ("Ce qui n'existe pas", [K_IMPOSSIBLE, K_REGLE, K_SOINS])]


def html(sections):
    return "".join(f"<h4>{h}</h4><p>{' '.join(ps)}</p>" for h, ps in sections)
