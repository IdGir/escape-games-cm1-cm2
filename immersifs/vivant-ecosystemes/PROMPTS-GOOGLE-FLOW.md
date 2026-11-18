# Prompts Google Flow — L'Expédition biodiversité

Ces prompts produisent les images du jeu `immersifs/vivant-ecosystemes/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin. Univers contemporain : la réserve naturelle inventée du Val-des-Saules, en Bourgogne, sa tente-laboratoire, la cabane du garde, une ancienne carrière, une mare, un pré avec des ruches et un étang. Aucune personne réelle, aucun animal blessé, aucun dinosaure vivant. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #15261a et #2f5f3a, lumières et accents #e3b23c, #f8e5b0, touches #d2e9ef.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La tente-laboratoire — `tente`

**Lieu** : La tente-laboratoire de l'expédition, au bord du ruisseau. Une grande tente de toile avec une table pliante, des loupes, un microscope de terrain, des boîtes d'observation et des carnets qui sèchent sur un fil.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le carnet de terrain** — Un carnet ouvert qui sèche sur la table, avec le dessin d'une mésange sans étiquettes. (énigme e1-1)
- en haut au centre : **Les notes mouillées** — Une pile de feuilles gondolées, l'encre a coulé par endroits. (énigme e1-2)
- en haut à droite : **Les boîtes d'observation** — Des boîtes transparentes avec une loupe sur le couvercle ; les fiches sont tombées à côté. (énigme e1-3)
- au centre : **La question des visiteurs** — Un panneau de questions laissé par les visiteurs de la veille. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La tente-laboratoire de l'expédition, au bord du ruisseau. Une grande tente de toile avec une table pliante, des loupes, un microscope de terrain, des boîtes d'observation et des carnets qui sèchent sur un fil. Quatre objets bien éclairés, nettement séparés et lisibles : Le carnet de terrain (en haut à gauche); Les notes mouillées (en haut au centre); Les boîtes d'observation (en haut à droite); La question des visiteurs (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #15261a et #2f5f3a, lumières et accents #e3b23c, #f8e5b0, touches #d2e9ef.
```

### 2. La cabane du garde — `cabane`

**Lieu** : La cabane du garde, à l'entrée de la forêt. Une cabane en bois avec des caisses de rangement, des fiches d'animaux, une grande clé de détermination punaisée au mur et un bac de feuilles mortes plein de petites bêtes.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les caisses renversées** — Des caisses en bois couchées sur le plancher, les fiches éparpillées. (énigme e2-1)
- en haut au centre : **L'affiche des règles** — Une affiche à moitié décollée : « Comment classer ? » (énigme e2-2)
- en haut à droite : **La clé des petites bêtes** — Une grande clé de détermination punaisée au mur, au-dessus d'un bac de feuilles mortes. (énigme e2-3)
- au centre : **La caisse des poils** — Une caisse étiquetée, avec une fiche qui dépasse. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La cabane du garde, à l'entrée de la forêt. Une cabane en bois avec des caisses de rangement, des fiches d'animaux, une grande clé de détermination punaisée au mur et un bac de feuilles mortes plein de petites bêtes. Quatre objets bien éclairés, nettement séparés et lisibles : Les caisses renversées (en haut à gauche); L'affiche des règles (en haut au centre); La clé des petites bêtes (en haut à droite); La caisse des poils (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #15261a et #2f5f3a, lumières et accents #e3b23c, #f8e5b0, touches #d2e9ef.
```

### 3. L'ancienne carrière — `carriere`

**Lieu** : L'ancienne carrière de calcaire de la réserve. Une paroi de roche en couches, des bacs de fossiles, un tamis, une grande frise du temps et une vitrine fermée par un cadenas.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La grande frise** — Une longue frise en tissu déroulée sur le sol, ses étapes décrochées. (énigme e3-1)
- en haut au centre : **Le tiroir des fossiles** — Un tiroir à compartiments, les fossiles sans leurs étiquettes. (énigme e3-2)
- en haut à droite : **Le panneau de la crise** — Un panneau illustré sur la disparition des dinosaures, avec des phrases à vérifier. (énigme e3-3)
- au centre : **La vitrine au cadenas** — Une vitrine fermée par un cadenas à chiffres, derrière laquelle brillent des ammonites. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : L'ancienne carrière de calcaire de la réserve. Une paroi de roche en couches, des bacs de fossiles, un tamis, une grande frise du temps et une vitrine fermée par un cadenas. Quatre objets bien éclairés, nettement séparés et lisibles : La grande frise (en haut à gauche); Le tiroir des fossiles (en haut au centre); Le panneau de la crise (en haut à droite); La vitrine au cadenas (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #15261a et #2f5f3a, lumières et accents #e3b23c, #f8e5b0, touches #d2e9ef.
```

### 4. La mare et le pré fleuri — `mare`

