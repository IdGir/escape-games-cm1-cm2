/* ============================================================
   DÉCORS SVG ANIMÉS — 5 salles immersives
   ------------------------------------------------------------
   Le décor SVG s'affiche IMMÉDIATEMENT (zéro attente, zéro fichier).
   Si l'enseignant dépose un média du même nom, js/media.js le fait
   passer devant, selon la cascade :

        VIDÉO  assets/videos/salle1.mp4   (ou .webm)
     →  IMAGE  assets/images/decors/salle1.png
     →  SVG    dessiné ci-dessous

   Le dossier « Elements EG/Revolution fr/ » est également exploré,
   et le fichier « Paris 1789.mp4 » y est reconnu comme décor de la
   salle 1 (voir la table ALIAS dans js/media.js).
   ============================================================ */

/**
 * Génère le HTML de la scène (décor) d'une salle.
 * @param {string} salle - 'palais-royal' | 'imprimerie' | 'tuileries' | 'bastille' | 'assemblee'
 * @param {object} contenu - {lieu, description, sens:[]}
 * @returns {string} HTML
 */
function htmlScene(salle, contenu){
  const svg = SVG_DECORS[salle] || SVG_DECORS["palais-royal"];
  const sens = (contenu.sens||[]).map(s=>`<span>${s}</span>`).join("");
  return `
    <div class="scene scene--media" data-salle="${salle}" data-media="salle${SALLE_NUM[salle]}">
      <div class="decor-fallback">${svg}</div>
      <div class="decor-overlay"></div>
      <div class="decor-contenu">
        <span class="lieu">${contenu.lieu||""}</span>
        <p class="description">${contenu.description||""}</p>
        ${sens?`<div class="sens">${sens}</div>`:""}
      </div>
    </div>`;
}

/**
 * Active la scène : lance la recherche du média (vidéo puis image).
 * Le SVG reste affiché tant que rien de mieux n'est trouvé.
 */
function activerScene(sceneEl){
  if(!sceneEl) return;
  if(typeof nettoyerVideos === "function") nettoyerVideos();
  const base = sceneEl.dataset.media;
  if(base && typeof installerDecor === "function"){
    installerDecor(sceneEl, base);
  }
}

const SALLE_NUM = {
  "palais-royal":1, "imprimerie":2, "tuileries":3, "bastille":4, "assemblee":5
};

/* ---- Bibliothèque des décors SVG ----
   Chaque décor : ciel/arrière-plan + éléments animés (pluie, bougie, fumée, pendule) */
