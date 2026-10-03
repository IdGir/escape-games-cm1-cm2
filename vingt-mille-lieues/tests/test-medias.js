/* ============================================================
   TEST DU CONTRAT DE REMPLACEMENT DES MÉDIAS (§ 7.5)
   ------------------------------------------------------------
   Dépose un faux PNG sous le nom attendu (assets/images/decors/carre.png),
   vérifie qu'il est affiché à la place de l'image de référence, puis le
   supprime et vérifie le retour à la référence ; idem pour un portrait
   (assets/images/personnages/conseil.png) et une vidéo de cinématique
   (assets/videos/transition-e2.mp4). Les fichiers de test sont TOUJOURS
   supprimés (même en cas d'échec) : rien n'est laissé dans le dépôt.
   Dans jsdom, une image « se charge » si le fichier existe sur le disque.
   ============================================================ */
const path = require("path"), fs = require("fs");
const { charger, compteur, attendreQue, dodo } = require("../../outils-tests/charge");
const JEU = path.resolve(__dirname, "..");
const { ok, fin, exception } = compteur("Médias remplaçables");
const RACINE = path.resolve(JEU, "..");
const PNG = Buffer.from("iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAYAAAA7KqwyAAAAEklEQVR42mNk+M9Qz0AEYBxVSF8FAJ2fCAEsZXz/AAAAAElFTkSuQmCC", "base64");
const FAUX = [path.join(JEU, "assets/images/decors/carre.png"), path.join(JEU, "assets/images/personnages/conseil.png"), path.join(JEU, "assets/videos/transition-e2.mp4")];

/* Image() simulée : succès si le fichier existe, avec un format 16:9 */
const avant = w => {
  w.VML_RAPIDE = true;
  w.Image = class {
    set src(v){
      this._src = v;
      const f = path.join(RACINE, decodeURIComponent(new URL(v, w.location.href).pathname));
      /* les vrais fichiers déposés sont ignorés : on teste la cascade comme dans un dépôt neuf */
      const depose = /assets[\\/]images[\\/](decors|personnages)[\\/]/.test(f) && !FAUX.includes(f);
      setTimeout(() => { if(!depose && fs.existsSync(f)){ this.naturalWidth = 1600; this.naturalHeight = 900; this.onload && this.onload(); } else this.onerror && this.onerror(); }, 0);
    }
    get src(){ return this._src; }
  };
};

(async () => {
  try{
    FAUX.forEach(f => { if(fs.existsSync(f)) throw new Error("un vrai fichier existe déjà : " + f + " (test annulé pour ne pas l'écraser)"); });
    let r = await charger(JEU, "?verif=1&escale=2&niveau=matelot&enigme=1", { avant });
    await attendreQue(() => r.w.document.querySelector("#scene-jeu[data-source]"));
    ok(r.w.document.querySelector("#scene-jeu").dataset.source === "reference", "sans fichier déposé : image de référence de l'enseignant");
    r.w.close();

    fs.writeFileSync(FAUX[0], PNG); fs.writeFileSync(FAUX[1], PNG); fs.writeFileSync(FAUX[2], Buffer.from("faux mp4"));
    r = await charger(JEU, "?verif=1&escale=2&niveau=matelot&enigme=1", { avant });
    let d = r.w.document;
    await attendreQue(() => d.querySelector("#scene-jeu[data-source]"));
    ok(d.querySelector("#scene-jeu").dataset.source === "depose", "fichier déposé : il prime sur la référence");
    ok(/assets\/images\/decors\/carre\.png/.test(d.querySelector("#scene-jeu .sc-fond img").getAttribute("src")), "fichier déposé : c'est lui qui est affiché");
    const portraitOk = await attendreQue(() => d.querySelector('#plaque .portrait-ovale.fichier img[src*="personnages/conseil.png"]'));
    ok(portraitOk, "portrait déposé : il remplace le portrait dessiné");
    ok(await r.w.VML.sonderVideo("transition-e2") === "assets/videos/transition-e2.mp4", "vidéo déposée : trouvée pour la cinématique");
    ok(d.querySelectorAll("#scene-jeu .zone").length === 3, "zones cliquables conservées sur l'image déposée");
    r.w.close();

    FAUX.forEach(f => fs.unlinkSync(f));
    r = await charger(JEU, "?verif=1&escale=2&niveau=matelot&enigme=1", { avant });
    d = r.w.document;
    await attendreQue(() => d.querySelector("#scene-jeu[data-source]"));
    ok(d.querySelector("#scene-jeu").dataset.source === "reference", "fichier retiré : retour à la référence");
    ok(await r.w.VML.sonderVideo("transition-e2") === null, "vidéo retirée : cinématique en direct");
    r.w.close();
    r = await charger(JEU, "?verif=1&escale=2&niveau=matelot&enigme=1&reference=0", { avant });
    await attendreQue(() => r.w.document.querySelector("#scene-jeu[data-source]"));
    ok(r.w.document.querySelector("#scene-jeu").dataset.source === "secours", "sans référence : décor dessiné de secours");
    r.w.close();
    r = await charger(JEU, "?verif=1&escale=2&niveau=matelot&enigme=2", { avant });
    await attendreQue(() => r.w.document.querySelector("#scene-jeu[data-source]"));
    ok(r.w.document.querySelector("#scene-jeu").dataset.source === "secours", "salle des machines électrique (pas de référence) : décor dessiné");
    r.w.close();
    const csv = fs.readFileSync(path.join(JEU, "medias.csv"), "utf8");
    ["assets/images/decors/carre.webp", "assets/images/decors/machines.webp", "assets/images/personnages/nemo.webp", "assets/videos/transition-e2.mp4"].forEach(n => ok(csv.includes(n), "medias.csv liste " + n));
  }catch(e){ exception(e); }
  finally{ FAUX.forEach(f => { try{ if(fs.existsSync(f) && fs.statSync(f).size < 200) fs.unlinkSync(f); }catch(e){} }); }
  await dodo(10);
  fin();
})();
