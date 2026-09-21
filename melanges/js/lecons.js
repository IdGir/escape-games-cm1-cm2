/* ============================================================
   LEÇONS — Bibliothèque consultable à tout moment
   Le Laboratoire de Madame Mélange : cinq leçons rédigées,
   une par salle (assets/data/lecons.json).
   Chaque leçon : objectifs, contenu CM1 / CM2, lexique,
   schéma SVG, source. Modal superposé, ne quitte pas le jeu.
   Reprend js/lecons.js de « Le Secret de la Déclaration ».
   ============================================================ */

let LECONS_DATA = null;

async function chargerLecons(){
  if(LECONS_DATA) return LECONS_DATA;
  let fetchOk = false;
  try{
    const resp = await fetch("assets/data/lecons.json", {cache:"no-store"});
    if(resp.ok){
      LECONS_DATA = await resp.json();
      fetchOk = true;
    }
  }catch(e){
    console.warn("Fetch lecons.json échoué (mode file:// ?). Bascule sur les leçons embarquées.");
  }
  if(!fetchOk || !LECONS_DATA || !LECONS_DATA.lecons){
    LECONS_DATA = JSON.parse(JSON.stringify(LECONS_FALLBACK));
  }
  return LECONS_DATA;
}

/* ---- Leçons embarquées minimales (secours file://) ---- */
const LECONS_FALLBACK = {
  lecons: [
    {id:"masses", salle:1, titre:"Mesurer et comparer des masses", duree:"4 min", niveau:"CM1-CM2",
     objectifs:["Comparer et mesurer des masses"],
     contenu:{cm1:"<p>La balance mesure la <b>masse</b>, en grammes (g) ou en kilogrammes (kg) : <b>1 kg = 1 000 g</b>. Masse d'un liquide = récipient plein − récipient vide.</p>",
              cm2:"<p>1 t = 1 000 kg · 1 kg = 1 000 g · 1 g = 1 000 mg. La touche « tare » remet la balance à zéro, récipient posé.</p>"},
     source:"Programme de sciences et technologie du cycle 3."},
    {id:"conservation", salle:2, titre:"La masse se conserve", duree:"3 min", niveau:"CM1-CM2",
     objectifs:["Savoir qu'un solide dissous est toujours là"],
     contenu:{cm1:"<p>eau (200 g) + sucre (20 g) → eau sucrée : <b>220 g</b>. Le sucre s'est dissous, il n'a pas disparu.</p>",
              cm2:"<p>Masse de l'eau + masse du solide = masse du mélange. Se dissoudre n'est pas fondre.</p>"},
     source:"La main à la pâte."},
    {id:"melanges", salle:3, titre:"Mélanges homogènes et hétérogènes", duree:"3 min", niveau:"CM1-CM2",
     objectifs:["Distinguer homogène et hétérogène"],
     contenu:{cm1:"<p><b>Homogène</b> : on ne voit qu'une chose (eau salée). <b>Hétérogène</b> : on voit au moins deux choses (eau et sable).</p>",
              cm2:"<p>Homogène : constituants indiscernables à l'œil nu (eau salée, air). Hétérogène : au moins deux constituants visibles.</p>"},
     source:"La main à la pâte."},
    {id:"separer-solides", salle:4, titre:"Séparer un mélange de solides", duree:"3 min", niveau:"CM1-CM2",
     objectifs:["Tamisage, aimantation, flottation, tri à la main"],
     contenu:{cm1:"<p>Le tamis trie selon la taille ; l'aimant attire le fer ; dans l'eau, la sciure flotte et le sable coule.</p>",
              cm2:"<p>Chaque méthode utilise une différence entre les constituants : taille, fer, flotter ou couler, aspect.</p>"},
     source:"La main à la pâte."},
    {id:"separer-liquide", salle:5, titre:"Séparer un solide d'un liquide", duree:"4 min", niveau:"CM1-CM2",
     objectifs:["Décanter, filtrer, évaporer"],
     contenu:{cm1:"<p>Le filtre retient le sable, mais le sel dissous passe. On récupère le sel en faisant évaporer l'eau.</p>",
              cm2:"<p>Décantation, filtration, évaporation. Protocole : peser, observer, aimanter, évaporer, comparer.</p>"},
     source:"Programme de sciences et technologie du cycle 3."}
  ]
};

