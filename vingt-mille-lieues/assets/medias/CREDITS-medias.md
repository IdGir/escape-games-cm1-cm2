# Crédits des médias

| Média | Origine | Licence / droits |
|---|---|---|
| `references/*` | créations de l'enseignant (images de référence d'ambiance) | usage dans le jeu par l'enseignant ; ne pas reproduire leurs personnages ni leurs objets distinctifs |
| Décors dessinés, portraits dessinés, icône | dessinés en code SVG/Canvas par Claude (js/decors-secours.js, js/personnages.js) | même licence que le dépôt |
| Sons et ambiances | synthétisés en direct (Web Audio, js/sons.js), aucun fichier | — |
| Voix | voix de synthèse du navigateur | — |
| Polices | Atkinson Hyperlegible, OpenDyslexic (commun/polices, licences dans ce dossier) | SIL OFL |

À compléter pour chaque média déposé : outil, date, prompt (identifiant de `medias.csv`), conditions d'usage vérifiées.

## Vidéos d'ouverture des escales 3 à 11 (3 octobre 2026)
Générées avec Agnes AI (modèle agnes-video-2.5-flash, mode keyframe, 720P, 8 s, 0 $) à partir des décors des escales (images de
départ dans `assets/medias-depart/`), puis dépouillées de leur piste audio. Elles se posent au-dessus du premier plan de chaque
cinématique d'ouverture (la voix et les sous-titres restent dans le code). À valider ou remplacer par l'enseignant : déposer un fichier
`assets/videos/transition-eN.mp4` de même nom.

## Vidéos d'intro et de fin, bande-annonce (4 octobre 2026)
- `intro.mp4` (début de l'escale 1) et `fin.mp4` (après l'ouverture du coffre) : Agnes AI, modèle agnes-video-2.5-flash, keyframe, 720P, 8 s,
  0 $, piste audio retirée. Images de départ : `assets/medias-depart/intro.jpg` et `fin.jpg`.
- `bande-annonce.mp4` (21 s) : montage local de cinq vidéos d'escale avec fondus (`outils/monter-bande-annonce.sh`), sans appel réseau ni coût.

## Vidéos de fin d'escale et d'ouverture de l'escale 2 (4 octobre 2026)
`fin-e1.mp4` à `fin-e11.mp4` et `transition-e2.mp4` : Agnes AI, agnes-video-2.5-flash, keyframe, 720P, 8 s, 0 $, piste audio retirée
(`outils/deposer-videos-cine.py`). Images de départ : `assets/medias-depart/`. Consignes : `outils/prompts-fins-escales.json`.
Elles se posent sur le premier plan de chaque cinématique ; voix, sous-titres et fondu au noir restent dans le code.
