# Guide pédagogique — Vingt mille lieues sous les mers, le Journal du Nautilus

> **État : escale pilote (escale 2) seule.** Les dix autres escales seront écrites après validation par l'enseignant
> (cahier des charges § 7.4). La matrice de couverture ci-dessous distingue ce qui est **fait** de ce qui est **prévu**.

## 1. Place dans les programmes

Cycle 3, CM1-CM2, différenciation de l'équivalent CE2 à l'équivalent 5ᵉ. Références reprises du dépôt (catalogue
`commun/donnees/catalogue.js`) : sciences et technologie, arrêté du 5 juin 2026 (BO n° 24 du 11 juin 2026), et programme
d'histoire-géographie `hg2026`. **Les libellés officiels n'ont pas pu être revérifiés sur education.gouv.fr (réseau bloqué
dans l'environnement de production) : voir A-VERIFIER.md.**

L'escale 2 travaille, en sciences et technologie :
- **L'électricité** (catalogue n° 14, Année A, P3) : conducteurs et isolants, circuit fermé/ouvert, série et dérivation,
  interrupteur, court-circuit et sécurité ;
- **Les objets techniques** (n° 04, Année A, P1) : fonction d'usage, instruments de mesure, lecture de graduations et d'unités ;
- **L'énergie** (thème « matière, mouvement, énergie », n° 09) : source, chaîne d'énergie, formes d'énergie.

Placement conseillé : P3 de l'Année A (avec « L'électricité ») ou en fin de P1 (après « L'Atelier de l'inventeur »).

## 2. Correspondance des grades (jamais affichée aux élèves)

| Grade | Équivalent | Ce qui change réellement dans l'escale 2 |
|---|---|---|
| 🐚 Mousse | ≈ CE2 | 6-8 objets à trier, une boucle à fermer, 3 instruments, 4 étapes ; premier indice offert, fiche mise en évidence, un choix faux écarté dans les QCM |
| ⚓ Matelot | ≈ CM1 | 8 objets, circuit en série avec interrupteur et pompe (la dérivation est refusée), 4 instruments dont manomètre et baromètre, 5 maillons |
| 🧭 Timonier | ≈ CM2 | pièges (graphite, eau de mer), deux lampes indépendantes (dérivation imposée), mesures à rattacher grâce aux **unités**, 6 maillons nommés par leur fonction |
| 🔭 Lieutenant | ≈ 6ᵉ | 10 objets dont le corps humain + **justification** ; dérivation + interrupteur qui ne commande que la pompe ; **calcul de profondeur** au manomètre ; texte à trous sur les **formes d'énergie** |
| 🔱 Second | ≈ 5ᵉ | carnet d'essais au galvanomètre (eau douce / eau de mer) ; repérer et retirer un fil de court-circuit ; pièges sur la pression de surface ; chaîne depuis la matière des piles ; justification |

Réglage : l'enseignant impose un grade à l'appareil (⚙️) ou laisse chaque équipe choisir ; depuis `prof.html`, il change le grade
d'une équipe à distance. En fin d'escale, « 🌊 Plonger plus profond » propose de rejouer au grade supérieur (sans classement).

## 3. Déroulé de l'escale pilote (≈ 25-30 min)

1. **Avant** (5 min) : imprimer la fiche de mission (⚙️ → Impressions), une par équipe ; rappeler les règles (10 / 3 / −2,
   Bibliothèque, mot à noter une seule fois).
