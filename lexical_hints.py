"""Mini-leçons et outils d'aide, rattachés aux 8 catégories d'erreurs.

Contenu adapté des leçons « Je retiens » de *Outils pour le français* CM1 et CM2
(Magnard), pour que la leçon proposée dans l'application soit exactement celle que
l'élève connaît en classe.

Chaque catégorie possède :
  · icone / couleur d'ambiance (l'affichage est coloré, grand et aéré) ;
  · a_retenir  : l'idée-clé, mise en avant en gros ;
  · regle      : la règle « Je retiens », en une ou deux phrases ;
  · questions  : les questions à se poser (niveau 1 de l'aide guidée) ;
  · procedure  : le geste mental, étape par étape ;
  · exemples   : des exemples « faux → juste » ;
  · piege      : le piège classique à éviter ;
  · source     : le renvoi au manuel (CM1/CM2) ;
  · lecon_id   : identifiant interne pour le suivi enseignant.
"""

LECONS = {
    "accord": {
        "lecon_id": "FR-ORTH-ACC-01",
        "titre": "Les accords dans le groupe nominal",
        "icone": "🧩",
        "a_retenir": "Dans un groupe nominal, tout s'accorde avec le nom : "
                     "le déterminant donne le nombre, tout le groupe suit.",
        "regle": "Le déterminant, le nom et l'adjectif s'accordent en genre "
                 "(masculin ou féminin) et en nombre (singulier ou pluriel) avec "
                 "le nom noyau du groupe.",
        "questions": [
            "Quel est le nom noyau (le mot le plus important du groupe) ?",
            "Le déterminant (le, les, des, ma, mes…) est-il singulier ou pluriel ?",
            "Masculin ou féminin ?",
            "As-tu accordé le nom ET chaque adjectif, même celui qui est loin du nom ?",
        ],
        "procedure": [
            "Je souligne le déterminant (le, les, des, mes…).",
            "Je me demande : singulier ou pluriel ? masculin ou féminin ?",
            "J'accorde le nom, puis chaque adjectif qui l'accompagne.",
        ],
        "exemples": [
            "les petit chien  →  les petits chiens",
            "des belle fleur  →  des belles fleurs",
            "une grandes maison  →  une grande maison",
        ],
        "piege": "L'adjectif peut être loin du nom : « Les fleurs du jardin sont belles. »",
        "source": "Je retiens CM1 p. 28-30 · CM2 (le groupe nominal)",
    },
    "conjugaison": {
        "lecon_id": "FR-CONJ-PRES-01",
        "titre": "Le verbe et son sujet",
        "icone": "🔗",
        "a_retenir": "Le sujet commande le verbe : le verbe s'accorde en personne "
                     "et en nombre avec son sujet.",
        "regle": "Le verbe s'accorde toujours avec son sujet, même quand le sujet "
                 "est éloigné du verbe ou placé après lui. Un même sujet peut "
                 "commander plusieurs verbes : il faut penser à tous les accorder.",
        "questions": [
            "Quel est le verbe conjugué (le mot qui change avec le temps) ?",
            "« Qui est-ce qui… ? » devant le verbe : quel est le sujet ?",
            "Par quel pronom peux-tu remplacer le sujet (il, elle, ils, elles) ?",
            "Quelle terminaison correspond à ce pronom ?",
        ],
        "procedure": [
            "Je trouve le verbe (le mot qui change quand je change le temps).",
            "Je pose la question « Qui est-ce qui… ? » pour trouver le sujet.",
            "Je remplace le sujet par un pronom (il, elle, ils, elles).",
            "J'écris la terminaison qui correspond.",
        ],
        "exemples": [
            "je -e/-s | tu -s | il/elle -e/-t | nous -ons | vous -ez | ils/elles -ent",
            "Les élèves de la classe travaille  →  travaillent",
            "Il von à l'école  →  Il va à l'école",
        ],
        "piege": "« -ent » à la fin d'un verbe ne s'entend pas, mais il s'écrit !",
        "source": "Je retiens CM1 p. 16-18 · CM2 p. 20 (le verbe et son sujet)",
    },
    "homophone": {
        "lecon_id": "FR-ORTH-HOM-01",
        "titre": "Les homophones grammaticaux",
        "icone": "👂",
        "a_retenir": "Des mots qui s'entendent pareil mais s'écrivent différemment : "
                     "c'est le REMPLACEMENT qui décide, pas l'oreille.",
        "regle": "Pour choisir entre deux homophones, on remplace le mot par un autre "
                 "mot ou une autre forme du verbe. Si la phrase garde son sens, c'est "
                 "le bon.",
        "questions": [
            "Peux-tu remplacer le mot par « avait », « était » ou « avaient » ?",
            "Si le remplacement marche, c'est le verbe (a, est, ont, sont).",
            "Sinon, c'est le petit mot (à, et, on, son).",
        ],
        "procedure": [
            "J'essaie de remplacer le mot par un autre mot que je connais.",
            "Si la phrase reste correcte, j'ai trouvé le bon.",
        ],
        "exemples": [
            "a / à  →  remplace par « avait » : « il a mangé » = « il avait mangé » ✔",
            "est / et  →  remplace par « était » : « il est parti » = « il était parti » ✔",
            "sont / son  →  remplace par « étaient »",
            "ont / on  →  remplace par « avaient »",
            "ou / où  →  remplace par « ou bien »",
            "ces / ses  →  « ces » = je montre ; « ses » = à lui, à elle",
        ],
        "piege": "Fais le test à voix basse : c'est le remplacement qui décide, pas l'oreille.",
        "source": "Je retiens CM1/CM2 (les homophones grammaticaux)",
    },
    "orthographe": {
        "lecon_id": "FR-ORTH-LEX-01",
        "titre": "L'orthographe des mots",
        "icone": "🔤",
        "a_retenir": "Pour une lettre muette à la fin, cherche un mot de la même "
                     "famille : grand → grandeur (on entend le « d »).",
        "regle": "Certains mots s'écrivent d'une seule façon : il faut les mémoriser. "
                 "Les accents et les lettres finales muettes se retrouvent souvent "
                 "grâce à un mot de la même famille.",
        "questions": [
            "Peux-tu découper le mot en syllabes pour l'écrire morceau par morceau ?",
            "Connais-tu un mot de la même famille (lent → lentement) ?",
            "Y a-t-il un accent (é, è, ê) ? une lettre muette à la fin ?",
        ],
        "procedure": [
            "Je découpe le mot en syllabes.",
            "Je cherche un mot de la même famille (lent → lentement).",
            "Je vérifie les accents et les lettres muettes.",
            "En cas de doute : je consulte le dictionnaire ou ma liste de mots.",
        ],
        "exemples": [
            "aujourdhui  →  aujourd'hui",
            "malgres  →  malgré",
            "tres  →  très",
            "grand → grandeur, petit → petitesse (la lettre finale se révèle)",
        ],
        "piege": "Les lettres muettes finales : cherche un mot de la même famille "
                 "(grand → grandeur).",
        "source": "Je retiens CM1/CM2 (orthographe lexicale, familles de mots)",
    },
    "segmentation": {
        "lecon_id": "FR-ORTH-SEG-01",
        "titre": "Séparer ou coller les mots",
        "icone": "✂️",
        "a_retenir": "Chaque mot a des frontières : on ne colle pas deux mots ensemble.",
        "regle": "Un mot doit exister tout seul dans le dictionnaire. Beaucoup de mots "
                 "se séparent (parce que, il y a) ou utilisent une apostrophe (d'abord).",
        "questions": [
            "Lis lentement : est-ce vraiment UN seul mot, ou plusieurs collés ?",
            "Chaque morceau existe-t-il tout seul dans le dictionnaire ?",
            "Faut-il une apostrophe (l', d', qu') ?",
        ],
        "procedure": [
            "Je relis lentement en marquant une petite pause entre chaque mot.",
            "Je vérifie si chaque morceau existe tout seul dans le dictionnaire.",
        ],
        "exemples": [
            "parceque  →  parce que",
            "ilya  →  il y a",
            "dabord  →  d'abord",
            "quelquun  →  quelqu'un",
        ],
        "piege": "Attention aux apostrophes : « l'école », « d'accord », « qu'il ».",
        "source": "Je retiens CM1/CM2 (orthographe, découpage des mots)",
    },
    "ponctuation": {
        "lecon_id": "FR-PONCT-01",
        "titre": "La ponctuation",
        "icone": "❗",
        "a_retenir": "La ponctuation marque les limites des phrases et donne le rythme.",
        "regle": "La ponctuation sert à marquer les limites entre les phrases et à "
                 "indiquer le ton. La virgule sépare des mots ou des groupes de mots. "
                 "Chaque phrase se termine par un point (. ! ?).",
        "questions": [
            "Lis à voix haute : où t'arrêtes-tu pour respirer ?",
            "Chaque phrase se termine-t-elle par . ! ou ? ",
            "As-tu bien mis l'espace APRÈS la virgule, mais pas avant ?",
        ],
        "procedure": [
            "Je lis mon texte à voix haute : là où je respire, il y a souvent un signe.",
            "Chaque phrase se termine par . ! ou ?",
            "Pas d'espace AVANT la virgule et le point ; une espace APRÈS.",
        ],
        "exemples": [
            "Il court , puis il s'arrête  →  Il court, puis il s'arrête",
            "Que fais-tu  →  Que fais-tu ?",
        ],
        "piege": "En français, on met une espace avant : ; ! ? mais pas avant , ni .",
        "source": "Je retiens CM1 p. 8 · CM2 p. 8 (la ponctuation)",
    },
    "majuscule": {
        "lecon_id": "FR-MAJ-01",
        "titre": "Les majuscules",
        "icone": "🅰️",
        "a_retenir": "Une majuscule au début de chaque phrase et à chaque nom propre.",
        "regle": "Une phrase commence par une majuscule et se termine par un point. "
                 "Les noms propres (prénoms, villes, pays) prennent aussi une majuscule.",
        "questions": [
            "Ce mot est-il juste après un point, donc au début d'une phrase ?",
            "Est-ce un nom propre (prénom, ville, pays) ?",
            "Si oui, la première lettre doit-elle être en grand ?",
        ],
        "procedure": [
            "Je repère chaque point : le mot juste après commence par une majuscule.",
            "Je repère les prénoms, noms de villes, de pays : majuscule.",
        ],
        "exemples": [
            "il va à paris  →  Il va à Paris",
            "hier, marie est venue  →  Hier, Marie est venue",
        ],
        "piege": "Les jours et les mois ne prennent PAS de majuscule : lundi, janvier.",
        "source": "Je retiens CM1 p. 6 · CM2 p. 6 (la phrase)",
    },
    "lexique": {
        "lecon_id": "FR-LEX-01",
        "titre": "Choisir le mot juste (et ne rien oublier)",
        "icone": "💬",
        "a_retenir": "Le mot juste, pas le mot rare — et relis pour vérifier "
                     "qu'aucun mot n'a été oublié.",
        "regle": "Un texte est plus clair quand les mots sont précis et variés. Relire "
                 "lentement permet aussi de repérer un mot oublié ou une phrase qui "
                 "ne veut rien dire.",
        "questions": [
            "Ta phrase veut-elle dire quelque chose quand tu la relis à voix haute ?",
            "Manque-t-il un petit mot (le, à, et…) ?",
            "Un mot est-il répété ou trop vague (truc, chose, faire) ?",
        ],
        "procedure": [
            "Je relis lentement pour vérifier qu'aucun mot n'est oublié.",
            "Je repère les mots répétés dans une même phrase.",
            "Je repère les mots « valises » : truc, machin, chose, faire, bien.",
            "Je cherche un synonyme plus précis.",
        ],
        "exemples": [
            "Il fait un gâteau, puis il fait ses devoirs  →  Il prépare un gâteau, "
            "puis il fait ses devoirs.",
            "un truc bizarre  →  un objet étrange",
        ],
        "piege": "Varier ne veut pas dire compliquer : le mot juste, pas le mot rare.",
        "source": "Je retiens CM1/CM2 (vocabulaire, sens de la phrase)",
    },
}


