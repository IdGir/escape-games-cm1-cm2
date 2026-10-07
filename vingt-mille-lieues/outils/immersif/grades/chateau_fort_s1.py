"""Salle 1 « La motte et la palissade » (fiche : construire-un-chateau)."""
from aide import *

F = "« Construire un château fort »"
A1 = "À partir du Xe siècle, le pouvoir du roi est faible."
A2 = "Le territoire est morcelé en seigneuries, dirigées par des seigneurs qui protègent, commandent et jugent les habitants."
A3 = "On choisit un site élevé (colline, éperon rocheux) ou l'on crée la hauteur : on creuse un fossé et l'on entasse la terre au centre."
A4 = "La motte porte une tour de bois ; une palissade entoure la basse-cour, où se trouvent les écuries, les réserves et les logements."
A5 = "Rapide à bâtir, la motte craint le feu."
A6 = "Au XIe siècle apparaissent les premiers donjons de pierre ; aux XIIe et XIIIe siècles, les enceintes de pierre flanquées de tours se multiplient."
A7 = "Un château de pierre coûte très cher et demande des années : seuls les seigneurs puissants peuvent se l'offrir."
A8 = "Depuis 1997, à Guédelon (Treigny, dans l'Yonne), des artisans construisent un château sur le modèle de ceux du XIIIe siècle, avec les outils et les matériaux de l'époque, pour comprendre comment on bâtissait."
A9 = "À Guédelon, une dizaine de métiers se côtoient : carriers, tailleurs de pierre, maçons, charpentiers, forgerons, chaufourniers, charretiers, tuiliers."


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Les premiers châteaux forts sont faits surtout de…", ["terre et de bois", "pierre et de marbre", "verre et de métal"], 0, "Une butte de terre, une tour de bois, une palissade.")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Au début, on construit vite, avec ce que l'on trouve.", "Le bois et la terre sont partout."]),
        "lieutenant": vf(
            "Maître Josselin vérifie cinq affirmations sur les débuts des châteaux. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique pourquoi les seigneurs construisent des châteaux.",
            [("À partir du Xe siècle, le pouvoir du roi est faible.", True, "Le territoire est morcelé."), ("Une motte est une butte de terre portant une tour de bois.", True, "Entourée d'une palissade."),
             ("Un château de pierre se construit en quelques semaines.", False, "Il demande des années."), ("La motte craint le feu.", True, "Elle est en bois."),
             ("Tous les seigneurs peuvent se payer un château de pierre.", False, "Seuls les seigneurs puissants le peuvent.")],
            ["Le bois craint le feu ; la pierre, non.", "La pierre coûte cher et demande du temps.", "Pour la justification : cherche la phrase qui parle des seigneuries."],
            J("Quelle phrase de la fiche explique le pouvoir des seigneurs ?", A2, [A1, A5, A7], pos=1)),
        "second": qcm(
            carnet("Notes de Maître Josselin", "(d'après la fiche). Xe siècle : mottes de terre et tours de bois. XIe siècle : premiers donjons de pierre. XIIe-XIIIe siècles : enceintes de pierre flanquées de tours. Depuis 1997 : le chantier de Guédelon.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Combien de siècles séparent les premières mottes des enceintes de pierre du XIIIe siècle ?", ["3 siècles", "1 siècle", "13 siècles", "30 siècles"], 0, "XIIIe moins Xe : 13 − 10 = 3."),
             ("Pourquoi les seigneurs passent-ils peu à peu du bois à la pierre ?", ["La pierre résiste mieux, mais seuls les plus puissants peuvent la payer", "Le roi leur interdit le bois", "La pierre est moins chère", "Le bois n'existe plus"], 0, "La pierre coûte très cher et demande des années."),
             ("Pourquoi les artisans de Guédelon utilisent-ils les outils de l'époque ?", ["Pour comprendre comment on bâtissait", "Parce qu'ils n'ont pas d'autres outils", "Pour aller plus vite", "Parce que c'est interdit autrement"], 0, "C'est un chantier expérimental.")],
            ["Calcule la différence entre les siècles.", "Pense au coût et à la durée du chantier.", "Guédelon sert à comprendre, pas à aller vite."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", A7, [A5, A6, A3], pos=2)),
    }
    d["e1-2"] = {
        "mousse": ordre(
            "Remets les étapes dans l'ordre, de la plus ancienne (en haut) à la plus récente (en bas). Utilise les flèches ▲ et ▼.",
            ["Une butte de terre et une tour de bois (Xe siècle)", "Les premiers donjons de pierre (XIe siècle)", "De grandes enceintes de pierre avec des tours (XIIe-XIIIe siècles)"],
            ["Ouvre la fiche " + F + ".", "Tout commence par la terre et le bois.", "La pierre vient après."]),
        "lieutenant": ordre(
            "Dame Aliénor décrit la construction d'un château de motte. Remets les cinq étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit la motte.",
            ["On choisit un site élevé, ou on crée la hauteur.", "On creuse un fossé et on entasse la terre au centre.", "On élève une tour de bois au sommet de la motte.", "On entoure la basse-cour d'une palissade.", "Plus tard, un seigneur riche remplace le bois par la pierre."],
            ["On prépare le terrain avant de construire.", "Le fossé donne la terre de la butte.", "La pierre vient après le bois."],
            J("Quelle phrase de la fiche décrit la motte et la palissade ?", A4, [A3, A5, A6], pos=0)),
        "second": tri(
            "Josselin classe les châteaux selon leur matériau et leur époque. Range chaque carte dans la bonne colonne, puis choisis la phrase de la fiche qui date les premiers donjons de pierre.",
            [("bois", "Terre et bois (Xe siècle)"), ("pierre", "Pierre (XIe-XIIIe siècles)")],
            [("Une tour de bois sur une butte", "bois"), ("Une palissade de pieux", "bois"), ("Un château qui craint le feu", "bois"), ("Un donjon de pierre", "pierre"), ("Une enceinte flanquée de tours", "pierre"), ("Un château qui coûte très cher et demande des années", "pierre")],
            ["Le bois craint le feu.", "La pierre est chère et longue à travailler.", "Les enceintes de pierre se multiplient aux XIIe et XIIIe siècles."],
            J("Quelle phrase de la fiche date les premiers donjons de pierre ?", A6, [A5, A7, A8], pos=1)),
    }
    d["e1-3"] = {
        "mousse": assoc(
            "Relie chaque métier à son travail. Clique sur un métier, puis sur son travail.",
            [("Le charpentier", "travailler le bois"), ("Le forgeron", "fabriquer des outils en fer"), ("Le maçon", "bâtir les murs")],
            ["Ouvre la fiche " + F + ".", "Le charpentier travaille le bois.", "Le forgeron travaille le fer au feu."]),
        "lieutenant": qcm(
            carnet("Chantier de Guédelon", "(d'après la fiche). On y trouve des carriers, des tailleurs de pierre, des maçons, des charpentiers, des forgerons, des chaufourniers, des charretiers et des tuiliers.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Combien de métiers sont cités dans le document ?", ["8", "4", "10", "12"], 0, "Carrier, tailleur de pierre, maçon, charpentier, forgeron, chaufournier, charretier, tuilier."),
             ("Quel métier transporte les pierres et les matériaux ?", ["Le charretier", "Le carrier", "Le tuilier", "Le forgeron"], 0, "Il conduit la charrette."),
             ("Pourquoi le chantier de Guédelon existe-t-il ?", ["Pour comprendre comment on construisait un château au XIIIe siècle", "Pour loger des touristes", "Pour défendre le pays", "Pour remplacer un château détruit"], 0, "C'est un chantier expérimental.")],
            ["Compte les métiers dans le document.", "Cherche celui qui transporte.", "Le chantier utilise les outils et les matériaux de l'époque."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", A8, [A9, A7, A6], pos=0)),
        "second": assoc(
            "Josselin organise son chantier. Relie chaque artisan à sa tâche précise, puis choisis la phrase de la fiche qui énumère les métiers de Guédelon.",
            [("Le carrier", "sort les blocs de pierre de la carrière"), ("Le tailleur de pierre", "façonne chaque bloc"), ("Le chaufournier", "cuit le calcaire pour faire la chaux"), ("Le tuilier", "fabrique les tuiles du toit"), ("Le charretier", "transporte les matériaux")],
            ["Chacun intervient à une étape différente.", "Le chaufournier travaille avec un four à chaux.", "Le tuilier fabrique la couverture du toit."],
            J("Quelle phrase de la fiche énumère les métiers de Guédelon ?", A9, [A8, A7, A4], pos=2)),
    }
    d["e1-4"] = {
        "lieutenant": trous(
            "Maître Josselin a dicté son carnet, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « pierre ».",
            "À partir du Xe siècle, le pouvoir du [[roi]] est faible et le territoire est partagé en [[seigneuries]]. La motte porte une tour de [[bois]], entourée d'une [[palissade]]. Au XIe siècle apparaissent les premiers donjons de [[pierre]].",
            ["roi", "seigneuries", "bois", "palissade", "pierre", "verre", "marbre", "brique", "papier"],
            ["Relis les deux premiers paragraphes de la fiche.", "Le bois craint le feu.", "Les châteaux de pierre sont chers."],
            J("Quelle phrase de la fiche justifie le mot « pierre » ?", A6, [A5, A3, A8], pos=1)),
        "second": trous(
            "Josselin résume l'histoire du château fort, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « puissants ».",
            "Les mottes du Xe siècle sont rapides à bâtir, mais elles craignent le [[feu]]. Un château de pierre coûte très [[cher]] et demande des [[années]] : seuls les seigneurs [[puissants]] peuvent se l'offrir. Aujourd'hui, à [[Guédelon]], on bâtit un château comme au XIIIe siècle.",
            ["feu", "cher", "années", "puissants", "Guédelon", "gratuit", "minutes", "pauvres", "Versailles"],
            ["Les mots viennent de la partie « Du bois à la pierre ».", "Un chantier de pierre prend du temps.", "Guédelon est dans l'Yonne."],
            J("Quelle phrase de la fiche justifie le mot « puissants » ?", A7, [A5, A6, A8], pos=1)),
    }
    return d
