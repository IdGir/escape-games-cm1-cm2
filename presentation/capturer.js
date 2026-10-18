#!/usr/bin/env node
/* ============================================================
   CAPTURES D'ÉCRAN DU KIT DE PRÉSENTATION (amélioration N21)
   ------------------------------------------------------------
   Régénère presentation/captures/*.jpg à partir des VRAIES pages du dépôt
   (accueil, jeu, énigme, correction collective, tableau de bord, bilan de classe,
   année), pour que le diaporama reste à jour quand les jeux évoluent :

       node presentation/capturer.js

   Il faut Chrome ou Edge installé et « npm install » dans outils-tests (puppeteer-core), comme
   pour outils-tests/verifier-responsive.js, dont il réutilise le serveur local.
   Les équipes et élèves des captures sont FICTIFS (données de démonstration injectées dans la
   page, jamais lues sur l'appareil) : aucune donnée d'élève réelle n'est publiée.
   ============================================================ */
const fs = require("fs");
const path = require("path");
const R = require("../outils-tests/verifier-responsive");
const SORTIE = path.join(__dirname, "captures");
const LARGEUR = 1280, HAUTEUR = 720;

/* Parties de démonstration (équipes fictives) pour le bilan de classe */
function parties(){
  const base = { type: "escape-game-compte-rendu", version: 1, jeu: "melanges", titre: "Le Laboratoire de Madame Mélange", mode: "equipe", niveau: "CM2", termine: true, scoreMax: 235, enigmes: 20, total: 20, dureeMin: 52 };
  const e = (id, s, l, pc, err, ind) => ({ id, s, l, ok: 1, pc, e: err, i: ind, p: 0, c: 0 });
  const equipes = [["Les Lynx", [0, 1, 1, 0, 1]], ["Les Hiboux", [0, 0, 1, 1, 1]], ["Les Renards", [1, 0, 1, 0, 1]], ["Les Aigles", [0, 1, 1, 1, 1]], ["Les Loutres", [0, 0, 0, 1, 1]]];
  const ids = [["1-1", 1, "masses"], ["1-2", 1, "masses"], ["2-1", 2, "conservation"], ["3-1", 3, "melanges"], ["5-1", 5, "separer-liquide"]];
  return equipes.map(([nom, pcs], k) => Object.assign({}, base, {
    eleve: nom, date: `2026-10-1${2 + (k % 3)}T10:${10 + k}`, partie: `2026-10-1${2 + (k % 3)}T09:${10 + k}`, score: 120 + 18 * k, premierCoup: 9 + k, erreurs: 6 - k, indices: 3,
    detail: ids.map(([id, s, l], i) => e(id, s, l, pcs[i], pcs[i] ? 0 : 1 + (k % 2), pcs[i] ? 0 : 1))
  }));
}
const EQUIPES = [
  { equipe: "Les Lynx", jeu: "melanges", niveau: "CM2", salle: 3, enigme: 1, score: 78, fragments: ["PESER", "COMPARER"], msEcoules: 1380000, enigmesReussies: 9, pouces: 1 },
  { equipe: "Les Hiboux", jeu: "melanges", niveau: "CM1", salle: 2, enigme: 2, score: 41, fragments: ["PESER"], msEcoules: 960000, palier: "decouverte", enigmesReussies: 5, passees: 1 },
  { equipe: "Les Renards", jeu: "melanges", niveau: "CM2", salle: 4, enigme: 0, score: 102, fragments: ["PESER", "COMPARER", "OBSERVER"], msEcoules: 1740000, enigmesReussies: 12 },
  { equipe: "Les Loutres", jeu: "melanges", niveau: "CM2", salle: 5, fini: true, score: 188, fragments: ["PESER", "COMPARER", "OBSERVER", "AIMANTER", "ÉVAPORER"], msEcoules: 2820000, enigmesReussies: 20 }
];

