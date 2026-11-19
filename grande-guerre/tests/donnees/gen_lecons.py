# -*- coding: utf-8 -*-
"""Génère grande-guerre/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>
Le texte CM2 est fait des phrases de fiches.py (reprises mot pour mot par les justifications des grades)."""
import json, os, sys
from schemas import camps, tranchee, front_arriere, frise, monument
import fiches as F

BO = "Programme d'histoire du cycle 3 (BO n° 22 du 28 mai 2026), Première Guerre mondiale ; progression de l'enseignant : thème 6, année A, période 5"
CDM = "Ministère des Armées, Chemins de mémoire"


def L(id, salle, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": str(salle), "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


LECONS = [
    L("causes", 1, "1914 : l'entrée en guerre",
      ["Connaître les causes de la guerre : rivalités entre puissances et alliances", "Situer l'attentat de Sarajevo et la mobilisation générale",
       "CM2 : dater précisément l'été 1914 (28 juin, 1er-2 août, 3 août)", "Distinguer la légende de « la fleur au fusil » de la réalité"],
      "<h4>Une Europe divisée</h4><p>En 1914, les grands pays d'Europe sont <b>rivaux</b>. Ils forment deux <b>alliances</b> : d'un côté la France, le Royaume-Uni et la Russie ; de l'autre l'Allemagne et l'Autriche-Hongrie.</p>"
      "<h4>L'été 1914</h4><p>Fin juin 1914, l'héritier de l'Autriche-Hongrie est tué à <b>Sarajevo</b>. À cause des alliances, les pays entrent en guerre les uns après les autres. Début août, l'affiche de la <b>mobilisation générale</b> est collée dans chaque commune : les hommes partent rejoindre l'armée.</p>"
      "<h4>Légende ou réalité ?</h4><p>Les cartes postales montrent des soldats joyeux, « la fleur au fusil ». En réalité, la plupart partent tristes mais décidés à faire leur devoir. Tout le monde croit que la guerre sera courte.</p>",
      F.html(F.LECON_CAUSES),
      [("alliance", "accord entre des pays qui promettent de s'aider en cas de guerre"), ("attentat", "attaque violente contre une personne ou un lieu, pour des raisons politiques"),
       ("mobilisation", "appel des hommes en âge de combattre pour qu'ils rejoignent l'armée"), ("déclaration de guerre", "annonce officielle qu'un pays entre en guerre contre un autre"),
       ("propagande", "images et textes qui cherchent à influencer l'opinion")],
      "Deux alliances face à face en 1914", camps(), BO + " ; Musée de l'Armée, « L'affiche de mobilisation » (2025) ; " + CDM + "."),
    L("front", 2, "Le front et les tranchées",
      ["Décrire une tranchée et la vie quotidienne des poilus", "Situer deux batailles emblématiques : Verdun et la Somme (1916)",
       "Connaître les armes nouvelles", "Savoir que des soldats venus des colonies ont combattu pour la France"],
      "<h4>La guerre des tranchées</h4><p>À la fin de 1914, les armées creusent des <b>tranchées</b> : des fossés protégés par des sacs de sable et des barbelés. Le front va de la mer du Nord à la Suisse.</p>"
      "<h4>La vie des poilus</h4><p>Les soldats français, les <b>poilus</b>, vivent dans la boue et le froid. Les lettres et les colis de leur famille, et l'amitié entre camarades, les aident à tenir.</p>"
      "<h4>De grandes batailles</h4><p>En 1916, les batailles de <b>Verdun</b> et de la <b>Somme</b> durent des mois. On utilise des armes nouvelles : mitrailleuses, gaz, avions, chars. Des soldats venus des <b>colonies</b> combattent aux côtés des soldats de France.</p>",
      F.html(F.LECON_FRONT),
      [("tranchée", "fossé creusé pour se protéger, où vivent les soldats du front"), ("poilu", "surnom des soldats français de la Grande Guerre"),
       ("front", "ligne où les armées se font face et combattent"), ("censure", "contrôle des lettres et des journaux par les autorités"),
       ("tirailleur", "soldat d'une unité recrutée dans les colonies, par exemple les tirailleurs sénégalais")],
      "Coupe d'une tranchée", tranchee(5, avec_noms=True), BO + " ; " + CDM + " ; Encyclopædia Universalis, « Le rôle des colonies »."),
    L("arriere", 3, "L'arrière : tout un pays en guerre",
      ["Savoir ce qu'est l'arrière", "Décrire le rôle des femmes dans les champs et les usines",
       "Comprendre l'économie de guerre", "CM2 : citer des chiffres (430 000 munitionnettes en 1918) et le rôle des travailleurs venus d'ailleurs"],
      "<h4>Tout un pays en guerre</h4><p>L'<b>arrière</b>, c'est tout le pays loin du front : les villes, les villages, les usines, les champs. Les usines fabriquent des obus et des canons : c'est l'<b>économie de guerre</b>.</p>"
      "<h4>Les femmes</h4><p>Les femmes remplacent les hommes partis : elles font les moissons, fabriquent des obus (on les appelle les <b>munitionnettes</b>), conduisent les tramways, soignent les blessés. Pourtant, elles n'ont pas encore le droit de vote.</p>"
      "<h4>Les enfants</h4><p>À l'école, les élèves écrivent aux soldats et collectent des vêtements. Des travailleurs venus des colonies et d'autres pays travaillent aussi dans les usines.</p>",
      F.html(F.LECON_ARRIERE),
      [("arrière", "partie du pays éloignée des combats"), ("munitionnette", "ouvrière qui fabrique des obus"),
       ("économie de guerre", "économie où les usines produisent surtout pour l'armée"), ("obus", "projectile tiré par un canon"),
       ("droit de vote", "droit de choisir ses représentants par une élection ; les Françaises l'obtiennent en 1944")],
      "Le front et l'arrière", front_arriere(), BO + " ; Encyclopædia Universalis, « Grande Guerre et société » ; " + CDM + "."),
    L("armistice", 4, "1918 : l'armistice et la paix",
      ["Dater l'armistice du 11 novembre 1918 et le traité de Versailles (1919)", "Distinguer armistice et paix",
       "Connaître le bilan humain avec des chiffres officiels", "CM2 : les clauses du traité et la colère des vaincus"],
      "<h4>La fin des combats</h4><p>En 1917, les <b>États-Unis</b> entrent en guerre aux côtés de la France. Le <b>11 novembre 1918</b>, l'<b>armistice</b> est signé : à 11 heures, les cloches sonnent dans toute la France, les combats s'arrêtent.</p>"
      "<h4>La paix</h4><p>La paix est signée l'année suivante, en 1919, à <b>Versailles</b>. L'Alsace et la Moselle redeviennent françaises.</p>"
      "<h4>Un bilan très lourd</h4><p>Près de <b>1,4 million</b> de soldats français sont morts. Beaucoup de familles ont perdu un père, un fils, un frère.</p>",
      F.html(F.LECON_ARMI),
      [("armistice", "accord qui arrête les combats, avant la signature de la paix"), ("traité", "accord écrit et signé entre des pays"),
       ("réparations", "argent que le pays vaincu doit payer pour les destructions"), ("veuve", "femme dont le mari est mort"), ("orphelin", "enfant qui a perdu son père ou sa mère")],
      "Frise de 1914 à 1922", frise(), BO + " ; " + CDM + " ; Musée de l'Armée.",
      document={"type": "texte", "titre": "Repères chiffrés (chiffres officiels)",
                "contenu": "Français mobilisés de 1914 à 1918 : 8,7 millions. Soldats français morts : près de 1,4 million. Veuves de guerre en France : près de 600 000. Armistice : 11 novembre 1918, signé à 5 h 15 à Rethondes ; fin des combats à 11 heures. Traité de Versailles : 28 juin 1919.",
                "source": "Ministère des Armées, Chemins de mémoire (« Un deuil national », « 11 novembre ») ; musée de l'Armée."}),
    L("memoire", 5, "Se souvenir, et une paix fragile",
      ["Comprendre le rôle du monument aux morts et du 11 novembre", "Savoir enquêter sur les noms d'un monument (Mémoire des hommes)",
       "CM2 : décrire les conséquences de la guerre", "CM2 : comprendre comment des régimes autoritaires profitent de la colère (Italie, 1922)"],
      "<h4>Le monument aux morts</h4><p>Après la guerre, presque chaque commune de France construit un <b>monument aux morts</b>. On y grave les noms des soldats de la commune « morts pour la France ».</p>"
      "<h4>Le 11 novembre</h4><p>Chaque année, le <b>11 novembre</b>, jour férié, on se rassemble devant le monument pour se souvenir. À Paris, le <b>Soldat inconnu</b> repose sous l'Arc de Triomphe.</p>"
      "<h4>Une paix fragile</h4><p>La guerre laisse des destructions, des familles en deuil et de la colère. Dans certains pays, des chefs promettent l'ordre par la force et suppriment les libertés.</p>",
      F.html(F.LECON_MEMOIRE),
      [("monument aux morts", "monument qui porte les noms des soldats d'une commune morts à la guerre"), ("commémorer", "se rassembler pour se souvenir ensemble"),
       ("mort pour la France", "mention officielle donnée aux soldats morts au service de la France"), ("régime autoritaire", "pouvoir qui supprime les libertés et ne tolère pas d'opposition"),
       ("extrémiste", "qui veut imposer ses idées par la force")],
      "Le monument aux morts", monument(5, avec_noms=True), BO + " ; " + CDM + " ; info.gouv.fr ; Mémoire des hommes ; ONACVG et Eduscol."),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
