"""exercices.py — Fiches d'exercices ciblées imprimables (section 4 Phase I).

Banque de phrases à corriger par catégorie. fiche() en tire N phrases pour la
catégorie faible d'un élève. Contenu de départ, librement remplaçable par les
phrases de l'enseignant (rattachées à ses leçons).
"""
import random

import database as db
from theme import CATEGORIES, LIBELLES_CATEGORIES

EXERCICES = {
    "accord": [
        ("Les enfants joue dans la cour.", "Les enfants jouent dans la cour.", "verbe au pluriel"),
        ("Elle a mangé des pommes rouge.", "Elle a mangé des pommes rouges.", "adjectif au pluriel"),
        ("Les fille sont parties.", "Les filles sont parties.", "nom au pluriel"),
        ("Ces livres sont intéressant.", "Ces livres sont intéressants.", "adjectif au pluriel"),
        ("Les maisons est grande.", "Les maisons sont grandes.", "verbe + adjectif pluriel"),
        ("Mon frère et ma sœur est content.", "Mon frère et ma sœur sont contents.", "sujet pluriel"),
    ],
    "conjugaison": [
        ("Demain, nous iront à l'école.", "Demain, nous irons à l'école.", "futur : -ons"),
        ("Tu prend ton cartable.", "Tu prends ton cartable.", "2e pers. : -s"),
        ("Ils finisse leurs devoirs.", "Ils finissent leurs devoirs.", "3e pers. pluriel"),
        ("Je suis aller au marché.", "Je suis allé au marché.", "participe passé"),
        ("Hier, il joue dans le jardin.", "Hier, il jouait dans le jardin.", "imparfait"),
        ("Nous mangeon à midi.", "Nous mangeons à midi.", "1re pers. pluriel"),
    ],
    "homophone": [
        ("Il va a l'école.", "Il va à l'école.", "a / à"),
        ("Son frère et sa sœur son partis.", "Son frère et sa sœur sont partis.", "son / sont"),
        ("Je ne sais pas ou il est.", "Je ne sais pas où il est.", "ou / où"),
        ("C'est chaussures sont neuves.", "Ces chaussures sont neuves.", "ces / c'est"),
        ("Tu a raison.", "Tu as raison.", "a / as"),
        ("Il pense quil a gagné.", "Il pense qu'il a gagné.", "qu'il"),
    ],
    "orthographe": [
        ("Il fait beaucoup de fotes.", "Il fait beaucoup de fautes.", "faute"),
        ("Un éléfant marche lentement.", "Un éléphant marche lentement.", "ph"),
        ("Il y a des animos dans le pré.", "Il y a des animaux dans le pré.", "pluriel -aux"),
        ("Nous avons vu un oizeau.", "Nous avons vu un oiseau.", "oi + s"),
        ("Le pharaon vivait en Égipte.", "Le pharaon vivait en Égypte.", "Égypte"),
        ("Elle porte un joli chapo.", "Elle porte un joli chapeau.", "-eau"),
    ],
    "segmentation": [
        ("Jai froid ce matin.", "J'ai froid ce matin.", "J'ai"),
        ("Ilya beaucoup de monde.", "Il y a beaucoup de monde.", "il y a"),
        ("Il ne veut pas yaller.", "Il ne veut pas y aller.", "y aller"),
        ("Apeupré dix élèves sont là.", "À peu près dix élèves sont là.", "à peu près"),
        ("Cet homme est untravailleur.", "Cet homme est un travailleur.", "un travailleur"),
        ("Elle part toutdesuite.", "Elle part tout de suite.", "tout de suite"),
    ],
    "ponctuation": [
        ("Où vas-tu", "Où vas-tu ?", "question → ?"),
        ("Quel beau temps", "Quel beau temps !", "exclamation → !"),
        ("Il achète des pommes des poires et des kiwis.",
         "Il achète des pommes, des poires et des kiwis.", "virgules d'énumération"),
        ("Attention le sol est glissant.", "Attention, le sol est glissant.", "virgule"),
        ("Viens ici", "Viens ici !", "ordre → !"),
        ("Le chien aboie le chat s'enfuit.", "Le chien aboie, le chat s'enfuit.", "virgule"),
    ],
    "majuscule": [
        ("je m'appelle paul.", "Je m'appelle Paul.", "début + prénom"),
        ("nous habitons à paris.", "Nous habitons à Paris.", "ville"),
        ("le lundi, nous avons sport.", "Le lundi, nous avons sport.", "début de phrase"),
        ("elle lit un livre.", "Elle lit un livre.", "début de phrase"),
        ("mon ami s'appelle karim.", "Mon ami s'appelle Karim.", "prénom"),
        ("la seine traverse paris.", "La Seine traverse Paris.", "fleuve + ville"),
    ],
    "lexique": [
        ("Cette histoire est très bien.", "Cette histoire est passionnante.", "éviter « bien »"),
        ("Il fait un truc bizarre.", "Il fait un geste étrange.", "éviter « truc »"),
        ("La nourriture était bonne.", "La nourriture était délicieuse.", "enrichir « bonne »"),
        ("Il y a beaucoup de choses.", "Il y a de nombreux objets.", "éviter « choses »"),
        ("C'était un bon film.", "C'était un film captivant.", "enrichir « bon »"),
        ("Elle a fait un dessin.", "Elle a réalisé un dessin.", "éviter « faire »"),
    ],
}


