/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — « Le Secret du donjon »
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

   Personnages : colin (page), josselin (maître maçon), alienor (dame
   du château), mahaut (jeune paysanne), perrine (meunière).
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.colin;
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

/* ---- Un visage complet ---- */
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

/**
 * Assemble un personnage plein corps (viewBox 200 × 320).
 * id        suffixe unique des dégradés
 * peau      une entrée de PEAU
 * fond      [clair, foncé] du fond
 * habit     [clair, foncé] du vêtement principal
 * robe      true : robe longue (les jambes ne se voient pas)
 * bas       couleur des chausses (si pas de robe)
 * cheveux   chemin SVG des cheveux (derrière le visage)
 * coiffe    SVG posé par-dessus la tête
 * dessus    SVG ajouté sur le buste (ceinture, tablier, blason…)
 * objetD    SVG tenu dans la main droite
 */
function perso({id, peau, fond, habit, robe=false, bas="#4a3b2a", cheveux="", coiffe="", dessus="", objetD="", visageOpts={}}){
  const g = `url(#habit${id})`, p = `url(#peau${id})`;
  const jambes = robe
    ? `<path d="M66 196 Q60 250 54 300 L146 300 Q140 250 134 196 Z" fill="${g}"/>
       <ellipse cx="80" cy="302" rx="14" ry="5" fill="#3b2a1a"/><ellipse cx="120" cy="302" rx="14" ry="5" fill="#3b2a1a"/>`
    : `<path d="M78 208 L74 292 L92 292 L95 208 Z" fill="${bas}"/>
       <path d="M105 208 L108 292 L126 292 L122 208 Z" fill="${bas}"/>
       <ellipse cx="82" cy="298" rx="15" ry="6" fill="#3b2a1a"/><ellipse cx="118" cy="298" rx="15" ry="6" fill="#3b2a1a"/>`;
  return `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fond${id}" cx="50%" cy="32%" r="78%"><stop offset="0%" stop-color="${fond[0]}"/><stop offset="100%" stop-color="${fond[1]}"/></radialGradient>
    <linearGradient id="peau${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${peau[0]}"/><stop offset="100%" stop-color="${peau[1]}"/></linearGradient>
    <linearGradient id="habit${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${habit[0]}"/><stop offset="100%" stop-color="${habit[1]}"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fond${id})"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">${jambes}</g>
    <g class="bras bras-g">
      <path d="M72 140 Q58 172 56 204" stroke="${g}" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M56 204 Q54 222 58 236" stroke="${g}" stroke-width="14" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="59" cy="242" r="9" fill="${p}"/>
      </g>
    </g>
    <g class="buste">
      <path d="M70 130 Q100 118 130 130 L138 210 Q100 220 62 210 Z" fill="${g}"/>
      <path d="M90 118 L110 118 L110 130 Q100 136 90 130 Z" fill="${p}"/>
      ${dessus}
    </g>
    <g class="bras bras-d">
      <path d="M128 140 Q142 172 144 204" stroke="${g}" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M144 204 Q146 222 142 236" stroke="${g}" stroke-width="14" fill="none" stroke-linecap="round"/>
        <g class="main-d"><circle cx="141" cy="242" r="9" fill="${p}"/>${objetD}</g>
      </g>
    </g>
    <g class="tete">
      ${cheveux}
      ${visage(Object.assign({idPeau:"peau"+id}, visageOpts))}
      ${coiffe}
    </g>
  </g>
</svg>`;
}

/* ============================================================
   BIBLIOTHÈQUE DES PERSONNAGES
   ============================================================ */
