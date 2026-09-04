/* ============================================================
   RÉGLAGES — Module enseignant
   ⚙️ accessible depuis le HUD
   - Agrandissement des textes (accessibilité)
   - Voix ON/OFF, volume
   - Durée du minuteur
   - Leçons activées/désactivées
   - Clés API (Albert/DeepSeek)
   - Accès impression fiches & évaluations
   ============================================================ */

let EVAL_DATA = null;

async function chargerEvaluations(){
  if(EVAL_DATA) return EVAL_DATA;
  let fetchOk = false;
  try{
    const resp = await fetch("assets/data/evaluations.json", {cache:"no-store"});
    if(resp.ok){
      EVAL_DATA = await resp.json();
      fetchOk = true;
    }
  }catch(e){
    console.warn("Fetch evaluations.json échoué (mode file:// ?). Bascule sur évaluations embarquées.");
  }
  if(!fetchOk || !EVAL_DATA || !EVAL_DATA.qcm){
    EVAL_DATA = JSON.parse(JSON.stringify(EVAL_FALLBACK));
  }
  return EVAL_DATA;
}

/* ---- Évaluations embarquées minimales (fallback file://) ---- */
const EVAL_FALLBACK = {
  qcm: {
    CM1: [
      {q:"Quand a été adoptée la Déclaration des droits de l'homme et du citoyen ?", options:["14 juillet 1789","26 août 1789","21 janvier 1793"], bonne:1, pts:1},
      {q:"Qui prend la Bastille le 14 juillet 1789 ?", options:["Le roi et ses gardes","Le peuple parisien","L'armée anglaise"], bonne:1, pts:1},
      {q:"Comment s'appelle le roi de France en 1789 ?", options:["Louis XIV","Louis XVI","Napoléon"], bonne:1, pts:1},
      {q:"Quel symbole représente l'égalité ?", options:["La balance ⚖️","La couronne 👑","L'épée 🗡️"], bonne:0, pts:1}
    ],
    CM2: [
      {q:"Quand a été adoptée la DDHC ?", options:["14 juillet 1789","26 août 1789","5 octobre 1789"], bonne:1, pts:1},
      {q:"Quel événement a lieu le 20 juin 1789 ?", options:["La prise de la Bastille","Le serment du Jeu de paume","La marche des femmes"], bonne:1, pts:1},
      {q:"Combien d'articles comporte la DDHC de 1789 ?", options:["10","17","21"], bonne:1, pts:1},
      {q:"Qui a écrit la Déclaration des droits de la femme (1791) ?", options:["Marie-Antoinette","Olympe de Gouges","Charlotte Corday"], bonne:1, pts:1}
    ]
  },
  questions_fermees: {
    CM1: [
      {q:"Vrai ou faux : la Bastille était une forteresse-prison.", type:"vf", bonne:"vrai", pts:1},
      {q:"Vrai ou faux : Louis XVI était le roi en 1789.", type:"vf", bonne:"vrai", pts:1},
      {q:"Donne le nom du roi de France en 1789.", type:"court", rep:"Louis XVI", pts:1},
      {q:"Date de la prise de la Bastille.", type:"court", rep:"14 juillet 1789", pts:1}
    ],
    CM2: [
      {q:"Vrai ou faux : la DDHC comporte 17 articles.", type:"vf", bonne:"vrai", pts:1},
      {q:"Vrai ou faux : les femmes avaient le droit de vote en 1789.", type:"vf", bonne:"faux", pts:1},
      {q:"Donne la date exacte d'adoption de la DDHC.", type:"court", rep:"26 août 1789", pts:1},
      {q:"Qui a écrit la Déclaration des droits de la femme et de la citoyenne ?", type:"court", rep:"Olympe de Gouges", pts:1}
    ]
  },
  etudes_documents: {
    CM1: [
      {
        titre:"La prise de la Bastille", salle_concernee:4,
        document:{type:"texte", source:"Témoignage adapté, juillet 1789", contenu:"« Ce matin du 14 juillet, la foule parisienne marchait vers la Bastille. Cette grande forteresse-prison faisait peur à tous : on y enfermait les gens sur l'ordre du roi, sans jugement. Après des heures de combat, la porte s'est ouverte. La Bastille était prise ! »"},
        questions:[
          {q:"Quel événement est décrit ?", type:"court", rep:"La prise de la Bastille (14 juillet 1789)", pts:1},
          {q:"Pourquoi la Bastille faisait-elle peur ?", type:"court", rep:"On y enfermait sans jugement.", pts:1},
          {q:"Donne la date.", type:"court", rep:"14 juillet 1789", pts:1}
        ]
      }
    ],
    CM2: [
      {
        titre:"DDHC — Article 1", salle_concernee:3,
        document:{type:"texte", source:"DDHC, article 1, 26 août 1789", contenu:"« Les hommes naissent et demeurent libres et égaux en droits. Les distinctions sociales ne peuvent être fondées que sur l'utilité commune. »"},
        questions:[
          {q:"Quelle est la date de ce texte ?", type:"court", rep:"26 août 1789", pts:1},
          {q:"Reformule le premier phrase.", type:"ouverte", rep_attendue:"Tous les hommes sont libres dès leur naissance et ont les mêmes droits.", pts:2}
        ]
      }
    ]
  },
  fiches_preparatoires: [
    {salle:1, titre:"Le cahier de doléances", objectifs:["Comprendre ce qu'est un cahier de doléances","Connaître le rôle du Tiers État"], vocabulaire:[{mot:"Doléance",def:"Plainte, réclamation"},{mot:"Tiers État",def:"Le peuple (97 % des Français)"}], contexte:"Avant 1789, le roi demande à chaque région d'écrire un cahier avec les plaintes du peuple."},
    {salle:2, titre:"La chronologie de 1789", objectifs:["Mémoriser les dates-clés"], vocabulaire:[{mot:"États généraux",def:"Grande réunion des 3 ordres"},{mot:"Serment",def:"Promesse solennelle"}], contexte:"L'année 1789 est riche en événements qui s'enchaînent très vite."},
    {salle:3, titre:"La Déclaration des droits", objectifs:["Connaître l'article 1"], vocabulaire:[{mot:"Déclaration",def:"Texte qui affirme des principes"},{mot:"Droits",def:"Ce qui est garanti"}], contexte:"Le 26 août 1789, la DDHC est adoptée."},
    {salle:4, titre:"Les grands personnages", objectifs:["Identifier Louis XVI, Danton, Robespierre"], vocabulaire:[{mot:"Orateur",def:"Celui qui parle bien en public"},{mot:"Monarchie",def:"Régime dirigé par un roi"}], contexte:"Plusieurs personnages marquent la Révolution."},
    {salle:5, titre:"L'Assemblée nationale", objectifs:["Comprendre le rôle de l'Assemblée"], vocabulaire:[{mot:"Assemblée",def:"Réunion de députés qui votent les lois"},{mot:"Constitution",def:"Règles fondamentales d'un pays"}], contexte:"L'Assemblée siège à Versailles puis à Paris."}
  ]
};

