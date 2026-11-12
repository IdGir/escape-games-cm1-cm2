#!/usr/bin/env node
/* Test EN DIRECT des boutons enseignant des variantes immersives (serveur local + une équipe qui joue).
 *
 *   NODE_PATH=$HOME/node_modules node vingt-mille-lieues/tests/test-boutons-enseignant-direct.js [jeu ...]
 *   (jsdom@24 ; python3 ; lance son propre serveur.py sur un port libre ; sans argument : tous les jeux)
 *
 * Complète outils-tests/test-boutons-enseignant.js (état initial, sans serveur) :
 *   1. une équipe démarre une partie dans immersifs/<jeu>/index.html (nom + grade + « Embarquer ») ;
 *   2. ⚙️ Réglages pendant la partie : chaque bouton [data-act] sans erreur ; Journal et Export fonctionnent ;
 *   3. prof.html voit l'équipe ; chaque bouton de sa carte (pause, +2, +5, message, coup de pouce, grade)
 *      et chaque bouton général (pause, reprise, message, fin de séance) arrive bien chez l'équipe ;
 *   4. Export CSV contient l'équipe.
 * Code de sortie 1 au moindre échec.
 */
const fs = require("fs"), path = require("path"), net = require("net"), { spawn } = require("child_process");
const { JSDOM, VirtualConsole } = require("jsdom");
const RACINE = path.resolve(__dirname, "../..");
let echecs = 0, verifs = 0;
const ok = (c, msg) => { verifs++; if(!c){ echecs++; console.log("  ✖ " + msg); } };
const dormir = ms => new Promise(r => setTimeout(r, ms));
const portLibre = () => new Promise(r => { const s = net.createServer(); s.listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => r(p)); }); });

async function charger(url, attente){
  const erreurs = [], ouverts = [], alertes = [], toasts = [], telechargements = [], impressions = [];
  const vc = new VirtualConsole();
  vc.on("jsdomError", e => { if(!/Not implemented|Could not load (img|link|script|video|audio)/.test(e.message)) erreurs.push(String(e.message).split("\n")[0]); });
  const dom = await JSDOM.fromURL(url, { runScripts: "dangerously", resources: "usable", pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w){
      w.fetch = (u, o) => fetch(new URL(u, w.location.href), o);
      w.open = u => { ouverts.push(new URL(u, w.location.href).href); return { focus(){}, document: { write(){}, close(){} }, print(){}, close(){} }; };
      w.URL.createObjectURL = b => { telechargements.push(b); return "blob:test"; }; w.URL.revokeObjectURL = () => {};
      w.HTMLAnchorElement.prototype.click = function(){};
      w.HTMLMediaElement.prototype.play = function(){ return Promise.resolve(); }; w.HTMLMediaElement.prototype.pause = function(){};
      w.speechSynthesis = { speak(){}, cancel(){}, getVoices: () => [], pause(){}, resume(){}, speaking: false };
      w.print = () => {}; w.confirm = () => true; w.prompt = () => "Message de test"; w.alert = m => alertes.push(m);
      w.addEventListener("error", e => erreurs.push("erreur non rattrapée : " + e.message));
    } });
  await dormir(attente || 2500);
  return { dom, w: dom.window, d: dom.window.document, erreurs, ouverts, alertes, toasts, telechargements, impressions };
}

const dossier = jeu => "immersifs/" + jeu;

