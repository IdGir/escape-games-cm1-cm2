/* ==========================================================================
   MODULE 1 — Autocorrection de l'élève.

   Le point technique délicat : surligner les erreurs DANS une zone de texte
   éditable. Solution retenue : un <textarea> au fond transparent, posé sur un
   calque qui rejoue exactement le même texte, avec des <mark> aux bons endroits.
   Le calque étant SOUS le texte, les marques apparaissent derrière les lettres,
   sans jamais gêner la frappe. Les deux couches partagent police, taille,
   interligne et padding : elles restent alignées au pixel près.
   ========================================================================== */

/* Catégories d'erreurs pour lesquelles le dictionnaire est vraiment utile :
   là où le problème est « comment ça s'écrit », pas « quelle terminaison ». */
const CATS_DICO = ["orthographe", "homophone", "lexique", "segmentation"];

const Correction = {
  // La procédure méthodique de relecture, toujours dans le même ordre.
  // À chaque passage, on ne met en lumière QUE la famille d'erreurs concernée :
  // l'élève ne cherche qu'une seule chose à la fois.
  PASSAGES: [
    { titre: "La cohérence", ico: "🧠",
      consigne: "Relis à voix haute. Est-ce que tout veut dire quelque chose ? Manque-t-il des mots ?",
      cats: ["lexique", "segmentation"] },
    { titre: "Ponctuation & majuscules", ico: "❗",
      consigne: "Vérifie les points et les virgules, et la majuscule au début de chaque phrase.",
      cats: ["ponctuation", "majuscule"] },
    { titre: "Les accords (groupe du nom)", ico: "🧩",
      consigne: "Regarde les déterminants : le nom et l'adjectif s'accordent avec eux (singulier / pluriel).",
      cats: ["accord"] },
    { titre: "Les homophones", ico: "👂",
      consigne: "Ces mots s'entendent pareil mais s'écrivent différemment : a/à, et/est, on/ont, son/sont, ou/où, ces/ses… Remplace-les pour vérifier.",
      cats: ["homophone"] },
    { titre: "La conjugaison", ico: "🔗",
      consigne: "Trouve chaque sujet et accorde son verbe (les petits mots comme a/à ont déjà été vus au passage précédent).",
      cats: ["conjugaison"] },
    { titre: "L'orthographe des mots", ico: "🔤",
      consigne: "Vérifie l'orthographe : syllabes, accents, lettres muettes (cherche un mot de la même famille).",
      cats: ["orthographe"] },
  ],

  etat: {},

  reinit() {
    this.etat = {
      origine: "saisie", texteId: null, reference: "", categories: {},
      texteInitial: "", etape: 0, debut: null, phase: "",
      erreursAvant: 0, detailAvant: {}, detailApres1: {},
      sigs: [], moteur: "", message: "", texteCourant: null,
      corrigeesSolo1: 0, corrigeesSolo: 0,
      corrigeesPassageSeul: 0, corrigeesPassageAide: 0,
      nbAides: 0, aidePassage: false, avantPassage: 0,
      debutCats: {}, ajouts: [],
    };
  },

  /* ---------------------------------------------------------------- Sources */
  async sources() {
    this.reinit();
    const c = Etat.ref.config;
    const t = [];
    if (c.source_saisie_libre)
      t.push(["⌨️", "J'écris mon texte", "Je tape ou je colle un texte que j'ai écrit.", "saisie"]);
    if (c.source_texte_impose)
      t.push(["📚", "Un texte de la classe", "Je choisis un texte préparé par mon enseignant.", "impose"]);
    if (c.source_generation_ia)
      t.push(["🎲", "Un texte surprise", "L'ordinateur me fabrique un texte plein d'erreurs.", "ia"]);

    $("#contenu").innerHTML =
      page("Je me corrige", "D'où vient ton texte ?") +
      `<div class="tuiles">${t.map(([e, h, p, k]) => `
        <div class="tuile" data-src="${k}">
          <div class="emo">${e}</div><h3>${h}</h3><p>${p}</p>
        </div>`).join("")}</div>`;

    $$(".tuile").forEach(x => x.onclick = () => {
      const s = x.dataset.src;
      if (s === "saisie") this.editeur("");
      else if (s === "impose") this.choisirTexte();
      else this.genererTexte();
    });
  },

  async choisirTexte() {
    const textes = await API.get("/api/textes/correction");
    if (!textes.length) { toast("Ton enseignant n'a pas encore enregistré de texte."); return; }
    $("#contenu").innerHTML =
      page("Je me corrige", "Choisis un texte de la classe.") +
      `<div class="carte">
        <label class="champ">Texte</label>
        <select id="sel-texte">
          <option value="">— choisis un texte —</option>
          ${textes.map((t, i) =>
            `<option value="${i}">${echapper(t.titre)} (niveau ${t.niveau})</option>`
          ).join("")}
        </select>
        <div id="apercu" style="margin-top:14px;color:var(--texte-doux);
             line-height:1.7;min-height:70px"></div>
        <div class="rangee" style="margin-top:16px">
          <button class="btn doux" id="retour">← Retour</button>
          <button class="btn" id="charger" disabled>Charger ce texte →</button>
        </div>
      </div>`;
    $("#retour").onclick = () => this.sources();
    $("#sel-texte").onchange = e => {
      const i = e.target.value;
      $("#apercu").textContent = i === "" ? "" : textes[i].contenu.slice(0, 400) + "…";
      $("#charger").disabled = i === "";
    };
    $("#charger").onclick = () => {
      const t = textes[$("#sel-texte").value];
      this.etat.origine = "impose";
      this.etat.texteId = t.id;
      this.etat.reference = (t.corrige || "").trim();
      this.etat.categories = {};
      this.editeur(t.contenu);
    };
  },

  async genererTexte() {
    $("#contenu").innerHTML =
      page("Je me corrige", "Un texte surprise, plein d'erreurs à retrouver.") +
      `<div class="carte">
        <label class="champ">Nombre de phrases</label>
        <input type="number" id="nb" min="2" max="15" value="${Etat.ref.config.ia_nb_phrases}"
               style="width:110px">
        <div class="rangee" style="margin-top:18px">
          <button class="btn doux" id="retour">← Retour</button>
          <button class="btn" id="go"><span class="ico">🎲</span> Fabriquer mon texte</button>
        </div>
        <div id="info" style="margin-top:12px;color:var(--texte-doux)"></div>
      </div>`;
    $("#retour").onclick = () => this.sources();
    $("#go").onclick = async () => {
      $("#info").innerHTML = `<span class="chargement"></span> Fabrication en cours…`;
      $("#go").disabled = true;
      const r = await API.post("/api/generer", { nb_phrases: +$("#nb").value });
      this.etat.origine = "ia";
      this.etat.texteId = null;
      this.etat.reference = r.reference;
      this.etat.categories = r.categories;
      this.editeur(r.texte, r.message);
    };
  },

  /* ---------------------------------------------------------------- Éditeur */
  editeur(contenu, message = "") {
    this.etat.etape = 0;
    $("#contenu").innerHTML =
      page("Mon texte", this.etat.origine === "saisie"
        ? "Écris ou colle ton texte, puis lance ta correction."
        : "Relis attentivement ce texte avant de commencer.") +
      `<div class="editeur">
        ${Confort.barre(true)}
        <div class="zone">
          <div class="calque" id="calque"></div>
          <textarea id="zone" spellcheck="false"
            placeholder="Écris ou colle ton texte ici…"></textarea>
        </div>
      </div>
      <div class="rangee" style="margin-top:16px">
        <button class="btn doux" id="retour">← Changer de texte</button>
        <span style="color:var(--texte-doux);font-size:12.5px" id="msg">
          ${echapper(message)}</span>
        <button class="btn vert grand pousse" id="lancer">
          <span class="ico">💾</span> Enregistrer et commencer ma correction →
        </button>
      </div>`;

    const zone = $("#zone");
    zone.value = contenu;
    Confort.brancher(() => this.redessiner());
    zone.addEventListener("input", () => this.redessiner());
    zone.addEventListener("scroll", () => { $("#calque").scrollTop = zone.scrollTop; });
    $("#retour").onclick = () => this.sources();
    $("#lancer").onclick = () => this.lancer();
    this.redessiner();
  },

  /* Redessine le calque : texte identique + marques d'erreur.
     On ne surligne QUE les erreurs de la famille du passage en cours. */
  /* La zone de texte grandit avec son contenu : quand l'élève agrandit la
     police, le texte ne se retrouve jamais coupé. Au-delà d'une certaine
     hauteur (pour que les boutons restent visibles), c'est un défilement —
     jamais une perte de texte. */
  _ajusterHauteur() {
    const zone = $("#zone");
    const calque = $("#calque");
    if (!zone) return;
    const plafond = Math.max(340, Math.round(window.innerHeight * 0.62));
    zone.style.height = "auto";
    const voulu = zone.scrollHeight + 4;

    // La colonne de droite ne doit pas dépasser dans le vide : on aligne le
    // bas des deux colonnes. Sans cela, le cadre du texte paraissait décalé
    // vers le haut, avec un grand blanc en dessous.
    let minimum = 260;
    const colonne = $("#colonne-suivi");
    const editeur = zone.closest(".editeur");
    if (colonne && editeur) {
      const barre = editeur.querySelector(".barre-outils");
      const hauteurBarre = barre ? barre.offsetHeight : 0;
      const dispo = colonne.offsetHeight - hauteurBarre;
      if (dispo > minimum) minimum = dispo;
    }

    const h = Math.min(Math.max(voulu, minimum), plafond);
    zone.style.height = h + "px";
    zone.style.overflowY = voulu > h ? "auto" : "hidden";
    if (calque) calque.style.overflowY = zone.style.overflowY;
  },

  redessiner() {
    const zone = $("#zone");
    const calque = $("#calque");
    if (!zone || !calque) return;
    const t = zone.value;
    const passage = this.PASSAGES[this.etat.etape - 1];
    // On ne surligne QUE pendant les passages guidés : ni dans l'éditeur de départ,
    // ni pendant la recherche seule (étapes 1 et 2).
    const cats = (this.etat.phase === "passages" && passage) ? passage.cats : [];
    const sigs = cats.length
      ? this.etat.sigs.filter(s => cats.includes(s.categorie)) : [];

    let html = "", pos = 0;
    for (const s of sigs) {
      if (s.debut < pos) continue;
      html += echapper(t.slice(pos, s.debut));
      const contenu = echapper(t.slice(s.debut, s.fin));
      if (!s.certain) {
        html += `<mark class="vig">${contenu}</mark>`;
      } else {
        const c = couleurCat(s.categorie);
        html += `<mark class="cat" style="background:${c}33;
                  box-shadow:inset 0 -2px 0 ${c}">${contenu}</mark>`;
      }
      pos = s.fin;
    }
    html += echapper(t.slice(pos));
    calque.innerHTML = html + "\n";
    this._ajusterHauteur();
    calque.scrollTop = zone.scrollTop;

    const cpt = $("#compteur");
    if (cpt) {
      const mots = (t.match(/[A-Za-zÀ-ÖØ-öø-ÿ-]+/g) || []).length;
      const ph = t.trim() ? t.split(/[.!?…]+/).filter(x => x.trim()).length || 1 : 0;
      cpt.textContent = `${mots} mot${mots > 1 ? "s" : ""} · ${ph} phrase${ph > 1 ? "s" : ""}`;
    }
  },

  /* ------------------------------------------------- Lancement de la correction */
  async lancer() {
    const t = $("#zone").value.trim();
    if ((t.match(/[A-Za-zÀ-ÿ-]+/g) || []).length < 5) {
      toast("Écris au moins une phrase complète (5 mots minimum)."); return;
    }
    this.etat.texteInitial = t;

    // Si aucun corrigé n'est connu (texte écrit par l'élève), on le fait établir
    // par le correcteur : c'est ce qui garantit qu'aucun mot juste ne sera souligné.
    if (!this.etat.reference) {
      $("#lancer").disabled = true;
      $("#msg").innerHTML = `<span class="chargement"></span> Analyse de ton texte…`;
      const r = await API.post("/api/corriger", { texte: t });
      this.etat.reference = r.reference || "";
      this.etat.categories = r.categories || {};
      this.etat.moteur = r.moteur;
      this.etat.message = r.message;
    }

    await this.analyser(t);
    this.etat.erreursAvant = this.etat.nbCertaines;
    this.etat.detailAvant = this.etat.parCategorie;
    this.etat.debut = Date.now();
    this.etat.texteCourant = t;
    this.rechercheSolo();          // Étape 1 : je cherche seul, sans surlignage
  },

  // Petit fil du parcours (avant les 5 passages surlignés).
  _friseIntro(n) {
    const et = [["1", "Je cherche seul"], ["2", "Mon bilan, je continue seul"],
                ["3", "Je corrige avec l'aide"]];
    return `<div class="frise">${et.map(([num, lib], i) =>
      `<div class="etape ${i + 1 < n ? "fait" : i + 1 === n ? "actu" : ""}">
        ${i + 1 < n ? "✓" : num}&nbsp; ${lib}</div>`).join("")}</div>`;
  },

  /* ---- Étape 1 : l'élève cherche seul. On ne donne QUE le nombre d'erreurs. ---- */
  rechercheSolo() {
    this.etat.phase = "solo";
    const n = this.etat.erreursAvant;
    $("#contenu").innerHTML =
      this._friseIntro(1) +
      page("Étape 1 — Je cherche seul(e)",
        "Relis ton texte et corrige ce que tu peux, sans aide. Les erreurs ne sont pas montrées.") +
      `<div class="deux-col">
        <div class="editeur">
          ${Confort.barre(true)}
          <div class="zone"><div class="calque" id="calque"></div>
            <textarea id="zone" spellcheck="false"></textarea></div>
        </div>
        <div id="panneau"><div class="carte" style="border-top:4px solid var(--accent)">
          <div class="carte-titre">🔎 Ton texte contient…</div>
          <div style="text-align:center;margin:14px 0">
            <div style="font-size:56px;font-weight:800;color:var(--accent);line-height:1">${n}</div>
            <div style="color:var(--texte-doux);font-size:12.5px">
              erreur${n > 1 ? "s" : ""} à retrouver</div>
          </div>
          <p style="color:var(--texte-doux);font-size:13px;line-height:1.6">
            À toi de les chercher toi-même. Le compteur ne bouge pas ici : tu verras
            ton résultat à l'étape suivante.</p>
        </div></div>
      </div>
      <div class="rangee" style="margin-top:16px">
        <button class="btn doux" id="retour">← Changer de texte</button>
        <button class="btn grand pousse" id="fini">J'ai cherché seul(e) →</button>
      </div>`;
    const zone = $("#zone");
    zone.value = this.etat.texteCourant ?? this.etat.texteInitial;
    Confort.brancher(() => this.redessiner());
    zone.addEventListener("scroll", () => { $("#calque").scrollTop = zone.scrollTop; });
    $("#retour").onclick = () => this.sources();
    $("#fini").onclick = async () => {
      this.etat.texteCourant = $("#zone").value;
      await this.analyser(this.etat.texteCourant);
      this.etat.detailApres1 = this.etat.parCategorie;
      this.etat.corrigeesSolo1 = Math.max(0, this.etat.erreursAvant - this.etat.nbCertaines);
      this.bilanIntermediaire();
    };
    this.redessiner();
  },

  _chip(c, k) {
    return `<span class="puce" style="background:${couleurCat(c)};
      margin:0 6px 6px 0;display:inline-block">${libelleCat(c)} × ${k}</span>`;
  },

  /* ---- Étape 2 : les deux bilans côte à côte + l'élève continue seul, SANS surlignage. ---- */
  bilanIntermediaire() {
    this.etat.phase = "solo2";               // toujours pas de surlignage

    $("#contenu").innerHTML =
      this._friseIntro(2) +
      page("Étape 2 — Mon bilan, et je continue seul(e)",
        "Tu connais maintenant les types d'erreurs qui restent : essaie encore d'en corriger, toujours sans aide.") +
      `<div class="grille g2 duo-bilan" id="duo"></div>
      <div class="editeur">
        ${Confort.barre(true)}
        <div class="zone"><div class="calque" id="calque"></div>
          <textarea id="zone" spellcheck="false"></textarea></div>
      </div>
      <div class="rangee" style="margin-top:16px">
        <span style="color:var(--texte-doux);font-size:13px">
          Quand tu ne trouves plus rien seul(e), l'application surlignera les erreurs pour t'aider.</span>
        <button class="btn grand pousse" id="go">Je corrige avec l'aide →</button>
      </div>`;

    const zone = $("#zone");
    zone.value = this.etat.texteCourant ?? this.etat.texteInitial;
    Confort.brancher(() => this.redessiner());
    zone.addEventListener("scroll", () => { $("#calque").scrollTop = zone.scrollTop; });
    let minuteur;
    zone.addEventListener("input", () => {
      clearTimeout(minuteur);
      minuteur = setTimeout(async () => {
        await this.analyser(zone.value);
        this._duoBilan();
      }, 350);
      this.redessiner();   // met le compteur à jour, sans surligner (phase solo2)
    });
    $("#go").onclick = async () => {
      this.etat.texteCourant = $("#zone").value;
      await this.analyser(this.etat.texteCourant);
      // Autonomie : les DEUX étapes sans surlignage comptent comme « corrigé seul ».
      this.etat.corrigeesSolo = Math.max(0, this.etat.erreursAvant - this.etat.nbCertaines);
      this.etat.etape = 1;
      this.etat.phase = "passages";
      this.procedure();
    };
    this.redessiner();
    this._duoBilan();
  },

  // Les deux cadres « corrigées / à corriger », sur une même ligne.
  // Ils restent affichés pendant TOUTE la procédure (étape 2 puis les passages)
  // et se mettent à jour en direct.
  _duoBilan() {
    const d = $("#duo");
    if (!d) return;
    const enPassages = this.etat.phase === "passages";
    const avant = this.etat.detailAvant || {}, now = this.etat.parCategorie || {};
    const cats = [...new Set([...Object.keys(avant), ...Object.keys(now)])];
    const corr = cats.map(c => [c, Math.max(0, (avant[c] || 0) - (now[c] || 0))])
      .filter(x => x[1] > 0).sort((a, b) => b[1] - a[1]);
    const rest = cats.map(c => [c, now[c] || 0])
      .filter(x => x[1] > 0).sort((a, b) => b[1] - a[1]);
    const nCorr = Math.max(0, this.etat.erreursAvant - this.etat.nbCertaines);
    const nRest = this.etat.nbCertaines;

    d.innerHTML = `
      <div class="carte bloc-bilan reussi">
        <div class="bloc-bilan-titre">✅ ${enPassages
          ? "Erreurs corrigées" : "Erreurs corrigées seul(e)"}</div>
        <div class="bloc-bilan-nombre" style="color:var(--vert)">${nCorr}</div>
        <div class="bloc-bilan-chips">${corr.length
          ? corr.map(([c, k]) => this._chip(c, k)).join("")
          : `<span class="bloc-bilan-vide">Rien encore — regarde à droite ce qu'il reste !</span>`}</div>
        ${enPassages ? `<div class="bloc-bilan-note">dont
          <b>${this.etat.corrigeesSolo}</b> trouvée(s) tout(e) seul(e), avant l'aide.</div>` : ""}
      </div>
      <div class="carte bloc-bilan restant">
        <div class="bloc-bilan-titre">🔎 Erreurs à corriger</div>
        <div class="bloc-bilan-nombre"
             style="color:${nRest ? "var(--orange)" : "var(--vert)"}">${nRest}</div>
        <div class="bloc-bilan-chips">${rest.length
          ? rest.map(([c, k]) => this._chip(c, k)).join("")
          : `<span style="color:var(--vert);font-weight:700">🎉 ${enPassages
              ? "Plus aucune erreur !" : "Plus rien à revoir seul(e) !"}</span>`}</div>
        ${nRest && !enPassages
          ? `<div class="bloc-bilan-note">Elles ne sont pas montrées : à toi de les trouver.</div>`
          : ""}
      </div>`;
  },

  async analyser(texte) {
    const r = await API.post("/api/analyser", {
      texte, reference: this.etat.reference, categories: this.etat.categories
    });
    this.etat.sigs = r.signalements;
    this.etat.nbCertaines = r.certaines;
    this.etat.nbVigilances = r.vigilances;
    this.etat.parCategorie = r.par_categorie;
    return r;
  },

  /* ------------------------------------------------- Procédure en passages ciblés */
  _compteCats(cats) {
    return this.etat.sigs.filter(s => s.certain && cats.includes(s.categorie)).length;
  },

  _phrase(sig) {
    const t = ($("#zone") && $("#zone").value) ||
      this.etat.texteCourant || this.etat.texteInitial || "";
    let a = sig.debut, b = sig.fin;
    while (a > 0 && !".!?…".includes(t[a - 1])) a--;
    while (b < t.length && !".!?…".includes(t[b])) b++;
    return t.slice(a, Math.min(t.length, b + 1)).trim();
  },

  procedure() {
    const e = this.etat.etape;
    if (e > this.PASSAGES.length) return this.bilan();
    const pas = this.PASSAGES[e - 1];
    this.etat.aidePassage = false;

    // Si l'élève a ajouté une erreur au passage précédent, on l'en informe ici.
    const aj = this.etat.ajouts || [];
    const avert = aj.length
      ? `<div class="alerte forte" style="margin-bottom:14px">
           <div class="rangee" style="gap:8px">
             <span class="puce" style="background:var(--rouge)">Attention</span>
             <span class="t">En corrigeant, tu as ajouté ${aj.reduce((s, x) => s + x[1], 0)}
               erreur(s) : ${aj.map(([c, k]) => `${libelleCat(c)}${k > 1 ? " ×" + k : ""}`).join(", ")}.</span>
           </div>
           <div class="r">Tu les retrouveras (surlignées) au passage qui leur correspond. Relis bien !</div>
         </div>`
      : "";

    // Le bandeau des passages faisait doublon avec le titre juste en dessous.
    // On le remplace par une frise fine, intégrée au titre : la place gagnée
    // profite au texte, et l'élève voit toujours où il en est.
    $("#contenu").innerHTML =
      // Tout tient sur une ligne : la frise, le titre, et le bouton qui fait
      // avancer. Plus aucune bande ne se répète.
      `<div class="entete-passage" style="--c:${couleurCat(pas.cats[0])}">
        <div class="ep-fil">
          ${this.PASSAGES.map((x, i) => `<span class="ep-point ${
            i + 1 < e ? "fait" : i + 1 === e ? "actu" : ""}"
            title="${echapper(x.titre)}">${i + 1 < e ? "✓" : i + 1}</span>`).join("")}
        </div>
        <h1 class="ep-h1">${pas.ico} ${echapper(pas.titre)}</h1>
        <span class="ep-rang">passage ${e} sur ${this.PASSAGES.length}</span>
        <button class="btn ep-suite" id="suite-haut">
          ${e === this.PASSAGES.length ? "Voir mon bilan →" : "Passage suivant →"}
        </button>
      </div>` +
      avert +
      // Les deux compteurs passent AU-DESSUS du texte, en bandeau bas :
      // ils se lisent d'un coup d'œil sans voler de la largeur au texte.
      `<div class="duo-bilan bandeau" id="duo"></div>` +
      // Disposition retenue : les deux compteurs (corrigées / à corriger) et
      // le passage en cours tiennent dans une colonne étroite à DROITE du
      // texte — ils se consultent d'un coup d'œil. L'AIDE, elle, s'ouvre
      // SOUS le texte, sur toute la largeur : c'est elle qui a besoin de
      // place pour se lire. On garde ainsi la vue d'ensemble.
      `<div class="deux-col">
        <div class="editeur">
          ${Confort.barre(true)}
          <div class="zone">
            <div class="calque" id="calque"></div>
            <textarea id="zone" spellcheck="false"></textarea>
          </div>
        </div>
        <div class="colonne-suivi" id="colonne-suivi">
          <div id="panneau"></div>
        </div>
      </div>
      <div id="zone-aide" class="zone-aide"></div>
      <div class="rangee" style="margin-top:14px" id="nav-etape"></div>`;
    $("#fil").textContent = `Passage ${e}/${this.PASSAGES.length} — ${pas.titre}`;
    $("#suite-haut").onclick = () => this.suivante();

    const zone = $("#zone");
    zone.value = this.etat.texteCourant ?? this.etat.texteInitial;
    Confort.brancher(() => this.redessiner());

    let minuteur;
    zone.addEventListener("input", () => {
      clearTimeout(minuteur);
      minuteur = setTimeout(async () => {
        await this.analyser(zone.value);
        this.redessiner();
        this.panneau();
        this._duoBilan();
      }, 350);
      this.redessiner();
    });
    zone.addEventListener("scroll", () => { $("#calque").scrollTop = zone.scrollTop; });

    // Clic sur une erreur surlignée du passage : la leçon + l'aide s'ouvrent.
    zone.addEventListener("click", () => {
      const p = zone.selectionStart;
      const s = this.etat.sigs.find(x => x.certain && pas.cats.includes(x.categorie)
        && p >= x.debut && p <= x.fin);
      if (s) this.lecon(s);
    });

    // Nombre d'erreurs de ce passage AU DÉPART (pour mesurer l'autonomie).
    this.etat.avantPassage = this._compteCats(pas.cats);
    // Photo des erreurs par catégorie à l'entrée du passage : sert à détecter
    // si l'élève AJOUTE une erreur pendant ce passage (on l'en informera après).
    this.etat.debutCats = { ...this.etat.parCategorie };
    this.redessiner();
    this.panneau();
    this._duoBilan();
    this.navigation();
  },

  navigation() {
    const n = $("#nav-etape");
    const e = this.etat.etape;
    const pas = this.PASSAGES[e - 1];
    const dernier = e === this.PASSAGES.length;
    // Le bouton qui fait avancer est déjà sur la ligne du titre : ici on ne
    // garde qu'un rappel discret, sans dupliquer le bouton.
    n.innerHTML =
      `<span style="color:var(--texte-doux);font-size:13px">
        Corrige ce que tu peux, puis passe à la suite avec le bouton en haut
        à droite.</span>`;
  },

  async suivante() {
    this.etat.texteCourant = $("#zone").value;
    await this.analyser(this.etat.texteCourant);
    const pas = this.PASSAGES[this.etat.etape - 1];
    const apres = this._compteCats(pas.cats);
    const corrige = Math.max(0, this.etat.avantPassage - apres);
    // Dans les passages, le texte est surligné (déjà une aide). Si en plus
    // l'élève a demandé un INDICE, ses corrections comptent « avec aide ».
    if (this.etat.aidePassage) this.etat.corrigeesPassageAide += corrige;
    else this.etat.corrigeesPassageSeul += corrige;

    // Détection des erreurs AJOUTÉES pendant ce passage (toutes catégories) :
    // on les signalera au passage suivant.
    const deb = this.etat.debutCats || {}, now = this.etat.parCategorie || {};
    const ajouts = [];
    for (const c of new Set([...Object.keys(deb), ...Object.keys(now)])) {
      const d = (now[c] || 0) - (deb[c] || 0);
      if (d > 0) ajouts.push([c, d]);
    }
    this.etat.ajouts = ajouts;

    this.etat.etape++;
    this.procedure();
  },

  panneau() {
    const p = $("#panneau");
    if (!p) return;
    const pas = this.PASSAGES[this.etat.etape - 1];
    const n = this._compteCats(pas.cats);
    const c = couleurCat(pas.cats[0]);
    // Encart compact, dans la colonne de droite : le passage en cours et le
    // nombre de zones restantes. L'aide, elle, s'ouvre sous le texte.
    p.innerHTML = `
      <div class="carte encart-passage" style="border-top:4px solid ${c}">
        <div class="ep-titre">${pas.ico} ${echapper(pas.titre)}</div>
        <div class="ep-consigne">${echapper(pas.consigne)}</div>
        <div class="ep-compteur" style="color:${n ? c : "var(--vert)"}">
          <span class="ep-nombre">${n}</span>
          <span class="ep-libelle">${n
            ? `zone${n > 1 ? "s" : ""} à revoir`
            : "rien à revoir 🎉"}</span>
        </div>
        <div class="ep-astuce">${n
          ? "👉 Clique sur une zone colorée : l'aide s'ouvre sous ton texte."
          : "Tu peux passer à la suite."}</div>
        ${pas.cats.some(c => CATS_DICO.includes(c)) ? `
          <button class="btn fantome ep-dico" id="ep-dico">
            🔎 Ouvrir le dictionnaire</button>` : ""}
      </div>`;
    // Sur les passages d'orthographe, de lexique ou d'homophones, l'élève
    // doit pouvoir consulter le dictionnaire sans avoir à cliquer d'abord
    // sur une erreur : c'est souvent là qu'il en a besoin.
    const bdico = $("#ep-dico");
    if (bdico) bdico.onclick = () => Dico.ouvrirFenetre("", choisi => {
      const z = $("#zone");
      if (z) { toast(`« ${choisi} » — recopie-le où il faut dans ton texte.`, 4000); }
    });
  },

  // On n'affiche QUE ce qui est utile au cas examiné : la question à se poser,
  // une ou deux pistes ciblées, puis — à la demande — un indice plus direct.
  async lecon(sig) {
    const cat = sig.categorie;
    const c = couleurCat(cat);
    const cible = $("#zone-aide") || $("#zone-lecon") || $("#panneau");
    cible.innerHTML = `<div class="lecon grande"><h4 style="background:${c}">Un instant…</h4></div>`;

    const contexte = this._phrase(sig);
    const A = await API.post("/api/aide", { categorie: cat, mot: sig.mot || "",
      correct: sig.suggestion || "", contexte, message: sig.message || "" });

    const motAff = sig.mot ? ` — « ${echapper(sig.mot)} »` : "";

    // Certains mots ne se déduisent pas (le « t » de « souvent ») : on le dit
    // franchement, au lieu de faire chercher l'élève pour rien.
    const bandeaux = {
      a_savoir: ["🧠", "Ce mot ne se devine pas",
        "Aucune règle ne permet de le retrouver : il faut le savoir, ou aller " +
        "le vérifier dans ton classeur ou le dictionnaire."],
      famille: ["🌳", "Ce mot, tu peux le retrouver",
        "Sa lettre muette s'entend dans un mot de la même famille."],
      accent: ["✏️", "C'est une question d'accent",
        "Le mot est bon : c'est seulement l'accent qui doit changer."],
    };
    const b = bandeaux[A.nature];
    const bandeau = b ? `<div class="lecon-nature ${A.nature}">
        <span class="lecon-nature-ico">${b[0]}</span>
        <span><b>${b[1]}</b><br>${b[2]}</span></div>` : "";

    cible.innerHTML = `<div class="lecon grande">
      <h4 style="background:${c}">${echapper(libelleCat(cat))}${motAff}</h4>
      <div class="corps">
        ${bandeau}
        <div class="lecon-question" style="border-color:${c}">
          <b style="color:${c}">💡 La question à te poser</b><br>${echapper(A.question || "")}
        </div>
        ${(A.pistes || []).length ? `
          <div class="lecon-soustitre" style="color:${c}">Des pistes</div>
          <ul>${A.pistes.map(p => `<li>${echapper(p)}</li>`).join("")}</ul>` : ""}
        <div class="aide-outils">
          ${A.lecon ? `<button class="btn btn-lecon" id="btn-lecon"
              data-id="${echapper(A.lecon.lecon_id)}">
              📘 Voir la leçon</button>` : ""}
          ${CATS_DICO.includes(cat) ? `<button class="btn fantome" id="btn-dico">
              🔎 Chercher ce mot</button>` : ""}
          ${cat === "conjugaison" ? `<button class="btn fantome" id="btn-conj">
              📖 Tableaux de conjugaison</button>` : ""}
          <button class="btn fantome" id="btn-indice">
            🆘 J'ai encore besoin d'un indice</button>
        </div>
        <div id="indice" class="lecon-indice" style="display:none;border-color:${c}"></div>
      </div></div>`;

    // Bouton leçon : n'apparaît que si une fiche du classeur correspond vraiment.
    const bl = $("#btn-lecon");
    if (bl) bl.onclick = () => this._ouvrirFicheClasseur(bl.dataset.id);

    // Le dictionnaire, sur les erreurs où il aide vraiment (orthographe,
    // homophones, lexique). Le mot choisi remplace le mot fautif dans le texte.
    const bd = $("#btn-dico");
    if (bd) bd.onclick = () => Dico.ouvrirFenetre(sig.mot || "",
      choisi => this._remplacerMot(sig, choisi));
    // Les tableaux de conjugaison sont ici, dans l'aide qui les concerne,
    // et non plus perdus dans la barre du bas.
    const bc = $("#btn-conj");
    if (bc) bc.onclick = () => this.conjugaison();

    const bi = $("#btn-indice");
    if (bi) bi.onclick = () => {
      const z = $("#indice");
      z.style.display = "block";
      z.innerHTML = `<b>Indice :</b> ${echapper(A.indice || "")}`;
      bi.style.display = "none";
      // L'indice est l'aide « directe » : on la compte pour l'autonomie.
      this.etat.aidePassage = true;
      this.etat.nbAides++;
    };
    // Une seule leçon est proposée : celle qui correspond exactement au cas.
    // En afficher cinq revenait à demander à l'élève de choisir — ce qu'il ne
    // sait pas faire, et ce qui le détourne de sa correction.
  },

  _ouvrirFicheClasseur(leconId) { return Classeur.ouvrir(leconId); },

  /* L'élève a choisi un mot dans le dictionnaire : on le pose à la place du
     mot fautif, dans SON texte. C'est bien lui qui corrige — l'application
     n'a fait que lui présenter les possibilités. */
  _remplacerMot(sig, choisi) {
    const zone = $("#zone");
    if (!zone || !choisi) return;
    const t = zone.value;
    // On se fie aux positions du repérage, en vérifiant qu'elles collent
    // encore : l'élève a pu modifier son texte entre-temps.
    const ok = sig && Number.isInteger(sig.debut) && Number.isInteger(sig.fin)
      && t.slice(sig.debut, sig.fin) === sig.mot;
    if (ok) {
      zone.value = t.slice(0, sig.debut) + choisi + t.slice(sig.fin);
    } else {
      const i = sig.mot ? t.indexOf(sig.mot) : -1;
      if (i === -1) { toast("Recopie le mot toi-même : " + choisi, 4000); return; }
      zone.value = t.slice(0, i) + choisi + t.slice(i + sig.mot.length);
    }
    this.etat.texteCourant = zone.value;
    // Le mot vient d'une recherche au dictionnaire : c'est une aide.
    this.etat.aidePassage = true;
    toast(`« ${choisi} » a remplacé « ${sig.mot} » dans ton texte.`, 3200);
    this.analyser(zone.value).then(() => {
      this.redessiner();
      if (this._duoBilan) this._duoBilan();
      if (this.panneau) this.panneau();
    });
  },

  async conjugaison() {
    const tabs = await API.get("/api/conjugaison");
    const cles = Object.keys(tabs);
    modale(`<div class="carte-titre">📖 Tableaux de conjugaison</div>
      <select id="sel-conj" style="margin:14px 0">
        ${cles.map(c => `<option>${echapper(c)}</option>`).join("")}</select>
      <div id="tab-conj" style="font-family:Consolas,monospace;font-size:15px;
           line-height:2.1"></div>
      <div class="rangee" style="margin-top:16px">
        <button class="btn doux" onclick="fermerModale()">Fermer</button></div>`);
    const afficher = () => {
      $("#tab-conj").innerHTML = tabs[$("#sel-conj").value]
        .map(l => `<div>${echapper(l)}</div>`).join("");
    };
    $("#sel-conj").onchange = afficher;
    afficher();
  },

  /* ---------------------------------------------------------------- Bilan */
  async bilan() {
    const final = this.etat.texteCourant ?? this.etat.texteInitial;
    await this.analyser(final);
    const apres = this.etat.nbCertaines;
    const detailApres = this.etat.parCategorie;
    const avant = this.etat.erreursAvant;
    const corrigees = Math.max(0, avant - apres);
    const nbAides = this.etat.nbAides;
    const cfg = Etat.ref.config || {};
    // « Sans aide » = tout ce que l'élève a corrigé pendant les DEUX étapes sans
    // surlignage (étapes 1 et 2). Si le réglage n'exige pas de pénaliser, on y
    // ajoute les corrections faites en passage sans avoir demandé d'indice.
    const penalise = cfg.aide_penalise_score !== false;
    let seul = this.etat.corrigeesSolo + (penalise ? 0 : this.etat.corrigeesPassageSeul);
    seul = Math.max(0, Math.min(seul, corrigees));
    const avecAide = Math.max(0, corrigees - seul);
    const secondes = Math.round((Date.now() - this.etat.debut) / 1000);
    const pct = avant ? Math.round(corrigees / avant * 100) : 100;
    const pctAuto = corrigees ? Math.round(seul / corrigees * 100) : 0;

    // Critères d'évaluation réglables par l'enseignant.
    const sReussi = +cfg.eval_seuil_reussi || 60;
    const sExcellent = +cfg.eval_seuil_excellent || 90;
    const objAuto = +cfg.eval_objectif_autonomie || 60;
    const felicit = (apres === 0 && avant > 0) ? "🏆 Bravo, tu as tout corrigé !"
      : pct >= sExcellent ? "🌟 Excellent travail !"
      : pct >= sReussi ? "👏 Beau travail !"
      : "💪 Continue, tu progresses !";
    const bonusAuto = (cfg.eval_bonus_sans_aide !== false && corrigees > 0 && pctAuto >= objAuto)
      ? `<div style="font-size:15px;color:var(--bleu);font-weight:600;margin-top:8px">
           🎯 Objectif d'autonomie atteint : ${pctAuto}% corrigé sans aide !</div>` : "";

    const cats = [...new Set([...Object.keys(this.etat.detailAvant),
                              ...Object.keys(detailApres)])];

    // Le bilan est AFFICHÉ D'ABORD. L'enregistrement vient ensuite : même s'il
    // échoue, l'élève voit son résultat — il ne doit jamais disparaître.
    $("#contenu").innerHTML =
      `<div class="frise">${this.PASSAGES.map(x =>
        `<div class="etape fait">✓ ${x.ico} ${x.titre}</div>`).join("")}</div>` +
      `<div class="bilan-bravo">
        <div class="bilan-felicit">${felicit}</div>
        ${bonusAuto}
        <div class="bilan-jauge">
          <div class="bilan-jauge-rempli" style="width:${pct}%"></div>
          <span class="bilan-jauge-txt">${pct}% des erreurs corrigées</span>
        </div>
      </div>

      <div class="bilan-grand">
        <div class="bilan-case depart">
          <div class="bilan-case-l">Erreurs au départ</div>
          <div class="bilan-case-v">${avant}</div>
        </div>
        <div class="bilan-fleche">→</div>
        <div class="bilan-case corrigees">
          <div class="bilan-case-l">J'ai corrigé</div>
          <div class="bilan-case-v">${corrigees}</div>
        </div>
        <div class="bilan-case restantes">
          <div class="bilan-case-l">Il reste</div>
          <div class="bilan-case-v">${apres}</div>
        </div>
      </div>

      <div class="bilan-second">
        <div class="bilan-mini"><div class="v" style="color:var(--bleu)">${pctAuto}%</div>
          <div class="l">corrigées <b>sans aide</b></div></div>
        <div class="bilan-mini"><div class="v" style="color:var(--ambre)">${nbAides}</div>
          <div class="l">indice${nbAides > 1 ? "s" : ""} utilisé${
            nbAides > 1 ? "s" : ""}</div></div>
        <div class="bilan-mini"><div class="v">${duree(secondes)}</div>
          <div class="l">temps passé</div></div>
      </div>

      <div class="carte bilan-cats">
        <div class="bilan-cats-titre">Mes erreurs, catégorie par catégorie</div>
        <div class="bilan-cats-grille">
          ${cats.length ? cats.map(c => {
            const a = this.etat.detailAvant[c] || 0, b = detailApres[c] || 0;
            const fini = b === 0 && a > 0;
            return `<div class="bilan-cat ${fini ? "fini" : ""}"
              style="--c:${couleurCat(c)}">
              <div class="bilan-cat-nom">${libelleCat(c)}</div>
              <div class="bilan-cat-chiffres">
                <span class="av">${a}</span>
                <span class="fl">→</span>
                <span class="ap" style="color:${b < a ? "var(--vert)"
                  : "var(--texte-doux)"}">${b}</span>
              </div>
              <div class="bilan-cat-etat">${fini ? "✅ tout corrigé"
                : b < a ? `👍 ${a - b} corrigée(s)` : "à retravailler"}</div>
            </div>`;
          }).join("") : `<div class="vide">Aucune erreur détectée. 🎉</div>`}
        </div>
      </div>
      <div id="etat-enr" style="color:var(--texte-doux);font-size:12.5px;
           margin-bottom:14px"></div>
      <div class="rangee">
        <button class="btn doux grand" id="menu">🏠 Retour au menu</button>
        <button class="btn grand pousse" id="autre">🔁 Corriger un autre texte</button>
      </div>`;

    $("#menu").onclick = () => Nav.aller("hub");
    $("#autre").onclick = () => this.sources();

    // Mots encore en erreur (lexique/orthographe/homophone) : alimentent la
    // banque lexicale personnelle de l'élève, pas une liste générique.
    const CATS_LEXICALES = ["lexique", "orthographe", "homophone"];
    const motsRestants = this.etat.sigs
      .filter(s => s.certain && CATS_LEXICALES.includes(s.categorie) && s.mot)
      .map(s => ({ mot: s.mot, categorie: s.categorie }));

    // Photo des réussites AVANT d'enregistrer : on pourra ainsi annoncer à
    // l'élève celles qu'il vient de débloquer avec ce texte-ci.
    let badgesAvant = [];
    try {
      const b0 = await API.get(`/api/eleve/${Etat.eleve.id}/bilan`);
      badgesAvant = (b0.badges || []).filter(x => x.obtenu).map(x => x.cle);
    } catch (e) { /* sans importance */ }

    // Enregistrement, protégé : un échec ne fait pas disparaître le bilan.
    try {
      const r = await API.post("/api/seance/correction", {
        eleve_id: Etat.eleve.id, origine: this.etat.origine,
        texte_id: this.etat.texteId, texte_initial: this.etat.texteInitial,
        texte_reference: this.etat.reference, texte_final: final,
        erreurs_avant: avant, erreurs_apres: apres,
        corrigees_seul: seul, corrigees_avec_aide: avecAide, nb_aides: nbAides,
        detail_avant: this.etat.detailAvant, detail_apres: detailApres,
        duree_secondes: secondes, etape_atteinte: this.PASSAGES.length, terminee: 1,
        mots_restants: motsRestants
      });
      $("#etat-enr").textContent = r.enregistre
        ? "✓ Résultat enregistré."
        : "⚠ Le résultat n'a pas pu être enregistré : " + (r.erreur || "");
      if (r.enregistre) this._feterNouveauxBadges(badgesAvant);
    } catch (e) {
      $("#etat-enr").textContent = "⚠ Le résultat n'a pas pu être enregistré.";
    }
  },

  /* Ce texte vient-il de débloquer une réussite ? Si oui, on le fête tout de
     suite : c'est le moment où l'élève est le plus réceptif. */
  async _feterNouveauxBadges(badgesAvant) {
    try {
      const b = await API.get(`/api/eleve/${Etat.eleve.id}/bilan`);
      const nouveaux = (b.badges || [])
        .filter(x => x.obtenu && !badgesAvant.includes(x.cle));
      if (!nouveaux.length) return;
      const zone = $("#etat-enr");
      if (!zone) return;
      zone.insertAdjacentHTML("beforebegin", `
        <div class="nouveaux-badges">
          <div class="nb-titre">🎉 ${nouveaux.length > 1
            ? "Nouvelles réussites débloquées !" : "Nouvelle réussite débloquée !"}</div>
          <div class="nb-liste">${nouveaux.map(x => `
            <div class="nb-badge">
              <span class="nb-emo">${x.emoji}</span>
              <span><b>${echapper(x.titre)}</b><br>
                <span class="nb-obj">${echapper(x.objectif)}</span></span>
            </div>`).join("")}</div>
          <button class="btn fantome" id="nb-voir">🏆 Voir tout mon bilan</button>
        </div>`);
      const bt = $("#nb-voir");
      if (bt) bt.onclick = () => Nav.aller("bilan");
    } catch (e) { /* la fête est un bonus, jamais un blocage */ }
  }
};
