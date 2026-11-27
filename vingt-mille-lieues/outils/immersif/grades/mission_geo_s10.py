"""Séance 10 « Les produits consommés » : grades mousse, lieutenant, second (fiche : Produits agricoles et produits transformés)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *
import schemas as S

FICHE = "« Produits agricoles et produits transformés »"
PLATEAU = [("Pomme", "agri"), ("Haricots verts", "agri"), ("Carottes", "agri"), ("Poulet", "agri"), ("Salade", "agri"), ("Yaourt", "trans"), ("Pain", "trans"), ("Cookie", "trans")]


def donnees(svg, bloc=None):
    d = {}
    d["e10-1"] = {
        "mousse": tri(
            "Camille te montre le plateau du jour. Range chaque aliment : vient-il directement de la nature, ou a-t-il été fabriqué ?",
            [("agri", "Produits agricoles"), ("trans", "Produits transformés")], PLATEAU,
            ["Ouvre la fiche " + FICHE + ".", "Une pomme se cueille sur un arbre.", "Il y a cinq produits agricoles et trois produits transformés."]),
        "lieutenant": tri(
            "Camille prépare ses commandes. Range chaque produit, puis choisis la phrase de la fiche qui définit un produit transformé.",
            [("agri", "Produits agricoles"), ("trans", "Produits transformés")],
            [("un œuf", "agri"), ("une carotte", "agri"), ("du lait", "agri"), ("du blé", "agri"), ("du pain", "trans"), ("du fromage", "trans"), ("du chocolat", "trans"), ("du sucre", "trans")],
            ["Le pain est fabriqué avec le blé.", "Le fromage est fabriqué avec le lait.", "Pour la justification : cherche « atelier ou une usine »."],
            J("Quelle phrase de la fiche définit un produit transformé ?", A_TRANS, [A_AGRI, A_EX, A_ESPACE], pos=1)),
    }
    d["e10-2"] = {
        "mousse": assoc(
            "Relie chaque produit agricole au produit transformé fabriqué à partir de lui.",
            [("Lait", "Fromage"), ("Blé", "Pain"), ("Cacao", "Chocolat")],
            ["Ouvre la fiche " + FICHE + ".", "Le pain est fabriqué avec le blé.", "Le chocolat vient du cacao."]),
        "lieutenant": qcm(
            "Camille te teste sur l'origine des produits. Réponds, puis choisis la phrase de la fiche qui donne des exemples de produits transformés.",
            [("Le pain est fabriqué à partir de…", ["blé", "lait", "cacao", "tomate"], 0, "La farine de blé fait le pain."),
             ("Le yaourt est fabriqué à partir de…", ["lait", "blé", "raisin", "betterave"], 0, "Comme le fromage."),
             ("Le sucre est fabriqué à partir de la canne à sucre ou de…", ["la betterave", "la pomme de terre", "la carotte", "le maïs"], 0, "Deux plantes donnent le sucre."),
             ("Le chocolat est fabriqué à partir du…", ["cacao", "café", "blé", "raisin"], 0, "Le cacao pousse sur un arbre tropical.")],
            ["Le pain vient du blé.", "Le sucre a deux origines possibles.", "Pour la justification : cherche « betterave »."],
            J("Quelle phrase de la fiche donne des exemples de produits transformés ?", A_EX, [A_AGRI, A_TRANS, A_ESPACE], pos=0)),
    }
    d["e10-3"] = {
        "mousse": qcm(
            "Camille vérifie ce que tu as retenu.",
            [("Un produit transformé est…", ["fabriqué à partir d'un produit agricole", "cueilli directement dans un champ", "toujours un fruit"], 0, "Il est fabriqué par quelqu'un."),
             ("Qui cultive les légumes ?", ["le maraîcher", "l'éleveur", "le céréalier"], 0, "Le maraîcher cultive les légumes.")],
            ["Ouvre la fiche " + FICHE + ".", "Un produit transformé a été fabriqué.", "Le maraîcher cultive des carottes."]),
        "lieutenant": assoc(
            "Relie chaque espace de production au métier de la personne qui y travaille, puis choisis la phrase de la fiche sur le verger.",
            [("un élevage", "l'éleveur"), ("un champ de céréales", "le céréalier"), ("une exploitation maraîchère", "le maraîcher"), ("un verger", "l'arboriculteur")],
            ["L'éleveur élève des animaux.", "Le céréalier cultive le blé.", "Pour la justification : cherche « pommes, poires et cerises »."],
            J("Quelle phrase de la fiche parle du verger ?", A_ARBO, [A_ELEV, A_CEREAL, A_MARAIC], pos=3)),
    }
    d["e10-4"] = {
        "lieutenant": ordre(
            "Camille te raconte le trajet du blé jusqu'au pain. Range les étapes dans l'ordre, puis choisis la phrase de la fiche qui dit d'où vient le pain.",
            ["Le blé est cultivé dans un champ", "Le blé est récolté", "Le blé est transformé en farine", "Le boulanger fabrique le pain avec la farine"],
            ["Tout commence dans un champ.", "La farine est faite avec le blé récolté.", "Pour la justification : cherche « Le pain vient du blé »."],
            J("Quelle phrase de la fiche dit d'où vient le pain ?", A_EX, [A_TRANS, A_CEREAL, A_ESPACE], pos=2)),
        "second": code(
            "Camille compte les aliments du plateau : une pomme, des haricots verts, des carottes, du poulet, de la salade, un yaourt, du pain et un cookie. Compte, puis choisis la phrase de la fiche qui définit un produit agricole.",
            [("Produits agricoles sur le plateau", "5", 1), ("Produits transformés sur le plateau", "3", 1), ("Aliments en tout", "8", 1)],
            ["Reprends le tri du plateau.", "Le yaourt, le pain et le cookie sont fabriqués.", "5 + 3. Pour la justification : cherche « directement de la nature »."],
            J("Quelle phrase de la fiche définit un produit agricole ?", A_AGRI, [A_TRANS, A_EX, A_ESPACE], pos=0)),
    }
    # grade second des énigmes 1 à 3 (association, tri, qcm)
    d["e10-1"]["second"] = assoc(
        "Chaque aliment du plateau vient d'un espace de production. Relie-les, puis choisis la phrase de la fiche qui parle des espaces de production.",
        [("le poulet", "un élevage"), ("le pain (blé)", "un champ de céréales"), ("les carottes", "une exploitation maraîchère"), ("la pomme", "un verger")],
        ["Le poulet est élevé.", "Les carottes sont des légumes.", "Pour la justification : cherche « espace de production »."],
        J("Quelle phrase de la fiche parle des espaces de production ?", A_ESPACE, [A_TRANS, A_AGRI, A_EX], pos=3))
    d["e10-2"]["second"] = tri(
        "Camille te teste avec des produits plus difficiles. Range chacun, puis choisis la phrase de la fiche qui définit un produit agricole.",
        [("agri", "Produits agricoles"), ("trans", "Produits transformés")],
        [("un yaourt nature", "trans"), ("de la compote de pommes", "trans"), ("un œuf", "agri"), ("du jus de raisin", "trans"), ("une salade", "agri"), ("de la sauce tomate", "trans"),
         ("des haricots verts", "agri"), ("du lait", "agri")],
        ["Le lait est du lait : il n'a pas été transformé.", "La compote est fabriquée avec des pommes.", "Pour la justification : cherche « presque tel quel »."],
        J("Quelle phrase de la fiche définit un produit agricole ?", A_AGRI, [A_TRANS, A_ESPACE, A_EX], pos=2))
    d["e10-3"]["second"] = qcm(
        "Camille vérifie tes connaissances, puis choisis la phrase de la fiche qui définit un produit transformé.",
        [("Quelle affirmation est exacte ?", ["un produit transformé est fabriqué à partir d'un ou de plusieurs produits agricoles", "un produit transformé vient directement de la nature",
                                              "un produit agricole est toujours fabriqué dans une usine", "le fromage est un produit agricole"], 0, "Le fromage est fabriqué à partir du lait."),
         ("Un yaourt est…", ["un produit transformé", "un produit agricole", "un légume", "un fruit"], 0, "Il est fabriqué à partir du lait."),
         ("Qui cultive le blé et le maïs ?", ["le céréalier", "l'éleveur", "le maraîcher", "l'arboriculteur"], 0, "Le céréalier cultive des céréales dans des champs.")],
        ["Le fromage est fabriqué à partir du lait.", "Le yaourt aussi.", "Pour la justification : cherche « un ou de plusieurs »."],
        J("Quelle phrase de la fiche définit un produit transformé ?", A_TRANS, [A_AGRI, A_EX, A_CEREAL], pos=1))
    return d
