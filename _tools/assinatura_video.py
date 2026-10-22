#!/usr/bin/env python3
"""Assinaturas para vídeo (PNG transparente) Cordial Level · CENTURY 21 Arquitectos · AMI 11414.
Uso: python3 _tools/assinatura_video.py <saida_dir>"""
import sys, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / '_tools'))
from carrossel import FONTS
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
LOGO = f'file://{ROOT}/cordiallevel/img/logo-cordial-level-claro.png'
SIG = 'Cordial Level | CENTURY 21 Arquitectos · AMI 11414'
CSS = FONTS + """*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent;overflow:hidden}
.c{position:relative;font-family:'Mulish';font-variant-numeric:lining-nums;color:#F7F5F0}
.lt{position:absolute;display:flex;align-items:center;gap:28px;background:rgba(18,40,75,.92);border-left:6px solid #D4B562;padding:22px 34px 22px 26px;border-radius:0 14px 14px 0}
.lt img{height:96px}.lt .t b{display:block;font-family:'Cormorant Garamond';font-weight:600;font-size:40px;line-height:1.05}
.lt .t span{display:block;font-weight:700;font-size:24px;color:#D4B562;margin-top:6px;letter-spacing:.03em}
.lt .w{display:flex;gap:26px;margin-top:10px;font-weight:800;font-size:24px}.lt .w i{font-style:normal;color:#D4B562}
.bug{position:absolute;font-weight:800;font-size:22px;letter-spacing:.04em;background:rgba(18,40,75,.78);padding:8px 14px;border-radius:8px}
.end{position:absolute;inset:0;background:#12284B;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:26px}
.end img{height:230px}.end h2{font-family:'Cormorant Garamond';font-weight:500;font-style:italic;font-size:52px;color:#D4B562}
.end .who{display:flex;gap:28px}.end .who div{border:2px solid #D4B562;border-radius:16px;padding:18px 30px}
.end .who b{display:block;font-family:'Cormorant Garamond';font-weight:600;font-size:44px}.end .who span{display:block;font-weight:800;font-size:28px;color:#D4B562;margin-top:4px}
.end .web{font-weight:700;font-size:28px}.end .sig{font-weight:800;font-size:26px;letter-spacing:.05em;color:#C9D2DE}
.v .end .who{flex-direction:column;gap:20px}
"""
def shot(name, w, h, body, transparent=True):
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="c {"v" if h>w else ""}" style="width:{w}px;height:{h}px">{body}</div></body></html>'
    f = OUT / f'{name}.html'; f.write_text(html)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': w, 'height': h})
        pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT / f'{name}.png'), omit_background=transparent); b.close()
    f.unlink(); print(name)
WHO = '<div class="w"><span>Casemiro Ramos <i>935 101 667</i></span><span>Francisco Medeiros <i>912 706 395</i></span></div>'
END = lambda: f'''<div class="end"><img src="{LOGO}"><h2>A sua exigência, a nossa assinatura.</h2>
<div class="who"><div><b>Casemiro Ramos</b><span>WhatsApp 935 101 667</span></div><div><b>Francisco Medeiros</b><span>WhatsApp 912 706 395</span></div></div>
<div class="web">Todos os imóveis: century21.pt/consultores/cramos</div><div class="sig">{SIG}</div></div>'''
if __name__ == '__main__':
    # 16:9
    shot('01-oraculo-marca-16x9', 1920, 1080, f'<div class="lt" style="left:0;bottom:90px"><img src="{LOGO}"><div class="t"><b>Cordial Level</b><span>CENTURY 21 Arquitectos · AMI 11414</span></div></div>')
    shot('02-oraculo-contactos-16x9', 1920, 1080, f'<div class="lt" style="left:0;bottom:90px"><img src="{LOGO}"><div class="t"><b>Fale connosco no WhatsApp</b>{WHO}<span>{SIG}</span></div></div>')
    shot('03-selo-ami-16x9', 1920, 1080, f'<div class="bug" style="right:40px;top:36px">CENTURY 21 Arquitectos · AMI 11414</div>')
    shot('04-cartao-final-16x9', 1920, 1080, END(), transparent=False)
    # 9:16 (Reels, Shorts, TikTok) — longe das zonas tapadas pelos botões
    shot('05-oraculo-marca-9x16', 1080, 1920, f'<div class="lt" style="left:0;top:1220px;max-width:900px"><img src="{LOGO}"><div class="t"><b>Cordial Level</b><span>CENTURY 21 Arquitectos · AMI 11414</span></div></div>')
    shot('06-oraculo-contactos-9x16', 1080, 1920, f'<div class="lt" style="left:0;top:1160px;max-width:920px"><div class="t"><b>Fale connosco no WhatsApp</b><div class="w" style="flex-direction:column;gap:6px"><span>Casemiro Ramos <i>935 101 667</i></span><span>Francisco Medeiros <i>912 706 395</i></span></div><span>{SIG}</span></div></div>')
    shot('07-selo-ami-9x16', 1080, 1920, f'<div class="bug" style="left:40px;top:150px">CENTURY 21 Arquitectos · AMI 11414</div>')
    shot('08-cartao-final-9x16', 1080, 1920, END(), transparent=False)
