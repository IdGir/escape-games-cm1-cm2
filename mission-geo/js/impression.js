/* =========================================================
   IMPRESSION — fiches A4 pour la classe
   ---------------------------------------------------------
   Toutes les fiches sont composées au format A4 strict :
   cartouche élève, titre, niveau, séance concernée, date,
   pagination, et mention CORRIGÉ quand il s'agit du corrigé.
   Le rendu se fait dans la modale, puis on lance l'impression :
   la feuille de style print.css masque tout le reste.
   ========================================================= */

const IMPRESSION = (function(){

  const jour = () => new Date().toLocaleDateString("fr-FR");

  function cartouche(sousTitre, corrige){
    const etat = SAUVEGARDE.lire();
    let h = "";
    if(corrige) h += '<p class="bandeau-corrige">Corrigé — document enseignant</p>';
    h += '<div class="cartouche">';
    h += corrige
      ? "<div class=\"lignes-eleve\"><b>Classe :</b> " + (etat.niveau || "CM1 / CM2") +
        " &nbsp; <b>Équipe :</b> " + (etat.equipe || "—") + "<br><b>Édité le :</b> " + jour() + "</div>"
      : "<div class=\"lignes-eleve\"><b>Nom :</b> <span></span> &nbsp; <b>Prénom :</b> <span></span>" +
        "<br><b>Classe :</b> " + (etat.niveau || "CM1 / CM2") + " &nbsp; <b>Date :</b> " + jour() + "</div>";
    h += "<div><b>Mission géographique — Année A</b><br>" + sousTitre + "</div>";
    h += "</div>";
    return h;
  }

  function pied(texte){
    return '<div class="pied-page"><span>Mission géographique — Année A</span><span>' +
           texte + "</span></div>";
  }

  function imprimer(html){
    APP.modale('<div class="apercu-a4">' + html + "</div>", () => {
      setTimeout(() => window.print(), 250);
    });
  }

  /* ---------------- Leçon ---------------- */
  function lecon(idLecon){
    const l = MISSION.lecons[idLecon];
    if(!l) return;
    const s = MISSION.sessions.find(x => x.lecon === idLecon);
    let h = '<section class="feuille">';
    h += cartouche("Leçon" + (s ? " — séance " + s.numero : ""), false);
    h += "<h1>" + l.titre + "</h1>";
    if(l.objectifs && l.objectifs.length){
      h += '<div class="encadre"><b>Ce que je dois savoir faire :</b><ul>';
      l.objectifs.forEach(o => h += "<li>" + o + "</li>");
      h += "</ul></div>";
    }
    h += l.texte;
    if(l.vocabulaire && l.vocabulaire.length){
      h += "<h2>Vocabulaire</h2><table><tr><th style='width:32%'>Mot</th><th>Définition</th></tr>";
      l.vocabulaire.forEach(([m, d]) => h += "<tr><td><b>" + m + "</b></td><td>" + d + "</td></tr>");
      h += "</table>";
    }
    if(l.aRetenir) h += '<div class="encadre a-retenir"><b>À retenir.</b> ' + l.aRetenir + "</div>";
    h += pied("Leçon " + idLecon.toUpperCase());
    h += "</section>";
    imprimer(h);
  }

  /* ---------------- Fiche de préparation ---------------- */
  function preparation(idSession){
    const s = MISSION.parId(idSession);
    if(!s) return;
    const l = MISSION.lecons[s.lecon];
    let h = '<section class="feuille">';
    h += cartouche("Fiche de préparation — séance " + s.numero, true);
    h += "<h1>Séance " + s.numero + " — " + s.titre + "</h1>";
    h += "<table>";
    h += "<tr><th style='width:28%'>Période</th><td>Période " + s.periode + "</td></tr>";
    h += "<tr><th>Thème du programme</th><td>" + s.theme + "</td></tr>";
    h += "<tr><th>Élément travaillé</th><td>" + s.element + "</td></tr>";
    h += "<tr><th>Lieu de la mission</th><td>" + s.lieu + "</td></tr>";
    h += "<tr><th>Page du livret papier</th><td>page " + s.livret + "</td></tr>";
    h += "<tr><th>Durée indicative</th><td>" + s.duree + " minutes</td></tr>";
    h += "<tr><th>Leçon associée</th><td>" + (l ? l.titre : "—") + "</td></tr>";
    h += "<tr><th>Indice obtenu</th><td>" + decrireIndice(s) + "</td></tr>";
    h += "</table>";

    if(l && l.objectifs){
      h += "<h2>Objectifs</h2><ul>";
      l.objectifs.forEach(o => h += "<li>" + o + "</li>");
      h += "</ul>";
    }

    h += "<h2>Déroulement</h2><ol>";
    h += "<li><b>Mise en situation</b> — projection de l'introduction (média + narration).</li>";
    s.activites.forEach((a, i) => {
      h += "<li><b>Énigme " + (i + 1) + "</b> (" + libelleType(a.type) + ", " +
           (a.points || 3) + " pts) — " + texteSimple(a.consigne) + "</li>";
    });
    h += "<li><b>Institutionnalisation</b> — lecture et copie de la leçon.</li>";
    h += "<li><b>Dénouement</b> — récupération de l'indice, report dans le carnet de mission.</li>";
    h += "</ol>";

    h += "<h2>Matériel et médias</h2><ul>";
    h += "<li>Poste élève ou vidéoprojecteur, application <i>mission-geo</i>.</li>";
    mediasAttendus(s).forEach(m => h += "<li>Emplacement média facultatif : <code>" + m + "</code></li>");
    h += "</ul>";

    h += pied("Séance " + s.numero + " — préparation");
    h += "</section>";
    imprimer(h);
  }

  /* ---------------- Fiche élève (exercices sur papier) ---------------- */
  function ficheEleve(idSession, corrige){
    const s = MISSION.parId(idSession);
    if(!s) return;
    const profil = SAUVEGARDE.lire().profil;
    let h = '<section class="feuille">';
    h += cartouche("Séance " + s.numero + " — " + s.titre, corrige);
    h += "<h1>" + s.titre + "</h1>";
    h += "<p><i>" + s.element + "</i></p>";

    s.activites.forEach((a, i) => {
      h += "<h2>" + (i + 1) + ". " + texteSimple(remplace(a.consigne, profil)) + "</h2>";
      if(a.precision) h += "<p><i>" + texteSimple(a.precision) + "</i></p>";
      if(a.document) h += '<div class="encadre">' + a.document + "</div>";
      h += rendreExercice(a, corrige, profil);
    });

    h += pied("Séance " + s.numero + (corrige ? " — corrigé" : " — fiche élève"));
    h += "</section>";
    imprimer(h);
  }

  function rendreExercice(a, corrige, profil){
    const R = x => corrige ? "<b>" + x + "</b>" : '<span class="ligne-reponse"></span>';
    let h = "";
    switch(a.type){
      case "qcm":
        h += "<ul>";
        a.options.forEach(o => h += "<li>" + (corrige ? (o.correct ? "☑ <b>" : "☐ ") : "☐ ") +
          o.texte + (corrige && o.correct ? "</b>" : "") + "</li>");
        h += "</ul>";
        break;
      case "vraifaux":
        h += "<table><tr><th>Affirmation</th><th style='width:14%'>V ou F</th></tr>";
        a.items.forEach(it => h += "<tr><td>" + it.texte + "</td><td style='text-align:center'>" +
          (corrige ? "<b>" + (it.reponse ? "V" : "F") + "</b>" : "") + "</td></tr>");
        h += "</table>";
        break;
      case "trous": {
        const mots = [];
        const texte = String(a.texte).replace(/\[\[([^\]]+)\]\]/g, (m, mot) => {
          mots.push(mot);
          return corrige ? "<b>" + mot + "</b>" : "…………………";
        });
        h += "<p><i>Mots à utiliser : " +
             ACTIVITES.melanger(mots.concat(a.intrus || [])).join(" · ") + "</i></p>";
        h += "<p>" + texte + "</p>";
        break;
      }
      case "relier": {
        h += "<table><tr><th>Colonne A</th><th>Colonne B</th></tr>";
        const droite = new Map(a.droite.map(d => [d.id, d.texte]));
        const paires = new Map(a.paires);
        a.gauche.forEach((g, i) => {
          h += "<tr><td>" + g.texte + "</td><td>" +
               (corrige ? "<b>" + (droite.get(paires.get(g.id)) || "") + "</b>"
                        : (a.droite[i] ? a.droite[i].texte : "")) + "</td></tr>";
        });
        h += "</table>";
        if(!corrige) h += "<p><i>Relie chaque élément de la colonne A à celui qui convient dans la colonne B.</i></p>";
        break;
      }
      case "ordre":
        h += "<table><tr><th style='width:12%'>N°</th><th>Étape</th></tr>";
        (corrige ? a.ordre.map(x => a.items.find(i => i.id === x)) : a.items).forEach((it, i) =>
          h += "<tr><td style='text-align:center'>" + (corrige ? "<b>" + (i + 1) + "</b>" : "") +
               "</td><td>" + it.texte + "</td></tr>");
        h += "</table>";
        break;
      case "etiquettes":
        h += "<p><i>Étiquettes à placer : " +
             a.zones.map(z => z.etiquette).concat(a.intrus || []).join(" · ") + "</i></p>";
        if(corrige){
          h += "<table><tr><th>Repère</th><th>Étiquette</th></tr>";
          a.zones.forEach((z, i) => h += "<tr><td>" + (i + 1) + "</td><td><b>" + z.etiquette + "</b></td></tr>");
          h += "</table>";
        } else {
          h += "<p><i>Carte à projeter ou à photocopier depuis l'application.</i></p>";
        }
        break;
      case "tri":
        h += "<table><tr>" + a.paniers.map(p => "<th>" + p.titre + "</th>").join("") + "</tr><tr>";
        a.paniers.forEach(p => {
          h += "<td>" + (corrige
            ? a.items.filter(i => i.panier === p.id).map(i => "<b>" + i.texte + "</b>").join("<br>")
            : "<br><br><br><br>") + "</td>";
        });
        h += "</tr></table>";
        if(!corrige) h += "<p><i>À classer : " + a.items.map(i => i.texte).join(" · ") + "</i></p>";
        break;
      case "motscroises":
        h += "<ol>";
        a.mots.forEach(m => h += "<li>" + m.definition +
          (corrige ? " → <b>" + m.mot + "</b>" : " " + "…".repeat(Math.min(m.mot.length, 20))) + "</li>");
        h += "</ol>";
        break;
      case "motsmeles":
        h += "<table>";
        a.grille.forEach(l => h += "<tr>" + (Array.isArray(l) ? l : l.split(""))
          .map(c => "<td style='text-align:center;width:1.2em'>" + c + "</td>").join("") + "</tr>");
        h += "</table><p><i>Mots à trouver : " +
             (corrige ? "<b>" + a.mots.join(" · ") + "</b>" : a.mots.length + " métiers ou activités") + "</i></p>";
        break;
      case "anagramme":
        h += "<p>Lettres : <b>" + a.lettres.split("").join(" · ") + "</b> → " + R(a.solution) + "</p>";
        break;
      case "saisie":
        h += "<table><tr><th>Question</th><th style='width:26%'>Réponse</th></tr>";
        a.champs.forEach(c => h += "<tr><td>" + remplace(c.label, profil) + "</td><td>" +
          (corrige ? "<b>" + remplace(String(c.solution), profil) + (c.unite ? " " + c.unite : "") + "</b>"
                   : "") + "</td></tr>");
        h += "</table>";
        break;
      case "repartition":
        h += "<table><tr>" + a.categories.map(c => "<th>" + c.titre + "</th>").join("") +
             "</tr><tr>" + a.categories.map(() => "<td style='height:16mm'></td>").join("") + "</tr></table>";
        h += "<p><i>Répartis " + a.total + " " + (a.unite || "jetons") +
             ". Il n'y a pas de bonne réponse : le choix se justifie à l'oral.</i></p>";
        break;
      case "tableau":
        h += "<table><tr><th>" + (a.entete || "") + "</th>" +
             a.colonnes.map(c => "<th>" + c.titre + "</th>").join("") + "</tr>";
        a.lignes.forEach(li => {
          h += "<tr><td>" + li.titre + "</td>" +
               li.solutions.map(sol => "<td>" + (corrige ? "<b>" + sol + "</b>" : "") + "</td>").join("") +
               "</tr>";
        });
        h += "</table>";
        break;
      case "diagramme":
        h += "<table><tr><th>Part</th><th>Usage</th></tr>";
        a.secteurs.forEach(s2 => h += "<tr><td style='text-align:center'>" + s2.pourcentage +
          " %</td><td>" + (corrige ? "<b>" + s2.label + "</b>" : "") + "</td></tr>");
        h += "</table>";
        break;
      case "ouverte":
        h += '<span class="ligne-reponse"></span><span class="ligne-reponse"></span>' +
             '<span class="ligne-reponse"></span>';
        if(corrige && a.pistes){
          h += '<div class="encadre"><b>Pistes attendues :</b><ul>';
          a.pistes.forEach(p => h += "<li>" + p + "</li>");
          h += "</ul></div>";
        }
        break;
      default:
        h += "<p><i>Activité interactive : à faire sur l'application.</i></p>";
    }
    return h;
  }

  /* ---------------- Progression annuelle ---------------- */
  function progression(){
    let h = '<section class="feuille">';
    h += cartouche("Progression annuelle", true);
    h += "<h1>Mission géographique — Année A</h1>";
    h += "<p>16 séances réparties sur les cinq périodes, une par élément du programme. " +
         "Chaque séance réussie dépose un indice dans le carnet ; les 16 indices ouvrent la piste finale.</p>";
    h += "<table><tr><th>P.</th><th>Séance</th><th>Élément du programme</th>" +
         "<th>Leçon</th><th>Indice</th><th>Livret</th></tr>";
    MISSION.ordre().forEach(s => {
      const l = MISSION.lecons[s.lecon];
      h += "<tr><td style='text-align:center'>" + s.periode + "</td>" +
           "<td><b>" + s.numero + ".</b> " + s.titre + "</td>" +
           "<td>" + s.element + "</td>" +
           "<td>" + (l ? l.titre : "—") + "</td>" +
           "<td>" + decrireIndice(s) + "</td>" +
           "<td style='text-align:center'>p. " + s.livret + "</td></tr>";
    });
    h += "</table>";

    const F = MISSION.final;
    h += "<h2>Solutions de la piste finale</h2><ul>";
    h += "<li><b>Pays :</b> " + F.pays.propositions.find(p => p.id === F.pays.solution).nom + "</li>";
    F.carte.calculs.forEach(c => {
      h += "<li><b>" + c.titre + " :</b> " + CARNET.ecrireCalcul(c.termes) + " = " +
           (CARNET.calculer(c.termes) === null ? "(indices manquants)" : CARNET.calculer(c.termes)) + "</li>";
    });
    h += "<li><b>Code du cadenas :</b> " + CARNET.ecrireCalcul(F.cadenas.termes) + " = " +
         (CARNET.calculer(F.cadenas.termes) === null ? "(indices manquants)" : CARNET.calculer(F.cadenas.termes)) + "</li>";
    h += "<li><b>Cachette :</b> " + F.carte.lieu + "</li></ul>";
    h += '<p class="encadre"><i>Les valeurs sont calculées à partir des indices déjà récoltés. ' +
         "Pour obtenir la table complète, activez l'ordre libre et jouez les 16 séances, " +
         "ou consultez la table des indices ci-dessous.</i></p>";

    h += "<h2>Table des indices</h2><table><tr><th>Séance</th><th>Symbole</th><th>Valeur ou fait</th></tr>";
    MISSION.ordre().forEach(s => {
      const i = s.indice;
      const g = i.type === "nombre" ? (MISSION.final.symboles[i.symbole] || {}).glyphe : "🗒️";
      h += "<tr><td>" + s.numero + ". " + s.titre + "</td><td style='text-align:center'>" + g +
           "</td><td>" + (i.type === "nombre" ? "<b>" + i.valeur + "</b> — " + i.libelle : i.texte) +
           "</td></tr>";
    });
    h += "</table>";
    h += pied("Progression annuelle");
    h += "</section>";
    imprimer(h);
  }

  /* ---------------- Bilan de mission ---------------- */
  function bilan(){
    const etat = SAUVEGARDE.lire();
    let h = '<section class="feuille">';
    h += cartouche("Bilan de la mission", false);
    h += "<h1>Bilan de mission — " + (etat.equipe || "") + "</h1>";
    h += "<table><tr><th>Séance</th><th>Réussie</th><th>Points</th><th>Durée</th><th>Date</th></tr>";
    MISSION.ordre().forEach(s => {
      const r = etat.sessions[s.id];
      h += "<tr><td>" + s.numero + ". " + s.titre + "</td>" +
           "<td style='text-align:center'>" + (r && r.reussie ? "✔" : "—") + "</td>" +
           "<td style='text-align:center'>" + (r ? r.points + " / " + (r.maximum || "") : "—") + "</td>" +
           "<td style='text-align:center'>" + (r && r.duree ? Math.round(r.duree / 60) + " min" : "—") + "</td>" +
           "<td style='text-align:center'>" + (r && r.date ? new Date(r.date).toLocaleDateString("fr-FR") : "—") +
           "</td></tr>";
    });
    h += "</table>";
    h += "<p><b>Total :</b> " + SAUVEGARDE.pointsTotaux() + " points · " +
         SAUVEGARDE.reussies() + " séance(s) sur " + MISSION.sessions.length + ".</p>";
    h += pied("Bilan de mission");
    h += "</section>";
    imprimer(h);
  }

  /* ---------------- Diplôme ---------------- */
  function diplome(){
    const etat = SAUVEGARDE.lire();
    let h = '<section class="feuille" style="text-align:center">';
    h += "<h1 style='border:none;font-size:26pt;margin-top:30mm'>Diplôme d'agent géographe</h1>";
    h += "<p style='font-size:14pt'>décerné à</p>";
    h += "<p style='font-size:22pt'><b>" + (etat.equipe || "………………………………") + "</b></p>";
    h += "<p style='font-size:13pt'>pour avoir mené à bien la <b>Mission géographique — Année A</b>,<br>" +
         "réuni les " + etat.indices.length + " indices, identifié le pays recherché<br>" +
         "et retrouvé la valise " + MISSION.final.carte.lieu + ".</p>";
    h += "<p style='font-size:12pt'>Total : <b>" + SAUVEGARDE.pointsTotaux() + " points</b> · " +
         SAUVEGARDE.reussies() + " séances sur " + MISSION.sessions.length + "</p>";
    h += "<p style='margin-top:24mm'>Fait le " + jour() + "</p>";
    h += "<p style='margin-top:14mm'><i>Le Professeur Atlas<br>" +
         "Bureau Mondial de Surveillance Géographique</i></p>";
    h += "</section>";
    imprimer(h);
  }

  /* ---------------- Outils ---------------- */
  function decrireIndice(s){
    const i = s.indice;
    if(!i) return "—";
    if(i.type === "nombre"){
      const g = (MISSION.final.symboles[i.symbole] || {}).glyphe || "◇";
      return g + " = " + i.valeur;
    }
    return "« " + i.texte + " »";
  }

  function libelleType(t){
    return ({
      qcm:"QCM", vraifaux:"vrai/faux", trous:"texte à trous", relier:"appariement",
      ordre:"remise en ordre", etiquettes:"carte à légender", tri:"classement",
      motscroises:"mots croisés", motsmeles:"mots mêlés", anagramme:"anagramme",
      saisie:"calcul ou réponse courte", repartition:"répartition à justifier",
      tableau:"tableau à compléter", diagramme:"diagramme circulaire", ouverte:"réponse rédigée"
    })[t] || t;
  }

  function texteSimple(x){ return String(x == null ? "" : x).replace(/<[^>]+>/g, ""); }
  function remplace(x, profil){
    return String(x == null ? "" : x)
      .replace(/\{\{profil\.(\w+)\}\}/g, (t, c) => profil[c] !== undefined ? profil[c] : t);
  }

  function mediasAttendus(s){
    const noms = [];
    const pousser = m => { if(m && m.base) noms.push(m.base); };
    pousser(s.intro && s.intro.media);
    pousser(s.mediaCoeur);
    pousser(s.fin && s.fin.media);
    s.activites.forEach(a => { pousser(a.media); if(a.fond) pousser(a.fond); });
    const l = MISSION.lecons[s.lecon];
    if(l) pousser(l.media);
    return [...new Set(noms)];
  }

  return { lecon, preparation, ficheEleve, progression, bilan, diplome, mediasAttendus };
})();
