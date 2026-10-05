/* ============================================================
   DÉCORS DE SECOURS — dessinés en SVG (1600 × 900, 16:9)
   ------------------------------------------------------------
   Affichés quand aucune image n'est déposée (ni image de référence).
   Assumés comme un niveau inférieur aux décors peints, mais soignés :
   dégradés, lumière chaude des lampes contre bleu des hublots,
   laiton, acajou, cuivre vert-de-gris. Les objets cliquables sont
   placés aux mêmes endroits que dans les images de référence
   (zones de assets/data/decors-fx.json).
   ============================================================ */
var VML = window.VML || (window.VML = {});

(function(){
  const R = (n, f) => Array.from({ length: n }, (_, i) => f(i)).join("");
  const rivets = (x1, y1, x2, y2, n, r = 3) => R(n, i => {
    const t = n > 1 ? i / (n - 1) : 0;
    return `<circle cx="${(x1 + (x2 - x1) * t).toFixed(1)}" cy="${(y1 + (y2 - y1) * t).toFixed(1)}" r="${r}" fill="url(#rivet)"/>`;
  });
  const defs = `
    <defs>
      <linearGradient id="acajou" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#4a2414"/><stop offset=".55" stop-color="#2c140b"/><stop offset="1" stop-color="#190b06"/></linearGradient>
      <linearGradient id="acajouH" x1="0" x2="1"><stop offset="0" stop-color="#2a130a"/><stop offset=".5" stop-color="#5a2d17"/><stop offset="1" stop-color="#2a130a"/></linearGradient>
      <linearGradient id="laiton" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#6b4a12"/><stop offset=".35" stop-color="#e2b65a"/><stop offset=".6" stop-color="#a87a28"/><stop offset="1" stop-color="#5a3c0d"/></linearGradient>
      <linearGradient id="cuivre" x1="0" x2="1"><stop offset="0" stop-color="#5c2a10"/><stop offset=".45" stop-color="#d47f45"/><stop offset="1" stop-color="#6a3315"/></linearGradient>
      <linearGradient id="vertdegris" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#2a4038"/><stop offset=".6" stop-color="#1c2d28"/><stop offset="1" stop-color="#121c19"/></linearGradient>
      <linearGradient id="parquet" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#3a1f10"/><stop offset="1" stop-color="#140a05"/></linearGradient>
      <radialGradient id="ocean" cx=".5" cy=".4" r=".7"><stop offset="0" stop-color="#4fd6ff"/><stop offset=".5" stop-color="#0f7fb5"/><stop offset="1" stop-color="#032a45"/></radialGradient>
      <radialGradient id="lumiereAmbre" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffe2a0" stop-opacity=".9"/><stop offset=".35" stop-color="#ffb84d" stop-opacity=".35"/><stop offset="1" stop-color="#ff9a2e" stop-opacity="0"/></radialGradient>
      <radialGradient id="lumiereVerte" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#d8ffd0" stop-opacity=".9"/><stop offset=".4" stop-color="#8fe68a" stop-opacity=".3"/><stop offset="1" stop-color="#8fe68a" stop-opacity="0"/></radialGradient>
      <radialGradient id="lumiereBleue" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#a6ecff" stop-opacity=".8"/><stop offset=".4" stop-color="#3bb6ff" stop-opacity=".25"/><stop offset="1" stop-color="#3bb6ff" stop-opacity="0"/></radialGradient>
      <radialGradient id="rivet" cx=".35" cy=".35" r=".7"><stop offset="0" stop-color="#f5d48a"/><stop offset=".5" stop-color="#9c7024"/><stop offset="1" stop-color="#3d2a08"/></radialGradient>
      <radialGradient id="ombre" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".75"/></radialGradient>
      <linearGradient id="papier" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#f3e6c4"/><stop offset="1" stop-color="#c9b48a"/></linearGradient>
      <linearGradient id="cuirVert" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#3d6b4c"/><stop offset="1" stop-color="#16301f"/></linearGradient>
      <pattern id="lattes" width="60" height="30" patternUnits="userSpaceOnUse"><rect width="60" height="30" fill="#2b170c"/><path d="M0 15 L30 0 L60 15 L30 30Z" fill="#3a2111" stroke="#1a0d06" stroke-width="1.5"/></pattern>
      <pattern id="caillebotis" width="24" height="24" patternUnits="userSpaceOnUse"><rect width="24" height="24" fill="#1a1d1c"/><rect x="2" y="2" width="20" height="9" fill="#2f3533"/><rect x="2" y="13" width="20" height="9" fill="#262b29"/></pattern>
      <filter id="flou"><feGaussianBlur stdDeviation="6"/></filter>
      <filter id="flouFort"><feGaussianBlur stdDeviation="18"/></filter>
    </defs>`;

  const hublot = (cx, cy, r, extra = "") => `
    <g>
      <circle cx="${cx}" cy="${cy}" r="${r * 1.32}" fill="url(#laiton)" stroke="#2a1a05" stroke-width="4"/>
      <circle cx="${cx}" cy="${cy}" r="${r * 1.12}" fill="#3b2a0c"/>
      ${R(16, i => { const a = i / 16 * Math.PI * 2; return `<circle cx="${(cx + Math.cos(a) * r * 1.22).toFixed(1)}" cy="${(cy + Math.sin(a) * r * 1.22).toFixed(1)}" r="${(r * .045).toFixed(1)}" fill="url(#rivet)"/>`; })}
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="url(#ocean)"/>
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="url(#lumiereBleue)" opacity=".5"/>
      ${extra}
      <path d="M${cx - r * .7} ${cy - r * .55} A ${r} ${r} 0 0 1 ${cx + r * .2} ${cy - r * .95}" stroke="#fff" stroke-opacity=".25" stroke-width="${r * .08}" fill="none" stroke-linecap="round"/>
    </g>`;
  const livres = (x, y, w, h, n) => R(n, i => {
    const lw = w / n, c = ["#5b1f17", "#2d3f2a", "#6a4a1c", "#1f2a44", "#4a1f2e", "#7a5a2a"][i % 6];
    const hh = h * (0.78 + 0.22 * ((i * 37) % 10) / 10);
    return `<rect x="${(x + i * lw).toFixed(1)}" y="${(y + h - hh).toFixed(1)}" width="${(lw - 1.5).toFixed(1)}" height="${hh.toFixed(1)}" fill="${c}"/><rect x="${(x + i * lw).toFixed(1)}" y="${(y + h - hh * .8).toFixed(1)}" width="${(lw - 1.5).toFixed(1)}" height="3" fill="#c9a24a" opacity=".6"/>`;
  });
  const etageres = (x, y, w, h, rangs) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#1e0f07"/>` + R(rangs, i => {
    const yy = y + i * h / rangs;
    return livres(x + 6, yy + 6, w - 12, h / rangs - 14, Math.round(w / 14)) + `<rect x="${x}" y="${yy + h / rangs - 8}" width="${w}" height="8" fill="url(#acajouH)"/>`;
  });
  const applique = (x, y, s = 1) => `
    <g transform="translate(${x} ${y}) scale(${s})">
      <circle r="90" fill="url(#lumiereAmbre)"/>
      <path d="M-26 10 Q0 -40 26 10 Q0 0 -26 10Z" fill="#f4d79a" stroke="#a87a28" stroke-width="2"/>
      ${R(5, i => `<path d="M0 8 L${-22 + i * 11} -18" stroke="#c99a48" stroke-width="1.5"/>`)}
      <rect x="-4" y="10" width="8" height="26" fill="url(#laiton)"/>
    </g>`;
  const lampeVerte = (x, y, s = 1) => `
    <g transform="translate(${x} ${y}) scale(${s})">
      <circle cy="20" r="150" fill="url(#lumiereVerte)" opacity=".7"/>
      <path d="M-55 10 Q0 -60 55 10 Z" fill="#6fcf73" stroke="#2f6b33" stroke-width="3"/>
      <path d="M-55 10 Q0 -60 55 10" fill="none" stroke="#d9ffd0" stroke-opacity=".5" stroke-width="2"/>
      <ellipse cy="10" rx="55" ry="8" fill="#fff6c8" opacity=".85"/>
      <rect x="-5" y="12" width="10" height="90" fill="url(#laiton)"/>
      <ellipse cy="104" rx="34" ry="9" fill="url(#laiton)"/>
    </g>`;
  const cadran = (cx, cy, r, angle = -40) => `
    <g>
      <circle cx="${cx}" cy="${cy}" r="${r + 7}" fill="url(#laiton)" stroke="#2a1a05" stroke-width="2"/>
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="#efe4c8"/>
      ${R(11, i => { const a = (-210 + i * 24) * Math.PI / 180; return `<line x1="${(cx + Math.cos(a) * r * .78).toFixed(1)}" y1="${(cy + Math.sin(a) * r * .78).toFixed(1)}" x2="${(cx + Math.cos(a) * r * .92).toFixed(1)}" y2="${(cy + Math.sin(a) * r * .92).toFixed(1)}" stroke="#2a2a2a" stroke-width="2"/>`; })}
      <line class="aiguille" x1="${cx}" y1="${cy}" x2="${(cx + Math.cos(angle * Math.PI / 180) * r * .8).toFixed(1)}" y2="${(cy + Math.sin(angle * Math.PI / 180) * r * .8).toFixed(1)}" stroke="#8a1c12" stroke-width="3" stroke-linecap="round"/>
      <circle cx="${cx}" cy="${cy}" r="${r * .1}" fill="#2a1a05"/>
    </g>`;

  /* ---------------- GRAND SALON ---------------- */
  const salon = `
  <svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Le grand salon du Nautilus (décor dessiné)">
    ${defs}
    <rect width="1600" height="900" fill="#0d0604"/>
    <!-- plafond à caissons -->
    <path d="M0 0 H1600 L1080 120 H520 Z" fill="#2a160b"/>
    ${R(7, i => `<path d="M${i * 266} 0 L${520 + i * 93} 120" stroke="#5a3218" stroke-width="3"/>`)}
    <!-- murs latéraux, galeries de bibliothèque -->
    <path d="M0 0 L520 120 L520 520 L0 900Z" fill="url(#acajou)"/>
    <path d="M1600 0 L1080 120 L1080 520 L1600 900Z" fill="url(#acajou)"/>
    <g opacity=".9">
      <path d="M40 40 L360 110 L360 300 L40 280Z" fill="#1c0e06"/>
      ${R(4, i => `<path d="M${60 + i * 75} ${48 + i * 16} L${120 + i * 75} ${60 + i * 16} L${120 + i * 75} ${285 - i * 3} L${60 + i * 75} ${282 - i * 3}Z" fill="${["#5b1f17", "#2d3f2a", "#6a4a1c", "#1f2a44"][i]}" opacity=".85"/>`)}
      <path d="M1560 40 L1240 110 L1240 300 L1560 280Z" fill="#1c0e06"/>
      ${R(4, i => `<path d="M${1540 - i * 75} ${48 + i * 16} L${1480 - i * 75} ${60 + i * 16} L${1480 - i * 75} ${285 - i * 3} L${1540 - i * 75} ${282 - i * 3}Z" fill="${["#4a1f2e", "#2d3f2a", "#7a5a2a", "#1f2a44"][i]}" opacity=".85"/>`)}
      <path d="M0 300 L520 330" stroke="url(#laiton)" stroke-width="6"/><path d="M1600 300 L1080 330" stroke="url(#laiton)" stroke-width="6"/>
    </g>
    <!-- mur du fond : orgue entre deux hublots -->
    <rect x="520" y="120" width="560" height="400" fill="#24120a"/>
    <rect x="520" y="120" width="560" height="400" fill="url(#acajou)" opacity=".7"/>
    <g>
      <rect x="722" y="150" width="100" height="205" fill="#1a0c05"/>
      ${R(11, i => { const h = 120 + 70 * Math.sin(i / 10 * Math.PI); return `<rect x="${728 + i * 8.6}" y="${355 - h}" width="6.5" height="${h}" rx="3" fill="url(#laiton)"/>`; })}
      <rect x="716" y="330" width="112" height="26" fill="url(#acajouH)"/>
      <rect x="726" y="335" width="92" height="7" fill="#efe9da"/>
    </g>
    ${hublot(656, 316, 52)}
    ${hublot(872, 316, 52)}
    <!-- lustre -->
    <g transform="translate(760 0)">
      <circle cy="60" r="140" fill="url(#lumiereAmbre)" opacity=".55"/>
      <line x1="0" y1="0" x2="0" y2="30" stroke="#a87a28" stroke-width="3"/>
      ${R(9, i => `<path d="M${-60 + i * 15} 30 Q${-60 + i * 15} 70 ${-40 + i * 10} ${80 + (i % 3) * 8}" stroke="#ffe7b0" stroke-width="1.5" fill="none" opacity=".8"/><circle cx="${-40 + i * 10}" cy="${82 + (i % 3) * 8}" r="3" fill="#fff4d0"/>`)}
    </g>
    ${applique(360, 140, 1.1)}${applique(1240, 140, 1.1)}
    <!-- sol : parquet en point de Hongrie, tapis à médaillon -->
    <path d="M0 900 L520 520 H1080 L1600 900Z" fill="url(#lattes)"/>
    <path d="M0 900 L520 520 H1080 L1600 900Z" fill="url(#parquet)" opacity=".55"/>
    <path d="M430 900 L640 560 H960 L1170 900Z" fill="#3a1414" opacity=".85"/>
    <path d="M470 900 L655 575 H945 L1130 900Z" fill="none" stroke="#c9a24a" stroke-width="3" opacity=".5"/>
    <ellipse cx="800" cy="720" rx="190" ry="70" fill="none" stroke="#c9a24a" stroke-width="3" opacity=".45"/>
    <!-- divan du fond et épure du Nautilus -->
    <g>
      <rect x="640" y="410" width="290" height="60" rx="16" fill="url(#cuirVert)"/>
      <rect x="640" y="388" width="290" height="34" rx="12" fill="#2a5539"/>
      ${R(6, i => `<circle cx="${670 + i * 46}" cy="404" r="3" fill="#123020"/>`)}
      <g transform="translate(700 420) rotate(-4)">
        <rect width="170" height="56" fill="url(#papier)" stroke="#8a7350"/>
        <path d="M18 30 Q85 6 152 30 Q85 48 18 30Z" fill="none" stroke="#2a4f8a" stroke-width="2"/>
        <path d="M18 30 H152" stroke="#2a4f8a" stroke-width="1" stroke-dasharray="4 3"/>
        ${R(5, i => `<circle cx="${50 + i * 18}" cy="30" r="2.5" fill="#2a4f8a"/>`)}
        <rect x="120" y="14" width="12" height="8" fill="none" stroke="#2a4f8a" stroke-width="1.5"/>
      </g>
    </g>
    <!-- vitrines de coraux, premier plan -->
    ${[0, 1].map(s => {
      const tr = s ? "translate(1600 0) scale(-1 1)" : "";
      return `<g transform="${tr}">
        <path d="M20 360 L330 400 L330 650 L20 700Z" fill="#0f2a2c" opacity=".55"/>
        <path d="M20 360 L330 400 L330 650 L20 700Z" fill="none" stroke="url(#laiton)" stroke-width="7"/>
        <path d="M20 600 L330 590 L330 650 L20 700Z" fill="url(#acajou)"/>
        <path d="M60 590 C70 520 90 470 80 420 M80 520 C110 490 130 470 150 430 M75 550 C40 500 30 470 45 440" stroke="#f0d2b4" stroke-width="9" stroke-linecap="round" fill="none"/>
        <path d="M200 585 l14 -30 l14 30 l-30 -18 h32z" fill="#e9a87a"/>
        <ellipse cx="270" cy="580" rx="30" ry="14" fill="#f4e4cc"/><path d="M250 580 q20 -26 40 0" stroke="#c9a88a" fill="none" stroke-width="3"/>
        <path d="M20 360 L330 400" stroke="#fff" stroke-opacity=".12" stroke-width="20"/>
      </g>`;
    }).join("")}
    <rect width="1600" height="900" fill="url(#ombre)"/>
  </svg>`;

  /* ---------------- CARRÉ DES OFFICIERS ---------------- */
  const carre = `
  <svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Le carré des officiers (décor dessiné)">
    ${defs}
    <rect width="1600" height="900" fill="url(#vertdegris)"/>
    ${R(8, i => `<line x1="${i * 210}" y1="0" x2="${i * 210}" y2="560" stroke="#0e1714" stroke-width="4"/>` + rivets(i * 210 + 10, 20, i * 210 + 10, 540, 14, 3.2))}
    <line x1="0" y1="430" x2="1600" y2="430" stroke="#0e1714" stroke-width="4"/>
    <rect x="0" y="430" width="1600" height="140" fill="url(#acajou)" opacity=".8"/>
    <!-- tuyauteries de cuivre -->
    <path d="M330 0 V470 M362 0 V470" stroke="url(#cuivre)" stroke-width="20"/>
    <path d="M0 60 H1600" stroke="url(#cuivre)" stroke-width="14"/>
    ${R(5, i => `<rect x="${322}" y="${70 + i * 90}" width="48" height="10" fill="url(#laiton)"/>`)}
    <!-- tableau des cadrans -->
    <g>
      <rect x="110" y="130" width="196" height="180" rx="8" fill="url(#acajouH)" stroke="url(#laiton)" stroke-width="6"/>
      ${cadran(160, 185, 30, 150)}${cadran(250, 185, 30, 160)}${cadran(160, 265, 26, 155)}${cadran(250, 265, 26, 150)}
    </g>
    ${cadran(370, 220, 30, -60)}
    <!-- bibliothèque -->
    ${etageres(700, 90, 190, 210, 3)}
    <!-- hublot et horloge -->
    ${hublot(1064, 252, 88, `<circle cx="1040" cy="230" r="10" fill="#bfefff" opacity=".35"/>`)}
    <g>
      <rect x="1280" y="100" width="90" height="190" rx="10" fill="url(#acajouH)" stroke="url(#laiton)" stroke-width="4"/>
      ${cadran(1325, 160, 34, -80)}
      <line x1="1325" y1="215" x2="1325" y2="270" stroke="url(#laiton)" stroke-width="3"/><circle cx="1325" cy="272" r="9" fill="url(#laiton)"/>
    </g>
    <!-- coquillages sur la desserte -->
    <rect x="980" y="455" width="420" height="22" fill="url(#acajouH)"/>
    ${R(5, i => `<path d="M${1010 + i * 80} 455 q18 -34 36 0z" fill="#e8cfa8" stroke="#a8875a"/>`)}
    <!-- applique coquille et lampe -->
    ${applique(560, 250, 1)}
    <!-- grande table en perspective -->
    <path d="M220 590 L1460 560 L1600 900 L120 900Z" fill="#3b1c0d"/>
    <path d="M220 590 L1460 560 L1600 900 L120 900Z" fill="url(#acajouH)" opacity=".6"/>
    <path d="M220 590 L1460 560" stroke="#7a4a26" stroke-width="5"/>
    <!-- cartes roussies, compas, règles, objets à trier -->
    <g>
      <path d="M300 650 L700 620 L760 840 L250 870Z" fill="url(#papier)" opacity=".9"/>
      <path d="M300 650 L700 620 L760 840 L250 870Z" fill="#2a1406" opacity=".25"/>
      <path d="M560 700 q40 30 90 10 q30 60 -40 90 q-60 10 -60 -40z" fill="#1a0d06" opacity=".55"/>
      <path d="M330 760 L520 735 M360 800 L600 770" stroke="#7a6a50" stroke-width="2"/>
      <circle cx="390" cy="700" r="40" fill="none" stroke="url(#laiton)" stroke-width="7"/>
      <line x1="390" y1="700" x2="420" y2="680" stroke="#2a1a05" stroke-width="3"/>
      <rect x="460" y="800" width="230" height="14" transform="rotate(-6 460 800)" fill="#b9c3c8"/>
      <path d="M660 660 l10 -60 l10 60z" fill="#d9e4ea" opacity=".75"/><ellipse cx="670" cy="662" rx="16" ry="6" fill="#cfe0e8" opacity=".6"/>
      <rect x="560" y="660" width="26" height="34" rx="6" fill="#a0784a"/>
      <path d="M720 650 q30 -50 70 -70" stroke="#f2ecd8" stroke-width="5"/>
    </g>
    <!-- lampe à pétrole à abat-jour vert -->
    ${lampeVerte(592, 420, 1)}
    <!-- câble brûlé -->
    <path d="M340 470 C 380 520, 300 560, 360 600" stroke="#111" stroke-width="10" fill="none"/>
    <path d="M352 585 l14 18" stroke="url(#cuivre)" stroke-width="5"/>
    <!-- journal de bord brûlé -->
    <g transform="translate(900 720) rotate(4)">
      <rect width="360" height="130" fill="#3b2410"/>
      <rect x="8" y="8" width="168" height="114" fill="#2b2522"/><rect x="184" y="8" width="168" height="114" fill="#3a302a"/>
      <path d="M20 40 q40 -10 60 10 t60 -6" stroke="#5a5048" fill="none" stroke-width="3"/>
      <path d="M190 30 h140 M190 50 h120 M190 70 h90" stroke="#6a5c52" stroke-width="3"/>
      <path d="M8 8 q50 40 20 114" fill="#000" opacity=".35"/>
    </g>
    <rect width="1600" height="900" fill="url(#ombre)"/>
  </svg>`;

  /* ---------------- SALLE DES MACHINES ÉLECTRIQUE ---------------- */
  const machines = `
  <svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="La salle des machines électriques (décor dessiné)">
    ${defs}
    <rect width="1600" height="900" fill="#0b1416"/>
    <!-- voûte rivetée -->
    <path d="M0 0 H1600 V160 Q800 40 0 160Z" fill="#1d2e2b"/>
    ${R(9, i => `<path d="M${i * 200} 0 Q${i * 200 + 100} 60 ${i * 200 + 200} 0" stroke="#0d1715" stroke-width="5" fill="none"/>`)}
    <rect x="0" y="120" width="1600" height="560" fill="url(#vertdegris)"/>
    ${R(9, i => `<line x1="${i * 200}" y1="120" x2="${i * 200}" y2="680" stroke="#0d1715" stroke-width="5"/>` + rivets(i * 200 + 12, 140, i * 200 + 12, 660, 16, 3.4))}
    <!-- câbles gainés au plafond -->
    ${R(5, i => `<path d="M0 ${150 + i * 14} C 500 ${110 + i * 16}, 1100 ${210 - i * 6}, 1600 ${150 + i * 14}" stroke="${i % 2 ? "#1b1b1b" : "#2a2522"}" stroke-width="9" fill="none"/>`)}
    <!-- accumulateurs (piles au sodium) -->
    <g>
      <rect x="40" y="420" width="450" height="380" fill="#121c1b"/>
      ${R(3, r => R(4, c => `
        <g transform="translate(${60 + c * 106} ${440 + r * 120})">
          <rect width="92" height="104" rx="6" fill="#2a3b3a" stroke="url(#laiton)" stroke-width="4"/>
          <rect x="10" y="22" width="72" height="66" fill="#6fd7d0" opacity=".18"/>
          <rect x="10" y="${60 - (c + r) % 3 * 10}" width="72" height="${28 + (c + r) % 3 * 10}" fill="#7ce6c8" opacity=".35"/>
          <rect x="18" y="-12" width="12" height="16" fill="url(#cuivre)"/><rect x="62" y="-12" width="12" height="16" fill="#999"/>
        </g>`))}
    </g>
    <!-- grand tableau de laiton (bornes) -->
    <g>
      <rect x="540" y="190" width="520" height="470" rx="14" fill="url(#acajouH)" stroke="url(#laiton)" stroke-width="12"/>
      <rect x="570" y="220" width="460" height="410" rx="6" fill="#2a1a0e"/>
      ${R(4, r => R(5, c => `<circle cx="${620 + c * 90}" cy="${300 + r * 90}" r="13" fill="url(#laiton)" stroke="#2a1a05" stroke-width="3"/>`))}
      ${R(5, c => `<g transform="translate(${620 + c * 90} 250)"><circle r="20" fill="#3a3a30"/><circle r="12" fill="#5a5544"/><path d="M-6 8 q6 -16 12 0" stroke="#bba" fill="none"/></g>`)}
      <path d="M620 300 q40 60 -10 120" stroke="#1d1d1d" stroke-width="7" fill="none"/>
      <path d="M800 390 q80 30 70 110" stroke="#1d1d1d" stroke-width="7" fill="none"/>
      <path d="M960 570 q-40 40 -120 30" stroke="#1d1d1d" stroke-width="7" fill="none"/>
      ${rivets(552, 202, 1048, 202, 18, 4)}${rivets(552, 648, 1048, 648, 18, 4)}
    </g>
    <!-- cadrans de contrôle -->
    <g>
      <rect x="1120" y="110" width="370" height="260" rx="10" fill="url(#acajouH)" stroke="url(#laiton)" stroke-width="6"/>
      ${cadran(1205, 200, 52, 145)}${cadran(1340, 200, 52, 150)}${cadran(1430, 300, 36, 140)}
      <rect x="1150" y="290" width="220" height="50" fill="#1a120a"/>
    </g>
    <!-- bobines et dynamo -->
    <g>
      ${R(3, i => `<g transform="translate(${1150 + i * 140} 480)">
        <rect x="-50" y="0" width="100" height="250" rx="10" fill="#4a2a14"/>
        ${R(14, k => `<rect x="-46" y="${10 + k * 16}" width="92" height="12" rx="5" fill="url(#cuivre)"/>`)}
        <rect x="-60" y="-14" width="120" height="20" fill="url(#laiton)"/><rect x="-60" y="244" width="120" height="20" fill="url(#laiton)"/>
      </g>`)}
      <circle cx="1290" cy="470" r="160" fill="url(#lumiereBleue)" opacity=".35"/>
    </g>
    <!-- passerelle en caillebotis -->
    <path d="M0 900 L380 690 H1220 L1600 900Z" fill="url(#caillebotis)"/>
    <path d="M380 690 H1220" stroke="url(#laiton)" stroke-width="8"/>
    <path d="M330 700 L0 880 M1270 700 L1600 880" stroke="url(#cuivre)" stroke-width="10"/>
    <rect width="1600" height="900" fill="url(#ombre)"/>
  </svg>`;

  /* ---------------- CHAMBRE DU CAPITAINE ---------------- */
  const cabine = `
  <svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="La chambre du capitaine Nemo (décor dessiné)">
    ${defs}
    <rect width="1600" height="900" fill="url(#acajou)"/>
    ${R(8, i => `<rect x="${i * 200 + 20}" y="40" width="160" height="380" rx="6" fill="none" stroke="#5a2d17" stroke-width="5"/>`)}
    <!-- alcôve à rideaux verts -->
    <rect x="40" y="60" width="380" height="560" fill="#0a0503"/>
    <path d="M40 60 q60 250 30 560 L40 620Z M420 60 q-70 250 -40 560 L420 620Z" fill="#1e4a32"/>
    <path d="M90 360 h300 v90 h-300z" fill="#d9d2c0" opacity=".35"/>
    <!-- hublot (centre) -->
    ${hublot(880, 216, 150, `<g opacity=".7"><ellipse cx="830" cy="190" rx="22" ry="15" fill="#e8dcff" opacity=".45"/><path d="M815 195 q4 30 -4 50 M830 197 q4 34 0 54 M845 195 q-2 28 6 48" stroke="#e8dcff" stroke-opacity=".4" fill="none"/></g>`)}
    <!-- mur des instruments -->
    <g>
      <rect x="1095" y="40" width="260" height="370" rx="8" fill="#2a140a" stroke="url(#laiton)" stroke-width="4"/>
      <rect x="1220" y="56" width="120" height="150" fill="#16233d" stroke="url(#laiton)" stroke-width="5"/>
      ${R(18, i => `<circle cx="${1232 + (i * 53) % 106}" cy="${70 + (i * 37) % 124}" r="${1.5 + i % 3}" fill="#f4edc8"/>`)}
      ${cadran(1160, 130, 48, -30)}
      ${cadran(1160, 260, 40, 160)}
      ${cadran(1290, 290, 44, 120)}
      <g transform="translate(1160 360)"><circle r="30" fill="url(#laiton)"/><circle r="24" fill="#efe4c8"/><path d="M0 -20 L6 0 L0 20 L-6 0Z" fill="#8a1c12"/><path d="M0 0 L6 0 L0 20 L-6 0Z" fill="#334"/></g>
    </g>
    ${applique(1420, 90, 1)}
    <!-- fauteuil Chesterfield -->
    <g>
      <path d="M330 470 q-20 -60 40 -70 h170 q60 10 40 70 v190 h-250z" fill="url(#cuirVert)"/>
      ${R(4, r => R(4, c => `<circle cx="${390 + c * 45}" cy="${430 + r * 30}" r="3.5" fill="#0e2416"/>`))}
      <rect x="310" y="560" width="60" height="140" rx="20" fill="#2a5539"/><rect x="560" y="560" width="60" height="140" rx="20" fill="#2a5539"/>
    </g>
    <!-- bureau d'acajou, plans, loupe, compas -->
    <g>
      <path d="M620 470 H1150 L1180 640 H600Z" fill="#4a2414"/>
      <path d="M620 470 H1150" stroke="#8a5a32" stroke-width="5"/>
      <rect x="640" y="640" width="520" height="260" fill="url(#acajou)"/>
      <path d="M700 500 L900 485 L920 590 L690 600Z" fill="url(#papier)"/>
      <path d="M720 520 q80 -20 170 0 M720 545 h150 M720 565 q60 10 140 -5" stroke="#5a7a9a" stroke-width="2" fill="none"/>
      <rect x="930" y="530" width="140" height="30" rx="15" fill="url(#papier)" transform="rotate(8 930 530)"/>
      <circle cx="990" cy="505" r="22" fill="none" stroke="url(#laiton)" stroke-width="6"/><circle cx="990" cy="505" r="17" fill="#bfefff" opacity=".35"/><line x1="1006" y1="520" x2="1040" y2="550" stroke="#3a2010" stroke-width="7"/>
      <path d="M760 600 l30 -70 l30 70" stroke="#c9c9c9" stroke-width="4" fill="none"/>
    </g>
    ${lampeVerte(912, 360, 0.9)}
    <!-- clavier d'orgue -->
    <g>
      <path d="M1250 620 H1600 V900 H1200Z" fill="#2a140a"/>
      <path d="M1250 650 H1600 V760 H1230Z" fill="#efe9da"/>
      ${R(16, i => `<line x1="${1250 + i * 22}" y1="650" x2="${1240 + i * 23}" y2="760" stroke="#999" stroke-width="1.5"/>${i % 7 !== 2 && i % 7 !== 6 ? `<rect x="${1262 + i * 22}" y="650" width="12" height="62" fill="#111"/>` : ""}`)}
    </g>
    <!-- tapis persan -->
    <path d="M200 900 L420 720 H1100 L1250 900Z" fill="#4a1414"/>
    <path d="M240 900 L440 735 H1080 L1210 900Z" fill="none" stroke="#c9a24a" stroke-width="4" opacity=".6"/>
    <rect width="1600" height="900" fill="url(#ombre)"/>
  </svg>`;

  VML.SVG_DECORS = { salon, carre, machines, cabine };
})();
