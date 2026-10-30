#!/usr/bin/env python3
"""Aviso de cookies + medição (GA4 e Meta Pixel) com consentimento, em todas as páginas do usinavideos.pt.

Idempotente: pode correr depois de qualquer gerador (site_usina, imovel, cordiallevel, proposta, blog...).
- Garante o bloco GA4 + Pixel (se faltar, insere antes de </head>).
- Carrega /consent.js ANTES das tags (Google Consent Mode v2 começa em "denied").
- Pixel arranca em 'revoke' até o visitante aceitar; remove o <noscript> do Pixel (dispararia sem consentimento).
- Link "Política de cookies · Preferências de cookies" no rodapé.
Não mexe em t4coral/ (gerido noutra sessão) nem nas Web Stories (AMP).
Uso: python3 _tools/tracking.py
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GA, PX = 'G-Q2SJMFPJ10', '2965321207157558'
SKIP = ('t4coral/', 'web-stories/', '_frames', 'node_modules')

TAGS = f"""<!-- Google tag (gtag.js) - Usina Vídeos -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA}');
document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a');if(!a)return;var h=a.href||'',ev=/wa\\.me|whatsapp/.test(h)?'whatsapp_click':/^mailto:/.test(h)?'email_click':/calendly/.test(h)?'agendar_click':/^tel:/.test(h)?'telefone_click':null;if(ev)gtag('event',ev,{{link_url:h,page_path:location.pathname}});}});</script>
<!-- Meta Pixel - Usina Vídeos -->
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','{PX}');fbq('track','PageView');
document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a');if(!a)return;var h=a.href||'';if(/wa\\.me|whatsapp|^mailto:|^tel:/.test(h))fbq('track','Contact');else if(/calendly/.test(h))fbq('track','Schedule');}});</script>
"""
CONSENT = '<script src="/consent.js"></script>\n'
FB_INIT = f"fbq('init','{PX}');"
FB_CONSENT = "fbq('consent',window.uvConsent&&uvConsent()?'grant':'revoke');"
NOSCRIPT = re.compile(r'<noscript><img[^>]*facebook\.com/tr\?id=' + PX + r'[^>]*/?></noscript>\n?')
LINK = {'pt': ('Política de cookies', 'Preferências de cookies', '/cookies/'),
        'en': ('Cookie policy', 'Cookie preferences', '/cookies/#en'),
        'es': ('Política de cookies', 'Preferencias de cookies', '/cookies/#es')}


FOTOS = {'Casemiro Ramos': '/cordiallevel/img/casemiro.jpg', 'Francisco Medeiros': '/cordiallevel/img/francisco.jpg'}
AVCSS = ('<style id="avcss">.dir .av{width:96px;height:96px;border-radius:50%;object-fit:cover;border:3px solid var(--gold,#B8962E);display:block;margin-bottom:4px}'
         '.bar a .bav{width:30px;height:30px;border-radius:50%;object-fit:cover;border:2px solid #fff;flex:none}</style>')


def fotos(s):
    """Foto dos consultores ao lado dos contactos (cartões .dir e barra fixa)."""
    if '<article class="dir">' not in s:
        return s
    for nome, src in FOTOS.items():
        s = re.sub(r'(<article class="dir">\s*)(<h3>' + nome + '</h3>)',
                   lambda m: m.group(1) + f'<img class="av" src="{src}" alt="{nome}" width="96" height="96" loading="lazy">' + m.group(2), s)
        s = re.sub(r'(aria-label="Fale comigo: WhatsApp ' + nome + r'">)(?!<img)',
                   lambda m: m.group(1) + f'<img class="bav" src="{src}" alt="" width="30" height="30">', s)
    if 'id="avcss"' not in s:
        s = s.replace('</head>', AVCSS + '</head>', 1)
    return s


def fix(s):
    if FB_INIT not in s and GA not in s:
        s = s.replace('</head>', TAGS + '</head>', 1)
    if CONSENT not in s:
        i = s.find('<!-- Google tag (gtag.js)')
        if i < 0:
            i = s.find(f'gtag/js?id={GA}')
            i = s.rfind('<script', 0, i)
        s = s[:i] + CONSENT + s[i:]
    if FB_CONSENT not in s:
        s = s.replace(FB_INIT, FB_CONSENT + FB_INIT)
    s = NOSCRIPT.sub('', s)
    if 'data-cookies' not in s and '</footer>' in s:
        m = re.search(r'<html[^>]*lang="([a-z]{2})', s)
        a, b, u = LINK.get(m.group(1) if m else 'pt', LINK['pt'])
        p = (f'<p class="uvck-l" style="margin:18px 0 0;font-size:13px;text-align:center;opacity:.8">'
             f'<a href="{u}" style="color:inherit">{a}</a> · <a href="{u}" data-cookies style="color:inherit">{b}</a></p>\n')
        k = s.rfind('</footer>')
        s = s[:k] + p + s[k:]
    return fotos(s)


def main(paths=None):
    n = 0
    files = paths or [os.path.join(d, f) for d, _, fs in os.walk(ROOT) for f in fs
                      if f.endswith('.html') and not d.startswith(os.path.join(ROOT, '.git'))]
    for p in files:
        rel = os.path.relpath(p, ROOT)
        if any(x in rel for x in SKIP) or os.path.basename(p).startswith('google'):
            continue
        s = open(p, encoding='utf-8').read()
        if '<head' not in s or 'http-equiv="refresh"' in s and 'gtag' not in s:
            continue
        t = fix(s)
        if t != s:
            open(p, 'w', encoding='utf-8').write(t); n += 1
    print(f'tracking: {n} ficheiros atualizados')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import stories_strip; stories_strip.main()
    main([os.path.abspath(a) for a in sys.argv[1:]] or None)
