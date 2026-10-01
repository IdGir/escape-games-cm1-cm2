# Catalogue des améliorations — Escape games CM1/CM2

Ce fichier recense **toutes** les pistes d'amélioration étudiées pour le dépôt
`escape-games-cm1-cm2`, qu'elles aient été retenues, écartées ou pas encore
traitées. **Règle : ne jamais reproposer une idée déjà listée ici**, même si
son statut est « Rejeté » ou « Reporté » — on la retrouve, on discute de la
changer de statut, on n'en récrit pas une variante qui s'ignore elle-même.

Statuts possibles : `Proposé` · `Sélectionné` (prêt à lancer) · `En cours` ·
`Fait` · `Rejeté` · `Reporté`.

Dernière étude approfondie : **27 septembre 2026**, à partir de l'état réel du
dépôt (code, README, guides pédagogiques, `A-VERIFIER.md`, scripts de
production média, tests). Les 9 jeux publiés au moment de l'étude :
`declaration`, `tour-du-monde`, `mission-geo`, `constitution`, `moyen-age-abbaye`,
`chateau-fort`, `station-meteo`, `melanges`, `objets-techniques`.

---

## Axe A — Structure et qualité technique

### A1 — Généraliser les tests automatisés à tous les jeux
Seuls `chateau-fort`, `moyen-age-abbaye` et `objets-techniques` ont un dossier
`tests/` (Node + jsdom). Les 6 autres (`constitution`, `declaration`,
`tour-du-monde`, `station-meteo`, `melanges`, `mission-geo`) n'en ont aucun :
une régression du moteur partagé peut donc passer inaperçue sur la majorité
des jeux. Reprendre le modèle de test existant et l'étendre.
**Jeux concernés :** constitution, declaration, tour-du-monde, station-meteo, melanges, mission-geo · **Effort :** M · **Statut :** Fait

### A2 — Différenciation CM1/CM2 pour mission-geo
`mission-geo` est le seul jeu sans bascule de niveau CM1/CM2 (les 8 autres
l'ont, avec un contenu réellement différent, pas seulement une quantité
différente). C'est l'incohérence de structure la plus visible du dépôt.
**Jeux concernés :** mission-geo · **Effort :** L · **Statut :** Proposé

### A3 — Tronc commun unique pour le moteur partagé
`app.js`, `enigmes.js`, `decors.js`, `audio.js`, `narration.js`,
`personnages.js`, `media.js`, `impression.js`, `reglages.js`, `sync.js`,
`api.js` existent en **8 copies quasi identiques**, une par jeu (tailles très
proches d'un dossier à l'autre). Un correctif ou une amélioration du moteur
doit aujourd'hui être recopié à la main dans huit dossiers. Faire converger
vers un socle commun versionné, avec uniquement les données (`enigmes.json`,
`decors.js` propre au décor) qui restent par jeu.
**Jeux concernés :** tous sauf mission-geo · **Effort :** L · **Statut :** Fait

### A4 — Mode hors-ligne installable (PWA)
Aucun `manifest.json` ni `service worker` dans le dépôt : l'usage sans
internet suppose de lancer `serveur.py` sur un poste. Une PWA installable sur
tablette fonctionnerait hors connexion sans aucun serveur à démarrer.
**Jeux concernés :** tous · **Effort :** L · **Statut :** Proposé

### A5 — Export/reprise de partie pour tous les jeux « salles »
Seul `mission-geo` a un export/import de progression en JSON. Les 8 jeux
« salles » n'ont qu'une reprise implicite sur le même poste/navigateur — ce
que confirme déjà le guide de `constitution` pour son déroulé en 5 séances de
25 minutes, mais sans portabilité d'un poste à l'autre.
**Jeux concernés :** constitution, declaration, tour-du-monde, station-meteo, melanges, objets-techniques, moyen-age-abbaye, chateau-fort · **Effort :** M · **Statut :** Proposé

