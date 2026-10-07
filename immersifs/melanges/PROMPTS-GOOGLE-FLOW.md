# Prompts Google Flow — Le Laboratoire de Madame Mélange

Ces prompts produisent les images du jeu `immersifs/melanges/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin. Univers contemporain mais chaleureux : un laboratoire d'enfants avec balances, fioles, atelier de tri et marais salants. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0a181d et #17303a, lumières et accents #35b8b0, #ffe08a, touches #9be7ff.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La salle des balances — `balances`

**Lieu** : La salle des balances — rez-de-chaussée du laboratoire. Sur les étagères, des balances de toutes les tailles : une vieille balance à deux plateaux en cuivre, une balance électronique, une boîte de masses marquées. Au sol, des fioles renversées portent encore leur étiquette.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La balance à plateaux** — Une balance à deux plateaux : on y compare des masses. (énigme e1-1)
- en haut au centre : **La balance électronique** — Une balance à affichage : une autre façon de peser. (énigme e1-2)
- en haut à droite : **Le flacon de liquide** — Un flacon qu'il faut peser sans oublier le récipient. (énigme e1-3)
- au centre : **Les poids en laiton** — Des masses marquées : g, kg, mg. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle des balances — rez-de-chaussée du laboratoire. Sur les étagères, des balances de toutes les tailles : une vieille balance à deux plateaux en cuivre, une balance électronique, une boîte de masses marquées. Au sol, des fioles renversées portent encore leur étiquette. Quatre objets bien éclairés, nettement séparés et lisibles : La balance à plateaux (en haut à gauche); La balance électronique (en haut au centre); Le flacon de liquide (en haut à droite); Les poids en laiton (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0a181d et #17303a, lumières et accents #35b8b0, #ffe08a, touches #9be7ff.
```

### 2. La cuisine d'essai — `cuisine`

