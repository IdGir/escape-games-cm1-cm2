/* ============================================================
   PORTRAITS SVG ANIMÉS — 4 personnages de la Révolution
   Bouche qui bouge, yeux qui clignent, respiration
   Fallback automatique : si une image IA existe dans
   assets/images/personnages/<nom>.png, on l'utilise à la place
   ============================================================ */

/**
 * Génère le HTML du portrait d'un personnage.
 * @param {string} perso - 'louise' | 'gutenberg' | 'marquis' | 'maximilien'
 * @param {boolean} forceSvg - forcer le SVG même si une image existe (utile pour tester)
 * @returns {string} HTML
 */
function htmlPortrait(perso, forceSvg=false){
  // Détection d'une éventuelle image IA réelle dans le dossier personnages
  // (en runtime navigateur, on tente un chargement ; en cas d'échec → SVG)
  const src = `assets/images/personnages/${perso}.png`;
  const svg = SVG_PORTRAITS[perso] || SVG_PORTRAITS.louise;
  // On rend l'<img> d'abord ; si elle plante, on bascule sur le SVG
  return `
    <div class="portrait-conteneur" data-perso="${perso}">
      <img src="${src}" alt="${perso}" class="portrait-img-cachee"
           onerror="this.style.display='none';this.parentElement.querySelector('.portrait-svg').style.display='block'"
           style="display:none">
      <div class="portrait-svg" style="display:block">${svg}</div>
    </div>`;
}

// Au chargement, si l'image existe réellement, on la montre et on cache le SVG
function activerPortrait(conteneur){
  if(!conteneur) return;
  const img = conteneur.querySelector(".portrait-img-cachee");
  const svg = conteneur.querySelector(".portrait-svg");
  if(!img || !svg) return;
  const test = new Image();
  test.onload = ()=>{ img.style.display="block"; svg.style.display="none"; };
  test.src = img.src;
}

/* ---- Bibliothèque des SVG par personnage ----
   Chaque SVG contient : .tete, .corps, .yeux .paupiere, .bouche, .bouche-ouverte, .bouche-fermee
   pour les animations définies dans animations.css */
