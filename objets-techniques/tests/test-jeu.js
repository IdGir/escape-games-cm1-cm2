/* ============================================================
   TESTS AUTOMATIQUES — L'Atelier de l'inventeur (Node + jsdom)
   ------------------------------------------------------------
   Lancement, depuis la racine du dépôt :
       npm install jsdom          (une seule fois, hors dépôt)
       python3 objets-techniques/tests/test-donnees.py
       node objets-techniques/tests/test-jeu.js
       node objets-techniques/tests/test-verifier.js
   Moteur d'énigmes v2 (outils-moteur/enigmes.js) : chaque énigme se
   valide par un bouton « Vérifier » ; une erreur n'indique que le
   NOMBRE de réponses justes, sans marquer bien/mal ; aucune
   correction après la réussite ; 10 points du premier coup, 3 après
   erreur ; coffre final où l'on retape les 5 mots-clés.
   test-jeu.js : partie CM1 sans faute (185 points = scoreMax()),
   partie CM2 avec une erreur et un coffre raté (235 − 7 − 7),
   mots-clés « Notez ce mot », coffre final (vide, refuse un mot
   faux, s'ouvre avec les bons mots), phrase du coffre-fort, quizz ;
   pour chaque type d'énigme : erreur « N … sur M », puis 3 points ;
   indices (−2 points), mode vérification, leçons, réglages,
   impressions.
   ============================================================ */
const fs=require("fs"), path=require("path");
const {charger}=require("./charge");
const JEU=path.resolve(__dirname,"..");
const ENIG=JSON.parse(fs.readFileSync(JEU+"/assets/data/enigmes.json","utf8"));
const dodo=ms=>new Promise(r=>setTimeout(r,ms));
let echecs=0, oks=0;
const ok=(c,m)=>{ if(c){oks++;} else {echecs++; console.log("  ✗ "+m);} };
async function attendreQue(fn, max=6000){ const t0=Date.now(); while(Date.now()-t0<max){ const r=fn(); if(r) return r; await dodo(40); } return null; }

/* ---- Résolution d'une énigme par des clics, comme un élève ----
   Calquée sur le solveur de outils-moteur/tester_parties.py : chaque type
   se valide par [data-valider]. Avec faux=true, la réponse contient
   volontairement une erreur (une seule pièce mal placée). */
