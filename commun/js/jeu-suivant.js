/* ============================================================
   JEU PRÉCÉDENT / SUIVANT EN FIN DE PARTIE (amélioration C4)
   ------------------------------------------------------------
   À l'écran de fin, un encart « Et ensuite ? » propose :
     • le jeu dont celui-ci est la SUITE DIRECTE, ou sa suite
       (champs « precedent » / « suite » du catalogue : la Déclaration
       est suivie du Sceau de la République) ;
     • sinon, le jeu disponible précédent et suivant dans la
       progression de la même année (A ou B), dans l'ordre des
       périodes P1 → P5.
   Les liens viennent de commun/donnees/catalogue.js : un futur jeu
   lié à un autre n'a qu'une ligne à y ajouter.
   Chargé après app.js, sans modifier app.js.
   ============================================================ */
(function(){
  /* jeu classique (JEU) ou variante immersive (VML_JEU) ; les liens mènent à la variante immersive par défaut */
  const idJeu = (typeof JEU !== "undefined" && JEU.id) || (window.VML_JEU && window.VML_JEU.id);
  if(typeof CATALOGUE === "undefined" || !idJeu) return;
  const pre = window.VML_JEU ? "../../" : "../";
  const jeux = CATALOGUE.jeux;
  const ici = jeux.find(j => j.dossier === idJeu || j.id === idJeu);
  if(!ici) return;
  const parId = id => jeux.find(j => j.id === id || j.dossier === id);
  const rang = j => (j.periodes && j.periodes.length ? +j.periodes[0].slice(1) : 9) * 100 + (parseInt(j.num, 10) || 50);

  function liens(){
    const out = [];
    if(ici.precedent && parId(ici.precedent)) out.push({ sens: "precedent", jeu: parId(ici.precedent), motif: "Ce jeu est la suite directe de :" });
    if(ici.suite && parId(ici.suite)) out.push({ sens: "suite", jeu: parId(ici.suite), motif: "La suite directe :" });
    if(!out.length && /^[AB]$/.test(ici.annee) && !ici.toutelannee){
      const suite = jeux.filter(j => j.dossier && j.annee === ici.annee && !j.toutelannee && j !== ici).sort((a, b) => rang(a) - rang(b));
      const avant = suite.filter(j => rang(j) < rang(ici)).pop(), apres = suite.find(j => rang(j) > rang(ici));
      if(avant) out.push({ sens: "precedent", jeu: avant, motif: `Jeu précédent de la progression (Année ${ici.annee}) :` });
      if(apres) out.push({ sens: "suite", jeu: apres, motif: `Jeu suivant de la progression (Année ${ici.annee}) :` });
    }
    return out;
  }

  function encart(){
    const l = liens();
    if(!l.length) return "";
    return `<div class="encart-suite" style="margin:22px auto;max-width:680px;padding:14px 18px;border-radius:14px;background:rgba(255,255,255,.85);color:#2b1d10;border:2px dashed rgba(0,0,0,.2)">
      <h3 style="margin:0 0 8px">🧭 Et ensuite ?</h3>
      ${l.map(x => `<p style="margin:6px 0">${x.motif}
        <a class="lien-jeu-${x.sens}" href="${pre}${x.jeu.immersif || x.jeu.dossier}/" style="font-weight:700">${x.sens === "precedent" ? "⬅️" : "➡️"} ${x.jeu.icone || ""} ${x.jeu.titre}</a>
        <span style="opacity:.75;font-size:.9rem">(${x.jeu.matiere}${x.jeu.periodes && x.jeu.periodes.length === 1 ? ", " + x.jeu.periodes[0] : ""})</span></p>`).join("")}
    </div>`;
  }

  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      const c = document.getElementById("fin-contenu");
      const h = encart();
      if(c && h && !c.querySelector(".encart-suite")){
        const boutons = [...c.querySelectorAll(".boutons")].pop();
        if(boutons) boutons.insertAdjacentHTML("afterend", h); else c.insertAdjacentHTML("beforeend", h);
      }
      return r;
    };
  }
  /* Variantes immersives : l'encart s'ajoute à l'écran du coffre ouvert */
  if(window.VML && typeof window.VML.ouvrirCoffre === "function"){
    const ouvrirCoffre = window.VML.ouvrirCoffre;
    window.VML.ouvrirCoffre = function(){
      const res = ouvrirCoffre.apply(this, arguments);
      const E = window.VML.ETAT, c = document.getElementById("fin-contenu"), h = encart();
      if(E && E.coffreOuvert && c && h && !c.querySelector(".encart-suite")) c.insertAdjacentHTML("beforeend", h);
      return res;
    };
  }
  window.JEU_SUIVANT = { liens, encart };
})();
