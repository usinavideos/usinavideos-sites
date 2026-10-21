#!/usr/bin/env python3
"""Gera apresentações de imóvel Cordial Level (uma página estática por imóvel).

Uso: python3 _tools/imovel.py            -> escreve t3leca/index.html e casaraofoz/index.html
Os dados de cada imóvel estão em IMOVEIS, no fim deste ficheiro.
"""
import html, os, urllib.parse as up

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRAMOS = 'https://century21.pt/consultores/cramos'
USINA_WA = 'https://wa.me/351912988971?text='

DIRETORES = [
    dict(nome='Casemiro Ramos', curto='Casemiro', num='351935101667', tel='+351 935 101 667',
         mail='cramos@century21.pt', site='https://century21.pt/consultores/cramos', site_txt='century21.pt/consultores/cramos'),
    dict(nome='Renê Medeiros', curto='Renê', num='351912706395', tel='+351 912 706 395',
         mail='franciscomedeiros@century21.pt', site='https://franciscomedeiros.century21.pt', site_txt='franciscomedeiros.century21.pt'),
]

WA_ICON = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/><path d="M9 9.5c.3 1.8 1.8 3.6 3.6 4.4l1.2-1.1 2 .9-.4 1.6c-3.2.3-6.9-3.2-6.8-6.6l1.6-.4.9 2z"/></svg>'
TEL_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'
PLAY = '<span class="play" aria-hidden="true"><svg width="40%" height="40%" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="#1B3A6B"/></svg></span>'

e = html.escape


def img(name, w=None):
    return f'img/{name}-t.jpg' if w and w <= 900 else f'img/{name}.jpg'


def wa(num, txt):
    return f'https://wa.me/{num}?text=' + up.quote(txt)


