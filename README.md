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

## 🖼️ Ajouter ou remplacer une image / vidéo sur GitHub

Chaque décor, personnage ou carte a un **nom de fichier attendu**. Déposez un
fichier portant ce nom au bon endroit sur GitHub, et il remplace automatiquement
le dessin par défaut — **rien à modifier dans le code**, pas besoin d'ouvrir
un logiciel de développement.

### La marche à suivre (identique pour tous les jeux)

1. Ouvrez le dossier concerné sur GitHub (liens ci-dessous pour chaque jeu).
2. Cliquez sur **Add file** (en haut à droite) → **Upload files**.
3. Glissez votre image ou vidéo dans la zone, **renommez-la exactement** comme
   indiqué dans les tableaux ci-dessous (GitHub permet de renommer avant
   d'envoyer, en cliquant sur le nom du fichier affiché).
4. Si le dossier n'existe pas encore, tapez son chemin complet dans le nom du
   fichier au moment de l'envoi, par exemple `assets/images/decors/salle1.jpg`
   — GitHub crée le dossier tout seul.
5. En bas de page, laissez **« Commit directly to the main branch »** coché,
   puis cliquez sur **Commit changes**.
6. Rechargez le jeu dans Chrome (**Ctrl+F5** pour forcer le rechargement, au
   cas où le navigateur aurait gardé l'ancienne version en mémoire). C'est en
   ligne en général en moins d'une minute.

> Aucune ligne de commande, aucun logiciel Git à installer : tout se fait dans
> le navigateur, sur la page GitHub.

### Formats acceptés
- **Images** : `.jpg`, `.png`, `.webp` — format **16:9** pour les décors,
  **carré (1:1)** pour les portraits de personnages.
- **Vidéos** : `.mp4` (recommandé) ou `.webm` — plutôt **courtes** (15-30 s en
  boucle) et **légères** (moins de 20 Mo) pour un chargement rapide.
- Si vous déposez à la fois une vidéo et une image du même nom, **la vidéo est
  prioritaire**. Sans aucun fichier, le jeu affiche son décor dessiné —
  ce n'est jamais une erreur, juste le mode par défaut.

---

### 🏛️ Le Secret de la Déclaration — dossiers médias

Dossier GitHub : [`/assets/`](https://github.com/IdGir/escape-games-cm1-cm2/tree/main/assets)

| Type | Dossier à ouvrir sur GitHub | Fichiers attendus |
|---|---|---|
| Décors des 5 salles | `assets/images/decors/` (vidéo : `assets/videos/`) | `salle1.jpg` … `salle5.jpg` (ou `.mp4`) |
| Cinématiques d'intro/fin | même dossiers | `intro.jpg`/`intro.mp4`, `final.jpg`/`final.mp4` |
| Portraits des personnages | `assets/images/personnages/` (vidéo : `assets/videos/personnages/`) | `louise`, `gutenberg`, `marquis`, `maximilien` (`.png` ou `.mp4`) |
| Variante « en train de parler » (optionnel) | même dossier vidéo | `louise-parle.mp4`, etc. |
| Documents d'époque (dans les leçons) | `assets/images/documents/` | nom indiqué dans la leçon concernée |

> Ces dossiers `assets/images/` et `assets/videos/` n'existent pas encore sur
> GitHub pour ce jeu (le jeu tourne pour l'instant sur ses décors dessinés) —
> ils seront créés automatiquement dès votre premier envoi.
> 💡 Prompts prêts à copier-coller pour générer les 5 images de salles avec
> une IA d'images : voir la réponse précédente dans cette conversation, ou
> les sections 4-5 de [`Le-Secret-de-la-Declaration.md`](Le-Secret-de-la-Declaration.md).

---

### 🧭 Le Tour du Monde en 80 minutes — dossiers médias

Dossier GitHub : [`/tour-du-monde/assets/`](https://github.com/IdGir/escape-games-cm1-cm2/tree/main/tour-du-monde/assets)

| Type | Dossier à ouvrir sur GitHub | Fichiers attendus |
|---|---|---|
| Décors des 5 escales | `tour-du-monde/assets/images/decors/` (vidéo : `tour-du-monde/assets/videos/`) | `etape1.jpg` … `etape5.jpg` (ou `.mp4`) |
| Cinématiques d'intro/fin | mêmes dossiers | `intro.jpg`/`.mp4` *(déjà en ligne)*, `final.jpg`/`.mp4` |
| Portraits des personnages | `tour-du-monde/assets/images/personnages/` (vidéo : `.../videos/personnages/`) | `fogg`, `passepartout`, `aouda`, `fix` (`.png` ou `.mp4`) |
| Cartes et paysages | `tour-du-monde/assets/images/cartes/` | `planisphere.jpg`, `paysage-desert.jpg`, `paysage-jungle.jpg`, `paysage-montagne.jpg`, `paysage-campagne.jpg`, `paysage-banquise.jpg`, `paysage-savane.jpg` |
| Documents d'époque (dans les leçons) | `tour-du-monde/assets/images/documents/` | nom indiqué dans la leçon concernée |

---

### 🗺️ Mission géographique — Année A — dossiers médias

Dossier GitHub : [`/mission-geo/assets/`](https://github.com/IdGir/escape-games-cm1-cm2/tree/main/mission-geo/assets)

Ce jeu a **16 séances × plusieurs emplacements** : plutôt qu'un tableau géant,
la **liste complète et exacte des noms attendus** est dans un fichier texte
dédié, à consulter avant chaque envoi :

📄 **[`mission-geo/assets/OU-DEPOSER-VOS-MEDIAS.txt`](https://github.com/IdGir/escape-games-cm1-cm2/blob/main/mission-geo/assets/OU-DEPOSER-VOS-MEDIAS.txt)**

En résumé :
- Vidéos → `mission-geo/assets/videos/<nom>.mp4`
- Images → `mission-geo/assets/images/<nom>.jpg`
- Le `<nom>` exact (ex. `s01-intro`, `s02-plan-dijon`, `recompense`…) est donné
  séance par séance dans le fichier ci-dessus.

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
