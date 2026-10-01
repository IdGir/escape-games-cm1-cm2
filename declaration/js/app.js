/* ============================================================
   APP — Moteur principal du jeu
   Coordonne : écrans, salles, décors, dialogues animés,
               énigmes, score, minuteur, leçons, réglages
   ============================================================ */

/* ---- État global de la partie ---- */
const ETAT = {
  equipe: "",
  niveau: "CM2",
  salle: 1,
  score: 0,
  fragments: [],
  badges: {bastille:false, avocat:false, fraternite:false, lumiere:false},
  debut: null,
  msEcoules: 0,
  enPause: false,
  tempsParSalle: {},
  salleDebut: null,
  indicesUtilises: 0,
  quiz: {repondu:false, score:0},
  fini: false,
  enigmesPremierCoup: 0, erreursTotal: 0, coffreOuvert: false, coffrePremierCoup: false,
  reglages: {
    narrationActive: true,
    volume: 1,
    tailleTexte: 1,
    dureeMin: 55,
    leconsAutorisees: true,
    apiActive: false,
    sonsActifs: true,        // ambiances et bruitages synthétisés
    volumeSons: 0.55,        // volume des ambiances (voix réglée à part)
    animationsReduites: false,
    // ---- Multimédia ----
    decorsVideo: true,       // décors filmés autorisés (si des fichiers existent)
    sonVideo: false,         // les décors sont muets par défaut
    cinematiques: true,      // séquences plein écran d'intro / de fin
  }
};

/* Score maximal atteignable (moteur v2, octobre 2026) :
     5 énigmes justes du premier coup × 10 pts = 50   (3 pts après une erreur)
   + 5 salles × 5 pts de rapidité              = 25
   + coffre final ouvert du premier coup       = 10   (3 pts après une erreur)
   + quizz final 5 questions × 2 pts           = 10
   -------------------------------------------------
                                                 95  */
const SCORE_MAX = 5*PTS_PREMIER_COUP + 5*5 + PTS_COFFRE_PREMIER + 10;

const CLE_SAUVEGARDE = "escape_declaration_v2";
let DONNEES = null; // dialogues.json chargé

/* ---- Réinitialisation complète de l'état de jeu ----
   On garde les réglages (persistés séparément), on remet tout le reste à zéro. */
function resetEtatJeu(){
  ETAT.equipe = "";
  ETAT.niveau = "CM2";
  ETAT.salle = 1;
  ETAT.score = 0;
  ETAT.fragments = [];
  ETAT.badges = {bastille:false, avocat:false, fraternite:false, lumiere:false};
  ETAT.debut = null;
  ETAT.msEcoules = 0;
  ETAT.enPause = false;
  ETAT.tempsParSalle = {};
  ETAT.salleDebut = null;
  ETAT.indicesUtilises = 0;
  ETAT.quiz = {repondu:false, score:0};
  ETAT.fini = false;
  ETAT.enigmesPremierCoup = 0; ETAT.erreursTotal = 0;
  ETAT.coffreOuvert = false; ETAT.coffrePremierCoup = false;
}

/* ---- Chargement des données ----
   Robuste : si le fetch échoue (ex: ouverture en file:// sans serveur,
   ou politique CORS), on bascule sur les données embarquées (DONNEES_FALLBACK). */
async function chargerDonnees(){
  let fetchOk = false;
  try{
    const resp = await fetch("assets/data/dialogues.json", {cache:"no-store"});
    if(resp.ok){
      DONNEES = await resp.json();
      fetchOk = true;
    }
  }catch(e){
    console.warn("Fetch dialogues.json échoué (probablement mode file://). Bascule sur données embarquées.");
  }
  if(!fetchOk || !DONNEES || !DONNEES.salles){
    DONNEES = JSON.parse(JSON.stringify(DONNEES_FALLBACK));
  }
  // Charger les réglages sauvegardés
  try{
    const r = localStorage.getItem("escape_reglages");
    if(r) Object.assign(ETAT.reglages, JSON.parse(r));
  }catch(e){}
  appliquerReglages();
}

/* ---- Données embarquées (fallback si fetch impossible) ----
   Version condensée de dialogues.json, suffisante pour jouer en file://. */
