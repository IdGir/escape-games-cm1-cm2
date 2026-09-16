/* MODULE 3 — Espace enseignant : analyse, remédiation, banques, réglages, pont. */

const Prof = {

  /* ============================================================ Paramètres
     Un seul onglet de menu regroupe : Classes & élèves, Réglages,
     Sécurité & données, Notes & Suivi. Chaque sous-écran écrit dans
     #param-corps au lieu de #contenu quand on est dans les Paramètres. */
  _cibleParam: null,
  _ongletParam: "classes",

  ONGLETS_PARAM: [
    ["classes",  "🏫", "Classes & élèves"],
    ["reglages", "⚙️", "Réglages"],
    ["securite", "🔐", "Sécurité & données"],
    ["pont",     "🔗", "Notes & Suivi"],
  ],

  /* Écrit un sous-écran soit en pleine page, soit dans l'onglet Paramètres. */
  _ecrire(titre, sous, html) {
    const zone = this._cibleParam ? $(this._cibleParam) : null;
    if (zone) {
      zone.innerHTML = `<div class="param-intro">${echapper(sous)}</div>` + html;
    } else {
      $("#contenu").innerHTML = page(titre, sous) + html;
    }
  },

  async parametres(onglet) {
    onglet = onglet || this._ongletParam || "classes";
    this._ongletParam = onglet;
    $("#contenu").innerHTML =
      page("Paramètres", "Vos classes, vos réglages, vos données — tout au même endroit.") +
      `<div class="onglets" id="ong-param">
        ${this.ONGLETS_PARAM.map(([cle, ico, lib]) => `
          <button class="onglet ${cle === onglet ? "actif" : ""}" data-ong="${cle}">
            <span class="onglet-ico">${ico}</span> ${lib}</button>`).join("")}
      </div>
      <div id="param-corps"></div>`;
    $$("#ong-param .onglet").forEach(b =>
      b.onclick = () => this.parametres(b.dataset.ong));
    this._cibleParam = "#param-corps";
    const vues = { classes: this.classes, reglages: this.reglages,
                   securite: this.securite, pont: this.pont };
    await vues[onglet].call(this);
  },

  /* --------------------------------------------- Bouton retour réutilisable */
  _retourBord(libelle = "← Retour au tableau de bord") {
    return `<button class="btn doux btn-retour" id="btn-retour-bord">${libelle}</button>`;
  },
  _brancherRetourBord() {
    const b = $("#btn-retour-bord");
    if (b) b.onclick = () => Nav.aller("bord");
  },

  /* ------------------------------------------------------------- Classeur */
  async classeur() {
    const dispo = await API.get("/api/classeur/disponible");
    if (!dispo.disponible) {
      $("#contenu").innerHTML = page("Classeur", "Fiches pédagogiques du classeur.") +
        `<div class="vide">Aucune fiche n'est installée pour l'instant.</div>`;
      return;
    }
    const fiches = await API.get("/api/classeur/liste");
    const domaines = [["orthographe", "🔤 Orthographe"], ["grammaire", "📝 Grammaire"],
      ["conjugaison", "⏳ Conjugaison"], ["vocabulaire", "📖 Vocabulaire"]];
    $("#contenu").innerHTML = page("Classeur",
      `${fiches.length} fiches CM1, celles utilisées en classe — consultables et imprimables.`) +
      `<div class="rangee" style="margin-bottom:14px;gap:8px">
        <button class="btn doux filtre-dom actif" data-dom="">Toutes</button>
        ${domaines.map(([d, l]) => `<button class="btn doux filtre-dom" data-dom="${d}">${l}</button>`).join("")}
      </div>
      <div id="grille-classeur" class="grille g3"></div>`;

    const dessiner = (dom) => {
      const liste = dom ? fiches.filter(f => f.domaine === dom) : fiches;
      $("#grille-classeur").innerHTML = liste.map(f => `
        <div class="carte carte-clic" data-id="${f.lecon_id}" style="cursor:pointer">
          <div style="font-size:13px;color:var(--texte-doux)">${echapper(f.sous_domaine)}</div>
          <div style="font-weight:700;margin-top:4px">${echapper(f.titre)}</div>
        </div>`).join("") ||
        `<div class="vide">Aucune fiche dans ce domaine.</div>`;
      $$(".carte-clic").forEach(c => c.onclick = () => this._voirFicheClasseur(c.dataset.id));
    };
    $$(".filtre-dom").forEach(b => b.onclick = () => {
      $$(".filtre-dom").forEach(x => x.classList.remove("actif"));
      b.classList.add("actif");
      dessiner(b.dataset.dom);
    });
    dessiner("");
  },

  // Même visionneuse agrandie que côté élève (voir noyau.js).
  _voirFicheClasseur(leconId) { return Classeur.ouvrir(leconId, { impression: true }); },


  async bord() {
    const classes = await API.get("/api/classes");
    $("#contenu").innerHTML =
      page("Tableau de bord", "Vue d'ensemble de la classe : écriture et lecture.") +
      `<div class="rangee barre-bord" style="margin-bottom:18px">
        <label class="champ" style="margin:0">Classe</label>
        <select id="sel-classe" style="width:240px">
          <option value="0">Toutes les classes</option>
          ${classes.map(c => `<option value="${c.id}">${echapper(c.nom)}</option>`).join("")}
        </select>
        <button class="btn pousse" id="btn-suggestions">
          🎯 À faire la prochaine fois</button>
        <button class="btn fantome" id="btn-mots-cherches">
          🔎 Mots cherchés</button>
        <button class="btn fantome" id="btn-impression">
          🖨️ Imprimer badges & leçons</button>
        <button class="btn fantome" id="btn-pilotage">
          📈 Pilotage fin</button>
      </div><div id="bord"></div>`;
    $("#sel-classe").onchange = () => this.dessinerBord($("#sel-classe").value);
    $("#btn-pilotage").onclick = () => Nav.aller("pilotage");
    $("#btn-mots-cherches").onclick = () => Nav.aller("motsCherches");
    $("#btn-suggestions").onclick = () => Nav.aller("devoirsSuggeres");
    $("#btn-impression").onclick = () => Nav.aller("impression");
    this.dessinerBord(0);
  },

  async dessinerBord(cid) {
    const d = await API.get("/api/prof/bord?classe_id=" + cid);
    if (!d.corrections && !d.lectures) {
      $("#bord").innerHTML = `<div class="vide">Aucune donnée pour l'instant.<br><br>
        Les résultats apparaîtront dès que les élèves auront utilisé les modules.</div>`;
      return;
    }
    const cats = Object.entries(d.par_categorie).sort((a, b) => b[1] - a[1])
      .map(([c, v]) => [libelleCat(c), v]);
    const coulCats = {};
    Object.keys(d.par_categorie).forEach(c => coulCats[libelleCat(c)] = couleurCat(c));

    // À la place de « Fluence par niveau de texte » (qui mesurait surtout le
    // texte choisi) : où se situent les ÉLÈVES par rapport au repère de leur
    // niveau de classe ? C'est ce qui déclenche une décision pédagogique.
    const p = d.fluence_profil || {};
    const bandes = [
      ["Au-delà", p.au_dela || 0, "var(--vert)"],
      ["Repère atteint", p.atteint || 0, "var(--cyan)"],
      ["Fragile", p.fragile || 0, "var(--orange)"],
      ["En difficulté", p.difficulte || 0, "var(--rouge)"],
    ];
    const coulFlu = {};
    bandes.forEach(([lib, , c]) => coulFlu[lib] = c);
    const carteLecture = d.fluence_nb_suivis
      ? `${Graph.barres(bandes.map(([l, v]) => [l, v]),
            { titre: `Lecture : situation des élèves (repère ${d.fluence_repere} mots/min)`,
              couleurs: coulFlu })}
         <div class="legende-bandes">
           <span><b>${d.fluence_en_progres}</b> élève(s) sur
             ${d.fluence_nb_progressions} progressent</span>
           <span>Gain moyen : <b style="color:${d.fluence_gain_moyen >= 0
             ? "var(--vert)" : "var(--rouge)"}">${d.fluence_gain_moyen >= 0 ? "+" : ""}${
             d.fluence_gain_moyen}</b> mots/min entre la 1<sup>re</sup> et la dernière lecture</span>
         </div>`
      : `<div class="carte-titre">Lecture : situation des élèves</div>
         <div class="vide">Aucune lecture chronométrée pour l'instant.</div>`;

    $("#bord").innerHTML = `
      <div class="stats">
        <div class="stat"><div class="v">${d.eleves}</div><div class="l">élèves</div></div>
        <div class="stat"><div class="v">${d.corrections}</div>
          <div class="l">séances d'écriture</div></div>
        <div class="stat"><div class="v" style="color:var(--vert)">${d.taux}%</div>
          <div class="l">erreurs corrigées</div></div>
        <div class="stat"><div class="v" style="color:var(--bleu)">${d.autonomie}%</div>
          <div class="l">corrigées sans aide</div></div>
        <div class="stat"><div class="v">${d.lectures}</div>
          <div class="l">lectures chronométrées</div></div>
        <div class="stat"><div class="v" style="color:var(--orange)">${d.mclm}</div>
          <div class="l">mots/min en moyenne</div></div>
      </div>
      <div class="grille g2">
        <div class="carte">${Graph.barres(cats,
          { titre: "Erreurs par catégorie", couleurs: coulCats })}</div>
        <div class="carte">${carteLecture}</div>
      </div>
      <div class="carte">
        <div class="carte-titre">Synthèse par élève</div>
        <div class="carte-sous">Cliquez sur une ligne pour ouvrir la fiche détaillée
          de l'élève.</div>
        <table><thead><tr>
          <th>Élève</th><th>Séances</th><th>% corrigé</th><th>% sans aide</th>
          <th>MCLM</th><th>Suivi</th></tr></thead>
        <tbody>${d.lignes.map(l => `<tr style="cursor:pointer" data-e="${l.id}">
          <td><b>${echapper(l.prenom)}</b>
            <span style="color:var(--texte-pale)"> ${echapper(l.classe)}</span></td>
          <td>${l.seances}</td><td>${l.taux}%</td><td>${l.autonomie}%</td>
          <td>${l.mclm || "—"}</td>
          <td>${l.besoins ? "⚠️".repeat(Math.min(3, l.besoins)) : "✔"}</td>
        </tr>`).join("")}</tbody></table>
      </div>`;
    $$("[data-e]").forEach(x => x.onclick = () => Nav.aller("eleve", +x.dataset.e));
  },

  /* ----------------------------------------------------------- Fiche élève */
  async fiche(eid) {
    const classes = await API.get("/api/classes");
    const eleves = classes.flatMap(c => c.eleves);
    $("#contenu").innerHTML =
      page("Fiche élève", "Le parcours d'un élève, séance après séance.") +
      `<div class="rangee" style="margin-bottom:18px">
        ${this._retourBord()}
        <label class="champ" style="margin:0 0 0 6px">Élève</label>
        <select id="sel-eleve" style="width:300px">
          <option value="">— choisis un élève —</option>
          ${eleves.map(e => `<option value="${e.id}" ${e.id === eid ? "selected" : ""}>
            ${echapper(e.prenom)} (${echapper(e.classe_nom)})</option>`).join("")}
        </select>
      </div><div id="fiche"></div>`;
    $("#sel-eleve").onchange = e => e.target.value && this.dessinerFiche(+e.target.value);
    this._brancherRetourBord();
    if (eid) this.dessinerFiche(eid);
    else $("#fiche").innerHTML = `<div class="vide">Choisis un élève ci-dessus.</div>`;
  },

  async dessinerFiche(eid) {
    const b = await API.get("/api/prof/eleve/" + eid);
    const cats = Object.entries(b.categories).sort((a, b2) => b2[1] - a[1])
      .map(([c, v]) => [libelleCat(c), v]);
    const coul = {};
    Object.keys(b.categories).forEach(c => coul[libelleCat(c)] = couleurCat(c));
    const prenom = b.eleve ? b.eleve.prenom : "";

    // Les deux modules sont deux compétences différentes : on ne les mélange
    // plus dans un même tableau de bord. Chacun a son bandeau et sa couleur.
    $("#fiche").innerHTML = `
      <section class="module-bloc module-ecrit">
        <div class="module-entete">
          <span class="module-ico">📝</span>
          <div><div class="module-nom">Je me corrige — écriture</div>
            <div class="module-sous">Ce que l'élève repère et répare dans un texte.</div></div>
          <span class="module-compte">${b.nb_corr} séance(s)</span>
        </div>
        ${b.nb_corr ? `
          <div class="stats">
            <div class="stat"><div class="v" style="color:var(--vert)">${b.taux_correction}%</div>
              <div class="l">erreurs corrigées</div></div>
            <div class="stat"><div class="v" style="color:var(--bleu)">${b.autonomie}%</div>
              <div class="l">corrigées sans aide</div></div>
            <div class="stat"><div class="v">${Object.values(b.categories)
              .reduce((s, v) => s + v, 0)}</div>
              <div class="l">erreurs sur les séances récentes</div></div>
          </div>
          <div class="grille g2">
            <div class="carte">${Graph.barres(cats,
              { titre: "Erreurs par catégorie (récentes)", couleurs: coul })}</div>
            <div class="carte">${Graph.courbe(b.progression,
              { titre: "% d'erreurs corrigées, séance après séance", unite: "%" })}</div>
          </div>`
        : `<div class="vide">Aucune séance d'écriture pour l'instant.</div>`}
      </section>

      <section class="module-bloc module-lecture">
        <div class="module-entete">
          <span class="module-ico">📖</span>
          <div><div class="module-nom">Je lis à voix haute — fluence</div>
            <div class="module-sous">Vitesse de lecture mesurée, comparée au repère
              de son niveau (${b.repere} mots/min).</div></div>
          <span class="module-compte">${b.nb_flu} lecture(s)</span>
        </div>
        ${b.nb_flu ? `
          <div class="stats">
            <div class="stat"><div class="v" style="color:var(--orange)">${b.mclm_dernier}</div>
              <div class="l">MCLM (dernière lecture)</div></div>
            <div class="stat"><div class="v" style="color:var(--vert)">${b.mclm_meilleur}</div>
              <div class="l">MCLM (record)</div></div>
            <div class="stat"><div class="v" style="color:var(--cyan)">${b.mclm_moyen}</div>
              <div class="l">MCLM (moyenne)</div></div>
          </div>
          <div class="carte">${Graph.courbe(b.fluence,
            { titre: "Progression en fluence (mots/min)", repere: b.repere,
              couleur: "var(--cyan)" })}</div>`
        : `<div class="vide">Aucune lecture chronométrée pour l'instant.</div>`}
      </section>

      ${b.nb_dictees ? `<section class="module-bloc module-dictee">
        <div class="module-entete">
          <span class="module-ico">✍️</span>
          <div><div class="module-nom">Ma dictée — orthographe sous dictée</div>
            <div class="module-sous">Dictée fabriquée à partir des mots que
              l'élève rate et de ceux qu'il cherche au dictionnaire.</div></div>
          <span class="module-compte">${b.nb_dictees} dictée(s)</span>
        </div>
        <div class="stats">
          <div class="stat"><div class="v" style="color:var(--ambre)">${
            b.dictee_score}%</div>
            <div class="l">mots justes en moyenne</div></div>
          <div class="stat"><div class="v">${b.dictee_orthographe}</div>
            <div class="l">bien entendus, mal écrits</div></div>
          <div class="stat"><div class="v">${b.dictee_ecoute}</div>
            <div class="l">mots non reconnus à l'oreille</div></div>
        </div>
        <div class="carte-sous" style="margin:0">${
          b.dictee_orthographe > b.dictee_ecoute
            ? "Le repérage auditif est solide : le travail porte sur la "
              + "mémorisation orthographique."
            : (b.dictee_ecoute > b.dictee_orthographe
               ? "Beaucoup de mots ne sont pas reconnus à l'oreille : "
                 + "vérifier l'audition et la discrimination des sons."
               : "Erreurs partagées entre écoute et orthographe.")}</div>
        ${b.dictee_courbe.length > 1 ? `<div class="carte">${Graph.courbe(
          b.dictee_courbe, { titre: "Scores de dictée (%)", unite: "%",
            couleur: "var(--ambre)" })}</div>` : ""}
      </section>` : ""}

      <section class="module-bloc module-besoins">
        <div class="module-entete">
          <span class="module-ico">🩺</span>
          <div><div class="module-nom">Besoins de suivi détectés</div>
            <div class="module-sous">Chaque besoin est livré avec sa fiche
              d'exercice ciblée, prête à imprimer.</div></div>
          <span class="module-compte">${b.besoins.length} besoin(s)</span>
        </div>
        <div class="rangee" style="margin-bottom:14px">
          <button class="btn fantome" id="voir-badges">
            🏆 Voir les réussites telles que l'élève les voit</button>
          <span style="font-size:12.5px;color:var(--texte-doux)">
            Pratique en entretien avec la famille.</span>
        </div>
        ${b.besoins.length
          ? b.besoins.map(x => this.alerte(x, { eleve_id: eid, prenom })).join("")
          : `<div class="vide" style="color:var(--vert)">
               ✅ Aucun besoin de suivi détecté pour l'instant.</div>`}
      </section>

      <div class="carte">
        <div class="carte-titre">🖨️ Autre fiche d'exercices</div>
        <div class="carte-sous">Pour travailler une catégorie de votre choix,
          même si elle n'a pas déclenché d'alerte.</div>
        <div class="rangee" style="margin-top:12px;align-items:flex-end">
          <div><label class="champ">Catégorie</label>
            <select id="fiche-cat">${Object.entries(Etat.ref.libelles || {})
              .map(([cle, lib]) => `<option value="${cle}">${echapper(lib)}</option>`)
              .join("")}</select></div>
          <div style="max-width:120px"><label class="champ">Nb de phrases</label>
            <input type="number" id="fiche-nb" min="3" max="12" value="6"></div>
          <button class="btn" id="fiche-go">Générer et imprimer</button>
        </div>
      </div>`;
    $("#fiche-go").onclick = () => this.genererFiche({
      eleve_id: eid, prenom, categorie: $("#fiche-cat").value,
      nombre: +$("#fiche-nb").value || 6 });
    if ($("#voir-badges")) $("#voir-badges").onclick = () => this.badgesEleve(eid);
    this._brancherFiches();
  },

  /* Le même écran de réussites que celui de l'élève, côté enseignant :
     utile pour valoriser un élève devant sa famille. */
  async badgesEleve(eid) {
    const b = await API.get(`/api/eleve/${eid}/bilan`);
    if (b.erreur) return;
    const obtenus = b.badges.filter(x => x.obtenu);
    modale(`
      <div class="carte-titre">🏆 Les réussites de ${echapper(b.prenom)}</div>
      <div class="carte-sous" style="margin-top:6px">${obtenus.length} réussite(s)
        sur ${b.badges.length}. C'est exactement ce que l'élève voit dans son
        onglet « Mon bilan ».</div>
      <div class="badges" style="margin-top:14px">
        ${b.badges.map(x => `<div class="badge ${x.obtenu ? "gagne" : "a-venir"}">
          <div class="badge-emo">${x.emoji}</div>
          <div class="badge-nom">${echapper(x.titre)}</div>
          <div class="badge-obj">${x.obtenu ? "✓ " : ""}${echapper(x.objectif)}</div>
          ${x.obtenu ? "" : `<div class="badge-reste">${x.valeur} / ${x.cible}</div>`}
        </div>`).join("")}
      </div>
      <div class="rangee" style="margin-top:18px">
        <button class="btn grand pousse" onclick="fermerModale()">Fermer</button>
      </div>`, true);
  },

  async genererFiche(corps) {
    toast("Préparation de la fiche…");
    await API.post("/api/prof/fiche", corps);
    toast("Fiche ouverte dans le navigateur pour l'impression " +
          "(sinon : dossier « exports »).", 4500);
  },

  /* Une alerte = un besoin + SA fiche d'exercice, dans le même cadre.
     opts.eleve_id / opts.prenom pour une fiche individuelle,
     opts.groupe pour une fiche d'atelier collectif. */
  alerte(b, opts = {}) {
    const forte = b.gravite === "forte";
    // Le type de fiche s'adapte au besoin : exercices écrits, lecture répétée
    // ou fiche de méthode de relecture.
    // Le type de fiche suit le DOMAINE, pas seulement la catégorie : un
    // besoin de fluence ou de dictée n'appelle pas une fiche d'exercices.
    const genre = b.domaine === "Lecture" ? "fluence"
      : (b.domaine === "Dictée" ? "dictee"
        : (b.categorie ? "exercices" : "methode"));
    const libelleBouton = { exercices: "🖨️ Fiche de remédiation",
      fluence: "🖨️ Fiche de lecture répétée",
      dictee: "🖨️ Fiche de mémorisation",
      methode: "🖨️ Fiche méthode de relecture" }[genre];
    const cible = opts.groupe
      ? `data-groupe="${echapper(opts.groupe)}"`
      : `data-eleve="${opts.eleve_id || ""}" data-prenom="${echapper(opts.prenom || "")}"`;

    return `<div class="besoin ${forte ? "forte" : ""}">
      <div class="besoin-haut">
        <span class="puce" style="background:${forte ? "var(--rouge)" : "var(--orange)"}">
          ${echapper(b.domaine)}</span>
        <span class="besoin-titre">${echapper(b.titre)}</span>
        ${forte ? `<span class="besoin-urgence">Prioritaire</span>` : ""}
      </div>
      <div class="besoin-corps">
        <div class="besoin-texte">
          <div class="besoin-remede">→ Remédiation : <b>${echapper(b.remediation)}</b>
            ${b.lecon_id ? `<span style="color:var(--texte-pale)"> (leçon ${
              echapper(b.lecon_id)})</span>` : ""}</div>
          ${(b.procedure || []).slice(0, 3).map(p =>
            `<div class="besoin-etape">• ${echapper(p)}</div>`).join("")}
        </div>
        <button class="btn fiche-besoin" data-genre="${genre}"
          data-cat="${echapper(b.categorie || "")}" ${cible}>${libelleBouton}</button>
      </div>
    </div>`;
  },

  /* Branche tous les boutons « fiche ciblée » présents à l'écran. */
  _brancherFiches() {
    $$(".fiche-besoin").forEach(btn => btn.onclick = () => {
      const d = btn.dataset;
      this.genererFiche({
        genre: d.genre, categorie: d.cat || null,
        eleve_id: d.eleve ? +d.eleve : null,
        prenom: d.groupe ? d.groupe : (d.prenom || ""),
        groupe: !!d.groupe, nombre: 6,
      });
    });
  },

  /* ----------------------------------------------------------- Remédiation */
  async remediation() {
    const d = await API.get("/api/prof/remediation");
    const groupes = Object.entries(d.groupes || {})
      .sort((a, b) => b[1].length - a[1].length);

    $("#contenu").innerHTML =
      page("Remédiation",
        "D'abord les groupes de besoin à constituer, ensuite le détail élève par élève.") +
      `<div class="rangee" style="margin-bottom:20px">
        <button class="btn fantome" id="exp">⬇ Exporter les besoins (CSV)</button>
        <span style="color:var(--texte-doux);font-size:12.5px">
          Les seuils sont réglables dans ⚙️ Paramètres → Réglages.</span>
      </div>` +
      (!d.besoins.length
        ? `<div class="vide" style="color:var(--vert)">
             ✅ Aucun besoin de suivi détecté pour l'instant.</div>`
        : `
        <section class="module-bloc module-groupes">
          <div class="module-entete">
            <span class="module-ico">👥</span>
            <div><div class="module-nom">Groupes de besoin</div>
              <div class="module-sous">Vos ateliers de la semaine, déjà constitués.
                Une fiche par groupe, prête à imprimer.</div></div>
            <span class="module-compte">${groupes.length} groupe(s)</span>
          </div>
          ${groupes.length ? `<div class="grille-groupes">
            ${groupes.map(([c, noms]) => `
              <div class="groupe-carte" style="--coul:${couleurCat(c)}">
                <div class="groupe-bandeau">
                  <span class="groupe-nom">${libelleCat(c)}</span>
                  <span class="groupe-effectif">${noms.length}</span>
                </div>
                <div class="groupe-corps">
                  <div class="groupe-eleves">${noms.map(n =>
                    `<span class="groupe-eleve">${echapper(n)}</span>`).join("")}</div>
                  <button class="btn fiche-besoin groupe-btn" data-genre="exercices"
                    data-cat="${echapper(c)}"
                    data-groupe="Groupe ${echapper(libelleCat(c))}">
                    🖨️ Fiche d'exercice ciblé pour ce groupe</button>
                </div>
              </div>`).join("")}
          </div>` : `<div class="vide">Aucun groupe : les besoins détectés sont
            individuels (méthode ou lecture).</div>`}
        </section>

        <section class="module-bloc module-besoins">
          <div class="module-entete">
            <span class="module-ico">🩺</span>
            <div><div class="module-nom">Besoins, élève par élève</div>
              <div class="module-sous">Les besoins prioritaires apparaissent en
                premier. Chaque besoin a sa fiche.</div></div>
            <span class="module-compte">${d.besoins.length} besoin(s)</span>
          </div>
          ${d.besoins.map(b => `
            <div class="besoin-ligne">
              <div class="besoin-eleve">
                <span class="besoin-prenom">${echapper(b.prenom)}</span>
                <span class="besoin-classe">${echapper(b.classe)}</span>
              </div>
              <div style="flex:1">${this.alerte(b,
                { eleve_id: b.eleve_id, prenom: b.prenom })}</div>
            </div>`).join("")}
        </section>`);
    this._brancherFiches();
    $("#exp").onclick = async () => {
      const r = await API.post("/api/export/besoins");
      toast("Fichier créé : " + r.chemin, 5000);
    };
  },

  /* ------------------------------------------------------- Banques de textes */
  async textes() {
    $("#contenu").innerHTML =
      page("Banques de textes", "Les textes proposés aux élèves dans les deux modules.") +
      `<div class="rangee" style="margin-bottom:16px">
        <button class="btn doux" id="t-corr">Textes à corriger</button>
        <button class="btn fantome" id="t-flu">Textes de fluence</button>
        <button class="btn fantome" id="t-dic">Dictées</button>
      </div><div id="banque"></div>`;
    const basculer = (actif, fn) => {
      ["t-corr", "t-flu", "t-dic"].forEach(x =>
        $("#" + x).className = x === actif ? "btn doux" : "btn fantome");
      fn.call(this);
    };
    $("#t-corr").onclick = () => basculer("t-corr", this.bCorr);
    $("#t-flu").onclick = () => basculer("t-flu", this.bFlu);
    $("#t-dic").onclick = () => basculer("t-dic", this.bDictee);
    this.bCorr();
  },

  /* ------------------------------------------------- Banque de dictées
     Même principe que les textes : l'IA en fabrique autant qu'on veut,
     l'enseignant valide, et cela alimente les dictées des élèves. */
  async bDictee(genre) {
    genre = genre || this._genreDictee || "mots";
    this._genreDictee = genre;
    const d = await API.get("/api/prof/banque-dictee?genre=" + genre);
    const libelles = { mots: "🔤 Mots", expressions: "🧩 Expressions",
                       phrases: "📜 Phrases" };
    const comptes = d.comptes || {};
    const total = g => Object.values(comptes[g] || {}).reduce((a, b) => a + b, 0);

    $("#banque").innerHTML = `<div class="carte">
      <div class="carte-titre">Banque de dictées</div>
      <div class="carte-sous">Ce que vous mettez ici est proposé aux élèves en
        priorité, avant les mots tirés de leurs propres erreurs. Les trois
        modes se travaillent séparément.</div>
      <div class="rangee" style="margin-bottom:14px">
        ${Object.entries(libelles).map(([g, lib]) => `
          <button class="btn ${g === genre ? "doux" : "fantome"} g-dic" data-g="${g}">
            ${lib} <span class="badge-nb">${total(g)}</span></button>`).join("")}
      </div>
      <div class="rangee" style="margin-bottom:14px">
        <button class="btn" id="bd-generer">✨ Fabriquer avec l'IA…</button>
        <button class="btn fantome" id="bd-ajouter">➕ Ajouter à la main</button>
      </div>
      <div class="compteur-banque">
        ${["1", "2", "3"].map(n =>
          `Niveau ${n} : <b>${(comptes[genre] || {})[n] || 0}</b>`).join(" · ")}
        ${total(genre) < 20 ? " — une banque confortable compte au moins "
          + "20 éléments par mode." : ""}
      </div>
      ${d.elements.length ? `<table><thead><tr>
        <th>Contenu</th><th>Niveau</th><th>Origine</th><th></th></tr></thead>
        <tbody>${d.elements.map(x => `<tr>
          <td>${echapper(x.contenu)}</td>
          <td><span class="puce doux">${x.niveau}</span></td>
          <td style="color:var(--texte-pale)">${echapper(x.source || "")}</td>
          <td><button class="mini" data-del-bd="${x.id}">🗑</button></td>
        </tr>`).join("")}</tbody></table>`
        : `<div class="vide">Rien encore dans ce mode.</div>`}
    </div>`;

    $$(".g-dic").forEach(b => b.onclick = () => this.bDictee(b.dataset.g));
    $("#bd-generer").onclick = () => this._genererDictees(genre);
    $("#bd-ajouter").onclick = () => this._ajouterDictees(genre);
    $$("[data-del-bd]").forEach(b => b.onclick = async () => {
      await API.del("/api/prof/banque-dictee/" + b.dataset.delBd);
      this.bDictee(genre);
    });
  },

  _genererDictees(genre) {
    const nom = { mots: "mots", expressions: "expressions",
                  phrases: "phrases" }[genre];
    modale(`
      <div class="carte-titre">✨ Fabriquer des ${nom} avec l'IA</div>
      <div class="carte-sous" style="margin-top:6px">${genre === "expressions"
        ? "L'IA reçoit une consigne stricte : des groupes nominaux formant une "
          + "unité de sens, ni phrases ni suites de mots au hasard."
        : (genre === "mots"
          ? "Uniquement des formes de base : ni pluriel, ni verbe conjugué."
          : "Des phrases courtes et complètes, avec un verbe conjugué.")}
        <b>Vous validez avant enregistrement.</b></div>
      <div class="grille g3" style="margin-top:10px">
        <div><label class="champ">Combien ?</label>
          <input type="number" id="bd-nb" min="5" max="60" value="20"></div>
        <div><label class="champ">Niveau</label>
          <select id="bd-niv">
            <option value="1">1 — facile</option>
            <option value="2" selected>2 — moyen</option>
            <option value="3">3 — difficile</option>
          </select></div>
        <div><label class="champ">Thème (facultatif)</label>
          <input type="text" id="bd-theme" placeholder="les animaux…"></div>
      </div>
      <div id="bd-info" style="margin-top:14px;font-size:13px;
        color:var(--texte-doux)"></div>
      <div class="rangee" style="margin-top:16px">
        <button class="btn doux" onclick="fermerModale()">Annuler</button>
        <button class="btn pousse" id="bd-go">Fabriquer</button>
      </div>`);
    $("#bd-go").onclick = async () => {
      $("#bd-go").disabled = true;
      $("#bd-info").innerHTML = `<span class="chargement"></span> Fabrication…`;
      const r = await API.post("/api/prof/banque-dictee/generer", {
        genre, nombre: +$("#bd-nb").value || 20,
        niveau: +$("#bd-niv").value || 2, theme: $("#bd-theme").value });
      if (!r.ok) {
        $("#bd-go").disabled = false;
        $("#bd-info").innerHTML =
          `<span style="color:var(--orange)">⚠ ${echapper(r.message)}</span>`;
        return;
      }
      this._validerDictees(genre, +$("#bd-niv").value || 2, r.propositions);
    };
  },

  _validerDictees(genre, niveau, propositions) {
    modale(`
      <div class="carte-titre">Relisez, puis cochez ce que vous gardez</div>
      <div class="carte-sous" style="margin-top:6px">${propositions.length}
        proposition(s). Les éléments décochés sont abandonnés.</div>
      <div class="props">${propositions.map((p, i) => `
        <label class="prop prop-ligne">
          <input type="checkbox" class="prop-case" data-i="${i}" checked>
          <span class="prop-contenu">${echapper(p)}</span>
        </label>`).join("")}</div>
      <div class="rangee" style="margin-top:16px">
        <button class="btn doux" onclick="fermerModale()">Tout abandonner</button>
        <button class="btn pousse" id="bd-save">💾 Ajouter à la banque</button>
      </div>`);
    $("#bd-save").onclick = async () => {
      const garder = $$(".prop-case").filter(x => x.checked)
        .map(x => propositions[+x.dataset.i]);
      if (!garder.length) { toast("Rien de coché."); return; }
      const r = await API.post("/api/prof/banque-dictee",
        { genre, niveau, elements: garder });
      fermerModale();
      toast(`${r.ajoutes} élément(s) ajouté(s).`, 4000);
      this.bDictee(genre);
    };
  },

  _ajouterDictees(genre) {
    modale(`
      <div class="carte-titre">➕ Ajouter à la main</div>
      <div class="carte-sous" style="margin-top:6px">Un élément par ligne.</div>
      <div class="grille g2" style="margin-top:8px">
        <div><label class="champ">Niveau</label>
          <select id="bdm-niv">
            <option value="1">1 — facile</option>
            <option value="2" selected>2 — moyen</option>
            <option value="3">3 — difficile</option>
          </select></div>
      </div>
      <textarea id="bdm-txt" rows="10" style="margin-top:10px"
        placeholder="${genre === "expressions" ? "des feuilles mortes\nun vieux château"
          : (genre === "phrases" ? "Le vent souffle dans les arbres."
             : "chapeau\néléphant")}"></textarea>
      <div class="rangee" style="margin-top:16px">
        <button class="btn doux" onclick="fermerModale()">Annuler</button>
        <button class="btn pousse" id="bdm-ok">💾 Enregistrer</button>
      </div>`);
    $("#bdm-ok").onclick = async () => {
      const elements = $("#bdm-txt").value.split("\n")
        .map(x => x.trim()).filter(Boolean);
      if (!elements.length) return;
      const r = await API.post("/api/prof/banque-dictee", {
        genre, niveau: +$("#bdm-niv").value || 2, elements, source: "enseignant" });
      fermerModale();
      toast(`${r.ajoutes} élément(s) ajouté(s).`, 4000);
      this.bDictee(genre);
    };
  },

  async bCorr() {
    const textes = await API.get("/api/textes/correction?tous=1");
    $("#banque").innerHTML = `<div class="carte">
      <div class="carte-titre">Textes à corriger (module élève)</div>
      <div class="carte-sous">Le corrigé est la pièce maîtresse : c'est lui qui permet
        de ne signaler QUE de vraies erreurs. Sans corrigé, l'application retombe sur
        des règles et peut souligner des mots pourtant justes.</div>
      <div class="rangee" style="margin-bottom:14px">
        <button class="btn" id="add">➕ Nouveau texte</button>
        <button class="btn fantome" id="gen">🎲 Générer un texte</button>
        <button class="btn fantome" id="gen-lot">⚡ Générer plusieurs textes…</button>
        <button class="btn fantome" id="fournis">📚 Ajouter les textes fournis (avec corrigés)</button>
      </div>
      <div class="compteur-banque">Banque actuelle : <b>${textes.length}</b> texte(s).
        ${textes.length < 15 ? `Une banque confortable compte au moins 15 à 20 textes —
        le bouton « Générer plusieurs textes » la remplit en une fois.` : ""}</div>
      <table><thead><tr><th>Titre</th><th>Niveau</th><th>Mots</th><th>Corrigé</th>
        <th></th></tr></thead>
      <tbody>${textes.map(t => `<tr>
        <td><b>${echapper(t.titre)}</b></td><td>${t.niveau}</td>
        <td>${t.contenu.split(/\s+/).length}</td>
        <td>${(t.corrige || "").trim()
          ? `<button class="mini" data-corr="${t.id}" style="color:var(--vert)">
               ✔ fourni — revoir</button>`
          : `<button class="mini" data-corr="${t.id}" style="color:var(--orange)">
               ⚠ ajouter le corrigé</button>`}</td>
        <td><button class="mini" data-del="${t.id}">🗑</button></td>
      </tr>`).join("")}</tbody></table></div>`;

    $$("[data-corr]").forEach(b => b.onclick = () =>
      this.editerCorrige(textes.find(t => t.id == b.dataset.corr)));
    $("#add").onclick = () => this.editeurTexte("correction");
    $("#gen").onclick = async () => {
      toast("Fabrication en cours…");
      const r = await API.post("/api/generer", {});
      // Le titre est proposé automatiquement, et reste modifiable.
      this.editeurTexte("correction", { contenu: r.texte, corrige: r.reference,
                                        titre: r.titre || "Texte généré" });
    };
    $("#gen-lot").onclick = () => this.lotCorrection();
    $("#fournis").onclick = async () => {
      const r = await API.post("/api/textes/correction/installer-fournis");
      toast(r.ajoutes ? `${r.ajoutes} texte(s) fourni(s) ajouté(s), avec leur corrigé.`
                      : "Les textes fournis sont déjà tous présents.", 4000);
      this.bCorr();
    };
    $$("[data-del]").forEach(b => b.onclick = () =>
      confirmer("Supprimer ce texte ?", "Cette action est définitive.", async () => {
        await API.del("/api/textes/correction/" + b.dataset.del);
        this.bCorr();
      }));
  },

  editerCorrige(t) {
    if (!t) return;
    modale(`
      <div class="carte-titre">Corrigé de « ${echapper(t.titre)} »</div>
      <div class="carte-sous" style="margin-top:6px">Le corrigé permet à
        l'application de ne signaler QUE de vraies erreurs. Il n'est jamais montré
        à l'élève.</div>
      <label class="champ">Texte de l'élève (avec les erreurs)</label>
      <textarea rows="4" readonly style="background:var(--fond-doux)">${echapper(t.contenu)}</textarea>
      <label class="champ" style="margin-top:12px">Le même texte, CORRIGÉ</label>
      <div style="font-size:12px;color:var(--texte-doux);margin-bottom:6px">
        Mêmes phrases, même ordre des mots : on ne répare QUE les erreurs.</div>
      <textarea id="c-corrige" rows="4">${echapper(t.corrige || "")}</textarea>
      <div class="rangee" style="margin-top:6px;gap:6px">
        <button class="mini" id="c-recopier">⧉ Recopier le texte</button>
        <button class="mini" id="c-gen">🤖 Générer le corrigé automatiquement</button>
      </div>
      <div id="c-info" style="font-size:12px;color:var(--texte-doux);margin-top:6px"></div>
      <div class="rangee" style="margin-top:18px">
        <button class="btn doux" onclick="fermerModale()">Annuler</button>
        <button class="btn pousse" id="c-ok">💾 Enregistrer le corrigé</button>
      </div>`);

    $("#c-recopier").onclick = () => { $("#c-corrige").value = t.contenu; };
    $("#c-gen").onclick = async () => {
      $("#c-info").innerHTML = `<span class="chargement"></span> Fabrication du corrigé…`;
      try {
        const r = await API.post("/api/textes/corrige-auto", { contenu: t.contenu });
        if (r.fiable && r.corrige) {
          $("#c-corrige").value = r.corrige;
          $("#c-info").innerHTML = `<span style="color:var(--vert)">✓ Proposé par ` +
            `${echapper(r.moteur)}. Relis et corrige si besoin.</span>`;
        } else {
          $("#c-info").innerHTML = `<span style="color:var(--orange)">⚠ ` +
            `${echapper(r.message)} Active une IA dans ⚙️ Réglages, ou écris le corrigé ` +
            `à la main.</span>`;
        }
      } catch (e) {
        $("#c-info").innerHTML = `<span style="color:var(--orange)">⚠ Génération impossible.</span>`;
      }
    };
    $("#c-ok").onclick = async () => {
      await API.post(`/api/textes/correction/${t.id}/corrige`,
                     { corrige: $("#c-corrige").value.trim() });
      fermerModale(); this.bCorr(); toast("Corrigé enregistré.");
    };
  },

  /* Création à la volée : on remplit la banque en une seule opération. */
  lotCorrection() {
    modale(`
      <div class="carte-titre">⚡ Générer plusieurs textes à corriger</div>
      <div class="carte-sous" style="margin-top:6px">Chaque texte est fabriqué
        avec son corrigé et un titre automatique. Vous pourrez tout modifier
        ensuite, texte par texte.</div>
      <div class="grille g3" style="margin-top:8px">
        <div><label class="champ">Combien de textes ?</label>
          <input type="number" id="lot-nb" min="1" max="30" value="10"></div>
        <div><label class="champ">Phrases par texte</label>
          <input type="number" id="lot-phrases" min="3" max="12" value="5"></div>
        <div><label class="champ">Niveau (1 à 5)</label>
          <input type="number" id="lot-niveau" min="1" max="5" value="2"></div>
      </div>
      <div id="lot-info" style="margin-top:14px;font-size:13px;
        color:var(--texte-doux);line-height:1.6"></div>
      <div class="rangee" style="margin-top:18px">
        <button class="btn doux" onclick="fermerModale()">Annuler</button>
        <button class="btn pousse" id="lot-ok">Lancer la fabrication</button>
      </div>`);
    $("#lot-ok").onclick = async () => {
      const nombre = +$("#lot-nb").value || 5;
      $("#lot-ok").disabled = true;
      $("#lot-info").innerHTML =
        `<span class="chargement"></span> Fabrication de ${nombre} texte(s)…
         Cela peut prendre un moment avec une IA en ligne.`;
      try {
        const r = await API.post("/api/generer-lot", {
          nombre, nb_phrases: +$("#lot-phrases").value || 5,
          niveau: +$("#lot-niveau").value || 2 });
        fermerModale();
        toast(`${r.ajoutes} texte(s) ajouté(s) à la banque.`, 4500);
        this.bCorr();
      } catch (e) {
        $("#lot-ok").disabled = false;
        $("#lot-info").innerHTML =
          `<span style="color:var(--orange)">⚠ Fabrication impossible.</span>`;
      }
    };
  },

  async bFlu() {
    const textes = await API.get("/api/textes/fluence?tous=1");
    $("#banque").innerHTML = `<div class="carte">
      <div class="carte-titre">Textes de fluence (5 niveaux)</div>
      <div class="carte-sous">Ces textes doivent être SANS erreur : ils sont lus à
        voix haute.</div>
      <div class="rangee" style="margin-bottom:14px">
        <button class="btn" id="add">➕ Nouveau texte</button>
        <button class="btn fantome" id="gen-flu">⚡ Générer plusieurs textes…</button>
        <button class="btn fantome" id="gen-litt">📖 Chercher des extraits littéraires…</button>
        <button class="btn fantome" id="reinst">↺ Réinstaller les textes fournis</button>
      </div>
      <div class="compteur-banque">Banque actuelle : <b>${textes.length}</b> texte(s).</div>
      <table><thead><tr><th>Titre</th><th>Niveau</th><th>Mots</th><th></th></tr></thead>
      <tbody>${textes.map(t => `<tr>
        <td><b>${echapper(t.titre)}</b></td>
        <td><span class="puce" style="background:${Etat.ref.niveaux_fluence[t.niveau].couleur}">
          ${t.niveau}</span></td>
        <td>${t.nb_mots}</td>
        <td><button class="mini" data-del="${t.id}">🗑</button></td>
      </tr>`).join("")}</tbody></table></div>`;
    $("#add").onclick = () => this.editeurTexte("fluence");
    $("#gen-flu").onclick = () => this.proposerFluence(false);
    $("#gen-litt").onclick = () => this.proposerFluence(true);
    $("#reinst").onclick = async () => {
      await API.post("/api/textes/reinstaller"); toast("Textes réinstallés."); this.bFlu();
    };
    $$("[data-del]").forEach(b => b.onclick = () =>
      confirmer("Supprimer ce texte ?", "Cette action est définitive.", async () => {
        await API.del("/api/textes/fluence/" + b.dataset.del); this.bFlu();
      }));
  },

  /* Propositions de textes de lecture : inventés, ou extraits d'œuvres pour
     enfants du domaine public. RIEN n'est enregistré sans votre validation. */
  proposerFluence(litteraire) {
    modale(`
      <div class="carte-titre">${litteraire
        ? "📖 Chercher des extraits littéraires pour enfants"
        : "⚡ Générer plusieurs textes de lecture"}</div>
      <div class="carte-sous" style="margin-top:6px">${litteraire
        ? "L'IA propose des extraits d'œuvres de littérature de jeunesse du " +
          "domaine public (La Fontaine, Perrault, Ségur, Malot, Verne, " +
          "Andersen…). Sans IA active, l'application puise dans sa propre " +
          "sélection d'extraits classiques."
        : "Des textes courts, sans erreur, destinés à la lecture à voix haute."}
        <b>Vous validez chaque texte avant qu'il n'entre dans la banque.</b></div>
      <div class="grille g2" style="margin-top:8px">
        <div><label class="champ">Combien de propositions ?</label>
          <input type="number" id="pf-nb" min="1" max="10" value="5"></div>
        <div><label class="champ">Niveau visé (1 à 5)</label>
          <input type="number" id="pf-niveau" min="1" max="5" value="2"></div>
      </div>
      <div id="pf-info" style="margin-top:14px;font-size:13px;color:var(--texte-doux)"></div>
      <div class="rangee" style="margin-top:18px">
        <button class="btn doux" onclick="fermerModale()">Annuler</button>
        <button class="btn pousse" id="pf-ok">Proposer</button>
      </div>`);
    $("#pf-ok").onclick = async () => {
      $("#pf-ok").disabled = true;
      $("#pf-info").innerHTML = `<span class="chargement"></span> Recherche en cours…`;
      try {
        const r = await API.post("/api/textes/fluence/proposer", {
          nombre: +$("#pf-nb").value || 5,
          niveau: +$("#pf-niveau").value || 2,
          litteraire: !!litteraire });
        this._validerPropositions(r);
      } catch (e) {
        $("#pf-ok").disabled = false;
        $("#pf-info").innerHTML =
          `<span style="color:var(--orange)">⚠ Recherche impossible.</span>`;
      }
    };
  },

  _validerPropositions(r) {
    const props = r.propositions || [];
    if (!props.length) {
      toast("Aucune proposition exploitable. Réessayez.", 4000);
      fermerModale();
      return;
    }
    modale(`
      <div class="carte-titre">Relisez, puis cochez ce que vous gardez</div>
      <div class="carte-sous" style="margin-top:6px">${echapper(r.message || "")}
        Les textes décochés sont simplement abandonnés.</div>
      <div class="props">${props.map((p, i) => `
        <div class="prop" data-i="${i}">
          <label class="prop-haut">
            <input type="checkbox" class="prop-case" checked>
            <input type="text" class="prop-titre" value="${echapper(p.titre)}">
            <span class="prop-meta">${p.nb_mots} mots · niv. ${p.niveau}</span>
          </label>
          ${p.source ? `<div class="prop-source">${echapper(p.source)}</div>` : ""}
          <textarea class="prop-texte" rows="5">${echapper(p.texte)}</textarea>
        </div>`).join("")}</div>
      <div class="rangee" style="margin-top:18px">
        <button class="btn doux" onclick="fermerModale()">Tout abandonner</button>
        <button class="btn pousse" id="pf-save">💾 Ajouter les textes cochés</button>
      </div>`);
    $("#pf-save").onclick = async () => {
      const garder = $$(".prop").filter(d => $(".prop-case", d).checked).map(d => ({
        titre: $(".prop-titre", d).value.trim(),
        contenu: $(".prop-texte", d).value.trim(),
        niveau: props[+d.dataset.i].niveau,
      })).filter(t => t.titre && t.contenu);
      if (!garder.length) { toast("Aucun texte coché."); return; }
      const rep = await API.post("/api/textes/fluence/lot", { textes: garder });
      fermerModale();
      toast(`${rep.ajoutes} texte(s) ajouté(s) à la banque de fluence.`, 4000);
      this.bFlu();
    };
  },

  editeurTexte(genre, pre = {}) {
    const corr = genre === "correction";
    modale(`
      <div class="carte-titre">Nouveau texte</div>
      <div style="margin-top:16px">
        <label class="champ">Titre</label>
        <input type="text" id="t-titre" value="${echapper(pre.titre || "")}">
        <div class="rangee" style="margin-top:6px">
          <button class="mini" id="t-titre-auto">✨ Proposer un titre</button>
          <span style="font-size:11.5px;color:var(--texte-pale)">
            Le titre proposé reste modifiable.</span>
        </div>
      </div>
      <div style="margin-top:12px">
        <label class="champ">Niveau de difficulté (1 à 5)</label>
        <input type="number" id="t-niv" min="1" max="5" value="2" style="width:100px">
      </div>
      <div style="margin-top:12px">
        <label class="champ">${corr
          ? "1. Texte AVEC les erreurs (celui que verra l'élève)"
          : "Texte à lire à voix haute (SANS erreur)"}</label>
        <textarea id="t-contenu" rows="${corr ? 5 : 12}"
          >${echapper(pre.contenu || "")}</textarea>
      </div>
      ${corr ? `<div style="margin-top:12px">
        <label class="champ">2. Le même texte, CORRIGÉ (indispensable)</label>
        <div style="font-size:12px;color:var(--texte-doux);margin-bottom:6px">
          Reprenez le texte ci-dessus et réparez uniquement les erreurs : mêmes
          phrases, même ordre des mots, ne reformulez pas. L'élève ne verra jamais
          ce corrigé.</div>
        <textarea id="t-corrige" rows="5">${echapper(pre.corrige || "")}</textarea>
        <div class="rangee" style="margin-top:6px;gap:6px">
          <button class="mini" id="recopier">⧉ Recopier le texte pour le corriger</button>
          <button class="mini" id="gen-corrige">🤖 Générer le corrigé automatiquement</button>
        </div>
        <div id="corr-info" style="font-size:12px;color:var(--texte-doux);margin-top:6px"></div>
      </div>` : ""}
      <div class="rangee" style="margin-top:20px">
        <button class="btn doux" onclick="fermerModale()">Annuler</button>
        <button class="btn pousse" id="t-ok">💾 Enregistrer</button>
      </div>`);

    $("#t-titre-auto").onclick = async () => {
      const source = (corr && $("#t-corrige") && $("#t-corrige").value.trim())
        || $("#t-contenu").value.trim();
      if (!source) { toast("Écris d'abord le texte."); return; }
      const r = await API.post("/api/textes/titre-auto", { contenu: source });
      if (r.titre) { $("#t-titre").value = r.titre; toast("Titre proposé."); }
    };

    if (corr) {
      $("#recopier").onclick = () => { $("#t-corrige").value = $("#t-contenu").value; };
      $("#gen-corrige").onclick = async () => {
        const contenu = $("#t-contenu").value.trim();
        if (!contenu) { toast("Écris d'abord le texte à corriger."); return; }
        $("#corr-info").innerHTML = `<span class="chargement"></span> Fabrication du corrigé…`;
        try {
          const r = await API.post("/api/textes/corrige-auto", { contenu });
          if (r.fiable && r.corrige) {
            $("#t-corrige").value = r.corrige;
            $("#corr-info").innerHTML =
              `<span style="color:var(--vert)">✓ Corrigé proposé par ${echapper(r.moteur)}. ` +
              `Relis-le et corrige si besoin avant d'enregistrer.</span>`;
          } else {
            $("#corr-info").innerHTML =
              `<span style="color:var(--orange)">⚠ ${echapper(r.message)}<br>` +
              `Sans IA active, le corrigé automatique n'est pas fiable : ` +
              `active une IA dans ⚙️ Réglages, ou écris le corrigé à la main.</span>`;
          }
        } catch (e) {
          $("#corr-info").innerHTML =
            `<span style="color:var(--orange)">⚠ Génération impossible.</span>`;
        }
      };
    }

    $("#t-ok").onclick = async () => {
      const titre = $("#t-titre").value.trim();
      const contenu = $("#t-contenu").value.trim();
      const niveau = +$("#t-niv").value;
      if (!titre || !contenu) { toast("Le titre et le texte sont obligatoires."); return; }
      if (!corr) {
        await API.post("/api/textes/fluence", { titre, contenu, niveau });
        fermerModale(); this.bFlu(); toast("Texte enregistré."); return;
      }
      const corrige = $("#t-corrige").value.trim();
      const enregistrer = async () => {
        await API.post("/api/textes/correction", { titre, contenu, niveau, corrige });
        fermerModale(); this.bCorr(); toast("Texte enregistré.");
      };
      if (!corrige) {
        confirmer("Corrigé manquant",
          "Sans corrigé, l'application devra deviner les erreurs avec des règles : " +
          "elle risque de souligner des mots pourtant justes, que l'élève ne pourra " +
          "pas corriger.<br><br>Enregistrer quand même ?",
          enregistrer, "Enregistrer quand même");
        return;
      }
      const a = contenu.split(/\s+/).length, b = corrige.split(/\s+/).length;
      if (Math.abs(a - b) > Math.max(3, a * 0.3)) {
        toast("Le corrigé n'a pas la même longueur que le texte : il doit être le " +
              "MÊME texte, seulement réparé.", 5000);
        return;
      }
      enregistrer();
    };
  },

  /* ------------------------------------------------------- Classes & élèves */
  async classes() {
    const classes = await API.get("/api/classes");
    this._ecrire("Classes & élèves", "Créez vos classes, importez vos listes.",
      `<div class="rangee" style="margin-bottom:16px">
        <button class="btn" id="add-c">➕ Nouvelle classe</button>
        <button class="btn fantome" id="imp">📥 Importer un CSV</button>
        <button class="btn doux pousse" id="purge">🧹 Effacer les données de démonstration</button>
      </div>
      ${classes.map(c => `<div class="carte">
        <div class="rangee">
          <div><div class="carte-titre">${echapper(c.nom)}
            <span class="puce doux">${echapper(c.niveau)}</span></div>
            <div class="carte-sous" style="margin:0">${c.eleves.length} élève(s)</div></div>
          <button class="btn fantome pousse" data-add-e="${c.id}">➕ Élève</button>
          <button class="mini" data-del-c="${c.id}">🗑 Supprimer la classe</button>
        </div>
        <div class="rangee" style="margin-top:12px">
          ${c.eleves.map(e => `<span class="puce doux" style="padding:6px 10px">
            ${echapper(e.prenom)} ${echapper(e.nom || "")}
            <b data-del-e="${e.id}" style="cursor:pointer;margin-left:5px">×</b>
          </span>`).join("") || `<span style="color:var(--texte-pale)">Aucun élève.</span>`}
        </div>
      </div>`).join("") || `<div class="vide">Aucune classe. Commence par en créer une.</div>`}
      <div style="color:var(--texte-doux);font-size:12.5px">
        Format du CSV : prénom ; nom ; classe — une ligne par élève. Les classes
        absentes sont créées, les doublons ignorés.</div>`);

    $("#add-c").onclick = () => modale(`
      <div class="carte-titre">Nouvelle classe</div>
      <div style="margin-top:14px"><label class="champ">Nom</label>
        <input type="text" id="c-nom" placeholder="CM2 Dupont"></div>
      <div style="margin-top:12px"><label class="champ">Niveau</label>
        <select id="c-niv">${Object.keys(Etat.ref.reperes_mclm)
          .map(n => `<option ${n === "CM1" ? "selected" : ""}>${n}</option>`).join("")}
        </select></div>
      <div class="rangee" style="margin-top:18px">
        <button class="btn doux" onclick="fermerModale()">Annuler</button>
        <button class="btn pousse" id="c-ok">Créer</button></div>`);

    document.addEventListener("click", async e => {
      if (e.target.id === "c-ok") {
        const nom = $("#c-nom").value.trim();
        if (!nom) return;
        await API.post("/api/classes", { nom, niveau: $("#c-niv").value });
        fermerModale(); this.classes();
      }
    }, { once: true });

    $$("[data-add-e]").forEach(b => b.onclick = () => {
      modale(`<div class="carte-titre">Nouvel élève</div>
        <div style="margin-top:14px"><label class="champ">Prénom</label>
          <input type="text" id="e-prenom"></div>
        <div style="margin-top:12px"><label class="champ">Nom (facultatif)</label>
          <input type="text" id="e-nom"></div>
        <div class="rangee" style="margin-top:18px">
          <button class="btn doux" onclick="fermerModale()">Annuler</button>
          <button class="btn pousse" id="e-ok">Ajouter</button></div>`);
      $("#e-ok").onclick = async () => {
        const p = $("#e-prenom").value.trim();
        if (!p) return;
        await API.post("/api/eleves", { prenom: p, nom: $("#e-nom").value.trim(),
                                        classe_id: +b.dataset.addE });
        fermerModale(); this.classes();
      };
    });

    $$("[data-del-c]").forEach(b => b.onclick = () =>
      confirmer("Supprimer cette classe ?",
        "Tous ses élèves ET leurs résultats seront supprimés.", async () => {
          await API.del("/api/classes/" + b.dataset.delC); this.classes();
        }));
    $$("[data-del-e]").forEach(b => b.onclick = () =>
      confirmer("Supprimer cet élève ?", "Ses résultats seront supprimés.", async () => {
        await API.del("/api/eleves/" + b.dataset.delE); this.classes();
      }));

    $("#imp").onclick = () => {
      modale(`<div class="carte-titre">Importer une liste d'élèves</div>
        <div class="carte-sous" style="margin-top:8px">Colle ici le contenu de ton
          fichier CSV (prénom ; nom ; classe).</div>
        <textarea id="csv" rows="10" placeholder="Lina;Martin;CM2 Dupont"></textarea>
        <div class="rangee" style="margin-top:16px">
          <button class="btn doux" onclick="fermerModale()">Annuler</button>
          <button class="btn pousse" id="imp-ok">Importer</button></div>`);
      $("#imp-ok").onclick = async () => {
        const r = await API.post("/api/eleves/import", { csv: $("#csv").value });
        fermerModale(); this.classes();
        toast(`${r.ajoutes} élève(s) ajouté(s), ${r.ignores} doublon(s) ignoré(s).`, 4000);
      };
    };

    $("#purge").onclick = () => confirmer("Tout effacer ?",
      "Cela supprime <b>toutes</b> les classes, <b>tous</b> les élèves et " +
      "<b>tous</b> leurs résultats.", async () => {
        await API.post("/api/donnees/purger"); this.classes();
      });
  },

  /* ---------------------------------------------------------------- Réglages */
  THEMES: [
    "La vie quotidienne à l'école", "Les animaux", "La nature et les saisons",
    "Le sport", "Les vacances et les voyages", "La famille et la maison",
    "Les métiers", "L'alimentation et la cuisine", "Les contes et l'imaginaire",
    "L'espace et les sciences", "L'histoire et le patrimoine",
    "L'environnement et la planète",
  ],

  async reglages() {
    const { valeurs: v } = await API.get("/api/reglages");
    const case_ = (cle, lib) => `<label class="inter">
      <input type="checkbox" data-r="${cle}" ${v[cle] ? "checked" : ""}> ${lib}</label>`;
    const champ = (cle, lib, type = "text", aide = "") => `
      <div><label class="champ">${lib}</label>
        <input type="${type}" data-r="${cle}" value="${echapper(v[cle])}">
        ${aide ? `<div style="font-size:11.5px;color:var(--texte-pale);margin-top:4px">
          ${aide}</div>` : ""}</div>`;

    this._ecrire("Réglages", "Apparence, repérage, moteur IA, seuils d'alerte.",
      `<div class="carte">
        <div class="carte-titre">🎨 Apparence</div>
        <div class="carte-sous">S'applique à toute l'application, écrans élèves compris.</div>
        <div class="rangee">
          <button class="btn ${Etat.ref.theme_sombre ? "fantome" : ""}" id="th-clair">
            ☀ Clair</button>
          <button class="btn ${Etat.ref.theme_sombre ? "" : "fantome"}" id="th-sombre">
            🌙 Sombre</button>
        </div>
      </div>

      <div class="carte">
        <div class="carte-titre">🔎 Repérage des erreurs</div>
        <div class="carte-sous">Quand le corrigé d'un texte est connu, seules les
          VRAIES erreurs sont signalées : un mot correct n'est jamais souligné.
          Pour un texte écrit par l'élève, l'application le fait corriger, puis compare.
          À défaut, elle applique des règles et peut proposer des « mots à vérifier ».</div>
        ${case_("vigilance_active",
          "Proposer des « mots à vérifier » (ne comptent jamais dans le score)")}
      </div>

      <div class="carte">
        <div class="carte-titre">🔒 Espace élève : ce que chacun peut ouvrir</div>
        <div class="carte-sous">Quand l'espace élève est verrouillé, l'élève ne
          peut plus revenir de lui-même côté enseignant : il faut votre code.
          Il ne voit que ses propres résultats, et seules les activités cochées
          lui sont proposées.</div>
        <div id="zone-acces"><span class="chargement"></span></div>
      </div>

      <div class="carte">
        <div class="carte-titre">📝 Sources de texte autorisées pour les élèves</div>
        ${case_("source_saisie_libre", "L'élève peut écrire ou coller son propre texte")}
        ${case_("source_texte_impose", "L'élève peut choisir un texte de la banque")}
        ${case_("source_generation_ia", "L'élève peut faire générer un texte surprise")}
      </div>

      <div class="carte">
        <div class="carte-titre">🤖 Moteur IA (correction et génération)</div>
        <div class="carte-sous">Si l'IA est absente ou en panne, l'application bascule
          seule sur ses règles hors ligne. L'élève n'est jamais bloqué.</div>
        ${case_("ia_active", "Utiliser une IA (sinon : règles hors ligne)")}
        <div class="grille g2" style="margin-top:12px">
          <div><label class="champ">Moteur</label>
            <select data-r="ia_moteur">
              <option value="deepseek" ${v.ia_moteur === "deepseek" ? "selected" : ""}>
                DeepSeek (cloud)</option>
              <option value="ollama" ${v.ia_moteur === "ollama" ? "selected" : ""}>
                Ollama (local, aucune donnée ne sort)</option>
              <option value="api" ${v.ia_moteur === "api" ? "selected" : ""}>
                Autre API (OpenAI, Mistral, Groq, OpenRouter…)</option>
            </select></div>
          ${champ("ia_nb_phrases", "Phrases par défaut (texte généré)", "number")}
        </div>

        <div class="bloc-moteur" data-moteur="deepseek" style="margin-top:6px">
          <div class="grille g2">
            ${champ("ia_cle_api", "Clé API DeepSeek", "password",
                    "à copier depuis platform.deepseek.com")}
          </div>
        </div>

        <div class="bloc-moteur" data-moteur="ollama" style="margin-top:6px">
          <div class="grille g2">
            ${champ("ia_url_ollama", "Adresse d'Ollama")}
            ${champ("ia_modele_ollama", "Modèle Ollama")}
          </div>
        </div>

        <div class="bloc-moteur" data-moteur="api" style="margin-top:6px">
          <div class="carte-sous" style="margin-bottom:8px">
            Pour brancher n'importe quel service compatible OpenAI. Renseigne
            l'adresse (souvent terminée par <code>/v1</code>), ta clé et le nom
            du modèle. Exemples : Google AI Studio (Gemini), OpenAI, Mistral,
            Groq, OpenRouter, ou un serveur installé sur ton ordinateur.</div>
          <div class="carte-sous" style="margin-bottom:8px">
            <b>Pas encore de clé ?</b> Celle de <b>Google AI Studio (Gemini)</b>
            est gratuite et s'obtient en deux minutes sur
            <code>aistudio.google.com/apikey</code>, sans carte bancaire.
            Cliquez sur son réglage tout prêt ci-dessous.</div>
          <div class="rangee" style="margin-bottom:10px">
            <span class="champ" style="margin:0">Réglages tout prêts</span>
            <span id="presets-m1"></span>
          </div>
          <div id="m1-aide" class="carte-sous" style="margin-bottom:10px"></div>
          <div class="grille g2">
            ${champ("ia_nom_api", "Nom affiché (au choix)")}
            ${champ("ia_modele_api", "Nom du modèle", "text",
                    "ex. gemini-3-flash, gpt-4o-mini, mistral-small-latest…")}
            ${champ("ia_url_api", "Adresse de l'API", "text",
                    "ex. https://generativelanguage.googleapis.com/v1beta/openai")}
            ${champ("ia_cle_api_perso", "Clé d'accès (API key)", "password")}
          </div>
        </div>

        <div style="margin-top:14px">
          <label class="champ">Thèmes des textes générés</label>
          <div class="carte-sous" style="margin-bottom:8px">Cochez-en autant que
            vous voulez : la génération en lot les fait tourner, ce qui évite
            dix textes semblables avec le même titre.</div>
          <div class="rangee" style="margin-bottom:10px">
            <button class="mini" id="th-tout">☑ Tout cocher</button>
            <button class="mini" id="th-rien">☐ Tout décocher</button>
            <span id="th-compte" style="font-size:12.5px;color:var(--texte-doux)"></span>
          </div>
          <div class="grille-themes">
            ${this.THEMES.map(t => `
              <label class="theme-choix">
                <input type="checkbox" class="coche-theme" value="${echapper(t)}"
                  ${(v.ia_themes || []).includes(t) ? "checked" : ""}>
                <span>${echapper(t)}</span>
              </label>`).join("")}
          </div>
          <label class="champ" style="margin-top:12px">Vos propres thèmes
            (un par ligne, facultatif)</label>
          <textarea id="themes-libres" rows="3"
            placeholder="Le cirque&#10;Les métiers d'autrefois">${
            echapper(((v.ia_themes || []).filter(t => !this.THEMES.includes(t)))
              .join("\n"))}</textarea>
        </div>
        <button class="btn fantome" id="test-ia" style="margin-top:14px">
          🔌 Tester le moteur</button>
        <div id="res-ia" style="margin-top:10px;font-size:13px;white-space:pre-wrap"></div>
      </div>

      <div class="carte">
        <div class="carte-titre">🤝 Un second moteur IA (facultatif)</div>
        <div class="carte-sous">Un moteur peut être meilleur pour corriger et
          l'autre pour rédiger. Vous pouvez en régler un deuxième, puis dire
          lequel s'occupe de quoi. Si le second n'est pas réglé, tout passe par
          le principal — rien ne casse.</div>
        <div id="zone-moteur2"><span class="chargement"></span></div>
      </div>

      <div class="carte">
        <div class="carte-titre">🧭 Aide guidée de l'élève</div>
        <div class="carte-sous">Quand l'élève clique sur une erreur, l'application lui
          propose des questions pour l'orienter, puis — s'il le demande — un indice
          plus direct. L'aide utilisée est comptée dans son bilan.</div>
        ${case_("aide_ia_active",
          "Laisser l'IA formuler des questions et indices sur mesure (si une IA est active)")}
        ${case_("aide_penalise_score",
          "Tenir compte de l'aide utilisée dans le score d'autonomie")}
      </div>

      <div class="carte">
        <div class="carte-titre">🎙️ Lecture en autonomie (facultatif)</div>
        <div class="carte-sous">Quand cette fonction est active, l'élève peut
          faire sa lecture seul : l'ordinateur enregistre sa voix, la fait
          transcrire, compare au texte et compte les mots. Vous n'avez plus
          qu'à vérifier.</div>

        <div class="avert-rgpd">
          <b>À lire avant d'activer.</b>
          <ul>
            <li><b>La voix de l'élève quitte l'ordinateur.</b> Elle est envoyée
              au service que vous réglez ci-dessous, le temps de la
              transcription. L'application ne conserve aucun enregistrement.</li>
            <li>Prévenez les familles et votre direction : la voix est une
              donnée personnelle. Avec Albert (DINUM), le traitement a lieu en
              France, sur un service de l'État.</li>
            <li><b>Le comptage est optimiste.</b> La machine repère les mots
              sautés ou remplacés, mais pas les hésitations ni les syllabes
              reprises : une lecture hachée sera transcrite comme correcte.
              Le résultat est présenté à l'élève comme une proposition à
              vérifier.</li>
            <li>Un <b>micro-casque</b> est vivement conseillé : à plusieurs
              dans une salle, la transcription se dégrade beaucoup.</li>
          </ul>
        </div>

        ${case_("stt_active", "Activer la lecture en autonomie")}
        <div class="grille g2" style="margin-top:12px">
          ${champ("stt_nom", "Nom du service")}
          ${champ("stt_modele", "Modèle de transcription", "text",
                  "ex. whisper-large-v3-turbo")}
          ${champ("stt_url", "Adresse de l'API", "text",
                  "Albert : https://albert.api.etalab.gouv.fr/v1 — vous pouvez "
                  + "aussi coller l'adresse complète terminée par "
                  + "/audio/transcriptions, les deux formes sont acceptées")}
          ${champ("stt_cle", "Clé d'accès", "password",
                  "Albert : demande auprès de la DINUM (agents publics)")}
        </div>
        <div class="rangee" style="margin-top:14px">
          <button class="btn fantome" id="test-stt">🔌 Tester le service</button>
          <button class="btn fantome" id="modeles-stt">📋 Voir les modèles disponibles</button>
        </div>
        <div id="res-stt" style="font-size:13px;margin-top:10px"></div>
        <div class="astuce-test">Le test utilise ce qui est écrit ci-dessus :
          pas besoin d'enregistrer avant d'essayer. Sur du silence, une
          transcription vide est le résultat normal — cela prouve que le
          service répond.</div>
      </div>

      <div class="carte">
        <div class="carte-titre">📖 Fluence de lecture</div>
        ${case_("fluence_afficher_nb_mots", "Afficher le nombre de mots aux élèves")}
        <div style="max-width:280px;margin-top:12px">
          <label class="champ">Niveau de classe de référence (repère MCLM)</label>
          <select data-r="fluence_niveau_classe">
            ${Object.entries(Etat.ref.reperes_mclm).map(([n, r]) =>
              `<option value="${n}" ${v.fluence_niveau_classe === n ? "selected" : ""}>
                ${n} — ${r} mots/min</option>`).join("")}
          </select></div>
      </div>

      <div class="carte">
        <div class="carte-titre">🎯 Évaluation du travail de correction</div>
        <div class="carte-sous">Ces critères décident du message de réussite affiché à
          l'élève à la fin de sa correction, et de l'objectif d'autonomie visé.</div>
        <div class="grille g2" style="margin-top:12px">
          ${champ("eval_seuil_reussi", "Travail « réussi » à partir de (% corrigé)", "number")}
          ${champ("eval_seuil_excellent", "Travail « excellent » à partir de (% corrigé)", "number")}
          ${champ("eval_objectif_autonomie", "Objectif d'autonomie (% corrigé sans aide)", "number")}
        </div>
        ${case_("eval_bonus_sans_aide",
          "Féliciter l'élève quand il atteint l'objectif d'autonomie")}
      </div>

      <div class="carte">
        <div class="carte-titre">🩺 Seuils de détection des besoins de suivi</div>
        <div class="grille g2" style="margin-top:12px">
          ${champ("seuil_nb_seances", "Séances récentes prises en compte", "number")}
          ${champ("seuil_categorie_alerte", "Erreurs d'une même catégorie → alerte", "number")}
          ${champ("seuil_autonomie_faible", "Autonomie minimale attendue (%)", "number")}
          ${champ("seuil_mclm_ecart", "Écart maximal au repère MCLM (%)", "number")}
        </div>
      </div>

      <div class="rangee">
        <button class="btn grand" id="sauver">💾 Enregistrer les réglages</button>
      </div>`);

    $("#th-clair").onclick = () => App.theme(false);
    $("#th-sombre").onclick = () => App.theme(true);
    this._blocAcces();
    this._blocMoteur2(v);

    // N'afficher que les réglages du moteur choisi (plus clair pour l'enseignant).
    const selMoteur = $('[data-r="ia_moteur"]');
    const majBlocs = () => $$(".bloc-moteur").forEach(b =>
      b.style.display = b.dataset.moteur === selMoteur.value ? "" : "none");
    selMoteur.onchange = majBlocs;
    majBlocs();

    // Thèmes : autant de cases cochées qu'on veut, plus des thèmes libres.
    const compterThemes = () => {
      const n = $$(".coche-theme").filter(x => x.checked).length
        + $("#themes-libres").value.split("\n").filter(x => x.trim()).length;
      $("#th-compte").textContent = `${n} thème(s) retenu(s)`;
    };
    $$(".coche-theme").forEach(x => x.onchange = compterThemes);
    $("#themes-libres").oninput = compterThemes;
    $("#th-tout").onclick = () => {
      $$(".coche-theme").forEach(x => x.checked = true); compterThemes();
    };
    $("#th-rien").onclick = () => {
      $$(".coche-theme").forEach(x => x.checked = false); compterThemes();
    };
    compterThemes();

    $("#sauver").onclick = async () => {
      const d = {};
      $$("[data-r]").forEach(x => {
        d[x.dataset.r] = x.type === "checkbox" ? x.checked : x.value;
      });
      const themes = $$(".coche-theme").filter(x => x.checked).map(x => x.value)
        .concat($("#themes-libres").value.split("\n")
          .map(x => x.trim()).filter(Boolean));
      d.ia_themes = themes.length ? themes : ["La vie quotidienne à l'école"];
      d.ia_theme = d.ia_themes[0];        // conservé pour compatibilité
      // Second moteur et répartition des tâches.
      if ($("#m2-choix")) {
        d.ia_moteur_secondaire = $("#m2-choix").value;
        const taches = {};
        $$("[data-tache]").forEach(x => taches[x.dataset.tache] = x.value);
        if (Object.keys(taches).length) d.ia_taches = taches;
      }
      const r = await API.post("/api/reglages", d);
      Etat.ref = await API.get("/api/referentiel");
      App.etatMoteur();
      toast("Réglages enregistrés.");
    };

    const valeursStt = () => ({
      url: ($('[data-r="stt_url"]') || {}).value || "",
      cle: ($('[data-r="stt_cle"]') || {}).value || "",
      modele: ($('[data-r="stt_modele"]') || {}).value || "",
    });

    $("#test-stt").onclick = async () => {
      $("#res-stt").innerHTML = `<span class="chargement"></span> Test en cours…`;
      const r = await API.post("/api/prof/stt/tester", valeursStt());
      $("#res-stt").innerHTML = `<div class="res-test ${r.ok ? "ok" : "ko"}">
        ${r.ok ? "✓" : "⚠"} ${echapper(r.message)}</div>`;
    };

    $("#modeles-stt").onclick = async () => {
      $("#res-stt").innerHTML =
        `<span class="chargement"></span> Interrogation du service…`;
      const v = valeursStt();
      const r = await API.post("/api/reglages/modeles", { url: v.url, cle: v.cle });
      if (!r.ok) {
        $("#res-stt").innerHTML = `<div class="res-test ko">⚠ ${echapper(r.message)}</div>`;
        return;
      }
      // Ici seuls les modèles de transcription nous intéressent.
      const audio = r.modeles.filter(m => /whisper|speech/i.test(m.id)
                                     || /speech-recognition/i.test(m.type));
      $("#res-stt").innerHTML = `
        <div class="res-test ok">✓ Clé valide — ${r.modeles.length} modèle(s)
          accessible(s)${audio.length ? ", dont " + audio.length +
          " pour la transcription" : ""}. Cliquez sur un nom pour l'utiliser.</div>
        <div class="liste-modeles">${(audio.length ? audio : r.modeles)
          .map(m => `<button class="mini choisir-stt"
            data-m="${echapper(m.id)}">${echapper(m.id)}</button>`).join("")}</div>
        ${audio.length ? "" : `<div class="astuce-test">Aucun modèle de
          transcription repéré : ce service ne fait peut-être que du texte.</div>`}`;
      $$(".choisir-stt").forEach(b => b.onclick = () => {
        $('[data-r="stt_modele"]').value = b.dataset.m;
        toast("Modèle choisi : " + b.dataset.m + " — pensez à enregistrer.", 4000);
      });
    };

    $("#test-ia").onclick = async () => {
      $("#res-ia").innerHTML = `<span class="chargement"></span> Test en cours…`;
      const r = await API.post("/api/reglages/tester");
      $("#res-ia").innerHTML = `<span style="color:${r.ok ? "var(--vert)" : "var(--orange)"}">
        ${r.ok ? "✓" : "⚠"} ${echapper(r.message)}</span>`;
    };
  },

  /* Le second moteur IA, et la répartition des tâches entre les deux. */
  async _blocMoteur2(v) {
    const z = $("#zone-moteur2");
    if (!z) return;
    const m = await API.get("/api/reglages/moteurs");
    const actif = m.secondaire && m.secondaire !== "aucun";

    // Réglages tout prêts du moteur PRINCIPAL (« Autre API ») : un clic remplit
    // adresse + modèle + nom. Évite d'aller chercher l'URL exacte du service.
    const zp = $("#presets-m1");
    if (zp) {
      zp.innerHTML = Object.entries(m.presets).map(([cle, p]) =>
        `<button class="mini preset1" data-p1="${cle}">${echapper(p.nom)}</button>`
      ).join(" ");
      $$(".preset1").forEach(b => b.onclick = () => {
        const p = m.presets[b.dataset.p1];
        $('[data-r="ia_nom_api"]').value = p.nom;
        $('[data-r="ia_url_api"]').value = p.url;
        $('[data-r="ia_modele_api"]').value = p.modele;
        $("#m1-aide").textContent = p.aide;
      });
    }

    z.innerHTML = `
      <label class="champ">Second moteur</label>
      <select id="m2-choix" style="max-width:340px">
        <option value="aucun" ${!actif ? "selected" : ""}>
          — aucun (tout passe par le moteur principal) —</option>
        <option value="api2" ${m.secondaire === "api2" ? "selected" : ""}>
          Un autre service (Albert, OpenAI, Mistral…)</option>
        <option value="ollama" ${m.secondaire === "ollama" ? "selected" : ""}>
          Ollama (local, aucune donnée ne sort)</option>
        <option value="deepseek" ${m.secondaire === "deepseek" ? "selected" : ""}>
          DeepSeek</option>
      </select>

      <div id="m2-reglages" style="${m.secondaire === "api2" ? "" : "display:none"}">
        <div class="rangee" style="margin:14px 0 10px">
          <span class="champ" style="margin:0">Réglages tout prêts</span>
          ${Object.entries(m.presets).map(([cle, p]) =>
            `<button class="mini preset" data-p="${cle}">${echapper(p.nom)}</button>`
          ).join("")}
        </div>
        <div id="m2-aide" class="carte-sous" style="margin-bottom:10px"></div>
        <div class="grille g2">
          <div><label class="champ">Nom affiché</label>
            <input type="text" data-r="ia_nom_api2" value="${echapper(v.ia_nom_api2 || "")}"></div>
          <div><label class="champ">Nom du modèle</label>
            <input type="text" data-r="ia_modele_api2" value="${echapper(v.ia_modele_api2 || "")}"></div>
          <div><label class="champ">Adresse de l'API</label>
            <input type="text" data-r="ia_url_api2" value="${echapper(v.ia_url_api2 || "")}"></div>
          <div><label class="champ">Clé d'accès</label>
            <input type="password" data-r="ia_cle_api2" value="${echapper(v.ia_cle_api2 || "")}"></div>
        </div>
      </div>

      <div id="m2-taches" style="${actif ? "" : "display:none"}">
        <div class="carte-sous" style="margin:18px 0 8px">
          <b>Qui fait quoi ?</b> Enregistrez d'abord les réglages ci-dessous,
          puis répartissez les tâches.</div>
        <table><thead><tr><th>Tâche</th><th>Moteur employé</th></tr></thead>
        <tbody>${Object.entries(m.libelles_taches).map(([cle, lib]) => `
          <tr><td>${echapper(lib)}</td>
            <td><select data-tache="${cle}" style="max-width:260px">
              <option value="principal" ${(m.taches[cle] || "principal") === "principal"
                ? "selected" : ""}>Principal — ${echapper(m.nom_principal)}</option>
              <option value="secondaire" ${m.taches[cle] === "secondaire"
                ? "selected" : ""}>Second — ${echapper(m.nom_secondaire || "non réglé")}</option>
            </select></td></tr>`).join("")}</tbody></table>
      </div>

      <div class="rangee" style="margin-top:14px">
        <button class="btn fantome" id="m2-tester">🔌 Tester le second moteur</button>
        <button class="btn fantome" id="m2-modeles">📋 Voir les modèles disponibles</button>
      </div>
      <div id="m2-res" style="font-size:13px;margin-top:10px"></div>
      <div class="astuce-test">Le test utilise ce qui est écrit ci-dessus :
        pas besoin d'enregistrer avant d'essayer.</div>`;

    $("#m2-choix").onchange = e => {
      $("#m2-reglages").style.display = e.target.value === "api2" ? "" : "none";
      $("#m2-taches").style.display = e.target.value === "aucun" ? "none" : "";
    };
    $$(".preset").forEach(b => b.onclick = () => {
      const p = m.presets[b.dataset.p];
      $('[data-r="ia_nom_api2"]').value = p.nom;
      $('[data-r="ia_url_api2"]').value = p.url;
      $('[data-r="ia_modele_api2"]').value = p.modele;
      $("#m2-aide").textContent = p.aide;
    });
    // Le test porte sur ce qui est SAISI, pas sur ce qui est enregistré :
    // sinon un « 401 » s'affiche alors que la clé vient d'être collée.
    const valeurs = () => ({
      url: ($('[data-r="ia_url_api2"]') || {}).value || "",
      cle: ($('[data-r="ia_cle_api2"]') || {}).value || "",
      modele: ($('[data-r="ia_modele_api2"]') || {}).value || "",
    });

    $("#m2-tester").onclick = async () => {
      $("#m2-res").innerHTML = `<span class="chargement"></span> Test en cours…`;
      const r = await API.post("/api/reglages/tester",
        { moteur: $("#m2-choix").value, ...valeurs() });
      $("#m2-res").innerHTML = `<div class="res-test ${r.ok ? "ok" : "ko"}">
        ${r.ok ? "✓" : "⚠"} ${echapper(r.message)}</div>`;
    };

    $("#m2-modeles").onclick = async () => {
      $("#m2-res").innerHTML =
        `<span class="chargement"></span> Interrogation du service…`;
      const r = await API.post("/api/reglages/modeles", valeurs());
      if (!r.ok) {
        $("#m2-res").innerHTML = `<div class="res-test ko">⚠ ${echapper(r.message)}</div>`;
        return;
      }
      // Les modèles de discussion d'abord : ce sont ceux qui nous servent ici.
      const texte = r.modeles.filter(m => !/whisper|embed|rerank/i.test(m.id)
                                     && !/automatic-speech|embedding/i.test(m.type));
      $("#m2-res").innerHTML = `
        <div class="res-test ok">✓ Clé valide — ${r.modeles.length} modèle(s)
          accessible(s). Cliquez sur un nom pour l'utiliser.</div>
        <div class="liste-modeles">${(texte.length ? texte : r.modeles)
          .map(m => `<button class="mini choisir-modele"
            data-m="${echapper(m.id)}">${echapper(m.id)}</button>`).join("")}</div>`;
      $$(".choisir-modele").forEach(b => b.onclick = () => {
        $('[data-r="ia_modele_api2"]').value = b.dataset.m;
        toast("Modèle choisi : " + b.dataset.m + " — pensez à enregistrer.", 4000);
      });
    };
  },

  /* Cloisonnement de l'espace élève : verrou + activités ouvertes par classe. */
  async _blocAcces() {
    const z = $("#zone-acces");
    if (!z) return;
    const a = await API.get("/api/prof/activites");
    const sec = await API.get("/api/securite/etat");
    const cases = (liste, prefixe, cid) => Object.entries(a.libelles).map(([cle, lib]) =>
      `<label class="inter" style="margin-right:16px">
        <input type="checkbox" data-act="${prefixe}" data-cle="${cle}"
          ${cid !== undefined ? `data-classe="${cid}"` : ""}
          ${liste.includes(cle) ? "checked" : ""}> ${lib}</label>`).join("");

    z.innerHTML = `
      <label class="inter verrou-inter">
        <input type="checkbox" id="acc-verrou" ${a.verrouille ? "checked" : ""}>
        <b>Verrouiller l'espace élève</b> — la sortie exige le code enseignant</label>
      ${a.verrouille && !sec.defini ? `<div class="avert-acces">
        ⚠ Aucun code enseignant n'est défini : le verrou ne protège rien.
        Créez-en un dans l'onglet <b>🔐 Sécurité &amp; données</b>.</div>` : ""}

      <div class="carte-sous" style="margin:16px 0 6px">
        <b>Activités ouvertes par défaut</b> (pour toutes les classes)</div>
      <div class="rangee">${cases(a.generales, "gen")}</div>

      ${a.classes.length ? `
        <div class="carte-sous" style="margin:18px 0 6px">
          <b>Exceptions, classe par classe</b> — décochez ce que cette classe
          ne doit pas voir</div>
        <table><thead><tr><th>Classe</th><th>Activités ouvertes</th></tr></thead>
        <tbody>${a.classes.map(c => `<tr>
          <td><b>${echapper(c.nom)}</b></td>
          <td><div class="rangee">${cases(c.activites, "cls", c.id)}</div></td>
        </tr>`).join("")}</tbody></table>` : ""}

      <button class="btn" id="acc-sauver" style="margin-top:16px">
        💾 Enregistrer les accès</button>`;

    $("#acc-verrou").onchange = async e => {
      // Activer le verrou sans code ne protégerait rien : on prévient.
      if (e.target.checked && !sec.defini) {
        confirmer("Aucun code enseignant",
          "Le verrou empêche l'élève de revenir côté enseignant… mais seulement " +
          "si un code existe. Voulez-vous en créer un maintenant ?",
          () => this.parametres("securite"), "Créer un code", false);
      }
    };
    $("#acc-sauver").onclick = async () => {
      const gen = $$('[data-act="gen"]').filter(x => x.checked).map(x => x.dataset.cle);
      const par = {};
      $$('[data-act="cls"]').forEach(x => {
        const cid = x.dataset.classe;
        par[cid] = par[cid] || [];
        if (x.checked) par[cid].push(x.dataset.cle);
      });
      await API.post("/api/prof/activites", {
        verrouille: $("#acc-verrou").checked, generales: gen, par_classe: par });
      toast("Accès des élèves enregistrés.");
      this._blocAcces();
    };
  },

  /* ============================================== Impression sur étiquettes
     Badges à coller dans le cahier, et leçons en cartes pour porte-clés.
     Dans les deux cas : on coche, on choisit la planche, on imprime. */
  async impression(onglet) {
    onglet = onglet || "badges";
    const p = await API.get("/api/prof/impression/planches");
    this._planches = p;
    $("#contenu").innerHTML =
      page("🖨️ Imprimer badges et leçons",
        "Sur planches d'étiquettes autocollantes, ou en cartes à plastifier.") +
      `<div class="onglets" id="ong-imp">
        <button class="onglet ${onglet === "badges" ? "actif" : ""}" data-o="badges">
          <span class="onglet-ico">🏅</span> Badges des élèves</button>
        <button class="onglet ${onglet === "lecons" ? "actif" : ""}" data-o="lecons">
          <span class="onglet-ico">📘</span> Leçons du classeur</button>
      </div>
      <div id="imp-corps"></div>`;
    $$("#ong-imp .onglet").forEach(b =>
      b.onclick = () => this.impression(b.dataset.o));
    if (onglet === "badges") this._impBadges();
    else this._impLecons();
  },

  _blocPlanche(liste, defaut) {
    return `
      <div class="carte">
        <div class="carte-titre">Sur quoi imprimer ?</div>
        <div class="grille g2" style="margin-top:10px">
          <div><label class="champ">Planche d'étiquettes</label>
            <select id="imp-planche">
              ${liste.map(x => `<option value="${x.cle}"
                ${x.cle === defaut ? "selected" : ""}>${echapper(x.nom)}</option>`)
                .join("")}
            </select></div>
          <div><label class="champ">Commencer à la case n°</label>
            <input type="number" id="imp-depart" min="1" value="1">
            <div class="astuce-test">Pour réutiliser une planche déjà entamée.</div>
          </div>
          <div><label class="champ">Décalage horizontal (mm)</label>
            <input type="number" id="imp-dx" step="0.5" value="0"></div>
          <div><label class="champ">Décalage vertical (mm)</label>
            <input type="number" id="imp-dy" step="0.5" value="0"></div>
        </div>
        <div class="astuce-test">
          <b>Faites toujours un essai sur papier ordinaire</b>, puis tenez la
          feuille devant la planche à la lumière : s'il y a un décalage, réglez-le
          ici (ou directement dans la fenêtre d'impression, qui propose le même
          réglage).
        </div>
      </div>`;
  },

  async _impBadges() {
    const classes = await API.get("/api/classes");
    const d = await API.get("/api/prof/badges/classe");
    this._badgesClasse = d.eleves;
    if (!d.eleves.length) {
      $("#imp-corps").innerHTML = `<div class="vide">
        Aucun badge obtenu pour l'instant.</div>`;
      return;
    }
    $("#imp-corps").innerHTML =
      this._blocPlanche(this._planches.badges, "L7159") +
      `<div class="rangee" style="margin-bottom:14px">
        <button class="btn fantome" id="imp-tout">☑ Tout sélectionner</button>
        <button class="btn fantome" id="imp-rien">☐ Tout décocher</button>
        <span id="imp-compte" class="compteur-banque" style="margin:0"></span>
        <button class="btn pousse" id="imp-go">🖨️ Imprimer la planche</button>
      </div>
      ${d.eleves.map(e => `
        <div class="carte carte-eleve-badges">
          <label class="inter eleve-tout">
            <input type="checkbox" class="coche-eleve" data-e="${e.eleve_id}">
            <b>${echapper(e.prenom)}</b>
            <span style="color:var(--texte-pale)">${echapper(e.classe)}</span>
            <span class="badge-nb">${e.badges.length} badge(s)</span>
          </label>
          <div class="badges-choix">
            ${e.badges.map(x => `
              <label class="badge-choix" style="--c:${x.couleur}">
                <input type="checkbox" class="coche-badge"
                  data-e="${e.eleve_id}" data-p="${echapper(e.prenom)}"
                  data-t="${echapper(x.titre)}" data-o="${echapper(x.objectif)}"
                  data-em="${x.emoji}" data-c="${x.couleur}">
                <span class="bc-emo">${x.emoji}</span>
                <span class="bc-txt">${echapper(x.titre)}</span>
              </label>`).join("")}
          </div>
        </div>`).join("")}`;

    const compter = () => {
      const n = $$(".coche-badge").filter(x => x.checked).length;
      $("#imp-compte").textContent = `${n} badge(s) sélectionné(s)`;
      $("#imp-go").disabled = !n;
    };
    $$(".coche-badge").forEach(x => x.onchange = compter);
    $$(".coche-eleve").forEach(x => x.onchange = () => {
      $$(`.coche-badge[data-e="${x.dataset.e}"]`).forEach(b => b.checked = x.checked);
      compter();
    });
    $("#imp-tout").onclick = () => {
      $$(".coche-badge, .coche-eleve").forEach(x => x.checked = true); compter();
    };
    $("#imp-rien").onclick = () => {
      $$(".coche-badge, .coche-eleve").forEach(x => x.checked = false); compter();
    };
    $("#imp-go").onclick = async () => {
      const badges = $$(".coche-badge").filter(x => x.checked).map(x => ({
        prenom: x.dataset.p, titre: x.dataset.t, objectif: x.dataset.o,
        emoji: x.dataset.em, couleur: x.dataset.c,
      }));
      if (!badges.length) return;
      const r = await API.post("/api/prof/impression/badges", {
        badges, planche: $("#imp-planche").value,
        depart: Math.max(0, (+$("#imp-depart").value || 1) - 1),
        dx: +$("#imp-dx").value || 0, dy: +$("#imp-dy").value || 0 });
      toast(`${r.nombre} badge(s) — planche ouverte pour l'impression.`, 5000);
    };
    compter();
  },

  async _impLecons() {
    const dispo = await API.get("/api/classeur/disponible");
    if (!dispo.disponible) {
      $("#imp-corps").innerHTML = `<div class="vide">
        Aucune fiche installée dans le classeur.</div>`;
      return;
    }
    const fiches = await API.get("/api/classeur/liste");
    const domaines = [...new Set(fiches.map(f => f.domaine))];
    $("#imp-corps").innerHTML =
      this._blocPlanche(this._planches.lecons, "A7") +
      `<div class="rangee" style="margin-bottom:14px">
        <button class="btn fantome" id="imp-tout">☑ Tout sélectionner</button>
        <button class="btn fantome" id="imp-rien">☐ Tout décocher</button>
        ${domaines.map(d => `<button class="btn fantome imp-dom" data-d="${d}">
          + ${echapper(d)}</button>`).join("")}
        <span id="imp-compte" class="compteur-banque" style="margin:0"></span>
        <button class="btn pousse" id="imp-go">🖨️ Imprimer les cartes</button>
      </div>
      <div class="grille-lecons-choix">
        ${fiches.map(f => `
          <label class="lecon-choix">
            <input type="checkbox" class="coche-lecon" data-id="${f.lecon_id}"
              data-dom="${echapper(f.domaine)}">
            <span class="lc-id">${echapper(f.lecon_id)}</span>
            <span class="lc-titre">${echapper(
              (f.titre || "").replace(/^[^\p{L}]+/u, ""))}</span>
          </label>`).join("")}
      </div>`;

    const compter = () => {
      const n = $$(".coche-lecon").filter(x => x.checked).length;
      $("#imp-compte").textContent = `${n} leçon(s) sélectionnée(s)`;
      $("#imp-go").disabled = !n;
    };
    $$(".coche-lecon").forEach(x => x.onchange = compter);
    $("#imp-tout").onclick = () => {
      $$(".coche-lecon").forEach(x => x.checked = true); compter();
    };
    $("#imp-rien").onclick = () => {
      $$(".coche-lecon").forEach(x => x.checked = false); compter();
    };
    $$(".imp-dom").forEach(b => b.onclick = () => {
      $$(`.coche-lecon[data-dom="${b.dataset.d}"]`).forEach(x => x.checked = true);
      compter();
    });
    $("#imp-go").onclick = async () => {
      const lecons = $$(".coche-lecon").filter(x => x.checked).map(x => x.dataset.id);
      if (!lecons.length) return;
      const r = await API.post("/api/prof/impression/lecons", {
        lecons, planche: $("#imp-planche").value,
        dx: +$("#imp-dx").value || 0, dy: +$("#imp-dy").value || 0 });
      toast(`${r.nombre} carte(s) — planche ouverte pour l'impression.`, 5000);
    };
    compter();
  },

  /* ------------------------------------------- Ce que l'analyse conseille
     L'enseignant ne lit plus des tableaux pour décider : l'analyse propose
     l'activité de reprise, il valide d'un clic. L'élève la trouve « à faire »
     au début de sa prochaine séance. */
  async devoirsSuggeres() {
    const classes = await API.get("/api/classes");
    $("#contenu").innerHTML =
      page("🎯 À faire la prochaine fois",
        "Ce que l'analyse conseille, élève par élève. Vous validez d'un clic.") +
      `<div class="rangee" style="margin-bottom:18px">
        ${this._retourBord()}
        <label class="champ" style="margin:0 0 0 6px">Classe</label>
        <select id="ds-classe" style="width:220px">
          <option value="0">Toutes les classes</option>
          ${classes.map(c => `<option value="${c.id}">${echapper(c.nom)}</option>`).join("")}
        </select>
        <button class="btn fantome pousse" id="ds-tout">
          ✓ Tout assigner (prioritaires)</button>
      </div><div id="ds-corps"></div>`;
    $("#ds-classe").onchange = () => this._dessinerSuggestions($("#ds-classe").value);
    this._brancherRetourBord();
    this._dessinerSuggestions(0);
  },

  async _dessinerSuggestions(cid) {
    const d = await API.get("/api/prof/devoirs-suggeres?classe_id=" + cid);
    this._suggestions = d;
    if (!d.suggestions.length) {
      $("#ds-corps").innerHTML = `<div class="vide" style="color:var(--vert)">
        ✅ Rien à signaler : aucun élève n'a besoin d'une reprise particulière.</div>`;
      return;
    }
    const ico = { flash: "⚡", dictee: "✍️", lecon: "📘", fluence: "📖" };
    $("#ds-corps").innerHTML = d.suggestions.map(s => `
      <div class="carte suggestion">
        <div class="sg-eleve">
          <span class="sg-prenom">${echapper(s.prenom)}</span>
          <span class="sg-classe">${echapper(s.classe)}</span>
        </div>
        <div class="sg-pistes">
          ${s.pistes.map(p => `
            <div class="sg-piste ${p.urgence >= 2 ? "urgente" : ""}">
              <span class="sg-ico">${ico[p.genre] || "•"}</span>
              <div class="sg-texte">
                <div class="sg-titre">${echapper(p.titre)}</div>
                <div class="sg-motif">${echapper(p.motif)}${p.lecon_titre
                  ? ` · leçon « ${echapper(p.lecon_titre.replace(/^[^\p{L}]+/u, ""))} »`
                  : ""}</div>
              </div>
              <button class="btn assigner" data-e="${s.eleve_id}"
                data-g="${p.genre}" data-c="${echapper(p.categorie || "")}"
                data-l="${echapper(p.lecon_id || "")}"
                data-t="${echapper(p.titre)}">Assigner</button>
            </div>`).join("")}
        </div>
      </div>`).join("");
    this._brancherAssigner();
    $("#ds-tout").onclick = () => this._assignerTout();
  },

  _brancherAssigner() {
    $$(".assigner").forEach(b => b.onclick = async () => {
      b.disabled = true;
      b.textContent = "✓ Assigné";
      await API.post("/api/prof/devoirs-suggeres/assigner", {
        eleve_id: +b.dataset.e, genre: b.dataset.g,
        categorie: b.dataset.c, lecon_id: b.dataset.l, titre: b.dataset.t });
    });
  },

  async _assignerTout() {
    const d = this._suggestions;
    if (!d || !d.suggestions.length) return;
    let n = 0;
    for (const s of d.suggestions) {
      const p = s.pistes.find(x => x.urgence >= 2);
      if (!p) continue;
      await API.post("/api/prof/devoirs-suggeres/assigner", {
        eleve_id: s.eleve_id, genre: p.genre, categorie: p.categorie || "",
        lecon_id: p.lecon_id || "", titre: p.titre });
      n++;
    }
    toast(`${n} activité(s) prioritaire(s) assignée(s).`, 4000);
    this._dessinerSuggestions($("#ds-classe").value);
  },

  /* ------------------------------------------------------ Mots cherchés
     Ce que les élèves cherchent au dictionnaire est une information rare :
     ce sont les mots dont ils DOUTENT, ceux qu'ils n'écriront jamais mal
     dans une dictée surveillée mais qui les bloquent en rédaction. */
  async motsCherches() {
    const classes = await API.get("/api/classes");
    $("#contenu").innerHTML =
      page("🔎 Ce que les élèves cherchent",
        "Les mots sur lesquels ils doutent — matière première pour vos leçons.") +
      `<div class="rangee" style="margin-bottom:18px">
        ${this._retourBord()}
        <label class="champ" style="margin:0 0 0 6px">Classe</label>
        <select id="mc-classe" style="width:220px">
          <option value="0">Toutes les classes</option>
          ${classes.map(c => `<option value="${c.id}">${echapper(c.nom)}</option>`).join("")}
        </select>
      </div><div id="mc-corps"></div>`;
    $("#mc-classe").onchange = () => this._dessinerMotsCherches($("#mc-classe").value);
    this._brancherRetourBord();
    this._dessinerMotsCherches(0);
  },

  async _dessinerMotsCherches(cid) {
    const d = await API.get("/api/prof/dico/recherches?classe_id=" + cid);
    if (!d.total) {
      $("#mc-corps").innerHTML = `<div class="vide">
        Aucune recherche pour l'instant.<br><br>
        Les mots apparaîtront ici dès que les élèves utiliseront
        « Mon dictionnaire ».</div>`;
      return;
    }
    const bloc = (titre, sous, liste, couleur) => `
      <div class="carte">
        <div class="carte-titre">${titre}</div>
        <div class="carte-sous">${sous}</div>
        ${liste.length ? `<div class="nuage-mots">
          ${liste.map(x => `<span class="mot-cherche" style="--c:${couleur}">
            ${echapper(x.mot)}<b>${x.n}</b></span>`).join("")}</div>`
        : `<div class="vide" style="padding:24px">Rien à signaler.</div>`}
      </div>`;

    $("#mc-corps").innerHTML = `
      <div class="stats">
        <div class="stat"><div class="v">${d.total}</div>
          <div class="l">recherches au total</div></div>
        <div class="stat"><div class="v" style="color:var(--vert)">${
          d.mots_cherches.length}</div>
          <div class="l">mots différents retenus</div></div>
        <div class="stat"><div class="v" style="color:var(--orange)">${
          d.sans_resultat.length}</div>
          <div class="l">essais restés sans réponse</div></div>
      </div>
      ${bloc("📖 Les mots qu'ils ont retenus",
        "Ils ont cherché, lu la définition, et choisi ce mot. Le chiffre est le " +
        "nombre de fois.", d.mots_cherches, "var(--bleu)")}
      ${bloc("🤔 Les essais sans choix",
        "Ils ont cherché mais n'ont ouvert aucune définition : le mot leur a " +
        "peut-être échappé.", d.essais_sans_choix, "var(--orange)")}
      ${bloc("❌ Les essais sans aucun résultat",
        "L'orthographe tentée était trop éloignée. Ces mots-là méritent une " +
        "leçon : l'élève ne s'en approche même pas à l'oreille.",
        d.sans_resultat, "var(--rouge)")}
      <div class="carte">
        <div class="carte-titre">Les dernières recherches</div>
        <table style="margin-top:10px"><thead><tr>
          <th>Élève</th><th>A écrit</th><th>A retenu</th><th>Depuis</th>
        </tr></thead><tbody>${d.recentes.map(r => `<tr>
          <td>${echapper(r.prenom || "—")}</td>
          <td><i>${echapper(r.essai)}</i></td>
          <td>${r.mot_retenu
            ? `<b>${echapper(r.mot_retenu)}</b>`
            : `<span style="color:var(--texte-pale)">—</span>`}</td>
          <td><span class="dev-type">${r.depuis === "correction"
            ? "Je me corrige" : "Dictionnaire"}</span></td>
        </tr>`).join("")}</tbody></table>
      </div>`;
  },

  /* --------------------------------------------------------- Pilotage fin */
  async pilotage() {
    const classes = await API.get("/api/classes");
    $("#contenu").innerHTML =
      page("Pilotage fin", "Points faibles de la classe et élèves qui décrochent.") +
      `<div class="rangee" style="margin-bottom:16px;align-items:center;gap:10px">
        ${this._retourBord()}
        <label class="champ" style="margin:0 0 0 6px">Classe</label>
        <select id="pil-classe" style="width:220px">
          <option value="0">Toutes les classes</option>
          ${classes.map(c => `<option value="${c.id}">${echapper(c.nom)}</option>`).join("")}
        </select></div>
      <div class="carte"><div class="carte-titre">🔥 Points faibles par catégorie</div>
        <div class="carte-sous">Nombre moyen d'erreurs par séance. Plus c'est foncé,
          plus la catégorie pose problème.</div>
        <div id="pil-heatmap" class="heatmap"></div></div>
      <div class="carte"><div class="carte-titre">📉 Élèves en régression</div>
        <div class="carte-sous">Ceux qui allaient bien et dont les résultats se
          dégradent — souvent plus urgents que les difficultés installées.</div>
        <div id="pil-reg" style="margin-top:12px"></div></div>`;
    const dessiner = () => {
      const cid = $("#pil-classe").value;
      this._heatmap(cid); this._regressions();
    };
    $("#pil-classe").onchange = dessiner;
    this._brancherRetourBord();
    dessiner();
  },

  async _heatmap(cid) {
    const { heatmap: h, libelles } = await API.get("/api/prof/heatmap?classe_id=" + cid);
    if (!h.eleves.length) {
      $("#pil-heatmap").innerHTML = `<div class="vide">Pas encore de séances de correction.</div>`;
      return;
    }
    const max = Math.max(...h.eleves.flatMap(e => Object.values(e.valeurs)), 1);
    const cell = v => {
      const t = Math.min(v / max, 1), l = 96 - t * 52;
      const bg = `hsl(${t > .55 ? 8 : 245},${28 + t * 46}%,${l}%)`;
      return `<div class="hm-cell" style="background:${bg};color:${t > .55 ? "#fff" : "var(--texte)"}">${v}</div>`;
    };
    let html = `<div class="hm-ligne"><div class="hm-nom entete">Élève</div>` +
      h.categories.map(c => `<div class="hm-cell entete">${libelles[c]}</div>`).join("") + `</div>`;
    for (const e of h.eleves)
      html += `<div class="hm-ligne"><div class="hm-nom">${echapper(e.nom)}</div>` +
        h.categories.map(c => cell(e.valeurs[c])).join("") + `</div>`;
    html += `<div class="hm-ligne"><div class="hm-nom entete">Moyenne</div>` +
      h.categories.map(c => cell(h.moyennes[c])).join("") + `</div>`;
    $("#pil-heatmap").innerHTML = html;
  },

  async _regressions() {
    const { regressions: rg, libelles } = await API.get("/api/prof/regressions");
    $("#pil-reg").innerHTML = rg.length ? rg.map(r => `
      <div class="reg-ligne">
        <div><b>${echapper(r.nom)}</b> <span style="color:var(--texte-pale)">
          (${echapper(r.classe)})</span>
          <div class="reg-meta">${r.avant} <span class="reg-fleche">→ ${r.apres}</span>
            erreurs / séance</div></div>
        <span class="reg-tag">${libelles[r.categorie] || r.categorie}</span>
      </div>`).join("") : `<div class="vide">Aucun décrochage détecté. 🎉</div>`;
  },

  /* ------------------------------------------------------------------ Devoirs */
  async devoirs() {
    const classes = await API.get("/api/classes");
    const eleves = classes.flatMap(c => c.eleves);
    const textes = await API.get("/api/textes/correction");
    $("#contenu").innerHTML =
      page("Devoirs", "Assigner un texte à corriger à une classe ou à un élève.") +
      `<div class="carte"><div class="rangee" style="align-items:flex-end;gap:14px;flex-wrap:wrap">
        <div><label class="champ">Texte</label>
          <select id="dev-texte" style="min-width:200px">
            ${textes.map(t => `<option value="${t.id}">${echapper(t.titre)}</option>`).join("")}
          </select></div>
        <div><label class="champ">Destinataire</label>
          <select id="dev-cible" style="min-width:220px">
            <optgroup label="Classe entière">
              ${classes.map(c => `<option value="c-${c.id}">Toute la ${echapper(c.nom)}</option>`).join("")}
            </optgroup>
            <optgroup label="Élève">
              ${eleves.map(e => `<option value="e-${e.id}">${echapper(e.prenom)} (${echapper(e.classe_nom)})</option>`).join("")}
            </optgroup>
          </select></div>
        <button class="btn" id="dev-assigner">Assigner</button>
      </div></div>
      <div class="carte"><div class="carte-titre">Devoirs en cours</div>
        <div id="dev-liste" style="margin-top:12px"></div></div>`;
    $("#dev-assigner").onclick = async () => {
      const [ty, id] = $("#dev-cible").value.split("-");
      const corps = { texte_id: +$("#dev-texte").value };
      if (ty === "c") corps.classe_id = +id; else corps.eleve_id = +id;
      await API.post("/api/assignations", corps);
      toast("Devoir assigné."); this._listeDevoirs();
    };
    this._listeDevoirs();
  },

  async _listeDevoirs() {
    const { assignations: a } = await API.get("/api/prof/assignations");
    $("#dev-liste").innerHTML = a.length ? a.map(d => `
      <div class="dev-ligne">
        <span><b>${echapper(d.titre)}</b> → ${echapper(d.cible)}
          <span class="dev-type">${d.type}</span></span>
        <button class="btn-supprimer" data-a="${d.id}">✕</button>
      </div>`).join("") : `<div class="vide">Aucun devoir assigné.</div>`;
    $$("[data-a]").forEach(b => b.onclick = async () => {
      await API.del("/api/assignations/" + b.dataset.a); this._listeDevoirs();
    });
  },

  /* -------------------------------------------------------- Sécurité & données */
  async securite() {
    const sec = await API.get("/api/securite/etat");
    const sauv = await API.get("/api/prof/sauvegardes");
    const sauvegardes = sauv.sauvegardes || [];
    const res = await API.get("/api/prof/reseau");
    this._ecrire("Sécurité & données", "Code enseignant, sauvegardes, accès des Chromebooks.",
      `<div class="carte"><div class="carte-titre">🔐 Code enseignant</div>
        <div class="carte-sous">Protège l'accès à cet espace. Les élèves gardent leur
          accès habituel (classe → prénom).</div>
        <div id="sec-pin" style="margin-top:12px"></div></div>

      <div class="carte"><div class="carte-titre">💾 Sauvegardes</div>
        <div class="carte-sous">Copie de sécurité automatique chaque jour d'utilisation
          (10 conservées). Restauration possible à tout moment.</div>
        <div class="rangee" style="margin:12px 0">
          <button class="btn" id="sec-sauver">Sauvegarder maintenant</button></div>
        <div id="sec-liste"></div></div>

      <div class="carte"><div class="carte-titre">🗄️ Deuxième copie (recommandé)</div>
        <div class="carte-sous">Les sauvegardes ci-dessus sont sur le même disque que
          vos données : si ce disque tombe en panne, tout disparaît ensemble.
          Indiquez ici un <b>second dossier</b> — un dossier Nextcloud synchronisé, une
          clé USB, un disque externe — et l'application y déposera une copie à chaque
          sauvegarde.</div>
        <div id="sec-externe" style="margin-top:12px"></div></div>

      <div class="carte"><div class="carte-titre">🖥️ Mode salle informatique</div>
        <div class="carte-sous">Permet aux Chromebooks d'ouvrir l'application sur le
          même wifi. Désactivé par défaut.</div>
        <label class="inter" style="margin-top:10px">
          <input type="checkbox" id="sec-salle" ${res.actif ? "checked" : ""}>
          Activer l'accès depuis les Chromebooks</label>
        <div id="sec-adresse" style="margin-top:12px">${this._blocAdresse(res)}</div></div>`);

    this._rendrePin(sec);
    this._rendreSauv(sauvegardes);
    this._rendreExterne(sauv.externe || {}, sauv.externes || []);
    $("#sec-sauver").onclick = async () => {
      const r = await API.post("/api/prof/sauvegardes/creer");
      toast(r.ok ? "Sauvegarde créée." : "Échec.", );
      if (r.ok) {
        this._rendreSauv(r.sauvegardes);
        this._rendreExterne(r.externe || {}, r.externes || []);
      }
    };
    $("#sec-salle").onchange = async e => {
      const r = await API.post("/api/prof/reseau/basculer", { actif: e.target.checked });
      $("#sec-adresse").innerHTML = this._blocAdresse(r);
      if (r.actif) toast("Redémarrez l'application pour ouvrir l'accès réseau.");
    };
  },

  _blocAdresse(r) {
    if (!r.actif) return `<div style="color:var(--texte-pale)">Inactif.</div>`;
    return `<div class="salle-adresse">${echapper(r.url)}</div>
      <div class="salle-qr">${r.qr || ""}</div>
      <div class="salle-note">Sur un Chromebook : ouvrir Chrome, taper cette adresse
        ou scanner le QR. Si ça ne marche pas, vérifier le même wifi ; sinon demander
        au service informatique de la ville si les appareils peuvent communiquer.</div>`;
  },

  _rendrePin(sec) {
    const z = $("#sec-pin");
    if (!sec.defini) {
      z.innerHTML = `<div style="color:var(--texte-pale);margin-bottom:10px">
        Aucun code défini : l'espace est libre d'accès.</div>
        <input id="np" class="champ-inline" inputmode="numeric" maxlength="6" placeholder="4 à 6 chiffres">
        <button class="btn" id="creer-pin">Créer un code</button>
        <div class="verrou-err" id="pin-err"></div>`;
      $("#creer-pin").onclick = async () => {
        const r = await API.post("/api/securite/creer", { pin: $("#np").value });
        if (r.erreur) return $("#pin-err").textContent = r.erreur;
        Etat.jeton = r.jeton;
        modale(`<div class="carte-titre">Code de récupération</div>
          <p style="color:var(--texte-doux);margin:8px 0">Notez-le : il ne s'affiche
          qu'une fois.</p><div class="verrou-code">${echapper(r.code_recuperation)}</div>
          <div class="rangee"><button class="btn" onclick="fermerModale()">J'ai noté</button></div>`);
        this.securite();
      };
    } else {
      z.innerHTML = `<div class="rangee" style="gap:8px;flex-wrap:wrap">
        <input id="pa" class="champ-inline" inputmode="numeric" maxlength="6" placeholder="code actuel">
        <input id="pn" class="champ-inline" inputmode="numeric" maxlength="6" placeholder="nouveau code">
        <button class="btn" id="chg-pin">Changer le code</button>
        <button class="btn fantome" id="sup-pin">Retirer le code</button></div>
        <div class="rangee" style="margin-top:12px;gap:8px;align-items:center">
          <label class="champ" style="margin:0">Verrouillage auto après</label>
          <select id="delai">
            ${[5, 15, 30, 60].map(m => `<option value="${m}" ${m === sec.delai ? "selected" : ""}>
              ${m < 60 ? m + " minutes" : "1 heure"}</option>`).join("")}</select></div>
        <div class="verrou-err" id="pin-err"></div>`;
      $("#chg-pin").onclick = async () => {
        const r = await API.post("/api/securite/changer",
          { ancien: $("#pa").value, nouveau: $("#pn").value });
        $("#pin-err").textContent = r.erreur || "";
        if (r.ok) toast("Code modifié.");
      };
      $("#sup-pin").onclick = () => confirmer("Retirer le code ?",
        "L'espace enseignant redeviendra libre d'accès.", async () => {
          const r = await API.post("/api/securite/supprimer");
          if (r.ok) { toast("Code retiré."); this.securite(); }
        });
      $("#delai").onchange = e =>
        API.post("/api/securite/delai", { minutes: +e.target.value });
    }
  },

  _rendreSauv(liste) {
    $("#sec-liste").innerHTML = liste.length ? liste.map(s => `
      <div class="dev-ligne">
        <span>${echapper(s.date)} <span class="dev-type">${s.taille_ko} Ko</span></span>
        <button class="btn-mini" data-s="${echapper(s.nom)}">Restaurer</button>
      </div>`).join("") : `<div class="vide">Aucune sauvegarde pour l'instant.</div>`;
    $$("#sec-liste [data-s]").forEach(b => b.onclick = () => confirmer("Restaurer ?",
      "Les données actuelles seront remplacées (une copie est faite avant).", async () => {
        const r = await API.post("/api/prof/sauvegardes/restaurer", { nom: b.dataset.s });
        toast(r.ok ? "Données restaurées." : "Échec.");
      }));
  },

  /* Deuxième dossier de sauvegarde : Nextcloud, clé USB, disque externe. */
  _rendreExterne(etat, copies) {
    const z = $("#sec-externe");
    if (!z) return;
    const dossier = etat.dossier || "";
    const actif = !!etat.actif;

    // État lisible : ce que l'enseignant a besoin de savoir en un coup d'œil.
    let ligneEtat = `<div style="color:var(--texte-pale)">Aucun second dossier : vos
      sauvegardes ne sont qu'à un seul endroit.</div>`;
    if (actif && etat.joignable) {
      ligneEtat = `<div style="color:var(--succes,#15A34A)">✔ Dossier joignable —
        ${copies.length} copie(s) déposée(s)${etat.derniere_copie
          ? `, dernière le ${echapper(etat.derniere_copie)}` : ""}.</div>`;
    } else if (actif && !etat.joignable) {
      ligneEtat = `<div style="color:var(--alerte,#D97706)">⚠ Dossier introuvable pour
        le moment (clé débranchée ? dossier Nextcloud non synchronisé ?). Les
        sauvegardes locales continuent normalement, et les copies manquantes seront
        rattrapées dès que le dossier sera de nouveau accessible.</div>`;
    }
    if (etat.message) {
      ligneEtat += `<div style="color:var(--texte-pale);margin-top:6px">
        ${echapper(etat.message)}</div>`;
    }

    z.innerHTML = `
      <label class="inter" style="margin-bottom:10px">
        <input type="checkbox" id="ext-actif" ${actif ? "checked" : ""}>
        Déposer une copie dans un second dossier</label>
      <div class="rangee" style="gap:8px;flex-wrap:wrap;align-items:center">
        <input id="ext-dossier" class="champ-inline" style="min-width:320px;flex:1"
          placeholder="Ex. : C:\\Users\\vous\\Nextcloud\\Sauvegardes  ou  E:\\Sauvegardes"
          value="${echapper(dossier)}">
        <button class="btn fantome" id="ext-tester">Tester</button>
        <button class="btn" id="ext-enregistrer">Enregistrer</button>
      </div>
      <div id="ext-msg" style="margin-top:8px">${ligneEtat}</div>
      <div id="ext-liste" style="margin-top:12px"></div>`;

    // Liste des copies externes (restaurables comme les locales).
    $("#ext-liste").innerHTML = copies.length ? copies.map(s => `
      <div class="dev-ligne">
        <span>${echapper(s.date)} <span class="dev-type">${s.taille_ko} Ko</span></span>
        <button class="btn-mini" data-x="${echapper(s.nom)}">Restaurer</button>
      </div>`).join("") : "";
    $$("#ext-liste [data-x]").forEach(b => b.onclick = () => confirmer("Restaurer ?",
      "Les données actuelles seront remplacées par cette copie externe (une copie de " +
      "sécurité est faite avant).", async () => {
        const r = await API.post("/api/prof/sauvegardes/restaurer",
          { nom: b.dataset.x, externe: true });
        toast(r.ok ? "Données restaurées." : "Échec.");
      }));

    $("#ext-tester").onclick = async () => {
      const r = await API.post("/api/prof/sauvegardes/externe/tester",
        { dossier: $("#ext-dossier").value });
      $("#ext-msg").innerHTML = `<div style="color:${r.ok
        ? "var(--succes,#15A34A)" : "var(--alerte,#D97706)"}">${echapper(r.message)}</div>`;
    };

    $("#ext-enregistrer").onclick = async () => {
      const r = await API.post("/api/prof/sauvegardes/externe", {
        dossier: $("#ext-dossier").value,
        actif: $("#ext-actif").checked,
      });
      if (r.erreur) {
        $("#ext-msg").innerHTML =
          `<div style="color:var(--alerte,#D97706)">${echapper(r.erreur)}</div>`;
        return;
      }
      toast(r.copiees
        ? `Réglage enregistré — ${r.copiees} sauvegarde(s) copiée(s).`
        : "Réglage enregistré.");
      this._rendreExterne(r.externe || {}, r.externes || []);
    };
  },

  /* ------------------------------------------------------------------- Pont */
  async pont() {
    const p = await API.get("/api/pont");
    this._ecrire("Notes & Suivi", "Envoyez automatiquement les résultats vers Notes & Suivi.",
      `<div class="carte">
        <div class="carte-titre">Pourquoi un « pont » ?</div>
        <p style="color:var(--texte-doux);line-height:1.7;margin-top:6px">
          Notes &amp; Suivi chiffre ses données et n'expose aucun serveur : on ne peut
          pas aller lire dedans. En revanche, elle sait aller <b>chercher</b> les
          données d'une application partenaire. C'est donc le Correcteur qui ouvre une
          petite porte locale, et Notes &amp; Suivi vient s'y servir.<br><br>
          Tout reste sur cet ordinateur : rien ne circule sur internet.</p>
      </div>

      <div class="carte">
        <div class="rangee">
          <span class="pastille ${p.actif ? "on" : ""}"></span>
          <b id="etat-pont">${p.actif ? "Pont actif" : "Pont arrêté"}</b>
          <code style="margin-left:12px;color:var(--accent)">${p.actif ? p.url : "—"}</code>
          <button class="btn vert pousse" id="on" ${p.actif ? "disabled" : ""}>
            ▶ Démarrer</button>
          <button class="btn rouge" id="off" ${p.actif ? "" : "disabled"}>⏹ Arrêter</button>
        </div>
      </div>

      <div class="carte">
        <div class="carte-titre">🏠 Portail Enseignant à la maison (tablette / téléphone)</div>
        <div class="carte-sous">Ouvre ce pont (port 4100, lecture seule) au wifi de la
          <b>maison</b> pour que le Portail Enseignant lise les statistiques depuis la
          tablette ou le téléphone. <b>Rien à voir avec le mode salle</b> (Sécurité &amp;
          données), qui ouvre l'espace <i>élève</i> aux Chromebooks de l'école : les deux
          options sont indépendantes et ne doivent jamais servir au même endroit.
          À n'activer que sur le PC fixe du domicile — jamais à l'école.</div>
        <label class="inter" style="margin-top:10px">
          <input type="checkbox" id="pont-lan" ${p.ecoute_lan ? "checked" : ""}>
          Autoriser le Portail (maison) à lire le pont depuis le réseau local</label>
        <div id="pont-lan-info" style="margin-top:10px">
          ${p.ecoute_lan_suspendue
            ? `<div style="color:var(--rouge,#dc2626)">⛔ Mode salle actif : l'écoute
               réseau du pont est suspendue automatiquement (127.0.0.1) tant que les
               Chromebooks ont accès à l'application. Garde-fou de confidentialité.</div>`
            : p.ecoute_lan && p.actif
              ? `<div>Adresse à saisir dans le Portail :
                 <code style="color:var(--accent)">http://${echapper(p.ip)}:4100</code></div>`
              : `<div style="color:var(--texte-pale)">Le pont n'écoute que sur cet
                 ordinateur (127.0.0.1).</div>`}
        </div>
      </div>

      <div class="carte">
        <div class="carte-titre">À faire une seule fois, dans Notes &amp; Suivi</div>
        <ol style="margin:12px 0 0 20px;line-height:2;color:var(--texte)">
          <li>Laisse le pont ci-dessus <b>démarré</b> (il repart tout seul à chaque ouverture).</li>
          <li>Ouvre Notes &amp; Suivi et déverrouille-la avec ton code PIN.</li>
          <li>Dans ses réglages d'intégration, indique l'adresse :
            <code style="color:var(--accent)">${p.url}</code></li>
          <li>Lance une synchronisation.</li>
        </ol>
        <div style="color:var(--texte-doux);font-size:12.5px;margin-top:12px">
          Notes &amp; Suivi récupérera alors, toutes les 5 minutes : la liste des élèves,
          l'évaluation « Autocorrection — français écrit » (note /100), l'évaluation
          « Fluence de lecture (MCLM) » (note /100), le détail de chaque séance
          avec les 8 catégories d'erreurs en compétences, et — nouveau —
          <b>les groupes de besoin</b> : un groupe par difficulté repérée, avec
          ses élèves, la remédiation conseillée et la leçon du classeur
          correspondante. Vos ateliers arrivent donc tout constitués dans
          Notes &amp; Suivi.<br>
          RGPD : seul le prénom est transmis par défaut.</div>
      </div>

      <div class="carte">
        <div class="carte-titre">Solution de secours : export par fichier</div>
        <div class="rangee" style="margin-top:12px">
          <button class="btn fantome" id="ej">⬇ Exporter en JSON</button>
          <button class="btn fantome" id="ec">⬇ Exporter en CSV (tableur)</button>
        </div>
      </div>

      <div class="carte">
        <div class="carte-titre">Journal des échanges (traçabilité RGPD)</div>
        <table style="margin-top:10px"><thead><tr><th>Date</th><th>Action</th>
          <th>Détail</th></tr></thead>
        <tbody>${p.journal.map(j => `<tr><td>${echapper(j.date_action)}</td>
          <td>${echapper(j.action)}</td>
          <td style="color:var(--texte-doux)">${echapper((j.details || "").slice(0, 90))}</td>
        </tr>`).join("") || `<tr><td colspan="3" style="color:var(--texte-pale)">
          Aucun échange pour l'instant.</td></tr>`}</tbody></table>
      </div>`);

    $("#on").onclick = async () => {
      const r = await API.post("/api/pont/demarrer"); toast(r.message); this.pont();
    };
    $("#off").onclick = async () => {
      const r = await API.post("/api/pont/arreter"); toast(r.message); this.pont();
    };
    $("#pont-lan").onchange = async e => {
      const actif = e.target.checked;
      if (actif && !confirm(
        "Ouvrir le pont au réseau local ?\n\n" +
        "À n'activer QUE sur le PC fixe de la maison (jamais sur un ordinateur " +
        "connecté au réseau de l'école). Le mode salle, lui, reste réservé aux " +
        "Chromebooks des élèves : les deux ne partagent rien.")) {
        e.target.checked = false;
        return;
      }
      await API.post("/api/reglages", { integration_ecoute_lan: actif });
      const r = await API.post("/api/pont/redemarrer");
      toast(r.message || (actif ? "Écoute réseau local activée." : "Retour à 127.0.0.1."));
      this.pont();
    };
    $("#ej").onclick = async () => {
      const r = await API.post("/api/export/json"); toast("Fichier créé : " + r.chemin, 5000);
    };
    $("#ec").onclick = async () => {
      const r = await API.post("/api/export/csv"); toast("Fichier créé : " + r.chemin, 5000);
    };
  }
};
