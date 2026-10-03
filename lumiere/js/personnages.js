/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — « Le Phare de l'île Lumière »
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

   Personnages (tous inventés) : maelle (gardienne du phare),
   salome (ingénieure en signalisation maritime), nils (9 ans, neveu
   de la gardienne), achille (horloger du port), yasmine (capitaine
   du voilier La Mouette). Aucune personne réelle ne parle.
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.maelle;
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

/* MAËLLE — gardienne du phare (personnage inventée) : vareuse bleue de marin, bonnet, lampe-tempête */
maelle: perso({
  id:"Ma", peau:PEAU.claire, fond:["#4f79a4","#13233a"], habit:["#2e5e8c","#1d3d60"], bas:"#2f3a40",
  cheveux:`<path d="M66 92 Q60 58 100 52 Q140 58 134 92 Q130 68 100 66 Q70 68 66 92" fill="#c9772f"/><path d="M128 86 Q144 110 134 134 L126 126 Q134 108 124 90 Z" fill="#c9772f"/>`,
  coiffe:`<path d="M66 72 Q64 40 100 38 Q136 40 134 72 Q100 64 66 72 Z" fill="#c0392b"/><rect x="66" y="64" width="68" height="10" rx="4" fill="#9a2b20"/><circle cx="100" cy="36" r="6" fill="#c0392b"/>`,
  dessus:`<g stroke="#f4f1ea" stroke-width="3" opacity=".9"><line x1="72" y1="150" x2="128" y2="150"/><line x1="70" y1="166" x2="130" y2="166"/><line x1="68" y1="182" x2="132" y2="182"/></g><path d="M86 128 L100 142 L114 128" stroke="#f4f1ea" stroke-width="3" fill="none"/>`,
  objetD:`<g transform="translate(150,246)"><path d="M-8 -30 Q0 -40 8 -30" stroke="#333" stroke-width="2.5" fill="none"/><rect x="-10" y="-30" width="20" height="5" fill="#333"/><rect x="-9" y="-25" width="18" height="22" rx="3" fill="#ffe9a0" stroke="#333" stroke-width="2"/><circle cx="0" cy="-14" r="4" fill="#ffb000"><animate attributeName="r" values="3.5;4.5;3.5" dur="1.6s" repeatCount="indefinite"/></circle><rect x="-11" y="-3" width="22" height="5" fill="#333"/></g>`,
  visageOpts:{oeil:"#2f5a7a", sourcil:"#9a5420", joue:".45"}
}),

