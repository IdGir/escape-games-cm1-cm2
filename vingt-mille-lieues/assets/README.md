# Médias du jeu — noms attendus

Déposer un fichier **sous ce nom exact** le fait apparaître dans le jeu, sans toucher au code ; le retirer ramène le secours.
Liste complète, statut et prompts : `../medias.csv` et `../PRODUCTION-MEDIAS.md` ; contrôle : `../medias.html`,
`python ../outils/verifier-medias.py`.

| Emplacement | Nom attendu | Format | Secours actuel |
|---|---|---|---|
| Grand salon | `images/decors/salon.webp` (ou `.jpg`, `.png`) | 1920 × 1080, 16:9 | image de référence `references/style-salon-nautilus.png`, sinon décor dessiné |
| Carré des officiers | `images/decors/carre.webp` | 1920 × 1080 | référence `style-salle-officiers-3.png` |
| Salle des machines électrique | `images/decors/machines.webp` | 1920 × 1080 | décor dessiné (aucune référence électrique) |
| Chambre du capitaine | `images/decors/cabine.webp` | 1920 × 1080 | référence `style-cabine-capitaine-2.png` |
| Portraits | `images/personnages/nemo.webp`, `aronnax.webp`, `conseil.webp`, `ned.webp` | 3:4, ≥ 600 × 800 | portraits dessinés animés |
| Cadre de dialogue | `images/ui/cadre-dialogue.png` | PNG transparent | cadre CSS (prévu ; non branché dans la pilote) |
| Cinématique d'escale 2 | `videos/transition-e2.mp4` (ou `.webm`) | 1280 × 720, H.264, 6-10 s, ≤ 6 Mo | cinématique en direct (décors + voix + sous-titres) |
| Intro, fin, autres transitions, bande-annonce | `videos/intro.mp4`, `fin.mp4`, `transition-eN.mp4`, `bande-annonce.mp4` | idem | prévus avec les escales suivantes |

Formats acceptés par ordre de priorité : `.webp`, `.jpg`, `.png` (images), `.mp4`, `.webm` (vidéos). Une image 3:2 ou 4:3 marche
aussi (recadrage automatique) ; recaler alors les zones avec `../outils/caler-effets.html`. Noms en minuscules, sans espace ni accent.
Propositions générées (non publiées) : `medias-proposes/`.
