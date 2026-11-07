/* ============================================================
   RAPPORT DE SÉANCE EN PDF (amélioration N31) — tronc commun
   ------------------------------------------------------------
   Le tableur (D5) et le bilan de classe (N12) donnent des données détaillées, à retravailler pour un
   cahier journal ou un rapport d'inspection. Ce module fabrique, à partir des comptes-rendus déjà
   produits, un document PDF d'UNE page, prêt à coller ou à joindre :
     classe · date · jeu · durée de la séance · nombre d'équipes · équipes (résultat, durée, état) ·
     compétences travaillées (liées au programme : C2 / C3) · référence du programme officiel.
   Le PDF est écrit ici même (texte, filets et aplats, police Helvetica de base, accents français
   compris) : AUCUNE bibliothèque, rien à installer, fonctionne hors connexion et sans serveur.

   Une SÉANCE = les parties d'un même jeu, jouées en équipe le même jour (le mode individuel, à la
   maison, n'en est pas une). Une équipe qui a rejoué est comptée une fois (sa dernière partie).

   SÉANCE INTERROMPUE OU INCOMPLÈTE : le rapport reste correct et le dit. Une équipe qui n'a pas
   terminé est marquée « interrompue » ; un bandeau précise que les chiffres portent sur ce qui a été
   joué ; sans le détail énigme par énigme (anciennes parties, textes collés), les compétences listées
   sont celles du jeu, présentées comme « prévues » et non comme « travaillées » ; une durée absente
   s'écrit « non enregistrée », jamais « 0 min ». Aucune valeur « undefined » ou « NaN » ne sort.

   Garantie « une page » : les listes longues sont raccourcies (« … et N autres équipes ») pour que le
   dernier bloc reste au-dessus de la marge basse.

   API : RAPPORT_SEANCE.seances(parties) → [{ cle, jeu, jour, parties }]  (la plus récente d'abord)
         RAPPORT_SEANCE.modele({ parties, jeu, meta, catalogue, classe, maintenant }) → modèle
         RAPPORT_SEANCE.pdf(modele) → { octets:Uint8Array, bas, pages:1 }
         RAPPORT_SEANCE.nomFichier(modele)
   ============================================================ */
