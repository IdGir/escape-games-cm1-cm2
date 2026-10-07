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

### e7-1 — La mer qui bout

| Champ | Contenu |
|---|---|
| `id` | e7-1 |
| `escale` | 7 |
| `decor` | volcan-santorin |
| `objets_cliquables` | thermometre, hublot-gauche, carte-archipel (objet principal : thermometre) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Près de Santorin, le thermomètre extérieur du salon monte sans arrêt ; derrière les hublots, l'eau bouillonne et se teinte de rouge. Conseil veut noter dans son carnet d'où vient cette chaleur, schéma à l'appui, avant que le capitaine ne décide de rester ou de s'éloigner. |
| `enjeu` | Tant qu'on ignore que la chaleur monte du volcan sous la mer, on croit pouvoir rester : or plus le Nautilus s'en approche, plus l'eau devient brûlante. |
| `episode_du_roman` | Partie II, ch. VI « L'Archipel en feu » : l'eau atteint une température telle que le capitaine fait virer de bord. |
| `competence_programme` | Sciences : la Terre active — décrire un volcan (cratère, cheminée, magma, lave, cendres) ; relier l'éruption à la chaleur interne de la Terre. |
| `pourquoi_ce_savoir_ici` | On ne comprend pourquoi la mer bout ici qu'en sachant ce qu'il y a sous l'île : un volcan en activité. |
| `reaction_du_decor` | L'aiguille du thermomètre redescend : le Nautilus s'écarte du volcan. |
| `liberte_ou_anachronisme` | L'éruption de Santorin (Néa Kaméni, 1866) est réelle ; les températures sont celles du roman (A-VERIFIER.md). Le schéma est simplifié pour le cycle 3. |
| `niveau_variantes` | Mousse : 3 cases du volcan. Matelot : 5 cases. Timonier : 5 cases et étiquettes pièges. Lieutenant : texte à trous sur l'éruption + justification. Second : QCM sur l'origine de la chaleur et des îles volcaniques + justification. |
| `fiche de la Bibliothèque` | Rayon Terre active, fiche 1 « Les volcans » |
| `types par grade` | 🐚 plan · ⚓ plan · 🧭 plan · 🔭 trous · 🔱 qcm |

### e7-2 — Ned veut débarquer

| Champ | Contenu |
|---|---|
| `id` | e7-2 |
| `escale` | 7 |
| `decor` | volcan-santorin |
| `objets_cliquables` | hublot-droit, carte-archipel, manometre (objet principal : hublot-droit) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | Par le hublot, Ned Land voit la côte toute proche. Une île, des maisons : l'occasion de s'enfuir ! Mais l'île tremble et fume. Avant qu'il ne se jette à l'eau, il faut lui montrer ce qui est dangereux ici, et ce que font les habitants d'un pays de volcans et de séismes pour se protéger. |
| `enjeu` | Débarquer sans connaître les dangers d'un volcan en éruption, c'est risquer les cendres, la lave et les secousses. |
| `episode_du_roman` | Fil du roman : Ned Land guette chaque côte pour s'évader (Partie II, ch. VI-VIII) ; l'éruption de Santorin de 1866 s'accompagna de secousses. |
| `competence_programme` | Sciences : la Terre active — identifier les risques liés aux volcans et aux séismes ; connaître des mesures de prévention et de protection. |
| `pourquoi_ce_savoir_ici` | Devant une île en éruption, savoir reconnaître un danger et le bon réflexe décide d'un départ ou d'un drame. |
| `reaction_du_decor` | Ned recule du hublot ; le Nautilus s'éloigne doucement de l'île. |
| `liberte_ou_anachronisme` | Les mesures de prévention (surveillance, alerte, évacuation) sont celles d'aujourd'hui : c'est le dossier de l'équipe de secours (XXIᵉ siècle). |
| `niveau_variantes` | Mousse : bonne ou mauvaise idée. Matelot : volcan ou séisme. Timonier : avant, pendant, après. Lieutenant : prévention ou protection + justification. Second : ordre de l'alerte + justification. |
| `fiche de la Bibliothèque` | Rayon Terre active, fiche 2 « Volcans et séismes : les risques » |
| `types par grade` | 🐚 tri · ⚓ tri · 🧭 tri · 🔭 tri · 🔱 ordre |

### e7-3 — Le mot sur la roche

