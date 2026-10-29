#!/usr/bin/env python3
"""Web story (AMP) do episódio do Panorama Imobiliário PT sobre crédito jovem (Cordial Level).

Uso: python3 _tools/webstory_panorama.py [pasta_saida_stories_png]
Gera web-stories/panorama-credito-jovem-2027/index.html (imagens em img/, já otimizadas)
e, se for dada uma pasta, as imagens 1080x1920 para Instagram/WhatsApp.
Regras: números com fonte oficial; "situação a" sempre visível; AMI em todas as peças.
"""
import html, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = 'panorama-credito-jovem-2027'
DIR = os.path.join(ROOT, 'web-stories', SLUG)
URL = f'https://usinavideos.pt/web-stories/{SLUG}/'
# Trocar pelo link do episódio quando estiver publicado no YouTube
VIDEO = 'https://www.youtube.com/@CordialLevelPT'
BLOG = '/blog/panorama-imobiliario-credito-jovem-2027/'
WA = 'https://wa.me/351935101667?text=' + 'Ol%C3%A1%20Casemiro%2C%20vi%20a%20web%20story%20do%20Panorama%20Imobili%C3%A1rio%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es.'
AMI = 'Cordial Level | CENTURY 21 Arquitectos · AMI 11414'
DATE = '2026-10-29'

PAGES = [
    dict(id='capa', kind='full', img='capa.jpg', alt='Vista de drone das Piscinas das Marés e da marginal de Leça da Palmeira',
         kicker='PANORAMA IMOBILIÁRIO PT · NOVO EPISÓDIO', h='Crédito jovem em 2027', big=True,
         p='Mercado, angariação e três imóveis para conhecer.', hosts=True, foot=AMI),
    dict(id='garantia', kind='text', kicker='CRÉDITO JOVEM', h='Garantia pública: as regras',
         rows=[('18–35', 'anos, com morada fiscal em Portugal'), ('15%', 'do valor garantido pelo Estado'),
               ('100%', 'de financiamento possível pelo banco'), ('1.ª', 'habitação própria e permanente'),
               ('450 mil €', 'valor máximo do imóvel')],
         note='A aprovação do crédito é sempre do banco.'),
    dict(id='2027', kind='text', kicker='E EM 2027?', h='O que está decidido',
         rows=[('Certo', 'Garantia válida para contratos assinados até 31 de dezembro de 2026'),
               ('Proposto', 'O Orçamento do Estado para 2027 prevê manter a garantia e as isenções de IMT e Imposto do Selo'),
               ('Pendente', 'A decisão formal do Governo ainda não foi tomada')],
         note='Situação a 27 de outubro de 2026.'),
    dict(id='vender', kind='text', kicker='PARA QUEM VENDE', h='Há compradores com financiamento', stat='40.148',
         p='contratos com garantia pública até junho de 2026, segundo o Banco de Portugal.',
         note='O preço certo e uma boa apresentação continuam a decidir a venda.',
         outlink=(WA, 'Pedir avaliação')),
    dict(id='antero', kind='frame', img='antero.jpg', alt='Igreja da Lapa e Rua Antero de Quental vistas de drone',
         kicker='CORDIAL LEVEL SHOPPING · PORTO', h='T2 remodelado na Antero de Quental',
         chips=['77,30 m²', '2 quartos', 'Cozinha equipada', '349 000 €'], foot='Ref. C0393-01689 · ' + AMI,
         outlink=('/cordiallevel/anteroquental/', 'Ver o imóvel')),
    dict(id='leca', kind='frame', img='leca.jpg', alt='Edifício do T3 em Leça da Palmeira junto ao mar, visto de drone',
         kicker='CORDIAL LEVEL SHOPPING · LEÇA DA PALMEIRA', h='T3 com suíte e 2 lugares de garagem',
         chips=['138 m²', 'Sala de 41,91 m²', 'Orientação Norte/Sul', '550 000 €'], foot='Ref. C0393-01659 · ' + AMI,
         outlink=('/cordiallevel/t3leca/', 'Ver o imóvel')),
    dict(id='foz', kind='frame', img='foz.jpg', alt='Fachada da moradia T4 na Foz do Douro',
         kicker='CORDIAL LEVEL SHOPPING · FOZ DO DOURO', h='Moradia T4 com vista de mar',
         chips=['165 m²', '4 quartos', 'Para renovar', '875 000 €'], foot='Ref. C0393-01661 · ' + AMI,
         outlink=('/cordiallevel/casaraofoz/', 'Ver o imóvel')),
    dict(id='episodio', kind='contact', kicker='EPISÓDIO COMPLETO', h='Veja no YouTube',
         lines=['Casemiro Ramos · +351 935 101 667', 'Francisco Medeiros · +351 912 706 395', 'usinavideos.pt/cordiallevel'],
         note='Chamada para a rede móvel nacional · ' + AMI, outlink=(VIDEO, 'Ver o episódio')),
]

