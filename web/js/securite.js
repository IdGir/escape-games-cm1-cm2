/* Sécurité : écran de code enseignant (création, déverrouillage, récupération).
   Le PIN est facultatif ; sans lui, cet écran ne s'affiche jamais. */

const Securite = {
  _onOuvrir: null,   // callback quand le prof est déverrouillé
  _onEleve: null,    // callback « aller à l'espace élève » (sans code)

  async etat() { return API.get("/api/securite/etat"); },

  /* Affiche l'écran de verrou. onOuvrir() = entrer côté prof ; onEleve() = élève. */
  async verrou(onOuvrir, onEleve) {
    this._onOuvrir = onOuvrir; this._onEleve = onEleve;
    const e = await this.etat();
    this._afficher(e.defini ? "entrer" : "creer");
  },

  reverrouiller() {
    Etat.jeton = null;
    if (this._onOuvrir) this.verrou(this._onOuvrir, this._onEleve);
  },

  fermer() { $("#verrou").innerHTML = ""; $("#verrou").classList.remove("on"); },

  _cadre(html) {
    $("#verrou").innerHTML = `<div class="verrou-carte">
      <div class="verrou-logo">✏️ Correcteur</div>${html}</div>`;
    $("#verrou").classList.add("on");
  },

  _afficher(mode) {
    if (mode === "creer") return this._creer();
    if (mode === "entrer") return this._entrer();
    if (mode === "recup") return this._recup();
    if (mode === "montrer") return; // géré par _montrerCode
  },

  _creer() {
    this._cadre(`
      <h2>Protéger l'espace enseignant</h2>
      <p class="verrou-aide">Choisissez un code de 4 à 6 chiffres. Il empêche les
        élèves d'accéder au tableau de bord et aux réglages. Facultatif : vous
        pouvez passer et le définir plus tard dans Réglages.</p>
      <input id="v-pin" class="verrou-pin" inputmode="numeric" maxlength="6" placeholder="••••">
      <button class="btn grand" id="v-creer" style="width:100%">Créer le code</button>
      <button class="btn doux" id="v-passer" style="width:100%;margin-top:8px">Plus tard</button>
      <div class="verrou-err" id="v-err"></div>`);
    $("#v-pin").focus();
    $("#v-creer").onclick = async () => {
      const r = await API.post("/api/securite/creer", { pin: $("#v-pin").value });
      if (r.erreur) return $("#v-err").textContent = r.erreur;
      Etat.jeton = r.jeton;
      this._montrerCode(r.code_recuperation);
    };
    $("#v-passer").onclick = () => { this.fermer(); this._onOuvrir && this._onOuvrir(); };
  },

  _montrerCode(code) {
    this._cadre(`
      <h2>Notez ce code de récupération</h2>
      <p class="verrou-aide">Il s'affiche <b>une seule fois</b>. Sans lui, un code
        oublié ne pourra plus être réinitialisé. Notez-le ou imprimez-le.</p>
      <div class="verrou-code">${echapper(code)}</div>
      <button class="btn grand" id="v-ok" style="width:100%">J'ai noté ce code</button>`);
    $("#v-ok").onclick = () => { this.fermer(); this._onOuvrir && this._onOuvrir(); };
  },

  _entrer() {
    this._cadre(`
      <h2>Espace enseignant</h2>
      <p class="verrou-aide">Saisissez votre code.</p>
      <input id="v-pin" class="verrou-pin" inputmode="numeric" maxlength="6" placeholder="••••">
      <button class="btn grand" id="v-entrer" style="width:100%">Entrer</button>
      ${this._onEleve ? `<button class="btn doux" id="v-eleve" style="width:100%;margin-top:8px">
        🎓 Aller à l'espace élève</button>` : ""}
      <button class="lien-verrou" id="v-oubli">Code oublié ?</button>
      <div class="verrou-err" id="v-err"></div>`);
    $("#v-pin").focus();
    const go = async () => {
      const r = await API.post("/api/securite/verifier", { pin: $("#v-pin").value });
      if (r.erreur) return $("#v-err").textContent = "Code incorrect.";
      Etat.jeton = r.jeton; this.fermer(); this._onOuvrir && this._onOuvrir();
    };
    $("#v-entrer").onclick = go;
    $("#v-pin").onkeydown = e => { if (e.key === "Enter") go(); };
    if (this._onEleve) $("#v-eleve").onclick = () => { this.fermer(); this._onEleve(); };
    $("#v-oubli").onclick = () => this._recup();
  },

  _recup() {
    this._cadre(`
      <h2>Réinitialiser le code</h2>
      <p class="verrou-aide">Entrez votre code de récupération, puis un nouveau code.</p>
      <input id="v-code" class="verrou-champ" placeholder="XXXX-XXXX-XXXX">
      <input id="v-pin" class="verrou-pin" inputmode="numeric" maxlength="6" placeholder="nouveau code">
      <button class="btn grand" id="v-valider" style="width:100%">Valider</button>
      <button class="lien-verrou" id="v-retour">Retour</button>
      <div class="verrou-err" id="v-err"></div>`);
    $("#v-valider").onclick = async () => {
      const r = await API.post("/api/securite/recuperer",
        { code: $("#v-code").value, pin: $("#v-pin").value });
      if (r.erreur) return $("#v-err").textContent = r.erreur;
      Etat.jeton = r.jeton; this._montrerCode(r.code_recuperation);
    };
    $("#v-retour").onclick = () => this._entrer();
  }
};
