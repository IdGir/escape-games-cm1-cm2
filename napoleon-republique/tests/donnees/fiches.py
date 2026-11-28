# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons CM2) du jeu « Le Testament de l'Empereur » (Napoléon et la République).
Utilisées mot pour mot : (1) dans lecons.json (gen_lecons.py), (2) dans les justifications des grades Archiviste et Conservateur
(vingt-mille-lieues/outils/immersif/grades/napoleon_republique_s*.py). Ne modifier une phrase qu'ici.
Bilan nuancé (ni hagiographie ni caricature) : réformes durables, mais guerres, morts, autoritarisme et rétablissement de l'esclavage.
Sources : Fondation Napoléon (napoleon.org, « Masses de granit », « Le Sacre ») ; Banque de France ; Musée de l'Armée ;
Élysée (« La Marseillaise ») ; Constitution du 4 octobre 1958, article 2 ; vie-publique.fr. Points à relire : A-VERIFIER.md."""

# ---------------------------------------------------------------- Leçon 1 : du général au Premier consul
G_NAISS = "Napoléon Bonaparte naît le 15 août 1769 à Ajaccio, en Corse, une île devenue française un an plus tôt."
G_OFFICIER = "Il devient officier d'artillerie dans l'armée du roi, puis il soutient la Révolution."
G_TOULON = "En décembre 1793, le jeune capitaine Bonaparte aide l'armée de la République à reprendre le port de Toulon aux Anglais : il est nommé général à 24 ans."
G_ITALIE = "En 1796 et 1797, il commande l'armée d'Italie et remporte de nombreuses victoires contre l'Autriche, comme à Arcole et à Rivoli."
G_GLOIRE = "Il fait raconter ses victoires dans des journaux et des tableaux : il devient un général très populaire."
G_EGYPTE = "En 1798, il part en Égypte avec une armée et des savants ; le 21 juillet 1798, il gagne la bataille des Pyramides."
G_SAVANTS = "Les savants étudient le pays ; la pierre de Rosette, découverte en 1799, aidera plus tard à lire les hiéroglyphes."
G_BRUMAIRE = "Le 18 brumaire an VIII, c'est-à-dire le 9 novembre 1799, il prend le pouvoir par un coup d'État."
G_CONSULAT = "Un nouveau régime commence, le Consulat : trois consuls gouvernent, mais le Premier consul, Bonaparte, a presque tous les pouvoirs."
G_CONCORDAT = "Le 15 juillet 1801, il signe avec le pape le Concordat, qui fait la paix avec l'Église catholique."
G_VIE = "En 1802, il est nommé consul à vie : il garde le pouvoir jusqu'à sa mort."
LECON_GENERAL = [("Un jeune officier", [G_NAISS, G_OFFICIER, G_TOULON]),
                 ("Un général célèbre", [G_ITALIE, G_GLOIRE, G_EGYPTE, G_SAVANTS]),
                 ("Le Premier consul", [G_BRUMAIRE, G_CONSULAT, G_CONCORDAT, G_VIE])]

# ---------------------------------------------------------------- Leçon 2 : le sacre et la naissance de l'Empire
S_PROCLAME = "Le 18 mai 1804, Bonaparte est proclamé empereur des Français : il prend le nom de Napoléon Ier."
S_PLEBISCITE = "Les Français approuvent ce changement par un vote, appelé plébiscite."
S_HEREDITAIRE = "L'Empire est héréditaire : le pouvoir doit passer à un fils de l'empereur, comme dans une monarchie."
S_SACRE = "Le 2 décembre 1804, il est sacré dans la cathédrale Notre-Dame de Paris, en présence du pape Pie VII."
S_COURONNE = "Pendant la cérémonie, Napoléon pose lui-même la couronne sur sa tête, puis il couronne l'impératrice Joséphine."
S_DAVID = "Le peintre Jacques-Louis David, premier peintre de l'Empereur, représente la cérémonie dans un immense tableau, aujourd'hui au musée du Louvre."
S_CHOIX = "David a choisi de peindre le moment où Napoléon couronne Joséphine."
S_AIGLE = "L'aigle, symbole de puissance et de victoire, devient l'emblème de l'Empire, comme dans la Rome antique."
S_ABEILLE = "Les abeilles d'or, brodées sur le manteau du sacre, remplacent la fleur de lys des rois."
S_INSIGNES = "Pour le sacre, l'empereur porte une couronne de lauriers d'or et tient le sceptre et la main de justice."
S_COUR = "Napoléon s'entoure d'une cour et crée une noblesse d'Empire, avec des princes, des comtes et des barons."
LECON_SACRE = [("Un empereur", [S_PROCLAME, S_PLEBISCITE, S_HEREDITAIRE]),
               ("Le sacre à Notre-Dame", [S_SACRE, S_COURONNE, S_DAVID, S_CHOIX]),
               ("Les symboles de l'Empire", [S_AIGLE, S_ABEILLE, S_INSIGNES, S_COUR])]

# ---------------------------------------------------------------- Leçon 3 : les conquêtes et la chute
C_AUSTER = "Le 2 décembre 1805, un an jour pour jour après le sacre, Napoléon bat les armées d'Autriche et de Russie à Austerlitz."
C_IENA = "Le 14 octobre 1806, il bat l'armée de Prusse à Iéna."
C_WAGRAM = "En juillet 1809, il bat de nouveau l'Autriche à Wagram, près de Vienne."
C_GRAND = "Vers 1811, l'Empire domine une grande partie de l'Europe : des pays sont annexés, d'autres sont dirigés par des frères de Napoléon ou deviennent ses alliés."
C_ARMEE = "La Grande Armée réunit des soldats français et des soldats venus des pays alliés ou conquis."
C_RUSSIE = "En juin 1812, Napoléon envahit la Russie ; en septembre, il entre dans Moscou, mais la ville est incendiée."
C_RETRAITE = "Pendant la retraite, le froid, la faim et les combats font disparaître la plus grande partie de la Grande Armée."
C_ABDIC = "Battu par les pays d'Europe unis contre lui, Napoléon abdique en avril 1814 ; il est exilé sur l'île d'Elbe, en Méditerranée."
C_CENTJ = "En mars 1815, il revient en France et reprend le pouvoir pendant environ cent jours."
C_WATERLOO = "Le 18 juin 1815, il est définitivement battu à Waterloo, en Belgique, par les Britanniques et les Prussiens."
C_HELENE = "Il est exilé sur l'île de Sainte-Hélène, au milieu de l'océan Atlantique, où il meurt le 5 mai 1821."
C_MORTS = "Les guerres de l'Empire ont fait des centaines de milliers de morts en France et dans toute l'Europe."
LECON_CONQUETES = [("Les grandes victoires", [C_AUSTER, C_IENA, C_WAGRAM, C_GRAND, C_ARMEE]),
                   ("La campagne de Russie", [C_RUSSIE, C_RETRAITE]),
                   ("La chute", [C_ABDIC, C_CENTJ, C_WATERLOO, C_HELENE, C_MORTS])]

# ---------------------------------------------------------------- Leçon 4 : ce qui reste de l'Empire
H_BANQUE = "Le 18 janvier 1800, la Banque de France est créée."
H_PREFETS = "Le 17 février 1800, il crée les préfets : dans chaque département, un préfet nommé par le gouvernement fait appliquer ses décisions."
H_LYCEES = "Le 1er mai 1802, une loi crée les lycées, pour former les futurs officiers, ingénieurs et fonctionnaires."
H_LEGION = "Le 19 mai 1802, il crée la Légion d'honneur, une décoration qui récompense les mérites militaires et civils."
H_CODE = "Le 21 mars 1804, le Code civil est promulgué : un seul livre de lois pour toute la France."
H_EGALITE = "Le Code civil garde des idées de la Révolution : l'égalité de tous devant la loi, la liberté de choisir son travail et le droit de propriété."
H_FEMMES = "Mais le Code civil soumet la femme mariée à l'autorité de son mari."
H_OMBRES = "L'Empire est un régime autoritaire : les journaux sont surveillés et censurés, les opposants sont arrêtés."
H_ESCLAV = "En 1802, Bonaparte rétablit l'esclavage dans les colonies françaises ; il ne sera aboli définitivement qu'en 1848."
H_ARC = "En 1806, Napoléon décide la construction de l'Arc de triomphe de l'Étoile pour célébrer la Grande Armée ; il est achevé en 1836."
H_SOLDAT = "Depuis 1921, le Soldat inconnu de la Première Guerre mondiale repose sous l'Arc de triomphe."
H_VENDOME = "À Paris, la colonne Vendôme est recouverte du bronze de canons pris à l'ennemi à Austerlitz."
H_INVAL = "En 1840, les cendres de Napoléon sont ramenées de Sainte-Hélène ; son tombeau est aujourd'hui sous le dôme des Invalides."
LECON_HERITAGE = [("Des institutions qui durent", [H_BANQUE, H_PREFETS, H_LYCEES, H_LEGION]),
                  ("Le Code civil", [H_CODE, H_EGALITE, H_FEMMES]),
                  ("Une part d'ombre", [H_OMBRES, H_ESCLAV]),
                  ("Des monuments", [H_ARC, H_SOLDAT, H_VENDOME, H_INVAL])]

# ---------------------------------------------------------------- Leçon 5 : lieux, symboles et rites de la République
R_ART2 = "La Constitution de 1958, dans son article 2, fixe les symboles de la République : le drapeau tricolore, l'hymne national et la devise."
R_DRAPEAU = "Le drapeau tricolore est bleu, blanc, rouge : il est né pendant la Révolution française."
R_DEVISE = "La devise de la République est « Liberté, Égalité, Fraternité » ; on la lit sur le fronton des mairies et des écoles."
R_MARSEIL = "La Marseillaise est écrite par Rouget de Lisle à Strasbourg en avril 1792 ; elle devient chant national le 14 juillet 1795."
R_MARIANNE = "Marianne, une femme coiffée d'un bonnet phrygien, représente la République : son buste est présent dans de nombreuses mairies."
R_14 = "Le 14 juillet est la fête nationale depuis 1880 : il rappelle la prise de la Bastille, le 14 juillet 1789, et la fête de la Fédération, le 14 juillet 1790."
R_LIEUX = "La mairie, l'école, le Panthéon, l'Assemblée nationale et le palais de l'Élysée sont des lieux de la République."
R_MAIRE = "À la mairie, le maire, qui porte une écharpe tricolore, célèbre les mariages et organise les élections."
R_VOTE = "Voter est un rite républicain : les citoyens choisissent librement leurs représentants."
R_CEREMONIES = "Les cérémonies du 8 Mai et du 11 Novembre, devant le monument aux morts, rappellent les victimes des guerres."
R_LOIS = "Les droits et les libertés sont protégés par des textes comme la Déclaration des droits de l'homme et du citoyen de 1789 et la Constitution de 1958."
LECON_REPUBLIQUE = [("Les symboles", [R_ART2, R_DRAPEAU, R_DEVISE, R_MARSEIL, R_MARIANNE, R_14]),
                    ("Les lieux et les rites", [R_LIEUX, R_MAIRE, R_VOTE, R_CEREMONIES]),
                    ("Des droits protégés", [R_LOIS])]


def html(sections):
    return "".join(f"<h4>{h}</h4><p>{' '.join(ps)}</p>" for h, ps in sections)