CSS = """
.pg{position:absolute;inset:0;background:#1B3A5C;color:#F5F1E8;font-family:'Montserrat',Arial,sans-serif;overflow:hidden}
.bg{position:absolute;inset:0;width:100%;height:100%}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,36,56,.6) 0%,rgba(15,36,56,0) 18%,rgba(15,36,56,0) 40%,rgba(15,36,56,.92) 66%,#0F2438 100%)}
.logo{position:absolute;left:7%;top:5%;width:24%;height:9%}
.box{position:absolute;left:7%;right:7%;bottom:9%;display:flex;flex-direction:column;gap:1.6vh}
.box.t{top:56%;bottom:auto}.box.m{top:19%;bottom:auto}
.k{font-size:1.7vh;letter-spacing:.22em;font-weight:600;color:#C9A961}
.h{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;font-size:5vh;line-height:1.05;margin:0}
.h.big{font-size:7.4vh}
.p{font-size:2.2vh;line-height:1.45;color:#E6EAEE;margin:0}
.rule{width:12%;height:2px;background:#C9A961}
.foot{font-size:1.45vh;color:#C9A961;letter-spacing:.02em}
.ph{position:absolute;left:5%;right:5%;top:16%;width:90%;height:36%;border-radius:2vh;overflow:hidden}
.chips{display:flex;flex-wrap:wrap;gap:1vh}
.chip{border:1px solid #C9A961;border-radius:999px;padding:.8vh 1.6vh;font-size:1.8vh;color:#F5F1E8}
.row{display:flex;gap:2vh;padding:1.5vh 0;border-bottom:1px solid rgba(245,241,232,.16);font-size:2.1vh;line-height:1.35}
.row b{color:#C9A961;min-width:11vh;flex:none}
.stat{font-size:11vh;font-weight:600;color:#C9A961;line-height:1}
.note{font-size:1.7vh;color:#B9C3CF}
.c{text-align:center;align-items:center}
.hosts{display:flex;gap:2.4vh;flex-wrap:wrap}.host{display:flex;align-items:center;gap:1.2vh}
.av{position:relative;width:7vh;height:7vh;border-radius:50%;border:.35vh solid #C9A961;overflow:hidden;flex:none}
.host b{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:2.4vh;color:#fff}.host span{font-size:1.5vh;color:#C9A961}
.brand{position:absolute;left:0;right:0;bottom:3%;text-align:center;font-size:1.4vh;color:#9FB0C2;letter-spacing:.08em}
"""


def esc(s):
    return html.escape(s, quote=True)


