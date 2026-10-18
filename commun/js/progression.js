/* ============================================================
   PROGRESSION PORTABLE : passeport + parties, d'un appareil à l'autre (N16)
   ------------------------------------------------------------
   Le passeport de compétences (C3) et l'historique des parties (trophées N1,
   résultats D5) sont gardés sur l'appareil où l'élève a joué. Un élève qui
   commence sur une tablette de classe et continue chez lui perdrait donc sa
   progression. Ce module (sans serveur ni compte) permet de :
     • « 📤 Exporter ma progression » : un fichier .json, ou un CODE COURT
       à copier-coller (texte « EGP1.… », compressé quand le navigateur sait) ;
     • « 📥 Importer » : le fichier ou le code est FUSIONNÉ avec la progression
       de l'appareil, sans jamais écraser ce qui est plus récent.
   Même enveloppe que l'export / reprise de partie (A5, export-partie.js) :
       { format:"escape-game-passeport", versionFormat:1, exporteLe, titre,
         eleve?, eleves:[…], notes:{élève:{cle:{v,date,t}}}, parties:[compte-rendu…] }
   Règles de fusion :
     • élèves : réunion des listes ;
     • notes du passeport : pour chaque compétence d'un élève, la note la PLUS RÉCENTE
       (t, sinon date) l'emporte ; à égalité, celle de l'appareil est gardée ;
     • parties : réunion (une partie est identifiée par jeu + élève + mode + début) ;
       à égalité, la partie terminée, ou celle qui a le détail des énigmes (N12), est gardée ;
       les 100 plus récentes sont conservées, comme l'historique des jeux ;
     • une note effacée ne se propage pas (l'absence d'une note ne dit rien).
   Un fichier de l'ancien export du passeport ({eleves, notes}) est accepté.
   Utilisé par passeport.html et par l'écran d'accueil des jeux (bouton « 🎓 Ma progression »).
   ============================================================ */
