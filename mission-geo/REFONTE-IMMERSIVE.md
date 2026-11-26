# Mission géographique — refonte immersive (session 4, audit du 26/11/2026)

Décision de l'enseignante (26/11/2026) : **nouvelle version immersive** `immersifs/mission-geo/`, même moteur
que les autres jeux (5 grades, décors, personnages, voix, coffre, suivi en direct, tableau de bord), avec
**16 escales = les 16 séances** de l'année. L'application actuelle `mission-geo/` reste jouable (« version
classique ») tant que la nouvelle n'est pas finie ; les parties commencées passent de l'une à l'autre sans perte.

## 1. Garantie « rien n'est perdu » (fait dans cette session)

| Étape | Outil |
|---|---|
| Les Chromebooks qui jouent depuis le PC de la classe copient leur mission sur ce PC, à l'ouverture et 3 s après chaque enregistrement | `mission-geo/js/sauvegarde.js` → `POST /api/parties` |
| Chromebook avec l'ancienne version, ou partie jouée sur le site en ligne | `mission-geo/secours-export.html` (même adresse que celle où l'équipe a joué) ou ⚙️ → Progression → Exporter : fichier `.json` |
| Rassembler, vérifier, importer (fusion sans perte, historique gardé) | tableau de bord → **Importer des parties** (`importer-parties.html`) |
| Reprendre sur un autre Chromebook | ⚙️ → Progression → « Reprendre depuis le PC de la classe » |
| Format commun, conversion, fusion | `commun/js/mission-geo-import.js` (format `mission-geo-partie` v2) |
| Rangement | `<dossier des résultats>/parties/mission-geo/<équipe>.json` (+ `_historique/`), jamais publié ni servi en fichier |

### Correspondance pour la future version immersive (à respecter)
- Séance `s01`…`s16` ↔ escale **1…16** (`partie.seances["N"]`, `numero` = N). Une séance réussie = escale réussie :
  toutes ses énigmes marquées résolues, points repris tels quels (pas de bonus), indices du carnet repris.
- Indices (`partie.indices`) : nombre + symbole ou fait sur le pays → mots/objets du journal immersif ; la piste
  finale (`partie.final` : pays, colonne, ligne, code, résolu) → coffre final.
- Niveau → grade : Découverte → `mousse`, CM1 → `matelot`, CM2 → `timonier` (l'enseignante peut imposer un grade à l'import).
- À l'ouverture de la variante immersive : si aucune partie locale, proposer « Reprendre la mission de mon équipe »
  (liste `GET /api/parties?jeu=mission-geo`), puis convertir avec `MISSION_GEO_IMPORT` ; si une partie locale de
  l'application classique existe (`localStorage.mission_geo_annee_a_v1`), la reprendre d'office.

## 2. Audit de l'existant

- 16 séances (5 en P1, 3 en P2, 2 en P3, 3 en P4, 3 en P5), environ 95 activités, une activité « Pour aller plus loin »
  CM2 par séance, palier Découverte (A2), 16 leçons, carnet d'indices, piste finale (pays, case, cadenas), récompense.
- Types d'activités de l'application et équivalent du moteur immersif :

| Application | Nombre | Moteur immersif |
|---|---|---|
| saisie, nombre | 22 | `code` (réponse courte, nombre) ou `trous` |
| qcm | 12 | `qcm` |
| ouverte | 8 | **à transformer** (non corrigeable) : `trous` ou `qcm` à justification, ou trace écrite hors jeu (fiche) |
| etiquettes, tableau | 15 | `plan` (carte SVG à repères numérotés) ou `association` |
| tri, repartition | 8 | `tri` |
| relier | 7 | `association` |
| fait | 6 | indice du carnet (pas une énigme) |
| ordre | 4 | `ordre` |
| vraifaux | 3 | `vraifaux` |
| trous | 3 | `trous` |
| motsmeles, motscroises, anagramme | 5 | `lettres` |
| diagramme | 1 | `instrument` ou `plan` (diagramme SVG) |

- Écarts au modèle (§ 1 du skill) : pas 3 énigmes CM1 / 4 CM2 par salle (de 3 à 7 activités par séance), pas 3 indices
  par niveau (un « coup de pouce »), pas de champ `source` ni `correction` distincte, pas de mot-clé par salle.
