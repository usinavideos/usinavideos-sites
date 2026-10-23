#!/usr/bin/env python3
"""Proposta comercial da Usina Vídeos, aberta a todos os clientes: usinavideos.pt/proposta/

Página para enviar por link (não indexada: os preços não vão para o Google).
Uso: python3 _tools/proposta.py
"""
import html, os, sys, urllib.parse as up
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_usina import CSS, WA_SVG, STRIPE, COLORS
from mea_banner import MEA_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
WA = 'https://wa.me/351912988971?text=' + up.quote('Olá Freire, vi a proposta da Usina Vídeos e gostaria de avançar com um orçamento.')
CAL = 'https://calendly.com/usinavideos/videoreport'
VALIDADE = '31 de dezembro de 2026'

ENTREG = [('Fotografia profissional', 'Alta resolução, luz e composição editorial, pronta para portais e redes sociais.'),
          ('Vídeo do imóvel', 'Edição dinâmica com música licenciada, legendas e versões para cada plataforma.'),
          ('Drone', 'Planos aéreos em foto e vídeo que mostram a envolvente, a localização e os acessos.'),
          ('Visita virtual 3D com planta', 'Visita navegável a 360° com planta técnica integrada, para portais e reuniões.')]

PACOTES = [
    ('Pacote 01', 'Essencial', '40€', ['Fotografia profissional de alta resolução', 'Vídeo do imóvel editado com música <em>(oferta de lançamento)</em>'],
     'Para a maioria das angariações do dia a dia.', False),
    ('Pacote 02', 'Aéreo', '65€', ['Fotografia profissional de alta resolução', 'Vídeo do imóvel editado com música <em>(oferta de lançamento)</em>', 'Fotografia e vídeo aéreos com drone'],
     'Para moradias, terrenos e imóveis com exterior ou vistas relevantes.', False),
    ('Pacote 03 · Referência', 'Completo', '98€', ['Fotografia profissional de alta resolução', 'Vídeo do imóvel editado com música', 'Fotografia e vídeo aéreos com drone',
     'Visita virtual 3D navegável (alojamento 6 meses)', 'Planta técnica integrada na visita'], 'Para imóveis premium e angariações de maior valor.', True),
]

PREMIUM = [('Apresentação digital do imóvel', '100€', '50€ com reportagem Usina', 'Página própria do imóvel com fotos, vídeo, mapa e contactos, em várias línguas. <a href="/t4coral/">Exemplo</a>'),
           ('Vídeo com o consultor em cena', '110€', 'por vídeo', 'Rosto, autoridade e presença nas redes, em formato vertical e horizontal.'),
           ('Vídeo de lançamento de empreendimento', 'desde 250€', '', 'Guião, narrativa e produção cinematográfica para empreendimentos e imóveis de luxo.'),
           ('Podcast imobiliário', '150€', 'por episódio', 'Gravação e edição completas. <a href="https://www.youtube.com/watch?v=ed1kwc3x27I" target="_blank" rel="noopener">Exemplo</a>'),
           ('Transmissão em direto', '300€', '', 'Open house ou lançamento em direto nas redes sociais e no YouTube.'),
           ('Gestão de campanhas e contactos', '100€', 'por imóvel', 'Campanhas Facebook e Instagram segmentadas por zona e comprador. Acresce o investimento em anúncios.')]

ESPECIAIS = [('Vídeos de luxo', 'Produções cinematográficas com narrativa e banda sonora, para propriedades de alto valor.'),
             ('Sites e páginas de imóveis', 'Sites para agências e consultores e páginas únicas por imóvel ou empreendimento. <a href="/cordiallevel/">Exemplo</a>'),
             ('Visitas interativas', 'Visitas virtuais com pontos de informação, medições e multimédia.'),
             ('Conteúdo de marca', 'Vídeos institucionais para promotores, construtoras e agências.')]

STEPS = [('Pedido', 'Por WhatsApp, e-mail ou marcação online: morada, tipologia e serviço pretendido.'),
         ('Produção', 'Deslocamo-nos ao imóvel e fazemos a captação. Uma sessão dura, em regra, até 1h30.'),
         ('Pós-produção', 'Seleção, tratamento de imagem, edição de vídeo e montagem.'),
         ('Entrega', 'Fotografias em 48 horas. Vídeo e visita 3D em 72 horas.')]

