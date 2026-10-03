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

## 4. Matrice programme → escales (alignée sur la programmation de l'enseignant)

Source : `references/programmation-2026.pdf` (programmation histoire, géographie, sciences, Années A et B, P1 à P5),
fournie par l'enseignant après la validation de l'escale pilote. Chaque escale garde l'ordre du roman ; les notions
postérieures à 1870 sont présentées comme un **dossier de l'équipe de secours (carnet du XXIᵉ siècle)** (§ 3 bis, règle 7).

| # | Escale (roman) | Énigmes prévues (lieu → notion) | Programmation (année, période) |
|---|---|---|---|
| 1 | La chasse au « monstre » (*Abraham Lincoln*, 1867) | salle des machines à vapeur → énergies et machines ; cambuse → conservation des aliments, chaîne de production du biscuit de mer ; passerelle → vitesse : distance et durée | Hist. B P5 âge industriel · Sc. A P2 conservation des aliments · Géo B P4 chaîne de production · Sc. B P2 mouvement |
| **2** | **Dans le ventre du Nautilus** | **carré, machines, cabine, salon → électricité, objets techniques, chaîne d'énergie** | **Sc. A P3 électricité · Sc. A P1 objets techniques · Sc. A P2 énergie** ✅ |
| 3 | La forêt de l'île Crespo (promenade sous-marine) | sas → air comprimé, états de la matière ; forêt → lumière sous l'eau ; récif → panorama du vivant, classification | Sc. A P2 lumière · Sc. A P4 panorama du vivant · Sc. B P1 matière |
| 4 | Vanikoro et Lapérouse | épaves → progrès techniques des explorations ; cabine → Louis XVI, contexte de 1789, fin de la monarchie absolue | Hist. B P3 explorations · Hist. A P4 Révolution |
| 5 | Les perles de Ceylan | banc d'huîtres → masses (la perle géante) ; carré → colonies, échanges commerciaux ; pont → inégalités dans le monde | Sc. B P1 masses · Hist. A P3 échanges avec les colonies · Géo B P2 inégalités |
| 6 | Le tunnel arabique et Suez | carte → se déplacer, moyens de transport, canal ; hublot → le Nil, usages de l'eau douce et conflits d'usage | Géo A P1-P2 se déplacer · Géo B P5 eau douce |
| 7 | Santorin et l'Atlantide | volcan sous-marin → la Terre, planète active ; temple englouti → activité interne, séismes | Sc. A P5 / B P5 Terre active |
| 8 | Sargasses, Gulf Stream, câble transatlantique | épave → traite des esclaves et plantations ; câble → communiquer grâce à internet (dossier XXIᵉ s.) ; Gulf Stream → climat, écosystème, chaînes alimentaires | Hist. A P3 traite · Géo A P3-P4 internet · Sc. A P4 écosystème · Sc. B P5 climat |
| 9 | Le pôle Sud (« Faute d'air ») | banquise → états de l'eau, mélanges (eau salée) ; instruments → mesures météorologiques ; drapeau de Nemo → symboles et rites de la République | Sc. B P1-P2 états de la matière, mélanges · Sc. A P1 météo · Hist. B P4 République |
| 10 | Les poulpes | plate-forme → développement des animaux (ovipares) et reproduction ; salon → le cerveau, attention et perception | Sc. B P3 développement · Sc. A P5 reproduction · Sc. B P5 cerveau |
| 11 | Vigo, le Maelström, le coffre | cabine → Louis XIV (1702) ; carte → Europe / Union européenne (la Norvège hors UE) ; poste de pilotage → programmer la manœuvre ; salle de l'orgue → coffre final (Léonard de Vinci et François Ier, tableaux du musée de Nemo) | Hist. A P2 Louis XIV · Géo A P5 UE · Hist. B P5 construction de l'UE · Sc. B P4 programmation · Hist. B P2 Renaissance |

**Non couvert à ce stade, déclaré dans le guide** (ancrage Verne trop artificiel ; ces notions sont travaillées par
d'autres jeux du dépôt) : Moyen Âge (Clovis, Charlemagne, Église, roman/gothique, château fort, paysans), Henri IV et
l'édit de Nantes, Napoléon, les deux guerres mondiales, migrations, organisation du territoire français, besoins
alimentaires (jeu « alimentation »), lois protectrices des libertés.

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
