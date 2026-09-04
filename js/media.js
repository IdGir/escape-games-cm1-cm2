/* ============================================================
   MEDIA — Moteur multimédia du jeu
   ------------------------------------------------------------
   Rôle : décider CE QUI s'affiche derrière chaque décor, selon
   ce que l'enseignant a réellement déposé dans les dossiers.

   CASCADE (du plus riche au plus sobre) :
      1. une VIDÉO   assets/videos/etape1.mp4  (ou .webm)
      2. une IMAGE   assets/images/decors/etape1.jpg (ou .png/.webp)
      3. le SVG animé intégré au code  (toujours disponible)

   Le jeu est donc pleinement jouable SANS AUCUN FICHIER : la
   cascade retombe silencieusement sur les décors dessinés.

   Gère aussi :
     • les cinématiques plein écran (intro / épilogue)
     • le gel des vidéos (accessibilité, postes lents)
     • la coupure globale des décors filmés (réglage enseignant)
   ============================================================ */

/* ---- Note pour qui ouvre la console (F12) ----
   La détection des médias procède par essais : le navigateur signale en
   404 chaque nom de fichier absent. C'est NORMAL et sans conséquence —
   c'est ainsi que le jeu découvre ce que l'enseignant a déposé, puis
   retombe sur les décors dessinés. Aucune de ces erreurs n'empêche de
   jouer. Le bouton « Vérifier les fichiers présents » du module ⚙️
   affiche le résultat de cette détection en clair. */
console.info(
  "%c[médias] Les erreurs 404 qui suivent sont normales : " +
  "le jeu cherche vos vidéos/images et se rabat sur les décors dessinés.",
  "color:#c08a3e;font-weight:bold"
);

const MEDIA = {
  decorsVideo: true,      // réglage enseignant : décors filmés autorisés
  sonVideo: false,        // les décors sont MUETS par défaut (ne couvre pas les voix)
  figees: false,          // mode « animations réduites »
  cache: {},              // { "etape1": {type, src, poster} } — évite de re-sonder
  videosActives: [],      // <video> de décor actuellement dans le DOM
};

/* ---- Où chercher les fichiers, dans l'ordre de préférence ----
   Les deux derniers chemins pointent vers le dossier « Elements EG »
   du projet, pour que l'enseignant puisse y ranger ses médias
   au même endroit que ceux des autres escape games. */
const DOSSIERS_VIDEO = [
  "assets/videos/",
  "Elements EG/Revolution fr/",
];
const DOSSIERS_IMAGE = [
  "assets/images/decors/",
  "Elements EG/Revolution fr/",
];

/* ---- Noms alternatifs acceptés pour chaque salle ----
   Permet d'utiliser un fichier déjà nommé autrement (par exemple la
   vidéo « Paris 1789.mp4 » livrée avec le projet) sans avoir à le
   renommer. Le premier nom trouvé l'emporte. */
const ALIAS = {
  salle1: ["salle1", "Paris 1789", "palais-royal"],
  salle2: ["salle2", "imprimerie"],
  salle3: ["salle3", "tuileries"],
  salle4: ["salle4", "bastille"],
  salle5: ["salle5", "assemblee"],
};
const EXT_VIDEO = [".mp4", ".webm"];
const EXT_IMAGE = [".jpg", ".png", ".webp", ".jpeg"];
/* .gif accepte pour les personnages : une animation bouclee toute simple */
const EXT_IMAGE_PERSO = [".png", ".gif", ".webp", ".jpg", ".jpeg"];

/* ---- PERSONNAGES ----
   Un personnage peut etre :
     - une VIDEO  assets/videos/personnages/fogg.mp4
       (+ eventuellement fogg-parle.mp4, jouee pendant qu'il parle)
     - une IMAGE  assets/images/personnages/fogg.png (ou .gif anime)
     - le personnage SVG plein corps dessine dans js/personnages.js */
const DOSSIERS_PERSO_VIDEO = [
  "assets/videos/personnages/",
  "assets/videos/",
  "Elements EG/Revolution fr/personnages/",
];
const DOSSIERS_PERSO_IMAGE = [
  "assets/images/personnages/",
  "Elements EG/Revolution fr/personnages/",
];

/* ---- CARTES ET ILLUSTRATIONS ----
   Planispheres, paysages, croquis, photos de documents... Toujours
   facultatifs : sans fichier, le jeu garde ses dessins et ses emojis. */
