/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — « De l'édit de Nantes à Versailles »
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

   Personnages : gabriel (apprenti secrétaire du roi), suzanne
   (imprimeuse protestante), mathurin (boulanger catholique), margot
   (aide-jardinière), isabeau (dame de la cour).
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.gabriel;
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

/* GABRIEL — 12 ans, apprenti secrétaire du roi (1682) : justaucorps bleu, rabat blanc, plume */
gabriel: perso({
  id:"Ga", peau:PEAU.claire, fond:["#4a5f86","#151d2e"], habit:["#2f4f8a","#1d3260"], bas:"#2a2a3a",
  cheveux:`<path d="M64 88 Q60 46 100 42 Q140 46 136 88 Q132 120 126 132 L122 100 Q118 62 100 60 Q82 62 78 100 L74 132 Q68 120 64 88" fill="#7a4a22"/>`,
  dessus:`<path d="M88 128 L112 128 L108 146 L92 146 Z" fill="#fbf6e8" stroke="#c9b98f"/>
          <g fill="#c9a227">${[150,166,182,198].map(y=>`<circle cx="100" cy="${y}" r="2.4"/>`).join("")}</g>`,
  objetD:`<g transform="translate(148,232) rotate(25)"><path d="M0 0 Q6 -24 18 -40 Q8 -18 3 2 Z" fill="#f3f0e6" stroke="#8a8170"/></g>`,
  visageOpts:{oeil:"#2d3a5a", sourcil:"#7a4a22"}
}),

/* SUZANNE — imprimeuse protestante (1598) : robe sombre, col blanc, tablier taché d'encre */
suzanne: perso({
  id:"Su", peau:PEAU.hale, fond:["#6b5a44","#221a12"], habit:["#3d3a44","#24222a"], robe:true,
  cheveux:`<path d="M68 86 Q64 110 70 124 L78 120 Q72 104 76 86 Z" fill="#4a2a14"/><path d="M132 86 Q136 110 130 124 L122 120 Q128 104 124 86 Z" fill="#4a2a14"/>`,
  coiffe:`<path d="M64 74 Q64 42 100 40 Q136 42 136 74 Q100 64 64 74 Z" fill="#f6f1e4"/>`,
  dessus:`<path d="M82 128 Q100 146 118 128 L118 136 Q100 152 82 136 Z" fill="#fbf6e8"/>
          <path d="M78 156 L122 156 L128 228 L72 228 Z" fill="#cdbf9f" opacity=".95"/>
          <g fill="#2b2b2b" opacity=".7"><circle cx="90" cy="186" r="3"/><circle cx="112" cy="200" r="2.5"/><circle cx="100" cy="214" r="2"/></g>`,
  objetD:`<g transform="translate(150,244)"><rect x="-14" y="-18" width="26" height="32" fill="#fbf6e8" stroke="#bfb193"/><g stroke="#6d6253"><line x1="-9" y1="-10" x2="7" y2="-10"/><line x1="-9" y1="-4" x2="7" y2="-4"/><line x1="-9" y1="2" x2="4" y2="2"/></g></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#4a2a14", joue:".3"}
}),

/* MATHURIN — boulanger catholique (1598) : chemise blanche, tablier fariné, pain */
mathurin: perso({
  id:"Mt", peau:PEAU.foncee, fond:["#8a6a42","#2a1e12"], habit:["#efe6cf","#cdbf9f"], bas:"#5e4128",
  cheveux:`<path d="M66 80 Q66 48 100 46 Q134 48 134 80 Q126 62 100 62 Q74 62 66 80" fill="#1c120a"/>`,
  coiffe:`<path d="M68 64 Q70 34 100 34 Q130 34 132 64 Q100 56 68 64 Z" fill="#f6f1e4"/>`,
  dessus:`<path d="M74 150 L126 150 L130 226 L70 226 Z" fill="#f6f1e4" stroke="#cdbf9f"/>
          <g fill="#fff" opacity=".7"><circle cx="88" cy="176" r="3"/><circle cx="112" cy="190" r="3.5"/></g>`,
  objetD:`<g transform="translate(152,246)"><ellipse rx="18" ry="9" fill="#c98a3c" stroke="#8a5a20"/><g stroke="#8a5a20" stroke-width="1.5"><line x1="-8" y1="-5" x2="-4" y2="5"/><line x1="0" y1="-5" x2="4" y2="5"/><line x1="8" y1="-5" x2="12" y2="4"/></g></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1c120a", joue:".2", nez:"#6e4020", bouche:"#7d3038", levre:"#5e2128"}
}),

