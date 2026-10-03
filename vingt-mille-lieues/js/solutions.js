/* ============================================================
   SOLUTIONS — texte des corrigés, pour l'enseignant uniquement
   ------------------------------------------------------------
   Utilisé par ⚙️ → Impression → Corrigés, par prof.html et par
   outils/generer-readme.js (README.md : toutes les solutions, tous
   les grades). Fonctionne dans le navigateur et dans Node.
   ============================================================ */
(function(racine){
  const VML = racine.VML || (racine.VML = {});
  const nettoie = s => String(s == null ? "" : s).replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();

  VML.solutionTexte = function(e, grade){
    const b = e[grade] || {};
    const type = b.type || e.type;
    const L = [];
    if(type === "tri"){
      (b.colonnes || []).forEach(c => L.push(`${nettoie(c.titre)} : ${(b.cartes || []).filter(x => x.col === c.id).map(x => nettoie(x.txt)).join(", ")}`));
    }else if(type === "association"){
      (b.paires || []).forEach(p => L.push(`${nettoie(p.g)} → ${nettoie(p.d)}`));
    }else if(type === "ordre"){
      L.push((b.items || []).map((it, i) => `${i + 1}. ${nettoie(it.txt)}`).join(" ; "));
    }else if(type === "trous"){
      L.push("Mots : " + [...String(b.texte || "").matchAll(/\[\[(.+?)\]\]/g)].map(m => m[1]).join(", "));
      const bonnes = [...String(b.texte || "").matchAll(/\[\[(.+?)\]\]/g)].map(m => m[1]);
      const leurres = (b.etiquettes || []).filter(x => !bonnes.includes(x));
      if(leurres.length) L.push("Étiquettes pièges : " + leurres.join(", "));
    }else if(type === "qcm"){
      (b.questions || []).forEach((q, i) => L.push(`Q${i + 1} : ${nettoie(q.options[q.bonne])}`));
    }else if(type === "circuit"){
      const a = b.attendu || {};
      const nom = id => ((b.composants || []).find(c => c.id === id) || {}).libelle || id;
      const amovibles = (b.fils || []).filter(f => !f.fixe);
      if(amovibles.length) L.push("Retirer : " + amovibles.map(f => f.libelle || (f.de + "–" + f.a)).join(", ") + " (court-circuit).");
      if(a.independants && a.independants.length){
        const k = Object.keys(a.commande || {});
        L.push(`Montage en dérivation : une boucle par appareil depuis les piles (${(a.allumes || []).map(nom).join(", ")})` + (k.length ? `, l'interrupteur ${k.join(", ")} placé seulement dans la boucle de ${(a.commande[k[0]] || []).map(nom).join(", ")}, et fermé.` : "."));
      }else if(a.commande && Object.keys(a.commande).length){
        const k = Object.keys(a.commande)[0];
        L.push(`Une seule boucle (série) : + → ${nom(k)} → ${(a.allumes || []).map(nom).join(" → ")} → −, ${nom(k)} fermé.`);
      }else{
        L.push(`Boucle fermée : + → ${(a.allumes || []).map(nom).join(" → ")} → −.`);
      }
      L.push("Tout montage qui remplit ces conditions est accepté (simulation du courant).");
    }else if(type === "intrus"){
      L.push("Intrus : " + nettoie(((b.cartes || []).find(c => c.intrus) || {}).txt));
    }else if(type === "code"){
      L.push((b.champs || []).map(c => `${nettoie(c.libelle)} ${c.valeur}`).join(" ; "));
    }else if(type === "vraifaux"){
      (b.affirmations || []).forEach(a => L.push(`${a.vrai ? "VRAI" : "FAUX"} — ${nettoie(a.txt)}`));
    }else if(type === "lettres"){
      L.push("Mot : " + (b.cible || []).join(""));
    }else if(type === "plan"){
      (b.cases || []).forEach(c => L.push(`${nettoie(c.libelle)} : ${c.reponse}`));
    }
    if((grade === "lieutenant" || grade === "second") && b.justification){
      L.push(`Justification : « ${nettoie(b.justification.options[b.justification.bonne])} »`);
    }
    return L;
  };
})(typeof window !== "undefined" ? window : globalThis);
