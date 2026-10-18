/* ============================================================
   TEST DU CONTRÔLE D'AFFICHAGE TABLETTE / SMARTPHONE (N17)
   Depuis la racine :  node commun/tests/test-responsive.js
   Il faut un navigateur Chrome ou Edge et puppeteer-core (npm install dans outils-tests) ;
   sinon le test est sauté (code de sortie 0).
   Le contrôleur doit laisser passer l'accueil réel d'un jeu aux trois formats, et attraper un
   bouton essentiel poussé hors de l'écran, recouvert, ou une page qui défile de côté.
   ============================================================ */
const path = require("path");
const R = require("../../outils-tests/verifier-responsive");
let ok = 0, ko = 0;
const verif = (c, m) => { if (c) { ok++; console.log("  ✓ " + m); } else { ko++; console.log("  ✗ " + m); } };

(async () => {
  console.log("== N17 : contrôle de l'affichage tablette et smartphone ==");
  const puppeteer = R.chargerPuppeteer();
  const nav = R.trouverNavigateur();
  if (!puppeteer || !nav) { console.log("  (sauté : " + (!puppeteer ? "puppeteer-core absent" : "navigateur introuvable") + ")"); process.exit(0); }
  verif(Object.keys(R.FORMATS).join() === "tablette10,tablette7,smartphone", "trois formats : tablette 10″, tablette 7″, smartphone");
  verif(R.FORMATS.tablette10.width > R.FORMATS.tablette7.width && R.FORMATS.tablette7.width > R.FORMATS.smartphone.width, "largeurs décroissantes (" + Object.values(R.FORMATS).map(f => f.width).join(" · ") + ")");
  const { s, port } = await R.serveur();
  const base = `http://127.0.0.1:${port}`;
  const b = await puppeteer.launch({ executablePath: nav, headless: true, args: ["--no-sandbox", "--hide-scrollbars", "--mute-audio"] });
  try {
    for (const [id, F] of Object.entries(R.FORMATS)) {
      const page = await b.newPage();
      await page.setViewport({ width: F.width, height: F.height, isMobile: F.mobile, hasTouch: F.mobile });
      const res = await R.controlerEcran(page, base, "melanges", "accueil", F);
      const m = res.m, go = m.essentiels.find(x => /btn-demarrer/.test(x.nom));
      verif(go && !go.horsEcran && !go.recouvert, `${F.nom} : bouton « Démarrer » de l'accueil accessible (${go && go.gauche} → ${go && go.droite} px sur ${m.vw})`);
      verif(m.defileX <= 2, `${F.nom} : la page ne défile pas de côté (${m.defileX} px)`);
      if (id === "smartphone") {
        // 1. bouton poussé hors de l'écran
        await page.evaluate(() => { const b = document.getElementById("btn-demarrer"); b.style.position = "relative"; b.style.left = "500px"; });
        let r = await page.evaluate(require("../../outils-tests/verifier-responsive").mesurerPage(), { essentiels: [["#btn-demarrer"]] });
        verif(r.essentiels[0].horsEcran === true, "défaut simulé : bouton poussé hors de l'écran → repéré (✗)");
        // 2. bouton recouvert par un autre élément
        await page.reload({ waitUntil: "load" });
        await page.waitForSelector("#btn-demarrer", { visible: true });
        await page.evaluate(() => { const c = document.createElement("div"); c.id = "couvercle"; c.style.cssText = "position:fixed;inset:0;background:rgba(0,0,0,.2);z-index:99999"; document.body.appendChild(c); });
        r = await page.evaluate(require("../../outils-tests/verifier-responsive").mesurerPage(), { essentiels: [["#btn-demarrer"]] });
        verif(r.essentiels[0].recouvert === true && /couvercle/.test(r.essentiels[0].par), "défaut simulé : bouton recouvert → repéré, avec le nom de l'élément qui le cache");
        // 3. débordement horizontal
        await page.reload({ waitUntil: "load" });
        await page.waitForSelector("#btn-demarrer", { visible: true });
        await page.evaluate(() => { const d = document.createElement("div"); d.id = "trop-large"; d.textContent = "texte trop large"; d.style.cssText = "width:900px;height:20px;background:#fcc"; document.body.appendChild(d); });
        r = await page.evaluate(require("../../outils-tests/verifier-responsive").mesurerPage(), { essentiels: [["#btn-demarrer"]] });
        verif(r.defileX > 2 && r.depassements.some(d => /trop-large/.test(d.nom)), `défaut simulé : élément trop large → page qui défile (${r.defileX} px) et élément nommé`);
      }
      await page.close();
    }
    // l'énigme et le coffre : boutons essentiels accessibles à 390 px
    const page = await b.newPage();
    const F = R.FORMATS.smartphone;
    await page.setViewport({ width: F.width, height: F.height, isMobile: true, hasTouch: true });
    for (const e of ["enigme", "coffre", "fin"]) {
      const res = await R.controlerEcran(page, base, "constitution", e, F);
      const utiles = res.m.essentiels.filter(x => !x.absent);
      verif(utiles.length >= 1 && utiles.every(x => !x.horsEcran && !x.recouvert), `constitution, smartphone, écran « ${e} » : ${utiles.length} bouton(s) essentiel(s) accessible(s)`);
    }
    await page.close();
  } finally { await b.close(); s.close(); }
  console.log(`\nContrôle responsive : ${ok} vérifications réussies, ${ko} échec(s).`);
  process.exit(ko ? 1 : 0);
})().catch(e => { console.log("  ✗ EXCEPTION " + (e && e.stack || e)); process.exit(1); });
