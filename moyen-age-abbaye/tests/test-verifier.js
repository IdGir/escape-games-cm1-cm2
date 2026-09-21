/* Test de verifier.html pour « Le Manuscrit de l'abbaye » et non-régression des autres onglets.
   Lancement depuis la racine du dépôt : node moyen-age-abbaye/tests/test-verifier.js */
const fs = require("fs"), path = require("path");
const { JSDOM, VirtualConsole, ResourceLoader } = require("jsdom");
class ChargeurLocal extends ResourceLoader {
  fetch(url){
    const f = path.join(RACINE, decodeURIComponent(new URL(url).pathname));
    return (fs.existsSync(f) && fs.statSync(f).isFile() && /\.js$/.test(f)) ? Promise.resolve(fs.readFileSync(f)) : null;
  }
}
const RACINE = path.resolve(__dirname, "..", "..");
let ko = 0, okn = 0;
const ok = (c, m) => { if(c) okn++; else { ko++; console.error("  ✗ " + m); } };
const pause = ms => new Promise(r => setTimeout(r, ms));

async function onglet(id){
  const erreurs = [];
  const vc = new VirtualConsole();
  vc.on("jsdomError", e => erreurs.push(e.message));
  const dom = new JSDOM(fs.readFileSync(path.join(RACINE, "verifier.html"), "utf8"), {
    url: "http://localhost/verifier.html#" + id, runScripts: "dangerously", resources: new ChargeurLocal(), pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w){
      w.fetch = async (url) => {
        const u = new URL(url, w.location.href);
        if(u.pathname === "/api/fichiers") return { ok: false, status: 404, json: async () => ({}) };
        const f = path.join(RACINE, decodeURIComponent(u.pathname));
        const existe = fs.existsSync(f) && fs.statSync(f).isFile();
        return { ok: existe, status: existe ? 200 : 404,
          json: async () => JSON.parse(fs.readFileSync(f, "utf8")), text: async () => existe ? fs.readFileSync(f, "utf8") : "",
          headers: { get: () => null } };
      };
      w.HTMLElement.prototype.scrollIntoView = function(){};
    }
  });
  const w = dom.window;
  for(let i = 0; i < 100 && !w.document.querySelector('a[href*="salle="], a[href*="seance="]'); i++) await pause(50);
  return { w, erreurs };
}

(async () => {
  const { w, erreurs } = await onglet("moyen-age-abbaye");
  const doc = w.document;
  ok(doc.querySelector('[data-onglet="moyen-age-abbaye"]'), "onglet présent");
  ok(doc.querySelector('[data-onglet="moyen-age-abbaye"]').getAttribute("aria-selected") === "true", "onglet actif via #moyen-age-abbaye");
  const liens = [...doc.querySelectorAll('a[href^="moyen-age-abbaye/?salle="]')].map(a => a.getAttribute("href"));
  const enigmes = [...new Set(liens.filter(h => /enigme=\d/.test(h)))];
  ok(enigmes.filter(h => h.includes("CM1")).length === 15, "15 liens d'énigmes CM1 : " + enigmes.filter(h => h.includes("CM1")).length);
  ok(enigmes.filter(h => h.includes("CM2")).length === 20, "20 liens d'énigmes CM2 : " + enigmes.filter(h => h.includes("CM2")).length);
  ok(liens.includes("moyen-age-abbaye/?salle=6&niveau=CM1"), "lien vers le fermoir");
  ok(/anselme\.(png|mp4)/.test(doc.body.innerHTML) && doc.body.innerHTML.includes("garin"), "emplacements des personnages");
  ok(doc.body.innerHTML.includes("e5-1"), "illustrations d'énigmes listées");
  ok(erreurs.length === 0, "erreurs : " + erreurs.join(" | "));
  w.close();
  for(const id of ["declaration", "tour-du-monde", "mission-geo", "constitution", "station-meteo", "melanges"]){
    const r = await onglet(id);
    ok(r.w.document.querySelector(`a[href^="${id}/"]`), `onglet ${id} toujours construit`);
    ok(r.erreurs.length === 0, `onglet ${id} : ` + r.erreurs.join(" | "));
    r.w.close();
  }
  console.log(`${okn} vérifications réussies, ${ko} échec(s).`);
  process.exit(ko ? 1 : 0);
})();
