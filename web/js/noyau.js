/* Noyau : appels à l'API, aides de rendu, état global. */

function _entetes(json) {
  const h = json ? { "Content-Type": "application/json" } : {};
  if (Etat.jeton) h["X-Jeton"] = Etat.jeton;   // session enseignante (si PIN actif)
  return h;
}
function _si401(r) {
  // Session expirée ou verrou actif : on repasse par l'écran de code.
  if (r.status === 401 && typeof Securite !== "undefined") Securite.reverrouiller();
  return r;
}
const API = {
  async get(url) {
    const r = _si401(await fetch(url, { headers: _entetes(false) }));
    return r.json();
  },
  async post(url, data) {
    const r = _si401(await fetch(url, {
      method: "POST", headers: _entetes(true), body: JSON.stringify(data || {})
    }));
    return r.json();
  },
  async del(url) {
    const r = _si401(await fetch(url, { method: "DELETE", headers: _entetes(false) }));
    return r.json();
  }
};

/* État partagé de l'application */
const Etat = {
  ref: null,        // référentiel (catégories, couleurs, repères, config)
  eleve: null,      // élève connecté
  espace: "prof",   // "prof" | "eleve"
  vue: null,
  jeton: null       // jeton de session enseignante (Phase I)
};

/* --- Aides DOM --- */
const $  = (s, p = document) => p.querySelector(s);
const $$ = (s, p = document) => [...p.querySelectorAll(s)];

function el(html) {
  const t = document.createElement("template");
  t.innerHTML = html.trim();
  return t.content.firstElementChild;
}

function vider(n) { while (n.firstChild) n.removeChild(n.firstChild); }

