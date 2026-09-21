/* ============================================================
   APP — Moteur principal du jeu « Le Manuscrit de l'abbaye »
   Coordonne : écrans, salles, décors, dialogues, énigmes,
               pages du livre, fermoir final, score, minuteur,
               leçons, réglages
   ------------------------------------------------------------
   Les énigmes ne sont PAS écrites ici : elles sont décrites dans
   assets/data/enigmes.json et rendues par js/enigmes.js.
   ============================================================ */

const NB_SALLES = 5;

const ETAT = {
  equipe: "",
  niveau: "CM2",
  salle: 1,
  enigme: 0,                 // index de l'énigme en cours dans la salle
  score: 0,
  motsCles: [],              // mots-clés des pages déjà refaites
  badges: {vitesse:false, copiste:false, charite:false, maitre:false},
  debut: null,
  msEcoules: 0,
  enPause: false,
  tempsParSalle: {},
  salleDebut: null,
  indicesSalle: 0,
  indicesTotal: 0,
  enigmesReussies: 0,
  quiz: {repondu:false, score:0},
  fini: false,
  reglages: {
    narrationActive: true,
    volume: 1,
    tailleTexte: 1,
    dureeMin: 60,
    leconsAutorisees: true,
    apiActive: false,
    sonsActifs: true,
    volumeSons: 0.55,
    animationsReduites: false,
    decorsVideo: true,
    sonVideo: false,
    cinematiques: true,
  }
};

const PTS_ENIGME   = 5;    // par énigme résolue
const PTS_RAPIDITE = 3;    // bonus par salle bouclée rapidement
const PTS_QUIZ     = 2;    // par bonne réponse au quizz final
const NB_QUIZ      = 5;
const MALUS_INDICE = 2;    // retiré du score à chaque indice consulté

/** Nombre d'énigmes du niveau courant (15 en CM1, 20 en CM2). */
function nbEnigmesTotal(){
  if(!ENIGMES) return 0;
  return ENIGMES.salles.reduce((t,s)=>t + enigmesDe(s).length, 0);
}
/** Énigmes d'une salle filtrées selon le niveau. */
function enigmesDe(salle){
  const n = ETAT.niveau || "CM2";
  return (salle.enigmes||[]).filter(e=>!e.niveaux || e.niveaux.includes(n));
}
/** Score maximal atteignable, pour le barème affiché et imprimé. */
function scoreMax(){
  return nbEnigmesTotal()*PTS_ENIGME + NB_SALLES*PTS_RAPIDITE + NB_QUIZ*PTS_QUIZ;
}

const CLE_SAUVEGARDE = "escape_moyenage_v1";
const VERSION_APP = "v1";
let DONNEES = null;   // dialogues.json
let ENIGMES = null;   // enigmes.json

function resetEtatJeu(){
  Object.assign(ETAT, {
    equipe:"", niveau:"CM2", salle:1, enigme:0, score:0, motsCles:[],
    badges:{vitesse:false, copiste:false, charite:false, maitre:false},
    debut:null, msEcoules:0, enPause:false, tempsParSalle:{}, salleDebut:null,
    indicesSalle:0, indicesTotal:0, enigmesReussies:0,
    quiz:{repondu:false, score:0}, fini:false, fermoir:false
  });
}

/* ============================================================
   CHARGEMENT DES DONNÉES
   Robuste : si fetch échoue (ouverture en file://), on bascule
   sur les données embarquées.
   ============================================================ */
async function chargerJSON(chemin){
  try{
    const r = await fetch(chemin, {cache:"no-store"});
    if(r.ok) return await r.json();
  }catch(e){
    console.warn("Fetch impossible ("+chemin+") — mode file:// ? Bascule sur les données embarquées.");
  }
  return null;
}

async function chargerDonnees(){
  // Les évaluations alimentent aussi le quizz final : on les charge dès le départ.
  if(typeof chargerEvaluations === "function") chargerEvaluations();
  DONNEES  = await chargerJSON("assets/data/dialogues.json");
  ENIGMES  = await chargerJSON("assets/data/enigmes.json");
  if(!DONNEES || !DONNEES.salles) DONNEES = JSON.parse(JSON.stringify(DONNEES_FALLBACK));
  if(!ENIGMES || !ENIGMES.salles){
    ENIGMES = JSON.parse(JSON.stringify(ENIGMES_FALLBACK));
    console.warn("enigmes.json introuvable : jeu réduit aux énigmes de secours. "
      + "Lancez le jeu via lancer.bat ou en ligne pour disposer des 20 énigmes.");
  }
  try{
    const r = localStorage.getItem("escape_reglages_moyenage");
    if(r) Object.assign(ETAT.reglages, JSON.parse(r));
  }catch(e){}
  appliquerReglages();
}

