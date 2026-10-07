# Prompts Google Flow — Le Phare de l'île Lumière

Ces prompts produisent les images du jeu `immersifs/lumiere/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #070c1a et #101a33, lumières et accents #f2b84b, #ffd27a, touches #8fd3ff.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La lanterne du phare — `lanterne`

**Lieu** : La lanterne, tout en haut du phare. Une petite pièce ronde entourée de vitres. Au centre, la grosse lampe du phare, éteinte, entourée de sa lentille en verre. Dehors, la mer devient sombre et un voilier approche.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La liste de Maëlle** — Une liste où les sources de lumière et les objets éclairés se mélangent. (énigme e1-1)
- en haut au centre : **Le schéma sur le mur** — Un schéma peint qui suit la lumière du phare jusqu'au bateau. (énigme e1-2)
- en haut à droite : **Le coffre des signaux** — Un coffre où l'on range les objets qui envoient des messages. (énigme e1-3)
- au centre : **Le cahier de Maëlle** — Le cahier où la gardienne note tout ce qu'elle sait de la lumière. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La lanterne, tout en haut du phare. Une petite pièce ronde entourée de vitres. Au centre, la grosse lampe du phare, éteinte, entourée de sa lentille en verre. Dehors, la mer devient sombre et un voilier approche. Quatre objets bien éclairés, nettement séparés et lisibles : La liste de Maëlle (en haut à gauche); Le schéma sur le mur (en haut au centre); Le coffre des signaux (en haut à droite); Le cahier de Maëlle (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #070c1a et #101a33, lumières et accents #f2b84b, #ffd27a, touches #8fd3ff.
```

### 2. L'atelier des vitres — `atelier`

