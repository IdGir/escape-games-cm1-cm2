/* ============================================================
   CAPTURES D'ÉCRAN ET CONTRÔLE DANS CHROMIUM (Playwright)
   ------------------------------------------------------------
   Usage (depuis la racine du dépôt, un serveur statique lancé sur
   le port 8765 : « python -m http.server 8765 ») :
     node vingt-mille-lieues/outils/captures.js [dossier-de-sortie]
   Produit des captures 1920×1080 (TBI) et 390×844 (téléphone) des
   écrans de l'escale pilote, vérifie l'absence d'erreur console et
   d'appel réseau externe. Chromium préinstallé (pas de téléchargement).
   ============================================================ */
const { chromium } = require("playwright");
const path = require("path"), fs = require("fs");
const BASE = process.env.BASE || "http://127.0.0.1:8765/vingt-mille-lieues/";
const SORTIE = path.resolve(process.argv[2] || "vingt-mille-lieues/captures");
fs.mkdirSync(SORTIE, { recursive: true });

(async () => {
  const nav = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined, args: ["--autoplay-policy=no-user-gesture-required"] });
  const erreurs = [], externes = [];
  const page = async (w, h) => {
    const ctx = await nav.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const p = await ctx.newPage();
    p.on("console", m => { if(m.type() === "error" && !/404|Failed to load resource/.test(m.text())) erreurs.push(m.text()); });
    p.on("pageerror", e => erreurs.push("JS : " + e.message));
    p.on("request", r => { const u = r.url(); if(!u.startsWith("http://127.0.0.1") && !u.startsWith("data:") && !u.startsWith("blob:")) externes.push(u); });
    return p;
  };
  const cap = async (p, nom) => { await p.waitForTimeout(900); await p.screenshot({ path: path.join(SORTIE, nom + ".png") }); console.log("📸", nom); };

  const p = await page(1920, 1080);
  await p.goto(BASE + "index.html"); await p.waitForTimeout(1500);
  await cap(p, "01-accueil");
  await p.fill("#nom-equipe", "Les Hublots");
  await p.click('[data-grade="timonier"]');
  await p.click("#btn-embarquer");
  await p.waitForTimeout(2500); await cap(p, "02-cinematique");
  await p.click(".cine-passer");
  await p.waitForTimeout(1500); await cap(p, "03-carre-plaque");
  await p.click(".zone.cible", { force: true }); await p.waitForTimeout(800); await cap(p, "04-enigme-tri");
  await p.click(".fermer-panneau");

  const verif = async (niveau, enigme, nom, avant) => {
    await p.goto(BASE + `index.html?verif=1&escale=2&niveau=${niveau}&enigme=${enigme}`);
    await p.waitForTimeout(1800);
    await cap(p, nom + "-decor");
    await p.evaluate(() => VML.ouvrirEnigmeCourante());
    await p.waitForTimeout(700);
    if(avant) await avant(p);
    await cap(p, nom + "-enigme");
  };
  await verif("matelot", 2, "05-machines-matelot");
  await verif("lieutenant", 2, "06-machines-lieutenant");
  await verif("timonier", 3, "07-cabine-timonier");
  await verif("second", 3, "08-cabine-second");
  await verif("matelot", 4, "09-salon-matelot");
  await verif("lieutenant", 4, "10-salon-lieutenant");
  await p.goto(BASE + "index.html?verif=1&escale=2&niveau=matelot&enigme=1"); await p.waitForTimeout(1500);
  await p.evaluate(() => VML.ouvrirBibliotheque("circuit")); await cap(p, "11-bibliotheque");
  await p.goto(BASE + "index.html?verif=1&escale=2&niveau=mousse&enigme=2&secours=1"); await p.waitForTimeout(1500); await cap(p, "12-machines-secours");
  await p.goto(BASE + "index.html?verif=1&escale=2&niveau=mousse&enigme=1&secours=1"); await p.waitForTimeout(1500); await cap(p, "13-carre-secours");
  await p.goto(BASE + "index.html?verif=1&escale=2&niveau=mousse&enigme=3&secours=1"); await p.waitForTimeout(1500); await cap(p, "14-cabine-secours");
  await p.goto(BASE + "index.html?verif=1&escale=2&niveau=mousse&enigme=4&secours=1"); await p.waitForTimeout(1500); await cap(p, "15-salon-secours");
  await p.goto(BASE + "index.html?verif=1&escale=2&niveau=timonier&fin=1"); await p.waitForTimeout(1500); await cap(p, "16-fin-escale");
  await p.goto(BASE.replace(/index.html$/, "") + "prof.html"); await p.waitForTimeout(1500); await cap(p, "17-prof");

  const m = await page(390, 844);
  await m.goto(BASE + "index.html"); await m.waitForTimeout(1200); await cap(m, "20-mobile-accueil");
  await m.goto(BASE + "index.html?verif=1&escale=2&niveau=matelot&enigme=2"); await m.waitForTimeout(1500); await cap(m, "21-mobile-decor");
  await m.evaluate(() => VML.ouvrirEnigmeCourante()); await cap(m, "22-mobile-enigme");

  console.log("\nErreurs console :", erreurs.length ? erreurs : "aucune");
  console.log("Requêtes externes :", externes.length ? externes : "aucune");
  await nav.close();
  process.exit(erreurs.length || externes.length ? 1 : 0);
})();