/* ---- Données de secours minimales (file:// sans serveur) ---- */
const DONNEES_FALLBACK = {
  personnages: {
    anselme:{nom:"Frère Anselme", emoji:"🕯️"},
    aude:{nom:"Aude", emoji:"🖋️"},
    alix:{nom:"Mère Alix", emoji:"🕊️"},
    garin:{nom:"Garin", emoji:"⛏️"}
  },
  incipit:"Au temps des FRANCS et de l'EMPIRE, la PLUME, la CHARITÉ et la PIERRE ont gardé la mémoire des hommes.",
  salles:[
    {num:1, titre:"Le baptême de Clovis", decor:"reims", motCle:"FRANCS",
     lieu:"⛪ Reims — la première page", description:"Un roi agenouillé devant un évêque, près d'une cuve d'eau.",
     dialogue_intro:{perso:"anselme", nom:"Frère Anselme", texte:"Cinq pages du livre ont disparu. Refaisons la première : Clovis, roi des Francs."},
     dialogue_reussite:{perso:"anselme", nom:"Frère Anselme", texte:"Première page refaite."}},
    {num:2, titre:"La cour de Charlemagne", decor:"aix", motCle:"EMPIRE",
     lieu:"👑 Aix-la-Chapelle — la deuxième page", description:"Un empereur et les élèves de son école.",
     dialogue_intro:{perso:"aude", nom:"Aude", texte:"Charlemagne est couronné empereur à Rome en l'an 800."},
     dialogue_reussite:{perso:"aude", nom:"Aude", texte:"Deuxième page refaite."}},
    {num:3, titre:"Le scriptorium de l'abbaye", decor:"scriptorium", motCle:"PLUME",
     lieu:"🕯️ Le scriptorium — la troisième page", description:"Des pupitres alignés sous les fenêtres.",
     dialogue_intro:{perso:"anselme", nom:"Frère Anselme", texte:"Ici, on copie les livres à la main, et on enseigne."},
     dialogue_reussite:{perso:"anselme", nom:"Frère Anselme", texte:"Troisième page refaite."}},
    {num:4, titre:"L'hôtel-Dieu et l'aumône", decor:"hoteldieu", motCle:"CHARITÉ",
     lieu:"🕊️ L'hôtel-Dieu — la quatrième page", description:"Une longue salle de lits, une chapelle au fond.",
     dialogue_intro:{perso:"alix", nom:"Mère Alix", texte:"Ici, on accueille gratuitement les malades pauvres."},
     dialogue_reussite:{perso:"alix", nom:"Mère Alix", texte:"Quatrième page refaite."}},
    {num:5, titre:"L'église romane et la cathédrale gothique", decor:"chantier", motCle:"PIERRE",
     lieu:"⛏️ Le chantier — la cinquième page", description:"Une église romane et une cathédrale gothique.",
     dialogue_intro:{perso:"garin", nom:"Garin", texte:"Voûte en berceau ou croisée d'ogives : à vous de les distinguer."},
     dialogue_fin:{perso:"anselme", nom:"Frère Anselme", texte:"Le livre est complet. Bravo, apprentis."}}
  ]
};

const ENIGMES_FALLBACK = { salles:[
  {num:1, enigmes:[{id:"secours-1", titre:"Clovis, roi des Francs", type:"qcm", lecon:"clovis",
    consigne:"Choisis la bonne réponse.", commun:{questions:[{q:"Clovis est le roi…",
      options:["des Francs","des Romains","des Gaulois"], bonne:0}]}}]},
  {num:2, enigmes:[]},{num:3, enigmes:[]},{num:4, enigmes:[]},{num:5, enigmes:[]}
]};

/* ---- Mode vérification (enseignant) ----
   index.html?salle=3&niveau=CM1 ouvre la salle 3 (salle=6 : écran de fin).
   Rien n'est sauvegardé : une partie en cours sur le poste reste intacte. */
const VERIF = (()=>{
  const p = new URLSearchParams(location.search);
  const n = parseInt(p.get("salle"), 10);
  if(!(n >= 1 && n <= NB_SALLES+1)) return null;
  return {
    salle:n,
    niveau: p.get("niveau") === "CM1" ? "CM1" : "CM2",
    enigme: Math.max(0, (parseInt(p.get("enigme"),10)||1) - 1)
  };
})();

/* ---- Sauvegarde ---- */
function sauvegarder(){
  if(VERIF) return;
  try{ localStorage.setItem(CLE_SAUVEGARDE, JSON.stringify(ETAT)); }catch(e){}
}

/* ---- Navigation ---- */
function aller(ecranId){
  document.querySelectorAll(".ecran").forEach(e=>e.classList.remove("actif"));
  document.getElementById(ecranId).classList.add("actif");
  window.scrollTo({top:0, behavior:"smooth"});
}

/* ---- HUD ---- */
function majHUD(){
  document.getElementById("hud").style.display = (ETAT.salle>=1 && ETAT.debut) ? "flex" : "none";
  document.getElementById("hud-eq-nom").textContent = ETAT.equipe || "—";
  document.getElementById("hud-score-val").textContent = ETAT.score;
  document.getElementById("hud-cle-val").textContent = ETAT.motsCles.length;
  const m = Math.floor(ETAT.msEcoules/60000);
  const s = Math.floor((ETAT.msEcoules%60000)/1000);
  document.getElementById("hud-min").textContent = String(m).padStart(2,"0");
  document.getElementById("hud-sec").textContent = String(s).padStart(2,"0");
  const limite = ETAT.reglages.dureeMin || 60;
  document.getElementById("hud-temps").classList.toggle("alerte", m >= limite-5);
  const btnL = document.getElementById("btn-lecons");
  if(btnL) btnL.style.display = ETAT.reglages.leconsAutorisees ? "inline-flex" : "none";
}