| Champ | Contenu |
|---|---|
| `id` | e7-3 |
| `escale` | 7 |
| `decor` | atlantide |
| `objets_cliquables` | temple, volcan-atlantide, statues (objet principal : temple) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Au fond de l'Atlantique, Nemo conduit Aronnax au milieu de ruines englouties par un volcan. Sur un rocher, il écrit un seul mot : ATLANTIS. Aronnax, savant, est bouleversé mais prudent : l'Atlantide est-elle une ville réelle ou un récit ? Il veut trier ce qu'on sait vraiment de ce qu'on raconte. |
| `enjeu` | Un savant qui confond un récit et une preuve écrit des erreurs dans son livre : Aronnax doit pouvoir distinguer ce que racontent les textes de ce que prouvent les fouilles. |
| `episode_du_roman` | Partie II, ch. IX « Un continent disparu » : Nemo écrit ATLANTIS à la craie sur un rocher, devant Aronnax stupéfait. |
| `competence_programme` | Histoire : distinguer un mythe (récit) d'un fait prouvé par des traces (fouilles, documents) ; se repérer dans le temps (frise). |
| `pourquoi_ce_savoir_ici` | Devant les ruines que montre Nemo, la question de l'historien se pose : comment sait-on qu'une chose a existé ? |
| `reaction_du_decor` | Les lettres ATLANTIS brillent un instant sur le rocher, sous la lueur du volcan. |
| `liberte_ou_anachronisme` | Les ruines de l'Atlantide sont une invention de Verne. L'Atlantide est un récit de Platon (vers 360 av. J.-C.). L'éruption de Santorin (vers 1600 av. J.-C.) et la ville d'Akrotiri, fouillée depuis 1967, sont réelles ; le lien avec le mythe est une hypothèse (A-VERIFIER.md). |
| `niveau_variantes` | Mousse : vrai ou faux simple. Matelot : vrai ou faux sur récit, trace, fouille. Timonier : frise chronologique. Lieutenant : QCM fait, hypothèse, récit + justification. Second : tri fait prouvé, hypothèse, récit inventé + justification. |
| `fiche de la Bibliothèque` | Rayon Histoire, fiche 6 « Mythe ou histoire ? » |
| `types par grade` | 🐚 vraifaux · ⚓ vraifaux · 🧭 ordre · 🔭 qcm · 🔱 tri |

### e8-1 — Qui mange qui ?

| Champ | Contenu |
|---|---|
| `id` | e8-1 |
| `escale` | 8 |
| `decor` | sargasses |
| `objets_cliquables` | algues, crabes, bouee (objet principal : algues) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Le Nautilus a fait surface au milieu d'une mer couverte d'algues dorées. Dessous, tout un monde vit caché : petits crabes, crevettes, poissons. Conseil veut ranger ces êtres vivants dans son carnet, non pas par familles cette fois, mais selon qui mange qui. |
| `enjeu` | Ned veut arracher toutes les algues pour libérer l'hélice ; s'il comprend que tout ce petit monde en dépend, il dégagera seulement l'hélice. |
| `episode_du_roman` | Partie II, ch. XI « La mer de Sargasses » : Aronnax décrit cette mer d'algues flottantes, peuplée de petits animaux. |
| `competence_programme` | Sciences : le vivant dans son environnement — chaînes alimentaires, producteurs et consommateurs, interdépendance dans un écosystème. |
| `pourquoi_ce_savoir_ici` | La mer des Sargasses est un écosystème à elle seule : sans algues, pas d'abri ni de nourriture pour ses habitants. |
| `reaction_du_decor` | Entre les algues, des crabes et des poissons apparaissent un instant, puis replongent. |
| `liberte_ou_anachronisme` | Les chaînes alimentaires sont simplifiées. Les anguilles d'Europe pondent bien en mer des Sargasses (savoir du XXᵉ siècle, présenté comme dossier de l'équipe de secours). |
| `niveau_variantes` | Mousse : animal ↔ nourriture. Matelot : chaîne alimentaire (4 maillons). Timonier : chaîne de 5 maillons avec rôles. Lieutenant : texte à trous producteur/consommateur + justification. Second : QCM sur l'interdépendance + justification. |
| `fiche de la Bibliothèque` | Rayon Vivant, fiche 4 « Qui mange qui ? Les chaînes alimentaires » |
| `types par grade` | 🐚 association · ⚓ ordre · 🧭 ordre · 🔭 trous · 🔱 qcm |

### e8-2 — Le fleuve dans la mer

