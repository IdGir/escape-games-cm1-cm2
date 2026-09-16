/* MODULE — Ma dictée : une dictée fabriquée à partir de MES erreurs.

   La dictée de classe est la même pour tous. Celle-ci est faite des mots que
   l'élève rate vraiment, et de ceux qu'il est allé chercher au dictionnaire.

   La voix est celle de Windows (synthèse vocale du navigateur). Si aucune voix
   française n'est installée, on bascule sur un mode « le mot s'affiche
   quelques secondes puis disparaît » : l'exercice reste faisable partout. */

const Dictee = {
  etat: null,
  voix: null,
  voixDispo: false,

  /* ------------------------------------------------------------------ Voix */
  voixFr: [],

  _chargerVoix() {
    if (!("speechSynthesis" in window)) { this.voixDispo = false; return; }
    const toutes = window.speechSynthesis.getVoices() || [];
    this.voixFr = toutes.filter(v => /^fr/i.test(v.lang));
    // Windows 11 propose des voix « Natural » nettement meilleures que les
    // anciennes : on les met d'office en tête.
    this.voixFr.sort((a, b) => {
      const nat = v => /natural|neural/i.test(v.name) ? 0 : 1;
      return nat(a) - nat(b) || a.name.localeCompare(b.name);
    });
    // Choix mémorisé par l'élève ou l'enseignant, sinon la meilleure trouvée.
    let choisie = null;
    try {
      const nom = localStorage.voixDictee;
      if (nom) choisie = this.voixFr.find(v => v.name === nom) || null;
    } catch (e) { /* stockage indisponible */ }
    this.voix = choisie || this.voixFr[0] || null;
    this.voixDispo = !!this.voix;
  },

  _choisirVoix(nom) {
    const v = this.voixFr.find(x => x.name === nom);
    if (!v) return;
    this.voix = v;
    try { localStorage.voixDictee = nom; } catch (e) { /* tant pis */ }
  },

  _prononcer(texte, surFin) {
    if (!this.voixDispo) { if (surFin) surFin(); return; }
    try {
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(texte);
      u.voice = this.voix;
      u.lang = this.voix.lang || "fr-FR";
      u.rate = this.etat && this.etat.vitesse ? this.etat.vitesse : 0.85;
      u.onend = () => { if (surFin) surFin(); };
      window.speechSynthesis.speak(u);
    } catch (e) { if (surFin) surFin(); }
  },

  /* ------------------------------------------ Choix du mode et du niveau
     Trois façons de dicter, parce qu'un mot seul et une phrase ne posent pas
     du tout les mêmes problèmes. */
  mode: "mots",
  niveau: 2,

  async choisir() {
    const r = await API.get("/api/dictee/modes");
    const modes = r.modes || {};
    const bilan = await API.get(`/api/eleve/${Etat.eleve.id}/bilan`)
      .catch(() => ({}));
    const faits = bilan.dictee_par_mode || {};

    $("#contenu").innerHTML =
      page("✍️ Ma dictée", "Choisis ce que tu veux écrire aujourd'hui.") +
      `<div class="modes-dictee">
        ${Object.entries(modes).map(([cle, m]) => {
          const f = faits[cle] || { nb: 0, meilleur: 0 };
          return `<div class="mode-carte" data-mode="${cle}">
            <div class="mode-emo">${m.emoji}</div>
            <div class="mode-nom">${echapper(m.nom)}</div>
            <div class="mode-expli">${echapper(m.explication)}</div>
            <div class="mode-suivi">${f.nb
              ? `${f.nb} dictée(s) · meilleur : <b>${f.meilleur}%</b>`
              : "jamais essayé"}</div>
            <div class="mode-niveaux">
              ${Object.entries(m.niveaux).map(([n, cfg]) => `
                <button class="btn fantome niv-btn" data-mode="${cle}" data-niv="${n}">
                  ${echapper(cfg.nom)}<br><span class="niv-nb">${cfg.nb} items</span>
                </button>`).join("")}
            </div>
          </div>`;
        }).join("")}
      </div>
      <div class="rangee" style="margin-top:18px">
        <button class="btn doux" id="d-retour">🏠 Retour au menu</button>
      </div>`;
    $("#d-retour").onclick = () => Nav.aller("hub");
    $$(".niv-btn").forEach(b => b.onclick = () => {
      this.mode = b.dataset.mode;
      this.niveau = +b.dataset.niv;
      this.ecran();
    });
  },

  /* ------------------------------------------------------------- Préparation */
  async ecran() {
    this._chargerVoix();
    // Sur certains systèmes la liste des voix arrive avec un temps de retard.
    if (!this.voixDispo && "speechSynthesis" in window) {
      await new Promise(r => {
        window.speechSynthesis.onvoiceschanged = () => r();
        setTimeout(r, 700);
      });
      this._chargerVoix();
    }

    $("#contenu").innerHTML =
      page("✍️ Ma dictée", "Une dictée rien que pour toi, avec les mots que tu rates.") +
      `<div class="vide"><span class="chargement"></span> Je prépare ta dictée…</div>`;

    const d = await API.get(`/api/eleve/${Etat.eleve.id}/dictee`
      + `?mode=${this.mode}&niveau=${this.niveau}`);
    if (d.erreur || !d.mots.length) {
      $("#contenu").innerHTML = page("✍️ Ma dictée", "") +
        `<div class="vide">Impossible de préparer la dictée pour l'instant.<br><br>
          <button class="btn" onclick="Dictee.choisir()">← Choisir un autre mode</button>
        </div>`;
      return;
    }

    this.etat = {
      mots: d.mots, i: 0, reponses: [], debut: Date.now(),
      vitesse: 0.85, ecoutes: 0, lecture: this.voixDispo ? "voix" : "flash",
      mode: this.mode, niveau: this.niveau,
      groupe: this.mode !== "mots",
      explicationMode: d.explication_mode || "",
    };

    $("#contenu").innerHTML =
      page("✍️ Ma dictée", "Une dictée rien que pour toi.") +
      `<div class="carte dictee-accueil">
        <div class="dictee-accueil-emo">✍️</div>
        <h3>${d.mots.length} ${this.mode === "phrases" ? "phrases"
          : (this.mode === "expressions" ? "expressions" : "mots")} à écrire</h3>
        <p class="dictee-expli">${echapper(d.explication_mode || "")}</p>
        <p class="dictee-expli">${echapper(d.explication)}</p>
        ${this.voixDispo
          ? `<p class="dictee-mode">🔊 Chaque mot sera lu à voix haute.
               Tu pourras le réécouter autant de fois que tu veux.</p>
             <div class="rangee dictee-vitesse">
               <span class="champ" style="margin:0">Vitesse de la voix</span>
               <button class="mini" data-v="0.7">Lente</button>
               <button class="mini actif" data-v="0.85">Normale</button>
               <button class="mini" data-v="1">Rapide</button>
               <button class="mini" id="essai-voix">🔊 Essayer</button>
             </div>
             ${this.voixFr.length > 1 ? `
               <div class="rangee dictee-vitesse">
                 <span class="champ" style="margin:0">Voix</span>
                 <select id="choix-voix" style="width:auto;min-width:220px">
                   ${this.voixFr.map(v => `<option value="${echapper(v.name)}"
                     ${v === this.voix ? "selected" : ""}>${echapper(v.name)}
                     ${/natural|neural/i.test(v.name) ? " ⭐" : ""}</option>`).join("")}
                 </select>
               </div>` : ""}`
          : `<div class="dictee-sans-voix">
               <b>Aucune voix française n'est installée sur cet ordinateur.</b>
               La dictée fonctionne quand même : chaque mot s'affichera
               quelques secondes, puis disparaîtra — à toi de le réécrire de
               mémoire. Ton maître peut aussi te le lire.
             </div>`}
        <button class="btn xl" id="dictee-start">Commencer →</button>
      </div>`;

    $$(".dictee-vitesse .mini[data-v]").forEach(b => b.onclick = () => {
      $$(".dictee-vitesse .mini[data-v]").forEach(x => x.classList.remove("actif"));
      b.classList.add("actif");
      this.etat.vitesse = parseFloat(b.dataset.v);
    });
    if ($("#essai-voix")) $("#essai-voix").onclick = () =>
      this._prononcer("Voici ma voix. Écoute bien chaque mot.");
    if ($("#choix-voix")) $("#choix-voix").onchange = ev => {
      this._choisirVoix(ev.target.value);
      this._prononcer("Voici ma voix.");
    };
    $("#dictee-start").onclick = () => this.motSuivant();
  },

  /* ---------------------------------------------------------------- Dictée */
  motSuivant() {
    const e = this.etat;
    if (e.i >= e.mots.length) return this.bilan();
    const item = e.mots[e.i];
    e.ecoutes = 0;

    $("#contenu").innerHTML = `
      <div class="dictee-barre">
        <div class="dictee-progres">
          <div style="width:${Math.round(e.i / e.mots.length * 100)}%"></div>
        </div>
        <span class="dictee-compte">Mot ${e.i + 1} sur ${e.mots.length}</span>
      </div>
      <div class="carte dictee-scene">
        <div class="dictee-consigne">Écoute, puis écris le mot.</div>
        <div class="dictee-boutons">
          <button class="btn xl dictee-ecouter" id="d-ecouter">
            🔊 ${e.lecture === "voix" ? "Écouter" : "Montrer"}</button>
          ${item.phrase ? `<button class="btn fantome" id="d-phrase">
            💬 Écouter la phrase entière</button>` : ""}
        </div>
        <div id="d-affichage" class="dictee-affichage"></div>
        <label class="champ" for="d-saisie" style="margin-top:20px">Ce que j'écris</label>
        <input type="text" id="d-saisie" class="dictee-champ" autocomplete="off"
          spellcheck="false" placeholder="écris le mot ici">
        <div class="dictee-actions">
          <button class="btn grand" id="d-valider">Je valide →</button>
          <button class="btn doux" id="d-passer">Je ne sais pas, je passe</button>
        </div>
        <div class="dictee-astuce">
          ${item.nature ? `Indice : c'est un <b>${echapper(item.nature)}</b>.` : ""}
        </div>
      </div>`;

    const champ = $("#d-saisie");
    champ.focus();
    champ.onkeydown = ev => { if (ev.key === "Enter") this.valider(); };
    $("#d-valider").onclick = () => this.valider();
    $("#d-passer").onclick = () => this.valider(true);
    $("#d-ecouter").onclick = () => this.ecouter(item);
    if ($("#d-phrase")) $("#d-phrase").onclick = () => this.ecouter(item, true);

    // Première écoute automatique, après un court instant.
    setTimeout(() => this.ecouter(item), 450);
  },

  ecouter(item, phraseEntiere) {
    this.etat.ecoutes++;
    const quoi = (phraseEntiere && item.phrase) ? item.phrase : (item.contenu || item.mot);
    if (this.etat.lecture === "voix") {
      this._prononcer(quoi);
      if (phraseEntiere) {
        // On répète le mot seul après la phrase : c'est lui qu'il faut écrire.
        setTimeout(() => this._prononcer(item.contenu || item.mot), 200);
      }
      return;
    }
    // Sans voix : le mot s'affiche quelques secondes, puis disparaît.
    const zone = $("#d-affichage");
    if (!zone) return;
    zone.innerHTML = `<div class="dictee-flash">${echapper(quoi)}</div>`;
    let reste = 4;
    const tic = setInterval(() => {
      reste--;
      const f = $(".dictee-flash");
      if (!f) { clearInterval(tic); return; }
      if (reste <= 0) { clearInterval(tic); zone.innerHTML =
        `<div class="dictee-cache">À toi d'écrire !</div>`; }
    }, 1000);
  },

  async valider(passe) {
    const e = this.etat;
    const item = e.mots[e.i];
    const attendu = item.contenu || item.mot;
    const saisi = passe ? "" : $("#d-saisie").value.trim();
    // Une expression ou une phrase se corrige mot par mot : l'élève doit voir
    // lesquels sont justes, pas seulement « c'est faux ».
    const v = e.groupe
      ? await API.post("/api/dictee/verifier-groupe", { attendu, saisi })
      : await API.post("/api/dictee/verifier", { attendu, saisi });

    e.reponses.push({
      attendu, saisi, juste: v.juste, genre: v.genre,
      conseil: v.conseil, categorie: item.categorie, origine: item.origine,
      detail: v.detail || null, ecoutes: e.ecoutes,
    });
    this._retour(v, item, () => { e.i++; this.motSuivant(); });
  },

  /* Retour immédiat : l'élève doit savoir tout de suite, pas à la fin. */
  _retour(v, item, suite) {
    const scene = $(".dictee-scene");
    if (!scene) { suite(); return; }
    scene.insertAdjacentHTML("beforeend", `
      <div class="dictee-retour ${v.juste ? "juste" : v.genre}">
        <div class="dr-haut">
          <span class="dr-emo">${v.juste ? "✅" : (v.genre === "accent" ? "✏️" : "🔎")}</span>
          <span class="dr-titre">${v.juste ? "Juste !" : "Pas encore"}</span>
        </div>
        ${v.juste ? "" : `<div class="dr-mot">
          ${v.detail
            ? `C'était : <b>${v.detail.map(x =>
                `<span class="dr-${x.etat}">${echapper(x.mot)}</span>`).join(" ")}</b>`
            : `Le mot était : <b>${echapper(item.contenu || item.mot)}</b>`}</div>`}
        ${v.conseil ? `<div class="dr-conseil">${echapper(v.conseil)}</div>` : ""}
        <button class="btn grand" id="dr-suite">Mot suivant →</button>
      </div>`);
    $("#d-valider").disabled = true;
    $("#d-passer").disabled = true;
    $("#d-saisie").disabled = true;
    const b = $("#dr-suite");
    b.focus();
    b.onclick = suite;
    b.scrollIntoView({ behavior: "smooth", block: "nearest" });
  },

  /* ----------------------------------------------------------------- Bilan */
  async bilan() {
    const e = this.etat;
    const secondes = Math.round((Date.now() - e.debut) / 1000);

    let badgesAvant = [];
    try {
      const b0 = await API.get(`/api/eleve/${Etat.eleve.id}/bilan`);
      badgesAvant = (b0.badges || []).filter(x => x.obtenu).map(x => x.cle);
    } catch (err) { /* sans importance */ }

    const r = await API.post("/api/seance/dictee", {
      eleve_id: Etat.eleve.id, reponses: e.reponses, duree_secondes: secondes,
      mode: e.mode, niveau: e.niveau });
    const b = (r && r.bilan) || { score: 0, justes: 0, total: e.reponses.length,
                                  message: "", par_genre: {} };

    const g = b.par_genre || {};
    const cartes = [
      ["orthographe", "🔤", "Le bon son, la mauvaise écriture",
       "Tu entends bien le mot, mais tu ne sais pas encore l'écrire."],
      ["accent", "✏️", "Seulement les accents",
       "Le mot est bon, il ne manque que les accents."],
      ["proche", "🔍", "Presque le bon mot",
       "Un seul son ne va pas : il faut réécouter plus lentement."],
      ["ecoute", "👂", "Un autre mot",
       "Le mot écrit n'est pas celui qui a été dicté."],
    ].filter(([cle]) => g[cle]);

    $("#contenu").innerHTML =
      `<div class="dictee-bravo">
        <div class="dictee-score">${b.score}%</div>
        <div class="dictee-score-l">${b.justes} mot(s) juste(s) sur ${b.total}</div>
        <div class="dictee-message">${echapper(b.message)}</div>
      </div>
      ${cartes.length ? `<div class="carte">
        <div class="carte-titre">Mes erreurs, et ce qu'elles veulent dire</div>
        <div class="dictee-genres">
          ${cartes.map(([cle, emo, titre, expli]) => `
            <div class="dictee-genre">
              <div class="dg-emo">${emo}</div>
              <div class="dg-n">${g[cle]}</div>
              <div class="dg-t">${titre}</div>
              <div class="dg-e">${expli}</div>
            </div>`).join("")}
        </div>
      </div>` : ""}
      <div class="carte">
        <div class="carte-titre">Mot par mot</div>
        <div class="dictee-liste">
          ${e.reponses.map(x => `
            <div class="dictee-ligne ${x.juste ? "juste" : "faux"}">
              <span class="dl-etat">${x.juste ? "✅" : "❌"}</span>
              <span class="dl-mot">${echapper(x.attendu)}</span>
              ${x.juste ? "" : `<span class="dl-saisi">tu as écrit :
                <i>${echapper(x.saisi || "rien")}</i></span>`}
              ${!x.juste && !/\s/.test(x.attendu) ? `<button class="mini dl-dico"
                data-mot="${echapper(x.attendu)}">🔎 Voir ce mot</button>` : ""}
            </div>`).join("")}
        </div>
      </div>
      <div id="dictee-badges"></div>
      <div class="rangee" style="margin-top:18px">
        <button class="btn doux grand" id="d-menu">🏠 Retour au menu</button>
        <button class="btn grand pousse" id="d-encore">🔁 Une autre dictée</button>
      </div>`;

    $("#d-menu").onclick = () => Nav.aller("hub");
    $("#d-encore").onclick = () => this.choisir();
    $$(".dl-dico").forEach(x => x.onclick = () =>
      Dico.ouvrirFenetre(x.dataset.mot));

    this._feterBadges(badgesAvant);
  },

  async _feterBadges(badgesAvant) {
    try {
      const b = await API.get(`/api/eleve/${Etat.eleve.id}/bilan`);
      const nouveaux = (b.badges || [])
        .filter(x => x.obtenu && !badgesAvant.includes(x.cle));
      if (!nouveaux.length) return;
      $("#dictee-badges").innerHTML = `
        <div class="nouveaux-badges">
          <div class="nb-titre">🎉 ${nouveaux.length > 1
            ? "Nouvelles réussites débloquées !" : "Nouvelle réussite débloquée !"}</div>
          <div class="nb-liste">${nouveaux.map(x => `
            <div class="nb-badge"><span class="nb-emo">${x.emoji}</span>
              <span><b>${echapper(x.titre)}</b><br>
                <span class="nb-obj">${echapper(x.objectif)}</span></span>
            </div>`).join("")}</div>
        </div>`;
    } catch (e) { /* bonus, jamais bloquant */ }
  }
};