EXTRA_CSS = """
.pk{display:grid;gap:16px;margin-top:36px}@media(min-width:900px){.pk{grid-template-columns:repeat(3,1fr)}}
.pk article{background:#fff;border:1px solid #E3DED6;border-radius:18px;padding:26px;border-top:5px solid var(--c);display:flex;flex-direction:column}
.pk article.ref{background:var(--ink);color:#D6D1CD;border-color:var(--ink);border-top-color:var(--y)}
.pk article.ref h3,.pk article.ref .pr{color:#fff}
.pk .lb{font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--c)}
.pk h3{font-size:28px;margin-top:6px}.pk .pr{font-size:48px;font-weight:900;color:var(--ink);line-height:1;margin-top:14px}
.pk .pr small{font-size:14px;font-weight:700;color:var(--muted);margin-left:6px}
.pk ul{list-style:none;margin:18px 0 0;padding:0;display:grid;gap:8px;font-size:15px}
.pk li{padding-left:22px;position:relative}.pk li::before{content:"✓";position:absolute;left:0;font-weight:900;color:var(--c)}
.pk li em{font-style:normal;color:var(--r);font-weight:700}
.pk p{margin:16px 0 0;font-size:14px}
.cmp{width:100%;border-collapse:collapse;margin-top:28px;background:#fff;border-radius:14px;overflow:hidden;font-size:15px}
.cmp th,.cmp td{padding:14px 16px;border-bottom:1px solid #E3DED6;text-align:left}.cmp th{background:var(--ink);color:#fff;font-size:13px;letter-spacing:.08em;text-transform:uppercase}
.cmp td:last-child{font-weight:800;color:var(--ink)}.cmp tr.t td{font-weight:900;background:var(--paper2)}
.prem{display:grid;gap:14px;margin-top:36px}@media(min-width:760px){.prem{grid-template-columns:1fr 1fr}}@media(min-width:1100px){.prem{grid-template-columns:repeat(3,1fr)}}
.prem article{background:var(--ink2);border:1px solid var(--line);border-radius:16px;padding:22px}
.prem b.pr{display:block;font-size:30px;font-weight:900;color:var(--y);line-height:1}.prem b.pr small{font-size:13px;color:#C9C3BF;font-weight:700;margin-left:6px}
.prem h3{font-size:19px;margin-top:10px}.prem p{margin:8px 0 0;font-size:15px}.prem a,.card a{color:var(--y)}
.note{margin-top:22px;font-size:14px;color:var(--muted)}
.cond{display:grid;gap:14px;margin-top:32px}@media(min-width:800px){.cond{grid-template-columns:repeat(3,1fr)}}
.cond div{background:#fff;border:1px solid #E3DED6;border-radius:14px;padding:20px}.cond b{display:block;color:var(--ink);font-size:16px;margin-bottom:6px}
"""


EDICAO = [('Reel ou short (até 60 s)', '50€', 'vertical, com legendas e música'),
          ('Vídeo até 3 minutos', '120€', 'imóvel, entrevista ou resumo de evento'),
          ('Vídeo até 10 minutos', '220€', 'reportagem, entrevista longa ou aftermovie'),
          ('Projetos mais longos', '30€/hora', 'orçamento fechado antes de começar')]

CLIENTES = {
    'ricardo-ribeiro': dict(nome='Ricardo Ribeiro', cidade='Lisboa',
        intro='Proposta preparada para o Ricardo Ribeiro, jornalista em Lisboa, para eventos, imóveis e edição de material já captado. Do jornalista para o jornalista: a mesma linguagem de reportagem, com prazos de redação.'),
}


def edicao_html():
    rows = ''.join(f'<article><b class="pr">{p}<small>+ IVA</small></b><h3>{e(n)}</h3><p>{e(d)}</p></article>' for n, p, d in EDICAO)
    return f'''<section id="edicao" class="dark">
  <div class="wrap"><span class="eb">Edição de material já captado</span><h2>Envie o material, nós editamos.</h2>
    <p class="lead">Recebemos os ficheiros por WeTransfer, Google Drive ou disco e devolvemos o vídeo pronto a publicar, em formato horizontal e vertical.</p>
    <div class="prem">{rows}</div>
    <div class="cond" style="margin-top:22px">
      <div style="background:var(--ink2);border-color:var(--line);color:#D6D1CD"><b style="color:#fff">Incluído</b>Seleção dos melhores planos, correção de cor, som, música licenciada, legendas e uma ronda de alterações.</div>
      <div style="background:var(--ink2);border-color:var(--line);color:#D6D1CD"><b style="color:#fff">Prazos</b>72 horas para vídeos até 3 minutos. Urgência em 24 horas: +30%.</div>
      <div style="background:var(--ink2);border-color:var(--line);color:#D6D1CD"><b style="color:#fff">Rondas extra</b>Cada ronda de alterações adicional: 20€ + IVA. Tradução e legendas noutras línguas sob orçamento.</div>
    </div>
    <p class="note" style="color:#C9C3BF">Cobertura de eventos e reportagem de imóveis em Lisboa: captação orçamentada por evento ou por dia, com a deslocação indicada à parte. Pode juntar a edição desta tabela.</p></div>
</section>
'''


