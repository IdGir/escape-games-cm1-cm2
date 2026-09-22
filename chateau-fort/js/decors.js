/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de « Le Secret du donjon »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux :
     motte        la motte et la palissade, chantier de pierre
     remparts     le chemin de ronde au-dessus de l'entrée
     grandesalle  la grande salle du donjon
     village      le village de torchis et les champs en bandes
     moulin       le moulin à eau et le four du seigneur
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["motte"];
  const sens = (contenu.sens||[]).map(s=>`<span>${s}</span>`).join("");
  return `
    <div class="scene scene--media" data-salle="${salle}" data-media="salle${SALLE_NUM[salle]||1}">
      <div class="decor-fallback">${svg}</div>
      <div class="decor-overlay"></div>
      <div class="decor-contenu">
        <span class="lieu">${contenu.lieu||""}</span>
        <p class="description">${contenu.description||""}</p>
        ${sens?`<div class="sens">${sens}</div>`:""}
      </div>
    </div>`;
}

/** Active la scène : cherche le média (vidéo puis image). */
function activerScene(sceneEl){
  if(!sceneEl) return;
  if(typeof nettoyerVideos === "function") nettoyerVideos();
  const base = sceneEl.dataset.media;
  if(base && typeof installerDecor === "function") installerDecor(sceneEl, base);
}

const SALLE_NUM = { "motte":1, "remparts":2, "grandesalle":3, "village":4, "moulin":5 };

/* ---- Fragments communs ---- */
const CIEL_MATIN = `
  <linearGradient id="cielMatin" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#8fb3d9"/><stop offset="65%" stop-color="#e7d9b8"/><stop offset="100%" stop-color="#f2e6c8"/>
  </linearGradient>`;
const NUAGES = `
  <g opacity=".6">
    <ellipse cx="120" cy="44" rx="58" ry="14" fill="#fff"><animate attributeName="cx" values="100;700;100" dur="100s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="560" cy="30" rx="40" ry="11" fill="#fff"><animate attributeName="cx" values="540;-60;540" dur="130s" repeatCount="indefinite"/></ellipse>
  </g>`;
const OISEAUX = `
  <g stroke="#3a3a3a" stroke-width="1.6" fill="none" opacity=".7">
    <path d="M0 0 q5 -5 10 0 q5 -5 10 0"><animateMotion dur="38s" repeatCount="indefinite" path="M-40 70 L840 40"/></path>
    <path d="M0 0 q4 -4 8 0 q4 -4 8 0"><animateMotion dur="44s" repeatCount="indefinite" path="M-80 90 L860 60"/></path>
  </g>`;

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — La motte et la palissade
   ------------------------------------------------------------ */