def categorie_faible(eleve_id):
    """Catégorie la plus fréquente dans les séances de l'élève (repli : accord)."""
    sc = db.seances_correction(eleve_id=eleve_id)
    tot = {c: 0 for c in CATEGORIES}
    for s in sc:
        for c, v in (s.get("detail_avant") or {}).items():
            if c in tot:
                tot[c] += v
    pire = max(tot, key=tot.get)
    return pire if tot[pire] > 0 else "accord"


# Ce qu'il faut regarder, catégorie par catégorie : rappel imprimé en tête de
# fiche, pour que l'élève sache QUOI chercher avant de corriger.
RAPPELS = {
    "accord": ("Je cherche le mot chef (le nom, le sujet), puis je regarde qui "
               "doit s'accorder avec lui.",
               ["Le nom au pluriel entraîne son adjectif : des pommes rouges.",
                "Le sujet au pluriel entraîne son verbe : les enfants jouent."]),
    "conjugaison": ("Je repère le sujet et le temps, puis je vérifie la "
                    "terminaison du verbe.",
                    ["je → -e / -s   tu → -s   il → -e / -t",
                     "nous → -ons   vous → -ez   ils → -ent"]),
    "homophone": ("Ces mots se prononcent pareil mais ne s'écrivent pas pareil : "
                  "je remplace pour vérifier.",
                  ["a → je remplace par « avait » ; sinon c'est à.",
                   "et → je remplace par « et puis » ; sinon c'est est.",
                   "son → je remplace par « le sien » ; sinon c'est sont."]),
    "orthographe": ("Je découpe le mot en syllabes et je me demande si je l'ai "
                    "déjà rencontré écrit.",
                    ["Attention aux sons qui s'écrivent de plusieurs façons : "
                     "o / au / eau, f / ph, s / ss / c.",
                     "Je pense aux mots de la même famille."]),
    "segmentation": ("Je vérifie que chaque mot est bien séparé du suivant.",
                     ["Il y a → trois mots.   J'ai → apostrophe.",
                      "Je lis lentement, mot par mot, avec le doigt."]),
    "ponctuation": ("Je relis à voix haute : là où ma voix s'arrête, il faut un "
                    "signe.",
                    ["Question → ?   Émotion, ordre → !   Fin → .",
                     "J'énumère → je sépare par des virgules."]),
    "majuscule": ("Une majuscule au début de chaque phrase et à chaque nom propre.",
                  ["Prénoms, noms de villes, de pays, de fleuves.",
                   "Après un point, on repart avec une majuscule."]),
    "lexique": ("Je remplace les mots passe-partout par un mot précis.",
                ["bien, truc, chose, faire, bon → je cherche mieux.",
                 "Un mot précis rend la phrase plus vivante."]),
}

