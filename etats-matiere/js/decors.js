/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de « La Fabrique des états »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux (la Fabrique des états, usine imaginaire, au lendemain d'un orage) :
     hall       le hall des cuves (trois cuves de verre, tuyaux, pupitre éteint)
     terrasse   la terrasse du ballon-sonde (girouette, abri météo, ballon)
     glacerie   la glacerie de Paolo (congélateur givré, bouilloire, thermomètres)
     cuisine    la cuisine de Fatou (balance, bols, congélateur, carnet)
     tour       le château d'eau de Ninon (bassin, vue sur le lac et les nuages)
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["hall"];
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

const SALLE_NUM = { "hall":1, "terrasse":2, "glacerie":3, "cuisine":4, "tour":5 };

/* ---- Fragments communs ---- */
const CIEL_JOUR = (id) => `
  <linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#9cc7e4"/><stop offset="100%" stop-color="#e3f1f9"/>
  </linearGradient>`;
/* Un nuage blanc qui dérive (x, y, échelle, durée) */
const NUAGE = (x, y, k=1, dur="60s") => `<g><g transform="translate(${x},${y}) scale(${k})" fill="#ffffff" opacity=".95">
  <ellipse cx="0" cy="0" rx="46" ry="18"/><ellipse cx="-22" cy="-10" rx="22" ry="17"/><ellipse cx="16" cy="-14" rx="26" ry="20"/></g>
  <animateTransform attributeName="transform" type="translate" values="0 0;50 0;0 0" dur="${dur}" repeatCount="indefinite"/></g>`;
/* Mur de briques (rectangle x, y, l, h) */
const BRIQUES = (x, y, l, h, c1="#a85a43", c2="#8d4a36") => {
  let r = `<rect x="${x}" y="${y}" width="${l}" height="${h}" fill="${c1}"/>`;
  for(let j=0; j*18 < h; j++){
    r += `<line x1="${x}" y1="${y+j*18}" x2="${x+l}" y2="${y+j*18}" stroke="${c2}" stroke-width="2"/>`;
    for(let i=(j%2)*20; i < l; i+=40) r += `<line x1="${x+i}" y1="${y+j*18}" x2="${x+i}" y2="${Math.min(y+h, y+j*18+18)}" stroke="${c2}" stroke-width="2"/>`;
  }
  return r;
};
/* Goutte qui tombe en boucle */
const GOUTTE = (x, y1, y2, dur="2.4s", delai="0s") => `<ellipse cx="${x}" cy="${y1}" rx="3" ry="4.5" fill="#5aa0d8">
  <animate attributeName="cy" values="${y1};${y2}" dur="${dur}" begin="${delai}" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="1;1;0" dur="${dur}" begin="${delai}" repeatCount="indefinite"/></ellipse>`;
/* Gouttelettes blanches qui montent (la « fumée » d'une casserole : de l'eau liquide) */
const BUEE = (x, y) => `<g fill="#ffffff">${[0,1,2,3,4].map(i=>`<circle cx="${x + (i%2?8:-8)}" cy="${y}" r="${5+i}" opacity=".0">
  <animate attributeName="cy" values="${y};${y-70}" dur="3.2s" begin="${i*0.6}s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0;.7;0" dur="3.2s" begin="${i*0.6}s" repeatCount="indefinite"/></circle>`).join("")}</g>`;
const SVG_OUV = (id) => `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">`;

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — Le hall des cuves
   ------------------------------------------------------------ */
"hall": `${SVG_OUV()}
  <defs><linearGradient id="solH" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#6f7c86"/><stop offset="100%" stop-color="#4a555e"/></linearGradient></defs>
  ${BRIQUES(0, 0, 800, 230)}
  <rect y="230" width="800" height="70" fill="url(#solH)"/>
  <!-- tuyaux au plafond -->
  <rect x="0" y="22" width="800" height="12" fill="#8a949c"/><rect x="0" y="46" width="800" height="8" fill="#b07a3e"/>
  ${[120,300,500,680].map(x=>`<rect x="${x}" y="34" width="10" height="60" fill="#8a949c"/>`).join("")}
  ${GOUTTE(305, 96, 228, "2.6s")}
  <!-- trois cuves : glace, eau, gaz -->
  ${[[150,"#dff1fb","glace"],[330,"#7fb8e6","eau"],[510,"#eef3f7","gaz"]].map(([x,c,t],i)=>`
    <g><rect x="${x-60}" y="96" width="120" height="140" rx="14" fill="#ffffff" fill-opacity=".35" stroke="#2f4a5f" stroke-width="4"/>
    ${t==="glace"?`<rect x="${x-50}" y="150" width="44" height="40" fill="${c}" stroke="#3b88b5" stroke-width="2"/><rect x="${x+2}" y="170" width="44" height="60" fill="${c}" stroke="#3b88b5" stroke-width="2"/><rect x="${x-46}" y="194" width="44" height="36" fill="${c}" stroke="#3b88b5" stroke-width="2"/>`:""}
    ${t==="eau"?`<rect x="${x-56}" y="150" width="112" height="82" fill="${c}"/><line x1="${x-56}" y1="150" x2="${x+56}" y2="150" stroke="#1d5c8f" stroke-width="3"><animate attributeName="y1" values="150;147;150" dur="3s" repeatCount="indefinite"/><animate attributeName="y2" values="150;153;150" dur="3s" repeatCount="indefinite"/></line>`:""}
    ${t==="gaz"?[0,1,2,3,4,5,6,7].map(k=>`<circle cx="${x-40+(k*23)%84}" cy="${120+(k*37)%100}" r="3" fill="#8fa3b5"><animate attributeName="cx" values="${x-40+(k*23)%84};${x-30+(k*41)%80};${x-40+(k*23)%84}" dur="${3+k%3}s" repeatCount="indefinite"/></circle>`).join(""):""}
    <rect x="${x-34}" y="104" width="68" height="18" rx="4" fill="#f4e9d0" stroke="#7a6a4a"/><text x="${x}" y="117" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#9a8a6a">? ? ?</text></g>`).join("")}
  <!-- le pupitre éteint -->
  <rect x="640" y="150" width="130" height="86" rx="8" fill="#3d4a55" stroke="#1f2a33" stroke-width="3"/>
  ${[0,1,2,3,4].map(i=>`<circle cx="${662+i*22}" cy="172" r="7" fill="#5b2a22"><animate attributeName="fill" values="#5b2a22;#8a3a2a;#5b2a22" dur="${2+i*0.3}s" repeatCount="indefinite"/></circle>`).join("")}
  ${[0,1,2,3,4].map(i=>`<rect x="${652+i*24}" y="196" width="20" height="24" rx="3" fill="#cfd6dc"/>`).join("")}
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — La terrasse du ballon-sonde
   ------------------------------------------------------------ */
"terrasse": `${SVG_OUV()}
  <defs>${CIEL_JOUR("cielT")}</defs>
  <rect width="800" height="300" fill="url(#cielT)"/>
  ${NUAGE(150, 60, 1, "70s")}${NUAGE(560, 40, .8, "55s")}
  <!-- toits de la ville au loin -->
  <path d="M0 210 L60 190 L120 205 L170 180 L240 200 L320 185 L400 205 L480 188 L560 202 L640 186 L720 200 L800 190 L800 230 L0 230 Z" fill="#9aa9b4"/>
  <rect y="226" width="800" height="74" fill="#7b8790"/><rect y="222" width="800" height="8" fill="#5c666e"/>
  <!-- girouette qui oscille -->
  <line x1="90" y1="226" x2="90" y2="120" stroke="#333" stroke-width="4"/>
  <g><polygon points="60,118 120,118 126,112 120,124 60,124 54,112" fill="#b03a2e"/><animateTransform attributeName="transform" type="rotate" values="-12 90 120;12 90 120;-12 90 120" dur="5s" repeatCount="indefinite"/></g>
  <!-- abri météo -->
  <rect x="170" y="160" width="70" height="66" fill="#ffffff" stroke="#8a949c" stroke-width="3"/>
  ${[0,1,2,3,4].map(i=>`<line x1="176" y1="${170+i*11}" x2="234" y2="${170+i*11}" stroke="#c9d1d8" stroke-width="3"/>`).join("")}
  <!-- le ballon-sonde, à moitié gonflé, qui se balance -->
  <g><ellipse cx="460" cy="110" rx="62" ry="54" fill="#f4f6f8" stroke="#b8c2ca" stroke-width="3"/>
    <line x1="460" y1="164" x2="460" y2="210" stroke="#555" stroke-width="2"/>
    <rect x="448" y="206" width="24" height="18" fill="#e07b2f"/>
    <animateTransform attributeName="transform" type="rotate" values="-3 460 220;3 460 220;-3 460 220" dur="4s" repeatCount="indefinite"/></g>
  <!-- table : pompe, ballon de basket, balance -->
  <rect x="580" y="196" width="190" height="10" fill="#7a4b2a"/><rect x="590" y="206" width="8" height="24" fill="#7a4b2a"/><rect x="752" y="206" width="8" height="24" fill="#7a4b2a"/>
  <circle cx="620" cy="178" r="18" fill="#e07b2f" stroke="#7a3d12" stroke-width="2"/>
  <rect x="664" y="180" width="54" height="16" rx="3" fill="#d8dee6" stroke="#5b6b7b"/><rect x="676" y="183" width="30" height="10" fill="#163c2c"/>
  <rect x="736" y="140" width="8" height="56" fill="#3b4a5a"/><rect x="726" y="136" width="28" height="6" fill="#3b4a5a"/>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — La glacerie de Paolo
   ------------------------------------------------------------ */
"glacerie": `${SVG_OUV()}
  <rect width="800" height="300" fill="#e8eef2"/>
  ${Array.from({length:20},(_,i)=>`<line x1="${i*40}" y1="0" x2="${i*40}" y2="230" stroke="#cfd9e0" stroke-width="2"/>`).join("")}
  ${Array.from({length:6},(_,j)=>`<line x1="0" y1="${j*40}" x2="800" y2="${j*40}" stroke="#cfd9e0" stroke-width="2"/>`).join("")}
  <rect y="230" width="800" height="70" fill="#9fb0bc"/>
  <!-- congélateur givré -->
  <rect x="60" y="80" width="170" height="150" rx="8" fill="#f7fbfd" stroke="#8aa0b0" stroke-width="4"/>
  <rect x="74" y="94" width="142" height="122" rx="4" fill="#dcecf6"/>
  ${[0,1,2,3,4,5].map(i=>`<path d="M${86+i*22} 100 l6 10 l6 -10" stroke="#ffffff" stroke-width="3" fill="none"/>`).join("")}
  <text x="145" y="164" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" font-weight="bold" fill="#5a7d95">−15 °C</text>
  <!-- thermomètres au mur -->
  ${[300,340,380].map((x,i)=>`<rect x="${x}" y="60" width="14" height="110" rx="7" fill="#ffffff" stroke="#8a93a0" stroke-width="2"/><circle cx="${x+7}" cy="176" r="10" fill="#c62828"/>
    <rect x="${x+4}" y="${[150,128,72][i]}" width="6" height="${176-[150,128,72][i]}" fill="#c62828"/>`).join("")}
  <!-- plaque, casserole qui bout, gouttelettes au-dessus -->
  <rect x="470" y="196" width="230" height="34" rx="4" fill="#3d4a55"/>
  <circle cx="530" cy="196" r="20" fill="#c0392b" opacity=".6"><animate attributeName="opacity" values=".4;.8;.4" dur="1.6s" repeatCount="indefinite"/></circle>
  <path d="M488 150 L572 150 L566 196 L494 196 Z" fill="#9aa4ad" stroke="#4d565e" stroke-width="3"/>
  <rect x="490" y="160" width="80" height="34" fill="#7fb8e6"/>
  ${[0,1,2,3].map(i=>`<circle cx="${504+i*18}" cy="190" r="4" fill="#ffffff" opacity=".8"><animate attributeName="cy" values="192;162" dur="${1+i*0.2}s" repeatCount="indefinite"/></circle>`).join("")}
  ${BUEE(530, 140)}
  <!-- bouilloire -->
  <path d="M624 196 Q620 150 650 146 Q680 150 676 196 Z" fill="#b8c2ca" stroke="#4d565e" stroke-width="3"/>
  <path d="M676 166 L700 150" stroke="#4d565e" stroke-width="6"/>
  ${BUEE(704, 140)}
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — La cuisine de Fatou
   ------------------------------------------------------------ */
"cuisine": `${SVG_OUV()}
  <rect width="800" height="300" fill="#f6efe2"/>
  ${Array.from({length:16},(_,i)=>`<rect x="${i*50}" y="120" width="50" height="50" fill="${i%2?"#ffffff":"#e9f1f4"}"/>`).join("")}
  <rect y="170" width="800" height="16" fill="#8b5e3c"/><rect y="186" width="800" height="114" fill="#c99b6d"/>
  <!-- fenêtre -->
  <rect x="300" y="20" width="200" height="90" fill="#bfe0f2" stroke="#8b5e3c" stroke-width="6"/><line x1="400" y1="20" x2="400" y2="110" stroke="#8b5e3c" stroke-width="5"/>
  ${NUAGE(360, 62, .5, "40s")}
  <!-- grand congélateur avec carnet -->
  <rect x="620" y="30" width="150" height="200" rx="8" fill="#f7fbfd" stroke="#8aa0b0" stroke-width="4"/>
  <line x1="620" y1="100" x2="770" y2="100" stroke="#8aa0b0" stroke-width="3"/>
  <rect x="650" y="118" width="54" height="64" fill="#fffbe6" stroke="#b9a66a" transform="rotate(-4 677 150)"/>
  ${[0,1,2,3].map(i=>`<line x1="656" y1="${132+i*12}" x2="698" y2="${130+i*12}" stroke="#8a7a50" stroke-width="2"/>`).join("")}
  <circle cx="676" cy="118" r="5" fill="#c0392b"/>
  <!-- balance et bol de glaçons -->
  <rect x="80" y="150" width="130" height="20" rx="4" fill="#d8dee6" stroke="#5b6b7b" stroke-width="2"/>
  <rect x="112" y="154" width="64" height="12" rx="2" fill="#163c2c"/>
  <text x="144" y="164" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#7cf0a8">100 g<animate attributeName="opacity" values="1;.5;1" dur="2s" repeatCount="indefinite"/></text>
  <path d="M100 108 Q145 150 190 108 Z" fill="#ffffff" stroke="#5b6b7b" stroke-width="2"/>
  ${[0,1,2,3].map(i=>`<rect x="${116+i*16}" y="${100-(i%2)*6}" width="14" height="14" rx="2" fill="#cfeaf8" stroke="#3b88b5" stroke-width="1.5"/>`).join("")}
  <!-- bouteille gonflée sur le plan de travail -->
  <path d="M500 170 L500 120 Q500 108 510 104 L510 94 L526 94 L526 104 Q538 108 538 120 L538 170 Z" fill="#dff1fb" stroke="#3b4a5a" stroke-width="2"/>
  <rect x="508" y="80" width="20" height="9" rx="2" fill="#c0392b" transform="rotate(-18 518 85)"/>
  <!-- marmite qui mijote -->
  <path d="M250 170 L250 132 L330 132 L330 170 Z" fill="#555f68"/><rect x="244" y="126" width="92" height="8" rx="3" fill="#3d4a55"/>
  ${BUEE(290, 118)}
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — Le château d'eau de Ninon
   ------------------------------------------------------------ */
"tour": `${SVG_OUV()}
  <defs>${CIEL_JOUR("cielR")}</defs>
  <rect width="800" height="300" fill="url(#cielR)"/>
  <circle cx="90" cy="60" r="28" fill="#ffd23f"/>
  ${NUAGE(420, 50, 1.1, "80s")}${NUAGE(640, 70, .9, "65s")}
  <!-- pluie sous un nuage -->
  ${[0,1,2,3,4,5].map(i=>GOUTTE(620+i*14, 92, 190, "1.6s", (i*0.25)+"s")).join("")}
  <!-- collines, rivière, lac -->
  <path d="M0 210 Q120 150 260 190 Q380 140 520 180 Q640 150 800 175 L800 300 L0 300 Z" fill="#8bb174"/>
  <path d="M700 178 Q620 220 520 230 Q420 240 360 270" stroke="#3f8fc4" stroke-width="10" fill="none"/>
  <ellipse cx="200" cy="268" rx="230" ry="40" fill="#3f8fc4"/>
  ${[0,1,2].map(i=>`<path d="M${120+i*60} ${258+i*6} q10 -4 20 0" stroke="#bfe0f2" stroke-width="2" fill="none"/>`).join("")}
  <!-- vapeur invisible : seulement des flèches pointillées qui montent du lac -->
  ${[0,1,2].map(i=>`<path d="M${150+i*60} 240 L${170+i*60} 140" stroke="#c0392b" stroke-width="2" stroke-dasharray="4 6" opacity=".55"><animate attributeName="stroke-dashoffset" values="20;0" dur="1.5s" repeatCount="indefinite"/></path>`).join("")}
  <!-- fenêtre de la tour (cadre) et bassin d'essai -->
  <rect x="0" y="0" width="800" height="300" fill="none" stroke="#6f5a48" stroke-width="22"/>
  <rect x="300" y="236" width="200" height="50" rx="10" fill="#9aa9b4" stroke="#5c666e" stroke-width="3"/>
  <rect x="308" y="244" width="184" height="34" rx="6" fill="#7fb8e6"/>
  <rect x="340" y="236" width="18" height="12" fill="#c49a6c"/><rect x="420" y="240" width="14" height="10" fill="#dff1fb" stroke="#3b88b5"/>
</svg>`
};

window.SVG_DECORS = SVG_DECORS;

window.SALLE_NUM = SALLE_NUM;