CSS = r"""
:root{--navy:#1B3A6B;--navy-d:#12284B;--gold:#B8962E;--gold-l:#D4B562;--cream:#F7F5F0;--ink:#1E2328;--muted:#5E6873;--line:#E3DED2;
--serif:'Cormorant Garamond',Georgia,serif;--sans:'Mulish',system-ui,-apple-system,sans-serif;--max:1120px}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--cream);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.65;padding-bottom:76px}
@media(min-width:900px){body{padding-bottom:0}}
img{max-width:100%;display:block}h1,h2,h3{font-family:var(--serif);font-weight:500;line-height:1.1;margin:0;text-wrap:balance}p{margin:0}
.wrap{max-width:var(--max);margin:0 auto;padding:0 20px}section{padding:80px 0;scroll-margin-top:56px}
.eyebrow{font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700}
.h2{font-size:clamp(30px,4.6vw,46px);color:var(--navy);margin:10px 0 14px}
.lead{color:var(--muted);font-size:17px;max-width:680px}
.nav{position:sticky;top:0;z-index:20;background:var(--navy);border-bottom:1px solid var(--gold)}
.nav .wrap{display:flex;align-items:center;gap:22px;min-height:56px;overflow-x:auto;white-space:nowrap;font-size:13px;letter-spacing:.08em}
.nav .brand{font-family:var(--serif);font-size:21px;color:var(--cream);text-decoration:none;margin-right:auto;letter-spacing:.03em}
.nav .brand b{color:var(--gold-l);font-weight:600}
.nav a{color:var(--cream);text-decoration:none}.nav a:hover{color:var(--gold-l)}
.hero{position:relative;min-height:88vh;min-height:88svh;display:flex;align-items:flex-end;padding:0;background:var(--navy);overflow:hidden}
.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero .band{position:relative;width:100%;background:rgba(18,40,75,.88);border-top:1px solid var(--gold)}
.hero .band .wrap{padding-top:30px;padding-bottom:34px;color:var(--cream);display:flex;flex-direction:column;gap:8px}
.hero .loc{font-size:12px;letter-spacing:.24em;color:var(--gold-l);text-transform:uppercase;font-weight:700}
.hero h1{font-size:clamp(40px,7.4vw,80px);line-height:1.02}
.hero .sub{font-size:18px}
.hero .price{font-family:var(--serif);font-size:clamp(30px,4vw,40px);color:var(--gold-l);font-weight:600;margin-top:4px}
.hero .by{font-size:13px;color:#C9D2DE}
.quote{max-width:860px;margin:0 auto;padding:84px 20px 64px;text-align:center;display:flex;flex-direction:column;gap:26px}
.quote p.q{font-family:var(--serif);font-style:italic;font-size:clamp(26px,4vw,38px);line-height:1.3;color:var(--navy);text-wrap:balance}
.quote .rule{width:64px;height:1px;background:var(--gold);margin:0 auto}
.quote p.t{font-size:17px;text-wrap:pretty}
.facts{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:var(--line);border:1px solid var(--line);margin-top:28px}
@media(min-width:760px){.facts{grid-template-columns:repeat(4,1fr)}}
.facts div{background:#fff;padding:18px 16px}
.facts b{display:block;font-family:var(--serif);font-size:30px;color:var(--navy);font-weight:600;line-height:1.05}
.facts span{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.feat{display:grid;gap:10px 28px;margin:28px 0 0;padding:0;list-style:none}
@media(min-width:760px){.feat{grid-template-columns:1fr 1fr}}
.feat li{padding-left:18px;position:relative}.feat li::before{content:"";position:absolute;left:0;top:.75em;width:9px;height:1px;background:var(--gold)}
.rooms{width:100%;border-collapse:collapse;margin-top:24px;font-size:15px;background:#fff;border:1px solid var(--line)}
.rooms td{padding:11px 16px;border-bottom:1px solid var(--line)}.rooms td:last-child{text-align:right;font-weight:700;color:var(--navy);white-space:nowrap}
.dark{background:var(--navy);color:var(--cream)}.dark .h2{color:var(--cream)}.dark .lead{color:#C9D2DE}
.media{position:relative;width:100%;aspect-ratio:16/9;margin-top:24px;border:1px solid var(--gold);overflow:hidden;background:#0F2438}
.media button,.media a.tour{position:absolute;inset:0;width:100%;height:100%;padding:0;border:0;background:#0F2438;cursor:pointer;display:block}
.media img{width:100%;height:100%;object-fit:cover;opacity:.9}
.media iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:clamp(64px,9vw,100px);height:clamp(64px,9vw,100px);border-radius:50%;background:rgba(212,181,98,.96);box-shadow:0 10px 30px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center}
.tourlabel{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:var(--gold-l);color:var(--navy);font-weight:700;padding:14px 22px;letter-spacing:.06em;white-space:nowrap}
.gal{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:28px}
@media(min-width:900px){.gal{grid-template-columns:repeat(4,1fr);gap:10px}.gal button:nth-child(5n+1){grid-column:span 2;grid-row:span 2}}
.gal button{padding:0;border:0;background:#E9E4D8;cursor:zoom-in;aspect-ratio:4/3;overflow:hidden}
.gal img{width:100%;height:100%;object-fit:cover;transition:transform .4s}.gal button:hover img{transform:scale(1.03)}
.more{margin-top:16px;font-size:14px;color:var(--muted)}
.lb{position:fixed;inset:0;z-index:60;background:rgba(8,16,30,.95);display:none;align-items:center;justify-content:center}
.lb.on{display:flex}.lb img{max-width:94vw;max-height:84vh;object-fit:contain}
.lb button{position:absolute;background:none;border:0;color:#fff;font-size:34px;cursor:pointer;padding:12px 18px}
.lb .x{top:8px;right:8px}.lb .p{left:4px;top:50%;transform:translateY(-50%)}.lb .n{right:4px;top:50%;transform:translateY(-50%)}
.lb .c{position:absolute;bottom:14px;left:0;right:0;text-align:center;color:#C9D2DE;font-size:13px}
.maplink{display:inline-block;margin-top:20px;color:var(--navy);font-weight:700}
.dirs{display:grid;gap:16px;margin-top:28px}@media(min-width:800px){.dirs{grid-template-columns:1fr 1fr}}
.dir{background:#fff;border:1px solid var(--line);padding:26px 24px;display:flex;flex-direction:column;gap:12px}
.dir h3{font-size:32px;color:var(--navy)}.dir .role{font-size:13px;color:var(--muted);margin-top:-6px}
.btns{display:grid;gap:10px}
.b{display:flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:8px 16px;border-radius:999px;text-decoration:none;font-weight:700;font-size:15px;text-align:center}
.b.wa{background:#1E9E4A;color:#fff}.b.navy{background:var(--navy);color:var(--cream)}.b.line{border:1px solid var(--navy);color:var(--navy)}
.b small{font-weight:400;font-size:12px;display:block}
.b:hover{filter:brightness(1.08)}
.mail{font-size:14px;color:var(--muted)}.mail a{color:var(--navy)}
.allprops{margin-top:28px;display:flex;flex-wrap:wrap;gap:10px 24px;justify-content:space-between;align-items:center;padding:20px 24px;background:var(--navy);color:var(--cream);text-decoration:none;border-left:4px solid var(--gold)}
.allprops span{font-family:var(--serif);font-size:clamp(20px,3.2vw,26px);word-break:break-word}
.allprops small{display:block;font-family:var(--sans);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-l);font-weight:700}
.allprops b{color:var(--gold-l);font-size:15px}
.sig{margin-top:36px;text-align:center;font-family:var(--serif);font-style:italic;font-size:clamp(22px,3.6vw,30px);color:var(--navy)}
footer{background:var(--navy-d);color:#C9D2DE;font-size:13px}
footer .wrap{padding-top:32px;padding-bottom:32px;display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center}
footer .usina{display:flex;align-items:center;gap:12px;color:inherit;text-decoration:none}footer .usina img{height:36px;width:auto}
footer a{color:inherit}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:40;display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:10px 12px calc(10px + env(safe-area-inset-bottom));background:rgba(18,40,75,.97);border-top:1px solid var(--gold)}
.bar a{display:flex;align-items:center;justify-content:center;gap:8px;min-height:48px;border-radius:999px;background:#1E9E4A;color:#fff;text-decoration:none;font-weight:700;font-size:14px}
@media(min-width:900px){.bar{left:auto;right:18px;bottom:18px;grid-template-columns:auto auto;border:1px solid var(--gold);border-radius:999px;padding:8px}.bar a{padding:0 18px}}
"""

