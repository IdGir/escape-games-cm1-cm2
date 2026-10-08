# Prompts Google Flow — Le Sceau de la République

Ces prompts produisent les images du jeu `immersifs/constitution/`. Les décors servent aussi de **premières images des vidéos** (Agnes).

## Mode d'emploi

1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.
2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).
3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.
4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.
5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.
6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source "Google Flow" --licence "…"`.

## Charte (à ajouter à chaque prompt)

> Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ. Univers contemporain : le Palais-Royal, la salle des textes, l'hémicycle, le Sénat et la salle des séances du Conseil constitutionnel. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0c1226 et #1d2a4a, lumières et accents #c9302c, #ffd27a, touches #b9cdfa.
>
> Éviter : texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, personne réelle ou célébrité, peinture, illustration, dessin, rendu 3D, aspect plastique, style dessin animé, violence, sang.

Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).

## Décors (16:9, 1920 × 1080)

### 1. La cour du Palais-Royal — `cour`

**Lieu** : 🏛️ La cour du Palais-Royal, à Paris — aujourd'hui. C'est ici, dans cette cour, que des apprentis ont un jour cherché un article volé de la Déclaration des droits de l'homme et du citoyen. Deux siècles plus tard, le même lieu abrite le Conseil constitutionnel. Sous les galeries, un vieux coffre de bois attend, posé sur un chariot.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **La grille de la cour** — La grille du Palais-Royal : on entre ici pour comprendre les règles. (énigme e1-1)
- en haut au centre : **Les affiches du hall** — Des affiches qui disent vrai ou faux sur la Constitution. (énigme e1-2)
- en haut à droite : **Les trois bustes** — Trois statues, trois pouvoirs : faire la loi, l'appliquer, juger. (énigme e1-3)
- au centre : **La première serrure** — Une serrure à lettres gravées. (énigme e1-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🏛️ La cour du Palais-Royal, à Paris — aujourd'hui. C'est ici, dans cette cour, que des apprentis ont un jour cherché un article volé de la Déclaration des droits de l'homme et du citoyen. Deux siècles plus tard, le même lieu abrite le Conseil constitutionnel. Sous les galeries, un vieux coffre de bois attend, posé sur un chariot. Quatre objets bien éclairés, nettement séparés et lisibles : La grille de la cour (en haut à gauche); Les affiches du hall (en haut au centre); Les trois bustes (en haut à droite); La première serrure (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0c1226 et #1d2a4a, lumières et accents #c9302c, #ffd27a, touches #b9cdfa.
```

### 2. La salle des Textes — `archives`

