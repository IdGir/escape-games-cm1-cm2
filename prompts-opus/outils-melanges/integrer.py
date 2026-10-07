# -*- coding: utf-8 -*-
"""Intègre le jeu melanges/ au dépôt (reproduit le schéma du commit 91238f4).
Idempotent : ne fait rien sur un fichier déjà intégré.
Usage : python3 integrer.py <racine du dépôt>
Conserve les fins de ligne d'origine (CRLF ou LF) de chaque fichier."""
import sys, os, io

RACINE = sys.argv[1] if len(sys.argv) > 1 else "."

def lire(p):
    b = open(os.path.join(RACINE, p), "rb").read()
    crlf = b"\r\n" in b
    return b.decode("utf-8").replace("\r\n", "\n"), crlf

def ecrire(p, s, crlf):
    if crlf: s = s.replace("\n", "\r\n")
    open(os.path.join(RACINE, p), "wb").write(s.encode("utf-8"))

def patch(p, pairs, marqueur):
    s, crlf = lire(p)
    if marqueur in s:
        print("déjà intégré :", p); return
    for a, b in pairs:
        if a not in s:
            raise SystemExit("ÉCHEC %s : motif introuvable :\n%s" % (p, a[:200]))
        s = s.replace(a, b, 1)
    ecrire(p, s, crlf); print("intégré :", p)

# ---------- index.html (accueil) ----------
CARTE = '''
  <article class="jeu melanges">
    <div class="bandeau">
      <div class="icone">⚗️</div>
      <h2>Le Laboratoire de Madame Mélange</h2>
      <div class="meta">Sciences · masses, mélanges et séparation · 60 à 75 min · 15 énigmes en CM1, 20 en CM2</div>
    </div>
    <div class="corps">
      <p>L'apprentie de Madame Mélange a renversé toutes les fioles. Peser, observer, trier, filtrer, évaporer : cinq opérations à retrouver pour compléter le testament de la chimiste.</p>
      <a class="jouer" href="melanges/">▶ Jouer</a>
      <div class="liens">
        <a class="prof" href="melanges/prof.html" hidden>👨‍🏫 Tableau de bord</a>
        <a href="https://github.com/IdGir/escape-games-cm1-cm2/tree/escape-games/melanges#readme" target="_blank" rel="noopener">📘 Guide du jeu</a>
      </div>
    </div>
  </article>
</main>'''
patch("index.html", [
    ("--cst:#5b2b6b; --cst-2:#c9a227;", "--cst:#5b2b6b; --cst-2:#c9a227; --mel:#1f5f6b; --mel-2:#8e3b62;"),
    ("  .constitution .jouer{background:var(--cst)}",
     "  .constitution .jouer{background:var(--cst)}\n  .melanges .bandeau{background:linear-gradient(135deg,var(--mel),#0b2a30 60%,var(--mel-2))}\n  .melanges .jouer{background:var(--mel)}"),
    ("\n</main>", CARTE),
], "jeu melanges")
# ---------- serveur.py ----------
import re
s, crlf = lire("serveur.py")
if '"melanges"' not in s:
    s = re.sub(r'(for jeu in \((?:"[^"]+",\s*)*"[^"]+")\)', r'\1, "melanges")', s, count=1)
    lignes = s.split("\n")
    def apres_dernier(motif, nouvelle):
        idx = [k for k, l in enumerate(lignes) if motif in l]
        lignes.insert(idx[-1] + 1, nouvelle)
    apres_dernier('/".format(ip, PORT))', '    print("     Mélanges (sciences)   →  http://{}:{}/melanges/".format(ip, PORT))')
    apres_dernier('/prof.html".format(PORT))', '    print("     http://127.0.0.1:{}/melanges/prof.html".format(PORT))')
    s = "\n".join(lignes)
    ecrire("serveur.py", s, crlf); print("intégré : serveur.py")
else:
    print("déjà intégré : serveur.py")

