# sequences/ — fiches « avant / après » autour de chaque jeu (N18)

Une **séquence** rend un jeu plus facile à intégrer dans une progression que de le jouer isolément :

| Temps | Durée | Contenu |
|---|---|---|
| 🔎 **Avant** | 15-20 min | mise en situation : une manipulation, une question, une observation |
| 🎮 **Le jeu** | 45-75 min | formule retenue (une séance ou plusieurs), rôles, réglages conseillés |
| 🧩 **Après** | 15-20 min | réinvestissement et trace écrite, appuyés sur le bilan de classe (N12) |

Chaque fiche donne aussi : l'**objectif** (une phrase), comment **évaluer**, des pistes **pour aller plus loin**
et le **lien avec la fiche de compétences par période** (C5, `periode.html`) et le **passeport** (C3).

## Les pages

- `index.html` — la liste des jeux et l'état de leur fiche (✅ disponible · ⏳ à rédiger) ;
- `fiche.html?jeu=<dossier>` — la fiche d'un jeu, **imprimable** (A4) ; pour un jeu sans fiche : le **modèle vierge**
  (objectif, avant, le jeu, après), à remplir à la main — **un jeu sans fiche n'est jamais bloqué** ;
- `donnees.js` — les fiches rédigées (objet `SEQUENCES`, une entrée par dossier de jeu).

Liens : chaque `prof.html` (bouton « 📘 Fiche de séquence »), la vue d'ensemble de l'année (`annee.html`, lien
« 📘 Séquence » sur chaque jeu) et le kit « adopter ce projet » (`adopter.html`).

## Fiches rédigées

`melanges` (sciences, la matière : masses, mélanges, séparation) et `chateau-fort` (histoire, le Moyen Âge).
Ce sont deux jeux stables, dont le guide pédagogique propose déjà des activités d'accroche et de trace écrite :
elles servent de **test du format**. Les autres suivent, jeu après jeu.

## Rédiger la fiche d'un nouveau jeu

1. Ouvrir le `GUIDE-PEDAGOGIQUE.md` du jeu : les déroulés « 5 min avant / 15 min de jeu / 5 min après », le matériel
   et la grille d'observation y sont déjà ; les regrouper en **une** activité avant et **une** activité après de 15-20 min.
2. Dans `donnees.js`, ajouter une entrée dont la clé est le **dossier** du jeu (comme dans `commun/donnees/catalogue.js`) :

   ```js
   "mon-jeu": {
     objectif: "Une phrase : ce que l'élève saura faire à la fin de la séquence.",
     niveaux: "CM1 · CM2",
     avant: { titre, duree: "15-20 min", modalite, deroule: ["…"], materiel: ["…"], trace: "…" },
     jeu:   { duree, formules: ["…"], roles: ["…"], conseils: ["…"] },
     apres: { titre, duree: "15-20 min", modalite, deroule: ["…"], materiel: ["…"], trace: "…" },
     evaluer: ["…"], prolonger: ["…"]
   }
   ```
3. Vérifier `sequences/fiche.html?jeu=mon-jeu` et son impression ; ne mentionner que ce que le jeu et son guide
   contiennent réellement (pas de matériel ou de règle inventés).
4. `node commun/tests/test-pages.js N18` contrôle que chaque fiche est complète et que les liens existent.
