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

<!-- ANCRAGE:FIN -->
