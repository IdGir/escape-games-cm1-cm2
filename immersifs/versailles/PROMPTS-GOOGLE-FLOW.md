# Prompts Google Flow — De l'édit de Nantes à Versailles

Ces prompts produisent les images du jeu `immersifs/versailles/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ. 1598 puis 1682-1715 : une imprimerie et une rue de la fin des guerres de Religion, puis les jardins, la chambre et le cabinet du Conseil à Versailles. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #17101c et #33263d, lumières et accents #cfa86a, #ffd98a, touches #cdb8e8.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. L'imprimerie de Suzanne — `imprimerie`

**Lieu** : Une imprimerie, dans une petite ville du royaume, en 1598. Des feuilles fraîchement imprimées sèchent sur des fils. La grande presse de bois grince. Sur l'établi, une Bible en français et un almanach où quelqu'un a noté des dates.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La frise des troubles** — Une frise des troubles religieux. (énigme e1-1)
- en haut au centre : **Les deux enseignes** — Catholiques et protestants, deux voisins. (énigme e1-2)
- en haut à droite : **Les livres imprimés** — Des livres qui disent pourquoi tant de troubles. (énigme e1-3)
- au centre : **La balance des différences** — Ce qui sépare, ce qui rapproche. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Une imprimerie, dans une petite ville du royaume, en 1598. Des feuilles fraîchement imprimées sèchent sur des fils. La grande presse de bois grince. Sur l'établi, une Bible en français et un almanach où quelqu'un a noté des dates. Quatre objets bien éclairés, nettement séparés et lisibles : La frise des troubles (en haut à gauche); Les deux enseignes (en haut au centre); Les livres imprimés (en haut à droite); La balance des différences (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #17101c et #33263d, lumières et accents #cfa86a, #ffd98a, touches #cdb8e8.
```

### 2. La rue des deux voisins — `rue`

**Lieu** : Une rue de la même ville, au printemps 1598. D'un côté, la boulangerie de Mathurin ; de l'autre, l'imprimerie de Suzanne. Au bout de la rue, le clocher de l'église. Sur la place, un crieur lit à voix haute un texte du roi.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **L'affiche de l'édit** — Le texte de l'édit de Nantes. (énigme e2-1)
- en haut au centre : **La balance des permissions** — Permis ou limité par l'édit. (énigme e2-2)
- en haut à droite : **La lettre de Mathurin** — Une lettre aux mots manquants. (énigme e2-3)
- au centre : **Le cachet de l'édit** — Le sceau du roi sur l'édit. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Une rue de la même ville, au printemps 1598. D'un côté, la boulangerie de Mathurin ; de l'autre, l'imprimerie de Suzanne. Au bout de la rue, le clocher de l'église. Sur la place, un crieur lit à voix haute un texte du roi. Quatre objets bien éclairés, nettement séparés et lisibles : L'affiche de l'édit (en haut à gauche); La balance des permissions (en haut au centre); La lettre de Mathurin (en haut à droite); Le cachet de l'édit (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #17101c et #33263d, lumières et accents #cfa86a, #ffd98a, touches #cdb8e8.
```

### 3. Les jardins de Versailles — `jardins`

**Lieu** : Les jardins du château de Versailles, en 1682. Des allées droites, des parterres dessinés comme des broderies, des fontaines. Au fond, un bassin où un dieu sort de l'eau sur son char. Le château, immense, brille au soleil.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le plan du domaine** — Un plan de Versailles à légender. (énigme e3-1)
- en haut au centre : **Les artistes du roi** — Le Nôtre, Le Brun, Mansart, Lully. (énigme e3-2)
- en haut à droite : **Le bassin d'Apollon** — Le dieu du Soleil dans son char. (énigme e3-3)
- au centre : **La statue du dieu** — Un dieu du bassin à retrouver. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Les jardins du château de Versailles, en 1682. Des allées droites, des parterres dessinés comme des broderies, des fontaines. Au fond, un bassin où un dieu sort de l'eau sur son char. Le château, immense, brille au soleil. Quatre objets bien éclairés, nettement séparés et lisibles : Le plan du domaine (en haut à gauche); Les artistes du roi (en haut au centre); Le bassin d'Apollon (en haut à droite); La statue du dieu (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #17101c et #33263d, lumières et accents #cfa86a, #ffd98a, touches #cdb8e8.
```

### 4. La chambre du roi — `chambre`

