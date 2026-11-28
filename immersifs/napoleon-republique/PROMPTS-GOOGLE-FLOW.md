# Prompts Google Flow — Le Testament de l'Empereur

Ces prompts produisent les images du jeu `immersifs/napoleon-republique/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin. France de 1800 à aujourd'hui : une antichambre du palais des Tuileries (1800), la cathédrale Notre-Dame décorée pour le sacre (1804), un bivouac de la Grande Armée, le dôme des Invalides et une salle des mariages de mairie (aujourd'hui). Aucune personne réelle (jamais Napoléon ni Joséphine en personne), aucun combat, aucune blessure. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16223a et #2f4a7a, lumières et accents #c9a24a, #f2e3c2, touches #d9e2ef.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. Le palais des Tuileries — `tuileries`

**Lieu** : Une antichambre du palais des Tuileries, à Paris, en 1800. Une antichambre aux boiseries claires, des cartes d'Italie et d'Égypte épinglées au mur, un pupitre avec un carnet de campagne, une giberne de soldat posée sur une chaise et un bureau couvert de lettres.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le carnet de campagne** — Un petit carnet de cuir posé sur le pupitre, aux pages volantes. (énigme e1-1)
- en haut au centre : **La giberne d'Antoine** — Une giberne de cuir posée sur une chaise, pleine de petits souvenirs. (énigme e1-2)
- en haut à droite : **Les lettres du bureau** — Un bureau couvert de lettres et de bulletins, près de la fenêtre. (énigme e1-3)
- au centre : **Les cartes de campagne** — Des cartes d'Italie et d'Égypte épinglées au mur, avec des épingles de couleur. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Une antichambre du palais des Tuileries, à Paris, en 1800. Une antichambre aux boiseries claires, des cartes d'Italie et d'Égypte épinglées au mur, un pupitre avec un carnet de campagne, une giberne de soldat posée sur une chaise et un bureau couvert de lettres. Quatre objets bien éclairés, nettement séparés et lisibles : Le carnet de campagne (en haut à gauche); La giberne d'Antoine (en haut au centre); Les lettres du bureau (en haut à droite); Les cartes de campagne (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16223a et #2f4a7a, lumières et accents #c9a24a, #f2e3c2, touches #d9e2ef.
```

### 2. Notre-Dame de Paris — `notre-dame`

**Lieu** : La cathédrale Notre-Dame de Paris, le 2 décembre 1804. La nef de Notre-Dame décorée de tentures rouges et or, des tribunes pleines d'invités, un autel illuminé, et dans un coin, la table de travail de la brodeuse avec du fil d'or, un registre et des motifs d'abeilles.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le registre de l'atelier** — Un registre ouvert sur la table de la brodeuse, taché d'encre. (énigme e2-1)
- en haut au centre : **Le grand tableau** — Un schéma du grand tableau de David, punaisé près de l'autel. (énigme e2-2)
- en haut à droite : **Les motifs de broderie** — Un carton de motifs brodés de fil d'or, posé sur la table de Rose. (énigme e2-3)
- au centre : **Le chemin de la couronne** — Une bande de tapis rouge déroulée vers l'autel, marquée de cinq étapes. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La cathédrale Notre-Dame de Paris, le 2 décembre 1804. La nef de Notre-Dame décorée de tentures rouges et or, des tribunes pleines d'invités, un autel illuminé, et dans un coin, la table de travail de la brodeuse avec du fil d'or, un registre et des motifs d'abeilles. Quatre objets bien éclairés, nettement séparés et lisibles : Le registre de l'atelier (en haut à gauche); Le grand tableau (en haut au centre); Les motifs de broderie (en haut à droite); Le chemin de la couronne (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16223a et #2f4a7a, lumières et accents #c9a24a, #f2e3c2, touches #d9e2ef.
```

### 3. Le bivouac — `bivouac`

**Lieu** : Le bivouac de la Grande Armée, au fil des campagnes de 1805 à 1815. Une tente de toile éclairée par une lanterne, une carte de l'Europe sur une table pliante, une malle cadenassée, la gourde et le tonnelet de la cantinière, et dehors, le feu de camp.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La carte de l'Europe** — Une carte de l'Europe couverte de traits, sur la table pliante de la tente. (énigme e3-1)
- en haut au centre : **Le carnet de route** — Un carnet de route rangé dans la poche du tablier de la cantinière. (énigme e3-2)
- en haut à droite : **Le feu de camp** — Un feu de camp devant la tente, entouré de jeunes soldats. (énigme e3-3)
- au centre : **La malle cadenassée** — Une malle de bois fermée par un cadenas à rouleaux, au fond de la tente. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le bivouac de la Grande Armée, au fil des campagnes de 1805 à 1815. Une tente de toile éclairée par une lanterne, une carte de l'Europe sur une table pliante, une malle cadenassée, la gourde et le tonnelet de la cantinière, et dehors, le feu de camp. Quatre objets bien éclairés, nettement séparés et lisibles : La carte de l'Europe (en haut à gauche); Le carnet de route (en haut au centre); Le feu de camp (en haut à droite); La malle cadenassée (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16223a et #2f4a7a, lumières et accents #c9a24a, #f2e3c2, touches #d9e2ef.
```

### 4. Le dôme des Invalides — `invalides`

