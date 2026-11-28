# -*- coding: utf-8 -*-
"""Génère napoleon-republique/assets/data/enigmes.json (Le Testament de l'Empereur). Lancer : python gen_enigmes.py <dossier data>
Bilan nuancé de l'Empire (réformes, mais guerres, autoritarisme, rétablissement de l'esclavage en 1802) ; aucune scène de combat ;
personnages inventés ; les personnes réelles ne parlent jamais. Salle 5 : symboles, lieux et rites de la République ; les lois
protectrices des droits sont traitées dans les jeux « Le Secret de la Déclaration » et « Le Sceau de la République » (renvoi)."""
import json, os, sys
from schemas import carte_europe, sacre, place

BO = "Programme d'histoire du cycle 3 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026), le temps de la Révolution et de l'Empire (niveau à confirmer, cf. A-VERIFIER.md) ; progression de l'enseignant : thème 4, année B, période 4"
FN = "Fondation Napoléon, napoleon.org (chronologies, dossiers « Masses de granit » et « Le Sacre »)"
MA = "Musée de l'Armée, Hôtel national des Invalides"
LOUVRE = "Musée du Louvre, Jacques-Louis David, « Sacre de l'empereur Napoléon Ier et couronnement de l'impératrice Joséphine »"
BDF = "Banque de France, « Histoire de la Banque de France »"
ELY = "Présidence de la République (elysee.fr), « La Marseillaise de Rouget de Lisle » et « Les symboles de la République »"
CONST = "Constitution du 4 octobre 1958, article 2 (Légifrance) ; vie-publique.fr, « Quels sont les symboles de la Ve République ? »"
HPI = "Histoire par l'image (Réunion des musées nationaux) et Eduscol, ressources sur le Consulat et l'Empire"

