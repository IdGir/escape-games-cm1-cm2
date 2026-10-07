# Prompts Google Flow — Le Manuscrit de l'abbaye

Ces prompts produisent les images du jeu `immersifs/moyen-age-abbaye/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ. Haut et central Moyen Âge (Ve-XIIIe siècles) : Reims, le palais d'Aix, l'abbaye et son scriptorium, un hôtel-Dieu, un chantier d'église. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1d0d12 et #3a1c24, lumières et accents #d1a43a, #ffcf7a, touches #a8c4f0.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. Le baptême de Clovis — `reims`

**Lieu** : ⛪ Reims, la ville du baptême — la première page du livre. La page montre un roi agenouillé devant un évêque, près d'une cuve d'eau. Autour, des guerriers regardent. En haut de la page, une grande lettre attend ses couleurs. Sous le dessin, une ligne s'est effacée : celle qui raconte comment, après l'Empire romain, un roi a réuni une grande partie de la Gaule.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le parchemin du baptême** — La première page du livre : Clovis et son baptême. (énigme e1-1)
- en haut au centre : **La frise de la première page** — Une frise en bandes qui n'est pas dans l'ordre. (énigme e1-2)
- en haut à droite : **Les enluminures** — Des personnages à identifier : qui a fait quoi ? (énigme e1-3)
- au centre : **La carte du royaume** — Une carte à légender : le royaume des Francs. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : ⛪ Reims, la ville du baptême — la première page du livre. La page montre un roi agenouillé devant un évêque, près d'une cuve d'eau. Autour, des guerriers regardent. En haut de la page, une grande lettre attend ses couleurs. Sous le dessin, une ligne s'est effacée : celle qui raconte comment, après l'Empire romain, un roi a réuni une grande partie de la Gaule. Quatre objets bien éclairés, nettement séparés et lisibles : Le parchemin du baptême (en haut à gauche); La frise de la première page (en haut au centre); Les enluminures (en haut à droite); La carte du royaume (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1d0d12 et #3a1c24, lumières et accents #d1a43a, #ffcf7a, touches #a8c4f0.
```

### 2. La cour de Charlemagne — `aix`