async function testerJeu(base, jeu){
  const nomEq = ("Test-" + jeu).slice(0, 20);   // le champ du nom d'équipe est limité en longueur (24 caractères)
  // 1. l'équipe démarre
  const j = await charger(`${base}/${dossier(jeu)}/index.html`, 3500);
  for(let i = 0; i < 20 && !(j.w.VML && j.w.VML.D && j.w.VML.D.enigmes && j.d.querySelector(".carte-grade")); i++) await dormir(500);   // machine chargée : laisser finir
  const V = j.w.VML;
  ok(V && V.D && V.D.enigmes, `${jeu} : moteur non chargé`); if(!V || !V.D) return;
  const t0 = V.toast; V.toast = (m, d) => { j.toasts.push(String(m)); try{ return t0 && t0(m, d); }catch(e){} };
  const finAvant = j.w.alerteFinSeance; let finRecue = null;
  j.w.alerteFinSeance = m => { finRecue = m; try{ return finAvant && finAvant(m); }catch(e){} };
  const g = j.d.querySelector(".carte-grade:not([disabled])"), champ = j.d.getElementById("nom-equipe"), btn = j.d.getElementById("btn-embarquer");
  ok(g && champ && btn, `${jeu} : accueil incomplet (grade, nom, embarquer)`); if(!g || !champ || !btn) return;
  g.click(); champ.value = nomEq; champ.dispatchEvent(new j.w.Event("input")); await dormir(50);
  ok(!btn.disabled, `${jeu} : « Embarquer » reste désactivé`); btn.click();
  await dormir(4000);
  ok(V.ETAT && V.ETAT.equipe === nomEq, `${jeu} : la partie n'a pas démarré`);
  ok(V.SYNC && V.SYNC.actif, `${jeu} : la synchronisation avec le serveur ne s'est pas activée`);
  if(!V.ETAT) return;
  const grade0 = V.ETAT.niveau;
  // passer la cinématique d'ouverture si elle est affichée
  for(let i = 0; i < 30 && j.d.body.dataset.ecran === "ecran-cine"; i++){ const p = j.d.querySelector(".cine-passer, [data-passer], .cine-suivant"); if(p) p.click(); await dormir(200); }

  // 2. réglages pendant la partie
  V.ouvrirReglages();
  const boutons = [...j.d.querySelectorAll("#reglages button[data-act]")].filter(b => b.dataset.act !== "effacer");
  ok(boutons.length >= 5, `${jeu} : ${boutons.length} bouton(s) de réglages`);
  for(const b of boutons){
    const n = j.erreurs.length, a = j.alertes.length;
    b.click(); await dormir(200);
    ok(j.erreurs.length === n, `${jeu} : réglages « ${b.textContent.trim()} » (partie en cours) lève une erreur : ${j.erreurs.slice(n).join(" | ")}`);
    if(["journal", "exporter"].includes(b.dataset.act)) ok(j.alertes.length === a, `${jeu} : « ${b.textContent.trim()} » refuse alors qu'une équipe joue : ${j.alertes.slice(a).join(" | ")}`);
  }
  j.d.querySelector(".fermer-reglages") && j.d.querySelector(".fermer-reglages").click();

  // 3. tableau de bord
  const p = await charger(`${base}/${dossier(jeu)}/prof.html`, 4500);
  ok(p.erreurs.length === 0, `${jeu} prof : erreurs au chargement : ${p.erreurs.slice(0, 2).join(" | ")}`);
  ok(p.d.getElementById("alerte-serveur").hidden, `${jeu} prof : le bandeau « serveur introuvable » reste affiché alors que le serveur tourne`);
  ["tout-pause", "tout-reprise", "tout-message", "tout-fin"].forEach(id => { const b = p.d.getElementById(id); ok(b && !b.disabled, `${jeu} prof : #${id} désactivé alors que le serveur tourne`); });
  const carte = () => [...p.d.querySelectorAll(".eq")].find(c => c.dataset.eq === nomEq);
  ok(carte(), `${jeu} prof : l'équipe « ${nomEq} » n'apparaît pas`); if(!carte()) return;

  const attendre = async (cond, ms = 9000) => { for(let t = 0; t < ms; t += 250){ if(await cond()) return true; await dormir(250); } return false; };
  const clicCarte = sel => { const b = carte() && carte().querySelector(sel); if(!b) return false; b.click(); return true; };
  const essais = [
    ["⏸ Pause (équipe)", () => clicCarte('[data-c="pause"]'), () => V.ETAT.enPause === true],
    ["▶️ Reprendre (équipe), aussitôt", () => { const b = carte() && carte().querySelector('[data-c="pause"]'); ok(b && /Reprendre/.test(b.textContent), `${jeu} prof : après « Pause », le bouton de l'équipe n'affiche pas « Reprendre » tout de suite`); return clicCarte('[data-c="pause"]'); }, () => !V.ETAT.enPause],
    ["(tableau de bord à jour en moins de 4 s)", () => true, async () => /⏸ Pause/.test((carte() || { textContent: "" }).textContent), 4000],
    ["⏱️ +2 min", () => clicCarte('[data-c="t2"]'), () => (V.ETAT.delaiAccordeMin || 0) >= 2],
    ["⏱️ +5 min", () => clicCarte('[data-c="t5"]'), () => (V.ETAT.delaiAccordeMin || 0) >= 7],
    ["📣 Message (équipe)", () => clicCarte('[data-c="msg"]'), () => j.toasts.some(m => m.includes("Message de test"))],
    ["🤝 Coup de pouce", () => clicCarte('[data-c="pouce"]'), () => j.toasts.some(m => m.includes("🤝"))],
    ["Grade (liste)", () => { const s = carte().querySelector('select[data-c="niveau"]'); const autre = [...s.options].map(o => o.value).find(v => v !== grade0); s.value = autre; s.dispatchEvent(new p.w.Event("change")); return !!autre; }, () => V.ETAT.niveau !== grade0],
    ["⏸ Pause générale", () => { p.d.getElementById("tout-pause").click(); return true; }, () => V.ETAT.enPause === true],
    ["🤝 Coup de pouce pendant la pause (gardé)", () => { j.toasts.length = 0; return clicCarte('[data-c="pouce"]'); }, () => !!V.ETAT.poucePending],
    ["▶️ Reprise générale", () => { p.d.getElementById("tout-reprise").click(); return true; }, () => !V.ETAT.enPause],
    ["(coup de pouce de la pause appliqué à la reprise)", () => true, () => j.toasts.some(m => m.includes("🤝"))],
    ["📣 Message à toutes", () => { j.toasts.length = 0; p.d.getElementById("tout-message").click(); return true; }, () => j.toasts.some(m => m.includes("Message de test"))],
    ["🔔 Fin de séance", () => { p.d.getElementById("tout-fin").click(); return true; }, () => finRecue != null],
  ];
  for(const [nom, agir, verifier, delai] of essais){
    const n = p.erreurs.length;
    const fait = await agir();
    ok(fait, `${jeu} prof : bouton « ${nom} » introuvable`); if(!fait) continue;
    ok(p.erreurs.length === n, `${jeu} prof : « ${nom} » lève une erreur : ${p.erreurs.slice(n).join(" | ")}`);
    ok(await attendre(verifier, delai), `${jeu} : la commande « ${nom} » n'est pas arrivée chez l'équipe`);
    await dormir(300);
  }
  ok(j.erreurs.length === 0, `${jeu} élève : erreurs pendant le test : ${j.erreurs.slice(0, 3).join(" | ")}`);

  // 4. export CSV
  p.telechargements.length = 0; p.d.getElementById("export-csv").click(); await dormir(100);
  const blob = p.telechargements[0];
  const csv = blob ? await new Promise(r => { const f = new p.w.FileReader(); f.onload = () => r(String(f.result)); f.onerror = () => r(""); f.readAsText(blob); }) : "";
  ok(csv.includes(nomEq), `${jeu} prof : l'export CSV ne contient pas l'équipe`);
  j.w.close(); p.w.close();
}

