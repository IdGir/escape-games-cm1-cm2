/* TRONC COMMUN (commun/js/) — un seul fichier pour tous les jeux : les textes
   propres à chaque jeu sont dans <jeu>/js/jeu.js (objet JEU). */
/* ============================================================
   MOTEUR D'ÉNIGMES GÉNÉRIQUE — piloté par assets/data/enigmes.json
   (version 2, octobre 2026 — modèle commun : outils-moteur/enigmes.js)
   ------------------------------------------------------------
   Aucune énigme n'est écrite en dur : chaque énigme est un objet
   JSON décrivant son TYPE et ses données. Dix types sont gérés :

     qcm          questions à choix unique (une ou plusieurs)
     vraifaux     affirmations à trancher
     association  relier deux colonnes
     ordre        remettre des éléments dans l'ordre (▲▼)
     tri          répartir des cartes dans des colonnes
     trous        texte à trous avec étiquettes
     lettres      retrouver les lettres cachées et les remettre
                  dans l'ordre (anagramme ; certaines sont des leurres)
     code         cadenas à composer (chiffres ou mots)
     intrus       trouver l'élément qui ne va pas avec les autres
     plan         placer des étiquettes sur les cases d'un schéma
     instrument   lire ou régler un instrument gradué (thermomètre, pluviomètre)

   Règles de jeu (version 2) :
     - chaque énigme se valide d'un seul coup (bouton « Vérifier ») :
       une vérification fausse compte comme UNE erreur ;
     - après une erreur, l'élève apprend seulement COMBIEN de
       réponses sont justes, jamais lesquelles : il doit retourner à
       la leçon ;
     - « tout juste du premier coup » rapporte PTS_PREMIER_COUP
       (app.js), une énigme résolue après erreur PTS_APRES_ERREUR ;
     - aucun texte n'apparaît après la résolution (ni correction, ni
       explication) : l'énigme suivante est proposée tout de suite.

   Différenciation : chaque énigme peut porter un bloc "cm1" et un
   bloc "cm2". À défaut, le bloc "commun" sert aux deux niveaux.

   Contrat avec app.js :
     enigmeHTML(e, numero, total)        → le HTML de la carte d'énigme
     activerEnigme(e, onReussite)        → branche les interactions ;
       onReussite(e, indicesUtilises, erreurs)
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
const pluriel = (n, mot, motPl) => n + " " + (n > 1 ? (motPl || mot + "s") : mot);

/* Libellé du bouton de leçon (un jeu peut le changer : « 📚 Fiche source »). */
const LIBELLE_BOUTON_LECON = ((typeof JEU !== "undefined" && JEU.enigmes && JEU.enigmes.libelleBoutonLecon) || "📚 Leçon");
const TITRE_BOUTON_LECON = ((typeof JEU !== "undefined" && JEU.enigmes && JEU.enigmes.titreBoutonLecon) || "Ouvrir la leçon liée à cette énigme");

/* ============================================================
   RENDU DE LA CARTE D'ÉNIGME
   ============================================================ */
const CORPS = {
  qcm: corpsQcm, vraifaux: corpsVraiFaux, association: corpsAssociation,
  ordre: corpsOrdre, tri: corpsTri, trous: corpsTrous, lettres: corpsLettres,
  code: corpsCode, intrus: corpsIntrus, plan: corpsPlan, instrument: corpsInstrument
};
function enigmeHTML(e, numero, total){
  const d = donneesNiveau(e);
  const consigne = texteNiveau(e.consigne);
  const corps = (CORPS[e.type] || (()=>`<p class="feedback erreur show">Type d'énigme inconnu : ${echapper(e.type)}</p>`))(d, e);

  return `
    <div class="enigme-carte" id="enigme-${e.id}" data-type="${echapper(e.type)}">
      <div class="enigme-tete">
        <span class="enigme-num">Énigme ${numero}/${total}</span>
        <h3>${echapper(e.titre)}</h3>
      </div>
      <div class="bandeau-bareme" title="Vérifiez dans la leçon avant de valider">
        🎯 Tout juste du premier coup : <b>${typeof PTS_PREMIER_COUP !== "undefined" ? PTS_PREMIER_COUP : 10} points</b>
        · après une erreur : ${typeof PTS_APRES_ERREUR !== "undefined" ? PTS_APRES_ERREUR : 3} points seulement
      </div>
      ${consigne ? `<div class="consigne">${consigne}</div>` : ""}
      ${mediaEnigmeHTML(e)}
      <div class="enigme-corps">${corps}</div>
      <div class="feedback" id="fb-${e.id}"></div>
      <div class="barre-outils">
        <button class="btn or petit" id="indice-${e.id}">💡 Indice</button>
        ${(e.lecon && (!window.ETAT || !ETAT.reglages || ETAT.reglages.leconsAutorisees !== false))
          ? `<button class="btn gris petit" data-fiche="${echapper(e.lecon)}" title="${TITRE_BOUTON_LECON}">${LIBELLE_BOUTON_LECON}</button>` : ""}
        ${e.source ? `<span class="source-enigme">Source : ${echapper(e.source)}</span>` : ""}
      </div>
    </div>`;
}

