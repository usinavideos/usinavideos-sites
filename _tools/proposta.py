#!/usr/bin/env python3
"""Proposta comercial da Usina Vídeos, aberta a todos os clientes: usinavideos.pt/proposta/

Página para enviar por link (não indexada: os preços não vão para o Google).
Uso: python3 _tools/proposta.py
"""
import html, os, sys, urllib.parse as up
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_usina import CSS, WA_SVG, STRIPE, COLORS, T, IG_SVG, IN_SVG, YT_SVG, MEA_ICON
from mea_banner import mea_banner
from mea_banner import MEA_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
WA = 'https://wa.me/351912988971?text=' + up.quote('Olá Freire, vi a proposta da Usina Vídeos e gostaria de avançar com um orçamento.')
CAL = 'https://calendly.com/usinavideos/videoreport'
VALIDADE = '31 de dezembro de 2026'

ENTREG = [('Fotografia profissional', 'Alta resolução, luz e composição editorial, pronta para portais e redes sociais.', '/cordiallevel/t3leca/img/leca-1-t.jpg'),
          ('Vídeo do imóvel', 'Edição dinâmica com música licenciada, legendas e versões para cada plataforma.', '/img/coral-cozinha.jpg'),
          ('Drone', 'Planos aéreos em foto e vídeo que mostram a envolvente, a localização e os acessos.', '/cordiallevel/t3leca/img/leca-37-t.jpg'),
          ('Visita virtual 3D com planta', 'Visita navegável a 360° com planta técnica integrada, para portais e reuniões.', '/cordiallevel/casaraofoz/img/foz-f2-t.jpg')]