**Lieu** : La cuisine d'essai — là où l'on teste les mélanges du quotidien. Un plan de travail blanc, une cafetière, un sucrier, des verres gradués et une balance de cuisine. Une affiche au mur : « Cuisine d'essai du laboratoire : ici, on mesure, on ne goûte pas. »

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le verre d'eau sucrée** — Le sucre a disparu dans l'eau : est-ce vrai ? (énigme e2-1)
- en haut au centre : **Le cahier taché** — Le cahier de Marius, tâché de café. (énigme e2-2)
- en haut à droite : **La tasse de café** — Un café sucré : combien pèse-t-il ? (énigme e2-3)
- au centre : **Le cadenas de la cuisine** — Un cadenas qui garde le placard. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La cuisine d'essai — là où l'on teste les mélanges du quotidien. Un plan de travail blanc, une cafetière, un sucrier, des verres gradués et une balance de cuisine. Une affiche au mur : « Cuisine d'essai du laboratoire : ici, on mesure, on ne goûte pas. » Quatre objets bien éclairés, nettement séparés et lisibles : Le verre d'eau sucrée (en haut à gauche); Le cahier taché (en haut au centre); La tasse de café (en haut à droite); Le cadenas de la cuisine (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0a181d et #17303a, lumières et accents #35b8b0, #ffe08a, touches #9be7ff.
```

### 3. La salle des fioles — `fioles`

**Lieu** : La salle des fioles — premier étage. Des centaines de fioles bouchées, bien rangées sur des étagères. Certaines sont transparentes, d'autres ont deux couches, d'autres encore sont troubles avec un dépôt au fond. Au mur, le portrait de Madame Mélange, loupe à la main.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les fioles homogènes** — Des fioles où l'on ne distingue rien, ou presque. (énigme e3-1)
- en haut au centre : **L'étagère aux fioles** — Une fiole qui n'a pas sa place là. (énigme e3-2)
- en haut à droite : **La loupe d'observation** — On observe ce qu'on voit dans un mélange. (énigme e3-3)
- au centre : **Les idées de Lila** — Des affirmations de Lila à vérifier. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle des fioles — premier étage. Des centaines de fioles bouchées, bien rangées sur des étagères. Certaines sont transparentes, d'autres ont deux couches, d'autres encore sont troubles avec un dépôt au fond. Au mur, le portrait de Madame Mélange, loupe à la main. Quatre objets bien éclairés, nettement séparés et lisibles : Les fioles homogènes (en haut à gauche); L'étagère aux fioles (en haut au centre); La loupe d'observation (en haut à droite); Les idées de Lila (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0a181d et #17303a, lumières et accents #35b8b0, #ffe08a, touches #9be7ff.
```

### 4. L'atelier de tri — `atelier`

**Lieu** : L'atelier de tri — au sous-sol. Des bacs en plastique alignés sur un établi, des tamis accrochés au mur, une bassine d'eau et un gros aimant en fer à cheval. Dans un bac, du sable gris brille par endroits : de la limaille de fer.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les bacs de tri** — Quatre bacs, quatre méthodes de tri. (énigme e4-1)
- en haut au centre : **Le tamis** — Un tamis qui sépare des grains. (énigme e4-2)
- en haut à droite : **L'aimant** — Un aimant qui attire certains métaux. (énigme e4-3)
- au centre : **L'établi de Nadia** — Un établi où Nadia sépare ses mélanges. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : L'atelier de tri — au sous-sol. Des bacs en plastique alignés sur un établi, des tamis accrochés au mur, une bassine d'eau et un gros aimant en fer à cheval. Dans un bac, du sable gris brille par endroits : de la limaille de fer. Quatre objets bien éclairés, nettement séparés et lisibles : Les bacs de tri (en haut à gauche); Le tamis (en haut au centre); L'aimant (en haut à droite); L'établi de Nadia (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0a181d et #17303a, lumières et accents #35b8b0, #ffe08a, touches #9be7ff.
```

### 5. La saline — `saline`

**Lieu** : La saline — la paillasse de filtration, face aux marais salants. Une grande fenêtre donne sur les bassins d'un marais salant. Sur la paillasse : un entonnoir, du papier filtre, des béchers, une coupelle posée au soleil. Et, au centre, le dernier bocal de Madame Mélange.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le filtre à café** — Filtrer, décanter, évaporer : trois méthodes. (énigme e5-1)
- en haut au centre : **Le montage de filtration** — Un entonnoir, un filtre, un bécher. (énigme e5-2)
- en haut à droite : **Le tas de sel** — Les cristaux de sel de la saline. (énigme e5-3)
- au centre : **Le testament de Madame Mélange** — Un parchemin qui donne les étapes de la séparation. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La saline — la paillasse de filtration, face aux marais salants. Une grande fenêtre donne sur les bassins d'un marais salant. Sur la paillasse : un entonnoir, du papier filtre, des béchers, une coupelle posée au soleil. Et, au centre, le dernier bocal de Madame Mélange. Quatre objets bien éclairés, nettement séparés et lisibles : Le filtre à café (en haut à gauche); Le montage de filtration (en haut au centre); Le tas de sel (en haut à droite); Le testament de Madame Mélange (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0a181d et #17303a, lumières et accents #35b8b0, #ffe08a, touches #9be7ff.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Lila — `lila`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Apprentie chimiste, 11 ans, genre : fille, cheveux longs, porte des lunettes, expression : curieuse et enthousiaste, adore expérimenter. Tenue en rapport avec son rôle (Apprentie chimiste, 11 ans). Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin.
```

### Marius — `marius`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Cuisinier de la cuisine d'essai, genre : homme, cheveux courts, expression : cuisinier gourmand et blagueur. Tenue en rapport avec son rôle (Cuisinier de la cuisine d'essai). Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin.
```

### Nadia — `nadia`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Laborantine de l'atelier de tri, genre : femme, cheveux longs, expression : précise et méthodique. Tenue en rapport avec son rôle (Laborantine de l'atelier de tri). Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin.
```

### Yann — `yann`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Paludier, ramasseur de sel de mer, genre : homme, cheveux courts, expression : paludier posé, parle de la mer. Tenue en rapport avec son rôle (Paludier, ramasseur de sel de mer). Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin.
```

### Madame Mélange — `melange`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Chimiste, directrice du laboratoire, genre : femme, cheveux longs, porte des lunettes, expression : directrice mystérieuse, solennelle. Tenue en rapport avec son rôle (Chimiste, directrice du laboratoire). Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `balances`) : « Lent travelling avant dans La salle des balances — rez-de-chaussée du laboratoire. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `cuisine`) : « Lent travelling avant dans La cuisine d'essai — là où l'on teste les mélanges du quotidien. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `fioles`) : « Lent travelling avant dans La salle des fioles — premier étage. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `atelier`) : « Lent travelling avant dans L'atelier de tri — au sous-sol. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `saline`) : « Lent travelling avant dans La saline — la paillasse de filtration, face aux marais salants. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.
