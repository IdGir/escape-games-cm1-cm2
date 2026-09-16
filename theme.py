"""Design system — refonte visuelle 2026.

Repris du design system de l'application d'origine, cohérent avec « Notes & Suivi ».

Deux ambiances, un seul langage visuel :
- Espace enseignant : indigo posé (pilotage, analyse).
- Espace élève : ambre soleil (accueillant pour des enfants).

Principes :
- Fond de contenu clair et neutre, cartes blanches à liseré discret + coiffe
  colorée (accent de l'espace) : du relief sans « boîtes grises ».
- Emojis rendus avec « Segoe UI Emoji » (glyphes couleur), jamais avec la police
  texte, qui les afficherait en monochrome cassé.
- Boutons d'action francs, padding généreux.
- Barre latérale ardoise profonde, comme dans Notes & Suivi.

Mode sombre : mêmes accents, fonds ardoise. Bascule dans les réglages ;
les vues sont reconstruites à la volée.
"""
from __future__ import annotations

from config_manager import config

# ==============================================================================
#  Couleurs d'action (identiques dans les deux modes)
# ==============================================================================
PRIMARY = "#2563EB"        # bleu franc : actions principales et pastille active
PRIMARY_DARK = "#1D4ED8"
PRIMARY_SOFT = "#EFF6FF"
SUCCESS = "#15A34A"
SUCCESS_DARK = "#12813B"
WARNING = "#D97706"
DANGER = "#DC2626"
INFO = "#0EA5E9"

# Ambiance élève (soleil)
STUDENT = "#E8890C"
STUDENT_DARK = "#B45309"
STUDENT_BG = "#FFF6E6"
STUDENT_BORDER = "#FBD79B"

# Ambiance enseignant
TEACHER = PRIMARY
TEACHER_BG = "#EEF1FE"
TEACHER_BORDER = "#C7D2FE"

# Barre latérale CLAIRE (le rendu attendu), séparée du contenu par un liseré.
SIDEBAR_BG = "#FBFBFD"
SIDEBAR_HOVER = "#F1F3F7"
SIDEBAR_BORDER = "#E5E7EB"
SIDEBAR_TEXT = "#1E2233"
SIDEBAR_TEXT_ACTIVE = "#FFFFFF"
SIDEBAR_MUTED = "#8A91A0"

# Rayons d'arrondi (composants dessinés sur Canvas)
RAYON_CARTE = 10
RAYON_BOUTON = 8
RAYON_NAV = 8
NAV_ACTIVE = {"correction": PRIMARY, "teacher": PRIMARY, "student": STUDENT}

RESOLVED_BG = "#DCFCE7"    # zone corrigée par l'élève
RESOLVED_FG = "#15803D"

FONT_FAMILY = "Segoe UI"
EMOJI_FONT = "Segoe UI Emoji"

# ==============================================================================
#  Fonds et textes — deux jeux, selon le mode
# ==============================================================================
CLAIR = {
    "BG": "#FFFFFF", "BG_ALT": "#F3F4F6", "CARD_BG": "#FFFFFF",
    "CARD_BORDER": "#E5E7EB", "FIELD_BG": "#FFFFFF",
    "TEXT": "#1E2233", "TEXT_MUTED": "#6B7280", "TEXT_FAINT": "#9AA1B0",
    "SURLIGNE": "#FEF3C7", "LIGNE_ALT": "#F5F0E6",
}

SOMBRE = {
    "BG": "#0F1117", "BG_ALT": "#1A1D26", "CARD_BG": "#171A22",
    "CARD_BORDER": "#2A2F3B", "FIELD_BG": "#12151C",
    "TEXT": "#E8EAF0", "TEXT_MUTED": "#9AA1B0", "TEXT_FAINT": "#6B7280",
    "SURLIGNE": "#4A3C12", "LIGNE_ALT": "#191D27",
}


def mode_sombre() -> bool:
    return bool(config.get("theme_sombre", False))


def _fonds():
    return SOMBRE if mode_sombre() else CLAIR


# ==============================================================================
#  Palettes exposées aux vues
#  Dictionnaires MUTÉS sur place : les vues reconstruites voient les nouvelles
#  valeurs sans avoir à ré-importer quoi que ce soit.
# ==============================================================================
ELEVE: dict = {}
PROF: dict = {}


