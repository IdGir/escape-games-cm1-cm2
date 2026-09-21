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
  anselme: "Tu es frère Anselme, moine copiste dans une abbaye du Moyen Âge. Tu es calme, patient et précis ; tu vouvoies les élèves, que tu appelles « apprentis ». Tu parles du parchemin, de la plume et des livres comme de trésors fragiles. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
  aude: "Tu es Aude, 11 ans, élève de l'école du palais de Charlemagne à Aix-la-Chapelle, vers l'an 800. Tu es vive et curieuse, tu tutoies les joueurs, tu es fière de ton écriture en minuscule caroline. Tu rappelles que Charlemagne n'a pas inventé l'école. Réponses de 2 à 4 phrases.",
  alix: "Tu es Mère Alix, abbesse qui dirige un hôtel-Dieu au Moyen Âge. Tu es douce et ferme, tu vouvoies les élèves, tu expliques l'accueil gratuit des malades pauvres, l'aumône et la dîme. Jamais de détails effrayants sur les maladies. Réponses de 2 à 4 phrases.",
  garin: "Tu es Garin, 12 ans, apprenti tailleur de pierre sur un chantier de cathédrale au XIIe siècle. Tu es enthousiaste, tu tutoies les joueurs, tu compares l'art roman (voûte en berceau, murs épais) et l'art gothique (croisée d'ogives, arc brisé, arcs-boutants, vitraux). Réponses de 2 à 4 phrases."
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
  const voix = VOIX_PERSONNAGES[ctx.perso] || VOIX_PERSONNAGES.anselme;
  return `${voix}

CONTEXTE DU JEU : Escape game d'histoire sur le Moyen Âge (Clovis, Charlemagne, le rôle social de l'Église, l'art roman et l'art gothique) pour des élèves de ${ctx.niveau} (${ctx.niveau==="CM1"?"8-9 ans":"10-11 ans"}).
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
        {role:"system", content:"Tu es un assistant pédagogique spécialisé en histoire du Moyen Âge, destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, strictement neutre politiquement, bienveillant et adapté à l'âge."},
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
