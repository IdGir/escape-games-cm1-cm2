# -*- coding: utf-8 -*-
"""Sous-titres systématiques des vidéos des jeux (amélioration B5).

    python outils-medias/sous-titres.py              (tous les jeux)
    python outils-medias/sous-titres.py melanges     (un seul)
    python outils-medias/sous-titres.py --verifier   (liste les vidéos sans sous-titres, ne crée rien)

Le moteur charge déjà automatiquement assets/videos/<nom>.vtt à côté de <nom>.mp4 :
cinématiques (intro, final) et décors filmés (salle1…, etape1…), et Mission géographique.
Les vidéos des jeux n'ont pas de paroles (les voix viennent de la synthèse vocale, déjà
sous-titrée) : les sous-titres disent CE QUE MONTRE la vidéo et signalent les bruits
d'ambiance, pour les élèves sourds ou malentendants et quand le son est coupé.

D'où vient le texte, par ordre de priorité :
  1. <nom>.txt à côté de la vidéo (une ligne = un sous-titre) — pour une vidéo avec paroles ;
  2. outils-medias/sous-titres-cinematiques.json (intro, final) ;
  3. décors filmés : le lieu de la salle (assets/data/dialogues.json, champ « lieu ») ;
     Mission géographique : la légende de la séance (js/…) ;
  4. sinon : rien (la vidéo est signalée).
Les bandes-annonces (muettes, avec cartons écrits) et les portraits animés ne sont pas concernés.

Un .vtt écrit par ce script commence par « NOTE sous-titres.py » : il est régénéré à chaque
passage. Pour le modifier à la main sans qu'il soit remplacé, supprimez cette ligne NOTE.
Aucune dépendance. Si ffmpeg est installé, les vidéos au son muet sont reconnues
(pas de mention « bruits d'ambiance »).
"""
import json, os, re, shutil, struct, subprocess, sys, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__)); RACINE = os.path.dirname(ICI)
MARQUE = "NOTE sous-titres.py"
EXCLUS = ("bande-annonce",)

def boites(f, debut, fin):
    """Parcourt les boîtes MP4 (taille, type, début du contenu, fin)."""
    pos = debut
    while pos + 8 <= fin:
        f.seek(pos); taille, typ = struct.unpack(">I4s", f.read(8)); entete = 8
        if taille == 1: taille = struct.unpack(">Q", f.read(8))[0]; entete = 16
        elif taille == 0: taille = fin - pos
        if taille < entete: break
        yield typ.decode("latin-1"), pos + entete, pos + taille
        pos += taille

def infos_mp4(chemin):
    """(durée en secondes, piste son présente) lues dans l'en-tête MP4, sans dépendance."""
    duree, son = None, False
    with open(chemin, "rb") as f:
        fin = os.fstat(f.fileno()).st_size
        for typ, d, e in boites(f, 0, fin):
            if typ != "moov": continue
            for t2, d2, e2 in boites(f, d, e):
                if t2 == "mvhd":
                    f.seek(d2); v = f.read(1)[0]
                    if v == 1: f.seek(d2 + 20); ech, du = struct.unpack(">IQ", f.read(12))
                    else: f.seek(d2 + 12); ech, du = struct.unpack(">II", f.read(8))
                    duree = du / ech if ech else None
                elif t2 == "trak":
                    for t3, d3, e3 in boites(f, d2, e2):
                        if t3 != "mdia": continue
                        for t4, d4, e4 in boites(f, d3, e3):
                            if t4 == "hdlr":
                                f.seek(d4 + 8)
                                if f.read(4) == b"soun": son = True
    return duree, son

def muet(chemin):
    """True si ffmpeg mesure un son quasi nul ; None si ffmpeg est absent."""
    if not shutil.which("ffmpeg"): return None
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", chemin, "-af", "volumedetect", "-vn", "-f", "null", "-"],
                       capture_output=True, text=True, errors="replace")
    m = re.search(r"max_volume:\s*(-?[\d.]+) dB", r.stderr)
    return m is not None and float(m.group(1)) < -50

def nettoyer(t):
    """Retire émojis et symboles décoratifs, espaces en trop."""
    t = "".join(c for c in t if unicodedata.category(c)[0] in "LNPZ" or c in "°'’«»—–-")
    return re.sub(r"\s+", " ", t).strip(" —-")

def phrases(t):
    return [p.strip() for p in re.split(r"(?<=[.!?…])\s+", t) if p.strip()]

