/* ============================================================
   APP — Moteur principal
   LE TOUR DU MONDE EN 80 MINUTES · Géographie CM1-CM2
   ------------------------------------------------------------
   Coordonne : écrans, escales, décors (SVG / image / vidéo),
   dialogues animés, énigmes, score, minuteur, leçons, réglages.
   ============================================================ */

/* ---- État global de la partie ---- */
const ETAT = {
  equipe: "",
  niveau: "CM2",
  salle: 1,                 // « salle » = escale (1 à 5)
  score: 0,
  fragments: [],            // cachets de voyage récoltés
  badges: {navigateur:false, geographe:false, voyageur:false, horloger:false},
  debut: null,
  msEcoules: 0,
  enPause: false,
  tempsParSalle: {},
  salleDebut: null,
  indicesUtilises: 0,
  indicesTotal: 0,
  quiz: {repondu:false, score:0},
  fini: false,
  reglages: {
    narrationActive: true,
    volume: 1,
    tailleTexte: 1,
    dureeMin: 55,
    leconsAutorisees: true,
    apiActive: false,
    sonsActifs: true,
    volumeSons: 0.55,
    animationsReduites: false,
    // ---- Réglages multimédia ----
    decorsVideo: true,       // décors filmés autorisés
    sonVideo: false,         // son des décors (muet par défaut)
    cinematiques: true,      // séquences d'intro / de fin
  }
};

/* Score maximal atteignable, utilisé pour le barème affiché et imprimé :
     5 escales × (10 pts + 5 pts de rapidité) = 75
   + quizz final 5 questions × 2 pts          = 10
   ------------------------------------------------
                                                85  */
const SCORE_MAX = 85;

const CLE_SAUVEGARDE = "escape_tourdumonde_v1";
const VERSION_APP = "v1";
let DONNEES = null;

function resetEtatJeu(){
  ETAT.equipe = "";
  ETAT.niveau = "CM2";
  ETAT.salle = 1;
  ETAT.score = 0;
  ETAT.fragments = [];
  ETAT.badges = {navigateur:false, geographe:false, voyageur:false, horloger:false};
  ETAT.debut = null;
  ETAT.msEcoules = 0;
  ETAT.enPause = false;
  ETAT.tempsParSalle = {};
  ETAT.salleDebut = null;
  ETAT.indicesUtilises = 0;
  ETAT.indicesTotal = 0;
  ETAT.quiz = {repondu:false, score:0};
  ETAT.fini = false;
}

/* ---- Chargement des données ----
   Robuste : si le fetch échoue (ouverture en file://), on bascule
   sur les données embarquées. Le jeu marche en double-clic. */
async function chargerDonnees(){
  let ok = false;
  try{
    const resp = await fetch("assets/data/dialogues.json", {cache:"no-store"});
    if(resp.ok){ DONNEES = await resp.json(); ok = true; }
  }catch(e){
    console.warn("Fetch dialogues.json impossible (mode file:// ?) — données embarquées.");
  }
  if(!ok || !DONNEES || !DONNEES.salles){
    DONNEES = JSON.parse(JSON.stringify(DONNEES_FALLBACK));
  }
  try{
    const r = localStorage.getItem("escape_tdm_reglages");
    if(r) Object.assign(ETAT.reglages, JSON.parse(r));
  }catch(e){}
  appliquerReglages();
}

/* ============================================================
   LES 5 ESCALES — données embarquées (fallback file://)
   ============================================================ */
