# 🧭 LE TOUR DU MONDE EN 80 MINUTES

**Escape game de géographie — CM1 / CM2 — d'après *Le Tour du monde en quatre-vingts jours* de Jules Verne (1873)**

Le carnet de route de **Phileas Fogg** a disparu. Sans itinéraire, le pari des
quatre-vingts jours est perdu. Cinq escales, cinq énigmes de géographie, quatre
cachets de voyage à décrocher — et, au bout, le mystère du 80ᵉ jour.

---

## 🚀 DÉMARRAGE

### Mode simple — 30 secondes
Double-cliquez sur **`index.html`**. ✅ *Aucune installation.*

> ⚠️ En double-clic (`file://`), les **décors vidéo ne peuvent pas se charger** :
> les navigateurs interdisent la lecture de fichiers locaux depuis une page locale.
> Le jeu bascule alors sur ses décors dessinés, et reste entièrement jouable.
> **Pour la vidéo, passez par le serveur** (ci-dessous).

### Mode complet — vidéo + pilotage prof
1. Depuis le dossier **parent**, double-cliquez sur `lancer.bat` (Windows) ou
   `lancer-mac.command` (Mac).
2. Postes élèves : `http://<ip-affichée>:8000/tour-du-monde/`
3. Poste enseignant : `http://127.0.0.1:8000/tour-du-monde/prof.html`

---

## 🗺️ LES CINQ ESCALES

| # | Lieu | Notion de géographie travaillée | Personnage |
|---|---|---|---|
| 1 | **Le Reform Club**, Londres | Le planisphère : continents, océans, équateur, méridien de Greenwich | Phileas Fogg |
| 2 | **L'isthme de Suez**, Égypte | Se déplacer : mers, détroits, canaux ; ordonner un itinéraire | L'inspecteur Fix |
| 3 | **La jungle de l'Inde** | Climats et paysages du monde ; latitude et altitude | Mrs Aouda |
| 4 | **La mer de Chine** | Moyens de transport, distances, **échelle d'une carte** | Jean Passepartout |
| 5 | **L'observatoire de Greenwich** | Méridiens, parallèles, **fuseaux horaires** — et le jour gagné | Phileas Fogg |

**Cachets de voyage à collecter :** 🧭 Rose des vents · 🚢 Le canal · 🌡️ Les climats · 🚂 La vapeur

### Différenciation CM1 / CM2

| | CM1 | CM2 |
|---|---|---|
| Escale 1 | 5 continents + 3 océans | 6 continents + Antarctique + 5 océans |
| Escale 2 | 4 escales à ordonner | 7 escales + mers traversées |
| Escale 3 | 4 paysages/climats | 6 paysages + zones climatiques |
| Escale 4 | 3 trajets | 5 trajets, nombres plus grands |
| Escale 5 | 3 villes (décalages positifs) | 5 villes (positifs **et** négatifs) |

---

## 🎬 INTÉGRER VOS PROPRES VIDÉOS

La charte graphique prévoit **cinq emplacements média** : décors, cinématiques, personnages, cartes et illustrations de leçon. Tout est **optionnel** :
sans le moindre fichier, le jeu tourne sur ses décors SVG animés.

### 1. Décors filmés (fond de scène)
Déposez vos fichiers dans **`assets/videos/`** :

| Fichier | Contenu attendu |
|---|---|
| `etape1.mp4` | Salon victorien du Reform Club, Londres 1872 |
| `etape2.mp4` | Le canal de Suez dans le désert |
| `etape3.mp4` | Jungle indienne, éléphant, voie ferrée |
| `etape4.mp4` | Tempête en mer de Chine, goélette |
| `etape5.mp4` | Observatoire de Greenwich, ligne du méridien |

### 2. Cinématiques plein écran
| Fichier | Moment |
|---|---|
| `intro.mp4` | Au clic sur « Lever l'ancre » — le pari |
| `final.mp4` | Après la dernière énigme — le jour gagné |

Elles s'affichent dans un **cadre-hublot de laiton**, avec barre de progression,
bouton **⏭ Passer** et **Échap** pour sortir. Si le fichier n'existe pas, la
cinématique est simplement **sautée**, sans message d'erreur.

### 3. Vidéo dans une leçon
Ajoutez une clé `"video"` à une leçon de `assets/data/lecons.json` :
```json
"video": { "base": "lecon-fuseaux", "titre": "Les fuseaux horaires", "source": "Production de classe" }
```
Le fichier attendu est alors `assets/videos/lecon-fuseaux.mp4`.

### 4. Personnages animés (vidéo ou image)
Chaque personnage peut être remplacé par une **vidéo en boucle** ou une **image**.
Déposez-les dans `assets/videos/personnages/` ou `assets/images/personnages/` :

| Fichier | Personnage |
|---|---|
| `fogg.mp4` ou `fogg.png` | Phileas Fogg |
| `passepartout.mp4` ou `.png` | Jean Passepartout |
| `aouda.mp4` ou `.png` | Mrs Aouda |
| `fix.mp4` ou `.png` | L'inspecteur Fix |

**Variante « en train de parler »** *(facultative)* : ajoutez `fogg-parle.mp4`.
Le jeu bascule alors tout seul sur cette boucle pendant que le personnage parle,
et revient à la boucle de repos ensuite. Sans cette variante, la boucle de repos
tourne en continu.

> Cadre : **170 × 262 px** (portrait vertical, plein corps). Les vidéos sont
> jouées **muettes** — la voix vient de la synthèse vocale, avec ses sous-titres.
> Un `.gif` animé est également accepté comme image.

### 5. Cartes, paysages et illustrations (images)
Déposez vos images dans `assets/images/cartes/` :

