# La Nurserie du zoo — escape game de sciences (cycle 3, jeu n°15)

Sciences et technologie, programme 2026 (BO n° 24 du 11 juin 2026), CM1, « Les êtres vivants dans leur environnement » : reproduction, croissance et développement ; progression de l'enseignant : année B, période 3 :
*Décrire les étapes du développement des animaux de la fécondation à la naissance. Mettre en relation le type de fécondation (interne ou externe) avec le mode de reproduction ovipare et vivipare des animaux.*

**Jouer** : version immersive `../immersifs/naissances-animaux/` (5 grades : Bénévole ≈ CE2, Apprenti soigneur ≈ CM1, Soigneur ≈ CM2, Biologiste ≈ 6ᵉ, Chef de la nurserie ≈ 5ᵉ).
Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas encore écrite.

**Vigilance** : pas de reproduction humaine (laissée à l'enseignant) ; aucune image ni vidéo de naissance ; les exceptions (ornithorynque, vipère aspic, requins) sont traitées comme des exceptions.

## Fil narratif

Une tempête a ouvert les fenêtres de la nurserie du zoo des Trois-Sources (inventé) : fiches et étiquettes des œufs et des berceaux sont mélangées. Les élèves, apprentis soigneurs, retrouvent comment naît chaque animal et cinq mots qui ouvrent le carnet de naissance :
> Une CELLULE de chaque parent forme l'œuf ; dans l'EAU ou dans le corps a lieu la fécondation ; l'ovipare pond, le VIVIPARE porte son petit ; l'EMBRYON grandit jusqu'à la NAISSANCE.

| Salle | Lieu | Guide (personnage inventé) | Mot |
|---|---|---|---|
| 1 | Le laboratoire de la vétérinaire, à côté de la nurserie | Inès, vétérinaire du zoo | CELLULE |
| 2 | L'aquarium et la mare pédagogique | Théo, soigneur de l'aquarium et de la mare | EAU |
| 3 | La galerie des animaux étonnants | Malo, soigneur de la galerie des animaux étonnants | VIVIPARE |
| 4 | La couveuse de la ferme du zoo | Jeanne, éleveuse de poules de la ferme du zoo | EMBRYON |
| 5 | Le bureau du carnet de naissance | Sacha, élève de CM2 en visite scolaire | NAISSANCE |

## 🎯 Compétences du programme (vue d'ensemble)

| Salle | Compétence du programme |
|---|---|
| 1 | Décrire les étapes du développement des animaux de la fécondation à la naissance : rencontre d'un gamète mâle et d'un gamète femelle, cellule-œuf, embryon |
| 2 | Distinguer fécondation externe (dans l'eau) et fécondation interne (dans le corps de la femelle) ; exemples |
| 3 | Mettre en relation le type de fécondation (interne ou externe) avec le mode de reproduction ovipare ou vivipare ; exceptions |
| 4 | Décrire le développement avant la naissance : couvaison et éclosion de l'œuf de poule, gestation de mammifères (durées sourcées) |
| 5 | Pour des animaux variés, dire le type de fécondation et le mode de reproduction (tableau à deux entrées) |

CM1 : 3 énigmes par salle (15) ; CM2 : 4 énigmes par salle (20). Repères en CM1 (cellule du mâle, cellule de la femelle, durées arrondies) ; vocabulaire exact et calculs en CM2 (gamètes, spermatozoïde, ovule, embryon, durées en jours).

## Solutions (générées depuis `assets/data/enigmes.json`)

### Salle 1 — Le laboratoire de la vétérinaire — La fécondation (mot : **CELLULE**)

<details><summary><b>1-1 Le schéma du microscope</b> (plan)</summary>

Sur ce dessin, la petite cellule qui nage est la cellule du mâle (repère 1) et la grosse cellule est celle de la femelle (repère 2) ; leur union donne la cellule-œuf (repère 3). En CM2, on emploie les mots spermatozoïde et ovule ; la cellule-œuf se divise et devient un embryon (repère 4) ; le repère 5 montre le flagelle qui fait avancer le spermatozoïde.

</details>

<details><summary><b>1-2 Les notes d'Inès</b> (vraifaux)</summary>

Un petit commence avec la rencontre d'une cellule du mâle et d'une cellule de la femelle : c'est la fécondation, qui donne l'œuf, première cellule du petit. Il faut donc un mâle et une femelle. En CM2 : les spermatozoïdes sont produits par les testicules et les ovules par les ovaires ; l'ovule est bien plus gros que le spermatozoïde ; un œuf de poule acheté au magasin n'a pas été fécondé.

</details>

<details><summary><b>1-3 Les bocaux étiquetés</b> (association)</summary>

La fécondation est la rencontre des deux cellules ; l'œuf est la première cellule du petit ; le mâle apporte une cellule minuscule et la femelle une grosse cellule. En CM2 : gamètes est le nom des cellules reproductrices, l'ovaire produit les ovules, le testicule les spermatozoïdes, et l'embryon est le petit qui commence à se former.

</details>

<details><summary><b>1-4 Du gamète à l'embryon</b> (ordre, CM2)</summary>

Le mâle produit des spermatozoïdes et la femelle des ovules ; un spermatozoïde rencontre un ovule et s'unit à lui : c'est la fécondation ; elle donne une cellule-œuf, qui se divise en deux, puis en quatre, puis en des milliers de cellules : c'est un embryon.

</details>


### Salle 2 — L'aquarium et la mare — Fécondation externe et interne (mot : **EAU**)

<details><summary><b>2-1 Les fiches de la mare</b> (tri)</summary>

La grenouille, le crapaud, la truite et le saumon ont une fécondation externe : les cellules se rencontrent dans l'eau. La poule, le chat, la vache, le canard, le crocodile et le requin ont une fécondation interne, dans le corps de la femelle. En CM2, le canard et le requin vivent dans l'eau mais leur fécondation est interne.

</details>

<details><summary><b>2-2 Les questions de Théo</b> (qcm)</summary>

Chez la grenouille, la femelle pond ses ovules dans l'eau et le mâle y libère ses cellules : la fécondation est externe. Chez la poule, elle a lieu dans son corps : elle est interne. En CM2 : beaucoup de cellules se perdent dans l'eau, c'est pourquoi les femelles pondent des centaines d'ovules ; une fécondation interne suit un accouplement.

</details>

<details><summary><b>2-3 Le panneau de la mare</b> (trous)</summary>

Au printemps, la grenouille femelle pond ses ovules dans l'eau ; le mâle y libère ses cellules : la fécondation est externe. Chez les oiseaux et les mammifères, elle a lieu dans le corps de la femelle : elle est interne. En CM2 : les gamètes perdus dans l'eau expliquent les pontes nombreuses ; les reptiles, les requins et les insectes ont aussi une fécondation interne.

</details>

<details><summary><b>2-4 Le grand bassin</b> (intrus, CM2)</summary>

La grenouille, la truite et le saumon ont une fécondation externe, dans l'eau. La tortue marine vit dans la mer, mais le mâle et la femelle s'accouplent : sa fécondation est interne, et elle va pondre sur une plage.

</details>


### Salle 3 — La galerie des surprises — Ovipares et vivipares (mot : **VIVIPARE**)

<details><summary><b>3-1 La vitrine des pondeurs</b> (intrus)</summary>

La poule, le crocodile et la tortue pondent des œufs : ils sont ovipares. Le chat ne pond pas : ses petits naissent vivants, il est vivipare. En CM2 : le lapin, la girafe et le dauphin sont des mammifères vivipares ; l'ornithorynque est un mammifère qui pond des œufs, une exception.

</details>

<details><summary><b>3-2 Le tableau de la galerie</b> (tri)</summary>

La poule, la grenouille, le papillon et le crocodile pondent : ils sont ovipares. La vache, le lapin et la girafe sont vivipares. En CM2 : la grenouille et la truite ont une fécondation externe et pondent ; la poule, le crocodile et le papillon ont une fécondation interne et pondent ; la girafe, le kangourou et le lion ont une fécondation interne et sont vivipares. Aucun animal n'a une fécondation externe et un petit qui grandit dans le ventre de sa mère.

</details>

<details><summary><b>3-3 Les surprises de Malo</b> (vraifaux)</summary>

L'ornithorynque est un mammifère qui pond des œufs et nourrit ses petits avec son lait. Tous les poissons ne pondent pas de la même façon : certains requins pondent, d'autres donnent naissance à des petits vivants. En CM2 : la vipère aspic garde ses œufs dans son ventre jusqu'à l'éclosion, ses petits naissent formés ; la roussette pond des œufs protégés par une capsule ; le requin-marteau donne naissance à des petits vivants ; ces exceptions ne changent pas la règle.

</details>

<details><summary><b>3-4 Les panneaux des exceptions</b> (association, CM2)</summary>

L'ornithorynque est un mammifère qui pond ; la vipère aspic garde ses œufs dans son ventre jusqu'à l'éclosion ; la roussette pond des œufs dans une capsule ; le requin-marteau donne naissance à des petits vivants ; la tortue marine vit dans la mer mais pond sur une plage.

</details>


### Salle 4 — La couveuse de la ferme — Le développement avant la naissance (mot : **EMBRYON**)

<details><summary><b>4-1 Le calendrier de la couveuse</b> (ordre)</summary>

Au début, on ne voit que le jaune ; vers le 3e jour, le cœur bat et des vaisseaux sanguins entourent le jaune ; vers le 7e jour, on reconnaît la forme du poussin ; vers le 18e jour, les plumes sont bien visibles ; le 21e jour, le poussin perce la coquille avec le diamant de son bec.

</details>

<details><summary><b>4-2 L'œuf à la loupe</b> (plan)</summary>

La coquille (repère 1) protège ; le jaune (repère 2) nourrit l'embryon ; le blanc (repère 3) l'entoure, le protège et lui fournit de l'eau. En CM2 : la chambre à air (repère 4) est du côté arrondi de l'œuf ; l'embryon (repère 5) est la petite tache posée sur le jaune.

</details>

<details><summary><b>4-3 Le cadenas des berceaux</b> (code)</summary>

La poule couve 21 jours, la gestation de la lapine dure 31 jours et celle de la vache 9 mois. En CM2 : la vache porte son veau 280 jours ; la jument porte son poulain 336 − 280 = 56 jours de plus que la vache ; la couvaison de la poule dure 21 jours, soit 3 semaines ; l'éléphante peut porter son petit jusqu'à 22 mois.

</details>

<details><summary><b>4-4 Le ventre de la jument</b> (vraifaux, CM2)</summary>

Le poulain se développe dans l'utérus de la jument ; il reçoit nourriture et oxygène par le placenta et le cordon ombilical. Cette durée s'appelle la gestation : 336 jours environ chez la jument, bien plus longue que chez la lapine (31 jours). En général, plus un mammifère est grand, plus sa gestation est longue.

</details>


### Salle 5 — Le bureau du carnet de naissance — La grande classification (mot : **NAISSANCE**)

<details><summary><b>5-1 Les enclos du zoo</b> (tri)</summary>

La grenouille et la truite : fécondation externe, ovipares. La poule, le crocodile et la tortue : fécondation interne, ovipares. La girafe, le lion et le dauphin : fécondation interne, vivipares. En CM2 : le crapaud et le saumon sont dans la première case ; l'autruche, le papillon, le manchot et la tortue dans la deuxième ; le kangourou, le zèbre, le dauphin et la chauve-souris dans la troisième.

</details>

<details><summary><b>5-2 Les berceaux de la nurserie</b> (association)</summary>

Le têtard sort d'un œuf pondu dans la mare ; le poussin sort d'un œuf couvé 21 jours ; le chaton a grandi dans le ventre de sa mère. En CM2 : le girafon naît vivant après une longue gestation ; le crocodile sort d'un œuf pondu sur la berge ; le petit de la vipère aspic naît déjà formé, l'œuf ayant éclos dans le ventre de sa mère.

</details>

<details><summary><b>5-3 Le carnet de naissance</b> (qcm)</summary>

Pour classer un animal, on se demande où a lieu la fécondation et comment naît le petit. Un animal à fécondation externe pond des œufs. En CM2 : aucune femelle ne porte dans son ventre un œuf fécondé dans l'eau ; une fécondation interne peut donner un animal ovipare (la poule) ou vivipare (le chat) ; une exception comme l'ornithorynque ne change pas la règle.

</details>

<details><summary><b>5-4 Les clés des enclos</b> (code, CM2)</summary>

Dans le registre, 2 animaux ont une fécondation externe (la grenouille et le saumon) ; 6 sont ovipares (la grenouille, le saumon, l'autruche, le manchot, la tortue et le papillon) ; 4 sont vivipares (le zèbre, le kangourou, le dauphin et la chauve-souris).

</details>


## Sources

- Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026), CM1, « Les êtres vivants dans leur environnement » : reproduction, croissance et développement (progression de l'enseignant : année B, période 3)
- Fondation La main à la pâte, « Biologie animale : fonctions de reproduction »
- Fondation La main à la pâte, séquence « Et ils eurent beaucoup d'enfants »
- Muséum national d'histoire naturelle et INPN (fiches espèces)
- Écolothèque de Montpellier Méditerranée Métropole, « Naissance d'un poussin »
- Techno-Science, glossaire « Gestation » (durées moyennes)
- Futura Sciences, « Pourquoi certains requins pondent-ils des œufs ? »
- Lumni, vidéos « La reproduction des animaux » (cycle 3). Détail : README.md, section Sources.

## Fichiers

- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; schémas SVG dans `tests/donnees/schemas.py`.
- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py naissances-animaux --theme naissances-animaux/tests/donnees/theme-immersif.json --force`, puis `appliquer-grades.py naissances-animaux`, `appliquer-narration.py naissances-animaux`, `finir-jeu.py naissances-animaux`.
- Grades : `vingt-mille-lieues/outils/immersif/grades/naissances_animaux_s1..s5.py` et `naissances_animaux_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/naissances-animaux.json`.
