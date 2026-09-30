// Générateur de cartes SVG pour les leçons imprimables.
// Données : Natural Earth (domaine public) via world-atlas + fleuves 10m.
// Usage : node carte.mjs spec.json > carte.svg
import fs from "fs";
import * as d3 from "d3-geo";
import * as d3p from "d3-geo-projection";
import * as topojson from "topojson-client";
const range = (a, b, p) => { const r = []; for(let v = a; v < b; v += p) r.push(v); return r; };

const spec = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const DIR = (process.env.GEO_DIR || new URL("./geo-donnees/", import.meta.url).pathname).replace(/\/?$/, "/");
const resol = spec.resolution || "50m";
const world = JSON.parse(fs.readFileSync(new URL(`./node_modules/world-atlas/countries-${resol}.json`, import.meta.url)));
const pays = topojson.feature(world, world.objects.countries).features;
const terres = topojson.feature(world, world.objects.land);
const frontieres = topojson.mesh(world, world.objects.countries, (a, b) => a !== b);

const W = spec.largeur || 400;
const [[w0, s0], [e0, n0]] = spec.etendue || [[-180, -60], [180, 85]];
const cadre = { type: "Feature", geometry: { type: "Polygon", coordinates: [[[w0, s0], [e0, s0], [e0, n0], [w0, n0], [w0, s0]].reverse()] } };
// densifier le cadre pour qu'il suive les projections courbes
function cadreDense(){
  const pts = []; const N = 40;
  for(let i=0;i<=N;i++) pts.push([w0 + (e0-w0)*i/N, s0]);
  for(let i=0;i<=N;i++) pts.push([e0, s0 + (n0-s0)*i/N]);
  for(let i=0;i<=N;i++) pts.push([e0 - (e0-w0)*i/N, n0]);
  for(let i=0;i<=N;i++) pts.push([w0, n0 - (n0-s0)*i/N]);
  return { type:"Feature", geometry:{ type:"MultiPoint", coordinates: pts } };
}

let proj;
switch(spec.projection){
  case "mercator": proj = d3.geoMercator(); break;
  case "equalEarth": proj = d3.geoEqualEarth(); break;
  case "naturalEarth": proj = d3.geoNaturalEarth1(); break;
  case "robinson": proj = d3p.geoRobinson(); break;
  case "equirect": proj = d3.geoEquirectangular(); break;
  default: { // conique conforme centrée sur l'étendue (Lambert, comme l'IGN)
    const lat1 = s0 + (n0 - s0) / 4, lat2 = n0 - (n0 - s0) / 4;
    proj = d3.geoConicConformal().parallels([lat1, lat2]).rotate([-(w0 + e0) / 2, 0]);
  }
}
if(spec.rotation) proj.rotate(spec.rotation);
proj.fitWidth(W, cadreDense());
const b = d3.geoPath(proj).bounds(cadreDense());
const H = Math.round(spec.hauteur || (b[1][1] - b[0][1]));
proj.fitExtent([[0, 0], [W, H]], cadreDense());
proj.clipExtent([[0, 0], [W, H]]);

// contexte qui arrondit et élimine les points trop proches (allège le SVG)
function cheminAllege(geo, seuil = 0.6){
  let out = "", lx = null, ly = null, premier = true;
  const ctx = {
    moveTo(x, y){ out += `M${x.toFixed(1)},${y.toFixed(1)}`; lx = x; ly = y; premier = false; },
    lineTo(x, y){ if(Math.hypot(x - lx, y - ly) < seuil) return; out += `L${x.toFixed(1)},${y.toFixed(1)}`; lx = x; ly = y; },
    closePath(){ out += "Z"; },
    arc(){}
  };
  d3.geoPath(proj, ctx)(geo);
  return out;
}

const C = Object.assign({
  mer: "#dcebf5", terre: "#f3efe6", terreSurlignee: "#fbe9c8", trait: "#9aa4ad",
  frontiere: "#b9b2a4", fleuve: "#4f8fc4", texte: "#1f2328", mers: "#4b7fa8"
}, spec.couleurs || {});
const fs0 = spec.taille_texte || (spec.cible_mm ? 2.6 * W / spec.cible_mm : Math.max(9, Math.round(W / 38)));

