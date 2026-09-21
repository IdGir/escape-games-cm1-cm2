# Le Laboratoire de Madame Mélange

**Escape game de sciences — CM1 / CM2 — la matière : masses, mélanges et séparation des constituants**  
60 à 75 minutes · équipes de 3-4 élèves, ou classe entière au TBI · **15 énigmes en CM1, 20 en CM2**.

> Lila, l'apprentie de Madame Mélange, a trébuché : toutes les fioles du laboratoire se sont renversées.
> Madame Mélange part à la retraite et lui a confié son testament de chimiste, un protocole en cinq
> opérations pour retrouver ses échantillons. Mais la page est effacée : chaque salle du laboratoire
> en cache une opération.

Progression de l'enseignant : **sciences, Année B, période 1**. Suite prévue : jeu n°10 (états de la matière).

| | |
|---|---|
| **Jouer** | [en ligne](https://idgir.github.io/escape-games-cm1-cm2/melanges/) · en local : http://127.0.0.1:8000/melanges/ (avec `lancer.bat`) |
| **Tableau de bord** | http://127.0.0.1:8000/melanges/prof.html — mode local uniquement |
| **Vérifier** | [page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#melanges) : tester chaque énigme, voir les médias |
| **Médias** | [assets/README.md](assets/README.md) : tous les noms de fichiers attendus |
| **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) : programmes, déroulés, différenciation, évaluation |

Lancement, vérification et dépôt des médias : voir le [README principal](../README.md).

---

## Les 5 salles

| # | Lieu | Notion | Personnage | Mot-clé | Énigmes | Tester |
|---|---|---|---|---|---|---|
| 1 | La salle des balances | Mesurer et comparer des masses | Lila | **PESER** | 3 en CM1 · 4 en CM2 | [CM1](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=1&niveau=CM1) · [CM2](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=1&niveau=CM2) |
| 2 | La cuisine d'essai | La masse se conserve | Marius | **COMPARER** | 3 en CM1 · 4 en CM2 | [CM1](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=2&niveau=CM1) · [CM2](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=2&niveau=CM2) |
| 3 | La salle des fioles | Mélanges homogènes et hétérogènes | Lila | **OBSERVER** | 3 en CM1 · 4 en CM2 | [CM1](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=3&niveau=CM1) · [CM2](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=3&niveau=CM2) |
| 4 | L'atelier de tri | Séparer un mélange de solides | Nadia | **AIMANTER** | 3 en CM1 · 4 en CM2 | [CM1](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=4&niveau=CM1) · [CM2](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=4&niveau=CM2) |
| 5 | La saline | Séparer un solide d'un liquide | Yann | **ÉVAPORER** | 3 en CM1 · 4 en CM2 | [CM1](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=5&niveau=CM1) · [CM2](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=5&niveau=CM2) |
| Fin | Le testament complet, badges, quizz | | Madame Mélange | | | [CM1](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=6&niveau=CM1) · [CM2](https://idgir.github.io/escape-games-cm1-cm2/melanges/?salle=6&niveau=CM2) |

**Le mécanisme final.** Les cinq mots-clés sont les cinq opérations du testament. Ils ne sont pas trouvés dans l'ordre du protocole : la dernière énigme (5-4) demande de les remettre dans l'ordre, en lisant le testament. Le protocole : **PESER → OBSERVER → AIMANTER → ÉVAPORER → COMPARER**. Il sépare le dernier bocal de Madame Mélange (500 g d'eau, 30 g de sel dissous, 20 g de limaille de fer) et prouve que la masse des solides est conservée : 20 g + 30 g = 50 g.

Les liens « Tester » ouvrent la salle directement, sans nom d'équipe ; **rien n'est sauvegardé**. On peut aussi viser une énigme précise : `melanges/?salle=5&niveau=CM2&enigme=4`.

---

## Énigmes et solutions

<details>
<summary>Solutions — à ne pas projeter en classe</summary>


### Salle 1 — La salle des balances — mot-clé PESER

Leçon : « Mesurer et comparer des masses ».

#### 1-1 · Du plus léger au plus lourd — `ordre` — CM1 et CM2

*CM1*

1. La fiole jaune (95 g)
2. La fiole verte (150 g)
3. La fiole bleue (305 g)
4. La fiole rouge (530 g)

*CM2*

1. La fiole jaune (95 g)
2. La fiole violette (0,2 kg)
3. La fiole verte (250 g)
4. Le bocal bleu (1,05 kg)
5. Le bocal rouge (1 200 g)

*Correction affichée :* Pour comparer des masses, on les écrit dans la même unité. 1 kg = 1 000 g : donc 0,2 kg = 200 g et 1,05 kg = 1 050 g. Ensuite, on compare les nombres comme d'habitude.

*Source :* Programme de sciences et technologie du cycle 3 (BO 2026) — la matière : masse, mélanges

#### 1-2 · Deux balances, deux façons de peser — `qcm` — CM1 et CM2

*CM1*

- Sur une balance à deux plateaux, le plateau qui descend porte… → **l'objet le plus lourd**
- La balance électronique affiche « 250 g ». Que veut dire « g » ? → **gramme**
- Les plateaux sont à l'équilibre : à gauche une pomme, à droite des masses de 100 g, 50 g et 20 g. La pomme pèse… → **170 g**

*CM2*

- À l'équilibre, un flacon est d'un côté ; de l'autre, des masses de 200 g, 50 g, 20 g et 5 g. Le flacon pèse… → **275 g**
- À quoi sert la touche « tare » (ou « zéro ») d'une balance électronique ? → **À remettre l'affichage à zéro avec le récipient posé, pour ne peser que ce qu'on y verse**
- Un litre d'eau et un litre d'huile ont-ils la même masse ? → **Non : le litre d'huile est plus léger**

*Correction affichée :* La balance à plateaux compare deux masses : le plateau le plus chargé descend, et les plateaux sont à la même hauteur quand les masses sont égales (c'est l'équilibre). La balance électronique affiche directement la masse, en grammes. Sa touche « tare » (ou « zéro ») remet l'affichage à zéro quand le récipient est posé : on ne pèse alors que ce que l'on y verse.

*Source :* Programme de sciences et technologie du cycle 3 (BO 2026) — la matière : masse, mélanges

#### 1-3 · Peser un liquide — `code` — CM1 et CM2

*CM1*

- L'eau du bécher (bécher vide 80 g, plein 330 g) → **250**
- Le sirop de la bouteille (bouteille vide 400 g, pleine 1 150 g) → **750**

*CM2*

- L'eau : bécher vide 85 g, bécher plein 335 g → **250**
- Un litre d'huile : flacon vide 0,3 kg, flacon plein 1 220 g → **920**
- Le sucre : bol vide 150 g, bol avec le sucre 225 g → **75**

*Correction affichée :* Masse du liquide = masse du récipient plein − masse du récipient vide. La touche « tare » d'une balance électronique fait ce calcul à notre place.

*Source :* Programme de sciences et technologie du cycle 3 (BO 2026) — la matière : masse, mélanges

#### 1-4 · Les unités de masse — `trous` — CM2 seulement

Dans l'ordre : **gramme**, **kilogramme**, **1 000**, **tonnes**, **milligramme**, **volume**.
Étiquettes pièges : mètre, 100, centimètre.

*Correction affichée :* Le gramme (g) est l'unité de base. 1 kg = 1 000 g ; 1 t = 1 000 kg ; 1 g = 1 000 mg. Le litre (L) mesure un volume, c'est-à-dire la place occupée : ce n'est pas une unité de masse.

*Source :* Programme de sciences et technologie du cycle 3 (BO 2026) — la matière : masse, mélanges


### Salle 2 — La cuisine d'essai — mot-clé COMPARER

Leçon : « La masse se conserve ».

#### 2-1 · Le sucre a-t-il disparu ? — `vraifaux` — CM1 et CM2

*CM1*

- Quand on met du sucre dans l'eau et qu'on remue, le sucre disparaît : il n'existe plus. → **Faux**
- Un verre d'eau de 200 g et un morceau de sucre de 6 g : après avoir remué, la balance affiche 206 g. → **Vrai**
- Pour savoir s'il y a du sucre dans l'eau, on peut la goûter. → **Faux**
- Le sable se dissout dans l'eau, comme le sucre. → **Faux**

*CM2*

- Quand on dissout du sucre dans l'eau, le sucre disparaît : il n'existe plus. → **Faux**
- 250 g d'eau et 20 g de sel : après dissolution, la balance affiche 270 g. → **Vrai**
- Après la dissolution, le mélange est plus léger, car le sel a fondu. → **Faux**
- On peut dissoudre autant de sel que l'on veut dans un verre d'eau. → **Faux**
- Pour vérifier qu'il y a du sel dans l'eau, on la goûte. → **Faux**
- Si on laisse l'eau salée s'évaporer, on retrouve le sel. → **Vrai**

*Correction affichée :* Le sucre et le sel ne disparaissent pas dans l'eau : ils se dissolvent. On ne les voit plus, mais ils sont toujours là, et la balance le prouve : la masse totale ne change pas. Au laboratoire, on ne goûte jamais pour vérifier.

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)

#### 2-2 · Le cahier taché de Marius — `plan` — CM1 et CM2

*CM1*

- 1. Le verre d'eau, seul sur la balance → **200 g**
- 2. Le sucre, pesé dans une coupelle tarée → **20 g**
- 3. Le sucre est versé dans l'eau, on remue : la balance affiche… → **220 g**
- 4. Ce qui est arrivé au sucre → **il s'est dissous**
Étiquettes pièges : 180 g, il a disparu.

*CM2*

- 1. Le verre d'eau, seul → **250 g**
- 2. Le sucre, pesé seul → **15 g**
- 3. L'eau sucrée, après avoir remué → **265 g**
- 4. Ce qui est arrivé au sucre → **dissous**
- 5. Le mélange obtenu est… → **homogène**
Étiquettes pièges : 280 g, fondu, hétérogène.

*Correction affichée :* Masse de l'eau + masse du sucre = masse de l'eau sucrée. Le sucre s'est dissous : on ne le voit plus, mais sa masse est toujours là. L'eau sucrée est un mélange homogène.

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)

#### 2-3 · Le café de Marius — `qcm` — CM1 et CM2

*CM1*

- La tasse de café pèse 180 g. Marius ajoute un sucre de 5 g et remue. La balance affiche… → **185 g**
- Où est passé le sucre ? → **Il est toujours dans le café, en morceaux trop petits pour être vus**
- Quelle phrase est juste ? → **L'air est de la matière : il a une masse**

*CM2*

- La tasse de café pèse 180 g. Marius ajoute deux sucres de 5 g chacun et remue. La balance affiche… → **190 g**
- Sur une balance précise, un ballon dégonflé pèse 420 g. On le gonfle bien. Il pèse maintenant… → **un peu plus de 420 g, car l'air a une masse**
- Pourquoi ne voit-on plus le sucre dans le café ? → **Il s'est séparé en morceaux si petits qu'on ne les voit plus, même à la loupe**

*Correction affichée :* Tout ce qui est matière a une masse : le sucre dissous, mais aussi l'air. Quand on ajoute un sucre dans une tasse, la balance augmente de la masse du sucre, même quand on ne le voit plus.

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)

