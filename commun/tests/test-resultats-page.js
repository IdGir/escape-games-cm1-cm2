/* ============================================================
   TEST DE BOUT EN BOUT : page resultats.html + VRAI serveur local (Node + jsdom + python)
   Depuis la racine du dépôt :  node commun/tests/test-resultats-page.js
   Vérifie ce qui compte pour l'enseignant : rien ne se perd. Import → fichier de la classe,
   fenêtre fermée puis rouverte (même navigateur ou autre), serveur arrêté puis relancé,
   sauvegarde de partie d'un jeu immersif, export en un clic d'un Chromebook.
   ============================================================ */
const fs = require("fs"), os = require("os"), path = require("path"), { spawn } = require("child_process");
let JSDOM, ResourceLoader; try { ({ JSDOM, ResourceLoader } = require("jsdom")); } catch (e) { console.error("jsdom introuvable (cd outils-tests && npm install, ou NODE_PATH)."); process.exit(2); }
const RACINE = path.resolve(__dirname, "..", "..");
const PORT = 8793, BASE = `http://127.0.0.1:${PORT}`;
let verifs = 0; const echecs = [];
const ok = (c, m) => { verifs++; if (!c) { echecs.push(m); console.log("  ✗", m); } else console.log("  ✓", m); };
const dodo = ms => new Promise(r => setTimeout(r, ms));
async function attendre(cond, ms = 4000){ const t = Date.now(); while (Date.now() - t < ms) { try { if (await cond()) return true; } catch (e) {} await dodo(50); } return false; }

const projet = fs.mkdtempSync(path.join(os.tmpdir(), "eg-page-"));
const copier = rel => { const d = path.join(projet, rel); fs.mkdirSync(path.dirname(d), { recursive: true }); fs.copyFileSync(path.join(RACINE, rel), d); };
["serveur.py", "resultats.html", "commun/donnees/catalogue.js", "commun/js/rapport-seance.js", "immersifs/moyen-age-abbaye/assets/data/enigmes.json"].forEach(copier);
let serveur = null;
const demarrer = async () => {
  serveur = spawn(process.platform === "win32" ? "python" : "python3", [path.join(projet, "serveur.py"), String(PORT)], { cwd: os.tmpdir(), stdio: "ignore", env: Object.assign({}, process.env, { PYTHONDONTWRITEBYTECODE: "1", ESCAPE_DONNEES: "" }) });
  ok(await attendre(async () => (await fetch(BASE + "/api/info")).ok, 6000), "serveur local démarré");
};
const arreter = async () => { serveur.kill(); await dodo(400); };

async function ouvrir(stockage){
  const dom = await JSDOM.fromURL(BASE + "/resultats.html", { runScripts: "dangerously", resources: "usable", pretendToBeVisual: true,
    beforeParse(w){
      for (const [k, v] of Object.entries(stockage || {})) w.localStorage.setItem(k, v);
      w.fetch = (u, o) => fetch(new URL(String(u), w.location.href), o);
      if (!w.Blob.prototype.text) w.Blob.prototype.text = function(){ return new Promise((ok, ko) => { const r = new w.FileReader(); r.onload = () => ok(r.result); r.onerror = ko; r.readAsText(this); }); };
      w.confirm = () => true; w.alert = () => {};
      w.addEventListener("error", e => (w.__erreurs = w.__erreurs || []).push(e.message));
    } });
  await attendre(() => dom.window.RESULTATS_PAGE, 4000); await dodo(500);
  return dom;
}
const lignes = dom => [...dom.window.document.querySelectorAll("#corps tr")].filter(tr => !tr.querySelector("td[colspan]")).length;
const stock = dom => { const o = {}, w = dom.window; for (let i = 0; i < w.localStorage.length; i++) { const k = w.localStorage.key(i); o[k] = w.localStorage.getItem(k); } return o; };
const texte = (dom, id) => dom.window.document.getElementById(id).textContent;
async function importer(dom, fichiers){
  const w = dom.window, inp = w.document.getElementById("fichiers");
  Object.defineProperty(inp, "files", { value: fichiers.map(([nom, contenu]) => new w.File([typeof contenu === "string" ? contenu : JSON.stringify(contenu)], nom)), configurable: true });
  inp.dispatchEvent(new w.Event("change")); await dodo(1200);
}
const cr = (eleve, debut, extra) => Object.assign({ type: "escape-game-compte-rendu", version: 1, jeu: "melanges", titre: "Le Laboratoire", eleve, mode: "equipe", niveau: "CM2", date: debut, partie: debut,
  termine: true, dureeMin: 30, score: 100, scoreMax: 125, enigmes: 20, total: 20, premierCoup: 15, erreurs: 2, indices: 1 }, extra || {});
