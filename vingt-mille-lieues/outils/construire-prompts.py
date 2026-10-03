#!/usr/bin/env python3
"""Construit PRODUCTION-MEDIAS.md et medias.csv à partir d'une SOURCE UNIQUE (ce fichier).

Pourquoi : la charte, les fiches personnages et la silhouette canonique du Nautilus doivent être
recopiées MOT POUR MOT dans chaque prompt ; les écrire une seule fois évite les variantes.
Usage : python vingt-mille-lieues/outils/construire-prompts.py
"""
import csv, io, os

ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)

STYLE_FR = ("peinture numérique semi-réaliste, gravure rétro-futuriste victorienne, laiton, bois, verre, "
            "lumière bleu-vert et ambre, contraste chaud/froid (lampes ambrées contre bleu des hublots), matières nobles, "
            "détails narratifs, rendu cinéma, grain léger, profondeur de champ")
STYLE_EN = ("semi-realistic digital painting, Victorian retro-futuristic engraving mood, brass, mahogany wood, glass, "
            "teal-blue and amber light, warm/cold contrast (amber lamps against the blue glow of portholes), noble materials, "
            "rich narrative details, cinematic rendering, subtle film grain, shallow depth of field")
MOTIFS_FR = ("appliques en coquille Saint-Jacques lumineuses, hublots ronds de laiton rivetés, lampes à abat-jour vert, "
             "fauteuils capitonnés de cuir vert, tapis orientaux, laiton et cuivre")
MOTIFS_EN = ("glowing scallop-shell wall sconces, round riveted brass portholes, green-shaded banker lamps, "
             "green tufted leather armchairs, oriental rugs, brass and copper fittings")
INTERDITS_FR = "pas de texte, pas de lettres, pas de logo, pas de filigrane, pas de personne réelle, pas de nom d'artiste"
INTERDITS_EN = "no text, no letters, no logo, no watermark, no real person"
RESERVE_FR = "bas de l'image (20 %) plus sombre et dégagé pour la plaque de dialogue"
RESERVE_EN = "keep the bottom 20% of the frame darker and uncluttered for the dialogue panel"
NAUTILUS_FR = ("le Nautilus : long fuseau cylindro-conique de tôle rivetée gris acier patiné, une rangée de hublots ronds "
               "éclairés d'ambre le long de la coque, une petite cage du pilote vitrée en laiton à facettes sur le dos, "
               "un fanal électrique, un canot encastré dans la coque, rambardes de laiton, aucune cheminée, aucune voile, aucun mât de navire à voile")
NAUTILUS_EN = ("the Nautilus: a long cylindro-conical spindle hull of weathered riveted steel plates, one row of round amber-lit "
               "portholes along the hull, a small faceted brass-and-glass pilot cage on its back, an electric searchlight, "
               "a dinghy recessed into the hull, brass railings, no funnel, no sails, no sailing masts")

PERSOS = {
    "nemo": ("Le capitaine Nemo : homme d'une cinquantaine d'années, cheveux gris plaqués en arrière, barbe poivre et sel taillée, "
             "regard grave, intense et mélancolique ; long manteau (redingote) bleu marine à double rang de boutons dorés, gilet et col "
             "blancs sobres, chaîne de montre ; posture droite, mains dans le dos.",
             "Captain Nemo: a man in his fifties, grey hair slicked back, neatly trimmed salt-and-pepper beard, grave, intense and "
             "melancholic gaze; long navy-blue double-breasted frock coat with gold buttons, plain white waistcoat and collar, watch chain; "
             "upright posture, hands behind his back."),
    "aronnax": ("Le professeur Aronnax : savant français d'environ 40 ans, cheveux bruns légèrement grisonnants aux tempes, moustache et "
                "favoris soignés, regard curieux ; redingote brune, gilet, cravate nouée, carnet de notes et crayon à la main.",
                "Professor Aronnax: a French naturalist about 40, brown hair slightly greying at the temples, neat moustache and side-whiskers, "
                "curious eyes; brown frock coat, waistcoat, knotted cravat, notebook and pencil in hand."),
    "conseil": ("Conseil : domestique flamand d'environ 30 ans, flegmatique, cheveux châtain clair bien peignés, rasé de près, petites "
                "lunettes rondes cerclées de métal ; tenue de serviteur soignée : veste sombre ajustée, gilet, col blanc, nœud discret.",
                "Conseil: a phlegmatic Flemish manservant about 30, light-brown neatly combed hair, clean-shaven, small round metal-rimmed "
                "glasses; tidy servant's outfit: fitted dark jacket, waistcoat, white collar, discreet bow."),
    "ned": ("Ned Land : harponneur canadien d'environ 40 ans, grand et large d'épaules, visage hâlé, barbe courte rousse, sourcils épais ; "
            "bonnet de laine, chemise de marin à col ouvert, gilet de cuir, harpon à la main.",
            "Ned Land: a Canadian harpooner about 40, tall and broad-shouldered, weathered tanned face, short red beard, thick eyebrows; "
            "wool cap, open-collared sailor's shirt, leather vest, harpoon in hand."),
}

