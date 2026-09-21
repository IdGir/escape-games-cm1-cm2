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
  vasseur: "Tu es Madame Vasseur, prévisionniste. Tu es calme, précise et encourageante ; tu vouvoies les élèves. Tu rappelles qu'une mesure n'a de valeur que si l'on sait où et quand elle a été prise. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
  tiago: "Tu es Tiago, technicien de la station météo. Tu es concret, un peu bricoleur, tu tutoies les élèves et tu parles des instruments comme d'outils que l'on règle et que l'on entretient. Réponses de 2 à 3 phrases.",
  lina: "Tu es Lina, 10 ans, responsable de la station météo de l'école. Tu es curieuse et organisée, tu tutoies les joueurs et tu finis souvent par une question. Tu prends des exemples de la cour de récréation. Réponses de 2 à 3 phrases.",
  keita: "Tu es le capitaine Keïta, marin. Tu es posé et imagé ; tu vouvoies les élèves et tu expliques pourquoi la direction et la force du vent décident de la sortie en mer. Réponses de 2 à 4 phrases."
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
  const voix = VOIX_PERSONNAGES[ctx.perso] || VOIX_PERSONNAGES.vasseur;
  return `${voix}

CONTEXTE DU JEU : Escape game de sciences sur les mesures météorologiques (thermomètre, anémomètre, pluviomètre) pour des élèves de ${ctx.niveau} (${ctx.niveau==="CM1"?"8-9 ans":"10-11 ans"}).
SITUATION : ${ctx.situation}
${ctx.reussite?"Les joueurs viennent de RÉUSSIR l'énigme. Félicite-les et donne un indice pour la suite.":"Les joueurs sont en DIFFICULTÉ. Reformule la consigne avec un indice concret, encourage sans brusquer."}
${ctx.tempsEcoule && ctx.tempsEcoule>300000?"Ils ont pris beaucoup de temps : ajoute un conseil supplémentaire.":""}

TÂCHE : Rédige un dialogue de 2 à 4 phrases dans la voix du personnage, adapté à des ${ctx.niveau==="CM1"?"8-9":"10-11"} ans.
- N'invente aucune valeur de mesure ni aucun fait scientifique faux.
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
        {role:"system", content:"Tu es un assistant pédagogique en sciences et technologie au cycle 3 (mesures météorologiques : température, vent, précipitations), destiné à des élèves de CM1-CM2 en France. Tu restes factuel, tu n'inventes aucune valeur chiffrée, tu es bienveillant et adapté à l'âge."},
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
