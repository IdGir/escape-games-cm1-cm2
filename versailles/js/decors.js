/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de « De l'édit de Nantes à Versailles »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux :
     imprimerie  l'atelier de Suzanne, la presse et les feuilles (1598)
     rue         la rue des deux voisins, l'église et le crieur (1598)
     jardins     les jardins de Versailles, le château au fond (1682)
     chambre     la chambre du roi, la balustrade dorée
     conseil     le cabinet du Conseil, la table au tapis vert
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["imprimerie"];
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

const SALLE_NUM = { "imprimerie":1, "rue":2, "jardins":3, "chambre":4, "conseil":5 };

/* ---- Fragments communs ---- */
const CIEL_JOUR = `
  <linearGradient id="cielJour" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#8fb8de"/><stop offset="70%" stop-color="#e6ecd8"/><stop offset="100%" stop-color="#f1ead2"/>
  </linearGradient>`;
const NUAGES = `
  <g opacity=".65">
    <ellipse cx="140" cy="40" rx="58" ry="13" fill="#fff"><animate attributeName="cx" values="120;700;120" dur="110s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="580" cy="28" rx="42" ry="10" fill="#fff"><animate attributeName="cx" values="560;-60;560" dur="140s" repeatCount="indefinite"/></ellipse>
  </g>`;
const OISEAUX = `
  <g stroke="#3a3a3a" stroke-width="1.6" fill="none" opacity=".7">
    <path d="M0 0 q5 -5 10 0 q5 -5 10 0"><animateMotion dur="40s" repeatCount="indefinite" path="M-40 60 L840 34"/></path>
    <path d="M0 0 q4 -4 8 0 q4 -4 8 0"><animateMotion dur="46s" repeatCount="indefinite" path="M-80 80 L860 52"/></path>
  </g>`;
/* Flamme de bougie animée (x, y) */
const flamme = (x, y) => `<g transform="translate(${x},${y})"><rect x="-3" y="0" width="6" height="18" fill="#f3ecd8" stroke="#c9b98f" stroke-width=".6"/>
  <path d="M0 -12 Q5 -4 0 0 Q-5 -4 0 -12 Z" fill="#ffb23c"><animateTransform attributeName="transform" type="scale" values="1 1;1 1.25;.95 1;1 1.15;1 1" dur="1.3s" repeatCount="indefinite"/></path>
  <circle cy="-5" r="12" fill="#ffd27a" opacity=".22"><animate attributeName="opacity" values=".15;.3;.18;.28;.15" dur="1.6s" repeatCount="indefinite"/></circle></g>`;

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — L'imprimerie de Suzanne (1598)
   ------------------------------------------------------------ */
