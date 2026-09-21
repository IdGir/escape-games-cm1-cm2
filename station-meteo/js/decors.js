/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de la station météo de l'école
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (zéro attente, zéro fichier).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux :
     abri    la cour de l'école et l'abri météo blanc à persiennes
     mat     le mât de l'anémomètre et de la girouette
     pluvio  le jardin et le pluviomètre, sous une averse
     bureau  le bureau des relevés (tableau, graphiques)
     studio  la salle de prévision et son écran
   Toutes les animations sont figées par le réglage « animations
   réduites » (classe body.calme, voir css/animations.css).
   ============================================================ */

function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["abri"];
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

function activerScene(sceneEl){
  if(!sceneEl) return;
  if(typeof nettoyerVideos === "function") nettoyerVideos();
  const base = sceneEl.dataset.media;
  if(base && typeof installerDecor === "function") installerDecor(sceneEl, base);
}

const SALLE_NUM = { "abri":1, "mat":2, "pluvio":3, "bureau":4, "studio":5 };

/* ---- Fragments communs ---- */
const CIEL_MATIN = `
  <linearGradient id="cielMatin" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#8fb8dc"/><stop offset="65%" stop-color="#cfe0ee"/><stop offset="100%" stop-color="#eef3f7"/>
  </linearGradient>`;
const CIEL_GRIS = `
  <linearGradient id="cielGris" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#6f7f8f"/><stop offset="100%" stop-color="#b8c4cf"/>
  </linearGradient>`;
function nuage(cx, cy, s, dur, sens){
  return `<g opacity=".85" transform="translate(${cx},${cy}) scale(${s})">
    <ellipse cx="0" cy="0" rx="46" ry="16" fill="#fff"/><ellipse cx="-22" cy="-8" rx="22" ry="14" fill="#fff"/>
    <ellipse cx="16" cy="-12" rx="26" ry="17" fill="#fff"/>
    <animateTransform attributeName="transform" type="translate" additive="sum" values="0 0;${sens*260} 0;0 0" dur="${dur}s" repeatCount="indefinite"/>
  </g>`;
}

