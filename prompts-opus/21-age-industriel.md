# Prompt n°21 — L'Exposition universelle (Histoire, Année B, période 5)

> À coller tel quel dans une NOUVELLE conversation avec Opus 5, dossier de travail : `E:\IDRISS\PROJET ESCAPE GAMES`. Un jeu par conversation.

---

# MISSION

Créer l'escape game n°21 « L'Exposition universelle » (histoire, CM1/CM2) dans le dépôt, en suivant les sections 1 à 9 ci-dessous.

## 1. Rôle et contexte

Tu travailles dans le dépôt local `E:\IDRISS\PROJET ESCAPE GAMES` (branche git `escape-games`, publiée par GitHub Pages sur https://idgir.github.io/escape-games-cm1-cm2/). Il contient une collection d'escape games pédagogiques HTML autonomes pour CM1/CM2 (élèves de 9 à 11 ans, classes à double niveau, académie de Dijon), conçus pour un enseignant de cycle 3.

Jeux déjà présents : `declaration/` (histoire, la Révolution de 1789), `tour-du-monde/` (géographie), `mission-geo/` (géographie, 16 séances), `constitution/` (EMC, le plus récent : c'est le modèle technique). Tu vas créer UN nouveau jeu, décrit à la section 9. Réponds en français.

## 2. À lire avant d'écrire quoi que ce soit (dans cet ordre)

1. `README.md` à la racine.
2. `constitution/README.md`, surtout « Modifier le contenu » et « Les dix types d'énigmes ».
3. `constitution/GUIDE-PEDAGOGIQUE.md` : modèle du guide enseignant.
4. `constitution/assets/data/enigmes.json` : structure d'une énigme (consigne cm1/cm2, indices, correction, source, blocs cm1 / cm2 / commun, champ `lecon`, bloc `media`).
5. `declaration/assets/data/lecons.json` : format des leçons rédigées en texte.
6. `git show --stat 91238f4` : liste exacte des fichiers d'intégration à toucher pour ajouter un jeu.
7. `programmation histoire-géo sciences 2026.pdf` (racine) : la progression annuelle de l'enseignant. L'extrait qui te concerne est recopié à la section 9.

## 3. Architecture à respecter

- Nouveau dossier `<slug>/` à la racine, créé en copiant le squelette de `constitution/` (index.html, prof.html, css/, js/), puis en remplaçant TOUT ce qui est propre à la Constitution : données, décors SVG, personnages SVG, dialogues, textes d'interface, mentions de source, module concours, fiches officielles PDF.
- Le moteur `js/enigmes.js` est générique (10 types d'énigmes pilotés par JSON) : ne pas le réécrire. Si un type d'énigme supplémentaire est vraiment utile au sujet, l'ajouter dans la copie du moteur de CE jeu seulement, piloté par JSON, avec un test. Ne modifier aucun autre jeu, hors intégration (section 5).
- Leçons : texte rédigé (comme `declaration/` et `tour-du-monde/`), pas de PDF. Une leçon par salle (3 à 4 minutes de lecture, contenu `cm1` et `cm2`, objectifs, lexique, schéma ou frise en SVG quand c'est utile), rattachée à l'énigme par le champ `lecon`, contrôlée automatiquement. Reprendre `js/lecons.js` de `declaration/` si celui de `constitution/` ne gère que des PDF.
- Médias : tout est facultatif. Le jeu doit être entièrement jouable avec des décors et des personnages SVG animés. Ne produis PAS de photos ni de vidéos dans cette session : documente seulement les emplacements attendus dans `assets/README.md`, avec les mêmes conventions de nommage que `constitution/assets/README.md`.
- Le jeu ne doit dépendre d'aucun réseau : pas de CDN, pas de bibliothèque externe, pas de police distante.

## 4. Cahier des charges commun

- 5 salles. 3 énigmes par salle en CM1 (15 au total), 4 en CM2 (20). Une salle = un lieu, une notion principale, un personnage, un mot-clé. Les 5 mots-clés composent la solution finale (formule, mot de passe ou mécanisme de sortie propre au jeu). Durée : 60 à 75 minutes. Barème du moteur v2 (voir la section « Règles du moteur v2 ») : score maximal 185 (CM1) / 235 (CM2), indice = moins 2 points, comme `constitution/`.
- Différenciation réelle CM1 / CM2, pas seulement plus ou moins d'énigmes : vocabulaire, nombre d'éléments, abstraction, précision des dates et des chiffres (repères en CM1, dates exactes en CM2).
- Variété : au moins 7 des 10 types d'énigmes dans le jeu, jamais deux énigmes consécutives du même type dans une salle, au moins une énigme par salle où l'élève manipule (ordonner, placer sur un schéma ou une carte, trier) plutôt que répondre à un QCM.
- Chaque énigme a : une consigne, trois indices progressifs, une correction pédagogique (jamais affichée après la réussite, utilisée dans les documents enseignant), une source, un lien vers la leçon.
- Rigueur factuelle : chaque date, chiffre, nom propre et définition est vérifié dans une source officielle ou de référence (voir section 9). Ne jamais inventer un chiffre. Si une date est discutée, écrire « vers » ou retirer l'information. Si la recherche web est disponible, l'utiliser systématiquement ; sinon consigner les points à contrôler dans `<slug>/A-VERIFIER.md`. Les sources sont citées dans le README du jeu et visibles dans l'interface (pied de leçon, correction).
- Conformité au programme : croiser avec le programme officiel de cycle 3 en vigueur (Eduscol) et avec l'extrait de la progression de l'enseignant (section 9). **Chaque énigme doit être visiblement reliée à une compétence du programme, dès l'ouverture du fichier** : dans `GUIDE-PEDAGOGIQUE.md`, une section « 🎯 Compétences du programme, énigme par énigme » juste après « 1. Place dans les programmes », avec un tableau à quatre colonnes (Salle | Énigme | Type | Compétence du programme) — une ligne par énigme, la compétence reprise mot pour mot ou très près de l'extrait de la progression ; dans `README.md`, une section « 🎯 Compétences du programme (vue d'ensemble) » juste avant la description des salles, avec un tableau condensé (Salle | Compétence du programme). Modèle exact à reproduire : `melanges/GUIDE-PEDAGOGIQUE.md` et `melanges/README.md`.
- Leçons imprimables A4 (obligatoire) : écrire `outils-lecons/jeux/<slug>.py` sur le modèle de `outils-lecons/jeux/melanges.py` (en-tête du jeu, compétence du programme de chaque leçon, cartes, graphiques, schémas et photos du jeu), lancer `python outils-lecons/construire.py <slug>`, ajouter le jeu à la liste `JEUX` de `outils-lecons/brancher_boutons.py` et de `outils-lecons/verifier.py`, puis lancer `python outils-lecons/brancher_boutons.py` : le bouton « 📖 Leçons à imprimer » apparaît dans ⚙️ Réglages. Chaque leçon doit tenir sur une page A4 (contrôle : `outils-lecons/verifier.py`). Mode d'emploi : `outils-lecons/README.md`.
- Contenu : pas d'emoji dans les énoncés, leçons, dialogues et corrections (les icônes d'interface déjà présentes dans le moteur restent). Phrases courtes, lexique de cycle 3, personnages filles et garçons, aucune violence ni peur gratuite.
- Accessibilité : garder les réglages du moteur (taille du texte, animations réduites), contrastes AA, aucune information portée par la seule couleur, jeu utilisable au TBI et sur tablette.
- Supports enseignant : `README.md` du jeu (salles, énigmes, solutions dans des `<details>`, comme `constitution/README.md`) ; `GUIDE-PEDAGOGIQUE.md` (place dans les programmes, prérequis, trois déroulés dont cinq séances de 25 minutes, différenciation, gestion de classe, lexique, évaluation, points de vigilance notionnels, sources) ; impressions A4 (fiches préparatoires, QCM, vrai/faux, étude de documents, avec corrigés) via `evaluations.json` ; tableau de bord enseignant `prof.html`.

## 5. Intégration au dépôt (reproduire le commit 91238f4)

- `index.html` : nouvelle carte de jeu, avec sa couleur.
- `verifier.html` : nouvel onglet dans `ONGLETS` et fonction de construction du jeu, avec test énigme par énigme (`?salle=N&niveau=X&enigme=K`).
- `serveur.py` : liste des jeux dans `/api/fichiers` et messages de démarrage.
- `README.md` racine : tableau des jeux et arborescence.
- `sync.js` et `prof.html` des jeux : identification du jeu par le champ `jeu`, comme dans le commit de référence.
- Vérifier ensuite que les jeux existants se chargent toujours.

## 6. Tests obligatoires (Node + jsdom, comme pour `constitution/`)

- JSON valides, sans clé dupliquée ; chaque énigme pointe une leçon existante ; chaque leçon est citée quelque part.
- Simulation d'une partie complète en CM1 et en CM2 : toutes les énigmes résolues, mots-clés, mécanisme final, coffre final, quizz, scores 185 et 235 (barème v2 : 10 points du premier coup, 3 après une erreur). Tests négatifs (une mauvaise réponse ne valide pas), indices (moins 2 points), mode vérification, réglages, impressions.
- Test de `verifier.html` pour le nouveau jeu.
- Relire les fichiers produits par script (erreurs silencieuses : clés JSON dupliquées, objets JavaScript mal fermés). Corriger par `str_replace` ciblé.

## 7. Git

- Vérifier la branche : `git branch --show-current` doit afficher `escape-games`.
- Ajouter les fichiers par chemins nommés. Jamais `git add .` ni `git add -A` : le dossier `Constitution 1958/` et les PDF sources ne doivent pas être embarqués.
- `git status` peut afficher des dizaines de fichiers « modifiés » qui ne le sont que par leurs fins de ligne (CRLF / LF) : ne PAS les commiter (`git diff --ignore-cr-at-eol --stat` le confirme). Le dossier `prompts-opus/` est un document de travail : ne pas l'ajouter non plus.
- Un commit en français, message clair. NE PAS pousser : `git push` est lancé par l'enseignant, car cet environnement n'a pas accès à ses identifiants GitHub.

## 8. Gestion de la session

- Avance par étapes : squelette, puis données salle par salle, leçons, guides, intégration, tests. Écris les gros fichiers en plusieurs blocs.
- Quand le contexte de la session atteint environ 80 %, arrête-toi proprement : commit de l'état cohérent, puis écris `RECAP-<slug>.md` à la racine du dépôt (à ne PAS commiter) : avancement, décisions prises, fichiers créés, reste à faire, pièges rencontrés, et ce qu'il faut dire pour reprendre. Ce fichier doit permettre de reprendre dans une nouvelle conversation, y compris dans une autre IA.
- Réponse finale courte : ce qui est fait, résultats des tests, ce qui reste, puis la procédure de publication pas à pas. Outil : Invite de commandes Windows. Démarrer : touches Windows + R, taper `cmd`, Entrée. Puis :
  1. `E:`
  2. `cd "\IDRISS\PROJET ESCAPE GAMES"`
  3. `git status` (vérifier qu'il ne reste rien d'inattendu)
  4. `git push origin escape-games`
  5. Une minute plus tard, ouvrir l'adresse du jeu (Ctrl + F5 si la page semble ancienne).

## 9. Le jeu à créer : n°21 — L'Exposition universelle

- Dossier du jeu : `age-industriel/`
- Matière : Histoire. Progression de l'enseignant : Année B, période 5.
- Le titre et le fil narratif sont des propositions : améliore-les si tu as mieux, sans t'éloigner du programme.

**Extrait de la progression de l'enseignant (à couvrir intégralement)**

> Thème 5 : L'âge industriel en France. Energies et machines, travail à la mine, à l'usine, à l'atelier, grands magasins. La ville industrielle : la révolution industrielle et le progrès technique.

**Accroche proposée**

À la veille d'une Exposition universelle, un inspecteur doit rassembler les cinq témoignages de l'industrie : la mine, la machine, l'usine, le grand magasin et la ville. Les élèves, apprentis reporters, reconstituent le panorama d'un siècle qui change.

**Les 5 salles (une notion principale par salle, un mot-clé par salle)**

Pour chaque salle, formule aussi la **compétence officielle correspondante** (BO, cf. l'extrait de la progression ci-dessus) : c'est elle qui alimentera le tableau de compétences décrit à la section 4.

1. Énergies et machines : le charbon, la machine à vapeur, la locomotive, puis l'électricité. Frise, association machine / énergie.
2. La mine : travail des mineurs, dangers, enfants au fond, habitat des corons ; ancrage local possible (Montceau-les-Mines, Le Creusot en Saône-et-Loire). Documents, ordre.
3. L'usine et l'atelier : ouvriers, machines, horaires, salaires, division du travail, premières lois sur le travail des enfants. Tri, vrai/faux.
4. Les grands magasins et la ville industrielle : Bon Marché, Printemps, gares, immeubles, quartiers ouvriers et bourgeois, transports en commun. Plan de la ville, association.
5. Le progrès technique : chemin de fer, télégraphe, photographie, électricité, Exposition universelle de 1889 et tour Eiffel, métro. Frise à remettre dans l'ordre, code final.

**Personnages suggérés** : Un mineur et son fils, une ouvrière de filature, une vendeuse de grand magasin, un ingénieur, un inspecteur du travail.

**Mécanique finale suggérée** : Le pass de l'Exposition : les 5 mots-clés composent le nom d'une invention à reconnaître au dernier écran.

**Sources de référence à consulter et à citer** : Écomusée du Creusot-Montceau, Musée des Arts et Métiers, Musée d'Orsay (Exposition de 1889), Cité des sciences et de l'industrie, Gallica (BnF), Eduscol, Lumni, Histoire par l'image.

**Points de vigilance** : Ne pas présenter la révolution industrielle comme uniquement progrès ou uniquement misère : montrer les deux. Le travail des enfants est un fait historique à traiter sans complaisance. Vérifier les lois citées (1841, 1874, 1892) et leurs contenus exacts. Bilans chiffrés sourcés.

**Liens avec les autres jeux** : Prépare le jeu n°22 (Europe et charbon-acier) ; prolonge les jeux n°04 (objets techniques), n°14 (électricité).

**Rappel des livrables** : dossier `age-industriel/` complet et jouable en CM1 et CM2, `README.md` et `GUIDE-PEDAGOGIQUE.md` du jeu, `assets/README.md` (médias attendus), intégration au dépôt, tests jsdom passés, commit sur `escape-games` (sans push), et `A-VERIFIER.md` si des faits n'ont pas pu être vérifiés en ligne.