function ouvrirReglages(){
  const overlay = document.getElementById("overlay-reglages");
  const corps = document.getElementById("corps-reglages");
  const r = ETAT.reglages;

  corps.innerHTML = `
    <div class="reglages-group">
      <h4>👤 Accessibilité</h4>
      <div class="reglage-ligne">
        <div class="libelle"><b>Agrandissement des textes</b><br><span style="font-size:.8rem;opacity:.7">Pour les élèves malvoyants</span></div>
        <div class="controle">
          <select id="reg-taille">
            <option value="1" ${r.tailleTexte==1?"selected":""}>Normal (100%)</option>
            <option value="1.15" ${r.tailleTexte==1.15?"selected":""}>Grand (115%)</option>
            <option value="1.3" ${r.tailleTexte==1.3?"selected":""}>Très grand (130%)</option>
            <option value="1.5" ${r.tailleTexte==1.5?"selected":""}>Très très grand (150%)</option>
          </select>
        </div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>🎬 Multimédia — décors filmés</h4>
      <p style="font-size:.85rem;opacity:.85;font-style:italic;margin-bottom:10px">
        Le jeu fonctionne <b>sans aucune vidéo</b> : les décors sont dessinés et animés
        dans le code. Si vous déposez vos propres fichiers, ils prennent automatiquement
        la place des dessins.
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
        <p style="margin:6px 0">Dans <code>assets/videos/</code>, nommés
        <code>salle1.mp4</code> … <code>salle5.mp4</code> (décors), plus
        <code>intro.mp4</code> et <code>final.mp4</code> (cinématiques).</p>
        <p style="margin:6px 0">Le dossier <code>Elements EG/Revolution fr/</code> est aussi
        exploré : le fichier <b>« Paris 1789.mp4 »</b> qui s'y trouve déjà est reconnu
        automatiquement comme décor de la <b>salle 1</b>.</p>
        <p style="margin:10px 0 4px"><b>Personnages</b> — vidéo en boucle ou image, dans
        <code>assets/videos/personnages/</code> ou <code>assets/images/personnages/</code> :
        <code>louise</code>, <code>gutenberg</code>, <code>marquis</code>, <code>maximilien</code>
        (+ une variante <code>&lt;nom&gt;-parle.mp4</code> facultative, jouée pendant qu'il parle).</p>
        <p style="margin:6px 0">Formats acceptés : <b>.mp4</b> ou <b>.webm</b>. Une image du même nom
        sert d'affiche et remplace la vidéo si celle-ci est absente. Des sous-titres
        <code>.vtt</code> du même nom sont chargés automatiquement.</p>
        <div class="boutons" style="margin-top:8px"><button class="btn petit bleu" id="btn-scan-medias">🔍 Vérifier les fichiers présents</button></div>
        <div id="resultat-scan" style="margin-top:8px"></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>🔊 Sons & voix</h4>
      <div class="reglage-ligne">
        <div class="libelle"><b>Voix des personnages</b><br><span style="font-size:.8rem;opacity:.7">Synthèse vocale française du navigateur</span></div>
        <div class="controle"><div class="bascule ${r.narrationActive?"actif":""}" id="reg-voix"></div></div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Volume des voix</b></div>
        <div class="controle"><input type="range" id="reg-volume" min="0" max="1" step="0.1" value="${r.volume}" style="width:120px"></div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Ambiances &amp; bruitages</b><br><span style="font-size:.8rem;opacity:.7">Pluie, imprimerie, foule, oiseaux, réussite… (générés par le navigateur, aucun fichier)</span></div>
        <div class="controle"><div class="bascule ${r.sonsActifs!==false?"actif":""}" id="reg-sons"></div></div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Volume des ambiances</b></div>
        <div class="controle"><input type="range" id="reg-volume-sons" min="0" max="1" step="0.05" value="${r.volumeSons!==undefined?r.volumeSons:0.55}" style="width:120px"></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>🎭 Personnages</h4>
      <div class="reglage-ligne">
        <div class="libelle"><b>Animations réduites</b><br><span style="font-size:.8rem;opacity:.7">Fige les mouvements de fond (respiration, balancement). Utile pour les élèves sensibles au mouvement ou en cas d'ordinateur lent.</span></div>
        <div class="controle"><div class="bascule ${r.animationsReduites?"actif":""}" id="reg-calme"></div></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>⏱️ Partie</h4>
      <div class="reglage-ligne">
        <div class="libelle"><b>Durée du minuteur</b><br><span style="font-size:.8rem;opacity:.7">Pour adapter à votre créneau</span></div>
        <div class="controle">
          <select id="reg-duree">
            <option value="30" ${r.dureeMin==30?"selected":""}>30 minutes</option>
            <option value="45" ${r.dureeMin==45?"selected":""}>45 minutes</option>
            <option value="55" ${r.dureeMin==55?"selected":""}>55 minutes (défaut)</option>
            <option value="60" ${r.dureeMin==60?"selected":""}>60 minutes</option>
          </select>
        </div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Bibliothèque de leçons 📚</b><br><span style="font-size:.8rem;opacity:.7">Accessible aux élèves pendant le jeu</span></div>
        <div class="controle"><div class="bascule ${r.leconsAutorisees?"actif":""}" id="reg-lecons"></div></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>🤖 IA optionnelle (avancé)</h4>
      <p style="font-size:.85rem;opacity:.8;font-style:italic;margin-bottom:10px">Si vous saisissez une clé API (Albert ou DeepSeek), les dialogues seront générés dynamiquement. Sans clé, le contenu statique reste utilisé (recommandé en classe).</p>
      <div class="reglage-ligne">
        <div class="libelle"><b>Activer l'IA en direct</b></div>
        <div class="controle"><div class="bascule ${r.apiActive?"actif":""}" id="reg-api"></div></div>
      </div>
      <div style="margin-top:8px">
        <label>Fournisseur</label>
        <select id="reg-api-fournisseur">
          <option value="deepseek" ${r.apiFournisseur=="deepseek"?"selected":""}>DeepSeek</option>
          <option value="albert" ${r.apiFournisseur=="albert"?"selected":""}>Albert (Service public français)</option>
        </select>
      </div>
      <div style="margin-top:8px">
        <label>Clé API (stockée localement sur ce poste uniquement)</label>
        <input type="password" id="reg-api-cle" placeholder="sk-..." value="${r.apiCle||""}" autocomplete="off">
      </div>
      <div class="boutons" style="margin-top:8px"><button class="btn petit bleu" id="btn-test-api">🔧 Tester la clé</button></div>
      <div id="fb-api" style="margin-top:8px"></div>
    </div>

    <div class="reglages-group">
      <h4>🖨️ Impressions A4</h4>
      <p style="font-size:.85rem;opacity:.8;font-style:italic;margin-bottom:10px">Fiches préparatoires et évaluations (avec corrigés séparés) prêtes à imprimer.</p>
      <div style="display:flex;flex-direction:column;gap:8px">
        <button class="btn bleu" id="btn-imprimer-prepa">📋 Fiches préparatoires (5 salles)</button>
        <button class="btn bleu" id="btn-imprimer-qcm">📝 QCM (15 questions)</button>
        <button class="btn bleu" id="btn-imprimer-fermees">✅ Questions fermées (V/F + réponses courtes)</button>
        <button class="btn bleu" id="btn-imprimer-docs">📄 Étude de documents</button>
        <button class="btn or" id="btn-imprimer-tout">📚 Tout imprimer (élève + corrigés)</button>
      </div>
    </div>

    <div class="boutons" style="margin-top:18px">
      <button class="btn vert" id="btn-sauver-reglages">💾 Enregistrer les réglages</button>
    </div>
  `;

  // Activer les bascules
  corps.querySelectorAll(".bascule").forEach(b=>{
    b.addEventListener("click", ()=>b.classList.toggle("actif"));
  });

  // Boutons impression
  corps.querySelector("#btn-imprimer-prepa").addEventListener("click", ()=>imprimerFiches("prepa"));
  corps.querySelector("#btn-imprimer-qcm").addEventListener("click", ()=>imprimerFiches("qcm"));
  corps.querySelector("#btn-imprimer-fermees").addEventListener("click", ()=>imprimerFiches("fermees"));
  corps.querySelector("#btn-imprimer-docs").addEventListener("click", ()=>imprimerFiches("docs"));
  corps.querySelector("#btn-imprimer-tout").addEventListener("click", ()=>imprimerFiches("tout"));

  // Test API
  corps.querySelector("#btn-test-api").addEventListener("click", testerAPI);
  corps.querySelector("#btn-scan-medias").addEventListener("click", scannerMedias);

  // Sauver
  corps.querySelector("#btn-sauver-reglages").addEventListener("click", sauverReglages);

  overlay.classList.add("show");
}

