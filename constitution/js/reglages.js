/* ============================================================
   RÉGLAGES — Module enseignant (⚙️ dans le HUD)
   - Accessibilité (taille des textes, animations réduites)
   - Multimédia : décors filmés, son, cinématiques, inventaire
   - Sons et voix
   - Durée de la séance, fiches officielles
   - CONCOURS « Découvrons notre Constitution » (facultatif)
   - IA facultative (Albert / DeepSeek)
   - Impressions A4 (fiches, évaluations, corrigés)
   ============================================================ */

/* Partagé avec impression.js et app.js : déclaré en var + exposé sur window,
   pour rester accessible quel que soit l'ordre de chargement des scripts. */
var EVAL_DATA = null;

async function chargerEvaluations(){
  if(EVAL_DATA) return EVAL_DATA;
  let ok = false;
  try{
    const r = await fetch("assets/data/evaluations.json", {cache:"no-store"});
    if(r.ok){ EVAL_DATA = await r.json(); ok = true; }
  }catch(e){
    console.warn("Fetch evaluations.json échoué (mode file:// ?). Bascule sur les évaluations embarquées.");
  }
  if(!ok || !EVAL_DATA || !EVAL_DATA.qcm) EVAL_DATA = JSON.parse(JSON.stringify(EVAL_FALLBACK));
  window.EVAL_DATA = EVAL_DATA;
  return EVAL_DATA;
}

/* ---- Évaluations embarquées minimales (secours file://) ---- */
const EVAL_FALLBACK = {
  qcm: {
    CM1: [
      {q:"Qu'est-ce qu'une Constitution ?", options:["Le règlement d'une école","L'ensemble des règles qui organisent un pays","La liste des habitants d'une ville"], bonne:1, pts:1},
      {q:"En quelle année la Constitution actuelle a-t-elle été promulguée ?", options:["1789","1958","2004"], bonne:1, pts:1},
      {q:"Qui vote les lois ?", options:["Le Parlement","Le président seul","Les juges"], bonne:0, pts:1},
      {q:"Combien de membres compte le Conseil constitutionnel ?", options:["5","9","15"], bonne:1, pts:1}
    ],
    CM2: [
      {q:"Quels textes forment le bloc de constitutionnalité avec la Constitution de 1958 ?", options:["La DDHC de 1789, le Préambule de 1946 et la Charte de l'environnement","Le Code civil et le Code pénal","Les traités européens"], bonne:0, pts:1},
      {q:"Combien de députés siègent à l'Assemblée nationale ?", options:["348","577","925"], bonne:1, pts:1},
      {q:"Combien de temps le président a-t-il pour promulguer une loi ?", options:["48 heures","15 jours","3 mois"], bonne:1, pts:1},
      {q:"Comment les sénateurs sont-ils élus ?", options:["Au suffrage universel direct","Au suffrage universel indirect","Ils sont nommés"], bonne:1, pts:1}
    ]
  },
  questions_fermees: {
    CM1: [
      {q:"Vrai ou faux : la Constitution est au-dessus de toutes les lois.", type:"vf", bonne:"vrai", pts:1},
      {q:"Donne la date de promulgation de la Constitution actuelle.", type:"court", rep:"4 octobre 1958", pts:1}
    ],
    CM2: [
      {q:"Vrai ou faux : le Conseil constitutionnel peut contrôler une loi déjà en vigueur.", type:"vf", bonne:"vrai", pts:1},
      {q:"Quel délai le président a-t-il pour promulguer une loi ?", type:"court", rep:"Quinze jours", pts:1}
    ]
  },
  etudes_documents: {CM1:[], CM2:[]},
  fiches_preparatoires: [
    {salle:1, titre:"Qu'est-ce qu'une Constitution ?", objectifs:["Définir une Constitution"],
     vocabulaire:[{mot:"Constitution", def:"Ensemble des règles qui organisent un pays"}],
     contexte:"Le Conseil constitutionnel siège au Palais-Royal, à Paris."}
  ]
};

/* ---- Les emplacements médias du jeu ----
   Un seul nom par emplacement : déposez le fichier, il apparaît. */
