/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de « Le Grand Prix de l'observatoire »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux (un plateau imaginaire, au pied d'un observatoire, le matin du Grand Prix) :
     depart    la ligne de départ (piste, plots renversés, décamètre, banderole)
     stand     le stand des chronométreurs (tente, horloge, chronomètres, caisse à savon)
     tableau   le tableau des temps (panneau, tribune, vélos)
     coupole   la coupole de l'observatoire (lunette, vue sur le circuit, manège, grande roue)
     quai      le quai du petit train (locomotive, wagons, pupitre du chronomètre officiel)
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["depart"];
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

const SALLE_NUM = { "depart":1, "stand":2, "tableau":3, "coupole":4, "quai":5 };

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

const PLOT = (x, y, couche=false) => couche
  ? `<g transform="translate(${x},${y}) rotate(80)"><polygon points="-10,10 10,10 3,-18 -3,-18" fill="#f28c28"/><rect x="-10" y="-4" width="20" height="4" fill="#fff"/></g>`
  : `<g transform="translate(${x},${y})"><polygon points="-10,10 10,10 3,-18 -3,-18" fill="#f28c28"/><rect x="-6" y="-6" width="12" height="4" fill="#fff"/></g>`;
const DAMIER = (x, y, n=8, t=10) => Array.from({length:n*2},(_,k)=>`<rect x="${x+(k%n)*t}" y="${y+Math.floor(k/n)*t}" width="${t}" height="${t}" fill="${(k%n + Math.floor(k/n))%2 ? "#fff" : "#222"}"/>`).join("");
const COUPOLE_LOIN = (x, y, k=1) => `<g transform="translate(${x},${y}) scale(${k})"><rect x="-30" y="0" width="60" height="40" fill="#f4f4f0" stroke="#9aa4ad"/><path d="M-34 0 Q-34 -38 0 -38 Q34 -38 34 0 Z" fill="#f8f8f4" stroke="#9aa4ad" stroke-width="2"/><rect x="-4" y="-38" width="8" height="38" fill="#3d4a55"/></g>`;

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — La ligne de départ
   ------------------------------------------------------------ */