let svg = [];
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
svg.push(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(spec.titre || "Carte")}" font-family="Segoe UI, Helvetica, Arial, sans-serif">`);
svg.push(`<rect width="${W}" height="${H}" fill="${C.mer}"/>`);

if(spec.graticule){
  const g = d3.geoGraticule().step(spec.graticule);
  svg.push(`<path d="${cheminAllege(g())}" fill="none" stroke="#b8cfe0" stroke-width="0.5"/>`);
}

// terres + pays
const surlignes = new Set(spec.pays_mis_en_avant || []);
svg.push(`<path d="${cheminAllege(terres)}" fill="${C.terre}" stroke="none"/>`);
for(const p of pays){
  if(surlignes.has(p.properties.name)){
    svg.push(`<path d="${cheminAllege(p)}" fill="${C.terreSurlignee}" stroke="none"/>`);
  }
}
if(spec.frontieres !== false){
  svg.push(`<path d="${cheminAllege(frontieres)}" fill="none" stroke="${C.frontiere}" stroke-width="0.6" stroke-dasharray="${spec.frontieres_pointillees ? "2 1.5" : "none"}"/>`);
}
svg.push(`<path d="${cheminAllege(terres)}" fill="none" stroke="${C.trait}" stroke-width="0.7"/>`);

// couches GeoJSON (régions, départements, massifs, pays colorés…)
for(const c of spec.couches || []){
  const gj = JSON.parse(fs.readFileSync(DIR + c.fichier));
  let feats = gj.features;
  if(c.filtre){
    const vals = new Set(c.filtre.valeurs.map(String));
    feats = feats.filter(f => vals.has(String(f.properties[c.filtre.prop])));
  }
  if(c.filtre_fn_prop){ // ex. {"prop":"featurecla","valeurs":["Range/mtn"]}
    const v2 = new Set(c.filtre_fn_prop.valeurs); feats = feats.filter(f => v2.has(f.properties[c.filtre_fn_prop.prop]));
  }
  for(const f of feats){
    let fill = c.remplissage || "none";
    if(c.couleurs_par){ const v = f.properties[c.couleurs_par.prop]; fill = c.couleurs_par.table[v] || c.couleurs_par.defaut || fill; }
    if(c.couleurs_individuelles){ const v = f.properties[c.couleurs_individuelles.prop]; fill = c.couleurs_individuelles.table[v] || fill; }
    svg.push(`<path d="${cheminAllege(f, c.seuil || 0.5)}" fill="${fill}" fill-opacity="${c.opacite ?? 1}" stroke="${c.contour || "none"}" stroke-width="${c.epaisseur || 0.6}" stroke-linejoin="round"/>`);
  }
  if(c.libelles){
    for(const f of feats){
      const nom = f.properties[c.libelles.prop]; if(!nom) continue;
      const pos = (c.libelles.positions || {})[nom];
      if(pos === null) continue;
      const p = proj(pos || d3.geoCentroid(f)); if(!p) continue;
      const txt = (c.libelles.renommer || {})[nom] || nom;
      const size = fs0 * (c.libelles.taille || 0.72);
      String(txt).split("\n").forEach((ln, k) => svg.push(`<text x="${p[0].toFixed(1)}" y="${(p[1] + size * 0.35 + k * size * 1.1).toFixed(1)}" font-size="${size.toFixed(1)}" text-anchor="middle" fill="${c.libelles.couleur || C.texte}" font-weight="${c.libelles.poids || 600}" ${c.libelles.italique ? 'font-style="italic"' : ""} paint-order="stroke" stroke="#fff" stroke-width="${c.libelles.halo ?? 2.2}" stroke-linejoin="round">${esc(ln)}</text>`));
    }
  }
}

