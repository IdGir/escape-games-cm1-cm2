# -*- coding: utf-8 -*-
"""Installe le moteur d'énigmes v2 et le nouveau déroulé dans les jeux à moteur commun.

    python outils-moteur/installer.py            (les 6 jeux)
    python outils-moteur/installer.py melanges   (un seul)

Règles v2 :
  - énigme juste du premier coup : PTS_PREMIER_COUP (10) ; après erreur : PTS_APRES_ERREUR (3) ;
  - après une erreur, seul le NOMBRE de réponses justes est donné ;
  - plus de texte après la résolution (correction, explication, dialogue de réussite) ;
  - le mot de chaque salle s'affiche UNE fois (« Notez-le ! ») puis disparaît ;
  - avant la fin, le coffre final demande de retaper les mots notés ;
  - aucun dialogue ne bloque le passage à la salle suivante.
Idempotent : un fichier déjà converti n'est pas modifié une seconde fois.
"""
import os
import re
import sys

# Depuis le tronc commun (amélioration A3, octobre 2026), le moteur n'existe plus qu'en UN
# exemplaire dans commun/js/ : ce script d'installation du moteur v2 a déjà été appliqué et
# recopierait des fichiers devenus inutiles dans les jeux. Il est conservé pour mémoire.
if os.path.exists(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "commun", "js", "enigmes.js")):
    print("Moteur v2 déjà installé. Depuis le tronc commun, corrigez directement commun/js/ (voir commun/README.md).")
    sys.exit(0)

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
JEUX = ["melanges", "chateau-fort", "moyen-age-abbaye", "station-meteo", "objets-techniques", "constitution"]
MARQUE = "PTS_PREMIER_COUP"


def lire(p):
    return open(p, encoding="utf-8").read()


def ecrire(p, s):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(s)


def fonction(src, nom):
    """(début, fin) d'une fonction de premier niveau « function nom(...){ … } »."""
    m = re.search(r"^(async )?function " + re.escape(nom) + r"\(", src, re.M)
    if not m:
        raise KeyError(nom)
    fin = src.index("\n}\n", m.start()) + 3
    return m.start(), fin


def remplacer_fonction(src, nom, nouveau):
    a, b = fonction(src, nom)
    return src[:a] + nouveau.rstrip() + "\n" + src[b:]


# ------------------------------------------------------------------ enigmes.js
def installer_moteur(jeu):
    p = os.path.join(RACINE, jeu, "js", "enigmes.js")
    ancien = lire(p)
    if "version 2, octobre 2026" in ancien:
        return
    nouveau = lire(os.path.join(ICI, "enigmes.js"))
    if jeu == "constitution":
        nouveau = nouveau.replace('const LIBELLE_BOUTON_LECON = "📚 Leçon";', 'const LIBELLE_BOUTON_LECON = "📚 Fiche source";')
        nouveau = nouveau.replace('const TITRE_BOUTON_LECON = "Ouvrir la leçon liée à cette énigme";',
                                  'const TITRE_BOUTON_LECON = "Ouvrir le document officiel dont vient cette énigme";')
    if jeu == "station-meteo":
        nouveau = greffer_instrument(ancien, nouveau)
    ecrire(p, nouveau)
    css = os.path.join(RACINE, jeu, "css", "enigmes.css")
    c = lire(css)
    if "Moteur d'énigmes v2" in c:      # remplace le bloc v2 déjà présent (toujours en fin de fichier)
        c = c[:c.index("/* ==== Moteur d'énigmes v2")]
    ecrire(css, c.rstrip() + "\n\n" + lire(os.path.join(ICI, "enigmes-v2.css")))


