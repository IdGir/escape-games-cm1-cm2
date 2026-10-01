/* ============================================================
   INDICES ADAPTATIFS (amélioration E3) — tronc commun
   ------------------------------------------------------------
   Avant : 3 indices par énigme, uniquement sur demande. Désormais le
   jeu PROPOSE un indice quand l'équipe semble bloquée :
     • après un temps sans aucune action sur l'énigme (2 min en CM1 et
       au palier Découverte, 3 min en CM2 — réglable) ;
     • ou après 2 vérifications fausses sur la même énigme.
   C'est une proposition, jamais une réponse : l'équipe choisit
   « 💡 Voir un indice » (même règle qu'avant : −2 points) ou « Pas
   maintenant » (la proposition reviendra plus tard). Rien n'est
   proposé pendant la pause, ni quand tous les indices sont déjà vus.
   Réglage enseignant dans ⚙️ Réglages (gardé sur l'appareil).
   Chargé après app.js, sans modifier app.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined") return;
  const CLE = "escape_indices_adaptatifs";
  const DEFAUT = { actif: true, delaiCM1: 120, delaiCM2: 180, erreurs: 2 };
  const lire = () => { try { return Object.assign({}, DEFAUT, JSON.parse(localStorage.getItem(CLE) || "{}")); } catch(e) { return Object.assign({}, DEFAUT); } };
  const ecrire = r => { try { localStorage.setItem(CLE, JSON.stringify(r)); } catch(e) {} };

  const style = document.createElement("style");
  style.textContent = `
    .proposition-indice{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;margin:10px 0;padding:10px 14px;
      border-radius:12px;background:#fff7e0;border:2px solid #e0b84c;color:#5b4300}
    .proposition-indice .txt{flex:1;min-width:200px}
    .proposition-indice button{font:inherit;padding:6px 12px;border-radius:999px;border:1px solid #c99a22;background:#fff;cursor:pointer}
    .proposition-indice button.oui{background:#e0b84c;color:#2d2100;font-weight:600}
  `;
  document.head.appendChild(style);

  let suivi = null;   // énigme suivie : { carte, bouton, derniere, erreurs0, refus }
  const maintenant = () => Date.now();

  function suivre(carte, bouton){
    if(suivi && suivi.carte !== carte) retirer();
    suivi = { carte, bouton, derniere: maintenant(), erreurs0: ETAT.erreursTotal || 0, refus: 0, propose: false };
    const actif = () => { if(suivi && suivi.carte === carte) suivi.derniere = maintenant(); };
    ["pointerdown", "keydown", "input", "change", "click"].forEach(t => carte.addEventListener(t, actif, true));
  }
  function retirer(){ document.querySelectorAll(".proposition-indice").forEach(p => p.remove()); }
  const restants = b => b && !b.disabled && !/Plus d'indices/.test(b.textContent);
  const resolue = c => c.classList.contains("resolue") || !document.body.contains(c);

  function proposer(raison){
    const s = suivi; if(!s || s.propose) return;
    s.propose = true;
    const p = document.createElement("div");
    p.className = "proposition-indice";
    p.setAttribute("role", "status");
    p.innerHTML = `<span class="txt">💡 ${raison} Un indice peut vous aider (−2 points, comme d'habitude).</span>
      <button type="button" class="oui">💡 Voir un indice</button><button type="button" class="non">Pas maintenant</button>`;
    p.querySelector(".oui").addEventListener("click", () => { p.remove(); s.propose = false; s.derniere = maintenant(); s.erreurs0 = ETAT.erreursTotal || 0; if(restants(s.bouton)) s.bouton.click(); });
    p.querySelector(".non").addEventListener("click", () => { p.remove(); s.propose = false; s.refus++; s.derniere = maintenant(); s.erreurs0 = ETAT.erreursTotal || 0; });
    const corps = s.carte.querySelector(".enigme-corps");
    if(corps) corps.after(p); else s.carte.appendChild(p);
  }

  function verifier(){
    const r = lire(), s = suivi;
    if(!r.actif || !s) return;
    if(ETAT.enPause || ETAT.fini){ s.derniere = maintenant(); return; }
    if(resolue(s.carte) || !restants(s.bouton)){ retirer(); suivi = null; return; }
    if(s.propose) return;
    const decouverte = ETAT.palier === "decouverte";
    const delai = ((ETAT.niveau === "CM1" || decouverte) ? r.delaiCM1 : r.delaiCM2) * 1000 * (1 + s.refus);
    const erreurs = (ETAT.erreursTotal || 0) - s.erreurs0;
    if(r.erreurs && erreurs >= r.erreurs) proposer(`${erreurs} essais sans succès sur cette énigme.`);
    else if(maintenant() - s.derniere >= delai) proposer("Vous êtes sur cette énigme depuis un moment.");
  }
  setInterval(verifier, 1000);

  /* Branchement : moteur commun (une carte par énigme) et moteur propre */
  if(typeof window.activerEnigme === "function"){
    const origine = window.activerEnigme;
    window.activerEnigme = function(e){
      const res = origine.apply(this, arguments);
      const carte = document.getElementById("enigme-" + e.id);
      if(carte) suivre(carte, carte.querySelector("#indice-" + e.id));
      return res;
    };
  }
  if(typeof window.activerBoutonIndice === "function"){
    const origine = window.activerBoutonIndice;
    window.activerBoutonIndice = function(){
      const res = origine.apply(this, arguments);
      const zone = document.querySelector("#salle-contenu .zone-enigme") || document.querySelector(".zone-enigme");
      if(zone) suivre(zone, document.getElementById("btn-indice"));
      return res;
    };
  }

  /* Réglage enseignant, inséré dans ⚙️ Réglages après le groupe « Accessibilité » */
  function bloc(){
    const r = lire();
    const g = document.createElement("div");
    g.className = "reglages-group"; g.id = "reglages-indices-adaptatifs";
    const opts = (v) => [[60, "1 min"], [120, "2 min"], [180, "3 min"], [300, "5 min"]].map(([s, t]) => `<option value="${s}" ${+v === s ? "selected" : ""}>${t}</option>`).join("");
    g.innerHTML = `<h4>💡 Indices proposés</h4>
      <div class="reglage-ligne"><div class="libelle"><b>Proposer un indice quand une équipe bloque</b><br>
        <span style="font-size:.8rem;opacity:.7">Après un temps sans action ou plusieurs essais faux. Les élèves restent libres de refuser. Gardé sur cet appareil.</span></div>
        <div class="controle"><input type="checkbox" id="ia-actif" ${r.actif ? "checked" : ""}></div></div>
      <div class="reglage-ligne"><div class="libelle">Délai sans action — CM1 et Découverte</div><div class="controle"><select id="ia-cm1">${opts(r.delaiCM1)}</select></div></div>
      <div class="reglage-ligne"><div class="libelle">Délai sans action — CM2</div><div class="controle"><select id="ia-cm2">${opts(r.delaiCM2)}</select></div></div>
      <div class="reglage-ligne"><div class="libelle">Après combien d'essais faux</div><div class="controle"><select id="ia-err">
        ${[[0, "jamais"], [2, "2 essais"], [3, "3 essais"]].map(([n, t]) => `<option value="${n}" ${+r.erreurs === n ? "selected" : ""}>${t}</option>`).join("")}</select></div></div>`;
    g.addEventListener("change", () => ecrire({ actif: g.querySelector("#ia-actif").checked, delaiCM1: +g.querySelector("#ia-cm1").value,
      delaiCM2: +g.querySelector("#ia-cm2").value, erreurs: +g.querySelector("#ia-err").value }));
    return g;
  }
  const obs = new MutationObserver(() => {
    const calme = document.getElementById("reg-calme");
    if(calme && !document.getElementById("reglages-indices-adaptatifs")){
      const grp = calme.closest(".reglages-group");
      if(grp) grp.after(bloc());
    }
  });
  const demarrer = () => obs.observe(document.body, { childList: true, subtree: true });
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
  window.INDICES_ADAPTATIFS = { lire, ecrire, verifier, get suivi(){ return suivi; } };
})();
