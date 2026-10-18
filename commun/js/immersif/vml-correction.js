/* ============================================================
   VARIANTES IMMERSIVES — CORRECTION COLLECTIVE PROJETABLE (amélioration D7)
   ------------------------------------------------------------
   Fournit à commun/js/correction-collective.js (chargé APRÈS ce fichier) l'adaptateur des variantes
   immersives : les escales, les grades au lieu de CM1/CM2, et pour chaque énigme sa bonne réponse
   (données du grade choisi), la phrase de justification des grades Lieutenant et Second, et le rappel
   « à retenir » (correction_origine). Accès : écran de fin d'escale (bouton), prof.html, ou
   index.html?correction=1[&niveau=<grade>][&salle=<n>]. Aucun effet sur la partie ni sur le score.
   ============================================================ */
(function(){
  const VML = window.VML;
  if(!VML || !VML.vueEnigme) return;
  const donnees = () => (VML.D || {}).enigmes || null;
  const escales = () => (donnees() || {}).escales || [];
  const esc = s => VML.echapper ? VML.echapper(s) : String(s == null ? "" : s);

  window.CORRECTION_ADAPTATEUR = {
    get titre(){ return VML.T ? VML.T("titre", document.title) : document.title; },
    motSalle: ((window.VML_JEU || {}).textes || {}).escale || "Étape",
    pret: () => !!donnees(),
    get niveaux(){ return VML.GRADES.map(g => ({ id: g, nom: VML.infoGrade(g).icone + " " + VML.infoGrade(g).nom })); },
    defaut: () => (VML.ETAT && VML.ETAT.niveau) || "matelot",
    nbSalles: () => escales().length,
    titreSalle: n => (VML.escale(n) || {}).titre || "",
    mot: n => (VML.escale(n) || {}).mot || "",
    enigmes(niveau, n){
      const es = VML.escale(n); if(!es) return [];
      const CC = window.CORRECTION_COLLECTIVE;
      return (es.enigmes || []).filter(e => e[niveau] && (!e.niveaux || !e.niveaux.length || e.niveaux.includes(niveau))).map(e => {
        const v = VML.vueEnigme(e, niveau);
        let reponse = CC ? CC.reponseHTML({ type: v.type }, v.donnees) : "";
        if(v.justification){ const j = v.justification; reponse += `<p class="cc-rappel"><b>Justification :</b> ${esc(j.options[j.bonne])}</p>`; }
        return { id: e.id, titre: e.titre, consigne: v.consigne, reponse, correction: e.correction_origine || "" };
      });
    }
  };

  /* Bouton sur l'écran de fin d'escale et sur celui du coffre */
  function bouton(){
    const c = document.getElementById("fin-contenu");
    if(!c || c.querySelector("#btn-correction-collective") || !(c.querySelector(".bilan") || c.querySelector(".coffre"))) return;
    const zone = c.querySelector(".boutons-fin");
    if(!zone) return;
    const b = document.createElement("button");
    b.type = "button"; b.id = "btn-correction-collective"; b.className = "btn-laiton";
    b.title = "Pour la mise en commun avec toute la classe : les bonnes réponses, étape par étape";
    b.textContent = "🖥️ Correction collective (à projeter)";
    b.addEventListener("click", () => window.CORRECTION_COLLECTIVE && window.CORRECTION_COLLECTIVE.ouvrir({ niveau: VML.ETAT && VML.ETAT.niveau, salle: VML.ETAT && VML.ETAT.escale }));
    zone.appendChild(b);
  }
  const demarrer = () => {
    const c = document.getElementById("fin-contenu");
    if(c && window.MutationObserver) new MutationObserver(bouton).observe(c, { childList: true, subtree: true });
  };
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
})();
