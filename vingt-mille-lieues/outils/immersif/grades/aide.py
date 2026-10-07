"""Constructeurs de blocs de grade (mousse, lieutenant, second) pour les énigmes d'une variante immersive.

Chaque fonction renvoie un bloc au format du moteur (voir vingt-mille-lieues/assets/data/enigmes.json) :
type, consigne, indices, [justification], et les données propres au type. Le champ `dialogue` est ajouté par
appliquer.py (repris du grade voisin). Les bonnes réponses sont écrites dans l'ordre voulu ; le moteur remélange.
"""
import re


def J(question, bonne, autres, pos=0):
    """Justification (lieutenant, second) : `bonne` est une phrase de la fiche ; `autres` : leurres crédibles."""
    opts = list(autres)
    opts.insert(pos, bonne)
    return {"question": question, "options": opts, "bonne": pos}


def _b(type_, consigne, indices, j, **donnees):
    b = {"type": type_, **donnees, "consigne": consigne, "indices": list(indices)}
    if j:
        b["justification"] = j
    return b


def tri(consigne, cols, cartes, indices, j=None):
    return _b("tri", consigne, indices, j, colonnes=[{"id": i, "titre": t} for i, t in cols],
              cartes=[{"txt": t, "col": c} for t, c in cartes])


def qcm(consigne, qs, indices, j=None):
    return _b("qcm", consigne, indices, j, questions=[
        {"q": q, "options": o, "bonne": bn, "explication": ex} for q, o, bn, ex in qs])


def vf(consigne, affs, indices, j=None):
    return _b("vraifaux", consigne, indices, j, affirmations=[
        {"txt": t, "vrai": v, "explication": ex} for t, v, ex in affs])


def ordre(consigne, items, indices, j=None):
    """items : (texte) ou (texte, sous) dans le BON ordre."""
    out = []
    for i, it in enumerate(items, 1):
        d = {"txt": it[0] if isinstance(it, tuple) else it, "rang": i}
        if isinstance(it, tuple):
            d["sous"] = it[1]
        out.append(d)
    return _b("ordre", consigne, indices, j, items=out)


def assoc(consigne, paires, indices, j=None):
    return _b("association", consigne, indices, j, paires=[{"g": g, "d": d} for g, d in paires])


def intrus(consigne, cartes, indices, j=None):
    return _b("intrus", consigne, indices, j, cartes=[{"txt": t, "intrus": bool(x)} for t, x in cartes])


def trous(consigne, texte, etiquettes, indices, j=None):
    return _b("trous", consigne, indices, j, texte="<p>" + texte + "</p>", etiquettes=list(etiquettes))


def lettres(consigne, cible, texte, indices, j=None):
    return _b("lettres", consigne, indices, j, cible=list(cible), texte="<p>" + texte + "</p>")


def code(consigne, champs, indices, j=None):
    """champs : (libelle, valeur, longueur) ou (libelle, valeur, longueur, numerique)."""
    ch = []
    for c in champs:
        d = {"libelle": c[0], "valeur": c[1], "longueur": c[2]}
        if len(c) > 3:
            d["numerique"] = c[3]
        ch.append(d)
    return _b("code", consigne, indices, j, champs=ch)


def svg_de(enigme, grade):
    """Le schéma SVG de la consigne d'un grade existant (pour le réutiliser dans une autre consigne)."""
    m = re.search(r"<svg.*?</svg>", enigme[grade]["consigne"], re.S)
    return m.group(0) if m else ""


MORSE = {"A": "•—", "C": "—•—•", "E": "•", "H": "••••", "I": "••", "L": "•—••", "N": "—•", "O": "———", "P": "•——•",
         "Q": "——•—", "R": "•—•", "S": "•••", "T": "—", "U": "••—", "V": "•••—"}
_TD = 'style="padding:4px 8px;border:1px solid #9fb3c8"'


def morse(mots, lettres_table):
    """HTML d'un message en Morse (un éclat court •, long —) et du tableau de lettres proposé."""
    msg = '<span style="display:inline-block;width:2.2em"></span>'.join(
        '<span style="white-space:nowrap">' + "   ".join(MORSE[c] for c in m) + "</span>" for m in mots)
    tab = "".join(f'<td {_TD}><b>{c}</b> <span style="font-size:1.15em;letter-spacing:2px">{MORSE[c]}</span></td>' for c in lettres_table)
    return ('<div class="message-morse" style="font-size:1.45em;letter-spacing:3px;text-align:center;background:#0f1a2b;color:#ffd23f;'
            f'padding:10px;border-radius:10px;margin:8px 0">{msg}</div>'
            f'<table class="tableau-releves" style="margin:8px auto;border-collapse:collapse;text-align:left"><tr>{tab}</tr></table>')
