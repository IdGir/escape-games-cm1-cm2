/* Tests automatiques — Le Grand Prix de l'observatoire (Node + jsdom)
   Depuis la racine du dépôt :  node mouvement/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node mouvement/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "Le Grand Prix de l'observatoire",
  scoresMax: { CM1: 185, CM2: 235 },
});
