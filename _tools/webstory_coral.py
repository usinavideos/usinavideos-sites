#!/usr/bin/env python3
"""Web story (AMP) e stories para Instagram do Condomínio Coral.

Uso: python3 _tools/webstory_coral.py [pasta_saida_stories_png]
Gera web-stories/condominio-coral-foz-do-douro/index.html e, se for dada uma pasta,
as imagens 1080x1920 para Instagram/WhatsApp (render com Playwright).
"""
import html, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = 'condominio-coral-foz-do-douro'
DIR = os.path.join(ROOT, 'web-stories', SLUG)
URL = f'https://usinavideos.pt/web-stories/{SLUG}/'
SITE = 'https://usinavideos.pt/t4coral/'
VIDEO = 'https://youtu.be/XQ-kl1XxiCo'
WA = 'https://wa.me/351913998917?text=' + 'Ol%C3%A1%20Cheila%2C%20vi%20a%20web%20story%20do%20Condom%C3%ADnio%20Coral%20e%20gostaria%20de%20agendar%20uma%20visita.'
SIG = 'Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414'
SIM = 'Simulação · imagem gerada digitalmente'

# cada página: tipo, imagem(ns), textos
PAGES = [
    dict(id='capa', kind='full', img='capa.jpg', alt='Vista aérea do Condomínio Coral com o mar ao fundo',
         kicker='FOZ DO DOURO · PORTO', h='Condomínio Coral', big=True,
         p='Dois apartamentos T4+1 com terraço', foot=f'Apresentado por {SIG}'),
    dict(id='foz', kind='full', img='praia.jpg', alt='Praia da Foz e a marginal atlântica vistas do ar',
         kicker='A FOZ DO DOURO', h='Onde o rio encontra o mar',
         p='Praias, Passeio Alegre e o farol de Felgueiras a poucos minutos. Universidade Católica e Colégio Britânico a 2 minutos a pé.'),
    dict(id='edificio', kind='frame', img='edificio.jpg', alt='Vista aérea do edifício e do jardim',
         kicker='O EDIFÍCIO', h='Arquitetura contemporânea, jardim privado',
         p='Nova construção com área verde exterior, terraços amplos e lugares de garagem.'),
    dict(id='interiores', kind='frame', img='cozinha.jpg', alt='Cozinha com ilha em pedra natural',
         kicker='OS INTERIORES', h='Pensado ao detalhe',
         chips=['T4+1 · 236 m² úteis', '4 suítes com closet', '5 casas de banho em mármore', 'Piso radiante · certificado A', '4 lugares de garagem']),
    dict(id='antes-depois', kind='pair', img='sala-real.jpg', img2='sala-simulacao.jpg',
         alt='Sala vazia, estado atual', alt2='Sala decorada, simulação de decoração',
         kicker='ANTES E DEPOIS', h='O espaço real e uma proposta de decoração', label1='Espaço real', label2=SIM),
    dict(id='terracos', kind='frame', img='cobertura-simulacao.jpg', alt='Terraço de cobertura decorado, simulação de decoração', sim=True,
         kicker='OS TERRAÇOS', h='Dois apartamentos, dois terraços',
         p='3.º andar: terraço na cobertura com vista mar. 2.º andar: terraço lateral em L.',
         outlink=(VIDEO, 'Ver o vídeo')),
    dict(id='contacto', kind='contact', img='cheila.jpg', alt='Cheila Monteiro',
         kicker='VISITAS', h='Agende a sua visita',
         p='Cheila Monteiro', p2='Consultora Imobiliária · CENTURY 21 Arquitectos II · AMI 11414',
         lines=['WhatsApp +351 913 998 917', 'usinavideos.pt/t4coral'],
         outlink=(WA, 'Falar com a Cheila')),
]

