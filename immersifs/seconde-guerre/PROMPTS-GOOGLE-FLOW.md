# Prompts Google Flow — Radio Londres

Ces prompts produisent les images du jeu `immersifs/seconde-guerre/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin. France de 1938 à 1945 : le village inventé de Chantelune-en-Morvan (Nièvre), sa salle de classe, sa petite gare, l'épicerie, une cabane de maquis dans la forêt, la place de la mairie pavoisée. Aucune personne réelle, aucun uniforme allemand, aucun symbole nazi, aucun combat, aucune image de camp. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1a2029 et #3b4a5a, lumières et accents #c2a061, #efe2c6, touches #d6dee6.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La salle de classe — `classe`

**Lieu** : La salle de classe de Chantelune-en-Morvan, en 1938. Une salle de classe de village, des pupitres en bois, un poêle, une carte de l'Europe au mur, une frise à demi effacée au tableau noir et un journal posé sur le bureau du maître.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La frise du tableau noir** — Une frise à la craie, à moitié effacée, au-dessus du bureau du maître. (énigme e1-1)
- en haut au centre : **La carte de l'Europe** — Une grande carte de l'Europe punaisée au mur, avec des étiquettes qui pendent. (énigme e1-2)
- en haut à droite : **Les cartons des élèves** — Une pile de cartons écrits à l'encre violette, sur un pupitre du premier rang. (énigme e1-3)
- au centre : **Le journal du maître** — Un journal plié en quatre sur le bureau, à côté de l'encrier. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle de classe de Chantelune-en-Morvan, en 1938. Une salle de classe de village, des pupitres en bois, un poêle, une carte de l'Europe au mur, une frise à demi effacée au tableau noir et un journal posé sur le bureau du maître. Quatre objets bien éclairés, nettement séparés et lisibles : La frise du tableau noir (en haut à gauche); La carte de l'Europe (en haut au centre); Les cartons des élèves (en haut à droite); Le journal du maître (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1a2029 et #3b4a5a, lumières et accents #c2a061, #efe2c6, touches #d6dee6.
```

### 2. La gare — `gare`