/* ---- Minuteur ---- */
let timerId = null, dernierTick = null;
function demarrerTimer(){
  if(timerId) return;
  dernierTick = Date.now();
  timerId = setInterval(()=>{
    if(ETAT.enPause || ETAT.fini){ dernierTick = Date.now(); return; }
    const now = Date.now();
    ETAT.msEcoules += now - dernierTick;
    dernierTick = now;
    majHUD();
    if(ETAT.salle >= 1) sauvegarder();
  }, 1000);
}

/* ---- Score, toast, confettis ---- */
function ajouterScore(pts, raison){
  ETAT.score += pts;
  majHUD();
  if(pts>0) toast("+"+pts+" pts"+(raison?" · "+raison:""));
}
function penaliserIndice(){
  ETAT.indicesSalle++; ETAT.indicesTotal++;
  ETAT.score = Math.max(0, ETAT.score - MALUS_INDICE);
  majHUD(); sauvegarder();
}
function toast(msg){
  const t = document.createElement("div");
  t.className = "toast"; t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(()=>{ t.style.transition="opacity .4s"; t.style.opacity="0"; setTimeout(()=>t.remove(),400); }, 1800);
}
function confettis(n=60){
  const couleurs=["#1d3a8a","#b22222","#c9a227","#2e7d32","#fff"];
  for(let i=0;i<n;i++){
    const c=document.createElement("div");
    c.className="confetti";
    c.style.left=Math.random()*100+"vw";
    c.style.background=couleurs[i%couleurs.length];
    c.style.animationDuration=(0.8+Math.random()*1.2)+"s";
    c.style.animationDelay=(Math.random()*0.3)+"s";
    c.style.transform="rotate("+Math.random()*360+"deg)";
    document.body.appendChild(c);
    setTimeout(()=>c.remove(),2200);
  }
}

/* ---- Barres de progression ---- */
function barreProgression(){
  let html = '<div class="progression" aria-label="Progression dans les salles">';
  for(let i=1;i<=NB_SALLES;i++){
    const cls = i < ETAT.salle ? "fait" : (i===ETAT.salle ? "actuel" : "");
    html += `<div class="prog-point ${cls}">${i}</div>`;
  }
  return html + "</div>";
}
function filEnigmes(total){
  let html = '<div class="fil-enigmes" aria-label="Énigmes de la salle">';
  for(let i=0;i<total;i++){
    const cls = i < ETAT.enigme ? "fait" : (i===ETAT.enigme ? "actuel" : "");
    html += `<div class="fil-point ${cls}">${i+1}</div>`;
  }
  return html + "</div>";
}
/** Les cinq pages du livre, telles qu'elles sont à l'instant t. */
function serruresHTML(){
  return `<div class="coffre-serrures" aria-label="Les cinq pages du livre">${DONNEES.salles.map((s,i)=>{
    const ouverte = ETAT.motsCles.includes(s.motCle);
    return `<div class="serrure ${ouverte?"ouverte":""}">
      <span class="icone" aria-hidden="true">${ouverte?"📜":"▫️"}</span>
      <span class="mot">${ouverte?s.motCle:"Page "+(i+1)+" : à refaire"}</span>
    </div>`;
  }).join("")}</div>`;
}

/* ============================================================
   DÉMARRAGE
   ============================================================ */
