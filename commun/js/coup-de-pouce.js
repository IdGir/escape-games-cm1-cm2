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
  if(typeof ETAT === "undefined" || !window.PALIER || !window.SUIVI_ENIGMES || !window.AIDES_ENIGMES) return;
  const SUIVI = window.SUIVI_ENIGMES;
  const { AIDES, norm, clic } = window.AIDES_ENIGMES;
  AIDES.qcm = ({ e, carte }, rang) => window.PALIER.ecarterChoixFaux(carte, e, rang) ? "un choix faux a été écarté" : "";   // code du palier Découverte réutilisé

  /* ---------------- L'énigme affichée ---------------- */
  function enigmeAffichee(){
    const carte = [...document.querySelectorAll(".enigme-carte[data-type]")].find(c => !c.classList.contains("resolue"));
    if(!carte) return null;
    const id = carte.id.replace(/^enigme-/, "");
    const liste = typeof window.salleEnigmes === "function" ? window.salleEnigmes(ETAT.salle) : [];
    const e = liste.find(x => String(x.id) === id);
    return e ? { e, carte, d: typeof donneesNiveau === "function" ? donneesNiveau(e) : {} } : null;
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
