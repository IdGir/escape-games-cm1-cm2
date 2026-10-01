# -*- coding: utf-8 -*-
"""Met à jour la documentation des jeux pour le moteur v2 (octobre 2026). Idempotent.

    python outils-moteur/maj_docs.py
"""
import os
import re

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARQUE = "<!-- moteur-v2 -->"

REGLES = """{m}
### Règles du moteur v2 (octobre 2026)

- **Tout juste du premier coup** : chaque énigme rapporte **10 points** si la première vérification est juste,
  **3 points seulement** après une erreur. Le barème est rappelé en tête de chaque énigme : les élèves ont
  intérêt à relire la leçon (bouton 📚) avant de valider.
- **Retour d'erreur** : le jeu dit seulement **combien** de réponses sont justes (« 2 associations justes sur 4 »),
  jamais lesquelles. Une réponse incomplète n'est pas comptée comme une erreur.
- **Aucun texte après la réussite** : ni correction, ni explication, ni dialogue de réussite. Le bouton suivant
  apparaît tout de suite ; le personnage se tait dès que les élèves touchent l'énigme (le chrono ne s'arrête jamais).
- **Mots à noter** : le mot gagné en fin de {etape} n'est affiché **qu'une fois** (« ✍️ Notez ce mot ») ; les élèves
  le recopient sur la **fiche de mission** (⚙️ Réglages › Impression › « ✍️ Fiche de mission », une par équipe), puis
  le retapent dans le **coffre final** (10 points du premier coup, 3 après une erreur ; accents et majuscules ignorés).
- **Lettres cachées** : les lettres marquées sont **dans le désordre**, avec des **leurres** ; on les range dans les cases.
"""


