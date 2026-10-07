# Escape games histoire et sciences : ordre de production et prompts Opus 5

Généré le 20/09/2026 à partir de `programmation histoire-géo sciences 2026.pdf` et des jeux présents dans le dépôt.

## Déjà fait (à ne pas refaire)

| Jeu existant | Ce qu'il couvre dans la progression |
|---|---|
| `declaration/` Le Secret de la Déclaration | Histoire, Année A, P4 : contexte de 1789, fin de la monarchie absolue, nouveaux principes |
| `constitution/` Le Sceau de la République | EMC, Constitution de 1958 ; couvre en grande partie « lois protectrices des droits et des libertés » (Année B, P4) |
| `mission-geo/` et `tour-du-monde/` | Géographie (hors périmètre de cette liste) |

Non couvert et hors périmètre demandé : géographie Année A (se déplacer, internet, Union européenne). Le jeu `mission-geo/` couvre en réalité les thèmes de la ligne « Année B » de la progression (organisation du territoire, inégalités, se nourrir, eau douce).

## Ordre de production (26 jeux)

Classés dans l'ordre du calendrier scolaire : la période 1 est en cours, on commence donc par elle. Dans une même période, les jeux Année A et Année B alternent : si votre classe suit l'Année A cette année, faites d'abord les jeux marqués A (et inversement).

| N° | Jeu | Matière | Année | Période | Compétence(s) du programme | Fichier prompt | Fait |
|---|---|---|---|---|---|---|---|
| 01 | Le Manuscrit de l'abbaye | Histoire | A | P1 | Décrire le rôle social de l'Église (pauvres et malades, enseignement) ; différencier art roman et art gothique. | `01-moyen-age-abbaye.md` | [ ] |
| 02 | Le Secret du donjon | Histoire | B | P1 | Décrire les fonctions d'un château fort ; raconter la vie quotidienne des paysannes et des paysans. | `02-chateau-fort.md` | [ ] |
| 03 | La Station météo disparue | Sciences | A | P1 | Réaliser et exploiter des mesures météorologiques avec des capteurs (thermomètre, anémomètre, pluviomètre). | `03-station-meteo.md` | [ ] |
| 04 | L'Atelier de l'inventeur | Sciences | A | P1 | Décrire le fonctionnement et la constitution d'objets techniques. | `04-objets-techniques.md` | [ ] |
| 05 | Le Laboratoire de Madame Mélange | Sciences | B | P1 | Comparer/mesurer des masses ; distinguer mélanges homogènes/hétérogènes ; séparer leurs constituants. | `05-melanges.md` | [ ] |
| 06 | De l'édit de Nantes à Versailles | Histoire | A | P2 | La naissance du protestantisme (édit de Nantes) ; la monarchie absolue à Versailles. | `06-versailles.md` | [x] |
| 07 | L'Atelier de Léonard à Amboise | Histoire | B | P2 | François Ier, protecteur des arts et des lettres à la Renaissance (Léonard de Vinci). | `07-renaissance.md` | [x] |
| 08 | Le Grand Repas du chef | Sciences | A | P2 | Besoins alimentaires et nutrition humaine (programme 2026 : besoin de matière pour grandir, variation des besoins, mastication et digestion, circulation sanguine et effort ; « production et conservation des aliments » ne figure plus au programme). | `08-alimentation.md` | [x] (commit 3f8fe6e, 03/10/2026, à pousser) |
| 09 | Le Phare de l'île Lumière | Sciences | A | P2 | La lumière (matière, mouvement, énergie et information). | `09-lumiere.md` | [x] (commit 09603ba, 03/10/2026, à pousser) |
| 10 | La Fabrique des états | Sciences | B | P2 | États et constitution de la matière à l'échelle macroscopique ; propriétés de la matière. | `10-etats-matiere.md` | [ ] |
| 11 | Le Grand Prix de l'observatoire | Sciences | B | P2 | Mesurer une distance et une durée lors d'un déplacement ; différents types de mouvement. | `11-mouvement.md` | [ ] |
| 12 | Les Archives du port | Histoire | A | P3 | La traite des esclaves Afrique-Amérique ; les échanges commerciaux avec les colonies. | `12-traite-colonies.md` | [ ] |
| 13 | La Caravelle du capitaine | Histoire | B | P3 | Les progrès techniques des explorations ; la constitution des premiers empires coloniaux. | `13-grandes-explorations.md` | [ ] |
| 14 | La Centrale en panne | Sciences | A | P3 | L'électricité. | `14-electricite.md` | [ ] |
| 15 | La Nurserie du zoo | Sciences | B | P3 | Étapes du développement des animaux (fécondation à la naissance) ; reproduction ovipare/vivipare. | `15-naissances-animaux.md` | [ ] |
| 16 | Le Testament de l'Empereur | Histoire | B | P4 | Napoléon, du général à l'empereur ; lieux, symboles et rites de la République ; lois protectrices des libertés. | `16-napoleon-republique.md` | [ ] |
| 17 | L'Expédition biodiversité | Sciences | A | P4 | Panorama du vivant, biodiversité ; structure et dynamique d'un écosystème. | `17-vivant-ecosystemes.md` | [ ] |
| 18 | Le Robot de l'atelier | Sciences | B | P4 | Traduire un langage simple en langage naturel ; utiliser un programme pour agir sur un objet technique. | `18-programmation-robot.md` | [ ] |
| 19 | Les Lettres du poilu | Histoire | A | P5 | Première Guerre mondiale : causes, déroulement, conséquences. | `19-grande-guerre.md` | [ ] |
| 20 | Radio Londres | Histoire | A | P5 | Seconde Guerre mondiale : montée des extrêmes, collaboration et résistance, victoire des alliés. | `20-seconde-guerre.md` | [ ] |
| 21 | L'Exposition universelle | Histoire | B | P5 | Énergies et machines ; la ville industrielle, révolution industrielle et progrès technique. | `21-age-industriel.md` | [ ] |
| 22 | Le Traité perdu de Rome | Histoire | B | P5 | La construction européenne : CECA, CEE, UE (monnaie unique, institutions). | `22-europe.md` | [ ] |
| 23 | L'Observatoire des volcans | Sciences | A | P5 | La Terre, une planète active (activité interne). | `23-terre-active.md` | [ ] |
| 24 | Le Jardin de la vie | Sciences | A | P5 | La reproduction sexuelle chez le vivant. | `24-reproduction.md` | [ ] |
| 25 | Le Labo des illusions | Sciences | B | P5 | Le cerveau ; mécanismes perceptifs ; stratégies d'attention et de mémorisation. | `25-cerveau.md` | [ ] |
| 26 | Mission Climat | Sciences | B | P5 | Définir le climat local ; conséquences du changement climatique, atténuation/adaptation. | `26-climat.md` | [ ] |

