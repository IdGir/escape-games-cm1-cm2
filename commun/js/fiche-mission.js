/* TRONC COMMUN (commun/js/) — un seul fichier pour tous les jeux : les textes
   propres à chaque jeu sont dans <jeu>/js/jeu.js (objet JEU). */
/* ============================================================
   FICHE DE MISSION — moteur d'énigmes v2 (octobre 2026)
   Feuille A4 distribuée à chaque équipe avant la partie.
   Les élèves y notent le mot trouvé dans chaque salle : il n'est
   affiché qu'une fois à l'écran, puis il faut le recopier dans le
   coffre final. Rappel du barème « tout juste du premier coup ».
   Imprimée depuis ⚙️ Réglages > Impression.
   Fichier maître : outils-moteur/fiche-mission.js
   ============================================================ */
function imprimerFicheMission(){
  const zone = preparerZoneImpression();
  const toutes = (typeof DONNEES !== "undefined" && DONNEES) ? (typeof DONNEES === "function" ? DONNEES() : DONNEES) : null;
  const liste = (toutes && toutes.salles) ? toutes.salles : (window.FICHE_MISSION_SALLES || []);
  // seules les étapes qui donnent un mot à noter (motCle ou fragment)
  const avecMot = liste.filter(s=>s.motCle || s.fragment || s.mot);
  const salles = avecMot.length ? avecMot : liste;
  const lib = window.FICHE_MISSION_LIBELLE || "Salle";     // « Escale » pour le Tour du monde
  const premier = (typeof PTS_PREMIER_COUP !== "undefined") ? PTS_PREMIER_COUP : 10;
  const apres = (typeof PTS_APRES_ERREUR !== "undefined") ? PTS_APRES_ERREUR : 3;
  const coffre = (typeof PTS_COFFRE_PREMIER !== "undefined") ? PTS_COFFRE_PREMIER : 10;
  const titreJeu = document.title.replace(/\s*[—-]\s*Escape Game.*$/i, "");
  const cases = n => Array.from({length:n}, ()=>'<span style="display:inline-block;width:7mm;height:7mm;border:1.2px solid #333;margin-right:2mm;border-radius:1.5mm"></span>').join("");
  const lignes = salles.map(s => `
    <tr>
      <td style="padding:3mm;border:1.5px solid #333;width:48%;vertical-align:top">
        <div style="font-size:9pt;color:#555">${s.etiquette || (lib + " " + s.num)}</div>
        <div style="font-size:12pt;font-weight:bold">${s.titre}</div>
      </td>
      <td style="padding:3mm;border:1.5px solid #333;vertical-align:bottom">
        <div style="font-size:8.5pt;color:#555;margin-bottom:6mm">Mot trouvé :</div>
        <div style="border-bottom:1.5px dotted #333;height:1mm"></div>
      </td>
    </tr>`).join("");
  zone.innerHTML = `
    ${enteteFiche("Fiche de mission", "Équipe", "", false)}
    <div class="impr-titre-principal">Fiche de mission</div>
    <div class="impr-soustitre">${titreJeu}</div>
    <div class="impr-cartouche">
      <div class="champ"><div class="label">Nom de l'équipe</div><div class="ligne"></div></div>
      <div class="champ"><div class="label">Prénoms</div><div class="ligne"></div></div>
      <div class="champ"><div class="label">Niveau</div><div class="ligne"></div></div>
    </div>
    <div style="border:2px solid #1d3a8a;border-radius:3mm;padding:3mm 4mm;margin:4mm 0;font-size:10.5pt;background:#eef3ff">
      <b>🎯 Le barème récompense la réflexion, pas la vitesse :</b><br>
      • énigme juste <b>du premier coup : ${premier} points</b> ; après une erreur : ${apres} points seulement ;<br>
      • l'ordinateur dit seulement <b>combien</b> de réponses sont justes, jamais lesquelles ;<br>
      • avant de valider, <b>relisez la leçon</b> (bouton 📚) pour être sûrs de votre réponse.
    </div>
    <div style="border:2px solid #b22222;border-radius:3mm;padding:3mm 4mm;margin:4mm 0;font-size:10.5pt;background:#fff3f0">
      <b>✍️ À chaque fin de ${lib.toLowerCase()}, un mot s'affiche une seule fois.</b> Notez-le tout de suite ci-dessous :
      il faudra recopier les ${salles.length || 5} mots pour ouvrir le coffre final (${coffre} points du premier coup).
    </div>
    <table style="width:100%;border-collapse:collapse;margin-top:3mm">${lignes}</table>
    <div style="margin-top:6mm;font-size:10pt">
      <b>Énigmes justes du premier coup</b> (cochez une case à chaque fois) :<br>
      <div style="margin-top:2mm">${cases(10)}</div><div style="margin-top:2mm">${cases(10)}</div>
    </div>
    ${piedPageFiche(1, 1, "Fiche de mission")}
  `;
  window.print();
}
window.imprimerFicheMission = imprimerFicheMission;
