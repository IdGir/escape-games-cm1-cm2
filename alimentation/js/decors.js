/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 lieux de « Le Grand Repas du chef »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq lieux (le restaurant Le Grand Couvert, la veille d'une étape) :
     potager       la cour du potager et du poulailler (Caramel)
     menus         la salle des menus (tableau, fiches, balance)
     degustation   la table de dégustation (pain, pommes, moulage de mâchoire)
     cabinet       le cabinet du Grand Tunnel (maquette du corps)
     entrainement  la salle d'entraînement (home-trainer, pouls)
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - clé de SVG_DECORS
 * @param {object} contenu - {lieu, description, sens:[]}
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["degustation"];
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

const SALLE_NUM = { "potager":1, "menus":2, "degustation":3, "cabinet":4, "entrainement":5 };

/* ---- Fragments communs ---- */
const CIEL_JOUR = `
  <linearGradient id="cielJour" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#8fc1e3"/><stop offset="70%" stop-color="#e3f0e6"/><stop offset="100%" stop-color="#f3efdc"/>
  </linearGradient>`;
const NUAGES = `
  <g opacity=".7">
    <ellipse cx="140" cy="40" rx="58" ry="13" fill="#fff"><animate attributeName="cx" values="120;700;120" dur="110s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="580" cy="28" rx="42" ry="10" fill="#fff"><animate attributeName="cx" values="560;-60;560" dur="140s" repeatCount="indefinite"/></ellipse>
  </g>`;
/* Une poule (x, y, échelle, sens 1 ou -1), qui picore */
const POULE = (x, y, k=1, sens=1, c="#c96a2a", dur="2.4s") => `<g transform="translate(${x},${y}) scale(${k*sens},${k})">
  <ellipse cx="0" cy="0" rx="20" ry="14" fill="${c}"/><path d="M-18 -4 Q-30 -18 -22 -22 Q-16 -10 -12 -8 Z" fill="${c}"/>
  <path d="M-4 4 Q4 -2 12 4" stroke="#7a3a12" stroke-width="2" fill="none"/>
  <g><circle cx="16" cy="-12" r="8" fill="${c}"/><path d="M14 -20 q2 -6 4 0 q2 -5 4 1" fill="#c0392b"/><path d="M23 -12 l7 2 l-7 2 Z" fill="#e0a020"/><circle cx="18" cy="-14" r="1.5" fill="#1a1a1a"/>
    <animateTransform attributeName="transform" type="rotate" values="0 10 -6;0 10 -6;38 10 -6;0 10 -6" keyTimes="0;.6;.75;1" dur="${dur}" repeatCount="indefinite"/></g>
  <g stroke="#d08a20" stroke-width="2"><line x1="-4" y1="12" x2="-6" y2="22"/><line x1="4" y1="12" x2="6" y2="22"/></g></g>`;
/* Une horloge murale dont l'aiguille tourne (x, y, r) */
const HORLOGE = (x, y, r=20) => `<g transform="translate(${x},${y})"><circle r="${r}" fill="#fbf8ef" stroke="#3d4f5a" stroke-width="3"/>
  ${[0,1,2,3,4,5,6,7,8,9,10,11].map(i=>`<line x1="0" y1="${-r+3}" x2="0" y2="${-r+6}" stroke="#3d4f5a" transform="rotate(${i*30})"/>`).join("")}
  <line x1="0" y1="0" x2="0" y2="${-r*.5}" stroke="#1f2a30" stroke-width="2.5" stroke-linecap="round" transform="rotate(60)"/>
  <line x1="0" y1="0" x2="0" y2="${-r*.8}" stroke="#a8432a" stroke-width="1.5" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" values="0;360" dur="60s" repeatCount="indefinite"/></line></g>`;
/* Vapeur qui monte d'un plat (x, y) */
const VAPEUR = (x, y) => `<g stroke="#ffffff" stroke-width="3" fill="none" opacity=".7" stroke-linecap="round">
  ${[0,1,2].map(i=>`<path d="M${x-10+i*10} ${y} q-6 -10 0 -20 q6 -10 0 -20"><animate attributeName="opacity" values="0;.8;0" dur="${3+i*.7}s" repeatCount="indefinite"/><animateTransform attributeName="transform" type="translate" values="0 6;0 -6" dur="${3+i*.7}s" repeatCount="indefinite"/></path>`).join("")}</g>`;

const SVG_DECORS = {

/* ------------------------------------------------------------
   SALLE 1 — La cour du potager et du poulailler
   ------------------------------------------------------------ */
"potager": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>${CIEL_JOUR}
    <linearGradient id="herbeP" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#9cc46a"/><stop offset="100%" stop-color="#6e9a44"/></linearGradient>
    <radialGradient id="lampeP" cx="50%" cy="0%" r="90%"><stop offset="0%" stop-color="#ffd27a" stop-opacity=".75"/><stop offset="100%" stop-color="#ffd27a" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="800" height="300" fill="url(#cielJour)"/>
  ${NUAGES}
  <circle cx="700" cy="48" r="24" fill="#ffe08a"><animate attributeName="r" values="23;26;23" dur="6s" repeatCount="indefinite"/></circle>
  <!-- mur du restaurant et porte de la cuisine, avec les marques de la toise de Lou -->
  <rect x="0" y="40" width="190" height="200" fill="#e9dcc2" stroke="#b9a582"/>
  <rect x="0" y="34" width="196" height="12" fill="#a8432a"/>
  <rect x="40" y="96" width="74" height="144" fill="#7a5a3a" stroke="#4e3722" stroke-width="3"/>
  <g stroke="#f6efe0" stroke-width="2">${[0,1,2,3,4].map(i=>`<line x1="54" y1="${190-i*16}" x2="${74+i*2}" y2="${190-i*16}"/>`).join("")}</g>
  <circle cx="104" cy="170" r="4" fill="#d9a21b"/>
  <rect x="130" y="80" width="44" height="40" fill="#bfe0ee" stroke="#7a5a3a" stroke-width="4"/>
  <!-- sol -->
  <rect y="210" width="800" height="90" fill="url(#herbeP)"/>
  <!-- potager : rangs de salades et de carottes -->
  <g transform="translate(206,212)">
    ${[0,1,2].map(r=>`<rect x="${r*8}" y="${r*26}" width="176" height="16" rx="6" fill="#7a5532"/>`).join("")}
    ${[0,1,2,3,4].map(i=>`<g transform="translate(${18+i*34},6)"><circle r="10" fill="#7dbb4a"/><circle r="6" fill="#a6d672"/></g>`).join("")}
    ${[0,1,2,3,4,5].map(i=>`<g transform="translate(${24+i*26},32)"><path d="M0 0 l-3 -12 M0 0 l3 -13 M0 0 l0 -14" stroke="#4f8a2a" stroke-width="2.5"><animateTransform attributeName="transform" type="rotate" values="-4;4;-4" dur="${3+i%3}s" repeatCount="indefinite"/></path><path d="M-4 0 L0 9 L4 0 Z" fill="#e07a1e"/></g>`).join("")}
    ${[0,1,2,3].map(i=>`<g transform="translate(${30+i*38},58)"><circle r="8" fill="#c0392b"/><path d="M0 -8 l-4 -5 M0 -8 l4 -5" stroke="#3f7a2a" stroke-width="2"/></g>`).join("")}
  </g>
  <!-- poulailler en bois -->
  <g transform="translate(560,96)">
    <path d="M-10 40 L80 -6 L170 40 Z" fill="#a8432a" stroke="#6b2a18" stroke-width="2"/>
    <rect x="0" y="40" width="160" height="96" fill="#b8874a" stroke="#6b4a2b" stroke-width="2"/>
    <g stroke="#8a6234" stroke-width="1.5">${[0,1,2,3,4,5].map(i=>`<line x1="0" y1="${52+i*16}" x2="160" y2="${52+i*16}"/>`).join("")}</g>
    <rect x="60" y="78" width="40" height="58" rx="4" fill="#4e3722"/>
    <path d="M60 136 L40 160 L120 160 L100 136" fill="#c9a26a" opacity=".8"/>
  </g>
  ${POULE(520,262,1,1,"#c96a2a","2.4s")}
  ${POULE(650,272,.9,-1,"#e8e2d0","3.1s")}
  ${POULE(760,262,1.05,-1,"#8a4a24","2.8s")}
  <!-- Caramel, le poussin, sous sa lampe chauffante -->
  <g transform="translate(440,232)">
    <line x1="0" y1="-120" x2="0" y2="-62" stroke="#3a3a3a" stroke-width="2"/>
    <path d="M-16 -62 L16 -62 L10 -50 L-10 -50 Z" fill="#3d4f5a"/>
    <path d="M-10 -50 L-60 26 L60 26 L10 -50 Z" fill="url(#lampeP)"><animate attributeName="opacity" values=".7;1;.7" dur="3s" repeatCount="indefinite"/></path>
    <g><ellipse cx="0" cy="12" rx="13" ry="10" fill="#f6d04a"/><circle cx="10" cy="0" r="8" fill="#f6d04a"/><path d="M17 0 l6 2 l-6 2 Z" fill="#e08a1e"/><circle cx="12" cy="-2" r="1.6" fill="#1a1a1a"/>
      <g stroke="#e08a1e" stroke-width="2"><line x1="-4" y1="21" x2="-5" y2="27"/><line x1="4" y1="21" x2="5" y2="27"/></g>
      <animateTransform attributeName="transform" type="translate" values="-30 0;30 0;30 0;-30 0;-30 0" keyTimes="0;.4;.5;.9;1" dur="9s" repeatCount="indefinite"/></g>
    <ellipse cx="-30" cy="28" rx="16" ry="4" fill="#c9a26a"/><text x="-30" y="44" text-anchor="middle" font-size="9" fill="#2f3a20" font-family="Georgia,serif">graines</text>
  </g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 2 — La salle des menus
   ------------------------------------------------------------ */
"menus": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murM" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e8eef0"/><stop offset="100%" stop-color="#c9d6da"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murM)"/>
  <rect y="236" width="800" height="64" fill="#8a6440"/>
  <g stroke="#6b4a2b" opacity=".5">${[0,1,2,3,4,5,6,7,8].map(i=>`<line x1="${i*100}" y1="236" x2="${i*100+40}" y2="300"/>`).join("")}</g>
  <rect y="226" width="800" height="10" fill="#2b5d6b"/>
  <!-- grand tableau noir des menus -->
  <g transform="translate(150,30)">
    <rect width="320" height="170" rx="6" fill="#26383a" stroke="#8a6440" stroke-width="10"/>
    <text x="160" y="32" text-anchor="middle" font-size="20" fill="#f6efe0" font-family="Georgia,serif" font-style="italic">Menus de la semaine</text>
    <g stroke="#e9e4d4" stroke-width="2" opacity=".85">
      <line x1="24" y1="56" x2="150" y2="56"/><line x1="24" y1="76" x2="132" y2="76"/><line x1="24" y1="96" x2="144" y2="96"/><line x1="24" y1="116" x2="120" y2="116"/>
    </g>
    <!-- petit diagramme en barres dessiné à la craie -->
    <g transform="translate(184,146)">
      <line x1="0" y1="0" x2="116" y2="0" stroke="#e9e4d4" stroke-width="2"/>
      ${[[0,34,"#f6e08a"],[30,44,"#bfe0ee"],[60,52,"#f2b6a0"],[90,96,"#f6d04a"]].map(([x,h,c],i)=>`<rect x="${x+6}" y="${-h}" width="18" height="${h}" fill="none" stroke="${c}" stroke-width="2.5"><animate attributeName="height" values="0;${h};${h}" keyTimes="0;.3;1" dur="8s" begin="${i*.4}s" repeatCount="indefinite"/><animate attributeName="y" values="0;${-h};${-h}" keyTimes="0;.3;1" dur="8s" begin="${i*.4}s" repeatCount="indefinite"/></rect>`).join("")}
    </g>
    <!-- craie qui écrit -->
    <g><rect x="-4" y="-2" width="16" height="5" rx="2" fill="#ffffff"/><animateMotion dur="6s" repeatCount="indefinite" path="M24 136 L120 136 L120 136"/></g>
  </g>
  <!-- fiches épinglées -->
  ${[[520,46,-4],[600,58,5],[680,44,-2]].map(([x,y,r],i)=>`<g transform="translate(${x},${y}) rotate(${r})"><rect width="62" height="78" fill="#fbf8ef" stroke="#c9c0ad"/><circle cx="31" cy="6" r="4" fill="${["#a8432a","#2b5d6b","#d9a21b"][i]}"/>
    <g stroke="#9a9384"><line x1="8" y1="22" x2="54" y2="22"/><line x1="8" y1="32" x2="48" y2="32"/><line x1="8" y1="42" x2="52" y2="42"/><line x1="8" y1="52" x2="40" y2="52"/></g></g>`).join("")}
  ${HORLOGE(80,70,24)}
  <!-- maillot de Basile accroché -->
  <g transform="translate(560,150)"><line x1="40" y1="-14" x2="40" y2="0" stroke="#5a5a5a" stroke-width="2"/><path d="M14 0 L66 0 L80 18 L68 26 L64 18 L64 70 L16 70 L16 18 L12 26 L0 18 Z" fill="#d9a21b" stroke="#a87a10"/><rect x="16" y="24" width="48" height="10" fill="#2b5d6b"/>
    <animateTransform attributeName="transform" type="rotate" values="-2 600 150;2 600 150;-2 600 150" dur="5s" repeatCount="indefinite" additive="sum"/></g>
  <!-- table : balance de cuisine, carnet, tasse -->
  <rect x="80" y="214" width="420" height="14" fill="#7a5532"/>
  <g transform="translate(160,186)"><rect x="-26" y="14" width="52" height="14" rx="3" fill="#3d4f5a"/><rect x="-14" y="18" width="28" height="7" rx="1" fill="#bfe0c9"/><ellipse cx="0" cy="10" rx="30" ry="6" fill="#c9d6da" stroke="#7a8a90"/></g>
  <g transform="translate(300,198)"><rect x="-30" y="0" width="60" height="16" fill="#7a5a3a"/><rect x="-26" y="-2" width="52" height="16" fill="#fbf8ef"/></g>
  <g transform="translate(420,196)"><rect x="-10" y="0" width="20" height="18" rx="3" fill="#ffffff" stroke="#8a8a8a"/><path d="M10 4 q8 0 8 6 q0 6 -8 6" stroke="#8a8a8a" fill="none"/>${VAPEUR(420,192).replace(/M(\d+) (\d+)/g,(m,a,b)=>`M${a-420} ${b-192}`)}</g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 3 — La table de dégustation (aussi l'écran d'accueil)
   ------------------------------------------------------------ */
"degustation": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murD" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f3e6cc"/><stop offset="100%" stop-color="#e0cba2"/></linearGradient>
    <linearGradient id="nappeD" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#ffffff"/><stop offset="100%" stop-color="#e9e6dc"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murD)"/>
  <!-- carrelage de cuisine en bas du mur -->
  <g>${Array.from({length:20},(_,i)=>`<rect x="${i*40}" y="150" width="40" height="40" fill="${i%2?"#d6e6e9":"#ffffff"}" stroke="#bccdd1"/>`).join("")}</g>
  <!-- fenêtre et passe-plat -->
  <g transform="translate(560,26)"><rect width="190" height="110" fill="#bfe0ee" stroke="#7a5a3a" stroke-width="6"/><line x1="95" y1="0" x2="95" y2="110" stroke="#7a5a3a" stroke-width="4"/><path d="M0 80 Q50 64 95 76 T190 70 L190 110 L0 110 Z" fill="#9cc46a"/></g>
  <!-- étagère : moulage de mâchoire, bocaux -->
  <rect x="60" y="100" width="300" height="8" fill="#7a5532"/>
  <g transform="translate(110,74)"><path d="M-30 24 Q-30 -10 0 -12 Q30 -10 30 24 L20 24 Q20 2 0 0 Q-20 2 -20 24 Z" fill="#e9a3a0" stroke="#b86f6c"/>
    ${[-24,-18,-11,-4,4,11,18,24].map((x,i)=>`<rect x="${x-3}" y="${Math.abs(x)<10?-12:Math.abs(x)<20?-6:4}" width="6" height="7" rx="2" fill="#fbf8ef" stroke="#7d7466" stroke-width=".8"/>`).join("")}</g>
  ${[[200,"#d9a21b"],[240,"#a8432a"],[280,"#4f8a2a"],[320,"#c0661c"]].map(([x,c])=>`<g transform="translate(${x},70)"><rect x="-12" y="0" width="24" height="30" rx="4" fill="#eaf3f5" stroke="#9ab6c9"/><rect x="-10" y="12" width="20" height="16" rx="3" fill="${c}" opacity=".85"/><rect x="-13" y="-5" width="26" height="6" rx="2" fill="#7a5a3a"/></g>`).join("")}
  <!-- la longue table nappée -->
  <path d="M30 200 L770 200 L790 236 L10 236 Z" fill="url(#nappeD)" stroke="#c9c4b4"/>
  <rect x="10" y="236" width="780" height="64" fill="#7a5532"/>
  <g stroke="#a8432a" stroke-width="3" opacity=".6"><line x1="30" y1="206" x2="770" y2="206"/></g>
  <!-- pain de campagne -->
  <g transform="translate(160,192)"><ellipse rx="56" ry="20" fill="#c08a4a" stroke="#7a5022"/><g stroke="#e9c48a" stroke-width="3"><path d="M-30 -6 l14 -8 M-6 -8 l14 -8 M18 -6 l14 -8"/></g></g>
  <g transform="translate(232,198)"><ellipse rx="16" ry="10" fill="#f3dcae" stroke="#c08a4a"/></g>
  <!-- assiette fumante -->
  <g transform="translate(390,196)"><ellipse rx="50" ry="12" fill="#ffffff" stroke="#b9c2c6"/><ellipse rx="34" ry="7" fill="#e07a1e"/><g fill="#4f8a2a"><circle cx="-12" cy="-2" r="3"/><circle cx="8" cy="0" r="3"/></g></g>
  ${VAPEUR(390,182)}
  <!-- coupe de pommes et carottes -->
  <g transform="translate(540,190)"><path d="M-40 0 Q0 26 40 0 Z" fill="#2b5d6b"/>
    ${[[-22,-6,"#c0392b"],[0,-10,"#8fbf3a"],[22,-6,"#c0392b"],[-10,-20,"#d94a3a"],[12,-20,"#a6c84a"]].map(([x,y,c])=>`<circle cx="${x}" cy="${y}" r="11" fill="${c}"/><path d="M${x} ${y-11} l2 -5" stroke="#5a3a1a" stroke-width="2"/>`).join("")}</g>
  <g transform="translate(660,198)">${[0,1,2].map(i=>`<g transform="rotate(${-20+i*12})"><path d="M0 0 L-60 -4 L-60 4 Z" fill="#e07a1e"/><path d="M0 0 l8 -6 M0 0 l9 0 M0 0 l8 6" stroke="#4f8a2a" stroke-width="2"/></g>`).join("")}</g>
  <!-- verre d'eau -->
  <g transform="translate(470,176)"><path d="M-10 0 L10 0 L8 26 L-8 26 Z" fill="#dff0f7" stroke="#8fb8c9"/><path d="M-9 8 L9 8 L8 26 L-8 26 Z" fill="#9fd0e6" opacity=".8"/></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 4 — Le cabinet du Grand Tunnel (maquette du corps)
   ------------------------------------------------------------ */
"cabinet": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murC" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#eaf2f4"/><stop offset="100%" stop-color="#cfdfe3"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murC)"/>
  <rect y="240" width="800" height="60" fill="#9aa5a8"/>
  <g stroke="#7f8a8d" opacity=".6">${[0,1,2,3,4,5,6,7,8,9,10].map(i=>`<line x1="${i*80}" y1="240" x2="${i*80}" y2="300"/>`).join("")}</g>
  <!-- affiches au mur : la bouchée qui voyage -->
  <g transform="translate(60,40)"><rect width="150" height="110" fill="#ffffff" stroke="#6f8f9a" stroke-width="3"/>
    <text x="75" y="20" text-anchor="middle" font-size="12" font-family="Georgia,serif" fill="#1d434e">Le voyage d'une bouchée</text>
    <g fill="#e48a72">${[0,1,2,3].map(i=>`<circle cx="${24+i*34}" cy="62" r="${12-i*2.5}"/>`).join("")}</g>
    <g stroke="#1d434e" stroke-width="2">${[0,1,2].map(i=>`<path d="M${38+i*34} 62 l10 0 m-4 -4 l4 4 l-4 4" fill="none"/>`).join("")}</g>
    <text x="75" y="98" text-anchor="middle" font-size="9" fill="#33464d">dur → mou → bouillie → liquide</text></g>
  ${HORLOGE(270,64,22)}
  <!-- étagère de livres -->
  <rect x="580" y="60" width="180" height="8" fill="#7a5532"/>
  ${[0,1,2,3,4,5,6,7].map(i=>`<rect x="${590+i*20}" y="${20+(i%3)*4}" width="16" height="${40-(i%3)*4}" fill="${["#2b5d6b","#a8432a","#d9a21b","#4f7a3a"][i%4]}" stroke="#2a2a2a" stroke-width=".6"/>`).join("")}
  <!-- bureau -->
  <rect x="380" y="200" width="380" height="14" fill="#7a5532"/><rect x="400" y="214" width="12" height="40" fill="#5e4128"/><rect x="730" y="214" width="12" height="40" fill="#5e4128"/>
  <g transform="translate(680,178)"><rect x="-26" y="0" width="52" height="22" fill="#fbf8ef" stroke="#c9c0ad"/><line x1="-18" y1="8" x2="18" y2="8" stroke="#9a9384"/><line x1="-18" y1="14" x2="12" y2="14" stroke="#9a9384"/></g>
  <!-- la maquette du corps (torse ouvert, simplifié) -->
  <g transform="translate(500,46)">
    <rect x="-40" y="150" width="80" height="10" rx="3" fill="#5e4128"/>
    <ellipse cx="0" cy="18" rx="22" ry="24" fill="#f3dcc4" stroke="#b98e6a" stroke-width="2"/>
    <path d="M-10 40 L-10 48 Q-38 52 -44 64 L-48 150 L48 150 L44 64 Q38 52 10 48 L10 40 Z" fill="#f3dcc4" stroke="#b98e6a" stroke-width="2"/>
    <path d="M-38 96 Q-36 84 -16 84 Q2 86 6 92 Q2 104 -10 108 Q-28 112 -36 104 Z" fill="#8f3b2e"/>
    <path d="M0 30 L0 52 Q0 74 4 90" stroke="#d98b6a" stroke-width="5" fill="none"/>
    <path d="M2 90 Q14 82 28 88 Q38 96 32 110 Q24 120 10 116 Q8 108 14 106 Q20 100 12 98 Q6 98 2 94 Z" fill="#e48a72" stroke="#a5513c"/>
    <path d="M-26 146 L-26 116 Q-26 110 -20 110 L22 112 Q28 112 28 118 L28 146" stroke="#c88a3a" stroke-width="8" fill="none" stroke-linejoin="round"/>
    <path d="M-8 120 q16 -4 16 4 q0 6 -16 6 q-16 0 -14 6 q2 6 18 4 q14 -2 14 4" stroke="#f2b6a0" stroke-width="5" fill="none" stroke-linecap="round"/>
    <!-- une petite bouchée qui voyage dans le tube -->
    <circle r="3.5" fill="#d9a21b" stroke="#7a5e10"><animateMotion dur="7s" repeatCount="indefinite" path="M0 30 L0 52 Q0 74 4 90 Q14 96 20 104 Q14 112 6 118 Q-8 124 0 130 Q10 134 -4 138"/></circle>
  </g>
  <!-- loupe -->
  <g transform="translate(440,186)"><circle r="12" fill="#dff0f7" stroke="#3d4f5a" stroke-width="3" opacity=".9"/><line x1="8" y1="8" x2="22" y2="18" stroke="#3d4f5a" stroke-width="4" stroke-linecap="round"/></g>
