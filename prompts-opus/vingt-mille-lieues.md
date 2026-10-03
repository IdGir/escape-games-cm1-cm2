# Prompt Opus (cloud) — « Vingt mille lieues sous les mers » : escape game immersif

> À coller tel quel dans une session Claude Code cloud (Opus), dépôt `idgir/escape-games-cm1-cm2`.

---

## 0. Ta mission

Tu es développeur·se web et ingénieur·e pédagogique senior. Tu dois **produire un nouvel escape game
complet, immersif et jouable**, adapté du roman de Jules Verne *Vingt mille lieues sous les mers* (1869-1870,
texte tombé dans le domaine public), pour des élèves de **cycle 3 (CM1/CM2)**, avec une **différenciation à
5 niveaux** (du CE2 à la 5ᵉ, sans jamais l'afficher aux élèves).

Le jeu doit :

1. **Couvrir le programme de l'année** (histoire, géographie, sciences et technologie, cycle 3 — CM1 *et* CM2),
   chaque énigme étant rattachée à une compétence précise du programme ;
2. Rester **cohérent avec l'histoire de Verne** : chaque énigme est une péripétie crédible du voyage du Nautilus,
   jamais un exercice scolaire plaqué ;
3. Pousser les élèves à **utiliser leurs leçons comme outil** (et non à cliquer à tâtons) ;
4. Offrir un **environnement totalement immersif** (vidéos d'intro, de transitions et de fin ; décors et personnages
   animés ; sons), dans l'esprit de https://rakura.fr/escape/La-Grande-Eclipse-Astralys (essaie de l'ouvrir avec
   WebFetch pour t'en inspirer : décors animés en couches, ambiance sonore, narration, interface « de l'univers » ;
   **n'en copie ni le texte, ni les images, ni le code**) ;
5. Fournir les outils enseignant : chrono, points, réglages, **tableau de bord**, pause, indices, etc.

**Ne repars pas de zéro.** Le dépôt contient déjà 12 jeux et un moteur v2 mature. Ton travail est d'ajouter un
13ᵉ jeu **sur ce moteur**, en l'étendant proprement là où il est insuffisant (5 niveaux, campagne en escales,
bibliothèque de leçons active), **sans casser les 12 autres jeux**.

## 1. Lis d'abord (obligatoire, avant d'écrire une ligne)

- `README.md` (surtout § 2 ter « Règles de jeu communes », § 4 « Organisation du dépôt »), `AMELIORATIONS.md`
  (**ne reproposer aucune idée déjà listée** ; mettre à jour le catalogue si tu en ajoutes), `commun/README.md`,
  `commun/donnees/catalogue.js`, `outils-moteur/README.md`, `outils-tests/README.md`, `outils-medias/`, `outils-pwa/README.md`.
- Un jeu de référence récent et complet : **`alimentation/`** (structure de dossier, `js/jeu.js`, `assets/data/*.json`,
  `GUIDE-PEDAGOGIQUE.md`, `A-VERIFIER.md`, `README.md`, `prof.html`, `tests/`). Calque l'organisation.
- `mission-geo/` (campagne en séances) et `moyen-age-abbaye/` (coffre final, fermoir) pour les mécaniques longues.
- Si la skill `produire-escape-game` est disponible, **applique sa procédure complète** (faits → données → leçons →
  intégration → tests → commit).
- Programmes officiels : le dépôt cite l'arrêté du 5 juin 2026 (BO n° 24, sciences et technologie) et le programme
  `hg2026` (histoire-géographie). **Revérifie sur education.gouv.fr si le réseau le permet** ; sinon reprends les
  libellés déjà présents dans le dépôt et consigne le doute dans `A-VERIFIER.md`. Aligne-toi sur la logique
  Année A / Année B et P1-P5 du catalogue.

## 2. Règles non négociables du dépôt (moteur v2)

