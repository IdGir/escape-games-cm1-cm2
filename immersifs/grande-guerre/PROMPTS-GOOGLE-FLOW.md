# Prompts Google Flow — Les Lettres du poilu

Ces prompts produisent les images du jeu `immersifs/grande-guerre/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin. France de 1914 à 1922 : le village inventé de Vaux-les-Tilleuls (Côte-d'Or), sa place et sa mairie, un abri de tranchée calme, une usine d'obus, une salle de classe devenue hôpital, le monument aux morts. Aucune personne réelle, aucun blessé visible, aucun combat, aucune explosion. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1b222e et #3d4f6b, lumières et accents #c9a45c, #f1e3c4, touches #d9e2ec.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La place du village — `place`

**Lieu** : La place de Vaux-les-Tilleuls, devant la mairie, le 2 août 1914. Une place de village de Bourgogne, l'église, la mairie et son affiche blanche sur la porte, un tilleul, des familles rassemblées et des valises posées au pied de la fontaine.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le cahier de Jeanne** — Un cahier d'écolière ouvert sur le rebord de la fontaine, des dates griffonnées dans tous les sens. (énigme e1-1)
- en haut au centre : **L'affiche de la mairie** — Une grande affiche blanche collée sur la porte de la mairie, un peu de travers. (énigme e1-2)
- en haut à droite : **La carte de Louis** — Une carte d'Europe dessinée au crayon par Louis, avec des pays sans nom. (énigme e1-3)
- au centre : **La carte postale** — Une carte postale colorée : des soldats souriants, une fleur au bout du fusil. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La place de Vaux-les-Tilleuls, devant la mairie, le 2 août 1914. Une place de village de Bourgogne, l'église, la mairie et son affiche blanche sur la porte, un tilleul, des familles rassemblées et des valises posées au pied de la fontaine. Quatre objets bien éclairés, nettement séparés et lisibles : Le cahier de Jeanne (en haut à gauche); L'affiche de la mairie (en haut au centre); La carte de Louis (en haut à droite); La carte postale (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1b222e et #3d4f6b, lumières et accents #c9a45c, #f1e3c4, touches #d9e2ec.
```

### 2. L'abri de la tranchée — `tranchee`

