/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — « Le Grand Prix de l'observatoire »
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

   Personnages (tous inventés) : margaux (commissaire de course),
   yanis (pilote de caisse à savon), salome (cycliste), leonie
   (astronome de l'observatoire), hugo (contrôleur du petit train).
   Aucune personne réelle ne parle.
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.margaux;
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

/* MARGAUX — commissaire de course (personnage inventée) : gilet jaune, casquette, drapeau à damier */
margaux: perso({
  id:"Ma", peau:PEAU.claire, fond:["#9cc7e4","#23406e"], habit:["#2f4f7a","#1f3556"], bas:"#1f3556",
  cheveux:`<path d="M64 96 Q56 52 100 48 Q144 52 136 96 Q138 72 124 62 Q100 54 76 62 Q62 72 64 96" fill="#6b4226"/><path d="M130 88 Q146 104 140 132 L132 128 Q136 106 124 94 Z" fill="#6b4226"/>`,
  coiffe:`<path d="M66 68 Q68 42 100 40 Q132 42 134 68 Z" fill="#c0392b"/><path d="M60 68 L142 68 Q150 70 146 76 L64 76 Z" fill="#8e2a1f"/>`,
  dessus:`<path d="M72 132 L94 132 L96 212 L66 210 Z" fill="#f2e33a"/><path d="M128 132 L106 132 L104 212 L134 210 Z" fill="#f2e33a"/><g stroke="#c9ccd1" stroke-width="4"><line x1="68" y1="180" x2="95" y2="180"/><line x1="105" y1="180" x2="132" y2="180"/></g>`,
  objetD:`<g transform="translate(150,236)"><line x1="0" y1="0" x2="0" y2="-52" stroke="#5c3a1e" stroke-width="3"/><g><rect x="0" y="-52" width="30" height="20" fill="#fff" stroke="#222"/>${[0,1,2,3,4].map(i=>`<rect x="${i*6}" y="${-52+(i%2)*10}" width="6" height="10" fill="#222"/>`).join("")}</g></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#6b4226", joue:".35", nez:"#c89a70", bouche:"#b0505a", levre:"#8e3a44"}
}),

/* YANIS — pilote de caisse à savon (personnage inventé) : combinaison rouge, casque, gants */
yanis: perso({
  id:"Ya", peau:PEAU.hale, fond:["#f0c27a","#7a2a1a"], habit:["#c0392b","#8e2a1f"], bas:"#2f3a40",
  cheveux:`<path d="M68 88 Q64 56 100 54 Q136 56 132 88 Q126 68 100 66 Q74 68 68 88" fill="#1c120a"/>`,
  coiffe:`<path d="M62 84 Q60 36 100 34 Q140 36 138 84 L128 84 Q126 52 100 50 Q74 52 72 84 Z" fill="#f4f4f0" stroke="#9aa4ad" stroke-width="2"/><rect x="92" y="34" width="16" height="22" fill="#c0392b"/>`,
  dessus:`<rect x="94" y="132" width="12" height="80" fill="#f4f4f0"/><circle cx="100" cy="160" r="9" fill="#f4f4f0" stroke="#8e2a1f" stroke-width="2"/><text x="100" y="164" text-anchor="middle" font-size="11" font-weight="700" fill="#8e2a1f">7</text>`,
  objetD:`<g transform="translate(150,238)"><circle cx="0" cy="-16" r="13" fill="none" stroke="#333" stroke-width="5"/><line x1="-13" y1="-16" x2="13" y2="-16" stroke="#333" stroke-width="3"/></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1c120a", joue:".25", nez:"#a87a50"}
}),

/* SALOMÉ — cycliste (personnage inventée) : maillot vert et jaune, casque de vélo */
salome: perso({
  id:"Sa", peau:PEAU.foncee, fond:["#b8e0a4","#2d6a3a"], habit:["#2e8b57","#1f6a3f"], bas:"#1c2a30",
  cheveux:`<path d="M66 94 Q60 58 100 54 Q140 58 134 94 Q128 72 100 70 Q72 72 66 94" fill="#1c120a"/><circle cx="134" cy="92" r="9" fill="#1c120a"/>`,
  coiffe:`<path d="M64 74 Q64 36 100 34 Q136 36 136 74 Q118 62 100 62 Q82 62 64 74 Z" fill="#f2c230" stroke="#9a7a10" stroke-width="2"/><g stroke="#9a7a10" stroke-width="2"><line x1="84" y1="42" x2="80" y2="62"/><line x1="100" y1="38" x2="100" y2="60"/><line x1="116" y1="42" x2="120" y2="62"/></g>`,
  dessus:`<path d="M74 150 L126 150 L126 166 L74 166 Z" fill="#f2c230"/>`,
  objetD:`<g transform="translate(150,238)"><circle cx="0" cy="-18" r="14" fill="#f4f4f0" stroke="#333" stroke-width="2"/><line x1="0" y1="-18" x2="0" y2="-28" stroke="#c0392b" stroke-width="2"/><line x1="0" y1="-18" x2="7" y2="-18" stroke="#333" stroke-width="2"/><rect x="-3" y="-36" width="6" height="5" fill="#333"/></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1c120a", joue:".2", nez:"#6e4020", bouche:"#7d3038", levre:"#5e2128"}
}),

/* LÉONIE — astronome de l'observatoire (personnage inventée) : veste bleu nuit étoilée, lunettes, petite lunette */
leonie: perso({
  id:"Le", peau:PEAU.pale, fond:["#3b4f86","#0e1a33"], habit:["#23406e","#182f54"], bas:"#3b4a5a",
  cheveux:`<path d="M64 98 Q56 54 100 50 Q144 54 136 98 Q132 70 100 66 Q68 70 64 98" fill="#b5541c"/><path d="M64 96 Q58 124 66 140 L74 136 Q68 118 72 100 Z M136 96 Q142 124 134 140 L126 136 Q132 118 128 100 Z" fill="#b5541c"/>`,
  coiffe:`<g fill="none" stroke="#2a2a2a" stroke-width="2"><circle cx="88" cy="83" r="8"/><circle cx="112" cy="83" r="8"/><line x1="96" y1="83" x2="104" y2="83"/></g>`,
  dessus:`<g fill="#ffe9a8"><circle cx="84" cy="160" r="2.5"/><circle cx="116" cy="176" r="2.5"/><circle cx="92" cy="196" r="2"/><circle cx="110" cy="148" r="2"/></g>`,
  objetD:`<g transform="translate(150,236)"><rect x="-6" y="-46" width="12" height="40" rx="5" fill="#d9dde3" stroke="#5b6b7b" transform="rotate(25)"/><circle cx="-14" cy="-40" r="7" fill="#9fdcf2" stroke="#5b6b7b"/></g>`,
  visageOpts:{oeil:"#2f5a7a", sourcil:"#b5541c", joue:".4", nez:"#c89a70", bouche:"#b0505a", levre:"#8e3a44"}
}),

/* HUGO — contrôleur du petit train (personnage inventé) : veste bleu marine, casquette à visière, sifflet */
hugo: perso({
  id:"Hu", peau:PEAU.claire, fond:["#cfe3ef","#2a4a66"], habit:["#1d2f52","#14213b"], bas:"#14213b",
  cheveux:`<path d="M66 92 Q64 70 76 62 Q72 76 72 92 Z M134 92 Q136 70 124 62 Q128 76 128 92 Z" fill="#7a7a7a"/><path d="M84 108 Q100 100 116 108 Q100 114 84 108 Z" fill="#7a7a7a"/>`,
  coiffe:`<path d="M68 68 L70 48 Q100 38 130 48 L132 68 Z" fill="#1d2f52"/><rect x="68" y="60" width="64" height="8" fill="#c9a227"/><path d="M66 68 L134 68 Q138 76 128 78 L72 78 Q62 76 66 68 Z" fill="#14213b"/>`,
  dessus:`<g fill="#c9a227"><circle cx="92" cy="150" r="3"/><circle cx="92" cy="168" r="3"/><circle cx="108" cy="150" r="3"/><circle cx="108" cy="168" r="3"/></g>`,
  objetD:`<g transform="translate(150,236)"><rect x="-10" y="-22" width="20" height="10" rx="4" fill="#c9a227" stroke="#7a5f10"/><circle cx="8" cy="-17" r="6" fill="#c9a227" stroke="#7a5f10"/><path d="M-10 -17 Q-22 -6 -14 6" stroke="#c0392b" stroke-width="2" fill="none"/></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#7a7a7a", joue:".35", nez:"#c89a70"}
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
