#!/usr/bin/env python3
"""Génère un mp3 par réplique pour chaque escape game, selon voix.json.
Usage :  python generer_voix.py            -> tous les jeux
         python generer_voix.py chateau-fort   -> un seul jeu
         python generer_voix.py --test         -> 1 réplique par personnage (écoute rapide)
Sortie : <jeu>/assets/audio/<perso>-<empreinte>.mp3 + <jeu>/assets/audio/manifest.json
Les fichiers déjà générés sont conservés (relancer ne refait que le nouveau texte)."""
import asyncio, hashlib, json, re, subprocess, sys
from pathlib import Path
import edge_tts

RACINE = Path(__file__).resolve().parent.parent
CAST = json.loads((Path(__file__).parent / "voix.json").read_text(encoding="utf-8"))

def nettoyer(t):                      # texte parlé = texte HTML sans balises
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def empreinte(t):
    return hashlib.sha1(t.encode("utf-8")).hexdigest()[:10]

def repliques(o, out):                # toute entrée {perso, texte} du JSON
    if isinstance(o, dict):
        if isinstance(o.get("perso"), str) and isinstance(o.get("texte"), str):
            out.append((o["perso"], nettoyer(o["texte"])))
        for v in o.values(): repliques(v, out)
    elif isinstance(o, list):
        for v in o: repliques(v, out)

async def une(jeu, perso, texte, cfg, dossier, manifest, sem, voix_ok):
    cle = empreinte(texte + cfg["voice"] + cfg["rate"] + cfg["pitch"] + cfg.get("fx", ""))
    fichier = f"{perso}-{cle}.mp3"
    chemin = dossier / fichier
    manifest[f"{perso}|{empreinte(texte)}"] = fichier
    if chemin.exists(): return
    voix = cfg["voice"] if cfg["voice"] in voix_ok else CAST["_defaut"]["voice"]
    if voix != cfg["voice"]: print(f"  ! voix {cfg['voice']} absente, remplacée ({perso})")
    async with sem:
        brut = chemin.with_suffix(".tmp.mp3")
        await edge_tts.Communicate(texte, voix, rate=cfg["rate"], pitch=cfg["pitch"]).save(str(brut))
    if cfg.get("fx"):
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",str(brut),"-af",cfg["fx"],str(chemin)], check=True)
        brut.unlink()
    else:
        brut.rename(chemin)
    print(f"  ok {fichier}")

async def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    test = "--test" in sys.argv
    voix_ok = {v["ShortName"] for v in await edge_tts.list_voices()}
    sem = asyncio.Semaphore(4)
    for f in sorted(RACINE.glob("*/assets/data/dialogues.json")):
        jeu = f.parts[-4]
        if args and jeu not in args: continue
        reps, vus = [], set()
        repliques(json.loads(f.read_text(encoding="utf-8")), reps)
        reps = [(p, t) for p, t in reps if t and (p, t) not in vus and not vus.add((p, t))]
        if test:
            vu, tmp = set(), []
            for p, t in reps:
                if p not in vu: vu.add(p); tmp.append((p, t))
            reps = tmp
        print(f"== {jeu} : {len(reps)} répliques")
        dossier = f.parent.parent / "audio"; dossier.mkdir(exist_ok=True)
        mf = {}
        cast = CAST.get(jeu, {})
        await asyncio.gather(*[une(jeu, p, t, {**CAST["_defaut"], **cast.get(p, {})}, dossier, mf, sem, voix_ok) for p, t in reps])
        (dossier / "manifest.json").write_text(json.dumps(mf, ensure_ascii=False, indent=1), encoding="utf-8")

asyncio.run(main())