"imprimerie": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murI" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d9c7a4"/><stop offset="100%" stop-color="#b79e74"/></linearGradient>
    <linearGradient id="solI" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#7a5a3a"/><stop offset="100%" stop-color="#4e3722"/></linearGradient>
    <linearGradient id="rayonI" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fff6d6" stop-opacity=".55"/><stop offset="100%" stop-color="#fff6d6" stop-opacity="0"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murI)"/>
  <rect y="236" width="800" height="64" fill="url(#solI)"/>
  <!-- poutres -->
  <g fill="#5e4128"><rect y="0" width="800" height="16"/><rect x="60" y="16" width="14" height="220"/><rect x="420" y="16" width="14" height="220"/><rect x="740" y="16" width="14" height="220"/></g>
  <!-- fenêtre et rayon de lumière -->
  <g transform="translate(110,40)">
    <rect width="120" height="100" fill="#cfe2ef" stroke="#5e4128" stroke-width="6"/>
    <g stroke="#5e4128" stroke-width="2"><line x1="60" y1="0" x2="60" y2="100"/><line x1="0" y1="50" x2="120" y2="50"/></g>
  </g>
  <path d="M110 140 L230 140 L420 236 L190 236 Z" fill="url(#rayonI)"><animate attributeName="opacity" values=".8;1;.8" dur="7s" repeatCount="indefinite"/></path>
  <!-- feuilles qui sèchent sur un fil -->
  <line x1="460" y1="42" x2="730" y2="52" stroke="#6b5a44" stroke-width="1.5"/>
  ${[0,1,2,3,4].map(i=>`<g transform="translate(${478+i*50},${44+i*2})"><rect x="-16" y="0" width="32" height="40" fill="#fbf6e8" stroke="#bfb193">
    <animateTransform attributeName="transform" type="rotate" values="-3 0 0;3 0 0;-3 0 0" dur="${4+i*.6}s" repeatCount="indefinite"/></rect>
    <g stroke="#6d6253" stroke-width="1"><line x1="-10" y1="8" x2="10" y2="8"/><line x1="-10" y1="14" x2="10" y2="14"/><line x1="-10" y1="20" x2="6" y2="20"/></g></g>`).join("")}
  <!-- la presse à bras -->
  <g transform="translate(470,110)">
    <rect x="0" y="0" width="16" height="130" fill="#6b4a2b"/><rect x="120" y="0" width="16" height="130" fill="#6b4a2b"/>
    <rect x="-6" y="-8" width="148" height="18" fill="#7a5532"/>
    <rect x="0" y="70" width="136" height="12" fill="#7a5532"/>
    <rect x="-20" y="96" width="176" height="14" fill="#8a6440"/>
    <g>
      <rect x="62" y="10" width="12" height="40" fill="#4a4a4a"/>
      <rect x="44" y="48" width="48" height="14" fill="#5e5e5e"/>
      <g><line x1="68" y1="28" x2="130" y2="18" stroke="#3a3a3a" stroke-width="5" stroke-linecap="round"/>
        <animateTransform attributeName="transform" type="rotate" values="0 68 28;-14 68 28;0 68 28" dur="5s" repeatCount="indefinite"/></g>
      <animateTransform attributeName="transform" type="translate" values="0 0;0 6;0 0" dur="5s" repeatCount="indefinite"/>
    </g>
  </g>
  <!-- casse de caractères -->
  <g transform="translate(250,170)">
    <rect width="150" height="66" fill="#8a6440" stroke="#4e3722" stroke-width="2"/>
    ${[0,1,2,3,4,5].map(c=>[0,1,2].map(r=>`<rect x="${6+c*24}" y="${6+r*20}" width="20" height="16" fill="#6b4a2b"/>`).join("")).join("")}
    <g fill="#9a9a9a">${[0,1,2,3,4,5,6,7].map(i=>`<rect x="${12+i*16}" y="${12+(i%3)*20}" width="3" height="6"/>`).join("")}</g>
  </g>
  <!-- Bible ouverte et chandelle -->
  <g transform="translate(640,200)">
    <rect x="-10" y="18" width="110" height="18" fill="#6b4a2b"/>
    <path d="M10 18 Q40 6 46 18 Q52 6 82 18 Z" fill="#f6efdc" stroke="#a58f68"/>
    ${flamme(96, 0)}
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — La rue des deux voisins (1598)
   ------------------------------------------------------------ */
