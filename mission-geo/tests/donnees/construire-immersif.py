# -*- coding: utf-8 -*-
"""Construit (ou reconstruit) la version immersive de « Mission géographique » : immersifs/mission-geo/.

    python mission-geo/tests/donnees/construire-immersif.py
Enchaîne : gen_escales.py (données au format des salles) → migrer-jeu.py (moteur de « Vingt mille lieues », thème
theme-immersif.json) → appliquer-grades.py (5 grades) → appliquer-narration.py → finitions propres au jeu (carnet d'indices,
textes du coffre, reprise des parties) → embarquer-donnees.py → test-immersif.js → test-reprise.js.
Tout est régénérable : on ne modifie jamais immersifs/mission-geo/ à la main (sauf les médias, conservés d'une construction à l'autre).
Variable NODE_PATH : dossier qui contient jsdom (par défaut ~/node_modules).
"""
import json, os, re, shutil, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
OUT = os.path.join(RACINE, "vingt-mille-lieues", "outils", "immersif")
SRC = os.path.join(OUT, "sources", "mission-geo")
DEST = os.path.join(RACINE, "immersifs", "mission-geo")
GARDER = ["assets/images/decors", "assets/images/personnages", "assets/videos", "assets/audio", "assets/medias-depart"]
env = dict(os.environ, PYTHONIOENCODING="utf-8", NODE_PATH=os.environ.get("NODE_PATH", os.path.join(os.path.expanduser("~"), "node_modules")))
py = sys.executable

# Indices du carnet de la version classique (mission-geo/js/donnees/sessions-p*.js), redonnés à la fin de chaque escale.
INDICES = {
    1: {"type": "nombre", "symbole": "etoile", "valeur": 5, "libelle": "Nombre de lettres de la ville de rendez-vous"},
    2: {"type": "nombre", "symbole": "cercle", "valeur": 7, "libelle": "Nombre de continents sur le planisphère"},
    3: {"type": "nombre", "symbole": "nuage", "valeur": 7, "libelle": "Total des trois densités calculées"},
    4: {"type": "fait", "texte": "Le pays recherché se trouve en Amérique latine.", "libelle": "Confidence d'une source à Besançon"},
    5: {"type": "fait", "texte": "Le pays recherché est situé dans l'hémisphère nord.", "libelle": "Remarque d'un skieur au refuge"},
}
SYMBOLES = {"etoile": "l'étoile", "cercle": "le cercle", "nuage": "le nuage"}
PERIODES = {1: "Période 1", 2: "Période 1", 3: "Période 1", 4: "Période 1", 5: "Période 1"}


def go(titre, cmd, cwd=RACINE, fin=4, obligatoire=True):
    print("==", titre, flush=True)
    r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    sortie = (r.stdout + r.stderr).strip().splitlines()
    print("\n".join(sortie[-fin:]), flush=True)
    if r.returncode and obligatoire:
        sys.exit(f"✖ échec : {titre}")
    return r.returncode


def lire(n):
    return json.load(open(os.path.join(DEST, "assets", "data", n), encoding="utf-8"))


