/* ============================================================
   CORRESPONDANCE PASSEPORT → LSU (amélioration N24) — données publiques communes
   ------------------------------------------------------------
   Le passeport de compétences (C3) note, pour chaque élève, une compétence par leçon de chaque
   jeu (intitulés internes, ceux de lecons-a4.json). Le LSU (Livret Scolaire Unique) utilise ses
   propres intitulés : les ÉLÉMENTS DE PROGRAMME et les COMPÉTENCES du cycle 3. Cette table fait
   correspondre chaque leçon du passeport à l'intitulé LSU le plus proche.

   S'appuie sur la correspondance du bandeau BO (C2) : la discipline LSU découle des programmes
   officiels déjà rattachés à chaque jeu dans commun/donnees/catalogue.js (jeu.programme →
   hg2026 / st2026 / emc2024 → « disciplines » ci-dessous). Pour une leçon que cette table ne
   connaît pas encore (nouveau jeu), l'export retombe sur la discipline du bandeau BO et
   signale « à rattacher dans votre LSU » : rien n'est inventé.

   « correspondance » : { "<dossier du jeu>": { "<clé de la leçon dans lecons-a4.json>": [intitulé, exactitude] } }
     exactitude "=" : intitulé LSU qui recouvre la leçon ;
                 "~" : intitulé le plus proche, à confirmer par l'enseignant.
   Un jeu ou une leçon ajoutée : ajouter sa ligne ici (le test commun/tests/test-pages.js N24 échoue
   tant qu'une leçon du passeport n'a pas de ligne).

   LIBELLÉS : listes de référence du LSU pour le cycle 3 (éléments de programme d'histoire et
   géographie, d'EMC, de sciences et technologie ; compétences associées), relevées sur les aides
   à la saisie académiques du LSU. Le LSU se paramètre par école et suit les programmes : un
   intitulé peut différer légèrement dans votre établissement (programmes 2026 compris). Les corriger
   ici, une seule fois, suffit pour tous les exports.
   Fichier .js (et non .json) pour fonctionner aussi en double-clic.
   ============================================================ */