const DOSSIERS_CARTE = [
  "assets/images/cartes/",
  "Elements EG/Revolution fr/cartes/",
];
const DOSSIERS_DOCUMENT = [
  "assets/images/documents/",
  "Elements EG/Revolution fr/documents/",
];

/* Délai maximal accordé à une sonde avant de passer à la suite.
   Court : on ne fait jamais attendre une classe entière. */
const DELAI_SONDE = 2500;

/* ---- Sonder l'existence d'une image ---- */
function sonderImage(url){
  return new Promise(resolve=>{
    const img = new Image();
    let fini = false;
    const stop = ok => { if(!fini){ fini = true; resolve(ok ? url : null); } };
    img.onload  = ()=>stop(img.naturalWidth > 0);
    img.onerror = ()=>stop(false);
    setTimeout(()=>stop(false), DELAI_SONDE);
    img.src = url;
  });
}

/* ---- Sonder l'existence d'une vidéo ----
   On ne charge que les métadonnées : aucun téléchargement inutile. */
function sonderVideo(url){
  return new Promise(resolve=>{
    const v = document.createElement("video");
    let fini = false;
    const stop = ok => {
      if(fini) return;
      fini = true;
      v.removeAttribute("src");
      try{ v.load(); }catch(e){}
      resolve(ok ? url : null);
    };
    v.preload = "metadata";
    v.muted = true;
    v.onloadedmetadata = ()=>stop(v.videoWidth > 0 || v.duration > 0);
    v.onerror = ()=>stop(false);
    setTimeout(()=>stop(false), DELAI_SONDE);
    v.src = url;
  });
}

/* ---- Première URL qui répond, parmi une liste de candidats ---- */
async function premierePresente(candidats, sonde){
  for(const url of candidats){
    const trouve = await sonde(url);
    if(trouve) return trouve;
  }
  return null;
}

/* ---- Construire la liste des candidats pour un nom de base ---- */
function candidats(base, dossiers, extensions){
  const liste = [];
  const noms = ALIAS[base] || [base];
  for(const n of noms){
    for(const d of dossiers){
      for(const e of extensions){
        // encodeURI : le dossier « Elements EG » contient une espace
        liste.push(encodeURI(d + n + e));
      }
    }
  }
  return liste;
}

/* ============================================================
   RÉSOLUTION D'UN DÉCOR
   @param {string} base — ex. "etape1"
   @returns {Promise<{type:'video'|'image'|'svg', src, poster}>}
   ============================================================ */
async function resoudreDecor(base){
  if(MEDIA.cache[base]) return MEDIA.cache[base];

  // L'image sert aussi de POSTER à la vidéo (première frame nette,
  // affichée pendant le chargement et à l'impression).
  const image = await premierePresente(candidats(base, DOSSIERS_IMAGE, EXT_IMAGE), sonderImage);

  let resultat;
  if(MEDIA.decorsVideo){
    const video = await premierePresente(candidats(base, DOSSIERS_VIDEO, EXT_VIDEO), sonderVideo);
    if(video){
      resultat = {type:"video", src:video, poster:image};
    }
  }
  if(!resultat) resultat = image ? {type:"image", src:image, poster:image}
                                 : {type:"svg", src:null, poster:null};

  MEDIA.cache[base] = resultat;
  return resultat;
}

/* ============================================================
   RESOLUTION D'UN PERSONNAGE
   @param {string} perso - ex. "fogg"
   @returns {Promise<{type:'video'|'image'|'svg', src, srcParle}>}
   ============================================================ */
async function resoudrePersonnage(perso){
  const cle = "perso:" + perso;
  if(MEDIA.cache[cle]) return MEDIA.cache[cle];

  let resultat = null;

  if(MEDIA.decorsVideo){
    const repos = await premierePresente(
      candidats(perso, DOSSIERS_PERSO_VIDEO, EXT_VIDEO), sonderVideo);
    if(repos){
      // Variante "en train de parler", facultative
      const parle = await premierePresente(
        candidats(perso + "-parle", DOSSIERS_PERSO_VIDEO, EXT_VIDEO), sonderVideo);
      resultat = {type:"video", src:repos, srcParle:parle};
    }
  }
  if(!resultat){
    const image = await premierePresente(
      candidats(perso, DOSSIERS_PERSO_IMAGE, EXT_IMAGE_PERSO), sonderImage);
    resultat = image ? {type:"image", src:image, srcParle:null}
                     : {type:"svg", src:null, srcParle:null};
  }

  MEDIA.cache[cle] = resultat;
  return resultat;
}

