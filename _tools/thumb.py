#!/usr/bin/env python3
"""Thumbnails YouTube 1280x720 Cordial Level. Uso: python3 _tools/thumb.py <saida_dir>"""
import sys, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / '_tools'))
from carrossel import FONTS
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
CSS = FONTS + """*{margin:0;padding:0;box-sizing:border-box}html,body{width:1280px;height:720px;overflow:hidden}
.t{position:relative;width:1280px;height:720px;overflow:hidden;font-family:'Mulish';font-variant-numeric:lining-nums;color:#F7F5F0}
.t>img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.g{position:absolute;inset:0;background:linear-gradient(90deg,rgba(18,40,75,.96) 0%,rgba(18,40,75,.85) 38%,rgba(18,40,75,.1) 70%,rgba(18,40,75,0) 100%)}
.lg{position:absolute;left:56px;top:44px;height:110px}
.tx{position:absolute;left:56px;top:190px;width:640px}
.eb{font-weight:800;font-size:26px;letter-spacing:.18em;color:#D4B562;text-transform:uppercase}
h1{font-family:'Cormorant Garamond';font-weight:600;font-size:118px;line-height:.92;margin:10px 0 18px}
.ck{display:flex;flex-direction:column;gap:10px}
.ck span{font-weight:800;font-size:34px;line-height:1.1}
.ck span b{color:#D4B562}
.pr{position:absolute;left:56px;bottom:46px;background:#D4B562;color:#12284B;font-family:'Cormorant Garamond';font-weight:600;font-size:64px;padding:2px 26px 6px;border-radius:8px}
"""
def thumb(name, img, eb, h1, lines, price):
    ck = ''.join(f'<span>{l}</span>' for l in lines)
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="t"><img class="bg" src="file://{img}"><div class="g"></div><img class="lg" src="file://{ROOT}/cordiallevel/img/logo-cordial-level-claro.png"><div class="tx"><div class="eb">{eb}</div><h1>{h1}</h1><div class="ck">{ck}</div></div><div class="pr">{price}</div></div></body></html>'
    f = OUT / f'{name}.html'; f.write_text(html)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1280, 'height': 720})
        pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT / f'{name}.jpg'), type='jpeg', quality=90); b.close()
    f.unlink()
if __name__ == '__main__':
    L = ROOT / 't3leca/img'
    thumb('thumb-t3-leca-a', L / 'leca-37.jpg', 'Leça da Palmeira', 'T3 junto<br>ao mar', ['<b>✓</b> Sala de 42 m² · suíte', '<b>✓</b> 2 lugares de garagem'], '550 000 €')
    thumb('thumb-t3-leca-b', L / 'leca-1.jpg', 'Leça da Palmeira · T3', '138 m²<br>de espaço', ['<b>✓</b> Sala de 42 m² · suíte', '<b>✓</b> 2 lugares de garagem'], '550 000 €')


VCSS = FONTS + """*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;overflow:hidden}
.v{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Mulish';font-variant-numeric:lining-nums;color:#F7F5F0}
.v>img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.g{position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,40,75,.92) 0%,rgba(18,40,75,.55) 26%,rgba(18,40,75,0) 42%,rgba(18,40,75,0) 55%,rgba(18,40,75,.75) 72%,rgba(18,40,75,.95) 100%)}
.lg{position:absolute;left:50%;transform:translateX(-50%);top:120px;height:150px}
.top{position:absolute;left:70px;right:70px;top:330px;text-align:center}
.eb{font-weight:800;font-size:38px;letter-spacing:.2em;color:#D4B562;text-transform:uppercase}
h1{font-family:'Cormorant Garamond';font-weight:600;font-size:150px;line-height:.92;margin-top:14px;text-shadow:0 4px 24px rgba(0,0,0,.35)}
.bot{position:absolute;left:70px;right:180px;top:1180px}
.ck{display:flex;flex-direction:column;gap:14px}
.ck span{font-weight:800;font-size:46px;line-height:1.1}.ck b{color:#D4B562}
.pr{display:inline-block;margin-top:30px;background:#D4B562;color:#12284B;font-family:'Cormorant Garamond';font-weight:600;font-size:92px;padding:0 32px 8px;border-radius:12px}
"""


def vthumb(name, img, eb, h1, lines, price):
    ck = ''.join(f'<span>{l}</span>' for l in lines)
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{VCSS}</style></head><body><div class="v"><img class="bg" src="file://{img}"><div class="g"></div><img class="lg" src="file://{ROOT}/cordiallevel/img/logo-cordial-level-claro.png"><div class="top"><div class="eb">{eb}</div><h1>{h1}</h1></div><div class="bot"><div class="ck">{ck}</div><div class="pr">{price}</div></div></div></body></html>'
    f = OUT / f'{name}.html'; f.write_text(html)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT / f'{name}.jpg'), type='jpeg', quality=90); b.close()
    f.unlink()