NEG = "texte, lettres, logo, filigrane, mains déformées, doigts en trop, visage déformé, flou, cheminée, voiles, charbon (décors du Nautilus), style dessin animé"
NEG_EN = "text, letters, logo, watermark, deformed hands, extra fingers, distorted face, blur, smokestack, sails, coal (Nautilus interiors), cartoon style"

# id, type, fichier, dimensions, durée, ratio, escale, référence/départ, statut, zones, effets, description FR, description EN
M = []
def ajoute(**k): M.append(k)

for pid, (fr, en) in PERSOS.items():
    ajoute(id="portrait-" + pid, type="image", fichier=f"assets/images/personnages/{pid}.webp", dim="1200×1600", duree="", ratio="3:4",
           escale="toutes", ref=("references/personnage-nemo-1.png, references/personnage-nemo-2.png" if pid == "nemo" else "references/style-cabine-capitaine-1.png, references/style-salle-officiers-2.png"),
           statut="secours actif (portrait dessiné)", zones="", effets="respiration, clignement, bouche animée (moteur)",
           fr=f"Portrait de référence, plan taille, cadrage vertical, fond flou de boiseries et de hublot bleu. {fr} Photoréaliste de cinéma, lumière latérale bleue froide + ambre chaud." + ("" if pid == "nemo" else " Les images jointes ne servent que pour le décor et la lumière : aucune personne des images ne doit apparaître."),
           en=f"Reference portrait, waist-up, vertical framing, blurred background of dark wood paneling and a blue porthole. {en} Cinematic photorealism, cold blue side light plus warm amber light.")

ajoute(id="cadre-dialogue", type="image", fichier="assets/images/ui/cadre-dialogue.png", dim="1600×360 (PNG transparent)", duree="", ratio="40:9", escale="toutes",
       ref="références de salon et de cabine (matériaux)", statut="secours actif (cadre CSS)", zones="", effets="",
       fr="Plaque de dialogue horizontale vide en laiton patiné et acajou, bordure rivetée, coins ornés de petites coquilles, centre lisse et sombre pour le texte, fond transparent.",
       en="Empty horizontal dialogue plaque in weathered brass and mahogany, riveted border, small shell ornaments at the corners, smooth dark centre for text, transparent background.")

