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
  return SVG_PERSOS[perso] || SVG_PERSOS.lina;
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
   MADAME VASSEUR — prévisionniste (la météorologue)
   ------------------------------------------------------------ */
vasseur: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondVa" cx="50%" cy="30%" r="78%"><stop offset="0%" stop-color="#2f5d8d"/><stop offset="100%" stop-color="#0f1f33"/></radialGradient>
    <linearGradient id="peauVa" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${PEAU.hale[0]}"/><stop offset="100%" stop-color="${PEAU.hale[1]}"/></linearGradient>
    <linearGradient id="vesteVa" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1d5c8f"/><stop offset="100%" stop-color="#133e62"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondVa)"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M74 214 L70 292 L90 292 L93 214 Z" fill="#2b2f36"/>
      <path d="M107 214 L110 292 L130 292 L126 214 Z" fill="#2b2f36"/>
      <ellipse cx="80" cy="298" rx="15" ry="6" fill="#1c1a17"/><ellipse cx="120" cy="298" rx="15" ry="6" fill="#1c1a17"/>
    </g>
    <g class="bras bras-g">
      <path d="M70 150 Q56 178 52 204" stroke="url(#vesteVa)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M52 204 Q50 220 54 234" stroke="url(#vesteVa)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="55" cy="240" r="9" fill="url(#peauVa)"/>
        <!-- tablette avec une carte météo -->
        <g transform="translate(58,246) rotate(-8)"><rect x="-4" y="-2" width="30" height="22" rx="3" fill="#1f2430"/><rect x="-1" y="1" width="24" height="16" fill="#5aa0d8"/><circle cx="8" cy="8" r="4" fill="#f2c14e"/></g>
      </g>
    </g>
    <g class="buste">
      <path d="M70 148 Q68 132 80 126 L120 126 Q132 132 130 148 L134 216 Q100 224 66 216 Z" fill="url(#vesteVa)"/>
      <path d="M86 126 Q100 150 114 126 Q120 130 122 140 Q100 162 78 140 Q80 130 86 126" fill="#eef4f9"/>
      <!-- badge : un petit soleil derrière un nuage -->
      <g transform="translate(118,162)"><circle cx="3" cy="-3" r="5" fill="#f2c14e"/><ellipse cx="-1" cy="2" rx="8" ry="4" fill="#fff"/></g>
      <path d="M90 116 L110 116 L110 132 Q100 138 90 132 Z" fill="#c48f5e"/>
    </g>
    <g class="bras bras-d">
      <path d="M130 150 Q144 176 148 202" stroke="url(#vesteVa)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M148 202 Q150 218 146 232" stroke="url(#vesteVa)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <g class="main-d"><circle cx="145" cy="238" r="9.5" fill="url(#peauVa)"/>
          <path d="M141 233 Q138 228 140 224" stroke="url(#peauVa)" stroke-width="4" fill="none" stroke-linecap="round"/></g>
      </g>
    </g>
    <g class="tete">
      <path d="M62 84 Q58 34 100 32 Q142 34 138 84 Q136 70 100 62 Q64 70 62 84" fill="#1c120c"/>
      ${visage({idPeau:"peauVa", oeil:"#2e1c10", sourcil:"#1c120c", nez:"#a8784c"})}
      <!-- chignon -->
      <circle cx="100" cy="30" r="14" fill="#1c120c"/>
      <path d="M66 62 Q100 44 134 62 Q134 72 100 66 Q66 72 66 62" fill="#1c120c"/>
      <!-- lunettes -->
      <g fill="none" stroke="#c9a227" stroke-width="1.8"><circle cx="88" cy="83" r="8"/><circle cx="112" cy="83" r="8"/><path d="M96 83 L104 83"/></g>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   TIAGO — technicien de la station
   ------------------------------------------------------------ */
tiago: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondTi" cx="50%" cy="30%" r="78%"><stop offset="0%" stop-color="#4c6b3a"/><stop offset="100%" stop-color="#15200f"/></radialGradient>
    <linearGradient id="peauTi" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${PEAU.claire[0]}"/><stop offset="100%" stop-color="${PEAU.claire[1]}"/></linearGradient>
    <linearGradient id="combiTi" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e8612c"/><stop offset="100%" stop-color="#b8461a"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondTi)"/>
  <ellipse cx="100" cy="308" rx="54" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M74 212 L70 292 L92 292 L95 212 Z" fill="#3a4a5c"/>
      <path d="M105 212 L108 292 L130 292 L126 212 Z" fill="#3a4a5c"/>
      <ellipse cx="80" cy="298" rx="17" ry="7" fill="#3b2a1a"/><ellipse cx="120" cy="298" rx="17" ry="7" fill="#3b2a1a"/>
    </g>
    <g class="bras bras-g">
      <path d="M68 152 Q54 180 50 206" stroke="url(#combiTi)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M50 206 Q48 222 52 236" stroke="url(#combiTi)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="53" cy="242" r="9" fill="url(#peauTi)"/>
        <!-- clé plate -->
        <g transform="translate(52,252) rotate(20)"><rect x="-2" y="0" width="4" height="22" fill="#9aa3ad"/><path d="M-6 22 L6 22 L4 28 L-4 28 Z" fill="#9aa3ad"/></g>
      </g>
    </g>
    <g class="buste">
      <path d="M68 150 Q66 132 80 126 L120 126 Q134 132 132 150 L136 214 Q100 222 64 214 Z" fill="url(#combiTi)"/>
      <!-- bandes réfléchissantes -->
      <rect x="68" y="176" width="66" height="7" fill="#f2f2e8" opacity=".9"/>
      <rect x="68" y="194" width="66" height="7" fill="#f2f2e8" opacity=".9"/>
      <path d="M92 118 L108 118 L108 134 Q100 140 92 134 Z" fill="#e0b78f"/>
    </g>
    <g class="bras bras-d">
      <path d="M132 152 Q146 178 150 204" stroke="url(#combiTi)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M150 204 Q152 220 148 234" stroke="url(#combiTi)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <g class="main-d"><circle cx="147" cy="240" r="9.5" fill="url(#peauTi)"/>
          <path d="M143 235 Q140 230 142 226" stroke="url(#peauTi)" stroke-width="4" fill="none" stroke-linecap="round"/></g>
      </g>
    </g>
    <g class="tete">
      <path d="M64 80 Q62 40 100 38 Q138 40 136 80 Q134 64 100 58 Q66 64 64 80" fill="#7a4a24"/>
      ${visage({idPeau:"peauTi", oeil:"#3f4a55", sourcil:"#5e3a1c", nez:"#d4a17a"})}
      <!-- casquette -->
      <path d="M64 64 Q100 30 136 64 Z" fill="#1d5c8f"/>
      <path d="M126 62 Q150 62 156 70 L128 68 Z" fill="#133e62"/>
      <!-- barbe de trois jours -->
      <path d="M76 100 Q80 120 100 122 Q120 120 124 100 Q118 114 100 115 Q82 114 76 100" fill="#7a4a24" opacity=".35"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   LINA — 10 ans, responsable de la station de l'école
   ------------------------------------------------------------ */
lina: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondLi" cx="50%" cy="32%" r="78%"><stop offset="0%" stop-color="#5a7fa3"/><stop offset="100%" stop-color="#172433"/></radialGradient>
    <linearGradient id="peauLi" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${PEAU.foncee[0]}"/><stop offset="100%" stop-color="${PEAU.foncee[1]}"/></linearGradient>
    <linearGradient id="cireLi" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f2c14e"/><stop offset="100%" stop-color="#d49a1c"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondLi)"/>
  <ellipse cx="100" cy="308" rx="48" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M78 214 L74 290 L92 290 L95 214 Z" fill="#2f4f7a"/>
      <path d="M105 214 L108 290 L126 290 L122 214 Z" fill="#2f4f7a"/>
      <!-- bottes de pluie -->
      <path d="M72 276 L94 276 L94 300 L68 300 Q68 290 72 286 Z" fill="#2e7d32"/>
      <path d="M106 276 L128 276 L132 286 Q132 290 132 300 L106 300 Z" fill="#2e7d32"/>
    </g>
    <g class="bras bras-g">
      <path d="M72 152 Q60 180 56 204" stroke="url(#cireLi)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M56 204 Q54 220 58 234" stroke="url(#cireLi)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="59" cy="240" r="9" fill="url(#peauLi)"/>
        <!-- cahier de relevés -->
        <g transform="translate(60,244) rotate(-6)"><rect x="-2" y="0" width="26" height="30" rx="2" fill="#fbfbf8" stroke="#8a93a0"/>
          <g stroke="#b9c0c7"><line x1="2" y1="8" x2="20" y2="8"/><line x1="2" y1="14" x2="20" y2="14"/><line x1="2" y1="20" x2="16" y2="20"/></g></g>
      </g>
    </g>
    <g class="buste">
      <path d="M72 148 Q70 134 82 128 L118 128 Q130 134 128 148 L132 214 Q100 222 68 214 Z" fill="url(#cireLi)"/>
      <path d="M100 130 L100 212" stroke="#b07a10" stroke-width="2"/>
      <circle cx="104" cy="160" r="2.4" fill="#b07a10"/><circle cx="104" cy="180" r="2.4" fill="#b07a10"/><circle cx="104" cy="200" r="2.4" fill="#b07a10"/>
      <path d="M92 118 L108 118 L108 134 Q100 140 92 134 Z" fill="#8e5a34"/>
    </g>
    <g class="bras bras-d">
      <path d="M128 152 Q142 178 146 202" stroke="url(#cireLi)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M146 202 Q148 218 144 232" stroke="url(#cireLi)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <g class="main-d"><circle cx="143" cy="238" r="9.5" fill="url(#peauLi)"/>
          <path d="M139 233 Q136 228 138 224" stroke="url(#peauLi)" stroke-width="4" fill="none" stroke-linecap="round"/></g>
      </g>
    </g>
    <g class="tete">
      <!-- tresses -->
      <path d="M62 84 Q54 120 62 150" stroke="#140d06" stroke-width="9" fill="none" stroke-linecap="round"/>
      <path d="M138 84 Q146 120 138 150" stroke="#140d06" stroke-width="9" fill="none" stroke-linecap="round"/>
      <circle cx="62" cy="152" r="5" fill="#e8612c"/><circle cx="138" cy="152" r="5" fill="#e8612c"/>
      <path d="M62 84 Q58 36 100 34 Q142 36 138 84 Q136 68 100 62 Q64 68 62 84" fill="#140d06"/>
      ${visage({idPeau:"peauLi", oeil:"#2a1a10", sourcil:"#140d06", joue:".2", nez:"#7d4a28", bouche:"#7d3038", levre:"#5e2128"})}
      <path d="M66 64 Q100 46 134 64 Q134 74 100 68 Q66 74 66 64" fill="#140d06"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   CAPITAINE KEÏTA — marin, dépend du vent
   ------------------------------------------------------------ */
keita: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondKe" cx="50%" cy="30%" r="78%"><stop offset="0%" stop-color="#2a6f8a"/><stop offset="100%" stop-color="#0c1f28"/></radialGradient>
    <linearGradient id="peauKe" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${PEAU.foncee[0]}"/><stop offset="100%" stop-color="${PEAU.foncee[1]}"/></linearGradient>
    <linearGradient id="vesteKe" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1c2b40"/><stop offset="100%" stop-color="#0f1826"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondKe)"/>
  <ellipse cx="100" cy="308" rx="56" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M74 214 L70 292 L91 292 L94 214 Z" fill="#e8e4dc"/>
      <path d="M106 214 L109 292 L130 292 L126 214 Z" fill="#e8e4dc"/>
      <ellipse cx="80" cy="298" rx="17" ry="7" fill="#5b3f2a"/><ellipse cx="120" cy="298" rx="17" ry="7" fill="#5b3f2a"/>
    </g>
    <g class="bras bras-g">
      <path d="M68 152 Q54 180 50 208" stroke="url(#vesteKe)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M50 208 Q48 224 52 238" stroke="url(#vesteKe)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="53" cy="244" r="9" fill="url(#peauKe)"/>
      </g>
    </g>
    <g class="buste">
      <path d="M68 150 Q66 132 80 126 L120 126 Q134 132 132 150 L136 216 Q100 224 64 216 Z" fill="url(#vesteKe)"/>
      <!-- marinière -->
      <path d="M84 126 L100 164 L116 126 Z" fill="#fbfbf8"/>
      <g stroke="#1d3a8a" stroke-width="3"><line x1="88" y1="136" x2="112" y2="136"/><line x1="92" y1="146" x2="108" y2="146"/><line x1="96" y1="156" x2="104" y2="156"/></g>
      <g fill="#c9a227"><circle cx="78" cy="170" r="3"/><circle cx="78" cy="190" r="3"/><circle cx="122" cy="170" r="3"/><circle cx="122" cy="190" r="3"/></g>
      <path d="M90 116 L110 116 L110 132 Q100 138 90 132 Z" fill="#7d4a28"/>
    </g>
    <g class="bras bras-d">
      <path d="M132 152 Q146 178 150 206" stroke="url(#vesteKe)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M150 206 Q152 222 148 236" stroke="url(#vesteKe)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <g class="main-d"><circle cx="147" cy="242" r="9.5" fill="url(#peauKe)"/>
          <path d="M143 237 Q140 232 142 228" stroke="url(#peauKe)" stroke-width="4" fill="none" stroke-linecap="round"/>
          <!-- boussole -->
          <g transform="translate(156,246)"><circle r="8" fill="#c9a227"/><circle r="6" fill="#fbfbf8"/><path d="M0 -5 L2 0 L0 5 L-2 0 Z" fill="#c62828"/></g>
        </g>
      </g>
    </g>
    <g class="tete">
      <path d="M66 80 Q64 44 100 42 Q136 44 134 80 Q132 66 100 60 Q68 66 66 80" fill="#1a1a1a"/>
      ${visage({idPeau:"peauKe", oeil:"#2a1a10", sourcil:"#101010", joue:".18", nez:"#5e3418", bouche:"#7d3038", levre:"#5e2128"})}
      <!-- barbe grisonnante -->
      <path d="M72 94 Q74 124 100 128 Q126 124 128 94 Q124 114 100 116 Q76 114 72 94" fill="#cfcac2" opacity=".95"/>
      <!-- casquette de marin -->
      <path d="M62 60 Q100 30 138 60 L138 66 L62 66 Z" fill="#fbfbf8" stroke="#9aa3ad"/>
      <rect x="62" y="62" width="76" height="8" fill="#1c2b40"/>
      <path d="M70 70 Q100 80 130 70 L126 76 Q100 84 74 76 Z" fill="#101010"/>
      <circle cx="100" cy="56" r="4" fill="#c9a227"/>
    </g>
  </g>
</svg>`
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
