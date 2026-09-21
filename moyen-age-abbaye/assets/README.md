# 🎞️ Médias du jeu — Le Manuscrit de l'abbaye

**Tout est facultatif.** Sans aucun fichier, le jeu affiche ses décors et ses personnages dessinés en
SVG, animés : c'est le mode par défaut, entièrement jouable. Déposer un fichier portant exactement le
nom attendu le fait apparaître à la place du dessin — **aucun code à modifier**.

Aucun média n'est fourni pour l'instant. La page de vérification
([verifier.html](../../verifier.html#moyen-age-abbaye)) et ⚙️ Réglages → « 🔍 Vérifier les fichiers
présents » affichent, pour chaque emplacement, ce qui est en place et le nom exact à utiliser.

## Règles de nommage

- Noms **en minuscules, sans espace ni accent** : `salle1.jpg`, jamais `Salle 1.JPG`.
- Vidéo **et** image du même nom : la vidéo s'affiche, l'image lui sert d'affiche.
- Un fichier `.vtt` du même nom qu'une vidéo est chargé automatiquement comme sous-titres.
- Les décors filmés sont joués **muets** (un bouton 🔇 permet d'activer le son).
- Supprimer un fichier ramène le dessin par défaut.

| | Formats acceptés |
|---|---|
| Décors et cinématiques | `.mp4` (H.264) ou `.webm`, 16:9, 15 à 30 s en boucle, < 20 Mo — ou `.jpg` / `.png` / `.webp` 16:9 |
| Personnages | `.mp4` en boucle, cadrage portrait vertical — ou `.png` carré à fond transparent (`.gif` animé accepté) |
| Illustrations d'énigmes | `.jpg` (ou `.png` / `.webp`) |

---

## 1. Décors et cinématiques — `assets/videos/` et `assets/images/decors/`

| Emplacement | Nom du fichier | Où il apparaît | Idée de visuel |
|---|---|---|---|
| Cinématique d'ouverture | `intro.mp4` | Plein écran au clic sur « Prendre la plume ». Sautée si absente. | Un livre enluminé qu'on ouvre : des pages manquent |
| Salle 1 — Reims, le baptême de Clovis | `salle1.mp4` *ou* `salle1.jpg` | Décor de fond de la salle 1 | Enluminure du baptême de Clovis (Grandes Chroniques de France, BnF / Gallica) |
| Salle 2 — Aix-la-Chapelle | `salle2.mp4` *ou* `salle2.jpg` | Décor de fond de la salle 2 | Intérieur de la chapelle palatine d'Aix-la-Chapelle |
| Salle 3 — Le scriptorium | `salle3.mp4` *ou* `salle3.jpg` | Décor de la salle 3 **et fond de l'écran d'accueil** | Salle des moines de l'abbaye de Fontenay, ou enluminure d'un copiste au travail |
| Salle 4 — L'hôtel-Dieu | `salle4.mp4` *ou* `salle4.jpg` | Décor de fond de la salle 4 | Grande salle des pôvres de l'hôtel-Dieu de Beaune |
| Salle 5 — Le chantier | `salle5.mp4` *ou* `salle5.jpg` | Décor de fond de la salle 5 | Nef romane et chœur gothique de Vézelay, ou chantier de cathédrale en enluminure |
| Cinématique de fin | `final.mp4` | Plein écran quand le fermoir s'ouvre. Sautée si absente. | Le livre complet qui se referme |

Les vidéos vont dans `assets/videos/`, les images dans `assets/images/decors/`.

## 2. Personnages — `assets/videos/personnages/` et `assets/images/personnages/`

| Personnage | Rôle | Nom du fichier | Variante « parle » |
|---|---|---|---|
| Frère Anselme | Moine copiste de l'abbaye (salles 1 et 3, intro, fermoir) | `anselme.mp4` *ou* `anselme.png` | `anselme-parle.mp4` (facultative) |
| Aude | Élève de l'école du palais, 11 ans (salle 2) | `aude.mp4` *ou* `aude.png` | `aude-parle.mp4` (facultative) |
| Mère Alix | Abbesse, responsable de l'hôtel-Dieu (salle 4) | `alix.mp4` *ou* `alix.png` | `alix-parle.mp4` (facultative) |
| Garin | Apprenti tailleur de pierre, 12 ans (salle 5) | `garin.mp4` *ou* `garin.png` | `garin-parle.mp4` (facultative) |

La variante `-parle` est jouée pendant que le personnage parle. Les quatre personnages sont **fictifs** :
s'ils sont générés, demander explicitement qu'ils ne ressemblent à aucune personne réelle, et rendre
les deux enfants (Aude, Garin) en style illustré plutôt que photoréaliste.

## 3. Illustrations d'énigmes — `assets/images/cartes/`

Déclarées dans `assets/data/enigmes.json` (champ `media`). Sans fichier, l'énigme reste jouable et un
encadré discret rappelle le nom attendu.

| Énigme | Nom du fichier | Légende prévue | Piste de source |
|---|---|---|---|
| 1-2 — La frise de la première page | `e1-2.jpg` | Le baptême de Clovis dans un manuscrit médiéval | Grandes Chroniques de France, BnF / Gallica |
| 2-3 — La carte de l'empire | `e2-3.jpg` | L'empire de Charlemagne en 814 | Carte d'atlas historique libre de droits |
| 3-2 — Comment naît un livre | `e3-2.jpg` | Une page de manuscrit enluminé, avec sa lettrine | BnF / Gallica, base Enluminures |
| 4-1 — Les documents de l'hôtel-Dieu | `e4-1.jpg` | La grande salle des malades de l'hôtel-Dieu de Beaune | Hospices civils de Beaune, Wikimedia Commons |
| 5-1 — Légende les deux églises | `e5-1.jpg` | Coupe d'une église romane et d'une cathédrale gothique | Schéma dessiné (un schéma est déjà dans la leçon 📚) |

Pour qu'une illustration soit une **vidéo**, ajoutez `"type": "video"` dans le bloc `media` de l'énigme et
déposez `<nom>.mp4` dans `assets/videos/`.

## 4. Où trouver des images libres de droits

- **BnF — Gallica** et **base Enluminures** (culture.fr) : manuscrits médiévaux ; vérifier les conditions
  de réutilisation indiquées sur chaque notice.
- **Wikimedia Commons** : photographies de Cluny, Vézelay, Fontenay, Beaune, Aix-la-Chapelle ; vérifier la
  licence de chaque fichier et noter l'auteur.
- **Réunion des musées nationaux (RMN)** : consultation ; la réutilisation est en général soumise à droits.

Vérifiez toujours les droits avant de publier le dépôt en ligne : les fichiers déposés ici sont
accessibles publiquement. Notez l'auteur et la licence de chaque fichier dans un `CREDITS.md`.