(async () => {
  const port = await portLibre();
  const srv = spawn("python3", [path.join(RACINE, "serveur.py"), String(port)], { cwd: RACINE, stdio: "ignore", env: Object.assign({}, process.env, { PYTHONIOENCODING: "utf-8" }) });
  const base = "http://127.0.0.1:" + port;
  for(let i = 0; i < 40; i++){ try{ const r = await fetch(base + "/api/info"); if(r.ok) break; }catch(e){} await dormir(250); }
  const tous = fs.readdirSync(path.join(RACINE, "immersifs"), { withFileTypes: true }).filter(e => e.isDirectory() && fs.existsSync(path.join(RACINE, "immersifs", e.name, "prof.html"))).map(e => e.name);   // vingt-mille-lieues/ (source) : tableau de bord simplifié, sans greffons : testé par test-boutons-enseignant.js
  const jeux = process.argv.length > 2 ? process.argv.slice(2) : tous;
  for(const jeu of jeux){
    const avant = echecs; console.log("== " + jeu);
    try{ await testerJeu(base, jeu); }catch(e){ ok(false, `${jeu} : exception ${e.message}`); }
    console.log(echecs === avant ? "  ✔ ok" : "  ✖ " + (echecs - avant) + " échec(s)");
  }
  console.log(`\n${verifs} vérifications, ${echecs} échec(s)`);
  srv.kill(); process.exit(echecs ? 1 : 0);
})();
