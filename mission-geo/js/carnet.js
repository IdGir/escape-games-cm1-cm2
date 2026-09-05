/* =========================================================
   CARNET DE MISSION — accueil des 16 séances, indices,
   et piste finale (pays, case, cadenas, récompense).
   ========================================================= */

const CARNET = (function(){

  const $ = (t, c, x) => { const e = document.createElement(t); if(c) e.className = c;
                           if(x !== undefined) e.textContent = x; return e; };

  const NOMS_PERIODES = {
    1: "Période 1 — septembre / octobre",
    2: "Période 2 — novembre / décembre",
    3: "Période 3 — janvier / février",
    4: "Période 4 — mars / avril",
    5: "Période 5 — mai / juin"
  };

  /* ---------------------------------------------------------
     Le tableau des séances
     --------------------------------------------------------- */
  function dessinerHub(){
    const etat = SAUVEGARDE.lire();
    const hote = document.getElementById("liste-periodes");
    hote.innerHTML = "";

    const total = MISSION.sessions.length;
    const faites = SAUVEGARDE.reussies();
    document.getElementById("carnet-total").textContent = total;
    document.getElementById("carnet-fait").textContent = faites;
    document.getElementById("jauge-progression").style.width = (faites / total * 100) + "%";
    document.getElementById("carnet-equipe").textContent =
      etat.equipe ? etat.equipe + " · " + etat.niveau + " · " + SAUVEGARDE.pointsTotaux() + " points"
                  : "";

    MISSION.parPeriode().forEach((seances, periode) => {
      const bloc = $("div", "periode");
      const titre = $("h3");
      titre.appendChild($("span", "etiquette-periode", "P" + periode));
      titre.appendChild($("span", null, NOMS_PERIODES[periode] || ("Période " + periode)));
      bloc.appendChild(titre);
      bloc.appendChild($("p", "theme", [...new Set(seances.map(s => s.theme))].join(" · ")));

      const grille = $("div", "grille-seances");
      seances.forEach(s => {
        const reussie  = SAUVEGARDE.estReussie(s.id);
        const ouverte  = estOuverte(s);
        const b = $("button", "carte-seance" + (reussie ? " reussie" : ""));
        b.type = "button";
        b.disabled = !ouverte && !reussie;
        b.appendChild($("span", "num", "Séance " + s.numero +
          (s.livret ? " · livret p. " + s.livret : "")));
        b.appendChild($("span", "titre", s.titre));
        b.appendChild($("span", "lieu", "📍 " + s.lieu));
        b.appendChild($("span", "etat", reussie ? "✅" : (ouverte ? "▶️" : "🔒")));
        b.title = s.element;
        b.addEventListener("click", () => APP.ouvrirSession(s.id));
        grille.appendChild(b);
      });
      bloc.appendChild(grille);
      hote.appendChild(bloc);
    });

    dessinerIndices();
  }

  /* Une séance est jouable si l'ordre libre est actif,
     ou si toutes les séances précédentes sont réussies. */
  function estOuverte(s){
    if(SAUVEGARDE.lire().reglages.ordreLibre) return true;
    return MISSION.ordre()
      .filter(x => x.numero < s.numero)
      .every(x => SAUVEGARDE.estReussie(x.id));
  }

  /* ---------------------------------------------------------
     Le panneau des indices
     --------------------------------------------------------- */
  function dessinerIndices(){
    const etat = SAUVEGARDE.lire();
    const ul = document.getElementById("liste-indices");
    const sym = MISSION.final.symboles;
    ul.innerHTML = "";

    if(!etat.indices.length){
      const li = $("li", "indices-vide", "Aucun indice pour l'instant. Réussis ta première séance !");
      ul.appendChild(li);
    }

    etat.indices
      .slice()
      .sort((a, b) => a.numero - b.numero)
      .forEach(i => {
        const li = $("li", i.type === "fait" ? "fait" : "");
        if(i.type === "nombre"){
          li.appendChild($("span", "symbole", (sym[i.symbole] || {}).glyphe || "◇"));
          const t = $("div");
          t.appendChild($("span", "valeur", "= " + i.valeur));
          t.appendChild($("small", null, i.libelle));
          li.appendChild(t);
        } else {
          li.appendChild($("span", "symbole", "🗒️"));
          const t = $("div");
          t.appendChild($("span", null, i.texte));
          t.appendChild($("small", null, i.libelle));
          li.appendChild(t);
        }
        ul.appendChild(li);
      });

    const total = MISSION.sessions.length;
    const bouton = document.getElementById("btn-valise");
    const aide = document.getElementById("aide-valise");
    const complet = etat.indices.length >= total;
    bouton.disabled = !complet && !etat.reglages.ordreLibre;
    aide.textContent = complet
      ? "Tous les indices sont réunis. La valise n'attend plus que toi."
      : "Encore " + (total - etat.indices.length) + " indice(s) à récolter avant d'ouvrir la piste finale.";
  }

  /* ---------------------------------------------------------
     Calculs de la piste finale
     --------------------------------------------------------- */
  function valeurSymbole(cle){
    const trouve = SAUVEGARDE.lire().indices.find(i => i.type === "nombre" && i.symbole === cle);
    return trouve ? trouve.valeur : null;
  }

  function calculer(termes){
    let total = null;
    for(const t of termes){
      const v = valeurSymbole(t.symbole);
      if(v === null) return null;
      if(total === null){ total = v; continue; }
      if(t.op === "-") total -= v;
      else if(t.op === "×") total *= v;
      else total += v;
    }
    return total;
  }

  function ecrireCalcul(termes){
    const sym = MISSION.final.symboles;
    return termes.map((t, i) => {
      const g = (sym[t.symbole] || {}).glyphe || "◇";
      return (i === 0 ? "" : " " + t.op + " ") + g;
    }).join("");
  }

  function ecrireCalculDetaille(termes){
    return termes.map((t, i) => {
      const v = valeurSymbole(t.symbole);
      return (i === 0 ? "" : " " + t.op + " ") + (v === null ? "?" : v);
    }).join("");
  }

  /* ---------------------------------------------------------
     L'écran final
     --------------------------------------------------------- */
  function ouvrirFinal(){
    const F = MISSION.final;
    const etat = SAUVEGARDE.lire();
    const scene = document.getElementById("final-scene");
    scene.innerHTML = "";

    const boite = $("div", "scene");
    boite.appendChild($("h2", null, "🧳 La piste finale"));
    boite.appendChild($("p", "fil", "Trois énigmes te séparent encore de la valise."));
    if(typeof MEDIAS !== "undefined")
      boite.appendChild(MEDIAS.bloc({ base: "final-intro", legende: "Aéroport d'Ajaccio" }));

    const rappel = $("div", "narration");
    rappel.innerHTML = "<p>Tu atterris à l'aéroport d'Ajaccio. Il est temps d'utiliser " +
      "tous les indices glanés au cours de ton aventure…</p>";
    boite.appendChild(rappel);

    /* ---- Étape 1 : le pays ---- */
    const e1 = $("section", "etape-finale" + (etat.final.pays ? " resolue" : ""));
    e1.appendChild($("h3", null, "1. À qui appartient la valise ?"));
    e1.appendChild($("p", null, F.pays.consigne));
    const listeFaits = $("ul");
    etat.indices.filter(i => i.type === "fait").forEach(i => listeFaits.appendChild($("li", null, i.texte)));
    if(!listeFaits.children.length) listeFaits.appendChild($("li", null, "(aucun indice textuel récolté)"));
    e1.appendChild(listeFaits);

    const choix = $("div", "choix-valises");
    F.pays.propositions.forEach(p => {
      const b = $("button");
      b.type = "button";
      b.appendChild($("span", "drapeau", p.drapeau));
      b.appendChild($("span", null, p.nom));
      if(etat.final.pays === p.id) b.classList.add("choisie");
      b.addEventListener("click", () => {
        choix.querySelectorAll("button").forEach(x => x.classList.remove("choisie"));
        b.classList.add("choisie");
        b.dataset.selection = "1";
        choix.dataset.choix = p.id;
      });
      choix.appendChild(b);
    });
    e1.appendChild(choix);

    const retour1 = $("p", "retour");
    retour1.hidden = true;
    const valider1 = $("button", "bouton-principal", "Valider le pays");
    valider1.type = "button";
    valider1.addEventListener("click", () => {
      const c = choix.dataset.choix;
      if(!c){ APP.message("Choisis d'abord une valise.", "erreur"); return; }
      if(c === F.pays.solution){
        etat.final.pays = c;
        SAUVEGARDE.enregistrer();
        e1.classList.add("resolue");
        retour1.className = "retour bon";
        retour1.innerHTML = "✅ " + F.pays.explication;
        retour1.hidden = false;
        valider1.disabled = true;
      } else {
        retour1.className = "retour faux";
        retour1.textContent = "Ce pays ne colle pas à tous les indices. Relis-les un par un et élimine.";
        retour1.hidden = false;
      }
    });
    e1.appendChild(valider1);
    e1.appendChild(retour1);
    if(etat.final.pays){
      valider1.disabled = true;
      retour1.className = "retour bon";
      retour1.innerHTML = "✅ " + F.pays.explication;
      retour1.hidden = false;
    }
    boite.appendChild(e1);

    /* ---- Étape 2 : la case de la carte ---- */
    const dejaCase = etat.final.colonne !== null && etat.final.ligne !== null;
    const e2 = $("section", "etape-finale" + (dejaCase ? " resolue" : ""));
    e2.appendChild($("h3", null, "2. Où se cache exactement la valise ?"));
    e2.appendChild($("p", null, F.carte.consigne));

    const attendus = {};
    F.carte.calculs.forEach(c => {
      const p = $("p");
      p.appendChild($("b", null, c.titre + " : "));
      const calc = $("span", "calcul-symboles", ecrireCalcul(c.termes));
      p.appendChild(calc);
      const detail = $("small", null, "  →  " + ecrireCalculDetaille(c.termes));
      p.appendChild(detail);
      e2.appendChild(p);
      attendus[c.cle] = calculer(c.termes);
    });

    const grille = $("div", "grille-corse");
    grille.style.gridTemplateColumns = "repeat(" + F.carte.colonnes + ", 1fr)";
    let choixCase = dejaCase ? { c: etat.final.colonne, l: etat.final.ligne } : null;
    for(let l = 1; l <= F.carte.lignes; l++){
      for(let c = 1; c <= F.carte.colonnes; c++){
        const b = $("button", null, c + "-" + l);
        b.type = "button";
        if(choixCase && choixCase.c === c && choixCase.l === l) b.classList.add("choisie");
        b.addEventListener("click", () => {
          grille.querySelectorAll("button").forEach(x => x.classList.remove("choisie"));
          b.classList.add("choisie");
          choixCase = { c, l };
        });
        grille.appendChild(b);
      }
    }
    const carteVisuelle = $("div", "media-slot");
    if(typeof CARTES !== "undefined"){
      const svg = CARTES.decor("corse-grille");
      if(svg) carteVisuelle.innerHTML = svg;
    }
    if(typeof MEDIAS !== "undefined")
      MEDIAS.remplir(carteVisuelle, { base: "carte-corse", decor: "corse-grille",
                                      legende: "Côte ouest de la Corse" });
    e2.appendChild(carteVisuelle);
    e2.appendChild($("p", "aide-panneau", "Clique sur la case « colonne-ligne » désignée par tes deux calculs."));
    e2.appendChild(grille);

    const retour2 = $("p", "retour");
    retour2.hidden = true;
    const valider2 = $("button", "bouton-principal", "Valider la case");
    valider2.type = "button";
    valider2.addEventListener("click", () => {
      if(!choixCase){ APP.message("Choisis une case sur la carte.", "erreur"); return; }
      if(attendus.colonne === null || attendus.ligne === null){
        APP.message("Il te manque des indices chiffrés pour faire ce calcul.", "erreur"); return;
      }
      if(choixCase.c === attendus.colonne && choixCase.l === attendus.ligne){
        etat.final.colonne = choixCase.c; etat.final.ligne = choixCase.l;
        SAUVEGARDE.enregistrer();
        e2.classList.add("resolue");
        retour2.className = "retour bon";
        retour2.textContent = "✅ Colonne " + attendus.colonne + ", ligne " + attendus.ligne +
          " : " + F.carte.lieu + ". C'est bien là.";
        retour2.hidden = false;
        valider2.disabled = true;
      } else {
        retour2.className = "retour faux";
        retour2.textContent = "Ce n'est pas la bonne case. Refais tes deux calculs, dans l'ordre.";
        retour2.hidden = false;
      }
    });
    e2.appendChild(valider2);
    e2.appendChild(retour2);
    if(dejaCase){
      valider2.disabled = true;
      retour2.className = "retour bon";
      retour2.textContent = "✅ Colonne " + etat.final.colonne + ", ligne " + etat.final.ligne +
        " : " + F.carte.lieu + ".";
      retour2.hidden = false;
    }
    boite.appendChild(e2);

    /* ---- Étape 3 : le cadenas ---- */
    const e3 = $("section", "etape-finale" + (etat.final.code ? " resolue" : ""));
    e3.appendChild($("h3", null, "3. Le code du cadenas"));
    e3.appendChild($("p", null, F.cadenas.consigne));
    const pc = $("p");
    pc.appendChild($("span", "calcul-symboles", ecrireCalcul(F.cadenas.termes)));
    pc.appendChild($("small", null, "  →  " + ecrireCalculDetaille(F.cadenas.termes)));
    e3.appendChild(pc);

    const champ = document.createElement("input");
    champ.type = "text"; champ.inputMode = "numeric"; champ.placeholder = "code à 2 chiffres";
    champ.style.maxWidth = "12rem";
    if(etat.final.code) { champ.value = etat.final.code; champ.disabled = true; }
    e3.appendChild(champ);

    const retour3 = $("p", "retour");
    retour3.hidden = true;
    const valider3 = $("button", "bouton-principal", "Ouvrir le cadenas");
    valider3.type = "button";
    valider3.style.marginLeft = ".6rem";
    const codeAttendu = calculer(F.cadenas.termes);
    valider3.addEventListener("click", () => {
      if(codeAttendu === null){
        APP.message("Il te manque des indices chiffrés pour trouver le code.", "erreur"); return;
      }
      if(parseInt(champ.value, 10) === codeAttendu){
        etat.final.code = codeAttendu;
        SAUVEGARDE.enregistrer();
        e3.classList.add("resolue");
        retour3.className = "retour bon";
        retour3.textContent = "✅ Clic. Le cadenas s'ouvre.";
        retour3.hidden = false;
        champ.disabled = true; valider3.disabled = true;
        verifierDenouement();
      } else {
        retour3.className = "retour faux";
        retour3.textContent = "Le cadenas résiste. Vérifie ton calcul.";
        retour3.hidden = false;
      }
    });
    e3.appendChild(valider3);
    e3.appendChild(retour3);
    if(etat.final.code){
      valider3.disabled = true;
      retour3.className = "retour bon";
      retour3.textContent = "✅ Le cadenas est ouvert.";
      retour3.hidden = false;
    }
    boite.appendChild(e3);

    /* ---- Dénouement et récompense ---- */
    const zoneFin = $("div");
    zoneFin.id = "zone-denouement";
    boite.appendChild(zoneFin);

    const pied = $("div", "pied-scene");
    const retourCarnet = $("button", "bouton-second", "← Revenir au carnet");
    retourCarnet.type = "button";
    retourCarnet.addEventListener("click", () => APP.afficherEcran("carnet"));
    pied.appendChild(retourCarnet);
    boite.appendChild(pied);

    scene.appendChild(boite);
    verifierDenouement();

    function verifierDenouement(){
      const e = SAUVEGARDE.lire();
      const zone = document.getElementById("zone-denouement");
      if(!zone) return;
      if(!(e.final.pays && e.final.colonne && e.final.code)){ zone.innerHTML = ""; return; }
      e.final.resolu = true;
      SAUVEGARDE.enregistrer();
      zone.innerHTML = "";
      const d = $("div", "narration");
      d.innerHTML = MISSION.final.denouement;
      zone.appendChild(d);
      zone.appendChild(recompense());
    }
  }

  /* ---------------------------------------------------------
     La récompense mystère (configurée par l'enseignant)
     --------------------------------------------------------- */
  function recompense(){
    const r = SAUVEGARDE.lire().recompense;
    const def = MISSION.final.recompenseParDefaut;
    const bloc = $("div", "recompense");
    bloc.appendChild($("h2", null, "🏆 " + ((r.active && r.titre) ? r.titre : def.titre)));

    const corps = $("div");
    if(r.active && r.texte){
      corps.innerHTML = "<p>" + r.texte.replace(/\n{2,}/g, "</p><p>").replace(/\n/g, "<br>") + "</p>";
    } else {
      corps.innerHTML = def.texte;
    }
    bloc.appendChild(corps);

    if(typeof MEDIAS !== "undefined"){
      bloc.appendChild(MEDIAS.bloc({
        base: (r.active && r.media) ? r.media : def.media,
        legende: ""
      }));
    }

    const b = $("button", "bouton-second", "🖨️ Imprimer le diplôme de mission");
    b.type = "button";
    b.addEventListener("click", () => IMPRESSION.diplome());
    bloc.appendChild(b);
    return bloc;
  }

  return { dessinerHub, dessinerIndices, ouvrirFinal, valeurSymbole,
           calculer, ecrireCalcul, ecrireCalculDetaille, estOuverte };
})();
