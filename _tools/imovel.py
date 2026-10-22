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
    dict(nome='Francisco Medeiros', curto='Francisco', num='351912706395', tel='+351 912 706 395',
         mail='franciscomedeiros@century21.pt', site='https://franciscomedeiros.century21.pt', site_txt='franciscomedeiros.century21.pt'),
]

WA_ICON = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/><path d="M9 9.5c.3 1.8 1.8 3.6 3.6 4.4l1.2-1.1 2 .9-.4 1.6c-3.2.3-6.9-3.2-6.8-6.6l1.6-.4.9 2z"/></svg>'
TEL_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'
PLAY = '<span class="play" aria-hidden="true"><svg width="40%" height="40%" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="#1B3A6B"/></svg></span>'

e = html.escape


def img(name, w=None):
    return f'img/{name}-t.jpg' if w and w <= 900 else f'img/{name}.jpg'


def simb(p, n):
    return (' data-sim="1"', '<span class="sim">Simulação</span>') if n in p.get('sim', ()) else ('', '')


def wa(num, txt):
    return f'https://wa.me/{num}?text=' + up.quote(txt)


CSS = r"""
:root{--navy:#1B3A6B;--navy-d:#12284B;--gold:#B8962E;--gold-l:#D4B562;--cream:#F7F5F0;--ink:#1E2328;--muted:#5E6873;--line:#E3DED2;
--serif:'Cormorant Garamond',Georgia,serif;--sans:'Mulish',system-ui,-apple-system,sans-serif;--max:1120px}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--cream);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.65;padding-bottom:100px;font-variant-numeric:lining-nums}
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
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}.chips span{border:1px solid var(--gold);padding:8px 16px;border-radius:999px;font-weight:700;font-size:15px;color:var(--navy);background:#fff}
.dark .chips span{background:transparent;color:var(--cream)}
.lprice{font-family:var(--serif);font-size:clamp(30px,4vw,38px);color:var(--gold);font-weight:600;margin-top:10px;font-variant-numeric:lining-nums}.lprice small{font-family:var(--sans,inherit);font-size:14px;font-weight:600;color:var(--muted);margin-left:10px;letter-spacing:.04em}.dark .lprice{color:var(--gold-l)}.dark .lprice small{color:#C9D2DE}
.rooms{width:100%;border-collapse:collapse;margin-top:24px;font-size:15px;background:#fff;border:1px solid var(--line)}
.rooms td{padding:11px 16px;border-bottom:1px solid var(--line)}.rooms td:last-child{text-align:right;font-weight:700;color:var(--navy);white-space:nowrap}
.dark{background:var(--navy);color:var(--cream)}.dark .h2{color:var(--cream)}.dark .lead{color:#C9D2DE}
.media{position:relative;width:100%;aspect-ratio:16/9;margin-top:24px;border:1px solid var(--gold);overflow:hidden;background:#0F2438}
.media button,.media a.tour{position:absolute;inset:0;width:100%;height:100%;padding:0;border:0;background:#0F2438;cursor:pointer;display:block}
.media.vert{aspect-ratio:9/16;max-width:420px;margin-left:auto;margin-right:auto}
.media img{width:100%;height:100%;object-fit:cover;opacity:.9}
.media iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:clamp(64px,9vw,100px);height:clamp(64px,9vw,100px);border-radius:50%;background:rgba(212,181,98,.96);box-shadow:0 10px 30px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center}
.tourlabel{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:var(--gold-l);color:var(--navy);font-weight:700;padding:14px 22px;letter-spacing:.06em;white-space:nowrap}
.strip{display:grid;gap:8px;margin-top:28px;grid-template-columns:1fr}
@media(min-width:640px){.strip.n2{grid-template-columns:1fr 1fr}.strip.n3{grid-template-columns:2fr 1fr}.strip.n3 button:first-child{grid-row:span 2}}
.strip button{padding:0;border:0;background:#E9E4D8;cursor:zoom-in;overflow:hidden;aspect-ratio:4/3}
.strip.n1 button{aspect-ratio:16/9}
@media(min-width:640px){.strip.n3 button:first-child{aspect-ratio:auto}}
.strip img{width:100%;height:100%;object-fit:cover;transition:transform .4s}
.strip button,.gal button{position:relative}
.sim{position:absolute;left:8px;bottom:8px;background:rgba(18,40,75,.86);color:#F7F5F0;font-size:11px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;padding:4px 8px;pointer-events:none}
.hero.plain{min-height:62vh;min-height:62svh;background:linear-gradient(160deg,#1B3A6B 0%,#12284B 100%)}
.hero.plain .logo{position:absolute;top:28px;left:50%;transform:translateX(-50%);width:min(220px,46vw);height:auto;opacity:.95}.strip button:hover img{transform:scale(1.03)}
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
.map{position:relative;width:100%;aspect-ratio:16/9;margin-top:24px;border:1px solid var(--gold);overflow:hidden;background:#0F2438}
@media(max-width:640px){.map{aspect-ratio:4/5}}
.map iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.maplink{display:inline-block;margin-top:20px;color:var(--navy);font-weight:700}
.dirs{display:grid;gap:16px;margin-top:28px}@media(min-width:800px){.dirs{grid-template-columns:1fr 1fr}}
.dir{background:#fff;border:1px solid var(--line);padding:26px 24px;display:flex;flex-direction:column;gap:12px}
.dir h3{font-size:32px;color:var(--navy)}.dir .role{font-size:13px;color:var(--muted);margin-top:-6px}
.btns{display:grid;gap:10px}
.b{display:flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:8px 16px;border-radius:999px;text-decoration:none;font-weight:700;font-size:15px;text-align:center}
.b.wa{background:#1E9E4A;color:#fff}.b.navy{background:var(--navy);color:var(--cream)}.b.line{border:1px solid var(--navy);color:var(--navy)}
.b small{font-weight:400;font-size:12px;display:block}
.b:hover{filter:brightness(1.08)}
.cta-lbl{font-family:var(--serif);font-style:italic;font-size:24px;color:var(--gold);margin:4px 0 -4px}
.bar-lbl{grid-column:1/-1;margin:0 0 -2px;text-align:center;font-family:var(--serif);font-style:italic;font-size:19px;color:var(--gold-l);line-height:1.1}
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
@media(min-width:900px){.bar{left:auto;right:18px;bottom:18px;grid-template-columns:auto auto;border:1px solid var(--gold);border-radius:22px;padding:10px 10px 10px}.bar a{padding:0 18px}}
"""