const CAPTURES = [
  { nom: "accueil", url: "/index.html", attend: ".mascotte-bloc", avant: p => p.evaluate(() => { const r = document.querySelector(".mascotte-regles"); if(r) r.hidden = true; }) },
  { nom: "jeu-accueil", url: "/melanges/index.html", attend: "#btn-demarrer", avant: p => p.evaluate(() => { const r = document.querySelector(".mascotte-regles"); if(r) r.hidden = false; const b = document.querySelector(".mascotte-bloc"); if(b) b.scrollIntoView({ block: "start" }); }) },
  { nom: "jeu-enigme", url: "/melanges/index.html?salle=2&niveau=CM2&enigme=1", attend: ".enigme-carte", avant: p => p.evaluate(() => { document.querySelectorAll(".toast").forEach(x => x.remove()); const c = document.querySelector(".enigme-carte"); if(c) c.scrollIntoView({ block: "start" }); }) },
  { nom: "correction-collective", url: "/melanges/index.html?correction=1&niveau=CM2&salle=1", attend: "#correction-collective .cc-enigme", avant: p => p.evaluate(() => { document.querySelectorAll("#correction-collective .cc-enigme .cc-voir").forEach((b, i) => { if(i < 2) b.click(); }); }) },
  { nom: "tableau-de-bord", url: "/melanges/prof.html", attend: "#corps-equipes", avant: p => p.evaluate(eq => { afficher(eq); document.getElementById("nb-equipes").textContent = eq.length; document.getElementById("ip-locale").textContent = "192.168.1.20:8000"; document.getElementById("url-eleves").textContent = "http://192.168.1.20:8000/"; }, EQUIPES) },
  { nom: "bilan-de-classe", url: "/resultats.html", attend: "#bilan", stockage: { escape_resultats: JSON.stringify(parties()) }, avant: async p => { await p.click("#btn-appareil"); await new Promise(r => setTimeout(r, 700)); await p.evaluate(() => document.getElementById("bilan").scrollIntoView({ block: "start" })); } },
  { nom: "annee", url: "/annee.html", attend: "#periodes .bloc" }
];

async function lancer(){
  const puppeteer = R.chargerPuppeteer(), nav = R.trouverNavigateur();
  if(!puppeteer || !nav){ console.log("⚠ Captures sautées : " + (!puppeteer ? "puppeteer-core absent (npm install dans outils-tests)" : "Chrome ou Edge introuvable (variable CHROME_PATH)") + "."); return 0; }
  fs.mkdirSync(SORTIE, { recursive: true });
  const { s, port } = await R.serveur();
  const b = await puppeteer.launch({ executablePath: nav, headless: true, args: ["--no-sandbox", "--mute-audio"] });
  let n = 0;
  try{
    for(const c of CAPTURES){
      const page = await b.newPage();
      await page.setViewport({ width: LARGEUR, height: HAUTEUR, deviceScaleFactor: 1 });
      await page.evaluateOnNewDocument(st => { try{ localStorage.clear(); Object.entries(st || {}).forEach(([k, v]) => localStorage.setItem(k, v)); }catch(e){} }, c.stockage || {});
      await page.goto(`http://127.0.0.1:${port}${c.url}`, { waitUntil: "load", timeout: 20000 });
      try{ await page.waitForSelector(c.attend, { visible: true, timeout: 8000 }); }catch(e){ console.log(`⚠ ${c.nom} : « ${c.attend} » introuvable`); }
      if(c.avant) await c.avant(page);
      await new Promise(r => setTimeout(r, 700));
      await page.screenshot({ path: path.join(SORTIE, c.nom + ".jpg"), type: "jpeg", quality: 82 });
      console.log(`✓ ${c.nom}.jpg (${Math.round(fs.statSync(path.join(SORTIE, c.nom + ".jpg")).size / 1024)} Ko)`);
      n++; await page.close();
    }
  } finally { await b.close(); s.close(); }
  console.log(`\n${n} capture(s) dans presentation/captures/.`);
  return 0;
}
if(require.main === module) lancer().then(c => process.exit(c), e => { console.error(e); process.exit(1); });
module.exports = { lancer, CAPTURES, EQUIPES, parties };
