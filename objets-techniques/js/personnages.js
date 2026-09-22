/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés
   ------------------------------------------------------------
   RIG (classes réutilisées par css/animations.css) :
     .tete .yeux .paupiere .bouche .sourcils   → lip-sync
     .buste                                    → respiration
     .bras-g / .bras-d  .avant-g / .avant-d    → épaule / coude
     .main-g  / .main-d                        → mains
     .jambes                                   → appui

   Gestes pilotés par des classes posées sur .portrait :
     .parle · .geste-pointe · .geste-joie · .geste-inquiet · .geste-salue

   Cascade d'affichage (voir js/media.js) :
     VIDÉO assets/videos/personnages/<nom>.mp4
   → IMAGE assets/images/personnages/<nom>.png
   → SVG dessiné ci-dessous
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.zoe;
}

/** HTML complet d'un personnage (image si présente, sinon SVG). */
function htmlPersonnage(perso){
  const src = `assets/images/personnages/${perso}.png`;
  const svg = svgPersonnage(perso);
  return `
    <div class="portrait-conteneur perso-plein-conteneur" data-perso="${perso}">
      <img src="${src}" alt="${perso}" class="portrait-img-cachee"
           onerror="this.style.display='none';this.parentElement.querySelector('.portrait-svg').style.display='block'"
           style="display:none">
      <div class="portrait-svg" style="display:block">${svg}</div>
    </div>`;
}

/** Version de base : media.js la remplace par la cascade vidéo/image. */
function activerPortraitBase(conteneur){
  if(!conteneur) return;
  const img = conteneur.querySelector(".portrait-img-cachee");
  const svg = conteneur.querySelector(".portrait-svg");
  if(!img || !svg) return;
  const test = new Image();
  test.onload = ()=>{ img.style.display="block"; svg.style.display="none"; };
  test.src = img.src;
}

/* ---- Fragments réutilisés : un visage complet ----
   idPeau : identifiant du dégradé de peau déjà déclaré dans <defs>. */
function visage({idPeau, oeil="#3a2a1a", sourcil="#3a2a1a", joue=".35", nez="#c89a70", bouche="#a8434a", levre="#8d3a40"}){
  return `
      <ellipse cx="100" cy="86" rx="31" ry="36" fill="url(#${idPeau})"/>
      <ellipse cx="82" cy="97" rx="8" ry="5" fill="#e79a97" opacity="${joue}"/>
      <ellipse cx="118" cy="97" rx="8" ry="5" fill="#e79a97" opacity="${joue}"/>
      <g class="sourcils">
        <path d="M82 74 Q88 70 94 74" stroke="${sourcil}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
        <path d="M106 74 Q112 70 118 74" stroke="${sourcil}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      </g>
      <g class="yeux">
        <ellipse cx="88" cy="83" rx="6" ry="4.6" fill="#fff"/>
        <ellipse cx="112" cy="83" rx="6" ry="4.6" fill="#fff"/>
        <circle cx="88" cy="83" r="3" fill="${oeil}"/>
        <circle cx="112" cy="83" r="3" fill="${oeil}"/>
        <circle cx="89.2" cy="81.8" r="1.1" fill="#fff"/>
        <circle cx="113.2" cy="81.8" r="1.1" fill="#fff"/>
        <ellipse class="paupiere" cx="88" cy="83" rx="6.3" ry="4.9" fill="url(#${idPeau})"/>
        <ellipse class="paupiere" cx="112" cy="83" rx="6.3" ry="4.9" fill="url(#${idPeau})"/>
      </g>
      <path d="M100 88 Q97 95 101 97" stroke="${nez}" stroke-width="2" fill="none" stroke-linecap="round"/>
      <ellipse class="bouche bouche-ouverte" cx="100" cy="107" rx="7" ry="4" fill="${bouche}"/>
      <path class="bouche-fermee" d="M93 107 Q100 110 107 107" stroke="${levre}" stroke-width="2" fill="none" stroke-linecap="round"/>`;
}

/* ============================================================
   BIBLIOTHÈQUE DES PERSONNAGES — viewBox 200 × 320
   Un gabarit commun (corpsPerso) : jambes, bras articulés, buste,
   tête ; chaque personnage lui passe ses couleurs, sa coiffure et
   son accessoire. Les classes du rig restent celles de css/animations.css.
   ============================================================ */
