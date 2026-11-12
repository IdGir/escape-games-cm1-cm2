# La Caravelle du capitaine — escape game d'histoire (cycle 3, jeu n°13)

Thème 3 « Explorations et conquêtes » (programme 2026, BO n° 22 du 28 mai 2026) ; progression de l'enseignant : année B, période 3 :
*les progrès techniques qui ont permis aux Européens de s'aventurer vers de nouveaux territoires ; la constitution des premiers empires coloniaux en Amérique.*

**Jouer** : version immersive `../immersifs/grandes-explorations/` (5 grades : Mousse ≈ CE2, Matelot ≈ CM1, Timonier ≈ CM2, Pilote ≈ 6ᵉ, Cartographe ≈ 5ᵉ).
Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas encore écrite.

## Fil narratif

Festival de la mer à Saint-Malo, à bord de la *Rose des vents*, copie d'une caravelle. Une tempête a dispersé les pages du journal de bord que l'équipage lit aux visiteurs.
Les élèves, nouveaux mousses, parcourent cinq lieux et retrouvent cinq mots qui ouvrent le coffre de bord :

> Pour les ÉPICES, guidés par l'ASTROLABE, les Européens traversent l'OCÉAN ; la RENCONTRE devient conquête et fonde des EMPIRES.

| Salle | Lieu | Guide (personnage inventé) | Mot |
|---|---|---|---|
| 1 | La cale de la Rose des vents | Amaury, guide du festival, spécialiste du commerce des épices | ÉPICES |
| 2 | Le pont de la Rose des vents | Rosa, cartographe, restauratrice de cartes anciennes | ASTROLABE |
| 3 | La chambre des cartes, sous le château arrière | Bastien, capitaine de la caravelle | OCÉAN |
| 4 | La tente des conteurs, sur le quai | Itzel, conteuse venue de mexico | RENCONTRE |
| 5 | Le cabinet du cartographe, au fond du navire | Simon, mousse de la caravelle | EMPIRES |

## 🎯 Compétences du programme (vue d'ensemble)

| Salle | Compétence du programme |
|---|---|
| 1 | Les raisons des explorations : épices, routes commerciales, or, religion, gloire, savoir (le monde connu vers 1450) |
| 2 | Les progrès techniques qui ont permis aux Européens de s'aventurer vers de nouveaux territoires (caravelle, boussole, astrolabe, cartes) |
| 3 | Les grands voyages d'exploration (Colomb 1492, Vasco de Gama 1498, Magellan et Elcano 1519-1522, Cartier 1534) : situer, dater, cartographier |
| 4 | La rencontre avec les peuples d'Amérique et la conquête (Aztèques, Incas, Iroquoiens ; conquistadors ; maladies ; échanges) |
| 5 | La constitution des premiers empires coloniaux en Amérique (Tordesillas 1494 ; Espagne, Portugal, France, Angleterre ; exploitation) |

CM1 : 3 énigmes par salle (15) ; CM2 : 4 énigmes par salle (20). Repères en CM1, dates exactes en CM2.

## Solutions (générées depuis `assets/data/enigmes.json`)

### Salle 1 — La cale aux épices — Pourquoi partir ? (mot : **ÉPICES**)

- **1-1 La carte du monde connu** (plan) : Sur cette carte, l'Europe est le repère 1, l'Afrique le repère 2 et l'Asie le repère 3. Les terres en pointillés, à gauche, sont celles que les Européens ne connaissaient pas encore : les Amériques. En CM2, le repère 4 est la mer Méditerranée et le repère 5 la route des épices, qui traverse l'Asie par la terre.
- **1-2 Les sacs de la cale** (association) : Les épices, comme le poivre, parfument et conservent les aliments. L'or sert à fabriquer des pièces de monnaie. La soie est un tissu précieux venu de Chine. En CM2 : les marchands espèrent acheter les épices moins cher, les rois veulent de l'or et de nouvelles terres, l'Église veut répandre la religion chrétienne, les marins veulent la gloire et les savants mieux connaître le monde.
- **1-3 Vrai ou légende ?** (vraifaux) : Le poivre venait bien d'Asie, de très loin, et coûtait très cher. Les savants savaient déjà que la Terre est ronde : la Terre plate est une légende. Les Européens ne connaissaient pas les Amériques. En CM2 : en 1453, les Turcs ottomans prennent Constantinople, et les Portugais longent déjà les côtes d'Afrique au XVe siècle.
- **1-4 Les caisses du négociant** (tri) : Acheter du poivre moins cher et trouver de l'or sont des raisons de richesse. Répandre la religion chrétienne est une raison religieuse. Mieux connaître le monde et dessiner de nouvelles cartes sont des raisons de savoir, comme gagner la gloire auprès du roi pour les marins.

