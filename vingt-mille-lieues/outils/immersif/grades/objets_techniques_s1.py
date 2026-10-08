"""Salle 1 « L'entrée de l'atelier » (fiche : besoin-fonction)."""
from aide import *

F = "« À quoi sert un objet ? »"
B1 = "Un objet technique est conçu et fabriqué par l'être humain pour répondre à un besoin."
B2 = "Un galet ramassé dans la rivière n'est pas un objet technique ; un parapluie en est un."
B3 = "La fonction d'usage décrit ce que l'objet permet de faire, avec un verbe d'action : la lampe torche permet d'éclairer loin d'une prise."
B4 = "La fonction d'estime explique pourquoi on préfère un modèle à un autre : couleur, forme, marque, décoration."
B5 = "Quand les besoins changent, les objets changent."
B6 = "Une bougie et une lampe torche répondent au même besoin, éclairer, avec des solutions très différentes. On dit qu'elles ont la même fonction d'usage."


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": assoc(
            "Zoé range ses objets. Relie chaque objet au besoin auquel il répond. Clique sur un objet, puis sur son besoin.",
            [("Une lampe torche", "éclairer quand il fait sombre"), ("Un ouvre-boîte", "ouvrir une conserve"), ("Un cartable", "transporter ses affaires")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Demande-toi : « à quoi ça sert ? »", "Le cartable sert à transporter."]),
        "lieutenant": vf(
            "Awa vérifie cinq affirmations sur les objets techniques. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui définit un objet technique.",
            [("Un objet technique est fabriqué par l'être humain pour répondre à un besoin.", True, "C'est la définition."), ("Un galet ramassé dans la rivière est un objet technique.", False, "Il n'est pas fabriqué."),
             ("Un parapluie est un objet technique.", True, "Il répond au besoin de se protéger de la pluie."), ("Quand les besoins changent, les objets restent identiques.", False, "Les objets évoluent."),
             ("La fonction d'usage se dit avec un verbe d'action.", True, "Par exemple : éclairer.")],
            ["Un objet technique est conçu et fabriqué.", "Un galet est naturel.", "Pour la justification : cherche la phrase qui parle de besoin."],
            J("Quelle phrase de la fiche définit un objet technique ?", B1, [B2, B3, B5], pos=2)),
        "second": qcm(
            carnet("Atelier d'Éléonore", "(inventé pour le jeu). Trois objets : un galet poli par la rivière, une lampe torche, une bougie. Éléonore se demande lesquels sont des objets techniques et lesquels répondent au même besoin.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Lequel n'est pas un objet technique ?", ["Le galet", "La lampe torche", "La bougie", "Les trois"], 0, "Le galet n'est pas fabriqué."),
             ("Quelle est la fonction d'usage de la lampe torche ?", ["Éclairer, loin d'une prise", "Être jolie", "Être achetée", "Faire du bruit"], 0, "Elle permet d'éclairer."),
             ("La bougie et la lampe torche ont-elles la même fonction d'usage ?", ["Oui : elles répondent au même besoin, éclairer", "Non : l'une est en cire", "Non : l'une est plus chère", "On ne peut pas savoir"], 0, "Même besoin, solutions différentes.")],
            ["Un objet technique est fabriqué.", "La fonction d'usage se dit avec un verbe.", "Même besoin, solutions différentes."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", B6, [B4, B1, B5], pos=1)),
    }
    d["e1-2"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("La fonction d'usage d'un objet, c'est…", ["ce à quoi il sert", "sa couleur préférée", "son prix"], 0, "Elle dit à quoi l'objet sert.")],
            ["Ouvre la fiche " + F + ".", "« Usage » : l'usage qu'on en fait.", "La couleur ne dit pas à quoi l'objet sert."]),
        "lieutenant": tri(
            "Zoé trie des phrases sur une trousse, un vélo et une lampe. Range chaque phrase : fonction d'usage ou fonction d'estime ? Puis choisis la phrase de la fiche qui définit la fonction d'estime.",
            [("usage", "Fonction d'usage"), ("estime", "Fonction d'estime")],
            [("La trousse range les crayons", "usage"), ("Le vélo permet de se déplacer", "usage"), ("La lampe éclaire à dix mètres", "usage"),
             ("La trousse est de ma couleur préférée", "estime"), ("Le vélo porte une marque connue", "estime"), ("La lampe a un boîtier brillant", "estime")],
            ["L'usage décrit ce que l'objet fait.", "L'estime parle de couleur, de forme, de marque.", "Un verbe d'action : usage."],
            J("Quelle phrase de la fiche définit la fonction d'estime ?", B4, [B3, B1, B6], pos=2)),
        "second": tri(
            "Zoé classe des objets. Range chaque carte dans la bonne colonne, puis choisis la phrase de la fiche qui explique pourquoi une bougie et une lampe torche ont la même fonction d'usage.",
            [("technique", "Objet technique"), ("naturel", "Pas un objet technique")],
            [("Un parapluie", "technique"), ("Une lampe torche", "technique"), ("Un cartable", "technique"), ("Un galet de rivière", "naturel"), ("Une branche tombée", "naturel"), ("Un caillou ramassé", "naturel")],
            ["Un objet technique est fabriqué.", "Un galet n'est pas fabriqué.", "Une branche tombée est naturelle."],
            J("Quelle phrase de la fiche explique pourquoi une bougie et une lampe torche ont la même fonction d'usage ?", B6, [B2, B5, B3], pos=2)),
    }
    d["e1-3"] = {
        "mousse": tri(
            "Range chaque phrase dans la bonne colonne : ce que l'objet fait, ou ce qui le rend joli. Clique sur une carte, puis sur une colonne.",
            [("usage", "Fonction d'usage"), ("estime", "Fonction d'estime")],
            [("La lampe éclaire le chemin", "usage"), ("Le cartable porte les cahiers", "usage"), ("La lampe est de ma couleur préférée", "estime"), ("Le cartable est à la mode", "estime")],
            ["Ouvre la fiche " + F + ".", "Ce que l'objet fait : usage.", "Ce qui plaît : estime."]),
        "lieutenant": qcm(
            carnet("Besoin de Zoé", "(inventé pour le jeu). Zoé veut un objet qui permette de se repérer dans la cave, sans prise de courant. Elle hésite entre une bougie et une lampe torche, puis choisit la lampe, qu'elle trouve plus jolie.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Quel est le besoin de Zoé ?", ["Éclairer dans la cave sans prise", "Décorer la cave", "Acheter une lampe", "Faire du feu"], 0, "Un besoin se dit avec un verbe."),
             ("Pourquoi la lampe répond-elle à ce besoin ?", ["Elle permet d'éclairer loin d'une prise", "Elle est jaune", "Elle est chère", "Elle est lourde"], 0, "C'est sa fonction d'usage."),
             ("Pourquoi Zoé préfère-t-elle la lampe pour la couleur ?", ["C'est la fonction d'estime", "C'est la fonction d'usage", "C'est un besoin", "C'est une panne"], 0, "Couleur, forme, marque, décoration.")],
            ["Le besoin dit ce qui manque.", "La fonction d'usage dit à quoi sert l'objet.", "La couleur relève de l'estime."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", B4, [B3, B6, B1], pos=0)),
        "second": vf(
            "Zoé a noté six phrases sur les besoins et les objets. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui parle de l'évolution des objets.",
            [("Les objets évoluent quand les besoins changent.", True, "Les objets changent."), ("Un objet peut répondre à un besoin sans être fabriqué.", False, "Un objet technique est fabriqué."),
             ("La bougie et la lampe torche ont la même fonction d'usage.", True, "Elles servent à éclairer."), ("La couleur d'un objet est sa fonction d'usage.", False, "C'est la fonction d'estime."),
             ("Un besoin dit ce qui manque.", True, "On voudrait pouvoir faire quelque chose."), ("La lampe torche permet d'éclairer seulement près d'une prise.", False, "Elle éclaire loin d'une prise.")],
            ["La fonction d'usage dit ce que l'objet permet de faire.", "Les objets évoluent.", "La lampe torche n'a pas besoin de prise."],
            J("Quelle phrase de la fiche parle de l'évolution des objets ?", B5, [B1, B4, B6], pos=2)),
    }
    d["e1-4"] = {
        "lieutenant": lettres(
            "Trouve le mot qui correspond à cette définition : « Fonction qui dit à quoi sert l'objet. » Ses lettres sont cachées en couleur dans le carnet de Zoé, dans le désordre. Clique-les dans l'ordre qui forme le mot (5 lettres). Deux lettres sont des pièges.",
            ["U", "S", "A", "G", "E"],
            marque("Zoé écrit dans son carnet : « Mon cartable ran[g]e mes cahiers. [E]t ma lampe, elle éclaire la cave. Ma [s]alopette a des poches pour mes outils. Papa dit qu'il faut savoir à quoi sert chaque chose avant de l'utiliser. [U]ne règle. [A]ppliquer. Le [p]lus important : [t]outes les questions ! »"),
            ["Le mot a cinq lettres.", "Il commence par U.", "Il se termine par E : fonction d'..."],
            J("Quelle phrase de la fiche cite ce mot ?", B3, [B4, B1, B6], pos=1)),
        "second": lettres(
            "Trouve le mot qui correspond à cette définition : « Fonction qui explique pourquoi on préfère un modèle à un autre : couleur, forme, marque. » Ses lettres sont cachées en couleur dans le carnet de Zoé, dans le désordre. Clique-les dans l'ordre qui forme le mot (6 lettres). Deux lettres sont des pièges.",
            ["E", "S", "T", "I", "M", "E"],
            marque("Dans mon carnet, je note : « J'aime ce vélo, il est [e]xcellent. Ce modèle a une [m]arque connue. Ma cousine [i]nsiste : elle veut le même, en bleu. [s]a couleur, c'est le plus important pour elle. [E]n revanche, moi, je regarde aussi ce qu'il permet de faire. Ça [t]ient la route ! [p]uis je le garde. [a]llez, on y va. »"),
            ["Le mot a six lettres.", "Il commence par E et finit par E.", "Fonction d'..."],
            J("Quelle phrase de la fiche définit ce mot ?", B4, [B3, B6, B1], pos=2)),
    }
    return d