JS = r"""
(function(){
var g=[].slice.call(document.querySelectorAll('.strip button,.gal button')),lb=document.querySelector('.lb'),li=lb.querySelector('img'),lc=lb.querySelector('.c'),i=0;
function show(k){i=(k+g.length)%g.length;li.src=g[i].dataset.full;li.alt=g[i].querySelector('img').alt;lc.textContent=(i+1)+' / '+g.length+(g[i].dataset.sim?' · Simulação, imagem gerada digitalmente':'');}
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
    navs = p.get('navs') or [('ficha', 'O imóvel'), ('galeria', 'Fotografias')]
    if not p.get('navs'):
        if p.get('video'): navs.insert(1, ('video', 'Vídeo'))
        if p.get('tour'): navs.insert(2 if p.get('video') else 1, ('tour', 'Visita 3D'))
    navs = navs + [('localizacao', 'Localização'), ('contacto', 'Contacto')]
    nav = ''.join(f'<a href="#{a}">{b}</a>' for a, b in navs)

    facts = ''.join(f'<div><b>{e(v)}</b><span>{e(k)}</span></div>' for k, v in p['facts'])
    feat = ''.join(f'<li>{e(x)}</li>' for x in p['features'])
    rooms = ''
    if p.get('rooms'):
        rooms = '<table class="rooms"><tbody>' + ''.join(f'<tr><td>{e(a)}</td><td>{e(b)}</td></tr>' for a, b in p['rooms']) + '</tbody></table>'

    caps = dict(p['gallery'])
    def strip(names):
        if not names: return ''
        bt = ''.join(f'<button data-full="{img(n)}"{simb(p, n)[0]} aria-label="Ampliar: {e(caps.get(n, p["alt"]))}"><img src="{img(n, 900)}" alt="{e(caps.get(n, p["alt"]))}" loading="lazy">{simb(p, n)[1]}</button>' for n in names)
        return f'<div class="strip n{len(names)}">{bt}</div>'

    def sec(x):
        paras = ''.join(f'<p class="lead" style="margin-top:12px">{e(t)}</p>' for t in x.get('paras', []))
        chips = ('<div class="chips">' + ''.join(f'<span>{e(c)}</span>' for c in x['chips']) + '</div>') if x.get('chips') else ''
        cls = ' class="dark"' if x.get('dark') else ''
        return f'''<section id="{x['id']}"{cls}>
  <div class="wrap">
    <span class="eyebrow">{e(x['eb'])}</span>
    <h2 class="h2">{e(x['h2'])}</h2>{paras}{chips}{strip(x.get('photos'))}
  </div>
</section>'''
    extras = ''.join(sec(x) for x in p.get('extras', []))

    def lote(x):
        lf = ''.join(f'<div><b>{e(v)}</b><span>{e(k)}</span></div>' for k, v in x['facts'])
        paras = ''.join(f'<p class="lead" style="margin-top:12px">{e(t)}</p>' for t in x.get('paras', []))
        chips = ('<div class="chips">' + ''.join(f'<span>{e(c)}</span>' for c in x['chips']) + '</div>') if x.get('chips') else ''
        la, lo = x['geo']
        strips = ''.join(strip(g) for g in x['photos'])
        cls = ' class="dark"' if x.get('dark') else ''
        lk = 'var(--gold-l)' if x.get('dark') else 'var(--navy)'
        return f'''<section id="{x['id']}"{cls}>
  <div class="wrap">
    <span class="eyebrow">{e(x['eb'])}</span>
    <h2 class="h2">{e(x['h2'])}</h2>
    <p class="lprice">{e(x['price'])} <small>Ref. {x['ref']}</small></p>{paras}{strips}
    <div class="facts">{lf}</div>{chips}
    <p class="more" style="margin-top:18px"><a href="https://www.google.com/maps/dir/?api=1&destination={la},{lo}" target="_blank" rel="noopener" style="color:{lk}">Localização no Google Maps ↗</a> · <a href="https://century21.pt/comprar/{x['ref']}" target="_blank" rel="noopener" style="color:{lk}">Ficha CENTURY 21 (ref. {x['ref']}) ↗</a></p>
  </div>
</section>'''
    lotes = ''.join(lote(x) for x in p.get('lotes', []))
    closing = sec(p['closing']) if p.get('closing') else ''
    ficha_lead = ''.join(f'<p class="lead" style="margin-top:12px">{e(t)}</p>' for t in p.get('ficha_lead', []))
    feat_h = f'<h3 style="margin-top:36px;font-size:28px;color:var(--navy)">{e(p["feat_h3"])}</h3>' if p.get('feat_h3') else ''
    rooms_h = f'<h3 style="margin-top:36px;font-size:28px;color:var(--navy)">{e(p["rooms_h3"])}</h3>' if p.get('rooms_h3') else ''

    if p.get('geo'):
        la, lo = p['geo']
        maplink = f'https://www.google.com/maps/dir/?api=1&destination={la},{lo}'
        mapframe = f'<div class="map"><iframe title="Localização aproximada do imóvel" src="https://maps.google.com/maps?q={la},{lo}&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>'
    else:
        maplink = 'https://www.google.com/maps/search/?api=1&query=' + up.quote(p['maps']); mapframe = ''

    video = ''
    if p.get('video'):
        video = f'''<section id="video" class="dark">
  <div class="wrap">
    <span class="eyebrow">O vídeo</span>
    <h2 class="h2">{e(p.get('video_h2', 'Conheça o imóvel em vídeo'))}</h2>
    <div class="media{' vert' if p.get('video_vertical') else ''}"><button data-yt="{p['video']}" aria-label="Ver o vídeo do imóvel"><img src="{img(p.get('video_img', p.get('hero')))}" alt="" loading="lazy">{PLAY}</button></div>
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
        f'<button data-full="{img(g)}"{simb(p, g)[0]} aria-label="Ampliar: {e(a)}"><img src="{img(g, 900)}" alt="{e(a)}" loading="lazy">{simb(p, g)[1]}</button>'
        for g, a in p['gallery'])

    def dir_card(d):
        return f'''<article class="dir">
        <h3>{d['nome']}</h3>
        <p class="role">Diretor · Cordial Level | CENTURY 21 Arquitectos · AMI 11414</p>
        <p class="cta-lbl">Fale comigo!</p>
        <div class="btns">
          <a class="b wa" href="{wa(d['num'], msg(d['curto']))}" target="_blank" rel="noopener">{WA_ICON}WhatsApp {d['curto']}</a>
          <a class="b line" href="tel:+{d['num']}">{TEL_ICON}Ligar · {d['tel']}</a>
          <a class="b line" href="{d['site']}" target="_blank" rel="noopener">Site CENTURY 21</a>
        </div>
        <p class="mail">E-mail: <a href="mailto:{d['mail']}?subject={up.quote('Ref. ' + ref + ' · ' + p['curto'])}">{d['mail']}</a></p>
      </article>'''

    bar = ''.join(f'<a href="{wa(d["num"], msg(d["curto"]))}" target="_blank" rel="noopener" aria-label="Fale comigo: WhatsApp {d["nome"]}">{WA_ICON}{d["curto"]}</a>' for d in DIRETORES)
    usina = USINA_WA + up.quote(f"Olá Freire, vi a apresentação do imóvel {p['curto']} e gostaria de saber mais sobre os serviços da Usina Vídeos.")

    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['desc'])}">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:image" content="{f"https://usinavideos.pt/cordiallevel/{p['slug']}/img/{p['hero']}.jpg" if p.get('hero') else 'https://usinavideos.pt/cordiallevel/img/capa-logo.jpg'}">
<meta name="theme-color" content="#1B3A6B">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Mulish:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Secções"><div class="wrap"><a class="brand" href="../">Cordial <b>Level</b></a>{nav}</div></nav>

<header id="inicio" class="hero{'' if p.get('hero') else ' plain'}">
  {f'<img src="{img(p["hero"], 2200)}" alt="{e(p["hero_alt"])}" fetchpriority="high"' + (f' style="object-position:{p["hero_pos"]}"' if p.get("hero_pos") else '') + '>' if p.get('hero') else '<img class="logo" src="../img/logo-cordial-level-claro.png" alt="Cordial Level">'}
  <div class="band"><div class="wrap">
    <div class="loc">{e(p['loc'])}</div>
    <h1>{e(p['h1'])}</h1>
    <p class="sub">{e(p['sub'])}</p>
    <div class="price">{e(p['price'])}</div>
    <p class="by">Cordial Level | CENTURY 21 Arquitectos · AMI 11414 · Ref. {ref}</p>
  </div></div>
</header>

<div class="quote">
  <p class="q">“{e(p['quote'])}”</p>
  <div class="rule"></div>
  <p class="t">{e(p['intro'])}</p>
</div>
{('<div class="wrap" style="margin-top:-24px;margin-bottom:56px">' + strip(p['photos_intro']) + '</div>') if p.get('photos_intro') else ''}

{lotes}{'' if p.get('lotes') else f'''<section id="ficha" style="padding-top:0">
  <div class="wrap">
    <span class="eyebrow">O imóvel</span>
    <h2 class="h2">{e(p['ficha_h2'])}</h2>{ficha_lead}{strip(p.get('photos_ficha'))}
    <div class="facts">{facts}</div>
    {rooms_h}{rooms}{strip(p.get('photos_rooms'))}
    {feat_h}<ul class="feat">{feat}</ul>
  </div>
</section>'''}
{extras}

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
    {mapframe}
    <a class="maplink" style="color:var(--gold-l)" href="{maplink}" target="_blank" rel="noopener">Abrir no Google Maps · obter direções ↗</a>
  </div>
</section>

{closing}
<section id="contacto">
  <div class="wrap">
    <span class="eyebrow">Contacto</span>
    <h2 class="h2">Marque a sua visita</h2>
    <p class="lead">Fale diretamente com um dos diretores da Cordial Level.</p>
    <div class="dirs">{dir_card(DIRETORES[0])}{dir_card(DIRETORES[1])}</div>
    <a class="allprops" href="{CRAMOS}" target="_blank" rel="noopener"><span><small>Todos os imóveis da Cordial Level</small>century21.pt/consultores/cramos</span><b>Ver a carteira completa →</b></a>
    <p class="more" style="margin-top:14px">{' · '.join(f'<a href="https://century21.pt/comprar/{r}" target="_blank" rel="noopener" style="color:var(--navy)">Ficha CENTURY 21 (ref. {r}) ↗</a>' for r in p.get('refs', [ref]))}</p>
    <p class="sig">A sua exigência, a nossa assinatura.</p>
  </div>
</section>

<footer><div class="wrap">
  <span><b style="color:#F7F5F0;font-weight:700">Cordial Level | CENTURY 21 Arquitectos · AMI 11414</b> · <a href="https://www.instagram.com/cordiallevel/">Instagram</a> · <a href="https://www.facebook.com/cordiallevel/">Facebook</a> · <a href="https://www.youtube.com/@CordialLevelPT">YouTube</a><br>{e(p['legal'])} Cada agência CENTURY 21 é jurídica e financeiramente independente.</span>
  <a class="usina" href="{usina}" target="_blank" rel="noopener" aria-label="Usina Vídeos — WhatsApp"><span>Produção audiovisual</span><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
</div></footer>

<nav class="bar" aria-label="Contacto rápido por WhatsApp"><p class="bar-lbl">Fale diretamente connosco</p>{bar}</nav>

<div class="lb" role="dialog" aria-modal="true" aria-label="Fotografia ampliada"><img alt=""><button class="x" aria-label="Fechar">×</button><button class="p" aria-label="Anterior">‹</button><button class="n" aria-label="Seguinte">›</button><div class="c"></div></div>
<script>{JS}</script>
</body>
</html>
'''


LECA_G = [
    ('leca-37', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-38', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-40', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-44', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-43', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-45', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-46', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-39', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-41', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-42', 'O edifício e o mar de Leça, vistos de drone'),
    ('leca-34', 'Fachada do edifício'),
    ('leca-35', 'Fachada do edifício'),
    ('leca-36', 'Fachada do edifício'),
    ('leca-1', 'Sala com 41,91 m²'),
    ('leca-2', 'Sala com 41,91 m²'),
    ('leca-3', 'Sala com 41,91 m²'),
    ('leca-5', 'Sala com 41,91 m²'),
    ('leca-7', 'Sala com 41,91 m²'),
    ('leca-8', 'Sala com 41,91 m²'),
    ('leca-4', 'Zona de refeições'),
    ('leca-6', 'Zona de refeições'),
    ('leca-11', 'Cozinha'),
    ('leca-10', 'Cozinha'),
    ('leca-9', 'Cozinha'),
    ('leca-12', 'Lavandaria'),
    ('leca-13', 'Lavandaria'),
    ('leca-21', 'Suíte'),
    ('leca-22', 'Suíte'),
    ('leca-23', 'Suíte'),
    ('leca-18', 'Casa de banho da suíte'),
    ('leca-19', 'Casa de banho da suíte'),
    ('leca-20', 'Casa de banho da suíte'),
    ('leca-24', 'Quarto'),
    ('leca-25', 'Quarto'),
    ('leca-14', 'Quarto'),
    ('leca-15', 'Quarto'),
    ('leca-16', 'Quarto'),
    ('leca-27', 'Casa de banho comum'),
    ('leca-28', 'Casa de banho comum'),
    ('leca-29', 'Casa de banho comum'),
    ('leca-30', 'Vestíbulo dos quartos e arrumação'),
    ('leca-17', 'Vestíbulo dos quartos e arrumação'),
    ('leca-31', 'Garagem com 2 lugares'),
    ('leca-32', 'Garagem com 2 lugares'),
    ('leca-33', 'Garagem com 2 lugares'),
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
        title='T3 com 2 lugares de garagem em Leça da Palmeira · Cordial Level',
        desc='T3 com 138 m², sala de 41,91 m², suíte, orientação Norte/Sul e 2 lugares de garagem em Leça da Palmeira. 550 000 €.',
        hero='leca-37', hero_alt='T3 em Leça da Palmeira, junto ao mar',
        loc='Rua Francisco Sá Carneiro · Leça da Palmeira · Matosinhos', h1='T3 em Leça da Palmeira',
        sub='138 m², suíte, orientação Norte/Sul e 2 lugares de garagem, perto do mar.',
        price='550 000 €',
        quote='Viver em um apartamento onde o espaço não é um luxo, é realidade.',
        intro='Este magnífico T3 em Leça da Palmeira, com 138 m² de área, distingue-se pelas suas áreas generosas, excelente organização dos espaços, orientação Norte/Sul e pela comodidade de dispor de 2 lugares de garagem. Uma solução ideal para quem procura uma habitação familiar com dimensão, conforto e funcionalidade, numa das zonas mais procuradas do concelho de Matosinhos.',
        photos_intro=['leca-1', 'leca-21', 'leca-11'],
        photos_ficha=['leca-3', 'leca-4'],
        photos_rooms=['leca-18', 'leca-24', 'leca-12'],
        ficha_h2='Um T3 onde as áreas fazem a diferença',
        ficha_lead=['A zona social é marcada por uma ampla sala com 41,91 m², um espaço generoso e versátil, com capacidade para criar distintas áreas de estar e jantar, perfeito para receber família e amigos.',
                    'A cozinha, com 9,53 m², é complementada por uma prática lavandaria de 3,36 m², proporcionando maior funcionalidade no dia a dia. Na zona privada, uma distribuição pensada para garantir conforto e privacidade.'],
        facts=[('Área útil', '138 m²'), ('Sala', '41,91 m²'), ('Quartos', '3 · 1 suíte'), ('Casas de banho', '2'),
               ('Garagem', '2 lugares'), ('Arrumação', '5,32 m²'), ('Orientação', 'Norte / Sul'), ('Certificado energético', 'C')],
        rooms_h3='Áreas por divisão',
        rooms=[('Sala', '41,91 m²'), ('Suíte', '18,78 m²'), ('Casa de banho da suíte', '5,18 m²'), ('Quarto', '13,37 m²'),
               ('Quarto', '11,12 m²'), ('Cozinha', '9,53 m²'), ('Vestíbulo dos quartos', '5,45 m²'), ('Arrumação', '5,32 m²'),
               ('Casa de banho comum', '4,00 m²'), ('Vestíbulo de entrada', '3,55 m²'), ('Vestíbulo', '3,50 m²'), ('Lavandaria', '3,36 m²'),
               ('2 lugares de garagem', '27,95 m²')],
        feat_h3='Conforto e equipamento',
        features=['Pavimento em soalho de afizélia com piso radiante', 'Teto falso em gesso cartonado', 'Porta de segurança',
                  'Recuperador de calor', 'Banheiras', 'Termoacumulador', 'Exaustor', 'Videoporteiro',
                  'Caixilharia com vidro duplo', 'Orientação Norte/Sul'],
        extras=[
            dict(id='garagem', eb='Estacionamento', h2='2 lugares de garagem', dark=True,
                 photos=['leca-32', 'leca-31'],
                 paras=['A propriedade dispõe ainda de 2 lugares de estacionamento, com uma área indicada de 27,95 m², proporcionando uma importante comodidade para quem valoriza estacionamento privativo e espaço adicional.']),
            dict(id='destaque', eb='Em destaque', h2='O essencial deste T3', photos=['leca-5', 'leca-27', 'leca-30'],
                 chips=['T3 com suíte', 'Sala de 41,91 m²', '2 lugares de garagem', 'Orientação Norte/Sul', 'Soalho em afizélia',
                        'Recuperador de calor', 'Caixilharia com vidro duplo', 'Porta de segurança', 'Videoporteiro', 'Arrumos de 5,32 m²']),
        ],
        closing=dict(id='espaco', eb='Para quem valoriza espaço', h2='Um apartamento para quem valoriza espaço', photos=['leca-7'],
                     paras=['Mais do que um simples T3, este é um apartamento pensado para quem procura áreas generosas, conforto e uma verdadeira sensação de espaço.',
                            'A combinação entre a dimensão da habitação, a sala de quase 42 m², a suíte, os dois lugares de garagem e a localização em Leça da Palmeira faz desta uma solução particularmente interessante para famílias que não querem abdicar de espaço e qualidade de vida.',
                            'Venha conhecer e descubra o espaço que este T3 tem para oferecer.']),
        gallery=LECA_G, alt='T3 em Leça da Palmeira', gal_h2='Por dentro e por fora',
        loc_h2='Leça da Palmeira: qualidade de vida perto de tudo',
        loc_txt='A localização na Rua Francisco Sá Carneiro permite conjugar a tranquilidade de uma zona residencial com a proximidade a comércio, serviços, escolas, restauração e acessibilidades. O mar, as praias de Leça da Palmeira e a marginal estão por perto, com excelentes ligações a Matosinhos, Porto, Maia, aeroporto e principais vias rodoviárias.',
        maps='Rua Francisco Sá Carneiro, Leça da Palmeira', geo=(41.1937336, -8.7060774),
        legal='Informação sujeita a confirmação; áreas e características segundo a ficha CENTURY 21.',
        video='vU0bXm_uhGk', video_vertical=True, video_img='leca-40',
        video_h2='Leça da Palmeira, junto às Piscinas das Marés', tour=None,
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
        maps='Rua Senhora da Luz, Foz do Douro, Porto', geo=(41.1512834, -8.6767872),
        legal='Informação sujeita a confirmação; áreas e características segundo a ficha CENTURY 21.',
        video='zno11IhgXtE', tour='https://realsee.ai/xGWWkzlx', tour_img='foz-f2', video_img='foz-f79',
    ),
    'bosquepicua': dict(
        ref='C0393-01555', curto='T2+1 Bosque da Pícua',
        title='T2+1 com terraço e box no Bosque da Pícua · Cordial Level',
        desc='T2+1 em construção no Bosque, Parque da Pícua, Águas Santas, com entrega prevista em 2028: 92,30 m², terraço de 26,65 m², box de 33 m² para 2 carros e certificado energético A.',
        hero=None, hero_alt='',
        loc='Bosque · Parque da Pícua · Águas Santas · Maia', h1='T2+1 no Bosque da Pícua',
        sub='Em construção, com entrega prevista em 2028. Terraço privativo de 26,65 m², box de 33 m² para dois carros e jardins à porta.',
        price='Preço sob consulta',
        quote='Viver dentro de um parque, a oito minutos do centro do Porto.',
        intro='Um T2+1 com áreas generosas e acabamentos de alta gama no Bosque, o empreendimento do Parque da Pícua, em Águas Santas, em construção e com entrega prevista em 2028. Suite com closet, um espaço extra para escritório, sala e cozinha em open space com 33,50 m² e um deck privativo de 26,65 m² para refeições ao ar livre. No piso -2, uma garagem em box com 33 m², com lugar para dois carros.',
        photos_intro=['bp-fachada', 'bp-lagos', 'bp-esquina'],
        ficha_h2='Um T2+1 pensado para viver dentro e fora',
        ficha_lead=['A zona social junta sala e cozinha num só espaço com 33,50 m², amplo e luminoso, com ligação ao terraço. A suite tem 19,65 m² e closet; o segundo quarto tem 11,60 m².',
                    'O espaço +1, com 5,20 m², serve de escritório para teletrabalho ou de quarto de apoio. Duas casas de banho completas.'],
        facts=[('Área útil', '92,30 m²'), ('Área bruta', '118,95 m²'), ('Terraço', '26,65 m²'), ('Quartos', '2 + escritório'),
               ('Casas de banho', '2'), ('Garagem', 'Box 33 m²'), ('Certificado energético', 'A'), ('Entrega prevista', '2028')],
        rooms_h3='Áreas por divisão',
        rooms=[('Sala e cozinha', '33,50 m²'), ('Suite com closet', '19,65 m²'), ('Quarto', '11,60 m²'), ('Espaço +1 (escritório)', '5,20 m²'),
               ('Terraço / deck privativo', '26,65 m²'), ('Garagem em box, piso -2 (2 lugares)', '33 m²')],
        feat_h3='Acabamentos e conforto',
        features=['Cozinha equipada Bosch: placa de indução, forno, micro-ondas, combinado e máquina de lavar loiça', 'Exaustor',
                  'Pré-instalação de ar condicionado', 'Bomba de calor de alta eficiência para águas sanitárias',
                  'Caixilharia em alumínio com corte térmico e vidros duplos', 'Pavimento melamínico de alta durabilidade',
                  'Aspiração central', 'Certificado energético A'],
        extras=[
            dict(id='garagem', eb='Estacionamento', h2='Uma box de 33 m² para dois carros', dark=True,
                 paras=['A fração inclui uma garagem em box fechada no piso -2, com uns invulgares 33 m²: espaço para dois carros e para arrumação.']),
            dict(id='empreendimento', eb='O empreendimento', h2='Bosque, no Parque da Pícua', photos=['bp-logradouro', 'bp-jardim'],
                 paras=['O Bosque é um projeto de construção anti-sísmica e sustentável, com 1,5 hectares dedicados a espaços verdes, jardins e lagos, e espaços comuns como ginásio, salas de lazer e coworking.',
                        'O edifício está em construção, com entrega prevista em 2028. As imagens nesta página são simulações do edifício concluído, criadas a partir de fotografias da obra.'],
                 chips=['Entrega prevista em 2028', 'Terraço de 26,65 m²', 'Box de 33 m² · 2 lugares', 'Suite com closet', 'Escritório', 'Certificado A', 'Cozinha Bosch', 'Aspiração central']),
        ],
        gallery=[('bp-fachada', 'Simulação: fachada principal com terraços ajardinados'), ('bp-lagos', 'Simulação: vista aérea com jardins e lagos'),
                 ('bp-esquina', 'Simulação: esquina do edifício e arruamento arborizado'), ('bp-logradouro', 'Simulação: logradouro com jardins privativos'),
                 ('bp-cobertura', 'Simulação: coberturas ajardinadas'), ('bp-jardim', 'Simulação: jardim com oliveiras e espelhos de água'),
                 ('bp-parque', 'Simulação: o edifício, os lagos e o relvado')],
        sim={'bp-fachada', 'bp-lagos', 'bp-esquina', 'bp-logradouro', 'bp-cobertura', 'bp-jardim', 'bp-parque'},
        alt='Bosque, Parque da Pícua', gal_h2='O Bosque, depois de concluído',
        gal_note='As imagens são simulações geradas digitalmente a partir de fotografias da obra e não são vinculativas.',
        loc_h2='Pícua, Águas Santas: sossego a minutos do Porto',
        loc_txt='Junto ao Jardim da Pícua e ao Parque Urbano dos Moutidos, com a A4, A3, A41, VCI e Circunvalação a poucos minutos. Hospital de São João e Polo Universitário a 6 minutos e centro do Porto a 8 minutos, segundo a ficha do imóvel.',
        maps='Pícua, Águas Santas, Maia', geo=(41.2037790756507, -8.56774606227663),
        legal='Informação sujeita a confirmação; áreas e características segundo a ficha CENTURY 21. Imagens do empreendimento: simulações, não vinculativas.',
        video=None, tour=None,
    ),

    'anteroquental': dict(
        ref='C0393-01689', curto='T2 Antero de Quental',
        title='T2 remodelado na Rua Antero de Quental, Porto · Cordial Level',
        desc='T2 com 77,30 m², totalmente remodelado e com cozinha equipada, na Rua Antero de Quental, no Porto. Pronto a habitar. 349 000 €.',
        hero='aq-lapa', hero_pos='78% 30%', hero_alt='A Igreja da Lapa e a Rua Antero de Quental, no Porto, vistas de drone',
        loc='Rua Antero de Quental · Porto', h1='T2 remodelado na Antero de Quental',
        sub='77,30 m², cozinha equipada e casa de banho nova, numa zona central e consolidada do Porto.',
        price='349 000 €',
        quote='Pronto a habitar, no coração do Porto.',
        intro='Apartamento T2 com 77,30 m², totalmente remodelado, na Rua Antero de Quental. Uma solução funcional e atual, pronta a habitar, adequada tanto para habitação própria como para investimento, perto de comércio, serviços, restauração e transportes públicos.',
        photos_intro=['aq-21', 'aq-1', 'aq-3'],
        ficha_h2='Remodelado, equipado e pronto a habitar',
        ficha_lead=['A sala junta zona de estar e de refeições, com muita luz natural e vista desafogada sobre o verde. A cozinha, remodelada e equipada, tem espaço para uma mesa de apoio.',
                    'Dois quartos amplos, uma casa de banho completamente renovada com base de duche e um corredor de distribuição que separa a zona social da zona privada.'],
        photos_ficha=['aq-14', 'aq-19'],
        facts=[('Área útil', '77,30 m²'), ('Área bruta', '78,43 m²'), ('Quartos', '2'), ('Casas de banho', '1'),
               ('Estado', 'Remodelado'), ('Cozinha', 'Equipada'), ('Certificado energético', 'D'), ('Tipologia', 'T2')],
        photos_rooms=['aq-4', 'aq-11', 'aq-6'],
        feat_h3='Equipamento e documentação',
        features=['Cozinha equipada com placa e exaustor', 'Frigorífico', 'Máquina de lavar loiça', 'Máquina de lavar roupa',
                  'Casa de banho renovada, com base de duche', 'Pavimento flutuante em todo o apartamento',
                  'Certificado energético D', 'Licença de utilização n.º 423/1983'],
        extras=[
            dict(id='lapa', eb='A rua', h2='Junto à Igreja da Lapa', photos=['aq-lapa', 'aq-rua'],
                 paras=['A Rua Antero de Quental parte do Largo da Lapa, ao lado da igreja barroca que é uma das imagens do Porto. Uma zona consolidada e central, com comércio, serviços e transportes à porta.']),
            dict(id='vista', eb='Luz e vista', h2='Janelas abertas sobre o verde', dark=True, photos=['aq-27', 'aq-28'],
                 paras=['As janelas da sala e dos quartos abrem para um interior de quarteirão arborizado: luz natural, sossego e uma vista desafogada, no centro da cidade.']),
            dict(id='destaque', eb='Em destaque', h2='O essencial deste T2', photos=['aq-24', 'aq-5', 'aq-18'],
                 chips=['T2 com 77,30 m²', 'Totalmente remodelado', 'Pronto a habitar', 'Cozinha equipada', 'Casa de banho nova',
                        'Zona central do Porto', 'Habitação ou investimento']),
        ],
        closing=dict(id='versatil', eb='Uma solução versátil', h2='Para viver ou para investir', photos=['aq-30'],
                     paras=['Pelas suas características, localização e estado de conservação, este T2 é uma opção interessante para quem procura casa no Porto ou para quem pretende investir no mercado imobiliário.',
                            'Marque a sua visita e venha conhecer este apartamento.']),
        gallery=[('aq-20', 'Sala'), ('aq-22', 'Sala'), ('aq-23', 'Sala'), ('aq-24', 'Sala com vista'), ('aq-21', 'Zona de refeições'),
                 ('aq-26', 'Zona de refeições'), ('aq-1', 'Cozinha equipada'), ('aq-14', 'Cozinha equipada'), ('aq-16', 'Cozinha'),
                 ('aq-17', 'Cozinha'), ('aq-19', 'Cozinha com zona de refeições'), ('aq-18', 'Zona de lavandaria'),
                 ('aq-11', 'Casa de banho renovada'), ('aq-12', 'Casa de banho renovada'), ('aq-3', 'Quarto'), ('aq-4', 'Quarto'),
                 ('aq-5', 'Quarto'), ('aq-6', 'Quarto'), ('aq-8', 'Quarto'), ('aq-9', 'Quarto'), ('aq-13', 'Entrada'), ('aq-15', 'Corredor'),
                 ('aq-27', 'Vista da janela'), ('aq-28', 'Vista da janela'), ('aq-30', 'O edifício'), ('aq-31', 'A rua e o edifício'),
                 ('aq-lapa', 'A Igreja da Lapa e a Rua Antero de Quental, vistas de drone'), ('aq-rua', 'A Rua Antero de Quental, vista de drone')],
        alt='T2 na Rua Antero de Quental, Porto', gal_h2='Por dentro e por fora',
        loc_h2='Antero de Quental: centralidade e mobilidade',
        loc_txt='Situado na Rua Antero de Quental, numa zona consolidada da cidade do Porto, o apartamento beneficia da proximidade a comércio, serviços, restauração, transportes públicos e equipamentos do dia a dia, com acesso rápido a diferentes zonas da cidade.',
        maps='Rua Antero de Quental, Porto', geo=(41.1602049, -8.6116069),
        legal='Informação sujeita a confirmação; áreas e características segundo a ficha CENTURY 21.',
        video=None, tour='https://realsee.ai/bbEEVDWB', tour_img='aq-22',
    ),
    'moncao': dict(
        ref='C0393-01441 · C0393-01442', refs=['C0393-01441', 'C0393-01442'], curto='Terrenos em Monção',
        title='Dois terrenos junto ao Rio Minho, em Monção · Cordial Level',
        desc='Dois terrenos de cultura e vinha em São Bento (Bela), Monção, na Região Demarcada do Alvarinho, perto do Rio Minho e das Termas: 3600 m² por 75 000 € e 1350 m² por 35 000 €.',
        hero='mc-rio-muralhas', hero_alt='O Rio Minho e as muralhas de Monção, vistos de drone',
        loc='São Bento (Bela) · Monção · Alto Minho', h1='Dois terrenos junto ao Rio Minho',
        sub='3600 m² e 1350 m² de terreno de cultura e vinha, na terra do Alvarinho, a minutos do rio, das Termas e do centro histórico.',
        price='75 000 € · 35 000 €',
        quote='Onde o coração do Alvarinho encontra a serenidade do Rio Minho.',
        intro='Dois terrenos rústicos de cultura e vinha na freguesia de São Bento (Bela), em Monção, na Região Demarcada do Vinho Alvarinho. Solo fértil para vinha, sossego total e o Rio Minho, as Termas e o centro histórico a poucos minutos. Para um projeto de vida, uma exploração agrícola ou um investimento a estudar.',
        photos_intro=['mc-muralhas', 'mc-rio', 't1-igreja'],
        navs=[('terreno1', 'Terreno 3600 m²'), ('terreno2', 'Terreno 1350 m²'), ('galeria', 'Fotografias')],
        lotes=[
            dict(id='terreno1', ref='C0393-01441', eb='Terreno 1 · Panasqueira, junto ao Recanto de São Bento',
                 h2='Terreno com 3600 m²', price='75 000 €', geo=(42.072910104535, -8.43833682762678),
                 paras=['Situado imediatamente ao lado do Recanto de São Bento, o terreno tem duas frentes, confrontando com caminhos a Norte e a Sul, o que garante boa acessibilidade e versatilidade para qualquer projeto.',
                        'Terreno rústico de cultura e vinha, com solo fértil e árvores de fruto. O Rio Minho fica a cerca de 2 minutos, as Termas de Monção a 2 km e o centro histórico a cerca de 5 minutos.'],
                 photos=[['t1-area'], ['t1-limites', 't1-d4'], ['t1-3', 't1-1', 't1-acesso']],
                 facts=[('Área do terreno', '3600 m²'), ('Preço por m²', '20,83 €'), ('Frentes', '2 · Norte e Sul'), ('Classificação', 'Rústico')],
                 chips=['Vinha · Região do Alvarinho', 'Árvores de fruto', 'Acesso por estrada', 'Duas frentes', 'Rio Minho a ~2 min', 'Termas a 2 km']),
            dict(id='terreno2', ref='C0393-01442', eb='Terreno 2 · Codeçais', dark=True,
                 h2='Terreno com 1350 m²', price='35 000 €', geo=(42.065256, -8.4206685),
                 paras=['No lugar de Codeçais, também em São Bento (Bela), um terreno rústico de cultura e vinha com 1350 m², boa exposição solar e vista sobre a vila.',
                        'O Rio Minho fica a cerca de 5 minutos, as Termas de Monção a cerca de 8 minutos e o centro histórico a cerca de 5 minutos.'],
                 photos=[['t2-area'], ['t2-limites', 't2-d1'], ['t2-d4', 't2-acesso', 't2-portao']],
                 facts=[('Área do terreno', '1350 m²'), ('Preço por m²', '25,93 €'), ('Exposição', 'Boa exposição solar'), ('Classificação', 'Rústico')],
                 chips=['Vinha · Região do Alvarinho', 'Árvores de fruto', 'Vista sobre a vila', 'Perto da igreja', 'Rio Minho a ~5 min']),
        ],
        extras=[
            dict(id='potencial', eb='O potencial', h2='Vinha, turismo ou um refúgio seu',
                 paras=['A região é conhecida pelo Alvarinho, pelas Termas e pelo turismo de natureza. Estes terrenos servem para vinha e cultura e podem ser o ponto de partida para um projeto turístico ou de habitação.',
                        'Importante: são terrenos classificados como rústicos. A possibilidade de construir — casa, alojamento local, glamping ou outro equipamento — depende do Plano Diretor Municipal de Monção e de licenciamento pela Câmara Municipal, não estando garantida. Antes de comprar com esse objetivo, recomendamos um pedido de informação prévia à Câmara.'],
                 photos=['mc-rio-muralhas', 't1-placa', 't2-d3']),
            dict(id='projetos', eb='Projetos possíveis', h2='O Terreno 1 hoje, e duas ideias para o seu futuro', dark=True,
                 paras=['Primeiro, o terreno de 3600 m² como está hoje. Depois, duas simulações: uma moradia térrea com piscina no meio da vinha e um pequeno núcleo de glamping em madeira.',
                        'Imagens ilustrativas, geradas digitalmente. Não são projetos aprovados: qualquer construção depende do PDM de Monção e de licenciamento pela Câmara Municipal.'],
                 photos=['mc-t1-hoje', 'mc-sim-casa', 'mc-sim-glamping']),
            dict(id='projetos2', eb='Projetos possíveis · Terreno 2', h2='Uma casa ou duas cabanas nos socalcos',
                 paras=['O terreno de 1350 m² hoje e duas simulações: socalcos de pedra recuperados com vinha, com uma pequena casa no socalco mais alto ou duas cabanas de madeira para turismo rural.',
                        'Imagem ilustrativa, gerada digitalmente. Não é um projeto aprovado: qualquer construção depende do PDM de Monção e de licenciamento pela Câmara Municipal.'],
                 photos=['mc-t2-hoje', 'mc-sim-t2-casa', 'mc-sim-t2-cabanas']),
        ],
        facts=[], features=[],
        gallery=[('t1-area', 'Terreno 1: limites aproximados dos 3600 m²'), ('t1-limites', 'Terreno 1: limites aproximados'),
                 ('t1-d4', 'Terreno 1 visto de drone'), ('t1-d1', 'Terreno 1 visto de drone'), ('t1-d2', 'Terreno 1 e o Recanto de São Bento'),
                 ('t1-d3', 'Terreno 1 e a serra'), ('t1-d5', 'Terreno 1 visto de drone'), ('t1-d6', 'Terreno 1 visto de drone'),
                 ('t1-d7', 'Terreno 1 visto de drone'), ('t1-1', 'Terreno 1'), ('t1-2', 'Terreno 1'), ('t1-3', 'Terreno 1: árvores'),
                 ('t1-4', 'Terreno 1: muro e caminho'), ('t1-5', 'Terreno 1: caminho de acesso'), ('t1-6', 'Terreno 1'),
                 ('t1-7', 'Terreno 1: frente para o caminho'), ('t1-acesso', 'Acesso pelo Recanto de São Bento'),
                 ('t1-placa', 'Recanto de São Bento'), ('t1-igreja', 'Igreja de São Bento'),
                 ('t2-area', 'Terreno 2: limites aproximados dos 1350 m²'), ('t2-limites', 'Terreno 2: limites aproximados'),
                 ('t2-d1', 'Terreno 2 visto de drone'), ('t2-d2', 'Terreno 2 visto de drone'), ('t2-d3', 'Terreno 2 visto de drone'),
                 ('t2-d4', 'Terreno 2 e a paisagem'), ('t2-acesso', 'Terreno 2: acesso'), ('t2-placa', 'Terreno 2'), ('t2-portao', 'Terreno 2: entrada'),
                 ('mc-rio', 'O Rio Minho em Monção'), ('mc-rio-muralhas', 'O Rio Minho e as muralhas'), ('mc-muralhas', 'As muralhas e o centro de Monção'),
                 ('mc-sim-casa', 'Simulação: moradia com piscina no meio da vinha (Terreno 1)'), ('mc-sim-glamping', 'Simulação: núcleo de glamping em madeira (Terreno 1)'),
                 ('mc-sim-t2-casa', 'Simulação: casa no topo dos socalcos (Terreno 2)'), ('mc-sim-t2-cabanas', 'Simulação: duas cabanas de madeira nos socalcos (Terreno 2)')],
        sim={'mc-sim-casa', 'mc-sim-glamping', 'mc-sim-t2-casa', 'mc-sim-t2-cabanas'},
        alt='Terrenos em Monção', gal_h2='Os terrenos, o rio e a vila',
        gal_note='Os limites desenhados nas fotografias são aproximados e servem apenas de orientação.',
        loc_h2='São Bento (Bela), Monção',
        loc_txt='Os dois terrenos ficam na freguesia de São Bento (Bela), a poucos minutos do Rio Minho, das Termas de Monção e do centro histórico, com as suas muralhas, gastronomia, comércio e serviços. O mapa mostra o Terreno 1; a localização de cada terreno está na respetiva secção.',
        maps='São Bento, Bela, Monção', geo=(42.072910104535, -8.43833682762678),
        legal='Informação sujeita a confirmação; áreas e características segundo as fichas CENTURY 21. Terrenos rústicos: a edificabilidade depende do PDM de Monção e de licenciamento municipal.',
        video='yo7RN7u6JJY', video_img='t1-d4', video_h2='Monção: dois terrenos entre o Minho e a Galiza', tour=None,
    ),
}

if __name__ == '__main__':
    for slug, p in IMOVEIS.items():
        p['slug'] = slug
        d = os.path.join(ROOT, 'cordiallevel', slug)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'index.html'), 'w') as f:
            f.write(build(p))
        # endereço antigo -> novo (links já partilhados no YouTube e redes)
        if slug not in ('t3leca', 'casaraofoz', 'bosquepicua'):
            print('ok', slug, len(p['gallery']), 'fotos'); continue
        old = os.path.join(ROOT, slug)
        os.makedirs(old, exist_ok=True)
        new = f'https://usinavideos.pt/cordiallevel/{slug}/'
        with open(os.path.join(old, 'index.html'), 'w') as f:
            f.write(f'<!doctype html><html lang="pt-PT"><head><meta charset="utf-8"><title>{e(p["title"])}</title>'
                    f'<link rel="canonical" href="{new}"><meta http-equiv="refresh" content="0; url=/cordiallevel/{slug}/">'
                    f'<script>location.replace("/cordiallevel/{slug}/"+location.hash)</script></head>'
                    f'<body><p><a href="/cordiallevel/{slug}/">{e(p["title"])}</a></p></body></html>')
        print('ok', slug, len(p['gallery']), 'fotos')
