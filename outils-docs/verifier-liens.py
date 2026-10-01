# -*- coding: utf-8 -*-
"""Vérifie que les sites de référence cités dans le dépôt répondent encore (amélioration F3).

    python outils-docs/verifier-liens.py                 (tout le dépôt)
    python outils-docs/verifier-liens.py --jeu melanges  (un jeu)

Les liens sont relevés dans les fichiers publiés : A-VERIFIER.md, README.md, guides, données JSON
(sources des énigmes et des leçons, concours…), pages HTML et scripts. Chaque adresse est testée
une fois (même si elle est citée plusieurs fois), avec un délai maximal de 15 s.
Résultat : un résumé à l'écran et le rapport outils-docs/rapport-liens.md (non publié), qui dit
pour chaque lien en échec OÙ il est cité (fichier et ligne), pour le corriger.
  ✅ répond           ↪️ redirigé (répond, mais l'adresse a changé : à mettre à jour)
  ⚠️ à vérifier à la main (site qui refuse les robots, surcharge, délai dépassé)
  ❌ introuvable (page supprimée, site disparu)
Code de sortie 1 s'il y a au moins un lien ❌ (utilisable dans une tâche planifiée).
Aucune dépendance : Python 3 suffit. À lancer une fois par période, par exemple.
"""
import argparse, concurrent.futures, os, re, subprocess, sys, time, urllib.error, urllib.request
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = re.compile(r"https?://[^\s)\"'<>`\]]+")
IGNORER = re.compile(r"(127\.0\.0\.1|localhost|192\.168\.|\$\{|\{\{|example\.(com|org)|<ip>|xxx)", re.I)
ENTETES = {"User-Agent": "Mozilla/5.0 (verification des liens d'un projet scolaire ; escape-games-cm1-cm2)",
           "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8", "Accept-Language": "fr-FR,fr;q=0.9"}

def fichiers(jeu=None):
    sortie = subprocess.run(["git", "ls-files", "-z"], cwd=RACINE, capture_output=True, check=True).stdout.decode("utf-8")
    for f in sortie.split("\0"):
        if not f or not f.endswith((".md", ".json", ".html", ".js")): continue
        if f.startswith(("outils-tests/", "node_modules/")) or "/tests/" in f or f == "sw-fichiers.js": continue
        if jeu and not f.startswith(jeu + "/"): continue
        yield f

def relever(jeu=None):
    citations = {}
    for f in fichiers(jeu):
        try:
            lignes = open(os.path.join(RACINE, f), encoding="utf-8").read().splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for n, l in enumerate(lignes, 1):
            for u in URL.findall(l):
                u = u.rstrip(".,;:»*_").replace("&amp;", "&")
                if IGNORER.search(u) or len(u) < 12: continue
                citations.setdefault(u, []).append(f"{f}:{n}")
    return citations

def tester(url):
    def essai(methode):
        req = urllib.request.Request(url, headers=ENTETES, method=methode)
        with urllib.request.urlopen(req, timeout=15) as r:
            if methode == "GET": r.read(2048)
            return r.status, r.geturl()
    try:
        try:
            code, finale = essai("HEAD")
        except urllib.error.HTTPError as e:
            if e.code in (403, 404, 405, 429, 500, 501, 503): code, finale = essai("GET")   # certains sites refusent HEAD
            else: raise
        redirige = finale.rstrip("/") != url.rstrip("/") and finale.split("#")[0].rstrip("/") != url.split("#")[0].rstrip("/")
        return ("↪️" if redirige else "✅"), code, finale if redirige else ""
    except urllib.error.HTTPError as e:
        return ("❌" if e.code in (404, 410) else "⚠️"), e.code, ""
    except Exception as e:
        msg = str(getattr(e, "reason", e))
        mort = any(x in msg for x in ("Name or service not known", "getaddrinfo failed", "nodename nor servname", "No address associated"))
        return ("❌" if mort else "⚠️"), 0, msg[:80]

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--jeu"); ap.add_argument("--max", type=int, default=0)
    a = ap.parse_args()
    cit = relever(a.jeu)
    urls = sorted(cit)[: a.max or None]
    print(f"{len(urls)} adresses différentes à tester…")
    t0, res = time.time(), {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for u, r in zip(urls, ex.map(tester, urls)):
            res[u] = r
    compte = {k: sum(1 for r in res.values() if r[0] == k) for k in ("✅", "↪️", "⚠️", "❌")}
    print(f"✅ {compte['✅']}  ↪️ {compte['↪️']}  ⚠️ {compte['⚠️']}  ❌ {compte['❌']}   ({time.time() - t0:.0f} s)")
    lignes = [f"# Rapport des liens externes — {time.strftime('%d/%m/%Y %H:%M')}", "",
              f"{len(urls)} adresses testées : ✅ {compte['✅']} · ↪️ {compte['↪️']} redirigées · ⚠️ {compte['⚠️']} à vérifier · ❌ {compte['❌']} introuvables.", ""]
    for symb, titre in (("❌", "Introuvables : à remplacer"), ("↪️", "Redirigées : mettre à jour l'adresse"), ("⚠️", "À vérifier à la main")):
        l = [(u, r) for u, r in res.items() if r[0] == symb]
        if not l: continue
        lignes += [f"## {symb} {titre}", "", "| Adresse | Réponse | Citée dans |", "|---|---|---|"]
        for u, r in l:
            rep = f"{r[1] or ''} {('→ ' + r[2]) if symb == '↪️' else r[2]}".strip()
            lignes.append(f"| {u} | {rep} | {', '.join(cit[u][:4])}{' …' if len(cit[u]) > 4 else ''} |")
        lignes.append("")
    with open(os.path.join(RACINE, "outils-docs", "rapport-liens.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lignes) + "\n")
    for u, r in res.items():
        if r[0] == "❌": print(f"  ❌ {u}  ({', '.join(cit[u][:2])})")
    print("Rapport complet : outils-docs/rapport-liens.md")
    sys.exit(1 if compte["❌"] else 0)

if __name__ == "__main__":
    main()
