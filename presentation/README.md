# presentation/ — kit de présentation pour une animation pédagogique ou un conseil de cycle (N21)

Le kit « adopter ce projet » (`adopter.html`, N2) s'adresse à **un** collègue qui veut essayer un jeu.
Ce dossier prépare une **présentation orale à plusieurs collègues à la fois** (animation pédagogique, conseil
de cycle, formation).

| Fichier | Contenu |
|---|---|
| `index.html` | page d'entrée : les supports, les chiffres, les captures (liée depuis `adopter.html`) |
| `diaporama.html` | 11 diapositives, **10 à 15 min** : constat de départ, principe du moteur commun, la collection en chiffres, démonstration, élèves, enseignant, après la partie, séquence avant / après, pour se lancer. ← → pour avancer, **N** pour les notes de l'intervenant, **F** plein écran ; impression : une diapositive par page (A4 paysage, notes comprises) |
| `deroule.html` | **déroulé minuté** de 30 ou 45 minutes, avec un temps de **manipulation par les collègues** (15 min en version complète), préparation, ateliers et plan de première séance à remplir |
| `chiffres.js` | nombre de jeux, de jeux prévus, de matières et de compétences, **calculés** depuis le catalogue (`commun/donnees/catalogue.js`, source de la vue d'ensemble C1) et les leçons de chaque jeu : à jour sans rien refaire |
| `captures/*.jpg` | captures des vraies pages (accueil, jeu, énigme, correction collective, tableau de bord, bilan de classe, année) |
| `capturer.js` | `node presentation/capturer.js` refait les captures (Chrome ou Edge + `npm install` dans `outils-tests`) |

## Principes

- **Rien à installer** pour présenter : un navigateur suffit (le diaporama est une page HTML, il marche aussi
  hors ligne une fois l'application installée ou l'archive décompressée).
- **Données fictives** sur les captures : les équipes et les résultats sont inventés par `capturer.js`
  (« Les Lynx », « Les Hiboux »…), jamais lus sur un appareil.
- **Chiffres à jour** : aucun nombre n'est écrit en dur dans le diaporama ; il lit le catalogue.
- Après une évolution visible d'un jeu ou d'un outil : relancer `node presentation/capturer.js`, relire les
  notes de l'intervenant, et adapter la diapositive concernée.
- `node commun/tests/test-pages.js N21` contrôle la durée du diaporama (10-15 min), celle des deux déroulés
  (30 et 45 min, avec manipulation), les chiffres, les captures et les liens.
