/* Tests automatiques — L'Atelier de Léonard à Amboise (Node + jsdom)
   Depuis la racine du dépôt :  node renaissance/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node renaissance/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "L'Atelier de Léonard à Amboise",
  scoresMax: { CM1: 185, CM2: 235 },
});
