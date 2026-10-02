/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de « L'Atelier de Léonard à Amboise »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux (Amboise, printemps 1518) :
     imprimerie  l'imprimerie de Maître Jacquet
     salle       la grande salle du château, tapisseries et salamandres
     atelier     l'atelier de Léonard au manoir du Cloux
     plans       le cabinet des plans des châteaux
     galerie     la galerie des tableaux, en perspective
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

const SALLE_NUM = { "imprimerie":1, "salle":2, "atelier":3, "plans":4, "galerie":5 };

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

const SALAMANDRE = (x, y, s=1, c="#c9a227") => `<g transform="translate(${x},${y}) scale(${s})"><path d="M-30 4 Q-18 -10 0 -4 Q16 2 26 -8 Q30 -2 22 4 Q8 12 -6 8 Q-20 6 -30 12 Z" fill="${c}"/>
  <g stroke="${c}" stroke-width="2.4"><line x1="-14" y1="2" x2="-18" y2="10"/><line x1="-2" y1="4" x2="2" y2="12"/></g>
  <g fill="#e08a1e" opacity=".8"><path d="M-26 16 q3 -10 6 0 q3 -9 6 0 q3 -10 6 0 q3 -9 6 0 q3 -10 6 0 q3 -9 6 0 Z"><animate attributeName="opacity" values=".55;.95;.6;.9;.55" dur="1.6s" repeatCount="indefinite"/></path></g></g>`;
const F_COURONNE = (x, y, c="#c9a227") => `<g transform="translate(${x},${y})"><path d="M-12 -14 l4 6 l4 -8 l4 8 l4 -8 l4 8 l4 -6 l0 8 l-24 0 Z" fill="${c}"/>
  <text y="16" text-anchor="middle" font-family="Georgia,serif" font-size="24" font-weight="bold" fill="${c}">F</text></g>`;

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — L'imprimerie de Maître Jacquet (Amboise, 1518)
   ------------------------------------------------------------ */
"imprimerie": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murI" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#ddcaa5"/><stop offset="100%" stop-color="#b79e74"/></linearGradient>
    <linearGradient id="solI" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#7a5a3a"/><stop offset="100%" stop-color="#4e3722"/></linearGradient>
    <linearGradient id="rayonI" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fff6d6" stop-opacity=".55"/><stop offset="100%" stop-color="#fff6d6" stop-opacity="0"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murI)"/>
  <rect y="236" width="800" height="64" fill="url(#solI)"/>
  <g fill="#5e4128"><rect y="0" width="800" height="16"/><rect x="60" y="16" width="14" height="220"/><rect x="420" y="16" width="14" height="220"/><rect x="740" y="16" width="14" height="220"/></g>
  <!-- gravure d'un temple antique au mur -->
  <g transform="translate(110,40)">
    <rect width="140" height="100" fill="#f6efdc" stroke="#6b4a2b" stroke-width="4"/>
    <path d="M14 40 L70 14 L126 40 Z" fill="none" stroke="#4a3825" stroke-width="2"/>
    <g stroke="#4a3825" stroke-width="2.5">${[26,46,66,86,106].map(x=>`<line x1="${x+4}" y1="44" x2="${x+4}" y2="84"/>`).join("")}</g>
    <line x1="14" y1="88" x2="126" y2="88" stroke="#4a3825" stroke-width="3"/>
  </g>
  <path d="M250 60 L320 60 L470 236 L330 236 Z" fill="url(#rayonI)"><animate attributeName="opacity" values=".7;1;.7" dur="7s" repeatCount="indefinite"/></path>
  <!-- feuilles qui sèchent -->
  <line x1="460" y1="42" x2="730" y2="52" stroke="#6b5a44" stroke-width="1.5"/>
  ${[0,1,2,3,4].map(i=>`<g transform="translate(${478+i*50},${44+i*2})"><rect x="-16" y="0" width="32" height="40" fill="#fbf6e8" stroke="#bfb193">
    <animateTransform attributeName="transform" type="rotate" values="-3 0 0;3 0 0;-3 0 0" dur="${4+i*.6}s" repeatCount="indefinite"/></rect>
    <g stroke="#6d6253" stroke-width="1"><line x1="-10" y1="8" x2="10" y2="8"/><line x1="-10" y1="14" x2="10" y2="14"/><line x1="-10" y1="20" x2="6" y2="20"/></g></g>`).join("")}
  <!-- la presse -->
  <g transform="translate(470,110)">
    <rect x="0" y="0" width="16" height="130" fill="#6b4a2b"/><rect x="120" y="0" width="16" height="130" fill="#6b4a2b"/>
    <rect x="-6" y="-8" width="148" height="18" fill="#7a5532"/><rect x="0" y="70" width="136" height="12" fill="#7a5532"/>
    <rect x="-20" y="96" width="176" height="14" fill="#8a6440"/>
    <g><rect x="62" y="10" width="12" height="40" fill="#4a4a4a"/><rect x="44" y="48" width="48" height="14" fill="#5e5e5e"/>
      <g><line x1="68" y1="28" x2="130" y2="18" stroke="#3a3a3a" stroke-width="5" stroke-linecap="round"/>
        <animateTransform attributeName="transform" type="rotate" values="0 68 28;-14 68 28;0 68 28" dur="5s" repeatCount="indefinite"/></g>
      <animateTransform attributeName="transform" type="translate" values="0 0;0 6;0 0" dur="5s" repeatCount="indefinite"/></g>
  </g>
  <!-- pile de livres -->
  <g transform="translate(250,186)">
    ${[0,1,2,3,4].map(i=>`<rect x="${(i%2)*6}" y="${50-i*12}" width="110" height="11" fill="${["#7a2a3a","#2f4f8a","#6b4a2b","#3f7a3a","#8a6d3b"][i]}" stroke="#2b1d10" stroke-width=".8"/>`).join("")}
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — La grande salle du château d'Amboise
   ------------------------------------------------------------ */
