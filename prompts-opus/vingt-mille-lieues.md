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
   WebFetch — le réseau le bloque probablement ; fie-toi alors à la description du § 7.1 ; **n'en copie ni le
   texte, ni les images, ni le code**) ;
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

### 7.1 Niveau visé et limites honnêtes

Référence de qualité (capture fournie par l'enseignant, page Rakura « La Grande Éclipse d'Astralys ») :
**grandes illustrations peintes très détaillées (une par salle, plein écran 16:9, éclairage dramatique, plan
fixe) sur lesquelles sont posés des effets animés** : fumée et bulles, flammes/lueurs qui pulsent, particules,
reflets, léger mouvement de caméra ; cadre d'interface « de l'univers » (ici une plaque de bois cloutée pour les
dialogues), objets interactifs cliquables dans le décor, roue de réglages discrète.
Équivalent attendu pour Verne : salle des machines, grand salon et sa bibliothèque, hublot sur les récifs,
pont du Nautilus, scaphandres, etc. avec cadre en laiton/rivets, jauges et boiseries.

**Tu ne peux pas générer ces illustrations ni vidéos IA depuis le cloud** (pas de modèle d'image/vidéo, pas
de réseau libre). Ne prétends jamais le contraire et ne simule pas : c'est ton travail de code qui doit rendre
ce niveau **atteignable dès qu'un humain dépose les images**.

### 7.2 Architecture « image peinte + calques d'effets » (à construire)

- Chaque décor = **1 image de fond** (`assets/images/decors/<id>.webp|jpg`, 1920×1080) + un fichier
  `assets/data/decors-fx.json` décrivant ses **effets animés** et ses **zones interactives**, en coordonnées
  relatives (%) pour être indépendants de l'image : émetteurs de bulles/fumée/étincelles, lueurs pulsantes
  (masques radiaux), rayons de lumière, caustiques ondulantes, poissons/bancs traversant, légère parallaxe/zoom
  lent (Ken Burns), vignette, grain, particules flottantes. Rendu Canvas/WebGL léger + CSS, 60 fps sur
  Chromebook, respect de « animations réduites ».
- Variante optionnelle **calques séparés** (`<id>-fond.webp`, `<id>-milieu.webp`, `<id>-avant.webp`, PNG
  transparents) pour une vraie parallaxe quand l'enseignant les fournit.
- **Si l'image est absente**, le moteur affiche le décor dessiné de secours (SVG/Canvas animé) : le jeu est toujours
  jouable. Le décor de secours doit être soigné (dégradés, lumière volumétrique, silhouettes), mais il est
  assumé comme un niveau inférieur.
- **Vidéos** (intro, 10 transitions, fin, bande-annonce) : lecture d'un `.mp4`/`.webm` si présent, sinon
  cinématique en direct (images fixes + Ken Burns + effets + sous-titres + voix + musique). Les fichiers attendus,
  leurs noms, durées (6-10 s transitions, 60-90 s intro, 45 s fin), poids (≤ 6 Mo chacune, H.264, 1280×720)
  sont listés dans `assets/README.md`. Tente un rendu par Chromium/Playwright (déjà installé, ne lance pas
  `playwright install`) + `ffmpeg` s'il existe, pour fabriquer les `.mp4` de secours.
- Personnages : portraits (cadre ovale, respiration, clignement, bouche animée pendant la voix, `narration.js`),
  voix du navigateur + sous-titres. Sons synthétisés (`audio.js`) : ambiance sous-marine, sonar, moteur,
  alarme de pression, orgue de Nemo.

### 7.3 Dossier de production médias (livrable obligatoire, pour que l'humain génère les images/vidéos)