# Extraits courts pour la lecture répétée, si aucun texte de fluence n'existe
# encore dans la base (domaine public).
EXTRAIT_SECOURS = (
    "Le vent se leva d'un coup et fit claquer les volets de la vieille maison. "
    "Dans la cour, les feuilles tournaient comme de petits oiseaux affolés. "
    "Marion approcha son visage de la vitre froide et retint son souffle : "
    "au fond du jardin, quelque chose venait de bouger derrière le grand "
    "noyer. Elle compta jusqu'à trois, poussa la porte et descendit les "
    "marches une à une."
)



# Objectif pédagogique de chaque fiche, formulé pour un document de suivi.
OBJECTIFS = {
    "accord": "Repérer le donneur d'accord et accorder le groupe nominal",
    "conjugaison": "Identifier le sujet et accorder le verbe",
    "homophone": "Distinguer les homophones grammaticaux par substitution",
    "orthographe": "Consolider l'orthographe lexicale",
    "segmentation": "Segmenter correctement la chaîne écrite",
    "ponctuation": "Employer la ponctuation de fin et la virgule",
    "majuscule": "Employer la majuscule en début de phrase et aux noms propres",
    "lexique": "Enrichir et préciser le vocabulaire",
    "lecture": "Développer la fluence par la lecture répétée",
    "methode": "Installer une procédure de relecture ordonnée",
}

def lecon_du_classeur(categorie):
    """Le contenu de la leçon du classeur rattachée à cette catégorie.

    C'est ce qui relie la fiche d'exercices aux leçons réellement vues en
    classe : l'élève retrouve la formulation de SON classeur, pas une règle
    réécrite par l'application.
    """
    try:
        import lecons_manuel as lm
        return lm.contenu_pour_categorie(categorie)
    except Exception:
        return None


def fiche(eleve_prenom, categorie, nombre=6, groupe=False):
    if categorie not in EXERCICES:
        categorie = "accord"
    banque = EXERCICES[categorie][:]
    random.shuffle(banque)
    phrases = banque[:min(nombre, len(banque))]
    rappel, astuces = RAPPELS.get(categorie, ("", []))

    # Si le classeur de l'enseignant contient une leçon sur cette catégorie,
    # c'est SA règle et SON astuce qui sont imprimées en tête de fiche.
    lec = lecon_du_classeur(categorie)
    if lec:
        if lec.get("regle"):
            rappel = lec["regle"]
        if lec.get("astuce"):
            astuces = [lec["astuce"]] + [a for a in astuces][:1]

    return {
        "genre": "exercices",
        "eleve": eleve_prenom,
        "groupe": groupe,
        "categorie": categorie,
        "categorie_label": LIBELLES_CATEGORIES.get(categorie, categorie),
        "domaine": "Étude de la langue",
        "objectif": OBJECTIFS.get(categorie, ""),
        "rappel": rappel,
        "astuces": astuces,
        "lecon": lec,
        "phrases": [{"faux": f, "correct": c, "indice": i} for (f, c, i) in phrases],
    }


def fiche_fluence(eleve_prenom, base, config):
    """Fiche de lecture répétée : un texte court, trois passages chronométrés."""
    texte, titre = EXTRAIT_SECOURS, "Le grand noyer"
    try:
        niveau = 2
        tous = [t for t in base.liste_textes_fluence() if t.get("contenu")]
        if tous:
            candidats = [t for t in tous if t.get("niveau") == niveau] or tous
            choisi = random.choice(candidats)
            texte, titre = choisi["contenu"], choisi.get("titre", "Texte de lecture")
    except Exception:
        pass
    nb_mots = len(texte.split())
    repere = 90
    try:
        from theme import REPERES_MCLM
        repere = REPERES_MCLM.get(config.get("fluence_niveau_classe", "CM1"), 90)
    except Exception:
        pass
    return {
        "genre": "fluence",
        "eleve": eleve_prenom,
        "groupe": False,
        "categorie": "lecture",
        "categorie_label": "Lecture à voix haute",
        "domaine": "Lecture",
        "objectif": OBJECTIFS["lecture"],
        "titre_texte": titre,
        "texte": texte,
        "nb_mots": nb_mots,
        "repere": repere,
        "rappel": "Je lis trois fois le même texte. À chaque passage, je lis un "
                  "peu mieux : je bute moins, je respire aux virgules.",
        "astuces": [
            "Passage 1 : je découvre. Je lis sans me presser.",
            "Passage 2 : je repère les mots difficiles et je les relis à part.",
            "Passage 3 : je lis pour être compris — je fais entendre la ponctuation.",
        ],
    }


