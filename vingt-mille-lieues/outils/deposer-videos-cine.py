#!/usr/bin/env python3
"""Dépose les vidéos de cinématique proposées (assets/medias-proposes/video-<nom>-v1.mp4) dans assets/videos/<nom>.mp4,
sans piste audio, et les branche sur le premier plan de la cinématique du même nom (dialogues.json et sources/).
Usage : python vingt-mille-lieues/outils/deposer-videos-cine.py   (puis assembler-escales.py, construire-prompts.py)"""
import glob, json, os, subprocess
JEU = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
noms = sorted(os.path.basename(f)[6:-7] for f in glob.glob(os.path.join(JEU, "assets/medias-proposes/video-*-v1.mp4")))
noms = [n for n in noms if n.startswith("fin-e") or n.startswith("transition-e")]
def regler(chemin, cle, nom):
    d = json.load(open(chemin, encoding="utf-8"))
    c = (d.get("dialogues", d) if "dialogues" in d else d)
    c = c.get("cinematiques", {}).get(cle)
    if not c: return False
    c.pop("video", None); c["plans"][0]["video"] = nom
    json.dump(d, open(chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=2); open(chemin, "a").write("\n")
    return True
for n in noms:
    sortie = os.path.join(JEU, "assets/videos", n + ".mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(JEU, f"assets/medias-proposes/video-{n}-v1.mp4"), "-an", "-c:v", "copy", sortie], check=True)
    cibles = [os.path.join(JEU, "assets/data/dialogues.json")] + glob.glob(os.path.join(JEU, "sources/escale-*.json"))
    print(n, "→", sum(regler(c, n, n) for c in cibles), "fichier(s) mis à jour")
