# Prompts Google Flow — La Centrale en panne

Ces prompts produisent les images du jeu `immersifs/electricite/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin. Univers contemporain : la centrale et la petite ville inventée de Clairval, plongées dans le noir après un orage. Aucune expérience avec le secteur, aucune personne électrisée montrée, aucune personne réelle. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0d1b2a et #1f4e79, lumières et accents #f2c230, #ffe9a0, touches #cfe6f3.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. L'atelier du club sciences — `atelier`

**Lieu** : L'atelier du club sciences, au rez-de-chaussée de la centrale. Une petite salle éclairée par une lampe torche. Sur la table, des piles plates, des lampes sur leurs douilles, des fils à pinces et un interrupteur. La lampe de secours du couloir est éteinte.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le montage de Nour** — Sur la table, une pile plate, une lampe sur sa douille, un interrupteur et des fils à pinces. (énigme e1-1)
- en haut au centre : **Le cahier d'expériences** — Un cahier ouvert, couvert de croquis de montages et de flèches. (énigme e1-2)
- en haut à droite : **Les essais ratés** — Des montages défaits, alignés sur une étagère, chacun avec une étiquette. (énigme e1-3)
- au centre : **La fiche du club** — Une feuille vierge épinglée au mur : « Fiche de montage du club ». (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : L'atelier du club sciences, au rez-de-chaussée de la centrale. Une petite salle éclairée par une lampe torche. Sur la table, des piles plates, des lampes sur leurs douilles, des fils à pinces et un interrupteur. La lampe de secours du couloir est éteinte. Quatre objets bien éclairés, nettement séparés et lisibles : Le montage de Nour (en haut à gauche); Le cahier d'expériences (en haut au centre); Les essais ratés (en haut à droite); La fiche du club (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0d1b2a et #1f4e79, lumières et accents #f2c230, #ffe9a0, touches #cfe6f3.
```

### 2. Le magasin de matériel — `magasin`

**Lieu** : Le magasin de matériel électrique. Des étagères pleines de bobines de fil, de boîtes de vis, de gants et d'outils. Un bac de pièces renversé par l'orage. Sur l'établi, un circuit testeur.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le bac renversé** — Un bac en plastique renversé : clés, gommes, vis, bouchons et trombones mêlés. (énigme e2-1)
- en haut au centre : **La boîte des métaux** — Une boîte en métal étiquetée « Conducteurs ». (énigme e2-2)
- en haut à droite : **Les bobines de fil** — Des bobines de fil de cuivre gainé de plastique, de toutes les couleurs. (énigme e2-3)
- au centre : **La notice du testeur** — Une notice plastifiée, tachée d'eau, accrochée à l'établi. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le magasin de matériel électrique. Des étagères pleines de bobines de fil, de boîtes de vis, de gants et d'outils. Un bac de pièces renversé par l'orage. Sur l'établi, un circuit testeur. Quatre objets bien éclairés, nettement séparés et lisibles : Le bac renversé (en haut à gauche); La boîte des métaux (en haut au centre); Les bobines de fil (en haut à droite); La notice du testeur (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0d1b2a et #1f4e79, lumières et accents #f2c230, #ffe9a0, touches #cfe6f3.
```

### 3. La salle de contrôle — `controle`

**Lieu** : La salle de contrôle de la centrale. Un grand pupitre couvert de boutons éteints. Au mur, un tableau où sont dessinés des schémas. Des feuilles de plans tombées par terre.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La légende du tableau** — Un grand tableau mural couvert de symboles ; la légende est effacée. (énigme e3-1)
- en haut au centre : **Le schéma du pupitre** — Un schéma dessiné sur le pupitre, à côté des voyants éteints. (énigme e3-2)
- en haut à droite : **Les voyants** — Une rangée de voyants verts et rouges au-dessus du schéma. (énigme e3-3)
- au centre : **Le trajet du courant** — Une baguette lumineuse posée sur le schéma. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La salle de contrôle de la centrale. Un grand pupitre couvert de boutons éteints. Au mur, un tableau où sont dessinés des schémas. Des feuilles de plans tombées par terre. Quatre objets bien éclairés, nettement séparés et lisibles : La légende du tableau (en haut à gauche); Le schéma du pupitre (en haut au centre); Les voyants (en haut à droite); Le trajet du courant (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0d1b2a et #1f4e79, lumières et accents #f2c230, #ffe9a0, touches #cfe6f3.
```

### 4. La maison témoin — `maison`