DECORS = [
    ("salon", 2, "references/style-salon-nautilus.png", "épure (divan centre), hublots, orgue, vitrines",
     "caustiques au sol, poissons derrière les hublots, scintillement du lustre, poussière, vignette",
     "Le grand salon-musée du Nautilus en enfilade, perspective centrale symétrique : boiseries sombres cirées, parquet en point de Hongrie, tapis à médaillon, lustre à pendeloques, double étage de bibliothèques à galerie, grand orgue au fond entre deux hublots ronds géants sur l'océan bleu turquoise, vitrines de coraux et de coquillages au premier plan, un divan de cuir vert au centre-fond avec un plan roulé posé dessus.",
     "The Nautilus grand salon-museum seen in a long symmetrical central perspective: dark waxed wood paneling, herringbone parquet, medallion rug, crystal chandelier, two-storey galleried bookcases, a great pipe organ at the far end between two giant round portholes onto turquoise ocean, glass cabinets of corals and shells in the foreground, a green leather divan at the back centre with a rolled plan lying on it."),
    ("carre", 2, "references/style-salle-officiers-3.png", "table (objets), journal de bord, tableau des cadrans",
     "fumée (panne), étincelles au tableau, bulles au hublot, lueur de la lampe verte",
     "Le carré des officiers du Nautilus : intérieur métallique riveté vert-de-gris patiné avec lambris et tuyauteries de cuivre, tableau de manomètres et cadrans en haut à gauche, grande table de bois au premier plan couverte de cartes roussies, compas, règles, un verre de cristal, un bouchon, une plume, un journal de bord noirci à droite, lampe à abat-jour vert, petit hublot rond sur l'eau, horloge murale.",
     "The Nautilus officers' wardroom: riveted verdigris metal interior with wood wainscoting and copper pipes, a panel of pressure gauges top left, a large wooden table in the foreground covered with scorched charts, compasses, rulers, a crystal glass, a cork, a quill, a blackened logbook on the right, green-shaded lamp, small round porthole onto water, wall clock."),
    ("machines", 2, "references/composition-machines-electriques.png (rendu du décor dessiné, pour garder la place des objets cliquables)", "tableau de bornes (centre), accumulateurs (gauche), cadrans (droite)",
     "lueurs bleutées des bobines, étincelles (panne), rayons de lumière, poussière",
     "La salle des machines ÉLECTRIQUE du Nautilus : rangées d'accumulateurs de verre et de laiton à gauche, grand tableau de laiton au centre avec bornes, câbles gainés débranchés et petites ampoules, cadrans de contrôle à droite, grosses bobines de cuivre, câbles gainés au plafond voûté riveté, passerelle en caillebotis, lumière électrique bleutée, aucun charbon, aucune flamme, aucune chaudière.",
     "The Nautilus ELECTRIC engine room: rows of glass-and-brass accumulator cells on the left, a large brass switchboard in the centre with terminals, unplugged sheathed cables and small bulbs, control dials on the right, big copper coils, sheathed cables under a riveted vaulted ceiling, metal grating catwalk, bluish electric light, no coal, no flames, no boilers."),
    ("cabine", 2, "references/style-cabine-capitaine-2.png", "mur des instruments (droite), bureau, hublot",
     "méduses et poissons au hublot, caustiques, lueur de la lampe, poussière",
     "La chambre du capitaine Nemo : pièce intime en acajou sombre, grand hublot rond de laiton riveté au centre sur l'eau bleue avec méduses, bureau d'acajou couvert de plans, loupe et compas, lampe de banquier verte, mur d'instruments à droite (baromètre, horloges, manomètre, boussole, carte du ciel), lit-alcôve à rideaux de velours vert à gauche, fauteuil Chesterfield vert, clavier d'orgue à droite, tapis persan.",
     "Captain Nemo's private cabin: intimate dark mahogany room, a large round riveted brass porthole in the centre onto blue water with jellyfish, mahogany desk covered with plans, magnifier and compasses, green banker's lamp, a wall of instruments on the right (barometer, clocks, pressure gauge, compass, star chart), curtained alcove bed in green velvet on the left, green Chesterfield armchair, organ keyboard on the right, Persian rug."),
]
for did, esc, ref, zones, effets, fr, en in DECORS:
    ajoute(id="decor-" + did, type="image", fichier=f"assets/images/decors/{did}.webp", dim="1920×1080", duree="", ratio="16:9", escale=str(esc), ref=ref,
           statut="référence active" if did != "machines" else "secours actif (décor dessiné)", zones=zones, effets=effets,
           fr=fr + " Garder exactement la composition, la perspective et l'emplacement des objets de l'image de référence fournie.",
           en=en + " Keep exactly the composition, perspective and object placement of the provided reference image.")

A_VENIR = [("pont-lincoln", 1, "pont de la frégate Abraham Lincoln, 1867"), ("machines-vapeur", 1, "salle des machines à vapeur et charbon de la frégate (références salle-machines 1-4)"),
           ("pont-nautilus", 1, "pont du Nautilus en surface (références pont 1-3)"), ("sas", 3, "sas et vestiaire des scaphandres"), ("recif-crespo", 3, "forêt sous-marine de Crespo (références récif)"),
           ("vanikoro", 4, "récif de Vanikoro, épaves de Lapérouse"), ("banc-perles", 5, "banc d'huîtres perlières de Ceylan"), ("tunnel-suez", 6, "Arabian Tunnel, mer Rouge et isthme de Suez"),
           ("atlantide", 7, "temple englouti (références atlantide)"), ("sargasses", 8, "mer des Sargasses"), ("banquise", 9, "Nautilus dans la banquise (référence nautilus-banquise)"),
           ("plateforme-poulpe", 10, "combat contre les poulpes (référence nautilus-poulpe)"), ("vigo", 11, "baie de Vigo, galions engloutis"), ("maelstrom", 11, "Maelström (référence nautilus-maelstrom)"),
           ("salle-orgue", 11, "salle de l'orgue et coffre du capitaine (variante du salon)")]