document.addEventListener("DOMContentLoaded", async ()=>{
  await chargerDonnees();
  initVoix();

  // Nettoyage d'une sauvegarde d'une version antérieure ou incohérente
  try{
    const vStockee = localStorage.getItem("escape_app_version_moyenage");
    const brut = localStorage.getItem(CLE_SAUVEGARDE);
    if(brut){
      const etat = JSON.parse(brut);
      if(vStockee !== VERSION_APP || (etat.salle && etat.salle > NB_SALLES) || etat.fini){
        localStorage.removeItem(CLE_SAUVEGARDE);
      }
    }
    localStorage.setItem("escape_app_version_moyenage", VERSION_APP);
  }catch(e){}

  const reglagesSauves = ETAT.reglages;
  resetEtatJeu();
  ETAT.reglages = reglagesSauves;

  // Sélection du niveau
  document.querySelectorAll(".opt-niveau").forEach(o=>{
    if(o.dataset.niveau === ETAT.niveau) o.classList.add("choisi");
    o.addEventListener("click", ()=>{
      document.querySelectorAll(".opt-niveau").forEach(x=>x.classList.remove("choisi"));
      o.classList.add("choisi");
      ETAT.niveau = o.dataset.niveau;
      majApercuNiveau();
      verifierPret();
    });
  });
  majApercuNiveau();

  const inp = document.getElementById("input-equipe");
  inp.addEventListener("input", e=>{ ETAT.equipe = e.target.value.trim(); verifierPret(); });

  document.getElementById("btn-demarrer").addEventListener("click", ()=>{
    const niveau = ETAT.niveau, equipe = ETAT.equipe, reglages = ETAT.reglages;
    resetEtatJeu();
    Object.assign(ETAT, {reglages, niveau, equipe, debut:Date.now(), salleDebut:Date.now(), msEcoules:0});
    lancerCine("intro", "L'abbaye, la veille de la visite de l'évêque", ()=>entrerDansLeJeu(false));
  });

  document.getElementById("btn-pause").addEventListener("click", ()=>{
    ETAT.enPause = true;
    if(typeof setFigerVideos === "function") setFigerVideos(true);
    aller("ecran-pause");
  });
  document.getElementById("btn-reprendre").addEventListener("click", ()=>{
    ETAT.enPause = false;
    dernierTick = Date.now();
    if(typeof setFigerVideos === "function") setFigerVideos(!!ETAT.reglages.animationsReduites);
    aller("ecran-salle");
  });
  document.getElementById("btn-lecons").addEventListener("click", ouvrirBiblioLecons);
  document.getElementById("btn-reglages").addEventListener("click", ouvrirReglages);
  verifierPret();

  if(VERIF){
    ETAT.equipe = "Vérification";
    ETAT.niveau = VERIF.niveau;
    ETAT.salle = Math.min(VERIF.salle, NB_SALLES);
    ETAT.enigme = VERIF.enigme;
    ETAT.debut = ETAT.salleDebut = Date.now();
    ETAT.msEcoules = 0;
    if(VERIF.salle > NB_SALLES){
      // Écran de fin : on simule une partie complète
      ETAT.motsCles = DONNEES.salles.map(s=>s.motCle);
      ETAT.enigmesReussies = nbEnigmesTotal();
      ETAT.score = Math.round(scoreMax()*0.8);
      appliquerReglages(); demarrerTimer(); aller("ecran-salle"); afficherFermoir();
    }else{
      entrerDansLeJeu(false);
    }
    toast("🔍 Mode vérification · " + VERIF.niveau + " · rien n'est sauvegardé");
    return;
  }

  // Reprise d'une partie en cours
  let partie = null;
  try{ const s = localStorage.getItem(CLE_SAUVEGARDE); if(s) partie = JSON.parse(s); }catch(e){}
  if(partie && partie.equipe && partie.debut && !partie.fini && partie.salle>=1 && partie.salle<=NB_SALLES){
    if(confirm("Une partie est en cours pour l'équipe « "+partie.equipe+" » (salle "+partie.salle+"/"+NB_SALLES+").\nVoulez-vous la reprendre ?")){
      Object.assign(ETAT, {
        equipe:partie.equipe, niveau:partie.niveau||"CM2", salle:partie.salle,
        enigme:partie.enigme||0, score:partie.score||0, motsCles:partie.motsCles||[],
        badges:partie.badges||ETAT.badges, msEcoules:partie.msEcoules||0,
        enigmesReussies:partie.enigmesReussies||0, indicesTotal:partie.indicesTotal||0,
        tempsParSalle:partie.tempsParSalle||{}, fini:false
      });
      ETAT.debut = Date.now() - ETAT.msEcoules;
      entrerDansLeJeu(true);
      return;
    }else{
      localStorage.removeItem(CLE_SAUVEGARDE);
    }
  }else if(partie && partie.fini){
    localStorage.removeItem(CLE_SAUVEGARDE);
  }
});

function verifierPret(){
  document.getElementById("btn-demarrer").disabled = !(ETAT.equipe.length>=2 && ETAT.niveau);
}
/** Affiche « 15 énigmes » ou « 20 énigmes » sous le choix du niveau. */
function majApercuNiveau(){
  const el = document.getElementById("apercu-niveau");
  if(!el || !ENIGMES) return;
  el.textContent = `${ETAT.niveau} · ${nbEnigmesTotal()} énigmes réparties en ${NB_SALLES} salles · ${scoreMax()} points maximum`;
}

function lancerCine(base, titre, suite){
  if(ETAT.reglages.cinematiques !== false && typeof jouerCinematique === "function"){
    jouerCinematique({base, titre, onFin:suite});
  }else{ suite(); }
}

function appliquerReglages(){
  document.documentElement.style.setProperty("--taille-texte", ETAT.reglages.tailleTexte+"rem");
  setNarrationActif(ETAT.reglages.narrationActive);
  setVolume(ETAT.reglages.volume);
  if(typeof setSonsActifs === "function") setSonsActifs(ETAT.reglages.sonsActifs !== false);
  if(typeof setVolumeSons === "function") setVolumeSons(ETAT.reglages.volumeSons !== undefined ? ETAT.reglages.volumeSons : 0.55);
  document.body.classList.toggle("calme", !!ETAT.reglages.animationsReduites);
  if(typeof setDecorsVideo === "function") setDecorsVideo(ETAT.reglages.decorsVideo !== false);
  if(typeof setSonVideo === "function")    setSonVideo(!!ETAT.reglages.sonVideo);
  if(typeof setFigerVideos === "function") setFigerVideos(!!ETAT.reglages.animationsReduites);
}

function entrerDansLeJeu(reprise){
  appliquerReglages();
  aller("ecran-salle");
  demarrerTimer();
  majHUD();
  afficherSalle(ETAT.salle);
  if(reprise) toast("Partie reprise ✓");
  if(!VERIF && typeof demarrerSync === "function") demarrerSync();
}

/* ============================================================
   AFFICHAGE D'UNE SALLE
   ============================================================ */