JS = r"""
(function(){
var g=[].slice.call(document.querySelectorAll('.gal button')),lb=document.querySelector('.lb'),li=lb.querySelector('img'),lc=lb.querySelector('.c'),i=0;
function show(k){i=(k+g.length)%g.length;li.src=g[i].dataset.full;li.alt=g[i].querySelector('img').alt;lc.textContent=(i+1)+' / '+g.length;}
g.forEach(function(b,k){b.addEventListener('click',function(){show(k);lb.classList.add('on');lb.querySelector('.x').focus();});});
lb.querySelector('.x').onclick=function(){lb.classList.remove('on');};
lb.querySelector('.p').onclick=function(){show(i-1);};lb.querySelector('.n').onclick=function(){show(i+1);};
lb.addEventListener('click',function(ev){if(ev.target===lb)lb.classList.remove('on');});
document.addEventListener('keydown',function(ev){if(!lb.classList.contains('on'))return;if(ev.key==='Escape')lb.classList.remove('on');if(ev.key==='ArrowLeft')show(i-1);if(ev.key==='ArrowRight')show(i+1);});
var v=document.querySelector('.media button[data-yt]');
if(v)v.addEventListener('click',function(){var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+v.dataset.yt+'?autoplay=1&rel=0';f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;f.title='Vídeo do imóvel';v.replaceWith(f);},{once:true});
})();
"""


