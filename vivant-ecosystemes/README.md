# L'Expédition biodiversité — escape game de sciences (cycle 3, jeu n°17)

Sciences et technologie, programme 2026 (BO n° 24 du 11 juin 2026, annexe 2), parties « Unité et diversité du vivant » et « Les écosystèmes » ; progression de l'enseignant : année A, période 4 :
*Le vivant, sa diversité et les fonctions qui le caractérisent. Panorama du vivant : organisation des êtres vivants et biodiversité actuelle et passée. La planète Terre. Écosystème : structure, fonctionnement et dynamique.*

**Jouer** : version immersive `../immersifs/vivant-ecosystemes/` (5 grades : Promeneur ≈ CE2, Jeune naturaliste ≈ CM1, Naturaliste ≈ CM2, Écologue ≈ 6ᵉ, Conservateur de la réserve ≈ 5ᵉ).
Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas écrite.

**Vigilance** : vocabulaire du programme (« milieu de vie », « êtres vivants » ; ni biotope ni biocénose) ; pas de groupe « invertébrés » (on ne classe pas sur une absence) ; ton non alarmiste ; réserve et personnages inventés.

## Fil narratif

Le ruisseau a débordé sur le campement de l'expédition, dans la réserve naturelle (inventée) du Val-des-Saules, en Bourgogne : toutes les fiches sont mélangées. Les élèves, jeunes naturalistes, aident cinq experts et rassemblent cinq mots qui ouvrent la boîte de la carte du vivant :
> Chaque ESPÈCE se range dans des GROUPES emboîtés ; les FOSSILES racontent le vivant d'autrefois ; chaque MILIEU abrite des êtres vivants liés en RÉSEAU.

| Étape | Lieu | Guide (personnage inventé) | Mot |
|---|---|---|---|
| 1 | La tente-laboratoire de l'expédition, au bord du ruisseau | Lina, biologiste de terrain, cheffe de l'expédition | ESPÈCE |
| 2 | La cabane du garde, à l'entrée de la forêt | Hugo, garde de la réserve naturelle | GROUPES |
| 3 | L'ancienne carrière de calcaire de la réserve | Amara, paléontologue | FOSSILES |
| 4 | La mare de la réserve et le pré fleuri où sont les ruches | Rose, apicultrice du pré de la réserve | MILIEU |
| 5 | Le ponton du grand étang de la réserve | Élio, pêcheur de l'étang | RÉSEAU |

## 🎯 Compétences du programme (vue d'ensemble)

| Étape | Compétence du programme |
|---|---|
| 1 | Définir l'espèce comme un ensemble d'individus interféconds ; décrire un être vivant par ses attributs (CM1) ; la cellule, unité du vivant (prolongement 6e) |
| 2 | Réaliser une classification en groupes emboîtés à partir d'attributs ; en déduire des liens de parenté ; identifier des espèces proches avec une clé de détermination (CM1) |
| 3 | Distinguer les échelles du temps géologique et de l'histoire humaine ; caractériser l'évolution de la biodiversité grâce aux fossiles ; extinction massive de la fin du Crétacé et remplacement rapide d'espèces (CM2) |
| 4 | Définir un écosystème : êtres vivants, milieu de vie et relations ; caractéristiques physiques du milieu ; relier la présence d'êtres vivants au milieu ; prédation et coopération (CM1) |
| 5 | Représenter les liens alimentaires par un réseau (flèche de la proie vers le prédateur) ; effet d'une forte variation d'une espèce (surpêche, espèce invasive) ; conséquences d'une action humaine (CM1 ; EDD en CM2) |

CM1 : 3 énigmes par étape (15) ; CM2 : 4 énigmes par étape (20). Repères en CM1 (ordre des grandes étapes, mots simples) ; dates et calculs en millions d'années en CM2 (4,6 milliards, 540, 252, 66 millions d'années, 300 000 ans).

## Solutions (générées depuis `assets/data/enigmes.json`)

### Étape 1 — La tente-laboratoire — Observer le vivant, l'espèce (mot : **ESPÈCE**)

<details><summary><b>1-1 La mésange du carnet</b> (plan)</summary>

Sur le dessin, le repère 1 montre le bec, le repère 2 l'œil et le repère 3 les plumes de l'aile. En CM2, le repère 4 montre la patte et le repère 5 la queue ; les poils et la coquille ne sont pas des attributs de la mésange.

</details>

<details><summary><b>1-2 Les notes mouillées</b> (vraifaux)</summary>

Une espèce réunit des êtres vivants qui se ressemblent et peuvent avoir ensemble des petits, qui auront à leur tour des petits. Un caniche et un berger allemand sont de la même espèce, le chien. En CM2 : le mulet ne peut pas avoir de petits, donc l'âne et le cheval sont deux espèces ; un attribut se voit sur l'être vivant ; ce qu'il mange n'en est pas un.

