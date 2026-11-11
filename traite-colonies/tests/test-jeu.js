/* Tests automatiques — Les Archives du port (Node + jsdom)
   Depuis la racine du dépôt :  node traite-colonies/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node traite-colonies/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "Les Archives du port",
  scoresMax: { CM1: 185, CM2: 235 },
});
