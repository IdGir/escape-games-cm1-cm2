/* =========================================================
   DIFFÉRENCIATION CM1 / CM2 (amélioration A2)
   ---------------------------------------------------------
   Les 16 séances restent celles du livret (mêmes documents, même
   indice à recopier pour la piste finale). Le niveau choisi sur
   l'écran d'accueil change la manière de les travailler :

   • CM1 — version GUIDÉE : méthode donnée dans la consigne, moins
     de distracteurs, calculs découpés en étapes, tableaux réduits à
     l'essentiel (ex. le secteur d'activité seulement), réponses
     ouvertes plus courtes.
   • CM2 — version du livret, complète, PLUS une activité « Pour aller
     plus loin » par séance : raisonner à partir des documents de la
     séance (comparer, calculer, justifier). Aucune donnée nouvelle
     n'est inventée : les nombres viennent des documents du livret,
     ou de situations présentées comme imaginaires (« Village A »).
   • Découverte (palier E2) — la version CM1, avec en plus le coup de
     pouce de chaque énigme affiché d'emblée, sans perte de points.

   Format, par séance :
     cm1 : { <n° d'activité> : { champs remplacés } }
     cm2 : { <n° d'activité> : { champs remplacés } }        (rare)
     plusCM2 : [ activité ]   ajoutée en fin de séance, en CM2 seulement
   Vérifier : index.html?seance=7&niveau=CM1  (CM1, CM2 ou DEC)
   ========================================================= */
