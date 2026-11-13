# La Centrale en panne — escape game de sciences (cycle 3, jeu n°14)

Sciences et technologie, programme 2026 (BO n° 24 du 11 juin 2026), CM2, partie « Signaux » : électricité ; progression de l'enseignant : année A, période 3 :
*Matière, mouvement, énergie et information. L'électricité.*

**Jouer** : version immersive `../immersifs/electricite/` (5 grades : Stagiaire ≈ CE2, Électricien ≈ CM1, Technicien ≈ CM2, Ingénieur ≈ 6ᵉ, Chef de quart ≈ 5ᵉ).
Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas encore écrite.

**Sécurité** : aucune expérience ni manipulation avec le secteur ; seules les piles de la classe sont utilisées.

## Fil narratif

Un orage a plongé dans le noir la petite ville de Clairval (inventée). Les élèves, apprentis électriciens de la centrale, réparent salle après salle et retrouvent cinq mots qui ferment le dernier circuit :

> Une BOUCLE sans trou, un CONDUCTEUR pour la fermer, un SCHÉMA pour la dessiner, la SÉCURITÉ toujours, et la CENTRALE rallume la ville.

| Salle | Lieu | Guide (personnage inventé) | Mot |
|---|---|---|---|
| 1 | L'atelier du club sciences, au rez-de-chaussée de la centrale | Nour, élève du club sciences de la centrale | BOUCLE |
| 2 | Le magasin de matériel électrique | Maëlle, magasinière du matériel électrique | CONDUCTEUR |
| 3 | La salle de contrôle de la centrale | Hélène, ingénieure de la centrale | SCHÉMA |
| 4 | La maison témoin, dans le hall des visites | Marius, électricien de la ville | SÉCURITÉ |
| 5 | Le poste de conduite du réseau | Karim, technicien du réseau | CENTRALE |

## 🎯 Compétences du programme (vue d'ensemble)

| Salle | Compétence du programme |
|---|---|
| 1 | Réaliser un circuit électrique à une boucle (pile, interrupteur, un ou deux récepteurs) ; circuit ouvert, circuit fermé |
| 2 | Identifier des matériaux conducteurs et isolants ; un même objet peut être fabriqué dans l'un ou l'autre type de matériau |
| 3 | Réaliser et schématiser un circuit, lire et utiliser des schémas normalisés ; justifier par une boucle ininterrompue de récepteurs et de conducteurs |
| 4 | Chercher des informations sur les règles de sécurité électrique et les appliquer ; économiser l'électricité |
| 5 | Produire et transporter l'électricité : centrales, sources renouvelables ou non, de la centrale à la prise (chiffres RTE 2025) |

CM1 : 3 énigmes par salle (15) ; CM2 : 4 énigmes par salle (20). La notion est au programme de CM2 ; en CM1 (et au grade Stagiaire), le jeu reste sur le circuit à une boucle, les matériaux et la sécurité.

## Solutions (générées depuis `assets/data/enigmes.json`)

### Salle 1 — L'atelier du club sciences — Le circuit électrique (mot : **BOUCLE**)

- **1-1 Le montage de Nour** (plan) : Sur ce dessin, la pile plate est le repère 1, la lampe sur sa douille le repère 2 et l'interrupteur le repère 3. En CM2, le repère 4 est un fil de connexion et le repère 5 une borne de la pile, la lame métallique où l'on branche le fil.
- **1-2 Ouvert ou fermé ?** (vraifaux) : La lampe ne brille que si le courant fait une boucle complète, d'une borne de la pile à l'autre : le circuit est alors fermé. Si l'interrupteur est ouvert, la boucle est coupée et la lampe reste éteinte. En CM2 : un seul fil suffit à couper la boucle s'il est débranché ; le courant ne s'use pas dans la lampe, c'est la pile qui s'use ; deux lampes dans la même boucle s'éteignent ensemble si l'une est dévissée.
- **1-3 Quelle lampe s'allume ?** (qcm) : Seul le montage où les deux bornes de la pile sont reliées à la lampe, avec l'interrupteur fermé, forme une boucle complète : la lampe brille. Un fil qui ne touche qu'une borne, ou un interrupteur ouvert, coupe la boucle. En CM2 : relier directement les deux bornes de la pile par un fil, sans lampe, est un court-circuit : le fil chauffe et la pile s'use très vite.
- **1-4 Le pas-à-pas de Nour** (ordre, CM2) : On vérifie d'abord que l'interrupteur est ouvert, puis on relie la borne + de la pile à l'interrupteur, l'interrupteur à la lampe, et la lampe à la borne − : la boucle est complète. On ferme enfin l'interrupteur pour allumer la lampe, et on l'ouvre pour l'éteindre.