"depart": `${SVG_OUV()}
  <defs>${CIEL_JOUR("cielD")}</defs>
  <rect width="800" height="300" fill="url(#cielD)"/>
  ${NUAGE(160, 50, 1, "70s")}${NUAGE(600, 70, .8, "60s")}
  <path d="M0 170 Q200 120 400 150 Q600 110 800 150 L800 300 L0 300 Z" fill="#9cc77a"/>
  ${COUPOLE_LOIN(660, 118, .9)}
  <!-- la piste qui descend -->
  <path d="M260 300 L360 160 L440 160 L640 300 Z" fill="#7b7b7b"/>
  <path d="M400 160 L450 300" stroke="#fff" stroke-width="3" stroke-dasharray="14 12"/>
  <!-- banderole de départ qui flotte -->
  <line x1="330" y1="80" x2="330" y2="170" stroke="#5c3a1e" stroke-width="5"/><line x1="470" y1="80" x2="470" y2="170" stroke="#5c3a1e" stroke-width="5"/>
  <g><path d="M330 84 Q400 96 470 84 L470 112 Q400 124 330 112 Z" fill="#c0392b"/>
    <text x="400" y="108" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="#fff">DÉPART</text>
    <animateTransform attributeName="transform" type="translate" values="0 0;0 3;0 0" dur="2.5s" repeatCount="indefinite"/></g>
  ${DAMIER(362, 166, 8, 10)}
  <!-- plots renversés par le vent -->
  ${PLOT(250, 262, true)}${PLOT(300, 228)}${PLOT(560, 250, true)}${PLOT(520, 212)}${PLOT(150, 280, true)}
  <!-- décamètre jaune dans l'herbe -->
  <circle cx="110" cy="236" r="20" fill="#f7d04a" stroke="#8a6d0b" stroke-width="3"/><circle cx="110" cy="236" r="6" fill="#8a6d0b"/>
  <path d="M128 244 Q180 262 240 258" stroke="#f7d04a" stroke-width="6" fill="none"/>
  <!-- feuilles de mesure qui s'envolent -->
  ${[0,1,2].map(i=>`<rect x="${620+i*40}" y="${210-i*30}" width="16" height="20" fill="#fff" stroke="#9aa4ad"><animateTransform attributeName="transform" type="translate" values="0 0;${30+i*10} -${20+i*8};0 0" dur="${5+i}s" repeatCount="indefinite"/></rect>`).join("")}
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — Le stand des chronométreurs
   ------------------------------------------------------------ */
"stand": `${SVG_OUV()}
  <defs>${CIEL_JOUR("cielS")}</defs>
  <rect width="800" height="300" fill="url(#cielS)"/>
  ${NUAGE(620, 50, .9, "65s")}
  <rect y="220" width="800" height="80" fill="#9cc77a"/>
  <!-- la tente rayée -->
  <polygon points="80,90 520,90 560,130 40,130" fill="#c0392b"/>
  ${[0,1,2,3,4,5,6,7,8,9,10].map(i=>`<polygon points="${80+i*40},90 ${100+i*40},90 ${104+i*44},130 ${82+i*44},130" fill="#fff"/>`).join("")}
  <rect x="50" y="130" width="8" height="100" fill="#8a949c"/><rect x="542" y="130" width="8" height="100" fill="#8a949c"/>
  <!-- la grande horloge -->
  <circle cx="300" cy="60" r="0" fill="none"/>
  <g transform="translate(680,120)"><circle r="46" fill="#fff" stroke="#23406e" stroke-width="6"/>
    ${Array.from({length:12},(_,i)=>`<line x1="0" y1="-38" x2="0" y2="-32" stroke="#23406e" stroke-width="3" transform="rotate(${i*30})"/>`).join("")}
    <line x1="0" y1="0" x2="0" y2="-24" stroke="#23406e" stroke-width="5" transform="rotate(330)"/>
    <line x1="0" y1="0" x2="0" y2="-34" stroke="#c0392b" stroke-width="3"><animateTransform attributeName="transform" type="rotate" values="0;360" dur="60s" repeatCount="indefinite"/></line></g>
  <rect x="676" y="166" width="8" height="64" fill="#5c666e"/>
  <!-- table : chronomètres et sablier -->
  <rect x="120" y="180" width="320" height="10" fill="#7a4b2a"/><rect x="130" y="190" width="8" height="40" fill="#7a4b2a"/><rect x="422" y="190" width="8" height="40" fill="#7a4b2a"/>
  ${[170,240,310].map(x=>`<g><circle cx="${x}" cy="164" r="15" fill="#e6ecf6" stroke="#23406e" stroke-width="3"/><rect x="${x-3}" y="144" width="6" height="6" fill="#23406e"/><line x1="${x}" y1="164" x2="${x}" y2="154" stroke="#c0392b" stroke-width="2"/></g>`).join("")}
  <g transform="translate(390,152)"><polygon points="-12,-14 12,-14 2,0 12,14 -12,14 -2,0" fill="#f6e3b0" stroke="#7a4b2a" stroke-width="2"/></g>
  <!-- la caisse à savon rouge -->
  <g transform="translate(560,232)"><rect x="0" y="-26" width="120" height="26" rx="6" fill="#c0392b"/><rect x="18" y="-40" width="40" height="14" fill="#8e2a1f"/>
    <circle cx="20" cy="2" r="12" fill="#333"/><circle cx="100" cy="2" r="12" fill="#333"/><text x="80" y="-8" font-family="Arial" font-size="13" font-weight="700" fill="#fff">7</text></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — Le tableau des temps
   ------------------------------------------------------------ */
