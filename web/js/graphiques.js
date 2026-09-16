/* Graphiques SVG dessinés à la main : aucune bibliothèque.
   Repère interne uniforme (viewBox W×H, mise à l'échelle proportionnelle) :
   le texte n'est jamais étiré, quel que soit le moteur de rendu (WebView2 inclus). */

const Graph = {
  _svg(inner, W, H) {
    return `<svg class="graph" viewBox="0 0 ${W} ${H}"
      preserveAspectRatio="xMidYMid meet"
      style="width:100%;height:auto;display:block;overflow:visible"
      font-family="var(--police)">${inner}</svg>`;
  },

  barres(donnees, { titre = "", couleurs = {}, unite = "" } = {}) {
    if (!donnees.length) return `<div class="vide">Aucune donnée</div>`;
    const W = 480, H = 260, mL = 30, mR = 10, mB = 40, mT = titre ? 34 : 14;
    const zw = W - mL - mR, zh = H - mB - mT;
    const vmax = Math.max(...donnees.map(d => d[1])) * 1.18 || 1;
    const pas = zw / donnees.length;

    const grille = [0, 1, 2, 3, 4].map(i => {
      const y = mT + zh - zh * i / 4;
      return `<line x1="${mL}" y1="${y}" x2="${W - mR}" y2="${y}"
                stroke="var(--bordure)" stroke-dasharray="3 3"/>
              <text x="${mL - 4}" y="${y + 3}" text-anchor="end"
                font-size="11" fill="var(--texte-doux)">${Math.round(vmax * i / 4)}</text>`;
    }).join("");

    const barres = donnees.map(([lib, v], i) => {
      const x = mL + pas * i + pas * 0.2, w = pas * 0.6, h = v / vmax * zh;
      const c = couleurs[lib] || "var(--accent)";
      const cx = x + w / 2;
      return `<rect x="${x}" y="${mT + zh - h}" width="${w}" height="${h}" fill="${c}" rx="3"/>
              <text x="${cx}" y="${mT + zh - h - 6}" text-anchor="middle"
                font-size="12" fill="var(--texte)">${v}${unite}</text>
              <text x="${cx}" y="${mT + zh + 16}" text-anchor="middle"
                font-size="11" fill="var(--texte-doux)">${echapper(
                  lib.length > 10 ? lib.slice(0, 9) + "." : lib)}</text>`;
    }).join("");

    return this._svg(
      (titre ? `<text x="${mL}" y="16" font-size="14" font-weight="600"
        fill="var(--texte)">${echapper(titre)}</text>` : "") + grille + barres, W, H);
  },

  courbe(points, { titre = "", repere = null, couleur = "var(--accent)", unite = "" } = {}) {
    if (!points.length) return `<div class="vide">Aucune donnée</div>`;
    const W = 480, H = 260, mL = 30, mR = 12, mB = 36, mT = titre ? 34 : 14;
    const zw = W - mL - mR, zh = H - mB - mT;
    const vals = points.map(p => p.valeur);
    const vmax = Math.max(...vals, repere || 0) * 1.2 || 1;
    const n = points.length;
    const px = i => n > 1 ? mL + zw * i / (n - 1) : mL + zw / 2;
    const py = v => mT + zh - v / vmax * zh;

    const grille = [0, 1, 2, 3, 4].map(i => {
      const y = mT + zh - zh * i / 4;
      return `<line x1="${mL}" y1="${y}" x2="${W - mR}" y2="${y}"
                stroke="var(--bordure)" stroke-dasharray="3 3"/>
              <text x="${mL - 4}" y="${y + 3}" text-anchor="end"
                font-size="11" fill="var(--texte-doux)">${Math.round(vmax * i / 4)}</text>`;
    }).join("");

    const rep = repere ? `
      <line x1="${mL}" y1="${py(repere)}" x2="${W - mR}" y2="${py(repere)}"
        stroke="var(--orange)" stroke-width="2" stroke-dasharray="6 3"/>
      <text x="${W - mR}" y="${py(repere) - 5}" text-anchor="end" font-size="11"
        fill="var(--orange)">repère ${repere}${unite}</text>` : "";

    const chemin = points.map((p, i) =>
      `${i ? "L" : "M"} ${px(i)} ${py(p.valeur)}`).join(" ");
    const pts = points.map((p, i) =>
      `<circle cx="${px(i)}" cy="${py(p.valeur)}" r="4" fill="${couleur}"
         stroke="var(--carte)" stroke-width="2"/>
       <text x="${px(i)}" y="${py(p.valeur) - 10}" text-anchor="middle"
         font-size="11" fill="var(--texte)">${Math.round(p.valeur)}</text>`).join("");

    const saut = Math.max(1, Math.ceil(n / 7));
    const libs = points.map((p, i) => i % saut ? "" :
      `<text x="${px(i)}" y="${mT + zh + 16}" text-anchor="middle"
        font-size="10" fill="var(--texte-doux)">${echapper(p.date)}</text>`).join("");

    return this._svg(
      (titre ? `<text x="${mL}" y="16" font-size="14" font-weight="600"
        fill="var(--texte)">${echapper(titre)}</text>` : "") +
      grille + rep +
      `<path d="${chemin}" fill="none" stroke="${couleur}" stroke-width="2"
        vector-effect="non-scaling-stroke"/>` + pts + libs, W, H);
  }
};