const DONNEES_FALLBACK = {
  personnages: {
    louise:     {nom:"Louise",                  emoji:"🧒"},
    gutenberg:  {nom:"Maître Gutenberg",        emoji:"🖨️"},
    marquis:    {nom:"Le Marquis de Montclair", emoji:"🎩"},
    maximilien: {nom:"Maximilien",              emoji:"⚖️"}
  },
  salles: [
    {
      num:1, titre:"La cour du Palais-Royal", decor:"palais-royal",
      lieu:"🌧️ La cour du Palais-Royal — 26 août 1789",
      description:"La pluie fine fouette les pavés luisants. Des affiches révolutionnaires, fraîchement collées, suintent sous l'humidité. Au loin, la rumeur d'une foule monte et descend, ponctuée du tintement d'une cloche.",
      sens:["👁️ pavés mouillés","👂 foule + cloche","👃 pain chaud"],
      dialogue_intro:{perso:"louise", nom:"Louise", texte:"Eh ! Vous, là ! Vous cherchez le manuscrit volé, pas vrai ? Tout Paris en parle. Moi, j'connais cette ville comme ma poche. Aidez-moi à décoder ce cahier, et j'vous file un renseignement. Marché conclu ?"},
      dialogue_reussite:{perso:"louise", nom:"Louise", texte:"Palsambleu, vous êtes malins ! Le voleur est passé par l'<b>imprimerie</b>, rue de la Harpe. Cherchez Maître Gutenberg."},
      fragment:"LIBERTÉ", badge_rapidite:"bastille"
    },
    {
      num:2, titre:"L'imprimerie clandestine", decor:"imprimerie",
      lieu:"🖨️ L'imprimerie clandestine — sous les toits de Paris",
      description:"La porte grince. Ici, c'est le cliquetis régulier de la presse à bras qui domine. L'air sent le plomb fondu et l'encre grasse. Une chandelle vacille.",
      sens:["👂 presse à bras","👃 encre & plomb","👁️ chandelle"],
      dialogue_intro:{perso:"gutenberg", nom:"Maître Gutenberg", texte:"Entrez, et refermez cette porte. La presse tourne : c'est par l'imprimé que les idées voyagent. Avant de vous aider, associez ces extraits de la Marseillaise aux bonnes images."},
      dialogue_reussite:{perso:"gutenberg", nom:"Maître Gutenberg", texte:"Joli. Rousseau disait que l'homme est né libre. Voici votre fragment. Le <b>Marquis de Montclair</b> rôde aux <b>Tuileries</b>."},
      fragment:"ÉGALITÉ", badge_rapidite:"avocat"
    },
    {
      num:3, titre:"Le jardin des Tuileries", decor:"tuileries",
      lieu:"🌳 Le jardin des Tuileries — après-midi ensoleillé",
      description:"Le soleil perce les nuages sur les allées de sable. Des paons crient près d'une volière. L'odeur des tilleuls en fleur se mêle au parfum de poudre de riz des nobles.",
      sens:["👁️ allées de sable","👂 paons","👃 tilleuls en fleur"],
      dialogue_intro:{perso:"marquis", nom:"Le Marquis de Montclair", texte:"Ah. Les voilà, les apprentis du futur. Je vous attendais. Croyez-vous vraiment que ce manuscrit vous attendrait sagement ? Je le cherche aussi. Prouvez-moi votre perspicacité."},
      dialogue_reussite:{perso:"marquis", nom:"Le Marquis de Montclair", texte:"Vous avez l'œil. Le vrai voleur veut <b>vendre</b> l'article secret. Il est à l'<b>Assemblée</b>. Voici votre fragment."},
      fragment:"FRATERNITÉ", badge_rapidite:"fraternite"
    },
    {
      num:4, titre:"La place de la Bastille", decor:"bastille",
      lieu:"🏰 La place de la Bastille — après la prise du 14 juillet 1789",
      description:"On dirait que le combat vient à peine de cesser. La fumée de poudre pique encore les yeux. Des débris de pierre jonchent le sol. La forteresse fume, à demi démantelée.",
      sens:["👁️ débris & fumée","👃 poudre métallique","👂 chants"],
      dialogue_intro:{perso:"louise", nom:"Louise", texte:"Regardez ! Sur cette table abandonnée, y'a des portraits de tous ces grands bonshommes. Si vous savez qui a dit quoi, vous trouverez le dernier indice. À vous de jouer !"},
      dialogue_reussite:{perso:"louise", nom:"Louise", texte:"Vous êtes incollables ! Le dernier fragment vous attend : le <b>mécanisme de l'Assemblée</b>."},
      fragment:"1789", badge_rapidite:"lumiere"
    },
    {
      num:5, titre:"La salle de l'Assemblée nationale", decor:"assemblee",
      lieu:"🏛️ La salle de l'Assemblée nationale — jour de l'adoption",
      description:"La salle est vaste et pleine d'écho. Des gradins en bois entourent une estrade où trône un fauteuil de président. Une horloge bat la mesure — tic, tac, tic, tac…",
      sens:["👂 tic-tac","👃 cire & bois","👁️ gradins"],
      dialogue_intro:{perso:"maximilien", nom:"Maximilien", texte:"Vous y êtes presque, apprentis. Voici la salle de l'Assemblée. Placez les étiquettes aux bons emplacements. Le bon ordre révèlera l'emplacement du manuscrit… et l'article secret."},
      dialogue_fin:{perso:"maximilien", nom:"Maximilien", texte:"Vous avez réussi. Les quatre fragments sont réunis. L'article secret est retrouvé. Voici ce qu'il disait…"},
      fragment:null, badge_rapidite:null
    }
  ]
};