**Lieu** : Le dôme des Invalides et les réserves du musée de l'Armée, aujourd'hui. Sous la grande coupole dorée, la crypte du tombeau ; à côté, une salle d'exposition en préparation avec des vitrines, des cartels, des panneaux et une boîte de fiches.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les cartels de l'exposition** — Une pile de cartels, de petites étiquettes de musée, sur un chariot. (énigme e4-1)
- en haut au centre : **La vitrine des créations** — Une vitrine éclairée avec des objets et des documents de l'Empire. (énigme e4-2)
- en haut à droite : **Les panneaux de l'exposition** — Deux grands panneaux vides, côte à côte, près de la crypte. (énigme e4-3)
- au centre : **La boîte de fiches** — Une boîte de fiches cartonnées dans les réserves du musée. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le dôme des Invalides et les réserves du musée de l'Armée, aujourd'hui. Sous la grande coupole dorée, la crypte du tombeau ; à côté, une salle d'exposition en préparation avec des vitrines, des cartels, des panneaux et une boîte de fiches. Quatre objets bien éclairés, nettement séparés et lisibles : Les cartels de l'exposition (en haut à gauche); La vitrine des créations (en haut au centre); Les panneaux de l'exposition (en haut à droite); La boîte de fiches (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16223a et #2f4a7a, lumières et accents #c9a24a, #f2e3c2, touches #d9e2ef.
```

### 5. La mairie — `mairie`

**Lieu** : La salle des mariages d'une mairie de Bourgogne, aujourd'hui. Une salle des mariages lumineuse, un buste de Marianne, un drapeau tricolore, une écharpe tricolore posée sur la table, une urne de vote rangée dans un coin et le coffre du testament.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le placard de la mairie** — Un vieux placard ouvert, plein d'objets de toutes les époques. (énigme e5-1)
- en haut au centre : **Le livret d'accueil** — Un livret d'accueil de la mairie posé près du buste de Marianne. (énigme e5-2)
- en haut à droite : **Le plan de la place** — Un plan de la place de la commune, dessiné à la main, sur la table. (énigme e5-3)
- au centre : **Le coffre du testament** — Le coffre de voyage des Invalides, posé sur la table des mariages. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle des mariages d'une mairie de Bourgogne, aujourd'hui. Une salle des mariages lumineuse, un buste de Marianne, un drapeau tricolore, une écharpe tricolore posée sur la table, une urne de vote rangée dans un coin et le coffre du testament. Quatre objets bien éclairés, nettement séparés et lisibles : Le placard de la mairie (en haut à gauche); Le livret d'accueil (en haut au centre); Le plan de la place (en haut à droite); Le coffre du testament (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #16223a et #2f4a7a, lumières et accents #c9a24a, #f2e3c2, touches #d9e2ef.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Antoine — `antoine`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Grenadier de la garde, ancien soldat de l'armée d'Italie, genre : homme, cheveux courts, expression : grenadier franc et fier, ancien soldat d'italie, admiratif du général mais lucide sur le prix des batailles. Tenue en rapport avec son rôle (Grenadier de la garde, ancien soldat de l'armée d'Italie). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin.
```

### Rose — `rose`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Brodeuse du manteau du sacre, genre : femme, cheveux longs, expression : brodeuse minutieuse et émerveillée, attentive aux détails des symboles. Tenue en rapport avec son rôle (Brodeuse du manteau du sacre). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin.
```

### Jeanne — `jeanne`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Cantinière de la Grande Armée, genre : femme, cheveux courts, expression : cantinière chaleureuse et grave, qui a vu la gloire et la souffrance des soldats. Tenue en rapport avec son rôle (Cantinière de la Grande Armée). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin.
```

### Hugo — `hugo`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Conservateur au musée de l'Armée, aux Invalides, genre : homme, cheveux courts, porte des lunettes, expression : conservateur de musée posé et honnête, qui veut tout montrer, l'héritage comme la part d'ombre. Tenue en rapport avec son rôle (Conservateur au musée de l'Armée, aux Invalides). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin.
```

### Inès — `ines`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Maire d'une commune de Bourgogne, genre : femme, cheveux longs, expression : maire accueillante et pédagogue, fière des symboles de la république. Tenue en rapport avec son rôle (Maire d'une commune de Bourgogne). Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, aucune inscription lisible, grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `tuileries`) : « Lent travelling avant dans Une antichambre du palais des Tuileries, à Paris, en 1800. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `notre-dame`) : « Lent travelling avant dans La cathédrale Notre-Dame de Paris, le 2 décembre 1804. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `bivouac`) : « Lent travelling avant dans Le bivouac de la Grande Armée, au fil des campagnes de 1805 à 1815. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `invalides`) : « Lent travelling avant dans Le dôme des Invalides et les réserves du musée de l'Armée, aujourd'hui. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `mairie`) : « Lent travelling avant dans La salle des mariages d'une mairie de Bourgogne, aujourd'hui. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/tuileries.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « Une antichambre du palais des Tuileries, à Paris, en 1800 », sans voix ni musique |
| `assets/audio/ambiances/notre-dame.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « La cathédrale Notre-Dame de Paris, le 2 décembre 1804 », sans voix ni musique |
| `assets/audio/ambiances/bivouac.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « Le bivouac de la Grande Armée, au fil des campagnes de 1805 à 1815 », sans voix ni musique |
| `assets/audio/ambiances/invalides.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « Le dôme des Invalides et les réserves du musée de l'Armée, aujourd'hui », sans voix ni musique |
| `assets/audio/ambiances/mairie.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « La salle des mariages d'une mairie de Bourgogne, aujourd'hui », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
