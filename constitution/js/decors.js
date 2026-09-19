/* ============================================================
   DÉCORS SVG ANIMÉS — 5 lieux de la République
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (zéro attente, zéro fichier).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.png
     →  SVG    dessiné ci-dessous

   Les cinq lieux sont réels :
     cour       la cour intérieure du Palais-Royal, à Paris
     archives   une salle de consultation des textes
     hemicycle  l'hémicycle de l'Assemblée nationale (Palais-Bourbon)
     senat      le palais du Luxembourg, siège du Sénat
     conseil    la salle des séances du Conseil constitutionnel
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["cour"];
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

const SALLE_NUM = { "cour":1, "archives":2, "hemicycle":3, "senat":4, "conseil":5 };

/* ---- Fragments communs ---- */
const CIEL_JOUR = `
  <linearGradient id="cielJour" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#7fa8d6"/><stop offset="60%" stop-color="#bcd3e8"/><stop offset="100%" stop-color="#e3ecf4"/>
  </linearGradient>`;

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — La cour du Palais-Royal (colonnes, galeries, jets d'eau)
   ------------------------------------------------------------ */
"cour": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_JOUR}
    <linearGradient id="pierreC" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e8e0d0"/><stop offset="100%" stop-color="#c4b79e"/>
    </linearGradient>
    <linearGradient id="solC" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#b9ae9a"/><stop offset="100%" stop-color="#8e8472"/>
    </linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielJour)"/>
  <!-- nuages lents -->
  <g opacity=".55">
    <ellipse cx="140" cy="46" rx="60" ry="16" fill="#fff"><animate attributeName="cx" values="120;700;120" dur="90s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="520" cy="34" rx="44" ry="12" fill="#fff"><animate attributeName="cx" values="500;-80;500" dur="120s" repeatCount="indefinite"/></ellipse>
  </g>
  <!-- aile de gauche -->
  <rect x="0" y="60" width="210" height="180" fill="url(#pierreC)"/>
  <g>
    <rect x="16" y="96" width="30" height="52" rx="14" fill="#5d6b7a" opacity=".8"/>
    <rect x="68" y="96" width="30" height="52" rx="14" fill="#5d6b7a" opacity=".8"/>
    <rect x="120" y="96" width="30" height="52" rx="14" fill="#5d6b7a" opacity=".8"/>
    <rect x="172" y="96" width="30" height="52" rx="14" fill="#5d6b7a" opacity=".8"/>
  </g>
  <!-- bâtiment du fond : le Conseil constitutionnel -->
  <rect x="210" y="40" width="380" height="200" fill="url(#pierreC)"/>
  <polygon points="210,40 400,6 590,40" fill="#d8cfbc"/>
  <rect x="210" y="36" width="380" height="8" fill="#b6a88e"/>
  <g>
    <rect x="240" y="82" width="34" height="62" rx="16" fill="#4f5d6c" opacity=".85"/>
    <rect x="300" y="82" width="34" height="62" rx="16" fill="#4f5d6c" opacity=".85"/>
    <rect x="360" y="82" width="34" height="62" rx="16" fill="#4f5d6c" opacity=".85"/>
    <rect x="420" y="82" width="34" height="62" rx="16" fill="#4f5d6c" opacity=".85"/>
    <rect x="480" y="82" width="34" height="62" rx="16" fill="#4f5d6c" opacity=".85"/>
    <rect x="540" y="82" width="34" height="62" rx="16" fill="#4f5d6c" opacity=".85"/>
  </g>
  <!-- colonnes du péristyle -->
  <g fill="#efe8da">
    <rect x="246" y="150" width="16" height="90"/><rect x="306" y="150" width="16" height="90"/>
    <rect x="366" y="150" width="16" height="90"/><rect x="426" y="150" width="16" height="90"/>
    <rect x="486" y="150" width="16" height="90"/><rect x="546" y="150" width="16" height="90"/>
  </g>
  <!-- drapeau tricolore -->
  <g transform="translate(398,10)">
    <rect x="-1" y="0" width="3" height="40" fill="#6b6152"/>
    <g>
      <rect x="2" y="2" width="14" height="22" fill="#0055a4"/>
      <rect x="16" y="2" width="14" height="22" fill="#f4f4f4"/>
      <rect x="30" y="2" width="14" height="22" fill="#ef4135"/>
      <animateTransform attributeName="transform" type="skewY" values="0;3;0;-3;0" dur="5s" repeatCount="indefinite"/>
    </g>
  </g>
  <!-- aile de droite -->
  <rect x="590" y="60" width="210" height="180" fill="url(#pierreC)"/>
  <g>
    <rect x="612" y="96" width="30" height="52" rx="14" fill="#5d6b7a" opacity=".8"/>
    <rect x="664" y="96" width="30" height="52" rx="14" fill="#5d6b7a" opacity=".8"/>
    <rect x="716" y="96" width="30" height="52" rx="14" fill="#5d6b7a" opacity=".8"/>
    <rect x="762" y="96" width="30" height="52" rx="14" fill="#5d6b7a" opacity=".8"/>
  </g>
  <!-- sol de la cour -->
  <rect x="0" y="240" width="800" height="60" fill="url(#solC)"/>
  <g stroke="#7d7462" stroke-width="1" opacity=".5">
    <line x1="0" y1="256" x2="800" y2="256"/><line x1="0" y1="274" x2="800" y2="274"/>
    <line x1="100" y1="240" x2="70" y2="300"/><line x1="260" y1="240" x2="240" y2="300"/>
    <line x1="420" y1="240" x2="420" y2="300"/><line x1="580" y1="240" x2="600" y2="300"/>
    <line x1="720" y1="240" x2="750" y2="300"/>
  </g>
  <!-- colonnes rayées de la cour d'honneur -->
  <g>
    <g transform="translate(150,206)"><rect width="18" height="40" fill="#f2f2f2"/><rect y="6" width="18" height="6" fill="#222"/><rect y="20" width="18" height="6" fill="#222"/><rect y="34" width="18" height="6" fill="#222"/></g>
    <g transform="translate(196,214)"><rect width="16" height="32" fill="#f2f2f2"/><rect y="5" width="16" height="5" fill="#222"/><rect y="17" width="16" height="5" fill="#222"/></g>
    <g transform="translate(620,210)"><rect width="18" height="36" fill="#f2f2f2"/><rect y="6" width="18" height="6" fill="#222"/><rect y="20" width="18" height="6" fill="#222"/></g>
    <g transform="translate(664,218)"><rect width="14" height="28" fill="#f2f2f2"/><rect y="5" width="14" height="5" fill="#222"/><rect y="16" width="14" height="5" fill="#222"/></g>
  </g>
  <!-- le coffre scellé, au centre -->
  <g transform="translate(372,214)">
    <rect x="0" y="6" width="58" height="30" rx="3" fill="#6b4a2a"/>
    <path d="M0 8 Q29 -6 58 8 Z" fill="#7d5730"/>
    <rect x="-2" y="18" width="62" height="5" fill="#c9a227"/>
    <rect x="24" y="14" width="10" height="14" rx="2" fill="#c9a227"/>
    <circle cx="29" cy="21" r="2.4" fill="#5b4520"/>
    <circle cx="29" cy="4" r="5" fill="#b22222" opacity=".9"><animate attributeName="opacity" values=".55;1;.55" dur="3.5s" repeatCount="indefinite"/></circle>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — La salle des Textes (rayonnages, vitrines, poussière)
   ------------------------------------------------------------ */
