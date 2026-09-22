/* ============================================================
   TESTS AUTOMATIQUES — L'Atelier de l'inventeur (Node + jsdom)
   ------------------------------------------------------------
   Lancement, depuis la racine du dépôt :
       npm install jsdom          (une seule fois, hors dépôt)
       python3 objets-techniques/tests/test-donnees.py
       node objets-techniques/tests/test-jeu.js
       node objets-techniques/tests/test-verifier.js
   test-jeu.js : parties complètes CM1 et CM2 (scores 100 et 125),
   mots-clés et phrase du coffre-fort, quizz, tests négatifs,
   indices (−2 points), mode vérification, leçons, réglages,
   impressions.
   ============================================================ */
const fs=require("fs"), path=require("path");
const {charger}=require("./charge");
const JEU=path.resolve(__dirname,"..");
const dodo=ms=>new Promise(r=>setTimeout(r,ms));
let echecs=0, oks=0;
const ok=(c,m)=>{ if(c){oks++;} else {echecs++; console.log("  ✗ "+m);} };

/* ---- Résolution d'une énigme par des clics, comme un élève ---- */
async function resoudre(w, e, d){
  const doc=w.document, carte=doc.getElementById("enigme-"+e.id);
  const clic=el=>el.dispatchEvent(new w.MouseEvent("click",{bubbles:true}));
  switch(e.type){
    case "qcm": d.questions.forEach((q,i)=>clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${q.bonne}"]`))); clic(carte.querySelector("[data-valider]")); break;
    case "vraifaux": d.affirmations.forEach((a,i)=>clic(carte.querySelector(`.vf-ligne[data-i="${i}"] [data-rep="${a.vrai?"vrai":"faux"}"]`))); clic(carte.querySelector("[data-valider]")); break;
    case "association": d.paires.forEach((p,i)=>{ clic(carte.querySelector(`[data-col="g"] [data-id="g${i}"]`)); clic(carte.querySelector(`[data-col="d"] [data-id="d${i}"]`)); }); break;
    case "ordre": { const liste=carte.querySelector(".liste-ordre"); const n=d.items.length;
      for(let r=1;r<=n;r++){ let guard=0; while(true){ const items=[...liste.querySelectorAll(".item-ordre")]; const idx=items.findIndex(x=>+x.dataset.rang===r); if(idx===r-1||guard++>20) break; clic(items[idx].querySelector(".btn-monter")); } }
      clic(carte.querySelector("[data-valider]")); break; }
    case "tri": [...carte.querySelectorAll(".carte-tri")].forEach(c=>{ clic(c); clic(carte.querySelector(`.tri-colonne[data-col="${c.dataset.col}"] .tri-zone`)); }); clic(carte.querySelector("[data-valider]")); break;
    case "trous": case "plan": { const sel=e.type==="trous"?".trou":".plan-case";
      [...carte.querySelectorAll(sel)].forEach(t=>{ const et=[...carte.querySelectorAll(".etiquette:not(.posee)")].find(x=>w.normaliser(x.dataset.mot)===w.normaliser(t.dataset.rep)); clic(et); clic(t); });
      clic(carte.querySelector("[data-valider]")); break; }
    case "lettres": { const els=[...carte.querySelectorAll("[data-l]")]; d.cible.forEach(l=>{ const el=els.find(x=>x.dataset.l===l && !x.classList.contains("utilisee")); clic(el); }); break; }
    case "code": d.champs.forEach((c,i)=>{ carte.querySelector("#code-"+i).value=c.valeur.toUpperCase(); }); clic(carte.querySelector("[data-valider]")); break;
    case "intrus": clic(carte.querySelector('[data-intrus="1"]')); break;
  }
  await dodo(20);
  return carte.classList.contains("resolue");
}

/* ---- Une réponse fausse ne doit pas valider ---- */
async function tenterFaux(w, e, d){
  const carte=w.document.getElementById("enigme-"+e.id);
  const clic=el=>el&&el.dispatchEvent(new w.MouseEvent("click",{bubbles:true}));
  if(e.type==="qcm"){ d.questions.forEach((q,i)=>clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${(q.bonne+1)%q.options.length}"]`))); clic(carte.querySelector("[data-valider]")); }
  else if(e.type==="vraifaux"){ d.affirmations.forEach((a,i)=>clic(carte.querySelector(`.vf-ligne[data-i="${i}"] [data-rep="${a.vrai?"faux":"vrai"}"]`))); clic(carte.querySelector("[data-valider]")); }
  else if(e.type==="intrus"){ clic(carte.querySelector('[data-intrus="0"]')); }
  else if(e.type==="code"){ d.champs.forEach((c,i)=>carte.querySelector("#code-"+i).value="xxxx"); clic(carte.querySelector("[data-valider]")); }
  else if(e.type==="association"){ clic(carte.querySelector('[data-col="g"] [data-id="g0"]')); clic(carte.querySelector('[data-col="d"] [data-id="d1"]')); }
  else return null;
  await dodo(20);
  return !carte.classList.contains("resolue");
}

async function partie(niveau){
  console.log(`\n== Partie complète ${niveau} ==`);
  const {w,erreurs}=await charger(JEU);
  const doc=w.document; const ETAT=w.ETAT;
  ETAT.reglages.cinematiques=false; ETAT.reglages.decorsVideo=false;
  doc.querySelector(`.opt-niveau[data-niveau="${niveau}"]`).click();
  const inp=doc.getElementById("input-equipe"); inp.value="Les Testeurs"; inp.dispatchEvent(new w.Event("input"));
  ok(!doc.getElementById("btn-demarrer").disabled, "bouton démarrer actif");
  doc.getElementById("btn-demarrer").click(); await dodo(200);
  const ENIG=JSON.parse(fs.readFileSync(JEU+"/assets/data/enigmes.json","utf8"));
  let negatifs=0;
  for(let s=1;s<=5;s++){
    ok(ETAT.salle===s, `salle courante ${s}`);
    ok(!!doc.querySelector(".scene .decor-fallback svg"), `décor SVG salle ${s}`);
    const liste=w.salleEnigmes(s);
    ok(liste.length===(niveau==="CM1"?3:4), `nb énigmes salle ${s} = ${liste.length}`);
    for(let k=0;k<liste.length;k++){
      const e=liste[k]; const d=w.donneesNiveau(e);
      ok(!!doc.getElementById("enigme-"+e.id), `énigme ${e.id} affichée`);
      ok(!!doc.querySelector(`#enigme-${e.id} [data-fiche="${e.lecon}"]`), `bouton leçon ${e.id}`);
      const nf=await tenterFaux(w,e,d); if(nf!==null){ ok(nf, `mauvaise réponse refusée ${e.id}`); negatifs++; }
      if(e.type==="association"||e.type==="intrus"||e.type==="code"){ // réafficher proprement
        w.afficherEnigmeCourante(); }
      const r=await resoudre(w,e,d); ok(r, `énigme ${e.id} (${e.type}) résolue`);
      await dodo(760);
      if(k<liste.length-1){ const b=doc.getElementById("btn-enigme-suivante"); ok(!!b,"bouton énigme suivante"); b && b.click(); }
    }
    await dodo(1000);
    ok(ETAT.motsCles.length===s, `mot-clé ${s} obtenu (${ETAT.motsCles.join(",")})`);
    if(s<5){ ETAT.salle++; ETAT.enigme=0; w.afficherSalle(ETAT.salle); await dodo(50); }
  }
  await dodo(2200);
  ok(doc.getElementById("ecran-fin").classList.contains("actif"), "écran de fin");
  ok(ETAT.motsCles.join(" ")==="BESOIN FONCTION MATÉRIAU ÉNERGIE NOTICE", "phrase du coffre : "+ETAT.motsCles.join(" "));
  ok(doc.getElementById("fin-contenu").textContent.includes("Un BESOIN, une FONCTION, un MATÉRIAU, une ÉNERGIE, une NOTICE"), "phrase affichée");
  const Q=w.quizzCourant();
  Q.forEach((q,i)=>doc.querySelector(`#quizz .qcm-question[data-i="${i}"] .qcm-option[data-j="${q.bonne}"]`).click());
  doc.getElementById("btn-voir-score").click(); await dodo(50);
  const attendu = niveau==="CM1"?100:125;
  ok(w.scoreMax()===attendu, `score max ${w.scoreMax()} = ${attendu}`);
  ok(ETAT.score===attendu, `score final ${ETAT.score} = ${attendu}`);
  ok(ETAT.enigmesReussies===(niveau==="CM1"?15:20), "énigmes réussies "+ETAT.enigmesReussies);
  ok(negatifs>=5, "tests négatifs "+negatifs);
  ok(erreurs.length===0, "erreurs JS : "+erreurs.join(" | "));
  return w;
}

async function indices(){
  console.log("\n== Indices, vérification, réglages, impressions, leçons ==");
  const {w,erreurs}=await charger(JEU,"?salle=3&niveau=CM1&enigme=2");
  const doc=w.document;
  ok(w.ETAT.equipe==="Vérification" && w.ETAT.salle===3 && w.ETAT.niveau==="CM1", "mode vérification salle 3 CM1");
  ok(!!doc.getElementById("enigme-3-2"), "énigme 3-2 ciblée par &enigme=2");
  w.ETAT.score=20; const avant=w.ETAT.score;
  doc.getElementById("indice-3-2").click();
  ok(w.ETAT.score===avant-2, `indice = moins 2 points (${avant} → ${w.ETAT.score})`);
  doc.getElementById("indice-3-2").click(); doc.getElementById("indice-3-2").click();
  ok(doc.querySelectorAll("#enigme-3-2 .feedback.indice").length===3, "trois indices progressifs");
  ok(!w.localStorage.getItem("escape_objets_techniques_v1") || !JSON.parse(w.localStorage.getItem("escape_objets_techniques_v1")).equipe.includes("Vérification") , "rien de sauvegardé en vérification");
  // leçons
  await w.ouvrirBiblioLecons();
  ok(doc.querySelectorAll("#corps-lecons .carte-lecon").length===5, "5 leçons dans la bibliothèque");
  w.afficherLecon("materiaux");
  const txt=doc.getElementById("corps-lecons").textContent;
  ok(txt.includes("Lexique") && txt.includes("Sources") && !!doc.querySelector("#corps-lecons svg"), "leçon : lexique, schéma, sources");
  // réglages
  w.ouvrirReglages(); await dodo(50);
  ok(doc.getElementById("overlay-reglages").classList.contains("show"), "réglages ouverts");
  doc.getElementById("reg-taille").value="1.3"; doc.getElementById("reg-calme").classList.add("actif");
  w.sauverReglages();
  ok(w.ETAT.reglages.tailleTexte===1.3 && w.ETAT.reglages.animationsReduites===true, "réglages taille et animations");
  ok(doc.body.classList.contains("calme"), "classe calme appliquée");
  // impressions
  await w.chargerEvaluations();
  for(const t of ["prepa","qcm","fermees","docs","tout"]){
    await w.imprimerFiches(t); await dodo(30);
    const z=doc.querySelector(".zone-impression"); const h=z?z.innerHTML:"";
    ok(h.length>500 && !/undefined|NaN/.test(h), `impression ${t} (${h.length} car.)`);
  }
  w.imprimerBilan(); await dodo(30);
  ok(!/undefined|NaN/.test(doc.querySelector(".zone-impression").innerHTML), "bilan imprimé");
  ok(erreurs.length===0, "erreurs JS : "+erreurs.join(" | "));
  // écran de fin direct
  const f=await charger(JEU,"?salle=6&niveau=CM2"); await dodo(300);
  ok(f.w.document.getElementById("ecran-fin").classList.contains("actif"), "vérification : écran de fin (salle=6)");
  ok(f.erreurs.length===0, "erreurs fin : "+f.erreurs.join(" | "));
}

(async()=>{
  await partie("CM1"); await partie("CM2"); await indices();
  console.log(`\n${oks} vérifications réussies, ${echecs} échec(s).`);
  process.exit(echecs?1:0);
})();
