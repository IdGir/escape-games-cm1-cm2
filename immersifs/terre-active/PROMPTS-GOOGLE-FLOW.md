# Prompts Google Flow — L'Observatoire des volcans

Ces prompts produisent les images du jeu `immersifs/terre-active/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin. Univers contemporain : la station d'observation des Hauts (inventée) au-dessus du village inventé de Bois-Clair, sur l'île de La Réunion : galerie d'exposition, salle des cartes, sentier au bord de l'enclos du cratère, salle des sismographes, centre de secours. Aucune personne réelle, aucune catastrophe montrée. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #141a22 et #1f4e79, lumières et accents #e8873a, #fbe0c2, touches #d4e6f1.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La galerie de la Terre — `galerie`

**Lieu** : La galerie d'exposition de la station d'observation des Hauts. Une grande salle avec une maquette de la Terre coupée en deux, des panneaux tombés au sol, des vitrines de roches volcaniques et une baie vitrée qui donne sur le volcan.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les panneaux renversés** — Des panneaux d'exposition tombés au sol, avec des photos de volcans, de tempêtes et de falaises. (énigme e1-1)
- en haut au centre : **La maquette de la Terre** — Une grande demi-sphère coupée, avec des couches de couleurs et des étiquettes tombées. (énigme e1-2)
- en haut à droite : **La borne du quiz** — Une borne à écran où défilent les questions du quiz des visiteurs. (énigme e1-3)
- au centre : **La frise du voyage** — Une longue bande qui descend du plafond au sol, de la surface jusqu'au centre de la Terre. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La galerie d'exposition de la station d'observation des Hauts. Une grande salle avec une maquette de la Terre coupée en deux, des panneaux tombés au sol, des vitrines de roches volcaniques et une baie vitrée qui donne sur le volcan. Quatre objets bien éclairés, nettement séparés et lisibles : Les panneaux renversés (en haut à gauche); La maquette de la Terre (en haut au centre); La borne du quiz (en haut à droite); La frise du voyage (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #141a22 et #1f4e79, lumières et accents #e8873a, #fbe0c2, touches #d4e6f1.
```

### 2. La salle des cartes — `cartes`

**Lieu** : La salle des cartes de la station. Un grand planisphère au mur, des punaises tombées, une table avec une maquette de plaques en polystyrène sur de la pâte à modeler, et des rouleaux de cartes.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La maquette des plaques** — Deux plaques de polystyrène posées sur de la pâte à modeler, avec un petit volcan en carton. (énigme e2-1)
- en haut au centre : **Les fiches de Noé** — Un paquet de fiches cartonnées éparpillées sur la table, certaines à l'envers. (énigme e2-2)
- en haut à droite : **Le panneau d'explication** — Un panneau à flèches à côté de la maquette : « ce que vous voyez » et « ce que cela représente ». (énigme e2-3)
- au centre : **Le planisphère** — Un grand planisphère au mur, des punaises rouges et vertes tombées au pied du mur. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle des cartes de la station. Un grand planisphère au mur, des punaises tombées, une table avec une maquette de plaques en polystyrène sur de la pâte à modeler, et des rouleaux de cartes. Quatre objets bien éclairés, nettement séparés et lisibles : La maquette des plaques (en haut à gauche); Les fiches de Noé (en haut au centre); Le panneau d'explication (en haut à droite); Le planisphère (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #141a22 et #1f4e79, lumières et accents #e8873a, #fbe0c2, touches #d4e6f1.
```

### 3. Le sentier du cratère — `cratere`

**Lieu** : Le sentier d'observation au bord de l'enclos du cratère. Un sentier balisé sur une ancienne coulée de lave noire, une table d'orientation, des capteurs sur trépied, et au loin le cratère d'où monte une fine fumée.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le carnet de Maëva** — Un carnet ouvert sur un rocher, avec le dessin d'un volcan en coupe. (énigme e3-1)
- en haut au centre : **La table d'orientation** — Une table d'orientation en pierre, avec des cartes d'étapes posées dessus en désordre. (énigme e3-2)
- en haut à droite : **La boîte d'échantillons** — Une boîte à compartiments avec des morceaux de lave, de la cendre et des fiches tombées. (énigme e3-3)
- au centre : **Les capteurs du sentier** — Des capteurs gris sur trépied, avec un petit écran qui compare deux éruptions. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le sentier d'observation au bord de l'enclos du cratère. Un sentier balisé sur une ancienne coulée de lave noire, une table d'orientation, des capteurs sur trépied, et au loin le cratère d'où monte une fine fumée. Quatre objets bien éclairés, nettement séparés et lisibles : Le carnet de Maëva (en haut à gauche); La table d'orientation (en haut au centre); La boîte d'échantillons (en haut à droite); Les capteurs du sentier (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #141a22 et #1f4e79, lumières et accents #e8873a, #fbe0c2, touches #d4e6f1.
```

### 4. La salle des sismographes — `sismographes`