const SVG_DECORS = {

/* ------------------------------------------------------------
   MODULE 1 — La cour de l'école et l'abri météo
   ------------------------------------------------------------ */
"abri": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_MATIN}
    <linearGradient id="solCour" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#b5b0a4"/><stop offset="100%" stop-color="#8f897c"/></linearGradient>
    <radialGradient id="soleilM" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#fff4c2"/><stop offset="100%" stop-color="#ffd76a" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielMatin)"/>
  <circle cx="690" cy="60" r="70" fill="url(#soleilM)"/><circle cx="690" cy="60" r="22" fill="#ffe28a"/>
  ${nuage(160,50,1,80,1)}${nuage(470,36,.8,110,-1)}
  <!-- bâtiment de l'école -->
  <rect x="20" y="92" width="360" height="150" fill="#e9dcc3"/>
  <polygon points="10,96 200,54 390,96" fill="#a5553a"/>
  <g fill="#6f93b3" stroke="#f7f1e3" stroke-width="3">
    <rect x="44" y="118" width="46" height="40"/><rect x="118" y="118" width="46" height="40"/>
    <rect x="236" y="118" width="46" height="40"/><rect x="310" y="118" width="46" height="40"/>
    <rect x="44" y="180" width="46" height="40"/><rect x="310" y="180" width="46" height="40"/>
  </g>
  <rect x="176" y="170" width="48" height="72" fill="#5b3f2a"/>
  <text x="200" y="112" font-size="12" text-anchor="middle" fill="#5b3f2a" font-family="Georgia,serif">ÉCOLE</text>
  <!-- arbre -->
  <g transform="translate(470,160)">
    <rect x="-7" y="10" width="14" height="72" fill="#6a4a2c"/>
    <g><ellipse cx="0" cy="-8" rx="52" ry="44" fill="#6f9a52"/><ellipse cx="-26" cy="8" rx="30" ry="24" fill="#5f8a45"/><ellipse cx="28" cy="6" rx="32" ry="26" fill="#6a9450"/>
      <animateTransform attributeName="transform" type="rotate" values="-1.5 0 60;1.5 0 60;-1.5 0 60" dur="6s" repeatCount="indefinite"/></g>
  </g>
  <!-- sol de la cour + marelle -->
  <rect x="0" y="242" width="800" height="58" fill="url(#solCour)"/>
  <g fill="none" stroke="#f3f0e8" stroke-width="2" opacity=".75">
    <rect x="80" y="258" width="28" height="22"/><rect x="108" y="258" width="28" height="22"/><rect x="136" y="258" width="28" height="22"/>
  </g>
  <!-- pelouse autour de l'abri -->
  <ellipse cx="640" cy="252" rx="130" ry="18" fill="#7ea35f"/>
  <!-- abri météo : boîte blanche à persiennes sur pied -->
  <g transform="translate(600,138)">
    <rect x="36" y="58" width="8" height="56" fill="#dcdcdc" stroke="#9aa3ad"/>
    <rect x="18" y="108" width="44" height="6" fill="#9aa3ad"/>
    <polygon points="-4,4 40,-12 84,4" fill="#f5f5f2" stroke="#9aa3ad" stroke-width="1.5"/>
    <rect x="0" y="4" width="80" height="56" fill="#fbfbf8" stroke="#9aa3ad" stroke-width="1.5"/>
    <g stroke="#b9c0c7" stroke-width="2">
      <line x1="6" y1="12" x2="36" y2="16"/><line x1="6" y1="22" x2="36" y2="26"/><line x1="6" y1="32" x2="36" y2="36"/><line x1="6" y1="42" x2="36" y2="46"/><line x1="6" y1="52" x2="36" y2="56"/>
      <line x1="44" y1="12" x2="74" y2="16"/><line x1="44" y1="22" x2="74" y2="26"/><line x1="44" y1="32" x2="74" y2="36"/><line x1="44" y1="42" x2="74" y2="46"/><line x1="44" y1="52" x2="74" y2="56"/>
    </g>
    <line x1="40" y1="4" x2="40" y2="60" stroke="#9aa3ad" stroke-width="1.5"/>
    <!-- repère de hauteur : 1,50 m -->
    <g stroke="#1d3a8a" stroke-width="1.4" fill="#1d3a8a">
      <line x1="100" y1="32" x2="100" y2="114"/><line x1="94" y1="32" x2="106" y2="32"/><line x1="94" y1="114" x2="106" y2="114"/>
    </g>
    <text x="108" y="78" font-size="12" fill="#1d3a8a" font-family="Arial,sans-serif">1,50 m</text>
  </g>
  <!-- feuille emportée par l'orage de la nuit -->
  <g transform="translate(300,220)">
    <path d="M0 0 q8 -8 16 0 q-8 8 -16 0z" fill="#8a6d2a"/>
    <animateTransform attributeName="transform" type="translate" values="300 220;420 234;540 226;300 220" dur="14s" repeatCount="indefinite"/>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MODULE 2 — Le mât de l'anémomètre et de la girouette
   ------------------------------------------------------------ */