/* MARGOT — 11 ans, aide-jardinière de l'équipe de Le Nôtre (1682) : robe verte, chapeau de paille, sécateur */
margot: perso({
  id:"Mg", peau:PEAU.claire, fond:["#6f9a5a","#1f2f18"], habit:["#4f7a3a","#335226"], robe:true,
  cheveux:`<path d="M66 84 Q60 120 70 146 L78 140 Q70 112 74 84 Z" fill="#c98a3c"/><path d="M134 84 Q140 120 130 146 L122 140 Q130 112 126 84 Z" fill="#c98a3c"/>`,
  coiffe:`<ellipse cx="100" cy="58" rx="52" ry="10" fill="#e3c97a" stroke="#a88a3c"/><path d="M74 58 Q76 32 100 32 Q124 32 126 58 Z" fill="#e3c97a" stroke="#a88a3c"/>
          <path d="M76 52 L124 52" stroke="#4f7a3a" stroke-width="4"/>`,
  dessus:`<path d="M80 150 L120 150 L126 222 L74 222 Z" fill="#e9dfc6" opacity=".95"/>`,
  objetD:`<g transform="translate(150,244) rotate(-15)"><path d="M-3 0 L-8 -22 M3 0 L8 -22" stroke="#777" stroke-width="3"/><circle cx="-4" cy="4" r="4" fill="none" stroke="#a0303a" stroke-width="2"/><circle cx="4" cy="4" r="4" fill="none" stroke="#a0303a" stroke-width="2"/></g>`,
  visageOpts:{oeil:"#2d4a2a", sourcil:"#a0642a", joue:".4"}
}),

/* DAME ISABEAU — dame de la cour de Louis XIV : robe de soie, coiffure haute, éventail */
isabeau: perso({
  id:"Is", peau:PEAU.pale, fond:["#7a5a8a","#24182c"], habit:["#8a4a7a","#5e2a52"], robe:true,
  cheveux:`<path d="M66 90 Q58 70 70 50 Q100 30 130 50 Q142 70 134 90 Q128 66 100 64 Q72 66 66 90 Z" fill="#3b2414"/>
           <circle cx="70" cy="96" r="7" fill="#3b2414"/><circle cx="130" cy="96" r="7" fill="#3b2414"/>`,
  coiffe:`<path d="M80 46 Q100 18 120 46 Q100 40 80 46 Z" fill="#fbf6e8" stroke="#c9b98f"/><circle cx="100" cy="44" r="3" fill="#c9a227"/>`,
  dessus:`<path d="M80 128 Q100 140 120 128" stroke="#fbf6e8" stroke-width="6" fill="none"/>
          <path d="M86 150 L114 150 L110 210 L90 210 Z" fill="#c9a227" opacity=".35"/>
          <path d="M70 200 Q100 210 130 200" stroke="#c9a227" stroke-width="3" fill="none"/>`,
  objetD:`<g transform="translate(150,236)"><path d="M0 0 L-16 -26 Q0 -34 16 -26 Z" fill="#fbf6e8" stroke="#c9a227"/><g stroke="#c9a227" stroke-width=".8"><line x1="0" y1="0" x2="-8" y2="-30"/><line x1="0" y1="0" x2="0" y2="-31"/><line x1="0" y1="0" x2="8" y2="-30"/></g></g>`,
  visageOpts:{oeil:"#2d3a5a", sourcil:"#3b2414", joue:".35"}
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
