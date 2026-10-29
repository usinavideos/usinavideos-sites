#!/usr/bin/env python3
"""Cobertura Usina Vídeos × CDJRegio (Clube Desportivo José Régio, Vila do Conde) → cdjregio/index.html

Atualizar todas as semanas:
  RESULTADOS  (mais recente primeiro)  · PROXIMOS (jogos em casa a seguir)
  COBERTURAS  (cada jogo coberto pela Usina: fotos em cdjregio/img/, vídeos YouTube, post Instagram)
Uso: python3 _tools/cdjregio.py && python3 _tools/tracking.py cdjregio/index.html
"""
import html, os, sys, urllib.parse as up
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_usina import CSS, WA_SVG, STRIPE
from social_banner import social_banner, SOCIAL_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
CLUBE = 'https://cdjregio.pt'
WA = 'https://wa.me/351912988971?text=' + up.quote('Olá Freire, vi a cobertura do CDJRegio no site da Usina Vídeos e quero saber mais para o meu clube / a minha marca.')
CASA = 'Pavilhão de Desportos de Vila do Conde'

# (data, escalão, casa, pts_casa, fora, pts_fora, competição)
RESULTADOS = [
    ('18 out.', 'Sub-14 Masculino A', 'CD José Régio', 86, 'CAA Salesianos', 34, 'Distrital 1.ª Divisão'),
    ('17 out.', 'Sénior Masculino', 'CD José Régio', 71, 'NCR Valongo', 89, 'Nacional 2.ª Divisão'),
    ('17 out.', 'Sub-16 Masculino B', 'CD José Régio', 51, 'CD Póvoa "B"', 56, 'Distrital 1.ª Divisão'),
    ('17 out.', 'Sub-14 Masculino B', 'CD Póvoa "B"', 28, 'CD José Régio', 37, 'Distrital 1.ª Divisão'),
    ('11 out.', 'Sénior Masculino', 'CAA Salesianos', 80, 'CD José Régio', 88, 'Nacional 2.ª Divisão'),
    ('11 out.', 'Sub-16 Masculino B', 'BC Campo', 37, 'CD José Régio', 72, 'Distrital 1.ª Divisão'),
    ('11 out.', 'Sub-16 Masculino A', 'Guifões SC "A"', 60, 'CD José Régio', 92, 'Distrital 1.ª Divisão'),
    ('10 out.', 'Sub-14 Feminino', 'CD José Régio', 49, 'Guifões SC "B"', 86, 'Distrital 1.ª Divisão'),
]

# (dia, hora, escalão, adversário, competição)
PROXIMOS = [
    ('Sáb. 7 nov.', '21:00', 'Sénior Masculino', 'BC Limiense', 'Nacional 2.ª Divisão'),
    ('Dom. 8 nov.', '11:00', 'Sub-16 Masculino A', 'CLIP Teams', 'Distrital 1.ª Divisão'),
    ('Dom. 15 nov.', '11:00', 'Sub-16 Masculino A', 'Juvemaia "A"', 'Distrital 1.ª Divisão'),
    ('Sáb. 21 nov.', '21:00', 'Sénior Masculino', 'GDB Leça', 'Nacional 2.ª Divisão'),
    ('Ter. 1 dez.', '15:00', 'Sénior Masculino', 'SC Muya', 'Nacional 2.ª Divisão'),
    ('Sáb. 12 dez.', '15:00', 'Sénior Masculino', 'CD Aves', 'Nacional 2.ª Divisão'),
]

# Coberturas Usina: dict(slug, data, titulo, resumo, capa='img/x.jpg', fotos=[...], yt='ID', ig='URL', story='/web-stories/x/')
COBERTURAS = [
    dict(slug='apresentacao-2026', data='Sábado, 17 de outubro de 2026', titulo='Apresentação das equipas e Sénior × NCR Valongo',
         resumo='Noite de apresentação das equipas da época 2026/2027 no Pavilhão de Desportos, seguida do jogo da equipa sénior com o NCR Valongo (71–89), no Nacional da 2.ª Divisão. O pavilhão veio abaixo com um triplo mesmo em cima do apito do primeiro tempo.',
         ig_code='Deri9uUiObc'),
]

