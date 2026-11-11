/* ============================================================
   DÉCORS SVG ANIMÉS — les 5 salles de « Les Archives du port »
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (aucun fichier requis).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.jpg (ou .png)
     →  SVG    dessiné ci-dessous

   Les cinq salles (des archives imaginaires dans un port de l'Atlantique) :
     cartes     la salle des cartes (meubles à plans, lampe, carte de l'Atlantique)
     registres  le cabinet des registres (étagères, journal de bord, maquette de navire sous verre)
     colonies   le fonds des colonies (table de lecture, plan d'habitation, livre de lois sous vitre, pluie)
     musee      le musée du port (vitrines, barriques, sacs, carte de la côte)
     lecture    la salle de lecture (longues tables, frise, registre reconstitué)
   Sujet sensible : aucun personnage réduit en esclavage n'est dessiné, aucune scène de violence.
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

const SALLE_NUM = { "cartes":1, "registres":2, "colonies":3, "musee":4, "lecture":5 };

/* ---- Fragments communs ---- */
const SVG_OUV = (id) => `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">`;
const MUR = (id, c1, c2) => `<linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${c1}"/><stop offset="1" stop-color="${c2}"/></linearGradient>`;
const PARQUET = (y, c1="#7a5232", c2="#6a4428") => `<rect x="0" y="${y}" width="800" height="${300-y}" fill="${c1}"/>` +
  Array.from({length:16},(_,i)=>`<line x1="${i*52}" y1="${y}" x2="${i*52-30}" y2="300" stroke="${c2}" stroke-width="2"/>`).join("");
const LAMPE = (x, y) => `<g transform="translate(${x},${y})"><rect x="-4" y="0" width="8" height="34" fill="#5c4630"/><path d="M-26 0 L26 0 L16 -22 L-16 -22 Z" fill="#2f6b4a"/>
  <ellipse cx="0" cy="40" rx="60" ry="10" fill="#ffe8a8" opacity=".35"><animate attributeName="opacity" values=".28;.4;.28" dur="4s" repeatCount="indefinite"/></ellipse></g>`;
const ETAGERE = (x, y, w, n=4) => `<g transform="translate(${x},${y})"><rect x="0" y="0" width="${w}" height="${n*36+8}" fill="#5c3b22"/>` +
  Array.from({length:n},(_,r)=>Array.from({length:Math.floor(w/14)},(_,k)=>`<rect x="${4+k*14}" y="${8+r*36}" width="11" height="28" rx="1" fill="${["#7a2e1f","#2f4858","#6b4f2a","#3e5a3a","#8a6d45"][(k+r)%5]}"/>`).join("")).join("") +
  Array.from({length:n},(_,r)=>`<rect x="0" y="${36+r*36}" width="${w}" height="4" fill="#3b2414"/>`).join("") + `</g>`;
const POUSSIERE = (x0, y0) => [0,1,2,3,4,5].map(i=>`<circle cx="${x0+i*37}" cy="${y0+(i%3)*25}" r="1.6" fill="#fff4cf" opacity=".7"><animateTransform attributeName="transform" type="translate" values="0 0;${6+i} ${-14-i*2};0 0" dur="${7+i}s" repeatCount="indefinite"/></circle>`).join("");
const FENETRE = (x, y, pluie=false) => `<g transform="translate(${x},${y})"><rect x="0" y="0" width="110" height="130" fill="#9fb6c4" stroke="#4a3624" stroke-width="6"/><line x1="55" y1="0" x2="55" y2="130" stroke="#4a3624" stroke-width="4"/><line x1="0" y1="65" x2="110" y2="65" stroke="#4a3624" stroke-width="4"/>` +
  (pluie ? [10,30,50,70,90].map((dx,i)=>`<line x1="${dx}" y1="0" x2="${dx-6}" y2="16" stroke="#e8f2f8" stroke-width="1.5" opacity=".8"><animateTransform attributeName="transform" type="translate" values="0 -10;0 130" dur="${1.1+i*.15}s" repeatCount="indefinite"/></line>`).join("") : "") + `</g>`;

