/* ============================================================
   COUP DE POUCE DE L'ENSEIGNANT (amélioration N13) — tronc commun
   ------------------------------------------------------------
   Entre l'indice et la réponse : depuis prof.html, bouton « 🤝 » sur la ligne
   d'une équipe. Quand les indices n'ont pas suffi, l'enseignant retire UN
   obstacle sur l'énigme affichée, sans en révéler la réponse :
     qcm, intrus     un choix faux est écarté (grisé), tant qu'il en reste deux ;
     vraifaux        une affirmation est fixée sur sa bonne valeur ;
     association     une paire est reliée et fixée ;
     tri             une étiquette est rangée dans sa colonne et fixée ;
     trous, plan     une étiquette est posée dans sa case et fixée ;
     ordre           un élément est remis à sa place et fixé ;
     lettres         la lettre suivante du mot est placée et fixée ;
     code            un caractère de plus est écrit dans une case du cadenas ;
     instrument      une lecture est donnée ;
     coffre final    première lettre et longueur de chaque mot (comme au palier Découverte).
   Le code du palier Découverte (E2) est réutilisé (PALIER.ecarterChoixFaux,
   PALIER.aideCoffre, PALIER.indiceOffert). Si plus aucune aide de ce type n'est
   possible, un indice est offert (sans point retiré).
   Trace : « 1 coup de pouce de l'enseignant » au bilan de fin, dans le compte-rendu
   (champ « pouces ») et sur la ligne de l'équipe dans prof.html. Coût en points
   choisi par l'enseignant à l'envoi (aucun par défaut).
   La commande arrive par sync.js ({pouce:true, cout, id}), comme les délais (E6).
   Jeux à moteur commun d'énigmes ; Déclaration et Tour du monde (énigmes écrites
   en dur) n'en disposent pas : le bouton n'apparaît pas dans leur prof.html.
   Chargé après palier-decouverte.js et suivi-enigmes.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined" || !window.PALIER || !window.SUIVI_ENIGMES) return;
  const SUIVI = window.SUIVI_ENIGMES;
  const norm = s => typeof window.normaliser === "function" ? window.normaliser(s) : String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]/g, "");
  const clic = el => { if(el) el.dispatchEvent(new MouseEvent("click", { bubbles: true })); };
  const verrou = el => { if(el){ el.classList.add("pouce-fixe"); el.setAttribute("aria-disabled", "true"); } };

  const style = document.createElement("style");
  style.textContent = `
    .pouce-fixe{pointer-events:none!important;outline:3px solid #2e7d32;outline-offset:1px;border-radius:6px}
    .carte-intrus.ecartee-pouce{opacity:.3;text-decoration:line-through;pointer-events:none}
    .feedback.pouce{background:#e5f5ea;color:#14532d;border:2px solid #2e7d32}`;
  document.head.appendChild(style);

  /* ---------------- L'énigme affichée ---------------- */
  function enigmeAffichee(){
    const carte = [...document.querySelectorAll(".enigme-carte[data-type]")].find(c => !c.classList.contains("resolue"));
    if(!carte) return null;
    const id = carte.id.replace(/^enigme-/, "");
    const liste = typeof window.salleEnigmes === "function" ? window.salleEnigmes(ETAT.salle) : [];
    const e = liste.find(x => String(x.id) === id);
    return e ? { e, carte, d: typeof donneesNiveau === "function" ? donneesNiveau(e) : {} } : null;
  }

  /* ---------------- Une aide par type d'énigme : renvoie un texte, ou "" si rien à faire ---------------- */
  const AIDES = {
    qcm({ e, carte }, rang){
      return window.PALIER.ecarterChoixFaux(carte, e, rang) ? "un choix faux a été écarté" : "";
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

  /* ---------------- Commande de l'enseignant ---------------- */
  function coupDePouce(cout){
    if(ETAT.fini || ETAT.enPause) return null;
    cout = Math.max(0, Math.min(5, Math.round(+cout || 0)));
    let id, texte = "", type = "";
    const coffre = document.getElementById("coffre-final");
    if(coffre && !ETAT.coffreOuvert){
      id = "coffre"; type = "coffre";
      texte = window.PALIER.aideCoffre() ? "la première lettre et le nombre de lettres de chaque mot sont indiqués" : "";
    }else{
      const ctx = enigmeAffichee();
      if(!ctx) return null;
      id = ctx.e.id; type = ctx.e.type;
      const rec = SUIVI.note(id);
      texte = AIDES[type] ? AIDES[type](ctx, rec.c || 0) : "";
      if(!texte){
        const b = ctx.carte.querySelector("#indice-" + ctx.e.id);
        if(b && !b.disabled){ window.PALIER.indiceOffert(b, "coup de pouce de l'enseignant"); texte = "un indice est offert, sans retirer de point"; }
      }
    }
    if(!texte){ if(typeof toast === "function") toast("🤝 L'enseignant a voulu vous aider, mais il n'y a plus d'aide possible ici : appelez-le !"); return { ok: false, type }; }
    const rec = SUIVI.note(id, { s: ETAT.salle });
    rec.c = (rec.c || 0) + 1;
    if(cout){ ETAT.score = Math.max(0, ETAT.score - cout); }
    if(typeof majHUD === "function") majHUD();
    if(typeof sauvegarder === "function") sauvegarder();
    if(typeof son === "function") son("indice");
    if(typeof toast === "function") toast(`🤝 L'enseignant vous donne un coup de pouce : ${texte}${cout ? ` (−${cout} point${cout > 1 ? "s" : ""})` : ""}.`);
    const carte = id === "coffre" ? coffre : document.getElementById("enigme-" + id);
    const fb = carte && carte.querySelector(".feedback:not(.indice)");
    if(fb && !fb.classList.contains("show")){ fb.className = "feedback pouce show"; fb.innerHTML = `🤝 <b>Coup de pouce de l'enseignant :</b> ${texte}.`; }
    return { ok: true, type, texte, cout };
  }
  window.coupDePouce = coupDePouce;

  /* Bilan de fin de partie */
  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      const c = document.getElementById("fin-contenu");
      const total = SUIVI.liste().reduce((t, x) => t + (x.c || 0), 0);
      if(c && total && !c.querySelector(".note-pouce"))
        c.insertAdjacentHTML("beforeend", `<p class="note-pouce" style="text-align:center;opacity:.8;font-size:.9rem">🤝 ${total} coup${total > 1 ? "s" : ""} de pouce de l'enseignant pendant la partie.</p>`);
      return r;
    };
  }
  window.COUP_DE_POUCE = { AIDES, enigmeAffichee };
})();