"mat": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_MATIN}
    <linearGradient id="herbeM" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#86ad64"/><stop offset="100%" stop-color="#5d8341"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielMatin)"/>
  ${nuage(120,70,1.1,40,1)}${nuage(420,40,.9,55,1)}${nuage(640,90,.7,48,1)}
  <!-- lignes de vent (de l'ouest vers l'est) -->
  <g stroke="#ffffff" stroke-width="2" stroke-linecap="round" fill="none" opacity=".7">
    <path d="M40 130 q30 -8 60 0 t60 0"><animateTransform attributeName="transform" type="translate" values="-60 0;700 0" dur="7s" repeatCount="indefinite"/></path>
    <path d="M0 180 q30 -8 60 0 t60 0"><animateTransform attributeName="transform" type="translate" values="-120 0;720 0" dur="9s" repeatCount="indefinite"/></path>
    <path d="M60 220 q30 -8 60 0"><animateTransform attributeName="transform" type="translate" values="-80 0;700 0" dur="6s" repeatCount="indefinite"/></path>
  </g>
  <!-- terrain dégagé -->
  <path d="M0 250 Q200 232 400 246 T800 240 L800 300 L0 300 Z" fill="url(#herbeM)"/>
  <!-- mât : 10 m au-dessus du sol (repère) -->
  <rect x="396" y="66" width="8" height="186" fill="#9aa3ad"/>
  <g stroke="#9aa3ad" stroke-width="1.5"><line x1="400" y1="120" x2="330" y2="252"/><line x1="400" y1="120" x2="470" y2="252"/></g>
  <g stroke="#1d3a8a" stroke-width="1.4" fill="#1d3a8a">
    <line x1="440" y1="66" x2="440" y2="250"/><line x1="434" y1="66" x2="446" y2="66"/><line x1="434" y1="250" x2="446" y2="250"/>
  </g>
  <text x="450" y="162" font-size="12" fill="#1d3a8a" font-family="Arial,sans-serif">10 m</text>
  <!-- anémomètre à coupelles (tourne) -->
  <g transform="translate(400,62)">
    <rect x="-3" y="-4" width="6" height="10" fill="#6b7580"/>
    <g>
      <line x1="-30" y1="-6" x2="30" y2="-6" stroke="#6b7580" stroke-width="3"/>
      <circle cx="-30" cy="-6" r="7" fill="#f2c14e" stroke="#6b7580"/><circle cx="30" cy="-6" r="7" fill="#f2c14e" stroke="#6b7580"/>
      <animateTransform attributeName="transform" type="scale" values="1 1;-1 1;1 1" dur="1.2s" repeatCount="indefinite"/>
    </g>
  </g>
  <!-- girouette : flèche pointée vers l'ouest, d'où vient le vent -->
  <g transform="translate(400,100)">
    <g>
      <line x1="-40" y1="0" x2="34" y2="0" stroke="#3a3f45" stroke-width="3"/>
      <polygon points="-48,0 -34,-7 -34,7" fill="#3a3f45"/>
      <polygon points="26,-14 44,-14 40,0 44,14 26,14 32,0" fill="#c62828"/>
      <animateTransform attributeName="transform" type="rotate" values="-4;4;-4" dur="3s" repeatCount="indefinite"/>
    </g>
  </g>
  <!-- croisillon des points cardinaux sous la girouette -->
  <g font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1f2430" text-anchor="middle">
    <line x1="366" y1="128" x2="434" y2="128" stroke="#3a3f45" stroke-width="2"/>
    <text x="356" y="132">O</text><text x="446" y="132">E</text>
  </g>
  <!-- manche à air -->
  <g transform="translate(640,160)">
    <rect x="-2" y="0" width="4" height="90" fill="#9aa3ad"/>
    <g><path d="M2 4 L62 10 L62 22 L2 28 Z" fill="#e8612c"/><path d="M22 6 L22 26 M42 8 L42 24" stroke="#fff" stroke-width="5"/>
      <animateTransform attributeName="transform" type="skewY" values="0;3;0;-2;0" dur="2.5s" repeatCount="indefinite"/></g>
  </g>
  <!-- petit voilier au loin -->
  <g transform="translate(150,236)">
    <path d="M0 10 L40 10 L34 18 L6 18 Z" fill="#5b3f2a"/><path d="M20 10 L20 -22 L38 8 Z" fill="#fbfbf8" stroke="#9aa3ad"/>
    <animateTransform attributeName="transform" type="translate" values="150 236;170 234;150 236" dur="8s" repeatCount="indefinite"/>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MODULE 3 — Le jardin et le pluviomètre, sous l'averse
   ------------------------------------------------------------ */
