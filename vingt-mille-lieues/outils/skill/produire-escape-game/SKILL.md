---
name: "produire-escape-game"
description: "Produire ou transformer les escape games CM1/CM2 du dépôt PROJET ESCAPE GAMES : choisir le mode (migrer un jeu existant au modèle immersif de « Vingt mille lieues sous les mers », créer un nouveau jeu, produire ou ajouter des images et vidéos avec une source au choix), puis appliquer la procédure complète (faits, données, leçons, intégration, tests, commit)."
---

# Produire ou transformer un escape game de la collection CM1/CM2

Dépôt : `E:\IDRISS\PROJET ESCAPE GAMES` (branche `escape-games`, publié sur https://idgir.github.io/escape-games-cm1-cm2/).
Répondre en français, de façon concise. **Ne jamais faire `git push`** : c'est l'enseignant qui publie (hors session cloud, où la consigne de la session l'emporte). **Ne jamais fusionner une PR sans accord explicite.**

## 0. Démarrage

1. Demander l'accès au dossier du dépôt (s'il n'est pas déjà connecté), puis travailler avec le shell de l'ordinateur.
2. Lire les documents du projet : `claude/eg-plan-histoire-sciences.md`, `claude/eg-renaissance.md`, `claude/eg-versailles.md` (pièges, fichiers d'intégration) et, pour le modèle immersif, `vingt-mille-lieues/GUIDE-IMMERSIF.md` et `vingt-mille-lieues/GUIDE-MEDIAS.md`.
3. Lire `prompts-opus/00-ORDRE-DE-PRODUCTION.md` (colonne « Fait »), `git log --oneline -5`, `git status -sb` : repérer les jeux non faits et un éventuel commit non poussé (le signaler).
4. **Choisir le mode** (AskUserQuestion, une seule réponse) si l'utilisateur ne l'a pas donné :
   - **A. Migrer un jeu existant au modèle immersif** (§ 2) ;
   - **B. Créer un nouveau jeu** (§ 3) ;
   - **C. Produire ou ajouter des images et des vidéos** (§ 4) ;
   - **D. Autre** : correction, leçons A4, intégration (§ 5-6).
5. **Choix des jeux (cases à cocher)** : si l'utilisateur n'a pas donné les numéros ou les noms, AskUserQuestion en `multiSelect: true` (4 jeux par question, jusqu'à 4 questions ; libellé « n°08 Le Grand Repas du chef (sciences, A, P2) »). L'option « Autre » permet de taper des numéros.
6. **Un seul jeu par conversation**. Pour les autres, dire à la fin d'ouvrir une nouvelle conversation et de relancer ce skill avec les numéros restants.
7. Si un fichier `RECAP-<slug>.md` existe à la racine pour ce jeu, reprendre là où il s'arrête.

## 1. Règles de contenu (tous les modes)

Le prompt du jeu (`prompts-opus/NN-<slug>.md`) fait foi : sections 4 (cahier des charges commun) et 9 (le jeu). Les titres et scénarios sont des propositions améliorables ; le contenu de la progression doit être couvert intégralement.

- 5 salles (ou étapes) ; 3 énigmes par salle en CM1 (15), 4 en CM2 (20) : l'énigme 4 de chaque salle a `"niveaux": ["CM2"]` et un bloc `commun`. Les types : qcm, vraifaux, association, ordre, tri, trous, lettres, code, intrus, plan, instrument ; jamais deux types identiques consécutifs dans une salle, au moins une manipulation `ordre`, `plan` ou `tri` par salle et par niveau.
- Chaque énigme : consigne (cm1/cm2), 3 indices par niveau, correction (jamais affichée après réussite ; elle ne doit pas commencer comme le texte de l'énigme), source, champ `lecon`.
- Un mot-clé par salle ; les mots forment une phrase-bilan (coffre final). Différenciation réelle : repères en CM1, dates exactes en CM2.
- Pas d'emoji dans les contenus élèves ; personnages **inventés** (filles et garçons) ; les personnes réelles ne parlent jamais ; aucune violence gratuite.
- **Faits vérifiés en ligne** sur des sources officielles ou de référence ; ne jamais inventer un chiffre ; les doutes vont dans `A-VERIFIER.md`.
- **Médias** : ne **jamais** produire d'image ou de vidéo sans l'accord de l'enseignant ; respecter les plafonds de coût ; **ne jamais montrer ni écrire une clé d'API** ; lieux réels = vraies photos, personnages jamais réels. Le jeu doit toujours fonctionner sans média (décors dessinés, cinématiques en direct).
- **Isolation** : `bash outils-tests/verifier-isolation.sh` doit afficher « OK » avant chaque commit. Il laisse libres `vingt-mille-lieues/` et `immersifs/`, et protège les 12 jeux d'origine, `commun/`, `serveur.py`, etc. Pour **remplacer** un jeu d'origine, l'enseignant l'autorise explicitement : `--autoriser <jeu>`.
- Cohérence narrative (jeux immersifs) : lieu, problème, personnage émetteur, lien avec l'histoire, raison du savoir ici, réaction du décor, liberté assumée ; pas de morale plaquée ; relecture sceptique avant livraison.

## 2. Mode A — Migrer un jeu existant au modèle immersif

Le modèle immersif est celui de « Vingt mille lieues sous les mers » : décor image + effets, objets cliquables, personnage qui parle, cinématiques, grades, journal, coffre. **Non destructif** : la variante est écrite dans `immersifs/<jeu>/`, l'original n'est pas touché.

1. `python vingt-mille-lieues/outils/immersif/migrer-jeu.py --lister` : jeux migrables (structure `salles`). `declaration`, `tour-du-monde`, `mission-geo` ne le sont pas : les refaire en mode B.
2. Choisir avec l'enseignant : jeu(x), **thème** (`outils/immersif/theme-defaut.json` à copier : mot « salle »/« étape », titres, noms des grades, palette, charte visuelle), **grades** (par défaut CM1 → matelot, CM2 → timonier ; option `--grades cm1:matelot,cm2:timonier,cm1:mousse`).
3. `python vingt-mille-lieues/outils/immersif/migrer-jeu.py <jeu> [--theme t.json] [--grades …]` ; lire `immersifs/<jeu>/MIGRATION-RAPPORT.md`.
4. `node immersifs/<jeu>/tests/test-immersif.js` : joue toutes les énigmes de tous les grades (doit être vert avant d'aller plus loin).
5. **Compléter les brouillons** (liste dans le rapport) : zones des décors (après dépôt des images, `outils/caler-effets.html`), `enjeu`, `reaction_du_decor`, `probleme_narratif`, phrases des personnages (`dialogue` de chaque grade), cinématiques (`dialogues.json`). Relancer `outils/embarquer-donnees.py` après chaque JSON modifié.
6. Médias : mode C (le `medias.csv` de la variante contient déjà les prompts).
7. Faire évoluer le moteur plus tard sans perdre le travail : `migrer-jeu.py --maj-moteur immersifs/<jeu>`.
8. **Remplacer l'original** seulement sur décision explicite de l'enseignant : `git mv`, garde-fou `--autoriser <jeu>`, intégration au catalogue (§ 5), tests communs. Sinon, garder les deux versions.

## 3. Mode B — Créer un nouveau jeu

Écrire les données au **format des jeux existants** (c'est ce que décrit le prompt du jeu) puis migrer :

1. Copier le squelette de `renaissance/` (le plus récent) : `index.html`, `prof.html`, `lecons-imprimables.html`, `js/`, `css/`, `tests/`. Générer les données par **scripts Python** (jamais à la main dans le JSON) :
   - `assets/data/enigmes.json` (métadonnées + 5 salles ; schémas SVG des énigmes `plan` produits par une fonction avec repères numérotés) ;
   - `dialogues.json` (personnages, `intro_accueil`, 5 salles avec lieu, description, 3 sens, `dialogue_intro`, `dialogue_reussite` ou `dialogue_fin`, `motCle`) ;
   - `lecons.json` (5 leçons : objectifs, contenu cm1/cm2, lexique, frise, document, sources ; 220 à 600 mots en CM2) ;
   - `evaluations.json` (quizz final, QCM, questions fermées, études de documents, fiches préparatoires ; mélanger la place de la bonne réponse).
2. Adapter `js/jeu.js`, `js/app.js` (clés localStorage `escape_<slug>…`, écran de fin avec la phrase des mots), `js/reglages.js`, `js/lecons.js`, `js/decors.js` (5 décors SVG), `js/personnages.js`, palette CSS. Contrôler la syntaxe (`node --check`) et `python <slug>/tests/test_json.py` ; vérifier visuellement (Playwright).
3. Documents : README (solutions générées), `GUIDE-PEDAGOGIQUE.md`, `A-VERIFIER.md`, `CHANGELOG.md`, `assets/README.md`, `assets/medias/CREDITS-medias.md` ; leçons A4 (`outils-lecons/`), affiche et bande-annonce (`outils-medias/`).
4. **Version immersive** : mode A sur ce nouveau jeu (`migrer-jeu.py <slug>`), puis compléter et produire les médias (mode C). On peut aussi n'écrire que la version immersive : partir de `immersifs/<slug>` migré et enrichir (cf. `vingt-mille-lieues/PLAN.md`, `COHERENCE.md` pour la méthode narrative).

## 4. Mode C — Produire ou ajouter des images et des vidéos

Détail : `vingt-mille-lieues/GUIDE-MEDIAS.md`. Outils (copiés dans chaque variante immersive) : `outils/medias/produire.py`, `importer-image.py`, `sources-medias.json`.

1. **Accord et plafonds** : demander à l'enseignant ce qu'il autorise (quels médias, quelle source, quel budget). Par défaut : 4 images, **0 vidéo** ; ne lever les plafonds qu'avec son accord (`--max-images`, `--max-videos`). Toujours commencer par `--essai`.
2. **Source** : `produire.py --liste-sources`. Fournies : `agnes` (images et vidéos), `openai-images`, `exemple-http-generique` (modèle), `fichier-local`. **Ajouter une source** = copier un bloc de `sources-medias.json` (adresse, nom de la variable de clé, noms des champs, chemins de réponse) ; pour un service hors cadre : `"adaptateur": "<fichier>.py"`. Vérifier avec `--liste-sources` puis `--essai`.
3. **Clé d'API** : seulement par variable d'environnement (nom donné par la source) ou ligne dans `cles-api.local` (jamais publié). **Ne jamais l'afficher, l'écrire dans un fichier commité, un journal, un message ou un commit.** Si elle manque, le dire et s'arrêter ; si le réseau bloque un domaine, le dire (Network access de l'environnement) plutôt que de simuler.
4. **Images fournies ou faites ailleurs** : `importer-image.py <fichier|adresse> --decor <id> | --portrait <id> | --depart <vidéo> | --video <nom>` (cumulables : un même fichier peut être fond ET point de départ d'une vidéo) ; ou `--dossier` avec des noms `decor-<id>.png`, `portrait-<id>.jpg`, `depart-<nom>.jpg`, `video-<nom>.mp4`. Renseigner `--source` et `--licence` (crédits automatiques).
5. **Vidéos** : point de départ = image déposée (`--depart`) ou décor déjà déposé (`--depart-decor`) ; les services la lisent par adresse publique (fichier de `assets/medias-depart/` poussé) ; files pleines et quotas sont réessayés ; `--reprendre` reprend un travail créé. La vidéo se pose sur le premier plan de la cinématique du même nom (`transition-e<N>`, `fin-e<N>`, `intro`, `fin`).
6. Regarder des images de chaque média produit avant de le déposer ; l'enseignant choisit (`outils/choisir-medias.html`). Mettre à jour `medias.csv` et les crédits (automatique avec l'import). Les ZIP d'envoi de l'agent sont limités à 30 Mo : découper si besoin.

## 5. Intégration au dépôt (remplacement, nouveau jeu)

`commun/donnees/catalogue.js` (dossier, résumé, couleurs) · `index.html` (carte, couleurs, liste hors connexion) · `verifier.html` (onglet, constructeur, COH_JEUX, COH_COMMUN_6) · `serveur.py` · `demo.html` · `editeur.html` · `outils-docs/maj-journaux.py` · `outils-lecons/brancher_boutons.py` et `verifier.py` · `commun/tests/*` (listes de jeux ; test-pages : compétences, extraits de démo, compteurs) · `outils-tests/moteur-commun.js` · README racine (tableau, liens de test, arborescence, « N jeux ») · `commun/README.md` (compteurs). Ces fichiers sont protégés par le garde-fou : `--autoriser` explicite.

## 6. Tests et commit

1. Tests jsdom : `npm install jsdom@24` dans `$HOME` de la VM, puis `NODE_PATH=$HOME/node_modules node outils-tests/tous.js <slug>` et les tests communs (`commun/tests/test-coherence.js`, `test-greffons.js`, `test-pages.js`, `test-hors-ligne.js`) ; un appel shell dure 180 s au plus : découper. Pour le modèle immersif : `tests/test-immersif.js`, `tests/test-migration.js`, `tests/test-medias-sources.js`.
2. `git branch --show-current` = `escape-games` (ou la branche de la session). `git add` **par chemins nommés** (jamais `-A` hors du dossier du jeu, ni `Constitution 1958/`, ni les PDF, ni `prompts-opus/`, ni `outils-lecons/package-lock.json`), **puis** `python3 outils-pwa/maj-hors-ligne.py` et `git add sw-fichiers.js`, relancer test-hors-ligne. `bash outils-tests/verifier-isolation.sh` → « OK ».
3. Si `.git/index.lock` reste bloqué : demander l'autorisation de suppression du dossier.
4. Un commit en français, message détaillé, terminé par les lignes d'attribution demandées par la session.
5. Cocher le jeu dans `prompts-opus/00-ORDRE-DE-PRODUCTION.md` ; écrire `claude/eg-<slug>.md` dans le projet et mettre à jour `claude/eg-plan-histoire-sciences.md`.

## 7. Fin de session

- Si le contexte approche 80 % : commit d'un état cohérent, puis `RECAP-<slug>.md` à la racine (non commité) : avancement, décisions, fichiers, reste à faire, pièges, phrase pour reprendre.
- Réponse finale courte : ce qui est fait, résultats des tests, points à relire, jeux restants à lancer dans une nouvelle conversation, puis la publication pas à pas. Outil : Invite de commandes Windows (touches Windows + R, taper `cmd`, Entrée) ; `E:` ; `cd "\IDRISS\PROJET ESCAPE GAMES"` ; `git status` ; `git push origin escape-games` ; une minute plus tard, ouvrir l'adresse du jeu (Ctrl + F5).