function salleEnigmes(n){
  const bloc = (ENIGMES.salles||[]).find(s=>s.num===n);
  return bloc ? enigmesDe(bloc) : [];
}

function afficherSalle(n){
  const salle = DONNEES.salles[n-1];
  if(!salle){ finDuJeu(); return; }
  ETAT.salleDebut = Date.now();
  ETAT.indicesSalle = 0;
  if(typeof stopperVideos === "function") stopperVideos();

  const c = document.getElementById("salle-contenu");
  c.innerHTML = `
    ${barreProgression()}
    <h2>📜 Page ${salle.num}/${NB_SALLES} — ${salle.titre}</h2>
    ${htmlScene(salle.decor, salle)}
    <div id="zone-dialogue"></div>
    <div class="zone-enigme" id="zone-enigme"></div>
  `;
  activerScene(c.querySelector(".scene"));
  if(typeof son === "function") son("transition");
  if(typeof ambiance === "function") ambiance(salle.decor);
  lancerDialogueIntro(salle);
  afficherEnigmeCourante();
  majHUD();
  sauvegarder();
}

async function lancerDialogueIntro(salle){
  let texte = salle.dialogue_intro.texte;
  if(ETAT.reglages.apiActive && ETAT.reglages.apiCle && typeof genererDialogue === "function"){
    try{
      const gen = await genererDialogue({
        perso: salle.dialogue_intro.perso,
        situation: "Arrivée dans : " + salle.titre,
        niveau: ETAT.niveau, reussite:false
      });
      if(gen && gen.trim()) texte = gen;
    }catch(e){ console.warn("IA indisponible, texte écrit conservé :", e.message); }
  }
  afficherDialogue({perso:salle.dialogue_intro.perso, nom:salle.dialogue_intro.nom, texte});
}

/* ---- Une énigme à la fois ---- */
function afficherEnigmeCourante(){
  const liste = salleEnigmes(ETAT.salle);
  const zone = document.getElementById("zone-enigme");
  if(!liste.length){
    zone.innerHTML = `<div class="feedback erreur show">Aucune énigme n'a pu être chargée pour cette salle.</div>`;
    return;
  }
  if(ETAT.enigme >= liste.length){ validerSalle(ETAT.salle); return; }
  const e = liste[ETAT.enigme];
  zone.innerHTML = filEnigmes(liste.length) + enigmeHTML(e, ETAT.enigme+1, liste.length);
  activerEnigme(e, ()=>reussirEnigme(e, liste));
  zone.scrollIntoView({behavior:"smooth", block:"nearest"});
  sauvegarder();
}

function reussirEnigme(e, liste){
  ETAT.enigmesReussies++;
  ajouterScore(PTS_ENIGME, "énigme résolue");
  confettis(18);
  ETAT.enigme++;
  sauvegarder();
  if(ETAT.enigme >= liste.length){
    setTimeout(()=>validerSalle(ETAT.salle), 900);
  }else{
    const zone = document.getElementById("zone-enigme");
    const suite = document.createElement("div");
    suite.className = "boutons";
    suite.innerHTML = `<button class="btn grand bleu" id="btn-enigme-suivante">➡️ Énigme suivante (${ETAT.enigme+1}/${liste.length})</button>`;
    zone.appendChild(suite);
    suite.querySelector("button").addEventListener("click", afficherEnigmeCourante);
    suite.scrollIntoView({behavior:"smooth", block:"center"});
  }
}

/* ---- Salle bouclée : la page est refaite ---- */
function validerSalle(n){
  const salle = DONNEES.salles[n-1];
  const duree = Date.now() - ETAT.salleDebut;
  ETAT.tempsParSalle[n] = duree;

  if(salle.motCle && !ETAT.motsCles.includes(salle.motCle)) ETAT.motsCles.push(salle.motCle);
  if(typeof son === "function") setTimeout(()=>son("deverrouille"), 300);

  let pts = 0, raison = "";
  const seuil = (ETAT.niveau === "CM1" ? 8 : 10) * 60000;  // rythme attendu par salle
  if(duree < seuil && ETAT.indicesSalle === 0){ pts = PTS_RAPIDITE; raison = "salle rapide et sans indice 🏃"; }
  else if(duree < seuil){ pts = Math.max(1, PTS_RAPIDITE-1); raison = "salle rapide"; }
  if(pts) ajouterScore(pts, raison);
  attribuerBadges(n, duree);

  const zone = document.getElementById("zone-enigme");
  zone.innerHTML = `
    <div class="mot-cle">
      <div class="lib">Page ${n} refaite — mot-clé</div>
      <div class="val">${salle.motCle}</div>
    </div>
    ${serruresHTML()}
    <p class="center" style="opacity:.8">⏱️ ${Math.floor(duree/60000)} min ${Math.floor((duree%60000)/1000)} s dans cette salle
       · 💡 ${ETAT.indicesSalle} indice${ETAT.indicesSalle>1?"s":""}</p>
  `;
  confettis(50);
  sauvegarder();

  if(n === NB_SALLES){
    setTimeout(afficherFermoir, 1600);
    return;
  }

  function boutonSuivant(){
    if(document.getElementById("btn-salle-suivante")) return;
    const b = document.createElement("div");
    b.className = "boutons";
    b.innerHTML = `<button class="btn grand vert" id="btn-salle-suivante">➡️ Page suivante</button>`;
    zone.appendChild(b);
    b.querySelector("button").addEventListener("click", ()=>{
      ETAT.salle++; ETAT.enigme = 0;
      if(ETAT.salle > NB_SALLES) finDuJeu(); else afficherSalle(ETAT.salle);
    });
    b.scrollIntoView({behavior:"smooth", block:"center"});
  }
  const filet = setTimeout(boutonSuivant, 12000);   // si la synthèse vocale ne démarre pas
  afficherDialogue({
    perso: salle.dialogue_reussite.perso,
    nom: salle.dialogue_reussite.nom,
    texte: salle.dialogue_reussite.texte,
    onFini: ()=>{
      clearTimeout(filet);
      if(typeof geste === "function" && typeof persoCourant === "function") geste(persoCourant(), "joie", 1600);
      boutonSuivant();
    }
  });
}