"rue": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_JOUR}
    <linearGradient id="paveR" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#a99a80"/><stop offset="100%" stop-color="#7d705c"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielJour)"/>
  ${NUAGES}${OISEAUX}
  <!-- clocher au bout de la rue -->
  <g transform="translate(372,40)">
    <rect x="0" y="40" width="56" height="150" fill="#cdbf9f" stroke="#7a6d55" stroke-width="2"/>
    <path d="M-6 42 L28 -20 L62 42 Z" fill="#5d6773"/>
    <line x1="28" y1="-20" x2="28" y2="-40" stroke="#4a4a4a" stroke-width="3"/><line x1="20" y1="-32" x2="36" y2="-32" stroke="#4a4a4a" stroke-width="3"/>
    <path d="M18 80 L18 64 Q28 54 38 64 L38 80 Z" fill="#3b3226"/>
  </g>
  <!-- rue pavée en perspective -->
  <path d="M300 300 L384 196 L416 196 L500 300 Z" fill="url(#paveR)"/>
  <g stroke="#6a5e4c" stroke-width="1" opacity=".6">${[210,226,246,270,296].map(y=>`<line x1="${400-(y-196)*0.95}" y1="${y}" x2="${400+(y-196)*0.95}" y2="${y}"/>`).join("")}</g>
  <!-- maison de gauche : l'imprimerie -->
  <g transform="translate(40,70)">
    <rect width="270" height="170" fill="#efe3c6" stroke="#5e4128" stroke-width="3"/>
    <g stroke="#5e4128" stroke-width="7"><line x1="0" y1="80" x2="270" y2="80"/><line x1="90" y1="0" x2="90" y2="170"/><line x1="180" y1="0" x2="180" y2="170"/>
      <line x1="0" y1="0" x2="90" y2="80"/><line x1="180" y1="80" x2="270" y2="0"/></g>
    <path d="M-12 2 L135 -54 L282 2 Z" fill="#7d4f36"/>
    <rect x="110" y="104" width="44" height="66" fill="#4e3722"/>
    <rect x="20" y="100" width="54" height="40" fill="#bcd4e2" stroke="#5e4128" stroke-width="3"/>
    <g transform="translate(200,96)"><rect width="56" height="30" fill="#f6efdc" stroke="#5e4128" stroke-width="2"/>
      <text x="28" y="20" font-size="11" text-anchor="middle" font-family="Georgia,serif" fill="#2b1d10">Imprimeur</text></g>
  </g>
  <!-- maison de droite : la boulangerie -->
  <g transform="translate(490,70)">
    <rect width="270" height="170" fill="#ead9b4" stroke="#5e4128" stroke-width="3"/>
    <g stroke="#5e4128" stroke-width="7"><line x1="0" y1="80" x2="270" y2="80"/><line x1="90" y1="0" x2="90" y2="170"/><line x1="180" y1="0" x2="180" y2="170"/>
      <line x1="90" y1="0" x2="0" y2="80"/><line x1="270" y1="80" x2="180" y2="0"/></g>
    <path d="M-12 2 L135 -54 L282 2 Z" fill="#8a5a3c"/>
    <rect x="210" y="-46" width="20" height="40" fill="#7a6d55"/>
    <g fill="#ddd" opacity=".55"><circle cx="220" cy="-52" r="8"><animate attributeName="cy" values="-50;-110" dur="6s" repeatCount="indefinite"/><animate attributeName="opacity" values=".6;0" dur="6s" repeatCount="indefinite"/></circle>
      <circle cx="226" cy="-60" r="6"><animate attributeName="cy" values="-56;-120" dur="7s" repeatCount="indefinite"/><animate attributeName="opacity" values=".5;0" dur="7s" repeatCount="indefinite"/></circle></g>
    <rect x="116" y="104" width="44" height="66" fill="#4e3722"/>
    <rect x="196" y="100" width="54" height="40" fill="#bcd4e2" stroke="#5e4128" stroke-width="3"/>
    <g transform="translate(20,96)"><rect width="60" height="32" fill="#f6efdc" stroke="#5e4128" stroke-width="2"/>
      <ellipse cx="30" cy="16" rx="18" ry="8" fill="#c98a3c"/><g stroke="#8a5a20" stroke-width="1.5"><line x1="22" y1="12" x2="26" y2="20"/><line x1="30" y1="12" x2="34" y2="20"/></g></g>
  </g>
  <!-- affiche de l'édit sur le mur -->
  <g transform="translate(330,150)"><rect width="30" height="40" fill="#fbf6e8" stroke="#8a6d3b"/>
    <g stroke="#6d6253" stroke-width="1"><line x1="5" y1="10" x2="25" y2="10"/><line x1="5" y1="16" x2="25" y2="16"/><line x1="5" y1="22" x2="25" y2="22"/><line x1="5" y1="28" x2="20" y2="28"/></g>
    <circle cx="15" cy="34" r="3.5" fill="#9b1c1c"/></g>
  <!-- le crieur et son rouleau -->
  <g transform="translate(436,186)">
    <rect x="-8" y="10" width="16" height="34" rx="4" fill="#2f4a6b"/><circle cy="2" r="9" fill="#e9c49e"/>
    <path d="M-10 -4 Q0 -14 10 -4 Z" fill="#3b2a1a"/>
    <g><rect x="8" y="10" width="18" height="24" fill="#fbf6e8" stroke="#8a6d3b"/>
      <animateTransform attributeName="transform" type="rotate" values="0 8 18;-6 8 18;0 8 18" dur="3s" repeatCount="indefinite"/></g>
    <rect x="-7" y="44" width="5" height="16" fill="#3b2a1a"/><rect x="2" y="44" width="5" height="16" fill="#3b2a1a"/>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — Les jardins de Versailles (1682)
   ------------------------------------------------------------ */