"pluvio": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_GRIS}
    <linearGradient id="herbeP" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#6e9a55"/><stop offset="100%" stop-color="#4b713a"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielGris)"/>
  <g fill="#e4e8ec" opacity=".9">
    <ellipse cx="150" cy="40" rx="120" ry="30"/><ellipse cx="420" cy="30" rx="150" ry="34"/><ellipse cx="690" cy="46" rx="130" ry="30"/>
  </g>
  <!-- pluie -->
  <g stroke="#dbe8f4" stroke-width="1.6" stroke-linecap="round" opacity=".8">
    ${Array.from({length:34},(_,i)=>{const x=(i*23+7)%800, y=(i*37)%120+40;return `<line x1="${x}" y1="${y}" x2="${x-4}" y2="${y+14}"><animateTransform attributeName="transform" type="translate" values="0 -60;0 180" dur="${1.1+(i%5)*.15}s" repeatCount="indefinite"/></line>`;}).join("")}
  </g>
  <!-- haie et potager -->
  <rect x="0" y="176" width="800" height="30" fill="#4f7a3e"/>
  <rect x="0" y="206" width="800" height="94" fill="url(#herbeP)"/>
  <g fill="#6a4a2c"><rect x="60" y="226" width="160" height="30" rx="4"/><rect x="560" y="232" width="170" height="30" rx="4"/></g>
  <g fill="#8fbf5a"><circle cx="90" cy="226" r="9"/><circle cx="130" cy="224" r="10"/><circle cx="170" cy="226" r="9"/><circle cx="600" cy="232" r="10"/><circle cx="650" cy="230" r="9"/><circle cx="700" cy="232" r="10"/></g>
  <!-- flaques qui s'agrandissent -->
  <g fill="#9cc2df" opacity=".75">
    <ellipse cx="300" cy="276" rx="30" ry="6"><animate attributeName="rx" values="24;34;24" dur="5s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="520" cy="284" rx="22" ry="5"><animate attributeName="rx" values="18;28;18" dur="6s" repeatCount="indefinite"/></ellipse>
  </g>
  <!-- pluviomètre : entonnoir + tube gradué, sur un piquet, en terrain dégagé -->
  <g transform="translate(400,138)">
    <rect x="-3" y="80" width="6" height="52" fill="#8a93a0"/>
    <path d="M-26 0 L26 0 L10 18 L-10 18 Z" fill="#e7eef5" stroke="#6b7580" stroke-width="1.5"/>
    <rect x="-10" y="18" width="20" height="64" fill="#f4f8fb" stroke="#6b7580" stroke-width="1.5"/>
    <rect x="-9" y="58" width="18" height="23" fill="#5aa0d8" opacity=".85">
      <animate attributeName="y" values="70;58;70" dur="9s" repeatCount="indefinite"/>
      <animate attributeName="height" values="11;23;11" dur="9s" repeatCount="indefinite"/>
    </rect>
    <g stroke="#1f2430" stroke-width="1"><line x1="10" y1="26" x2="16" y2="26"/><line x1="10" y1="38" x2="16" y2="38"/><line x1="10" y1="50" x2="16" y2="50"/><line x1="10" y1="62" x2="16" y2="62"/><line x1="10" y1="74" x2="16" y2="74"/></g>
    <text x="22" y="54" font-size="11" fill="#fff" font-family="Arial,sans-serif">mm</text>
  </g>
  <!-- un arbre loin du pluviomètre (on l'installe à l'écart) -->
  <g transform="translate(120,120)"><rect x="-6" y="30" width="12" height="60" fill="#5b4327"/><ellipse cx="0" cy="18" rx="40" ry="38" fill="#4f7a3e"/></g>
