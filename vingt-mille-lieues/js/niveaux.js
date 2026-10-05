/* ============================================================
   NIVEAUX — les cinq grades du Nautilus
   ------------------------------------------------------------
   Les grades sont affichés sans aucune étiquette scolaire. Leur
   équivalent (≈ CE2 … ≈ 5ᵉ) n'apparaît que dans le guide et prof.html.
   Le moteur commun (commun/js/enigmes.js) lit déjà les blocs par
   niveau : donneesNiveau(e) cherche e[ETAT.niveau] ; il suffit donc
   que ETAT.niveau vaille « mousse », « matelot »…
   ============================================================ */
var VML = window.VML || (window.VML = {});

VML.GRADES = ["mousse", "matelot", "timonier", "lieutenant", "second"];

VML.infoGrade = function(id){
  const l = ((VML.D && VML.D.enigmes) || {}).niveaux || [];
  return l.find(n => n.id === id) || { id, nom: id, icone: "⚓" };
};
VML.gradeValide = function(id){
  id = String(id || "").toLowerCase();
  return VML.GRADES.includes(id) ? id : null;
};
VML.gradeSuivant = function(id){
  const i = VML.GRADES.indexOf(id);
  return i >= 0 && i < VML.GRADES.length - 1 ? VML.GRADES[i + 1] : null;
};
/** Aide « Découverte » intégrée au grade Mousse */
VML.aideRenforcee = g => g === "mousse";
/** Justification demandée (Lieutenant, Second) */
VML.avecJustification = g => g === "lieutenant" || g === "second";

/**
 * Vue d'une énigme pour un grade : fusion de la fiche commune
 * et du bloc du grade (type, consigne, données, indices…).
 */
VML.vueEnigme = function(e, grade){
  const b = e[grade] || e.matelot || {};
  return {
    e, grade,
    type: b.type || e.type,
    consigne: b.consigne || "",
    dialogue: b.dialogue || "",
    donnees: b,
    indices: b.indices || [],
    justification: VML.avecJustification(grade) ? (b.justification || null) : null
  };
};
