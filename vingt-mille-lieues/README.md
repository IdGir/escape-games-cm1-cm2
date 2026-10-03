# ⚓ Vingt mille lieues sous les mers — Le Journal du Nautilus

Escape game immersif de cycle 3 (CM1-CM2), d'après le roman de Jules Verne (1869-1870, domaine public), **5 grades** de
difficulté, campagne prévue en **11 escales**. **État : escales 1 à 6 jouables (pilote validé : escale 2) ; escales 7 à 11 en cours.**

- Jouer : `vingt-mille-lieues/index.html` (en ligne, ou `lancer.bat` puis http://127.0.0.1:8000/vingt-mille-lieues/).
- Tableau de bord enseignant (mode local) : `prof.html` · médias : `medias.html` · leçons A4 : `lecons-imprimables.html`.
- Vérifier une énigme sans rien enregistrer : `index.html?verif=1&escale=2&niveau=lieutenant&enigme=3`
  (`&secours=1` : décors dessinés ; `&fin=1` : écran de fin d'escale).
- Guide : [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) · cohérence : [COHERENCE.md](COHERENCE.md) · plan : [PLAN.md](PLAN.md) ·
  médias : [PRODUCTION-MEDIAS.md](PRODUCTION-MEDIAS.md) · faits à vérifier : [A-VERIFIER.md](A-VERIFIER.md) ·
  intégration au site (seconde PR) : [INTEGRATION.md](INTEGRATION.md).

> Fichier généré par `node vingt-mille-lieues/outils/generer-docs.js` à partir de `assets/data/enigmes.json`.

## Grades (équivalences réservées à l'enseignant)

| Grade affiché | Équivalent | Profil |
|---|---|---|
| 🐚 Mousse | ≈ CE2 | énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, un choix faux écarté, fiche mise en évidence) |
| ⚓ Matelot | ≈ CM1 | cœur de programme CM1 |
| 🧭 Timonier | ≈ CM2 | cœur de programme CM2 |
| 🔭 Lieutenant | ≈ 6ᵉ | raisonnement en deux étapes, documents à croiser, justification |
| 🔱 Second | ≈ 5ᵉ | synthèse, données chiffrées, pièges de logique, justification |

## Barème

10 points tout juste du premier coup, 3 après une erreur, −2 par indice (Mousse : premier indice offert). Bonus :
📚 « Bien documenté » +2 (réussite du premier coup après avoir ouvert la bonne fiche pendant l'énigme), 🏊 « Maître-nageur » +5
(escale sans indice), ⏱️ rapidité +5 (≤ durée de référence − 5 min) ou +3 (≤ durée de référence ; 25 min par défaut, plus les
minutes accordées). **Maximum par escale de 4 énigmes : 4 × 12 + 5 + 5 = 58 points, à tous les grades.** La jauge d'air est un
décor : elle ne retire aucun point. Anti-tâtonnement : 3 erreurs en 60 s → sas verrouillé 20 s, puis 40 s, puis 80 s.

## Solutions

### Escale 1 — La chasse au « monstre » · mot du journal : **NARVAL**

*Première partie, ch. I à VII (le « monstre », la frégate Abraham Lincoln, le harpon de Ned Land, la chute à la mer)*

#### 1.1 Le livre de quart — pont-lincoln, objet « livre-quart », Le professeur Aronnax

Compétence : Sciences : mesurer une distance et une durée lors du déplacement d'un objet ; différents types de mouvement. · Fiche : Rayon Navigation, fiche 2 « Mesurer un déplacement »

- **🐚 Mousse** (qcm) — Q1 : 4 heures · Q2 : circulaire
- **⚓ Matelot** (code) — Durée de la poursuite (en minutes) 90 ; Milles parcourus en 1 heure 15
- **🧭 Timonier** (code) — Vitesse de la frégate (nœuds) 18 ; Vitesse de la lueur (nœuds) 24
- **🔭 Lieutenant** (qcm) — Q1 : 18 milles · Q2 : de rectiligne à circulaire · Justification : « Quand deux objets vont dans le même sens, l'écart entre eux change chaque heure de la différence de leurs vitesses. »
- **🔱 Second** (code) — Heures pour la rattraper 4 ; 18 nœuds ≈ ? km/h 33 · Justification : « Quand deux objets vont dans le même sens, l'écart entre eux change chaque heure de la différence de leurs vitesses. »

#### 1.2 Forcer les feux — machines-vapeur, objet « chaudiere », Conseil

Compétence : Histoire : l'âge industriel — énergies et machines ; la machine à vapeur, révolution industrielle et progrès technique. · Fiche : Rayon Histoire, fiche 1 « La machine à vapeur »

- **🐚 Mousse** (ordre) — 1. Le charbon brûle dans le foyer. ; 2. L'eau de la chaudière chauffe et devient de la vapeur. ; 3. La vapeur pousse le piston. ; 4. L'hélice tourne et la frégate avance.
- **⚓ Matelot** (ordre) — 1. Le foyer ; 2. La chaudière ; 3. Le cylindre ; 4. La bielle et l'arbre ; 5. L'hélice
- **🧭 Timonier** (ordre) — 1. Le charbon ; 2. La combustion dans le foyer ; 3. La chaudière ; 4. Le piston dans le cylindre ; 5. La bielle et l'arbre ; 6. L'hélice
- **🔭 Lieutenant** (trous) — Mots : chimique, chaleur, vapeur, piston, mouvement, manomètre · Étiquettes pièges : électrique, glace, boussole · Justification : « Plus de charbon brûlé donne plus de chaleur, donc plus de vapeur sous pression, donc un piston poussé plus fort. »
- **🔱 Second** (qcm) — Q1 : Pour remplir ses soutes de charbon. · Q2 : Le charbon brûle dans le foyer : c'est une combustion. · Q3 : tirer son énergie d'une autre source que la combustion de charbon à bord. · Justification : « Une machine ne crée pas d'énergie : il faut une source (charbon, vent, eau, piles…) et chaque source a ses traces : le charbon brûlé produit fumée et chaleur. »

#### 1.3 La cambuse — cambuse, objet « etagere-vivres », Ned Land

Compétence : Sciences : production et conservation des aliments (salaison, séchage, fumage, conserve) ; produits agricoles et produits transformés. · Fiche : Rayon Vivant, fiche 1 « Conserver les aliments »

- **🐚 Mousse** (association) — La morue → avec beaucoup de sel · Le jambon → à la fumée · Les petits pois → dans une boîte fermée, chauffée
- **⚓ Matelot** (association) — La morue → la salaison (le sel) · Le jambon → le fumage · Le biscuit de mer → le séchage (cuit et séché très dur) · Les petits pois en boîte → la conserve (chauffée dans une boîte fermée) · La confiture → le sucre
- **🧭 Timonier** (association) — Saler → le sel retire l'eau dont les microbes ont besoin · Sécher → on enlève l'eau de l'aliment · Mettre en conserve → la chaleur tue les microbes et la boîte fermée empêche d'autres d'entrer · Garder au froid → le froid ralentit les microbes · Sucrer fortement → beaucoup de sucre retient l'eau, comme le sel
- **🔭 Lieutenant** (qcm) — Q1 : Pour prévenir le scorbut, une maladie due au manque de vitamine C. · Q2 : le congélateur électrique · Justification : « Sans fruits ni légumes frais, les marins des longues traversées souffraient du scorbut, causé par un manque de vitamine C ; citrons et choucroute en apportent. »
- **🔱 Second** (tri) — On lui a retiré l'eau (sel, séchage, sucre, fumée) : morue salée, biscuit de mer, confiture, jambon fumé · Chauffé puis fermé (conserve) : petits pois en boîte de fer-blanc, viande en bocal stérilisé · Frais : à consommer vite : poisson pêché ce matin, lait de la chèvre du bord · Justification : « Beaucoup de sucre retient l'eau, comme le sel : les microbes ne peuvent plus s'en servir. »

#### 1.4 Le harpon de Ned Land — pont-lincoln, objet « harpon », Ned Land

Compétence : Sciences : caractéristiques du vivant (naître, grandir, se nourrir, respirer, se reproduire, mourir) ; distinguer un être vivant d'un objet technique. · Fiche : Rayon Vivant, fiche 2 « Être vivant ou objet ? »

- **🐚 Mousse** (tri) — Être vivant : une baleine, un narval, une mouette · Objet fabriqué : une frégate, un harpon, une lanterne
- **⚓ Matelot** (tri) — Un être vivant… : naît et grandit, se nourrit, respire, se reproduit · Un objet technique… : est fabriqué par des humains, a besoin d'une source d'énergie fournie (charbon, piles…), est fait de pièces assemblées (rivets, boulons), répond à un besoin humain
- **🧭 Timonier** (tri) — Indique une machine : le harpon sonne comme sur du fer, on devine des plaques boulonnées, sa lumière s'éteint d'un coup, comme une lampe qu'on coupe · Indique un être vivant :  · Ne permet pas de conclure : il brille dans la nuit, il souffle des jets d'eau, il nage plus vite que la frégate, des oiseaux de mer le suivent pour manger les poissons qu'il fait fuir
- **🔭 Lieutenant** (tri) — Indique une machine : le harpon sonne comme sur du fer, on devine des rivets et des plaques de tôle · Indique un être vivant : il a des petits qui le suivent · Ne permet pas de conclure : il n'a jamais été vu manger, il brille dans la nuit, il souffle des jets d'eau, sa taille n'a pas changé depuis un an d'observations · Justification : « Certains êtres vivants produisent leur propre lumière (bioluminescence) ; une machine peut aussi porter des lampes. »
- **🔱 Second** (qcm) — Q1 : Des plaques de tôle assemblées par des boulons. · Q2 : Il naît, grandit, se nourrit, se reproduit et meurt. · Q3 : Il souffle des jets d'eau. · Justification : « Un objet technique est fait de pièces fabriquées et assemblées par des humains ; aucun être vivant n'est boulonné. »

### Escale 2 — Dans le ventre du Nautilus · mot du journal : **MOBILIS**

*Première partie, ch. XI « Le Nautilus », ch. XII « Tout par l'électricité », ch. XIII « Quelques chiffres »*

#### 2.1 Le câble brûlé du carré — carre, objet « table », Conseil

Compétence : Électricité : distinguer conducteurs et isolants ; connaître les dangers de l'électricité (court-circuit, eau salée). · Fiche : Rayon Électricité, fiche 1 « Conducteurs et isolants »

- **🐚 Mousse** (tri) — Laisse passer le courant : un fil de cuivre, une clé en fer, une cuillère en argent, une règle en laiton · Arrête le courant : un verre en cristal, un bouchon de liège, une feuille de papier, un ruban de caoutchouc
- **⚓ Matelot** (tri) — Conducteur (pour l'âme du câble) : un compas en acier, une clé en fer, un fil de cuivre, une plume d'écriture en acier · Isolant (pour la gaine) : une carafe en verre, un ruban de caoutchouc, une carte marine en papier, une règle en bois sec
- **🧭 Timonier** (tri) — Conducteur : un fil de cuivre, l'aiguille d'acier d'une boussole, la mine d'un crayon (graphite), l'eau de mer renversée sur la table · Isolant : une feuille de caoutchouc, une carafe en cristal, le cuir sec d'un fauteuil, une ficelle sèche, une soucoupe en porcelaine
- **🔭 Lieutenant** (tri) — Conducteur : une lame de couteau en acier, un anneau en or, la mine d'un crayon (graphite), l'eau de mer, le corps humain (une main mouillée) · Isolant : une gaine de caoutchouc, une poignée en porcelaine, un manche en bois sec, une vitre de verre, l'air sec entre deux fils · Justification : « Un isolant ne laisse pas passer le courant : une gaine isolante empêche le courant de s'échapper par ce qui touche le câble. »
- **🔱 Second** (qcm) — Q1 : L'eau de mer laisse passer un peu le courant, l'eau douce distillée presque pas. · Q2 : L'eau de mer a relié les deux fils : le courant est passé de l'un à l'autre sans traverser les lampes. · Q3 : le compas en acier · Justification : « Il y a court-circuit quand les deux bornes de la pile sont reliées par un conducteur sans passer par un appareil : le fil chauffe, il peut y avoir un incendie. »

#### 2.2 Le tableau de laiton — machines, objet « tableau-bornes », Le professeur Aronnax

Compétence : Électricité : réaliser un circuit électrique fermé ; circuits en série et en dérivation ; rôle de l'interrupteur ; court-circuit. · Fiche : Rayon Électricité, fiche 2 « Le circuit électrique »

- **🐚 Mousse** (circuit) — Boucle fermée : + → Lustre du salon → −. · Tout montage qui remplit ces conditions est accepté (simulation du courant).
- **⚓ Matelot** (circuit) — Une seule boucle (série) : + → Manette → Lustre du salon → Pompe à air → −, Manette fermé. · Tout montage qui remplit ces conditions est accepté (simulation du courant).
- **🧭 Timonier** (circuit) — Montage en dérivation : une boucle par appareil depuis les piles (Lustre du salon, Lampe de la coursive). · Tout montage qui remplit ces conditions est accepté (simulation du courant).
- **🔭 Lieutenant** (circuit) — Montage en dérivation : une boucle par appareil depuis les piles (Lustre du salon, Lampe de la coursive, Pompe à air), l'interrupteur K2 placé seulement dans la boucle de Pompe à air, et fermé. · Tout montage qui remplit ces conditions est accepté (simulation du courant). · Justification : « En dérivation, chaque appareil a sa propre boucle : si une lampe grille, les autres restent allumées, et un interrupteur placé dans une boucle ne commande que l'appareil de cette boucle. »
- **🔱 Second** (circuit) — Retirer : fil de secours (court-circuit). · Montage en dérivation : une boucle par appareil depuis les piles (Lustre du salon, Lampe de la coursive, Pompe à air), l'interrupteur K2 placé seulement dans la boucle de Pompe à air, et fermé. · Tout montage qui remplit ces conditions est accepté (simulation du courant). · Justification : « Il y a court-circuit quand les deux bornes de la pile sont reliées par un conducteur sans passer par un appareil : le fil chauffe, il peut y avoir un incendie. »

#### 2.3 Le mur des instruments — cabine, objet « mur-instruments », Le capitaine Nemo

Compétence : Objets techniques : identifier la fonction d'usage d'un objet ; réaliser et exploiter des mesures (instruments de mesure, lecture d'une graduation). · Fiche : Rayon Navigation, fiche 1 « Les instruments du bord »

- **🐚 Mousse** (association) — La boussole → la direction à suivre · Le thermomètre → la température · L'horloge → l'heure
- **⚓ Matelot** (association) — La boussole → la direction (le cap) · Le thermomètre → la température à bord · Le manomètre → la profondeur, grâce à la pression de l'eau · Le baromètre → le temps qu'il fera en surface
- **🧭 Timonier** (association) — La boussole → « nord-est » · Le thermomètre → « 18 °C » · Le manomètre → « 4 atmosphères » · Le baromètre → « 758 mm de mercure, en baisse » · Le chronomètre → « 10 h 42 min »
- **🔭 Lieutenant** (qcm) — Q1 : environ 30 m · Q2 : Elle descendra vers 1 atmosphère. · Justification : « À la surface, l'air appuie déjà avec une pression d'environ 1 atmosphère ; ensuite, la pression augmente d'environ 1 atmosphère tous les 10 m d'eau de mer. »
- **🔱 Second** (qcm) — Q1 : environ 50 m · Q2 : Le mauvais temps arrivait : il faut s'attendre à une mer agitée en surface. · Q3 : environ 10 m · Justification : « Parce qu'à la surface, l'air appuie déjà avec environ 1 atmosphère : seules 5 atmosphères sont dues à l'eau. »

#### 2.4 L'épure du capitaine — salon, objet « epure », Ned Land

Compétence : Objets techniques et énergie : identifier la source d'énergie d'un objet ; ordonner une chaîne d'énergie (stocker, commander, distribuer, convertir, transmettre, agir) ; formes d'énergie. · Fiche : Rayon Électricité, fiche 3 « La chaîne d'énergie »

- **🐚 Mousse** (ordre) — 1. Les piles gardent l'énergie. ; 2. On abaisse la manette. ; 3. Le moteur électrique tourne. ; 4. L'hélice pousse le Nautilus.
- **⚓ Matelot** (ordre) — 1. Les piles au sodium ; 2. La manette de commande ; 3. Les câbles qui vont de la manette au moteur ; 4. Le moteur électrique ; 5. L'hélice
- **🧭 Timonier** (ordre) — 1. Les piles au sodium ; 2. La manette ; 3. Les câbles qui vont de la manette au moteur ; 4. Le moteur électrique ; 5. L'arbre de l'hélice ; 6. L'hélice
- **🔭 Lieutenant** (trous) — Mots : chimique, électrique, commande, convertit, mouvement, transmet · Étiquettes pièges : lumineuse, crée, stocke · Justification : « Un objet ne crée pas d'énergie : il la reçoit d'une source et la transforme. »
- **🔱 Second** (ordre) — 1. Le sel dissous dans l'eau de mer ; 2. Le sodium extrait du sel ; 3. Les piles au sodium ; 4. La manette ; 5. Les câbles qui vont de la manette au moteur ; 6. Le moteur électrique ; 7. L'hélice (par son arbre) · Justification : « Nemo tire le sodium de ses piles du sel de l'eau de mer : la mer fournit la matière de sa réserve d'énergie. »

### Escale 3 — La forêt de l'île Crespo · mot du journal : **CRESPO**

*Première partie, ch. XV « Une invitation par lettre », XVI « Promenade en plaine », XVII « Une forêt sous-marine »*

#### 3.1 Les réservoirs d'air — sas, objet « scaphandres », Ned Land

Compétence : Sciences : états et constitution de la matière à l'échelle macroscopique ; l'air est de la matière (il occupe de l'espace, il a une masse, il se comprime) ; propriétés des solides, liquides et gaz. · Fiche : Rayon Matière et lumière, fiche 1 « L'air, c'est de la matière »

- **🐚 Mousse** (vraifaux) — VRAI — L'air est invisible, mais il existe. · FAUX — L'air ne prend pas de place. · VRAI — Quand on remplit le sas d'eau, l'eau chasse l'air. · FAUX — Un réservoir plein d'air est exactement aussi lourd qu'un réservoir vide.
- **⚓ Matelot** (qcm) — Q1 : le réservoir B, le plus lourd · Q2 : Parce que l'air se comprime.
- **🧭 Timonier** (tri) — Solide : il a une forme propre : le casque de cuivre, les semelles de plomb · Liquide : il prend la forme du récipient, sa surface reste horizontale : l'eau de mer qui monte dans le sas, l'huile des charnières · Gaz : il occupe tout l'espace et se comprime : l'air comprimé du réservoir, les bulles qui remontent
- **🔭 Lieutenant** (code) — Litres d'air à l'air libre 500 ; Masse de cet air (en g) 600 · Justification : « L'air a une masse : à l'air libre, un litre d'air pèse environ 1,2 gramme. »
- **🔱 Second** (qcm) — Q1 : Le piston de la seringue d'air s'enfonce un peu, celui de la seringue d'eau presque pas. · Q2 : 600 g · Q3 : Deux matières ne peuvent pas occuper la même place : l'eau chasse l'air. · Justification : « Un gaz se comprime : on peut le serrer dans un plus petit volume ; un liquide se comprime très peu. »

#### 3.2 La plaine aux mille couleurs — recif, objet « faune-recif », Conseil

Compétence : Sciences : panorama du vivant ; organisation des êtres vivants (classer selon les caractères partagés) ; biodiversité. · Fiche : Rayon Vivant, fiche 3 « Classer le vivant »

- **🐚 Mousse** (intrus) — Intrus : l'étoile de mer
- **⚓ Matelot** (tri) — Vertébrés (squelette interne, colonne vertébrale) : le poisson-clown, la tortue de mer, le requin · Invertébrés (pas de colonne vertébrale) : l'étoile de mer, le crabe, la méduse, l'oursin
- **🧭 Timonier** (association) — Les poissons → des nageoires, des branchies, souvent des écailles · Les reptiles marins (tortue) → des poumons et une peau couverte d'écailles ou d'une carapace ; ils pondent sur la terre · Les crustacés (crabe) → une carapace et des pattes articulées · Les mollusques (bénitier) → un corps mou, souvent protégé par une coquille · Les échinodermes (étoile de mer, oursin) → une peau épineuse et un corps en cinq parties
- **🔭 Lieutenant** (intrus) — Intrus : le dauphin · Justification : « On classe par les caractères partagés : le dauphin respire avec des poumons et allaite ses petits, comme les mammifères ; les poissons respirent avec des branchies. »
- **🔱 Second** (tri) — Vertébrés > poissons : le requin, l'hippocampe · Vertébrés > mammifères : le dauphin, le dugong · Invertébrés > mollusques : le bénitier géant, le poulpe · Invertébrés > cnidaires (corps mou, tentacules urticants) : la méduse, le corail · Justification : « Le corail est un animal : de petits polypes au corps mou et aux tentacules urticants, comme les méduses. »

#### 3.3 La lampe dans la forêt — foret-crespo, objet « lampe-ruhmkorff », Le professeur Aronnax

Compétence : Sciences : la lumière — sources de lumière et objets éclairés, propagation rectiligne, ombres, absorption de la lumière par l'eau. · Fiche : Rayon Matière et lumière, fiche 2 « La lumière sous la mer »

- **🐚 Mousse** (tri) — Produit sa lumière (source) : le Soleil, la lampe du scaphandrier, le fanal du Nautilus · Est seulement éclairé : la gorgone, le rocher, le casque de cuivre
- **⚓ Matelot** (vraifaux) — VRAI — La lumière se propage en ligne droite. · VRAI — L'ombre d'un scaphandrier se forme du côté opposé à la lampe. · FAUX — Un rocher produit sa propre lumière. · FAUX — Plus on descend, plus il fait clair.
- **🧭 Timonier** (ordre) — 1. Le rouge ; 2. L'orange ; 3. Le jaune ; 4. Le vert ; 5. Le bleu
- **🔭 Lieutenant** (qcm) — Q1 : La lumière rouge du Soleil a été absorbée par l'eau avant d'arriver jusqu'à elle. · Q2 : Elle paraît de nouveau rouge. · Justification : « Un objet ne paraît rouge que si une lumière contenant du rouge l'éclaire ; la lampe proche apporte cette lumière avant que l'eau ne l'absorbe. »
- **🔱 Second** (code) — Profondeur au moins (m) 25 ; Au plus (m) 35 ; Couleurs encore visibles 2 · Justification : « L'eau absorbe les couleurs les unes après les autres : d'abord le rouge, puis l'orange, le jaune, le vert ; le bleu va le plus loin. »

### Escale 4 — Vanikoro et Lapérouse · mot du journal : **ASTROLABE**

*Première partie, ch. XIX « Vanikoro » : le Nautilus passe sur les épaves de l'expédition de Lapérouse ; Nemo montre à Aronnax une boîte de fer-blanc contenant les instructions de l'expédition annotées par Louis XVI.*

#### 4.1 Les instruments engloutis — epave-vanikoro, objet « instruments-epave », Le professeur Aronnax

Compétence : Histoire : les progrès techniques qui ont permis aux Européens de s'aventurer vers de nouveaux territoires (boussole, astrolabe, sextant, chronomètre, cartes). · Fiche : Rayon Histoire, fiche 2 « Les instruments des explorateurs »

- **🐚 Mousse** (association) — La boussole → trouver la direction du nord · La longue-vue → voir loin · La carte → dessiner et retrouver les routes
- **⚓ Matelot** (association) — La boussole → trouver le nord, donc garder sa direction · L'astrolabe → mesurer la hauteur du Soleil pour savoir si l'on est loin de l'équateur · Le loch et le sablier → mesurer la vitesse du navire · La carte → noter les côtes découvertes et les routes
- **🧭 Timonier** (association) — La boussole → garder sa direction même sans voir les étoiles · L'astrolabe, puis le sextant → trouver sa latitude (distance à l'équateur) grâce au Soleil · Le chronomètre de marine → trouver sa longitude en comparant les heures · La caravelle → naviguer loin, même contre le vent · Les cartes et portulans → garder la mémoire des côtes et des routes
- **🔭 Lieutenant** (qcm) — Q1 : en mesurant la hauteur du Soleil à midi (astrolabe, sextant) · Q2 : en comparant l'heure locale à l'heure du port de départ, gardée par un chronomètre · Justification : « La Terre fait un tour (360°) en 24 heures : chaque heure d'écart entre l'heure locale et l'heure du port de départ correspond à 15° de longitude. »
- **🔱 Second** (code) — Heures d'écart 4 ; Degrés de longitude 60 ; Est ou ouest ? OUEST · Justification : « Le Soleil se lève à l'est : quand il est midi chez lui, il est déjà plus tard à Paris ; le navire est donc à l'ouest. »

#### 4.2 La boîte de fer-blanc — cabine, objet « bureau », Le capitaine Nemo

Compétence : Histoire : le temps de la Révolution ; contexte du royaume en 1789 ; fin de la monarchie absolue et de l'Ancien Régime ; repères chronologiques. · Fiche : Rayon Histoire, fiche 3 « Lapérouse et la Révolution »

- **🐚 Mousse** (ordre) — 1. Le roi Louis XVI envoie Lapérouse explorer le monde. ; 2. Les navires de Lapérouse font naufrage à Vanikoro. ; 3. La prise de la Bastille. ; 4. On retrouve enfin les épaves.
- **⚓ Matelot** (ordre) — 1. Louis XVI devient roi de France. ; 2. Départ de Lapérouse, de Brest. ; 3. Naufrage à Vanikoro. ; 4. Prise de la Bastille ; Déclaration des droits de l'homme et du citoyen. ; 5. Exécution de Louis XVI.
- **🧭 Timonier** (ordre) — 1. Avènement de Louis XVI, roi absolu. ; 2. L'expédition de Lapérouse quitte Brest. ; 3. Dernières nouvelles, depuis l'Australie ; naufrage à Vanikoro. ; 4. États généraux, prise de la Bastille, abolition des privilèges. ; 5. Fin de la royauté : la République est proclamée. ; 6. Dumont d'Urville retrouve le lieu du naufrage.
- **🔭 Lieutenant** (ordre) — 1. Avènement de Louis XVI. ; 2. Le roi annote de sa main les instructions de l'expédition. ; 3. Départ de Brest de La Boussole et de L'Astrolabe. ; 4. Naufrage à Vanikoro. ; 5. Déclaration des droits de l'homme et du citoyen. ; 6. Abolition de la royauté. ; 7. Exécution de Louis XVI. · Justification : « Elle a été décidée et organisée par un roi absolu, avant 1789 et la fin de l'Ancien Régime. »
- **🔱 Second** (ordre) — 1. Avènement de Louis XVI. ; 2. Départ de l'expédition de Lapérouse. ; 3. Naufrage à Vanikoro. ; 4. Réunion des états généraux. ; 5. Prise de la Bastille. ; 6. Proclamation de la République. ; 7. Les épaves sont retrouvées par Dumont d'Urville. · Justification : « L'expédition a disparu juste avant la Révolution : partie d'une monarchie absolue, elle ne pouvait plus rentrer dans le même pays. »

#### 4.3 Les papiers d'un autre monde — carre, objet « table », Conseil

Compétence : Histoire : la société d'Ancien Régime (trois ordres, privilèges) ; fin de la monarchie absolue ; affirmation des nouveaux principes (Déclaration des droits de l'homme et du citoyen). · Fiche : Rayon Histoire, fiche 4 « L'Ancien Régime et 1789 »

- **🐚 Mousse** (tri) — Avant 1789 : le roi décide de tout : « Louis, roi par la grâce de Dieu, ordonne… », « Seuls les nobles peuvent chasser. » · Après 1789 : les droits de l'homme : « Les hommes naissent et demeurent libres et égaux en droits. », « Les privilèges sont abolis. »
- **⚓ Matelot** (tri) — Le clergé (ceux qui prient) : un évêque, un moine · La noblesse (ceux qui combattent) : un comte, le comte de Lapérouse, officier de marine · Le tiers état (ceux qui travaillent) : un paysan, un marchand, un charpentier de marine
- **🧭 Timonier** (tri) — Ancien Régime : le roi a tous les pouvoirs (monarchie absolue), la société est divisée en trois ordres, le clergé et la noblesse ont des privilèges, seul le tiers état paie la taille · Nouveaux principes (1789) : les hommes naissent libres et égaux en droits, le pouvoir appartient à la nation, les privilèges sont abolis (nuit du 4 août), chacun paie l'impôt selon ses moyens
- **🔭 Lieutenant** (tri) — Ancien Régime : le roi tient son pouvoir de Dieu, les nobles ne paient pas la taille, on peut être emprisonné sur simple ordre du roi (lettre de cachet) · Nouveaux principes (1789) : les emplois sont ouverts à tous selon leurs talents, la souveraineté réside dans la nation, nul ne peut être arrêté que dans les cas prévus par la loi, la liberté d'opinion, même religieuse · Justification : « « Les hommes naissent et demeurent libres et égaux en droits. » »
- **🔱 Second** (qcm) — Q1 : un avantage réservé à certains, par exemple ne pas payer certains impôts · Q2 : le tiers état · Q3 : les députés abolissent les privilèges · Justification : « Le 4 août 1789, les députés abolissent les privilèges : la loi devient la même pour tous. »

### Escale 5 — Les perles de Ceylan · mot du journal : **PERLE**

*Deuxième partie, ch. II « Une nouvelle proposition du capitaine Nemo » et ch. III « Une perle de dix millions »*

#### 5.1 La perle géante — banc-perles, objet « huitre-geante », Conseil

Compétence : Sciences : comparer et mesurer des masses (balance, unités g et kg) ; propriétés de la matière. · Fiche : Rayon Matière et lumière, fiche 3 « Mesurer des masses »

- **🐚 Mousse** (qcm) — Q1 : la perle · Q2 : une balance
- **⚓ Matelot** (ordre) — 1. une petite perle ; 2. un coquillage ; 3. le poignard du capitaine ; 4. une huître ordinaire ; 5. la perle géante (estimée)
- **🧭 Timonier** (code) — Masse de toutes nos perles (g) 950 ; La perle du capitaine pèse de plus (g) 550
- **🔭 Lieutenant** (qcm) — Q1 : 17 g · Q2 : penche du côté droit · Justification : « À l'équilibre, la masse totale d'un plateau est égale à la masse totale de l'autre. »
- **🔱 Second** (code) — Masse de la perle (g) 1500 ; en kg 1,5 · Justification : « La masse d'un ensemble est la somme des masses de ses parties : on retrouve une partie en soustrayant les autres. »

#### 5.2 Le pêcheur de perles — banc-perles, objet « pecheur », Ned Land

Compétence : Géographie : les inégalités dans le monde — identifier les manifestations des inégalités de niveau de vie ; localiser les grandes aires géographiques. · Fiche : Rayon Géographie, fiche 1 « Les inégalités dans le monde »

- **🐚 Mousse** (tri) — Vie aisée : aller à l'école chaque jour, avoir de l'eau potable au robinet, être soigné quand on est malade · Vie difficile : travailler enfant pour nourrir sa famille, risquer sa vie pour quelques pièces, aller chercher l'eau loin de chez soi
- **⚓ Matelot** (tri) — Niveau de vie élevé : on vit en moyenne plus de 80 ans, presque tous les enfants vont à l'école, presque tous les logements ont l'eau potable · Niveau de vie faible : beaucoup d'enfants meurent avant 5 ans, beaucoup d'adultes ne savent pas lire, une grande partie des habitants vit avec très peu d'argent
- **🧭 Timonier** (tri) — Le tableau le prouve : On vit plus longtemps dans le pays A., Dans le pays B, environ 45 personnes sur 100 n'ont pas l'eau potable. · Le tableau dit le contraire : Le pays B a plus de médecins que le pays A., Tous les enfants du pays B vont à l'école. · Le tableau ne le dit pas : Le pays A est plus grand que le pays B., Les habitants du pays B pêchent des perles.
- **🔭 Lieutenant** (tri) — Exact : Les pays au niveau de vie le plus faible se trouvent surtout en Afrique subsaharienne et en Asie du Sud., On mesure le niveau de vie avec plusieurs indicateurs : espérance de vie, école, revenu., Dans un même pays, il peut y avoir des riches et des pauvres. · Faux : Un seul indicateur suffit toujours pour comparer deux pays., Les inégalités n'existent qu'entre pays, jamais dans un pays., Tous les pays d'Asie ont le même niveau de vie. · Justification : « Dans un même pays, certains vivent dans l'aisance et d'autres dans la pauvreté : ici, le pêcheur risque sa vie quand le marchand de perles s'enrichit. »
- **🔱 Second** (qcm) — Q1 : Un revenu moyen élevé peut cacher de fortes inégalités entre habitants. · Q2 : croiser plusieurs indicateurs (revenu, santé, école, eau) · Q3 : une colonie britannique · Justification : « Un indicateur seul peut tromper : une moyenne cache les écarts ; on croise plusieurs indicateurs. »

#### 5.3 Les voiles de Ceylan — pont-ceylan, objet « barques », Le professeur Aronnax

Compétence : Histoire : les échanges commerciaux avec les colonies (produits des colonies vers l'Europe, produits manufacturés vers les colonies). · Fiche : Rayon Histoire, fiche 5 « Colonies et échanges »

- **🐚 Mousse** (association) — le café → les plantations de Ceylan · la cannelle → les arbres de Ceylan · les tissus de coton → les usines d'Angleterre
- **⚓ Matelot** (qcm) — Q1 : elle part de Ceylan vers l'Europe · Q2 : elle part de Ceylan vers l'Europe · Q3 : elle part de Ceylan vers l'Europe · Q4 : elle arrive d'Europe à Ceylan · Q5 : elle arrive d'Europe à Ceylan · Q6 : elle arrive d'Europe à Ceylan
- **🧭 Timonier** (association) — le café de Ceylan → des plantations de la colonie vers Londres · les perles de Manaar → du banc de perles vers les marchands d'Europe · les tissus de coton → des usines anglaises vers les marchés de la colonie · les rails de chemin de fer → des forges anglaises vers les routes des plantations · les soldats et fonctionnaires → de Grande-Bretagne vers la colonie, pour la gouverner
- **🔭 Lieutenant** (qcm) — Q1 : un territoire dominé et gouverné par un pays étranger · Q2 : La colonie fournit des produits bruts bon marché et achète cher des produits fabriqués, au profit de la métropole. · Justification : « La métropole achète à bas prix les produits agricoles de la colonie et lui vend ses produits fabriqués : les profits reviennent surtout à la métropole et à ses marchands. »
- **🔱 Second** (tri) — Produit de la colonie (agricole ou brut) : le café, la cannelle, les perles · Produit fabriqué en métropole : les tissus de coton, les machines à vapeur · Contrôle de la colonie : le gouverneur britannique, les navires de guerre de la Royal Navy · Justification : « Ils assurent le contrôle de la colonie par la métropole : le Nautilus, navire d'un homme qui se dit du « pays des opprimés », y serait un ennemi. »

### Escale 6 — Le tunnel arabique et Suez · mot du journal : **ISTHME**

*Deuxième partie, ch. IV « La mer Rouge » et ch. V « Arabian-Tunnel » : Nemo fait passer le Nautilus de la mer Rouge à la Méditerranée par un tunnel sous l'isthme de Suez, alors que le canal est en construction.*

#### 6.1 Le passage secret — tunnel-arabique, objet « carte-route », Le professeur Aronnax

Compétence : Géographie : se déplacer — itinéraires, distances, canaux ; comment se déplace-t-on d'un bout à l'autre du monde ? · Fiche : Rayon Géographie, fiche 2 « Itinéraires et canaux »

- **🐚 Mousse** (qcm) — Q1 : de l'Afrique · Q2 : la mer Rouge et la mer Méditerranée
- **⚓ Matelot** (code) — Kilomètres économisés 19840
- **🧭 Timonier** (qcm) — Q1 : la Méditerranée à la mer Rouge, donc à l'océan Indien · Q2 : raccourcit le trajet de plusieurs milliers de kilomètres · Q3 : est une invention de Jules Verne
- **🔭 Lieutenant** (code) — Jours par le Cap 50 ; Jours par Suez 29 · Justification : « Un trajet plus court fait gagner du temps, du charbon et de l'argent : le canal de Suez rapproche l'Europe de l'Asie. »
- **🔱 Second** (qcm) — Q1 : entre l'Europe et l'Asie (Inde, Chine) · Q2 : le Royaume-Uni · Q3 : Moins de distance, c'est moins de charbon brûlé. · Justification : « Un trajet plus court fait gagner du temps, du charbon et de l'argent : le canal de Suez rapproche l'Europe de l'Asie. »

#### 6.2 Le fleuve et le désert — tunnel-arabique, objet « carte-nil », Conseil

Compétence : Géographie : les usages de l'eau douce ; repérer les principaux fleuves ; l'eau, ressource convoitée faisant l'objet de conflits d'usage. · Fiche : Rayon Géographie, fiche 3 « L'eau douce, une ressource convoitée »

- **🐚 Mousse** (tri) — Eau douce : l'eau du Nil, l'eau d'un puits, l'eau de pluie · Eau salée : l'eau de la mer Rouge, l'eau de la Méditerranée, l'eau de l'océan Indien
- **⚓ Matelot** (tri) — Usage de l'eau douce : boire, arroser les champs (irrigation), abreuver les troupeaux, naviguer sur le fleuve · Pas un usage de l'eau douce : pêcher la morue en mer, récolter le sel de mer
- **🧭 Timonier** (association) — Usage domestique → boire, cuisiner, se laver dans les villages · Agriculture → irriguer les champs de coton et de blé · Transport → les felouques qui descendent le fleuve · Industrie et énergie → aujourd'hui, l'électricité du barrage d'Assouan · Chantiers → le canal d'eau douce qui abreuvait les ouvriers de l'isthme
- **🔭 Lieutenant** (tri) — Conflit d'usage : un pays en amont construit un barrage ; le pays en aval craint de manquer d'eau, les villes et les agriculteurs se disputent l'eau pendant une sécheresse, une usine rejette ses eaux sales dans le fleuve où d'autres puisent leur eau · Simple usage, sans rivalité : un pêcheur pêche dans le fleuve en crue, où l'eau abonde, une famille puise l'eau d'un puits qui ne manque jamais · Justification : « Il y a conflit d'usage quand plusieurs utilisateurs veulent la même eau alors qu'il n'y en a pas assez pour tous, ou quand l'usage des uns gâte l'eau des autres. »
- **🔱 Second** (tri) — Éthiopie (amont) : « Nous avons besoin d'électricité pour nous développer. », « L'eau qui naît sur nos montagnes nous appartient aussi. » · Égypte (aval) : « Sans le Nil, notre pays est un désert. », « Si le réservoir se remplit trop vite, le débit baissera chez nous. » · Soudan (entre les deux) : « Un barrage en amont limitera nos inondations. » · Justification : « Elle est en aval : elle reçoit l'eau après les autres, et presque toute sa population dépend du fleuve dans un pays de désert. »

#### 6.3 Le plan d'évasion de Ned — pont-port-said, objet « lumieres-port », Ned Land

Compétence : Géographie : se déplacer — comment se déplace-t-on ailleurs ? quels moyens de transport, pour aller où ? · Fiche : Rayon Géographie, fiche 4 « Se déplacer »

- **🐚 Mousse** (association) — le paquebot à vapeur → pour traverser la mer · le train → pour traverser un pays par voie ferrée · la marche à pied → pour aller du quai à la gare
- **⚓ Matelot** (ordre) — 1. Gagner le port de Port-Saïd à la nage ou en canot. ; 2. Prendre un paquebot à vapeur pour traverser la Méditerranée jusqu'à Marseille. ; 3. Prendre le train à travers la France jusqu'au Havre. ; 4. Prendre un paquebot transatlantique jusqu'à Québec.
- **🧭 Timonier** (ordre) — 1. Du Nautilus au quai ; 2. Du quai à la gare maritime ; 3. De Port-Saïd à Marseille ; 4. De Marseille au Havre ; 5. Du Havre à Québec
- **🔭 Lieutenant** (ordre) — 1. Canot jusqu'au quai de Port-Saïd ; 2. Paquebot Port-Saïd → Marseille ; 3. Train Marseille → Paris → Le Havre ; 4. Paquebot Le Havre → Québec ; 5. Diligence ou train vers son village · Justification : « On choisit le moyen de transport selon la distance à parcourir, le milieu (mer ou terre) et ce qui existe à l'époque. »
- **🔱 Second** (code) — 20 jours = ? heures 480 ; Combien de fois plus long en 1868 ? 24 · Justification : « Les progrès des transports (vapeur, chemin de fer, puis avion) ont raccourci les durées de voyage : le monde paraît plus petit. »