**Lieu** : La salle des sismographes de la station. Des écrans qui affichent des tracés en zigzag, un vieux sismographe à tambour, un grand tableau avec un schéma de séisme et des tiroirs d'étiquettes ouverts.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les tiroirs d'étiquettes** — Des tiroirs ouverts pleins d'étiquettes de mots : foyer, épicentre, magnitude. (énigme e4-1)
- en haut au centre : **Le grand tableau** — Un tableau blanc avec le schéma d'un séisme en coupe, sans légende. (énigme e4-2)
- en haut à droite : **Le téléphone de l'observatoire** — Un téléphone avec une liste de questions notées par les habitants de Bois-Clair. (énigme e4-3)
- au centre : **Le panneau de la plage** — Un panneau de consignes à moitié rédigé, avec des mots manquants. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle des sismographes de la station. Des écrans qui affichent des tracés en zigzag, un vieux sismographe à tambour, un grand tableau avec un schéma de séisme et des tiroirs d'étiquettes ouverts. Quatre objets bien éclairés, nettement séparés et lisibles : Les tiroirs d'étiquettes (en haut à gauche); Le grand tableau (en haut au centre); Le téléphone de l'observatoire (en haut à droite); Le panneau de la plage (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #141a22 et #1f4e79, lumières et accents #e8873a, #fbe0c2, touches #d4e6f1.
```

### 5. Le centre de secours — `secours`

**Lieu** : Le centre de secours des sapeurs-pompiers de Bois-Clair. Un bureau avec la carte des risques du village, des affiches de consignes, un poste de radio, des casques rangés, et un ordinateur où attend le message d'information verrouillé.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **L'affiche des réflexes** — Une grande affiche vierge avec des vignettes de gestes posées à côté. (énigme e5-1)
- en haut au centre : **La carte des risques** — La carte des risques du village épinglée au mur, avec trois zones de couleur. (énigme e5-2)
- en haut à droite : **La fiche de l'exercice** — Une fiche « exercice séisme » avec des étapes découpées, posée près du poste de radio. (énigme e5-3)
- au centre : **Le message verrouillé** — Un ordinateur dont l'écran affiche un message d'information verrouillé par trois nombres. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le centre de secours des sapeurs-pompiers de Bois-Clair. Un bureau avec la carte des risques du village, des affiches de consignes, un poste de radio, des casques rangés, et un ordinateur où attend le message d'information verrouillé. Quatre objets bien éclairés, nettement séparés et lisibles : L'affiche des réflexes (en haut à gauche); La carte des risques (en haut au centre); La fiche de l'exercice (en haut à droite); Le message verrouillé (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #141a22 et #1f4e79, lumières et accents #e8873a, #fbe0c2, touches #d4e6f1.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Inès — `ines`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Géologue, responsable de la galerie de la station, genre : femme, cheveux longs, porte des lunettes, expression : géologue posée et chaleureuse, aime les maquettes et les comparaisons simples, rassure les visiteurs. Tenue en rapport avec son rôle (Géologue, responsable de la galerie de la station). Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin.
```

### Noé — `noe`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Géophysicien, spécialiste des plaques, genre : homme, cheveux courts, expression : géophysicien enthousiaste, parle des plaques comme d'un grand puzzle, aime faire manipuler. Tenue en rapport avec son rôle (Géophysicien, spécialiste des plaques). Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin.
```

### Maëva — `maeva`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Volcanologue, née à La Réunion, genre : femme, cheveux longs, expression : volcanologue réunionnaise, fière de son île, calme et précise, rappelle toujours les règles de sécurité. Tenue en rapport avec son rôle (Volcanologue, née à La Réunion). Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin.
```

### Samuel — `samuel`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Sismologue, né en Guadeloupe, genre : homme, cheveux courts, porte des lunettes, expression : sismologue guadeloupéen, méthodique, rigoureux sur les mots, jamais alarmiste. Tenue en rapport avec son rôle (Sismologue, né en Guadeloupe). Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin.
```

### Adèle — `adele`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Lieutenante de sapeurs-pompiers du centre de secours de Bois-Clair, genre : femme, cheveux courts, expression : lieutenante de sapeurs-pompiers énergique et bienveillante, répète que l'on sait se préparer. Tenue en rapport avec son rôle (Lieutenante de sapeurs-pompiers du centre de secours de Bois-Clair). Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `galerie`) : « Lent travelling avant dans La galerie d'exposition de la station d'observation des Hauts. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `cartes`) : « Lent travelling avant dans La salle des cartes de la station. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `cratere`) : « Lent travelling avant dans Le sentier d'observation au bord de l'enclos du cratère. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `sismographes`) : « Lent travelling avant dans La salle des sismographes de la station. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `secours`) : « Lent travelling avant dans Le centre de secours des sapeurs-pompiers de Bois-Clair. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/galerie.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « La galerie d'exposition de la station d'observation des Hauts », sans voix ni musique |
| `assets/audio/ambiances/cartes.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « La salle des cartes de la station », sans voix ni musique |
| `assets/audio/ambiances/cratere.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « Le sentier d'observation au bord de l'enclos du cratère », sans voix ni musique |
| `assets/audio/ambiances/sismographes.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « La salle des sismographes de la station », sans voix ni musique |
| `assets/audio/ambiances/secours.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « Le centre de secours des sapeurs-pompiers de Bois-Clair », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