| Fichier | Où il apparaît |
|---|---|
| `planisphere.jpg` | Fond de carte de l'escale 1, **sous** les zones cliquables |
| `paysage-desert.jpg` | Vignette du désert (escale 3) |
| `paysage-jungle.jpg` | Vignette de la jungle |
| `paysage-montagne.jpg` | Vignette de l'Himalaya |
| `paysage-campagne.jpg` | Vignette de la campagne anglaise |
| `paysage-banquise.jpg` | Vignette de la banquise |
| `paysage-savane.jpg` | Vignette de la savane |

Le planisphère reste **entièrement jouable** avec une vraie carte en fond : les
zones à placer se posent par-dessus et gardent leurs couleurs de validation.

**Dans une leçon**, ajoutez une carte avec la clé `carte` de `assets/data/lecons.json` :
```json
"carte": { "base": "planisphere-vierge", "legende": "Planisphère à compléter", "source": "IGN" }
```
Et une image de document avec `"document": { "type": "image", "fichier": "extrait-verne", … }`,
attendue dans `assets/images/documents/`.

### Règles communes
- **Formats** : `.mp4` (recommandé, H.264) ou `.webm`. Format d'image **16/9**.
- **Affiche** : une image du même nom dans `assets/images/decors/`
  (`etape1.jpg`, `.png` ou `.webp`) sert de première image — et **remplace la
  vidéo** si celle-ci est absente.
- **Sous-titres** : un fichier `.vtt` du même nom est chargé automatiquement.
- **Son** : les décors sont **toujours muets** au départ, pour ne jamais couvrir
  la voix des personnages. Un bouton 🔇 permet de l'activer ponctuellement.
- **Dossier alternatif** : `../Elements EG/Jules Verne/` est également exploré,
  si vous préférez ranger vos médias avec ceux des autres escape games.
- **Poids** : visez moins de 20 Mo par vidéo, et 15 à 30 secondes en boucle pour
  un décor. Le serveur les diffuse **par morceaux** (requêtes *Range*), donc la
  lecture démarre sans attendre le téléchargement complet.

### Vérifier ce qui est détecté
⚙️ **Réglages → Multimédia → « 🔍 Vérifier les fichiers présents »** liste, pour
chaque séquence, si le jeu a trouvé une vidéo, une image, ou s'il utilise le
décor dessiné.

> 💡 Les erreurs **404** visibles dans la console (F12) sont **normales** :
> c'est la détection automatique qui essaie chaque nom de fichier possible.

---

## 👨‍🏫 MODULE ENSEIGNANT (⚙️)

- **Accessibilité** : agrandissement des textes (100 → 150 %), **animations réduites**
  (fige aussi les décors filmés)
- **Multimédia** : décors vidéo ON/OFF, son des vidéos, cinématiques ON/OFF
- **Sons** : voix des personnages, ambiances synthétisées, volumes séparés
- **Partie** : durée du minuteur (30 / 45 / 55 / 60 / **80** min), bibliothèque de leçons
- **IA optionnelle** : clé DeepSeek ou Albert pour des dialogues dynamiques
  (bascule automatiquement sur le contenu statique en cas d'échec)
- **Impressions A4** : fiches préparatoires (5 escales), QCM, questions fermées,
  études de documents — **corrigés séparés**

---

## 📚 BIBLIOTHÈQUE DE LEÇONS (📚)

Six leçons consultables à tout moment, en version CM1 **et** CM2 :
planisphère · points cardinaux · lire une carte (légende, échelle) ·
climats et paysages · se déplacer dans le monde · méridiens et fuseaux horaires.

---

## 🏆 SCORE ET BADGES

**85 points au total** : 5 escales × (10 pts + 5 pts de rapidité) = 75, plus le
quizz final (5 × 2 pts) = 10. Chaque indice consulté coûte 2 points.

| Badge | Obtenu en… |
|---|---|
| 🧭 Le Navigateur | complétant vite le planisphère |
| 🌍 Le Géographe | terminant **sans aucun indice** |
| 🚂 Le Voyageur | enchaînant rapidement les escales |
| ⏰ Maître du Temps | résolvant vite l'énigme des fuseaux |

---

## 📁 STRUCTURE

```
tour-du-monde/
├── index.html          ← Poste élève
├── prof.html           ← Tableau de bord enseignant
├── css/
│   ├── style.css       ← Charte « Verne » (laiton, abysse, carte marine)
│   ├── video.css       ← ★ Charte VIDÉO (décors, cinématiques, leçons)
│   ├── animations.css  ← Décors animés + lip-sync
│   ├── personnages.css ← Scène plein corps, gestes
│   └── print.css       ← Mise en page A4
├── js/
│   ├── media.js        ← ★ Moteur média : cascade vidéo → image → SVG
│   ├── decors.js       ← 5 décors SVG animés
│   ├── personnages.js  ← Fogg, Passepartout, Aouda, Fix (plein corps)
│   ├── enigmes.js      ← 5 énigmes de géographie
│   ├── audio.js        ← Ambiances synthétisées (aucun fichier)
│   ├── narration.js    ← Voix française + sous-titres
│   ├── lecons.js · impression.js · reglages.js · api.js · sync.js
│   └── app.js          ← Moteur principal
└── assets/
    ├── videos/              ← ← ← décors et cinématiques
    │   └── personnages/     ← ← ← personnages animés
    ├── images/
    │   ├── decors/          ← ← ← images d'affiche des décors
    │   ├── personnages/     ← ← ← portraits (png, jpg, gif animé)
    │   ├── cartes/          ← ← ← planisphère, paysages, croquis
    │   └── documents/       ← ← ← documents illustrés des leçons
    └── data/           ← dialogues, leçons, évaluations (JSON)
```

---

## 🌍 BON VOYAGE, APPRENTIS GÉOGRAPHES !
