/* ============================================================
   SOLVEURS — répondent aux énigmes dans jsdom (utilisés par test-jeu.js et test-immersif.js)
   ============================================================ */
const path = require("path");
const { dodo, clic } = require(path.join(process.env.OUTILS_TESTS || path.resolve(__dirname, "../../outils-tests"), "charge"));

/** Répond juste à l'énigme ouverte (ou faux si « faux » est vrai). */
async function repondre(w, e, grade, faux){
  const d = w.document, b = e[grade], type = b.type || e.type;
  const carte = d.getElementById("enigme-" + e.id);
  if(!carte) throw new Error("carte absente " + e.id);
  if(type === "tri"){
    const cartes = [...carte.querySelectorAll(".carte-tri")];
    cartes.forEach((c, i) => {
      clic(w, c);
      let col = c.dataset.col;
      if(faux && i === 0) col = (b.colonnes.find(x => x.id !== col) || {}).id;
      clic(w, carte.querySelector(`.tri-colonne[data-col="${col}"]`));
    });
  }else if(type === "association"){
    const g = [...carte.querySelectorAll('[data-col="g"] .carte-match')];
    g.forEach((c, i) => {
      clic(w, c);
      let cible = c.dataset.bon;
      if(faux && i < 2) cible = g[1 - i].dataset.bon;
      clic(w, carte.querySelector(`[data-col="d"] [data-id="${cible}"]`));
    });
  }else if(type === "ordre"){
    const liste = carte.querySelector(".liste-ordre");
    const items = [...liste.querySelectorAll(".item-ordre")].sort((a, c) => a.dataset.rang - c.dataset.rang);
    if(faux) [items[0], items[1]] = [items[1], items[0]];
    items.forEach(it => liste.appendChild(it));
  }else if(type === "trous"){
    const trous = [...carte.querySelectorAll(".trou")];
    trous.forEach((t, i) => {
      let mot = t.dataset.rep;
      if(faux && i === 0) mot = b.etiquettes.find(x => !String(b.texte).includes("[[" + x + "]]"));
      clic(w, carte.querySelector(`.etiquette[data-mot="${mot}"]:not(.posee)`));
      clic(w, t);
    });
  }else if(type === "qcm"){
    carte.querySelectorAll(".qcm-question").forEach((q, i) => {
      let j = b.questions[+q.dataset.i].bonne;
      if(faux && i === 0) j = (j + 1) % b.questions[+q.dataset.i].options.length;
      clic(w, q.querySelector(`.qcm-option[data-j="${j}"]`));
    });
  }else if(type === "code"){
    b.champs.forEach((c, i) => { const inp = carte.querySelector("#code-" + i); inp.value = (faux && i === 0) ? String(c.valeur) + "9" : String(c.valeur); });
  }else if(type === "vraifaux"){
    carte.querySelectorAll(".vf-ligne").forEach((l, i) => { const v = !!b.affirmations[+l.dataset.i].vrai; clic(w, l.querySelector(`[data-rep="${(faux && i === 0) ? !v ? "vrai" : "faux" : v ? "vrai" : "faux"}"]`)); });
  }else if(type === "intrus"){
    clic(w, carte.querySelector(`.carte-intrus[data-intrus="${faux ? 0 : 1}"]`));
  }else if(type === "plan"){
    [...carte.querySelectorAll(".plan-case")].forEach((cs, i) => {
      let mot = cs.dataset.rep;
      if(faux && i === 0) mot = [...carte.querySelectorAll(".etiquette")].map(x => x.dataset.mot).find(x => x !== mot);
      clic(w, carte.querySelector(`.etiquette[data-mot="${mot}"]:not(.posee)`)); clic(w, cs);
    });
  }else if(type === "lettres"){
    const cible = b.cible.map(String), pris = new Set();
    cible.forEach((l, i) => {
      const el = [...carte.querySelectorAll("[data-l]")].find(x => !pris.has(x) && (faux && i === 0 ? x.dataset.l !== l : x.dataset.l === l));
      pris.add(el); clic(w, el);
    });
  }else if(type === "instrument"){
    [...carte.querySelectorAll(".instr-item")].forEach((it, i) => {
      const v = b.items[+it.dataset.i].valeur;
      if(it.dataset.mode === "lire") it.querySelector(".instr-champ").value = String((faux && i === 0) ? v + 1 : v).replace(".", ",");
      else it.dataset.niveau = String((faux && i === 0) ? v + (b.pas || 1) : v);
    });
  }else if(type === "circuit"){
    const s = b.solution;
    const c = carte._circuit;
    if(s.retirer) c.fils.splice(0, c.fils.length, ...c.fils.filter(f => f.fixe));
    (faux ? s.fils.slice(0, s.fils.length - 1) : s.fils).forEach(([de, a]) => c.fils.push({ de, a }));
    Object.assign(c.fermes, s.fermes);
  }
  if(b.justification && (grade === "lieutenant" || grade === "second")){
    clic(w, carte.querySelector(`.justif-option[data-j="${b.justification.bonne}"]`));
  }
  clic(w, carte.querySelector("[data-valider]"));
  await dodo(30);
}

module.exports = { repondre };