### Salle 2 — Le magasin de matériel — Conducteurs et isolants (mot : **CONDUCTEUR**)

- **2-1 Le bac renversé** (tri) : Les objets en métal (clé en fer, trombone, papier d'aluminium, pièce de monnaie) sont conducteurs. Les objets en plastique, en bois, en verre, en caoutchouc ou en papier sont isolants. En CM2, la mine du crayon à papier, en graphite, est conductrice alors que ce n'est pas un métal.
- **2-2 L'intrus de la boîte** (intrus) : La cuillère en bois est l'intrus en CM1 : le bois est isolant, alors que la fourchette, le clou et la canette sont en métal. En CM2, l'intrus est le gant en caoutchouc : il est isolant, c'est même pour cela que les électriciens en portent ; la mine de crayon en graphite, elle, est conductrice.
- **2-3 Les étiquettes des bobines** (association) : Le cœur en cuivre du fil conduit le courant ; la gaine en plastique isole et protège les doigts ; le circuit testeur dit si un objet est conducteur. En CM2 : les poignées des outils et les prises sont en plastique pour protéger les personnes ; l'air sec, entre les lames d'un interrupteur ouvert, coupe la boucle ; le corps humain conduit le courant, d'où le danger du secteur.
- **2-4 La notice du testeur** (trous, CM2) : On place l'objet dans la boucle du circuit testeur. Si la lampe s'allume, l'objet est conducteur ; si elle reste éteinte, il est isolant. Les métaux, comme le cuivre, sont conducteurs ; le plastique est isolant.

### Salle 3 — La salle de contrôle — Le schéma électrique (mot : **SCHÉMA**)

- **3-1 La légende des symboles** (association) : Un grand trait et un petit trait parallèles représentent la pile ; un cercle barré d'une croix, la lampe ; un cercle avec un M, le moteur. En CM2 : le trait levé est un interrupteur ouvert, le trait couché qui ferme le passage un interrupteur fermé, et le trait droit un fil de connexion.
- **3-2 Le schéma du pupitre** (plan) : Le repère 1, à gauche, est la pile : un grand trait et un petit trait. Le repère 2, en haut, est l'interrupteur, ici ouvert. Le repère 3, à droite, est la lampe. En CM2, le repère 4 est le moteur, le cercle avec un M, et le repère 5 un fil de connexion.
- **3-3 Ce que dit le schéma** (vraifaux) : Sur ce schéma, l'interrupteur est ouvert : la boucle est coupée, la lampe est éteinte et le moteur à l'arrêt. Un schéma utilise des symboles, pas des dessins ressemblants. En CM2 : la lampe, le moteur et l'interrupteur sont dans une seule boucle, donc l'interrupteur commande les deux ; et le grand trait de la pile est la borne +.
- **3-4 Suivre le courant** (ordre, CM2) : En partant du grand trait de la pile, la borne +, le courant traverse d'abord l'interrupteur, en haut, puis la lampe, à droite, puis le moteur, en bas, avant de revenir à la borne −, le petit trait.

### Salle 4 — La maison témoin — La sécurité électrique (mot : **SÉCURITÉ**)

- **4-1 Le quiz de Marius** (qcm) : La pile plate de la classe, de 4,5 volts, est sans danger ; le courant des prises, de 230 volts, est dangereux et peut tuer. On ne met jamais d'objet dans une prise. En CM2 : en cas d'accident, on ne touche pas la personne, on coupe le courant au disjoncteur, puis on appelle le 18 ou le 112 ; on débranche en tirant sur la fiche, pas sur le fil.
- **4-2 Les affiches tombées** (tri) : Une pile plate, une lampe de poche ou un jouet à piles sont sans danger. Mettre un objet dans une prise, toucher un sèche-cheveux branché avec les mains mouillées ou jouer près d'un pylône sont dangereux. En CM2 : faire voler un cerf-volant près des lignes, entrer dans un poste électrique, utiliser un fil abîmé sont dangereux ; débrancher par la fiche, éteindre la lumière en partant et laisser un adulte changer une ampoule appareil débranché sont de bons réflexes.
- **4-3 Les idées reçues** (vraifaux) : On peut faire des expériences avec une pile plate, mais jamais avec le secteur. L'eau et l'électricité du secteur ensemble sont très dangereuses. Éteindre la lumière en quittant une pièce économise l'électricité. En CM2 : une lampe à LED consomme beaucoup moins qu'une lampe à incandescence ; un appareil en veille consomme encore ; une ligne électrique peut être dangereuse même sans la toucher.
- **4-4 Les bons réflexes** (association, CM2) : Dans la salle de bain, on n'utilise pas d'appareil électrique près de l'eau. Pour débrancher, on tire sur la fiche. Face à une personne électrisée, on coupe le courant avant de la toucher. Un ballon dans un poste électrique : on appelle un adulte, qui préviendra le gestionnaire du réseau. En quittant la pièce, on éteint la lumière.

### Salle 5 — Le poste de conduite du réseau — Produire et transporter l'électricité (mot : **CENTRALE**)

- **5-1 De la centrale à la prise** (ordre) : L'électricité part de la centrale, voyage sur les lignes à très haute tension portées par des pylônes, arrive dans un poste près de la ville, puis passe par les câbles du quartier jusqu'à la maison. En CM2 : un transformateur élève la tension à la sortie de la centrale ; le poste l'abaisse ; le réseau de distribution va jusqu'au compteur, puis aux prises.
- **5-2 Les centrales de la vallée** (tri) : Les centrales hydrauliques (l'eau d'un barrage), les éoliennes (le vent) et les panneaux solaires (la lumière du Soleil) utilisent des sources renouvelables. Les centrales nucléaires (l'uranium) et les centrales thermiques (gaz, charbon, fioul) utilisent des sources qui ne se renouvellent pas.
- **5-3 Le pupitre de reconnexion** (code) : Le quartier de la gare se rallume avec 373, la production nucléaire ; le quartier du port avec 62, l'hydraulique ; le quartier des écoles avec 50, l'éolien ; le quartier du marché avec 33, le solaire. En CM2, il fallait arrondir 62,4 à 62, 49,6 à 50 et 32,9 à 33, et calculer la part du nucléaire : 373 sur 547,5, soit environ 68 %.
- **5-4 Le carnet de Karim** (trous, CM2) : Dans la plupart des centrales, une turbine reliée à un alternateur tourne pour produire le courant : la vapeur dans une centrale nucléaire, l'eau d'un barrage dans une centrale hydraulique, le vent dans une éolienne. Les panneaux solaires, eux, transforment directement la lumière. L'électricité se stocke très mal : il faut produire à chaque instant autant que l'on consomme.

## Sources

- Programme de sciences et technologie, cycle 3 (arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), CM2, « Signaux » : électricité
- Fondation La main à la pâte, « L'électricité au cycle 3 »
- Eduscol, ressources d'accompagnement du programme de sciences et technologie au cycle 3
- Enedis, conseils de prévention des accidents électriques
- RTE, Bilan électrique 2025 (d'après Connaissance des énergies)
- Connaissance des énergies, fiche pédagogique « RTE » (réseau de transport)
- Lumni, vidéos « L'électricité » (cycle 3). Détail : README.md, section Sources.

## Fichiers

- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; montages et schémas SVG par `tests/donnees/schemas.py`.
- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py electricite --theme electricite/tests/donnees/theme-immersif.json --force`, puis `appliquer-grades.py electricite`, `appliquer-narration.py electricite`, `immersifs/electricite/outils/embarquer-donnees.py`.
- Grades : `vingt-mille-lieues/outils/immersif/grades/electricite_s1..s5.py` et `electricite_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/electricite.json`.