def fiche_dictee(eleve_prenom, eleve_id=None):
    """Fiche de mémorisation : les mots que l'élève rate en dictée.

    Trois colonnes — le mot modèle, une copie, une écriture de mémoire :
    c'est la procédure « regarde, cache, écris, vérifie », la plus efficace
    pour installer l'image orthographique d'un mot.
    """
    mots = []
    try:
        if eleve_id:
            mots = [m["mot"] for m in db.banque_lexicale(eleve_id)][:12]
    except Exception:
        pass
    if not mots:
        mots = ["beaucoup", "toujours", "souvent", "longtemps", "aujourd'hui",
                "quelquefois", "pourtant", "maintenant"]
    return {
        "genre": "dictee",
        "eleve": eleve_prenom,
        "groupe": False,
        "categorie": "methode",
        "categorie_label": "Mémoriser mes mots",
        "domaine": "Orthographe lexicale",
        "objectif": "Mémoriser l'orthographe des mots régulièrement échoués",
        "mots": mots,
        "rappel": "Je regarde le mot, je le cache, je l'écris de mémoire, "
                  "puis je vérifie. Trois fois de suite, sans erreur.",
        "astuces": [
            "Je découpe le mot en syllabes et je repère la partie difficile.",
            "Je m'attarde sur les lettres que l'on n'entend pas.",
        ],
    }