PK_IMG = ['/cordiallevel/anteroquental/img/aq-20-t.jpg', '/cordiallevel/moncao/img/t1-d4-t.jpg', '/img/coral-fachada.jpg']
VIDEOS = [('yo7RN7u6JJY', 'Terrenos em Monção', 'Drone e vídeo-reportagem · 1 min 45 s'),
          ('xEDuuPNMacM', 'T3 em Leça da Palmeira', 'Vídeo do imóvel com drone · 1 min 42 s'),
          ('vU0bXm_uhGk', 'Short vertical de Leça', 'Formato para Reels, Shorts e TikTok'),
          ('7JOcy10W8oY', 'T1 em Matosinhos', 'Vídeo-reportagem · 10 min'),
          ('ed1kwc3x27I', 'Podcast Panorama Imobiliário PT', 'Gravação e edição · 26 min'),
          ('Re8UZQRVTOY', 'Prédio na Baixa do Porto', 'Vídeo do imóvel · 1 min 12 s')]

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
@media(min-width:900px){.pk.pk4{grid-template-columns:repeat(2,1fr)}}@media(min-width:1200px){.pk.pk4{grid-template-columns:repeat(4,1fr)}.pk4 h3{font-size:22px}.pk4 .pr{font-size:40px}}
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
.tab{margin-top:8px;font-size:14px;color:var(--muted)}.tab b{color:#23863D}.cmp td.dc{color:#23863D}
.zg{display:grid;gap:12px;margin-top:30px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}.zn{background:#fff;border:1px solid #E3DED6;border-left:5px solid var(--c);border-radius:14px;padding:16px 18px;display:grid;gap:4px}.zn span{font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--c)}.zn b{font-size:17px;color:var(--ink)}.zn em{font-style:normal;color:var(--muted);font-size:15px}
.cmp td:last-child{font-weight:800;color:var(--ink)}.cmp tr.t td{font-weight:900;background:var(--paper2)}
.prem{display:grid;gap:14px;margin-top:36px}@media(min-width:760px){.prem{grid-template-columns:1fr 1fr}}@media(min-width:1100px){.prem{grid-template-columns:repeat(3,1fr)}}
.prem article{background:var(--ink2);border:1px solid var(--line);border-radius:16px;padding:22px}
.prem b.pr{display:block;font-size:30px;font-weight:900;color:var(--y);line-height:1}.prem b.pr small{font-size:13px;color:#C9C3BF;font-weight:700;margin-left:6px}
.prem h3{font-size:19px;margin-top:10px}.prem p{margin:8px 0 0;font-size:15px}.prem a,.card a{color:var(--y)}
.card.ic{padding:0;overflow:hidden}.card.ic img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block}.card.ic .n,.card.ic h3,.card.ic p{margin-left:22px;margin-right:22px}.card.ic .n{display:block;margin-top:16px}.card.ic p{margin-bottom:22px}
.pk .pkimg{width:calc(100% + 52px);margin:-26px -26px 18px;aspect-ratio:16/9;object-fit:cover;display:block;border-radius:13px 13px 0 0}
.pvs{display:grid;gap:18px;margin-top:32px}@media(min-width:700px){.pvs{grid-template-columns:1fr 1fr}}@media(min-width:1050px){.pvs{grid-template-columns:repeat(3,1fr)}}
.pv{margin:0}.yt2{position:relative;display:block;width:100%;aspect-ratio:16/9;padding:0;border:0;border-radius:14px;overflow:hidden;background:#000;cursor:pointer}
.yt2 img{width:100%;height:100%;object-fit:cover;opacity:.9}.yt2:hover img{opacity:1}.yt2 iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.yt2 .pl{position:absolute;left:50%;top:50%;width:66px;height:66px;margin:-33px 0 0 -33px;border-radius:50%;background:var(--y)}
.yt2 .pl::after{content:"";position:absolute;left:27px;top:21px;border-style:solid;border-width:12px 0 12px 19px;border-color:transparent transparent transparent var(--ink)}
.pv figcaption{margin-top:10px}.pv b{display:block;color:#fff;font-size:18px}.pv span{font-size:14px;color:#C9C3BF}
#redes .side{grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}@media(min-width:1100px){#redes .side{grid-template-columns:repeat(4,1fr)}}.mini.fb em{color:#5AA3E8}
.prem4{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))!important}@media(min-width:1100px){.prem4{grid-template-columns:repeat(4,1fr)!important}}
.note{margin-top:22px;font-size:14px;color:var(--muted)}
.cond{display:grid;gap:14px;margin-top:32px}@media(min-width:800px){.cond{grid-template-columns:repeat(3,1fr)}}
.cond div{background:#fff;border:1px solid #E3DED6;border-radius:14px;padding:20px}.cond b{display:block;color:var(--ink);font-size:16px;margin-bottom:6px}
"""


EDICAO = [('Reel ou short (até 60 s)', '35€', 'vertical, com legendas e música'),
          ('Vídeo até 3 minutos', '95€', 'imóvel, entrevista ou resumo de evento'),
          ('Vídeo até 10 minutos', '150€', 'reportagem, entrevista longa ou aftermovie'),
          ('Projetos mais longos', '20€/hora', 'orçamento fechado antes de começar')]

CLIENTES = {
    'cristina-russo': dict(nome='Cristina Russo', cidade='Grande Porto', edicao=False,
        h1='Os seus imóveis, apresentados como merecem.',
        intro='Proposta preparada para a Cristina Russo, consultora imobiliária. Depois das reportagens em Leça, em Campo (Valongo) e no Cerco, propomos uma parceria com preços fixos por imóvel, prazos curtos e um único contacto para tudo.',
        juntos=[('img/cr-leca-t.jpg', 'T3 em Leça da Palmeira', 'Fotografia e vídeo'),
                ('img/cr-valongo-t.jpg', 'T2 em Campo, Valongo', 'Fotografia e vídeo'),
                ('img/cr-cerco-t.jpg', 'T3 no Cerco, Porto', 'Fotografia e vídeo · outubro de 2026')]),
    'ricardo-ribeiro': dict(nome='Ricardo Ribeiro', cidade='Lisboa', edicao=True, h1='Vídeo para eventos, imóveis e reportagem.',
        intro='Proposta preparada para o Ricardo Ribeiro, jornalista em Lisboa, para eventos, imóveis e edição de material já captado. Do jornalista para o jornalista: a mesma linguagem de reportagem, com prazos de redação.'),
    'tiago-branquinha': dict(nome='Tiago Branquinha', cidade='Porto', edicao=False,
        h1='O seu T2 na Prelada, contado por quem conhece a zona.',
        intro='Proposta preparada para o Tiago Branquinha, consultor imobiliário. Partimos da vídeo-reportagem que já fizemos ao T2 na Prelada e juntamos um vídeo consigo a apresentar a região, uma página própria do imóvel e uma campanha nas redes para gerar contactos. Ao fim de um mês avaliamos os resultados juntos.',
        hero='img/tb-predio.jpg',
        juntos_t=('A reportagem que já fizemos', 'O T2 na Prelada, pela Usina.', 'Fotografia e vídeo já entregues. São estas imagens que fecham o novo vídeo e dão vida à página do imóvel.'),
        juntos=[('img/tb-sala-t.jpg', 'Sala', 'Ampla, com luz natural'),
                ('img/tb-vista-t.jpg', 'Vista', 'Desafogada sobre a zona'),
                ('img/tb-cozinha-t.jpg', 'Cozinha', 'Equipada e funcional')],
        plano=[('Fase 1 · Semana 1', 'Vídeo «Viver na Prelada»', 100, 175,
                ['Gravação consigo em cena a apresentar a zona: metro, comércio, escolas, parques', 'Imagens novas da região e planos aéreos com drone', 'Final com as imagens do T2 que já temos', 'Versão YouTube (horizontal, até 3 min) e 2 Reels verticais com legendas']),
               ('Fase 2 · Semana 2', 'Página de apresentação do imóvel', 50, 100,
                ['Página própria do T2 com fotos, vídeos, planta, mapa e distâncias', 'Botões de WhatsApp e chamada direta para si', 'Formulário de contacto para captar leads', 'Pronta a partilhar nos anúncios e nas redes']),
               ('Fase 3 · Semanas 2 a 5', 'Gestão da campanha nas redes', 50, 100,
                ['Anúncios Facebook e Instagram segmentados por zona e perfil de comprador', 'Vídeo e Reels a levar tráfego para a página do imóvel', 'Ajustes semanais de público e criativos', 'Investimento em anúncios: 120€ no mês (30€ por semana)']),
               ('Fase 4 · Semana 6', 'Avaliação de resultados', 0, 0,
                ['Relatório de visualizações, cliques e contactos recebidos', 'Reunião de 30 minutos para decidir os próximos passos', 'Ajuste ou reforço da estratégia com base nos números'])],
        meta=120,
        zona_t='Rua Dr. Cruz Malpique, Prelada · Ramalde, Porto',
        zona=[('Metro', 'Estação Ramalde', '650 m · 10 min a pé'), ('Metro', 'Estação Viso', '1,1 km · 15 min a pé'),
              ('Autocarro', 'Paragens STCP Parque da Prelada', '550 m · 7 min a pé'), ('Supermercado', 'Pingo Doce Ramalde', '400 m · 6 min a pé'),
              ('Supermercado', 'Continente Bom Dia Prelada', '950 m · 13 min a pé'), ('Escola', 'EB 2/3 Maria Lamas', '450 m · 6 min a pé'),
              ('Saúde', 'Hospital da Prelada', '550 m · 8 min a pé'), ('Saúde', 'Hospital de São João', '2,9 km · 10 min de carro'),
              ('Lazer', 'Casa e jardins da Prelada, de Nasoni', '450 m · 6 min a pé'), ('Parque', 'Parque da Cidade e praia', '3,8 km · 10 min de carro'),
              ('Compras', 'NorteShopping', '1,9 km · 5 min de carro'), ('Cultura', 'Casa da Música', '1,5 km · 2 estações de metro')]),
}


def plano_html(c):
    def pr(v, t):
        if not v:
            return '<div class="pr" style="font-size:34px">Incluída</div>'
        return f'<div class="pr">{v}€<small>+ IVA</small></div><div class="tab">Tabela <s>{t}€</s> · <b>poupa {t - v}€</b></div>'
    cards = ''.join(f'<article style="--c:{COLORS[i % 3]}"><span class="lb">{e(f)}</span><h3>{e(n)}</h3>{pr(v, t)}<ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></article>' for i, (f, n, v, t, items) in enumerate(c['plano']))
    rows = ''.join(f'<tr><td>{e(n)}</td><td>{f"{t}€" if t else "—"}</td><td>{f"{v}€" if v else "Incluída"}</td><td class="dc">{f"−{t - v}€ ({round((t - v) * 100 / t)}%)" if t else "—"}</td></tr>' for f, n, v, t, items in c['plano'])
    tt = sum(x[3] for x in c['plano']); tv = sum(x[2] for x in c['plano']); m = c['meta']
    return f'''<section id="plano">
  <div class="wrap"><span class="eb">O plano para o seu imóvel</span><h2>Vídeo, página e campanha: um mês para gerar contactos.</h2>
    <p class="lead">Quatro fases, um só contacto. Cada fase alimenta a seguinte: o vídeo leva às redes, as redes levam à página, a página leva até si.</p>
    <div class="pk pk4">{cards}</div>
    <div style="overflow-x:auto;margin-top:28px;border-radius:14px"><table class="cmp" style="margin-top:0;min-width:560px"><thead><tr><th>Serviço</th><th>Preço de tabela</th><th>Para si</th><th>Desconto</th></tr></thead><tbody>{rows}
      <tr class="t"><td>Produção e gestão</td><td>{tt}€ + IVA</td><td>{tv}€ + IVA</td><td class="dc">−{tt - tv}€ ({round((tt - tv) * 100 / tt)}%)</td></tr>
      <tr><td>Investimento em anúncios na Meta (4 semanas × 30€)</td><td>{m}€</td><td>{m}€</td><td>sem margem</td></tr>
      <tr class="t"><td>Total do primeiro mês <small style="font-weight:600">(IVA à parte na produção)</small></td><td>{tt + m}€</td><td>{tv + m}€</td><td class="dc">−{tt - tv}€</td></tr></tbody></table></div>
    <div class="orc" style="margin-top:28px"><div><h3>{tv}€ + IVA + {m}€ em anúncios</h3><p>Produção e gestão por {tv}€ + IVA, em vez de {tt}€ de tabela: um desconto de {tt - tv}€ por já ser nosso cliente. Os {m}€ de anúncios vão integralmente para a Meta, sem margem da Usina, pagos por si diretamente na conta de anúncios.</p></div>
      <div><h4>Como avançamos</h4><ul><li>Marcamos a gravação consigo na Prelada</li><li>Vídeo e página prontos na semana seguinte</li><li>Avaliação conjunta ao fim de 1 mês de campanha</li></ul></div></div>
    <p class="note">Drone sujeito às condições meteorológicas e às autorizações de voo. Os resultados da campanha dependem do mercado e do investimento; o relatório mostra os números reais, sem promessas de vendas.</p></div>
</section>
'''


def zona_html(c):
    cards = ''.join(f'<div class="zn" style="--c:{COLORS[i % 3]}"><span>{e(k)}</span><b>{e(n)}</b><em>{e(d)}</em></div>' for i, (k, n, d) in enumerate(c['zona']))
    return f'''<section id="zona" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">A zona · {e(c['zona_t'])}</span><h2>Tudo perto, num bairro calmo.</h2>
    <p class="lead">É isto que vai mostrar no vídeo: metro a 10 minutos a pé, supermercados, escola e hospital no bairro, e os jardins históricos da Prelada ao virar da esquina.</p>
    <div class="zg">{cards}</div>
    <p class="note">Distâncias aproximadas a partir da Rua Dr. Cruz Malpique, em linha reta e tempos estimados. Confirmamos no terreno durante a gravação.</p></div>
</section>
'''


def edicao_html():
    rows = ''.join(f'<article><b class="pr">{p}<small>+ IVA</small></b><h3>{e(n)}</h3><p>{e(d)}</p></article>' for n, p, d in EDICAO)
    return f'''<section id="edicao" class="dark">
  <div class="wrap"><span class="eb">Edição de material já captado</span><h2>Envie o material, nós editamos.</h2>
    <p class="lead">Recebemos os ficheiros por WeTransfer, Google Drive ou disco e devolvemos o vídeo pronto a publicar, em formato horizontal e vertical.</p>
    <div class="prem prem4">{rows}</div>
    <div class="cond" style="margin-top:22px">
      <div style="background:var(--ink2);border-color:var(--line);color:#D6D1CD"><b style="color:#fff">Incluído</b>Seleção dos melhores planos, correção de cor, som, música licenciada, legendas e uma ronda de alterações.</div>
      <div style="background:var(--ink2);border-color:var(--line);color:#D6D1CD"><b style="color:#fff">Prazos</b>72 horas para vídeos até 3 minutos. Urgência em 24 horas: +30%.</div>
      <div style="background:var(--ink2);border-color:var(--line);color:#D6D1CD"><b style="color:#fff">Rondas extra</b>Cada ronda de alterações adicional: 20€ + IVA. Tradução e legendas noutras línguas sob orçamento.</div>
    </div>
    <p class="note" style="color:#C9C3BF">Cobertura de eventos e reportagem de imóveis em Lisboa: captação orçamentada por evento ou por dia, com a deslocação indicada à parte. Pode juntar a edição desta tabela.</p></div>
</section>
'''


def juntos_html(c):
    cards = ''.join(f'<article class="card ic" style="--c:{COLORS[i % 3]}"><img src="{im}" alt="{e(t)}" loading="lazy"><span class="n">{i + 1:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></article>' for i, (im, t, d) in enumerate(c['juntos']))
    jt = c.get('juntos_t', ('Já trabalhámos juntos', 'Os seus imóveis, pela Usina.', 'Algumas das reportagens que fizemos para si. É este o padrão que propomos manter em todas as angariações.'))
    return f'''<section id="juntos" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">{e(jt[0])}</span><h2>{e(jt[1])}</h2>
    <p class="lead">{e(jt[2])}</p>
    <div class="grid3">{cards}</div></div>
</section>
'''


def build(cliente=None):
    ent = ''.join(f'<article class="card ic" style="--c:{COLORS[i % 3]}"><img src="{im}" alt="{e(a)}" loading="lazy"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b, im) in enumerate(ENTREG))
    vids = ''.join(f'<figure class="pv"><button class="yt2" data-id="{v}" aria-label="Ver vídeo: {e(t)}"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="" loading="lazy"><span class="pl" aria-hidden="true"></span></button><figcaption><b>{e(t)}</b><span>{e(m)}</span></figcaption></figure>' for v, t, m in VIDEOS)
    pk = ''.join(f'<article class="{"ref" if ref else ""}" style="--c:{COLORS[i % 3]}"><img class="pkimg" src="{PK_IMG[i]}" alt="" loading="lazy"><span class="lb">{e(lb)}</span><h3>{e(n)}</h3><div class="pr">{p}<small>+ IVA · por imóvel</small></div><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul><p>{e(d)}</p></article>'
                 for i, (lb, n, p, items, d, ref) in enumerate(PACOTES))
    prem = ''.join(f'<article><b class="pr">{p}<small>{e(s)}</small></b><h3>{e(n)}</h3><p>{d}</p></article>' for n, p, s, d in PREMIUM)
    esp = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><h3>{e(a)}</h3><p>{b}</p></article>' for i, (a, b) in enumerate(ESPECIAIS))
    socials = ''.join(f'<a class="mini {k}" href="{u}" target="_blank" rel="noopener">{MEA_ICON if "motoreseacao" in u else (IG_SVG if k == "ig" else IN_SVG)}<div><b>{e(a)}</b><span>{e(b)}</span></div><em>{e(c)} →</em></a>' for u, k, a, b, c in T['pt']['socials'])
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
  <div class="links">{'<a href="#edicao">Edição</a>' if cliente and cliente.get('edicao') else ''}{'<a href="#juntos">O nosso trabalho</a>' if cliente and cliente.get('juntos') else ''}{'<a href="#zona">A zona</a>' if cliente and cliente.get('zona') else ''}{'<a href="#plano">O plano</a>' if cliente and cliente.get('plano') else ''}<a href="#pacotes">Pacotes</a><a href="#videos">Vídeos</a><a href="#premium">Serviços premium</a><a href="#condicoes">Condições</a><a href="/#trabalhos">Trabalhos</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Avançar</a>
</div></nav>

<header class="hero dark" style="min-height:min(70vh,620px)">
  <img src="{(cliente or {}).get('hero', '/img/foz-drone.jpg')}" alt="" fetchpriority="high">
  <div class="wrap">
    <span class="eb">{e('Proposta para ' + cliente['nome'] + ' · ' + cliente['cidade']) if cliente else 'Proposta de serviços · Usina Vídeos'}</span>
    <h1>{e(cliente['h1']) if cliente else 'Produção audiovisual para o mercado imobiliário.'}</h1>
    <p>{e(cliente['intro']) if cliente else 'Para agências, consultores, promotores e proprietários. Um parceiro, um briefing, um contacto, do Norte a todo o país.'}</p>
    <div class="row"><a class="btn y" href="{'#plano' if cliente and cliente.get('plano') else '#pacotes'}">{'Ver o plano' if cliente and cliente.get('plano') else 'Ver pacotes'}</a><a class="btn o" href="{CAL}" target="_blank" rel="noopener">Marcar sessão</a></div>
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

{edicao_html() if cliente and cliente.get('edicao') else ''}{juntos_html(cliente) if cliente and cliente.get('juntos') else ''}{zona_html(cliente) if cliente and cliente.get('zona') else ''}{plano_html(cliente) if cliente and cliente.get('plano') else ''}
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

<section id="videos" class="dark">
  <div class="wrap"><span class="eb">Exemplos em vídeo</span><h2>Veja o resultado.</h2>
    <p class="lead">Trabalhos recentes da Usina Vídeos. Toque para ver aqui mesmo.</p>
    <div class="pvs">{vids}</div>
    <div style="margin-top:24px"><a class="btn o" style="color:#fff" href="https://www.youtube.com/@CordialLevelPT" target="_blank" rel="noopener">Mais vídeos no YouTube →</a></div></div>
</section>

<section id="premium" class="dark" style="border-top:1px solid var(--line)">
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
    <div class="stats"><a href="/cordiallevel/" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Cordial Level</b><span>site, vídeos e podcast →</span></a><a href="/t4coral/" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Coral</b><span>apresentação em 4 línguas →</span></a><a href="https://century21.pt/ref/C0554-00006" target="_blank" rel="noopener" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>C21 Core</b><span>fotografia e vídeo →</span></a><a href="https://cdjregio.pt/" target="_blank" rel="noopener" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>CDJRegio</b><span>reportagem desportiva →</span></a></div>
  </div>
</section>

<section id="redes" class="dark" style="padding-top:0">
  <div class="wrap"><span class="eb">Siga o nosso trabalho</span><h2 style="font-size:clamp(26px,3vw,36px)">Redes e canais.</h2>
    <div class="side" style="margin-top:28px">{socials}<a class="mini yt" href="https://www.youtube.com/@DicasdoFreire/" target="_blank" rel="noopener">{YT_SVG}<div><b>Dicas do Freire</b><span>O canal de Freire Neto no YouTube.</span></div><em>Ver o canal →</em></a><a class="mini yt" href="https://www.youtube.com/@motoreseacao" target="_blank" rel="noopener">{MEA_ICON}<div><b>Motores e Ação</b><span>YouTube · @motoreseacao</span></div><em>Ver o canal →</em></a><a class="mini fb" href="https://www.facebook.com/usinacomvideos" target="_blank" rel="noopener"><svg width="34" height="34" viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" fill="#1877F2"/><path d="M13.5 20v-6h2l.4-2.5h-2.4V10c0-.7.3-1.3 1.4-1.3H16V6.5c-.3 0-1.1-.1-2-.1-2 0-3.2 1.2-3.2 3.3v1.8H8.7V14h2.1v6z" fill="#fff"/></svg><div><b>Usina Vídeos</b><span>Facebook · /usinacomvideos</span></div><em>Seguir →</em></a></div>
  </div>
</section>

<footer><div class="wrap" style="display:block;margin-bottom:28px">{mea_banner('pt', 'proposta')}</div><div class="wrap">
  <a href="/" aria-label="Usina Vídeos · página inicial"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <span>A sua exigência, a nossa assinatura. · © Usina Vídeos</span>
</div></footer>
<script>document.querySelectorAll('.yt2').forEach(function(b){{b.addEventListener('click',function(){{var i=document.createElement('iframe');i.src='https://www.youtube-nocookie.com/embed/'+b.dataset.id+'?autoplay=1&rel=0';i.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';i.allowFullscreen=true;i.title=b.getAttribute('aria-label');b.innerHTML='';b.appendChild(i)}},{{once:true}})}});</script>
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
