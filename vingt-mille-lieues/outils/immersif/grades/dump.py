"""Affiche, sans les schémas SVG, les énigmes d'une variante (grades présents) et le texte des fiches : base de travail pour écrire les grades manquants.
    python vingt-mille-lieues/outils/immersif/grades/dump.py <jeu> [salle]"""
import json, os, re, sys
RACINE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
jeu = sys.argv[1]; num = int(sys.argv[2]) if len(sys.argv) > 2 else None
d = os.path.join(RACINE, "immersifs", jeu, "assets", "data")
E = json.load(open(os.path.join(d, "enigmes.json"), encoding="utf-8")); L = json.load(open(os.path.join(d, "lecons.json"), encoding="utf-8"))
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h or "")).strip()
lec = {l["id"]: l for l in L["lecons"]}
vus = set()
for s in E["escales"]:
    if num and s["numero"] != num: continue
    print(f"##### SALLE {s['numero']} {s['titre']} | {s.get('lieu','')} | mot {s.get('mot')}")
    for e in s["enigmes"]:
        print(f"=== {e['id']} {e['type']} « {e['titre']} » lecon={e['lecon']} niveaux={e.get('niveaux')} decor={e['decor']} perso={e['personnage_emetteur']}")
        for g in ("mousse", "matelot", "timonier", "lieutenant", "second"):
            if g in e:
                b = {k: v for k, v in e[g].items() if k not in ("dialogue",)}
                j = re.sub(r"<svg.*?</svg>", "<SVG/>", json.dumps(b, ensure_ascii=False), flags=re.S)
                print(" ", g, j)
    for e in s["enigmes"]:
        if e["lecon"] not in vus:
            vus.add(e["lecon"]); l = lec[e["lecon"]]
            print(f"--- FICHE {l['id']} : {l['titre']}\n  APPROFONDI: {txt(l.get('approfondi'))}\n  EXPERT: {txt(l.get('expert'))}")
