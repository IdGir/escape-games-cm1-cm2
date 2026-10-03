# ⚓ Vingt mille lieues sous les mers — Le Journal du Nautilus

Escape game immersif de cycle 3 (CM1-CM2), d'après le roman de Jules Verne (1869-1870, domaine public), **5 grades** de
difficulté, campagne prévue en **11 escales**. **État : escale pilote (escale 2) seule, en attente de validation.**

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