"motte": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_MATIN}
    <linearGradient id="terreM" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#9c7a4f"/><stop offset="100%" stop-color="#6e5232"/></linearGradient>
    <linearGradient id="herbeM" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#8fae62"/><stop offset="100%" stop-color="#5f7d3c"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielMatin)"/>
  ${NUAGES}${OISEAUX}
  <path d="M0 190 Q200 150 400 176 T800 168 L800 300 L0 300 Z" fill="#a7bf82" opacity=".7"/>
  <rect y="222" width="800" height="78" fill="url(#herbeM)"/>
  <!-- fossé -->
  <path d="M150 238 Q330 262 520 238" stroke="#5f8fb0" stroke-width="12" fill="none" opacity=".85"/>
  <!-- motte -->
  <path d="M200 236 L270 120 L390 120 L460 236 Z" fill="url(#terreM)"/>
  <!-- vieille tour de bois -->
  <g transform="translate(300,56)">
    <rect width="60" height="66" fill="#8a5d33" stroke="#4a2f16" stroke-width="2"/>
    <g stroke="#4a2f16" stroke-width="1.2"><line x1="15" y1="0" x2="15" y2="66"/><line x1="30" y1="0" x2="30" y2="66"/><line x1="45" y1="0" x2="45" y2="66"/></g>
    <path d="M-6 2 L30 -26 L66 2 Z" fill="#5d3e20"/>
    <rect x="24" y="36" width="12" height="18" fill="#2b1a0c"/>
  </g>
  <!-- palissade -->
  <g fill="#7a5230" stroke="#4a2f16" stroke-width="1">
    ${Array.from({length:14},(_,i)=>`<path d="M${270+i*9} 122 l0 -18 l4 -5 l4 5 l0 18 Z"/>`).join("")}
  </g>
  <!-- chantier de pierre : mur qui monte, échafaudage, treuil -->
  <g transform="translate(540,120)">
    <rect x="0" y="40" width="170" height="76" fill="#cfc3a8" stroke="#6e6452" stroke-width="2"/>
    <g stroke="#9a8e76" stroke-width="1">${[52,64,76,88,100].map(y=>`<line x1="0" y1="${y}" x2="170" y2="${y}"/>`).join("")}</g>
    <g stroke="#6d4a28" stroke-width="3"><line x1="-6" y1="116" x2="-6" y2="10"/><line x1="176" y1="116" x2="176" y2="10"/><line x1="-6" y1="30" x2="176" y2="30"/></g>
    <g transform="translate(80,0)">
      <circle r="14" fill="none" stroke="#6d4a28" stroke-width="3"><animateTransform attributeName="transform" type="rotate" values="0;360" dur="9s" repeatCount="indefinite"/></circle>
      <line x1="0" y1="0" x2="0" y2="30" stroke="#444" stroke-width="1.5"/>
      <rect x="-8" y="30" width="16" height="10" fill="#bdb094"><animate attributeName="y" values="36;20;36" dur="9s" repeatCount="indefinite"/></rect>
    </g>
  </g>
  <!-- charrette de pierres -->
  <g transform="translate(470,236)">
    <rect x="0" y="-22" width="60" height="16" fill="#8a5d33"/>
    <g fill="#bdb094"><rect x="6" y="-32" width="14" height="10"/><rect x="24" y="-34" width="16" height="12"/><rect x="42" y="-30" width="12" height="8"/></g>
    <circle cx="14" cy="-4" r="9" fill="none" stroke="#4a2f16" stroke-width="3"/><circle cx="48" cy="-4" r="9" fill="none" stroke="#4a2f16" stroke-width="3"/>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — Les remparts : entrée, douves, pont-levis, herse
   ------------------------------------------------------------ */
"remparts": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="cielGris" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#7d8fa3"/><stop offset="100%" stop-color="#c9ced3"/></linearGradient>
    <linearGradient id="pierreR" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#c6bba4"/><stop offset="100%" stop-color="#958a73"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielGris)"/>
  ${NUAGES}
  <rect y="250" width="800" height="50" fill="#6f8f4f"/>
  <!-- douves -->
  <rect y="236" width="800" height="26" fill="#5c87a6"/>
  <g stroke="#9fc1d8" stroke-width="1.5" opacity=".7" fill="none">
    <path d="M0 246 q20 -4 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0"><animateTransform attributeName="transform" type="translate" values="0 0;-40 0;0 0" dur="6s" repeatCount="indefinite"/></path>
  </g>
  <!-- courtine -->
  <rect x="0" y="100" width="800" height="136" fill="url(#pierreR)"/>
  <g fill="url(#pierreR)">${Array.from({length:20},(_,i)=>`<rect x="${i*42}" y="80" width="24" height="22"/>`).join("")}</g>
  <!-- mâchicoulis au-dessus de la porte -->
  <g transform="translate(330,86)"><rect width="140" height="18" fill="#a89c84" stroke="#6e6452"/>
    <g fill="#3a2e22">${[8,32,56,80,104,128].map(x=>`<rect x="${x}" y="18" width="8" height="8"/>`).join("")}</g></g>
  <!-- tours rondes -->
  <g><rect x="70" y="60" width="110" height="180" fill="#b3a88f" stroke="#6e6452" stroke-width="2"/><path d="M60 62 L125 12 L190 62 Z" fill="#5a4b6b"/>
     <rect x="120" y="130" width="6" height="30" fill="#2b2b2b"/></g>
  <g><rect x="620" y="60" width="110" height="180" fill="#b3a88f" stroke="#6e6452" stroke-width="2"/><path d="M610 62 L675 12 L740 62 Z" fill="#5a4b6b"/>
     <rect x="672" y="130" width="6" height="30" fill="#2b2b2b"/></g>
  <!-- porte, herse, pont-levis -->
  <path d="M360 236 L360 170 Q400 130 440 170 L440 236 Z" fill="#2a2017"/>
  <g stroke="#555" stroke-width="4">
    <g><animateTransform attributeName="transform" type="translate" values="0 0;0 -8;0 0" dur="7s" repeatCount="indefinite"/>
      ${[370,384,398,412,426].map(x=>`<line x1="${x}" y1="150" x2="${x}" y2="212"/>`).join("")}
      <line x1="362" y1="172" x2="438" y2="172"/><line x1="362" y1="196" x2="438" y2="196"/>
    </g>
  </g>
  <path d="M360 236 L318 136 L330 132 L372 232 Z" fill="#7a5230" stroke="#4a2f16"/>
  <line x1="324" y1="134" x2="362" y2="104" stroke="#333" stroke-width="1.5"/>
  <!-- bannière -->
  <g transform="translate(125,12)"><line x1="0" y1="0" x2="0" y2="-10" stroke="#333" stroke-width="2"/>
    <path d="M0 -10 L26 -6 L0 -1 Z" fill="#8f2d24"><animate attributeName="d" values="M0 -10 L26 -6 L0 -1 Z;M0 -10 L24 -3 L0 -1 Z;M0 -10 L26 -6 L0 -1 Z" dur="2.4s" repeatCount="indefinite"/></path></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — La grande salle du donjon
   ------------------------------------------------------------ */
