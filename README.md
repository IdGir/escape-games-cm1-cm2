# 🎓 ESCAPE GAMES PÉDAGOGIQUES — CM1 / CM2

Guide pratique : **lancer chaque jeu depuis Chrome**, et **ajouter ou remplacer
des images/vidéos directement sur GitHub**, sans rien installer.

> 📁 Dépôt GitHub : **https://github.com/IdGir/escape-games-cm1-cm2**
> 🌐 Site en ligne : **https://idgir.github.io/escape-games-cm1-cm2/**

---

## 🚀 Lancer les jeux (dans Chrome, aucune installation)

Cliquez simplement sur l'adresse, ou copiez-la dans un nouvel onglet Chrome —
sur PC, TBI Android ou Chromebook, ça marche pareil :

| Jeu | Adresse à ouvrir dans Chrome |
|---|---|
| 🏛️ **Le Secret de la Déclaration** (Histoire, 1789) | [idgir.github.io/escape-games-cm1-cm2/](https://idgir.github.io/escape-games-cm1-cm2/) |
| 🧭 **Le Tour du Monde en 80 minutes** (Géographie) | [idgir.github.io/escape-games-cm1-cm2/tour-du-monde/](https://idgir.github.io/escape-games-cm1-cm2/tour-du-monde/) |
| 🗺️ **Mission géographique — Année A** (Géographie, année entière) | [idgir.github.io/escape-games-cm1-cm2/mission-geo/](https://idgir.github.io/escape-games-cm1-cm2/mission-geo/) |

💡 **Astuce classe** : mettez ces trois adresses en **favoris Chrome** (étoile
dans la barre d'adresse) sur chaque poste/TBI une fois pour toutes — les élèves
n'auront plus qu'à cliquer sur le favori.

Chaque élève/équipe garde sa progression automatiquement sur **l'appareil
utilisé** (même onglet, même navigateur). Pas besoin de compte, pas de wifi
particulier au-delà d'une connexion internet normale.

> ⚠️ **Ce qui ne fonctionne PAS en ligne** : le **tableau de bord enseignant
> synchronisé en direct** (`prof.html` qui suit les équipes en temps réel)
> a besoin d'un petit serveur qui tourne sur un ordinateur — GitHub ne peut
> pas le faire tourner. Tout le reste (le jeu, les leçons, les fiches à
> imprimer) fonctionne parfaitement en ligne. Voir [tout en bas](#-pour-aller-plus-loin--le-mode-serveur-local) si vous voulez ce mode avancé.

---

## 🖼️ Ajouter ou remplacer une image / vidéo

Chaque décor, personnage ou carte a un **nom de fichier attendu**, propre à
**un seul dossier canonique**. Déposez un fichier portant ce nom dans ce
dossier, et il remplace automatiquement le dessin par défaut — **rien à
modifier dans le code**.

> ⚠️ **Un seul et même dossier fait foi pour chaque jeu : `assets/` à sa
> racine.** Le dossier `Elements EG/` (utilisé dans une version antérieure)
> n'est plus la référence — ne l'utilisez plus, pour éviter d'avoir deux
> emplacements possibles pour la même image.

### Deux façons d'envoyer un fichier — au choix

**A. Directement sur GitHub (aucune installation)**
1. Ouvrez le dossier concerné sur GitHub (liens ci-dessous, un par jeu).
2. **Add file** (en haut à droite) → **Upload files**.
3. Glissez votre fichier, **renommez-le exactement** comme indiqué dans le
   `README.md` de ce dossier (visible directement sous la liste des fichiers,
   sur la page GitHub du dossier).
4. En bas de page, laissez **« Commit directly to the main branch »** coché
   → **Commit changes**.

**B. Dans le dossier du projet sur votre ordinateur**
1. Placez le fichier, avec le bon nom, directement dans le sous-dossier
   `assets/...` correspondant du projet (celui que Claude Code utilise).
2. Dites-le-moi (« j'ai déposé tel fichier ») : je le publie sur GitHub pour vous.

Dans les deux cas, **c'est en ligne en général en moins d'une minute** une
fois le commit fait — rechargez avec **Ctrl+F5** pour forcer le rechargement.

### Formats acceptés
- **Images** : `.jpg`, `.png`, `.webp` — format **16:9** pour les décors,
  **carré (1:1)** pour les portraits de personnages.
- **Vidéos** : `.mp4` (recommandé) ou `.webm` — plutôt **courtes** (15-30 s en
  boucle) et **légères** (moins de 20 Mo) pour un chargement rapide.
- Si vous déposez à la fois une vidéo et une image du même nom, **la vidéo est
  prioritaire**. Sans aucun fichier, le jeu affiche son décor dessiné —
  ce n'est jamais une erreur, juste le mode par défaut.
- **Noms de fichiers toujours en minuscules** (`salle1.jpg`, pas `Salle1.jpg`) :
  le site est sensible à la casse, une majuscule empêche la détection.

---

### 🏛️ Le Secret de la Déclaration — dossiers médias

Dossier GitHub : [`/assets/`](https://github.com/IdGir/escape-games-cm1-cm2/tree/main/assets) — chaque sous-dossier a son propre `README.md` avec la liste exacte des noms attendus et ce qui est déjà en ligne.

| Sous-dossier | Contenu |
|---|---|
| [`assets/videos/`](assets/videos/) | Décors filmés des 5 salles + cinématiques *(salle1 déjà en ligne)* |
| [`assets/images/decors/`](assets/images/decors/) | Images des mêmes décors *(salle4 déjà en ligne)* |
| [`assets/images/personnages/`](assets/images/personnages/) | Portraits de Louise, Gutenberg, le Marquis, Maximilien |
| [`assets/videos/personnages/`](assets/videos/personnages/) | Mêmes personnages, en vidéo |
| [`assets/images/documents/`](assets/images/documents/) | Documents d'époque des leçons |

> 💡 Prompts prêts à copier-coller pour générer les images de salles avec une
> IA : sections 4-5 de [`Le-Secret-de-la-Declaration.md`](Le-Secret-de-la-Declaration.md).

---

### 🧭 Le Tour du Monde en 80 minutes — dossiers médias

Dossier GitHub : [`/tour-du-monde/assets/`](https://github.com/IdGir/escape-games-cm1-cm2/tree/main/tour-du-monde/assets)

| Sous-dossier | Contenu |
|---|---|
| [`tour-du-monde/assets/videos/`](tour-du-monde/assets/videos/) | Décors filmés des 5 escales + cinématiques *(tout déjà en ligne)* |
| [`tour-du-monde/assets/images/decors/`](tour-du-monde/assets/images/decors/) | Images des mêmes décors *(intro déjà en ligne)* |
| [`tour-du-monde/assets/images/personnages/`](tour-du-monde/assets/images/personnages/) | Portraits de Fogg, Passepartout, Aouda, Fix |
| [`tour-du-monde/assets/videos/personnages/`](tour-du-monde/assets/videos/personnages/) | Mêmes personnages, en vidéo |
| [`tour-du-monde/assets/images/cartes/`](tour-du-monde/assets/images/cartes/) | Planisphère *(déjà en ligne)* et paysages des climats |
| [`tour-du-monde/assets/images/documents/`](tour-du-monde/assets/images/documents/) | Documents d'époque des leçons |

---

### 🗺️ Mission géographique — Année A — dossiers médias

Dossier GitHub : [`/mission-geo/assets/`](https://github.com/IdGir/escape-games-cm1-cm2/tree/main/mission-geo/assets)

Ce jeu a **16 séances × plusieurs emplacements** : tout est **à plat**, pas de
sous-dossiers.

| Sous-dossier | Contenu |
|---|---|
| [`mission-geo/assets/videos/`](mission-geo/assets/videos/) | Toutes les vidéos, `<nom>.mp4` |
| [`mission-geo/assets/images/`](mission-geo/assets/images/) | Toutes les images, `<nom>.jpg` |

📄 La **liste complète et exacte des noms attendus** (un par séance et par
emplacement) est dans
**[`mission-geo/assets/OU-DEPOSER-VOS-MEDIAS.txt`](https://github.com/IdGir/escape-games-cm1-cm2/blob/main/mission-geo/assets/OU-DEPOSER-VOS-MEDIAS.txt)**
— à consulter avant chaque envoi.

---

## ✅ Vérifier que vos médias sont bien détectés

Dans chaque jeu, ouvrez le module enseignant (icône **⚙️**) puis
**Multimédia → « Vérifier les fichiers présents »** (ou « Vérifier les
fichiers détectés » selon le jeu). Le jeu liste, décor par décor, s'il a
trouvé une vidéo, une image, ou s'il utilise le dessin par défaut.

---

## 👨‍🏫 Modules enseignant, impressions, leçons

Chaque jeu a son propre module ⚙️ (accessibilité, sons, minuteur, choix
CM1/CM2) et ses fiches A4 imprimables (préparation, élève, corrigé, bilan) —
tout cela fonctionne **directement en ligne**, sans serveur. Le détail complet
de chaque jeu (énigmes, personnages, notions travaillées, dépannage) est dans
son propre README :

- [`tour-du-monde/README.md`](tour-du-monde/README.md)
- [`mission-geo/README.md`](mission-geo/README.md)

---

## 🔧 En cas de problème

| Problème | Solution |
|---|---|
| Mon image/vidéo n'apparaît pas après l'envoi | Ctrl+F5 pour forcer le rechargement ; vérifiez le **nom exact** (minuscules, bon dossier, bonne extension) ; ⚙️ → Multimédia → « Vérifier les fichiers » |
| J'ai renommé un fichier mais l'ancien reste affiché | Le navigateur garde une copie en cache : Ctrl+F5, ou attendez quelques minutes |
| Le tableau de bord prof n'affiche aucune équipe | Normal en ligne (GitHub Pages) : ce module a besoin du [mode serveur local](#-pour-aller-plus-loin--le-mode-serveur-local) |
| Page blanche ou jeu figé | Utilisez Chrome ou Edge à jour ; rechargez la page |
| Je veux effacer la progression d'un élève | Bouton « Rejouer » en fin de partie, ou effacer les données de navigation de cet onglet |

---

## 🔬 Pour aller plus loin : le mode serveur local

Si un jour vous voulez le **tableau de bord enseignant en direct** (suivi
équipe par équipe pendant la partie, pause générale, indices envoyés à la
volée), il faut faire tourner le petit serveur inclus sur **un ordinateur de
la classe** :

1. Téléchargez le dépôt (`Code` → `Download ZIP` sur GitHub), ou clonez-le.
2. Vérifiez que **Python 3** est installé.
3. Double-cliquez sur `lancer.bat` (Windows) ou `lancer-mac.command` (Mac).
4. Donnez aux élèves l'adresse IP locale affichée par le serveur ; ouvrez
   `prof.html` sur votre poste.

Ce mode est **optionnel** : tout le contenu pédagogique (jeu, leçons, fiches)
est identique en ligne et en local. Détails complets dans les README de
chaque jeu.

---

## 🎓 Bonne aventure, apprentis chercheurs !

*Trois escape games pédagogiques, CM1-CM2 · Histoire et Géographie*
