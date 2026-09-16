/* MODULE — Mon dictionnaire : chercher un mot en l'écrivant comme on l'entend.

   Le principe pédagogique tient en une phrase : l'application ne corrige pas
   l'élève, elle lui propose et il choisit. C'est en lisant les définitions
   qu'il tranche entre « ver », « vers », « verre » et « vert ». */

const Dico = {
  _dernierEssai: "",
  _retour: null,          // où revenir quand on est appelé depuis « Je me corrige »

  /* Écran complet (menu de l'élève). */
  async ecran(prefill) {
    this._retour = null;
    const etat = await API.get("/api/dico/etat");
    $("#contenu").innerHTML =
      page("🔎 Mon dictionnaire",
        "Tu ne sais pas comment s'écrit un mot ? Écris-le comme tu l'entends.") +
      this._formulaire(etat) +
      `<div id="dico-resultats"></div>`;
    this._brancher();
    if (prefill) { $("#dico-essai").value = prefill; this.chercher(); }
    else $("#dico-essai").focus();
  },

  _formulaire(etat) {
    return `
      <div class="carte dico-boite">
        <label class="champ" for="dico-essai">Écris le mot comme tu l'entends</label>
        <div class="dico-ligne">
          <input type="text" id="dico-essai" class="dico-champ" autocomplete="off"
            spellcheck="false" placeholder="par exemple : éléfan, oizo, sitrouye…">
          <button class="btn grand" id="dico-go">Chercher</button>
        </div>
        <div class="dico-aide">
          Ce n'est pas grave si l'orthographe est fausse : l'application cherche
          les mots qui <b>sonnent pareil</b>.
          ${etat && etat.nb_mots
            ? `<span class="dico-compte">${etat.nb_mots.toLocaleString("fr-FR")}
               mots dans le dictionnaire</span>` : ""}
        </div>
      </div>`;
  },

  _brancher() {
    const champ = $("#dico-essai");
    $("#dico-go").onclick = () => this.chercher();
    champ.onkeydown = e => { if (e.key === "Enter") this.chercher(); };
    // Recherche automatique après une petite pause : l'élève voit les
    // propositions bouger pendant qu'il tape, c'est plus encourageant.
    let minuteur;
    champ.oninput = () => {
      clearTimeout(minuteur);
      minuteur = setTimeout(() => {
        if (champ.value.trim().length >= 3) this.chercher(true);
      }, 420);
    };
  },

  async chercher(silencieux) {
    const essai = $("#dico-essai").value.trim();
    const zone = $("#dico-resultats");
    if (essai.length < 2) { zone.innerHTML = ""; return; }
    this._dernierEssai = essai;
    if (!silencieux) zone.innerHTML =
      `<div class="vide"><span class="chargement"></span> Je cherche…</div>`;

    const r = await API.post("/api/dico/chercher", {
      essai, eleve_id: Etat.eleve ? Etat.eleve.id : null,
      depuis: this._retour ? "correction" : "dictionnaire", limite: 10 });

    if (!r.resultats.length) {
      zone.innerHTML = `<div class="dico-rien">
        <div class="dico-rien-emo">🤔</div>
        <b>Aucun mot ne correspond.</b>
        <p>Essaie d'écrire le mot autrement, en le prononçant lentement
           syllabe par syllabe. Ou demande à ton maître.</p></div>`;
      return;
    }

    const memeSon = r.resultats.filter(x => x.meme_son);
    zone.innerHTML = `
      ${r.bien_ecrit ? `<div class="dico-bravo">
        ✅ <b>« ${echapper(essai)} » existe et s'écrit bien comme ça.</b>
        Tu peux quand même lire sa définition ci-dessous.</div>` : ""}
      <div class="dico-intro">
        ${memeSon.length
          ? `<b>${memeSon.length} mot${memeSon.length > 1 ? "s" : ""}</b> se
             prononce${memeSon.length > 1 ? "nt" : ""} exactement comme ce que
             tu as écrit. Clique sur un mot pour lire ce qu'il veut dire.`
          : `Voici les mots les plus proches. Clique sur un mot pour lire ce
             qu'il veut dire.`}
      </div>
      <div class="dico-liste">
        ${r.resultats.map((x, i) => `
          <button class="dico-mot ${x.meme_son ? "meme-son" : ""}" data-mot="${echapper(x.mot)}">
            <span class="dico-rang">${i + 1}</span>
            <span class="dico-mot-txt">
              <span class="dico-mot-nom">${echapper(x.mot)}</span>
              <span class="dico-mot-nat">${echapper(x.nature)}</span>
            </span>
            ${x.meme_son ? `<span class="dico-etiq">même son</span>` : ""}
            <span class="dico-jauge" title="${x.score} sur 100">
              <span style="width:${Math.round(x.score)}%"></span></span>
          </button>`).join("")}
      </div>
      <div id="dico-fiche"></div>`;

    $$(".dico-mot").forEach(b =>
      b.onclick = () => this.voirMot(b.dataset.mot, b));
  },

  async voirMot(mot, bouton) {
    $$(".dico-mot").forEach(b => b.classList.toggle("choisi", b === bouton));
    const zone = $("#dico-fiche");
    zone.innerHTML = `<div class="dico-def"><span class="chargement"></span>
      Je cherche la définition…</div>`;
    const d = await API.post("/api/dico/definition", {
      mot, eleve_id: Etat.eleve ? Etat.eleve.id : null,
      essai: this._dernierEssai,
      depuis: this._retour ? "correction" : "dictionnaire" });

    zone.innerHTML = `
      <div class="dico-def">
        <div class="dico-def-haut">
          <div>
            <div class="dico-def-mot">${echapper(d.mot)}</div>
            <div class="dico-def-nat">${echapper(d.nature || "")}</div>
          </div>
          ${this._retour ? `<button class="btn dico-utiliser" id="dico-utiliser">
            ✓ C'est ce mot-là, je l'utilise</button>` : ""}
        </div>
        ${d.definition
          ? `<div class="dico-def-txt">${echapper(d.definition)}</div>`
          : `<div class="dico-def-vide">${echapper(d.message)}</div>`}
        ${(d.famille || []).length ? `
          <div class="dico-famille">
            <div class="dico-famille-t">🌳 Mots de la même famille</div>
            <div class="dico-famille-l">${d.famille.map(f =>
              `<span class="dico-famille-m">${echapper(f.mot)}</span>`).join("")}</div>
            <div class="dico-famille-aide">Ils aident à retrouver les lettres
              qu'on n'entend pas à la fin.</div>
          </div>` : ""}
        <div class="dico-actions">
          <button class="btn fantome" id="dico-banque">🎒 Ajouter à ma banque de mots</button>
          <button class="btn fantome" id="dico-copier">⧉ Copier le mot</button>
        </div>
      </div>`;

    const bu = $("#dico-utiliser");
    if (bu) bu.onclick = () => this._utiliser(d.mot);
    $("#dico-copier").onclick = async () => {
      try { await navigator.clipboard.writeText(d.mot); toast("Mot copié."); }
      catch (e) { toast("Recopie le mot à la main : " + d.mot, 4000); }
    };
    $("#dico-banque").onclick = async () => {
      if (!Etat.eleve) return;
      await API.post(`/api/eleve/${Etat.eleve.id}/banque-lexicale/maitrise`,
        { mot: d.mot, categorie: "orthographe", maitrise: false });
      toast("Mot ajouté à ta banque de mots. 🎒");
    };
    zone.scrollIntoView({ behavior: "smooth", block: "nearest" });
  },

  /* ------------------------------------------------- Appel depuis Je me corrige
     On ouvre le dictionnaire dans une fenêtre, sans quitter son texte. */
  ouvrirFenetre(motDepart, surChoix) {
    this._retour = surChoix || (() => {});
    modale(`<div class="dico-modale">
        <div class="dico-poignee" id="dico-poignee">
          <div>
            <div class="carte-titre">🔎 Chercher un mot dans le dictionnaire</div>
            <div class="carte-sous" style="margin:4px 0 0">Écris le mot comme
              tu l'entends, puis clique sur celui qui a le bon sens.</div>
          </div>
          <span class="dico-deplacer">✥ déplaçable</span>
        </div>
        ${this._formulaire(null)}
        <div id="dico-resultats"></div>
        <div class="rangee" style="margin-top:16px">
          <button class="btn doux pousse" onclick="fermerModale()">Fermer</button>
        </div>
      </div>`, true);
    // La fenêtre s'ouvre dans la moitié basse et se déplace à la souris :
    // l'élève doit pouvoir relire son texte pendant qu'il cherche.
    this._placerEtRendreDeplacable();
    this._brancher();
    if (motDepart) { $("#dico-essai").value = motDepart; this.chercher(); }
    else $("#dico-essai").focus();
  },

  _placerEtRendreDeplacable() {
    const boite = $("#modale-corps");
    const poignee = $("#dico-poignee");
    if (!boite || !poignee) return;
    const modale = $("#modale");
    modale.classList.add("dico-flottante");
    boite.style.position = "absolute";
    boite.style.left = "50%";
    boite.style.transform = "translateX(-50%)";
    // Plus bas que le centre : le texte de l'élève reste visible au-dessus.
    boite.style.top = Math.round(window.innerHeight * 0.34) + "px";
    boite.style.maxHeight = "62vh";

    let ox = 0, oy = 0, actif = false;
    const debut = ev => {
      actif = true;
      const p = ev.touches ? ev.touches[0] : ev;
      const r = boite.getBoundingClientRect();
      ox = p.clientX - r.left;
      oy = p.clientY - r.top;
      boite.style.transform = "none";
      boite.style.left = r.left + "px";
      boite.style.top = r.top + "px";
      ev.preventDefault();
    };
    const bouger = ev => {
      if (!actif) return;
      const p = ev.touches ? ev.touches[0] : ev;
      const l = Math.max(4, Math.min(window.innerWidth - 120, p.clientX - ox));
      const t = Math.max(4, Math.min(window.innerHeight - 80, p.clientY - oy));
      boite.style.left = l + "px";
      boite.style.top = t + "px";
    };
    const fin = () => { actif = false; };
    poignee.addEventListener("mousedown", debut);
    poignee.addEventListener("touchstart", debut, { passive: false });
    document.addEventListener("mousemove", bouger);
    document.addEventListener("touchmove", bouger, { passive: false });
    document.addEventListener("mouseup", fin);
    document.addEventListener("touchend", fin);
  },

  _utiliser(mot) {
    const f = this._retour;
    fermerModale();
    this._retour = null;
    if (f) f(mot);
  }
};
