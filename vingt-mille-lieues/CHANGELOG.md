# Journal des versions — Le Journal du Nautilus

## 2026-10-06 — modèle immersif réutilisable, migrateur, sources de médias
- **Migrateur** `outils/immersif/migrer-jeu.py` : transforme un jeu existant (9 migrables) en variante immersive dans `immersifs/<jeu>/`, sans toucher à l'original ; thème, grades et vocabulaire configurables ; `--maj-moteur` met à jour le moteur sans perdre le travail ; rapport des brouillons. Variante de démonstration : `immersifs/renaissance/`.
- **Moteur** : configuration par jeu (`js/jeu-config.js`, `css/theme.css`), vocabulaire du thème (« salle » à la place d'« escale »), énigmes réservées à certains grades (`niveaux`), portraits génériques déduits de la fiche d'un personnage, type « instrument » pris en charge par les corrigés et les tests.
- **Médias** : `outils/medias/` — sources décrites en JSON (Agnes, API compatible OpenAI, modèle à copier, adaptateur Python), clé par variable d'environnement ou `cles-api.local` (jamais publiée), plafonds, reprises (503, 429), vidéos avec point de départ ; `importer-image.py` dépose une image ou une vidéo faite ailleurs comme fond, portrait ou point de départ de vidéo (`--dossier` par noms de fichiers).
- **Garde-fou** `outils-tests/verifier-isolation.sh` : `vingt-mille-lieues/` et `immersifs/` évolutifs, le reste protégé ; `--autoriser <jeu>` pour un remplacement voulu par l'enseignant.
- **Skill** `produire-escape-game` : modes migrer / créer / médias (`outils/skill/produire-escape-game/SKILL.md`).
- Guides : `GUIDE-IMMERSIF.md`, `GUIDE-MEDIAS.md`. Tests : `test-immersif.js`, `test-migration.js`, `test-medias-sources.js` (+ `test_medias_sources.py`).


## 2026-10-04 — fondus au noir et cinématiques de fin
- Toutes les cinématiques se terminent par un fondu au noir (0,9 s ; 0,35 s si on les passe, 0,25 s avec « Animations réduites »),
  l'écran suivant se met en place sous le voile, puis le voile se lève (`VML.fonduNoir` dans `js/app.js`).
- Vidéos des fins d'escale et de l'ouverture de l'escale 2 (voir `assets/medias/CREDITS-medias.md`).

## 2026-10-03 — escales 7 à 11, campagne complète
- Escales 7 (Santorin, Atlantide), 8 (Sargasses, Gulf Stream, traite, câble), 9 (pôle Sud, « Faute d'air »), 10 (poulpes),
  11 (Vigo, Renaissance, Maelström, Union européenne) : 17 énigmes × 5 grades ; nouveaux rayons Terre active, Communication,
  Vivre ensemble ; relecture sceptique (COHERENCE.md § 5) ; scénarimages ; décors Agnes déposés.
- Moteur : paramètre « debut » de la jauge d'air (l'air ne baisse qu'après l'énigme indiquée).

## 2026-10-03 — escales 1 à 6
- Moteur de campagne (escales enchaînées, coffre final, « Plonger plus profond », choix des escales dans les réglages).
- Escales 1 (chasse au monstre), 3 (forêt de Crespo), 4 (Vanikoro), 5 (Ceylan), 6 (Suez) : 16 énigmes × 5 grades,
  alignées sur la programmation 2026 de l'enseignant (PLAN.md § 4) ; relecture sceptique (COHERENCE.md § 4) ; scénarimages.
- Décors générés avec Agnes (images, accord de l'enseignant) et déposés ; travelling vidéo de la salle des machines à vapeur
  monté localement (ffmpeg) à partir des 4 images fournies.

## 2026-10-03 — escale pilote (en attente de validation)
- Plan, base de référence des tests, scénarimage de l'escale 2.
- Escale 2 « Dans le ventre du Nautilus » : 4 énigmes × 5 grades (tri, circuit, association/QCM, ordre/trous), ancrées
  dans 4 décors ; relecture sceptique et corrections (COHERENCE.md).
- Moteur propre au jeu (aucun fichier existant modifié) : décors « image + calques d'effets » (Canvas), zones cliquables,
  type d'énigme « circuit » avec simulation du courant, sas anti-tâtonnement, justification, bonus « Bien documenté »,
  « Maître-nageur », rapidité, jauge d'air (décor), Bibliothèque du Nautilus, journal de bord, réglages, tableau de bord,
  service worker limité au dossier, sons synthétisés, voix et portraits animés.
- Dossier de production médias (charte, fiches personnages, prompts par outil, Agnes), outils de vérification, de calage
  et de choix des médias ; aucun média généré.