</svg>`,

/* ------------------------------------------------------------
   MODULE 4 — Le bureau des relevés
   ------------------------------------------------------------ */
"bureau": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murB" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e9eef2"/><stop offset="100%" stop-color="#cfd8df"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murB)"/>
  <!-- fenêtre : dehors, le temps change -->
  <rect x="40" y="40" width="180" height="130" fill="#9cc3e0" stroke="#fff" stroke-width="6"/>
  <line x1="130" y1="40" x2="130" y2="170" stroke="#fff" stroke-width="5"/>
  <g><ellipse cx="90" cy="90" rx="34" ry="12" fill="#fff"/><animateTransform attributeName="transform" type="translate" values="-30 0;60 0;-30 0" dur="30s" repeatCount="indefinite"/></g>
  <!-- tableau de relevés -->
  <g transform="translate(260,32)">
    <rect width="300" height="150" rx="6" fill="#ffffff" stroke="#5b6b7a" stroke-width="2"/>
    <g stroke="#9aa6b2" stroke-width="1">
      ${[30,60,90,120].map(y=>`<line x1="0" y1="${y}" x2="300" y2="${y}"/>`).join("")}
      ${[60,120,180,240].map(x=>`<line x1="${x}" y1="0" x2="${x}" y2="150"/>`).join("")}
    </g>
    <g font-family="Arial,sans-serif" font-size="11" fill="#1f2430" text-anchor="middle">
      <text x="90" y="20">Lun</text><text x="150" y="20">Mar</text><text x="210" y="20">Mer</text><text x="270" y="20">Jeu</text>
      <text x="30" y="50">°C</text><text x="30" y="80">km/h</text><text x="30" y="110">mm</text>
    </g>
    <!-- une case clignote : il manque une valeur -->
    <rect x="182" y="92" width="56" height="26" fill="#f2c14e" opacity=".5"><animate attributeName="opacity" values=".15;.6;.15" dur="2.4s" repeatCount="indefinite"/></rect>
  </g>
  <!-- graphique en barres punaisé -->
  <g transform="translate(590,52)">
    <rect width="170" height="120" fill="#fff" stroke="#5b6b7a"/>
    <circle cx="85" cy="6" r="4" fill="#c62828"/>
    <g fill="#5aa0d8"><rect x="22" y="96" width="18" height="4"/><rect x="50" y="84" width="18" height="16"/><rect x="78" y="72" width="18" height="28"/><rect x="106" y="52" width="18" height="48"/><rect x="134" y="98" width="18" height="2"/></g>
    <line x1="14" y1="100" x2="160" y2="100" stroke="#1f2430"/>
  </g>
  <!-- bureau et cahier -->
  <rect x="0" y="222" width="800" height="78" fill="#a77a4f"/>
  <rect x="0" y="216" width="800" height="10" fill="#8b6340"/>
  <g transform="translate(330,196) rotate(-4)">
    <rect width="140" height="40" fill="#fbfbf8" stroke="#8a93a0"/><line x1="70" y1="0" x2="70" y2="40" stroke="#8a93a0"/>
    <g stroke="#b9c0c7"><line x1="8" y1="12" x2="62" y2="12"/><line x1="8" y1="22" x2="62" y2="22"/><line x1="78" y1="12" x2="132" y2="12"/><line x1="78" y1="22" x2="120" y2="22"/></g>
  </g>
  <g transform="translate(520,206)"><rect width="10" height="44" rx="3" fill="#2f5d8d" transform="rotate(70)"/></g>
</svg>`,

/* ------------------------------------------------------------
   MODULE 5 — La salle de prévision
   ------------------------------------------------------------ */
