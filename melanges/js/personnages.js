/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — Le Laboratoire de Madame Mélange
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
  return SVG_PERSOS[perso] || SVG_PERSOS.lila;
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
   Le Laboratoire de Madame Mélange
   Un seul gabarit (même rig que les autres jeux), habillé
   différemment pour chaque personnage.
   ============================================================ */

/**
 * Construit un personnage plein corps.
 * o.id       : préfixe unique des dégradés
 * o.peau     : clé de PEAU
 * o.fond     : [couleur centre, couleur bord] du fond
 * o.haut     : [clair, foncé] du vêtement du haut
 * o.bas      : [clair, foncé] du pantalon / de la jupe
 * o.jupe     : true pour une jupe
 * o.cheveux  : SVG des cheveux (derrière la tête)
 * o.devant   : SVG posé sur la tête (frange, toque, chapeau…)
 * o.buste    : SVG ajouté sur le buste (blouse, tablier, badge…)
 * o.mainD    : SVG tenu dans la main droite (repère : main en 143,242)
 * o.chaussures : couleur
 * o.visage   : options de visage()
 */
function construirePerso(o){
  const P = PEAU[o.peau] || PEAU.claire;
  const id = o.id;
  const jambes = o.jupe
    ? `<path d="M68 208 L60 262 L140 262 L132 208 Z" fill="url(#bas${id})"/>
       <rect x="78" y="262" width="12" height="30" fill="url(#peau${id})"/><rect x="110" y="262" width="12" height="30" fill="url(#peau${id})"/>`
    : `<path d="M76 212 L70 292 L90 292 L94 212 Z" fill="url(#bas${id})"/>
       <path d="M106 212 L110 292 L130 292 L124 212 Z" fill="url(#bas${id})"/>`;
  return `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet" aria-hidden="true">
  <defs>
    <radialGradient id="fond${id}" cx="50%" cy="32%" r="78%">
      <stop offset="0%" stop-color="${o.fond[0]}"/><stop offset="100%" stop-color="${o.fond[1]}"/>
    </radialGradient>
    <linearGradient id="peau${id}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${P[0]}"/><stop offset="100%" stop-color="${P[1]}"/>
    </linearGradient>
    <linearGradient id="haut${id}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${o.haut[0]}"/><stop offset="100%" stop-color="${o.haut[1]}"/>
    </linearGradient>
    <linearGradient id="bas${id}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${o.bas[0]}"/><stop offset="100%" stop-color="${o.bas[1]}"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fond${id})"/>
  <ellipse cx="100" cy="308" rx="50" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      ${jambes}
      <ellipse cx="80" cy="298" rx="16" ry="7" fill="${o.chaussures||"#3a2a1a"}"/>
      <ellipse cx="120" cy="298" rx="16" ry="7" fill="${o.chaussures||"#3a2a1a"}"/>
    </g>
    <g class="bras bras-g">
      <path d="M70 152 Q58 180 54 206" stroke="url(#haut${id})" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M54 206 Q52 222 56 236" stroke="url(#haut${id})" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="57" cy="242" r="9" fill="url(#peau${id})"/>
      </g>
    </g>
    <g class="buste">
      <path d="M70 148 Q68 134 80 128 L120 128 Q132 134 130 148 L134 214 Q100 222 66 214 Z" fill="url(#haut${id})"/>
      <path d="M90 126 L100 140 L110 126 Z" fill="url(#peau${id})"/>
      ${o.buste||""}
    </g>
    <g class="bras bras-d">
      <path d="M130 152 Q142 180 146 206" stroke="url(#haut${id})" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M146 206 Q148 222 144 236" stroke="url(#haut${id})" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-d" cx="143" cy="242" r="9" fill="url(#peau${id})"/>
        ${o.mainD||""}
      </g>
    </g>
    <g class="tete">
      <rect x="92" y="112" width="16" height="18" fill="url(#peau${id})"/>
      ${o.cheveux||""}
      <ellipse cx="69" cy="88" rx="5" ry="8" fill="url(#peau${id})"/>
      <ellipse cx="131" cy="88" rx="5" ry="8" fill="url(#peau${id})"/>
      ${visage(Object.assign({idPeau:"peau"+id}, o.visage||{}))}
      ${o.devant||""}
    </g>
  </g>
</svg>`;
}