**Lieu** : L'antichambre et la chambre du roi, au château de Versailles. Un lit entouré d'une balustrade dorée. Des courtisans attendent, debout, dans l'antichambre. Un huissier garde la porte et laisse entrer chacun selon son rang.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La pendule du lever** — La journée du roi, du lever au coucher. (énigme e4-1)
- en haut au centre : **L'intrus de la journée** — Un moment qui n'est pas dans la journée. (énigme e4-2)
- en haut à droite : **Le lexique de la cour** — Les mots de la cour à associer. (énigme e4-3)
- au centre : **Le carnet de Dame Isabeau** — Un carnet aux mots manquants. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : L'antichambre et la chambre du roi, au château de Versailles. Un lit entouré d'une balustrade dorée. Des courtisans attendent, debout, dans l'antichambre. Un huissier garde la porte et laisse entrer chacun selon son rang. Quatre objets bien éclairés, nettement séparés et lisibles : La pendule du lever (en haut à gauche); L'intrus de la journée (en haut au centre); Le lexique de la cour (en haut à droite); Le carnet de Dame Isabeau (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #17101c et #33263d, lumières et accents #cfa86a, #ffd98a, touches #cdb8e8.
```

### 5. Le cabinet du Conseil — `conseil`

**Lieu** : Le cabinet du Conseil, au château de Versailles. Une grande table couverte d'un tapis vert, des fauteuils, des cartes du royaume. C'est ici que le roi réunit ses ministres et prend ses décisions.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La table du Conseil** — Henri IV ou Louis XIV ? (énigme e5-1)
- en haut au centre : **Le fauteuil du roi** — Le roi décide de tout. (énigme e5-2)
- en haut à droite : **Le cadenas du Conseil** — Un cadenas à chiffres sur le coffre du Conseil. (énigme e5-3)
- au centre : **La révocation** — 1685 : la fin de la tolérance. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : Le cabinet du Conseil, au château de Versailles. Une grande table couverte d'un tapis vert, des fauteuils, des cartes du royaume. C'est ici que le roi réunit ses ministres et prend ses décisions. Quatre objets bien éclairés, nettement séparés et lisibles : La table du Conseil (en haut à gauche); Le fauteuil du roi (en haut au centre); Le cadenas du Conseil (en haut à droite); La révocation (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #17101c et #33263d, lumières et accents #cfa86a, #ffd98a, touches #cdb8e8.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Gabriel — `gabriel`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Apprenti secrétaire au cabinet du roi, à Versailles, 12 ans, genre : garçon, cheveux courts, expression : jeune secrétaire zélé, un peu intimidé. Tenue en rapport avec son rôle (Apprenti secrétaire au cabinet du roi, à Versailles, 12 ans). Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Suzanne — `suzanne`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Imprimeuse protestante (huguenote), en 1598, genre : femme, cheveux longs, expression : imprimeuse courageuse, voix calme. Tenue en rapport avec son rôle (Imprimeuse protestante (huguenote), en 1598). Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Mathurin — `mathurin`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Boulanger catholique, voisin de Suzanne, en 1598, genre : homme, cheveux courts, expression : boulanger chaleureux, voisin fidèle. Tenue en rapport avec son rôle (Boulanger catholique, voisin de Suzanne, en 1598). Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Margot — `margot`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Aide-jardinière dans l'équipe d'André Le Nôtre, 11 ans, genre : fille, cheveux longs, expression : aide-jardinière malicieuse. Tenue en rapport avec son rôle (Aide-jardinière dans l'équipe d'André Le Nôtre, 11 ans). Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Dame Isabeau — `isabeau`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Dame de la cour de Louis XIV, genre : femme, cheveux longs, expression : dame de la cour, élégante et ironique. Tenue en rapport avec son rôle (Dame de la cour de Louis XIV). Peinture numérique semi-réaliste de cinéma, ambiance du Grand Siècle, lumière dorée contre ombres prune, marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `imprimerie`) : « Lent travelling avant dans Une imprimerie, dans une petite ville du royaume, en 1598. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `rue`) : « Lent travelling avant dans Une rue de la même ville, au printemps 1598. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `jardins`) : « Lent travelling avant dans Les jardins du château de Versailles, en 1682. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `chambre`) : « Lent travelling avant dans L'antichambre et la chambre du roi, au château de Versailles. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `conseil`) : « Lent travelling avant dans Le cabinet du Conseil, au château de Versailles. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.