const DONNEES_FALLBACK = {
  personnages: {
    fogg:         {nom:"Phileas Fogg",      emoji:"🎩"},
    passepartout: {nom:"Jean Passepartout", emoji:"🧳"},
    aouda:        {nom:"Mrs Aouda",         emoji:"🌺"},
    fix:          {nom:"L'inspecteur Fix",  emoji:"🔍"}
  },
  salles: [
    {
      num:1, titre:"Le Reform Club, à Londres", decor:"reform-club",
      lieu:"🎩 Londres, Angleterre — mercredi 2 octobre 1872, 20 h 45",
      coordonnees:"51° N · 0° — Méridien de Greenwich",
      description:"Le feu crépite dans la cheminée du club le plus fermé de Londres. Sur un guéridon d'acajou, un grand globe terrestre tourne doucement. Phileas Fogg vient de parier vingt mille livres qu'il ferait le tour du monde en quatre-vingts jours — mais son carnet de route a disparu.",
      sens:["👁️ le globe qui tourne","👂 la pluie sur la vitre","👃 le bois du foyer"],
      dialogue_intro:{perso:"fogg", nom:"Phileas Fogg", texte:"Messieurs, mesdemoiselles. Je viens de parier que je ferai le tour du monde en quatre-vingts jours. Mais on m'a dérobé mon carnet de route. Sans itinéraire, je ne puis partir. Reconstituez d'abord ma carte du monde : placez chaque continent et chaque océan à sa juste place. Le temps, lui, ne nous attendra pas."},
      dialogue_reussite:{perso:"fogg", nom:"Phileas Fogg", texte:"Parfait. La Terre reprend sa forme. Nous partirons par l'<b>est</b> : Paris, l'Italie, puis l'Égypte. Passepartout, les bagages ! Rendez-vous au <b>canal de Suez</b>."},
      fragment:"ROSE DES VENTS", badge_rapidite:"navigateur"
    },
    {
      num:2, titre:"L'isthme de Suez", decor:"suez",
      lieu:"🐫 Suez, Égypte — mercredi 9 octobre 1872",
      coordonnees:"30° N · 32° E — entre deux mers",
      description:"Le sable brûle sous un soleil blanc. Devant vous s'ouvre une longue tranchée d'eau bleue creusée à travers le désert : le canal de Suez, ouvert depuis trois ans à peine. Le paquebot Mongolia y glisse lentement, sa cheminée crachant un panache blanc.",
      sens:["👁️ le canal dans le désert","👂 la sirène du vapeur","👃 le sable chaud"],
      dialogue_intro:{perso:"fix", nom:"L'inspecteur Fix", texte:"Halte-là ! Inspecteur Fix, de Scotland Yard. Votre monsieur Fogg m'a tout l'air d'un voleur en fuite. Vous prétendez l'aider ? Fort bien : prouvez-moi que vous savez seulement où vous allez. Remettez ces escales dans l'ordre. Et dites-moi donc à quoi sert ce canal."},
      dialogue_reussite:{perso:"fix", nom:"L'inspecteur Fix", texte:"Hum. Vous connaissez votre géographie, je vous l'accorde. Le canal relie la Méditerranée à la mer Rouge — sans lui, il faudrait contourner toute l'Afrique. Filez donc vers l'<b>Inde</b>. Je vous suis de près."},
      fragment:"LE CANAL", badge_rapidite:"voyageur"
    },
    {
      num:3, titre:"La jungle de l'Inde", decor:"inde",
      lieu:"🐘 Près de Kholby, Inde — mardi 22 octobre 1872",
      coordonnees:"22° N · 78° E — sous les tropiques",
      description:"Le train s'est arrêté net : la voie ferrée n'est pas terminée. Devant vous, cinquante kilomètres de jungle épaisse, et pour seule monture un éléphant nommé Kiouni. Au loin, les cimes blanches de l'Himalaya percent la brume de chaleur.",
      sens:["👁️ la voie ferrée coupée","👂 les singes dans la canopée","👃 la terre humide"],
      dialogue_intro:{perso:"aouda", nom:"Mrs Aouda", texte:"Vous m'avez sauvée, je vous aiderai à mon tour. Voyez ce carnet : monsieur Fogg y notait les paysages traversés. Les pages se sont mêlées. Retrouvez quel climat va avec quel paysage — car on ne voyage pas sans savoir quel temps l'on trouvera."},
      dialogue_reussite:{perso:"aouda", nom:"Mrs Aouda", texte:"C'est cela même. Du désert brûlant à la banquise, tout dépend de la distance à l'<b>équateur</b> et de l'altitude. Hâtons-nous : le vapeur de <b>Hong Kong</b> n'attendra pas."},
      fragment:"LES CLIMATS", badge_rapidite:"geographe"
    },
    {
      num:4, titre:"La mer de Chine", decor:"mer-chine",
      lieu:"🌊 À bord de la Tankadère, mer de Chine — 7 novembre 1872",
      coordonnees:"22° N · 114° E — cap au nord-est",
      description:"La goélette tangue dans une mer démontée. Le vent hurle dans les haubans, la pluie cingle le pont. Le pilote hurle des ordres qu'on n'entend plus. Il faut tenir le cap — et surtout, savoir combien de chemin il reste à parcourir.",
      sens:["👁️ les éclairs sur l'horizon","👂 le vent dans les voiles","👃 l'embrun salé"],
      dialogue_intro:{perso:"passepartout", nom:"Jean Passepartout", texte:"Sacrebleu, quelle tempête ! Aidez-moi, je vous en prie : le timonier veut le journal de bord tout de suite. Pour chaque étape, il faut le bon moyen de transport et la vraie distance. On mesure sur la carte, puis on multiplie avec l'échelle. Vite, mes amis, vite !"},
      dialogue_reussite:{perso:"passepartout", nom:"Jean Passepartout", texte:"Ah ! Vous êtes des as ! Le timonier a son cap. Encore l'Amérique à traverser, et nous voilà rentrés à <b>Londres</b>… si toutefois nous arrivons à l'heure."},
      fragment:"LA VAPEUR", badge_rapidite:"voyageur"
    },
    {
      num:5, titre:"L'observatoire de Greenwich", decor:"greenwich",
      lieu:"⏰ Greenwich, Londres — samedi 21 décembre 1872",
      coordonnees:"51° N · 0° — longitude zéro",
      description:"Vous voici revenus au point de départ, sur la ligne de laiton du méridien zéro. Phileas Fogg croit avoir perdu son pari d'un seul jour. Il se trompe. Toute la clé de l'histoire tient dans une chose que la Terre fait en tournant : les fuseaux horaires.",
      sens:["👁️ la ligne du méridien","👂 le carillon de Big Ben","👃 le froid de décembre"],
      dialogue_intro:{perso:"fogg", nom:"Phileas Fogg", texte:"J'ai échoué, dit-on. Quatre-vingt-un jours au lieu de quatre-vingts. Et pourtant… quelque chose ne tourne pas rond dans mes comptes. Nous avons voyagé vers l'est tout du long. Calculez donc l'heure qu'il est dans ces villes, puis dites-moi ce qui a bien pu m'arriver."},
      dialogue_fin:{perso:"fogg", nom:"Phileas Fogg", texte:"Ainsi donc… en allant vers l'est, j'ai gagné un jour sans m'en apercevoir. Le carnet est complet, et le pari est gagné. Messieurs, mesdemoiselles : vous êtes de fort bons géographes."},
      fragment:null, badge_rapidite:"horloger"
    }
  ]
};