"salle": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murS" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e6d6b4"/><stop offset="100%" stop-color="#c8b28a"/></linearGradient>
    <linearGradient id="tapS" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2f4f8a"/><stop offset="100%" stop-color="#1d3260"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murS)"/>
  <rect y="240" width="800" height="60" fill="#7a5532"/>
  <g stroke="#5e3f1f" opacity=".5">${[0,1,2,3,4,5,6,7,8].map(i=>`<line x1="${i*100}" y1="240" x2="${i*100-30}" y2="300"/>`).join("")}</g>
  <!-- plafond à poutres -->
  <rect width="800" height="22" fill="#5e4128"/><g fill="#6b4a2b">${[0,1,2,3,4,5,6,7].map(i=>`<rect x="${i*110}" y="22" width="18" height="10"/>`).join("")}</g>
  <!-- tapisseries semées de lettres F et de salamandres -->
  ${[60,560].map(x=>`<g transform="translate(${x},44)"><rect width="180" height="150" fill="url(#tapS)" stroke="#c9a227" stroke-width="4"/>
    ${F_COURONNE(45,50)}${F_COURONNE(135,50)}${SALAMANDRE(90,110,1)}</g>`).join("")}
  <!-- fenêtre sur la Loire -->
  <g transform="translate(330,40)">
    <rect width="140" height="160" fill="#a9cbe3" stroke="#6b4a2b" stroke-width="8"/>
    <path d="M0 110 Q40 100 70 112 T140 104 L140 160 L0 160 Z" fill="#6fa0c4"/>
    <path d="M0 96 Q30 86 70 92 T140 88 L140 108 Q100 100 70 108 T0 112 Z" fill="#7aa35a"/>
    <g stroke="#e9f4fb" opacity=".8"><line x1="20" y1="132" x2="44" y2="132"><animate attributeName="x1" values="20;30;20" dur="5s" repeatCount="indefinite"/></line><line x1="90" y1="140" x2="120" y2="140"/></g>
    <g stroke="#6b4a2b" stroke-width="3"><line x1="70" y1="0" x2="70" y2="160"/><line x1="0" y1="80" x2="140" y2="80"/></g>
  </g>
  <!-- table de fête -->
  <g transform="translate(220,200)">
    <rect width="360" height="16" fill="#f4ead2" stroke="#b8a27a"/><rect x="10" y="16" width="10" height="24" fill="#6b4a2b"/><rect x="340" y="16" width="10" height="24" fill="#6b4a2b"/>
    <g fill="#c9a227">${[40,100,160,220,280,320].map(x=>`<ellipse cx="${x}" cy="0" rx="12" ry="4"/>`).join("")}</g>
    <g fill="#8a2626">${[70,190,300].map(x=>`<circle cx="${x}" cy="-6" r="6"/>`).join("")}</g>
  </g>
  <!-- un luth posé -->
  <g transform="translate(640,220) rotate(-20)"><ellipse rx="18" ry="13" fill="#a0703c" stroke="#5e3f1f"/><rect x="14" y="-3" width="34" height="6" fill="#6b4a2b"/><circle r="4" fill="#3b2a1a"/></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — L'atelier de Léonard au manoir du Cloux
   ------------------------------------------------------------ */
