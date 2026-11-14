/* ============================================================
   CHIFFRES SIMPLES DU KIT DE PRÉSENTATION (amélioration N21)
   ------------------------------------------------------------
   Nombre de jeux jouables, de jeux prévus à la progression, de matières et de
   compétences du programme couvertes, tirés du catalogue (commun/donnees/catalogue.js, la
   source de la vue d'ensemble de l'année, C1) et des leçons de chaque jeu : ils sont donc
   à jour tout seuls quand un jeu est publié. Même décompte que le passeport de compétences (C3) :
   une compétence par leçon de chaque jeu publié.
   Utilisation : <span data-chiffre="jeux">…</span>, puis CHIFFRES.afficher().
   ============================================================ */
var CHIFFRES = (function(){
  async function lireJson(url){ try{ const r = await fetch(url, { cache: "no-store" }); return r.ok ? await r.json() : null; }catch(e){ return null; } }
  /** Renvoie { jeux, prevus, matieres[], competences, enigmes, niveaux, estime } */
  async function calculer(racine){
    racine = racine || "../";
    const cat = (typeof CATALOGUE !== "undefined" && CATALOGUE.jeux) || [];
    const publies = cat.filter(j => j.dossier);
    const matieres = [...new Set(publies.map(j => j.matiere))];
    let competences = 0, estime = false;
    for(const j of publies){
      const a = await lireJson(`${racine}${j.dossier}/assets/data/lecons-a4.json`);
      if(a && a.lecons){ competences += Object.values(a.lecons).filter(l => l && l.competence).length; }
      else if(j.classique !== false){ competences += 1; estime = true; }   // lecture impossible (double-clic) : au moins la compétence du catalogue ; jeu immersif seul sans leçons A4 : rien
    }
    return { jeux: publies.length, prevus: cat.length, matieres, nbMatieres: matieres.length, competences, estime, niveaux: 3 };
  }
  async function afficher(racine){
    const c = await calculer(racine);
    const v = { jeux: c.jeux, prevus: c.prevus, matieres: c.nbMatieres, listematieres: c.matieres.join(", "), competences: (c.estime ? "≈ " : "") + c.competences, niveaux: c.niveaux };
    document.querySelectorAll("[data-chiffre]").forEach(el => { const k = el.dataset.chiffre; if(k in v) el.textContent = v[k]; });
    window.CHIFFRES_VALEURS = c;
    return c;
  }
  return { calculer, afficher };
})();