function corpsPerso(o){
  const id = o.id;
  return `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet" role="img" aria-label="${o.nom}">
  <defs>
    <radialGradient id="fond${id}" cx="50%" cy="32%" r="78%">
      <stop offset="0%" stop-color="${o.fond[0]}"/><stop offset="100%" stop-color="${o.fond[1]}"/>
    </radialGradient>
    <linearGradient id="peau${id}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${o.peau[0]}"/><stop offset="100%" stop-color="${o.peau[1]}"/>
    </linearGradient>
    <linearGradient id="haut${id}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${o.haut[0]}"/><stop offset="100%" stop-color="${o.haut[1]}"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fond${id})"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M75 212 L70 292 L90 292 L94 212 Z" fill="${o.bas}"/>
      <path d="M106 212 L110 292 L130 292 L125 212 Z" fill="${o.bas}"/>
      <ellipse cx="80" cy="298" rx="16" ry="7" fill="${o.chaussures}"/>
      <ellipse cx="120" cy="298" rx="16" ry="7" fill="${o.chaussures}"/>
    </g>
    <g class="bras bras-g">
      <path d="M69 152 Q56 180 52 207" stroke="url(#haut${id})" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M52 207 Q50 223 54 237" stroke="url(#haut${id})" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="55" cy="243" r="9" fill="url(#peau${id})"/>
        ${o.mainG||""}
      </g>
    </g>
    <g class="buste">
      <path d="M69 150 Q67 133 80 127 L120 127 Q133 133 131 150 L135 215 Q100 223 65 215 Z" fill="url(#haut${id})"/>
      <path d="M90 118 L110 118 L110 133 Q100 139 90 133 Z" fill="${o.peau[1]}"/>
      ${o.buste||""}
    </g>
    <g class="bras bras-d">
      <path d="M131 152 Q145 178 149 205" stroke="url(#haut${id})" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M149 205 Q151 221 147 235" stroke="url(#haut${id})" stroke-width="13" fill="none" stroke-linecap="round"/>
        <g class="main-d"><circle cx="146" cy="241" r="9.5" fill="url(#peau${id})"/>${o.mainD||""}</g>
      </g>
    </g>
    <g class="tete">
      ${o.cheveuxArriere||""}
      ${visage({idPeau:"peau"+id, oeil:o.oeil||"#2e1c10", sourcil:o.sourcil||"#2a1608", nez:o.nez||"#b07a4e"})}
      ${o.cheveuxAvant||""}
      ${o.tete||""}
    </g>
  </g>
</svg>`;
}

