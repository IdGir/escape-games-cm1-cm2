# PRODUCTION DES MÉDIAS — Le Journal du Nautilus

> Fichier **généré** par `outils/construire-prompts.py` (source unique de la charte, des fiches personnages et des
> prompts) : modifier le script, puis le relancer. Liste machine : `medias.csv` (même contenu).
> **Aucun média n'a été généré par Claude** : le jeu tourne avec les images de référence de l'enseignant et des décors
> dessinés en code (secours). Ce dossier sert à produire les images et vidéos définitives.

## 1. Comment un média entre dans le jeu (sans toucher au code)

1. Générer (outil au choix, § 4) ou faire générer (`outils/generer-medias.py`, Agnes, facultatif) → les propositions vont dans
   `assets/medias-proposes/` (jamais publiées, exclues par `.gitignore`).
2. Comparer et choisir dans `outils/choisir-medias.html` (proposition / secours côte à côte), télécharger la proposition retenue
   **sous le nom exact** de sa fiche (ex. `carre.webp`), la déposer dans le dossier indiqué (`assets/images/decors/`…).
3. Vérifier : `medias.html` (fichier déposé / référence / secours, aperçu côte à côte) et `python outils/verifier-medias.py`
   (dimensions, poids, ratio, noms). Recaler zones cliquables et effets si besoin : `outils/caler-effets.html`.
4. Un fichier déposé **prime toujours** ; le retirer ramène le secours. Formats acceptés, par priorité : `.webp`, `.jpg`, `.png`
   (images), `.mp4`, `.webm` (vidéos). Textes, voix et sous-titres restent dans le code : ne jamais les incruster.

## 2. Charte graphique (à recopier dans chaque prompt — c'est fait automatiquement ci-dessous)

- **Style (FR)** : {STYLE_FR}.
- **Style (EN)** : {STYLE_EN}.
- **Deux directions, une seule lumière** : photoréaliste cinéma pour les scènes **avec personnages** ; peinture numérique pour
  les décors **sans personnage** ; même palette et même éclairage (ambre chaud + bleu aquatique par les hublots).
- **Palette** : abysse `#050e15` · océan `#0b2230` · turquoise des hublots `#0f7fb5` / `#5fd0ff` · laiton `#c9a24a` /
  `#f0d48e` / `#6b4a12` · acajou `#3a1a0c` / `#5a2d17` · vert-de-gris `#2a4038` · ambre des lampes `#ffcf7a` · cuir vert `#2a5539`.
- **Motifs récurrents (identité visuelle)** : {MOTIFS_FR}.
- **Deux ambiances à bord** : salons de bois et de laiton (salon, bibliothèque, cabine) ; coursives et salles de travail de
  métal patiné vert-de-gris et de cuivre (carré, machines, sas).
- **Cadrage** : 16:9, 1920 × 1080, plan large fixe, perspective lisible, objets narratifs nombreux et identifiables,
  avant-plan sombre et plan moyen éclairé ; **réserve** : {RESERVE_FR}.
- **Interdits** : {INTERDITS_FR} ; pas de charbon ni de flammes ni de cheminée dans le Nautilus (il est **électrique**) ;
  pas d'inscription lisible inventée.
- **Silhouette canonique du Nautilus (extérieurs, mot pour mot)** : {NAUTILUS_FR}.
  *EN :* {NAUTILUS_EN}.
- **Références de l'enseignant** (`references/`) : étalon de qualité et d'ambiance ; ne pas en reproduire les personnages, les
  objets distinctifs ni l'interface. Ne citer **aucun nom d'artiste vivant** dans les prompts.

## 3. Fiches d'identité des personnages (à recopier à l'identique)

{PERSOS}

Ordre conseillé : 1) portraits de référence (Nemo d'après `references/personnage-nemo-1.png` et `-2.png`), validation par
l'enseignant, puis dépôt dans `references/personnage-<nom>-1.png` ; 2) cadre d'interface ; 3) décors (avec les références de
style) ; 4) vidéos à partir des décors **validés** ; 5) retouches.

## 4. Outils et conditions d'usage

- **Images** : tout générateur d'images (Midjourney, Flux, Imagen, Ideogram, Agnes…). **Vidéos** : générateur image→vidéo
  (Runway, Kling, Veo, Luma, Agnes) en partant de l'image du décor validé. **À défaut** : gravures d'époque du roman (Alphonse
  de Neuville, Édouard Riou, domaine public), retraitées.
- **Conditions d'usage à contrôler par l'enseignant** avant publication : droits d'usage scolaire et de publication en ligne
  de chaque service (offre gratuite ou payante), mention éventuelle de l'outil, absence de personne réelle. Noter chaque média
  dans `assets/medias/CREDITS-medias.md` (outil, date, prompt, licence).
- **Agnes** (facultatif, `outils/generer-medias.py`) : vérifier sur `wiki.agnes-ai.com` les modèles et tarifs du jour ; le
  script affiche une estimation et respecte les plafonds `--max-images` / `--max-videos`.
- **Vidéos** : 1280 × 720, H.264, ≤ 6 Mo ; transitions 6-10 s, intro 60-90 s, fin 45 s ; sans texte ni personnage qui parle.
