/* ============================================================
   AUTO-ÉVALUATION EN FIN DE PARTIE (amélioration N6) — tronc commun
   ------------------------------------------------------------
   À l'écran de fin, l'équipe (ou l'élève en mode individuel) se situe
   sur cinq affirmations rattachées aux domaines du socle commun de
   connaissances, de compétences et de culture :
     D1 les langages pour penser et communiquer ;
     D2 les méthodes et outils pour apprendre (×2 : chercher, persévérer) ;
     D3 la formation de la personne et du citoyen ;
     D4 (sciences) ou D5 (histoire, géographie) — EMC : D3.
   Trois réponses : « Pas encore », « Un peu », « Oui ! ».
   Les réponses sont gardées avec la partie (ETAT.autoEval) et ajoutées
   au compte-rendu (champ autoEval, code de contrôle recalculé) : elles
   apparaissent dans l'historique de resultats.html et dans le
   compte-rendu du mode individuel. Une grille vierge s'imprime pour
   que chaque élève de l'équipe la remplisse sur papier.
   Chargé après compte-rendu.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined") return;
  const JEU_ID = (typeof JEU !== "undefined" && JEU.id) || "";
  const fiche = (typeof CATALOGUE !== "undefined" && CATALOGUE.jeux) ? CATALOGUE.jeux.find(j => j.dossier === JEU_ID || j.id === JEU_ID) : null;
  const matiere = (fiche && fiche.matiere) || "";
  const NIVEAUX = [[1, "😟", "Pas encore"], [2, "🙂", "Un peu"], [3, "😃", "Oui !"]];

  function items(){
    const disc = /Sciences/i.test(matiere)
      ? { id: "e4", d: "D4", t: "J'ai observé, mesuré ou raisonné comme un scientifique pour trouver les réponses." }
      : /EMC/i.test(matiere)
        ? { id: "e4", d: "D3", t: "Je comprends à quoi sert une règle commune et pourquoi elle protège chacun." }
        : /G[ée]ographie/i.test(matiere)
          ? { id: "e4", d: "D5", t: "Je sais situer sur une carte les lieux que j'ai découverts." }
          : { id: "e4", d: "D5", t: "Je sais situer dans le temps les événements et les personnages que j'ai découverts." };
    return [
      { id: "e1", d: "D1", t: "Je connais les mots importants du thème et je peux les expliquer à quelqu'un." },
      { id: "e2", d: "D2", t: "Avant de répondre, j'ai cherché l'information dans les leçons et les documents." },
      { id: "e3", d: "D3", t: "J'ai écouté les autres et j'ai accepté une idée qui n'était pas la mienne." },
      disc,
      { id: "e5", d: "D2", t: "Quand c'était difficile, je n'ai pas abandonné." }
    ];
  }
  const DOMAINES = { D1: "Les langages pour penser et communiquer", D2: "Les méthodes et outils pour apprendre",
    D3: "La formation de la personne et du citoyen", D4: "Les systèmes naturels et les systèmes techniques",
    D5: "Les représentations du monde et l'activité humaine" };

  /* ---- Compte-rendu : les réponses y sont ajoutées, code de contrôle recalculé ---- */
  if(typeof COMPTE_RENDU !== "undefined"){
    const construire = COMPTE_RENDU.construire;
    COMPTE_RENDU.construire = function(){
      const cr = construire.apply(this, arguments);
      if(cr && ETAT.autoEval && Object.keys(ETAT.autoEval).length){
        cr.autoEval = Object.assign({}, ETAT.autoEval);
        COMPTE_RENDU.signer(cr);
      }
      return cr;
    };
    const texte = COMPTE_RENDU.texte;
    COMPTE_RENDU.texte = function(cr){
      let t = texte.apply(this, arguments);
      if(cr && cr.autoEval){
        const lib = { 1: "pas encore", 2: "un peu", 3: "oui" };
        const l = items().filter(i => cr.autoEval[i.id]).map(i => `  ${i.d} — ${i.t} : ${lib[cr.autoEval[i.id]]}`);
        if(l.length) t = t.replace(/\nCode de contrôle/, "\nAuto-évaluation (socle commun) :\n" + l.join("\n") + "\nCode de contrôle");
      }
      return t;
    };
  }

  function bloc(){
    const solo = !!ETAT.solo;
    const d = document.createElement("section");
    d.className = "auto-evaluation"; d.id = "auto-evaluation";
    d.innerHTML = `
      <h2>🪞 ${solo ? "Je m'évalue" : "On s'évalue"}</h2>
      <p class="ae-aide">${solo ? "Pour chaque phrase, choisis ce qui est vrai pour toi." : "Pour chaque phrase, mettez-vous d'accord sur la réponse de l'équipe. (Votre enseignant peut aussi imprimer une grille pour chacun.)"}</p>
      <table class="ae-grille">
        <thead><tr><th scope="col">Ce que j'ai fait pendant le jeu</th>${NIVEAUX.map(([, e, l]) => `<th scope="col">${e}<br>${l}</th>`).join("")}</tr></thead>
        <tbody>${items().map(i => `<tr data-item="${i.id}"><th scope="row">${i.t}<span class="ae-domaine" title="${DOMAINES[i.d]}">Socle ${i.d}</span></th>
          ${NIVEAUX.map(([v, e, l]) => `<td><button type="button" class="ae-choix" data-v="${v}" aria-label="${l}" aria-pressed="false">${e}</button></td>`).join("")}</tr>`).join("")}</tbody>
      </table>
      <p class="ae-merci" aria-live="polite"></p>
      <p class="ae-actions"><button type="button" class="btn gris petit" id="btn-imprimer-auto-eval">🖨️ Imprimer la grille (une par élève)</button></p>`;
    const maj = () => {
      d.querySelectorAll("tr[data-item]").forEach(tr => tr.querySelectorAll(".ae-choix").forEach(b => {
        const on = +(ETAT.autoEval || {})[tr.dataset.item] === +b.dataset.v;
        b.classList.toggle("choisi", on); b.setAttribute("aria-pressed", on ? "true" : "false");
      }));
      const n = Object.keys(ETAT.autoEval || {}).length;
      d.querySelector(".ae-merci").textContent = n >= 5 ? "✅ Merci ! Tes réponses sont gardées avec le bilan de la partie." : "";
    };
    d.addEventListener("click", ev => {
      const b = ev.target.closest(".ae-choix"); if(!b) return;
      const id = b.closest("tr").dataset.item;
      ETAT.autoEval = Object.assign({}, ETAT.autoEval, { [id]: +b.dataset.v });
      if(typeof sauvegarder === "function") sauvegarder();
      if(typeof COMPTE_RENDU !== "undefined" && !new URLSearchParams(location.search).get("salle")) COMPTE_RENDU.memoriser(COMPTE_RENDU.construire());
      maj();
    });
    d.querySelector("#btn-imprimer-auto-eval").addEventListener("click", imprimer);
    maj();
    return d;
  }

  function imprimer(){
    if(typeof preparerZoneImpression !== "function"){ window.print(); return; }
    const zone = preparerZoneImpression();
    const titreJeu = (typeof JEU !== "undefined" && JEU.titre) || document.title;
    const page = () => `
      ${typeof enteteFiche === "function" ? enteteFiche("Auto-évaluation", "Élève", "", false) : ""}
      <div class="impr-titre-principal">Je m'évalue</div>
      <div class="impr-soustitre">${titreJeu}</div>
      <p style="font-size:11pt">Prénom : ........................................ &nbsp; Équipe : ............................ &nbsp; Date : ............</p>
      <p style="font-size:10.5pt">Pour chaque phrase, coche la case qui est vraie pour toi.</p>
      <table style="width:100%;border-collapse:collapse;font-size:11pt;margin-top:3mm">
        <tr><th style="border:1.5px solid #333;padding:2mm;text-align:left">Pendant le jeu…</th>${NIVEAUX.map(([, e, l]) => `<th style="border:1.5px solid #333;padding:2mm;width:18mm">${e}<br><span style="font-size:8.5pt">${l}</span></th>`).join("")}</tr>
        ${items().map(i => `<tr><td style="border:1.5px solid #333;padding:3mm">${i.t}<br><span style="font-size:8pt;color:#555">Socle commun ${i.d} — ${DOMAINES[i.d]}</span></td>${NIVEAUX.map(() => `<td style="border:1.5px solid #333;text-align:center"><span style="display:inline-block;width:6mm;height:6mm;border:1.2px solid #333;border-radius:1mm"></span></td>`).join("")}</tr>`).join("")}
      </table>
      <p style="margin-top:6mm;font-size:11pt">Ce que j'ai appris de plus important :</p>
      <div style="border-bottom:1.2px dotted #333;height:9mm"></div><div style="border-bottom:1.2px dotted #333;height:9mm"></div>
      ${typeof piedPageFiche === "function" ? piedPageFiche(1, 1, "Auto-évaluation") : ""}`;
    zone.innerHTML = page();
    window.print();
  }

  function styles(){
    if(document.getElementById("style-auto-eval")) return;
    const s = document.createElement("style"); s.id = "style-auto-eval";
    s.textContent = `
      .auto-evaluation{margin:22px 0 8px;padding-top:14px;border-top:2px dotted var(--parchemin-ombre,#e0cfa6)}
      .auto-evaluation .ae-aide{opacity:.85;font-size:.95rem}
      .ae-grille{width:100%;border-collapse:collapse;margin-top:8px}
      .ae-grille th,.ae-grille td{padding:6px;border-bottom:1px solid rgba(0,0,0,.12);vertical-align:middle}
      .ae-grille thead th{font-size:.8rem;text-align:center}
      .ae-grille tbody th{text-align:left;font-weight:normal}
      .ae-domaine{display:inline-block;margin-left:6px;font-size:.7rem;padding:1px 6px;border-radius:8px;background:var(--parchemin-ombre,#e0cfa6);opacity:.9}
      .ae-grille td{text-align:center;width:64px}
      .ae-choix{font-size:1.5rem;line-height:1;padding:6px 8px;border-radius:12px;border:2px solid transparent;background:rgba(255,255,255,.6);cursor:pointer;filter:grayscale(.7);opacity:.75}
      .ae-choix.choisi{border-color:var(--or,#c9a227);background:#fff;filter:none;opacity:1;transform:scale(1.08)}
      .ae-choix:focus-visible{outline:3px solid var(--or,#c9a227)}
      .ae-merci{font-weight:bold;text-align:center;min-height:1em}
      .ae-actions{text-align:center}
      @media (max-width:560px){.ae-grille td{width:44px}.ae-choix{font-size:1.2rem;padding:4px}}
      @media print{.ae-actions{display:none}}`;
    document.head.appendChild(s);
  }

  /* Écran de fin : la grille est placée avant les boutons « Rejouer / Imprimer » */
  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      const c = document.getElementById("fin-contenu");
      if(c && !document.getElementById("auto-evaluation")){
        styles();
        const rej = c.querySelector("#btn-rejouer");
        const avant = rej && rej.closest(".boutons");
        if(avant && avant.parentNode) avant.parentNode.insertBefore(bloc(), avant); else c.appendChild(bloc());
      }
      return r;
    };
  }
  /* Nouvelle partie : grille remise à zéro */
  const go = document.getElementById("btn-demarrer");
  if(go) go.addEventListener("click", () => { ETAT.autoEval = {}; });

  window.AUTO_EVALUATION = { items, imprimer, DOMAINES, matiere };
})();
