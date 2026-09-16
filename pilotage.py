"""pilotage.py — Analyse avancée pour l'enseignant (section 7 Phase I).

S'appuie sur les séances de correction réelles (database.seances_correction),
dont les erreurs sont stockées en JSON {categorie: nb} dans detail_avant.

- heatmap(classe_id)   : grille élève × catégorie (moyenne d'erreurs / séance).
- regressions()        : élèves dont les résultats récents se dégradent.
- besoins_nouveaux()   : compteur pour le badge de nouveautés.
"""
import database as db
from theme import CATEGORIES


def _moyennes_par_categorie(seances):
    """Moyenne d'erreurs par séance, pour chaque catégorie."""
    if not seances:
        return {c: 0 for c in CATEGORIES}
    tot = {c: 0 for c in CATEGORIES}
    for s in seances:
        for c, v in (s.get("detail_avant") or {}).items():
            if c in tot:
                tot[c] += v
    return {c: round(tot[c] / len(seances), 1) for c in CATEGORIES}


def heatmap(classe_id=None):
    eleves = db.liste_eleves(classe_id=classe_id)
    lignes, colonnes = [], {c: [] for c in CATEGORIES}
    for e in eleves:
        sc = db.seances_correction(eleve_id=e["id"])
        if not sc:
            continue
        moy = _moyennes_par_categorie(sc)
        for c in CATEGORIES:
            colonnes[c].append(moy[c])
        lignes.append({"eleve_id": e["id"], "nom": e["prenom"], "valeurs": moy})
    moyennes = {c: round(sum(v) / len(v), 1) if v else 0
                for c, v in colonnes.items()}
    return {"categories": CATEGORIES, "eleves": lignes, "moyennes": moyennes}


def _total_par_seance(seances):
    if not seances:
        return 0
    return sum(sum((s.get("detail_avant") or {}).values()) for s in seances) / len(seances)


def regressions(classe_id=None):
    """
    Signale un élève quand la moyenne d'erreurs de ses 2 séances récentes
    dépasse celle des précédentes d'au moins +25 % ET +2 erreurs.
    """
    signales = []
    for e in db.liste_eleves(classe_id=classe_id):
        sc = db.seances_correction(eleve_id=e["id"])
        if len(sc) < 4:
            continue
        sc = sorted(sc, key=lambda s: s.get("date_seance") or "")
        anciennes, recentes = sc[:-2], sc[-2:]
        passe = _total_par_seance(anciennes)
        recent = _total_par_seance(recentes)
        if recent >= passe * 1.25 and recent - passe >= 2:
            ma, mr = _moyennes_par_categorie(anciennes), _moyennes_par_categorie(recentes)
            pire, ecart = None, 0
            for c in CATEGORIES:
                d = mr[c] - ma[c]
                if d > ecart:
                    ecart, pire = d, c
            signales.append({
                "eleve_id": e["id"], "nom": e["prenom"], "classe": e["classe_nom"],
                "avant": round(passe, 1), "apres": round(recent, 1), "categorie": pire,
            })
    signales.sort(key=lambda x: x["apres"] - x["avant"], reverse=True)
    return signales


def besoins_nouveaux(config):
    total = len(regressions())
    if total == 0:
        return {"nombre": 0, "message": "Aucun décrochage détecté."}
    mot = "élève" if total == 1 else "élèves"
    return {"nombre": total, "message": f"{total} {mot} en régression à surveiller."}