function echapper(s) {
  return (s ?? "").toString()
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

/* --- Retour visuel --- */
let minuteurToast;
function toast(message, duree = 2600) {
  const t = $("#toast");
  t.textContent = message;
  t.classList.add("on");
  clearTimeout(minuteurToast);
  minuteurToast = setTimeout(() => t.classList.remove("on"), duree);
}

function modale(html, large = false) {
  const boite = $("#modale-corps");
  boite.innerHTML = html;
  // Les fiches de leçon ont besoin de place : on élargit la fenêtre pour elles.
  boite.style.maxWidth = large ? "1000px" : "";
  $("#modale").classList.add("on");
}
function fermerModale() {
  const fenetre = $("#modale");
  fenetre.classList.remove("on", "dico-flottante");
  const boite = $("#modale-corps");
  if (boite) {
    // On remet la fenêtre à sa place : la suivante ne doit pas hériter
    // de la position où l'élève avait déplacé le dictionnaire.
    boite.style.maxWidth = "";
    boite.style.position = "";
    boite.style.left = "";
    boite.style.top = "";
    boite.style.transform = "";
    boite.style.maxHeight = "";
  }
}

document.addEventListener("click", e => {
  if (e.target.id === "modale") fermerModale();
});
document.addEventListener("keydown", e => {
  if (e.key === "Escape") fermerModale();
});

/* --- Confirmation, à la place de confirm() qui est bloquant et laid --- */
function confirmer(titre, texte, surOui, libelle = "Confirmer", danger = true) {
  modale(`
    <div class="carte-titre">${echapper(titre)}</div>
    <p style="color:var(--texte-doux);margin:8px 0 18px;line-height:1.6">
      ${texte}</p>
    <div class="rangee">
      <button class="btn doux" onclick="fermerModale()">Annuler</button>
      <button class="btn ${danger ? "rouge" : ""}" id="oui">${echapper(libelle)}</button>
    </div>`);
  $("#oui").onclick = () => { fermerModale(); surOui(); };
}

/* --- Titre de page --- */
function page(titre, sous) {
  $("#fil").textContent = titre;
  return `<div class="page-titre">${echapper(titre)}</div>
          <div class="page-sous">${echapper(sous || "")}</div>`;
}

/* --------------------------------------------------------------------------
   Visionneuse des fiches du classeur, partagée par l'élève et l'enseignant.

   Ces fiches sont dessinées au format carte A7 (7,4 cm) : affichées telles
   quelles à l'écran, elles sont illisibles. On les agrandit donc franchement
   (180 % par défaut), avec un réglage − / + mémorisé d'une fiche à l'autre.
   -------------------------------------------------------------------------- */
const Classeur = {
  // Les fiches sont dessinées en millimètres (carte de 105 × 74,2 mm) : une
  // simple mise à l'échelle du cadre ne changeait rien au texte. On agrandit
  // donc la carte elle-même avec « zoom », qui recalcule vraiment la mise en
  // page — le texte reste net et se réagence proprement.
  zoom: 2.2,
  MIN: 1.4,
  MAX: 3.6,

  async ouvrir(leconId, { impression = false } = {}) {
    const rep = await API.get(`/api/classeur/fiche/${leconId}`);
    if (!rep || rep.erreur) return;
    const titre = (rep.titre || "Fiche du classeur").replace(/^[^\p{L}]+/u, "");
    modale(`<div class="lecon-modale">
        <div class="lecon-modale-haut">
          <div>
            <div class="carte-titre">📘 ${echapper(titre)}</div>
            <div class="lecon-modale-sous">${echapper(rep.sous_domaine || "")}</div>
          </div>
          <div class="zoom-reglage">
            <span class="zoom-lib">Taille du texte</span>
            <button class="btn-zoom" id="zoom-moins" title="Réduire">−</button>
            <span class="zoom-valeur" id="zoom-valeur"></span>
            <button class="btn-zoom" id="zoom-plus" title="Agrandir">+</button>
          </div>
        </div>
        <div class="lecon-cadre">
          <iframe id="iframe-fiche" title="Fiche pédagogique"></iframe>
        </div>
        <div class="rangee" style="margin-top:14px">
          ${impression ? `<span style="font-size:12.5px;color:var(--texte-doux)">
            Astuce : cette fenêtre s'imprime aussi directement (Ctrl+P).</span>` : ""}
          <button class="btn grand pousse" onclick="fermerModale()">Fermer</button>
        </div>
      </div>`, true);

    const cadre = $("#iframe-fiche");
    const appliquer = () => {
      const z = this.zoom;
      const v = $("#zoom-valeur");
      if (v) v.textContent = Math.round(z * 100) + " %";
      if (!cadre) return;
      cadre.srcdoc = `<!DOCTYPE html><html><head><meta charset="utf-8">
        <style>${rep.css}
          html,body{background:#fff;margin:0;padding:0;}
          body{display:flex;justify-content:center;align-items:flex-start;
               padding:10px;}
          /* « zoom » agrandit réellement le contenu de la carte : les tailles
             en millimètres sont recalculées, le texte devient lisible. */
          .card{zoom:${z};border:0;margin:0;}
          .card .punch{display:none;}   /* le trou de perforation : inutile ici */
          .card::before{display:none;}  /* la marge de reliure non plus */
        </style></head><body>${rep.html}</body></html>`;
      // La carte fait 74,2 mm de haut : sa hauteur réelle à l'écran suit le
      // zoom. Le cadre s'y ajuste, donc rien n'est coupé.
      const HAUTEUR_CARTE_PX = 74.2 * 3.7795;   // millimètres → pixels
      cadre.style.height = Math.round(HAUTEUR_CARTE_PX * z + 26) + "px";
    };
    const bm = $("#zoom-moins"), bp = $("#zoom-plus");
    if (bm) bm.onclick = () => {
      this.zoom = Math.max(this.MIN, +(this.zoom - 0.2).toFixed(2)); appliquer();
    };
    if (bp) bp.onclick = () => {
      this.zoom = Math.min(this.MAX, +(this.zoom + 0.2).toFixed(2)); appliquer();
    };
    appliquer();
  }
};

/* --- Utilitaires --- */
const couleurCat = c => (Etat.ref?.couleurs || {})[c] || "var(--accent)";
const libelleCat = c => (Etat.ref?.libelles || {})[c] || c;

function duree(s) {
  const m = Math.floor(s / 60), r = Math.floor(s % 60);
  return `${m}′${String(r).padStart(2, "0")}″`;
}