async function resoudre(w, e, d, faux=false){
  const doc=w.document, carte=doc.getElementById("enigme-"+e.id), N=w.normaliser;
  const clic=el=>el.dispatchEvent(new w.MouseEvent("click",{bubbles:true}));
  // remise à zéro d'une tentative précédente (comme le ferait un élève)
  carte.querySelectorAll(".slots-lettres .slot.ok").forEach(clic);
  carte.querySelectorAll(".trou[data-pose], .plan-case[data-pose]").forEach(clic);
  switch(e.type){
    case "qcm": d.questions.forEach((q,i)=>clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${faux&&i===0?(q.bonne+1)%q.options.length:q.bonne}"]`))); break;
    case "vraifaux": d.affirmations.forEach((a,i)=>clic(carte.querySelector(`.vf-ligne[data-i="${i}"] [data-rep="${(faux&&i===0?!a.vrai:!!a.vrai)?"vrai":"faux"}"]`))); break;
    case "association": { // appariement gauche → droite (numéros de paire), puis Vérifier
      const g=[...carte.querySelectorAll('[data-col="g"] .carte-match')];
      g.forEach((c,i)=>{ clic(c); clic(carte.querySelector(`[data-col="d"] [data-id="${faux&&g.length>1?g[(i+1)%g.length].dataset.bon:c.dataset.bon}"]`)); }); break; }
    case "ordre": { const liste=carte.querySelector(".liste-ordre"); const n=d.items.length;
      for(let r=1;r<=n;r++){ let guard=0; while(true){ const items=[...liste.querySelectorAll(".item-ordre")]; const idx=items.findIndex(x=>+x.dataset.rang===r); if(idx===r-1||guard++>20) break; clic(items[idx].querySelector(".btn-monter")); } }
      if(faux) clic(liste.children[0].querySelector(".btn-descendre"));
      break; }
    case "tri": { // clic sur une carte, puis sur une colonne
      const cols=[...carte.querySelectorAll(".tri-colonne")];
      [...carte.querySelectorAll(".carte-tri")].forEach((c,i)=>{ let col=c.dataset.col; if(faux&&i===0) col=(cols.find(k=>k.dataset.col!==col)||cols[0]).dataset.col;
        clic(c); clic(carte.querySelector(`.tri-colonne[data-col="${col}"] .tri-zone`)); }); break; }
    case "trous": case "plan": { const cibles=[...carte.querySelectorAll(e.type==="trous"?".trou":".plan-case")];
      const reps=cibles.map(t=>t.dataset.rep); if(faux&&reps.length>1) [reps[0],reps[1]]=[reps[1],reps[0]];
      cibles.forEach((t,i)=>{ const et=[...carte.querySelectorAll(".etiquette:not(.posee)")].find(x=>N(x.dataset.mot)===N(reps[i])); clic(et); clic(t); }); break; }
    case "lettres": { // anagramme : les lettres [data-l] remplissent les cases (des leurres existent)
      let cible=d.cible.slice();
      if(faux){ [cible[0],cible[cible.length-1]]=[cible[cible.length-1],cible[0]]; if(N(cible.join(""))===N(d.cible.join(""))) cible.reverse(); }
      cible.forEach(l=>clic([...carte.querySelectorAll("[data-l]:not(.utilisee)")].find(x=>N(x.dataset.l)===N(l)))); break; }
    case "code": d.champs.forEach((c,i)=>{ carte.querySelector("#code-"+i).value=faux&&i===0?"xxxx":c.valeur.toUpperCase(); }); break;
    case "intrus": clic(carte.querySelector(`[data-intrus="${faux?0:1}"]`)); break;   // sélection, puis « C'est l'intrus ! »
  }
  clic(carte.querySelector("[data-valider]"));
  await dodo(20);
  return carte.classList.contains("resolue");
}

/* Débuts des textes de correction / explication, hors phrases déjà présentes dans l'énoncé. */
const sansBalises=s=>String(s||"").replace(/<[^>]*>/g," ").replace(/\s+/g," ").trim();
function textesCorrection(e){
  const t=[];
  const parcourir=o=>{ if(o&&typeof o==="object") Object.entries(o).forEach(([k,v])=>{
    if(/^(correction|explication)$/.test(k)) [].concat(typeof v==="object"&&v?Object.values(v):v).forEach(x=>typeof x==="string"&&t.push(sansBalises(x)));
    else parcourir(v); }); };
  parcourir(e);
  const enonce=sansBalises(JSON.stringify(e,(k,v)=>/^(correction|explication)$/.test(k)?undefined:v));
  return t.filter(x=>x.length>=12).map(x=>x.slice(0,40)).filter(x=>!enonce.includes(x));
}
/* Après une vérification fausse : seul le NOMBRE de réponses justes est donné. */
function controlerErreur(w, e, etiquette){
  const carte=w.document.getElementById("enigme-"+e.id), fb=w.document.getElementById("fb-"+e.id).textContent;
  ok(!carte.classList.contains("resolue"), `${etiquette} (${e.type}) : mauvaise réponse refusée`);
  ok(/Pas tout juste/.test(fb) && (e.type==="intrus" ? /Ce n'est pas l'intrus/.test(fb) : /\b\d+ [^.]+ sur \d+\./.test(fb)), `${etiquette} (${e.type}) : message « N … sur M » attendu, obtenu « ${fb.replace(/\s+/g," ").slice(0,90)} »`);
  ok(!carte.querySelector(".bien, .mal, .correct, .incorrect"), `${etiquette} (${e.type}) : des éléments sont marqués bien/mal`);
}
/* Après la réussite : les points, et aucune correction, explication ni source. */
function controlerReussite(w, e, pts, etiquette){
  const carte=w.document.getElementById("enigme-"+e.id), fb=w.document.getElementById("fb-"+e.id).textContent;
  ok(fb.includes("+"+pts+" points") && (pts===10)===/Tout juste du premier coup/.test(fb), `${etiquette} : « +${pts} points » attendu, obtenu « ${fb.slice(0,80)} »`);
  const copie=carte.cloneNode(true); copie.querySelectorAll(".barre-outils, .consigne").forEach(x=>x.remove());   // la source figure dès le début dans la barre d'outils
  const txt=copie.textContent.replace(/\s+/g," "), fuite=textesCorrection(e).find(x=>txt.includes(x));
  ok(!carte.querySelector(".correction, .source-correction, .explication") && !fuite && !(e.source&&fb.includes(e.source)), `${etiquette} : aucune correction affichée après la réussite`+(fuite?" (trouvé : « "+fuite+" »)":""));
}
const bareme=w=>w.eval("({premier:PTS_PREMIER_COUP, apres:PTS_APRES_ERREUR, rapidite:PTS_RAPIDITE, quiz:PTS_QUIZ, nbQuiz:NB_QUIZ, malus:MALUS_INDICE, coffre:PTS_COFFRE_PREMIER, coffreApres:PTS_COFFRE_APRES})");

/* ---- Partie complète ----
   avecErreurs : la première énigme et le coffre sont d'abord ratés. */
async function partie(niveau, avecErreurs){
  console.log(`\n== Partie complète ${niveau}${avecErreurs?" (une erreur, un coffre raté)":""} ==`);
  const {w,erreurs}=await charger(JEU);
  const doc=w.document; const ETAT=w.ETAT, B=bareme(w), DONNEES=w.eval("DONNEES");
  ETAT.reglages.cinematiques=false; ETAT.reglages.decorsVideo=false;
  doc.querySelector(`.opt-niveau[data-niveau="${niveau}"]`).click();
  const inp=doc.getElementById("input-equipe"); inp.value="Les Testeurs"; inp.dispatchEvent(new w.Event("input"));
  ok(!doc.getElementById("btn-demarrer").disabled, "bouton démarrer actif");
  doc.getElementById("btn-demarrer").click(); await dodo(200);
  let total=0;
  for(let s=1;s<=5;s++){
    ok(ETAT.salle===s, `salle courante ${s}`);
    ok(!!doc.querySelector(".scene .decor-fallback svg"), `décor SVG salle ${s}`);
    const liste=w.salleEnigmes(s);
    ok(liste.length===(niveau==="CM1"?3:4), `nb énigmes salle ${s} = ${liste.length}`);
    for(let k=0;k<liste.length;k++){
      const e=liste[k]; const d=w.donneesNiveau(e);
      ok(!!doc.getElementById("enigme-"+e.id), `énigme ${e.id} affichée`);
      ok(!!doc.querySelector(`#enigme-${e.id} [data-fiche="${e.lecon}"]`), `bouton leçon ${e.id}`);
      const avant=ETAT.score, premiere=avecErreurs&&total===0;
      if(premiere){ await resoudre(w,e,d,true); controlerErreur(w,e,e.id); }
      const r=await resoudre(w,e,d); ok(r, `énigme ${e.id} (${e.type}) résolue`);
      const pts=premiere?B.apres:B.premier;
      controlerReussite(w,e,pts,e.id);
      total++;
      if(k<liste.length-1){
        const b=await attendreQue(()=>doc.getElementById("btn-enigme-suivante")); ok(!!b,"bouton énigme suivante après "+e.id);
        ok(ETAT.score-avant===pts, `${e.id} : +${pts} points au score (obtenu ${ETAT.score-avant})`);
        b && b.click();
      }
    }
    // fin de salle : plus de dialogue de réussite, le bouton suivant apparaît tout de suite
    const id=s<5?"btn-salle-suivante":"btn-coffre-final";
    const b=await attendreQue(()=>doc.getElementById(id), 2500);
    ok(!!b, `salle ${s} : bouton ${id} tout de suite`);
    ok(ETAT.motsCles.length===s, `mot-clé ${s} obtenu (${ETAT.motsCles.join(",")})`);
    const zone=doc.getElementById("zone-enigme").textContent;
    ok(zone.includes(DONNEES.salles[s-1].motCle) && /Notez ce mot/.test(zone), `salle ${s} : mot ${DONNEES.salles[s-1].motCle} affiché avec « Notez ce mot »`);
    if(!b) return w;
    b.click(); await dodo(60);
    ok(!doc.querySelector(".mot-cle"), `salle ${s} : le mot n'est plus affiché ensuite`);
  }
  // coffre final : les 5 mots sont à retaper, rien n'est prérempli
  const coffre=await attendreQue(()=>doc.getElementById("coffre-final"));
  ok(!!coffre, "coffre final affiché");
  if(!coffre) return w;
  const champs=DONNEES.salles.map((x,i)=>doc.getElementById("coffre-"+i));
  ok(champs.every(c=>c&&c.value===""), "coffre final : les 5 champs sont vides");
  ok(!DONNEES.salles.some(x=>coffre.textContent.includes(x.motCle)), "coffre final : aucun mot-clé affiché");
  if(avecErreurs){
    champs.forEach((c,i)=>c.value=i===4?"mode d'emploi":DONNEES.salles[i].motCle);
    doc.getElementById("btn-coffre").click();
    ok(!ETAT.coffreOuvert && /4 mots justes sur 5/.test(doc.getElementById("fb-coffre").textContent), "coffre final : un mot faux est refusé (« 4 mots justes sur 5 »)");
  }
  const avantCoffre=ETAT.score;
  champs.forEach((c,i)=>c.value=w.normaliser(DONNEES.salles[i].motCle));   // minuscules, sans accent (MATÉRIAU → materiau)
  doc.getElementById("btn-coffre").click();
  ok(ETAT.coffreOuvert, "coffre final : s'ouvre avec les bons mots (accents et casse ignorés)");
  ok(ETAT.score-avantCoffre===(avecErreurs?B.coffreApres:B.coffre), `coffre final : +${avecErreurs?B.coffreApres:B.coffre} points`);
  await attendreQue(()=>doc.getElementById("ecran-fin").classList.contains("actif"), 5000);
  ok(doc.getElementById("ecran-fin").classList.contains("actif"), "écran de fin");
  ok(ETAT.motsCles.join(" ")==="BESOIN FONCTION MATÉRIAU ÉNERGIE NOTICE", "phrase du coffre : "+ETAT.motsCles.join(" "));
  ok(doc.getElementById("fin-contenu").textContent.includes("Un BESOIN, une FONCTION, un MATÉRIAU, une ÉNERGIE, une NOTICE"), "phrase affichée");
  const Q=w.quizzCourant();
  Q.forEach((q,i)=>doc.querySelector(`#quizz .qcm-question[data-i="${i}"] .qcm-option[data-j="${q.bonne}"]`).click());
  doc.getElementById("btn-voir-score").click(); await dodo(50);
  // barème v2 : énigmes × 10 + coffre 10 + 5 salles × 3 (rapidité) + quizz 5 × 2
  const max=total*B.premier+B.coffre+5*B.rapidite+B.nbQuiz*B.quiz;
  ok(w.scoreMax()===max && max===(niveau==="CM1"?185:235), `score max ${w.scoreMax()} = ${max}`);
  const attendu=max-(avecErreurs?(B.premier-B.apres)+(B.coffre-B.coffreApres):0);
  ok(ETAT.score===attendu, `score final ${ETAT.score} = ${attendu}`);
  ok(ETAT.enigmesReussies===(niveau==="CM1"?15:20), "énigmes réussies "+ETAT.enigmesReussies);
  ok(ETAT.enigmesPremierCoup===total-(avecErreurs?1:0) && ETAT.erreursTotal===(avecErreurs?2:0) && ETAT.coffrePremierCoup===!avecErreurs,
     `bilan : ${ETAT.enigmesPremierCoup} du premier coup, ${ETAT.erreursTotal} erreur(s), coffre du premier coup : ${ETAT.coffrePremierCoup}`);
  ok(erreurs.length===0, "erreurs JS : "+erreurs.join(" | "));
  return w;
}

/* ---- Chaque type d'énigme (mode vérification) : réponse incomplète, fausse, puis juste ---- */
async function types(){
  console.log("\n== Chaque type : erreur « N … sur M », puis 3 points ==");
  const vus=new Set(); let negatifs=0;
  for(const s of ENIG.salles){
    const liste=s.enigmes.filter(e=>!e.niveaux||e.niveaux.includes("CM2"));
    for(let k=0;k<liste.length;k++){
      const e=liste[k]; if(vus.has(e.type)) continue; vus.add(e.type);
      const {w,erreurs}=await charger(JEU,`?salle=${s.num}&niveau=CM2&enigme=${k+1}`);
      const carte=w.document.getElementById("enigme-"+e.id);
      if(!carte){ ok(false, "accès direct à "+e.id); continue; }
      const B=bareme(w), d=w.donneesNiveau(e);
      if(e.type!=="ordre"){   // l'ordre se valide toujours (pas d'état incomplet)
        carte.querySelector("[data-valider]").click();
        ok(!carte.classList.contains("resolue") && w.ETAT.erreursTotal===0, `${e.id} (${e.type}) : une réponse incomplète n'est pas comptée comme erreur`);
      }
      const errAvant=w.ETAT.erreursTotal;
      await resoudre(w,e,d,true); controlerErreur(w,e,e.id); negatifs++;
      ok(w.ETAT.erreursTotal===errAvant+1, `${e.id} (${e.type}) : une erreur comptée`);
      ok(await resoudre(w,e,d), `${e.id} (${e.type}) résolue après l'erreur`);
      controlerReussite(w,e,B.apres,e.id);
      await dodo(600);
      ok(w.ETAT.score===B.apres, `${e.id} (${e.type}) : ${B.apres} points après une erreur (score ${w.ETAT.score})`);
      ok(erreurs.length===0, `${e.id} : erreurs JS : `+erreurs.join(" | "));
    }
  }
  ok(vus.size===10 && negatifs===10, `${vus.size} types testés, ${negatifs} réponses fausses refusées`);
}

async function indices(){
  console.log("\n== Indices, vérification, réglages, impressions, leçons ==");
  const {w,erreurs}=await charger(JEU,"?salle=3&niveau=CM1&enigme=2");
  const doc=w.document;
  ok(w.ETAT.equipe==="Vérification" && w.ETAT.salle===3 && w.ETAT.niveau==="CM1", "mode vérification salle 3 CM1");
  ok(!!doc.getElementById("enigme-3-2"), "énigme 3-2 ciblée par &enigme=2");
  ok(/10 points/.test(doc.querySelector("#enigme-3-2 .bandeau-bareme").textContent) && /3 points/.test(doc.querySelector("#enigme-3-2 .bandeau-bareme").textContent), "bandeau du barème : 10 / 3 points");
  w.ETAT.score=20; const avant=w.ETAT.score;
  doc.getElementById("indice-3-2").click();
  ok(w.ETAT.score===avant-2, `indice = moins 2 points (${avant} → ${w.ETAT.score})`);
  doc.getElementById("indice-3-2").click(); doc.getElementById("indice-3-2").click();
  ok(doc.querySelectorAll("#enigme-3-2 .feedback.indice").length===3, "trois indices progressifs");
  // les indices ne retirent pas le bonus du premier coup
  const e32=ENIG.salles[2].enigmes[1]; const s0=w.ETAT.score;
  ok(await resoudre(w,e32,w.donneesNiveau(e32)), "3-2 résolue après trois indices");
  controlerReussite(w,e32,10,"3-2 après indices");
  await dodo(600);
  ok(w.ETAT.score===s0+10, `3-2 : +10 du premier coup malgré les indices (${s0} → ${w.ETAT.score})`);
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
  try{ await partie("CM1", false); await partie("CM2", true); await types(); await indices(); }
  catch(e){ echecs++; console.log("  ✗ EXCEPTION "+e.stack); }
  console.log(`\n${oks} vérifications réussies, ${echecs} échec(s).`);
  process.exit(echecs?1:0);
})();
