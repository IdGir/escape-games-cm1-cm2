/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — « La Fabrique des états »
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

   Personnages (tous inventés) : ines (ingénieure de la Fabrique),
   bastien (agent météo), paolo (glacier), fatou (cuisinière de la
   cantine), ninon (gardienne du château d'eau). Aucune personne réelle
   ne parle.
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

/* INÈS — ingénieure de la Fabrique (personnage inventée) : bleu de travail, casque blanc, gilet orange, porte-bloc */
ines: perso({
  id:"In", peau:PEAU.foncee, fond:["#5c8fa8","#16313f"], habit:["#2f5f7a","#1f4256"], bas:"#1f4256",
  cheveux:`<path d="M64 96 Q56 52 100 48 Q144 52 136 96 Q140 70 124 62 Q100 54 76 62 Q60 70 64 96" fill="#1c120a"/><path d="M128 90 Q142 100 138 120 L130 116 Q134 102 124 94 Z" fill="#1c120a"/>`,
  coiffe:`<path d="M68 66 Q70 36 100 36 Q130 36 132 66 Z" fill="#f4f4f0" stroke="#b9b9b0" stroke-width="1.5"/><rect x="62" y="62" width="76" height="8" rx="3" fill="#e6e6df"/>`,
  dessus:`<path d="M70 132 L92 132 L96 212 L64 210 Z" fill="#f28c28"/><path d="M130 132 L108 132 L104 212 L136 210 Z" fill="#f28c28"/><g stroke="#e8f0f0" stroke-width="4"><line x1="68" y1="176" x2="94" y2="176"/><line x1="106" y1="176" x2="132" y2="176"/></g>`,
  objetD:`<g transform="translate(150,236)"><rect x="-14" y="-40" width="28" height="38" rx="3" fill="#8b5e3c"/><rect x="-11" y="-34" width="22" height="30" fill="#ffffff"/><rect x="-6" y="-44" width="12" height="7" rx="2" fill="#9aa4ad"/><g stroke="#5a6678" stroke-width="1.5"><line x1="-8" y1="-26" x2="8" y2="-26"/><line x1="-8" y1="-19" x2="8" y2="-19"/><line x1="-8" y1="-12" x2="4" y2="-12"/></g></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1c120a", joue:".15", nez:"#6e4020", bouche:"#7d3038", levre:"#5e2128"}
}),

/* BASTIEN — agent météo (personnage inventé) : parka bleu clair, écharpe rouge, anémomètre à coupelles */
bastien: perso({
  id:"Ba", peau:PEAU.hale, fond:["#9cc7e4","#2a4a66"], habit:["#4a90c2","#2f6a96"], bas:"#2f3a40",
  cheveux:`<path d="M66 90 Q62 52 100 50 Q138 52 134 90 Q130 66 112 62 Q100 58 88 62 Q70 66 66 90" fill="#5a3a1e"/>`,
  dessus:`<path d="M78 128 Q100 140 122 128 L122 140 Q100 152 78 140 Z" fill="#c0392b"/><rect x="84" y="138" width="10" height="34" fill="#c0392b"/><g stroke="#2f6a96" stroke-width="2"><line x1="100" y1="144" x2="100" y2="212"/></g>`,
  objetD:`<g transform="translate(150,232)"><line x1="0" y1="0" x2="0" y2="-34" stroke="#333" stroke-width="3"/><line x1="-14" y1="-34" x2="14" y2="-34" stroke="#333" stroke-width="2"/><circle cx="-14" cy="-34" r="5" fill="#e6e6df" stroke="#333"/><circle cx="14" cy="-34" r="5" fill="#e6e6df" stroke="#333"/><g><circle cx="0" cy="-34" r="2.5" fill="#333"/><animateTransform attributeName="transform" type="rotate" values="0 0 -34;360 0 -34" dur="2s" repeatCount="indefinite"/></g></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#5a3a1e", joue:".3", nez:"#a87a50"}
}),

/* PAOLO — glacier (personnage inventé) : veste blanche, calot blanc, moustache, cornet de glace */
paolo: perso({
  id:"Pa", peau:PEAU.claire, fond:["#cfeaf8","#3b6b88"], habit:["#f7f7f2","#d9d9d0"], bas:"#3b4a5a",
  cheveux:`<path d="M66 92 Q64 70 76 62 Q72 76 72 92 Z M134 92 Q136 70 124 62 Q128 76 128 92 Z" fill="#3a2a1a"/><path d="M86 108 Q100 102 114 108 Q100 112 86 108 Z" fill="#3a2a1a"/>`,
  coiffe:`<path d="M70 66 L72 48 Q100 40 128 48 L130 66 Z" fill="#ffffff" stroke="#c9c9c0" stroke-width="1.5"/><rect x="70" y="60" width="60" height="7" fill="#7fb8e6"/>`,
  dessus:`<g fill="#7fb8e6"><circle cx="92" cy="150" r="3"/><circle cx="92" cy="168" r="3"/><circle cx="108" cy="150" r="3"/><circle cx="108" cy="168" r="3"/></g>`,
  objetD:`<g transform="translate(150,238)"><path d="M-8 -20 L0 6 L8 -20 Z" fill="#d9a35e" stroke="#9a6a30"/><circle cx="0" cy="-26" r="10" fill="#f5c6d8"/><circle cx="-4" cy="-34" r="7" fill="#fff4d6"/></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#3a2a1a", joue:".35", nez:"#c89a70"}
}),

/* FATOU — cuisinière de la cantine (personnage inventée) : tablier vert, foulard de cuisine, fouet */
fatou: perso({
  id:"Fa", peau:PEAU.foncee, fond:["#f0c27a","#6a3e12"], habit:["#f7f1e3","#e0d6bf"], bas:"#4a3b2a",
  cheveux:`<path d="M66 92 Q62 58 100 54 Q138 58 134 92 Q128 72 100 70 Q72 72 66 92" fill="#1c120a"/>`,
  coiffe:`<path d="M64 76 Q62 40 100 38 Q138 40 136 76 Q118 64 100 64 Q82 64 64 76 Z" fill="#2e8b57"/><path d="M128 52 Q146 46 140 66 Q134 58 128 60 Z" fill="#2e8b57"/><g fill="#f2c230"><circle cx="86" cy="52" r="3"/><circle cx="104" cy="46" r="3"/><circle cx="118" cy="56" r="3"/></g>`,
  dessus:`<path d="M76 140 L124 140 L130 214 L70 214 Z" fill="#2e8b57"/><rect x="88" y="166" width="24" height="16" rx="3" fill="#25724a"/>`,
  objetD:`<g transform="translate(150,236)"><rect x="-3" y="-6" width="6" height="18" rx="2" fill="#8b5e3c"/><path d="M0 -6 Q-12 -26 0 -40 Q12 -26 0 -6 M0 -6 Q-6 -26 0 -40 Q6 -26 0 -6" stroke="#9aa4ad" stroke-width="1.5" fill="none"/></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1c120a", joue:".2", nez:"#6e4020", bouche:"#7d3038", levre:"#5e2128"}
}),

/* NINON — gardienne du château d'eau (personnage inventée) : veste verte, chignon gris, trousseau de clés */
ninon: perso({
  id:"No", peau:PEAU.pale, fond:["#8bb174","#2a4a24"], habit:["#4f7a3a","#365a26"], bas:"#3b4a5a",
  cheveux:`<path d="M66 94 Q60 56 100 52 Q140 56 134 94 Q130 68 100 66 Q70 68 66 94" fill="#b9b9b9"/><circle cx="100" cy="46" r="13" fill="#b9b9b9"/>`,
  coiffe:`<g fill="none" stroke="#3a3a3a" stroke-width="2"><circle cx="88" cy="83" r="8"/><circle cx="112" cy="83" r="8"/><line x1="96" y1="83" x2="104" y2="83"/></g>`,
  dessus:`<path d="M86 128 L100 142 L114 128" stroke="#e8f0e0" stroke-width="3" fill="none"/><g fill="#d9a21b"><circle cx="106" cy="156" r="3"/><circle cx="106" cy="176" r="3"/><circle cx="106" cy="196" r="3"/></g>`,
  objetD:`<g transform="translate(150,240)"><circle cx="0" cy="-14" r="9" fill="none" stroke="#b88a10" stroke-width="3"/><path d="M-4 -6 L-6 12 L-2 12 L-2 8 L-6 8 M6 -6 L8 10 L12 10" stroke="#8a6d10" stroke-width="3" fill="none"/></g>`,
  visageOpts:{oeil:"#2f5a7a", sourcil:"#8a8a8a", joue:".35", nez:"#c89a70"}
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
