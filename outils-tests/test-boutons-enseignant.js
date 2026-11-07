#!/usr/bin/env node
/* Test des boutons de l'espace enseignant, À L'ÉTAT INITIAL (aucune équipe démarrée).
 *
 *   NODE_PATH=$HOME/node_modules node outils-tests/test-boutons-enseignant.js [jeu ...]
 *   (jsdom@24 : npm install jsdom@24 dans $HOME ; sans argument : tous les jeux)
 *
 * Pourquoi : un test fait avec une équipe démarrée ne voit pas les boutons qui lisent VML.ETAT (vide avant la partie).
 * Pour chaque jeu immersif (immersifs/<jeu>/) :
 *   - index.html : ouvre ⚙️ Réglages et clique chaque bouton [data-act] ; aucune erreur ; « Leçons A4 » ouvre une adresse qui existe ;
 *   - prof.html  : clique les boutons d'ouverture (window.open) et vérifie que chaque lien cible un fichier qui existe ;
 *                  sans serveur local, les boutons de suivi sont désactivés et le bandeau d'explication est visible ;
 *   - lecons-imprimables.html : 5 pages pour chacun des 5 grades.
 * Pour le jeu classique (<jeu>/) : prof.html (boutons d'ouverture) et lecons-imprimables.html.
 * Code de sortie 1 au moindre échec.
 */
const http = require("http"), fs = require("fs"), path = require("path");
const { JSDOM, VirtualConsole } = require("jsdom");
const RACINE = path.resolve(__dirname, "..");
const MIME = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".json": "application/json", ".css": "text/css", ".svg": "image/svg+xml" };
const GRADES = ["mousse", "matelot", "timonier", "lieutenant", "second"];
let echecs = 0, verifs = 0;
const ok = (c, msg) => { verifs++; if(!c){ echecs++; console.log("  ✖ " + msg); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));

const serveur = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split("?")[0]);
  const f = path.join(RACINE, u.endsWith("/") ? u + "index.html" : u);
  if(!f.startsWith(RACINE) || !fs.existsSync(f) || fs.statSync(f).isDirectory()){ res.writeHead(404); return res.end("404"); }
  res.writeHead(200, { "Content-Type": MIME[path.extname(f)] || "application/octet-stream" });
  fs.createReadStream(f).pipe(res);
});

function existe(base, href){            // l'adresse (relative à base) correspond-elle à un fichier du dépôt ?
  try{
    const u = new URL(href, base); if(u.hostname !== "127.0.0.1") return true;     // lien externe : hors test
    let f = path.join(RACINE, decodeURIComponent(u.pathname)); if(f.endsWith(path.sep)) f += "index.html";
    return fs.existsSync(f);
  }catch(e){ return false; }
}

async function charger(url, attente){
  const erreurs = [], ouverts = [], alertes = [];
  const vc = new VirtualConsole();
  vc.on("jsdomError", e => { if(!/Not implemented/.test(e.message)) erreurs.push(String(e.message).split("\n")[0]); });
  const dom = await JSDOM.fromURL(url, { runScripts: "dangerously", resources: "usable", pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w){
      w.fetch = (u, o) => fetch(new URL(u, w.location.href), o);
      w.open = u => { ouverts.push(new URL(u, w.location.href).href); return { focus(){} }; };
      w.URL.createObjectURL = () => 'blob:test'; w.URL.revokeObjectURL = () => {}; w.HTMLAnchorElement.prototype.click = function(){};
      w.print = () => {}; w.confirm = () => false; w.prompt = () => null; w.alert = m => alertes.push(m);
      w.addEventListener("error", e => erreurs.push("erreur non rattrapée : " + e.message));
    } });
  await dormir(attente || 2500);
  return { dom, w: dom.window, d: dom.window.document, erreurs, ouverts, alertes };
}

async function testReglages(base, jeu){
  const p = await charger(`${base}/immersifs/${jeu}/index.html`, 3000);
  ok(p.w.VML && typeof p.w.VML.ouvrirReglages === "function", `${jeu} : le moteur n'est pas chargé (index immersif)`);
  if(p.w.VML && p.w.VML.ouvrirReglages){
    ok(p.w.VML.ETAT == null, `${jeu} : l'état initial devrait être vide pour ce test`);
    p.w.VML.ouvrirReglages();
    const boutons = [...p.d.querySelectorAll("button[data-act]")];
    ok(boutons.length >= 5, `${jeu} : boutons de réglages trouvés : ${boutons.length}`);
    for(const b of boutons){
      const n = p.erreurs.length, o = p.ouverts.length;
      b.click(); await dormir(150);
      ok(p.erreurs.length === n, `${jeu} : le bouton « ${b.textContent.trim()} » lève une erreur à l'état initial : ${p.erreurs.slice(n).join(" | ")}`);
      if(b.dataset.act === "lecons"){
        ok(p.ouverts.length === o + 1, `${jeu} : « Leçons A4 » n'ouvre rien`);
        if(p.ouverts.length > o) ok(existe(base, p.ouverts[o]), `${jeu} : « Leçons A4 » ouvre une adresse inexistante : ${p.ouverts[o]}`);
      }
    }
  }
  p.w.close();
}