| Champ | Contenu |
|---|---|
| `id` | e8-2 |
| `escale` | 8 |
| `decor` | sargasses |
| `objets_cliquables` | bouee, carte-courants, algues (objet principal : bouee) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | La bouée-phare prise dans les algues dérive lentement : un courant l'emporte. Sur la carte des courants dépliée sur le pont, Aronnax suit une large flèche rouge : le Gulf Stream, « fleuve » d'eau chaude qui traverse l'Atlantique. Il veut comprendre pourquoi les algues s'accumulent ici, au milieu de ce grand tourbillon, et pourquoi Brest a des hivers plus doux que Terre-Neuve, à la même latitude. |
| `enjeu` | Pour sortir de la mer d'algues sans gaspiller d'énergie, il faut savoir où passe le courant et dans quel sens il porte le Nautilus. |
| `episode_du_roman` | Partie II, ch. XI et ch. XIX « Le Gulf Stream » : Aronnax décrit ce « fleuve » chaud au milieu de l'océan et ses effets sur le climat. |
| `competence_programme` | Géographie et sciences : les grands courants marins, leur influence sur le climat ; lire une carte et des relevés de températures. |
| `pourquoi_ce_savoir_ici` | La mer des Sargasses est au centre du grand tourbillon de courants dont le Gulf Stream fait partie : c'est lui qui retient les algues et adoucit l'Europe. |
| `reaction_du_decor` | La flèche rouge du Gulf Stream s'illumine sur la carte, du golfe du Mexique jusqu'à l'Europe. |
| `liberte_ou_anachronisme` | Les températures moyennes de janvier sont des ordres de grandeur actuels (A-VERIFIER.md). Les chapitres XI et XIX sont rapprochés dans cette escale. |
| `niveau_variantes` | Mousse : QCM courant chaud. Matelot : tri villes douces / froides. Timonier : écart de températures (code). Lieutenant : QCM sur l'effet du courant + justification. Second : vrai ou faux sur courants et climat + justification. |
| `fiche de la Bibliothèque` | Rayon Terre active, fiche 3 « Courants marins et climat » |
| `types par grade` | 🐚 qcm · ⚓ tri · 🧭 code · 🔭 qcm · 🔱 vraifaux |

### e8-3 — Les chaînes de l'épave

| Champ | Contenu |
|---|---|
| `id` | e8-3 |
| `escale` | 8 |
| `decor` | sargasses |
| `objets_cliquables` | carte-courants, bouee, algues (objet principal : carte-courants) |
| `personnage_emetteur` | Le capitaine Nemo |
| `probleme_narratif` | Dans les algues, les plongeurs du Nautilus ont trouvé l'épave d'un ancien navire négrier : des fers, des chaînes. Nemo les fait déposer sur la carte des courants et confie aux mousses une tâche : retracer la route de ce navire et dater son histoire, pour la vitrine du musée. Il ne veut pas qu'on oublie. |
| `enjeu` | Sans l'histoire de cette route, ces chaînes ne seraient que de la ferraille : on oublierait des millions de personnes. |
| `episode_du_roman` | Fil du roman : Nemo se veut l'ennemi des oppresseurs et l'ami des opprimés (Partie II, ch. VIII et XXI). L'épave est inventée. |
| `competence_programme` | Histoire : la traite atlantique et l'esclavage (le commerce triangulaire) ; les abolitions ; se repérer sur une carte et sur une frise. |
| `pourquoi_ce_savoir_ici` | La route des navires négriers suivait les vents et les courants de l'Atlantique : on la lit sur cette carte. |
| `reaction_du_decor` | Le triangle Europe, Afrique, Amériques se dessine sur la carte, puis s'efface lentement. |
| `liberte_ou_anachronisme` | L'épave est inventée. En 1868, l'esclavage existe encore au Brésil et à Cuba ; la loi française de 2001 (loi Taubira) est un dossier de l'équipe de secours. Les chiffres sont des estimations d'historiens (A-VERIFIER.md). |
| `niveau_variantes` | Mousse : les 3 trajets du triangle dans l'ordre. Matelot : schéma du triangle. Timonier : schéma avec étiquettes pièges. Lieutenant : frise des abolitions + justification. Second : QCM sur le commerce triangulaire + justification. |
| `fiche de la Bibliothèque` | Rayon Histoire, fiche 7 « La traite et l'esclavage » |
| `types par grade` | 🐚 ordre · ⚓ plan · 🧭 plan · 🔭 ordre · 🔱 qcm |

### e8-4 — Le fil sous la mer

