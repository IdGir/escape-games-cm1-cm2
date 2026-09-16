/* Coquille de l'application : barre latérale, navigation, thème. */

/* Menu volontairement court : 6 entrées.
   « Pilotage fin » est un bouton du tableau de bord, « Fiche élève » s'ouvre
   depuis la synthèse par élève, et tout le paramétrage tient dans « Paramètres ». */
const NAV_PROF = [
  ["bord",       "📊", "Tableau de bord",   "Vue de la classe"],
  ["remed",      "🩺", "Remédiation",       "Besoins & groupes"],
  ["devoirs",    "📌", "Devoirs",           "Assigner des textes"],
  ["textes",     "📚", "Banques de textes", "Correction & fluence"],
  ["classeur",   "📘", "Classeur",          "Fiches de leçons"],
  ["parametres", "⚙️", "Paramètres",        "Classes, réglages, données"]
];

const NAV_ELEVE = [
  ["hub",        "🏠", "Mon menu",            "Choisir une activité"],
  ["correction", "📝", "Je me corrige",       "Écrire et se relire"],
  ["fluence",    "📖", "Je lis à voix haute", "Mesurer ma vitesse"],
  ["dico",       "🔎", "Mon dictionnaire",    "Trouver comment ça s'écrit"],
  ["dictee",     "✍️", "Ma dictée",           "Avec mes mots à moi"],
  // Toujours accessible : c'est le retour de l'élève sur son propre travail,
  // pas une activité que l'enseignant ouvre ou ferme.
  ["bilan",      "🏆", "Mon bilan",           "Mes réussites"]
];

/* Droits de l'élève connecté, renvoyés par le serveur (activités ouvertes,
   mode verrouillé). Par défaut : tout est ouvert, comme avant. */
const Acces = {
  d: { verrouille: false,
       activites: ["correction", "fluence", "banque", "dico", "dictee"] },
  autorise(a) { return (this.d.activites || []).includes(a); },
  get verrouille() { return !!this.d.verrouille; },
};

/* Vues internes rattachées à une entrée du menu (pour garder la puce bleue
   allumée alors qu'on est sur un écran qui n'a plus son entrée). */
const RATTACHEMENT = {
  pilotage: "bord", eleve: "bord", motsCherches: "bord",
  devoirsSuggeres: "bord", impression: "bord",
  classes: "parametres", reglages: "parametres",
  securite: "parametres", pont: "parametres"
};

const Nav = {
  aller(vue, arg) {
    Etat.vue = vue;
    const actif = RATTACHEMENT[vue] || vue;
    $$(".nav-item").forEach(x =>
      x.classList.toggle("actif", x.dataset.vue === actif));
    if (typeof Prof !== "undefined" && vue !== "parametres") Prof._cibleParam = null;
    switch (vue) {
      case "bord":       return Prof.bord();
      case "pilotage":   return Prof.pilotage();
      case "motsCherches": return Prof.motsCherches();
      case "devoirsSuggeres": return Prof.devoirsSuggeres();
      case "impression": return Prof.impression(arg);
      case "eleve":      return Prof.fiche(arg);
      case "remed":      return Prof.remediation();
      case "devoirs":    return Prof.devoirs();
      case "textes":     return Prof.textes();
      case "classeur":   return Prof.classeur();
      case "parametres": return Prof.parametres(arg);
      // Anciennes entrées, désormais des onglets de « Paramètres ».
      case "classes":    return Prof.parametres("classes");
      case "reglages":   return Prof.parametres("reglages");
      case "securite":   return Prof.parametres("securite");
      case "pont":       return Prof.parametres("pont");
      // Une activité fermée par l'enseignant n'est pas atteignable, même en
      // passant par un raccourci : on ramène l'élève à son menu.
      case "hub":        return App.hub();
      case "correction": return Acces.autorise("correction")
                                ? Correction.sources() : App.hub();
      case "fluence":    return Acces.autorise("fluence")
                                ? Fluence.niveaux() : App.hub();
      case "bilan":      return App.bilan();
      case "mesLecons":  return App.mesLecons();
      case "dico":       return Acces.autorise("dico")
                                ? Dico.ecran(arg) : App.hub();
      case "dictee":     return Acces.autorise("dictee")
                                ? Dictee.choisir() : App.hub();
    }
  }
};