**Lieu** : 📜 La salle des Textes — premier étage. Des rayonnages jusqu'au plafond, une seule lampe, et au centre une vitrine. Sous le verre : quatre documents, datés 1789, 1946, 1958 et 2004. Une plaque de cuivre indique « Bloc de constitutionnalité ».

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Les quatre textes sous vitrine** — Quatre textes fondateurs, à ranger du plus ancien au plus récent. (énigme e2-1)
- en haut au centre : **Le tableau des apports** — Chaque texte apporte quelque chose de précis. (énigme e2-2)
- en haut à droite : **La fiche d'identité** — La fiche d'identité de la Constitution à compléter. (énigme e2-3)
- au centre : **Le cadenas du coffre des textes** — Un cadenas à chiffres sur le coffre. (énigme e2-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 📜 La salle des Textes — premier étage. Des rayonnages jusqu'au plafond, une seule lampe, et au centre une vitrine. Sous le verre : quatre documents, datés 1789, 1946, 1958 et 2004. Une plaque de cuivre indique « Bloc de constitutionnalité ». Quatre objets bien éclairés, nettement séparés et lisibles : Les quatre textes sous vitrine (en haut à gauche); Le tableau des apports (en haut au centre); La fiche d'identité (en haut à droite); Le cadenas du coffre des textes (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0c1226 et #1d2a4a, lumières et accents #c9302c, #ffd27a, touches #b9cdfa.
```

### 3. L'hémicycle — `hemicycle`

**Lieu** : 🏛️ L'hémicycle de l'Assemblée nationale — Palais-Bourbon. Les bancs rouges montent en gradins autour de la tribune. Au-dessus du perchoir, les lettres « RF ». Le tableau de vote s'allume : vert, blanc, rouge. Pour l'instant, la salle est vide.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le plan de l'hémicycle** — Un plan qui montre qui siège où et qui fait quoi. (énigme e3-1)
- en haut au centre : **Le fauteuil du président** — Le fauteuil du président de la République. (énigme e3-2)
- en haut à droite : **L'urne du bureau de vote** — Une urne et un isoloir : tout n'est pas à sa place. (énigme e3-3)
- au centre : **Le tableau des présidents** — Les portraits des présidents de la Ve République. (énigme e3-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🏛️ L'hémicycle de l'Assemblée nationale — Palais-Bourbon. Les bancs rouges montent en gradins autour de la tribune. Au-dessus du perchoir, les lettres « RF ». Le tableau de vote s'allume : vert, blanc, rouge. Pour l'instant, la salle est vide. Quatre objets bien éclairés, nettement séparés et lisibles : Le plan de l'hémicycle (en haut à gauche); Le fauteuil du président (en haut au centre); L'urne du bureau de vote (en haut à droite); Le tableau des présidents (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0c1226 et #1d2a4a, lumières et accents #c9302c, #ffd27a, touches #b9cdfa.
```

### 4. La navette parlementaire — `senat`

**Lieu** : 🏛️ Entre le Palais-Bourbon et le palais du Luxembourg. Deux palais, un jardin, un bassin. Entre les deux, un dossier voyage sans cesse : l'Assemblée nationale l'amende, le Sénat le modifie, il revient. C'est ce que l'on appelle la navette.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le dictionnaire de la loi** — Les mots de la loi : projet, proposition, amendement, vote. (énigme e4-1)
- en haut au centre : **La navette entre les deux assemblées** — Un texte fait des allers-retours entre deux chambres. (énigme e4-2)
- en haut à droite : **Les dossiers du Parlement** — Des dossiers à vérifier : vrai ou faux. (énigme e4-3)
- au centre : **Le cadenas du Parlement** — Un cadenas sur la porte de l'assemblée. (énigme e4-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : 🏛️ Entre le Palais-Bourbon et le palais du Luxembourg. Deux palais, un jardin, un bassin. Entre les deux, un dossier voyage sans cesse : l'Assemblée nationale l'amende, le Sénat le modifie, il revient. C'est ce que l'on appelle la navette. Quatre objets bien éclairés, nettement séparés et lisibles : Le dictionnaire de la loi (en haut à gauche); La navette entre les deux assemblées (en haut au centre); Les dossiers du Parlement (en haut à droite); Le cadenas du Parlement (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0c1226 et #1d2a4a, lumières et accents #c9302c, #ffd27a, touches #b9cdfa.
```

### 5. La salle des séances du Conseil constitutionnel — `conseil`

**Lieu** : ⚖️ La salle des séances — Conseil constitutionnel, Palais-Royal. Neuf fauteuils rouges en fer à cheval, une table sombre, des dossiers posés. Gravée au-dessus des boiseries : « Liberté, Égalité, Fraternité ». C'est ici que l'on vérifie qu'une loi respecte la Constitution.

**Les objets des énigmes** (un par énigme, bien séparés) :

- en haut à gauche : **Le texte des articles 1 et 2** — Les premiers articles de la Constitution à compléter. (énigme e5-1)
- en haut au centre : **La devise gravée** — Les valeurs et principes de la République. (énigme e5-2)
- en haut à droite : **Le journal du quotidien** — Un journal montre comment la Constitution touche notre vie. (énigme e5-3)
- au centre : **La fiche du Conseil** — La fiche d'identité du Conseil constitutionnel. (énigme e5-4)

**Prompt**

```
Décor d'escape game pour enfants, plan large 16:9 : ⚖️ La salle des séances — Conseil constitutionnel, Palais-Royal. Neuf fauteuils rouges en fer à cheval, une table sombre, des dossiers posés. Gravée au-dessus des boiseries : « Liberté, Égalité, Fraternité ». C'est ici que l'on vérifie qu'une loi respecte la Constitution. Quatre objets bien éclairés, nettement séparés et lisibles : Le texte des articles 1 et 2 (en haut à gauche); La devise gravée (en haut au centre); Le journal du quotidien (en haut à droite); La fiche du Conseil (au centre). Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ. Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond #0c1226 et #1d2a4a, lumières et accents #c9302c, #ffd27a, touches #b9cdfa.
```

## Portraits (3:4, 1200 × 1600)

Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).

### Monsieur Berthier — `berthier`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Gardien-archiviste du Palais-Royal, genre : homme, cheveux absents, porte des lunettes, expression : gardien solennel et attentif aux détails. Tenue en rapport avec son rôle (Gardien-archiviste du Palais-Royal). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Nour — `nour`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Déléguée de classe, 10 ans, genre : fille, cheveux longs, expression : déléguée de classe vive et sérieuse. Tenue en rapport avec son rôle (Déléguée de classe, 10 ans). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Madame Ferrand — `ferrand`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Députée à l'Assemblée nationale, genre : femme, cheveux courts, expression : députée claire, passionnée de débat. Tenue en rapport avec son rôle (Députée à l'Assemblée nationale). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ.
```

### Maître Sylla — `sylla`

```
Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : Juriste au Conseil constitutionnel, genre : homme, cheveux courts, porte des lunettes, expression : juriste précis, mesure chaque mot. Tenue en rapport avec son rôle (Juriste au Conseil constitutionnel). Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ.
```

## Vidéos (Agnes, à partir des images)

Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. Prompt de mouvement (court, calme, sans texte) :

- `transition-e1` (départ : `cour`) : « Lent travelling avant dans 🏛️ La cour du Palais-Royal, à Paris — aujourd'hui. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e2` (départ : `archives`) : « Lent travelling avant dans 📜 La salle des Textes — premier étage. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e3` (départ : `hemicycle`) : « Lent travelling avant dans 🏛️ L'hémicycle de l'Assemblée nationale — Palais-Bourbon. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e4` (départ : `senat`) : « Lent travelling avant dans 🏛️ Entre le Palais-Bourbon et le palais du Luxembourg. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `transition-e5` (départ : `conseil`) : « Lent travelling avant dans ⚖️ La salle des séances — Conseil constitutionnel, Palais-Royal. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »
- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).
- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.
- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.

## Ambiances et musiques (fichiers libres de droits)

Le moteur joue des fichiers mp3 s'ils existent, sinon l'ambiance synthétisée. Sources libres conseillées : Pixabay (sons et musiques), Freesound (CC0 ou CC BY), Free Music Archive, Incompetech (CC BY), YouTube Audio Library. Vérifier la licence, noter auteur + licence + URL dans `assets/audio/CREDITS-audio.md`. Boucles d'ambiance : 30 à 90 s, sans début ni fin marqués. Musiques : instrumentales, sans voix, 20 à 60 s (elles se coupent en fondu à la fin de la cinématique).

| Fichier à déposer | Rôle | Mots-clés de recherche |
|---|---|---|
| `assets/audio/ambiances/cour.mp3` | Ambiance de la salle 1 (boucle, discrète) | ambiance sonore « 🏛️ La cour du Palais-Royal, à Paris — aujourd'hui », sans voix ni musique |
| `assets/audio/ambiances/archives.mp3` | Ambiance de la salle 2 (boucle, discrète) | ambiance sonore « 📜 La salle des Textes — premier étage », sans voix ni musique |
| `assets/audio/ambiances/hemicycle.mp3` | Ambiance de la salle 3 (boucle, discrète) | ambiance sonore « 🏛️ L'hémicycle de l'Assemblée nationale — Palais-Bourbon », sans voix ni musique |
| `assets/audio/ambiances/senat.mp3` | Ambiance de la salle 4 (boucle, discrète) | ambiance sonore « 🏛️ Entre le Palais-Bourbon et le palais du Luxembourg », sans voix ni musique |
| `assets/audio/ambiances/conseil.mp3` | Ambiance de la salle 5 (boucle, discrète) | ambiance sonore « ⚖️ La salle des séances — Conseil constitutionnel, Palais-Royal », sans voix ni musique |
| `assets/audio/musiques/intro.mp3` | Cinématique d'ouverture | musique instrumentale de cinéma, mystérieuse, qui s'installe |
| `assets/audio/musiques/transition.mp3` | Toutes les transitions entre salles (ou un fichier `transition-e<N>.mp3` par salle) | musique instrumentale douce, en avancée, curieuse |
| `assets/audio/musiques/fin-salle.mp3` | Fins de salle (ou `fin-e<N>.mp3`) | courte musique de réussite, lumineuse et apaisée |
| `assets/audio/musiques/fin.mp3` | Cinématique finale | musique instrumentale de conclusion, triomphante puis calme |

Réglages des élèves : « Sons et ambiances » (déjà présent) ; volumes par défaut 0,35 (ambiance) et 0,5 (musique), modifiables avec `VML.reglage("volumeAmbiance")` et `VML.reglage("volumeMusique")`.
