# Prompts Google Flow — La Caravelle du capitaine

Ces prompts produisent les images du jeu `immersifs/grandes-explorations/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin. Univers contemporain : un festival de la mer à Saint-Malo, à bord d'une copie de caravelle. Le journal de bord lu aux visiteurs raconte les explorations et les conquêtes des XVe et XVIe siècles. Aucune scène de violence, aucune personne réelle. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f2433 et #1f4f6b, lumières et accents #c9a227, #ffe8a8, touches #cfe3ee.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La cale aux épices — `cale`

**Lieu** : La cale de la Rose des vents. Une cale basse, éclairée par des lanternes. Des sacs de toile, des coffres et des tonneaux. Une carte roulée dépasse d'un coffre ouvert.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La carte roulée** — Une carte roulée dépasse d'un coffre ouvert ; l'eau de la tempête a effacé les noms. (énigme e1-1)
- en haut au centre : **Les sacs de la cale** — Des sacs de toile et des coffres dont les étiquettes ont glissé au sol. (énigme e1-2)
- en haut à droite : **Le tonneau aux histoires** — Un tonneau couvert de feuillets punaisés : les histoires que racontent les visiteurs. (énigme e1-3)
- au centre : **Les caisses du négociant** — Trois caisses vides marquées richesse, religion, savoir. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La cale de la Rose des vents. Une cale basse, éclairée par des lanternes. Des sacs de toile, des coffres et des tonneaux. Une carte roulée dépasse d'un coffre ouvert. Quatre objets bien éclairés, nettement séparés et lisibles : La carte roulée (en haut à gauche); Les sacs de la cale (en haut au centre); Le tonneau aux histoires (en haut à droite); Les caisses du négociant (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f2433 et #1f4f6b, lumières et accents #c9a227, #ffe8a8, touches #cfe3ee.
```

### 2. Le pont de la caravelle — `pont`

**Lieu** : Le pont de la Rose des vents. Le pont en bois, les mâts, les voiles repliées. Près de la barre, un coffre d'instruments en laiton est ouvert : une boussole, un astrolabe, un sablier.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le coffre d'instruments** — Un coffre en laiton ouvert près de la barre : boussole, astrolabe, sablier. (énigme e2-1)
- en haut au centre : **Le plan de la caravelle** — Un plan cloué près du mât, dont les noms ont été arrachés par le vent. (énigme e2-2)
- en haut à droite : **La barre** — La barre du navire, où Rosa interroge ceux qui veulent la tenir. (énigme e2-3)
- au centre : **L'astrolabe de midi** — L'astrolabe suspendu à un crochet, prêt à viser le Soleil. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le pont de la Rose des vents. Le pont en bois, les mâts, les voiles repliées. Près de la barre, un coffre d'instruments en laiton est ouvert : une boussole, un astrolabe, un sablier. Quatre objets bien éclairés, nettement séparés et lisibles : Le coffre d'instruments (en haut à gauche); Le plan de la caravelle (en haut au centre); La barre (en haut à droite); L'astrolabe de midi (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f2433 et #1f4f6b, lumières et accents #c9a227, #ffe8a8, touches #cfe3ee.
```

### 3. La chambre des cartes — `cartes`

**Lieu** : La chambre des cartes, sous le château arrière. Une petite pièce sous le château arrière. Sur la table, une grande carte du monde, un compas à pointes sèches et une corde où pendent les pages du journal.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La corde aux pages** — Une corde tendue où pendent, en désordre, les pages du journal. (énigme e3-1)
- en haut au centre : **Les cartons des explorateurs** — Des cartons portant des noms d'explorateurs, posés sur la table. (énigme e3-2)
- en haut à droite : **La grande carte** — La grande carte du monde, couverte de routes de couleur sans étiquettes. (énigme e3-3)
- au centre : **La page mouillée** — Une page du journal encore humide, dont des mots ont coulé. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La chambre des cartes, sous le château arrière. Une petite pièce sous le château arrière. Sur la table, une grande carte du monde, un compas à pointes sèches et une corde où pendent les pages du journal. Quatre objets bien éclairés, nettement séparés et lisibles : La corde aux pages (en haut à gauche); Les cartons des explorateurs (en haut au centre); La grande carte (en haut à droite); La page mouillée (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f2433 et #1f4f6b, lumières et accents #c9a227, #ffe8a8, touches #cfe3ee.
```

### 4. Le rivage — `rivage`