**Lieu** : La mare de la réserve et le pré fleuri où sont les ruches. Une mare entourée de roseaux, des nénuphars, des libellules au-dessus de l'eau, et plus loin un pré plein de fleurs avec trois ruches en bois.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le dessin de la mare** — Un grand dessin de la mare sur un chevalet, ses étiquettes envolées. (énigme e4-1)
- en haut au centre : **Les relevés de Rose** — Un carnet de relevés posé sur une ruche, plein de mots mélangés. (énigme e4-2)
- en haut à droite : **Les questions de Rose** — Rose, voile d'apicultrice relevée, près des ruches qui bourdonnent. (énigme e4-3)
- au centre : **Les panneaux du sentier** — Des panneaux en bois à planter le long du sentier, encore vierges. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La mare de la réserve et le pré fleuri où sont les ruches. Une mare entourée de roseaux, des nénuphars, des libellules au-dessus de l'eau, et plus loin un pré plein de fleurs avec trois ruches en bois. Quatre objets bien éclairés, nettement séparés et lisibles : Le dessin de la mare (en haut à gauche); Les relevés de Rose (en haut au centre); Les questions de Rose (en haut à droite); Les panneaux du sentier (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #15261a et #2f5f3a, lumières et accents #e3b23c, #f8e5b0, touches #d2e9ef.
```

### 5. Le ponton de l'étang — `etang`

**Lieu** : Le ponton du grand étang de la réserve. Un ponton de bois au-dessus de l'eau, une barque, un carnet de pêche, et sur une table la boîte fermée de la carte du vivant.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La chaîne d'Élio** — Des cartes d'êtres vivants accrochées à une ficelle le long du ponton, dans le désordre. (énigme e5-1)
- en haut au centre : **Les flèches du carnet** — Le carnet de pêche d'Élio, couvert de flèches au crayon. (énigme e5-2)
- en haut à droite : **L'affiche déchirée** — Une affiche de la réserve déchirée, des morceaux de mots manquent. (énigme e5-3)
- au centre : **La boîte de la carte du vivant** — Une boîte en bois fermée par un cadenas à trois chiffres, posée sur la table du ponton. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le ponton du grand étang de la réserve. Un ponton de bois au-dessus de l'eau, une barque, un carnet de pêche, et sur une table la boîte fermée de la carte du vivant. Quatre objets bien éclairés, nettement séparés et lisibles : La chaîne d'Élio (en haut à gauche); Les flèches du carnet (en haut au centre); L'affiche déchirée (en haut à droite); La boîte de la carte du vivant (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #15261a et #2f5f3a, lumières et accents #e3b23c, #f8e5b0, touches #d2e9ef.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Lina — `lina`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Biologiste de terrain, cheffe de l'expédition, genre : femme, cheveux longs, expression : biologiste de terrain énergique et précise, aime observer et compter, encourage les jeunes naturalistes. Tenue en rapport avec son rôle (Biologiste de terrain, cheffe de l'expédition). Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin.
```

### Hugo — `hugo`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Garde de la réserve naturelle, genre : homme, cheveux courts, expression : garde de la réserve calme et patient, rigoureux sur les règles du classement, connaît chaque sentier. Tenue en rapport avec son rôle (Garde de la réserve naturelle). Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin.
```

### Amara — `amara`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Paléontologue, genre : femme, cheveux courts, porte des lunettes, expression : paléontologue passionnée, parle des millions d'années comme d'hier, s'émerveille de chaque fossile. Tenue en rapport avec son rôle (Paléontologue). Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin.
```

### Rose — `rose`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Apicultrice du pré de la réserve, genre : femme, cheveux longs, expression : apicultrice chaleureuse, voit des liens partout, parle de ses abeilles avec tendresse. Tenue en rapport avec son rôle (Apicultrice du pré de la réserve). Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin.
```

### Élio — `elio`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Pêcheur de l'étang, genre : homme, cheveux courts, expression : pêcheur jovial et malin, connaît l'étang par cœur, aime poser des devinettes. Tenue en rapport avec son rôle (Pêcheur de l'étang). Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `tente`) : « Lent travelling avant dans La tente-laboratoire de l'expédition, au bord du ruisseau. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `cabane`) : « Lent travelling avant dans La cabane du garde, à l'entrée de la forêt. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `carriere`) : « Lent travelling avant dans L'ancienne carrière de calcaire de la réserve. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `mare`) : « Lent travelling avant dans La mare de la réserve et le pré fleuri où sont les ruches. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `etang`) : « Lent travelling avant dans Le ponton du grand étang de la réserve. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/tente.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « La tente-laboratoire de l'expédition, au bord du ruisseau », sans voix ni musique |
| `assets/audio/ambiances/cabane.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « La cabane du garde, à l'entrée de la forêt », sans voix ni musique |
| `assets/audio/ambiances/carriere.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « L'ancienne carrière de calcaire de la réserve », sans voix ni musique |
| `assets/audio/ambiances/mare.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « La mare de la réserve et le pré fleuri où sont les ruches », sans voix ni musique |
| `assets/audio/ambiances/etang.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « Le ponton du grand étang de la réserve », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