# ---------- verifier.html ----------
CONSTRUCTEUR = '''async function construireMelanges(){
  const R = "melanges/";
  const [dial, lec, enig] = await Promise.all([
    json(R + "assets/data/dialogues.json"),
    json(R + "assets/data/lecons.json"),
    json(R + "assets/data/enigmes.json")
  ]);
  const lien = (n, niv, e) => `${R}?salle=${n}&niveau=${niv}` + (e ? "&enigme=" + e : "");
  const deux = n => [{ libelle: "CM1", url: lien(n, "CM1") }, { libelle: "CM2", url: lien(n, "CM2") }];
  const salles = dial.salles;
  const persoSalles = p => salles.filter(s => (s.dialogue_intro && s.dialogue_intro.perso === p) || (s.dialogue_fin && s.dialogue_fin.perso === p))
                                 .map(s => ({ libelle: "Salle " + s.num, url: lien(s.num, "CM2") }));
  /* Énigmes du niveau demandé, dans l'ordre où le jeu les présente */
  const enigmesDe = (num, niv) => {
    const b = (enig.salles || []).find(x => x.num === num);
    return b ? (b.enigmes || []).filter(e => !e.niveaux || e.niveaux.includes(niv)) : [];
  };
  /* Illustrations facultatives déclarées dans enigmes.json */
  const illustrations = [];
  (enig.salles || []).forEach(b => (b.enigmes || []).forEach(e => {
    if(!e.media || !e.media.base) return;
    const niv = (!e.niveaux || e.niveaux.includes("CM1")) ? "CM1" : "CM2";
    const rang = enigmesDe(b.num, niv).findIndex(x => x.id === e.id) + 1;
    illustrations.push(imageSeule(R + "assets/images/cartes/", e.media.base,
      `Énigme ${e.id} — ${e.titre}`,
      (e.media.legende || "Illustration facultative") + ". Sans fichier, l'énigme reste jouable.",
      EXT.image, [{ libelle: "Salle " + b.num + " · " + niv, url: lien(b.num, niv, rang) }]));
  }));

  return {
    id: "melanges", nom: "Le Laboratoire de Madame Mélange", R,
    defaut: "Sans fichier : décor dessiné",
    tests: ["CM1", "CM2"].map(niv => ({ titre: niv + " — " + salles.reduce((t,s)=>t+enigmesDe(s.num,niv).length,0) + " énigmes", liens: [
      ...salles.flatMap(s => [
        { libelle: s.num + ". " + s.titre + " (" + s.motCle + ")", url: lien(s.num, niv) },
        ...enigmesDe(s.num, niv).map((e, i) => ({ libelle: "   ↳ " + e.id + " " + e.titre + " (" + e.type + ")", url: lien(s.num, niv, i + 1) }))
      ]),
      { libelle: "🏁 Fin : testament, badges, quizz", url: lien(6, niv) }
    ]})),
    familles: [
      { titre: "Décors et cinématiques", slots: [
        decor(R, "intro", "Cinématique d'ouverture", "Plein écran au clic sur « Entrer dans le laboratoire ». Sautée si absente.", [{ libelle: "Accueil", url: R }]),
        ...salles.map(s => decor(R, "salle" + s.num, `Salle ${s.num} — ${s.titre}`,
          "Décor de fond de la salle" + (s.num === 1 ? ", et de l'écran d'accueil" : "") + ".", deux(s.num))),
        decor(R, "final", "Cinématique de fin", "Plein écran quand le testament est complet. Sautée si absente.", [{ libelle: "Salle 5", url: lien(5, "CM2") }])
      ]},
      { titre: "Personnages", slots: Object.entries(dial.personnages || {}).map(([cle, p]) =>
          personnage(R, cle, (p && p.nom) || cle, persoSalles(cle))) },
      { titre: "Illustrations d'énigmes (facultatives)", slots: illustrations }
    ],
    docs: [
      { libelle: "📘 Guide du jeu (énigmes et solutions)", url: lienGitHub(R + "README.md") },
      { libelle: "🎞️ Liste des médias", url: lienGitHub(R + "assets/README.md") },
      { libelle: "📖 Guide pédagogique", url: lienGitHub(R + "GUIDE-PEDAGOGIQUE.md") },
      { libelle: "🔎 Points à vérifier", url: lienGitHub(R + "A-VERIFIER.md") },
      { libelle: "▶ Écran d'accueil du jeu", url: R }
    ]
  };
}

async function construireTour(){'''
patch("verifier.html", [
    ("async function construireTour(){", CONSTRUCTEUR),
], "construireMelanges")
s, crlf = lire("verifier.html")
if '"melanges": construireMelanges' not in s:
    i = s.index("const ONGLETS = ["); j = s.index("\n];", i)
    s = s[:j].rstrip() + ',\n  { id: "melanges",      titre: "⚗️ Le Laboratoire de Madame Mélange" }' + s[j:]
    i = s.index("const CONSTRUCTEURS = {"); j = s.index("\n};", i)
    s = s[:j].rstrip() + ',\n  "melanges": construireMelanges' + s[j:]
    s = s.replace(",,", ",")
    ecrire("verifier.html", s, crlf); print("intégré : verifier.html (onglet)")

# ---------- README.md racine ----------
LIGNE = ("| ⚗️ | **Le Laboratoire de Madame Mélange** — Sciences, masses et mélanges | "
         "[▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/melanges/) | "
         "[melanges/README.md](melanges/README.md) | [liste](melanges/assets/README.md) |")
s, crlf = lire("README.md")
if "melanges/" not in s:
    lignes = s.split("\n")
    i = max(k for k, l in enumerate(lignes) if l.startswith("| ") and "[▶ en ligne]" in l)
    lignes.insert(i + 1, LIGNE)
    s = "\n".join(lignes)
    s = s.replace("et `http://127.0.0.1:8000/constitution/prof.html`.",
                  "`http://127.0.0.1:8000/constitution/prof.html`\net `http://127.0.0.1:8000/melanges/prof.html`.")
    a = "| Le Sceau de la République | `constitution/?salle=N&niveau=CM2`"
    k = s.index(a); fin = s.index("\n", k)
    s = s[:fin] + "\n| Le Laboratoire de Madame Mélange | `melanges/?salle=N&niveau=CM1` — N de 1 à 5, 6 = fin ; `&enigme=K` vise une énigme | [salle 5, énigme 4, CM2](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=5&niveau=CM2&enigme=4) |" + s[fin:]
    k0 = s.index("PROJET ESCAPE GAMES/")
    fin = s.index("```", k0)
    bloc = s[k0:fin].split("\n")
    dern = max(n for n, l in enumerate(bloc) if l.startswith("└── "))
    for n in range(dern, len(bloc)):
        if bloc[n].startswith("└── "): bloc[n] = "├── " + bloc[n][4:]
        elif bloc[n].startswith("    "): bloc[n] = "│   " + bloc[n][4:]
    while bloc and bloc[-1].strip() == "": bloc.pop()
    s = s[:k0] + "\n".join(bloc) + """
│
└── melanges/               ⚗️ Le Laboratoire de Madame Mélange (sciences)
    ├── README.md           Guide du jeu : salles, énigmes, solutions
    ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation
    ├── A-VERIFIER.md       Faits à contrôler
    ├── index.html · prof.html
    ├── assets/data/        ★ enigmes.json, lecons.json (leçons rédigées), dialogues, évaluations
    ├── css/
    └── js/                 même moteur à 10 types d'énigmes
""" + s[fin:]
    ecrire("README.md", s, crlf); print("intégré : README.md")
else:
    print("déjà intégré : README.md")
