# Reprise : intégration du jeu n°11 « Le Grand Prix de l'observatoire » (mouvement) à l'accueil

État au 09/11/2026 (tâche planifiée) : `mouvement/` et `immersifs/mouvement/` existent (commit 1b41786) mais le jeu
**n'apparaît pas sur l'accueil** (catalogue : `"dossier": null`, pas de carte dans `index.html`). Les 11 autres jeux à variante
immersive ouvrent bien l'immersif par défaut.

Intégration préparée puis annulée (fichiers protégés, médias nécessaires) : `RECAP-integration-mouvement.diff`
(19 fichiers : catalogue, carte de l'accueil en immersif par défaut, verifier.html, serveur.py, demo.html, listes des tests et
outils, README). Pour la reprendre : `git apply RECAP-integration-mouvement.diff`.

Restait à faire pour que les tests communs passent (commun/tests/test-pages.js, test-coherence.js) :
- affiche et bande-annonce de mouvement (`outils-medias/`) et leur crédit dans `mouvement/assets/medias/CREDITS-medias.md` : **médias, accord de l'enseignant** ;
- compteurs de test-pages.js : 15 jeux publiés, 95 compétences (passeport.html : 85 → à vérifier), « P2 Année B : 0 jeu à venir », extrait de démo, bandeau ;
- intitulés LSU et formulations des 5 leçons (mouvement/distance, duree, comparer, trajectoires, observateur) ;
- test-coherence : format de `mouvement/CHANGELOG.md` (F2).
