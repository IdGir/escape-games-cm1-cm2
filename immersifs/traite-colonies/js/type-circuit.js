/* ============================================================
   TYPE « CIRCUIT » — relier les bornes d'un tableau électrique
   ------------------------------------------------------------
   Nouveau type (12ᵉ), propre à ce jeu, branché sur le moteur commun
   SANS le modifier : on ajoute une entrée aux tables CORPS et
   ACTIVATEURS de commun/js/enigmes.js (objets globaux).
   Pourquoi un nouveau type : l'énigme se joue sur l'objet lui-même
   (les bornes du tableau de laiton), et la réussite est vérifiée
   par une vraie simulation du courant, pas par une réponse attendue
   recopiable (plusieurs montages justes sont acceptés).

   JSON : { composants:[{id, type:"pile"|"lampe"|"moteur"|"interrupteur",
             libelle, x, y (en %), ferme}],
            fils:[{de, a, fixe, libelle}],         bornes : P+ P- / <id>a <id>b
            attendu:{ allumes:[ids], fermes:[ids], independants:[ids], serie:[ids],
                      commande:{K:[ids]} } }
   Correction : on compte les vérifications remplies (appareils qui
   fonctionnent, interrupteurs fermés, indépendance, commande, absence
   de court-circuit) et on dit seulement COMBIEN, jamais lesquelles ;
   rien ne s'allume tant que tout n'est pas juste.
   ============================================================ */
var VML = window.VML || (window.VML = {});

