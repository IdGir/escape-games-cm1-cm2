/* Test de verifier.html pour « De l'édit de Nantes à Versailles » et non-régression des autres onglets.
   Lancement depuis la racine du dépôt : node versailles/tests/test-verifier.js */
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
  const { w, erreurs } = await onglet("versailles");
  const doc = w.document;
  ok(doc.querySelector('[data-onglet="versailles"]'), "onglet présent");
  ok(doc.querySelector('[data-onglet="versailles"]').getAttribute("aria-selected") === "true", "onglet actif via #versailles");
  const liens = [...doc.querySelectorAll('a[href^="versailles/?salle="]')].map(a => a.getAttribute("href"));
  const enigmes = [...new Set(liens.filter(h => /enigme=\d/.test(h)))];
  ok(enigmes.filter(h => h.includes("CM1")).length === 15, "15 liens d'énigmes CM1 : " + enigmes.filter(h => h.includes("CM1")).length);
  ok(enigmes.filter(h => h.includes("CM2")).length === 20, "20 liens d'énigmes CM2 : " + enigmes.filter(h => h.includes("CM2")).length);
  ok(liens.includes("versailles/?salle=6&niveau=CM1"), "lien vers le coffre et le pli final");
  ok(/gabriel\.(png|mp4)/.test(doc.body.innerHTML) && doc.body.innerHTML.includes("isabeau"), "emplacements des personnages");
  ok(/salle3/.test(doc.body.innerHTML), "emplacements des décors");
  ok(erreurs.length === 0, "erreurs : " + erreurs.join(" | "));
  w.close();
  for(const id of ["declaration", "constitution", "chateau-fort", "melanges"]){
    const r = await onglet(id);
    ok(r.w.document.querySelector(`a[href^="${id}/"]`), `onglet ${id} toujours construit`);
    ok(r.erreurs.length === 0, `onglet ${id} : ` + r.erreurs.join(" | "));
    r.w.close();
  }
  console.log(`${okn} vérifications réussies, ${ko} échec(s).`);
  process.exit(ko ? 1 : 0);
})();
