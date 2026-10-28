/* Usina Vídeos · consentimento de cookies (RGPD / ePrivacy)
   Google Consent Mode v2 + Meta Pixel: nada de publicidade/estatística sem "Aceitar".
   Carregado em <head> ANTES do gtag.js e do pixel. Escolha guardada 6 meses. */
(function () {
  var KEY = 'uv_consent', MAX = 182 * 864e5;
  function read() {
    try { var o = JSON.parse(localStorage.getItem(KEY)); if (o && Date.now() - o.t < MAX) return o.v; } catch (e) {}
    return null;
  }
  function save(v) { try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {} }
  var v = read();
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { dataLayer.push(arguments); };
  var G = { ad_storage: 'granted', analytics_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted' };
  var D = { ad_storage: 'denied', analytics_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' };
  gtag('consent', 'default', Object.assign({ wait_for_update: 500 }, v === 'granted' ? G : D));
  window.uvConsent = function () { return v === 'granted'; };

  var L = (document.documentElement.lang || 'pt').slice(0, 2);
  var T = {
    pt: ['Usamos cookies para medir as visitas e mostrar anúncios relevantes (Google Analytics e Meta). Só os ativamos com a sua autorização.', 'Aceitar', 'Recusar', 'Saber mais', '/cookies/', 'Preferências de cookies'],
    en: ['We use cookies to measure visits and show relevant ads (Google Analytics and Meta). We only turn them on with your permission.', 'Accept', 'Decline', 'Learn more', '/cookies/#en', 'Cookie preferences'],
    es: ['Usamos cookies para medir las visitas y mostrar anuncios relevantes (Google Analytics y Meta). Solo las activamos con su permiso.', 'Aceptar', 'Rechazar', 'Más información', '/cookies/#es', 'Preferencias de cookies']
  };
  T = T[L] || T.pt;

  function decide(nv) {
    var was = v; v = nv; save(nv);
    gtag('consent', 'update', nv === 'granted' ? G : D);
    if (window.fbq) {
      fbq('consent', nv === 'granted' ? 'grant' : 'revoke');
      if (nv === 'granted' && was !== 'granted') fbq('track', 'PageView');
    }
    hide();
  }
  var box;
  function hide() { if (box) box.style.display = 'none'; }
  function show() {
    if (!box) {
      var css = document.createElement('style');
      css.textContent = '#uvck{position:fixed;left:16px;right:16px;bottom:16px;z-index:2147483000;max-width:560px;margin:0 auto;background:#141213;color:#EDE9E4;border:1px solid rgba(255,255,255,.14);border-top:4px solid #E5AE29;border-radius:16px;padding:18px 18px 16px;box-shadow:0 18px 50px rgba(0,0,0,.35);font:15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}' +
        '#uvck p{margin:0 0 14px;color:#EDE9E4}#uvck a{color:#E5AE29}#uvck .b{display:flex;gap:10px;flex-wrap:wrap}' +
        '#uvck button{flex:1 1 130px;min-height:44px;border-radius:999px;font:700 15px system-ui,sans-serif;cursor:pointer;border:1px solid #E5AE29}' +
        '#uvck .y{background:#E5AE29;color:#141213}#uvck .n{background:transparent;color:#fff;border-color:rgba(255,255,255,.4)}' +
        '#uvck button:focus-visible{outline:3px solid #fff;outline-offset:2px}';
      document.head.appendChild(css);
      box = document.createElement('div');
      box.id = 'uvck'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-live', 'polite'); box.setAttribute('aria-label', T[5]);
      box.innerHTML = '<p>' + T[0] + ' <a href="' + T[4] + '">' + T[3] + '</a></p><div class="b"><button type="button" class="n">' + T[2] + '</button><button type="button" class="y">' + T[1] + '</button></div>';
      box.querySelector('.y').onclick = function () { decide('granted'); };
      box.querySelector('.n').onclick = function () { decide('denied'); };
      document.body.appendChild(box);
    }
    box.style.display = 'block';
  }
  window.uvCookies = show; /* link "Preferências de cookies": onclick="uvCookies();return false" */
  function init() {
    if (v === null) show();
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('[data-cookies]');
      if (a) { e.preventDefault(); show(); }
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