#### 2-4 · Le cadenas de la cuisine — `code` — CM2 seulement

- 300 g d'eau + 30 g de sel, après dissolution → **330**
- Bol d'eau sucrée : 420 g. Le bol vide pèse 150 g, le sucre 20 g. Masse de l'eau ? → **250**
- On fait évaporer toute l'eau salée du premier nombre. Masse de sel retrouvée ? → **30**

*Correction affichée :* La masse se conserve : 300 g d'eau + 30 g de sel = 330 g d'eau salée. Pour l'eau du bol : 420 − 150 − 20 = 250 g. Et quand toute l'eau s'évapore, on retrouve exactement les 30 g de sel.

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)


### Salle 3 — La salle des fioles — mot-clé OBSERVER

Leçon : « Mélanges homogènes et hétérogènes ».

#### 3-1 · Homogène ou hétérogène ? — `tri` — CM1 et CM2

*CM1*

- **Homogène : je ne vois qu'une seule chose** : Eau salée, Sirop de menthe à l'eau, Eau sucrée
- **Hétérogène : je vois au moins deux choses** : Eau et huile, Eau et sable, Jus d'orange avec pulpe

*CM2*

- **Mélange homogène** : Eau salée, Sirop à l'eau, Eau du robinet, Air
- **Mélange hétérogène** : Eau et huile, Eau boueuse, Vinaigrette, Jus d'orange avec pulpe, Riz et semoule

