/* ============================================================
   APPLICATION INSTALLABLE — enregistrement du service worker (A4)
   Chargé par l'accueil et par chaque jeu. Sans effet en double-clic
   (file://) ou dans un navigateur sans service worker.
   ============================================================ */
(function(){
  if(!("serviceWorker" in navigator) || !/^https?:$/.test(location.protocol)) return;
  const ici = document.currentScript && document.currentScript.src;
  const racine = ici ? new URL("../../", ici).href : new URL(location.pathname.split("/").length > 2 ? "../" : "./", location.href).href;
  window.addEventListener("load", () => {
    navigator.serviceWorker.register(racine + "sw.js", { scope: racine }).catch(e => console.info("Hors connexion indisponible :", e.message));
  });
})();