"archives": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murA" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4a3a2a"/><stop offset="100%" stop-color="#2b2118"/>
    </linearGradient>
    <radialGradient id="lampeA" cx="50%" cy="0%" r="90%">
      <stop offset="0%" stop-color="#ffe6a8" stop-opacity=".85"/><stop offset="100%" stop-color="#ffe6a8" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murA)"/>
  <!-- rayonnages -->
  <g>
    <rect x="20" y="40" width="230" height="230" fill="#3a2c1f"/>
    <rect x="550" y="40" width="230" height="230" fill="#3a2c1f"/>
    <g fill="#241a12">
      <rect x="24" y="92" width="222" height="7"/><rect x="24" y="150" width="222" height="7"/><rect x="24" y="208" width="222" height="7"/>
      <rect x="554" y="92" width="222" height="7"/><rect x="554" y="150" width="222" height="7"/><rect x="554" y="208" width="222" height="7"/>
    </g>
    <g>
      <rect x="32" y="56" width="12" height="36" fill="#8d3b2f"/><rect x="46" y="60" width="10" height="32" fill="#2f5d8d"/>
      <rect x="58" y="54" width="14" height="38" fill="#c9a227"/><rect x="74" y="62" width="9" height="30" fill="#4a7c59"/>
      <rect x="86" y="58" width="13" height="34" fill="#6b3f8d"/><rect x="102" y="64" width="10" height="28" fill="#8d3b2f"/>
      <rect x="120" y="56" width="12" height="36" fill="#2f5d8d"/><rect x="136" y="60" width="11" height="32" fill="#c9a227"/>
      <rect x="152" y="54" width="13" height="38" fill="#4a7c59"/><rect x="170" y="62" width="10" height="30" fill="#8d3b2f"/>
      <rect x="186" y="58" width="12" height="34" fill="#6b3f8d"/><rect x="204" y="56" width="14" height="36" fill="#2f5d8d"/>
      <rect x="222" y="62" width="10" height="30" fill="#c9a227"/>
      <rect x="32" y="114" width="12" height="36" fill="#4a7c59"/><rect x="48" y="118" width="11" height="32" fill="#8d3b2f"/>
      <rect x="62" y="112" width="13" height="38" fill="#2f5d8d"/><rect x="80" y="120" width="10" height="30" fill="#c9a227"/>
      <rect x="96" y="116" width="12" height="34" fill="#6b3f8d"/><rect x="114" y="114" width="14" height="36" fill="#4a7c59"/>
      <rect x="134" y="120" width="10" height="30" fill="#8d3b2f"/><rect x="150" y="114" width="12" height="36" fill="#2f5d8d"/>
      <rect x="168" y="118" width="11" height="32" fill="#c9a227"/><rect x="184" y="112" width="13" height="38" fill="#6b3f8d"/>
      <rect x="204" y="120" width="10" height="30" fill="#4a7c59"/><rect x="220" y="116" width="12" height="34" fill="#8d3b2f"/>
      <rect x="562" y="56" width="12" height="36" fill="#2f5d8d"/><rect x="578" y="60" width="11" height="32" fill="#c9a227"/>
      <rect x="592" y="54" width="13" height="38" fill="#8d3b2f"/><rect x="610" y="62" width="10" height="30" fill="#4a7c59"/>
      <rect x="626" y="58" width="12" height="34" fill="#6b3f8d"/><rect x="644" y="56" width="14" height="36" fill="#2f5d8d"/>
      <rect x="664" y="62" width="10" height="30" fill="#c9a227"/><rect x="680" y="54" width="13" height="38" fill="#8d3b2f"/>
      <rect x="698" y="60" width="11" height="32" fill="#4a7c59"/><rect x="714" y="58" width="12" height="34" fill="#6b3f8d"/>
      <rect x="732" y="56" width="14" height="36" fill="#2f5d8d"/><rect x="752" y="62" width="10" height="30" fill="#c9a227"/>
      <rect x="562" y="114" width="12" height="36" fill="#c9a227"/><rect x="578" y="118" width="11" height="32" fill="#6b3f8d"/>
      <rect x="594" y="112" width="13" height="38" fill="#4a7c59"/><rect x="612" y="120" width="10" height="30" fill="#2f5d8d"/>
      <rect x="628" y="116" width="12" height="34" fill="#8d3b2f"/><rect x="646" y="114" width="14" height="36" fill="#c9a227"/>
      <rect x="666" y="120" width="10" height="30" fill="#6b3f8d"/><rect x="682" y="114" width="12" height="36" fill="#4a7c59"/>
      <rect x="700" y="118" width="11" height="32" fill="#2f5d8d"/><rect x="716" y="112" width="13" height="38" fill="#8d3b2f"/>
      <rect x="736" y="120" width="10" height="30" fill="#c9a227"/><rect x="752" y="116" width="12" height="34" fill="#6b3f8d"/>
    </g>
  </g>
  <!-- vitrine centrale : les quatre textes -->
  <rect x="280" y="70" width="240" height="150" rx="6" fill="#1d1710" stroke="#c9a227" stroke-width="3"/>
  <rect x="288" y="78" width="224" height="134" fill="#f4ecd8" opacity=".12"/>
  <g transform="translate(300,92)">
    <g><rect width="44" height="56" rx="2" fill="#f0e6cd"/><rect x="5" y="8" width="34" height="2.5" fill="#8a7a5c"/><rect x="5" y="16" width="34" height="2.5" fill="#8a7a5c"/><rect x="5" y="24" width="26" height="2.5" fill="#8a7a5c"/><text x="22" y="48" font-size="9" text-anchor="middle" fill="#6b4a2a" font-family="Georgia,serif">1789</text></g>
    <g transform="translate(56,0)"><rect width="44" height="56" rx="2" fill="#f0e6cd"/><rect x="5" y="8" width="34" height="2.5" fill="#8a7a5c"/><rect x="5" y="16" width="34" height="2.5" fill="#8a7a5c"/><rect x="5" y="24" width="30" height="2.5" fill="#8a7a5c"/><text x="22" y="48" font-size="9" text-anchor="middle" fill="#6b4a2a" font-family="Georgia,serif">1946</text></g>
    <g transform="translate(112,0)"><rect width="44" height="56" rx="2" fill="#f6efdd"/><rect x="5" y="8" width="34" height="2.5" fill="#8a7a5c"/><rect x="5" y="16" width="34" height="2.5" fill="#8a7a5c"/><rect x="5" y="24" width="24" height="2.5" fill="#8a7a5c"/><text x="22" y="48" font-size="9" text-anchor="middle" fill="#b22222" font-family="Georgia,serif">1958</text></g>
    <g transform="translate(168,0)"><rect width="44" height="56" rx="2" fill="#e6f0dd"/><rect x="5" y="8" width="34" height="2.5" fill="#6d8a5c"/><rect x="5" y="16" width="34" height="2.5" fill="#6d8a5c"/><rect x="5" y="24" width="28" height="2.5" fill="#6d8a5c"/><text x="22" y="48" font-size="9" text-anchor="middle" fill="#3d6b2a" font-family="Georgia,serif">2004</text></g>
  </g>
  <text x="400" y="200" font-size="11" text-anchor="middle" fill="#c9a227" font-family="Georgia,serif" letter-spacing="2">BLOC DE CONSTITUTIONNALITÉ</text>
  <!-- halo de la lampe -->
  <ellipse cx="400" cy="30" rx="300" ry="150" fill="url(#lampeA)">
    <animate attributeName="ry" values="150;158;150" dur="7s" repeatCount="indefinite"/>
  </ellipse>
  <!-- poussière en suspension -->
  <g fill="#ffeec2" opacity=".5">
    <circle cx="180" cy="120" r="1.6"><animate attributeName="cy" values="120;60;120" dur="14s" repeatCount="indefinite"/></circle>
    <circle cx="350" cy="230" r="1.2"><animate attributeName="cy" values="230;150;230" dur="18s" repeatCount="indefinite"/></circle>
    <circle cx="520" cy="180" r="1.8"><animate attributeName="cy" values="180;90;180" dur="16s" repeatCount="indefinite"/></circle>
    <circle cx="640" cy="240" r="1.3"><animate attributeName="cy" values="240;160;240" dur="20s" repeatCount="indefinite"/></circle>
  </g>
  <rect x="0" y="262" width="800" height="38" fill="#241a12"/>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — L'hémicycle de l'Assemblée nationale
   ------------------------------------------------------------ */
