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

- 🏠 **Accueil des jeux** : https://idgir.github.io/escape-games-cm1-cm2/ — avec la **frise de l'année** : les 26 jeux de la progression sur les périodes P1 à P5 (Années A et B), en couleur ceux qui sont déjà jouables
- 📅 **L'année en escape games** (périodes, Années A/B, points du programme couverts) : https://idgir.github.io/escape-games-cm1-cm2/annee.html
- 🗓️ **Fiche de période** (une page A4 pour la direction ou les familles : jeux et compétences travaillées) : https://idgir.github.io/escape-games-cm1-cm2/periode.html?p=P1&annee=A
- 📺 **Démonstration en boucle** (salle des professeurs, portes ouvertes) : https://idgir.github.io/escape-games-cm1-cm2/demo.html — un extrait de chaque jeu, enchaîné automatiquement, sans rien enregistrer
- 🔍 **Page de vérification** (énigmes, médias) : https://idgir.github.io/escape-games-cm1-cm2/verifier.html
- 📖 **Leçons à imprimer** (A4 illustrées, CM1 ou CM2) : depuis ⚙️ Réglages dans chaque jeu — voir la partie 2 bis

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

### 📲 Sur tablette, sans internet — application installable

Ouvrez une fois l'accueil en ligne dans Chrome ou Edge : quand le bloc **📲 Sur tablette, sans internet**
indique « ✅ Prêt hors connexion », les 9 jeux fonctionnent **sans réseau et sans serveur**. Le bouton
**📲 Installer l'application** les place sur l'écran d'accueil de la tablette. Hors connexion, les vidéos sont
remplacées par les images ou les décors dessinés. Détails et mise à jour : [outils-pwa/README.md](outils-pwa/README.md).

### 🏠 À la maison — mode individuel (devoirs)

Donnez aux élèves l'adresse d'un jeu suivie de `?solo=1`, par exemple
`https://idgir.github.io/escape-games-cm1-cm2/melanges/?solo=1` (ou `?solo=1&niveau=CM1`). L'élève joue seul,
avec son prénom ; à la fin, il **copie son compte-rendu** dans un message de l'ENT, le **télécharge** (fichier
à déposer) ou l'**imprime**. Le compte-rendu porte un code de contrôle ; rassemblez-les dans
[resultats.html](resultats.html) (export tableur et Schooly).

### Sur l'ordinateur — sans internet, ou pour vérifier avant de publier

1. Installez **Python 3** (une seule fois : https://www.python.org/downloads/,
   cochez « Add Python to PATH »).
2. Double-cliquez sur **`lancer.bat`** (Windows) ou **`lancer-mac.command`** (Mac).
3. Le navigateur s'ouvre sur l'accueil : **http://127.0.0.1:8000/**
4. Pour les autres postes de la classe (même réseau) : l'adresse est affichée
   dans la fenêtre noire, par exemple `http://192.168.1.20:8000/`.

Laissez la fenêtre noire ouverte pendant la séance. Ce mode ajoute les
**tableaux de bord enseignant en direct** (suivi des équipes, pause générale,
indices envoyés à la volée, **⏱️ + : minutes accordées à une équipe sans lui faire perdre son bonus de rapidité**) :
`http://127.0.0.1:8000/declaration/prof.html`, `http://127.0.0.1:8000/tour-du-monde/prof.html`,
`http://127.0.0.1:8000/constitution/prof.html`, `http://127.0.0.1:8000/station-meteo/prof.html`
et `http://127.0.0.1:8000/objets-techniques/prof.html` (le principe est le même pour chaque jeu).

**📺 Écran de classement à projeter** (séparé du pilotage) : `http://127.0.0.1:8000/classement.html` — bouton
« 📺 Écran de classement » dans chaque tableau de bord. Par défaut, il montre la **progression** des équipes
(salles franchies), pas les scores ; on peut choisir « les scores ». Aucune commande n'y est possible.

> Un double-clic direct sur un `index.html` lance aussi le jeu, mais **sans les
> vidéos** (le navigateur les bloque) : préférez l'une des deux méthodes ci-dessus.

---

