/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés
   ------------------------------------------------------------
   Remplace les portraits « buste » par des personnages complets :
   tête, torse, bras articulés, mains, jambes.

   RIG (classes réutilisées par animations.css) :
     .tete .yeux .paupiere .bouche .sourcils   → lip-sync existant
     .buste                                    → respiration
     .bras-g / .bras-d                         → épaule (pivot haut)
     .avant-g / .avant-d                       → coude
     .main-g  / .main-d                        → main
     .jambes                                   → appui / balancement

   Les gestes sont pilotés par des classes posées sur .portrait :
     .parle · .geste-pointe · .geste-joie · .geste-inquiet · .entree
   ============================================================ */

/* ---- Palette commune ---- */
const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e8c39a","#d3a273"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

/**
 * Génère le SVG plein corps d'un personnage.
 * @param {string} perso - louise|gutenberg|marquis|maximilien
 * @returns {string} markup SVG
 */
function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.louise;
}

/**
 * Génère le HTML complet du personnage (image IA prioritaire, sinon SVG).
 * Remplace htmlPortrait() : tous les appels existants bénéficient
 * automatiquement du plein corps, sans modification des autres fichiers.
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
   LOUISE — jeune Parisienne du peuple, 12 ans, vive et curieuse
   ------------------------------------------------------------ */