const MEDIA_DECORS = [
  {base:"intro",  nom:"Cinématique d'ouverture"},
  {base:"salle1", nom:"Salle 1 · La cour du Palais-Royal"},
  {base:"salle2", nom:"Salle 2 · La salle des Textes"},
  {base:"salle3", nom:"Salle 3 · L'hémicycle"},
  {base:"salle4", nom:"Salle 4 · La navette parlementaire"},
  {base:"salle5", nom:"Salle 5 · La salle des séances"},
  {base:"final",  nom:"Cinématique de fin"}
];
const MEDIA_PERSOS = [
  {base:"berthier", nom:"Monsieur Berthier (gardien-archiviste)"},
  {base:"nour",     nom:"Nour (déléguée de classe)"},
  {base:"ferrand",  nom:"Madame Ferrand (députée)"},
  {base:"sylla",    nom:"Maître Sylla (juriste)"}
];
/* Illustrations d'énigmes : lues dans enigmes.json (champ "media"). */
function mediaEnigmes(){
  const liste = [];
  const src = (typeof ENIGMES === "function" ? ENIGMES() : null);
  if(!src || !src.salles) return liste;
  src.salles.forEach(s=>(s.enigmes||[]).forEach(e=>{
    if(e.media && e.media.base) liste.push({base:e.media.base, nom:`Énigme ${e.id} · ${e.titre}`});
  }));
  return liste;
}

