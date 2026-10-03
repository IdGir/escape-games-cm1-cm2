# PLAN — *Vingt mille lieues sous les mers — Le Journal du Nautilus*

13ᵉ jeu du dépôt, cycle 3 (CM1/CM2), 5 niveaux, 11 escales. Cahier des charges :
`prompts-opus/vingt-mille-lieues.md` (il fait foi). Ce plan est court : il fixe les choix ; le détail est
dans `COHERENCE.md`, `GUIDE-PEDAGOGIQUE.md`, `assets/data/enigmes.json`.

## 1. Garde-fou n° 1 : on n'ajoute que des fichiers

- Tout est écrit dans `vingt-mille-lieues/` ; aucun fichier existant n'est modifié (contrôle :
  `bash outils-tests/verifier-isolation.sh` avant chaque commit et chaque push).
- Le jeu **réutilise sans les modifier** deux fichiers du tronc commun, chargés en lecture :
  `commun/js/enigmes.js` (rendu et correction des 11 types d'énigmes : tables `CORPS` et `ACTIVATEURS`,
  `melanger`, `normaliser`) et les polices `commun/polices/` (lecture facilitée). Tout le reste (déroulé,
  5 niveaux, décors animés, sons, voix, tableau de bord) est **nouveau** et propre au jeu.
- Les outils demandés dans `outils-medias/` par le cahier des charges (`verifier-medias.py`,
  `caler-effets.html`, `choisir-medias.html`, `generer-medias.py`) seraient des ajouts **hors des dossiers
  autorisés** par le script d'isolation : ils sont placés dans `vingt-mille-lieues/outils/` ; leur
  déplacement éventuel est décrit dans `INTEGRATION.md`.
- Pas d'intégration à l'accueil, au catalogue, au hors-ligne global, aux tests globaux ni au README dans
  cette PR : tout est préparé dans `INTEGRATION.md`. Le jeu se joue par `vingt-mille-lieues/index.html`, avec
  son propre service worker de portée `vingt-mille-lieues/`.
- Remarque : `outils-tests/tous.js` découvre tout seul les dossiers qui ont un sous-dossier `tests/` ; les
  tests du jeu y apparaissent donc sans modifier ce fichier. Ils doivent rester verts.

## 2. Architecture du jeu (nouveaux fichiers)

```
vingt-mille-lieues/
├── index.html                  le jeu (adresse directe), ?escale=2&niveau=matelot&enigme=1&verif=1
├── prof.html                   tableau de bord enseignant (serveur local serveur.py, API existante)
├── lecons-imprimables.html     Bibliothèque du Nautilus en pages A4
├── sw.js                       service worker limité au dossier (cache propre « vml-… »)
├── css/nautilus.css            interface laiton/rivets, cadre de dialogue, panneaux d'énigme
├── css/enigmes-nautilus.css    habillage des 11 types (+ type « circuit »)
├── js/donnees.js               chargement des JSON (fetch, et repli inline pour le double-clic)
├── js/niveaux.js               les 5 grades, résolution des variantes par niveau
├── js/scene.js                 décor : cascade image déposée → image de référence → décor dessiné ;
│                               calques d'effets Canvas (bulles, lueurs, caustiques, poissons, étincelles,
│                               poussière, Ken Burns, vignette, grain) ; zones cliquables en %
├── js/decors-secours.js        les décors dessinés en SVG (secours)
├── js/personnages.js           portraits SVG animés (respiration, clignement, bouche) + cascade fichier
├── js/sons.js                  sons synthétisés (ambiance sous-marine, sonar, moteur électrique, alarme,
│                               orgue, étincelles) — Web Audio, aucun fichier
├── js/voix.js                  dialogues : voix du navigateur + sous-titres, plaque de laiton
├── js/type-circuit.js          12ᵉ type d'énigme « circuit » (bornes à relier, simulation du courant)
├── js/moteur.js                énigme ouverte depuis l'objet du décor ; barème 10/3, −2 par indice ;
│                               sas anti-tâtonnement ; options remélangées à chaque essai ;
│                               justification (Lieutenant/Second) ; bonus « Bien documenté »,
│                               « Maître-nageur », rapidité ; jauge d'air (décor) ; indices proposés
├── js/bibliotheque.js          Bibliothèque du Nautilus (fiches, rayons), détection des fiches ouvertes
├── js/journal.js               journal de bord de l'équipe (compte rendu imprimable / exportable)
├── js/reglages.js              ⚙️ réglages enseignant, impressions, export/import de partie
├── js/sync-nautilus.js         envoi de l'état au serveur local (même API que commun/js/sync.js)
├── js/app.js                   déroulé : accueil, cinématiques, escales, fin d'escale, sauvegarde
├── assets/data/                enigmes.json (fiches d'ancrage + variantes), decors-fx.json, lecons.json,
│                               dialogues.json, personnages.json
├── assets/images/decors|personnages|ui/   fichiers déposés (priment toujours sur le secours)
├── assets/videos/              intro.mp4, transition-eN.mp4, fin.mp4 (facultatifs)
├── assets/medias/CREDITS-medias.md
├── outils/                     verifier-medias.py, caler-effets.html, choisir-medias.html,
│                               generer-medias.py (Agnes, facultatif), captures.js (Playwright)
├── tests/                      test-jeu.js, test-coherence-narrative.js, test-medias.js
└── PLAN.md, COHERENCE.md, GUIDE-PEDAGOGIQUE.md, README.md, A-VERIFIER.md, CHANGELOG.md,
    PRODUCTION-MEDIAS.md, medias.csv, INTEGRATION.md, BASELINE-TESTS.md, scenarimages/escale-NN.md
```