# Lances já publicados no YouTube (canal Dicas do Freire): (id, título, legenda)
VIDEOS = [
    ('W928uxPDX6U', 'CDJ Régio 78–74 Beira-Mar', 'Afundanços e o 3.º lugar · fev. 2026'),
    ('YHqB45YwLjc', 'Vitória sobre o Benfica OA (75–73)', 'Apuramento para a 2.ª fase · jan. 2026'),
    ('wd4Ms8ICggc', 'CDJ Régio × GDB Leça', 'Melhores momentos · nov. 2025'),
    ('0zziUdQ3Mw0', 'CD José Régio 63–81 CPN', 'Nacional 1.ª Divisão Feminina · out. 2025', 'https://motoreseacao.com/campeonato-portugues-de-basquetebol-feminino-cdjr-63-x-81-cpn-melhores-momentos/'),
]
SHORT = 'FpYg6vGqiEs'


def vid(v, t, m, art=None):
    a = f'<a class="art" href="{art}" target="_blank" rel="noopener">Ler a reportagem no Motores e Ação ↗</a>' if art else ''
    return (f'<figure class="pv"><button class="yt2" data-id="{v}" aria-label="Ver vídeo: {e(t)}"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="" loading="lazy">'
            f'<span class="pl" aria-hidden="true"></span></button><figcaption><b>{e(t)}</b><span>{e(m)}</span>{a}</figcaption></figure>')


def jogo(r):
    d, esc, a, pa, b, pb, comp = r
    regio_casa = 'Régio' in a
    venceu = (pa > pb) == regio_casa
    tag = '<span class="res v">V</span>' if venceu else '<span class="res d">D</span>'
    A = f'<b>{e(a)}</b>' if regio_casa else e(a)
    B = f'<b>{e(b)}</b>' if not regio_casa else e(b)
    return (f'<li>{tag}<div><small>{e(d)} · {e(esc)} · {e(comp)}</small>'
            f'<p>{A} <strong>{pa} – {pb}</strong> {B}</p></div></li>')


def prox(p):
    d, h, esc, adv, comp = p
    return f'<li><time>{e(d)}<b>{e(h)}</b></time><div><small>{e(esc)} · {e(comp)}</small><p><b>CD José Régio</b> × {e(adv)}</p></div></li>'


def ig(code):
    u = f'https://www.instagram.com/p/{code}/'
    return (f'<blockquote class="instagram-media" data-instgrm-permalink="{u}?utm_source=ig_embed" data-instgrm-version="14" '
            f'style="background:#fff;border:0;border-radius:14px;margin:0 auto;max-width:540px;min-width:280px;width:100%"><a href="{u}" target="_blank" rel="noopener">Ver a publicação no Instagram</a></blockquote>')


def cobertura(c):
    if c.get('ig_code') and not c.get('capa'):
        return (f'<article class="cob"><div class="cb"><small>{e(c["data"])}</small><h3>{e(c["titulo"])}</h3><p>{e(c["resumo"])}</p>'
                f'<div class="cl"><a class="cv" href="https://www.instagram.com/p/{c["ig_code"]}/" target="_blank" rel="noopener">Ver os lances no Instagram ↗</a></div></div>'
                f'<div class="cb" style="background:#F2EEE8">{ig(c["ig_code"])}</div></article>')
    media = ''
    if c.get('yt'):
        media += f'<a class="cv" href="https://youtu.be/{c["yt"]}" target="_blank" rel="noopener">Ver os lances no YouTube ↗</a>'
    if c.get('ig'):
        media += f'<a class="cv" href="{c["ig"]}" target="_blank" rel="noopener">Ver no Instagram ↗</a>'
    if c.get('story'):
        media += f'<a class="cv" href="{c["story"]}">Web Story ↗</a>'
    fotos = ''.join(f'<img src="{f.replace(".jpg", "-t.jpg")}" alt="{e(c["titulo"])}" loading="lazy">' for f in c.get('fotos', [])[:6])
    return (f'<article class="cob"><img class="cap" src="{c["capa"].replace(".jpg", "-t.jpg")}" alt="{e(c["titulo"])}" loading="lazy">'
            f'<div class="cb"><small>{e(c["data"])}</small><h3>{e(c["titulo"])}</h3><p>{e(c["resumo"])}</p>'
            f'<div class="cg">{fotos}</div><div class="cl">{media}</div></div></article>')


