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

- **Style (FR)** : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ.
- **Style (EN)** : semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field.
- **Deux directions, une seule lumière** : photoréaliste cinéma pour les scènes **avec personnages** ; peinture numérique pour
  les décors **sans personnage** ; même palette et même éclairage (ambre chaud + bleu aquatique par les hublots).
- **Palette** : abysse `#050e15` · océan `#0b2230` · turquoise des hublots `#0f7fb5` / `#5fd0ff` · laiton `#c9a24a` /
  `#f0d48e` / `#6b4a12` · acajou `#3a1a0c` / `#5a2d17` · vert-de-gris `#2a4038` · ambre des lampes `#ffcf7a` · cuir vert `#2a5539`.
- **Motifs récurrents (identité visuelle)** : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre.
- **Deux ambiances à bord** : salons de bois et de laiton (salon, bibliothèque, cabine) ; coursives et salles de travail de
  métal patiné vert-de-gris et de cuivre (carré, machines, sas).
- **Cadrage** : 16:9, 1920 × 1080, plan large fixe, perspective lisible, objets narratifs nombreux et identifiables,
  avant-plan sombre et plan moyen éclairé ; **réserve** : bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue.
- **Interdits** : pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste ; pas de charbon ni de flammes ni de cheminée dans le Nautilus (il est **électrique**) ;
  pas d'inscription lisible inventée.
- **Silhouette canonique du Nautilus (extérieurs, mot pour mot)** : le Nautilus : long fuseau cylindro-conique de tôle rivetée gris acier patiné, une rangée de hublots ronds éclairés d'ambre le long de la coque, une petite cage du pilote vitrée en laiton à facettes sur le dos, un fanal électrique, un canot encastré dans la coque, rambardes de laiton, aucune cheminée, aucune voile, aucun mât de navire à voile.
  *EN :* the Nautilus: a long cylindro-conical spindle hull of weathered riveted steel plates, one row of round amber-lit portholes along the hull, a small faceted brass-and-glass pilot cage on its back, an electric searchlight, a dinghy recessed into the hull, brass railings, no funnel, no sails, no sailing masts.
- **Références de l'enseignant** (`references/`) : étalon de qualité et d'ambiance ; ne pas en reproduire les personnages, les
  objets distinctifs ni l'interface. Ne citer **aucun nom d'artiste vivant** dans les prompts.

## 3. Fiches d'identité des personnages (à recopier à l'identique)

- **nemo** — Le capitaine Nemo : homme d'une cinquantaine d'années, cheveux gris plaqués en arrière, barbe poivre et sel taillée, regard grave, intense et mélancolique ; long manteau (redingote) bleu marine à double rang de boutons dorés, gilet et col blancs sobres, chaîne de montre ; posture droite, mains dans le dos.
  *EN :* Captain Nemo: a man in his fifties, grey hair slicked back, neatly trimmed salt-and-pepper beard, grave, intense and melancholic gaze; long navy-blue double-breasted frock coat with gold buttons, plain white waistcoat and collar, watch chain; upright posture, hands behind his back.
- **aronnax** — Le professeur Aronnax : savant français d'environ 40 ans, cheveux bruns légèrement grisonnants aux tempes, moustache et favoris soignés, regard curieux ; redingote brune, gilet, cravate nouée, carnet de notes et crayon à la main.
  *EN :* Professor Aronnax: a French naturalist about 40, brown hair slightly greying at the temples, neat moustache and side-whiskers, curious eyes; brown frock coat, waistcoat, knotted cravat, notebook and pencil in hand.
- **conseil** — Conseil : domestique flamand d'environ 30 ans, flegmatique, cheveux châtain clair bien peignés, rasé de près, petites lunettes rondes cerclées de métal ; tenue de serviteur soignée : veste sombre ajustée, gilet, col blanc, nœud discret.
  *EN :* Conseil: a phlegmatic Flemish manservant about 30, light-brown neatly combed hair, clean-shaven, small round metal-rimmed glasses; tidy servant's outfit: fitted dark jacket, waistcoat, white collar, discreet bow.
- **ned** — Ned Land : harponneur canadien d'environ 40 ans, grand et large d'épaules, visage hâlé, barbe courte rousse, sourcils épais ; bonnet de laine, chemise de marin à col ouvert, gilet de cuir, harpon à la main.
  *EN :* Ned Land: a Canadian harpooner about 40, tall and broad-shouldered, weathered tanned face, short red beard, thick eyebrows; wool cap, open-collared sailor's shirt, leather vest, harpoon in hand.

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


## 5. Fiches média (une par fichier)

