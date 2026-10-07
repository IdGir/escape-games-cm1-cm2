# COHÉRENCE NARRATIVE — escale pilote (cahier des charges § 3 bis)

## 1. Règles appliquées, et règles ajoutées après la relecture sceptique

Règles du § 3 bis (lieu, problème, émetteur, lien au roman, raison du savoir, réaction du décor, anachronismes assumés,
pas de morale plaquée) : contrôlées par `tests/test-coherence-narrative.js`.

La relecture sceptique a jugé deux énigmes « à renforcer ». **On a corrigé les énigmes et ajouté trois règles** (elles
s'appliqueront aux dix autres escales) :

- **R9 — Le personnage ne demande pas ce qu'il sait.** Un émetteur ne pose pas aux élèves une question dont il connaît la
  réponse sans raison narrative ; s'il est expert, il est ailleurs (au porte-voix, blessé, occupé) et les élèves agissent à sa
  place. *Appliqué à e2-3 : Nemo est à la cage du pilote ; les mousses lisent ses instruments.*
- **R10 — Une réaction ne devance pas l'énigme suivante.** La réaction du décor montre l'effet de CETTE énigme, jamais la
  résolution de la suivante. *Appliqué : e2-3 ne fait plus « remonter » le Nautilus ; c'est e2-4 (l'hélice) qui le fait.*