2. **Cinématique** (≈ 30 s) : visite du salon, court-circuit, avarie.
3. **Quatre énigmes**, chacune ouverte en cliquant l'objet du décor désigné par le personnage :
   carré (tri), salle des machines (circuit), chambre de Nemo (instruments), grand salon (chaîne d'énergie).
4. **Fin** : le fragment `MOBILIS` s'affiche une seule fois → les élèves le notent ; journal de bord de l'équipe (imprimable).
5. **Après** (10 min) : mise en commun sur les « notions à revoir » du journal ; leçons A4 (`lecons-imprimables.html`).

**Faire utiliser les leçons** : la Bibliothèque (📚) contient tout ce qu'il faut, jamais la réponse toute faite. Les données
de Lieutenant et Second ne sont qu'en partie dans l'énoncé (carnet, manomètre, note du pilote) et se croisent avec la fiche.
Bonus « Bien documenté » : ouvrir la bonne fiche puis réussir du premier coup.

## 4. Matrice de couverture (provisoire)

| Point du programme | Escale | Énigme | Grades | État |
|---|---|---|---|---|
| Conducteurs et isolants ; sécurité électrique | 2 | e2-1 | tous | ✅ fait |
| Circuit fermé, série, dérivation, interrupteur, court-circuit | 2 | e2-2 | tous (série : Matelot ; dérivation : Timonier et plus) | ✅ fait |
| Objets techniques : fonction d'usage, instruments de mesure | 2 | e2-3 | tous | ✅ fait |
| Énergie : source, chaîne d'énergie, formes d'énergie | 2 | e2-4 | tous (formes : Lieutenant, Second) | ✅ fait |
| Âge industriel : machines à vapeur, transports | 1 | — | — | prévu |
| Repères géographiques, océans, latitude/longitude, courants | 3 | — | — | prévu |
| Louis XVI, Lumières, explorations, Révolution | 4 | — | — | prévu |
| Traite, colonies, abolition (1848), échanges | 5 | — | — | prévu |
| Canal de Suez, mobilités, échanges maritimes | 6 | — | — | prévu |
| Antiquité ; Terre active (volcans, séismes) | 7 | — | — | prévu |
| Vivant, biodiversité, écosystèmes, chaînes alimentaires | 8 | — | — | prévu |
| États de l'eau, saisons, Antarctique | 9 | — | — | prévu |
| Classification, régimes alimentaires, respiration | 10 | — | — | prévu |
| Louis XIV (1702), Europe, marées et courants | 11 | — | — | prévu |
| Moyen Âge, Gaule, Clovis, Renaissance, guerres mondiales, EMC | — | — | — | **non couvert à ce stade** ; ancrages à proposer après la pilote |

## 5. Évaluation et suivi

- Journal de bord par équipe (fin d'escale et ⚙️ → Impressions) : énigmes réussies du premier coup, erreurs, indices, fiches
  consultées, **notions à revoir** (renvoi à la fiche). Enregistré au format des autres jeux : visible dans `resultats.html`.
- Tableau de bord `prof.html` (mode local) : une carte par équipe, alertes (sas verrouillé, ≥ 4 erreurs, bloquée > 6 min),
  pause, minutes accordées, message, grade ; synthèse par notion ; export CSV ; impression.
- Corrigés des 5 grades : ⚙️ → Impressions → 🔑 Corrigés, et `README.md`.

## 6. Prolongements

Construire en classe les circuits de l'énigme 2 (piles 4,5 V, ampoules, interrupteurs) ; tester des objets conducteurs ;
lire un vrai baromètre ; lire l'extrait du roman (Partie I, ch. XII) ; débattre de ce que Verne imagine et de ce qui existait en
1869 (A-VERIFIER.md, « Fidélité au roman »).

## 7. Fiches d'ancrage des énigmes (générées depuis `enigmes.json`)

<!-- ANCRAGE:DEBUT -->

### e1-1 — Le livre de quart

| Champ | Contenu |
|---|---|
| `id` | e1-1 |
| `escale` | 1 |
| `decor` | pont-lincoln |
| `objets_cliquables` | livre-quart, loch, longue-vue (objet principal : livre-quart) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Une lueur bleuâtre file sous la surface, devant la frégate. Le commandant Farragut veut savoir s'il peut la rattraper avant l'aube. Aronnax ouvre le livre de quart, où l'officier note les heures et les distances relevées au loch : il faut en tirer des durées et des vitesses. |
| `enjeu` | Si la lueur est plus rapide, la chasse est perdue d'avance ; sinon, il faut forcer la marche tout de suite. |
| `episode_du_roman` | Partie I, ch. VI « À toute vapeur » : pendant des semaines, la frégate poursuit la lueur que l'on prend pour un animal ; elle ne parvient pas à la rattraper. |
| `competence_programme` | Sciences : mesurer une distance et une durée lors du déplacement d'un objet ; différents types de mouvement. |
| `pourquoi_ce_savoir_ici` | Pour savoir qui va le plus vite, il faut comparer les distances parcourues en une même durée : c'est exactement ce que note le livre de quart. |
| `reaction_du_decor` | Un tracé lumineux se dessine sur la mer : la route de la frégate et celle de la lueur. |
| `liberte_ou_anachronisme` | Les relevés du livre de quart sont inventés pour le jeu (nombres simples). Le nœud (1 mille marin par heure) et le mille marin (1 852 m) sont les vraies unités de la marine. |
| `niveau_variantes` | Mousse : lire une durée en heures, reconnaître un mouvement circulaire. Matelot : durée en minutes et distance en une heure. Timonier : deux vitesses en nœuds à comparer. Lieutenant : écart de distance après 3 h + type de mouvement + justification. Second : temps de rattrapage avec avance, conversion en km/h + justification. |
| `fiche de la Bibliothèque` | Rayon Navigation, fiche 2 « Mesurer un déplacement » |
| `types par grade` | 🐚 qcm · ⚓ code · 🧭 code · 🔭 qcm · 🔱 code |

### e1-2 — Forcer les feux

| Champ | Contenu |
|---|---|
| `id` | e1-2 |
| `escale` | 1 |
| `decor` | machines-vapeur |
| `objets_cliquables` | chaudiere, manometre-vapeur, chauffeur (objet principal : chaudiere) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Le commandant fait « forcer les feux » pour gagner de la vitesse. Dans la chaufferie, le mécanicien surveille le manomètre : trop de vapeur, et la chaudière peut exploser. Conseil, qui ne fait rien sans méthode, veut remettre dans l'ordre le trajet de l'énergie, du charbon jusqu'à l'hélice, pour savoir où agit chaque pelletée. |
| `enjeu` | Sans vitesse, la lueur s'échappe ; sans méthode, on pousse la chaudière au-delà du raisonnable. |
| `episode_du_roman` | Partie I, ch. VI « À toute vapeur » : le commandant Farragut fait pousser les feux au maximum pour atteindre l'animal. |
| `competence_programme` | Histoire : l'âge industriel — énergies et machines ; la machine à vapeur, révolution industrielle et progrès technique. |
| `pourquoi_ce_savoir_ici` | Comprendre la chaîne charbon → chaleur → vapeur → mouvement, c'est comprendre pourquoi « forcer les feux » fait avancer la frégate, et pourquoi cela a des limites. |
| `reaction_du_decor` | Les foyers rougeoient plus fort, un jet de vapeur siffle, la machine accélère. |
| `liberte_ou_anachronisme` | La salle des machines est celle d'une frégate à vapeur (charbon), pas celle du Nautilus, électrique : le contraste est voulu (voir escale 2). |
| `niveau_variantes` | Mousse : 4 étapes. Matelot : 5 étapes avec les pièces. Timonier : 6 étapes avec les transformations d'énergie. Lieutenant : texte à trous sur les formes d'énergie + justification. Second : QCM qui compare la frégate à vapeur et le Nautilus électrique + justification. |
| `fiche de la Bibliothèque` | Rayon Histoire, fiche 1 « La machine à vapeur » |
| `types par grade` | 🐚 ordre · ⚓ ordre · 🧭 ordre · 🔭 trous · 🔱 qcm |

### e1-3 — La cambuse

| Champ | Contenu |
|---|---|
| `id` | e1-3 |
| `escale` | 1 |
| `decor` | cambuse |
| `objets_cliquables` | etagere-vivres, tonneaux, biscuits (objet principal : etagere-vivres) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | La chasse peut durer des mois. Le cambusier doit savoir quels vivres consommer d'abord et lesquels garder pour la fin. Ned Land connaît la morue salée, mais les boîtes de fer-blanc et les bocaux, nouveautés du siècle, le laissent méfiant : il faut trier les vivres selon leur façon d'être conservés. |
| `enjeu` | Des vivres gâtés au milieu du Pacifique, c'est la faim et la maladie pour tout l'équipage. |
| `episode_du_roman` | Partie I, ch. IV-V : l'Abraham Lincoln part pour une campagne de plusieurs mois ; vraisemblance : une frégate de 1867 emporte salaisons, biscuit de mer et conserves. |
| `competence_programme` | Sciences : production et conservation des aliments (salaison, séchage, fumage, conserve) ; produits agricoles et produits transformés. |
| `pourquoi_ce_savoir_ici` | Savoir comment un aliment est conservé, c'est savoir combien de temps il tiendra en mer. |
| `reaction_du_decor` | La lanterne s'avive ; les rayons de la cambuse s'éclairent, rangés. |
| `liberte_ou_anachronisme` | La conserve en récipient fermé et chauffé (Nicolas Appert) date du début du XIXᵉ siècle ; la chèvre du bord est une vraisemblance. |
| `niveau_variantes` | Mousse : 3 aliments et leur méthode. Matelot : 5 aliments et leur méthode. Timonier : 5 méthodes et ce qu'elles font aux microbes. Lieutenant : QCM (scorbut, ce qui n'existait pas en 1867) + justification. Second : tri en trois colonnes (on retire l'eau / on chauffe et on ferme / frais) + justification. |
| `fiche de la Bibliothèque` | Rayon Vivant, fiche 1 « Conserver les aliments » |
| `types par grade` | 🐚 association · ⚓ association · 🧭 association · 🔭 qcm · 🔱 tri |

### e1-4 — Le harpon de Ned Land

| Champ | Contenu |
|---|---|
| `id` | e1-4 |
| `escale` | 1 |
| `decor` | pont-lincoln |
| `objets_cliquables` | harpon, lueur-mer, loch (objet principal : harpon) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | La frégate est enfin à portée. Ned Land lance son harpon : il rebondit en sonnant comme sur du métal. Avant que le commandant ne fasse donner le canon, il faut décider : cette « bête » est-elle un être vivant ou une machine ? |
| `enjeu` | Si c'est une machine, il y a des hommes à bord, et l'on tire peut-être sur un navire. |
| `episode_du_roman` | Partie I, ch. VI-VII : Ned Land lance son harpon, qui frappe un corps dur ; Aronnax, tombé à la mer, découvre ensuite des plaques de tôle boulonnées. |
| `competence_programme` | Sciences : caractéristiques du vivant (naître, grandir, se nourrir, respirer, se reproduire, mourir) ; distinguer un être vivant d'un objet technique. |
| `pourquoi_ce_savoir_ici` | Les indices observés ne prouvent pas tous la même chose : seuls les caractères du vivant permettent de trancher. |
| `reaction_du_decor` | Un choc ébranle la frégate ; une gerbe d'eau balaie le pont. |
| `liberte_ou_anachronisme` | La bioluminescence (lumière produite par des êtres vivants) est citée pour montrer qu'une lumière seule ne prouve rien. |
| `niveau_variantes` | Mousse : êtres vivants ou objets fabriqués. Matelot : caractères du vivant ou de l'objet technique. Timonier et Lieutenant : indices sur le « monstre » en 3 colonnes, dont « ne permet pas de conclure » (+ justification pour Lieutenant). Second : QCM sur la preuve et le contre-exemple + justification. |
| `fiche de la Bibliothèque` | Rayon Vivant, fiche 2 « Être vivant ou objet ? » |
| `types par grade` | 🐚 tri · ⚓ tri · 🧭 tri · 🔭 tri · 🔱 qcm |

### e2-1 — Le câble brûlé du carré

| Champ | Contenu |
|---|---|
| `id` | e2-1 |
| `escale` | 2 |
| `decor` | carre |
| `objets_cliquables` | table, journal, tableau-cadrans (objet principal : table) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Un câble a perdu sa gaine et touché la table mouillée : court-circuit, début d'incendie, journal de bord et cartes brûlés. Pour refaire un câble, Conseil veut trier les objets posés sur la table : ceux qui laissent passer le courant (pour l'âme du câble) et ceux qui l'arrêtent (pour la gaine). |
| `enjeu` | Sans câble neuf, le courant ne peut pas revenir : pas de lumière, pas de pompe à air. |
| `episode_du_roman` | Partie I, ch. XII « Tout par l'électricité » : tout, à bord, fonctionne à l'électricité (vraisemblance : un câble abîmé suffit à tout arrêter). L'avarie elle-même est une invention du jeu. |
| `competence_programme` | Électricité : distinguer conducteurs et isolants ; connaître les dangers de l'électricité (court-circuit, eau salée). |
| `pourquoi_ce_savoir_ici` | Un câble, c'est une âme qui conduit et une gaine qui isole : on ne peut pas le refaire sans savoir quels matériaux laissent passer le courant. |
| `reaction_du_decor` | Un câble neuf (cuivre gainé de caoutchouc) apparaît sur la table ; la fumée du carré se dissipe. |
| `liberte_ou_anachronisme` | Avarie inventée (court-circuit, début d'incendie). Isolation simplifiée : les câbles sous-marins des années 1858-1866 étaient isolés à la gutta-percha ; le jeu parle de caoutchouc, isolant connu des élèves (voir A-VERIFIER.md). |
| `niveau_variantes` | Mousse : 6 objets. Matelot : 8 objets. Timonier : 9 objets dont la mine de crayon et l'eau de mer. Lieutenant : 10 objets + justification. Second : QCM sur le carnet d'essais de Conseil (galvanomètre) + justification. |
| `fiche de la Bibliothèque` | Rayon Électricité, fiche 1 « Conducteurs et isolants » |
| `types par grade` | 🐚 tri · ⚓ tri · 🧭 tri · 🔭 tri · 🔱 qcm |

### e2-2 — Le tableau de laiton

| Champ | Contenu |
|---|---|
| `id` | e2-2 |
| `escale` | 2 |
| `decor` | machines |
| `objets_cliquables` | tableau-bornes, accumulateurs, cadrans (objet principal : tableau-bornes) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Les piles du bord sont chargées, mais pendant l'avarie l'équipage a débranché les bornes du grand tableau de laiton. Le courant ne va plus nulle part : il faut reconnecter le circuit pour rallumer le grand salon et relancer la pompe à air, sans recréer de court-circuit. |
| `enjeu` | Tant que la pompe à air ne tourne pas, la réserve d'air du Nautilus continue de baisser. |
| `episode_du_roman` | Partie I, ch. XII « Tout par l'électricité » : Nemo explique que l'électricité l'éclaire, le chauffe et anime ses machines, et qu'il la tire de piles au sodium. |
| `competence_programme` | Électricité : réaliser un circuit électrique fermé ; circuits en série et en dérivation ; rôle de l'interrupteur ; court-circuit. |
| `pourquoi_ce_savoir_ici` | Les bornes ne servent à rien si l'on ne sait pas faire une boucle fermée ; et pour que le salon ne retombe pas dans le noir à la première ampoule grillée, il faut savoir monter en dérivation. |
| `reaction_du_decor` | Les ampoules du tableau s'allument, le bourdonnement des bobines monte, la pompe à air ronronne ; la jauge d'air cesse de baisser. |
| `liberte_ou_anachronisme` | Le tableau à bornes et les ampoules sont une représentation simplifiée : Verne parle de piles au sodium et de lampes électriques ; les ampoules à filament pratiques datent de 1879 (Edison, Swan), après le roman. Écart signalé dans A-VERIFIER.md. |
| `niveau_variantes` | Mousse : fermer la boucle d'une lampe. Matelot : pile, interrupteur, lampe et pompe en une boucle. Timonier : deux lampes qui restent indépendantes (dérivation). Lieutenant : dérivation + interrupteur qui ne commande que la pompe + justification. Second : idem + un fil de secours dangereux à repérer et retirer + justification. |
| `fiche de la Bibliothèque` | Rayon Électricité, fiche 2 « Le circuit électrique » |
| `types par grade` | 🐚 circuit · ⚓ circuit · 🧭 circuit · 🔭 circuit · 🔱 circuit |

### e2-3 — Le mur des instruments

| Champ | Contenu |
|---|---|
| `id` | e2-3 |
| `escale` | 2 |
| `decor` | cabine |
| `objets_cliquables` | mur-instruments, bureau, hublot-cabine (objet principal : mur-instruments) |
| `personnage_emetteur` | Le capitaine Nemo |
| `probleme_narratif` | La lumière est revenue, mais l'incendie a consumé de l'air : il faut remonter en refaire provision. Les cartes ont brûlé. Nemo a rejoint la cage du pilote et, par le porte-voix, réclame des mesures que l'on ne peut lire que sur le mur d'instruments de sa chambre. Les mousses, nouveaux à bord, doivent d'abord savoir quel instrument donne quelle mesure. |
| `enjeu` | Remonter sans connaître la profondeur ni l'état de la mer en surface, c'est risquer de jaillir trop vite ou en pleine tempête. |
| `episode_du_roman` | Partie I, ch. XII : dans sa chambre, Nemo montre à Aronnax les instruments nécessaires à la navigation (thermomètre, baromètre, boussole, sextant, chronomètres, lunettes…) et le manomètre, qui lui donne la profondeur par la pression de l'eau. Le porte-voix vers la cage du pilote est une vraisemblance (à vérifier). |
| `competence_programme` | Objets techniques : identifier la fonction d'usage d'un objet ; réaliser et exploiter des mesures (instruments de mesure, lecture d'une graduation). |
| `pourquoi_ce_savoir_ici` | Sans cartes, seuls les instruments disent où l'on est : il faut savoir à quoi sert chacun pour transmettre la bonne mesure au pilote. |
| `reaction_du_decor` | Les aiguilles des instruments s'animent ; le pilote reçoit les mesures. |
| `liberte_ou_anachronisme` | Lieutenant et Second : la règle « environ 1 atmosphère de plus tous les 10 m d'eau de mer » est une notion de collège, donnée dans la fiche (document à exploiter). |
| `niveau_variantes` | Mousse : 3 instruments. Matelot : 4 (manomètre, baromètre). Timonier : 5 mesures lues à rattacher à leur instrument grâce aux unités. Lieutenant : lecture du manomètre et calcul de la profondeur + justification. Second : trois documents (manomètre, baromètre, remontée) avec pièges sur la pression de surface + justification. |
| `fiche de la Bibliothèque` | Rayon Navigation, fiche 1 « Les instruments du bord » |
| `types par grade` | 🐚 association · ⚓ association · 🧭 association · 🔭 qcm · 🔱 qcm |

### e2-4 — L'épure du capitaine

| Champ | Contenu |
|---|---|
| `id` | e2-4 |
| `escale` | 2 |
| `decor` | salon |
| `objets_cliquables` | epure, hublots, orgue, vitrines (objet principal : epure) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | Pendant la panne, l'hélice s'est arrêtée : le Nautilus dérive. Sur le divan du salon, l'épure (plan et coupe) que Nemo a montrée plus tôt. Ned Land s'impatiente : il faut retrouver le chemin de l'énergie, des piles jusqu'à l'hélice, pour savoir quoi remettre en marche, dans quel ordre. |
| `enjeu` | Sans hélice, le Nautilus ne peut ni se diriger ni gagner une surface sûre pour renouveler son air ; et Ned Land n'aura jamais sa chance de s'évader. |
| `episode_du_roman` | Partie I, ch. XIII « Quelques chiffres » : assis dans le salon, Nemo montre à Aronnax une épure du Nautilus (plan, coupe, élévation) et explique que ses piles font tourner l'hélice. |
| `competence_programme` | Objets techniques et énergie : identifier la source d'énergie d'un objet ; ordonner une chaîne d'énergie (stocker, commander, distribuer, convertir, transmettre, agir) ; formes d'énergie. |
| `pourquoi_ce_savoir_ici` | Pour relancer une machine, il faut suivre le trajet de l'énergie dans l'ordre : on ne réenclenche pas l'hélice avant d'avoir rétabli la commande et le courant. |
| `reaction_du_decor` | Vibration de l'hélice, les panneaux de fer des hublots glissent, l'océan apparaît éclairé par le fanal ; le Nautilus remonte et la jauge d'air se remplit. |
| `liberte_ou_anachronisme` | Simplification : Verne décrit des électro-aimants, leviers et engrenages plutôt qu'un « moteur électrique » ; le jeu emploie le vocabulaire de l'école. Second : le sel de la mer fournit la matière du sodium ; Verne précise que l'extraction demande du charbon (à vérifier, A-VERIFIER.md). |
| `niveau_variantes` | Mousse : 4 étapes en mots simples. Matelot : 5 étapes. Timonier : 6 étapes nommées par leur fonction. Lieutenant : texte à trous sur les formes d'énergie + justification. Second : 7 étapes depuis le sel de la mer + justification. |
| `fiche de la Bibliothèque` | Rayon Électricité, fiche 3 « La chaîne d'énergie » |
| `types par grade` | 🐚 ordre · ⚓ ordre · 🧭 ordre · 🔭 trous · 🔱 ordre |

### e3-1 — Les réservoirs d'air

| Champ | Contenu |
|---|---|
| `id` | e3-1 |
| `escale` | 3 |
| `decor` | sas |
| `objets_cliquables` | scaphandres, porte-sas, niveau-eau (objet principal : scaphandres) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | Le capitaine Nemo invite à chasser dans sa forêt sous-marine. Dans le vestiaire, chacun reçoit un scaphandre et un réservoir d'air comprimé. Ned Land se méfie : il ne voit rien dans son réservoir, il le croit vide, et refuse de sortir sans preuve. Avant de remplir le sas d'eau, il faut prouver ce que contient un réservoir. |
| `enjeu` | Sortir avec un réservoir vide, c'est l'asphyxie au fond de la mer. |
| `episode_du_roman` | Partie I, ch. XVI « Promenade en plaine » : avant de sortir, Aronnax revêt un scaphandre muni d'un réservoir d'air comprimé ; le sas se remplit d'eau. |
| `competence_programme` | Sciences : états et constitution de la matière à l'échelle macroscopique ; l'air est de la matière (il occupe de l'espace, il a une masse, il se comprime) ; propriétés des solides, liquides et gaz. |
| `pourquoi_ce_savoir_ici` | On ne voit pas l'air : seules ses propriétés (masse, volume, compressibilité) permettent de savoir s'il est là. |
| `reaction_du_decor` | La porte ronde du sas pivote : l'eau envahit le sas, les bulles montent. |
| `liberte_ou_anachronisme` | Les masses et volumes des réservoirs sont des nombres du jeu ; la masse d'un litre d'air (environ 1,2 g) est réelle. |
| `niveau_variantes` | Mousse : vrai/faux sur l'air. Matelot : comparer deux masses à la balance. Timonier : trier solides, liquides, gaz par leurs propriétés. Lieutenant : calcul de la masse d'air comprimé + justification. Second : QCM (masse, compressibilité) + justification. |
| `fiche de la Bibliothèque` | Rayon Matière et lumière, fiche 1 « L'air, c'est de la matière » |
| `types par grade` | 🐚 vraifaux · ⚓ qcm · 🧭 tri · 🔭 code · 🔱 qcm |

### e3-2 — La plaine aux mille couleurs

| Champ | Contenu |
|---|---|
| `id` | e3-2 |
| `escale` | 3 |
| `decor` | recif |
| `objets_cliquables` | faune-recif, tortue, etoile-mer (objet principal : faune-recif) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Sur la plaine sous-marine, Conseil voudrait tout classer pour le musée du capitaine, mais on ne parle pas sous un casque de cuivre : il faut se mettre d'accord avant de remonter sur ce qui ira dans chaque vitrine. Le capitaine ne gardera qu'une collection bien rangée. |
| `enjeu` | Une collection mal classée sera refusée par le capitaine, et la sortie n'aura servi à rien. |
| `episode_du_roman` | Partie I, ch. XVI « Promenade en plaine » : Aronnax et Conseil traversent une plaine couverte d'êtres marins de toutes sortes ; Conseil, grand classificateur, ne peut s'empêcher de les ranger. |
| `competence_programme` | Sciences : panorama du vivant ; organisation des êtres vivants (classer selon les caractères partagés) ; biodiversité. |
| `pourquoi_ce_savoir_ici` | Classer, c'est regrouper les êtres vivants par ce qu'ils ont en commun : exactement le travail d'un musée. |
| `reaction_du_decor` | Un banc de poissons argentés s'ouvre et se referme ; la plaine scintille. |
| `liberte_ou_anachronisme` | Les animaux représentés sont ceux d'un récif tropical du Pacifique, cohérents avec le lieu. |
| `niveau_variantes` | Mousse : trouver l'intrus parmi des poissons. Matelot : vertébrés et invertébrés. Timonier : associer chaque groupe à son caractère. Lieutenant : intrus (le dauphin) + justification. Second : groupes emboîtés en 3 colonnes + justification. |
| `fiche de la Bibliothèque` | Rayon Vivant, fiche 3 « Classer le vivant » |
| `types par grade` | 🐚 intrus · ⚓ tri · 🧭 association · 🔭 intrus · 🔱 tri |

### e3-3 — La lampe dans la forêt

| Champ | Contenu |
|---|---|
| `id` | e3-3 |
| `escale` | 3 |
| `decor` | foret-crespo |
| `objets_cliquables` | lampe-ruhmkorff, gorgone, rayons-surface (objet principal : lampe-ruhmkorff) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Dans la forêt sous-marine, la lumière baisse avec la profondeur. Une gorgone qu'on disait rouge vif paraît grise ; le capitaine fait signe d'allumer les lampes électriques. Aronnax, fasciné, veut comprendre où sont passées les couleurs avant de décider s'il faut continuer à descendre ou remonter. |
| `enjeu` | Sans comprendre la lumière, on se perd dans l'obscurité : ici, on ne retrouve son chemin qu'en voyant. |
| `episode_du_roman` | Partie I, ch. XVII « Une forêt sous-marine » : la lumière diminue avec la profondeur ; les promeneurs allument leurs lampes électriques (appareils de Ruhmkorff). |
| `competence_programme` | Sciences : la lumière — sources de lumière et objets éclairés, propagation rectiligne, ombres, absorption de la lumière par l'eau. |
| `pourquoi_ce_savoir_ici` | Savoir comment la lumière voyage et s'éteint dans l'eau, c'est savoir ce qu'on voit vraiment, et quand allumer sa lampe. |
| `reaction_du_decor` | Les lampes s'allument : la gorgone retrouve son rouge, la forêt sort de l'ombre. |
| `liberte_ou_anachronisme` | Les profondeurs indiquées pour la disparition des couleurs sont des ordres de grandeur (voir A-VERIFIER.md). |
| `niveau_variantes` | Mousse : sources de lumière et objets éclairés. Matelot : vrai/faux sur la propagation et l'ombre. Timonier : ordre de disparition des couleurs. Lieutenant : QCM sur la gorgone grise + justification. Second : lecture d'un tableau de profondeurs (code) + justification. |
| `fiche de la Bibliothèque` | Rayon Matière et lumière, fiche 2 « La lumière sous la mer » |
| `types par grade` | 🐚 tri · ⚓ vraifaux · 🧭 ordre · 🔭 qcm · 🔱 code |

### e4-1 — Les instruments engloutis

| Champ | Contenu |
|---|---|
| `id` | e4-1 |
| `escale` | 4 |
| `decor` | epave-vanikoro |
| `objets_cliquables` | instruments-epave, canons, coque (objet principal : instruments-epave) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Sous le Nautilus, une épave couverte de coraux. Quels navires étaient-ce ? Aronnax aperçoit dans le sable un compas et un sextant : en reconnaissant ces instruments et leur usage, on comprendra que l'on se trouve sur les restes d'une grande expédition d'exploration, dont les navires portaient les noms mêmes de deux instruments. |
| `enjeu` | Identifier l'épave, c'est résoudre l'un des grands mystères de la marine française. |
| `episode_du_roman` | Partie I, ch. XIX « Vanikoro » : le Nautilus survole les épaves des deux navires de Lapérouse, La Boussole et L'Astrolabe, perdus en 1788. |
| `competence_programme` | Histoire : les progrès techniques qui ont permis aux Européens de s'aventurer vers de nouveaux territoires (boussole, astrolabe, sextant, chronomètre, cartes). |
| `pourquoi_ce_savoir_ici` | Ces instruments sont ceux des explorateurs : savoir à quoi ils servaient, c'est reconnaître une expédition. |
| `reaction_du_decor` | Le sable se soulève ; la boussole et le sextant brillent sous le fanal. |
| `liberte_ou_anachronisme` | Lieutenant et Second : le calcul de la longitude par le chronomètre (15° par heure) est une notion de collège, donnée dans la fiche. |
| `niveau_variantes` | Mousse : 3 instruments. Matelot : 4 instruments. Timonier : 5 instruments dont le chronomètre. Lieutenant : QCM sur la latitude et la longitude + justification. Second : calcul d'une longitude par l'heure (code) + justification. |
| `fiche de la Bibliothèque` | Rayon Histoire, fiche 2 « Les instruments des explorateurs » |
| `types par grade` | 🐚 association · ⚓ association · 🧭 association · 🔭 qcm · 🔱 code |

### e4-2 — La boîte de fer-blanc

| Champ | Contenu |
|---|---|
| `id` | e4-2 |
| `escale` | 4 |
| `decor` | cabine |
| `objets_cliquables` | bureau, mur-instruments, hublot-cabine (objet principal : bureau) |
| `personnage_emetteur` | Le capitaine Nemo |
| `probleme_narratif` | Dans sa chambre, Nemo ouvre une boîte de fer-blanc trouvée dans l'épave : les instructions de l'expédition, annotées de la main du roi Louis XVI. Les feuillets se sont mélangés : pour les ranger dans les archives du Nautilus, il faut remettre les événements dans l'ordre, de l'avènement du roi jusqu'à la découverte des épaves. |
| `enjeu` | Mal datés, ces documents uniques perdraient leur valeur de preuve. |
| `episode_du_roman` | Partie I, ch. XIX « Vanikoro » : Nemo montre une boîte de fer-blanc aux armes de France, contenant les instructions du ministère de la Marine annotées par Louis XVI. |
| `competence_programme` | Histoire : le temps de la Révolution ; contexte du royaume en 1789 ; fin de la monarchie absolue et de l'Ancien Régime ; repères chronologiques. |
| `pourquoi_ce_savoir_ici` | Ranger des archives, c'est se repérer dans le temps : l'expédition partie sous un roi absolu disparaît juste avant la Révolution. |
| `reaction_du_decor` | Les feuillets se rangent ; les horloges du mur sonnent l'heure. |
| `liberte_ou_anachronisme` | Le mot de Louis XVI demandant des nouvelles de Lapérouse avant sa mort est rapporté par la tradition (voir A-VERIFIER.md) ; il n'est pas utilisé comme preuve. |
| `niveau_variantes` | Mousse : 4 événements. Matelot : 5. Timonier : 6 avec dates. Lieutenant : 7 avec dates + justification. Second : 7 événements sans dates, à retrouver avec la fiche + justification. |
| `fiche de la Bibliothèque` | Rayon Histoire, fiche 3 « Lapérouse et la Révolution » |
| `types par grade` | 🐚 ordre · ⚓ ordre · 🧭 ordre · 🔭 ordre · 🔱 ordre |

### e4-3 — Les papiers d'un autre monde

| Champ | Contenu |
|---|---|
| `id` | e4-3 |
| `escale` | 4 |
| `decor` | carre |
| `objets_cliquables` | table, tableau-cadrans, journal (objet principal : table) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Au fond de la boîte, d'autres papiers : certains parlent de privilèges et d'un roi « par la grâce de Dieu », d'autres d'égalité et de nation. Conseil, chargé de les archiver, veut les séparer : ceux de l'ancien royaume et ceux des temps nouveaux. Il les étale sur la table du carré. |
| `enjeu` | Mélanger ces papiers, ce serait mélanger deux mondes que la Révolution a séparés. |
| `episode_du_roman` | Vraisemblance : la boîte de Lapérouse contient des papiers officiels (Partie I, ch. XIX) ; Conseil classe tout ce qui lui passe entre les mains. |
| `competence_programme` | Histoire : la société d'Ancien Régime (trois ordres, privilèges) ; fin de la monarchie absolue ; affirmation des nouveaux principes (Déclaration des droits de l'homme et du citoyen). |
| `pourquoi_ce_savoir_ici` | Pour archiver ces papiers, il faut reconnaître ce qui appartient à l'Ancien Régime et ce qu'a apporté 1789. |
| `reaction_du_decor` | Les papiers se rangent en deux piles nettes ; la lampe s'avive. |
| `liberte_ou_anachronisme` | Les papiers postérieurs à 1788 n'ont pas pu se trouver dans la boîte : ils sont présentés comme les documents que Nemo y a ajoutés pour comparer (vraisemblance assumée). |
| `niveau_variantes` | Mousse : avant / après 1789, 4 papiers. Matelot : les trois ordres. Timonier : Ancien Régime / nouveaux principes. Lieutenant : idem, plus difficile + justification. Second : QCM sur privilèges et égalité + justification. |
| `fiche de la Bibliothèque` | Rayon Histoire, fiche 4 « L'Ancien Régime et 1789 » |
| `types par grade` | 🐚 tri · ⚓ tri · 🧭 tri · 🔭 tri · 🔱 qcm |

### e5-1 — La perle géante

| Champ | Contenu |
|---|---|
| `id` | e5-1 |
| `escale` | 5 |
| `decor` | banc-perles |
| `objets_cliquables` | huitre-geante, banc, requin (objet principal : huitre-geante) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Dans une grotte, le capitaine montre une huître géante qui cache une perle énorme. Conseil a pesé, à bord, les perles ramassées sur le banc ; le capitaine affirme que la sienne pèse plus que toutes réunies. Avant de remonter, il faut comparer les masses notées dans le carnet de Conseil. |
| `enjeu` | Le capitaine laisse sa perle grandir ; il ne la confiera qu'à qui sait mesurer avec rigueur. |
| `episode_du_roman` | Partie II, ch. III « Une perle de dix millions » : dans une grotte, Nemo montre à Aronnax une huître gigantesque contenant une perle énorme, qu'il laisse grossir. |
| `competence_programme` | Sciences : comparer et mesurer des masses (balance, unités g et kg) ; propriétés de la matière. |
| `pourquoi_ce_savoir_ici` | « Plus lourd », « plus léger » : seule une mesure dans la même unité permet de comparer des perles si différentes. |
| `reaction_du_decor` | La valve de l'huître s'entrouvre : la perle luit sous le fanal. |
| `liberte_ou_anachronisme` | Les masses du carnet de Conseil sont inventées pour le jeu. |
| `niveau_variantes` | Mousse : lire une balance, choisir l'instrument. Matelot : ranger 5 masses (g et kg). Timonier : additionner et convertir (code). Lieutenant : équilibre d'une balance de Roberval + justification. Second : masse par différence (code) + justification. |
| `fiche de la Bibliothèque` | Rayon Matière et lumière, fiche 3 « Mesurer des masses » |
| `types par grade` | 🐚 qcm · ⚓ ordre · 🧭 code · 🔭 qcm · 🔱 code |

### e5-2 — Le pêcheur de perles

| Champ | Contenu |
|---|---|
| `id` | e5-2 |
| `escale` | 5 |
| `decor` | banc-perles |
| `objets_cliquables` | pecheur, banc, requin (objet principal : pecheur) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | Un pêcheur indien plonge sans scaphandre, une pierre au pied, pour quelques huîtres. Un requin l'attaque ; le capitaine et Ned Land le sauvent, et Nemo lui donne un sac de perles. Ned, révolté, veut comprendre : pourquoi cet homme risque-t-il sa vie pour si peu, quand d'autres s'enrichissent de son travail ? Avant de repartir, il faut mesurer ces inégalités. |
| `enjeu` | Ned refuse de repartir sans comprendre ; Nemo, lui, se dit « de ce pays-là », celui des opprimés. |
| `episode_du_roman` | Partie II, ch. III : Nemo et Ned Land sauvent un pêcheur de perles attaqué par un requin ; Nemo lui donne un sachet de perles et se dit du « pays des opprimés ». |
| `competence_programme` | Géographie : les inégalités dans le monde — identifier les manifestations des inégalités de niveau de vie ; localiser les grandes aires géographiques. |
| `pourquoi_ce_savoir_ici` | Mesurer la pauvreté ou la richesse d'un pays demande des indicateurs : on ne peut pas juger à l'œil. |
| `reaction_du_decor` | Le requin s'éloigne ; le pêcheur remonte vers la lumière. |
| `liberte_ou_anachronisme` | Les indicateurs d'aujourd'hui (espérance de vie, école, eau potable) sont un dossier de l'équipe de secours (XXIᵉ siècle) ; les pays A et B du tableau sont fictifs. |
| `niveau_variantes` | Mousse : signes de vie difficile ou aisée. Matelot : indicateurs de niveau de vie. Timonier : tableau de deux pays fictifs. Lieutenant : aires géographiques et indicateurs + justification. Second : QCM sur les indicateurs et leurs pièges + justification. |
| `fiche de la Bibliothèque` | Rayon Géographie, fiche 1 « Les inégalités dans le monde » |
| `types par grade` | 🐚 tri · ⚓ tri · 🧭 tri · 🔭 tri · 🔱 qcm |

### e5-3 — Les voiles de Ceylan

| Champ | Contenu |
|---|---|
| `id` | e5-3 |
| `escale` | 5 |
| `decor` | pont-ceylan |
| `objets_cliquables` | barques, cage-pilote, fanal (objet principal : barques) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Le Nautilus fait surface au large de Ceylan. Des voiles partout : barques de pêcheurs et navires de commerce de la colonie britannique. Le capitaine ne veut croiser aucun navire de commerce. Aronnax, à la longue-vue, classe les cargaisons pour savoir quels bateaux partent vers l'Europe et lesquels en reviennent. |
| `enjeu` | Se faire voir d'un navire de la colonie, c'est révéler le Nautilus au monde. |
| `episode_du_roman` | Partie II, ch. II-III : le Nautilus croise au large de Ceylan, colonie britannique, près des bancs de perles de Manaar ; Nemo évite les navires. |
| `competence_programme` | Histoire : les échanges commerciaux avec les colonies (produits des colonies vers l'Europe, produits manufacturés vers les colonies). |
| `pourquoi_ce_savoir_ici` | Savoir ce que transportent les navires, c'est savoir d'où ils viennent et où ils vont, donc lesquels éviter. |
| `reaction_du_decor` | Une route se dessine sur la mer : des navires vers l'Europe, d'autres vers Ceylan. |
| `liberte_ou_anachronisme` | Ceylan exportait surtout du café, de la cannelle et des perles vers 1868 ; le thé ne l'emportera qu'après 1880 (A-VERIFIER.md). |
| `niveau_variantes` | Mousse : produit et lieu d'origine. Matelot : marchandises qui partent ou arrivent. Timonier : association produit ↔ origine et destination. Lieutenant : QCM sur la colonie et l'échange inégal + justification. Second : tri en trois colonnes + justification. |
| `fiche de la Bibliothèque` | Rayon Histoire, fiche 5 « Colonies et échanges » |
| `types par grade` | 🐚 association · ⚓ qcm · 🧭 association · 🔭 qcm · 🔱 tri |

### e6-1 — Le passage secret

| Champ | Contenu |
|---|---|
| `id` | e6-1 |
| `escale` | 6 |
| `decor` | tunnel-arabique |
| `objets_cliquables` | carte-route, gouvernail, vitres-tunnel (objet principal : carte-route) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Aronnax ne croit pas au « tunnel arabique » : pour passer de la mer Rouge à la Méditerranée, il faudrait contourner toute l'Afrique. Dans la cage du pilote, la carte de route permet de comparer les itinéraires avant que Nemo ne lance le Nautilus dans le courant. |
| `enjeu` | Si Aronnax ne mesure pas ce que l'isthme fait gagner, il prend le capitaine pour un fou ; or ce raccourci secret est l'avance du Nautilus sur tous les navires du monde. |
| `episode_du_roman` | Partie II, ch. V « Arabian-Tunnel » : Nemo révèle un passage souterrain sous l'isthme de Suez ; Aronnax n'y croyait pas. |
| `competence_programme` | Géographie : se déplacer — itinéraires, distances, canaux ; comment se déplace-t-on d'un bout à l'autre du monde ? |
| `pourquoi_ce_savoir_ici` | Comparer des itinéraires sur une carte, c'est comprendre pourquoi un passage par l'isthme change tout pour la navigation. |
| `reaction_du_decor` | La route du Nautilus s'illumine sur la carte, sous l'isthme. |
| `liberte_ou_anachronisme` | Le tunnel arabique est une invention de Verne : il n'existe pas. Le canal de Suez, lui, est inauguré le 17 novembre 1869. Les distances sont des ordres de grandeur (A-VERIFIER.md). |
| `niveau_variantes` | Mousse : lire la carte (contourner l'Afrique). Matelot : différence de distances. Timonier : QCM sur la carte et le canal. Lieutenant : durées de trajet selon la vitesse (code) + justification. Second : QCM sur les échanges que change le canal + justification. |
| `fiche de la Bibliothèque` | Rayon Géographie, fiche 2 « Itinéraires et canaux » |
| `types par grade` | 🐚 qcm · ⚓ code · 🧭 qcm · 🔭 code · 🔱 qcm |

### e6-2 — Le fleuve et le désert

| Champ | Contenu |
|---|---|
| `id` | e6-2 |
| `escale` | 6 |
| `decor` | tunnel-arabique |
| `objets_cliquables` | carte-nil, gouvernail, vitres-tunnel (objet principal : carte-nil) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Sur l'autre carte du pilote, Conseil remarque un mince trait bleu : un canal d'eau douce creusé depuis le Nil pour abreuver les milliers d'ouvriers du canal, en plein désert. Il veut classer les usages de cette eau rare, car le Nautilus, lui, doit fabriquer la sienne en distillant l'eau de mer. |
| `enjeu` | Mal partagée, l'eau douce manque toujours à quelqu'un : ouvriers de l'isthme, paysans du Nil… ou équipage du Nautilus. |
| `episode_du_roman` | Vraisemblance : Partie II, ch. IV-V, le Nautilus longe l'isthme de Suez où l'on creuse le canal ; un canal d'eau douce, venu du Nil, alimentait réellement les chantiers (1863). |
| `competence_programme` | Géographie : les usages de l'eau douce ; repérer les principaux fleuves ; l'eau, ressource convoitée faisant l'objet de conflits d'usage. |
| `pourquoi_ce_savoir_ici` | Dans un pays de désert, chaque usage de l'eau du fleuve compte : c'est là que naissent les conflits d'usage. |
| `reaction_du_decor` | Le trait bleu du Nil s'illumine sur la carte. |
| `liberte_ou_anachronisme` | Le barrage d'Assouan (1970) et le grand barrage éthiopien sont présentés comme un dossier de l'équipe de secours (XXIᵉ siècle). |
| `niveau_variantes` | Mousse : eau douce ou salée. Matelot : usages de l'eau douce. Timonier : association usage ↔ exemple au bord du Nil. Lieutenant : conflit d'usage ou non + justification. Second : tri des acteurs du conflit du Nil + justification. |
| `fiche de la Bibliothèque` | Rayon Géographie, fiche 3 « L'eau douce, une ressource convoitée » |
| `types par grade` | 🐚 tri · ⚓ tri · 🧭 association · 🔭 tri · 🔱 tri |

### e6-3 — Le plan d'évasion de Ned

| Champ | Contenu |
|---|---|
| `id` | e6-3 |
| `escale` | 6 |
| `decor` | pont-port-said |
| `objets_cliquables` | lumieres-port, canal, lanterne (objet principal : lumieres-port) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | Le Nautilus fait surface devant Port-Saïd, la nuit. Ned Land voit les lumières de la ville et rêve de s'évader jusqu'au Canada. Mais par où, et comment ? Il faut choisir, pour chaque étape du voyage, le moyen de transport adapté à la distance et au lieu. |
| `enjeu` | Un mauvais plan, et Ned se jette à l'eau pour rien : l'évasion échoue avant de commencer. |
| `episode_du_roman` | Partie II, ch. V-VI : le Nautilus débouche en Méditerranée près de Port-Saïd ; Ned Land pense sans cesse à s'évader. |
| `competence_programme` | Géographie : se déplacer — comment se déplace-t-on ailleurs ? quels moyens de transport, pour aller où ? |
| `pourquoi_ce_savoir_ici` | Choisir un moyen de transport, c'est tenir compte de la distance, du lieu (mer, terre) et de l'époque. |
| `reaction_du_decor` | Un itinéraire en pointillés se trace de Port-Saïd vers l'ouest. |
| `liberte_ou_anachronisme` | Les moyens de transport de 1868 sont ceux du roman ; la comparaison avec aujourd'hui (avion) est signalée comme dossier du XXIᵉ siècle. |
| `niveau_variantes` | Mousse : moyen de transport ↔ lieu. Matelot : étapes du voyage dans l'ordre. Timonier : étapes avec le moyen adapté. Lieutenant : idem avec durées + justification. Second : comparer 1868 et aujourd'hui (code) + justification. |
| `fiche de la Bibliothèque` | Rayon Géographie, fiche 4 « Se déplacer » |
| `types par grade` | 🐚 association · ⚓ ordre · 🧭 ordre · 🔭 ordre · 🔱 code |

<!-- ANCRAGE:FIN -->