Crée `vingt-mille-lieues/PRODUCTION-MEDIAS.md` (et un `medias.csv`) :
1. **Charte graphique unique** : style (« peinture numérique semi-réaliste, gravure rétro-futuriste victorienne,
   laiton, bois, verre, lumière bleu-vert et ambre »), palette hexadécimale, ratio, cadrage, éclairage, interdits
   (pas de texte dans l'image, pas de personnes réelles, pas de logos), **fiche d'identité de chaque personnage**
   (âge, tenue, traits, accessoires) à recopier à l'identique dans chaque prompt pour garder la cohérence.
2. **Une ligne par média** (fond de chaque salle/escale ≈ 15-20 décors, portraits, objets cliquables, cadre
   d'interface, 12 vidéos) : identifiant, nom de fichier exact, dimensions, durée, **prompt d'image/vidéo complet
   prêt à coller** (en français et en anglais), prompt négatif, zones interactives prévues, effets animés à
   ajouter par le moteur, statut (à produire / livré / secours actif).
3. **Consignes outils** : pour les images, un générateur d'images quelconque ; pour les vidéos, un générateur
   image→vidéo (partir de l'image du décor pour garder la cohérence) ; sinon gravures d'époque du roman
   (Neuville, Riou, domaine public) retraitées. Crédits dans `assets/medias/CREDITS-medias.md`.
4. **Contrôle qualité** : un outil `outils-medias/verifier-medias.py` (ou page `verifier.html`) qui liste les
   médias présents/manquants, leurs dimensions, leur poids, et signale ceux qui ne respectent pas la charte
   (ratio, taille, nom).

### 7.4 Escale pilote (point de validation avant la suite)

Réalise **d'abord l'escale 2 (« Dans le ventre du Nautilus ») de bout en bout** : intro, 3-4 énigmes aux
5 niveaux, décor avec effets animés, personnages, sons, tableau de bord, tests, captures d'écran. Publie-la,
fais un compte rendu avec les captures (1920×1080), puis **enchaîne les 9 autres escales sans attendre**
(l'enseignant relira le pilote en parallèle et pourra demander des ajustements de charte avant la production
finale des images).

### 7.5 Contrat de remplacement : déposer une image générée remplace celle de Claude, sans toucher au code

Exigence forte : **tout média produit par Claude (décor dessiné, image, cinématique) doit pouvoir être remplacé
par un fichier généré par IA, sans modifier une ligne de code**, et **sans régression** si le fichier est mauvais
ou retiré.
- **Convention de noms stable et unique**, documentée dans `assets/README.md` et `medias.csv` :
  `assets/images/decors/<id>.webp` (ou `.jpg`/`.png`, formats acceptés par l'ordre de priorité),
  `assets/images/personnages/<id>.webp`, `assets/videos/<id>.mp4` (ou `.webm`), `assets/images/ui/cadre-dialogue.png`.
  Un fichier déposé **prime toujours** sur le secours généré par Claude (cascade de `media.js`).
- **Tolérance aux dimensions/ratios** : le moteur recadre (`object-fit: cover`) et calcule les effets et zones
  cliquables en % de l'image, donc une image 16:9, 3:2 ou 4:3 fonctionne ; avertissement (pas d'erreur) dans
  `verifier.html` si le ratio s'écarte de 16:9.
- **Effets animés indépendants de l'image** : `decors-fx.json` référence des positions en % ; fournis un
  **outil de calage** (`outils-medias/caler-effets.html`) où l'enseignant clique sur l'image pour replacer
  l'émetteur de fumée, la lueur ou la zone cliquable, et exporte le JSON (pas besoin de coder).
- **Remplacement partiel possible** : un seul décor, un seul portrait ou une seule vidéo peuvent être remplacés ;
  le reste reste en secours. Un bouton « 🖼️ Médias » dans `prof.html`/`verifier.html` montre pour chaque média
  s'il est « Claude (secours) » ou « Fichier déposé » avec aperçu côte à côte.
- **Test automatique** : copie un faux PNG/MP4 sous le nom attendu, vérifie qu'il est servi à la place du secours,
  puis le supprime et vérifie le retour au secours. `sw-fichiers.js` (hors-ligne) doit lister ces chemins.
- Sous-titres, voix et textes restent **dans le code/JSON**, jamais incrustés dans les images ou vidéos, pour que
  tout média remplacé reste compatible.

### 7.6 Prompts prêts à coller, par outil

Dans `PRODUCTION-MEDIAS.md`, pour **chaque média**, fournis une version adaptée à chacun de ces outils, avec ses
spécificités (syntaxe, paramètres, limites) :
- **Midjourney** : prompt anglais descriptif + `--ar 16:9 --style raw --v` (version courante), `--no text, watermark`,
  références `--cref` / `--sref` pour garder personnages et style ; variantes `--ar 3:4` pour les portraits.
- **Flux** (ex. Flux 1.1 Pro / Kontext) : prompt en phrases naturelles longues, ratio 16:9, image de référence
  pour la cohérence ; **Imagen** et **Ideogram** : prompt naturel, ratio 16:9, rappel « sans texte dans l'image ».
- **Vidéo image→vidéo (Runway, Kling, Veo, Luma)** : image de départ = le décor correspondant ; prompt de
  mouvement court (caméra lente, bulles qui montent, lueur qui pulse), durée 5-10 s, boucle si possible, pas de
  personnage qui parle ; liste des plans de transition et de leur image de départ.
- **Ordre de génération conseillé** : 1) portraits de référence des personnages, 2) cadre d'interface, 3) décors
  (en réutilisant style et références), 4) vidéos à partir des décors validés, 5) retouches. Chaque prompt rappelle
  la charte et les fiches personnages à l'identique.
