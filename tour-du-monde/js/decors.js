/* ============================================================
   DÉCORS — Les 5 escales du Tour du Monde
   ------------------------------------------------------------
   Chaque escale possède un décor SVG animé, dessiné à la main,
   qui s'affiche IMMÉDIATEMENT (zéro attente, zéro fichier).

   Si l'enseignant dépose une vidéo ou une image du même nom
   (etape1.mp4 / etape1.jpg…), media.js la fait passer devant.
   Voir js/media.js pour la cascade complète.
   ============================================================ */

/* Correspondance escale → nom de fichier média */
const ETAPE_FICHIER = {
  "reform-club":"etape1",
  "suez":"etape2",
  "inde":"etape3",
  "mer-chine":"etape4",
  "greenwich":"etape5",
};

/**
 * Génère le HTML de la scène (décor) d'une escale.
 * @param {string} escale
 * @param {object} contenu - {lieu, description, sens:[], coordonnees}
 */
function htmlScene(escale, contenu){
  const svg  = SVG_DECORS[escale] || SVG_DECORS["reform-club"];
  const sens = (contenu.sens||[]).map(s=>`<span>${s}</span>`).join("");
  const coord = contenu.coordonnees
    ? `<div class="coordonnees">${contenu.coordonnees}</div>` : "";
  return `
    <div class="scene scene--media" data-escale="${escale}" data-media="${ETAPE_FICHIER[escale]||""}">
      <div class="decor-fallback">${svg}</div>
      <div class="decor-overlay"></div>
      ${coord}
      <div class="decor-contenu">
        <span class="lieu">${contenu.lieu||""}</span>
        <p class="description">${contenu.description||""}</p>
        ${sens?`<div class="sens">${sens}</div>`:""}
      </div>
    </div>`;
}

/**
 * Active la scène : lance la recherche du média (vidéo puis image).
 * Le SVG reste affiché tant que rien de mieux n'est trouvé.
 */
function activerScene(sceneEl){
  if(!sceneEl) return;
  if(typeof nettoyerVideos === "function") nettoyerVideos();
  const base = sceneEl.dataset.media;
  if(base && typeof installerDecor === "function"){
    installerDecor(sceneEl, base);
  }
}

/* Style commun à tous les SVG de décor */
const S = 'class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%"';

/* ============================================================
   BIBLIOTHÈQUE DES DÉCORS
   ============================================================ */