function sauverReglages(){
  const corps = document.getElementById("corps-reglages");
  ETAT.reglages.tailleTexte = parseFloat(corps.querySelector("#reg-taille").value);
  ETAT.reglages.narrationActive = corps.querySelector("#reg-voix").classList.contains("actif");
  ETAT.reglages.volume = parseFloat(corps.querySelector("#reg-volume").value);
  ETAT.reglages.sonsActifs = corps.querySelector("#reg-sons").classList.contains("actif");
  ETAT.reglages.volumeSons = parseFloat(corps.querySelector("#reg-volume-sons").value);
  ETAT.reglages.animationsReduites = corps.querySelector("#reg-calme").classList.contains("actif");
  ETAT.reglages.decorsVideo = corps.querySelector("#reg-video").classList.contains("actif");
  ETAT.reglages.sonVideo = corps.querySelector("#reg-video-son").classList.contains("actif");
  ETAT.reglages.cinematiques = corps.querySelector("#reg-cine").classList.contains("actif");
  ETAT.reglages.dureeMin = parseInt(corps.querySelector("#reg-duree").value);
  ETAT.reglages.leconsAutorisees = corps.querySelector("#reg-lecons").classList.contains("actif");
  ETAT.reglages.apiActive = corps.querySelector("#reg-api").classList.contains("actif");
  ETAT.reglages.apiFournisseur = corps.querySelector("#reg-api-fournisseur").value;
  ETAT.reglages.apiCle = corps.querySelector("#reg-api-cle").value;
  // Persister les réglages (indépendants de la partie)
  try{ localStorage.setItem("escape_reglages", JSON.stringify(ETAT.reglages)); }catch(e){}
  appliquerReglages();
  majHUD();
  // Le décor filmé doit être rechargé si le réglage vient de changer
  const scene = document.querySelector("#ecran-salle .scene, #scene-accueil");
  if(scene && typeof activerScene === "function" && ETAT.reglages.decorsVideo){
    activerScene(scene);
  }
  toast("Réglages enregistrés ✓");
  document.getElementById("overlay-reglages").classList.remove("show");
}

