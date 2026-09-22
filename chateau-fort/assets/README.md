# Médias attendus — Le Secret du donjon

**Tout est facultatif.** Sans aucun fichier, le jeu est entièrement jouable : décors et personnages sont dessinés
en SVG animé (`js/decors.js`, `js/personnages.js`). Un fichier déposé au bon endroit, avec le bon nom, remplace
automatiquement le dessin (cascade : vidéo → image → dessin). ⚙️ Réglages → « Vérifier les fichiers présents »
et la page [verifier.html](../../verifier.html#chateau-fort) listent l'état de chaque emplacement.

Aucune photo ni vidéo n'est fournie avec ce jeu. Pour les images d'œuvres, n'utiliser que des images du domaine public
ou sous licence libre, et noter le crédit dans la légende (`enigmes.json`, bloc `media`, champ `source`).

## Décors et cinématiques

| Fichier | Où il apparaît | Sans fichier |
|---|---|---|
| `videos/intro.mp4` | cinématique plein écran au clic sur « Entrer au château » | sautée |
| `videos/salle1.mp4` ou `images/decors/salle1.jpg` | salle 1, la motte et la palissade, et l'écran d'accueil | dessin `motte` |
| `videos/salle2.mp4` ou `images/decors/salle2.jpg` | salle 2, les remparts | dessin `remparts` |
| `videos/salle3.mp4` ou `images/decors/salle3.jpg` | salle 3, la grande salle | dessin `grandesalle` |
| `videos/salle4.mp4` ou `images/decors/salle4.jpg` | salle 4, le village et les champs | dessin `village` |
| `videos/salle5.mp4` ou `images/decors/salle5.jpg` | salle 5, le moulin du seigneur | dessin `moulin` |
| `videos/final.mp4` | cinématique plein écran à la fin (la herse se lève) | sautée |

Format conseillé : vidéo MP4 (H.264) 16/9, 1280 × 720, moins de 20 Mo, boucle de 8 à 15 s sans son indispensable ;
image JPG 1600 × 600 environ, moins de 3 Mo (`.png` et `.webm` sont aussi acceptés).

## Personnages

| Clé | Personnage | Image | Vidéo au repos | Vidéo qui parle |
|---|---|---|---|---|
| `colin` | Colin, page (garçon, 11 ans) | `images/personnages/colin.png` | `videos/personnages/colin.mp4` | `videos/personnages/colin-parle.mp4` |
| `josselin` | Maître Josselin, maître maçon | `images/personnages/josselin.png` | `videos/personnages/josselin.mp4` | `videos/personnages/josselin-parle.mp4` |
| `alienor` | Dame Aliénor, dame du château | `images/personnages/alienor.png` | `videos/personnages/alienor.mp4` | `videos/personnages/alienor-parle.mp4` |
| `mahaut` | Mahaut, jeune paysanne (fille, 11 ans) | `images/personnages/mahaut.png` | `videos/personnages/mahaut.mp4` | `videos/personnages/mahaut-parle.mp4` |
| `perrine` | Perrine, meunière | `images/personnages/perrine.png` | `videos/personnages/perrine.mp4` | `videos/personnages/perrine-parle.mp4` |

Image PNG en pied, fond uni ou transparent, format portrait (environ 600 × 960). Costumes : XIIIe siècle, sobres,
sans armes brandies.

## Illustrations d'énigmes (`images/cartes/`)

| Fichier | Énigme | Contenu suggéré |
|---|---|---|
| `e1-2.jpg` | 1-2 Du bois à la pierre | un chantier de château fort du XIIIe siècle (par exemple Guédelon, photo libre de droits) |
| `e4-1.jpg` | 4-1 Le calendrier des travaux | une page du calendrier des *Très Riches Heures du duc de Berry* (domaine public, musée Condé) |
| `e5-2.jpg` | 5-2 Le registre de Perrine | un moulin à eau médiéval |

## Documents des leçons (`images/documents/`, format `.jpg` uniquement)

| Fichier | Leçon |
|---|---|
| `tres-riches-heures-octobre.jpg` | La vie des paysannes et des paysans — *Octobre : les semailles, devant le Louvre* (domaine public) |