const SVG_DECORS = {

/* ---- Escale 1 — Le Reform Club, Londres, 2 octobre 1872 ---- */
"reform-club": `<svg ${S}>
  <defs>
    <linearGradient id="murClub" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4a3020"/><stop offset="100%" stop-color="#2c1c11"/>
    </linearGradient>
    <radialGradient id="lueurFoyer" cx="22%" cy="72%" r="45%">
      <stop offset="0%" stop-color="#ffb257" stop-opacity=".45"/>
      <stop offset="100%" stop-color="#ffb257" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murClub)"/>
  <!-- Boiseries -->
  <rect x="0" y="0" width="800" height="14" fill="#1d120a"/>
  <rect x="0" y="196" width="800" height="8" fill="#1d120a"/>
  <g fill="#3a2415">
    <rect x="30" y="20" width="120" height="172"/><rect x="620" y="20" width="150" height="172"/>
  </g>
  <!-- Bibliothèque -->
  <g>
    <rect x="630" y="34" width="130" height="66" fill="#22150c"/>
    <g fill="#8a5a2a"><rect x="636" y="40" width="9" height="54"/><rect x="649" y="44" width="8" height="50"/>
      <rect x="661" y="38" width="10" height="56"/><rect x="675" y="46" width="7" height="48"/>
      <rect x="686" y="40" width="9" height="54"/><rect x="699" y="43" width="8" height="51"/>
      <rect x="711" y="38" width="10" height="56"/><rect x="725" y="45" width="8" height="49"/></g>
    <rect x="630" y="108" width="130" height="66" fill="#22150c"/>
    <g fill="#7a4a24"><rect x="636" y="114" width="9" height="54"/><rect x="649" y="118" width="8" height="50"/>
      <rect x="661" y="112" width="10" height="56"/><rect x="675" y="120" width="7" height="48"/>
      <rect x="686" y="114" width="9" height="54"/><rect x="700" y="117" width="8" height="51"/></g>
  </g>
  <!-- Grande fenêtre : Londres sous la pluie -->
  <rect x="290" y="26" width="230" height="140" fill="#26424f"/>
  <rect x="290" y="26" width="230" height="140" fill="none" stroke="#c08a3e" stroke-width="5"/>
  <line x1="405" y1="26" x2="405" y2="166" stroke="#c08a3e" stroke-width="4"/>
  <line x1="290" y1="96" x2="520" y2="96" stroke="#c08a3e" stroke-width="4"/>
  <!-- Silhouette urbaine derrière la vitre -->
  <g fill="#16303c">
    <rect x="300" y="112" width="34" height="54"/><rect x="342" y="96" width="26" height="70"/>
    <rect x="376" y="120" width="24" height="46"/><rect x="416" y="104" width="30" height="62"/>
    <rect x="454" y="126" width="28" height="40"/><rect x="488" y="110" width="28" height="56"/>
  </g>
  <!-- Big Ben au loin -->
  <rect x="352" y="52" width="16" height="46" fill="#1b3a48"/>
  <polygon points="352,52 360,36 368,52" fill="#122b36"/>
  <circle cx="360" cy="62" r="5" fill="#e8bf72" opacity=".7"/>
  <!-- Ruissellement sur la vitre -->
  <g stroke="#9fd0e0" stroke-width="1.2" opacity=".45">
    <line class="ruissellement" x1="318" y1="30" x2="314" y2="160"/>
    <line class="ruissellement" x1="382" y1="34" x2="378" y2="164" style="animation-delay:-1.4s"/>
    <line class="ruissellement" x1="446" y1="28" x2="441" y2="158" style="animation-delay:-2.6s"/>
    <line class="ruissellement" x1="498" y1="36" x2="494" y2="162" style="animation-delay:-.7s"/>
  </g>
  <!-- Cheminée et feu -->
  <rect x="46" y="126" width="96" height="70" fill="#1a1008"/>
  <rect x="40" y="118" width="108" height="12" fill="#5a3a1e"/>
  <ellipse class="flamme-foyer" cx="94" cy="180" rx="26" ry="16" fill="#ff8a2a"/>
  <ellipse class="flamme-foyer" cx="94" cy="184" rx="15" ry="10" fill="#ffd77a" style="animation-delay:-.6s"/>
  <!-- Pendule sur la cheminée -->
  <circle cx="94" cy="100" r="16" fill="#e6d3ab" stroke="#c08a3e" stroke-width="3"/>
  <line x1="94" y1="100" x2="94" y2="90" stroke="#33261a" stroke-width="2"/>
  <line class="pendule-aiguille" x1="94" y1="100" x2="94" y2="111" stroke="#33261a" stroke-width="2"/>
  <!-- Globe terrestre sur pied -->
  <ellipse cx="580" cy="248" rx="30" ry="6" fill="#000" opacity=".35"/>
  <rect x="576" y="216" width="8" height="30" fill="#7a4a24"/>
  <circle class="globe-tourne" cx="580" cy="196" r="34" fill="#2b6f9e" stroke="#c08a3e" stroke-width="3"/>
  <path d="M556 182 q14 -8 26 2 q12 10 24 2 M556 206 q16 10 30 0 q10 -8 20 0" stroke="#3f9c86" stroke-width="5" fill="none" opacity=".85"/>
  <ellipse cx="580" cy="196" rx="34" ry="12" fill="none" stroke="#e8bf72" stroke-width="1.5" opacity=".5"/>
  <!-- Table de whist, cartes et sac de guinées -->
  <rect x="230" y="212" width="300" height="12" fill="#5a3a1e"/>
  <rect x="248" y="224" width="10" height="46" fill="#3a2415"/>
  <rect x="502" y="224" width="10" height="46" fill="#3a2415"/>
  <g transform="rotate(-8 300 206)"><rect x="286" y="196" width="26" height="18" rx="2" fill="#f7efdc" stroke="#8a5a2a"/></g>
  <g transform="rotate(6 336 204)"><rect x="322" y="194" width="26" height="18" rx="2" fill="#f7efdc" stroke="#8a5a2a"/></g>
  <ellipse cx="440" cy="204" rx="24" ry="14" fill="#9c7a3c"/>
  <text x="440" y="209" font-size="10" fill="#3a2415" text-anchor="middle" font-family="Georgia">£</text>
  <!-- Sol et halo du foyer -->
  <rect x="0" y="270" width="800" height="30" fill="#241608"/>
  <rect width="800" height="300" fill="url(#lueurFoyer)"/>
</svg>`,

/* ---- Escale 2 — L'isthme de Suez, 9 octobre 1872 ---- */
"suez": `<svg ${S}>
  <defs>
    <linearGradient id="cielDesert" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f2c98a"/>
      <stop offset="55%" stop-color="#f7dfae"/><stop offset="100%" stop-color="#fbeed0"/>
    </linearGradient>
    <linearGradient id="eauCanal" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3f8fae"/><stop offset="100%" stop-color="#1d5875"/>
    </linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielDesert)"/>
  <!-- Soleil bas et voilé -->
  <circle cx="640" cy="72" r="40" fill="#ffe9b0" opacity=".75"/>
  <circle cx="640" cy="72" r="26" fill="#fff6d8"/>
  <!-- Dunes -->
  <path d="M0 176 q120 -34 240 -6 q130 30 250 -12 q160 -34 310 6 L800 300 L0 300 Z" fill="#e0bd82"/>
  <path d="M0 208 q160 -26 300 4 q140 30 300 -8 q110 -22 200 2 L800 300 L0 300 Z" fill="#cfa669"/>
  <!-- Le canal : une longue trouée d'eau dans le sable -->
  <path d="M0 236 L800 214 L800 258 L0 286 Z" fill="url(#eauCanal)"/>
  <g class="vagues" opacity=".35">
    <path d="M0 250 q60 -6 120 0 q60 6 120 0 q60 -6 120 0 q60 6 120 0 q60 -6 120 0 q60 6 120 0" stroke="#cdeaf5" stroke-width="2" fill="none"/>
    <path d="M0 266 q60 6 120 0 q60 -6 120 0 q60 6 120 0 q60 -6 120 0 q60 6 120 0 q60 -6 120 0" stroke="#cdeaf5" stroke-width="1.5" fill="none" style="animation-delay:-2s"/>
  </g>
  <!-- Le Mongolia, vapeur des Messageries -->
  <g>
    <path d="M300 232 L520 226 L512 254 L308 258 Z" fill="#2c2118"/>
    <rect x="330" y="200" width="150" height="28" fill="#e8e0cf"/>
    <rect x="330" y="200" width="150" height="7" fill="#a33327"/>
    <rect x="392" y="164" width="17" height="38" fill="#3a2415"/>
    <rect x="392" y="164" width="17" height="9" fill="#a33327"/>
    <!-- Mât et pavillon -->
    <line x1="352" y1="200" x2="352" y2="150" stroke="#5a3a1e" stroke-width="3"/>
    <rect x="352" y="150" width="26" height="15" fill="#f0e6d0"/>
    <rect x="352" y="150" width="26" height="5" fill="#2b6f9e"/>
    <!-- Panache de vapeur -->
    <circle class="fumee" cx="400" cy="150" r="12" fill="#f4ecdc" opacity=".8"/>
    <circle class="fumee" cx="414" cy="136" r="15" fill="#eee5d3" opacity=".65" style="animation-delay:-2s"/>
    <circle class="fumee" cx="428" cy="120" r="19" fill="#e8dfcd" opacity=".5" style="animation-delay:-4s"/>
    <!-- Reflet -->
    <ellipse cx="410" cy="262" rx="105" ry="7" fill="#0f3f57" opacity=".35"/>
  </g>
  <!-- Palmiers -->
  <g>
    <rect x="96" y="176" width="7" height="60" fill="#7a5a2a"/>
    <g class="feuillage">
      <path d="M100 178 q-34 -14 -46 4 q30 -6 46 6" fill="#3f7a44"/>
      <path d="M100 178 q34 -14 46 4 q-30 -6 -46 6" fill="#356b3a"/>
      <path d="M100 176 q-8 -32 -32 -36 q20 18 26 40" fill="#3f7a44"/>
      <path d="M100 176 q8 -32 32 -36 q-20 18 -26 40" fill="#356b3a"/>
    </g>
  </g>
  <g>
    <rect x="152" y="192" width="6" height="46" fill="#6a4a24"/>
    <g class="feuillage" style="animation-delay:-1.5s">
      <path d="M155 194 q-26 -12 -36 2 q24 -4 36 5" fill="#356b3a"/>
      <path d="M155 194 q26 -12 36 2 q-24 -4 -36 5" fill="#2f6034"/>
    </g>
  </g>
  <!-- Minaret et village au loin -->
  <g fill="#d8b88c">
    <rect x="668" y="150" width="60" height="46"/><rect x="736" y="164" width="42" height="32"/>
    <rect x="700" y="112" width="13" height="44"/>
  </g>
  <circle cx="706" cy="108" r="8" fill="#e6cba0"/>
  <path d="M706 100 l0 -9" stroke="#c08a3e" stroke-width="2"/>
  <!-- Chameau et chamelier -->
  <g fill="#a5763f">
    <ellipse cx="200" cy="228" rx="24" ry="12"/>
    <path d="M182 224 q6 -14 14 -2 q8 -14 16 0" fill="#a5763f"/>
    <rect x="184" y="236" width="4" height="16"/><rect x="196" y="236" width="4" height="16"/>
    <rect x="210" y="236" width="4" height="16"/>
    <path d="M220 224 q12 -6 14 -18 q2 -8 -4 -8 q-4 8 -12 16 Z"/>
  </g>
</svg>`,

/* ---- Escale 3 — La jungle de l'Inde, près de Kholby ---- */
"inde": `<svg ${S}>
  <defs>
    <linearGradient id="cielJungle" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8fc0a8"/><stop offset="100%" stop-color="#dbe8c8"/>
    </linearGradient>
    <radialGradient id="rayonJungle" cx="62%" cy="8%" r="55%">
      <stop offset="0%" stop-color="#fffbe0" stop-opacity=".55"/>
      <stop offset="100%" stop-color="#fffbe0" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielJungle)"/>
  <!-- Contreforts de l'Himalaya au loin -->
  <polygon points="0,150 90,86 160,132 250,72 340,146 430,104 520,150" fill="#9fb3c0" opacity=".75"/>
  <polygon points="60,110 90,86 120,112" fill="#f2f6fa"/>
  <polygon points="222,100 250,72 280,104" fill="#f2f6fa"/>
  <!-- Canopée arrière -->
  <g opacity=".85" fill="#4a7a44">
    <ellipse cx="80" cy="150" rx="90" ry="52"/><ellipse cx="230" cy="140" rx="80" ry="46"/>
    <ellipse cx="640" cy="136" rx="105" ry="58"/><ellipse cx="760" cy="152" rx="80" ry="50"/>
  </g>
  <!-- Temple hindou -->
  <g>
    <polygon points="470,150 500,72 530,150" fill="#c99f6a"/>
    <rect x="466" y="150" width="68" height="58" fill="#d8b184"/>
    <rect x="490" y="176" width="20" height="32" fill="#4a2f18"/>
    <circle cx="500" cy="66" r="6" fill="#e8bf72"/>
    <g fill="#b8895a"><rect x="466" y="150" width="68" height="6"/><rect x="472" y="164" width="56" height="4"/></g>
  </g>
  <!-- Voie ferrée inachevée : les rails s'arrêtent net -->
  <rect x="0" y="238" width="800" height="62" fill="#8a7a52"/>
  <g>
    <rect x="0" y="252" width="330" height="5" fill="#5a4a30"/>
    <rect x="0" y="268" width="330" height="5" fill="#5a4a30"/>
    <g fill="#4a3a24">
      <rect x="10" y="248" width="9" height="30"/><rect x="56" y="248" width="9" height="30"/>
      <rect x="102" y="248" width="9" height="30"/><rect x="148" y="248" width="9" height="30"/>
      <rect x="194" y="248" width="9" height="30"/><rect x="240" y="248" width="9" height="30"/>
      <rect x="286" y="248" width="9" height="30"/>
    </g>
    <!-- Panneau : fin des travaux -->
    <rect x="336" y="216" width="4" height="42" fill="#5a3a1e"/>
    <rect x="316" y="204" width="46" height="18" rx="2" fill="#f0e2c4" stroke="#a33327" stroke-width="2"/>
    <text x="339" y="217" font-size="9" fill="#a33327" text-anchor="middle" font-family="Georgia">STOP</text>
  </g>
  <!-- L'éléphant Kiouni, avec son howdah -->
  <g>
    <ellipse cx="600" cy="232" rx="66" ry="42" fill="#8c8880"/>
    <ellipse cx="546" cy="216" rx="30" ry="28" fill="#98948c"/>
    <ellipse class="oreille-elephant" cx="536" cy="214" rx="18" ry="22" fill="#807c74"/>
    <path class="trompe" d="M528 228 q-20 16 -12 36 q4 10 14 6" stroke="#98948c" stroke-width="11" fill="none" stroke-linecap="round"/>
    <path d="M534 224 q-14 8 -20 18" stroke="#f0ece0" stroke-width="4" fill="none" stroke-linecap="round"/>
    <g fill="#7a766e"><rect x="560" y="264" width="15" height="30" rx="4"/><rect x="592" y="266" width="15" height="28" rx="4"/>
      <rect x="626" y="264" width="15" height="30" rx="4"/><rect x="652" y="266" width="14" height="28" rx="4"/></g>
    <!-- Howdah (nacelle) -->
    <rect x="576" y="176" width="56" height="26" rx="4" fill="#a33327"/>
    <rect x="576" y="172" width="56" height="8" rx="3" fill="#c08a3e"/>
    <line x1="580" y1="172" x2="580" y2="156" stroke="#c08a3e" stroke-width="3"/>
    <line x1="628" y1="172" x2="628" y2="156" stroke="#c08a3e" stroke-width="3"/>
    <rect x="576" y="150" width="56" height="8" rx="3" fill="#8a5f24"/>
  </g>
  <!-- Feuillages du premier plan -->
  <g class="feuillage">
    <path d="M0 300 q30 -70 20 -120 q26 62 44 120 Z" fill="#2f6034"/>
    <path d="M40 300 q40 -50 62 -76 q-14 44 -20 76 Z" fill="#3a7040"/>
  </g>
  <g class="feuillage" style="animation-delay:-2s">
    <path d="M800 300 q-34 -74 -22 -128 q-28 66 -48 128 Z" fill="#2f6034"/>
    <path d="M756 300 q-42 -52 -66 -80 q16 46 22 80 Z" fill="#3a7040"/>
  </g>
  <rect width="800" height="300" fill="url(#rayonJungle)"/>
</svg>`,

/* ---- Escale 4 — La mer de Chine, à bord de la Tankadère ---- */
"mer-chine": `<svg ${S}>
  <defs>
    <linearGradient id="cielTempete" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2b3a4a"/><stop offset="60%" stop-color="#4a5a68"/>
      <stop offset="100%" stop-color="#6c7c86"/>
    </linearGradient>
    <linearGradient id="merHoule" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#26505f"/><stop offset="100%" stop-color="#0f2c3a"/>
    </linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielTempete)"/>
  <!-- Nuages d'orage -->
  <g fill="#1e2c39" opacity=".8">
    <ellipse cx="140" cy="52" rx="130" ry="42"/><ellipse cx="330" cy="36" rx="150" ry="38"/>
    <ellipse cx="560" cy="56" rx="140" ry="44"/><ellipse cx="740" cy="40" rx="110" ry="36"/>
  </g>
  <!-- Éclair -->
  <polygon class="eclair" points="300,52 288,116 308,112 292,178 336,102 314,106 330,52" fill="#fff6c8"/>
  <!-- Horizon -->
  <rect x="0" y="150" width="800" height="150" fill="url(#merHoule)"/>
  <!-- Vagues successives -->
  <g class="vagues">
    <path d="M0 168 q60 -22 120 0 q60 22 120 0 q60 -22 120 0 q60 22 120 0 q60 -22 120 0 q60 22 120 0 L800 300 L0 300 Z" fill="#1c4453" opacity=".9"/>
  </g>
  <g class="vagues" style="animation-delay:-1.6s">
    <path d="M0 200 q70 -26 140 0 q70 26 140 0 q70 -26 140 0 q70 26 140 0 q70 -26 140 0 L800 300 L0 300 Z" fill="#153745"/>
  </g>
  <g class="vagues" style="animation-delay:-3.2s">
    <path d="M0 244 q80 -30 160 0 q80 30 160 0 q80 -30 160 0 q80 30 160 0 q80 -30 160 0 L800 300 L0 300 Z" fill="#0e2733"/>
  </g>
  <!-- Écume -->
  <g stroke="#cfe6ef" stroke-width="2" fill="none" opacity=".5">
    <path d="M60 198 q22 -10 44 0"/><path d="M300 232 q26 -12 52 0"/><path d="M600 210 q24 -11 48 0"/>
  </g>
  <!-- La Tankadère, goélette gîtée dans la houle -->
  <g class="navire" transform="translate(400 196)">
    <path d="M-84 12 L86 6 L68 44 L-64 48 Z" fill="#3a2415"/>
    <path d="M-84 12 L86 6 L84 16 L-82 22 Z" fill="#c08a3e"/>
    <!-- Mâts -->
    <line x1="-28" y1="10" x2="-34" y2="-92" stroke="#4a3018" stroke-width="4"/>
    <line x1="40" y1="8" x2="34" y2="-64" stroke="#4a3018" stroke-width="4"/>
    <!-- Voiles gonflées -->
    <path d="M-32 -88 q52 26 40 82 L-30 6 Z" fill="#e8e0cd"/>
    <path d="M-36 -84 q-38 30 -30 84 L-30 4 Z" fill="#dcd3bd"/>
    <path d="M36 -60 q36 20 28 62 L38 6 Z" fill="#e8e0cd"/>
    <!-- Pavillon -->
    <rect x="-38" y="-96" width="22" height="12" fill="#a33327"/>
  </g>
  <!-- Rideau de pluie -->
  <g class="pluie-oblique" stroke="#b8d8e4" stroke-width="1.2" opacity=".4">
    <line x1="40" y1="0" x2="16" y2="80"/><line x1="140" y1="0" x2="116" y2="80"/>
    <line x1="240" y1="0" x2="216" y2="80"/><line x1="340" y1="0" x2="316" y2="80"/>
    <line x1="440" y1="0" x2="416" y2="80"/><line x1="540" y1="0" x2="516" y2="80"/>
    <line x1="640" y1="0" x2="616" y2="80"/><line x1="740" y1="0" x2="716" y2="80"/>
  </g>
</svg>`,

/* ---- Escale 5 — L'observatoire de Greenwich, Londres ---- */
"greenwich": `<svg ${S}>
  <defs>
    <linearGradient id="cielNuit" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a1626"/><stop offset="60%" stop-color="#16334c"/>
      <stop offset="100%" stop-color="#2d5570"/>
    </linearGradient>
    <radialGradient id="haloMeridien" cx="50%" cy="100%" r="60%">
      <stop offset="0%" stop-color="#3f9c86" stop-opacity=".38"/>
      <stop offset="100%" stop-color="#3f9c86" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielNuit)"/>
  <!-- Étoiles -->
  <g class="etoiles" fill="#fff">
    <circle cx="70" cy="40" r="1.4"/><circle cx="160" cy="72" r="1"/><circle cx="248" cy="34" r="1.6"/>
    <circle cx="330" cy="60" r="1.1"/><circle cx="470" cy="30" r="1.5"/><circle cx="556" cy="66" r="1"/>
    <circle cx="640" cy="42" r="1.3"/><circle cx="726" cy="74" r="1.1"/><circle cx="392" cy="88" r="1"/>
    <circle cx="120" cy="104" r="1"/><circle cx="690" cy="106" r="1.2"/>
  </g>
  <!-- Lune -->
  <circle cx="700" cy="52" r="22" fill="#f2ecd6"/>
  <circle cx="691" cy="46" r="4" fill="#dcd4bc" opacity=".7"/>
  <circle cx="706" cy="60" r="6" fill="#dcd4bc" opacity=".55"/>
  <!-- Coupole de l'observatoire -->
  <g>
    <rect x="286" y="140" width="126" height="86" fill="#2a3d4e"/>
    <rect x="286" y="140" width="126" height="9" fill="#c08a3e"/>
    <path d="M286 140 q63 -56 126 0 Z" fill="#3a5266"/>
    <path d="M330 118 l0 -34 l14 0 l0 30" fill="#1c2c3a"/>
    <!-- Boule horaire rouge de Greenwich -->
    <rect x="346" y="52" width="5" height="34" fill="#8a5f24"/>
    <circle cx="348" cy="50" r="11" fill="#a33327" stroke="#c08a3e" stroke-width="2"/>
    <!-- Fenêtres éclairées -->
    <g fill="#e8bf72" opacity=".85">
      <rect x="302" y="166" width="14" height="20"/><rect x="332" y="166" width="14" height="20"/>
      <rect x="362" y="166" width="14" height="20"/><rect x="392" y="166" width="12" height="20"/>
    </g>
  </g>
  <!-- Bâtiments annexes -->
  <rect x="150" y="176" width="120" height="50" fill="#22323f"/>
  <rect x="428" y="182" width="140" height="44" fill="#22323f"/>
  <g fill="#e8bf72" opacity=".6">
    <rect x="166" y="192" width="11" height="15"/><rect x="196" y="192" width="11" height="15"/>
    <rect x="226" y="192" width="11" height="15"/><rect x="446" y="196" width="11" height="14"/>
    <rect x="480" y="196" width="11" height="14"/><rect x="514" y="196" width="11" height="14"/>
  </g>
  <!-- Big Ben au loin, à droite -->
  <g>
    <rect x="640" y="130" width="26" height="96" fill="#1c2c3a"/>
    <polygon points="640,130 653,104 666,130" fill="#16232e"/>
    <circle cx="653" cy="150" r="10" fill="#f2e4c8"/>
    <line x1="653" y1="150" x2="653" y2="144" stroke="#33261a" stroke-width="1.6"/>
    <line class="pendule-aiguille" x1="653" y1="150" x2="653" y2="157" stroke="#33261a" stroke-width="1.6"/>
  </g>
  <!-- Le sol -->
  <rect x="0" y="226" width="800" height="74" fill="#16232e"/>
  <!-- LA LIGNE DU MÉRIDIEN : le cœur de l'énigme finale -->
  <rect width="800" height="300" fill="url(#haloMeridien)"/>
  <g>
    <rect x="346" y="226" width="6" height="74" fill="#3f9c86"/>
    <rect class="ligne-meridien" x="346" y="226" width="6" height="74" fill="#7fe8cf" opacity=".7"/>
    <text x="376" y="252" font-size="11" fill="#7fe8cf" font-family="Georgia">0°</text>
    <text x="228" y="272" font-size="10" fill="#cfe0ea" font-family="Georgia" text-anchor="middle">← OUEST</text>
    <text x="486" y="272" font-size="10" fill="#cfe0ea" font-family="Georgia" text-anchor="middle">EST →</text>
  </g>
  <!-- Plaque de laiton gravée -->
  <rect x="86" y="240" width="120" height="26" rx="4" fill="#c08a3e"/>
  <text x="146" y="257" font-size="9" fill="#3a2415" text-anchor="middle" font-family="Georgia" letter-spacing="1">GREENWICH</text>
</svg>`,
};

window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.ETAPE_FICHIER = ETAPE_FICHIER;