// zones historiques ou thématiques (polygones en lon/lat)
for(const z of spec.zones || []){
  const ring = z.coords.slice(); if(ring[0][0] !== ring[ring.length - 1][0] || ring[0][1] !== ring[ring.length - 1][1]) ring.push(ring[0]);
  let geo = { type: "Polygon", coordinates: [ring] };
  if(d3.geoArea(geo) > 2 * Math.PI) geo = { type: "Polygon", coordinates: [ring.slice().reverse()] };
  const intersect = z.limiter_aux_terres !== false;
  const d = cheminAllege(geo, 0.3);
  if(intersect){
    const id = "clip" + Math.random().toString(36).slice(2, 8);
    svg.push(`<clipPath id="${id}"><path d="${cheminAllege(terres)}"/></clipPath>`);
    svg.push(`<path d="${d}" fill="${z.couleur || "#c0392b"}" fill-opacity="${z.opacite ?? 0.35}" clip-path="url(#${id})"/>`);
  }else{
    svg.push(`<path d="${d}" fill="${z.couleur || "#c0392b"}" fill-opacity="${z.opacite ?? 0.35}"/>`);
  }
  if(z.contour !== false) svg.push(`<path d="${d}" fill="none" stroke="${z.couleur_contour || z.couleur || "#c0392b"}" stroke-width="${z.epaisseur || 1.1}" stroke-dasharray="${z.pointille ? "4 2.5" : "none"}" ${intersect ? `clip-path="url(#${svg.at(-2).match(/id="([^"]+)"/)[1]})"` : ""}/>`);
}

// fleuves
if(spec.fleuves && spec.fleuves.length){
  const riv = JSON.parse(fs.readFileSync(DIR + "ne_10m_rivers_lake_centerlines.geojson"));
  const noms = new Set(spec.fleuves.map(n => n.toLowerCase()));
  for(const f of riv.features){
    const n = (f.properties.name || "").toLowerCase();
    const nfr = (f.properties.name_fr || "").toLowerCase();
    if(noms.has(n) || noms.has(nfr)){
      svg.push(`<path d="${cheminAllege(f, 1.0)}" fill="none" stroke="${C.fleuve}" stroke-width="${spec.epaisseur_fleuve || 1.2}" stroke-linejoin="round" stroke-linecap="round"/>`);
    }
  }
}

// méridiens particuliers (fuseaux horaires)
for(const m of spec.meridiens || []){
  const line = { type: "LineString", coordinates: range(-85, 86, 2).map(la => [m.lon, la]) };
  svg.push(`<path d="${cheminAllege(line)}" fill="none" stroke="${m.couleur || "#7a8691"}" stroke-width="${m.epaisseur || 0.7}" stroke-dasharray="${m.pointille === false ? "none" : "3 2"}"/>`);
  if(m.libelle){
    const p = proj([m.lon, m.lat_libelle ?? (s0 + 2)]);
    if(p) svg.push(`<text x="${p[0].toFixed(1)}" y="${p[1].toFixed(1)}" font-size="${fs0 * 0.72}" text-anchor="middle" fill="${m.couleur || "#4b5560"}" font-weight="600">${esc(m.libelle)}</text>`);
  }
}

// bandes (climats)
for(const bd of spec.bandes || []){
  const ring = [];
  for(let lo = -180; lo <= 180; lo += 5) ring.push([lo, bd.lat[0]]);
  for(let lo = 180; lo >= -180; lo -= 5) ring.push([lo, bd.lat[1]]);
  ring.push(ring[0]);
  let geo = { type: "Polygon", coordinates: [ring] };
  if(d3.geoArea(geo) > 2 * Math.PI) geo = { type: "Polygon", coordinates: [ring.slice().reverse()] };
  const id = "bd" + Math.random().toString(36).slice(2, 8);
  svg.push(`<clipPath id="${id}"><path d="${cheminAllege(terres)}"/></clipPath>`);
  svg.push(`<path d="${cheminAllege(geo, 0.3)}" fill="${bd.couleur}" fill-opacity="${bd.opacite ?? 0.75}" clip-path="url(#${id})"/>`);
}
if((spec.bandes || []).length) svg.push(`<path d="${cheminAllege(terres)}" fill="none" stroke="${C.trait}" stroke-width="0.6"/>`);