def lecon(categorie: str) -> dict:
    return LECONS.get(categorie, {})


def lecon_id(categorie: str) -> str:
    return LECONS.get(categorie, {}).get("lecon_id", "")


# --- Tableaux de conjugaison de secours (étape 2 de la procédure) ---
CONJUGAISON = {
    "être (présent)":  ["je suis", "tu es", "il/elle est", "nous sommes",
                        "vous êtes", "ils/elles sont"],
    "avoir (présent)": ["j'ai", "tu as", "il/elle a", "nous avons",
                        "vous avez", "ils/elles ont"],
    "aller (présent)": ["je vais", "tu vas", "il/elle va", "nous allons",
                        "vous allez", "ils/elles vont"],
    "faire (présent)": ["je fais", "tu fais", "il/elle fait", "nous faisons",
                        "vous faites", "ils/elles font"],
    "chanter (1er groupe, présent)": ["je chante", "tu chantes", "il/elle chante",
                                      "nous chantons", "vous chantez", "ils/elles chantent"],
    "finir (2e groupe, présent)": ["je finis", "tu finis", "il/elle finit",
                                   "nous finissons", "vous finissez", "ils/elles finissent"],
    "être (imparfait)": ["j'étais", "tu étais", "il/elle était", "nous étions",
                         "vous étiez", "ils/elles étaient"],
    "chanter (imparfait)": ["je chantais", "tu chantais", "il/elle chantait",
                            "nous chantions", "vous chantiez", "ils/elles chantaient"],
    "chanter (futur)": ["je chanterai", "tu chanteras", "il/elle chantera",
                        "nous chanterons", "vous chanterez", "ils/elles chanteront"],
    "chanter (passé composé)": ["j'ai chanté", "tu as chanté", "il/elle a chanté",
                                "nous avons chanté", "vous avez chanté",
                                "ils/elles ont chanté"],
}