async function testerAPI(){
  const corps = document.getElementById("corps-reglages");
  const fournisseur = corps.querySelector("#reg-api-fournisseur").value;
  const cle = corps.querySelector("#reg-api-cle").value;
  const fb = corps.querySelector("#fb-api");
  if(!cle){ fb.innerHTML = '<div class="feedback erreur show">Veuillez saisir une clé.</div>'; return; }
  fb.innerHTML = '<div class="feedback indice show">Test en cours... <span class="spinner"></span></div>';
  try{
    const ok = await testerCleAPI(fournisseur, cle);
    if(ok){
      fb.innerHTML = '<div class="feedback succes show">✅ Clé valide ! L\'IA est prête.</div>';
    }else{
      fb.innerHTML = '<div class="feedback erreur show">❌ Clé invalide ou erreur. Vérifiez la clé et le fournisseur.</div>';
    }
  }catch(e){
    fb.innerHTML = '<div class="feedback erreur show">❌ Erreur réseau : '+e.message+'. (Hors-ligne ? L\'IA reste optionnelle.)</div>';
  }
}

/* ---- Inventaire des médias réellement présents ----
   Évite à l'enseignant de deviner pourquoi son fichier n'apparaît pas.
   Trois familles sont sondées : décors et cinématiques, personnages,
   cartes et illustrations. « Dessiné » n'est jamais une erreur : c'est
   le mode par défaut, entièrement jouable. */