/* ---- Mode vérification (enseignant) ----
   index.html?salle=3&niveau=CM1 ouvre directement la salle 3 (salle=6 :
   écran de fin), sans nom d'équipe. Rien n'est sauvegardé ni envoyé au
   tableau de bord : une partie en cours sur ce poste reste intacte.
   Les liens sont prêts dans verifier.html, à la racine du projet. */
const VERIF = (()=>{
  const p = new URLSearchParams(location.search);
  const n = parseInt(p.get("salle"), 10);
  if(!(n >= 1 && n <= 6)) return null;
  return { salle:n, niveau: p.get("niveau") === "CM1" ? "CM1" : "CM2" };
})();

/* ---- Sauvegarde / chargement partie ---- */
function sauvegarder(){
  if(VERIF) return;
  try{ localStorage.setItem(CLE_SAUVEGARDE, JSON.stringify(ETAT)); }catch(e){}
}
function chargerPartie(){
  try{
    const s = localStorage.getItem(CLE_SAUVEGARDE);
    if(!s) return false;
    Object.assign(ETAT, JSON.parse(s));
    return true;
  }catch(e){ return false; }
}

/* ---- Navigation entre écrans ---- */
function aller(ecranId){
  document.querySelectorAll(".ecran").forEach(e=>e.classList.remove("actif"));
  document.getElementById(ecranId).classList.add("actif");
  window.scrollTo({top:0,behavior:"smooth"});
}