(function(){
  const DIFF = {
    s01: {
      cm1: {
        2: { precision: "Exemple : à la mairie, on fait des papiers officiels → fonction administrative. Deux lieux ont la même fonction : santé." },
        3: { precision: "Les lettres marquées sont D, I, J, N, O. La ville commence par D et compte 5 lettres." }
      },
      plusCM2: [{
        type: "qcm", multiple: true, points: 3,
        titre: "Pour aller plus loin",
        consigne: "Parmi les lieux de ta mission, lesquels sont des services publics de la commune (ouverts à tous, gérés par la mairie) ?",
        precision: "Plusieurs réponses attendues. Un commerce vend quelque chose ; un service public rend un service à tous les habitants.",
        options: [
          { texte: "La mairie", correct: true },
          { texte: "L'école publique", correct: true },
          { texte: "La bibliothèque municipale", correct: true },
          { texte: "La boulangerie", correct: false },
          { texte: "La pharmacie", correct: false }
        ],
        aide: "Trois services publics : ce sont les lieux où l'on ne paie pas ce que l'on vient chercher."
      }]
    },
    s02: {
      cm1: {
        3: { precision: "Une seule bonne réponse par ligne. Indice : notre monnaie est aussi celle de l'Allemagne et de l'Espagne.",
             colonnes: [{ titre: "Réponse", options: ["Europe", "Asie", "551 695 km²", "350 000 km²", "68 millions", "7 milliards", "Paris", "Marseille",
               "français", "anglais", "l'euro", "le dollar", "La Marseillaise", "L'hymne à la joie", "Liberté, égalité, fraternité", "Un pour tous, tous pour un"] }] },
        4: { precision: "Commence par cinq régions faciles : la Bretagne (pointe à l'ouest), la Corse (l'île), les Hauts-de-France (tout au nord), le Grand Est (à l'est), l'Occitanie (au sud, vers l'Espagne)." },
        6: { precision: "Pour t'aider : l'école → la commune ; le collège → le département ; le lycée → la région." }
      },
      plusCM2: [{
        type: "ordre", points: 3,
        titre: "Pour aller plus loin",
        consigne: "Range ces territoires du plus vaste au plus petit.",
        items: [
          { id: "t1", texte: "L'Europe (continent)" },
          { id: "t2", texte: "La France (pays)" },
          { id: "t3", texte: "La Bourgogne-Franche-Comté (région)" },
          { id: "t4", texte: "La Côte-d'Or (département)" },
          { id: "t5", texte: "Dijon (commune)" }
        ],
        ordre: ["t1", "t2", "t3", "t4", "t5"],
        aide: "Chaque territoire est contenu dans le précédent : Dijon est en Côte-d'Or, qui est en Bourgogne-Franche-Comté."
      }]
    },
    s03: {
      cm1: {
        3: { precision: "Densité = habitants ÷ surface en km². Espace C : la surface est 2 km × 2 km = 4 km², puis 4 habitants ÷ 4 km²." },
        5: { precision: "Il y a 4 avantages et 6 inconvénients." }
      },
      plusCM2: [{
        type: "saisie", points: 4,
        titre: "Pour aller plus loin",
        consigne: "Compare deux communes imaginaires.",
        document: "<p><b>Village A</b> : 600 habitants sur 30 km². <b>Ville B</b> : 60 000 habitants sur 40 km².</p>",
        champs: [
          { label: "Densité du village A", solution: "20", unite: "hab/km²" },
          { label: "Densité de la ville B", solution: "1500", unite: "hab/km²" },
          { label: "La ville B est combien de fois plus dense que le village A ?", solution: "75" }
        ],
        aide: "600 ÷ 30, puis 60 000 ÷ 40. Pour comparer : 1 500 ÷ 20."
      }]
    },
    s04: {
      cm1: {
        1: { precision: "Les mots se lisent horizontalement ou verticalement. Regarde la première colonne de haut en bas !" },
        2: { consigne: "Pour chaque métier trouvé, indique le secteur d'activité.",
             precision: "Primaire : on exploite la nature. Secondaire : on fabrique, on transforme. Tertiaire : on rend un service.",
             colonnes: [{ titre: "Secteur", options: ["primaire", "secondaire", "tertiaire"] }],
             lignes: [
               { titre: "Caissier", solutions: ["tertiaire"] }, { titre: "Soudeur", solutions: ["secondaire"] },
               { titre: "Infirmier", solutions: ["tertiaire"] }, { titre: "Guide", solutions: ["tertiaire"] },
               { titre: "Ambulancier", solutions: ["tertiaire"] }, { titre: "Glacier", solutions: ["secondaire"] },
               { titre: "Pédiatre", solutions: ["tertiaire"] }, { titre: "Serveur", solutions: ["tertiaire"] },
               { titre: "Magasinier", solutions: ["tertiaire"] }, { titre: "Consultant", solutions: ["tertiaire"] }
             ] }
      },
      plusCM2: [{
        type: "saisie", points: 4,
        titre: "Pour aller plus loin",
        consigne: "Lis à nouveau le document sur les secteurs d'activité, puis calcule.",
        document: "<p>En 1911, près de 40 % des actifs travaillaient dans le secteur primaire.\n        Aujourd'hui : primaire 2,1 % • secondaire 18,2 % • tertiaire 79,7 %.</p>",
        champs: [
          { label: "Sur 100 actifs d'aujourd'hui, environ combien travaillent dans le tertiaire ?", solution: "80", tolerance: 1 },
          { label: "Et dans le secondaire (arrondis) ?", solution: "18", tolerance: 1 },
          { label: "De combien de points la part du primaire a-t-elle baissé depuis 1911 (arrondis) ?", solution: "38", tolerance: 1 }
        ],
        aide: "79,7 % est proche de 80 %. Pour la baisse : 40 − 2,1."
      }]
    },
    s05: {
      cm1: {
        3: { precision: "Chaque légende décrit un problème pour la montagne : l'air, la nature, le sol, l'eau, l'électricité. Un mot ne sert à rien." },
        5: { minimum: 8 }
      },
      plusCM2: [{
        type: "tri", points: 4,
        titre: "Pour aller plus loin",
        consigne: "Le tourisme est-il bon pour la montagne ? Range chaque proposition.",
        paniers: [{ id: "p", titre: "👍 Effets positifs" }, { id: "n", titre: "👎 Effets négatifs" }],
        items: [
          { id: "m1", texte: "Des emplois pour les habitants (moniteurs, saisonniers)", panier: "p" },
          { id: "m2", texte: "Des revenus pour les hôtels, les restaurants et les commerces", panier: "p" },
          { id: "m3", texte: "Des files de voitures qui polluent l'air", panier: "n" },
          { id: "m4", texte: "De nouvelles résidences construites sur la forêt", panier: "n" },
          { id: "m5", texte: "De l'eau prélevée pour les canons à neige", panier: "n" },
          { id: "m6", texte: "Des villages qui restent habités toute l'année", panier: "p" }
        ],
        aide: "Trois effets positifs, trois effets négatifs. Les effets négatifs sont ceux de tes photographies."
      }]
    },
    s06: {
      cm1: {
        1: { precision: "Lis bien le document : chaque touriste a un goût différent.",
             droite: [{ id: "a1", texte: "Le GR21 (randonnée sur les falaises)" }, { id: "a2", texte: "Le marché couvert" }, { id: "a3", texte: "Le parc des Roches" },
                      { id: "a4", texte: "Le Clos Lupin" }, { id: "a5", texte: "Le château les Aygues" }] },
        4: { precision: "Trois points positifs, trois points négatifs." },
        5: { minimum: 10 }
      },
      plusCM2: [{
        type: "saisie", points: 4,
        titre: "Pour aller plus loin",
        consigne: "Reprends le document sur la fréquentation d'Étretat.",
        document: "<p>Chaque année, les 1 200 habitants doivent cohabiter avec un million de visiteurs.\n        En 20 ans, près de 400 habitants ont quitté la station balnéaire.</p>",
        champs: [
          { label: "Environ combien de visiteurs par habitant chaque année ?", solution: "833", tolerance: 5 },
          { label: "Combien d'habitants Étretat comptait-elle il y a 20 ans, environ ?", solution: "1600", tolerance: 10 }
        ],
        aide: "1 000 000 ÷ 1 200. Il y a 20 ans : les 1 200 habitants d'aujourd'hui + les 400 qui sont partis."
      }]
    },
    s07: {
      cm1: {
        2: { precision: "Repère sur la carte : la Manche au nord-ouest, la mer du Nord tout au nord, l'océan Atlantique à l'ouest, la Méditerranée au sud." },
        4: { precision: "Hors vacances : 1 100 ÷ 4. L'été, il faut d'abord ajouter les touristes : 1 100 + 15 000 = 16 100, puis ÷ 4.",
             champs: [{ label: "Densité hors vacances", solution: "275", tolerance: 1, unite: "hab/km²" },
                      { label: "Densité pendant l'été", solution: "4025", tolerance: 5, unite: "hab/km²" }] }
      },
      plusCM2: [{
        type: "qcm", points: 3, disposition: "liste",
        titre: "Pour aller plus loin",
        consigne: "Pourquoi la densité d'Étretat est-elle environ 15 fois plus forte l'été ?",
        options: [
          { texte: "Parce que la surface de la commune diminue l'été.", correct: false },
          { texte: "Parce que les touristes s'ajoutent aux habitants, sur la même surface.", correct: true },
          { texte: "Parce que les habitants partent en vacances ailleurs.", correct: false }
        ],
        aide: "La surface reste 4 km² ; seul le nombre de personnes change."
      }]
    },
    s08: {
      cm1: {
        3: { precision: "Trois bonnes réponses : cherche les zones les plus riches sur la carte." },
        5: { precision: "Classe d'abord les pays du revenu le plus élevé (Norvège) au plus faible (Bangladesh)." },
        6: { minimum: 10 }
      },
      plusCM2: [{
        type: "qcm", points: 3, disposition: "liste",
        titre: "Pour aller plus loin",
        consigne: "D'après le tableau du PNUD, le Bangladesh a un revenu par habitant plus faible que la Guinée équatoriale, mais une espérance de vie plus longue (74,7 ans contre 63,7 ans). Que peut-on en conclure ?",
        options: [
          { texte: "La richesse ne suffit pas, à elle seule, à mesurer le développement d'un pays.", correct: true },
          { texte: "Les deux pays ont exactement le même niveau de vie.", correct: false },
          { texte: "L'espérance de vie ne dépend que du revenu des habitants.", correct: false }
        ],
        aide: "On mesure le développement avec plusieurs critères : le revenu, la santé (espérance de vie), l'éducation."
      }]
    },
    s09: {
      cm1: {
        2: { minimum: 10 },
        3: { precision: "Pose les additions : 3,81 + 2,29 + 1,22. Puis 8 − ce total.",
             champs: [
               { label: "La famille C achète 1 kg de pâtes importées, 100 g de fromage et 1 yaourt. Combien dépense-t-elle ?", solution: "7.32", tolerance: 0.02, unite: "€" },
               { label: "Combien lui reste-t-il alors sur ses 8 € ?", solution: "0.68", tolerance: 0.02, unite: "€" }
             ] }
      },
      plusCM2: [{
        type: "saisie", points: 3,
        titre: "Pour aller plus loin",
        consigne: "La famille A (France, 25 €) achète les mêmes produits importés que la famille C.",
        champs: [
          { label: "Combien lui reste-t-il ?", solution: "17.68", tolerance: 0.02, unite: "€" },
          { label: "Quelle part de son budget a-t-elle dépensée ? (en %, arrondi à l'unité)", solution: "29", tolerance: 1, unite: "%" }
        ],
        aide: "25 − 7,32. Pour la part : 7,32 ÷ 25 × 100. La famille C, elle, a dépensé plus de 90 % de ses 8 €."
      }]
    },
    s10: {
      cm1: {
        3: { consigne: "À la ferme de Bray : quel métier produit l'aliment de chaque espace de production ?",
             precision: "L'éleveur s'occupe des animaux, le céréalier du blé, le maraîcher des légumes, l'arboriculteur des arbres fruitiers.",
             colonnes: [{ titre: "Métier", options: ["éleveur", "céréalier", "maraîcher", "arboriculteur"] }],
             lignes: [
               { titre: "Un élevage", solutions: ["éleveur"] }, { titre: "Un champ de blé", solutions: ["céréalier"] },
               { titre: "Un champ ou exploitation maraîchère", solutions: ["maraîcher"] }, { titre: "Un verger", solutions: ["arboriculteur"] }
             ] }
      },
      plusCM2: [{
        type: "tri", points: 4,
        titre: "Pour aller plus loin",
        consigne: "Du champ à ton assiette : range chaque activité dans son secteur.",
        paniers: [{ id: "pri", titre: "Primaire (exploiter la nature)" }, { id: "sec", titre: "Secondaire (transformer)" }, { id: "ter", titre: "Tertiaire (rendre un service)" }],
        items: [
          { id: "x1", texte: "Élever des poulets", panier: "pri" },
          { id: "x2", texte: "Cultiver des carottes", panier: "pri" },
          { id: "x3", texte: "Fabriquer du fromage", panier: "sec" },
          { id: "x4", texte: "Fabriquer des cookies", panier: "sec" },
          { id: "x5", texte: "Livrer les magasins", panier: "ter" },
          { id: "x6", texte: "Vendre les produits au marché", panier: "ter" }
        ],
        aide: "Deux activités par secteur. Transporter et vendre, c'est rendre un service."
      }]
    },
    s11: {
      cm1: {
        1: { precision: "La première étape se passe au pré, la dernière au supermarché." },
        4: { minimum: 10 }
      },
      plusCM2: [{
        type: "tri", points: 4,
        titre: "Pour aller plus loin",
        consigne: "Le yaourt passe par les trois secteurs d'activité. Range chaque étape.",
        paniers: [{ id: "pri", titre: "Primaire" }, { id: "sec", titre: "Secondaire" }, { id: "ter", titre: "Tertiaire" }],
        items: [
          { id: "y1", texte: "Les vaches pâturent au pré", panier: "pri" },
          { id: "y2", texte: "La traite du lait à la ferme", panier: "pri" },
          { id: "y3", texte: "Le lait est chauffé et ensemencé de ferments", panier: "sec" },
          { id: "y4", texte: "Le yaourt est mis en pots", panier: "sec" },
          { id: "y5", texte: "Le camion frigorifique livre les magasins", panier: "ter" },
          { id: "y6", texte: "Le yaourt est vendu au supermarché", panier: "ter" }
        ],
        aide: "À la ferme : primaire. À l'usine : secondaire. Transport et vente : tertiaire."
      }]
    },
    s12: {
      cm1: {
        2: { precision: "Additionne deux par deux : 11 702 + 2 585 = 14 287 ; 1 013 + 3 422 = 4 435 ; puis 14 287 + 4 435, et enfin + 2 292." },
        3: { precision: "Quatre bonnes réponses." }
      },
      plusCM2: [{
        type: "saisie", points: 3,
        titre: "Pour aller plus loin",
        consigne: "Et si la poire de la salade venait d'un verger français, à quelques kilomètres ?",
        precision: "On compte alors 0 km pour la poire au lieu de 11 702 km.",
        champs: [
          { label: "Nouveau total des kilomètres alimentaires", solution: "9312", tolerance: 0, unite: "km" },
          { label: "Combien de kilomètres économise-t-on ?", solution: "11702", tolerance: 0, unite: "km" }
        ],
        aide: "21 014 − 11 702. Un seul produit lointain pèse plus que tous les autres réunis !"
      }]
    },
    s13: {
      cm1: {
        1: { precision: "Commence par la Seine (elle traverse Paris), la Garonne (au sud-ouest), les Pyrénées (frontière avec l'Espagne) et les Alpes (frontière avec l'Italie)." },
        4: { precision: "Six massifs : Alpes, Pyrénées, Massif central, Jura, Vosges, Corse." }
      },
      plusCM2: [{
        type: "tableau", points: 4,
        titre: "Pour aller plus loin",
        consigne: "Dans quel massif chacun de ces fleuves prend-il sa source ?",
        precision: "Certaines sources se trouvent hors de France : le Rhône et le Rhin naissent en Suisse, la Garonne en Espagne.",
        entete: "Fleuve",
        colonnes: [{ titre: "Massif de la source", options: ["les Alpes", "les Pyrénées", "le Massif central", "les Vosges", "le Jura"] }],
        lignes: [
          { titre: "La Loire", solutions: ["le Massif central"] },
          { titre: "La Garonne", solutions: ["les Pyrénées"] },
          { titre: "Le Rhône", solutions: ["les Alpes"] },
          { titre: "Le Rhin", solutions: ["les Alpes"] }
        ],
        aide: "La Loire naît au mont Gerbier-de-Jonc (Ardèche). Deux fleuves viennent des Alpes suisses."
      }]
    },
    s14: {
      cm1: {
        4: { precision: "L'amont et la source sont en haut du schéma, l'aval, l'estuaire et la mer en bas, à droite." }
      },
      plusCM2: [{
        type: "qcm", points: 3, disposition: "liste",
        titre: "Pour aller plus loin",
        consigne: "La Seine traverse Paris, puis rejoint la mer près du Havre. Par rapport à Paris, Le Havre est donc situé…",
        options: [
          { texte: "en amont, car il est plus près de la source", correct: false },
          { texte: "en aval, car il est plus près de l'embouchure", correct: true },
          { texte: "sur un affluent de la Seine", correct: false }
        ],
        aide: "L'aval, c'est la direction vers laquelle coule l'eau : vers la mer."
      }]
    },
    s15: {
      cm1: {
        2: { precision: "Additionne les huit postes du document pour trouver la consommation d'un Français.",
             champs: [
               { label: "Consommation moyenne d'un Français, en litres par jour", solution: "150", tolerance: 5, unite: "L" },
               { label: "Pourcentage de l'usage domestique", solution: "24", unite: "%" },
               { label: "Nombre de litres bus chaque jour par un Français", solution: "1.5", tolerance: 0.1, unite: "L" }
             ] },
        4: { precision: "Le trajet commence dans la rivière (ou la nappe) et se termine dans le milieu naturel." }
      },
      plusCM2: [{
        type: "saisie", points: 3,
        titre: "Pour aller plus loin",
        consigne: "Reprends le document sur la consommation quotidienne d'un Français (150 L).",
        document: "<p>Bain et douche 58,5 L • sanitaires 30 L • lave-linge 18 L • vaisselle 15 L • lavage voiture 9 L •\n        arrosage 9 L • cuisine 9 L • boisson 1,5 L.</p>",
        champs: [
          { label: "Quel pourcentage de l'eau sert au bain et à la douche ? (arrondi)", solution: "39", tolerance: 1, unite: "%" },
          { label: "Combien de litres pour les sanitaires et le lave-linge ensemble ?", solution: "48", unite: "L" }
        ],
        aide: "58,5 ÷ 150 × 100. Puis 30 + 18."
      }]
    },
    s16: {
      cm1: {
        2: { minimum: 10 },
        4: { precision: "Trois usages autorisés, deux avec restrictions, cinq interdits." }
      },
      plusCM2: [{
        type: "ouverte", points: 3, minimum: 20,
        titre: "Pour aller plus loin",
        consigne: "Le préfet autorise l'arrosage des cultures, mais seulement la nuit. Pourquoi la nuit, à ton avis ?",
        pistes: [
          "La nuit, il fait plus frais : moins d'eau s'évapore avant d'atteindre les racines.",
          "On économise donc l'eau tout en sauvant les récoltes.",
          "C'est un compromis entre les besoins des agriculteurs et la protection de la ressource."
        ]
      }]
    }
  };

  /** Normalise le niveau : "CM1", "CM2" ou "DEC" (palier Découverte). */
  function niveauDe(v){ v = String(v || "").toUpperCase(); return v === "CM1" || v === "DEC" ? v : "CM2"; }

  /**
   * Version d'une séance pour un niveau (copie : les données d'origine ne changent pas).
   * Chaque activité garde la trace de son origine : a.niveauSource = "livret" | "cm1" | "cm2+".
   */
  MISSION.adapter = function(s, niveau){
    const n = niveauDe(niveau), d = DIFF[s.id] || {};
    const copie = JSON.parse(JSON.stringify(s));
    copie.niveau = n;
    const regles = n === "CM2" ? (d.cm2 || {}) : (d.cm1 || {});
    copie.activites = copie.activites.map((a, i) => {
      const r = regles[i + 1];
      return r ? Object.assign(a, JSON.parse(JSON.stringify(r)), { niveauSource: n === "CM2" ? "cm2" : "cm1" }) : Object.assign(a, { niveauSource: "livret" });
    });
    if(n === "CM2") (d.plusCM2 || []).forEach(a => {
      const x = Object.assign(JSON.parse(JSON.stringify(a)), { niveauSource: "cm2+" });
      if(x.titre) x.consigne = "🚀 " + x.titre + " — " + x.consigne;
      copie.activites.push(x);
    });
    if(n === "DEC") copie.activites.forEach(a => {
      if(a.aide && !(a.precision || "").includes(a.aide)) a.precision = (a.precision ? a.precision + " " : "") + "💡 " + a.aide;
      a.aideOfferte = true;
    });
    return copie;
  };
  MISSION.niveauDe = niveauDe;
  MISSION.DIFFERENCIATION = DIFF;
})();
