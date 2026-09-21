/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 salles du laboratoire de Madame Mélange
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (zéro attente, zéro fichier).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.png (ou .jpg, .webp)
     →  SVG    dessiné ci-dessous

   Les cinq lieux :
     balances  la salle des balances (balance à plateaux, électronique)
     cuisine   la cuisine d'essai (café, sucre, balance de cuisine)
     fioles    la salle des fioles (mélanges homogènes / hétérogènes)
     atelier   l'atelier de tri (tamis, aimant, bassine)
     saline    la saline (filtration, évaporation, marais salants)
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["balances"];
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
  // Animations réduites : les animations SVG (SMIL) sont figées
  if(document.body.classList.contains("calme")){
    sceneEl.querySelectorAll("svg").forEach(s=>{ try{ s.pauseAnimations(); }catch(e){} });
  }
}

const SALLE_NUM = { "balances":1, "cuisine":2, "fioles":3, "atelier":4, "saline":5 };

/* ---- Fragments communs ---- */
const MUR_LABO = (id, c1, c2) => `
  <linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="${c1}"/><stop offset="100%" stop-color="${c2}"/>
  </linearGradient>`;

/** Une fiole (erlenmeyer) : x, y = base gauche ; liquide éventuellement en deux couches. */
function fiole(x, y, h, couleur, couche){
  const w = h*0.8;
  return `<g transform="translate(${x},${y})">
    <path d="M${w*0.38} ${-h} h${w*0.24} v${h*0.3} L${w} 0 H0 L${w*0.38} ${-h*0.7} Z" fill="#eaf4f8" stroke="#56707a" stroke-width="1.5"/>
    <path d="M${w*0.14} ${-h*0.28} L${w*0.86} ${-h*0.28} L${w} 0 H0 Z" fill="${couleur}" opacity=".85"/>
    ${couche?`<path d="M${w*0.24} ${-h*0.46} L${w*0.76} ${-h*0.46} L${w*0.86} ${-h*0.28} H${w*0.14} Z" fill="${couche}" opacity=".9"/>`:""}
    <rect x="${w*0.36}" y="${-h-5}" width="${w*0.28}" height="6" rx="2" fill="#8b5a2b"/>
  </g>`;
}

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — La salle des balances
   ------------------------------------------------------------ */
"balances": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true">
  <defs>${MUR_LABO("murB","#e9eef1","#cdd8de")}
    <linearGradient id="bois1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#b98a57"/><stop offset="100%" stop-color="#8a6238"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murB)"/>
  <!-- carrelage mural -->
  <g stroke="#b9c7cf" stroke-width="1" opacity=".6">
    ${Array.from({length:16},(_,i)=>`<line x1="${i*50}" y1="0" x2="${i*50}" y2="200"/>`).join("")}
    ${Array.from({length:5},(_,i)=>`<line x1="0" y1="${i*40}" x2="800" y2="${i*40}"/>`).join("")}
  </g>
  <!-- étagère haute avec masses marquées -->
  <rect x="40" y="70" width="300" height="10" fill="url(#bois1)"/>
  <g fill="#b08d2a">
    <rect x="60" y="44" width="22" height="26" rx="3"/><rect x="92" y="50" width="18" height="20" rx="3"/><rect x="118" y="55" width="14" height="15" rx="3"/><rect x="138" y="59" width="10" height="11" rx="2"/>
  </g>
  <g transform="translate(200,40)">${fiole(0,30,30,"#6fa8dc")}</g>
  <g transform="translate(250,40)">${fiole(0,30,30,"#f1c232")}</g>
  <!-- horloge -->
  <g transform="translate(700,60)">
    <circle r="26" fill="#fff" stroke="#56707a" stroke-width="3"/>
    <line x1="0" y1="0" x2="0" y2="-16" stroke="#333" stroke-width="3"><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="60s" repeatCount="indefinite"/></line>
    <line x1="0" y1="0" x2="10" y2="0" stroke="#333" stroke-width="3"/>
  </g>
  <!-- paillasse -->
  <rect x="0" y="200" width="800" height="100" fill="#dfe3e6"/>
  <rect x="0" y="196" width="800" height="10" fill="#9aa7ae"/>
  <!-- balance à plateaux (qui oscille doucement) -->
  <g transform="translate(250,196)">
    <rect x="-40" y="-8" width="80" height="8" fill="#6b5410"/>
    <rect x="-4" y="-80" width="8" height="72" fill="#8a6d12"/>
    <g>
      <animateTransform attributeName="transform" type="rotate" values="-4 0 -80;4 0 -80;-4 0 -80" dur="6s" repeatCount="indefinite"/>
      <rect x="-90" y="-84" width="180" height="7" rx="3" fill="#c9a227"/>
      <line x1="-80" y1="-80" x2="-80" y2="-50" stroke="#555"/><line x1="80" y1="-80" x2="80" y2="-50" stroke="#555"/>
      <path d="M-110 -50 H-50 L-58 -40 H-102 Z" fill="#c9a227"/><path d="M50 -50 H110 L102 -40 H58 Z" fill="#c9a227"/>
      <circle cx="-80" cy="-60" r="10" fill="#c0392b"/>
      <rect x="70" y="-66" width="10" height="16" fill="#555"/><rect x="84" y="-60" width="8" height="10" fill="#555"/>
    </g>
  </g>
  <!-- balance électronique -->
  <g transform="translate(520,196)">
    <rect x="-70" y="-30" width="140" height="30" rx="6" fill="#cfd8df" stroke="#56707a"/>
    <rect x="-56" y="-44" width="112" height="12" rx="3" fill="#aab6bf"/>
    <rect x="-48" y="-24" width="62" height="18" fill="#123"/>
    <text x="-17" y="-10" text-anchor="middle" font-family="monospace" font-size="13" fill="#7CFC9A">250 g<animate attributeName="opacity" values="1;.6;1" dur="2s" repeatCount="indefinite"/></text>
    <rect x="22" y="-24" width="36" height="18" rx="3" fill="#1d3a8a"/><text x="40" y="-11" text-anchor="middle" font-family="system-ui" font-size="9" fill="#fff">TARE</text>
    <g transform="translate(-20,-44)">${fiole(0,0,40,"#93c47d")}</g>
  </g>
  <!-- fioles renversées au sol -->
  <g transform="translate(680,250) rotate(80)">${fiole(0,0,34,"#e06666")}</g>
  <ellipse cx="660" cy="262" rx="40" ry="6" fill="#e06666" opacity=".35"/>
  <g transform="translate(90,262) rotate(-75)">${fiole(0,0,30,"#8e7cc3")}</g>
  <ellipse cx="120" cy="266" rx="30" ry="5" fill="#8e7cc3" opacity=".3"/>
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — La cuisine d'essai
   ------------------------------------------------------------ */