/* ---- HUD ---- */
function majHUD(){
  document.getElementById("hud").style.display = (ETAT.salle>=1 && ETAT.debut) ? "flex" : "none";
  document.getElementById("hud-eq-nom").textContent = ETAT.equipe || "—";
  document.getElementById("hud-score-val").textContent = ETAT.score;
  document.getElementById("hud-frag-val").textContent = ETAT.fragments.length;
  const m = Math.floor(ETAT.msEcoules/60000);
  const s = Math.floor((ETAT.msEcoules%60000)/1000);
  document.getElementById("hud-min").textContent = String(m).padStart(2,"0");
  document.getElementById("hud-sec").textContent = String(s).padStart(2,"0");
  const limite = ETAT.reglages.dureeMin || 55;
  const alerte = m >= limite-5;
  document.getElementById("hud-temps").classList.toggle("alerte", alerte);
  // bouton leçons
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

/* ---- Score & toast ---- */
function ajouterScore(pts, raison){
  ETAT.score += pts;
  majHUD();
  if(pts>0) toast("+"+pts+" pts"+(raison?" · "+raison:""));
}
function toast(msg){
  let t = document.createElement("div");
  t.className = "toast";
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(()=>{ t.style.transition="opacity .4s"; t.style.opacity="0"; setTimeout(()=>t.remove(),400); }, 1800);
}

/* ---- Confettis ---- */
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

/* ---- Barre de progression ---- */
function barreProgression(){
  let html = '<div class="progression" aria-label="Progression">';
  for(let i=1;i<=5;i++){
    let cls = i < ETAT.salle ? "fait" : (i===ETAT.salle ? "actuel" : "");
    html += `<div class="prog-point ${cls}">${i}</div>`;
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
    if(idx >= indices.length){
      btn.textContent = "💡 Plus d'indices";
      return;
    }
    const fb = document.createElement("div");
    fb.className = "feedback indice show";
    fb.innerHTML = "💡 " + indices[idx];
    document.querySelector(".zone-enigme").appendChild(fb);
    idx++;
    ETAT.indicesUtilises++;
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

  // ===== Détection de version : si la sauvegarde provient d'une version
  // antérieure (v1 ou v2 sans reset propre), on l'efface pour repartir à zéro.
  // Évite le bug "on arrive directement à la fin" si une partie terminée
  // d'une ancienne version est restée dans localStorage.
  const VERSION_APP = "v7";   // v7 : moteur v2 (premier coup, coffre final)
  try{
    const vStockee = localStorage.getItem("escape_app_version");
    const etatBrut = localStorage.getItem(CLE_SAUVEGARDE);
    if(etatBrut){
      const etat = JSON.parse(etatBrut);
      // Si l'état est incohérent (salle>5, fini mais pas de quizz, etc.) OU
      // si la version stockée diffère, on nettoie tout.
      if(vStockee !== VERSION_APP || (etat.salle && etat.salle>5) || etat.fini){
        console.info("Nettoyage de l'ancienne sauvegarde (version "+(vStockee||"inconnue")+" → "+VERSION_APP+")");
        localStorage.removeItem(CLE_SAUVEGARDE);
      }
    }
    localStorage.setItem("escape_app_version", VERSION_APP);
  }catch(e){}

  // Réinitialiser l'état de jeu (on garde uniquement les réglages)
  // pour éviter qu'une partie précédente terminée ne ramène directement à la fin.
  const reglagesSauves = ETAT.reglages;
  resetEtatJeu();
  ETAT.reglages = reglagesSauves;

  // ===== Attachement SYSTÉMATIQUE de tous les listeners fixes =====
  // (indispensable : doit avoir lieu même si on reprend une partie en cours)
  // Sélection niveau
  document.querySelectorAll(".opt-niveau").forEach(o=>{
    if(o.dataset.niveau === ETAT.niveau) o.classList.add("choisi");
    o.addEventListener("click", ()=>{
      document.querySelectorAll(".opt-niveau").forEach(x=>x.classList.remove("choisi"));
      o.classList.add("choisi");
      ETAT.niveau = o.dataset.niveau;
      verifierPret();
    });
  });
  // Nom équipe
  const inp = document.getElementById("input-equipe");
  inp.addEventListener("input", e=>{ ETAT.equipe = e.target.value.trim(); verifierPret(); });

  // Bouton démarrer (toujours repartir d'un état propre)
  document.getElementById("btn-demarrer").addEventListener("click", ()=>{
    const niveauChoisi = ETAT.niveau;
    const equipeChoisie = ETAT.equipe;
    const reglagesCourants = ETAT.reglages;
    resetEtatJeu();
    ETAT.reglages = reglagesCourants;
    ETAT.niveau = niveauChoisi;
    ETAT.equipe = equipeChoisie;
    ETAT.debut = Date.now();
    ETAT.salleDebut = Date.now();
    ETAT.msEcoules = 0;
    // Cinématique d'ouverture, si l'enseignant a fourni intro.mp4
    lancerCine("intro", "Paris, août 1789", ()=>entrerDansLeJeu(false));
  });
  // Boutons HUD (pause / reprendre / leçons / réglages)
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
    ETAT.salle = VERIF.salle;
    ETAT.debut = ETAT.salleDebut = Date.now();
    ETAT.msEcoules = 0;
    entrerDansLeJeu(false);
    toast("🔍 Mode vérification · " + VERIF.niveau + " · rien n'est sauvegardé");
    return;
  }

  // ===== Gestion de la reprise d'une partie en cours =====
  let partieEnCours = null;
  try{
    const s = localStorage.getItem(CLE_SAUVEGARDE);
    if(s){
      partieEnCours = JSON.parse(s);
    }
  }catch(e){}

  if(partieEnCours && partieEnCours.equipe && partieEnCours.debut && !partieEnCours.fini && partieEnCours.salle>=1 && partieEnCours.salle<=5){
    if(confirm("Une partie est en cours pour l'équipe « "+partieEnCours.equipe+" » (salle "+partieEnCours.salle+"/5).\nVoulez-vous la reprendre ?")){
      ETAT.equipe = partieEnCours.equipe;
      ETAT.niveau = partieEnCours.niveau || "CM2";
      ETAT.salle = partieEnCours.salle;
      ETAT.score = partieEnCours.score || 0;
      ETAT.fragments = partieEnCours.fragments || [];
      ETAT.badges = partieEnCours.badges || ETAT.badges;
      ETAT.msEcoules = partieEnCours.msEcoules || 0;
      ETAT.enigmesPremierCoup = partieEnCours.enigmesPremierCoup || 0;
      ETAT.erreursTotal = partieEnCours.erreursTotal || 0;
      ETAT.coffreOuvert = !!partieEnCours.coffreOuvert;
      ETAT.coffrePremierCoup = !!partieEnCours.coffrePremierCoup;
      ETAT.debut = Date.now() - ETAT.msEcoules;
      ETAT.fini = false;
      entrerDansLeJeu(true);
      return;
    }else{
      localStorage.removeItem(CLE_SAUVEGARDE);
    }
  }else if(partieEnCours && partieEnCours.fini){
    localStorage.removeItem(CLE_SAUVEGARDE);
  }
});