def build(cliente=None):
    ent = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b) in enumerate(ENTREG))
    pk = ''.join(f'<article class="{"ref" if ref else ""}" style="--c:{COLORS[i % 3]}"><span class="lb">{e(lb)}</span><h3>{e(n)}</h3><div class="pr">{p}<small>+ IVA · por imóvel</small></div><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul><p>{e(d)}</p></article>'
                 for i, (lb, n, p, items, d, ref) in enumerate(PACOTES))
    prem = ''.join(f'<article><b class="pr">{p}<small>{e(s)}</small></b><h3>{e(n)}</h3><p>{d}</p></article>' for n, p, s, d in PREMIUM)
    esp = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><h3>{e(a)}</h3><p>{b}</p></article>' for i, (a, b) in enumerate(ESPECIAIS))
    steps = ''.join(f'<div class="step"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in STEPS)
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e('Proposta para ' + cliente['nome'] + ' · Usina Vídeos') if cliente else 'Proposta de serviços · Usina Vídeos'}</title>
<meta name="description" content="Pacotes de fotografia, vídeo, drone, visita 3D e apresentações digitais para o mercado imobiliário. Proposta Usina Vídeos.">
<meta name="robots" content="noindex, follow">
<meta property="og:title" content="Proposta de serviços · Usina Vídeos"><meta property="og:description" content="Fotografia, vídeo, drone, visita 3D e apresentações digitais para imóveis. Pacotes a partir de 40€ + IVA.">
<meta property="og:image" content="https://usinavideos.pt/img/foz-drone.jpg"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#141213">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}{MEA_CSS}{EXTRA_CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Menu"><div class="wrap">
  <a class="logo" href="/"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <div class="links">{'<a href="#edicao">Edição</a>' if cliente else ''}<a href="#pacotes">Pacotes</a><a href="#premium">Serviços premium</a><a href="#condicoes">Condições</a><a href="/#trabalhos">Trabalhos</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Avançar</a>
</div></nav>

<header class="hero dark" style="min-height:min(70vh,620px)">
  <img src="/img/foz-drone.jpg" alt="" fetchpriority="high">
  <div class="wrap">
    <span class="eb">{e('Proposta para ' + cliente['nome'] + ' · ' + cliente['cidade']) if cliente else 'Proposta de serviços · Usina Vídeos'}</span>
    <h1>{'Vídeo para eventos, imóveis e reportagem.' if cliente else 'Produção audiovisual para o mercado imobiliário.'}</h1>
    <p>{e(cliente['intro']) if cliente else 'Para agências, consultores, promotores e proprietários. Um parceiro, um briefing, um contacto, do Norte a todo o país.'}</p>
    <div class="row"><a class="btn y" href="#pacotes">Ver pacotes</a><a class="btn o" href="{CAL}" target="_blank" rel="noopener">Marcar sessão</a></div>
    {STRIPE}
  </div>
</header>

<section>
  <div class="wrap two">
    <div><span class="eb">Porquê um parceiro</span><h2>Avulso ou parceria estruturada?</h2>
      <p style="margin-top:20px">Contratar cada serviço a um fornecedor diferente gera custos imprevisíveis e qualidade variável de imóvel para imóvel. Com a Usina Vídeos, fotografia, vídeo, drone, visita 3D e apresentação digital saem da mesma equipa, com o mesmo padrão e um único contacto.</p>
      <p>A equipa é dirigida por <b>Freire Neto</b>, jornalista desde 1997 e fundador do Motores e Ação, e por <b>Sandra Freire</b>, na edição de vídeo.</p></div>
    <div class="stats"><div><b>25+</b><span>anos de reportagem</span></div><div><b>48h</b><span>entrega de fotografias</span></div><div><b>72h</b><span>vídeo e visita 3D</span></div><div><b>PT · EN · ES · FR</b><span>apresentações multilingues</span></div></div>
  </div>
</section>

<section style="background:var(--paper2)">
  <div class="wrap"><span class="eb">O que recebe</span><h2>Quatro entregáveis, um briefing.</h2>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">{ent}</div></div>
</section>