function ouvrirReglages(){
  const overlay = document.getElementById("overlay-reglages");
  const corps = document.getElementById("corps-reglages");
  const r = ETAT.reglages;

  corps.innerHTML = `
    <div class="reglages-group">
      <h4>👤 Accessibilité</h4>
      <div class="reglage-ligne">
        <div class="libelle"><b>Agrandissement des textes</b><br><span style="font-size:.8rem;opacity:.7">Pour les élèves malvoyants, ou pour une projection au TBI</span></div>
        <div class="controle">
          <select id="reg-taille">
            <option value="1" ${r.tailleTexte==1?"selected":""}>Normal (100 %)</option>
            <option value="1.15" ${r.tailleTexte==1.15?"selected":""}>Grand (115 %)</option>
            <option value="1.3" ${r.tailleTexte==1.3?"selected":""}>Très grand (130 %)</option>
            <option value="1.5" ${r.tailleTexte==1.5?"selected":""}>Très très grand (150 %)</option>
          </select>
        </div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Animations réduites</b><br><span style="font-size:.8rem;opacity:.7">Fige les mouvements de fond et les vidéos. Utile pour les élèves sensibles au mouvement ou sur un poste lent.</span></div>
        <div class="controle"><div class="bascule ${r.animationsReduites?"actif":""}" id="reg-calme"></div></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>🏛️ Concours « Découvrons notre Constitution »</h4>
      <p style="font-size:.85rem;opacity:.85;font-style:italic;margin-bottom:10px">
        <b>Désactivé par défaut.</b> Une fois activé, un encart apparaît <b>à la toute fin</b> de la partie,
        après le bilan : présentation du concours national, calendrier officiel, liens vers le règlement
        et fiche de projet à imprimer. Le jeu reste entièrement jouable sans cette option.
        Le contenu de l'encart se met à jour dans <code>assets/data/concours.json</code>.
      </p>
      <div class="reglage-ligne">
        <div class="libelle"><b>Annoncer le concours en fin de partie</b><br><span style="font-size:.8rem;opacity:.7">Participation facultative, collective, du CM1 au lycée</span></div>
        <div class="controle"><div class="bascule ${r.concoursActif?"actif":""}" id="reg-concours"></div></div>
      </div>
      <div class="boutons" style="margin-top:8px">
        <button class="btn petit bleu" id="btn-apercu-concours">👁️ Aperçu de l'encart</button>
        <button class="btn petit or" id="btn-fiche-concours-reglages">🖨️ Fiche de projet</button>
      </div>
      <div id="apercu-concours" style="margin-top:8px"></div>
    </div>

    <div class="reglages-group">
      <h4>🎬 Multimédia — images et vidéos</h4>
      <p style="font-size:.85rem;opacity:.85;font-style:italic;margin-bottom:10px">
        Le jeu fonctionne <b>sans aucun fichier</b> : décors et personnages sont dessinés et animés
        dans le code. Si vous déposez vos propres fichiers, ils prennent automatiquement la place des dessins.
      </p>
      <div class="reglage-ligne">
        <div class="libelle"><b>Décors vidéo</b><br><span style="font-size:.8rem;opacity:.7">Utiliser les vidéos si elles sont présentes</span></div>
        <div class="controle"><div class="bascule ${r.decorsVideo!==false?"actif":""}" id="reg-video"></div></div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Son des décors vidéo</b><br><span style="font-size:.8rem;opacity:.7">Désactivé par défaut : évite de couvrir la voix des personnages</span></div>
        <div class="controle"><div class="bascule ${r.sonVideo?"actif":""}" id="reg-video-son"></div></div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Cinématiques d'intro et de fin</b><br><span style="font-size:.8rem;opacity:.7">Séquences plein écran, avec bouton « Passer »</span></div>
        <div class="controle"><div class="bascule ${r.cinematiques!==false?"actif":""}" id="reg-cine"></div></div>
      </div>
      <div style="background:#fff8e6;border:1px solid var(--parchemin-ombre);border-radius:10px;padding:12px;margin-top:10px;font-size:.85rem">
        <b>📁 Où déposer vos fichiers ?</b>
        <p style="margin:6px 0"><b>Décors et cinématiques</b> — <code>assets/videos/</code> :
        <code>salle1.mp4</code> … <code>salle5.mp4</code>, plus <code>intro.mp4</code> et <code>final.mp4</code>.
        Une image du même nom dans <code>assets/images/decors/</code> sert d'affiche, ou remplace la vidéo absente.</p>
        <p style="margin:6px 0"><b>Personnages</b> — <code>assets/videos/personnages/</code> ou
        <code>assets/images/personnages/</code> : <code>berthier</code>, <code>nour</code>,
        <code>ferrand</code>, <code>sylla</code> (+ une variante <code>&lt;nom&gt;-parle.mp4</code>
        facultative, jouée pendant qu'il parle).</p>
        <p style="margin:6px 0"><b>Illustrations d'énigmes</b> — <code>assets/images/cartes/</code> :
        les noms sont listés dans l'inventaire ci-dessous et dans <code>assets/README.md</code>.</p>
        <p style="margin:6px 0">Formats : <b>.mp4</b> ou <b>.webm</b> pour la vidéo, <b>.jpg</b>, <b>.png</b>
        ou <b>.webp</b> pour l'image. Noms en minuscules, sans espace ni accent. Des sous-titres
        <code>.vtt</code> du même nom que la vidéo sont chargés automatiquement.</p>
        <div class="boutons" style="margin-top:8px"><button class="btn petit bleu" id="btn-scan-medias">🔍 Vérifier les fichiers présents</button></div>
        <div id="resultat-scan" style="margin-top:8px"></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>🔊 Sons &amp; voix</h4>
      <div class="reglage-ligne">
        <div class="libelle"><b>Voix des personnages</b><br><span style="font-size:.8rem;opacity:.7">Synthèse vocale française du navigateur</span></div>
        <div class="controle"><div class="bascule ${r.narrationActive?"actif":""}" id="reg-voix"></div></div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Volume des voix</b></div>
        <div class="controle"><input type="range" id="reg-volume" min="0" max="1" step="0.1" value="${r.volume}" style="width:120px"></div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Ambiances &amp; bruitages</b><br><span style="font-size:.8rem;opacity:.7">Générés par le navigateur, aucun fichier à télécharger</span></div>
        <div class="controle"><div class="bascule ${r.sonsActifs!==false?"actif":""}" id="reg-sons"></div></div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Volume des ambiances</b></div>
        <div class="controle"><input type="range" id="reg-volume-sons" min="0" max="1" step="0.05" value="${r.volumeSons!==undefined?r.volumeSons:0.55}" style="width:120px"></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>⏱️ Séance</h4>
      <div class="reglage-ligne">
        <div class="libelle"><b>Durée du minuteur</b><br><span style="font-size:.8rem;opacity:.7">Pour adapter à votre créneau. Le minuteur n'arrête jamais la partie : il vire au rouge 5 minutes avant la fin.</span></div>
        <div class="controle">
          <select id="reg-duree">
            <option value="45" ${r.dureeMin==45?"selected":""}>45 minutes</option>
            <option value="60" ${r.dureeMin==60?"selected":""}>60 minutes (défaut)</option>
            <option value="75" ${r.dureeMin==75?"selected":""}>75 minutes</option>
            <option value="90" ${r.dureeMin==90?"selected":""}>90 minutes</option>
          </select>
        </div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Fiches officielles 📚</b><br><span style="font-size:.8rem;opacity:.7">Les documents du Conseil constitutionnel, consultables pendant la partie</span></div>
        <div class="controle"><div class="bascule ${r.leconsAutorisees?"actif":""}" id="reg-lecons"></div></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>🤖 IA facultative (avancé)</h4>
      <p style="font-size:.85rem;opacity:.8;font-style:italic;margin-bottom:10px">Avec une clé API (Albert ou DeepSeek), les dialogues d'introduction sont générés à la volée. Sans clé, les textes écrits sont utilisés — c'est le mode recommandé en classe.</p>
      <div class="reglage-ligne">
        <div class="libelle"><b>Activer l'IA en direct</b></div>
        <div class="controle"><div class="bascule ${r.apiActive?"actif":""}" id="reg-api"></div></div>
      </div>
      <div style="margin-top:8px">
        <label>Fournisseur</label>
        <select id="reg-api-fournisseur">
          <option value="deepseek" ${r.apiFournisseur=="deepseek"?"selected":""}>DeepSeek</option>
          <option value="albert" ${r.apiFournisseur=="albert"?"selected":""}>Albert (service public français)</option>
        </select>
      </div>
      <div style="margin-top:8px">
        <label>Clé API (stockée sur ce poste uniquement)</label>
        <input type="password" id="reg-api-cle" placeholder="sk-..." value="${r.apiCle||""}" autocomplete="off">
      </div>
      <div class="boutons" style="margin-top:8px"><button class="btn petit bleu" id="btn-test-api">🔧 Tester la clé</button></div>
      <div id="fb-api" style="margin-top:8px"></div>
    </div>

    <div class="reglages-group">
      <h4>🖨️ Impressions A4</h4>
      <p style="font-size:.85rem;opacity:.8;font-style:italic;margin-bottom:10px">Fiches préparatoires et évaluations, corrigés séparés, prêts à imprimer.</p>
      <div style="display:flex;flex-direction:column;gap:8px">
        <button class="btn bleu" id="btn-imprimer-prepa">📋 Fiches préparatoires (5 salles)</button>
        <button class="btn bleu" id="btn-imprimer-qcm">📝 QCM</button>
        <button class="btn bleu" id="btn-imprimer-fermees">✅ Vrai/Faux et réponses courtes</button>
        <button class="btn bleu" id="btn-imprimer-docs">📄 Étude de documents</button>
        <button class="btn or" id="btn-imprimer-tout">📚 Tout imprimer (élève + corrigés)</button>
      </div>
    </div>

    <div class="boutons" style="margin-top:18px">
      <button class="btn vert" id="btn-sauver-reglages">💾 Enregistrer les réglages</button>
    </div>
  `;

  corps.querySelectorAll(".bascule").forEach(b=>b.addEventListener("click", ()=>b.classList.toggle("actif")));
  corps.querySelector("#btn-imprimer-prepa").addEventListener("click", ()=>imprimerFiches("prepa"));
  corps.querySelector("#btn-imprimer-qcm").addEventListener("click", ()=>imprimerFiches("qcm"));
  corps.querySelector("#btn-imprimer-fermees").addEventListener("click", ()=>imprimerFiches("fermees"));
  corps.querySelector("#btn-imprimer-docs").addEventListener("click", ()=>imprimerFiches("docs"));
  corps.querySelector("#btn-imprimer-tout").addEventListener("click", ()=>imprimerFiches("tout"));
  corps.querySelector("#btn-test-api").addEventListener("click", testerAPI);
  corps.querySelector("#btn-scan-medias").addEventListener("click", scannerMedias);
  corps.querySelector("#btn-fiche-concours-reglages").addEventListener("click", imprimerFicheConcours);
  corps.querySelector("#btn-apercu-concours").addEventListener("click", apercuConcours);
  corps.querySelector("#btn-sauver-reglages").addEventListener("click", sauverReglages);

  overlay.classList.add("show");
}

