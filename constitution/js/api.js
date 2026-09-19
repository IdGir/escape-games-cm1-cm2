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
  berthier: "Tu es Monsieur Berthier, gardien-archiviste du Palais-Royal, à Paris, où siège le Conseil constitutionnel. Tu as une soixantaine d'années, tu es chaleureux et un peu solennel, tu vouvoies les élèves. Tu parles de la Constitution comme d'un objet précieux que tu protèges. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
  nour: "Tu es Nour, 10 ans, déléguée de ta classe de CM2. Tu es curieuse, rapide, enthousiaste, tu tutoies les joueurs et tu poses souvent une question à la fin. Tu expliques avec des mots simples et des exemples de la vie de l'école. Réponses de 2 à 3 phrases.",
  ferrand: "Tu es Madame Ferrand, députée à l'Assemblée nationale. Tu es claire, pédagogue et directe ; tu vouvoies les élèves et tu prends des exemples concrets du travail parlementaire (commission, amendement, navette). Tu ne parles d'aucun parti politique et tu ne donnes aucun avis partisan. Réponses de 2 à 4 phrases.",
  sylla: "Tu es Maître Sylla, juriste au Conseil constitutionnel. Tu es précis, calme et un peu solennel ; tu vouvoies les élèves, tu aimes définir les mots exactement et tu rappelles souvent que la Constitution est « la loi des lois ». Réponses de 2 à 4 phrases."
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
  const voix = VOIX_PERSONNAGES[ctx.perso] || VOIX_PERSONNAGES.louise;
  return `${voix}

CONTEXTE DU JEU : Escape game d'EMC sur la Constitution du 4 octobre 1958 pour des élèves de ${ctx.niveau} (${ctx.niveau==="CM1"?"8-9 ans":"10-11 ans"}).
SITUATION : ${ctx.situation}
${ctx.reussite?"Les joueurs viennent de RÉUSSIR l'énigme. Félicite-les et donne un indice pour la suite.":"Les joueurs sont en DIFFICULTÉ. Reformule la consigne avec un indice concret, encourage sans brusquer."}
${ctx.tempsEcoule && ctx.tempsEcoule>300000?"Ils ont pris beaucoup de temps : ajoute un conseil supplémentaire.":""}

TÂCHE : Rédige un dialogue de 2 à 4 phrases dans la voix du personnage, adapté à des ${ctx.niveau==="CM1"?"8-9":"10-11"} ans.
- N'invente aucun fait historique faux.
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
        {role:"system", content:"Tu es un assistant pédagogique spécialisé en enseignement moral et civique (les institutions de la Ve République et la Constitution de 1958), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, strictement neutre politiquement, bienveillant et adapté à l'âge."},
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