| Champ | Contenu |
|---|---|
| `id` | e8-4 |
| `escale` | 8 |
| `decor` | cable |
| `objets_cliquables` | cable, plongeurs, hublot-cable (objet principal : cable) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | Près de Terre-Neuve, sur le fond, un long serpent couvert de coquillages : le câble télégraphique qui relie l'Europe à l'Amérique. Ned Land n'en revient pas : un message passerait par là jusqu'au Canada ? Avant de rêver d'y accrocher le sien, il veut comprendre comment l'on communique d'un bout à l'autre du monde, hier et aujourd'hui. |
| `enjeu` | Si Ned comprend qu'on ne lit pas un message en touchant le câble, il renonce à l'abîmer, et l'Europe ne perd pas sa ligne avec l'Amérique. |
| `episode_du_roman` | Vraisemblance : Partie II, ch. XIX, le Nautilus remonte l'Atlantique vers Terre-Neuve, où repose le câble transatlantique posé en 1866 par le Great Eastern (chapitre exact à vérifier). |
| `competence_programme` | Géographie : communiquer d'un bout à l'autre du monde grâce à l'internet ; un monde de réseaux ; des habitants inégalement connectés. |
| `pourquoi_ce_savoir_ici` | Le câble de 1866 est l'ancêtre direct des câbles sous-marins qui transportent aujourd'hui presque tout l'internet entre les continents. |
| `reaction_du_decor` | Une lueur court le long du câble, comme un message qui passe. |
| `liberte_ou_anachronisme` | Le câble de 1866 est réel ; la place du passage dans le roman est à vérifier (A-VERIFIER.md). Internet est un dossier de l'équipe de secours (XXIᵉ siècle). |
| `niveau_variantes` | Mousse : hier ou aujourd'hui. Matelot : inventions dans l'ordre. Timonier : QCM sur les câbles et internet. Lieutenant : durées d'un message (code) + justification. Second : bien ou mal connectés + justification. |
| `fiche de la Bibliothèque` | Rayon Communication, fiche 1 « Communiquer d'un bout à l'autre du monde » |
| `types par grade` | 🐚 tri · ⚓ ordre · 🧭 qcm · 🔭 code · 🔱 tri |

### e9-1 — Le ciel de la banquise

| Champ | Contenu |
|---|---|
| `id` | e9-1 |
| `escale` | 9 |
| `decor` | banquise |
| `objets_cliquables` | instruments-meteo, aurore, icebergs (objet principal : instruments-meteo) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Le Nautilus a fait surface au bord de la banquise, sous une aurore australe. Avant de plonger sous la glace, Nemo veut connaître le temps qui vient : une tempête refermerait les passages. Aronnax, sur le pont, relève les instruments de la petite station météorologique. |
| `enjeu` | Si l'on ne sait pas lire les instruments, on plonge sans savoir qu'une tempête approche et que la glace va se refermer derrière nous. |
| `episode_du_roman` | Partie II, ch. XIII « La banquise » : Aronnax note les températures, le vent, les glaces ; Nemo choisit le moment de plonger. |
| `competence_programme` | Sciences : la météorologie — mesurer le temps qu'il fait avec des instruments (thermomètre, baromètre, anémomètre, girouette, pluviomètre) ; interpréter des relevés. |
| `pourquoi_ce_savoir_ici` | Au bord de la banquise, le temps décide de tout : une baisse du baromètre annonce la tempête qui refermera les passages. |
| `reaction_du_decor` | Les aiguilles des instruments s'agitent, puis se fixent : la mesure est prise. |
| `liberte_ou_anachronisme` | Le pluviomètre et l'anémomètre existent en 1868 ; la petite station sur le pont est inventée. Unités de pression en millimètres de mercure, comme à l'époque. |
| `niveau_variantes` | Mousse : instrument ↔ ce qu'il mesure. Matelot : instrument ↔ mesure et unité. Timonier : écarts de température et de pression (code). Lieutenant : QCM de prévision + justification. Second : rapport à trous + justification. |
| `fiche de la Bibliothèque` | Rayon Terre active, fiche 4 « Le temps qu'il fait » |
| `types par grade` | 🐚 association · ⚓ association · 🧭 code · 🔭 qcm · 🔱 trous |

### e9-2 — Le pavillon du pôle