async function testProf(base, chemin, immersif){
  const p = await charger(`${base}/${chemin}`, 3000);
  const nom = chemin;
  ok(p.erreurs.length === 0, `${nom} : erreurs au chargement : ${p.erreurs.slice(0, 2).join(" | ")}`);
  // liens
  [...p.d.querySelectorAll("a[href]")].forEach(a => {
    const h = a.getAttribute("href"); if(/^(#|mailto:|javascript:)/.test(h)) return;
    ok(existe(p.w.location.href, h), `${nom} : lien cassé « ${a.textContent.trim().slice(0, 30)} » → ${h}`);
  });
  // boutons d'ouverture (window.open)
  for(const b of [...p.d.querySelectorAll("[onclick]")].filter(x => /window\.open/.test(x.getAttribute("onclick")))){
    const n = p.erreurs.length, o = p.ouverts.length;
    b.click(); await dormir(100);
    ok(p.erreurs.length === n, `${nom} : « ${b.textContent.trim().slice(0, 30)} » lève une erreur`);
    ok(p.ouverts.length === o + 1 && existe(p.w.location.href, p.ouverts[o]), `${nom} : « ${b.textContent.trim().slice(0, 30)} » n'ouvre pas une adresse existante`);
  }
  if(immersif){
    // sans serveur local : bandeau visible, boutons de suivi désactivés, mais les autres boutons restent actifs
    const bandeau = p.d.getElementById("alerte-serveur");
    ok(bandeau && !bandeau.hidden, `${nom} : le bandeau « suivi en direct indisponible » n'apparaît pas sans serveur`);
    ["tout-pause", "tout-reprise", "tout-message", "tout-fin"].forEach(id => { const b = p.d.getElementById(id); ok(b && b.disabled, `${nom} : #${id} devrait être désactivé sans serveur`); });
    const txt = [...p.d.querySelectorAll("a.btn-laiton")].map(a => a.textContent);
    ["Leçons à imprimer", "Résultats", "classement", "poste élève", "Correction collective", "Fiche de séquence"].forEach(t =>
      ok(txt.some(x => x.toLowerCase().includes(t.toLowerCase())), `${nom} : bouton « ${t} » absent`));
    // boutons « Export CSV » et « Imprimer » : aucun plantage
    for(const id of ["export-csv", "imprimer", "anonymiser"]){
      const b = p.d.getElementById(id), n = p.erreurs.length; if(!b){ ok(false, `${nom} : #${id} absent`); continue; }
      b.click(); await dormir(100); ok(p.erreurs.length === n, `${nom} : #${id} lève une erreur`);
    }
  }
  p.w.close();
}

async function testLecons(base, chemin, niveaux){
  for(const n of niveaux){
    const p = await charger(`${base}/${chemin}?niveau=${n}`, 3500);
    const pages = p.d.querySelectorAll(".page, .feuille").length;
    ok(pages >= 5, `${chemin}?niveau=${n} : ${pages} page(s) rendue(s) (5 attendues)`);
    ok(p.erreurs.length === 0, `${chemin}?niveau=${n} : erreurs : ${p.erreurs.slice(0, 2).join(" | ")}`);
    p.w.close();
  }
}

(async () => {
  await new Promise(r => serveur.listen(0, "127.0.0.1", r));
  const base = "http://127.0.0.1:" + serveur.address().port;
  const tous = fs.readdirSync(path.join(RACINE, "immersifs"), { withFileTypes: true }).filter(e => e.isDirectory() && fs.existsSync(path.join(RACINE, "immersifs", e.name, "index.html"))).map(e => e.name);
  const jeux = process.argv.length > 2 ? process.argv.slice(2) : tous;
  for(const jeu of jeux){
    const avant = echecs;
    console.log("== " + jeu);
    const cfg = fs.readFileSync(path.join(RACINE, "immersifs", jeu, "js", "jeu-config.js"), "utf8");
    const g = GRADES.filter(x => cfg.includes('"' + x + '"'));
    ok(g.length === 5, `${jeu} : ${g.length} grade(s) dans jeu-config.js (5 attendus : ${GRADES.join(", ")})`);
    await testReglages(base, jeu);
    await testProf(base, `immersifs/${jeu}/prof.html`, true);
    await testLecons(base, `immersifs/${jeu}/lecons-imprimables.html`, GRADES);
    if(fs.existsSync(path.join(RACINE, jeu, "prof.html"))){
      await testProf(base, `${jeu}/prof.html`, false);
      await testLecons(base, `${jeu}/lecons-imprimables.html`, ["CM1", "CM2"]);
    }
    console.log(echecs === avant ? "  ✔ ok" : "  ✖ " + (echecs - avant) + " échec(s)");
  }
  console.log(`\n${verifs} vérifications, ${echecs} échec(s)`);
  serveur.close(); process.exit(echecs ? 1 : 0);
})();
