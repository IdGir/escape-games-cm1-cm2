/* ============================================================
   INDICES À COÛT DÉGRESSIF (amélioration N5) — tronc commun
   ------------------------------------------------------------
   Barème habituel : chaque indice coûte 2 points. Option enseignant
   (⚙️ Réglages → 💡 Indices, gardée sur l'appareil) : coût DÉGRESSIF,
   le 1er indice d'une énigme coûte 2 points, le 2e et le 3e 1 point.
   But : qu'une équipe ose demander le deuxième indice quand le premier
   n'a pas suffi, au lieu de tenter au hasard.
   En mode dégressif, le coût du prochain indice est écrit sur le bouton.
   Fonctionne avec les deux moteurs (bouton #indice-<id> ou #btn-indice),
   sans modifier app.js ni enigmes.js : le score est recalculé juste
   après le clic.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined") return;
  const CLE = "escape_indices_cout";
  const BAREMES = { fixe: [2, 2, 2], degressif: [2, 1, 1] };
  const mode = () => { try { const m = JSON.parse(localStorage.getItem(CLE) || "{}").mode; return BAREMES[m] ? m : "fixe"; } catch(e) { return "fixe"; } };
  const choisir = m => { try { localStorage.setItem(CLE, JSON.stringify({ mode: m })); } catch(e) {} annoterTout(); };
  const rangs = {};   // énigme → nombre d'indices déjà vus
  const cleDe = b => `${ETAT.niveau}|${ETAT.salle}|${b.id === "btn-indice" ? "salle" : b.id}`;
  const cout = rang => { const b = BAREMES[mode()]; return b[Math.min(rang, b.length - 1)]; };
  const estBouton = b => b && b.tagName === "BUTTON" && (b.id === "btn-indice" || /^indice-/.test(b.id));

  /* Le clic passe d'abord ici (phase de capture), puis dans le moteur */
  document.addEventListener("click", ev => {
    const b = ev.target && ev.target.closest && ev.target.closest("button");
    if(!estBouton(b) || b.disabled) return;
    const avant = { score: ETAT.score, indices: ETAT.indicesTotal || 0 }, cle = cleDe(b);
    setTimeout(() => {
      if((ETAT.indicesTotal || 0) <= avant.indices) return;   // pas d'indice donné (plus d'indices…)
      const r = rangs[cle] || 0;
      rangs[cle] = r + 1;
      ETAT.score = Math.max(0, avant.score - cout(r));
      if(typeof majHUD === "function") majHUD();
      if(typeof sauvegarder === "function") sauvegarder();
      annoter(b);
    }, 0);
  }, true);

  /* Coût écrit sur le bouton (mode dégressif seulement) */
  function annoter(b){
    if(!b || !b.isConnected) return;
    const base = b.textContent.replace(/\s*\(−\d+\s*pts?\)\s*$/, "");
    if(mode() !== "degressif" || /Plus d'indices/.test(base)) { b.textContent = base; return; }
    const c = cout(rangs[cleDe(b)] || 0);
    b.textContent = `${base} (−${c} pt${c > 1 ? "s" : ""})`;
  }
  function annoterTout(){ document.querySelectorAll("#btn-indice, button[id^='indice-']").forEach(annoter); }
  /* Proposition d'indice (E3) : le texte suit le barème */
  function ajusterPropositions(){
    document.querySelectorAll(".proposition-indice .txt").forEach(t => {
      if(mode() !== "degressif" || t.dataset.n5) return;
      const b = document.querySelector("#btn-indice, button[id^='indice-']");
      const c = b ? cout(rangs[cleDe(b)] || 0) : 2;
      t.dataset.n5 = "1";
      t.innerHTML = t.innerHTML.replace(/\(−2 points, comme d'habitude\)/, `(−${c} point${c > 1 ? "s" : ""})`);
    });
  }

  /* Réglage enseignant : dans le groupe « 💡 Indices proposés » (E3), sinon après « Accessibilité » */
  function reglage(){
    if(document.getElementById("reg-cout-indices")) return;
    const grp = document.getElementById("reglages-indices-adaptatifs")
      || (document.getElementById("reg-calme") && document.getElementById("reg-calme").closest(".reglages-group"));
    if(!grp) return;
    const l = document.createElement("div");
    l.className = "reglage-ligne";
    l.innerHTML = `<div class="libelle"><b>Coût des indices</b><br><span style="font-size:.8rem;opacity:.7">Dégressif : le 1er indice d'une énigme coûte 2 points, les suivants 1 point. Gardé sur cet appareil.</span></div>
      <div class="controle"><select id="reg-cout-indices">
        <option value="fixe">Fixe : −2 points chacun</option>
        <option value="degressif">Dégressif : −2, puis −1, puis −1</option></select></div>`;
    l.querySelector("select").value = mode();
    l.querySelector("select").addEventListener("change", e => choisir(e.target.value));
    if(grp.id === "reglages-indices-adaptatifs") grp.appendChild(l); else grp.after(l);
  }

  let attente = null;
  const obs = new MutationObserver(() => {
    reglage(); ajusterPropositions();
    if(mode() === "degressif" && !attente) attente = setTimeout(() => { attente = null; document.querySelectorAll("#btn-indice, button[id^='indice-']").forEach(b => { if(!/\(−\d/.test(b.textContent)) annoter(b); }); }, 0);
  });
  const demarrer = () => { obs.observe(document.body, { childList: true, subtree: true }); annoterTout(); };
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
  window.INDICES_DEGRESSIFS = { mode, choisir, cout, BAREMES };
})();
