#!/usr/bin/env node
/* ============================================================
   CONTRÔLE DE LA CHARTE GRAPHIQUE (amélioration B1)
   Voir CHARTE-GRAPHIQUE.md. Sans dépendance :
     node outils-tests/verifier-charte.js [jeu …]
   ✗ = écart à corriger (code de sortie 1) · ⚠ = à regarder.
   ============================================================ */
const fs = require("fs"), path = require("path");
const RACINE = path.resolve(__dirname, "..");
const SOCLE = { "parchemin": "#f4e9d0", "parchemin-clair": "#fbf3dd", "parchemin-ombre": "#e0cfa6",
  "encre": "#2b1d10", "encre-doux": "#4a3825", "blanc": "#fbf6e9", "or": "#c9a227", "or-clair": "#e6c757" };
const EXCEPTIONS = { melanges: ["parchemin", "parchemin-clair", "parchemin-ombre", "encre", "encre-doux", "blanc"] };
const PEAUX = ["#f6dcc0", "#e9c49e", "#e2b183", "#c48f5e", "#a2663c", "#7d4a28", "#f8e6d2", "#ecd0b4",
  "#e8c39a", "#d3a273", "#d9a06a", "#b87c48"];   // + variantes historiques de declaration / tour-du-monde

function luminance(h){
  const c = [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255).map(v => v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4));
  return .2126 * c[0] + .7152 * c[1] + .0722 * c[2];
}
const contraste = (a, b) => { const [x, y] = [luminance(a), luminance(b)].sort((p, q) => q - p); return (x + .05) / (y + .05); };

function jeux(){
  return fs.readdirSync(RACINE).filter(j => ["css/style.css", "js/decors.js", "js/personnages.js"].every(f => fs.existsSync(path.join(RACINE, j, f)))).sort();
}

function controler(j){
  const err = [], warn = [];
  const css = fs.readFileSync(path.join(RACINE, j, "css/style.css"), "utf8");
  const root = (css.match(/:root\s*\{([\s\S]*?)\}/) || [])[1] || "";
  const v = {}; for (const m of root.matchAll(/--([a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{6})\b/g)) if (!v[m[1]]) v[m[1]] = m[2].toLowerCase();
  for (const [k, val] of Object.entries(SOCLE)) {
    if ((EXCEPTIONS[j] || []).includes(k)) continue;
    if (v[k] !== val) err.push(`--${k} vaut ${v[k] || "(absent)"} au lieu de ${val} (socle commun)`);
  }
  for (const k of ["bleu", "rouge"]) {
    if (!v[k]) { err.push(`--${k} absent (couleur d'accent du jeu)`); continue; }
    const c = contraste(v[k], v.blanc || SOCLE.blanc);
    if (c < 4.5) err.push(`--${k} ${v[k]} : contraste ${c.toFixed(1)}:1 avec le blanc des boutons (minimum 4,5)`);
  }
  if (v["rouge-vif"] && contraste(v["rouge-vif"], v.blanc || SOCLE.blanc) < 4.5) warn.push(`--rouge-vif ${v["rouge-vif"]} : contraste ${contraste(v["rouge-vif"], v.blanc || SOCLE.blanc).toFixed(1)}:1 (réservé aux grands textes)`);
  if (!/body\s*\{[^}]*font-family:\s*Georgia/.test(css)) warn.push("police du texte : Georgia attendue");
  const dec = fs.readFileSync(path.join(RACINE, j, "js/decors.js"), "utf8");
  const vbD = [...new Set([...dec.matchAll(/class="decor-svg"[^>]*viewBox="([^"]+)"|viewBox="([^"]+)"[^>]*class="decor-svg"/g)].map(m => m[1] || m[2]))];
  if (!vbD.length) warn.push("aucun décor dessiné (class=\"decor-svg\") trouvé");
  vbD.filter(x => x !== "0 0 800 300").forEach(x => err.push(`décor en viewBox « ${x} » (attendu 0 0 800 300)`));
  const larges = [...dec.matchAll(/stroke-width="([0-9.]+)"/g)].map(m => +m[1]).filter(x => x > 12);
  if (larges.length) warn.push(`${larges.length} trait(s) de plus de 12 (max relevé : ${Math.max(...larges)})`);
  const per = fs.readFileSync(path.join(RACINE, j, "js/personnages.js"), "utf8");
  [...new Set([...per.matchAll(/viewBox="([^"]+)"/g)].map(m => m[1]))].filter(x => x !== "0 0 200 320").forEach(x => err.push(`personnage en viewBox « ${x} » (attendu 0 0 200 320)`));
  const peau = (per.match(/const PEAU\s*=\s*\{([\s\S]*?)\};/) || [])[1];
  if (!peau) warn.push("objet PEAU absent de personnages.js");
  else [...peau.matchAll(/#[0-9a-fA-F]{6}/g)].map(m => m[0].toLowerCase()).filter(c => !PEAUX.includes(c)).forEach(c => err.push(`carnation ${c} hors de la palette PEAU`));
  ["tete", "bouche", "buste"].forEach(cl => { if (!new RegExp(`class=\\\\?["']${cl}\\b`).test(per) && !per.includes(`"${cl}"`) && !per.includes(`class="${cl}`)) warn.push(`classe .${cl} introuvable (squelette commun)`); });
  return { j, err, warn, accents: [v.bleu, v.rouge] };
}

function lancer(choix){
  const liste = choix.length ? choix : jeux();
  let nErr = 0; const couples = {};
  console.log("Contrôle de la charte graphique (B1)\n");
  for (const j of liste) {
    const r = controler(j);
    console.log(`${r.err.length ? "✗" : r.warn.length ? "⚠" : "✓"} ${j.padEnd(20)} accents ${r.accents.join(" / ")}`);
    r.err.forEach(m => console.log("    ✗ " + m)); r.warn.forEach(m => console.log("    ⚠ " + m));
    nErr += r.err.length;
    const k = r.accents.join("/"); (couples[k] = couples[k] || []).push(j);
  }
  Object.entries(couples).filter(([, l]) => l.length > 2).forEach(([k, l]) => console.log(`\nℹ même couple d'accents ${k} pour ${l.join(", ")} (palette par défaut)`));
  console.log(`\n${liste.length} jeu(x), ${nErr} écart(s) à corriger.`);
  return nErr;
}
module.exports = { controler, jeux, contraste, lancer };
if (require.main === module) process.exitCode = lancer(process.argv.slice(2)) ? 1 : 0;
