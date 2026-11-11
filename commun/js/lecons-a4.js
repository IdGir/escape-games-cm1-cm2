/* ============================================================
   LEÇONS IMPRIMABLES A4 — script commun aux escape games
   ------------------------------------------------------------
   Page : lecons-imprimables.html?niveau=CM2&lecon=toutes
     niveau  : CM1 | CM2           (défaut : CM2)
     lecon   : toutes | <id>        (défaut : toutes)
     salle   : 1..5  (sélectionne la leçon de cette salle)
     imprimer: 1 → ouvre la fenêtre d'impression une fois prêt

   Données :
     assets/data/lecons.json     les leçons du jeu (texte CM1/CM2,
                                 objectifs, schéma, frise, lexique,
                                 document, sources) — déjà utilisées
                                 dans le jeu ;
     assets/data/lecons-a4.json  compléments pour l'impression :
                                 en-tête du jeu, compétence du
                                 programme, cartes, graphiques et
                                 photos (facultatif).

   Une leçon = une page A4. La taille du texte et des visuels est
   ajustée automatiquement pour remplir la page sans déborder.
   ============================================================ */
(function(){
  "use strict";

  const params = new URLSearchParams(location.search);
  const etat = {
    niveau: (params.get("niveau") || "CM2").toUpperCase() === "CM1" ? "CM1" : "CM2",
    lecon: params.get("lecon") || "toutes",
    salle: params.get("salle"),
    imprimer: params.get("imprimer") === "1",
    lecons: [],
    a4: { jeu:{}, lecons:{} }
  };

  const $ = (s, r=document) => r.querySelector(s);

  async function lireJSON(url, obligatoire){
    try{
      const r = await fetch(url, {cache:"no-store"});
      if(!r.ok) throw new Error(r.status);
      return await r.json();
    }catch(e){
      if(obligatoire) throw e;
      return null;
    }
  }

  function texte(v){ return v == null ? "" : String(v); }

  /* ---------- Normalisation d'une leçon ---------- */
  function contenuNiveau(l){
    const c = l.contenu;
    if(!c) return "";
    if(typeof c === "string") return c;
    const n = etat.niveau.toLowerCase();
    return c[n] || c.cm2 || c.cm1 || "";
  }

  function visibles(){
    return etat.lecons.filter(l => !(l.niveau === "CM2" && etat.niveau === "CM1"));
  }

  function selection(){
    const v = visibles();
    if(etat.salle){
      const s = v.filter(l => String(l.salle) === String(etat.salle));
      if(s.length) return s;
    }
    if(etat.lecon && etat.lecon !== "toutes"){
      const s = v.filter(l => l.id === etat.lecon);
      if(s.length) return s;
    }
    return v;
  }

  /* ---------- mission-geo : leçons déclarées en JavaScript (MISSION.lecon) ---------- */
  function depuisMission(){
    const M = window.MISSION;
    const parLecon = {};
    (M.sessions || []).forEach(s => { if(s.lecon) parLecon[s.lecon] = s; });
    return Object.values(M.lecons).map(l => {
      const s = parLecon[l.id] || {};
      const retenir = l.aRetenir ? `<div class="encadre"><b>À retenir :</b> ${l.aRetenir}</div>` : "";
      return {
        id: l.id, titre: l.titre, objectifs: l.objectifs || [],
        salle: s.numero, icone: s.numero ? String(s.numero) : "",
        contenu: { cm1: (l.texte || "") + retenir, cm2: (l.texte || "") + retenir },
        lexique: (l.vocabulaire || []).map(v => Array.isArray(v) ? { mot: v[0], def: v[1] } : v),
        sources: l.source || l.sources || ""
      };
    });
  }

  /* ---------- Blocs ---------- */
  function blocVisuel(v){
    if(!v) return "";
    // Code couleur : le cadre dépend du rôle du visuel (carte, graphique, tableau → ardoise ;
    // schéma / expérience → orange ; document → violet ; photo → gris)
    const estPhoto = v.type === "photo" || v.type === "image";
    const etiquette = v.etiquette || (estPhoto ? "Photo" : "Schéma");
    const norm = etiquette.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
    const role = { carte:"carte", graphique:"graphique", tableau:"tableau", schema:"schema", protocole:"schema",
                   experience:"schema", document:"document", photo:"photo" }[norm] || (estPhoto ? "photo" : "schema");
    const titre = v.titre ? `<div class="vtitre">${v.titre}</div>` : "";
    const legende = v.legende ? `<div class="legende">${v.legende}</div>` : "";
    const credit = (v.credit || v.source) ? `<div class="credit">${v.credit || v.source}</div>` : "";
    const fac = (v.facultatif === true || (v.facultatif !== false && estPhoto && v.etiquette !== "Document")) ? ' data-facultatif="1"' : "";
    const tete = `<span class="etiq">${etiquette}</span>${titre}`;
    const vb = /viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)/.exec(v.svg || "");
    const ratio = vb && +vb[2] > 0 ? Math.max(0.6, Math.min(4, +vb[1] / +vb[2])) : 1.4;
    const st = ` style="--ratio:${ratio.toFixed(2)}"`;
    if(estPhoto){
      return `<figure class="visuel cadre v-${role} photo"${fac}${st}>${tete}<img src="${encodeURI(v.src)}" alt="${texte(v.alt || v.titre).replace(/"/g,"&quot;")}" loading="eager">${legende}${credit}</figure>`;
    }
    return `<figure class="visuel cadre v-${role}"${fac}${st}>${tete}${v.svg || ""}${legende}${credit}</figure>`;
  }

  function listeVisuels(l, extra){
    const liste = [];
    let sc = l.schema;
    if(typeof sc === "string") sc = { svg: sc };
    if(sc && !sc.svg && (sc.cm1 || sc.cm2)) sc = sc[etat.niveau.toLowerCase()] || sc.cm2 || sc.cm1;
    if(typeof sc === "string") sc = { svg: sc };
    const schema = (sc && sc.svg)
      ? { type:"svg", etiquette:"Schéma", titre:sc.titre || l.schema_titre || "Schéma", svg:sc.svg, legende:sc.legende, source:sc.source }
      : null;
    const masquer = extra.masquer || [];
    const doc = l.document;
    const docImage = (doc && doc.type === "image" && doc.fichier && !masquer.includes("document"))
      ? { type:"photo", etiquette:"Document", titre:doc.titre, src:"assets/images/documents/" + doc.fichier + ".jpg", credit:doc.source }
      : null;

    const ajouts = extra.visuels || [];
    let schemaPlace = false;
    ajouts.forEach(v => {
      if(v.type === "schema"){ if(schema && !masquer.includes("schema")){ liste.push(Object.assign({}, schema, v, {type:"svg", svg:schema.svg})); } schemaPlace = true; }
      else liste.push(v);
    });
    if(schema && !schemaPlace && !masquer.includes("schema")) liste.unshift(schema);
    if(docImage) liste.push(docImage);
    return liste;
  }

  function blocFrise(l){
    const f = l.frise;
    if(!f || !f.length) return "";
    return `<div class="frise cadre"><span class="etiq">Frise chronologique</span>${l.frise_titre ? `<div class="ftitre">${l.frise_titre}</div>` : ""}
      <div class="ligne">${f.map(e => `<div class="evt"><b>${e.date}</b>${e.evt}</div>`).join("")}</div></div>`;
  }

  function blocDocument(l, extra){
    const d = l.document;
    if(!d || (extra.masquer || []).includes("document")) return "";
    if(d.type === "text" || d.type === "texte"){
      return `<div class="document cadre"><span class="etiq">Document</span><div class="dtitre">${d.titre || ""}</div>
        ${/^\s*[«"“]/.test(d.contenu || "") ? `<span class="citation">${d.contenu}</span>` : `<q>${d.contenu || ""}</q>`}${d.source ? `<div class="dsource">${d.source}</div>` : ""}</div>`;
    }
    return "";
  }

  function blocLexique(l){
    const lx = l.lexique;
    if(!lx || !lx.length) return "";
    return `<div class="lexique cadre"><span class="etiq">Lexique</span>
      <dl>${lx.map(m => `<div><dt>${m.mot}</dt><dd>${m.def}</dd></div>`).join("")}</dl></div>`;
  }

  function blocObjectifs(l){
    if(!l.objectifs || !l.objectifs.length) return "";
    return `<div class="objectifs"><b>J'apprends à</b><ul>${l.objectifs.map(o => `<li>${o}</li>`).join("")}</ul></div>`;
  }

  function versTexte(v){
    if(v == null) return "";
    if(Array.isArray(v)) return v.map(versTexte).filter(Boolean).join(" ; ");
    if(typeof v === "object") return texte(v.titre || v.nom || v.texte || "");
    return texte(v);
  }

  function sources(l, extra){
    const s = [];
    if(l.sources) s.push(versTexte(l.sources));
    else if(l.source) s.push(versTexte(l.source));
    if(extra.sources) s.push(versTexte(extra.sources));
    return s.join(" ; ");
  }

  /* ---------- Une page ---------- */
  function page(l, i, n){
    const jeu = etat.a4.jeu || {};
    const extra = (etat.a4.lecons || {})[l.id] || {};
    const visuels = listeVisuels(l, extra);
    const colonne = visuels.filter(v => v.largeur !== "pleine");
    const larges = visuels.filter(v => v.largeur === "pleine");
    const pastille = texte(l.icone).length <= 3 && l.icone ? l.icone : (l.salle || i + 1);
    const sous = [
      l.salle ? `${(etat.a4.jeu||{}).unite || "Salle"} ${l.salle}` : `Leçon ${i + 1}`,
      jeu.titre ? `escape game « ${jeu.titre} »` : ""
    ].filter(Boolean).join(" · ");
    // version courte, rédigée pour l'impression (outils-lecons/textes/<jeu>.json) : texte plus gros
    const tc = extra.texte;
    const texteCourt = tc ? (typeof tc === "string" ? tc : (tc[etat.niveau.toLowerCase()] || tc.cm2 || tc.cm1 || "")) : "";
    const competence = extra.competence
      ? `<div class="competence"><b>Compétence du programme :</b> ${extra.competence}</div>` : "";

    return `
    <section class="feuille" data-id="${l.id}" data-matiere="${texte(jeu.matiere).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z]+/g, "-")}">
      <header class="entete">
        <div class="matiere"><b>${jeu.matiere || "Leçon"}</b><span>Cycle 3 · CM1-CM2</span></div>
        <div class="jeu"><div class="nom-jeu">${jeu.titre || ""}</div><div class="theme">${jeu.theme || ""}</div></div>
        <div class="eleve"><span>Prénom :</span><span>Date :</span></div>
      </header>
      <div class="titre">
        <div class="pastille">${pastille}</div>
        <div><h2>${l.titre}</h2><div class="sous">${sous}</div></div>
        <div class="niveau">${etat.niveau}</div>
      </div>
      ${competence}
      <div class="corps ${colonne.length ? "" : "sans-visuel"}">
        <div class="texte cadre"><span class="etiq">La leçon à connaître</span>${texteCourt ? "" : blocObjectifs(l)}${texteCourt || contenuNiveau(l)}</div>
        ${colonne.length ? `<div class="visuels">${colonne.map(blocVisuel).join("")}</div>` : ""}
      </div>
      ${larges.length ? `<div class="pleine-largeur">${larges.map(blocVisuel).join("")}</div>` : ""}
      <div class="bas">${blocFrise(l)}${blocDocument(l, extra)}${blocLexique(l)}</div>
      <div class="espace-pied"></div>
      <footer class="pied">
        <div class="sources">${sources(l, extra) ? "Sources : " + sources(l, extra) : ""}</div>
        <div class="num">${jeu.titre ? jeu.titre + " · " : ""}${i + 1} / ${n}</div>
      </footer>
    </section>`;
  }

  /* ---------- Ajustement : chaque leçon remplit sa page sans déborder ----------
     1. pour une taille de texte donnée (--echelle), on cherche la plus grande
        taille de visuels (--echelle-visuel) qui ne dépasse pas la hauteur du
        texte : les deux colonnes s'équilibrent ;
     2. on cherche la plus grande taille de texte qui tient sur la page. */
  function deborde(f){ return f.scrollHeight > f.clientHeight + 1; }

  function equilibrer(f, e){
    f.style.setProperty("--echelle", e.toFixed(3));
    const txt = f.querySelector(".texte"), vis = f.querySelector(".visuels");
    if(!vis || !txt){ f.style.setProperty("--echelle-visuel", Math.min(1.25, e).toFixed(3)); return; }
    let bas = 0.4, haut = 1.6, ok = 0.4;
    for(let k = 0; k < 8; k++){
      const m = (bas + haut) / 2;
      f.style.setProperty("--echelle-visuel", m.toFixed(3));
      if(vis.offsetHeight <= Math.max(txt.offsetHeight, 60) * 1.04){ ok = m; bas = m; } else haut = m;
    }
    f.style.setProperty("--echelle-visuel", ok.toFixed(3));
  }

  // visuels en pleine largeur (grandes cartes) : leur taille est réglée à part (--echelle-pleine)
  function reglerPleine(f, min){
    if(!f.querySelector(".pleine-largeur")) return 1;
    let bas = min, haut = 1.25, ok = null;
    f.style.setProperty("--echelle-pleine", haut);
    if(!deborde(f)) return haut;
    for(let k = 0; k < 7; k++){
      const m = (bas + haut) / 2;
      f.style.setProperty("--echelle-pleine", m.toFixed(3));
      if(deborde(f)) haut = m; else { ok = m; bas = m; }
    }
    f.style.setProperty("--echelle-pleine", (ok == null ? min : ok).toFixed(3));
    return ok;
  }

  function tient(f, e, minPleine){
    equilibrer(f, e);
    const ep = reglerPleine(f, minPleine);
    return ep != null && !deborde(f);
  }

  const EMAX = 1.6;     // le texte ne dépasse pas ≈ 16,5 pt, même sur une page presque vide

  function chercher(f, minPleine){
    let bas = 0.62, haut = EMAX, ok = null;
    if(tient(f, haut, minPleine)) return haut;
    for(let k = 0; k < 8; k++){
      const m = (bas + haut) / 2;
      if(tient(f, m, minPleine)){ ok = m; bas = m; } else haut = m;
    }
    return ok;
  }

  /* Les visuels (cartes, graphiques, schémas) passent avant le texte :
     on part de la colonne la plus large et on la rétrécit seulement si le texte
     devrait descendre sous SEUIL (≈ 10 pt) pour que la page tienne.
     Les photos d'illustration (facultatives) ne comptent pas dans ce calcul :
     on les met de côté, puis on les remet seulement si la colonne des visuels
     a de la place, à la taille de cette place. */
  const COLONNES = [112, 106, 100, 94, 88, 82, 76, 70];  // largeur de la colonne des visuels, en mm
  const SEUIL = 0.95;                                     // échelle de texte souhaitée (≈ 10 pt)
  const ACCEPTE = 0.88;                                   // échelle de texte encore acceptée (≈ 9 pt)

  function choisirColonne(f){
    // la colonne la plus large où le texte garde une taille confortable, sinon acceptable,
    // sinon la colonne qui laisse le plus grand texte
    for(const seuil of [SEUIL, ACCEPTE]){
      for(const w of COLONNES){
        f.style.setProperty("--col-vis", w + "mm");
        if(tient(f, seuil, 0.6)) return w;
      }
    }
    let meilleur = COLONNES[COLONNES.length - 1], emax = -1;
    for(const w of COLONNES){
      f.style.setProperty("--col-vis", w + "mm");
      const e = chercher(f, 0.6);
      if(e != null && e > emax + 0.02){ emax = e; meilleur = w; }
    }
    return meilleur;
  }

  // remet une photo dans la colonne des visuels, à la plus grande hauteur qui tient sur la page
  function remettrePhoto(f, photo){
    const vis = f.querySelector(".visuels");
    const px_mm = f.clientWidth / 210;
    vis.appendChild(photo);
    let bas = 0, haut = 72, ok = 0;
    for(let k = 0; k < 7; k++){
      const m = (bas + haut) / 2;
      photo.style.setProperty("--h-photo", m.toFixed(1) + "mm");
      if(!deborde(f)){ ok = m; bas = m; } else haut = m;
    }
    if(ok < 26){ photo.remove(); return; }              // pas assez de place : on y renonce
    photo.style.setProperty("--h-photo", ok.toFixed(1) + "mm");
  }

  // état de départ d'une page : photos d'illustration mises de côté (f._photos), disposition en colonne
  function preparer(f){
    f.classList.remove("rempli");
    const corps = f.querySelector(".corps");
    corps.classList.remove("rangee");
    const vis = f.querySelector(".visuels");
    if(!vis) return null;
    if(!f._photos){
      f._photos = [...vis.querySelectorAll("[data-facultatif]")];
      f._photos.forEach(p => p.remove());
      f._photoSeule = false;
      if(!vis.querySelector(".visuel")){
        if(f.querySelector(".pleine-largeur")){            // la grande carte est en pleine largeur :
          vis.remove(); f._photos = [];                    // pas de colonne, le texte prend toute la largeur
          corps.classList.add("sans-visuel");
          return null;
        }
        vis.appendChild(f._photos.shift());                // photo seule : elle reste
        f._photoSeule = true;
      }
    }else{
      f._photos.forEach(p => { p.remove(); p.style.removeProperty("--h-photo"); });
    }
    f.style.removeProperty("--rb");
    return vis;
  }

  /* Disposition A : la leçon à gauche, les visuels dans une colonne à droite */
  function fitA(f, vis){
    if(vis) f.style.setProperty("--col-vis", choisirColonne(f) + "mm");
    // on cherche le plus grand texte possible ; une grande carte en pleine largeur n'est
    // réduite que si le texte descend sous SEUIL (90 % → 75 % → 60 % → 45 % de sa largeur)
    let ok = null, mp = 0.6;
    for(const m of (f.querySelector(".pleine-largeur") ? [0.9, 0.75, 0.6, 0.45] : [0.6, 0.45])){
      const e = chercher(f, m);
      if(e != null && (ok == null || e > ok + 0.02)){ ok = e; mp = m; }
      if(ok != null && ok >= (f.querySelector(".pleine-largeur") ? ACCEPTE : SEUIL)) break;
    }
    tient(f, ok == null ? 0.62 : ok, ok == null ? 0.45 : mp);
    // page peu remplie (texte court) : on agrandit encore les visuels tant que la page n'est pas pleine
    if(ok === EMAX && vis){
      let evb = parseFloat(f.style.getPropertyValue("--echelle-visuel")), evh = 2.2, evok = evb;
      for(let k = 0; k < 8; k++){
        const m = (evb + evh) / 2;
        f.style.setProperty("--echelle-visuel", m.toFixed(3));
        if(deborde(f)) evh = m; else { evok = m; evb = m; }
      }
      f.style.setProperty("--echelle-visuel", evok.toFixed(3));
    }
    // la place qui reste dans la colonne des visuels est offerte à une photo d'illustration
    if(vis && f._photos && f._photos.length && !deborde(f)) remettrePhoto(f, f._photos[0]);
  }

  /* Disposition B : la leçon en pleine largeur (texte sur 2 colonnes), puis les visuels
     côte à côte en grand, à la même hauteur. Utile quand la colonne de droite resterait
     à moitié vide (visuels plats ou peu nombreux). */
  function fitB(f){
    f.querySelector(".corps").classList.add("rangee");
    f.style.setProperty("--echelle-visuel", "1");
    f.style.setProperty("--rb", "1");
    for(let e = EMAX; e >= ACCEPTE - 0.001; e -= 0.04){          // d'abord le texte le plus grand, rangée pleine largeur
      f.style.setProperty("--echelle", e.toFixed(3));
      if(!deborde(f)) return;
    }
    f.style.setProperty("--echelle", "0.92");                     // sinon on réduit la rangée
    for(let r = 0.95; r >= 0.45; r -= 0.05){
      f.style.setProperty("--rb", r.toFixed(2));
      if(!deborde(f)) return;
    }
  }

  // surface des cartes, graphiques et schémas, en mm² : ce que l'on cherche à agrandir
  function metriques(f){
    const mm = f.clientWidth / 210;
    let aire = 0;
    f.querySelectorAll(".visuel:not(.v-photo) svg").forEach(s => {
      const r = s.getBoundingClientRect(); aire += r.width * r.height / (mm * mm);
    });
    // place vide dans la colonne de droite (disposition A) : hauteur du texte − hauteur des visuels
    const t = f.querySelector(".texte"), v = f.querySelector(".visuels");
    const vide = (t && v && !f.querySelector(".corps.rangee")) ? (t.offsetHeight - v.offsetHeight) / mm : 0;
    return { aire, vide, e: parseFloat(f.style.getPropertyValue("--echelle")), deb: deborde(f) };
  }

  function ajuster(f){
    const vis = preparer(f);
    fitA(f, vis);
    if(vis && !f._photoSeule && !f.querySelector(".pleine-largeur")){
      const mA = metriques(f);
      preparer(f); fitB(f);
      const mB = metriques(f);
      const valA = !mA.deb && mA.e >= ACCEPTE - 0.005, valB = !mB.deb && mB.e >= ACCEPTE - 0.005;
      // B l'emporte si ses visuels sont nettement plus grands, ou si la colonne de droite
      // resterait à moitié vide en A (plus de 30 mm de blanc), pourvu que le texte reste lisible
      const prendreB = valB ? (!valA || (mB.aire > 1.15 * mA.aire && mB.e >= SEUIL - 0.005) || mA.vide > 30)
                            : (!valA && !mB.deb && mB.e > mA.e);
      if(!prendreB){ preparer(f); fitA(f, f.querySelector(".visuels")); }
    }
    // l'espace restant est absorbé par le cadre de la leçon et celui du visuel principal :
    // les deux zones descendent jusqu'au bas du corps, la page est pleine
    f.classList.add("rempli");
    if(deborde(f)) f.classList.remove("rempli");
    f.classList.toggle("deborde", deborde(f));
  }

  function imagesChargees(racine){
    const imgs = [...racine.querySelectorAll("img")];
    return Promise.all(imgs.map(img => new Promise(res => {
      const fin = () => res();
      const erreur = () => { const fig = img.closest("figure"); if(fig) fig.remove(); res(); };
      if(img.complete){ if(img.naturalWidth === 0) erreur(); else fin(); }
      else{ img.addEventListener("load", fin, {once:true}); img.addEventListener("error", erreur, {once:true}); }
    })));
  }

  /* ---------- Rendu ---------- */
  async function rendre(){
    const zone = $("#pages");
    const liste = selection();
    zone.innerHTML = liste.map((l, i) => page(l, i, liste.length)).join("");
    await imagesChargees(zone);
    zone.querySelectorAll(".visuel.photo img").forEach(img => {
      if(img.naturalWidth) img.closest("figure").style.setProperty("--ratio", Math.max(0.8, Math.min(1.8, img.naturalWidth / img.naturalHeight)).toFixed(2));
    });
    if(document.fonts && document.fonts.ready) await document.fonts.ready;
    zone.querySelectorAll(".feuille").forEach(ajuster);
    document.body.dataset.pret = "1";
    majBarre();
  }

  function majBarre(){
    document.querySelectorAll(".bascule button").forEach(b => b.classList.toggle("actif", b.dataset.niveau === etat.niveau));
    const sel = $("#choix-lecon");
    const v = visibles();
    const courant = (etat.salle && v.find(l => String(l.salle) === String(etat.salle)))
      ? v.find(l => String(l.salle) === String(etat.salle)).id : etat.lecon;
    sel.innerHTML = `<option value="toutes">Toutes les leçons (${v.length} pages)</option>` +
      v.map(l => `<option value="${l.id}">${l.salle ? ((etat.a4.jeu||{}).unite || "Salle") + " " + l.salle + " — " : ""}${l.titre}</option>`).join("");
    sel.value = v.some(l => l.id === courant) ? courant : "toutes";
  }

  function majURL(){
    const p = new URLSearchParams();
    p.set("niveau", etat.niveau);
    p.set("lecon", etat.lecon);
    history.replaceState(null, "", location.pathname + "?" + p.toString());
  }

  function brancher(){
    document.querySelectorAll(".bascule button").forEach(b => b.addEventListener("click", () => {
      etat.niveau = b.dataset.niveau; majURL(); rendre();
    }));
    $("#choix-lecon").addEventListener("change", e => {
      etat.lecon = e.target.value; etat.salle = null; majURL(); rendre();
    });
    $("#btn-imprimer").addEventListener("click", () => window.print());
  }

  async function demarrer(){
    brancher();
    try{
      const a4 = await lireJSON("assets/data/lecons-a4.json", false);
      if(a4) etat.a4 = a4;
      let liste;
      if(a4 && Array.isArray(a4.lecons_base)) liste = a4.lecons_base;               // leçons rédigées pour l'impression
      else if(window.MISSION && window.MISSION.lecons) liste = depuisMission();        // mission-geo : leçons en JS
      else liste = ((await lireJSON("assets/data/lecons.json", true)).lecons || []);
      etat.lecons = liste.slice().sort((a, b) => (a.salle || 99) - (b.salle || 99));
    }catch(e){
      $("#pages").innerHTML = `<div class="message">Les leçons n'ont pas pu être chargées.<br>
        Ouvrez le jeu avec <b>lancer.bat</b> (ou en ligne), puis revenez à cette page :
        le navigateur bloque la lecture des fichiers quand la page est ouverte par un double-clic.</div>`;
      return;
    }
    const jeu = etat.a4.jeu || {};
    if(jeu.couleur) document.documentElement.style.setProperty("--c1", jeu.couleur);
    if(jeu.accent) document.documentElement.style.setProperty("--c2", jeu.accent);
    if(jeu.couleur_pale) document.documentElement.style.setProperty("--c1-pale", jeu.couleur_pale);
    if(jeu.accent_pale) document.documentElement.style.setProperty("--c2-pale", jeu.accent_pale);
    if(jeu.titre){ document.title = "Leçons à imprimer — " + jeu.titre; $("#titre-barre").textContent = "Leçons à imprimer — " + jeu.titre; }
    await rendre();
    if(etat.imprimer) setTimeout(() => window.print(), 300);
  }

  window.LECONS_A4 = { rendre, etat };
  document.addEventListener("DOMContentLoaded", demarrer);
})();