"tableau": `${SVG_OUV()}
  <defs>${CIEL_JOUR("cielT")}</defs>
  <rect width="800" height="300" fill="url(#cielT)"/>
  ${NUAGE(120, 40, .8, "60s")}
  <rect y="226" width="800" height="74" fill="#9cc77a"/>
  <!-- la tribune -->
  ${[0,1,2,3].map(i=>`<rect x="${500+i*14}" y="${150+i*20}" width="${260-i*28}" height="20" fill="${i%2?"#b5654a":"#c9a227"}"/>`).join("")}
  <!-- le grand panneau noir -->
  <rect x="80" y="60" width="360" height="160" rx="6" fill="#26352b" stroke="#7a4b2a" stroke-width="10"/>
  <text x="260" y="92" text-anchor="middle" font-family="Georgia,serif" font-size="20" fill="#f4f4f0">TABLEAU DES TEMPS</text>
  ${[0,1,2,3].map(i=>`<line x1="110" y1="${118+i*26}" x2="${300+((i*53)%110)}" y2="${118+i*26}" stroke="#e8efe8" stroke-width="3" stroke-dasharray="${8+i*2} 6" opacity=".8"/>`).join("")}
  <rect x="96" y="214" width="40" height="8" fill="#f4f4f0"/>
  <!-- vélos appuyés contre la barrière -->
  <rect x="440" y="214" width="360" height="6" fill="#8a949c"/>
  ${[560,680].map(x=>`<g><circle cx="${x}" cy="252" r="22" fill="none" stroke="#333" stroke-width="4"/><circle cx="${x+60}" cy="252" r="22" fill="none" stroke="#333" stroke-width="4"/><path d="M${x} 252 L${x+24} 222 L${x+50} 222 L${x+60} 252 M${x+24} 222 L${x+30} 252 L${x} 252" stroke="#2e8b57" stroke-width="5" fill="none"/></g>`).join("")}
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — La coupole de l'observatoire
   ------------------------------------------------------------ */
