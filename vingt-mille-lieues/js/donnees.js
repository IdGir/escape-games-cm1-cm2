/* ============================================================
   DONNÉES — chargement des fichiers JSON du jeu
   ------------------------------------------------------------
   En ligne ou avec serveur.py : fetch() des fichiers de assets/data/
   (une correction d'un JSON est prise en compte tout de suite).
   En double-clic (file://), fetch est bloqué par le navigateur :
   on prend la copie embarquée js/donnees-embarquees.js, régénérée
   par outils/embarquer-donnees.py (un test vérifie qu'elle est à jour).
   ============================================================ */
var VML = window.VML || (window.VML = {});

VML.FICHIERS_DONNEES = ["enigmes", "lecons", "decors-fx", "dialogues", "personnages"];

VML.chargerDonnees = async function(){
  const D = {};
  const emb = window.VML_DONNEES_EMBARQUEES || {};
  for(const nom of VML.FICHIERS_DONNEES){
    let val = null;
    if(location.protocol !== "file:"){
      try{
        const r = await fetch("assets/data/" + nom + ".json", {cache: "no-cache"});
        if(r.ok) val = await r.json();
      }catch(e){ val = null; }
    }
    D[nom] = val || emb[nom] || null;
  }
  VML.D = D;
  return D;
};

/* Raccourcis */
VML.escale = function(num){
  return ((VML.D.enigmes || {}).escales || []).find(e => e.numero === +num) || null;
};
VML.lecon = function(id){
  return ((VML.D.lecons || {}).lecons || []).find(l => l.id === id) || null;
};
VML.rayon = function(id){
  return ((VML.D.lecons || {}).rayons || []).find(r => r.id === id) || null;
};
VML.decor = function(id){
  return ((VML.D["decors-fx"] || {}).decors || {})[id] || null;
};
VML.perso = function(id){
  return ((VML.D.personnages || {}).personnages || {})[id] || null;
};
/** « Rayon Électricité, fiche 2 » */
VML.referenceFiche = function(id){
  const l = VML.lecon(id); if(!l) return "";
  const r = VML.rayon(l.rayon);
  return (r ? r.titre : "Bibliothèque") + ", fiche " + l.fiche;
};