EXTRA = """
.pvs{display:grid;gap:18px;margin-top:32px}@media(min-width:700px){.pvs{grid-template-columns:1fr 1fr}}
.pv{margin:0}.yt2{position:relative;display:block;width:100%;aspect-ratio:16/9;padding:0;border:0;border-radius:14px;overflow:hidden;background:#000;cursor:pointer}
.yt2 img{width:100%;height:100%;object-fit:cover;opacity:.9}.yt2:hover img{opacity:1}.yt2 iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.yt2 .pl{position:absolute;left:50%;top:50%;width:66px;height:66px;margin:-33px 0 0 -33px;border-radius:50%;background:var(--y)}
.yt2 .pl::after{content:"";position:absolute;left:27px;top:21px;border-style:solid;border-width:12px 0 12px 19px;border-color:transparent transparent transparent var(--ink)}
.pv .art{display:inline-block;margin-top:6px;color:var(--y);font-weight:800;font-size:14px}.pv figcaption{margin-top:10px}.pv b{display:block;color:#fff;font-size:18px}.pv span{font-size:14px;color:#C9C3BF}

.cdj{display:flex;align-items:center;gap:18px;margin-bottom:18px}.cdj img{width:84px;height:84px;background:#fff;border-radius:50%;padding:6px}
.cdj span{font-weight:900;font-size:22px;color:#fff}.cdj i{font-style:normal;color:var(--y);font-size:28px;font-weight:900}
.grid2{display:grid;gap:28px}@media(min-width:900px){.grid2{grid-template-columns:1fr 1fr}}
.lst{list-style:none;margin:22px 0 0;padding:0;display:grid;gap:10px}
.lst li{display:flex;gap:14px;align-items:center;background:#fff;border:1px solid #E3DED6;border-radius:14px;padding:14px 16px}
.lst small{display:block;font-size:12px;color:#7A726E;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
.lst p{margin:2px 0 0;color:var(--ink)}.lst strong{font-size:19px;margin:0 6px}
.res{flex:0 0 36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;color:#fff}
.res.v{background:var(--g)}.res.d{background:var(--r)}
.lst time{flex:0 0 92px;font-weight:800;color:var(--ink);font-size:14px;line-height:1.2}.lst time b{display:block;color:var(--r);font-size:18px}
.big{background:var(--ink);color:#fff;border-radius:18px;padding:26px;border-left:6px solid var(--r);margin-top:22px}
.big small{color:var(--y);font-weight:800;letter-spacing:.14em;text-transform:uppercase;font-size:12px}.big h3{color:#fff;font-size:clamp(24px,3.4vw,34px);margin:8px 0}
.big p{margin:0;color:#D6D1CD}
.cobs{display:grid;gap:22px;margin-top:28px}
.cob{background:#fff;border:1px solid #E3DED6;border-radius:18px;overflow:hidden;display:grid}@media(min-width:900px){.cob{grid-template-columns:1.1fr 1fr}}
.cob .cap{width:100%;height:100%;min-height:240px;object-fit:cover}.cb{padding:24px}.cb small{color:var(--r);font-weight:800;text-transform:uppercase;letter-spacing:.12em;font-size:12px}
.cb h3{font-size:26px;margin:6px 0 10px}.cg{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:14px}.cg img{aspect-ratio:1;object-fit:cover;border-radius:8px;width:100%}
.cl{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}.cv{font-weight:800;color:var(--ink);border:2px solid var(--ink);border-radius:999px;padding:9px 16px;text-decoration:none;font-size:14px}
.soon{margin-top:24px;background:#fff;border:2px dashed #D9D2C7;border-radius:18px;padding:28px;text-align:center;color:#6E6764}
.links3{display:grid;gap:12px;margin-top:24px}@media(min-width:760px){.links3{grid-template-columns:repeat(3,1fr)}}
.links3 a{display:block;background:var(--ink);border:1px solid var(--line);border-radius:14px;padding:18px;color:#fff;text-decoration:none}.links3 b{display:block;font-size:18px}.links3 span{color:#C9C3BF;font-size:14px}
"""


