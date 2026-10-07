# RECAP — reprise de la production des escape games (après le n°07)

Document de reprise (NE PAS commiter). Dépôt `E:\IDRISS\PROJET ESCAPE GAMES`, branche `escape-games`.

## État au 3 octobre 2026

- Jeu 08 fait : `alimentation/`, commit 3f8fe6e (**à pousser**, avec 70c6483). Tests verts pour 12 jeux. Prochain jeu : n°09 « Le Phare de l'île Lumière » (`prompts-opus/09-lumiere.md`), à partir du squelette `alimentation/` ou `renaissance/`.
- Nouveau piège : la session cloud ne peut transférer de gros fichiers ; travailler par archive réduite (sans vidéos/PDF) et faire `git add`, `maj-hors-ligne.py`, tests et commit sur le PC.

## État au 2 octobre 2026 (historique)

- Jeux 01 à 07 faits. Derniers commits : 49d06ff (n°06 `versailles/`, déjà poussé), 70c6483 (n°07 `renaissance/`, **à pousser**).
- Tous les tests sont verts (11 jeux) : `node outils-tests/tous.js` (jeu par jeu si besoin) et `commun/tests/test-*.js`.
- Prochain jeu : n°08 « Le Grand Repas du chef » (sciences, année A, P2) — prompt `prompts-opus/08-alimentation.md`.

## Méthode qui marche (à reprendre pour chaque jeu)

1. Lire le prompt (section 9), vérifier les faits en ligne (sources officielles), noter les doutes dans `A-VERIFIER.md`.
2. Copier le squelette de `renaissance/` (index.html, prof.html, lecons-imprimables.html, js/, css/, tests/).
3. Générer les données par scripts Python : `enigmes.json` (5 salles, 3 énigmes CM1 + 1 CM2 par salle, 10 types, jamais deux types
   consécutifs, une manipulation ordre/plan/tri par salle), `dialogues.json`, `lecons.json` (220-600 mots CM2 + lexique + document),
   `evaluations.json` (quizz 5/5, QCM 10/12, fermées 8/8, documents 2/2, 5 fiches ; options mélangées).
4. Adapter `js/jeu.js`, `js/app.js` (clés localStorage, données de secours, écran de fin, badges, mentions, quizz de secours),
   `js/reglages.js`, `js/lecons.js`, `js/decors.js` (5 SVG), `js/personnages.js` (5 personnages inventés), `index.html`, `prof.html`, `css/style.css`.
5. Docs : `tests/generer-readme.py` + `tests/readme-suite.md` → README.md ; GUIDE-PEDAGOGIQUE.md (tableau compétence énigme par énigme) ;
   A-VERIFIER.md ; CHANGELOG.md (finir par `<!-- dernier-commit: <HEAD> -->`) ; assets/README.md ; assets/medias/CREDITS-medias.md.
6. Leçons A4 : `outils-lecons/jeux/<slug>.py`, puis `GEO_DIR="$PWD/outils-lecons/geo-donnees/" python3 outils-lecons/construire.py <slug>`
   (geo-donnees et node_modules d'outils-lecons doivent être présents ; voir outils-lecons/README.md).
7. Affiche + bande-annonce : capturer les décors SVG en JPG (Playwright), `affiche-fond.jpg` dans le jeu, puis
   `outils-medias/affiches.py <slug>` et `bande-annonce.py <slug>` (les captures de salles ne doivent PAS rester dans assets/images/decors/).
8. Intégration : catalogue.js (dossier, résumé, couleurs), index.html (carte + couleurs + liste hors connexion), verifier.html (onglet,
   constructeur, COH_JEUX, COH_COMMUN_6), serveur.py, demo.html, editeur.html, outils-docs/maj-journaux.py, outils-lecons (brancher_boutons.py,
   verifier.py), commun/tests (listes de jeux ; compteurs de test-pages : compétences 5 par jeu, extraits demo, « 1 / N », jeux à venir de la
   période), outils-tests/moteur-commun.js (commentaire), README racine (tableau, liens de test, arborescence, « N jeux »), commun/README.md.
9. `git add` par chemins nommés, PUIS `python3 outils-pwa/maj-hors-ligne.py` (il ne voit que les fichiers suivis), re-`git add sw-fichiers.js`, tests, commit.

## Pièges

- Le dossier monté interdit la suppression par défaut : git laisse `.git/index.lock` ; demander l'autorisation de suppression.
- Tests jsdom : installer `jsdom@24` dans `$HOME` de la VM (`npm install jsdom@24`) et lancer avec `NODE_PATH=$HOME/node_modules`.
- Le test « aucune correction affichée » échoue si la correction commence comme le texte de l'énigme : reformuler la correction.
- Les lettres cachées (type `lettres`) doivent être dans le désordre, avec des leurres.

## Pour publier (Invite de commandes Windows)

Windows + R, `cmd`, Entrée, puis : `E:` ; `cd "\IDRISS\PROJET ESCAPE GAMES"` ; `git status` ; `git push origin escape-games`.