"grandesalle": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murGS" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#6f6250"/><stop offset="100%" stop-color="#4a3f33"/></linearGradient>
    <radialGradient id="feuGS" cx="50%" cy="80%" r="60%"><stop offset="0%" stop-color="#ffd27a"/><stop offset="60%" stop-color="#e0782a"/><stop offset="100%" stop-color="#8a2f10" stop-opacity="0"/></radialGradient>
    <radialGradient id="lueurGS" cx="50%" cy="70%" r="60%"><stop offset="0%" stop-color="#ffb35c" stop-opacity=".35"/><stop offset="100%" stop-color="#ffb35c" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murGS)"/>
  <g stroke="#3d342a" stroke-width="1" opacity=".5">${[40,80,120,160,200].map(y=>`<line x1="0" y1="${y}" x2="800" y2="${y}"/>`).join("")}</g>
  <!-- poutres -->
  <g fill="#3b2a1a">${[0,160,320,480,640].map(x=>`<rect x="${x}" y="0" width="160" height="14"/>`).join("")}<rect x="0" y="12" width="800" height="6"/></g>
  <!-- tapisseries -->
  <g><rect x="60" y="50" width="120" height="130" fill="#7a2a2a"/><rect x="68" y="58" width="104" height="114" fill="none" stroke="#c9a227" stroke-width="2"/>
     <path d="M120 80 L100 150 L140 150 Z" fill="#c9a227" opacity=".8"/><circle cx="120" cy="80" r="10" fill="#c9a227" opacity=".8"/></g>
  <g><rect x="620" y="50" width="120" height="130" fill="#23466b"/><rect x="628" y="58" width="104" height="114" fill="none" stroke="#c9a227" stroke-width="2"/>
     <path d="M660 150 Q680 90 700 150" stroke="#c9a227" stroke-width="4" fill="none"/></g>
  <!-- cheminée -->
  <g transform="translate(320,40)">
    <path d="M0 0 L160 0 L180 40 L-20 40 Z" fill="#8e8270"/>
    <rect x="10" y="40" width="140" height="140" fill="#2a2119"/>
    <rect x="-10" y="40" width="20" height="140" fill="#8e8270"/><rect x="150" y="40" width="20" height="140" fill="#8e8270"/>
    <ellipse cx="80" cy="165" rx="50" ry="28" fill="url(#feuGS)"><animate attributeName="ry" values="26;32;24;30;26" dur="1.6s" repeatCount="indefinite"/></ellipse>
    <g fill="#3b2a1a"><rect x="40" y="170" width="80" height="8" rx="3"/></g>
  </g>
  <ellipse cx="400" cy="230" rx="330" ry="120" fill="url(#lueurGS)"><animate attributeName="opacity" values=".8;1;.85;1;.8" dur="2s" repeatCount="indefinite"/></ellipse>
  <!-- longue table sur tréteaux -->
  <rect y="238" width="800" height="62" fill="#3a2e22"/>
  <g transform="translate(150,214)">
    <rect width="500" height="14" fill="#7a5230" stroke="#4a2f16"/>
    <g stroke="#4a2f16" stroke-width="5"><line x1="30" y1="14" x2="10" y2="50"/><line x1="30" y1="14" x2="50" y2="50"/><line x1="470" y1="14" x2="450" y2="50"/><line x1="470" y1="14" x2="490" y2="50"/></g>
    <g fill="#d8c29a"><ellipse cx="120" cy="-4" rx="20" ry="6"/><ellipse cx="250" cy="-6" rx="28" ry="8"/><ellipse cx="380" cy="-4" rx="20" ry="6"/></g>
    <g fill="#c9a227"><rect x="190" y="-16" width="8" height="14"/><rect x="300" y="-16" width="8" height="14"/></g>
  </g>
  <!-- blason -->
  <g transform="translate(400,24)"><path d="M-14 0 L14 0 L14 14 Q0 28 -14 14 Z" fill="#8f2d24" stroke="#c9a227" stroke-width="2"/><path d="M-6 6 L6 6 L0 16 Z" fill="#c9a227"/></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — Le village et les champs
   ------------------------------------------------------------ */
