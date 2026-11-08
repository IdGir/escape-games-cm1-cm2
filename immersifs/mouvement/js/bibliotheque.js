/* ============================================================
   BIBLIOTHÈQUE DU NAUTILUS — les fiches de leçon
   ------------------------------------------------------------
   Rayons → fiches. Contenu selon le grade : « essentiel » pour tous,
   « approfondi » à partir de Timonier, « expert » pour Lieutenant et
   Second. Chaque ouverture de fiche est notée (VML.noterFiche) :
   bonus « Bien documenté », journal de bord, tableau de bord.
   Les fiches ne parlent jamais dans la scène : elles restent ici.
   ============================================================ */
var VML = window.VML || (window.VML = {});

VML.contenuFiche = function(l, grade){
  const i = VML.GRADES.indexOf(grade);
  return `<div class="fiche-corps">${l.essentiel || ""}${i >= 2 && l.approfondi ? l.approfondi : ""}${i >= 3 && l.expert ? l.expert : ""}</div>
    ${l.dans_le_roman ? `<p class="fiche-roman">📖 ${l.dans_le_roman}</p>` : ""}`;
};

VML.ouvrirBibliotheque = function(idFiche){
  let el = document.getElementById("biblio");
  if(!el){
    el = document.createElement("div");
    el.id = "biblio"; el.className = "biblio";
    el.setAttribute("role", "dialog"); el.setAttribute("aria-modal", "true"); el.setAttribute("aria-label", VML.T("bibliotheque").replace(/^La /, ""));
    document.body.appendChild(el);
  }
  const L = VML.D.lecons || { rayons: [], lecons: [] };
  const grade = VML.ETAT.niveau || "matelot";
  const consultees = VML.ETAT.fichesConsultees || [];
  el.innerHTML = `
    <div class="biblio-boite">
      <div class="biblio-tete"><h3>📚 ${VML.T("bibliotheque")}</h3><button class="fermer-biblio" aria-label="Fermer la bibliothèque">✕</button></div>
      <div class="biblio-corps">
        <nav class="biblio-rayons">
          ${L.rayons.map(r => `<div class="rayon"><div class="rayon-titre">${r.icone} ${r.titre}</div>
            ${L.lecons.filter(l => l.rayon === r.id).sort((a, b) => a.fiche - b.fiche).map(l =>
              `<button class="fiche-lien ${consultees.includes(l.id) ? "lue" : ""}" data-fiche="${l.id}">Fiche ${l.fiche} — ${l.icone} ${l.titre}</button>`).join("")}</div>`).join("")}
        </nav>
        <article class="biblio-fiche" tabindex="-1"><p class="biblio-accueil">Choisissez une fiche dans les rayons. Les réponses ne sont pas écrites telles quelles : il faut lire, comparer et réfléchir.</p></article>
      </div>
    </div>`;
  el.classList.add("ouverte");
  if(VML.son) VML.son("page");
  const fermer = () => { el.classList.remove("ouverte"); document.removeEventListener("keydown", echap, true); };
  const echap = ev => { if(ev.key === "Escape"){ ev.stopPropagation(); fermer(); } };
  document.addEventListener("keydown", echap, true);
  el.querySelector(".fermer-biblio").addEventListener("click", fermer);
  el.addEventListener("click", ev => { if(ev.target === el) fermer(); });
  const afficher = id => {
    const l = VML.lecon(id); if(!l) return;
    el.querySelectorAll(".fiche-lien").forEach(b => b.classList.toggle("active", b.dataset.fiche === id));
    const art = el.querySelector(".biblio-fiche");
    art.innerHTML = `<div class="fiche-ref">${VML.referenceFiche(id)}</div><h4>${l.icone} ${l.titre}</h4>${VML.contenuFiche(l, grade)}`;
    art.focus && art.focus();
    VML.noterFiche(id);
    const b = el.querySelector(`.fiche-lien[data-fiche="${id}"]`); if(b) b.classList.add("lue");
    if(VML.son) VML.son("page");
  };
  el.querySelectorAll(".fiche-lien").forEach(b => b.addEventListener("click", () => afficher(b.dataset.fiche)));
  if(idFiche) afficher(idFiche);
  VML.afficherFiche = afficher;
  return el;
};
