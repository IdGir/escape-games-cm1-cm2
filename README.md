# 🎓 Escape games pédagogiques — CM1 / CM2

Neuf escape games d'histoire, de géographie, d'EMC et de sciences, jouables dans Chrome, sans installation.

| | Jeu | Jouer | Guide : énigmes, solutions | Médias |
|---|---|---|---|---|
| 🏛️ | **Le Secret de la Déclaration** — Histoire, 1789 | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/declaration/) | [declaration/README.md](declaration/README.md) | [liste](declaration/assets/README.md) |
| 🧭 | **Le Tour du Monde en 80 minutes** — Géographie | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/tour-du-monde/) | [tour-du-monde/README.md](tour-du-monde/README.md) | [liste](tour-du-monde/assets/README.md) |
| 🗺️ | **Mission géographique — Année A** — Géographie, 16 séances | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/mission-geo/) | [mission-geo/README.md](mission-geo/README.md) | [liste](mission-geo/assets/README.md) |
| ⚖️ | **Le Sceau de la République** — EMC, la Constitution de 1958 | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/constitution/) | [constitution/README.md](constitution/README.md) | [liste](constitution/assets/README.md) |
| 🌦️ | **La Station météo disparue** — Sciences, mesures météorologiques | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/station-meteo/) | [station-meteo/README.md](station-meteo/README.md) | [liste](station-meteo/assets/README.md) |
| ⚗️ | **Le Laboratoire de Madame Mélange** — Sciences, masses et mélanges | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/melanges/) | [melanges/README.md](melanges/README.md) | [liste](melanges/assets/README.md) |
| ⚙️ | **L'Atelier de l'inventeur** — Sciences, les objets techniques | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/objets-techniques/) | [objets-techniques/README.md](objets-techniques/README.md) | [liste](objets-techniques/assets/README.md) |
| 📜 | **Le Manuscrit de l'abbaye** — Histoire, le Moyen Âge | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/moyen-age-abbaye/) | [moyen-age-abbaye/README.md](moyen-age-abbaye/README.md) | [liste](moyen-age-abbaye/assets/README.md) |
| 🏰 | **Le Secret du donjon** — Histoire, le château fort et les paysans | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/chateau-fort/) | [chateau-fort/README.md](chateau-fort/README.md) | [liste](chateau-fort/assets/README.md) |

- 🏠 **Accueil des jeux** : https://idgir.github.io/escape-games-cm1-cm2/
- 🔍 **Page de vérification** (énigmes, médias) : https://idgir.github.io/escape-games-cm1-cm2/verifier.html

---

## 1. Lancer un jeu

### En ligne — n'importe où, le plus simple

Ouvrez **https://idgir.github.io/escape-games-cm1-cm2/** dans Chrome (PC, TBI,
Chromebook, tablette) et cliquez sur le jeu. Mettez l'adresse en favori une
fois pour toutes.

- La progression de chaque équipe est gardée **sur l'appareil** (même navigateur).
- Tout fonctionne en ligne : jeux, vidéos, leçons, fiches à imprimer. Seul le
  tableau de bord enseignant en direct demande le mode local (ci-dessous).
- L'adresse racine du site ouvre désormais **l'accueil des cinq jeux**.
  Pour arriver directement dans un jeu, mettez son adresse en favori
  (par exemple `…/declaration/`).

### Sur l'ordinateur — sans internet, ou pour vérifier avant de publier

1. Installez **Python 3** (une seule fois : https://www.python.org/downloads/,
   cochez « Add Python to PATH »).
2. Double-cliquez sur **`lancer.bat`** (Windows) ou **`lancer-mac.command`** (Mac).
3. Le navigateur s'ouvre sur l'accueil : **http://127.0.0.1:8000/**
4. Pour les autres postes de la classe (même réseau) : l'adresse est affichée
   dans la fenêtre noire, par exemple `http://192.168.1.20:8000/`.

Laissez la fenêtre noire ouverte pendant la séance. Ce mode ajoute les
**tableaux de bord enseignant en direct** (suivi des équipes, pause générale,
indices envoyés à la volée) :
`http://127.0.0.1:8000/declaration/prof.html`, `http://127.0.0.1:8000/tour-du-monde/prof.html`,
`http://127.0.0.1:8000/constitution/prof.html`, `http://127.0.0.1:8000/station-meteo/prof.html`
et `http://127.0.0.1:8000/objets-techniques/prof.html` (le principe est le même pour chaque jeu).