def fiche_methode(eleve_prenom):
    """Fiche de méthode : relire en cherchant UNE catégorie à la fois."""
    return {
        "genre": "methode",
        "eleve": eleve_prenom,
        "groupe": False,
        "categorie": "methode",
        "categorie_label": "Ma méthode de relecture",
        "domaine": "Méthodologie",
        "objectif": OBJECTIFS["methode"],
        "rappel": "On ne trouve pas tout en une seule relecture. Je relis "
                  "plusieurs fois, en cherchant une seule chose à chaque fois.",
        "astuces": [
            "Je relis à voix basse, avec le doigt : je vois mieux les mots.",
            "Je coche une case dès qu'un passage est terminé.",
        ],
        "passages": [
            ("1", "Les majuscules et les points",
             "Chaque phrase commence par une majuscule et finit par un point."),
            ("2", "Les verbes", "Je souligne chaque verbe, je cherche son sujet, "
             "je vérifie la terminaison."),
            ("3", "Les accords", "J'entoure les noms au pluriel et je vérifie "
             "leurs adjectifs."),
            ("4", "Les petits mots qui piègent",
             "a / à — et / est — son / sont — ou / où — ces / c'est."),
            ("5", "Les mots que je ne suis pas sûr d'écrire",
             "Je les entoure au crayon et je vais les vérifier."),
        ],
    }


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# --------------------------------------------------------------------------
#  Rendu imprimable
# --------------------------------------------------------------------------
_CSS = """
@page { size: A4; margin: 14mm 15mm 12mm; }
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Segoe UI",system-ui,-apple-system,Roboto,sans-serif;
 color:#1E2233;background:#F1F3F8;padding:22px}
.feuille{max-width:196mm;margin:0 auto;background:#fff;padding:18mm 16mm 14mm;
 box-shadow:0 8px 30px rgba(16,24,40,.14);border-radius:6px}
.bandeau{display:flex;align-items:flex-start;gap:16px;
 border-bottom:3px solid var(--c);padding-bottom:14px;margin-bottom:6px}
.bandeau .ico{width:52px;height:52px;flex:0 0 52px;border-radius:14px;
 background:var(--c);color:#fff;display:flex;align-items:center;
 justify-content:center;font-size:26px}
.bandeau h1{font-size:21px;letter-spacing:-.02em;line-height:1.2}
.bandeau .sur{font-size:11px;font-weight:700;letter-spacing:.12em;
 text-transform:uppercase;color:var(--c);margin-bottom:3px}
.bandeau .cible{margin-left:auto;text-align:right;font-size:12px;color:#5B6478;
 line-height:1.9;min-width:130px}
.bandeau .cible b{display:block;font-size:14px;color:#1E2233}
.trait-nom{display:inline-block;min-width:96px;border-bottom:1px solid #C3C9D6}
.consigne{background:var(--pale);border-left:5px solid var(--c);
 border-radius:0 10px 10px 0;padding:13px 16px;margin:18px 0 6px;font-size:14px;
 line-height:1.55}
.consigne .t{font-weight:700;color:var(--c);font-size:12px;
 text-transform:uppercase;letter-spacing:.08em;margin-bottom:4px}
.renvoi-lecon{margin-top:16px;font-size:12.5px;color:#5B6478;
 background:#F5F7FB;border:1px solid #E2E6EF;border-radius:9px;padding:9px 13px}
.renvoi-lecon .ref{color:#9AA1B0;font-size:11px;letter-spacing:.04em}
.modeles{border:1.5px dashed var(--c);border-radius:11px;padding:12px 15px;
 margin:0 0 20px;background:var(--pale)}
.modeles-t{font-size:11px;font-weight:700;letter-spacing:.08em;
 text-transform:uppercase;color:var(--c);margin-bottom:7px}
.modele{font-size:13.5px;line-height:1.7}
.astuces{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 20px}
.astuce{background:#F5F7FB;border:1px solid #E2E6EF;border-radius:9px;
 padding:8px 12px;font-size:12.5px;color:#3D465C;flex:1 1 240px}
ol.items{list-style:none;counter-reset:n}
ol.items li{counter-increment:n;display:flex;gap:14px;align-items:flex-start;
 padding:13px 0 15px;border-bottom:1px dashed #DDE1EA;page-break-inside:avoid}
ol.items li:last-child{border-bottom:none}
ol.items li::before{content:counter(n);flex:0 0 30px;height:30px;border-radius:50%;
 background:var(--pale);color:var(--c);font-weight:800;font-size:14px;
 display:flex;align-items:center;justify-content:center;margin-top:1px}
.phrase{font-size:15.5px;font-weight:600;line-height:1.5}
.ligne-ecriture{margin-top:11px;border-bottom:1.5px solid #C9CFDC;height:22px}
.ligne-ecriture.courte{width:78%}
.zone-texte{border:2px solid var(--pale);border-radius:12px;padding:18px 20px;
 font-family:Georgia,"Times New Roman",serif;font-size:16.5px;line-height:2.05;
 text-align:justify;margin:6px 0 18px}
.chrono-grille{display:flex;gap:10px;margin-bottom:18px}
.chrono-case{flex:1;border:2px solid #E2E6EF;border-radius:12px;padding:12px;
 text-align:center}
.chrono-case .n{font-size:11px;font-weight:700;letter-spacing:.08em;
 text-transform:uppercase;color:var(--c)}
.chrono-case .l{border-bottom:1.5px solid #C9CFDC;height:26px;margin:10px 4px 6px}
.chrono-case .u{font-size:10.5px;color:#8A93A6}
.etapes{display:flex;flex-direction:column;gap:10px}
.etape-m{display:flex;gap:13px;align-items:flex-start;border:1.5px solid #E2E6EF;
 border-left:5px solid var(--c);border-radius:0 11px 11px 0;padding:12px 15px;
 page-break-inside:avoid}
.etape-m .case{flex:0 0 22px;height:22px;border:2px solid var(--c);
 border-radius:6px;margin-top:1px}
.etape-m .t{font-weight:700;font-size:14.5px}
.etape-m .d{font-size:12.5px;color:#5B6478;margin-top:3px;line-height:1.5}
.auto{margin-top:22px;border-top:2px solid #E2E6EF;padding-top:14px;
 display:flex;align-items:center;gap:14px;font-size:12.5px;color:#5B6478;
 page-break-inside:avoid}
.auto .q{font-weight:700;color:#1E2233}
.smiley{display:flex;gap:9px;margin-left:auto}
.smiley span{width:34px;height:34px;border:2px solid #D5DAE4;border-radius:50%;
 display:flex;align-items:center;justify-content:center;font-size:17px}
.pied{margin-top:16px;font-size:10.5px;color:#9AA1B0;text-align:center;
 border-top:1px solid #EDEFF4;padding-top:9px}
.corrige{page-break-before:always;margin-top:26px}
.bandeau-titre{flex:1;min-width:0}
.bandeau .sous-titre{font-size:11.5px;color:#5B6478;margin-top:2px;font-style:italic}
.cible{margin-left:auto;text-align:right;min-width:44mm}
.cible-l{font-size:9px;text-transform:uppercase;letter-spacing:.09em;
 color:#9AA1B0;font-weight:700;margin-top:2.5mm}
.cible-v{font-size:13px;font-weight:700;color:#1E2233;line-height:1.3}
.cible-v.trait{border-bottom:0.3mm solid #C3C9D6;min-height:5mm}
.cible-ref{margin-top:2.5mm;font-size:9px;color:#B4BAC6;letter-spacing:.05em}
.pied{display:flex;justify-content:space-between;align-items:center;gap:10px;
 flex-wrap:wrap}
.pied-espace{white-space:nowrap}
.pied-trait{display:inline-block;width:26mm;border-bottom:0.3mm solid #C3C9D6}
ol.rep li{justify-content:space-between}
ol.rep .coche{display:flex;gap:2mm;flex:0 0 auto;margin-left:auto}
ol.rep .coche i{display:block;width:4.5mm;height:4.5mm;border:0.3mm solid #C3C9D6;
 border-radius:1mm}
ol.rep .coche i:first-child{border-color:#15A34A}
ol.rep .coche i:last-child{border-color:#D97706}
.legende-coche{font-size:10px;color:#9AA1B0;margin-top:2mm;text-align:right}
table.memo{width:100%;border-collapse:collapse;margin-top:2mm}
table.memo th{background:var(--pale);color:var(--c);font-size:10px;
 text-transform:uppercase;letter-spacing:.06em;padding:2.5mm 2mm;
 border:0.25mm solid var(--pale);text-align:left}
table.memo td{border:0.25mm solid #E2E6EF;height:10mm;padding:1mm 2mm}
.memo-mot{font-size:14px;font-weight:700;color:var(--c);width:28%}
.memo-vide{width:28%}
.memo-coche{width:16%;background:#FAFBFD}
.grille-suivi{margin-top:8mm;border:0.3mm solid #E2E6EF;border-radius:2mm;
 padding:4mm 5mm;page-break-inside:avoid}
.gs-t{font-size:10px;font-weight:700;text-transform:uppercase;
 letter-spacing:.08em;color:#5B6478;margin-bottom:3mm}
.gs-l{border-bottom:0.25mm solid #E2E6EF;height:7mm}
.gs-bas{display:flex;justify-content:space-between;gap:10px;margin-top:4mm;
 font-size:11px;color:#5B6478;flex-wrap:wrap}
.gs-case{display:inline-block;width:9mm;border-bottom:0.3mm solid #C3C9D6}
.gs-trait{display:inline-block;width:52mm;border-bottom:0.3mm solid #C3C9D6}

.corrige .bandeau{border-color:#15A34A}
.corrige .bandeau .ico{background:#15A34A}
.corrige .bandeau .sur{color:#15A34A}
ol.rep{list-style:none;counter-reset:m;margin-top:14px}
ol.rep li{counter-increment:m;display:flex;gap:13px;padding:9px 0;
 border-bottom:1px solid #EDEFF4;font-size:14px;line-height:1.5}
ol.rep li::before{content:counter(m);flex:0 0 26px;height:26px;border-radius:50%;
 background:#E6F6EC;color:#15A34A;font-weight:800;font-size:12.5px;
 display:flex;align-items:center;justify-content:center}
ol.rep em{color:#15A34A;font-style:normal;font-weight:600;font-size:12.5px}
.barre{position:fixed;top:0;left:0;right:0;background:#1E2233;color:#fff;
 padding:10px 18px;display:flex;align-items:center;gap:14px;font-size:13px;
 box-shadow:0 2px 10px rgba(0,0,0,.25);z-index:9}
.barre button{background:var(--c);color:#fff;border:none;padding:9px 20px;
 border-radius:8px;cursor:pointer;font-size:13.5px;font-weight:600;
 font-family:inherit}
.barre button:hover{filter:brightness(1.1)}
body{padding-top:60px}
@media print{
 body{background:#fff;padding:0}
 .feuille{box-shadow:none;max-width:none;padding:0;border-radius:0}
 .noprint{display:none !important}
}
"""