"cuisine": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true">
  <defs>${MUR_LABO("murC","#fbf3e4","#efdcc0")}</defs>
  <rect width="800" height="300" fill="url(#murC)"/>
  <!-- carrelage en damier -->
  <g fill="#f3e6cf">${Array.from({length:32},(_,i)=>`<rect x="${(i%16)*50+((Math.floor(i/16))%2?25:0)}" y="${110+Math.floor(i/16)*30}" width="25" height="30"/>`).join("")}</g>
  <!-- affiche -->
  <g transform="translate(560,30)">
    <rect width="190" height="70" rx="6" fill="#fff" stroke="#c0392b" stroke-width="3"/>
    <text x="95" y="28" text-anchor="middle" font-family="system-ui" font-size="14" font-weight="bold" fill="#c0392b">CUISINE D'ESSAI</text>
    <text x="95" y="50" text-anchor="middle" font-family="system-ui" font-size="12" fill="#333">Ici, on mesure.</text>
    <text x="95" y="64" text-anchor="middle" font-family="system-ui" font-size="12" fill="#333">On ne goûte pas.</text>
  </g>
  <!-- étagère : bocaux -->
  <rect x="40" y="80" width="260" height="8" fill="#a0764a"/>
  <g>
    <rect x="60" y="40" width="40" height="40" rx="6" fill="#fff" stroke="#999"/><text x="80" y="64" text-anchor="middle" font-family="system-ui" font-size="10" fill="#555">SUCRE</text>
    <rect x="120" y="44" width="40" height="36" rx="6" fill="#fff" stroke="#999"/><text x="140" y="66" text-anchor="middle" font-family="system-ui" font-size="10" fill="#555">SEL</text>
    <rect x="180" y="40" width="40" height="40" rx="6" fill="#6b4226" stroke="#999"/><text x="200" y="64" text-anchor="middle" font-family="system-ui" font-size="10" fill="#fff">CAFÉ</text>
  </g>
  <!-- plan de travail -->
  <rect x="0" y="200" width="800" height="100" fill="#eee"/>
  <rect x="0" y="194" width="800" height="12" fill="#b7b7b7"/>
  <!-- cafetière fumante -->
  <g transform="translate(160,194)">
    <path d="M-30 0 V-70 H30 V0 Z" fill="#333"/><rect x="-24" y="-60" width="48" height="36" fill="#6b4226" opacity=".85"/>
    <path d="M30 -60 q20 10 0 30" stroke="#333" stroke-width="5" fill="none"/>
    <g stroke="#bbb" stroke-width="3" fill="none" opacity=".7">
      <path d="M-8 -78 q6 -12 0 -24"><animate attributeName="opacity" values="0;.8;0" dur="3s" repeatCount="indefinite"/></path>
      <path d="M8 -80 q6 -12 0 -24"><animate attributeName="opacity" values=".8;0;.8" dur="3s" repeatCount="indefinite"/></path>
    </g>
  </g>
  <!-- tasse sur la balance de cuisine -->
  <g transform="translate(400,194)">
    <rect x="-60" y="-16" width="120" height="16" rx="5" fill="#dfe6ee" stroke="#777"/>
    <rect x="-22" y="-12" width="44" height="10" fill="#123"/><text x="0" y="-4" text-anchor="middle" font-family="monospace" font-size="9" fill="#7CFC9A">185 g</text>
    <path d="M-24 -16 V-50 H24 V-16 Z" fill="#fff" stroke="#777"/><path d="M24 -44 q14 6 0 20" stroke="#777" stroke-width="4" fill="none"/>
    <rect x="-20" y="-44" width="40" height="6" fill="#6b4226"/>
    <!-- cuillère qui tourne -->
    <g><animateTransform attributeName="transform" type="translate" values="-6 0;6 0;-6 0" dur="1.6s" repeatCount="indefinite"/>
      <line x1="0" y1="-44" x2="10" y2="-70" stroke="#aaa" stroke-width="3"/></g>
  </g>
  <!-- sucrier et verres gradués -->
  <g transform="translate(560,194)">
    <path d="M-20 0 V-30 H20 V0 Z" fill="#fff" stroke="#777"/><rect x="-10" y="-40" width="8" height="8" fill="#fff" stroke="#999"/><rect x="2" y="-38" width="8" height="8" fill="#fff" stroke="#999"/>
  </g>
  <g transform="translate(650,194)">
    <path d="M-16 0 V-60 H16 V0 Z" fill="#e8f4fb" stroke="#56707a"/><rect x="-14" y="-34" width="28" height="32" fill="#9fd3f5"/>
    <g stroke="#56707a">${[10,20,30,40,50].map(v=>`<line x1="-16" y1="${-v}" x2="-8" y2="${-v}"/>`).join("")}</g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — La salle des fioles
   ------------------------------------------------------------ */