def build(p):
    ref = p['ref']
    ficha = f'https://century21.pt/comprar/{ref}'
    msg = lambda nome: f"Olá {nome}, vi a apresentação do imóvel {p['curto']} (ref. {ref}) e gostaria de mais informações."
    navs = [('ficha', 'O imóvel'), ('galeria', 'Fotografias')]
    if p.get('video'): navs.insert(1, ('video', 'Vídeo'))
    if p.get('tour'): navs.insert(2 if p.get('video') else 1, ('tour', 'Visita 3D'))
    navs += [('localizacao', 'Localização'), ('contacto', 'Contacto')]
    nav = ''.join(f'<a href="#{a}">{b}</a>' for a, b in navs)

    facts = ''.join(f'<div><b>{e(v)}</b><span>{e(k)}</span></div>' for k, v in p['facts'])
    feat = ''.join(f'<li>{e(x)}</li>' for x in p['features'])
    rooms = ''
    if p.get('rooms'):
        rooms = '<table class="rooms"><tbody>' + ''.join(f'<tr><td>{e(a)}</td><td>{e(b)}</td></tr>' for a, b in p['rooms']) + '</tbody></table>'

    video = ''
    if p.get('video'):
        video = f'''<section id="video" class="dark">
  <div class="wrap">
    <span class="eyebrow">O vídeo</span>
    <h2 class="h2">Conheça o imóvel em vídeo</h2>
    <div class="media"><button data-yt="{p['video']}" aria-label="Ver o vídeo do imóvel"><img src="{img(p.get('video_img', p['hero']))}" alt="" loading="lazy">{PLAY}</button></div>
  </div>
</section>'''
    tour = ''
    if p.get('tour'):
        tour = f'''<section id="tour" style="padding-bottom:0">
  <div class="wrap">
    <span class="eyebrow">Visita virtual 3D</span>
    <h2 class="h2">Percorra a casa ao seu ritmo</h2>
    <p class="lead">Visita navegável a 360°, em ecrã inteiro, no telemóvel ou no computador.</p>
    <div class="media"><a class="tour" href="{p['tour']}" target="_blank" rel="noopener"><img src="{img(p['tour_img'])}" alt="" loading="lazy"><span class="tourlabel">Abrir a visita 3D ↗</span></a></div>
  </div>
</section>'''

    gal = ''.join(
        f'<button data-full="{img(g)}" aria-label="Ampliar: {e(a)}"><img src="{img(g, 900)}" alt="{e(a)}" loading="lazy"></button>'
        for g, a in p['gallery'])

    def dir_card(d):
        return f'''<article class="dir">
        <h3>{d['nome']}</h3>
        <p class="role">Diretor · Cordial Level | CENTURY 21 Arquitectos</p>
        <div class="btns">
          <a class="b wa" href="{wa(d['num'], msg(d['curto']))}" target="_blank" rel="noopener">{WA_ICON}WhatsApp {d['curto']}</a>
          <a class="b line" href="tel:+{d['num']}">{TEL_ICON}Ligar · {d['tel']}</a>
          <a class="b line" href="{d['site']}" target="_blank" rel="noopener">Site CENTURY 21</a>
        </div>
        <p class="mail">E-mail: <a href="mailto:{d['mail']}?subject={up.quote('Ref. ' + ref + ' · ' + p['curto'])}">{d['mail']}</a></p>
      </article>'''

    bar = ''.join(f'<a href="{wa(d["num"], msg(d["curto"]))}" target="_blank" rel="noopener" aria-label="WhatsApp {d["nome"]}">{WA_ICON}{d["curto"]}</a>' for d in DIRETORES)
    usina = USINA_WA + up.quote(f"Olá Freire, vi a apresentação do imóvel {p['curto']} e gostaria de saber mais sobre os serviços da Usina Vídeos.")

    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['desc'])}">
<meta name="robots" content="noindex">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:image" content="https://usinavideos.pt/{p['slug']}/img/{p['hero']}.jpg">
<meta name="theme-color" content="#1B3A6B">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Mulish:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Secções"><div class="wrap"><a class="brand" href="#inicio">Cordial <b>Level</b></a>{nav}</div></nav>

<header id="inicio" class="hero">
  <img src="{img(p['hero'], 2200)}" alt="{e(p['hero_alt'])}" fetchpriority="high">
  <div class="band"><div class="wrap">
    <div class="loc">{e(p['loc'])}</div>
    <h1>{e(p['h1'])}</h1>
    <p class="sub">{e(p['sub'])}</p>
    <div class="price">{e(p['price'])}</div>
    <p class="by">Cordial Level | CENTURY 21 Arquitectos · Ref. {ref}</p>
  </div></div>