**Lieu** : L'atelier, au pied de l'escalier du phare. Un établi couvert de plaques de verre, de papier calque, de planches et de feuilles d'aluminium. Une lampe de bureau éclaire un banc d'essai.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **L'établi des mots** — Un établi où trois mots sont gravés dans le bois. (énigme e2-1)
- en haut au centre : **Le banc d'essai** — Un banc avec une lampe devant lequel on place chaque matériau. (énigme e2-2)
- en haut à droite : **Le carnet d'essais** — Un carnet taché d'huile où des mots ont disparu. (énigme e2-3)
- au centre : **Le registre de l'ingénieure** — Le registre des vitres fabriquées dans l'atelier. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : L'atelier, au pied de l'escalier du phare. Un établi couvert de plaques de verre, de papier calque, de planches et de feuilles d'aluminium. Une lampe de bureau éclaire un banc d'essai. Quatre objets bien éclairés, nettement séparés et lisibles : L'établi des mots (en haut à gauche); Le banc d'essai (en haut au centre); Le carnet d'essais (en haut à droite); Le registre de l'ingénieure (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #070c1a et #101a33, lumières et accents #f2b84b, #ffd27a, touches #8fd3ff.
```

### 3. La chambre aux ombres — `chambre`

**Lieu** : La chambre du gardien, au deuxième étage. Un lit sous la fenêtre ronde, un drap tendu en guise d'écran, une lampe de poche et des figurines découpées dans du carton : un bateau, une mouette, un phare.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **L'écran blanc de Nils** — Un écran blanc où une balle projette son ombre. (énigme e3-1)
- en haut au centre : **Le carnet d'observations** — Les affirmations de Nils sur les ombres, écrites une par une. (énigme e3-2)
- en haut à droite : **Le théâtre d'ombres** — Une petite scène avec une figurine de bateau et une lampe mobile. (énigme e3-3)
- au centre : **La boîte à ombres** — Une boîte où un mot est caché derrière des lettres. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La chambre du gardien, au deuxième étage. Un lit sous la fenêtre ronde, un drap tendu en guise d'écran, une lampe de poche et des figurines découpées dans du carton : un bateau, une mouette, un phare. Quatre objets bien éclairés, nettement séparés et lisibles : L'écran blanc de Nils (en haut à gauche); Le carnet d'observations (en haut au centre); Le théâtre d'ombres (en haut à droite); La boîte à ombres (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #070c1a et #101a33, lumières et accents #f2b84b, #ffd27a, touches #8fd3ff.
```

### 4. La cour du cadran solaire — `cour`

**Lieu** : La cour du phare, autour du cadran solaire. Une cour pavée entourée d'un muret. Au centre, un bâton planté dans le sol ; autour, des traits peints et des heures. Sur un banc, l'appareil photo et le carnet d'Achille.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les photos d'Achille** — Une série de photos de l'ombre d'un bâton dans la cour. (énigme e4-1)
- en haut au centre : **Le cadran de pierre** — Le cadran solaire gravé au milieu de la cour. (énigme e4-2)
- en haut à droite : **Le plan de la cour** — Un plan de la cour vu de dessus avec trois ombres tracées. (énigme e4-3)
- au centre : **Le carnet de l'été** — Un carnet où Achille relève la longueur des ombres tout l'été. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La cour du phare, autour du cadran solaire. Une cour pavée entourée d'un muret. Au centre, un bâton planté dans le sol ; autour, des traits peints et des heures. Sur un banc, l'appareil photo et le carnet d'Achille. Quatre objets bien éclairés, nettement séparés et lisibles : Les photos d'Achille (en haut à gauche); Le cadran de pierre (en haut au centre); Le plan de la cour (en haut à droite); Le carnet de l'été (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #070c1a et #101a33, lumières et accents #f2b84b, #ffd27a, touches #8fd3ff.
```

### 5. La galerie du phare — `galerie`

**Lieu** : La galerie extérieure, autour de la lanterne, face à la mer. Un balcon étroit avec une rambarde, tout en haut du phare. Le vent souffle fort. Entre deux nuages, un disque pâle éclaire la mer ; au loin, une petite lumière clignote : c'est La Mouette.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le carnet de la Lune** — Un carnet où la capitaine dessine la Lune chaque soir. (énigme e5-1)
- en haut au centre : **La rose des phases** — Un tableau où chaque phase de la Lune attend sa description. (énigme e5-2)
- en haut à droite : **La lampe à signaux** — La lampe de La Mouette qui répond au phare par éclats courts et longs. (énigme e5-3)
- au centre : **Le journal de bord** — Le journal où Yasmine note ses observations du ciel et de la mer. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La galerie extérieure, autour de la lanterne, face à la mer. Un balcon étroit avec une rambarde, tout en haut du phare. Le vent souffle fort. Entre deux nuages, un disque pâle éclaire la mer ; au loin, une petite lumière clignote : c'est La Mouette. Quatre objets bien éclairés, nettement séparés et lisibles : Le carnet de la Lune (en haut à gauche); La rose des phases (en haut au centre); La lampe à signaux (en haut à droite); Le journal de bord (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #070c1a et #101a33, lumières et accents #f2b84b, #ffd27a, touches #8fd3ff.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Maëlle — `maelle`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Gardienne du phare de l'île Lumière, genre : femme, cheveux longs, expression : gardienne du phare, posée, attentive aux signaux. Tenue en rapport avec son rôle (Gardienne du phare de l'île Lumière). Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ.
```

### Salomé — `salome`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Ingénieure en signalisation maritime, genre : femme, cheveux courts, porte des lunettes, expression : ingénieure précise, aime tester et comparer. Tenue en rapport avec son rôle (Ingénieure en signalisation maritime). Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ.
```

### Nils — `nils`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Neveu de Maëlle, 9 ans, passionné d'ombres, genre : garçon, cheveux courts, expression : jeune gardien curieux, joue avec les ombres. Tenue en rapport avec son rôle (Neveu de Maëlle, 9 ans, passionné d'ombres). Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ.
```

### Achille — `achille`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Horloger du port, constructeur de cadrans solaires, genre : homme, cheveux courts, porte des lunettes, expression : horloger méticuleux, patient, aime l'ordre. Tenue en rapport avec son rôle (Horloger du port, constructeur de cadrans solaires). Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ.
```

### Capitaine Yasmine — `yasmine`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Capitaine du voilier La Mouette, genre : femme, cheveux longs, expression : capitaine bavarde et rieuse, parle de la mer et du ciel. Tenue en rapport avec son rôle (Capitaine du voilier La Mouette). Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, nombreux détails narratifs lisibles, grain fin, profondeur de champ.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `lanterne`) : « Lent travelling avant dans La lanterne, tout en haut du phare. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `atelier`) : « Lent travelling avant dans L'atelier, au pied de l'escalier du phare. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `chambre`) : « Lent travelling avant dans La chambre du gardien, au deuxième étage. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `cour`) : « Lent travelling avant dans La cour du phare, autour du cadran solaire. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `galerie`) : « Lent travelling avant dans La galerie extérieure, autour de la lanterne, face à la mer. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.