/* ============================================================
   INSTALLER UN PERSONNAGE
   C'est le nouveau activerPortrait() : le personnage dessine est
   deja a l'ecran, on le surclasse seulement si un media existe.
   @param {HTMLElement} conteneur - le .portrait-conteneur
   ============================================================ */
async function installerPersonnage(conteneur){
  if(!conteneur) return;
  const perso = conteneur.dataset.perso;
  if(!perso) return;

  const media = await resoudrePersonnage(perso);
  if(!conteneur.isConnected || media.type === "svg") return;

  const svg = conteneur.querySelector(".portrait-svg");
  const img = conteneur.querySelector(".portrait-img-cachee");

  if(media.type === "image"){
    if(!img) return;
    img.src = media.src;
    img.style.display = "block";
    if(svg) svg.style.display = "none";
    return;
  }

  /* ---- Personnage filme ----
     Deux boucles superposees : au repos et en train de parler. Le
     basculement est purement CSS, pilote par la classe .parle que
     narration.js pose deja sur le .portrait (voir css/video.css). */
  if(conteneur.querySelector(".perso-video")) return;   // deja installe

  const faire = (src, variante)=>{
    const v = document.createElement("video");
    v.className = "perso-video perso-video--" + variante;
    v.src = src;
    v.muted = true;          // la voix vient de la synthese vocale
    v.loop = true;
    v.playsInline = true;
    v.setAttribute("playsinline", "");
    v.setAttribute("aria-hidden", "true");
    v.preload = "auto";
    v.disablePictureInPicture = true;
    conteneur.appendChild(v);
    MEDIA.videosActives.push(v);
    if(!MEDIA.figees){ const p = v.play(); if(p && p.catch) p.catch(()=>{}); }
    return v;
  };

  const repos = faire(media.src, "repos");
  repos.addEventListener("error", ()=>{
    // Fichier illisible : on revient au personnage dessine
    conteneur.querySelectorAll(".perso-video").forEach(x=>x.remove());
    conteneur.classList.remove("perso-filme");
    if(svg) svg.style.display = "block";
  }, {once:true});

  if(media.srcParle) faire(media.srcParle, "parle");

  if(svg) svg.style.display = "none";
  if(img) img.style.display = "none";
  conteneur.classList.add("perso-filme");
}

/* ============================================================
   CARTES, PAYSAGES ET DOCUMENTS (images facultatives)
   ============================================================ */

/** URL de l'illustration si elle existe, sinon null. */
async function resoudreIllustration(base, dossiers){
  const cle = dossiers[0] + base;
  if(MEDIA.cache[cle] !== undefined) return MEDIA.cache[cle];
  const url = await premierePresente(candidats(base, dossiers, EXT_IMAGE), sonderImage);
  MEDIA.cache[cle] = url;
  return url;
}
const resoudreCarte       = base => resoudreIllustration(base, DOSSIERS_CARTE);
const resoudreDocumentImg = base => resoudreIllustration(base, DOSSIERS_DOCUMENT);

/**
 * Pose une image de fond dans un conteneur, SI le fichier existe.
 * Sert au planisphere, aux croquis, aux fonds de carte.
 */
async function poserFondCarte(hote, base, classe){
  if(!hote) return false;
  const url = await resoudreCarte(base);
  if(!url || !hote.isConnected) return false;
  if(hote.querySelector("." + classe)) return true;
  const img = document.createElement("img");
  img.className = classe;
  img.src = url;
  img.alt = "";
  img.setAttribute("aria-hidden", "true");
  hote.insertBefore(img, hote.firstChild);
  hote.classList.add("a-fond-image");
  return true;
}

/**
 * Remplace le contenu d'une vignette (un emoji) par une image, si
 * l'enseignant en a depose une. Sinon l'emoji reste.
 */
async function illustrerVignette(vignette, base){
  if(!vignette) return false;
  const url = await resoudreCarte(base);
  if(!url || !vignette.isConnected) return false;
  const img = document.createElement("img");
  img.className = "vignette-image";
  img.src = url;
  img.alt = "";
  vignette.innerHTML = "";
  vignette.appendChild(img);
  vignette.classList.add("vignette--illustree");
  return true;
}

