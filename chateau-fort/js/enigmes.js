/* ============================================================
   MOTEUR D'ÉNIGMES GÉNÉRIQUE — piloté par assets/data/enigmes.json
   ------------------------------------------------------------
   Aucune énigme n'est écrite en dur : chaque énigme est un objet
   JSON décrivant son TYPE et ses données. Dix types sont gérés :

     qcm          questions à choix unique (une ou plusieurs)
     vraifaux     affirmations à trancher
     association  relier deux colonnes
     ordre        remettre des éléments dans l'ordre (▲▼)
     tri          répartir des cartes dans des colonnes
     trous        texte à trous avec étiquettes
     lettres      cliquer des lettres cachées, dans l'ordre
     code         cadenas à composer (chiffres ou mots)
     intrus       trouver l'élément qui ne va pas avec les autres
     plan         placer des étiquettes sur les cases d'un schéma

   Différenciation : chaque énigme peut porter un bloc "cm1" et un
   bloc "cm2". À défaut, le bloc "commun" sert aux deux niveaux.

   Contrat avec app.js :
     enigmeHTML(e, numero, total)   → le HTML de la carte d'énigme
     activerEnigme(e, onReussite)   → branche les interactions
   ============================================================ */

/* ---- Utilitaires ---- */
function melanger(tab){
  const t = tab.slice();
  for(let i=t.length-1;i>0;i--){
    const j = Math.floor(Math.random()*(i+1));
    [t[i],t[j]] = [t[j],t[i]];
  }
  return t;
}
function echapper(s){
  return String(s==null?"":s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}
/** Données de l'énigme pour le niveau courant. */
function donneesNiveau(e){
  const n = (ETAT.niveau || "CM2").toLowerCase();
  return e[n] || e.commun || e.cm2 || e.cm1 || {};
}
/** Champ différencié : soit une chaîne, soit {cm1, cm2}. */
function texteNiveau(v){
  if(v == null) return "";
  if(typeof v === "string") return v;
  const n = (ETAT.niveau || "CM2").toLowerCase();
  return v[n] || v.commun || v.cm2 || v.cm1 || "";
}
/** Normalisation d'une saisie libre : casse, accents et espaces ignorés. */
function normaliser(s){
  return String(s||"")
    .trim().toLowerCase()
    .normalize("NFD").replace(/[̀-ͯ]/g,"")
    .replace(/[^a-z0-9]/g,"");
}

/* ============================================================
   RENDU DE LA CARTE D'ÉNIGME
   ============================================================ */
function enigmeHTML(e, numero, total){
  const d = donneesNiveau(e);
  const consigne = texteNiveau(e.consigne);
  const corps = ({
    qcm: corpsQcm, vraifaux: corpsVraiFaux, association: corpsAssociation,
    ordre: corpsOrdre, tri: corpsTri, trous: corpsTrous, lettres: corpsLettres,
    code: corpsCode, intrus: corpsIntrus, plan: corpsPlan
  }[e.type] || (()=>`<p class="feedback erreur show">Type d'énigme inconnu : ${echapper(e.type)}</p>`))(d, e);

  return `
    <div class="enigme-carte" id="enigme-${e.id}" data-type="${echapper(e.type)}">
      <div class="enigme-tete">
        <span class="enigme-num">Énigme ${numero}/${total}</span>
        <h3>${echapper(e.titre)}</h3>
      </div>
      ${consigne ? `<div class="consigne">${consigne}</div>` : ""}
      ${mediaEnigmeHTML(e)}
      <div class="enigme-corps">${corps}</div>
      <div class="feedback" id="fb-${e.id}"></div>
      <div class="barre-outils">
        <button class="btn or petit" id="indice-${e.id}">💡 Indice</button>
        ${(e.lecon && (!window.ETAT || !ETAT.reglages || ETAT.reglages.leconsAutorisees !== false))
          ? `<button class="btn gris petit" data-fiche="${echapper(e.lecon)}" title="Ouvrir la leçon qui explique cette énigme">📚 Leçon</button>` : ""}
        ${e.source ? `<span class="source-enigme">Source : ${echapper(e.source)}</span>` : ""}
      </div>
    </div>`;
}

/* ---- Ouvrir la leçon rattachée à l'énigme (champ "lecon") ----
   Ouvre la bibliothèque (📚) directement sur la bonne leçon. */
async function ouvrirFicheSource(id){
  if(typeof ouvrirBiblioLecons !== "function") return;
  await ouvrirBiblioLecons();
  if(typeof afficherLecon === "function") afficherLecon(id);
}

/* ---- Illustration ou vidéo facultative de l'énigme ----
   L'enseignant dépose <base>.jpg dans assets/images/cartes/ ou
   <base>.mp4 dans assets/videos/ : le fichier apparaît ici. Sans
   fichier, un encadré discret rappelle le nom attendu. */
function mediaEnigmeHTML(e){
  if(!e.media) return "";
  const m = e.media;
  if(m.type === "video" && typeof htmlVideoDoc === "function"){
    return htmlVideoDoc(m.base, m.legende || "", m.source || "");
  }
  if(typeof htmlIllustration === "function"){
    return htmlIllustration(m.base, m.legende || "", m.source || "");
  }
  return "";
}

/* ============================================================
   TYPE 1 — QCM (une ou plusieurs questions à choix unique)
   ============================================================ */
function corpsQcm(d){
  return `<div class="bloc-qcm">${(d.questions||[]).map((q,i)=>`
    <div class="qcm-question" data-i="${i}">
      <div class="q">${q.q}</div>
      ${melanger((q.options||[]).map((o,j)=>({o,j}))).map(({o,j})=>
        `<label class="qcm-option" data-j="${j}">${o}</label>`).join("")}
      <div class="explication" data-exp="${i}">${q.explication ? echapper(q.explication) : ""}</div>
    </div>`).join("")}
    <div class="center"><button class="btn vert" data-valider="1">✅ Vérifier mes réponses</button></div>
  </div>`;
}
function activerQcm(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  const choix = {};
  carte.querySelectorAll(".qcm-question").forEach(qi=>{
    const i = +qi.dataset.i;
    qi.querySelectorAll(".qcm-option").forEach(opt=>{
      opt.addEventListener("click", ()=>{
        if(qi.classList.contains("verrouille")) return;
        qi.querySelectorAll(".qcm-option").forEach(x=>x.classList.remove("select"));
        opt.classList.add("select");
        choix[i] = +opt.dataset.j;
      });
    });
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const qs = d.questions||[];
    if(Object.keys(choix).length < qs.length){ rater("Il reste une question sans réponse."); return; }
    let justes = 0;
    qs.forEach((q,i)=>{
      const qi = carte.querySelector(`.qcm-question[data-i="${i}"]`);
      const opt = qi.querySelector(`.qcm-option[data-j="${choix[i]}"]`);
      if(choix[i] === q.bonne){ justes++; opt.classList.add("bien"); opt.classList.remove("select"); }
      else{ opt.classList.add("mal"); setTimeout(()=>opt.classList.remove("mal"),600); }
    });
    if(justes === qs.length){
      qs.forEach((q,i)=>{
        const qi = carte.querySelector(`.qcm-question[data-i="${i}"]`);
        qi.classList.add("verrouille");
        const exp = qi.querySelector(".explication");
        if(exp && exp.textContent.trim()) exp.classList.add("show");
      });
      reussir();
    }else{
      rater(`${justes} bonne${justes>1?"s":""} réponse${justes>1?"s":""} sur ${qs.length}. Corrige et revérifie.`);
    }
  });
}

/* ============================================================
   TYPE 2 — VRAI / FAUX
   ============================================================ */
function corpsVraiFaux(d){
  return `<div class="bloc-vf">
    ${(d.affirmations||[]).map((a,i)=>`
      <div class="vf-ligne" data-i="${i}">
        <div class="vf-txt">${a.txt}</div>
        <div class="vf-boutons">
          <button class="btn petit vf-btn" data-rep="vrai">Vrai</button>
          <button class="btn petit vf-btn" data-rep="faux">Faux</button>
        </div>
        <div class="explication" data-exp="${i}">${a.explication ? echapper(a.explication) : ""}</div>
      </div>`).join("")}
    <div class="center"><button class="btn vert" data-valider="1">✅ Vérifier</button></div>
  </div>`;
}
function activerVraiFaux(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  const rep = {};
  carte.querySelectorAll(".vf-ligne").forEach(l=>{
    const i = +l.dataset.i;
    l.querySelectorAll(".vf-btn").forEach(b=>{
      b.addEventListener("click", ()=>{
        if(l.classList.contains("verrouille")) return;
        l.querySelectorAll(".vf-btn").forEach(x=>x.classList.remove("select"));
        b.classList.add("select");
        rep[i] = b.dataset.rep === "vrai";
      });
    });
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const aff = d.affirmations||[];
    if(Object.keys(rep).length < aff.length){ rater("Réponds à toutes les affirmations."); return; }
    let justes = 0;
    aff.forEach((a,i)=>{
      const l = carte.querySelector(`.vf-ligne[data-i="${i}"]`);
      if(rep[i] === !!a.vrai){ justes++; l.classList.add("bien"); }
      else{ l.classList.remove("bien"); l.classList.add("mal"); setTimeout(()=>l.classList.remove("mal"),700); }
    });
    if(justes === aff.length){
      aff.forEach((a,i)=>{
        const l = carte.querySelector(`.vf-ligne[data-i="${i}"]`);
        l.classList.add("verrouille");
        const exp = l.querySelector(".explication");
        if(exp && exp.textContent.trim()) exp.classList.add("show");
      });
      reussir();
    }else{
      rater(`${justes} sur ${aff.length}. Les lignes en vert sont justes : reprends les autres.`);
    }
  });
}

/* ============================================================
   TYPE 3 — ASSOCIATION (relier deux colonnes)
   ============================================================ */
function corpsAssociation(d){
  const paires = d.paires||[];
  const gauche = paires.map((p,i)=>({...p, id:"g"+i, bon:"d"+i}));
  const droite = melanger(paires.map((p,i)=>({...p, id:"d"+i})));
  return `<div class="rang-match">
    <div class="colonne-match" data-col="g">
      ${gauche.map(p=>`<div class="carte-match" data-id="${p.id}" data-bon="${p.bon}">${p.icone?`<span class="emoji">${p.icone}</span>`:""}${p.g}</div>`).join("")}
    </div>
    <div class="colonne-match" data-col="d">
      ${droite.map(p=>`<div class="carte-match" data-id="${p.id}">${p.d}</div>`).join("")}
    </div>
  </div>`;
}
function activerAssociation(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  let sel = null;
  carte.querySelectorAll('[data-col="g"] .carte-match').forEach(c=>{
    c.addEventListener("click", ()=>{
      if(c.classList.contains("bien")) return;
      carte.querySelectorAll('[data-col="g"] .carte-match').forEach(x=>x.classList.remove("select"));
      c.classList.add("select"); sel = c;
    });
  });
  carte.querySelectorAll('[data-col="d"] .carte-match').forEach(c=>{
    c.addEventListener("click", ()=>{
      if(!sel){ rater("Choisis d'abord un élément dans la colonne de gauche."); return; }
      if(c.classList.contains("bien")) return;
      if(sel.dataset.bon === c.dataset.id){
        sel.classList.add("bien"); sel.classList.remove("select");
        c.classList.add("bien"); sel = null;
        if(carte.querySelectorAll('[data-col="g"] .carte-match:not(.bien)').length === 0) reussir();
      }else{
        c.classList.add("mal"); setTimeout(()=>c.classList.remove("mal"),500);
        rater("Ce n'est pas la bonne association.");
      }
    });
  });
}

/* ============================================================
   TYPE 4 — ORDRE (remettre dans l'ordre avec ▲▼)
   ============================================================ */
function corpsOrdre(d){
  const items = melanger((d.items||[]).map((it,i)=>({...it, rang: it.rang!=null?it.rang:i+1})));
  return `<div class="liste-ordre">
    ${items.map(it=>`<div class="item-ordre" data-rang="${it.rang}">
      <span class="rang"></span>
      <div class="contenu"><b>${it.txt}</b>${it.sous?`<br><span class="sous">${it.sous}</span>`:""}</div>
      <div class="controles-ordre">
        <button class="btn-monter" aria-label="Monter">▲</button>
        <button class="btn-descendre" aria-label="Descendre">▼</button>
      </div>
    </div>`).join("")}
  </div>
  <div class="center"><button class="btn vert" data-valider="1">✅ Vérifier l'ordre</button></div>`;
}
function activerOrdre(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  const liste = carte.querySelector(".liste-ordre");
  const renumeroter = ()=> liste.querySelectorAll(".item-ordre").forEach((it,i)=>{
    it.querySelector(".rang").textContent = i+1;
  });
  renumeroter();
  liste.addEventListener("click", ev=>{
    const it = ev.target.closest(".item-ordre");
    if(!it) return;
    if(ev.target.classList.contains("btn-monter") && it.previousElementSibling){
      liste.insertBefore(it, it.previousElementSibling); renumeroter();
    }
    if(ev.target.classList.contains("btn-descendre") && it.nextElementSibling){
      liste.insertBefore(it.nextElementSibling, it); renumeroter();
    }
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const items = [...liste.querySelectorAll(".item-ordre")];
    let justes = 0;
    items.forEach((it,i)=>{
      const ok = +it.dataset.rang === i+1;
      it.classList.toggle("bien", ok);
      it.classList.toggle("mal", !ok);
      if(ok) justes++;
    });
    if(justes === items.length){
      items.forEach(it=>it.classList.add("verrouille"));
      reussir();
    }else{
      setTimeout(()=>items.forEach(it=>it.classList.remove("mal")),900);
      rater(`${justes} élément${justes>1?"s":""} bien placé${justes>1?"s":""} sur ${items.length}.`);
    }
  });
}

/* ============================================================
   TYPE 5 — TRI (répartir des cartes dans des colonnes)
   ============================================================ */
function corpsTri(d){
  const cartes = melanger((d.cartes||[]).map((c,i)=>({...c, id:"c"+i})));
  return `<div class="tri-reserve" data-reserve="1">
      ${cartes.map(c=>`<div class="carte-tri" data-id="${c.id}" data-col="${echapper(c.col)}">${c.icone?`<span class="emoji">${c.icone}</span>`:""}${c.txt}</div>`).join("")}
    </div>
    <div class="tri-colonnes">
      ${(d.colonnes||[]).map(col=>`<div class="tri-colonne" data-col="${echapper(col.id)}">
        <div class="tri-titre">${col.icone?col.icone+" ":""}${col.titre}</div>
        <div class="tri-zone"></div>
      </div>`).join("")}
    </div>
    <div class="center"><button class="btn vert" data-valider="1">✅ Vérifier le classement</button></div>`;
}
function activerTri(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  const reserve = carte.querySelector(".tri-reserve");
  let sel = null;
  const choisir = el=>{
    carte.querySelectorAll(".carte-tri").forEach(x=>x.classList.remove("select"));
    el.classList.add("select"); sel = el;
  };
  carte.addEventListener("click", ev=>{
    const c = ev.target.closest(".carte-tri");
    if(c){ if(!c.classList.contains("verrouille")) choisir(c); return; }
    const zone = ev.target.closest(".tri-zone");
    if(zone && sel){ zone.appendChild(sel); sel.classList.remove("select"); sel = null; return; }
    if(ev.target.closest(".tri-reserve") && sel){ reserve.appendChild(sel); sel.classList.remove("select"); sel = null; }
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const restantes = reserve.querySelectorAll(".carte-tri").length;
    if(restantes){ rater(`Il reste ${restantes} étiquette${restantes>1?"s":""} à classer.`); return; }
    let justes = 0, total = 0;
    carte.querySelectorAll(".tri-colonne").forEach(col=>{
      col.querySelectorAll(".carte-tri").forEach(c=>{
        total++;
        const ok = c.dataset.col === col.dataset.col;
        c.classList.toggle("bien", ok); c.classList.toggle("mal", !ok);
        if(ok) justes++;
      });
    });
    if(justes === total){
      carte.querySelectorAll(".carte-tri").forEach(c=>c.classList.add("verrouille"));
      reussir();
    }else{
      setTimeout(()=>carte.querySelectorAll(".carte-tri").forEach(c=>c.classList.remove("mal")),900);
      rater(`${justes} carte${justes>1?"s":""} bien classée${justes>1?"s":""} sur ${total}. Déplace celles qui restent.`);
    }
  });
}

/* ============================================================
   TYPE 6 — TEXTE À TROUS
   Le texte contient des marqueurs [[reponse]] ; les étiquettes
   proposées mélangent les bonnes réponses et des distracteurs.
   ============================================================ */
function corpsTrous(d){
  let n = 0;
  const bonnes = [];
  const texte = String(d.texte||"").replace(/\[\[(.+?)\]\]/g, (_, rep)=>{
    bonnes.push(rep);
    return `<span class="trou" data-i="${n++}" data-rep="${echapper(rep)}"></span>`;
  });
  const etiquettes = melanger((d.etiquettes && d.etiquettes.length) ? d.etiquettes : bonnes);
  return `<div class="texte-trous">${texte}</div>
    <div class="etiquettes">
      ${etiquettes.map(t=>`<span class="etiquette" data-mot="${echapper(t)}">${echapper(t)}</span>`).join("")}
    </div>
    <div class="center"><button class="btn vert" data-valider="1">✅ Vérifier le texte</button></div>`;
}
function activerTrous(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  let sel = null;
  carte.querySelectorAll(".etiquette").forEach(et=>{
    et.addEventListener("click", ()=>{
      if(et.classList.contains("posee")) return;
      carte.querySelectorAll(".etiquette").forEach(x=>x.classList.remove("select"));
      et.classList.add("select"); sel = et;
    });
  });
  carte.querySelectorAll(".trou").forEach(tr=>{
    tr.addEventListener("click", ()=>{
      if(tr.classList.contains("verrouille")) return;
      // Reposer l'étiquette déjà présente dans la réserve
      if(tr.dataset.pose){
        const anc = carte.querySelector(`.etiquette.posee[data-mot="${CSS.escape(tr.dataset.pose)}"]`);
        if(anc) anc.classList.remove("posee");
        tr.textContent = ""; delete tr.dataset.pose;
        tr.classList.remove("rempli");
        if(!sel) return;
      }
      if(!sel){ rater("Choisis d'abord une étiquette."); return; }
      tr.textContent = sel.dataset.mot;
      tr.dataset.pose = sel.dataset.mot;
      tr.classList.add("rempli");
      sel.classList.add("posee"); sel.classList.remove("select"); sel = null;
    });
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const trous = [...carte.querySelectorAll(".trou")];
    if(trous.some(t=>!t.dataset.pose)){ rater("Tous les trous ne sont pas remplis."); return; }
    let justes = 0;
    trous.forEach(t=>{
      const ok = normaliser(t.dataset.pose) === normaliser(t.dataset.rep);
      t.classList.toggle("bien", ok); t.classList.toggle("mal", !ok);
      if(ok) justes++;
    });
    if(justes === trous.length){
      trous.forEach(t=>t.classList.add("verrouille"));
      reussir();
    }else{
      setTimeout(()=>trous.forEach(t=>t.classList.remove("mal")),900);
      rater(`${justes} mot${justes>1?"s":""} bien placé${justes>1?"s":""} sur ${trous.length}.`);
    }
  });
}

/* ============================================================
   TYPE 7 — LETTRES CACHÉES (cliquer dans l'ordre)
   ============================================================ */
function corpsLettres(d){
  const cible = d.cible || [];
  return `<div class="slots">${cible.map(()=>'<div class="slot vide"></div>').join("")}</div>
    <div class="texte-doc">${d.texte||""}</div>`;
}
function activerLettres(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  const cible = d.cible || [];
  let pos = 0;
  const slots = carte.querySelectorAll(".slot");
  carte.querySelectorAll("[data-l]").forEach(l=>{
    l.classList.add("lettre-clic");
    l.addEventListener("click", ()=>{
      if(l.classList.contains("utilisee")) return;
      if(l.dataset.l === cible[pos]){
        l.classList.add("utilisee");
        const s = slots[pos];
        s.classList.remove("vide"); s.classList.add("ok"); s.textContent = cible[pos];
        pos++;
        if(pos === cible.length) reussir();
      }else{
        l.classList.add("mal"); setTimeout(()=>l.classList.remove("mal"),400);
        rater("Pas dans le bon ordre : cherche la lettre suivante du mot.");
      }
    });
  });
}

/* ============================================================
   TYPE 8 — CODE (cadenas à composer)
   ============================================================ */
function corpsCode(d){
  return `<div class="cadenas">
    ${(d.champs||[]).map((c,i)=>`
      <div class="cadenas-champ">
        <label for="code-${i}">${c.libelle}</label>
        <input type="text" id="code-${i}" data-i="${i}" inputmode="${c.numerique===false?"text":"numeric"}"
               maxlength="${c.longueur||6}" autocomplete="off" placeholder="${"·".repeat(c.longueur||4)}">
      </div>`).join("")}
    <button class="btn vert" data-valider="1">🔓 Ouvrir</button>
  </div>`;
}
function activerCode(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  const champs = d.champs||[];
  const valider = ()=>{
    let justes = 0;
    champs.forEach((c,i)=>{
      const inp = carte.querySelector(`#code-${i}`);
      const ok = normaliser(inp.value) === normaliser(c.valeur);
      inp.classList.toggle("bien", ok); inp.classList.toggle("mal", !ok);
      if(ok) justes++;
    });
    if(justes === champs.length){
      carte.querySelectorAll(".cadenas input").forEach(i=>i.disabled = true);
      reussir();
    }else{
      setTimeout(()=>carte.querySelectorAll(".cadenas input").forEach(i=>i.classList.remove("mal")),900);
      rater(`${justes} champ${justes>1?"s":""} correct${justes>1?"s":""} sur ${champs.length}.`);
    }
  };
  carte.querySelector("[data-valider]").addEventListener("click", valider);
  carte.querySelectorAll(".cadenas input").forEach(inp=>{
    inp.addEventListener("keydown", ev=>{ if(ev.key === "Enter") valider(); });
  });
}

/* ============================================================
   TYPE 9 — INTRUS
   ============================================================ */
function corpsIntrus(d){
  const cartes = melanger((d.cartes||[]).map((c,i)=>({...c, id:"i"+i})));
  return `<div class="grille-intrus">
    ${cartes.map(c=>`<div class="carte-intrus" data-intrus="${c.intrus?1:0}">
      ${c.icone?`<span class="emoji">${c.icone}</span>`:""}
      <div class="txt">${c.txt}</div>
      ${c.sous?`<div class="sous">${c.sous}</div>`:""}
    </div>`).join("")}
  </div>`;
}
function activerIntrus(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  carte.querySelectorAll(".carte-intrus").forEach(c=>{
    c.addEventListener("click", ()=>{
      if(carte.dataset.fini) return;
      if(c.dataset.intrus === "1"){
        carte.dataset.fini = "1";
        c.classList.add("bien");
        reussir();
      }else{
        c.classList.add("mal"); setTimeout(()=>c.classList.remove("mal"),600);
        rater("Celui-là est bien à sa place. Cherche encore.");
      }
    });
  });
}

/* ============================================================
   TYPE 10 — PLAN (placer des étiquettes sur les cases d'un schéma)
   ============================================================ */
function corpsPlan(d){
  const cases = d.cases||[];
  const etiquettes = melanger((d.etiquettes && d.etiquettes.length)
    ? d.etiquettes : cases.map(c=>c.reponse));
  const cols = d.colonnes || 3;
  return `
    ${d.titre?`<div class="plan-titre">${d.titre}</div>`:""}
    <div class="plan-grille" style="--plan-cols:${cols}">
      ${cases.map(c=>`<div class="plan-case" data-rep="${echapper(c.reponse)}"
            ${c.span?`style="grid-column:span ${c.span}"`:""}>
        <div class="plan-libelle">${c.libelle||""}</div>
        <div class="plan-slot"></div>
      </div>`).join("")}
    </div>
    <div class="etiquettes">
      ${etiquettes.map(t=>`<span class="etiquette" data-mot="${echapper(t)}">${echapper(t)}</span>`).join("")}
    </div>
    <div class="center"><button class="btn vert" data-valider="1">✅ Vérifier le schéma</button></div>`;
}
function activerPlan(e, d, reussir, rater){
  const carte = document.getElementById("enigme-"+e.id);
  let sel = null;
  carte.querySelectorAll(".etiquette").forEach(et=>{
    et.addEventListener("click", ()=>{
      if(et.classList.contains("posee")) return;
      carte.querySelectorAll(".etiquette").forEach(x=>x.classList.remove("select"));
      et.classList.add("select"); sel = et;
    });
  });
  carte.querySelectorAll(".plan-case").forEach(cs=>{
    cs.addEventListener("click", ()=>{
      if(cs.classList.contains("verrouille")) return;
      const slot = cs.querySelector(".plan-slot");
      if(cs.dataset.pose){
        const anc = carte.querySelector(`.etiquette.posee[data-mot="${CSS.escape(cs.dataset.pose)}"]`);
        if(anc) anc.classList.remove("posee");
        slot.textContent = ""; delete cs.dataset.pose; cs.classList.remove("rempli");
        if(!sel) return;
      }
      if(!sel){ rater("Choisis d'abord une étiquette."); return; }
      slot.textContent = sel.dataset.mot;
      cs.dataset.pose = sel.dataset.mot;
      cs.classList.add("rempli");
      sel.classList.add("posee"); sel.classList.remove("select"); sel = null;
    });
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const cases = [...carte.querySelectorAll(".plan-case")];
    if(cases.some(c=>!c.dataset.pose)){ rater("Toutes les cases ne sont pas remplies."); return; }
    let justes = 0;
    cases.forEach(c=>{
      const ok = normaliser(c.dataset.pose) === normaliser(c.dataset.rep);
      c.classList.toggle("bien", ok); c.classList.toggle("mal", !ok);
      if(ok) justes++;
    });
    if(justes === cases.length){
      cases.forEach(c=>c.classList.add("verrouille"));
      reussir();
    }else{
      setTimeout(()=>cases.forEach(c=>c.classList.remove("mal")),900);
      rater(`${justes} case${justes>1?"s":""} juste${justes>1?"s":""} sur ${cases.length}.`);
    }
  });
}

/* ============================================================
   BRANCHEMENT DES INTERACTIONS
   ============================================================ */
const ACTIVATEURS = {
  qcm: activerQcm, vraifaux: activerVraiFaux, association: activerAssociation,
  ordre: activerOrdre, tri: activerTri, trous: activerTrous, lettres: activerLettres,
  code: activerCode, intrus: activerIntrus, plan: activerPlan
};

/**
 * Branche une énigme affichée.
 * @param {object} e        l'énigme (objet JSON)
 * @param {function} onReussite  appelée une fois l'énigme résolue
 */
function activerEnigme(e, onReussite){
  const d = donneesNiveau(e);
  const carte = document.getElementById("enigme-"+e.id);
  if(!carte) return;
  const fb = carte.querySelector("#fb-"+e.id);
  let resolu = false;

  const rater = msg=>{
    if(resolu) return;
    if(typeof son === "function") son("erreur");
    fb.className = "feedback erreur show";
    fb.innerHTML = "✋ " + msg;
    clearTimeout(fb._t);
    fb._t = setTimeout(()=>fb.classList.remove("show"), 3200);
  };
  const reussir = ()=>{
    if(resolu) return;
    resolu = true;
    if(typeof son === "function") son("succes");
    fb.className = "feedback succes show";
    const corr = texteNiveau(e.correction);
    fb.innerHTML = "✨ Bien vu ! " + (corr ? `<div class="correction">${corr}</div>` : "")
      + (e.source ? `<div class="source-correction">Source : ${echapper(e.source)}</div>` : "");
    carte.classList.add("resolue");
    const bi = carte.querySelector("#indice-"+e.id);
    if(bi) bi.disabled = true;
    setTimeout(()=>onReussite(e, indicesUtilises), 700);
  };

  const bf = carte.querySelector("[data-fiche]");
  if(bf) bf.addEventListener("click", ()=>ouvrirFicheSource(bf.dataset.fiche));

  (ACTIVATEURS[e.type] || (()=>{}))(e, d, reussir, rater);

  /* ---- Indices progressifs (−2 points chacun) ---- */
  let indicesUtilises = 0;
  const indices = (()=>{
    const src = e.indices || {};
    if(Array.isArray(src)) return src;
    const n = (ETAT.niveau||"CM2").toLowerCase();
    return src[n] || src.commun || src.cm2 || src.cm1 || [];
  })();
  const btn = carte.querySelector("#indice-"+e.id);
  if(btn){
    btn.addEventListener("click", ()=>{
      if(indicesUtilises >= indices.length){ btn.textContent = "💡 Plus d'indices"; btn.disabled = true; return; }
      const bulle = document.createElement("div");
      bulle.className = "feedback indice show";
      bulle.innerHTML = "💡 " + indices[indicesUtilises];
      carte.querySelector(".enigme-corps").after(bulle);
      indicesUtilises++;
      if(typeof penaliserIndice === "function") penaliserIndice();
      btn.textContent = indicesUtilises < indices.length ? "💡 Indice suivant" : "💡 Plus d'indices";
      bulle.scrollIntoView({behavior:"smooth", block:"center"});
    });
  }
}

window.ouvrirFicheSource = ouvrirFicheSource;
window.enigmeHTML     = enigmeHTML;
window.activerEnigme  = activerEnigme;
window.donneesNiveau  = donneesNiveau;
window.texteNiveau    = texteNiveau;
window.melanger       = melanger;
window.normaliser     = normaliser;