/* ---- Badges ---- */
function attribuerBadges(n, duree){
  if(duree < 6*60000) ETAT.badges.vitesse = true;                 // une salle en moins de 6 min
  if(n === 3 && ETAT.indicesSalle === 0) ETAT.badges.copiste = true;
  if(n === 4 && ETAT.indicesSalle === 0) ETAT.badges.charite = true;
  if(n === NB_SALLES && ETAT.indicesTotal <= 3) ETAT.badges.maitre = true;
}

/* ============================================================
   LE FERMOIR DU LIVRE — mécanisme de sortie
   Les cinq mots reconstituent la première ligne (l'incipit) ;
   le fermoir s'ouvre quand la frise chronologique est rangée.
   L'énigme est décrite dans enigmes.json (clé "final") et
   rendue par le moteur générique (type "ordre").
   ============================================================ */
function incipitHTML(){
  const phrase = (DONNEES && DONNEES.incipit) || DONNEES_FALLBACK.incipit;
  const mots = DONNEES.salles.map(s=>s.motCle);
  let html = echapper(phrase);
  mots.forEach(m=>{
    const trouve = ETAT.motsCles.includes(m);
    html = html.replace(m, trouve ? `<b class="mot-incipit">${m}</b>` : `<span class="mot-manquant">${"_ ".repeat(m.length).trim()}</span>`);
  });
  return `<div class="incipit"><span class="lettrine" aria-hidden="true">${echapper(phrase.charAt(0))}</span><span class="sr-only">${echapper(phrase.charAt(0))}</span>${html.slice(1)}</div>`;
}

function afficherFermoir(){
  const fin = ENIGMES && ENIGMES.final;
  if(!fin || ETAT.fermoir){ lancerCine("final", "Le livre est complet", finDuJeu); return; }
  if(typeof stopperVideos === "function") stopperVideos();
  const cf = (DONNEES && DONNEES.cadenas_final) || {};
  const c = document.getElementById("salle-contenu");
  c.innerHTML = `
    ${barreProgression()}
    <h2>🔒 ${echapper(cf.titre || fin.titre || "Le fermoir du livre")}</h2>
    <p class="center" style="font-style:italic">La première ligne du livre se lit de nouveau :</p>
    ${incipitHTML()}
    <div id="zone-dialogue"></div>
    <div class="zone-enigme" id="zone-enigme">${enigmeHTML(fin, 1, 1)}</div>`;
  if(cf.texte) afficherDialogue({perso: cf.perso || "anselme", nom: (DONNEES.personnages[cf.perso||"anselme"]||{}).nom || "", texte: cf.texte});
  activerEnigme(fin, ()=>{
    ETAT.fermoir = true;
    sauvegarder();
    if(typeof son === "function") son("deverrouille");
    setTimeout(()=>lancerCine("final", "Le livre est complet", finDuJeu), 1400);
  });
  majHUD();
  sauvegarder();
}

/* ============================================================
   FIN DU JEU
   ============================================================ */
