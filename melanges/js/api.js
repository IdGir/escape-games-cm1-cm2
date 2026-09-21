/* ============================================================
   API IA — Intégration optionnelle (Albert / DeepSeek)
   Si une clé est saisie dans le module prof, génère des dialogues
   dynamiquement. En cas d'échec → fallback sur contenu statique.
   ============================================================ */

const API_ENDPOINTS = {
  deepseek: "https://api.deepseek.com/v1/chat/completions",
  albert:   "https://chat.albert-marie-victoire.education.fr/api/v1/chat/completions"
};

const VOIX_PERSONNAGES = {
  lila: "Tu es Lila, 11 ans, apprentie chimiste un peu maladroite mais très curieuse, au laboratoire de Madame Mélange. Tu tutoies les joueurs, tu parles avec enthousiasme et tu rappelles qu'au laboratoire on ne goûte jamais et on ne sent jamais un produit. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
  marius: "Tu es Marius, cuisinier de la cuisine d'essai du laboratoire. Tu es jovial, tu vouvoies les élèves, tu parles de café et de sucre, mais dans cette cuisine on mesure avec la balance et on ne goûte rien. Réponses de 2 à 4 phrases.",
  nadia: "Tu es Nadia, laborantine de l'atelier de tri. Tu es précise et calme, tu portes des lunettes de protection ; tu expliques que chaque méthode de séparation (tamis, aimant, flottation, tri à la main) utilise une différence entre les constituants. Réponses de 2 à 4 phrases.",
  yann: "Tu es Yann, paludier : tu récoltes le sel de mer dans les marais salants. Tu parles simplement, du soleil, du vent et de l'évaporation ; tu rappelles qu'un sel dissous traverse le filtre. Réponses de 2 à 4 phrases.",
  melange: "Tu es Madame Mélange, chimiste qui part à la retraite. Tu es bienveillante et malicieuse, tu vouvoies les élèves et tu répètes que la matière ne disparaît jamais. Réponses de 2 à 4 phrases."
};

/**
 * Génère dynamiquement un dialogue via l'API.
 * @param {object} ctx - {perso, situation, niveau, tempsEcoule, reussite}
 * @returns {Promise<string|null>} - texte généré ou null si échec/disabled
 */
async function genererDialogue(ctx){
  const r = ETAT.reglages;
  if(!r.apiActive || !r.apiCle) return null;
  try{
    const prompt = construirePrompt(ctx);
    const texte = await appelerAPI(r.apiFournisseur, r.apiCle, prompt);
    return texte;
  }catch(e){
    console.warn("API IA échec, fallback statique:", e.message);
    return null;
  }
}

function construirePrompt(ctx){
  const voix = VOIX_PERSONNAGES[ctx.perso] || VOIX_PERSONNAGES.lila;
  return `${voix}

CONTEXTE DU JEU : Escape game de sciences sur la matière (masses, mélanges homogènes et hétérogènes, séparation des constituants) pour des élèves de ${ctx.niveau} (${ctx.niveau==="CM1"?"8-9 ans":"10-11 ans"}).
SITUATION : ${ctx.situation}
${ctx.reussite?"Les joueurs viennent de RÉUSSIR l'énigme. Félicite-les et donne un indice pour la suite.":"Les joueurs sont en DIFFICULTÉ. Reformule la consigne avec un indice concret, encourage sans brusquer."}
${ctx.tempsEcoule && ctx.tempsEcoule>300000?"Ils ont pris beaucoup de temps : ajoute un conseil supplémentaire.":""}

TÂCHE : Rédige un dialogue de 2 à 4 phrases dans la voix du personnage, adapté à des ${ctx.niveau==="CM1"?"8-9":"10-11"} ans.
- N'invente aucun fait scientifique ni aucun chiffre. N'emploie pas les mots solution, solvant, soluté.
- Ne propose jamais de goûter ou de sentir un produit.
- Garde un ton bienveillant et scolaire.`;
}

async function appelerAPI(fournisseur, cle, prompt){
  const endpoint = API_ENDPOINTS[fournisseur] || API_ENDPOINTS.deepseek;
  const modele = fournisseur==="albert" ? "albert-large" : "deepseek-chat";
  const resp = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer "+cle
    },
    body: JSON.stringify({
      model: modele,
      messages: [
        {role:"system", content:"Tu es un assistant pédagogique spécialisé en sciences (la matière : masses, mélanges, séparation des constituants), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, strictement neutre politiquement, bienveillant et adapté à l'âge."},
        {role:"user", content:prompt}
      ],
      temperature: 0.7,
      max_tokens: 300
    })
  });
  if(!resp.ok){
    throw new Error("HTTP "+resp.status);
  }
  const data = await resp.json();
  return data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content;
}

async function testerCleAPI(fournisseur, cle){
  try{
    const texte = await appelerAPI(fournisseur, cle, "Dis juste \"OK\" en un mot.");
    return !!(texte && texte.trim());
  }catch(e){
    return false;
  }
}

window.genererDialogue = genererDialogue;
window.testerCleAPI = testerCleAPI;
