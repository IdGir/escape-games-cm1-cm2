# 🎞️ Médias — Mission géographique, Année A

Tous les médias du jeu sont dans ce dossier, `mission-geo/assets/`, **à plat** :

- vidéos → `videos/<nom>.mp4` (ou `.webm`, `.m4v`)
- images → `images/<nom>.jpg` (ou `.png`, `.webp`, `.gif`, `.svg`)

Pour chaque emplacement, le jeu cherche d'abord la vidéo, puis l'image, puis
retombe sur son dessin intégré (ou masque l'emplacement). **Aucun fichier
n'est obligatoire.**

👉 Ce qui est déjà en place, avec aperçu, séance par séance :
[page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#mission-geo)
(en local : http://127.0.0.1:8000/verifier.html).
Comment déposer un fichier : [README principal, § 3](../../README.md#3-ajouter-ou-remplacer-une-image-ou-une-vidéo).

**Exemple** : pour illustrer l'introduction de la séance 1, déposez
`videos/s01-intro.mp4` ou `images/s01-intro.jpg`.

Les **fonds de carte** remplacent le dessin sans déplacer les zones de dépôt
(exprimées en pourcentage) : gardez des proportions proches de celles du dessin.

---

## Liste des noms attendus

*(Générée à partir des données du jeu, `js/donnees/`.)*

### Emplacements communs

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `mission-intro` | Écran d'accueil | Ouverture de la mission |
| `final-intro` | Piste finale : introduction | Aéroport d'Ajaccio |
| `carte-corse` | Piste finale : **fond de carte** (remplace le dessin) | Carte quadrillée de la côte ouest de la Corse |
| `recompense` | Fin de mission (nom modifiable dans ⚙️ → Récompense mystère) | Récompense mystère |

### Séance 1 — Le grand départ

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s01-intro` | Introduction (vidéo conseillée) | Le message du Professeur Atlas |
| `s01-coeur` | Décor du cœur de séance | Le plan de notre commune |
| `s01-fin` | Dénouement | En route ! |
| `lecon-01-commune` | Illustration de la leçon | Ma commune vue du ciel |

### Séance 2 — Direction Dijon !

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s02-intro` | Introduction (vidéo conseillée) | Arrivée à Dijon |
| `s02-coeur` | Décor du cœur de séance | Le palais des ducs de Bourgogne |
| `s02-plan-dijon` | Illustration de l'énigme 1 (qcm) | Plan du centre de Dijon |
| `planisphere` | **Fond de carte** de l'énigme 2 (remplace le dessin) | Planisphère muet |
| `carte-regions` | **Fond de carte** de l'énigme 4 (remplace le dessin) | Les 13 régions métropolitaines |
| `s02-fin` | Dénouement |  |
| `lecon-02-decoupage` | Illustration de la leçon | Les 13 régions de France métropolitaine |

### Séance 3 — Vivre à Clamecy, vivre dans une commune rurale

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s03-intro` | Introduction (vidéo conseillée) | Arrivée à Clamecy |
| `s03-coeur` | Décor du cœur de séance | Un bourg de la Nièvre |
| `s03-photos` | Illustration de l'énigme 1 (qcm) | Quatre paysages français |
| `village-clamecy` | **Fond de carte** de l'énigme 4 (remplace le dessin) | Un village vu du ciel |
| `s03-fin` | Dénouement |  |
| `lecon-03-rural` | Illustration de la leçon | Un village vu du ciel |

### Séance 4 — Besançon, travailler en ville

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s04-intro` | Introduction (vidéo conseillée) | Besançon depuis la citadelle |
| `s04-coeur` | Décor du cœur de séance | Les quartiers de Besançon |
| `besancon-aerien` | **Fond de carte** de l'énigme 4 (remplace le dessin) | Besançon vue du ciel |
| `s04-fin` | Dénouement |  |
| `lecon-04-ville` | Illustration de la leçon | Une ville et ses quartiers |

### Séance 5 — Profitons des loisirs de la montagne

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s05-intro` | Introduction (vidéo conseillée) | Le massif de la Dôle |
| `s05-coeur` | Décor du cœur de séance | Le domaine skiable |
| `s05-photos` | Illustration de l'énigme 3 (trous) | Cinq photographies prises en station |
| `s05-fin` | Dénouement |  |
| `lecon-05-montagne` | Illustration de la leçon | Un domaine skiable |

### Séance 6 — Étretat, station balnéaire

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s06-intro` | Introduction (vidéo conseillée) | Les falaises d'Étretat |
| `s06-coeur` | Décor du cœur de séance | L'Aiguille creuse |
| `s06-photos` | Illustration de l'énigme 4 (tri) | Six photographies prises à Étretat |
| `s06-fin` | Dénouement |  |
| `lecon-06-balneaire` | Illustration de la leçon | Une station balnéaire |

### Séance 7 — Le littoral atlantique

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s07-intro` | Introduction (vidéo conseillée) | Le littoral atlantique |
| `s07-coeur` | Décor du cœur de séance | La grande plage de Biarritz |
| `carte-mers` | **Fond de carte** de l'énigme 1 (remplace le dessin) | La France et ses mers |
| `s07-fin` | Dénouement |  |
| `lecon-07-littoral` | Illustration de la leçon | Les mers et océans bordant la France |

### Séance 8 — Niveaux de vie dans le monde

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s08-intro` | Introduction (vidéo conseillée) | Dhaka, Bangladesh |
| `s08-coeur` | Décor du cœur de séance | Inégalités mondiales |
| `carte-richesses` | Illustration de l'énigme 1 (vraifaux) | Doc. 1 : Les inégalités de richesse dans le monde |
| `s08-gateau` | Illustration de l'énigme 2 (qcm) | La répartition des richesses, caricature de Selçuk (1997) |
| `s08-enfants` | Illustration de l'énigme 6 (ouverte) | Enfants au travail |
| `s08-fin` | Dénouement |  |
| `lecon-08-inegalites` | Illustration de la leçon | Les inégalités de richesse dans le monde |

### Séance 9 — Les pratiques alimentaires

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s09-intro` | Introduction (vidéo conseillée) | Un marché de Bamako |
| `s09-coeur` | Décor du cœur de séance | Étals du marché |
| `s09-frigos` | Illustration de l'énigme 1 (tri) | Un frigo français, un frigo malien |
| `carte-sous-alimentation` | Illustration de l'énigme 4 (tableau) | La sous-alimentation dans le monde (2022-2024) — source FAO 2025 |
| `s09-fin` | Dénouement |  |
| `lecon-09-alimentation` | Illustration de la leçon | Un marché au Mali |

### Séance 10 — Les produits consommés

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s10-intro` | Introduction (vidéo conseillée) | Un plateau de cantine |
| `s10-coeur` | Décor du cœur de séance | La ferme de Bray |
| `s10-plateau` | Illustration de l'énigme 1 (tri) | Le plateau du jour |
| `s10-ferme` | Illustration de l'énigme 3 (tableau) | Les espaces de production de la ferme de Bray |
| `s10-fin` | Dénouement |  |
| `lecon-10-produits` | Illustration de la leçon | Un plateau de cantine |

### Séance 11 — Chaînes de production

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s11-intro` | Introduction (vidéo conseillée) | La ferme de Bray |
| `s11-coeur` | Décor du cœur de séance | Dans l'usine |
| `s11-etapes` | Illustration de l'énigme 1 (ordre) | Les huit étapes, dans le désordre |
| `s11-fin` | Dénouement |  |
| `lecon-11-chaine` | Illustration de la leçon | De la ferme à l'usine |

### Séance 12 — L'heure du ravitaillement

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s12-intro` | Introduction (vidéo conseillée) | Un étal de marché |
| `s12-coeur` | Décor du cœur de séance | D'où viennent nos aliments ? |
| `s12-etals` | Illustration de l'énigme 1 (tri) | Les étiquettes du marché |
| `s12-fin` | Dénouement |  |
| `lecon-12-km` | Illustration de la leçon | D'où viennent nos aliments ? |

### Séance 13 — L'eau en France : fleuves et massifs

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s13-intro` | Introduction (vidéo conseillée) | Un torrent alpin |
| `s13-coeur` | Décor du cœur de séance | Fleuves et massifs de France |
| `carte-fleuves-montagnes` | **Fond de carte** de l'énigme 1 (remplace le dessin) | La France, fleuves et montagnes |
| `s13-fin` | Dénouement |  |
| `lecon-13-fleuves` | Illustration de la leçon | Fleuves et massifs de France |

### Séance 14 — Le trajet de l'eau, de la source à la mer

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s14-intro` | Introduction (vidéo conseillée) | La Seine, de la source à la mer |
| `s14-coeur` | Décor du cœur de séance | De l'amont vers l'aval |
| `s14-photos` | Illustration de l'énigme 1 (ordre) | Cinq paysages de la Seine |
| `s14-schema` | Illustration de l'énigme 2 (motscroises) | Vue d'ensemble d'un cours d'eau |
| `schema-cours-eau` | **Fond de carte** de l'énigme 4 (remplace le dessin) | Vue d'ensemble d'un cours d'eau |
| `s14-fin` | Dénouement |  |
| `lecon-14-cours-eau` | Illustration de la leçon | Vue d'ensemble d'un cours d'eau |

### Séance 15 — Besoin en eau

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s15-intro` | Introduction (vidéo conseillée) | La Garonne à Toulouse |
| `s15-coeur` | Décor du cœur de séance | Les usages de l'eau |
| `s15-trajet` | Illustration de l'énigme 3 (vraifaux) | Le trajet de l'eau consommée en France |
| `paysage-usages` | **Fond de carte** de l'énigme 5 (remplace le dessin) | Où va cette eau ? |
| `s15-fin` | Dénouement |  |
| `lecon-15-usages` | Illustration de la leçon | Le trajet de l'eau consommée |

### Séance 16 — Au secours, il n'y a plus d'eau !

| Nom du fichier | Où il apparaît | Légende affichée |
|---|---|---|
| `s16-intro` | Introduction (vidéo conseillée) | Une rivière à sec dans le Var |
| `s16-coeur` | Décor du cœur de séance | Le lac à son plus bas niveau |
| `s16-paysage` | Illustration de l'énigme 1 (repartition) | La vallée en pénurie d'eau |
| `s16-fin` | Dénouement | La carte marine abandonnée |
| `lecon-16-secheresse` | Illustration de la leçon | Une rivière à sec |

---

## Remplacer, changer de format, supprimer

- **Remplacer** : déposez un fichier du même nom, il écrase l'ancien.
- **Changer de format** : supprimez l'ancien fichier, pour qu'il ne reste qu'un
  fichier par emplacement (une vidéo passe toujours avant une image).
- **Supprimer** : le jeu revient à son dessin, ou masque l'emplacement.
- Noms **en minuscules**, sans espace ni accent.