def build():
    res = ''.join(jogo(r) for r in RESULTADOS)
    nxt = ''.join(prox(p) for p in PROXIMOS[1:])
    d, h, esc, adv, comp = PROXIMOS[0]
    cobs = (f'<div class="cobs">{"".join(cobertura(c) for c in COBERTURAS)}</div>' if COBERTURAS else
            '<div class="soon"><b>A primeira cobertura da época está a chegar.</b><br>Fotografias, lances em vídeo e Web Story de cada jogo em casa.</div>')
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CDJRegio · Cobertura da época 2026/2027 · Usina Vídeos</title>
<meta name="description" content="Fotografias, lances em vídeo, resultados e próximos jogos do Clube Desportivo José Régio (basquetebol, Vila do Conde), pela Usina Vídeos.">
<meta property="og:title" content="CDJRegio · Cobertura Usina Vídeos"><meta property="og:description" content="Resultados, fotografias e lances em vídeo do basquetebol do José Régio, em Vila do Conde.">
<meta property="og:image" content="https://usinavideos.pt/img/logo/cdjregio.png">
<meta name="theme-color" content="#141213">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}{SOCIAL_CSS}{EXTRA}</style>
</head>
<body>
<nav class="nav" aria-label="Menu"><div class="wrap">
  <a class="logo" href="/"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <div class="links"><a href="#jogos">Jogos</a><a href="#coberturas">Coberturas</a><a href="#lances">Vídeos</a><a href="#clube">O clube</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Falar connosco</a>
</div></nav>

<header class="hero dark" style="min-height:auto;padding:72px 0 64px">
  <div class="wrap">
    <div class="cdj"><img src="/img/logo/cdjregio.png" alt="CD José Régio" width="84" height="84"><i>×</i><span>Usina Vídeos</span></div>
    <span class="eb">Basquetebol · Vila do Conde · Época 2026/2027</span>
    <h1>O José Régio em campo, pela lente da Usina.</h1>
    <p>Fotografias, lances em vídeo e resultados do Clube Desportivo José Régio, do Baby Basket ao Sénior. A Usina Vídeos acompanha os jogos em casa no {CASA} e partilha tudo aqui, no YouTube e no Instagram.</p>
    <div class="row"><a class="btn y" href="#jogos">Resultados e jogos</a><a class="btn o" href="{CLUBE}" target="_blank" rel="noopener">Site do clube ↗</a></div>
    {STRIPE}
  </div>
</header>

<section id="jogos">
  <div class="wrap">
    <span class="eb">Próximo jogo em casa</span>
    <div class="big"><small>{e(d)} · {e(h)} · {e(comp)}</small><h3>CD José Régio × {e(adv)}</h3><p>{e(esc)} · {CASA}. Venha apoiar.</p></div>
    <div class="grid2" style="margin-top:44px">
      <div><span class="eb">Últimos resultados</span><h2 style="font-size:32px">A época até agora</h2><ul class="lst">{res}</ul>
        <p style="font-size:14px;margin-top:12px">Resultados oficiais e calendário completo em <a href="{CLUBE}/calendario" target="_blank" rel="noopener">cdjregio.pt</a>.</p></div>
      <div><span class="eb">A seguir no Pavilhão</span><h2 style="font-size:32px">Jogos em casa</h2><ul class="lst">{nxt}</ul></div>
    </div>
  </div>