"fioles": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true">
  <defs>${MUR_LABO("murF","#e4ecef","#c3d2d8")}
    <radialGradient id="lumF" cx="50%" cy="0%" r="70%"><stop offset="0%" stop-color="#fff8dc" stop-opacity=".8"/><stop offset="100%" stop-color="#fff8dc" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murF)"/>
  <rect width="800" height="300" fill="url(#lumF)"/>
  <!-- trois étagères de fioles -->
  ${[70,145,220].map((y,r)=>`
    <rect x="30" y="${y}" width="480" height="8" fill="#8a6238"/>
    ${Array.from({length:9},(_,i)=>{
      const couleurs=[["#9fd3f5",""],["#9fd3f5","#f1c232"],["#b6d7a8",""],["#cfe2f3",""],["#d9c7a7",""],["#ea9999",""],["#9fd3f5","#f1c232"],["#fce5cd",""],["#b4a7d6",""]];
      const c=couleurs[(i+r*3)%9];
      return fiole(44+i*52, y, 40, c[0], c[1]);
    }).join("")}`).join("")}
  <!-- dépôt au fond d'une fiole : eau boueuse -->
  <g transform="translate(252,145)"><rect x="6" y="-6" width="20" height="6" fill="#8d6e3f"/></g>
  <!-- portrait de Madame Mélange -->
  <g transform="translate(610,40)">
    <rect width="140" height="170" rx="4" fill="#c9a227"/><rect x="10" y="10" width="120" height="150" fill="#2c3e50"/>
    <circle cx="70" cy="68" r="28" fill="#e2b183"/>
    <path d="M40 60 q30 -44 60 0 q-4 -30 -30 -32 q-26 2 -30 32" fill="#dcdcdc"/>
    <circle cx="60" cy="66" r="7" fill="none" stroke="#333" stroke-width="2"/><circle cx="80" cy="66" r="7" fill="none" stroke="#333" stroke-width="2"/><line x1="67" y1="66" x2="73" y2="66" stroke="#333" stroke-width="2"/>
    <path d="M36 160 Q70 96 104 160 Z" fill="#fff"/>
    <g transform="translate(104,110)"><circle r="10" fill="none" stroke="#c9a227" stroke-width="3"/><line x1="7" y1="7" x2="18" y2="18" stroke="#c9a227" stroke-width="4"/></g>
    <text x="70" y="186" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#333">Madame Mélange</text>
  </g>
  <!-- sol -->
  <rect x="0" y="240" width="800" height="60" fill="#b8c4ca"/>
  <!-- bulles qui montent dans une fiole de sirop -->
  <g transform="translate(560,240)">${fiole(0,0,50,"#b6d7a8")}
    <circle cx="20" cy="-8" r="2" fill="#fff"><animate attributeName="cy" values="-6;-22;-6" dur="3s" repeatCount="indefinite"/></circle>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — L'atelier de tri
   ------------------------------------------------------------ */