</header>

<div class="quote">
  <p class="q">“{e(p['quote'])}”</p>
  <div class="rule"></div>
  <p class="t">{e(p['intro'])}</p>
</div>

<section id="ficha" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">O imóvel</span>
    <h2 class="h2">{e(p['ficha_h2'])}</h2>
    <div class="facts">{facts}</div>
    <ul class="feat">{feat}</ul>
    {rooms}
  </div>
</section>

{video}
{tour}

<section id="galeria">
  <div class="wrap">
    <span class="eyebrow">Fotografias</span>
    <h2 class="h2">{e(p['gal_h2'])}</h2>
    <div class="gal">{gal}</div>
    <p class="more">Toque numa fotografia para ampliar. {e(p.get('gal_note', ''))}</p>
  </div>
</section>

<section id="localizacao" class="dark">
  <div class="wrap">
    <span class="eyebrow">Localização</span>
    <h2 class="h2">{e(p['loc_h2'])}</h2>
    <p class="lead">{e(p['loc_txt'])}</p>
    <a class="maplink" style="color:var(--gold-l)" href="https://www.google.com/maps/search/?api=1&query={up.quote(p['maps'])}" target="_blank" rel="noopener">Ver no Google Maps ↗</a>
  </div>
</section>

<section id="contacto">
  <div class="wrap">
    <span class="eyebrow">Contacto</span>
    <h2 class="h2">Marque a sua visita</h2>
    <p class="lead">Fale diretamente com um dos diretores da Cordial Level.</p>
    <div class="dirs">{dir_card(DIRETORES[0])}{dir_card(DIRETORES[1])}</div>
    <a class="allprops" href="{CRAMOS}" target="_blank" rel="noopener"><span><small>Todos os imóveis da Cordial Level</small>century21.pt/consultores/cramos</span><b>Ver a carteira completa →</b></a>
    <p class="more" style="margin-top:14px"><a href="{ficha}" target="_blank" rel="noopener" style="color:var(--navy)">Ficha oficial deste imóvel na CENTURY 21 (ref. {ref}) ↗</a></p>
    <p class="sig">A sua exigência, a nossa assinatura.</p>
  </div>
</section>

<footer><div class="wrap">
  <span>Cordial Level | CENTURY 21 Arquitectos · <a href="https://www.instagram.com/cordiallevel/">Instagram</a> · <a href="https://www.facebook.com/cordiallevel/">Facebook</a> · <a href="https://www.youtube.com/@CordialLevelPT">YouTube</a><br>{e(p['legal'])} Cada agência CENTURY 21 é jurídica e financeiramente independente.</span>
  <a class="usina" href="{usina}" target="_blank" rel="noopener" aria-label="Usina Vídeos — WhatsApp"><span>Produção audiovisual</span><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
</div></footer>

<nav class="bar" aria-label="Contacto rápido por WhatsApp">{bar}</nav>

