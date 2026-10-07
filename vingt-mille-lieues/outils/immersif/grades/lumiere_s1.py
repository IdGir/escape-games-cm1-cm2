"""Salle 1 « La lanterne du phare » : grades mousse, lieutenant, second (fiche : sources)."""
from aide import *

FICHE = "« D'où vient la lumière ? Comment voyage-t-elle ? »"


def donnees(svg, bloc=None):
    d = {}
    # ---------------------------------------------------------------- e1-1 : sources et objets éclairés
    d["e1-1"] = {
        "mousse": tri(
            "Maëlle range sa liste. Range chaque carte : elle produit sa lumière, ou elle renvoie celle d'un autre.",
            [("source", "Elle produit sa lumière"), ("eclaire", "Elle renvoie la lumière")],
            [("le Soleil", "source"), ("une bougie allumée", "source"), ("la Lune", "eclaire"), ("un livre", "eclaire")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Dans le noir complet, un livre ne se voit pas.",
             "La Lune brille la nuit parce que le Soleil l'éclaire."]),
        "lieutenant": tri(
            "Maëlle a dressé la liste de ce qu'elle voit depuis la lanterne. Classe les dix éléments, puis choisis la phrase de la fiche qui prouve que la Lune n'est pas une source de lumière.",
            [("source", "Source de lumière"), ("eclaire", "Objet éclairé")],
            [("une étoile", "source"), ("la flamme d'une bougie", "source"), ("l'écran allumé d'une tablette", "source"),
             ("la lampe du phare, allumée", "source"), ("la Lune", "eclaire"), ("une lampe éteinte", "eclaire"),
             ("un miroir", "eclaire"), ("la page d'un livre", "eclaire"), ("la voile d'un bateau", "eclaire"),
             ("le sol de la jetée", "eclaire")],
            ["Dans une pièce noire, un objet éclairé ne se voit plus ; une source, si.", "Une lampe éteinte ne produit plus rien.",
             "Pour la justification : cherche la phrase qui parle de la Lune elle-même."],
            J("Quelle phrase de la fiche prouve que la Lune n'est pas une source de lumière ?",
              "La Lune brille la nuit, mais elle ne fait que renvoyer la lumière du Soleil.",
              ["Une lampe éteinte, elle, n'est plus une source.",
               "Une source de lumière produit sa propre lumière : le Soleil et les autres étoiles, une flamme, une lampe ou un écran allumés.",
               "Dans l'air, la lumière se propage en ligne droite, très vite."], pos=2)),
        "second": qcm(
            "<div class='doc-carnet'><b>Carnet de Maëlle</b> (relevé inventé pour le jeu). Dans une pièce sans fenêtre, tout est éteint : on ne voit aucun des objets posés sur la table. On allume la bougie : on voit alors la bougie, mais aussi le miroir et le livre. On éteint la bougie : tout redevient invisible.</div>Réponds aux trois questions à partir du carnet et de la fiche.",
            [("Quel objet de la table est une source de lumière ?", ["La bougie allumée", "Le miroir", "Le livre", "La table"], 0,
              "Seule la bougie produit sa lumière."),
             ("Pourquoi voit-on le livre quand la bougie est allumée ?", [
                 "Parce que la lumière de la bougie arrive sur le livre, qui en renvoie une partie vers nos yeux",
                 "Parce que le livre produit de la lumière quand il y a une bougie",
                 "Parce que nos yeux envoient de la lumière vers le livre",
                 "Parce que la bougie rend le livre brillant pour toujours"], 0, "On voit un objet quand sa lumière entre dans l'œil."),
             ("Après avoir éteint la bougie, que devient la bougie ?", [
                 "Un objet éclairé, comme les autres, mais plus éclairé du tout",
                 "Une source de lumière qu'on ne voit plus",
                 "Un objet transparent",
                 "Une source qui continue de produire de la lumière"], 0, "Éteinte, elle ne produit plus rien : ce n'est plus une source.")],
            ["Compare le noir complet et la pièce éclairée par la bougie.", "Un objet éclairé n'est visible que s'il reçoit de la lumière d'une source.",
             "L'œil reçoit la lumière : il n'en envoie pas."],
            J("Quelle phrase de la fiche explique ta réponse à la question 2 ?",
              "On voit un objet quand la lumière qu'il produit ou qu'il renvoie entre dans notre œil.",
              ["Une lampe éteinte, elle, n'est plus une source.", "Un phare, un feu tricolore, une lampe qui clignote en Morse envoient des signaux lumineux.",
               "La Lune brille la nuit, mais elle ne fait que renvoyer la lumière du Soleil."], pos=1)),
    }
    # ---------------------------------------------------------------- e1-2 : le trajet de la lumière
    d["e1-2"] = {
        "mousse": assoc(
            "Pour voir la voile du bateau, la lumière fait un voyage. Regarde le schéma, puis relie chaque élément à son rôle. Clique sur un élément, puis sur son rôle.\n" + svg("e1-2", "matelot"),
            [("la lampe du phare", "elle produit la lumière"), ("la voile du bateau", "elle renvoie la lumière"),
             ("l'œil de la gardienne", "il reçoit la lumière")],
            ["Ouvre la fiche " + FICHE + " : cherche « Comment voit-on ? ».", "Le voyage de la lumière commence à la lampe.",
             "L'œil est la fin du voyage : il reçoit."]),
        "lieutenant": plan_l1_2(svg),
        "second": ordre(
            "Maëlle écrit le trajet de la lumière pour que la gardienne voie la voile du bateau, la nuit. Les étapes sont mélangées : remets-les dans l'ordre (utilise les flèches ▲ et ▼), puis choisis la phrase de la fiche qui justifie le début du trajet.",
            ["La lampe du phare produit de la lumière.",
             "La lumière voyage en ligne droite de la lampe jusqu'à la voile.",
             "La voile renvoie une partie de la lumière qu'elle reçoit.",
             "La lumière renvoyée voyage en ligne droite de la voile jusqu'à l'œil.",
             "L'œil reçoit la lumière : la gardienne voit la voile."],
            ["Une étape produit la lumière, une autre la renvoie, une autre la reçoit.", "La voile ne produit rien : elle ne peut pas venir avant la lampe.",
             "Le voyage se termine dans l'œil."],
            J("Quelle phrase de la fiche prouve que la voile n'envoie de la lumière vers l'œil que si la lampe l'éclaire ?",
              "Tous les autres objets sont des objets éclairés : ils renvoient une partie de la lumière qu'ils reçoivent.",
              ["L'œil reçoit la lumière, il n'en envoie pas.", "Dans l'air, la lumière se propage en ligne droite, très vite : environ 300 000 km par seconde."], pos=0)),
    }
    # ---------------------------------------------------------------- e1-3 : signaux
    d["e1-3"] = {
        "mousse": intrus(
            "La lumière sert aussi à envoyer des messages. Trois objets envoient un signal lumineux. Trouve celui qui n'en envoie pas, puis vérifie.",
            [("Le phare et ses éclats", False), ("Les feux rouges d'une voiture", False), ("La lampe qui clignote en Morse", False),
             ("Le sifflet d'un arbitre", True)],
            ["Un signal lumineux se voit avec les yeux.", "Un des objets s'entend au lieu de se voir.", "Ouvre la fiche " + FICHE + " : cherche « La lumière transmet des messages »."]),
        "lieutenant": intrus(
            "Quatre objets transmettent une information grâce à la lumière. Un seul n'utilise pas la lumière. Trouve l'intrus, puis choisis la phrase de la fiche qui prouve que le phare transmet une information.",
            [("Le rythme d'éclats d'un phare", False), ("Le feu rouge d'un passage à niveau", False),
             ("La lampe à signaux d'un bateau", False), ("Le voyant d'un chargeur de téléphone", False),
             ("La sirène du port", True)],
            ["Quatre objets se voient ; un seul s'entend.", "Un voyant est une petite lampe qui renseigne.", "Pour la justification : cherche la phrase qui parle du rythme d'éclats."],
            J("Quelle phrase de la fiche prouve qu'un phare transmet une information ?",
              "Chaque phare a son propre rythme d'éclats : la nuit, les marins le reconnaissent.",
              ["Un phare, un feu tricolore, une lampe qui clignote en Morse envoient des signaux lumineux.",
               "On le voit quand le faisceau d'un phare traverse la brume.", "Dans l'air, la lumière se propage en ligne droite."], pos=0)),
        "second": vf(
            "Maëlle a noté six affirmations sur les signaux lumineux et le code Morse. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui permet de contrôler l'affirmation sur la lettre N.",
            [("Un phare transmet une information : son rythme d'éclats permet de le reconnaître.", True, "Chaque phare a son rythme."),
             ("Le code Morse n'utilise que des éclats longs.", False, "Il utilise des éclats courts et des éclats longs."),
             ("En Morse, la lettre E s'écrit avec un seul éclat long.", False, "E s'écrit avec un seul éclat court : •."),
             ("En Morse, la lettre N s'écrit — • (un éclat long, puis un éclat court).", True, "N = —•."),
             ("Le signal SOS s'écrit ••• ——— •••.", True, "S = •••, O = ———."),
             ("Le code Morse ne peut être envoyé qu'avec des sons.", False, "Une lampe à signaux envoie aussi des éclats.")],
            ["Un éclat court se note •, un éclat long se note —.", "Compare chaque lettre avec la liste d'exemples de la fiche.", "SOS est fait de deux fois trois éclats courts autour de trois éclats longs."],
            J("Quelle phrase de la fiche permet de contrôler l'affirmation sur la lettre N ?",
              "Exemples : E = •, I = ••, L = •—••, N = —•, U = ••—, S = •••, O = ———.",
              ["Le signal de détresse SOS s'écrit ••• ——— •••.", "Avec le code Morse, une lampe envoie des éclats courts et longs qui forment des lettres.",
               "Chaque phare a son propre rythme d'éclats : la nuit, les marins le reconnaissent."], pos=2)),
    }
    # ---------------------------------------------------------------- e1-4 : questions de la gardienne (timonier, lieutenant, second)
    d["e1-4"] = {
        "lieutenant": qcm(
            "<div class='doc-carnet'><b>Carnet de Maëlle</b> (scène inventée). La nuit, depuis la jetée, Maëlle voit la voile blanche d'un bateau éclairée par la lampe du phare. Elle place un grand carton noir entre la lampe et la voile.</div>Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie ta réponse à la question 1.",
            [("Que voit Maëlle quand le carton cache la lampe à la voile ?", [
                "La voile n'est plus visible, car elle ne reçoit plus la lumière du phare", "La voile brille plus fort", "La voile est visible, mais plus petite",
                "La voile produit sa propre lumière"], 0, "Sans lumière reçue, un objet éclairé ne renvoie rien."),
             ("Quelle est la source de lumière dans cette scène ?", ["La lampe du phare", "La voile blanche", "Le carton noir", "L'œil de Maëlle"], 0, "Seule la lampe produit de la lumière."),
             ("Le carton noir est…", ["opaque", "transparent", "translucide", "une source de lumière"], 0, "Il arrête toute la lumière.")],
            ["Une voile éclairée renvoie la lumière qu'elle reçoit.", "Le carton arrête la lumière : elle n'arrive plus à la voile.", "Le carton ne laisse passer aucune lumière."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?",
              "On voit un objet quand la lumière qu'il produit ou qu'il renvoie entre dans notre œil.",
              ["Dans l'air, la lumière se propage en ligne droite.", "Une lampe éteinte, elle, n'est plus une source.",
               "Un phare, un feu tricolore, une lampe qui clignote en Morse envoient des signaux lumineux."], pos=0)),
        "second": qcm(
            "<div class='doc-carnet'><b>Données du phare</b> (valeurs arrondies). Vitesse de la lumière dans l'air : environ 300 000 km par seconde. Le Soleil est à environ 150 millions de km de la Terre. Un bateau est à 30 km du phare.</div>Réponds aux trois questions, puis choisis la phrase de la fiche qui donne la vitesse de la lumière.",
            [("Combien de temps la lumière du phare met-elle pour atteindre le bateau, à 30 km ?", ["environ 0,0001 seconde", "environ 1 seconde", "environ 10 secondes", "environ 1 minute"], 0,
              "30 km ÷ 300 000 km/s = 0,0001 s."),
             ("Combien de temps la lumière du Soleil met-elle pour arriver sur la Terre ?", ["environ 8 minutes", "environ 8 secondes", "environ 8 heures", "elle arrive instantanément"], 0,
              "150 000 000 ÷ 300 000 = 500 s, soit environ 8 minutes."),
             ("Un rocher opaque se trouve en ligne droite entre le phare et le bateau. Que voit le bateau ?", [
                 "Le feu du phare est caché, car la lumière ne contourne pas le rocher", "Le feu du phare est plus brillant", "Le feu du phare est visible, car la lumière contourne le rocher",
                 "Le feu du phare est visible mais plus petit"], 0, "La lumière se propage en ligne droite.")],
            ["Distance ÷ vitesse = durée.", "Passe de 150 millions à 150 000 000 pour calculer : 500 secondes, ce n'est pas 8 secondes.", "Pas de courbe : la lumière va en ligne droite."],
            J("Quelle phrase de la fiche donne la vitesse de la lumière dans l'air ?",
              "Dans l'air, la lumière se propage en ligne droite, très vite : environ 300 000 km par seconde.",
              ["On voit un objet quand la lumière qu'il produit ou qu'il renvoie entre dans notre œil.", "Sur un schéma, on dessine un rayon de lumière par un trait droit muni d'une flèche.",
               "Chaque phare a son propre rythme d'éclats."], pos=1)),
    }
    return d