const SVG_DECORS = {

/* SALLE 1 — La salle des cartes */
"cartes": `${SVG_OUV()}
  <defs>${MUR("murC","#d9c9a8","#b9a47e")}</defs>
  <rect width="800" height="300" fill="url(#murC)"/>
  <!-- grande carte de l'Atlantique au mur -->
  <g transform="translate(250,24)"><rect x="0" y="0" width="300" height="160" fill="#efe2c4" stroke="#6b4f2a" stroke-width="8"/>
    <rect x="8" y="8" width="284" height="144" fill="#cfe0e6"/>
    <path d="M20 20 Q60 14 80 40 Q70 70 90 100 Q80 130 60 140 Q40 110 30 80 Z" fill="#e5d6b4"/>
    <path d="M220 18 Q260 14 270 40 Q250 54 228 50 Z M222 66 Q262 60 275 90 Q268 120 250 140 Q236 120 230 100 Q216 84 222 66 Z" fill="#e5d6b4"/>
    <path d="M232 46 Q190 60 226 74" fill="none" stroke="#2f4858" stroke-width="2" stroke-dasharray="5 4"/>
    <path d="M228 96 Q150 130 92 92" fill="none" stroke="#8c2f1c" stroke-width="2.5" stroke-dasharray="5 4"/>
    <path d="M84 60 Q150 20 232 40" fill="none" stroke="#3e5a3a" stroke-width="2" stroke-dasharray="5 4"/>
    <circle cx="150" cy="75" r="14" fill="none" stroke="#6b4f2a" stroke-width="1.5"/><path d="M150 61 L150 89 M136 75 L164 75" stroke="#6b4f2a" stroke-width="1"/></g>
  ${PARQUET(232)}
  <!-- meubles à plans -->
  ${[0,1].map(i=>`<g transform="translate(${40+i*600},150)"><rect x="0" y="0" width="120" height="84" fill="#6b4422"/>${[0,1,2,3].map(r=>`<rect x="6" y="${6+r*19}" width="108" height="15" fill="#7d5230" stroke="#4a2e18"/><rect x="52" y="${11+r*19}" width="16" height="4" fill="#c9a227"/>`).join("")}</g>`).join("")}
  <!-- table de consultation et page du registre -->
  <rect x="290" y="204" width="220" height="12" fill="#5c3b22"/><rect x="300" y="216" width="10" height="60" fill="#4a2e18"/><rect x="490" y="216" width="10" height="60" fill="#4a2e18"/>
  <g><rect x="360" y="190" width="70" height="14" fill="#f6eedb" stroke="#b9a47e" transform="rotate(-4 395 197)"/>
    <animateTransform attributeName="transform" type="translate" values="0 0;0 -1;0 0" dur="5s" repeatCount="indefinite"/></g>
  <g transform="translate(455,186)"><circle cx="0" cy="0" r="10" fill="none" stroke="#c9a227" stroke-width="3"/><circle cx="0" cy="0" r="7" fill="#cfe7f2" opacity=".6"/><line x1="7" y1="7" x2="18" y2="18" stroke="#5c3b22" stroke-width="4"/></g>
  ${LAMPE(330,166)}
  ${POUSSIERE(300,120)}
</svg>`,

/* SALLE 2 — Le cabinet des registres */
"registres": `${SVG_OUV()}
  <defs>${MUR("murR","#cdb994","#a88f66")}</defs>
  <rect width="800" height="300" fill="url(#murR)"/>
  ${ETAGERE(20,40,200)}${ETAGERE(580,40,200)}
  ${PARQUET(232,"#6e4a2c","#5c3d22")}
  <!-- maquette de navire sous verre -->
  <g transform="translate(300,70)"><rect x="0" y="0" width="200" height="110" rx="4" fill="#dfeef2" opacity=".55" stroke="#8a6d45" stroke-width="3"/>
    <path d="M30 80 L170 80 L155 98 L45 98 Z" fill="#5c3b22"/>
    <line x1="70" y1="80" x2="70" y2="18" stroke="#3b2414" stroke-width="3"/><line x1="105" y1="80" x2="105" y2="10" stroke="#3b2414" stroke-width="3"/><line x1="140" y1="80" x2="140" y2="24" stroke="#3b2414" stroke-width="3"/>
    ${[70,105,140].map((x,i)=>`<path d="M${x-18} ${26+i*2} Q${x} ${34} ${x+18} ${26+i*2} L${x+16} ${52} Q${x} ${58} ${x-16} ${52} Z" fill="#efe6d0"/>`).join("")}
    <rect x="0" y="110" width="200" height="16" fill="#5c3b22"/></g>
  <!-- pupitre et journal de bord ouvert -->
  <g transform="translate(330,196)"><path d="M0 0 L140 0 L130 36 L10 36 Z" fill="#5c3b22"/>
    <path d="M14 -6 Q70 -16 70 2 Q70 -16 126 -6 L124 10 Q70 0 70 14 Q70 0 16 10 Z" fill="#f6eedb" stroke="#b9a47e"/>
    ${[0,1,2].map(i=>`<line x1="${24}" y1="${-2+i*4}" x2="${62}" y2="${-4+i*4}" stroke="#8a7a5a"/><line x1="${78}" y1="${-4+i*4}" x2="${116}" y2="${-2+i*4}" stroke="#8a7a5a"/>`).join("")}</g>
  <!-- horloge du cabinet -->
  <g transform="translate(400,40)"><circle r="18" fill="#f6eedb" stroke="#6b4f2a" stroke-width="4"/>
    <line x1="0" y1="0" x2="0" y2="-12" stroke="#2b2118" stroke-width="2"><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="60s" repeatCount="indefinite"/></line>
    <line x1="0" y1="0" x2="8" y2="0" stroke="#2b2118" stroke-width="3"/></g>
  ${POUSSIERE(240,90)}
</svg>`,

/* SALLE 3 — Le fonds des colonies */
"colonies": `${SVG_OUV()}
  <defs>${MUR("murF","#d6c8ad","#b3a184")}</defs>
  <rect width="800" height="300" fill="url(#murF)"/>
  ${FENETRE(60,40,true)}${FENETRE(630,40,true)}
  ${PARQUET(232,"#7a5634","#684628")}
  <!-- plan d'habitation au mur (sans personnage) -->
  <g transform="translate(270,30)"><rect x="0" y="0" width="260" height="120" fill="#efe2c4" stroke="#6b4f2a" stroke-width="6"/>
    <rect x="12" y="12" width="96" height="96" fill="#b8cf8e"/>${Array.from({length:7},(_,i)=>`<line x1="${20+i*13}" y1="16" x2="${20+i*13}" y2="104" stroke="#6f8a45" stroke-width="2"/>`).join("")}
    ${[[120,14,40,30],[168,14,40,30],[216,14,34,30],[120,60,60,46],[188,60,62,46]].map(r=>`<rect x="${r[0]}" y="${r[1]}" width="${r[2]}" height="${r[3]}" fill="#d9c7a0" stroke="#6b4f2a"/>`).join("")}</g>
  <!-- table de lecture et livre de lois sous vitre -->
  <rect x="250" y="200" width="300" height="12" fill="#5c3b22"/><rect x="262" y="212" width="10" height="66" fill="#4a2e18"/><rect x="528" y="212" width="10" height="66" fill="#4a2e18"/>
  <g transform="translate(340,172)"><rect x="0" y="0" width="120" height="28" fill="#dfeef2" opacity=".5" stroke="#8a6d45" stroke-width="2"/>
    <path d="M8 24 Q60 10 60 24 Q60 10 112 24 L112 26 L8 26 Z" fill="#f2e6c8" stroke="#8a7a5a"/></g>
  ${LAMPE(500,166)}
</svg>`,

/* SALLE 4 — Le musée du port */
"musee": `${SVG_OUV()}
  <defs>${MUR("murM","#e6dccb","#c7b89e")}</defs>
  <rect width="800" height="300" fill="url(#murM)"/>
  <!-- carte de la côte -->
  <g transform="translate(320,30)"><rect x="0" y="0" width="160" height="110" fill="#efe2c4" stroke="#6b4f2a" stroke-width="5"/><rect x="6" y="6" width="148" height="98" fill="#cfe0e6"/>
    <path d="M70 10 Q110 8 140 30 Q150 60 138 90 Q110 100 86 96 Q70 70 60 50 Q48 36 70 10 Z" fill="#e5d6b4"/>
    ${[[72,16],[56,46],[62,62],[76,86]].map(p=>`<circle cx="${p[0]}" cy="${p[1]}" r="4" fill="#8c2f1c"/>`).join("")}</g>
  ${PARQUET(236,"#8a6a48","#77583a")}
  <!-- vitrines éclairées -->
  ${[0,1].map(i=>`<g transform="translate(${70+i*530},110)"><rect x="0" y="0" width="130" height="126" fill="#5c3b22"/><rect x="8" y="8" width="114" height="70" fill="#f4f0dc" opacity=".55"/>
    <rect x="22" y="44" width="26" height="30" rx="4" fill="#efe6d0" stroke="#8a6d45"/><circle cx="84" cy="62" r="12" fill="#6b3f22"/><rect x="62" y="66" width="44" height="10" fill="#2f4858"/>
    <rect x="8" y="8" width="114" height="70" fill="#fff8d0" opacity=".15"><animate attributeName="opacity" values=".1;.25;.1" dur="5s" repeatCount="indefinite"/></rect></g>`).join("")}
  <!-- barriques et sacs de toile -->
  ${[0,1,2].map(i=>`<g transform="translate(${290+i*62},${196})"><ellipse cx="26" cy="0" rx="26" ry="8" fill="#8a5a32"/><rect x="0" y="0" width="52" height="44" fill="#9a6a3c"/><ellipse cx="26" cy="44" rx="26" ry="8" fill="#7a4a26"/><rect x="0" y="12" width="52" height="4" fill="#4a3624"/><rect x="0" y="30" width="52" height="4" fill="#4a3624"/></g>`).join("")}
  ${[0,1].map(i=>`<path d="M${480+i*44} 244 Q${470+i*44} 214 ${490+i*44} 206 Q${510+i*44} 214 ${504+i*44} 244 Z" fill="#c9b48a" stroke="#8a6d45"/>`).join("")}
</svg>`,

/* SALLE 5 — La salle de lecture */
"lecture": `${SVG_OUV()}
  <defs>${MUR("murL","#efe6d2","#d2c3a3")}</defs>
  <rect width="800" height="300" fill="url(#murL)"/>
  ${[90,250,550,710].map(x=>`<rect x="${x-40}" y="20" width="80" height="140" rx="40" fill="#cfe3ee" stroke="#8a6d45" stroke-width="5"/><line x1="${x}" y1="20" x2="${x}" y2="160" stroke="#8a6d45" stroke-width="3"/>`).join("")}
  ${PARQUET(226,"#8a6a48","#77583a")}
  <!-- chevalet et frise inachevée -->
  <g transform="translate(330,40)"><line x1="20" y1="0" x2="0" y2="180" stroke="#5c3b22" stroke-width="6"/><line x1="120" y1="0" x2="140" y2="180" stroke="#5c3b22" stroke-width="6"/>
    <rect x="-6" y="16" width="152" height="70" fill="#fbf6e9" stroke="#8a6d45" stroke-width="3"/>
    <line x1="4" y1="56" x2="136" y2="56" stroke="#2b2118" stroke-width="2"/>${[14,40,62,84,116].map((x,i)=>`<circle cx="${x}" cy="56" r="4" fill="${i<2?"#8c2f1c":"#c9b48a"}"/>`).join("")}</g>
  <!-- longues tables et registre au fermoir -->
  <rect x="80" y="210" width="640" height="12" fill="#5c3b22"/>${[100,380,700].map(x=>`<rect x="${x}" y="222" width="10" height="56" fill="#4a2e18"/>`).join("")}
  <g transform="translate(372,176)"><rect x="0" y="0" width="64" height="34" rx="3" fill="#6b3f22" stroke="#3b2414" stroke-width="2"/><rect x="58" y="12" width="14" height="10" rx="2" fill="#c9a227"/>
    <circle cx="65" cy="17" r="2" fill="#5e3f10"><animate attributeName="fill" values="#5e3f10;#ffe27a;#5e3f10" dur="2.5s" repeatCount="indefinite"/></circle></g>
  ${LAMPE(170,176)}${LAMPE(630,176)}
  ${POUSSIERE(420,110)}
</svg>`
};

window.SVG_DECORS = SVG_DECORS;

window.SALLE_NUM = SALLE_NUM;
