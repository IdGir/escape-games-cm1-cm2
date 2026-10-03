/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — « Le Grand Repas du chef »
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

   Personnages (tous inventés) : rosalie (cheffe du restaurant),
   nathan (commis), ines (médecin de l'équipe cycliste), basile
   (coureur cycliste). Lou, la fille de la cheffe, n'apparaît que
   dans les données (toise, pouls).
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.rosalie;
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

/* ROSALIE — cheffe du Grand Couvert (personnage inventé) : veste blanche croisée, toque, cuillère en bois */
rosalie: perso({
  id:"Ro", peau:PEAU.claire, fond:["#5f8f9a","#173a44"], habit:["#fbfbf7","#dcdcd2"], bas:"#2f3a40",
  cheveux:`<path d="M66 90 Q62 60 100 54 Q138 60 134 90 Q130 70 100 68 Q70 70 66 90" fill="#8a4a24"/><path d="M128 84 Q140 102 132 120 L124 112 Q130 98 124 86 Z" fill="#8a4a24"/>`,
  coiffe:`<path d="M70 66 Q64 30 84 30 Q88 16 100 20 Q112 16 116 30 Q136 30 130 66 Z" fill="#ffffff" stroke="#c9c9bf" stroke-width="1.5"/><rect x="70" y="58" width="60" height="10" rx="3" fill="#f2f2ea" stroke="#c9c9bf"/>`,
  dessus:`<path d="M84 130 L116 130 L100 150 Z" fill="#f0f0e8"/><g fill="#a8432a"><circle cx="90" cy="160" r="3"/><circle cx="90" cy="178" r="3"/><circle cx="110" cy="160" r="3"/><circle cx="110" cy="178" r="3"/></g>
          <path d="M70 196 L130 196 L134 214 L66 214 Z" fill="#2b5d6b"/>`,
  objetD:`<g transform="translate(150,236)"><rect x="-2.5" y="-34" width="5" height="34" rx="2" fill="#b07a3a"/><ellipse cx="0" cy="-38" rx="7" ry="9" fill="#c08a4a" stroke="#7a5022"/></g>`,
  visageOpts:{oeil:"#3a5a2a", sourcil:"#7a3e1c", joue:".4"}
}),

/* NATHAN — commis (personnage inventé) : tablier vert, casquette, panier d'œufs */
nathan: perso({
  id:"Na", peau:PEAU.hale, fond:["#8fb36a","#2c4a1c"], habit:["#e8e2d0","#c9bfa4"], bas:"#3f4a5a",
  cheveux:`<path d="M66 86 Q62 54 100 50 Q138 54 134 86 Q128 66 100 64 Q72 66 66 86" fill="#2a1a10"/>`,
  coiffe:`<path d="M66 66 Q68 40 100 40 Q132 40 134 66 Q100 58 66 66 Z" fill="#a8432a"/><path d="M100 60 Q130 58 150 66 Q132 70 100 66 Z" fill="#7d2f1c"/>`,
  dessus:`<path d="M78 140 L122 140 L128 222 L72 222 Z" fill="#4f7a3a"/><rect x="88" y="168" width="24" height="14" rx="2" fill="#3f6430"/><path d="M78 140 L72 126 M122 140 L128 126" stroke="#4f7a3a" stroke-width="4"/>`,
  objetD:`<g transform="translate(150,244)"><path d="M-18 -6 Q0 18 18 -6 Z" fill="#b8874a" stroke="#7a5522"/><path d="M-16 -6 Q0 -26 16 -6" stroke="#7a5522" stroke-width="2.5" fill="none"/><g fill="#f5ecd8" stroke="#c9b48a"><ellipse cx="-7" cy="-8" rx="5" ry="6"/><ellipse cx="4" cy="-10" rx="5" ry="6"/><ellipse cx="10" cy="-6" rx="4.5" ry="5.5"/></g></g>`,
  visageOpts:{oeil:"#2a1a10", sourcil:"#2a1a10", joue:".3", nez:"#9a6a40"}
}),

/* DOCTEURE INÈS MOREL — médecin de l'équipe cycliste (personnage inventé) : blouse blanche, stéthoscope, chignon */
ines: perso({
  id:"In", peau:PEAU.pale, fond:["#9ab6c9","#24394a"], habit:["#ffffff","#e4e8ea"], bas:"#3d4f6b",
  cheveux:`<path d="M66 92 Q60 56 100 50 Q140 56 134 92 Q128 66 100 64 Q72 66 66 92" fill="#1f1a18"/><circle cx="100" cy="44" r="13" fill="#1f1a18"/>`,
  dessus:`<path d="M84 128 L100 150 L116 128 L116 140 L100 160 L84 140 Z" fill="#7aa3c2"/><path d="M86 136 Q78 176 98 188 Q118 176 112 136" stroke="#3a3a3a" stroke-width="3" fill="none"/><circle cx="98" cy="190" r="6" fill="#9aa5a8" stroke="#3a3a3a" stroke-width="2"/>
          <rect x="108" y="170" width="16" height="20" rx="2" fill="#eef2f4" stroke="#b9c2c6"/><line x1="112" y1="166" x2="112" y2="178" stroke="#2b5d6b" stroke-width="2"/>`,
  objetD:`<g transform="translate(150,242)"><rect x="-13" y="-20" width="26" height="32" rx="2" fill="#7a5a3a"/><rect x="-10" y="-16" width="20" height="25" fill="#fbf8ef"/><g stroke="#8a8a8a"><line x1="-7" y1="-10" x2="7" y2="-10"/><line x1="-7" y1="-4" x2="7" y2="-4"/><line x1="-7" y1="2" x2="4" y2="2"/></g><rect x="-5" y="-23" width="10" height="5" rx="1" fill="#9aa5a8"/></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#1f1a18", joue:".3"}
}),

/* BASILE NDIAYE — coureur cycliste (personnage inventé) : maillot d'équipe, casquette de cycliste, gourde */
basile: perso({
  id:"Bs", peau:PEAU.foncee, fond:["#e0b04a","#6a3f10"], habit:["#d9a21b","#b07a10"], bas:"#1f2430",
  cheveux:`<path d="M68 82 Q66 56 100 52 Q134 56 132 82 Q126 66 100 64 Q74 66 68 82" fill="#1c120a"/>`,
  coiffe:`<path d="M68 70 Q70 44 100 44 Q130 44 132 70 Q100 62 68 70 Z" fill="#2b5d6b"/><path d="M68 70 Q84 66 100 68 Q86 76 66 76 Z" fill="#1d434e"/><path d="M76 52 L124 52" stroke="#ffffff" stroke-width="3"/>`,
  dessus:`<path d="M70 150 L130 150 L132 166 L68 166 Z" fill="#2b5d6b"/><path d="M94 124 L106 124 L104 196 L96 196 Z" fill="#ffffff" opacity=".85"/><text x="114" y="186" font-size="12" font-weight="bold" fill="#1f2430" font-family="Arial,sans-serif">7</text>`,
  objetD:`<g transform="translate(150,238)"><rect x="-8" y="-26" width="16" height="34" rx="6" fill="#4aa3c8" stroke="#1d5f7a"/><rect x="-4" y="-32" width="8" height="7" rx="2" fill="#1f2430"/><rect x="-8" y="-12" width="16" height="6" fill="#ffffff" opacity=".6"/></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1c120a", joue:".15", nez:"#6e4020", bouche:"#7d3038", levre:"#5e2128"}
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
