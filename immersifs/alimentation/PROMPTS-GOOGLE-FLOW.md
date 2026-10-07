# Prompts Google Flow — Le Grand Repas du chef

Ces prompts produisent les images du jeu `immersifs/alimentation/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ. Univers contemporain, un restaurant de campagne, « Le Grand Couvert », et une équipe cycliste en préparation d'étape. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0e1a12 et #1f3326, lumières et accents #e8803a, #ffd08a, touches #bde6a8.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La cour du potager et du poulailler — `potager`

**Lieu** : La cour du restaurant, entre le potager et le poulailler. Des rangs de salades et de carottes, un poulailler en bois, des poules qui picorent. Dans un coin, sous une lampe, le petit Caramel trottine.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le carnet du poulailler** — Un carnet où Nathan note la masse et la taille de ses poussins. (énigme e1-1)
- en haut au centre : **Le panier du potager** — Légumes et œufs : la matière qui nourrit les êtres vivants vient de là. (énigme e1-2)
- en haut à droite : **La toise de la cuisine** — Une toise gravée sur le montant de la porte : on y mesure la taille des petits. (énigme e1-3)
- au centre : **Le mot de Nathan** — Un mot griffonné où manquent des termes. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La cour du restaurant, entre le potager et le poulailler. Des rangs de salades et de carottes, un poulailler en bois, des poules qui picorent. Dans un coin, sous une lampe, le petit Caramel trottine. Quatre objets bien éclairés, nettement séparés et lisibles : Le carnet du poulailler (en haut à gauche); Le panier du potager (en haut au centre); La toise de la cuisine (en haut à droite); Le mot de Nathan (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0e1a12 et #1f3326, lumières et accents #e8803a, #ffd08a, touches #bde6a8.
```

### 2. La salle des menus — `menus`

**Lieu** : La salle des menus, au premier étage du restaurant. Un grand tableau couvert de menus, des fiches épinglées, une balance de cuisine. Sur la table, le carnet de la docteure et le maillot de Basile.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les assiettes de la salle des menus** — Des assiettes très différentes : peu ou beaucoup d'énergie. (énigme e2-1)
- en haut au centre : **Le tableau des besoins** — Un grand tableau où les besoins en énergie sont classés. (énigme e2-2)
- en haut à droite : **Le plat qui tombe** — Une assiette qui n'a rien à voir avec les autres. (énigme e2-3)
- au centre : **Le carnet de la docteure** — Les notes d'Inès sur ce qui fait varier ce dont on a besoin. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle des menus, au premier étage du restaurant. Un grand tableau couvert de menus, des fiches épinglées, une balance de cuisine. Sur la table, le carnet de la docteure et le maillot de Basile. Quatre objets bien éclairés, nettement séparés et lisibles : Les assiettes de la salle des menus (en haut à gauche); Le tableau des besoins (en haut au centre); Le plat qui tombe (en haut à droite); Le carnet de la docteure (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0e1a12 et #1f3326, lumières et accents #e8803a, #ffd08a, touches #bde6a8.
```

### 3. La table de dégustation — `degustation`

**Lieu** : La table de dégustation, près des cuisines. Une longue table nappée de blanc : du pain de campagne, des pommes, des carottes croquantes. Sur une étagère, le moulage d'une mâchoire prêté par un dentiste.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les outils de cuisine** — Couteau, pilon, mixeur : chaque outil a sa tâche, comme chaque dent. (énigme e3-1)
- en haut au centre : **Le moulage de la mâchoire** — Un moulage de mâchoire en plâtre posé sur la table. (énigme e3-2)
- en haut à droite : **Le verre d'eau et la bouchée** — Une bouchée de pain qui se ramollit : le liquide de la bouche agit. (énigme e3-3)
- au centre : **La bouchée de pain** — Un morceau de pain à suivre dans la bouche. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La table de dégustation, près des cuisines. Une longue table nappée de blanc : du pain de campagne, des pommes, des carottes croquantes. Sur une étagère, le moulage d'une mâchoire prêté par un dentiste. Quatre objets bien éclairés, nettement séparés et lisibles : Les outils de cuisine (en haut à gauche); Le moulage de la mâchoire (en haut au centre); Le verre d'eau et la bouchée (en haut à droite); La bouchée de pain (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0e1a12 et #1f3326, lumières et accents #e8803a, #ffd08a, touches #bde6a8.
```