/* ---- Aperçu de l'encart concours, sans lancer une partie ---- */
function apercuConcours(){
  const zone = document.getElementById("apercu-concours");
  const c = donneesConcours();
  zone.innerHTML = `
    <div class="encart-concours" style="margin:0">
      <h3>🏛️ ${c.nom} — session ${c.session}</h3>
      <p>Thème : <b>« ${c.theme} »</b> · catégorie <b>${c.categorie_visee}</b> · participation ${c.participation}.</p>
      <div class="dates">${(c.dates||[]).map(d=>`<div class="date-case"><b>${d.quoi}</b>${d.quand}</div>`).join("")}</div>
      <p class="avert">⚠️ ${c.avertissement}</p>
    </div>`;
}

function sauverReglages(){
  const corps = document.getElementById("corps-reglages");
  const R = ETAT.reglages;
  R.tailleTexte       = parseFloat(corps.querySelector("#reg-taille").value);
  R.animationsReduites= corps.querySelector("#reg-calme").classList.contains("actif");
  R.concoursActif     = corps.querySelector("#reg-concours").classList.contains("actif");
  R.decorsVideo       = corps.querySelector("#reg-video").classList.contains("actif");
  R.sonVideo          = corps.querySelector("#reg-video-son").classList.contains("actif");
  R.cinematiques      = corps.querySelector("#reg-cine").classList.contains("actif");
  R.narrationActive   = corps.querySelector("#reg-voix").classList.contains("actif");
  R.volume            = parseFloat(corps.querySelector("#reg-volume").value);
  R.sonsActifs        = corps.querySelector("#reg-sons").classList.contains("actif");
  R.volumeSons        = parseFloat(corps.querySelector("#reg-volume-sons").value);
  R.dureeMin          = parseInt(corps.querySelector("#reg-duree").value);
  R.leconsAutorisees  = corps.querySelector("#reg-lecons").classList.contains("actif");
  R.apiActive         = corps.querySelector("#reg-api").classList.contains("actif");
  R.apiFournisseur    = corps.querySelector("#reg-api-fournisseur").value;
  R.apiCle            = corps.querySelector("#reg-api-cle").value;
  try{ localStorage.setItem("escape_reglages_constitution", JSON.stringify(R)); }catch(e){}
  appliquerReglages();
  majHUD();
  const scene = document.querySelector("#ecran-salle .scene, #scene-accueil");
  if(scene && typeof activerScene === "function" && R.decorsVideo) activerScene(scene);
  toast("Réglages enregistrés ✓");
  document.getElementById("overlay-reglages").classList.remove("show");
}