def greffer_instrument(ancien, nouveau):
    """Reprend le type « instrument » propre à la Station météo et l'adapte au contrat v2."""
    debut = ancien.index("/* ============================================================\n   TYPE 11")
    fin = ancien.index("/* ============================================================\n   BRANCHEMENT")
    bloc = ancien[debut:fin]
    bloc = bloc.replace("function activerInstrument(e, d, reussir, rater){",
                        "function activerInstrument(e, d, api){\n  const reussir = api.reussir;")
    # messages : incomplets / erreurs comptées sans montrer lesquelles
    bloc = re.sub(r"rater\(`\$\{justes\}([^`]*)`\)", lambda m: "api.erreur(justes, items.length, null, `${justes}" + m.group(1) + "`)", bloc)
    bloc = re.sub(r"rater\(", "api.incomplet(", bloc)
    bloc = re.sub(r'\n[^\n]*classList\.toggle\("(bien|mal)"[^\n]*', "", bloc)
    nouveau = nouveau.replace("  code: corpsCode, intrus: corpsIntrus, plan: corpsPlan\n};",
                              "  code: corpsCode, intrus: corpsIntrus, plan: corpsPlan, instrument: corpsInstrument\n};")
    nouveau = nouveau.replace("  code: activerCode, intrus: activerIntrus, plan: activerPlan\n};",
                              "  code: activerCode, intrus: activerIntrus, plan: activerPlan,\n  instrument: activerInstrument\n};")
    nouveau = nouveau.replace("     plan         placer des étiquettes sur les cases d'un schéma\n",
                              "     plan         placer des étiquettes sur les cases d'un schéma\n"
                              "     instrument   lire ou régler un instrument gradué (propre à ce jeu)\n")
    i = nouveau.index("/* ============================================================\n   BRANCHEMENT")
    return nouveau[:i] + bloc + nouveau[i:]


# ------------------------------------------------------------------ app.js
REUSSIR_ENIGME = '''function reussirEnigme(e, liste, indices, erreurs){
  ETAT.enigmesReussies++;
  const premierCoup = !erreurs;
  if(premierCoup) ETAT.enigmesPremierCoup = (ETAT.enigmesPremierCoup || 0) + 1;
  ajouterScore(premierCoup ? PTS_PREMIER_COUP : PTS_APRES_ERREUR, premierCoup ? "tout juste du premier coup 🎯" : "énigme résolue");
  confettis(premierCoup ? 40 : 12);
  ETAT.enigme++;
  sauvegarder();
  if(ETAT.enigme >= liste.length){
    setTimeout(()=>validerSalle(ETAT.salle), 700);
  }else{
    const zone = document.getElementById("zone-enigme");
    const suite = document.createElement("div");
    suite.className = "boutons";
    suite.innerHTML = `<button class="btn grand bleu" id="btn-enigme-suivante">➡️ Énigme suivante (${ETAT.enigme+1}/${liste.length})</button>`;
    zone.appendChild(suite);
    suite.querySelector("button").addEventListener("click", afficherEnigmeCourante);
    suite.scrollIntoView({behavior:"smooth", block:"center"});
  }
}

/* Une vérification fausse (compteur pour le bilan et le tableau de bord). */
function compterErreur(){
  ETAT.erreursTotal = (ETAT.erreursTotal || 0) + 1;
  sauvegarder();
}
'''

COFFRE = '''/* ============================================================
   LE COFFRE FINAL — les élèves retapent les mots notés sur leur
   fiche de mission, salle par salle. Rien n'est rempli pour eux.
   ============================================================ */
function afficherCoffre(suite){
  if(ETAT.coffreOuvert){ suite(); return; }
  const zone = document.getElementById("zone-enigme") || document.getElementById("salle-contenu");
  const dlg = document.querySelector("#salle-contenu .personnage-scene");
  if(dlg) dlg.remove();
  let erreurs = 0;
  zone.innerHTML = `
    <div class="enigme-carte coffre-final" id="coffre-final">
      <div class="enigme-tete"><span class="enigme-num">Énigme finale</span><h3>🔐 Le coffre final</h3></div>
      <div class="bandeau-bareme">🎯 Tout juste du premier coup : <b>${PTS_COFFRE_PREMIER} points</b> · après une erreur : ${PTS_COFFRE_APRES} points seulement</div>
      <div class="consigne">Recopiez, salle par salle, les mots que vous avez notés sur votre fiche de mission. Les accents et les majuscules ne comptent pas.</div>
      ${DONNEES.salles.map((s,i)=>`<div class="coffre-ligne">
        <label for="coffre-${i}">Salle ${s.num} — ${s.titre}</label>
        <input type="text" id="coffre-${i}" autocomplete="off" spellcheck="false" maxlength="24">
      </div>`).join("")}
      <div class="feedback" id="fb-coffre"></div>
      <div class="center"><button class="btn grand vert" id="btn-coffre">🔓 Ouvrir le coffre</button></div>
    </div>`;
  const fb = document.getElementById("fb-coffre");
  const valider = ()=>{
    const champs = DONNEES.salles.map((s,i)=>document.getElementById("coffre-"+i));
    if(champs.some(c=>!c.value.trim())){
      fb.className = "feedback indice show"; fb.innerHTML = "✋ Il manque au moins un mot."; return;
    }
    const justes = DONNEES.salles.filter((s,i)=>normaliser(champs[i].value) === normaliser(s.motCle)).length;
    if(justes === DONNEES.salles.length){
      ETAT.coffreOuvert = true;
      champs.forEach(c=>c.disabled = true);
      document.getElementById("btn-coffre").disabled = true;
      ajouterScore(erreurs ? PTS_COFFRE_APRES : PTS_COFFRE_PREMIER, erreurs ? "coffre ouvert" : "coffre ouvert du premier coup 🎯");
      if(!erreurs) ETAT.coffrePremierCoup = true;
      fb.className = "feedback succes" + (erreurs ? "" : " premier-coup") + " show";
      fb.innerHTML = erreurs ? `✔ Le coffre s'ouvre : +${PTS_COFFRE_APRES} points.` : `🎯 <b>Tout juste du premier coup !</b> +${PTS_COFFRE_PREMIER} points`;
      if(typeof son === "function") son("deverrouille");
      confettis(60);
      sauvegarder();
      setTimeout(suite, 900);
    }else{
      erreurs++;
      if(typeof compterErreur === "function") compterErreur();
      if(typeof son === "function") son("erreur");
      fb.className = "feedback erreur show";
      fb.innerHTML = `✗ <b>Le coffre reste fermé.</b> ${justes} mot${justes>1?"s":""} juste${justes>1?"s":""} sur ${DONNEES.salles.length}.`
        + (erreurs === 1 ? `<div class="perte-bonus">Le bonus du premier coup est perdu : vérifiez votre fiche de mission.</div>` : "");
    }
  };
  document.getElementById("btn-coffre").addEventListener("click", valider);
  zone.querySelectorAll("input").forEach(inp=>inp.addEventListener("keydown", ev=>{ if(ev.key === "Enter") valider(); }));
  zone.scrollIntoView({behavior:"smooth", block:"start"});
}
'''