**Lieu** : La petite gare de Chantelune, en juin 1940. Un quai de gare de campagne encombré de valises et de vélos, une horloge, une carte de France au mur du bureau du chef de gare et un poste de radio posé sur le guichet.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le quai encombré** — Des valises, des vélos et des paniers entassés le long du quai. (énigme e2-1)
- en haut au centre : **Le poste du chef de gare** — Un poste de radio en bois posé sur le guichet, qui grésille. (énigme e2-2)
- en haut à droite : **La carte du bureau** — Une carte de France accrochée au mur du bureau, barrée d'une ligne rouge. (énigme e2-3)
- au centre : **Le carnet de Paul** — Un petit carnet noir posé à côté du poste, ouvert sur une page à trous. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La petite gare de Chantelune, en juin 1940. Un quai de gare de campagne encombré de valises et de vélos, une horloge, une carte de France au mur du bureau du chef de gare et un poste de radio posé sur le guichet. Quatre objets bien éclairés, nettement séparés et lisibles : Le quai encombré (en haut à gauche); Le poste du chef de gare (en haut au centre); La carte du bureau (en haut à droite); Le carnet de Paul (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1a2029 et #3b4a5a, lumières et accents #c2a061, #efe2c6, touches #d6dee6.
```

### 3. L'épicerie — `epicerie`

**Lieu** : L'épicerie de Madeleine, pendant l'hiver 1942-1943. Une petite épicerie de village aux étagères presque vides, un comptoir avec une balance, un cahier de comptes, des tickets de rationnement et une file de clients dehors, dans le froid.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le cahier de comptes** — Un cahier de comptes ouvert sur le comptoir, à côté de la balance. (énigme e3-1)
- en haut au centre : **Les étagères** — Des étagères presque vides, avec quelques bocaux et des étiquettes écrites à la main. (énigme e3-2)
- en haut à droite : **La convocation de Robert** — Une feuille officielle posée sur le comptoir, sous un poids de la balance. (énigme e3-3)
- au centre : **Le cahier de Lucienne** — Un cahier d'écolière posé sur une caisse, avec une liste de mots. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : L'épicerie de Madeleine, pendant l'hiver 1942-1943. Une petite épicerie de village aux étagères presque vides, un comptoir avec une balance, un cahier de comptes, des tickets de rationnement et une file de clients dehors, dans le froid. Quatre objets bien éclairés, nettement séparés et lisibles : Le cahier de comptes (en haut à gauche); Les étagères (en haut au centre); La convocation de Robert (en haut à droite); Le cahier de Lucienne (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1a2029 et #3b4a5a, lumières et accents #c2a061, #efe2c6, touches #d6dee6.
```

### 4. Le maquis — `maquis`

**Lieu** : Une cabane de résistants cachée dans la forêt du Morvan, au printemps 1944. Une cabane de bûcherons cachée sous les grands arbres, une table avec un poste émetteur dans une valise, un carnet, une carte roulée, une machine à écrire et une lampe tempête.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le carnet chiffré** — Un petit carnet couvert de lettres sans suite, à côté du poste émetteur. (énigme e4-1)
- en haut au centre : **Le carnet de liaison** — Un carnet usé, attaché par un élastique, posé sur la carte roulée. (énigme e4-2)
- en haut à droite : **Les fiches de Marc** — Des fiches tapées à la machine, en vrac sur la table. (énigme e4-3)
- au centre : **Le poste émetteur** — Un poste émetteur caché dans une valise, avec un casque d'écoute. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Une cabane de résistants cachée dans la forêt du Morvan, au printemps 1944. Une cabane de bûcherons cachée sous les grands arbres, une table avec un poste émetteur dans une valise, un carnet, une carte roulée, une machine à écrire et une lampe tempête. Quatre objets bien éclairés, nettement séparés et lisibles : Le carnet chiffré (en haut à gauche); Le carnet de liaison (en haut au centre); Les fiches de Marc (en haut à droite); Le poste émetteur (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1a2029 et #3b4a5a, lumières et accents #c2a061, #efe2c6, touches #d6dee6.
```

### 5. La place de la mairie — `mairie`

**Lieu** : La place de la mairie de Chantelune, le 8 mai 1945. Une place de village pavoisée de drapeaux tricolores, la mairie, un grand calendrier affiché, une carte de France dessinée à la main et, sur une table, un vieux poste de radio fermé.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La carte de Lucie** — Une carte de France dessinée à la main, épinglée sur le panneau de la mairie. (énigme e5-1)
- en haut au centre : **Le calendrier de la mairie** — Un grand calendrier affiché à côté de la porte de la mairie. (énigme e5-2)
- en haut à droite : **Les drapeaux** — Une caisse de drapeaux posée au pied d'un mât, pour la fête de la victoire. (énigme e5-3)
- au centre : **Le vieux poste de radio** — Un vieux poste de radio en bois, posé sur une table, avec un cadran de fréquences. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La place de la mairie de Chantelune, le 8 mai 1945. Une place de village pavoisée de drapeaux tricolores, la mairie, un grand calendrier affiché, une carte de France dessinée à la main et, sur une table, un vieux poste de radio fermé. Quatre objets bien éclairés, nettement séparés et lisibles : La carte de Lucie (en haut à gauche); Le calendrier de la mairie (en haut au centre); Les drapeaux (en haut à droite); Le vieux poste de radio (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1a2029 et #3b4a5a, lumières et accents #c2a061, #efe2c6, touches #d6dee6.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Bastien — `bastien`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Instituteur du village, genre : homme, cheveux courts, porte des lunettes, expression : instituteur de village calme et inquiet, pédagogue, qui veut que ses élèves comprennent le danger des dictatures sans leur faire peur. Tenue en rapport avec son rôle (Instituteur du village). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin.
```

### Paul — `paul`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Cheminot, employé de la gare, genre : homme, cheveux courts, expression : cheminot simple et chaleureux, bouleversé par l'exode mais attentif aux familles, partagé entre les deux voix de la radio. Tenue en rapport avec son rôle (Cheminot, employé de la gare). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin.
```

### Madeleine — `madeleine`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Épicière du village, genre : femme, cheveux courts, expression : épicière courageuse et pratique, discrète, qui protège les siens sans se plaindre. Tenue en rapport avec son rôle (Épicière du village). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin.
```

### Marc — `marc`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Opérateur radio du maquis, genre : homme, cheveux courts, expression : jeune opérateur radio prudent et précis, qui parle à voix basse et explique avec patience. Tenue en rapport avec son rôle (Opérateur radio du maquis). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin.
```

### Lucie — `lucie`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Agente de liaison, 17 ans, genre : femme, cheveux longs, expression : agente de liaison de 17 ans, vive et déterminée, émue le jour de la victoire, attachée au souvenir. Tenue en rapport avec son rôle (Agente de liaison, 17 ans). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `classe`) : « Lent travelling avant dans La salle de classe de Chantelune-en-Morvan, en 1938. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `gare`) : « Lent travelling avant dans La petite gare de Chantelune, en juin 1940. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `epicerie`) : « Lent travelling avant dans L'épicerie de Madeleine, pendant l'hiver 1942-1943. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `maquis`) : « Lent travelling avant dans Une cabane de résistants cachée dans la forêt du Morvan, au printemps 1944. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `mairie`) : « Lent travelling avant dans La place de la mairie de Chantelune, le 8 mai 1945. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/classe.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « La salle de classe de Chantelune-en-Morvan, en 1938 », sans voix ni musique |
| `assets/audio/ambiances/gare.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « La petite gare de Chantelune, en juin 1940 », sans voix ni musique |
| `assets/audio/ambiances/epicerie.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « L'épicerie de Madeleine, pendant l'hiver 1942-1943 », sans voix ni musique |
| `assets/audio/ambiances/maquis.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « Une cabane de résistants cachée dans la forêt du Morvan, au printemps 1944 », sans voix ni musique |
| `assets/audio/ambiances/mairie.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « La place de la mairie de Chantelune, le 8 mai 1945 », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