const App = {

  async demarrer() {
    Etat.ref = await API.get("/api/referentiel");
    document.documentElement.dataset.theme =
      Etat.ref.theme_sombre ? "sombre" : "clair";
    $("#btn-theme").textContent = Etat.ref.theme_sombre ? "☀️" : "🌙";
    $("#btn-theme").onclick = () => this.theme(!Etat.ref.theme_sombre);
    $("#btn-reglages").onclick = () => {
      if (Etat.espace === "eleve") this.espaceProf();
      Nav.aller("parametres", "reglages");
    };
    Confort.appliquer();
    // Si un code enseignant est défini, on demande à déverrouiller avant d'entrer.
    const sec = await Securite.etat();
    if (sec.defini) {
      Securite.verrou(() => this.espaceProf(true), () => this.connexion());
    } else {
      this.espaceProf(true);
    }
  },

  async theme(sombre) {
    await API.post("/api/theme", { sombre });
    Etat.ref.theme_sombre = sombre;
    document.documentElement.dataset.theme = sombre ? "sombre" : "clair";
    $("#btn-theme").textContent = sombre ? "☀️" : "🌙";
    if (Etat.vue === "parametres" && Prof._ongletParam === "reglages")
      Prof.parametres("reglages");
  },

  /* --------------------------------------------------- Barre latérale */
  sidebar(entrees, pied) {
    $("#nav").innerHTML = entrees.map(([cle, ico, lib, sub]) => `
      <button class="nav-item" data-vue="${cle}">
        <span class="ico">${ico}</span>
        <span><span class="lib">${lib}</span><br><span class="sub">${sub}</span></span>
      </button>`).join("");
    $$(".nav-item").forEach(x => x.onclick = () => Nav.aller(x.dataset.vue));
    $("#sidebar-pied").innerHTML = pied;
  },

  etatMoteur() {
    const m = Etat.ref.moteur;
    const e = $("#etat-ia");
    if (!e) return;
    e.innerHTML = `
      <div class="ligne"><span class="pastille ${m.actif ? "on" : ""}"></span>
        <span class="t">Moteur IA</span></div>
      <div class="n">${echapper(m.nom)}</div>
      <div class="d">${echapper(m.detail)}</div>`;
  },

  /* --------------------------------------------------- Espace enseignant */
  async espaceProf(deverrouille) {
    // Depuis l'espace élève, revenir côté prof repasse par le code si besoin.
    if (!deverrouille && !Etat.jeton) {
      const sec = await Securite.etat();
      if (sec.defini) {
        return Securite.verrou(() => this.espaceProf(true), () => this.connexion());
      }
    }
    Etat.espace = "prof";
    Etat.eleve = null;
    document.documentElement.dataset.espace = "prof";
    $("#logo-ico").textContent = "✏️";
    $("#logo-sous").textContent = "Correction & analyse";
    this.sidebar(NAV_PROF, `
      <button class="nav-item" id="vers-eleve">
        <span class="ico">🎓</span>
        <span><span class="lib">Espace élève</span><br>
          <span class="sub">Je m'autocorrige</span></span>
      </button>
      <div class="etat-ia" id="etat-ia"></div>`);
    $("#vers-eleve").onclick = () => this.connexion();
    this.etatMoteur();
    Nav.aller("bord");
  },

  /* --------------------------------------------------- Connexion élève */
  async connexion() {
    Etat.espace = "eleve";
    document.documentElement.dataset.espace = "eleve";
    $("#logo-ico").textContent = "🎓";
    $("#logo-sous").textContent = "Espace élève";
    $("#nav").innerHTML = "";
    // Le bouton de retour côté enseignant est toujours protégé par le code
    // (espaceProf() repasse par l'écran de verrou dès qu'un code est défini).
    $("#sidebar-pied").innerHTML = `
      <button class="nav-item" id="vers-prof">
        <span class="ico">🔒</span>
        <span><span class="lib">Espace enseignant</span><br>
          <span class="sub">Code demandé</span></span>
      </button>`;
    $("#vers-prof").onclick = () => this.espaceProf();

    const classes = await API.get("/api/classes");
    // Aucune liste déroulante : l'élève clique sa classe, puis son prénom.
    $("#contenu").innerHTML = `
      <div class="accueil">
        <div class="accueil-entete">
          <div class="accueil-emo">👋</div>
          <h1 class="accueil-titre">Bonjour !</h1>
          <p class="accueil-sous">Clique sur ta classe, puis sur ton prénom.</p>
        </div>
        <div class="accueil-etape" id="etape-classe">
          <div class="accueil-numero"><span>1</span> Ma classe</div>
          <div class="cartes-classe">
            ${classes.map((c, i) => `
              <button class="carte-classe" data-c="${i}">
                <span class="carte-classe-ico">🏫</span>
                <span class="carte-classe-nom">${echapper(c.nom)}</span>
                <span class="carte-classe-nb">${c.eleves.length} élèves</span>
              </button>`).join("") ||
              `<div class="vide">Aucune classe n'a encore été créée.</div>`}
          </div>
        </div>
        <div class="accueil-etape" id="etape-prenom" hidden>
          <div class="accueil-numero"><span>2</span> Mon prénom
            <button class="lien-retour" id="chg-classe">← changer de classe</button>
          </div>
          <div class="grille-prenoms" id="grille-prenoms"></div>
        </div>
      </div>`;
    $("#fil").textContent = "Espace élève";

    const ouvrirClasse = i => {
      const c = classes[i];
      $$(".carte-classe").forEach(b =>
        b.classList.toggle("actif", +b.dataset.c === i));
      $("#etape-prenom").hidden = false;
      $("#grille-prenoms").innerHTML = c.eleves.length
        ? c.eleves.map((e, k) => `
            <button class="carte-prenom" data-e="${k}">
              <span class="carte-prenom-ini">${echapper(
                (e.prenom || "?").trim().charAt(0).toUpperCase())}</span>
              <span class="carte-prenom-nom">${echapper(e.prenom)}</span>
            </button>`).join("")
        : `<div class="vide">Aucun élève dans cette classe.</div>`;
      $$(".carte-prenom").forEach(b => b.onclick = () => {
        Etat.eleve = c.eleves[+b.dataset.e];
        this.espaceEleve();
      });
      $("#etape-prenom").scrollIntoView({ behavior: "smooth", block: "nearest" });
    };

    $$(".carte-classe").forEach(b => b.onclick = () => ouvrirClasse(+b.dataset.c));
    $("#chg-classe").onclick = () => {
      $("#etape-prenom").hidden = true;
      $$(".carte-classe").forEach(b => b.classList.remove("actif"));
    };
    // Une seule classe : on affiche directement les prénoms.
    if (classes.length === 1) ouvrirClasse(0);
  },

  async espaceEleve() {
    // Le serveur dit ce à quoi CET élève a droit. L'interface ne fait que
    // s'y conformer : rien n'est décidé côté navigateur.
    try {
      const a = await API.get(`/api/eleve/${Etat.eleve.id}/acces`);
      if (!a.erreur) Acces.d = a;
    } catch (e) { /* hors ligne : on reste sur les droits par défaut */ }

    $("#logo-sous").textContent = Etat.eleve.prenom + " — " + Etat.eleve.classe_nom;
    // Seules les activités ouvertes apparaissent dans le menu.
    const entrees = NAV_ELEVE.filter(([cle]) =>
      cle === "hub" || cle === "bilan" || Acces.autorise(cle));
    Dico._retour = null;

    // Verrouillé : plus de retour libre côté enseignant, et la sortie est un
    // geste explicite (« j'ai fini »), pas un changement d'élève discret.
    const pied = Acces.verrouille
      ? `<button class="nav-item" id="fini-seance">
           <span class="ico">👋</span>
           <span><span class="lib">J'ai fini ma séance</span><br>
             <span class="sub">Laisser la place au suivant</span></span>
         </button>`
      : `<button class="nav-item" id="deco">
           <span class="ico">🔙</span>
           <span><span class="lib">Changer d'élève</span><br>
             <span class="sub">${echapper(Etat.eleve.classe_nom)}</span></span>
         </button>
         <button class="nav-item" id="vers-prof-2">
           <span class="ico">🔒</span>
           <span><span class="lib">Espace enseignant</span><br>
             <span class="sub">Code demandé</span></span>
         </button>`;
    this.sidebar(entrees, pied);

    if ($("#deco")) $("#deco").onclick = () => this.connexion();
    if ($("#vers-prof-2")) $("#vers-prof-2").onclick = () => this.espaceProf();
    if ($("#fini-seance")) $("#fini-seance").onclick = () =>
      confirmer("Tu as fini ta séance ?",
        "Ton travail est déjà enregistré. L'écran va revenir à la liste des " +
        "prénoms pour l'élève suivant.",
        () => { Etat.eleve = null; this.connexion(); },
        "Oui, j'ai fini", false);
    Nav.aller("hub");
  },

  async hub() {
    const r = await API.get(`/api/eleve/${Etat.eleve.id}/resume`);
    const dv = await API.get(`/api/eleve/${Etat.eleve.id}/devoirs`);
    const bouts = [];
    if (r.corrections) bouts.push(`${r.corrections} texte(s) corrigé(s)`);
    if (r.lectures) bouts.push(
      `${r.lectures} lecture(s) — meilleur score : ${Math.round(r.meilleur_mclm)} mots/min`);

    // Ce que le maître a décidé après avoir vu l'analyse : c'est prioritaire,
    // donc c'est tout en haut, avant les activités libres.
    let aFaire = [];
    try {
      const r = await API.get(`/api/eleve/${Etat.eleve.id}/a-faire`);
      aFaire = r.activites || [];
    } catch (e) { /* pas bloquant */ }
    const icoAct = { flash: "⚡", dictee: "✍️", lecon: "📘", fluence: "📖" };
    const blocAFaire = aFaire.length ? `
      <div class="carte a-faire">
        <div class="carte-titre">🎯 Ce que le maître veut que tu fasses d'abord</div>
        <div class="af-liste">
          ${aFaire.map(a => `
            <button class="af-tuile" data-id="${a.id}" data-genre="${a.genre}"
              data-lecon="${echapper(a.lecon_id || "")}">
              <span class="af-ico">${icoAct[a.genre] || "•"}</span>
              <span class="af-txt">${echapper(a.consigne || a.genre)}</span>
              <span class="af-go">Commencer →</span>
            </button>`).join("")}
        </div>
      </div>` : "";

    const devoirs = (dv.devoirs || []);
    const blocDevoirs = devoirs.length ? `
      <div class="carte devoirs-eleve">
        <div class="carte-titre">📌 À faire : ${devoirs.length} texte(s) donné(s) par le maître</div>
        <div class="rangee-devoirs">
          ${devoirs.slice(0, 4).map(d => `
            <button class="devoir-tuile" data-tid="${d.texte_id}">
              <span class="devoir-ico">📝</span>
              <span>${echapper(d.titre)}</span></button>`).join("")}
        </div>
      </div>` : "";

    $("#contenu").innerHTML =
      page(`Bonjour ${Etat.eleve.prenom} !`, "Que veux-tu faire aujourd'hui ?") +
      blocAFaire +
      blocDevoirs +
      // Une activité fermée par l'enseignant n'apparaît pas du tout : l'élève
      // ne voit pas une porte close, il voit un menu qui lui correspond.
      `<div class="tuiles">
        ${Acces.autorise("correction") ? `<div class="tuile" id="t-corr">
          <div class="emo">📝</div>
          <h3>J'écris et je me corrige</h3>
          <p>Un texte à moi, un texte de la classe,<br>ou un texte surprise à corriger.</p>
        </div>` : ""}
        ${Acces.autorise("fluence") ? `<div class="tuile" id="t-flu">
          <div class="emo">📖</div>
          <h3>Je lis à voix haute</h3>
          <p>Je m'entraîne à lire vite et bien.<br>Je mesure ma vitesse de lecture.</p>
        </div>` : ""}
        ${Acces.autorise("banque") ? `<div class="tuile" id="t-mots">
          <div class="emo">🎒</div>
          <h3>Ma banque de mots</h3>
          <p>Les mots que je rate souvent,<br>pour m'entraîner juste sur eux.</p>
        </div>` : ""}
        ${Acces.autorise("dico") ? `<div class="tuile tuile-dico" id="t-dico">
          <div class="emo">🔎</div>
          <h3>Mon dictionnaire</h3>
          <p>J'écris le mot comme je l'entends,<br>et je trouve comment il s'écrit.</p>
        </div>` : ""}
        ${Acces.autorise("dictee") ? `<div class="tuile tuile-dictee" id="t-dictee">
          <div class="emo">✍️</div>
          <h3>Ma dictée</h3>
          <p>Une dictée rien que pour moi,<br>avec les mots que je rate.</p>
        </div>` : ""}
        <div class="tuile tuile-bilan" id="t-bilan">
          <div class="emo">🏆</div>
          <h3>Mon bilan</h3>
          <p>Tout ce que j'ai réussi,<br>et comment je progresse.</p>
        </div>
      </div>
      <div style="text-align:center;color:var(--texte-doux);margin-top:26px">
        ${bouts.join("  •  ") || "C'est ta première fois : choisis une activité !"}
      </div>`;
    if ($("#t-corr")) $("#t-corr").onclick = () => Nav.aller("correction");
    if ($("#t-flu")) $("#t-flu").onclick = () => Nav.aller("fluence");
    if ($("#t-mots")) $("#t-mots").onclick = () => App.banqueLexicale();
    if ($("#t-bilan")) $("#t-bilan").onclick = () => Nav.aller("bilan");
    if ($("#t-dico")) $("#t-dico").onclick = () => Nav.aller("dico");
    if ($("#t-dictee")) $("#t-dictee").onclick = () => Nav.aller("dictee");
    $$(".devoir-tuile").forEach(b => b.onclick = () => Nav.aller("correction"));

    // Une activité « à faire » conduit directement au bon écran, et se
    // marque terminée dès que l'élève s'y rend.
    $$(".af-tuile").forEach(b => b.onclick = async () => {
      const { id, genre, lecon } = b.dataset;
      try {
        await API.post(`/api/eleve/${Etat.eleve.id}/a-faire/${id}/termine`, {});
      } catch (e) { /* on ouvre l'activité quand même */ }
      if (genre === "flash") return App.banqueLexicale();
      if (genre === "dictee") return Nav.aller("dictee");
      if (genre === "fluence") return Nav.aller("fluence");
      if (genre === "lecon") {
        if (lecon) await Classeur.ouvrir(lecon);
        return Nav.aller("correction");
      }
      Nav.aller("hub");
    });
  },

  /* ------------------------------------------------------- Mon bilan (élève)
     Tout est écrit pour un enfant : on montre d'abord ce qui est réussi, on
     explique chaque chiffre en une phrase, et on ne compare jamais l'élève
     aux autres — seulement à lui-même, semaine après semaine. */
  async bilan() {
    $("#contenu").innerHTML = `<div class="vide">
      <span class="chargement"></span> Je prépare ton bilan…</div>`;
    const b = await API.get(`/api/eleve/${Etat.eleve.id}/bilan`);
    if (b.erreur) { $("#contenu").innerHTML = `<div class="vide">Bilan indisponible.</div>`; return; }

    // Le bilan n'est vide que si l'élève n'a RIEN fait du tout. Oublier les
    // dictées ici masquait tout le bilan d'un élève qui n'avait fait que ça.
    const rien = !b.nb_corrections && !b.nb_lectures && !b.nb_dictees
                 && !(b.mots_appris + b.mots_restants);
    if (rien) {
      $("#contenu").innerHTML =
        page(`Mon bilan`, "Ici, tu verras tout ce que tu as réussi.") +
        `<div class="bilan-vide">
          <div class="bilan-vide-emo">🌱</div>
          <h3>Ton bilan est encore tout neuf</h3>
          <p>Corrige un texte ou fais une lecture chronométrée :<br>
             tes réussites apparaîtront ici.</p>
          <button class="btn grand" id="go-menu">Choisir une activité →</button>
        </div>`;
      $("#go-menu").onclick = () => Nav.aller("hub");
      return;
    }

    const obtenus = b.badges.filter(x => x.obtenu);
    // On n'affiche que les badges gagnés et le PROCHAIN de chaque série :
    // une liste de cinquante badges hors de portée décourage au lieu d'aider.
    const visibles = b.badges.filter(x => x.visible);
    const prochain = (b.badges_resume || {}).prochain;
    // Jauge de lecture : où en suis-je par rapport à mon objectif ?
    const pctRepere = b.repere ? Math.min(100, Math.round(b.mclm_meilleur / b.repere * 100)) : 0;

    $("#contenu").innerHTML =
      page(`Le bilan de ${Etat.eleve.prenom}`,
           "Tout ce que tu as réussi depuis le début. Bravo !") +

      /* ---- Mes réussites ---- */
      `<section class="bl-bloc">
        <h2 class="bl-titre"><span>🏆</span> Mes réussites
          <span class="bl-compte">${obtenus.length} sur ${b.badges.length}</span></h2>
        ${prochain ? `<div class="prochain-badge">
          <span class="pb-emo">${prochain.emoji}</span>
          <div><b>Le plus proche : ${echapper(prochain.titre)}</b><br>
            <span class="pb-obj">${echapper(prochain.objectif)} —
              tu en es à ${prochain.valeur} sur ${prochain.cible}</span></div>
          <div class="pb-jauge"><div style="width:${Math.min(100,
            Math.round(prochain.valeur / prochain.cible * 100))}%"></div></div>
        </div>` : ""}
        <div class="badges">
          ${visibles.map(x => `<div class="badge ${x.obtenu ? "gagne" : "a-venir"}"
            style="--c:${x.couleur}" title="${echapper(x.famille_nom)} — palier ${
            x.palier} sur ${x.nb_paliers}">
            <div class="badge-emo">${x.emoji}</div>
            <div class="badge-nom">${echapper(x.titre)}</div>
            <div class="badge-obj">${x.obtenu ? "✓ " : ""}${echapper(x.objectif)}</div>
            ${x.obtenu ? "" : `
              <div class="badge-jauge">
                <div style="width:${Math.min(100,
                  Math.round(x.valeur / x.cible * 100))}%"></div></div>
              <div class="badge-reste">${x.valeur} / ${x.cible}</div>`}
            <div class="badge-palier">${"●".repeat(x.palier)}${
              "○".repeat(Math.max(0, x.nb_paliers - x.palier))}</div>
          </div>`).join("")}
        </div>
        <div class="bl-legende" style="margin-top:12px">
          Chaque série compte plusieurs paliers. Quand tu en décroches un,
          le suivant apparaît.
        </div>
      </section>` +

      /* ---- L'écriture ---- */
      (b.nb_corrections ? `<section class="bl-bloc bl-ecrit">
        <h2 class="bl-titre"><span>📝</span> Quand j'écris et je me corrige</h2>
        <div class="bl-duo">
          <div class="bl-chiffres colonne">
            <div class="bl-chiffre">
              <div class="v">${b.nb_corrections}</div>
              <div class="l">textes corrigés</div>
              <div class="e">Le nombre de fois où tu es allé(e) au bout.</div>
            </div>
            <div class="bl-chiffre vert">
              <div class="v">${b.erreurs_corrigees_total}</div>
              <div class="l">erreurs réparées</div>
              <div class="e">Toutes tes corrections depuis le début.</div>
            </div>
            <div class="bl-chiffre bleu">
              <div class="v">${b.autonomie}%</div>
              <div class="l">trouvées tout(e) seul(e)</div>
              <div class="e">Sur 10 erreurs corrigées, tu en as trouvé
                ${Math.round(b.autonomie / 10)} sans aucune aide.</div>
            </div>
          </div>
          ${b.progression.length > 1 ? `<div class="carte bl-graph">
            ${Graph.courbe(b.progression,
              { titre: "Mes corrections, texte après texte (%)", unite: "%",
                couleur: "var(--vert)" })}
            <div class="bl-legende">Chaque point est un texte. Plus le point est
              haut, plus tu as réparé d'erreurs dans ce texte-là.</div>
          </div>` : ""}
        </div>
      </section>` : "") +

      /* ---- Ce qui progresse ---- */
      (b.evolution.length ? `<section class="bl-bloc bl-progres">
        <h2 class="bl-titre"><span>📈</span> Ce que je réussis de mieux en mieux</h2>
        <div class="bl-legende" style="margin-bottom:12px">
          ${b.evolution.some(x => x.comparable)
            ? "On compare tes 3 derniers textes avec les 3 d'avant. Moins il y a d'erreurs, mieux c'est !"
            : "Voici les erreurs que tu fais le plus souvent en ce moment. Continue : on pourra bientôt comparer avec avant."}
        </div>
        <div class="evolutions">
          ${b.evolution.map(x => `
            <div class="evo ${x.comparable ? (x.mieux ? "mieux" : "pareil") : ""}">
              <div class="evo-nom">${echapper(x.libelle)}</div>
              ${x.comparable ? `
                <div class="evo-chiffres">
                  <span class="evo-avant">${x.avant}</span>
                  <span class="evo-fleche">→</span>
                  <span class="evo-apres">${x.maintenant}</span>
                </div>
                <div class="evo-mot">${x.mieux
                  ? "👏 tu en fais moins qu'avant"
                  : (x.maintenant === x.avant ? "= comme avant" : "à retravailler")}</div>`
              : `<div class="evo-chiffres"><span class="evo-apres">${x.maintenant}</span></div>
                 <div class="evo-mot">par texte, en moyenne</div>`}
            </div>`).join("")}
        </div>
        ${b.a_travailler.length ? `<button class="btn grand" id="bl-lecons"
          style="margin-top:16px">📘 Revoir les leçons qui vont m'aider</button>` : ""}
      </section>` : "") +

      /* ---- La lecture ---- */
      (b.nb_lectures ? `<section class="bl-bloc bl-lecture">
        <h2 class="bl-titre"><span>📖</span> Quand je lis à voix haute</h2>
        <div class="bl-objectif">
          <div class="bl-objectif-txt">
            <b>Mon meilleur score : ${Math.round(b.mclm_meilleur)} mots en 1 minute.</b><br>
            Mon objectif pour cette année : ${b.repere} mots par minute.
            ${b.mclm_meilleur >= b.repere
              ? " 🎉 Tu l'as déjà atteint, bravo !"
              : ` Encore ${Math.max(1, Math.round(b.repere - b.mclm_meilleur))} mots et c'est gagné !`}
          </div>
          <div class="bl-jauge">
            <div class="bl-jauge-rempli" style="width:${pctRepere}%"></div>
            <span class="bl-jauge-txt">${pctRepere}% de mon objectif</span>
          </div>
        </div>
        <div class="bl-duo">
          <div class="bl-chiffres colonne">
            <div class="bl-chiffre">
              <div class="v">${b.nb_lectures}</div>
              <div class="l">lectures chronométrées</div></div>
            <div class="bl-chiffre orange">
              <div class="v">${Math.round(b.mclm_dernier)}</div>
              <div class="l">ma dernière lecture</div></div>
            <div class="bl-chiffre ${b.mclm_gain >= 0 ? "vert" : ""}">
              <div class="v">${b.mclm_gain >= 0 ? "+" : ""}${
                Math.round(b.mclm_gain)}</div>
              <div class="l">mots gagnés depuis le début</div>
              <div class="e">${b.mclm_gain > 0
                ? "Tu lis plus vite qu'à ta première lecture. 🚀"
                : "Continue à t'entraîner : ça viendra !"}</div>
            </div>
          </div>
          ${b.fluence.length > 1 ? `<div class="carte bl-graph">
            ${Graph.courbe(b.fluence, { titre: "Ma vitesse de lecture (mots par minute)",
              repere: (b.objectif && b.objectif.mclm_vise) || b.repere,
              couleur: "var(--cyan)" })}
            <div class="bl-legende">La ligne orange en pointillés, c'est ton
              objectif. Chaque point est une lecture.</div>
          </div>` : ""}
        </div>
        ${this._blocObjectif(b)}
      </section>` : "") +

      /* ---- Ma dictée ---- */
      (b.nb_dictees ? `<section class="bl-bloc bl-dictee">
        <h2 class="bl-titre"><span>✍️</span> Quand je fais ma dictée</h2>
        <div class="bl-chiffres">
          <div class="bl-chiffre"><div class="v">${b.nb_dictees}</div>
            <div class="l">dictées faites</div></div>
          <div class="bl-chiffre vert"><div class="v">${Math.round(b.dictee_meilleur)}%</div>
            <div class="l">mon meilleur score</div>
            <div class="e">Le pourcentage de mots écrits sans faute.</div></div>
          <div class="bl-chiffre bleu"><div class="v">${Math.round(b.dictee_score)}%</div>
            <div class="l">ma moyenne</div></div>
        </div>
        ${(b.dictee_orthographe + b.dictee_ecoute) ? `
          <div class="bl-legende" style="margin-top:14px">
            Sur toutes tes dictées : <b>${b.dictee_orthographe}</b> mot(s) que tu
            avais bien entendus mais mal écrits, et <b>${b.dictee_ecoute}</b> mot(s)
            que tu n'avais pas bien entendus.
            ${b.dictee_orthographe > b.dictee_ecoute
              ? " Ton oreille est bonne : c'est l'écriture qu'il faut travailler."
              : (b.dictee_ecoute > b.dictee_orthographe
                 ? " Prends le temps de réécouter chaque mot avant d'écrire."
                 : "")}
          </div>` : ""}
        ${b.dictee_courbe.length > 1 ? `<div class="carte bl-graph compact">
          ${Graph.courbe(b.dictee_courbe,
            { titre: "Mes scores de dictée (%)", unite: "%",
              couleur: "var(--ambre)" })}
        </div>` : ""}
      </section>` : "") +

      /* ---- Ma banque de mots ---- */
      ((b.mots_appris + b.mots_restants) ? `<section class="bl-bloc bl-mots">
        <h2 class="bl-titre"><span>🎒</span> Ma banque de mots</h2>
        <div class="bl-chiffres">
          <div class="bl-chiffre vert"><div class="v">${b.mots_appris}</div>
            <div class="l">mots appris</div>
            <div class="e">Tu as coché « je le sais maintenant ».</div></div>
          <div class="bl-chiffre orange"><div class="v">${b.mots_restants}</div>
            <div class="l">mots à travailler</div>
            <div class="e">Ceux que tu rates encore de temps en temps.</div></div>
        </div>
        ${Acces.autorise("banque")
          ? `<button class="btn" id="bl-banque">🎒 Aller m'entraîner sur ces mots</button>`
          : ""}
      </section>` : "") +

      `<div class="rangee" style="margin-top:20px">
        <button class="btn doux grand" id="bl-menu">🏠 Retour au menu</button>
        <button class="btn fantome pousse" id="bl-imprimer">🖨️ Imprimer mon bilan</button>
      </div>`;

    this._brancherObjectif(b);
    $("#bl-menu").onclick = () => Nav.aller("hub");
    $("#bl-imprimer").onclick = () => window.print();
    if ($("#bl-banque")) $("#bl-banque").onclick = () => this.banqueLexicale();
    if ($("#bl-lecons")) $("#bl-lecons").onclick = () => this.mesLecons(b.a_travailler);
  },

  /* L'élève choisit lui-même de viser plus haut. On ne le lui impose pas :
     un objectif qu'on s'est donné soi-même engage bien davantage. */
  _blocObjectif(b) {
    const repere = b.repere;
    const vise = (b.objectif && b.objectif.mclm_vise) || 0;
    const meilleur = Math.round(b.mclm_meilleur);
    // On ne propose de viser plus haut que si le repère est déjà atteint.
    const atteint = meilleur >= repere;
    const propositions = [repere + 10, repere + 20, repere + 30]
      .filter(v => v > meilleur);

    if (vise) {
      const fait = meilleur >= vise;
      return `<div class="objectif-perso ${fait ? "atteint" : ""}">
        <div class="op-txt">
          <b>🎯 Mon objectif à moi : ${vise} mots par minute.</b><br>
          ${fait ? "Tu l'as atteint ! Tu peux en viser un plus haut."
                 : `Il te manque ${Math.max(1, vise - meilleur)} mots. Courage !`}
        </div>
        <button class="btn fantome" id="op-changer">Changer d'objectif</button>
      </div>`;
    }
    if (!atteint || !propositions.length) return "";
    return `<div class="objectif-perso propose">
      <div class="op-txt">
        <b>🎯 Tu as atteint l'objectif de ta classe. Tu veux viser plus haut ?</b><br>
        Choisis toi-même ton nouvel objectif — c'est le tien, personne ne
        te le demande.
      </div>
      <div class="op-choix">
        ${propositions.map(v => `<button class="btn op-viser" data-v="${v}">
          ${v} mots/min</button>`).join("")}
        <button class="btn doux op-viser" data-v="0">Non merci</button>
      </div>
    </div>`;
  },

  _brancherObjectif(b) {
    const poser = async v => {
      await API.post(`/api/eleve/${Etat.eleve.id}/objectif`, { mclm_vise: v });
      toast(v ? `Nouvel objectif : ${v} mots par minute. 🎯`
              : "Objectif retiré.", 3500);
      this.bilan();
    };
    $$(".op-viser").forEach(x => x.onclick = () => poser(+x.dataset.v));
    if ($("#op-changer")) $("#op-changer").onclick = () => {
      const base = Math.max(b.repere, Math.round(b.mclm_meilleur));
      modale(`<div class="carte-titre">🎯 Mon objectif de lecture</div>
        <div class="carte-sous" style="margin-top:6px">Choisis le nombre de mots
          par minute que tu veux atteindre.</div>
        <div class="op-choix" style="margin-top:12px">
          ${[base + 5, base + 10, base + 20, base + 30].map(v =>
            `<button class="btn op-modale" data-v="${v}">${v} mots/min</button>`).join("")}
          <button class="btn doux op-modale" data-v="0">Retirer mon objectif</button>
        </div>`);
      $$(".op-modale").forEach(x => x.onclick = () => {
        fermerModale(); poser(+x.dataset.v);
      });
    };
  },

  /* Les leçons du classeur qui correspondent aux difficultés de CET élève :
     les leçons ne restent pas dans un classeur, elles servent. */
  async mesLecons(categories) {
    categories = categories || this._categoriesATravailler || [];
    this._categoriesATravailler = categories;
    $("#contenu").innerHTML =
      page("📘 Mes leçons", "Les leçons qui t'aideront le plus en ce moment.") +
      `<div id="zone-mes-lecons"><span class="chargement"></span></div>
       <div class="rangee" style="margin-top:18px">
         <button class="btn doux" id="ml-retour">← Retour à mon bilan</button></div>`;
    $("#ml-retour").onclick = () => Nav.aller("bilan");

    const blocs = [];
    for (const cat of categories.slice(0, 3)) {
      try {
        const rep = await API.get(`/api/classeur/pour-categorie/${cat}`);
        const f = (rep.fiches || [])[0];      // une seule leçon par difficulté
        if (f) blocs.push({ cat, fiche: f });
      } catch (e) { /* leçon indisponible : on passe */ }
    }
    $("#zone-mes-lecons").innerHTML = blocs.length
      ? `<div class="grille-lecons">${blocs.map(({ cat, fiche }) => `
          <div class="carte-lecon" style="--c:${couleurCat(cat)}">
            <div class="carte-lecon-haut">${libelleCat(cat)}</div>
            <div class="carte-lecon-titre">${echapper(
              (fiche.titre || "").replace(/^[^\p{L}]+/u, ""))}</div>
            <div class="carte-lecon-sous">${echapper(fiche.sous_domaine || "")}</div>
            <button class="btn ouvrir-lecon" data-id="${echapper(fiche.lecon_id)}">
              Ouvrir la leçon</button>
          </div>`).join("")}</div>`
      : `<div class="vide">Aucune leçon à revoir pour l'instant : continue comme ça !</div>`;
    $$(".ouvrir-lecon").forEach(b =>
      b.onclick = () => Classeur.ouvrir(b.dataset.id));
  },

  async banqueLexicale() {
    const mots = await API.get(`/api/eleve/${Etat.eleve.id}/banque-lexicale`);
    $("#contenu").innerHTML =
      page("🎒 Ma banque de mots",
        "Les mots que tu rates souvent. Entraîne-toi, puis prouve que tu les sais.") +
      (mots.length ? `
        <div class="carte banque-entrainement">
          <div class="be-texte">
            <div class="carte-titre">⚡ M'entraîner en éclair</div>
            <div class="carte-sous" style="margin:0">Le mot s'affiche deux
              secondes, puis disparaît : à toi de le réécrire. C'est comme ça
              qu'on retient l'image d'un mot. Les mots réussis
              <b>trois fois</b> sortent de ta banque.</div>
          </div>
          <button class="btn grand" id="lancer-flash">
            Commencer (${mots.length} mot${mots.length > 1 ? "s" : ""})</button>
        </div>
        <div class="grille g3" id="grille-mots">
        ${mots.map(m => `
          <div class="carte" data-mot="${echapper(m.mot)}" data-cat="${echapper(m.categorie)}">
            <div style="font-size:20px;font-weight:800">${echapper(m.mot)}</div>
            <div style="font-size:12.5px;color:var(--texte-doux);margin:4px 0 10px">
              ${echapper(libelleCat(m.categorie))} · raté ${m.nb_fois} fois</div>
            <button class="btn fantome btn-su">✓ Je le sais maintenant</button>
          </div>`).join("")}
      </div>` : `<div class="vide">Aucun mot à travailler pour l'instant — continue à te corriger !</div>`) +
      `<div class="rangee" style="margin-top:16px">
        <button class="btn doux" id="retour-hub">← Retour au menu</button></div>`;
    $("#retour-hub").onclick = () => Nav.aller("hub");
    if ($("#lancer-flash")) $("#lancer-flash").onclick = () => Flash.demarrer(mots);
    $$("#grille-mots .btn-su").forEach(b => b.onclick = async (ev) => {
      const carte = ev.target.closest(".carte");
      await API.post(`/api/eleve/${Etat.eleve.id}/banque-lexicale/maitrise`,
        { mot: carte.dataset.mot, categorie: carte.dataset.cat, maitrise: true });
      carte.remove();
    });
  }
};