"atelier": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murA" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e9dcc0"/><stop offset="100%" stop-color="#cdb98f"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murA)"/>
  <rect y="242" width="800" height="58" fill="#8a6440"/>
  <!-- fenêtre et oiseaux -->
  <g transform="translate(60,40)">
    <rect width="130" height="130" fill="#bcd8ea" stroke="#6b4a2b" stroke-width="7"/>
    <g stroke="#333" stroke-width="1.6" fill="none"><path d="M0 0 q6 -6 12 0 q6 -6 12 0"><animateMotion dur="9s" repeatCount="indefinite" path="M10 60 L110 30"/></path>
      <path d="M0 0 q5 -5 10 0 q5 -5 10 0"><animateMotion dur="12s" repeatCount="indefinite" path="M0 90 L120 50"/></path></g>
    <g stroke="#6b4a2b" stroke-width="3"><line x1="65" y1="0" x2="65" y2="130"/><line x1="0" y1="65" x2="130" y2="65"/></g>
  </g>
  <!-- dessins épinglés : machine à ailes, engrenage, aile d'oiseau, tourbillon -->
  <g transform="translate(230,34)">
    ${[[0,0],[120,10],[240,0],[360,8]].map(([x,y],i)=>`<g transform="translate(${x},${y}) rotate(${[-3,2,-2,3][i]})"><rect width="100" height="74" fill="#f3e6c8" stroke="#a58f68"/><circle cx="50" cy="4" r="3" fill="#8a2626"/></g>`).join("")}
    <g stroke="#5a4630" stroke-width="1.4" fill="none">
      <path d="M14 46 Q50 10 86 46 M50 28 L50 58 M30 40 Q50 50 70 40"/>
      <g transform="translate(170,47)"><g><circle r="18"/><circle r="6"/>${[0,30,60,90,120,150,180,210,240,270,300,330].map(a=>`<line x1="0" y1="-18" x2="0" y2="-24" transform="rotate(${a})"/>`).join("")}
        <animateTransform attributeName="transform" type="rotate" values="0;360" dur="20s" repeatCount="indefinite"/></g></g>
      <path d="M256 50 Q280 20 330 30 M262 50 Q285 30 326 38 M268 50 Q290 38 322 46"/>
      <path d="M410 44 q10 -16 20 0 q-10 14 -20 0 q6 -8 10 0"/>
    </g>
  </g>
  <!-- chevalet et portrait (silhouette) -->
  <g transform="translate(560,110)">
    <g stroke="#6b4a2b" stroke-width="6"><line x1="20" y1="132" x2="60" y2="0"/><line x1="120" y1="132" x2="80" y2="0"/><line x1="70" y1="10" x2="70" y2="140"/></g>
    <rect x="16" y="20" width="108" height="92" fill="#5e6b4a" stroke="#b8860b" stroke-width="4"/>
    <ellipse cx="70" cy="52" rx="14" ry="17" fill="#d8b48c"/><path d="M48 112 Q50 74 70 70 Q90 74 92 112 Z" fill="#3b2a1a"/>
    <path d="M56 46 Q70 30 84 46 Q86 70 92 80 L48 80 Q54 70 56 46 Z" fill="#3b2a1a" opacity=".85"/>
  </g>
  <!-- table : carnet ouvert, plume, bougie -->
  <g transform="translate(250,196)">
    <rect width="260" height="14" fill="#6b4a2b"/><rect x="10" y="14" width="10" height="32" fill="#5e3f1f"/><rect x="240" y="14" width="10" height="32" fill="#5e3f1f"/>
    <path d="M60 0 Q90 -12 120 0 Q150 -12 180 0 Z" fill="#f6efdc" stroke="#a58f68"/>
    <g stroke="#6d6253" stroke-width=".8"><line x1="70" y1="-4" x2="110" y2="-6"/><line x1="130" y1="-6" x2="170" y2="-4"/></g>
    <g transform="translate(200,-2)"><path d="M0 0 Q12 -24 30 -36 Q14 -16 4 2 Z" fill="#f3f0e6" stroke="#8a8170">
      <animateTransform attributeName="transform" type="rotate" values="0 0 0;6 0 0;0 0 0" dur="3s" repeatCount="indefinite"/></path></g>
    <g transform="translate(30,-20)"><rect x="-3" y="0" width="6" height="20" fill="#f3ecd8"/><path d="M0 -12 Q5 -4 0 0 Q-5 -4 0 -12 Z" fill="#ffb23c"><animateTransform attributeName="transform" type="scale" values="1 1;1 1.2;1 1" dur="1.4s" repeatCount="indefinite"/></path></g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — Le cabinet des plans
   ------------------------------------------------------------ */