louise: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondLo" cx="50%" cy="35%" r="75%">
      <stop offset="0%" stop-color="#6b4a33"/><stop offset="100%" stop-color="#1c1220"/>
    </radialGradient>
    <linearGradient id="peauLo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.claire[0]}"/><stop offset="100%" stop-color="${PEAU.claire[1]}"/>
    </linearGradient>
    <linearGradient id="jupeLo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8d6a9c"/><stop offset="100%" stop-color="#5b4068"/>
    </linearGradient>
    <linearGradient id="corsLo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#c9603f"/><stop offset="100%" stop-color="#9a4229"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondLo)"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>

  <g class="perso-corps">
    <!-- Jambes / jupe -->
    <g class="jambes">
      <path d="M66 214 Q60 268 58 296 Q100 304 142 296 Q140 268 134 214 Z" fill="url(#jupeLo)"/>
      <path d="M78 220 Q74 262 72 294" stroke="#4a3356" stroke-width="2.5" fill="none" opacity=".6"/>
      <path d="M100 218 Q99 260 99 296" stroke="#4a3356" stroke-width="2.5" fill="none" opacity=".6"/>
      <path d="M122 220 Q126 262 128 294" stroke="#4a3356" stroke-width="2.5" fill="none" opacity=".6"/>
      <!-- Tablier -->
      <path d="M82 214 Q80 260 79 292 Q100 297 121 292 Q120 260 118 214 Z" fill="#e8ddc4" opacity=".85"/>
      <!-- Sabots -->
      <ellipse cx="82" cy="300" rx="14" ry="6" fill="#6b4a2a"/>
      <ellipse cx="118" cy="300" rx="14" ry="6" fill="#6b4a2a"/>
    </g>

    <!-- Bras arrière (gauche à l'écran) -->
    <g class="bras bras-g">
      <path d="M68 150 Q56 178 52 204" stroke="url(#corsLo)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M52 204 Q50 220 54 234" stroke="url(#corsLo)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="55" cy="240" r="9" fill="url(#peauLo)"/>
      </g>
    </g>

    <!-- Buste -->
    <g class="buste">
      <!-- Corsage -->
      <path d="M70 148 Q68 136 78 130 L122 130 Q132 136 130 148 L134 216 Q100 224 66 216 Z" fill="url(#corsLo)"/>
      <!-- Fichu croisé blanc -->
      <path d="M78 130 Q100 158 122 130 Q130 134 132 146 Q100 176 68 146 Q70 134 78 130" fill="#f2ece0"/>
      <path d="M78 130 Q100 158 122 130" stroke="#cfc4b0" stroke-width="1.5" fill="none"/>
      <!-- Lacet du corsage -->
      <path d="M92 172 L108 180 M92 182 L108 190 M92 192 L108 200" stroke="#f0d98a" stroke-width="2" opacity=".9"/>
      <!-- Cocarde tricolore -->
      <g class="cocarde" transform="translate(126,158)">
        <circle r="8" fill="#c8102e"/><circle r="5.5" fill="#f2ece0"/><circle r="3" fill="#0055a4"/>
      </g>
      <!-- Cou -->
      <path d="M90 120 L110 120 L110 136 Q100 142 90 136 Z" fill="#e0b78f"/>
    </g>

    <!-- Bras avant (droit à l'écran) — celui qui gesticule -->
    <g class="bras bras-d">
      <path d="M132 150 Q146 176 150 202" stroke="url(#corsLo)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M150 202 Q152 218 148 232" stroke="url(#corsLo)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="147" cy="238" r="9.5" fill="url(#peauLo)"/>
          <path d="M143 233 Q140 228 142 224" stroke="url(#peauLo)" stroke-width="4" fill="none" stroke-linecap="round"/>
        </g>
      </g>
    </g>

    <!-- Tête -->
    <g class="tete">
      <!-- Chevelure arrière -->
      <path d="M62 78 Q60 34 100 32 Q140 34 138 78 Q142 104 132 120 Q136 70 100 66 Q64 70 68 120 Q58 104 62 78" fill="#4a2a18"/>
      <!-- Nattes -->
      <path d="M63 88 Q56 114 64 134" stroke="#4a2a18" stroke-width="9" fill="none" stroke-linecap="round"/>
      <path d="M137 88 Q144 114 136 134" stroke="#4a2a18" stroke-width="9" fill="none" stroke-linecap="round"/>
      <circle cx="64" cy="136" r="4" fill="#c8102e"/>
      <circle cx="136" cy="136" r="4" fill="#0055a4"/>
      <!-- Visage -->
      <ellipse cx="100" cy="86" rx="31" ry="36" fill="url(#peauLo)"/>
      <!-- Bonnet / fichu de tête -->
      <path d="M66 64 Q100 44 134 64 Q136 76 100 72 Q64 76 66 64" fill="#dcd2bc"/>
      <!-- Joues -->
      <ellipse cx="82" cy="96" rx="8" ry="5" fill="#e79a97" opacity=".45"/>
      <ellipse cx="118" cy="96" rx="8" ry="5" fill="#e79a97" opacity=".45"/>
      <!-- Sourcils -->
      <g class="sourcils">
        <path d="M82 74 Q88 70 94 74" stroke="#3a1d0a" stroke-width="2.4" fill="none" stroke-linecap="round"/>
        <path d="M106 74 Q112 70 118 74" stroke="#3a1d0a" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux -->
      <g class="yeux">
        <ellipse cx="88" cy="83" rx="6" ry="4.6" fill="#fff"/>
        <ellipse cx="112" cy="83" rx="6" ry="4.6" fill="#fff"/>
        <circle cx="88" cy="83" r="3" fill="#4a2c18"/>
        <circle cx="112" cy="83" r="3" fill="#4a2c18"/>
        <circle cx="89.2" cy="81.8" r="1.1" fill="#fff"/>
        <circle cx="113.2" cy="81.8" r="1.1" fill="#fff"/>
        <ellipse class="paupiere" cx="88" cy="83" rx="6.3" ry="4.9" fill="url(#peauLo)"/>
        <ellipse class="paupiere" cx="112" cy="83" rx="6.3" ry="4.9" fill="url(#peauLo)"/>
      </g>
      <!-- Nez -->
      <path d="M100 88 Q97 95 101 97" stroke="#d4a17a" stroke-width="2" fill="none" stroke-linecap="round"/>
      <!-- Bouche -->
      <ellipse class="bouche bouche-ouverte" cx="100" cy="106" rx="7" ry="4" fill="#a8434a"/>
      <path class="bouche-fermee" d="M93 106 Q100 109 107 106" stroke="#8d3a40" stroke-width="2" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MAÎTRE GUTENBERG — imprimeur barbu, tablier de cuir, lunettes
   ------------------------------------------------------------ */
gutenberg: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondGu" cx="50%" cy="30%" r="75%">
      <stop offset="0%" stop-color="#6a4f2a"/><stop offset="100%" stop-color="#1a1410"/>
    </radialGradient>
    <linearGradient id="peauGu" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.hale[0]}"/><stop offset="100%" stop-color="${PEAU.hale[1]}"/>
    </linearGradient>
    <linearGradient id="tablGu" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#8a5a2e"/><stop offset="100%" stop-color="#5c3a1c"/>
    </linearGradient>
    <linearGradient id="chemGu" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e6dcc4"/><stop offset="100%" stop-color="#c8bb9c"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondGu)"/>
  <ellipse cx="100" cy="308" rx="56" ry="9" fill="#000" opacity=".35"/>

  <g class="perso-corps">
    <!-- Jambes -->
    <g class="jambes">
      <path d="M74 214 L70 292 L88 292 L92 214 Z" fill="#4a4034"/>
      <path d="M108 214 L112 292 L130 292 L126 214 Z" fill="#4a4034"/>
      <ellipse cx="78" cy="298" rx="16" ry="7" fill="#3a2c1c"/>
      <ellipse cx="122" cy="298" rx="16" ry="7" fill="#3a2c1c"/>
    </g>

    <!-- Bras arrière -->
    <g class="bras bras-g">
      <path d="M64 152 Q50 178 46 202" stroke="url(#chemGu)" stroke-width="17" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M46 202 Q44 220 50 234" stroke="url(#peauGu)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="52" cy="241" r="10" fill="url(#peauGu)"/>
      </g>
    </g>

    <!-- Buste -->
    <g class="buste">
      <!-- Chemise ample -->
      <path d="M64 152 Q62 134 78 128 L122 128 Q138 134 136 152 L140 218 Q100 228 60 218 Z" fill="url(#chemGu)"/>
      <!-- Tablier de cuir -->
      <path d="M78 134 Q100 144 122 134 L128 220 Q100 228 72 220 Z" fill="url(#tablGu)"/>
      <path d="M78 134 Q100 144 122 134" stroke="#43290f" stroke-width="2" fill="none"/>
      <!-- Poche du tablier + composteur -->
      <rect x="86" y="182" width="28" height="20" rx="3" fill="#43290f" opacity=".65"/>
      <rect x="90" y="176" width="4" height="14" rx="1" fill="#b9b2a4"/>
      <rect x="97" y="174" width="4" height="16" rx="1" fill="#b9b2a4"/>
      <!-- Taches d'encre -->
      <circle cx="112" cy="164" r="3.5" fill="#1a1a2a" opacity=".55"/>
      <circle cx="120" cy="172" r="2.2" fill="#1a1a2a" opacity=".45"/>
      <!-- Cou -->
      <path d="M90 116 L110 116 L110 132 Q100 138 90 132 Z" fill="#c99a6c"/>
    </g>

    <!-- Bras avant -->
    <g class="bras bras-d">
      <path d="M136 152 Q152 176 156 200" stroke="url(#chemGu)" stroke-width="17" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M156 200 Q158 218 152 232" stroke="url(#peauGu)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="150" cy="239" r="10.5" fill="url(#peauGu)"/>
          <path d="M145 234 Q141 228 143 223" stroke="url(#peauGu)" stroke-width="4.5" fill="none" stroke-linecap="round"/>
          <circle cx="152" cy="242" r="3" fill="#1a1a2a" opacity=".5"/>
        </g>
      </g>
    </g>

    <!-- Tête -->
    <g class="tete">
      <!-- Bonnet d'imprimeur -->
      <path d="M64 62 Q66 36 100 34 Q134 36 136 62 Q138 70 100 68 Q62 70 64 62" fill="#5a4a34"/>
      <path d="M62 62 Q100 54 138 62 Q138 72 100 70 Q62 72 62 62" fill="#463726"/>
      <!-- Visage -->
      <ellipse cx="100" cy="84" rx="32" ry="35" fill="url(#peauGu)"/>
      <!-- Cheveux latéraux grisonnants -->
      <path d="M67 74 Q62 96 70 114" stroke="#8e8378" stroke-width="8" fill="none" stroke-linecap="round"/>
      <path d="M133 74 Q138 96 130 114" stroke="#8e8378" stroke-width="8" fill="none" stroke-linecap="round"/>
      <!-- Sourcils broussailleux -->
      <g class="sourcils">
        <path d="M79 72 Q88 66 96 72" stroke="#7a6a58" stroke-width="4" fill="none" stroke-linecap="round"/>
        <path d="M104 72 Q112 66 121 72" stroke="#7a6a58" stroke-width="4" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux -->
      <g class="yeux">
        <ellipse cx="88" cy="82" rx="6" ry="4.4" fill="#fff"/>
        <ellipse cx="112" cy="82" rx="6" ry="4.4" fill="#fff"/>
        <circle cx="88" cy="82" r="2.9" fill="#3a5a4a"/>
        <circle cx="112" cy="82" r="2.9" fill="#3a5a4a"/>
        <circle cx="89.1" cy="80.9" r="1" fill="#fff"/>
        <circle cx="113.1" cy="80.9" r="1" fill="#fff"/>
        <ellipse class="paupiere" cx="88" cy="82" rx="6.3" ry="4.7" fill="url(#peauGu)"/>
        <ellipse class="paupiere" cx="112" cy="82" rx="6.3" ry="4.7" fill="url(#peauGu)"/>
      </g>
      <!-- Lunettes rondes -->
      <g class="lunettes" opacity=".92">
        <circle cx="88" cy="82" r="11" fill="none" stroke="#c9a227" stroke-width="2"/>
        <circle cx="112" cy="82" r="11" fill="none" stroke="#c9a227" stroke-width="2"/>
        <path d="M99 82 L101 82" stroke="#c9a227" stroke-width="2"/>
        <path d="M77 80 L68 76 M123 80 L132 76" stroke="#c9a227" stroke-width="1.8" fill="none"/>
      </g>
      <!-- Nez -->
      <path d="M100 86 Q96 95 102 98" stroke="#b8825a" stroke-width="2.2" fill="none" stroke-linecap="round"/>
      <!-- Barbe -->
      <path d="M74 96 Q76 128 100 134 Q124 128 126 96 Q120 116 100 118 Q80 116 74 96" fill="#8e8378"/>
      <!-- Moustache -->
      <path d="M86 104 Q100 100 114 104 Q108 110 100 108 Q92 110 86 104" fill="#9a8f84"/>
      <!-- Bouche (entre moustache et barbe) -->
      <ellipse class="bouche bouche-ouverte" cx="100" cy="112" rx="7" ry="3.6" fill="#7a3238"/>
      <path class="bouche-fermee" d="M93 112 Q100 115 107 112" stroke="#6a2a30" stroke-width="2" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MARQUIS DE MONTCLAIR — aristocrate, perruque poudrée, habit de soie
   ------------------------------------------------------------ */
marquis: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondMa" cx="50%" cy="30%" r="75%">
      <stop offset="0%" stop-color="#3a4a6a"/><stop offset="100%" stop-color="#141020"/>
    </radialGradient>
    <linearGradient id="peauMa" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.pale[0]}"/><stop offset="100%" stop-color="${PEAU.pale[1]}"/>
    </linearGradient>
    <linearGradient id="habitMa" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#3c5f9c"/><stop offset="100%" stop-color="#223a68"/>
    </linearGradient>
    <linearGradient id="gileMa" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f0e2b8"/><stop offset="100%" stop-color="#d8c48e"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondMa)"/>
  <ellipse cx="100" cy="308" rx="54" ry="9" fill="#000" opacity=".35"/>

  <g class="perso-corps">
    <!-- Jambes : culotte + bas blancs -->
    <g class="jambes">
      <path d="M76 210 L72 244 L90 244 L92 210 Z" fill="#223a68"/>
      <path d="M108 210 L110 244 L128 244 L124 210 Z" fill="#223a68"/>
      <path d="M74 244 Q72 272 76 292 L88 292 Q90 268 90 244 Z" fill="#eae4d4"/>
      <path d="M110 244 Q110 268 112 292 L124 292 Q128 272 126 244 Z" fill="#eae4d4"/>
      <!-- Souliers à boucle -->
      <ellipse cx="80" cy="298" rx="15" ry="6.5" fill="#2a2018"/>
      <ellipse cx="120" cy="298" rx="15" ry="6.5" fill="#2a2018"/>
      <rect x="75" y="293" width="7" height="5" rx="1" fill="#d8c48e"/>
      <rect x="115" y="293" width="7" height="5" rx="1" fill="#d8c48e"/>
    </g>

    <!-- Bras arrière -->
    <g class="bras bras-g">
      <path d="M66 150 Q52 176 48 200" stroke="url(#habitMa)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M48 200 Q46 218 52 232" stroke="url(#habitMa)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <!-- Manchette de dentelle -->
        <path d="M46 228 Q52 234 58 228 Q56 238 52 238 Q48 238 46 228" fill="#f2ece0"/>
        <circle class="main-g" cx="53" cy="243" r="9" fill="url(#peauMa)"/>
      </g>
    </g>

    <!-- Buste -->
    <g class="buste">
      <!-- Habit bleu -->
      <path d="M66 150 Q64 132 80 126 L120 126 Q136 132 134 150 L138 214 Q100 222 62 214 Z" fill="url(#habitMa)"/>
      <!-- Gilet brodé -->
      <path d="M84 130 Q100 142 116 130 L120 216 Q100 222 80 216 Z" fill="url(#gileMa)"/>
      <!-- Boutons dorés -->
      <circle cx="100" cy="158" r="3" fill="#c9a227"/>
      <circle cx="100" cy="174" r="3" fill="#c9a227"/>
      <circle cx="100" cy="190" r="3" fill="#c9a227"/>
      <circle cx="100" cy="206" r="3" fill="#c9a227"/>
      <!-- Revers galonnés -->
      <path d="M80 126 Q86 156 78 190" stroke="#c9a227" stroke-width="2.5" fill="none" opacity=".85"/>
      <path d="M120 126 Q114 156 122 190" stroke="#c9a227" stroke-width="2.5" fill="none" opacity=".85"/>
      <!-- Jabot de dentelle -->
      <path d="M88 122 Q100 118 112 122 Q114 140 100 152 Q86 140 88 122" fill="#f6f1e6"/>
      <path d="M94 128 Q100 134 106 128 M94 138 Q100 144 106 138" stroke="#d8d0c0" stroke-width="1.4" fill="none"/>
      <!-- Cou -->
      <path d="M91 112 L109 112 L109 126 Q100 131 91 126 Z" fill="#e2cbb0"/>
    </g>

    <!-- Bras avant : tient une canne -->
    <g class="bras bras-d">
      <path d="M134 150 Q150 174 154 198" stroke="url(#habitMa)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M154 198 Q156 216 150 230" stroke="url(#habitMa)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <path d="M144 226 Q150 232 157 226 Q155 236 150 236 Q146 236 144 226" fill="#f2ece0"/>
        <g class="main-d">
          <circle cx="150" cy="240" r="9.5" fill="url(#peauMa)"/>
          <!-- Canne -->
          <path d="M150 234 L150 296" stroke="#5a3a20" stroke-width="4" stroke-linecap="round"/>
          <circle cx="150" cy="232" r="5" fill="#c9a227"/>
        </g>
      </g>
    </g>

    <!-- Tête -->
    <g class="tete">
      <!-- Perruque poudrée -->
      <path d="M62 74 Q60 32 100 30 Q140 32 138 74 Q140 92 132 104 Q136 66 100 62 Q64 66 68 104 Q60 92 62 74" fill="#eae6dc"/>
      <!-- Rouleaux latéraux -->
      <ellipse cx="66" cy="92" rx="12" ry="9" fill="#eae6dc"/>
      <ellipse cx="134" cy="92" rx="12" ry="9" fill="#eae6dc"/>
      <ellipse cx="66" cy="92" rx="12" ry="9" fill="none" stroke="#d2ccbe" stroke-width="1.5"/>
      <ellipse cx="134" cy="92" rx="12" ry="9" fill="none" stroke="#d2ccbe" stroke-width="1.5"/>
      <!-- Catogan (queue nouée) -->
      <path d="M100 108 Q104 124 100 138" stroke="#eae6dc" stroke-width="9" fill="none" stroke-linecap="round"/>
      <rect x="94" y="118" width="12" height="6" rx="2" fill="#1a1a2a"/>
      <!-- Visage -->
      <ellipse cx="100" cy="84" rx="30" ry="34" fill="url(#peauMa)"/>
      <!-- Mouche (grain de beauté à la mode) -->
      <circle cx="116" cy="98" r="2" fill="#2a1a10"/>
      <!-- Sourcils hautains -->
      <g class="sourcils">
        <path d="M82 72 Q89 67 96 71" stroke="#8a7a68" stroke-width="2.4" fill="none" stroke-linecap="round"/>
        <path d="M104 71 Q111 67 118 72" stroke="#8a7a68" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux -->
      <g class="yeux">
        <ellipse cx="89" cy="82" rx="5.8" ry="4.2" fill="#fff"/>
        <ellipse cx="111" cy="82" rx="5.8" ry="4.2" fill="#fff"/>
        <circle cx="89" cy="82" r="2.8" fill="#4a5a6a"/>
        <circle cx="111" cy="82" r="2.8" fill="#4a5a6a"/>
        <circle cx="90.1" cy="80.9" r="1" fill="#fff"/>
        <circle cx="112.1" cy="80.9" r="1" fill="#fff"/>
        <ellipse class="paupiere" cx="89" cy="82" rx="6.1" ry="4.5" fill="url(#peauMa)"/>
        <ellipse class="paupiere" cx="111" cy="82" rx="6.1" ry="4.5" fill="url(#peauMa)"/>
      </g>
      <!-- Nez aquilin -->
      <path d="M100 84 Q95 94 102 97" stroke="#d3b394" stroke-width="2.2" fill="none" stroke-linecap="round"/>
      <!-- Bouche -->
      <ellipse class="bouche bouche-ouverte" cx="100" cy="106" rx="6.5" ry="3.6" fill="#a05058"/>
      <path class="bouche-fermee" d="M94 106 Q100 108 106 105" stroke="#8a4048" stroke-width="2" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MAXIMILIEN — jeune avocat idéaliste, écharpe tricolore
   ------------------------------------------------------------ */
maximilien: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondMx" cx="50%" cy="30%" r="75%">
      <stop offset="0%" stop-color="#2f4a44"/><stop offset="100%" stop-color="#12161a"/>
    </radialGradient>
    <linearGradient id="peauMx" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.claire[0]}"/><stop offset="100%" stop-color="${PEAU.claire[1]}"/>
    </linearGradient>
    <linearGradient id="habitMx" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#2e5248"/><stop offset="100%" stop-color="#1a332e"/>
    </linearGradient>
    <linearGradient id="gileMx" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#eee8da"/><stop offset="100%" stop-color="#d4ccb8"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondMx)"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>

  <g class="perso-corps">
    <!-- Jambes -->
    <g class="jambes">
      <path d="M76 212 L72 246 L90 246 L92 212 Z" fill="#1a332e"/>
      <path d="M108 212 L110 246 L128 246 L124 212 Z" fill="#1a332e"/>
      <path d="M74 246 Q72 272 76 292 L88 292 Q90 268 90 246 Z" fill="#e6e0d0"/>
      <path d="M110 246 Q110 268 112 292 L124 292 Q128 272 126 246 Z" fill="#e6e0d0"/>
      <ellipse cx="80" cy="298" rx="15" ry="6.5" fill="#2a2018"/>
      <ellipse cx="120" cy="298" rx="15" ry="6.5" fill="#2a2018"/>
    </g>

    <!-- Bras arrière -->
    <g class="bras bras-g">
      <path d="M66 152 Q52 178 48 202" stroke="url(#habitMx)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M48 202 Q46 220 52 234" stroke="url(#habitMx)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <!-- Rouleau de papier tenu dans la main gauche -->
        <g class="main-g">
          <circle cx="53" cy="242" r="9" fill="url(#peauMx)"/>
          <rect x="38" y="232" width="26" height="9" rx="4" fill="#f2e8cf" transform="rotate(-14 51 236)"/>
          <path d="M40 234 L60 229" stroke="#c9bda0" stroke-width="1.2"/>
        </g>
      </g>
    </g>

    <!-- Buste -->
    <g class="buste">
      <!-- Habit vert sombre -->
      <path d="M66 152 Q64 134 80 128 L120 128 Q136 134 134 152 L138 216 Q100 224 62 216 Z" fill="url(#habitMx)"/>
      <!-- Gilet clair -->
      <path d="M84 132 Q100 144 116 132 L119 218 Q100 224 81 218 Z" fill="url(#gileMx)"/>
      <!-- Écharpe tricolore en bandoulière -->
      <path d="M70 140 L128 224 L140 216 L82 132 Z" fill="#0055a4" opacity=".95"/>
      <path d="M76 136 L134 220 L140 216 L82 132 Z" fill="#f2ece0" opacity=".95"/>
      <path d="M80 133 L138 217 L142 210 L86 129 Z" fill="#c8102e" opacity=".95"/>
      <!-- Cravate blanche montante -->
      <path d="M88 124 Q100 118 112 124 Q116 138 100 148 Q84 138 88 124" fill="#f6f1e6"/>
      <path d="M92 130 Q100 136 108 130" stroke="#d8d0c0" stroke-width="1.4" fill="none"/>
      <!-- Cou -->
      <path d="M91 114 L109 114 L109 128 Q100 133 91 128 Z" fill="#dcb492"/>
    </g>

    <!-- Bras avant : geste oratoire -->
    <g class="bras bras-d">
      <path d="M134 152 Q150 176 154 200" stroke="url(#habitMx)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M154 200 Q156 218 150 232" stroke="url(#habitMx)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="149" cy="239" r="9.5" fill="url(#peauMx)"/>
          <!-- Index tendu (geste de l'orateur) -->
          <path d="M145 233 Q141 226 143 220" stroke="url(#peauMx)" stroke-width="4.5" fill="none" stroke-linecap="round"/>
        </g>
      </g>
    </g>

    <!-- Tête -->
    <g class="tete">
      <!-- Cheveux tirés en arrière + catogan -->
      <path d="M64 76 Q62 36 100 34 Q138 36 136 76 Q138 92 130 104 Q134 68 100 64 Q66 68 70 104 Q62 92 64 76" fill="#6a5236"/>
      <path d="M100 106 Q104 122 100 134" stroke="#6a5236" stroke-width="8" fill="none" stroke-linecap="round"/>
      <rect x="95" y="116" width="10" height="5" rx="2" fill="#1a1a2a"/>
      <!-- Visage -->
      <ellipse cx="100" cy="84" rx="30" ry="34" fill="url(#peauMx)"/>
      <!-- Sourcils décidés -->
      <g class="sourcils">
        <path d="M82 71 Q89 67 96 71" stroke="#4a3a24" stroke-width="2.6" fill="none" stroke-linecap="round"/>
        <path d="M104 71 Q111 67 118 71" stroke="#4a3a24" stroke-width="2.6" fill="none" stroke-linecap="round"/>
      </g>
      <!-- Yeux -->
      <g class="yeux">
        <ellipse cx="89" cy="82" rx="5.8" ry="4.4" fill="#fff"/>
        <ellipse cx="111" cy="82" rx="5.8" ry="4.4" fill="#fff"/>
        <circle cx="89" cy="82" r="2.9" fill="#2f5a4a"/>
        <circle cx="111" cy="82" r="2.9" fill="#2f5a4a"/>
        <circle cx="90.1" cy="80.9" r="1" fill="#fff"/>
        <circle cx="112.1" cy="80.9" r="1" fill="#fff"/>
        <ellipse class="paupiere" cx="89" cy="82" rx="6.1" ry="4.7" fill="url(#peauMx)"/>
        <ellipse class="paupiere" cx="111" cy="82" rx="6.1" ry="4.7" fill="url(#peauMx)"/>
      </g>
      <!-- Nez -->
      <path d="M100 85 Q96 94 102 97" stroke="#d4a17a" stroke-width="2.2" fill="none" stroke-linecap="round"/>
      <!-- Bouche -->
      <ellipse class="bouche bouche-ouverte" cx="100" cy="106" rx="6.8" ry="3.8" fill="#a04a50"/>
      <path class="bouche-fermee" d="M93 106 Q100 109 107 106" stroke="#8a3a42" stroke-width="2" fill="none" stroke-linecap="round"/>
    </g>
  </g>
</svg>`

};

/* ============================================================
   GESTES — pilotage depuis le jeu
   ============================================================ */

/**
 * Applique un geste à un personnage affiché.
 * @param {HTMLElement|string} cible - élément .portrait ou sélecteur
 * @param {string} geste - pointe|joie|inquiet|salue|neutre
 * @param {number} duree - ms avant retour au neutre (0 = permanent)
 */
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

/* ---- Remplacement transparent de l'ancienne API ----
   portraits.js définit htmlPortrait() ; on l'écrase ici pour que
   TOUS les appels existants (narration.js, index.html, app.js)
   affichent désormais le personnage plein corps. ---- */
window.htmlPortrait = htmlPersonnage;
window.htmlPersonnage = htmlPersonnage;
window.svgPersonnage = svgPersonnage;
window.geste = geste;
window.persoCourant = persoCourant;
window.SVG_PERSOS = SVG_PERSOS;