for did, esc, desc in A_VENIR:
    ajoute(id="decor-" + did, type="image", fichier=f"assets/images/decors/{did}.webp", dim="1920×1080", duree="", ratio="16:9", escale=str(esc), ref="", statut=f"à produire avec l'escale {esc}",
           zones="à définir", effets="à définir", fr=f"À rédiger avec l'escale {esc} : {desc}.", en="")

ajoute(id="video-intro", type="vidéo", fichier="assets/videos/intro.mp4", dim="1280×720", duree="60-90 s", ratio="16:9", escale="1", ref="decor-pont-nautilus (validé)", statut="à produire après l'escale 1",
       zones="", effets="sous-titres et voix dans le code", fr="À rédiger avec l'escale 1 (la chasse au « monstre »).", en="")
ajoute(id="video-transition-e2", type="vidéo", fichier="assets/videos/transition-e2.mp4", dim="1280×720", duree="8-10 s", ratio="16:9", escale="2", ref="assets/images/decors/salon.webp (validé) en première image",
       statut="cinématique en direct active", zones="", effets="sous-titres et voix dans le code (dialogues.json)",
       fr="Image de départ : le grand salon validé. Lent travelling avant vers l'orgue ; les lampes du salon vacillent deux fois puis s'éteignent ; il ne reste que la lumière bleue des hublots ; une lueur rouge d'alarme pulse doucement. Aucun personnage ne parle, aucun texte.",
       en="Start frame: the approved grand salon. Slow push-in toward the organ; the salon lamps flicker twice then go out; only the blue light of the portholes remains; a soft red alarm glow pulses. No character speaking, no text.")
for n in [1] + list(range(3, 12)):
    ajoute(id=f"video-transition-e{n}", type="vidéo", fichier=f"assets/videos/transition-e{n}.mp4", dim="1280×720", duree="6-10 s", ratio="16:9", escale=str(n), ref="décor validé de l'escale",
           statut=f"à produire avec l'escale {n}", zones="", effets="sous-titres dans le code", fr=f"À rédiger avec l'escale {n}.", en="")
ajoute(id="video-fin", type="vidéo", fichier="assets/videos/fin.mp4", dim="1280×720", duree="45 s", ratio="16:9", escale="11", ref="decor-pont-nautilus", statut="à produire en fin de campagne", zones="", effets="", fr="À rédiger avec l'escale 11 (le Nautilus regagne la surface).", en="")
ajoute(id="video-bande-annonce", type="vidéo", fichier="assets/videos/bande-annonce.mp4", dim="1280×720", duree="15-20 s", ratio="16:9", escale="toutes", ref="décors validés", statut="à monter en fin de campagne", zones="", effets="", fr="Montage des décors validés (outils-medias/bande-annonce.py du dépôt, après intégration).", en="")


def prompt_image_en(m):
    return f"{m['en']} Style: {STYLE_EN}. Recurring motifs: {MOTIFS_EN}. {RESERVE_EN}. {INTERDITS_EN}."

def prompt_image_fr(m):
    return f"{m['fr']} Style : {STYLE_FR}. Motifs récurrents : {MOTIFS_FR}. {RESERVE_FR}. {INTERDITS_FR}."