def plan_l1_2(svg):
    figure = svg("e1-2", "timonier")
    b = _plan_l12(figure)
    return b


def _plan_l12(figure):
    """Plan à 4 repères sur le schéma du phare (les repères 1 à 4 sont ceux du grade timonier)."""
    b = {
        "type": "plan", "titre": "Le trajet de la lumière", "colonnes": 2,
        "cases": [{"libelle": "Repère 1", "reponse": "source : elle produit la lumière"},
                  {"libelle": "Repère 2", "reponse": "objet éclairé : il renvoie la lumière vers l'œil"},
                  {"libelle": "Repère 3", "reponse": "récepteur : l'œil reçoit la lumière"},
                  {"libelle": "Repère 4", "reponse": "premier trajet : de la lampe à la voile"}],
        "etiquettes": ["source : elle produit la lumière", "objet éclairé : il renvoie la lumière vers l'œil", "récepteur : l'œil reçoit la lumière",
                       "premier trajet : de la lampe à la voile", "premier trajet : de l'œil à la voile", "second trajet : de la voile à la lampe"],
        "consigne": "Maëlle a schématisé le voyage de la lumière entre le phare, la voile et son œil. Place chaque étiquette sur le bon repère. Deux étiquettes décrivent des trajets qui n'existent pas. Puis choisis la phrase de la fiche qui justifie le repère 4." + figure,
        "indices": ["Le repère 4 est posé sur un trait droit, entre la lampe et la voile.", "La flèche donne le sens du trajet : de la lampe vers la voile.",
                    "L'œil ne lance pas de rayons : il reçoit."],
        "justification": J("Quelle phrase de la fiche justifie le sens du premier trajet ?",
                           "Pour voir la voile d'un bateau la nuit, la lumière fait donc deux trajets : de la lampe du phare à la voile, puis de la voile à l'œil.",
                           ["L'œil reçoit la lumière, il n'en envoie pas.", "Dans l'air, la lumière se propage en ligne droite, très vite.",
                            "Un phare, un feu tricolore, une lampe qui clignote en Morse envoient des signaux lumineux."], pos=1),
    }
    return b
