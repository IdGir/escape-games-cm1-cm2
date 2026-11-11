# Médias attendus — Les Archives du port

**Tout est facultatif.** Sans aucun fichier, le jeu est entièrement jouable : décors et personnages sont dessinés
en SVG animé (`js/decors.js`, `js/personnages.js`). Un fichier déposé au bon endroit, avec le bon nom, remplace
automatiquement le dessin (cascade : vidéo → image → dessin). ⚙️ Réglages → « Vérifier les fichiers présents » liste
l'état de chaque emplacement.

Règles du projet : **lieux et documents réels** = photographies réelles sous licence libre (Wikimedia Commons : salles
d'archives, registres, musées) ; **personnages** = réalistes mais **jamais de personnes réelles** (tous inventés) ;
**cartes et schémas** : dessinés, jamais générés par IA. **Sujet sensible** : aucune image de violence, de chaînes, de
corps ou de navire négrier chargé de captifs ; aucune image générée par IA représentant des personnes réduites en
esclavage. Aucun média n'a été produit : la production se fait seulement avec l'accord de l'enseignant.
Crédits dans `assets/medias/CREDITS-medias.md`.

## Décors et cinématiques

| Fichier | Où il apparaît | Sans fichier | Contenu suggéré |
|---|---|---|---|
| `videos/intro.mp4` | cinématique au clic sur « Entrer aux Archives » | sautée | la façade d'un bâtiment d'archives sur un quai, un matin d'automne |
| `videos/salle1.mp4` ou `images/decors/salle1.jpg` | salle 1, la salle des cartes, et l'écran d'accueil | dessin `cartes` | meubles à plans, carte ancienne de l'Atlantique (photo libre) |
| `videos/salle2.mp4` ou `images/decors/salle2.jpg` | salle 2, le cabinet des registres | dessin `registres` | étagères de registres reliés, maquette de navire de commerce (sans captifs) |
| `videos/salle3.mp4` ou `images/decors/salle3.jpg` | salle 3, le fonds des colonies | dessin `colonies` | salle de lecture, plan ancien d'habitation, livre ancien sous vitre |
| `videos/salle4.mp4` ou `images/decors/salle4.jpg` | salle 4, le musée du port | dessin `musee` | vitrines de musée, barriques, sacs de toile |
| `videos/salle5.mp4` ou `images/decors/salle5.jpg` | salle 5, la salle de lecture | dessin `lecture` | grande salle de lecture claire, longues tables |
| `videos/final.mp4` | cinématique de fin | sautée | un registre que l'on referme, la lumière d'une lampe |

## Personnages (inventés)

`images/personnages/<nom>.png` ou `videos/personnages/<nom>.mp4` (+ `<nom>-parle.mp4` facultatif) :
`ines` (archiviste), `malik` (historien venu de Dakar), `celia` (historienne venue de Guadeloupe),
`margot` (conservatrice du musée du port), `theo` (élève de l'atelier d'enquête).

## Illustrations d'énigmes

Aucune pour l'instant. Une énigme accepte un bloc `"media"` dans `enigmes.json` (`{"base":"e3-2", ...}` ; fichier
`images/cartes/e3-2.jpg`). Idées compatibles avec les règles : la première page de l'édit de mars 1685 (archives,
domaine public), une gravure du décret de 1848, le portrait de Victor Schœlcher (domaine public) ; jamais d'image de violence.