// itinéraires
const defs = [];
for(const [i, l] of (spec.lignes || []).entries()){
  const coul = l.couleur || "#b3261e";
  const geo = { type: "LineString", coordinates: l.coords };
  if(l.fleches){
    defs.push(`<marker id="fl${i}" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="${l.taille_fleche || 5}" markerHeight="${l.taille_fleche || 5}" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="${coul}"/></marker>`);
  }
  // découpe en segments pour poser une flèche par étape
  if(l.fleches && l.coords.length > 1){
    for(let k = 0; k < l.coords.length - 1; k++){
      const seg = { type: "LineString", coordinates: [l.coords[k], l.coords[k + 1]] };
      svg.push(`<path d="${cheminAllege(seg, 0.4)}" fill="none" stroke="${coul}" stroke-width="${l.epaisseur || 1.6}" stroke-dasharray="${l.pointille ? "4 3" : "none"}" marker-end="url(#fl${i})" stroke-linecap="round"/>`);
    }
  }else{
    svg.push(`<path d="${cheminAllege(geo, 0.4)}" fill="none" stroke="${coul}" stroke-width="${l.epaisseur || 1.6}" stroke-dasharray="${l.pointille ? "4 3" : "none"}" stroke-linecap="round"/>`);
  }
}
if(defs.length) svg.splice(1, 0, `<defs>${defs.join("")}</defs>`);

// textes libres (mers, régions)
for(const t of spec.textes || []){
  const p = proj(t.lonlat); if(!p) continue;
  const st = t.style || "mer";
  const size = fs0 * (t.taille || (st === "mer" ? 0.8 : st === "region" ? 0.9 : 1));
  const fill = t.couleur || (st === "mer" ? C.mers : C.texte);
  const fw = st === "region" ? 700 : 400;
  const it = st === "mer" ? ' font-style="italic"' : "";
  const ls = st === "region" || st === "mer" ? ' letter-spacing="1"' : "";
  const lignes = String(t.texte).split("\n");
  lignes.forEach((ln, k) => svg.push(`<text x="${p[0].toFixed(1)}" y="${(p[1] + k * size * 1.1).toFixed(1)}" font-size="${size.toFixed(1)}" text-anchor="middle" fill="${fill}" font-weight="${fw}"${it}${ls}>${esc(ln)}</text>`));
}

// points
for(const pt of spec.points || []){
  const p = proj(pt.lonlat); if(!p) continue;
  const [x, y] = p;
  const coul = pt.couleur || "#1f2328";
  const r = pt.rayon || (pt.style === "capitale" ? 3.6 : 2.8);
  if(pt.style === "capitale") svg.push(`<rect x="${(x - r).toFixed(1)}" y="${(y - r).toFixed(1)}" width="${2 * r}" height="${2 * r}" fill="${coul}" stroke="#fff" stroke-width="0.8"/>`);
  else if(pt.style === "etoile"){
    const s = r * 1.7, pts = [];
    for(let k = 0; k < 10; k++){ const a = Math.PI / 5 * k - Math.PI / 2, rr = k % 2 ? s * 0.45 : s; pts.push(`${(x + rr * Math.cos(a)).toFixed(1)},${(y + rr * Math.sin(a)).toFixed(1)}`); }
    svg.push(`<polygon points="${pts.join(" ")}" fill="${coul}" stroke="#fff" stroke-width="0.6"/>`);
  }
  else if(pt.style === "numero"){
    svg.push(`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${r * 2.4}" fill="${coul}" stroke="#fff" stroke-width="1"/><text x="${x.toFixed(1)}" y="${(y + fs0 * 0.3).toFixed(1)}" font-size="${fs0 * 0.8}" font-weight="700" text-anchor="middle" fill="#fff">${esc(pt.numero)}</text>`);
  }
  else if(pt.style === "symbole"){
    svg.push(`<g transform="translate(${x.toFixed(1)},${y.toFixed(1)})">${pt.symbole}</g>`);
  }
  else svg.push(`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${r}" fill="${coul}" stroke="#fff" stroke-width="0.8"/>`);
  if(pt.nom){
    const pos = pt.pos || "e"; const d = r + 3 + (pt.style === "numero" ? r * 1.6 : 0);
    let tx = x, ty = y + fs0 * 0.33, an = "start";
    if(pos.includes("e")){ tx = x + d; an = "start"; }
    if(pos.includes("w")){ tx = x - d; an = "end"; }
    if(pos === "n" || pos === "s") an = "middle";
    if(pos.includes("n")) ty = y - d - (pos === "n" ? 0 : -fs0 * 0.1) ;
    if(pos.includes("s")) ty = y + d + fs0 * 0.75;
    const size = fs0 * (pt.taille || 0.92);
    const lignes = String(pt.nom).split("\n");
    lignes.forEach((ln, k) => svg.push(`<text x="${tx.toFixed(1)}" y="${(ty + k * size * 1.1).toFixed(1)}" font-size="${size.toFixed(1)}" text-anchor="${an}" fill="${pt.couleur_texte || C.texte}" font-weight="${pt.gras === false ? 400 : 600}" paint-order="stroke" stroke="#ffffff" stroke-width="2.4" stroke-linejoin="round">${esc(ln)}</text>`));
  }
}