### Salle 2 — Le pont de la caravelle — Les progrès techniques (mot : **ASTROLABE**)

- **2-1 Les instruments de Rosa** (association) : La boussole indique le nord grâce à son aiguille aimantée. L'astrolabe mesure la hauteur du Soleil ou d'une étoile. La carte marine montre les côtes et les ports. En CM2 : le quadrant mesure aussi la hauteur d'un astre, comme l'étoile Polaire, et le sablier mesure le temps passé.
- **2-2 Le plan de la caravelle** (plan) : Le repère 1 est une voile triangulaire, appelée voile latine : elle permet d'avancer même quand le vent n'est pas dans le dos. Le repère 2 est un mât et le repère 3 le gouvernail, à l'arrière. En CM2 : le repère 2 est une voile carrée, le repère 3 le gouvernail d'étambot, le repère 4 le château arrière et le repère 5 la coque.
- **2-3 Les questions de la cartographe** (qcm) : Une caravelle est un navire léger, d'une vingtaine de mètres, avec une vingtaine de marins. Ses voiles latines l'aident à avancer même contre le vent. La boussole a été inventée en Chine. En CM2 : la latitude est la position entre le nord et le sud ; ce sont les Portugais qui ont mis au point la caravelle au XVe siècle.
- **2-4 Faire le point à midi** (ordre) : À midi, quand le Soleil est au plus haut, le pilote vise le Soleil avec l'astrolabe. Il lit l'angle sur le cercle gradué. Il cherche dans ses tables la latitude qui correspond à cet angle et à la date. Il reporte enfin cette latitude sur la carte marine pour savoir où se trouve le navire.

### Salle 3 — La chambre des cartes — Les grands voyages (mot : **OCÉAN**)

- **3-1 La frise des voyages** (ordre) : Le premier voyage est celui de Christophe Colomb, arrivé aux Antilles en 1492. Vasco de Gama arrive en Inde en 1498. L'expédition de Magellan part en 1519 et revient avec Elcano en 1522. Jacques Cartier arrive au Canada en 1534. En CM2, on ajoute le Portugais Cabral, arrivé au Brésil en 1500.
- **3-2 Qui est allé où ?** (association) : Christophe Colomb a traversé l'Atlantique vers l'ouest et atteint les Antilles. Vasco de Gama a fait le tour de l'Afrique pour arriver en Inde. Jacques Cartier a remonté le Saint-Laurent, au Canada. En CM2 : Magellan cherchait un passage vers l'Asie par l'ouest et a été tué aux Philippines, et Elcano a terminé le premier tour du monde.
- **3-3 La carte des routes** (plan) : Le repère 1 est sur la route de Colomb, vers les Antilles. Le repère 2 est sur la route de Vasco de Gama, qui contourne l'Afrique vers l'Inde. Le repère 3 est sur la route de Cartier, au nord, vers le Canada. En CM2, le repère 4 est sur la route de Magellan et Elcano, au sud de l'Amérique, et le repère 5 est le cap de Bonne-Espérance, au sud de l'Afrique.
- **3-4 La page mouillée** (trous) : L'expédition part d'Espagne en 1519 avec cinq navires et environ 250 hommes. Magellan est tué aux Philippines en 1521. Elcano rentre en Espagne le 6 septembre 1522 sur la Victoria, avec seulement 18 hommes : c'est le premier tour du monde.

### Salle 4 — Le rivage — Rencontres et conquêtes (mot : **RENCONTRE**)

- **4-1 Trois peuples d'Amérique** (tri) : Les Aztèques vivent au Mexique ; leur capitale, Tenochtitlan, est bâtie sur un lac. Les Incas vivent dans la cordillère des Andes ; leur capitale est Cuzco. Les Iroquoiens du Saint-Laurent, au Canada, cultivent le maïs et vivent dans des maisons longues. En CM2 : Hernán Cortés prend Tenochtitlan en 1521 ; Francisco Pizarro capture l'empereur inca Atahualpa en 1532 ; Cartier rencontre le chef iroquoien Donnacona en 1534.
- **4-2 Le récit d'Itzel** (qcm) : D'après le texte, l'Amérique était peuplée de millions de personnes : elle n'était pas vide. Les Espagnols avaient des chevaux et des armes à feu, que les Amérindiens ne connaissaient pas. Les maladies comme la variole ont tué un très grand nombre d'Amérindiens. En CM2 : Cortés n'était pas seul, il avait des alliés amérindiens, ennemis des Aztèques.
- **4-3 Ce qu'il faut dire juste** (vraifaux) : L'Amérique était habitée depuis des milliers d'années : on dit aujourd'hui « arrivée des Européens ». Le maïs et la tomate viennent d'Amérique. Les chevaux n'existaient pas en Amérique à cette époque : les Espagnols les ont amenés. En CM2 : les Européens donnent des noms nouveaux à des lieux qui en avaient déjà, et le cacao, le chocolat des Aztèques, arrive en Europe.
- **4-4 L'intrus du panier** (intrus) : Le maïs, la pomme de terre, la tomate et le cacao viennent d'Amérique et ont traversé l'Atlantique vers l'Europe. Le blé est l'intrus : il a fait le chemin inverse, de l'Europe vers l'Amérique, comme le cheval et la vache.

