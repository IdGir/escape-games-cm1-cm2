/* ============================================================
   MODULE CONCOURS — entièrement FACULTATIF
   ------------------------------------------------------------
   Désactivé par défaut. L'enseignant l'active dans ⚙️ Réglages →
   « Concours ». Il ajoute alors, à la toute fin de la partie et
   APRÈS le bilan, un encart annonçant le concours « Découvrons
   notre Constitution » et une fiche de projet à imprimer.

   Le contenu (édition, thème, dates, liens) vient de
   assets/data/concours.json : il se met à jour sans toucher au code.
   ============================================================ */

const CONCOURS_FALLBACK = {
  nom: "Découvrons notre Constitution",
  organisateurs: "Ministère de l'Éducation nationale et Conseil constitutionnel",
  session: "2026-2027",
  theme: "L'État de droit",
  categorie_visee: "Cycle 3 (CM1, CM2, 6e)",
  participation: "collective : une classe, plusieurs classes ou un établissement",
  formats: ["texte ou dossier","film, documentaire","affiche, production plastique","pièce de théâtre, chorégraphie","site internet"],
  dates: [
    {quoi:"Inscription", quand:"jusqu'au vendredi 29 janvier 2027", comment:"via l'application ADAGE, ou par le formulaire officiel pour les établissements sans ADAGE"},
    {quoi:"Dépôt des productions", quand:"mardi 4 mai 2027", comment:"auprès du référent académique"},
    {quoi:"Jury académique", quand:"avant le 27 mai 2027", comment:"sélection des travaux transmis au jury national"},
    {quoi:"Jury national", quand:"fin juin / début juillet 2027", comment:""},
    {quoi:"Remise des prix", quand:"septembre-octobre 2027", comment:"au Conseil constitutionnel, à Paris"}
  ],
  liens: [
    {libelle:"Règlement officiel et formulaires (éduscol)", url:"https://eduscol.education.gouv.fr/3295/concours-decouvrons-notre-constitution"},
    {libelle:"Ressources pédagogiques (decouvronsnotreconstitution.fr)", url:"https://www.decouvronsnotreconstitution.fr/concours-decouvrons-notre-constitution"},
    {libelle:"Page du Conseil constitutionnel", url:"https://www.conseil-constitutionnel.fr/evenements/concours-decouvrons-notre-constitution"}
  ],
  contact: "laconstitution.dgesco@education.gouv.fr",
  avertissement: "Dates et thème relevés le 19 septembre 2026 sur les sites officiels. Vérifiez le règlement en vigueur avant toute inscription : il fait seul foi."
};

function donneesConcours(){
  const c = (typeof CONCOURS === "function" ? CONCOURS() : null);
  return (c && c.nom) ? c : CONCOURS_FALLBACK;
}

/* ---- Encart affiché en fin de partie (si l'option est activée) ---- */
function afficherConcours(){
  const zone = document.getElementById("zone-concours");
  if(!zone || zone.dataset.fait) return;
  zone.dataset.fait = "1";
  const c = donneesConcours();

  zone.innerHTML = `
    <div class="encart-concours">
      <h3>🏛️ Et maintenant ? Le concours « ${c.nom} »</h3>
      <p>Vous venez d'ouvrir le coffre. Votre classe connaît désormais la Constitution
         assez bien pour <b>présenter son propre travail</b> au concours national
         <b>« ${c.nom} »</b>, organisé par le ${c.organisateurs}.</p>
      <p><b>Session ${c.session}</b> · thème : <b>« ${c.theme} »</b> ·
         catégorie <b>${c.categorie_visee}</b> · participation ${c.participation}.</p>

      <p style="margin-top:10px"><b>Sous quelle forme ?</b> Au choix :</p>
      <ul>${(c.formats||[]).map(f=>`<li>${f}</li>`).join("")}</ul>

      <div class="dates">
        ${(c.dates||[]).map(d=>`<div class="date-case"><b>${d.quoi}</b>${d.quand}${d.comment?`<br><span style="opacity:.75">${d.comment}</span>`:""}</div>`).join("")}
      </div>

      <p><b>Pour aller plus loin :</b></p>
      <ul>${(c.liens||[]).map(l=>`<li><a href="${l.url}" target="_blank" rel="noopener">${l.libelle}</a></li>`).join("")}</ul>
      ${c.contact?`<p>Contact national : <b>${c.contact}</b></p>`:""}

      <div class="boutons" style="margin-top:12px">
        <button class="btn or" id="btn-fiche-concours">🖨️ Imprimer la fiche de projet</button>
      </div>
      <p class="avert">⚠️ ${c.avertissement}</p>
    </div>`;

  const b = document.getElementById("btn-fiche-concours");
  if(b) b.addEventListener("click", imprimerFicheConcours);
  zone.scrollIntoView({behavior:"smooth", block:"start"});
  if(typeof son === "function") son("badge");
}

