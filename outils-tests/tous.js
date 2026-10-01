/* ============================================================
   LANCE TOUS LES TESTS AUTOMATIQUES DES JEUX, l'un après l'autre
   ------------------------------------------------------------
   Depuis la racine du dépôt :   node outils-tests/tous.js
   Un seul jeu :                 node outils-tests/tous.js melanges
   Affiche un tableau récapitulatif ; code de sortie 1 si un jeu échoue.
   ============================================================ */
const { spawnSync } = require("child_process");
const fs = require("fs"), path = require("path");
const RACINE = path.resolve(__dirname, "..");

/* Un jeu = un dossier contenant tests/test-*.js (hors fichiers d'aide). */
const jeux = fs.readdirSync(RACINE).filter(d => fs.existsSync(path.join(RACINE, d, "tests"))).sort();
const filtre = process.argv.slice(2);
const choisis = filtre.length ? jeux.filter(j => filtre.includes(j)) : jeux;

const nodePath = [path.join(__dirname, "node_modules"), process.env.NODE_PATH || ""].filter(Boolean).join(path.delimiter);
const lignes = [];
let echec = false;
for (const jeu of choisis) {
  const fichiers = fs.readdirSync(path.join(RACINE, jeu, "tests"))
    .filter(f => /^test-.*\.js$/.test(f)).sort();
  for (const f of fichiers) {
    const t0 = Date.now();
    process.stdout.write(`▶ ${jeu}/tests/${f} … `);
    const r = spawnSync(process.execPath, [path.join(jeu, "tests", f)], {
      cwd: RACINE, encoding: "utf8", env: { ...process.env, NODE_PATH: nodePath }, maxBuffer: 64 * 1024 * 1024
    });
    const sortie = (r.stdout || "") + (r.stderr || "");
    const bilan = (sortie.match(/(\d+) vérifications réussies, (\d+) échec\(s\)/) || []);
    const ok = r.status === 0;
    if (!ok) echec = true;
    const s = ((Date.now() - t0) / 1000).toFixed(0) + " s";
    console.log(ok ? `ok (${bilan[1] || "?"} vérifications, ${s})` : `ÉCHEC (${s})`);
    if (!ok) console.log(sortie.split("\n").filter(l => /✗|EXCEPTION|ÉCHEC|Error/.test(l)).slice(0, 15).map(l => "    " + l).join("\n"));
    lignes.push({ jeu, test: f, resultat: ok ? "ok" : "ÉCHEC", verifications: bilan[1] || "?", echecs: bilan[2] || "?", duree: s });
  }
}
console.log("");
console.table(lignes);
console.log(echec ? "\nAu moins un jeu a des échecs : voir ci-dessus." : `\nTous les tests passent (${lignes.length} fichiers).`);
process.exit(echec ? 1 : 0);
