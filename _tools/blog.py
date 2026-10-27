#!/usr/bin/env python3
"""Blog da Usina Vídeos (PT): usinavideos.pt/blog/ e usinavideos.pt/blog/<slug>/

Uso: python3 _tools/blog.py
Regras editoriais (herdadas do Motores e Ação):
- números só de fontes oficiais, com link; nunca valores gerados por IA;
- notas de bastidores retiradas antes de publicar; imagens IA sempre identificadas;
- clientes só com autorização; textos curtos e diretos;
- fórmula: declaração de impacto + corpo + "💡 Dica do Freire" + "Veredito Usina" + assinatura.
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_usina import CSS, COLORS, WA_SVG
from mea_banner import mea_banner, MEA_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://usinavideos.pt'
WA = 'https://wa.me/351912988971?text=Ol%C3%A1%20Freire%2C%20li%20o%20blog%20da%20Usina%20V%C3%ADdeos%20e%20gostaria%20de%20falar%20sobre%20um%20projeto.'
e = html.escape
SIG = 'Atitude fala mais alto. — Freire Neto | Usina Vídeos'

CATS = {'bastidores': 'Bastidores e making of', 'comunicacao': 'Comunicação e marketing digital',
        'mercados': 'Mercados', 'cases': 'Cases'}

POSTS = [
    dict(slug='bastidores-condominio-coral-foz', cat='bastidores', date='2026-10-27',
         title='Bastidores: como produzimos o T4+1 do Condomínio Coral, na Foz',
         desc='Fotografia, drone, vídeo com a consultora e uma página em quatro línguas: o making of de um imóvel premium na Foz do Douro.',
         img='/img/coral-fachada.jpg',
         lead='Um imóvel premium não se vende com três fotos e um texto. Precisa de ser mostrado por inteiro: por dentro, de cima e por quem o conhece.',
         body='''<p>O T4+1 do Condomínio Coral, na Foz do Douro, é uma construção nova com 236 m², quatro suítes e terraços. A consultora <b>Cheila Monteiro</b> (CENTURY 21 Arquitectos II · AMI 11414) pediu-nos tudo numa só produção.</p>
<h2>O que fizemos</h2>
<ul><li><b>Fotografia</b> de interiores e exteriores, com tratamento de cor e luz.</li>
<li><b>Drone</b> sobre a Foz, para mostrar o imóvel no território: mar, acessos e vizinhança.</li>
<li><b>Vídeo com a consultora em cena</b>, a apresentar o imóvel à câmara.</li>
<li><b>Página própria do imóvel</b> em português, inglês, espanhol e francês, com uma simulação identificada como IA.</li></ul>
<figure class="bf"><img src="/img/coral-drone.jpg" alt="Drone sobre o Condomínio Coral, Foz do Douro" loading="lazy"><figcaption>Drone Usina Vídeos · Foz do Douro</figcaption></figure>
<h2>Porque é que funciona</h2>
<p>Quem compra na Foz compara muito e muitas vezes está fora do país. O vídeo dá confiança, o drone responde à pergunta «onde fica?» e a página em quatro línguas evita o reencaminhamento de PDFs e fotos soltas.</p>
<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/qwL_NxCdlNY?rel=0" title="Vídeo do Condomínio Coral com Cheila Monteiro" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>''',
         dica='Grave o consultor sempre no próprio imóvel e no fim do vídeo. É o rosto que o comprador vai procurar quando ligar.',
         veredito='Um briefing, uma produção, quatro entregáveis. É este o padrão que propomos para qualquer imóvel premium.',
         links=[('Ver a apresentação do Coral', '/t4coral/'), ('Ver o vídeo no YouTube', 'https://youtu.be/qwL_NxCdlNY')]),
    dict(slug='5-regras-video-que-gera-contactos', cat='comunicacao', date='2026-10-27',
         title='5 regras para um vídeo que gera contactos',
         desc='Gancho, legendas, formatos, contacto no ecrã e resposta rápida: o que separa um vídeo bonito de um vídeo que traz clientes.',
         img='/img/foz-drone.jpg',
         lead='Um vídeo bonito não chega. O que conta é quantas pessoas falam consigo depois de o ver.',
         body='''<p>Seja um imóvel, um carro, uma loja ou um clube, as regras são as mesmas. São as que aplicamos em todas as produções da Usina.</p>
<h2>1. Ganhe os primeiros 2 segundos</h2><p>Comece pelo melhor plano ou por uma frase forte. Nas redes, quem não fica no início não chega ao fim.</p>
<h2>2. Legende tudo</h2><p>Muita gente vê vídeos sem som. Legendas grandes, fora da zona dos botões do Instagram.</p>
<h2>3. Um vídeo, vários formatos</h2>
<table class="bt"><thead><tr><th>Formato</th><th>Duração</th><th>Onde</th></tr></thead><tbody>
<tr><td>Horizontal 16:9</td><td>1 a 3 min</td><td>YouTube, site, apresentações</td></tr>
<tr><td>Vertical 9:16</td><td>15 a 45 s</td><td>Reels, Shorts, TikTok, anúncios</td></tr>
<tr><td>Quadrado 1:1</td><td>15 a 30 s</td><td>Feed e carrosséis</td></tr></tbody></table>
<h2>4. Contacto sempre no ecrã</h2><p>Nome, telefone ou WhatsApp sempre que a pessoa aparece e no fim. Quem quer ligar não deve ter de procurar.</p>
<h2>5. Responda depressa</h2><p>O vídeo traz o contacto; a resposta rápida e cordial fecha a visita, a reunião ou a venda.</p>''',
         dica='Prepare antes do lançamento três mensagens de resposta: primeiro contacto, seguimento e confirmação de visita ou reunião.',
         veredito='Produção boa é a que gera conversas. Medimos o sucesso em contactos, não em visualizações.',
         links=[('Peça orçamento pelo WhatsApp', WA)]),
    dict(slug='usina-videos-e-motores-e-acao', cat='cases', date='2026-10-27',
         title='Usina Vídeos e Motores e Ação: a mesma casa desde 2002',
         desc='A produtora e a marca de jornalismo automóvel nasceram juntas. O que uma aprende, a outra aplica.',
         img='/img/mea-toro.jpg', img_cap='Fiat Toro Ranch · imagem Fiat',
         lead='O Motores e Ação é a prova diária do que a Usina faz para os clientes: conteúdo regular, com credibilidade, que gera audiência e negócio.',
         body='''<p>A Usina Vídeos foi criada em 2002 por <b>Freire Neto</b>, o mesmo ano em que nasceu o <b>Motores e Ação</b>, marca de jornalismo automóvel com mais de 115 mil inscritos no YouTube, no Brasil e em Portugal.</p>
<h2>O que passa de um lado para o outro</h2>
<ul><li><b>Ritmo:</b> gravar uma vez e distribuir em todo o lado: vídeo longo, Reels, carrosséis e artigo.</li>
<li><b>Rigor:</b> números e preços só de fontes oficiais.</li>
<li><b>Linguagem:</b> reportagem, não publicidade. O espectador percebe a diferença.</li></ul>
<p>É este método que levamos a imobiliárias, stands, clubes, lojas e empresas.</p>''',
         dica='Escolha um formato que consiga manter todas as semanas. A regularidade constrói mais audiência do que um vídeo isolado.',
         veredito='Duas marcas, a mesma escola: comunicação feita por jornalistas, ao serviço de quem precisa de ser visto.',
         links=[('Ler o Motores e Ação', 'https://www.motoreseacao.com/?utm_source=usinavideos&utm_medium=blog&utm_campaign=usina'), ('Ver o canal no YouTube', 'https://www.youtube.com/@motoreseacao')]),
]

MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']


def data_pt(d):
    y, m, dd = d.split('-')
    return f'{int(dd)} de {MESES[int(m) - 1]} de {y}'


BLOG_CSS = '''
.bh{padding:56px 0 24px}.bh h1{font-size:clamp(32px,4.6vw,54px);line-height:1.05;margin-top:10px}
.bcats{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}.bcats span{font-size:13px;font-weight:800;padding:7px 12px;border-radius:999px;background:#fff;border:1px solid #E3DED6}
.bgrid{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));padding-bottom:72px}
.bc{display:flex;flex-direction:column;background:#fff;border:1px solid #E3DED6;border-top:5px solid var(--c);border-radius:18px;overflow:hidden;text-decoration:none;color:inherit}
.bc img{width:100%;aspect-ratio:16/9;object-fit:cover}.bc div{padding:18px 20px 22px}.bc span{font-size:12px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--c)}
.bc h3{font-size:21px;line-height:1.2;margin-top:6px;color:var(--ink)}.bc p{margin-top:8px;font-size:15px}.bc em{display:block;margin-top:12px;font-style:normal;font-size:13px;color:var(--muted)}
.art{max-width:760px;margin:0 auto;padding:44px 0 72px}.art h1{font-size:clamp(30px,4.2vw,46px);line-height:1.08;margin-top:10px}
.art .meta{margin-top:14px;font-size:14px;color:var(--muted)}.art .hero{width:100%;border-radius:18px;margin-top:26px;aspect-ratio:16/9;object-fit:cover}
.art .cap{font-size:12px;color:var(--muted);margin-top:6px}
.art .imp{margin-top:26px;font-size:21px;line-height:1.45;font-weight:700;color:var(--ink);border-left:5px solid var(--y);padding-left:18px}
.art h2{font-size:26px;margin-top:34px}.art p,.art li{font-size:18px;line-height:1.65}.art p{margin-top:14px}.art ul{margin-top:14px;padding-left:22px;display:grid;gap:8px}
.art .bf{margin:26px 0 0}.art .bf img{width:100%;border-radius:16px}.art figcaption{font-size:12px;color:var(--muted);margin-top:6px}
.art .yt{position:relative;aspect-ratio:16/9;margin-top:26px;border-radius:16px;overflow:hidden;background:#000}.art .yt iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.bt{width:100%;border-collapse:collapse;margin-top:16px;background:#fff;border-radius:12px;overflow:hidden;font-size:16px}.bt th,.bt td{padding:12px 14px;border-bottom:1px solid #E3DED6;text-align:left}.bt th{background:var(--ink);color:#fff;font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.dica{margin-top:30px;background:#FFF7E3;border:1px solid #F1D592;border-radius:16px;padding:20px 22px}.dica b{display:block;font-size:15px;color:var(--ink)}.dica p{margin-top:6px!important}
.ver{margin-top:18px;background:var(--ink);color:#E9E5E1;border-radius:16px;padding:20px 22px}.ver b{display:block;color:var(--y);font-size:13px;letter-spacing:.14em;text-transform:uppercase}.ver p{margin-top:6px!important;color:#E9E5E1}
.sig{margin-top:26px;font-weight:800;color:var(--ink)}.blinks{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}
'''


def head(title, desc, url, img, kind, ld):
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:type" content="{kind}"><meta property="og:image" content="{BASE}{img}"><meta property="og:site_name" content="Usina Vídeos"><meta property="og:locale" content="pt_PT">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/rss+xml" title="Blog Usina Vídeos" href="{BASE}/blog/feed.xml">
<meta name="theme-color" content="#141213">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}{MEA_CSS}{BLOG_CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Menu"><div class="wrap">
  <a class="logo" href="/"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <div class="links" style="display:flex"><a href="/">Início</a><a href="/blog/">Blog</a><a href="/#trabalhos">Trabalhos</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Peça orçamento</a>
</div></nav>
'''


FOOT = f'''<footer><div class="wrap" style="display:block;margin-bottom:28px">{mea_banner('pt', 'usinavideos_blog')}</div><div class="wrap">
  <a href="/" aria-label="Usina Vídeos · página inicial"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <span>Produtora de conteúdo e comunicação · Norte e todo o Portugal · © Usina Vídeos</span>
</div></footer>
</body>
</html>
'''

PUB = {'@type': 'Organization', '@id': BASE + '/#usina', 'name': 'Usina Vídeos', 'logo': {'@type': 'ImageObject', 'url': BASE + '/img/logo/usina-horizontal-1200.png'}}
AUTHOR = {'@type': 'Person', 'name': 'Freire Neto', 'url': 'https://www.linkedin.com/in/freireneto/'}


def card(p, i):
    return (f'<a class="bc" href="/blog/{p["slug"]}/" style="--c:{COLORS[i % 3]}"><img src="{p["img"]}" alt="" loading="lazy">'
            f'<div><span>{e(CATS[p["cat"]])}</span><h3>{e(p["title"])}</h3><p>{e(p["desc"])}</p><em>{data_pt(p["date"])} · Freire Neto</em></div></a>')


def teaser():
    """Bloco com os 3 artigos mais recentes, para a página inicial."""
    ps = sorted(POSTS, key=lambda p: p['date'], reverse=True)[:3]
    return ''.join(card(p, i) for i, p in enumerate(ps))


def build():
    d = os.path.join(ROOT, 'blog'); os.makedirs(d, exist_ok=True)
    ps = sorted(POSTS, key=lambda p: p['date'], reverse=True)
    url = BASE + '/blog/'
    ld = {'@context': 'https://schema.org', '@type': 'Blog', 'url': url, 'name': 'Blog Usina Vídeos', 'inLanguage': 'pt-PT', 'publisher': PUB,
          'blogPost': [{'@type': 'BlogPosting', 'headline': p['title'], 'url': f'{BASE}/blog/{p["slug"]}/', 'datePublished': p['date']} for p in ps]}
    cats = ''.join(f'<span>{e(v)}</span>' for v in CATS.values())
    open(os.path.join(d, 'index.html'), 'w').write(head('Blog · Usina Vídeos', 'Bastidores, comunicação e marketing digital, mercados e cases da Usina Vídeos, produtora de conteúdo e comunicação.', url, '/img/foz-drone.jpg', 'website', ld) + f'''
<header class="bh"><div class="wrap"><span class="eb">Blog Usina Vídeos</span><h1>Bastidores, ideias e mercados.</h1>
  <p class="lead">O que fazemos, como fazemos e o que está a mudar nos setores com que trabalhamos.</p><div class="bcats">{cats}</div></div></header>
<main class="wrap bgrid">{''.join(card(p, i) for i, p in enumerate(ps))}</main>
''' + FOOT)
    for p in ps:
        u = f'{BASE}/blog/{p["slug"]}/'
        ld = {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': p['title'], 'description': p['desc'], 'image': BASE + p['img'],
              'datePublished': p['date'], 'dateModified': p['date'], 'author': AUTHOR, 'publisher': PUB, 'mainEntityOfPage': u, 'inLanguage': 'pt-PT',
              'articleSection': CATS[p['cat']]}
        links = ''.join(f'<a class="btn {"y" if j == 0 else "o"}" href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}>{e(t)}</a>' for j, (t, h) in enumerate(p['links']))
        cap = f'<p class="cap">{e(p["img_cap"])}</p>' if p.get('img_cap') else ''
        os.makedirs(os.path.join(d, p['slug']), exist_ok=True)
        open(os.path.join(d, p['slug'], 'index.html'), 'w').write(head(p['title'] + ' · Usina Vídeos', p['desc'], u, p['img'], 'article', ld) + f'''
<main class="wrap"><article class="art">
  <span class="eb">{e(CATS[p['cat']])}</span><h1>{e(p['title'])}</h1>
  <p class="meta">{data_pt(p['date'])} · por <a href="https://www.linkedin.com/in/freireneto/" target="_blank" rel="noopener">Freire Neto</a></p>
  <img class="hero" src="{p['img']}" alt="" fetchpriority="high">{cap}
  <p class="imp">{e(p['lead'])}</p>
  {p['body']}
  <div class="dica"><b>💡 Dica do Freire</b><p>{e(p['dica'])}</p></div>
  <div class="ver"><b>Veredito Usina</b><p>{e(p['veredito'])}</p></div>
  <p class="sig">{e(SIG)}</p>
  <div class="blinks">{links}<a class="btn o" href="/blog/">Mais artigos</a></div>
</article></main>
''' + FOOT)
    items = ''.join(f'<item><title>{e(p["title"])}</title><link>{BASE}/blog/{p["slug"]}/</link><guid>{BASE}/blog/{p["slug"]}/</guid><description>{e(p["desc"])}</description></item>' for p in ps)
    open(os.path.join(d, 'feed.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Blog Usina Vídeos</title><link>{BASE}/blog/</link><description>Bastidores, comunicação e marketing digital, mercados e cases.</description><language>pt-PT</language>{items}</channel></rss>\n')
    print('ok blog', len(ps), 'artigos')


if __name__ == '__main__':
    build()
