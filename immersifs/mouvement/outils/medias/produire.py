#!/usr/bin/env python3
"""Produit des images et des vidéos pour le jeu avec la SOURCE de votre choix (sources-medias.json).

Rien n'est généré sans que vous le demandiez, et dans la limite de plafonds : 4 images et 0 vidéo par défaut
(--max-images, --max-videos). Les propositions sont écrites dans assets/medias-proposes/ (jamais publié) ;
vous choisissez ensuite (outils/choisir-medias.html) puis déposez avec importer-image.py.

Exemples :
  python produire.py --liste-sources                                   sources connues et état des clés
  python produire.py --essai --id decor-imprimerie                     montre l'appel prévu, sans rien appeler
  python produire.py --id decor-imprimerie --variantes 2               image avec la source par défaut
  python produire.py --source openai-images --id portrait-tommaso      autre source, pour cette fois
  python produire.py --types video --id video-transition-e1 --max-videos 1 --depart assets/medias-depart/transition-e1.jpg
  python produire.py --types video --id video-transition-e1 --max-videos 1 --depart-decor imprimerie   (image de départ prise dans le décor déposé)
  python produire.py --reprendre                                       reprend les vidéos dont le travail est déjà créé

La clé d'API : variable d'environnement indiquée par la source (ex. AGNES_API_KEY), ou ligne NOM=valeur dans cles-api.local.
Elle n'est jamais affichée ni enregistrée.
"""
import argparse, csv, json, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import medias_lib as L

JOBS = os.path.join(L.SORTIE, "jobs.json")


