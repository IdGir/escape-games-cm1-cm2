# -*- coding: utf-8 -*-
# Lancement depuis la racine du dépôt : python chateau-fort/tests/test_json.py
# Contrôles statiques des données de chateau-fort/ : JSON valides, sans clé dupliquée,
# liens énigme → leçon, leçons toutes citées, règles du cahier des charges, absence d'emoji.
import json, sys, re, os
from collections import Counter
R = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
echecs = 0
def ok(c, m):
    global echecs
    print(("  ok  " if c else "  ÉCHEC  ") + m)
    if not c: echecs += 1

def sans_doublon(paires):
    cles = [k for k, _ in paires]
    d = [k for k, n in Counter(cles).items() if n > 1]
    if d: raise ValueError("clé dupliquée : " + ", ".join(d))
    return dict(paires)

data = {}
for f in ["enigmes", "dialogues", "lecons", "evaluations"]:
    p = os.path.join(R, "assets/data", f + ".json")
    try:
        data[f] = json.load(open(p, encoding="utf-8"), object_pairs_hook=sans_doublon)
        ok(True, f"{f}.json valide, sans clé dupliquée")
    except Exception as e:
        ok(False, f"{f}.json : {e}")
E, D, L, EV = data["enigmes"], data["dialogues"], data["lecons"], data["evaluations"]
ids_lecons = {l["id"] for l in L["lecons"]}
citees = set()
types = Counter()
for s in E["salles"]:
    seq = [e["type"] for e in s["enigmes"]]
    ok(all(a != b for a, b in zip(seq, seq[1:])), f"salle {s['num']} : pas deux types consécutifs identiques ({', '.join(seq)})")
    for niv in ("CM1", "CM2"):
        l = [e for e in s["enigmes"] if not e.get("niveaux") or niv in e["niveaux"]]
        ok(len(l) == (3 if niv == "CM1" else 4), f"salle {s['num']} {niv} : {len(l)} énigmes")
        manip = [e for e in l if e["type"] in ("ordre", "plan", "tri")]
        ok(bool(manip), f"salle {s['num']} {niv} : manipulation ({', '.join(e['id'] for e in manip)})")
    for e in s["enigmes"]:
        types[e["type"]] += 1
        ok(e.get("lecon") in ids_lecons, f"{e['id']} → leçon « {e.get('lecon')} » existe")
        citees.add(e.get("lecon"))
        for k in ("consigne", "correction", "source", "indices"):
            ok(bool(e.get(k)), f"{e['id']} : champ {k}")
        ind = e["indices"]
        nivs = [n.lower() for n in (e.get("niveaux") or ["CM1", "CM2"])]
        ok(all(len(ind.get(n, ind.get("commun", []))) == 3 for n in nivs), f"{e['id']} : 3 indices par niveau")
        # cohérence des données
        for n in nivs:
            d = e.get(n) or e.get("commun")
            ok(d is not None, f"{e['id']} : données {n}")
            if e["type"] == "trous":
                reps = re.findall(r"\[\[(.+?)\]\]", d["texte"])
                ok(all(r in d["etiquettes"] for r in reps), f"{e['id']} {n} : toutes les réponses sont des étiquettes")
            if e["type"] == "plan" and d.get("etiquettes"):
                ok(all(c["reponse"] in d["etiquettes"] for c in d["cases"]), f"{e['id']} {n} : réponses du plan présentes")
            if e["type"] == "ordre":
                ok(sorted(i["rang"] for i in d["items"]) == list(range(1, len(d["items"]) + 1)), f"{e['id']} {n} : rangs 1..n")
            if e["type"] == "intrus":
                ok(sum(1 for c in d["cartes"] if c["intrus"]) == 1, f"{e['id']} {n} : un seul intrus")
            if e["type"] == "lettres":
                ok(len(re.findall(r"data-l=", d["texte"])) == len(d["cible"]), f"{e['id']} : autant de lettres cachées que de cibles")
ok(len(types) >= 7, f"{len(types)} types d'énigmes utilisés (au moins 7) : {dict(types)}")
ok(citees == ids_lecons, "chaque leçon est citée par au moins une énigme")
ok([s["motCle"] for s in D["salles"]] == ["PIERRE", "REMPARTS", "SEIGNEUR", "VILLAGE", "REDEVANCES"], "mots-clés des 5 salles")
ok(all(len(EV["quizz_final"][n]) == 5 for n in ("CM1", "CM2")), "quizz final : 5 questions par niveau")
ok(len(EV["qcm"]["CM1"]) == 10 and len(EV["qcm"]["CM2"]) == 12, "QCM imprimable : 10 / 12 questions")
for l in L["lecons"]:
    ok(l["contenu"].get("cm1") and l["contenu"].get("cm2") and l.get("objectifs") and l.get("lexique") and l.get("sources"),
       f"leçon {l['id']} : cm1, cm2, objectifs, lexique, sources")
    ok(bool(l.get("schema") or l.get("frise")), f"leçon {l['id']} : schéma ou frise")
    mots = len(re.sub(r"<[^>]+>", " ", l["contenu"]["cm2"]).split())
    annexes = sum(len((m["mot"] + " " + m["def"]).split()) for m in l["lexique"]) + len(l.get("document", {}).get("contenu", "").split())
    ok(220 <= mots + annexes <= 600, f"leçon {l['id']} : {mots} + {annexes} mots en CM2 (3 à 4 min de lecture à 9-11 ans)")
# Pas d'emoji dans les contenus élèves
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-⇿]")
def textes(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("svg",): continue
            yield from textes(v)
    elif isinstance(o, list):
        for v in o: yield from textes(v)
    elif isinstance(o, str): yield o
for nom, obj in (("enigmes", E), ("dialogues", D), ("lecons", L), ("evaluations", EV)):
    trouves = [t for t in textes(obj) if EMOJI.search(t.replace("▲", "").replace("▼", ""))]
    ok(not trouves, f"{nom}.json : aucun emoji" + (f" ({trouves[0][:60]})" if trouves else ""))
print("\n" + (f"{echecs} échec(s)" if echecs else "TOUT EST VERT"))
sys.exit(1 if echecs else 0)