Respecte `README.md § 2 ter` à la lettre, sauf extension explicitement décrite plus bas et documentée :
10 pts juste du premier coup / 3 pts après erreur ; indice −2 pts ; en cas d'erreur on dit **combien** de réponses
sont justes, **jamais lesquelles** ; aucun texte (correction/dialogue) après la réussite ; mot gagné affiché une
seule fois, noté sur la fiche de mission puis retapé au coffre ; lettres cachées mélangées avec leurres ;
indices proposés (jamais imposés) après inactivité ; palier Découverte ; accessibilité (Atkinson/OpenDyslexic,
animations réduites) ; PWA hors-ligne ; fonctionne en double-clic via `serveur.py`/`lancer.bat` comme en ligne.
Mêmes 11 types d'énigmes (`commun/js/enigmes.js`) : n'en invente un nouveau que s'il apporte vraiment de la variété,
avec tests.

Contraintes générales : français correct (accents, typographie), **aucune donnée personnelle**, aucune
dépendance réseau obligatoire (CDN interdits pour le jeu lui-même), pas de clé d'API en dur, polices/sons/images
libres de droits ou générés par le code (documente les crédits dans `assets/medias/CREDITS-medias.md`).

## 3. Scénario et structure

Dossier : `vingt-mille-lieues/` (id : `vingt-mille-lieues`). Titre : *Vingt mille lieues sous les mers — Le Journal
du Nautilus*. Les élèves sont l'**équipage de secours** embarqué à bord du Nautilus à la place de Conseil, d'Aronnax
et de Ned Land : le capitaine Nemo (vu à travers ses notes, jamais caricaturé), le professeur Aronnax, Conseil
(le classificateur) et Ned Land (le harponneur) guident ou taquinent l'équipe. **Fil rouge** : le Nautilus a perdu
ses cartes et son journal de bord à cause d'une avarie ; pour regagner la surface avant que la réserve d'air ne soit
épuisée, l'équipage doit, escale après escale, reconstituer le journal en retrouvant des **fragments** (le mot de
chaque escale) puis ouvrir le **coffre du capitaine** (final).

**Campagne en 10 escales** (≈ 25-30 min chacune, 3 à 4 énigmes par escale ; sauvegarde/reprise ; jouable en
séances séparées ou en continu ; l'enseignant peut **choisir/ordonner les escales** par période P1→P5).
Proposition à ajuster selon le programme réel (tu es libre de réordonner/fusionner, pas de supprimer une
compétence couverte) :

| # | Escale (Verne) | Matière dominante | Pistes de compétences du programme |
|---|---|---|---|
| 1 | La chasse au « monstre » (frégate *Abraham Lincoln*, 1867) | Histoire + technologie | Le XIXᵉ siècle : industrialisation, machine à vapeur, transports ; Second Empire |
| 2 | Dans le ventre du Nautilus | Sciences/technologie | Objets techniques, énergie électrique, circuits, fonctions/ chaîne d'énergie, sas |
| 3 | La forêt de Crespo, Pacifique | Géographie | Océans/continents, repères, latitude/longitude, courants (Kuro Shio), fuseaux |
| 4 | Vanikoro et Lapérouse | Histoire + géo | Louis XVI, Lumières, Révolution (1789), explorations ; Nouvelle-Calédonie (outre-mer) |
| 5 | Les perles de Ceylan | Histoire + géo | Colonisation et abolition de l'esclavage (1848), commerce mondial, Asie |
| 6 | Le tunnel arabique et Suez | Géographie | Canal de Suez (1869), mobilités, échanges maritimes, mondialisation, Égypte |
| 7 | Crète, Santorin, Atlantide | Histoire + sciences | Antiquité (mythes, Grèce, Rome/Gaule selon programme), volcans et séismes |
| 8 | Sargasses et Gulf Stream | Sciences | Écosystèmes, chaînes alimentaires, classification, biodiversité, courants/climat |
| 9 | Le pôle Sud | Sciences + géo | États de l'eau, banquise, saisons/jour polaire, Terre-Lune-Soleil, Antarctique |
| 10 | Vigo, puis le Maelström | Histoire + géo | Louis XIV et la guerre de succession d'Espagne (1702), Europe/UE, marées ; évasion → coffre final |

Si un point du programme CM1/CM2 n'entre dans aucune escale (ex. Moyen Âge, Gaule, Clovis, EMC), trouve **un
ancrage vraiment crédible** (flashback d'Aronnax, relique du musée du Nautilus, bibliothèque de Nemo, légende
vikinge au Maelström…) ou, à défaut, déclare-le honnêtement dans la matrice de couverture (§ 6).

**Fidélité à Verne** : cite brièvement le roman quand c'est utile (extraits courts, authentiques, ponctués de
la page/chapitre) ; signale clairement ce qui est **imaginé par Verne ou anachronique** (ex. vitesse du Nautilus,
Atlantide, date du pôle Sud atteint en 1911 par Amundsen), pour ne jamais enseigner de faux en histoire ou en
sciences. Tous les faits, chiffres et dates sont vérifiés et sourcés ; ce que tu ne peux pas vérifier va dans
`A-VERIFIER.md`.

