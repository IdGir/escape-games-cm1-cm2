/* ============================================================
   AIDES NON RÉVÉLATRICES PAR TYPE D'ÉNIGME (amélioration N13) — tronc commun
   ------------------------------------------------------------
   Une aide par type d'énigme du moteur commun (commun/js/enigmes.js), sans en
   révéler la réponse : choix faux écarté, affirmation / paire / étiquette /
   élément / lettre fixés, caractère de plus au cadenas, lecture donnée.
   Indépendant du jeu : utilisé par coup-de-pouce.js (jeux classiques) et par
   immersif/vml-pouce.js (variantes immersives), qui fournissent l'énigme affichée.
     AIDES_ENIGMES.AIDES[type]({ e, carte, d, ecarterChoixFaux? }, rang) → texte, ou "" si rien à faire
   ============================================================ */
(function(){
  const norm = s => typeof window.normaliser === "function" ? window.normaliser(s) : String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]/g, "");
  const clic = el => { if(el) el.dispatchEvent(new MouseEvent("click", { bubbles: true })); };
  const verrou = el => { if(el){ el.classList.add("pouce-fixe"); el.setAttribute("aria-disabled", "true"); } };

  const style = document.createElement("style");
  style.textContent = `
    .pouce-fixe{pointer-events:none!important;outline:3px solid #2e7d32;outline-offset:1px;border-radius:6px}
    .carte-intrus.ecartee-pouce{opacity:.3;text-decoration:line-through;pointer-events:none}
    .feedback.pouce{background:#e5f5ea;color:#14532d;border:2px solid #2e7d32}`;
  document.head.appendChild(style);

  /* Un choix faux de plus écarté dans chaque QCM d'au moins trois choix (tant qu'il reste deux choix) */
  function ecarterChoixFaux(carte, e, d, rang){
    let n = 0;
    ((d && d.questions) || []).forEach((q, i) => {
      if(!q.options || q.options.length < 3) return;
      const bloc = carte.querySelector(`.qcm-question[data-i="${i}"]`); if(!bloc) return;
      const faux = q.options.map((_, j) => j).filter(j => j !== q.bonne && !bloc.querySelector(`.qcm-option[data-j="${j}"].ecartee`));
      if(faux.length < 2) return;
      const o = bloc.querySelector(`.qcm-option[data-j="${faux[(i + String(e.id).length + (rang || 0)) % faux.length]}"]`);
      if(o){ o.classList.add("ecartee"); o.classList.remove("select"); o.setAttribute("aria-disabled", "true"); o.title = "Choix écarté"; n++; }
    });
    return n;
  }

  /* ---------------- Une aide par type d'énigme : renvoie un texte, ou "" si rien à faire ---------------- */
  const AIDES = {
    qcm(ctx, rang){
      return (ctx.ecarterChoixFaux ? ctx.ecarterChoixFaux(ctx.carte, ctx.e, rang) : ecarterChoixFaux(ctx.carte, ctx.e, ctx.d, rang)) ? "un choix faux a été écarté" : "";
    },
    intrus({ carte }){
      const faux = [...carte.querySelectorAll('.carte-intrus[data-intrus="0"]:not(.ecartee-pouce)')];
      if(faux.length < 2) return "";
      const c = faux[0]; c.classList.add("ecartee-pouce"); c.classList.remove("select");
      return "une carte qui n'est pas l'intrus a été écartée";
    },
    vraifaux({ d, carte }){
      const lignes = [...carte.querySelectorAll(".vf-ligne")];
      const l = lignes.find(x => !x.classList.contains("pouce-fixe")); if(!l) return "";
      const a = (d.affirmations || [])[+l.dataset.i];
      clic(l.querySelector(`[data-rep="${a && a.vrai ? "vrai" : "faux"}"]`));
      verrou(l);
      return "une affirmation a été fixée sur sa bonne réponse";
    },
    association({ carte }){
      const c = [...carte.querySelectorAll('[data-col="g"] .carte-match')].find(x => !x.classList.contains("pouce-fixe")); if(!c) return "";
      const d = carte.querySelector(`[data-col="d"] [data-id="${c.dataset.bon}"]`); if(!d) return "";
      clic(c); clic(d); verrou(c); verrou(d);
      return "une paire a été reliée";
    },
    tri({ carte }){
      const mal = [...carte.querySelectorAll(".carte-tri")].find(c => !c.classList.contains("pouce-fixe")
        && !(c.parentNode.classList.contains("tri-zone") && c.closest(".tri-colonne").dataset.col === c.dataset.col));
      if(!mal) return "";
      clic(mal); clic(carte.querySelector(`.tri-colonne[data-col="${mal.dataset.col}"] .tri-zone`));
      mal.classList.remove("select"); verrou(mal);
      return "une étiquette a été rangée dans sa colonne";
    },
    trous(ctx){ return placerEtiquette(ctx, ".trou"); },
    plan(ctx){ return placerEtiquette(ctx, ".plan-case"); },
    ordre({ carte }){
      const liste = carte.querySelector(".liste-ordre"); if(!liste) return "";
      garderOrdre(liste);
      const items = [...liste.querySelectorAll(".item-ordre")];
      const libres = items.map((it, i) => i).filter(i => !items[i].classList.contains("pouce-fixe"));
      /* le plus petit rang non encore fixé */
      const cible = items.filter(it => !it.classList.contains("pouce-fixe")).sort((x, y) => +x.dataset.rang - +y.dataset.rang)[0];
      if(!cible) return "";
      const place = +cible.dataset.rang - 1;
      if(!libres.includes(place)) return "";
      const ordre = libres.map(i => items[i]).filter(it => it !== cible);
      ordre.splice(libres.indexOf(place), 0, cible);
      const finale = items.slice();
      libres.forEach((pos, k) => { finale[pos] = ordre[k]; });
      finale.forEach(it => liste.appendChild(it));
      finale.forEach((it, i) => { const r = it.querySelector(".rang"); if(r) r.textContent = i + 1; });
      verrou(cible);
      return "un élément a été remis à sa place";
    },
    lettres({ d, carte }){
      const cible = (d.cible || []).map(String);
      const slots = [...carte.querySelectorAll(".slot")];
      const k = slots.filter(s => s.classList.contains("pouce-fixe")).length;
      if(k >= cible.length) return "";
      slots.filter(s => s.classList.contains("ok") && !s.classList.contains("pouce-fixe")).forEach(clic);
      const l = [...carte.querySelectorAll("[data-l]:not(.utilisee)")].find(x => norm(x.dataset.l) === norm(cible[k]));
      if(!l) return "";
      clic(l); verrou(slots[k]);
      return `la lettre n° ${k + 1} du mot a été placée`;
    },
    code({ d, carte }){
      for(const [i, c] of (d.champs || []).entries()){
        const inp = carte.querySelector("#code-" + i); if(!inp || inp.disabled) continue;
        const v = String(c.valeur), k = +(inp.dataset.pouce || 0);
        if(norm(inp.value) === norm(v) || k >= v.length - 1) continue;
        inp.value = v.slice(0, k + 1); inp.dataset.pouce = k + 1;
        return `un caractère de plus est écrit dans la case « ${c.libelle} »`;
      }
      return "";
    },
    instrument({ d, carte }){
      const it = [...carte.querySelectorAll(".instr-item")].find(x => !x.classList.contains("verrouille")); if(!it) return "";
      const item = (d.items || [])[+it.dataset.i]; if(!item) return "";
      if(it.dataset.mode === "lire"){ const inp = it.querySelector(".instr-champ"); inp.value = String(item.valeur).replace(".", ","); inp.disabled = true; }
      else clic(it.querySelector(`.instr-cran[data-v="${item.valeur}"]`));
      it.classList.add("verrouille");
      return "une lecture a été donnée";
    }
  };
  /* trous (texte à trous) et plan (schéma) : une étiquette posée dans sa case */
  function placerEtiquette({ carte }, selecteur){
    const slot = [...carte.querySelectorAll(selecteur)].find(s => !s.classList.contains("pouce-fixe") && norm(s.dataset.pose) !== norm(s.dataset.rep));
    if(!slot) return "";
    if(slot.dataset.pose) clic(slot);                                         // vide la case si elle contient une mauvaise étiquette
    const ailleurs = [...carte.querySelectorAll(selecteur)].find(s => s !== slot && s.dataset.pose && norm(s.dataset.pose) === norm(slot.dataset.rep));
    if(ailleurs) clic(ailleurs);                                              // reprend l'étiquette posée ailleurs
    const et = [...carte.querySelectorAll(".etiquette:not(.posee)")].find(x => norm(x.dataset.mot) === norm(slot.dataset.rep));
    if(!et) return "";
    clic(et); clic(slot); verrou(slot);
    return "une étiquette a été posée dans sa case";
  }
  /* Ordre : un élément fixé ne bouge plus, les autres passent par-dessus (échange avec le voisin libre) */
  function garderOrdre(liste){
    if(liste.dataset.pouce) return;
    liste.dataset.pouce = "1";
    liste.addEventListener("click", ev => {
      const b = ev.target.closest && ev.target.closest(".btn-monter, .btn-descendre"); if(!b) return;
      const it = b.closest(".item-ordre"), items = [...liste.querySelectorAll(".item-ordre")];
      if(!items.some(x => x.classList.contains("pouce-fixe"))) return;
      ev.stopImmediatePropagation(); ev.preventDefault();
      if(it.classList.contains("pouce-fixe")) return;
      const sens = b.classList.contains("btn-monter") ? -1 : 1;
      let j = items.indexOf(it) + sens;
      while(items[j] && items[j].classList.contains("pouce-fixe")) j += sens;
      const autre = items[j]; if(!autre) return;
      const marqueur = document.createElement("span"); it.before(marqueur); autre.before(it); marqueur.replaceWith(autre);
      [...liste.querySelectorAll(".item-ordre")].forEach((x, i) => { const r = x.querySelector(".rang"); if(r) r.textContent = i + 1; });
    }, true);
  }
  window.AIDES_ENIGMES = { AIDES, norm, clic, verrou, ecarterChoixFaux };
})();