"coupole": `${SVG_OUV()}
  <rect width="800" height="300" fill="#1a2440"/>
  <!-- la fente du toit, ouverte sur le ciel et le circuit -->
  <path d="M260 0 L540 0 L520 210 L280 210 Z" fill="#9cc7e4"/>
  <path d="M280 160 Q400 120 520 150 L520 210 L280 210 Z" fill="#9cc77a"/>
  <path d="M290 200 L380 200 Q420 200 430 170 Q440 146 510 146" stroke="#6b6b6b" stroke-width="8" fill="none"/>
  <!-- la grande roue qui tourne, le manège -->
  <g transform="translate(470,120)"><circle r="26" fill="none" stroke="#c0392b" stroke-width="3"/>
    <g>${[0,1,2,3,4,5].map(i=>`<line x1="0" y1="0" x2="0" y2="-26" stroke="#c0392b" stroke-width="1.5" transform="rotate(${i*60})"/><circle cx="0" cy="-26" r="4" fill="#f2c230" transform="rotate(${i*60})"/>`).join("")}
    <animateTransform attributeName="transform" type="rotate" values="0;360" dur="20s" repeatCount="indefinite"/></g></g>
  <line x1="470" y1="120" x2="458" y2="160" stroke="#8e2a1f" stroke-width="3"/><line x1="470" y1="120" x2="482" y2="160" stroke="#8e2a1f" stroke-width="3"/>
  <ellipse cx="340" cy="176" rx="22" ry="7" fill="#b06a2b"/>
  <!-- étoiles peintes sur le dôme -->
  ${[[60,40],[140,90],[200,30],[620,50],[700,110],[740,30],[90,160],[660,180]].map(([x,y],i)=>`<circle cx="${x}" cy="${y}" r="2.5" fill="#ffe9a8"><animate attributeName="opacity" values=".3;1;.3" dur="${2+i*0.4}s" repeatCount="indefinite"/></circle>`).join("")}
  <!-- le plancher et la grande lunette -->
  <rect y="230" width="800" height="70" fill="#3d4a55"/>
  <g transform="translate(400,236)"><rect x="-8" y="-60" width="16" height="60" fill="#5b6b7b"/><rect x="-90" y="-110" width="170" height="30" rx="14" fill="#d9dde3" stroke="#5b6b7b" stroke-width="3" transform="rotate(-25)"/></g>
  <!-- le grand écran du système solaire -->
  <rect x="610" y="190" width="150" height="90" rx="6" fill="#10172e" stroke="#9aa4ad" stroke-width="4"/>
  <circle cx="685" cy="235" r="9" fill="#ffcc33"/><ellipse cx="685" cy="235" rx="50" ry="28" fill="none" stroke="#6f7fb8" stroke-width="1.5"/>
  <circle cx="735" cy="235" r="5" fill="#3b82c4"><animateTransform attributeName="transform" type="rotate" values="0 685 235;360 685 235" dur="12s" repeatCount="indefinite"/></circle>
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — Le quai du petit train
   ------------------------------------------------------------ */
"quai": `${SVG_OUV()}
  <defs>${CIEL_JOUR("cielQ")}</defs>
  <rect width="800" height="300" fill="url(#cielQ)"/>
  ${NUAGE(300, 50, 1, "75s")}
  <path d="M0 170 Q200 130 400 160 Q600 130 800 160 L800 220 L0 220 Z" fill="#9cc77a"/>
  ${COUPOLE_LOIN(120, 130, .7)}
  <!-- arbres qui défilent derrière le train -->
  <g>${[0,1,2,3,4,5].map(i=>`<g transform="translate(${80+i*150},178)"><rect x="-4" y="0" width="8" height="24" fill="#7a4b2a"/><circle cx="0" cy="-8" r="20" fill="#4f8a3a"/></g>`).join("")}
    <animateTransform attributeName="transform" type="translate" values="0 0;-150 0" dur="6s" repeatCount="indefinite"/></g>
  <!-- rails et quai de bois -->
  <rect y="230" width="800" height="8" fill="#6b6b6b"/>${Array.from({length:20},(_,i)=>`<rect x="${i*40}" y="236" width="24" height="6" fill="#7a4b2a"/>`).join("")}
  <rect y="248" width="800" height="52" fill="#b08a5a"/>${Array.from({length:16},(_,i)=>`<line x1="${i*50}" y1="248" x2="${i*50}" y2="300" stroke="#8a6a3a" stroke-width="2"/>`).join("")}
  <!-- la locomotive verte et deux wagons -->
  <g transform="translate(200,170)"><rect x="0" y="10" width="140" height="50" rx="6" fill="#2e7d32"/><rect x="90" y="-16" width="50" height="40" rx="4" fill="#2e7d32"/><rect x="100" y="-8" width="30" height="20" fill="#d9eef8"/>
    <rect x="20" y="-10" width="18" height="24" fill="#1c2a30"/><circle cx="29" cy="-18" r="8" fill="#e6ecf6" opacity=".8"><animate attributeName="cy" values="-18;-50" dur="2.5s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0" dur="2.5s" repeatCount="indefinite"/></circle>
    ${[24,70,116].map(x=>`<circle cx="${x}" cy="62" r="12" fill="#333"/>`).join("")}</g>
  ${[0,1].map(i=>`<g transform="translate(${350+i*140},180)"><rect x="0" y="0" width="128" height="50" rx="6" fill="#c0392b"/><rect x="10" y="8" width="48" height="24" fill="#d9eef8"/><rect x="70" y="8" width="48" height="24" fill="#d9eef8"/><circle cx="24" cy="52" r="10" fill="#333"/><circle cx="104" cy="52" r="10" fill="#333"/></g>`).join("")}
  <!-- le pupitre du chronomètre officiel -->
  <rect x="660" y="214" width="90" height="36" rx="4" fill="#3d4a55"/><circle cx="705" cy="200" r="22" fill="#e6ecf6" stroke="#c9a227" stroke-width="5"/>
  <rect x="699" y="172" width="12" height="8" fill="#c9a227"/><line x1="705" y1="200" x2="705" y2="186" stroke="#c0392b" stroke-width="3"/>
  ${[0,1,2,3,4].map(i=>`<rect x="${668+i*16}" y="226" width="12" height="16" rx="2" fill="#cfd6dc"/>`).join("")}
</svg>`
};

window.SVG_DECORS = SVG_DECORS;

window.SALLE_NUM = SALLE_NUM;