def patch_app(jeu):
    p = os.path.join(RACINE, jeu, "js", "app.js")
    s = lire(p)
    if MARQUE in s:
        return
    # 1. barème
    s = re.sub(r"const PTS_ENIGME\s*=\s*5;[^\n]*",
               "const PTS_PREMIER_COUP   = 10;   // énigme juste du premier coup\n"
               "const PTS_APRES_ERREUR   = 3;    // énigme résolue après une ou plusieurs erreurs\n"
               "const PTS_COFFRE_PREMIER = 10;   // coffre final ouvert du premier coup\n"
               "const PTS_COFFRE_APRES   = 3;    // coffre final ouvert après erreur\n"
               "const PTS_ENIGME = PTS_PREMIER_COUP;   // (compatibilité)", s, count=1)
    s = s.replace("return nbEnigmesTotal()*PTS_ENIGME + NB_SALLES*PTS_RAPIDITE + NB_QUIZ*PTS_QUIZ;",
                  "return nbEnigmesTotal()*PTS_PREMIER_COUP + PTS_COFFRE_PREMIER + NB_SALLES*PTS_RAPIDITE + NB_QUIZ*PTS_QUIZ;")
    # 2. énigme réussie
    s = remplacer_fonction(s, "reussirEnigme", REUSSIR_ENIGME)
    s = s.replace("activerEnigme(e, ()=>reussirEnigme(e, liste));",
                  "activerEnigme(e, (en, indices, erreurs)=>reussirEnigme(e, liste, indices, erreurs));")
    # 3. salle bouclée
    a, b = fonction(s, "validerSalle")
    v = s[a:b]
    # 3a. le mot, une seule fois, à noter ; plus de serrures détaillées ni de statistiques
    v = re.sub(r'(<div class="val">\$\{salle\.motCle\}</div>)',
               r'\1\n      <div class="a-noter">✍️ Notez ce mot sur votre fiche de mission : il ne sera plus affiché !</div>', v)
    v = re.sub(r"\n\s*\$\{serruresHTML\(\)\}", "", v)
    v = re.sub(r'\n\s*<p class="center"[^\n]*\n[^\n]*indicesSalle[^\n]*</p>', "", v)
    # 3b. dernière salle : le coffre final avant la suite prévue
    m = re.search(r"  if\(n === NB_SALLES\)\{\n    (setTimeout\(.*?\);)\n    return;\n  \}", v, re.S)
    if not m:
        raise RuntimeError(jeu + " : fin de validerSalle introuvable")
    appel = m.group(1)
    v = v.replace(m.group(0), "  if(n === NB_SALLES){\n    ajouterBoutonCoffre(()=>" + appel.rstrip(";") + ");\n    return;\n  }")
    # 3c. plus de dialogue de réussite bloquant : le bouton « Salle suivante » arrive tout de suite
    m = re.search(r"  const filet = setTimeout\(boutonSuivant, \d+\);.*?\n  \}\);\n", v, re.S)
    if not m:
        raise RuntimeError(jeu + " : dialogue de réussite introuvable")
    v = v.replace(m.group(0), "  boutonSuivant();\n")
    s = s[:a] + v + s[b:]
    # 4. coffre final + bouton d'accès
    s = s.replace("/* ---- Badges ---- */", COFFRE + '''
function ajouterBoutonCoffre(suite){
  const zone = document.getElementById("zone-enigme");
  const b = document.createElement("div");
  b.className = "boutons";
  b.innerHTML = `<button class="btn grand vert" id="btn-coffre-final">🔐 Aller au coffre final</button>`;
  zone.appendChild(b);
  b.querySelector("button").addEventListener("click", ()=>afficherCoffre(suite));
  b.scrollIntoView({behavior:"smooth", block:"center"});
}

/* ---- Badges ---- */''', 1)
    if "function afficherCoffre" not in s:
        raise RuntimeError(jeu + " : ancre Badges introuvable")
    # 5. les serrures n'affichent les mots qu'une fois le coffre ouvert
    a, b = fonction(s, "serruresHTML")
    f = s[a:b].replace("const ouverte = ETAT.motsCles.includes(s.motCle);",
                       "const ouverte = ETAT.motsCles.includes(s.motCle);\n    const lisible = ouverte && ETAT.coffreOuvert;")
    f = re.sub(r"\$\{ouverte\?s\.motCle:", "${lisible?s.motCle:ouverte?\"🔓 trouvé\":", f)
    s = s[:a] + f + s[b:]
    # 6. plus de dialogue après la fin
    s = s.replace("const fin = DONNEES.salles[NB_SALLES-1].dialogue_fin;",
                  "const fin = null;   // v2 : aucun texte après la résolution")
    # 7. état, reprise, vérification, bilan
    s = s.replace("    equipe:\"\", niveau:\"CM2\", salle:1, enigme:0, score:0, motsCles:[],",
                  "    equipe:\"\", niveau:\"CM2\", salle:1, enigme:0, score:0, motsCles:[],\n"
                  "    enigmesPremierCoup:0, erreursTotal:0, coffreOuvert:false, coffrePremierCoup:false,", 1)
    s = s.replace("tempsParSalle:partie.tempsParSalle||{}, fini:false",
                  "tempsParSalle:partie.tempsParSalle||{}, fini:false,\n"
                  "        enigmesPremierCoup:partie.enigmesPremierCoup||0, erreursTotal:partie.erreursTotal||0,\n"
                  "        coffreOuvert:!!partie.coffreOuvert, coffrePremierCoup:!!partie.coffrePremierCoup", 1)
    s = s.replace("      ETAT.motsCles = DONNEES.salles.map(s=>s.motCle);\n      ETAT.enigmesReussies = nbEnigmesTotal();",
                  "      ETAT.motsCles = DONNEES.salles.map(s=>s.motCle);\n      ETAT.coffreOuvert = true;\n      ETAT.enigmesReussies = nbEnigmesTotal();", 1)
    s = re.sub(r"(      <div>🧩 Énigmes : <b>\$\{ETAT\.enigmesReussies\}/\$\{nbEnigmesTotal\(\)\}</b></div>)",
               r"\1\n      <div>🎯 Justes du premier coup : <b>${ETAT.enigmesPremierCoup||0}/${nbEnigmesTotal()}</b> · ✗ Erreurs : <b>${ETAT.erreursTotal||0}</b></div>", s, count=1)
    ecrire(p, s)