*Correction affichée :* Dans un mélange homogène, on ne distingue pas les constituants à l'œil nu : eau salée, eau sucrée, sirop à l'eau, eau du robinet, air. Dans un mélange hétérogène, on voit au moins deux constituants : eau et huile, eau et sable, vinaigrette, jus avec pulpe, eau boueuse.

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)

#### 3-2 · L'intrus de l'étagère — `intrus` — CM1 et CM2

*CM1*

Intrus : **Eau et sable**.

*CM2*

Intrus : **Vinaigrette**.

*Correction affichée :* L'intrus est le seul mélange hétérogène : on y distingue deux constituants à l'œil nu. Tous les autres sont homogènes, même quand on n'y voit « que de l'eau » ou « rien du tout ».

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)

#### 3-3 · Ce que l'on observe — `association` — CM1 et CM2

*CM1*

- Eau et huile ↔ **Deux couches : l'huile reste au-dessus**
- Eau et sable ↔ **Les grains tombent au fond**
- Eau salée ↔ **Un liquide transparent : on ne voit pas le sel**

*CM2*

- Eau et huile ↔ **Deux couches : pour un même volume, l'huile est plus légère que l'eau**
- Eau boueuse ↔ **Trouble ; au repos, la terre se dépose au fond**
- Sirop à l'eau ↔ **Coloré mais uniforme : le même aspect partout**
- Air ↔ **Invisible, mais il a une masse et occupe de la place**

