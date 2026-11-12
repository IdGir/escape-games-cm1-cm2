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

/* Configuration du jeu (js/jeu-config.js) et textes du thème */
VML.JEU = window.VML_JEU || { id: "vingt-mille-lieues", prefixeStockage: "vml", grades: ["mousse", "matelot", "timonier", "lieutenant", "second"], textes: {} };
VML.T = function(cle, defaut){ const t = (VML.JEU.textes || {})[cle]; return t == null ? (defaut == null ? "" : defaut) : t; };
/** Remplace le texte des éléments portant data-t="<clé>" (data-t-html pour du HTML) et le titre de la page. */
VML.appliquerTextes = function(racine){
  (racine || document).querySelectorAll("[data-t]").forEach(el => { const t = VML.T(el.dataset.t, null); if(t) el.textContent = t; });
  (racine || document).querySelectorAll("[data-t-attr]").forEach(el => { const [a, c] = el.dataset.tAttr.split(":"); const t = VML.T(c, null); if(t) el.setAttribute(a, t); });
  const titre = document.documentElement.dataset.titrePage;
  if(titre) document.title = VML.motsDuTheme(titre.replace("{journal}", VML.T("journal", document.title)));
  VML.activerMots();
};

/** Vocabulaire du thème : remplace « escale(s) » par le mot du jeu (VML_JEU.mots.escale, au féminin) dans le TEXTE affiché. */
VML.motsDuTheme = function(s){
  const m = VML.JEU.mots; if(!m || !m.escale || m.escale === "escale") return s;
  const pl = m.escales || m.escale + "s", maj = x => x.charAt(0).toUpperCase() + x.slice(1);
  return s.replace(/\b([Ll])['’]escale(s?)\b/g, (x, l, p) => (l === "L" ? "La " : "la ") + (p ? pl : m.escale))
          .replace(/\b([Ee])scale(s?)\b/g, (x, e, p) => { const w = p ? pl : m.escale; return e === "E" ? maj(w) : w; });
};
VML.activerMots = function(){
  const m = VML.JEU.mots; if(!m || !m.escale || m.escale === "escale" || VML._motsActifs) return;
  VML._motsActifs = true;
  const passer = n => {
    if(n.nodeType === 3){ const t = VML.motsDuTheme(n.nodeValue); if(t !== n.nodeValue) n.nodeValue = t; return; }
    if(n.nodeType !== 1 || /^(SCRIPT|STYLE|TEXTAREA)$/.test(n.nodeName)) return;
    n.childNodes.forEach(passer);
    ["title", "aria-label", "placeholder"].forEach(a => { const v = n.getAttribute(a); if(v){ const t = VML.motsDuTheme(v); if(t !== v) n.setAttribute(a, t); } });
  };
  passer(document.body);
  new MutationObserver(ms => ms.forEach(r => { r.addedNodes.forEach(passer); if(r.type === "characterData") passer(r.target); }))
    .observe(document.body, { childList: true, subtree: true, characterData: true });
};

/* Raccourcis */
const _escaleBrute = num => ((VML.D.enigmes || {}).escales || []).find(e => e.numero === +num) || null;
const _escalesFiltrees = {};
/** Escale vue par le grade en cours : une énigme portant "niveaux": ["timonier"] n'existe que pour ces grades. */
VML.escale = function(num){
  const es = _escaleBrute(num), g = window.ETAT && window.ETAT.niveau;
  if(!es || !g || !es.enigmes.some(e => e.niveaux && e.niveaux.length)) return es;
  const cle = es.numero + "|" + g;
  const f = _escalesFiltrees[cle];
  if(f && f._source === es) return f;
  return (_escalesFiltrees[cle] = Object.assign({}, es, { enigmes: es.enigmes.filter(e => !e.niveaux || !e.niveaux.length || e.niveaux.includes(g)), _source: es }));
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

/* Textes du thème appliqués dès que la page est prête (toutes les pages du jeu chargent ce fichier) */
if(typeof document !== "undefined"){
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", () => VML.appliquerTextes());
  else VML.appliquerTextes();
}
