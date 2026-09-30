# -*- coding: utf-8 -*-
"""Leçons imprimables — Le Sceau de la République (constitution).

Le jeu utilise comme leçons les fiches officielles (PDF) de
decouvronsnotreconstitution.fr. Pour l'impression, cinq leçons rédigées,
une par salle, reprennent ces fiches et les faits vérifiés des énigmes.
"""
from graphiques import ouvrir, texte, taille, tableau, etapes

JEU = {
    "titre": "Le Sceau de la République",
    "matiere": "EMC",
    "theme": "La Constitution du 4 octobre 1958 : règles, textes, pouvoirs, loi, valeurs",
    "couleur": "#13286b", "accent": "#b22222",
    "couleur_pale": "#ebeff8", "accent_pale": "#fbecec",
}
BLEU, ROUGE, OR, VERT, GRIS = "#1d3a8a", "#b22222", "#b8860b", "#2e7d32", "#5b6470"
SOURCES = ("Fiches pédagogiques cycle 3 de decouvronsnotreconstitution.fr (Conseil constitutionnel, ministère de l'Éducation nationale) ; "
           "texte de la Constitution sur Légifrance ; conseil-constitutionnel.fr")


def pyramide():
    W, H = 360, 200
    fs = taille(W, 66)
    s = [ouvrir(W, H, "La Constitution est au-dessus des lois")]
    niveaux = [("CONSTITUTION", "le texte le plus important", BLEU), ("LOIS", "votées par le Parlement", "#3f63b8"),
               ("DÉCRETS, RÈGLEMENTS", "pris par le Gouvernement", "#8aa3dc")]
    for i, (t, st, c) in enumerate(niveaux):
        y0, y1 = 8 + i * 62, 8 + (i + 1) * 62 - 4
        hw0, hw1 = 40 + i * 58, 40 + (i + 1) * 58
        s.append(f'<polygon points="{180 - hw0},{y0} {180 + hw0},{y0} {180 + hw1},{y1} {180 - hw1},{y1}" fill="{c}"/>')
        s.append(texte(180, y0 + 26, t, fs * (0.9 if i else 0.85), fill="#fff", poids=800))
        s.append(texte(180, y0 + 26 + fs * 1.1, st, fs * 0.72, fill="#fff"))
    s.append("</svg>")
    return "".join(s)


def trois_pouvoirs(citoyens=False):
    W, H = 360, 230 if citoyens else 175
    fs = taille(W, 66)
    s = [ouvrir(W, H, "La séparation des pouvoirs")]
    cols = [("LÉGISLATIF", "fait les lois", "le Parlement :\nAssemblée nationale\net Sénat", BLEU),
            ("EXÉCUTIF", "les fait appliquer", "le président de la\nRépublique et le\nGouvernement", ROUGE),
            ("JUDICIAIRE", "juge", "les juges et\nles tribunaux", GRIS)]
    w = (W - 16) / 3
    top = 58 if citoyens else 4
    if citoyens:
        s.append('<defs><marker id="ar" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#444"/></marker></defs>')
        s.append(f'<rect x="80" y="4" width="200" height="28" rx="14" fill="{OR}"/>')
        s.append(texte(180, 23, "LES CITOYENS VOTENT", fs * 0.9, fill="#fff", poids=800))
        s.append(f'<line x1="120" y1="33" x2="{4 + w/2:.0f}" y2="{top - 2}" stroke="#444" stroke-width="1.4" marker-end="url(#ar)"/>')
        s.append(f'<line x1="200" y1="33" x2="{4 + w*1.5 + 4:.0f}" y2="{top - 2}" stroke="#444" stroke-width="1.4" marker-end="url(#ar)"/>')
        s.append(texte(50, 48, "députés", fs * 0.7, fill="#444", italique=True))
        s.append(texte(255, 48, "président", fs * 0.7, fill="#444", italique=True))
    for i, (t, st, qui, c) in enumerate(cols):
        x = 4 + i * (w + 4)
        s.append(f'<rect x="{x:.1f}" y="{top}" width="{w:.1f}" height="{H - top - 4}" rx="7" fill="#fff" stroke="{c}" stroke-width="1.6"/>')
        s.append(f'<rect x="{x:.1f}" y="{top}" width="{w:.1f}" height="{fs * 2:.1f}" rx="7" fill="{c}"/>')
        s.append(texte(x + w / 2, top + fs * 1.35, t, fs * 0.9, fill="#fff", poids=800))
        s.append(texte(x + w / 2, top + fs * 3.3, st, fs * 0.9, fill=c, poids=700))
        s.append(texte(x + w / 2, top + fs * 5.0, qui, fs * 0.75))
    s.append("</svg>")
    return "".join(s)


