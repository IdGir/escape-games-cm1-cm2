# Prompts Google Flow — La Nurserie du zoo

Ces prompts produisent les images du jeu `immersifs/naissances-animaux/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin. Univers contemporain : le zoo inventé des Trois-Sources, sa nurserie, sa mare, sa galerie et sa ferme. Aucune scène de naissance ni de mise bas, aucun animal blessé, aucune personne réelle. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1c2b1a et #3f6b3a, lumières et accents #e9b949, #fbe7b0, touches #d3ebf2.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. Le laboratoire de la vétérinaire — `laboratoire`

**Lieu** : Le laboratoire de la vétérinaire, à côté de la nurserie. Une salle blanche avec un microscope, des bocaux étiquetés et un tableau couvert de dessins de cellules. Une fenêtre bat encore au vent.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le schéma d'Inès** — Au tableau blanc, un dessin de cellules dont les étiquettes sont tombées au sol. (énigme e1-1)
- en haut au centre : **Les fiches du stagiaire** — Une pile de fiches recopiées à la main, posée près du microscope. (énigme e1-2)
- en haut à droite : **L'armoire aux bocaux** — Une armoire vitrée remplie de bocaux dont les étiquettes ont glissé. (énigme e1-3)
- au centre : **L'affiche des visiteurs** — Une grande affiche en morceaux, posée sur la paillasse. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le laboratoire de la vétérinaire, à côté de la nurserie. Une salle blanche avec un microscope, des bocaux étiquetés et un tableau couvert de dessins de cellules. Une fenêtre bat encore au vent. Quatre objets bien éclairés, nettement séparés et lisibles : Le schéma d'Inès (en haut à gauche); Les fiches du stagiaire (en haut au centre); L'armoire aux bocaux (en haut à droite); L'affiche des visiteurs (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1c2b1a et #3f6b3a, lumières et accents #e9b949, #fbe7b0, touches #d3ebf2.
```

### 2. L'aquarium et la mare — `aquarium`

**Lieu** : L'aquarium et la mare pédagogique. De grands bassins éclairés en bleu, une mare avec des pontes de grenouille accrochées aux plantes. Les fiches des animaux flottent sur l'eau.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les fiches flottantes** — Des fiches plastifiées qui flottent à la surface du grand bassin. (énigme e2-1)
- en haut au centre : **La vitre de l'aquarium** — Une grande vitre derrière laquelle nagent des truites argentées. (énigme e2-2)
- en haut à droite : **Le panneau de la mare** — Un panneau en bois au bord de la mare, couvert d'éclaboussures. (énigme e2-3)
- au centre : **Le grand bassin** — Le grand bassin et ses quatre fiches accrochées à la rambarde. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : L'aquarium et la mare pédagogique. De grands bassins éclairés en bleu, une mare avec des pontes de grenouille accrochées aux plantes. Les fiches des animaux flottent sur l'eau. Quatre objets bien éclairés, nettement séparés et lisibles : Les fiches flottantes (en haut à gauche); La vitre de l'aquarium (en haut au centre); Le panneau de la mare (en haut à droite); Le grand bassin (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1c2b1a et #3f6b3a, lumières et accents #e9b949, #fbe7b0, touches #d3ebf2.
```

### 3. La galerie des surprises — `galerie`

**Lieu** : La galerie des animaux étonnants. Un long couloir de vitrines : des œufs de toutes les tailles, une capsule de roussette, des panneaux sur l'ornithorynque et la vipère. Plusieurs panneaux sont tombés.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La vitrine des pondeurs** — Une vitrine remplie d'œufs de toutes les tailles. (énigme e3-1)
- en haut au centre : **Le tableau de la galerie** — Un grand tableau aimanté, ses cartes d'animaux tombées au pied du mur. (énigme e3-2)
- en haut à droite : **Les panneaux des surprises** — Des panneaux sur l'ornithorynque, les requins et la vipère. (énigme e3-3)
- au centre : **Le mur des exceptions** — Un mur de cadres mélangés : photos et légendes séparées. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La galerie des animaux étonnants. Un long couloir de vitrines : des œufs de toutes les tailles, une capsule de roussette, des panneaux sur l'ornithorynque et la vipère. Plusieurs panneaux sont tombés. Quatre objets bien éclairés, nettement séparés et lisibles : La vitrine des pondeurs (en haut à gauche); Le tableau de la galerie (en haut au centre); Les panneaux des surprises (en haut à droite); Le mur des exceptions (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1c2b1a et #3f6b3a, lumières et accents #e9b949, #fbe7b0, touches #d3ebf2.
```

### 4. La couveuse de la ferme — `couveuse`