function verifierPret(){
  const ok = ETAT.equipe.length>=2 && ETAT.niveau;
  document.getElementById("btn-demarrer").disabled = !ok;
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
  // Ambiances & bruitages
  if(typeof setSonsActifs === "function"){
    setSonsActifs(ETAT.reglages.sonsActifs !== false);
  }
  if(typeof setVolumeSons === "function"){
    setVolumeSons(ETAT.reglages.volumeSons !== undefined ? ETAT.reglages.volumeSons : 0.55);
  }
  // Mode « animations réduites » (élèves sensibles au mouvement / postes lents)
  document.body.classList.toggle("calme", !!ETAT.reglages.animationsReduites);
  // ---- Multimédia (voir js/media.js) ----
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
  // Démarrer la synchronisation avec le serveur prof (si présent)
  if(!VERIF && typeof demarrerSync === "function") demarrerSync();
}

/* ============================================================
   AFFICHAGE DES SALLES
   ============================================================ */
function afficherSalle(n){
  const salle = DONNEES.salles[n-1];
  if(!salle) { finDuJeu(); return; }
  const c = document.getElementById("salle-contenu");
  ETAT.salleDebut = Date.now();
  ETAT.indicesUtilises = 0;

  // Libère la vidéo de la salle précédente avant de reconstruire
  if(typeof stopperVideos === "function") stopperVideos();

  c.innerHTML = `
    ${barreProgression()}
    <h2>📜 Salle ${salle.num} — ${salle.titre}</h2>
    ${htmlScene(salle.decor, salle)}
    <div class="consigne">${consigneSalle(n)}</div>
    <div class="zone-enigme">${enigmeSalle(n)}</div>
  `;
  // Activer les images IA si présentes
  activerScene(c.querySelector(".scene"));
  // Ambiance sonore du lieu + balayage de transition
  if(typeof son === "function") son("transition");
  if(typeof ambiance === "function") ambiance(salle.decor);
  // Lancer le dialogue d'intro animé
  // (si l'IA est activée, on tente une génération dynamique ; sinon, statique)
  lancerDialogueIntro(salle);
  // Activer les interactions de l'énigme
  activerEnigme(n);
  v2TairePersonnage(c.querySelector(".zone-enigme"));
  majHUD();
  sauvegarder();
}

async function lancerDialogueIntro(salle){
  let texte = salle.dialogue_intro.texte;
  // IA optionnelle : si activée et configurée, on tente une génération dynamique
  if(ETAT.reglages.apiActive && ETAT.reglages.apiCle && typeof genererDialogue === "function"){
    try{
      const gen = await genererDialogue({
        perso: salle.dialogue_intro.perso,
        situation: "Arrivée dans : "+salle.titre,
        niveau: ETAT.niveau,
        reussite: false
      });
      if(gen && gen.trim()) texte = gen;
    }catch(e){
      console.warn("IA échec, fallback statique:", e.message);
    }
  }
  afficherDialogue({
    perso: salle.dialogue_intro.perso,
    nom: salle.dialogue_intro.nom,
    texte: texte
  });
}