const save = { version: 2, equipe: "Les girls powers", niveau: "timonier", score: 174, escale: 5, escalesFaites: [1, 2, 3, 4], escaleTerminee: false, debut: Date.parse("2026-11-05T13:55:00Z"),
  msTotal: 3532968, erreursTotal: 13, indicesTotal: 0, resolues: { "e1-1": { pts: 10, premier: true }, "e1-2": { pts: 10, premier: false, erreurs: 2 } } };
const serveurListe = async () => (await (await fetch(BASE + "/api/resultats")).json()).resultats;

(async () => {
  try {
    console.log("\n== Page des résultats + vrai serveur ==");
    await demarrer();
    let A = await ouvrir();
    ok(/Enregistrement automatique actif/.test(texte(A, "stockage")) && /http:\/\/[\d.]+:8793\//.test(texte(A, "stockage")), "bandeau : enregistrement automatique actif + adresse à donner aux élèves");
    await importer(A, [["parties-a.json", [cr("Les Lynx", "2026-11-13T09:00"), cr("Les Hiboux", "2026-11-13T09:05")]], ["moyen-age-abbaye-Les_girls_powers.json", save]]);
    ok(lignes(A) === 3, "3 parties importées : 2 comptes-rendus + 1 sauvegarde de partie immersive (" + lignes(A) + ")");
    ok(/sauvegarde\(s\) de partie/.test(texte(A, "message")), "message clair pour la sauvegarde de partie : " + texte(A, "message").slice(0, 90));
    ok(await attendre(async () => (await serveurListe()).length === 3), "les 3 parties sont dans le fichier de la classe (serveur)");
    ok(/Gardé dans le fichier de la classe/.test(texte(A, "message-stockage")), "confirmation affichée : « gardé dans le fichier de la classe »");
    ok((await serveurListe()).some(r => r.eleve === "Les girls powers" && r.enigmes === 2 && r.total === 20 && r.score === 174), "la sauvegarde est convertie (2 énigmes sur 20, score 174)");
    const sa = stock(A); A.window.close();

    console.log("\n== Fenêtre fermée, puis rouverte ==");
    let B = await ouvrir();                                   // autre navigateur : rien en local, tout vient du serveur
    ok(lignes(B) === 3, "autre navigateur (stockage vide) : les 3 parties reviennent toutes seules du serveur (" + lignes(B) + ")");
    B.window.close();
    let C = await ouvrir(sa);                                 // même navigateur
    ok(lignes(C) === 3, "même navigateur : 3 parties, sans doublon (" + lignes(C) + ")");
    C.window.close();

    console.log("\n== Serveur arrêté : rien n'est perdu, tout est renvoyé au redémarrage ==");
    await arreter();
    let D = await ouvrir(sa).catch(() => null);
    ok(D === null, "(page inaccessible sans serveur : on ouvre le fichier autrement)");
    // page ouverte avant l'arrêt = navigateur déjà chargé : on simule en relançant le serveur puis en coupant juste après le chargement
    await demarrer();
    D = await ouvrir(sa);
    await arreter();
    await importer(D, [["parties-b.json", [cr("Les Renards", "2026-11-13T10:00")]]]);
    ok(lignes(D) === 4 && /seulement dans ce navigateur/.test(texte(D, "message-stockage")), "serveur coupé : la partie est gardée dans le navigateur, avec un avertissement clair");
    const sd = stock(D); D.window.close();
    await demarrer();
    ok((await serveurListe()).length === 3, "serveur relancé : 3 parties seulement (la 4e n'est pas encore arrivée)");
    const E = await ouvrir(sd);
    ok(await attendre(async () => (await serveurListe()).length === 4), "à la prochaine ouverture avec le serveur : la 4e partie est envoyée toute seule");
    ok(lignes(E) === 4, "4 parties affichées (" + lignes(E) + ")");
    ok(fs.readFileSync(path.join(projet, "resultats-classe.csv"), "utf8").split("\n").filter(Boolean).length === 5, "resultats-classe.csv (Excel) à jour : en-tête + 4 parties");
    E.window.close();

    console.log("\n== Cas d'erreur et Chromebook ==");
    const F = await ouvrir();
    await importer(F, [["vide.json", "[]"], ["autre.json", { a: 1 }], ["casse.json", "{pas du json"]]);
    ok(/vide/.test(texte(F, "message")) && /ignoré/.test(texte(F, "message")) && /illisible/.test(texte(F, "message")), "fichier vide, étranger et cassé : chacun expliqué (« " + texte(F, "message").slice(0, 80) + "… »)");
    F.window.document.getElementById("depot").dispatchEvent(Object.assign(new F.window.Event("drop", { bubbles: true, cancelable: true }), { dataTransfer: { files: [] } })); await dodo(100);
    ok(/Aucun fichier reçu/.test(texte(F, "message")), "dépôt sans fichier (glisser depuis Nextcloud en ligne) : explication au lieu de « 0 ajouté »");
    F.window.close();
    await arreter();
    class DepotGitHub extends ResourceLoader { fetch(url){ const m = String(url).match(/^https:\/\/idgir\.github\.io\/escape-games-cm1-cm2\/([^?#]+)/); return m ? Promise.resolve(fs.readFileSync(path.join(projet, m[1]))) : null; } }
    const G = await JSDOM.fromFile(path.join(projet, "resultats.html"), { runScripts: "dangerously", resources: new DepotGitHub(), url: "https://idgir.github.io/escape-games-cm1-cm2/resultats.html", pretendToBeVisual: true,
      beforeParse(w){ w.localStorage.setItem("escape_resultats", JSON.stringify([cr("Chromebook 3", "2026-11-12T14:00"), cr("Chromebook 3 bis", "2026-11-12T14:30")]));
        w.fetch = async () => ({ ok: false, status: 404, json: async () => ({}) }); if (!w.Blob.prototype.text) w.Blob.prototype.text = function(){ return new Promise((ok, ko) => { const r = new w.FileReader(); r.onload = () => ok(r.result); r.onerror = ko; r.readAsText(this); }); }; w.confirm = () => true; w.URL.createObjectURL = () => "blob:x"; } });
    await attendre(() => G.window.RESULTATS_PAGE, 4000); await dodo(600);
    ok(/GitHub/.test(texte(G, "stockage")) && /aucune partie n'est centralisée/.test(texte(G, "stockage")), "sur GitHub : bandeau honnête (pas de centralisation) avec la marche à suivre");
    G.window.document.getElementById("exp-appareil").click(); await dodo(100);
    const ex = G.window.__dernierExport;
    ok(ex && /^parties-appareil-\d{4}-\d\d-\d\d-\d\dh\d\d\.json$/.test(ex.nom) && JSON.parse(ex.contenu).length === 2, "Chromebook : « Exporter les parties de cet appareil » donne un fichier de 2 parties, jamais vide");
    G.window.close();
  } finally {
    if (serveur) serveur.kill();
    fs.rmSync(projet, { recursive: true, force: true });
  }
  console.log(`\nPage + serveur : ${verifs} vérifications, ${echecs.length} échec(s).`);
  process.exit(echecs.length ? 1 : 0);
})();