**Lieu** : La couveuse de la ferme du zoo. Une salle tiède où ronronne une couveuse vitrée remplie d'œufs. Au mur, un calendrier de 21 cases et un tableau des durées. Une lampe permet de regarder dans les œufs.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le calendrier de la couveuse** — Un calendrier de 21 cases accroché au-dessus de la couveuse. (énigme e4-1)
- en haut au centre : **La lampe à mirer** — Une lampe qui éclaire l'intérieur d'un œuf, et un dessin à légender. (énigme e4-2)
- en haut à droite : **L'armoire des berceaux** — Une armoire en bois fermée par un cadenas à chiffres. (énigme e4-3)
- au centre : **L'écurie de la jument** — Une stalle paisible où la jument attend son poulain. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La couveuse de la ferme du zoo. Une salle tiède où ronronne une couveuse vitrée remplie d'œufs. Au mur, un calendrier de 21 cases et un tableau des durées. Une lampe permet de regarder dans les œufs. Quatre objets bien éclairés, nettement séparés et lisibles : Le calendrier de la couveuse (en haut à gauche); La lampe à mirer (en haut au centre); L'armoire des berceaux (en haut à droite); L'écurie de la jument (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1c2b1a et #3f6b3a, lumières et accents #e9b949, #fbe7b0, touches #d3ebf2.
```

### 5. Le bureau du carnet de naissance — `bureau`

**Lieu** : Le bureau du carnet de naissance. Un petit bureau en bois avec le grand registre du zoo, une carte des enclos et un carnet fermé par un cadenas. Sur la table, des étiquettes d'enclos à remettre.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les panneaux des enclos** — Des panneaux d'enclos empilés sur le bureau, à remettre dans la bonne case. (énigme e5-1)
- en haut au centre : **Les berceaux de la nurserie** — Une rangée de berceaux et de paniers, chacun avec un petit qui attend. (énigme e5-2)
- en haut à droite : **Le carnet de naissance** — Un gros carnet de cuir posé sur le bureau, presque complet. (énigme e5-3)
- au centre : **Le cadenas du carnet** — Un petit cadenas à trois chiffres sur la couverture du carnet. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le bureau du carnet de naissance. Un petit bureau en bois avec le grand registre du zoo, une carte des enclos et un carnet fermé par un cadenas. Sur la table, des étiquettes d'enclos à remettre. Quatre objets bien éclairés, nettement séparés et lisibles : Les panneaux des enclos (en haut à gauche); Les berceaux de la nurserie (en haut au centre); Le carnet de naissance (en haut à droite); Le cadenas du carnet (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1c2b1a et #3f6b3a, lumières et accents #e9b949, #fbe7b0, touches #d3ebf2.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Inès — `ines`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Vétérinaire du zoo, genre : femme, cheveux longs, porte des lunettes, expression : vétérinaire calme et précise, aime les mots exacts, rassure les apprentis. Tenue en rapport avec son rôle (Vétérinaire du zoo). Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin.
```

### Théo — `theo`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Soigneur de l'aquarium et de la mare, genre : homme, cheveux courts, expression : soigneur enthousiaste de l'aquarium, parle vite, adore les grenouilles. Tenue en rapport avec son rôle (Soigneur de l'aquarium et de la mare). Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin.
```

### Malo — `malo`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Soigneur de la galerie des animaux étonnants, genre : homme, cheveux courts, expression : soigneur malicieux de la galerie, aime surprendre et poser des pièges. Tenue en rapport avec son rôle (Soigneur de la galerie des animaux étonnants). Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin.
```

### Jeanne — `jeanne`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Éleveuse de poules de la ferme du zoo, genre : femme, cheveux courts, expression : éleveuse chaleureuse et patiente, compte les jours sur son calendrier. Tenue en rapport avec son rôle (Éleveuse de poules de la ferme du zoo). Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin.
```

### Sacha — `sacha`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Élève de CM2 en visite scolaire, genre : homme, cheveux courts, porte des lunettes, expression : élève de cm2 en visite, curieux, un peu inquiet de mal faire, content d'avoir de l'aide. Tenue en rapport avec son rôle (Élève de CM2 en visite scolaire). Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `laboratoire`) : « Lent travelling avant dans Le laboratoire de la vétérinaire, à côté de la nurserie. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `aquarium`) : « Lent travelling avant dans L'aquarium et la mare pédagogique. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `galerie`) : « Lent travelling avant dans La galerie des animaux étonnants. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `couveuse`) : « Lent travelling avant dans La couveuse de la ferme du zoo. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `bureau`) : « Lent travelling avant dans Le bureau du carnet de naissance. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/laboratoire.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « Le laboratoire de la vétérinaire, à côté de la nurserie », sans voix ni musique |
| `assets/audio/ambiances/aquarium.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « L'aquarium et la mare pédagogique », sans voix ni musique |
| `assets/audio/ambiances/galerie.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « La galerie des animaux étonnants », sans voix ni musique |
| `assets/audio/ambiances/couveuse.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « La couveuse de la ferme du zoo », sans voix ni musique |
| `assets/audio/ambiances/bureau.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « Le bureau du carnet de naissance », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