Regroupements possibles si vous voulez moins de jeux : 19 + 20 (les deux guerres mondiales), 15 + 24 (reproduction), 10 + 11 (matière et mouvement).

## Une conversation par jeu, l'une après l'autre

Oui : ouvrir une nouvelle conversation pour chaque jeu, et les enchaîner (pas en parallèle).

- Un jeu complet (15 à 20 énigmes, décors SVG, leçons, guides, tests jsdom) remplit un contexte : au-delà, la qualité baisse.
- Chaque jeu retouche les mêmes fichiers partagés (`index.html`, `verifier.html`, `serveur.py`, `README.md`) : deux conversations en même temps se marcheraient dessus.
- Chaque prompt est autonome : la nouvelle conversation n'a besoin d'aucun historique.
- Faire le n°01 en pilote. Si le résultat vous convient, enchaîner ; sinon dites-le-moi et j'ajuste le socle commun avant de lancer les 25 suivants.

## Lancer un jeu, pas à pas

Outil : l'application Claude sur votre ordinateur, avec accès au dossier du dépôt.

1. Nouvelle conversation ; choisir le modèle Opus 5 et le dossier de travail `E:\IDRISS\PROJET ESCAPE GAMES`.
2. Ouvrir le fichier prompt du jeu (colonne « Fichier prompt ») avec le Bloc-notes. Ctrl + A, Ctrl + C.
3. Coller dans la conversation (Ctrl + V) et envoyer.
4. À la fin, Opus 5 vous donne les commandes de publication ; vérifier qu'il indique `escape-games` comme branche.
5. Publier : touches Windows + R, taper `cmd`, Entrée, puis `E:`, `cd "\IDRISS\PROJET ESCAPE GAMES"`, `git status`, `git push origin escape-games`.
6. Cocher la case « Fait », passer au jeu suivant dans une nouvelle conversation.

Si une conversation approche de 80 % de contexte, elle écrit `RECAP-<jeu>.md` à la racine du dépôt (à ne pas commiter) : coller ce fichier dans une nouvelle conversation, avec le prompt du jeu, pour reprendre.

## Notes

- Les scénarios, titres et découpages en salles sont des propositions : Opus 5 peut les améliorer, mais le contenu de la colonne « programme » doit être couvert.
- Trois jeux touchent des sujets sensibles (n°12 traite et plantations, n°19 et n°20 guerres mondiales) : relire attentivement avant de les proposer aux élèves.
- Les faits (dates, chiffres) sont à vérifier par Opus 5 sur des sources officielles ; les points non vérifiés sont listés dans `A-VERIFIER.md` de chaque jeu.

## Règles du moteur v2 (octobre 2026) — obligatoires

Le jeu utilise le moteur d'énigmes v2 (fichiers maîtres dans `outils-moteur/`, voir `outils-moteur/README.md` ; s'installe avec `python outils-moteur/installer.py`, en ajoutant le slug du jeu à la liste `JEUX`) :
- Barème : énigme juste **du premier coup = 10 points**, après une erreur = **3 points** ; coffre final 10 / 3 ; bonus de rapidité 3 points par salle ; indice = moins 2 points. Score maximal 185 (CM1) / 235 (CM2). Le barème est rappelé en tête de chaque énigme : les élèves doivent être poussés à relire la leçon avant de valider.
- Chaque énigme se valide par un bouton. En cas d'erreur, n'afficher que **le nombre** de réponses justes (« 2 associations justes sur 4 »), jamais lesquelles ; une réponse incomplète n'est pas une erreur.
- **Aucun texte après la réussite** : ni correction, ni explication, ni dialogue de réussite (`dialogue_reussite` n'est pas joué). Le champ `correction` reste dans `enigmes.json` pour le README, les guides et les corrigés imprimés. Le bouton suivant apparaît tout de suite ; un personnage qui parle ne bloque jamais le jeu ni le chrono.
- **Mots à noter** : le mot-clé de fin de salle s'affiche une seule fois (« Notez ce mot ») ; les élèves le recopient sur la **fiche de mission** imprimable (⚙️ Réglages › Impression) et le retapent dans le **coffre final**. Ne jamais rassembler les mots automatiquement.
- **Énigmes « lettres »** : les lettres marquées sont **dans le désordre** dans le texte et accompagnées d'**au moins deux leurres** ; les élèves les rangent dans les cases.
- Tests : en plus des tests jsdom, faire passer `outils-moteur/tester_parties.py` (normal et `--toutes-fausses`) après avoir ajouté le jeu à sa liste.
