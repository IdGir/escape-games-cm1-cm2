"""Tests de la production de médias (outils/medias) avec un FAUX service local : aucun réseau externe, aucune vraie clé.

Vérifie : sources décrites en JSON (Agnes et une source « inconnue » ajoutée sans code), clé envoyée dans l'en-tête et jamais
écrite dans les journaux, reprises sur file pleine (503) et quota (429), vidéo (création → sondage → téléchargement), adaptateur Python,
plafonds, import d'images comme fond / portrait / départ de vidéo, import par dossier, mise à jour de medias.csv et des crédits.
Lancement : python -m unittest vingt-mille-lieues/tests/test_medias_sources.py   (ou node tests/test-medias-sources.js)
"""
import base64, csv, io, json, os, shutil, struct, subprocess, sys, tempfile, threading, unittest, zlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

os.environ["MEDIAS_DELAI_S"] = "0.01"
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(ICI), "outils", "medias"))
import medias_lib as L

CLE = "cle-de-test-0123456789"


def png(largeur=64, hauteur=36, rgb=(200, 120, 40)):
    brut = b"".join(b"\x00" + bytes(rgb) * largeur for _ in range(hauteur))
    def bloc(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    return b"\x89PNG\r\n\x1a\n" + bloc(b"IHDR", struct.pack(">IIBBBBB", largeur, hauteur, 8, 2, 0, 0, 0)) + bloc(b"IDAT", zlib.compress(brut)) + bloc(b"IEND", b"")


class Faux(BaseHTTPRequestHandler):
    etat = {}

    def log_message(self, *a):
        pass

    def _json(self, code, d):
        corps = json.dumps(d).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def _corps(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}")

    def do_HEAD(self):
        self.send_response(200 if self.path.startswith("/pub/") else 404)
        self.end_headers()

    def do_GET(self):
        e = Faux.etat
        if self.path.startswith("/files/"):
            data = png() if self.path.endswith(".png") else b"FAKEMP4-DATA"
            self.send_response(200); self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data); return
        if self.path.startswith("/agnesapi") or self.path.startswith("/video/jobs/"):
            e["sondages"] = e.get("sondages", 0) + 1
            if e["sondages"] == 1:
                return self._json(429, {"error": "too many video status queries"})
            if e["sondages"] == 2:
                return self._json(200, {"status": "processing", "job": {"state": "running"}})
            return self._json(200, {"status": "completed", "url": f"http://127.0.0.1:{self.server.server_port}/files/clip.mp4",
                                    "job": {"state": "done", "output": {"url": f"http://127.0.0.1:{self.server.server_port}/files/clip.mp4"}}})
        self._json(404, {})

    def do_POST(self):
        e = Faux.etat
        corps = self._corps()
        e.setdefault("requetes", []).append({"chemin": self.path, "en_tetes": dict(self.headers), "corps": corps})
        if self.path == "/v1/images/generations":
            if self.headers.get("Authorization") != "Bearer " + CLE:
                return self._json(401, {"error": "cle refusee"})
            e["img"] = e.get("img", 0) + 1
            if e["img"] == 1:
                return self._json(503, {"error": "upstream request failed"})
            return self._json(200, {"data": [{"b64_json": base64.b64encode(png()).decode()}]})
        if self.path == "/v1/videos":
            e["vid"] = e.get("vid", 0) + 1
            if e["vid"] == 1:
                return self._json(503, {"code": "video_queue_full", "message": "video queue is full"})
            return self._json(200, {"video_id": "job-1"})
        if self.path == "/generate":
            if self.headers.get("X-Api-Key") != CLE:
                return self._json(401, {"error": "x"})
            return self._json(200, {"result": {"image_url": f"http://127.0.0.1:{self.server.server_port}/files/img.png"}})
        if self.path == "/video/jobs":
            if self.headers.get("X-Api-Key") != CLE:
                return self._json(401, {"error": "x"})
            return self._json(200, {"job": {"id": "j9"}})
        self._json(404, {})