**Lieu** : 👑 Aix-la-Chapelle, le palais de Charlemagne — la deuxième page. Sur la page, un homme couronné est assis. Devant lui, des enfants tiennent des tablettes de cire. Plus loin, une chapelle ronde coiffée d'une coupole. Une carte occupe le bas de la page : elle va de l'océan aux grands fleuves de l'est, mais ses noms ont été grattés.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La galerie du palais** — De Clovis à Charlemagne, une longue lignée. (énigme e2-1)
- en haut au centre : **La couronne sur le coussin** — La couronne de l'an 800 sur un coussin de velours. (énigme e2-2)
- en haut à droite : **La carte de l'empire** — Les frontières de l'empire de Charlemagne. (énigme e2-3)
- au centre : **La page cachée** — Un mot caché dans la deuxième page. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 👑 Aix-la-Chapelle, le palais de Charlemagne — la deuxième page. Sur la page, un homme couronné est assis. Devant lui, des enfants tiennent des tablettes de cire. Plus loin, une chapelle ronde coiffée d'une coupole. Une carte occupe le bas de la page : elle va de l'océan aux grands fleuves de l'est, mais ses noms ont été grattés. Quatre objets bien éclairés, nettement séparés et lisibles : La galerie du palais (en haut à gauche); La couronne sur le coussin (en haut au centre); La carte de l'empire (en haut à droite); La page cachée (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1d0d12 et #3a1c24, lumières et accents #d1a43a, #ffcf7a, touches #a8c4f0.
```

### 3. Le scriptorium de l'abbaye — `scriptorium`

**Lieu** : 🕯️ Le scriptorium de l'abbaye — la troisième page. Des pupitres en bois alignés sous de hautes fenêtres. Ici, on travaille à la lumière du jour : le feu pourrait détruire les livres. Sur chaque pupitre, une peau tendue, une plume d'oie, un petit couteau, un encrier de corne. La page à refaire montre un moine penché sur son travail.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le pupitre du moine** — Une journée de moine rythmée par la prière et le travail. (énigme e3-1)
- en haut au centre : **Le livre en fabrication** — Peaux, plumes, encres : comment naît un livre. (énigme e3-2)
- en haut à droite : **La classe de l'abbaye** — Où apprend-on à lire ? À l'abbaye et à l'école du palais. (énigme e3-3)
- au centre : **Le cadenas de la bibliothèque** — Une serrure à chiffres pour les livres précieux. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🕯️ Le scriptorium de l'abbaye — la troisième page. Des pupitres en bois alignés sous de hautes fenêtres. Ici, on travaille à la lumière du jour : le feu pourrait détruire les livres. Sur chaque pupitre, une peau tendue, une plume d'oie, un petit couteau, un encrier de corne. La page à refaire montre un moine penché sur son travail. Quatre objets bien éclairés, nettement séparés et lisibles : Le pupitre du moine (en haut à gauche); Le livre en fabrication (en haut au centre); La classe de l'abbaye (en haut à droite); Le cadenas de la bibliothèque (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1d0d12 et #3a1c24, lumières et accents #d1a43a, #ffcf7a, touches #a8c4f0.
```

### 4. L'hôtel-Dieu et l'aumône — `hoteldieu`

**Lieu** : 🕊️ L'hôtel-Dieu, près de l'abbaye — la quatrième page. Une très longue salle, des lits alignés le long des murs, une chapelle au fond pour que les malades puissent suivre la messe depuis leur lit. À la porte, des pauvres attendent la distribution du pain. La page à refaire montre cette file, et une main qui donne.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les registres de l'hôtel-Dieu** — Les registres de l'aide aux pauvres et aux malades. (énigme e4-1)
- en haut au centre : **Le tronc de l'aumône** — Le tronc où l'on dépose l'aumône. (énigme e4-2)
- en haut à droite : **La porte de l'hôtel-Dieu** — Les pauvres, les malades, les pèlerins : où les envoyer ? (énigme e4-3)
- au centre : **Le tableau des mots** — Les mots de la charité à associer. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🕊️ L'hôtel-Dieu, près de l'abbaye — la quatrième page. Une très longue salle, des lits alignés le long des murs, une chapelle au fond pour que les malades puissent suivre la messe depuis leur lit. À la porte, des pauvres attendent la distribution du pain. La page à refaire montre cette file, et une main qui donne. Quatre objets bien éclairés, nettement séparés et lisibles : Les registres de l'hôtel-Dieu (en haut à gauche); Le tronc de l'aumône (en haut au centre); La porte de l'hôtel-Dieu (en haut à droite); Le tableau des mots (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1d0d12 et #3a1c24, lumières et accents #d1a43a, #ffcf7a, touches #a8c4f0.
```

### 5. L'église romane et la cathédrale gothique — `chantier`

**Lieu** : ⛏️ Le chantier, entre l'église de l'abbaye et la cathédrale neuve — la cinquième page. À gauche, l'église de l'abbaye : trapue, des murs épais, de petites fenêtres, des arcs arrondis. À droite, le chantier de la cathédrale : des échafaudages, des arcs pointus, d'immenses fenêtres de verre coloré. La dernière page doit montrer les deux.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les deux églises** — Une église romane et une cathédrale gothique à légender. (énigme e5-1)
- en haut au centre : **Le tas de matériaux** — Un objet qui n'a rien à faire sur le chantier. (énigme e5-2)
- en haut à droite : **Les voûtes** — Arc en plein cintre ou arc brisé : roman ou gothique ? (énigme e5-3)
- au centre : **Le plan du maître d'œuvre** — Le plan de la cathédrale et celui qui le dirige. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : ⛏️ Le chantier, entre l'église de l'abbaye et la cathédrale neuve — la cinquième page. À gauche, l'église de l'abbaye : trapue, des murs épais, de petites fenêtres, des arcs arrondis. À droite, le chantier de la cathédrale : des échafaudages, des arcs pointus, d'immenses fenêtres de verre coloré. La dernière page doit montrer les deux. Quatre objets bien éclairés, nettement séparés et lisibles : Les deux églises (en haut à gauche); Le tas de matériaux (en haut au centre); Les voûtes (en haut à droite); Le plan du maître d'œuvre (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #1d0d12 et #3a1c24, lumières et accents #d1a43a, #ffcf7a, touches #a8c4f0.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Frère Anselme — `anselme`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Moine copiste de l'abbaye, genre : homme, cheveux absents, expression : moine copiste, doux et érudit. Tenue en rapport avec son rôle (Moine copiste de l'abbaye). Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Aude — `aude`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Élève de l'école du palais d'Aix, 11 ans, genre : fille, cheveux longs, expression : élève curieuse, parle vite. Tenue en rapport avec son rôle (Élève de l'école du palais d'Aix, 11 ans). Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Mère Alix — `alix`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Abbesse, responsable de l'hôtel-Dieu, genre : femme, cheveux courts, expression : abbesse ferme et bienveillante. Tenue en rapport avec son rôle (Abbesse, responsable de l'hôtel-Dieu). Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Garin — `garin`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Apprenti tailleur de pierre, 12 ans, genre : garçon, cheveux courts, expression : apprenti tailleur de pierre, franc et fier de son métier. Tenue en rapport avec son rôle (Apprenti tailleur de pierre, 12 ans). Peinture numérique semi-réaliste de cinéma, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `reims`) : « Lent travelling avant dans ⛪ Reims, la ville du baptême — la première page du livre. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `aix`) : « Lent travelling avant dans 👑 Aix-la-Chapelle, le palais de Charlemagne — la deuxième page. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `scriptorium`) : « Lent travelling avant dans 🕯️ Le scriptorium de l'abbaye — la troisième page. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `hoteldieu`) : « Lent travelling avant dans 🕊️ L'hôtel-Dieu, près de l'abbaye — la quatrième page. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `chantier`) : « Lent travelling avant dans ⛏️ Le chantier, entre l'église de l'abbaye et la cathédrale neuve — la cinquième page. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.
