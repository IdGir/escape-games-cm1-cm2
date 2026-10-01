/* ============================================================
   TESTS DES JEUX À MOTEUR PROPRE (Node + jsdom)
   ------------------------------------------------------------
   declaration et tour-du-monde : 5 salles à énigme unique, 4 fragments,
   coffre final. Reprise en jsdom des scripts Playwright de
   outils-moteur/tester_declaration.py et tester_tour_du_monde.py,
   plus : vérification de la fin, réglages, leçons, impressions,
   tableau de bord. Chaque jeu fournit :
     resoudre : code d'une fonction (n) => {…} exécutée DANS la page
     faux1    : code d'une fonction () => texte du retour, salle 1 ratée
     attenduFaux1 : expressions attendues dans ce retour
     interdits : expressions de correction interdites après la réussite
   ============================================================ */
const fs = require("fs"), path = require("path");
const { charger, compteur, dodo, attendreQue, testerLeconsA4 } = require("./charge");

function lancer(dossierJeu, cfg){
  const JEU = path.resolve(dossierJeu);
  const T = compteur(cfg.titre); const ok = T.ok;
  const texte = (w, sel) => { const el = w.document.querySelector(sel); return el ? el.textContent.replace(/\s+/g, " ") : ""; };
  const clic = (w, el) => el && el.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));

  async function partie(niveau){
    console.log(`\n== Partie complète ${niveau} (salle 1 ratée, coffre raté une fois) ==`);
    const { w, erreurs } = await charger(JEU, `?salle=1&niveau=${niveau}`, { attente: 800 });
    w.eval("ETAT.reglages.cinematiques = false; setNarrationActif(false)");
    const fragments = [];
    for (let n = 1; n <= 5; n++) {
      ok(await attendreQue(() => w.document.querySelector(".zone-enigme"), 6000), `${niveau} salle ${n} : zone d'énigme`);
      if (n === 1) {
        const fb = w.eval(`(${cfg.faux1})()`);
        ok(/Pas tout juste/.test(fb) && /bonus/.test(fb) && cfg.attenduFaux1.every(x => fb.includes(x)), `${niveau} salle 1 : retour d'erreur inattendu : « ${fb.replace(/\s+/g, " ").slice(0, 120)} »`);
      }
      w.eval(`(${cfg.resoudre})(${n})`);
      await dodo(300);
      const fb = texte(w, `#fb-${n}`);
      ok(fb.includes(n === 1 ? "Résolue" : "premier coup"), `${niveau} salle ${n} : retour de réussite inattendu : « ${fb.slice(0, 100)} »`);
      ok(!cfg.interdits.some(x => fb.includes(x)), `${niveau} salle ${n} : texte de correction après la réussite : « ${fb.slice(0, 100)} »`);
      await dodo(900);
      if (n < 5) {
        ok(/Notez/.test(texte(w, ".zone-enigme")), `${niveau} salle ${n} : « Notez » présent`);
        fragments.push(texte(w, ".mot-cle .val").trim());
        ok(!w.document.querySelector("#salle-contenu .personnage-scene"), `${niveau} salle ${n} : aucun dialogue après la réussite`);
        const b = await attendreQue(() => w.document.getElementById("btn-salle-suivante"), 2500);
        ok(!!b, `${niveau} salle ${n} : bouton salle suivante`);
        clic(w, b); await dodo(500);
      }
    }
    const bc = await attendreQue(() => w.document.getElementById("btn-coffre-final"), 3000);
    ok(!!bc, `${niveau} : bouton du coffre final`);
    clic(w, bc); await dodo(100);
    const champs = [...w.document.querySelectorAll("#coffre-final input")];
    ok(champs.length === 4, `${niveau} : le coffre a ${champs.length} champs (attendu 4)`);
    ok(champs.every(c => !c.value), `${niveau} : coffre vide au départ`);
    champs.forEach((c, i) => c.value = i === 0 ? "FAUX" : fragments[i]);
    clic(w, w.document.getElementById("btn-coffre"));
    ok(/3 mots justes sur 4/.test(texte(w, "#fb-coffre")), `${niveau} : retour du coffre « 3 mots justes sur 4 »`);
    champs[0].value = String(fragments[0]).toLowerCase();
    clic(w, w.document.getElementById("btn-coffre"));
    await attendreQue(() => w.document.getElementById("ecran-fin").classList.contains("actif"), 5000);
    ok(w.document.getElementById("ecran-fin").classList.contains("actif"), `${niveau} : écran de fin`);
    const st = w.eval("({score:ETAT.score, max:SCORE_MAX, pc:ETAT.enigmesPremierCoup, err:ETAT.erreursTotal, coffre:ETAT.coffreOuvert})");
    const attendu = 3 + 4 * 10 + 5 * 5 + 3;
    ok(st.score === attendu, `${niveau} : score ${st.score} (attendu ${attendu})`);
    ok(st.max === 95 && st.pc === 4 && st.err === 2 && st.coffre, `${niveau} : état final ${JSON.stringify(st)}`);
    ok(erreurs.length === 0, `${niveau} : erreurs JS : ` + erreurs.join(" | "));
    console.log(`  ${niveau} : score ${st.score}/${st.max}, fragments ${fragments.join(" · ")}`);
  }

  async function divers(){
    console.log("\n== Vérification, réglages, leçons, impressions ==");
    const { w, erreurs } = await charger(JEU, "?salle=3&niveau=CM1", { attente: 800 });
    ok(w.ETAT.salle === 3 && w.ETAT.niveau === "CM1", "mode vérification salle 3 CM1");
    const cle = w.eval("CLE_SAUVEGARDE");
    ok(!w.localStorage.getItem(cle), "rien de sauvegardé en vérification");
    await w.ouvrirBiblioLecons(); await dodo(50);
    ok(w.document.querySelectorAll("#corps-lecons .carte-lecon, #corps-lecons [data-lecon]").length >= 1, "bibliothèque des leçons");
    w.ouvrirReglages(); await dodo(50);
    ok(w.document.getElementById("overlay-reglages").classList.contains("show"), "réglages ouverts");
    w.document.getElementById("reg-taille").value = "1.3"; w.document.getElementById("reg-calme").classList.add("actif");
    w.sauverReglages();
    ok(w.ETAT.reglages.tailleTexte === 1.3 && w.ETAT.reglages.animationsReduites === true && w.document.body.classList.contains("calme"), "réglages taille et animations");
    await w.chargerEvaluations();
    for (const t of ["prepa", "qcm", "fermees", "docs", "tout"]) {
      await w.imprimerFiches(t); await dodo(30);
      const z = w.document.querySelector(".zone-impression"); const h = z ? z.innerHTML : "";
      ok(h.length > 500 && !/undefined|NaN/.test(h), `impression ${t} (${h.length} car.)`);
    }
    w.imprimerBilan(); await dodo(30);
    ok(!/undefined|NaN/.test(w.document.querySelector(".zone-impression").innerHTML), "bilan imprimé");
    w.imprimerFicheMission(); await dodo(30);
    ok(!/undefined|NaN/.test(w.document.querySelector(".zone-impression").innerHTML), "fiche de mission imprimée");
    ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
    const f = await charger(JEU, "?salle=6&niveau=CM2", { attente: 800 });
    ok(f.w.document.getElementById("ecran-fin").classList.contains("actif"), "vérification : écran de fin (salle=6)");
    ok(f.erreurs.length === 0, "erreurs fin : " + f.erreurs.join(" | "));
    if (fs.existsSync(JEU + "/prof.html")) {
      const p = await charger(JEU, "", { page: "prof.html" });
      ok(p.erreurs.length === 0, "prof.html : erreurs JS : " + p.erreurs.join(" | "));
    }
    await testerLeconsA4(JEU, ok);
  }

  const etapes = (process.argv[2] || "partie,divers").split(",");
  (async () => {
    try {
      if (etapes.includes("partie")) { await partie("CM1"); await partie("CM2"); }
      if (etapes.includes("divers")) await divers();
    } catch (e) { T.exception(e); }
    T.fin();
  })();
}
module.exports = { lancer };
