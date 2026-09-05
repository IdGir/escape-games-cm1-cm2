/* =========================================================
   LEÇONS — affichage de la trace écrite
   Consultable pendant l'énigme, après la réussite,
   et imprimable au format A4.
   ========================================================= */

const LECONS = (function(){

  function corps(id, options){
    options = options || {};
    const l = MISSION.lecons[id];
    if(!l) return "<p>Leçon introuvable.</p>";

    let h = '<div class="lecon">';
    h += "<h2>" + l.titre + "</h2>";

    if(l.objectifs && l.objectifs.length){
      h += '<div class="objectifs"><b>Ce que je dois savoir faire :</b><ul>';
      l.objectifs.forEach(o => { h += "<li>" + o + "</li>"; });
      h += "</ul></div>";
    }

    h += l.texte;

    if(l.vocabulaire && l.vocabulaire.length){
      h += "<h3>Vocabulaire</h3><dl class=\"vocabulaire\">";
      l.vocabulaire.forEach(([mot, def]) => {
        h += "<dt>" + mot + "</dt><dd>" + def + "</dd>";
      });
      h += "</dl>";
    }

    if(l.aRetenir){
      h += '<div class="a-retenir"><h4>À retenir</h4><p>' + l.aRetenir + "</p></div>";
    }
    h += "</div>";

    if(!options.sansMedia && l.media) h += '<div class="media-slot" data-lecon-media="' + id + '"></div>';
    return h;
  }

  function ouvrir(id){
    const l = MISSION.lecons[id];
    if(!l){ APP.message("Aucune leçon associée à cette séance.", "erreur"); return; }
    APP.modale(corps(id), () => {
      const hote = document.querySelector('[data-lecon-media="' + id + '"]');
      if(hote && typeof MEDIAS !== "undefined") MEDIAS.remplir(hote, l.media);
    });
  }

  /* Bibliothèque : toutes les leçons débloquées */
  function bibliotheque(){
    const etat = SAUVEGARDE.lire();
    let h = "<h2>📚 Bibliothèque des leçons</h2>";
    h += '<p class="aide-panneau">Les leçons des séances déjà jouées sont consultables ici ' +
         'à tout moment.</p><ul style="list-style:none;padding:0;display:grid;gap:.5rem">';
    MISSION.ordre().forEach(s => {
      const l = MISSION.lecons[s.lecon];
      if(!l) return;
      const ouvertePar = SAUVEGARDE.estReussie(s.id) || etat.reglages.ordreLibre;
      h += '<li><button class="bouton-second" style="width:100%;text-align:left" ' +
           (ouvertePar ? '' : 'disabled ') +
           'data-lecon="' + s.lecon + '">' +
           (ouvertePar ? "📖 " : "🔒 ") + "Séance " + s.numero + " — " + l.titre +
           "</button></li>";
    });
    h += "</ul>";
    APP.modale(h, () => {
      document.querySelectorAll("[data-lecon]").forEach(b => {
        b.addEventListener("click", () => ouvrir(b.dataset.lecon));
      });
    });
  }

  return { ouvrir, corps, bibliotheque };
})();
