/* ============================================================
   MODE INDIVIDUEL — devoirs à la maison (amélioration D2)
   ------------------------------------------------------------
   Le jeu est pensé pour des équipes de 3-4. En mode individuel :
     • sur l'écran d'accueil, « 🏠 Je joue seul » : on écrit son prénom
       au lieu d'un nom d'équipe ; adresse directe à donner aux élèves :
       …/melanges/?solo=1  (ou ?solo=1&niveau=CM1) ;
     • aucune synchronisation avec un tableau de bord (à la maison, il
       n'y en a pas), règles et barème inchangés ;
     • à la fin, un COMPTE-RENDU POUR L'ENSEIGNANT : score, énigmes
       réussies du premier coup, erreurs, indices, temps par salle, et
       un code de contrôle. L'élève le copie dans un message de l'ENT,
       le télécharge (fichier à déposer) ou l'imprime. L'enseignant les
       rassemble dans resultats.html (tableur, Schooly).
   Chargé après app.js, sans modifier app.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined" || !document.getElementById("input-equipe")) return;
  const inp = document.getElementById("input-equipe");
  const titreEquipe = inp.previousElementSibling && /^H3$/.test(inp.previousElementSibling.tagName) ? inp.previousElementSibling : null;
  const placeholderEquipe = inp.placeholder;
  const params = new URLSearchParams(location.search);

  const style = document.createElement("style");
  style.textContent = `
    .bascule-solo{display:flex;justify-content:center;margin:6px 0 10px;font-size:.95rem}
    .bascule-solo label{display:inline-flex;gap:8px;align-items:center;cursor:pointer;padding:6px 12px;border-radius:999px;background:rgba(255,255,255,.6)}
    .compte-rendu{margin:22px auto;max-width:680px;padding:16px 18px;border-radius:14px;background:#fff;border:2px solid #1d3a8a;color:#1f2430}
    .compte-rendu pre{white-space:pre-wrap;font:inherit;font-size:.92rem;background:#f4f6fb;padding:10px 12px;border-radius:10px;margin:8px 0}
    .compte-rendu .boutons{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
  `;
  document.head.appendChild(style);

  const bascule = document.createElement("div");
  bascule.className = "bascule-solo";
  bascule.innerHTML = `<label><input type="checkbox" id="mode-solo"> 🏠 Je joue seul (devoirs à la maison)</label>`;
  inp.before(bascule);
  const caseSolo = bascule.querySelector("#mode-solo");
  function majLibelles(){
    const solo = caseSolo.checked;
    if(titreEquipe) titreEquipe.textContent = solo ? "👤 Ton prénom" : "👤 Votre équipe";
    inp.placeholder = solo ? "Ton prénom (et l'initiale de ton nom)" : placeholderEquipe;
  }
  caseSolo.addEventListener("change", majLibelles);
  if(params.get("solo") === "1"){ caseSolo.checked = true; majLibelles(); }

  const go = document.getElementById("btn-demarrer");
  if(go) go.addEventListener("click", () => { ETAT.solo = caseSolo.checked; });
  // Reprise d'une partie individuelle : le mode est relu dans la sauvegarde
  try{
    const s = JSON.parse(localStorage.getItem(typeof CLE_SAUVEGARDE !== "undefined" ? CLE_SAUVEGARDE : "") || "null");
    if(s && s.solo && !s.fini && !params.get("salle")) ETAT.solo = true;
  }catch(e){}

  /* Pas de tableau de bord à la maison */
  if(typeof window.demarrerSync === "function"){
    const origine = window.demarrerSync;
    window.demarrerSync = function(){ if(ETAT.solo) return; return origine.apply(this, arguments); };
  }

  /* Compte-rendu pour l'enseignant, à l'écran de fin */
  function bloc(){
    const d = document.createElement("div");
    d.className = "compte-rendu"; d.id = "compte-rendu";
    d.innerHTML = `<h3 style="margin:0 0 6px">📨 Ton compte-rendu pour l'enseignant</h3>
      <p style="margin:0;font-size:.9rem">Réponds d'abord au quizz final, puis envoie ce compte-rendu à ton enseignant (message de l'ENT, fichier ou papier).</p>
      <pre id="cr-texte"></pre>
      <div class="boutons">
        <button type="button" class="btn bleu" id="cr-copier">📋 Copier le compte-rendu</button>
        <button type="button" class="btn gris" id="cr-fichier">💾 Télécharger le fichier</button>
        <button type="button" class="btn gris" id="cr-imprimer">🖨️ Imprimer</button>
      </div>`;
    const maj = () => { const cr = COMPTE_RENDU.construire(); d.querySelector("#cr-texte").textContent = COMPTE_RENDU.texte(cr); return cr; };
    maj();
    d.querySelector("#cr-copier").addEventListener("click", ev => {
      const t = COMPTE_RENDU.texte(maj());
      const fini = () => { ev.target.textContent = "✓ Copié : colle-le dans ton message"; };
      if(navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(fini).catch(() => prompt("Copie ce texte :", t));
      else prompt("Copie ce texte :", t);
    });
    d.querySelector("#cr-fichier").addEventListener("click", () => {
      const cr = maj();
      const nom = `compte-rendu-${cr.jeu}-${(cr.eleve || "eleve").replace(/[^\p{L}\p{N}]+/gu, "-")}-${cr.date.slice(0, 10)}.json`;
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([JSON.stringify(cr, null, 1)], { type: "application/json" }));
      a.download = nom; document.body.appendChild(a); a.click(); a.remove();
    });
    d.querySelector("#cr-imprimer").addEventListener("click", () => {
      const cr = maj();
      const z = typeof preparerZoneImpression === "function" ? preparerZoneImpression() : null;
      if(z){ z.innerHTML = `<h2>Compte-rendu — ${cr.titre}</h2><pre style="white-space:pre-wrap;font:12pt/1.5 sans-serif">${COMPTE_RENDU.texte(cr).replace(/</g, "&lt;")}</pre>`; }
      window.print();
    });
    const q = document.getElementById("btn-voir-score");
    if(q) q.addEventListener("click", () => setTimeout(maj, 80));
    return d;
  }
  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      const c = document.getElementById("fin-contenu");
      if(ETAT.solo && c && !document.getElementById("compte-rendu") && typeof COMPTE_RENDU !== "undefined"){
        const q = document.getElementById("quizz");
        const apres = (q && q.parentNode === c) ? document.getElementById("score-recap") || q : null;
        if(apres) apres.after(bloc()); else c.appendChild(bloc());
      }
      return r;
    };
  }
  window.MODE_SOLO = { actif: () => !!ETAT.solo };
})();
