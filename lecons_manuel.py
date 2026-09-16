"""lecons_manuel.py — Fiches du classeur de l'enseignant (Phase J).

Contenu réel fourni par l'enseignant : 70 mini-leçons CM1 au format carte A7
(orthographe, grammaire, conjugaison, vocabulaire), déjà mises en forme en HTML
imprimable. Ce module les charge telles quelles pour les rattacher aux 8
catégories d'erreurs détectées par le correcteur, et pour être consultables
librement par l'élève ou l'enseignant.

Fichiers sources : data_lecons_manuel.json (contenu des 70 fiches),
data_lecons_manuel.css (mise en forme d'origine des cartes).
"""
import json
import os

from paths import dossier_ressources

_ICI = str(dossier_ressources())
_JSON = os.path.join(_ICI, "data_lecons_manuel.json")
_CSS = os.path.join(_ICI, "data_lecons_manuel.css")

# Rattachement des 8 catégories du correcteur aux fiches du classeur les plus
# pertinentes (par lecon_id). Une catégorie peut pointer vers plusieurs fiches :
# la première est proposée en priorité, les suivantes en "pour aller plus loin".
RATTACHEMENT = {
    # Accords : d'abord la règle générale du groupe nominal, puis les cas.
    "accord": ["ORTH-24", "ORTH-25", "ORTH-23", "ORTH-20", "ORTH-19",
               "ORTH-21", "ORTH-22", "ORTH-18"],
    # Conjugaison : le verbe et son sujet, puis l'accord sujet-verbe et les temps.
    "conjugaison": ["ORTH-25", "GRAM-05", "GRAM-06", "CONJ-03", "CONJ-04",
                    "CONJ-06", "CONJ-10", "CONJ-14", "CONJ-18", "ORTH-26"],
    "homophone": ["ORTH-13", "ORTH-14", "ORTH-15", "ORTH-16", "ORTH-17",
                  "VOCA-06"],
    "orthographe": ["ORTH-07", "ORTH-11", "ORTH-06", "ORTH-01", "ORTH-02",
                    "ORTH-05", "ORTH-12"],
    "segmentation": ["GRAM-01", "ORTH-12", "GRAM-16"],
    "ponctuation": ["GRAM-02", "GRAM-03", "GRAM-04"],
    # Majuscules : noms propres d'abord, puis les limites de la phrase.
    "majuscule": ["GRAM-09", "GRAM-01", "GRAM-02"],
    "lexique": ["VOCA-07", "VOCA-03", "VOCA-09", "VOCA-04", "VOCA-05"],
}


def _charger():
    if not os.path.exists(_JSON):
        return {}
    with open(_JSON, encoding="utf-8") as f:
        return json.load(f)


LECONS_MANUEL = _charger()
CSS_MANUEL = open(_CSS, encoding="utf-8").read() if os.path.exists(_CSS) else ""


def disponible():
    return bool(LECONS_MANUEL)


def liste(domaine=None):
    """Liste légère (sans le HTML) pour affichage en index/menu."""
    items = [
        {"lecon_id": v["lecon_id"], "domaine": v["domaine"],
         "sous_domaine": v["sous_domaine"], "titre": v["titre"]}
        for v in LECONS_MANUEL.values()
    ]
    if domaine:
        items = [i for i in items if i["domaine"] == domaine]
    return sorted(items, key=lambda i: i["lecon_id"])


def fiche(lecon_id):
    """Une fiche complète (avec son HTML prêt à afficher)."""
    return LECONS_MANUEL.get(lecon_id)


def fiches_pour_categorie(categorie):
    """Fiches du classeur rattachées à une catégorie d'erreur du correcteur."""
    ids = RATTACHEMENT.get(categorie, [])
    return [LECONS_MANUEL[i] for i in ids if i in LECONS_MANUEL]


def fiche_principale(categorie):
    """La fiche du classeur la plus pertinente pour une catégorie (ou None)."""
    fiches = fiches_pour_categorie(categorie)
    return fiches[0] if fiches else None


# --------------------------------------------------------------------------
#  Extraction du contenu d'une fiche, pour le réutiliser ailleurs
#  (fiches d'exercices imprimées, aide guidée de l'élève).
#  On repart du HTML fourni par l'enseignant : c'est SA formulation qui est
#  reprise, pas une paraphrase.
# --------------------------------------------------------------------------
# Balises « dans le mot » : elles servent à mettre une lettre en gras
# (de grand<b>s</b> pieds). Les retirer avec une espace couperait le mot.
_INLINE = r"</?(?:b|i|em|strong|span|sub|sup|u|small)\b[^>]*>"


def _texte_brut(html_):
    import html as _h
    import re
    t = html_ or ""
    t = re.sub(_INLINE, "", t)              # collées : on les enlève sans espace
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)          # les autres séparent bien deux blocs
    t = _h.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    # Pas d'espace avant une ponctuation faible, ni après une apostrophe.
    t = re.sub(r"\s+([,.;:!?»])", r"\1", t)
    t = re.sub(r"([«'’])\s+", r"\1", t)
    return t.strip()


def contenu(lecon_id):
    """Renvoie {"titre", "regle", "astuce", "exemples"} pour une fiche du classeur.

    · regle    : la règle énoncée dans la fiche (bloc « rule »)
    · astuce   : le conseil de la fiche (bloc « tip », le 💡)
    · exemples : les transformations « X → Y » présentes dans la fiche
    """
    import re
    f = LECONS_MANUEL.get(lecon_id)
    if not f:
        return None
    h = f.get("html", "")
    regles = [_texte_brut(x) for x in
              re.findall(r'<div class="rule">(.*?)</div>', h, re.S)]
    astuces = [_texte_brut(x) for x in
               re.findall(r'<div class="tip">(.*?)</div>', h, re.S)]
    # Exemples : les transformations « X → Y » des tableaux et des encadrés.
    exemples, vus = [], set()
    for motif in (r"<td[^>]*>(.*?)</td>", r'<div class="ex[^"]*">(.*?)</div>',
                  r'<div class="sent">(.*?)</div>'):
        for bloc in re.findall(motif, h, re.S):
            e = _texte_brut(bloc)
            if "\n" in e:                       # exemple sur plusieurs lignes :
                continue                        # illisible une fois recopié
            if "→" in e and 6 < len(e) < 110 and e not in vus:
                vus.add(e)
                exemples.append(e)
    return {
        "lecon_id": f["lecon_id"],
        "titre": re.sub(r"^[^\w]+", "", f.get("titre", "")).strip(),
        "sous_domaine": f.get("sous_domaine", ""),
        # La règle tient parfois sur plusieurs lignes : on garde la première,
        # qui est l'énoncé, pour ne pas surcharger la fiche imprimée.
        "regle": (regles[0].split("\n")[0].strip() if regles else ""),
        "regle_complete": regles[0] if regles else "",
        # Le 💡 est déjà dans le texte : on le retire pour le remettre nous-mêmes.
        "astuce": (astuces[0] if astuces else "").lstrip("💡 ").strip(),
        "exemples": exemples[:4],
    }


def contenu_pour_categorie(categorie):
    """Le contenu de la leçon principale rattachée à une catégorie (ou None)."""
    f = fiche_principale(categorie)
    return contenu(f["lecon_id"]) if f else None