| Champ | Contenu |
|---|---|
| `id` | e9-2 |
| `escale` | 9 |
| `decor` | pole |
| `objets_cliquables` | pavillon, sextant, manchots (objet principal : pavillon) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Au pôle Sud, Nemo déploie un pavillon noir marqué d'un N d'or : il prend possession de cette terre en son seul nom. Conseil, troublé, se demande ce que signifie un drapeau, et ce que représentent ceux d'un pays. L'équipe de secours du XXIᵉ siècle lui envoie un dossier sur les symboles de la République française. |
| `enjeu` | Sans comprendre ce qu'est un symbole, on ne voit pas la différence entre le drapeau d'un homme seul et celui d'un peuple tout entier. |
| `episode_du_roman` | Partie II, ch. XIV « Le pôle Sud » : le 21 mars 1868, Nemo déploie son pavillon noir au N d'or et prend possession du pôle. |
| `competence_programme` | EMC : connaître les symboles de la République française (drapeau, hymne, devise, Marianne, fête nationale) et ce qu'ils signifient. |
| `pourquoi_ce_savoir_ici` | Le geste de Nemo, qui plante son propre drapeau, oblige à se demander ce qu'un drapeau représente. |
| `reaction_du_decor` | Le pavillon claque au vent ; le N d'or brille un instant sous le soleil rasant. |
| `liberte_ou_anachronisme` | En 1868, la France est un Empire (Napoléon III), pas une République ; son drapeau est déjà tricolore. Les symboles de la République sont présentés comme dossier de l'équipe de secours (XXIᵉ siècle). Le premier homme réellement arrivé au pôle Sud est Roald Amundsen, en 1911. |
| `niveau_variantes` | Mousse : l'intrus parmi les symboles. Matelot : symbole ou non. Timonier : symbole ↔ description. Lieutenant : vrai ou faux + justification. Second : QCM sur le sens des symboles + justification. |
| `fiche de la Bibliothèque` | Rayon Vivre ensemble, fiche 1 « Les symboles de la République » |
| `types par grade` | 🐚 intrus · ⚓ tri · 🧭 association · 🔭 vraifaux · 🔱 qcm |

### e9-3 — Faute d'air

| Champ | Contenu |
|---|---|
| `id` | e9-3 |
| `escale` | 9 |
| `decor` | banquise |
| `objets_cliquables` | icebergs, glaces, instruments-meteo (objet principal : icebergs) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | Sur le chemin du retour, un iceberg se retourne : le Nautilus est enfermé sous la glace. L'air s'épuise. L'équipage creuse à la pioche, et le capitaine fait injecter de l'eau bouillante pour que l'eau autour de la coque ne gèle pas. Ned Land, pioche en main, veut comprendre ce qui se passe avec cette eau qui gèle, fond et bout. |
| `enjeu` | Si l'eau autour du Nautilus gèle, la prison se referme : il faut savoir comment empêcher l'eau de passer à l'état solide. |
| `episode_du_roman` | Partie II, ch. XV-XVI « Faute d'air » : le Nautilus emprisonné ; l'équipage creuse, des jets d'eau bouillante retardent la congélation, et le navire brise enfin la glace de tout son poids. |
| `competence_programme` | Sciences : les états de l'eau (solide, liquide, gaz) et les changements d'état ; températures de fusion et d'ébullition ; l'eau de mer gèle vers −2 °C. |
| `pourquoi_ce_savoir_ici` | Sous la glace, la survie dépend d'un changement d'état : garder l'eau liquide autour de la coque. |
| `reaction_du_decor` | Une secousse : le Nautilus, alourdi, brise la glace sous lui et retrouve l'eau libre ; la jauge d'air remonte. |
| `liberte_ou_anachronisme` | Le récit suit le roman ; la température de congélation de l'eau de mer (environ −2 °C) est une valeur moyenne (A-VERIFIER.md). |
| `niveau_variantes` | Mousse : tri solide, liquide, gaz. Matelot : schéma des changements d'état. Timonier : QCM sur les températures. Lieutenant : calcul de températures + justification. Second : ordre des actions du roman + justification. |
| `fiche de la Bibliothèque` | Rayon Matière et lumière, fiche 4 « Les états de l'eau » |
| `types par grade` | 🐚 tri · ⚓ plan · 🧭 qcm · 🔭 code · 🔱 ordre |

### e10-1 — Le monstre à la vitre

| Champ | Contenu |
|---|---|
| `id` | e10-1 |
| `escale` | 10 |
| `decor` | salon |
| `objets_cliquables` | hublots, vitrines, epure (objet principal : hublots) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Derrière la grande vitre du salon, un œil énorme, des bras couverts de ventouses. Conseil, fidèle à lui-même, veut d'abord le classer : poisson, crustacé, mollusque ? Le classer, c'est savoir comment il se défend, et où il est vulnérable. |
| `enjeu` | Mal classé, le monstre est mal compris : on frapperait une carapace qu'il n'a pas, au lieu de viser son corps mou. |
| `episode_du_roman` | Partie II, ch. XVIII « Les poulpes » : Conseil et Aronnax observent un calmar géant par la vitre du salon et discutent de sa classification. |
| `competence_programme` | Sciences : classer les êtres vivants selon les caractères qu'ils partagent (mollusques, céphalopodes, crustacés, poissons). |
| `pourquoi_ce_savoir_ici` | Devant un animal inconnu, la classification dit ce qu'il a (corps mou, bras à ventouses) et ce qu'il n'a pas (squelette, carapace). |
| `reaction_du_decor` | Derrière la vitre, le grand œil s'éloigne ; une ventouse se décolle lentement. |
| `liberte_ou_anachronisme` | Verne appelle « poulpes » des calmars géants, à huit bras chez lui. On distingue ici poulpe (8 bras) et calmar (8 bras et 2 tentacules). |
| `niveau_variantes` | Mousse : l'intrus parmi les céphalopodes. Matelot : tri mollusque, crustacé, poisson. Timonier : vrai ou faux sur les céphalopodes. Lieutenant : tri par caractères + justification. Second : QCM sur la classification + justification. |
| `fiche de la Bibliothèque` | Rayon Vivant, fiche 5 « Les céphalopodes » |
| `types par grade` | 🐚 intrus · ⚓ tri · 🧭 vraifaux · 🔭 tri · 🔱 qcm |

