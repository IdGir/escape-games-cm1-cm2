/* =========================================================
   PÉRIODE 3 — SE NOURRIR
   Séances 9 et 10 (livret papier : pages 13 et 15)
   ========================================================= */

/* ---------------------------------------------------------
   SÉANCE 9 — Les pratiques alimentaires  (livret p. 13)
   --------------------------------------------------------- */
MISSION.session({
  id: "s09", numero: 9, periode: 3, livret: 13,
  titre: "Les pratiques alimentaires",
  lieu: "Bamako, Mali",
  theme: "Se nourrir",
  element: "Différences de pratiques alimentaires entre pays riches et pays pauvres",
  duree: 55,
  lecon: "l09",

  intro: {
    texte: `<p>Tu continues ton chemin, et te voilà maintenant au <b>Mali</b>.
      Pour te remettre de ton long voyage, tu décides d'aller faire un tour au marché.</p>
      <p>Tu te rends compte qu'il y a là des aliments que tu ne connais pas… et que
      beaucoup de ceux que tu connais coûtent ici une fortune.</p>`,
    media: { base: "s09-intro", legende: "Un marché de Bamako" }
  },

  activites: [
    {
      type: "tri",
      consigne: "Range chaque aliment dans le frigo où on le trouve le plus couramment.",
      precision: "Au Mali, on consomme surtout ce qui est produit sur place ; les produits importés sont rares et chers.",
      points: 5,
      media: { base: "s09-frigos", legende: "Un frigo français, un frigo malien" },
      paniers: [
        { id: "fr", titre: "🇫🇷 Frigo en France" },
        { id: "ml", titre: "🇲🇱 Frigo au Mali" }
      ],
      items: [
        { id: "a1", texte: "Pain de mie",   panier: "fr" },
        { id: "a2", texte: "Pâtes",         panier: "fr" },
        { id: "a3", texte: "Fromage",       panier: "fr" },
        { id: "a4", texte: "Yaourt",        panier: "fr" },
        { id: "a5", texte: "Pomme",         panier: "fr" },
        { id: "a6", texte: "Carotte",       panier: "fr" },
        { id: "a7", texte: "Millet",        panier: "ml" },
        { id: "a8", texte: "Riz",           panier: "ml" },
        { id: "a9", texte: "Arachides",     panier: "ml" },
        { id: "a10",texte: "Haricots rouges", panier: "ml" },
        { id: "a11",texte: "Gombo",         panier: "ml" },
        { id: "a12",texte: "Mangue",        panier: "ml" },
        { id: "a13",texte: "Poulet entier", panier: "ml" }
      ],
      aide: "Le frigo malien contient sept aliments : ceux qui poussent ou s'élèvent sur place."
    },
    {
      type: "ouverte",
      consigne: "Tu es étonné(e) de voir qu'il y a peu de poisson, peu de bœuf et peu de variété de fruits et légumes. À ton avis, pourquoi ?",
      points: 3,
      minimum: 20,
      pistes: [
        "Le Mali est un pays enclavé, sans accès à la mer : le poisson de mer y est rare et cher.",
        "Le climat est chaud et sec : peu de cultures variées, saison des pluies courte.",
        "Les revenus sont faibles : la viande et les produits importés coûtent trop cher.",
        "Peu de familles possèdent un réfrigérateur : difficile de conserver viande et poisson."
      ]
    },
    {
      type: "saisie",
      consigne: "Deux familles font leurs courses. Compare ce qu'elles peuvent acheter.",
      points: 4,
      document: `<div class="enveloppe-tableau"><table class="donnees">
        <tr><th>Produit local</th><th>Prix</th><th>Produit importé</th><th>Prix</th></tr>
        <tr><td>Millet (1 kg)</td><td>0,76 €</td><td>Pain (1 pièce)</td><td>0,46 €</td></tr>
        <tr><td>Riz (1 kg)</td><td>0,91 €</td><td>Pâtes importées (1 kg)</td><td>3,81 €</td></tr>
        <tr><td>Arachides (1 kg)</td><td>1,52 €</td><td>Fromage importé (100 g)</td><td>2,29 €</td></tr>
        <tr><td>Haricots (1 kg)</td><td>1,37 €</td><td>Yaourt importé (1 pot)</td><td>1,22 €</td></tr>
        <tr><td>Gombo (1 kg)</td><td>1,22 €</td><td>Pomme importée (1 pièce)</td><td>1,52 €</td></tr>
        <tr><td>Mangue (1 kg)</td><td>1,06 €</td><td>Carotte (1 kg)</td><td>1,06 €</td></tr>
        </table>
        <p><b>Famille A</b> (France) dispose de <b>25 €</b>. <b>Famille C</b> (Mali) dispose de <b>8 €</b>.</p></div>`,
      champs: [
        { label: "La famille C achète 1 kg de pâtes importées, 100 g de fromage et 1 yaourt. Combien dépense-t-elle ?",
          solution: "7.32", tolerance: 0.02, unite: "€" },
        { label: "Combien lui reste-t-il alors sur ses 8 € ?",
          solution: "0.68", tolerance: 0.02, unite: "€" },
        { label: "Avec ces mêmes 8 €, combien de kilos de millet aurait-elle pu acheter ? (nombre entier)",
          solution: "10", tolerance: 0 },
        { label: "Combien de fois la famille A est-elle plus riche que la famille C ? (arrondis)",
          solution: "3", tolerance: 0.2 }
      ],
      aide: "3,81 + 2,29 + 1,22 pour la première question. Pour le millet : 8 ÷ 0,76."
    },
    {
      type: "tableau",
      consigne: "Complète le tableau à partir de la carte de la sous-alimentation.",
      points: 4,
      media: { base: "carte-sous-alimentation", decor: "planisphere",
               legende: "La sous-alimentation dans le monde (2022-2024) — source FAO 2025" },
      document: `<p>Part de la population qui ne mange pas assez : moins de 2,5 % (très clair) •
        2,5 à 5 % • 5 à 10 % • 10 à 25 % • plus de 25 % (très foncé).</p>`,
      entete: "Pays",
      colonnes: [
        { titre: "Continent", options: ["Europe","Amérique du Nord","Amérique du Sud","Afrique","Asie","Océanie"] },
        { titre: "Sous-alimentation", options: ["faible","forte"] }
      ],
      lignes: [
        { titre: "France",      solutions: ["Europe", "faible"] },
        { titre: "États-Unis",  solutions: ["Amérique du Nord", "faible"] },
        { titre: "Haïti",       solutions: ["Amérique du Nord", "forte"] },
        { titre: "Tchad",       solutions: ["Afrique", "forte"] }
      ],
      aide: "Haïti est une île des Caraïbes : elle appartient à l'Amérique du Nord."
    }
  ],

  mediaCoeur: { base: "s09-coeur", legende: "Étals du marché" },

  fin: {
    texte: `<p>Sur le marché, une marchande reconnaît le drapeau de ta photographie
      froissée. « Ah, celui-là ! Il y a aussi du rouge dessus. »</p>`,
    media: { base: "s09-fin" }
  },

  indice: {
    type: "fait",
    texte: "Le drapeau du pays recherché comporte aussi du rouge.",
    libelle: "Précision d'une marchande de Bamako"
  }
});