var LSU = {
 "version": "2026-11",
 "avertissement": "Aide à la saisie, pas une validation : les niveaux sont des suggestions calculées d'après le passeport. L'enseignant garde la main : c'est lui qui saisit et valide dans le LSU, après avoir vérifié chaque intitulé (ils peuvent différer légèrement selon l'établissement).",
 "disciplines": {
  "hg2026": "Histoire et géographie",
  "st2026": "Sciences et technologie",
  "emc2024": "Enseignement moral et civique"
 },
 "niveaux": {
  "N": "Objectifs non atteints",
  "E": "Objectifs partiellement atteints",
  "A": "Objectifs atteints"
 },
 "items": {
  "hg-avant": { "discipline": "Histoire et géographie", "type": "Élément de programme", "libelle": "Et avant la France ?" },
  "hg-rois": { "discipline": "Histoire et géographie", "type": "Élément de programme", "libelle": "Le temps des rois" },
  "hg-revol": { "discipline": "Histoire et géographie", "type": "Élément de programme", "libelle": "Le temps de la Révolution et de l'Empire" },
  "hg-lieux": { "discipline": "Histoire et géographie", "type": "Élément de programme", "libelle": "Découvrir le(s) lieu(x) où j'habite" },
  "hg-loger": { "discipline": "Histoire et géographie", "type": "Élément de programme", "libelle": "Se loger, travailler, se cultiver, avoir des loisirs en France" },
  "hg-consommer": { "discipline": "Histoire et géographie", "type": "Élément de programme", "libelle": "Consommer en France" },
  "hg-deplacer": { "discipline": "Histoire et géographie", "type": "Élément de programme", "libelle": "Se déplacer" },
  "hg-periodes": { "discipline": "Histoire et géographie", "type": "Compétence", "libelle": "Situer des grandes périodes historiques" },
  "hg-localiser": { "discipline": "Histoire et géographie", "type": "Compétence", "libelle": "Nommer et localiser les grands repères géographiques" },
  "hg-echelle": { "discipline": "Histoire et géographie", "type": "Compétence", "libelle": "Appréhender la notion d'échelle géographique" },
  "emc-droits": { "discipline": "Enseignement moral et civique", "type": "Élément de programme", "libelle": "Les droits et les devoirs de l'élève, du citoyen" },
  "emc-principes": { "discipline": "Enseignement moral et civique", "type": "Élément de programme", "libelle": "Les principes et les valeurs de la République française" },
  "sc-matiere": { "discipline": "Sciences et technologie", "type": "Élément de programme", "libelle": "Matière, mouvement, énergie, information : décrire les états et la constitution de la matière à l'échelle macroscopique" },
  "sc-energie": { "discipline": "Sciences et technologie", "type": "Élément de programme", "libelle": "Matière, mouvement, énergie, information : identifier différentes sources d'énergie" },
  "sc-signal": { "discipline": "Sciences et technologie", "type": "Élément de programme", "libelle": "Matière, mouvement, énergie, information : identifier un signal et une information" },
  "sc-vivant": { "discipline": "Sciences et technologie", "type": "Élément de programme", "libelle": "Le vivant, sa diversité et les fonctions qui le caractérisent" },
  "sc-objets": { "discipline": "Sciences et technologie", "type": "Élément de programme", "libelle": "Matériaux et objets techniques" },
  "sc-terre": { "discipline": "Sciences et technologie", "type": "Élément de programme", "libelle": "La planète Terre. Les êtres vivants dans leur environnement" },
  "sc-outils": { "discipline": "Sciences et technologie", "type": "Compétence", "libelle": "S'approprier des outils et des méthodes" },
  "sc-langages": { "discipline": "Sciences et technologie", "type": "Compétence", "libelle": "Pratiquer des langages" }
 },
 "correspondance": {
  "moyen-age-abbaye": {
   "clovis": ["hg-avant", "="], "charlemagne": ["hg-avant", "="],
   "scriptorium": ["hg-rois", "~"], "hotel-dieu": ["hg-rois", "~"], "roman-gothique": ["hg-rois", "~"]
  },
  "chateau-fort": {
   "construire-un-chateau": ["hg-rois", "~"], "les-defenses": ["hg-rois", "~"], "vie-du-seigneur": ["hg-rois", "~"],
   "vie-des-paysans": ["hg-rois", "~"], "seigneur-et-paysans": ["hg-rois", "~"]
  },
  "versailles": {
   "reforme-guerres": ["hg-rois", "="], "edit-de-nantes": ["hg-rois", "="], "chateau-versailles": ["hg-rois", "="],
   "journee-du-roi": ["hg-rois", "="], "monarchie-absolue": ["hg-rois", "="]
  },
  "renaissance": {
   "renaissance-humanisme": ["hg-rois", "="], "francois-mecene": ["hg-rois", "="], "leonard-de-vinci": ["hg-rois", "="],
   "chateaux-renaissance": ["hg-rois", "="], "art-renaissance": ["hg-rois", "="]
  },
  "declaration": {
   "causes": ["hg-revol", "="], "etats-generaux": ["hg-revol", "="], "bastille": ["hg-revol", "="], "declaration": ["hg-revol", "="],
   "personnages": ["hg-revol", "="], "devise": ["hg-revol", "="], "femmes": ["hg-revol", "="], "paris": ["hg-localiser", "~"]
  },
  "constitution": {
   "regles": ["emc-droits", "~"], "textes": ["emc-principes", "="], "peuple": ["emc-principes", "~"],
   "loi": ["emc-principes", "~"], "gardien": ["emc-principes", "="]
  },
  "mission-geo": {
   "l01": ["hg-lieux", "="], "l02": ["hg-lieux", "="], "l03": ["hg-loger", "="], "l04": ["hg-loger", "="], "l05": ["hg-loger", "="],
   "l06": ["hg-loger", "~"], "l07": ["hg-loger", "~"], "l08": ["hg-consommer", "~"], "l09": ["hg-consommer", "="], "l10": ["hg-consommer", "="],
   "l11": ["hg-consommer", "="], "l12": ["hg-consommer", "="], "l13": ["hg-localiser", "~"], "l14": ["hg-localiser", "~"],
   "l15": ["hg-consommer", "~"], "l16": ["hg-consommer", "~"]
  },
  "tour-du-monde": {
   "planisphere": ["hg-localiser", "="], "orientation": ["hg-localiser", "="], "carte": ["hg-echelle", "="],
   "climats": ["hg-localiser", "="], "deplacer": ["hg-deplacer", "="], "fuseaux": ["hg-localiser", "="]
  },
  "etats-matiere": {
   "etats": ["sc-matiere", "="], "air": ["sc-matiere", "="], "changements": ["sc-matiere", "="], "conservation": ["sc-matiere", "="], "proprietes": ["sc-matiere", "="]
  },
  "mouvement": {
   "distance": ["sc-matiere", "="], "duree": ["sc-matiere", "="], "comparer": ["sc-matiere", "="], "trajectoires": ["sc-matiere", "="], "observateur": ["sc-terre", "~"]
  },
  "traite-colonies": {
   "triangle": ["hg-rois", "~"], "traite": ["hg-rois", "~"], "plantations": ["hg-rois", "~"], "ports": ["hg-rois", "~"], "abolitions": ["hg-revol", "~"]
  },
  "melanges": {
   "masses": ["sc-matiere", "~"], "conservation": ["sc-matiere", "="], "melanges": ["sc-matiere", "="],
   "separer-solides": ["sc-matiere", "="], "separer-liquide": ["sc-matiere", "="]
  },
  "lumiere": {
   "sources": ["sc-signal", "="], "matieres": ["sc-signal", "~"], "ombres": ["sc-signal", "~"], "soleil": ["sc-terre", "="], "lune": ["sc-terre", "="]
  },
  "alimentation": {
   "croissance": ["sc-vivant", "="], "besoins": ["sc-vivant", "="], "mastication": ["sc-vivant", "="], "digestion": ["sc-vivant", "="], "circulation": ["sc-vivant", "="]
  },
  "objets-techniques": {
   "besoin-fonction": ["sc-objets", "="], "constituants": ["sc-objets", "="], "materiaux": ["sc-objets", "="],
   "energie-mouvement": ["sc-energie", "="], "notice-montage": ["sc-objets", "="]
  },
  "station-meteo": {
   "thermometre": ["sc-outils", "="], "vent": ["sc-outils", "="], "pluie": ["sc-outils", "="], "releves": ["sc-langages", "="], "bulletin": ["sc-terre", "~"]
  }
 }
};
if(typeof module !== "undefined") module.exports = LSU;
