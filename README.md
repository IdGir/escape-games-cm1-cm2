# 🎓 ESCAPE GAMES PÉDAGOGIQUES — CM1 / CM2

Ce dossier contient **trois escape games** partageant le même serveur local :

| Jeu | Matière | Format | Dossier | Lancer |
|---|---|---|---|---|
| 🏛️ **Le Secret de la Déclaration** | Histoire — Révolution française, 1789 | séance unique | *(racine)* | `index.html` |
| 🧭 **Le Tour du Monde en 80 minutes** | Géographie — d'après Jules Verne | séance unique | `tour-du-monde/` | `tour-du-monde/index.html` |
| 🗺️ **Mission géographique — Année A** | **Géographie CM1/CM2 — programme complet** | **16 séances sur l'année** | `mission-geo/` | `mission-geo/index.html` |

Un seul serveur sert les trois : `lancer.bat` (Windows) ou `lancer-mac.command` (Mac).

> 📖 Documentation de chaque jeu :
> [`tour-du-monde/README.md`](tour-du-monde/README.md) ·
> [`mission-geo/README.md`](mission-geo/README.md)

---

## 🗺️ MISSION GÉOGRAPHIQUE — ANNÉE A (nouveauté)

Adaptation interactive **intégrale** du livret papier *Mission géographique — Année A*,
redécoupée en **16 séances filées sur toute l'année**, une par élément du programme
de géographie (organisation du territoire, inégalités dans le monde, se nourrir,
usages de l'eau douce).

* Chaque séance réussie dépose **un indice** dans un carnet qui se remplit toute l'année ;
* les 16 indices réunis ouvrent une **piste finale** en trois énigmes ;
* la valise s'ouvre alors sur une **récompense mystère** que l'enseignant définit
  quand il le souhaite, dans l'espace enseignant ;
* **15 types d'énigmes interactives**, une **leçon** par séance, et des fiches A4
  (préparation, élève, corrigé, leçon, progression + solutions, bilan, diplôme) ;
* **des emplacements image ou vidéo réservés partout** : introduction, cœur de
  séance, chaque énigme, dénouement, leçon, récompense — aucun fichier n'est
  obligatoire, le jeu fonctionne tel quel.

👉 Tout est détaillé dans [`mission-geo/README.md`](mission-geo/README.md).

---

## 🎬 DÉCORS VIDÉO (nouveauté)

La charte graphique des **deux jeux** accepte désormais des **éléments vidéo**
et des **illustrations** à tous les endroits utiles : décors, cinématiques,
personnages, cartes et documents.
Le principe est une **cascade** : pour chaque décor, le jeu cherche d'abord une
vidéo, puis une image, et retombe sinon sur son décor dessiné animé. Aucun
fichier n'est obligatoire — le jeu reste entièrement jouable sans rien ajouter.

| Emplacement | Dossier | Noms attendus |
|---|---|---|
| Décors — Révolution | `assets/videos/` | `salle1.mp4` … `salle5.mp4` |
| Décors — Géographie | `tour-du-monde/assets/videos/` | `etape1.mp4` … `etape5.mp4` |
| Cinématiques | idem | `intro.mp4`, `final.mp4` |
| **Personnages** | `…/assets/videos/personnages/` | `fogg.mp4`, `louise.mp4`… (+ `-parle.mp4` facultatif) |
| **Personnages (image)** | `…/assets/images/personnages/` | `fogg.png`, `louise.png`, `.gif` animé… |
| **Cartes et paysages** | `tour-du-monde/assets/images/cartes/` | `planisphere.jpg`, `paysage-desert.jpg`… |
| **Documents de leçon** | `…/assets/images/documents/` | image nommée d'après la leçon |

Un personnage filmé peut avoir **deux boucles** : `fogg.mp4` au repos et
`fogg-parle.mp4` pendant qu'il parle. Le jeu bascule de l'une à l'autre tout seul.
Les cartes se glissent **sous** les zones cliquables des énigmes, qui restent
parfaitement utilisables.

Le dossier `Elements EG/` est également exploré. La vidéo **« Paris 1789.mp4 »**
qui s'y trouve déjà est **reconnue automatiquement** comme décor de la **salle 1**
du jeu d'histoire, sans avoir à la renommer.

⚙️ **Réglages → Multimédia** permet de couper les décors filmés, d'activer leur
son, de désactiver les cinématiques, et de **vérifier quels fichiers sont détectés**.

> ⚠️ Les décors vidéo exigent le **serveur** (`lancer.bat`). En double-clic sur
> `index.html`, les navigateurs bloquent la lecture des vidéos locales : le jeu
> affiche alors ses décors dessinés.

---

# 🏛️ LE SECRET DE LA DÉCLARATION

**Escape game immersif sur la Révolution française (1789) — CM1 / CM2**

Application web multimédia : personnages animés qui **parlent** (voix française), décors vivants inspirés des vrais lieux, sons, bibliothèque de leçons, module enseignant avec impression A4 et pilotage synchronisé des équipes.

---

## 🚀 DÉMARRAGE RAPIDE

### Mode simple (sans serveur prof) — 30 secondes
1. Ouvrez le dossier `PROJET ESCAPE GAMES`.
2. **Double-cliquez sur `index.html`**.
3. Le jeu s'ouvre dans votre navigateur. ✅ *Aucune installation.*

### Mode complet (avec pilotage prof synchronisé)
1. Vérifiez que **Python 3** est installé ([python.org](https://www.python.org/downloads/)).
2. **Double-cliquez sur `lancer.bat`** (Windows) ou `lancer-mac.command` (Mac).
3. Le serveur démarre et ouvre le navigateur automatiquement.
4. Notez l'**adresse IP locale** affichée (ex. : `http://192.168.1.35:8000/`).
5. Donnez cette adresse aux **postes élèves**.
6. Ouvrez `http://127.0.0.1:8000/prof.html` sur le **poste enseignant**.

> 💡 Sans Python : le mode simple (`index.html` double-clic) fonctionne sur **tout poste**, individuellement, sans réseau.

---

## 🎮 CE QUE VIT L'ÉLÈVE

| Élément | Description |
|---|---|
| 🎭 **Personnages plein corps animés** | Louise, Maître Gutenberg, le Marquis de Montclair, Maximilien — **corps entiers** dessinés en SVG : tête, torse, bras articulés, mains, jambes. Ils **respirent**, se balancent, **entrent en scène**, **gesticulent en parlant**, **pointent du doigt**, **sautent de joie** à la réussite |
| 🎙️ **Personnages qui parlent** | Bouche synchronisée sur la parole, clignement des yeux, sourcils expressifs + **voix française** du navigateur (Web Speech API) + sous-titres |
| 🔊 **Ambiances sonores synthétisées** | Chaque salle a sa bande-son **générée en direct par le navigateur** (aucun fichier à télécharger) : pluie et tonnerre au Palais-Royal, presse et bougie à l'imprimerie, oiseaux et vent aux Tuileries, foule, feu, canon et tocsin à la Bastille, murmure et pendule à l'Assemblée |
| 🎵 **Bruitages d'interaction** | Clic, réussite (arpège), erreur (deux notes douces, jamais punitives), fragment récupéré (scintillement), déverrouillage, fanfare de victoire |
| 🖼️ **Décors vivants** | 5 lieux de 1789 en style peinture d'époque : Palais-Royal sous la pluie, imprimerie à la bougie, Tuileries ensoleillées, Bastille fumante, Assemblée. Animations : pluie qui tombe, bougie vacillante, fumée, pendule… |
| 🎧 **Ambiance sonore** | Description immersive aux 5 sens, sons d'ambiance (en option) |
| 🧩 **5 énigmes interactives** | Différenciées CM1/CM2 : cahier de doléances codé, Marseillaise, rébus, portraits, mécanisme de l'Assemblée |
| 📚 **Bibliothèque de leçons** | 8 leçons consultables à tout moment (icône 📚) : textes + frises chronologiques + documents d'époque |
| ⏱️ **Minuteur + score + badges** | 55 min (réglables), points par énigme, bonus rapidité, 4 badges |
| 📝 **Quizz final** | 5 questions auto-corrigées |
| 💾 **Sauvegarde auto** | Reprend la partie après fermeture accidentelle |

---

## 👨‍🏫 MODULE ENSEIGNANT (icône ⚙️)

### Réglages accessibles
- **Agrandissement des textes** (100 % → 150 %, accessibilité malvoyants)
- **Voix ON/OFF** + volume des voix
- **Ambiances & bruitages ON/OFF** + volume séparé (pour ne pas gêner une classe voisine)
- **Animations réduites** : fige les mouvements de fond des personnages — utile pour les élèves sensibles au mouvement ou sur un poste lent
- **Durée du minuteur** (30 / 45 / 55 / 60 min)
- **Bibliothèque de leçons** activée/désactivée
- **Clé API IA** optionnelle (DeepSeek ou Albert) pour dialogues dynamiques
- **Choix du niveau** (CM1 / CM2)

### Impression A4 (fiches structurées, corrigés séparés)
Toutes les fiches respectent le **format A4 strict** (marges maîtrisées, aucune coupure, pagination, références complètes).

| Fiche | Contenu |
|---|---|
| 📋 **Fiches préparatoires** | 1 par salle (5 au total) : objectifs, vocabulaire, contexte |
| 📝 **QCM** | 10 questions (CM1) / 15 (CM2) — barème, corrigé séparé |
| ✅ **Questions fermées** | Vrai/Faux + réponses courtes — corrigé séparé |
| 📄 **Étude de documents** | Textes d'époque + questionnement type brevet — corrigé séparé |
| 🏆 **Bilan de partie** | Score, badges, temps — imprimable en fin de jeu |

> Chaque fiche porte : titre, niveau, salle concernée, cartouche élève, date, pagination, mention « CORRIGÉ » le cas échéant.

---

## 🌐 TABLEAU DE BORD PROF (`prof.html`)

Visible sur le poste enseignant quand le serveur tourne :

- 📊 **Vue temps réel** de toutes les équipes : salle atteinte, progression visuelle, score, fragments, temps, statut (en cours / en pause / terminé)
- ⏸ **Pause générale synchronisée** (toutes les équipes en même temps)
- ▶️ **Reprise générale**
- 📣 **Diffuser un message** à toutes les équipes
- 💡 **Donner un indice** à une équipe précise ou à toutes
- 📊 **Export CSV** des scores finaux
- 📱 **Adresse IP locale** affichée pour la donner aux élèves

---

## 🤖 IA OPTIONNELLE (avancé)

L'IA **n'est jamais obligatoire** : tous les dialogues sont pré-écrits et fonctionnent hors-ligne.

Si vous souhaitez des **dialogues dynamiques générés en temps réel** :
1. Ouvrez le module ⚙️ → section « IA optionnelle ».
2. Choisissez un fournisseur : **DeepSeek** ou **Albert** (service public français).
3. Saisissez votre clé API (stockée localement sur ce poste uniquement).
4. Activez l'IA.

En cas d'**échec réseau** ou d'**erreur**, l'application bascule automatiquement sur le contenu statique — l'expérience n'est jamais cassée.

---

## 📁 STRUCTURE DU PROJET

```
PROJET ESCAPE GAMES/
├── index.html              ← Point d'entrée élèves (double-clic)
├── prof.html               ← Tableau de bord enseignant
├── serveur.py              ← Serveur local (Python stdlib, 0 dépendance)
├── lancer.bat              ← Lancement Windows (double-clic)
├── lancer-mac.command      ← Lancement macOS/Linux
├── README.md               ← Ce guide
├── Le-Secret-de-la-Declaration.md  ← Script complet (référence)
├── css/
│   ├── style.css           ← Charte immersive tricolore
│   ├── animations.css      ← Lip-sync, décors animés
│   ├── personnages.css     ← Scène plein corps, gestes, respiration, entrées
│   └── print.css           ← Mise en page A4
├── js/
│   ├── portraits.js        ← Anciens portraits buste (conservés en secours)
│   ├── personnages.js      ← ★ Personnages PLEIN CORPS animés + gestes
│   ├── audio.js            ← ★ Moteur sonore Web Audio (ambiances + bruitages)
│   ├── decors.js           ← Décors SVG animés (5 salles)
│   ├── narration.js        ← Voix Web Speech API + sous-titres
│   ├── enigmes.js          ← 5 énigmes interactives
│   ├── lecons.js           ← Bibliothèque de leçons (modal)
│   ├── impression.js       ← Génération fiches A4 + corrigés
│   ├── reglages.js         ← Module enseignant
│   ├── api.js              ← IA optionnelle (DeepSeek/Albert)
│   ├── sync.js             ← Synchro élève ↔ serveur prof
│   └── app.js              ← Moteur principal
├── assets/
│   ├── images/
│   │   ├── decors/         ← ← ← Déposez ici vos décors IA (salle1.png … salle5.png)
│   │   ├── personnages/    ← ← ← Déposez ici vos portraits IA (louise.png, gutenberg.png…)
│   │   ├── documents/      ← Gravures d'époque (Wikimedia)
│   │   └── cartes/         ← Cartes & frises
│   ├── audio/              ← Ambiances sonores (optionnel)
│   └── data/
│       ├── dialogues.json  ← Tous les dialogues du jeu
│       ├── lecons.json     ← 8 leçons structurées
│       └── evaluations.json← Banque QCM + questions + études de docs
└── ancienne-version/       ← Prototype textuel initial (archive)
```

---

## 🎨 AMÉLIORER LES VISUELS (optionnel)

L'application fonctionne **immédiatement** avec des décors et portraits **SVG animés** dessinés à la main (intégrés au code).

Pour utiliser de **vraies images IA** (peintures d'époque) :

1. Générez les images avec un outil d'IA (DALL·E, Midjourney, ChatGPT…) en respectant les noms ci-dessous.
2. Déposez-les dans les dossiers correspondants.
3. L'application les **détectera automatiquement** et les utilisera à la place des SVG.

### Décors (format 16:9, dossier `assets/images/decors/`)
| Fichier | Sujet |
|---|---|
| `salle1.png` | Palais-Royal sous la pluie (1789) |
| `salle2.png` | Atelier d'imprimerie à la bougie |
| `salle3.png` | Jardins des Tuileries ensoleillés |
| `salle4.png` | Place de la Bastille fumante |
| `salle5.png` | Salle de l'Assemblée nationale |

### Portraits (format carré 1:1, dossier `assets/images/personnages/`)
| Fichier | Personnage |
|---|---|
| `louise.png` | Petite parisienne de 12 ans |
| `gutenberg.png` | Imprimeur barbu à lunettes |
| `marquis.png` | Aristocrate à perruque poudrée |
| `maximilien.png` | Jeune avocat idéaliste |

> 💡 Prompts détaillés : voir les sections 4 et 5 du fichier `Le-Secret-de-la-Declaration.md`.

---

## 🔧 EN CAS DE PROBLÈME

| Problème | Solution |
|---|---|
| `lancer.bat` affiche « Python n'est pas installé » | Installer Python 3, ou utiliser `index.html` en double-clic (mode autonome) |
| Pas de voix des personnages | Cliquer une fois sur la page (les navigateurs exigent une interaction) ; vérifier que la voix est activée dans ⚙️ |
| Pas d'ambiance sonore | Les navigateurs bloquent le son tant que l'élève n'a rien cliqué : le son démarre au premier clic. Vérifier aussi ⚙️ → « Ambiances & bruitages » |
| Le son gêne la classe voisine | ⚙️ → baisser « Volume des ambiances », ou couper « Ambiances & bruitages » (les voix restent actives) |
| Les personnages bougent trop (élève gêné) | ⚙️ → activer « Animations réduites ». Le réglage système « réduire les animations » de Windows/macOS est également respecté automatiquement |
| Pas de voix française | Installer une voix FR dans le système (Windows : Paramètres → Heure et langue → Langue → Français → Options → Télécharger les voix) |
| Page blanche | Ouvrir avec Chrome/Edge récent ; vérifier la console (F12) |
| Le serveur ne démarre pas | Vérifier que le port 8000 est libre ; utiliser `python serveur.py 9000` pour changer |
| Les équipes ne remontent pas dans le prof | Vérifier que les élèves utilisent l'adresse IP (pas `file://`) et que le pare-feu autorise Python |
| Je veux effacer une partie | Bouton « Rejouer » en fin de partie, ou vider le cache du navigateur |

---

## 📚 CONTENU PÉDAGOGIQUE

### Événements historiques travaillés
- **Mai 1789** — États généraux à Versailles
- **20 juin 1789** — Serment du Jeu de paume
- **14 juillet 1789** — Prise de la Bastille
- **Nuit du 4 août 1789** — Abolition des privilèges
- **26 août 1789** — Déclaration des droits de l'homme et du citoyen
- **5 octobre 1789** — Marche des femmes à Versailles

### Personnages
- **Fictifs** : Louise, Maître Gutenberg, Marquis de Montclair, Maximilien (inspiré de Robespierre).
- **Historiques** : Louis XVI, Mirabeau, Danton, Robespierre, Bailly, Olympe de Gouges, Voltaire, Rousseau.

### Notions-clés
Liberté · Égalité · Fraternité · Souveraineté nationale · DDHC · Cahier de doléances · Société d'ordres · Lumières.

---

## 🎓 BONNE AVENTURE, APPRENTIS HISTORIENS !

*Conçu avec GLM 5.2 · Révolution française · 1789*