def outils(m):
    if not m["en"]:
        return ""
    ar = "3:4" if m["ratio"] == "3:4" else ("16:9" if m["ratio"] == "16:9" else "4:1")
    en = prompt_image_en(m)
    ref = m["ref"]
    if m["type"] == "image":
        mj = f"{en} --ar {ar} --style raw --v <version courante> --no text, letters, watermark, logo" + (" --cref <URL du portrait validé> --sref <URL de references/style-salon-nautilus.png>" if "portrait" in m["id"] else " --sref <URL de references/style-salon-nautilus.png>")
        return f"""
**Midjourney** (anglais, paramètres en fin de ligne ; `--cref` = personnage, `--sref` = style ; mettre le numéro de version courant) :
```
{mj}
```
**Flux 1.1 Pro / Kontext** (phrases longues, ratio {ar}, image de référence pour la cohérence) — joindre : {ref or "—"}
```
{en}
```
**Imagen / Ideogram** (prompt naturel, ratio {ar}, rappeler « sans texte ») :
```
{en} Absolutely no text or lettering anywhere in the image.
```
**Agnes** (`agnes-image-2.5-flash`, `size: "2K"`, `ratio: "{ar}"`, `extra_body.image` = {ref or "aucune"} ; recadrer ensuite en {m['dim'].split(' ')[0]}) :
```
{prompt_image_fr(m)}
```
Prompt négatif : `{NEG}` · *Negative:* `{NEG_EN}`
"""
    return f"""
**Vidéo image→vidéo (Runway, Kling, Veo, Luma)** — image de départ : {ref} ; durée {m['duree']} ; boucle si possible ; aucun personnage qui parle ; aucun texte :
```
{m['en']}
```
**Agnes** (`agnes-video-2.5`, `mode: "keyframe"`, `first_frame` = URL publique du décor validé, `seconds: "8"`, `size: "720P"`, `aspect_ratio: "16:9"` ; tâche asynchrone : `video_id` puis `GET /agnesapi?video_id=…&model_name=agnes-video-2.5`) :
```
{m['fr']}
```
"""

ENTETE = open(os.path.join(ICI, "production-medias-entete.md"), encoding="utf-8").read()
corps = [ENTETE.format(STYLE_FR=STYLE_FR, STYLE_EN=STYLE_EN, MOTIFS_FR=MOTIFS_FR, MOTIFS_EN=MOTIFS_EN, INTERDITS_FR=INTERDITS_FR,
                       RESERVE_FR=RESERVE_FR, NAUTILUS_FR=NAUTILUS_FR, NAUTILUS_EN=NAUTILUS_EN,
                       PERSOS="\n".join(f"- **{k}** — {v[0]}\n  *EN :* {v[1]}" for k, v in PERSOS.items()))]
corps.append("\n## 5. Fiches média (une par fichier)\n")
corps.append("| Identifiant | Fichier exact | Dimensions | Durée | Escale | Statut |\n|---|---|---|---|---|---|")
for m in M:
    corps.append(f"| {m['id']} | `{m['fichier']}` | {m['dim']} | {m['duree'] or '—'} | {m['escale']} | {m['statut']} |")
for m in M:
    if not m["en"]:
        continue
    corps.append(f"\n### {m['id']} — `{m['fichier']}`\n")
    corps.append(f"- Dimensions : {m['dim']} · ratio {m['ratio']}{' · durée ' + m['duree'] if m['duree'] else ''} · escale {m['escale']} · statut : {m['statut']}")
    if m["zones"]:
        corps.append(f"- Zones interactives prévues : {m['zones']} (à recaler avec `outils/caler-effets.html`)")
    if m["effets"]:
        corps.append(f"- Effets ajoutés par le moteur (ne pas peindre) : {m['effets']}")
    corps.append(f"- Référence / image de départ : {m['ref'] or '—'}")
    corps.append("- Critères d'acceptation : lisible en 1280×720 ; aucun texte ; mains et visages corrects ; bas de l'image dégagé pour la plaque ; objets cliquables visibles et à leur place ; cohérence avec la charte et les fiches personnages.")
    corps.append(f"\n**Prompt (français)** :\n```\n{prompt_image_fr(m) if m['type'] == 'image' else m['fr']}\n```")
    corps.append(outils(m))
with open(os.path.join(JEU, "PRODUCTION-MEDIAS.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(corps).rstrip() + "\n")

buf = io.StringIO()
w = csv.writer(buf, delimiter=";", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
w.writerow(["id", "type", "fichier", "dimensions", "duree", "ratio", "escale", "reference_ou_depart", "statut", "zones", "effets_moteur", "prompt_fr", "prompt_en", "negatif"])
for m in M:
    w.writerow([m["id"], m["type"], m["fichier"], m["dim"], m["duree"], m["ratio"], m["escale"], m["ref"], m["statut"], m["zones"], m["effets"],
                prompt_image_fr(m) if (m["type"] == "image" and m["en"]) else m["fr"],
                prompt_image_en(m) if (m["type"] == "image" and m["en"]) else m["en"], NEG if m["type"] == "image" else ""])
with open(os.path.join(JEU, "medias.csv"), "w", encoding="utf-8", newline="") as f:
    f.write(buf.getvalue())
print(f"écrits : PRODUCTION-MEDIAS.md, medias.csv ({len(M)} médias)")