</details>

<details><summary><b>1-3 Les boîtes d'observation</b> (association)</summary>

L'escargot a une coquille enroulée, la libellule six pattes et quatre ailes, le renard des poils. En CM2 : le héron a des plumes et un long bec, la grenouille une peau nue et quatre membres, l'araignée huit pattes, et la fougère des feuilles mais pas de fleurs.

</details>

<details><summary><b>1-4 Même espèce ?</b> (tri, CM2)</summary>

Le caniche et le berger allemand, le chat roux et le chat noir, le coq et la poule sont de la même espèce : leurs petits peuvent avoir des petits. L'âne et le cheval donnent des mulets qui n'ont pas de petits ; le chat et le tigre, la mésange et le moineau ne se reproduisent pas ensemble : ce sont des espèces différentes.

</details>


### Étape 2 — La cabane du garde — Classer le vivant (mot : **GROUPES**)

<details><summary><b>2-1 Les caisses du garde</b> (tri)</summary>

Le renard et le hérisson ont des poils ; le héron et le canard ont des plumes ; la libellule et la fourmi ont six pattes. En CM2 : la chauve-souris a des poils (elle vole, mais ce n'est pas un oiseau) ; la grenouille et le lézard ont quatre membres sans poils ni plumes ; la truite a un squelette interne et des nageoires.

</details>

<details><summary><b>2-2 Les règles du classement</b> (qcm)</summary>

On classe les êtres vivants selon les attributs qu'ils possèdent en commun, pas selon l'endroit où ils vivent ni ce qu'ils mangent. La chauve-souris a des poils : elle est rangée avec le renard. En CM2 : on ne fait jamais de groupe avec une absence ; les groupes sont emboîtés ; le dauphin est rangé avec les animaux qui allaitent leurs petits.

</details>

<details><summary><b>2-3 La clé des petites bêtes</b> (plan)</summary>

La clé se lit de haut en bas : l'escargot n'a pas de pattes (case 1) ; la fourmi, un insecte, a six pattes (case 2) ; l'araignée en a huit (case 3). En CM2 : le cloporte a quatorze pattes (case 4) et le mille-pattes plus de trente (case 5). La libellule et le scarabée sont des insectes : ils iraient dans la case des six pattes, déjà occupée par la fourmi.

</details>

<details><summary><b>2-4 La caisse des poils</b> (intrus, CM2)</summary>

Le renard, le hérisson, la chauve-souris et le ragondin ont des poils. Le lézard a des écailles, sans poils : il n'a rien à faire dans cette caisse, même s'il a quatre membres comme eux.

</details>


### Étape 3 — L'ancienne carrière — La biodiversité passée (mot : **FOSSILES**)

<details><summary><b>3-1 La frise de la carrière</b> (ordre)</summary>

D'abord la formation de la Terre, puis les premières traces de vie, puis les trilobites dans la mer, puis la disparition des dinosaures, et enfin l'apparition de notre espèce. En CM2 : il y a environ 4,6 milliards d'années, 3,8 milliards d'années, 540 millions d'années, 66 millions d'années et 300 000 ans.

</details>

<details><summary><b>3-2 Le tiroir des fossiles</b> (association)</summary>

Une ammonite était un animal marin à coquille enroulée, un trilobite un animal marin à carapace, une empreinte de fougère la trace d'une plante. En CM2 : une dent de requin trouvée dans un champ montre qu'une mer recouvrait autrefois ce lieu ; un os de dinosaure, que de grands reptiles vivaient sur la terre ferme ; les ammonites ont disparu il y a 66 millions d'années, les trilobites il y a 252 millions d'années.

</details>

<details><summary><b>3-3 Le panneau de la crise</b> (vraifaux)</summary>

Les dinosaures ont disparu il y a très longtemps, bien avant l'apparition des humains : aucun humain n'en a vu vivant. Un fossile est un reste ou une trace d'être vivant conservé dans une roche. En CM2 : il y a environ 66 millions d'années, une extinction massive a fait disparaître un très grand nombre d'espèces ; les causes étudiées sont une météorite géante au Mexique et d'énormes éruptions en Inde ; les oiseaux descendent de petits dinosaures à plumes ; ensuite, les mammifères se sont diversifiés.

</details>

<details><summary><b>3-4 Le cadenas des millions</b> (code, CM2)</summary>

Les trilobites ont disparu 252 − 66 = 186 millions d'années avant les ammonites. Les ammonites ont disparu il y a environ 66 millions d'années : c'est le second nombre.

</details>


### Étape 4 — La mare et le pré fleuri — L'écosystème (mot : **MILIEU**)

<details><summary><b>4-1 La coupe de la mare</b> (plan)</summary>

Le repère 1 montre la lumière du soleil, le repère 2 l'eau de la mare, le repère 3 un roseau. En CM2, le repère 4 montre une grenouille et le repère 5 la vase du fond. La lumière, l'eau et la vase font partie du milieu de vie ; le roseau et la grenouille sont des êtres vivants.

</details>

<details><summary><b>4-2 Les relevés de Rose</b> (tri)</summary>

La lumière, la température de l'eau et la pluie décrivent le milieu de vie ; le nénuphar, la libellule et le champignon sont des êtres vivants. En CM2 : l'humidité de l'air et la profondeur de l'eau décrivent aussi le milieu ; la mousse et la paramécie, minuscule, sont des êtres vivants.

</details>

<details><summary><b>4-3 Les questions de l'apicultrice</b> (qcm)</summary>

Le héron qui attrape une grenouille est un prédateur et la grenouille sa proie : c'est la prédation. L'abeille boit le nectar et transporte le pollen d'une fleur à l'autre : chacun gagne, c'est une coopération. En CM2 : un écosystème réunit un milieu de vie, des êtres vivants et leurs relations ; la grenouille a besoin de l'eau de la mare pour pondre ; les nénuphars ont besoin d'une eau calme et ensoleillée.

</details>

<details><summary><b>4-4 Qui vit où ?</b> (association, CM2)</summary>

Le nénuphar a besoin d'une eau calme et ensoleillée ; la mousse d'un endroit humide et ombragé ; la grenouille d'eau pour pondre ; l'abeille de fleurs pour son nectar ; le héron d'une eau peu profonde où il pêche à pied.

</details>


### Étape 5 — Le ponton de l'étang — Le réseau alimentaire (mot : **RÉSEAU**)

<details><summary><b>5-1 Qui mange qui ?</b> (ordre)</summary>

Les algues sont mangées par les têtards, les têtards par les larves de libellule, puis par les perches. En CM2 : la chaîne continue jusqu'au héron cendré, qui mange les perches. Chaque chaîne commence par une plante ou une algue.

</details>

<details><summary><b>5-2 Les flèches d'Élio</b> (vraifaux)</summary>

La flèche va de celui qui est mangé vers celui qui le mange : algues → têtard veut dire « les algues sont mangées par le têtard ». Les animaux mangent d'autres êtres vivants pour grandir. En CM2 : les chaînes se croisent et forment un réseau ; si une espèce change beaucoup en nombre, tout le réseau est touché ; au départ de chaque chaîne il y a une plante ou une algue.

</details>

<details><summary><b>5-3 L'intruse venue d'Amérique</b> (trous)</summary>

L'écrevisse de Louisiane vient d'Amérique ; relâchée dans la nature, elle détruit les plantes de l'eau et mange les petits animaux de la mare. Il ne faut jamais relâcher un animal exotique dans la nature. En CM2 : elle a été introduite en France en 1976 ; le frelon asiatique, observé en France depuis 2004, chasse surtout les abeilles ; on peut aider la mare en ne relâchant aucun animal et en gardant des haies.

</details>

<details><summary><b>5-4 Le maillon manquant</b> (code, CM2)</summary>

Le maillon 1 mange les algues et est mangé par la larve de libellule : c'est le têtard (n° 4). Le maillon 2 mange les têtards et les larves de libellule : c'est la perche (n° 3). Le maillon 3 mange les perches et les grenouilles : c'est le héron cendré (n° 2). Le code est 4, 3, 2.

</details>


## Sources

- Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2) : « Unité et diversité du vivant » et « Les écosystèmes » (progression de l'enseignant : année A, période 4)
- Muséum national d'histoire naturelle et INPN (inpn.mnhn.fr)
- Fondation La main à la pâte, « Classification du vivant » et « Écosystèmes »
- Académie de Martinique, « Marche des temps géologiques », dossier pédagogique (2024)
- Espace des sciences, Sciences Ouest n° 413, « Disparition des dinosaures : que s'est-il passé ? »
- Centre de ressources Espèces exotiques envahissantes (OFB, UICN France), fiche « Écrevisse de Louisiane »
- MNHN, Villemant et al. (2011), « Bilan de l'invasion de Vespa velutina en France »
- Office français de la biodiversité (OFB). Détail : README.md, section Sources.

## Fichiers

- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; schémas SVG dans `tests/donnees/schemas.py`.
- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py vivant-ecosystemes --theme vivant-ecosystemes/tests/donnees/theme-immersif.json --force`, puis `appliquer-narration.py vivant-ecosystemes` et `finir-jeu.py vivant-ecosystemes` ; enfin remplacer « la étape » par « l'étape » dans `immersifs/vivant-ecosystemes/assets/data/*.json` (le migrateur écrit « la » devant le mot du thème) et relancer `outils/embarquer-donnees.py`.
- Grades : `vingt-mille-lieues/outils/immersif/grades/vivant_ecosystemes_s1..s5.py` et `vivant_ecosystemes_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/vivant-ecosystemes.json`.
