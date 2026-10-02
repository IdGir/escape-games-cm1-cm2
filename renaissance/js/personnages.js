/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés — « L'Atelier de Léonard à Amboise »
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

   Personnages (tous inventés) : tommaso (apprenti de Léonard),
   jacquet (imprimeur), helene (dame de la cour), colombe (fille du
   maître maçon), bastien (jeune peintre).
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.tommaso;
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

/* TOMMASO — 12 ans, apprenti de Léonard (personnage inventé) : pourpoint ocre, béret rouge, carnet */
tommaso: perso({
  id:"To", peau:PEAU.hale, fond:["#8a6a42","#2a1e12"], habit:["#b07a2a","#7a5218"], bas:"#5e3f1f",
  cheveux:`<path d="M66 86 Q62 52 100 48 Q138 52 134 86 Q128 66 100 64 Q72 66 66 86" fill="#3b2414"/>`,
  coiffe:`<ellipse cx="96" cy="54" rx="36" ry="12" fill="#a0303a"/><path d="M64 56 Q96 30 132 52 Z" fill="#a0303a"/>`,
  dessus:`<path d="M84 130 L116 130 L112 140 L88 140 Z" fill="#f6efdc"/><rect x="64" y="196" width="72" height="6" fill="#5e3f1f"/>`,
  objetD:`<g transform="translate(150,244)"><rect x="-12" y="-16" width="24" height="30" rx="2" fill="#7a4e2a" stroke="#4a2f16"/><rect x="-9" y="-13" width="18" height="24" fill="#f4ead2"/></g>`,
  visageOpts:{oeil:"#2a1a10", sourcil:"#3b2414", joue:".3", nez:"#9a6a40"}
}),

/* MAÎTRE JACQUET — imprimeur (personnage inventé) : tablier taché d'encre, bonnet noir, feuille imprimée */
jacquet: perso({
  id:"Ja", peau:PEAU.claire, fond:["#6b5a44","#221a12"], habit:["#4a4a5a","#2e2e3a"], bas:"#3b2a1a",
  cheveux:`<path d="M70 92 Q72 124 100 130 Q128 124 130 92 Q124 116 100 118 Q76 116 70 92" fill="#7a7a7a"/>`,
  coiffe:`<path d="M66 72 Q68 42 100 42 Q132 42 134 72 Q100 62 66 72 Z" fill="#1f1f24"/>`,
  dessus:`<path d="M74 150 L126 150 L130 226 L70 226 Z" fill="#cdbf9f"/><g fill="#2b2b2b" opacity=".7"><circle cx="88" cy="180" r="3"/><circle cx="114" cy="196" r="2.5"/></g>`,
  objetD:`<g transform="translate(150,244)"><rect x="-14" y="-18" width="26" height="32" fill="#fbf6e8" stroke="#bfb193"/><g stroke="#6d6253"><line x1="-9" y1="-10" x2="7" y2="-10"/><line x1="-9" y1="-4" x2="7" y2="-4"/><line x1="-9" y1="2" x2="4" y2="2"/></g></g>`,
  visageOpts:{oeil:"#3a2a1a", sourcil:"#7a7a7a", joue:".25"}
}),

/* DAME HÉLÈNE — dame de la cour de François Ier (personnage inventé) : robe de velours, coiffe à la française */
helene: perso({
  id:"He", peau:PEAU.pale, fond:["#2f4f8a","#111a2e"], habit:["#2f4f8a","#1d3260"], robe:true,
  cheveux:`<path d="M70 84 Q66 104 72 118 L80 114 Q74 100 76 84 Z" fill="#5a3418"/><path d="M130 84 Q134 104 128 118 L120 114 Q126 100 124 84 Z" fill="#5a3418"/>`,
  coiffe:`<path d="M62 86 Q60 42 100 38 Q140 42 138 86 L130 86 Q128 52 100 50 Q72 52 70 86 Z" fill="#1f1f24"/>
          <path d="M70 60 Q100 44 130 60" stroke="#c9a227" stroke-width="4" fill="none"/>`,
  dessus:`<path d="M78 128 L122 128 L118 146 L82 146 Z" fill="#c9a227" opacity=".6"/>
          <path d="M84 150 L116 150 L112 214 L88 214 Z" fill="#f4ead2" opacity=".35"/>
          <path d="M66 200 Q100 212 134 200" stroke="#c9a227" stroke-width="3" fill="none"/>`,
  objetD:`<g transform="translate(150,242)"><path d="M0 0 L-16 -26 Q0 -34 16 -26 Z" fill="#a0303a" stroke="#c9a227"/></g>`,
  visageOpts:{oeil:"#2d3a5a", sourcil:"#5a3418", joue:".35"}
}),

/* COLOMBE — 11 ans, fille d'un maître maçon (personnage inventée) : robe simple, coiffe de toile, règle et compas */
colombe: perso({
  id:"Cb", peau:PEAU.foncee, fond:["#6a7f8f","#1c242a"], habit:["#7a6a4a","#54482e"], robe:true,
  cheveux:`<path d="M66 84 Q60 116 66 136 L76 132 Q70 110 74 84 Z" fill="#1c120a"/><path d="M134 84 Q140 116 134 136 L124 132 Q130 110 126 84 Z" fill="#1c120a"/>`,
  coiffe:`<path d="M64 74 Q64 42 100 40 Q136 42 136 74 Q100 62 64 74 Z" fill="#efe6cf"/>`,
  dessus:`<path d="M80 150 L120 150 L126 222 L74 222 Z" fill="#d9cdb2" opacity=".95"/>`,
  objetD:`<g transform="translate(150,240)"><g stroke="#555" stroke-width="2.5"><line x1="0" y1="-20" x2="-8" y2="10"/><line x1="0" y1="-20" x2="8" y2="10"/></g><circle cy="-20" r="3" fill="#777"/></g>`,
  visageOpts:{oeil:"#1c120a", sourcil:"#1c120a", joue:".15", nez:"#6e4020", bouche:"#7d3038", levre:"#5e2128"}
}),

/* BASTIEN — jeune peintre de la cour (personnage inventé) : blouse claire, palette et pinceau */
bastien: perso({
  id:"Ba", peau:PEAU.claire, fond:["#7a5a8a","#24182c"], habit:["#5a7a4a","#3a5230"], bas:"#4a3b2a",
  cheveux:`<path d="M66 82 Q64 46 100 44 Q136 46 134 82 Q128 62 100 60 Q72 62 66 82" fill="#c98a3c"/>`,
  dessus:`<path d="M76 136 L124 136 L128 214 L72 214 Z" fill="#efe6cf" opacity=".9"/><g fill="#a0303a"><circle cx="90" cy="176" r="3"/></g><g fill="#2f4f8a"><circle cx="110" cy="192" r="3"/></g>`,
  objetD:`<g transform="translate(150,240)"><ellipse rx="18" ry="12" fill="#c9a26a" stroke="#6b4a2b"/><g><circle cx="-8" cy="-3" r="3" fill="#a0303a"/><circle cx="0" cy="-5" r="3" fill="#2f4f8a"/><circle cx="8" cy="-2" r="3" fill="#c9a227"/><circle cx="2" cy="5" r="3" fill="#3f7a3a"/></g></g>`,
  visageOpts:{oeil:"#2d4a2a", sourcil:"#a0642a", joue:".35"}
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