- Pour chaque prompt : critères d'acceptation (« lisible en 1280×720 », « zone de dialogue en bas libre »,
  « pas de texte », « mains correctes »), et **réserve visible pour l'interface** (bas de l'image dégagé).
Ne cite aucun nom d'artiste vivant dans les prompts ; vérifie dans `PRODUCTION-MEDIAS.md` les rappels sur les
conditions d'usage (usage scolaire, publication) à contrôler par l'enseignant.

### 7.7 Génération automatisée via l'API Agnes AI (clé fournie par l'enseignant)

Fournisseur retenu : **Agnes AI** (images : texte→image, édition ; vidéo : image→vidéo, vidéo avec audio
synchronisé). API **compatible OpenAI** ; URL de base `https://apihub.agnes-ai.com/v1` ; authentification par en-tête
`Authorization: Bearer $AGNES_API_KEY`. Index de la documentation : `https://wiki.agnes-ai.com/llms.txt` (lis-le,
puis les pages des modèles d'image et de vidéo : noms de modèles, endpoints, paramètres de ratio/taille/durée,
format de réponse — certaines générations vidéo sont asynchrones : prévois l'interrogation d'état).
**N'invente aucun nom de modèle ni de paramètre** : tout vient de la documentation. Si `wiki.agnes-ai.com` ou
`apihub.agnes-ai.com` est bloqué par le réseau, ou si `AGNES_API_KEY` est absent, livre le script **non testé**
en le disant clairement et continue sans lui.