</svg>`,

/* ------------------------------------------------------------
   SALLE 5 — La salle d'entraînement (home-trainer et pouls)
   ------------------------------------------------------------ */
"entrainement": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
  <defs>
    <linearGradient id="murE" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e7eef3"/><stop offset="100%" stop-color="#c3d1db"/></linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#murE)"/>
  <rect y="246" width="800" height="54" fill="#3d4f5a"/>
  <rect x="0" y="240" width="800" height="6" fill="#d9a21b"/>
  <!-- grande fenêtre sur les montagnes -->
  <g transform="translate(40,30)"><rect width="300" height="150" fill="#cfe7f3" stroke="#5a6a72" stroke-width="6"/>
    <path d="M0 150 L60 70 L100 110 L160 40 L220 104 L260 74 L300 120 L300 150 Z" fill="#7d8f9a"/>
    <path d="M160 40 L176 58 L148 58 Z M60 70 L72 86 L50 84 Z" fill="#ffffff"/>
    <path d="M0 150 Q100 128 160 150 Z" fill="#7aa35a"/>
    <path d="M150 150 Q170 120 200 110 Q230 100 260 76" stroke="#f6efe0" stroke-width="3" fill="none" stroke-dasharray="6 5"/>
    <line x1="150" y1="0" x2="150" y2="150" stroke="#5a6a72" stroke-width="4"/></g>
  <!-- écran : vitesse et pouls -->
  <g transform="translate(400,40)"><rect width="170" height="100" rx="8" fill="#1f2a30" stroke="#5a6a72" stroke-width="4"/>
    <text x="16" y="30" font-size="13" fill="#9fd0e6" font-family="Arial,sans-serif">Vitesse</text>
    <text x="16" y="52" font-size="20" font-weight="bold" fill="#ffffff" font-family="Arial,sans-serif">28 km/h</text>
    <path d="M100 26 C92 16 80 22 88 32 L100 44 L112 32 C120 22 108 16 100 26 Z" fill="#e0393b"><animateTransform attributeName="transform" type="scale" values="1;1.12;1" dur=".8s" repeatCount="indefinite" additive="sum"/></path>
    <text x="126" y="40" font-size="14" font-weight="bold" fill="#ffffff" font-family="Arial,sans-serif">pouls</text>
    <path d="M12 82 L52 82 L60 66 L70 94 L78 74 L86 82 L158 82" stroke="#5be38a" stroke-width="2.5" fill="none" stroke-dasharray="220" stroke-dashoffset="220"><animate attributeName="stroke-dashoffset" values="220;0" dur="1.6s" repeatCount="indefinite"/></path></g>
  <!-- ventilateur -->
  <g transform="translate(690,160)"><line x1="0" y1="0" x2="0" y2="84" stroke="#5a6a72" stroke-width="5"/><ellipse cx="0" cy="86" rx="24" ry="6" fill="#5a6a72"/>
    <circle r="34" fill="#ffffff" stroke="#5a6a72" stroke-width="3" opacity=".9"/>
    <g fill="#9fd0e6">${[0,1,2].map(i=>`<path d="M0 0 Q12 -24 0 -30 Q-10 -20 0 0 Z" transform="rotate(${i*120})"/>`).join("")}<animateTransform attributeName="transform" type="rotate" values="0;360" dur="1s" repeatCount="indefinite"/></g>
    <circle r="5" fill="#3d4f5a"/></g>
  <!-- vélo de course sur home-trainer -->
  <g transform="translate(470,196)">
    <rect x="-36" y="40" width="72" height="12" rx="4" fill="#3d4f5a"/><path d="M-26 52 L-46 70 M26 52 L46 70" stroke="#3d4f5a" stroke-width="6"/><rect x="94" y="52" width="32" height="10" rx="3" fill="#3d4f5a"/>
    <circle cx="0" cy="22" r="32" fill="none" stroke="#1f2430" stroke-width="5"/>
    <circle cx="110" cy="22" r="32" fill="none" stroke="#1f2430" stroke-width="5"/>
    <g transform="translate(0,22)"><g stroke="#9aa5a8" stroke-width="1.2">${[0,1,2,3,4,5].map(i=>`<line x1="-30" y1="0" x2="30" y2="0" transform="rotate(${i*30})"/>`).join("")}<animateTransform attributeName="transform" type="rotate" values="0;360" dur="1.4s" repeatCount="indefinite"/></g></g>
    <g transform="translate(110,22)"><g stroke="#9aa5a8" stroke-width="1.2">${[0,1,2,3,4,5].map(i=>`<line x1="-30" y1="0" x2="30" y2="0" transform="rotate(${i*30})"/>`).join("")}<animateTransform attributeName="transform" type="rotate" values="0;360" dur="1.4s" repeatCount="indefinite"/></g></g>
    <path d="M0 22 L40 -20 L96 -20 L110 22 M40 -20 L54 22 L0 22 M54 22 L96 -20 M96 -20 L92 -34" stroke="#d9a21b" stroke-width="5" fill="none" stroke-linejoin="round"/>
    <path d="M30 -28 L52 -28" stroke="#1f2430" stroke-width="5" stroke-linecap="round"/><path d="M40 -20 L40 -28" stroke="#d9a21b" stroke-width="4"/>
    <path d="M86 -36 Q96 -42 104 -34" stroke="#1f2430" stroke-width="4" fill="none"/>
    <g transform="translate(54,22)"><line x1="0" y1="0" x2="14" y2="0" stroke="#1f2430" stroke-width="4"><animateTransform attributeName="transform" type="rotate" values="0;360" dur="1.4s" repeatCount="indefinite"/></line><circle r="7" fill="none" stroke="#1f2430" stroke-width="2"/></g>
  </g>
  <!-- gourde et serviette -->
  <g transform="translate(380,214)"><rect x="-8" y="0" width="16" height="30" rx="6" fill="#4aa3c8" stroke="#1d5f7a"/><rect x="-4" y="-6" width="8" height="7" rx="2" fill="#1f2430"/></g>
  <g transform="translate(300,232)"><rect x="-30" y="0" width="60" height="12" rx="3" fill="#a8432a"/><line x1="-30" y1="4" x2="30" y2="4" stroke="#ffffff" opacity=".5"/></g>
</svg>`
};


window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
window.SALLE_NUM = SALLE_NUM;