## 1 bis. Les résultats de l'année : resultats.html

**[resultats.html](https://idgir.github.io/escape-games-cm1-cm2/resultats.html)** rassemble les comptes-rendus de
parties, au lieu de bilans A4 isolés : parties jouées sur l'appareil, parties de la classe gardées par le
serveur local (`lancer.bat` : fichier `resultats-classe.jsonl` sur votre ordinateur, **jamais publié**),
comptes-rendus envoyés par les élèves en mode individuel (fichiers déposés ou textes collés, avec code de
contrôle). Exports : **tableur** (CSV pour Excel/LibreOffice), **Schooly** (CSV, une ligne par élève et par
partie), sauvegarde JSON. Rien n'est envoyé sur internet.

## 1 ter. Le passeport de compétences : passeport.html

**[passeport.html](https://idgir.github.io/escape-games-cm1-cm2/passeport.html)** cumule, pour chaque élève et
sur toute l'année, les compétences du programme travaillées dans les escape games (une par leçon de chaque jeu
publié) : *Non acquis / En cours / Acquis*, avec une jauge par matière, une vue de la classe, l'impression
d'un passeport par élève et un export CSV (tableur, Schooly). Les données restent dans le navigateur de
l'appareil : exportez-les régulièrement (💾).

## 2. Tout vérifier : la page de vérification

**[verifier.html](https://idgir.github.io/escape-games-cm1-cm2/verifier.html)** —
en ligne, ou en local sur http://127.0.0.1:8000/verifier.html. Un onglet par jeu :

| Rubrique | Ce qu'elle fait |
|---|---|
| 🧩 **Tester les énigmes** | Un bouton par salle, escale ou séance (en CM1 et en CM2) : le jeu s'ouvre directement au bon endroit. **Rien n'est sauvegardé** : les parties des élèves ne sont pas touchées. |
| 🎞️ **Médias** | Chaque emplacement du jeu : aperçu, fichier trouvé et son poids — ou, s'il manque, le nom exact à utiliser (📋 le copie) et le bouton pour le déposer sur GitHub. Filtres *Présents / Manquants / Lourds*. |
| 🧹 **Fichiers mal nommés** | Les fichiers présents dans les dossiers mais que le jeu ne verra pas (majuscule, faute de frappe, mauvais dossier). |
| 📚 **Documents** | Les guides du jeu. |
| 🧬 **Cohérence du moteur** *(dernier onglet)* | Vérifie que les 8 jeux « salles » chargent tous le même tronc commun `commun/js/` (aucune copie locale oubliée, numéros de version à jour, `js/jeu.js` complet) et signale les fonctions présentes dans certains `app.js`/`reglages.js` mais absentes d'autres : la trace d'un correctif recopié dans un seul jeu. |

Les boutons « Tester » sont de simples adresses, que vous pouvez aussi taper ou mettre en favori :

| Jeu | Adresse | Exemple |
|---|---|---|
| Le Secret de la Déclaration | `declaration/?salle=N&niveau=CM1` (ou `CM2`) — N de 1 à 5, 6 = fin | [salle 3 en CM1](https://idgir.github.io/escape-games-cm1-cm2/declaration/?salle=3&niveau=CM1) |
| Le Tour du Monde | `tour-du-monde/?salle=N&niveau=CM2` — N de 1 à 5, 6 = fin | [escale 5 en CM2](https://idgir.github.io/escape-games-cm1-cm2/tour-du-monde/?salle=5&niveau=CM2) |
| Mission géographique | `mission-geo/?seance=N&niveau=CM1` (ou `CM2`, `DEC` pour Découverte) — N de 1 à 16, ou `final` | [séance 13 en CM1](https://idgir.github.io/escape-games-cm1-cm2/mission-geo/?seance=13&niveau=CM1) |
| Le Sceau de la République | `constitution/?salle=N&niveau=CM2` — N de 1 à 5, 6 = fin ; `&enigme=K` vise une énigme | [salle 4, énigme 2, CM2](https://idgir.github.io/escape-games-cm1-cm2/constitution/?salle=4&niveau=CM2&enigme=2) |
| Le Laboratoire de Madame Mélange | `melanges/?salle=N&niveau=CM1` — N de 1 à 5, 6 = fin ; `&enigme=K` vise une énigme | [salle 5, énigme 4, CM2](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=5&niveau=CM2&enigme=4) |
| L'Atelier de l'inventeur | `objets-techniques/?salle=N&niveau=CM1` (ou `CM2`) — N de 1 à 5, 6 = fin ; `&enigme=K` vise une énigme | [salle 4, énigme 3, CM2](https://idgir.github.io/escape-games-cm1-cm2/objets-techniques/?salle=4&niveau=CM2&enigme=3) |
| La Station météo disparue | `station-meteo/?salle=N&niveau=CM1` (ou `CM2`) — N de 1 à 5, 6 = fin ; `&enigme=K` vise une énigme | [module 1, énigme 1, CM2](https://idgir.github.io/escape-games-cm1-cm2/station-meteo/?salle=1&niveau=CM2&enigme=1) |
| Le Manuscrit de l'abbaye | `moyen-age-abbaye/?salle=N&niveau=CM1` — N de 1 à 5, 6 = fermoir puis fin ; `&enigme=K` vise une énigme | [salle 5, énigme 1, CM1](https://idgir.github.io/escape-games-cm1-cm2/moyen-age-abbaye/?salle=5&niveau=CM1&enigme=1) |
| Le Secret du donjon | `chateau-fort/?salle=N&niveau=CM1` (ou `CM2`) — N de 1 à 5, 6 = inscription, herse et fin ; `&enigme=K` vise une énigme | [salle 2, énigme 4, CM2](https://idgir.github.io/escape-games-cm1-cm2/chateau-fort/?salle=2&niveau=CM2&enigme=4) |

---

## 2 bis. Imprimer les leçons (A4 illustrées)

Chaque jeu propose ses leçons en **pages A4 prêtes à imprimer** : une page par leçon, en version
**CM1** ou **CM2**, avec l'en-tête du jeu, la **compétence du programme**, le texte de la leçon,
des **cartes**, **schémas**, **graphiques** et **photos** légendés et sourcés, la frise, un
document, le lexique et les sources. La taille du texte s'ajuste pour que chaque leçon tienne
sur sa page.

**Depuis le jeu (volet enseignant)** : ⚙️ **Réglages** → bloc **📖 Leçons à imprimer** → choisir
« Toutes les leçons » ou une salle → **📖 CM1** ou **📖 CM2**. L'aperçu s'ouvre dans un nouvel
onglet ; changer de niveau ou de leçon en haut de la page, puis cliquer sur **Imprimer**.
Mission géographique : ⚙️ **Espace enseignant** → *Impressions* → **📖 Leçon A4 illustrée**
(séance choisie) ou **📖 Les 16 leçons A4**. Le tableau de bord `prof.html` a aussi un bouton.

**Dans la fenêtre d'impression** : format **A4**, **portrait**, marges « par défaut » (ou
« aucune »), et cocher **Graphiques d'arrière-plan** pour garder les couleurs. On peut aussi
choisir « Enregistrer au format PDF ».

Adresse directe : `<jeu>/lecons-imprimables.html?niveau=CM1&salle=3` (une salle) ou
`?niveau=CM2&lecon=toutes` — par exemple
[les leçons du Secret du donjon en CM2](https://idgir.github.io/escape-games-cm1-cm2/chateau-fort/lecons-imprimables.html?niveau=CM2&lecon=toutes).

Les cartes sont dessinées à partir de données géographiques réelles (Natural Earth, contours IGN
des régions) ; les photos sont celles du jeu, avec leur crédit. Pour modifier une leçon
imprimée ou en régénérer les visuels : [outils-lecons/README.md](outils-lecons/README.md).

---

## 2 ter. Règles de jeu communes (moteur v2, octobre 2026)

Les 9 jeux suivent les mêmes règles, pensées pour que les élèves **réfléchissent et consultent les
leçons** plutôt que de cliquer au hasard :

- **Tout juste du premier coup = 10 points**, après une erreur = **3 points** seulement (rappel en
  tête de chaque énigme). Le chrono n'est pas touché.
- En cas d'erreur, le jeu dit **combien** de réponses sont justes, **jamais lesquelles**.
- **Aucun texte après la réussite** (ni correction, ni dialogue) : le bouton suivant apparaît tout de
  suite et le personnage se tait dès que les élèves touchent l'énigme.
- Le **mot gagné** à la fin d'une salle n'est affiché **qu'une fois** : les élèves le notent sur leur
  **fiche de mission** (⚙️ Réglages → Impression → **✍️ Fiche de mission**, une par équipe), puis le
  retapent dans le **coffre final**.
- Les **lettres cachées** sont mélangées et accompagnées de leurres.

**Indices proposés** : quand une équipe reste longtemps sans agir sur une énigme (2 min en CM1, 3 min en
CM2) ou se trompe deux fois, le jeu lui *propose* un indice (−2 points, comme d'habitude) ; elle peut refuser.
Réglable dans ⚙️ Réglages → 💡 Indices proposés.

**Trois paliers** dans les 8 jeux « salles » : **CM1**, **CM2** et **🌱 Découverte** (classes à triple niveau,
élèves en difficulté) : les énigmes du CM1 avec une aide renforcée — premier indice offert sans perte de
points, un choix faux écarté dans les QCM, leçon mise en évidence, première lettre des mots au coffre.
Vérification : ajouter `&palier=decouverte` à une adresse en `niveau=CM1`.

Scores maximaux : 185 (CM1) / 235 (CM2) pour les jeux à 5 salles (195 / 245 pour l'abbaye, avec le
fermoir), 95 pour la Déclaration et le Tour du monde ; Mission géographique : 10 points par énigme.
Outils : [outils-moteur/README.md](outils-moteur/README.md) · tests automatiques des 9 jeux :
[outils-tests/README.md](outils-tests/README.md).

---

## 2 quater. Modifier une énigme sans écrire de code : editeur.html

**[editeur.html](https://idgir.github.io/escape-games-cm1-cm2/editeur.html)** ouvre le fichier `enigmes.json` d'un des
6 jeux à moteur commun et présente chaque énigme sous forme de formulaire (titre, niveaux CM1/CM2, consigne,
contenu — questions, paires, cartes, cases… —, indices, corrigé, variantes). Les **contrôles** sont faits en
direct (bonne réponse présente, réponses parmi les étiquettes, identifiants uniques, nombre d'énigmes par niveau).
**👁️ Tester dans le jeu** ouvre l'énigme modifiée dans le jeu, sans rien enregistrer. Pour garder la modification :
**💾 Télécharger enigmes.json** puis le déposer dans `<jeu>/assets/data/` ; ou, avec `lancer.bat` sur l'ordinateur
de l'enseignant, **💾 Enregistrer dans le jeu** (l'ancien fichier est gardé : `enigmes.json.avant-…`).
Déclaration et Tour du monde (énigmes écrites dans le code) et Mission géographique ne sont pas concernés.

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
├── outils-tests/          Tests automatiques des 9 jeux (Node + jsdom) : node outils-tests/tous.js
├── commun/                ★ Tronc commun du moteur (médias, sons, voix, énigmes, impressions…) : un seul
│                           exemplaire pour tous les jeux — voir commun/README.md
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
│   └── js/                 jeu.js = ce qui est propre au jeu ; le moteur est dans commun/
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
│   └── js/                 jeu.js ; moteur d'énigmes commun : commun/js/enigmes.js
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
│   └── js/                 jeu.js ; type « instrument » dans commun/js/enigmes.js
│
├── melanges/               ⚗️ Le Laboratoire de Madame Mélange (sciences)
│   ├── README.md           Guide du jeu : salles, énigmes, solutions
│   ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation
│   ├── A-VERIFIER.md       Faits à contrôler
│   ├── index.html · prof.html
│   ├── assets/data/        ★ enigmes.json, lecons.json (leçons rédigées), dialogues, évaluations
│   ├── css/
│   └── js/                 jeu.js ; moteur commun (commun/js/)
│
├── objets-techniques/      ⚙️ L'Atelier de l'inventeur (sciences, les objets techniques)
│   ├── README.md           Guide du jeu : salles, énigmes, solutions, sources
│   ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation
│   ├── A-VERIFIER.md       Points à contrôler
│   ├── index.html · prof.html
│   ├── assets/data/        ★ enigmes.json (20 énigmes) · lecons.json (5 leçons rédigées)
│   ├── css/ · js/          moteur commun (commun/js/)
│   └── tests/              tests Node + jsdom
│
├── moyen-age-abbaye/       📜 Le Manuscrit de l'abbaye (histoire, le Moyen Âge)
│   ├── README.md           Guide du jeu : salles, énigmes, solutions, sources
│   ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation
│   ├── A-VERIFIER.md       Faits vérifiés et points à relire
│   ├── index.html · prof.html
│   ├── assets/data/        ★ enigmes.json (+ le fermoir) · lecons.json = 5 leçons rédigées
│   ├── css/ · js/          moteur commun (commun/js/)
│   └── tests/              test-jeu.js (Node + jsdom)
│
└── chateau-fort/           🏰 Le Secret du donjon (histoire, le château fort et les paysans)
    ├── README.md           Guide du jeu : salles, énigmes, solutions, sources
    ├── GUIDE-PEDAGOGIQUE.md  Programmes, déroulés, différenciation, évaluation
    ├── A-VERIFIER.md       Faits vérifiés et points à relire
    ├── index.html · prof.html
    ├── assets/data/        ★ enigmes.json (20 énigmes) · lecons.json = 5 leçons rédigées
    ├── css/ · js/          moteur commun (commun/js/)
    └── tests/              test_json.py · test-chateau-fort.js (Node + jsdom)
```

Le livret source `Mission géographique Année A.pdf` reste sur l'ordinateur
(dans `mission-geo/`), il n'est pas publié.

---

### Journal des versions

Chaque jeu a son **`CHANGELOG.md`** (journal durable et publié des évolutions, du plus récent au plus ancien).
Avant de publier : **Invite de commandes** → `E:` → `cd "\IDRISS\PROJET ESCAPE GAMES"` →
`python outils-docs\maj-journaux.py` (ajoute les nouveaux commits en tête de chaque journal) → `git add */CHANGELOG.md`.
On peut compléter un journal à la main : le texte existant n'est jamais réécrit.

## 5. En cas de problème

**Toutes les questions fréquentes, pour tous les jeux, avec recherche :** [faq.html](https://idgir.github.io/escape-games-cm1-cm2/faq.html) (lien sur l'accueil). Le tableau ci-dessous en reprend l'essentiel.

| Problème | Solution |
|---|---|
| Mon image ou ma vidéo n'apparaît pas | Page de vérification : la carte indique le nom attendu, et la rubrique 🧹 signale les fichiers mal nommés. Puis **Ctrl+F5** dans le jeu. |
| L'ancienne image reste affichée | Le navigateur garde une copie : **Ctrl+F5**, ou attendez quelques minutes après un envoi sur GitHub. |
| Pas de vidéo, seulement les dessins | Le jeu a été ouvert en double-clic : passez par l'adresse en ligne ou par `lancer.bat`. |
| `lancer.bat` affiche « Python n'est pas installé » | Installez Python en cochant « Add Python to PATH », ou jouez en ligne. |
| Le tableau de bord n'affiche aucune équipe | Il ne fonctionne qu'en mode local, avec les élèves sur l'adresse affichée par `lancer.bat`. |
| Page blanche ou jeu figé | Chrome ou Edge à jour ; rechargez la page. |
| Un élève dyslexique ou lecteur fragile | ⚙️ Réglages → Accessibilité → **📖 Lecture facilitée** : police OpenDyslexic ou très lisible, interlignage aéré, espacement. Réglé une fois, valable pour tous les jeux sur cet appareil. |
| Effacer la progression d'une équipe | Bouton « Rejouer » en fin de partie (Mission géo : ⚙️ → Progression → « Repartir de zéro »). |

Les erreurs « 404 » visibles dans la console du navigateur (F12) sont normales :
c'est le jeu qui cherche les médias que vous auriez pu déposer.