/* Petits accessoires */
const FIOLE_MAIN = `<g transform="translate(150,228)"><path d="M-4 -22 h8 v8 L10 4 H-10 L-4 -14 Z" fill="#eaf4f8" stroke="#56707a"/><path d="M-8 -2 H8 L10 4 H-10 Z" fill="#6fa8dc"/></g>`;
const LUNETTES = `<g fill="none" stroke="#333" stroke-width="2"><circle cx="88" cy="83" r="8"/><circle cx="112" cy="83" r="8"/><line x1="96" y1="83" x2="104" y2="83"/></g>`;
const LUNETTES_PROTECTION = `<path d="M74 76 Q100 68 126 76 L124 92 Q100 98 76 92 Z" fill="#bfe3f7" opacity=".55" stroke="#4a6572" stroke-width="2"/>`;

const SVG_PERSOS = {

/* ---- LILA — 11 ans, apprentie chimiste, blouse trop grande ---- */
lila: construirePerso({
  id:"Li", peau:"foncee", fond:["#3b6a5a","#10241d"],
  haut:["#ffffff","#dfe6ea"], bas:["#5b7fb0","#34507a"], chaussures:"#e8e4dc",
  cheveux:`<circle cx="100" cy="74" r="40" fill="#1e140c"/><circle cx="64" cy="96" r="16" fill="#1e140c"/><circle cx="136" cy="96" r="16" fill="#1e140c"/>`,
  devant:`<path d="M70 70 Q100 40 130 70 Q116 58 100 60 Q84 58 70 70" fill="#1e140c"/><rect x="118" y="52" width="18" height="6" rx="3" fill="#f1c232" transform="rotate(20 127 55)"/>`,
  buste:`<path d="M80 130 L92 214 M120 130 L108 214" stroke="#c7d0d6" stroke-width="2"/><rect x="108" y="160" width="16" height="12" rx="2" fill="#e0ecf2" stroke="#9fb3bf"/><text x="116" y="169" text-anchor="middle" font-family="system-ui" font-size="7" fill="#1d3a8a">L</text>`,
  mainD: FIOLE_MAIN,
  visage:{oeil:"#2a1a0a", sourcil:"#1e140c", nez:"#6d3f20", bouche:"#8a2f35", levre:"#5e2226"}
}),

/* ---- MARIUS — cuisinier, toque et tablier ---- */
marius: construirePerso({
  id:"Ma", peau:"claire", fond:["#8a5a2b","#2a1a0c"],
  haut:["#ffffff","#e6e6e6"], bas:["#3b3b3b","#1f1f1f"],
  cheveux:`<path d="M68 90 Q66 56 100 52 Q134 56 132 90 Q128 70 100 68 Q72 70 68 90" fill="#7a4a24"/>`,
  devant:`<rect x="72" y="40" width="56" height="18" fill="#fff" stroke="#ddd"/><circle cx="80" cy="30" r="14" fill="#fff" stroke="#ddd"/><circle cx="100" cy="24" r="16" fill="#fff" stroke="#ddd"/><circle cx="120" cy="30" r="14" fill="#fff" stroke="#ddd"/>
          <path d="M84 104 Q100 112 116 104" stroke="#7a4a24" stroke-width="5" fill="none" stroke-linecap="round"/>`,
  buste:`<path d="M80 150 H120 V214 Q100 220 80 214 Z" fill="#c0392b" opacity=".9"/><circle cx="92" cy="140" r="2.5" fill="#999"/><circle cx="108" cy="140" r="2.5" fill="#999"/>`,
  mainD:`<g transform="translate(150,232)"><line x1="0" y1="0" x2="10" y2="-26" stroke="#aaa" stroke-width="3"/><ellipse cx="11" cy="-28" rx="4" ry="6" fill="#aaa"/></g>`,
  visage:{oeil:"#3a5a7a", sourcil:"#5a3418"}
}),

/* ---- NADIA — laborantine de l'atelier de tri, lunettes de protection ---- */
nadia: construirePerso({
  id:"Na", peau:"hale", fond:["#4a6572","#152026"],
  haut:["#2e86ab","#1d5f7a"], bas:["#34495e","#1f2d3a"], chaussures:"#222",
  cheveux:`<path d="M66 92 Q62 48 100 46 Q138 48 134 92 L138 130 Q126 120 122 96 L78 96 Q74 120 62 130 Z" fill="#2b1d12"/>`,
  devant:`<path d="M70 72 Q100 46 130 72 Q112 62 100 64 Q86 62 70 72" fill="#2b1d12"/>` + LUNETTES_PROTECTION,
  buste:`<rect x="84" y="150" width="32" height="26" rx="3" fill="#1d5f7a" stroke="#174a60"/><path d="M92 158 v8 a8 8 0 0 0 16 0 v-8 h-4 v8 a4 4 0 0 1 -8 0 v-8 z" fill="#c0392b"/>`,
  mainD:`<g transform="translate(150,236)"><circle r="12" fill="none" stroke="#7d5a33" stroke-width="4"/><g stroke="#9a9280" stroke-width="1"><line x1="-8" y1="0" x2="8" y2="0"/><line x1="0" y1="-8" x2="0" y2="8"/></g></g>`,
  visage:{oeil:"#3a2a1a", sourcil:"#2b1d12"}
}),

/* ---- YANN — paludier, chapeau de paille et « las » (le grand râteau du paludier) ---- */
yann: construirePerso({
  id:"Ya", peau:"hale", fond:["#5b8fb0","#15283a"],
  haut:["#e9e3d3","#cfc6ad"], bas:["#2f4f6f","#1b3048"], chaussures:"#2a2a2a",
  cheveux:`<path d="M68 92 Q66 60 100 58 Q134 60 132 92 Q126 76 100 74 Q74 76 68 92" fill="#c9a86b"/>`,
  devant:`<ellipse cx="100" cy="56" rx="50" ry="10" fill="#e3c77a" stroke="#b8963e"/><path d="M72 56 Q74 30 100 28 Q126 30 128 56 Z" fill="#e3c77a" stroke="#b8963e"/><rect x="72" y="46" width="56" height="6" fill="#2f4f6f"/>
          <path d="M82 104 Q100 116 118 104" stroke="#c9a86b" stroke-width="3" fill="none" opacity=".8"/>`,
  buste:`<path d="M72 150 Q100 160 128 150" stroke="#cfc6ad" stroke-width="3" fill="none"/>`,
  mainD:`<g transform="translate(146,240)"><line x1="0" y1="40" x2="4" y2="-120" stroke="#8a6238" stroke-width="5"/><rect x="-20" y="-126" width="48" height="8" rx="2" fill="#8a6238"/></g>`,
  visage:{oeil:"#2a4a6a", sourcil:"#9a7a3b", joue:".5"}
}),

/* ---- MADAME MÉLANGE — chimiste, cheveux blancs, blouse, loupe ---- */
melange: construirePerso({
  id:"Me", peau:"hale", fond:["#6b4c7a","#1f1426"], jupe:true,
  haut:["#ffffff","#e2e6ea"], bas:["#6b4c7a","#4a3357"], chaussures:"#3a2a1a",
  cheveux:`<circle cx="100" cy="70" r="36" fill="#e6e6e6"/><circle cx="100" cy="36" r="16" fill="#e6e6e6"/>`,
  devant:`<path d="M68 76 Q100 48 132 76 Q118 64 100 66 Q82 64 68 76" fill="#e6e6e6"/>` + LUNETTES,
  buste:`<path d="M80 130 L90 214 M120 130 L110 214" stroke="#c7d0d6" stroke-width="2"/><g transform="translate(116,160)">${""}<path d="M-4 -10 h8 v5 L8 6 H-8 L-4 -5 Z" fill="#eaf4f8" stroke="#56707a"/><path d="M-6 1 H6 L8 6 H-8 Z" fill="#b4a7d6"/></g>`,
  mainD:`<g transform="translate(152,226)"><circle r="11" fill="#e8f4fb" fill-opacity=".5" stroke="#c9a227" stroke-width="3"/><line x1="-6" y1="10" x2="-12" y2="26" stroke="#8a6238" stroke-width="5" stroke-linecap="round"/></g>`,
  visage:{oeil:"#3a2a1a", sourcil:"#bdbdbd", joue:".45"}
})
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
