# Prompts Google Flow — Le Secret du donjon

Ces prompts produisent les images du jeu `immersifs/chateau-fort/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ. Moyen Âge central (Xe-XIIIe siècles), un château en construction et le village à ses pieds. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #14151a et #2b2d35, lumières et accents #b94a3a, #ffb55a, touches #a9c4e0.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La motte et la palissade — `motte`

**Lieu** : Le tertre de la vieille tour, au petit matin. Une grosse butte de terre porte encore les souches noircies d'une tour de bois. Tout autour, une palissade à moitié tombée. En bas, des charrettes de pierres attendent : le chantier du nouveau château commence ici.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La butte et ses souches** — Une grosse butte de terre où se dressait une tour de bois : pourquoi bâtir si haut ? (énigme e1-1)
- en haut au centre : **Les charrettes de pierres** — Des charrettes chargées de blocs : la pierre arrive là où le bois brûlait. (énigme e1-2)
- en haut à droite : **L'échafaudage des ouvriers** — Tailleurs de pierre, maçons, charpentiers : chaque métier a son outil. (énigme e1-3)
- au centre : **Le carnet du maître maçon** — Un carnet ouvert sur une pierre, aux phrases à moitié effacées. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le tertre de la vieille tour, au petit matin. Une grosse butte de terre porte encore les souches noircies d'une tour de bois. Tout autour, une palissade à moitié tombée. En bas, des charrettes de pierres attendent : le chantier du nouveau château commence ici. Quatre objets bien éclairés, nettement séparés et lisibles : La butte et ses souches (en haut à gauche); Les charrettes de pierres (en haut au centre); L'échafaudage des ouvriers (en haut à droite); Le carnet du maître maçon (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #14151a et #2b2d35, lumières et accents #b94a3a, #ffb55a, touches #a9c4e0.
```

### 2. Les remparts — `remparts`

**Lieu** : Le chemin de ronde, au-dessus de l'entrée. De là, on voit tout : le fossé plein d'eau, le pont-levis relevé, la herse coincée à mi-hauteur, les tours rondes aux angles et, au centre, la tour maîtresse. Chaque ouverture, chaque saillie a une raison d'être.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le plan sur la table de pierre** — Un plan du château à légender : tours, fossé, pont-levis. (énigme e2-1)
- en haut au centre : **La herse et le pont-levis** — Les engins de l'entrée, chacun avec sa fonction. (énigme e2-2)
- en haut à droite : **Les créneaux** — Le haut du rempart, où l'on s'abrite pour tirer. (énigme e2-3)
- au centre : **Le treuil du pont-levis** — Un lourd treuil de bois fermé par un cadenas à chiffres. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le chemin de ronde, au-dessus de l'entrée. De là, on voit tout : le fossé plein d'eau, le pont-levis relevé, la herse coincée à mi-hauteur, les tours rondes aux angles et, au centre, la tour maîtresse. Chaque ouverture, chaque saillie a une raison d'être. Quatre objets bien éclairés, nettement séparés et lisibles : Le plan sur la table de pierre (en haut à gauche); La herse et le pont-levis (en haut au centre); Les créneaux (en haut à droite); Le treuil du pont-levis (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #14151a et #2b2d35, lumières et accents #b94a3a, #ffb55a, touches #a9c4e0.
```

### 3. La grande salle — `grandesalle`

**Lieu** : La grande salle du donjon, avant le repas. Une cheminée assez large pour s'y tenir debout, des tapisseries contre le froid, une longue table posée sur des tréteaux. À côté, une petite chapelle ; plus loin, les cuisines. C'est ici que le seigneur reçoit, juge, festoie et montre ce qu'il est.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La grande cheminée** — Un feu où l'on cuit les viandes : le château, c'est aussi une maison. (énigme e3-1)
- en haut au centre : **La table du seigneur** — Une longue table où le seigneur prend ses repas et rend justice. (énigme e3-2)
- en haut à droite : **Le banc des serviteurs** — Les gens qui vivent au château : cuisiniers, écuyers, gardes. (énigme e3-3)
- au centre : **Le coffre aux objets** — Un coffre où traîne un objet qui n'a rien à faire là. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La grande salle du donjon, avant le repas. Une cheminée assez large pour s'y tenir debout, des tapisseries contre le froid, une longue table posée sur des tréteaux. À côté, une petite chapelle ; plus loin, les cuisines. C'est ici que le seigneur reçoit, juge, festoie et montre ce qu'il est. Quatre objets bien éclairés, nettement séparés et lisibles : La grande cheminée (en haut à gauche); La table du seigneur (en haut au centre); Le banc des serviteurs (en haut à droite); Le coffre aux objets (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #14151a et #2b2d35, lumières et accents #b94a3a, #ffb55a, touches #a9c4e0.
```

### 4. Le village et les champs — `village`