(function(){
  const FORMAT = "escape-game-passeport", VERSION = 1;
  const CLE_PASSEPORT = "escape_passeport", CLE_PARTIES = "escape_resultats";
  const MAX_PARTIES = 100;
  const norm = s => String(s == null ? "" : s).normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/\s+/g, " ").trim().toLowerCase();
  const slug = s => String(s || "classe").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "").toLowerCase() || "classe";
  const jour = () => new Date().toISOString().slice(0, 10);
  const lireJSON = (stock, cle, defaut) => { try{ const v = JSON.parse(stock.getItem(cle) || "null"); return v == null ? defaut : v; }catch(e){ return defaut; } };
  const stockage = () => { try{ return window.localStorage; }catch(e){ return null; } };

  /* ---------------- Lecture de l'appareil ---------------- */
  function lire(stock){
    stock = stock || stockage();
    const p = lireJSON(stock, CLE_PASSEPORT, {}) || {};
    return {
      eleves: Array.isArray(p.eleves) ? p.eleves.slice() : [],
      notes: p.notes && typeof p.notes === "object" ? JSON.parse(JSON.stringify(p.notes)) : {},
      parties: lireJSON(stock, CLE_PARTIES, []).filter(x => x && x.type === "escape-game-compte-rendu")
    };
  }
  function ecrire(etat, stock){
    stock = stock || stockage();
    stock.setItem(CLE_PASSEPORT, JSON.stringify({ eleves: etat.eleves, notes: etat.notes }));
    stock.setItem(CLE_PARTIES, JSON.stringify(etat.parties));
  }

  /* ---------------- Export ---------------- */
  /** Le contenu à emporter : toute la progression de l'appareil, ou celle d'un seul élève (nom normalisé). */
  function contenu(options){
    options = options || {};
    const e = options.etat || lire(options.stockage);
    const n = options.eleve ? norm(options.eleve) : "";
    const eleves = n ? e.eleves.filter(x => norm(x) === n) : e.eleves.slice();
    if(n && !eleves.length) eleves.push(String(options.eleve).trim());
    const notes = {};
    Object.keys(e.notes).forEach(k => { if(!n || norm(k) === n) notes[k] = e.notes[k]; });
    const parties = e.parties.filter(p => !n || norm(p.eleve) === n);
    return { format: FORMAT, versionFormat: VERSION, titre: "Passeport de compétences et parties des escape games",
      exporteLe: new Date().toISOString(), eleve: n ? String(options.eleve).trim() : "", eleves, notes, parties };
  }
  const nomFichier = c => `passeport-${slug(c.eleve)}-${jour()}.json`;

  /* ---------------- Fusion ---------------- */
  const tn = x => (x && (x.t || (x.date ? x.date + "T00:00" : ""))) || "";
  const cleePartie = r => [r.jeu, norm(r.eleve), r.mode, r.partie || r.date].join("|");
  const riche = r => (r.termine ? 2 : 0) + (Array.isArray(r.detail) && r.detail.length ? 1 : 0);
  /** Fusionne « distant » dans « local » (sans modifier ses arguments). Renvoie { etat, bilan }. */
  function fusionner(local, distant){
    const etat = { eleves: local.eleves.slice(), notes: JSON.parse(JSON.stringify(local.notes)), parties: local.parties.slice() };
    const bilan = { eleves: 0, notes: 0, remplacees: 0, gardees: 0, parties: 0 };
    const d = distant || {};
    (Array.isArray(d.eleves) ? d.eleves : []).forEach(x => {
      if(typeof x === "string" && x.trim() && !etat.eleves.some(y => norm(y) === norm(x))){ etat.eleves.push(x.trim()); bilan.eleves++; }
    });
    Object.entries(d.notes && typeof d.notes === "object" ? d.notes : {}).forEach(([eleve, cles]) => {
      const nom = etat.eleves.find(y => norm(y) === norm(eleve)) || eleve;
      if(!etat.eleves.some(y => y === nom)){ etat.eleves.push(nom); bilan.eleves++; }
      const cible = etat.notes[nom] = etat.notes[nom] || {};
      Object.entries(cles || {}).forEach(([cle, note]) => {
        if(!note || !/^[NEA]$/.test(note.v)) return;
        const loc = cible[cle];
        if(!loc){ cible[cle] = note; bilan.notes++; }
        else if(tn(note) > tn(loc)){ cible[cle] = note; bilan.remplacees++; }
        else if(loc.v !== note.v) bilan.gardees++;
      });
    });
    (Array.isArray(d.parties) ? d.parties : []).forEach(r => {
      if(!r || r.type !== "escape-game-compte-rendu") return;
      const i = etat.parties.findIndex(x => cleePartie(x) === cleePartie(r));
      if(i < 0){ etat.parties.push(r); bilan.parties++; }
      else if(riche(r) > riche(etat.parties[i])){ etat.parties[i] = r; bilan.parties++; }
    });
    etat.parties.sort((a, b) => String(a.date).localeCompare(String(b.date)));
    etat.parties = etat.parties.slice(-MAX_PARTIES);
    return { etat, bilan };
  }

  /* ---------------- Code court ---------------- */
  /* UTF-8 sans TextEncoder (absent de certains environnements) */
  const enOctets = t => { const b = unescape(encodeURIComponent(t)), o = new Uint8Array(b.length); for(let i = 0; i < b.length; i++) o[i] = b.charCodeAt(i); return o; };
  const enTexte = o => { let b = ""; for(let i = 0; i < o.length; i += 0x8000) b += String.fromCharCode.apply(null, o.subarray(i, i + 0x8000)); return decodeURIComponent(escape(b)); };
  const versB64 = oct => { let s = ""; for(let i = 0; i < oct.length; i += 0x8000) s += String.fromCharCode.apply(null, oct.subarray(i, i + 0x8000)); return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, ""); };
  const depuisB64 = t => { const s = atob(String(t).replace(/-/g, "+").replace(/_/g, "/")); const o = new Uint8Array(s.length); for(let i = 0; i < s.length; i++) o[i] = s.charCodeAt(i); return o; };
  const CS = () => (typeof window !== "undefined" && window.CompressionStream) || (typeof CompressionStream !== "undefined" ? CompressionStream : null);
  const DS = () => (typeof window !== "undefined" && window.DecompressionStream) || (typeof DecompressionStream !== "undefined" ? DecompressionStream : null);
  async function flux(Classe, octets, mode){
    const f = new Classe(mode), w = f.writable.getWriter();
    w.write(octets); w.close();
    return new Uint8Array(await new Response(f.readable).arrayBuffer());
  }
  /** Version compacte du contenu : sans espaces, sans le détail des énigmes (le code reste court). */
  function compact(c){
    const parties = (c.parties || []).map(p => { const q = Object.assign({}, p); delete q.detail; delete q.code; return q; });
    return Object.assign({}, c, { parties, allege: true });
  }
  async function codeCourt(c, options){
    const texte = JSON.stringify(compact(c));
    const octets = enOctets(texte);
    if(!(options && options.sansCompression) && CS()){
      try{ return "EGP1z." + versB64(await flux(CS(), octets, "deflate-raw")); }catch(e){}
    }
    return "EGP1." + versB64(octets);
  }
  async function depuisCode(code){
    const m = String(code || "").trim().replace(/\s+/g, "").match(/^EGP1(z?)\.([A-Za-z0-9_-]+)$/);
    if(!m) throw new Error("Ce texte n'est pas un code de progression (il doit commencer par « EGP1. »).");
    let octets = depuisB64(m[2]);
    if(m[1]){
      if(!DS()) throw new Error("Ce code est compressé : ouvrez-le avec un navigateur récent (Chrome, Edge, Firefox, Safari).");
      octets = await flux(DS(), octets, "deflate-raw");
    }
    return JSON.parse(enTexte(octets));
  }

  /* ---------------- Import ---------------- */
  /** Contrôle un contenu ; renvoie un message d'erreur ou "". Accepte l'ancien export du passeport. */
  function controler(c){
    if(!c || typeof c !== "object") return "Fichier illisible.";
    if(c.format === FORMAT){ if(c.versionFormat > VERSION) return "Ce fichier vient d'une version plus récente du site : mettez la page à jour."; return ""; }
    if(Array.isArray(c.eleves) && c.notes && typeof c.notes === "object" && !c.format) return "";      // ancien export du passeport (C3)
    return "Ce fichier n'est pas une progression exportée par les escape games.";
  }
  /** Importe un texte (fichier .json ou code court) : contrôle, fusion, écriture. Renvoie { ok, message, bilan }. */
  async function importerTexte(texte, options){
    options = options || {};
    let c = null;
    const t = String(texte || "").trim();
    try{
      c = /^EGP1/.test(t.replace(/\s+/g, "")) ? await depuisCode(t) : JSON.parse(t);
    }catch(e){ return { ok: false, message: /code|compress/.test(e.message) ? e.message : "Fichier illisible (ce n'est ni un fichier .json valide, ni un code « EGP1… »)." }; }
    const err = controler(c);
    if(err) return { ok: false, message: err };
    const stock = options.stockage || stockage();
    const r = fusionner(lire(stock), c);
    try{ ecrire(r.etat, stock); }catch(e){ return { ok: false, message: "Impossible d'écrire sur cet appareil (navigation privée ?)." }; }
    const b = r.bilan;
    const bits = [];
    if(b.notes) bits.push(`${b.notes} compétence(s) ajoutée(s)`);
    if(b.remplacees) bits.push(`${b.remplacees} mise(s) à jour (plus récentes)`);
    if(b.gardees) bits.push(`${b.gardees} note(s) de cet appareil gardée(s) (plus récentes)`);
    if(b.parties) bits.push(`${b.parties} partie(s) ajoutée(s)`);
    if(b.eleves) bits.push(`${b.eleves} élève(s) ajouté(s)`);
    return { ok: true, bilan: b, etat: r.etat,
      message: bits.length ? "📥 Progression fusionnée : " + bits.join(", ") + "." : "📥 Rien de nouveau : cet appareil était déjà à jour." };
  }

  /* ---------------- Fichier / presse-papiers (navigateur) ---------------- */
  function telecharger(nom, texte){
    try{
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([texte], { type: "application/json" }));
      a.download = nom; document.body.appendChild(a); a.click(); a.remove();
    }catch(e){}
    window.__dernierExport = { nom, contenu: texte };
  }
  async function exporterFichier(options){
    const c = contenu(options), texte = JSON.stringify(c, null, 1), nom = nomFichier(c);
    telecharger(nom, texte);
    return { nom, contenu: c };
  }
  async function copier(texte){
    try{ await navigator.clipboard.writeText(texte); return true; }catch(e){ return false; }
  }

  /* ---------------- Panneau « 🎓 Ma progression » (écran d'accueil des jeux) ---------------- */
  function panneau(){
    if(document.getElementById("panneau-progression")) return;
    if(!document.getElementById("style-progression")){
      const st = document.createElement("style"); st.id = "style-progression";
      st.textContent = "#panneau-progression .btn{font:inherit;font-size:.92rem;padding:6px 14px;border-radius:999px;border:2px solid #c9a227;background:#fff8e1;color:#2b1d10;cursor:pointer;display:inline-block}";
      document.head.appendChild(st);
    }
    const nomAccueil = (document.getElementById("input-equipe") || document.getElementById("nom-equipe") || {}).value || "";
    const el = document.createElement("div");
    el.id = "panneau-progression"; el.setAttribute("role", "dialog"); el.setAttribute("aria-label", "Ma progression");
    el.style.cssText = "position:fixed;inset:0;z-index:9300;background:rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center;padding:12px";
    el.innerHTML = `<div style="background:#fffdf6;color:#1f2430;border-radius:16px;max-width:560px;width:100%;max-height:92vh;overflow:auto;padding:16px 20px;font-family:system-ui,sans-serif">
      <h2 style="margin:0 0 6px">🎓 Ma progression</h2>
      <p style="margin:0 0 10px;font-size:.92rem;opacity:.85">Pour continuer chez toi ce que tu as commencé en classe (ou l'inverse) : tu emportes ta progression dans un fichier ou dans un code à copier, puis tu l'importes sur l'autre appareil. Rien n'est envoyé sur internet.</p>
      <label style="font-size:.9rem">Ton nom ou celui de ton équipe :<br><input id="prog-nom" type="text" maxlength="40" value="${String(nomAccueil).replace(/"/g, "&quot;")}" placeholder="(laisser vide : tout ce qui est sur cet appareil)" style="width:100%;padding:8px;font:inherit;border:2px solid #ccc;border-radius:10px;margin:4px 0 10px"></label>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:10px">
        <button type="button" id="prog-exporter" class="btn">📤 Exporter ma progression (fichier)</button>
        <button type="button" id="prog-code" class="btn gris">🔤 Obtenir un code court</button>
      </div>
      <textarea id="prog-code-texte" readonly rows="3" style="display:none;width:100%;font:.8rem monospace;padding:8px;border-radius:10px;border:2px solid #ccc"></textarea>
      <hr style="margin:12px 0;border:0;border-top:1px solid #ddd">
      <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:8px">
        <label class="btn gris" for="prog-fichier" style="cursor:pointer">📥 Importer un fichier</label><input type="file" id="prog-fichier" accept=".json,application/json" hidden>
      </div>
      <textarea id="prog-coller" rows="2" placeholder="… ou colle ici un code « EGP1… »" style="width:100%;font:.8rem monospace;padding:8px;border-radius:10px;border:2px solid #ccc"></textarea>
      <button type="button" id="prog-importer" class="btn gris" style="margin-top:6px">📥 Importer le code</button>
      <p id="prog-message" role="status" style="min-height:1.4em;margin:10px 0 0;font-size:.92rem"></p>
      <div style="text-align:right"><button type="button" id="prog-fermer" class="btn">Fermer</button></div></div>`;
    document.body.appendChild(el);
    const msg = t => { el.querySelector("#prog-message").textContent = t; };
    const nom = () => el.querySelector("#prog-nom").value.trim();
    el.querySelector("#prog-fermer").addEventListener("click", () => el.remove());
    el.querySelector("#prog-exporter").addEventListener("click", async () => {
      const r = await exporterFichier({ eleve: nom() });
      msg(`📤 ${r.nom} enregistré (${r.contenu.parties.length} partie(s), ${Object.keys(r.contenu.notes).length} élève(s) avec des compétences). Garde ce fichier pour l'autre appareil.`);
    });
    el.querySelector("#prog-code").addEventListener("click", async () => {
      const code = await codeCourt(contenu({ eleve: nom() }));
      const ta = el.querySelector("#prog-code-texte"); ta.style.display = "block"; ta.value = code; ta.select();
      msg((await copier(code)) ? `🔤 Code copié (${code.length} caractères) : colle-le sur l'autre appareil.` : `🔤 Code prêt (${code.length} caractères) : copie-le puis colle-le sur l'autre appareil.`);
    });
    el.querySelector("#prog-fichier").addEventListener("change", async ev => {
      const f = ev.target.files && ev.target.files[0]; if(!f) return;
      msg((await importerTexte(await f.text())).message); ev.target.value = "";
    });
    el.querySelector("#prog-importer").addEventListener("click", async () => {
      msg((await importerTexte(el.querySelector("#prog-coller").value)).message);
    });
  }
  function bouton(){
    const go = document.getElementById("btn-demarrer") || document.getElementById("btn-embarquer");
    const zone = go && (go.closest(".boutons") || go.closest(".boutons-accueil") || go.parentNode);
    if(!zone || document.getElementById("btn-progression")) return;
    const p = document.createElement("p");
    p.className = "progression-portable"; p.style.cssText = "text-align:center;margin:.4rem 0 0";
    p.innerHTML = `<button type="button" class="${document.getElementById("btn-embarquer") ? "btn-laiton gris petit" : "btn gris petit"}" id="btn-progression" title="Continuer chez soi, ou en classe, ce qu'on a commencé ailleurs">🎓 Ma progression (maison ↔ classe)</button>`;
    p.querySelector("button").addEventListener("click", panneau);
    const apres = document.querySelector(".import-partie") || zone;
    apres.after(p);
  }
  if(typeof document !== "undefined" && document.getElementById){
    if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", bouton); else bouton();
  }
  const API = { FORMAT, VERSION, lire, ecrire, contenu, fusionner, codeCourt, depuisCode, importerTexte, controler, exporterFichier, nomFichier, panneau, norm };
  if(typeof window !== "undefined") window.PROGRESSION = API;
  if(typeof module !== "undefined") module.exports = API;
})();
