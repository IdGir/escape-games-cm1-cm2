/* ============================================================
   TESTS AUTOMATIQUES — Mission géographique (Node + jsdom)
   Depuis la racine du dépôt :  node mission-geo/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md)
   Étapes au choix :  node mission-geo/tests/test-jeu.js seances,final  (ou CM1, CM2, DEC)
   Reprise en jsdom de outils-moteur/tester_mission_geo.py : pour chaque
   séance (?seance=N), chaque énigme est résolue avec la correction du
   moteur. Séance 1, énigme 1 : d'abord une vérification vide (fausse),
   dont le retour ne doit donner que le NOMBRE de bonnes réponses.
   Contrôles : barème 10 / 3, dénouement sans texte, indice à recopier,
   piste finale sans valeurs recopiées, fiche de mission (16 séances).
   ============================================================ */
const path = require("path");
const { charger, compteur, dodo, attendreQue, testerLeconsA4 } = require("../../outils-tests/charge");
const JEU = path.resolve(__dirname, "..");
const T = compteur("Mission géographique"); const ok = T.ok;
const clic = (w, el) => el && el.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
const txt = el => el ? el.textContent.replace(/\s+/g, " ") : "";

async function seance(n, niveau = "CM2"){
  const { w, erreurs } = await charger(JEU, `?seance=${n}&niveau=${niveau}`, { attente: 700 });
  const doc = w.document;
  w.eval("(() => { const o = ACTIVITES.rendre; ACTIVITES.rendre = (a, h, x) => { const r = o(a, h, x); window.__m = r.moteur; return r; }; })()");
  const nb = w.eval("APP.courant.s.activites.length");
  const D = w.eval("MISSION.DIFFERENCIATION")["s" + String(n).padStart(2, "0")] || {};
  const livret = w.eval(`MISSION.parId("s${String(n).padStart(2, "0")}").activites.length`);
  ok(nb === livret + (niveau === "CM2" ? (D.plusCM2 || []).length : 0), `séance ${n} ${niveau} : ${nb} énigmes (livret ${livret}${niveau === "CM2" ? " + pour aller plus loin" : ""})`);
  if (niveau !== "CM2") for (const k of Object.keys(D.cm1 || {})) {
    const a = w.eval(`APP.courant.s.activites[${k - 1}]`), r = D.cm1[k];
    ok(Object.keys(r).every(c => JSON.stringify(a[c]) === JSON.stringify(r[c]) || (niveau === "DEC" && c === "precision")), `séance ${n} ${niveau} : activité ${k} en version guidée`);
  }
  ok(/10 points/.test(txt(doc.getElementById("session-scene"))), `séance ${n} : barème dans l'introduction`);
  const go = [...doc.querySelectorAll("#session-scene button")].find(b => /Commencer la mission/.test(b.textContent));
  ok(!!go, `séance ${n} : bouton « Commencer la mission »`);
  clic(w, go); await dodo(50);
  let attendu = 0;
  const valider = () => clic(w, doc.querySelector(".activite .barre-actions .bouton-principal"));
  for (let k = 0; k < nb; k++) {
    ok(await attendreQue(() => doc.querySelector(".activite"), 4000), `séance ${n} énigme ${k + 1} affichée`);
    if (niveau === "DEC") {
      const a = w.eval(`APP.courant.s.activites[${k}]`);
      if (a.aide) ok(doc.querySelector(".activite .precision") && doc.querySelector(".activite .precision").textContent.includes(a.aide) && [...doc.querySelectorAll(".activite .barre-actions button")].find(b => /Coup de pouce/.test(b.textContent)).hidden, `séance ${n} DEC énigme ${k + 1} : coup de pouce affiché d'emblée, bouton masqué`);
    }
    if (n === 1 && k === 0) {
      valider(); await dodo(30);
      const fb = txt(doc.querySelector(".activite .retour"));
      ok(!doc.querySelector(".activite .corps .bon, .activite .corps .faux, .activite .corps .mauvais"), "séance 1 : aucune réponse marquée juste/fausse après une erreur");
      const erreur = /Pas tout juste/.test(fb);
      ok(erreur || /✋/.test(fb), `séance 1 : retour d'erreur inattendu « ${fb.slice(0, 90)} »`);
      attendu += erreur ? 3 : 10;
    } else attendu += 10;
    w.eval("window.__m.corriger()");
    valider(); await dodo(30);
    let fb = txt(doc.querySelector(".activite .retour"));
    if (/✋/.test(fb)) {   // répartition libre (sans solution) : on place tous les jetons
      w.eval(`(() => { const plus = [...document.querySelectorAll('.activite .poste .boutons button:last-child')];
        for(let k = 0; k < 500 && !document.querySelector('.reste-a-placer.ok'); k++) plus[k % plus.length].click(); })()`);
      valider(); await dodo(30);
      fb = txt(doc.querySelector(".activite .retour"));
    }
    ok(/points/.test(fb) && /premier coup|Résolue|enregistrée/.test(fb), `séance ${n} énigme ${k + 1} : retour de réussite inattendu « ${fb.slice(0, 90)} »`);
    clic(w, doc.querySelector("#session-scene .pied-scene .bouton-principal")); await dodo(30);
  }
  await dodo(300);
  const scene = txt(doc.getElementById("session-scene"));
  const pts = w.eval("APP.courant ? APP.courant.points : -1");
  ok(pts === attendu, `séance ${n} : ${pts} points (attendu ${attendu})`);
  ok(/Recopie cet indice/.test(scene), `séance ${n} : consigne « Recopie cet indice »`);
  ok(!doc.querySelector("#session-scene .narration, #session-scene .lecon, #session-scene .a-retenir"), `séance ${n} : aucun texte (récit ou leçon) après la résolution`);
  ok(erreurs.length === 0, `séance ${n} : erreurs JS : ` + erreurs.join(" | "));
  console.log(`  séance ${String(n).padStart(2)} ${niveau} : ${nb} énigmes, ${pts}/${nb * 10} points`);
}