{edicao_html() if cliente else ''}
<section id="pacotes">
  <div class="wrap"><span class="eb">Pacotes por imóvel</span><h2>Preços claros, por imóvel.</h2>
    <p class="lead">Valores sem IVA, que acresce à taxa legal em vigor.</p>
    <div class="pk">{pk}</div>
    <div style="overflow-x:auto;margin-top:28px;border-radius:14px"><table class="cmp" style="margin-top:0;min-width:560px"><thead><tr><th>Entregável</th><th>Contratado em separado (média)</th><th>Usina Vídeos</th></tr></thead><tbody>
      <tr><td>Fotografia profissional</td><td>80–120€</td><td>Incluído</td></tr>
      <tr><td>Vídeo do imóvel</td><td>90–150€</td><td>Incluído</td></tr>
      <tr><td>Drone</td><td>60–80€</td><td>Incluído no Aéreo e no Completo</td></tr>
      <tr><td>Visita virtual 3D com planta</td><td>80–120€</td><td>Incluído no Completo</td></tr>
      <tr class="t"><td>Total</td><td>310–470€</td><td>98€ + IVA (Completo)</td></tr></tbody></table></div>
    <p class="note">A oferta de lançamento do vídeo editado nos pacotes Essencial e Aéreo é válida até {VALIDADE}. Drone sujeito às condições meteorológicas, à disponibilidade e às autorizações de voo.</p>
  </div>
</section>

<section id="premium" class="dark">
  <div class="wrap"><span class="eb">Serviços premium</span><h2>Autoridade digital e geração de contactos.</h2>
    <p class="lead">Além dos pacotes por imóvel, produções que valorizam o consultor, a agência e o empreendimento.</p>
    <div class="prem">{prem}</div></div>
</section>

<section style="background:var(--paper2)">
  <div class="wrap"><span class="eb">Projetos especiais</span><h2>À medida do projeto.</h2>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">{esp}</div>
    <div class="orc" style="margin-top:28px"><div><h3>Bolsa de produções</h3><p>Sem avença nem compromisso de volume: um crédito pré-pago, válido 12 meses, usado à medida das angariações. Sem renovação automática.</p></div>
      <div><h4>Ideal para</h4><ul><li>Lojas e equipas com volume variável</li><li>Períodos de transição</li><li>Um primeiro teste à parceria</li></ul></div></div>
  </div>
</section>

<section id="condicoes">
  <div class="wrap"><span class="eb">Processo e condições</span><h2>Do pedido à entrega.</h2>
    <div class="steps">{steps}</div>
    <div class="cond">
      <div><b>Zona e deslocações</b>Preços para produções no Norte de Portugal. Fora do Norte, como Lisboa, a deslocação é orçamentada à parte e indicada na proposta.</div>
      <div><b>Faturação</b>Uma fatura por serviço ou pacote, ou condições acordadas por projeto.</div>
      <div><b>Validade</b>Valores válidos até {VALIDADE}. Simulações feitas com IA são sempre identificadas como tal.</div>
    </div>
  </div>
</section>

<section class="dark">
  <div class="wrap two">
    <div><span class="eb">Falemos do seu próximo imóvel</span><h2>Freire Neto</h2><p style="margin-top:14px">Jornalista e produtor de conteúdo · Usina Vídeos</p>
      <div class="row" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:22px"><a class="btn y" href="{WA}" target="_blank" rel="noopener">{WA_SVG}WhatsApp +351 912 988 971</a><a class="btn o" style="color:#fff" href="{CAL}" target="_blank" rel="noopener">Marcar sessão online</a></div>
      <p style="margin-top:18px">E-mail: <a href="mailto:freireneto@me.com" style="color:var(--y)">freireneto@me.com</a> · <a href="/" style="color:var(--y)">usinavideos.pt</a></p></div>
    <div class="stats"><div><b>Cordial Level</b><span>site, vídeos e podcast</span></div><div><b>Coral</b><span>apresentação em 4 línguas</span></div><div><b>C21 Core</b><span>fotografia e vídeo</span></div><div><b>CDJRegio</b><span>reportagem desportiva</span></div></div>
  </div>
</section>

<footer><div class="wrap">
  <img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298">
  <span>A sua exigência, a nossa assinatura. · © Usina Vídeos</span>
</div></footer>
</body>
</html>
'''


if __name__ == '__main__':
    d = os.path.join(ROOT, 'proposta')
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(build())
    for slug, c in CLIENTES.items():
        os.makedirs(os.path.join(d, slug), exist_ok=True)
        open(os.path.join(d, slug, 'index.html'), 'w').write(build(c))
    print('ok proposta +', ', '.join(CLIENTES))
