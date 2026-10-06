/* ============================================================
   CONFIGURATION DU JEU (la SEULE chose à changer pour décliner le moteur immersif)
   ------------------------------------------------------------
   Chargée avant tout le reste. Le moteur lit ces valeurs partout (titres, grades, clés de sauvegarde).
   Un jeu issu du migrateur (outils/immersif/migrer-jeu.py) reçoit son propre fichier.
   Les valeurs ci-dessous sont celles de « Vingt mille lieues sous les mers » : rien ne change pour lui.
   ============================================================ */
window.VML_JEU = {
  id: "vingt-mille-lieues",
  prefixeStockage: "vml",                       // clés du navigateur : <prefixe>_partie, <prefixe>_reglages
  grades: ["mousse", "matelot", "timonier", "lieutenant", "second"],   // grades proposés (ordre croissant)
  textes: {
    auteur: "Jules Verne",
    titre: "Vingt mille lieues sous les mers",
    sousTitre: "Le Journal du Nautilus",
    journal: "Le Journal du Nautilus",           // titre court (onglet, tableau de bord, comptes rendus)
    hud: "⚓ Le Journal du Nautilus",
    bibliotheque: "La Bibliothèque du Nautilus",
    coffre: "🔐 Le coffre du capitaine Nemo",
    pause: "⏸ Le Nautilus est stoppé",
    fichierExport: "nautilus",
    mission: "✍️ Fiche de mission — le journal du Nautilus",
    lecons: "Leçons A4 — La Bibliothèque du Nautilus",
    escale: "Escale"                              // mot employé pour une étape (« salle », « station »…)
  }
};
