# 🎞️ Médias du jeu — Le Sceau de la République

> **Production automatique :** double-cliquez sur `medias/produire-medias.bat` pour
> installer les photographies des cinq lieux réels et générer les personnages et les
> cinématiques. Crédits et licences : [`medias/CREDITS.md`](medias/CREDITS.md).

**Tout est facultatif.** Sans aucun fichier, le jeu affiche ses décors et ses personnages
dessinés en SVG, animés : c'est le mode par défaut, entièrement jouable. Déposer un fichier
portant exactement le nom attendu le fait apparaître à la place du dessin — **aucun code à
modifier**.

La page de vérification ([verifier.html](../../verifier.html#constitution)) et ⚙️ Réglages →
« 🔍 Vérifier les fichiers présents » affichent, pour chaque emplacement, ce qui est en place
et le nom exact à utiliser.

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
| Illustrations d'énigmes et documents | `.jpg` (ou `.png` / `.webp`) |

---

## 1. Décors et cinématiques — `assets/videos/` et `assets/images/decors/`

| Emplacement | Nom du fichier | Où il apparaît |
|---|---|---|
| Cinématique d'ouverture | `intro.mp4` | Plein écran au clic sur « Ouvrir le coffre ». Sautée si absente. |
| Salle 1 — La cour du Palais-Royal | `salle1.mp4` *ou* `salle1.jpg` | Décor de fond de la salle, et fond de l'écran d'accueil |
| Salle 2 — La salle des Textes | `salle2.mp4` *ou* `salle2.jpg` | Décor de fond de la salle |
| Salle 3 — L'hémicycle | `salle3.mp4` *ou* `salle3.jpg` | Décor de fond de la salle |
| Salle 4 — La navette parlementaire | `salle4.mp4` *ou* `salle4.jpg` | Décor de fond de la salle |
| Salle 5 — La salle des séances du Conseil constitutionnel | `salle5.mp4` *ou* `salle5.jpg` | Décor de fond de la salle |
| Cinématique de fin | `final.mp4` | Plein écran quand le coffre s'ouvre. Sautée si absente. |

Les vidéos vont dans `assets/videos/`, les images dans `assets/images/decors/`.

**Les décors fournis sont de vraies photographies**, pas des images inventées : cour du
Palais-Royal (colonnes de Buren), salle de consultation des Archives nationales, hémicycle de
l'Assemblée nationale, hémicycle du Sénat, salle des délibérés du Conseil constitutionnel.
Elles viennent de Wikimedia Commons sous licence libre — auteur et licence sont rappelés dans
⚙️ Réglages → « Crédits des médias » et dans [`medias/CREDITS.md`](medias/CREDITS.md).

## 2. Personnages — `assets/videos/personnages/` et `assets/images/personnages/`

| Personnage | Rôle | Nom du fichier | Variante « parle » |
|---|---|---|---|
| Monsieur Berthier | Gardien-archiviste du Palais-Royal | `berthier.mp4` *ou* `berthier.png` | `berthier-parle.mp4` (facultative) |
| Nour | Déléguée de classe, 10 ans | `nour.mp4` *ou* `nour.png` | `nour-parle.mp4` (facultative) |
| Madame Ferrand | Députée à l'Assemblée nationale | `ferrand.mp4` *ou* `ferrand.png` | `ferrand-parle.mp4` (facultative) |
| Maître Sylla | Juriste au Conseil constitutionnel | `sylla.mp4` *ou* `sylla.png` | `sylla-parle.mp4` (facultative) |

La variante `-parle` est jouée pendant que le personnage parle ; sans elle, la vidéo au repos
est conservée.

Les quatre personnages sont **fictifs** : ils sont générés à partir des descriptions de
`medias/medias.json`, qui demandent explicitement de ne ressembler à aucune personne réelle.
Nour, l'élève, est rendue en style illustré plutôt que photoréaliste.

## 3. Illustrations d'énigmes — `assets/images/cartes/`

Chaque illustration est **facultative** : sans fichier, l'énigme reste entièrement jouable et
un encadré discret rappelle le nom attendu. Ces emplacements sont déclarés dans
`assets/data/enigmes.json` (champ `media`) : en ajouter un ne demande aucune modification de code.

| Énigme | Nom du fichier | Légende prévue |
|---|---|---|
| 1-1 — La règle du jeu (salle 1) | `e1-1.jpg` | Le coffre scellé le 4 octobre 1958 — *généré* |
| 1-3 — Les trois pouvoirs (salle 1) | `e1-3.jpg` ✅ | La séparation des pouvoirs |
| 2-1 — Les quatre textes, dans l'ordre (salle 2) | `e2-1.jpg` ✅ | Le bloc de constitutionnalité |
| 3-1 — Qui fait quoi dans la République ? (salle 3) | `e3-1.jpg` ✅ | L'organisation des pouvoirs |
| 4-2 — Le parcours d'une loi (salle 4) | `e4-2.jpg` ✅ | Le parcours d'une loi, étape par étape |
| 5-1 — Les articles 1 et 2 (salle 5) | `e5-1.jpg` ✅ | Les symboles de la République |
| 5-3 — La Constitution dans ton quotidien (salle 5) | `e5-3.jpg` | La Constitution dans ton quotidien |

Les cinq schémas marqués ✅ sont **déjà fournis** : ce sont des schémas dessinés pour le jeu,
dont chaque information provient d'une fiche officielle citée en bas de l'image. Les deux autres
(`e1-1`, `e5-3`) sont produits par `medias/produire-medias.bat`.

Pour qu'une illustration soit une **vidéo**, ajoutez `"type": "video"` dans le bloc `media` de
l'énigme et déposez `<nom>.mp4` dans `assets/videos/`.

## 4. Fiches officielles des leçons — `assets/lecons/`

Les leçons du jeu (📚) **sont** les 16 documents PDF officiels du site
« Découvrons notre Constitution ». Ce ne sont pas des médias facultatifs comme les décors :
ils constituent le contenu pédagogique du jeu.

- **Installation :** double-cliquez sur `assets/lecons/telecharger-fiches.bat`.
- **Liste complète, noms attendus et liens :** [`assets/lecons/README.md`](lecons/README.md).
- **Si un fichier manque :** la leçon ouvre le document sur le site officiel — rien n'est cassé.
- **Vérification :** ⚙️ Réglages → « 🔍 Vérifier les fichiers présents », ou `verifier.html`
  à la racine du dépôt (onglet ⚖️, famille « Fiches officielles »).

Aucune image n'est attendue dans `assets/images/documents/` : ce dossier n'est plus utilisé.

## 5. Où trouver des images libres de droits

- **Conseil constitutionnel** — photographies du Palais-Royal et de la salle des séances.
- **Assemblée nationale** et **Sénat** — visuels de l'hémicycle et du palais du Luxembourg.
- **Wikimedia Commons** — vérifiez la licence de chaque fichier avant de le publier.

Vérifiez toujours les droits avant de publier le dépôt en ligne : les fichiers déposés ici
sont accessibles publiquement.