**Lieu** : La maison témoin, dans le hall des visites. Une petite maison en bois grandeur nature, montée dans le hall : une cuisine, une salle de bain, un salon, un tableau électrique avec son disjoncteur. Des affiches de prévention sont tombées au sol.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le tableau électrique** — Le tableau électrique de la maison témoin, avec son disjoncteur. (énigme e4-1)
- en haut au centre : **Les affiches tombées** — Des affiches de prévention éparpillées sur le sol du salon. (énigme e4-2)
- en haut à droite : **Le tableau des idées reçues** — Un tableau blanc couvert de phrases écrites par les visiteurs. (énigme e4-3)
- au centre : **La visite des pièces** — Les portes de la cuisine, de la salle de bain et du salon de la maison témoin. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La maison témoin, dans le hall des visites. Une petite maison en bois grandeur nature, montée dans le hall : une cuisine, une salle de bain, un salon, un tableau électrique avec son disjoncteur. Des affiches de prévention sont tombées au sol. Quatre objets bien éclairés, nettement séparés et lisibles : Le tableau électrique (en haut à gauche); Les affiches tombées (en haut au centre); Le tableau des idées reçues (en haut à droite); La visite des pièces (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0d1b2a et #1f4e79, lumières et accents #f2c230, #ffe9a0, touches #cfe6f3.
```

### 5. Le poste de conduite du réseau — `reseau`

**Lieu** : Le poste de conduite du réseau. Une salle sombre avec une grande carte lumineuse de la vallée : la centrale, les lignes, les postes et les quatre quartiers de Clairval, tous éteints. Devant la carte, le pupitre de reconnexion.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La carte lumineuse** — Une grande carte de la vallée : la centrale, les pylônes, les postes et la ville. (énigme e5-1)
- en haut au centre : **Les centrales de la vallée** — Des pions lumineux sur la carte : barrage, éoliennes, panneaux solaires, centrales. (énigme e5-2)
- en haut à droite : **Le pupitre de reconnexion** — Quatre leviers, un par quartier, sous quatre cadrans à chiffres. (énigme e5-3)
- au centre : **Le carnet de Karim** — Un petit carnet mouillé, ouvert sur la table de conduite. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le poste de conduite du réseau. Une salle sombre avec une grande carte lumineuse de la vallée : la centrale, les lignes, les postes et les quatre quartiers de Clairval, tous éteints. Devant la carte, le pupitre de reconnexion. Quatre objets bien éclairés, nettement séparés et lisibles : La carte lumineuse (en haut à gauche); Les centrales de la vallée (en haut au centre); Le pupitre de reconnexion (en haut à droite); Le carnet de Karim (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0d1b2a et #1f4e79, lumières et accents #f2c230, #ffe9a0, touches #cfe6f3.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Nour — `nour`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Élève du club sciences de la centrale, genre : femme, cheveux longs, expression : élève curieuse et têtue, fait des essais, n'aime pas qu'une lampe refuse de s'allumer. Tenue en rapport avec son rôle (Élève du club sciences de la centrale). Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin.
```

### Maëlle — `maelle`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Magasinière du matériel électrique, genre : femme, cheveux courts, porte des lunettes, expression : magasinière pratique et rapide, aime que tout soit rangé à sa place, insiste sur la protection. Tenue en rapport avec son rôle (Magasinière du matériel électrique). Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin.
```

### Hélène — `helene`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Ingénieure de la centrale, genre : femme, cheveux longs, porte des lunettes, expression : ingénieure posée et rassurante, explique avec des mots exacts, rappelle la règle des piles. Tenue en rapport avec son rôle (Ingénieure de la centrale). Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin.
```

### Marius — `marius`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Électricien de la ville, genre : homme, cheveux courts, expression : électricien ferme et bienveillant, ne plaisante jamais avec la sécurité. Tenue en rapport avec son rôle (Électricien de la ville). Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin.
```

### Karim — `karim`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Technicien du réseau, genre : homme, cheveux courts, expression : technicien du réseau calme sous pression, pense à toute la ville, aime les chiffres justes. Tenue en rapport avec son rôle (Technicien du réseau). Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `atelier`) : « Lent travelling avant dans L'atelier du club sciences, au rez-de-chaussée de la centrale. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `magasin`) : « Lent travelling avant dans Le magasin de matériel électrique. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `controle`) : « Lent travelling avant dans La salle de contrôle de la centrale. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `maison`) : « Lent travelling avant dans La maison témoin, dans le hall des visites. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `reseau`) : « Lent travelling avant dans Le poste de conduite du réseau. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/atelier.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « L'atelier du club sciences, au rez-de-chaussée de la centrale », sans voix ni musique |
| `assets/audio/ambiances/magasin.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « Le magasin de matériel électrique », sans voix ni musique |
| `assets/audio/ambiances/controle.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « La salle de contrôle de la centrale », sans voix ni musique |
| `assets/audio/ambiances/maison.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « La maison témoin, dans le hall des visites », sans voix ni musique |
| `assets/audio/ambiances/reseau.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « Le poste de conduite du réseau », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
