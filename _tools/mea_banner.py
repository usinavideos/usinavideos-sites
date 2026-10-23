"""Banner Motores e Ação para os sites da Usina e da Cordial Level (HTML + CSS, sem dependências).

mea_banner(lang, source) devolve o <section> pronto; MEA_CSS vai no <style> da página.
"""
LOGO = 'https://motoreseacao.com/wp-content/uploads/2021/10/cropped-Motores-e-Acao.png'
IMG = '/img/mea-toro.jpg'

TXT = {
    'pt': dict(eb='Jornalismo automóvel desde 2002', h='Vai trocar de carro?<br>Vê primeiro o teste sem filtro.',
               p='Lançamentos, testes e ofertas no Brasil e em Portugal, com quem anda nisto há mais de 20 anos.',
               stat='115 mil+', stat_l='inscritos no YouTube', cta='Ver os testes', yt='Ver no YouTube', cap='Fiat Toro Ranch · imagem Fiat'),
    'en': dict(eb='Automotive journalism since 2002', h='Changing cars?<br>Watch the honest test first.',
               p='Launches, road tests and offers in Brazil and Portugal, from people who have done this for over 20 years (in Portuguese).',
               stat='115K+', stat_l='YouTube subscribers', cta='See the tests', yt='Watch on YouTube', cap='Fiat Toro Ranch · image: Fiat'),
    'es': dict(eb='Periodismo del motor desde 2002', h='¿Vas a cambiar de coche?<br>Mira primero la prueba sin filtro.',
               p='Lanzamientos, pruebas y ofertas en Brasil y Portugal, con más de 20 años de experiencia (en portugués).',
               stat='115 mil+', stat_l='suscriptores en YouTube', cta='Ver las pruebas', yt='Ver en YouTube', cap='Fiat Toro Ranch · imagen: Fiat'),
}

MEA_CSS = """
.meab{position:relative;overflow:hidden;background:#0B0E14;color:#fff;border-radius:22px;isolation:isolate;min-height:420px;display:flex;align-items:center}
.meab>img.mb-car{position:absolute;inset:0 0 0 auto;width:68%;height:100%;object-fit:cover;z-index:-2}
.meab::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,#0B0E14 0,#0B0E14 34%,rgba(11,14,20,.86) 46%,rgba(0,77,154,.18) 78%,rgba(0,0,0,.05) 100%)}
.meab::after{content:"";position:absolute;left:0;right:0;bottom:0;height:6px;background:linear-gradient(90deg,#004D9A,#2F7FD0 60%,#fff)}
.meab .mb-in{padding:44px 40px;max-width:640px}
.meab .mb-lg{width:min(300px,64vw);height:auto;filter:brightness(0) invert(1);display:block}
.meab .mb-eb{display:block;margin-top:22px;font-size:12px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:#5AA3E8}
.meab h3{margin:10px 0 0;font-family:Mulish,system-ui,sans-serif;font-weight:900;font-size:clamp(28px,3.6vw,44px);line-height:1.05;letter-spacing:-.01em;color:#fff}
.meab p{margin:14px 0 0;color:#C9CFD8;font-size:17px;line-height:1.5;max-width:46ch}
.meab .mb-row{border:0;padding:0;display:flex;flex-wrap:wrap;align-items:center;gap:12px 14px;margin-top:24px}
.meab .mb-go{display:inline-flex;align-items:center;gap:8px;background:#004D9A;color:#fff;font-weight:800;font-size:16px;padding:15px 24px;border-radius:999px;text-decoration:none;box-shadow:0 8px 28px rgba(0,77,154,.45);animation:meapulse 2.6s ease-in-out infinite}
.meab .mb-go:hover{background:#2F7FD0}
.meab .mb-yt{display:inline-flex;align-items:center;gap:8px;color:#fff;font-weight:800;font-size:15px;padding:13px 18px;border-radius:999px;border:2px solid rgba(255,255,255,.4);text-decoration:none}
.meab .mb-yt:hover{border-color:#fff}
.meab .mb-st{display:flex;align-items:baseline;gap:8px;margin-top:22px;font-size:14px;color:#C9CFD8}.meab .mb-st b{font-size:26px;font-weight:900;color:#fff}
.meab .mb-cap{position:absolute;right:16px;bottom:14px;font-size:11px;color:rgba(255,255,255,.6)}
@keyframes meapulse{0%,100%{box-shadow:0 8px 28px rgba(0,77,154,.45)}50%{box-shadow:0 8px 34px rgba(47,127,208,.8)}}
@media(prefers-reduced-motion:reduce){.meab .mb-go{animation:none}}
@media(max-width:760px){.meab{flex-direction:column;align-items:stretch;min-height:0}.meab>img.mb-car{position:relative;width:100%;height:230px;order:-1}
.meab::before{background:linear-gradient(180deg,rgba(11,14,20,0) 0,rgba(11,14,20,0) 150px,#0B0E14 230px)}.meab .mb-in{padding:4px 22px 34px}.meab .mb-cap{top:200px;bottom:auto}}
"""

YT_ICON = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="4" fill="#D0252F"/><path d="M10 9v6l5-3z" fill="#fff"/></svg>'


def mea_banner(lang='pt', source='usinavideos'):
    t = TXT[lang]
    utm = f'?utm_source={source}&amp;utm_medium=banner&amp;utm_campaign=mea_top'
    return f'''<div class="meab">
  <img class="mb-car" src="{IMG}" alt="" loading="lazy" width="2200" height="1467">
  <div class="mb-in">
    <img class="mb-lg" src="{LOGO}" alt="Motores e Ação" width="1000" height="286" loading="lazy">
    <span class="mb-eb">{t['eb']}</span>
    <h3>{t['h']}</h3>
    <p>{t['p']}</p>
    <div class="mb-row"><a class="mb-go" href="https://motoreseacao.com/{utm}" target="_blank" rel="noopener">{t['cta']} →</a><a class="mb-yt" href="https://www.youtube.com/@motoreseacao" target="_blank" rel="noopener">{YT_ICON}{t['yt']}</a></div>
    <div class="mb-st"><b>{t['stat']}</b>{t['stat_l']}</div>
  </div>
  <span class="mb-cap">{t['cap']}</span>
</div>'''
