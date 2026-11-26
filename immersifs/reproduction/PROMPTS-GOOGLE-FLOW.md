# Prompts Google Flow — Le Jardin de la vie

Ces prompts produisent les images du jeu `immersifs/reproduction/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin. Univers contemporain : le jardin des Coteaux (inventé) et la ferme voisine, en Bourgogne : serre, rucher au bord d'un verger, potager d'école, cour de ferme avec étang, bergerie et mare. Aucune personne réelle, aucun animal blessé, aucun animal habillé ou qui parle. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16210f et #2f5d2a, lumières et accents #e0a526, #fbecc2, touches #e3f0d8.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La serre du botaniste — `serre`

**Lieu** : La serre du jardin des Coteaux. Une serre vitrée pleine de fleurs, une table de dissection avec des loupes, une grande planche de fleur tombée au sol, des étiquettes éparpillées et des pots renversés par le vent.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La planche de la fleur** — Une grande planche illustrée d'une fleur coupée en deux, tombée au pied de la table, ses étiquettes éparpillées. (énigme e1-1)
- en haut au centre : **Le fichier des pièces** — Une boîte à fiches ouverte, avec des cartes mélangées sur la table de dissection. (énigme e1-2)
- en haut à droite : **Le carnet d'observation** — Un carnet à spirale ouvert, mouillé par une goutte de pluie, posé à côté d'une loupe. (énigme e1-3)
- au centre : **La table de dissection** — Une table avec une tulipe ouverte, une pince, une loupe et une feuille où sont collées des pièces. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La serre du jardin des Coteaux. Une serre vitrée pleine de fleurs, une table de dissection avec des loupes, une grande planche de fleur tombée au sol, des étiquettes éparpillées et des pots renversés par le vent. Quatre objets bien éclairés, nettement séparés et lisibles : La planche de la fleur (en haut à gauche); Le fichier des pièces (en haut au centre); Le carnet d'observation (en haut à droite); La table de dissection (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16210f et #2f5d2a, lumières et accents #e0a526, #fbecc2, touches #e3f0d8.
```

### 2. Le rucher — `rucher`