_COULEURS = {
    "accord": ("#2563EB", "#EFF6FF"), "conjugaison": ("#7C3AED", "#F3EEFF"),
    "homophone": ("#D97706", "#FFF6E6"), "orthographe": ("#DC2626", "#FEF0F0"),
    "segmentation": ("#0891B2", "#E7F7FB"), "ponctuation": ("#15A34A", "#E9F8EF"),
    "majuscule": ("#DB2777", "#FDF0F7"), "lexique": ("#0EA5E9", "#E8F6FE"),
    "lecture": ("#0EA5E9", "#E8F6FE"), "methode": ("#2563EB", "#EFF6FF"),
}

_ICONES = {"exercices": "✏️", "fluence": "📖", "methode": "🧭"}


def _bandeau(f, coul):
    """En-tête de la fiche : toutes les références utiles au suivi.

    Une fiche de remédiation se range dans un classeur, se montre aux
    familles, se compare d'une séance à l'autre : elle doit porter le nom de
    l'élève, le domaine travaillé et la date.
    """
    ico = _ICONES.get(f["genre"], "✏️")
    qui = "Groupe" if f.get("groupe") else "Élève"
    lec = f.get("lecon") or {}
    reference = lec.get("lecon_id") or f.get("categorie", "").upper()[:8]
    return f"""<div class="bandeau">
  <div class="ico">{ico}</div>
  <div class="bandeau-titre">
    <div class="sur">Remédiation · {_esc(f.get("domaine", "Français"))}</div>
    <h1>{_esc(f["categorie_label"])}</h1>
    <div class="sous-titre">{_esc(f.get("objectif", ""))}</div>
  </div>
  <div class="cible">
    <div class="cible-l">{qui}</div>
    <div class="cible-v">{_esc(f["eleve"]) or "&nbsp;"}</div>
    <div class="cible-l">Date</div>
    <div class="cible-v trait"></div>
    <div class="cible-ref">Réf. {_esc(reference)}</div>
  </div>
</div>"""