"village": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_MATIN}</defs>
  <rect width="800" height="300" fill="url(#cielMatin)"/>
  ${NUAGES}${OISEAUX}
  <!-- château au loin -->
  <g transform="translate(600,60)" opacity=".75"><rect x="0" y="30" width="120" height="60" fill="#b3a88f"/><rect x="44" y="0" width="32" height="90" fill="#a39781"/>
    <g fill="#b3a88f">${[0,20,40,60,80,100].map(x=>`<rect x="${x}" y="22" width="12" height="10"/>`).join("")}</g></g>
  <path d="M0 160 Q200 130 400 150 T800 140 L800 300 L0 300 Z" fill="#9cb86e"/>
  <!-- champs en bandes -->
  <g>${[0,1,2,3,4,5,6].map(i=>`<path d="M${i*120-40} 170 L${i*120+80} 170 L${i*120+120} 300 L${i*120} 300 Z" fill="${["#d9c36a","#8fae62","#b58a54","#d9c36a","#8fae62","#b58a54","#d9c36a"][i]}" opacity=".85"/>`).join("")}</g>
  <!-- blé qui ondule -->
  <g stroke="#b99a3a" stroke-width="2">
    <g><animateTransform attributeName="transform" type="skewX" values="0;4;0;-3;0" dur="5s" repeatCount="indefinite"/>
    ${Array.from({length:18},(_,i)=>`<line x1="${20+i*8}" y1="236" x2="${22+i*8}" y2="222"/>`).join("")}</g>
  </g>
  <!-- église -->
  <g transform="translate(330,94)"><rect x="0" y="30" width="60" height="50" fill="#d8ccb0" stroke="#6e6452"/><rect x="18" y="0" width="24" height="34" fill="#cfc3a8" stroke="#6e6452"/>
    <path d="M14 2 L30 -18 L46 2 Z" fill="#6e5a4a"/><path d="M-4 32 L30 14 L64 32 Z" fill="#8a6e4a"/></g>
  <!-- maisons de torchis, toits de chaume -->
  ${[[150,150],[230,158],[430,152],[510,160],[80,164]].map(([x,y])=>`
  <g transform="translate(${x},${y})"><rect x="0" y="14" width="56" height="30" fill="#e3d2a8" stroke="#8a7348"/>
    <g stroke="#6d4a28" stroke-width="2"><line x1="0" y1="14" x2="56" y2="44"/><line x1="56" y1="14" x2="0" y2="44"/></g>
    <rect x="22" y="26" width="12" height="18" fill="#5d3e20"/>
    <path d="M-6 16 L28 -10 L62 16 Z" fill="#c9a954" stroke="#8a7030"/></g>`).join("")}
  <!-- fumée -->
  <g fill="#ddd" opacity=".6"><circle cx="180" cy="130" r="6"><animate attributeName="cy" values="136;96" dur="5s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0" dur="5s" repeatCount="indefinite"/></circle>
    <circle cx="460" cy="130" r="5"><animate attributeName="cy" values="138;100" dur="6s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0" dur="6s" repeatCount="indefinite"/></circle></g>
  <!-- oies -->
  <g fill="#f4f1ea"><ellipse cx="300" cy="258" rx="10" ry="6"><animate attributeName="cx" values="300;330;300" dur="12s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="320" cy="266" rx="9" ry="5"><animate attributeName="cx" values="320;350;320" dur="12s" repeatCount="indefinite"/></ellipse></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — Le moulin à eau et le four du seigneur
   ------------------------------------------------------------ */