"hemicycle": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <radialGradient id="voute" cx="50%" cy="8%" r="80%">
      <stop offset="0%" stop-color="#f3e4c0"/><stop offset="100%" stop-color="#b79a6c"/>
    </radialGradient>
    <linearGradient id="gradinsH" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8e4b3a"/><stop offset="100%" stop-color="#5e2f24"/>
    </linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#voute)"/>
  <!-- coupole -->
  <g opacity=".35" stroke="#8a7346" fill="none" stroke-width="2">
    <path d="M60 110 Q400 -60 740 110"/><path d="M130 110 Q400 -20 670 110"/><path d="M210 110 Q400 12 590 110"/>
    <line x1="400" y1="0" x2="400" y2="110"/><line x1="250" y1="26" x2="300" y2="110"/><line x1="550" y1="26" x2="500" y2="110"/>
  </g>
  <!-- tenture et tribune -->
  <rect x="300" y="96" width="200" height="86" rx="4" fill="#3c2a1e"/>
  <rect x="312" y="106" width="176" height="66" fill="#6b1f1f"/>
  <g transform="translate(400,140)">
    <circle r="22" fill="#e8dcc0" opacity=".9"/>
    <text y="5" font-size="16" text-anchor="middle" fill="#6b1f1f" font-family="Georgia,serif">RF</text>
  </g>
  <!-- perchoir -->
  <rect x="356" y="182" width="88" height="34" rx="3" fill="#7b4a2c"/>
  <rect x="368" y="176" width="64" height="10" rx="2" fill="#a06a3f"/>
  <!-- gradins en arc -->
  <g>
    <path d="M40 300 Q400 150 760 300 Z" fill="url(#gradinsH)"/>
    <g stroke="#3f1f18" stroke-width="2" fill="none" opacity=".7">
      <path d="M70 300 Q400 176 730 300"/><path d="M110 300 Q400 200 690 300"/>
      <path d="M155 300 Q400 224 645 300"/><path d="M205 300 Q400 248 595 300"/>
    </g>
  </g>
  <!-- pupitres et députés stylisés -->
  <g fill="#2c2c34">
    <circle cx="150" cy="268" r="7"/><circle cx="196" cy="256" r="7"/><circle cx="244" cy="246" r="7"/>
    <circle cx="296" cy="238" r="7"/><circle cx="350" cy="232" r="7"/><circle cx="400" cy="230" r="7"/>
    <circle cx="450" cy="232" r="7"/><circle cx="504" cy="238" r="7"/><circle cx="556" cy="246" r="7"/>
    <circle cx="604" cy="256" r="7"/><circle cx="650" cy="268" r="7"/>
  </g>
  <g fill="#e2d6bd" opacity=".9">
    <rect x="132" y="276" width="36" height="6" rx="2"/><rect x="178" y="264" width="36" height="6" rx="2"/>
    <rect x="226" y="254" width="36" height="6" rx="2"/><rect x="278" y="246" width="36" height="6" rx="2"/>
    <rect x="332" y="240" width="36" height="6" rx="2"/><rect x="382" y="238" width="36" height="6" rx="2"/>
    <rect x="432" y="240" width="36" height="6" rx="2"/><rect x="486" y="246" width="36" height="6" rx="2"/>
    <rect x="538" y="254" width="36" height="6" rx="2"/><rect x="586" y="264" width="36" height="6" rx="2"/>
    <rect x="632" y="276" width="36" height="6" rx="2"/>
  </g>
  <!-- tableau de vote clignotant -->
  <g transform="translate(628,96)">
    <rect width="140" height="52" rx="4" fill="#15181f" stroke="#c9a227" stroke-width="2"/>
    <text x="70" y="18" font-size="10" text-anchor="middle" fill="#c9a227" font-family="Georgia,serif">SCRUTIN</text>
    <circle cx="34" cy="34" r="8" fill="#2e7d32"><animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/></circle>
    <circle cx="70" cy="34" r="8" fill="#c9a227" opacity=".4"/>
    <circle cx="106" cy="34" r="8" fill="#b22222"><animate attributeName="opacity" values=".35;1;.35" dur="2.4s" repeatCount="indefinite"/></circle>
  </g>
  <!-- horloge -->
  <g transform="translate(60,110)">
    <circle r="24" fill="#efe6cf" stroke="#8a7346" stroke-width="3"/>
    <line x1="0" y1="0" x2="0" y2="-15" stroke="#333" stroke-width="2.4">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="60s" repeatCount="indefinite"/>
    </line>
    <line x1="0" y1="0" x2="10" y2="0" stroke="#333" stroke-width="2">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="720s" repeatCount="indefinite"/>
    </line>
    <circle r="2.4" fill="#333"/>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — Le palais du Luxembourg, siège du Sénat, et la navette
   ------------------------------------------------------------ */