**Lieu** : Le rucher au fond du jardin, près du verger. Des ruches en bois au bord d'un verger en fleurs, une cabane d'apicultrice avec une combinaison accrochée, un cahier taché par la pluie, des pots de miel et un panneau à moitié peint.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les dessins du rucher** — Une série de dessins accrochés à une ficelle sous l'auvent de la cabane, décrochés par le vent. (énigme e2-1)
- en haut au centre : **Le cahier du rucher** — Un cahier taché par la pluie, posé sur une ruche, avec des mots effacés. (énigme e2-2)
- en haut à droite : **Le plan des ruches** — Un plan du verger et des champs voisins, avec des petites ruches en bois à poser. (énigme e2-3)
- au centre : **Le panneau des pollinisateurs** — Un grand panneau en bois à moitié peint, destiné aux agriculteurs voisins. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le rucher au fond du jardin, près du verger. Des ruches en bois au bord d'un verger en fleurs, une cabane d'apicultrice avec une combinaison accrochée, un cahier taché par la pluie, des pots de miel et un panneau à moitié peint. Quatre objets bien éclairés, nettement séparés et lisibles : Les dessins du rucher (en haut à gauche); Le cahier du rucher (en haut au centre); Le plan des ruches (en haut à droite); Le panneau des pollinisateurs (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16210f et #2f5d2a, lumières et accents #e0a526, #fbecc2, touches #e3f0d8.
```

### 3. Le potager de l'école — `potager`

**Lieu** : Le potager de l'école, au bord du jardin. Des carrés de légumes, une table avec quatre pots d'expérience, des boîtes de graines renversées, une affiche du cycle de vie d'une plante et un arrosoir.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les boîtes de graines** — Des boîtes en carton renversées dans l'allée, avec des fruits et des graines de toutes formes. (énigme e3-1)
- en haut au centre : **Les pots d'expérience** — Quatre pots en plastique sur la table, garnis de coton et de haricots, avec un tableau à moitié effacé. (énigme e3-2)
- en haut à droite : **L'affiche du cycle** — Une grande affiche ronde du cycle de vie d'une plante, dont les images sont tombées dans l'herbe. (énigme e3-3)
- au centre : **La graine ouverte** — Une graine de haricot gonflée d'eau, ouverte en deux sur une soucoupe, à côté d'une loupe. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le potager de l'école, au bord du jardin. Des carrés de légumes, une table avec quatre pots d'expérience, des boîtes de graines renversées, une affiche du cycle de vie d'une plante et un arrosoir. Quatre objets bien éclairés, nettement séparés et lisibles : Les boîtes de graines (en haut à gauche); Les pots d'expérience (en haut au centre); L'affiche du cycle (en haut à droite); La graine ouverte (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16210f et #2f5d2a, lumières et accents #e0a526, #fbecc2, touches #e3f0d8.
```

### 4. La ferme des Coteaux — `ferme`

**Lieu** : La cour de la ferme des Coteaux, près de l'étang. Une cour de ferme avec un poulailler, une étable, un petit étang aux roseaux, un tableau noir où est écrit le registre des animaux, et des panneaux tombés près de la barrière.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le tableau des questions** — Un tableau noir à l'entrée de la ferme pédagogique, où les visiteurs écrivent leurs questions. (énigme e4-1)
- en haut au centre : **Le registre de la ferme** — Un gros registre ouvert sur un tonneau, avec la liste des animaux de la ferme et de l'étang. (énigme e4-2)
- en haut à droite : **Le panneau de l'enclos** — Un panneau tombé devant l'enclos, avec des cartes d'animaux épinglées. (énigme e4-3)
- au centre : **Les panneaux de l'étang** — Deux petits panneaux plantés au bord de l'étang, près des roseaux. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La cour de la ferme des Coteaux, près de l'étang. Une cour de ferme avec un poulailler, une étable, un petit étang aux roseaux, un tableau noir où est écrit le registre des animaux, et des panneaux tombés près de la barrière. Quatre objets bien éclairés, nettement séparés et lisibles : Le tableau des questions (en haut à gauche); Le registre de la ferme (en haut au centre); Le panneau de l'enclos (en haut à droite); Les panneaux de l'étang (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16210f et #2f5d2a, lumières et accents #e0a526, #fbecc2, touches #e3f0d8.
```

### 5. La bergerie et la mare — `bergerie`

**Lieu** : La bergerie de la ferme et la mare voisine. Une bergerie avec des brebis et leurs agneaux, une couveuse avec des œufs, une mare pleine de têtards, la trousse de la vétérinaire et le grand portail fermé par un cadenas à chiffres.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La liste de tournée** — Une planchette avec la liste des animaux à visiter, posée sur la trousse de la vétérinaire. (énigme e5-1)
- en haut au centre : **Le carnet de la vétérinaire** — Un petit carnet à couverture rouge, ouvert sur une botte de paille. (énigme e5-2)
- en haut à droite : **La couveuse et la mare** — Une couveuse vitrée avec des œufs, et à côté un aquarium de têtards pris dans la mare. (énigme e5-3)
- au centre : **Le portail du jardin** — Le grand portail en fer entre la ferme et le jardin, fermé par un cadenas à chiffres. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La bergerie de la ferme et la mare voisine. Une bergerie avec des brebis et leurs agneaux, une couveuse avec des œufs, une mare pleine de têtards, la trousse de la vétérinaire et le grand portail fermé par un cadenas à chiffres. Quatre objets bien éclairés, nettement séparés et lisibles : La liste de tournée (en haut à gauche); Le carnet de la vétérinaire (en haut au centre); La couveuse et la mare (en haut à droite); Le portail du jardin (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16210f et #2f5d2a, lumières et accents #e0a526, #fbecc2, touches #e3f0d8.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Basile — `basile`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Botaniste, responsable de la serre du jardin des Coteaux, genre : homme, cheveux courts, porte des lunettes, expression : botaniste posé et précis, aime les loupes et les planches bien rangées, explique avec des mots exacts. Tenue en rapport avec son rôle (Botaniste, responsable de la serre du jardin des Coteaux). Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin.
```

### Capucine — `capucine`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Apicultrice, elle s'occupe des ruches du jardin, genre : femme, cheveux longs, expression : apicultrice chaleureuse, parle de ses abeilles avec admiration mais sans leur prêter d'intentions, attentive aux pollinisateurs. Tenue en rapport avec son rôle (Apicultrice, elle s'occupe des ruches du jardin). Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin.
```

### Tom — `tom`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Élève de CM2, jardinier du potager de l'école voisine, genre : homme, cheveux courts, expression : élève de cm2 enthousiaste, curieux, aime les expériences et vérifier par lui-même. Tenue en rapport avec son rôle (Élève de CM2, jardinier du potager de l'école voisine). Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin.
```

### Yasmine — `yasmine`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Éleveuse de la ferme des Coteaux, genre : femme, cheveux longs, expression : éleveuse énergique et concrète, connaît chaque animal de la ferme, va droit au but. Tenue en rapport avec son rôle (Éleveuse de la ferme des Coteaux). Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin.
```

### Nadia — `nadia`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Vétérinaire des animaux de la ferme, genre : femme, cheveux courts, porte des lunettes, expression : vétérinaire douce et rigoureuse, rassurante, insiste sur le vocabulaire juste. Tenue en rapport avec son rôle (Vétérinaire des animaux de la ferme). Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `serre`) : « Lent travelling avant dans La serre du jardin des Coteaux. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `rucher`) : « Lent travelling avant dans Le rucher au fond du jardin, près du verger. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `potager`) : « Lent travelling avant dans Le potager de l'école, au bord du jardin. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `ferme`) : « Lent travelling avant dans La cour de la ferme des Coteaux, près de l'étang. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `bergerie`) : « Lent travelling avant dans La bergerie de la ferme et la mare voisine. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/serre.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « La serre du jardin des Coteaux », sans voix ni musique |
| `assets/audio/ambiances/rucher.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « Le rucher au fond du jardin, près du verger », sans voix ni musique |
| `assets/audio/ambiances/potager.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « Le potager de l'école, au bord du jardin », sans voix ni musique |
| `assets/audio/ambiances/ferme.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « La cour de la ferme des Coteaux, près de l'étang », sans voix ni musique |
| `assets/audio/ambiances/bergerie.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « La bergerie de la ferme et la mare voisine », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