- **R11 — L'enjeu dépend du savoir mobilisé.** Le danger évoqué doit être évité grâce au savoir de l'énigme. *Appliqué : e2-3
  ne parle plus de heurter un navire (aucun instrument ne l'éviterait) mais de jaillir trop vite ou en pleine tempête.*
- **R12 — La réaction découle du travail fait.** Si le décor montre un objet fabriqué (le câble cuivre-caoutchouc), les
  matériaux triés doivent le contenir à tous les grades. *Appliqué à e2-1 (Mousse, Matelot).*

## 2. Relecture sceptique (second passage, 3 octobre 2026) — verdicts

| Énigme | Pourquoi ici ? | Pourquoi maintenant ? | Pourquoi ce personnage ? | Si l'on échoue ? | Verdict initial | Après correction |
|---|---|---|---|---|---|---|
| e2-1 Le câble brûlé du carré | le câble a brûlé sur cette table | début : comprendre la panne | Conseil « classe tout » | pas de câble : ni lumière ni pompe | ✅ ancrée (réaction mal reliée aux cartes Mousse/Matelot) | ✅ cuivre et caoutchouc ajoutés au tri |
| e2-2 Le tableau de laiton | les bornes sont dans la salle des machines | obstacle : le courant ne va nulle part | Aronnax, curieux de tout (acceptable : il découvre les machines) | la jauge d'air continue de baisser | ✅ ancrée | ✅ « série » vérifiée au grade Matelot |
| e2-3 Le mur des instruments | mur d'instruments du ch. XII | rebondissement : il faut remonter | Nemo demandait ce qu'il sait (invraisemblable) | enjeu sans lien avec les instruments | ⚠️ à renforcer | ✅ Nemo au porte-voix, enjeu « remonter trop vite / tempête », réaction sans remontée |
| e2-4 L'épure du capitaine | épure montrée au salon (ch. XIII) | résolution : relancer l'hélice | Ned Land impatient | « sans hélice pas de remontée » : faux chez Verne | ⚠️ à renforcer | ✅ « sans hélice, ni direction ni surface sûre » |

Autres corrections issues de la relecture : origine de la **matière** (et non de l'énergie) au grade Second ; isolation
historique à la gutta-percha (A-VERIFIER) ; baromètre réaliste (760 → 752 mm en 6 h) ; thermomètre « à bord » ; « piles » au lieu
d'« accumulateurs » ; « vider les réservoirs » (et non « ouvrir les ballasts ») ; libellé « les câbles qui vont de la manette au
moteur » (ordre unique) ; sous-titres retirés au grade Second (ils donnaient l'ordre) ; questions trop faciles remplacées
(Second) ; leurres de justification crédibles (phrases vraies de la fiche, mais qui ne prouvent pas) ; « Une fois les fils
posés » (au lieu de « quand tu es prêt ») ; plume ajoutée à la liste des isolants ; « en série » ajouté à la partie de la fiche
visible au grade Matelot ; mesures à rattacher par leurs **unités** au grade Timonier (différenciation réelle).

## 3. Table roman ↔ programme (pour juger en 5 minutes)

| Énigme | Épisode du roman | Lieu | Matière | Compétence | Liberté prise |
|---|---|---|---|---|---|
| e2-1 | Partie I, ch. XII « Tout par l'électricité » | carré des officiers | sciences | conducteurs / isolants, danger | avarie inventée ; caoutchouc au lieu de gutta-percha |
| e2-2 | Partie I, ch. XII | salle des machines (version électrique) | sciences | circuit, série, dérivation, court-circuit | tableau à bornes et ampoules (1879) simplifiés |
| e2-3 | Partie I, ch. XII (instruments de la chambre de Nemo, manomètre) | chambre de Nemo | technologie | fonction d'usage, mesures, unités | porte-voix vers la cage du pilote (vraisemblance) ; pression : notion de collège pour Lieutenant/Second |
| e2-4 | Partie I, ch. XIII « Quelques chiffres » (épure au salon) | grand salon | technologie | chaîne d'énergie, formes d'énergie | « moteur électrique » pour les électro-aimants de Verne |

Personnages inventés : les mousses de l'*Abraham Lincoln* (les élèves). Fil rouge inventé : l'avarie et le journal de bord à
reconstituer. Fragment `MOBILIS` : devise du Nautilus dans le roman (*Mobilis in mobili*).

## 4. Relecture sceptique des escales 1, 3, 4, 5 et 6 (3 octobre 2026)

Mêmes questions qu'au § 2, mêmes règles R9 à R12. Corrections faites avant intégration.

| Énigme | Pourquoi ici ? | Pourquoi maintenant ? | Pourquoi ce personnage ? | Si l'on échoue ? | Verdict initial | Après correction |
|---|---|---|---|---|---|---|
| e1-1 Le livre de quart | relevés de vitesse sur le pont | début : la lueur file | Aronnax tient le journal | la chasse est perdue d'avance | ✅ ancrée | — |
| e1-2 Forcer les feux | chaufferie de la frégate | obstacle : pas assez rapide | Conseil, méthodique | chaudière poussée sans méthode | ✅ ancrée | — |
| e1-3 La cambuse | vivres d'une chasse qui dure | rebondissement : des mois de mer | Ned Land, marin de longs cours | faim, scorbut | ✅ ancrée | consigne Mousse reformulée |
| e1-4 Le harpon de Ned Land | le harpon frappe le « monstre » | résolution | Ned est le harponneur | tirer sur un navire habité | ✅ ancrée | — |
| e3-1 Les réservoirs d'air | sas des scaphandres (ch. XV-XVI) | avant de sortir | Conseil, d'habitude confiant | asphyxie | ⚠️ 3 énigmes, 2 émetteurs | ✅ Ned, méfiant (il refuse la promenade chez Verne) |
| e3-2 La plaine aux mille couleurs | « Promenade en plaine » (ch. XVI) | pendant la promenade | Conseil classificateur | collection refusée | ✅ ancrée | — |
| e3-3 La lampe dans la forêt | forêt de l'île Crespo, pénombre | rebondissement : il fait noir | Aronnax, la lampe Ruhmkorff | perdu dans l'obscurité | ✅ ancrée | — |
| e4-1 Les instruments engloutis | épave de Vanikoro (II, ch. XIX) | début | Aronnax, savant | mystère non résolu | ✅ ancrée | — |
| e4-2 La boîte de fer-blanc | archives de Nemo | après la plongée | Nemo confie un travail (R9 : tâche, pas question) | documents sans valeur de preuve | ⚠️ limite R9 | ✅ maintenu : Nemo délègue un classement, il n'interroge pas |
| e4-3 Les papiers d'un autre monde | carré, papiers triés | résolution | Conseil classe | confusion des deux régimes | ✅ ancrée | — |
| e5-1 La perle géante | banc de Manaar (II, ch. II-III) | début | Conseil et sa balance | perle refusée | ✅ ancrée | — |
| e5-2 Le pêcheur de perles | pêcheur sauvé du requin | obstacle | Ned, indigné | Ned refuse de repartir | ✅ ancrée (enjeu moral tiré du roman, pas plaqué) | — |
| e5-3 Les voiles de Ceylan | surface au large de Ceylan | résolution | Conseil (3ᵉ fois) | Nautilus repéré | ⚠️ 3 énigmes, 2 émetteurs | ✅ Aronnax à la longue-vue ; une seule énigme Matelot « tri » de suite → QCM |
| e6-1 Le passage secret | cage du pilote, tunnel (II, ch. V) | avant le tunnel | Aronnax n'y croit pas (ch. IV) | « tunnel trop étroit » : aucun calcul ne l'évite (R11) | ⚠️ à renforcer | ✅ enjeu : comprendre l'avance que donne le raccourci |
| e6-2 Le fleuve et le désert | carte du Nil, chantiers de l'isthme | pendant la traversée | Conseil classe les usages | enjeu de survie sans lien au tri (R11) | ⚠️ à renforcer | ✅ enjeu : l'eau mal partagée manque à quelqu'un |
| e6-3 Le plan d'évasion de Ned | surface devant Port-Saïd | résolution | Ned rêve de fuir (fil du roman) | évasion ratée | ✅ ancrée | — |

## 5. Relecture sceptique des escales 7 à 11 (3 octobre 2026)

| Énigme | Pourquoi ici ? | Pourquoi maintenant ? | Pourquoi ce personnage ? | Si l'on échoue ? | Verdict initial | Après correction |
|---|---|---|---|---|---|---|
| e7-1 La mer qui bout | salon, thermomètre extérieur (II, ch. VI) | début : l'eau chauffe | Conseil note tout | rester trop près du volcan | ✅ ancrée | — |
| e7-2 Ned veut débarquer | hublot sur la côte en feu | obstacle | Ned guette chaque côte | débarquer dans l'éruption | ✅ ancrée | — |
| e7-3 Le mot sur la roche | ruines de l'Atlantide (II, ch. IX) | résolution : le mot ATLANTIS | Aronnax, savant prudent | confondre récit et preuve | ✅ ancrée | — |
| e8-1 Qui mange qui ? | mer des Sargasses (II, ch. XI) | début | Conseil classe | Ned arrache toutes les algues | ✅ ancrée | — |
| e8-2 Le fleuve dans la mer | carte des courants, bouée qui dérive | obstacle : sortir des algues | Aronnax (ch. XIX) | ⚠️ même objet que e8-3 | ⚠️ | ✅ objet propre : la bouée qui dérive |
| e8-3 Les chaînes de l'épave | carte des courants | rebondissement | Nemo confie une tâche (R9 : tâche, pas question), fidèle à son rôle d'ami des opprimés | l'oubli | ⚠️ épave inventée, sujet grave | ✅ maintenu : ton sobre, chiffres d'historiens, aucune mise en scène de la violence |
| e8-4 Le fil sous la mer | le câble sur le fond | résolution | Ned rêve d'écrire au Canada | Ned abîme le câble | ⚠️ chapitre du roman incertain | ✅ « vraisemblance », à vérifier (A-VERIFIER.md) |
| e9-1 Le ciel de la banquise | station sur le pont, aurore | début : avant de plonger | Aronnax note les relevés (ch. XIII) | plonger dans la tempête | ✅ ancrée | — |
| e9-2 Le pavillon du pôle | pavillon au N d'or (ch. XIV) | au pôle | Conseil troublé par le geste | — (savoir civique) | ⚠️ lien par contraste seulement ; anachronisme (Empire en 1868) | ✅ assumé et signalé : dossier de l'équipe de secours |
| e9-3 Faute d'air | sous la banquise (ch. XV-XVI) | rebondissement final | Ned, pioche en main (il creuse dans le roman) | la glace se referme | ⚠️ la jauge baissait dès le pôle, en surface | ✅ l'air ne baisse qu'après e9-2 (paramètre « debut » du moteur) |
| e10-1 Le monstre à la vitre | vitre du salon (ch. XVIII) | début | Conseil classe (fidèle au roman) | frapper au mauvais endroit | ✅ ancrée | — |
| e10-2 La hache et le harpon | plate-forme, combat | obstacle | Ned frappe au cœur | être emporté | ✅ ancrée | « le second du capitaine » → « un marin » (fidélité) |
| e10-3 Les bocaux du musée | vitrines du salon | après le combat | Aronnax, naturaliste | rester dans des eaux à calmars | ⚠️ enjeu un peu construit | ✅ maintenu : le savoir (ponte en masse) fonde la décision de partir |
| e11-1 L'or des galions | baie de Vigo (II, ch. VIII) | début | Aronnax doute de Nemo | prendre Nemo pour un pilleur | ✅ ancrée (nuance historique sur le trésor signalée) | — |
| e11-2 Le dernier soir au salon | salon, orgue, toiles (I, ch. XI ; II, ch. XXII) | la nuit de l'évasion | Nemo confie une tâche (R9) | le passage reste fermé | ⚠️ dans le roman, Nemo ne parle pas aux fugitifs | ✅ liberté signalée dans la fiche |
| e11-3 Le programme de l'évasion | canot sur le dos du Nautilus | résolution | Ned a tout prévu | rester boulonné, aspiré | ✅ ancrée | — |
| e11-4 Le réveil aux Lofoten | côte de Norvège (ch. XXIII) | épilogue | Conseil organise le retour | se perdre au retour | ✅ ancrée (dossier XXIᵉ siècle) | — |
