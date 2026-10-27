#!/usr/bin/env python3
"""Gera carrosséis 1080x1350 (Instagram/Facebook) da Cordial Level a partir das fotografias da Usina.
Uso: python3 _tools/carrossel.py <pasta_saida>   (precisa das fontes em /tmp/fx e do playwright)"""
import os, sys, html, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
FX = pathlib.Path('/tmp/fx')
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / '_carrosseis')
e = html.escape

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

CSS = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden;background:#12284B}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Mulish',sans-serif;color:#F7F5F0;font-variant-numeric:lining-nums}
.s>img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,40,75,.55) 0%,rgba(18,40,75,0) 22%,rgba(18,40,75,0) 48%,rgba(18,40,75,.92) 78%,#12284B 100%)}
.top{position:absolute;left:64px;right:64px;top:56px;display:flex;justify-content:space-between;align-items:center}
.top img{height:150px}
.pg{font-size:22px;letter-spacing:.2em;color:#F7F5F0;font-weight:700;background:rgba(18,40,75,.55);padding:10px 16px;border-radius:999px}
.txt{position:absolute;left:64px;right:64px;bottom:96px}
.eb{font-size:26px;letter-spacing:.22em;text-transform:uppercase;color:#D4B562;font-weight:800;margin-bottom:18px}
h1{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:104px;line-height:.98;margin-bottom:22px}
h2{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:78px;line-height:1.02;margin-bottom:18px}
p{font-size:34px;line-height:1.38;color:#E8ECF2;max-width:900px}
.price{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:84px;color:#D4B562;margin-top:18px}
.chips{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}
.chips span{border:2px solid #D4B562;color:#F7F5F0;font-weight:700;font-size:26px;padding:10px 20px;border-radius:999px;background:rgba(18,40,75,.6)}
.ami{position:absolute;left:64px;right:64px;bottom:34px;font-size:21px;font-weight:700;letter-spacing:.06em;color:#C9D2DE}
.band>img.bg{height:800px;bottom:auto}
.band .shade{background:linear-gradient(180deg,rgba(18,40,75,.55) 0%,rgba(18,40,75,0) 20%,rgba(18,40,75,0) 45%,#12284B 60%,#12284B 100%)}
.band .ia{top:auto;bottom:auto;top:700px}
.band .txt{top:850px;bottom:auto}
.band .swipe{bottom:96px}
.swipe{position:absolute;right:64px;bottom:96px;font-size:24px;font-weight:700;letter-spacing:.12em;color:#D4B562}
.ia{position:absolute;left:64px;top:200px;font-size:20px;font-weight:800;letter-spacing:.12em;color:#E0A93B;border:2px solid #E0A93B;padding:6px 12px;background:rgba(18,40,75,.75)}
/* final */
.end{background:#F7F5F0;color:#1B3A6B;padding:72px 64px;display:flex;flex-direction:column}
.end .logo{height:190px;align-self:center;margin-bottom:26px}
.end h2{color:#1B3A6B;text-align:center;font-size:66px}
.end .lead{color:#5E6873;text-align:center;font-size:30px;margin:0 auto 30px;max-width:880px}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:2px;background:#E3DED2;border:2px solid #E3DED2;margin-bottom:30px}
.facts div{background:#fff;padding:18px 22px}
.facts b{display:block;font-family:'Cormorant Garamond',serif;font-size:56px;font-weight:600;color:#1B3A6B;line-height:1.05}
.facts i{font-style:normal;font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:#5E6873;font-weight:700}
.who{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.who div{background:#1B3A6B;color:#F7F5F0;padding:22px 24px;border-radius:14px}
.who b{display:block;font-family:'Cormorant Garamond',serif;font-size:46px;font-weight:600}
.who span{display:block;font-size:28px;font-weight:700;color:#D4B562;margin-top:4px}
.web{margin-top:auto;text-align:center;font-size:30px;font-weight:700;color:#1B3A6B}
.web small{display:block;font-size:20px;font-weight:600;color:#5E6873;margin-top:8px;letter-spacing:.04em}
"""


def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def photo_slide(img, n, total, eb, title, text='', price='', chips=(), big=False, ia=False, logo=True, band=False):
    lg = f'<img src="file://{ROOT}/cordiallevel/img/logo-cordial-level-claro.png">' if logo else '<span></span>'
    h = f'<h1>{e(title)}</h1>' if big else f'<h2>{e(title)}</h2>'
    t = f'<p>{e(text)}</p>' if text else ''
    pr = f'<div class="price">{e(price)}</div>' if price else ''
    ch = ('<div class="chips">' + ''.join(f'<span>{e(c)}</span>' for c in chips) + '</div>') if chips else ''
    sw = '<div class="swipe">DESLIZE →</div>' if n == 1 else ''
    iab = f'<div class="ia">{e(ia if isinstance(ia, str) else "SIMULAÇÃO IA · ILUSTRATIVA")}</div>' if ia else ''
    if band:
        return page(f'''<div class="s band"><img class="bg" src="file://{img}"><div class="shade"></div>
<div class="top">{lg}<span class="pg">{n}/{total}</span></div>{iab}
<div class="txt"><div class="eb">{e(eb)}</div>{h}{t}{pr}{ch}</div>{sw}<div class="ami">Cordial Level | CENTURY 21 Arquitectos · AMI 11414</div></div>''')
    return page(f'''<div class="s"><img class="bg" src="file://{img}"><div class="shade"></div>
<div class="top">{lg}<span class="pg">{n}/{total}</span></div>{iab}
<div class="txt"><div class="eb">{e(eb)}</div>{h}{t}{pr}{ch}</div>{sw}<div class="ami">Cordial Level | CENTURY 21 Arquitectos · AMI 11414</div></div>''')


def end_slide(n, total, title, lead, facts, link, link_label='Apresentação completa'):
    fx = ''.join(f'<div><b>{e(v)}</b><i>{e(k)}</i></div>' for k, v in facts)
    return page(f'''<div class="s end"><img class="logo" src="file://{ROOT}/cordiallevel/img/logo-cordial-level.png">
<h2>{e(title)}</h2><p class="lead">{e(lead)}</p>
<div class="facts">{fx}</div>
<div class="who"><div><b>Casemiro Ramos</b><span>WhatsApp 935 101 667</span></div><div><b>Francisco Medeiros</b><span>WhatsApp 912 706 395</span></div></div>
<div class="web">{e(link_label)}: {e(link)}<br>Todos os imóveis: century21.pt/consultores/cramos
<small>Cordial Level | CENTURY 21 Arquitectos · AMI 11414 · Ref. {e(n and '')}</small></div></div>''')


def build(name, slides):
    d = OUT / name
    d.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        for i, h in enumerate(slides, 1):
            f = d / f'{i:02d}.html'
            f.write_text(h)
            pg.goto(f'file://{f}')
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(d / f'{name}-{i:02d}.jpg'), type='jpeg', quality=92)
            f.unlink()
        b.close()
    print(name, len(slides))


FOZ = ROOT / 'cordiallevel/casaraofoz/img'
LEC = ROOT / 'cordiallevel/t3leca/img'


def foz():
    T = 8
    s = [
        photo_slide(FOZ / 'foz-f52.jpg', 1, T, 'Foz do Douro · Porto', 'Moradia T4 com vista de mar', 'Uma casa para renovar na Foz tradicional.', '875 000 €', big=True),
        photo_slide(FOZ / 'foz-f79.jpg', 2, T, 'Rua Senhora da Luz', 'No coração da Foz velha', 'A poucos passos da marginal, das praias e do Passeio Alegre.'),
        photo_slide(FOZ / 'foz-f2.jpg', 3, T, 'Interiores', 'Pés-direitos altos e tetos trabalhados', 'Salas com luz natural e o carácter de uma casa portuense.'),
        photo_slide(FOZ / 'foz-f90.jpg', 4, T, 'Sala de jantar', 'Espaço para receber', 'Divisões amplas, prontas para ganhar uma nova vida.'),
        photo_slide(FOZ / 'foz-f15.jpg', 5, T, 'Escadaria com claraboia', 'Luz em todos os pisos', ''),
        photo_slide(FOZ / 'foz-f40.jpg', 6, T, 'Quatro quartos', '165 m² úteis', '4 quartos e 2 casas de banho, distribuídos por vários pisos.', chips=('T4', '165 m²', '2 WC')),
        photo_slide(FOZ / 'foz-f43.jpg', 7, T, 'A vista', 'O mar ao fundo', 'Para renovar à sua medida — para viver ou investir.'),
        end_slide(8, T, 'Moradia T4 · Foz do Douro', 'Para renovar · dispensada de licença de utilização · vídeo e visita virtual 3D na apresentação.',
                  [('Preço', '875 000 €'), ('Área útil', '165 m²'), ('Quartos', '4'), ('Construção', '1990')], 'usinavideos.pt/cordiallevel/casaraofoz'),
    ]
    s[-1] = s[-1].replace('Ref. ', 'Ref. C0393-01661')
    build('carrossel-foz', s)


def leca():
    T = 8
    s = [
        photo_slide(LEC / 'leca-37.jpg', 1, T, 'Leça da Palmeira · Matosinhos', 'T3 junto ao mar', 'Com 2 lugares de garagem, a poucos passos da praia.', '550 000 €', big=True),
        photo_slide(LEC / 'leca-44.jpg', 2, T, 'A praia ali ao lado', 'Viver a poucos passos do mar', 'A marginal, as praias e a piscina das marés de Leça.'),
        photo_slide(LEC / 'leca-1.jpg', 3, T, 'Sala', '42 m² de sala, cheia de luz', 'Chão em madeira de afizélia com aquecimento radiante.'),
        photo_slide(LEC / 'leca-11.jpg', 4, T, 'Cozinha', 'Cozinha equipada', 'Com lavandaria independente.'),
        photo_slide(LEC / 'leca-21.jpg', 5, T, 'Suite', 'Três quartos, um em suite', 'Suite com 18,78 m² e casa de banho privativa.'),
        photo_slide(LEC / 'leca-18.jpg', 6, T, 'Casas de banho', 'Duas casas de banho', 'Acabamentos cuidados, pronto a habitar.'),
        photo_slide(LEC / 'leca-32.jpg', 7, T, 'Garagem', 'Dois lugares de garagem', 'Em Leça da Palmeira, um pormenor que faz toda a diferença.', chips=('2 lugares', 'Arrecadação')),
        end_slide(8, T, 'T3 junto ao mar · Leça da Palmeira', 'Construção de 2008 · certificado energético C · pronto a habitar.',
                  [('Preço', '550 000 €'), ('Área útil', '138 m²'), ('Quartos', '3 · 1 suite'), ('Garagem', '2 lugares')], 'usinavideos.pt/cordiallevel/t3leca'),
    ]
    s[-1] = s[-1].replace('Ref. ', 'Ref. C0393-01659')
    build('carrossel-leca', s)


ANT = pathlib.Path(os.environ.get('ANTERO_IMG', '/tmp/antero-img'))
BP = ROOT / 'cordiallevel/bosquepicua/img'


def antero():
    T = 8
    s = [
        photo_slide(ANT / 'antero-24.jpg', 1, T, 'Porto · Rua Antero de Quental', 'T2 remodelado no centro do Porto', 'Pronto a habitar, com 77,3 m².', '349 000 €', big=True),
        photo_slide(ANT / 'antero-31.jpg', 2, T, 'Localização', 'Centralidade e mobilidade', 'Comércio, serviços, restauração e transportes à porta.'),
        photo_slide(ANT / 'antero-26.jpg', 3, T, 'Sala', 'Sala e zona de refeições', 'Luminosa, com janelas para a cidade.'),
        photo_slide(ANT / 'antero-17.jpg', 4, T, 'Cozinha', 'Cozinha remodelada e equipada', 'Placa, exaustor, frigorífico e máquinas de lavar loiça e roupa.'),
        photo_slide(ANT / 'antero-3.jpg', 5, T, 'Quartos', 'Dois quartos', 'Com roupeiros e muita luz natural.', chips=('T2', '77,3 m²')),
        photo_slide(ANT / 'antero-11.jpg', 6, T, 'Casa de banho', 'Casa de banho renovada', 'Base de duche e acabamentos atuais.'),
        photo_slide(ANT / 'antero-27.jpg', 7, T, 'Para viver ou investir', 'Uma solução versátil', 'Para quem procura casa no Porto ou quer investir.'),
        end_slide(8, T, 'T2 remodelado · Rua Antero de Quental', 'Imóvel renovado · cozinha equipada · licença de utilização n.º 423/1983 · certificado energético D.',
                  [('Preço', '349 000 €'), ('Área útil', '77,3 m²'), ('Quartos', '2'), ('Estado', 'Renovado')], 'century21.pt/comprar/C0393-01689', 'Ficha completa'),
    ]
    s[-1] = s[-1].replace('Ref. ', 'Ref. C0393-01689')
    build('carrossel-antero', s)


def bosque():
    T = 8
    SIM = 'SIMULAÇÃO · NÃO VINCULATIVA'
    s = [
        photo_slide(BP / 'bp-fachada.jpg', 1, T, 'Bosque · Parque da Pícua · Maia', 'T2+1 com terraço e box', 'Em construção, com entrega prevista em 2028.', 'Preço sob consulta', big=True, ia=SIM, band=True),
        photo_slide(BP / 'bp-lagos.jpg', 2, T, 'O empreendimento', '1,5 hectares de jardins e lagos', 'Construção anti-sísmica e sustentável.', ia=SIM, band=True),
        photo_slide(BP / 'bp-jardim.jpg', 3, T, 'Águas Santas', 'Viver dentro de um parque', 'A oito minutos do centro do Porto.', ia=SIM, band=True),
        photo_slide(BP / 'bp-cobertura.jpg', 4, T, 'Exterior privativo', 'Terraço de 26,65 m²', 'Um deck para refeições ao ar livre.', ia=SIM, band=True),
        photo_slide(BP / 'bp-logradouro.jpg', 5, T, 'A casa', '92,30 m² bem distribuídos', 'Suite com closet, escritório e sala com cozinha em open space de 33,50 m².', ia=SIM, band=True),
        photo_slide(BP / 'bp-esquina.jpg', 6, T, 'Garagem', 'Box de 33 m² para dois carros', 'No piso -2, com espaço para arrumação.', chips=('Certificado A', 'Cozinha Bosch'), ia=SIM, band=True),
        photo_slide(BP / 'bp-parque.jpg', 7, T, 'Espaços comuns', 'Ginásio, coworking e lazer', 'Jardins, lagos e espaços para toda a família.', ia=SIM, band=True),
        end_slide(8, T, 'T2+1 · Bosque da Pícua', 'Em construção · entrega prevista em 2028 · imagens: simulações não vinculativas.',
                  [('Área útil', '92,30 m²'), ('Terraço', '26,65 m²'), ('Garagem', 'Box 33 m²'), ('Entrega', '2028')], 'usinavideos.pt/cordiallevel/bosquepicua'),
    ]
    s[-1] = s[-1].replace('Ref. ', 'Ref. C0393-01555')
    build('carrossel-bosque-picua', s)


if __name__ == '__main__':
    quais = sys.argv[2:] or ['foz', 'leca']
    for q in quais:
        globals()[q]()
