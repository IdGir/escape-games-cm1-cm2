# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons CM2) du jeu « Les Lettres du poilu » (Première Guerre mondiale).
Utilisées mot pour mot : (1) dans lecons.json (gen_lecons.py), (2) dans les justifications des grades Historien et Gardien de la mémoire
(vingt-mille-lieues/outils/immersif/grades/grande_guerre_s*.py). Ne modifier une phrase qu'ici.
SUJET SENSIBLE : ton du souvenir, aucun détail violent, chiffres officiels uniquement (sources ci-dessous).
Sources : ministère des Armées, Chemins de mémoire (« Un deuil national », « 1916. Les batailles de Verdun et de la Somme »,
« 11 novembre, journée nationale de commémoration ») ; musée de l'Armée, fiche objet « L'affiche de mobilisation » (2025) ;
Encyclopædia Universalis, « Le rôle des colonies » et « Grande Guerre et société » ; info.gouv.fr, « Pourquoi le 11 novembre est-il férié ? »."""

# ---------------------------------------------------------------- Leçon 1 : 1914, l'entrée en guerre
C_RIVAL = "Au début du XXe siècle, les grandes puissances d'Europe sont rivales : elles se disputent des territoires, des colonies et des marchés."
C_ALSACE = "Depuis la guerre de 1870, l'Alsace et la Moselle appartiennent à l'Allemagne, et beaucoup de Français veulent les retrouver."
C_ALLI = "Les pays forment deux alliances : la Triple-Entente (France, Royaume-Uni, Russie) face à l'alliance de l'Allemagne et de l'Autriche-Hongrie."
C_SARA = "Le 28 juin 1914, à Sarajevo, l'archiduc François-Ferdinand, héritier de l'Autriche-Hongrie, est assassiné par un jeune nationaliste serbe."
C_ENGRE = "À cause des alliances, les pays entrent en guerre les uns après les autres : une crise locale devient une guerre européenne, puis mondiale."
C_MOBIL = "Le 1er août 1914, l'affiche de la mobilisation générale est collée dans toutes les communes de France ; la mobilisation commence le 2 août."
C_DECLA = "Le 3 août 1914, l'Allemagne déclare la guerre à la France."
C_NOMBRE = "En 1914, la mobilisation fait passer l'armée française de 800 000 à près de 3,6 millions d'hommes ; pendant toute la guerre, 8,7 millions de Français sont mobilisés."
C_FLEUR = "L'image des soldats partant « la fleur au fusil » est surtout une légende : la plupart partent avec résignation et sens du devoir."
C_COURTE = "Presque tout le monde croit à une guerre courte, finie en quelques mois : elle durera plus de quatre ans."
C_SERBIE = "Le 28 juillet 1914, l'Autriche-Hongrie déclare la guerre à la Serbie."
C_BELGIQUE = "Pour attaquer la France, l'armée allemande traverse la Belgique, un pays neutre : le Royaume-Uni entre alors en guerre."
LECON_CAUSES = [("Une Europe divisée", [C_RIVAL, C_ALSACE, C_ALLI]),
                ("L'été 1914", [C_SARA, C_SERBIE, C_ENGRE, C_MOBIL, C_DECLA, C_BELGIQUE, C_NOMBRE]),
                ("Légende ou réalité ?", [C_FLEUR, C_COURTE])]

# ---------------------------------------------------------------- Leçon 2 : le front et les tranchées
F_FRONT = "À la fin de 1914, les armées s'enterrent : un front continu de tranchées va de la mer du Nord à la frontière suisse."
F_TRANCHEE = "Une tranchée est un fossé creusé dans la terre, protégé par des sacs de sable et des barbelés ; des boyaux la relient à l'arrière."
F_ABRI = "Les soldats dorment dans des abris creusés sous terre ; entre les tranchées ennemies s'étend le no man's land, la « terre de personne »."
F_POILU = "On appelle « poilus » les soldats français de la Grande Guerre."
F_VIE = "Les poilus vivent dans la boue et le froid, avec les rats et les poux ; ils sont souvent épuisés et ont peur."
F_LETTRES = "Pour tenir, ils écrivent des lettres, reçoivent des colis de leur famille et comptent sur la camaraderie."
F_CENSURE = "Le courrier est surveillé par la censure : les soldats ne doivent pas écrire où ils sont ni ce que prépare l'armée."
F_VERDUN = "La bataille de Verdun dure du 21 février au 18 décembre 1916 ; l'armée française y résiste aux attaques allemandes."
F_SOMME = "La bataille de la Somme commence le 1er juillet 1916 : les Britanniques et les Français y attaquent ensemble jusqu'au 18 novembre 1916."
F_ARMES = "La guerre utilise des armes nouvelles ou bien plus nombreuses : mitrailleuses, canons lourds, gaz de combat, avions et chars."
F_GAZ = "Les gaz de combat sont employés à partir de 1915 : les soldats doivent alors porter des masques."
F_CHARS = "Les premiers chars d'assaut, britanniques, apparaissent en 1916 pendant la bataille de la Somme."
F_COLONIES = "Environ 600 000 soldats venus des colonies, d'Afrique du Nord, d'Afrique de l'Ouest, de Madagascar ou d'Indochine, combattent dans l'armée française."
LECON_FRONT = [("La guerre des tranchées", [F_FRONT, F_TRANCHEE, F_ABRI]),
               ("La vie des poilus", [F_POILU, F_VIE, F_LETTRES, F_CENSURE]),
               ("Batailles et armes", [F_VERDUN, F_SOMME, F_ARMES, F_GAZ, F_CHARS]),
               ("Des soldats de tout l'empire", [F_COLONIES])]

# ---------------------------------------------------------------- Leçon 3 : l'arrière
A_ARRIERE = "L'arrière, c'est tout le pays qui n'est pas sur le front : les villes, les villages, les usines et les champs."
A_CHAMPS = "Dans les campagnes, les femmes, les enfants et les anciens font les moissons et les vendanges à la place des hommes partis."
A_USINES = "Dans les usines, des femmes remplacent les hommes ; celles qui fabriquent des obus sont appelées les « munitionnettes »."
A_430 = "En 1918, environ 430 000 femmes travaillent dans les usines d'armement."
A_METIERS = "Les femmes deviennent aussi conductrices de tramway, factrices ou infirmières."
A_ECOLE = "À l'école, les élèves écrivent aux soldats, collectent de l'argent et des vêtements : la guerre entre dans la classe."
A_ECONOMIE = "Toute l'économie travaille pour la guerre : les usines fabriquent des obus, des canons et des uniformes ; on parle d'économie de guerre."
A_TRAVAILLEURS = "Des travailleurs venus des colonies et de pays étrangers travaillent dans les usines, les ports et les champs de France."
A_CHINOIS = "Environ 40 000 ouvriers chinois sont ainsi employés en France, par exemple dans les usines du Creusot."
A_VOTE = "Malgré leur travail, les femmes ne votent pas encore en France : elles obtiendront le droit de vote en 1944."
A_ATTENTE = "À l'arrière, les familles attendent les lettres, et chaque village apprend la mort de certains de ses soldats."
A_HOPITAL = "Des écoles, des hôtels et des châteaux deviennent des hôpitaux pour soigner les blessés."
LECON_ARRIERE = [("Tout un pays en guerre", [A_ARRIERE, A_ECONOMIE, A_HOPITAL, A_ATTENTE]),
                 ("Les femmes", [A_CHAMPS, A_USINES, A_430, A_METIERS, A_VOTE]),
                 ("Les enfants et les travailleurs venus d'ailleurs", [A_ECOLE, A_TRAVAILLEURS, A_CHINOIS])]

# ---------------------------------------------------------------- Leçon 4 : 1918, la fin des combats
R_USA = "En avril 1917, les États-Unis entrent en guerre aux côtés de la France et du Royaume-Uni."
R_RUSSIE = "En 1917, la Russie connaît une révolution et arrête bientôt de combattre."
R_ARMI = "L'armistice est signé le 11 novembre 1918 à 5 h 15, dans la clairière de Rethondes, en forêt de Compiègne."
R_ONZE = "Le 11 novembre 1918, à 11 heures, les clairons et les cloches annoncent dans toute la France la fin des combats."
R_DEF = "Un armistice est un accord qui arrête les combats ; ce n'est pas encore la paix."
R_VERSAILLES = "La paix est signée le 28 juin 1919 à Versailles, dans la galerie des Glaces : c'est le traité de Versailles."
R_TRAITE = "L'Allemagne est déclarée responsable de la guerre : elle doit rendre l'Alsace et la Moselle à la France, payer des réparations et réduire son armée."
R_MORTS = "Près de 1,4 million de soldats français sont morts pendant la guerre."
R_VEUVES = "La guerre laisse en France près de 600 000 veuves et des centaines de milliers d'orphelins."
R_DUREE = "Pour la France, la guerre a duré plus de quatre ans, du 3 août 1914 au 11 novembre 1918."
R_BLESSES = "Beaucoup de soldats reviennent blessés ou malades et en gardent les traces toute leur vie."
R_RETOUR = "Les soldats ne rentrent pas tous chez eux tout de suite : la démobilisation dure de longs mois."
LECON_ARMI = [("La fin des combats", [R_USA, R_RUSSIE, R_DEF, R_ARMI, R_ONZE, R_DUREE]),
              ("La paix", [R_VERSAILLES, R_TRAITE]),
              ("Un bilan très lourd", [R_MORTS, R_VEUVES, R_BLESSES, R_RETOUR])]

# ---------------------------------------------------------------- Leçon 5 : se souvenir, et les conséquences
M_MONUMENT = "Après la guerre, presque chaque commune de France construit un monument aux morts, surtout au début des années 1920."
M_NOMS = "Sur le monument sont gravés les noms des soldats de la commune « morts pour la France »."
M_11NOV = "Depuis la loi du 24 octobre 1922, le 11 novembre est un jour férié : on se rassemble devant le monument aux morts."
M_INCONNU = "Le 11 novembre 1920, le cercueil d'un soldat inconnu est conduit à l'Arc de Triomphe, à Paris : il représente tous les morts de la guerre."
M_2012 = "Depuis 2012, le 11 novembre rend hommage à tous les morts pour la France, de toutes les guerres."
M_BASE = "Aujourd'hui, la base « Mémoire des hommes » du ministère des Armées permet de retrouver la fiche de chaque soldat mort pour la France."
M_CONSEQ = "La guerre laisse des régions détruites, des familles en deuil et beaucoup de colère, surtout dans les pays vaincus."
M_CRISE = "Après la guerre, beaucoup de pays connaissent des difficultés : dettes, chômage, puis une grave crise économique à partir de 1929."
M_EXTREMES = "Dans ce climat, des partis extrémistes promettent l'ordre par la force : en Italie, Mussolini prend le pouvoir en 1922 et supprime peu à peu les libertés."
M_SUITE = "Ces régimes autoritaires conduiront le monde vers une nouvelle guerre mondiale, qui commence en 1939."
M_DEUIL = "Dans les familles, le deuil dure longtemps : beaucoup d'enfants grandissent sans leur père."
LECON_MEMOIRE = [("Le monument aux morts", [M_MONUMENT, M_NOMS, M_DEUIL, M_BASE]),
                 ("Le 11 novembre", [M_11NOV, M_INCONNU, M_2012]),
                 ("Une paix fragile", [M_CONSEQ, M_CRISE, M_EXTREMES, M_SUITE])]


def html(sections):
    return "".join(f"<h4>{h}</h4><p>{' '.join(ps)}</p>" for h, ps in sections)