> Un double-clic direct sur un `index.html` lance aussi le jeu, mais **sans les
> vidéos** (le navigateur les bloque) : préférez l'une des deux méthodes ci-dessus.

---

## 2. Tout vérifier : la page de vérification

**[verifier.html](https://idgir.github.io/escape-games-cm1-cm2/verifier.html)** —
en ligne, ou en local sur http://127.0.0.1:8000/verifier.html. Un onglet par jeu :

| Rubrique | Ce qu'elle fait |
|---|---|
| 🧩 **Tester les énigmes** | Un bouton par salle, escale ou séance (en CM1 et en CM2) : le jeu s'ouvre directement au bon endroit. **Rien n'est sauvegardé** : les parties des élèves ne sont pas touchées. |
| 🎞️ **Médias** | Chaque emplacement du jeu : aperçu, fichier trouvé et son poids — ou, s'il manque, le nom exact à utiliser (📋 le copie) et le bouton pour le déposer sur GitHub. Filtres *Présents / Manquants / Lourds*. |
| 🧹 **Fichiers mal nommés** | Les fichiers présents dans les dossiers mais que le jeu ne verra pas (majuscule, faute de frappe, mauvais dossier). |
| 📚 **Documents** | Les guides du jeu. |

Les boutons « Tester » sont de simples adresses, que vous pouvez aussi taper ou mettre en favori :

| Jeu | Adresse | Exemple |
|---|---|---|
| Le Secret de la Déclaration | `declaration/?salle=N&niveau=CM1` (ou `CM2`) — N de 1 à 5, 6 = fin | [salle 3 en CM1](https://idgir.github.io/escape-games-cm1-cm2/declaration/?salle=3&niveau=CM1) |
| Le Tour du Monde | `tour-du-monde/?salle=N&niveau=CM2` — N de 1 à 5, 6 = fin | [escale 5 en CM2](https://idgir.github.io/escape-games-cm1-cm2/tour-du-monde/?salle=5&niveau=CM2) |
| Mission géographique | `mission-geo/?seance=N` — N de 1 à 16, ou `final` | [séance 13](https://idgir.github.io/escape-games-cm1-cm2/mission-geo/?seance=13) |
| Le Sceau de la République | `constitution/?salle=N&niveau=CM2` — N de 1 à 5, 6 = fin ; `&enigme=K` vise une énigme | [salle 4, énigme 2, CM2](https://idgir.github.io/escape-games-cm1-cm2/constitution/?salle=4&niveau=CM2&enigme=2) |
| Le Laboratoire de Madame Mélange | `melanges/?salle=N&niveau=CM1` — N de 1 à 5, 6 = fin ; `&enigme=K` vise une énigme | [salle 5, énigme 4, CM2](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=5&niveau=CM2&enigme=4) |
| L'Atelier de l'inventeur | `objets-techniques/?salle=N&niveau=CM1` (ou `CM2`) — N de 1 à 5, 6 = fin ; `&enigme=K` vise une énigme | [salle 4, énigme 3, CM2](https://idgir.github.io/escape-games-cm1-cm2/objets-techniques/?salle=4&niveau=CM2&enigme=3) |
| La Station météo disparue | `station-meteo/?salle=N&niveau=CM1` (ou `CM2`) — N de 1 à 5, 6 = fin ; `&enigme=K` vise une énigme | [module 1, énigme 1, CM2](https://idgir.github.io/escape-games-cm1-cm2/station-meteo/?salle=1&niveau=CM2&enigme=1) |
| Le Manuscrit de l'abbaye | `moyen-age-abbaye/?salle=N&niveau=CM1` — N de 1 à 5, 6 = fermoir puis fin ; `&enigme=K` vise une énigme | [salle 5, énigme 1, CM1](https://idgir.github.io/escape-games-cm1-cm2/moyen-age-abbaye/?salle=5&niveau=CM1&enigme=1) |
| Le Secret du donjon | `chateau-fort/?salle=N&niveau=CM1` (ou `CM2`) — N de 1 à 5, 6 = inscription, herse et fin ; `&enigme=K` vise une énigme | [salle 2, énigme 4, CM2](https://idgir.github.io/escape-games-cm1-cm2/chateau-fort/?salle=2&niveau=CM2&enigme=4) |

---

## 3. Ajouter ou remplacer une image ou une vidéo

**La règle** : chaque jeu a **un seul dossier médias**, `<jeu>/assets/`, et chaque
emplacement **un seul nom de fichier**. Il suffit de déposer un fichier portant
ce nom : il remplace le dessin par défaut, ou l'ancien fichier du même nom.
Aucun code à modifier.

Les noms attendus sont dans la page de vérification (📋 copie le nom) et dans
le `README.md` du dossier `assets/` de chaque jeu.

### Méthode A — sur l'ordinateur, puis publication *(on voit le rendu avant de publier)*

1. Lancez `lancer.bat` et ouvrez http://127.0.0.1:8000/verifier.html.
2. Copiez le fichier dans le bon dossier, avec le bon nom — par exemple
   `declaration/assets/videos/salle1.mp4`.
3. Revenez sur la page de vérification : l'aperçu apparaît aussitôt, et
   ▶ ouvre la salle dans le jeu.
4. Publiez sur GitHub : demandez-le à Claude Code (« publie les nouveaux
   médias »), ou `git add` → `git commit` → `git push`.

### Méthode B — directement sur GitHub *(rien à installer)*

1. Sur la page de vérification en ligne, cliquez **⬆️ Vidéo → GitHub** ou
   **⬆️ Image → GitHub** sur la carte de l'emplacement : le bon dossier s'ouvre
   sur GitHub.
2. Glissez le fichier, **nommé exactement** comme indiqué.
3. **Commit changes**. C'est en ligne en une minute environ ; rechargez le jeu
   avec **Ctrl+F5**.

> Après un envoi sur GitHub, récupérez le fichier sur l'ordinateur avant d'y
> retravailler (`git pull`, ou demandez-le à Claude Code) : le dossier local
> et GitHub doivent rester identiques.

### Formats

| | Décors et cinématiques | Personnages | Cartes, documents de leçon |
|---|---|---|---|
| **Vidéo** | `.mp4` (H.264) ou `.webm`, 16:9, 15 à 30 s en boucle, moins de 20 Mo | `.mp4` en boucle, cadre portrait vertical | — |
| **Image** | `.jpg`, `.png` ou `.webp`, 16:9 | `.png` carré (fond transparent), `.gif` animé accepté | `.jpg` |

- Noms **en minuscules, sans espace ni accent** : `salle1.jpg`, pas `Salle 1.JPG`.
- Vidéo et image du même nom : la vidéo s'affiche, l'image lui sert d'affiche.
- Les vidéos de décor sont jouées **muettes** (un bouton 🔇 permet d'activer le son).
- Sous-titres : un fichier `.vtt` du même nom que la vidéo est chargé automatiquement.
- Sans fichier, le jeu affiche son dessin : ce n'est jamais une erreur.
- Supprimer un fichier ramène le dessin par défaut.

---

## 4. Organisation du dépôt

```
PROJET ESCAPE GAMES/
├── index.html              Accueil : tous les jeux
├── verifier.html           Vérification : énigmes, médias, fichiers mal nommés
├── lancer.bat              Serveur local, Windows (double-clic)
├── lancer-mac.command      Serveur local, Mac
├── serveur.py              Le serveur lui-même (Python, rien d'autre à installer)
│
├── declaration/            🏛️ Le Secret de la Déclaration
│   ├── README.md           Guide du jeu : salles, énigmes, solutions
│   ├── GUIDE-PEDAGOGIQUE.md  Scénario, déroulé, évaluation, fiches à imprimer
│   ├── index.html          Le jeu
│   ├── prof.html           Tableau de bord enseignant (mode local)
│   ├── assets/             ★ Médias du jeu — README.md = liste des noms
│   │   ├── videos/         décors, cinématiques (+ personnages/)
│   │   ├── images/         decors/, personnages/, documents/
│   │   └── data/           textes : dialogues, leçons, évaluations
│   ├── css/
│   └── js/
│
├── tour-du-monde/          🧭 Même organisation (+ assets/images/cartes/)
│
├── mission-geo/            🗺️ Mission géographique
│   ├── README.md
│   ├── index.html
│   ├── assets/             ★ videos/ et images/, tout à plat
│   ├── css/
│   └── js/donnees/         le contenu des 16 séances
│
├── constitution/           ⚖️ Le Sceau de la République (EMC)
│   ├── README.md           Guide du jeu : salles, énigmes, solutions
│   ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation, concours
│   ├── index.html          Le jeu
│   ├── prof.html           Tableau de bord enseignant (mode local)
│   ├── assets/
│   │   ├── data/           ★ enigmes.json = les 20 énigmes · concours.json = le concours
│   │   ├── videos/         décors, cinématiques (+ personnages/)
│   │   └── images/         decors/, personnages/, cartes/, documents/
│   ├── css/                (+ enigmes.css)
│   └── js/                 enigmes.js = moteur générique à 10 types d'énigmes
│
├── station-meteo/          🌦️ La Station météo disparue (sciences)
│   ├── README.md           Guide du jeu : modules, énigmes, solutions, sources
│   ├── GUIDE-PEDAGOGIQUE.md  Programmes, protocole de mini-station, déroulés, évaluation
│   ├── A-VERIFIER.md       Points factuels à contrôler
│   ├── fiche-releves.html  Fiche de relevés à imprimer (station de la cour)
│   ├── index.html          Le jeu
│   ├── prof.html           Tableau de bord enseignant (mode local)
│   ├── assets/data/        ★ enigmes.json (20 énigmes) · lecons.json (5 leçons rédigées)
│   ├── css/
│   └── js/                 enigmes.js = moteur + type « instrument » (thermomètre, pluviomètre)
│
├── melanges/               ⚗️ Le Laboratoire de Madame Mélange (sciences)
│   ├── README.md           Guide du jeu : salles, énigmes, solutions
│   ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation
│   ├── A-VERIFIER.md       Faits à contrôler
│   ├── index.html · prof.html
│   ├── assets/data/        ★ enigmes.json, lecons.json (leçons rédigées), dialogues, évaluations
│   ├── css/
│   └── js/                 même moteur à 10 types d'énigmes
│
├── objets-techniques/      ⚙️ L'Atelier de l'inventeur (sciences, les objets techniques)
│   ├── README.md           Guide du jeu : salles, énigmes, solutions, sources
│   ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation
│   ├── A-VERIFIER.md       Points à contrôler
│   ├── index.html · prof.html
│   ├── assets/data/        ★ enigmes.json (20 énigmes) · lecons.json (5 leçons rédigées)
│   ├── css/ · js/          même moteur à 10 types d'énigmes que constitution/
│   └── tests/              tests Node + jsdom
│
├── moyen-age-abbaye/       📜 Le Manuscrit de l'abbaye (histoire, le Moyen Âge)
│   ├── README.md           Guide du jeu : salles, énigmes, solutions, sources
│   ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation
│   ├── A-VERIFIER.md       Faits vérifiés et points à relire
│   ├── index.html · prof.html
│   ├── assets/data/        ★ enigmes.json (+ le fermoir) · lecons.json = 5 leçons rédigées
│   ├── css/ · js/          même moteur que constitution/
│   └── tests/              test-jeu.js (Node + jsdom)
│
└── chateau-fort/           🏰 Le Secret du donjon (histoire, le château fort et les paysans)
    ├── README.md           Guide du jeu : salles, énigmes, solutions, sources
    ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation
    ├── A-VERIFIER.md       Faits vérifiés et points à relire
    ├── index.html · prof.html
    ├── assets/data/        ★ enigmes.json (20 énigmes) · lecons.json = 5 leçons rédigées
    ├── css/ · js/          même moteur à 10 types d'énigmes que constitution/
    └── tests/              test_json.py · test-chateau-fort.js (Node + jsdom)
```

Le livret source `Mission géographique Année A.pdf` reste sur l'ordinateur
(dans `mission-geo/`), il n'est pas publié.

---

## 5. En cas de problème

| Problème | Solution |
|---|---|
| Mon image ou ma vidéo n'apparaît pas | Page de vérification : la carte indique le nom attendu, et la rubrique 🧹 signale les fichiers mal nommés. Puis **Ctrl+F5** dans le jeu. |
| L'ancienne image reste affichée | Le navigateur garde une copie : **Ctrl+F5**, ou attendez quelques minutes après un envoi sur GitHub. |
| Pas de vidéo, seulement les dessins | Le jeu a été ouvert en double-clic : passez par l'adresse en ligne ou par `lancer.bat`. |
| `lancer.bat` affiche « Python n'est pas installé » | Installez Python en cochant « Add Python to PATH », ou jouez en ligne. |
| Le tableau de bord n'affiche aucune équipe | Il ne fonctionne qu'en mode local, avec les élèves sur l'adresse affichée par `lancer.bat`. |
| Page blanche ou jeu figé | Chrome ou Edge à jour ; rechargez la page. |
| Effacer la progression d'une équipe | Bouton « Rejouer » en fin de partie (Mission géo : ⚙️ → Progression → « Repartir de zéro »). |

Les erreurs « 404 » visibles dans la console du navigateur (F12) sont normales :
c'est le jeu qui cherche les médias que vous auriez pu déposer.