"plans": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murP" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#dfe3d6"/><stop offset="100%" stop-color="#c2c7b4"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murP)"/>
  <rect y="246" width="800" height="54" fill="#7a5532"/>
  <!-- grande fenêtre à meneaux : silhouette d'un château symétrique -->
  <g transform="translate(520,30)">
    <rect width="220" height="150" fill="#bcd8ea" stroke="#6b4a2b" stroke-width="7"/>
    <g fill="#e9dcc0" stroke="#8a7a5a"><rect x="40" y="90" width="140" height="44"/><rect x="90" y="66" width="40" height="68"/><circle cx="40" cy="104" r="14"/><circle cx="180" cy="104" r="14"/></g>
    <g fill="#5d6773"><path d="M86 66 L110 40 L134 66 Z"/><path d="M26 92 L40 72 L54 92 Z"/><path d="M166 92 L180 72 L194 92 Z"/></g>
    <rect x="104" y="30" width="12" height="16" fill="#efe3c8" stroke="#8a7a5a"/>
    <g stroke="#6b4a2b" stroke-width="3"><line x1="110" y1="0" x2="110" y2="150" stroke-dasharray="1 0"/><line x1="0" y1="75" x2="220" y2="75"/></g>
    <line x1="110" y1="10" x2="110" y2="140" stroke="#b8860b" stroke-dasharray="4 4"><animate attributeName="opacity" values=".3;1;.3" dur="3s" repeatCount="indefinite"/></line>
  </g>
  <!-- table à dessin et plans -->
  <g transform="translate(60,150)">
    <path d="M0 40 L400 40 L420 96 L-20 96 Z" fill="#8a6440"/>
    <g transform="translate(30,14)"><rect width="150" height="76" fill="#f4ead2" stroke="#a58f68" transform="skewX(-12)"/>
      <g stroke="#4a3825" stroke-width="1.2" fill="none" transform="skewX(-12)"><rect x="40" y="14" width="50" height="50"/><line x1="65" y1="14" x2="65" y2="64"/><line x1="40" y1="39" x2="90" y2="39"/><circle cx="65" cy="39" r="6"/>
        <circle cx="40" cy="14" r="6"/><circle cx="90" cy="14" r="6"/><circle cx="40" cy="64" r="6"/><circle cx="90" cy="64" r="6"/></g></g>
    <g transform="translate(220,20)"><rect width="140" height="70" fill="#f6efdc" stroke="#a58f68" transform="skewX(-12)"/>
      <g stroke="#4a3825" fill="none" transform="skewX(-12)"><path d="M20 50 L120 50 M30 50 L30 24 L50 24 L50 50 M90 50 L90 24 L110 24 L110 50 M50 30 L90 30"/></g></g>
    <!-- compas qui pivote -->
    <g transform="translate(200,10)"><g stroke="#555" stroke-width="3"><line x1="0" y1="0" x2="-12" y2="40"/><line x1="0" y1="0" x2="12" y2="40">
      <animateTransform attributeName="transform" type="rotate" values="0 0 0;-14 0 0;0 0 0" dur="4s" repeatCount="indefinite"/></line></g><circle r="4" fill="#777"/></g>
    <rect x="0" y="30" width="180" height="6" fill="#c9a227" transform="rotate(-4)"/>
  </g>
  <g transform="translate(400,70)"><circle r="46" fill="#efe6cf" stroke="#c9a227" stroke-width="5"/>${F_COURONNE(0,-22,"#8a6d3b")}</g>
  ${SALAMANDRE(400,92,0.9,"#8a6d3b")}
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — La galerie des tableaux (en perspective)
   ------------------------------------------------------------ */
