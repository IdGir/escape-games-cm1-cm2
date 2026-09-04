/* ============================================================
   RÉGLAGES — Module enseignant  (⚙️ dans le HUD)
   - Accessibilité (taille des textes, animations réduites)
   - Voix, ambiances sonores
   - MULTIMÉDIA : décors vidéo, son des vidéos, cinématiques
   - Durée de la partie, bibliothèque de leçons
   - IA optionnelle
   - Impressions A4 (fiches + évaluations + corrigés)
   ============================================================ */

let EVAL_DATA = null;

async function chargerEvaluations(){
  if(EVAL_DATA) return EVAL_DATA;
  let ok = false;
  try{
    const resp = await fetch("assets/data/evaluations.json", {cache:"no-store"});
    if(resp.ok){ EVAL_DATA = await resp.json(); ok = true; }
  }catch(e){
    console.warn("Fetch evaluations.json impossible (file:// ?) — évaluations embarquées.");
  }
  if(!ok || !EVAL_DATA || !EVAL_DATA.qcm){
    EVAL_DATA = JSON.parse(JSON.stringify(EVAL_FALLBACK));
  }
  return EVAL_DATA;
}

/* ---- Évaluations embarquées (fallback file://) ---- */
const EVAL_FALLBACK = {
  qcm: {
    CM1: [
      {q:"Combien y a-t-il de continents sur Terre ?", options:["5","6","10"], bonne:1, pts:1},
      {q:"Quel est le plus grand océan du monde ?", options:["Atlantique","Indien","Pacifique"], bonne:2, pts:1},
      {q:"Quelle ligne imaginaire coupe la Terre en deux moitiés égales ?", options:["L'équateur","Le méridien","Le tropique"], bonne:0, pts:1},
      {q:"Sur une carte, où se trouve le nord ?", options:["En bas","En haut","À droite"], bonne:1, pts:1},
      {q:"Dans un désert, le climat est…", options:["Chaud et sec","Froid et humide","Doux et pluvieux"], bonne:0, pts:1}
    ],
    CM2: [
      {q:"Le canal de Suez relie la Méditerranée à…", options:["la mer Rouge","la mer Noire","la Baltique"], bonne:0, pts:1},
      {q:"En combien de fuseaux horaires la Terre est-elle découpée ?", options:["12","24","36"], bonne:1, pts:1},
      {q:"Le méridien de référence (longitude 0°) passe par…", options:["Paris","Greenwich","Rome"], bonne:1, pts:1},
      {q:"Quel continent est situé au pôle Sud ?", options:["L'Océanie","L'Antarctique","L'Amérique du Sud"], bonne:1, pts:1},
      {q:"Sur une carte au 1 cm = 200 km, un trajet de 7 cm représente…", options:["700 km","1 400 km","200 km"], bonne:1, pts:1},
      {q:"Un climat équatorial est…", options:["chaud et humide toute l'année","froid et sec","tempéré"], bonne:0, pts:1}
    ]
  },
  questions_fermees: {
    CM1: [
      {q:"Vrai ou faux : l'océan Pacifique est le plus grand océan du monde.", type:"vf", bonne:"vrai", pts:1},
      {q:"Vrai ou faux : l'Europe est plus grande que l'Asie.", type:"vf", bonne:"faux", pts:1},
      {q:"Cite les quatre points cardinaux.", type:"court", rep:"Nord, Sud, Est, Ouest", pts:2},
      {q:"Sur quel continent se trouve la France ?", type:"court", rep:"L'Europe", pts:1},
      {q:"Comment s'appelle la ligne imaginaire qui fait le tour de la Terre à égale distance des deux pôles ?", type:"court", rep:"L'équateur", pts:1}
    ],
    CM2: [
      {q:"Vrai ou faux : le méridien de Greenwich sert de référence pour les longitudes.", type:"vf", bonne:"vrai", pts:1},
      {q:"Vrai ou faux : en allant vers l'ouest, on ajoute des heures.", type:"vf", bonne:"faux", pts:1},
      {q:"Cite les cinq océans du monde.", type:"court", rep:"Pacifique, Atlantique, Indien, Arctique, Austral", pts:2},
      {q:"S'il est midi à Londres, quelle heure est-il à Paris (+1 h) ?", type:"court", rep:"13 h", pts:1},
      {q:"Explique pourquoi Phileas Fogg a gagné un jour.", type:"ouverte", rep_attendue:"En voyageant vers l'est, il a franchi les 24 fuseaux horaires en ajoutant une heure à chaque fois, soit 24 heures : un jour de plus que les Londoniens.", pts:2}
    ]
  },
  etudes_documents: {
    CM1: [
      {
        titre:"Lire un planisphère", salle_concernee:1,
        document:{type:"texte", source:"Manuel de géographie, cycle 3",
          contenu:"« Un planisphère est une carte qui représente toute la Terre à plat. On y voit les six continents — Europe, Asie, Afrique, Amérique du Nord, Amérique du Sud, Océanie et Antarctique — séparés par les océans. Une ligne horizontale, l'équateur, partage la Terre en deux moitiés : l'hémisphère nord et l'hémisphère sud. »"},
        questions:[
          {q:"Qu'est-ce qu'un planisphère ?", type:"court", rep:"Une carte qui représente toute la Terre à plat.", pts:1},
          {q:"Comment s'appelle la ligne qui partage la Terre en deux moitiés ?", type:"court", rep:"L'équateur", pts:1},
          {q:"Nomme trois continents.", type:"court", rep:"Réponses variées : Europe, Afrique, Asie…", pts:1}
        ]
      }
    ],
    CM2: [
      {
        titre:"Le dernier chapitre du Tour du monde", salle_concernee:5,
        document:{type:"texte", source:"Jules Verne, Le Tour du monde en quatre-vingts jours, 1873 (extrait adapté)",
          contenu:"« En se dirigeant vers l'est, Phileas Fogg allait au-devant du soleil, et les jours diminuaient pour lui d'autant de fois quatre minutes qu'il franchissait de degrés. Or, il y a trois cent soixante degrés sur la circonférence terrestre, ce qui donne vingt-quatre heures — c'est-à-dire ce jour gagné à son insu. »"},
        questions:[
          {q:"Dans quel sens Phileas Fogg a-t-il voyagé ?", type:"court", rep:"Vers l'est", pts:1},
          {q:"Combien de degrés compte la circonférence de la Terre ?", type:"court", rep:"360 degrés", pts:1},
          {q:"Explique avec tes mots pourquoi il a gagné un jour.", type:"ouverte", rep_attendue:"Chaque degré parcouru vers l'est fait gagner 4 minutes ; 360 × 4 minutes = 1440 minutes = 24 heures, soit un jour entier.", pts:2}
        ]
      }
    ]
  },
  fiches_preparatoires: [
    {salle:1, titre:"Le planisphère : continents et océans",
     objectifs:["Nommer et situer les 6 continents","Nommer et situer les 5 océans","Repérer l'équateur et le méridien de Greenwich"],
     vocabulaire:[{mot:"Planisphère",def:"Carte représentant toute la Terre à plat"},{mot:"Continent",def:"Très grande étendue de terre"},{mot:"Équateur",def:"Ligne imaginaire à égale distance des deux pôles"}],
     contexte:"Avant de partir, Phileas Fogg doit reconstituer sa carte du monde : c'est l'occasion de revoir les grands repères du planisphère."},
    {salle:2, titre:"Se déplacer d'un continent à l'autre",
     objectifs:["Situer les mers, détroits et canaux","Comprendre l'utilité du canal de Suez","Ordonner un itinéraire"],
     vocabulaire:[{mot:"Canal",def:"Voie d'eau creusée par l'homme"},{mot:"Détroit",def:"Passage étroit entre deux terres"},{mot:"Escale",def:"Arrêt au cours d'un voyage"}],
     contexte:"Ouvert en 1869, le canal de Suez relie la Méditerranée à la mer Rouge et évite de contourner l'Afrique : il révolutionne les voyages."},
    {salle:3, titre:"Les climats et les paysages du monde",
     objectifs:["Distinguer zones chaude, tempérée et froide","Associer un paysage à son climat","Comprendre le rôle de la latitude et de l'altitude"],
     vocabulaire:[{mot:"Climat",def:"Temps qu'il fait habituellement dans une région"},{mot:"Aride",def:"Très sec, presque sans pluie"},{mot:"Latitude",def:"Distance à l'équateur"}],
     contexte:"De l'Égypte à l'Himalaya, le voyage traverse en quelques semaines presque tous les climats de la planète."},
    {salle:4, titre:"Transports, distances et échelle",
     objectifs:["Identifier les moyens de transport du XIXᵉ siècle","Lire l'échelle d'une carte","Calculer une distance réelle"],
     vocabulaire:[{mot:"Échelle",def:"Rapport entre la carte et la réalité"},{mot:"Vapeur",def:"Machine qui a permis trains et paquebots"},{mot:"Itinéraire",def:"Chemin suivi pour aller d'un lieu à un autre"}],
     contexte:"C'est la vapeur (train et paquebot) qui rend le pari de Fogg possible : trente ans plus tôt, il aurait été absurde."},
    {salle:5, titre:"Méridiens, parallèles et fuseaux horaires",
     objectifs:["Comprendre le rôle du méridien de Greenwich","Calculer une heure locale","Expliquer le jour gagné vers l'est"],
     vocabulaire:[{mot:"Méridien",def:"Demi-cercle imaginaire allant d'un pôle à l'autre"},{mot:"Fuseau horaire",def:"Bande de 15° où l'on lit la même heure"},{mot:"Longitude",def:"Distance au méridien de Greenwich"}],
     contexte:"La Terre tourne de 360° en 24 h, soit 15° par heure : c'est tout le secret du dénouement du roman."}
  ]
};