function consigneSalle(n){
  const cm1 = ETAT.niveau==="CM1";
  const consignes = {
    1: cm1
      ? "Lis le texte. Les lettres <b style='color:var(--rouge)'>en rouge</b> sont <b>dans le désordre</b> et <b>deux sont des pièges</b>. Range les bonnes dans les 7 cases : elles forment ce que réclament les habitants, un mot de la devise de la France."
      : "Lis le cahier de doléances. Neuf lettres sont marquées, <b>dans le désordre</b> ; <b>deux sont des pièges</b>. Range les autres dans les 7 cases pour écrire ce que réclament les habitants, un mot de la devise de la France.",
    2: cm1
      ? "Associe chaque extrait de la Marseillaise à l'image qui lui correspond (<b>3 paires</b>), puis clique sur « Vérifier »."
      : "Remets ces <b>5 événements de 1789</b> dans l'ordre chronologique (du plus ancien au plus récent) avec les flèches ▲▼, puis clique sur « Vérifier ».",
    3: "Déchiffre les <b>3 rébus</b> et choisis le bon mot pour compléter la phrase de la Déclaration.",
    4: "Associe chaque <b>portrait</b> à sa <b>citation</b>, puis clique sur « Vérifier ».",
    5: "Clique sur une <b>case</b> du plan, puis sur l'<b>étiquette</b> à y placer. Remplis tout le plan, puis clique sur « Vérifier ».",
  };
  return consignes[n] || "";
}

/* ---- Validation d'une salle (moteur v2) ----
   erreurs : nombre de vérifications fausses sur l'énigme de la salle.
   Aucun texte après la réussite : le fragment s'affiche une seule fois
   (à noter sur la fiche de mission) et le bouton suivant apparaît aussitôt. */
function validerSalle(n, erreurs){
  const salle = DONNEES.salles[n-1];
  const duree = Date.now() - ETAT.salleDebut;
  const dejaValidee = ETAT.tempsParSalle[n] !== undefined;   // reprise après rechargement
  ETAT.tempsParSalle[n] = duree;
  if(salle.fragment && !ETAT.fragments.includes(salle.fragment)){
    ETAT.fragments.push(salle.fragment);
    if(typeof son === "function") setTimeout(()=>son("fragment"), 600);
  }
  ajouterScore(erreurs ? PTS_APRES_ERREUR : PTS_PREMIER_COUP, erreurs ? "énigme résolue" : "tout juste du premier coup 🎯");
  let pts = 0;
  if(duree < 180000){ pts = 5; if(salle.badge_rapidite) ETAT.badges[salle.badge_rapidite] = true; }
  else if(duree < 360000){ pts = 2; }
  if(pts && !dejaValidee) setTimeout(()=>ajouterScore(pts, "rapidité 🏃"), 900);
  confettis(erreurs ? 15 : 45);

  const zoneEnigme = document.querySelector("#salle-contenu .zone-enigme");
  const dlg = document.querySelector("#salle-contenu .personnage-scene");
  if(dlg) dlg.remove();
  if("speechSynthesis" in window) speechSynthesis.cancel();

  // Salle 5 : le coffre final (recopier les 4 fragments notés), puis la fin
  if(n === 5){
    sauvegarder();
    const b = document.createElement("div");
    b.className = "boutons";
    b.innerHTML = `<button class="btn grand vert" id="btn-coffre-final">🔐 Ouvrir le coffre de l'article secret</button>`;
    zoneEnigme.appendChild(b);
    b.querySelector("button").addEventListener("click", ()=>afficherCoffre(()=>setTimeout(()=>lancerCine("final", "L'article secret", finDuJeu), 600)));
    b.scrollIntoView({behavior:"smooth", block:"center"});
    return;
  }

  zoneEnigme.innerHTML = v2MotANoter(`Fragment de la devise retrouvé dans la salle ${n}`, salle.fragment)
    + `<div class="boutons"><button class="btn grand vert" id="btn-salle-suivante">➡️ Salle suivante</button></div>`;
  zoneEnigme.querySelector("#btn-salle-suivante").addEventListener("click", ()=>{
    ETAT.salle++;
    if(ETAT.salle > 5) finDuJeu();
    else afficherSalle(ETAT.salle);
  });
  zoneEnigme.scrollIntoView({behavior:"smooth", block:"center"});
  sauvegarder();
}

/* ---- Coffre final : les 4 fragments notés sur la fiche de mission ---- */
function afficherCoffre(suite){
  if(ETAT.coffreOuvert){ suite(); return; }
  const zone = document.querySelector("#salle-contenu .zone-enigme");
  const lignes = DONNEES.salles.filter(s=>s.fragment).map(s=>({label:`Salle ${s.num} — ${s.titre}`, mot:s.fragment}));
  v2Coffre(zone, "Le coffre de l'article secret", lignes, (pts, premier)=>{
    ETAT.coffreOuvert = true;
    if(premier) ETAT.coffrePremierCoup = true;
    ajouterScore(pts, premier ? "coffre ouvert du premier coup 🎯" : "coffre ouvert");
    confettis(60);
    sauvegarder();
  }, suite);
}