async function scannerMedias(){
  const zone = document.getElementById("resultat-scan");
  zone.innerHTML = '<div class="feedback indice show">Recherche en cours… <span class="spinner"></span></div>';

  const CLAP = "🎬", IMAGE = "🖼️", CRAYON = "✏️";
  const ligne = (nom, etat) =>
    `<tr><td style="padding:4px">${nom}</td><td style="padding:4px">${etat}</td></tr>`;

  /* ---- Décors et cinématiques ---- */
  const decors = [
    {base:"intro", nom:"Cinématique d'ouverture"},
    {base:"salle1", nom:"Salle 1 · Palais-Royal"},
    {base:"salle2", nom:"Salle 2 · Imprimerie"},
    {base:"salle3", nom:"Salle 3 · Tuileries"},
    {base:"salle4", nom:"Salle 4 · Bastille"},
    {base:"salle5", nom:"Salle 5 · Assemblée"},
    {base:"final", nom:"Cinématique de fin"}
  ];
  /* Les trois familles sont sondées EN PARALLÈLE : sondées une à une,
     l'inventaire prenait une bonne vingtaine de secondes, ce qui est
     trop long pour un simple clic en classe. */
  const lignesDecor = (await Promise.all(decors.map(async d => {
    const m = await resoudreDecor(d.base);
    return ligne(d.nom,
      m.type === "video" ? CLAP + " vidéo trouvée"
    : m.type === "image" ? IMAGE + " image trouvée (pas de vidéo)"
                         : CRAYON + " décor dessiné (aucun fichier)");
  })));

  /* ---- Personnages ---- */
  const persos = [
    {base:"louise", nom:"Louise"},
    {base:"gutenberg", nom:"Maître Gutenberg"},
    {base:"marquis", nom:"Le Marquis de Montclair"},
    {base:"maximilien", nom:"Maximilien"}
  ];
  const lignesPerso = (await Promise.all(persos.map(async p => {
    const m = await resoudrePersonnage(p.base);
    return ligne(p.nom,
      m.type === "video" ? CLAP + " vidéo trouvée" + (m.srcParle ? " + variante « parle »" : "")
    : m.type === "image" ? IMAGE + " image trouvée"
                         : CRAYON + " personnage dessiné (aucun fichier)");
  })));

  /* ---- Cartes et illustrations ---- */
  const cartes = [
    /* aucune carte pour ce jeu */
  ];
  const lignesCarte = (await Promise.all(cartes.map(async c => {
    const url = await resoudreCarte(c.base);
    return ligne(c.nom,
      url ? IMAGE + " image trouvée" : CRAYON + " tracé dessiné (aucun fichier)");
  })));

  const tableau = (titre, corps) => corps ? `
    <table style="width:100%;font-size:.82rem;background:#fff;border-radius:8px;margin-bottom:8px">
      <tr><th style="text-align:left;padding:4px">${titre}</th><th style="text-align:left;padding:4px">État</th></tr>
      ${corps}
    </table>` : "";

  zone.innerHTML =
      tableau("Décors et cinématiques", lignesDecor.join(""))
    + tableau("Personnages", lignesPerso.join(""))
    + tableau("Cartes et illustrations", lignesCarte.join(""))
    + `<p style="font-size:.78rem;opacity:.7;margin-top:6px">
        « Dessiné » n'est pas une erreur : c'est le mode par défaut, entièrement jouable.</p>`;
}
window.scannerMedias = scannerMedias;
window.ouvrirReglages = ouvrirReglages;
window.sauverReglages = sauverReglages;
window.testerAPI = testerAPI;
window.chargerEvaluations = chargerEvaluations;
