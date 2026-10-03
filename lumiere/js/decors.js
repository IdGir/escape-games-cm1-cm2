/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de « Le Phare de l'île Lumière »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux (le phare de l'île Lumière, île imaginaire, à la tombée de la nuit) :
     lanterne   la lanterne, tout en haut du phare (grosse lampe éteinte, lentille)
     atelier    l'atelier des vitres (banc d'essai : vitre, calque, bois)
     chambre    la chambre aux ombres (théâtre d'ombres de Nils)
     cour       la cour du cadran solaire (bâton et ombre qui tourne)
     galerie    la galerie extérieure (Lune, nuages, La Mouette au loin)
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["galerie"];
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

const SALLE_NUM = { "lanterne":1, "atelier":2, "chambre":3, "cour":4, "galerie":5 };

/* ---- Fragments communs ---- */
const CIEL_NUIT = (id) => `
  <linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0f1a2b"/><stop offset="60%" stop-color="#22385a"/><stop offset="100%" stop-color="#3f5f86"/>
  </linearGradient>`;
/* Étoiles qui scintillent (positions fixes, durées variées) */
const ETOILES = (n=26, hmax=150) => `<g fill="#fdf6d8">${Array.from({length:n},(_,i)=>{
  const x = (i*97 + 31) % 800, y = (i*53 + 17) % hmax, r = 0.8 + (i%3)*0.5;
  return `<circle cx="${x}" cy="${y}" r="${r}"><animate attributeName="opacity" values="1;.25;1" dur="${2.5+(i%5)*0.7}s" repeatCount="indefinite"/></circle>`;
}).join("")}</g>`;
/* Vagues animées (y : hauteur de la ligne d'eau) */
const VAGUES = (y, couleur="#5d8bb8", dur="7s") => `<path d="M-40 ${y} q20 -6 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0" stroke="${couleur}" stroke-width="2" fill="none" opacity=".8">
  <animateTransform attributeName="transform" type="translate" values="0 0;40 0;0 0" dur="${dur}" repeatCount="indefinite"/></path>`;
/* Un voilier (x, y, échelle) avec son feu qui clignote */
const VOILIER = (x, y, k=1, feu=true) => `<g transform="translate(${x},${y}) scale(${k})">
  <path d="M-30 0 L30 0 L22 12 L-22 12 Z" fill="#6b4a2b"/>
  <line x1="0" y1="0" x2="0" y2="-58" stroke="#222" stroke-width="2"/>
  <polygon points="2,-54 2,-4 34,-4" fill="#eceee8"/><polygon points="-2,-46 -2,-4 -24,-4" fill="#d9dccf"/>
  ${feu?`<circle cx="0" cy="-60" r="3.5" fill="#ffd23f"><animate attributeName="opacity" values="1;1;0;0;1;0;1" dur="2.2s" repeatCount="indefinite"/></circle>`:""}
</g>`;

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — La lanterne du phare
   ------------------------------------------------------------ */
"lanterne": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_NUIT("cielL")}
    <radialGradient id="lueurL" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#ffe9a0" stop-opacity=".55"/><stop offset="100%" stop-color="#ffe9a0" stop-opacity="0"/></radialGradient>
    <linearGradient id="verreL" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#cfe6f5" stop-opacity=".35"/><stop offset="50%" stop-color="#ffffff" stop-opacity=".12"/><stop offset="100%" stop-color="#cfe6f5" stop-opacity=".35"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielL)"/>
  ${ETOILES(30, 120)}
  <!-- la mer derrière les vitres -->
  <rect y="170" width="800" height="130" fill="#1b3553"/>
  ${VAGUES(184, "#4f79a4", "8s")}${VAGUES(204, "#416a95", "10s")}
  <g>${VOILIER(640, 182, .8)}<animateTransform attributeName="transform" type="translate" values="0 0;-60 2;0 0" dur="40s" repeatCount="indefinite"/></g>
  <!-- montants de la lanterne (vitres) -->
  <rect x="0" y="40" width="800" height="200" fill="url(#verreL)"/>
  <g fill="#2a2f38">${[0,1,2,3,4,5,6,7,8].map(i=>`<rect x="${i*100-6}" y="30" width="12" height="220"/>`).join("")}</g>
  <rect x="0" y="22" width="800" height="18" fill="#2a2f38"/><rect x="0" y="240" width="800" height="60" fill="#3a3f48"/>
  <rect x="0" y="240" width="800" height="6" fill="#5a606b"/>
  <!-- la grosse lampe et sa lentille à échelons (éteinte) -->
  <g transform="translate(400,150)">
    <ellipse rx="120" ry="100" fill="url(#lueurL)"><animate attributeName="opacity" values=".25;.45;.25" dur="5s" repeatCount="indefinite"/></ellipse>
    <rect x="-62" y="-92" width="124" height="176" rx="18" fill="#c7d5df" opacity=".55" stroke="#8aa0b0" stroke-width="3"/>
    ${[0,1,2,3,4,5,6].map(i=>`<rect x="-58" y="${-84+i*24}" width="116" height="10" rx="5" fill="#e8f1f7" opacity=".6"/>`).join("")}
    <circle r="18" fill="#efe6c2" stroke="#a89a6a" stroke-width="3"/>
    <rect x="-34" y="84" width="68" height="30" fill="#4a505a"/><rect x="-50" y="110" width="100" height="14" fill="#5a606b"/>
  </g>
  <!-- tableau de commande verrouillé -->
  <g transform="translate(640,250)"><rect x="-60" y="-34" width="120" height="44" rx="6" fill="#2e3440" stroke="#8a93a3"/>
    ${[0,1,2,3,4].map(i=>`<circle cx="${-42+i*21}" cy="-12" r="6" fill="#5a1f1f"><animate attributeName="fill" values="#5a1f1f;#b33a3a;#5a1f1f" dur="${2+i*0.3}s" repeatCount="indefinite"/></circle>`).join("")}</g>
  <!-- registre du gardien sur un tabouret -->
  <g transform="translate(150,256)"><rect x="-30" y="-6" width="60" height="8" fill="#6b4a2b"/><rect x="-24" y="2" width="6" height="40" fill="#6b4a2b"/><rect x="18" y="2" width="6" height="40" fill="#6b4a2b"/>
    <rect x="-22" y="-16" width="44" height="10" fill="#1d3557"/><rect x="-20" y="-14" width="40" height="6" fill="#f3ead2"/></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — L'atelier des vitres
   ------------------------------------------------------------ */
