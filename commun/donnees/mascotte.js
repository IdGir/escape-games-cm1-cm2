/* ============================================================
   TEXTES DE LA MASCOTTE COMMUNE (amélioration N11)
   ------------------------------------------------------------
   Noa, le guide de la collection d'escape games (portrait SVG et animation :
   commun/js/mascotte.js). Elle n'a que trois rôles, jamais pendant une énigme :
     1. accueillir la classe (accueil de la collection et accueil de chaque jeu) ;
     2. expliquer les règles communes au premier lancement (« Comment jouer ? ») :
        barème, coffre, indices ;
     3. annoncer les trophées gagnés (N1) à l'écran de fin.
   Un texte propre à un jeu ne s'écrit jamais ici (elle parle de la collection).
   Les valeurs du barème sont lues dans le jeu quand il les déclare
   (PTS_PREMIER_COUP, PTS_APRES_ERREUR, MALUS_INDICE, PTS_COFFRE_PREMIER),
   sinon les valeurs communes ci-dessous sont utilisées.
   Fichier .js (et non .json) pour fonctionner aussi en double-clic.
   ============================================================ */
var MASCOTTE_TEXTES = {
  nom: "Noa",
  role: "Le guide de la collection",
  /* barème commun, utilisé quand le jeu ne le déclare pas */
  bareme: { premier: 10, apres: 3, indice: 2, coffre: 10 },

  /* ---- Accueil de la collection (accueil des jeux) ---- */
  accueilCollection: function(n){
    return "Bonjour la classe ! Moi, c'est Noa. Dans cette collection, " + (n > 1 ? "vous avez " + n + " escape games" : "vous avez un escape game")
      + " pour apprendre en s'amusant : on explore des lieux, on résout des énigmes en équipe, et on ouvre un coffre à la fin. Choisissez un jeu !";
  },
  /* ---- Accueil d'un jeu ---- */
  accueilJeu: "Bonjour l'équipe ! Je suis Noa, je vous accompagne dans tous les escape games. Choisissez un nom d'équipe et votre niveau, puis lancez-vous.",
  retour: "Content de vous revoir ! Même règles que d'habitude : on réfléchit ensemble, on lit les leçons, on se fait confiance.",

  /* ---- Comment jouer ? (règles communes) ---- */
  regles: function(b){
    return [
      { icone: "🎯", titre: "Les points",
        texte: "Une énigme réussie du premier coup rapporte " + b.premier + " points ; après une erreur, " + b.apres + " points seulement. Un indice coûte " + b.indice + " points : mieux vaut d'abord relire la leçon !" },
      { icone: "🔐", titre: "Le coffre final",
        texte: "Chaque salle vous donne un mot. Notez-le tout de suite sur votre fiche de mission : il ne s'affichera qu'une seule fois. À la fin, recopiez tous les mots dans le coffre (" + b.coffre + " points si c'est juste du premier coup)." },
      { icone: "💡", titre: "Les indices et les leçons",
        texte: "Bloqués ? Demandez un indice (jusqu'à trois par énigme) ou ouvrez la leçon 📚. Quand vous vous trompez, le jeu dit combien de réponses sont justes, mais jamais lesquelles : à vous de chercher !" },
      { icone: "🤝", titre: "En équipe",
        texte: "On réfléchit ensemble, chacun son tour pour manipuler, et on s'écoute. Votre enseignant peut vous aider ou vous prévenir quand la séance se termine." },
      { icone: "🏅", titre: "Les trophées",
        texte: "Chaque partie terminée peut vous faire gagner des trophées, qui se cumulent d'un jeu à l'autre sous le même nom d'équipe." }
    ];
  },
  /* lecture à voix haute de « Comment jouer ? » */
  lectureRegles: function(b){
    return this.regles(b).map(function(r){ return r.titre + ". " + r.texte; }).join(" ");
  },

  /* ---- Trophées gagnés (écran de fin) ---- */
  trophees: function(noms){
    if(noms.length === 1) return "Bravo ! Vous avez gagné un nouveau trophée : " + noms[0] + ". Retrouvez tous vos trophées dans la vitrine.";
    return "Bravo ! Vous avez gagné " + noms.length + " nouveaux trophées : " + noms.slice(0, -1).join(", ") + " et " + noms[noms.length - 1] + ". Retrouvez-les tous dans la vitrine.";
  }
};
