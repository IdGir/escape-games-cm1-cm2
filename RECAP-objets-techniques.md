# RECAP — Escape game n°04 « L'Atelier de l'inventeur » (objets-techniques/)

État : **TERMINÉ et commité** sur `escape-games` (commit 9871822). Push à faire par l'enseignant.

- 5 salles (entrée de l'atelier / établi / matériauthèque / salle des machines / coin montage),
  personnages Zoé, Awa, Monsieur Marcel, Éléonore Marchand.
- Mots-clés BESOIN, FONCTION, MATÉRIAU, ÉNERGIE, NOTICE → « Un BESOIN, une FONCTION, un MATÉRIAU, une ÉNERGIE, une NOTICE. »
- 15 énigmes CM1 / 20 CM2, 10 types ; 5 leçons texte (schéma SVG, lexique, sources) ; évaluations.
- Moteur `enigmes.js` de constitution/ inchangé (seul le libellé du bouton devient « 📚 Leçon ») ;
  `lecons.js` réécrit pour des leçons texte ; concours retiré.
- Tests : `objets-techniques/tests/` (NODE_PATH vers un jsdom installé hors dépôt) —
  227 vérifications jeu OK, verifier.html OK (8 onglets), données OK.
- Reste : points de `objets-techniques/A-VERIFIER.md` (référence BO du nouveau programme 2026) ;
  médias facultatifs (`assets/README.md`).
- Piège : dans le dossier monté, `git status` peut laisser un `.git/index.lock` vide (suppression
  interdite par défaut) → utiliser `git --no-optional-locks status` ou demander le droit de suppression.