**Faits vérifiés dans la documentation Agnes (octobre 2026) — à reconfirmer sur `wiki.agnes-ai.com` avant de coder :**
- **Images** : modèle `agnes-image-2.5-flash` (le plus récent ; repli `agnes-image-2.1-flash`). `POST
  https://apihub.agnes-ai.com/v1/images/generations` avec `model`, `prompt`, `size` (`1K`/`2K`/`3K`/`4K`), `ratio`
  (`16:9`, `3:2`, `4:3`, `3:4`, `2:3`, `1:1`, `9:16`, `21:9`), `image` (tableau d'URL publiques ou Data URI base64,
  pour l'image→image et la composition multi-images : **sert à garder la cohérence des personnages et du style**),
  `extra_body.response_format` = `url` ou `b64_json`. Les dimensions exactes (ex. 1920×1080) ne sont **pas natives** :
  demander `size:"2K"`, `ratio:"16:9"`, puis recadrer/redimensionner côté script (Pillow) vers 1920×1080.
  Écris le texte des prompts en tenant compte que le modèle est « haute densité d'information » (scènes riches).
- **Vidéo** : modèles `agnes-video-2.5` (720P/1080P/1K/2K) et `agnes-video-2.5-flash` (720P uniquement, ≤ 5 images
  de référence). `POST /v1/videos` avec `model`, `prompt`, `mode` (`text` | `keyframe` | `reference`), `seconds`
  (`"4"` à `"12"`), `size`, `aspect_ratio`, `seed`, `n`=1 ; `keyframe` accepte `first_frame`/`last_frame` en **URL
  publique** → **image→vidéo = mode `keyframe` avec le décor validé comme `first_frame`** (l'image du décor doit donc
  être accessible par URL publique : utilise l'URL renvoyée par l'API d'images tant qu'elle est valable, sinon
  signale qu'un hébergement public temporaire est nécessaire). Tâche **asynchrone** : récupérer `video_id`, puis
  `GET https://apihub.agnes-ai.com/agnesapi?video_id=<ID>&model_name=<modèle>` toutes les 1-2 s jusqu'à
  `status` = `completed` (champ `url` du `.mp4`) ou `failed`.
- **Coûts** : au moment de la rédaction, images 2.5 Flash et vidéo 2.5 Flash sont affichées à 0 $ (promotion) ; la
  vidéo `agnes-video-2.5` coûte environ 0,025 $/s en 720P. Garde néanmoins les plafonds `--max-*` et affiche un
  coût estimé avant de lancer ; la promotion peut s'arrêter.
- **Clé** : en-tête `Authorization: Bearer …` ; ne jamais exposer dans le code client ni le dépôt.
- Les vidéos générées par l'API n'ont **pas** d'image ni de texte incrustés garantis : prompts « sans texte ». Les
  textes de jeu restent dans le code.

Script **facultatif** `outils-medias/generer-medias.py` (Python standard + `requests` si disponible) :
- lit `medias.csv` (identifiant, type image/vidéo, prompt, ratio, image de départ pour les vidéos) ;
- appelle l'API ; enregistre dans **`assets/medias-proposes/<id>-v1.webp|mp4`** (jamais directement dans
  `assets/images/` ni `assets/videos/`), avec reprise sur erreur et sans régénérer ce qui existe ;
- options `--seulement <id>`, `--variantes N` (2-4 propositions par décor), `--max-images` et `--max-videos`
  (**plafond de coût**), `--essai` (affiche les appels sans les faire), journal `generation.log` ;
- ordre imposé : portraits de référence → cadre → décors → vidéos (image de départ = décor **validé**) ;
- l'environnement peut injecter la clé lui-même (« identifiants API » : la session appelle `apihub.agnes-ai.com`
  sans voir la clé) : le script doit donc fonctionner **sans** `AGNES_API_KEY` (pas d'en-tête `Authorization`
  ajouté) et, si un appel renvoie 401/403, réessayer avec `AGNES_API_KEY` quand elle existe ; sinon s'arrêter
  proprement ;
- la clé n'est lue que dans la variable d'environnement `AGNES_API_KEY` : **jamais écrite** dans un fichier, un
  journal, un commit ou une page web ; `.gitignore` exclut `assets/medias-proposes/` ;
- page `outils-medias/choisir-medias.html` : compare les propositions et le secours de Claude côte à côte ;
  l'enseignant **valide** (téléchargement/renommage vers le nom attendu du § 7.5). Rien n'entre dans le jeu sans
  validation ; refuser une proposition ne change rien (le secours reste).
Les prompts du § 7.6 restent la source de vérité : adapte-les ensuite aux spécificités des modèles Agnes
(version « Agnes » ajoutée à côté de Midjourney/Flux/etc. dans `PRODUCTION-MEDIAS.md`).

