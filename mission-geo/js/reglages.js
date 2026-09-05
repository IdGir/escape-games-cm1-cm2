/* =========================================================
   ESPACE ENSEIGNANT — réglages, repères locaux, récompense,
   impressions, sauvegarde.
   ========================================================= */

const REGLAGES = (function(){

  function ouvrir(){
    const etat = SAUVEGARDE.lire();
    const r = etat.reglages, p = etat.profil, rec = etat.recompense;

    const h = `
      <h2>⚙️ Espace enseignant</h2>
      <p class="aide-panneau">Ces réglages sont conservés sur ce poste. Ils ne modifient
      jamais le contenu des séances : ils adaptent l'application à votre classe.</p>

      <h3>📍 Repères locaux de la classe</h3>
      <p class="aide-panneau">Utilisés par les séances 1 et 2 pour que les élèves complètent
      la fiche de <b>leur</b> commune. Par défaut : les valeurs du livret papier (Dijon).</p>
      <div class="deux-colonnes">
        <label>Commune<input type="text" id="r-commune" value="${e(p.commune)}"></label>
        <label>Département<input type="text" id="r-departement" value="${e(p.departement)}"></label>
        <label>N° du département<input type="text" id="r-numdep" value="${e(p.numeroDepartement)}"></label>
        <label>Région<input type="text" id="r-region" value="${e(p.region)}"></label>
        <label>Pays<input type="text" id="r-pays" value="${e(p.pays)}"></label>
        <label>Continent<input type="text" id="r-continent" value="${e(p.continent)}"></label>
      </div>

      <h3>👀 Accessibilité</h3>
      <label>Taille des textes
        <select id="r-taille">
          <option value="1">100 %</option>
          <option value="1.15">115 %</option>
          <option value="1.3">130 %</option>
          <option value="1.5">150 %</option>
        </select>
      </label>
      <p><label><input type="checkbox" id="r-anim"> Réduire les animations</label></p>

      <h3>🎬 Multimédia</h3>
      <p class="aide-panneau">Le jeu cherche d'abord une vidéo, puis une image, puis retombe
      sur son dessin intégré. Aucun fichier n'est obligatoire.</p>
      <p><label><input type="checkbox" id="r-video"> Autoriser les vidéos</label></p>
      <p><label><input type="checkbox" id="r-sonvideo"> Son des vidéos activé</label></p>
      <p><label><input type="checkbox" id="r-images"> Autoriser les images déposées</label></p>
      <button class="bouton-second" id="r-diag">🔍 Vérifier les fichiers détectés</button>
      <div id="r-diag-sortie"></div>

      <h3>🧭 Déroulement</h3>
      <p><label><input type="checkbox" id="r-libre"> Ordre libre : toutes les séances
      accessibles d'emblée (utile pour préparer, réviser ou rattraper)</label></p>

      <h3>🏆 Récompense mystère</h3>
      <p class="aide-panneau">Affichée à la toute fin, une fois la valise ouverte.
      Vous pouvez la définir maintenant ou plus tard.</p>
      <p><label><input type="checkbox" id="r-rec-active"> Activer ma récompense</label></p>
      <label>Titre<input type="text" id="r-rec-titre" value="${e(rec.titre)}"
        placeholder="Ex. : Votre récompense"></label>
      <label>Message<textarea id="r-rec-texte" rows="4"
        placeholder="Ex. : Bravo ! Rendez-vous vendredi pour…">${e(rec.texte)}</textarea></label>
      <label>Nom du fichier image ou vidéo (sans extension), déposé dans <code>assets/</code>
        <input type="text" id="r-rec-media" value="${e(rec.media)}" placeholder="recompense"></label>

      <h3>🖨️ Impressions</h3>
      <p class="aide-panneau">Choisissez une séance, puis la fiche à imprimer.</p>
      <label>Séance
        <select id="r-seance">
          ${MISSION.ordre().map(s => `<option value="${s.id}">Séance ${s.numero} — ${e(s.titre)}</option>`).join("")}
        </select>
      </label>
      <p style="display:flex;gap:.5rem;flex-wrap:wrap">
        <button class="bouton-second" id="r-imp-prep">Fiche de préparation</button>
        <button class="bouton-second" id="r-imp-eleve">Fiche élève</button>
        <button class="bouton-second" id="r-imp-corrige">Corrigé</button>
        <button class="bouton-second" id="r-imp-lecon">Leçon</button>
      </p>
      <p style="display:flex;gap:.5rem;flex-wrap:wrap">
        <button class="bouton-second" id="r-imp-prog">Progression annuelle + solutions</button>
        <button class="bouton-second" id="r-imp-bilan">Bilan de mission</button>
      </p>

      <h3>💾 Progression</h3>
      <p class="aide-panneau">La mission dure toute l'année : pensez à exporter la progression
      de temps en temps, ou avant de changer de poste.</p>
      <p style="display:flex;gap:.5rem;flex-wrap:wrap;align-items:center">
        <button class="bouton-second" id="r-export">⬇️ Exporter</button>
        <label class="bouton-second" style="cursor:pointer">⬆️ Importer
          <input type="file" id="r-import" accept="application/json" hidden>
        </label>
        <button class="bouton-second" id="r-reset">♻️ Repartir de zéro</button>
      </p>

      <p style="margin-top:1.4rem">
        <button class="bouton-principal" id="r-ok">Enregistrer et fermer</button>
      </p>
    `;

    APP.modale(h, () => {
      const g = s => document.getElementById(s);
      g("r-taille").value  = String(r.tailleTexte);
      g("r-anim").checked  = !!r.animationsReduites;
      g("r-video").checked = !!r.videosActives;
      g("r-sonvideo").checked = !!r.sonVideo;
      g("r-images").checked = !!r.imagesActives;
      g("r-libre").checked  = !!r.ordreLibre;
      g("r-rec-active").checked = !!rec.active;

      g("r-ok").addEventListener("click", () => {
        const et = SAUVEGARDE.lire();
        Object.assign(et.profil, {
          commune: g("r-commune").value.trim() || et.profil.commune,
          departement: g("r-departement").value.trim(),
          numeroDepartement: g("r-numdep").value.trim(),
          region: g("r-region").value.trim(),
          pays: g("r-pays").value.trim(),
          continent: g("r-continent").value.trim()
        });
        Object.assign(et.reglages, {
          tailleTexte: parseFloat(g("r-taille").value),
          animationsReduites: g("r-anim").checked,
          videosActives: g("r-video").checked,
          sonVideo: g("r-sonvideo").checked,
          imagesActives: g("r-images").checked,
          ordreLibre: g("r-libre").checked
        });
        Object.assign(et.recompense, {
          active: g("r-rec-active").checked,
          titre: g("r-rec-titre").value.trim(),
          texte: g("r-rec-texte").value,
          media: g("r-rec-media").value.trim()
        });
        SAUVEGARDE.enregistrer();
        APP.appliquerReglages();
        APP.fermerModale();
        CARNET.dessinerHub();
        APP.message("Réglages enregistrés.", "reussite");
      });

      g("r-diag").addEventListener("click", async () => {
        const sortie = g("r-diag-sortie");
        sortie.innerHTML = "<p class='aide-panneau'>Recherche en cours…</p>";
        const bases = [...new Set(
          MISSION.sessions.flatMap(s => IMPRESSION.mediasAttendus(s))
            .concat(["mission-intro", "final-intro", "carte-corse", "recompense"])
        )];
        const lignes = await MEDIAS.diagnostic(bases);
        const trouves = lignes.filter(l => l.trouve);
        sortie.innerHTML =
          "<p><b>" + trouves.length + "</b> fichier(s) détecté(s) sur " + lignes.length +
          " emplacements possibles.</p><div class='enveloppe-tableau'><table class='donnees'>" +
          "<tr><th>Emplacement</th><th>Fichier trouvé</th></tr>" +
          lignes.map(l => "<tr><td>" + l.base + "</td><td>" +
            (l.trouve ? l.type + " : " + l.trouve : "—") + "</td></tr>").join("") +
          "</table></div>";
      });

      const seance = () => g("r-seance").value;
      g("r-imp-prep").addEventListener("click",    () => IMPRESSION.preparation(seance()));
      g("r-imp-eleve").addEventListener("click",   () => IMPRESSION.ficheEleve(seance(), false));
      g("r-imp-corrige").addEventListener("click", () => IMPRESSION.ficheEleve(seance(), true));
      g("r-imp-lecon").addEventListener("click",   () => {
        const s = MISSION.parId(seance());
        if(s) IMPRESSION.lecon(s.lecon);
      });
      g("r-imp-prog").addEventListener("click",  () => IMPRESSION.progression());
      g("r-imp-bilan").addEventListener("click", () => IMPRESSION.bilan());

      g("r-export").addEventListener("click", () => SAUVEGARDE.exporter());
      g("r-import").addEventListener("change", ev => {
        const f = ev.target.files[0];
        if(!f) return;
        SAUVEGARDE.importer(f)
          .then(() => { APP.fermerModale(); APP.appliquerReglages(); CARNET.dessinerHub();
                        APP.message("Progression importée.", "reussite"); })
          .catch(() => APP.message("Ce fichier n'est pas une sauvegarde valide.", "erreur"));
      });
      g("r-reset").addEventListener("click", () => {
        if(!confirm("Effacer toute la progression (séances, indices, piste finale) ?\n" +
                    "Les réglages et la récompense seront conservés.")) return;
        SAUVEGARDE.reinitialiser(true);
        APP.fermerModale();
        CARNET.dessinerHub();
        APP.afficherEcran("accueil");
        APP.message("Nouvelle mission prête.", "reussite");
      });
    });
  }

  function e(x){
    return String(x == null ? "" : x)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  return { ouvrir };
})();