### A6 — Étendre verifier.html à un onglet « cohérence du moteur »
En plus des 4 onglets déjà présents (énigmes, médias, fichiers mal nommés,
documents), ajouter un onglet qui compare les fichiers `js/` communs entre
les 8 jeux « salles » pour repérer un correctif appliqué à un seul jeu et
oublié ailleurs — un vrai risque avec la duplication actuelle (voir A3).
**Jeux concernés :** tous · **Effort :** M · **Statut :** Fait

### A7 — Contrôle automatique des fichiers enigmes.json avant publication
Un script qui vérifie, avant un `git push`, la cohérence de chaque
`enigmes.json` (clés attendues par type d'énigme, nombre CM1 ≤ CM2, pas de
mot de passe de serrure dupliqué) — pour rattraper une erreur de saisie avant
qu'une classe ne tombe dessus.
**Jeux concernés :** tous · **Effort :** S · **Statut :** Proposé

---

## Axe B — Design et présentations vidéo

### B1 — Charte graphique écrite, commune aux 9 jeux
Chaque jeu a ses propres couleurs (déjà choisies sur l'accueil) et son propre
style de décor SVG, dessiné indépendamment dans `decors.js`. Écrire une
charte courte (palette, épaisseurs de trait, style des personnages) pour que
l'identité visuelle reste cohérente malgré la production jeu par jeu.
**Jeux concernés :** tous · **Effort :** M · **Statut :** Proposé

### B2 — Bande-annonce courte par jeu (15-20 s)
`outils-medias/produire-medias.ps1` sait déjà générer des vidéos animées via
l'API Agnes à partir de photos/images (clé déjà configurée et testée d'après
`diag.txt`). Prolonger ce pipeline pour produire une bande-annonce par jeu,
utilisable en amont en classe ou pour présenter le projet aux collègues/parents.
**Jeux concernés :** tous · **Effort :** M · **Statut :** Proposé

### B3 — Frise visuelle des 26 jeux sur l'accueil
`prompts-opus/00-ORDRE-DE-PRODUCTION.md` contient déjà tout le calendrier
(26 jeux, périodes P1-P5, années A/B) mais c'est un fichier de travail interne,
non public. En tirer une frise visuelle sur `index.html` : jeux disponibles en
couleur, jeux à venir en grisé, positionnés sur le calendrier scolaire.
**Jeux concernés :** page d'accueil · **Effort :** M · **Statut :** Proposé

### B4 — Affiche/miniature 16:9 par jeu
Remplacer ou compléter les vignettes actuelles (dégradé de couleur + icône
emoji) par une vraie affiche par jeu, réutilisable aussi pour les partages
hors du site (ENT, messages aux familles).
**Jeux concernés :** tous · **Effort :** S · **Statut :** Proposé

### B5 — Sous-titres systématiques sur les vidéos de décor
Le moteur charge déjà automatiquement un fichier `.vtt` du même nom qu'une
vidéo, si présent (fonctionnalité existante, sous-utilisée). Généraliser la
production de sous-titres à toutes les vidéos de décor déposées.
**Jeux concernés :** tous · **Effort :** S · **Statut :** Proposé

### B6 — Transitions animées entre salles
Actuellement une coupure nette d'une salle à l'autre. Ajouter une transition
courte, désactivable par le réglage « animations réduites » déjà présent.
**Jeux concernés :** tous · **Effort :** M · **Statut :** Fait

---

## Axe C — Lien avec les programmes et la progression

### C1 — Vue d'ensemble publique de l'année
Créer, à partir de `00-ORDRE-DE-PRODUCTION.md` (aujourd'hui un fichier de
travail), une page publique qui croise périodes (P1-P5), années (A/B) et
jeux disponibles avec les points du programme couverts. Rend la progression
visible sans avoir à ouvrir un fichier de production interne.
**Jeux concernés :** page d'accueil / nouvelle page · **Effort :** M · **Statut :** Proposé