- Cartes : `js/cartes.js` dessine déjà en SVG (conforme : jamais d'IA). Les cartes IGN / SANDRE / SHOM demandées
  restent à intégrer comme photos de documents officiels créditées, ou redessinées en SVG avec la source en légende.
- Médias : 93 noms attendus (`assets/README.md`) ; 10 médias sans crédit (AUDIT-MEDIAS).
- Tests : `mission-geo/tests/test-jeu.js` (985 vérifications) à garder verts tant que la version classique existe.

## 3. Étape P1 faite (26/11/2026) : séances 1 à 5

**Construire ou reconstruire** (tout est régénéré, les médias déposés sont gardés) :
`python mission-geo/tests/donnees/construire-immersif.py` (Python 3 + Node ; `NODE_PATH` vers jsdom pour les tests).

| Fichier | Rôle |
|---|---|
| `mission-geo/tests/donnees/gen_escales.py` | énigmes CM1 / CM2, dialogues, leçons, au format des salles → `vingt-mille-lieues/outils/immersif/sources/mission-geo/assets/data/` (la version classique n'est pas touchée) |
| `mission-geo/tests/donnees/fiches.py` | phrases des fiches (leçons CM2), reprises mot pour mot par les justifications |
| `mission-geo/tests/donnees/schemas.py` | cartes à repères numérotés : fonds de `js/cartes.js` (mêmes dessins que la version classique) |
| `mission-geo/tests/donnees/theme-immersif.json` | thème : « Le bureau du Professeur Atlas », mot « séance » |
| `vingt-mille-lieues/outils/immersif/grades/mission_geo_theme.py`, `mission_geo_s1.py` … `_s5.py` | grades Découverte, Géographe, Chef de mission ; palette, voix, portraits, guides |
| `vingt-mille-lieues/outils/immersif/narration/mission-geo.json` | objets, enjeux, réactions du décor, phrases des personnages |
| `mission-geo/tests/donnees/reprise-immersif.js` | reprise des parties (§ 1), ajoutée à `immersifs/mission-geo/js/jeu-config.js` |
| `mission-geo/tests/donnees/construire-immersif.py`, `test-reprise.js` | chaîne complète et test de la reprise |

- Personnages inventés : Professeur Atlas (séance 1), Léna (Dijon), Malik (Clamecy), Zoé (Besançon), Hugo (Les Rousses).
- Mots du coffre : COMMUNE, EMBOÎTÉS, DENSITÉ, TERTIAIRE, TOURISME ; l'indice du carnet de la version classique est redonné à la fin de chaque séance.
- Activités transformées : fiche d'agent « ta commune » et « village ou ville ? » (réponses propres à chaque école) → trace écrite sur la fiche de mission ;
  questions ouvertes des séances 4 et 5 → QCM et vrai/faux de déduction ; mots mêlés et mots croisés → `lettres`, `association`, `tri`.
- Tests : `test-immersif.js` 565 vérifications ; `test-reprise.js` 18 ; version classique `tests/test-jeu.js` 985 (inchangée).
- Non fait : voix mp3 (Edge, à générer sur le PC : `python immersifs/mission-geo/outils/voix/generer-voix.py`), médias, intégration au catalogue
  (le champ `immersif` du catalogue n'est pas posé : l'accueil et le tableau de bord proposent toujours la version classique).

## 4. Plan des prochaines conversations (une période à la fois)

1. ~~**P1 (séances 1 à 5)**~~ (fait, voir § 3) : script `mission-geo/tests/donnees/gen_escales.py` (lit `js/donnees/*.js` par Node, écrit
   `assets/data/enigmes.json` au format des salles, escales 1-5), thème `theme-immersif.json` (Bureau du Professeur
   Atlas, mot « séance »), grades `vingt-mille-lieues/outils/immersif/grades/mission_geo_s1..s5.py`, narration,
   `migrer-jeu.py mission-geo --theme …`, `appliquer-grades.py`, `appliquer-narration.py`, `finir-jeu.py`,
   lecture d'une partie importée (§ 1), tests `test-immersif.js`.
2. **P2 (6 à 8)**, 3. **P3-P4 (9 à 13)**, 4. **P5 (14 à 16) + piste finale et coffre**. Pour chaque période : ajouter les salles à `gen_escales.py`
   (E6…), les leçons et phrases à `fiches.py`, `mission_geo_s6.py`…, la narration, `GUIDES` et `PERIODES`, `INDICES` dans `construire-immersif.py`,
   puis relancer `construire-immersif.py`. Le coffre de la P1 s'ouvre provisoirement après la séance 5 (phrase-bilan de la période).
5. Leçons A4 (les 16 leçons existent : textes courts dans `outils-lecons/textes/mission-geo.json`), évaluations
   imprimables, LSU (`commun/donnees/lsu.js`), familles, fiche de mission, `medias.csv` (16 décors, 5 portraits —
   Professeur Atlas et 4 agents inventés —, 16 vidéos ; prompts complets, aucune image générée ici), affiche et
   bande-annonce (fabrique de nuit), intégration (catalogue `immersif`, accueil, tableau de bord, `demo.html`).

Grades proposés : Découverte (≈ CE2) · Agent CM1 · Agent CM2 · Géographe (6ᵉ) · Chef de mission (5ᵉ) ; 15 à 20 énigmes
par séance seraient trop : viser **3 énigmes par escale (Découverte, CM1), 4 (CM2 et plus)**, la séance restant de 45 min.