function finDuJeu(){
  ETAT.fini = true;
  if(typeof stopperVideos === "function") stopperVideos();
  aller("ecran-fin");
  if(typeof ambiance === "function") ambiance("accueil");
  if(typeof son === "function"){
    son("succes"); setTimeout(()=>son("deverrouille"), 600); setTimeout(()=>son("badge"), 1300);
  }
  const min = Math.floor(ETAT.msEcoules/60000), sec = Math.floor((ETAT.msEcoules%60000)/1000);
  const c = document.getElementById("fin-contenu");
  c.innerHTML = `
    <h2>📖 Le livre est complet !</h2>
    <div id="fin-dialogue"></div>
    ${serruresHTML()}
    <div class="article-secret">
      <div class="sceau">✒️</div>
      <div class="numero">INCIPIT — LA PREMIÈRE LIGNE DU LIVRE</div>
      ${incipitHTML()}
      <div style="font-size:.8rem;opacity:.75">« Incipit » est un mot latin qui veut dire « ici commence ».
        Les copistes du Moyen Âge l'écrivaient souvent au début d'un livre.</div>
    </div>
    <div class="grille-badges">
      ${badgeHTML("vitesse","⏱️","Équipe rapide","une salle en moins de 6 minutes")}
      ${badgeHTML("copiste","✒️","Plume sûre","page 3 sans aucun indice")}
      ${badgeHTML("charite","🕊️","Cœur charitable","page 4 sans aucun indice")}
      ${badgeHTML("maitre","📖","Maître copiste","3 indices au maximum sur toute la partie")}
    </div>
    <p style="text-align:center;opacity:.85">⏱️ Temps total : <b>${min} min ${sec} s</b>
       · 🧩 Énigmes résolues : <b>${ETAT.enigmesReussies}/${nbEnigmesTotal()}</b></p>
    <hr style="border:none;border-top:2px dotted var(--parchemin-ombre);margin:18px 0">
    <h2>📝 Quizz final — valide tes acquis</h2>
    <div id="quizz"></div>
    <div class="feedback" id="fb-quizz"></div>
    <div class="boutons" id="quizz-actions" style="display:none">
      <button class="btn grand vert" id="btn-voir-score">🏆 Voir mon score final</button>
    </div>
    <div id="score-recap" style="display:none"></div>
    <div class="boutons" style="margin-top:24px">
      <button class="btn bleu" id="btn-rejouer">🔄 Rejouer</button>
      <button class="btn gris" id="btn-imprimer-bilan">🖨️ Imprimer le bilan</button>
    </div>
  `;
  const fin = DONNEES.salles[NB_SALLES-1].dialogue_fin;
  if(fin){
    setTimeout(()=>{
      const scene = document.createElement("div");
      scene.className = "personnage-scene entrer";
      scene.innerHTML = `
        <div class="portrait">${htmlPortrait(fin.perso)}</div>
        <div class="bulle"><div class="nom-perso">${fin.nom}</div><div class="texte" id="fin-texte"></div></div>`;
      c.querySelector("#fin-dialogue").appendChild(scene);
      activerPortrait(scene.querySelector(".portrait-conteneur"));
      machineEcrire(scene.querySelector("#fin-texte"), fin.texte);
      if(NARRATION.parlerActif) parler(fin.perso, fin.texte, scene);
    }, 200);
  }
  construireQuizz();
  document.getElementById("btn-rejouer").addEventListener("click", ()=>{
    localStorage.removeItem(CLE_SAUVEGARDE);
    location.reload();
  });
  document.getElementById("btn-imprimer-bilan").addEventListener("click", imprimerBilan);
  confettis(100);
  sauvegarder();
}

function badgeHTML(cle, icone, nom, desc){
  return `<div class="badge ${ETAT.badges[cle]?"gagne":""}">
    <div class="icone">${icone}</div><div class="nom">${nom}</div><div class="desc">${desc}</div></div>`;
}

/* ============================================================
   QUIZZ FINAL — 5 questions, différenciées, lues dans
   assets/data/evaluations.json (clé "quizz_final")
   ============================================================ */
const QUIZZ_FALLBACK = {
  CM1:[
    {q:"Qui est Clovis ?", options:["Le roi des Francs","Un empereur romain","Un moine copiste"], bonne:0},
    {q:"Qui est couronné empereur à Rome en l'an 800 ?", options:["Clovis","Charlemagne","Saint Louis"], bonne:1},
    {q:"Comment appelle-t-on la salle où les moines copient les livres ?", options:["Le réfectoire","Le scriptorium","Le donjon"], bonne:1},
    {q:"Qu'est-ce qu'un hôtel-Dieu ?", options:["Un château de seigneur","Une auberge payante","Une maison qui accueille gratuitement les malades pauvres"], bonne:2},
    {q:"Des arcs pointus, des arcs-boutants et de grands vitraux : c'est…", options:["l'art gothique","l'art roman","l'art romain"], bonne:0}
  ],
  CM2:[
    {q:"Pourquoi écrit-on que Clovis est baptisé « vers l'an 500 » ?", options:["Parce que la date exacte est discutée (496, 499 ou 508)","Parce qu'il a été baptisé en l'an 500 exactement","Parce qu'il n'a jamais été baptisé"], bonne:0},
    {q:"Quelle est la date du couronnement impérial de Charlemagne ?", options:["25 décembre 800","4 août 1443","14 juillet 814"], bonne:0},
    {q:"Charlemagne a-t-il inventé l'école ?", options:["Oui, pour tous les enfants","Non : il a demandé davantage d'écoles dans les monastères et les évêchés, qui existaient déjà","Non : l'école n'existe pas au Moyen Âge"], bonne:1},
    {q:"Comment l'Église finance-t-elle l'aide aux pauvres ?", options:["Par la dîme, ses terres et les dons","Par un impôt du roi","Par les paiements des malades"], bonne:0},
    {q:"Pourquoi les églises gothiques peuvent-elles avoir de grands vitraux ?", options:["Parce que la croisée d'ogives et les arcs-boutants soulagent les murs","Parce que leurs murs sont plus épais","Parce que le verre est plus solide que la pierre"], bonne:0}
  ]
};
function quizzCourant(){
  const ev = (typeof window !== "undefined" && window.EVAL_DATA) || null;
  const src = (ev && ev.quizz_final) || QUIZZ_FALLBACK;
  return (src[ETAT.niveau] || QUIZZ_FALLBACK[ETAT.niveau] || QUIZZ_FALLBACK.CM2).slice(0, NB_QUIZ);
}

