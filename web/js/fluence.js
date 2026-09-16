/* MODULE 2 — Fluence de lecture. */

const Fluence = {
  etat: {},

  async niveaux() {
    const parNiveau = {};
    for (let n = 1; n <= 5; n++)
      parNiveau[n] = await API.get("/api/textes/fluence?niveau=" + n);

    $("#contenu").innerHTML =
      page("Je lis à voix haute", "Choisis un niveau, puis un texte. Lis-le à voix haute le mieux possible : ni trop vite, ni trop lentement.") +
      `<div class="rangee" style="gap:12px;margin-bottom:22px">
        ${[1,2,3,4,5].map(n => {
          const info = Etat.ref.niveaux_fluence[n];
          const nb = parNiveau[n].length;
          return `<div class="tuile" data-niv="${n}" style="min-width:0;padding:18px 10px">
            <div style="font-size:32px;font-weight:800;color:${info.couleur}">${n}</div>
            <div style="font-weight:600;font-size:13px">${info.libelle.split("—")[1].trim()}</div>
            <p style="font-size:12px">${nb} texte${nb > 1 ? "s" : ""}</p>
          </div>`;
        }).join("")}
      </div>
      <div id="liste-textes"><div class="vide">👆 Choisis d'abord un niveau.</div></div>`;

    $$("[data-niv]").forEach(x => x.onclick = () => {
      const n = +x.dataset.niv;
      $$("[data-niv]").forEach(y => y.style.borderColor = "var(--bordure)");
      x.style.borderColor = Etat.ref.niveaux_fluence[n].couleur;
      this.listerTextes(parNiveau[n]);
    });
  },

  listerTextes(textes) {
    const afficherMots = Etat.ref.config.fluence_afficher_nb_mots;
    if (!textes.length) {
      $("#liste-textes").innerHTML =
        `<div class="vide">Aucun texte à ce niveau pour l'instant.</div>`;
      return;
    }
    $("#liste-textes").innerHTML = `
      <div class="carte-titre" style="margin-bottom:12px">Choisis ton texte</div>
      <div class="tuiles">
        ${textes.map((t, i) => `
          <div class="tuile" data-i="${i}" style="min-width:200px;padding:20px">
            <h3 style="margin-top:0;font-size:15px">${echapper(t.titre)}</h3>
            ${afficherMots ? `<p>${t.nb_mots} mots</p>` : ""}
          </div>`).join("")}
      </div>`;
    $$("[data-i]", $("#liste-textes")).forEach(x =>
      x.onclick = () => this.lire(textes[+x.dataset.i]));
  },

  /* --------------------------------------------------- Lecture en autonomie
     Quand l'enseignant l'a activée, l'ordinateur écoute, transcrit, et compte
     lui-même les mots correctement lus. L'élève peut alors s'entraîner seul.
     Sans cela — ou si le micro est refusé — on retombe sur le comptage à la
     main, exactement comme avant. */
  _auto: null,
  _micro: null,

  async _etatAuto() {
    if (this._auto !== null) return this._auto;
    try {
      this._auto = await API.get("/api/fluence/auto/etat");
    } catch (e) {
      this._auto = { active: false, reglee: false };
    }
    return this._auto;
  },

  _peutEnregistrer() {
    return !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia
              && window.MediaRecorder);
  },

  async _demarrerMicro() {
    const flux = await navigator.mediaDevices.getUserMedia({ audio: true });
    const morceaux = [];
    const rec = new MediaRecorder(flux);
    rec.ondataavailable = e => { if (e.data && e.data.size) morceaux.push(e.data); };
    rec.start();
    this._micro = { rec, flux, morceaux };
  },

  _arreterMicro() {
    return new Promise(resolve => {
      const m = this._micro;
      if (!m) return resolve(null);
      m.rec.onstop = () => {
        m.flux.getTracks().forEach(t => t.stop());
        this._micro = null;
        resolve(new Blob(m.morceaux, { type: "audio/webm" }));
      };
      try { m.rec.stop(); } catch (e) { resolve(null); }
    });
  },

  /* ------------------------------------------------------------- La lecture */
  lire(texte) {
    this.etat = { texte, t0: null, secondes: 0, minuteur: null, auto: false };
    const info = Etat.ref.niveaux_fluence[texte.niveau];
    const p = Confort.charger();

    $("#contenu").innerHTML =
      page(texte.titre, "Appuie sur Démarrer, lis à voix haute, puis appuie sur J'ai fini.") +
      `<div class="rangee" style="margin-bottom:12px">
        <span class="puce" style="background:${info.couleur}">Niveau ${texte.niveau}</span>
        ${Etat.ref.config.fluence_afficher_nb_mots
          ? `<span style="color:var(--texte-doux)">${texte.nb_mots} mots</span>` : ""}
      </div>
      <div class="editeur">
        ${Confort.barre(true)}
        <div class="lecture ${p.lignes ? "ligne-alt-on" : ""} ${p.regle ? "regle-on" : ""}"
             id="texte-lecture"></div>
      </div>
      <div class="carte" style="margin-top:18px">
        <div class="rangee">
          <button class="btn doux" id="retour">← Choisir un autre texte</button>
          <span class="chrono" id="chrono" style="margin-left:20px">0′00″</span>
          <button class="btn vert xl pousse" id="chrono-btn">▶ &nbsp;DÉMARRER LA LECTURE</button>
        </div>
        <div id="zone-auto" style="margin-top:10px"></div>
      </div>`;

    Confort.brancher(() => this.rendreTexte());
    this.rendreTexte();
    $("#retour").onclick = () => this.niveaux();
    $("#chrono-btn").onclick = () => this.basculer();
    this._proposerAuto();
  },

  /* Propose l'écoute automatique si elle est réglée et que le micro existe. */
  async _proposerAuto() {
    const zone = $("#zone-auto");
    if (!zone) return;
    const a = await this._etatAuto();
    if (!a.reglee || !this._peutEnregistrer()) {
      zone.innerHTML = `<div class="auto-note">
        L'élève ou l'enseignant appuie sur le bouton, puis compte les erreurs
        à la fin.</div>`;
      return;
    }
    zone.innerHTML = `
      <label class="inter auto-choix">
        <input type="checkbox" id="opt-auto" checked>
        <span><b>🎙️ L'ordinateur m'écoute et compte tout seul</b><br>
          <span class="auto-detail">Ta voix est envoyée à
            ${echapper(a.service)} le temps de reconnaître les mots, puis elle
            est effacée. Décoche si tu préfères compter avec le maître.</span>
        </span></label>`;
  },

  rendreTexte() {
    const zone = $("#texte-lecture");
    if (!zone) return;
    const p = Confort.charger();
    const t = this.etat.texte.contenu;
    const lignes = t.split(/\n/);
    const rendre = s => p.syllabes ? Confort.colorerSyllabes(s) : echapper(s);
    zone.innerHTML = lignes.map(l => `<div class="lg">${rendre(l)}</div>`).join("");
    zone.classList.toggle("ligne-alt-on", p.lignes);
    zone.classList.toggle("regle-on", p.regle);
  },

  async basculer() {
    if (this.etat.t0 === null) {
      // Le micro d'abord : si l'élève refuse, on continue sans, sans drame.
      const veutAuto = $("#opt-auto") && $("#opt-auto").checked;
      if (veutAuto) {
        try {
          await this._demarrerMicro();
          this.etat.auto = true;
        } catch (e) {
          this.etat.auto = false;
          toast("Le micro n'est pas disponible : le comptage se fera à la main.",
                4500);
        }
      }
      this.etat.t0 = Date.now();
      const b = $("#chrono-btn");
      b.className = "btn rouge xl pousse";
      b.innerHTML = "⏹ &nbsp;J'AI FINI DE LIRE";
      if (this.etat.auto && $("#zone-auto"))
        $("#zone-auto").innerHTML = `<div class="auto-actif">
          <span class="auto-pastille"></span> Enregistrement en cours…</div>`;
      this.etat.minuteur = setInterval(() => {
        $("#chrono").textContent = duree((Date.now() - this.etat.t0) / 1000);
      }, 200);
    } else {
      clearInterval(this.etat.minuteur);
      this.etat.secondes = (Date.now() - this.etat.t0) / 1000;
      this.etat.t0 = null;
      const audio = this.etat.auto ? await this._arreterMicro() : null;
      if (this.etat.secondes < 3) {
        toast("La lecture a duré moins de 3 secondes. Recommence.");
        this.lire(this.etat.texte);
        return;
      }
      if (audio && audio.size > 2000) return this.analyserAudio(audio);
      this.saisirErreurs();
    }
  },

  /* Envoi de l'enregistrement, puis comparaison mot à mot. */
  async analyserAudio(audio) {
    const t = this.etat.texte;
    $("#contenu").innerHTML =
      page("J'écoute ta lecture… 🎧",
        "L'ordinateur compare ce que tu as lu au texte. Ça prend quelques secondes.") +
      `<div class="vide"><span class="chargement"></span>
        Analyse de l'enregistrement…</div>`;

    let r = null;
    try {
      const form = new FormData();
      form.append("audio", audio, "lecture.webm");
      form.append("texte_id", t.id);
      form.append("reference", t.contenu);
      form.append("secondes", this.etat.secondes);
      const rep = await fetch("/api/fluence/auto/analyser",
        { method: "POST", body: form });
      r = await rep.json();
    } catch (e) {
      r = { ok: false, message: "L'analyse n'a pas abouti." };
    }

    if (!r || !r.ok) {
      // Échec : on ne bloque jamais l'élève, on repasse au comptage manuel.
      toast((r && r.message) || "Analyse impossible.", 5000);
      this.saisirErreurs();
      return;
    }
    this.etat.analyse = r;
    this.resultatAuto(r);
  },

  /* Le compte rendu : le texte relu, chaque mot coloré selon ce qui a été
     entendu. C'est ce qui rend le résultat vérifiable d'un coup d'œil. */
  resultatAuto(r) {
    const t = this.etat.texte;
    $("#contenu").innerHTML =
      page("Ce que l'ordinateur a entendu",
        "Vérifie : tu peux corriger les chiffres avant d'enregistrer.") +
      `<div class="stats">
        <div class="stat"><div class="v" style="color:var(--cyan)">${
          Math.round(r.mclm)}</div>
          <div class="l">mots corrects par minute</div></div>
        <div class="stat"><div class="v" style="color:var(--vert)">${r.justes}</div>
          <div class="l">mots bien lus</div></div>
        <div class="stat"><div class="v" style="color:var(--orange)">${r.erreurs}</div>
          <div class="l">mots sautés ou remplacés</div></div>
        <div class="stat"><div class="v">${r.mots_lus} / ${r.nb_total}</div>
          <div class="l">mots atteints dans le texte</div></div>
      </div>

      <div class="carte">
        <div class="carte-titre">Ta lecture, mot par mot</div>
        <div class="carte-sous">
          <span class="lg-cle lu">bien lu</span>
          <span class="lg-cle remplace">autre mot entendu</span>
          <span class="lg-cle oublie">sauté</span>
          <span class="lg-cle non_lu">pas atteint</span>
        </div>
        <div class="relecture">${r.mots.map(m =>
          `<span class="mot-${m.etat}"${m.entendu
            ? ` title="entendu : ${echapper(m.entendu)}"` : ""}>${
            echapper(m.mot)}</span>`).join(" ")}</div>
        ${r.nb_ajouts ? `<div class="carte-sous" style="margin-top:12px">
          ${r.nb_ajouts} mot(s) en plus ont été entendus :
          <i>${echapper(r.ajouts.join(", "))}</i></div>` : ""}
      </div>

      <div class="avert-auto">⚠️ ${echapper(r.avertissement)}</div>

      <div class="carte" style="max-width:620px">
        <div class="carte-titre">Je vérifie et j'enregistre</div>
        <div class="grille g2">
          <div><label class="champ">Erreurs de lecture</label>
            <input type="number" id="err" min="0" value="${r.erreurs}"></div>
          <div><label class="champ">Mots réellement lus</label>
            <input type="number" id="lus" min="1" value="${r.mots_lus}"></div>
        </div>
        <div class="rangee" style="margin-top:18px">
          <button class="btn doux" id="refaire">🔁 Recommencer</button>
          <button class="btn pousse" id="voir">Voir mon score →</button>
        </div>
      </div>
      <div style="display:none">
        <input type="radio" name="qui" value="auto" checked>
      </div>`;
    $("#refaire").onclick = () => this.lire(t);
    $("#voir").onclick = () => this.resultat();
  },

  /* --------------------------------------------------- Saisie des erreurs */
  saisirErreurs() {
    const t = this.etat.texte;
    $("#contenu").innerHTML =
      page("Lecture terminée ⏱️", `Temps : ${duree(this.etat.secondes)}`) +
      `<div class="carte" style="max-width:620px">
        <div class="carte-titre">Combien de mots ont été mal lus ?</div>
        <div class="carte-sous">Un mot oublié, ajouté, inventé ou mal prononcé
          compte pour une erreur.</div>
        <div class="grille g2">
          <div><label class="champ">Erreurs de lecture</label>
            <input type="number" id="err" min="0" value="0"></div>
          <div><label class="champ">Mots réellement lus</label>
            <input type="number" id="lus" min="1" value="${t.nb_mots}">
            <div style="font-size:11.5px;color:var(--texte-pale);margin-top:4px">
              sur ${t.nb_mots} — à changer seulement si le texte n'a pas été fini
            </div></div>
        </div>
        <label class="champ" style="margin-top:14px">Qui a compté ?</label>
        <div class="rangee">
          <label class="inter"><input type="radio" name="qui" value="eleve" checked>
            L'élève</label>
          <label class="inter"><input type="radio" name="qui" value="enseignant">
            L'enseignant</label>
        </div>
        <div class="rangee" style="margin-top:20px">
          <button class="btn doux" id="refaire">🔁 Recommencer</button>
          <button class="btn pousse" id="voir">Voir mon score →</button>
        </div>
      </div>`;
    $("#refaire").onclick = () => this.lire(t);
    $("#voir").onclick = () => this.resultat();
  },

  /* ------------------------------------------------------------- Résultat */
  async resultat() {
    const t = this.etat.texte;
    const erreurs = Math.max(0, +$("#err").value || 0);
    const lus = Math.max(1, +$("#lus").value || t.nb_mots);
    const qui = $("input[name=qui]:checked").value;
    const minutes = Math.max(0.05, this.etat.secondes / 60);
    const mclm = Math.round(Math.max(0, lus - erreurs) / minutes * 10) / 10;

    const avant = await API.get(`/api/eleve/${Etat.eleve.id}/resume`);
    const niveau = Etat.eleve.classe_niveau || Etat.ref.config.fluence_niveau_classe;
    const repere = Etat.ref.reperes_mclm[niveau] || 90;
    const precision = Math.round(Math.max(0, lus - erreurs) / lus * 100);
    const record = mclm > avant.meilleur_mclm && avant.lectures > 0;
    const titre = record ? "🏆 Nouveau record personnel !"
      : mclm >= repere ? "🎉 Objectif atteint !" : "💪 Continue à t'entraîner !";
    const maxi = Math.max(mclm, repere) * 1.25;

    $("#contenu").innerHTML =
      `<div style="text-align:center;margin-bottom:22px">
        <div style="font-size:30px;font-weight:800;color:var(--vert)">${titre}</div>
      </div>
      <div class="carte" style="text-align:center;max-width:420px;margin:0 auto 20px">
        <div class="grand-score">${Math.round(mclm)}</div>
        <div style="color:var(--texte-doux);margin-top:6px">
          mots corrects lus par minute</div>
      </div>
      <div class="stats" style="max-width:760px;margin:0 auto 18px">
        <div class="stat"><div class="v">${duree(this.etat.secondes)}</div>
          <div class="l">temps de lecture</div></div>
        <div class="stat"><div class="v" style="color:var(--orange)">${erreurs}</div>
          <div class="l">erreur(s) de lecture</div></div>
        <div class="stat"><div class="v" style="color:var(--vert)">${precision}%</div>
          <div class="l">de mots bien lus</div></div>
        <div class="stat"><div class="v" style="color:var(--texte-doux)">${repere}</div>
          <div class="l">repère ${niveau}</div></div>
      </div>
      <div style="max-width:760px;margin:0 auto">
        <div class="jauge">
          <div class="rempli" style="width:${Math.min(100, mclm / maxi * 100)}%;
            background:${mclm >= repere ? "var(--vert)" : "var(--orange)"}"></div>
          <div class="repere" style="left:${repere / maxi * 100}%"></div>
        </div>
        <div style="color:var(--texte-doux);font-size:12px;text-align:center">
          le trait rouge est l'objectif de ta classe (${niveau})</div>
        <div class="rangee" style="margin-top:24px;justify-content:center">
          <button class="btn doux" id="menu">🏠 Menu</button>
          <button class="btn fantome" id="relire">🔁 Relire ce texte</button>
          <button class="btn" id="autre">📖 Un autre texte</button>
        </div>
        <div id="etat-enr" style="text-align:center;color:var(--texte-doux);
             font-size:12.5px;margin-top:14px"></div>
      </div>`;

    $("#menu").onclick = () => Nav.aller("hub");
    $("#relire").onclick = () => this.lire(t);
    $("#autre").onclick = () => this.niveaux();

    try {
      const r = await API.post("/api/seance/fluence", {
        eleve_id: Etat.eleve.id, texte_id: t.id, titre_texte: t.titre,
        niveau: t.niveau, nb_mots_texte: t.nb_mots, mots_lus: lus,
        erreurs, duree_secondes: Math.round(this.etat.secondes * 10) / 10,
        mclm, saisi_par: qui
      });
      $("#etat-enr").textContent = r.enregistre ? "✓ Score enregistré."
        : "⚠ Le score n'a pas pu être enregistré.";
    } catch { $("#etat-enr").textContent = "⚠ Le score n'a pas pu être enregistré."; }
  }
};