CSS = """
.pg{position:absolute;inset:0;background:#1B3A5C;color:#F5F1E8;font-family:'Montserrat',Arial,sans-serif;overflow:hidden}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,36,56,.6) 0%,rgba(15,36,56,0) 18%,rgba(15,36,56,0) 40%,rgba(15,36,56,.9) 68%,#0F2438 100%)}
.box.t{top:53%;bottom:auto}
.top{position:absolute;left:7%;right:7%;top:5.5%;display:flex;justify-content:space-between;align-items:center;font-size:2.1vh;letter-spacing:.25em;font-weight:600;color:#C9A961}
.box{position:absolute;left:7%;right:7%;bottom:9%;display:flex;flex-direction:column;gap:1.6vh}
.k{font-size:1.7vh;letter-spacing:.24em;font-weight:600;color:#C9A961}
.h{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:5vh;line-height:1.05;margin:0}
.h.big{font-size:7.6vh}
.p{font-size:2.2vh;line-height:1.45;color:#E6EAEE;margin:0}
.rule{width:12%;height:2px;background:#C9A961}
.foot{font-size:1.55vh;color:#C9A961;letter-spacing:.02em}
.ph{position:absolute;left:5%;right:5%;top:10%;width:90%;height:38%;object-fit:cover;border-radius:2vh}
.ph2{position:absolute;left:5%;right:5%;width:90%;height:24.5%;object-fit:cover;border-radius:2vh}
.tag{position:absolute;font-size:1.5vh;padding:.7vh 1.4vh;border-radius:999px;font-weight:600}
.tag.d{background:rgba(15,36,56,.88);color:#F5F1E8}
.tag.g{background:#C9A961;color:#1B3A5C}
.chips{display:flex;flex-wrap:wrap;gap:1vh}
.chip{border:1px solid #C9A961;border-radius:999px;padding:.8vh 1.6vh;font-size:1.8vh;color:#F5F1E8}
.av{width:30vh;height:30vh;border-radius:50%;object-fit:cover;border:.5vh solid #C9A961;margin:0 auto}
.c{text-align:center;align-items:center}
.brand{position:absolute;left:0;right:0;bottom:3%;text-align:center;font-size:1.4vh;color:#9FB0C2;letter-spacing:.08em}
"""


def esc(s):
    return html.escape(s, quote=True)


def page_inner(pg, img):
    """HTML interior de uma página (img(nome) -> url)."""
    k = pg['kind']; o = []
    if k == 'full':
        o.append(f'<img class="bg" src="{img(pg["img"])}" alt="{esc(pg["alt"])}">')
        o.append('<div class="shade"></div>')
    elif k == 'frame':
        o.append(f'<img class="ph" src="{img(pg["img"])}" alt="{esc(pg["alt"])}">')
        if pg.get('sim'):
            o.append(f'<span class="tag g" style="left:8%;top:44%">{SIM}</span>')
    elif k == 'pair':
        o.append(f'<img class="ph2" style="top:10%" src="{img(pg["img"])}" alt="{esc(pg["alt"])}">')
        o.append(f'<span class="tag d" style="left:8%;top:11.5%">{esc(pg["label1"])}</span>')
        o.append(f'<img class="ph2" style="top:36%" src="{img(pg["img2"])}" alt="{esc(pg["alt2"])}">')
        o.append(f'<span class="tag g" style="left:8%;top:37.5%">{esc(pg["label2"])}</span>')
    o.append('<div class="top"><span>CONDOMÍNIO CORAL</span></div>' if pg['id'] != 'capa' else '')
    if k == 'contact':
        o.append('<div class="box c" style="top:14%;bottom:auto">')
        o.append(f'<div class="k">{esc(pg["kicker"])}</div><h2 class="h">{esc(pg["h"])}</h2>')
        o.append(f'<img class="av" src="{img(pg["img"])}" alt="{esc(pg["alt"])}">')
        o.append(f'<p class="h" style="font-size:4vh">{esc(pg["p"])}</p><p class="p">{esc(pg["p2"])}</p><div class="rule"></div>')
        for l in pg['lines']:
            o.append(f'<p class="p" style="font-size:2.6vh;color:#F5F1E8">{esc(l)}</p>')
        o.append('</div>')
    else:
        o.append('<div class="box t" style="top:64%">' if k=='pair' else ('<div class="box t">' if k=='frame' else '<div class="box">'))
        o.append(f'<div class="k">{esc(pg["kicker"])}</div>')
        o.append(f'<h1 class="h{" big" if pg.get("big") else ""}">{esc(pg["h"])}</h1>')
        if pg.get('p'):
            o.append(f'<p class="p">{esc(pg["p"])}</p>')
        if pg.get('chips'):
            o.append('<div class="chips">' + ''.join(f'<span class="chip">{esc(c)}</span>' for c in pg['chips']) + '</div>')
        if pg.get('foot'):
            o.append(f'<div class="rule"></div><div class="foot">{esc(pg["foot"])}</div>')
        o.append('</div>')
    o.append('<div class="brand">Produção Usina Vídeos · usinavideos.pt</div>')
    return '\n'.join(x for x in o if x)