*Correction affichée :* Observer, c'est la première étape d'une séparation : on regarde si l'on distingue les constituants, s'ils flottent, s'ils tombent au fond, ou si le mélange est pareil partout. C'est ce qui permet de choisir la bonne méthode.

*Source :* Cité des sciences et de l'industrie / Lumni — ressources sur les mélanges et la séparation

#### 3-4 · Les idées fausses de Lila — `vraifaux` — CM2 seulement

- L'eau salée n'est pas un mélange, puisqu'on ne voit qu'un seul liquide. → **Faux**
- L'air n'est pas de la matière. → **Faux**
- Du sel dans l'eau : juste avant de remuer, le mélange est hétérogène ; une fois le sel dissous, il est homogène. → **Vrai**
- L'eau du robinet est de l'eau pure. → **Faux**
- Dans une vinaigrette laissée au repos, l'huile remonte à la surface. → **Vrai**
- Pour savoir ce que contient une fiole, on ne la goûte pas et on ne la sent pas : on observe et on mesure. → **Vrai**

*Correction affichée :* L'eau salée est un mélange homogène. L'air est de la matière : c'est un mélange de gaz qui a une masse (environ 1,2 g par litre à 20 °C). L'eau du robinet contient des sels minéraux dissous. Un mélange de sel et d'eau est hétérogène tant que le sel n'est pas dissous, puis homogène.

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)


### Salle 4 — L'atelier de tri — mot-clé AIMANTER

Leçon : « Séparer un mélange de solides ».

#### 4-1 · Une méthode pour chaque mélange — `association` — CM1 et CM2

*CM1*

- Limaille de fer et sable ↔ **L'aimant**
- Gravier et sable fin ↔ **Le tamis**
- Sciure de bois et sable ↔ **Une bassine d'eau**
- Boutons rouges et boutons bleus ↔ **Le tri à la main**

*CM2*

- Limaille de fer et sable ↔ **Aimantation : seul le fer est attiré par l'aimant**
- Gravier et sable fin ↔ **Tamisage : les grains fins passent, les gros restent**
- Sciure de bois et sable ↔ **Flottation : dans l'eau, la sciure flotte et le sable coule**
- Boutons rouges et boutons bleus ↔ **Tri à la main : seule la couleur les distingue**

*Correction affichée :* Chaque méthode utilise une différence entre les constituants : la taille (tamisage), le fer attiré par l'aimant (aimantation), le fait de flotter ou de couler (flottation), ou simplement ce que l'on voit (tri à la main).

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)

