/* Confort de lecture : polices dys, taille, interligne, syllabes, règle.
   Tout passe par des variables CSS — bien plus simple qu'en Tkinter. */

const Confort = {
  defauts: {
    police: "Verdana", taille: 16, interligne: 1.9, espacement: 0,
    fond: "#FFFFFF", syllabes: false, lignes: false, regle: false
  },

  polices: [
    ["OpenDyslexic", "OpenDyslexic (police dys)"],
    ["Luciole", "Luciole (police dys)"],
    ["Andika", "Andika (police dys)"],
    ["Verdana", "Verdana (lettres larges)"],
    ["Century Gothic", "Century Gothic (formes simples)"],
    ["Comic Sans MS", "Comic Sans (formes rondes)"],
    ["Arial", "Arial"],
    ["Georgia", "Georgia (livre)"]
  ],

  fonds: {
    "Blanc": "#FFFFFF", "Crème": "#FDF6E3", "Bleuté": "#E8F1F8",
    "Verdâtre": "#EAF4EA", "Rosé": "#FBEEF0", "Gris doux": "#F0F0F0"
  },

  interlignes: { "Serré": 1.4, "Normal": 1.9, "Aéré": 2.4, "Très aéré": 3.0 },

  charger() {
    try { return { ...this.defauts, ...JSON.parse(localStorage.confort || "{}") }; }
    catch { return { ...this.defauts }; }
  },

  sauver(p) { localStorage.confort = JSON.stringify(p); },

  /* Applique les préférences en posant les variables CSS sur la racine. */
  appliquer() {
    const p = this.charger();
    const r = document.documentElement.style;
    r.setProperty("--lect-police", `"${p.police}"`);
    r.setProperty("--lect-taille", p.taille + "px");
    r.setProperty("--lect-interligne", p.interligne);
    r.setProperty("--lect-espacement", p.espacement + "px");
    r.setProperty("--lect-fond", p.fond);
    if (this.surChangement) this.surChangement();
  },

  /* La barre repliable, à poser au-dessus d'une zone de texte. */
  barre(avecSyllabes = true) {
    const p = this.charger();
    const opts = (liste, val, cle) => liste.map(([v, l]) =>
      `<option value="${v}" ${v === val ? "selected" : ""}>${l}</option>`).join("");

    return `
      <div class="barre-outils">
        <button class="mini" id="c-ouvrir">🔎 Confort de lecture ▾</button>
        <button class="mini" id="c-moins" title="Réduire la police">A−</button>
        <button class="mini" id="c-plus" title="Agrandir la police">A+</button>
        <span style="color:var(--texte-doux);font-size:12px" id="c-taille">
          ${p.taille} pt</span>
        <span class="compteur" id="compteur">0 mot · 0 phrase</span>
      </div>
      <div class="confort" id="c-panneau">
        <div class="rangee">
          <div><label class="champ">Police</label>
            <select id="c-police">${opts(this.polices, p.police)}</select></div>
          <div><label class="champ">Fond</label>
            <select id="c-fond">${Object.entries(this.fonds).map(([l, v]) =>
              `<option value="${v}" ${v === p.fond ? "selected" : ""}>${l}</option>`
            ).join("")}</select></div>
          <div><label class="champ">Interligne</label>
            <select id="c-inter">${Object.entries(this.interlignes).map(([l, v]) =>
              `<option value="${v}" ${v == p.interligne ? "selected" : ""}>${l}</option>`
            ).join("")}</select></div>
          <div><label class="champ">Espacement</label>
            <select id="c-esp">
              <option value="0" ${p.espacement == 0 ? "selected" : ""}>Normal</option>
              <option value="1" ${p.espacement == 1 ? "selected" : ""}>Aéré</option>
              <option value="2" ${p.espacement == 2 ? "selected" : ""}>Très aéré</option>
            </select></div>
        </div>
        <div class="rangee" style="margin-top:8px">
          ${avecSyllabes ? `<label class="inter"><input type="checkbox" id="c-syl"
            ${p.syllabes ? "checked" : ""}> Colorer les syllabes</label>` : ""}
          <label class="inter"><input type="checkbox" id="c-lig"
            ${p.lignes ? "checked" : ""}> Colorer une ligne sur deux</label>
          <label class="inter"><input type="checkbox" id="c-reg"
            ${p.regle ? "checked" : ""}> Règle de lecture</label>
        </div>
      </div>`;
  },

  /* Branche les interactions de la barre. */
  brancher(surChangement) {
    this.surChangement = surChangement;
    const maj = (cle, val) => {
      const p = this.charger(); p[cle] = val; this.sauver(p); this.appliquer();
    };
    $("#c-ouvrir").onclick = () => {
      const pan = $("#c-panneau");
      pan.classList.toggle("ouvert");
      $("#c-ouvrir").textContent =
        "🔎 Confort de lecture " + (pan.classList.contains("ouvert") ? "▴" : "▾");
    };
    const tailles = [12, 14, 16, 18, 20, 24, 28, 32, 38, 44];
    const bouger = d => {
      const p = this.charger();
      let i = tailles.reduce((b, t, k) =>
        Math.abs(t - p.taille) < Math.abs(tailles[b] - p.taille) ? k : b, 0);
      i = Math.max(0, Math.min(tailles.length - 1, i + d));
      maj("taille", tailles[i]);
      $("#c-taille").textContent = tailles[i] + " pt";
    };
    $("#c-plus").onclick  = () => bouger(1);
    $("#c-moins").onclick = () => bouger(-1);
    $("#c-police").onchange = e => maj("police", e.target.value);
    $("#c-fond").onchange   = e => maj("fond", e.target.value);
    $("#c-inter").onchange  = e => maj("interligne", parseFloat(e.target.value));
    $("#c-esp").onchange    = e => maj("espacement", parseInt(e.target.value));
    const syl = $("#c-syl"), lig = $("#c-lig"), reg = $("#c-reg");
    if (syl) syl.onchange = e => maj("syllabes", e.target.checked);
    if (lig) lig.onchange = e => maj("lignes", e.target.checked);
    if (reg) reg.onchange = e => maj("regle", e.target.checked);
    this.appliquer();
  },

  /* --- Syllabation (mêmes règles que la version Python) --- */
  VOYELLES: "aeiouyàâäéèêëîïôöùûüœ",
  INSECABLES: new Set(["bl","br","cl","cr","dr","fl","fr","gl","gr","pl","pr",
                       "tr","vr","ch","ph","th","gn","qu"]),

  syllaber(mot) {
    if (mot.length <= 3) return [mot];
    const m = mot.toLowerCase(), coupes = [];
    let i = 0;
    while (i < m.length - 1) {
      if (this.VOYELLES.includes(m[i])) {
        let j = i + 1, cons = "";
        while (j < m.length && !this.VOYELLES.includes(m[j])) { cons += m[j]; j++; }
        if (j >= m.length) break;
        if (cons.length === 0) { i++; continue; }
        let coupe;
        if (cons.length === 1) coupe = i + 1;
        else if (this.INSECABLES.has(cons.slice(0, 2))) coupe = i + 1;
        else coupe = i + 2;
        if (coupe > 0 && coupe < m.length) coupes.push(coupe);
        i = j;
      } else i++;
    }
    const out = []; let d = 0;
    for (const c of coupes) { if (c - d >= 1) { out.push(mot.slice(d, c)); d = c; } }
    out.push(mot.slice(d));
    return out.filter(Boolean);
  },

  /* Colore les syllabes d'un texte, en HTML. */
  colorerSyllabes(texte) {
    return texte.replace(/[A-Za-zÀ-ÖØ-öø-ÿ'-]+/g, mot => {
      let k = 0;
      return this.syllaber(mot)
        .map(s => `<span class="syl-${k++ % 2}">${echapper(s)}</span>`).join("");
    });
  }
};
