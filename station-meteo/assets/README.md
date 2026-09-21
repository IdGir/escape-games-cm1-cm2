# 🎞️ Médias du jeu — La Station météo disparue

**Tout est facultatif.** Sans aucun fichier, le jeu affiche ses décors et ses personnages
dessinés en SVG, animés : c'est le mode par défaut, entièrement jouable. Déposer un fichier
portant exactement le nom attendu le fait apparaître à la place du dessin — **aucun code à
modifier**. Aucun média n'a été produit pour ce jeu : cette page liste seulement les
emplacements prévus.

La page de vérification ([verifier.html](../../verifier.html#station-meteo)) et ⚙️ Réglages →
« 🔍 Vérifier les fichiers présents » affichent, pour chaque emplacement, ce qui est en place
et le nom exact à utiliser.

## Règles de nommage

- Noms **en minuscules, sans espace ni accent** : `salle1.jpg`, jamais `Salle 1.JPG`.
- Vidéo **et** image du même nom : la vidéo s'affiche, l'image lui sert d'affiche.
- Un fichier `.vtt` du même nom qu'une vidéo est chargé automatiquement comme sous-titres.
- Les décors filmés sont joués **muets** (un bouton 🔇 permet d'activer le son).
- Supprimer un fichier ramène le dessin par défaut.
- **Aucune valeur météorologique** ne doit apparaître sur une photo ou une vidéo si elle
  contredit les relevés du jeu (21 °C, 24 km/h, 7 mm mercredi) : préférer des instruments
  sans affichage lisible.

| | Formats acceptés |
|---|---|
| Décors et cinématiques | `.mp4` (H.264) ou `.webm`, 16:9, 15 à 30 s en boucle, < 20 Mo — ou `.jpg` / `.png` / `.webp` 16:9 |
| Personnages | `.mp4` en boucle, cadrage portrait vertical — ou `.png` carré à fond transparent (`.gif` animé accepté) |
| Illustrations d'énigmes | `.jpg` (ou `.png` / `.webp`) |

---

## 1. Décors et cinématiques — `assets/videos/` et `assets/images/decors/`

| Emplacement | Nom du fichier | Où il apparaît | Idée de prise de vue |
|---|---|---|---|
| Cinématique d'ouverture | `intro.mp4` | Plein écran au clic sur « Remettre la station en service ». Sautée si absente. | La cour au petit matin après un orage |
| Module 1 — L'abri météo | `salle1.mp4` *ou* `salle1.jpg` | Décor du module 1 et fond de l'écran d'accueil | Un abri blanc à persiennes sur une pelouse |
| Module 2 — Le mât du vent | `salle2.mp4` *ou* `salle2.jpg` | Décor du module 2 | Anémomètre à coupelles et girouette en haut d'un mât |
| Module 3 — Le pluviomètre | `salle3.mp4` *ou* `salle3.jpg` | Décor du module 3 | Pluviomètre dans un jardin, sous la pluie |
| Module 4 — Le tableau des relevés | `salle4.mp4` *ou* `salle4.jpg` | Décor du module 4 | Un bureau, un tableau de relevés, un graphique au mur |
| Module 5 — Le bulletin du jour | `salle5.mp4` *ou* `salle5.jpg` | Décor du module 5 | Un plateau de bulletin météo, une carte à l'écran |
| Cinématique de fin | `final.mp4` | Plein écran quand la station repart. Sautée si absente. | Le soleil revient sur la cour |

Les vidéos vont dans `assets/videos/`, les images dans `assets/images/decors/`.

## 2. Personnages — `assets/videos/personnages/` et `assets/images/personnages/`

| Personnage | Nom du fichier | Variante « parle » (facultative) | Modules |
|---|---|---|---|
| Madame Vasseur, prévisionniste | `vasseur.mp4` *ou* `vasseur.png` | `vasseur-parle.mp4` | accueil, 1, 5 |
| Capitaine Keïta, marin | `keita.mp4` *ou* `keita.png` | `keita-parle.mp4` | 2 |
| Tiago, technicien de la station | `tiago.mp4` *ou* `tiago.png` | `tiago-parle.mp4` | 3 |
| Lina, élève responsable de la station | `lina.mp4` *ou* `lina.png` | `lina-parle.mp4` | 4, fin |

Personnages fictifs : n'utiliser l'image d'aucune personne réelle, ni d'élève.

## 3. Illustrations d'énigmes (facultatives) — `assets/images/cartes/`

Déclarées dans `assets/data/enigmes.json` (bloc `media`). Sans fichier, un encadré discret
rappelle le nom attendu et l'énigme reste jouable.

| Énigme | Nom du fichier | Contenu attendu |
|---|---|---|
| 1-2 · Où placer le thermomètre ? | `e1-2.jpg` | Un abri météorologique à persiennes |
| 2-2 · Girouette et anémomètre | `e2-2.jpg` | Une girouette et un anémomètre à coupelles |
| 3-2 · Un millimètre de pluie | `e3-2.jpg` | Un pluviomètre gradué installé dans un jardin |

Source et licence de chaque photo à noter dans un fichier `assets/images/cartes/CREDITS.md`
(photos libres de droits, par exemple Wikimedia Commons, ou photos de la station de
l'école sans élève reconnaissable).

## 4. Documents des leçons

Les leçons de ce jeu sont des **textes rédigés avec schémas SVG** (`assets/data/lecons.json`) :
aucun fichier n'est attendu. Le dossier `assets/images/documents/` est réservé à un usage
futur.