const SVG_PORTRAITS = {

  /* Louise — jeune fille du peuple, vive, cheveux bruns */
  louise: `<svg class="portrait-svg-interne" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
    <defs>
      <radialGradient id="fondLouise" cx="50%" cy="40%" r="70%">
        <stop offset="0%" stop-color="#5a3a2a"/>
        <stop offset="100%" stop-color="#1a1020"/>
      </radialGradient>
      <linearGradient id="peauL" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#f3d5b5"/><stop offset="100%" stop-color="#e8c098"/>
      </linearGradient>
    </defs>
    <rect width="200" height="200" fill="url(#fondLouise)"/>
    <g class="corps">
      <!-- Fichu et épaules -->
      <path d="M30 200 Q40 150 100 145 Q160 150 170 200 Z" fill="#8a6a3a"/>
      <path d="M55 165 Q100 150 145 165 Q150 175 100 178 Q50 175 55 165" fill="#c9a227" opacity=".5"/>
    </g>
    <g class="tete">
      <!-- Cheveux -->
      <path d="M48 95 Q50 50 100 48 Q150 50 152 95 Q155 80 150 110 Q145 70 100 68 Q55 70 50 110 Q45 80 48 95" fill="#4a2a18"/>
      <path d="M45 100 Q42 130 55 150" stroke="#4a2a18" stroke-width="8" fill="none" stroke-linecap="round"/>
      <path d="M155 100 Q158 130 145 150" stroke="#4a2a18" stroke-width="8" fill="none" stroke-linecap="round"/>
      <!-- Fichu sur la tête -->
      <path d="M52 78 Q100 60 148 78 Q150 92 100 88 Q50 92 52 78" fill="#a8865a"/>
      <!-- Visage -->
      <ellipse cx="100" cy="105" rx="38" ry="44" fill="url(#peauL)"/>
      <!-- Joues roses -->
      <ellipse cx="78" cy="118" rx="9" ry="6" fill="#e8a0a0" opacity=".5"/>
      <ellipse cx="122" cy="118" rx="9" ry="6" fill="#e8a0a0" opacity=".5"/>
      <!-- Sourcils -->
      <g class="sourcils">
        <path d="M75 95 Q82 91 90 95" stroke="#3a1d0a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M110 95 Q118 91 125 95" stroke="#3a1d0a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux -->
      <g class="yeux">
        <ellipse cx="83" cy="105" rx="6" ry="5" fill="#fff"/>
        <ellipse cx="117" cy="105" rx="6" ry="5" fill="#fff"/>
        <circle cx="84" cy="106" r="3" fill="#5a3a1a"/>
        <circle cx="118" cy="106" r="3" fill="#5a3a1a"/>
        <circle cx="85" cy="105" r="1" fill="#fff"/>
        <circle cx="119" cy="105" r="1" fill="#fff"/>
        <rect class="paupiere" x="76" y="100" width="14" height="11" fill="url(#peauL)"/>
        <rect class="paupiere" x="110" y="100" width="14" height="11" fill="url(#peauL)"/>
      </g>
      <!-- Nez -->
      <path d="M100 110 Q98 122 95 128 Q100 131 105 128 Q102 122 100 110" fill="#d8a888" opacity=".5"/>
      <!-- Bouche (sourire malicieux) -->
      <g class="bouche">
        <path class="bouche-fermee" d="M88 138 Q100 144 112 138" stroke="#a04040" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <ellipse class="bouche-ouverte" cx="100" cy="140" rx="9" ry="5" fill="#7d2828"/>
      </g>
      <!-- Taches de rousseur -->
      <circle cx="76" cy="118" r="1" fill="#a87040" opacity=".6"/>
      <circle cx="80" cy="122" r="1" fill="#a87040" opacity=".6"/>
      <circle cx="124" cy="118" r="1" fill="#a87040" opacity=".6"/>
      <circle cx="120" cy="122" r="1" fill="#a87040" opacity=".6"/>
    </g>
  </svg>`,

  /* Gutenberg — imprimeur barbu, lunettes rondes */
  gutenberg: `<svg class="portrait-svg-interne" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
    <defs>
      <radialGradient id="fondGut" cx="50%" cy="40%" r="70%">
        <stop offset="0%" stop-color="#3a2a1a"/><stop offset="100%" stop-color="#100808"/>
      </radialGradient>
      <linearGradient id="peauG" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#e8c8a0"/><stop offset="100%" stop-color="#c89868"/>
      </linearGradient>
    </defs>
    <rect width="200" height="200" fill="url(#fondGut)"/>
    <g class="corps">
      <!-- Tablier de cuir -->
      <path d="M35 200 Q45 150 100 148 Q155 150 165 200 Z" fill="#5a3a20"/>
      <!-- Chemise blanche -->
      <path d="M80 155 Q100 150 120 155 L120 200 L80 200 Z" fill="#d8c8a8"/>
    </g>
    <g class="tete">
      <!-- Crâne dégarni -->
      <ellipse cx="100" cy="95" rx="42" ry="48" fill="url(#peauG)"/>
      <!-- Cheveux courts gris -->
      <path d="M58 95 Q55 75 70 70 Q100 60 130 70 Q145 75 142 95 Q140 82 100 78 Q60 82 58 95" fill="#888"/>
      <path d="M55 110 Q50 135 60 150" stroke="#888" stroke-width="6" fill="none" stroke-linecap="round"/>
      <path d="M145 110 Q150 135 140 150" stroke="#888" stroke-width="6" fill="none" stroke-linecap="round"/>
      <!-- Oreilles -->
      <ellipse cx="58" cy="105" rx="5" ry="9" fill="url(#peauG)"/>
      <ellipse cx="142" cy="105" rx="5" ry="9" fill="url(#peauG)"/>
      <!-- Sourcils gris -->
      <g class="sourcils">
        <path d="M72 92 Q82 88 92 92" stroke="#aaa" stroke-width="3" fill="none" stroke-linecap="round"/>
        <path d="M108 92 Q118 88 128 92" stroke="#aaa" stroke-width="3" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Lunettes rondes -->
      <circle cx="82" cy="105" r="12" fill="none" stroke="#c9a227" stroke-width="2.5"/>
      <circle cx="118" cy="105" r="12" fill="none" stroke="#c9a227" stroke-width="2.5"/>
      <line x1="94" y1="105" x2="106" y2="105" stroke="#c9a227" stroke-width="2"/>
      <circle cx="82" cy="105" r="10" fill="#b8d8e8" opacity=".25"/>
      <circle cx="118" cy="105" r="10" fill="#b8d8e8" opacity=".25"/>
      <!-- Yeux -->
      <g class="yeux">
        <circle cx="82" cy="105" r="3" fill="#3a2a1a"/>
        <circle cx="118" cy="105" r="3" fill="#3a2a1a"/>
        <rect class="paupiere" x="70" y="100" width="24" height="11" fill="url(#peauG)"/>
        <rect class="paupiere" x="106" y="100" width="24" height="11" fill="url(#peauG)"/>
      </g>
      <!-- Nez -->
      <path d="M100 115 L96 132 Q100 135 104 132 Z" fill="#b88858" opacity=".6"/>
      <!-- Barbe poivre et sel -->
      <path d="M70 135 Q75 160 100 165 Q125 160 130 135 Q120 150 100 152 Q80 150 70 135" fill="#999"/>
      <!-- Bouche (cachée par barbe supérieure) -->
      <g class="bouche">
        <path class="bouche-fermee" d="M90 145 Q100 149 110 145" stroke="#7a4030" stroke-width="2" fill="none" stroke-linecap="round"/>
        <ellipse class="bouche-ouverte" cx="100" cy="146" rx="7" ry="4" fill="#6a2828"/>
      </g>
    </g>
  </svg>`,

  /* Marquis — aristocrate, perruque poudrée, habit brodé */
  marquis: `<svg class="portrait-svg-interne" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
    <defs>
      <radialGradient id="fondMarq" cx="50%" cy="40%" r="70%">
        <stop offset="0%" stop-color="#4a2a3a"/><stop offset="100%" stop-color="#1a0810"/>
      </radialGradient>
      <linearGradient id="peauM" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#f5dccb"/><stop offset="100%" stop-color="#e0bca0"/>
      </linearGradient>
    </defs>
    <rect width="200" height="200" fill="url(#fondMarq)"/>
    <g class="corps">
      <!-- Habit brodé bordeaux -->
      <path d="M30 200 Q40 145 100 142 Q160 145 170 200 Z" fill="#6a1a2a"/>
      <!-- Jabot en dentelle -->
      <path d="M85 155 Q100 150 115 155 L120 200 L80 200 Z" fill="#f8f0e0"/>
      <path d="M88 165 Q100 162 112 165" stroke="#d8c8a8" stroke-width="1" fill="none"/>
      <path d="M88 175 Q100 172 112 175" stroke="#d8c8a8" stroke-width="1" fill="none"/>
      <!-- Broderies dorées -->
      <path d="M50 175 Q55 185 50 195" stroke="#c9a227" stroke-width="2" fill="none"/>
      <path d="M150 175 Q145 185 150 195" stroke="#c9a227" stroke-width="2" fill="none"/>
    </g>
    <g class="tete">
      <!-- Perruque poudrée -->
      <path d="M50 100 Q45 60 100 55 Q155 60 150 100 Q160 130 150 160 Q140 165 100 165 Q60 165 50 160 Q40 130 50 100" fill="#e8e0d0"/>
      <ellipse cx="100" cy="80" rx="55" ry="28" fill="#f0e8d8"/>
      <!-- Boucles perruque -->
      <ellipse cx="55" cy="120" rx="10" ry="14" fill="#e8e0d0"/>
      <ellipse cx="145" cy="120" rx="10" ry="14" fill="#e8e0d0"/>
      <!-- Visage -->
      <ellipse cx="100" cy="108" rx="34" ry="40" fill="url(#peauM)"/>
      <!-- Joues poudrées -->
      <ellipse cx="78" cy="122" rx="8" ry="5" fill="#e8a8b8" opacity=".4"/>
      <ellipse cx="122" cy="122" rx="8" ry="5" fill="#e8a8b8" opacity=".4"/>
      <!-- Sourcils fins -->
      <g class="sourcils">
        <path d="M75 98 Q82 95 90 98" stroke="#6a4a2a" stroke-width="2" fill="none" stroke-linecap="round"/>
        <path d="M110 98 Q118 95 125 98" stroke="#6a4a2a" stroke-width="2" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux (regard hautain) -->
      <g class="yeux">
        <ellipse cx="83" cy="106" rx="6" ry="4" fill="#fff"/>
        <ellipse cx="117" cy="106" rx="6" ry="4" fill="#fff"/>
        <circle cx="84" cy="105" r="2.5" fill="#3a2a4a"/>
        <circle cx="118" cy="105" r="2.5" fill="#3a2a4a"/>
        <rect class="paupiere" x="76" y="102" width="14" height="9" fill="url(#peauM)"/>
        <rect class="paupiere" x="110" y="102" width="14" height="9" fill="url(#peauM)"/>
      </g>
      <!-- Nez fin -->
      <path d="M100 112 L97 130 Q100 132 103 130 Z" fill="#d0a890" opacity=".5"/>
      <!-- Moustache fine -->
      <path d="M85 138 Q100 136 115 138" stroke="#5a3a2a" stroke-width="1.5" fill="none"/>
      <!-- Bouche (légèrement ironique) -->
      <g class="bouche">
        <path class="bouche-fermee" d="M88 142 Q100 145 112 142" stroke="#8a3030" stroke-width="2" fill="none" stroke-linecap="round"/>
        <ellipse class="bouche-ouverte" cx="100" cy="143" rx="8" ry="4" fill="#7a2828"/>
      </g>
      <!-- Grain de beauté (élégance) -->
      <circle cx="112" cy="118" r="1.5" fill="#3a1a1a"/>
    </g>
  </svg>`,

  /* Maximilien — jeune avocat idéaliste, regard passionné */
  maximilien: `<svg class="portrait-svg-interne" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
    <defs>
      <radialGradient id="fondMax" cx="50%" cy="40%" r="70%">
        <stop offset="0%" stop-color="#2a2a3a"/><stop offset="100%" stop-color="#080808"/>
      </radialGradient>
      <linearGradient id="peauMax" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#f0d8c0"/><stop offset="100%" stop-color="#d8b898"/>
      </linearGradient>
    </defs>
    <rect width="200" height="200" fill="url(#fondMax)"/>
    <g class="corps">
      <!-- Costume noir d'avocat -->
      <path d="M32 200 Q42 150 100 146 Q158 150 168 200 Z" fill="#1a1a2a"/>
      <!-- Fraise (col) -->
      <ellipse cx="100" cy="158" rx="28" ry="8" fill="#f8f0e0"/>
      <path d="M75 158 Q100 152 125 158" stroke="#d0c0a0" stroke-width="1" fill="none"/>
      <path d="M78 162 Q100 156 122 162" stroke="#d0c0a0" stroke-width="1" fill="none"/>
    </g>
    <g class="tete">
      <!-- Perruque courte poudrée -->
      <path d="M58 95 Q55 60 100 55 Q145 60 142 95 Q148 100 145 110 Q140 75 100 72 Q60 75 55 110 Q52 100 58 95" fill="#dcd4c4"/>
      <!-- Visage pâle -->
      <ellipse cx="100" cy="108" rx="35" ry="42" fill="url(#peauMax)"/>
      <!-- Joues très pâles (idéaliste) -->
      <ellipse cx="78" cy="120" rx="6" ry="4" fill="#e8a098" opacity=".25"/>
      <ellipse cx="122" cy="120" rx="6" ry="4" fill="#e8a098" opacity=".25"/>
      <!-- Sourcils graves -->
      <g class="sourcils">
        <path d="M74 96 Q83 93 91 96" stroke="#6a4a2a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M109 96 Q117 93 126 96" stroke="#6a4a2a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux (regard intense) -->
      <g class="yeux">
        <ellipse cx="83" cy="106" rx="6" ry="5" fill="#fff"/>
        <ellipse cx="117" cy="106" rx="6" ry="5" fill="#fff"/>
        <circle cx="84" cy="107" r="3" fill="#4a5a3a"/>
        <circle cx="118" cy="107" r="3" fill="#4a5a3a"/>
        <circle cx="85" cy="106" r="1" fill="#fff"/>
        <circle cx="119" cy="106" r="1" fill="#fff"/>
        <rect class="paupiere" x="76" y="101" width="14" height="11" fill="url(#peauMax)"/>
        <rect class="paupiere" x="110" y="101" width="14" height="11" fill="url(#peauMax)"/>
      </g>
      <!-- Nez droit -->
      <path d="M100 113 L97 130 Q100 132 103 130 Z" fill="#c8a888" opacity=".5"/>
      <!-- Bouche (déterminée, sérieuse) -->
      <g class="bouche">
        <path class="bouche-fermee" d="M88 142 L112 142" stroke="#8a3030" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <ellipse class="bouche-ouverte" cx="100" cy="143" rx="8" ry="4" fill="#6a2828"/>
      </g>
      <!-- Légère ride de réflexion -->
      <path d="M88 92 Q90 90 92 92" stroke="#b89878" stroke-width=".8" fill="none" opacity=".6"/>
      <path d="M108 92 Q110 90 112 92" stroke="#b89878" stroke-width=".8" fill="none" opacity=".6"/>
    </g>
  </svg>`,
};

// Exposer globalement
window.htmlPortrait = htmlPortrait;
window.activerPortrait = activerPortrait;
window.SVG_PORTRAITS = SVG_PORTRAITS;