"jardins": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_JOUR}
    <linearGradient id="herbeJ" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#9cc27a"/><stop offset="100%" stop-color="#5f8a3c"/></linearGradient>
    <linearGradient id="eauJ" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#9cc8e4"/><stop offset="100%" stop-color="#4f86ad"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielJour)"/>
  ${NUAGES}${OISEAUX}
  <!-- le château au fond -->
  <g transform="translate(120,92)">
    <rect width="560" height="56" fill="#e9dcc0" stroke="#8a7a5a" stroke-width="2"/>
    <rect x="230" y="-14" width="100" height="70" fill="#efe3c8" stroke="#8a7a5a" stroke-width="2"/>
    <rect y="-8" width="560" height="8" fill="#5d6773"/>
    <g fill="#9cb7cc" stroke="#7a6a4a" stroke-width="1">${Array.from({length:23},(_,i)=>`<rect x="${10+i*24}" y="${i>=10&&i<=13?2:12}" width="12" height="${i>=10&&i<=13?40:30}"/>`).join("")}</g>
    <g fill="#d4a72c">${Array.from({length:12},(_,i)=>`<rect x="${14+i*48}" y="-14" width="4" height="8"/>`).join("")}</g>
  </g>
  <!-- parterres de broderie -->
  <rect y="150" width="800" height="150" fill="url(#herbeJ)"/>
  <path d="M370 150 L430 150 L520 300 L280 300 Z" fill="#e8dfc6"/>
  <g fill="none" stroke="#3f6a26" stroke-width="3">
    <path d="M60 190 q30 -18 60 0 t60 0 t60 0 t60 0"/><path d="M520 190 q30 -18 60 0 t60 0 t60 0 t60 0"/>
    <path d="M40 240 q40 -24 80 0 t80 0 t80 0"/><path d="M560 240 q40 -24 80 0 t80 0 t80 0"/>
  </g>
  <!-- ifs taillés en cône -->
  ${[60,150,240,560,650,740].map((x,i)=>`<path d="M${x} ${i%3===2?215:178} l-10 30 l20 0 Z" fill="#2f5a22" transform="scale(1)"/>`).join("")}
  <!-- bassin et jets d'eau -->
  <ellipse cx="400" cy="250" rx="110" ry="26" fill="url(#eauJ)" stroke="#d9cfb8" stroke-width="5"/>
  <g stroke="#e9f4fb" stroke-width="3" fill="none" opacity=".9">
    <path d="M400 248 L400 190"><animate attributeName="d" values="M400 248 L400 190;M400 248 L400 176;M400 248 L400 190" dur="2.4s" repeatCount="indefinite"/></path>
    <path d="M350 250 Q340 220 330 248"><animate attributeName="opacity" values=".4;1;.4" dur="2s" repeatCount="indefinite"/></path>
    <path d="M450 250 Q460 220 470 248"><animate attributeName="opacity" values="1;.4;1" dur="2s" repeatCount="indefinite"/></path>
  </g>
  <!-- char du dieu au centre du bassin (doré) -->
  <g transform="translate(400,238)" fill="#c9a227" stroke="#7a5a12" stroke-width="1">
    <path d="M-26 6 L26 6 L20 -6 L-20 -6 Z"/><circle cx="-14" cy="8" r="6"/><circle cx="14" cy="8" r="6"/>
    <path d="M-30 -2 q-10 -12 -20 -4 l6 8 Z"/><path d="M30 -2 q10 -12 20 -4 l-6 8 Z"/>
    <circle cy="-16" r="6"/><g stroke="#e3be3e" stroke-width="2">${[0,45,90,135,180,225,270,315].map(a=>`<line x1="0" y1="-16" x2="${Math.round(12*Math.cos(a*Math.PI/180))}" y2="${Math.round(-16+12*Math.sin(a*Math.PI/180))}"/>`).join("")}</g>
  </g>
  <!-- reflets -->
  <g stroke="#fff" stroke-width="1.4" opacity=".6"><line x1="330" y1="258" x2="356" y2="258"><animate attributeName="x1" values="330;340;330" dur="4s" repeatCount="indefinite"/></line><line x1="440" y1="262" x2="470" y2="262"/></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — La chambre du roi
   ------------------------------------------------------------ */