def _construire():
    f = _fonds()
    sombre = mode_sombre()

    commun = {
        "fond": f["BG"], "fond_alt": f["BG_ALT"], "fond_carte": f["CARD_BG"],
        "bordure": f["CARD_BORDER"], "champ": f["FIELD_BG"],
        "texte": f["TEXT"], "texte_doux": f["TEXT_MUTED"],
        "texte_pale": f["TEXT_FAINT"],
        "succes": SUCCESS, "succes_fonce": SUCCESS_DARK,
        "alerte": WARNING, "danger": DANGER, "info": INFO,
        "surligne": f["SURLIGNE"], "ligne_alt": f["LIGNE_ALT"],
        "resolu_fond": "#1E3A2A" if sombre else RESOLVED_BG,
        "resolu_texte": "#86EFAC" if sombre else RESOLVED_FG,
        "sidebar": "#12151C" if sombre else SIDEBAR_BG,
        "sidebar_survol": "#1D212B" if sombre else SIDEBAR_HOVER,
        "sidebar_bordure": "#262B36" if sombre else SIDEBAR_BORDER,
        "sidebar_texte": "#E8EAF0" if sombre else SIDEBAR_TEXT,
        "sidebar_actif": SIDEBAR_TEXT_ACTIVE,
        "sidebar_pale": SIDEBAR_MUTED,
        "doux": "#232833" if sombre else "#F3F4F6",     # boutons secondaires
        "doux_survol": "#2C323F" if sombre else "#E5E7EB",
    }

    ELEVE.clear(); ELEVE.update(commun)
    ELEVE.update({
        "primaire": STUDENT, "primaire_fonce": STUDENT_DARK,
        "secondaire": INFO, "accent": PRIMARY,
        "bandeau": "#3A2E18" if sombre else STUDENT_BG,
        "bandeau_bordure": "#5C4A22" if sombre else STUDENT_BORDER,
        "nav_actif": STUDENT,
    })

    PROF.clear(); PROF.update(commun)
    PROF.update({
        "primaire": PRIMARY, "primaire_fonce": PRIMARY_DARK,
        "secondaire": INFO, "accent": STUDENT,
        "bandeau": "#20243A" if sombre else TEACHER_BG,
        "bandeau_bordure": "#343B5C" if sombre else TEACHER_BORDER,
        "nav_actif": PRIMARY,
    })


_construire()


def basculer_mode(sombre: bool):
    config.set("theme_sombre", bool(sombre))
    config.sauver()
    _construire()


# ==============================================================================
#  Polices
# ==============================================================================
def base_font(size=10, weight="normal"):
    return (FONT_FAMILY, size, weight)


def emoji_font(size=12):
    """Police dédiée aux emojis : glyphes couleur, pas de rendu monochrome cassé."""
    return (EMOJI_FONT, size)


TITRE_XL = base_font(24, "bold")
TITRE_L = base_font(19, "bold")
TITRE_M = base_font(12, "bold")
CORPS_G = base_font(11)
CORPS = base_font(10)
PETIT = base_font(9)
STAT = base_font(22, "bold")
MONO = ("Consolas", 13)

# ==============================================================================
#  Les 8 catégories d'erreurs
# ==============================================================================
COULEURS_CATEGORIES = {
    "accord": "#DC2626", "conjugaison": "#D97706", "homophone": "#4F46E5",
    "orthographe": "#0EA5E9", "segmentation": "#15A34A", "ponctuation": "#C026D3",
    "majuscule": "#0284C7", "lexique": "#92400E",
}

LIBELLES_CATEGORIES = {
    "accord": "Accords", "conjugaison": "Conjugaison", "homophone": "Homophones",
    "orthographe": "Orthographe", "segmentation": "Segmentation",
    "ponctuation": "Ponctuation", "majuscule": "Majuscules", "lexique": "Lexique",
}

CATEGORIES = list(LIBELLES_CATEGORIES)

NIVEAUX_FLUENCE = {
    1: ("Niveau 1 — Débutant", SUCCESS),
    2: ("Niveau 2 — Facile", INFO),
    3: ("Niveau 3 — Intermédiaire", PRIMARY),
    4: ("Niveau 4 — Confirmé", WARNING),
    5: ("Niveau 5 — Expert", DANGER),
}

REPERES_MCLM = {"CP": 30, "CE1": 50, "CE2": 70, "CM1": 90, "CM2": 110, "6e": 120}


# ==============================================================================
#  Ces couleurs sont reprises telles quelles dans web/css/style.css
#  (variables CSS). theme.py reste la source de vérité pour le back-end :
#  couleurs des catégories, niveaux de fluence, repères MCLM.
# ==============================================================================
