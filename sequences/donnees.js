/* ============================================================
   FICHES DE SÉQUENCE « AVANT / APRÈS » AUTOUR D'UN JEU (amélioration N18)
   ------------------------------------------------------------
   Chaque jeu touche déjà une discipline précise. Une courte séquence — une
   activité de MISE EN SITUATION avant (15-20 min), le JEU, une activité de
   RÉINVESTISSEMENT après (15-20 min) — le rend plus facile à intégrer dans une
   progression que de le jouer isolément.
   Une fiche = une entrée ci-dessous, clé = dossier du jeu (comme dans
   commun/donnees/catalogue.js). Un jeu SANS entrée n'est pas bloqué : la page
   fiche.html affiche alors le modèle vierge (voir README.md pour en rédiger une).
   Format d'une entrée :
     objectif        une phrase : ce que l'élève saura faire à la fin de la séquence
     niveaux         "CM1 · CM2"
     avant / apres   { titre, duree, modalite, deroule:[étapes], materiel:[…], trace }
     jeu             { duree, formules:[…], roles:[…], conseils:[…] }
     evaluer         [ idées de trace et d'évaluation ]
     prolonger       [ pistes facultatives ]
   Les activités s'appuient sur le GUIDE-PEDAGOGIQUE.md du jeu (déroulés, matériel,
   grille d'observation) ; le lien avec la fiche de compétences par période (C5) et le
   passeport (C3) est ajouté par la page.
   Fichier .js (et non .json) pour fonctionner aussi en double-clic.
   ============================================================ */