| Identifiant | Fichier exact | Dimensions | Durée | Escale | Statut |
|---|---|---|---|---|---|
| portrait-nemo | `assets/images/personnages/nemo.webp` | 1200×1600 | — | toutes | secours actif (portrait dessiné) |
| portrait-aronnax | `assets/images/personnages/aronnax.webp` | 1200×1600 | — | toutes | secours actif (portrait dessiné) |
| portrait-conseil | `assets/images/personnages/conseil.webp` | 1200×1600 | — | toutes | secours actif (portrait dessiné) |
| portrait-ned | `assets/images/personnages/ned.webp` | 1200×1600 | — | toutes | secours actif (portrait dessiné) |
| cadre-dialogue | `assets/images/ui/cadre-dialogue.png` | 1600×360 (PNG transparent) | — | toutes | secours actif (cadre CSS) |
| decor-salon | `assets/images/decors/salon.webp` | 1920×1080 | — | 2 | référence active |
| decor-carre | `assets/images/decors/carre.webp` | 1920×1080 | — | 2 | référence active |
| decor-machines | `assets/images/decors/machines.webp` | 1920×1080 | — | 2 | secours actif (décor dessiné) |
| decor-cabine | `assets/images/decors/cabine.webp` | 1920×1080 | — | 2 | référence active |
| decor-pont-lincoln | `assets/images/decors/pont-lincoln.webp` | 1920×1080 | — | 1 | déposé (Agnes, à valider par l'enseignant) |
| decor-machines-vapeur | `assets/images/decors/machines-vapeur.webp` | 1920×1080 | — | 1 | déposé (Agnes, à valider par l'enseignant) |
| decor-cambuse | `assets/images/decors/cambuse.webp` | 1920×1080 | — | 1 | déposé (Agnes, à valider par l'enseignant) |
| decor-pont-nautilus | `assets/images/decors/pont-nautilus.webp` | 1920×1080 | — | 1 | à produire avec l'escale 1 |
| decor-sas | `assets/images/decors/sas.webp` | 1920×1080 | — | 3 | déposé (Agnes, à valider par l'enseignant) |
| decor-recif | `assets/images/decors/recif.webp` | 1920×1080 | — | 3 | déposé (Agnes, à valider par l'enseignant) |
| decor-foret-crespo | `assets/images/decors/foret-crespo.webp` | 1920×1080 | — | 3 | déposé (Agnes, à valider par l'enseignant) |
| decor-epave-vanikoro | `assets/images/decors/epave-vanikoro.webp` | 1920×1080 | — | 4 | déposé (Agnes, à valider par l'enseignant) |
| decor-banc-perles | `assets/images/decors/banc-perles.webp` | 1920×1080 | — | 5 | déposé (Agnes, à valider par l'enseignant) |
| decor-pont-ceylan | `assets/images/decors/pont-ceylan.webp` | 1920×1080 | — | 5 | déposé (Agnes, à valider par l'enseignant) |
| decor-tunnel-arabique | `assets/images/decors/tunnel-arabique.webp` | 1920×1080 | — | 6 | déposé (Agnes, à valider par l'enseignant) |
| decor-pont-port-said | `assets/images/decors/pont-port-said.webp` | 1920×1080 | — | 6 | déposé (Agnes, à valider par l'enseignant) |
| decor-volcan-santorin | `assets/images/decors/volcan-santorin.webp` | 1920×1080 | — | 7 | déposé (Agnes, à valider par l'enseignant) |
| decor-atlantide | `assets/images/decors/atlantide.webp` | 1920×1080 | — | 7 | déposé (Agnes, à valider par l'enseignant) |
| decor-sargasses | `assets/images/decors/sargasses.webp` | 1920×1080 | — | 8 | déposé (Agnes, à valider par l'enseignant) |
| decor-cable | `assets/images/decors/cable.webp` | 1920×1080 | — | 8 | déposé (Agnes, à valider par l'enseignant) |
| decor-banquise | `assets/images/decors/banquise.webp` | 1920×1080 | — | 9 | déposé (Agnes, à valider par l'enseignant) |
| decor-pole | `assets/images/decors/pole.webp` | 1920×1080 | — | 9 | déposé (Agnes, à valider par l'enseignant) |
| decor-plateforme-poulpe | `assets/images/decors/plateforme-poulpe.webp` | 1920×1080 | — | 10 | déposé (Agnes, à valider par l'enseignant) |
| decor-baie-vigo | `assets/images/decors/baie-vigo.webp` | 1920×1080 | — | 11 | déposé (Agnes, à valider par l'enseignant) |
| decor-maelstrom | `assets/images/decors/maelstrom.webp` | 1920×1080 | — | 11 | déposé (Agnes, à valider par l'enseignant) |
| decor-salle-orgue | `assets/images/decors/salle-orgue.webp` | 1920×1080 | — | 11 | déposé (Agnes, à valider par l'enseignant) |
| video-intro | `assets/videos/intro.mp4` | 1280×720 | 8 s | 1 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-transition-e2 | `assets/videos/transition-e2.mp4` | 1280×720 | 8-10 s | 2 | cinématique en direct active |
| video-transition-e1 | `assets/videos/transition-e1.mp4` | 1280×720 | 6-10 s | 1 | à produire avec l'escale 1 |
| video-transition-e3 | `assets/videos/transition-e3.mp4` | 1280×720 | 6-10 s | 3 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-transition-e4 | `assets/videos/transition-e4.mp4` | 1280×720 | 6-10 s | 4 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-transition-e5 | `assets/videos/transition-e5.mp4` | 1280×720 | 6-10 s | 5 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-transition-e6 | `assets/videos/transition-e6.mp4` | 1280×720 | 6-10 s | 6 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-transition-e7 | `assets/videos/transition-e7.mp4` | 1280×720 | 6-10 s | 7 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-transition-e8 | `assets/videos/transition-e8.mp4` | 1280×720 | 6-10 s | 8 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-transition-e9 | `assets/videos/transition-e9.mp4` | 1280×720 | 6-10 s | 9 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-transition-e10 | `assets/videos/transition-e10.mp4` | 1280×720 | 6-10 s | 10 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-transition-e11 | `assets/videos/transition-e11.mp4` | 1280×720 | 6-10 s | 11 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-fin | `assets/videos/fin.mp4` | 1280×720 | 8 s | 11 | déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant) |
| video-bande-annonce | `assets/videos/bande-annonce.mp4` | 1280×720 | 15-20 s | toutes | monté (ffmpeg, à partir des vidéos déposées) |

### portrait-nemo — `assets/images/personnages/nemo.webp`

- Dimensions : 1200×1600 · ratio 3:4 · escale toutes · statut : secours actif (portrait dessiné)
- Effets ajoutés par le moteur (ne pas peindre) : respiration, clignement, bouche animée (moteur)
- Référence / image de départ : references/personnage-nemo-1.png, references/personnage-nemo-2.png
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Portrait de référence, plan taille, cadrage vertical, fond flou de boiseries et de hublot bleu. Le capitaine Nemo : homme d'une cinquantaine d'années, cheveux gris plaqués en arrière, barbe poivre et sel taillée, regard grave, intense et mélancolique ; long manteau (redingote) bleu marine à double rang de boutons dorés, gilet et col blancs sobres, chaîne de montre ; posture droite, mains dans le dos. Photoréaliste de cinéma, lumière latérale bleue froide + ambre chaud. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```

**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Captain Nemo: a man in his fifties, grey hair slicked back, neatly trimmed salt-and-pepper beard, grave, intense and melancholic gaze; long navy-blue double-breasted frock coat with gold buttons, plain white waistcoat and collar, watch chain; upright posture, hands behind his back. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. --ar 3:4 --style raw --v <version courante> --no text, letters, watermark, logo --cref <URL du portrait validé> --sref <URL de references/style-salon-nautilus.png>
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio 3:4, image de référence pour la cohérence) — joindre : references/personnage-nemo-1.png, references/personnage-nemo-2.png
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Captain Nemo: a man in his fifties, grey hair slicked back, neatly trimmed salt-and-pepper beard, grave, intense and melancholic gaze; long navy-blue double-breasted frock coat with gold buttons, plain white waistcoat and collar, watch chain; upright posture, hands behind his back. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person.
```
**Imagen / Ideogram** (prompt naturel, ratio 3:4, rappeler « sans texte ») :
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Captain Nemo: a man in his fifties, grey hair slicked back, neatly trimmed salt-and-pepper beard, grave, intense and melancholic gaze; long navy-blue double-breasted frock coat with gold buttons, plain white waistcoat and collar, watch chain; upright posture, hands behind his back. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "3:4"`, `extra_body.image` = references/personnage-nemo-1.png, references/personnage-nemo-2.png ; recadrer ensuite en 1200×1600) :
```
Portrait de référence, plan taille, cadrage vertical, fond flou de boiseries et de hublot bleu. Le capitaine Nemo : homme d'une cinquantaine d'années, cheveux gris plaqués en arrière, barbe poivre et sel taillée, regard grave, intense et mélancolique ; long manteau (redingote) bleu marine à double rang de boutons dorés, gilet et col blancs sobres, chaîne de montre ; posture droite, mains dans le dos. Photoréaliste de cinéma, lumière latérale bleue froide + ambre chaud. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```
Prompt négatif : `texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé` · *Negative:* `text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style`


### portrait-aronnax — `assets/images/personnages/aronnax.webp`

- Dimensions : 1200×1600 · ratio 3:4 · escale toutes · statut : secours actif (portrait dessiné)
- Effets ajoutés par le moteur (ne pas peindre) : respiration, clignement, bouche animée (moteur)
- Référence / image de départ : references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Portrait de référence, plan taille, cadrage vertical, fond flou de boiseries et de hublot bleu. Le professeur Aronnax : savant français d'environ 40 ans, cheveux bruns légèrement grisonnants aux tempes, moustache et favoris soignés, regard curieux ; redingote brune, gilet, cravate nouée, carnet de notes et crayon à la main. Photoréaliste de cinéma, lumière latérale bleue froide + ambre chaud. Les images jointes ne servent que pour le décor et la lumière : aucune personne des images ne doit apparaître. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```

**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Professor Aronnax: a French naturalist about 40, brown hair slightly greying at the temples, neat moustache and side-whiskers, curious eyes; brown frock coat, waistcoat, knotted cravat, notebook and pencil in hand. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. --ar 3:4 --style raw --v <version courante> --no text, letters, watermark, logo --cref <URL du portrait validé> --sref <URL de references/style-salon-nautilus.png>
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio 3:4, image de référence pour la cohérence) — joindre : references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Professor Aronnax: a French naturalist about 40, brown hair slightly greying at the temples, neat moustache and side-whiskers, curious eyes; brown frock coat, waistcoat, knotted cravat, notebook and pencil in hand. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person.
```
**Imagen / Ideogram** (prompt naturel, ratio 3:4, rappeler « sans texte ») :
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Professor Aronnax: a French naturalist about 40, brown hair slightly greying at the temples, neat moustache and side-whiskers, curious eyes; brown frock coat, waistcoat, knotted cravat, notebook and pencil in hand. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "3:4"`, `extra_body.image` = references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png ; recadrer ensuite en 1200×1600) :
```
Portrait de référence, plan taille, cadrage vertical, fond flou de boiseries et de hublot bleu. Le professeur Aronnax : savant français d'environ 40 ans, cheveux bruns légèrement grisonnants aux tempes, moustache et favoris soignés, regard curieux ; redingote brune, gilet, cravate nouée, carnet de notes et crayon à la main. Photoréaliste de cinéma, lumière latérale bleue froide + ambre chaud. Les images jointes ne servent que pour le décor et la lumière : aucune personne des images ne doit apparaître. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```
Prompt négatif : `texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé` · *Negative:* `text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style`


### portrait-conseil — `assets/images/personnages/conseil.webp`

- Dimensions : 1200×1600 · ratio 3:4 · escale toutes · statut : secours actif (portrait dessiné)
- Effets ajoutés par le moteur (ne pas peindre) : respiration, clignement, bouche animée (moteur)
- Référence / image de départ : references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Portrait de référence, plan taille, cadrage vertical, fond flou de boiseries et de hublot bleu. Conseil : domestique flamand d'environ 30 ans, flegmatique, cheveux châtain clair bien peignés, rasé de près, petites lunettes rondes cerclées de métal ; tenue de serviteur soignée : veste sombre ajustée, gilet, col blanc, nœud discret. Photoréaliste de cinéma, lumière latérale bleue froide + ambre chaud. Les images jointes ne servent que pour le décor et la lumière : aucune personne des images ne doit apparaître. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```

**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Conseil: a phlegmatic Flemish manservant about 30, light-brown neatly combed hair, clean-shaven, small round metal-rimmed glasses; tidy servant's outfit: fitted dark jacket, waistcoat, white collar, discreet bow. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. --ar 3:4 --style raw --v <version courante> --no text, letters, watermark, logo --cref <URL du portrait validé> --sref <URL de references/style-salon-nautilus.png>
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio 3:4, image de référence pour la cohérence) — joindre : references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Conseil: a phlegmatic Flemish manservant about 30, light-brown neatly combed hair, clean-shaven, small round metal-rimmed glasses; tidy servant's outfit: fitted dark jacket, waistcoat, white collar, discreet bow. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person.
```
**Imagen / Ideogram** (prompt naturel, ratio 3:4, rappeler « sans texte ») :
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Conseil: a phlegmatic Flemish manservant about 30, light-brown neatly combed hair, clean-shaven, small round metal-rimmed glasses; tidy servant's outfit: fitted dark jacket, waistcoat, white collar, discreet bow. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "3:4"`, `extra_body.image` = references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png ; recadrer ensuite en 1200×1600) :
```
Portrait de référence, plan taille, cadrage vertical, fond flou de boiseries et de hublot bleu. Conseil : domestique flamand d'environ 30 ans, flegmatique, cheveux châtain clair bien peignés, rasé de près, petites lunettes rondes cerclées de métal ; tenue de serviteur soignée : veste sombre ajustée, gilet, col blanc, nœud discret. Photoréaliste de cinéma, lumière latérale bleue froide + ambre chaud. Les images jointes ne servent que pour le décor et la lumière : aucune personne des images ne doit apparaître. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```
Prompt négatif : `texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé` · *Negative:* `text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style`


### portrait-ned — `assets/images/personnages/ned.webp`

- Dimensions : 1200×1600 · ratio 3:4 · escale toutes · statut : secours actif (portrait dessiné)
- Effets ajoutés par le moteur (ne pas peindre) : respiration, clignement, bouche animée (moteur)
- Référence / image de départ : references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Portrait de référence, plan taille, cadrage vertical, fond flou de boiseries et de hublot bleu. Ned Land : harponneur canadien d'environ 40 ans, grand et large d'épaules, visage hâlé, barbe courte rousse, sourcils épais ; bonnet de laine, chemise de marin à col ouvert, gilet de cuir, harpon à la main. Photoréaliste de cinéma, lumière latérale bleue froide + ambre chaud. Les images jointes ne servent que pour le décor et la lumière : aucune personne des images ne doit apparaître. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```

**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Ned Land: a Canadian harpooner about 40, tall and broad-shouldered, weathered tanned face, short red beard, thick eyebrows; wool cap, open-collared sailor's shirt, leather vest, harpoon in hand. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. --ar 3:4 --style raw --v <version courante> --no text, letters, watermark, logo --cref <URL du portrait validé> --sref <URL de references/style-salon-nautilus.png>
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio 3:4, image de référence pour la cohérence) — joindre : references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Ned Land: a Canadian harpooner about 40, tall and broad-shouldered, weathered tanned face, short red beard, thick eyebrows; wool cap, open-collared sailor's shirt, leather vest, harpoon in hand. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person.
```
**Imagen / Ideogram** (prompt naturel, ratio 3:4, rappeler « sans texte ») :
```
Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. Ned Land: a Canadian harpooner about 40, tall and broad-shouldered, weathered tanned face, short red beard, thick eyebrows; wool cap, open-collared sailor's shirt, leather vest, harpoon in hand. Cinematic photorealism, cold blue side light plus warm amber light. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "3:4"`, `extra_body.image` = references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png ; recadrer ensuite en 1200×1600) :
```
Portrait de référence, plan taille, cadrage vertical, fond flou de boiseries et de hublot bleu. Ned Land : harponneur canadien d'environ 40 ans, grand et large d'épaules, visage hâlé, barbe courte rousse, sourcils épais ; bonnet de laine, chemise de marin à col ouvert, gilet de cuir, harpon à la main. Photoréaliste de cinéma, lumière latérale bleue froide + ambre chaud. Les images jointes ne servent que pour le décor et la lumière : aucune personne des images ne doit apparaître. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```
Prompt négatif : `texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé` · *Negative:* `text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style`


### cadre-dialogue — `assets/images/ui/cadre-dialogue.png`

- Dimensions : 1600×360 (PNG transparent) · ratio 40:9 · escale toutes · statut : secours actif (cadre CSS)
- Référence / image de départ : références de salon et de cabine (matériaux)
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Plaque de dialogue horizontale vide en laiton patiné et acajou, bordure rivetée, coins ornés de petites coquilles, centre lisse et sombre pour le texte, fond transparent. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```

**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
Empty horizontal dialogue plaque in weathered brass and mahogany, riveted border, small shell ornaments at the corners, smooth dark centre for text, transparent background. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. --ar 4:1 --style raw --v <version courante> --no text, letters, watermark, logo --sref <URL de references/style-salon-nautilus.png>
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio 4:1, image de référence pour la cohérence) — joindre : références de salon et de cabine (matériaux)
```
Empty horizontal dialogue plaque in weathered brass and mahogany, riveted border, small shell ornaments at the corners, smooth dark centre for text, transparent background. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person.
```
**Imagen / Ideogram** (prompt naturel, ratio 4:1, rappeler « sans texte ») :
```
Empty horizontal dialogue plaque in weathered brass and mahogany, riveted border, small shell ornaments at the corners, smooth dark centre for text, transparent background. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "4:1"`, `extra_body.image` = références de salon et de cabine (matériaux) ; recadrer ensuite en 1600×360) :
```
Plaque de dialogue horizontale vide en laiton patiné et acajou, bordure rivetée, coins ornés de petites coquilles, centre lisse et sombre pour le texte, fond transparent. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```
Prompt négatif : `texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé` · *Negative:* `text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style`


### decor-salon — `assets/images/decors/salon.webp`

- Dimensions : 1920×1080 · ratio 16:9 · escale 2 · statut : référence active
- Zones interactives prévues : épure (divan centre), hublots, orgue, vitrines (à recaler avec `outils/caler-effets.html`)
- Effets ajoutés par le moteur (ne pas peindre) : caustiques au sol, poissons derrière les hublots, scintillement du lustre, poussière, vignette
- Référence / image de départ : references/style-salon-nautilus.png
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Le grand salon-musée du Nautilus en enfilade, perspective centrale symétrique : boiseries sombres cirées, parquet en point de Hongrie, tapis à médaillon, lustre à pendeloques, double étage de bibliothèques à galerie, grand orgue au fond entre deux hublots ronds géants sur l'océan bleu turquoise, vitrines de coraux et de coquillages au premier plan, un divan de cuir vert au centre-fond avec un plan roulé posé dessus. Garder exactement la composition, la perspective et l'emplacement des objets de l'image de référence fournie. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```

**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
The Nautilus grand salon-museum seen in a long symmetrical central perspective: dark waxed wood paneling, herringbone parquet, medallion rug, crystal chandelier, two-storey galleried bookcases, a great pipe organ at the far end between two giant round portholes onto turquoise ocean, glass cabinets of corals and shells in the foreground, a green leather divan at the back centre with a rolled plan lying on it. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. --ar 16:9 --style raw --v <version courante> --no text, letters, watermark, logo --sref <URL de references/style-salon-nautilus.png>
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio 16:9, image de référence pour la cohérence) — joindre : references/style-salon-nautilus.png
```
The Nautilus grand salon-museum seen in a long symmetrical central perspective: dark waxed wood paneling, herringbone parquet, medallion rug, crystal chandelier, two-storey galleried bookcases, a great pipe organ at the far end between two giant round portholes onto turquoise ocean, glass cabinets of corals and shells in the foreground, a green leather divan at the back centre with a rolled plan lying on it. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person.
```
**Imagen / Ideogram** (prompt naturel, ratio 16:9, rappeler « sans texte ») :
```
The Nautilus grand salon-museum seen in a long symmetrical central perspective: dark waxed wood paneling, herringbone parquet, medallion rug, crystal chandelier, two-storey galleried bookcases, a great pipe organ at the far end between two giant round portholes onto turquoise ocean, glass cabinets of corals and shells in the foreground, a green leather divan at the back centre with a rolled plan lying on it. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "16:9"`, `extra_body.image` = references/style-salon-nautilus.png ; recadrer ensuite en 1920×1080) :
```
Le grand salon-musée du Nautilus en enfilade, perspective centrale symétrique : boiseries sombres cirées, parquet en point de Hongrie, tapis à médaillon, lustre à pendeloques, double étage de bibliothèques à galerie, grand orgue au fond entre deux hublots ronds géants sur l'océan bleu turquoise, vitrines de coraux et de coquillages au premier plan, un divan de cuir vert au centre-fond avec un plan roulé posé dessus. Garder exactement la composition, la perspective et l'emplacement des objets de l'image de référence fournie. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```
Prompt négatif : `texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé` · *Negative:* `text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style`


### decor-carre — `assets/images/decors/carre.webp`

- Dimensions : 1920×1080 · ratio 16:9 · escale 2 · statut : référence active
- Zones interactives prévues : table (objets), journal de bord, tableau des cadrans (à recaler avec `outils/caler-effets.html`)
- Effets ajoutés par le moteur (ne pas peindre) : fumée (panne), étincelles au tableau, bulles au hublot, lueur de la lampe verte
- Référence / image de départ : references/style-salle-officiers-3.png
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Le carré des officiers du Nautilus : intérieur métallique riveté vert-de-gris patiné avec lambris et tuyauteries de cuivre, tableau de manomètres et cadrans en haut à gauche, grande table de bois au premier plan couverte de cartes roussies, compas, règles, un verre de cristal, un bouchon, une plume, un journal de bord noirci à droite, lampe à abat-jour vert, petit hublot rond sur l'eau, horloge murale. Garder exactement la composition, la perspective et l'emplacement des objets de l'image de référence fournie. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```

**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
The Nautilus officers' wardroom: riveted verdigris metal interior with wood wainscoting and copper pipes, a panel of pressure gauges top left, a large wooden table in the foreground covered with scorched charts, compasses, rulers, a crystal glass, a cork, a quill, a blackened logbook on the right, green-shaded lamp, small round porthole onto water, wall clock. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. --ar 16:9 --style raw --v <version courante> --no text, letters, watermark, logo --sref <URL de references/style-salon-nautilus.png>
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio 16:9, image de référence pour la cohérence) — joindre : references/style-salle-officiers-3.png
```
The Nautilus officers' wardroom: riveted verdigris metal interior with wood wainscoting and copper pipes, a panel of pressure gauges top left, a large wooden table in the foreground covered with scorched charts, compasses, rulers, a crystal glass, a cork, a quill, a blackened logbook on the right, green-shaded lamp, small round porthole onto water, wall clock. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person.
```
**Imagen / Ideogram** (prompt naturel, ratio 16:9, rappeler « sans texte ») :
```
The Nautilus officers' wardroom: riveted verdigris metal interior with wood wainscoting and copper pipes, a panel of pressure gauges top left, a large wooden table in the foreground covered with scorched charts, compasses, rulers, a crystal glass, a cork, a quill, a blackened logbook on the right, green-shaded lamp, small round porthole onto water, wall clock. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "16:9"`, `extra_body.image` = references/style-salle-officiers-3.png ; recadrer ensuite en 1920×1080) :
```
Le carré des officiers du Nautilus : intérieur métallique riveté vert-de-gris patiné avec lambris et tuyauteries de cuivre, tableau de manomètres et cadrans en haut à gauche, grande table de bois au premier plan couverte de cartes roussies, compas, règles, un verre de cristal, un bouchon, une plume, un journal de bord noirci à droite, lampe à abat-jour vert, petit hublot rond sur l'eau, horloge murale. Garder exactement la composition, la perspective et l'emplacement des objets de l'image de référence fournie. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```
Prompt négatif : `texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé` · *Negative:* `text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style`


### decor-machines — `assets/images/decors/machines.webp`

- Dimensions : 1920×1080 · ratio 16:9 · escale 2 · statut : secours actif (décor dessiné)
- Zones interactives prévues : tableau de bornes (centre), accumulateurs (gauche), cadrans (droite) (à recaler avec `outils/caler-effets.html`)
- Effets ajoutés par le moteur (ne pas peindre) : lueurs bleutées des bobines, étincelles (panne), rayons de lumière, poussière
- Référence / image de départ : references/composition-machines-electriques.png (rendu du décor dessiné, pour garder la place des objets cliquables)
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
La salle des machines ÉLECTRIQUE du Nautilus : rangées d'accumulateurs de verre et de laiton à gauche, grand tableau de laiton au centre avec bornes, câbles gainés débranchés et petites ampoules, cadrans de contrôle à droite, grosses bobines de cuivre, câbles gainés au plafond voûté riveté, passerelle en caillebotis, lumière électrique bleutée, aucun charbon, aucune flamme, aucune chaudière. Garder exactement la composition, la perspective et l'emplacement des objets de l'image de référence fournie. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```

**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
The Nautilus ELECTRIC engine room: rows of glass-and-brass accumulator cells on the left, a large brass switchboard in the centre with terminals, unplugged sheathed cables and small bulbs, control dials on the right, big copper coils, sheathed cables under a riveted vaulted ceiling, metal grating catwalk, bluish electric light, no coal, no flames, no boilers. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. --ar 16:9 --style raw --v <version courante> --no text, letters, watermark, logo --sref <URL de references/style-salon-nautilus.png>
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio 16:9, image de référence pour la cohérence) — joindre : references/composition-machines-electriques.png (rendu du décor dessiné, pour garder la place des objets cliquables)
```
The Nautilus ELECTRIC engine room: rows of glass-and-brass accumulator cells on the left, a large brass switchboard in the centre with terminals, unplugged sheathed cables and small bulbs, control dials on the right, big copper coils, sheathed cables under a riveted vaulted ceiling, metal grating catwalk, bluish electric light, no coal, no flames, no boilers. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person.
```
**Imagen / Ideogram** (prompt naturel, ratio 16:9, rappeler « sans texte ») :
```
The Nautilus ELECTRIC engine room: rows of glass-and-brass accumulator cells on the left, a large brass switchboard in the centre with terminals, unplugged sheathed cables and small bulbs, control dials on the right, big copper coils, sheathed cables under a riveted vaulted ceiling, metal grating catwalk, bluish electric light, no coal, no flames, no boilers. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "16:9"`, `extra_body.image` = references/composition-machines-electriques.png (rendu du décor dessiné, pour garder la place des objets cliquables) ; recadrer ensuite en 1920×1080) :
```
La salle des machines ÉLECTRIQUE du Nautilus : rangées d'accumulateurs de verre et de laiton à gauche, grand tableau de laiton au centre avec bornes, câbles gainés débranchés et petites ampoules, cadrans de contrôle à droite, grosses bobines de cuivre, câbles gainés au plafond voûté riveté, passerelle en caillebotis, lumière électrique bleutée, aucun charbon, aucune flamme, aucune chaudière. Garder exactement la composition, la perspective et l'emplacement des objets de l'image de référence fournie. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```
Prompt négatif : `texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé` · *Negative:* `text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style`


### decor-cabine — `assets/images/decors/cabine.webp`

- Dimensions : 1920×1080 · ratio 16:9 · escale 2 · statut : référence active
- Zones interactives prévues : mur des instruments (droite), bureau, hublot (à recaler avec `outils/caler-effets.html`)
- Effets ajoutés par le moteur (ne pas peindre) : méduses et poissons au hublot, caustiques, lueur de la lampe, poussière
- Référence / image de départ : references/style-cabine-capitaine-2.png
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
La chambre du capitaine Nemo : pièce intime en acajou sombre, grand hublot rond de laiton riveté au centre sur l'eau bleue avec méduses, bureau d'acajou couvert de plans, loupe et compas, lampe de banquier verte, mur d'instruments à droite (baromètre, horloges, manomètre, boussole, carte du ciel), lit-alcôve à rideaux de velours vert à gauche, fauteuil Chesterfield vert, clavier d'orgue à droite, tapis persan. Garder exactement la composition, la perspective et l'emplacement des objets de l'image de référence fournie. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```

**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
Captain Nemo's private cabin: intimate dark mahogany room, a large round riveted brass porthole in the centre onto blue water with jellyfish, mahogany desk covered with plans, magnifier and compasses, green banker's lamp, a wall of instruments on the right (barometer, clocks, pressure gauge, compass, star chart), curtained alcove bed in green velvet on the left, green Chesterfield armchair, organ keyboard on the right, Persian rug. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. --ar 16:9 --style raw --v <version courante> --no text, letters, watermark, logo --sref <URL de references/style-salon-nautilus.png>
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio 16:9, image de référence pour la cohérence) — joindre : references/style-cabine-capitaine-2.png
```
Captain Nemo's private cabin: intimate dark mahogany room, a large round riveted brass porthole in the centre onto blue water with jellyfish, mahogany desk covered with plans, magnifier and compasses, green banker's lamp, a wall of instruments on the right (barometer, clocks, pressure gauge, compass, star chart), curtained alcove bed in green velvet on the left, green Chesterfield armchair, organ keyboard on the right, Persian rug. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person.
```
**Imagen / Ideogram** (prompt naturel, ratio 16:9, rappeler « sans texte ») :
```
Captain Nemo's private cabin: intimate dark mahogany room, a large round riveted brass porthole in the centre onto blue water with jellyfish, mahogany desk covered with plans, magnifier and compasses, green banker's lamp, a wall of instruments on the right (barometer, clocks, pressure gauge, compass, star chart), curtained alcove bed in green velvet on the left, green Chesterfield armchair, organ keyboard on the right, Persian rug. Keep exactly the composition, perspective and object placement of the provided reference image. Style: semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, rich narrative details, cinematic rendering, subtle film grain, shallow depth of field. Recurring motifs: glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, green tufted leather armchairs, oriental rugs, brass and copper fittings. keep the bottom 20% of the frame darker and uncluttered for the dialogue panel. no text, no letters, no logo, no watermark, no real person. Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "16:9"`, `extra_body.image` = references/style-cabine-capitaine-2.png ; recadrer ensuite en 1920×1080) :
```
La chambre du capitaine Nemo : pièce intime en acajou sombre, grand hublot rond de laiton riveté au centre sur l'eau bleue avec méduses, bureau d'acajou couvert de plans, loupe et compas, lampe de banquier verte, mur d'instruments à droite (baromètre, horloges, manomètre, boussole, carte du ciel), lit-alcôve à rideaux de velours vert à gauche, fauteuil Chesterfield vert, clavier d'orgue à droite, tapis persan. Garder exactement la composition, la perspective et l'emplacement des objets de l'image de référence fournie. Style : peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, détails narratifs, rendu cinéma, grain léger, profondeur de champ. Motifs récurrents : appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre. bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue. pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste.
```
Prompt négatif : `texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé` · *Negative:* `text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style`


### video-intro — `assets/videos/intro.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 8 s · escale 1 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres et voix dans le code
- Référence / image de départ : assets/medias-depart/intro.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Image de départ : le pont de la frégate la nuit. Lent travelling avant sur la mer sombre ; au loin, une longue lueur verdâtre file sous l'eau, puis s'éteint ; les vagues, les cordages et la lanterne bougent doucement. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/intro.jpg ; durée 8 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
Start frame: the frigate's deck at night. Slow push-in over the dark sea; far away a long greenish glow glides under the water, then fades; waves, ropes and the lantern move gently. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
Image de départ : le pont de la frégate la nuit. Lent travelling avant sur la mer sombre ; au loin, une longue lueur verdâtre file sous l'eau, puis s'éteint ; les vagues, les cordages et la lanterne bougent doucement. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e2 — `assets/videos/transition-e2.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 8-10 s · escale 2 · statut : cinématique en direct active
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres et voix dans le code (dialogues.json)
- Référence / image de départ : assets/images/decors/salon.webp (validé) en première image
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Image de départ : le grand salon validé. Lent travelling avant vers l'orgue ; les lampes du salon vacillent deux fois puis s'éteignent ; il ne reste que la lumière bleue des hublots ; une lueur rouge d'alarme pulse doucement. Aucun personnage ne parle, aucun texte.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/images/decors/salon.webp (validé) en première image ; durée 8-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
Start frame: the approved grand salon. Slow push-in toward the organ; the salon lamps flicker twice then go out; only the blue light of the portholes remains; a soft red alarm glow pulses. No character speaking, no text.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
Image de départ : le grand salon validé. Lent travelling avant vers l'orgue ; les lampes du salon vacillent deux fois puis s'éteignent ; il ne reste que la lumière bleue des hublots ; une lueur rouge d'alarme pulse doucement. Aucun personnage ne parle, aucun texte.
```


### video-transition-e1 — `assets/videos/transition-e1.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 1 · statut : à produire avec l'escale 1
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : décor validé de l'escale
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
À rédiger avec l'escale 1. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : décor validé de l'escale ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
 No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
À rédiger avec l'escale 1. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e3 — `assets/videos/transition-e3.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 3 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : assets/medias-depart/transition-e3.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Le sas des scaphandres : lent travelling avant vers la porte ronde ; des bulles montent derrière les hublots, les lampes ambrées vacillent doucement. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/transition-e3.jpg ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
The diving-suit airlock: slow push-in toward the round door; bubbles rise behind the portholes, the amber lamps flicker softly. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
Le sas des scaphandres : lent travelling avant vers la porte ronde ; des bulles montent derrière les hublots, les lampes ambrées vacillent doucement. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e4 — `assets/videos/transition-e4.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 4 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : assets/medias-depart/transition-e4.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
L'épave de Vanikoro : lent travelling avant sur le canon et le sextant ; des particules flottent dans le faisceau du fanal, un banc de poissons passe. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/transition-e4.jpg ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
The Vanikoro wreck: slow push-in on the cannon and the sextant; particles drift in the lamp beam, a school of fish passes. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
L'épave de Vanikoro : lent travelling avant sur le canon et le sextant ; des particules flottent dans le faisceau du fanal, un banc de poissons passe. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e5 — `assets/videos/transition-e5.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 5 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : assets/medias-depart/transition-e5.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Le banc de perles : lent travelling avant vers l'huître géante ; le faisceau des lampes glisse sur les coquilles, la perle luit. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/transition-e5.jpg ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
The pearl bed: slow push-in toward the giant oyster; lamp beams glide over the shells, the pearl glows. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
Le banc de perles : lent travelling avant vers l'huître géante ; le faisceau des lampes glisse sur les coquilles, la perle luit. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e6 — `assets/videos/transition-e6.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 6 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : assets/medias-depart/transition-e6.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
La cage du pilote dans le tunnel : léger travelling avant ; la roche défile derrière les vitres éclairées par le fanal, vibration discrète de la coque. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/transition-e6.jpg ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
The pilot's cage in the tunnel: gentle push-in; rock slides past the lit windows, a faint hull vibration. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
La cage du pilote dans le tunnel : léger travelling avant ; la roche défile derrière les vitres éclairées par le fanal, vibration discrète de la coque. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e7 — `assets/videos/transition-e7.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 7 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : assets/medias-depart/transition-e7.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Le salon près de Santorin : lent travelling avant vers les hublots ; l'eau bouillonne, lueurs rouges et orangées du volcan, bulles denses. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/transition-e7.jpg ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
The salon near Santorin: slow push-in toward the portholes; the water boils, red and orange volcano glow, dense bubbles. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
Le salon près de Santorin : lent travelling avant vers les hublots ; l'eau bouillonne, lueurs rouges et orangées du volcan, bulles denses. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e8 — `assets/videos/transition-e8.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 8 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : assets/medias-depart/transition-e8.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
La mer des Sargasses : lent travelling avant sur la bouée ; les algues dorées ondulent au rythme des vagues, un petit crabe passe. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/transition-e8.jpg ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
The Sargasso Sea: slow push-in on the buoy; golden seaweed sways with the waves, a small crab scuttles by. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
La mer des Sargasses : lent travelling avant sur la bouée ; les algues dorées ondulent au rythme des vagues, un petit crabe passe. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e9 — `assets/videos/transition-e9.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 9 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : assets/medias-depart/transition-e9.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
La banquise : lent travelling avant ; l'aurore australe ondule dans le ciel, des cristaux de glace tourbillonnent dans le vent. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/transition-e9.jpg ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
The ice field: slow push-in; the southern aurora ripples in the sky, ice crystals swirl in the wind. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
La banquise : lent travelling avant ; l'aurore australe ondule dans le ciel, des cristaux de glace tourbillonnent dans le vent. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e10 — `assets/videos/transition-e10.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 10 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : assets/medias-depart/transition-e10.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Le salon, derrière la vitre : lent travelling avant ; une ombre immense passe devant la vitre, les lampes vacillent. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/transition-e10.jpg ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
The salon, behind the window: slow push-in; an immense shadow passes in front of the glass, the lamps flicker. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
Le salon, derrière la vitre : lent travelling avant ; une ombre immense passe devant la vitre, les lampes vacillent. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-transition-e11 — `assets/videos/transition-e11.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 6-10 s · escale 11 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres dans le code
- Référence / image de départ : assets/medias-depart/transition-e11.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
La baie de Vigo : lent travelling avant vers le trésor ; des rayons ondulent, l'or étincelle, les plongeurs avancent d'un pas. Aucun personnage ne parle, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/transition-e11.jpg ; durée 6-10 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
Vigo bay: slow push-in toward the treasure; light rays ripple, the gold glints, the divers take a step forward. No character speaking, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
La baie de Vigo : lent travelling avant vers le trésor ; des rayons ondulent, l'or étincelle, les plongeurs avancent d'un pas. Aucun personnage ne parle, aucun texte, aucune lettre.
```


### video-fin — `assets/videos/fin.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 8 s · escale 11 · statut : déposé (Agnes flash, 8 s, sans piste audio ; à valider par l'enseignant)
- Effets ajoutés par le moteur (ne pas peindre) : sous-titres et voix dans le code
- Référence / image de départ : assets/medias-depart/fin.jpg
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Image de départ : le grand salon. Lent travelling avant vers l'orgue ; la lumière des hublots passe du bleu profond à un bleu clair et doré, comme si le Nautilus remontait vers le soleil ; les lampes se rallument doucement. Aucun personnage, aucun texte, aucune lettre.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : assets/medias-depart/fin.jpg ; durée 8 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
Start frame: the grand salon. Slow push-in toward the organ; the porthole light shifts from deep blue to bright golden blue, as if the Nautilus were rising toward the sun; the lamps glow back on. No characters, no text, no letters.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
Image de départ : le grand salon. Lent travelling avant vers l'orgue ; la lumière des hublots passe du bleu profond à un bleu clair et doré, comme si le Nautilus remontait vers le soleil ; les lampes se rallument doucement. Aucun personnage, aucun texte, aucune lettre.
```


### video-bande-annonce — `assets/videos/bande-annonce.mp4`

- Dimensions : 1280×720 · ratio 16:9 · durée 15-20 s · escale toutes · statut : monté (ffmpeg, à partir des vidéos déposées)
- Référence / image de départ : décors validés
- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.

**Prompt (français)** :
```
Montage local (ffmpeg) des vidéos d'ouverture des escales, avec fondus enchaînés : outils/monter-bande-annonce.sh.
```

**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : décors validés ; durée 15-20 s ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
Local ffmpeg montage of the escale opening videos, with cross-fades.
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
Montage local (ffmpeg) des vidéos d'ouverture des escales, avec fondus enchaînés : outils/monter-bande-annonce.sh.
```
