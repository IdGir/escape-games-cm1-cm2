/* ============================================================
   DÉCORS SVG ANIMÉS — les cinq pages du « Manuscrit de l'abbaye »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (zéro attente, zéro fichier).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg
     →  SVG    dessiné ci-dessous

   Les cinq lieux :
     reims        Reims, le baptême de Clovis (vers l'an 500)
     aix          Aix-la-Chapelle, la chapelle et la cour de Charlemagne
     scriptorium  le scriptorium de l'abbaye
     hoteldieu    la grande salle de l'hôtel-Dieu
     chantier     l'église romane de l'abbaye et la cathédrale gothique
   Les dessins sont des évocations, pas des restitutions exactes.
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["scriptorium"];
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

const SALLE_NUM = { "reims":1, "aix":2, "scriptorium":3, "hoteldieu":4, "chantier":5 };

/* ---- Fragments communs ---- */
const SVG_OUVERT = `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">`;

/** Une flamme de bougie qui vacille. */
function bougie(x, y, h=26){
  return `<g>
    <rect x="${x-4}" y="${y}" width="8" height="${h}" fill="#f3ead2" stroke="#b9a77c"/>
    <path d="M${x} ${y-14} Q${x+6} ${y-5} ${x} ${y-1} Q${x-6} ${y-5} ${x} ${y-14}" fill="#f6c343">
      <animateTransform attributeName="transform" type="scale" additive="sum" values="1 1;1 1.12;1 .94;1 1" dur="1.6s" repeatCount="indefinite"/>
    </path>
    <circle cx="${x}" cy="${y-6}" r="14" fill="#ffd966" opacity=".18">
      <animate attributeName="opacity" values=".12;.25;.12" dur="1.6s" repeatCount="indefinite"/>
    </circle>
  </g>`;
}

/** Un arc en plein cintre (roman) ou brisé (gothique), ouvert. */
function arc(x, y, l, h, brise, remplissage){
  const m = x + l/2;
  const haut = brise
    ? `Q${x} ${y-h*0.25} ${m} ${y-h*0.55} Q${x+l} ${y-h*0.25} ${x+l} ${y}`
    : `A${l/2} ${l/2} 0 0 1 ${x+l} ${y}`;
  return `<path d="M${x} ${y+h} L${x} ${y} ${haut} L${x+l} ${y+h} Z" fill="${remplissage}"/>`;
}

