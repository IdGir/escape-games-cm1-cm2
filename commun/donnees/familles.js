/* ============================================================
   FORMULATIONS POUR LES FAMILLES (amélioration N30) — données publiques communes
   ------------------------------------------------------------
   La fiche synthèse pour les familles (passeport.html, « 👪 Fiche pour les familles ») redit, en
   langage de tous les jours, ce que le passeport de compétences (C3) note en termes de programme.
   Pour chaque leçon d'un jeu (clé de lecons-a4.json) : ce que l'élève a appris à FAIRE, en une
   proposition à l'infinitif, sans jargon (pas de « compétence », « socle », « cycle », « programme »,
   « acquis »…), qui se lit après « Apprendre à … » ou une puce.
   « deroule » : une phrase sur le jeu lui-même, pour les parents (ce que les enfants ont vécu).
   Un nouveau jeu : ajouter ici ses leçons et sa phrase ; le test commun/tests/test-pages.js (N30)
   échoue tant qu'une leçon du passeport n'a pas de formulation, ou si le jargon s'y glisse.
   Ces textes sont À RELIRE par un parent non enseignant (voir commun/README.md, N30).
   Fichier .js (et non .json) pour fonctionner aussi en double-clic.
   ============================================================ */
var FAMILLES = {
 "version": "2026-11",
 "niveaux": {
  "A": "bien en place",
  "E": "en progrès",
  "N": "à consolider"
 },
 "jeux": {
  "alimentation": {
   "deroule": "En équipe, les élèves sont devenus les aides d'une cheffe de cuisine et ont résolu des énigmes pour comprendre ce que devient un repas dans le corps.",
   "lecons": {
    "croissance": "comprendre pourquoi le corps a besoin de manger pour grandir",
    "besoins": "expliquer pourquoi on ne mange pas pareil à tous les âges, ni quand on fait beaucoup de sport",
    "mastication": "suivre le trajet des aliments dans la bouche et voir comment les dents les transforment",
    "digestion": "nommer les organes de la digestion et dire à quoi sert chacun",
    "circulation": "comprendre comment le sang apporte ce qu'il faut aux muscles, et pourquoi le cœur bat plus vite à l'effort"
   }
  },
  "chateau-fort": {
   "deroule": "Au Moyen Âge, en équipe, les élèves ont parcouru un château et son village pour retrouver cinq clés cachées, en résolvant une énigme à chaque étape.",
   "lecons": {
    "construire-un-chateau": "expliquer comment et pourquoi on construisait un château fort",
    "les-defenses": "décrire comment un château fort protégeait ceux qui y vivaient",
    "vie-du-seigneur": "raconter la vie du seigneur et pourquoi son château montrait sa puissance",
    "vie-des-paysans": "raconter la vie de tous les jours des paysans et des paysannes au Moyen Âge",
    "seigneur-et-paysans": "expliquer les liens entre le seigneur et les paysans qui vivaient près de son château"
   }
  },
  "constitution": {
   "deroule": "En équipe, les élèves ont ouvert, énigme après énigme, un coffre scellé en 1958 : celui de la Constitution, le texte qui organise notre République.",
   "lecons": {
    "regles": "comprendre pourquoi un pays a besoin de règles communes, écrites dans une Constitution",
    "textes": "connaître les grands textes sur lesquels s'appuie la Constitution de la Ve République",
    "peuple": "distinguer ceux qui font les lois, ceux qui les appliquent et ceux qui jugent, et dire le rôle du président",
    "loi": "suivre le parcours d'une loi avant qu'elle soit adoptée",
    "gardien": "comprendre comment les lois protègent nos droits et nos libertés"
   }
  },
  "declaration": {
   "deroule": "À Paris, en août 1789, un article secret de la Déclaration des droits de l'homme a disparu : les élèves, en équipe, l'ont retrouvé en résolvant des énigmes sur la Révolution française.",
   "lecons": {
    "causes": "expliquer pourquoi les Français étaient mécontents en 1789",
    "etats-generaux": "raconter comment le pouvoir absolu du roi a commencé à prendre fin",
    "bastille": "raconter la prise de la Bastille et pourquoi elle est restée célèbre",
    "declaration": "expliquer ce que dit la Déclaration des droits de l'homme et du citoyen",
    "personnages": "reconnaître les personnages importants de la Révolution française",
    "devise": "expliquer le sens de la devise « Liberté, Égalité, Fraternité »",
    "femmes": "comprendre quelle place avaient les femmes pendant la Révolution",
    "paris": "situer sur une carte les lieux de la Révolution à Paris et à Versailles"
   }
  },
  "etats-matiere": {
   "deroule": "En équipe, les élèves sont devenus ingénieurs stagiaires d'une usine arrêtée après un orage et ont remis les machines en marche en comprenant le solide, le liquide et le gaz.",
   "lecons": {
    "etats": "reconnaître un solide, un liquide et un gaz grâce à ce qu'on peut observer",
    "air": "montrer que l'air est bien de la matière : il prend de la place et il pèse",
    "changements": "observer et nommer les changements d'état de l'eau (fonte, ébullition…) et leurs températures",
    "conservation": "comparer avant et après un changement d'état : la masse reste la même",
    "proprietes": "classer des matériaux selon leurs propriétés et raconter le cycle de l'eau"
   }
  },
  "mouvement": {
   "deroule": "En équipe, les élèves sont devenus commissaires d'un Grand Prix de véhicules et ont retrouvé les feuilles de mesure en mesurant des distances et des durées.",
   "lecons": {
    "distance": "mesurer la distance parcourue par un objet et passer d'une unité à l'autre",
    "duree": "mesurer une durée entre deux instants avec un chronomètre",
    "comparer": "comparer deux déplacements : lequel va le plus loin, lequel va le plus vite",
    "trajectoires": "reconnaître un mouvement en ligne droite ou en cercle",
    "observateur": "comprendre qu'un mouvement se décrit toujours depuis la place de celui qui regarde"
   }
  },
  "traite-colonies": {
   "deroule": "En équipe, les élèves ont enquêté dans les archives d'un port pour comprendre la traite des esclaves, la vie dans les plantations, les résistances et les abolitions.",
   "lecons": {
    "triangle": "expliquer le commerce triangulaire entre l'Europe, l'Afrique et l'Amérique",
    "traite": "comprendre ce qu'était la traite des Africains réduits en esclavage",
    "plantations": "décrire la vie et le travail forcé des esclaves dans les plantations",
    "ports": "montrer comment des ports français se sont enrichis grâce à ce commerce",
    "abolitions": "situer les résistances et les abolitions de l'esclavage (1794, 1848)"
   }
  },
  "lumiere": {
   "deroule": "Sur une île imaginaire, le phare ne s'allumait plus : en équipe, les élèves l'ont rallumé avant l'arrivée d'un bateau, en résolvant des énigmes sur la lumière, les ombres, le Soleil et la Lune.",
   "lecons": {
    "sources": "reconnaître une source de lumière et comprendre que la lumière voyage en ligne droite",
    "matieres": "trier les matériaux selon qu'ils laissent passer la lumière ou non",
    "ombres": "fabriquer une ombre et comprendre ce qui change sa forme et sa taille",
    "soleil": "relier la place de l'ombre d'un bâton au déplacement du Soleil dans la journée",
    "lune": "dessiner et nommer les phases de la Lune"
   }
  },
  "melanges": {
   "deroule": "Dans le laboratoire d'une savante dont l'apprentie avait renversé toutes les fioles, les élèves ont pesé, trié, filtré et fait évaporer, en équipe, pour retrouver cinq opérations à la suite.",
   "lecons": {
    "masses": "comparer et mesurer des masses avec une balance",
    "conservation": "comprendre ce qui se passe quand on dissout du sucre ou du sel dans l'eau",
    "melanges": "distinguer les mélanges où l'on voit les ingrédients de ceux où on ne les voit plus",
    "separer-solides": "séparer des mélanges de solides (tri, aimant)",
    "separer-liquide": "séparer un liquide et un solide mélangés (filtrer, laisser reposer, faire évaporer)"
   }
  },
  "mission-geo": {
   "deroule": "Une valise a été volée : au fil des séances, les élèves ont rassemblé des indices de géographie pour la retrouver, jusqu'à une piste finale en Corse.",
   "lecons": {
    "l01": "découvrir sa commune et ses lieux importants",
    "l02": "situer sa commune dans le département, la région, le pays et le continent",
    "l03": "comprendre comment on vit à la campagne et où la population est plus ou moins nombreuse",
    "l04": "comprendre comment on vit en ville et quels métiers on y exerce",
    "l05": "découvrir la vie en montagne et le tourisme",
    "l06": "découvrir une autre région : le littoral normand et ses touristes",
    "l07": "nommer les mers et les océans qui bordent la France et découvrir le tourisme sur le littoral",
    "l08": "repérer les inégalités de richesse dans le monde et les situer sur une carte du monde",
    "l09": "comparer ce que mangent les habitants des pays riches et des pays pauvres",
    "l10": "faire la différence entre un produit agricole et un produit transformé",
    "l11": "suivre le trajet d'un aliment, de la ferme à l'assiette (le yaourt)",
    "l12": "découvrir d'où viennent nos aliments et le chemin qu'ils parcourent",
    "l13": "repérer les grands fleuves et les grandes montagnes de France",
    "l14": "suivre le trajet de l'eau d'un fleuve, de la source à l'embouchure",
    "l15": "décrire à quoi sert l'eau douce en France",
    "l16": "comprendre pourquoi l'eau est précieuse et peut être source de désaccords"
   }
  },
  "moyen-age-abbaye": {
   "deroule": "À la veille de la visite de l'évêque, cinq pages d'un manuscrit avaient disparu : en équipe, les élèves, apprentis moines copistes, les ont refaites en résolvant des énigmes sur le Moyen Âge.",
   "lecons": {
    "clovis": "situer la fin de l'Empire romain et l'arrivée des royaumes francs, avec Clovis",
    "charlemagne": "raconter qui était Charlemagne et ce qu'il a construit",
    "scriptorium": "expliquer le rôle de l'Église dans l'enseignement : les moines copistes",
    "hotel-dieu": "expliquer comment l'Église aidait les pauvres et les malades",
    "roman-gothique": "reconnaître une église romane et une église gothique"
   }
  },
  "objets-techniques": {
   "deroule": "Une inventrice était partie en laissant cinq machines démontées : en équipe, les élèves ont compris à quoi elles servent, de quoi elles sont faites et comment elles fonctionnent pour ouvrir son coffre.",
   "lecons": {
    "besoin-fonction": "expliquer à quoi sert un objet et quel besoin il satisfait",
    "constituants": "décrire les pièces d'un objet et les repérer sur un schéma",
    "materiaux": "dire dans quelles matières un objet est fabriqué, et pourquoi",
    "energie-mouvement": "expliquer comment l'énergie fait fonctionner un objet et transmet le mouvement",
    "notice-montage": "lire une notice et comprendre les étapes de fabrication ou de montage"
   }
  },
  "renaissance": {
   "deroule": "À Amboise, en 1518, un coup de vent a dispersé les pages du carnet de Léonard de Vinci : en équipe, les élèves les ont retrouvées avant la fête du roi, en résolvant des énigmes sur la Renaissance.",
   "lecons": {
    "renaissance-humanisme": "expliquer comment la Renaissance est arrivée d'Italie, avec l'imprimerie et l'humanisme",
    "francois-mecene": "raconter comment François Ier a protégé les artistes et les écrivains",
    "leonard-de-vinci": "découvrir Léonard de Vinci, à la fois peintre, ingénieur et observateur",
    "chateaux-renaissance": "reconnaître les châteaux de la Renaissance (Amboise, Blois, Chambord)",
    "art-renaissance": "reconnaître ce qui change dans l'art : la perspective, les proportions, le portrait"
   }
  },
  "station-meteo": {
   "deroule": "Un orage avait déréglé la station météo de l'école : en équipe, les élèves ont remis en service ses cinq instruments pour pouvoir annoncer le bulletin météo.",
   "lecons": {
    "thermometre": "mesurer la température avec un thermomètre",
    "vent": "mesurer la force et la direction du vent",
    "pluie": "mesurer la pluie avec un pluviomètre",
    "releves": "noter des mesures dans un tableau et les lire",
    "bulletin": "faire la différence entre météo et climat, et préparer un bulletin météo"
   }
  },
  "tour-du-monde": {
   "deroule": "Sur les traces d'un célèbre voyageur dont le carnet avait disparu, les élèves ont fait escale en cinq lieux du monde et résolu à chaque étape une énigme de géographie.",
   "lecons": {
    "planisphere": "nommer et situer les continents et les océans sur une carte du monde",
    "orientation": "s'orienter avec les points cardinaux et la rose des vents",
    "carte": "lire une carte : sa légende et son échelle",
    "climats": "reconnaître les grands climats et les paysages du monde",
    "deplacer": "suivre un itinéraire et connaître les moyens de transport, les canaux et les détroits",
    "fuseaux": "comprendre les méridiens et les fuseaux horaires"
   }
  },
  "versailles": {
   "deroule": "Un pli scellé de 1598 a traversé un siècle d'histoire : en équipe, les élèves, secrétaires du roi, ont levé ses cinq sceaux en résolvant des énigmes, d'Henri IV à Louis XIV.",
   "lecons": {
    "reforme-guerres": "raconter comment la Réforme a mené aux guerres de Religion",
    "edit-de-nantes": "expliquer l'édit de Nantes (1598), un accord pour vivre ensemble malgré les religions",
    "chateau-versailles": "décrire le château de Versailles et la cour de Louis XIV, le roi Soleil",
    "journee-du-roi": "raconter une journée de Louis XIV et les règles de la cour",
    "monarchie-absolue": "comprendre ce qu'est un roi qui décide de tout, en comparant Henri IV et Louis XIV"
   }
  }
 }
};
if(typeof module !== "undefined") module.exports = FAMILLES;