def verifier_etat(jeu):
    """Le champ ETAT doit connaître les nouveaux compteurs (déclaration initiale)."""
    p = os.path.join(RACINE, jeu, "js", "app.js")
    s = lire(p)
    if "  enigmesPremierCoup:" not in s.split("function")[0]:
        s = re.sub(r"(  motsCles: \[\],[^\n]*\n)", r"\1  enigmesPremierCoup: 0, erreursTotal: 0, coffreOuvert: false, coffrePremierCoup: false,\n", s, count=1)
        ecrire(p, s)


def installer_fiche_mission(jeu):
    """Fiche de mission A4 (impression) + bouton dans ⚙️ Réglages + versions des fichiers."""
    import shutil
    d = os.path.join(RACINE, jeu)
    shutil.copyfile(os.path.join(RACINE, "outils-moteur", "fiche-mission.js"), os.path.join(d, "js", "fiche-mission.js"))
    # index.html : script + numéros de version (cache du navigateur / GitHub Pages)
    p = os.path.join(d, "index.html")
    s = lire(p)
    if "js/fiche-mission.js" not in s:
        s = re.sub(r'(<script src="js/impression\.js[^"]*"></script>)', r'\1\n<script src="js/fiche-mission.js?m2"></script>', s, count=1)
    for f in ("css/enigmes.css", "js/enigmes.js", "js/app.js", "js/reglages.js", "js/impression.js"):
        s = re.sub(r'(%s)\?[^"]*"' % re.escape(f), r'\1?m2"', s)
    ecrire(p, s)
    # reglages.js : bouton « Fiche de mission »
    p = os.path.join(d, "js", "reglages.js")
    s = lire(p)
    if "btn-imprimer-mission" not in s:
        s = s.replace('<button class="btn or" id="btn-imprimer-tout">',
                      '<button class="btn vert" id="btn-imprimer-mission">✍️ Fiche de mission (1 par équipe)</button>\n'
                      '        <button class="btn or" id="btn-imprimer-tout">', 1)
        s = s.replace('  corps.querySelector("#btn-imprimer-tout").addEventListener(',
                      '  corps.querySelector("#btn-imprimer-mission").addEventListener("click", ()=>imprimerFicheMission());\n'
                      '  corps.querySelector("#btn-imprimer-tout").addEventListener(', 1)
        if "btn-imprimer-mission\").addEventListener" not in s:
            raise RuntimeError(jeu + " : bouton fiche de mission non branché")
        ecrire(p, s)
    # app.js : les anciennes sauvegardes (ancien barème) ne sont plus reprises
    p = os.path.join(d, "js", "app.js")
    s = lire(p)
    s = s.replace('const VERSION_APP = "v1";', 'const VERSION_APP = "v2";   // v2 : barème du premier coup, coffre final')
    ecrire(p, s)