### 7.8 Références de style fournies par l'enseignant (à intégrer dans la charte graphique)

Dix-neuf images servent (dix-huit sont dans le dossier ci-dessous ; la capture Rakura n'y est pas) d'étalon de qualité (si un dossier `vingt-mille-lieues/references/` existe, regarde-les ; sinon
fie-toi aux descriptions) :
1. **Décor d'escape game (Rakura)** : peinture numérique très détaillée, plan large 16:9, éclairage dramatique à
   forte teinte dominante (violet/bleu froid + pointes chaudes orange/vert), objets narratifs nombreux et lisibles
   (fioles, livres, gargouille, chaudron), profondeur nette (avant-plan sombre, plan moyen éclairé), cadre
   d'interface en bois et métal cloué pour les dialogues. Effets animés posés dessus (vapeur, flammes, lueurs).
2. **Scène « cabinet victorien » de style cinématographique semi-réaliste** (salon boisé, haute fenêtre sur un
   monument éclairé par un jour pluvieux gris-bleu, cheminée avec vrai feu, globe terrestre en laiton, fauteuil
   Chesterfield en cuir, rideaux de velours à motifs, chapeau haut-de-forme, personnage en costume d'époque tenant
   une montre à gousset) : rendu **photoréaliste de cinéma**, lumière chaude du feu contre lumière froide de la fenêtre,
   matériaux crédibles (bois ciré, cuir, laiton, marbre), personnage expressif bien intégré. **C'est le niveau
   visé pour les scènes avec personnages** (Nemo, Aronnax, Conseil, Ned Land).

3. **Grand salon du Nautilus (référence directe, `references/style-salon-nautilus.png`)** : vaste salon-musée en
   enfilade, boiseries sombres cirées, parquet en point de Hongrie avec tapis à médaillon, lustre à pendeloques,
   appliques en coquillage lumineuses, double étage de bibliothèques à galerie, **grand orgue au fond**, deux
   hublots ronds géants sur l'océan bleu turquoise (lumière froide qui se reflète en caustiques sur le sol), vitrines
   de coraux, coquillages et étoiles de mer au premier plan. Perspective centrale symétrique, profondeur forte,
   éclairage doré chaud des lampes contre le bleu des hublots. **C'est le décor-pivot du jeu** (hub entre les
   escales et salle de l'orgue/coffre final) : décline-le en variantes (de nuit, alarme rouge, pression, panne
   d'électricité, victoire) à partir de cette image de référence, et réutilise ses matériaux dans tous les autres
   décors intérieurs (salle des machines, bibliothèque, cabine, sas). Effets animés prévus : caustiques qui
   ondulent sur le parquet, poissons/bancs derrière les hublots, scintillement du lustre, bulles, poussière en
   suspension dans les rayons.

4. **Cabine du capitaine Nemo (`references/style-cabine-capitaine-1.png`, `-2.png`)** : pièce intime en acajou sombre,
   hublot rond à cadre de laiton riveté sur l'eau bleue avec méduses et poissons, lit-alcôve à rideaux de velours
   vert, fauteuil Chesterfield capitonné vert, **bureau d'acajou couvert de plans, loupe, compas, rouleaux, lampe de
   banquier à abat-jour vert** (zone parfaite d'énigmes à documents), carte du ciel et instruments (horloges, baromètre)
   au mur, **clavier d'orgue/piano** à droite, tapis persan, appliques en forme de coquille Saint-Jacques, grande
   verrière ronde au plafond avec lumière aquatique, globe terrestre, coffret de coquillages. Lumière : lampes
   ambrées + bleu froid du hublot, grain cinéma, profondeur de champ.
5. **Salle des officiers / carré (`references/style-salle-officiers-1.png`, `-2.png`, `-3.png`)** : intérieur de sous-marin
   **métallique riveté vert-de-gris patiné avec lambris et cuivre** (tuyauteries de cuivre, tableau de manomètres et
   cadrans, horloges murales, téléphone-phonographe ancien), grande table de travail en bois entourée de fauteuils
   capitonnés verts, **lampe à pétrole à abat-jour vert**, cartes marines, règles, compas, rapporteur, encrier et plume,
   carafe et verres en cristal, bibliothèque, poêle à feu visible, petit hublot rond sur l'eau, vitrine de coquillages.
   Atmosphère chaleureuse, usée, « vécue ». Contraste voulu avec le grand salon (plus luxueux) : **le Nautilus a
   deux ambiances — salons de bois et de laiton, coursives et salles de travail de métal patiné et de cuivre**.
   Ces pièces servent de décors d'énigmes (cartes, instruments, cadrans, journal de bord).

6. **Salle des machines (`references/style-salle-machines-1.png` à `-4.png`)** : 4 images successives d'un **travelling
   avant** (du sas riveté d'entrée vers le fond) dans une chaufferie/machinerie industrielle de style steampunk
   réaliste : passerelle en caillebotis métallique, **rambardes et tuyauteries de cuivre**, grosses chaudières rivetées
   en cuivre/bronze aux foyers incandescents, charbon répandu au sol, manomètres, volants de vannes, escalier en
   colimaçon, rayons de lumière poussiéreux et vapeur dans la pénombre, dominante brun-cuivre + orange feu + vert-de-gris.
   Ces 4 plans servent de **modèle d'une transition vidéo** (caméra qui avance) : fabrique la vidéo par génération
   image→vidéo (mode `keyframe` avec première et dernière image) ou, à défaut, par un travelling Ken Burns entre
   les 4 plans.
   **Attention à la cohérence avec Verne et les sciences** : cette machinerie est à **vapeur et à charbon**. Le
   Nautilus de Verne est **électrique** (piles au sodium) et n'a ni charbon ni cheminée. Utilise donc ce décor pour
   l'**escale 1 (frégate *Abraham Lincoln*, machine à vapeur, révolution industrielle)** et pour une énigme
   « énergie : vapeur contre électricité » ; pour la salle des machines du Nautilus, décline la même charte en
   **version électrique** (accumulateurs, bobines, tableaux de cadrans de laiton, câbles gainés, lumière bleutée,
   pas de charbon ni de flammes) et mets cette différence dans les énigmes de sciences et dans `A-VERIFIER.md`.

7. **Atlantide / promenade sous-marine (`references/style-atlantide-1.png`, `-2.png`)** : trois scaphandriers en
   scaphandre à casque de laiton à hublots, combinaison de toile épaisse, **bouteilles d'air sur le dos**, tuyaux de
   liaison, lampe-torche à faisceau lumineux, bâton, bottes lestées (cohérent avec la promenade sous-marine de Verne
   et ses appareils à réserve d'air) ; devant les **ruines d'un temple grec** immergé (fronton sculpté, colonnes
   cannelées, deux grandes statues, marches, colonnes brisées couvertes de coraux), méduses, rayons de lumière
   bleue venant de la surface, projecteur du Nautilus au loin. Palette bleu profond + turquoise + pierre blanche
   patinée ; profondeur et échelle (petits personnages devant un grand monument). **Décor de l'escale 7
   (Crète/Santorin/Atlantide)** et des scènes de sorties sous-marines ; adapte la couleur de la pierre et les
   inscriptions selon l'énigme (jamais d'inscription lisible inventée sans la vérifier).
8. **Pont du Nautilus en surface (`references/style-pont-1.png` à `-3.png`)** : coque fuselée en plaques de métal
   rivetées gris argent patinées, **rambardes de laiton**, panneaux d'écoutille à fermoirs, **cage vitrée du pilote
   en laiton (lanterne à facettes)**, **fanal/projecteur de laiton sur pied**, canot encastré sous bâche, compas de
   route en laiton avec feux vert et rouge, volants de vannes, caillebotis ; mer calme, lumière dorée de fin de
   journée, ciel nuageux, **ailerons de cétacés/requins** au loin (clin d'œil au « monstre »). Mouvements : houle,
   écume, reflets, petits nuages ; travelling avant possible (plans 1 → 3). Sert pour l'escale 1 (la
   rencontre avec le « monstre »), le **début et la fin du jeu** et les moments « lever de la tête hors de l'eau ».
   Aucune cheminée ni voile : le Nautilus est électrique.

9. **Le capitaine Nemo (référence officielle du personnage : `references/personnage-nemo-1.png`, `-2.png`)** : homme
   d'une cinquantaine d'années, cheveux gris plaqués en arrière, **barbe poivre et sel taillée**, regard grave, intense et
   mélancolique ; **long manteau/redingote bleu marine à double rang de boutons dorés**, gilet et col blancs sobres,
   chaîne de montre ; posture droite, mains dans le dos ou main posée sur le cadre du hublot, face à l'océan.
   Cadrage : plan américain/mi-cuisse, hublot rond de laiton à sa gauche avec méduses et poissons phosphorescents,
   bibliothèque, lampe à abat-jour vert, carte déroulée et compas sur la table (donc dans sa cabine). Lumière
   latérale bleue froide + ambre chaud, rendu photoréaliste cinéma. **Ce visage et ce costume sont la fiche
   d'identité de Nemo** : recopie sa description à l'identique dans tous les prompts, et passe ces deux images en
   `image` de référence à chaque génération (API images Agnes, mode image→image / multi-images) pour garder la
   même personne dans toutes les scènes. Ton du personnage : énigmatique, cultivé, jamais caricatural ni méchant
   (cf. § 3 : Nemo « vu à travers ses notes »).
   **À produire ensuite, avec la même méthode** (référence = ces portraits + la charte) : Aronnax (savant, 40 ans,
   redingote brune, carnets, regard curieux), Conseil (domestique-classificateur, flegmatique, tenue soignée de
   serviteur, lunettes), Ned Land (harponneur canadien, large, chemise de marin, bonnet, harpon). Génère leurs
   portraits de référence **avant** tout décor avec personnages, fais-les valider par l'enseignant, puis déposes-les
   dans `references/` sous le nom `personnage-<nom>-1.png`.

Cohérence : tous les décors partagent la même lumière (ambre chaud + bleu aquatique par les hublots), les mêmes
motifs (appliques en coquille, hublots ronds rivetés, lampes à abat-jour vert, fauteuils capitonnés verts, tapis
orientaux, laiton/cuivre) et le même rendu cinéma. **Ces motifs forment l'identité visuelle du jeu** : liste-les
dans la charte et répète-les dans chaque prompt de génération.

Traduction pour Verne (à inscrire telle quelle dans la charte de `PRODUCTION-MEDIAS.md`) : mêmes principes
(contraste chaud/froid, matières nobles, détails narratifs, personnage « jouant » une action précise) transposés au
**Nautilus** : grand salon boisé avec bibliothèque et orgue, hublot géant ouvrant sur l'eau bleu-vert éclairée par
les projecteurs, laiton, cuir, cuivre, instruments de navigation, lumière électrique ambrée. Garde **une direction
photoréaliste cinéma pour les scènes à personnages** et **une direction peinture numérique pour les décors
sans personnage**, mais avec la même palette et la même lumière pour que l'ensemble soit homogène.
Pour les vidéos, privilégie les mouvements discrets de ces références : léger travelling, flammes/eau qui bougent,
personnage qui effectue un geste simple (regarde une montre, tourne un globe), jamais de scène d'action rapide.
Rappel : ces captures sont des **références d'ambiance** ; ne reproduis ni leurs personnages, ni leurs objets
distinctifs, ni leurs éléments d'interface.

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