const SVG_DECORS = {

  /* Salle 1 — Palais-Royal sous la pluie */
  "palais-royal": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
    <defs>
      <linearGradient id="cielPluie" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#4a5566"/>
        <stop offset="100%" stop-color="#6a7588"/>
      </linearGradient>
      <linearGradient id="paveHumide" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#3a3848"/>
        <stop offset="100%" stop-color="#5a5868"/>
      </linearGradient>
    </defs>
    <rect width="800" height="300" fill="url(#cielPluie)"/>
    <!-- Bâtiments Palais-Royal -->
    <rect x="0" y="60" width="220" height="200" fill="#6a5848"/>
    <rect x="200" y="40" width="180" height="220" fill="#7a6858"/>
    <rect x="560" y="50" width="240" height="210" fill="#6a5848"/>
    <rect x="380" y="100" width="180" height="160" fill="#8a7868"/>
    <!-- Toits -->
    <polygon points="0,60 110,30 220,60" fill="#3a2818"/>
    <polygon points="200,40 290,15 380,40" fill="#3a2818"/>
    <polygon points="380,100 470,75 560,100" fill="#3a2818"/>
    <!-- Fenêtres illuminées -->
    <rect x="40" y="100" width="18" height="28" fill="#e8c878" opacity=".8"/>
    <rect x="90" y="100" width="18" height="28" fill="#e8c878" opacity=".6"/>
    <rect x="140" y="100" width="18" height="28" fill="#1a1820"/>
    <rect x="240" y="80" width="18" height="28" fill="#e8c878" opacity=".7"/>
    <rect x="290" y="80" width="18" height="28" fill="#e8c878" opacity=".8"/>
    <rect x="340" y="80" width="18" height="28" fill="#1a1820"/>
    <rect x="610" y="90" width="18" height="28" fill="#e8c878" opacity=".6"/>
    <rect x="660" y="90" width="18" height="28" fill="#e8c878" opacity=".7"/>
    <rect x="710" y="90" width="18" height="28" fill="#1a1820"/>
    <rect x="760" y="90" width="18" height="28" fill="#e8c878" opacity=".5"/>
    <!-- Affiches révolutionnaires sur les murs -->
    <rect x="60" y="160" width="30" height="40" fill="#d8c898" transform="rotate(-3 75 180)"/>
    <rect x="320" y="150" width="28" height="38" fill="#d8c898" transform="rotate(2 334 169)"/>
    <rect x="640" y="160" width="30" height="42" fill="#d8c898" transform="rotate(-2 655 181)"/>
    <text x="75" y="180" font-size="7" fill="#3a1a1a" text-anchor="middle" transform="rotate(-3 75 180)">LIBERTÉ</text>
    <text x="334" y="172" font-size="7" fill="#3a1a1a" text-anchor="middle" transform="rotate(2 334 169)">1789</text>
    <!-- Pavés au sol -->
    <rect x="0" y="240" width="800" height="60" fill="url(#paveHumide)"/>
    <line x1="0" y1="255" x2="800" y2="255" stroke="#2a2838" stroke-width="1" opacity=".5"/>
    <line x1="0" y1="275" x2="800" y2="275" stroke="#2a2838" stroke-width="1" opacity=".5"/>
    <!-- Reflets sur pavés -->
    <ellipse cx="200" cy="270" rx="60" ry="6" fill="#fff" opacity=".08"/>
    <ellipse cx="500" cy="280" rx="80" ry="8" fill="#fff" opacity=".06"/>
    <!-- Silhouettes de passants -->
    <ellipse cx="180" cy="240" rx="8" ry="20" fill="#1a1820"/>
    <circle cx="180" cy="218" r="6" fill="#1a1820"/>
    <ellipse cx="420" cy="245" rx="7" ry="18" fill="#1a1820"/>
    <circle cx="420" cy="225" r="5" fill="#1a1820"/>
  </svg>
  <div class="pluie"></div>`,

  /* Salle 2 — Imprimerie clandestine, bougie */
  "imprimerie": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
    <defs>
      <radialGradient id="lumBougie" cx="75%" cy="60%" r="60%">
        <stop offset="0%" stop-color="#f8d878" stop-opacity=".4"/>
        <stop offset="50%" stop-color="#8a5828" stop-opacity=".2"/>
        <stop offset="100%" stop-color="#1a0808" stop-opacity="0"/>
      </radialGradient>
      <linearGradient id="murBois" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#3a2410"/>
        <stop offset="100%" stop-color="#2a1808"/>
      </linearGradient>
    </defs>
    <rect width="800" height="300" fill="#1a0c06"/>
    <rect width="800" height="220" fill="url(#murBois)"/>
    <!-- Poutres -->
    <rect x="0" y="40" width="800" height="10" fill="#1a0c04"/>
    <rect x="0" y="120" width="800" height="6" fill="#1a0c04"/>
    <rect x="0" y="180" width="800" height="6" fill="#1a0c04"/>
    <!-- Portrait de Voltaire au mur -->
    <rect x="80" y="60" width="60" height="80" fill="#5a4020" stroke="#c9a227" stroke-width="2"/>
    <ellipse cx="110" cy="90" rx="20" ry="25" fill="#d8b898"/>
    <text x="110" y="155" font-size="9" fill="#c9a227" text-anchor="middle">VOLTAIRE</text>
    <!-- Presse à imprimerie (grand objet central) -->
    <rect x="300" y="120" width="200" height="140" fill="#5a3a20"/>
    <rect x="320" y="140" width="160" height="100" fill="#3a2410"/>
    <rect x="350" y="160" width="100" height="60" fill="#d8c8a8"/>
    <line x1="350" y1="180" x2="450" y2="180" stroke="#888" stroke-width="1"/>
    <line x1="350" y1="200" x2="450" y2="200" stroke="#888" stroke-width="1"/>
    <line x1="370" y1="160" x2="370" y2="220" stroke="#888" stroke-width="1"/>
    <line x1="400" y1="160" x2="400" y2="220" stroke="#888" stroke-width="1"/>
    <line x1="430" y1="160" x2="430" y2="220" stroke="#888" stroke-width="1"/>
    <!-- Levier de presse -->
    <rect x="380" y="90" width="40" height="40" fill="#4a3020"/>
    <rect x="395" y="60" width="10" height="40" fill="#2a1810"/>
    <circle cx="400" cy="55" r="8" fill="#6a4a2a"/>
    <!-- Tas de feuilles -->
    <rect x="560" y="200" width="120" height="50" fill="#e8d8b8"/>
    <rect x="565" y="195" width="115" height="8" fill="#f0e0c0"/>
    <rect x="570" y="190" width="110" height="8" fill="#e8d8b8"/>
    <!-- Cahiers empilés -->
    <rect x="100" y="220" width="80" height="35" fill="#c8a878"/>
    <rect x="100" y="212" width="80" height="10" fill="#d8b888"/>
    <!-- Bougie allumée -->
    <rect x="640" y="170" width="14" height="50" fill="#e8d8a8"/>
    <line x1="647" y1="170" x2="647" y2="155" stroke="#3a2810" stroke-width="1.5"/>
    <ellipse class="bougie-flamme" cx="647" cy="148" rx="6" ry="12" fill="#ffb040"/>
    <ellipse cx="647" cy="148" rx="3" ry="7" fill="#fff0a8"/>
    <!-- Halo de lumière -->
    <rect width="800" height="300" fill="url(#lumBougie)"/>
    <!-- Sol -->
    <rect x="0" y="260" width="800" height="40" fill="#1a0c04"/>
    <!-- Particules de poussière dorée -->
    <circle cx="500" cy="100" r="1" fill="#ffd878" opacity=".5"/>
    <circle cx="550" cy="80" r="1.5" fill="#ffd878" opacity=".4"/>
    <circle cx="600" cy="120" r="1" fill="#ffd878" opacity=".6"/>
  </svg>`,

  /* Salle 3 — Jardins des Tuileries ensoleillés */
  "tuileries": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
    <defs>
      <linearGradient id="cielSoleil" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#8ab8e8"/>
        <stop offset="100%" stop-color="#d8e8f8"/>
      </linearGradient>
      <radialGradient id="lumiereSoleil" cx="80%" cy="20%" r="50%">
        <stop offset="0%" stop-color="#fff8d8" stop-opacity=".5"/>
        <stop offset="100%" stop-color="#fff8d8" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <rect width="800" height="300" fill="url(#cielSoleil)"/>
    <rect width="800" height="300" fill="url(#lumiereSoleil)"/>
    <!-- Soleil -->
    <circle cx="640" cy="60" r="35" fill="#fff8c8" opacity=".9"/>
    <circle cx="640" cy="60" r="25" fill="#fff8e8"/>
    <!-- Palais des Tuileries à l'arrière -->
    <rect x="0" y="80" width="800" height="120" fill="#d8c8a8"/>
    <rect x="0" y="80" width="800" height="10" fill="#b8a888"/>
    <!-- Toits -->
    <polygon points="0,80 80,50 160,80" fill="#8a4838"/>
    <polygon points="160,80 240,50 320,80" fill="#8a4838"/>
    <polygon points="320,80 400,50 480,80" fill="#8a4838"/>
    <polygon points="480,80 560,50 640,80" fill="#8a4838"/>
    <polygon points="640,80 720,50 800,80" fill="#8a4838"/>
    <!-- Fenêtres du palais -->
    <g fill="#3a4858">
      <rect x="30" y="110" width="20" height="40"/>
      <rect x="90" y="110" width="20" height="40"/>
      <rect x="150" y="110" width="20" height="40"/>
      <rect x="210" y="110" width="20" height="40"/>
      <rect x="270" y="110" width="20" height="40"/>
      <rect x="330" y="110" width="20" height="40"/>
      <rect x="390" y="110" width="20" height="40"/>
      <rect x="450" y="110" width="20" height="40"/>
      <rect x="510" y="110" width="20" height="40"/>
      <rect x="570" y="110" width="20" height="40"/>
      <rect x="630" y="110" width="20" height="40"/>
      <rect x="690" y="110" width="20" height="40"/>
      <rect x="750" y="110" width="20" height="40"/>
    </g>
    <!-- Allée de sable -->
    <rect x="0" y="200" width="800" height="100" fill="#e8d4a8"/>
    <line x1="0" y1="220" x2="800" y2="220" stroke="#d0b888" stroke-width="1" opacity=".5"/>
    <!-- Tilleuls (feuillage animé) -->
    <g class="feuillage">
      <ellipse cx="80" cy="200" rx="55" ry="50" fill="#5a8a3a"/>
      <ellipse cx="90" cy="190" rx="40" ry="38" fill="#6a9a4a"/>
      <rect x="75" y="200" width="10" height="40" fill="#4a3018"/>
    </g>
    <g class="feuillage" style="animation-delay:-1s">
      <ellipse cx="720" cy="200" rx="50" ry="48" fill="#5a8a3a"/>
      <ellipse cx="710" cy="190" rx="38" ry="36" fill="#6a9a4a"/>
      <rect x="715" y="200" width="10" height="40" fill="#4a3018"/>
    </g>
    <!-- Banc -->
    <rect x="320" y="220" width="120" height="6" fill="#6a4828"/>
    <rect x="330" y="226" width="6" height="20" fill="#6a4828"/>
    <rect x="424" y="226" width="6" height="20" fill="#6a4828"/>
    <!-- Nobles qui se promènent -->
    <g>
      <ellipse cx="220" cy="240" rx="12" ry="22" fill="#6a1a2a"/>
      <circle cx="220" cy="216" r="9" fill="#f0d8b8"/>
      <ellipse cx="220" cy="208" rx="14" ry="8" fill="#e8e0d0"/>
    </g>
    <g>
      <ellipse cx="540" cy="240" rx="11" ry="20" fill="#3a3a5a"/>
      <circle cx="540" cy="218" r="8" fill="#f0d8b8"/>
      <ellipse cx="540" cy="210" rx="12" ry="7" fill="#e8e0d0"/>
    </g>
    <!-- Garde suisse au loin -->
    <g>
      <ellipse cx="650" cy="250" rx="8" ry="16" fill="#b22222"/>
      <circle cx="650" cy="232" r="6" fill="#f0d8b8"/>
    </g>
  </svg>`,

  /* Salle 4 — Place de la Bastille fumante */
  "bastille": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
    <defs>
      <linearGradient id="cielFumee" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#a89888"/>
        <stop offset="60%" stop-color="#c8b898"/>
        <stop offset="100%" stop-color="#d8c8a8"/>
      </linearGradient>
      <radialGradient id="haloIncendie" cx="50%" cy="70%" r="50%">
        <stop offset="0%" stop-color="#d84818" stop-opacity=".3"/>
        <stop offset="100%" stop-color="#d84818" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <rect width="800" height="300" fill="url(#cielFumee)"/>
    <!-- Tour de la Bastille à demi démantelée -->
    <rect x="200" y="80" width="400" height="170" fill="#888070"/>
    <rect x="200" y="80" width="400" height="20" fill="#6a6050"/>
    <!-- Créneaux -->
    <rect x="200" y="70" width="20" height="20" fill="#888070"/>
    <rect x="240" y="70" width="20" height="20" fill="#888070"/>
    <rect x="280" y="70" width="20" height="20" fill="#888070"/>
    <rect x="320" y="70" width="20" height="20" fill="#888070"/>
    <!-- Tours latérales -->
    <rect x="170" y="60" width="60" height="190" fill="#a09080"/>
    <ellipse cx="200" cy="60" rx="30" ry="20" fill="#888070"/>
    <rect x="570" y="60" width="60" height="190" fill="#a09080"/>
    <ellipse cx="600" cy="60" rx="30" ry="20" fill="#888070"/>
    <!-- Brèche dans le mur central -->
    <polygon points="340,250 360,200 380,180 400,170 420,180 440,200 460,250" fill="#3a2818"/>
    <polygon points="350,250 370,210 390,195 410,195 430,210 450,250" fill="#1a0808"/>
    <!-- Fenêtres de la forteresse -->
    <rect x="230" y="120" width="14" height="24" fill="#1a0c04"/>
    <rect x="270" y="120" width="14" height="24" fill="#2a1810"/>
    <rect x="490" y="120" width="14" height="24" fill="#1a0c04"/>
    <rect x="530" y="120" width="14" height="24" fill="#2a1810"/>
    <rect x="230" y="170" width="14" height="24" fill="#1a0c04"/>
    <rect x="530" y="170" width="14" height="24" fill="#1a0c04"/>
    <!-- Débris de pierre au sol -->
    <polygon points="100,260 130,250 140,260" fill="#6a6050"/>
    <polygon points="660,255 690,245 700,260" fill="#6a6050"/>
    <rect x="80" y="262" width="40" height="10" fill="#888070" transform="rotate(15 100 267)"/>
    <rect x="700" y="260" width="35" height="8" fill="#888070" transform="rotate(-12 717 264)"/>
    <!-- Sol -->
    <rect x="0" y="250" width="800" height="50" fill="#5a4838"/>
    <!-- Volontaires Garde nationale -->
    <g>
      <ellipse cx="120" cy="245" rx="10" ry="18" fill="#3a5a8a"/>
      <circle cx="120" cy="225" r="7" fill="#f0d8b8"/>
      <rect x="116" y="208" width="8" height="14" fill="#3a5a8a" rx="2"/>
    </g>
    <g>
      <ellipse cx="680" cy="245" rx="10" ry="18" fill="#3a5a8a"/>
      <circle cx="680" cy="225" r="7" fill="#f0d8b8"/>
      <rect x="676" y="208" width="8" height="14" fill="#3a5a8a" rx="2"/>
    </g>
    <!-- Drapeau tricolore -->
    <line x1="300" y1="250" x2="300" y2="180" stroke="#4a3018" stroke-width="2"/>
    <rect x="300" y="180" width="6" height="9" fill="#1d3a8a"/>
    <rect x="306" y="180" width="6" height="9" fill="#fff"/>
    <rect x="312" y="180" width="6" height="9" fill="#b22222"/>
    <!-- Halo d'incendie -->
    <rect width="800" height="300" fill="url(#haloIncendie)"/>
    <!-- Fumée animée -->
    <circle class="fumee" cx="400" cy="180" r="20" fill="#aaa" style="animation-delay:0s"/>
    <circle class="fumee" cx="420" cy="190" r="15" fill="#999" style="animation-delay:-2s"/>
    <circle class="fumee" cx="380" cy="185" r="18" fill="#bbb" style="animation-delay:-4s"/>
  </svg>`,

  /* Salle 5 — Salle de l'Assemblée nationale */
  "assemblee": `<svg class="decor-svg" viewBox="0 0 800 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0;width:100%;height:100%">
    <defs>
      <linearGradient id="murAssemblee" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#d8c8a0"/>
        <stop offset="100%" stop-color="#b8a888"/>
      </linearGradient>
      <radialGradient id="lumZenitale" cx="50%" cy="0%" r="70%">
        <stop offset="0%" stop-color="#fff8e0" stop-opacity=".5"/>
        <stop offset="100%" stop-color="#fff8e0" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <rect width="800" height="300" fill="url(#murAssemblee)"/>
    <rect width="800" height="300" fill="url(#lumZenitale)"/>
    <!-- Plafond à caissons -->
    <polygon points="0,0 800,0 700,40 100,40" fill="#a89060"/>
    <line x1="200" y1="40" x2="600" y2="40" stroke="#6a5028" stroke-width="2"/>
    <!-- Grande horloge au mur (pendule animée) -->
    <circle cx="120" cy="80" r="32" fill="#e8d8b8" stroke="#6a4828" stroke-width="3"/>
    <text x="120" y="76" font-size="8" fill="#3a2818" text-anchor="middle">XII</text>
    <text x="120" y="108" font-size="8" fill="#3a2818" text-anchor="middle">VI</text>
    <text x="96" y="86" font-size="7" fill="#3a2818" text-anchor="middle">IX</text>
    <text x="144" y="86" font-size="7" fill="#3a2818" text-anchor="middle">III</text>
    <line x1="120" y1="80" x2="120" y2="60" stroke="#3a2818" stroke-width="2"/>
    <line class="pendule-aiguille" x1="120" y1="80" x2="120" y2="102" stroke="#3a2818" stroke-width="2.5" stroke-linecap="round"/>
    <circle cx="120" cy="80" r="3" fill="#3a2818"/>
    <!-- Grand plan affiché au mur -->
    <rect x="600" y="50" width="120" height="80" fill="#f0e0b8" stroke="#6a4828" stroke-width="3"/>
    <line x1="610" y1="65" x2="710" y2="65" stroke="#888" stroke-width=".5"/>
    <line x1="610" y1="80" x2="710" y2="80" stroke="#888" stroke-width=".5"/>
    <line x1="610" y1="95" x2="710" y2="95" stroke="#888" stroke-width=".5"/>
    <line x1="610" y1="110" x2="710" y2="110" stroke="#888" stroke-width=".5"/>
    <text x="660" y="60" font-size="6" fill="#3a2818" text-anchor="middle">PLAN DE LA SALLE</text>
    <!-- Estrade présidentielle -->
    <rect x="300" y="180" width="200" height="100" fill="#8a6838"/>
    <rect x="300" y="180" width="200" height="10" fill="#6a4828"/>
    <!-- Fauteuil de président -->
    <rect x="370" y="160" width="60" height="50" fill="#6a1a2a"/>
    <rect x="370" y="155" width="60" height="10" fill="#4a0818"/>
    <rect x="365" y="165" width="6" height="50" fill="#c9a227"/>
    <rect x="429" y="165" width="6" height="50" fill="#c9a227"/>
    <!-- Dorures fauteuil -->
    <ellipse cx="400" cy="180" rx="22" ry="8" fill="#c9a227" opacity=".5"/>
    <!-- Gradins en bois (côtés) -->
    <polygon points="0,250 200,200 200,300 0,300" fill="#a88860"/>
    <polygon points="0,270 200,220 200,230 0,280" fill="#8a6838"/>
    <polygon points="600,200 800,250 800,300 600,300" fill="#a88860"/>
    <polygon points="600,220 800,270 800,280 600,230" fill="#8a6838"/>
    <!-- Bancs députés -->
    <rect x="220" y="240" width="80" height="8" fill="#8a6838"/>
    <rect x="220" y="255" width="80" height="8" fill="#8a6838"/>
    <rect x="500" y="240" width="80" height="8" fill="#8a6838"/>
    <rect x="500" y="255" width="80" height="8" fill="#8a6838"/>
    <!-- Sol -->
    <rect x="0" y="280" width="800" height="20" fill="#6a5028"/>
  </svg>`,
};

window.htmlScene = htmlScene;
window.activerScene = activerScene;
window.SVG_DECORS = SVG_DECORS;