**Lieu** : Le village, au pied du château. Une vingtaine de maisons basses, murs de torchis et toits de chaume, serrées autour de l'église. Devant chaque porte, un jardin. Au-delà, les champs en longues bandes, et les bois où les cochons vont manger les glands.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le calendrier du village** — Les travaux des champs au fil des saisons. (énigme e4-1)
- en haut au centre : **La remise aux outils** — Les outils d'un paysan : faux, herse, charrue. (énigme e4-2)
- en haut à droite : **La maison de Mahaut** — Une chaumière au toit de paille : une journée dans une vie de paysanne. (énigme e4-3)
- au centre : **La cloche du village** — La cloche qui rythme le travail et cache un mot. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le village, au pied du château. Une vingtaine de maisons basses, murs de torchis et toits de chaume, serrées autour de l'église. Devant chaque porte, un jardin. Au-delà, les champs en longues bandes, et les bois où les cochons vont manger les glands. Quatre objets bien éclairés, nettement séparés et lisibles : Le calendrier du village (en haut à gauche); La remise aux outils (en haut au centre); La maison de Mahaut (en haut à droite); La cloche du village (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #14151a et #2b2d35, lumières et accents #b94a3a, #ffb55a, touches #a9c4e0.
```

### 5. Le moulin du seigneur — `moulin`

**Lieu** : Le moulin à eau, au bord de la rivière. La roue tourne, la meule gronde, la farine blanchit tout. Contre le mur, des sacs marqués d'une croix : la part prélevée sur chaque sac moulu. À côté, le four du seigneur, où tout le village vient cuire son pain.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les sacs de grain** — Ce que les paysans apportent au moulin : farine, blé, redevances. (énigme e5-1)
- en haut au centre : **Le registre de la meunière** — Un registre où Perrine note ce qui est dû au seigneur. (énigme e5-2)
- en haut à droite : **La roue du moulin** — La roue tourne : ce que les paysans donnent, ce qu'ils reçoivent. (énigme e5-3)
- au centre : **Le plan du domaine** — Un plan qui montre le château et le village côte à côte. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le moulin à eau, au bord de la rivière. La roue tourne, la meule gronde, la farine blanchit tout. Contre le mur, des sacs marqués d'une croix : la part prélevée sur chaque sac moulu. À côté, le four du seigneur, où tout le village vient cuire son pain. Quatre objets bien éclairés, nettement séparés et lisibles : Les sacs de grain (en haut à gauche); Le registre de la meunière (en haut au centre); La roue du moulin (en haut à droite); Le plan du domaine (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #14151a et #2b2d35, lumières et accents #b94a3a, #ffb55a, touches #a9c4e0.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Colin — `colin`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Jeune page au service du seigneur, 11 ans, genre : garçon, cheveux courts, expression : vif et bavard, un peu fier de sa mission de page. Tenue en rapport avec son rôle (Jeune page au service du seigneur, 11 ans). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ.
```

### Maître Josselin — `josselin`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Maître maçon du chantier du château, genre : homme, cheveux courts, expression : franc et pratique, parle comme un homme de chantier. Tenue en rapport avec son rôle (Maître maçon du chantier du château). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ.
```

### Dame Aliénor — `alienor`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Dame du château, elle gouverne le domaine, genre : femme, cheveux longs, expression : posée, autoritaire mais juste. Tenue en rapport avec son rôle (Dame du château, elle gouverne le domaine). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ.
```

### Mahaut — `mahaut`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Jeune paysanne du village, 11 ans, genre : fille, cheveux longs, expression : directe, rieuse, connaît la terre. Tenue en rapport avec son rôle (Jeune paysanne du village, 11 ans). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ.
```

### Perrine — `perrine`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Meunière du moulin du seigneur, genre : femme, cheveux courts, expression : maligne, un brin moqueuse, compte tout. Tenue en rapport avec son rôle (Meunière du moulin du seigneur). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `motte`) : « Lent travelling avant dans Le tertre de la vieille tour, au petit matin. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `remparts`) : « Lent travelling avant dans Le chemin de ronde, au-dessus de l'entrée. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `grandesalle`) : « Lent travelling avant dans La grande salle du donjon, avant le repas. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `village`) : « Lent travelling avant dans Le village, au pied du château. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `moulin`) : « Lent travelling avant dans Le moulin à eau, au bord de la rivière. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/motte.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « Le tertre de la vieille tour, au petit matin », sans voix ni musique |
| `assets/audio/ambiances/remparts.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « Le chemin de ronde, au-dessus de l'entrée », sans voix ni musique |
| `assets/audio/ambiances/grandesalle.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « La grande salle du donjon, avant le repas », sans voix ni musique |
| `assets/audio/ambiances/village.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « Le village, au pied du château », sans voix ni musique |
| `assets/audio/ambiances/moulin.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « Le moulin à eau, au bord de la rivière », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
