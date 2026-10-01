/* ============================================================
   BANDEAU DE RÉFÉRENCE OFFICIELLE (amélioration C2) — tronc commun
   ------------------------------------------------------------
   Affiche sur l'écran d'accueil de chaque jeu la référence exacte du
   programme officiel (arrêté, numéro et date du Bulletin officiel,
   lien), VÉRIFIÉE sur education.gouv.fr — jusque-là signalée « non
   confirmée » dans plusieurs A-VERIFIER.md. Données uniques dans
   commun/donnees/catalogue.js (CATALOGUE.programmes) : une référence
   qui change se corrige une seule fois, pour tous les jeux.
   ============================================================ */
(function(){
  if(typeof CATALOGUE === "undefined" || !CATALOGUE.programmes) return;
  const id = (typeof JEU !== "undefined" && JEU.id) || location.pathname.split("/").filter(x => x && !/\.html?$/.test(x)).slice(-1)[0];
  const jeu = CATALOGUE.jeux.find(j => j.dossier === id || j.id === id);
  if(!jeu || !jeu.programme) return;
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;" }[c]));
  const refs = jeu.programme.map(k => CATALOGUE.programmes[k]).filter(Boolean);
  const d = CATALOGUE.programmesVerifies ? new Date(CATALOGUE.programmesVerifies).toLocaleDateString("fr-FR") : "";
  const b = document.createElement("div");
  b.className = "bandeau-bo";
  b.setAttribute("role", "note");
  b.style.cssText = "margin:14px auto 4px;max-width:720px;padding:8px 12px;border-radius:10px;background:rgba(255,255,255,.82);border:1px solid rgba(0,0,0,.15);font-size:.82rem;line-height:1.45;color:#1f2430;text-align:left";
  b.innerHTML = `📘 <b>Programme officiel</b>${d ? ` <span style="opacity:.7">(référence vérifiée le ${esc(d)})</span>` : ""} :` +
    refs.map(r => `<br>• ${esc(r.discipline)} : <a href="${esc(r.lien)}" target="_blank" rel="noopener">${esc(r.texte)}</a>${r.nor ? ` (NOR ${esc(r.nor)})` : ""} — ${esc(r.vigueur)}.`).join("");
  const ecran = document.getElementById("ecran-accueil");
  const cible = ecran && (ecran.querySelector(".accueil-carte, .carte-accueil, .contenu, .boite") || ecran);
  if(cible) cible.appendChild(b);
  window.BANDEAU_BO = { refs };
})();