(function(){
  const LARG = 600, HAUT = 360;
  const bornesDe = c => c.type === "pile" ? [c.id + "+", c.id + "-"] : [c.id + "a", c.id + "b"];
  const posBorne = (c, k) => {
    const cx = c.x / 100 * LARG, cy = c.y / 100 * HAUT;
    if(c.type === "pile") return k === 0 ? { x: cx, y: cy - 62 } : { x: cx, y: cy + 62 };
    return k === 0 ? { x: cx - 48, y: cy } : { x: cx + 48, y: cy };
  };

  /* ---------------- Simulation ----------------
     Fils et interrupteurs fermés fusionnent les bornes (union-find) ;
     lampes et moteurs sont des résistances égales ; la pile impose
     1 entre + et −. Résolution des tensions des nœuds (méthode des
     nœuds, élimination de Gauss). Un appareil fonctionne si la tension
     à ses bornes dépasse 0,15. */
  VML.simulerCircuit = function(composants, fils, fermes, retires){
    retires = retires || [];
    const parent = {};
    const find = x => { while(parent[x] !== x){ parent[x] = parent[parent[x]]; x = parent[x]; } return x; };
    const unir = (a, b) => { parent[find(a)] = find(b); };
    composants.forEach(c => bornesDe(c).forEach(b => parent[b] = b));
    fils.forEach(f => { if(parent[f.de] != null && parent[f.a] != null) unir(f.de, f.a); });
    composants.forEach(c => { if(c.type === "interrupteur" && fermes[c.id] && !retires.includes(c.id)) unir(c.id + "a", c.id + "b"); });
    const pile = composants.find(c => c.type === "pile");
    const res = { cc: false, tension: {} };
    if(!pile) return res;
    const Sp = find(pile.id + "+"), Sm = find(pile.id + "-");
    if(Sp === Sm){ res.cc = true; composants.forEach(c => res.tension[c.id] = 0); return res; }
    const recepteurs = composants.filter(c => (c.type === "lampe" || c.type === "moteur") && !retires.includes(c.id));
    const noeuds = [...new Set(Object.keys(parent).map(find))].filter(n => n !== Sp && n !== Sm);
    const idx = {}; noeuds.forEach((n, i) => idx[n] = i);
    const N = noeuds.length;
    const A = Array.from({ length: N }, () => new Array(N + 1).fill(0));
    noeuds.forEach((n, i) => A[i][i] += 1e-6);
    const V = n => n === Sp ? 1 : n === Sm ? 0 : null;
    recepteurs.forEach(c => {
      const a = find(c.id + "a"), b = find(c.id + "b");
      if(a === b) return;
      [[a, b], [b, a]].forEach(([p, q]) => {
        if(V(p) !== null) return;
        const i = idx[p];
        A[i][i] += 1;
        if(V(q) !== null) A[i][N] += V(q); else A[i][idx[q]] -= 1;
      });
    });
    for(let k = 0; k < N; k++){
      let m = k; for(let r = k + 1; r < N; r++) if(Math.abs(A[r][k]) > Math.abs(A[m][k])) m = r;
      [A[k], A[m]] = [A[m], A[k]];
      const p = A[k][k] || 1e-12;
      for(let r = 0; r < N; r++){ if(r === k) continue; const f = A[r][k] / p; if(f) for(let c = k; c <= N; c++) A[r][c] -= f * A[k][c]; }
    }
    const val = n => V(n) !== null ? V(n) : A[idx[n]][N] / (A[idx[n]][idx[n]] || 1e-12);
    composants.forEach(c => {
      if(c.type !== "lampe" && c.type !== "moteur") return;
      if(retires.includes(c.id)){ res.tension[c.id] = 0; return; }
      res.tension[c.id] = Math.abs(val(find(c.id + "a")) - val(find(c.id + "b")));
    });
    return res;
  };
  const marche = (r, id) => (r.tension[id] || 0) > 0.15;

  /** Vérifications : [{ok}] — on n'en communique que le nombre. */
  VML.verifierCircuit = function(d, fils, fermes){
    const comps = d.composants || [], att = d.attendu || {};
    const liste = [];
    const r = VML.simulerCircuit(comps, fils, fermes);
    liste.push({ nom: "pas de court-circuit", ok: !r.cc });
    (att.fermes || []).forEach(id => liste.push({ nom: id + " fermé", ok: !!fermes[id] }));
    (att.allumes || []).forEach(id => liste.push({ nom: id + " fonctionne", ok: !r.cc && marche(r, id) }));
    (att.independants || []).forEach(id => {
      const r2 = VML.simulerCircuit(comps, fils, fermes, [id]);
      const autres = (att.independants || []).filter(x => x !== id);
      liste.push({ nom: id + " indépendant", ok: !r.cc && marche(r, id) && !r2.cc && autres.every(x => marche(r2, x)) });
    });
    (att.serie || []).forEach(id => {
      const r2 = VML.simulerCircuit(comps, fils, fermes, [id]);
      const autres = (att.serie || []).filter(x => x !== id);
      liste.push({ nom: id + " en série", ok: !r.cc && marche(r, id) && autres.every(x => !marche(r2, x)) });
    });
    Object.entries(att.commande || {}).forEach(([k, ids]) => {
      const f2 = Object.assign({}, fermes, { [k]: false });
      const r2 = VML.simulerCircuit(comps, fils, f2);
      const autres = (att.allumes || []).filter(x => !ids.includes(x));
      liste.push({ nom: k + " commande " + ids.join(","), ok: !!fermes[k] && !r.cc && ids.every(x => marche(r, x) && !marche(r2, x)) && autres.every(x => marche(r2, x)) });
    });
    return { liste, sim: r };
  };

  /* ---------------- Dessin ---------------- */
  function symbole(c, fermes){
    const cx = c.x / 100 * LARG, cy = c.y / 100 * HAUT;
    const lib = `<text x="${cx}" y="${c.type === "pile" ? cy + 92 : cy + 42}" text-anchor="middle" class="circ-lib">${c.libelle || c.id}</text>`;
    if(c.type === "pile") return `<g class="circ-comp" data-comp="${c.id}">
      <line x1="${cx}" y1="${cy - 62}" x2="${cx}" y2="${cy - 40}" class="circ-patte"/><line x1="${cx}" y1="${cy + 40}" x2="${cx}" y2="${cy + 62}" class="circ-patte"/>
      <rect x="${cx - 26}" y="${cy - 42}" width="52" height="84" rx="8" class="circ-pile"/>
      <rect x="${cx - 10}" y="${cy - 50}" width="20" height="9" class="circ-pile-tete"/>
      <text x="${cx + 34}" y="${cy - 50}" class="circ-signe">+</text><text x="${cx + 34}" y="${cy + 62}" class="circ-signe">−</text>
      <path d="M${cx - 12} ${cy + 4} l14 -22 l-4 16 l12 -2 l-14 22 l4 -16z" fill="#ffe08a"/>${lib}</g>`;
    if(c.type === "lampe") return `<g class="circ-comp circ-lampe" data-comp="${c.id}">
      <line x1="${cx - 48}" y1="${cy}" x2="${cx - 22}" y2="${cy}" class="circ-patte"/><line x1="${cx + 22}" y1="${cy}" x2="${cx + 48}" y2="${cy}" class="circ-patte"/>
      <circle cx="${cx}" cy="${cy}" r="40" class="circ-halo"/>
      <circle cx="${cx}" cy="${cy}" r="22" class="circ-ampoule"/>
      <path d="M${cx - 15} ${cy - 15} L${cx + 15} ${cy + 15} M${cx + 15} ${cy - 15} L${cx - 15} ${cy + 15}" class="circ-filament"/>${lib}</g>`;
    if(c.type === "moteur") return `<g class="circ-comp circ-moteur" data-comp="${c.id}">
      <line x1="${cx - 48}" y1="${cy}" x2="${cx - 24}" y2="${cy}" class="circ-patte"/><line x1="${cx + 24}" y1="${cy}" x2="${cx + 48}" y2="${cy}" class="circ-patte"/>
      <circle cx="${cx}" cy="${cy}" r="24" class="circ-moteur-corps"/>
      <g class="circ-helice" style="transform-origin:${cx}px ${cy}px"><path d="M${cx} ${cy} l0 -18 M${cx} ${cy} l16 9 M${cx} ${cy} l-16 9" stroke="#2a1a05" stroke-width="4" stroke-linecap="round"/></g>
      <text x="${cx}" y="${cy + 5}" text-anchor="middle" class="circ-m">M</text>${lib}</g>`;
    if(c.type === "interrupteur"){
      const f = !!fermes[c.id];
      return `<g class="circ-comp circ-inter ${f ? "ferme" : ""}" data-comp="${c.id}" data-inter="${c.id}" tabindex="0" role="switch" aria-checked="${f}" aria-label="${c.libelle || c.id} : ${f ? "fermé" : "ouvert"}">
        <rect x="${cx - 48}" y="${cy - 30}" width="96" height="52" fill="transparent"/>
        <line x1="${cx - 48}" y1="${cy}" x2="${cx - 24}" y2="${cy}" class="circ-patte"/><line x1="${cx + 24}" y1="${cy}" x2="${cx + 48}" y2="${cy}" class="circ-patte"/>
        <circle cx="${cx - 24}" cy="${cy}" r="5" fill="#2a1a05"/><circle cx="${cx + 24}" cy="${cy}" r="5" fill="#2a1a05"/>
        <line x1="${cx - 24}" y1="${cy}" x2="${f ? cx + 24 : cx + 16}" y2="${f ? cy : cy - 22}" class="circ-levier"/>${lib}</g>`;
    }
    return "";
  }

  function dessinerFils(svg, fils){
    const g = svg.querySelector(".circ-fils");
    const comps = svg._comps;
    const pos = id => {
      for(const c of comps){ const b = bornesDe(c); const k = b.indexOf(id); if(k >= 0) return posBorne(c, k); }
      return { x: 0, y: 0 };
    };
    g.innerHTML = fils.map((f, i) => {
      const a = pos(f.de), b = pos(f.a);
      const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2 + Math.min(60, Math.hypot(a.x - b.x, a.y - b.y) * 0.18);
      const d = `M${a.x} ${a.y} Q${mx} ${my} ${b.x} ${b.y}`;
      return `<g class="circ-fil ${f.fixe ? "fixe" : "mobile"}" data-fil="${i}" ${f.fixe ? "" : `tabindex="0" role="button" aria-label="Retirer le fil ${f.libelle || (f.de + " – " + f.a)}"`}>
        <path d="${d}" class="circ-fil-zone"/><path d="${d}" class="circ-fil-gaine"/><path d="${d}" class="circ-fil-ame"/></g>`;
    }).join("");
  }

  function corpsCircuit(d){
    const comps = d.composants || [];
    const fermes = {}; comps.forEach(c => { if(c.type === "interrupteur") fermes[c.id] = !!c.ferme; });
    const bornes = comps.map(c => bornesDe(c).map((b, k) => { const p = posBorne(c, k);
      return `<g class="circ-borne" data-borne="${b}" tabindex="0" role="button" aria-label="Borne ${b}"><circle cx="${p.x}" cy="${p.y}" r="24" class="circ-borne-zone"/><circle cx="${p.x}" cy="${p.y}" r="9" class="circ-borne-tete"/></g>`; }).join("")).join("");
    return `<div class="bloc-circuit">
      <p class="aide-type">Clique une borne, puis une autre, pour poser un fil. Clique un fil pour le retirer${comps.some(c => c.type === "interrupteur") ? ", et un interrupteur pour l'ouvrir ou le fermer" : ""}. Rien ne s'allume avant la mise sous tension.</p>
      <svg class="circ-svg" viewBox="0 0 ${LARG} ${HAUT}" role="group" aria-label="Tableau de bornes">
        <defs><radialGradient id="circHalo"><stop offset="0" stop-color="#fff3b0" stop-opacity=".95"/><stop offset="1" stop-color="#ffcc55" stop-opacity="0"/></radialGradient></defs>
        <rect x="4" y="4" width="${LARG - 8}" height="${HAUT - 8}" rx="16" class="circ-fond"/>
        ${comps.map(c => symbole(c, fermes)).join("")}
        <g class="circ-fils"></g>
        ${bornes}
      </svg>
      <div class="center"><button class="btn vert" data-valider="1">⚡ Mettre sous tension</button></div>
    </div>`;
  }

  function activerCircuit(e, d, api){
    const carte = document.getElementById("enigme-" + e.id);
    const svg = carte.querySelector(".circ-svg");
    const comps = d.composants || [];
    svg._comps = comps;
    const fils = (d.fils || []).map(f => Object.assign({}, f));
    const fermes = {}; comps.forEach(c => { if(c.type === "interrupteur") fermes[c.id] = !!c.ferme; });
    let sel = null;
    const eteindre = () => { svg.querySelectorAll(".allume,.tourne").forEach(x => x.classList.remove("allume", "tourne")); svg.classList.remove("sous-tension"); };
    const redessiner = () => { dessinerFils(svg, fils); eteindre(); };
    redessiner();
    const resolu = () => carte.classList.contains("resolue");

    const choisirBorne = b => {
      if(resolu()) return;
      const id = b.dataset.borne;
      if(!sel){ sel = id; b.classList.add("select"); return; }
      svg.querySelectorAll(".circ-borne.select").forEach(x => x.classList.remove("select"));
      if(sel !== id && !fils.some(f => (f.de === sel && f.a === id) || (f.de === id && f.a === sel))){
        fils.push({ de: sel, a: id }); if(VML.son) VML.son("fil");
      }
      sel = null; redessiner();
    };
    svg.addEventListener("click", ev => {
      if(resolu()) return;
      const b = ev.target.closest(".circ-borne"); if(b){ choisirBorne(b); return; }
      const fl = ev.target.closest(".circ-fil.mobile");
      if(fl){ fils.splice(+fl.dataset.fil, 1); if(VML.son) VML.son("clic"); redessiner(); return; }
      const k = ev.target.closest("[data-inter]");
      if(k){
        const id = k.dataset.inter; fermes[id] = !fermes[id];
        const c = comps.find(x => x.id === id);
        k.outerHTML = symbole(c, fermes);
        if(VML.son) VML.son("clic"); eteindre();
      }
    });
    svg.addEventListener("keydown", ev => {
      if(ev.key !== "Enter" && ev.key !== " ") return;
      const t = ev.target.closest(".circ-borne, .circ-fil.mobile, [data-inter]");
      if(t){ ev.preventDefault(); t.dispatchEvent(new MouseEvent("click", { bubbles: true })); }
    });
    carte.querySelector("[data-valider]").addEventListener("click", () => {
      if(resolu()) return;
      const { liste, sim } = VML.verifierCircuit(d, fils, fermes);
      const justes = liste.filter(x => x.ok).length;
      if(justes === liste.length){
        svg.classList.add("sous-tension");
        comps.forEach(c => {
          const g = svg.querySelector(`[data-comp="${c.id}"]`);
          if(!g) return;
          if(c.type === "lampe" && (sim.tension[c.id] || 0) > 0.15){ g.classList.add("allume"); g.style.setProperty("--eclat", Math.min(1, sim.tension[c.id] * 1.4).toFixed(2)); }
          if(c.type === "moteur" && (sim.tension[c.id] || 0) > 0.15) g.classList.add("tourne");
        });
        api.reussir();
      }else{
        if(sim.cc && VML.son) VML.son("courtcircuit");
        api.erreur(justes, liste.length, ["vérification réussie", "vérifications réussies"]);
      }
    });
    carte._circuit = { fils, fermes };     // pour les tests
  }

  if(typeof CORPS !== "undefined" && typeof ACTIVATEURS !== "undefined"){
    CORPS.circuit = corpsCircuit;
    ACTIVATEURS.circuit = activerCircuit;
  }
  VML.corpsCircuit = corpsCircuit;
  VML.activerCircuit = activerCircuit;
})();