/**
 * HTML d'une illustration de lecon (carte, gravure, photo).
 * L'image se retire d'elle-meme si le fichier n'existe pas, en
 * laissant un encadre qui indique ou le deposer.
 */
function htmlIllustration(base, legende, source){
  const url = encodeURI("assets/images/cartes/" + base + ".jpg");
  return `
    <figure class="illustration" data-base="${base}">
      <img src="${url}" alt="${legende||""}"
           onerror="this.closest('.illustration').classList.add('absente');this.remove()">
      <div class="illustration-absente">
        Illustration facultative &mdash; deposez <code>${base}.jpg</code>
        dans <code>assets/images/cartes/</code>
      </div>
      ${legende?`<figcaption>${legende}${source?`<span class="source">${source}</span>`:""}</figcaption>`:""}
    </figure>`;
}

/* ============================================================
   INSTALLER LE DÉCOR DANS UNE SCÈNE
   La scène est d'abord rendue avec son SVG (affichage immédiat,
   zéro attente), puis surclassée si un média est trouvé.
   ============================================================ */
async function installerDecor(sceneEl, base){
  if(!sceneEl) return;
  const media = await resoudreDecor(base);
  // La scène a pu être remplacée entre-temps (changement d'étape rapide)
  if(!sceneEl.isConnected) return;

  const fallback = sceneEl.querySelector(".decor-fallback");

  if(media.type === "svg"){
    marquerSource(sceneEl, "décor dessiné");
    return; // le SVG est déjà en place
  }

  if(media.type === "image"){
    const img = document.createElement("img");
    img.className = "decor-img";
    img.src = media.src;
    img.alt = "";
    img.setAttribute("aria-hidden", "true");
    sceneEl.insertBefore(img, sceneEl.firstChild);
    if(fallback) fallback.style.display = "none";
    marquerSource(sceneEl, "décor illustré");
    return;
  }

  /* ---- Décor filmé ---- */
  const v = document.createElement("video");
  v.className = "decor-video";
  v.dataset.pret = "non";
  v.src = media.src;
  if(media.poster) v.poster = media.poster;
  v.muted = !MEDIA.sonVideo;   // muet : la vidéo ne couvre jamais les voix
  v.loop = true;
  v.playsInline = true;
  v.setAttribute("playsinline", "");   // iOS
  v.setAttribute("aria-hidden", "true");
  v.preload = "auto";
  v.disablePictureInPicture = true;

  v.addEventListener("loadeddata", ()=>{
    v.dataset.pret = "oui";
    if(fallback) fallback.style.display = "none";
  }, {once:true});

  // Si le fichier casse en cours de route, on retombe sur le SVG
  v.addEventListener("error", ()=>{
    v.remove();
    if(fallback) fallback.style.display = "block";
    marquerSource(sceneEl, "décor dessiné");
  }, {once:true});

  sceneEl.insertBefore(v, sceneEl.firstChild);
  MEDIA.videosActives.push(v);
  marquerSource(sceneEl, "décor filmé");
  ajouterCommandesScene(sceneEl, v);

  if(MEDIA.figees){
    v.pause();
  }else{
    // Les navigateurs refusent parfois l'autoplay : on échoue en silence,
    // le poster reste affiché et le bouton ▶ permet de lancer la lecture.
    const p = v.play();
    if(p && p.catch) p.catch(()=>{ /* autoplay bloqué : poster affiché */ });
  }
}

/* ---- Pastille indiquant la source du décor (repère enseignant) ---- */
function marquerSource(sceneEl, libelle){
  let p = sceneEl.querySelector(".pastille-media");
  if(!p){
    p = document.createElement("div");
    p.className = "pastille-media";
    sceneEl.appendChild(p);
  }
  p.textContent = libelle;
}