def taire_personnage(jeu):
    """Le personnage se tait dès que les élèves touchent l'énigme : la parole ne bloque jamais le jeu."""
    p = os.path.join(RACINE, jeu, "js", "app.js")
    s = lire(p)
    if "taire le personnage" in s:
        return
    ancre = "  zone.innerHTML = filEnigmes(liste.length) + enigmeHTML(e, ETAT.enigme+1, liste.length);\n"
    if ancre not in s:
        raise RuntimeError(jeu + " : ancre afficherEnigmeCourante introuvable")
    s = s.replace(ancre, ancre +
        "  // v2 : taire le personnage dès que les élèves commencent l'énigme (le chrono ne s'arrête jamais)\n"
        "  zone.addEventListener(\"pointerdown\", ()=>{ if(\"speechSynthesis\" in window) speechSynthesis.cancel(); }, {once:true});\n", 1)
    ecrire(p, s)


def corriger_doubles_points(jeu):
    """Le quizz ne rapporte ses points qu'une fois ; une salle reprise après
    rechargement ne redonne pas le bonus de rapidité."""
    p = os.path.join(RACINE, jeu, "js", "app.js")
    s = lire(p)
    a = 'document.getElementById("btn-voir-score").onclick = ()=>{\n'
    if a in s and "quizz déjà compté" not in s:
        s = s.replace(a, a + "    if(ETAT.quiz.repondu) return;   // quizz déjà compté : pas de points en double\n", 1)
    a = "  ETAT.tempsParSalle[n] = duree;\n"
    if a in s and "dejaValidee" not in s:
        s = s.replace(a, "  const dejaValidee = ETAT.tempsParSalle[n] !== undefined;   // reprise après rechargement\n" + a, 1)
        s = s.replace("  if(pts) ajouterScore(pts, raison);", "  if(pts && !dejaValidee) ajouterScore(pts, raison);", 1)
    ecrire(p, s)


if __name__ == "__main__":
    for jeu in (sys.argv[1:] or JEUX):
        installer_moteur(jeu)
        patch_app(jeu)
        verifier_etat(jeu)
        installer_fiche_mission(jeu)
        taire_personnage(jeu)
        corriger_doubles_points(jeu)
        print("moteur v2 :", jeu)
