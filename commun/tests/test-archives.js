/* ============================================================
   TEST DES ARCHIVES HORS LIGNE SANS SERVEUR (N9)
   Depuis la racine :  node commun/tests/test-archives.js
   Construit l'archive (décompressée) de deux jeux avec
   outils-pwa/archives-hors-ligne.py, puis les ouvre comme en
   double-clic : toute lecture de fichier .json par fetch échoue.
   ============================================================ */
const fs = require("fs"), path = require("path"), { execFileSync } = require("child_process");
const { charger, compteur, dodo, RACINE } = require("../../outils-tests/charge");
const T = compteur("Archives hors ligne (N9)"); const ok = T.ok;
const SORTIE = path.join(RACINE, "archives-hors-ligne", "_test");
const sansFetch = w => { w.fetch = () => Promise.reject(new TypeError("Failed to fetch (file://)")); };
const python = ["python3", "python"].find(p => { try { execFileSync(p, ["--version"], { stdio: "ignore" }); return true; } catch (e) { return false; } });

(async () => {
  try {
    console.log("\n== N9 : archives hors ligne, sans serveur ==");
    if (!python) { ok(false, "Python introuvable : test impossible"); return T.fin(); }
    fs.rmSync(SORTIE, { recursive: true, force: true });
    execFileSync(python, [path.join(RACINE, "outils-pwa", "archives-hors-ligne.py"), "--dossier", "--sortie", SORTIE, "lumiere", "tour-du-monde"], { cwd: RACINE, stdio: "ignore" });
    for (const [j, attendu] of [["lumiere", 20], ["tour-du-monde", null]]) {
      const base = path.join(SORTIE, j + "-hors-ligne");
      ok(fs.existsSync(path.join(base, "JOUER.html")) && fs.existsSync(path.join(base, "LISEZ-MOI.txt")) && fs.existsSync(path.join(base, "commun", "js", "media.js")), `${j} : JOUER.html, LISEZ-MOI.txt et commun/ présents`);
      ok(!fs.existsSync(path.join(base, j, "tests")) && !fs.existsSync(path.join(base, "commun", "tests")), `${j} : sans les dossiers de tests`);
      const html = fs.readFileSync(path.join(base, j, "index.html"), "utf8");
      ok(html.indexOf("js/donnees-embarquees.js") > -1 && html.indexOf("js/donnees-embarquees.js") < html.indexOf("<script src=\"js/jeu.js") , `${j} : données embarquées chargées en premier`);
      const { w, erreurs } = await charger(path.join(base, j), "?salle=1&niveau=CM2", { avant: sansFetch, attente: 700 });
      await dodo(300);
      if (attendu) {
        const n = w.eval("ENIGMES.salles.reduce((t,s)=>t+s.enigmes.filter(e=>!e.niveaux||e.niveaux.includes('CM2')).length,0)");
        ok(n === attendu, `${j} : sans serveur, ${n} énigmes CM2 (toutes, pas le repli de secours)`);
      }
      ok(w.eval("DONNEES && DONNEES.salles && DONNEES.salles.length") === 5, `${j} : dialogues des 5 salles chargés`);
      ok(erreurs.filter(e => !/Failed to fetch/.test(e)).length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
      const l = await charger(path.join(base, j), "", { page: "lecons-imprimables.html", avant: sansFetch, attente: 700 });
      ok(/donnees-embarquees/.test(fs.readFileSync(path.join(base, j, "lecons-imprimables.html"), "utf8")) && l.w.document.body.textContent.length > 500, `${j} : leçons imprimables lisibles sans serveur`);
    }
    // Témoin : le jeu du dépôt, ouvert sans serveur, n'a que ses énigmes de secours
    const t = await charger(path.join(RACINE, "lumiere"), "?salle=1&niveau=CM2", { avant: sansFetch, attente: 700 });
    const n0 = t.w.eval("ENIGMES.salles.reduce((t,s)=>t+s.enigmes.length,0)");
    ok(n0 < 20, `témoin : sans données embarquées, seulement ${n0} énigme(s) de secours`);
    fs.rmSync(SORTIE, { recursive: true, force: true });
  } catch (e) { T.exception(e); }
  T.fin();
})();