def quatre_textes():
    return etapes([
        ("1789 · Déclaration des droits de l'homme", "liberté, égalité devant la loi, propriété, sûreté", BLEU),
        ("1946 · Préambule de la Constitution", "droits sociaux : santé, école gratuite et laïque, travail", "#3f63b8"),
        ("1958 · Constitution de la Ve République", "préambule et 108 articles : qui gouverne, comment", ROUGE),
        ("2004 · Charte de l'environnement", "vivre dans un environnement équilibré et sain", VERT),
    ], sens="v", numeros=False)


def symboles():
    W, H = 360, 180
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Les symboles de la République (article 2)")]
    # drapeau
    for i, c in enumerate(["#1d3a8a", "#ffffff", "#c8102e"]):
        s.append(f'<rect x="{10 + i * 30}" y="14" width="30" height="60" fill="{c}" stroke="#9aa4ad" stroke-width="0.6"/>')
    s.append(texte(55, 92, "l'emblème : le\ndrapeau tricolore", fs * 0.72))
    items = [("la langue", "le français"), ("l'hymne", "La Marseillaise"),
             ("la devise", "Liberté, Égalité,\nFraternité"), ("le principe", "gouvernement du\npeuple, par le peuple\net pour le peuple")]
    for k, (t, v) in enumerate(items):
        x = 120 + (k % 2) * 122
        y = 14 + (k // 2) * 78
        s.append(f'<rect x="{x}" y="{y}" width="116" height="70" rx="6" fill="#fff" stroke="{BLEU}" stroke-width="1.2"/>')
        s.append(texte(x + 58, y + fs * 1.3, t.upper(), fs * 0.78, fill=ROUGE, poids=800))
        s.append(texte(x + 58, y + fs * 2.7, v, fs * (0.8 if k < 2 else 0.66), fill="#1f2328", poids=600))
    s.append("</svg>")
    return "".join(s)


def conseil():
    W, H = 360, 190
    fs = taille(W, 66)
    s = [ouvrir(W, H, "La composition du Conseil constitutionnel")]
    s.append('<defs><marker id="ar" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#444"/></marker></defs>')
    qui = [("président de\nla République", ROUGE), ("président de\nl'Assemblée", BLEU), ("président\ndu Sénat", "#6b4c9a")]
    for i, (t, c) in enumerate(qui):
        x = 10 + i * 118
        s.append(f'<rect x="{x}" y="6" width="104" height="40" rx="6" fill="{c}"/>')
        s.append(texte(x + 52, 22, t, fs * 0.72, fill="#fff", poids=700))
        s.append(f'<line x1="{x + 52}" y1="48" x2="{x + 52}" y2="84" stroke="#444" stroke-width="1.4" marker-end="url(#ar)"/>')
        s.append(texte(x + 62, 70, "nomme 3", fs * 0.7, "start", "#444", 700))
        for k in range(3):
            s.append(f'<circle cx="{x + 30 + k * 22}" cy="102" r="9" fill="{c}" fill-opacity=".85"/>')
    s.append(f'<rect x="10" y="120" width="340" height="62" rx="8" fill="#f3f5fa" stroke="{BLEU}"/>')
    s.append(texte(180, 142, "9 MEMBRES, NOMMÉS POUR 9 ANS", fs * 0.95, fill=BLEU, poids=800))
    s.append(texte(180, 142 + fs * 1.4, "renouvelés par tiers tous les 3 ans · siège au Palais-Royal", fs * 0.75))
    s.append("</svg>")
    return "".join(s)


LECONS_BASE = [
    {
        "id": "regles", "salle": 1, "icone": "I", "titre": "Qu'est-ce qu'une Constitution ?", "niveau": "CM1-CM2",
        "objectifs": ["Dire ce qu'est une Constitution", "Savoir qu'elle est au-dessus des lois",
                      "Nommer les trois pouvoirs et dire qui les exerce"],
        "contenu": {
            "cm1": "<h4>Des règles pour tout un pays</h4><p>Dans la classe, des <b>règles de vie</b> permettent de vivre ensemble. "
                   "Dans un pays, c'est la même chose : la <b>Constitution</b> est l'ensemble des règles qui organisent la vie de tous les citoyens.</p>"
                   "<div class='encadre'>La Constitution est le <b>texte le plus important</b> du pays : toutes les <b>lois</b> doivent la respecter.</div>"
                   "<h4>Ce que dit la Constitution</h4><p>Elle dit <b>qui gouverne</b>, comment on <b>vote</b> et quels <b>droits</b> sont protégés. "
                   "En France, elle est <b>écrite</b>.</p>"
                   "<h4>Trois pouvoirs séparés</h4><p>Pour éviter qu'une seule personne ait tous les pouvoirs, la Constitution les <b>sépare</b> : "
                   "le Parlement <b>fait les lois</b>, le président de la République et le Gouvernement les <b>font appliquer</b>, "
                   "les juges <b>jugent</b> ceux qui ne les respectent pas.</p>",
            "cm2": "<h4>La règle du jeu d'un pays</h4><p>Une <b>Constitution</b> est l'ensemble des règles qui organisent la vie d'un pays : "
                   "qui gouverne, comment on choisit ses représentants, quels droits et libertés sont garantis.</p>"
                   "<div class='encadre'>C'est le texte le plus important : il est <b>au-dessus des lois</b>. Une loi contraire à la Constitution "
                   "ne peut pas s'appliquer ; c'est le <b>Conseil constitutionnel</b> qui le vérifie.</div>"
                   "<h4>La séparation des pouvoirs</h4><p>Cette idée des Lumières (Montesquieu) est inscrite dans la Constitution : "
                   "le pouvoir <b>législatif</b> (le Parlement) fait et vote les lois ; le pouvoir <b>exécutif</b> (le président de la République "
                   "et le Gouvernement) les fait appliquer ; l'autorité <b>judiciaire</b> (les juges et les tribunaux) sanctionne ceux qui ne les respectent pas.</p>"
                   "<h4>Plusieurs Constitutions</h4><p>La première Constitution écrite de la France date de <b>1791</b>. Depuis, le pays en a connu plusieurs. "
                   "Celle d'aujourd'hui date du <b>4 octobre 1958</b> : elle a fondé la <b>Ve République</b>.</p>",
        },
        "frise": [{"date": "1791", "evt": "Première Constitution écrite"}, {"date": "1848", "evt": "IIe République"},
                  {"date": "1875", "evt": "IIIe République"}, {"date": "1946", "evt": "IVe République"},
                  {"date": "1958", "evt": "Ve République"}],
        "frise_titre": "Quelques Constitutions de la France",
        "document": {"type": "texte", "titre": "Article 16 de la Déclaration des droits de l'homme et du citoyen (1789)",
                     "contenu": "« Toute société dans laquelle la garantie des droits n'est pas assurée, ni la séparation des pouvoirs déterminée, n'a point de Constitution. »",
                     "source": "Déclaration des droits de l'homme et du citoyen, 26 août 1789."},
        "lexique": [{"mot": "Constitution", "def": "ensemble des règles qui organisent la vie d'un pays"},
                    {"mot": "loi", "def": "règle votée par le Parlement, qui s'applique à tous"},
                    {"mot": "citoyen", "def": "personne qui a des droits et des devoirs dans un pays, dont le droit de vote"},
                    {"mot": "pouvoir", "def": "droit de décider et d'agir (faire les lois, les appliquer, juger)"}],
        "sources": SOURCES,
    },
    {
        "id": "textes", "salle": 2, "icone": "II", "titre": "Le texte de la Constitution de 1958", "niveau": "CM1-CM2",
        "objectifs": ["Dater la Constitution de la Ve République", "Décrire comment elle est organisée",
                      "Nommer les quatre textes qu'elle protège"],
        "contenu": {
            "cm1": "<h4>Une Constitution votée par les Français</h4><p>En <b>septembre 1958</b>, les Français acceptent la nouvelle Constitution "
                   "par un <b>référendum</b> : ils répondent « oui » ou « non » par un vote. Elle est <b>promulguée le 4 octobre 1958</b> : "
                   "c'est la naissance de la <b>Ve République</b>.</p>"
                   "<div class='encadre'>La Constitution comprend un <b>préambule</b> (une introduction) et <b>108 articles</b>.</div>"
                   "<h4>Quatre textes importants</h4><p>Le préambule renvoie à trois autres textes. Avec la Constitution, ils forment "
                   "<b>quatre textes</b> que toutes les lois doivent respecter : la Déclaration des droits de l'homme et du citoyen (<b>1789</b>), "
                   "le Préambule de la Constitution de <b>1946</b>, la Constitution de <b>1958</b> et la Charte de l'environnement (<b>2004</b>).</p>",
            "cm2": "<h4>Naissance de la Ve République</h4><p>Adoptée par <b>référendum</b> en septembre 1958, la Constitution est "
                   "<b>promulguée le 4 octobre 1958</b>. Elle comporte un <b>préambule</b> et <b>108 articles</b> regroupés en titres : "
                   "la souveraineté, le président de la République, le Gouvernement, le Parlement, le Conseil constitutionnel…</p>"
                   "<h4>Le bloc de constitutionnalité</h4><p>Le préambule renvoie à trois textes plus anciens ou plus récents. Les quatre textes "
                   "forment le <b>bloc de constitutionnalité</b> : c'est sur eux que le Conseil constitutionnel s'appuie pour vérifier qu'une loi est conforme.</p>"
                   "<div class='encadre'><b>1789</b> : les droits de l'homme (liberté, égalité, propriété, sûreté). <b>1946</b> : des droits sociaux "
                   "(santé, école gratuite et laïque, travail, égalité femmes-hommes). <b>2004</b> : le droit de vivre dans un environnement équilibré, "
                   "intégré à la Constitution en <b>2005</b>.</div>"
                   "<h4>Un texte qui évolue</h4><p>La Constitution peut être modifiée : on parle de <b>révision</b>. Elle l'a été plus de vingt fois depuis 1958.</p>",
        },
        "frise": [{"date": "1789", "evt": "Déclaration des droits de l'homme"}, {"date": "1946", "evt": "Préambule de la Constitution"},
                  {"date": "sept. 1958", "evt": "Référendum"}, {"date": "4 oct. 1958", "evt": "Promulgation"},
                  {"date": "2005", "evt": "Charte de l'environnement intégrée"}],
        "document": {"type": "texte", "titre": "Le début du préambule de la Constitution de 1958",
                     "contenu": "« Le peuple français proclame solennellement son attachement aux Droits de l'homme et aux principes de la souveraineté nationale "
                                "tels qu'ils ont été définis par la Déclaration de 1789, confirmée et complétée par le préambule de la Constitution de 1946, "
                                "ainsi qu'aux droits et devoirs définis dans la Charte de l'environnement de 2004. »",
                     "source": "Constitution du 4 octobre 1958, préambule."},
        "lexique": [{"mot": "référendum", "def": "vote où les citoyens répondent par oui ou par non à une question"},
                    {"mot": "promulguer", "def": "rendre un texte officiel en le signant (rôle du président)"},
                    {"mot": "préambule", "def": "introduction d'un texte, qui en donne les principes"},
                    {"mot": "article", "def": "partie numérotée d'un texte de loi"},
                    {"mot": "révision", "def": "modification de la Constitution"}],
        "sources": SOURCES,
    },
    {
        "id": "peuple", "salle": 3, "icone": "III", "titre": "La vie démocratique : qui décide ?", "niveau": "CM1-CM2",
        "objectifs": ["Dire que le pouvoir appartient au peuple", "Nommer les élus et dire comment ils sont choisis",
                      "Associer chaque institution à son pouvoir"],
        "contenu": {
            "cm1": "<h4>Le peuple choisit ses représentants</h4><p>En France, le pouvoir appartient au <b>peuple</b>. Les citoyens français "
                   "de <b>18 ans</b> et plus <b>votent</b> pour choisir leurs représentants.</p>"
                   "<div class='encadre'>Le <b>président de la République</b> est élu pour <b>5 ans</b> par tous les électeurs. "
                   "Les <b>577 députés</b> sont élus pour 5 ans. Les <b>348 sénateurs</b> sont élus par d'autres élus.</div>"
                   "<h4>Qui fait quoi ?</h4><p>Le <b>Parlement</b> (l'Assemblée nationale et le Sénat) vote les lois. Le <b>président</b> et le "
                   "<b>Gouvernement</b> (le Premier ministre et les ministres) les font appliquer. Les <b>juges</b> rendent la justice.</p>",
            "cm2": "<h4>La souveraineté du peuple</h4><p>La Constitution dit que la souveraineté appartient au <b>peuple</b>, qui l'exerce "
                   "par ses <b>représentants</b> élus et par le <b>référendum</b>. Votent les citoyens français de 18 ans et plus.</p>"
                   "<h4>Le pouvoir exécutif</h4><p>Le <b>président de la République</b> est élu au <b>suffrage universel direct</b> pour "
                   "<b>5 ans</b>, renouvelable une fois. Il veille au respect de la Constitution, nomme le <b>Premier ministre</b>, promulgue les lois "
                   "et est chef des armées. Le <b>Gouvernement</b> dirige la politique du pays et applique les lois.</p>"
                   "<h4>Le pouvoir législatif</h4><p>Le <b>Parlement</b> a deux assemblées : l'<b>Assemblée nationale</b> (577 députés élus pour "
                   "5 ans au suffrage universel direct) et le <b>Sénat</b> (348 sénateurs élus pour 6 ans au <b>suffrage indirect</b>, par de "
                   "« grands électeurs » : maires, conseillers municipaux, départementaux et régionaux, députés).</p>"
                   "<div class='encadre'>L'autorité <b>judiciaire</b>, indépendante, est confiée aux juges.</div>",
        },
        "frise": [{"date": "1959", "evt": "Charles de Gaulle"}, {"date": "1969", "evt": "Georges Pompidou"},
                  {"date": "1974", "evt": "Valéry Giscard d'Estaing"}, {"date": "1981", "evt": "François Mitterrand"},
                  {"date": "1995", "evt": "Jacques Chirac"}, {"date": "2007", "evt": "Nicolas Sarkozy"},
                  {"date": "2012", "evt": "François Hollande"}, {"date": "2017", "evt": "Emmanuel Macron"}],
        "frise_titre": "Les présidents de la Ve République (début du mandat)",
        "document": {"type": "texte", "titre": "Article 3 de la Constitution",
                     "contenu": "« La souveraineté nationale appartient au peuple qui l'exerce par ses représentants et par la voie du référendum. »",
                     "source": "Constitution du 4 octobre 1958, article 3."},
        "lexique": [{"mot": "suffrage universel direct", "def": "tous les électeurs votent eux-mêmes pour choisir l'élu"},
                    {"mot": "suffrage indirect", "def": "des élus votent pour choisir un autre élu (les sénateurs)"},
                    {"mot": "député", "def": "élu qui siège à l'Assemblée nationale et vote les lois"},
                    {"mot": "Gouvernement", "def": "le Premier ministre et les ministres, qui appliquent les lois"}],
        "sources": SOURCES,
    },
    {
        "id": "loi", "salle": 4, "icone": "IV", "titre": "Le parcours d'une loi", "niveau": "CM1-CM2",
        "objectifs": ["Dire qui peut proposer une loi", "Remettre dans l'ordre les étapes du vote d'une loi",
                      "Expliquer la navette entre les deux assemblées"],
        "contenu": {
            "cm1": "<h4>D'où vient une loi ?</h4><p>Le <b>Gouvernement</b> propose un <b>projet de loi</b> ; les députés ou les sénateurs "
                   "proposent une <b>proposition de loi</b>.</p>"
                   "<h4>Le vote au Parlement</h4><p>Le texte est étudié, discuté et modifié par des <b>amendements</b>. L'<b>Assemblée nationale</b> "
                   "et le <b>Sénat</b> le votent chacun à leur tour : c'est la <b>navette</b>, jusqu'à ce qu'ils soient d'accord.</p>"
                   "<div class='encadre'>Ensuite, le président de la République <b>promulgue</b> la loi (il a 15 jours). Elle est publiée au "
                   "<b>Journal officiel</b> et s'applique alors à <b>tous</b>.</div>",
            "cm2": "<h4>L'initiative</h4><p>Une loi part d'un <b>projet de loi</b> (Gouvernement) ou d'une <b>proposition de loi</b> "
                   "(députés ou sénateurs). Le texte est d'abord examiné en <b>commission</b>, puis débattu en séance ; chacun peut déposer "
                   "des <b>amendements</b> pour le modifier.</p>"
                   "<h4>La navette</h4><p>Le texte passe de l'Assemblée nationale au Sénat, et inversement, jusqu'à être voté dans les "
                   "mêmes termes. En cas de désaccord, une commission de 7 députés et 7 sénateurs cherche un compromis ; si cela échoue, "
                   "l'<b>Assemblée nationale peut avoir le dernier mot</b>.</p>"
                   "<h4>Du vote à l'application</h4><p>Avant la promulgation, le <b>Conseil constitutionnel</b> peut être saisi pour vérifier "
                   "que la loi respecte la Constitution. Le président la <b>promulgue</b> dans les <b>15 jours</b>, puis elle est publiée au "
                   "<b>Journal officiel</b> ; le Gouvernement la fait appliquer.</p>",
        },
        "document": {"type": "texte", "titre": "Article 24 de la Constitution",
                     "contenu": "« Le Parlement vote la loi. Il contrôle l'action du Gouvernement. Il évalue les politiques publiques. »",
                     "source": "Constitution du 4 octobre 1958, article 24."},
        "lexique": [{"mot": "projet de loi", "def": "texte proposé par le Gouvernement"},
                    {"mot": "proposition de loi", "def": "texte proposé par des députés ou des sénateurs"},
                    {"mot": "amendement", "def": "modification proposée à un texte de loi"},
                    {"mot": "navette", "def": "allers-retours d'un texte entre l'Assemblée nationale et le Sénat"},
                    {"mot": "Journal officiel", "def": "journal où sont publiées les lois pour que tous les connaissent"}],
        "sources": SOURCES,
    },
    {
        "id": "gardien", "salle": 5, "icone": "V", "titre": "Valeurs, libertés et gardien de la Constitution", "niveau": "CM1-CM2",
        "objectifs": ["Citer les valeurs et les symboles de la République", "Donner des exemples de droits protégés",
                      "Dire le rôle et la composition du Conseil constitutionnel"],
        "contenu": {
            "cm1": "<h4>Les valeurs de la République</h4><p>L'article 1er dit : « La France est une République <b>indivisible</b>, "
                   "<b>laïque</b>, <b>démocratique</b> et <b>sociale</b>. » Tous les citoyens sont <b>égaux devant la loi</b>.</p>"
                   "<h4>Les symboles</h4><p>L'article 2 donne la langue (le <b>français</b>), le <b>drapeau</b> bleu, blanc, rouge, l'hymne "
                   "(<b>La Marseillaise</b>) et la devise « <b>Liberté, Égalité, Fraternité</b> ».</p>"
                   "<div class='encadre'>Le <b>Conseil constitutionnel</b> est le <b>gardien</b> de la Constitution : il vérifie que les lois la "
                   "respectent. Il a <b>9 membres</b>, nommés pour <b>9 ans</b>, et siège au Palais-Royal, à Paris.</div>",
            "cm2": "<h4>Des principes et des valeurs</h4><p>La République est <b>indivisible</b> (une seule loi pour tout le territoire), "
                   "<b>laïque</b> (elle respecte toutes les croyances et n'en impose aucune), <b>démocratique</b> (le pouvoir vient du peuple) "
                   "et <b>sociale</b> (elle aide ceux qui en ont besoin). Elle assure l'<b>égalité devant la loi</b>.</p>"
                   "<h4>La Constitution au quotidien</h4><p>Elle protège des droits qui touchent la vie de tous : l'<b>école gratuite et laïque</b>, "
                   "la <b>protection de la santé</b>, le droit à un <b>environnement</b> sain, la <b>liberté d'expression</b>…</p>"
                   "<h4>Le Conseil constitutionnel</h4><p>Ses <b>9 membres</b> sont nommés pour <b>9 ans</b> : 3 par le président de la République, "
                   "3 par le président de l'Assemblée nationale, 3 par le président du Sénat ; un tiers est renouvelé tous les 3 ans. "
                   "Il contrôle les lois <b>avant</b> leur promulgation, et <b>après</b> : depuis 2010, lors d'un procès, une personne peut demander "
                   "si une loi respecte ses droits (question prioritaire de constitutionnalité).</p>",
        },
        "document": {"type": "texte", "titre": "Article 2 de la Constitution (extrait)",
                     "contenu": "« La langue de la République est le français. L'emblème national est le drapeau tricolore, bleu, blanc, rouge. "
                                "L'hymne national est la Marseillaise. La devise de la République est Liberté, Égalité, Fraternité. "
                                "Son principe est : gouvernement du peuple, par le peuple et pour le peuple. »",
                     "source": "Constitution du 4 octobre 1958, article 2."},
        "lexique": [{"mot": "laïque", "def": "qui respecte toutes les croyances sans en favoriser aucune"},
                    {"mot": "indivisible", "def": "qui ne peut pas être partagé : une seule loi pour tout le territoire"},
                    {"mot": "Conseil constitutionnel", "def": "institution qui vérifie que les lois respectent la Constitution"},
                    {"mot": "hymne", "def": "chant officiel d'un pays"}],
        "sources": SOURCES,
    },
]

LECONS = {
    "regles": {
        "competence": "EMC — Identifier les règles communes qui organisent la vie collective : qu'est-ce qu'une Constitution ?",
        "visuels": [{"type": "svg", "titre": "La Constitution est au-dessus des lois", "svg": pyramide()},
                    {"type": "svg", "titre": "Trois pouvoirs séparés", "svg": trois_pouvoirs()},
                    {"type": "photo", "src": "assets/images/decors/salle1.jpg", "titre": "Le Palais-Royal, à Paris",
                     "legende": "Il abrite le Conseil constitutionnel."}],
    },
    "textes": {
        "competence": "EMC — Connaître les textes fondateurs de la Constitution de la Ve République.",
        "visuels": [{"type": "svg", "titre": "Les quatre textes du bloc de constitutionnalité", "svg": quatre_textes()},
                    {"type": "photo", "src": "assets/images/decors/salle2.jpg", "titre": "Les Archives nationales, à Paris",
                     "legende": "L'original de la Constitution de 1958 y est conservé."}],
    },
    "peuple": {
        "competence": "EMC — Distinguer les pouvoirs législatif, exécutif et judiciaire ; le rôle du président de la République.",
        "visuels": [{"type": "svg", "titre": "Les citoyens élisent, les pouvoirs sont séparés", "svg": trois_pouvoirs(citoyens=True)},
                    {"type": "svg", "etiquette": "Tableau", "titre": "Les élus nationaux",
                     "svg": tableau(["", "Nombre", "Mandat", "Élu par"], [
                         ["Président", "1", "5 ans", "tous les électeurs"],
                         ["Députés", "577", "5 ans", "tous les électeurs"],
                         ["Sénateurs", "348", "6 ans", "des grands électeurs"],
                     ], couleur=BLEU, largeurs=[1.1, 0.8, 0.8, 1.5])},
                    {"type": "photo", "src": "assets/images/decors/salle3.jpg", "titre": "Le Palais Bourbon, siège de l'Assemblée nationale"}],
    },
    "loi": {
        "competence": "EMC — Comprendre le parcours d'une loi (la navette parlementaire).",
        "visuels": [{"type": "svg", "titre": "Le parcours d'une loi",
                     "svg": etapes([("Dépôt", "projet (Gouvernement) ou proposition (parlementaires)", GRIS),
                                    ("Commission et débat", "le texte est étudié et amendé", "#3f63b8"),
                                    ("Navette", "vote à l'Assemblée nationale et au Sénat", BLEU),
                                    ("Promulgation", "par le président, dans les 15 jours", ROUGE),
                                    ("Journal officiel", "la loi est publiée, puis appliquée", VERT)], sens="v")},
                    {"type": "photo", "src": "assets/images/decors/salle4.jpg", "titre": "Le palais du Luxembourg, siège du Sénat"}],
    },
    "gardien": {
        "competence": "Histoire — Lois protectrices des droits et des libertés ; EMC — valeurs et principes de la République.",
        "visuels": [{"type": "svg", "titre": "Les symboles de la République (article 2)", "svg": symboles()},
                    {"type": "svg", "titre": "Le gardien de la Constitution", "svg": conseil()},
                    {"type": "photo", "src": "assets/images/decors/salle5.jpg", "titre": "Le Conseil constitutionnel, au Palais-Royal"}],
    },
}