"studio": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murS" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1c2b40"/><stop offset="100%" stop-color="#0f1826"/></linearGradient>
    <linearGradient id="ecranS" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1f5a8a"/><stop offset="100%" stop-color="#113a5c"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murS)"/>
  <!-- grand écran : une carte stylisée avec des symboles -->
  <g transform="translate(200,26)">
    <rect width="400" height="190" rx="8" fill="url(#ecranS)" stroke="#6f8aa6" stroke-width="3"/>
    <path d="M150 30 L230 22 L290 60 L300 120 L250 170 L170 168 L120 120 L110 70 Z" fill="#3d7a55" stroke="#9fd0ae" stroke-width="1.5"/>
    <!-- soleil -->
    <g transform="translate(180,70)"><circle r="12" fill="#f2c14e"/>
      <g stroke="#f2c14e" stroke-width="3"><line x1="0" y1="-20" x2="0" y2="-16"/><line x1="0" y1="16" x2="0" y2="20"/><line x1="-20" y1="0" x2="-16" y2="0"/><line x1="16" y1="0" x2="20" y2="0"/>
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="20s" repeatCount="indefinite"/></g></g>
    <!-- nuage et pluie -->
    <g transform="translate(250,120)"><ellipse cx="0" cy="0" rx="22" ry="10" fill="#e4e8ec"/><ellipse cx="-10" cy="-6" rx="12" ry="9" fill="#e4e8ec"/>
      <g stroke="#9cc2df" stroke-width="2"><line x1="-8" y1="12" x2="-10" y2="20"/><line x1="4" y1="12" x2="2" y2="20"/><line x1="14" y1="12" x2="12" y2="20"/></g></g>
    <!-- flèche de vent d'ouest -->
    <g transform="translate(60,110)"><line x1="0" y1="0" x2="50" y2="0" stroke="#fff" stroke-width="3"/><polygon points="50,-7 64,0 50,7" fill="#fff"/>
      <animateTransform attributeName="transform" type="translate" values="50 110;70 110;50 110" dur="3s" repeatCount="indefinite"/></g>
    <text x="330" y="40" font-size="16" fill="#fff" font-family="Arial,sans-serif" font-weight="bold">21 °C</text>
    <text x="330" y="62" font-size="11" fill="#cfe0ee" font-family="Arial,sans-serif">max.</text>
  </g>
  <!-- bureau du présentateur et micro -->
  <rect x="0" y="236" width="800" height="64" fill="#26364d"/>
  <rect x="280" y="226" width="240" height="20" rx="4" fill="#3a4e6a"/>
  <g transform="translate(400,200)"><rect x="-2" y="0" width="4" height="28" fill="#9aa3ad"/><rect x="-7" y="-14" width="14" height="18" rx="7" fill="#3a3f45"/></g>
  <!-- voyant « à l'antenne » -->
  <g transform="translate(700,40)"><rect width="74" height="24" rx="4" fill="#2a0d0d" stroke="#c62828"/>
    <text x="37" y="16" font-size="11" fill="#ff8a80" text-anchor="middle" font-family="Arial,sans-serif">BULLETIN</text>
    <animate attributeName="opacity" values="1;.4;1" dur="2s" repeatCount="indefinite"/></g>
  <!-- projecteurs -->
  <g fill="#fff4c2" opacity=".08"><polygon points="40,0 120,0 260,236 120,236"/><polygon points="680,0 760,0 680,236 540,236"/></g>
</svg>`
};

/* ---- Animations réduites : les animations SMIL des SVG ne suivent pas
   le CSS ; on les fige donc explicitement quand body.calme est posé. ---- */
function figerDecorsSVG(){
  const calme = document.body && document.body.classList.contains("calme");
  document.querySelectorAll("svg.decor-svg").forEach(s=>{
    try{ calme ? s.pauseAnimations() : s.unpauseAnimations(); }catch(e){}
  });
}
if(typeof MutationObserver === "function"){
  const lancer = ()=>{
    new MutationObserver(figerDecorsSVG).observe(document.body, {attributes:true, attributeFilter:["class"], childList:true, subtree:true});
  };
  if(document.body) lancer(); else document.addEventListener("DOMContentLoaded", lancer);
}

window.figerDecorsSVG = figerDecorsSVG;
window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
