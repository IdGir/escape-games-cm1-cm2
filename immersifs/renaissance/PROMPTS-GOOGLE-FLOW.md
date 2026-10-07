# Prompts Google Flow — L'Atelier de Léonard à Amboise

Ces prompts produisent les images du jeu `immersifs/renaissance/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ. Début du XVIe siècle, règne de François Ier : Amboise, l'imprimerie, l'atelier de Léonard, Chambord et la galerie de peinture. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #12130a et #26271a, lumières et accents #a8872c, #ffd27a, touches #b9d8c0.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. L'imprimerie de Maître Jacquet — `imprimerie`

**Lieu** : Une imprimerie de la ville d'Amboise, au printemps 1518. Des livres frais sortent de la presse : des textes latins et grecs, des traductions, des almanachs. Sur le mur, la gravure d'un temple romain à colonnes.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à droite : **La gravure du temple romain** — Sur le mur, un temple à colonnes : ce que les savants admirent. (énigme e1-1)
- en bas à gauche : **La pile de livres** — Des livres imprimés, empilés : des mots nouveaux pour un temps nouveau. (énigme e1-2)
- en haut au centre : **La presse à imprimer** — Une grande presse en bois : pourquoi dit-on « renaître » ? (énigme e1-3)
- au milieu à droite : **La page d'épreuve** — Une page d'épreuve où manquent des mots. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Une imprimerie de la ville d'Amboise, au printemps 1518. Des livres frais sortent de la presse : des textes latins et grecs, des traductions, des almanachs. Sur le mur, la gravure d'un temple romain à colonnes. Quatre objets bien éclairés, nettement séparés et lisibles : La gravure du temple romain (en haut à droite); La pile de livres (en bas à gauche); La presse à imprimer (en haut au centre); La page d'épreuve (au milieu à droite). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #12130a et #26271a, lumières et accents #a8872c, #ffd27a, touches #b9d8c0.
```

### 2. La grande salle d'Amboise — `salle`

**Lieu** : La grande salle du château royal d'Amboise. On accroche des tapisseries, on dresse les tables. Sur les murs, la lettre F couronnée et des salamandres. Par les fenêtres, on voit la Loire.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en bas à gauche : **Le trône** — Le trône du roi François Ier. (énigme e2-1)
- en haut à gauche : **Les portraits du roi** — Des portraits à ranger dans l'ordre d'une vie. (énigme e2-2)
- au centre : **La tapisserie** — Une tapisserie qui montre les protégés du roi. (énigme e2-3)
- en bas à droite : **Le coffret de Dame Hélène** — Un coffret fermé par un cadenas à chiffres. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La grande salle du château royal d'Amboise. On accroche des tapisseries, on dresse les tables. Sur les murs, la lettre F couronnée et des salamandres. Par les fenêtres, on voit la Loire. Quatre objets bien éclairés, nettement séparés et lisibles : Le trône (en bas à gauche); Les portraits du roi (en haut à gauche); La tapisserie (au centre); Le coffret de Dame Hélène (en bas à droite). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #12130a et #26271a, lumières et accents #a8872c, #ffd27a, touches #b9d8c0.
```

### 3. L'atelier du Cloux — `atelier`

**Lieu** : L'atelier de Léonard, au manoir du Cloux, près du château. Des feuilles couvertes de dessins : des visages, des machines, des oiseaux, des tourbillons d'eau. Sur un chevalet, un portrait de femme au sourire léger.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut au centre : **Les œuvres de l'atelier** — Peinture, ingénieur, savant : plusieurs talents. (énigme e3-1)
- au milieu à gauche : **Les carnets en désordre** — Les carnets de Léonard, tous mêlés. (énigme e3-2)
- au milieu à droite : **La table de l'atelier** — Un objet qui n'appartient pas à l'atelier. (énigme e3-3)
- au centre : **Le miroir** — Léonard écrit à l'envers : un mot à lire dans le miroir. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : L'atelier de Léonard, au manoir du Cloux, près du château. Des feuilles couvertes de dessins : des visages, des machines, des oiseaux, des tourbillons d'eau. Sur un chevalet, un portrait de femme au sourire léger. Quatre objets bien éclairés, nettement séparés et lisibles : Les œuvres de l'atelier (en haut au centre); Les carnets en désordre (au milieu à gauche); La table de l'atelier (au milieu à droite); Le miroir (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #12130a et #26271a, lumières et accents #a8872c, #ffd27a, touches #b9d8c0.
```