const SVG_PERSOS = {

/* ZOÉ — 11 ans, apprentie ingénieure : salopette, lunettes de protection sur le front, carnet */
zoe: corpsPerso({id:"Zo", nom:"Zoé", fond:["#2f6f7a","#0e2a30"], peau:PEAU.claire, haut:["#3f7fbf","#2a5a8c"], bas:"#2a5a8c", chaussures:"#e8e4dc",
  oeil:"#3a5a2a", sourcil:"#8a4b1c",
  buste:`<rect x="82" y="150" width="36" height="30" rx="4" fill="#2a5a8c" stroke="#1b3f63"/><rect x="94" y="158" width="12" height="10" rx="2" fill="#f2c94c"/>
         <path d="M82 150 L78 130 M118 150 L122 130" stroke="#1b3f63" stroke-width="4"/>`,
  mainG:`<g transform="translate(55,252)"><rect x="-10" y="-6" width="20" height="26" rx="2" fill="#f4e9d0" stroke="#8a6d12"/><line x1="-6" y1="2" x2="6" y2="2" stroke="#999"/><line x1="-6" y1="8" x2="6" y2="8" stroke="#999"/></g>`,
  cheveuxArriere:`<path d="M64 84 Q60 36 100 34 Q140 36 136 84 L140 128 Q128 118 130 96 L70 96 Q72 118 60 128 Z" fill="#b5651d"/>`,
  cheveuxAvant:`<path d="M68 70 Q100 44 132 70 Q120 58 100 58 Q80 58 68 70" fill="#b5651d"/>`,
  tete:`<g><rect x="72" y="52" width="56" height="12" rx="6" fill="#444"/><circle cx="88" cy="58" r="7" fill="#9fd3e6" stroke="#333" stroke-width="2"/><circle cx="112" cy="58" r="7" fill="#9fd3e6" stroke="#333" stroke-width="2"/></g>`}),

/* AWA — ouvrière de l'atelier : bleu de travail, foulard, clé plate */
awa: corpsPerso({id:"Aw", nom:"Awa", fond:["#5a4a32","#18130d"], peau:PEAU.foncee, haut:["#2f4f7f","#1d3557"], bas:"#1d3557", chaussures:"#2b2118",
  oeil:"#1a0f08", sourcil:"#140a04", nez:"#5a3418",
  buste:`<rect x="112" y="150" width="14" height="18" rx="2" fill="#1d3557" stroke="#0f213a"/><path d="M100 128 L100 214" stroke="#0f213a" stroke-width="2"/>`,
  mainD:`<g transform="translate(150,244) rotate(-30)"><rect x="-3" y="-2" width="6" height="34" rx="2" fill="#9aa4ad"/><path d="M-9 -2 L-3 -12 L3 -12 L9 -2 L4 -2 L0 -8 L-4 -2 Z" fill="#9aa4ad"/></g>`,
  cheveuxArriere:`<ellipse cx="100" cy="60" rx="38" ry="30" fill="#1a1a1a"/>`,
  cheveuxAvant:`<path d="M62 70 Q100 30 138 70 L138 60 Q100 20 62 60 Z" fill="#e0a800"/><path d="M62 64 Q100 50 138 64" stroke="#c0392b" stroke-width="3" fill="none"/>`}),

/* MONSIEUR MARCEL — réparateur de vélos : casquette, moustache blanche, tablier, chambre à air */
marcel: corpsPerso({id:"Ma", nom:"Monsieur Marcel", fond:["#4f6a3a","#141d0d"], peau:PEAU.pale, haut:["#8a6440","#5c4127"], bas:"#3a3a3a", chaussures:"#1c1a17",
  oeil:"#3a4a5a", sourcil:"#dcdcdc", nez:"#c48f5e",
  buste:`<path d="M78 140 L122 140 L126 214 L74 214 Z" fill="#3e4a52"/><rect x="92" y="170" width="16" height="12" rx="2" fill="#2b3338"/>`,
  mainG:`<circle cx="55" cy="262" r="16" fill="none" stroke="#1d1d1d" stroke-width="5"/>`,
  cheveuxArriere:`<path d="M66 90 Q64 70 70 64 L130 64 Q136 70 134 90 Q132 76 124 74 L76 74 Q68 76 66 90" fill="#dcdcdc"/>`,
  tete:`<path d="M66 66 Q100 36 134 66 Z" fill="#2f4f3a"/><path d="M62 66 L148 66 L150 72 L62 72 Z" fill="#23392b"/>
        <path d="M86 100 Q100 94 114 100 Q106 106 100 102 Q94 106 86 100" fill="#e8e8e8"/>`}),

/* ÉLÉONORE MARCHAND — l'inventrice : blouse claire, chignon, crayon sur l'oreille, carnet de croquis */
eleonore: corpsPerso({id:"El", nom:"Éléonore Marchand", fond:["#6b3a5a","#1f0f1a"], peau:PEAU.hale, haut:["#f2efe6","#d8d2c2"], bas:"#4a3a5a", chaussures:"#6e2c10",
  oeil:"#2e1c10", sourcil:"#3a2210",
  buste:`<path d="M84 128 L100 160 L116 128" fill="none" stroke="#b8b09a" stroke-width="2"/><rect x="110" y="160" width="14" height="16" rx="2" fill="#d8d2c2" stroke="#b8b09a"/>
         <line x1="113" y1="156" x2="113" y2="170" stroke="#c0392b" stroke-width="2"/><line x1="119" y1="156" x2="119" y2="170" stroke="#1e5a6e" stroke-width="2"/>`,
  mainD:`<g transform="translate(146,252)"><rect x="-12" y="-8" width="24" height="30" rx="2" fill="#1e5a6e"/><circle cx="0" cy="6" r="6" fill="none" stroke="#f2c94c" stroke-width="2"/></g>`,
  cheveuxArriere:`<path d="M62 84 Q58 34 100 32 Q142 34 138 84 Q136 64 100 60 Q64 64 62 84" fill="#5a3a22"/><circle cx="100" cy="30" r="15" fill="#5a3a22"/>`,
  tete:`<g transform="translate(136,72) rotate(20)"><rect x="-2" y="-14" width="4" height="26" fill="#e0a800"/><path d="M-2 12 L0 18 L2 12 Z" fill="#333"/></g>`})
};

/* ---- Gestes ---- */
function geste(cible, nomGeste, duree=2200){
  const el = typeof cible === "string" ? document.querySelector(cible) : cible;
  if(!el) return;
  ["geste-pointe","geste-joie","geste-inquiet","geste-salue"].forEach(c=>el.classList.remove(c));
  if(nomGeste && nomGeste !== "neutre"){
    void el.offsetWidth;
    el.classList.add("geste-"+nomGeste);
    if(duree > 0) setTimeout(()=>el.classList.remove("geste-"+nomGeste), duree);
  }
}

/** Le personnage actuellement à l'écran. */
function persoCourant(){
  return document.querySelector(".personnage-scene .portrait");
}

window.htmlPortrait     = htmlPersonnage;
window.htmlPersonnage   = htmlPersonnage;
window.svgPersonnage    = svgPersonnage;
window.activerPortrait  = activerPortraitBase; // media.js remplace ensuite
window.geste            = geste;
window.persoCourant     = persoCourant;
window.SVG_PERSOS       = SVG_PERSOS;