const SVG_PERSOS = {

/* COLIN — 11 ans, page du seigneur : tunique aux couleurs du blason */
colin: perso({
  id:"Co", peau:PEAU.claire, fond:["#5a6f86","#1c2530"], habit:["#2f5d8a","#1d3c5c"], bas:"#8f2d24",
  cheveux:`<path d="M66 82 Q64 46 100 44 Q136 46 134 82 Q128 62 100 60 Q72 62 66 82" fill="#a0642a"/>`,
  dessus:`<path d="M100 132 L100 212" stroke="#c9a227" stroke-width="3"/>
          <path d="M88 150 L112 150 L112 164 Q100 176 88 164 Z" fill="#8f2d24" stroke="#c9a227" stroke-width="2"/>
          <rect x="64" y="196" width="72" height="6" fill="#5d3e20"/>`
}),

/* MAÎTRE JOSSELIN — maître maçon : tablier de cuir, bonnet, marteau */
josselin: perso({
  id:"Jo", peau:PEAU.hale, fond:["#7a6a52","#2a2218"], habit:["#8a7a5e","#5e523e"], bas:"#4a3b2a",
  cheveux:`<path d="M70 92 Q72 124 100 128 Q128 124 130 92 Q124 114 100 116 Q76 114 70 92" fill="#6b6b6b"/>`,
  coiffe:`<path d="M66 70 Q70 40 100 40 Q130 40 134 70 Q100 60 66 70 Z" fill="#b08a4e"/>`,
  dessus:`<path d="M76 150 L124 150 L128 214 L72 214 Z" fill="#7a4e2a" opacity=".95"/>
          <path d="M76 150 L90 132 M124 150 L110 132" stroke="#5e3a1c" stroke-width="3"/>`,
  objetD:`<g transform="translate(150,238) rotate(-20)"><rect x="-2" y="-30" width="4" height="34" fill="#7a5230"/><rect x="-10" y="-36" width="20" height="9" fill="#777"/></g>`,
  visageOpts:{oeil:"#2a1a10", sourcil:"#555", joue:".2", nez:"#9a6a40"}
}),

/* DAME ALIÉNOR — dame du château : robe longue, voile et touret, trousseau de clés */
alienor: perso({
  id:"Al", peau:PEAU.pale, fond:["#6b3a4a","#22111a"], habit:["#7a2a3a","#4e1824"], robe:true,
  cheveux:`<path d="M68 84 Q62 120 70 150 L80 150 Q72 116 76 84 Z" fill="#6b3f1f"/><path d="M132 84 Q138 120 130 150 L120 150 Q128 116 124 84 Z" fill="#6b3f1f"/>`,
  coiffe:`<path d="M64 76 Q64 42 100 40 Q136 42 136 76 L132 76 Q128 52 100 52 Q72 52 68 76 Z" fill="#f2ead6"/>
          <rect x="72" y="44" width="56" height="10" rx="3" fill="#c9a227"/>`,
  dessus:`<path d="M72 196 Q100 204 128 196" stroke="#c9a227" stroke-width="4" fill="none"/>
          <path d="M90 130 Q100 142 110 130" stroke="#c9a227" stroke-width="2" fill="none"/>`,
  objetD:`<g transform="translate(146,252)"><circle r="6" fill="none" stroke="#c9a227" stroke-width="2"/><path d="M0 6 L0 20 M0 16 L5 16 M0 20 L4 20" stroke="#c9a227" stroke-width="2"/></g>`,
  visageOpts:{oeil:"#2d4a2a", sourcil:"#6b3f1f", joue:".3"}
}),

/* MAHAUT — 11 ans, jeune paysanne : robe de laine, tablier, coiffe de toile, gerbe */
mahaut: perso({
  id:"Ma", peau:PEAU.foncee, fond:["#6f8a4a","#1f2a14"], habit:["#9a7a4a","#6e5230"], robe:true,
  cheveux:`<path d="M66 84 Q60 112 66 132 L76 128 Q70 108 74 84 Z" fill="#1c120a"/><path d="M134 84 Q140 112 134 132 L124 128 Q130 108 126 84 Z" fill="#1c120a"/>`,
  coiffe:`<path d="M64 74 Q64 42 100 40 Q136 42 136 74 Q100 62 64 74 Z" fill="#efe6cf"/>`,
  dessus:`<path d="M78 150 L122 150 L128 224 L72 224 Z" fill="#e9dfc6" opacity=".95"/>`,
  objetD:`<g transform="translate(152,236)"><g stroke="#c9a954" stroke-width="2.4">${[-6,-3,0,3,6].map(x=>`<line x1="${x}" y1="10" x2="${x*1.8}" y2="-24"/>`).join("")}</g><rect x="-8" y="-2" width="16" height="4" fill="#8a7030"/></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1c120a", joue:".15", nez:"#6e4020", bouche:"#7d3038", levre:"#5e2128"}
}),

/* PERRINE — meunière : robe, tablier fariné, foulard, sac de farine */
perrine: perso({
  id:"Pe", peau:PEAU.hale, fond:["#6a7f8f","#1c242a"], habit:["#5a6a4a","#3a4630"], robe:true,
  cheveux:`<path d="M68 90 Q66 112 72 124 L80 120 Q74 106 76 90 Z" fill="#7a3f1a"/>`,
  coiffe:`<path d="M62 78 Q62 40 100 38 Q138 40 138 78 Q124 64 100 64 Q76 64 62 78 Z" fill="#b8423a"/>
          <path d="M134 74 L148 96 L138 98 Z" fill="#b8423a"/>`,
  dessus:`<path d="M76 150 L124 150 L130 226 L70 226 Z" fill="#f4f0e4" opacity=".95"/>
          <g fill="#fff" opacity=".6"><circle cx="90" cy="180" r="3"/><circle cx="110" cy="196" r="4"/><circle cx="98" cy="212" r="3"/></g>`,
  objetD:`<g transform="translate(150,246)"><rect x="-12" y="-16" width="24" height="30" rx="7" fill="#e9dfc6" stroke="#9a8e76"/><path d="M-6 -8 l12 16 M6 -8 l-12 16" stroke="#8f2d24" stroke-width="2"/></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#7a3f1a", joue:".35"}
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
