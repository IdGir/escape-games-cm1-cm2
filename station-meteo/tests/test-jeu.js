/* Tests automatiques — La Station météo disparue (Node + jsdom)
   Depuis la racine du dépôt :  node station-meteo/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node station-meteo/tests/test-jeu.js partie   (ou types, divers, prof)
   Le type « instrument » (thermomètre, pluviomètre) est propre à ce jeu. */
const fs = require("fs");
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "La Station météo disparue",
  scoresMax: { CM1: 185, CM2: 235 },
  plus: async ({ ok, JEU }) => {
    console.log("\n== Fiche de relevés ==");
    const h = fs.readFileSync(JEU + "/fiche-releves.html", "utf8");
    ok(/<table/i.test(h) && /<title>/i.test(h), "fiche-releves.html : tableau et titre présents");
  }
});