### e10-2 — La hache et le harpon

| Champ | Contenu |
|---|---|
| `id` | e10-2 |
| `escale` | 10 |
| `decor` | plateforme-poulpe |
| `objets_cliquables` | oeil, tentacules, equipage (objet principal : oeil) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | L'hélice est bloquée : le Nautilus remonte, et l'équipage monte sur la plate-forme, hache à la main, sous l'orage. Les bras du monstre frappent de partout. Ned Land, harpon levé, guette. Il faut réagir vite et juste : voir, décider, frapper. Comment notre corps fait-il cela, et comment le monstre fait-il de même ? |
| `enjeu` | Celui qui ne voit pas venir le bras, ou qui réagit trop tard, est emporté : la vitesse du message entre l'œil, le cerveau et les muscles décide du combat. |
| `episode_du_roman` | Partie II, ch. XVIII : combat sur la plate-forme ; Nemo frappe à la hache, Ned Land plonge son harpon au cœur du calmar ; un marin est emporté. |
| `competence_programme` | Sciences : le fonctionnement du corps humain — les organes des sens, les nerfs, le cerveau et les muscles ; le cerveau commande les mouvements. |
| `pourquoi_ce_savoir_ici` | Au cœur du combat, chaque geste suit le même chemin : un sens perçoit, le cerveau décide, les muscles agissent. |
| `reaction_du_decor` | Un choc : un bras tranché retombe ; le monstre recule dans un nuage d'encre. |
| `liberte_ou_anachronisme` | Le combat suit le roman. La proportion de neurones dans les bras du poulpe est une valeur approchée (A-VERIFIER.md). |
| `niveau_variantes` | Mousse : 3 étapes (voir, décider, agir). Matelot : 5 étapes. Timonier : schéma sens → nerfs → cerveau → nerfs → muscles. Lieutenant : QCM + justification. Second : texte à trous sur le poulpe + justification. |
| `fiche de la Bibliothèque` | Rayon Vivant, fiche 6 « Le cerveau commande les mouvements » |
| `types par grade` | 🐚 ordre · ⚓ ordre · 🧭 plan · 🔭 qcm · 🔱 trous |

### e10-3 — Les bocaux du musée

| Champ | Contenu |
|---|---|
| `id` | e10-3 |
| `escale` | 10 |
| `decor` | salon |
| `objets_cliquables` | vitrines, hublots, orgue (objet principal : vitrines) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Le combat est fini ; un homme a disparu. Nemo veut savoir s'il faut fuir ces parages. Dans les vitrines du salon, Aronnax a des bocaux : des grappes d'œufs de calmar, des œufs de tortue, un jeune dauphin conservé. Si les calmars se reproduisent ici, d'autres viendront. Encore faut-il savoir comment ils naissent et grandissent. |
| `enjeu` | Si l'on comprend que ces calmars pondent ici des milliers d'œufs, on sait qu'il faut quitter ces parages sans attendre. |
| `episode_du_roman` | Partie II, ch. XVIII-XIX : après le combat, Nemo pleure son compagnon ; le Nautilus quitte les Lucayes et remonte vers le nord. |
| `competence_programme` | Sciences : reproduction et développement des animaux — ovipares et vivipares, stades de développement (œuf, larve, jeune, adulte), nombre de petits et soins. |
| `pourquoi_ce_savoir_ici` | Savoir comment se reproduit un animal, c'est savoir s'il va revenir, et combien. |
| `reaction_du_decor` | Le Nautilus s'éloigne ; dans le salon, le grand orgue se tait et les bocaux scintillent doucement. |
| `liberte_ou_anachronisme` | Les bocaux du musée sont inventés. Les nombres d'œufs sont des ordres de grandeur (A-VERIFIER.md). |
| `niveau_variantes` | Mousse : ovipare ou vivipare. Matelot : tri avec animaux marins variés. Timonier : stades du développement dans l'ordre. Lieutenant : calcul de survie des œufs + justification. Second : vrai ou faux sur les stratégies + justification. |
| `fiche de la Bibliothèque` | Rayon Vivant, fiche 7 « Naître et grandir » |
| `types par grade` | 🐚 tri · ⚓ tri · 🧭 ordre · 🔭 code · 🔱 vraifaux |