/* ============================================================
   FIN DU JEU
   ============================================================ */
function finDuJeu(){
  ETAT.fini = true;
  if(typeof stopperVideos === "function") stopperVideos();
  aller("ecran-fin");
  // Bascule vers l'ambiance solennelle + fanfare de victoire
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
    <h2>🎉 Mission accomplie !</h2>
    <div id="fin-dialogue"></div>
    <div class="article-secret">
      <div class="sceau">🏛️</div>
      <div class="numero">ARTICLE 18 — SECRET</div>
      <div class="texte">« Nul ne peut être accusé, arrêté ni détenu que dans les cas déterminés par la Loi et selon les formes qu'elle a prescrites. »</div>
      <div style="font-size:.8rem;opacity:.7">Librement adapté de l'esprit de l'article 7 de la Déclaration de 1789.</div>
    </div>
    <div class="grille-badges">
      ${badgeHTML("bastille","🥖","Esprit de la Bastille","rapidité")}
      ${badgeHTML("avocat","⚖️","L'Avocat","raisonnement")}
      ${badgeHTML("fraternite","🤝","Fraternité","coopération")}
      ${badgeHTML("lumiere","📚","Lettre & Lumière","lecture")}
    </div>
    <p style="text-align:center;opacity:.8">⏱️ Temps total : <b>${min} min ${sec} s</b></p>
    <hr style="border:none;border-top:2px dotted var(--parchemin-ombre);margin:18px 0">
    <h2>📝 Quizz final — Valide tes acquis !</h2>
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
  // Dialogue final de Maximilien
  const finDialogue = DONNEES.salles[4].dialogue_fin;
  const oldConteneur = c;
  // Mini-hack : on utilise un conteneur temporaire pour le dialogue
  const dialDiv = document.createElement("div");
  oldConteneur.querySelector("#fin-dialogue").appendChild(dialDiv);
  // Forcer l'affichage du dialogue dans la zone prévue
  setTimeout(()=>{
    const scene = document.createElement("div");
    scene.className = "personnage-scene entrer";
    scene.innerHTML = `
      <div class="portrait">${htmlPortrait(finDialogue.perso)}</div>
      <div class="bulle"><div class="nom-perso">${finDialogue.nom}</div><div class="texte" id="fin-texte"></div></div>`;
    dialDiv.appendChild(scene);
    activerPortrait(scene.querySelector(".portrait-conteneur"));
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
  const gagne = ETAT.badges[cle];
  return `<div class="badge ${gagne?"gagne":""}">
    <div class="icone">${icone}</div>
    <div class="nom">${nom}</div>
    <div class="desc">${desc}</div>
  </div>`;
}

/* ============================================================
   QUIZZ FINAL
   ============================================================ */
const QUIZZ = [
  {q:"1. Quand a été adoptée la Déclaration des droits de l'homme et du citoyen ?",
   options:["14 juillet 1789","26 août 1789","21 janvier 1793"], bonne:1},
  {q:"2. Que signifie « liberté » dans la Déclaration ?",
   options:["Faire tout ce qu'on veut","Agir sans nuire aux droits des autres","Ne plus avoir de lois"], bonne:1},
  {q:"3. Qui prend la Bastille le 14 juillet 1789 ?",
   options:["Le roi et ses gardes","Le peuple parisien","L'armée anglaise"], bonne:1},
  {q:"4. Qu'est-ce qu'un « cahier de doléances » ?",
   options:["Un cahier d'écolier","Un texte où le peuple exprime ses plaintes au roi","Un journal intime"], bonne:1},
  {q:"5. Quel symbole représente l'égalité dans la Révolution ?",
   options:["La balance ⚖️","La couronne 👑","L'épée 🗡️"], bonne:0},
];

function construireQuizz(){
  const cont = document.getElementById("quizz");
  if(!cont) return;
  cont.innerHTML = QUIZZ.map((item,i)=>`
    <div class="qcm-question" data-i="${i}">
      <div class="q">${item.q}</div>
      ${item.options.map((o,j)=>`<label class="qcm-option" data-j="${j}"><input type="radio" name="q${i}" value="${j}" style="display:none">${o}</label>`).join("")}
    </div>
  `).join("");
  let repondu = Array(QUIZZ.length).fill(null);
  cont.querySelectorAll(".qcm-question").forEach(qi=>{
    const i = +qi.dataset.i;
    qi.querySelectorAll(".qcm-option").forEach(opt=>{
      opt.addEventListener("click", ()=>{
        qi.querySelectorAll(".qcm-option").forEach(x=>{x.classList.remove("select");x.classList.remove("bonne");x.classList.remove("mauvaise")});
        opt.classList.add("select");
        repondu[i] = +opt.dataset.j;
        if(repondu.every(r=>r!==null)){
          document.getElementById("quizz-actions").style.display="flex";
        }
      });
    });
  });
  const btnVoir = document.getElementById("btn-voir-score");
  if(btnVoir){
    btnVoir.onclick = ()=>{
      if(ETAT.quiz.repondu) return;   // quizz déjà compté : pas de points en double
      let score = 0;
      QUIZZ.forEach((item,i)=>{
        const qi = cont.querySelector(`.qcm-question[data-i="${i}"]`);
        qi.querySelectorAll(".qcm-option").forEach(opt=>{
          const j=+opt.dataset.j;
          opt.classList.remove("select");
          if(j===item.bonne) opt.classList.add("bonne");
          else if(j===repondu[i]) opt.classList.add("mauvaise");
        });
        if(repondu[i]===item.bonne) score++;
      });
      ETAT.quiz.repondu = true;
      ETAT.quiz.score = score;
      const pts = score*2;
      ETAT.score += pts;
      majHUD();
      const fb = document.getElementById("fb-quizz");
      fb.className = "feedback "+(score>=4?"succes":(score>=3?"indice":"erreur"))+" show";
      fb.innerHTML = `Tu as <b>${score}/${QUIZZ.length}</b> bonnes réponses (+${pts} points). ${
        score===5?"Parfait, tu es un véritable apprenti historien ! 🌟":
        score>=4?"Très bien ! Encore un petit effort.":
        score>=3?"Pas mal ! Révise les dates-clés de 1789.":"Relis bien la Déclaration et les événements de 1789."}`;
      const recap = document.getElementById("score-recap");
      recap.style.display="block";
      const min = Math.floor(ETAT.msEcoules/60000);
      const sec = Math.floor((ETAT.msEcoules%60000)/1000);
      const nbBadges = Object.values(ETAT.badges).filter(Boolean).length;
      let mention = "";
      if(ETAT.score>=0.9*SCORE_MAX) mention="🏆 Maître de la Révolution";
      else if(ETAT.score>=0.75*SCORE_MAX) mention="🥈 Patriote éclairé";
      else if(ETAT.score>=0.6*SCORE_MAX) mention="🥉 Bon citoyen";
      else mention="📜 Apprenti motivé";
      recap.innerHTML = `
        <div class="article-secret">
          <div class="sceau">🏁</div>
          <div class="numero">BILAN DE L'ÉQUIPE « ${ETAT.equipe.toUpperCase()} »</div>
          <div class="score-final">${ETAT.score}<span class="sur"> / ${SCORE_MAX}</span></div>
          <div style="font-size:1.1rem;color:var(--bleu-fonce);font-weight:bold">${mention}</div>
          <hr style="border:none;border-top:1px solid #c9b78a;margin:12px 0">
          <div>⏱️ Temps : <b>${min} min ${sec} s</b></div>
          <div>🎯 Justes du premier coup : <b>${ETAT.enigmesPremierCoup||0}/5</b> · ✗ Erreurs : <b>${ETAT.erreursTotal||0}</b></div>
          <div>📜 Fragments : <b>${ETAT.fragments.length}/4</b>${ETAT.coffreOuvert?" · coffre ouvert":""}</div>
          <div>📝 Quizz : <b>${ETAT.quiz.score}/${QUIZZ.length}</b></div>
          <div>🏅 Badges : <b>${nbBadges}/4</b></div>
          <div>Niveau : <b>${ETAT.niveau}</b></div>
        </div>`;
      recap.scrollIntoView({behavior:"smooth",block:"center"});
      confettis(60);
      sauvegarder();
    };
  }
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
window.SCORE_MAX = SCORE_MAX;
window.afficherCoffre = afficherCoffre;