/* ---- Fiche A4 : de l'escape game au projet de concours ---- */
function imprimerFicheConcours(){
  const c = donneesConcours();
  const zone = preparerZoneImpression();
  zone.innerHTML = `
    ${enteteFiche("Du jeu au projet — concours « "+c.nom+" »", "Fiche de projet — cycle 3", ETAT.equipe, false)}
    <p><b>Session ${c.session}</b> — thème : <b>« ${c.theme} »</b> — catégorie : ${c.categorie_visee}.
       Participation ${c.participation}. Organisé par le ${c.organisateurs}.</p>

    <h3>1. Ce que notre classe a appris pendant l'escape game</h3>
    <table class="tab-fiche">
      <tr><th style="width:34%">Salle</th><th>Ce que nous savons maintenant</th></tr>
      <tr><td>1 — La cour du Palais-Royal</td><td style="height:34px"></td></tr>
      <tr><td>2 — La salle des Textes</td><td style="height:34px"></td></tr>
      <tr><td>3 — L'hémicycle</td><td style="height:34px"></td></tr>
      <tr><td>4 — La navette parlementaire</td><td style="height:34px"></td></tr>
      <tr><td>5 — Le Conseil constitutionnel</td><td style="height:34px"></td></tr>
    </table>

    <h3>2. Notre sujet</h3>
    <p style="font-size:.9rem;font-style:italic">Quel aspect de la Constitution voulons-nous faire découvrir ?
       Un article, un principe, un droit du quotidien, une institution…</p>
    <div class="cadre-libre" style="height:70px"></div>

    <h3>3. Notre forme</h3>
    <p>${(c.formats||[]).map(f=>`☐ ${f}`).join(" &nbsp; ")} &nbsp; ☐ autre : ..............................</p>

    <h3>4. Notre plan de travail</h3>
    <table class="tab-fiche">
      <tr><th style="width:24%">Étape</th><th style="width:38%">Qui fait quoi</th><th>Pour quand</th></tr>
      <tr><td>Chercher</td><td style="height:30px"></td><td></td></tr>
      <tr><td>Écrire / dessiner</td><td style="height:30px"></td><td></td></tr>
      <tr><td>Fabriquer</td><td style="height:30px"></td><td></td></tr>
      <tr><td>Relire et corriger</td><td style="height:30px"></td><td></td></tr>
      <tr><td>Déposer</td><td style="height:30px"></td><td></td></tr>
    </table>

    <h3>5. Le calendrier officiel</h3>
    <table class="tab-fiche">
      <tr><th style="width:30%">Étape</th><th style="width:34%">Date</th><th>Comment</th></tr>
      ${(c.dates||[]).map(d=>`<tr><td>${d.quoi}</td><td>${d.quand}</td><td>${d.comment||""}</td></tr>`).join("")}
    </table>

    <h3>6. Où trouver le règlement</h3>
    <ul>${(c.liens||[]).map(l=>`<li>${l.libelle} — <span style="font-size:.8rem">${l.url}</span></li>`).join("")}</ul>
    ${c.contact?`<p>Contact national : ${c.contact}</p>`:""}
    <p style="font-size:.78rem;font-style:italic;margin-top:10px">${c.avertissement}</p>
    ${piedPageFiche(1,1,"Fiche de projet — concours")}
  `;
  window.print();
}

window.afficherConcours      = afficherConcours;
window.imprimerFicheConcours = imprimerFicheConcours;
window.donneesConcours       = donneesConcours;
