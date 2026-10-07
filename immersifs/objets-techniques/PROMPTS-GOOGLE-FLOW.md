# Prompts Google Flow — L'Atelier de l'inventeur

Ces prompts produisent les images du jeu `immersifs/objets-techniques/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ. Univers contemporain : un atelier de réparation de vélos et de fabrication d'objets du quotidien. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #11181d et #26323b, lumières et accents #c0732a, #ffc46b, touches #8fd0e8.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. L'entrée de l'atelier — `atelier`

**Lieu** : 🚪 L'entrée de l'atelier. Une grande porte de bois, une table couverte d'objets du quotidien et, au fond, le coffre-fort de l'inventrice. Sur chaque objet, une étiquette vide attend une réponse.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le mur des objets** — Des objets accrochés : chacun répond à un besoin. (énigme e1-1)
- en haut au centre : **La vitrine** — Des objets pour servir ou pour plaire. (énigme e1-2)
- en haut à droite : **Le tri de l'inventrice** — Une caisse d'objets à trier. (énigme e1-3)
- au centre : **La première serrure** — Une serrure à mot. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🚪 L'entrée de l'atelier. Une grande porte de bois, une table couverte d'objets du quotidien et, au fond, le coffre-fort de l'inventrice. Sur chaque objet, une étiquette vide attend une réponse. Quatre objets bien éclairés, nettement séparés et lisibles : Le mur des objets (en haut à gauche); La vitrine (en haut au centre); Le tri de l'inventrice (en haut à droite); La première serrure (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #11181d et #26323b, lumières et accents #c0732a, #ffc46b, touches #8fd0e8.
```

### 2. L'établi — `etabli`

**Lieu** : 🔧 L'établi de démontage. Sur le grand établi, une lampe torche est ouverte. Ses pièces sont alignées sur un tapis vert. Au mur, un vélo est accroché, la chaîne enlevée.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le schéma de la lampe torche** — Un schéma accroché à l'établi. (énigme e2-1)
- en haut au centre : **Les pièces démontées** — Chaque pièce a son rôle. (énigme e2-2)
- en haut à droite : **L'étiquette de l'établi** — Le bon mot au bon endroit. (énigme e2-3)
- au centre : **Le carnet de l'inventrice** — Un carnet aux mots effacés. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🔧 L'établi de démontage. Sur le grand établi, une lampe torche est ouverte. Ses pièces sont alignées sur un tapis vert. Au mur, un vélo est accroché, la chaîne enlevée. Quatre objets bien éclairés, nettement séparés et lisibles : Le schéma de la lampe torche (en haut à gauche); Les pièces démontées (en haut au centre); L'étiquette de l'établi (en haut à droite); Le carnet de l'inventrice (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #11181d et #26323b, lumières et accents #c0732a, #ffc46b, touches #8fd0e8.
```

### 3. La matériauthèque — `materiaux`

**Lieu** : 🗄️ La matériauthèque. Des casiers du sol au plafond. Dans chacun, des échantillons : un morceau de bois, une plaque de métal, un éclat de verre, de la laine, du plastique. Certains casiers ont été mélangés.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les casiers** — Des casiers de matériaux à classer. (énigme e3-1)
- en haut au centre : **Les étiquettes de la matériauthèque** — Des affirmations sur les matériaux. (énigme e3-2)
- en haut à droite : **L'échantillon égaré** — Un échantillon qui n'est pas dans la bonne famille. (énigme e3-3)
- au centre : **Le tableau des usages** — Quel matériau pour quel usage ? (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🗄️ La matériauthèque. Des casiers du sol au plafond. Dans chacun, des échantillons : un morceau de bois, une plaque de métal, un éclat de verre, de la laine, du plastique. Certains casiers ont été mélangés. Quatre objets bien éclairés, nettement séparés et lisibles : Les casiers (en haut à gauche); Les étiquettes de la matériauthèque (en haut au centre); L'échantillon égaré (en haut à droite); Le tableau des usages (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #11181d et #26323b, lumières et accents #c0732a, #ffc46b, touches #8fd0e8.
```

