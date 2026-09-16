"""phonetique.py — « Comment ça sonne ? » plutôt que « comment ça s'écrit ».

Quand un élève écrit « éléfan », « ortografe » ou « oizo », aucun dictionnaire
alphabétique ne peut l'aider : il cherche à la lettre E, et le mot commence
bien par un E… mais la suite est fausse. Ce module traduit une suite de lettres
en une suite de SONS. Deux mots qui se prononcent pareil obtiennent le même
code, quelle que soit leur orthographe :

    éléfan   → ELEFA      éléphant → ELEFA      (même code : trouvé !)
    oizo     → WAZO       oiseau   → WAZO
    ortografe→ ORTOGRAF   orthographe → ORTOGRAF

Le codage est volontairement « grossier » : on regroupe les sons proches
(é/è/ê → E, o/au/eau → O) parce qu'un enfant qui hésite sur l'orthographe
hésite justement sur ces nuances-là.

Aucune dépendance : tout est en Python pur, tout marche hors ligne.
"""
import unicodedata

# --------------------------------------------------------------------------
#  Alphabet de sortie (un caractère = un son)
#
#   A E I O U    voyelles simples        Y = [y] (u de « lune »)
#   Q = [ø/œ]    (eu, œu)                W = [wa] (oi)
#   1 = [ɛ̃]      (in, ain, ein, un)      2 = [ɑ̃] (an, en)   3 = [ɔ̃] (on)
#   S Z F V K G T D P B M N L R J        consonnes
#   C = [ʃ]      (ch)                    X = [ʒ] (j, ge)
#   H = [ɲ]      (gn)
# --------------------------------------------------------------------------

VOYELLES = set("aeiouyàâäéèêëîïôöùûü")


def _sans_accent(mot):
    return "".join(c for c in unicodedata.normalize("NFD", mot)
                   if unicodedata.category(c) != "Mn")


# Règles appliquées dans l'ordre : la première qui correspond gagne. On va du
# plus long au plus court, sinon « eau » serait mangé par « e ».
# Chaque règle : (motif, son, condition)
#   condition None       → toujours
#   condition "avant_ei" → seulement si la lettre suivante est e, i ou y
#   condition "sauf_ei"  → seulement si la lettre suivante n'est pas e, i ni y
#   condition "entre_voy"→ seulement entre deux voyelles
#   condition "final"    → seulement en fin de mot
#   condition "non_final"→ seulement ailleurs qu'en fin de mot
REGLES = [
    # --- Nasales : elles doivent passer AVANT les voyelles simples ---
    ("aient", "E", "final"),        # ils chantaient → CHATE
    ("eaient", "E", "final"),
    ("aien", "1", None),
    ("oin", "W1", "non_final_voy"),
    ("ain", "1", "non_final_voy"),
    ("ein", "1", "non_final_voy"),
    ("aim", "1", "non_final_voy"),
    ("eim", "1", "non_final_voy"),
    ("ien", "I2", "non_final_voy"),
    ("ian", "I2", "non_final_voy"),
    ("ion", "I3", "non_final_voy"),
    ("oun", "U2", "non_final_voy"),
    ("ent", "2", "final_verbe"),    # « ils chantent » : terminaison muette
    ("an", "2", "non_final_voy"),
    ("am", "2", "non_final_voy"),
    ("en", "2", "non_final_voy"),
    ("em", "2", "non_final_voy"),
    ("on", "3", "non_final_voy"),
    ("om", "3", "non_final_voy"),
    ("in", "1", "non_final_voy"),
    ("im", "1", "non_final_voy"),
    ("yn", "1", "non_final_voy"),
    ("ym", "1", "non_final_voy"),
    ("un", "1", "non_final_voy"),
    ("um", "3", "non_final_voy"),

    # --- Voyelle + « l mouillé » : travail, soleil, feuille, grenouille ---
    ("aill", "AJ", None),
    ("eill", "EJ", None),
    ("euill", "QJ", None),
    ("ouill", "UJ", None),
    ("ueill", "QJ", None),
    ("ail", "AJ", "final"),
    ("eil", "EJ", "final"),
    ("euil", "QJ", "final"),
    ("ouil", "UJ", "final"),

    # --- Groupes de voyelles ---
    ("eau", "O", None),
    ("aux", "O", "final"),
    ("eaux", "O", "final"),
    ("au", "O", None),
    ("oeu", "Q", None),
    ("œu", "Q", None),
    ("oe", "Q", None),
    ("œ", "Q", None),
    ("eu", "Q", None),
    ("ou", "U", None),
    ("oi", "W", None),
    ("oy", "WJ", None),
    ("ai", "E", None),
    ("ei", "E", None),
    ("ay", "EJ", None),
    ("ey", "EJ", None),
    ("uy", "YJ", None),

    # --- Consonnes composées ---
    ("sch", "C", None),
    ("ch", "C", None),
    ("ph", "F", None),
    ("gn", "H", None),
    ("th", "T", None),
    ("qu", "K", None),
    ("gu", "G", "avant_ei"),
    ("cqu", "K", None),
    ("cc", "K", "sauf_ei"),
    ("ck", "K", None),
    ("sc", "S", "avant_ei"),
    ("ti", "SI", "ti_prononce_si"),   # attention, nation, patience
    ("ill", "IJ", None),
    ("il", "IJ", "final_apres_voy"),  # travail, soleil

    # --- Consonnes simples avec conditions ---
    ("c", "S", "avant_ei"),
    ("ç", "S", None),
    ("c", "K", None),
    ("g", "X", "avant_ei"),
    ("g", "G", None),
    ("j", "X", None),
    ("s", "Z", "entre_voy"),
    ("s", "S", None),
    ("x", "KS", None),
    ("z", "Z", None),
    ("h", "", None),                  # toujours muet en français
    ("w", "V", None),
    ("y", "J", "entre_voy"),
    ("y", "I", None),

    # --- Voyelles simples ---
    ("a", "A", None),
    ("e", "E", None),
    ("i", "I", None),
    ("o", "O", None),
    ("u", "Y", None),

    # --- Consonnes restantes ---
    ("b", "B", None), ("d", "D", None), ("f", "F", None), ("k", "K", None),
    ("l", "L", None), ("m", "M", None), ("n", "N", None), ("p", "P", None),
    ("q", "K", None), ("r", "R", None), ("t", "T", None), ("v", "V", None),
]