"chambre": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murC" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e9dcc0"/><stop offset="100%" stop-color="#cdbb94"/></linearGradient>
    <linearGradient id="parquetC" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#9a6b3e"/><stop offset="100%" stop-color="#6b4626"/></linearGradient>
    <linearGradient id="tentureC" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#7d1d23"/><stop offset="50%" stop-color="#a0303a"/><stop offset="100%" stop-color="#7d1d23"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murC)"/>
  <rect y="244" width="800" height="56" fill="url(#parquetC)"/>
  <g stroke="#5a3a1e" stroke-width="1" opacity=".5">${[0,1,2,3,4,5,6,7,8,9].map(i=>`<line x1="${i*90}" y1="244" x2="${i*90-40}" y2="300"/>`).join("")}</g>
  <!-- pilastres dorés -->
  <g fill="#d4a72c" stroke="#8a6a1a">${[40,200,600,760].map(x=>`<rect x="${x-8}" y="20" width="16" height="224"/>`).join("")}</g>
  <!-- emblème du Soleil au-dessus du lit -->
  <g transform="translate(400,58)">
    <g><g stroke="#d4a72c" stroke-width="4">${Array.from({length:16},(_,i)=>{const a=i*22.5*Math.PI/180;return `<line x1="${Math.round(26*Math.cos(a))}" y1="${Math.round(26*Math.sin(a))}" x2="${Math.round(42*Math.cos(a))}" y2="${Math.round(42*Math.sin(a))}"/>`;}).join("")}</g>
      <animateTransform attributeName="transform" type="rotate" values="0;360" dur="60s" repeatCount="indefinite"/></g>
    <circle r="24" fill="#e3be3e" stroke="#8a6a1a" stroke-width="2"/>
    <g fill="#8a6a1a"><circle cx="-8" cy="-4" r="2.5"/><circle cx="8" cy="-4" r="2.5"/></g><path d="M-8 8 Q0 14 8 8" stroke="#8a6a1a" stroke-width="2" fill="none"/>
  </g>
  <!-- le lit et son ciel -->
  <g transform="translate(300,104)">
    <rect x="0" y="-6" width="200" height="16" fill="#a0303a" stroke="#d4a72c" stroke-width="2"/>
    <path d="M0 10 Q12 70 0 140 L22 140 Q30 70 22 10 Z" fill="url(#tentureC)"/>
    <path d="M200 10 Q188 70 200 140 L178 140 Q170 70 178 10 Z" fill="url(#tentureC)"/>
    <rect x="22" y="82" width="156" height="58" fill="#f2ead6" stroke="#c9b98f"/>
    <rect x="22" y="100" width="156" height="40" fill="#a0303a"/>
    <g stroke="#d4a72c" stroke-width="2" fill="none"><path d="M30 112 q20 -10 40 0 t40 0 t40 0 t20 0"/></g>
  </g>
  <!-- balustrade dorée -->
  <g transform="translate(250,214)">
    <rect width="300" height="8" fill="#d4a72c" stroke="#8a6a1a"/><rect y="34" width="300" height="6" fill="#d4a72c" stroke="#8a6a1a"/>
    <g fill="#e3be3e" stroke="#8a6a1a">${Array.from({length:15},(_,i)=>`<path d="M${10+i*20} 8 q6 8 0 13 q-6 5 0 13 l4 0 q6 -8 0 -13 q-6 -5 0 -13 Z"/>`).join("")}</g>
  </g>
  <!-- grandes fenêtres et lumière -->
  ${[100,700].map(x=>`<g transform="translate(${x-36},40)"><rect width="72" height="170" fill="#cfe2ef" stroke="#d4a72c" stroke-width="5"/>
    <g stroke="#d4a72c" stroke-width="2"><line x1="36" y1="0" x2="36" y2="170"/>${[42,84,126].map(y=>`<line x1="0" y1="${y}" x2="72" y2="${y}"/>`).join("")}</g></g>`).join("")}
  <!-- chandeliers -->
  ${flamme(250,170)}${flamme(550,170)}
  <!-- courtisans qui attendent (silhouettes) -->
  <g opacity=".75">
    <g transform="translate(150,196)"><rect x="-10" y="0" width="20" height="44" rx="6" fill="#3d5266"/><circle cy="-8" r="9" fill="#e9c49e"/><path d="M-11 -10 Q-12 6 -6 10 L-4 -6 Z M11 -10 Q12 6 6 10 L4 -6 Z" fill="#6b4a2b"/></g>
    <g transform="translate(650,196)"><path d="M-16 44 L-8 0 L8 0 L16 44 Z" fill="#6b3a6a"/><circle cy="-8" r="9" fill="#f6dcc0"/><path d="M-9 -14 Q0 -24 9 -14 Z" fill="#3b2a1a"/></g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — Le cabinet du Conseil
   ------------------------------------------------------------ */