"senat": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_JOUR}
    <linearGradient id="pierreS" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ece3d0"/><stop offset="100%" stop-color="#bdb096"/>
    </linearGradient>
    <linearGradient id="pelouse" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#6f9152"/><stop offset="100%" stop-color="#4d6b38"/>
    </linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielJour)"/>
  <g opacity=".5">
    <ellipse cx="220" cy="38" rx="52" ry="13" fill="#fff"><animate attributeName="cx" values="200;760;200" dur="110s" repeatCount="indefinite"/></ellipse>
  </g>
  <!-- Palais-Bourbon (à gauche) : l'Assemblée nationale -->
  <g>
    <rect x="30" y="112" width="220" height="110" fill="url(#pierreS)"/>
    <polygon points="30,112 140,72 250,112" fill="#ddd3bd"/>
    <g fill="#efe8da">
      <rect x="48" y="128" width="12" height="94"/><rect x="82" y="128" width="12" height="94"/>
      <rect x="116" y="128" width="12" height="94"/><rect x="150" y="128" width="12" height="94"/>
      <rect x="184" y="128" width="12" height="94"/><rect x="218" y="128" width="12" height="94"/>
    </g>
    <text x="140" y="240" font-size="12" text-anchor="middle" fill="#3b3527" font-family="Georgia,serif">ASSEMBLÉE NATIONALE</text>
  </g>
  <!-- Palais du Luxembourg (à droite) : le Sénat -->
  <g>
    <rect x="550" y="108" width="220" height="114" fill="url(#pierreS)"/>
    <rect x="600" y="76" width="120" height="34" fill="#e2d9c4"/>
    <polygon points="600,76 660,50 720,76" fill="#cfc5ad"/>
    <g fill="#5d6b7a" opacity=".8">
      <rect x="570" y="132" width="24" height="44" rx="11"/><rect x="612" y="132" width="24" height="44" rx="11"/>
      <rect x="654" y="132" width="24" height="44" rx="11"/><rect x="696" y="132" width="24" height="44" rx="11"/>
      <rect x="734" y="132" width="24" height="44" rx="11"/>
    </g>
    <text x="660" y="240" font-size="12" text-anchor="middle" fill="#3b3527" font-family="Georgia,serif">SÉNAT</text>
  </g>
  <!-- la navette parlementaire : un texte qui fait l'aller-retour -->
  <g>
    <line x1="260" y1="176" x2="540" y2="176" stroke="#8a7346" stroke-width="2" stroke-dasharray="6 6" opacity=".7"/>
    <g>
      <rect x="-16" y="-11" width="32" height="22" rx="2" fill="#f6efdd" stroke="#b6a88e"/>
      <rect x="-10" y="-5" width="20" height="2" fill="#9a8a6a"/><rect x="-10" y="0" width="20" height="2" fill="#9a8a6a"/><rect x="-10" y="5" width="14" height="2" fill="#9a8a6a"/>
      <animateMotion dur="9s" repeatCount="indefinite" keyPoints="0;1;0" keyTimes="0;0.5;1" calcMode="linear"
        path="M270,176 L530,176"/>
    </g>
  </g>
  <!-- jardin et bassin -->
  <rect x="0" y="222" width="800" height="78" fill="url(#pelouse)"/>
  <ellipse cx="400" cy="264" rx="120" ry="26" fill="#7fa8c6"/>
  <ellipse cx="400" cy="264" rx="120" ry="26" fill="none" stroke="#c9bfa4" stroke-width="5"/>
  <g stroke="#e8f2f8" stroke-width="1.5" fill="none" opacity=".7">
    <ellipse cx="400" cy="264" rx="40" ry="9"><animate attributeName="rx" values="12;96;12" dur="6s" repeatCount="indefinite"/><animate attributeName="ry" values="3;21;3" dur="6s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0;.8" dur="6s" repeatCount="indefinite"/></ellipse>
  </g>
  <!-- arbres taillés -->
  <g>
    <g transform="translate(120,232)"><rect x="-3" y="0" width="6" height="26" fill="#5b4327"/><ellipse cy="-12" rx="22" ry="20" fill="#5f8347"/></g>
    <g transform="translate(220,240)"><rect x="-3" y="0" width="6" height="22" fill="#5b4327"/><ellipse cy="-10" rx="18" ry="16" fill="#54793e"/></g>
    <g transform="translate(600,238)"><rect x="-3" y="0" width="6" height="24" fill="#5b4327"/><ellipse cy="-11" rx="20" ry="18" fill="#5f8347"/></g>
    <g transform="translate(700,232)"><rect x="-3" y="0" width="6" height="26" fill="#5b4327"/><ellipse cy="-12" rx="22" ry="20" fill="#54793e"/></g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — La salle des séances du Conseil constitutionnel
   ------------------------------------------------------------ */
