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