/* ---- Ouvrir la bibliothèque ---- */
async function ouvrirBiblioLecons(){
  await chargerLecons();
  const overlay = document.getElementById("overlay-lecons");
  const corps = document.getElementById("corps-lecons");
  const lecons = LECONS_DATA.lecons || [];
  const niveau = ETAT.niveau || "CM2";
  const visibles = lecons.filter(l=>!(l.niveau==="CM2" && niveau==="CM1"));

  corps.innerHTML = `
    <p style="opacity:.8;font-style:italic;margin-bottom:14px">Clique sur une leçon pour la lire. Tu peux revenir au jeu quand tu veux.</p>
    <div class="biblio-grille">
      ${visibles.map(l=>`
        <div class="carte-lecon" data-id="${l.id}" role="button" tabindex="0">
          <div class="icone">Salle ${l.salle || l.icone || ""}</div>
          <div class="titre">${l.titre}</div>
          <div class="duree">⏱️ ${l.duree}</div>
        </div>
      `).join("")}
    </div>
  `;
  corps.querySelectorAll(".carte-lecon").forEach(c=>{
    c.addEventListener("click", ()=>afficherLecon(c.dataset.id));
    c.addEventListener("keydown", ev=>{ if(ev.key==="Enter" || ev.key===" "){ ev.preventDefault(); afficherLecon(c.dataset.id); } });
  });
  overlay.classList.add("show");
}

/* ---- Afficher une leçon en détail ---- */
function afficherLecon(id){
  const lecon = ((LECONS_DATA && LECONS_DATA.lecons)||[]).find(l=>l.id===id);
  if(!lecon) return;
  const niveau = (ETAT.niveau || "CM2").toLowerCase();
  const contenu = (lecon.contenu && (lecon.contenu[niveau] || lecon.contenu.cm2 || lecon.contenu.cm1)) || "";
  const corps = document.getElementById("corps-lecons");

  const objectifs = lecon.objectifs ? `<div class="encadre" style="margin-bottom:14px"><b>Tu vas apprendre à :</b><ul style="margin:6px 0 0 18px">${lecon.objectifs.map(o=>`<li>${o}</li>`).join("")}</ul></div>` : "";
  const schema = lecon.schema ? `<h4>Schéma</h4><div class="lecon-schema">${lecon.schema}</div>` : "";
  const lexique = (lecon.lexique && lecon.lexique.length) ? `<h4>Lexique</h4><dl class="lecon-lexique">${
    lecon.lexique.map(m=>`<dt>${m.mot}</dt><dd>${m.def}</dd>`).join("")}</dl>` : "";
  const source = lecon.source ? `<p class="lecon-source">Source : ${lecon.source}</p>` : "";

  corps.innerHTML = `
    <div class="lecon-contenu">
      <button class="btn petit gris" id="btn-retour-biblio" style="margin-bottom:14px">← Retour aux leçons</button>
      <h3 style="color:var(--bleu-fonce);border-bottom:2px solid var(--or);padding-bottom:6px;margin-bottom:10px">Salle ${lecon.salle||""} · ${lecon.titre}</h3>
      ${objectifs}
      ${contenu}
      ${schema}
      ${lexique}
      ${source}
    </div>
  `;
  document.getElementById("btn-retour-biblio").addEventListener("click", ouvrirBiblioLecons);
  corps.scrollTop = 0;
}

window.chargerLecons = chargerLecons;
window.ouvrirBiblioLecons = ouvrirBiblioLecons;
window.afficherLecon = afficherLecon;
