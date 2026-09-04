/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés
   Le Tour du Monde en 80 minutes · d'après Jules Verne
   ------------------------------------------------------------
   RIG (classes réutilisées par animations.css / personnages.css) :
     .tete .yeux .paupiere .bouche .sourcils   → lip-sync
     .buste                                    → respiration
     .bras-g / .bras-d                         → épaule (pivot haut)
     .avant-g / .avant-d                       → coude
     .main-g  / .main-d                        → main
     .jambes                                   → appui / balancement

   Gestes pilotés par des classes posées sur .portrait :
     .parle · .geste-pointe · .geste-joie · .geste-inquiet · .geste-salue
   ============================================================ */

/* ---- Palette commune ---- */
const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e8c39a","#d3a273"],
  ambre:  ["#d9a06a","#b87c48"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

/**
 * Génère le SVG plein corps d'un personnage.
 * @param {string} perso - fogg|passepartout|aouda|fix
 */
function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.passepartout;
}

/**
 * HTML complet du personnage : image de l'enseignant si elle existe
 * (assets/images/personnages/<perso>.png), sinon le SVG animé.
 */
function htmlPersonnage(perso){
  const src = `assets/images/personnages/${perso}.png`;
  const svg = svgPersonnage(perso);
  return `
    <div class="portrait-conteneur perso-plein-conteneur" data-perso="${perso}">
      <img src="${src}" alt="${perso}" class="portrait-img-cachee"
           onerror="this.style.display='none';this.parentElement.querySelector('.portrait-svg').style.display='block'"
           style="display:none">
      <div class="portrait-svg" style="display:block">${svg}</div>
    </div>`;
}

/* ============================================================
   BIBLIOTHÈQUE DES PERSONNAGES
   viewBox 200 × 320 — le personnage occupe toute la hauteur
   ============================================================ */
