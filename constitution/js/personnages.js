/* ============================================================
   PERSONNAGES PLEIN CORPS — SVG animés
   ------------------------------------------------------------
   RIG (classes réutilisées par css/animations.css) :
     .tete .yeux .paupiere .bouche .sourcils   → lip-sync
     .buste                                    → respiration
     .bras-g / .bras-d  .avant-g / .avant-d    → épaule / coude
     .main-g  / .main-d                        → mains
     .jambes                                   → appui

   Gestes pilotés par des classes posées sur .portrait :
     .parle · .geste-pointe · .geste-joie · .geste-inquiet · .geste-salue

   Cascade d'affichage (voir js/media.js) :
     VIDÉO assets/videos/personnages/<nom>.mp4
   → IMAGE assets/images/personnages/<nom>.png
   → SVG dessiné ci-dessous
   ============================================================ */

const PEAU = {
  claire: ["#f6dcc0","#e9c49e"],
  hale:   ["#e2b183","#c48f5e"],
  foncee: ["#a2663c","#7d4a28"],
  pale:   ["#f8e6d2","#ecd0b4"],
};

function svgPersonnage(perso){
  return SVG_PERSOS[perso] || SVG_PERSOS.nour;
}

/** HTML complet d'un personnage (image si présente, sinon SVG). */
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

/** Version de base : media.js la remplace par la cascade vidéo/image. */
function activerPortraitBase(conteneur){
  if(!conteneur) return;
  const img = conteneur.querySelector(".portrait-img-cachee");
  const svg = conteneur.querySelector(".portrait-svg");
  if(!img || !svg) return;
  const test = new Image();
  test.onload = ()=>{ img.style.display="block"; svg.style.display="none"; };
  test.src = img.src;
}

/* ---- Fragments réutilisés : un visage complet ----
   idPeau : identifiant du dégradé de peau déjà déclaré dans <defs>. */
function visage({idPeau, oeil="#3a2a1a", sourcil="#3a2a1a", joue=".35", nez="#c89a70", bouche="#a8434a", levre="#8d3a40"}){
  return `
      <ellipse cx="100" cy="86" rx="31" ry="36" fill="url(#${idPeau})"/>
      <ellipse cx="82" cy="97" rx="8" ry="5" fill="#e79a97" opacity="${joue}"/>
      <ellipse cx="118" cy="97" rx="8" ry="5" fill="#e79a97" opacity="${joue}"/>
      <g class="sourcils">
        <path d="M82 74 Q88 70 94 74" stroke="${sourcil}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
        <path d="M106 74 Q112 70 118 74" stroke="${sourcil}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      </g>
      <g class="yeux">
        <ellipse cx="88" cy="83" rx="6" ry="4.6" fill="#fff"/>
        <ellipse cx="112" cy="83" rx="6" ry="4.6" fill="#fff"/>
        <circle cx="88" cy="83" r="3" fill="${oeil}"/>
        <circle cx="112" cy="83" r="3" fill="${oeil}"/>
        <circle cx="89.2" cy="81.8" r="1.1" fill="#fff"/>
        <circle cx="113.2" cy="81.8" r="1.1" fill="#fff"/>
        <ellipse class="paupiere" cx="88" cy="83" rx="6.3" ry="4.9" fill="url(#${idPeau})"/>
        <ellipse class="paupiere" cx="112" cy="83" rx="6.3" ry="4.9" fill="url(#${idPeau})"/>
      </g>
      <path d="M100 88 Q97 95 101 97" stroke="${nez}" stroke-width="2" fill="none" stroke-linecap="round"/>
      <ellipse class="bouche bouche-ouverte" cx="100" cy="107" rx="7" ry="4" fill="${bouche}"/>
      <path class="bouche-fermee" d="M93 107 Q100 110 107 107" stroke="${levre}" stroke-width="2" fill="none" stroke-linecap="round"/>`;
}

/* ============================================================
   BIBLIOTHÈQUE DES PERSONNAGES — viewBox 200 × 320
   ============================================================ */