def _consigne(f):
    astuces = "".join(f'<div class="astuce">{_esc(a)}</div>'
                      for a in f.get("astuces", []))
    lec = f.get("lecon") or {}
    # Renvoi explicite vers la leçon du classeur : l'élève sait où réviser.
    renvoi = ""
    if lec.get("titre"):
        renvoi = (f'<div class="renvoi-lecon">📘 Leçon du classeur : '
                  f'<b>{_esc(lec["titre"])}</b> '
                  f'<span class="ref">{_esc(lec.get("lecon_id", ""))}</span></div>')
    modeles = ""
    if lec.get("exemples"):
        modeles = ('<div class="modeles"><div class="modeles-t">Les modèles de la '
                   'leçon</div>' + "".join(
                       f'<div class="modele">{_esc(e)}</div>'
                       for e in lec["exemples"]) + "</div>")
    return f"""{renvoi}<div class="consigne"><div class="t">Ce qu'il faut regarder</div>
{_esc(f.get("rappel", ""))}</div>
<div class="astuces">{astuces}</div>{modeles}"""


def _autoeval():
    return """<div class="auto">
  <span class="q">Comment ça s'est passé ?</span>
  <span>Je colorie la tête qui me correspond.</span>
  <span class="smiley"><span>🙂</span><span>😐</span><span>🙁</span></span>
</div>"""