var SEQUENCES = {

  "melanges": {
    objectif: "Comparer et mesurer des masses, reconnaître un mélange homogène ou hétérogène (la masse se conserve quand on dissout), et choisir la bonne méthode pour séparer les constituants d'un mélange.",
    niveaux: "CM1 · CM2",
    avant: {
      titre: "Le sucre a-t-il disparu ? — une manipulation d'accroche",
      duree: "15-20 min",
      modalite: "Équipes de 4, une balance par équipe (ou une démonstration au bureau).",
      deroule: [
        "Poser un verre d'eau et un morceau de sucre sur une balance de cuisine ; noter la masse affichée.",
        "Chaque équipe écrit sa prévision sur l'ardoise : « quand le sucre sera dissous, la balance affichera… plus / moins / pareil ».",
        "Dissoudre le sucre en remuant, sans rien retirer du verre ; relire la balance ; comparer avec la prévision.",
        "Montrer quatre bocaux (eau salée, eau et huile, eau et sable, sirop à l'eau) : « combien de choses voit-on ? » ; les élèves les classent en deux groupes.",
        "Garder deux questions écrites au tableau pour le jeu : « où est passé le sucre ? » et « comment récupérer le sel ? »."
      ],
      materiel: ["balance de cuisine électronique (au gramme)", "verres ou gobelets transparents", "sucre, eau", "quatre bocaux : eau salée, eau et huile, eau et sable, sirop à l'eau"],
      trace: "Dans le cahier de sciences : la prévision, ce qu'on a constaté, et une phrase « Je me demande… »."
    },
    jeu: {
      duree: "60 à 75 min en une séance, ou cinq séances de 25 min (une salle par séance, recommandé en CM1)",
      formules: ["Le Laboratoire de Madame Mélange : cinq salles, cinq opérations du protocole (peser, comparer, observer, aimanter, évaporer), puis le coffre final.", "Niveau CM1 (15 énigmes) ou CM2 (20 énigmes) ; palier Découverte pour les élèves en difficulté."],
      roles: ["lecteur (lit la consigne)", "calculateur (pose les calculs)", "gardien du temps", "porte-parole (demande l'indice à l'enseignant avant de cliquer)"],
      conseils: ["Faire relire la leçon (bouton 📚) avant d'ouvrir un indice.", "Pause générale depuis le tableau de bord pour une mise au point sur « fondre / dissoudre » après la salle 2.", "Imprimer une fiche de mission par équipe (⚙️ Réglages → Impression)."]
    },
    apres: {
      titre: "Récupérer le sel et reconstituer le protocole",
      duree: "15-20 min",
      modalite: "Équipes de 4, puis mise en commun collective.",
      deroule: [
        "Reprendre la question « comment récupérer le sel ? » : chaque équipe propose une méthode, puis on teste : filtrer de l'eau boueuse (filtre à café et entonnoir), et mettre une coupelle d'eau salée au soleil ou sur un radiateur (le résultat se verra quelques jours plus tard).",
        "Remplir un tableau « mélange → ce que l'on voit → méthode de séparation » avec les mélanges rencontrés dans le jeu et dans la manipulation d'accroche (eau salée, eau et huile, eau et sable, eau boueuse…).",
        "Reconstituer le protocole de Madame Mélange dans l'ordre à partir des cinq mots trouvés aux serrures, et expliquer à l'oral pourquoi chaque opération vient à sa place.",
        "Consulter le bilan de classe (resultats.html) : les énigmes les moins bien réussies du premier coup guident la leçon à reprendre collectivement."
      ],
      materiel: ["filtres à café, entonnoir, eau boueuse", "coupelle, eau salée", "tableau à compléter (à copier au cahier)"],
      trace: "Trace écrite : la différence entre « fondre » et « dissoudre », la définition d'un mélange homogène et d'un mélange hétérogène, et le tableau des méthodes de séparation."
    },
    evaluer: [
      "Grille d'observation du GUIDE-PEDAGOGIQUE.md pendant le jeu (lecture de la consigne, relecture de la leçon avant l'indice, justification d'un choix).",
      "Le passeport de compétences (C3) : noter pour chaque élève les cinq compétences du jeu (non acquis · en cours · acquis).",
      "Le bilan de classe (resultats.html) : réussite du premier coup par énigme et par compétence, avec la liste « à retravailler »."
    ],
    prolonger: ["Chercher à la maison un mélange homogène et un mélange hétérogène de la cuisine et les apporter (photo ou dessin).", "Comparer la masse d'un même volume d'eau pure et d'eau salée."]
  },

  "chateau-fort": {
    objectif: "Décrire les trois fonctions d'un château fort (protéger, loger le seigneur, symboliser sa puissance) et raconter la vie quotidienne des paysannes et des paysans, leurs relations avec le seigneur.",
    niveaux: "CM1 · CM2",
    avant: {
      titre: "À quoi sert un château, à part se défendre ?",
      duree: "15-20 min",
      modalite: "Collectif au TBI, puis binômes pour le vocabulaire.",
      deroule: [
        "Poser la question au tableau : « À quoi sert un château, à part se défendre ? » ; recueillir les idées sans les corriger.",
        "Projeter le plan d'un château (ou un schéma simple) : les élèves repèrent ce qu'ils connaissent (tour, pont-levis, remparts…) et ce qu'ils ne connaissent pas.",
        "En binômes, lire la fiche préparatoire 1 (vocabulaire : motte, palissade, donjon, enceinte…) et surligner trois mots nouveaux.",
        "Noter les idées de la classe sous trois colonnes laissées vides : on les nommera après le jeu."
      ],
      materiel: ["plan ou schéma de château projeté", "fiche préparatoire 1 du jeu (imprimable depuis ⚙️ Réglages)", "tableau divisé en trois colonnes"],
      trace: "Au cahier : les mots nouveaux et la question de départ, laissée sans réponse."
    },
    jeu: {
      duree: "60 à 75 min en une séance, ou deux séances de 35-40 min (salles 1 à 3 : le château ; salles 4 et 5 : le village), ou cinq séances de 25 min",
      formules: ["Le Secret du donjon : cinq salles (la motte et la palissade, les remparts, la grande salle, le village et les champs, le moulin du seigneur), cinq clés, puis le coffre final.", "Niveau CM1 (15 énigmes) ou CM2 (20 énigmes) ; palier Découverte possible."],
      roles: ["lecteur (lit à voix haute)", "manipulateur (clique)", "vérificateur (relit avant de valider)", "secrétaire (note le mot-clé)"],
      conseils: ["Entre les salles 3 et 4 : mise en commun courte « les trois fonctions du château ».", "Pour une salle seule : ouvrir le jeu avec ?salle=N&niveau=CM1 (mode vérification, rien n'est sauvegardé)."]
    },
    apres: {
      titre: "Le tableau des trois fonctions et le débat des redevances",
      duree: "15-20 min",
      modalite: "Collectif, puis travail individuel au cahier.",
      deroule: [
        "Compléter ensemble le tableau laissé vide avant le jeu : protéger (remparts, donjon, herse) · loger le seigneur et sa famille (grande salle, chambre) · montrer sa puissance (taille, pierre, décor) ; chaque élève justifie avec une scène du jeu.",
        "Passer au village : placer sur un calendrier simplifié les travaux des champs rencontrés dans le jeu (labours, semailles, moisson, vendange…).",
        "Débat court à partir de la salle 5 : « Les paysans donnaient des redevances au seigneur : qu'est-ce que le seigneur leur apportait en échange ? Est-ce équitable ? » — chacun écrit un avis argumenté en deux phrases.",
        "Consulter le bilan de classe (resultats.html) pour repérer la leçon à reprendre collectivement."
      ],
      materiel: ["tableau des trois fonctions (à copier)", "calendrier des travaux à compléter (frise ou cercle des mois)"],
      trace: "Trace écrite : « Un château fort sert à protéger, à loger le seigneur et à montrer sa puissance » + trois phrases sur la vie des paysannes et des paysans."
    },
    evaluer: [
      "Grille d'observation du GUIDE-PEDAGOGIQUE.md : vocabulaire employé, capacité à relier une scène du jeu à une fonction du château.",
      "Le passeport de compétences (C3) : les deux compétences du jeu (fonctions du château · vie quotidienne des paysans).",
      "Le bilan de classe (resultats.html) et, pour les familles, la fiche de période (C5)."
    ],
    prolonger: ["Légender un plan de château vierge (ouvrage, tours, pont-levis, donjon, basse-cour).", "Rédiger la journée d'un enfant au village, vue par lui-même."]
  }
};