const SVG_PERSOS = {

/* ------------------------------------------------------------
   NOUR — 10 ans, déléguée de classe, curieuse et rapide
   ------------------------------------------------------------ */
nour: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondNo" cx="50%" cy="32%" r="78%">
      <stop offset="0%" stop-color="#3b5a7a"/><stop offset="100%" stop-color="#111a26"/>
    </radialGradient>
    <linearGradient id="peauNo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.hale[0]}"/><stop offset="100%" stop-color="${PEAU.hale[1]}"/>
    </linearGradient>
    <linearGradient id="sweatNo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f0b429"/><stop offset="100%" stop-color="#c98a12"/>
    </linearGradient>
    <linearGradient id="jeanNo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3f5f8a"/><stop offset="100%" stop-color="#27405e"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondNo)"/>
  <ellipse cx="100" cy="308" rx="50" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M76 212 L70 292 L90 292 L94 212 Z" fill="url(#jeanNo)"/>
      <path d="M106 212 L110 292 L130 292 L124 212 Z" fill="url(#jeanNo)"/>
      <path d="M78 250 L92 250 M108 250 L124 250" stroke="#1e3247" stroke-width="1.5" opacity=".6"/>
      <ellipse cx="80" cy="298" rx="16" ry="7" fill="#e8e4dc"/>
      <ellipse cx="120" cy="298" rx="16" ry="7" fill="#e8e4dc"/>
      <path d="M64 298 Q80 292 96 298" stroke="#c0392b" stroke-width="2" fill="none"/>
      <path d="M104 298 Q120 292 136 298" stroke="#c0392b" stroke-width="2" fill="none"/>
    </g>
    <g class="bras bras-g">
      <path d="M70 152 Q58 180 54 206" stroke="url(#sweatNo)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M54 206 Q52 222 56 236" stroke="url(#sweatNo)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="57" cy="242" r="9" fill="url(#peauNo)"/>
      </g>
    </g>
    <g class="buste">
      <path d="M70 148 Q68 134 80 128 L120 128 Q132 134 130 148 L134 214 Q100 222 66 214 Z" fill="url(#sweatNo)"/>
      <path d="M84 128 Q100 146 116 128 Q122 132 124 140 Q100 160 76 140 Q78 132 84 128" fill="#fdf3d8" opacity=".92"/>
      <!-- badge de déléguée -->
      <g transform="translate(124,166)">
        <rect x="-13" y="-9" width="26" height="18" rx="3" fill="#ffffff" stroke="#8a6d12"/>
        <rect x="-10" y="-6" width="7" height="12" fill="#0055a4"/><rect x="-3" y="-6" width="6" height="12" fill="#f4f4f4"/><rect x="3" y="-6" width="7" height="12" fill="#ef4135"/>
      </g>
      <path d="M90 118 L110 118 L110 134 Q100 140 90 134 Z" fill="#cf9a6a"/>
    </g>
    <g class="bras bras-d">
      <path d="M130 152 Q144 178 148 204" stroke="url(#sweatNo)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M148 204 Q150 220 146 234" stroke="url(#sweatNo)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="145" cy="240" r="9.5" fill="url(#peauNo)"/>
          <path d="M141 235 Q138 230 140 226" stroke="url(#peauNo)" stroke-width="4" fill="none" stroke-linecap="round"/>
        </g>
      </g>
    </g>
    <g class="tete">
      <path d="M60 80 Q58 32 100 30 Q142 32 140 80 Q144 100 134 116 Q138 66 100 62 Q62 66 66 116 Q56 100 60 80" fill="#2f1d12"/>
      <circle cx="63" cy="52" r="11" fill="#2f1d12"/><circle cx="137" cy="52" r="11" fill="#2f1d12"/>
      <circle cx="72" cy="38" r="12" fill="#2f1d12"/><circle cx="128" cy="38" r="12" fill="#2f1d12"/>
      <circle cx="100" cy="30" r="13" fill="#2f1d12"/>
      ${visage({idPeau:"peauNo", oeil:"#2e1c10", sourcil:"#2a1608", nez:"#b07a4e"})}
      <path d="M68 60 Q100 40 132 60 Q134 70 100 66 Q66 70 68 60" fill="#2f1d12"/>
      <circle cx="132" cy="56" r="5" fill="#ef4135"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MONSIEUR BERTHIER — gardien-archiviste du Palais-Royal
   ------------------------------------------------------------ */
berthier: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondBe" cx="50%" cy="30%" r="78%">
      <stop offset="0%" stop-color="#5a4a32"/><stop offset="100%" stop-color="#18130d"/>
    </radialGradient>
    <linearGradient id="peauBe" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.pale[0]}"/><stop offset="100%" stop-color="${PEAU.pale[1]}"/>
    </linearGradient>
    <linearGradient id="vesteBe" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2b3c5c"/><stop offset="100%" stop-color="#18253c"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondBe)"/>
  <ellipse cx="100" cy="308" rx="56" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M74 214 L70 292 L90 292 L93 214 Z" fill="#33404f"/>
      <path d="M107 214 L110 292 L130 292 L126 214 Z" fill="#33404f"/>
      <ellipse cx="79" cy="298" rx="17" ry="7" fill="#1c1a17"/>
      <ellipse cx="121" cy="298" rx="17" ry="7" fill="#1c1a17"/>
    </g>
    <g class="bras bras-g">
      <path d="M68 152 Q54 180 50 208" stroke="url(#vesteBe)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M50 208 Q48 224 52 238" stroke="url(#vesteBe)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="53" cy="244" r="9" fill="url(#peauBe)"/>
        <!-- trousseau de clés -->
        <g transform="translate(53,254)">
          <circle r="5" fill="none" stroke="#c9a227" stroke-width="2"/>
          <path d="M-3 4 L-6 14 L-3 14 M-6 10 L-9 10" stroke="#c9a227" stroke-width="2" fill="none"/>
          <path d="M3 4 L6 16 L3 16 M6 11 L9 11" stroke="#b08d1e" stroke-width="2" fill="none"/>
        </g>
      </g>
    </g>
    <g class="buste">
      <path d="M68 150 Q66 132 80 126 L120 126 Q134 132 132 150 L136 216 Q100 224 64 216 Z" fill="url(#vesteBe)"/>
      <path d="M84 126 L100 168 L116 126 Q124 130 128 142 L120 214 L80 214 L72 142 Q76 130 84 126" fill="#e8e2d4"/>
      <path d="M96 128 L100 150 L104 128 Z" fill="#7b1f24"/>
      <path d="M100 150 L96 200 L104 200 Z" fill="#7b1f24"/>
      <!-- écusson -->
      <g transform="translate(122,158)">
        <path d="M-8 -9 L8 -9 L8 4 Q0 12 -8 4 Z" fill="#c9a227" stroke="#8a6d12"/>
        <text y="2" font-size="8" text-anchor="middle" fill="#3a2c0a" font-family="Georgia,serif">RF</text>
      </g>
      <path d="M90 116 L110 116 L110 132 Q100 138 90 132 Z" fill="#dcc0a4"/>
    </g>
    <g class="bras bras-d">
      <path d="M132 152 Q146 178 150 206" stroke="url(#vesteBe)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M150 206 Q152 222 148 236" stroke="url(#vesteBe)" stroke-width="14" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="147" cy="242" r="9.5" fill="url(#peauBe)"/>
          <path d="M143 237 Q140 232 142 228" stroke="url(#peauBe)" stroke-width="4" fill="none" stroke-linecap="round"/>
        </g>
      </g>
    </g>
    <g class="tete">
      <path d="M64 78 Q62 44 100 42 Q138 44 136 78 Q140 92 132 102 Q136 64 100 60 Q64 64 68 102 Q60 92 64 78" fill="#cfcac2"/>
      ${visage({idPeau:"peauBe", oeil:"#3f4a55", sourcil:"#9a948a", joue:".28", nez:"#d2ac86"})}
      <!-- moustache -->
      <path d="M86 100 Q100 96 114 100 Q100 106 86 100" fill="#cfcac2"/>
      <!-- lunettes -->
      <g fill="none" stroke="#6b6b6b" stroke-width="2">
        <circle cx="88" cy="83" r="9"/><circle cx="112" cy="83" r="9"/>
        <path d="M97 83 L103 83"/><path d="M79 82 L69 78"/><path d="M121 82 L131 78"/>
      </g>
      <!-- rides -->
      <path d="M74 70 Q80 66 86 68" stroke="#cdbfae" stroke-width="1.4" fill="none"/>
      <path d="M114 68 Q120 66 126 70" stroke="#cdbfae" stroke-width="1.4" fill="none"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MADAME FERRAND — députée à l'Assemblée nationale
   ------------------------------------------------------------ */
ferrand: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondFe" cx="50%" cy="30%" r="78%">
      <stop offset="0%" stop-color="#6b4046"/><stop offset="100%" stop-color="#1a1014"/>
    </radialGradient>
    <linearGradient id="peauFe" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.claire[0]}"/><stop offset="100%" stop-color="${PEAU.claire[1]}"/>
    </linearGradient>
    <linearGradient id="tailFe" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2f4f7a"/><stop offset="100%" stop-color="#1c3453"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondFe)"/>
  <ellipse cx="100" cy="308" rx="52" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M72 214 Q68 258 68 288 Q100 296 132 288 Q132 258 128 214 Z" fill="url(#tailFe)"/>
      <path d="M86 288 L84 300 M114 288 L116 300" stroke="#e0c0a4" stroke-width="8" stroke-linecap="round"/>
      <ellipse cx="83" cy="302" rx="12" ry="5" fill="#2a2320"/>
      <ellipse cx="117" cy="302" rx="12" ry="5" fill="#2a2320"/>
    </g>
    <g class="bras bras-g">
      <path d="M70 150 Q56 178 52 204" stroke="url(#tailFe)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M52 204 Q50 220 54 234" stroke="url(#tailFe)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="55" cy="240" r="9" fill="url(#peauFe)"/>
      </g>
    </g>
    <g class="buste">
      <path d="M70 148 Q68 132 80 126 L120 126 Q132 132 130 148 L134 216 Q100 224 66 216 Z" fill="url(#tailFe)"/>
      <path d="M86 126 Q100 152 114 126 Q120 130 122 140 Q100 166 78 140 Q80 130 86 126" fill="#f3efe6"/>
      <!-- écharpe tricolore d'élue, portée en travers -->
      <path d="M78 132 L128 214 L138 206 L90 128 Z" fill="#0055a4"/>
      <path d="M84 130 L134 210 L142 202 L94 126 Z" fill="#f4f4f4" opacity=".95"/>
      <path d="M90 128 L140 206 L148 198 L100 124 Z" fill="#ef4135"/>
      <path d="M90 116 L110 116 L110 132 Q100 138 90 132 Z" fill="#e0b78f"/>
    </g>
    <g class="bras bras-d">
      <path d="M130 150 Q144 176 148 202" stroke="url(#tailFe)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M148 202 Q150 218 146 232" stroke="url(#tailFe)" stroke-width="13" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="145" cy="238" r="9.5" fill="url(#peauFe)"/>
          <path d="M141 233 Q138 228 140 224" stroke="url(#peauFe)" stroke-width="4" fill="none" stroke-linecap="round"/>
        </g>
      </g>
    </g>
    <g class="tete">
      <path d="M62 80 Q60 36 100 34 Q140 36 138 80 Q142 96 132 110 Q136 66 100 62 Q64 66 68 110 Q58 96 62 80" fill="#6b3a1e"/>
      <path d="M62 86 Q52 108 60 126 Q66 104 66 88 Z" fill="#6b3a1e"/>
      <path d="M138 86 Q148 108 140 126 Q134 104 134 88 Z" fill="#6b3a1e"/>
      ${visage({idPeau:"peauFe", oeil:"#2f5d4a", sourcil:"#4a2a12", nez:"#d4a17a", bouche:"#a8434a"})}
      <path d="M66 62 Q100 44 134 62 Q136 74 100 68 Q64 74 66 62" fill="#6b3a1e"/>
      <!-- boucles d'oreilles discrètes -->
      <circle cx="68" cy="94" r="2.6" fill="#c9a227"/><circle cx="132" cy="94" r="2.6" fill="#c9a227"/>
    </g>
  </g>
</svg>`,

/* ------------------------------------------------------------
   MAÎTRE SYLLA — juriste au Conseil constitutionnel
   ------------------------------------------------------------ */
sylla: `<svg class="portrait-svg-interne perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet">
  <defs>
    <radialGradient id="fondSy" cx="50%" cy="28%" r="78%">
      <stop offset="0%" stop-color="#33405e"/><stop offset="100%" stop-color="#0e1320"/>
    </radialGradient>
    <linearGradient id="peauSy" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="${PEAU.foncee[0]}"/><stop offset="100%" stop-color="${PEAU.foncee[1]}"/>
    </linearGradient>
    <linearGradient id="robeSy" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#30302f"/><stop offset="100%" stop-color="#15151a"/>
    </linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#fondSy)"/>
  <ellipse cx="100" cy="308" rx="58" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M62 206 Q56 258 54 296 Q100 304 146 296 Q144 258 138 206 Z" fill="url(#robeSy)"/>
      <path d="M100 210 L100 298" stroke="#0c0c10" stroke-width="2" opacity=".7"/>
      <ellipse cx="82" cy="300" rx="14" ry="6" fill="#0b0b0e"/>
      <ellipse cx="118" cy="300" rx="14" ry="6" fill="#0b0b0e"/>
    </g>
    <g class="bras bras-g">
      <path d="M66 152 Q50 182 46 210" stroke="url(#robeSy)" stroke-width="18" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M46 210 Q44 226 48 240" stroke="url(#robeSy)" stroke-width="16" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="49" cy="246" r="9" fill="url(#peauSy)"/>
      </g>
    </g>
    <g class="buste">
      <path d="M66 150 Q64 132 80 126 L120 126 Q136 132 134 150 L140 218 Q100 226 60 218 Z" fill="url(#robeSy)"/>
      <!-- rabat blanc -->
      <path d="M92 124 L108 124 L108 134 L112 156 L100 162 L88 156 L92 134 Z" fill="#f7f7f4"/>
      <path d="M100 130 L100 158" stroke="#d8d8d2" stroke-width="1.4"/>
      <!-- épitoge -->
      <path d="M74 132 Q70 170 72 200 L84 200 Q82 168 86 134 Z" fill="#22222a"/>
      <path d="M90 118 L110 118 L110 132 Q100 138 90 132 Z" fill="#8e5a34"/>
    </g>
    <g class="bras bras-d">
      <path d="M134 152 Q150 180 154 208" stroke="url(#robeSy)" stroke-width="18" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M154 208 Q156 224 152 238" stroke="url(#robeSy)" stroke-width="16" fill="none" stroke-linecap="round"/>
        <g class="main-d">
          <circle cx="151" cy="244" r="9.5" fill="url(#peauSy)"/>
          <path d="M147 239 Q144 234 146 230" stroke="url(#peauSy)" stroke-width="4" fill="none" stroke-linecap="round"/>
          <!-- dossier tenu à la main -->
          <g transform="translate(160,240) rotate(12)">
            <rect x="-10" y="-14" width="20" height="28" rx="2" fill="#f2ead6" stroke="#c9a227"/>
            <rect x="-6" y="-8" width="12" height="2" fill="#a89a78"/><rect x="-6" y="-3" width="12" height="2" fill="#a89a78"/><rect x="-6" y="2" width="8" height="2" fill="#a89a78"/>
          </g>
        </g>
      </g>
    </g>
    <g class="tete">
      <path d="M64 76 Q62 40 100 38 Q138 40 136 76 Q138 84 134 90 Q136 60 100 56 Q64 60 66 90 Q62 84 64 76" fill="#17110c"/>
      ${visage({idPeau:"peauSy", oeil:"#2a1a10", sourcil:"#140d06", joue:".18", nez:"#7d4a28", bouche:"#7d3038", levre:"#5e2128"})}
      <!-- barbe courte -->
      <path d="M72 92 Q74 122 100 126 Q126 122 128 92 Q124 112 100 114 Q76 112 72 92" fill="#17110c" opacity=".92"/>
      <!-- lunettes fines -->
      <g fill="none" stroke="#c9a227" stroke-width="1.8">
        <rect x="79" y="76" width="18" height="13" rx="3"/><rect x="103" y="76" width="18" height="13" rx="3"/>
        <path d="M97 82 L103 82"/><path d="M79 80 L69 77"/><path d="M121 80 L131 77"/>
      </g>
    </g>
  </g>
</svg>`
};

/* ---- Gestes ---- */
function geste(cible, nomGeste, duree=2200){
  const el = typeof cible === "string" ? document.querySelector(cible) : cible;
  if(!el) return;
  ["geste-pointe","geste-joie","geste-inquiet","geste-salue"].forEach(c=>el.classList.remove(c));
  if(nomGeste && nomGeste !== "neutre"){
    void el.offsetWidth;
    el.classList.add("geste-"+nomGeste);
    if(duree > 0) setTimeout(()=>el.classList.remove("geste-"+nomGeste), duree);
  }
}

/** Le personnage actuellement à l'écran. */
function persoCourant(){
  return document.querySelector(".personnage-scene .portrait");
}

window.htmlPortrait     = htmlPersonnage;
window.htmlPersonnage   = htmlPersonnage;
window.svgPersonnage    = svgPersonnage;
window.activerPortrait  = activerPortraitBase; // media.js remplace ensuite
window.geste            = geste;
window.persoCourant     = persoCourant;
window.SVG_PERSOS       = SVG_PERSOS;