def html_fiche(f):
    """Page HTML imprimable complète (ouverte ensuite dans le navigateur)."""
    coul, pale = _COULEURS.get(f["categorie"], ("#2563EB", "#EFF6FF"))
    corps, corrige = "", ""

    if f["genre"] == "exercices":
        corps = '<ol class="items">' + "".join(
            f'<li><div style="flex:1"><div class="phrase">{_esc(p["faux"])}</div>'
            f'<div class="ligne-ecriture"></div></div></li>'
            for p in f["phrases"]) + "</ol>"
        lec = f.get("lecon") or {}
        corrige = f"""<div class="corrige">
<div class="bandeau"><div class="ico">✅</div>
  <div class="bandeau-titre">
    <div class="sur">Document enseignant</div>
    <h1>Corrigé et grille d'observation</h1>
    <div class="sous-titre">{_esc(f["categorie_label"])}
      {" · leçon " + _esc(lec["lecon_id"]) if lec.get("lecon_id") else ""}</div>
  </div>
  <div class="cible">
    <div class="cible-l">{"Groupe" if f.get("groupe") else "Élève"}</div>
    <div class="cible-v">{_esc(f["eleve"]) or "&nbsp;"}</div>
    <div class="cible-l">Date de passation</div>
    <div class="cible-v trait"></div>
  </div></div>
<ol class="rep">{"".join(
    f'<li><span><b>{_esc(p["correct"])}</b> '
    f'<em>{_esc(p["indice"])}</em></span>'
    f'<span class="coche"><i></i><i></i></span></li>'
    for p in f["phrases"])}</ol>
<div class="legende-coche">Cochez la première case si l'item est réussi,
la seconde s'il reste à travailler.</div>
<div class="grille-suivi">
  <div class="gs-t">Observations</div>
  <div class="gs-l"></div><div class="gs-l"></div><div class="gs-l"></div>
  <div class="gs-bas">
    <span>Items réussis : <b class="gs-case"></b> / {len(f["phrases"])}</span>
    <span>Suite à donner : <span class="gs-trait"></span></span>
  </div>
</div></div>"""

    elif f["genre"] == "fluence":
        corps = f"""<div style="font-size:12px;color:#8A93A6;margin-bottom:6px">
  « {_esc(f["titre_texte"])} » — {f["nb_mots"]} mots</div>
<div class="zone-texte">{_esc(f["texte"])}</div>
<div class="chrono-grille">
  {"".join(f'''<div class="chrono-case"><div class="n">Passage {i}</div>
    <div class="l"></div><div class="u">mots lus en 1 minute</div></div>'''
    for i in (1, 2, 3))}
</div>
<div class="consigne"><div class="t">Mon objectif</div>
  Lire <b>{f["repere"]} mots en une minute</b>, sans se tromper et en faisant
  entendre la ponctuation.</div>"""

    elif f["genre"] == "dictee":
        corps = ('<table class="memo"><thead><tr>'
                 '<th>Le mot modèle</th><th>Je le copie</th>'
                 '<th>Je l\'écris de mémoire</th><th>Vérifié</th></tr></thead><tbody>'
                 + "".join(
                     f'<tr><td class="memo-mot">{_esc(m)}</td>'
                     f'<td class="memo-vide"></td><td class="memo-vide"></td>'
                     f'<td class="memo-coche"></td></tr>' for m in f["mots"])
                 + "</tbody></table>")

    else:  # methode
        corps = '<div class="etapes">' + "".join(
            f'<div class="etape-m"><div class="case"></div>'
            f'<div><div class="t">{_esc(n)}. {_esc(t)}</div>'
            f'<div class="d">{_esc(d)}</div></div></div>'
            for n, t, d in f["passages"]) + "</div>"

    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fiche — {_esc(f["categorie_label"])}</title>
<style>:root{{--c:{coul};--pale:{pale}}}{_CSS}</style></head><body>
<div class="barre noprint">
  <span>Fiche prête. Utilisez le bouton pour l'imprimer ou l'enregistrer en PDF.</span>
  <button onclick="window.print()">🖨️ Imprimer / PDF</button>
</div>
<div class="feuille">
{_bandeau(f, coul)}
{_consigne(f)}
{corps}
{_autoeval()}
<div class="pied">
  <span>Remédiation individualisée — établie d'après le suivi des séances.</span>
  <span class="pied-espace">Vu par l'enseignant : <span class="pied-trait"></span>
    &nbsp;&nbsp; Vu par la famille : <span class="pied-trait"></span></span>
</div>
{corrige}
</div></body></html>"""