async function testerAPI(){
  const corps = document.getElementById("corps-reglages");
  const fournisseur = corps.querySelector("#reg-api-fournisseur").value;
  const cle = corps.querySelector("#reg-api-cle").value;
  const fb = corps.querySelector("#fb-api");
  if(!cle){ fb.innerHTML = '<div class="feedback erreur show">Veuillez saisir une clé.</div>'; return; }
  fb.innerHTML = '<div class="feedback indice show">Test en cours… <span class="spinner"></span></div>';
  try{
    const ok = await testerCleAPI(fournisseur, cle);
    fb.innerHTML = ok
      ? '<div class="feedback succes show">✅ Clé valide : l\'IA est prête.</div>'
      : '<div class="feedback erreur show">❌ Clé invalide ou erreur. Vérifiez la clé et le fournisseur.</div>';
  }catch(e){
    fb.innerHTML = '<div class="feedback erreur show">❌ Erreur réseau : '+e.message+'. (Hors-ligne ? L\'IA reste facultative.)</div>';
  }
}

/* ---- Inventaire des médias réellement présents ----
   « Dessiné » n'est jamais une erreur : c'est le mode par défaut. ---- */
async function scannerMedias(){
  const zone = document.getElementById("resultat-scan");
  zone.innerHTML = '<div class="feedback indice show">Recherche en cours… <span class="spinner"></span></div>';
  const CLAP = "🎬", IMAGE = "🖼️", CRAYON = "✏️";
  const ligne = (nom, etat, fichier) =>
    `<tr><td style="padding:4px">${nom}</td><td style="padding:4px">${etat}</td><td style="padding:4px"><code style="font-size:.78rem">${fichier}</code></td></tr>`;

  const lignesDecor = (await Promise.all(MEDIA_DECORS.map(async d=>{
    const m = await resoudreDecor(d.base);
    return ligne(d.nom,
      m.type === "video" ? CLAP + " vidéo trouvée"
    : m.type === "image" ? IMAGE + " image trouvée (pas de vidéo)"
                         : CRAYON + " décor dessiné (aucun fichier)",
      "assets/videos/"+d.base+".mp4");
  })));

  const lignesPerso = (await Promise.all(MEDIA_PERSOS.map(async p=>{
    const m = await resoudrePersonnage(p.base);
    return ligne(p.nom,
      m.type === "video" ? CLAP + " vidéo trouvée" + (m.srcParle ? " + variante « parle »" : "")
    : m.type === "image" ? IMAGE + " image trouvée"
                         : CRAYON + " personnage dessiné (aucun fichier)",
      "assets/images/personnages/"+p.base+".png");
  })));

  /* Fiches officielles (leçons) : présentes dans assets/lecons/ ou lues en ligne */
  let lignesFiches = "";
  try{
    const donnees = await chargerLecons();
    const dossier = donnees.dossier || "assets/lecons/";
    lignesFiches = (await Promise.all((donnees.lecons||[]).map(async l=>{
      const presente = await fichePresente(dossier + l.fichier);
      return ligne((l.type==="jeu" ? "🎲 " : "📄 ") + l.titre,
        presente ? "📄 fiche installée (hors connexion)"
                 : "🔗 lien vers le site officiel (fichier absent)",
        dossier + l.fichier);
    }))).join("");
  }catch(e){ lignesFiches = ""; }

  const enig = mediaEnigmes();
  const lignesEnig = (await Promise.all(enig.map(async c=>{
    const url = await resoudreCarte(c.base);
    return ligne(c.nom, url ? IMAGE + " image trouvée" : CRAYON + " aucune image (l'énigme reste jouable)",
      "assets/images/cartes/"+c.base+".jpg");
  })));

  const tableau = (titre, corps) => corps ? `
    <table style="width:100%;font-size:.82rem;background:#fff;border-radius:8px;margin-bottom:8px">
      <tr><th style="text-align:left;padding:4px">${titre}</th><th style="text-align:left;padding:4px">État</th><th style="text-align:left;padding:4px">Nom attendu</th></tr>
      ${corps}
    </table>` : "";

  zone.innerHTML =
      tableau("Décors et cinématiques", lignesDecor.join(""))
    + tableau("Personnages", lignesPerso.join(""))
    + tableau("Illustrations d'énigmes", lignesEnig.join(""))
    + tableau("Fiches officielles (leçons 📚)", lignesFiches)
    + `<p style="font-size:.78rem;opacity:.7;margin-top:6px">
        « Dessiné » n'est pas une erreur : c'est le mode par défaut, entièrement jouable.
        Une fiche « absente » n'est pas une erreur non plus : la leçon ouvre alors le document sur le site du Conseil constitutionnel.
        Pour les installer hors connexion : <code>assets/lecons/telecharger-fiches.bat</code>.
        Les erreurs 404 visibles dans la console (F12) sont normales : le jeu cherche les fichiers que vous pourriez déposer.</p>`;
}

window.scannerMedias      = scannerMedias;
window.ouvrirReglages     = ouvrirReglages;
window.sauverReglages     = sauverReglages;
window.testerAPI          = testerAPI;
window.chargerEvaluations = chargerEvaluations;
window.EVAL_FALLBACK      = EVAL_FALLBACK;
window.apercuConcours     = apercuConcours;