"atelier": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true">
  <defs>${MUR_LABO("murA","#dde3e2","#b9c3c1")}
    <linearGradient id="etabli" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#b98a57"/><stop offset="100%" stop-color="#7d5a33"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murA)"/>
  <!-- briques -->
  <g stroke="#a9b3b1" stroke-width="1" opacity=".7">
    ${Array.from({length:6},(_,r)=>`<line x1="0" y1="${r*32}" x2="800" y2="${r*32}"/>`).join("")}
  </g>
  <!-- tamis accrochés -->
  ${[80,160,240].map((x,i)=>`<g transform="translate(${x},70)">
    <circle r="${26-i*4}" fill="#d9d2c0" stroke="#7d5a33" stroke-width="5"/>
    <g stroke="#9a9280" stroke-width="1">${[-12,-6,0,6,12].map(v=>`<line x1="${v}" y1="-18" x2="${v}" y2="18"/><line x1="-18" y1="${v}" x2="18" y2="${v}"/>`).join("")}</g>
  </g>`).join("")}
  <!-- grand aimant en fer à cheval, qui se balance -->
  <g transform="translate(420,30)">
    <line x1="0" y1="0" x2="0" y2="40" stroke="#555" stroke-width="2"/>
    <g><animateTransform attributeName="transform" type="rotate" values="-6 0 0;6 0 0;-6 0 0" dur="4s" repeatCount="indefinite"/>
      <path d="M-30 40 v40 a30 30 0 0 0 60 0 v-40 h-16 v40 a14 14 0 0 1 -28 0 v-40 z" fill="#c0392b"/>
      <rect x="-30" y="40" width="16" height="12" fill="#ccc"/><rect x="14" y="40" width="16" height="12" fill="#ccc"/>
      <text x="-22" y="62" font-family="system-ui" font-size="10" font-weight="bold" fill="#fff">N</text><text x="18" y="62" font-family="system-ui" font-size="10" font-weight="bold" fill="#fff">S</text>
    </g>
  </g>
  <!-- établi -->
  <rect x="0" y="200" width="800" height="100" fill="#8f9a98"/>
  <rect x="20" y="188" width="760" height="16" fill="url(#etabli)"/>
  <!-- bacs -->
  ${[["#d8c08a","sable"],["#8d8d8d","gravier"],["#c9a36b","sciure"],["#d8c08a","limaille"]].map((b,i)=>`<g transform="translate(${80+i*170},188)">
    <path d="M-60 0 L-50 -40 H50 L60 0 Z" fill="#4a90a4" opacity=".85"/>
    <ellipse cx="0" cy="-40" rx="50" ry="6" fill="${b[0]}"/>
    ${b[1]==="limaille"?`<g fill="#555">${[-30,-14,4,22,34].map(v=>`<rect x="${v}" y="-44" width="3" height="3"><animate attributeName="opacity" values="1;.3;1" dur="${2+Math.abs(v)%3}s" repeatCount="indefinite"/></rect>`).join("")}</g>`:""}
    <text x="0" y="-14" text-anchor="middle" font-family="system-ui" font-size="12" fill="#fff">${b[1]}</text>
  </g>`).join("")}
  <!-- bassine d'eau -->
  <g transform="translate(700,250)">
    <ellipse cx="0" cy="0" rx="60" ry="16" fill="#bfe3f7" stroke="#4a6572" stroke-width="3"/>
    <g fill="#b5783a"><rect x="-20" y="-4" width="8" height="3"><animate attributeName="y" values="-4;-6;-4" dur="2.5s" repeatCount="indefinite"/></rect><rect x="10" y="-2" width="8" height="3"/></g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — La saline
   ------------------------------------------------------------ */