## 4. Les 5 niveaux de difficulté (jamais appelés CE2/CM1/CM2/6ᵉ/5ᵉ à l'écran)

Nomme-les par des **grades du Nautilus** (ou des profondeurs), à l'écran et dans les réglages élèves :

| Nom affiché (exemple) | Équivalent (réservé au guide enseignant et à `prof.html`) | Profil |
|---|---|---|
| 🐚 Mousse | ≈ CE2 | énigmes courtes, vocabulaire simple, aides renforcées |
| ⚓ Matelot | ≈ CM1 | niveau « cœur de programme » CM1 |
| 🧭 Timonier | ≈ CM2 | niveau « cœur de programme » CM2 |
| 🔭 Lieutenant | ≈ 6ᵉ | raisonnement en deux étapes, documents à croiser, notions de début de cycle 4 abordables |
| 🔱 Second | ≈ 5ᵉ | synthèse, justification rédigée, données chiffrées, pièges de logique |

(Les noms exacts sont à ta discrétion, mais restent maritimes, cohérents et sans correspondance scolaire visible.)

La différenciation doit être **réelle** (contenu, raisonnement et documents différents), pas seulement un nombre
d'énigmes ou une durée différente : dans `enigmes.json`, chaque énigme porte ses **variantes par niveau**
(données, consignes, leurres, type d'énigme possible), avec un tronc de compétences commun. Étends proprement
`palier-decouverte.js`/`variantes.js`/le moteur pour gérer 5 niveaux **sans régression** pour les 12 jeux
existants (les autres jeux gardent CM1/CM2/Découverte). Réglage enseignant : niveau global **ou par équipe**.
Le barème maximal est calculé et documenté par niveau. Les élèves peuvent être invités à « plonger plus
profond » à la fin d'une escale (rejouer à un niveau supérieur) — sans classement humiliant.

## 5. Mécaniques : faire utiliser les leçons

Objectif : **la bonne réponse se trouve dans les leçons, pas au hasard.** Implémente (et teste) :

1. **La Bibliothèque du Nautilus** (⚙️ → leçons) : fiches de leçon courtes, illustrées, consultables à tout moment,
   alignées sur les leçons A4 imprimables (`lecons-a4.json` + `outils-lecons/`). Chaque énigme renvoie à sa leçon
   (« Voir : rayon Océans, fiche 3 ») **sans donner la réponse**.
2. **Énigmes à documents** : les données nécessaires ne sont dans l'énoncé qu'en partie ; l'élève doit consulter
   la leçon/la carte/la frise pour compléter (carte muette à légender avec la leçon, frise à recaler, tableau de
   mesures à interpréter selon la méthode vue en classe).
3. **Bonus « Bien documenté » (+2)** : réussir du premier coup après avoir **ouvert la bonne fiche** (le jeu le
   détecte, sans forcer). **Bonus « Maître-nageur »** : escale sans aucun indice. **Bonus de rapidité** modéré
   (le chrono ne punit jamais les erreurs, cf. règles communes).
4. **Anti-tâtonnement** : barème 10/3 conservé ; en plus, après 3 réponses fausses en 60 s sur une même énigme, un
   **« sas de sécurité »** se verrouille 20 s (puis 40 s…) avec message d'ambiance qui invite à relire la leçon ; les
   énigmes à choix multiples **mélangent** leurs options à chaque essai ; les lettres/codes ont des leurres. Jamais
   de correction ni d'indication des bonnes réponses.
5. **Justification** (niveaux Lieutenant/Second) : certaines énigmes demandent de **choisir la phrase de la leçon**
   qui prouve la réponse (QCM de justification) avant de valider, pour récompenser le raisonnement.
6. **Jauge d'air / de pression** (ambiance + pédagogie) : visuelle, liée au temps restant et aux indices ; **ne
   change pas** le barème sans l'indiquer dans le règlement affiché et dans le guide. Si tu l'utilises pour
   pénaliser, documente-le comme extension des règles § 2 ter.
7. **Journal de bord** : à la fin, compte-rendu par équipe (réussites du premier coup, fiches consultées, notions
   à revoir), exportable/imprimable, relié à `resultats.html` et au passeport de compétences.
8. **Fiche de mission papier** par équipe (déjà dans le moteur), avec 1 case par fragment.

## 6. Outils enseignant et fonctionnalités attendues

- **Chrono** global et par escale (temps accordé par l'enseignant : `minuteur-equipe.js`), **pause** (élève : demande
  de pause ; enseignant : pause/reprise à distance depuis `prof.html`), **points**, classement doux (équipes
  anonymisables), badges.
- **Réglages** (`⚙️`) : niveau (global/par équipe), escales à jouer, durée, indices (activés, coût, délai de
  proposition), anti-tâtonnement, voix/sons/animations, lecture facilitée, mode solo, mode « vérification »
  (`?verif=1`), export/import de partie, impression (fiche de mission, leçons, évaluations, corrigés).
- **Tableau de bord `prof.html`** (mode local, via `sync.js`/`serveur.py`) : une carte par équipe (escale, énigme en
  cours, points, indices, erreurs, fiches consultées, temps), alertes « équipe bloquée », ajout de temps, pause, envoi
  d'un message à une équipe, vue synthèse par notion/compétence, export CSV/PDF.
- **Guide pédagogique** (`GUIDE-PEDAGOGIQUE.md`) : place dans les programmes, **matrice de couverture complète**
  (chaque compétence CM1 + CM2 d'histoire, géographie, sciences → escale/énigme/niveaux ; liste honnête des points
  non couverts), déroulés par période, correspondance niveaux affichés ↔ niveaux scolaires, évaluation, prolongements.
- `README.md` (solutions de **toutes** les énigmes, tous niveaux), `A-VERIFIER.md`, `CHANGELOG.md`,
  `lecons-imprimables.html`, `assets/README.md` (liste des médias attendus).
- Variété des énigmes : mélange tous les types (code, qcm, tri, ordre, association, intrus, trous, lettres, plan,
  vrai/faux…), 35 à 45 énigmes au total ; jamais deux énigmes de même type d'affilée dans une escale ; chaque
  matière représentée à chaque période.

## 7. Immersion audiovisuelle

Cascade de médias déjà gérée par `commun/js/media.js` (vidéo → image → décor dessiné). Fournis **toujours** le
niveau « décor dessiné » (qui marche sans fichier), puis les médias enrichis :

- **Vidéo d'intro** (≈ 60-90 s : légende du monstre, rapport de l'*Abraham Lincoln*, capture, première image du
  Nautilus), **transitions** entre escales (10 courtes, 6-10 s, avec carte animée du trajet du Nautilus et
  sous-titres), **vidéo de fin** (≈ 45 s, selon réussite), bande-annonce 16 s (cf. `outils-medias/bande-annonce.py`).