"conseil": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murK" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e3e6dc"/><stop offset="100%" stop-color="#c3c8b8"/></linearGradient>
    <linearGradient id="tapisK" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3f7a4a"/><stop offset="100%" stop-color="#26502f"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murK)"/>
  <rect y="246" width="800" height="54" fill="#7a5532"/>
  <!-- boiseries dorées -->
  <g fill="none" stroke="#c9a227" stroke-width="3">${[30,230,430,630].map(x=>`<rect x="${x}" y="30" width="140" height="150" rx="6"/>`).join("")}</g>
  <!-- carte du royaume (feuille avec rose des vents) -->
  <g transform="translate(250,40)">
    <rect width="300" height="130" fill="#f4ead2" stroke="#8a6d3b" stroke-width="3"/>
    <path d="M40 90 q30 -50 80 -30 t90 -10 t50 40 q-20 30 -60 24 t-90 4 t-70 -28 Z" fill="#e3d6b0" stroke="#8a7a5a" stroke-width="1.5"/>
    <path d="M60 70 q40 10 70 30 t80 0" stroke="#5f8fb0" stroke-width="2" fill="none"/>
    <g transform="translate(262,30)"><circle r="14" fill="none" stroke="#6b4a2b"/><path d="M0 -14 L4 0 L0 14 L-4 0 Z M-14 0 L0 4 L14 0 L0 -4 Z" fill="#6b4a2b"/></g>
    <g fill="#9b1c1c">${[[110,70],[170,58],[210,96]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="3"/>`).join("")}</g>
  </g>
  <!-- la table au tapis vert -->
  <g transform="translate(130,188)">
    <path d="M0 0 L540 0 L560 40 L-20 40 Z" fill="url(#tapisK)"/>
    <rect x="-20" y="40" width="580" height="10" fill="#1d3a22"/>
    <g fill="#5e4128"><rect x="0" y="50" width="12" height="10"/><rect x="530" y="50" width="12" height="10"/></g>
    <!-- papiers, encrier, plume -->
    <g fill="#fbf6e8" stroke="#bfb193">${[60,180,330,450].map(x=>`<rect x="${x}" y="8" width="44" height="24" transform="rotate(-4 ${x} 8)"/>`).join("")}</g>
    <g transform="translate(260,14)"><rect x="-10" y="0" width="20" height="14" fill="#2b2b2b"/>
      <path d="M0 0 Q14 -30 34 -46 Q16 -20 4 2 Z" fill="#f3f0e6" stroke="#8a8170">
        <animateTransform attributeName="transform" type="rotate" values="0 0 0;8 0 0;0 0 0;-4 0 0;0 0 0" dur="3.2s" repeatCount="indefinite"/></path></g>
    <g transform="translate(400,8)"><circle r="9" fill="#9b1c1c"/><rect x="-2" y="-22" width="4" height="14" fill="#5e3a1a"/></g>
  </g>
  <!-- fauteuils -->
  <g fill="#a0303a" stroke="#d4a72c" stroke-width="2">${[150,290,430,570].map(x=>`<path d="M${x} 186 L${x} 150 Q${x+20} 138 ${x+40} 150 L${x+40} 186 Z"/>`).join("")}</g>
  <!-- chandelles -->
  ${flamme(90,180)}${flamme(710,180)}
</svg>`
};

window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
