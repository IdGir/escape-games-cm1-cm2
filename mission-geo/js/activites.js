/* =========================================================
   ACTIVITÉS — moteur générique des énigmes
   ---------------------------------------------------------
   Toutes les activités du livret papier sont ramenées à
   15 types réutilisables. Chaque séance se contente de
   décrire ses activités en données ; le rendu, la
   vérification, les essais, les coups de pouce et la
   correction sont gérés ici, une fois pour toutes.
   ========================================================= */

const ACTIVITES = (function(){

  /* ---------------- Outils ---------------- */
  const $ = (tag, classe, texte) => {
    const e = document.createElement(tag);
    if(classe) e.className = classe;
    if(texte !== undefined && texte !== null) e.textContent = texte;
    return e;
  };

  function melanger(tableau){
    const t = tableau.slice();
    for(let i = t.length - 1; i > 0; i--){
      const j = Math.floor(Math.random() * (i + 1));
      [t[i], t[j]] = [t[j], t[i]];
    }
    return t;
  }

  /* Comparaison souple : accents, casse, ponctuation et espaces ignores */
  function normaliser(s){
    return String(s == null ? "" : s)
      .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "");
  }

  function nombreDe(s){
    const n = parseFloat(String(s).replace(/\s/g, "").replace(",", "."));
    return isNaN(n) ? null : n;
  }

  /* =========================================================
     Les 15 constructeurs.
     Chacun recoit (act, corps) et renvoie :
       { verifier() -> {ok, faits, total, message?}, corriger() }
     ========================================================= */
  const TYPES = {};

  /* ---------- 1. QCM (choix unique ou multiple) ---------- */
  TYPES.qcm = function(act, corps){
    const choisis = new Set();
    const liste = $("div", "qcm" + (act.disposition === "liste" ? " liste" : ""));
    const boutons = [];

    act.options.forEach((op, i) => {
      const b = $("button");
      b.type = "button";
      if(op.image || op.icone){
        const v = $("div", "vignette");
        if(op.image){ const img = $("img"); img.src = op.image; img.alt = op.texte || ""; v.appendChild(img); }
        else v.textContent = op.icone;
        b.appendChild(v);
      }
      b.appendChild($("span", null, op.texte || ""));
      b.addEventListener("click", () => {
        if(!act.multiple){ choisis.clear(); boutons.forEach(x => x.classList.remove("choisi")); }
        if(choisis.has(i)){ choisis.delete(i); b.classList.remove("choisi"); }
        else { choisis.add(i); b.classList.add("choisi"); }
      });
      boutons.push(b);
      liste.appendChild(b);
    });
    corps.appendChild(liste);

    const bons = act.options.map((o, i) => o.correct ? i : -1).filter(i => i >= 0);

    return {
      verifier(){
        const ok = choisis.size === bons.length && bons.every(i => choisis.has(i));
        boutons.forEach((b, i) => {
          b.classList.remove("bon", "mauvais");
          if(choisis.has(i)) b.classList.add(bons.includes(i) ? "bon" : "mauvais");
        });
        const justes = [...choisis].filter(i => bons.includes(i)).length;
        return { ok, faits: justes, total: bons.length };
      },
      corriger(){
        choisis.clear();
        bons.forEach(i => choisis.add(i));
        boutons.forEach((b, i) => {
          b.classList.remove("choisi", "mauvais");
          if(bons.includes(i)) b.classList.add("bon");
        });
      }
    };
  };

  /* ---------- 2. Vrai / Faux ---------- */
  TYPES.vraifaux = function(act, corps){
    const table = $("table", "vf");
    const lignes = [];
    act.items.forEach(item => {
      const tr = $("tr");
      tr.appendChild($("td", null, item.texte));
      const td = $("td");
      let valeur = null;
      const mk = (lib, val) => {
        const b = $("button", "bascule", lib);
        b.type = "button";
        b.addEventListener("click", () => {
          valeur = val;
          td.querySelectorAll(".bascule").forEach(x => x.classList.remove("choisi"));
          b.classList.add("choisi");
        });
        return b;
      };
      td.appendChild(mk("V", true));
      td.appendChild(mk("F", false));
      tr.appendChild(td);
      table.appendChild(tr);
      lignes.push({ tr, td, item, lire: () => valeur, ecrire: v => {
        valeur = v;
        td.querySelectorAll(".bascule").forEach((x, k) => x.classList.toggle("choisi", (k === 0) === v));
      }});
    });
    corps.appendChild(table);

    return {
      verifier(){
        let justes = 0;
        lignes.forEach(l => {
          const bon = l.lire() === l.item.reponse;
          l.tr.classList.remove("bon", "faux");
          if(l.lire() !== null) l.tr.classList.add(bon ? "bon" : "faux");
          if(bon) justes++;
        });
        return { ok: justes === lignes.length, faits: justes, total: lignes.length };
      },
      corriger(){
        lignes.forEach(l => { l.ecrire(l.item.reponse); l.tr.classList.remove("faux"); l.tr.classList.add("bon"); });
      }
    };
  };

  /* ---------- 3. Texte a trous ---------- */
  TYPES.trous = function(act, corps){
    const solutions = [];
    const morceaux = String(act.texte).split(/(\[\[[^\]]+\]\])/);
    let motChoisi = null;
    const banque = $("div", "banque-mots");
    const zone = $("div", "texte-trous");
    const trous = [];

    morceaux.forEach(m => {
      const cap = m.match(/^\[\[(.+)\]\]$/);
      if(cap){
        const attendu = cap[1];
        solutions.push(attendu);
        const t = $("span", "trou vide", "...........");
        t.dataset.attendu = attendu;
        t.dataset.rempli = "";
        t.addEventListener("click", () => {
          if(t.dataset.rempli){          /* on vide le trou et on rend l'etiquette */
            libererMot(t.dataset.rempli);
            t.dataset.rempli = "";
            t.textContent = "...........";
            t.classList.add("vide");
          } else if(motChoisi){
            t.dataset.rempli = motChoisi;
            t.textContent = motChoisi;
            t.classList.remove("vide");
            occuperMot(motChoisi);
            motChoisi = null;
            banque.querySelectorAll(".mot-etiquette").forEach(x => x.classList.remove("selectionne"));
          }
        });
        trous.push(t);
        zone.appendChild(t);
      } else if(m){
        zone.appendChild(document.createTextNode(m));
      }
    });

    const mots = melanger(solutions.concat(act.intrus || []));
    const etiquettes = [];
    mots.forEach(mot => {
      const b = $("button", "mot-etiquette", mot);
      b.type = "button";
      b.addEventListener("click", () => {
        if(b.classList.contains("utilise")) return;
        motChoisi = (motChoisi === mot && b.classList.contains("selectionne")) ? null : mot;
        banque.querySelectorAll(".mot-etiquette").forEach(x => x.classList.remove("selectionne"));
        if(motChoisi) b.classList.add("selectionne");
      });
      etiquettes.push(b);
      banque.appendChild(b);
    });

    function occuperMot(mot){
      const libre = etiquettes.find(e => e.textContent === mot && !e.classList.contains("utilise"));
      if(libre) libre.classList.add("utilise");
    }
    function libererMot(mot){
      const pris = etiquettes.find(e => e.textContent === mot && e.classList.contains("utilise"));
      if(pris) pris.classList.remove("utilise");
    }

    corps.appendChild(banque);
    corps.appendChild(zone);

    return {
      verifier(){
        let justes = 0;
        trous.forEach(t => {
          const bon = normaliser(t.dataset.rempli) === normaliser(t.dataset.attendu);
          t.classList.remove("bon", "faux");
          if(t.dataset.rempli) t.classList.add(bon ? "bon" : "faux");
          if(bon) justes++;
        });
        return { ok: justes === trous.length, faits: justes, total: trous.length };
      },
      corriger(){
        trous.forEach(t => {
          t.dataset.rempli = t.dataset.attendu;
          t.textContent = t.dataset.attendu;
          t.classList.remove("vide", "faux");
          t.classList.add("bon");
        });
        etiquettes.forEach(e => e.classList.add("utilise"));
      }
    };
  };

  /* ---------- 4. Relier deux colonnes ---------- */
  TYPES.relier = function(act, corps){
    const grille = $("div", "relier");
    const colG = $("div", "colonne"), colD = $("div", "colonne");
    const milieu = $("div", "lien-milieu", "relie");
    let selection = null;
    const liens = new Map();           /* idGauche -> idDroite */
    const btnG = new Map(), btnD = new Map();

    const lettres = "ABCDEFGHIJ";
    const faireBouton = (item, cote) => {
      const b = $("button");
      b.type = "button";
      const p = $("span", "pastille", "");
      b.appendChild(p);
      if(item.image){ const i = $("img"); i.src = item.image; i.alt = ""; b.appendChild(i); }
      b.appendChild($("span", null, item.texte));
      b.dataset.id = item.id;
      b.dataset.cote = cote;
      b.addEventListener("click", () => {
        if(cote === "g"){
          if(liens.has(item.id)){ delier(item.id); return; }
          selection = selection === item.id ? null : item.id;
          rafraichir();
        } else {
          if(!selection){
            const dejaG = [...liens.entries()].find(([, d]) => d === item.id);
            if(dejaG) delier(dejaG[0]);
            return;
          }
          for(const [g, d] of liens) if(d === item.id) liens.delete(g);
          liens.set(selection, item.id);
          selection = null;
          rafraichir();
        }
      });
      return b;
    };

    function delier(idG){ liens.delete(idG); rafraichir(); }

    function rafraichir(){
      let n = 0;
      const marques = new Map();
      for(const [g, d] of liens){ marques.set(g, lettres[n]); marques.set("d:" + d, lettres[n]); n++; }
      btnG.forEach((b, id) => {
        b.classList.toggle("selectionne", selection === id);
        b.classList.toggle("appariee", liens.has(id));
        b.querySelector(".pastille").textContent = marques.get(id) || "";
      });
      btnD.forEach((b, id) => {
        const m = marques.get("d:" + id);
        b.classList.toggle("appariee", !!m);
        b.querySelector(".pastille").textContent = m || "";
      });
    }

    act.gauche.forEach(it => { const b = faireBouton(it, "g"); btnG.set(it.id, b); colG.appendChild(b); });
    melanger(act.droite).forEach(it => { const b = faireBouton(it, "d"); btnD.set(it.id, b); colD.appendChild(b); });
    grille.appendChild(colG); grille.appendChild(milieu); grille.appendChild(colD);
    corps.appendChild(grille);

    const attendu = new Map(act.paires);

    return {
      verifier(){
        let justes = 0;
        btnG.forEach((b, id) => {
          b.classList.remove("bon", "faux");
          if(liens.has(id)){
            const bon = liens.get(id) === attendu.get(id);
            b.classList.add(bon ? "bon" : "faux");
            if(bon) justes++;
          }
        });
        return { ok: justes === attendu.size, faits: justes, total: attendu.size };
      },
      corriger(){
        liens.clear();
        attendu.forEach((d, g) => liens.set(g, d));
        rafraichir();
        btnG.forEach(b => { b.classList.remove("faux"); b.classList.add("bon"); });
      }
    };
  };

  /* ---------- 5. Remise en ordre ---------- */
  TYPES.ordre = function(act, corps){
    const zone = $("div", "ordre");
    let items = melanger(act.items);
    /* on evite le hasard qui donnerait la solution d'emblee */
    if(items.every((it, i) => it.id === act.ordre[i]) && items.length > 1) items = items.reverse();

    function dessiner(){
      zone.innerHTML = "";
      items.forEach((it, i) => {
        const l = $("div", "element");
        l.appendChild($("span", "rang"));
        if(it.image){ const img = $("img"); img.src = it.image; img.alt = ""; l.appendChild(img); }
        l.appendChild($("span", "libelle", it.texte));
        const f = $("div", "fleches");
        const haut = $("button", null, "▲"), bas = $("button", null, "▼");
        haut.type = bas.type = "button";
        haut.disabled = i === 0; bas.disabled = i === items.length - 1;
        haut.addEventListener("click", () => { [items[i-1], items[i]] = [items[i], items[i-1]]; dessiner(); });
        bas .addEventListener("click", () => { [items[i+1], items[i]] = [items[i], items[i+1]]; dessiner(); });
        f.appendChild(haut); f.appendChild(bas);
        l.appendChild(f);
        l.dataset.id = it.id;
        zone.appendChild(l);
      });
    }
    dessiner();
    corps.appendChild(zone);

    return {
      verifier(){
        let justes = 0;
        [...zone.children].forEach((l, i) => {
          const bon = l.dataset.id === act.ordre[i];
          l.classList.remove("bon", "faux");
          l.classList.add(bon ? "bon" : "faux");
          if(bon) justes++;
        });
        return { ok: justes === act.ordre.length, faits: justes, total: act.ordre.length };
      },
      corriger(){
        items = act.ordre.map(id => act.items.find(x => x.id === id));
        dessiner();
        [...zone.children].forEach(l => l.classList.add("bon"));
      }
    };
  };

  /* ---------- 6. Etiquettes a placer sur une carte ---------- */
  TYPES.etiquettes = function(act, corps){
    const fond = $("div", "carte-zone");
    if(act.fond && act.fond.decor && typeof CARTES !== "undefined"){
      const svg = CARTES.decor(act.fond.decor);
      if(svg) fond.innerHTML = svg;
    }
    if(act.fond && act.fond.base && typeof MEDIAS !== "undefined"){
      /* une vraie carte deposee par l'enseignant remplace le dessin */
      MEDIAS.chercher(act.fond.base).then(t => {
        if(t && t.type === "image"){
          const img = $("img"); img.src = t.url; img.alt = act.fond.alt || "";
          fond.insertBefore(img, fond.firstChild);
          if(fond.querySelector("svg")) fond.querySelector("svg").remove();
        }
      });
    }

    let etiquetteChoisie = null;
    const bac = $("div", "banque-mots");
    const zones = [];

    act.zones.forEach(z => {
      const d = $("div", "zone-depot vide", z.vide || "?");
      d.style.left = z.x + "%";
      d.style.top  = z.y + "%";
      d.dataset.attendu = z.etiquette;
      d.dataset.rempli = "";
      d.title = z.aide || "";
      d.addEventListener("click", () => {
        if(d.dataset.rempli){
          rendre(d.dataset.rempli);
          d.dataset.rempli = ""; d.textContent = z.vide || "?"; d.classList.add("vide");
        } else if(etiquetteChoisie){
          d.dataset.rempli = etiquetteChoisie;
          d.textContent = etiquetteChoisie;
          d.classList.remove("vide");
          prendre(etiquetteChoisie);
          etiquetteChoisie = null;
          bac.querySelectorAll(".mot-etiquette").forEach(x => x.classList.remove("selectionne"));
        }
      });
      zones.push(d);
      fond.appendChild(d);
    });

    const boutons = [];
    melanger(act.zones.map(z => z.etiquette).concat(act.intrus || [])).forEach(txt => {
      const b = $("button", "mot-etiquette", txt);
      b.type = "button";
      b.addEventListener("click", () => {
        if(b.classList.contains("utilise")) return;
        etiquetteChoisie = b.classList.contains("selectionne") ? null : txt;
        bac.querySelectorAll(".mot-etiquette").forEach(x => x.classList.remove("selectionne"));
        if(etiquetteChoisie) b.classList.add("selectionne");
      });
      boutons.push(b);
      bac.appendChild(b);
    });
    const prendre = t => { const b = boutons.find(x => x.textContent === t && !x.classList.contains("utilise")); if(b) b.classList.add("utilise"); };
    const rendre  = t => { const b = boutons.find(x => x.textContent === t &&  x.classList.contains("utilise")); if(b) b.classList.remove("utilise"); };

    corps.appendChild(bac);
    corps.appendChild(fond);

    return {
      verifier(){
        let justes = 0;
        zones.forEach(z => {
          const bon = normaliser(z.dataset.rempli) === normaliser(z.dataset.attendu);
          z.classList.remove("bon", "faux");
          if(z.dataset.rempli) z.classList.add(bon ? "bon" : "faux");
          if(bon) justes++;
        });
        return { ok: justes === zones.length, faits: justes, total: zones.length };
      },
      corriger(){
        zones.forEach(z => {
          z.dataset.rempli = z.dataset.attendu;
          z.textContent = z.dataset.attendu;
          z.classList.remove("vide", "faux"); z.classList.add("bon");
        });
        boutons.forEach(b => b.classList.add("utilise"));
      }
    };
  };

  /* ---------- 7. Tri en paniers ---------- */
  TYPES.tri = function(act, corps){
    let jetonChoisi = null;
    const reserve = $("div", "reserve-jetons");
    const rangee = $("div", "paniers");
    const place = new Map();     /* idItem -> idPanier ("" = reserve) */

    const jetons = new Map();
    melanger(act.items).forEach(it => {
      const b = $("button", "jeton-tri");
      b.type = "button";
      if(it.image){ const i = $("img"); i.src = it.image; i.alt = ""; b.appendChild(i); }
      if(it.icone) b.appendChild($("span", null, it.icone));
      b.appendChild($("span", null, it.texte));
      b.addEventListener("click", () => {
        if(place.get(it.id)){       /* deja dans un panier : on le reprend */
          place.set(it.id, "");
          reserve.appendChild(b);
          jetonChoisi = null;
        } else {
          jetonChoisi = jetonChoisi === it.id ? null : it.id;
        }
        rafraichir();
      });
      jetons.set(it.id, b);
      place.set(it.id, "");
      reserve.appendChild(b);
    });

    act.paniers.forEach(p => {
      const bloc = $("div", "panier");
      bloc.appendChild($("h4", null, p.titre));
      const dedans = $("div", "contenu");
      bloc.dataset.id = p.id;
      bloc.addEventListener("click", () => {
        if(!jetonChoisi) return;
        place.set(jetonChoisi, p.id);
        dedans.appendChild(jetons.get(jetonChoisi));
        jetonChoisi = null;
        rafraichir();
      });
      bloc.appendChild(dedans);
      rangee.appendChild(bloc);
    });

    function rafraichir(){
      jetons.forEach((b, id) => b.classList.toggle("selectionne", jetonChoisi === id));
    }

    corps.appendChild(reserve);
    corps.appendChild(rangee);

    return {
      verifier(){
        let justes = 0;
        act.items.forEach(it => {
          const b = jetons.get(it.id);
          b.classList.remove("bon", "faux");
          const p = place.get(it.id);
          if(p){ const bon = p === it.panier; b.classList.add(bon ? "bon" : "faux"); if(bon) justes++; }
        });
        return { ok: justes === act.items.length, faits: justes, total: act.items.length };
      },
      corriger(){
        act.items.forEach(it => {
          const b = jetons.get(it.id);
          const cible = rangee.querySelector('[data-id="' + it.panier + '"] .contenu');
          if(cible) cible.appendChild(b);
          place.set(it.id, it.panier);
          b.classList.remove("faux"); b.classList.add("bon");
        });
      }
    };
  };

  /* ---------- 8. Mots croises ---------- */
  TYPES.motscroises = function(act, corps){
    const bloc = $("div", "mots-croises");
    const grille = $("div", "grille-mc");
    const cases = new Map();     /* "x,y" -> input */
    const attendu = new Map();

    act.mots.forEach(m => {
      const lettres = m.mot.toUpperCase().split("");
      lettres.forEach((L, k) => {
        const x = m.dir === "h" ? m.x + k : m.x;
        const y = m.dir === "h" ? m.y : m.y + k;
        attendu.set(x + "," + y, L);
      });
    });

    const largeur = act.grille.largeur, hauteur = act.grille.hauteur;
    grille.style.gridTemplateColumns = "repeat(" + largeur + ", 1.85rem)";
    for(let y = 0; y < hauteur; y++){
      for(let x = 0; x < largeur; x++){
        const cle = x + "," + y;
        const c = $("div", "case");
        if(attendu.has(cle)){
          c.classList.add("jouable");
          const debut = act.mots.find(m => m.x === x && m.y === y);
          if(debut) c.appendChild($("span", "num", String(debut.num)));
          const i = document.createElement("input");
          i.maxLength = 1;
          i.dataset.cle = cle;
          i.addEventListener("input", () => {
            i.value = i.value.toUpperCase().slice(0, 1);
            if(i.value){
              const suivant = [...cases.values()].find(o => o.tabIndex === i.tabIndex + 1);
              if(suivant) suivant.focus();
            }
          });
          cases.set(cle, i);
          c.appendChild(i);
        }
        grille.appendChild(c);
      }
    }
    let n = 0;
    cases.forEach(i => { i.tabIndex = ++n; });

    const defs = $("div", "definitions");
    ["h", "v"].forEach(dir => {
      const liste = act.mots.filter(m => m.dir === dir);
      if(!liste.length) return;
      defs.appendChild($("h4", null, dir === "h" ? "Horizontalement" : "Verticalement"));
      const ol = $("ul");
      ol.style.listStyle = "none"; ol.style.paddingLeft = "0";
      liste.sort((a, b) => a.num - b.num).forEach(m => {
        ol.appendChild($("li", null, m.num + ". " + m.definition));
      });
      defs.appendChild(ol);
    });

    bloc.appendChild(grille); bloc.appendChild(defs);
    const env = $("div", "enveloppe-tableau"); env.appendChild(bloc);
    corps.appendChild(env);

    return {
      verifier(){
        let justes = 0;
        cases.forEach((i, cle) => {
          const bon = normaliser(i.value) === normaliser(attendu.get(cle));
          i.parentElement.classList.remove("bon", "faux");
          if(i.value) i.parentElement.classList.add(bon ? "bon" : "faux");
          if(bon) justes++;
        });
        return { ok: justes === cases.size, faits: justes, total: cases.size };
      },
      corriger(){
        cases.forEach((i, cle) => {
          i.value = attendu.get(cle);
          i.parentElement.classList.remove("faux"); i.parentElement.classList.add("bon");
        });
      }
    };
  };

  /* ---------- 9. Mots meles ---------- */
  TYPES.motsmeles = function(act, corps){
    const lignes = act.grille.map(l => Array.isArray(l) ? l : l.split(""));
    const H = lignes.length, L = lignes[0].length;
    const grille = $("div", "grille-mm");
    grille.style.gridTemplateColumns = "repeat(" + L + ", 2rem)";
    const cellules = [];
    let depart = null;
    const trouves = new Set();

    for(let y = 0; y < H; y++){
      for(let x = 0; x < L; x++){
        const c = $("div", "lettre", lignes[y][x]);
        c.dataset.x = x; c.dataset.y = y;
        c.addEventListener("click", () => {
          if(!depart){ depart = {x, y}; c.classList.add("selection"); return; }
          const mot = lireSegment(depart, {x, y});
          nettoyerSelection();
          if(mot){
            const cible = act.mots.find(m =>
              normaliser(m) === normaliser(mot) || normaliser(m) === normaliser([...mot].reverse().join("")));
            if(cible && !trouves.has(cible)){
              trouves.add(cible);
              marquerSegment(depart, {x, y});
              majListe();
            }
          }
          depart = null;
        });
        cellules.push(c);
        grille.appendChild(c);
      }
    }
    function cellule(x, y){ return cellules[y * L + x]; }
    function nettoyerSelection(){ cellules.forEach(c => c.classList.remove("selection")); }

    function segment(a, b){
      const dx = Math.sign(b.x - a.x), dy = Math.sign(b.y - a.y);
      const n = Math.max(Math.abs(b.x - a.x), Math.abs(b.y - a.y));
      if(!(dx === 0 || dy === 0 || Math.abs(b.x - a.x) === Math.abs(b.y - a.y))) return null;
      const out = [];
      for(let k = 0; k <= n; k++) out.push({x: a.x + dx * k, y: a.y + dy * k});
      return out;
    }
    function lireSegment(a, b){
      const s = segment(a, b);
      return s ? s.map(p => lignes[p.y][p.x]).join("") : null;
    }
    function marquerSegment(a, b){
      (segment(a, b) || []).forEach(p => cellule(p.x, p.y).classList.add("trouve"));
    }

    const liste = $("div", "liste-a-trouver");
    function majListe(){
      liste.innerHTML = "";
      act.mots.forEach(m => {
        const s = $("span", trouves.has(m) ? "trouve" : "", act.masquer ? "•".repeat(m.length) : m);
        liste.appendChild(s);
      });
    }
    majListe();

    corps.appendChild($("p", "aide-calcul", "Clique sur la première lettre du mot, puis sur la dernière."));
    const env = $("div", "enveloppe-tableau"); env.appendChild(grille); corps.appendChild(env);
    corps.appendChild(liste);

    return {
      verifier(){
        return { ok: trouves.size === act.mots.length, faits: trouves.size, total: act.mots.length };
      },
      corriger(){
        act.mots.forEach(m => trouves.add(m));
        /* recherche automatique de chaque mot dans les 8 directions */
        const dirs = [[1,0],[0,1],[1,1],[1,-1],[-1,0],[0,-1],[-1,-1],[-1,1]];
        act.mots.forEach(mot => {
          const M = normaliser(mot);
          for(let y = 0; y < H; y++) for(let x = 0; x < L; x++) for(const [dx, dy] of dirs){
            let s = "";
            const pts = [];
            for(let k = 0; k < M.length; k++){
              const px = x + dx * k, py = y + dy * k;
              if(px < 0 || py < 0 || px >= L || py >= H) { s = ""; break; }
              s += lignes[py][px]; pts.push({x: px, y: py});
            }
            if(normaliser(s) === M){ pts.forEach(p => cellule(p.x, p.y).classList.add("trouve")); return; }
          }
        });
        majListe();
      }
    };
  };

  /* ---------- 10. Anagramme ---------- */
  TYPES.anagramme = function(act, corps){
    const bloc = $("div", "anagramme");
    const rangee = $("div", "lettres");
    const rep = $("div", "reponse");
    let construit = [];

    const lettres = melanger(act.lettres.toUpperCase().split(""));
    const boutons = lettres.map((L, i) => {
      const b = $("button", null, L);
      b.type = "button";
      b.addEventListener("click", () => {
        if(b.classList.contains("utilisee")) return;
        b.classList.add("utilisee");
        construit.push({L, b});
        dessiner();
      });
      rangee.appendChild(b);
      return b;
    });

    function dessiner(){
      rep.innerHTML = "";
      construit.forEach((c, i) => {
        const s = $("span", null, c.L);
        s.addEventListener("click", () => { c.b.classList.remove("utilisee"); construit.splice(i, 1); dessiner(); });
        rep.appendChild(s);
      });
      if(!construit.length) rep.appendChild($("span", null, "?"));
    }
    dessiner();

    bloc.appendChild(rangee);
    bloc.appendChild(rep);
    if(act.aideLettres) bloc.appendChild($("p", "aide-calcul", act.aideLettres));
    corps.appendChild(bloc);

    return {
      verifier(){
        const mot = construit.map(c => c.L).join("");
        const ok = normaliser(mot) === normaliser(act.solution);
        rep.querySelectorAll("span").forEach(s => s.style.borderColor = ok ? "var(--vert)" : "var(--rouge)");
        return { ok, faits: ok ? 1 : 0, total: 1 };
      },
      corriger(){
        construit = [];
        boutons.forEach(b => b.classList.remove("utilisee"));
        act.solution.toUpperCase().split("").forEach(L => {
          const b = boutons.find(x => x.textContent === L && !x.classList.contains("utilisee"));
          if(b){ b.classList.add("utilisee"); construit.push({L, b}); }
        });
        dessiner();
        rep.querySelectorAll("span").forEach(s => s.style.borderColor = "var(--vert)");
      }
    };
  };

  /* ---------- 11. Saisies (nombres, mots) ---------- */
  TYPES.saisie = function(act, corps){
    if(act.tableau){
      const env = $("div", "enveloppe-tableau");
      env.innerHTML = act.tableau;
      corps.appendChild(env);
    }
    const zone = $("div", "saisies");
    const champs = act.champs.map(c => {
      const l = $("div", "ligne");
      const lab = $("label", null, c.label);
      const inp = document.createElement("input");
      inp.type = "text";
      inp.inputMode = c.texte ? "text" : "numeric";
      inp.placeholder = c.exemple || "";
      lab.setAttribute("for", "");
      l.appendChild(lab);
      l.appendChild(inp);
      if(c.unite) l.appendChild($("span", "unite", c.unite));
      zone.appendChild(l);
      return { c, l, inp };
    });
    corps.appendChild(zone);
    if(act.aide) corps.appendChild($("p", "aide-calcul", act.aide));

    return {
      verifier(){
        let justes = 0;
        champs.forEach(({c, l, inp}) => {
          let bon;
          if(c.texte){
            const acceptes = [c.solution].concat(c.variantes || []);
            bon = acceptes.some(a => normaliser(a) === normaliser(inp.value));
          } else {
            const v = nombreDe(inp.value), att = nombreDe(c.solution);
            bon = v !== null && att !== null && Math.abs(v - att) <= (c.tolerance || 0);
          }
          l.classList.remove("bon", "faux");
          if(inp.value.trim()) l.classList.add(bon ? "bon" : "faux");
          if(bon) justes++;
        });
        return { ok: justes === champs.length, faits: justes, total: champs.length };
      },
      corriger(){
        champs.forEach(({c, l, inp}) => {
          inp.value = c.solution;
          l.classList.remove("faux"); l.classList.add("bon");
        });
      }
    };
  };

  /* ---------- 12. Repartition (10 gouttes, budget de courses...) ---------- */
  TYPES.repartition = function(act, corps){
    const total = act.total;
    const valeurs = new Map(act.categories.map(c => [c.id, 0]));
    const rangee = $("div", "repartition");
    const reste = $("p", "reste-a-placer");

    act.categories.forEach(cat => {
      const p = $("div", "poste");
      p.appendChild($("h4", null, cat.titre));
      if(cat.description) p.appendChild($("p", "aide-calcul", cat.description));
      const compteur = $("div", "compteur", "0");
      const b = $("div", "boutons");
      const moins = $("button", null, "−"), plus = $("button", null, "+");
      moins.type = plus.type = "button";
      moins.addEventListener("click", () => { if(valeurs.get(cat.id) > 0){ valeurs.set(cat.id, valeurs.get(cat.id) - 1); maj(); } });
      plus .addEventListener("click", () => { if(somme() < total){ valeurs.set(cat.id, valeurs.get(cat.id) + 1); maj(); } });
      b.appendChild(moins); b.appendChild(plus);
      p.appendChild(compteur); p.appendChild(b);
      p.dataset.id = cat.id;
      p._compteur = compteur;
      rangee.appendChild(p);
    });

    const somme = () => [...valeurs.values()].reduce((a, b) => a + b, 0);
    function maj(){
      [...rangee.children].forEach(p => { p._compteur.textContent = valeurs.get(p.dataset.id); });
      const r = total - somme();
      reste.textContent = r === 0
        ? "Tout est réparti : " + total + " sur " + total + "."
        : "Il reste " + r + " " + (act.unite || "jeton(s)") + " à placer.";
      reste.classList.toggle("ok", r === 0);
    }

    corps.appendChild(rangee);
    corps.appendChild(reste);
    maj();

    return {
      verifier(){
        const complet = somme() === total;
        if(!complet) return { ok:false, faits:somme(), total, message:"Place d'abord tous les " + (act.unite || "jetons") + "." };
        if(act.solution){
          let justes = 0;
          act.categories.forEach(c => { if(valeurs.get(c.id) === act.solution[c.id]) justes++; });
          return { ok: justes === act.categories.length, faits: justes, total: act.categories.length };
        }
        /* pas de bonne reponse : le partage se justifie a l'oral */
        return { ok:true, faits:1, total:1, ouverte:true,
                 reponse: Object.fromEntries(valeurs) };
      },
      corriger(){
        if(act.solution){
          act.categories.forEach(c => valeurs.set(c.id, act.solution[c.id] || 0));
          maj();
        }
      }
    };
  };

  /* ---------- 13. Tableau a completer (listes deroulantes) ---------- */
  TYPES.tableau = function(act, corps){
    const env = $("div", "enveloppe-tableau");
    const t = $("table", "a-completer");
    const thead = $("thead"), trh = $("tr");
    trh.appendChild($("th", null, act.entete || ""));
    act.colonnes.forEach(c => trh.appendChild($("th", null, c.titre)));
    thead.appendChild(trh); t.appendChild(thead);

    const tbody = $("tbody");
    const cellules = [];
    act.lignes.forEach(ligne => {
      const tr = $("tr");
      tr.appendChild($("th", null, ligne.titre));
      act.colonnes.forEach((col, j) => {
        const td = $("td");
        const s = document.createElement("select");
        s.appendChild(new Option("—", ""));
        (col.options || []).forEach(o => s.appendChild(new Option(o, o)));
        td.appendChild(s);
        tr.appendChild(td);
        cellules.push({ td, s, attendu: ligne.solutions[j] });
      });
      tbody.appendChild(tr);
    });
    t.appendChild(tbody);
    env.appendChild(t);
    corps.appendChild(env);

    return {
      verifier(){
        let justes = 0;
        cellules.forEach(c => {
          const bon = normaliser(c.s.value) === normaliser(c.attendu);
          c.td.classList.remove("bon", "faux");
          if(c.s.value) c.td.classList.add(bon ? "bon" : "faux");
          if(bon) justes++;
        });
        return { ok: justes === cellules.length, faits: justes, total: cellules.length };
      },
      corriger(){
        cellules.forEach(c => {
          c.s.value = c.attendu;
          c.td.classList.remove("faux"); c.td.classList.add("bon");
        });
      }
    };
  };

  /* ---------- 14. Diagramme circulaire a legender ---------- */
  TYPES.diagramme = function(act, corps){
    const bloc = $("div", "diagramme");
    const couleurs = ["#2f8fd8", "#2e9e5b", "#e8b21f", "#cf3b30", "#8a6f45", "#7b5ea7"];
    const NS = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(NS, "svg");
    svg.setAttribute("viewBox", "0 0 200 200");

    let angle = -Math.PI / 2;
    act.secteurs.forEach((s, i) => {
      const part = s.pourcentage / 100 * Math.PI * 2;
      const x1 = 100 + 92 * Math.cos(angle), y1 = 100 + 92 * Math.sin(angle);
      const x2 = 100 + 92 * Math.cos(angle + part), y2 = 100 + 92 * Math.sin(angle + part);
      const grand = part > Math.PI ? 1 : 0;
      const p = document.createElementNS(NS, "path");
      p.setAttribute("d", "M100,100 L" + x1.toFixed(1) + "," + y1.toFixed(1) +
        " A92,92 0 " + grand + ",1 " + x2.toFixed(1) + "," + y2.toFixed(1) + " Z");
      p.setAttribute("fill", couleurs[i % couleurs.length]);
      p.setAttribute("class", "secteur");
      svg.appendChild(p);
      const milieu = angle + part / 2;
      const tx = 100 + 58 * Math.cos(milieu), ty = 100 + 58 * Math.sin(milieu);
      const txt = document.createElementNS(NS, "text");
      txt.setAttribute("x", tx.toFixed(1)); txt.setAttribute("y", ty.toFixed(1));
      txt.setAttribute("text-anchor", "middle"); txt.setAttribute("font-size", "13");
      txt.setAttribute("font-weight", "700"); txt.setAttribute("fill", "#fff");
      txt.textContent = s.pourcentage + "%";
      svg.appendChild(txt);
      angle += part;
    });

    const legende = $("div", "legende-diagramme");
    const selects = [];
    act.secteurs.forEach((s, i) => {
      const l = $("div", "ligne");
      const pastille = $("span", "pastille");
      pastille.style.background = couleurs[i % couleurs.length];
      const sel = document.createElement("select");
      sel.appendChild(new Option("— choisis l'usage —", ""));
      melanger(act.secteurs.map(x => x.label).concat(act.intrus || [])).forEach(o => sel.appendChild(new Option(o, o)));
      l.appendChild(pastille);
      l.appendChild($("span", null, s.pourcentage + " %"));
      l.appendChild(sel);
      legende.appendChild(l);
      selects.push({ sel, attendu: s.label, ligne: l });
    });

    bloc.appendChild(svg); bloc.appendChild(legende);
    corps.appendChild(bloc);

    return {
      verifier(){
        let justes = 0;
        selects.forEach(s => {
          const bon = normaliser(s.sel.value) === normaliser(s.attendu);
          s.ligne.style.background = s.sel.value ? (bon ? "var(--vert-pale)" : "var(--rouge-pale)") : "";
          if(bon) justes++;
        });
        return { ok: justes === selects.length, faits: justes, total: selects.length };
      },
      corriger(){
        selects.forEach(s => { s.sel.value = s.attendu; s.ligne.style.background = "var(--vert-pale)"; });
      }
    };
  };

  /* ---------- 15. Reponse ouverte (debat, oral, ecrit) ---------- */
  TYPES.ouverte = function(act, corps){
    const bloc = $("div", "ouverte");
    const ta = document.createElement("textarea");
    ta.placeholder = act.exemple || "Écris ici ta réponse, ou réponds à l'oral avec ton groupe.";
    bloc.appendChild(ta);
    if(act.pistes && act.pistes.length){
      const p = $("div", "pistes");
      p.appendChild($("b", null, "Pistes attendues (pour l'enseignant) :"));
      const ul = $("ul");
      act.pistes.forEach(x => ul.appendChild($("li", null, x)));
      p.appendChild(ul);
      p.hidden = true;
      const b = $("button", "bouton-second", "Afficher les pistes");
      b.type = "button";
      b.addEventListener("click", () => { p.hidden = !p.hidden; b.textContent = p.hidden ? "Afficher les pistes" : "Masquer les pistes"; });
      bloc.appendChild(b);
      bloc.appendChild(p);
    }
    corps.appendChild(bloc);

    return {
      verifier(){
        const rempli = ta.value.trim().length >= (act.minimum || 0);
        return rempli
          ? { ok:true, faits:1, total:1, ouverte:true, reponse: ta.value.trim() }
          : { ok:false, faits:0, total:1, message:"Écris au moins une phrase (ou coche avec l'enseignant que la réponse a été donnée à l'oral)." };
      },
      corriger(){ if(!ta.value.trim()) ta.value = "(réponse donnée à l'oral)"; }
    };
  };

  /* =========================================================
     Enveloppe commune : consigne, media, essais, correction
     ========================================================= */
  function rendre(act, hote, options){
    options = options || {};
    const section = $("section", "activite");
    section.dataset.type = act.type;

    section.appendChild($("p", "consigne", act.consigne));
    if(act.precision) section.appendChild($("p", "precision", act.precision));
    if(act.document){
      const d = $("div", "encadre");
      d.innerHTML = act.document;
      section.appendChild(d);
    }
    if(act.media && typeof MEDIAS !== "undefined") section.appendChild(MEDIAS.bloc(act.media));

    const corps = $("div", "corps");
    section.appendChild(corps);

    const constructeur = TYPES[act.type];
    if(!constructeur){
      corps.appendChild($("p", "avertissement", "Type d'activité inconnu : " + act.type));
      hote.appendChild(section);
      return { section, resultat:{ reussi:false } };
    }
    const moteur = constructeur(act, corps);

    const barre = $("div", "barre-actions");
    const bVerifier = $("button", "bouton-principal", "Vérifier");
    const bAide     = $("button", "bouton-second", "Coup de pouce");
    const bCorriger = $("button", "bouton-second", "Voir la correction");
    const compteur  = $("span", "essais", "");
    bVerifier.type = bAide.type = bCorriger.type = "button";
    bCorriger.hidden = true;
    if(!act.aide) bAide.hidden = true;
    barre.appendChild(bVerifier); barre.appendChild(bAide); barre.appendChild(bCorriger); barre.appendChild(compteur);
    section.appendChild(barre);

    const retour = $("div", "retour");
    retour.hidden = true;
    section.appendChild(retour);

    const pointsMax = act.points || 3;
    let essais = 0, termine = false, aideUtilisee = false;

    function afficher(classe, texte){
      retour.className = "retour " + classe;
      retour.textContent = texte;
      retour.hidden = false;
    }

    function conclure(reussi, points, detail){
      termine = true;
      section.classList.add("validee");
      bVerifier.disabled = true;
      bCorriger.hidden = true;
      corps.querySelectorAll("button, input, select, textarea").forEach(e => {
        if(!e.closest(".pistes")) e.disabled = true;
      });
      if(options.onFini) options.onFini({ reussi, points, essais, aideUtilisee, detail: detail || null });
    }

    bVerifier.addEventListener("click", () => {
      if(termine) return;
      essais++;
      const r = moteur.verifier();
      if(r.ok){
        const malus = Math.min(essais - 1, 2) + (aideUtilisee ? 1 : 0);
        const points = Math.max(1, pointsMax - malus);
        afficher("bon", (r.ouverte
          ? "Réponse enregistrée. Vous en discuterez ensemble."
          : "Bravo, tout est juste !") + "  (+" + points + " point" + (points > 1 ? "s" : "") + ")");
        conclure(true, points, r.reponse);
      } else {
        const detail = r.message ||
          ("Il y a " + (r.total - r.faits) + " erreur(s) sur " + r.total + ". Corrige et réessaie.");
        afficher("faux", detail);
        compteur.textContent = "Essai " + essais;
        if(essais >= 3) bCorriger.hidden = false;
      }
    });

    bAide.addEventListener("click", () => {
      aideUtilisee = true;
      afficher("bon", "💡 " + act.aide);
      bAide.disabled = true;
    });

    bCorriger.addEventListener("click", () => {
      moteur.corriger();
      afficher("bon", "Voici la correction. Relis-la avec attention : elle compte pour la suite de l'enquête.");
      conclure(false, 0);
    });

    hote.appendChild(section);
    return { section, moteur };
  }

  return { rendre, melanger, normaliser, types: Object.keys(TYPES) };
})();