/* ---- Sauvegarde ---- */
function sauvegarder(){
  try{ localStorage.setItem(CLE_SAUVEGARDE, JSON.stringify(ETAT)); }catch(e){}
}

/* ---- Navigation ---- */
function aller(ecranId){
  document.querySelectorAll(".ecran").forEach(e=>e.classList.remove("actif"));
  const cible = document.getElementById(ecranId);
  if(cible) cible.classList.add("actif");
  window.scrollTo({top:0,behavior:"smooth"});
}

/* ---- HUD ---- */
function majHUD(){
  const hud = document.getElementById("hud");
  hud.style.display = (ETAT.salle>=1 && ETAT.debut) ? "flex" : "none";
  document.getElementById("hud-eq-nom").textContent = ETAT.equipe || "—";
  document.getElementById("hud-score-val").textContent = ETAT.score;
  document.getElementById("hud-frag-val").textContent = ETAT.fragments.length;
  const m = Math.floor(ETAT.msEcoules/60000);
  const s = Math.floor((ETAT.msEcoules%60000)/1000);
  document.getElementById("hud-min").textContent = String(m).padStart(2,"0");
  document.getElementById("hud-sec").textContent = String(s).padStart(2,"0");
  const limite = ETAT.reglages.dureeMin || 55;
  document.getElementById("hud-temps").classList.toggle("alerte", m >= limite-5);
  const btnL = document.getElementById("btn-lecons");
  if(btnL) btnL.style.display = ETAT.reglages.leconsAutorisees ? "inline-flex" : "none";
}

/* ---- Minuteur ---- */
let timerId = null;
let dernierTick = null;
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

