/* ============================================================
   LEÇONS — Bibliothèque des fiches officielles
   Chaque leçon est un document du site « Découvrons notre
   Constitution » (Conseil constitutionnel / Éducation nationale).
   Les PDF sont attendus dans assets/lecons/ ; si un fichier
   manque, le lien officiel est proposé à la place.
   ============================================================ */


/* ---- Liste embarquée (repli si la page est ouverte en double-clic) ---- */
const LECONS_FALLBACK = {
  "_commentaire": "Bibliotheque de lecons du jeu (bouton 📚). Chaque lecon est un document officiel telechargeable du site Decouvrons notre Constitution (Conseil constitutionnel / ministere de l'Education nationale). Les fichiers sont attendus dans assets/lecons/ ; si un fichier est absent, le jeu propose automatiquement le lien officiel.",
  "dossier": "assets/lecons/",
  "source_officielle": {
    "site": "Découvrons notre Constitution",
    "editeur": "Conseil constitutionnel et ministère de l'Éducation nationale",
    "url": "https://www.decouvronsnotreconstitution.fr/",
    "mention": "Source : Conseil constitutionnel / Découvrons notre Constitution - www.decouvronsnotreconstitution.fr",
    "illustrations": "Illustrations cycle 3 : Fabrice Mosca. Infographies : Amélie Blanquet (Play Bac Presse). Textes et jeux : Bayard Jeunesse.",
    "date_extraction": "19/09/2026",
    "conditions": "Contenus librement diffusables et reproductibles pour un usage non commercial, sous réserve de citer la source, de conserver le titre, la date d'extraction et le nom de l'illustrateur, et de ne pas altérer les contenus (mentions légales du site)."
  },
  "salles": {
    "1": "Salle 1 — Qu'est-ce qu'une Constitution ?",
    "2": "Salle 2 — Les textes de la Constitution",
    "3": "Salle 3 — La vie démocratique",
    "4": "Salle 4 — Le parcours d'une loi",
    "5": "Salle 5 — Les valeurs et le gardien",
    "6": "Pour aller plus loin — La Constitution au quotidien"
  },
  "lecons": [
    {
      "id": "constitution-francaise",
      "icone": "📘",
      "titre": "La Constitution française",
      "salle": 1,
      "theme": "Qu'est-ce qu'une Constitution ?",
      "type": "fiche",
      "format": "Infographie — 1 page",
      "apercu": "L'essentiel en une page : ce qu'est une Constitution, les trois pouvoirs et le gardien du texte.",
      "fichier": "c3-la-constitution-francaise.pdf",
      "poids": "1,98 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2025-10/C3_La_Constitution_francaise_2025.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-qu-est-ce-qu-une-constitution",
      "notions": [
        "Définition d'une Constitution",
        "Les trois pouvoirs",
        "15 Constitutions depuis 1789",
        "Rôle du Conseil constitutionnel"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "theme1-constitution",
      "icone": "📗",
      "titre": "Qu'est-ce qu'une Constitution ? (dossier)",
      "salle": 1,
      "theme": "Qu'est-ce qu'une Constitution ?",
      "type": "fiche",
      "format": "Dossier élève — 5 rubriques",
      "apercu": "Le dossier complet du thème 1 : à quoi sert le texte le plus important du pays, et comment on peut le modifier.",
      "fichier": "c3-theme1-qu-est-ce-qu-une-constitution.pdf",
      "poids": "3,63 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-02/Cycle%203%20-%20Th%C3%A8me%201.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-qu-est-ce-qu-une-constitution",
      "notions": [
        "Le texte de droit le plus important",
        "Séparation des pouvoirs",
        "Droits garantis",
        "Révision de la Constitution"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "jeu-sais-tu",
      "icone": "🎲",
      "titre": "Jeu : Sais-tu ce qu'est une Constitution ?",
      "salle": 1,
      "theme": "Qu'est-ce qu'une Constitution ?",
      "type": "jeu",
      "format": "Fiche-jeu — 6 questions, corrigé inclus",
      "apercu": "Le quiz officiel du site, à imprimer : 6 questions à choix multiples avec les réponses au bas de la page.",
      "fichier": "jeu-sais-tu-ce-qu-est-une-constitution.pdf",
      "poids": "1,53 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/Sais-tu%20ce%20qu%27est%20une%20Constitution%20%288-10%20ans%29.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-qu-est-ce-qu-une-constitution",
      "notions": [
        "QCM de révision",
        "Corrigé fourni"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "textes-constitution",
      "icone": "📜",
      "titre": "Les textes de notre Constitution",
      "salle": 2,
      "theme": "Le texte de la Constitution de la Ve République",
      "type": "fiche",
      "format": "Infographie — 1 page",
      "apercu": "Les quatre textes qui forment notre Constitution, avec un petit dictionnaire des mots difficiles.",
      "fichier": "c3-les-textes-de-notre-constitution.pdf",
      "poids": "0,74 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-07/C3_textes_Constitution.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-le-texte-de-la-constitution-de-la-ve-republique",
      "notions": [
        "Constitution du 4 octobre 1958",
        "Déclaration des droits de l'homme et du citoyen de 1789",
        "Préambule de 1946",
        "Charte de l'environnement de 2005"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "theme2-texte",
      "icone": "📕",
      "titre": "Le texte de la Constitution de la Ve République (dossier)",
      "salle": 2,
      "theme": "Le texte de la Constitution de la Ve République",
      "type": "fiche",
      "format": "Dossier élève — 4 à 5 pages",
      "apercu": "Le dossier complet du thème 2, avec son lexique : histoire du texte, pouvoirs, gardien et révision.",
      "fichier": "c3-theme2-le-texte-de-la-constitution.pdf",
      "poids": "4,26 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-02/Cycle%203%20-%20Th%C3%A8me%202.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-le-texte-de-la-constitution-de-la-ve-republique",
      "notions": [
        "Histoire institutionnelle",
        "Les trois pouvoirs",
        "Conseil constitutionnel",
        "Modifier la Constitution",
        "Lexique"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "jeu-incollable-ve",
      "icone": "🎲",
      "titre": "Jeu : Es-tu incollable sur la Constitution de la Ve République ?",
      "salle": 2,
      "theme": "Le texte de la Constitution de la Ve République",
      "type": "jeu",
      "format": "Fiche-jeu — 6 questions, corrigé inclus",
      "apercu": "Quiz officiel à imprimer : 6 questions sur le texte, la devise et les principes, corrigé au bas de la page.",
      "fichier": "jeu-es-tu-incollable-constitution-ve-republique.pdf",
      "poids": "1,51 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/jeu-es-tu-incollable-sur-la-Constitution-de-la-Ve-Republique-8-10_ans.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-le-texte-de-la-constitution-de-la-ve-republique",
      "notions": [
        "QCM de révision",
        "Corrigé fourni"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "theme4-democratie",
      "icone": "🗳️",
      "titre": "Comment la Constitution organise la vie démocratique",
      "salle": 3,
      "theme": "La vie démocratique",
      "type": "fiche",
      "format": "Dossier élève — 3 pages",
      "apercu": "Pourquoi le pouvoir appartient aux citoyens, et comment ils l'exercent par le vote.",
      "fichier": "c3-theme4-vie-democratique.pdf",
      "poids": "3,14 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-02/Cycle%203%20-%20Th%C3%A8me%204.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-comment-la-constitution-organise-la-vie-democratique-en-france",
      "notions": [
        "Souveraineté du peuple",
        "Le vote et le référendum",
        "Exécutif, législatif, judiciaire"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "president",
      "icone": "🎩",
      "titre": "Le président de la République",
      "salle": 3,
      "theme": "La vie démocratique",
      "type": "fiche",
      "format": "Infographie — 1 page",
      "apercu": "Comment on élit le président, pour combien de temps, et ce qu'il a le droit de faire.",
      "fichier": "c3-le-president-de-la-republique.pdf",
      "poids": "1,39 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-07/C3_President_Republique.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-comment-la-constitution-organise-la-vie-democratique-en-france",
      "notions": [
        "Suffrage universel direct",
        "Mandat de 5 ans renouvelable une fois",
        "Nomination des ministres",
        "Dissolution de l'Assemblée nationale",
        "Référendum"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "parcours-loi",
      "icone": "⚙️",
      "titre": "Le parcours d'une loi",
      "salle": 4,
      "theme": "La procédure d'élaboration des lois",
      "type": "fiche",
      "format": "Infographie — 1 page",
      "apercu": "Les trois grandes étapes d'une loi, de la première ligne écrite jusqu'à son application.",
      "fichier": "le-parcours-d-une-loi.pdf",
      "poids": "0,65 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/Parcours_Loi_8-10_ans.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-comment-la-constitution-organise-la-procedure-d-elaboration-des-lois",
      "notions": [
        "Le texte",
        "Le vote et la navette parlementaire",
        "Promulgation et Journal officiel"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "theme5-lois",
      "icone": "📘",
      "titre": "La procédure d'élaboration des lois (dossier 2025)",
      "salle": 4,
      "theme": "La procédure d'élaboration des lois",
      "type": "fiche",
      "format": "Dossier élève — 3 pages",
      "apercu": "Qui peut proposer une loi, comment le Parlement l'examine, et qui la promulgue.",
      "fichier": "c3-theme5-elaboration-des-lois.pdf",
      "poids": "1,57 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2025-10/V3_T5-Cycle_3-nouveau-bureau-2.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-comment-la-constitution-organise-la-procedure-d-elaboration-des-lois",
      "notions": [
        "Projet et proposition de loi",
        "Examen et vote au Parlement",
        "Promulgation et entrée en vigueur",
        "Composition du Conseil constitutionnel en 2025"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "jeu-lois",
      "icone": "🎲",
      "titre": "Jeu : Que sais-tu sur la procédure d'élaboration des lois ?",
      "salle": 4,
      "theme": "La procédure d'élaboration des lois",
      "type": "jeu",
      "format": "Fiche-jeu — 5 vrai/faux, corrigé inclus",
      "apercu": "Quiz officiel à imprimer : 5 affirmations vrai ou faux, chacune expliquée dans le corrigé.",
      "fichier": "jeu-que-sais-tu-elaboration-des-lois.pdf",
      "poids": "1,54 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/jeu-que%20sais-tu-sur-la-procedure-d-elaboration-des-lois-8-10_ans_0.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-comment-la-constitution-organise-la-procedure-d-elaboration-des-lois",
      "notions": [
        "Vrai ou faux",
        "Corrigé expliqué"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "valeurs-principes",
      "icone": "⚖️",
      "titre": "Les valeurs et principes de la République française",
      "salle": 5,
      "theme": "Les principes et valeurs de la République",
      "type": "fiche",
      "format": "Infographie — 1 page",
      "apercu": "Ce que disent les articles 1er et 2 de la Constitution : la devise et les grands principes.",
      "fichier": "valeurs-et-principes-de-la-republique.pdf",
      "poids": "1,13 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/Valeur_Principe_republique_8-10_ans.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-la-garantie-des-principes-et-valeurs-de-la-republique",
      "notions": [
        "Liberté, Égalité, Fraternité",
        "République indivisible, laïque, démocratique et sociale",
        "La laïcité et la loi de 1905"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "symboles",
      "icone": "🇫🇷",
      "titre": "Les symboles de la République française",
      "salle": 5,
      "theme": "Les principes et valeurs de la République",
      "type": "fiche",
      "format": "Infographie — 1 page",
      "apercu": "Les symboles inscrits dans la Constitution, et ceux qui n'y sont pas mais que tout le monde connaît.",
      "fichier": "c3-les-symboles-de-la-republique.pdf",
      "poids": "0,98 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-07/C3_Symbole_Republique.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-la-garantie-des-principes-et-valeurs-de-la-republique",
      "notions": [
        "La Marseillaise (1792)",
        "Le drapeau tricolore (1794)",
        "La devise (1848)",
        "Bonus : le coq, le 14 juillet, Marianne"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "libertes",
      "icone": "🕊️",
      "titre": "Les libertés en France",
      "salle": 5,
      "theme": "Les principes et valeurs de la République",
      "type": "fiche",
      "format": "Infographie — 1 page",
      "apercu": "Cinq libertés fondamentales expliquées avec des mots d'élèves.",
      "fichier": "les-libertes-en-france.pdf",
      "poids": "0,93 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/Libertes_en_France_8-10_ans.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-la-garantie-des-principes-et-valeurs-de-la-republique",
      "notions": [
        "Aller et venir",
        "Penser et s'exprimer",
        "Une presse libre",
        "Aimer librement",
        "Croire ou ne pas croire"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "quotidien",
      "icone": "🏠",
      "titre": "La Constitution au quotidien",
      "salle": 6,
      "theme": "Des exemples de la vie courante",
      "type": "fiche",
      "format": "Infographie — 1 page",
      "apercu": "Des situations de tous les jours où la Constitution s'applique vraiment.",
      "fichier": "la-constitution-au-quotidien.pdf",
      "poids": "1,36 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2023-09/la_constitution_dans_quotidien_8-10_ans.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-exemples-de-la-vie-courante",
      "notions": [
        "Travail et égalité des salaires",
        "Protection de l'environnement",
        "Vaccination obligatoire",
        "Internet et vie privée"
      ],
      "niveau": "CM1-CM2"
    },
    {
      "id": "theme8-quotidien",
      "icone": "📙",
      "titre": "La Constitution dans ta vie quotidienne (dossier)",
      "salle": 6,
      "theme": "Des exemples de la vie courante",
      "type": "fiche",
      "format": "Dossier élève — 3 pages",
      "apercu": "Le dossier complet du thème 8 : cinq domaines de la vie quotidienne, un par un.",
      "fichier": "c3-theme8-la-constitution-dans-ta-vie-quotidienne.pdf",
      "poids": "3,69 Mo",
      "url": "https://www.decouvronsnotreconstitution.fr/sites/default/files/2024-02/Cycle%203%20-%20Th%C3%A8me%208_0.pdf",
      "page": "https://www.decouvronsnotreconstitution.fr/8-10-ans-exemples-de-la-vie-courante",
      "notions": [
        "La santé et la Sécurité sociale",
        "L'école gratuite et laïque",
        "Le travail",
        "L'environnement",
        "Internet"
      ],
      "niveau": "CM1-CM2"
    }
  ]
};

let LECONS_DATA = null;
const DOSSIER_LECONS = "assets/lecons/";
const _presence = new Map();   // chemin -> true/false (une seule vérification par fichier)

async function chargerLecons(){
  if(LECONS_DATA) return LECONS_DATA;
  let fetchOk = false;
  try{
    const resp = await fetch("assets/data/lecons.json", {cache:"no-store"});
    if(resp.ok){ LECONS_DATA = await resp.json(); fetchOk = true; }
  }catch(e){
    console.warn("Fetch lecons.json échoué (mode file:// ?). Bascule sur la liste embarquée.");
  }
  if(!fetchOk || !LECONS_DATA || !LECONS_DATA.lecons){
    LECONS_DATA = JSON.parse(JSON.stringify(LECONS_FALLBACK));
  }
  return LECONS_DATA;
}

/* ---- Le fichier est-il présent dans assets/lecons/ ? ---- */
async function fichePresente(chemin){
  if(_presence.has(chemin)) return _presence.get(chemin);
  let ok = false;
  try{
    const r = await fetch(chemin, {method:"HEAD"});
    ok = r.ok;
  }catch(e){ ok = false; }        // file:// ou fichier absent
  _presence.set(chemin, ok);
  return ok;
}

const _echap = s => String(s==null?"":s).replace(/[&<>"']/g,
  c => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]));

/* ---- Ouvrir la bibliothèque ---- */
async function ouvrirBiblioLecons(){
  await chargerLecons();
  const overlay = document.getElementById("overlay-lecons");
  const corps   = document.getElementById("corps-lecons");
  const lecons  = LECONS_DATA.lecons || [];
  const salles  = LECONS_DATA.salles || {};
  const src     = LECONS_DATA.source_officielle || {};

  // Regroupement par salle, dans l'ordre des salles du jeu
  const groupes = [];
  lecons.forEach(l=>{
    const cle = String(l.salle || 0);
    let g = groupes.find(x=>x.cle===cle);
    if(!g){ g = {cle, titre: salles[cle] || ("Salle " + cle), items: []}; groupes.push(g); }
    g.items.push(l);
  });
  groupes.sort((a,b)=>Number(a.cle)-Number(b.cle));

  corps.innerHTML = `
    <p class="biblio-intro">Voici les <b>documents officiels</b> dont sont tirées toutes les énigmes du jeu.
    Clique sur une fiche pour la lire ; tu peux revenir au jeu quand tu veux.</p>
    ${groupes.map(g=>`
      <h4 class="biblio-salle">${_echap(g.titre)}</h4>
      <div class="biblio-grille">
        ${g.items.map(l=>`
          <div class="carte-lecon carte-doc" data-id="${_echap(l.id)}">
            <div class="icone">${l.icone||"📄"}</div>
            <div class="titre">${_echap(l.titre)}</div>
            <div class="doc-meta">
              <span class="badge-format ${l.type==="jeu"?"badge-jeu":""}">${l.type==="jeu"?"🎲 fiche-jeu":"📄 fiche"}</span>
              <span class="doc-format">${_echap(l.format||"")}</span>
            </div>
          </div>
        `).join("")}
      </div>
    `).join("")}
    <p class="doc-source-globale">${_echap(src.mention||"")}<br>
      <span>${_echap(src.illustrations||"")}</span></p>
  `;
  corps.querySelectorAll(".carte-lecon").forEach(c=>{
    c.addEventListener("click", ()=>afficherLecon(c.dataset.id));
  });
  overlay.classList.add("show");
  corps.scrollTop = 0;
}

/* ---- Afficher un document ---- */
async function afficherLecon(id){
  const lecon = (LECONS_DATA.lecons||[]).find(l=>l.id===id);
  if(!lecon) return;
  const corps = document.getElementById("corps-lecons");
  const src   = LECONS_DATA.source_officielle || {};
  const dossier = LECONS_DATA.dossier || DOSSIER_LECONS;
  const chemin  = dossier + lecon.fichier;

  const notions = (lecon.notions && lecon.notions.length)
    ? `<div class="encadre doc-notions"><b>📌 Dans ce document :</b>
         <ul>${lecon.notions.map(n=>`<li>${_echap(n)}</li>`).join("")}</ul></div>` : "";

  // Affichage provisoire pendant la vérification du fichier
  corps.innerHTML = `
    <div class="lecon-contenu">
      <button class="btn petit gris" id="btn-retour-biblio">← Retour aux documents</button>
      <h3 class="doc-titre">${lecon.icone||"📄"} ${_echap(lecon.titre)}</h3>
      <p class="doc-format-ligne">${_echap(lecon.format||"")} · ${_echap(lecon.poids||"")} ·
         <span class="doc-theme">${_echap(lecon.theme||"")}</span></p>
      <p class="doc-apercu">${_echap(lecon.apercu||"")}</p>
      ${notions}
      <div id="zone-doc" class="doc-zone"><p class="doc-attente">Ouverture du document…</p></div>
      <p class="doc-source">${_echap(src.mention||"")}<br>
         <span>${_echap(lecon.titre)} — extrait le ${_echap(src.date_extraction||"")}.
         ${_echap(src.illustrations||"")}</span></p>
    </div>
  `;
  document.getElementById("btn-retour-biblio").addEventListener("click", ouvrirBiblioLecons);
  corps.scrollTop = 0;

  const zone = document.getElementById("zone-doc");
  const presente = await fichePresente(chemin);
  if(presente){
    zone.innerHTML = `
      <object class="doc-visionneuse" data="${encodeURI(chemin)}#view=FitH" type="application/pdf">
        <p class="doc-repli">Votre navigateur n'affiche pas les PDF dans la page.
           Utilisez le bouton « Ouvrir le document » ci-dessous.</p>
      </object>
      <div class="doc-actions">
        <a class="btn petit" href="${encodeURI(chemin)}" target="_blank" rel="noopener">📖 Ouvrir en grand</a>
        <a class="btn petit gris" href="${encodeURI(chemin)}" download>⬇️ Télécharger</a>
        <a class="btn petit gris" href="${_echap(lecon.page||src.url||"")}" target="_blank" rel="noopener">🔗 Page officielle</a>
      </div>`;
  }else{
    zone.innerHTML = `
      <div class="doc-absent">
        <p><b>📥 Ce document n'est pas encore installé.</b></p>
        <p>Il reste consultable en ligne sur le site officiel. Pour l'avoir hors connexion,
           l'enseignant dépose le fichier <code>${_echap(lecon.fichier)}</code> dans
           <code>${_echap(dossier)}</code> (voir <code>assets/lecons/README.md</code>).</p>
        <div class="doc-actions">
          <a class="btn petit" href="${_echap(lecon.url||"")}" target="_blank" rel="noopener">📖 Lire la fiche officielle</a>
          <a class="btn petit gris" href="${_echap(lecon.page||src.url||"")}" target="_blank" rel="noopener">🔗 Page du site</a>
        </div>
      </div>`;
  }
}

/* ---- Liste des fiches (utilisée par les réglages et l'impression) ---- */
function listeFiches(){
  const d = LECONS_DATA || LECONS_FALLBACK;
  return (d.lecons || []).map(l => ({
    id: l.id, titre: l.titre, fichier: (d.dossier||DOSSIER_LECONS) + l.fichier,
    poids: l.poids, url: l.url, page: l.page, salle: l.salle, type: l.type
  }));
}

window.chargerLecons      = chargerLecons;
window.ouvrirBiblioLecons = ouvrirBiblioLecons;
window.afficherLecon      = afficherLecon;
window.listeFiches        = listeFiches;
window.fichePresente      = fichePresente;