const SVG_DECORS = {

/* ------------------------------------------------------------
   PAGE 1 — Reims : la cuve du baptême, sous des arcs arrondis
   ------------------------------------------------------------ */
"reims": `${SVG_OUVERT}
  <defs>
    <linearGradient id="murRe" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#6e5a44"/><stop offset="100%" stop-color="#3d3024"/></linearGradient>
    <linearGradient id="solRe" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#8b7657"/><stop offset="100%" stop-color="#5c4b37"/></linearGradient>
    <radialGradient id="lumRe" cx="50%" cy="20%" r="60%"><stop offset="0%" stop-color="#ffe7a3" stop-opacity=".55"/><stop offset="100%" stop-color="#ffe7a3" stop-opacity="0"/></radialGradient>
    <linearGradient id="eauRe" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#8fc3d9"/><stop offset="100%" stop-color="#3f7f9a"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murRe)"/>
  <!-- arcades en plein cintre -->
  <g fill="#2a2119" opacity=".75">
    ${arc(40,110,110,150,false,"#2a2119")}${arc(190,110,110,150,false,"#2a2119")}
    ${arc(500,110,110,150,false,"#2a2119")}${arc(650,110,110,150,false,"#2a2119")}
  </g>
  <g stroke="#a58c68" stroke-width="3" fill="none" opacity=".7">
    <path d="M40 110 A55 55 0 0 1 150 110"/><path d="M190 110 A55 55 0 0 1 300 110"/>
    <path d="M500 110 A55 55 0 0 1 610 110"/><path d="M650 110 A55 55 0 0 1 760 110"/>
  </g>
  <!-- fenêtre haute et rayon de lumière -->
  <rect x="385" y="26" width="30" height="54" rx="15" fill="#f7e2a4"/>
  <polygon points="385,80 415,80 470,300 330,300" fill="url(#lumRe)">
    <animate attributeName="opacity" values=".7;1;.7" dur="7s" repeatCount="indefinite"/>
  </polygon>
  <!-- sol -->
  <rect y="240" width="800" height="60" fill="url(#solRe)"/>
  <!-- cuve baptismale -->
  <ellipse cx="400" cy="244" rx="92" ry="16" fill="#3a2f24"/>
  <path d="M312 214 L322 250 Q400 266 478 250 L488 214 Z" fill="#b8a585" stroke="#6e5a44" stroke-width="2"/>
  <ellipse cx="400" cy="214" rx="88" ry="14" fill="url(#eauRe)"/>
  <ellipse cx="400" cy="214" rx="40" ry="5" fill="#d8f0f7" opacity=".6">
    <animate attributeName="rx" values="30;60;30" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values=".6;.1;.6" dur="4s" repeatCount="indefinite"/>
  </ellipse>
  <!-- bannières franques -->
  <g>
    <path d="M110 60 L150 60 L150 118 L130 106 L110 118 Z" fill="#7d1818"><animateTransform attributeName="transform" type="skewX" values="0;2;0;-2;0" dur="6s" repeatCount="indefinite"/></path>
    <path d="M650 60 L690 60 L690 118 L670 106 L650 118 Z" fill="#16296b"><animateTransform attributeName="transform" type="skewX" values="0;-2;0;2;0" dur="6s" repeatCount="indefinite"/></path>
  </g>
  ${bougie(250,206)}${bougie(550,206)}
</svg>`,

/* ------------------------------------------------------------
   PAGE 2 — Aix-la-Chapelle : la chapelle à coupole, l'or des mosaïques
   ------------------------------------------------------------ */
"aix": `${SVG_OUVERT}
  <defs>
    <linearGradient id="cielAx" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#7fa0c9"/><stop offset="100%" stop-color="#d8e2ee"/></linearGradient>
    <linearGradient id="pierreAx" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e3d6bc"/><stop offset="100%" stop-color="#b9a584"/></linearGradient>
    <linearGradient id="orAx" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f3d97a"/><stop offset="100%" stop-color="#b8892a"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielAx)"/>
  <g opacity=".5"><ellipse cx="160" cy="44" rx="56" ry="14" fill="#fff"><animate attributeName="cx" values="140;660;140" dur="100s" repeatCount="indefinite"/></ellipse></g>
  <!-- chapelle octogonale à coupole -->
  <rect x="300" y="120" width="200" height="130" fill="url(#pierreAx)"/>
  <polygon points="300,120 330,96 470,96 500,120" fill="#cbb994"/>
  <path d="M330 96 Q400 20 470 96 Z" fill="#8a7a5c"/>
  <rect x="396" y="8" width="8" height="28" fill="#b8892a"/>
  <g fill="#4e5d6e">
    ${arc(318,150,30,50,false,"#4e5d6e")}${arc(362,150,30,50,false,"#4e5d6e")}${arc(408,150,30,50,false,"#4e5d6e")}${arc(452,150,30,50,false,"#4e5d6e")}
  </g>
  <!-- porte et mosaïque dorée -->
  <path d="M378 250 L378 214 A22 22 0 0 1 422 214 L422 250 Z" fill="url(#orAx)"/>
  <circle cx="400" cy="226" r="6" fill="#16296b"/>
  <!-- palais (ailes) -->
  <rect x="40" y="150" width="240" height="100" fill="url(#pierreAx)"/>
  <polygon points="40,150 160,118 280,150" fill="#a8452f"/>
  <rect x="520" y="150" width="240" height="100" fill="url(#pierreAx)"/>
  <polygon points="520,150 640,118 760,150" fill="#a8452f"/>
  <g fill="#4e5d6e">${[70,120,170,220,550,600,650,700].map(x=>`<rect x="${x}" y="176" width="22" height="34" rx="11"/>`).join("")}</g>
  <!-- cour -->
  <rect y="250" width="800" height="50" fill="#9b8b6c"/>
  <!-- tablettes de cire des élèves, posées sur un banc -->
  <rect x="560" y="262" width="150" height="10" fill="#6d4c2f"/>
  <g>
    <rect x="572" y="248" width="30" height="16" fill="#c9a24d" stroke="#6d4c2f"/><rect x="612" y="248" width="30" height="16" fill="#c9a24d" stroke="#6d4c2f"/><rect x="652" y="248" width="30" height="16" fill="#c9a24d" stroke="#6d4c2f"/>
  </g>
  <!-- étendard qui flotte -->
  <g transform="translate(400,8)">
    <path d="M4 2 L40 6 L4 18 Z" fill="#a8261b"><animateTransform attributeName="transform" type="skewY" values="0;4;0;-4;0" dur="5s" repeatCount="indefinite"/></path>
  </g>
</svg>`,

/* ------------------------------------------------------------
   PAGE 3 — Le scriptorium : pupitres sous les fenêtres
   ------------------------------------------------------------ */
"scriptorium": `${SVG_OUVERT}
  <defs>
    <linearGradient id="murSc" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#8c7a60"/><stop offset="100%" stop-color="#5b4c3a"/></linearGradient>
    <linearGradient id="rayonSc" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fff2c4" stop-opacity=".6"/><stop offset="100%" stop-color="#fff2c4" stop-opacity="0"/></linearGradient>
    <linearGradient id="boisSc" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#8a5a33"/><stop offset="100%" stop-color="#5a3a20"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murSc)"/>
  <!-- voûte -->
  <path d="M0 40 Q400 -30 800 40 L800 0 L0 0 Z" fill="#4a3c2d"/>
  <!-- trois fenêtres et leurs rayons -->
  ${[150,400,650].map((x,i)=>`
    <rect x="${x-18}" y="46" width="36" height="70" rx="18" fill="#fbeec0" stroke="#4a3c2d" stroke-width="3"/>
    <polygon points="${x-18},116 ${x+18},116 ${x+80},290 ${x-20},290" fill="url(#rayonSc)">
      <animate attributeName="opacity" values=".6;1;.6" dur="${8+i}s" repeatCount="indefinite"/>
    </polygon>`).join("")}
  <!-- sol -->
  <rect y="246" width="800" height="54" fill="#6f5d45"/>
  <!-- pupitres avec parchemin -->
  ${[150,400,650].map(x=>`
    <g>
      <rect x="${x-6}" y="196" width="12" height="54" fill="url(#boisSc)"/>
      <polygon points="${x-54},196 ${x+54},178 ${x+54},190 ${x-54},208" fill="url(#boisSc)"/>
      <polygon points="${x-44},192 ${x+42},177 ${x+42},184 ${x-44},199" fill="#f4ead0"/>
      <g stroke="#2b1d10" stroke-width="1" opacity=".6">
        <line x1="${x-38}" y1="193" x2="${x+30}" y2="181"/><line x1="${x-38}" y1="196" x2="${x+10}" y2="188"/>
      </g>
      <rect x="${x-40}" y="189" width="7" height="7" fill="#a8261b"/>
      <!-- plume d'oie qui écrit -->
      <g>
        <path d="M${x+22} 182 q10 -22 26 -30 q-8 18 -24 32 Z" fill="#fbfbf6" stroke="#8c7a60"/>
        <animateTransform attributeName="transform" type="translate" values="0 0;-6 1;0 0" dur="2.4s" repeatCount="indefinite"/>
      </g>
    </g>`).join("")}
  <!-- grains de poussière dans la lumière -->
  <g fill="#fff6d6">
    <circle cx="420" cy="160" r="1.6"><animate attributeName="cy" values="160;130;160" dur="9s" repeatCount="indefinite"/></circle>
    <circle cx="440" cy="200" r="1.2"><animate attributeName="cy" values="200;170;200" dur="11s" repeatCount="indefinite"/></circle>
    <circle cx="170" cy="190" r="1.4"><animate attributeName="cy" values="190;150;190" dur="10s" repeatCount="indefinite"/></circle>
    <circle cx="680" cy="170" r="1.3"><animate attributeName="cy" values="170;140;170" dur="12s" repeatCount="indefinite"/></circle>
  </g>
  <!-- étagère de livres -->
  <rect x="740" y="120" width="60" height="8" fill="url(#boisSc)"/>
  <g>${["#16296b","#7d1818","#2e6b3a","#8a6d12"].map((c,i)=>`<rect x="${744+i*13}" y="92" width="11" height="28" fill="${c}"/>`).join("")}</g>
</svg>`,

/* ------------------------------------------------------------
   PAGE 4 — L'hôtel-Dieu : la grande salle, les lits, la chapelle
   ------------------------------------------------------------ */
"hoteldieu": `${SVG_OUVERT}
  <defs>
    <linearGradient id="charpHd" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#5b3a22"/><stop offset="100%" stop-color="#8a5a33"/></linearGradient>
    <linearGradient id="murHd" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e9dcc0"/><stop offset="100%" stop-color="#cdb992"/></linearGradient>
    <linearGradient id="rideauHd" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#8e1d17"/><stop offset="50%" stop-color="#b3322a"/><stop offset="100%" stop-color="#8e1d17"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murHd)"/>
  <!-- charpente en berceau lambrissé -->
  <path d="M0 110 Q400 -60 800 110 L800 0 L0 0 Z" fill="url(#charpHd)"/>
  <g stroke="#3d2614" stroke-width="3" opacity=".7">
    ${[80,200,320,480,600,720].map(x=>`<line x1="${x}" y1="${110-Math.round(Math.sin(Math.PI*x/800)*80)}" x2="${x}" y2="112"/>`).join("")}
  </g>
  <!-- chapelle au fond -->
  <path d="M360 230 L360 150 Q400 110 440 150 L440 230 Z" fill="#6f5a3e"/>
  <rect x="382" y="166" width="36" height="46" rx="18" fill="#7fa8d6" stroke="#3d2614" stroke-width="2"/>
  <path d="M400 166 V212 M382 186 H418" stroke="#3d2614" stroke-width="2"/>
  ${bougie(372,208,18)}${bougie(428,208,18)}
  <!-- sol -->
  <rect y="230" width="800" height="70" fill="#a98f67"/>
  <g stroke="#8a7050" opacity=".5">${[260,280].map(y=>`<line x1="0" y1="${y}" x2="800" y2="${y}"/>`).join("")}</g>
  <!-- lits à rideaux, de chaque côté -->
  ${[20,130,240].map(x=>`
    <g>
      <rect x="${x}" y="150" width="90" height="12" fill="#5b3a22"/>
      <rect x="${x}" y="162" width="16" height="80" fill="url(#rideauHd)"/>
      <rect x="${x+16}" y="206" width="74" height="26" fill="#f4efe2" stroke="#b9a77c"/>
      <rect x="${x+16}" y="232" width="74" height="10" fill="#5b3a22"/>
    </g>`).join("")}
  ${[470,580,690].map(x=>`
    <g>
      <rect x="${x}" y="150" width="90" height="12" fill="#5b3a22"/>
      <rect x="${x+74}" y="162" width="16" height="80" fill="url(#rideauHd)"/>
      <rect x="${x}" y="206" width="74" height="26" fill="#f4efe2" stroke="#b9a77c"/>
      <rect x="${x}" y="232" width="74" height="10" fill="#5b3a22"/>
    </g>`).join("")}
  <!-- corbeille de pains, au premier plan -->
  <ellipse cx="400" cy="276" rx="46" ry="12" fill="#6d4c2f"/>
  <g fill="#d89b4a">
    <ellipse cx="384" cy="268" rx="14" ry="8"/><ellipse cx="410" cy="266" rx="14" ry="8"/><ellipse cx="398" cy="260" rx="13" ry="7"/>
  </g>
  <!-- vapeur du bouillon -->
  <g fill="none" stroke="#fff" stroke-width="2" opacity=".5">
    <path d="M520 260 q6 -10 0 -20 q-6 -10 0 -20"><animate attributeName="opacity" values=".5;0;.5" dur="4s" repeatCount="indefinite"/></path>
  </g>
  <rect x="506" y="258" width="28" height="18" rx="4" fill="#6f5a3e"/>
</svg>`,

/* ------------------------------------------------------------
   PAGE 5 — Le chantier : église romane (gauche), cathédrale gothique (droite)
   ------------------------------------------------------------ */
"chantier": `${SVG_OUVERT}
  <defs>
    <linearGradient id="cielCh" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#8db3dd"/><stop offset="100%" stop-color="#e6eef6"/></linearGradient>
    <linearGradient id="pierreRo" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d9c9a8"/><stop offset="100%" stop-color="#a8966f"/></linearGradient>
    <linearGradient id="pierreGo" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#ece3cf"/><stop offset="100%" stop-color="#bfb193"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielCh)"/>
  <g opacity=".55"><ellipse cx="300" cy="40" rx="60" ry="14" fill="#fff"><animate attributeName="cx" values="260;720;260" dur="110s" repeatCount="indefinite"/></ellipse></g>
  <!-- ÉGLISE ROMANE : trapue, murs épais, petites fenêtres rondes -->
  <rect x="40" y="140" width="250" height="110" fill="url(#pierreRo)"/>
  <polygon points="40,140 165,96 290,140" fill="#8e5a3c"/>
  <rect x="140" y="70" width="50" height="70" fill="url(#pierreRo)"/>
  <polygon points="140,70 165,48 190,70" fill="#8e5a3c"/>
  <rect x="157" y="84" width="16" height="22" rx="8" fill="#3d3024"/>
  <g fill="#3d3024">${[62,112,202,250].map(x=>`<rect x="${x}" y="168" width="14" height="24" rx="7"/>`).join("")}</g>
  <path d="M146 250 L146 214 A19 19 0 0 1 184 214 L184 250 Z" fill="#4a3825"/>
  <!-- contreforts collés au mur -->
  <g fill="#9c8a64">${[40,95,224,278].map(x=>`<rect x="${x}" y="150" width="12" height="100"/>`).join("")}</g>
  <!-- CATHÉDRALE GOTHIQUE : haute, arcs brisés, rosace, arcs-boutants -->
  <rect x="470" y="96" width="220" height="154" fill="url(#pierreGo)"/>
  <polygon points="470,96 580,40 690,96" fill="#bfb193"/>
  <g fill="#7fa8d6" stroke="#4a3825" stroke-width="2">
    ${[488,540,600,652].map(x=>`<path d="M${x} 232 L${x} 150 Q${x} 128 ${x+15} 118 Q${x+30} 128 ${x+30} 150 L${x+30} 232 Z"/>`).join("")}
  </g>
  <circle cx="580" cy="92" r="20" fill="#7fa8d6" stroke="#4a3825" stroke-width="3"/>
  <path d="M580 72 V112 M560 92 H600 M566 78 L594 106 M594 78 L566 106" stroke="#4a3825" stroke-width="1.6"/>
  <!-- arcs-boutants -->
  <g fill="none" stroke="#a89878" stroke-width="7">
    <path d="M470 130 Q440 136 430 176"/><path d="M690 130 Q720 136 730 176"/>
  </g>
  <rect x="420" y="176" width="20" height="74" fill="#a89878"/><rect x="720" y="176" width="20" height="74" fill="#a89878"/>
  <!-- échafaudage à droite -->
  <g stroke="#6d4c2f" stroke-width="3">
    <line x1="700" y1="40" x2="700" y2="250"/><line x1="760" y1="40" x2="760" y2="250"/>
    <line x1="700" y1="90" x2="760" y2="90"/><line x1="700" y1="150" x2="760" y2="150"/><line x1="700" y1="210" x2="760" y2="210"/>
  </g>
  <!-- poulie et pierre qui monte -->
  <line x1="700" y1="44" x2="780" y2="44" stroke="#6d4c2f" stroke-width="4"/>
  <circle cx="776" cy="50" r="6" fill="#6d4c2f"/>
  <g>
    <line x1="776" y1="56" x2="776" y2="200" stroke="#4a3825" stroke-width="1.5"/>
    <rect x="766" y="200" width="20" height="14" fill="#d9c9a8" stroke="#8a7a5c"/>
    <animateTransform attributeName="transform" type="translate" values="0 0;0 -90;0 -90;0 0" dur="10s" repeatCount="indefinite"/>
  </g>
  <!-- sol du chantier, blocs de pierre -->
  <rect y="250" width="800" height="50" fill="#b4a27d"/>
  <g fill="#d9c9a8" stroke="#8a7a5c">
    <rect x="330" y="258" width="34" height="20"/><rect x="368" y="262" width="30" height="16"/><rect x="346" y="242" width="30" height="16"/>
  </g>
  <!-- repères écrits, pour ne pas s'appuyer sur la seule couleur -->
  <g font-family="system-ui,sans-serif" font-size="13" font-weight="bold" fill="#2b1d10">
    <text x="165" y="282" text-anchor="middle">ROMAN</text>
    <text x="580" y="282" text-anchor="middle">GOTHIQUE</text>
  </g>
</svg>`
};

window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