(function(){
  const GRADES = ["mousse", "matelot", "timonier", "lieutenant", "second"];
  const JOURS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];
  const MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];
  const nombre = v => (typeof v === "number" && isFinite(v)) ? v : 0;
  const nettoie = s => String(s == null ? "" : s).replace(/[  ]/g, " ").replace(/\s+/g, " ").trim();

  /* ================= Données : séances et modèle ================= */
  const jourDe = r => String(r.date || "").slice(0, 10);
  function seances(parties){
    const m = new Map();
    for(const r of parties || []){
      if(!r || r.mode === "solo" || !r.jeu || !/^\d{4}-\d\d-\d\d$/.test(jourDe(r))) continue;
      const cle = r.jeu + "|" + jourDe(r);
      if(!m.has(cle)) m.set(cle, { cle, jeu: r.jeu, jour: jourDe(r), parties: [] });
      m.get(cle).parties.push(r);
    }
    return [...m.values()].sort((a, b) => b.jour.localeCompare(a.jour) || a.jeu.localeCompare(b.jeu));
  }
  function dateLongue(jour){
    const d = new Date(jour + "T12:00:00");
    return isNaN(d) ? "" : `${JOURS[d.getDay()]} ${d.getDate() === 1 ? "1er" : d.getDate()} ${MOIS[d.getMonth()]} ${d.getFullYear()}`;
  }
  /** Une équipe = une ligne : sa dernière partie du jour (une partie terminée l'emporte sur une interrompue plus récente). */
  function parEquipe(parties){
    const m = new Map();
    for(const r of parties){
      const k = nettoie(r.eleve).toLowerCase() || ("?" + m.size);
      const cur = m.get(k);
      if(!cur || (!!r.termine > !!cur.termine) || (!!r.termine === !!cur.termine && String(r.date) > String(cur.date))) m.set(k, r);
    }
    return [...m.values()].sort((a, b) => String(a.eleve).localeCompare(String(b.eleve), "fr"));
  }
  function modele(o){
    const parties = (o.parties || []).filter(r => r && r.jeu === o.jeu && r.mode !== "solo");
    const jour = parties.length ? jourDe(parties[0]) : "";
    const lignes = parEquipe(parties);
    const info = ((o.catalogue && o.catalogue.jeux) || []).find(j => j.dossier === o.jeu || j.id === o.jeu) || {};
    const meta = o.meta || {};
    const termine = lignes.filter(r => r.termine), interrompues = lignes.length - termine.length;
    const durees = lignes.map(r => nombre(r.dureeMin)).filter(x => x > 0);
    const plusLongue = durees.length ? Math.max(...durees) : 0;
    const moyenne = durees.length ? Math.round(durees.reduce((a, b) => a + b, 0) / durees.length) : 0;
    /* compétences : détail énigme par énigme quand il existe, sinon les compétences du jeu (prévues) */
    const ordre = Object.keys(meta.comp || {});
    const stats = new Map();
    for(const r of lignes) for(const n of (Array.isArray(r.detail) ? r.detail : [])){
      if(!n || n.id === "coffre") continue;
      const lecon = n.l || (meta.leconDeSalle || {})[n.s] || "";
      if(!lecon) continue;
      const s = stats.get(lecon) || { lecon, n: 0, pc: 0 };
      s.n++; if(n.pc) s.pc++; stats.set(lecon, s);
    }
    const texteDe = l => nettoie((meta.comp || {})[l] || (meta.leconTitre || {})[l] || "");
    let competences, detailDispo = stats.size > 0;
    if(detailDispo){
      competences = [...stats.values()].filter(s => texteDe(s.lecon)).sort((a, b) => (ordre.indexOf(a.lecon) + 1 || 99) - (ordre.indexOf(b.lecon) + 1 || 99))
        .map(s => ({ texte: texteDe(s.lecon), pc: Math.round(100 * s.pc / s.n) }));
      if(!competences.length) detailDispo = false;
    }
    if(!detailDispo) competences = ordre.map(texteDe).filter(Boolean).map(t => ({ texte: t }));
    const programmes = ((info.programme || []).map(k => o.catalogue && o.catalogue.programmes && o.catalogue.programmes[k]).filter(Boolean))
      .map(p => `${p.discipline} — ${p.texte}`);
    const avertissements = [];
    if(interrompues) avertissements.push(`Séance incomplète : ${interrompues} équipe${interrompues > 1 ? "s" : ""} sur ${lignes.length} n'${interrompues > 1 ? "ont" : "a"} pas terminé (partie interrompue). Les chiffres portent sur ce qui a été joué.`);
    if(!lignes.length) avertissements.push("Aucune partie en équipe pour ce jeu à cette date.");
    if(lignes.length && !detailDispo) avertissements.push("Le détail énigme par énigme n'est pas enregistré pour cette séance : les compétences indiquées sont celles prévues par le jeu.");
    return {
      classe: nettoie(o.classe), jour, dateTexte: dateLongue(jour),
      jeuTitre: nettoie(info.titre || (parties[0] && parties[0].titre) || o.jeu), matiere: nettoie(info.matiere),
      nbEquipes: lignes.length, nbTerminees: termine.length, nbInterrompues: interrompues,
      plusLongue, moyenne, dureeTexte: plusLongue ? `${plusLongue} min (équipe la plus longue), ${moyenne} min en moyenne` : "non enregistrée",
      equipes: lignes.map(r => {
        const g = GRADES.includes(r.palier) ? r.palier : "";
        const sc = nombre(r.score), max = nombre(r.scoreMax);
        return { nom: nettoie(r.eleve) || "(sans nom)", niveau: nettoie(g || r.niveau) || "—",
          enigmes: `${nombre(r.enigmes)}/${nombre(r.total) || "?"}`, score: max ? `${Math.round(100 * sc / max)} %` : (sc ? `${sc} pts` : "—"),
          duree: nombre(r.dureeMin) > 0 ? `${nombre(r.dureeMin)} min` : "—", etat: r.termine ? "terminée" : "interrompue", fini: !!r.termine };
      }),
      competences, detailDispo, programmes, avertissements,
      genere: o.maintenant instanceof Date && !isNaN(o.maintenant) ? o.maintenant : new Date()
    };
  }
  const slug = s => nettoie(s).normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "").toLowerCase() || "seance";
  const nomFichier = m => `rapport-seance-${m.jour || "sans-date"}-${slug(m.jeuTitre)}.pdf`;

  /* ================= PDF : écriture ================= */
  /* Largeurs Helvetica (1/1000 em) des caractères ASCII 32..126 ; les lettres accentuées ont celle de leur lettre de base. */
  const LARG = [278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278, 556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556,
    1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556,
    333, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334, 260, 334, 584];
  const WIN1252 = { "€": 0x80, "‚": 0x82, "ƒ": 0x83, "„": 0x84, "…": 0x85, "†": 0x86, "‡": 0x87, "ˆ": 0x88, "‰": 0x89, "Š": 0x8A, "‹": 0x8B, "Œ": 0x8C, "Ž": 0x8E,
    "‘": 0x91, "’": 0x92, "“": 0x93, "”": 0x94, "•": 0x95, "–": 0x96, "—": 0x97, "˜": 0x98, "™": 0x99, "š": 0x9A, "›": 0x9B, "œ": 0x9C, "ž": 0x9E, "Ÿ": 0x9F };
  const SPECIAL = { 0x85: 1000, 0x92: 222, 0x91: 222, 0x93: 333, 0x94: 333, 0x95: 350, 0x96: 556, 0x97: 1000, 0x9C: 944, 0x8C: 1000, 0x80: 556, 0xA0: 278, 0xAB: 556, 0xBB: 556, 0xB0: 400, 0xD7: 584 };
  /** Texte → octets Windows-1252 (une chaîne de caractères 0-255). Hors jeu de caractères : supprimé (emojis, flèches…). */
  function encode(s){
    let out = "";
    for(const ch of nettoie(s)){
      const c = ch.codePointAt(0);
      if(c >= 32 && c < 127) out += ch;
      else if(WIN1252[ch] != null) out += String.fromCharCode(WIN1252[ch]);
      else if(c >= 0x80 && c <= 0xFF) out += ch;          // déjà en Windows-1252 (encode est sans danger si on le rappelle)
      else if(c === 0x2019) out += "\x92";
      else if(c === 0x2192) out += "->";
    }
    return out.replace(/ {2,}/g, " ").trim();
  }
  function largeur(enc, taille){
    let w = 0;
    for(let i = 0; i < enc.length; i++){
      const c = enc.charCodeAt(i);
      if(c >= 32 && c < 127) w += LARG[c - 32];
      else if(SPECIAL[c] != null) w += SPECIAL[c];
      else { const base = String.fromCharCode(c).normalize("NFD").charCodeAt(0); w += base >= 32 && base < 127 ? LARG[base - 32] : 556; }
    }
    return w * taille / 1000;
  }
  const echappe = enc => enc.replace(/[\\()]/g, m => "\\" + m).replace(/[\r\n]/g, " ");
  /** Coupe un texte en lignes qui tiennent dans « max » points. */
  function coupe(texte, taille, max){
    const mots = encode(texte).split(" ").filter(Boolean), lignes = [];
    let cur = "";
    for(let mot of mots){
      while(largeur(mot, taille) > max){          // mot plus large que la ligne : on le coupe
        let k = mot.length; while(k > 1 && largeur(mot.slice(0, k), taille) > max) k--;
        if(cur){ lignes.push(cur); cur = ""; }
        lignes.push(mot.slice(0, k)); mot = mot.slice(k);
      }
      const essai = cur ? cur + " " + mot : mot;
      if(largeur(essai, taille) <= max) cur = essai; else { if(cur) lignes.push(cur); cur = mot; }
    }
    if(cur) lignes.push(cur);
    return lignes.length ? lignes : [""];
  }
  /** Coupe en ajoutant « … » à la fin si le texte dépasse « max » (une seule ligne). */
  function tronque(texte, taille, max){
    const e = encode(texte);
    if(largeur(e, taille) <= max) return e;
    let k = e.length; while(k > 1 && largeur(e.slice(0, k) + "...", taille) > max) k--;
    return e.slice(0, k).trimEnd() + "...";
  }

  const A4 = { l: 595.28, h: 841.89 }, MARGE = 40, BAS = 52;
  function pdf(m){
    const ops = [];
    let y = A4.h - MARGE;
    const rgb = c => c.map(v => (v / 255).toFixed(3)).join(" ");
    const texte = (s, x, yy, taille, o = {}) => {
      const enc = echappe(encode(s));
      ops.push(`BT ${rgb(o.couleur || [31, 36, 48])} rg ${o.gras ? "2 Tr 0.35 w " + rgb(o.couleur || [31, 36, 48]) + " RG " : "0 Tr "}/F1 ${taille} Tf ${x.toFixed(2)} ${yy.toFixed(2)} Td (${enc}) Tj ET`);
    };
    const rect = (x, yy, w, h, remplir, bord) => {
      ops.push(`${remplir ? rgb(remplir) + " rg " : ""}${bord ? rgb(bord) + " RG 0.8 w " : ""}${x.toFixed(2)} ${yy.toFixed(2)} ${w.toFixed(2)} ${h.toFixed(2)} re ${remplir && bord ? "B" : remplir ? "f" : "S"}`);
    };
    const filet = (x1, yy, x2, couleur = [210, 205, 195]) => ops.push(`${rgb(couleur)} RG 0.6 w ${x1.toFixed(2)} ${yy.toFixed(2)} m ${x2.toFixed(2)} ${yy.toFixed(2)} l S`);
    const L = A4.l - 2 * MARGE;
    const reste = () => y - BAS;

    /* Bandeau de titre */
    rect(0, A4.h - 86, A4.l, 86, [31, 36, 48]);
    texte("Rapport de séance", MARGE, A4.h - 46, 22, { couleur: [255, 255, 255], gras: true });
    texte("Escape game CM1-CM2 · pour le cahier journal", MARGE, A4.h - 66, 10.5, { couleur: [214, 220, 232] });
    y = A4.h - 112;

    /* Identité de la séance */
    const champs = [["Classe", m.classe || "à compléter"], ["Date", m.dateTexte || "non datée"], ["Jeu", m.jeuTitre + (m.matiere ? " (" + m.matiere + ")" : "")],
      ["Durée de la séance", m.dureeTexte], ["Nombre d'équipes", m.nbEquipes ? `${m.nbEquipes}${m.nbInterrompues ? " dont " + m.nbInterrompues + " interrompue" + (m.nbInterrompues > 1 ? "s" : "") : ""}` : "aucune"]];
    for(const [k, v] of champs){
      texte(k, MARGE, y, 9.5, { couleur: [93, 100, 114], gras: true });
      const lignes = coupe(v, 11, L - 120).slice(0, 2);
      lignes.forEach((l, i) => texte(l, MARGE + 120, y - i * 13, 11));
      y -= 17 + (lignes.length - 1) * 13;
    }
    y -= 4;

    /* Avertissements (séance incomplète, détail absent…) */
    for(const a of m.avertissements){
      const lignes = coupe(a, 9.5, L - 20), h = lignes.length * 12 + 10;
      rect(MARGE, y - h + 8, L, h, [255, 244, 224], [214, 168, 96]);
      lignes.forEach((l, i) => texte(l, MARGE + 10, y - 6 - i * 12, 9.5, { couleur: [120, 70, 10] }));
      y -= h + 6;
    }

    /* Équipes */
    const titreBloc = t => { y -= 4; texte(t, MARGE, y, 12.5, { gras: true }); y -= 6; filet(MARGE, y, MARGE + L); y -= 14; };
    /* Place à garder sous les équipes : au moins 4 compétences, la référence au programme et le pied de page */
    const uniteComp = c => coupe(c.texte, 10, L - 24 - (c.pc != null ? 78 : 0));
    const hComp = c => uniteComp(c).length * 12 + 4;
    const hProg = m.programmes.reduce((t, p) => t + Math.min(2, coupe(p, 9.5, L).length) * 12 + 2, m.programmes.length ? 24 : 0);
    const reserveComp = 24 + m.competences.slice(0, 4).reduce((t, c) => t + hComp(c), 0) + (m.competences.length > 4 ? 14 : 0) + hProg + 12;
    titreBloc("Équipes");
    if(!m.equipes.length){ texte("Aucune équipe à afficher.", MARGE, y, 10); y -= 16; }
    else {
      const cols = [["Équipe", 0, 150], ["Niveau", 155, 60], ["Énigmes", 220, 52], ["Score", 277, 48], ["Durée", 330, 48], ["État", 383, 70]];
      cols.forEach(([t, dx]) => texte(t, MARGE + dx, y, 9, { couleur: [93, 100, 114], gras: true })); y -= 4; filet(MARGE, y, MARGE + L); y -= 12;
      const ligneH = 14;
      const place = Math.max(1, Math.floor((reste() - reserveComp) / ligneH));
      const visibles = m.equipes.length <= place ? m.equipes : m.equipes.slice(0, Math.max(1, place - 1));
      for(const e of visibles){
        const v = [e.nom, e.niveau, e.enigmes, e.score, e.duree, e.etat];
        cols.forEach(([, dx, w], i) => texte(tronque(v[i], 10, w), MARGE + dx, y, 10, e.fini || i < 5 ? {} : { couleur: [150, 80, 10], gras: true }));
        y -= ligneH;
      }
      if(visibles.length < m.equipes.length){ texte(`... et ${m.equipes.length - visibles.length} autre${m.equipes.length - visibles.length > 1 ? "s" : ""} équipe${m.equipes.length - visibles.length > 1 ? "s" : ""} (voir le tableur).`, MARGE, y, 9.5, { couleur: [93, 100, 114] }); y -= ligneH; }
    }

    /* Compétences */
    titreBloc(m.detailDispo ? "Compétences travaillées" : "Compétences prévues par le jeu");
    const pied = hProg + 12;
    if(!m.competences.length){ texte("Compétences non disponibles pour ce jeu.", MARGE, y, 10); y -= 16; }
    else {
      let affiches = 0;
      for(const c of m.competences){
        const lignes = uniteComp(c);
        const apres = m.competences.length - affiches - 1;
        const besoin = lignes.length * 12 + 4 + (apres > 0 ? 14 : 0);
        if(reste() - pied < besoin && affiches < m.competences.length){ if(affiches) break; }
        texte("-", MARGE + 4, y, 10);
        lignes.forEach((l, i) => texte(l, MARGE + 16, y - i * 12, 10));
        if(c.pc != null) texte(`${c.pc} % du 1er coup`, MARGE + L - 74, y, 9, { couleur: c.pc < 50 ? [150, 80, 10] : [21, 110, 60] });
        y -= lignes.length * 12 + 4; affiches++;
      }
      if(affiches < m.competences.length){ texte(`... et ${m.competences.length - affiches} autre${m.competences.length - affiches > 1 ? "s" : ""} compétence${m.competences.length - affiches > 1 ? "s" : ""} (voir le bilan de classe).`, MARGE, y, 9.5, { couleur: [93, 100, 114] }); y -= 14; }
    }

    /* Référence au programme (C2) */
    if(m.programmes.length){
      titreBloc("Programme de référence");
      for(const p of m.programmes){ const lignes = coupe(p, 9.5, L).slice(0, 2); lignes.forEach((l, i) => texte(l, MARGE, y - i * 12, 9.5, { couleur: [60, 66, 80] })); y -= lignes.length * 12 + 2; }
    }

    /* Pied : toujours en bas de page */
    const g = m.genere;
    const jj = `${String(g.getDate()).padStart(2, "0")}/${String(g.getMonth() + 1).padStart(2, "0")}/${g.getFullYear()}`;
    filet(MARGE, 40, MARGE + L);
    coupe(`Document généré automatiquement le ${jj} par les escape games CM1-CM2, à partir des comptes-rendus de parties. À relire avant de le joindre au cahier journal.`, 7.5, L)
      .slice(0, 2).forEach((l, i) => texte(l, MARGE, 29 - i * 10, 7.5, { couleur: [93, 100, 114] }));
    const bas = y;

    /* Assemblage du fichier */
    const flux = ops.join("\n");
    const objets = [
      "<< /Type /Catalog /Pages 2 0 R >>",
      "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
      `<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${A4.l} ${A4.h}] /Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>`,
      `<< /Length ${flux.length} >>\nstream\n${flux}\nendstream`,
      "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
      `<< /Title (${echappe(encode("Rapport de séance - " + m.jeuTitre))}) /Creator (Escape games CM1-CM2) /Producer (Escape games CM1-CM2) >>`
    ];
    let doc = "%PDF-1.4\n%\xE2\xE3\xCF\xD3\n";
    const pos = [];
    objets.forEach((o, i) => { pos.push(doc.length); doc += `${i + 1} 0 obj\n${o}\nendobj\n`; });
    const xref = doc.length;
    doc += `xref\n0 ${objets.length + 1}\n0000000000 65535 f \n` + pos.map(p => String(p).padStart(10, "0") + " 00000 n \n").join("");
    doc += `trailer\n<< /Size ${objets.length + 1} /Root 1 0 R /Info 6 0 R >>\nstartxref\n${xref}\n%%EOF\n`;
    const octets = new Uint8Array(doc.length);
    for(let i = 0; i < doc.length; i++) octets[i] = doc.charCodeAt(i) & 255;
    return { octets, bas, pages: 1, bandeBas: BAS };
  }

  const API = { seances, modele, pdf, nomFichier, dateLongue, encode, largeur, coupe, tronque, echappe, parEquipe, MARGE, BAS };
  if(typeof window !== "undefined") window.RAPPORT_SEANCE = API;
  if(typeof module !== "undefined") module.exports = API;
})();