/* ---- Score & retours visuels ---- */
function ajouterScore(pts, raison){
  ETAT.score += pts;
  majHUD();
  if(pts>0) toast("+"+pts+" pts"+(raison?" · "+raison:""));
}
function toast(msg){
  const t = document.createElement("div");
  t.className = "toast";
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(()=>{ t.style.transition="opacity .4s"; t.style.opacity="0"; setTimeout(()=>t.remove(),400); }, 1900);
}
function confettis(n=60){
  const couleurs=["#c08a3e","#2b6f9e","#2f7d6b","#a33327","#f2e4c8"];
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

/* ---- Barre de progression : les 5 escales ---- */
function barreProgression(){
  let html = '<div class="progression" aria-label="Progression du voyage">';
  for(let i=1;i<=5;i++){
    const cls = i < ETAT.salle ? "fait" : (i===ETAT.salle ? "actuel" : "");
    html += `<div class="prog-point ${cls}" title="Escale ${i}">${i}</div>`;
    if(i<5) html += '<div class="prog-lien"></div>';
  }
  return html + '</div>';
}

/* ---- Système d'indices ---- */
function activerBoutonIndice(indices){
  let idx = 0;
  const btn = document.getElementById("btn-indice");
  if(!btn) return;
  btn.textContent = "💡 Indice";
  btn.addEventListener("click", ()=>{
    if(idx >= indices.length){ btn.textContent = "💡 Plus d'indices"; return; }
    const fb = document.createElement("div");
    fb.className = "feedback indice show";
    fb.innerHTML = "💡 " + indices[idx];
    document.querySelector(".zone-enigme").appendChild(fb);
    idx++;
    ETAT.indicesUtilises++;
    ETAT.indicesTotal++;
    ETAT.score = Math.max(0, ETAT.score-2);
    majHUD();
    btn.textContent = idx < indices.length ? "💡 Indice suivant" : "💡 Plus d'indices";
    fb.scrollIntoView({behavior:"smooth",block:"center"});
  });
}

/* ============================================================
   DÉMARRAGE
   ============================================================ */
document.addEventListener("DOMContentLoaded", async ()=>{
  await chargerDonnees();
  initVoix();

  // Une sauvegarde d'une autre version, ou une partie terminée,
  // est effacée : on ne veut jamais retomber directement sur la fin.
  try{
    const vStockee = localStorage.getItem("escape_tdm_version");
    const brut = localStorage.getItem(CLE_SAUVEGARDE);
    if(brut){
      const e = JSON.parse(brut);
      if(vStockee !== VERSION_APP || (e.salle && e.salle > 5) || e.fini){
        localStorage.removeItem(CLE_SAUVEGARDE);
      }
    }
    localStorage.setItem("escape_tdm_version", VERSION_APP);
  }catch(e){}

  const reglagesSauves = ETAT.reglages;
  resetEtatJeu();
  ETAT.reglages = reglagesSauves;

  // ---- Listeners fixes ----
  document.querySelectorAll(".opt-niveau").forEach(o=>{
    if(o.dataset.niveau === ETAT.niveau) o.classList.add("choisi");
    o.addEventListener("click", ()=>{
      document.querySelectorAll(".opt-niveau").forEach(x=>x.classList.remove("choisi"));
      o.classList.add("choisi");
      ETAT.niveau = o.dataset.niveau;
      verifierPret();
    });
  });
  const inp = document.getElementById("input-equipe");
  inp.addEventListener("input", e=>{ ETAT.equipe = e.target.value.trim(); verifierPret(); });

  document.getElementById("btn-demarrer").addEventListener("click", ()=>{
    const niveau = ETAT.niveau, equipe = ETAT.equipe, reg = ETAT.reglages;
    resetEtatJeu();
    ETAT.reglages = reg;
    ETAT.niveau = niveau;
    ETAT.equipe = equipe;
    ETAT.debut = Date.now();
    ETAT.salleDebut = Date.now();
    ETAT.msEcoules = 0;
    // Cinématique d'ouverture, si l'enseignant a fourni intro.mp4
    lancerCine("intro", "Le pari de Phileas Fogg", ()=>entrerDansLeJeu(false));
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

  // ---- Reprise éventuelle d'une partie ----
  let enCours = null;
  try{
    const s = localStorage.getItem(CLE_SAUVEGARDE);
    if(s) enCours = JSON.parse(s);
  }catch(e){}

  if(enCours && enCours.equipe && enCours.debut && !enCours.fini && enCours.salle>=1 && enCours.salle<=5){
    if(confirm("Une partie est en cours pour l'équipe « "+enCours.equipe+" » (escale "+enCours.salle+"/5).\nVoulez-vous la reprendre ?")){
      ETAT.equipe = enCours.equipe;
      ETAT.niveau = enCours.niveau || "CM2";
      ETAT.salle = enCours.salle;
      ETAT.score = enCours.score || 0;
      ETAT.fragments = enCours.fragments || [];
      ETAT.badges = enCours.badges || ETAT.badges;
      ETAT.msEcoules = enCours.msEcoules || 0;
      ETAT.indicesTotal = enCours.indicesTotal || 0;
      ETAT.debut = Date.now() - ETAT.msEcoules;
      ETAT.fini = false;
      entrerDansLeJeu(true);
    }else{
      localStorage.removeItem(CLE_SAUVEGARDE);
    }
  }else if(enCours && enCours.fini){
    localStorage.removeItem(CLE_SAUVEGARDE);
  }
});

function verifierPret(){
  document.getElementById("btn-demarrer").disabled = !(ETAT.equipe.length>=2 && ETAT.niveau);
}

/* Joue une cinématique si elle est autorisée et disponible ; sinon enchaîne. */
function lancerCine(base, titre, suite){
  if(ETAT.reglages.cinematiques !== false && typeof jouerCinematique === "function"){
    jouerCinematique({base, titre, onFin:suite});
  }else{
    suite();
  }
}

function appliquerReglages(){
  document.documentElement.style.setProperty("--taille-texte", ETAT.reglages.tailleTexte+"rem");
  setNarrationActif(ETAT.reglages.narrationActive);
  setVolume(ETAT.reglages.volume);
  if(typeof setSonsActifs === "function") setSonsActifs(ETAT.reglages.sonsActifs !== false);
  if(typeof setVolumeSons === "function") setVolumeSons(ETAT.reglages.volumeSons !== undefined ? ETAT.reglages.volumeSons : 0.55);
  document.body.classList.toggle("calme", !!ETAT.reglages.animationsReduites);
  // ---- Multimédia ----
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
  if(reprise) toast("Voyage repris ✓");
  if(typeof demarrerSync === "function") demarrerSync();
}

/* ============================================================
   AFFICHAGE D'UNE ESCALE
   ============================================================ */
function afficherSalle(n){
  const salle = DONNEES.salles[n-1];
  if(!salle){ finDuJeu(); return; }
  const c = document.getElementById("salle-contenu");
  ETAT.salleDebut = Date.now();
  ETAT.indicesUtilises = 0;

  // Libère les vidéos de l'escale précédente avant de reconstruire
  if(typeof stopperVideos === "function") stopperVideos();

  c.innerHTML = `
    ${barreProgression()}
    <h2>🧭 Escale ${salle.num} — ${salle.titre}</h2>
    ${htmlScene(salle.decor, salle)}
    <div class="consigne">${consigneSalle(n)}</div>
    <div class="zone-enigme">${enigmeSalle(n)}</div>
  `;
  // Cherche vidéo puis image ; garde le SVG si rien n'est trouvé
  activerScene(c.querySelector(".scene"));
  if(typeof son === "function") son("transition");
  if(typeof ambiance === "function") ambiance(salle.decor);
  lancerDialogueIntro(salle);
  activerEnigme(n);
  majHUD();
  sauvegarder();
}

async function lancerDialogueIntro(salle){
  let texte = salle.dialogue_intro.texte;
  if(ETAT.reglages.apiActive && ETAT.reglages.apiCle && typeof genererDialogue === "function"){
    try{
      const gen = await genererDialogue({
        perso: salle.dialogue_intro.perso,
        situation: "Arrivée à l'escale : "+salle.titre,
        niveau: ETAT.niveau,
        reussite: false
      });
      if(gen && gen.trim()) texte = gen;
    }catch(e){ console.warn("IA indisponible, dialogue statique utilisé."); }
  }
  afficherDialogue({
    perso: salle.dialogue_intro.perso,
    nom:   salle.dialogue_intro.nom,
    texte: texte
  });
}

function consigneSalle(n){
  const cm1 = ETAT.niveau==="CM1";
  return {
    1: cm1
      ? "Clique sur une <b>zone de la carte</b>, puis sur son <b>nom</b> en bas. Place les <b>5 continents</b> et les <b>3 océans</b>."
      : "Clique sur une <b>zone de la carte</b>, puis sur son <b>nom</b> en bas. Place les <b>6 continents</b>, l'<b>Antarctique</b> et les <b>5 océans</b>.",
    2: cm1
      ? "Remets les <b>4 escales</b> dans l'ordre du voyage avec les flèches ▲▼, puis réponds à la question sur le canal."
      : "Remets les <b>7 escales</b> dans l'ordre du voyage avec les flèches ▲▼, puis réponds à la question sur le canal de Suez.",
    3: cm1
      ? "Clique sur un <b>paysage</b>, puis sur le <b>climat</b> qui lui va. Associe les <b>4 paires</b>."
      : "Clique sur un <b>paysage</b>, puis sur le <b>climat</b> qui lui va. Associe les <b>6 paires</b> et repère la zone climatique.",
    4: "Pour chaque étape : choisis le <b>moyen de transport</b>, puis calcule la <b>distance réelle</b> (mesure en cm × échelle).",
    5: "Calcule l'<b>heure locale</b> de chaque ville à partir de midi à Londres, puis réponds à la grande question du <b>jour gagné</b>.",
  }[n] || "";
}

/* ---- Validation d'une escale ---- */
function validerSalle(n){
  const salle = DONNEES.salles[n-1];
  const duree = Date.now() - ETAT.salleDebut;
  ETAT.tempsParSalle[n] = duree;

  if(salle.fragment && !ETAT.fragments.includes(salle.fragment)){
    ETAT.fragments.push(salle.fragment);
    if(typeof son === "function") setTimeout(()=>son("fragment"), 600);
  }

  let pts = 10, raison = "";
  if(duree < 180000){ pts += 5; raison = "rapidité 🏃"; if(salle.badge_rapidite) ETAT.badges[salle.badge_rapidite] = true; }
  else if(duree < 360000){ pts += 2; }
  if(ETAT.indicesUtilises > 0 && raison !== "rapidité 🏃") pts = Math.max(5, pts-2);
  ajouterScore(pts, raison);

  // Le badge du géographe récompense un parcours sans indice
  if(n === 5 && ETAT.indicesTotal === 0) ETAT.badges.geographe = true;

  if(n === 5){
    confettis(60);
    sauvegarder();
    setTimeout(()=>lancerCine("final", "Le quatre-vingtième jour", finDuJeu), 1200);
    return;
  }

  /* Affiche le bouton d'escale suivante. Idempotent : peut être appelé
     plusieurs fois sans créer de doublon. */
  function afficherBoutonSuivant(){
    const c = document.getElementById("salle-contenu");
    const zoneEnigme = c && c.querySelector(".zone-enigme");
    if(!zoneEnigme || c.querySelector("#btn-salle-suivante")) return;
    const zone = document.createElement("div");
    zone.className = "boutons";
    zone.innerHTML = `<button class="btn grand jade" id="btn-salle-suivante">➡️ Escale suivante</button>`;
    zoneEnigme.appendChild(zone);
    zone.querySelector("#btn-salle-suivante").addEventListener("click", ()=>{
      ETAT.salle++;
      if(ETAT.salle > 5) finDuJeu();
      else afficherSalle(ETAT.salle);
    });
  }

  /* Filet de sécurité : sur certains postes, la synthèse vocale ne démarre
     jamais (pas de voix installée, lecture bloquée tant que l'élève n'a
     rien cliqué…) et l'événement de fin de réplique n'arrive pas. Sans ce
     minuteur, l'équipe resterait bloquée sur une énigme déjà réussie. */
  const filet = setTimeout(afficherBoutonSuivant, 12000);

  afficherDialogue({
    perso: salle.dialogue_reussite.perso,
    nom:   salle.dialogue_reussite.nom,
    texte: salle.dialogue_reussite.texte +
      `<div class="sous-titre" style="margin-top:8px;font-size:.85rem">⏱️ ${Math.floor(duree/60000)} min ${Math.floor((duree%60000)/1000)} s · +${pts} points${salle.fragment?` · 🛂 Cachet obtenu : <b>${salle.fragment}</b>`:""}</div>`,
    onFini: ()=>{
      clearTimeout(filet);
      if(typeof geste === "function" && typeof persoCourant === "function"){
        geste(persoCourant(), "joie", 1600);
      }
      afficherBoutonSuivant();
    }
  });
  confettis(40);
  sauvegarder();
}

/* ============================================================
   FIN DU VOYAGE
   ============================================================ */
function finDuJeu(){
  ETAT.fini = true;
  if(typeof stopperVideos === "function") stopperVideos();
  aller("ecran-fin");
  if(typeof ambiance === "function") ambiance("accueil");
  if(typeof son === "function"){
    son("succes");
    setTimeout(()=>son("badge"), 700);
    setTimeout(()=>son("fragment"), 1500);
  }
  const min = Math.floor(ETAT.msEcoules/60000);
  const sec = Math.floor((ETAT.msEcoules%60000)/1000);
  const c = document.getElementById("fin-contenu");

  c.innerHTML = `
    <h2>🎉 Le pari est gagné !</h2>
    <div id="fin-dialogue"></div>

    <div class="carnet-final">
      <div class="sceau-cire">🛂</div>
      <div class="numero">CARNET DE ROUTE — DERNIÈRE PAGE</div>
      <div class="texte">« En voyageant vers l'<b>est</b>, Phileas Fogg est allé à la rencontre du soleil.
      Il a vu se lever <b>quatre-vingts</b> soleils quand les Londoniens n'en voyaient que
      <b>soixante-dix-neuf</b>. Il avait gagné un jour — et son pari. »</div>
      <div style="font-size:.82rem;opacity:.72">D'après <i>Le Tour du monde en quatre-vingts jours</i>, Jules Verne, 1873.</div>
    </div>

    <h3 class="center">🛂 Vos cachets de voyage</h3>
    <div class="cachets">
      ${["ROSE DES VENTS","LE CANAL","LES CLIMATS","LA VAPEUR"].map(f=>{
        const eu = ETAT.fragments.includes(f);
        const ic = {"ROSE DES VENTS":"🧭","LE CANAL":"🚢","LES CLIMATS":"🌡️","LA VAPEUR":"🚂"}[f];
        return `<div class="cachet ${eu?"":"vide"}"><span class="icone">${eu?ic:"·"}</span>${eu?f:"non obtenu"}</div>`;
      }).join("")}
    </div>

    <div class="grille-badges">
      ${badgeHTML("navigateur","🧭","Le Navigateur","carte du monde")}
      ${badgeHTML("geographe","🌍","Le Géographe","aucun indice")}
      ${badgeHTML("voyageur","🚂","Le Voyageur","escales rapides")}
      ${badgeHTML("horloger","⏰","Maître du Temps","fuseaux horaires")}
    </div>
    <p class="center" style="opacity:.8">⏱️ Temps total : <b>${min} min ${sec} s</b></p>

    <hr style="border:none;border-top:2px dotted var(--velin-ombre);margin:18px 0">
    <h2>📝 Quizz final — Valide tes connaissances</h2>
    <div id="quizz"></div>
    <div class="feedback" id="fb-quizz"></div>
    <div class="boutons" id="quizz-actions" style="display:none">
      <button class="btn grand jade" id="btn-voir-score">🏆 Voir mon score final</button>
    </div>
    <div id="score-recap" style="display:none"></div>

    <div class="boutons" style="margin-top:24px">
      <button class="btn azur" id="btn-rejouer">🔄 Repartir en voyage</button>
      <button class="btn gris" id="btn-imprimer-bilan">🖨️ Imprimer le bilan</button>
    </div>
  `;

  // Réplique finale de Phileas Fogg
  const finDialogue = DONNEES.salles[4].dialogue_fin;
  const hote = c.querySelector("#fin-dialogue");
  setTimeout(()=>{
    const scene = document.createElement("div");
    scene.className = "personnage-scene entrer";
    scene.innerHTML = `
      <div class="portrait">${htmlPortrait(finDialogue.perso)}</div>
      <div class="bulle"><div class="nom-perso">${finDialogue.nom}</div><div class="texte" id="fin-texte"></div></div>`;
    hote.appendChild(scene);
    machineEcrire(scene.querySelector("#fin-texte"), finDialogue.texte);
    if(NARRATION.parlerActif) parler(finDialogue.perso, finDialogue.texte, scene);
  }, 200);

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
    <div class="icone">${icone}</div>
    <div class="nom">${nom}</div>
    <div class="desc">${desc}</div>
  </div>`;
}

/* ============================================================
   QUIZZ FINAL — géographie
   ============================================================ */
const QUIZZ = [
  {q:"1. Combien y a-t-il de continents sur Terre ?",
   options:["5","6","10"], bonne:1},
  {q:"2. Quel est le plus grand océan du monde ?",
   options:["L'océan Atlantique","L'océan Indien","L'océan Pacifique"], bonne:2},
  {q:"3. Le canal de Suez relie la mer Méditerranée à…",
   options:["la mer Rouge","la mer Noire","l'océan Pacifique"], bonne:0},
  {q:"4. La ligne imaginaire qui coupe la Terre en deux moitiés, nord et sud, s'appelle…",
   options:["le méridien de Greenwich","l'équateur","le tropique du Cancer"], bonne:1},
  {q:"5. En combien de fuseaux horaires la Terre est-elle découpée ?",
   options:["12","24","36"], bonne:1},
];

function construireQuizz(){
  const cont = document.getElementById("quizz");
  if(!cont) return;
  cont.innerHTML = QUIZZ.map((item,i)=>`
    <div class="qcm-question" data-i="${i}">
      <div class="q">${item.q}</div>
      ${item.options.map((o,j)=>`<label class="qcm-option" data-j="${j}">${o}</label>`).join("")}
    </div>`).join("");

  const repondu = Array(QUIZZ.length).fill(null);
  cont.querySelectorAll(".qcm-question").forEach(qi=>{
    const i = +qi.dataset.i;
    qi.querySelectorAll(".qcm-option").forEach(opt=>{
      opt.addEventListener("click", ()=>{
        qi.querySelectorAll(".qcm-option").forEach(x=>x.classList.remove("select","bonne","mauvaise"));
        opt.classList.add("select");
        repondu[i] = +opt.dataset.j;
        if(repondu.every(r=>r!==null)) document.getElementById("quizz-actions").style.display="flex";
      });
    });
  });

  const btnVoir = document.getElementById("btn-voir-score");
  if(!btnVoir) return;
  btnVoir.onclick = ()=>{
    let score = 0;
    QUIZZ.forEach((item,i)=>{
      const qi = cont.querySelector(`.qcm-question[data-i="${i}"]`);
      qi.querySelectorAll(".qcm-option").forEach(opt=>{
        const j = +opt.dataset.j;
        opt.classList.remove("select");
        if(j === item.bonne) opt.classList.add("bonne");
        else if(j === repondu[i]) opt.classList.add("mauvaise");
      });
      if(repondu[i] === item.bonne) score++;
    });
    ETAT.quiz.repondu = true;
    ETAT.quiz.score = score;
    const pts = score*2;
    ETAT.score += pts;
    majHUD();

    const fb = document.getElementById("fb-quizz");
    fb.className = "feedback "+(score>=4?"succes":(score>=3?"indice":"erreur"))+" show";
    fb.innerHTML = `Tu as <b>${score}/${QUIZZ.length}</b> bonnes réponses (+${pts} points). ${
      score===5 ? "Parfait — tu es un véritable géographe ! 🌍" :
      score>=4  ? "Très bien ! Encore un petit effort." :
      score>=3  ? "Pas mal ! Revois les continents et les océans." :
                  "Relis les leçons sur le planisphère et les fuseaux horaires."}`;

    const recap = document.getElementById("score-recap");
    recap.style.display = "block";
    const min = Math.floor(ETAT.msEcoules/60000);
    const sec = Math.floor((ETAT.msEcoules%60000)/1000);
    const nbBadges = Object.values(ETAT.badges).filter(Boolean).length;
    const mention = ETAT.score>=78 ? "🏆 Maître du Tour du Monde"
                  : ETAT.score>=64 ? "🥈 Grand Voyageur"
                  : ETAT.score>=50 ? "🥉 Explorateur confirmé"
                  : "🧭 Apprenti géographe";
    recap.innerHTML = `
      <div class="carnet-final">
        <div class="sceau-cire">🏁</div>
        <div class="numero">BILAN DE L'ÉQUIPE « ${ETAT.equipe.toUpperCase()} »</div>
        <div class="score-final">${ETAT.score}<span class="sur"> / ${SCORE_MAX}</span></div>
        <div style="font-size:1.1rem;color:var(--abysse-2);font-weight:bold">${mention}</div>
        <hr style="border:none;border-top:1px solid var(--velin-ombre);margin:12px 0">
        <div>⏱️ Temps : <b>${min} min ${sec} s</b></div>
        <div>🛂 Cachets : <b>${ETAT.fragments.length}/4</b></div>
        <div>📝 Quizz : <b>${ETAT.quiz.score}/${QUIZZ.length}</b></div>
        <div>🏅 Badges : <b>${nbBadges}/4</b></div>
        <div>Niveau : <b>${ETAT.niveau}</b></div>
      </div>`;
    recap.scrollIntoView({behavior:"smooth",block:"center"});
    confettis(60);
    sauvegarder();
  };
}

/* Exposé global */
window.ETAT = ETAT;
window.DONNEES = () => DONNEES;
window.afficherSalle = afficherSalle;
window.validerSalle = validerSalle;
window.finDuJeu = finDuJeu;
window.sauvegarder = sauvegarder;
window.majHUD = majHUD;
window.ajouterScore = ajouterScore;
window.toast = toast;
window.confettis = confettis;
window.activerBoutonIndice = activerBoutonIndice;
window.aller = aller;
window.appliquerReglages = appliquerReglages;
window.QUIZZ = QUIZZ;
window.SCORE_MAX = SCORE_MAX;
