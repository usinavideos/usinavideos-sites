#!/usr/bin/env python3
"""Banners para o motoreseacao.com (medidas dos banners Fiat/Citroën do site).

Slider principal: 1920x784 · Faixa: 1200x300.
Uso: python3 _tools/banner_mea.py <pasta_saida>   (fontes em /tmp/fx, playwright)
"""
import pathlib, subprocess, sys, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
FX = pathlib.Path('/tmp/fx')
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'banners')
OUT.mkdir(parents=True, exist_ok=True)

FONTS = ''.join(
    f"@font-face{{font-family:'{fam}';src:url('file://{FX}/{f}') format('woff2');font-weight:{w};font-style:{st}}}"
    for fam, f, w, st in [
        ('Cormorant Garamond', 'cormorant-garamond-latin-500-normal.woff2', 500, 'normal'),
        ('Cormorant Garamond', 'cormorant-garamond-latin-600-normal.woff2', 600, 'normal'),
        ('Cormorant Garamond', 'cormorant-garamond-latin-500-italic.woff2', 500, 'italic'),
        ('Mulish', 'mulish-latin-400-normal.woff2', 400, 'normal'),
        ('Mulish', 'mulish-latin-600-normal.woff2', 600, 'normal'),
        ('Mulish', 'mulish-latin-700-normal.woff2', 700, 'normal'),
        ('Mulish', 'mulish-latin-800-normal.woff2', 800, 'normal'),
    ])

def f(p): return 'file://' + str(ROOT / p)

CL_LOGO = f('cordiallevel/img/logo-cordial-level-claro.png')
US_LOGO = f('img/logo/usina-horizontal-claro.svg')
WA = '<svg viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/></svg>'