/* ---- Boutons de contrôle du décor filmé ---- */
function ajouterCommandesScene(sceneEl, video){
  if(sceneEl.querySelector(".scene-commandes")) return;
  const box = document.createElement("div");
  box.className = "scene-commandes";
  box.innerHTML = `
    <button type="button" data-act="lecture" title="Figer / animer le décor" aria-label="Figer ou animer le décor">⏸</button>
    <button type="button" data-act="son" title="Son du décor" aria-label="Activer ou couper le son du décor">🔇</button>
  `;
  sceneEl.appendChild(box);

  const btnLecture = box.querySelector('[data-act="lecture"]');
  const btnSon     = box.querySelector('[data-act="son"]');

  btnLecture.addEventListener("click", ()=>{
    if(video.paused){
      video.play().catch(()=>{});
      btnLecture.textContent = "⏸";
    }else{
      video.pause();
      btnLecture.textContent = "▶";
    }
  });
  btnSon.addEventListener("click", ()=>{
    video.muted = !video.muted;
    btnSon.textContent = video.muted ? "🔇" : "🔊";
  });
  if(video.paused) btnLecture.textContent = "▶";
}

/* ============================================================
   CINÉMATIQUE PLEIN ÉCRAN
   @param {object} opts
     - base       : nom du fichier sans extension (ex. "intro")
     - titre      : bandeau affiché en haut
     - replique   : texte de secours affiché SI aucune vidéo n'existe
     - onFin      : callback appelé à la fin (ou au « Passer »)
   Si aucun fichier vidéo n'est trouvé, la cinématique est
   simplement SAUTÉE : onFin est appelé immédiatement.
   ============================================================ */
async function jouerCinematique(opts){
  const {base, titre, onFin} = opts;
  const fin = ()=>{ if(typeof onFin === "function") onFin(); };

  if(!MEDIA.decorsVideo){ fin(); return; }

  const url = await premierePresente(candidats(base, DOSSIERS_VIDEO, EXT_VIDEO), sonderVideo);
  if(!url){ fin(); return; }   // pas de vidéo : on enchaîne sans rien dire

  const overlay = document.getElementById("overlay-cine");
  if(!overlay){ fin(); return; }

  const posterUrl = await premierePresente(candidats(base, DOSSIERS_IMAGE, EXT_IMAGE), sonderImage);
  const pisteVtt  = encodeURI("assets/videos/" + base + ".vtt");

  overlay.innerHTML = `
    <div class="cine" role="dialog" aria-modal="true" aria-label="${titre||"Séquence vidéo"}">
      <div class="cine-titre">${titre||""}</div>
      <video id="cine-video" playsinline ${posterUrl?`poster="${posterUrl}"`:""}>
        <source src="${url}">
        <track kind="subtitles" srclang="fr" label="Français" src="${pisteVtt}" default>
      </video>
      <div class="cine-barre">
        <button type="button" id="cine-play" aria-label="Pause">⏸ Pause</button>
        <div class="progression-cine"><i id="cine-progres"></i></div>
        <button type="button" id="cine-son" aria-label="Couper le son">🔊 Son</button>
        <button type="button" id="cine-passer">⏭ Passer</button>
      </div>
    </div>
  `;
  overlay.classList.add("show");

  const v        = overlay.querySelector("#cine-video");
  const progres  = overlay.querySelector("#cine-progres");
  const btnPlay  = overlay.querySelector("#cine-play");
  const btnSon   = overlay.querySelector("#cine-son");
  const btnPasser= overlay.querySelector("#cine-passer");

  let termine = false;
  function fermer(){
    if(termine) return;
    termine = true;
    try{ v.pause(); }catch(e){}
    overlay.classList.remove("show");
    overlay.innerHTML = "";
    document.removeEventListener("keydown", surTouche);
    fin();
  }
  function surTouche(e){
    if(e.key === "Escape") fermer();
    if(e.key === " "){ e.preventDefault(); btnPlay.click(); }
  }

  v.addEventListener("timeupdate", ()=>{
    if(v.duration) progres.style.width = (v.currentTime / v.duration * 100) + "%";
  });
  v.addEventListener("ended", fermer);
  v.addEventListener("error", fermer);
  btnPasser.addEventListener("click", fermer);
  btnPlay.addEventListener("click", ()=>{
    if(v.paused){ v.play().catch(()=>{}); btnPlay.textContent = "⏸ Pause"; }
    else       { v.pause();               btnPlay.textContent = "▶ Lire"; }
  });
  btnSon.addEventListener("click", ()=>{
    v.muted = !v.muted;
    btnSon.textContent = v.muted ? "🔇 Muet" : "🔊 Son";
  });
  document.addEventListener("keydown", surTouche);

  // Une cinématique a du SON (c'est une narration) : on tente avec le son,
  // et on bascule en muet si le navigateur refuse l'autoplay sonore.
  v.muted = false;
  try{
    await v.play();
  }catch(e){
    v.muted = true;
    btnSon.textContent = "🔇 Muet";
    try{ await v.play(); }catch(e2){ /* l'élève cliquera sur ▶ */ }
  }
}