### 4. Le cabinet du Grand Tunnel — `cabinet`

**Lieu** : Le cabinet de la docteure Inès, à côté de la salle d'entraînement. Sur le bureau, une grande maquette du corps humain que l'on peut ouvrir. Au mur, des affiches sur la digestion. Une bouchée en pâte à modeler attend au départ du Grand Tunnel.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La maquette du corps** — Une maquette où l'on place le tube digestif. (énigme e4-1)
- en haut au centre : **Les cartes des organes** — Des cartes à associer : estomac, intestin grêle, gros intestin. (énigme e4-2)
- en haut à droite : **Les fiches de la docteure** — Des affirmations à vérifier : vrai ou faux ? (énigme e4-3)
- au centre : **L'organe qui ne voit rien** — Un organe qui n'est pas dans le tube digestif. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le cabinet de la docteure Inès, à côté de la salle d'entraînement. Sur le bureau, une grande maquette du corps humain que l'on peut ouvrir. Au mur, des affiches sur la digestion. Une bouchée en pâte à modeler attend au départ du Grand Tunnel. Quatre objets bien éclairés, nettement séparés et lisibles : La maquette du corps (en haut à gauche); Les cartes des organes (en haut au centre); Les fiches de la docteure (en haut à droite); L'organe qui ne voit rien (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0e1a12 et #1f3326, lumières et accents #e8803a, #ffd08a, touches #bde6a8.
```

### 5. La salle d'entraînement — `entrainement`

**Lieu** : La salle d'entraînement, au fond du restaurant. Un vélo de course monté sur un home-trainer, un écran qui affiche la vitesse et le pouls, une gourde d'eau. Basile pédale, les joues rouges.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le compteur de pouls** — Un compteur qui bat au rythme du cœur du coureur. (énigme e5-1)
- en haut au centre : **Le message du home-trainer** — Un message affiché sur l'écran du home-trainer. (énigme e5-2)
- en haut à droite : **Les chronos du coureur** — Des relevés de pouls : vite ou lentement ? (énigme e5-3)
- au centre : **Le schéma de la livraison** — Un schéma où le sang livre l'oxygène aux muscles. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle d'entraînement, au fond du restaurant. Un vélo de course monté sur un home-trainer, un écran qui affiche la vitesse et le pouls, une gourde d'eau. Basile pédale, les joues rouges. Quatre objets bien éclairés, nettement séparés et lisibles : Le compteur de pouls (en haut à gauche); Le message du home-trainer (en haut au centre); Les chronos du coureur (en haut à droite); Le schéma de la livraison (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0e1a12 et #1f3326, lumières et accents #e8803a, #ffd08a, touches #bde6a8.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Rosalie — `rosalie`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Cheffe du restaurant Le Grand Couvert, genre : femme, cheveux courts, expression : cheffe exigeante, chaleureuse, parle cuisine. Tenue en rapport avec son rôle (Cheffe du restaurant Le Grand Couvert). Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ.
```

### Nathan — `nathan`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Commis : il s'occupe du potager et du poulailler, genre : garçon, cheveux courts, expression : jeune commis enthousiaste, les mains dans la terre. Tenue en rapport avec son rôle (Commis : il s'occupe du potager et du poulailler). Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ.
```

### Docteure Inès — `ines`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Médecin de l'équipe cycliste, genre : femme, cheveux longs, porte des lunettes, expression : médecin calme et précise, pédagogue. Tenue en rapport avec son rôle (Médecin de l'équipe cycliste). Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ.
```

### Basile — `basile`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Coureur cycliste, genre : homme, cheveux courts, expression : coureur essoufflé, plein d'humour et d'énergie. Tenue en rapport avec son rôle (Coureur cycliste). Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `potager`) : « Lent travelling avant dans La cour du restaurant, entre le potager et le poulailler. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `menus`) : « Lent travelling avant dans La salle des menus, au premier étage du restaurant. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `degustation`) : « Lent travelling avant dans La table de dégustation, près des cuisines. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `cabinet`) : « Lent travelling avant dans Le cabinet de la docteure Inès, à côté de la salle d'entraînement. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `entrainement`) : « Lent travelling avant dans La salle d'entraînement, au fond du restaurant. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.