def horodatage(s):
    h, s = divmod(s, 3600); m, s = divmod(s, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"

def vtt(repliques, duree, ambiance):
    """Répartit les répliques sur la durée de la vidéo (au moins 1,5 s chacune)."""
    duree = max(duree or 5.0, 1.5)
    n = len(repliques); pas = duree / n
    lignes = ["WEBVTT", "", MARQUE + " — régénéré à chaque passage ; supprimez cette ligne pour le garder tel quel.", ""]
    for i, r in enumerate(repliques):
        texte = ("[Bruits d'ambiance]\n" if ambiance and i == 0 else "") + r
        lignes += [str(i + 1), f"{horodatage(i * pas)} --> {horodatage(duree if i == n - 1 else (i + 1) * pas)}", texte, ""]
    return "\n".join(lignes)

def lieux_salles(jeu):
    f = os.path.join(RACINE, jeu, "assets", "data", "dialogues.json")
    if not os.path.exists(f): return {}
    d = json.load(open(f, encoding="utf-8"))
    return {s.get("num"): nettoyer(s.get("lieu") or s.get("titre") or "") for s in d.get("salles", [])}

def legendes_mission_geo():
    res = {}
    for dos, _, fichiers in sorted(os.walk(os.path.join(RACINE, "mission-geo", "js"))):
        for n in sorted(fichiers):
            if n.endswith(".js"):
                txt = open(os.path.join(dos, n), encoding="utf-8").read()
                for b, l in re.findall(r'base:\s*"([^"]+)"\s*,\s*legende:\s*"([^"]+)"', txt): res.setdefault(b, l)
    return res

def texte_pour(jeu, base, dossier, cine, lieux, legendes):
    txt = os.path.join(dossier, base + ".txt")
    if os.path.exists(txt):
        return [l.strip() for l in open(txt, encoding="utf-8") if l.strip()], "fichier .txt"
    if base in cine.get(jeu, {}):
        return phrases(cine[jeu][base]), "cinématique"
    m = re.fullmatch(r"(?:salle|etape)(\d+)", base)
    if m and lieux.get(int(m.group(1))):
        return [lieux[int(m.group(1))]], "lieu de la salle"
    if jeu == "mission-geo" and base in legendes:
        return [legendes[base]], "légende de la séance"
    return None, None

def main(args):
    verifier = "--verifier" in args
    choix = [a for a in args if not a.startswith("--")]
    cine = json.load(open(os.path.join(ICI, "sous-titres-cinematiques.json"), encoding="utf-8"))
    legendes = legendes_mission_geo()
    jeux = choix or sorted(j for j in os.listdir(RACINE) if os.path.isdir(os.path.join(RACINE, j, "assets", "videos"))
                           and os.path.exists(os.path.join(RACINE, j, "index.html")) and j != "vingt-mille-lieues")
    crees = gardes = manquants = 0
    for jeu in jeux:
        dossier = os.path.join(RACINE, jeu, "assets", "videos")
        if not os.path.isdir(dossier): continue
        lieux = lieux_salles(jeu)
        for nom in sorted(os.listdir(dossier)):
            base, ext = os.path.splitext(nom)
            if ext.lower() not in (".mp4", ".webm") or base.startswith(EXCLUS): continue
            cible = os.path.join(dossier, base + ".vtt")
            if os.path.exists(cible) and MARQUE not in open(cible, encoding="utf-8").read():
                gardes += 1; continue   # écrit ou retouché à la main : on n'y touche pas
            repliques, origine = texte_pour(jeu, base, dossier, cine, lieux, legendes)
            if not repliques:
                manquants += 1; print(f"  ⚠ {jeu}/{base}{ext} : aucun texte (ajoutez {base}.txt à côté de la vidéo)"); continue
            if verifier:
                if not os.path.exists(cible): manquants += 1; print(f"  ⚠ {jeu}/{base}{ext} : pas de sous-titres")
                continue
            duree, son = infos_mp4(os.path.join(dossier, nom)) if ext.lower() == ".mp4" else (None, False)
            ambiance = son and muet(os.path.join(dossier, nom)) is not True
            contenu = vtt(repliques, duree, ambiance)
            ancien = open(cible, encoding="utf-8").read() if os.path.exists(cible) else None
            if ancien != contenu:
                with open(cible, "w", encoding="utf-8", newline="\n") as f: f.write(contenu)
                crees += 1; print(f"  ✓ {jeu}/{base}.vtt ({origine}, {duree or 0:.0f} s{', bruits d’ambiance' if ambiance else ''})")
    print(f"\n{crees} sous-titre(s) écrit(s), {gardes} gardé(s) tels quels (retouchés à la main), {manquants} vidéo(s) sans texte.")
    return 1 if (verifier and manquants) else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
