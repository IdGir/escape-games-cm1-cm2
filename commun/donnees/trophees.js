/* ============================================================
   TROPHÉES CUMULABLES D'UN JEU À L'AUTRE (amélioration N1)
   ------------------------------------------------------------
   Règles communes aux jeux (écran de fin) et à trophees.html.
   Calculés sur l'historique des parties de l'appareil (compte-rendu.js,
   clé escape_resultats) pour un même nom d'équipe ou d'élève (majuscules,
   accents et espaces ignorés). Seules les parties TERMINÉES comptent.
   Fichier .js (et non .json) pour fonctionner aussi en double-clic.
   ============================================================ */
var TROPHEES = (function(){
  const norm = s => String(s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/\s+/g, " ").trim().toLowerCase();
  const matiereDe = (id, cat) => { const j = cat && cat.jeux ? cat.jeux.find(x => x.dossier === id || x.id === id) : null; return j ? j.matiere : ""; };
  const finies = l => l.filter(p => p.termine);
  const jeuxDiff = l => new Set(finies(l).map(p => p.jeu));
  const parMatiere = (l, cat, m) => new Set(finies(l).filter(p => matiereDe(p.jeu, cat) === m).map(p => p.jeu)).size;

  const LISTE = [
    { id: "premier-coffre", icone: "🔓", titre: "Premier coffre", regle: "Terminer un escape game.", test: l => jeuxDiff(l).size >= 1 },
    { id: "trois-coffres", icone: "🗝️", titre: "Trois coffres", regle: "Terminer trois escape games différents.", test: l => jeuxDiff(l).size >= 3 },
    { id: "grand-explorateur", icone: "🏰", titre: "Grand explorateur", regle: "Terminer six escape games différents.", test: l => jeuxDiff(l).size >= 6 },
    { id: "sans-faute", icone: "🎯", titre: "Sans faute", regle: "Réussir au moins 90 % des énigmes d'un jeu du premier coup.", test: l => finies(l).some(p => p.total && p.premierCoup / p.total >= .9) },
    { id: "sans-coup-de-pouce", icone: "🧠", titre: "Sans coup de pouce", regle: "Terminer un jeu sans demander un seul indice.", test: l => finies(l).some(p => +p.indices === 0) },
    { id: "quizz-parfait", icone: "📝", titre: "Quizz parfait", regle: "Obtenir 5/5 au quizz final d'un jeu.", test: l => l.some(p => +p.quiz === 5) },
    { id: "historien", icone: "📜", titre: "Historien", regle: "Terminer deux jeux d'histoire.", test: (l, c) => parMatiere(l, c, "Histoire") >= 2 },
    { id: "scientifique", icone: "🔬", titre: "Scientifique", regle: "Terminer deux jeux de sciences.", test: (l, c) => parMatiere(l, c, "Sciences") >= 2 },
    { id: "geographe", icone: "🌍", titre: "Géographe", regle: "Terminer un jeu de géographie.", test: (l, c) => parMatiere(l, c, "Géographie") >= 1 },
    { id: "citoyen", icone: "🗳️", titre: "Citoyen", regle: "Terminer un jeu d'enseignement moral et civique.", test: (l, c) => parMatiere(l, c, "EMC") >= 1 },
    { id: "touche-a-tout", icone: "🌈", titre: "Touche-à-tout", regle: "Terminer des jeux dans trois matières différentes.", test: (l, c) => new Set(finies(l).map(p => matiereDe(p.jeu, c)).filter(Boolean)).size >= 3 },
    { id: "suite-de-l-histoire", icone: "🔗", titre: "La suite de l'histoire", regle: "Terminer la Déclaration, puis la Constitution.", test: l => { const f = finies(l); return f.some(p => p.jeu === "declaration") && f.some(p => p.jeu === "constitution"); } },
    { id: "perseverant", icone: "🔁", titre: "Persévérant", regle: "Rejouer un jeu déjà terminé et améliorer son score.", test: l => {
        const f = finies(l).slice().sort((a, b) => String(a.date).localeCompare(String(b.date))); const best = {};
        return f.some(p => { const b = best[p.jeu]; best[p.jeu] = Math.max(b == null ? -1 : b, +p.score || 0); return b != null && +p.score > b; }); } }
  ];

  /** Parties d'un même nom (équipe ou élève) */
  function partiesDe(nom, historique){ const n = norm(nom); return (historique || []).filter(p => p && norm(p.eleve) === n && !/^verification$/.test(n)); }
  /** Trophées obtenus : [{id, icone, titre, regle}] */
  function obtenus(nom, historique, catalogue){
    const l = partiesDe(nom, historique);
    return LISTE.filter(t => { try { return !!t.test(l, catalogue); } catch(e) { return false; } });
  }
  /** Noms présents dans l'historique (forme la plus récente de chaque nom) */
  function noms(historique){
    const m = new Map();
    (historique || []).forEach(p => { if(p && p.eleve && !/^v[ée]rification$/i.test(p.eleve)) m.set(norm(p.eleve), p.eleve); });
    return [...m.values()].sort((a, b) => a.localeCompare(b, "fr"));
  }
  return { LISTE, obtenus, partiesDe, noms, norm };
})();