#### 4-2 · Pas à pas — `ordre` — CM1 et CM2

*CM1*

1. Poser le tamis au-dessus d'une bassine vide
2. Verser le mélange de gravier et de sable dans le tamis
3. Secouer doucement le tamis
4. Le sable est dans la bassine, le gravier est resté dans le tamis

*CM2*

1. Verser le mélange de sciure et de sable dans une bassine d'eau
2. Remuer, puis attendre quelques instants
3. Observer : la sciure flotte, le sable est au fond
4. Récupérer la sciure à la surface avec une passoire
5. Laisser sécher la sciure sur du papier journal

*Correction affichée :* Une séparation se fait toujours dans un ordre logique : préparer le matériel, mettre le mélange, agir, observer, récupérer chaque constituant.

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)

#### 4-3 · Ce que l'aimant attire — `qcm` — CM1 et CM2

*CM1*

- Un aimant attire… → **les objets en fer**
- Une canette en aluminium est-elle attirée par l'aimant ? → **Non : l'aluminium n'est pas attiré**
- Pour séparer la limaille de fer du sable, on utilise… → **un aimant**

*CM2*

- Lequel de ces objets l'aimant attire-t-il ? → **un trombone en acier**
- Pourquoi le tamis ne suffit-il pas à séparer la limaille de fer du sable ? → **Les grains ont à peu près la même taille**
- Dans un centre de tri des déchets, un gros aimant sert à… → **séparer les boîtes de conserve en acier des autres déchets**

*Correction affichée :* Un aimant attire le fer et les objets en acier (l'acier contient du fer). Il n'attire pas tous les métaux : l'aluminium, le cuivre ou l'or ne sont pas attirés. Dans les centres de tri, de gros aimants séparent les boîtes de conserve en acier des autres déchets.

*Source :* Cité des sciences et de l'industrie / Lumni — ressources sur les mélanges et la séparation

#### 4-4 · L'établi de Nadia — `plan` — CM2 seulement

- Bac A : boutons rouges et boutons bleus → **les mains**
- Bac B : farine pleine de grumeaux → **le tamis**
- Bac C : trombones en acier et perles en plastique → **l'aimant**
- Bac D : sciure de bois et sable → **la bassine d'eau**
Étiquettes pièges : le filtre, la balance.

*Correction affichée :* Bac A : seule la couleur distingue les boutons, on trie à la main. Bac B : les grumeaux sont plus gros que la farine, le tamis les retient. Bac C : les trombones en acier sont attirés par l'aimant, pas les perles. Bac D : dans l'eau, la sciure flotte et le sable coule.

*Source :* Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)


### Salle 5 — La saline — mot-clé ÉVAPORER

Leçon : « Séparer un solide d'un liquide ».

#### 5-1 · Filtrer, décanter, évaporer — `trous` — CM1 et CM2

*CM1*

Dans l'ordre : **décantation**, **filtre**, **reste**, **évaporer**.
Étiquettes pièges : aimant, fondre, tamis.

*CM2*

Dans l'ordre : **décantation**, **filtre**, **retenus**, **dissous**, **évaporer**, **35**.
Étiquettes pièges : fondu, 350, aimantation, tamisage.

*Correction affichée :* Décantation : on laisse reposer, le solide tombe au fond, on verse doucement le liquide. Filtration : le filtre retient les grains solides, le liquide passe. Mais un solide dissous, comme le sel, traverse le filtre : pour le récupérer, on fait évaporer l'eau. L'eau filtrée ne se boit pas pour autant.

*Source :* Programme de sciences et technologie du cycle 3 (BO 2026) — la matière : masse, mélanges

#### 5-2 · Le montage de filtration — `plan` — CM2 seulement

- En forme de cône, il guide le liquide → **l'entonnoir**
- Plié dans l'entonnoir, il retient les grains → **le papier filtre**
- Sous l'entonnoir, il recueille le liquide → **le bécher**
- Ce qui reste dans le filtre (eau salée + sable) → **le sable**
- Ce qui coule dans le bécher (eau salée + sable) → **l'eau salée**
- La méthode pour récupérer ensuite le sel → **l'évaporation**
Étiquettes pièges : l'eau pure, l'aimant, la décantation.

