/* ============================================================
   RÉGLAGES ⚙️ — volet enseignant
   ------------------------------------------------------------
   Gardés sur l'appareil (localStorage « vml_reglages »).
   Niveau imposé (global) ou laissé au choix de chaque équipe (le
   tableau de bord peut aussi changer le grade d'une équipe), escales,
   durée de référence, indices, anti-tâtonnement, sons, voix,
   animations, lecture facilitée, images de référence, export/import
   de la partie, impressions (fiche de mission, leçons, corrigés,
   journal de bord).
   ============================================================ */
var VML = window.VML || (window.VML = {});

VML.REGLAGES_DEFAUT = {
  niveauImpose: null, indices: true, delaiIndiceMin: null, antiTatonnement: true,
  sons: true, voix: true, debitVoix: 1, animationsReduites: false, lecture: "normale",
  sansReference: false, dureeEscaleMin: 25, escales: [2]
};

(function(){
  const CLE = "vml_reglages";
  let R = null;
  const charger = () => {
    if(R) return R;
    R = Object.assign({}, VML.REGLAGES_DEFAUT);
    try{ Object.assign(R, JSON.parse(localStorage.getItem(CLE) || "{}")); }catch(e){}
    return R;
  };
  VML.reglage = function(cle){ const r = charger(); return cle ? r[cle] : r; };
  VML.changerReglage = function(cle, val){
    charger()[cle] = val;
    try{ localStorage.setItem(CLE, JSON.stringify(R)); }catch(e){}
    VML.appliquerReglages();
  };
  VML.appliquerReglages = function(){
    const r = charger();
    document.body.classList.toggle("anim-reduites", !!r.animationsReduites);
    document.body.dataset.lecture = r.lecture || "normale";
    if(!r.sons && VML.couperAmbiances) VML.couperAmbiances();
  };

  const ligne = (id, lib, html) => `<label class="reg-ligne" for="${id}"><span>${lib}</span>${html}</label>`;
  const caseACocher = (cle, lib) => ligne("reg-" + cle, lib, `<input type="checkbox" id="reg-${cle}" data-cle="${cle}" ${VML.reglage(cle) ? "checked" : ""}>`);

  VML.ouvrirReglages = function(){
    const el = document.getElementById("reglages");
    const r = VML.reglage();
    const grades = ((VML.D.enigmes || {}).niveaux || []);
    const es = (VML.D.enigmes || {}).escales || [];
    el.innerHTML = `
      <div class="reglages-boite" role="dialog" aria-modal="true" aria-label="Réglages">
        <div class="biblio-tete"><h3>⚙️ Réglages (enseignant)</h3><button class="fermer-reglages" aria-label="Fermer">✕</button></div>
        <div class="reglages-corps">
          <section><h4>🎚️ Grade</h4>
            ${ligne("reg-niveau", "Grade imposé à cet appareil", `<select id="reg-niveau"><option value="">au choix de l'équipe</option>${grades.map(g => `<option value="${g.id}" ${r.niveauImpose === g.id ? "selected" : ""}>${g.icone} ${g.nom} (${g.equivalent})</option>`).join("")}</select>`)}
            <p class="note">Les équivalences scolaires ne sont visibles qu'ici et dans le tableau de bord. Pour régler une équipe à distance : <code>prof.html</code>.</p>
          </section>
          <section><h4>🗺️ Escales</h4>
            ${es.map(x => ligne("reg-es-" + x.numero, `Escale ${x.numero} — ${x.titre}`, `<input type="checkbox" checked disabled>`)).join("")}
            <p class="note">Escale pilote seule pour l'instant ; les dix autres escales seront ajoutées après validation.</p>
          </section>
          <section><h4>⏱️ Temps et aides</h4>
            ${ligne("reg-duree", "Durée de référence d'une escale (bonus de rapidité)", `<input type="number" id="reg-duree" min="10" max="60" value="${r.dureeEscaleMin}"> min`)}
            ${caseACocher("indices", "Indices disponibles (−2 points chacun)")}
            ${ligne("reg-delai", "Proposer un indice après (minutes sans action)", `<input type="number" id="reg-delai" min="1" max="10" placeholder="auto" value="${r.delaiIndiceMin || ""}">`)}
            ${caseACocher("antiTatonnement", "Sas de sécurité (anti-tâtonnement)")}
          </section>
          <section><h4>🔊 Sons, voix, affichage</h4>
            ${caseACocher("sons", "Sons et ambiances")}
            ${caseACocher("voix", "Voix des personnages (les sous-titres restent)")}
            ${ligne("reg-debit", "Débit de la voix", `<input type="range" id="reg-debit" min="0.7" max="1.3" step="0.05" value="${r.debitVoix}">`)}
            ${caseACocher("animationsReduites", "Animations réduites")}
            ${ligne("reg-lecture", "Lecture facilitée", `<select id="reg-lecture"><option value="normale">normale</option><option value="atkinson" ${r.lecture === "atkinson" ? "selected" : ""}>police très lisible</option><option value="opendyslexic" ${r.lecture === "opendyslexic" ? "selected" : ""}>OpenDyslexic</option></select>`)}
            ${caseACocher("sansReference", "Ignorer les images de référence (décors dessinés)")}
          </section>
          <section><h4>🖨️ Impressions</h4>
            <div class="reg-boutons">
              <button class="btn-laiton petit" data-act="fiche">✍️ Fiche de mission</button>
              <button class="btn-laiton petit" data-act="lecons">📖 Leçons A4</button>
              <button class="btn-laiton petit" data-act="corriges">🔑 Corrigés (5 grades)</button>
              <button class="btn-laiton petit" data-act="journal">📔 Journal de bord</button>
            </div>
          </section>
          <section><h4>💾 Partie</h4>
            <div class="reg-boutons">
              <button class="btn-laiton petit" data-act="exporter">⬇️ Exporter la partie</button>
              <label class="btn-laiton petit">⬆️ Importer <input type="file" accept=".json" data-act="importer" hidden></label>
              <button class="btn-laiton petit gris" data-act="effacer">🗑️ Effacer la partie de cet appareil</button>
            </div>
            <p class="note">Vérification sans rien enregistrer : <code>?verif=1&amp;escale=2&amp;niveau=timonier&amp;enigme=3</code> · <a href="medias.html" target="_blank" rel="noopener">🖼️ Médias</a> · <a href="prof.html" target="_blank" rel="noopener">📊 Tableau de bord</a></p>
          </section>
        </div>
      </div>`;
    el.classList.add("ouverte");
    const fermer = () => el.classList.remove("ouverte");
    el.querySelector(".fermer-reglages").addEventListener("click", fermer);
    el.onclick = ev => { if(ev.target === el) fermer(); };
    el.querySelectorAll("[data-cle]").forEach(c => c.addEventListener("change", () => VML.changerReglage(c.dataset.cle, c.checked)));
    el.querySelector("#reg-niveau").addEventListener("change", ev => { VML.changerReglage("niveauImpose", ev.target.value || null); if(ev.target.value && VML.changerGrade) VML.changerGrade(ev.target.value); });
    el.querySelector("#reg-duree").addEventListener("change", ev => VML.changerReglage("dureeEscaleMin", Math.max(10, +ev.target.value || 25)));
    el.querySelector("#reg-delai").addEventListener("change", ev => VML.changerReglage("delaiIndiceMin", +ev.target.value || null));
    el.querySelector("#reg-debit").addEventListener("change", ev => VML.changerReglage("debitVoix", +ev.target.value));
    el.querySelector("#reg-lecture").addEventListener("change", ev => VML.changerReglage("lecture", ev.target.value));
    el.querySelectorAll("[data-act]").forEach(b => b.addEventListener(b.tagName === "INPUT" ? "change" : "click", ev => VML.actionReglage(b.dataset.act, ev)));
  };

  VML.actionReglage = function(act, ev){
    if(act === "fiche") VML.imprimer(VML.htmlFicheMission(), "Fiche de mission");
    if(act === "lecons") window.open("lecons-imprimables.html?niveau=" + (VML.ETAT.niveau || "matelot"), "_blank");
    if(act === "corriges") VML.imprimer(VML.htmlCorriges(), "Corrigés (enseignant)");
    if(act === "journal") VML.imprimer(VML.htmlJournal(), "Journal de bord");
    if(act === "exporter") VML.telecharger("nautilus-" + (VML.ETAT.equipe || "partie").replace(/[^\w-]+/g, "_") + ".json", JSON.stringify(VML.ETAT, null, 1));
    if(act === "importer"){
      const f = ev.target.files && ev.target.files[0]; if(!f) return;
      f.text().then(t => { try{ const d = JSON.parse(t); if(!d || !d.niveau) throw 0; localStorage.setItem(VML.CLE_PARTIE, JSON.stringify(d)); location.reload(); }catch(e){ alert("Fichier de partie illisible."); } });
    }
    if(act === "effacer" && confirm("Effacer la partie enregistrée sur cet appareil ?")){
      try{ localStorage.removeItem(VML.CLE_PARTIE); }catch(e){}
      location.href = location.pathname;
    }
  };

  VML.htmlFicheMission = function(){
    const E = VML.ETAT;
    const cases = Array.from({ length: 11 }, (_, i) => `<div class="fm-case"><div class="fm-num">Escale ${i + 1}</div><div class="fm-mot"></div></div>`).join("");
    return `<div class="fiche-mission">
      <h2>✍️ Fiche de mission — le journal du Nautilus</h2>
      <p>Équipe : <b>${VML.echapper(E.equipe || "………………………")}</b> &nbsp;·&nbsp; Grade : ${E.niveau ? VML.infoGrade(E.niveau).icone + " " + VML.infoGrade(E.niveau).nom : "…………"}</p>
      <p>À chaque escale, un fragment du journal de bord apparaît <b>une seule fois</b>. Recopiez-le aussitôt dans sa case : il faudra le retaper pour ouvrir le coffre du capitaine.</p>
      <div class="fm-grille">${cases}</div>
      <p class="fm-regles">Règles : 10 points tout juste du premier coup, 3 points après une erreur, −2 par indice. +2 « Bien documenté » si vous avez ouvert la bonne fiche de la Bibliothèque avant de réussir du premier coup.</p>
    </div>`;
  };

  VML.htmlCorriges = function(){
    const es = (VML.D.enigmes || {}).escales || [];
    return es.map(x => `<h2>Escale ${x.numero} — ${x.titre} · mot : ${x.mot}</h2>` + x.enigmes.map(e => `
      <div class="corrige"><h3>${e.ordre}. ${e.titre} <small>(${e.decor}, objet : ${e.objet_principal})</small></h3>
      ${VML.GRADES.map(g => `<p><b>${VML.infoGrade(g).icone} ${VML.infoGrade(g).nom} (${VML.infoGrade(g).equivalent})</b> — ${VML.solutionTexte(e, g).map(VML.echapper).join(" · ")}</p>`).join("")}
      </div>`).join("")).join("");
  };
})();