/* ============================================================
   PANNEAU DE RÉGLAGES
   ============================================================ */
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
            <option value="1" ${r.tailleTexte==1?"selected":""}>Normal (100 %)</option>
            <option value="1.15" ${r.tailleTexte==1.15?"selected":""}>Grand (115 %)</option>
            <option value="1.3" ${r.tailleTexte==1.3?"selected":""}>Très grand (130 %)</option>
            <option value="1.5" ${r.tailleTexte==1.5?"selected":""}>Très très grand (150 %)</option>
          </select>
        </div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Animations réduites</b><br><span style="font-size:.8rem;opacity:.7">Fige les décors, les vidéos et les mouvements des personnages. Utile pour les élèves sensibles au mouvement ou sur un poste lent.</span></div>
        <div class="controle"><div class="bascule ${r.animationsReduites?"actif":""}" id="reg-calme"></div></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>🎬 Multimédia — décors filmés</h4>
      <p style="font-size:.85rem;opacity:.85;font-style:italic;margin-bottom:10px">
        Le jeu fonctionne <b>sans aucune vidéo</b> : les décors sont dessinés et animés dans le code.
        Si vous déposez vos propres fichiers, ils prennent automatiquement la place des dessins.
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
      <div style="background:#fff6e2;border:1px solid var(--velin-ombre);border-radius:10px;padding:12px;margin-top:10px;font-size:.85rem">
        <b>📁 Où déposer vos fichiers ?</b>
        <table style="width:100%;margin-top:8px;font-size:.82rem">
          <tr><th style="text-align:left;padding:4px">Fichier</th><th style="text-align:left;padding:4px">Contenu attendu</th></tr>
          <tr><td style="padding:4px"><code>assets/videos/intro.mp4</code></td><td style="padding:4px">Cinématique d'ouverture (le pari)</td></tr>
          <tr><td style="padding:4px"><code>assets/videos/etape1.mp4</code></td><td style="padding:4px">Décor · Reform Club, Londres</td></tr>
          <tr><td style="padding:4px"><code>assets/videos/etape2.mp4</code></td><td style="padding:4px">Décor · canal de Suez</td></tr>
          <tr><td style="padding:4px"><code>assets/videos/etape3.mp4</code></td><td style="padding:4px">Décor · jungle indienne</td></tr>
          <tr><td style="padding:4px"><code>assets/videos/etape4.mp4</code></td><td style="padding:4px">Décor · tempête en mer de Chine</td></tr>
          <tr><td style="padding:4px"><code>assets/videos/etape5.mp4</code></td><td style="padding:4px">Décor · observatoire de Greenwich</td></tr>
          <tr><td style="padding:4px"><code>assets/videos/final.mp4</code></td><td style="padding:4px">Cinématique de fin (le jour gagné)</td></tr>
        </table>
        <p style="margin-top:10px"><b>Personnages</b> — vidéo en boucle ou image, dans
        <code>assets/videos/personnages/</code> ou <code>assets/images/personnages/</code> :</p>
        <table style="width:100%;margin-top:4px;font-size:.82rem">
          <tr><td style="padding:4px"><code>fogg.mp4</code> · <code>fogg.png</code></td><td style="padding:4px">Phileas Fogg</td></tr>
          <tr><td style="padding:4px"><code>passepartout.mp4</code></td><td style="padding:4px">Jean Passepartout</td></tr>
          <tr><td style="padding:4px"><code>aouda.mp4</code></td><td style="padding:4px">Mrs Aouda</td></tr>
          <tr><td style="padding:4px"><code>fix.mp4</code></td><td style="padding:4px">L'inspecteur Fix</td></tr>
          <tr><td style="padding:4px"><code>fogg-<b>parle</b>.mp4</code></td><td style="padding:4px">Variante jouée pendant qu'il parle (facultatif)</td></tr>
        </table>
        <p style="margin-top:10px"><b>Cartes et paysages</b> — images dans <code>assets/images/cartes/</code> :</p>
        <table style="width:100%;margin-top:4px;font-size:.82rem">
          <tr><td style="padding:4px"><code>planisphere.jpg</code></td><td style="padding:4px">Fond de carte de l'escale 1</td></tr>
          <tr><td style="padding:4px"><code>paysage-desert.jpg</code></td><td style="padding:4px">Photo du désert (escale 3)</td></tr>
          <tr><td style="padding:4px"><code>paysage-jungle.jpg</code> · <code>-montagne</code> · <code>-campagne</code> · <code>-banquise</code> · <code>-savane</code></td><td style="padding:4px">Les autres paysages</td></tr>
        </table>
        <p style="margin-top:8px">Formats acceptés : <b>.mp4</b> ou <b>.webm</b>. Une image du même nom
        (<code>assets/images/decors/etape1.jpg</code>) sert d'affiche, et remplace la vidéo si celle-ci est absente.
        Des sous-titres <code>.vtt</code> du même nom sont chargés automatiquement.</p>
        <div class="boutons" style="margin-top:8px"><button class="btn petit azur" id="btn-scan-medias">🔍 Vérifier les fichiers présents</button></div>
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
        <div class="libelle"><b>Ambiances &amp; bruitages</b><br><span style="font-size:.8rem;opacity:.7">Vent du désert, tempête, tic-tac de Greenwich… générés par le navigateur, aucun fichier</span></div>
        <div class="controle"><div class="bascule ${r.sonsActifs!==false?"actif":""}" id="reg-sons"></div></div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Volume des ambiances</b></div>
        <div class="controle"><input type="range" id="reg-volume-sons" min="0" max="1" step="0.05" value="${r.volumeSons!==undefined?r.volumeSons:0.55}" style="width:120px"></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>⏱️ Partie</h4>
      <div class="reglage-ligne">
        <div class="libelle"><b>Durée du minuteur</b><br><span style="font-size:.8rem;opacity:.7">Pour l'adapter à votre créneau</span></div>
        <div class="controle">
          <select id="reg-duree">
            <option value="30" ${r.dureeMin==30?"selected":""}>30 minutes</option>
            <option value="45" ${r.dureeMin==45?"selected":""}>45 minutes</option>
            <option value="55" ${r.dureeMin==55?"selected":""}>55 minutes (défaut)</option>
            <option value="60" ${r.dureeMin==60?"selected":""}>60 minutes</option>
            <option value="80" ${r.dureeMin==80?"selected":""}>80 minutes (clin d'œil 😉)</option>
          </select>
        </div>
      </div>
      <div class="reglage-ligne">
        <div class="libelle"><b>Bibliothèque de leçons 📚</b><br><span style="font-size:.8rem;opacity:.7">Consultable par les élèves pendant le jeu</span></div>
        <div class="controle"><div class="bascule ${r.leconsAutorisees?"actif":""}" id="reg-lecons"></div></div>
      </div>
    </div>

    <div class="reglages-group">
      <h4>🤖 IA optionnelle (avancé)</h4>
      <p style="font-size:.85rem;opacity:.8;font-style:italic;margin-bottom:10px">
        Sans clé, tous les dialogues sont pré-écrits et fonctionnent hors-ligne (recommandé en classe).</p>
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
        <label>Clé API (stockée localement sur ce poste uniquement)</label>
        <input type="password" id="reg-api-cle" placeholder="sk-..." value="${r.apiCle||""}" autocomplete="off">
      </div>
      <div class="boutons" style="margin-top:8px"><button class="btn petit azur" id="btn-test-api">🔧 Tester la clé</button></div>
      <div id="fb-api" style="margin-top:8px"></div>
    </div>

    <div class="reglages-group">
      <h4>🖨️ Impressions A4</h4>
      <p style="font-size:.85rem;opacity:.8;font-style:italic;margin-bottom:10px">
        Fiches préparatoires et évaluations, avec corrigés séparés.</p>
      <div style="display:flex;flex-direction:column;gap:8px">
        <button class="btn azur" id="btn-imprimer-prepa">📋 Fiches préparatoires (5 escales)</button>
        <button class="btn azur" id="btn-imprimer-qcm">📝 QCM de géographie</button>
        <button class="btn azur" id="btn-imprimer-fermees">✅ Questions fermées (V/F + réponses courtes)</button>
        <button class="btn azur" id="btn-imprimer-docs">📄 Étude de documents</button>
        <button class="btn laiton" id="btn-imprimer-tout">📚 Tout imprimer (élève + corrigés)</button>
      </div>
    </div>

    <div class="boutons" style="margin-top:18px">
      <button class="btn jade" id="btn-sauver-reglages">💾 Enregistrer les réglages</button>
    </div>
  `;

  corps.querySelectorAll(".bascule").forEach(b=>{
    b.addEventListener("click", ()=>b.classList.toggle("actif"));
  });

  corps.querySelector("#btn-imprimer-prepa").addEventListener("click", ()=>imprimerFiches("prepa"));
  corps.querySelector("#btn-imprimer-qcm").addEventListener("click", ()=>imprimerFiches("qcm"));
  corps.querySelector("#btn-imprimer-fermees").addEventListener("click", ()=>imprimerFiches("fermees"));
  corps.querySelector("#btn-imprimer-docs").addEventListener("click", ()=>imprimerFiches("docs"));
  corps.querySelector("#btn-imprimer-tout").addEventListener("click", ()=>imprimerFiches("tout"));
  corps.querySelector("#btn-test-api").addEventListener("click", testerAPI);
  corps.querySelector("#btn-scan-medias").addEventListener("click", scannerMedias);
  corps.querySelector("#btn-sauver-reglages").addEventListener("click", sauverReglages);

  overlay.classList.add("show");
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
    {base:"etape1", nom:"Escale 1 · Reform Club"},
    {base:"etape2", nom:"Escale 2 · Suez"},
    {base:"etape3", nom:"Escale 3 · Inde"},
    {base:"etape4", nom:"Escale 4 · Mer de Chine"},
    {base:"etape5", nom:"Escale 5 · Greenwich"},
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
    {base:"fogg", nom:"Phileas Fogg"},
    {base:"passepartout", nom:"Jean Passepartout"},
    {base:"aouda", nom:"Mrs Aouda"},
    {base:"fix", nom:"L'inspecteur Fix"}
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
    {base:"planisphere", nom:"Fond du planisphère (escale 1)"},
    {base:"paysage-desert", nom:"Paysage : désert"},
    {base:"paysage-jungle", nom:"Paysage : jungle"},
    {base:"paysage-montagne", nom:"Paysage : montagne"},
    {base:"paysage-campagne", nom:"Paysage : campagne"},
    {base:"paysage-banquise", nom:"Paysage : banquise"},
    {base:"paysage-savane", nom:"Paysage : savane"}
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
function sauverReglages(){
  const c = document.getElementById("corps-reglages");
  ETAT.reglages.tailleTexte       = parseFloat(c.querySelector("#reg-taille").value);
  ETAT.reglages.animationsReduites= c.querySelector("#reg-calme").classList.contains("actif");
  ETAT.reglages.decorsVideo       = c.querySelector("#reg-video").classList.contains("actif");
  ETAT.reglages.sonVideo          = c.querySelector("#reg-video-son").classList.contains("actif");
  ETAT.reglages.cinematiques      = c.querySelector("#reg-cine").classList.contains("actif");
  ETAT.reglages.narrationActive   = c.querySelector("#reg-voix").classList.contains("actif");
  ETAT.reglages.volume            = parseFloat(c.querySelector("#reg-volume").value);
  ETAT.reglages.sonsActifs        = c.querySelector("#reg-sons").classList.contains("actif");
  ETAT.reglages.volumeSons        = parseFloat(c.querySelector("#reg-volume-sons").value);
  ETAT.reglages.dureeMin          = parseInt(c.querySelector("#reg-duree").value);
  ETAT.reglages.leconsAutorisees  = c.querySelector("#reg-lecons").classList.contains("actif");
  ETAT.reglages.apiActive         = c.querySelector("#reg-api").classList.contains("actif");
  ETAT.reglages.apiFournisseur    = c.querySelector("#reg-api-fournisseur").value;
  ETAT.reglages.apiCle            = c.querySelector("#reg-api-cle").value;

  try{ localStorage.setItem("escape_tdm_reglages", JSON.stringify(ETAT.reglages)); }catch(e){}
  appliquerReglages();
  majHUD();

  // Les décors filmés doivent être rechargés si le réglage a changé
  const scene = document.querySelector("#ecran-salle .scene, #scene-accueil");
  if(scene && typeof activerScene === "function" && ETAT.reglages.decorsVideo){
    activerScene(scene);
  }

  toast("Réglages enregistrés ✓");
  document.getElementById("overlay-reglages").classList.remove("show");
}

async function testerAPI(){
  const c  = document.getElementById("corps-reglages");
  const fb = c.querySelector("#fb-api");
  const fournisseur = c.querySelector("#reg-api-fournisseur").value;
  const cle = c.querySelector("#reg-api-cle").value;
  if(!cle){ fb.innerHTML = '<div class="feedback erreur show">Veuillez saisir une clé.</div>'; return; }
  fb.innerHTML = '<div class="feedback indice show">Test en cours… <span class="spinner"></span></div>';
  try{
    const ok = await testerCleAPI(fournisseur, cle);
    fb.innerHTML = ok
      ? '<div class="feedback succes show">✅ Clé valide ! L\'IA est prête.</div>'
      : '<div class="feedback erreur show">❌ Clé invalide ou erreur. Vérifiez la clé et le fournisseur.</div>';
  }catch(e){
    fb.innerHTML = '<div class="feedback erreur show">❌ Erreur réseau : '+e.message+'. (L\'IA reste optionnelle.)</div>';
  }
}

window.ouvrirReglages = ouvrirReglages;
window.sauverReglages = sauverReglages;
window.testerAPI = testerAPI;
window.scannerMedias = scannerMedias;
window.chargerEvaluations = chargerEvaluations;