def page_inner(pg, img):
    k = pg['kind']; o = []
    if k == 'full':
        o += [f'<img class="bg" src="{img(pg["img"])}" alt="{esc(pg["alt"])}">', '<div class="shade"></div>']
    elif k == 'frame':
        o.append(f'<img class="ph" src="{img(pg["img"])}" alt="{esc(pg["alt"])}">')
    o.append(f'<img class="logo" src="{img("logo.png")}" alt="Cordial Level" data-fit="contain">' if k in ('full', 'text', 'frame') else '')
    if k == 'contact':
        o.append('<div class="box c" style="top:14%;bottom:auto">')
        o.append(f'<img class="logo" style="position:relative;left:auto;top:auto;width:42vh;height:27vh;margin:0 auto" src="{img("logo.png")}" alt="Cordial Level" data-fit="contain">')
        o.append(f'<div class="k">{esc(pg["kicker"])}</div><h2 class="h">{esc(pg["h"])}</h2><p class="h" style="font-size:3.4vh;color:#C9A961">@CordialLevelPT</p><div class="rule"></div>')
        o += [f'<p class="p" style="font-size:2.4vh;color:#F5F1E8">{esc(l)}</p>' for l in pg['lines']]
        o.append(f'<p class="note">{esc(pg["note"])}</p></div>')
    else:
        o.append({'frame': '<div class="box t">', 'text': '<div class="box m">'}.get(k, '<div class="box">'))
        o.append(f'<div class="k">{esc(pg["kicker"])}</div><h1 class="h{" big" if pg.get("big") else ""}">{esc(pg["h"])}</h1>')
        if pg.get('stat'):
            o.append(f'<div class="stat">{esc(pg["stat"])}</div>')
        if pg.get('p'):
            o.append(f'<p class="p">{esc(pg["p"])}</p>')
        if pg.get('hosts'):
            o.append('<div class="hosts">' + ''.join(
                f'<div class="host"><img class="av" src="{img(f)}" alt="{esc(n)}"><div><b>{esc(n)}</b><span>{esc(r)}</span></div></div>'
                for f, n, r in [('francisco.png', 'Francisco Medeiros', 'Consultor imobiliário'), ('freire.png', 'Freire Neto', 'Jornalista')]) + '</div>')
        if pg.get('rows'):
            o.append('<div>' + ''.join(f'<div class="row"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in pg['rows']) + '</div>')
        if pg.get('chips'):
            o.append('<div class="chips">' + ''.join(f'<span class="chip">{esc(c)}</span>' for c in pg['chips']) + '</div>')
        if pg.get('note'):
            o.append(f'<p class="note">{esc(pg["note"])}</p>')
        if pg.get('foot'):
            o.append(f'<div class="rule"></div><div class="foot">{esc(pg["foot"])}</div>')
        o.append('</div>')
    o.append('<div class="brand">Produção Usina Vídeos · usinavideos.pt</div>')
    return '\n'.join(x for x in o if x)


def to_amp(inner):
    def conv(m):
        a = m.group(1)
        cls = re.search(r'class="([^"]*)"', a).group(1)
        st = re.search(r'style="([^"]*)"', a)
        src = re.search(r'src="([^"]*)"', a).group(1)
        alt = re.search(r'alt="([^"]*)"', a).group(1)
        fit = 'contain' if 'data-fit="contain"' in a else 'cover'
        st = f' style="{st.group(1)}"' if st else ''
        return f'<div class="{cls}"{st}><amp-img src="{src}" alt="{alt}" layout="fill" object-fit="{fit}"></amp-img></div>'
    return re.sub(r'<img ([^>]*)>', conv, inner)


def amp():
    pages = []
    for pg in PAGES:
        inner = to_amp(page_inner(pg, lambda n: f'img/{n}'))
        ol = ''
        if pg.get('outlink'):
            u, t = pg['outlink']
            ol = f'<amp-story-page-outlink layout="nodisplay" cta-accent-element="background" cta-accent-color="#C9A961" theme="custom"><a href="{u}">{esc(t)}</a></amp-story-page-outlink>'
        pages.append(f'<amp-story-page id="p-{pg["id"]}" auto-advance-after="8s">\n<amp-story-grid-layer template="fill"><div class="pg">\n{inner}\n</div></amp-story-grid-layer>\n{ol}\n</amp-story-page>')
    title = 'Crédito jovem em 2027: o novo episódio do Panorama Imobiliário PT'
    desc = ('Garantia pública para jovens, o que está decidido para 2027 e três imóveis da Cordial Level no Porto, '
            'em Leça da Palmeira e na Foz do Douro. ' + AMI + '.')
    css = CSS + '.bg,.ph,.logo{display:block;overflow:hidden}'
    ld = (f'{{"@context":"https://schema.org","@type":"Article","headline":"{esc(title)}","image":["{URL}img/poster.jpg"],'
          f'"datePublished":"{DATE}","author":{{"@type":"Person","name":"Freire Neto"}},'
          '"publisher":{"@type":"Organization","name":"Usina Vídeos","logo":{"@type":"ImageObject","url":"https://usinavideos.pt/img/logo/usina-simbolo-512.png"}},'
          f'"mainEntityOfPage":"{URL}"}}')
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
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
<script async src="https://cdn.ampproject.org/v0.js"></script>
<script async custom-element="amp-story" src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>
<script type="application/ld+json">{ld}</script>
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
    css = CSS + '.bg,.ph{object-fit:cover;display:block}.logo{object-fit:contain;display:block}'
    return f'''<!doctype html><html lang="pt-PT"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;width:1080px;height:1920px}}{css}</style></head><body><div class="pg">{inner}</div></body></html>'''


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
                f = os.path.join(DIR, f'_s{i}.html'); open(f, 'w').write(ig_html(pg))
                page.goto('file://' + f); page.wait_for_timeout(500)
                page.screenshot(path=os.path.join(out, f'Story_Panorama_{i:02d}_{pg["id"]}.png'))
                os.remove(f)
            b.close()
        print('stories:', out)
