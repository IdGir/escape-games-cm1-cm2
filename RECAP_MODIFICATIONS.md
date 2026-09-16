# Correcteur Pédagogique — modifications (juillet 2026)

Ce fichier récapitule ce qui a été changé et **comment tester / fabriquer l'exe**.
Toutes les modifications sont déjà **dans ce dossier** — rien à déplacer.

---

## Ce qui a été fait (tes 6 demandes)

1. **Fiche élève — graphique + besoins sur une même ligne.**
   Le graphique « % d'erreurs corrigées séance après séance » (trop grand) et le
   bloc « Besoins de suivi détectés » (trop petit) sont maintenant **côte à côte**,
   sur une même rangée. Le graphique est plus compact, les besoins plus visibles.

2. **Réglages — brancher d'autres IA / API.**
   Nouveau moteur **« Autre API (compatible OpenAI) »** : tu peux brancher OpenAI,
   Mistral, Groq, OpenRouter, ou un serveur local. Il suffit d'indiquer l'**adresse**
   (souvent terminée par `/v1`), la **clé** et le **nom du modèle**. Un bouton
   « Tester le moteur » vérifie la connexion. Seuls les réglages du moteur choisi
   s'affichent, pour rester clair.

3. **Corrigés des textes de la classe** (les deux solutions demandées) :
   - **Bouton « 🤖 Générer le corrigé automatiquement »** dans l'éditeur de texte
     ET dans chaque texte existant (colonne « Corrigé » → « ⚠ ajouter le corrigé »).
     À relire avant d'enregistrer.
   - **Bouton « 📚 Ajouter les textes fournis (avec corrigés) »** : ajoute d'un coup
     de nouveaux textes CM1/CM2 tout prêts, **sans doublon**. La banque fournie passe
     de 5 à **11 textes**, tous avec corrigé.

4. **Module élève « Je me corrige » — procédure méthodique en 5 passages.**
   L'élève avance maintenant dans un ordre fixe, un seul type d'erreur à la fois :
   1. **La cohérence** (manque-t-il des mots ? est-ce que ça veut dire quelque chose ?)
   2. **Ponctuation & majuscules**
   3. **Les accords** (groupe du nom)
   4. **La conjugaison** (accord sujet-verbe, + a/à, est/et, ont/on, son/sont)
   5. **L'orthographe des mots**

   À chaque passage, **seule la famille d'erreurs concernée est surlignée** : l'élève
   ne cherche qu'une chose à la fois. Un bilan termine le parcours.

5. **Mini-leçons en aide, colorées, grandes et aérées.**
   Les leçons reprennent les « Je retiens » d'*Outils pour le français* CM1/CM2
   (renvoi au manuel affiché). Elles présentent : l'idée-clé, la règle, les
   **questions à se poser**, des exemples et le piège à éviter — en grand et coloré.

6. **Aide IA en deux niveaux, prise en compte dans l'évaluation.**
   Quand l'élève clique sur une erreur :
   - une **question** l'oriente vers la réponse (ex. « singulier ou pluriel ? ») ;
   - un bouton **« 🆘 J'ai besoin d'un indice »** donne un indice plus direct
     (ex. *un mot de la même famille pour retrouver une lettre muette*).
   Si une IA est branchée, elle **formule ces questions/indices sur mesure** selon la
   phrase de l'élève ; sinon, des règles hors ligne les fournissent.
   **L'aide est comptée** : les corrections faites après un indice comptent « avec
   aide », le bilan affiche le **nombre d'indices utilisés**, et ce nombre part aussi
   dans l'**export CSV** de l'enseignant. Réglable dans ⚙️ Réglages (« Aide guidée »).

---

## Comment essayer tout de suite (sans fabriquer l'exe)

1. Ouvre ce dossier dans l'explorateur Windows.
2. Double-clique sur **`lancer.bat`**.
3. Une fenêtre noire s'ouvre (laisse-la ouverte), puis l'application apparaît.
   - Si un message dit que **Python n'est pas installé** : va sur
     https://www.python.org/downloads/, clique sur **Download Python**,
     **coche « Add Python to PATH »**, installe, puis relance `lancer.bat`.

### Choses à vérifier
- **Espace enseignant → Fiche élève** : choisis un élève ayant des séances → le
  graphique et les besoins sont sur la même ligne.
- **Réglages → Moteur IA** : choisis « Autre API », remplis adresse/clé/modèle,
  clique « Tester le moteur ».
- **Banques de textes → Textes à corriger** : bouton « Ajouter les textes fournis »,
  et sur un texte « ⚠ ajouter le corrigé » → bouton « Générer le corrigé ».
- **Espace élève → Je me corrige** : lance une correction → tu suis les 5 passages,
  clique sur une zone colorée → leçon + question + bouton « indice ».

---

## Comment fabriquer le `.exe`

1. Double-clique sur **`build_exe.bat`**.
2. Attends 3 à 6 minutes (ne ferme pas la fenêtre).
3. Ton programme se trouve dans **`dist\CorrecteurPedagogique.exe`**.
   Copie-le sur une clé USB ou les postes de la classe : il fonctionne seul.

> Les deux nouveaux fichiers (`ia_client.py`, `aide.py`) sont inclus automatiquement
> dans l'exe : rien de plus à faire.

---

## Fichiers modifiés / ajoutés

**Ajoutés** : `ia_client.py` (client IA unifié), `aide.py` (aide en 2 niveaux).

