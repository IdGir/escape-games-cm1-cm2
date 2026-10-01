/* ============================================================
   FRISE DE L'ANNÉE (amélioration B3) — tronc commun
   ------------------------------------------------------------
   Dessine, à partir de commun/donnees/catalogue.js, la frise des 26
   jeux de la progression sur le calendrier scolaire : périodes P1 à
   P5 en colonnes, Année A et Année B en lignes ; jeux disponibles en
   couleur (lien pour jouer), jeux à venir en grisé. Mission
   géographique (toute l'année) et le Tour du monde (révision libre)
   ont leur propre ligne.
   Utilisée par l'accueil (index.html) et la vue de l'année (annee.html).
     FRISE.dessiner(element, { annee: "A" | "B" | "" , lien: true })
   ============================================================ */
(function(){
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;" }[c]));
  const P = ["P1", "P2", "P3", "P4", "P5"];
  const STYLE = `
    .frise{--case:#fff;--ligne:#e2ddd2;--doux:#5d6472;font-size:.88rem}
    .frise-grille{display:grid;grid-template-columns:7.5em repeat(5,1fr);gap:6px}
    .frise-tete{font-weight:700;text-align:center;padding:6px 4px;border-radius:10px;background:#efe9dc}
    .frise-tete small{display:block;font-weight:500;color:var(--doux)}
    .frise-ligne{font-weight:700;display:flex;align-items:center;padding:6px;border-radius:10px;background:#f4f1ea}
    .frise-case{display:flex;flex-direction:column;gap:5px;padding:6px;border-radius:10px;background:var(--case);border:1px solid var(--ligne);min-height:3.2em}
    .frise-jeu{display:flex;gap:6px;align-items:center;padding:5px 8px;border-radius:9px;text-decoration:none;color:#fff;line-height:1.2;font-weight:600;text-shadow:0 1px 2px rgba(0,0,0,.35)}
    .frise-jeu.avenir{text-shadow:none}
    .frise-jeu.avenir{background:repeating-linear-gradient(135deg,#f3f1ec,#f3f1ec 6px,#ebe7de 6px,#ebe7de 12px);color:#8a8f99;border:1px dashed #c9c3b5;font-weight:500}
    .frise-jeu .ic{font-size:1.15em}
    .frise-jeu .mat{display:block;font-size:.78em;opacity:.85;font-weight:500}
    .frise-bande{grid-column:2 / span 5;display:flex;gap:8px;flex-wrap:wrap}
    .frise-bande .frise-jeu{flex:1;min-width:14em}
    .frise-legende{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:8px;color:var(--doux);font-size:.85em}
    .frise-legende span{display:inline-flex;align-items:center;gap:6px}
    .frise-legende i{display:inline-block;width:1.2em;height:.8em;border-radius:3px}
    @media (max-width:760px){
      .frise-grille{grid-template-columns:1fr}
      .frise-tete.vide{display:none}
      .frise-tete{text-align:left}
      .frise-case::before{content:attr(data-periode);font-weight:700;color:var(--doux);font-size:.85em}
      .frise-bande{grid-column:auto}
    }
    @media print{ .frise-jeu{color:#000 !important;background:#fff !important;border:1px solid #888} .frise-jeu.avenir{color:#777 !important} }
  `;
  function style(){
    if(document.getElementById("style-frise")) return;
    const s = document.createElement("style"); s.id = "style-frise"; s.textContent = STYLE; document.head.appendChild(s);
  }
  function puce(j, o){
    const dispo = !!j.dossier;
    const fond = dispo ? `background:linear-gradient(135deg,${j.couleurs[0]} 0%,${j.couleurs[0]} 55%,${j.couleurs[1] || j.couleurs[0]} 150%)` : "";
    const contenu = `<span class="ic" aria-hidden="true">${esc(j.icone || "🎲")}</span><span>${esc(j.titre)}<span class="mat">${esc(j.matiere)}${dispo ? "" : " · à venir"}</span></span>`;
    const titre = `${j.titre} — ${j.matiere}${j.annee && j.annee.length === 1 ? ", Année " + j.annee : ""}${j.periodes.length === 1 ? ", " + j.periodes[0] : ""} : ${j.competences}`;
    return dispo && o.lien !== false
      ? `<a class="frise-jeu" style="${fond}" href="${esc(o.racine || "")}${esc(j.dossier)}/" title="${esc(titre)}" data-jeu="${esc(j.id)}">${contenu}</a>`
      : `<span class="frise-jeu ${dispo ? "" : "avenir"}" style="${fond}" title="${esc(titre)}" data-jeu="${esc(j.id)}">${contenu}</span>`;
  }
  function dessiner(el, o = {}){
    if(typeof CATALOGUE === "undefined" || !el) return;
    style();
    const C = CATALOGUE, jeux = C.jeux;
    const annees = o.annee ? [o.annee] : ["A", "B"];
    const tri = (a, b) => (parseInt(a.num, 10) || 99) - (parseInt(b.num, 10) || 99);
    let h = `<div class="frise"><div class="frise-grille"><div class="frise-tete vide"></div>` +
      P.map(p => `<div class="frise-tete">${p}<small>${esc(C.periodes[p] || "")}</small></div>`).join("");
    for(const a of annees){
      h += `<div class="frise-ligne">Année ${a}</div>` + P.map(p =>
        `<div class="frise-case" data-periode="${p} · Année ${a}">${jeux.filter(j => j.annee === a && !j.toutelannee && j.periodes.length === 1 && j.periodes[0] === p).sort(tri).map(j => puce(j, o)).join("")}</div>`).join("");
    }
    const annuels = jeux.filter(j => j.toutelannee && (!o.annee || j.annee === o.annee || j.annee === "AB"));
    if(annuels.length) h += `<div class="frise-ligne">Toute l'année</div><div class="frise-bande">${annuels.map(j => puce(j, o)).join("")}</div>`;
    const libres = jeux.filter(j => j.libre);
    if(libres.length) h += `<div class="frise-ligne">Révision libre</div><div class="frise-bande">${libres.map(j => puce(j, o)).join("")}</div>`;
    const nbDispo = jeux.filter(j => j.dossier).length;
    h += `</div><div class="frise-legende"><span><i style="background:linear-gradient(135deg,#1d3a8a,#b22222)"></i>disponible (${nbDispo})</span>
      <span><i style="background:#ebe7de;border:1px dashed #c9c3b5"></i>à venir (${jeux.length - nbDispo})</span>
      <span>Votre classe suit l'Année A ou l'Année B selon l'année scolaire : les deux alternent.</span></div></div>`;
    el.innerHTML = h;
  }
  window.FRISE = { dessiner };
})();
