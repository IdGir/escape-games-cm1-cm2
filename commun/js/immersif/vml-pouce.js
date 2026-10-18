/* ============================================================
   VARIANTES IMMERSIVES — COUP DE POUCE DE L'ENSEIGNANT (amélioration N13)
   ------------------------------------------------------------
   Même principe que commun/js/coup-de-pouce.js, adapté au moteur VML : depuis prof.html, « 🤝 » sur la
   ligne d'une équipe. L'enseignant retire UN obstacle sur l'énigme ouverte, sans en révéler la réponse
   (les aides par type sont celles de commun/js/aides-enigmes.js : choix faux écarté, étiquette placée,
   lettre ou caractère donné, élément fixé…). Si plus aucune aide de ce type n'est possible, un indice
   est offert (sans point retiré) ; au coffre final : première lettre et longueur de chaque mot.
   Si l'équipe n'a pas ouvert d'énigme, l'aide l'attend : elle s'applique à l'ouverture du panneau.
   Trace : « pouces » dans l'état de l'énigme, le journal, le compte-rendu (vml-suivi.js) et prof.html.
   Coût en points choisi à l'envoi (aucun par défaut). Commande : {pouce:true, cout, id}.
   Chargé après js/app.js, vml-suivi.js et aides-enigmes.js.
   ============================================================ */
(function(){
  const VML = window.VML;
  if(!VML || !VML.ouvrirEnigme || !window.AIDES_ENIGMES) return;
  const { AIDES } = window.AIDES_ENIGMES;
  const toast = m => { if(VML.toast) VML.toast(m, 7000); };

  const trouver = id => { for(const es of (((VML.D || {}).enigmes || {}).escales || [])){ const e = (es.enigmes || []).find(x => x.id === id); if(e) return e; } return null; };

  /* Un indice offert : le clic passe, puis points, compteurs et jauge d'air sont rendus */
  function indiceOffert(carte){
    const b = carte.querySelector("[data-indice]");
    if(!b || b.disabled) return false;
    const E = VML.ETAT, avant = { score: E.score, t: E.indicesTotal, es: E.indicesEscale, air: E.air };
    const s = VML.etatEnigme(carte.id.replace(/^enigme-/, ""));
    const n0 = s.indices;
    b.click();
    if(s.indices === n0) return false;
    E.score = avant.score; E.indicesTotal = avant.t; E.indicesEscale = avant.es; E.air = avant.air;
    s.indicesOfferts = (s.indicesOfferts || 0) + 1;
    if(VML.majHUD) VML.majHUD();
    return true;
  }

  /** Applique un coup de pouce ; renvoie { ok, texte } ou { ok:false, attente:true }. */
  VML.coupDePouce = function(cout){
    const E = VML.ETAT;
    if(!E || E.enPause || E.fini) return null;
    cout = Math.max(0, Math.min(5, Math.round(+cout || 0)));
    const coffre = document.querySelector(".coffre") && !E.coffreOuvert;
    let texte = "", id = null, carte = null;
    if(coffre){
      id = "coffre";
      document.querySelectorAll(".coffre-case input[data-escale]").forEach(inp => {
        if(inp.disabled) return;
        const mot = String((VML.escale(+inp.dataset.escale) || {}).mot || "");
        const n = [...mot.replace(/\s/g, "")].length;
        if(mot){ inp.placeholder = mot[0] + " " + "_ ".repeat(Math.max(0, n - 1)).trim() + ` (${n} lettres)`; texte = "la première lettre et le nombre de lettres de chaque mot sont indiqués"; }
      });
    }else{
      const eid = VML.enigmeOuverte;
      carte = eid && document.getElementById("enigme-" + eid);
      if(!carte || carte.classList.contains("resolue")){
        E.poucePending = { cout, ts: Date.now() };
        if(VML.sauver) VML.sauver();
        toast("🤝 L'enseignant veut vous aider : ouvrez l'énigme en cours, le coup de pouce vous y attend.");
        return { ok: false, attente: true };
      }
      id = eid;
      const e = trouver(eid), v = VML.vueEnigme(e, carte.dataset.gradeEnigme || E.niveau), s = VML.etatEnigme(eid);
      const ctx = { e: Object.assign({}, e, { type: v.type }), carte, d: v.donnees };
      texte = AIDES[v.type] ? AIDES[v.type](ctx, s.pouces || 0) : "";
      if(!texte && indiceOffert(carte)) texte = "un indice est offert, sans retirer de point";
    }
    if(!texte){ toast("🤝 L'enseignant a voulu vous aider, mais il n'y a plus d'aide possible ici : appelez-le !"); return { ok: false }; }
    if(id !== "coffre"){ const s = VML.etatEnigme(id); s.pouces = (s.pouces || 0) + 1; }
    else E.poucesCoffre = (E.poucesCoffre || 0) + 1;
    if(cout) E.score = Math.max(0, (E.score || 0) - cout);
    if(VML.majHUD) VML.majHUD();
    if(VML.son) VML.son("indice");
    if(VML.sauver) VML.sauver();
    toast(`🤝 L'enseignant vous donne un coup de pouce : ${texte}${cout ? ` (−${cout} point${cout > 1 ? "s" : ""})` : ""}.`);
    const fb = carte && carte.querySelector("#fb-" + id);
    if(fb && !fb.classList.contains("show")){ fb.className = "feedback pouce show"; fb.innerHTML = `🤝 <b>Coup de pouce de l'enseignant :</b> ${texte}.`; }
    return { ok: true, texte, cout };
  };

  /* Coup de pouce en attente : appliqué à l'ouverture de l'énigme suivante */
  const ouvrir = VML.ouvrirEnigme;
  VML.ouvrirEnigme = function(){
    const res = ouvrir.apply(this, arguments);
    const E = VML.ETAT;
    if(E && E.poucePending && !E.enPause){
      const c = E.poucePending.cout; delete E.poucePending;
      setTimeout(() => VML.coupDePouce(c), 250);
    }
    return res;
  };
})();