"atelier": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murA" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d9cdb4"/><stop offset="100%" stop-color="#b9a988"/></linearGradient>
    <linearGradient id="faisceauA" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff2b0" stop-opacity=".9"/><stop offset="100%" stop-color="#fff2b0" stop-opacity=".15"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murA)"/>
  <!-- mur de pierres arrondi -->
  <g stroke="#a8977a" stroke-width="1.5" fill="none" opacity=".6">${[0,1,2,3,4,5].map(r=>`<path d="M0 ${30+r*34} H800"/>`).join("")}</g>
  <!-- fenêtre ronde : la nuit tombe -->
  <circle cx="110" cy="80" r="44" fill="#22385a" stroke="#5b4630" stroke-width="8"/>
  ${[0,1,2,3,4,5].map(i=>`<circle cx="${84+i*11}" cy="${62+(i%3)*10}" r="1.2" fill="#fdf6d8"><animate attributeName="opacity" values="1;.3;1" dur="${2+i*0.4}s" repeatCount="indefinite"/></circle>`).join("")}
  <line x1="66" y1="80" x2="154" y2="80" stroke="#5b4630" stroke-width="4"/><line x1="110" y1="36" x2="110" y2="124" stroke="#5b4630" stroke-width="4"/>
  <!-- étagère avec plaques de verre -->
  <rect x="560" y="70" width="210" height="10" fill="#6b4a2b"/>
  ${[0,1,2,3,4,5].map(i=>`<rect x="${572+i*32}" y="${28+(i%2)*6}" width="10" height="42" fill="${["#cfe6f5","#e9e4d4","#8a5a33","#cfe6f5","#c0c4c8","#e9e4d4"][i]}" stroke="#555" opacity=".9"/>`).join("")}
  <!-- établi -->
  <rect x="0" y="200" width="800" height="100" fill="#7a5532"/><rect x="0" y="196" width="800" height="10" fill="#946a40"/>
  <!-- banc d'essai : lampe, vitre, calque, bois -->
  <g transform="translate(250,196)">
    <rect x="-20" y="-10" width="40" height="10" fill="#333"/><line x1="0" y1="-10" x2="0" y2="-70" stroke="#333" stroke-width="4"/>
    <path d="M-6 -70 L26 -92 L36 -76 L8 -62 Z" fill="#c0392b"/>
    <circle cx="34" cy="-80" r="7" fill="#ffd23f"><animate attributeName="r" values="7;8;7" dur="2s" repeatCount="indefinite"/></circle>
    <polygon points="38,-86 300,-110 300,-50 38,-74" fill="url(#faisceauA)" opacity=".55"><animate attributeName="opacity" values=".45;.6;.45" dur="3s" repeatCount="indefinite"/></polygon>
    <!-- vitre (transparente) -->
    <rect x="110" y="-120" width="8" height="112" fill="#cfe6f5" opacity=".6" stroke="#6f8f9a"/>
    <!-- calque (translucide) -->
    <rect x="200" y="-120" width="6" height="112" fill="#f3efe2" opacity=".85" stroke="#9a9070"/>
    <g fill="#fff6c8" opacity=".55">${[-20,0,20].map(d=>`<polygon points="206,-80 300,${-80+d*2-8} 300,${-80+d*2+8}"/>`).join("")}</g>
    <!-- bois (opaque) et l'ombre derrière -->
    <rect x="300" y="-124" width="14" height="116" fill="#8a5a33" stroke="#5b3a1f"/>
    <rect x="314" y="-124" width="110" height="116" fill="#3a2a1a" opacity=".35"/>
    <g font-family="Arial,sans-serif" font-size="12" fill="#2b1c0e" font-weight="bold">
      <text x="114" y="14" text-anchor="middle">vitre</text><text x="203" y="14" text-anchor="middle">calque</text><text x="307" y="14" text-anchor="middle">bois</text></g>
  </g>
  <!-- outils -->
  <g transform="translate(640,230)" stroke="#2e3440" stroke-width="4" stroke-linecap="round"><line x1="0" y1="0" x2="40" y2="-14"/><line x1="56" y1="4" x2="96" y2="4"/></g>
  <rect x="80" y="214" width="70" height="40" fill="#d9c9a0" stroke="#8a7a50"/><text x="115" y="238" text-anchor="middle" font-family="Georgia,serif" font-size="11" fill="#3a2a1a">essais</text>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — La chambre aux ombres (théâtre d'ombres de Nils)
   ------------------------------------------------------------ */
"chambre": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murC" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3b3550"/><stop offset="100%" stop-color="#2a2639"/></linearGradient>
    <radialGradient id="tacheC" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#fff7d6"/><stop offset="100%" stop-color="#f1e6c0"/></radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murC)"/>
  <!-- fenêtre ronde et la Lune -->
  <circle cx="690" cy="70" r="40" fill="#18253a" stroke="#6b5a8a" stroke-width="7"/>
  <circle cx="702" cy="62" r="14" fill="#f7f1d0"/><circle cx="696" cy="62" r="13" fill="#18253a"/>
  <!-- lit -->
  <rect x="650" y="190" width="150" height="50" fill="#6b4a2b"/><rect x="654" y="170" width="146" height="30" rx="6" fill="#2e86ab"/>
  <rect x="740" y="150" width="40" height="40" rx="6" fill="#f3ead2"/>
  <!-- plancher -->
  <rect y="240" width="800" height="60" fill="#5b4630"/>
  <g stroke="#4a3826">${[0,1,2,3,4,5,6,7].map(i=>`<line x1="${i*110}" y1="240" x2="${i*110-30}" y2="300"/>`).join("")}</g>
  <!-- drap tendu (écran) -->
  <line x1="150" y1="40" x2="470" y2="40" stroke="#8a7a50" stroke-width="5"/>
  <rect x="160" y="42" width="300" height="180" fill="url(#tacheC)" stroke="#cfc3a0"/>
  <!-- ombre portée du bateau : grandit et rapetisse quand la lampe avance et recule -->
  <g transform="translate(310,140)">
    <g><animateTransform attributeName="transform" type="scale" values="0.7;1.35;0.7" dur="7s" repeatCount="indefinite"/>
      <path d="M-50 10 L50 10 L38 26 L-38 26 Z" fill="#1d1a24"/><line x1="0" y1="10" x2="0" y2="-60" stroke="#1d1a24" stroke-width="5"/>
      <polygon points="3,-56 3,6 44,6" fill="#1d1a24"/><polygon points="-3,-48 -3,6 -30,6" fill="#1d1a24"/></g>
  </g>
  <!-- figurine en carton sur son pied, et la lampe de poche qui avance et recule -->
  <g transform="translate(500,190)">
    <rect x="-3" y="0" width="6" height="50" fill="#8a7a50"/>
    <path d="M-20 -4 L20 -4 L15 4 L-15 4 Z" fill="#7a5532"/><line x1="0" y1="-4" x2="0" y2="-34" stroke="#7a5532" stroke-width="3"/><polygon points="2,-32 2,-6 20,-6" fill="#c9a26a"/>
  </g>
  <g transform="translate(590,186)"><rect x="-44" y="0" width="88" height="8" fill="#6b4a2b"/><rect x="-38" y="8" width="6" height="46" fill="#6b4a2b"/><rect x="32" y="8" width="6" height="46" fill="#6b4a2b"/></g>
  <g><animateTransform attributeName="transform" type="translate" values="30 0;-40 0;30 0" dur="7s" repeatCount="indefinite"/>
    <g transform="translate(590,176) rotate(180)"><rect x="-26" y="-8" width="40" height="16" rx="4" fill="#c0392b"/><rect x="14" y="-11" width="10" height="22" rx="2" fill="#7a2418"/>
      <circle cx="26" cy="0" r="6" fill="#ffd23f"/></g></g>
  <!-- cahier d'expériences -->
  <g transform="translate(90,262)"><rect x="-36" y="-10" width="72" height="20" fill="#f3ead2" stroke="#8a7a50"/><line x1="0" y1="-10" x2="0" y2="10" stroke="#8a7a50"/></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — La cour du cadran solaire (souvenir de la journée)
   ------------------------------------------------------------ */
"cour": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="cielCour" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f6b26b"/><stop offset="55%" stop-color="#f9d89c"/><stop offset="100%" stop-color="#cfe3f0"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielCour)"/>
  <!-- mer et île au loin -->
  <rect y="120" width="800" height="40" fill="#5f8fb8"/>${VAGUES(132, "#86aed0", "9s")}
  <!-- le phare, à gauche -->
  <g transform="translate(90,0)">
    <polygon points="-22,190 22,190 15,40 -15,40" fill="#f4f1ea" stroke="#555"/>
    <rect x="-17" y="80" width="34" height="14" fill="#c0392b"/><rect x="-20" y="130" width="40" height="14" fill="#c0392b"/>
    <rect x="-14" y="18" width="28" height="22" fill="#d9e8f5" stroke="#333"/><polygon points="-18,18 18,18 0,4" fill="#333"/>
    <rect x="-24" y="38" width="48" height="5" fill="#333"/>
  </g>
  <!-- cour pavée -->
  <rect y="160" width="800" height="140" fill="#d9c8a4"/>
  <g stroke="#bfae88" stroke-width="1.5">${[0,1,2,3].map(r=>`<line x1="0" y1="${178+r*32}" x2="800" y2="${178+r*32}"/>`).join("")}${Array.from({length:16},(_,i)=>`<line x1="${i*54}" y1="160" x2="${i*54-40}" y2="300"/>`).join("")}</g>
  <!-- muret -->
  <rect x="0" y="150" width="800" height="14" fill="#a8977a"/>
  <!-- cadran solaire au sol : traits des heures (ellipse vue en perspective) -->
  <g transform="translate(430,236)">
    <ellipse rx="190" ry="52" fill="none" stroke="#7a6a48" stroke-width="2" stroke-dasharray="4 6"/>
    ${[-75,-50,-25,0,25,50,75].map((a,i)=>{ const r=Math.PI*a/180; return `<line x1="0" y1="0" x2="${(Math.sin(r)*190).toFixed(0)}" y2="${(-Math.cos(r)*52).toFixed(0)}" stroke="#7a6a48" stroke-width="2" opacity=".6"/><text x="${(Math.sin(r)*208).toFixed(0)}" y="${(-Math.cos(r)*60).toFixed(0)}" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#5b4a2a">${["8","10","12","14","16","18","20"][i]}</text>`; }).join("")}
    <!-- l'ombre du bâton qui tourne au fil de la journée -->
    <g><animateTransform attributeName="transform" type="rotate" values="-70;70;-70" dur="16s" repeatCount="indefinite"/>
      <line x1="0" y1="0" x2="0" y2="-48" stroke="#3b3b3b" stroke-width="7" stroke-linecap="round" opacity=".6"/></g>
    <rect x="-4" y="-70" width="8" height="70" fill="#7a4b2a"/><ellipse cy="0" rx="10" ry="4" fill="#5b3a1f"/>
  </g>
  <!-- banc, appareil photo et carnet d'Achille -->
  <g transform="translate(690,250)"><rect x="-60" y="-6" width="120" height="10" fill="#6b4a2b"/><rect x="-54" y="4" width="8" height="30" fill="#6b4a2b"/><rect x="46" y="4" width="8" height="30" fill="#6b4a2b"/>
    <rect x="-40" y="-22" width="34" height="16" rx="3" fill="#2e3440"/><circle cx="-23" cy="-14" r="5" fill="#8aa0b0"/>
    <rect x="10" y="-14" width="36" height="8" fill="#f3ead2" stroke="#8a7a50"/></g>
  <!-- mouettes -->
  <g stroke="#3b3b3b" stroke-width="2" fill="none">
    <path d="M300 60 q8 -8 16 0 q8 -8 16 0"><animateTransform attributeName="transform" type="translate" values="0 0;200 -10;0 0" dur="26s" repeatCount="indefinite"/></path>
    <path d="M520 84 q6 -6 12 0 q6 -6 12 0"><animateTransform attributeName="transform" type="translate" values="0 0;-160 8;0 0" dur="30s" repeatCount="indefinite"/></path></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — La galerie du phare (la Lune, La Mouette)
   ------------------------------------------------------------ */
"galerie": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_NUIT("cielG")}
    <radialGradient id="halo" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#f7f1d0" stop-opacity=".35"/><stop offset="100%" stop-color="#f7f1d0" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielG)"/>
  ${ETOILES(36, 150)}
  <!-- la pleine lune, éclairée par le Soleil -->
  <circle cx="600" cy="70" r="60" fill="url(#halo)"/>
  <circle cx="600" cy="70" r="26" fill="#f7f1d0"/>
  <!-- nuages qui passent devant -->
  <g fill="#4a5a75" opacity=".85">
    <g><animateTransform attributeName="transform" type="translate" values="-200 0;900 0" dur="38s" repeatCount="indefinite"/>
      <ellipse cx="0" cy="72" rx="70" ry="16"/><ellipse cx="-30" cy="62" rx="34" ry="14"/><ellipse cx="26" cy="60" rx="38" ry="16"/></g>
    <g><animateTransform attributeName="transform" type="translate" values="300 0;-500 0" dur="52s" repeatCount="indefinite"/>
      <ellipse cx="400" cy="110" rx="90" ry="14"/><ellipse cx="370" cy="100" rx="40" ry="14"/></g>
  </g>
  <!-- la mer argentée -->
  <rect y="178" width="800" height="122" fill="#1b3553"/>
  <g stroke="#f7f1d0" stroke-width="2" opacity=".55">${[0,1,2,3,4].map(i=>`<line x1="${560+i*6}" y1="${190+i*12}" x2="${620-i*4}" y2="${190+i*12}"><animate attributeName="opacity" values=".2;.9;.2" dur="${2.5+i*0.5}s" repeatCount="indefinite"/></line>`).join("")}</g>
  ${VAGUES(196, "#4f79a4", "8s")}${VAGUES(222, "#416a95", "11s")}
  <!-- rochers -->
  <path d="M200 210 q20 -24 46 -10 q18 -14 34 6 l10 14 Z" fill="#2c2a28"/><path d="M330 220 q14 -16 32 -6 q10 -8 20 6 Z" fill="#2c2a28"/>
  <!-- La Mouette, au loin, qui envoie ses éclats -->
  <g>${VOILIER(470, 196, .9, false)}
    <circle cx="470" cy="140" r="5" fill="#ffd23f"><animate attributeName="opacity" values="1;1;0;1;0;0;1;1;1;0;0;1" dur="4s" repeatCount="indefinite"/></circle>
    <animateTransform attributeName="transform" type="translate" values="0 0;-30 2;0 0" dur="30s" repeatCount="indefinite"/></g>
  <!-- la rambarde de la galerie, au premier plan -->
  <rect x="0" y="246" width="800" height="54" fill="#2a2f38"/>
  <rect x="0" y="210" width="800" height="6" fill="#4a505a"/>
  <g fill="#3a3f48">${Array.from({length:20},(_,i)=>`<rect x="${i*42+10}" y="216" width="5" height="32"/>`).join("")}</g>
  <!-- radio du phare -->
  <g transform="translate(120,262)"><rect x="-34" y="-22" width="68" height="34" rx="5" fill="#4a505a" stroke="#8a93a3"/><circle cx="-16" cy="-5" r="8" fill="#2e3440"/>
    <rect x="2" y="-14" width="24" height="8" fill="#7fd17f"><animate attributeName="opacity" values="1;.4;1" dur="1.2s" repeatCount="indefinite"/></rect>
    <line x1="26" y1="-22" x2="38" y2="-48" stroke="#8a93a3" stroke-width="2"/></g>
</svg>`
};

window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