- **Décors animés en couches (parallaxe)** : rayons de lumière, bulles, poissons, algues, lueur de l'électricité,
  hublot du grand salon, tableau de bord du Nautilus, boussole/profondimètre, carte du monde animée.
  SVG/Canvas/CSS ; fluidité sur Chromebook ; respecte « animations réduites ».
- **Personnages** (portraits animés, voix navigateur + sous-titres, `narration.js`/`personnages.css`) : Nemo, Aronnax,
  Conseil, Ned Land, et un équipage fictif de secours si besoin. Ton bienveillant, humour léger, jamais condescendant.
- **Sons** synthétisés (`audio.js`) : ambiance sous-marine, sonar, moteur, alarme de pression, orgue du salon
  (Nemo joue de l'orgue chez Verne).
- Fabrication des vidéos : essaie, dans cet ordre, ce qui existe dans l'environnement — rendu des décors animés par
  Chromium/Playwright (déjà installé, ne lance pas `playwright install`) puis `ffmpeg` si présent ; sinon livre les
  **cinématiques en HTML/Canvas lues en direct** (même qualité de narration), avec les `.mp4` attendus décrits dans
  `assets/README.md` et un script de production pour la machine de l'enseignant (cf. `outils-medias/`). Poids
  total des médias raisonnable (viser < 40 Mo hors vidéos facultatives), dépôt GitHub Pages compatible.
- Aucun contenu généré par IA qui représente des personnes réelles ; illustrations d'archives libres uniquement
  (gravures de Neuville/Riou, domaine public) avec crédits.

## 8. Qualité, tests, intégration

- Ajoute le jeu au **catalogue** (`commun/donnees/catalogue.js` : hors liste ou nouvelle entrée, `dossier`, couleurs,
  programme), à l'accueil `index.html`, à `annee.html`, `verifier.html`, `editeur.html` (si compatible), `sw.js`/
  `sw-fichiers.js` (hors-ligne), `outils-tests/tous.js` et `README.md` (tableau des jeux, compteurs « douze » → « treize »).
- **Tests automatiques** : `vingt-mille-lieues/tests/test-jeu.js` sur le modèle des autres jeux (partie complète aux
  5 niveaux, barème, erreurs, bonus, verrou anti-tâtonnement, coffre, réglages, impressions, `prof.html`,
  cohérence des JSON). Lance **`node outils-tests/tous.js` : les 12 jeux existants doivent rester verts.**
- Vérifie réellement dans Chromium (Playwright) : parcours d'une escale par niveau, captures d'écran
  (mobile + TBI 1920×1080), console sans erreur, zéro requête réseau externe.
- Relis chaque fait (date, nom, chiffre, notion) et chaque correction d'énigme : une seule réponse possible, sans
  ambiguïté, sans coquille, adaptée à l'âge. Les énigmes de niveaux différents ne doivent pas avoir la même réponse
  recopiable d'un niveau à l'autre.
- Accessibilité : contraste, navigation clavier, texte alternatif, pas de clignotement dangereux.

## 9. Méthode de travail

1. Commence par un **plan écrit court** (`vingt-mille-lieues/PLAN.md`) : matrice programme → escales → énigmes,
   architecture des 5 niveaux, liste des extensions du moteur. Ne demande pas de validation : décide et avance.
2. Procède **escale par escale** : données → leçons → énigmes (5 niveaux) → décors/narration → tests → commit.
   Commits fréquents, messages clairs en français. Pousse régulièrement sur la branche désignée par la session.
3. Étends le moteur dans `commun/` de façon rétro-compatible, avec tests, avant de t'en servir.
4. Termine par : matrice de couverture complète, `A-VERIFIER.md` honnête, README/guide à jour, tests verts,
   et un **compte rendu final** (ce qui est fait, ce qui reste, comment lancer, limites connues).
5. Si une exigence est impossible dans l'environnement cloud (vidéo réelle, réseau, voix), **dis-le clairement** et
   livre la meilleure alternative fonctionnelle plutôt que de la simuler.

**Critère de réussite** : une classe peut ouvrir `vingt-mille-lieues/index.html`, choisir un niveau (sans étiquette
scolaire), voir l'intro, jouer une escale en consultant ses leçons pour réussir, être récompensée pour cela, et
l'enseignant suit tout depuis `prof.html`.