/* ============================================================
   VIDÉO DOCUMENT (leçons)
   Retourne le HTML d'un lecteur, ou un encadré « où déposer
   le fichier » si l'enseignant n'a rien fourni.
   ============================================================ */
function htmlVideoDoc(base, titre, source){
  const url = encodeURI("assets/videos/" + base + ".mp4");
  return `
    <div class="video-doc" data-base="${base}">
      <video controls preload="none" playsinline poster="${encodeURI("assets/images/decors/"+base+".jpg")}">
        <source src="${url}" type="video/mp4">
        <track kind="subtitles" srclang="fr" label="Français" src="${encodeURI("assets/videos/"+base+".vtt")}">
      </video>
      <div class="legende">
        <b>${titre||""}</b>
        ${source?`<span class="source">${source}</span>`:""}
      </div>
    </div>`;
}

/* Emplacement documenté quand aucun fichier n'existe encore */
function htmlVideoAbsente(base){
  return `
    <div class="video-absente">
      <span class="grosse-icone">🎬</span>
      <div>Aucune vidéo pour cette étape.</div>
      <div>Déposez un fichier nommé <code>${base}.mp4</code> dans <code>assets/videos/</code></div>
    </div>`;
}

/* ============================================================
   RÉGLAGES (appelés depuis le module enseignant)
   ============================================================ */
function setDecorsVideo(actif){
  MEDIA.decorsVideo = !!actif;
  document.body.classList.toggle("sans-video", !actif);
  if(!actif) stopperVideos();
}
function setFigerVideos(figees){
  MEDIA.figees = !!figees;
  MEDIA.videosActives.forEach(v=>{
    if(!v.isConnected) return;
    if(figees) v.pause();
    else v.play().catch(()=>{});
  });
}
function setSonVideo(actif){
  MEDIA.sonVideo = !!actif;
  MEDIA.videosActives.forEach(v=>{ if(v.isConnected) v.muted = !actif; });
}
function stopperVideos(){
  MEDIA.videosActives.forEach(v=>{ try{ v.pause(); v.remove(); }catch(e){} });
  MEDIA.videosActives = [];
}
/* Nettoyage : appelé avant chaque changement d'étape */
function nettoyerVideos(){
  MEDIA.videosActives = MEDIA.videosActives.filter(v=>{
    if(v.isConnected) return true;
    try{ v.pause(); v.removeAttribute("src"); v.load(); }catch(e){}
    return false;
  });
}

/* Économie de batterie / CPU : on gèle les décors quand l'onglet
   passe en arrière-plan (le prof bascule sur son diaporama…). */
document.addEventListener("visibilitychange", ()=>{
  if(document.hidden){
    MEDIA.videosActives.forEach(v=>{ if(v.isConnected) v.pause(); });
  }else if(!MEDIA.figees){
    MEDIA.videosActives.forEach(v=>{ if(v.isConnected) v.play().catch(()=>{}); });
  }
});

/* activerPortrait() est le nom historique attendu par narration.js et par
   l'ecran d'accueil : il pointe desormais sur la cascade personnage. */
window.activerPortrait      = installerPersonnage;
window.installerPersonnage  = installerPersonnage;
window.resoudrePersonnage   = resoudrePersonnage;
window.resoudreCarte        = resoudreCarte;
window.resoudreDocumentImg  = resoudreDocumentImg;
window.poserFondCarte       = poserFondCarte;
window.illustrerVignette    = illustrerVignette;
window.htmlIllustration     = htmlIllustration;

window.MEDIA = MEDIA;
window.resoudreDecor = resoudreDecor;
window.installerDecor = installerDecor;
window.jouerCinematique = jouerCinematique;
window.htmlVideoDoc = htmlVideoDoc;
window.htmlVideoAbsente = htmlVideoAbsente;
window.setDecorsVideo = setDecorsVideo;
window.setFigerVideos = setFigerVideos;
window.setSonVideo = setSonVideo;
window.stopperVideos = stopperVideos;
window.nettoyerVideos = nettoyerVideos;