</section>

<section id="coberturas" style="padding-top:0">
  <div class="wrap">
    <span class="eb">Coberturas Usina Vídeos</span>
    <h2>Cada jogo, contado em imagem.</h2>
    <p class="lead">Galeria de fotografias, os melhores lances em vídeo e uma Web Story com o resultado, logo a seguir a cada jogo.</p>
    {cobs}
  </div>
</section>

<section id="lances" class="dark">
  <div class="wrap">
    <span class="eb">Lances em vídeo</span>
    <h2>Os melhores momentos, no YouTube.</h2>
    <p class="lead">Highlights produzidos pela Usina Vídeos nas épocas do José Régio.</p>
    <div class="pvs">{"".join(vid(*r) for r in VIDEOS)}</div>
    <div class="row" style="margin-top:26px"><a class="btn y" href="https://www.youtube.com/shorts/{SHORT}" target="_blank" rel="noopener">Ver o Short dos afundanços ↗</a><a class="btn o" style="color:#fff" href="https://www.youtube.com/@DicasdoFreire?sub_confirmation=1" target="_blank" rel="noopener">Subscrever no YouTube</a></div>
  </div>
</section>

<section id="clube">
  <div class="wrap">
    <span class="eb">O clube</span>
    <h2>Mais de 200 atletas, 10 equipas e mais de 29 anos de basquetebol.</h2>
    <p class="lead">O Clube Desportivo José Régio forma atletas e cidadãos em Vila do Conde, do Baby Basket à equipa sénior no Campeonato Nacional da 2.ª Divisão.</p>
    <div class="links3">
      <a href="{CLUBE}" target="_blank" rel="noopener"><b>cdjregio.pt ↗</b><span>Equipas, calendário e notícias do clube</span></a>
      <a href="{CLUBE}/renovacao" target="_blank" rel="noopener"><b>Inscrições 2026/2027 ↗</b><span>Inscreva um atleta ou renove a inscrição</span></a>
      <a href="https://loja.cdjregio.pt/" target="_blank" rel="noopener"><b>Loja oficial ↗</b><span>Merchandising do CDJR</span></a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="big" style="border-left-color:var(--y)"><small>Para clubes, atletas e marcas</small><h3>Quer esta cobertura para o seu clube?</h3>
      <p>Fotografia e vídeo de jogos, lances para as redes, apresentações de equipas, entrevistas e conteúdos para patrocinadores. A Usina Vídeos produz, edita e publica.</p>
      <div class="row" style="margin-top:18px"><a class="btn y" href="{WA}" target="_blank" rel="noopener">{WA_SVG} Falar com o Freire</a><a class="btn o" style="color:#fff" href="/#servicos">Ver serviços</a></div></div>
    <div style="margin-top:40px">{social_banner('usina', 'pt')}</div>
  </div>
</section>

<footer><div class="wrap">
  <a href="/" aria-label="Usina Vídeos · página inicial"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <span>Cobertura do CD José Régio pela Usina Vídeos. Emblema e resultados: Clube Desportivo José Régio. · © Usina Vídeos</span>
</div></footer>
<script>document.querySelectorAll('.yt2').forEach(function(b){{b.addEventListener('click',function(){{var i=document.createElement('iframe');i.src='https://www.youtube-nocookie.com/embed/'+b.dataset.id+'?autoplay=1&rel=0';i.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';i.allowFullscreen=true;i.title=b.getAttribute('aria-label');b.innerHTML='';b.appendChild(i)}},{{once:true}})}});</script>
<script async src="https://www.instagram.com/embed.js"></script>
</body>
</html>
'''


if __name__ == '__main__':
    d = os.path.join(ROOT, 'cdjregio')
    os.makedirs(os.path.join(d, 'img'), exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(build())
    print('ok cdjregio', len(RESULTADOS), 'resultados', len(PROXIMOS), 'jogos', len(COBERTURAS), 'coberturas')