// échelle
if(spec.echelle_km){
  const km = spec.echelle_km;
  const x0 = 10, y0 = H - 12;
  const c = proj.invert([W / 2, H / 2]);
  const R = 6371;
  // pixels pour km au centre
  const p1 = proj(c), dLon = km / (R * Math.cos(c[1] * Math.PI / 180)) * 180 / Math.PI;
  const p2 = proj([c[0] + dLon, c[1]]);
  const px = Math.abs(p2[0] - p1[0]);
  svg.push(`<g font-size="${fs0 * 0.72}" fill="${C.texte}"><rect x="${x0 - 4}" y="${y0 - fs0 - 2}" width="${px + 8 + 30}" height="${fs0 + 8}" fill="#fff" fill-opacity=".75" rx="2"/><rect x="${x0}" y="${y0 - 3}" width="${px / 2}" height="4" fill="#333"/><rect x="${x0 + px / 2}" y="${y0 - 3}" width="${px / 2}" height="4" fill="#fff" stroke="#333" stroke-width=".6"/><text x="${x0}" y="${y0 - 6}">0</text><text x="${x0 + px}" y="${y0 - 6}" text-anchor="middle">${km} km</text></g>`);
}
// flèche du nord
if(spec.nord !== false){
  const x = W - 16, y = 20;
  svg.push(`<g><path d="M${x},${y - 12} l6,16 l-6,-4 l-6,4 z" fill="#333"/><text x="${x}" y="${y + 16}" font-size="${fs0 * 0.8}" text-anchor="middle" font-weight="700" fill="#333">N</text></g>`);
}
// légende
if(spec.legende && spec.legende.length){
  const lh = fs0 * 1.25, pad = 5;
  const wL = Math.max(...spec.legende.map(l => l.texte.length)) * fs0 * 0.5 + 26;
  const hL = spec.legende.length * lh + pad * 2;
  const pos = spec.position_legende || "bas-droite";
  const lx = pos.includes("gauche") ? 6 : W - wL - 6;
  const ly = pos.includes("haut") ? 6 : H - hL - 6;
  svg.push(`<g font-size="${fs0 * 0.78}" fill="${C.texte}"><rect x="${lx}" y="${ly}" width="${wL}" height="${hL}" fill="#fff" fill-opacity=".9" stroke="#c9ced4" stroke-width=".6" rx="3"/>`);
  spec.legende.forEach((l, k) => {
    const yy = ly + pad + k * lh + lh / 2;
    if(l.type === "ligne") svg.push(`<line x1="${lx + 6}" y1="${yy}" x2="${lx + 20}" y2="${yy}" stroke="${l.couleur}" stroke-width="2" stroke-dasharray="${l.pointille ? "3 2" : "none"}"/>`);
    else if(l.type === "point") svg.push(`<circle cx="${lx + 13}" cy="${yy}" r="3" fill="${l.couleur}"/>`);
    else if(l.type === "etoile") svg.push(`<text x="${lx + 13}" y="${yy + 4}" text-anchor="middle" fill="${l.couleur}" font-size="${fs0}">★</text>`);
    else svg.push(`<rect x="${lx + 6}" y="${yy - 5}" width="14" height="10" fill="${l.couleur}" fill-opacity="${l.opacite ?? 0.6}" stroke="${l.couleur}" stroke-width=".6"/>`);
    svg.push(`<text x="${lx + 25}" y="${yy + fs0 * 0.28}">${esc(l.texte)}</text>`);
  });
  svg.push(`</g>`);
}
svg.push(`</svg>`);
process.stdout.write(svg.join(""));