### C2 — Bandeau de référence BO sur chaque jeu, une fois confirmée
Plusieurs `A-VERIFIER.md` (chateau-fort, station-meteo, objets-techniques…)
signalent que la référence exacte du Bulletin officiel n'a pas pu être
confirmée en ligne pendant la production. Une fois vérifiée, l'afficher
clairement dans le jeu et le guide (aujourd'hui elle reste en note interne).
**Jeux concernés :** tous · **Effort :** S · **Statut :** Proposé

### C3 — Passeport de compétences cumulé sur l'année
Chaque `GUIDE-PEDAGOGIQUE.md` contient déjà une grille d'observation par jeu,
mais rien ne cumule ces grilles d'un jeu à l'autre. Un passeport élève qui
additionne les compétences validées jeu après jeu rendrait la progression
individuelle visible sur l'année, pas seulement jeu par jeu.
**Jeux concernés :** tous · **Effort :** L · **Statut :** Proposé

### C4 — Liens « jeu précédent / suivant » affichés dans le jeu
Le lien entre `declaration` et `constitution` (« suite directe ») n'existe
aujourd'hui qu'en texte dans les README. L'afficher directement à l'écran de
fin de partie, et le généraliser aux futurs jeux qui se suivent dans la
progression.
**Jeux concernés :** declaration, constitution (puis futurs jeux liés) · **Effort :** S · **Statut :** Proposé

### C5 — Fiche one-page imprimable par période
Une fiche de synthèse par période (P1 à P5) destinée à la communication
(direction, parents, inspection) : jeux joués, compétences travaillées,
sans avoir à assembler l'information à la main depuis les guides séparés.
**Jeux concernés :** tous · **Effort :** M · **Statut :** Proposé

---

## Axe D — Nouvelles fonctionnalités

### D1 — Écran de classement en direct, séparé du pilotage
Le tableau de bord enseignant (`prof.html`) suit déjà chaque équipe en
temps réel, mais c'est un outil de pilotage, pas un écran de projection.
Ajouter un écran « classement » dédié, projetable au TBI pendant la partie.
**Jeux concernés :** tous les jeux « salles » · **Effort :** M · **Statut :** Proposé

### D2 — Mode individuel (devoirs à la maison)
Le jeu est pensé pour des équipes de 3-4 ; un mode solo, avec compte-rendu
envoyé à l'enseignant, permettrait un usage en dehors de la classe.
**Jeux concernés :** tous · **Effort :** L · **Statut :** Proposé

### D3 — Banque de questions randomisée
Piocher aléatoirement parmi plusieurs variantes d'une même énigme pour
permettre de rejouer un jeu d'une année sur l'autre sans que les réponses
soient déjà connues des élèves (frères et sœurs, redoublants).
**Jeux concernés :** tous · **Effort :** L · **Statut :** Proposé

### D4 — Éditeur graphique (no-code) des énigmes
Chaque README promet déjà « aucune énigme écrite en dur » et un contenu
entièrement en JSON — mais modifier `enigmes.json` suppose encore d'éditer du
JSON à la main. Une petite interface locale qui édite ce JSON visuellement
tiendrait complètement cette promesse.
**Jeux concernés :** tous · **Effort :** L · **Statut :** Proposé

### D5 — Export des résultats vers un tableur ou vers Schooly
Centraliser les scores de la classe sur l'année (aujourd'hui uniquement des
impressions A4 isolées par partie), avec un export réutilisable dans le
suivi élève déjà en place ([[schooly]]).
**Jeux concernés :** tous · **Effort :** M · **Statut :** Proposé

### D6 — QR-code de démarrage de séance
Un QR-code affiché en début de séance pour rejoindre directement la bonne
salle et le bon niveau sur les tablettes, sans taper l'URL.
**Jeux concernés :** tous · **Effort :** S · **Statut :** Proposé

### D7 — Mode correction collective projetable
Après la partie, un mode qui rejoue les bonnes réponses salle par salle,
pour l'institutionnalisation en grand groupe (sans rouvrir chaque énigme une
par une).
**Jeux concernés :** tous · **Effort :** M · **Statut :** Proposé