*Correction affichée :* L'entonnoir guide le liquide ; le papier filtre, plié en cône, retient les grains de sable ; le bécher recueille le liquide filtré. Si le mélange était de l'eau salée avec du sable, le sable reste dans le filtre et l'eau salée coule dans le bécher : on récupère ensuite le sel par évaporation.

*Source :* Programme de sciences et technologie du cycle 3 (BO 2026) — la matière : masse, mélanges

#### 5-3 · Le mot du paludier — `lettres` — CM1 et CM2

Mot : **ÉVAPORER**.

*Correction affichée :* ÉVAPORER : l'eau passe à l'état de vapeur et part dans l'air ; le sel, lui, reste. C'est ainsi que l'on récolte le sel de mer dans les marais salants.

*Source :* Cité des sciences et de l'industrie / Lumni — ressources sur les mélanges et la séparation

#### 5-4 · Le testament de Madame Mélange — `ordre` — CM1 et CM2

*CM1*

1. PESER (noter la masse du bocal au départ)
2. OBSERVER (regarder : on voit la limaille dans l'eau salée)
3. AIMANTER (retirer la limaille de fer)
4. ÉVAPORER (laisser partir l'eau : le sel reste)
5. COMPARER (vérifier que rien ne manque)

*CM2*

1. PESER (masse de départ : 550 g)
2. OBSERVER (mélange hétérogène : la limaille se voit ; l'eau salée est homogène)
3. AIMANTER (on récupère les 20 g de limaille)
4. ÉVAPORER (la vapeur emporte l'eau ; il reste 30 g de sel)
5. COMPARER (20 g + 30 g = 50 g : la masse des solides est conservée)

*Correction affichée :* Le protocole : PESER le bocal au départ, OBSERVER le mélange (on voit la limaille : il est hétérogène ; l'eau salée, elle, est homogène), AIMANTER pour retirer le fer, ÉVAPORER l'eau pour récupérer le sel, COMPARER enfin : 20 g de fer + 30 g de sel = 50 g, exactement ce qui avait été mis. Rien n'a disparu.

*Source :* Protocole de séparation établi d'après Fondation La main à la pâte, séquence « À la découverte des mélanges » (cycle 3)

</details>

---

## Score

| | CM1 | CM2 |
|---|---|---|
| Énigmes résolues (5 pts) | 15 × 5 = 75 | 20 × 5 = 100 |
| Bonus de rapidité (3 pts par salle) | 15 | 15 |
| Quizz final (2 pts × 5) | 10 | 10 |
| **Total maximal** | **100** | **125** |

Un indice consulté retire **2 points**. Le bonus de rapidité tombe à 2 points si la salle a demandé un indice, et à 0 au-delà de 8 minutes (CM1) ou 10 minutes (CM2) par salle.

**Mentions** : 90 % → Grand chimiste · 75 % → Chimiste confirmé · 55 % → Apprenti chimiste · en dessous → Apprenti motivé.

**Badges** : Équipe rapide (une salle en moins de 6 min) · Œil de lynx (salle 3 sans indice) · Main sûre (salle 4 sans indice) · Héritier de Madame Mélange (3 indices au maximum sur toute la partie).

---

## Les leçons (bouton « Leçons »)

Cinq leçons rédigées, une par salle, de 3 à 4 minutes de lecture, avec un texte différent en CM1 et en CM2, des objectifs, un lexique, un schéma et la source. Sous chaque énigme, le bouton « Leçon » ouvre directement la leçon correspondante.

| Leçon | Salle | Énigmes |
|---|---|---|

| Mesurer et comparer des masses | 1 | 1-1, 1-2, 1-3, 1-4 |
| La masse se conserve | 2 | 2-1, 2-2, 2-3, 2-4 |
| Mélanges homogènes et hétérogènes | 3 | 3-1, 3-2, 3-3, 3-4 |
| Séparer un mélange de solides | 4 | 4-1, 4-2, 4-3, 4-4 |
| Séparer un solide d'un liquide | 5 | 5-1, 5-2, 5-3, 5-4 |

---

## Sécurité : ne jamais goûter, ne jamais sentir

La règle est rappelée par Lila dès l'accueil, affichée dans la cuisine d'essai, reprise dans les énigmes 2-1, 3-4 et dans les leçons. Pour les manipulations en classe, voir le guide pédagogique (section 10).

## Sources

- **Programme de sciences et technologie du cycle 3** (Bulletin officiel, 2026, applicable à la rentrée 2026), partie « La matière » : comparer et mesurer des masses, effectuer des conversions d'unités de masse, séparer les constituants d'un mélange de solides ou d'un mélange solide-liquide par tamisage, décantation, filtration, récupérer un solide dissous par évaporation, montrer que la masse totale se conserve lors du mélange d'un solide dans un liquide. [education.gouv.fr](https://www.education.gouv.fr/sites/default/files/document/Annexe%20%E2%80%93%20Programme%20de%20sciences%20et%20technologie%20du%20cycle%203-365166.pdf)
- **Fondation La main à la pâte**, séquence « À la découverte des mélanges » (cycle 3) : mélanges homogènes et hétérogènes, dissolution, tamisage, décantation, filtration, évaporation, aimantation ; consigne de ne jamais goûter ni sentir. [fondation-lamap.org](https://fondation-lamap.org/sequence-d-activites/a-la-decouverte-des-melanges)
- **Eau de mer** : salinité moyenne des océans d'environ 35 g par litre (entre 30 et 40 g selon les mers). **Sel** : solubilité d'environ 36 g pour 100 mL d'eau à 20 °C (non utilisée dans les énigmes, citée dans le guide).
- **Air** : masse volumique d'environ 1,2 g par litre à 20 °C (valeur usuelle des manuels de physique-chimie de 4e).
- Cité des sciences et de l'industrie et Lumni : ressources de consolidation citées dans le guide pédagogique.

Les points qui méritent une vérification complémentaire sont listés dans [A-VERIFIER.md](A-VERIFIER.md).

---

## Modifier le contenu

| Pour changer… | Fichier |
|---|---|
| **les énigmes** : questions, réponses, indices, corrections | `assets/data/enigmes.json` |
| les dialogues, les lieux, les mots-clés, le protocole | `assets/data/dialogues.json` |
| les leçons (texte, lexique, schéma, source) | `assets/data/lecons.json` |
| les évaluations imprimables et le quizz final | `assets/data/evaluations.json` |
| les décors dessinés | `js/decors.js` |
| les personnages dessinés | `js/personnages.js` |

Le moteur `js/enigmes.js` est le même que celui du *Sceau de la République* : dix types d'énigmes pilotés par le JSON. Ce jeu les utilise tous les dix.

| Type | Ce que fait l'élève | Utilisé ici |
|---|---|---|

| `qcm` | choisit une réponse par question | 1-2, 2-3, 4-3 |
| `vraifaux` | tranche vrai ou faux | 2-1, 3-4 |
| `association` | relie deux colonnes | 3-3, 4-1 |
| `ordre` | remet des éléments dans l'ordre avec ▲▼ | 1-1, 4-2, 5-4 |
| `tri` | range des étiquettes dans des colonnes | 3-1 |
| `trous` | place des étiquettes dans un texte à trous | 1-4, 5-1 |
| `lettres` | clique des lettres cachées, dans l'ordre | 5-3 |
| `code` | compose un cadenas à nombres | 1-3, 2-4 |
| `intrus` | repère l'élément qui ne va pas avec les autres | 3-2 |
| `plan` | place des étiquettes sur les cases d'un schéma | 2-2, 4-4, 5-2 |

Après une modification d'un fichier `js/` ou `css/`, augmentez son numéro de version dans `index.html` (`app.js?v1` → `app.js?v2`).

```
melanges/
├── index.html · prof.html
├── README.md · GUIDE-PEDAGOGIQUE.md · A-VERIFIER.md
├── assets/
│   ├── data/      enigmes.json, dialogues.json, lecons.json, evaluations.json
│   ├── videos/    décors et cinématiques (+ personnages/) — facultatif
│   └── images/    decors/, personnages/, cartes/ — facultatif
├── css/           style, enigmes, video, animations, personnages, impression
└── js/            app (moteur), enigmes (les 10 types), decors, personnages, media,
                   narration, audio, lecons, impression, api, sync, reglages
```