/* ---------------------------------------------------------
   SÉANCE 10 — Les produits consommés  (livret p. 15)
   --------------------------------------------------------- */
MISSION.session({
  id: "s10", numero: 10, periode: 3, livret: 15,
  titre: "Les produits consommés",
  lieu: "La cantine de l'école",
  theme: "Se nourrir",
  element: "Différence entre produits agricoles et produits dérivés",
  duree: 45,
  lecon: "l10",

  intro: {
    texte: `<p>Pour ne pas attirer l'attention sur toi, tu retournes à l'école quelques jours,
      histoire de réfléchir à tous les indices déjà récupérés.</p>
      <p>Tu y redécouvres les joies de la cantine. Observe bien ton plateau : d'où vient
      chacun de ces aliments ?</p>`,
    media: { base: "s10-intro", legende: "Un plateau de cantine" }
  },

  activites: [
    {
      type: "tri",
      consigne: "Observe ton plateau et range chaque aliment dans le bon panier.",
      points: 4,
      media: { base: "s10-plateau", legende: "Le plateau du jour" },
      paniers: [
        { id: "agri", titre: "🌿 Produits agricoles (viennent directement de la nature)" },
        { id: "trans",titre: "🏭 Produits transformés (fabriqués à partir de produits agricoles)" }
      ],
      items: [
        { id: "c1", texte: "Pomme",         panier: "agri" },
        { id: "c2", texte: "Haricots verts",panier: "agri" },
        { id: "c3", texte: "Carottes",      panier: "agri" },
        { id: "c4", texte: "Poulet",        panier: "agri" },
        { id: "c5", texte: "Salade",        panier: "agri" },
        { id: "c6", texte: "Yaourt",        panier: "trans" },
        { id: "c7", texte: "Pain",          panier: "trans" },
        { id: "c8", texte: "Cookie",        panier: "trans" }
      ],
      aide: "Un produit transformé a été fabriqué par quelqu'un à partir d'autre chose : le pain vient du blé."
    },
    {
      type: "relier",
      consigne: "Relie chaque produit agricole au produit transformé fabriqué à partir de lui.",
      points: 4,
      gauche: [
        { id: "g1", texte: "Raisin" },
        { id: "g2", texte: "Lait" },
        { id: "g3", texte: "Tomate" },
        { id: "g4", texte: "Canne à sucre" },
        { id: "g5", texte: "Blé" },
        { id: "g6", texte: "Cacao" }
      ],
      droite: [
        { id: "t1", texte: "Jus de raisin" },
        { id: "t2", texte: "Fromage" },
        { id: "t3", texte: "Sauce tomate" },
        { id: "t4", texte: "Sucre" },
        { id: "t5", texte: "Pain" },
        { id: "t6", texte: "Chocolat" }
      ],
      paires: [["g1","t1"],["g2","t2"],["g3","t3"],["g4","t4"],["g5","t5"],["g6","t6"]],
      aide: "Le chocolat est fabriqué à partir des fèves d'un arbre tropical."
    },
    {
      type: "tableau",
      consigne: "À la ferme de Bray : quel aliment de ton plateau vient de chaque espace de production, et quel métier le produit ?",
      points: 4,
      media: { base: "s10-ferme", legende: "Les espaces de production de la ferme de Bray" },
      entete: "Espace de production",
      colonnes: [
        { titre: "Aliment du plateau", options: ["Poulet","Pain (blé)","Carottes","Pomme"] },
        { titre: "Métier", options: ["éleveur","céréalier","maraîcher","arboriculteur"] }
      ],
      lignes: [
        { titre: "Un élevage",                       solutions: ["Poulet", "éleveur"] },
        { titre: "Un champ de blé",                  solutions: ["Pain (blé)", "céréalier"] },
        { titre: "Un champ ou exploitation maraîchère", solutions: ["Carottes", "maraîcher"] },
        { titre: "Un verger",                        solutions: ["Pomme", "arboriculteur"] }
      ],
      aide: "Le maraîcher cultive les légumes ; l'arboriculteur s'occupe des arbres fruitiers."
    },
    {
      type: "saisie",
      consigne: "Compte les produits agricoles de ton plateau.",
      points: 2,
      champs: [{ label: "Nombre de produits agricoles sur le plateau", solution: "5" }],
      aide: "Reprends le premier exercice et compte le panier vert."
    },
    {
      type: "qcm",
      consigne: "Quelle affirmation est exacte ?",
      disposition: "liste",
      points: 2,
      options: [
        { texte: "Un produit transformé vient directement de la nature.", correct: false },
        { texte: "Un produit transformé est fabriqué à partir d'un ou de plusieurs produits agricoles.", correct: true },
        { texte: "Un produit agricole est toujours fabriqué dans une usine.", correct: false },
        { texte: "Le fromage est un produit agricole.", correct: false }
      ],
      aide: "Relis la définition du panier bleu."
    }
  ],

  mediaCoeur: { base: "s10-coeur", legende: "La ferme de Bray" },

  fin: {
    texte: `<p>Cinq produits agricoles sur le plateau. Un nombre de plus dans ton carnet…
      et une question qui te trotte dans la tête : par où passe donc un yaourt avant
      d'arriver dans ton assiette ?</p>`,
    media: { base: "s10-fin" }
  },

  indice: {
    type: "nombre", symbole: "goutte", valeur: 5,
    libelle: "Nombre de produits agricoles sur le plateau"
  }
});
