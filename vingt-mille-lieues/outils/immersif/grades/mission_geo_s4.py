"""Séance 4 « Besançon, travailler en ville » : grades mousse, lieutenant, second (fiche : Travailler en ville : les trois secteurs)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *

FICHE = "« Travailler en ville : les trois secteurs »"


def L(c):
    return f"<b data-l='{c.upper()}'>{c}</b>"


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": assoc(
            "Zoé rencontre trois personnes. Relie chaque métier à ce que fait la personne.",
            [("le boulanger", "il fabrique le pain"), ("l'infirmière", "elle soigne les malades"), ("le caissier", "il encaisse les achats")],
            ["Ouvre la fiche " + FICHE + ".", "Le pain sort du four du boulanger.", "La caisse est au bout du magasin."]),
        "lieutenant": lettres(
            "La source a laissé un message codé : le nom de son métier (11 lettres) est caché dans les lettres en couleur. Écris-le, puis choisis la phrase de la fiche qui classe ce métier dans un secteur.",
            "AMBULANCIER",
            f"Rendez-vous ce soir. Je passe par le {L('c')}ouloir de l'{L('a')}ccueil, après ma {L('n')}uit à l'{L('i')}nfirmerie. Je pousse le {L('b')}rancard jusqu'à l'{L('e')}ntrée des "
            f"{L('u')}rgences, je refais le {L('l')}it, je salue le {L('m')}édecin de {L('r')}adiologie, j'{L('a')}nnonce mon départ et je quitte l'hôp{L('i')}tal par le {L('p')}ortail. Bon {L('t')}rajet !",
            ["Ce métier conduit des malades à l'hôpital.", "Il commence par A et finit par R.", "Pour la justification : cherche « rend des services »."],
            J("Quelle phrase de la fiche montre que ce métier appartient au secteur tertiaire ?", V_TERTIAIRE, [V_SECONDAIRE, V_PRIMAIRE, V_ESPACES], pos=2)),
        "second": qcm(
            "Zoé teste les agents avec des métiers piégés. Choisis le bon secteur, puis la phrase de la fiche qui définit le secteur primaire.",
            [("Un pêcheur qui ramène des poissons au port travaille dans le secteur…", ["primaire", "secondaire", "tertiaire", "quaternaire"], 0, "Il exploite une ressource de la nature."),
             ("Une boulangère qui fabrique son pain travaille dans le secteur…", ["primaire", "secondaire", "tertiaire", "aucun"], 1, "Elle transforme la farine."),
             ("Un conducteur de tramway travaille dans le secteur…", ["primaire", "secondaire", "tertiaire", "aucun"], 2, "Il transporte des voyageurs : c'est un service."),
             ("Un bûcheron qui abat des arbres travaille dans le secteur…", ["primaire", "secondaire", "tertiaire", "aucun"], 0, "Il exploite la forêt.")],
            ["Exploiter la nature, transformer, ou rendre un service ?", "Transporter des personnes, c'est un service.", "Pour la justification : cherche « ressources de la nature »."],
            J("Quelle phrase de la fiche définit le secteur primaire ?", V_PRIMAIRE, [V_TERTIAIRE, V_SECONDAIRE, V_1911], pos=0)),
    }
    d["e4-2"] = {
        "mousse": tri(
            "Range chaque métier dans son secteur.",
            [("p", "Primaire : la nature"), ("s", "Secondaire : fabriquer"), ("t", "Tertiaire : rendre un service")],
            [("l'agriculteur", "p"), ("le boulanger", "s"), ("l'infirmier", "t")],
            ["Ouvre la fiche " + FICHE + ".", "L'agriculteur cultive la terre.", "L'infirmier soigne : c'est un service."]),
        "lieutenant": tri(
            "Range ces douze métiers dans leur secteur, puis choisis la phrase de la fiche qui définit le secteur secondaire.",
            [("p", "Primaire"), ("s", "Secondaire"), ("t", "Tertiaire")],
            [("agriculteur", "p"), ("pêcheur", "p"), ("bûcheron", "p"), ("soudeur", "s"), ("maçon", "s"), ("boulanger", "s"), ("ouvrier d'usine", "s"),
             ("caissier", "t"), ("infirmier", "t"), ("guide", "t"), ("magasinier", "t"), ("consultant", "t")],
            ["Le maçon construit : il transforme des matériaux.", "Le magasinier range des marchandises : c'est un service.", "Pour la justification : cherche « transforme »."],
            J("Quelle phrase de la fiche définit le secteur secondaire ?", V_SECONDAIRE, [V_PRIMAIRE, V_TERTIAIRE, V_2024], pos=1)),
        "second": tri(
            "Zoé a noté les métiers croisés dans la journée. Range-les, puis choisis la phrase de la fiche qui définit le secteur tertiaire.",
            [("p", "Primaire"), ("s", "Secondaire"), ("t", "Tertiaire")],
            [("éleveuse de vaches laitières", "p"), ("fromager qui fabrique le comté", "s"), ("horlogère qui assemble des montres", "s"),
             ("pédiatre", "t"), ("ambulancier", "t"), ("serveuse", "t"), ("conductrice de tramway", "t"), ("bûcheron", "p")],
            ["Le fromager transforme le lait.", "Assembler des montres, c'est fabriquer.", "Pour la justification : cherche « rend des services »."],
            J("Quelle phrase de la fiche définit le secteur tertiaire ?", V_TERTIAIRE, [V_SECONDAIRE, V_ESPACES, V_VILLE], pos=3)),
    }
    d["e4-3"] = {
        "mousse": qcm(
            "La source pose une question.",
            [("Aujourd'hui, la plupart des Français travaillent…", ["en rendant des services", "dans les champs", "dans les mines"], 0, "Plus de 3 emplois sur 4.")],
            ["Ouvre la fiche " + FICHE + ".", "Pense aux métiers de la ville : vendeur, infirmier, serveur.", "Ce sont des services."]),
        "lieutenant": code(
            "La source montre un document : « En 1911, près de 40 % des actifs travaillaient dans l'agriculture. En 2024, le tertiaire regroupe 76,6 % des emplois et l'agriculture 2,3 %. » Arrondis à l'unité, puis choisis la phrase de la fiche sur 1911.",
            [("Sur 100 emplois de 2024, combien dans le tertiaire (arrondi) ?", "77", 2), ("Sur 100 actifs de 1911, combien dans l'agriculture (environ) ?", "40", 2),
             ("De combien de points la part de l'agriculture a-t-elle baissé (40 − 2,3, arrondi) ?", "38", 2)],
            ["76,6 s'arrondit à 77.", "40 − 2,3 = 37,7.", "37,7 s'arrondit à 38. Pour la justification : cherche « 1911 »."],
            J("Quelle phrase de la fiche parle de l'année 1911 ?", V_1911, [V_2024, V_PRIMAIRE, V_BESANCON], pos=0)),
        "second": ordre(
            "La source teste les agents : range ces secteurs du plus grand au plus petit nombre d'emplois en 2024 (Insee), puis choisis la phrase de la fiche qui donne la répartition.",
            [("le tertiaire", "76,6 % des emplois"), ("l'industrie", "12,6 %"), ("la construction", "6,6 %"), ("l'agriculture", "2,3 %")],
            ["Compare les pourcentages.", "L'industrie et la construction forment ensemble le secondaire.", "Pour la justification : cherche « 3 emplois sur 4 »."],
            J("Quelle phrase de la fiche donne la répartition des emplois en 2024 ?", V_2024, [V_1911, V_TERTIAIRE, V_VILLE], pos=2)),
    }
    d["e4-4"] = {
        "lieutenant": assoc(
            "Relie chaque espace de la ville à ce que l'on y trouve, puis choisis la phrase de la fiche qui décrit les espaces de la ville.",
            [("le centre-ville", "des commerces, des administrations et des monuments"), ("le quartier d'affaires", "des bureaux et des entreprises"),
             ("le CHU", "un grand hôpital"), ("le centre commercial", "de grands magasins en périphérie, avec des parkings"),
             ("le parc technologique", "des entreprises de recherche")],
            ["Le centre commercial est souvent au bord des grandes routes.", "CHU : centre hospitalier universitaire.", "Pour la justification : cherche « en périphérie »."],
            J("Quelle phrase de la fiche décrit les espaces de la ville ?", V_ESPACES, [V_VILLE, V_BESANCON, V_TERTIAIRE], pos=1)),
        "second": vf(
            "Zoé rédige son rapport sur Besançon. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur Besançon.",
            [("Besançon est la préfecture du Doubs.", True, "Le Doubs est aussi le nom de la rivière."),
             ("La vieille ville de Besançon est entourée par une boucle de la rivière.", True, "C'est la boucle du Doubs."),
             ("En ville, la densité de population est faible.", False, "Elle est forte."),
             ("Les centres commerciaux sont le plus souvent au cœur de la vieille ville.", False, "Ils sont surtout en périphérie."),
             ("En ville, la plupart des emplois sont dans le secteur tertiaire.", True, "Commerces, hôpital, bureaux, transports.")],
            ["Besançon et la rivière portent des noms différents.", "La périphérie, c'est le bord de la ville.", "Pour la justification : cherche « boucle »."],
            J("Quelle phrase de la fiche décrit Besançon ?", V_BESANCON, [V_VILLE, V_ESPACES, V_2024], pos=3)),
    }
    return d