---

## Axe E — Niveaux de difficulté et adaptabilité

### E1 — (voir A2) Différenciation CM1/CM2 pour mission-geo
Classée aussi ici : c'est le manque le plus direct en matière de niveaux de
difficulté. Voir A2 pour le détail — ne pas créer de doublon, mettre à jour
le statut de A2 seulement.
**Jeux concernés :** mission-geo · **Effort :** L · **Statut :** Proposé (= A2)

### E2 — Troisième palier de difficulté
Au-delà de CM1/CM2 : un palier « découverte », avec assistance renforcée,
pour les classes à triple niveau ou les élèves très en difficulté — en
réutilisant le mécanisme de bascule de niveau déjà en place.
**Jeux concernés :** tous · **Effort :** L · **Statut :** Fait

### E3 — Indices adaptatifs selon le rythme de l'équipe
Aujourd'hui : 3 indices par énigme, sur demande, coûtant 2 points, quel que
soit le temps déjà passé. Proposer automatiquement un indice après un délai
d'inactivité ou un nombre d'essais, pour s'adapter au rythme réel de chaque
équipe plutôt qu'à un barème fixe.
**Jeux concernés :** tous les jeux « salles » · **Effort :** M · **Statut :** Fait

### E4 — Police et réglages dyslexie-amis
En complément des réglages d'accessibilité déjà présents (texte jusqu'à
150 %, animations réduites) : une police adaptée en option (type
OpenDyslexic) et un interlignage augmenté.
**Jeux concernés :** tous · **Effort :** S · **Statut :** Fait

### E5 — Lecture à voix haute des consignes d'énigmes
La synthèse vocale existe déjà pour les dialogues des personnages ; l'étendre
aux consignes des énigmes elles-mêmes profiterait aux lecteurs fragiles,
au-delà de l'immersion narrative.
**Jeux concernés :** tous les jeux « salles » · **Effort :** M · **Statut :** Proposé

### E6 — Minuteur adaptatif par équipe, depuis le tableau de bord
Aujourd'hui, le seuil de bonus par salle est fixe (8 à 10 min). Permettre à
l'enseignant d'accorder, depuis `prof.html`, un délai supplémentaire à une
équipe précise sans lui faire perdre son bonus de rapidité.
**Jeux concernés :** tous les jeux « salles » · **Effort :** M · **Statut :** Fait

---

## Axe F — Diffusion, maintenance, exploitation

### F1 — FAQ / dépannage commune, visible depuis l'accueil
Le dépannage existe déjà (voir le tableau « En cas de problème » de
`mission-geo`) mais reste dispersé par jeu. Une FAQ commune, accessible
depuis `index.html`, éviterait de chercher dans chaque README.
**Jeux concernés :** page d'accueil · **Effort :** S · **Statut :** Proposé

### F2 — Journal des versions (CHANGELOG.md) par jeu
Les `RECAP-<jeu>.md` actuels servent à reprendre une conversation interrompue
(non commités, but différent). Un vrai changelog, commité et durable,
tracerait les évolutions d'un jeu au fil des mises à jour.
**Jeux concernés :** tous · **Effort :** S · **Statut :** Proposé

### F3 — Contrôle automatique des liens externes cités
Les `A-VERIFIER.md` citent de nombreux sites de référence (Eduscol, BnF,
Météo-France…) : un script qui vérifie périodiquement que ces liens
répondent encore éviterait de découvrir un lien mort face à la classe.
**Jeux concernés :** tous · **Effort :** S · **Statut :** Proposé

### F4 — Mode démonstration en boucle
Un mode qui enchaîne automatiquement de courts extraits de chaque jeu, sans
manipulation — utile en salle des professeurs, portes ouvertes, ou réunion
avec les familles.
**Jeux concernés :** page d'accueil · **Effort :** M · **Statut :** Proposé