**Lieu** : Un abri creusé sous la terre, dans une tranchée du front, au printemps 1916. Un abri étroit étayé de planches, une bougie dans une boîte de conserve, une couverture, un masque dans sa boîte, des lettres et un colis ouvert sur une caisse.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le croquis de la tranchée** — Une feuille de carnet clouée à une planche, avec un dessin de tranchée sans légende. (énigme e2-1)
- en haut au centre : **La lettre barrée** — Une lettre dont plusieurs lignes ont été recouvertes d'encre noire. (énigme e2-2)
- en haut à droite : **Les notes de 1916** — Deux pages de carnet mélangées, l'une marquée d'un V, l'autre d'un S. (énigme e2-3)
- au centre : **La photo des camarades** — Une petite photo usée de quatre soldats en capote, dont Amadou, souriant. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Un abri creusé sous la terre, dans une tranchée du front, au printemps 1916. Un abri étroit étayé de planches, une bougie dans une boîte de conserve, une couverture, un masque dans sa boîte, des lettres et un colis ouvert sur une caisse. Quatre objets bien éclairés, nettement séparés et lisibles : Le croquis de la tranchée (en haut à gauche); La lettre barrée (en haut au centre); Les notes de 1916 (en haut à droite); La photo des camarades (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1b222e et #3d4f6b, lumières et accents #c9a45c, #f1e3c4, touches #d9e2ec.
```

### 3. L'usine d'obus — `usine`

**Lieu** : L'atelier d'une usine d'obus de la ville voisine, en 1917. Un grand atelier sous une verrière, des machines alignées, des caisses d'obus vides, des ouvrières en blouse et en foulard, et sur un établi la lettre de Marcelle.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les photos du journal** — Des photos découpées dans un journal, épinglées au-dessus de l'établi. (énigme e3-1)
- en haut au centre : **Le tableau des nouvelles** — Un tableau noir de l'atelier, divisé en deux colonnes à la craie. (énigme e3-2)
- en haut à droite : **Le carnet de l'usine** — Un petit carnet taché d'huile posé près d'une machine. (énigme e3-3)
- au centre : **Les portraits de l'arrière** — Une série de petits portraits dessinés au crayon sur le mur du vestiaire. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : L'atelier d'une usine d'obus de la ville voisine, en 1917. Un grand atelier sous une verrière, des machines alignées, des caisses d'obus vides, des ouvrières en blouse et en foulard, et sur un établi la lettre de Marcelle. Quatre objets bien éclairés, nettement séparés et lisibles : Les photos du journal (en haut à gauche); Le tableau des nouvelles (en haut au centre); Le carnet de l'usine (en haut à droite); Les portraits de l'arrière (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1b222e et #3d4f6b, lumières et accents #c9a45c, #f1e3c4, touches #d9e2ec.
```

### 4. L'hôpital de l'école — `hopital`

**Lieu** : La salle de classe de Vaux-les-Tilleuls transformée en hôpital, le 11 novembre 1918. Une salle de classe aux pupitres poussés contre le mur, des lits blancs alignés, une infirmière, un tableau noir avec la date du jour, et par la fenêtre le clocher qui sonne.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les étiquettes du mur** — Des étiquettes de pansements épinglées en vrac au mur de la classe. (énigme e4-1)
- en haut au centre : **Le tableau noir** — Le tableau noir de la classe, avec la date du jour écrite à la craie. (énigme e4-2)
- en haut à droite : **Le registre de l'hôpital** — Un gros registre relié de toile, ouvert sur une page de chiffres. (énigme e4-3)
- au centre : **Le journal de 1919** — Une coupure de journal jaunie, collée dans le cahier d'Odette. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle de classe de Vaux-les-Tilleuls transformée en hôpital, le 11 novembre 1918. Une salle de classe aux pupitres poussés contre le mur, des lits blancs alignés, une infirmière, un tableau noir avec la date du jour, et par la fenêtre le clocher qui sonne. Quatre objets bien éclairés, nettement séparés et lisibles : Les étiquettes du mur (en haut à gauche); Le tableau noir (en haut au centre); Le registre de l'hôpital (en haut à droite); Le journal de 1919 (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1b222e et #3d4f6b, lumières et accents #c9a45c, #f1e3c4, touches #d9e2ec.
```

### 5. Le monument aux morts — `monument`

**Lieu** : La place du village, devant le nouveau monument aux morts, le 11 novembre 1922. Un monument de pierre claire surmonté d'une statue de poilu, des noms gravés, une gerbe de fleurs bleues, blanches et rouges, et le village rassemblé en silence.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le plan du monument** — Un grand plan roulé posé sur une table devant la mairie. (énigme e5-1)
- en haut au centre : **Le discours du maire** — Quelques feuillets écrits à la plume, tenus par un caillou sur la table. (énigme e5-2)
- en haut à droite : **Le registre des noms** — Le registre de la mairie, ouvert sur la liste des noms à graver. (énigme e5-3)
- au centre : **La dernière lettre** — Une enveloppe fermée par un petit cadenas à chiffres. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La place du village, devant le nouveau monument aux morts, le 11 novembre 1922. Un monument de pierre claire surmonté d'une statue de poilu, des noms gravés, une gerbe de fleurs bleues, blanches et rouges, et le village rassemblé en silence. Quatre objets bien éclairés, nettement séparés et lisibles : Le plan du monument (en haut à gauche); Le discours du maire (en haut au centre); Le registre des noms (en haut à droite); La dernière lettre (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1b222e et #3d4f6b, lumières et accents #c9a45c, #f1e3c4, touches #d9e2ec.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Jeanne — `jeanne`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Petite sœur de Louis, 10 ans en 1914, genre : femme, cheveux longs, expression : petite fille de dix ans, sérieuse et attachante, inquiète pour son frère mais curieuse de tout comprendre. Tenue en rapport avec son rôle (Petite sœur de Louis, 10 ans en 1914). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin.
```

### Louis — `louis`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Soldat, l'auteur des lettres, genre : homme, cheveux courts, expression : jeune soldat tendre et pudique, rassure sa petite sœur, parle simplement de sa vie sans rien d'effrayant. Tenue en rapport avec son rôle (Soldat, l'auteur des lettres). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin.
```

### Marcelle — `marcelle`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Ouvrière dans une usine d'obus, genre : femme, cheveux longs, expression : ouvrière énergique et fière de son travail, chaleureuse, lucide sur l'injustice faite aux femmes. Tenue en rapport avec son rôle (Ouvrière dans une usine d'obus). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin.
```

### Odette — `odette`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Infirmière à l'hôpital installé dans l'école, genre : femme, cheveux courts, porte des lunettes, expression : infirmière douce et calme, émue mais posée, explique avec patience. Tenue en rapport avec son rôle (Infirmière à l'hôpital installé dans l'école). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin.
```

### Émile — `emile`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Maire de Vaux-les-Tilleuls, genre : homme, cheveux courts, porte des lunettes, expression : maire de village grave et bienveillant, attaché au souvenir, inquiet pour la paix. Tenue en rapport avec son rôle (Maire de Vaux-les-Tilleuls). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `place`) : « Lent travelling avant dans La place de Vaux-les-Tilleuls, devant la mairie, le 2 août 1914. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `tranchee`) : « Lent travelling avant dans Un abri creusé sous la terre, dans une tranchée du front, au printemps 1916. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `usine`) : « Lent travelling avant dans L'atelier d'une usine d'obus de la ville voisine, en 1917. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `hopital`) : « Lent travelling avant dans La salle de classe de Vaux-les-Tilleuls transformée en hôpital, le 11 novembre 1918. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `monument`) : « Lent travelling avant dans La place du village, devant le nouveau monument aux morts, le 11 novembre 1922. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/place.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « La place de Vaux-les-Tilleuls, devant la mairie, le 2 août 1914 », sans voix ni musique |
| `assets/audio/ambiances/tranchee.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « Un abri creusé sous la terre, dans une tranchée du front, au printemps 1916 », sans voix ni musique |
| `assets/audio/ambiances/usine.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « L'atelier d'une usine d'obus de la ville voisine, en 1917 », sans voix ni musique |
| `assets/audio/ambiances/hopital.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « La salle de classe de Vaux-les-Tilleuls transformée en hôpital, le 11 novembre 1918 », sans voix ni musique |
| `assets/audio/ambiances/monument.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « La place du village, devant le nouveau monument aux morts, le 11 novembre 1922 », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