# Terminaisons muettes : « chat », « souris », « grand », « nez »…
# « ent » n'y figure pas : dans « souvent », « argent », « moment », il se
# prononce. La tolérance du score suffit à rapprocher « chante » de « chantent ».
TERMINAISONS_MUETTES = ("es", "e", "s", "t", "x", "d", "z")

# Mots dont la prononciation défie toutes les règles. Il y en a peu, mais ce
# sont des mots très fréquents : autant les traiter directement.
EXCEPTIONS = {
    "femme": "FAM", "femmes": "FAM",
    "monsieur": "MESIQ", "messieurs": "MESIQ",
    "oignon": "OH3", "oignons": "OH3",
    "automne": "OTON", "automnes": "OTON",
    "second": "SEG3", "seconde": "SEG3", "secondes": "SEG3",
    "paon": "P2", "faon": "F2", "taon": "T2",
    "album": "ALBOM", "aquarium": "AKWARIOM",
    "fils": "FIS", "os": "OS", "ours": "URS", "sens": "S2S",
    "eu": "Y", "eue": "Y", "eus": "Y",
    "aiguille": "EGYIJ", "orgueil": "ORGQJ",
    "chorale": "KORAL", "chœur": "KQR", "choeur": "KQR",
    "technique": "TEKNIK", "orchestre": "ORKESTR",
}


def _prononce_si(mot, i):
    """« ti » se dit-il [si] ? (nation, patience — mais pas « partie »)."""
    suite = mot[i + 2:i + 4]
    return suite.startswith(("on", "en", "an", "el", "eu"))


