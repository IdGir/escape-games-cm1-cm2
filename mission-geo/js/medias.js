/* =========================================================
   MÉDIAS — cascade vidéo > image > décor dessiné
   ---------------------------------------------------------
   Chaque emplacement de média du jeu porte un « nom de base ».
   Le moteur cherche, dans l'ordre :
     1. assets/videos/<base>.mp4  (puis .webm, .m4v)
     2. assets/images/<base>.jpg  (puis .png, .webp, .gif, .jpeg)
     3. le décor dessiné (SVG) fourni par cartes.js, s'il existe
     4. sinon : l'emplacement disparaît purement et simplement.

   Aucun fichier n'est obligatoire : le jeu reste entièrement
   jouable sans déposer la moindre image.
   ========================================================= */

const MEDIAS = (function(){

  const DOSSIER_VIDEO  = "assets/videos/";
  const DOSSIER_IMAGE  = "assets/images/";
  const EXT_VIDEO = [".mp4", ".webm", ".m4v"];
  const EXT_IMAGE = [".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"];

  /* Cache des sondages deja effectues : evite de re-tester 40 fois
     le meme fichier absent au cours d'une seance. */
  const cache = new Map();

  /* Reglages, alimentes par reglages.js */
  const options = {
    videosActives: true,
    sonVideo: false,
    imagesActives: true
  };

  /* ---- Sondage d'une URL image ---- */
  function testerImage(url){
    if(cache.has(url)) return cache.get(url);
    const p = new Promise(resolve=>{
      const img = new Image();
      const fin = ok => resolve(ok ? url : null);
      img.onload  = ()=> fin(img.naturalWidth > 0);
      img.onerror = ()=> fin(false);
      img.src = url;
    });
    cache.set(url, p);
    return p;
  }

  /* ---- Sondage d'une URL video ----
     En file:// certains navigateurs refusent la lecture des videos
     locales : on laisse 3 s puis on abandonne proprement. */
  function testerVideo(url){
    if(cache.has(url)) return cache.get(url);
    const p = new Promise(resolve=>{
      const v = document.createElement("video");
      let fini = false;
      const fin = ok => { if(!fini){ fini = true; v.removeAttribute("src"); resolve(ok ? url : null); } };
      v.preload = "metadata";
      v.muted = true;
      v.addEventListener("loadedmetadata", ()=> fin(true));
      v.addEventListener("error", ()=> fin(false));
      setTimeout(()=> fin(false), 1800);
      v.src = url;
    });
    cache.set(url, p);
    return p;
  }

  /* ---- Recherche du meilleur fichier disponible ----
     Les extensions sont sondées EN PARALLÈLE (et non l'une après l'autre) :
     sur un poste sans aucun média déposé, l'attente reste imperceptible. */
  async function premier(urls, testeur){
    const resultats = await Promise.all(urls.map(u => testeur(u)));
    return resultats.find(u => u) || null;
  }

  async function chercher(base){
    if(!base) return null;
    if(options.videosActives){
      const url = await premier(EXT_VIDEO.map(e => DOSSIER_VIDEO + base + e), testerVideo);
      if(url) return { type:"video", url };
    }
    if(options.imagesActives){
      const url = await premier(EXT_IMAGE.map(e => DOSSIER_IMAGE + base + e), testerImage);
      if(url) return { type:"image", url };
    }
    return null;
  }

  /* ---- Construction du contenu d'un emplacement ---- */
  function baliseVideo(url, spec){
    const v = document.createElement("video");
    v.src = url;
    v.controls = true;
    v.playsInline = true;
    v.muted = !options.sonVideo && !spec.sonForce;
    if(spec.boucle) { v.loop = true; v.autoplay = true; v.controls = false; }
    v.preload = "metadata";
    return v;
  }

  function baliseImage(url, spec){
    const i = document.createElement("img");
    i.src = url;
    i.alt = spec.alt || spec.legende || "";
    i.loading = "lazy";
    return i;
  }

  /* ---- API principale ----
     spec : { base, legende, alt, decor, boucle, sonForce, obligatoire }
       base   : nom de fichier attendu (sans extension)
       decor  : nom d'un decor dessine de cartes.js (repli)
       legende: texte affiche en surimpression
     Retourne l'element hote (deja insere par l'appelant) pour chainage. */
  function remplir(hote, spec){
    if(!hote) return hote;
    spec = spec || {};
    hote.innerHTML = "";
    hote.hidden = true;

    const poser = (noeud, legende)=>{
      hote.innerHTML = "";
      hote.appendChild(noeud);
      if(legende){
        const l = document.createElement("div");
        l.className = "media-legende";
        l.textContent = legende;
        hote.appendChild(l);
      }
      hote.hidden = false;
    };

    /* Repli immediat sur le decor dessine, remplace ensuite si un
       fichier est trouve : l'eleve n'attend jamais devant un vide. */
    const decor = spec.decor && typeof CARTES !== "undefined" ? CARTES.decor(spec.decor) : null;
    if(decor){
      const enveloppe = document.createElement("div");
      enveloppe.className = "media-decor";
      enveloppe.innerHTML = decor;
      poser(enveloppe, spec.legende);
    }

    chercher(spec.base).then(trouve=>{
      if(!trouve) return;
      poser(trouve.type === "video" ? baliseVideo(trouve.url, spec) : baliseImage(trouve.url, spec),
            spec.legende);
    });

    return hote;
  }

  /* ---- Fabrique un emplacement pret a l'emploi ---- */
  function bloc(spec){
    const d = document.createElement("div");
    d.className = "media-slot";
    if(spec && spec.classe) d.classList.add(spec.classe);
    remplir(d, spec);
    return d;
  }

  /* ---- Diagnostic : liste ce qui est reellement detecte ----
     Utilise par l'espace enseignant (Reglages > Multimedia). */
  async function diagnostic(bases){
    const lignes = [];
    for(const base of bases){
      const t = await chercher(base);
      lignes.push({ base, trouve: t ? t.url : null, type: t ? t.type : null });
    }
    return lignes;
  }

  function configurer(nouvelles){
    Object.assign(options, nouvelles || {});
    cache.clear();
  }

  return { remplir, bloc, chercher, diagnostic, configurer, options };
})();