/* ==========================================================================
   Flash cards — la mémorisation éclair

   Le mot apparaît brièvement, puis disparaît : l'élève doit le réécrire de
   mémoire. C'est l'exercice qui installe l'image orthographique du mot, bien
   plus efficace que de le recopier vingt fois en le regardant.
   Un mot n'est acquis qu'après TROIS réussites : une fois peut être un coup
   de chance, trois fois non.
   ========================================================================== */
const Flash = {
  REUSSITES_POUR_VALIDER: 3,
  etat: null,

  demarrer(mots) {
    // On mélange, et on garde une file de travail avec le compteur de réussites.
    const file = mots.map(m => ({
      mot: m.mot, categorie: m.categorie, reussites: 0, essais: 0,
    })).sort(() => Math.random() - 0.5);
    this.etat = { file, i: 0, acquis: [], debut: Date.now(), tours: 0 };
    this.carte();
  },

  _restants() {
    return this.etat.file.filter(x => x.reussites < this.REUSSITES_POUR_VALIDER);
  },

  carte() {
    const restants = this._restants();
    if (!restants.length) return this.bilan();
    // On repart au début de la file quand on en a fait le tour.
    if (this.etat.i >= restants.length) { this.etat.i = 0; this.etat.tours++; }
    const item = restants[this.etat.i];
    const total = this.etat.file.length;
    const faits = total - restants.length;

    $("#contenu").innerHTML =
      `<div class="dictee-barre">
        <div class="dictee-progres">
          <div style="width:${Math.round(faits / total * 100)}%"></div></div>
        <span class="dictee-compte">${faits} mot(s) acquis sur ${total}</span>
      </div>
      <div class="carte flash-scene">
        <div class="flash-etoiles">${
          "★".repeat(item.reussites) +
          "☆".repeat(this.REUSSITES_POUR_VALIDER - item.reussites)}</div>
        <div class="flash-zone" id="flash-zone">
          <div class="flash-mot" id="flash-mot">${echapper(item.mot)}</div>
        </div>
        <label class="champ" for="flash-saisie" style="margin-top:18px">
          Réécris le mot</label>
        <input type="text" id="flash-saisie" class="dictee-champ" autocomplete="off"
          spellcheck="false" disabled placeholder="regarde bien…">
        <div class="dictee-actions">
          <button class="btn grand" id="flash-ok" disabled>Je valide →</button>
          <button class="btn doux" id="flash-revoir" disabled>👁 Revoir le mot</button>
        </div>
        <div class="flash-quitter">
          <button class="lien-retour" id="flash-stop">Arrêter l'entraînement</button>
        </div>
      </div>`;

    $("#flash-stop").onclick = () => this.bilan();
    $("#flash-revoir").onclick = () => this._montrer(item, true);
    $("#flash-ok").onclick = () => this.valider(item);
    $("#flash-saisie").onkeydown = ev => {
      if (ev.key === "Enter" && !$("#flash-ok").disabled) this.valider(item);
    };
    this._montrer(item);
  },

  /* Le mot s'affiche, un compte à rebours, puis il disparaît. */
  _montrer(item, cestUnRappel) {
    const zone = $("#flash-zone");
    const champ = $("#flash-saisie");
    if (!zone || !champ) return;
    champ.disabled = true;
    champ.placeholder = "regarde bien…";
    $("#flash-ok").disabled = true;
    $("#flash-revoir").disabled = true;
    // Un rappel est plus court : on ne redonne pas le confort du premier coup.
    let reste = cestUnRappel ? 1 : 2;
    zone.innerHTML = `<div class="flash-mot">${echapper(item.mot)}</div>
      <div class="flash-chrono" id="flash-chrono">${reste}</div>`;
    const tic = setInterval(() => {
      reste--;
      const c = $("#flash-chrono");
      if (c) c.textContent = reste;
      if (reste <= 0) {
        clearInterval(tic);
        if (!$("#flash-zone")) return;
        $("#flash-zone").innerHTML = `<div class="flash-cache">🙈 À toi !</div>`;
        champ.disabled = false;
        champ.value = "";
        champ.placeholder = "écris le mot de mémoire";
        champ.focus();
        $("#flash-ok").disabled = false;
        $("#flash-revoir").disabled = false;
      }
    }, 1000);
  },

  valider(item) {
    const saisi = $("#flash-saisie").value.trim();
    const juste = saisi.toLowerCase() === item.mot.toLowerCase();
    const exact = saisi === item.mot;
    item.essais++;
    if (juste && exact) item.reussites++;
    else item.reussites = 0;      // une erreur remet le compteur à zéro

    const scene = $(".flash-scene");
    const acquis = item.reussites >= this.REUSSITES_POUR_VALIDER;
    scene.insertAdjacentHTML("beforeend", `
      <div class="dictee-retour ${exact ? "juste" : (juste ? "accent" : "ecoute")}">
        <div class="dr-haut">
          <span class="dr-emo">${exact ? (acquis ? "🏅" : "✅")
            : (juste ? "✏️" : "🔎")}</span>
          <span class="dr-titre">${exact
            ? (acquis ? "Mot acquis !" : "Juste !")
            : (juste ? "Presque : les accents ou la majuscule" : "Pas encore")}</span>
        </div>
        ${exact ? "" : `<div class="dr-mot">Le mot s'écrit :
          <b>${echapper(item.mot)}</b></div>`}
        ${acquis ? `<div class="dr-conseil">Tu l'as écrit juste
          ${this.REUSSITES_POUR_VALIDER} fois : il sort de ta banque. 🎉</div>`
          : (exact ? `<div class="dr-conseil">Encore
              ${this.REUSSITES_POUR_VALIDER - item.reussites} fois et il est à
              toi.</div>` : "")}
        <button class="btn grand" id="flash-suite">Mot suivant →</button>
      </div>`);
    $("#flash-ok").disabled = true;
    $("#flash-revoir").disabled = true;
    $("#flash-saisie").disabled = true;

    const b = $("#flash-suite");
    b.focus();
    b.onclick = async () => {
      if (acquis) {
        this.etat.acquis.push(item.mot);
        try {
          await API.post(`/api/eleve/${Etat.eleve.id}/banque-lexicale/maitrise`,
            { mot: item.mot, categorie: item.categorie, maitrise: true });
        } catch (e) { /* on continue quand même */ }
      } else {
        this.etat.i++;
      }
      this.carte();
    };
    b.scrollIntoView({ behavior: "smooth", block: "nearest" });
  },

  bilan() {
    const e = this.etat;
    const restants = this._restants().length;
    $("#contenu").innerHTML =
      page("⚡ Entraînement terminé", "") +
      `<div class="dictee-bravo">
        <div class="dictee-score">${e.acquis.length}</div>
        <div class="dictee-score-l">mot(s) acquis aujourd'hui</div>
        <div class="dictee-message">${e.acquis.length
          ? "Ils sortent de ta banque : tu sais les écrire de mémoire. 🎉"
          : "Rien d'acquis cette fois — mais chaque essai laisse une trace. Recommence !"}</div>
      </div>
      ${e.acquis.length ? `<div class="carte">
        <div class="carte-titre">Les mots que tu sais maintenant</div>
        <div class="flash-acquis">${e.acquis.map(m =>
          `<span class="flash-acquis-mot">${echapper(m)}</span>`).join("")}</div>
      </div>` : ""}
      ${restants ? `<div class="carte">
        <div class="carte-sous" style="margin:0">Il te reste
          <b>${restants} mot(s)</b> à travailler dans ta banque.</div>
      </div>` : ""}
      <div class="rangee" style="margin-top:18px">
        <button class="btn doux grand" id="fl-banque">🎒 Ma banque de mots</button>
        <button class="btn grand pousse" id="fl-menu">🏠 Retour au menu</button>
      </div>`;
    $("#fl-banque").onclick = () => App.banqueLexicale();
    $("#fl-menu").onclick = () => Nav.aller("hub");
  }
};

window.addEventListener("DOMContentLoaded", () => App.demarrer());
