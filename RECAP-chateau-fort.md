# RECAP — Escape game n°02 « Le Secret du donjon » (`chateau-fort/`)

Document de reprise (non commité). Dépôt `E:\IDRISS\PROJET ESCAPE GAMES`, branche `escape-games`.

## État : TERMINÉ — commit e402982 (non poussé)

- 5 salles, 20 énigmes (15 en CM1), 10 types ; clés PIERRE, REMPARTS, SEIGNEUR, VILLAGE, REDEVANCES ;
  inscription de la porte + herse relevée par le quizz final (5 questions).
- Personnages : Colin (page), Maître Josselin (maçon ; renommé pour ne pas confondre avec Garin du jeu n°01),
  Dame Aliénor, Mahaut (paysanne), Perrine (meunière).
- JS repris de `moyen-age-abbaye/` (version déjà nettoyée de constitution/ : pas de concours, bouton « Leçon »,
  source dans la correction) ; `app.js` = constitution/ adapté ; `lecons.js` = leçons texte + schéma SVG + lexique + sources.
- Tests : `python chateau-fort/tests/test_json.py` puis `node chateau-fort/tests/test-chateau-fort.js`
  (nécessite `npm install jsdom@26` : la version 30 n'a plus ResourceLoader). Tout est vert.

## Reste à faire

- `git push origin escape-games` (par l'enseignant).
- Relire `chateau-fort/A-VERIFIER.md` (libellé exact du programme 2026, points mineurs).
- Médias facultatifs : voir `chateau-fort/assets/README.md`.

## Pièges

- Plusieurs sessions modifient en parallèle `index.html`, `verifier.html`, `serveur.py`, `README.md` :
  toujours relire la version courante avant d'y écrire.
- Le dossier monté interdit la suppression par défaut : git laisse alors un `.git/index.lock` orphelin.
  Il faut l'autorisation de suppression (ou supprimer le verrou à la main) avant de commiter.
- `test-jeu.js` de moyen-age-abbaye semble bloquer à l'étape 4 avec jsdom 26 (indépendant de ce jeu).