def lire(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def ecrire(p, s):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(s)


def table_score(cm1, cm2, extra=""):
    return f"""| | CM1 | CM2 |
|---|---|---|
| Énigmes justes du premier coup (10 pts ; 3 pts après une erreur) | 15 × 10 = 150 | 20 × 10 = 200 |
{extra}| Coffre final ouvert du premier coup (10 pts ; 3 après une erreur) | 10 | 10 |
| Bonus de rapidité (3 pts par salle) | 15 | 15 |
| Quizz final (2 pts × 5) | 10 | 10 |
| **Total maximal** | **{cm1}** | **{cm2}** |"""


MOTEUR_COMMUN = ["melanges", "chateau-fort", "moyen-age-abbaye", "station-meteo", "objets-techniques", "constitution"]

for jeu in MOTEUR_COMMUN:
    abb = jeu == "moyen-age-abbaye"
    cm1, cm2 = (195, 245) if abb else (185, 235)
    extra = "| Fermoir du manuscrit (10 pts ; 3 après une erreur) | 10 | 10 |\n" if abb else ""
    # README
    p = os.path.join(R, jeu, "README.md")
    s = lire(p)
    nl = "\r\n" if "\r\n" in s else "\n"
    s = s.replace("\r\n", "\n")
    s = re.sub(r"\| \| CM1 \| CM2 \|\n\|---\|---\|---\|\n\| Énigmes résolues \(5 pts\)[^\n]*\n(?:\|[^\n]*\n)*?\| \*\*Total maximal\*\* \| \*\*100\*\* \| \*\*125\*\* \|",
               table_score(cm1, cm2, extra), s)
    s = s.replace("(scores 100 et 125)", f"(scores {cm1} et {cm2})")
    s = s.replace("| `lettres` | clique des lettres cachées, dans l'ordre |", "| `lettres` | range dans les cases des lettres cachées, mélangées, avec des leurres |")
    s = s.replace("| Score maximal | **100 en CM1**, **125 en CM2** ; un indice coûte 2 points |",
                  f"| Score maximal | **{cm1} en CM1**, **{cm2} en CM2** (10 pts par énigme juste du premier coup, 3 après une erreur) ; un indice coûte 2 points |")
    if MARQUE not in s:
        m = re.search(r"\n## Score[^\n]*\n", s)
        bloc = REGLES.format(m=MARQUE, etape="salle") + "\n"
        if m:
            s = s[:m.end()] + "\n" + bloc + s[m.end():]
        else:
            s = s.rstrip() + "\n\n## Score et règles du moteur v2\n\n" + bloc
    ecrire(p, s.replace("\n", nl))
    # Guide pédagogique
    p = os.path.join(R, jeu, "GUIDE-PEDAGOGIQUE.md")
    if os.path.exists(p):
        g = lire(p)
        nl = "\r\n" if "\r\n" in g else "\n"
        g = g.replace("\r\n", "\n")
        g = g.replace("(100 en CM1, 125 en CM2)", f"({cm1} en CM1, {cm2} en CM2)")
        g = g.replace("| Score maximal | 100 points | 125 points |", f"| Score maximal | {cm1} points | {cm2} points |")
        if MARQUE not in g:
            g = g.rstrip() + "\n\n## Déroulé en classe (moteur v2)\n\n" + REGLES.format(m=MARQUE, etape="salle") + \
                "\n**À préparer** : imprimer une fiche de mission par équipe (⚙️ Réglages › Impression). " \
                "Annoncer aux élèves que le mot de chaque salle ne s'affiche qu'une fois et que les erreurs coûtent cher.\n"
        ecrire(p, g.replace("\n", nl))
    print("docs v2 :", jeu)

# ---- Déclaration et Tour du monde ----
for jeu, etape, mots in (("declaration", "salle", "les 4 fragments de la devise (LIBERTÉ, ÉGALITÉ, FRATERNITÉ, 1789)"),
                          ("tour-du-monde", "escale", "les 4 cachets de voyage (ROSE DES VENTS, LE CANAL, LES CLIMATS, LA VAPEUR)")):
    p = os.path.join(R, jeu, "README.md")
    s = lire(p)
    nl = "\r\n" if "\r\n" in s else "\n"
    s = s.replace("\r\n", "\n")
    s = s.replace("Cliquer **dans l'ordre** les lettres cachées dans le texte : **L-I-B-E-R-T-É** → **LIBERTÉ**.",
                  "Ranger dans les 7 cases les lettres marquées du texte, **mélangées et avec deux leurres** : → **LIBERTÉ**.")
    s = re.sub(r"Chaque salle réussie rapporte \*\*10 points\*\*, plus \*\*5 points\*\* si elle est[\s\S]*?le score maximal est de \*\*85 points\*\*\.",
               "Chaque énigme juste **du premier coup** rapporte **10 points** (3 après une erreur), plus **5 points** si la salle\n"
               "est bouclée en moins de 3 minutes (2 en moins de 6). Un indice retire 2 points. Le **coffre final** (" + mots +
               " à retaper) rapporte 10 points du premier coup, 3 après une erreur. Un quizz final clôt la partie ;\n"
               "le score maximal est de **95 points**.", s)
    if MARQUE not in s:
        s = s.rstrip() + "\n\n## Règles du moteur v2\n\n" + REGLES.format(m=MARQUE, etape=etape) + \
            f"\nLe coffre final demande {mots}. Score maximal : **95 points** (5 × 10 + 5 × 5 de rapidité + 10 de coffre + 10 de quizz).\n" + \
            "\n**Feuilles de style** : elles manquaient au dépôt (le jeu s'affichait sans mise en page). Elles ont été restaurées en " \
            "octobre 2026 à partir de la charte commune (Constitution)" + (" avec la charte « carnet de voyage » propre au jeu (`outils-moteur/theme-tour-du-monde.css`)." if jeu == "tour-du-monde" else ".") + "\n"
    ecrire(p, s.replace("\n", nl))
    p = os.path.join(R, jeu, "GUIDE-PEDAGOGIQUE.md")
    if os.path.exists(p):
        g = lire(p)
        nl = "\r\n" if "\r\n" in g else "\n"
        g = g.replace("\r\n", "\n")
        if MARQUE not in g:
            g = g.rstrip() + "\n\n## Déroulé en classe (moteur v2)\n\n" + REGLES.format(m=MARQUE, etape=etape) + \
                f"\nLe coffre final demande {mots}. Les répliques de réussite des personnages citées plus haut ne sont plus jouées " \
                "(aucun texte après la réussite).\n\n**À préparer** : une fiche de mission par équipe (⚙️ Réglages › Impression).\n"
        ecrire(p, g.replace("\n", nl))
    print("docs v2 :", jeu)

# ---- Mission géographique ----
p = os.path.join(R, "mission-geo", "README.md")
s = lire(p)
nl = "\r\n" if "\r\n" in s else "\n"
s = s.replace("\r\n", "\n")
if MARQUE not in s:
    s = s.rstrip() + "\n\n## Règles du moteur v2 (octobre 2026)\n\n" + MARQUE + """
- **Barème** : chaque énigme rapporte **10 points** juste du premier coup, **3 points** après une erreur ; un coup de pouce
  retire 2 points. Le barème est rappelé en tête de chaque énigme et dans l'introduction de la séance.
- **Retour d'erreur** : seulement le **nombre** de bonnes réponses, sans marquer lesquelles. « Voir la correction » reste
  proposé après 3 essais (0 point).
- **Fin de séance** : plus de récit ni de leçon après la résolution ; seuls le bilan chiffré et l'**indice** s'affichent,
  **une seule fois** : les élèves le recopient sur leur **fiche de mission** (⚙️ Espace enseignant › « ✍️ Fiche de mission »,
  2 pages, à garder toute l'année). Le carnet garde la trace des indices obtenus, pas leur contenu, et la piste finale
  ne recopie plus les valeurs : les élèves calculent avec leur fiche.
- La progression déjà enregistrée sur les postes est conservée (pas de remise à zéro).
- **Feuilles de style** : `css/style.css`, `css/activites.css` et `css/print.css` manquaient au dépôt (le jeu s'affichait sans
  mise en page) ; elles ont été écrites en octobre 2026. Les styles du barème sont dans `css/v2.css`.
"""
ecrire(p, s.replace("\n", nl))
print("docs v2 : mission-geo")
