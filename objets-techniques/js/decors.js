/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de l'atelier de l'inventrice
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (zéro attente, zéro fichier).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.png
     →  SVG    dessiné ci-dessous

     atelier    l'entrée de l'atelier (table d'objets, coffre-fort)
     etabli     l'établi de démontage (lampe torche, vélo au mur)
     materiaux  la matériauthèque (casiers d'échantillons)
     machines   la salle des machines (engrenages, poulie, éolienne)
     montage    le coin montage (plans, notice, coffre-fort)
   Les animations sont figées par le réglage « animations réduites »
   (css/animations.css).
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["atelier"];
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

const SALLE_NUM = { "atelier":1, "etabli":2, "materiaux":3, "machines":4, "montage":5 };

/* ---- Fragments communs ---- */
const MUR_BOIS = `
  <linearGradient id="murBois" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#6b4a2e"/><stop offset="100%" stop-color="#4a3220"/>
  </linearGradient>
  <linearGradient id="solAtelier" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#8a7a66"/><stop offset="100%" stop-color="#5e5244"/>
  </linearGradient>
  <radialGradient id="halo" cx="50%" cy="0%" r="80%">
    <stop offset="0%" stop-color="#fff2b8" stop-opacity=".55"/><stop offset="100%" stop-color="#fff2b8" stop-opacity="0"/>
  </radialGradient>`;

/** Roue dentée : cx, cy, rayon, nombre de dents, couleur, durée d'un tour (s), sens (1 ou -1). */
function roueDentee(cx, cy, r, n, coul, dur, sens){
  let dents = "";
  for(let i=0;i<n;i++){
    const a = i*360/n;
    dents += `<rect x="${-r*0.12}" y="${-r-r*0.22}" width="${r*0.24}" height="${r*0.3}" rx="1.5" transform="rotate(${a})"/>`;
  }
  const fin = sens>0 ? 360 : -360;
  return `<g transform="translate(${cx},${cy})"><g fill="${coul}">
    <animateTransform attributeName="transform" type="rotate" from="0" to="${fin}" dur="${dur}s" repeatCount="indefinite"/>
    ${dents}<circle r="${r}"/><circle r="${r*0.35}" fill="#2b2b2b" opacity=".55"/>
    <circle r="${r*0.12}" fill="#d9d9d9"/></g></g>`;
}

/** Lampe suspendue qui se balance doucement. */
function lampe(x){
  return `<g transform="translate(${x},0)">
    <g><animateTransform attributeName="transform" type="rotate" values="-2 0 0;2 0 0;-2 0 0" dur="6s" repeatCount="indefinite"/>
      <line x1="0" y1="0" x2="0" y2="40" stroke="#222" stroke-width="2"/>
      <path d="M-18 40 L18 40 L10 26 L-10 26 Z" fill="#2f5d50"/>
      <circle cy="44" r="6" fill="#fff6b0"/>
      <path d="M-60 300 L-14 44 L14 44 L60 300 Z" fill="#fff6b0" opacity=".10"/>
    </g></g>`;
}

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — L'entrée de l'atelier
   ------------------------------------------------------------ */
"atelier": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${MUR_BOIS}</defs>
  <rect width="800" height="300" fill="url(#murBois)"/>
  <g stroke="#3d2917" stroke-width="2" opacity=".6">
    <line x1="0" y1="60" x2="800" y2="60"/><line x1="0" y1="120" x2="800" y2="120"/><line x1="0" y1="180" x2="800" y2="180"/>
  </g>
  <!-- grande fenêtre avec pluie -->
  <rect x="60" y="30" width="160" height="130" fill="#9fc3d9" stroke="#2b1c10" stroke-width="6"/>
  <line x1="140" y1="30" x2="140" y2="160" stroke="#2b1c10" stroke-width="4"/><line x1="60" y1="95" x2="220" y2="95" stroke="#2b1c10" stroke-width="4"/>
  <g stroke="#e8f2f8" stroke-width="1.5" opacity=".8">
    <line x1="80" y1="40" x2="76" y2="52"><animate attributeName="y1" values="34;150" dur="1.4s" repeatCount="indefinite"/><animate attributeName="y2" values="46;162" dur="1.4s" repeatCount="indefinite"/></line>
    <line x1="120" y1="40" x2="116" y2="52"><animate attributeName="y1" values="34;150" dur="1.1s" begin=".4s" repeatCount="indefinite"/><animate attributeName="y2" values="46;162" dur="1.1s" begin=".4s" repeatCount="indefinite"/></line>
    <line x1="170" y1="40" x2="166" y2="52"><animate attributeName="y1" values="34;150" dur="1.3s" begin=".8s" repeatCount="indefinite"/><animate attributeName="y2" values="46;162" dur="1.3s" begin=".8s" repeatCount="indefinite"/></line>
    <line x1="200" y1="40" x2="196" y2="52"><animate attributeName="y1" values="34;150" dur="1.2s" begin=".2s" repeatCount="indefinite"/><animate attributeName="y2" values="46;162" dur="1.2s" begin=".2s" repeatCount="indefinite"/></line>
  </g>
  <!-- panneau à outils -->
  <rect x="270" y="30" width="220" height="110" rx="4" fill="#c9a76e" stroke="#7a5a2e" stroke-width="3"/>
  <g fill="#555"><rect x="290" y="45" width="8" height="60" rx="2"/><rect x="284" y="40" width="20" height="14" rx="3"/>
    <rect x="330" y="50" width="6" height="70"/><path d="M322 50 L344 50 L340 60 L326 60 Z"/>
    <circle cx="390" cy="70" r="18" fill="none" stroke="#555" stroke-width="5"/><rect x="386" y="86" width="8" height="40"/>
    <rect x="430" y="45" width="40" height="8" rx="3"/><rect x="446" y="53" width="8" height="60"/></g>
  <!-- coffre-fort -->
  <g transform="translate(600,70)">
    <rect width="150" height="170" rx="8" fill="#3e4a52" stroke="#1f262b" stroke-width="4"/>
    <rect x="12" y="12" width="126" height="146" rx="6" fill="#4f5d66"/>
    <circle cx="75" cy="80" r="30" fill="#2b3338" stroke="#c9a227" stroke-width="3"/>
    <g transform="translate(75,80)"><g stroke="#c9a227" stroke-width="3">
      <animateTransform attributeName="transform" type="rotate" values="0;40;-20;0" dur="8s" repeatCount="indefinite"/>
      <line x1="0" y1="-22" x2="0" y2="22"/><line x1="-22" y1="0" x2="22" y2="0"/></g></g>
    <g fill="#c9a227">${[0,1,2,3,4].map(i=>`<rect x="${20+i*23}" y="126" width="18" height="18" rx="3"/>`).join("")}</g>
  </g>
  <!-- sol -->
  <rect x="0" y="240" width="800" height="60" fill="url(#solAtelier)"/>
  <!-- table d'objets -->
  <rect x="220" y="196" width="340" height="12" fill="#7a5a36"/><rect x="236" y="208" width="10" height="40" fill="#5c4127"/><rect x="534" y="208" width="10" height="40" fill="#5c4127"/>
  <g>
    <rect x="248" y="178" width="46" height="16" rx="7" fill="#c0392b"/><circle cx="296" cy="186" r="9" fill="#f7e27a"/>
    <rect x="320" y="170" width="30" height="24" rx="4" fill="#2f6fa7"/><rect x="326" y="164" width="18" height="8" rx="3" fill="#2f6fa7"/>
    <g transform="translate(390,180)" fill="none" stroke="#333" stroke-width="3"><circle cx="0" cy="8" r="9"/><circle cx="40" cy="8" r="9"/><path d="M0 8 L16 -6 L34 -6 L40 8 M16 -6 L20 8"/></g>
    <rect x="460" y="176" width="24" height="18" rx="3" fill="#e0a800"/><rect x="496" y="160" width="40" height="34" rx="6" fill="#2e7d32"/>
  </g>
  <rect width="800" height="300" fill="url(#halo)"/>
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — L'établi de démontage
   ------------------------------------------------------------ */
"etabli": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${MUR_BOIS}</defs>
  <rect width="800" height="300" fill="#4e5b52"/>
  <g stroke="#3f4a43" stroke-width="2">${Array.from({length:14},(_,i)=>`<line x1="${i*60}" y1="0" x2="${i*60}" y2="200"/>`).join("")}</g>
  ${lampe(400)}
  <!-- vélo accroché au mur -->
  <g transform="translate(90,70)" fill="none" stroke="#1d1d1d" stroke-width="4">
    <circle cx="0" cy="60" r="38"/><circle cx="120" cy="60" r="38"/>
    <path d="M0 60 L40 10 L95 10 L120 60 M40 10 L55 60 L95 10 M55 60 L0 60" stroke="#c0392b"/>
    <circle cx="55" cy="60" r="8"/><line x1="95" y1="10" x2="100" y2="-4"/><line x1="92" y1="-4" x2="110" y2="-4"/>
  </g>
  <!-- établi -->
  <rect x="0" y="200" width="800" height="100" fill="url(#solAtelier)"/>
  <rect x="200" y="186" width="560" height="20" fill="#8a6440"/>
  <rect x="220" y="160" width="520" height="28" rx="4" fill="#2e6b4a"/>
  <!-- pièces de la lampe torche, alignées -->
  <g>
    <rect x="240" y="166" width="80" height="16" rx="6" fill="#c0392b"/>
    <rect x="340" y="166" width="36" height="16" rx="3" fill="#f2c94c"/><rect x="376" y="170" width="4" height="8" fill="#888"/>
    <rect x="392" y="166" width="36" height="16" rx="3" fill="#f2c94c"/><rect x="428" y="170" width="4" height="8" fill="#888"/>
    <rect x="452" y="168" width="18" height="12" rx="3" fill="#333"/>
    <path d="M494 164 L520 164 L530 184 L484 184 Z" fill="#d9d9d9"/>
    <circle cx="560" cy="174" r="8" fill="#fff6b0" stroke="#888"><animate attributeName="fill" values="#fff6b0;#ffe066;#fff6b0" dur="3s" repeatCount="indefinite"/></circle>
    <ellipse cx="600" cy="174" rx="14" ry="10" fill="#cfe6f5" stroke="#8aa"/>
  </g>
  <!-- tournevis qui tourne -->
  <g transform="translate(680,150)"><g>
    <animateTransform attributeName="transform" type="rotate" values="0;-10;0;10;0" dur="4s" repeatCount="indefinite"/>
    <rect x="-4" y="-40" width="8" height="30" rx="3" fill="#e0a800"/><rect x="-1.5" y="-10" width="3" height="24" fill="#999"/></g></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — La matériauthèque
   ------------------------------------------------------------ */
"materiaux": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${MUR_BOIS}</defs>
  <rect width="800" height="300" fill="#3b3a44"/>
  ${lampe(200)}${lampe(600)}
  <!-- casiers -->
  <g transform="translate(60,40)">
    ${Array.from({length:4},(_,l)=>Array.from({length:8},(_,c)=>{
      const coul = ["#9aa4ad","#7fb3d5","#8d6e4b","#d9e8ef","#c98b5a","#e8d6b8","#b0b7bd","#6fa36b"][(l*3+c)%8];
      return `<g transform="translate(${c*86},${l*52})"><rect width="80" height="46" fill="#5a4632" stroke="#2c2118" stroke-width="2"/>
        <rect x="16" y="14" width="48" height="24" rx="4" fill="${coul}"/></g>`;}).join("")).join("")}
  </g>
  <!-- un échantillon mal rangé qui clignote -->
  <g transform="translate(404,154)"><rect width="48" height="24" rx="4" fill="#c0392b" stroke="#fff" stroke-width="2">
    <animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/></rect></g>
  <rect x="0" y="252" width="800" height="48" fill="url(#solAtelier)"/>
  <!-- échelle -->
  <g stroke="#8a6440" stroke-width="5"><line x1="740" y1="30" x2="760" y2="260"/><line x1="770" y1="30" x2="790" y2="260"/>
    ${[60,100,140,180,220].map(y=>`<line x1="${743+y*0.087}" y1="${y}" x2="${773+y*0.087}" y2="${y}"/>`).join("")}</g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — La salle des machines
   ------------------------------------------------------------ */
"machines": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${MUR_BOIS}
    <linearGradient id="ciel4" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#8fbde0"/><stop offset="100%" stop-color="#d7e9f5"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="#34414a"/>
  <!-- fenêtre avec éolienne -->
  <rect x="560" y="30" width="200" height="140" fill="url(#ciel4)" stroke="#1f2a31" stroke-width="6"/>
  <g transform="translate(660,100)"><line x1="0" y1="0" x2="0" y2="70" stroke="#eee" stroke-width="4"/>
    <g fill="#f4f4f4"><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="5s" repeatCount="indefinite"/>
      <path d="M0 0 L-4 -46 L4 -46 Z"/><path d="M0 0 L-4 -46 L4 -46 Z" transform="rotate(120)"/><path d="M0 0 L-4 -46 L4 -46 Z" transform="rotate(240)"/></g>
    <circle r="5" fill="#bbb"/></g>
  <!-- panneau solaire sur l'appui -->
  <g transform="translate(570,160) skewX(-20)"><rect width="70" height="24" fill="#1d3557" stroke="#aaa"/>
    <g stroke="#6c8fb3"><line x1="23" y1="0" x2="23" y2="24"/><line x1="46" y1="0" x2="46" y2="24"/><line x1="0" y1="12" x2="70" y2="12"/></g></g>
  <!-- engrenages qui s'entraînent : sens contraires -->
  ${roueDentee(140, 110, 46, 14, "#b08d57", 8, 1)}
  ${roueDentee(218, 142, 30, 9, "#8c9aa3", 5.14, -1)}
  ${roueDentee(266, 104, 24, 8, "#c9a227", 4.57, 1)}
  <!-- poulie au plafond et charge -->
  <g transform="translate(420,40)">
    <line x1="0" y1="-40" x2="0" y2="0" stroke="#222" stroke-width="3"/>
    <g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="6s" repeatCount="indefinite"/>
      <circle r="18" fill="#777" stroke="#333" stroke-width="3"/><line x1="-18" y1="0" x2="18" y2="0" stroke="#333" stroke-width="2"/></g>
    <line x1="-18" y1="0" x2="-18" y2="150" stroke="#c8b38a" stroke-width="2"/>
    <line x1="18" y1="0" x2="18" y2="110" stroke="#c8b38a" stroke-width="2"/>
    <rect x="4" y="110" width="28" height="24" fill="#8a6440"><animate attributeName="y" values="110;90;110" dur="6s" repeatCount="indefinite"/></rect>
  </g>
  <rect x="0" y="240" width="800" height="60" fill="url(#solAtelier)"/>
  <!-- vélo sur support, roue arrière qui tourne -->
  <g transform="translate(300,200)">
    <rect x="-10" y="36" width="24" height="10" fill="#555"/>
    <g transform="translate(0,20)"><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="2s" repeatCount="indefinite"/>
      <circle r="28" fill="none" stroke="#1d1d1d" stroke-width="4"/><line x1="-28" y1="0" x2="28" y2="0" stroke="#777"/><line x1="0" y1="-28" x2="0" y2="28" stroke="#777"/></g></g>
    <circle cx="100" cy="20" r="28" fill="none" stroke="#1d1d1d" stroke-width="4"/>
    <path d="M0 20 L35 -20 L80 -20 L100 20 M35 -20 L45 20 L80 -20 M45 20 L0 20" fill="none" stroke="#2e7d32" stroke-width="4"/>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — Le coin montage
   ------------------------------------------------------------ */
"montage": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${MUR_BOIS}</defs>
  <rect width="800" height="300" fill="#2e3f5c"/>
  <!-- plans épinglés -->
  ${[[60,30,-4],[210,40,3],[360,26,-2]].map(([x,y,r])=>`<g transform="translate(${x},${y}) rotate(${r})">
    <rect width="130" height="96" fill="#dfe9f5" stroke="#9fb3c8"/>
    <g stroke="#2f5d8a" stroke-width="1.5" fill="none"><rect x="14" y="16" width="60" height="40"/><circle cx="96" cy="36" r="16"/><line x1="14" y1="72" x2="116" y2="72"/><line x1="14" y1="82" x2="90" y2="82"/></g>
    <circle cx="65" cy="4" r="4" fill="#c0392b"/></g>`).join("")}
  <!-- coffre-fort -->
  <g transform="translate(600,60)">
    <rect width="150" height="180" rx="8" fill="#3e4a52" stroke="#1f262b" stroke-width="4"/>
    <rect x="14" y="16" width="122" height="30" rx="4" fill="#12202a"/>
    <text x="75" y="37" text-anchor="middle" font-family="monospace" font-size="14" fill="#7cf29a">_ _ _ _ _<animate attributeName="opacity" values="1;.3;1" dur="1.6s" repeatCount="indefinite"/></text>
    <circle cx="75" cy="110" r="32" fill="#2b3338" stroke="#c9a227" stroke-width="3"/>
    <rect x="130" y="95" width="10" height="30" rx="3" fill="#c9a227"/>
  </g>
  <rect x="0" y="240" width="800" height="60" fill="url(#solAtelier)"/>
  <!-- table lumineuse avec notice -->
  <rect x="120" y="196" width="420" height="14" fill="#7a5a36"/>
  <rect x="140" y="176" width="380" height="20" fill="#f8f3dc"><animate attributeName="fill" values="#f8f3dc;#fffbe8;#f8f3dc" dur="5s" repeatCount="indefinite"/></rect>
  <g transform="translate(250,150)"><rect width="150" height="40" fill="#fff" stroke="#999"/>
    ${[0,1,2,3,4].map(i=>`<g transform="translate(${10+i*28},8)"><rect width="20" height="20" rx="3" fill="#e3eefa" stroke="#2f5d8a"/><text x="10" y="15" text-anchor="middle" font-size="11" fill="#1f2430">${i+1}</text></g>`).join("")}</g>
</svg>`
};

window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
