# Journal des versions — Le Tour du Monde en 80 minutes

Les évolutions du jeu, de la plus récente à la plus ancienne. Ce journal est durable et publié
(contrairement aux fichiers RECAP-… de reprise de session). Les entrées viennent de l'historique
git (`python outils-docs/maj-journaux.py`) ; on peut les compléter à la main.

## 1 octobre 2026

- D4 : éditeur graphique (no-code) des énigmes (editeur.html)
- C1 : vue d'ensemble publique de l'année (annee.html)
- B3 : frise visuelle des 26 jeux sur l'accueil
- A4 : application installable, jouable hors connexion (PWA)
- D5 : résultats de l'année exportables vers un tableur ou Schooly
- D2 : mode individuel (devoirs à la maison) avec compte-rendu à l'enseignant
- D1 : écran de classement en direct, à projeter (classement.html)
- D3 : banque d'énigmes à variantes (greffon commun/js/variantes.js)
- C4 : liens « jeu précédent / suivant » à l'écran de fin
- E6 : minuteur adaptatif par équipe depuis prof.html
- E3 : indices proposés selon le rythme de l'équipe (greffon indices-adaptatifs.js)
- E2 : troisième palier « Découverte » (greffon commun/js/palier-decouverte.js)
- E4 : lecture facilitée — police dyslexie, interlignage, espacement
- B6 : transitions animées entre salles (greffon commun/js/transitions.js)
- A3 : tronc commun du moteur (commun/) — un seul exemplaire pour tous les jeux
- A1 : tests automatiques (Node + jsdom) pour les 6 jeux qui n'en avaient pas
- Fins de ligne : .gitattributes (LF, CRLF pour .bat/.ps1) et normalisation
- Moteur v2 : premier coup récompensé, mots à noter, coffre final (9 jeux)

## 30 septembre 2026

- Leçons imprimables A4 illustrées pour les 9 escape games

## 29 septembre 2026

- Ajoute les médias des escape games (photos Commons, images et vidéos Agnes) - lot 2
- Ajoute les médias des escape games (photos Commons, images et vidéos Agnes) - lot 1
- Ajoute le tableau de compétences du programme dans les 9 escape games

## 16 septembre 2026

- Liens GitHub pointés vers la branche escape-games
- Passe fix (repos+parle) en fond noir : les 8 personnages ont maintenant un fond noir cohérent avec éclairage dramatique
- Passe aouda (repos+parle) en fond noir
- Passe fogg (repos+parle) et passepartout (repos) en fond noir, pour rester cohérent avec les portraits

## 15 septembre 2026

- Ajoute les médias manquants produits avec Agnes (Mission géo, variantes -parle, affiche de fin)
- Passe les portraits de personnages en fond noir avec éclairage dramatique (spot), au lieu du fond clair uni
- Remplace les images de décor du Tour du monde par une image extraite de leur vidéo correspondante, pour garantir la cohérence visuelle

## 13 septembre 2026

- Change le style des vidéos de personnages : dessin animé vers photoréaliste, pour rester cohérent avec les nouveaux portraits
- Change le style des portraits de personnages : dessin animé/aquarelle vers photoréaliste (Déclaration + Tour du monde)
- Ajoute les vidéos des personnages (Déclaration + Tour du monde) et le décor filmé d'intro, générées avec Agnes (image-to-video)
- Ajoute les personnages et décors manquants (portraits, étapes du tour du monde, paysages), corrige les noms de fichiers en majuscule et l'incohérence carte-fuseaux-horaires, générés avec Agnes
- Synchronise localement les médias déjà déposés sur GitHub (décors salle 1/2/3/5, bastille recompressée, cartes tour du monde)

## 12 septembre 2026

- Range le dépôt : un dossier par jeu, page d'accueil et page de vérification
- Nouvelle vidéo salle 4 ; masque le bandeau texte sur les décors filmés ou illustrés

## 11 septembre 2026

- Corrige le texte incrusté dans une vidéo, recalibre le planisphère, illustre les leçons

## 10 septembre 2026

- Réorganise l'arborescence des médias : un seul dossier canonique par emplacement
- Renomme les vidéos des escales en minuscules (etape1.mp4...final.mp4)
- Médias déposés directement sur GitHub

## 5 septembre 2026

- Ajoute la video et l'image d'introduction du Tour du Monde

## 4 septembre 2026

- Version initiale : deux escape games pedagogiques CM1-CM2

<!-- dernier-commit: 9878079 -->