## 3. Les 5 niveaux (grades du Nautilus)

| Affiché | Clé | Réservé au guide | Différence réelle |
|---|---|---|---|
| 🐚 Mousse | `mousse` | ≈ CE2 | énoncés courts, 3-4 éléments, + aide « Découverte » intégrée : 1ᵉʳ indice offert, un choix faux écarté, fiche mise en évidence |
| ⚓ Matelot | `matelot` | ≈ CM1 | cœur de programme CM1 |
| 🧭 Timonier | `timonier` | ≈ CM2 | cœur de programme CM2, plus d'éléments, vocabulaire précis |
| 🔭 Lieutenant | `lieutenant` | ≈ 6ᵉ | deux étapes, documents à croiser, **justification** (phrase de la fiche qui prouve) |
| 🔱 Second | `second` | ≈ 5ᵉ | données chiffrées, pièges de logique, justification |

Chaque énigme de `enigmes.json` porte un bloc par grade (`mousse`, `matelot`, …) : données, consigne,
indices, et éventuellement un **type différent**. Le moteur commun lit déjà ce schéma : `donneesNiveau(e)`
cherche `e[niveau]`. Réglage : niveau global (⚙️) ou par équipe (choix à l'accueil, ou commande envoyée
depuis `prof.html`). « Plonger plus profond » : à la fin d'une escale, rejouer au grade supérieur.

## 4. Matrice programme → escales (projet ; la pilote est l'escale 2)

| # | Escale | Décors | Programme (libellés du catalogue du dépôt, `hg2026` / `st2026`) | Énigmes (types) |
|---|---|---|---|---|
| 1 | La chasse au « monstre » (1867) | pont de l'*Abraham Lincoln*, salle des machines à vapeur | Âge industriel : énergies et machines (vapeur, charbon), transports | 3 |
| **2** | **Dans le ventre du Nautilus** | **carré, salle des machines électrique, cabine de Nemo, grand salon** | **L'électricité (conducteurs/isolants, circuit, série/dérivation, sécurité) ; objets techniques (fonction d'usage, instruments de mesure) ; chaîne d'énergie** | **4 : tri, circuit, association, ordre** |
| 3 | Forêt de Crespo | sas et vestiaire, récif | Repères (océans, continents, latitude/longitude), courant Kuro-Shio ; sas et scaphandre (objet technique) | 3-4 |
| 4 | Vanikoro et Lapérouse | cabine de Nemo (reliques), récif | Louis XVI, Lumières, explorations ; Révolution (1789) ; Nouvelle-Calédonie | 3-4 |
| 5 | Les perles de Ceylan | carré, banc d'huîtres | Traite et colonies, abolition (1848), échanges ; Asie | 3-4 |
| 6 | Le tunnel arabique et Suez | carré (cartes), pont | Canal de Suez (1869), mobilités, échanges maritimes | 3-4 |
| 7 | Crète, Santorin, Atlantide | promenade, temple englouti | Antiquité (mythes, Grèce) ; Terre active (volcans, séismes) | 3-4 |
| 8 | Sargasses et Gulf Stream | grand salon (hublots), récif | Vivant, biodiversité, écosystème, chaînes alimentaires ; courants et climat | 3-4 |
| 9 | Le pôle Sud | banquise, pont | États de l'eau ; saisons, Terre-Soleil ; Antarctique (continent ≠ banquise) | 3-4 |
| 10 | Les poulpes | plate-forme, salon | Classification (mollusques céphalopodes), régimes, respiration en milieu aquatique | 3-4 |
| 11 | Vigo puis le Maelström | cabine (galion), salle de l'orgue | Louis XIV, guerre de Succession d'Espagne (1702) ; Europe/UE ; marées et courants → coffre final | 3-4 |

Points du programme sans ancrage naturel (Moyen Âge, Gaule, Clovis, Renaissance, guerres mondiales, EMC…) :
ancrages proposés dans la bibliothèque de Nemo ou le musée du Nautilus — à arbitrer **après** la pilote ;
sinon déclarés « non couverts » dans la matrice du guide. Total visé : 38 à 42 énigmes.

## 5. Escale pilote (point d'arrêt obligatoire)

Escale 2 seule, de bout en bout : scénarimage (`scenarimages/escale-02.md`), 4 énigmes × 5 grades ancrées
dans 4 décors, `COHERENCE.md` (relecture sceptique : 4 questions par énigme), décors animés (références de
l'enseignant + secours dessinés), personnages, sons, tableau de bord, tests, captures 1920×1080 et mobile.
Puis **arrêt** et compte rendu ; aucune autre escale avant validation.

## 6. Médias

Aucun média généré sans l'accord de l'enseignant. Livrés : décors dessinés en code (secours), dossier
`PRODUCTION-MEDIAS.md` + `medias.csv` (charte, fiches personnages, prompts par outil, Agnes), script Agnes
facultatif **testé seulement en mode `--essai`** (aucun appel payant ou non), plafonds `--max-images`
/`--max-videos`. Les images de `references/` (créations de l'enseignant) servent de **décor intermédiaire**
quand aucun fichier n'est déposé (basse définition, signalé « référence » dans les vérifications).