<div class="lb" role="dialog" aria-modal="true" aria-label="Fotografia ampliada"><img alt=""><button class="x" aria-label="Fechar">×</button><button class="p" aria-label="Anterior">‹</button><button class="n" aria-label="Seguinte">›</button><div class="c"></div></div>
<script>{JS}</script>
</body>
</html>
'''


LECA_G = [
    ('leca-37', 'O edifício junto ao mar, visto de drone'), ('leca-38', 'O edifício e a orla marítima de Leça'),
    ('leca-40', 'O mar e a piscina das marés, a poucos passos'), ('leca-44', 'A praia de Leça da Palmeira'),
    ('leca-34', 'Fachada do edifício'), ('leca-36', 'O edifício e os jardins'),
    ('leca-1', 'Sala com 42 m²'), ('leca-3', 'Sala'), ('leca-4', 'Zona de refeições junto à janela'),
    ('leca-6', 'Mesa de jantar'), ('leca-7', 'Sala e zona de refeições'), ('leca-11', 'Cozinha equipada'),
    ('leca-10', 'Cozinha'), ('leca-9', 'Cozinha'), ('leca-18', 'Casa de banho da suite'), ('leca-19', 'Casa de banho da suite'),
    ('leca-21', 'Suite'), ('leca-23', 'Suite'), ('leca-14', 'Quarto'), ('leca-25', 'Quarto'),
    ('leca-27', 'Casa de banho comum'), ('leca-30', 'Corredor dos quartos'), ('leca-12', 'Lavandaria'),
    ('leca-32', 'Garagem com 2 lugares'), ('leca-43', 'O edifício visto de drone'), ('leca-45', 'A marginal e a praia'),
    ('leca-46', 'A orla de Leça da Palmeira'),
]

FOZ_G = [
    ('foz-f52', 'A fachada da casa'), ('foz-f79', 'A rua vista da varanda'), ('foz-f80', 'A rua Senhora da Luz'),
    ('foz-f43', 'Vista sobre os telhados até ao mar'), ('foz-f45', 'Luz natural no último piso'),
    ('foz-f2', 'Sala com tetos trabalhados'), ('foz-f3', 'Sala'), ('foz-f94', 'Sala com móveis de época'), ('foz-f67', 'Sala de estar'),
    ('foz-f6', 'Escritório'), ('foz-f90', 'Sala de jantar'), ('foz-f91', 'Sala de jantar'), ('foz-f81', 'Cozinha'),
    ('foz-f84', 'Cozinha'), ('foz-f14', 'Entrada e corredor'), ('foz-f11', 'Hall e escadas'), ('foz-f87', 'Casa de banho'),
    ('foz-f15', 'Escadaria com claraboia'), ('foz-f100', 'Claraboia'), ('foz-f40', 'Quarto principal'), ('foz-f41', 'Quarto principal'),
    ('foz-f42', 'Janela com vista'), ('foz-f31', 'Quarto'), ('foz-f21', 'Quarto com varanda'), ('foz-f24', 'Quarto'),
    ('foz-f18', 'Quarto no sótão'), ('foz-f70', 'Quarto'), ('foz-f97', 'Casa de banho'),
    ('foz-f58', 'A rua e os telhados, vistos de drone'), ('foz-f59', 'A casa vista de drone'), ('foz-f61', 'A fachada vista de drone'),
    ('foz-f54', 'Os telhados da Foz'),
]

IMOVEIS = {
    't3leca': dict(
        ref='C0393-01659', curto='T3 Leça da Palmeira',
        title='T3 junto ao mar em Leça da Palmeira · Cordial Level',
        desc='T3 com 138 m² úteis e 2 lugares de garagem, junto ao mar em Leça da Palmeira. 550 000 €.',
        hero='leca-37', hero_alt='T3 junto ao mar em Leça da Palmeira',
        loc='Leça da Palmeira · Matosinhos', h1='T3 junto ao mar', sub='138 m² úteis, 3 quartos e 2 lugares de garagem, a poucos passos das praias de Leça.',
        price='550 000 €',
        quote='Há casas que se escolhem pela planta. Esta escolhe-se também pelo que fica lá fora: o mar, as praias e o ritmo calmo de Leça.',
        intro='Um T3 de 2008 com sala de quase 42 m², suite, chão em madeira de afizélia com aquecimento radiante e dois lugares de garagem — pronto a habitar, junto ao mar em Leça da Palmeira.',
        ficha_h2='Espaço, conforto e dois lugares de garagem',
        facts=[('Área útil', '138 m²'), ('Área bruta', '171 m²'), ('Quartos', '3 · 1 suite'), ('Casas de banho', '2'),
               ('Garagem', '2 lugares'), ('Construção', '2008'), ('Certificado energético', 'C'), ('Exposição', 'Norte / Sul')],
        features=['Pavimento em madeira de afizélia com aquecimento radiante', 'Recuperador de calor',
                  'Cozinha equipada, com máquina de lavar loiça', 'Lavandaria independente',
                  'Caixilharia com vidro duplo', 'Porta de segurança, alarme e videoporteiro',
                  'Tetos falsos em pladur', 'Arrecadação'],
        rooms=[('Sala', '41,91 m²'), ('Suite (quarto)', '18,78 m²'), ('Casa de banho da suite', '5,18 m²'), ('Quarto 2', '13,37 m²'),
               ('Quarto 3', '11,12 m²'), ('Cozinha', '9,53 m²'), ('Corredor dos quartos', '5,45 m²'), ('Arrecadação', '5,32 m²'),
               ('Casa de banho comum', '4,00 m²'), ('Lavandaria', '3,36 m²')],
        gallery=LECA_G, alt='T3 em Leça da Palmeira', gal_h2='Por dentro e por fora',
        loc_h2='Leça da Palmeira, junto ao mar',
        loc_txt='Rua Francisco Sá Carneiro, em Leça da Palmeira. A poucos minutos a pé das praias e da marginal, com comércio, restauração, escolas e o centro de Matosinhos por perto, e acesso rápido ao Porto e ao aeroporto.',
        maps='Rua Francisco Sá Carneiro, Leça da Palmeira',
        legal='Informação sujeita a confirmação; áreas e características segundo a ficha CENTURY 21.',
        video=None, tour=None,
    ),
    'casaraofoz': dict(
        ref='C0393-01661', curto='Moradia T4 Foz do Douro',
        title='Moradia T4 com vista de mar na Foz do Douro · Cordial Level',
        desc='Moradia T4 com vista de mar na Foz do Douro, para renovar. Rua Senhora da Luz, Porto. 875 000 €.',
        hero='foz-f52', hero_alt='Moradia T4 com vista de mar na Foz do Douro',
        loc='Rua Senhora da Luz · Foz do Douro · Porto', h1='Moradia T4 com vista de mar',
        sub='Uma casa para renovar na Foz tradicional, a poucos passos da marginal e do Passeio Alegre.',
        price='875 000 €',
        quote='Na Foz velha, as casas com vista de mar raramente mudam de mãos. Quando mudam, são para quem sabe ver o que podem vir a ser.',
        intro='Moradia T4 de 1990 com 165 m² úteis, pés-direitos altos, muita luz natural e vista de mar. Para renovar ao seu gosto — para habitação própria ou investimento — e dispensada de licença de utilização.',
        ficha_h2='Uma moradia para renovar, com vista de mar',
        facts=[('Área útil', '165 m²'), ('Área bruta', '169 m²'), ('Quartos', '4'), ('Casas de banho', '2'),
               ('Construção', '1990'), ('Certificado energético', 'E'), ('Estado', 'Para renovar'), ('Tipologia', 'Moradia T4')],
        features=['Vista de mar', 'Boa exposição solar e muita luz natural', 'Pés-direitos altos',
                  'Isenta de licença de utilização', 'Potencial de valorização após obras',
                  'Zona tradicional da Foz do Douro, junto à marginal'],
        rooms=None,
        gallery=FOZ_G, alt='Moradia T4 na Foz do Douro', gal_h2='A casa, a rua e o mar',
        loc_h2='Foz do Douro, entre o rio e o mar',
        loc_txt='Rua Senhora da Luz, no coração da Foz tradicional. Praias, marginal e Passeio Alegre a poucos minutos a pé, com comércio, restauração, escolas, banco e mercado na zona — tranquilidade residencial com acesso rápido ao centro do Porto.',
        maps='Rua Senhora da Luz, Foz do Douro, Porto',
        legal='Informação sujeita a confirmação; áreas e características segundo a ficha CENTURY 21.',
        video='zno11IhgXtE', tour='https://realsee.ai/xGWWkzlx', tour_img='foz-f2', video_img='foz-f79',
    ),
}

if __name__ == '__main__':
    for slug, p in IMOVEIS.items():
        p['slug'] = slug
        os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
        with open(os.path.join(ROOT, slug, 'index.html'), 'w') as f:
            f.write(build(p))
        print('ok', slug, len(p['gallery']), 'fotos')