/* ---- Ouvrir la leçon liée à l'énigme ----
   Ouvre la bibliothèque (📚) directement sur la bonne leçon. */
async function ouvrirFicheSource(id){
  if(typeof ouvrirBiblioLecons !== "function") return;
  await ouvrirBiblioLecons();
  if(typeof afficherLecon === "function") afficherLecon(id);
}

/* ---- Illustration ou vidéo facultative de l'énigme ---- */
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

/* Bouton de validation commun */
const BOUTON_VERIFIER = libelle => `<div class="center"><button class="btn vert" data-valider="1">✅ ${libelle || "Vérifier"}</button></div>`;

/* ============================================================
   Contrat des activateurs :
     activerX(e, d, api)   api = {reussir, erreur, incomplet}
       erreur(justes, total, unite)  → une vérification fausse
       incomplet(msg)                → rien n'est compté (réponse incomplète)
   ============================================================ */

/* ============================================================
   TYPE 1 — QCM (une ou plusieurs questions à choix unique)
   ============================================================ */
function corpsQcm(d){
  return `<div class="bloc-qcm">${(d.questions||[]).map((q,i)=>`
    <div class="qcm-question" data-i="${i}">
      <div class="q">${q.q}</div>
      ${melanger((q.options||[]).map((o,j)=>({o,j}))).map(({o,j})=>
        `<label class="qcm-option" data-j="${j}">${o}</label>`).join("")}
    </div>`).join("")}
    ${BOUTON_VERIFIER("Vérifier mes réponses")}
  </div>`;
}
function activerQcm(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  const choix = {};
  carte.querySelectorAll(".qcm-question").forEach(qi=>{
    const i = +qi.dataset.i;
    qi.querySelectorAll(".qcm-option").forEach(opt=>{
      opt.addEventListener("click", ()=>{
        if(carte.classList.contains("resolue")) return;
        qi.querySelectorAll(".qcm-option").forEach(x=>x.classList.remove("select"));
        opt.classList.add("select");
        choix[i] = +opt.dataset.j;
      });
    });
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const qs = d.questions||[];
    if(Object.keys(choix).length < qs.length){ api.incomplet("Il reste une question sans réponse."); return; }
    const justes = qs.filter((q,i)=>choix[i] === q.bonne).length;
    if(justes === qs.length) api.reussir();
    else api.erreur(justes, qs.length, ["bonne réponse", "bonnes réponses"]);
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
      </div>`).join("")}
    ${BOUTON_VERIFIER("Vérifier mes réponses")}
  </div>`;
}
function activerVraiFaux(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  const rep = {};
  carte.querySelectorAll(".vf-ligne").forEach(l=>{
    const i = +l.dataset.i;
    l.querySelectorAll(".vf-btn").forEach(b=>{
      b.addEventListener("click", ()=>{
        if(carte.classList.contains("resolue")) return;
        l.querySelectorAll(".vf-btn").forEach(x=>x.classList.remove("select"));
        b.classList.add("select");
        rep[i] = b.dataset.rep === "vrai";
      });
    });
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const aff = d.affirmations||[];
    if(Object.keys(rep).length < aff.length){ api.incomplet("Réponds à toutes les affirmations."); return; }
    const justes = aff.filter((a,i)=>rep[i] === !!a.vrai).length;
    if(justes === aff.length) api.reussir();
    else api.erreur(justes, aff.length, ["réponse juste", "réponses justes"]);
  });
}

/* ============================================================
   TYPE 3 — ASSOCIATION (relier deux colonnes)
   On choisit un élément à gauche, puis son partenaire à droite :
   ils reçoivent le même numéro. Rien n'est corrigé avant « Vérifier ».
   ============================================================ */
function corpsAssociation(d){
  const paires = d.paires||[];
  const gauche = paires.map((p,i)=>({...p, id:"g"+i, bon:"d"+i}));
  const droite = melanger(paires.map((p,i)=>({...p, id:"d"+i})));
  return `<p class="aide-type">Clique un élément à gauche, puis celui qui lui correspond à droite. Clique une paire pour la défaire.</p>
  <div class="rang-match">
    <div class="colonne-match" data-col="g">
      ${gauche.map((p,i)=>`<div class="carte-match" data-id="${p.id}" data-bon="${p.bon}" data-num="${i+1}"><span class="num-paire">${i+1}</span>${p.icone?`<span class="emoji">${p.icone}</span>`:""}${p.g}</div>`).join("")}
    </div>
    <div class="colonne-match" data-col="d">
      ${droite.map(p=>`<div class="carte-match" data-id="${p.id}"><span class="num-paire"></span>${p.d}</div>`).join("")}
    </div>
  </div>
  ${BOUTON_VERIFIER("Vérifier les associations")}`;
}
function activerAssociation(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  const liens = {};           // id gauche → id droite
  let sel = null;
  const G = id => carte.querySelector(`[data-col="g"] [data-id="${id}"]`);
  const D = id => carte.querySelector(`[data-col="d"] [data-id="${id}"]`);
  const dessiner = ()=>{
    carte.querySelectorAll('[data-col="d"] .carte-match').forEach(c=>{
      c.classList.remove("apparie"); c.querySelector(".num-paire").textContent = "";
    });
    carte.querySelectorAll('[data-col="g"] .carte-match').forEach(c=>c.classList.toggle("apparie", !!liens[c.dataset.id]));
    Object.entries(liens).forEach(([g, dd])=>{
      const c = D(dd); c.classList.add("apparie"); c.querySelector(".num-paire").textContent = G(g).dataset.num;
    });
  };
  carte.querySelectorAll('[data-col="g"] .carte-match').forEach(c=>{
    c.addEventListener("click", ()=>{
      if(carte.classList.contains("resolue")) return;
      if(liens[c.dataset.id] && sel !== c){ delete liens[c.dataset.id]; dessiner(); }
      carte.querySelectorAll('[data-col="g"] .carte-match').forEach(x=>x.classList.remove("select"));
      c.classList.add("select"); sel = c;
    });
  });
  carte.querySelectorAll('[data-col="d"] .carte-match').forEach(c=>{
    c.addEventListener("click", ()=>{
      if(carte.classList.contains("resolue")) return;
      const deja = Object.keys(liens).find(g=>liens[g] === c.dataset.id);
      if(!sel){
        if(deja){ delete liens[deja]; dessiner(); return; }
        api.incomplet("Choisis d'abord un élément dans la colonne de gauche."); return;
      }
      if(deja) delete liens[deja];
      liens[sel.dataset.id] = c.dataset.id;
      sel.classList.remove("select"); sel = null;
      dessiner();
    });
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const gauches = [...carte.querySelectorAll('[data-col="g"] .carte-match')];
    const manquent = gauches.filter(g=>!liens[g.dataset.id]).length;
    if(manquent){ api.incomplet(`Il reste ${pluriel(manquent, "élément")} à relier.`); return; }
    const justes = gauches.filter(g=>liens[g.dataset.id] === g.dataset.bon).length;
    if(justes === gauches.length) api.reussir();
    else api.erreur(justes, gauches.length, ["association juste", "associations justes"]);
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
  ${BOUTON_VERIFIER("Vérifier l'ordre")}`;
}
function activerOrdre(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  const liste = carte.querySelector(".liste-ordre");
  const renumeroter = ()=> liste.querySelectorAll(".item-ordre").forEach((it,i)=>{
    it.querySelector(".rang").textContent = i+1;
  });
  renumeroter();
  liste.addEventListener("click", ev=>{
    if(carte.classList.contains("resolue")) return;
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
    const justes = items.filter((it,i)=>+it.dataset.rang === i+1).length;
    if(justes === items.length) api.reussir();
    else api.erreur(justes, items.length, ["élément bien placé", "éléments bien placés"]);
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
    ${BOUTON_VERIFIER("Vérifier le classement")}`;
}
function activerTri(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  const reserve = carte.querySelector(".tri-reserve");
  let sel = null;
  const choisir = el=>{
    carte.querySelectorAll(".carte-tri").forEach(x=>x.classList.remove("select"));
    el.classList.add("select"); sel = el;
  };
  carte.addEventListener("click", ev=>{
    if(carte.classList.contains("resolue")) return;
    const col = ev.target.closest(".tri-colonne");
    const c = ev.target.closest(".carte-tri");
    /* Une carte est choisie : un clic n'importe où dans la colonne l'y dépose,
       y compris sur son titre ou sur une carte déjà posée. */
    if(sel && col){
      const zone = col.querySelector(".tri-zone");
      if(zone && c !== sel){ zone.appendChild(sel); sel.classList.remove("select"); sel = null; return; }
    }
    if(c){ choisir(c); return; }
    if(ev.target.closest(".tri-reserve") && sel){ reserve.appendChild(sel); sel.classList.remove("select"); sel = null; }
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    const restantes = reserve.querySelectorAll(".carte-tri").length;
    if(restantes){ api.incomplet(`Il reste ${pluriel(restantes, "étiquette")} à classer.`); return; }
    let justes = 0, total = 0;
    carte.querySelectorAll(".tri-colonne").forEach(col=>{
      col.querySelectorAll(".carte-tri").forEach(c=>{ total++; if(c.dataset.col === col.dataset.col) justes++; });
    });
    if(justes === total) api.reussir();
    else api.erreur(justes, total, ["carte bien classée", "cartes bien classées"]);
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
    ${BOUTON_VERIFIER("Vérifier le texte")}`;
}
/* Étiquettes à poser dans des emplacements (trous et plan) */
function brancherEtiquettes(carte, selecteurCible, slotDe, api){
  let sel = null;
  carte.querySelectorAll(".etiquette").forEach(et=>{
    et.addEventListener("click", ()=>{
      if(et.classList.contains("posee") || carte.classList.contains("resolue")) return;
      carte.querySelectorAll(".etiquette").forEach(x=>x.classList.remove("select"));
      et.classList.add("select"); sel = et;
    });
  });
  carte.querySelectorAll(selecteurCible).forEach(cible=>{
    cible.addEventListener("click", ()=>{
      if(carte.classList.contains("resolue")) return;
      const slot = slotDe(cible);
      if(cible.dataset.pose){
        const anc = carte.querySelector(`.etiquette.posee[data-mot="${CSS.escape(cible.dataset.pose)}"]`);
        if(anc) anc.classList.remove("posee");
        slot.textContent = ""; delete cible.dataset.pose; cible.classList.remove("rempli");
        if(!sel) return;
      }
      if(!sel){ api.incomplet("Choisis d'abord une étiquette."); return; }
      slot.textContent = sel.dataset.mot;
      cible.dataset.pose = sel.dataset.mot;
      cible.classList.add("rempli");
      sel.classList.add("posee"); sel.classList.remove("select"); sel = null;
    });
  });
}
function verifierEmplacements(liste, api, unites, messageIncomplet){
  if(liste.some(t=>!t.dataset.pose)){ api.incomplet(messageIncomplet); return; }
  const justes = liste.filter(t=>normaliser(t.dataset.pose) === normaliser(t.dataset.rep)).length;
  if(justes === liste.length) api.reussir();
  else api.erreur(justes, liste.length, unites);
}
function activerTrous(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  brancherEtiquettes(carte, ".trou", t=>t, api);
  carte.querySelector("[data-valider]").addEventListener("click", ()=>
    verifierEmplacements([...carte.querySelectorAll(".trou")], api, ["mot bien placé", "mots bien placés"], "Tous les trous ne sont pas remplis."));
}

/* ============================================================
   TYPE 7 — LETTRES CACHÉES (anagramme)
   Des lettres sont marquées dans le texte (data-l), dans le
   désordre, et certaines sont des leurres. L'élève clique celles
   qu'il retient : elles se placent dans les cases, de gauche à
   droite ; un clic sur une case rend la lettre au texte. Il
   valide quand le mot est complet.
   ============================================================ */
function corpsLettres(d){
  const cible = d.cible || [];
  return `<div class="slots slots-lettres">${cible.map((_, i)=>`<button type="button" class="slot vide" data-i="${i}" aria-label="Case ${i+1}"></button>`).join("")}</div>
    <p class="aide-type">Clique les lettres en couleur dans le texte pour les placer dans les cases, dans l'ordre qui forme le mot. Attention : certaines lettres sont des pièges. Clique une case pour la vider.</p>
    <div class="texte-doc">${d.texte||""}</div>
    ${BOUTON_VERIFIER("Vérifier le mot")}`;
}
function activerLettres(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  const cible = (d.cible || []).map(x=>String(x));
  const slots = [...carte.querySelectorAll(".slot")];
  const contenu = Array(cible.length).fill(null);    // lettre cliquée (élément du texte) par case
  const dessiner = ()=> slots.forEach((s,i)=>{
    const el = contenu[i];
    s.textContent = el ? el.dataset.l : "";
    s.classList.toggle("vide", !el); s.classList.toggle("ok", !!el);
  });
  carte.querySelectorAll("[data-l]").forEach(l=>{
    l.classList.add("lettre-clic");
    l.setAttribute("role", "button"); l.setAttribute("tabindex", "0");
    const prendre = ()=>{
      if(carte.classList.contains("resolue") || l.classList.contains("utilisee")) return;
      const libre = contenu.indexOf(null);
      if(libre < 0){ api.incomplet("Toutes les cases sont remplies : vide une case ou vérifie."); return; }
      contenu[libre] = l; l.classList.add("utilisee"); dessiner();
    };
    l.addEventListener("click", prendre);
    l.addEventListener("keydown", ev=>{ if(ev.key === "Enter" || ev.key === " "){ ev.preventDefault(); prendre(); } });
  });
  slots.forEach((s,i)=>s.addEventListener("click", ()=>{
    if(carte.classList.contains("resolue") || !contenu[i]) return;
    contenu[i].classList.remove("utilisee"); contenu[i] = null; dessiner();
  }));
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    if(contenu.includes(null)){ api.incomplet("Le mot n'est pas complet."); return; }
    const justes = contenu.filter((el,i)=>normaliser(el.dataset.l) === normaliser(cible[i])).length;
    if(justes === cible.length) api.reussir();
    else api.erreur(justes, cible.length, ["lettre bien placée", "lettres bien placées"]);
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
function activerCode(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  const champs = d.champs||[];
  const valider = ()=>{
    if(carte.classList.contains("resolue")) return;
    const inputs = champs.map((c,i)=>carte.querySelector(`#code-${i}`));
    if(inputs.some(inp=>!inp.value.trim())){ api.incomplet("Remplis toutes les cases du cadenas."); return; }
    const justes = champs.filter((c,i)=>normaliser(inputs[i].value) === normaliser(c.valeur)).length;
    if(justes === champs.length){
      inputs.forEach(i=>i.disabled = true);
      api.reussir();
    }else api.erreur(justes, champs.length, ["case juste", "cases justes"]);
  };
  carte.querySelector("[data-valider]").addEventListener("click", valider);
  carte.querySelectorAll(".cadenas input").forEach(inp=>{
    inp.addEventListener("keydown", ev=>{ if(ev.key === "Enter") valider(); });
  });
}

/* ============================================================
   TYPE 9 — INTRUS (choisir, puis vérifier)
   ============================================================ */
function corpsIntrus(d){
  const cartes = melanger((d.cartes||[]).map((c,i)=>({...c, id:"i"+i})));
  return `<div class="grille-intrus">
    ${cartes.map(c=>`<div class="carte-intrus" data-intrus="${c.intrus?1:0}">
      ${c.icone?`<span class="emoji">${c.icone}</span>`:""}
      <div class="txt">${c.txt}</div>
      ${c.sous?`<div class="sous">${c.sous}</div>`:""}
    </div>`).join("")}
  </div>
  ${BOUTON_VERIFIER("C'est l'intrus !")}`;
}
function activerIntrus(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  let choix = null;
  carte.querySelectorAll(".carte-intrus").forEach(c=>{
    c.addEventListener("click", ()=>{
      if(carte.classList.contains("resolue")) return;
      carte.querySelectorAll(".carte-intrus").forEach(x=>x.classList.remove("select"));
      c.classList.add("select"); choix = c;
    });
  });
  carte.querySelector("[data-valider]").addEventListener("click", ()=>{
    if(!choix){ api.incomplet("Choisis d'abord une carte."); return; }
    if(choix.dataset.intrus === "1") api.reussir();
    else api.erreur(0, 1, null, "Ce n'est pas l'intrus.");
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
    ${BOUTON_VERIFIER("Vérifier le schéma")}`;
}
function activerPlan(e, d, api){
  const carte = document.getElementById("enigme-"+e.id);
  brancherEtiquettes(carte, ".plan-case", cs=>cs.querySelector(".plan-slot"), api);
  carte.querySelector("[data-valider]").addEventListener("click", ()=>
    verifierEmplacements([...carte.querySelectorAll(".plan-case")], api, ["case juste", "cases justes"], "Toutes les cases ne sont pas remplies."));
}

/* ============================================================
   TYPE 11 — INSTRUMENT (utilisé par « La Station météo disparue »)
   Un instrument gradué dessiné en SVG : thermomètre ou pluviomètre.
   Deux modes par item :
     "lire"   le niveau est affiché ; l'élève écrit la valeur lue
     "regler" l'élève monte ou descend le niveau (▲ ▼ ou clic sur
              l'échelle) jusqu'à la valeur demandée ; aucune valeur
              n'est affichée : il doit lire lui-même la graduation.
   JSON : { instrument, unite, min, max, pas, etiquettes,
            items:[{libelle, mode, valeur, depart}] }
   ============================================================ */
const INSTR_H = 260, INSTR_HAUT = 28, INSTR_BAS = 214;   // zone graduée (y)
function instrY(d, v){
  return INSTR_BAS - (v - d.min) * (INSTR_BAS - INSTR_HAUT) / (d.max - d.min);
}
/** Lecture numérique tolérante : « −4 », « -4 °C », « 2,5 mm ». */
function lireNombre(s){
  const m = String(s==null?"":s).replace(/[−–]/g,"-").replace(",",".").replace(/\s/g,"").match(/-?\d+(\.\d+)?/);
  return m ? parseFloat(m[0]) : NaN;
}
function fmtNombre(v){ return (v<0?"−":"") + String(Math.abs(v)).replace(".",","); }

function svgInstrument(d, niveau){
  const thermo = d.instrument !== "pluviometre";
  const pas = d.pas || 1, etiq = d.etiquettes || pas*5;
  let graduations = "";
  const n = Math.round((d.max - d.min)/pas);
  const xTube = thermo ? 52 : 40, lTube = thermo ? 14 : 40;
  for(let k=0;k<=n;k++){
    const v = +(d.min + k*pas).toFixed(4);
    const y = instrY(d, v);
    const grand = Math.abs((v - d.min) % etiq) < 1e-9 || Math.abs(v % etiq) < 1e-9;
    const x1 = xTube + lTube + 2;
    graduations += `<line x1="${x1}" y1="${y}" x2="${x1 + (grand?14:7)}" y2="${y}" stroke="#1f2430" stroke-width="${grand?1.6:0.9}"/>`;
    if(grand) graduations += `<text x="${x1+17}" y="${y+4}" font-size="11" fill="#1f2430" font-family="Arial,sans-serif">${fmtNombre(v)}</text>`;
    graduations += `<rect class="instr-cran" data-v="${v}" x="${xTube-6}" y="${y-(INSTR_BAS-INSTR_HAUT)/n/2}" width="${lTube+40}" height="${(INSTR_BAS-INSTR_HAUT)/n}" fill="transparent"/>`;
  }
  const yN = instrY(d, niveau);
  const zero = (thermo && d.min < 0 && d.max > 0)
    ? `<line x1="${xTube-4}" y1="${instrY(d,0)}" x2="${xTube+lTube+18}" y2="${instrY(d,0)}" stroke="#1d3a8a" stroke-width="1.4" stroke-dasharray="3 2"/>` : "";
  if(thermo){
    return `<svg class="instr-svg" viewBox="0 0 120 ${INSTR_H}" role="img" aria-label="Thermomètre gradué en ${d.unite||"°C"}">
      <rect x="${xTube-4}" y="${INSTR_HAUT-14}" width="${lTube+8}" height="${INSTR_BAS-INSTR_HAUT+30}" rx="11" fill="#f4f6f8" stroke="#8a93a0" stroke-width="1.5"/>
      <circle cx="${xTube+lTube/2}" cy="${INSTR_BAS+24}" r="15" fill="#c62828" stroke="#8a93a0" stroke-width="1.5"/>
      <rect class="instr-liquide" x="${xTube+3}" y="${yN}" width="${lTube-6}" height="${INSTR_BAS+14-yN}" fill="#c62828"/>
      ${zero}${graduations}
      <text x="4" y="${INSTR_HAUT-2}" font-size="11" fill="#1f2430" font-family="Arial,sans-serif">${d.unite||"°C"}</text>
    </svg>`;
  }
  return `<svg class="instr-svg" viewBox="0 0 120 ${INSTR_H}" role="img" aria-label="Pluviomètre gradué en ${d.unite||"mm"}">
    <path d="M${xTube-12} ${INSTR_HAUT-20} L${xTube+lTube+12} ${INSTR_HAUT-20} L${xTube+lTube} ${INSTR_HAUT-4} L${xTube} ${INSTR_HAUT-4} Z" fill="#dfe6ee" stroke="#8a93a0" stroke-width="1.5"/>
    <rect x="${xTube}" y="${INSTR_HAUT-4}" width="${lTube}" height="${INSTR_BAS-INSTR_HAUT+8}" fill="#f4f8fb" stroke="#8a93a0" stroke-width="1.5"/>
    <rect class="instr-liquide" x="${xTube+1}" y="${yN}" width="${lTube-2}" height="${Math.max(0,INSTR_BAS-yN)}" fill="#5aa0d8" opacity=".85"/>
    <line class="instr-menisque" x1="${xTube+1}" y1="${yN}" x2="${xTube+lTube-1}" y2="${yN}" stroke="#1d5c8f" stroke-width="2"/>
    ${graduations}
    <rect x="${xTube-6}" y="${INSTR_BAS+4}" width="${lTube+12}" height="10" rx="2" fill="#8a93a0"/>
    <text x="2" y="${INSTR_BAS+34}" font-size="11" fill="#1f2430" font-family="Arial,sans-serif">${d.unite||"mm"}</text>
  </svg>`;
}

function corpsInstrument(d){
  return `<div class="instr-rangee">${(d.items||[]).map((it,i)=>{
    const depart = it.mode === "regler" ? (it.depart!=null ? it.depart : d.min) : it.valeur;
    return `<div class="instr-item" data-i="${i}" data-mode="${it.mode}" data-niveau="${depart}">
      <div class="instr-libelle">${it.libelle||""}</div>
      ${svgInstrument(d, depart)}
      ${it.mode === "regler"
        ? `<div class="instr-reglage">
             <button class="btn petit instr-moins" aria-label="Descendre le niveau">▼</button>
             <button class="btn petit instr-plus" aria-label="Monter le niveau">▲</button>
           </div>`
        : `<label class="instr-saisie">Je lis :
             <input type="text" inputmode="decimal" maxlength="7" autocomplete="off" class="instr-champ" aria-label="Valeur lue sur ${echapper(it.libelle||"l'instrument")}">
             <span>${d.unite||""}</span></label>`}
    </div>`;}).join("")}</div>
    <div class="center"><button class="btn vert" data-valider="1">✅ Vérifier les lectures</button></div>`;
}

function activerInstrument(e, d, api){
  const reussir = api.reussir;
  const carte = document.getElementById("enigme-"+e.id);
  const pas = d.pas || 1;
  const poser = (item, v)=>{
    v = Math.max(d.min, Math.min(d.max, +(+v).toFixed(4)));
    item.dataset.niveau = v;
    const y = instrY(d, v);
    const liq = item.querySelector(".instr-liquide");
    const thermo = d.instrument !== "pluviometre";
    liq.setAttribute("y", y);
    liq.setAttribute("height", thermo ? (INSTR_BAS+14-y) : Math.max(0, INSTR_BAS-y));
    const men = item.querySelector(".instr-menisque");
    if(men){ men.setAttribute("y1", y); men.setAttribute("y2", y); }
    item.classList.remove("bien","mal");
  };
  carte.querySelectorAll('.instr-item[data-mode="regler"]').forEach(item=>{
    item.querySelector(".instr-plus").addEventListener("click", ()=>{ if(!item.classList.contains("verrouille")) poser(item, +item.dataset.niveau + pas); });
    item.querySelector(".instr-moins").addEventListener("click", ()=>{ if(!item.classList.contains("verrouille")) poser(item, +item.dataset.niveau - pas); });
    item.querySelectorAll(".instr-cran").forEach(c=>c.addEventListener("click", ()=>{
      if(!item.classList.contains("verrouille")) poser(item, +c.dataset.v);
    }));
  });
  const valider = ()=>{
    const items = [...carte.querySelectorAll(".instr-item")];
    const vides = items.filter(it=>it.dataset.mode==="lire" && !it.querySelector(".instr-champ").value.trim()).length;
    if(vides){ api.incomplet(`Il reste ${vides} lecture${vides>1?"s":""} à écrire.`); return; }
    let justes = 0;
    items.forEach(it=>{
      const attendu = (d.items[+it.dataset.i]||{}).valeur;
      const v = it.dataset.mode === "lire" ? lireNombre(it.querySelector(".instr-champ").value) : +it.dataset.niveau;
      const ok = Math.abs(v - attendu) < 1e-6;
      if(ok) justes++;
    });
    if(justes === items.length){
      items.forEach(it=>{ it.classList.add("verrouille"); const c = it.querySelector(".instr-champ"); if(c) c.disabled = true; });
      reussir();
    }else{
      setTimeout(()=>items.forEach(it=>it.classList.remove("mal")),900);
      api.erreur(justes, items.length, null, `${justes} lecture${justes>1?"s":""} juste${justes>1?"s":""} sur ${items.length}. Regarde bien où arrive le liquide.`);
    }
  };
  carte.querySelector("[data-valider]").addEventListener("click", valider);
  carte.querySelectorAll(".instr-champ").forEach(c=>c.addEventListener("keydown", ev=>{ if(ev.key==="Enter") valider(); }));
}

/* ============================================================
   BRANCHEMENT DES INTERACTIONS
   ============================================================ */
const ACTIVATEURS = {
  qcm: activerQcm, vraifaux: activerVraiFaux, association: activerAssociation,
  ordre: activerOrdre, tri: activerTri, trous: activerTrous, lettres: activerLettres,
  code: activerCode, intrus: activerIntrus, plan: activerPlan,
  instrument: activerInstrument
};

/**
 * Branche une énigme affichée.
 * @param {object} e        l'énigme (objet JSON)
 * @param {function} onReussite  appelée une fois l'énigme résolue : (e, indices, erreurs)
 */
function activerEnigme(e, onReussite){
  const d = donneesNiveau(e);
  const carte = document.getElementById("enigme-"+e.id);
  if(!carte) return;
  const fb = carte.querySelector("#fb-"+e.id);
  let resolu = false, erreurs = 0, indicesUtilises = 0;
  const ptsPremier = typeof PTS_PREMIER_COUP !== "undefined" ? PTS_PREMIER_COUP : 10;
  const ptsApres = typeof PTS_APRES_ERREUR !== "undefined" ? PTS_APRES_ERREUR : 3;

  const montrer = (classe, html, duree)=>{
    fb.className = "feedback " + classe + " show";
    fb.innerHTML = html;
    clearTimeout(fb._t);
    if(duree) fb._t = setTimeout(()=>fb.classList.remove("show"), duree);
  };
  const api = {
    incomplet(msg){
      if(resolu) return;
      montrer("indice", "✋ " + msg, 2600);
    },
    erreur(justes, total, unites, message){
      if(resolu) return;
      erreurs++;
      if(typeof son === "function") son("erreur");
      if(typeof compterErreur === "function") compterErreur();
      const detail = message || (unites ? `${justes} ${justes > 1 ? unites[1] : unites[0]} sur ${total}.` : "");
      const perte = erreurs === 1
        ? `<div class="perte-bonus">Le bonus du premier coup est perdu : cette énigme ne rapportera plus que ${ptsApres} points. Vérifie dans la leçon avant de revalider.</div>`
        : "";
      carte.classList.remove("secoue"); void carte.offsetWidth; carte.classList.add("secoue");
      montrer("erreur", `✗ <b>Pas tout juste.</b> ${detail}${perte}`, 0);
    },
    reussir(){
      if(resolu) return;
      resolu = true;
      if(typeof son === "function") son("succes");
      carte.classList.add("resolue");
      carte.querySelectorAll("[data-valider]").forEach(b=>b.disabled = true);
      const bi = carte.querySelector("#indice-"+e.id);
      if(bi) bi.disabled = true;
      montrer(erreurs ? "succes" : "succes premier-coup",
        erreurs ? `✔ Résolue : <b>+${ptsApres} points</b>.`
                : `🎯 <b>Tout juste du premier coup !</b> <b>+${ptsPremier} points</b>`, 0);
      setTimeout(()=>onReussite(e, indicesUtilises, erreurs), 500);
    }
  };

  const bf = carte.querySelector("[data-fiche]");
  if(bf) bf.addEventListener("click", ()=>ouvrirFicheSource(bf.dataset.fiche));

  (ACTIVATEURS[e.type] || (()=>{}))(e, d, api);

  /* ---- Indices progressifs (−MALUS_INDICE points chacun) ---- */
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