### e11-1 — L'or des galions

| Champ | Contenu |
|---|---|
| `id` | e11-1 |
| `escale` | 11 |
| `decor` | baie-vigo |
| `objets_cliquables` | galions, tresor, plongeurs (objet principal : galions) |
| `personnage_emetteur` | Le professeur Aronnax |
| `probleme_narratif` | Au fond de la baie de Vigo, en Espagne, les plongeurs du Nautilus ramassent des lingots et des pièces d'or dans les épaves de galions. Aronnax veut comprendre comment ce trésor est arrivé là : une guerre voulue par Louis XIV, un roi qui décidait de tout. Pour juger l'usage que Nemo fait de cet or, il faut d'abord connaître son histoire. |
| `enjeu` | Sans l'histoire de ces galions, Aronnax prend Nemo pour un pilleur d'épaves ; avec elle, il comprend d'où vient cet or et à qui il appartenait. |
| `episode_du_roman` | Partie II, ch. VIII « La baie de Vigo » : Nemo raconte la bataille de 1702 et montre ses plongeurs ramassant l'or des galions. |
| `competence_programme` | Histoire : Louis XIV, un monarque absolu ; la guerre de Succession d'Espagne ; se repérer sur une frise. |
| `pourquoi_ce_savoir_ici` | Ces galions ont coulé à cause d'une guerre décidée par Louis XIV pour placer son petit-fils sur le trône d'Espagne. |
| `reaction_du_decor` | Sous le fanal, l'or des coffres éventrés étincelle un instant. |
| `liberte_ou_anachronisme` | La bataille de Vigo (23 octobre 1702) est réelle ; le trésor a en grande partie été débarqué avant le combat, et la richesse des épaves reste discutée (A-VERIFIER.md). La phrase « L'État, c'est moi » est une légende. |
| `niveau_variantes` | Mousse : QCM sur Louis XIV. Matelot : frise du règne. Timonier : fait ↔ explication. Lieutenant : tri des signes de la monarchie absolue + justification. Second : texte à trous sur Vigo + justification. |
| `fiche de la Bibliothèque` | Rayon Histoire, fiche 8 « Louis XIV, roi absolu » |
| `types par grade` | 🐚 qcm · ⚓ ordre · 🧭 association · 🔭 tri · 🔱 trous |

### e11-2 — Le dernier soir au salon

| Champ | Contenu |
|---|---|
| `id` | e11-2 |
| `escale` | 11 |
| `decor` | salle-orgue |
| `objets_cliquables` | toiles, orgue, vitrines-orgue (objet principal : toiles) |
| `personnage_emetteur` | Le capitaine Nemo |
| `probleme_narratif` | C'est la nuit de l'évasion. Pour gagner le canot, il faut traverser le salon, où Nemo joue de l'orgue, seul. Il ne se retourne pas ; il parle à mi-voix de ses toiles de maîtres, Léonard de Vinci, Raphaël, Titien, « ce que les hommes ont fait de plus beau ». Il confie aux mousses un dernier travail : ranger ces œuvres dans l'ordre de leur siècle, pour que leur mémoire au moins survive. |
| `enjeu` | Ce dernier service rendu, Nemo reste à son orgue et ne retient personne : le chemin du canot est libre. |
| `episode_du_roman` | Partie I, ch. XI (les toiles de maîtres du salon : Raphaël, Léonard de Vinci, Titien…) et Partie II, ch. XXII : la dernière nuit, Aronnax traverse le salon où Nemo joue de l'orgue. |
| `competence_programme` | Histoire : la Renaissance — un temps de découvertes, d'artistes et d'inventions ; François Iᵉʳ et Léonard de Vinci. |
| `pourquoi_ce_savoir_ici` | Le salon de Nemo est un musée de la Renaissance : ses toiles racontent ce temps d'artistes et d'inventeurs. |
| `reaction_du_decor` | Le lustre s'éclaire doucement ; l'orgue joue un dernier accord. |
| `liberte_ou_anachronisme` | La tâche confiée par Nemo est inventée. Les dates sont celles des manuels ; Léonard a dessiné un appareil pour respirer sous l'eau, il n'a pas construit de sous-marin. |
| `niveau_variantes` | Mousse : artiste ↔ œuvre. Matelot : QCM sur la Renaissance. Timonier : frise. Lieutenant : vrai ou faux + justification. Second : tri Moyen Âge ou Renaissance + justification. |
| `fiche de la Bibliothèque` | Rayon Histoire, fiche 9 « La Renaissance » |
| `types par grade` | 🐚 association · ⚓ qcm · 🧭 ordre · 🔭 vraifaux · 🔱 tri |

