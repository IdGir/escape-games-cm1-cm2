# Le Jardin de la vie — escape game de sciences (cycle 3, jeu n°24)

Sciences et technologie, programme 2026 (BO n° 24 du 11 juin 2026, annexe 2), « Les êtres vivants dans leur environnement » (CM1 « Reproduction, croissance et développement » et « Unité et diversité du vivant », 6e « Reproduction, croissance et développement ») ; progression de l'enseignant : année A, période 5 :
*Le vivant, sa diversité et les fonctions qui le caractérisent. La reproduction sexuelle.*

**Jouer** : version immersive `../immersifs/reproduction/` (5 grades : Visiteur du jardin ≈ CE2, Apprenti jardinier ≈ CM1, Naturaliste ≈ CM2, Botaniste ≈ 6ᵉ, Directeur du jardin ≈ 5ᵉ).
Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas écrite.

**Vigilance** : plantes et animaux seulement ; la reproduction humaine et la puberté ne sont pas abordées (partie « Puberté et reproduction humaine » du programme, menée à part par l'enseignant). Pas d'anthropomorphisme. Jardin, ferme et personnages inventés.

## Fil narratif

Cette nuit, un orage a ouvert la serre du jardin des Coteaux (inventé, Bourgogne) et les barrières de la ferme voisine : planches, cahiers, graines et registres sont mélangés, et le portail entre le jardin et la ferme s'est verrouillé. Les élèves, apprentis naturalistes, aident cinq personnes et rassemblent cinq mots qui ouvrent le portail :
> La FLEUR reçoit le POLLEN et devient un fruit plein de GRAINES ; chez les animaux, la FÉCONDATION donne un petit de la même ESPÈCE que ses parents.

| Salle | Lieu | Guide (personnage inventé) | Mot |
|---|---|---|---|
| 1 | La serre du jardin des Coteaux | Basile, botaniste, responsable de la serre du jardin des Coteaux | FLEUR |
| 2 | Le rucher au fond du jardin, près du verger | Capucine, apicultrice, elle s'occupe des ruches du jardin | POLLEN |
| 3 | Le potager de l'école, au bord du jardin | Tom, élève de CM2, jardinier du potager de l'école voisine | GRAINES |
| 4 | La cour de la ferme des Coteaux, près de l'étang | Yasmine, éleveuse de la ferme des Coteaux | FÉCONDATION |
| 5 | La bergerie de la ferme et la mare voisine | Nadia, vétérinaire des animaux de la ferme | ESPÈCE |

## 🎯 Compétences du programme (vue d'ensemble)

| Salle | Compétence du programme |
|---|---|
| 1 | Identifier les organes reproducteurs de la fleur (étamines, pollen, pistil, ovaire, ovules) — première approche de la reproduction des plantes à fleurs (programme de 6e) ; vocabulaire mobilisé par le programme : pollen, pistil |
| 2 | Mettre en évidence le rôle de la pollinisation dans la transformation de la fleur en fruit et des ovules en graines ; illustrer la coopération par la pollinisation ; relier insecticides et pollinisateurs (programme de 6e, première approche en CM1-CM2) |
| 3 | Ordonner les étapes de la vie d'une plante à fleurs : germination, croissance, fleur, fruit, dispersion des graines (rappel du CE2) ; besoins de la germination (démarche expérimentale) |
| 4 | Mettre en relation le type de fécondation (interne ou externe) avec le mode de reproduction des animaux (CM1) |
| 5 | Décrire les étapes du développement des animaux de la fécondation à la naissance ; distinguer ovipares et vivipares (CM1) ; définir une espèce comme un ensemble d'individus interféconds (CM1) ; diversité des individus et variation héréditaire (6e) |

CM1 : 3 énigmes par salle (15) ; CM2 : 4 énigmes par salle (20). Repères en CM1 (pétale, étamine, pistil, fécondation dans le corps ou dans l'eau, œuf ou ventre de la mère) ; vocabulaire précis en CM2 (sépale, ovaire, stigmate, gamète, interne, externe, ovipare, vivipare, larve, espèce) et durées (21 jours, 9 mois, 5 mois).

## Solutions (générées depuis `assets/data/enigmes.json`)

### Salle 1 — La serre du botaniste — La fleur (mot : **FLEUR**)

<details><summary><b>1-1 La planche tombée</b> (plan)</summary>

Le repère 1 montre un pétale, coloré ; le repère 2 une étamine, dont le bout fabrique le pollen ; le repère 3 le pistil, au centre de la fleur. En CM2 : le repère 4 est un sépale, vert, sous les pétales ; le repère 5 est l'ovaire, la partie renflée du pistil, qui contient les ovules. Une racine et une graine ne sont pas des pièces de la fleur.

</details>

<details><summary><b>1-2 Les fiches des pièces de la fleur</b> (association)</summary>

Les pétales, souvent colorés, attirent les insectes ; les étamines, organes mâles, fabriquent le pollen ; le pistil, organe femelle, contient les ovules dans son ovaire. En CM2 : les sépales protègent le bouton avant qu'il s'ouvre ; le stigmate, en haut du pistil, est collant et retient le pollen.

</details>

<details><summary><b>1-3 Le carnet d'observation</b> (vraifaux)</summary>

La fleur sert à la reproduction de la plante. Le pollen est fabriqué par les étamines, pas par les pétales. Les ovules sont dans le pistil. En CM2 : beaucoup de fleurs ont à la fois des étamines et un pistil, mais le noisetier a des fleurs mâles et des fleurs femelles séparées ; pour observer une fleur, on la dissèque de l'extérieur vers le centre.

</details>

<details><summary><b>1-4 L'étiquette égarée</b> (intrus, CM2)</summary>

Le pistil, l'ovaire, les ovules et le stigmate appartiennent à l'organe femelle de la fleur. L'étamine est un organe mâle : elle fabrique le pollen.

</details>


### Salle 2 — Le rucher — Pollinisation et fécondation (mot : **POLLEN**)

<details><summary><b>2-1 Le voyage du pollen</b> (ordre)</summary>

Une abeille vient boire le nectar d'une fleur et se couvre de pollen ; elle vole vers une autre fleur de la même espèce ; le pollen se dépose sur le pistil ; l'ovaire grossit et devient un fruit qui contient des graines. En CM2 : le pollen déposé sur le stigmate permet de féconder les ovules ; après la fécondation, les pétales fanent, l'ovaire devient le fruit et les ovules deviennent les graines.

</details>

<details><summary><b>2-2 Le cahier du rucher</b> (trous)</summary>

La pollinisation est le transport du pollen des étamines jusqu'au pistil. Les abeilles viennent boire le nectar et transportent le pollen. Après la fécondation, l'ovaire devient le fruit et les ovules deviennent les graines.

</details>

<details><summary><b>2-3 Les ruches et le vent</b> (tri)</summary>

Le pommier, le cerisier et le tournesol ont de grandes fleurs colorées et du nectar : les insectes les pollinisent. Le maïs, le noisetier et les graminées des prairies ont des fleurs discrètes et beaucoup de pollen : le vent les pollinise. En CM2 : le fraisier et la courgette sont pollinisés par les insectes ; le bouleau, par le vent.

</details>

<details><summary><b>2-4 Le panneau des pollinisateurs</b> (qcm, CM2)</summary>

La pollinisation est une coopération : l'insecte se nourrit de nectar et de pollen, et la plante est fécondée. Après la fécondation, l'ovaire devient le fruit. Quand on utilise beaucoup d'insecticides, les pollinisateurs deviennent moins nombreux et certaines cultures donnent moins de fruits et de graines.

</details>


### Salle 3 — Le potager de l'école — Graines et germination (mot : **GRAINES**)

<details><summary><b>3-1 Les graines voyageuses</b> (tri)</summary>

Les graines du pissenlit (aigrettes) et de l'érable (ailes) sont emportées par le vent. Les fruits de la bardane s'accrochent aux poils des animaux ; les glands sont cachés par le geai et parfois oubliés. La noix de coco flotte sur l'eau. En CM2 : le tilleul a des fruits munis d'une aile (vent) ; les oiseaux mangent les cerises et rejettent le noyau plus loin (animaux) ; les graines de l'aulne flottent sur l'eau.

</details>

<details><summary><b>3-2 L'expérience des quatre pots</b> (qcm)</summary>

Seuls les pots B et D ont germé : ils avaient de l'eau et une température douce. Le pot A (sans eau) et le pot C (trop froid) n'ont pas germé. Le pot D, dans le noir, a germé : la plupart des graines n'ont pas besoin de lumière pour germer. En CM2 : une bonne expérience ne change qu'une seule chose à la fois ; après la germination, la jeune plante aura besoin de lumière pour grandir.

</details>

<details><summary><b>3-3 Le cycle du haricot</b> (ordre)</summary>

La graine germe, la jeune plante grandit, elle fleurit, la fleur devient un fruit qui contient des graines. En CM2 : entre la floraison et le fruit, il faut la pollinisation et la fécondation ; à la fin, les graines sont dispersées et le cycle recommence.

</details>

<details><summary><b>3-4 La graine ouverte</b> (association, CM2)</summary>

L'enveloppe protège la graine ; l'embryon est la future plante ; les réserves nourrissent la jeune plante au début ; l'eau réveille la graine ; la lumière servira ensuite à la jeune plante pour grandir.

</details>


### Salle 4 — La ferme des Coteaux — La fécondation chez les animaux (mot : **FÉCONDATION**)

<details><summary><b>4-1 Les questions de la ferme</b> (qcm)</summary>

Chez les animaux, pour avoir des petits, il faut en général un mâle et une femelle de la même espèce. La fécondation est la rencontre d'une cellule reproductrice mâle et d'une cellule reproductrice femelle. En CM2 : ces cellules s'appellent les gamètes ; chez les oiseaux et les mammifères, la fécondation est interne ; chez la grenouille, elle est externe, dans l'eau.

</details>

<details><summary><b>4-2 Le registre de la ferme</b> (tri)</summary>

La poule, la vache et le lapin ont une fécondation interne, dans le corps de la femelle. La grenouille et la truite ont une fécondation externe, dans l'eau. En CM2 : la tortue et la cane, qui pondent pourtant des œufs, ont une fécondation interne ; le crapaud et le saumon ont une fécondation externe.

</details>

<details><summary><b>4-3 L'intrus de l'enclos</b> (intrus)</summary>

La poule, la chèvre, le cheval et la lapine ont une fécondation interne. La grenouille a une fécondation externe : ses ovules sont fécondés dans l'eau. En CM2 : la phrase « Les ovules sont pondus dans l'eau avant d'être fécondés » décrit une fécondation externe.

</details>

<details><summary><b>4-4 Les panneaux de l'étang</b> (vraifaux, CM2)</summary>

La fécondation externe se fait dans l'eau, car les cellules reproductrices ne survivraient pas à l'air libre. Les animaux à fécondation externe pondent souvent un très grand nombre d'œufs. Un mâle et une femelle d'espèces différentes, comme un coq et une cane, n'ont pas de petits ensemble.

</details>


### Salle 5 — La bergerie et la mare — Naître ou éclore (mot : **ESPÈCE**)

<details><summary><b>5-1 Les nids et la bergerie</b> (tri)</summary>

La poule, la tortue et la grenouille pondent des œufs : elles sont ovipares. La vache, la brebis et la lapine portent leur petit dans leur ventre : elles sont vivipares. En CM2 : la truite et le papillon sont ovipares ; le dauphin et la chauve-souris sont des mammifères vivipares, même si l'un vit dans l'eau et l'autre vole.

</details>

<details><summary><b>5-2 Le carnet de la vétérinaire</b> (vraifaux)</summary>

Un petit appartient toujours à la même espèce que ses parents. Les petits ressemblent à leurs parents sans être identiques. L'œuf de poule contient un embryon et des réserves. En CM2 : une fécondation externe va toujours avec la ponte d'œufs ; une fécondation interne peut aller avec la ponte (poule) ou avec la naissance (vache) ; une espèce est un ensemble d'êtres vivants qui peuvent se reproduire entre eux.

</details>

<details><summary><b>5-3 De l'œuf au petit</b> (ordre)</summary>

Chez la poule : la fécondation a lieu dans le corps de la poule, elle pond l'œuf, elle le couve pendant que l'embryon se développe (environ 21 jours), le poussin sort de l'œuf (éclosion), puis il grandit. En CM2, chez la grenouille : les ovules sont pondus dans l'eau et fécondés par le mâle, l'embryon se développe dans l'œuf, une larve, le têtard, sort de l'œuf, des pattes lui poussent, puis il devient une jeune grenouille qui quitte l'eau.

</details>

<details><summary><b>5-4 Le portail du jardin</b> (code, CM2)</summary>

L'œuf de poule éclot après environ 21 jours de couvaison ; le veau naît après environ 9 mois ; l'agneau après environ 5 mois. Le code est 21, 9, 5.

</details>


## Sources

- Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2) : « Les êtres vivants dans leur environnement », CM1 « Reproduction, croissance et développement » et « Unité et diversité du vivant », 6e « Reproduction, croissance et développement » (progression de l'enseignant : année A, période 5)
- Programme du cycle 2, CE2, « Reproduction, croissance et développement » (BO n° 24 du 11 juin 2026, annexe 1) : étapes de la vie d'une plante à fleurs
- La main à la pâte, séquence « Le cycle de vie des végétaux » (cycle 3)
- La main à la pâte, « De quoi a besoin une graine pour germer ? »
- Encyclopædia Universalis, « Fleur : les fleurs, organes reproducteurs »
- Muséum national d'histoire naturelle (MNHN) et Office français de la biodiversité (OFB), Spipoll et pages « Les pollinisateurs »
- FAO, « Incubation naturelle » (élevage des poules)
- Lumni, vidéos « La reproduction des animaux » (ovipares et vivipares). Détail : README.md, section Sources.

## Fichiers

- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; schémas SVG dans `tests/donnees/schemas.py`.
- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py reproduction --theme reproduction/tests/donnees/theme-immersif.json --force`, puis `appliquer-narration.py reproduction`, `finir-jeu.py reproduction` et `python reproduction/tests/donnees/gen_medias.py` (prompts des médias), enfin `prompts-flow.py reproduction`.
- Grades : `vingt-mille-lieues/outils/immersif/grades/reproduction_s1..s5.py` et `reproduction_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/reproduction.json`.
