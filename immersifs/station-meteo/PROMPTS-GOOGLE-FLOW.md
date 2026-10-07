# Prompts Google Flow — La Station météo disparue

Ces prompts produisent les images du jeu `immersifs/station-meteo/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ. Univers contemporain : la station météo d'une école, après un orage qui a dérangé les instruments. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f1c26 et #243746, lumières et accents #3d9be9, #ffd166, touches #bfe7ff.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. L'abri météo — `abri`

**Lieu** : 🌡️ L'abri météo, dans la cour de l'école. Au bout de la cour, sur une petite pelouse, se dresse une boîte blanche à persiennes, montée sur un pied. Sa porte bat au vent. Le thermomètre a été sorti de l'abri et posé sur le muret, en plein soleil.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le thermomètre de l'abri** — Un thermomètre à lire, y compris sous zéro. (énigme e1-1)
- en haut au centre : **L'abri blanc à persiennes** — L'abri météo : où placer le thermomètre ? (énigme e1-2)
- en haut à droite : **Les relevés de la semaine** — Des températures à ranger du plus froid au plus chaud. (énigme e1-3)
- au centre : **Les fiches de mesure** — Des mesures fiables et d'autres faussées. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🌡️ L'abri météo, dans la cour de l'école. Au bout de la cour, sur une petite pelouse, se dresse une boîte blanche à persiennes, montée sur un pied. Sa porte bat au vent. Le thermomètre a été sorti de l'abri et posé sur le muret, en plein soleil. Quatre objets bien éclairés, nettement séparés et lisibles : Le thermomètre de l'abri (en haut à gauche); L'abri blanc à persiennes (en haut au centre); Les relevés de la semaine (en haut à droite); Les fiches de mesure (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f1c26 et #243746, lumières et accents #3d9be9, #ffd166, touches #bfe7ff.
```

### 2. Le mât du vent — `mat`

**Lieu** : 🧭 Le mât de l'anémomètre et de la girouette. Au sommet d'un mât, des coupelles tournent et une girouette hésite. L'orage a fait pivoter la croix des points cardinaux : plus personne ne sait où est le nord.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La rose des vents** — Une rose des vents à compléter. (énigme e2-1)
- en haut au centre : **La girouette et l'anémomètre** — Deux instruments : direction et vitesse du vent. (énigme e2-2)
- en haut à droite : **L'échelle de Beaufort** — Une échelle qui décrit la force du vent. (énigme e2-3)
- au centre : **Le carnet du capitaine** — Le carnet de bord de Keita, aux mots manquants. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🧭 Le mât de l'anémomètre et de la girouette. Au sommet d'un mât, des coupelles tournent et une girouette hésite. L'orage a fait pivoter la croix des points cardinaux : plus personne ne sait où est le nord. Quatre objets bien éclairés, nettement séparés et lisibles : La rose des vents (en haut à gauche); La girouette et l'anémomètre (en haut au centre); L'échelle de Beaufort (en haut à droite); Le carnet du capitaine (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f1c26 et #243746, lumières et accents #3d9be9, #ffd166, touches #bfe7ff.
```

### 3. Le pluviomètre — `pluvio`

**Lieu** : 🌧️ Le pluviomètre, au fond du jardin. Loin des arbres et des murs, un entonnoir surmonte un tube gradué. Il pleut encore un peu. Sur le cahier de Tiago, les relevés de la semaine sont brouillés par les gouttes.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le pluviomètre** — Un pluviomètre à lire. (énigme e3-1)
- en haut au centre : **Le pluviomètre à graduations** — Un millimètre de pluie, qu'est-ce que c'est ? (énigme e3-2)
- en haut à droite : **Le tableau des pluies** — Des journées à ranger du plus sec au plus arrosé. (énigme e3-3)
- au centre : **Le cadenas du cumul** — Un cadenas dont le code est un cumul de pluie. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🌧️ Le pluviomètre, au fond du jardin. Loin des arbres et des murs, un entonnoir surmonte un tube gradué. Il pleut encore un peu. Sur le cahier de Tiago, les relevés de la semaine sont brouillés par les gouttes. Quatre objets bien éclairés, nettement séparés et lisibles : Le pluviomètre (en haut à gauche); Le pluviomètre à graduations (en haut au centre); Le tableau des pluies (en haut à droite); Le cadenas du cumul (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f1c26 et #243746, lumières et accents #3d9be9, #ffd166, touches #bfe7ff.
```