### 4. La salle des machines — `machines`

**Lieu** : ⚙️ La salle des machines. Des engrenages accrochés au mur, une poulie au plafond, une petite éolienne près de la fenêtre et un panneau solaire sur l'appui. Au centre, un vélo sur un support tourne à vide.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La chaîne d'énergie** — D'où vient l'énergie, où va-t-elle ? (énigme e4-1)
- en haut au centre : **Les machines alignées** — Chaque machine a sa source d'énergie. (énigme e4-2)
- en haut à droite : **Les engrenages** — Des engrenages transmettent le mouvement. (énigme e4-3)
- au centre : **Le cadenas à mots** — Un cadenas à mots sur la porte. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : ⚙️ La salle des machines. Des engrenages accrochés au mur, une poulie au plafond, une petite éolienne près de la fenêtre et un panneau solaire sur l'appui. Au centre, un vélo sur un support tourne à vide. Quatre objets bien éclairés, nettement séparés et lisibles : La chaîne d'énergie (en haut à gauche); Les machines alignées (en haut au centre); Les engrenages (en haut à droite); Le cadenas à mots (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #11181d et #26323b, lumières et accents #c0732a, #ffc46b, touches #8fd0e8.
```

### 5. Le coin montage — `montage`

**Lieu** : 📋 Le coin montage. Une table lumineuse, des plans épinglés au mur, une notice ouverte. À côté, le coffre-fort de l'inventrice et son clavier à cinq mots.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La notice dépliée** — Les étapes du montage. (énigme e5-1)
- en haut au centre : **Le mode d'emploi** — Des phrases sur la lecture de la notice. (énigme e5-2)
- en haut à droite : **Les deux objets** — Deux objets pour un même besoin. (énigme e5-3)
- au centre : **Le cycle de l'inventrice** — Le cycle de vie d'un objet. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 📋 Le coin montage. Une table lumineuse, des plans épinglés au mur, une notice ouverte. À côté, le coffre-fort de l'inventrice et son clavier à cinq mots. Quatre objets bien éclairés, nettement séparés et lisibles : La notice dépliée (en haut à gauche); Le mode d'emploi (en haut au centre); Les deux objets (en haut à droite); Le cycle de l'inventrice (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #11181d et #26323b, lumières et accents #c0732a, #ffc46b, touches #8fd0e8.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Zoé — `zoe`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Apprentie ingénieure, 11 ans, genre : fille, cheveux longs, porte des lunettes, expression : apprentie enthousiaste, pose des questions. Tenue en rapport avec son rôle (Apprentie ingénieure, 11 ans). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Awa — `awa`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Ouvrière de l'atelier, genre : femme, cheveux courts, expression : ouvrière efficace, ne perd pas de temps. Tenue en rapport avec son rôle (Ouvrière de l'atelier). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Monsieur Marcel — `marcel`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Réparateur de vélos, genre : homme, cheveux absents, expression : réparateur bourru mais bienveillant. Tenue en rapport avec son rôle (Réparateur de vélos). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Éléonore Marchand — `eleonore`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : L'inventrice, genre : femme, cheveux longs, expression : inventrice rêveuse et précise. Tenue en rapport avec son rôle (L'inventrice). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `atelier`) : « Lent travelling avant dans 🚪 L'entrée de l'atelier. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `etabli`) : « Lent travelling avant dans 🔧 L'établi de démontage. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `materiaux`) : « Lent travelling avant dans 🗄️ La matériauthèque. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `machines`) : « Lent travelling avant dans ⚙️ La salle des machines. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `montage`) : « Lent travelling avant dans 📋 Le coin montage. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/atelier.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « 🚪 L'entrée de l'atelier », sans voix ni musique |
| `assets/audio/ambiances/etabli.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « 🔧 L'établi de démontage », sans voix ni musique |
| `assets/audio/ambiances/materiaux.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « 🗄️ La matériauthèque », sans voix ni musique |
| `assets/audio/ambiances/machines.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « ⚙️ La salle des machines », sans voix ni musique |
| `assets/audio/ambiances/montage.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « 📋 Le coin montage », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