"conseil": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murCC" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2b3550"/><stop offset="100%" stop-color="#141b2c"/>
    </linearGradient>
    <linearGradient id="tapisCC" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#7a1f24"/><stop offset="100%" stop-color="#4c1216"/>
    </linearGradient>
    <radialGradient id="lustre" cx="50%" cy="0%" r="70%">
      <stop offset="0%" stop-color="#ffe9b0" stop-opacity=".7"/><stop offset="100%" stop-color="#ffe9b0" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murCC)"/>
  <!-- boiseries -->
  <g fill="none" stroke="#c9a227" stroke-width="2" opacity=".45">
    <rect x="40" y="46" width="130" height="150" rx="4"/><rect x="630" y="46" width="130" height="150" rx="4"/>
    <rect x="200" y="34" width="400" height="120" rx="6"/>
  </g>
  <!-- devise gravée -->
  <text x="400" y="80" font-size="15" text-anchor="middle" fill="#e6d3a0" font-family="Georgia,serif" letter-spacing="3">LIBERTÉ · ÉGALITÉ · FRATERNITÉ</text>
  <text x="400" y="110" font-size="10" text-anchor="middle" fill="#9fb0cf" font-family="Georgia,serif" letter-spacing="2">CONSEIL CONSTITUTIONNEL</text>
  <!-- les neuf sièges des Sages -->
  <g>
    <g fill="#8a2a2f" stroke="#c9a227" stroke-width="1.5">
      <rect x="196" y="128" width="26" height="30" rx="4"/><rect x="240" y="126" width="26" height="32" rx="4"/>
      <rect x="284" y="124" width="26" height="34" rx="4"/><rect x="328" y="122" width="26" height="36" rx="4"/>
      <rect x="374" y="120" width="28" height="38" rx="4"/>
      <rect x="422" y="122" width="26" height="36" rx="4"/><rect x="466" y="124" width="26" height="34" rx="4"/>
      <rect x="510" y="126" width="26" height="32" rx="4"/><rect x="554" y="128" width="26" height="30" rx="4"/>
    </g>
    <g fill="#e9dfc6" opacity=".85">
      <circle cx="209" cy="124" r="6"/><circle cx="253" cy="121" r="6"/><circle cx="297" cy="119" r="6"/>
      <circle cx="341" cy="117" r="6"/><circle cx="388" cy="114" r="7"/><circle cx="435" cy="117" r="6"/>
      <circle cx="479" cy="119" r="6"/><circle cx="523" cy="121" r="6"/><circle cx="567" cy="124" r="6"/>
    </g>
  </g>
  <!-- table en fer à cheval -->
  <path d="M170 176 Q400 146 630 176 L630 204 Q400 176 170 204 Z" fill="#4a2f22" stroke="#c9a227" stroke-width="2"/>
  <!-- dossiers posés -->
  <g fill="#f2ead6">
    <rect x="236" y="176" width="22" height="14" rx="1" transform="rotate(-3 247 183)"/>
    <rect x="382" y="170" width="26" height="15" rx="1"/>
    <rect x="520" y="176" width="22" height="14" rx="1" transform="rotate(3 531 183)"/>
  </g>
  <!-- tapis -->
  <rect x="0" y="212" width="800" height="88" fill="url(#tapisCC)"/>
  <g stroke="#c9a227" stroke-width="2" fill="none" opacity=".35">
    <rect x="24" y="226" width="752" height="60" rx="6"/>
  </g>
  <!-- pupitre du rapporteur -->
  <g transform="translate(360,214)">
    <rect width="80" height="46" rx="3" fill="#5c3a28" stroke="#c9a227"/>
    <rect x="12" y="10" width="56" height="4" fill="#e9dfc6"/><rect x="12" y="20" width="44" height="4" fill="#e9dfc6"/>
    <rect x="12" y="30" width="50" height="4" fill="#e9dfc6"/>
  </g>
  <!-- balance de la justice -->
  <g transform="translate(700,200)" opacity=".9">
    <line x1="0" y1="-40" x2="0" y2="14" stroke="#c9a227" stroke-width="3"/>
    <g>
      <line x1="-26" y1="-36" x2="26" y2="-36" stroke="#c9a227" stroke-width="3"/>
      <path d="M-26 -36 L-34 -22 L-18 -22 Z" fill="#c9a227"/>
      <path d="M26 -36 L18 -22 L34 -22 Z" fill="#c9a227"/>
      <animateTransform attributeName="transform" type="rotate" values="-3;3;-3" dur="6s" repeatCount="indefinite"/>
    </g>
    <ellipse cy="16" rx="18" ry="5" fill="#c9a227"/>
  </g>
  <!-- lustre -->
  <ellipse cx="400" cy="10" rx="280" ry="130" fill="url(#lustre)">
    <animate attributeName="opacity" values=".85;1;.85" dur="6s" repeatCount="indefinite"/>
  </ellipse>
</svg>`
};

window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