### e11-3 — Le programme de l'évasion

| Champ | Contenu |
|---|---|
| `id` | e11-3 |
| `escale` | 11 |
| `decor` | maelstrom |
| `objets_cliquables` | canot, tourbillon, fanal (objet principal : canot) |
| `personnage_emetteur` | Ned Land |
| `probleme_narratif` | Le canot est fixé sur le dos du Nautilus par des boulons. Dehors, la mer gronde : le Nautilus approche du Maelström. Ned Land a tout prévu, mais dans le noir, sans un mot, chacun doit exécuter les ordres dans l'ordre exact. Il faut écrire le plan comme un programme : des instructions précises, des répétitions, des conditions. |
| `enjeu` | Une instruction oubliée ou mal placée, et le canot reste boulonné au Nautilus, entraîné avec lui dans le tourbillon. |
| `episode_du_roman` | Partie II, ch. XXII : Ned, Aronnax et Conseil se glissent dans le canot ; ils dévissent les écrous quand le Nautilus est happé par le Maelström. |
| `competence_programme` | Technologie et mathématiques : programmer — écrire une suite d'instructions (algorithme), utiliser une boucle « répéter » et une condition « si… alors ». |
| `pourquoi_ce_savoir_ici` | Dans le noir et le vacarme, un plan exécuté pas à pas, sans ambiguïté, est le seul qui marche : c'est exactement ce qu'est un programme. |
| `reaction_du_decor` | Un craquement : le canot se détache et part en tournoyant sur les vagues. |
| `liberte_ou_anachronisme` | Écrire le plan comme un programme est un choix pédagogique ; le vocabulaire (boucle, condition) est celui d'aujourd'hui. |
| `niveau_variantes` | Mousse : 3 instructions dans l'ordre. Matelot : 5 instructions. Timonier : QCM sur la boucle et la condition. Lieutenant : exécuter un programme (code) + justification. Second : compléter le programme avec des blocs + justification. |
| `fiche de la Bibliothèque` | Rayon Communication, fiche 2 « Programmer » |
| `types par grade` | 🐚 ordre · ⚓ ordre · 🧭 qcm · 🔭 code · 🔱 plan |

### e11-4 — Le réveil aux Lofoten

| Champ | Contenu |
|---|---|
| `id` | e11-4 |
| `escale` | 11 |
| `decor` | maelstrom |
| `objets_cliquables` | cote, canot, tourbillon (objet principal : cote) |
| `personnage_emetteur` | Conseil |
| `probleme_narratif` | Rejetés par le Maelström, les trois compagnons se réveillent dans une cabane de pêcheurs des îles Lofoten, en Norvège. Conseil veut savoir comment rentrer en France, et l'équipe de secours du XXIᵉ siècle lui répond par un dossier sur l'Europe d'aujourd'hui : quels pays font partie de l'Union européenne, et la Norvège en est-elle ? |
| `enjeu` | Pour organiser le retour, il faut savoir quels pays on traverse et ce qui change d'un pays à l'autre (frontières, monnaie). |
| `episode_du_roman` | Partie II, ch. XXIII « Conclusion » : réveil dans une cabane de pêcheurs des îles Lofoten ; ils attendent un bateau pour regagner la France. |
| `competence_programme` | Géographie : la France dans l'Union européenne — pays membres, symboles, monnaie, libre circulation ; repérer la Norvège, pays européen non membre. |
| `pourquoi_ce_savoir_ici` | Les Lofoten sont en Norvège : un pays d'Europe qui n'a pas choisi d'entrer dans l'Union européenne. |
| `reaction_du_decor` | Sur la mer apaisée, la route du retour se dessine, de la Norvège vers la France. |
| `liberte_ou_anachronisme` | L'Union européenne n'existe pas en 1868 : c'est le dossier de l'équipe de secours (XXIᵉ siècle). Le nombre de pays utilisant l'euro évolue ; on dit « une vingtaine » (A-VERIFIER.md). |
| `niveau_variantes` | Mousse : tri pays membres ou non. Matelot : tri avec pays plus difficiles. Timonier : symboles de l'UE. Lieutenant : QCM sur l'UE + justification. Second : vrai ou faux sur la Norvège, Schengen et l'euro + justification. |
| `fiche de la Bibliothèque` | Rayon Géographie, fiche 5 « L'Union européenne » |
| `types par grade` | 🐚 tri · ⚓ tri · 🧭 association · 🔭 qcm · 🔱 vraifaux |

<!-- ANCRAGE:FIN -->
