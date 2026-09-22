# Contrôle des données JSON (clés dupliquées, leçons, types, emoji). python3 objets-techniques/tests/test-donnees.py
import json, re, sys, os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","assets","data")+os.sep
err=[]
def sans_doublon(paires):
    cles=[k for k,_ in paires]
    for k in set(cles):
        if cles.count(k)>1: err.append("clé dupliquée : "+k)
    return dict(paires)
J={f:json.load(open(D+f,encoding='utf-8'),object_pairs_hook=sans_doublon) for f in ["enigmes.json","dialogues.json","lecons.json","evaluations.json"]}
E,DI,L,EV=J["enigmes.json"],J["dialogues.json"],J["lecons.json"],J["evaluations.json"]
ids={l["id"] for l in L["lecons"]}; citees=set()
types=set(); emoji=re.compile("[\U0001F300-\U0001FAFF☀-➿]")
for s in E["salles"]:
    for niv in ("CM1","CM2"):
        es=[e for e in s["enigmes"] if "niveaux" not in e or niv in e["niveaux"]]
        if len(es)!=(3 if niv=="CM1" else 4): err.append(f"salle {s['num']} {niv}: {len(es)} énigmes")
        for a,b in zip(es,es[1:]):
            if a["type"]==b["type"]: err.append(f"types consécutifs {a['id']} {b['id']}")
        if not any(e["type"] in ("ordre","plan","tri") for e in es): err.append(f"pas de manipulation salle {s['num']} {niv}")
    for e in s["enigmes"]:
        types.add(e["type"])
        for c in ("consigne","indices","correction","source","lecon"):
            if not e.get(c): err.append(f"{e['id']} sans {c}")
        ind=e["indices"]; 
        for v in ([ind] if isinstance(ind,list) else ind.values()):
            if len(v)!=3: err.append(f"{e['id']} : {len(v)} indices")
        if e["lecon"] not in ids: err.append(f"{e['id']} : leçon inconnue {e['lecon']}")
        citees.add(e["lecon"])
        txt=json.dumps({k:e[k] for k in ("consigne","correction","indices")},ensure_ascii=False)
        if emoji.search(txt): err.append(f"{e['id']} : emoji dans consigne/correction/indices")
        for k in ("cm1","cm2","commun"):
            d=e.get(k)
            if not d: continue
            if e["type"]=="lettres":
                l=re.findall(r"data-l='(.)'",d["texte"])
                if l!=d["cible"]: err.append(f"{e['id']} lettres {l}")
            if e["type"]=="trous":
                for r in re.findall(r"\[\[(.+?)\]\]",d["texte"]):
                    if r not in d["etiquettes"]: err.append(f"{e['id']} trou sans étiquette {r}")
            if e["type"]=="ordre":
                if sorted(i["rang"] for i in d["items"])!=list(range(1,len(d["items"])+1)): err.append(f"{e['id']} rangs")
            if e["type"]=="intrus" and sum(c["intrus"] for c in d["cartes"])!=1: err.append(f"{e['id']} intrus")
            if e["type"]=="tri":
                cols={c["id"] for c in d["colonnes"]}
                if any(c["col"] not in cols for c in d["cartes"]): err.append(f"{e['id']} tri col")
            if e["type"]=="qcm":
                for q in d["questions"]:
                    if not 0<=q["bonne"]<len(q["options"]): err.append(f"{e['id']} qcm bonne")
            if e["type"]=="plan":
                reps=[c["reponse"] for c in d["cases"]]
                if len(set(reps))!=len(reps): err.append(f"{e['id']} plan réponses en double")
if len(types)<7: err.append(f"types : {len(types)}")
for i in ids-citees: err.append("leçon jamais citée : "+i)
for s in DI["salles"]:
    for k in ("dialogue_intro","dialogue_reussite","dialogue_fin"):
        if k in s and emoji.search(s[k]["texte"]): err.append(f"emoji dialogue salle {s['num']}")
    if s["dialogue_intro"]["perso"] not in DI["personnages"]: err.append("perso inconnu")
for l in L["lecons"]:
    for n in ("cm1","cm2"):
        c=re.sub("<[^>]+>","",l["contenu"][n])
        if emoji.search(c): err.append(f"emoji leçon {l['id']}")
    for c in ("objectifs","lexique","sources","schema"):
        if not l.get(c): err.append(f"leçon {l['id']} sans {c}")
mots=[s["motCle"] for s in DI["salles"]]
if mots!=["BESOIN","FONCTION","MATÉRIAU","ÉNERGIE","NOTICE"]: err.append("mots-clés")
for niv in ("CM1","CM2"):
    if len(EV["quizz_final"][niv])!=5: err.append("quizz")
print("types utilisés :", sorted(types), len(types))
print("ERREURS :", err if err else "aucune")
sys.exit(1 if err else 0)