def amp():
    pages = []
    for pg in PAGES:
        inner = page_inner(pg, lambda n: f'img/{n}')
        # amp-img: converter <img ...> em <amp-img layout="fill"> dentro de wrappers posicionados
        import re
        def conv(m):
            attrs = m.group(1)
            cls = re.search(r'class="([^"]*)"', attrs).group(1)
            style = re.search(r'style="([^"]*)"', attrs)
            src = re.search(r'src="([^"]*)"', attrs).group(1)
            alt = re.search(r'alt="([^"]*)"', attrs).group(1)
            st = f' style="{style.group(1)}"' if style else ''
            return f'<div class="{cls}"{st}><amp-img src="{src}" alt="{alt}" layout="fill" object-fit="cover"></amp-img></div>'
        inner = re.sub(r'<img ([^>]*)>', conv, inner)
        ol = ''
        if pg.get('outlink'):
            u, t = pg['outlink']
            ol = f'<amp-story-page-outlink layout="nodisplay" cta-accent-element="background" cta-accent-color="#C9A961" theme="custom"><a href="{u}">{esc(t)}</a></amp-story-page-outlink>'
        pages.append(f'<amp-story-page id="{pg["id"]}" auto-advance-after="7s">\n<amp-story-grid-layer template="fill"><div class="pg">\n{inner}\n</div></amp-story-grid-layer>\n{ol}\n</amp-story-page>')
    title = 'Condomínio Coral: dois T4+1 com terraço na Foz do Douro'
    desc = 'Web story do Condomínio Coral, na Foz do Douro: dois apartamentos T4+1 de nova construção com terraço, jardim e garagem. Apresentado por ' + SIG + '.'
    css = CSS.replace('.pg{', '.pg{').replace('object-fit:cover}', 'object-fit:cover}')
    css += '.bg,.ph,.ph2,.av{display:block;overflow:hidden}.av{position:relative}.ph2{position:absolute}'
    return f'''<!doctype html>
<html amp lang="pt-PT">
<head>
<meta charset="utf-8">
<title>{esc(title)}</title>
<link rel="canonical" href="{URL}">
<meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{URL}img/poster.jpg">
<meta property="og:url" content="{URL}">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500&family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
<script async src="https://cdn.ampproject.org/v0.js"></script>
<script async custom-element="amp-story" src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{esc(title)}","image":["{URL}img/poster.jpg"],"datePublished":"2026-10-27","author":{{"@type":"Organization","name":"Usina Vídeos","url":"https://usinavideos.pt/"}},"publisher":{{"@type":"Organization","name":"Usina Vídeos","logo":{{"@type":"ImageObject","url":"https://usinavideos.pt/img/logo/usina-simbolo-512.png"}}}},"mainEntityOfPage":"{URL}"}}</script>
<style amp-boilerplate>body{{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}}@-webkit-keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}@-moz-keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}@-ms-keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}@-o-keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}@keyframes -amp-start{{from{{visibility:hidden}}to{{visibility:visible}}}}</style><noscript><style amp-boilerplate>body{{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}}</style></noscript>
<style amp-custom>{css}</style>
</head>
<body>
<amp-story standalone title="{esc(title)}" publisher="Usina Vídeos" publisher-logo-src="https://usinavideos.pt/img/logo/usina-simbolo-512.png" poster-portrait-src="{URL}img/poster.jpg">
{chr(10).join(pages)}
</amp-story>
</body>
</html>
'''


def ig_html(pg):
    inner = page_inner(pg, lambda n: 'file://' + os.path.join(DIR, 'img', n))
    return f'''<!doctype html><html lang="pt-PT"><head><meta charset="utf-8"><style>html,body{{margin:0;width:1080px;height:1920px}}
{CSS}.bg,.ph,.ph2{{display:block}}.av{{display:block}}</style></head><body><div class="pg">{inner}</div></body></html>'''


if __name__ == '__main__':
    os.makedirs(DIR, exist_ok=True)
    open(os.path.join(DIR, 'index.html'), 'w').write(amp())
    print('web story:', os.path.join(DIR, 'index.html'))
    if len(sys.argv) > 1:
        out = sys.argv[1]; os.makedirs(out, exist_ok=True)
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch(); page = b.new_page(viewport={'width': 1080, 'height': 1920})
            for i, pg in enumerate(PAGES, 1):
                f = os.path.join(out, f'_s{i}.html'); open(f, 'w').write(ig_html(pg))
                page.goto('file://' + f); page.wait_for_timeout(400)
                page.screenshot(path=os.path.join(out, f'Story_Coral_{i:02d}_{pg["id"]}.png'))
                os.remove(f)
            b.close()
        print('stories:', out)