/* SALOMÉ — ingénieure en signalisation maritime (personnage inventée) : gilet orange de sécurité, casque blanc, plaque de verre */
salome: perso({
  id:"Sa", peau:PEAU.foncee, fond:["#e0b04a","#5a3a10"], habit:["#3d4f6b","#273449"], bas:"#273449",
  cheveux:`<path d="M64 96 Q56 52 100 48 Q144 52 136 96 Q140 70 124 62 Q100 54 76 62 Q60 70 64 96" fill="#1c120a"/><g fill="#1c120a"><circle cx="66" cy="96" r="9"/><circle cx="134" cy="96" r="9"/><circle cx="62" cy="80" r="8"/><circle cx="138" cy="80" r="8"/></g>`,
  coiffe:`<path d="M68 66 Q70 36 100 36 Q130 36 132 66 Z" fill="#f4f4f0" stroke="#b9b9b0" stroke-width="1.5"/><rect x="62" y="62" width="76" height="8" rx="3" fill="#e6e6df"/>`,
  dessus:`<path d="M70 132 L92 132 L96 212 L64 210 Z" fill="#f28c28"/><path d="M130 132 L108 132 L104 212 L136 210 Z" fill="#f28c28"/><g stroke="#e8f0f0" stroke-width="4"><line x1="68" y1="176" x2="94" y2="176"/><line x1="106" y1="176" x2="132" y2="176"/></g>`,
  objetD:`<g transform="translate(150,236)"><rect x="-4" y="-40" width="8" height="46" fill="#cfe6f5" stroke="#6f8f9a" opacity=".9"/><line x1="-1" y1="-36" x2="-1" y2="0" stroke="#ffffff" stroke-width="1.5" opacity=".8"/></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1c120a", joue:".15", nez:"#6e4020", bouche:"#7d3038", levre:"#5e2128"}
}),

/* NILS — 9 ans, neveu de la gardienne (personnage inventé) : pull jaune, lampe de poche, figurine en carton */
nils: perso({
  id:"Ni", peau:PEAU.pale, fond:["#6b5a8a","#221c33"], habit:["#f2c230","#d19a12"], bas:"#3d4f6b",
  cheveux:`<path d="M66 90 Q60 50 100 48 Q140 50 134 90 Q132 64 112 60 L118 52 L104 58 L100 48 L94 58 L80 54 L86 62 Q68 66 66 90" fill="#e6c27a"/>`,
  dessus:`<path d="M80 150 Q100 160 120 150" stroke="#c48a10" stroke-width="3" fill="none"/><rect x="88" y="176" width="24" height="14" rx="3" fill="#d19a12"/>`,
  objetD:`<g transform="translate(150,242)"><rect x="-6" y="-26" width="12" height="26" rx="3" fill="#c0392b"/><rect x="-8" y="-32" width="16" height="7" rx="2" fill="#7a2418"/><circle cx="0" cy="-34" r="4" fill="#ffd23f"/></g>`,
  visageOpts:{oeil:"#2f5a7a", sourcil:"#b8904a", joue:".5"}
}),

/* ACHILLE — horloger du port (personnage inventé) : gilet brun, lunettes rondes, barbe grise, montre à gousset */
achille: perso({
  id:"Ac", peau:PEAU.hale, fond:["#c9a26a","#4a3418"], habit:["#f4efe2","#d9d1bc"], bas:"#3b2a1a",
  cheveux:`<path d="M66 92 Q64 70 76 62 Q72 76 72 92 Z M134 92 Q136 70 124 62 Q128 76 128 92 Z" fill="#b9b9b9"/>`,
  coiffe:`<path d="M72 100 Q74 128 100 132 Q126 128 128 100 Q120 116 100 116 Q80 116 72 100 Z" fill="#c9c9c9"/><g fill="none" stroke="#3a3a3a" stroke-width="2"><circle cx="88" cy="83" r="8"/><circle cx="112" cy="83" r="8"/><line x1="96" y1="83" x2="104" y2="83"/></g>`,
  dessus:`<path d="M72 132 L94 132 L98 212 L66 210 Z" fill="#7a4b2a"/><path d="M128 132 L106 132 L102 212 L134 210 Z" fill="#7a4b2a"/><g fill="#d9a21b"><circle cx="90" cy="156" r="2.5"/><circle cx="90" cy="172" r="2.5"/><circle cx="90" cy="188" r="2.5"/></g><path d="M112 170 Q122 178 118 190" stroke="#d9a21b" stroke-width="2" fill="none"/><circle cx="118" cy="194" r="6" fill="#e8c24a" stroke="#8a6d10"/>`,
  objetD:`<g transform="translate(150,240)"><rect x="-14" y="-18" width="28" height="22" rx="3" fill="#2e3440"/><circle cx="0" cy="-7" r="7" fill="#8aa0b0" stroke="#1d2430" stroke-width="2"/><rect x="6" y="-22" width="7" height="5" fill="#2e3440"/></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#9a9a9a", joue:".25", nez:"#9a6a40"}
}),

/* CAPITAINE YASMINE — capitaine du voilier La Mouette (personnage inventée) : ciré jaune, casquette de capitaine, lampe à signaux */
yasmine: perso({
  id:"Ya", peau:PEAU.hale, fond:["#2e86ab","#0f2a3d"], habit:["#f2c230","#c99a12"], bas:"#1f2430",
  cheveux:`<path d="M66 94 Q60 54 100 50 Q140 54 134 94 Q128 66 100 64 Q72 66 66 94" fill="#2a1a10"/><path d="M130 84 Q146 120 128 150 L122 140 Q136 116 124 90 Z" fill="#2a1a10"/>`,
  coiffe:`<path d="M66 68 Q66 44 100 42 Q134 44 134 68 Z" fill="#1d3557"/><path d="M64 68 L136 68 Q120 78 100 78 Q80 78 64 68 Z" fill="#111a2b"/><circle cx="100" cy="56" r="5" fill="#d9a21b"/>`,
  dessus:`<g stroke="#b88a10" stroke-width="2"><line x1="100" y1="128" x2="100" y2="214"/></g><g fill="#b88a10"><circle cx="106" cy="150" r="3"/><circle cx="106" cy="170" r="3"/><circle cx="106" cy="190" r="3"/></g>`,
  objetD:`<g transform="translate(150,236)"><rect x="-12" y="-22" width="24" height="22" rx="4" fill="#3a3f48" stroke="#1d2430" stroke-width="2"/><circle cx="12" cy="-11" r="7" fill="#ffd23f" stroke="#1d2430" stroke-width="2"><animate attributeName="opacity" values="1;1;.2;1;.2;.2;1" dur="2.4s" repeatCount="indefinite"/></circle><rect x="-4" y="0" width="8" height="10" fill="#1d2430"/></g>`,
  visageOpts:{oeil:"#2a1a10", sourcil:"#2a1a10", joue:".3", nez:"#9a6a40"}
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
