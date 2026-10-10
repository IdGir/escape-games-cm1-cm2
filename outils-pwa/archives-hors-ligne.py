# -*- coding: utf-8 -*-
"""Archive zip par jeu, pour jouer SANS SERVEUR NI INTERNET (amélioration N9).

    python outils-pwa/archives-hors-ligne.py               (tous les jeux)
    python outils-pwa/archives-hors-ligne.py melanges      (un seul)
    options : --sortie <dossier>   (défaut : archives-hors-ligne/, non publié)
              --dossier            (écrit l'arborescence décompressée au lieu du zip : pour les tests)

Chaque archive <jeu>-hors-ligne.zip contient :
  JOUER.html          à ouvrir d'un double-clic (renvoie vers <jeu>/index.html)
  LISEZ-MOI.txt       mode d'emploi pour l'enseignant
  <jeu>/              le jeu (fichiers suivis par git, sans les tests)
  commun/             le tronc commun du moteur (sans les tests)
Ouvert d'un double-clic (adresse file://), un navigateur refuse de lire les fichiers .json :
le jeu retombait alors sur ses quelques « énigmes de secours ». Ici, toutes les données
(assets/data/*.json, assets/medias/medias.json) sont EMBARQUÉES dans <jeu>/js/donnees-embarquees.js,
chargé en premier par les pages du jeu dans l'archive : les 15 à 20 énigmes, les leçons, le
quizz final et les leçons imprimables fonctionnent sans serveur.
Seuls les fichiers suivis par git sont copiés (rien de privé : clés, journaux…).
Sans effet sur le dépôt lui-même. Publication automatique : .github/workflows/archives-hors-ligne.yml
(release « hors-ligne » du dépôt GitHub).
"""
import io, json, os, re, subprocess, sys, zipfile

ICI = os.path.dirname(os.path.abspath(__file__)); RACINE = os.path.dirname(ICI)
STOCKES = (".mp4", ".webm", ".m4v", ".mp3", ".ogg", ".jpg", ".jpeg", ".png", ".webp", ".gif", ".woff2", ".pdf", ".zip")
PAGES = ("index.html", "lecons-imprimables.html")

SHIM = r"""/* DONNÉES EMBARQUÉES — fichier GÉNÉRÉ par outils-pwa/archives-hors-ligne.py (N9).
   Version hors ligne sans serveur : ouvert d'un double-clic (file://), le navigateur refuse
   de lire les .json ; on les sert ici, depuis la mémoire. Ne pas modifier à la main. */
(function(){
  var D = %s;
  window.__DONNEES_EMBARQUEES = D;
  var origine = window.fetch;
  window.fetch = function(url){
    try{
      var u = new URL(String(url && url.url || url), location.href).href.split(/[?#]/)[0];
      for(var k in D){
        if(u.slice(-(k.length + 1)) === "/" + k){
          var v = D[k];
          return Promise.resolve({ ok: true, status: 200, url: u,
            headers: { get: function(){ return "application/json"; } },
            json: function(){ return Promise.resolve(JSON.parse(JSON.stringify(v))); },
            text: function(){ return Promise.resolve(JSON.stringify(v)); } });
        }
      }
    }catch(e){}
    return origine ? origine.apply(this, arguments) : Promise.reject(new TypeError("fetch indisponible"));
  };
})();
"""

def suivis():
    sortie = subprocess.run(["git", "ls-files", "-z"], cwd=RACINE, capture_output=True, check=True).stdout
    return [f for f in sortie.decode("utf-8").split("\0") if f]

def jeux_publiables():
    return sorted(j for j in os.listdir(RACINE)
                  if os.path.isfile(os.path.join(RACINE, j, "index.html")) and os.path.isdir(os.path.join(RACINE, j, "assets", "data"))
                  and j != "vingt-mille-lieues")

def titre_de(jeu):
    try:
        t = open(os.path.join(RACINE, jeu, "index.html"), encoding="utf-8").read()
        m = re.search(r"<title>(.*?)</title>", t, re.S)
        return re.sub(r"\s+", " ", m.group(1)).strip() if m else jeu
    except OSError:
        return jeu

def lisez_moi(jeu, titre):
    return f"""{titre} — version hors ligne, sans serveur
{"=" * 60}

1. Décompressez l'archive (clic droit → « Extraire tout… »), par exemple sur le bureau
   ou sur une clé USB. Ne lancez pas le jeu depuis l'intérieur du fichier zip.
2. Double-cliquez sur JOUER.html : le jeu s'ouvre dans le navigateur (Chrome, Edge ou Firefox).
   Aucune connexion internet, aucun serveur, rien à installer.

Ce qui fonctionne : toutes les énigmes (CM1, CM2, Découverte), les leçons, les décors,
les vidéos, les voix des personnages (voix du navigateur), le quizz, les impressions
(leçons A4, fiche de mission, corrigés), le mode individuel et le mode duel,
la reprise de partie (y compris par fichier).

Ce qui demande le mode « classe » (lancer.bat, dans le dépôt complet) : le tableau de
bord enseignant en direct (prof.html), l'écran de classement, le regroupement des
résultats sur l'ordinateur de l'enseignant. Les liens vers les autres jeux de la
collection ne mènent nulle part dans cette archive : ils sont en ligne sur
https://idgir.github.io/escape-games-cm1-cm2/

Crédits des images et vidéos : {jeu}/assets/medias/CREDITS-medias.md (si présent)
et les mentions affichées dans le jeu.
"""

