# Journal des versions — Le Secret de la Déclaration

Les évolutions du jeu, de la plus récente à la plus ancienne. Ce journal est durable et publié
(contrairement aux fichiers RECAP-… de reprise de session). Les entrées viennent de l'historique
git (`python outils-docs/maj-journaux.py`) ; on peut les compléter à la main.

## 2 octobre 2026

- B2 : bande-annonce de 16 s pour chaque jeu

## 1 octobre 2026

- B4 : affiche 16:9 pour chacun des 9 jeux
- C2 : référence officielle du programme vérifiée et affichée partout
- F2 : journal des versions (CHANGELOG.md) pour chacun des 9 jeux
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

## 19 septembre 2026

- Ajoute l'escape game Le Sceau de la Republique (Constitution de 1958)

## 16 septembre 2026

- Liens GitHub pointés vers la branche escape-games

## 15 septembre 2026

- Ajoute les médias manquants produits avec Agnes (Mission géo, variantes -parle, affiche de fin)
- Passe les vidéos de personnages en fond noir (marquis, maximilien) et ajoute les variantes "-parle" (louise, gutenberg, marquis) pour l'animation pendant les dialogues
- Corrige les décors filmés : Palais-Royal historiquement fidèle (salle1), costumes d'époque uniquement (salle3), suppression de l'anachronisme Arc de Triomphe (cinématique de fin)
- Passe les portraits de personnages en fond noir avec éclairage dramatique (spot), au lieu du fond clair uni
- Met à jour les décors salle2/salle5 (nouvelles vidéos déposées) et ajoute un fondu au noir en fin de salle4

## 13 septembre 2026

- Change le style des vidéos de personnages : dessin animé vers photoréaliste, pour rester cohérent avec les nouveaux portraits
- Change le style des portraits de personnages : dessin animé/aquarelle vers photoréaliste (Déclaration + Tour du monde)
- Ajoute les décors filmés manquants de la Déclaration (salle1, salle2, salle3, salle5, cinématique de fin), générés avec Agnes (text-to-video)
- Ajoute les vidéos des personnages (Déclaration + Tour du monde) et le décor filmé d'intro, générées avec Agnes (image-to-video)
- Ajoute les personnages et décors manquants (portraits, étapes du tour du monde, paysages), corrige les noms de fichiers en majuscule et l'incohérence carte-fuseaux-horaires, générés avec Agnes
- Ajoute le décor de la cinématique d'ouverture (cour du Palais-Royal, 1789), généré avec Agnes
- Synchronise localement les médias déjà déposés sur GitHub (décors salle 1/2/3/5, bastille recompressée, cartes tour du monde)

## 12 septembre 2026

- Range le dépôt : un dossier par jeu, page d'accueil et page de vérification

<!-- dernier-commit: a3167f8 -->