"saline": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true">
  <defs>
    <linearGradient id="cielS" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#8ec5e8"/><stop offset="100%" stop-color="#e3f1f8"/></linearGradient>
    <linearGradient id="murS" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f4f1ea"/><stop offset="100%" stop-color="#ddd6c6"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murS)"/>
  <!-- grande fenêtre sur les marais salants -->
  <g transform="translate(360,20)">
    <rect width="400" height="170" fill="url(#cielS)" stroke="#8a6238" stroke-width="8"/>
    <circle cx="330" cy="40" r="22" fill="#f6d55c"><animate attributeName="r" values="21;24;21" dur="5s" repeatCount="indefinite"/></circle>
    <!-- bassins -->
    <g>
      ${[0,1,2,3].map(i=>`<rect x="${10+i*96}" y="110" width="88" height="22" fill="#a9d4e6" stroke="#c9b28c" stroke-width="3"/>`).join("")}
      ${[0,1,2,3].map(i=>`<rect x="${10+i*96}" y="138" width="88" height="22" fill="#bfe1ee" stroke="#c9b28c" stroke-width="3"/>`).join("")}
    </g>
    <!-- tas de sel -->
    <path d="M240 110 l20 -26 l20 26 z" fill="#fff" stroke="#ccc"/><path d="M280 110 l14 -18 l14 18 z" fill="#fff" stroke="#ccc"/>
    <!-- mouette -->
    <path d="M60 40 q10 -8 20 0 q10 -8 20 0" stroke="#555" stroke-width="2" fill="none"><animateTransform attributeName="transform" type="translate" values="0 0;160 -10;0 0" dur="18s" repeatCount="indefinite"/></path>
    <line x1="200" y1="0" x2="200" y2="170" stroke="#8a6238" stroke-width="6"/>
    <line x1="0" y1="85" x2="400" y2="85" stroke="#8a6238" stroke-width="4" opacity=".5"/>
  </g>
  <!-- paillasse -->
  <rect x="0" y="200" width="800" height="100" fill="#d9dde0"/>
  <rect x="0" y="194" width="800" height="12" fill="#98a4ab"/>
  <!-- montage de filtration avec gouttes -->
  <g transform="translate(140,194)">
    <rect x="-50" y="-150" width="8" height="150" fill="#777"/><rect x="-50" y="-110" width="60" height="6" fill="#777"/>
    <path d="M-30 -140 H50 L16 -100 V-80 H4 V-100 Z" fill="#e8eef3" stroke="#555"/>
    <path d="M-20 -137 H40 L10 -104 Z" fill="#fff" stroke="#aaa"/><path d="M-4 -120 H24 L10 -104 Z" fill="#c8a86b"/>
    <circle cx="10" cy="-76" r="3" fill="#7fb8e0"><animate attributeName="cy" values="-76;-30;-76" dur="1.4s" repeatCount="indefinite"/></circle>
    <path d="M-16 -50 V0 H36 V-50" fill="none" stroke="#555" stroke-width="3"/><rect x="-14" y="-24" width="48" height="22" fill="#bfe3f7"/>
  </g>
  <!-- coupelle d'évaporation au soleil -->
  <g transform="translate(300,194)">
    <path d="M-40 -6 Q0 16 40 -6" fill="#fff" stroke="#555" stroke-width="3"/>
    <g fill="#fff" stroke="#999"><rect x="-10" y="-4" width="5" height="4"/><rect x="0" y="-3" width="5" height="4"/><rect x="10" y="-4" width="5" height="4"/></g>
    <g stroke="#9aa" stroke-width="2" fill="none">
      <path d="M-14 -16 q5 -10 0 -20"><animate attributeName="opacity" values="0;.9;0" dur="3s" repeatCount="indefinite"/></path>
      <path d="M8 -18 q5 -10 0 -20"><animate attributeName="opacity" values=".9;0;.9" dur="3s" repeatCount="indefinite"/></path>
    </g>
  </g>
  <!-- le dernier bocal de Madame Mélange -->
  <g transform="translate(560,194)">
    <path d="M-34 0 V-70 Q-34 -80 -24 -80 H24 Q34 -80 34 -70 V0 Z" fill="#e8f4fb" stroke="#56707a" stroke-width="2"/>
    <rect x="-32" y="-54" width="64" height="52" fill="#bfe3f7"/>
    <g fill="#555">${[-20,-8,6,18].map(v=>`<rect x="${v}" y="-8" width="3" height="3"/>`).join("")}</g>
    <rect x="-26" y="-92" width="52" height="12" rx="3" fill="#8b5a2b"/>
    <rect x="-24" y="-44" width="48" height="18" fill="#fff" opacity=".9"/><text x="0" y="-31" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#333">n° 5</text>
  </g>
</svg>`
};

window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