class TestSources(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.serveur = ThreadingHTTPServer(("127.0.0.1", 0), Faux)
        cls.port = cls.serveur.server_port
        threading.Thread(target=cls.serveur.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.serveur.shutdown()

    def setUp(self):
        Faux.etat.clear()
        self.tmp = tempfile.mkdtemp()
        L.JEU, L.SORTIE = self.tmp, os.path.join(self.tmp, "assets", "medias-proposes")
        L.JOURNAL = os.path.join(L.SORTIE, "generation.log")
        L.FICHIER_SOURCES = os.path.join(self.tmp, "sources-test.json")
        L.FICHIER_CLES = os.path.join(self.tmp, "cles-api.local")
        base = f"http://127.0.0.1:{self.port}"
        reg = json.load(open(os.path.join(os.path.dirname(ICI), "outils", "medias", "sources-medias.json"), encoding="utf-8"))
        reg["sources"]["agnes"]["base_url"] = base
        reg["sources"]["agnes"]["cle"]["optionnelle"] = False
        reg["sources"]["agnes"]["video"]["sonder"]["intervalle_s"] = 0.01
        reg["sources"]["agnes"]["video"]["depart"] = {"mode": "data-uri"}
        # une source AJOUTÉE SANS CODE : autres noms de champs, autre en-tête de clé
        reg["sources"]["service-neuf"] = json.loads(json.dumps(reg["sources"]["exemple-http-generique"]).replace("https://api.exemple.fr", base))
        reg["sources"]["service-neuf"]["video"]["sonder"]["intervalle_s"] = 0.01
        reg["hebergement_images"] = {"mode": "url-base", "url_base": base + "/pub"}
        json.dump(reg, open(L.FICHIER_SOURCES, "w", encoding="utf-8"))
        os.environ["AGNES_API_KEY"] = CLE
        os.environ["EXEMPLE_API_KEY"] = CLE
        with open(os.path.join(self.tmp, "medias.csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["id", "type", "fichier", "dimensions", "duree", "ratio", "escale", "reference_ou_depart", "statut", "zones", "effets_moteur", "prompt_fr", "prompt_en", "negatif"])
            w.writerow(["decor-atelier", "image", "assets/images/decors/atelier.webp", "1920×1080", "", "16:9", "1", "", "à produire", "", "", "Un atelier d'imprimeur", "", "texte"])
            w.writerow(["portrait-tommaso", "image", "assets/images/personnages/tommaso.webp", "1200×1600", "", "3:4", "toutes", "", "à produire", "", "", "Un apprenti", "", ""])
            w.writerow(["video-transition-e1", "vidéo", "assets/videos/transition-e1.mp4", "1280×720", "8 s", "16:9", "1", "", "à produire", "", "", "Travelling avant", "", ""])
        os.makedirs(os.path.join(self.tmp, "assets", "medias-depart"), exist_ok=True)
        open(os.path.join(self.tmp, "assets", "medias-depart", "transition-e1.jpg"), "wb").write(png())

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def produire(self, *args):
        sys.argv = ["produire.py"] + list(args)
        import importlib
        import produire
        importlib.reload(produire)
        sortie = io.StringIO()
        ancien, sys.stdout = sys.stdout, sortie
        try:
            produire.main()
        except SystemExit as e:
            sys.stdout = ancien
            return str(e.code), sortie.getvalue()
        finally:
            sys.stdout = ancien
        return None, sortie.getvalue()

    # ---- images
    def test_image_agnes_avec_reprise_et_cle(self):
        err, _ = self.produire("--id", "decor-atelier")
        self.assertIsNone(err)
        fichier = os.path.join(L.SORTIE, "decor-atelier-v1.webp")
        self.assertTrue(os.path.isfile(fichier), "l'image doit être reçue après une reprise sur 503")
        self.assertEqual(Faux.etat["img"], 2, "une reprise après le 503")
        r = Faux.etat["requetes"][-1]
        self.assertEqual(r["en_tetes"]["Authorization"], "Bearer " + CLE, "la clé est envoyée dans l'en-tête")
        self.assertEqual(r["corps"]["model"], "agnes-image-2.5-flash")
        self.assertEqual(r["corps"]["ratio"], "16:9")
        self.assertEqual(r["corps"]["size"], "2K")
        self.assertNotIn("image", r["corps"].get("extra_body", {}), "pas de référence : le champ est retiré")
        dim = subprocess.run(["identify", "-format", "%wx%h", fichier], capture_output=True, text=True).stdout
        self.assertEqual(dim, "1920x1080", "recadrée au format du décor")

    def test_la_cle_n_apparait_jamais(self):
        self.produire("--id", "decor-atelier")
        tout = open(L.JOURNAL, encoding="utf-8").read()
        for racine, _, fichiers in os.walk(self.tmp):
            for f in fichiers:
                if f.endswith((".log", ".json", ".csv", ".md")):
                    tout += open(os.path.join(racine, f), encoding="utf-8", errors="ignore").read()
        self.assertNotIn(CLE, tout)
        self.assertEqual(L.masquer(f"erreur {CLE} fin").count(CLE), 0, "masquer() retire les clés connues")

    def test_cle_absente_message_clair(self):
        del os.environ["AGNES_API_KEY"]
        err, _ = self.produire("--id", "decor-atelier")
        self.assertIn("AGNES_API_KEY", err or "")
        self.assertNotIn("Traceback", err or "")

    def test_cle_lue_dans_le_fichier_local_jamais_publie(self):
        del os.environ["AGNES_API_KEY"]
        open(L.FICHIER_CLES, "w").write(f"# commentaire\nAGNES_API_KEY={CLE}\n")
        err, _ = self.produire("--id", "decor-atelier")
        self.assertIsNone(err)
        self.assertTrue(os.path.isfile(os.path.join(L.SORTIE, "decor-atelier-v1.webp")))

    def test_plafond_d_images(self):
        err, sortie = self.produire("--id", "decor-atelier", "--id", "portrait-tommaso", "--max-images", "1")
        self.assertIsNone(err)
        self.assertIn("plafond", sortie)
        self.assertFalse(os.path.isfile(os.path.join(L.SORTIE, "portrait-tommaso-v1.webp")))

    def test_essai_n_appelle_rien(self):
        _, sortie = self.produire("--essai", "--id", "decor-atelier")
        self.assertIn("[essai]", sortie)
        self.assertNotIn("requetes", Faux.etat)

    # ---- nouvelle source ajoutée sans code
    def test_source_ajoutee_sans_code(self):
        err, _ = self.produire("--source-image", "service-neuf", "--id", "decor-atelier")
        self.assertIsNone(err, err)
        r = Faux.etat["requetes"][-1]
        self.assertEqual(r["chemin"], "/generate")
        self.assertEqual(r["en_tetes"].get("X-Api-Key"), CLE, "en-tête et format de clé propres à la source")
        self.assertEqual(r["corps"]["text"], "Un atelier d'imprimeur")
        self.assertEqual(r["corps"]["aspect"], "16:9")
        self.assertTrue(os.path.isfile(os.path.join(L.SORTIE, "decor-atelier-v1.webp")), "image récupérée par URL")

    def test_adaptateur_python(self):
        ad = os.path.join(self.tmp, "mon_adaptateur.py")
        open(ad, "w").write("import base64\ndef produire_image(source, prompt, ratio, taille, refs, negatif=''):\n    return base64.b64decode('%s')\n" % base64.b64encode(png()).decode())
        reg = json.load(open(L.FICHIER_SOURCES))
        reg["sources"]["bizarre"] = {"nom": "Service hors cadre", "adaptateur": ad}
        json.dump(reg, open(L.FICHIER_SOURCES, "w"))
        err, _ = self.produire("--source-image", "bizarre", "--id", "decor-atelier")
        self.assertIsNone(err, err)
        self.assertTrue(os.path.isfile(os.path.join(L.SORTIE, "decor-atelier-v1.webp")))

    # ---- vidéos
    def test_video_file_pleine_quota_puis_telechargement(self):
        err, _ = self.produire("--types", "video", "--id", "video-transition-e1", "--max-videos", "1")
        self.assertIsNone(err, err)
        self.assertEqual(open(os.path.join(L.SORTIE, "video-transition-e1-v1.mp4"), "rb").read(), b"FAKEMP4-DATA")
        creation = [r for r in Faux.etat["requetes"] if r["chemin"] == "/v1/videos"][-1]["corps"]
        self.assertEqual(creation["model"], "agnes-video-2.5-flash")
        self.assertEqual(creation["mode"], "keyframe")
        self.assertTrue(creation["first_frame"].startswith("data:image/jpeg;base64,"), "image de départ transmise selon le mode de la source")
        self.assertNotIn("last_frame", creation, "champ absent retiré")
        self.assertEqual(Faux.etat["vid"], 2, "reprise après « video_queue_full »")
        self.assertGreaterEqual(Faux.etat["sondages"], 3, "reprise après un 429 de sondage")
        jobs = json.load(open(os.path.join(L.SORTIE, "jobs.json")))
        self.assertTrue(all(j["fini"] for j in jobs.values()))

    def test_plafond_de_videos_par_defaut_zero(self):
        err, sortie = self.produire("--types", "video", "--id", "video-transition-e1")
        self.assertIsNone(err)
        self.assertIn("plafond de vidéos", sortie)
        self.assertNotIn("requetes", Faux.etat)

    def test_depart_pris_dans_un_decor_depose(self):
        dec = os.path.join(self.tmp, "assets", "images", "decors")
        os.makedirs(dec)
        L.convertir_image_orig = L.convertir_image
        open(os.path.join(self.tmp, "src.png"), "wb").write(png(160, 90))
        L.convertir_image(os.path.join(self.tmp, "src.png"), os.path.join(dec, "atelier.webp"), 1920, 1080)
        os.remove(os.path.join(self.tmp, "assets", "medias-depart", "transition-e1.jpg"))
        err, _ = self.produire("--types", "video", "--id", "video-transition-e1", "--max-videos", "1", "--depart-decor", "atelier")
        self.assertIsNone(err, err)
        dim = subprocess.run(["identify", "-format", "%wx%h", os.path.join(self.tmp, "assets", "medias-depart", "transition-e1.jpg")], capture_output=True, text=True).stdout
        self.assertEqual(dim, "1280x720")

    def test_depart_non_publie_refuse_clairement(self):
        reg = json.load(open(L.FICHIER_SOURCES))
        reg["sources"]["agnes"]["video"]["depart"] = {"mode": "url"}
        reg["hebergement_images"] = {"mode": "url-base", "url_base": f"http://127.0.0.1:{self.port}/absent"}
        json.dump(reg, open(L.FICHIER_SOURCES, "w"))
        err, _ = self.produire("--types", "video", "--id", "video-transition-e1", "--max-videos", "1")
        self.assertIn("pas encore publique", err or "")
        self.assertNotIn("/v1/videos", [r["chemin"] for r in Faux.etat.get("requetes", [])], "rien n'est demandé tant que l'image n'est pas publique")

    # ---- import d'images faites ailleurs
    def importer(self, *args):
        sys.argv = ["importer-image.py"] + list(args)
        import importlib
        import importlib.util
        spec = importlib.util.spec_from_file_location("importer_image", os.path.join(os.path.dirname(ICI), "outils", "medias", "importer-image.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.main()

    def test_importer_decor_et_depart(self):
        src = os.path.join(self.tmp, "midjourney.png")
        open(src, "wb").write(png(320, 240))
        self.importer(src, "--decor", "atelier", "--depart", "transition-e9", "--source", "Midjourney v6", "--licence", "droits du compte")
        d = subprocess.run(["identify", "-format", "%wx%h", os.path.join(self.tmp, "assets", "images", "decors", "atelier.webp")], capture_output=True, text=True).stdout
        j = subprocess.run(["identify", "-format", "%wx%h", os.path.join(self.tmp, "assets", "medias-depart", "transition-e9.jpg")], capture_output=True, text=True).stdout
        self.assertEqual((d, j), ("1920x1080", "1280x720"))
        lignes = list(csv.DictReader(open(os.path.join(self.tmp, "medias.csv"), encoding="utf-8"), delimiter=";"))
        self.assertTrue(next(l for l in lignes if l["id"] == "decor-atelier")["statut"].startswith("déposé (Midjourney v6"))
        credits = open(os.path.join(self.tmp, "assets", "medias", "CREDITS-medias.md"), encoding="utf-8").read()
        self.assertIn("Midjourney v6", credits)
        self.assertIn("droits du compte", credits)

    def test_importer_portrait_depuis_une_adresse(self):
        self.importer(f"http://127.0.0.1:{self.port}/files/x.png", "--portrait", "tommaso", "--source", "ChatGPT")
        d = subprocess.run(["identify", "-format", "%wx%h", os.path.join(self.tmp, "assets", "images", "personnages", "tommaso.webp")], capture_output=True, text=True).stdout
        self.assertEqual(d, "1200x1600")

    def test_importer_dossier_par_noms_de_fichiers(self):
        dossier = os.path.join(self.tmp, "assets", "medias-a-importer")
        os.makedirs(dossier)
        open(os.path.join(dossier, "decor-atelier.png"), "wb").write(png(300, 200))
        open(os.path.join(dossier, "portrait-tommaso.png"), "wb").write(png(300, 400))
        open(os.path.join(dossier, "video-transition-e1.mp4"), "wb").write(b"CLIP")
        open(os.path.join(dossier, "n-importe-quoi.png"), "wb").write(png())
        self.importer("--dossier", dossier)
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, "assets", "images", "decors", "atelier.webp")))
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, "assets", "images", "personnages", "tommaso.webp")))
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, "assets", "videos", "transition-e1.mp4")))
        self.assertTrue(os.path.isfile(os.path.join(dossier, "n-importe-quoi.png")), "fichier au nom inconnu laissé en place")
        self.assertTrue(os.path.isfile(os.path.join(dossier, "importes", "decor-atelier.png")), "fichiers traités rangés")


class TestRemplir(unittest.TestCase):
    def test_modeles(self):
        v = {"prompt": "chat", "refs": ["a", "b"], "ratio": None}
        self.assertEqual(L.remplir({"p": "{prompt}", "l": "{refs}", "r": "{ratio}", "t": "x {prompt} y"}, v), {"p": "chat", "l": ["a", "b"], "t": "x chat y"})
        self.assertEqual(L.extraire({"data": [{"b64": "ok"}]}, "data.0.b64"), "ok")
        self.assertIsNone(L.extraire({"data": []}, "data.0.b64"))


if __name__ == "__main__":
    unittest.main()