const SVG_PERSOS = {

/* ------------------------------------------------------------
   PHILEAS FOGG — gentleman anglais, flegme absolu, redingote
   noire, cravate blanche, montre à gousset. Ne s'étonne jamais.
   ------------------------------------------------------------ */
fogg: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondFo" cx="50%" cy="32%" r="78%">
      <stop offset="0%" stop-color="#2c4358"/><stop offset="100%" stop-color="#0a1626"/>
    </radialGradient>
    <linearGradient id="peauFo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.pale[0]}"/><stop offset="100%" stop-color="${PEAU.pale[1]}"/>
    </linearGradient>
    <linearGradient id="habitFo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2b3038"/><stop offset="100%" stop-color="#14181e"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondFo)"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>

  <g class="perso-corps">
    <!-- Jambes : pantalon à rayures fines -->
    <g class="jambes">
      <path d="M72 212 Q68 262 66 296 L88 296 Q92 258 94 212 Z" fill="url(#habitFo)"/>
      <path d="M106 212 Q108 258 112 296 L134 296 Q132 262 128 212 Z" fill="url(#habitFo)"/>
      <g stroke="#4a515c" stroke-width="1" opacity=".55">
        <line x1="78" y1="220" x2="74" y2="292"/><line x1="86" y1="220" x2="83" y2="292"/>
        <line x1="114" y1="220" x2="117" y2="292"/><line x1="122" y1="220" x2="125" y2="292"/>
      </g>
      <!-- Escarpins vernis -->
      <ellipse cx="76" cy="299" rx="16" ry="6" fill="#0d0f13"/>
      <ellipse cx="124" cy="299" rx="16" ry="6" fill="#0d0f13"/>
    </g>

    <!-- Bras arrière : tient un parapluie/canne -->
    <g class="bras bras-g">
      <path d="M68 150 Q56 178 52 204" stroke="url(#habitFo)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M52 204 Q50 220 54 234" stroke="url(#habitFo)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="55" cy="240" r="9" fill="url(#peauFo)"/>
        <!-- Canne -->
        <line x1="55" y1="232" x2="55" y2="298" stroke="#5a3a1e" stroke-width="4" stroke-linecap="round"/>
        <circle cx="55" cy="230" r="5" fill="#c08a3e"/>
      </g>
    </g>

    <!-- Buste : redingote, gilet crème, cravate blanche -->
    <g class="buste">
      <path d="M68 148 Q66 134 78 128 L122 128 Q134 134 132 148 L136 216 Q100 224 64 216 Z" fill="url(#habitFo)"/>
      <!-- Gilet -->
      <path d="M86 132 Q100 156 114 132 L118 210 Q100 216 82 210 Z" fill="#e0d5b8"/>
      <!-- Chaîne et montre à gousset : l'objet emblématique de Fogg -->
      <path d="M88 176 Q100 186 114 178" stroke="#c08a3e" stroke-width="2" fill="none"/>
      <circle cx="115" cy="180" r="6" fill="#e8bf72" stroke="#8a5f24" stroke-width="1.4"/>
      <line x1="115" y1="180" x2="115" y2="176" stroke="#3a2415" stroke-width="1"/>
      <line x1="115" y1="180" x2="118" y2="181" stroke="#3a2415" stroke-width="1"/>
      <!-- Revers de la redingote -->
      <path d="M78 128 Q90 154 100 132 Q110 154 122 128 L124 152 Q100 178 76 152 Z" fill="#1b2028"/>
      <!-- Cravate blanche nouée -->
      <path d="M92 126 Q100 140 108 126 Q112 132 100 146 Q88 132 92 126" fill="#f7f4ec"/>
      <!-- Cou et col cassé -->
      <path d="M91 116 L109 116 L109 132 Q100 138 91 132 Z" fill="#e6c6a4"/>
      <path d="M88 124 L100 134 L112 124" stroke="#f7f4ec" stroke-width="4" fill="none" stroke-linejoin="round"/>
    </g>

    <!-- Bras avant : celui qui gesticule (sobrement — c'est Fogg) -->
    <g class="bras bras-d">
      <path d="M132 150 Q146 176 150 202" stroke="url(#habitFo)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M150 202 Q152 218 148 232" stroke="url(#habitFo)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="147" cy="238" r="9.5" fill="url(#peauFo)"/>
          <path d="M143 233 Q140 228 142 224" stroke="url(#peauFo)" stroke-width="4" fill="none" stroke-linecap="round"/>
        </g>
      </g>
    </g>

    <!-- Tête : chapeau haut-de-forme, favoris, regard imperturbable -->
    <g class="tete">
      <!-- Cheveux -->
      <path d="M68 84 Q66 48 100 46 Q134 48 132 84 Q134 96 128 104 Q130 66 100 64 Q70 66 72 104 Q66 96 68 84" fill="#33261a"/>
      <!-- Visage -->
      <ellipse cx="100" cy="88" rx="30" ry="35" fill="url(#peauFo)"/>
      <!-- Favoris (« côtelettes ») anglais -->
      <path d="M71 82 Q68 100 76 114 Q82 108 80 84 Z" fill="#33261a"/>
      <path d="M129 82 Q132 100 124 114 Q118 108 120 84 Z" fill="#33261a"/>
      <!-- Chapeau haut-de-forme -->
      <ellipse cx="100" cy="52" rx="42" ry="8" fill="#191d24"/>
      <path d="M74 52 L76 14 Q100 8 124 14 L126 52 Q100 58 74 52" fill="#22272f"/>
      <rect x="75" y="40" width="50" height="8" fill="#0d0f13"/>
      <ellipse cx="100" cy="14" rx="24" ry="5" fill="#2b3038"/>
      <!-- Sourcils : rigoureusement horizontaux -->
      <g class="sourcils">
        <path d="M82 76 Q88 74 95 76" stroke="#2a1f14" stroke-width="2.6" fill="none" stroke-linecap="round"/>
        <path d="M105 76 Q112 74 118 76" stroke="#2a1f14" stroke-width="2.6" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux -->
      <g class="yeux">
        <ellipse cx="88" cy="86" rx="6" ry="4.4" fill="#fff"/>
        <ellipse cx="112" cy="86" rx="6" ry="4.4" fill="#fff"/>
        <circle cx="88" cy="86" r="2.9" fill="#3a5a6a"/>
        <circle cx="112" cy="86" r="2.9" fill="#3a5a6a"/>
        <circle cx="89.1" cy="84.9" r="1.1" fill="#fff"/>
        <circle cx="113.1" cy="84.9" r="1.1" fill="#fff"/>
        <ellipse class="paupiere" cx="88" cy="86" rx="6.3" ry="4.7" fill="url(#peauFo)"/>
        <ellipse class="paupiere" cx="112" cy="86" rx="6.3" ry="4.7" fill="url(#peauFo)"/>
      </g>
      <!-- Nez -->
      <path d="M100 90 Q97 98 101 100" stroke="#d8b48f" stroke-width="2" fill="none" stroke-linecap="round"/>
      <!-- Bouche : une ligne nette, jamais un sourire -->
      <ellipse class="bouche bouche-ouverte" cx="100" cy="109" rx="6.5" ry="3.4" fill="#a05a55"/>
      <path class="bouche-fermee" d="M92 109 L108 109" stroke="#8d4a48" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   JEAN PASSEPARTOUT — le domestique français, ancien gymnaste,
   bavard, chaleureux. C'est lui qui guide les élèves.
   ------------------------------------------------------------ */
passepartout: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondPa" cx="50%" cy="34%" r="76%">
      <stop offset="0%" stop-color="#4a5c3a"/><stop offset="100%" stop-color="#141c14"/>
    </radialGradient>
    <linearGradient id="peauPa" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.claire[0]}"/><stop offset="100%" stop-color="${PEAU.claire[1]}"/>
    </linearGradient>
    <linearGradient id="vestePa" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3f6f8a"/><stop offset="100%" stop-color="#28495d"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondPa)"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>

  <g class="perso-corps">
    <!-- Jambes : pantalon de toile beige -->
    <g class="jambes">
      <path d="M72 212 Q68 260 66 294 L90 294 Q93 256 95 212 Z" fill="#b9a377"/>
      <path d="M105 212 Q107 256 110 294 L134 294 Q132 260 128 212 Z" fill="#b9a377"/>
      <path d="M70 250 L94 250 M106 250 L132 250" stroke="#9c8760" stroke-width="1.5" opacity=".6"/>
      <!-- Souliers de marche -->
      <ellipse cx="78" cy="299" rx="16" ry="7" fill="#5a3a20"/>
      <ellipse cx="122" cy="299" rx="16" ry="7" fill="#5a3a20"/>
    </g>

    <!-- Bras arrière -->
    <g class="bras bras-g">
      <path d="M68 152 Q54 178 50 204" stroke="url(#vestePa)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M50 204 Q48 220 53 234" stroke="url(#vestePa)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="54" cy="240" r="9.5" fill="url(#peauPa)"/>
      </g>
    </g>

    <!-- Buste : veste courte, gilet rayé -->
    <g class="buste">
      <path d="M68 150 Q66 134 78 128 L122 128 Q134 134 132 150 L136 214 Q100 222 64 214 Z" fill="url(#vestePa)"/>
      <!-- Gilet rayé rouge et blanc (le Français !) -->
      <path d="M84 132 Q100 154 116 132 L120 208 Q100 214 80 208 Z" fill="#f2ece0"/>
      <g stroke="#c0392b" stroke-width="4" opacity=".85">
        <line x1="84" y1="146" x2="118" y2="146"/><line x1="82" y1="162" x2="119" y2="162"/>
        <line x1="81" y1="178" x2="120" y2="178"/><line x1="80" y1="194" x2="120" y2="194"/>
      </g>
      <!-- Boutons de laiton -->
      <circle cx="76" cy="158" r="3" fill="#e8bf72"/>
      <circle cx="76" cy="176" r="3" fill="#e8bf72"/>
      <circle cx="76" cy="194" r="3" fill="#e8bf72"/>
      <!-- Foulard rouge noué -->
      <path d="M86 126 Q100 140 114 126 Q120 132 100 148 Q80 132 86 126" fill="#c0392b"/>
      <!-- Cou -->
      <path d="M91 116 L109 116 L109 132 Q100 138 91 132 Z" fill="#e0b78f"/>
    </g>

    <!-- Bras avant : très expressif -->
    <g class="bras bras-d">
      <path d="M132 152 Q148 176 152 202" stroke="url(#vestePa)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M152 202 Q154 218 149 232" stroke="url(#vestePa)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="148" cy="238" r="10" fill="url(#peauPa)"/>
          <path d="M144 232 Q140 226 143 222" stroke="url(#peauPa)" stroke-width="4.5" fill="none" stroke-linecap="round"/>
        </g>
      </g>
    </g>

    <!-- Tête : cheveux bruns en bataille, moustache, sourire franc -->
    <g class="tete">
      <path d="M66 82 Q64 42 100 40 Q136 42 134 82 Q136 96 130 106 Q132 62 100 60 Q68 62 70 106 Q64 96 66 82" fill="#5a3a1e"/>
      <!-- Mèches rebelles -->
      <path d="M74 52 Q80 40 90 46" stroke="#5a3a1e" stroke-width="7" fill="none" stroke-linecap="round"/>
      <path d="M112 46 Q122 40 128 52" stroke="#5a3a1e" stroke-width="7" fill="none" stroke-linecap="round"/>
      <!-- Visage rond -->
      <ellipse cx="100" cy="88" rx="32" ry="35" fill="url(#peauPa)"/>
      <!-- Joues rouges de bon vivant -->
      <ellipse cx="80" cy="98" rx="9" ry="5.5" fill="#e08b80" opacity=".5"/>
      <ellipse cx="120" cy="98" rx="9" ry="5.5" fill="#e08b80" opacity=".5"/>
      <!-- Sourcils hauts et mobiles -->
      <g class="sourcils">
        <path d="M81 74 Q88 68 95 73" stroke="#4a2c14" stroke-width="2.8" fill="none" stroke-linecap="round"/>
        <path d="M105 73 Q112 68 119 74" stroke="#4a2c14" stroke-width="2.8" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux vifs -->
      <g class="yeux">
        <ellipse cx="88" cy="85" rx="6.4" ry="5" fill="#fff"/>
        <ellipse cx="112" cy="85" rx="6.4" ry="5" fill="#fff"/>
        <circle cx="88" cy="85" r="3.1" fill="#4a3418"/>
        <circle cx="112" cy="85" r="3.1" fill="#4a3418"/>
        <circle cx="89.3" cy="83.7" r="1.2" fill="#fff"/>
        <circle cx="113.3" cy="83.7" r="1.2" fill="#fff"/>
        <ellipse class="paupiere" cx="88" cy="85" rx="6.7" ry="5.3" fill="url(#peauPa)"/>
        <ellipse class="paupiere" cx="112" cy="85" rx="6.7" ry="5.3" fill="url(#peauPa)"/>
      </g>
      <!-- Nez -->
      <path d="M100 90 Q96 99 101 101" stroke="#d4a17a" stroke-width="2.2" fill="none" stroke-linecap="round"/>
      <!-- Moustache -->
      <path d="M86 106 Q100 100 114 106" stroke="#5a3a1e" stroke-width="5" fill="none" stroke-linecap="round"/>
      <!-- Bouche souriante -->
      <ellipse class="bouche bouche-ouverte" cx="100" cy="113" rx="8" ry="4.6" fill="#a8434a"/>
      <path class="bouche-fermee" d="M91 111 Q100 118 109 111" stroke="#8d3a40" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MRS AOUDA — jeune femme parsie sauvée en Inde, cultivée,
   parle anglais. Sari rouge et or, bijoux.
   ------------------------------------------------------------ */
aouda: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondAo" cx="50%" cy="34%" r="76%">
      <stop offset="0%" stop-color="#6a4a2a"/><stop offset="100%" stop-color="#1e1410"/>
    </radialGradient>
    <linearGradient id="peauAo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.ambre[0]}"/><stop offset="100%" stop-color="${PEAU.ambre[1]}"/>
    </linearGradient>
    <linearGradient id="sariAo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#c33b45"/><stop offset="100%" stop-color="#8e2230"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondAo)"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>

  <g class="perso-corps">
    <!-- Jupe du sari, drapée -->
    <g class="jambes">
      <path d="M66 210 Q58 264 54 298 Q100 306 146 298 Q142 264 134 210 Z" fill="url(#sariAo)"/>
      <!-- Plis -->
      <path d="M80 216 Q74 262 70 296" stroke="#75182a" stroke-width="2.5" fill="none" opacity=".7"/>
      <path d="M100 214 Q99 258 99 298" stroke="#75182a" stroke-width="2.5" fill="none" opacity=".7"/>
      <path d="M120 216 Q126 262 130 296" stroke="#75182a" stroke-width="2.5" fill="none" opacity=".7"/>
      <!-- Galon doré du bas -->
      <path d="M56 288 Q100 298 144 288 L146 298 Q100 307 54 298 Z" fill="#e8bf72"/>
      <g fill="#c08a3e"><circle cx="72" cy="294" r="2"/><circle cx="90" cy="297" r="2"/>
        <circle cx="110" cy="297" r="2"/><circle cx="128" cy="294" r="2"/></g>
    </g>

    <!-- Bras arrière, bracelets -->
    <g class="bras bras-g">
      <path d="M70 152 Q58 178 54 204" stroke="url(#peauAo)" stroke-width="13" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M54 204 Q52 220 56 234" stroke="url(#peauAo)" stroke-width="12" fill="none" stroke-linecap="round"/>
        <g stroke="#e8bf72" stroke-width="2.2">
          <line x1="49" y1="212" x2="59" y2="212"/><line x1="49" y1="218" x2="59" y2="218"/>
        </g>
        <circle class="main-g" cx="57" cy="240" r="8.5" fill="url(#peauAo)"/>
      </g>
    </g>

    <!-- Buste : corsage (choli) + drapé du sari sur l'épaule -->
    <g class="buste">
      <path d="M70 148 Q68 134 80 128 L120 128 Q132 134 130 148 L134 214 Q100 222 66 214 Z" fill="url(#sariAo)"/>
      <!-- Drapé (pallu) qui traverse le buste en diagonale -->
      <path d="M120 128 Q104 168 70 190 L66 214 Q104 194 132 148 Z" fill="#d9584f" opacity=".9"/>
      <path d="M120 130 Q106 168 74 190" stroke="#e8bf72" stroke-width="3" fill="none"/>
      <path d="M126 140 Q112 176 80 198" stroke="#e8bf72" stroke-width="1.8" fill="none" opacity=".7"/>
      <!-- Collier -->
      <path d="M88 134 Q100 148 112 134" stroke="#e8bf72" stroke-width="2.4" fill="none"/>
      <circle cx="100" cy="146" r="4.5" fill="#e8bf72"/>
      <circle cx="100" cy="146" r="2" fill="#2f7d6b"/>
      <!-- Cou -->
      <path d="M91 116 L109 116 L109 132 Q100 138 91 132 Z" fill="#c9925c"/>
    </g>

    <!-- Bras avant -->
    <g class="bras bras-d">
      <path d="M130 152 Q144 176 148 202" stroke="url(#peauAo)" stroke-width="13" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M148 202 Q150 218 146 232" stroke="url(#peauAo)" stroke-width="12" fill="none" stroke-linecap="round"/>
        <g stroke="#e8bf72" stroke-width="2.2">
          <line x1="142" y1="210" x2="153" y2="210"/><line x1="142" y1="216" x2="153" y2="216"/>
        </g>
        <g class="main-d">
          <circle cx="145" cy="238" r="9" fill="url(#peauAo)"/>
          <path d="M141 232 Q138 227 140 223" stroke="url(#peauAo)" stroke-width="4" fill="none" stroke-linecap="round"/>
        </g>
      </g>
    </g>

    <!-- Tête : longue chevelure noire, voile du sari, bindi -->
    <g class="tete">
      <!-- Chevelure -->
      <path d="M64 86 Q62 42 100 40 Q138 42 136 86 Q140 118 130 140 Q136 74 100 70 Q64 74 70 140 Q60 118 64 86" fill="#1d1310"/>
      <!-- Tresse sur l'épaule -->
      <path d="M132 108 Q146 140 138 172" stroke="#1d1310" stroke-width="11" fill="none" stroke-linecap="round"/>
      <circle cx="138" cy="176" r="4" fill="#e8bf72"/>
      <!-- Visage -->
      <ellipse cx="100" cy="88" rx="30" ry="35" fill="url(#peauAo)"/>
      <!-- Voile du sari posé sur les cheveux -->
      <path d="M62 78 Q66 42 100 40 Q134 42 138 78 Q120 58 100 58 Q80 58 62 78" fill="#c33b45" opacity=".92"/>
      <path d="M64 74 Q100 50 136 74" stroke="#e8bf72" stroke-width="2.6" fill="none"/>
      <!-- Bindi -->
      <circle cx="100" cy="66" r="3.2" fill="#8e2230"/>
      <!-- Boucles d'oreilles -->
      <circle cx="70" cy="96" r="4" fill="#e8bf72"/>
      <circle cx="130" cy="96" r="4" fill="#e8bf72"/>
      <!-- Sourcils fins -->
      <g class="sourcils">
        <path d="M82 76 Q88 71 95 75" stroke="#241612" stroke-width="2.2" fill="none" stroke-linecap="round"/>
        <path d="M105 75 Q112 71 118 76" stroke="#241612" stroke-width="2.2" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux grands et sombres -->
      <g class="yeux">
        <ellipse cx="88" cy="86" rx="6.6" ry="5" fill="#fff"/>
        <ellipse cx="112" cy="86" rx="6.6" ry="5" fill="#fff"/>
        <circle cx="88" cy="86" r="3.2" fill="#2a1a10"/>
        <circle cx="112" cy="86" r="3.2" fill="#2a1a10"/>
        <circle cx="89.3" cy="84.8" r="1.2" fill="#fff"/>
        <circle cx="113.3" cy="84.8" r="1.2" fill="#fff"/>
        <ellipse class="paupiere" cx="88" cy="86" rx="6.9" ry="5.3" fill="url(#peauAo)"/>
        <ellipse class="paupiere" cx="112" cy="86" rx="6.9" ry="5.3" fill="url(#peauAo)"/>
      </g>
      <!-- Nez -->
      <path d="M100 90 Q97 98 101 100" stroke="#a8763f" stroke-width="2" fill="none" stroke-linecap="round"/>
      <!-- Bouche -->
      <ellipse class="bouche bouche-ouverte" cx="100" cy="109" rx="7" ry="4" fill="#9e3a44"/>
      <path class="bouche-fermee" d="M93 108 Q100 113 107 108" stroke="#87313a" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   L'INSPECTEUR FIX — petit policier de Scotland Yard, chapeau
   melon, loupe. Il suit Fogg partout. Soupçonneux, agité.
   ------------------------------------------------------------ */
fix: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondFi" cx="50%" cy="34%" r="76%">
      <stop offset="0%" stop-color="#4a4a52"/><stop offset="100%" stop-color="#15161c"/>
    </radialGradient>
    <linearGradient id="peauFi" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.hale[0]}"/><stop offset="100%" stop-color="${PEAU.hale[1]}"/>
    </linearGradient>
    <linearGradient id="costFi" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#6a6252"/><stop offset="100%" stop-color="#443f34"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondFi)"/>
  <ellipse cx="100" cy="308" rx="50" ry="9" fill="#000" opacity=".35"/>

  <g class="perso-corps">
    <!-- Jambes courtes (Fix est petit) -->
    <g class="jambes">
      <path d="M74 222 Q70 264 68 296 L90 296 Q93 260 95 222 Z" fill="url(#costFi)"/>
      <path d="M105 222 Q107 260 110 296 L132 296 Q130 264 126 222 Z" fill="url(#costFi)"/>
      <ellipse cx="78" cy="299" rx="15" ry="6" fill="#26221b"/>
      <ellipse cx="122" cy="299" rx="15" ry="6" fill="#26221b"/>
    </g>

    <!-- Bras arrière : tient un mandat d'arrêt roulé -->
    <g class="bras bras-g">
      <path d="M70 158 Q58 182 54 206" stroke="url(#costFi)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M54 206 Q52 220 57 234" stroke="url(#costFi)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="58" cy="240" r="9" fill="url(#peauFi)"/>
        <g transform="rotate(-18 58 240)">
          <rect x="44" y="234" width="30" height="11" rx="5" fill="#f0e6d0" stroke="#c0b49a"/>
          <line x1="49" y1="240" x2="69" y2="240" stroke="#a33327" stroke-width="1.4"/>
        </g>
      </g>
    </g>

    <!-- Buste : costume gris étriqué, gilet boutonné -->
    <g class="buste">
      <path d="M70 156 Q68 142 80 136 L120 136 Q132 142 130 156 L134 222 Q100 230 66 222 Z" fill="url(#costFi)"/>
      <path d="M86 140 Q100 160 114 140 L118 218 Q100 224 82 218 Z" fill="#8a8272"/>
      <g fill="#2f2b22"><circle cx="100" cy="170" r="2.6"/><circle cx="100" cy="186" r="2.6"/><circle cx="100" cy="202" r="2.6"/></g>
      <!-- Revers -->
      <path d="M80 136 Q90 158 100 140 Q110 158 120 136 L122 158 Q100 180 78 158 Z" fill="#524c40"/>
      <!-- Cravate noire étroite -->
      <path d="M95 134 L105 134 L102 168 L100 174 L98 168 Z" fill="#2a2620"/>
      <!-- Cou -->
      <path d="M92 124 L108 124 L108 140 Q100 145 92 140 Z" fill="#d3a273"/>
      <path d="M90 132 L100 140 L110 132" stroke="#f2ece0" stroke-width="3.5" fill="none" stroke-linejoin="round"/>
    </g>

    <!-- Bras avant : brandit une loupe -->
    <g class="bras bras-d">
      <path d="M130 158 Q144 180 148 204" stroke="url(#costFi)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M148 204 Q150 218 146 232" stroke="url(#costFi)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="145" cy="238" r="9" fill="url(#peauFi)"/>
          <!-- Loupe -->
          <line x1="145" y1="234" x2="152" y2="216" stroke="#5a3a1e" stroke-width="3.5" stroke-linecap="round"/>
          <circle cx="154" cy="208" r="11" fill="#cfe6ef" opacity=".55" stroke="#c08a3e" stroke-width="3"/>
        </g>
      </g>
    </g>

    <!-- Tête : chapeau melon, visage maigre, regard en coin -->
    <g class="tete">
      <path d="M72 92 Q70 62 100 60 Q130 62 128 92 Q130 100 126 106 Q128 78 100 76 Q72 78 74 106 Q70 100 72 92" fill="#3a3228"/>
      <!-- Visage étroit -->
      <ellipse cx="100" cy="94" rx="27" ry="33" fill="url(#peauFi)"/>
      <!-- Chapeau melon -->
      <ellipse cx="100" cy="66" rx="40" ry="7" fill="#22201a"/>
      <path d="M76 66 Q76 34 100 32 Q124 34 124 66 Z" fill="#2e2b23"/>
      <rect x="77" y="56" width="46" height="7" fill="#191710"/>
      <!-- Favoris courts -->
      <path d="M75 90 Q73 104 79 114 Q84 108 82 90 Z" fill="#3a3228"/>
      <path d="M125 90 Q127 104 121 114 Q116 108 118 90 Z" fill="#3a3228"/>
      <!-- Sourcils froncés : c'est sa marque -->
      <g class="sourcils">
        <path d="M83 82 Q89 79 95 83" stroke="#2c251c" stroke-width="2.8" fill="none" stroke-linecap="round"/>
        <path d="M105 83 Q111 79 117 82" stroke="#2c251c" stroke-width="2.8" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux plissés, soupçonneux -->
      <g class="yeux">
        <ellipse cx="89" cy="92" rx="5.6" ry="3.8" fill="#fff"/>
        <ellipse cx="111" cy="92" rx="5.6" ry="3.8" fill="#fff"/>
        <circle cx="90" cy="92" r="2.7" fill="#3a2c18"/>
        <circle cx="112" cy="92" r="2.7" fill="#3a2c18"/>
        <circle cx="91" cy="91" r="1" fill="#fff"/>
        <circle cx="113" cy="91" r="1" fill="#fff"/>
        <ellipse class="paupiere" cx="89" cy="92" rx="5.9" ry="4.1" fill="url(#peauFi)"/>
        <ellipse class="paupiere" cx="111" cy="92" rx="5.9" ry="4.1" fill="url(#peauFi)"/>
      </g>
      <!-- Nez pointu -->
      <path d="M100 96 Q95 106 101 108" stroke="#bb8a58" stroke-width="2" fill="none" stroke-linecap="round"/>
      <!-- Fine moustache -->
      <path d="M89 113 Q100 109 111 113" stroke="#3a3228" stroke-width="3.4" fill="none" stroke-linecap="round"/>
      <!-- Bouche pincée -->
      <ellipse class="bouche bouche-ouverte" cx="100" cy="118" rx="6" ry="3.4" fill="#9c4a4a"/>
      <path class="bouche-fermee" d="M93 118 Q100 116 107 118" stroke="#84393c" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>`,
};

/* ============================================================
   GESTES
   @param {HTMLElement|string} cible - élément .portrait ou sélecteur
   @param {string} nomGeste - pointe|joie|inquiet|salue|neutre
   @param {number} duree - ms avant retour au neutre (0 = permanent)
   ============================================================ */
function geste(cible, nomGeste, duree=2200){
  const el = typeof cible === "string" ? document.querySelector(cible) : cible;
  if(!el) return;
  const tous = ["geste-pointe","geste-joie","geste-inquiet","geste-salue"];
  tous.forEach(c=>el.classList.remove(c));
  if(nomGeste && nomGeste !== "neutre"){
    // Forcer le redémarrage de l'animation même si le geste est répété
    void el.offsetWidth;
    el.classList.add("geste-"+nomGeste);
    if(duree > 0){
      setTimeout(()=>el.classList.remove("geste-"+nomGeste), duree);
    }
  }
}

/** Raccourci : le personnage actuellement à l'écran */
function persoCourant(){
  return document.querySelector(".personnage-scene .portrait");
}

window.htmlPortrait = htmlPersonnage;
window.htmlPersonnage = htmlPersonnage;
window.svgPersonnage = svgPersonnage;
window.geste = geste;
window.persoCourant = persoCourant;
window.SVG_PERSOS = SVG_PERSOS;