def lire_csv():
    chemin = os.path.join(L.JEU, "medias.csv")
    if not os.path.isfile(chemin):
        raise L.ErreurSource("medias.csv introuvable à la racine du jeu.")
    with open(chemin, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def dimensions(txt):
    try:
        w, h = [int(x) for x in txt.split(" ")[0].replace("×", "x").split("x")]
        return w, h
    except Exception:
        return 1920, 1080


def prompt_de(ligne, supplement=""):
    return (ligne.get("prompt_fr") or "").strip() + (" " + supplement if supplement else "")


def references_pour(s_img, ligne, essai):
    """Images de référence d'une image à produire, dans la forme attendue par la source (URL publique, base64…)."""
    spec = (s_img.get("image") or {}).get("references") or {}
    mode, refus = spec.get("mode", "urls"), spec.get("formats_refuses", [])
    if mode == "aucune":
        return []
    res = []
    for r in [x.strip().split(" ")[0] for x in (ligne.get("reference_ou_depart") or "").replace(";", ",").split(",") if x.strip()]:
        p = os.path.join(L.JEU, r)
        if not os.path.isfile(p):
            continue
        if os.path.splitext(p)[1].lower().lstrip(".") in refus:
            print(f"· référence ignorée ({os.path.basename(p)} : format refusé par « {s_img['_nom']} »)")
            continue
        res.append(L.en_data_uri(p) if mode in ("base64", "data-uri") else ("(url publique)" if essai else L.url_publique_verifiee(p)))
    return res[: spec.get("max", 4)]


def jobs_lire():
    return json.load(open(JOBS, encoding="utf-8")) if os.path.isfile(JOBS) else {}


def jobs_ecrire(d):
    os.makedirs(L.SORTIE, exist_ok=True)
    json.dump(d, open(JOBS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def prochain_numero(base, ext):
    k = 1
    while os.path.exists(os.path.join(L.SORTIE, f"{base}-v{k}.{ext}")):
        k += 1
    return k


def etat_sources():
    d = L.lire_sources()
    print("Source par défaut : image =", d["defaut"].get("image"), "· vidéo =", d["defaut"].get("video"))
    for nom, s in d["sources"].items():
        c = s.get("cle") or {}
        etat = "pas de clé nécessaire" if not c.get("env") else ("clé définie" if L.cle_de(s) else ("clé non définie" + (" (facultative : proxy possible)" if c.get("optionnelle") else "")))
        genres = ", ".join(g for g in ("image", "video") if s.get(g)) or ("dossier : " + s.get("dossier", "") if s.get("type") == "dossier" else "—")
        print(f"  - {nom:<24} {genres:<22} {etat}   {s.get('cout', '')}")


def main():
    L.charger_cles_locales()
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--liste-sources", action="store_true")
    a.add_argument("--essai", action="store_true", help="affiche les appels prévus sans rien appeler")
    a.add_argument("--source", help="source pour les images ET les vidéos")
    a.add_argument("--source-image"), a.add_argument("--source-video")
    a.add_argument("--id", action="append", help="identifiant(s) de medias.csv (ex. decor-imprimerie)")
    a.add_argument("--types", choices=["image", "video"], help="restreint aux images ou aux vidéos")
    a.add_argument("--variantes", type=int, default=1, help="propositions par image (1 à 4)")
    a.add_argument("--max-images", type=int, default=4)
    a.add_argument("--max-videos", type=int, default=0)
    a.add_argument("--depart", help="fichier image de départ de la vidéo (sera publié pour le service)")
    a.add_argument("--depart-decor", help="identifiant d'un décor déjà déposé, pris comme image de départ")
    a.add_argument("--fin", help="fichier image d'arrivée de la vidéo (facultatif)")
    a.add_argument("--secondes", type=int, default=8)
    a.add_argument("--supplement", default="", help="texte ajouté au prompt")
    a.add_argument("--reprendre", action="store_true")
    o = a.parse_args()
    try:
        if o.liste_sources:
            return etat_sources()
        lignes = lire_csv()
        voulus = set(o.id or [])
        cibles = [l for l in lignes if (not voulus or l["id"] in voulus) and (not o.types or (l["type"].startswith("vid") == (o.types == "video")))]
        if voulus and not cibles:
            raise L.ErreurSource("Identifiant(s) introuvable(s) dans medias.csv : " + ", ".join(sorted(voulus)))
        if not voulus and not o.reprendre:
            raise L.ErreurSource("Indiquez au moins un --id (rien n'est généré en bloc), ou --reprendre. --liste-sources pour voir les sources.")
        s_img = L.source(o.source_image or o.source, "image")
        s_vid = L.source(o.source_video or o.source, "video")
        faites_i = faites_v = 0
        jobs = jobs_lire()
        if o.reprendre:
            for jid, j in list(jobs.items()):
                if j.get("fini"):
                    continue
                s = L.source(j["source"])
                url, _ = L.produire_video(s, "", None, None, 8, reprise=j["job"])
                cible = os.path.join(L.SORTIE, j["fichier"])
                L.telecharger(url, cible)
                j["fini"] = True
                jobs_ecrire(jobs)
                L.journal(f"{j['fichier']} : vidéo reçue (reprise)")
            return
        for l in cibles:
            est_video = l["type"].startswith("vid")
            if est_video:
                if faites_v >= o.max_videos:
                    print(f"· {l['id']} : plafond de vidéos atteint ({o.max_videos} ; --max-videos N pour autoriser).")
                    continue
                depart = o.depart
                if not depart and o.depart_decor:
                    src = os.path.join(L.JEU, "assets", "images", "decors", o.depart_decor + ".webp")
                    if not os.path.isfile(src):
                        raise L.ErreurSource(f"Décor déposé introuvable : {src}")
                    depart = os.path.join(L.JEU, "assets", "medias-depart", l["id"].replace("video-", "") + ".jpg")
                    if not o.essai:
                        L.convertir_image(src, depart, 1280, 720, 82)
                if not depart and l.get("reference_ou_depart"):
                    cand = os.path.join(L.JEU, l["reference_ou_depart"].split(",")[0].strip().split(" ")[0])
                    depart = cand if os.path.isfile(cand) else None
                if not depart:
                    par_convention = os.path.join(L.JEU, "assets", "medias-depart", l["id"].replace("video-", "", 1) + ".jpg")
                    depart = par_convention if os.path.isfile(par_convention) else None
                if not depart:
                    raise L.ErreurSource(f"{l['id']} : il faut une image de départ (--depart <fichier> ou --depart-decor <id>).")
                dep_val = fin_val = None
                if o.essai:
                    print(f"[essai] vidéo {l['id']} avec « {s_vid['_nom']} » · départ : {os.path.relpath(depart, L.JEU)} · {o.secondes} s\n        prompt : {prompt_de(l, o.supplement)[:160]}…")
                    faites_v += 1
                    continue
                dep_val = L.image_de_depart(s_vid, depart)
                fin_val = L.image_de_depart(s_vid, os.path.join(L.JEU, o.fin)) if o.fin else None
                nom_fichier = f"{l['id']}-v{prochain_numero(l['id'], 'mp4')}.mp4"
                url, ident = L.produire_video(s_vid, prompt_de(l, o.supplement), dep_val, fin_val, o.secondes)
                jobs[ident] = {"source": s_vid["_nom"], "job": ident, "fichier": nom_fichier, "fini": False}
                jobs_ecrire(jobs)
                L.telecharger(url, os.path.join(L.SORTIE, nom_fichier))
                jobs[ident]["fini"] = True
                jobs_ecrire(jobs)
                L.journal(f"{nom_fichier} : vidéo reçue (source {s_vid['_nom']})")
                faites_v += 1
            else:
                for k in range(max(1, min(4, o.variantes))):
                    if faites_i >= o.max_images:
                        print(f"· {l['id']} : plafond d'images atteint ({o.max_images} ; --max-images N pour autoriser).")
                        break
                    refs = references_pour(s_img, l, o.essai)
                    if o.essai:
                        print(f"[essai] image {l['id']} avec « {s_img['_nom']} » · {len(refs)} référence(s) · ratio {l.get('ratio') or '16:9'}\n        prompt : {prompt_de(l, o.supplement)[:160]}…")
                        faites_i += 1
                        continue
                    octets = L.produire_image(s_img, prompt_de(l, o.supplement), l.get("ratio") or "16:9", None, [r for r in refs if r], negatif=l.get("negatif", ""))
                    brut = os.path.join(L.SORTIE, f"_brut-{l['id']}.img")
                    os.makedirs(L.SORTIE, exist_ok=True)
                    open(brut, "wb").write(octets)
                    w, h = dimensions(l.get("dimensions", ""))
                    sortie = os.path.join(L.SORTIE, f"{l['id']}-v{prochain_numero(l['id'], 'webp')}.webp")
                    L.convertir_image(brut, sortie, w, h)
                    os.remove(brut)
                    L.journal(f"{os.path.basename(sortie)} : image reçue (source {s_img['_nom']})")
                    faites_i += 1
        if not o.essai:
            print("\nTerminé. Propositions dans", os.path.relpath(L.SORTIE, L.JEU), "— comparez dans outils/choisir-medias.html, puis déposez :")
            print("  python outils/medias/importer-image.py <proposition> --decor <id>   (ou --portrait / --depart / --video)")
    except L.ErreurSource as e:
        sys.exit("✖ " + L.masquer(e))


if __name__ == "__main__":
    main()