"moulin": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_MATIN}</defs>
  <rect width="800" height="300" fill="url(#cielMatin)"/>
  ${NUAGES}
  <path d="M0 170 Q200 140 400 160 T800 150 L800 300 L0 300 Z" fill="#8fae62"/>
  <!-- rivière -->
  <path d="M0 240 Q200 226 400 244 T800 236 L800 280 Q600 290 400 276 T0 282 Z" fill="#5c87a6"/>
  <g stroke="#9fc1d8" stroke-width="1.5" fill="none" opacity=".7"><path d="M40 258 q20 -4 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0"><animateTransform attributeName="transform" type="translate" values="0 0;-40 0" dur="3s" repeatCount="indefinite"/></path></g>
  <!-- bâtiment du moulin -->
  <g transform="translate(300,110)">
    <rect width="200" height="130" fill="#cfc3a8" stroke="#6e6452" stroke-width="2"/>
    <path d="M-14 4 L100 -50 L214 4 Z" fill="#8a3a2a" stroke="#5e2618"/>
    <rect x="80" y="70" width="40" height="60" fill="#5d3e20"/>
    <rect x="30" y="30" width="24" height="24" fill="#3a2e22"/><rect x="146" y="30" width="24" height="24" fill="#3a2e22"/>
    <!-- sacs marqués d'une croix -->
    <g><rect x="130" y="100" width="22" height="30" rx="6" fill="#e9dfc6" stroke="#9a8e76"/><path d="M136 108 l10 14 M146 108 l-10 14" stroke="#8f2d24" stroke-width="2"/></g>
    <g><rect x="156" y="104" width="22" height="26" rx="6" fill="#e9dfc6" stroke="#9a8e76"/><path d="M162 110 l10 12 M172 110 l-10 12" stroke="#8f2d24" stroke-width="2"/></g>
  </g>
  <!-- roue à aubes -->
  <g transform="translate(270,210)">
    <g><animateTransform attributeName="transform" type="rotate" values="0;-360" dur="12s" repeatCount="indefinite"/>
      <circle r="50" fill="none" stroke="#6d4a28" stroke-width="6"/><circle r="10" fill="#6d4a28"/>
      ${[0,30,60,90,120,150].map(a=>`<line x1="0" y1="-50" x2="0" y2="50" stroke="#6d4a28" stroke-width="4" transform="rotate(${a})"/>`).join("")}
      ${[0,30,60,90,120,150,180,210,240,270,300,330].map(a=>`<rect x="-6" y="-60" width="12" height="14" fill="#8a5d33" transform="rotate(${a})"/>`).join("")}
    </g>
  </g>
  <!-- four banal -->
  <g transform="translate(580,170)">
    <path d="M0 70 L0 30 Q60 -20 120 30 L120 70 Z" fill="#b58a54" stroke="#6e5232" stroke-width="2"/>
    <path d="M44 70 L44 46 Q60 30 76 46 L76 70 Z" fill="#2a1a10"/>
    <ellipse cx="60" cy="62" rx="12" ry="7" fill="#ff9a3c"><animate attributeName="opacity" values=".7;1;.6;1;.7" dur="1.4s" repeatCount="indefinite"/></ellipse>
    <g fill="#ddd" opacity=".6"><circle cx="100" cy="20" r="6"><animate attributeName="cy" values="22;-20" dur="5s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0" dur="5s" repeatCount="indefinite"/></circle></g>
  </g>
  <!-- farine en suspension -->
  <g fill="#fff" opacity=".5">${[0,1,2,3,4,5].map(i=>`<circle cx="${390+i*14}" cy="190" r="1.8"><animate attributeName="cy" values="${196-i*2};${150-i*3};${196-i*2}" dur="${4+i}s" repeatCount="indefinite"/></circle>`).join("")}</g>
</svg>`
};

window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
