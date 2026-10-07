# À coller dans une nouvelle conversation (application Claude sur l'ordinateur, dossier E:\IDRISS\PROJET ESCAPE GAMES)

Construis l'escape game n°08 « Le Grand Repas du chef » dans le dossier `alimentation/`. Le contenu est déjà rédigé dans le pack joint : `enigmes.json`, `lecons.json`, `GUIDE-PEDAGOGIQUE.md`, `README.md`, `A-VERIFIER.md`.

- Pars de `renaissance/` (squelette, branché sur `commun/` et les greffons, moteur v2 : 185 / 235 points). Ne copie pas `constitution/`.
- Convertis `enigmes.json` et `lecons.json` au format exact de `renaissance/assets/data/`. Garde les textes tels quels, sauf erreur manifeste.
- Le programme 2026 ne contient plus « production et conservation des aliments ». Suis les compétences du pack et mets à jour la ligne n°08 de `eg-plan-histoire-sciences.md` / du prompt 08.
- À dessiner en SVG : 5 décors (cour du potager et du poulailler, salle des menus, table de dégustation, cabinet avec maquette du corps, salle d'entraînement avec home-trainer), 4 personnages (Rosalie, Nathan, Inès, Basile), et les schémas `schema-machoire` et `schema-appareil-digestif` des énigmes « plan ». Les schémas anatomiques doivent être dessinés, jamais générés par IA.
- Leçons A4 : `outils-lecons/jeux/alimentation.py`. Visuels : courbe de Caramel, toise, barres des besoins, mâchoire, tube digestif, pouls.
- Intégration complète selon `eg-versailles.md` et `eg-renaissance.md` : catalogue, tests communs et compteurs, `demo.html`, `editeur.html`, `sw-fichiers.js` (après `git add`), CHANGELOG avec `dernier-commit`, affiche et bande-annonce.
- Tests : `alimentation/tests/test-jeu.js`, `test-verifier.js`, `test_json.py`, plus les tests communs.
- Fais un commit ciblé sur `escape-games` (jamais `git add .`). **Ne fais pas `git push`.**