def ecrire(n, o):
    json.dump(o, open(os.path.join(DEST, "assets", "data", n), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)


def texte_indice(n):
    i = INDICES[n]
    if i["type"] == "nombre":
        return f"Indice pour le carnet de mission : sous {SYMBOLES[i['symbole']]}, écrivez {i['valeur']} ({i['libelle'].lower()})."
    return f"Indice pour le carnet de mission : {i['texte']}"


def finitions():
    E, DL = lire("enigmes.json"), lire("dialogues.json")
    mots = []
    for s in E["escales"]:
        n = s["numero"]
        s["matiere"], s["periode_conseillee"] = "Géographie", PERIODES.get(n, "")
        s["mot_origine"] = f"Le mot-clé de la séance {n}, à recopier sur la fiche de mission."
        mots.append(s["mot"])
        for e in s["enigmes"]:
            e["episode_du_roman"] = f"Séance {n} du livret « Mission géographique » (Année A)"
        f = DL["fin_escale"][str(n)]
        f["texte"] = f"Notez le mot de cette séance, {s['mot']} : il servira à ouvrir le coffre. " + texte_indice(n)
    DL["accueil"]["texte"] = ("Bienvenue au bureau du Professeur Atlas. Une valise pleine d'informations secrètes a été volée. Séance après séance, vous allez suivre "
                              "sa trace à travers la France, puis le monde. Chaque séance réussie vous donne un mot pour le coffre et un indice pour votre carnet de mission.")
    DL["coffre"]["texte"] = ("Mon coffre ne s'ouvre qu'avec le mot de chaque séance, dans l'ordre. Ensemble, ils résument ce que vous avez appris : "
                             "votre COMMUNE fait partie de territoires EMBOÎTÉS ; la DENSITÉ distingue la campagne de la ville ; la ville vit surtout du secteur TERTIAIRE ; "
                             "la montagne vit du TOURISME.")
    DL["cinematiques"]["fin"]["plans"][0]["texte"] = ("Le coffre est ouvert. Vous connaissez maintenant le territoire où vous vivez, ses villes, ses campagnes et ses montagnes. "
                                                      "Mais la valise, elle, a quitté l'Europe. Gardez précieusement votre carnet : la mission continue à la séance suivante.")
    ecrire("enigmes.json", E)
    ecrire("dialogues.json", DL)
    P = lire("personnages.json")
    P["personnages"]["atlas"]["court"] = "Professeur Atlas"
    ecrire("personnages.json", P)
    # reprise des parties : bloc placé avant « window.VML_JEU = » dans js/jeu-config.js
    esc = {s["numero"]: {"mot": s["mot"], "titre": s["titre"], "ids": [e["id"] for e in s["enigmes"]], "indice": INDICES.get(s["numero"])} for s in E["escales"]}
    cfg_p = os.path.join(DEST, "js", "jeu-config.js")
    cfg = open(cfg_p, encoding="utf-8").read()
    cle = json.loads(re.search(r"window\.VML_JEU = (\{[\s\S]*\});", cfg).group(1))["prefixeStockage"] + "_partie"
    bloc = open(os.path.join(ICI, "reprise-immersif.js"), encoding="utf-8").read().replace("__ESCALES__", json.dumps(esc, ensure_ascii=False)).replace("__CLE__", json.dumps(cle))
    i = cfg.index("window.VML_JEU =")
    open(cfg_p, "w", encoding="utf-8", newline="\n").write(cfg[:i] + bloc + "\n" + cfg[i:])
    json.loads(re.search(r"window\.VML_JEU = (\{[\s\S]*\});", open(cfg_p, encoding="utf-8").read()).group(1))   # l'objet reste lisible
    r = os.path.join(DEST, "MIGRATION-RAPPORT.md")
    t = open(r, encoding="utf-8").read()
    note = ("> **Construit par `mission-geo/tests/donnees/construire-immersif.py`** : les points 2, 3 et 5 ci-dessous sont faits (narration, phrases "
            "des personnages, 5 grades). Restent : zones des décors (après dépôt des images), médias (photos Wikimedia Commons pour les lieux réels), "
            "voix mp3. Ne pas modifier ce dossier à la main : relancer le script (voir mission-geo/REFONTE-IMMERSIVE.md, § 3).\n\n")
    t = t.replace("\n\n", "\n\n" + note, 1)
    open(r, "w", encoding="utf-8", newline="\n").write(t)
    print("finitions :", ", ".join(mots))


def main():
    go("données (gen_escales.py)", [py, os.path.join(ICI, "gen_escales.py"), os.path.join(SRC, "assets", "data")], fin=1)
    garde = DEST + ".medias-gardes"
    if os.path.isdir(DEST):
        for g in GARDER:
            if os.path.isdir(os.path.join(DEST, g)) and any(os.scandir(os.path.join(DEST, g))):
                shutil.copytree(os.path.join(DEST, g), os.path.join(garde, g), dirs_exist_ok=True)
    go("migration (migrer-jeu.py)", [py, os.path.join(OUT, "migrer-jeu.py"), SRC, "--vers", DEST, "--theme", os.path.join(ICI, "theme-immersif.json"), "--force"], fin=2)
    if os.path.isdir(garde):
        shutil.copytree(garde, DEST, dirs_exist_ok=True)
        shutil.rmtree(garde)
    go("grades (appliquer-grades.py)", [py, os.path.join(OUT, "appliquer-grades.py"), "mission-geo"], fin=30)
    go("narration (appliquer-narration.py)", [py, os.path.join(OUT, "appliquer-narration.py"), "mission-geo"], fin=1)
    finitions()
    go("données embarquées", [py, os.path.join(DEST, "outils", "embarquer-donnees.py")], fin=1)
    go("test immersif", ["node", os.path.join(DEST, "tests", "test-immersif.js")], fin=3)
    go("test de la reprise des parties", ["node", os.path.join(ICI, "test-reprise.js")], fin=8)


if __name__ == "__main__":
    main()