"galerie": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murG" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#ead8b2"/><stop offset="100%" stop-color="#cbb48a"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murG)"/>
  <!-- murs et sol en perspective vers un point de fuite central -->
  <path d="M0 0 L340 110 L340 190 L0 300 Z" fill="#dcc79e"/>
  <path d="M800 0 L460 110 L460 190 L800 300 Z" fill="#dcc79e"/>
  <path d="M0 300 L340 190 L460 190 L800 300 Z" fill="#9a6b3e"/>
  <rect x="340" y="110" width="120" height="80" fill="#e9dcc0" stroke="#8a7a5a"/>
  <clipPath id="solGal"><path d="M0 300 L340 190 L460 190 L800 300 Z"/></clipPath>
  <g stroke="#6b4626" stroke-width="1" opacity=".7" clip-path="url(#solGal)">${[-200,-60,80,220,360,500,640,780,920].map(x=>`<line x1="${x}" y1="300" x2="400" y2="150"/>`).join("")}</g>
  <!-- tableaux sur les murs, de plus en plus petits -->
  ${[[40,60,90,110],[150,92,60,74],[228,110,40,50],[290,122,26,32]].map(([x,y,w,h],i)=>`<g><rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${["#5e6b4a","#7a5a3a","#4a5e7a","#6b4a4a"][i]}" stroke="#c9a227" stroke-width="${4-i*.8}"/>
    <circle cx="${x+w/2}" cy="${y+h*.42}" r="${w*.16}" fill="#d8b48c"/></g>`).join("")}
  ${[[670,60,90,110],[590,92,60,74],[532,110,40,50],[484,122,26,32]].map(([x,y,w,h],i)=>`<g><rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${["#4a6a7a","#6b5a3a","#5a4a6a","#4a6b5a"][i]}" stroke="#c9a227" stroke-width="${4-i*.8}"/>
    <path d="M${x+4} ${y+h-6} L${x+w/2} ${y+h*.35} L${x+w-4} ${y+h-6} Z" fill="#9cc27a" opacity=".8"/></g>`).join("")}
  <!-- point de fuite qui scintille -->
  <circle cx="400" cy="150" r="3" fill="#8a2626"><animate attributeName="r" values="2;5;2" dur="2.5s" repeatCount="indefinite"/></circle>
  <!-- deux visiteurs : proche (grand) et lointain (petit) -->
  <g transform="translate(200,206)" fill="#3d5266"><rect x="-12" y="0" width="24" height="56" rx="8"/><circle cy="-10" r="11" fill="#e9c49e"/></g>
  <g transform="translate(420,176)" fill="#7a2a3a"><rect x="-4" y="0" width="8" height="18" rx="3"/><circle cy="-4" r="4" fill="#e9c49e"/></g>
</svg>`
};


window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