### 4. Le tableau des relevés — `bureau`

**Lieu** : 📋 Le bureau des relevés. Au mur, un tableau à double entrée et un graphique en barres. L'eau a effacé des cases, et quelqu'un a recopié une valeur impossible.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le tableau à double entrée** — Un tableau où des cases sont effacées. (énigme e4-1)
- en haut au centre : **La valeur impossible** — Un relevé qui n'est pas possible. (énigme e4-2)
- en haut à droite : **La fiche d'analyse** — Ce que dit le tableau des relevés. (énigme e4-3)
- au centre : **Le graphique de la pluie** — Un graphique à barres de la pluie. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 📋 Le bureau des relevés. Au mur, un tableau à double entrée et un graphique en barres. L'eau a effacé des cases, et quelqu'un a recopié une valeur impossible. Quatre objets bien éclairés, nettement séparés et lisibles : Le tableau à double entrée (en haut à gauche); La valeur impossible (en haut au centre); La fiche d'analyse (en haut à droite); Le graphique de la pluie (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f1c26 et #243746, lumières et accents #3d9be9, #ffd166, touches #bfe7ff.
```

### 5. Le bulletin du jour — `studio`

**Lieu** : 📡 La salle de prévision. Un grand écran montre une carte, un soleil, un nuage et une flèche de vent. Le micro attend. Pour lancer le bulletin, il faut entrer la valeur de vérité de mercredi : trois mesures justes.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le mur météo et climat** — Météo ou climat ? Deux mots à ne pas confondre. (énigme e5-1)
- en haut au centre : **La carte de prévision** — Prévoir la sortie à partir des mesures. (énigme e5-2)
- en haut à droite : **Le bulletin** — Un mot caché dans le bulletin du jour. (énigme e5-3)
- au centre : **Le cadenas de la prévision** — Le dernier cadenas : la valeur de vérité. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 📡 La salle de prévision. Un grand écran montre une carte, un soleil, un nuage et une flèche de vent. Le micro attend. Pour lancer le bulletin, il faut entrer la valeur de vérité de mercredi : trois mesures justes. Quatre objets bien éclairés, nettement séparés et lisibles : Le mur météo et climat (en haut à gauche); La carte de prévision (en haut au centre); Le bulletin (en haut à droite); Le cadenas de la prévision (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0f1c26 et #243746, lumières et accents #3d9be9, #ffd166, touches #bfe7ff.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Madame Vasseur — `vasseur`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Prévisionniste, marraine de la station de l'école, genre : femme, cheveux courts, porte des lunettes, expression : prévisionniste rassurante, rigoureuse. Tenue en rapport avec son rôle (Prévisionniste, marraine de la station de l'école). Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ.
```

### Tiago — `tiago`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Technicien de station météo, genre : homme, cheveux courts, expression : technicien pragmatique, toujours une clé à molette. Tenue en rapport avec son rôle (Technicien de station météo). Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ.
```

### Lina — `lina`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Élève de CM2, responsable de la station de l'école, genre : fille, cheveux longs, expression : élève sérieuse, fière de sa station. Tenue en rapport avec son rôle (Élève de CM2, responsable de la station de l'école). Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ.
```

### Capitaine Keïta — `keita`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Marin, dépend du vent pour sortir en mer, genre : homme, cheveux absents, expression : capitaine du vent, parle comme un marin. Tenue en rapport avec son rôle (Marin, dépend du vent pour sortir en mer). Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `abri`) : « Lent travelling avant dans 🌡️ L'abri météo, dans la cour de l'école. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `mat`) : « Lent travelling avant dans 🧭 Le mât de l'anémomètre et de la girouette. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `pluvio`) : « Lent travelling avant dans 🌧️ Le pluviomètre, au fond du jardin. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `bureau`) : « Lent travelling avant dans 📋 Le bureau des relevés. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `studio`) : « Lent travelling avant dans 📡 La salle de prévision. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.
