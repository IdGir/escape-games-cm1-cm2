/* =========================================================
   LA PISTE FINALE — symboles, calculs, pays, récompense
   ---------------------------------------------------------
   Chaque séance réussie dépose dans le carnet soit un NOMBRE
   porté par un symbole, soit un FAIT sur le pays recherché.
   La piste finale se joue en trois temps :
     1. identifier le PAYS grâce aux six faits ;
     2. calculer la CASE de la carte grâce aux dix nombres ;
     3. ouvrir le cadenas de la valise grâce au CODE.
   Les valeurs attendues ne sont écrites nulle part en dur :
   elles sont recalculées à partir des indices des séances,
   ce qui garantit qu'elles restent justes si vous modifiez
   une activité.
   ========================================================= */

MISSION.definirFinal({

  /* ---- Les symboles utilisés par les indices chiffrés ---- */
  symboles: {
    etoile:    { glyphe: "✳", nom: "l'étoile" },
    cercle:    { glyphe: "●", nom: "le cercle" },
    nuage:     { glyphe: "☁", nom: "le nuage" },
    pentagone: { glyphe: "⬟", nom: "le pentagone" },
    trapeze:   { glyphe: "▽", nom: "le trapèze" },
    goutte:    { glyphe: "💧", nom: "la goutte" },
    hexagone:  { glyphe: "⬡", nom: "l'hexagone" },
    losange:   { glyphe: "◆", nom: "le losange" },
    coeur:     { glyphe: "♥", nom: "le cœur" },
    carre:     { glyphe: "■", nom: "le carré" }
  },

  /* ---- Étape 1 : le pays ---- */
  pays: {
    consigne: "Relis les indices de ton carnet. À quel pays appartient la valise ?",
    propositions: [
      { id: "espagne",  nom: "Espagne",       drapeau: "🇪🇸" },
      { id: "usa",      nom: "États-Unis",    drapeau: "🇺🇸" },
      { id: "uk",       nom: "Royaume-Uni",   drapeau: "🇬🇧" },
      { id: "mexique",  nom: "Mexique",       drapeau: "🇲🇽" }
    ],
    solution: "mexique",
    explication: `Le Mexique est le seul pays qui réunit les six indices : il se trouve en
      Amérique latine, dans l'hémisphère nord ; on y parle espagnol ; il est bordé par
      l'océan Pacifique ; son drapeau est vert, blanc et rouge.`
  },

  /* ---- Étape 2 : la case de la carte ---- */
  carte: {
    consigne: "Sur la carte quadrillée de la côte ouest de la Corse, calcule la colonne puis la ligne.",
    colonnes: 5,
    lignes: 5,
    lieu: "les calanques de Piana, dans le golfe de Porto",
    calculs: [
      {
        cle: "colonne",
        titre: "Numéro de la colonne",
        termes: [
          { op: "+", symbole: "nuage" },
          { op: "-", symbole: "etoile" }
        ]
      },
      {
        cle: "ligne",
        titre: "Numéro de la ligne",
        termes: [
          { op: "+", symbole: "carre" },
          { op: "-", symbole: "trapeze" },
          { op: "-", symbole: "coeur" },
          { op: "+", symbole: "losange" },
          { op: "-", symbole: "hexagone" },
          { op: "+", symbole: "goutte" },
          { op: "-", symbole: "pentagone" }
        ]
      }
    ]
  },

  /* ---- Étape 3 : le code du cadenas ---- */
  cadenas: {
    consigne: "Un cadenas à deux chiffres ferme la valise. Calcule son code.",
    termes: [
      { op: "+", symbole: "cercle" },
      { op: "×", symbole: "etoile" }
    ]
  },

  /* ---- Texte de dénouement ---- */
  denouement: `<p>La valise est là, à demi enfouie sous un pin, à l'endroit exact que tes
    calculs désignaient. Le cadenas cède.</p>
    <p>À l'intérieur, pas d'arme, pas de trésor : un carnet, des relevés, des photographies.
    La « nouvelle ressource » que les malfaiteurs voulaient s'approprier, c'était
    <b>l'eau douce</b> — et les moyens de la partager équitablement.</p>
    <p>Le Professeur Atlas t'attend. Il a préparé quelque chose pour toi…</p>`,

  /* ---- Récompense : entièrement configurable dans l'espace enseignant ---- */
  recompenseParDefaut: {
    titre: "La récompense mystère",
    texte: `<p>La récompense n'a pas encore été déposée par ton enseignant.</p>
      <p><i>Enseignant : ouvrez l'espace enseignant (⚙️), rubrique « Récompense mystère »,
      pour écrire le message et, si vous le souhaitez, déposer une image ou une vidéo
      qui s'affichera ici.</i></p>`,
    media: "recompense"
  }
});