def sons(mot):
    """Traduit un mot en sa suite de sons (chaîne de codes)."""
    m = _sans_accent((mot or "").lower().strip())
    # Les accents disparaissent APRÈS avoir servi : é/è/ê donnent tous [E],
    # ce qui est exactement ce qu'on veut pour retrouver un mot mal accentué.
    m = "".join(c for c in m if c.isalpha() or c in "'-")
    m = m.replace("'", "").replace("-", "")
    if not m:
        return ""
    if m in EXCEPTIONS:
        return EXCEPTIONS[m]

    # 1. Le g final après une nasale ne s'entend pas : sang, long, poing.
    if len(m) > 3 and m.endswith("g") and m[-2] == "n":
        m = m[:-1]

    # 2. On coupe la terminaison muette : « souris » → « souri »
    for fin in TERMINAISONS_MUETTES:
        if len(m) > len(fin) + 2 and m.endswith(fin):
            if fin in ("es", "e") and not m.endswith("ee"):
                m = m[:-len(fin)]
            elif fin in ("s", "x", "t", "d", "z"):
                m = m[:-1]
            break

    sortie, i, n = [], 0, len(m)
    while i < n:
        suivant = m[i + 1] if i + 1 < n else ""
        for motif, son, cond in REGLES:
            if not m.startswith(motif, i):
                continue
            apres = m[i + len(motif):i + len(motif) + 1]
            avant = m[i - 1] if i > 0 else ""
            fin_de_mot = (i + len(motif) == n)

            # Attention : une chaîne vide est « dans » toute chaîne. En fin de
            # mot, « apres » vaut "" — il faut donc le tester explicitement,
            # sans quoi « sang » verrait son g traité comme un g de « genou ».
            suit_ei = bool(apres) and apres in "eiy"
            if cond == "avant_ei" and not suit_ei:
                continue
            if cond == "sauf_ei" and suit_ei:
                continue
            if cond == "entre_voy" and not (avant in VOYELLES
                                            and bool(apres) and apres in VOYELLES):
                continue
            if cond == "final" and not fin_de_mot:
                continue
            if cond == "final_apres_voy" and not (fin_de_mot and avant in VOYELLES):
                continue
            if cond == "final_verbe" and not fin_de_mot:
                continue
            if cond == "non_final_voy" and apres in VOYELLES:
                continue          # « ane » : le n se prononce, pas de nasale
            if cond == "ti_prononce_si" and not _prononce_si(m, i):
                continue

            sortie.append(son)
            i += len(motif)
            break
        else:
            i += 1                # lettre inconnue : on l'ignore

    code = "".join(sortie)

    # 2. Deux consonnes identiques de suite ne s'entendent qu'une fois
    compact = []
    for c in code:
        if not compact or compact[-1] != c:
            compact.append(c)
    code = "".join(compact)

    # 3. Un E final ne s'entend pas (« table » se dit TABL)
    while len(code) > 2 and code.endswith("E"):
        code = code[:-1]
    return code


# --------------------------------------------------------------------------
#  Comparaison de deux mots
# --------------------------------------------------------------------------
def distance(a, b):
    """Distance de Levenshtein (nombre de modifications d'une chaîne à l'autre)."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    precedent = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        courant = [i]
        for j, cb in enumerate(b, 1):
            courant.append(min(precedent[j] + 1,        # suppression
                               courant[j - 1] + 1,      # insertion
                               precedent[j - 1] + (ca != cb)))  # substitution
        precedent = courant
    return precedent[-1]


# Sons que l'oreille confond facilement : leur substitution coûte moins cher.
PROCHES = [
    set("EI"), set("OU"), set("YU"), set("QE"), set("123"),
    set("SZ"), set("FV"), set("KG"), set("TD"), set("PB"),
    set("CX"), set("MN"), set("JI"), set("HN"),
]


def _cout_substitution(a, b):
    if a == b:
        return 0
    for groupe in PROCHES:
        if a in groupe and b in groupe:
            return 0.5           # confusion courante : on pardonne à moitié
    return 1


def distance_sons(a, b):
    """Comme distance(), mais indulgente sur les sons proches."""
    if a == b:
        return 0.0
    if not a or not b:
        return float(len(a or b))
    precedent = [float(x) for x in range(len(b) + 1)]
    for i, ca in enumerate(a, 1):
        courant = [float(i)]
        for j, cb in enumerate(b, 1):
            courant.append(min(precedent[j] + 1,
                               courant[j - 1] + 1,
                               precedent[j - 1] + _cout_substitution(ca, cb)))
        precedent = courant
    return precedent[-1]


def ressemblance(essai, mot, sons_essai=None, sons_mot=None):
    """Score de 0 à 100 : à quel point « mot » est ce que l'élève voulait écrire.

    On combine trois indices, du plus important au moins important :
      · la ressemblance des SONS (c'est le cœur : l'élève écrit ce qu'il entend)
      · la ressemblance des LETTRES (il a souvent une partie juste)
      · la différence de longueur (un mot deux fois plus long est suspect)
    """
    se = sons_essai if sons_essai is not None else sons(essai)
    sm = sons_mot if sons_mot is not None else sons(mot)
    if not se or not sm:
        return 0.0

    d_son = distance_sons(se, sm) / max(len(se), len(sm))
    e = _sans_accent((essai or "").lower())
    m = _sans_accent((mot or "").lower())
    d_lettre = distance(e, m) / max(len(e), len(m), 1)
    d_long = abs(len(e) - len(m)) / max(len(e), len(m), 1)

    score = 100 * (1 - (0.68 * d_son + 0.24 * d_lettre + 0.08 * d_long))
    if se == sm:
        score = max(score, 92)       # même prononciation : forcément pertinent
    return round(max(0.0, min(100.0, score)), 1)