function construireQuizz(){
  const cont = document.getElementById("quizz");
  if(!cont) return;
  const QUIZZ = quizzCourant();
  cont.innerHTML = QUIZZ.map((item,i)=>`
    <div class="qcm-question" data-i="${i}">
      <div class="q">${i+1}. ${item.q}</div>
      ${item.options.map((o,j)=>`<label class="qcm-option" data-j="${j}">${o}</label>`).join("")}
    </div>`).join("");
  const repondu = Array(QUIZZ.length).fill(null);
  cont.querySelectorAll(".qcm-question").forEach(qi=>{
    const i = +qi.dataset.i;
    qi.querySelectorAll(".qcm-option").forEach(opt=>{
      opt.addEventListener("click", ()=>{
        qi.querySelectorAll(".qcm-option").forEach(x=>x.classList.remove("select","bien","mal"));
        opt.classList.add("select");
        repondu[i] = +opt.dataset.j;
        if(repondu.every(r=>r!==null)) document.getElementById("quizz-actions").style.display="flex";
      });
    });
  });
  document.getElementById("btn-voir-score").onclick = ()=>{
    let score = 0;
    QUIZZ.forEach((item,i)=>{
      const qi = cont.querySelector(`.qcm-question[data-i="${i}"]`);
      qi.querySelectorAll(".qcm-option").forEach(opt=>{
        const j = +opt.dataset.j;
        opt.classList.remove("select");
        if(j===item.bonne) opt.classList.add("bien");
        else if(j===repondu[i]) opt.classList.add("mal");
      });
      if(repondu[i]===item.bonne) score++;
    });
    ETAT.quiz = {repondu:true, score};
    ETAT.score += score*PTS_QUIZ;
    majHUD();
    const fb = document.getElementById("fb-quizz");
    fb.className = "feedback " + (score>=4?"succes":(score>=3?"indice":"erreur")) + " show";
    fb.innerHTML = `Tu as <b>${score}/${QUIZZ.length}</b> bonnes réponses (+${score*PTS_QUIZ} points). ${
      score===5?"Parfait : tu es un vrai copiste !" :
      score>=4?"Très bien ! Encore un petit effort." :
      score>=3?"Pas mal. Relis la leçon 📚 sur l'art roman et l'art gothique." :
               "Reprends les leçons 📚 : Clovis, Charlemagne et le rôle de l'Église."}`;
    afficherRecap();
    sauvegarder();
  };
}

function afficherRecap(){
  const recap = document.getElementById("score-recap");
  const max = scoreMax();
  const min = Math.floor(ETAT.msEcoules/60000), sec = Math.floor((ETAT.msEcoules%60000)/1000);
  const nbBadges = Object.values(ETAT.badges).filter(Boolean).length;
  const part = ETAT.score / max;
  const mention = part>=0.9 ? "🏆 Maître copiste"
                : part>=0.75 ? "🥈 Enlumineur"
                : part>=0.55 ? "🥉 Apprenti copiste"
                : "📜 Novice motivé";
  recap.style.display = "block";
  recap.innerHTML = `
    <div class="article-secret">
      <div class="sceau">🏁</div>
      <div class="numero">BILAN DE L'ÉQUIPE « ${ETAT.equipe.toUpperCase()} »</div>
      <div class="score-final">${ETAT.score}<span class="sur"> / ${max}</span></div>
      <div style="font-size:1.1rem;color:var(--bleu-fonce);font-weight:bold">${mention}</div>
      <hr style="border:none;border-top:1px solid #c9b78a;margin:12px 0">
      <div>⏱️ Temps : <b>${min} min ${sec} s</b></div>
      <div>🧩 Énigmes : <b>${ETAT.enigmesReussies}/${nbEnigmesTotal()}</b></div>
      <div>📜 Pages refaites : <b>${ETAT.motsCles.length}/${NB_SALLES}</b></div>
      <div>💡 Indices utilisés : <b>${ETAT.indicesTotal}</b></div>
      <div>📝 Quizz : <b>${ETAT.quiz.score}/${NB_QUIZ}</b></div>
      <div>🏅 Badges : <b>${nbBadges}/4</b></div>
      <div>Niveau : <b>${ETAT.niveau}</b></div>
    </div>`;
  recap.scrollIntoView({behavior:"smooth", block:"center"});
  confettis(60);
}

/* Exposé global */
window.ETAT = ETAT;
window.DONNEES = () => DONNEES;
window.ENIGMES = () => ENIGMES;
window.afficherFermoir = afficherFermoir;
window.NB_SALLES = NB_SALLES;
window.afficherSalle = afficherSalle;
window.validerSalle = validerSalle;
window.finDuJeu = finDuJeu;
window.sauvegarder = sauvegarder;
window.majHUD = majHUD;
window.ajouterScore = ajouterScore;
window.penaliserIndice = penaliserIndice;
window.toast = toast;
window.confettis = confettis;
window.scoreMax = scoreMax;
window.nbEnigmesTotal = nbEnigmesTotal;
window.salleEnigmes = salleEnigmes;
window.enigmesDe = enigmesDe;
window.quizzCourant = quizzCourant;
