/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — « Les Archives du port »
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

   Personnages (tous inventés) : ines (archiviste), malik (historien venu
   de Dakar), celia (historienne venue de Guadeloupe), margot (conservatrice
   du musée du port), theo (élève de l'atelier d'enquête).
   Aucune personne réelle ne parle.
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.ines;
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

/* INÈS — archiviste (personnage inventé) : blouse grise, lunettes, foulard, dossier */
ines: perso({
  id:"In", peau:PEAU.hale, fond:["#e8d9b8","#6b4f2a"], habit:["#7d8a8f","#5c676b"], robe:true,
  cheveux:`<path d="M64 100 Q56 52 100 48 Q144 52 136 100 Q132 70 100 64 Q68 70 64 100" fill="#2b1a10"/><path d="M64 96 Q60 130 70 150 L78 146 Q70 124 72 100 Z M136 96 Q140 130 130 150 L122 146 Q130 124 128 100 Z" fill="#2b1a10"/>`,
  coiffe:`<g fill="none" stroke="#3a2a1a" stroke-width="2"><rect x="80" y="77" width="16" height="12" rx="4"/><rect x="104" y="77" width="16" height="12" rx="4"/><line x1="96" y1="83" x2="104" y2="83"/></g>`,
  dessus:`<path d="M80 124 Q100 140 120 124 L118 136 Q100 150 82 136 Z" fill="#8c2f1c"/>`,
  objetD:`<g transform="translate(150,236)"><rect x="-14" y="-40" width="26" height="34" rx="2" fill="#c9a26a" stroke="#6b4f2a" stroke-width="2"/><line x1="-10" y1="-30" x2="8" y2="-30" stroke="#6b4f2a"/><line x1="-10" y1="-22" x2="8" y2="-22" stroke="#6b4f2a"/></g>`,
  visageOpts:{oeil:"#2b1a10", sourcil:"#2b1a10", joue:".3", nez:"#a87a50", bouche:"#9c4a4a", levre:"#7d3838"}
}),

/* MALIK — historien venu de Dakar (personnage inventé) : veste brune, chemise claire, carnet */
malik: perso({
  id:"Mk", peau:PEAU.foncee, fond:["#d9c9a8","#5c3b22"], habit:["#6b4a2c","#4a321c"], bas:"#2b2118",
  cheveux:`<path d="M68 82 Q66 56 100 54 Q134 56 132 82 Q124 64 100 62 Q76 64 68 82" fill="#141010"/><path d="M80 112 Q100 124 120 112 Q118 122 100 126 Q82 122 80 112 Z" fill="#141010"/>`,
  dessus:`<path d="M92 128 L108 128 L104 200 L96 200 Z" fill="#efe6d0"/><path d="M92 128 L100 142 L108 128" fill="none" stroke="#2f4858" stroke-width="3"/>`,
  objetD:`<g transform="translate(150,236)"><rect x="-12" y="-36" width="22" height="30" rx="2" fill="#2f4858" stroke="#1d2f3a" stroke-width="2"/><rect x="-9" y="-33" width="16" height="2" fill="#c9a227"/></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#141010", joue:".15", nez:"#5e3418", bouche:"#6e2f34", levre:"#4e1d22"}
}),

/* CÉLIA — historienne venue de Guadeloupe (personnage inventé) : robe verte, cheveux bouclés, livre */
celia: perso({
  id:"Ce", peau:PEAU.foncee, fond:["#cfe0c4","#3e5a3a"], habit:["#3e7a52","#2a5a3a"], robe:true,
  cheveux:`${[0,1,2,3,4,5,6,7,8].map(k=>`<circle cx="${66+k*8.5}" cy="${62+Math.abs(4-k)*4}" r="13" fill="#1a1210"/>`).join("")}<circle cx="64" cy="96" r="12" fill="#1a1210"/><circle cx="136" cy="96" r="12" fill="#1a1210"/>`,
  dessus:`<circle cx="100" cy="134" r="5" fill="#c9a227"/>`,
  objetD:`<g transform="translate(150,236)"><path d="M-16 -34 Q-2 -40 0 -32 Q2 -40 16 -34 L16 -10 Q2 -16 0 -8 Q-2 -16 -16 -10 Z" fill="#f2e6c8" stroke="#6b4f2a" stroke-width="2"/></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1a1210", joue:".2", nez:"#6e4020", bouche:"#7d3038", levre:"#5e2128"}
}),

/* MARGOT — conservatrice du musée du port (personnage inventé) : tailleur bleu ardoise, chignon, gants blancs */
margot: perso({
  id:"Mg", peau:PEAU.claire, fond:["#e6dccb","#2f4858"], habit:["#2f4858","#22343f"], bas:"#22343f",
  cheveux:`<path d="M66 96 Q58 52 100 48 Q142 52 134 96 Q130 70 100 64 Q70 70 66 96" fill="#b07a3a"/><circle cx="100" cy="46" r="14" fill="#b07a3a"/>`,
  dessus:`<path d="M84 126 L100 150 L116 126" fill="#f4f0e6"/>`,
  objetD:`<g transform="translate(150,238)"><circle cx="0" cy="-6" r="9" fill="#ffffff" stroke="#c9ccd1"/></g>`,
  visageOpts:{oeil:"#3a5a7a", sourcil:"#8a5a2a", joue:".35", nez:"#c89a70", bouche:"#b0505a", levre:"#8e3a44"}
}),

/* THÉO — élève de l'atelier d'enquête (personnage inventé) : sweat rouge, sac à dos, fiche */
theo: perso({
  id:"Th", peau:PEAU.pale, fond:["#f0e2c0","#8c2f1c"], habit:["#b8432a","#8c2f1c"], bas:"#2f4858",
  cheveux:`<path d="M66 86 Q62 52 100 50 Q138 52 134 86 Q128 62 104 62 Q96 74 84 66 Q72 70 66 86" fill="#c98a3a"/>`,
  dessus:`<path d="M70 136 L64 196 L74 198 L80 140 Z M130 136 L136 196 L126 198 L120 140 Z" fill="#2f4858"/>`,
  objetD:`<g transform="translate(150,236)"><rect x="-12" y="-36" width="24" height="30" fill="#fbf6e9" stroke="#8a6d45" stroke-width="2"/><line x1="-8" y1="-26" x2="8" y2="-26" stroke="#8c2f1c" stroke-width="2"/><line x1="-8" y1="-18" x2="6" y2="-18" stroke="#8a7a5a"/></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#a8702a", joue:".45", nez:"#d0a080"}
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