### 4. Le cabinet des plans — `plans`

**Lieu** : Le cabinet des plans, au château d'Amboise. Sur une grande table, des plans de châteaux : Amboise, Blois où l'on construit une aile nouvelle, et le projet d'un château immense dans la forêt de Chambord.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à droite : **Le plan de Chambord** — Le plan d'un grand château. (énigme e4-1)
- en haut à gauche : **Les deux maquettes** — Un château fort et un château Renaissance. (énigme e4-2)
- en haut au centre : **Les trois châteaux** — Trois châteaux, trois secrets. (énigme e4-3)
- en bas à gauche : **La salamandre sculptée** — L'emblème du roi sur la cheminée. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le cabinet des plans, au château d'Amboise. Sur une grande table, des plans de châteaux : Amboise, Blois où l'on construit une aile nouvelle, et le projet d'un château immense dans la forêt de Chambord. Quatre objets bien éclairés, nettement séparés et lisibles : Le plan de Chambord (en haut à droite); Les deux maquettes (en haut à gauche); Les trois châteaux (en haut au centre); La salamandre sculptée (en bas à gauche). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #12130a et #26271a, lumières et accents #a8872c, #ffd27a, touches #b9d8c0.
```

### 5. La galerie des tableaux — `galerie`

**Lieu** : La galerie des tableaux du château. Des tableaux venus d'Italie : des portraits, des paysages, des palais peints si profonds qu'on croirait pouvoir y entrer.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à droite : **Le tableau en perspective** — Un tableau en perspective à lire. (énigme e5-1)
- en haut à gauche : **Les secrets des peintres** — Les techniques des peintres. (énigme e5-2)
- en haut à gauche : **Le cadenas du carnet** — Un cadenas qui garde le carnet. (énigme e5-3)
- en haut à droite : **La leçon de Bastien** — Un texte à compléter sur la perspective. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : La galerie des tableaux du château. Des tableaux venus d'Italie : des portraits, des paysages, des palais peints si profonds qu'on croirait pouvoir y entrer. Quatre objets bien éclairés, nettement séparés et lisibles : Le tableau en perspective (en haut à droite); Les secrets des peintres (en haut à gauche); Le cadenas du carnet (en haut à gauche); La leçon de Bastien (en haut à droite). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #12130a et #26271a, lumières et accents #a8872c, #ffd27a, touches #b9d8c0.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Tommaso — `tommaso`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Apprenti de Léonard de Vinci, 12 ans, venu d'Italie, genre : garçon, cheveux courts, expression : apprenti curieux, émerveillé par léonard. Tenue en rapport avec son rôle (Apprenti de Léonard de Vinci, 12 ans, venu d'Italie). Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Maître Jacquet — `jacquet`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Imprimeur à Amboise, genre : homme, cheveux courts, porte des lunettes, expression : imprimeur grave mais passionné. Tenue en rapport avec son rôle (Imprimeur à Amboise). Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Dame Hélène — `helene`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Dame de la cour de François Ier, genre : femme, cheveux longs, expression : dame de la cour, fine et cultivée. Tenue en rapport avec son rôle (Dame de la cour de François Ier). Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Colombe — `colombe`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Fille d'un maître maçon des chantiers du roi, 11 ans, genre : fille, cheveux longs, expression : fille de maçon, concrète et directe. Tenue en rapport avec son rôle (Fille d'un maître maçon des chantiers du roi, 11 ans). Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Bastien — `bastien`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Jeune peintre de la cour, élève des artistes italiens, genre : garçon, cheveux courts, expression : jeune peintre fier de son art. Tenue en rapport avec son rôle (Jeune peintre de la cour, élève des artistes italiens). Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `imprimerie`) : « Lent travelling avant dans Une imprimerie de la ville d'Amboise, au printemps 1518. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `salle`) : « Lent travelling avant dans La grande salle du château royal d'Amboise. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `atelier`) : « Lent travelling avant dans L'atelier de Léonard, au manoir du Cloux, près du château. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `plans`) : « Lent travelling avant dans Le cabinet des plans, au château d'Amboise. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `galerie`) : « Lent travelling avant dans La galerie des tableaux du château. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.