def jouer_html(jeu, titre):
    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>{titre}</title>
<meta http-equiv="refresh" content="0; url={jeu}/index.html"></head>
<body style="font:18px/1.5 Georgia,serif;text-align:center;padding:40px">
<p><a href="{jeu}/index.html">▶ Ouvrir « {titre} »</a></p>
<p style="font-size:14px;color:#555">Si rien ne se passe, cliquez sur le lien ci-dessus.</p>
</body></html>
"""

def donnees_embarquees(jeu, fichiers):
    d = {}
    for f in fichiers:
        rel = f[len(jeu) + 1:]
        if (rel.startswith("assets/data/") and rel.endswith(".json")) or rel == "assets/medias/medias.json":
            with open(os.path.join(RACINE, f), encoding="utf-8-sig") as h:
                d[rel] = json.load(h)
    return SHIM % json.dumps(d, ensure_ascii=False, separators=(",", ":"))

def injecter(html):
    balise = '<script src="js/donnees-embarquees.js"></script>\n'
    i = html.find("<script")
    return html[:i] + balise + html[i:] if i >= 0 else html.replace("</head>", balise + "</head>")

def contenu_archive(jeu, tous):
    """Liste de (chemin dans l'archive, octets ou chemin source)."""
    racine_zip = f"{jeu}-hors-ligne/"
    fichiers = [f for f in tous if f.startswith(jeu + "/") and "/tests/" not in f]
    commun = [f for f in tous if f.startswith("commun/") and not f.startswith("commun/tests/")]
    titre = titre_de(jeu)
    elements = [(racine_zip + "JOUER.html", jouer_html(jeu, titre).encode("utf-8")),
                (racine_zip + "LISEZ-MOI.txt", lisez_moi(jeu, titre).replace("\n", "\r\n").encode("utf-8")),
                (racine_zip + jeu + "/js/donnees-embarquees.js", donnees_embarquees(jeu, fichiers).encode("utf-8"))]
    for f in fichiers + commun:
        src = os.path.join(RACINE, f)
        if not os.path.isfile(src): continue
        if f in (f"{jeu}/{p}" for p in PAGES):
            elements.append((racine_zip + f, injecter(open(src, encoding="utf-8").read()).encode("utf-8")))
        else:
            elements.append((racine_zip + f, src))
    return elements

def ecrire_zip(chemin, elements):
    with zipfile.ZipFile(chemin, "w") as z:
        for nom, data in elements:
            mode = zipfile.ZIP_STORED if nom.lower().endswith(STOCKES) else zipfile.ZIP_DEFLATED
            if isinstance(data, bytes): z.writestr(zipfile.ZipInfo(nom, (2026, 1, 1, 0, 0, 0)), data, compress_type=mode)
            else: z.write(data, nom, compress_type=mode)

def ecrire_dossier(base, elements):
    for nom, data in elements:
        cible = os.path.join(base, *nom.split("/"))
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        if isinstance(data, bytes):
            with open(cible, "wb") as h: h.write(data)
        else:
            with open(data, "rb") as s, open(cible, "wb") as h: h.write(s.read())

def main(args):
    sortie = os.path.join(RACINE, "archives-hors-ligne")
    if "--sortie" in args:
        i = args.index("--sortie"); sortie = os.path.abspath(args[i + 1]); del args[i:i + 2]
    dossier = "--dossier" in args
    choix = [a for a in args if not a.startswith("--")] or jeux_publiables()
    os.makedirs(sortie, exist_ok=True)
    tous = suivis()
    for jeu in choix:
        if not os.path.isfile(os.path.join(RACINE, jeu, "index.html")):
            print(f"  ✗ {jeu} : jeu introuvable"); continue
        elements = contenu_archive(jeu, tous)
        if dossier:
            ecrire_dossier(sortie, elements); print(f"  ✓ {jeu} : {len(elements)} fichiers → {os.path.join(sortie, jeu + '-hors-ligne')}")
        else:
            chemin = os.path.join(sortie, f"{jeu}-hors-ligne.zip")
            ecrire_zip(chemin, elements)
            print(f"  ✓ {jeu}-hors-ligne.zip : {len(elements)} fichiers, {os.path.getsize(chemin) / 1e6:.1f} Mo")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