### Salle 5 — Le cabinet du cartographe — Les premiers empires coloniaux (mot : **EMPIRES**)

- **5-1 La carte du partage** (plan) : Le repère 1 est la ligne de Tordesillas, tracée en 1494. Le repère 2, à l'ouest de la ligne, montre les terres attribuées à l'Espagne ; le repère 3, à l'est, celles attribuées au Portugal. En CM2, le repère 4 est le Brésil, qui dépasse la ligne vers l'est et devient portugais ; le repère 5 est la Nouvelle-France, où la France s'installe malgré le partage.
- **5-2 Les pavillons des colonies** (association) : Le Mexique et le Pérou sont dominés par l'Espagne. Le Brésil est une colonie du Portugal. La Nouvelle-France, autour de Québec, est une colonie de la France. En CM2 : Québec est fondée par Champlain en 1608 ; la Virginie, colonie anglaise, en 1607 ; le Brésil cultive la canne à sucre ; l'Espagne exploite les mines d'argent.
- **5-3 Le cadenas du coffre de bord** (code) : Colomb arrive aux Antilles en 1492, Vasco de Gama en Inde en 1498 et Cartier au Canada en 1534. En CM2, il faut aussi 1494, l'année du traité de Tordesillas, et 1522, l'année du retour d'Elcano.
- **5-4 Les richesses des colonies** (tri) : L'Espagne exploite l'or et surtout l'argent des mines du Mexique et du Pérou. Le Portugal crée au Brésil des plantations de canne à sucre. La France fait en Nouvelle-France le commerce des fourrures avec les Amérindiens. Dans les mines et les plantations, les colons font travailler de force des Amérindiens, puis des Africains réduits en esclavage : c'est le lien avec le jeu « Les Archives du port ».

## Fabriquer / mettre à jour

```
cd grandes-explorations/tests/donnees
python gen_enigmes.py ../../assets/data
python gen_lecons.py ../../assets/data
python gen_dialogues.py ../../assets/data
cd ../../..
python vingt-mille-lieues/outils/immersif/migrer-jeu.py grandes-explorations --theme grandes-explorations/tests/donnees/theme-immersif.json --force
python vingt-mille-lieues/outils/immersif/appliquer-narration.py grandes-explorations
python vingt-mille-lieues/outils/immersif/appliquer-grades.py grandes-explorations
python immersifs/grandes-explorations/outils/embarquer-donnees.py
node immersifs/grandes-explorations/tests/test-immersif.js
```

Les phrases des fiches (leçons CM2) sont dans `tests/donnees/fiches.py` : elles sont reprises mot pour mot par les justifications des grades Pilote et Cartographe
(`vingt-mille-lieues/outils/immersif/grades/grandes_explorations_s1.py` … `_s5.py`, identité dans `grandes_explorations_theme.py`, narration dans `narration/grandes-explorations.json`).
Cartes et schéma de la caravelle : SVG dessinés par `tests/donnees/schemas.py` (jamais par IA).

## Sources

- Programme d'histoire-géographie du cycle 3, arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026.
- Hérodote : « La vérité sur les bateaux de Colomb » (https://www.herodote.net/La_verite_sur_les_bateaux_de_Colomb-synthese-119.php) ; « 20 mai 1498 » (https://www.herodote.net/20_mai_1498-evenement-14980520.php) ; « 24 juillet 1534 » (https://www.herodote.net/almanach-ID-3801.php).
- National Geographic, Elcano (https://www.nationalgeographic.com/history/history-magazine/article/this-man-was-actually-first-to-sail-around-the-world).
- World History Encyclopedia, « Le traité de Tordesillas » (https://www.worldhistory.org/trans/fr/1-19935/le-traite-de-tordesillas/) ; « The Iberian Conquest of the Americas » (https://worldhistory.org/article/1920) ; UNESCO, Mémoire du monde, traité de Tordesillas.
- Schoolmouv, « Siège de Tenochtitlán (30 mai – 13 août 1521) ».
- Musée national de la Marine ; BnF ; BAnQ ; Lumni (références générales à consulter avec les élèves).