BASE = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}body{width:%dpx;height:%dpx;overflow:hidden;font-family:Mulish,sans-serif;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums}
.b{position:relative;width:100%%;height:100%%;overflow:hidden}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
"""

# ---------- Cordial Level ----------
CL_CSS = """
.b{background:#13284A;color:#F7F5F0}
.ph{left:44%%;background-image:url('%s')}
.fade{position:absolute;inset:0;background:linear-gradient(90deg,#13284A 0,#13284A 44%%,rgba(19,40,74,.88) 52%%,rgba(19,40,74,0) 72%%)}
.gold{color:#D4B562}
"""
def cl_big():
    css = CL_CSS % f('cordiallevel/t3leca/img/leca-37.jpg') + """
.t{position:absolute;left:96px;top:56px;width:900px}
.logo{height:104px}
.eb{margin-top:30px;font-weight:800;font-size:22px;letter-spacing:.24em;color:#D4B562}
h1{margin-top:14px;font-family:'Cormorant Garamond';font-weight:600;font-size:76px;line-height:1.02}
p.s{margin-top:18px;font-size:26px;line-height:1.4;color:#D9DEE6;width:780px}
.row{display:flex;gap:18px;margin-top:28px;align-items:center}
.cta{background:#D4B562;color:#0E1E38;font-weight:800;font-size:26px;padding:20px 34px;border-radius:999px}
.row2{display:flex;gap:14px;margin-top:18px}
.wa{display:flex;gap:10px;align-items:center;font-weight:700;font-size:21px;color:#fff;border:2px solid rgba(255,255,255,.55);padding:12px 22px;border-radius:999px}
.ami{position:absolute;left:96px;bottom:40px;font-weight:800;font-size:19px;letter-spacing:.06em;color:#F7F5F0;opacity:.92}
.ami span{color:#D4B562}
"""
    html = f"""<div class="b"><div class="ph"></div><div class="fade"></div>
<div class="t"><img class="logo" src="{CL_LOGO}">
<div class="eb">IMÓVEIS E INVESTIMENTO EM PORTUGAL</div>
<h1>Viver ou investir em Portugal,<br>com quem conhece o terreno.</h1>
<p class="s">Casas, apartamentos e terrenos no Grande Porto e no Minho, apresentados em vídeo.</p>
<div class="row"><span class="cta">Conheça os imóveis →</span></div>
<div class="row2"><span class="wa">{WA} Casemiro · +351 935 101 667</span><span class="wa">{WA} Francisco · +351 912 706 395</span></div></div>
<div class="ami">Cordial Level | CENTURY 21 Arquitectos · AMI 11414 <span>· usinavideos.pt/cordiallevel</span></div></div>"""
    return css, html

def cl_strip():
    css = CL_CSS % f('cordiallevel/t3leca/img/leca-37.jpg') + """
.ph{left:58%}
.fade{background:linear-gradient(90deg,#13284A 0,#13284A 58%,rgba(19,40,74,.6) 66%,rgba(19,40,74,0) 82%)}
.logo{position:absolute;left:40px;top:50%;transform:translateY(-50%);height:96px}
.t{position:absolute;left:210px;top:84px;width:520px}
.eb{font-weight:800;font-size:13px;letter-spacing:.22em;color:#D4B562}
h1{margin-top:8px;font-family:'Cormorant Garamond';font-weight:600;font-size:40px;line-height:1.02}
.ami{margin-top:12px;font-weight:800;font-size:12.5px;letter-spacing:.05em;opacity:.92}
.cta{position:absolute;right:42px;top:50%;transform:translateY(-50%);background:#D4B562;color:#0E1E38;font-weight:800;font-size:19px;padding:15px 24px;border-radius:999px;box-shadow:0 6px 24px rgba(0,0,0,.35)}
"""
    html = f"""<div class="b"><div class="ph"></div><div class="fade"></div><img class="logo" src="{CL_LOGO}">
<div class="t"><div class="eb">IMÓVEIS E INVESTIMENTO EM PORTUGAL</div><h1>Viver ou investir em Portugal</h1>
<div class="ami">Cordial Level | CENTURY 21 Arquitectos · AMI 11414</div></div>
<span class="cta">Ver imóveis →</span></div>"""
    return css, html

# ---------- Usina Vídeos ----------
US_CSS = """
.b{background:#141213;color:#F2F0EB}
.ph{left:46%%;background-image:url('%s')}
.fade{position:absolute;inset:0;background:linear-gradient(90deg,#141213 0,#141213 46%%,rgba(20,18,19,.85) 54%%,rgba(20,18,19,0) 74%%)}
.stripe{display:flex;height:6px;border-radius:3px;overflow:hidden}.stripe i{flex:1}
"""
STRIPE = '<div class="stripe"><i style="background:#3EB15C"></i><i style="background:#E5AE29"></i><i style="background:#D0252F"></i></div>'
def us_big():
    css = US_CSS % f('cordiallevel/anteroquental/img/aq-lapa.jpg') + """
.t{position:absolute;left:96px;top:92px;width:900px}
.logo{height:118px}
.stripe{width:200px;margin-top:30px}
.eb{margin-top:34px;font-weight:800;font-size:22px;letter-spacing:.24em;color:#E5AE29}
h1{margin-top:14px;font-weight:800;font-size:66px;line-height:1.04;letter-spacing:-.01em}
p.s{margin-top:18px;font-size:26px;line-height:1.4;color:#D6D1CD;width:800px}
.row{display:flex;gap:18px;margin-top:34px;align-items:center}
.cta{background:#E5AE29;color:#141213;font-weight:800;font-size:26px;padding:20px 34px;border-radius:999px}
.wa{display:flex;gap:10px;align-items:center;font-weight:700;font-size:22px;color:#fff;border:2px solid rgba(255,255,255,.5);padding:17px 24px;border-radius:999px}
"""
    html = f"""<div class="b"><div class="ph"></div><div class="fade"></div>
<div class="t"><img class="logo" src="{US_LOGO}">{STRIPE}
<div class="eb">PRODUÇÃO AUDIOVISUAL · PORTUGAL</div>
<h1>Vídeo, drone e apresentações<br>digitais para imóveis.</h1>
<p class="s">Reportagem, fotografia e páginas premium para consultores e proprietários no Porto e no Norte.</p>
<div class="row"><span class="cta">usinavideos.pt →</span><span class="wa">{WA} +351 912 988 971</span></div></div></div>"""
    return css, html

def us_strip():
    css = US_CSS % f('cordiallevel/anteroquental/img/aq-lapa.jpg') + """
.ph{left:60%}
.fade{background:linear-gradient(90deg,#141213 0,#141213 60%,rgba(20,18,19,.6) 68%,rgba(20,18,19,0) 84%)}
.logo{position:absolute;left:40px;top:58px;height:72px}
.stripe{position:absolute;left:40px;top:150px;width:120px;height:4px}
.sub{position:absolute;left:40px;top:176px;font-weight:700;font-size:15px;color:#D6D1CD;letter-spacing:.02em}
.t{position:absolute;left:400px;top:62px;width:340px}
h1{font-weight:800;font-size:30px;line-height:1.08}
.cta{position:absolute;right:42px;top:50%;transform:translateY(-50%);background:#E5AE29;color:#141213;font-weight:800;font-size:19px;padding:15px 24px;border-radius:999px;box-shadow:0 6px 24px rgba(0,0,0,.35)}
"""
    html = f"""<div class="b"><div class="ph"></div><div class="fade"></div><img class="logo" src="{US_LOGO}">{STRIPE}
<div class="sub">Produção audiovisual · Porto</div>
<div class="t"><h1>Vídeo, drone e apresentações para imóveis</h1></div>
<span class="cta">usinavideos.pt →</span></div>"""
    return css, html

JOBS = [('cordial-level-slider-1920x784', 1920, 784, cl_big), ('cordial-level-faixa-1200x300', 1200, 300, cl_strip),
        ('usina-videos-slider-1920x784', 1920, 784, us_big), ('usina-videos-faixa-1200x300', 1200, 300, us_strip)]

pages = []
for name, w, h, fn in JOBS:
    css, body = fn()
    p = OUT / f'{name}.html'
    p.write_text(f'<!doctype html><meta charset="utf-8"><style>{BASE % (w, h)}{css}</style>{body}')
    pages.append([str(p), str(OUT / f'{name}.png'), w, h])

js = """const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const [src,out,w,h] of %s){const p=await b.newPage({viewport:{width:w,height:h}});await p.goto('file://'+src);
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);await p.screenshot({path:out});}
await b.close();})();""" % json.dumps(pages)
subprocess.run(['node', '-e', js], check=True, env={**__import__('os').environ, 'NODE_PATH': subprocess.check_output(['npm', 'root', '-g'], text=True).strip()})
from PIL import Image
for src, out, w, h in pages:
    Image.open(out).convert('RGB').save(out.replace('.png', '.jpg'), quality=90, optimize=True, progressive=True)
    pathlib.Path(out).unlink(); pathlib.Path(src).unlink()
    print('ok', out.replace('.png', '.jpg'))