async function final(){
  console.log("\n== Piste finale, fiche de mission, leçons A4 ==");
  const { w, erreurs } = await charger(JEU, "?seance=final", { attente: 800 });
  const doc = w.document;
  const t = txt(doc.getElementById("final-scene"));
  ok(!(t.includes("→") && t.includes("?")), "piste finale : les valeurs des indices ne sont pas recopiées automatiquement");
  w.eval("REGLAGES.ouvrir()"); await dodo(300);
  const b = doc.getElementById("r-imp-mission");
  ok(!!b, "réglages : bouton fiche de mission");
  clic(w, b); await dodo(600);
  const lignes = doc.querySelectorAll(".table-fiche-mission tr").length;
  ok(lignes === 17 && (w.__imprime || 0) > 0, `fiche de mission : ${lignes} lignes (attendu 17), impression lancée`);
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  await testerLeconsA4(JEU, ok);
  // Accueil : le choix « Découverte » est enregistré (contenu CM1 + palier)
  const a = await charger(JEU, "", { attente: 600 });
  a.w.document.getElementById("champ-equipe").value = "Les Pousses";
  a.w.document.querySelector('input[name="niveau"][value="DEC"]').checked = true;
  a.w.document.getElementById("form-depart").dispatchEvent(new a.w.Event("submit", { cancelable: true }));
  const et = a.w.eval("SAUVEGARDE.lire()");
  ok(et.niveau === "CM1" && et.palier === "decouverte" && a.w.eval("APP.niveauCourant()") === "DEC", "accueil : Découverte = niveau CM1 + palier « decouverte »");
  ok(a.erreurs.length === 0, "accueil : erreurs JS : " + a.erreurs.join(" | "));
}

const etapes = (process.argv[2] || "seances,final").split(",");
(async () => {
  try {
    for (const niveau of ["CM2", "CM1", "DEC"]) if (etapes.includes("seances") || etapes.includes(niveau)) {
      console.log(`\n== Les 16 séances, niveau ${niveau} ==`); for (let n = 1; n <= 16; n++) await seance(n, niveau);
    }
    if (etapes.includes("final")) await final();
  } catch (e) { T.exception(e); }
  T.fin();
})();