**Modifiés** :
`config_manager.py` (nouveaux réglages), `corrector.py`, `ai_generator.py`
(moteur « autre API »), `api.py` (routes `/api/aide`, `/api/textes/corrige-auto`,
`/api/textes/correction/<id>/corrige`, `/api/textes/correction/installer-fournis`,
export CSV), `database.py` (colonne `nb_aides`, migration v3),
`lexical_hints.py` (mini-leçons enrichies), `seed_data.py` (banque élargie),
`web/js/eleve.js` (5 passages + aide), `web/js/prof.js` (fiche, réglages, corrigés),
`web/css/style.css` (mini-leçons).

**Compatibilité** : la base de données existante est conservée (migration
automatique au démarrage). Aucune donnée d'élève n'est perdue.

## Mise à jour (compléments)

- **Réglages → thème des textes générés** : c'est maintenant une **liste déroulante**
  de thèmes (école, animaux, nature, sport, voyages, sciences, contes…). On choisit,
  ou on prend « ✏️ Autre thème » pour écrire le sien.
- **« Je me corrige » — deux étapes ajoutées AVANT la correction guidée :**
  1. **Je cherche seul(e)** : on donne uniquement le **nombre d'erreurs**, sans les
     surligner. L'élève corrige ce qu'il repère tout seul.
  2. **Mon premier bilan** : on lui indique **ce qu'il a corrigé seul** et **les
     types d'erreurs (avec le nombre) qui restent**, toujours **sans surlignage**.
  3. **Je corrige avec l'aide** : la procédure en 5 passages surlignés (déjà en place).

  Conséquence pédagogique : « corrigées SANS aide » = ce qui est réparé pendant
  l'étape 1 (vraie autonomie, avant tout surlignage).
- **Leçons recentrées** : quand l'élève clique sur une erreur, on n'affiche plus la
  leçon générale mais **seulement ce qui sert à ce cas précis** : la question à se
  poser, une ou deux pistes ciblées, puis l'indice à la demande.

## Mise à jour 2 (étape 2 + évaluation)

- **Étape 2 « Mon bilan, et je continue seul(e) »** :
  - le **premier bilan est mis en avant en grand** (gros chiffre « corrigées seul » +
    pastilles par type) ;
  - **le texte reste affiché et modifiable** : sachant quels **types** d'erreurs
    restent (affichés à droite, comptés en direct, **sans surlignage**), l'élève peut
    **continuer à se corriger seul** ;
  - ce n'est **qu'ensuite** qu'on passe aux 5 passages surlignés.
- **Autonomie** : les corrections faites pendant **les deux étapes sans surlignage**
  (1 et 2) comptent désormais comme « corrigées sans aide ».
- **Réglages → « 🎯 Évaluation du travail de correction »** (nouveaux critères,
  modifiables par l'enseignant) :
  - seuil pour un travail **« réussi »** (% corrigé) — défaut 60 ;
  - seuil pour **« excellent »** — défaut 90 ;
  - **objectif d'autonomie** (% corrigé sans aide) — défaut 60 ;
  - féliciter (ou non) l'élève quand l'objectif d'autonomie est atteint.
  Ces critères pilotent le message de réussite et le badge « 🎯 objectif atteint »
  affichés à l'élève à la fin.

## Mise à jour 3 (passage homophones + erreurs ajoutées)

- **Nouveau passage « 👂 Les homophones »**, intercalé **entre « Accords » et
  « Conjugaison »**. La procédure guidée compte donc maintenant **6 passages** :
  cohérence → ponctuation/majuscules → accords → **homophones** → conjugaison →
  orthographe. Résultat : les mots comme *a/à, et/est, on/ont, son/sont* sont
  traités à part, et le passage « conjugaison » ne montre plus que de vrais verbes.
- **Erreur ajoutée par l'élève** : si, en croyant se corriger, l'élève **introduit
  une nouvelle erreur** pendant un passage, un bandeau rouge le lui **signale au
  passage suivant** (« En corrigeant, tu as ajouté 1 erreur : accord. »), en
  précisant qu'il la retrouvera surlignée à son passage.

## Mise à jour 4 (présentation de l'étape 2)

Les deux cadres **« ✅ Erreurs corrigées seul(e) »** et **« 🔎 Erreurs à corriger »**
sont désormais **côte à côte sur une même ligne**, juste au-dessus du texte, et bien
plus visibles : cadre coloré (vert / orange), bordure épaisse, fond teinté, très gros
chiffre et pastilles de types agrandies. Les deux se **mettent à jour en direct**
pendant que l'élève continue à se corriger (toujours sans surlignage) : le nombre
corrigé monte, le nombre restant descend. Le texte occupe maintenant toute la largeur
en dessous. Sur écran étroit, les deux cadres se superposent automatiquement.

**Ces deux cadres restent affichés pendant toute la procédure** : on les retrouve
au-dessus du texte à chacun des 6 passages guidés, en version compacte pour ne pas
manger la place. Pendant les passages, le cadre vert s'intitule « Erreurs corrigées »
(total, mis à jour en direct) et précise en dessous **« dont N trouvée(s) tout(e)
seul(e), avant l'aide »** — l'élève garde ainsi sous les yeux sa progression globale
et sa part d'autonomie. Le cadre orange liste toujours **tous** les types restants,
alors que le panneau de droite ne compte que la famille du passage en cours.

## Vérifications effectuées
- Tous les fichiers Python compilent ; les fichiers JavaScript passent le contrôle
  de syntaxe.
- Test central : **0 erreur** quand l'élève rend exactement le corrigé (aucun faux
  positif).
- Les 8 catégories ont bien question + indice + mini-leçon enrichie.
- Enregistrement d'une séance avec `nb_aides` : OK. Toutes les routes clés : 200.