**Lieu** : La tente des conteurs, sur le quai. Sur le quai, une grande tente de toile. À l'intérieur, des tapis, un panier de maïs, de cacao et de tomates, et des dessins de Tenochtitlan accrochés aux piquets.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les dessins de la tente** — Des dessins accrochés aux piquets de la tente : une ville sur un lac, des montagnes, des maisons longues. (énigme e4-1)
- en haut au centre : **Le livre d'Itzel** — Un livre ouvert sur les genoux d'Itzel, avec un texte adapté pour les élèves. (énigme e4-2)
- en haut à droite : **Le sable du rivage** — Un bac de sable où des visiteurs ont écrit des phrases avec un bâton. (énigme e4-3)
- au centre : **Le panier d'Itzel** — Un panier rempli de maïs, de tomates, de cacao et de pommes de terre. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La tente des conteurs, sur le quai. Sur le quai, une grande tente de toile. À l'intérieur, des tapis, un panier de maïs, de cacao et de tomates, et des dessins de Tenochtitlan accrochés aux piquets. Quatre objets bien éclairés, nettement séparés et lisibles : Les dessins de la tente (en haut à gauche); Le livre d'Itzel (en haut au centre); Le sable du rivage (en haut à droite); Le panier d'Itzel (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f2433 et #1f4f6b, lumières et accents #c9a227, #ffe8a8, touches #cfe3ee.
```

### 5. Le cabinet du cartographe — `cabinet`

**Lieu** : Le cabinet du cartographe, au fond du navire. Un réduit éclairé par une lampe. Au mur, une carte partagée par une ligne en pointillés. Des pavillons pliés sur une étagère. Au centre, le coffre de bord, fermé par un cadenas à chiffres.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La carte du partage** — Au mur, une carte coupée par une ligne en pointillés. (énigme e5-1)
- en haut au centre : **Les pavillons pliés** — Des pavillons pliés sur une étagère, chacun avec une fiche. (énigme e5-2)
- en haut à droite : **Le coffre de bord** — Le coffre de bord, fermé par un cadenas à chiffres. (énigme e5-3)
- au centre : **Les registres de marchandises** — Des registres de marchandises posés sur le coffre. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le cabinet du cartographe, au fond du navire. Un réduit éclairé par une lampe. Au mur, une carte partagée par une ligne en pointillés. Des pavillons pliés sur une étagère. Au centre, le coffre de bord, fermé par un cadenas à chiffres. Quatre objets bien éclairés, nettement séparés et lisibles : La carte du partage (en haut à gauche); Les pavillons pliés (en haut au centre); Le coffre de bord (en haut à droite); Les registres de marchandises (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f2433 et #1f4f6b, lumières et accents #c9a227, #ffe8a8, touches #cfe3ee.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Amaury — `amaury`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Guide du festival, spécialiste du commerce des épices, genre : homme, cheveux courts, expression : guide chaleureux et gourmand d'histoires, aime faire sentir les épices aux visiteurs, appelle les élèves « moussaillons ». Tenue en rapport avec son rôle (Guide du festival, spécialiste du commerce des épices). Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin.
```

### Rosa — `rosa`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Cartographe, restauratrice de cartes anciennes, genre : femme, cheveux longs, porte des lunettes, expression : cartographe précise et patiente, explique les instruments avec des gestes, insiste sur la sécurité en mer. Tenue en rapport avec son rôle (Cartographe, restauratrice de cartes anciennes). Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin.
```

### Bastien — `bastien`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Capitaine de la caravelle, genre : homme, cheveux courts, expression : capitaine posé, parle peu mais juste, rappelle que les terres atteintes étaient habitées. Tenue en rapport avec son rôle (Capitaine de la caravelle). Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin.
```

### Itzel — `itzel`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Conteuse venue de Mexico, genre : femme, cheveux longs, expression : conteuse calme et fière, donne le point de vue des peuples d'amérique, sobre sur les violences. Tenue en rapport avec son rôle (Conteuse venue de Mexico). Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin.
```

### Simon — `simon`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Mousse de la caravelle, genre : homme, cheveux courts, expression : mousse enthousiaste et curieux, pose les questions que les élèves se posent, aime les cadenas. Tenue en rapport avec son rôle (Mousse de la caravelle). Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `cale`) : « Lent travelling avant dans La cale de la Rose des vents. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `pont`) : « Lent travelling avant dans Le pont de la Rose des vents. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `cartes`) : « Lent travelling avant dans La chambre des cartes, sous le château arrière. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `rivage`) : « Lent travelling avant dans La tente des conteurs, sur le quai. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `cabinet`) : « Lent travelling avant dans Le cabinet du cartographe, au fond du navire. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/cale.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « La cale de la Rose des vents », sans voix ni musique |
| `assets/audio/ambiances/pont.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « Le pont de la Rose des vents », sans voix ni musique |
| `assets/audio/ambiances/cartes.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « La chambre des cartes, sous le château arrière », sans voix ni musique |
| `assets/audio/ambiances/rivage.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « La tente des conteurs, sur le quai », sans voix ni musique |
| `assets/audio/ambiances/cabinet.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « Le cabinet du cartographe, au fond du navire », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
