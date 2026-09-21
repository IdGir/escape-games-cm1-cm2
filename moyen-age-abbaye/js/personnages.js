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
  return SVG_PERSOS[perso] || SVG_PERSOS.anselme;
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
   ============================================================ */
const SVG_PERSOS = {

/* ------------------------------------------------------------
   FRÈRE ANSELME — moine copiste, robe noire, tonsure, plume
   ------------------------------------------------------------ */
anselme: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondAn" cx="50%" cy="30%" r="78%"><stop offset="0%" stop-color="#6b5436"/><stop offset="100%" stop-color="#1e150c"/></radialGradient>
    <linearGradient id="peauAn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${PEAU.claire[0]}"/><stop offset="100%" stop-color="${PEAU.claire[1]}"/></linearGradient>
    <linearGradient id="robeAn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a3530"/><stop offset="100%" stop-color="#1c1916"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondAn)"/>
  <ellipse cx="100" cy="308" rx="54" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M66 214 L58 298 L142 298 L134 214 Z" fill="url(#robeAn)"/>
      <path d="M100 220 L100 296" stroke="#0f0d0b" stroke-width="2" opacity=".6"/>
      <ellipse cx="80" cy="300" rx="14" ry="6" fill="#4a3320"/><ellipse cx="120" cy="300" rx="14" ry="6" fill="#4a3320"/>
    </g>
    <g class="bras bras-g">
      <path d="M70 150 Q56 180 54 206" stroke="url(#robeAn)" stroke-width="18" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M54 206 Q54 222 60 236" stroke="url(#robeAn)" stroke-width="16" fill="none" stroke-linecap="round"/>
        <g class="main-g">
          <circle cx="62" cy="242" r="9" fill="url(#peauAn)"/>
          <rect x="44" y="232" width="30" height="22" rx="2" fill="#8a2a1f" stroke="#5a1a12"/>
          <rect x="47" y="235" width="24" height="16" fill="#f4ead0"/>
        </g>
      </g>
    </g>
    <g class="buste">
      <path d="M68 148 Q66 132 80 126 L120 126 Q134 132 132 148 L136 216 Q100 224 64 216 Z" fill="url(#robeAn)"/>
      <path d="M76 128 Q100 150 124 128 Q128 140 120 146 Q100 160 80 146 Q72 140 76 128" fill="#2a2622"/>
      <path d="M72 196 Q100 204 128 196" stroke="#6b5436" stroke-width="3" fill="none"/>
      <path d="M100 200 L96 232 M100 200 L104 232" stroke="#6b5436" stroke-width="2"/>
    </g>
    <g class="bras bras-d">
      <path d="M130 150 Q144 178 148 204" stroke="url(#robeAn)" stroke-width="18" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M148 204 Q150 220 146 234" stroke="url(#robeAn)" stroke-width="16" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="145" cy="240" r="9.5" fill="url(#peauAn)"/>
          <path d="M146 236 Q156 214 172 204 Q164 222 150 238 Z" fill="#fbfbf6" stroke="#a89878"/>
        </g>
      </g>
    </g>
    <g class="tete">
      <path d="M58 120 Q54 70 100 64 Q146 70 142 120 L134 128 Q100 110 66 128 Z" fill="#2a2622"/>
      ${visage({idPeau:"peauAn", oeil:"#3a4a5a", sourcil:"#6b5a48", nez:"#c89a70"})}
      <path d="M69 72 Q100 54 131 72 Q134 60 100 52 Q66 60 69 72" fill="#7a6a58"/>
      <ellipse cx="100" cy="58" rx="24" ry="9" fill="url(#peauAn)"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   AUDE — 11 ans, élève de l'école du palais, tablette de cire
   ------------------------------------------------------------ */
aude: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondAu" cx="50%" cy="32%" r="78%"><stop offset="0%" stop-color="#3b5a7a"/><stop offset="100%" stop-color="#111a26"/></radialGradient>
    <linearGradient id="peauAu" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${PEAU.hale[0]}"/><stop offset="100%" stop-color="${PEAU.hale[1]}"/></linearGradient>
    <linearGradient id="robeAu" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2f5aa8"/><stop offset="100%" stop-color="#1c3b75"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondAu)"/>
  <ellipse cx="100" cy="308" rx="48" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M72 206 L62 294 L138 294 L128 206 Z" fill="url(#robeAu)"/>
      <path d="M64 286 L136 286" stroke="#c9a227" stroke-width="3"/>
      <ellipse cx="82" cy="298" rx="13" ry="6" fill="#5a3a20"/><ellipse cx="118" cy="298" rx="13" ry="6" fill="#5a3a20"/>
    </g>
    <g class="bras bras-g">
      <path d="M72 152 Q60 180 56 206" stroke="url(#robeAu)" stroke-width="14" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M56 206 Q54 222 58 236" stroke="url(#robeAu)" stroke-width="12" fill="none" stroke-linecap="round"/>
        <g class="main-g">
          <rect x="38" y="222" width="34" height="26" rx="2" fill="#8a5a33"/>
          <rect x="42" y="226" width="26" height="18" fill="#c9a24d"/>
          <path d="M45 232 H64 M45 238 H58" stroke="#6d4c2f" stroke-width="1.2"/>
          <circle cx="59" cy="242" r="8" fill="url(#peauAu)"/>
        </g>
      </g>
    </g>
    <g class="buste">
      <path d="M72 148 Q70 134 82 128 L118 128 Q130 134 128 148 L130 210 Q100 218 70 210 Z" fill="url(#robeAu)"/>
      <path d="M86 128 Q100 142 114 128" stroke="#c9a227" stroke-width="3" fill="none"/>
      <path d="M72 186 H128" stroke="#c9a227" stroke-width="3"/>
      <path d="M92 118 L108 118 L108 132 Q100 138 92 132 Z" fill="#c48f5e"/>
    </g>
    <g class="bras bras-d">
      <path d="M128 152 Q142 178 146 204" stroke="url(#robeAu)" stroke-width="14" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M146 204 Q148 220 144 234" stroke="url(#robeAu)" stroke-width="12" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="143" cy="240" r="8.5" fill="url(#peauAu)"/>
          <path d="M146 236 L162 212" stroke="#d9c9a8" stroke-width="3" stroke-linecap="round"/>
        </g>
      </g>
    </g>
    <g class="tete">
      <path d="M62 84 Q60 36 100 34 Q140 36 138 84 Q140 120 128 140 L126 96 Q100 66 74 96 L72 140 Q60 120 62 84" fill="#4a2a14"/>
      ${visage({idPeau:"peauAu", oeil:"#2e1c10", sourcil:"#3a2010", nez:"#b07a4e"})}
      <path d="M66 66 Q100 44 134 66" stroke="#c9a227" stroke-width="4" fill="none"/>
      <path d="M126 96 Q134 124 124 150" stroke="#4a2a14" stroke-width="9" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MÈRE ALIX — abbesse de l'hôtel-Dieu, voile noir, guimpe blanche
   ------------------------------------------------------------ */
alix: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondAl" cx="50%" cy="30%" r="78%"><stop offset="0%" stop-color="#6e4a3a"/><stop offset="100%" stop-color="#1f130d"/></radialGradient>
    <linearGradient id="peauAl" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${PEAU.foncee[0]}"/><stop offset="100%" stop-color="${PEAU.foncee[1]}"/></linearGradient>
    <linearGradient id="robeAl" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f1ede4"/><stop offset="100%" stop-color="#cfc6b3"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondAl)"/>
  <ellipse cx="100" cy="308" rx="54" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M66 212 L58 298 L142 298 L134 212 Z" fill="url(#robeAl)"/>
      <path d="M84 214 L80 298 M116 214 L120 298" stroke="#b5ab96" stroke-width="2"/>
      <ellipse cx="80" cy="300" rx="14" ry="6" fill="#2a2018"/><ellipse cx="120" cy="300" rx="14" ry="6" fill="#2a2018"/>
    </g>
    <g class="bras bras-g">
      <path d="M70 150 Q56 180 54 206" stroke="url(#robeAl)" stroke-width="18" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M54 206 Q54 222 60 236" stroke="url(#robeAl)" stroke-width="16" fill="none" stroke-linecap="round"/>
        <g class="main-g">
          <path d="M40 236 Q60 262 80 236 Z" fill="#8a5a33"/>
          <ellipse cx="52" cy="234" rx="8" ry="5" fill="#d89b4a"/><ellipse cx="66" cy="233" rx="8" ry="5" fill="#d89b4a"/>
          <circle cx="62" cy="244" r="8" fill="url(#peauAl)"/>
        </g>
      </g>
    </g>
    <g class="buste">
      <path d="M68 148 Q66 132 80 126 L120 126 Q134 132 132 148 L136 216 Q100 224 64 216 Z" fill="url(#robeAl)"/>
      <path d="M100 150 V180 M88 162 H112" stroke="#8a6d12" stroke-width="4" stroke-linecap="round"/>
    </g>
    <g class="bras bras-d">
      <path d="M130 150 Q144 178 148 204" stroke="url(#robeAl)" stroke-width="18" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M148 204 Q150 220 146 234" stroke="url(#robeAl)" stroke-width="16" fill="none" stroke-linecap="round"/>
        <g class="main-d"><circle cx="145" cy="240" r="9" fill="url(#peauAl)"/></g>
      </g>
    </g>
    <g class="tete">
      <path d="M54 150 Q48 60 100 48 Q152 60 146 150 Z" fill="#1c1916"/>
      <path d="M68 118 Q100 150 132 118 L132 132 Q100 160 68 132 Z" fill="#fbfaf6"/>
      <path d="M66 72 Q100 52 134 72 L134 84 Q100 70 66 84 Z" fill="#fbfaf6"/>
      ${visage({idPeau:"peauAl", oeil:"#1e120a", sourcil:"#1e120a", nez:"#6d3f22", bouche:"#7a2e2e", levre:"#5a2020"})}
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   GARIN — 12 ans, apprenti tailleur de pierre, tablier, maillet
   ------------------------------------------------------------ */
garin: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondGa" cx="50%" cy="32%" r="78%"><stop offset="0%" stop-color="#7fa0c9"/><stop offset="100%" stop-color="#27394f"/></radialGradient>
    <linearGradient id="peauGa" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${PEAU.pale[0]}"/><stop offset="100%" stop-color="${PEAU.pale[1]}"/></linearGradient>
    <linearGradient id="tuniqueGa" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#9a6a3a"/><stop offset="100%" stop-color="#6d4722"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondGa)"/>
  <ellipse cx="100" cy="308" rx="48" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M78 212 L74 292 L92 292 L96 212 Z" fill="#4e5d3a"/>
      <path d="M104 212 L108 292 L126 292 L122 212 Z" fill="#4e5d3a"/>
      <ellipse cx="82" cy="298" rx="14" ry="6" fill="#4a3320"/><ellipse cx="118" cy="298" rx="14" ry="6" fill="#4a3320"/>
    </g>
    <g class="bras bras-g">
      <path d="M72 152 Q60 180 56 206" stroke="url(#tuniqueGa)" stroke-width="14" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M56 206 Q54 222 58 236" stroke="url(#peauGa)" stroke-width="11" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="58" cy="242" r="8.5" fill="url(#peauGa)"/>
      </g>
    </g>
    <g class="buste">
      <path d="M72 148 Q70 134 82 128 L118 128 Q130 134 128 148 L132 216 Q100 224 68 216 Z" fill="url(#tuniqueGa)"/>
      <path d="M80 160 L120 160 L124 224 L76 224 Z" fill="#6b4a2c" stroke="#3d2614"/>
      <path d="M80 160 L72 136 M120 160 L128 136" stroke="#3d2614" stroke-width="2"/>
      <path d="M92 118 L108 118 L108 132 Q100 138 92 132 Z" fill="#ecd0b4"/>
    </g>
    <g class="bras bras-d">
      <path d="M128 152 Q142 178 146 204" stroke="url(#tuniqueGa)" stroke-width="14" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M146 204 Q148 220 144 234" stroke="url(#peauGa)" stroke-width="11" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <path d="M144 240 L160 204" stroke="#6d4c2f" stroke-width="5" stroke-linecap="round"/>
          <rect x="150" y="190" width="22" height="16" rx="3" fill="#8a7a5c" transform="rotate(24 161 198)"/>
          <circle cx="143" cy="240" r="9" fill="url(#peauGa)"/>
        </g>
      </g>
    </g>
    <g class="tete">
      <path d="M64 86 Q62 44 100 42 Q138 44 136 86 Q128 70 100 68 Q72 70 64 86" fill="#c98a3a"/>
      ${visage({idPeau:"peauGa", oeil:"#3a5a2a", sourcil:"#9a6424", nez:"#d0a07a"})}
      <path d="M64 70 Q100 30 136 70 Q120 58 100 58 Q80 58 64 70" fill="#5a6b3a"/>
      <circle cx="84" cy="96" r="1.2" fill="#c98a3a"/><circle cx="118" cy="98" r="1.2" fill="#c98a3a"/>
    </g>
  </g>
</svg>`
};

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
