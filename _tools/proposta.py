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
VIDEOS = [('qwL_NxCdlNY', 'T4+1 no Condomínio Coral, Foz do Douro', 'Vídeo com a consultora Cheila Monteiro'),
          ('yo7RN7u6JJY', 'Terrenos em Monção', 'Drone e vídeo-reportagem · 1 min 45 s'),
          ('xEDuuPNMacM', 'T3 em Leça da Palmeira', 'Vídeo do imóvel com drone · 1 min 42 s'),
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

SITES = [('Página em usinavideos.pt', '100€', 'por página', 'A sua página de apresentação ou de imóvel no site da Usina, indexada no Google. Incluída na consultoria mensal.'),
         ('Site no seu domínio', '150€', 'uma vez', 'Configuração e migração para o seu domínio (ex. oseunome.pt), com HTTPS e redirecionamento das páginas antigas sem perder o Google.'),
         ('Alojamento', '0€', 'incluído', 'Alojamento rápido e seguro, sem custo de servidor. Só paga o domínio, diretamente à entidade de registo e em seu nome.'),
         ('Manutenção base', '25€', 'por mês', 'Site sempre no ar, HTTPS, cópias de segurança e pequenas correções até 1 hora por mês.'),
         ('Manutenção e atualização', '50€', 'por mês', 'A manutenção base e até 4 atualizações por mês: novos imóveis, vídeos, notícias ou blog.'),
         ('Trabalho extra', '20€', 'por hora', 'Novas secções, redesenho ou conteúdos fora do plano, com orçamento fechado antes de começar.')]

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
.cl{margin:18px 0 0;padding:0;list-style:none;display:grid;gap:8px}.cl li{padding-left:22px;position:relative;color:#D6D1CD}.cl li::before{content:"✓";position:absolute;left:0;color:var(--y);font-weight:900}
.cs{display:grid;grid-template-columns:1fr 1fr;gap:10px}.cs img{width:100%;height:100%;object-fit:cover;border-radius:14px;aspect-ratio:4/3}.cs img:first-child{grid-column:1/3;aspect-ratio:16/9}
.leads{margin-top:28px;display:grid;gap:18px 40px;grid-template-columns:1fr;background:#fff;border:1px solid #E3DED6;border-left:5px solid var(--g);border-radius:18px;padding:26px}@media(min-width:900px){.leads{grid-template-columns:1fr 1.6fr;align-items:center}}.leads h3{font-size:26px;margin-top:6px}.leads ul{margin:0;padding-left:20px;display:grid;gap:10px}
.ev{display:flex;flex-wrap:wrap;gap:16px 40px;align-items:center;justify-content:space-between}
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
    'cristina-russo': dict(nome='Cristina Russo', cidade='Leça da Palmeira', edicao=False,
        h1='A sua moradia em Leça, apresentada por quem conhece a zona.',
        intro='Proposta preparada para a Cristina Russo, consultora imobiliária da CENTURY 21 Arquitectos III (AMI 23921). Partimos da vídeo-reportagem que já fizemos à moradia T3 da Viela das Icas e juntamos um vídeo consigo a apresentar Leça, uma página própria do imóvel e uma campanha nas redes, a começar pelo open house de 29 de outubro. Ao fim de um mês avaliamos os resultados juntos.',
        hero='img/cr-leca.jpg',
        evento=('Open house', '29 de outubro · quinta-feira · 15h às 18h', 'Viela das Icas, n.º 7 · Leça da Palmeira', 'Antes do evento publicamos um Reel-convite e pomos a campanha a chegar a quem procura casa em Matosinhos e no Porto. No dia, podemos captar imagens para os conteúdos seguintes.'),
        juntos_t=('Já trabalhámos juntos', 'Os seus imóveis, pela Usina.', 'Os três imóveis que tem hoje à venda foram todos fotografados e filmados pela Usina. A moradia de Leça abre agora o novo vídeo e a página do imóvel.'),
        juntos=[('img/cr-leca-t.jpg', 'Moradia T3 em Leça da Palmeira', '745 000 € · 3 quartos · 3 WC · 188 m² · o imóvel desta proposta', 'https://cristinarusso.century21.pt/comprar/C0521-00227'),
                ('img/cr-valongo-t.jpg', 'T2 em Campo, Valongo', '210 000 € · 2 quartos · 1 WC · 80 m² · fotografia e vídeo', 'https://cristinarusso.century21.pt/comprar/C0521-00219'),
                ('img/cr-cerco-t.jpg', 'T3 no Cerco, Campanhã', '310 000 € · 3 quartos · 2 WC · 109 m² · fotografia e vídeo', 'https://cristinarusso.century21.pt/comprar/C0521-00222')],
        plano=[('Fase 1 · Esta semana', 'Vídeo «Viver em Leça»', 100, 175,
                ['Gravação consigo em cena a apresentar Leça: praia, Quinta da Conceição, comércio, autocarros', 'Imagens aéreas de Leça com drone', 'Final com o vídeo e as fotos da moradia que já produzimos', 'Versão YouTube (até 3 min) e 2 Reels, um deles convite para o open house']),
               ('Fase 2 · Semanas 1 e 2', 'Página de apresentação do imóvel', 50, 100,
                ['Página própria da moradia com fotos, vídeos, mapa e distâncias', 'Destaque para o open house de 29 de outubro', 'Botões de WhatsApp, chamada e e-mail diretos para si, com ligação a cristinarusso.century21.pt', 'Formulário de contacto para captar leads']),
               ('Fase 3 · Semanas 1 a 4', 'Gestão da campanha nas redes', 50, 100,
                ['Primeira semana dedicada a levar visitas ao open house', 'Anúncios Facebook e Instagram segmentados por zona e perfil de comprador', 'Ajustes semanais de público e criativos', 'Investimento em anúncios: 120€ no mês (30€ por semana), gerido pela Usina']),
               ('Fase 4 · Semana 5', 'Avaliação de resultados', 0, 0,
                ['Relatório de visualizações, cliques e contactos recebidos', 'Reunião de 30 minutos para decidir os próximos passos', 'Ajuste ou reforço da estratégia com base nos números'])],
        meta=120,
        passos=['Gravamos consigo em Leça no início da semana', 'Reel-convite publicado antes de 29 de outubro', 'Vídeo completo e página logo a seguir; avaliação ao fim de 1 mês'],
        zona_t='Viela das Icas, Leça da Palmeira · Matosinhos', zona_ref='Viela das Icas, n.º 7',
        zona_h2='Tudo a poucos passos, num bairro de topo.',
        zona_lead='É isto que vai mostrar no vídeo: autocarro, supermercados, farmácia, bancos e centro de saúde a menos de 5 minutos a pé, a Quinta da Conceição ao lado e a praia de Leça logo ali.',
        zona=[('Autocarro', 'Paragem Centro de Saúde de Leça', '200 m · 3 min a pé'), ('Supermercado', 'Mercadona', '270 m · 4 min a pé'),
              ('Supermercado', 'Pingo Doce e Continente', '350 a 550 m · 5 a 8 min a pé'), ('Farmácia', 'Farmácia Beleza', '300 m · 5 min a pé'),
              ('Banco', 'ABANCA, BPI e Santander', '220 a 800 m · 3 a 11 min a pé'), ('Saúde', 'USF Maresia (centro de saúde)', '250 m · 4 min a pé'),
              ('Saúde', 'Hospital Pedro Hispano', '3,3 km · 8 min de carro'), ('Escola', 'EB Eng. Fernando Pinto de Oliveira', '600 m · 9 min a pé'),
              ('Parque', 'Parque da Quinta da Conceição', '700 m · 10 min a pé'), ('Praia', 'Praia de Leça e Piscina das Marés', '1,3 a 1,5 km · 4 min de carro'),
              ('Compras', 'MAR Shopping e IKEA', '1,2 km · 4 min de carro'), ('Lazer', 'Farol e Casa de Chá da Boa Nova', '1,8 km · 5 min de carro'),
              ('Metro', 'Estação Mercado, Matosinhos', '1,3 km · 5 min de carro'), ('Viagens', 'Aeroporto Francisco Sá Carneiro', '5,5 km · 10 min de carro')]),
    'cristina-russo-mensal': dict(nome='Cristina Russo', cidade='Leça da Palmeira', edicao=False,
        h1='A referência em Leça da Palmeira tem um rosto. O seu.',
        intro='Proposta preparada para a Cristina Russo, consultora imobiliária da CENTURY 21 Arquitectos III (AMI 23921). Deixamos-lhe duas formas de trabalhar connosco: uma consultoria mensal, com vídeos e artes todas as semanas, as redes e campanhas geridas pela Usina e um site seu a captar contactos; ou ações à medida, em que escolhe só os vídeos e serviços de que precisa, quando precisa. O objetivo é o mesmo: que, em Leça, quem pensa em comprar, vender ou arrendar se lembre de si.',
        hero='/proposta/cristina-russo/img/cr-leca.jpg',
        juntos_t=('Já trabalhámos juntos', 'Os seus imóveis, pela Usina.', 'Os três imóveis que tem hoje à venda foram todos fotografados e filmados pela Usina. A moradia de Leça e o T3 do Cerco abrem o primeiro mês da consultoria.'),
        juntos=[('/proposta/cristina-russo/img/cr-leca-t.jpg', 'Moradia T3 em Leça da Palmeira', '745 000 € · 3 quartos · 3 WC · 188 m² · vídeo «Viver em Leça» no 1.º mês', 'https://cristinarusso.century21.pt/comprar/C0521-00227'),
                ('/proposta/cristina-russo/img/cr-cerco-t.jpg', 'T3 no Cerco, Campanhã', '310 000 € · 3 quartos · 2 WC · 109 m² · vídeo de divulgação no 1.º mês', 'https://cristinarusso.century21.pt/comprar/C0521-00222'),
                ('/proposta/cristina-russo/img/cr-valongo-t.jpg', 'T2 em Campo, Valongo', '210 000 € · 2 quartos · 1 WC · 80 m² · fotografia e vídeo', 'https://cristinarusso.century21.pt/comprar/C0521-00219')],
        acao=[('/cordiallevel/t3leca/img/leca-44-t.jpg', 'Vídeo consigo em cena', '110€', ' · por vídeo', ['Vlog ou vídeo consigo a apresentar a zona, um imóvel ou uma dica', 'Imagens aéreas com drone quando fizer sentido', 'Versão YouTube e Reel vertical, com legendas']),
              ('/proposta/cristina-russo/img/cr-cerco-t.jpg', 'Vídeo com imagens já captadas', '95€', ' · até 3 min', ['Montagem com as fotos e vídeos que já temos dos seus imóveis', 'Texto em off e legendas, sem precisar de nova gravação', 'Reel ou short avulso: 35€ + IVA']),
              ('/proposta/cristina-russo/img/cr-valongo-t.jpg', 'Reportagem de nova angariação', 'desde 40€', ' · por imóvel', ['Essencial 40€: fotografia e vídeo do imóvel', 'Aéreo 65€: com drone, em foto e vídeo', 'Completo 98€: com visita virtual 3D e planta']),
              ('/proposta/cristina-russo/img/cr-leca-t.jpg', 'Página do imóvel e campanha', '50€', ' · por página', ['Página do imóvel com fotos, vídeo, mapa e contactos diretos: 50€ com reportagem Usina (tabela 100€)', 'Gestão da campanha Facebook e Instagram: 100€ + IVA por imóvel', 'Transmissão em direto de open house: 300€ + IVA'])],
        ideias=[('Vlog', '«Um dia de consultora»', 'Visitas, angariações e reuniões, do pequeno-almoço ao fecho do dia'), ('Vlog', '«Um dia de mãe em Leça»', 'Escola, parques, compras e lazer: a zona vista por quem lá vive'),
                ('Vlog', 'Bastidores de produção', 'Como se prepara e grava um imóvel com a Usina'), ('Leça da Palmeira', '«Viver em Leça»', 'Praia, Boa Nova, Quinta da Conceição, comércio'),
                ('Matosinhos', '«Viver em Matosinhos»', 'Mar, mercado, restaurantes, metro e acessos'), ('Perafita', '«Viver em Perafita»', 'Praias, sossego e vida em família'),
                ('Lavra', '«Viver em Lavra»', 'Praia de Angeiras, natureza e tranquilidade'), ('Imagens captadas', 'T3 do Cerco: o espaço e as conveniências', 'Supermercados, transportes, acessos')],
        mensal=dict(preco=250, tabela=[('4 vídeos por mês, consigo em cena ou em reportagem', 440, '4 × 110€'),
                                        ('Página de apresentação e captação de contactos', 100, '1 por mês'),
                                        ('Gestão de redes, campanhas e contactos', 100, 'por mês')],
            fotos=[('/cordiallevel/t3leca/img/leca-44.jpg', 'Praia de Leça vista do céu'), ('/cordiallevel/t3leca/img/leca-40-t.jpg', 'Piscina das Marés, Leça da Palmeira'), ('/cordiallevel/t3leca/img/leca-46-t.jpg', 'Marginal de Leça da Palmeira')],
            cards=[('/cordiallevel/t3leca/img/leca-45-t.jpg', 'Todas as semanas', 'Vídeos para as suas redes',
                    ['2 dias de captação por mês, em Leça e nos seus imóveis', '4 vídeos por mês, em formato vertical e horizontal, com legendas', 'Vlogs: um dia de consultora, um dia de mãe na zona e bastidores de produção', 'Sítios e diferenciais de Leça, Matosinhos, Perafita e Lavra', 'Dicas: cafés, padarias, restaurantes, farmácias, serviços, zonas mais calmas e oportunidades']),
                   ('/proposta/cristina-russo/img/cr-cerco-t.jpg', 'Todas as semanas', 'Artes e textos',
                    ['4 artes por mês para Instagram e Facebook', 'Textos de cada publicação, prontos a publicar', 'Calendário editorial do mês, combinado consigo', 'Capas e miniaturas dos vídeos']),
                   ('/proposta/cristina-russo/img/cr-valongo-t.jpg', 'Todos os meses', 'Redes, campanhas e contactos',
                    ['Gestão do Instagram e da página de Facebook', 'Canal no YouTube com os seus vídeos', 'Campanhas Facebook, Instagram e Google Ads em Leça, Matosinhos, Perafita e Lavra, com foco em Leça', 'Relatório mensal com os números reais e reunião de acompanhamento']),
                   ('/proposta/cristina-russo/img/cr-leca-t.jpg', 'A sua presença online', 'O seu site e as angariações',
                    ['O seu site de apresentação em usinavideos.pt, pensado para captar contactos', '1 página de apresentação por mês incluída (tabela: 100€); as seguintes a 50€ + IVA', 'Enquanto for nossa cliente, o site fica no ar com os destaques, as vídeo-reportagens e as angariações', 'Padrão usinavideos.pt, indexado no Google, com divulgação a construir a sua autoridade online', 'Botões de WhatsApp, chamada e e-mail diretos para si e ligação a cristinarusso.century21.pt'])],
            arranque=['Criação da sua página de apresentação em usinavideos.pt', 'Criação da página de Facebook e do canal no YouTube', 'Configuração das contas de anúncios Meta e Google em seu nome'],
            mes1=['Vídeo «Viver em Leça», consigo em cena, com drone', 'Vídeo de divulgação do T3 do Cerco: o espaço do apartamento e as conveniências por perto', 'Mais 2 vídeos e as 4 artes do mês, segundo o calendário']),
        zona_t='Viela das Icas, Leça da Palmeira · Matosinhos', zona_ref='Viela das Icas, n.º 7',
        zona_h2='Tudo a poucos passos, num bairro de topo.',
        zona_lead='É isto que vai mostrar no vídeo: autocarro, supermercados, farmácia, bancos e centro de saúde a menos de 5 minutos a pé, a Quinta da Conceição ao lado e a praia de Leça logo ali.',
        zona=[('Autocarro', 'Paragem Centro de Saúde de Leça', '200 m · 3 min a pé'), ('Supermercado', 'Mercadona', '270 m · 4 min a pé'),
              ('Supermercado', 'Pingo Doce e Continente', '350 a 550 m · 5 a 8 min a pé'), ('Farmácia', 'Farmácia Beleza', '300 m · 5 min a pé'),
              ('Banco', 'ABANCA, BPI e Santander', '220 a 800 m · 3 a 11 min a pé'), ('Saúde', 'USF Maresia (centro de saúde)', '250 m · 4 min a pé'),
              ('Saúde', 'Hospital Pedro Hispano', '3,3 km · 8 min de carro'), ('Escola', 'EB Eng. Fernando Pinto de Oliveira', '600 m · 9 min a pé'),
              ('Parque', 'Parque da Quinta da Conceição', '700 m · 10 min a pé'), ('Praia', 'Praia de Leça e Piscina das Marés', '1,3 a 1,5 km · 4 min de carro'),
              ('Compras', 'MAR Shopping e IKEA', '1,2 km · 4 min de carro'), ('Lazer', 'Farol e Casa de Chá da Boa Nova', '1,8 km · 5 min de carro'),
              ('Metro', 'Estação Mercado, Matosinhos', '1,3 km · 5 min de carro'), ('Viagens', 'Aeroporto Francisco Sá Carneiro', '5,5 km · 10 min de carro')],),
    'ruben-assis': dict(nome='Rúben Assis', cidade='Gaia e região', edicao=False,
        h1='As suas angariações em vídeo e a sua voz como referência em Gaia.',
        intro='Proposta preparada para o Rúben Assis, Gestor de Ativos Imobiliários na Predilar (AMI 11428). Juntamos duas frentes: vídeo-reportagem de cada angariação, para vender mais rápido, e vídeos de autoridade em que o Rúben apresenta Gaia, Esmoriz, Ovar e a região, para ser a referência de quem quer comprar, vender ou investir. Ao fim de um mês avaliamos os resultados juntos.',
        plano_eb='O plano para a sua marca', plano_h2='Angariações em vídeo e conteúdo de autoridade: um mês para gerar contactos.',
        plano_lead='Quatro frentes, um só objetivo: que quem procura casa ou quer vender na sua zona pense primeiro em si. Os imóveis mostram o que tem, os vídeos de autoridade mostram quem é.',
        unid={65: ' · por imóvel', 100: ' · por vídeo'},
        orc_txt='Exemplo para o primeiro mês, com um vídeo de autoridade e uma angariação. Cada angariação a mais acresce 65€ + IVA (Pacote Aéreo) ou 98€ + IVA (Pacote Completo, com visita 3D). Os 120€ de anúncios vão integralmente para a Meta, sem margem: a Usina gere a campanha e mostra-lhe todos os números.',
        plano=[('Fase 1 · Semana 1', 'Vídeo de autoridade «Viver em Gaia»', 100, 100,
                ['Gravação consigo em cena a apresentar a zona: Cais de Gaia, praias, comércio, escolas, acessos', 'Imagens aéreas com drone', 'Versão YouTube (até 3 min) e 2 Reels verticais com legendas', 'Série a continuar: Esmoriz, Ovar, Espinho e Porto, um vídeo por zona']),
               ('Fase 2 · Cada angariação', 'Vídeo-reportagem do imóvel', 65, 65,
                ['Fotografia profissional e vídeo com drone (Pacote Aéreo)', 'Reel vertical consigo a apresentar o imóvel', 'Opcional: visita virtual 3D (Pacote Completo, 98€ + IVA)', 'Pronto para portais, redes sociais e WhatsApp']),
               ('Fase 3 · Semanas 1 a 4', 'Gestão da campanha nas redes', 50, 50,
                ['Publicação dos vídeos no Instagram, Facebook e YouTube do Rúben', 'Anúncios Facebook e Instagram segmentados por zona e perfil', 'Ajustes semanais de público e criativos', 'Investimento em anúncios: 120€ no mês (30€ por semana), gerido pela Usina']),
               ('Fase 4 · Semana 5', 'Avaliação de resultados', 0, 0,
                ['Relatório de visualizações, cliques e contactos recebidos', 'Reunião de 30 minutos para decidir os próximos passos', 'Ajuste do calendário de vídeos de autoridade e angariações'])],
        meta=120,
        passos=['Escolhemos a primeira angariação e o tema do vídeo de autoridade', 'Gravamos consigo em Gaia na mesma deslocação', 'Vídeos publicados na semana seguinte; avaliação ao fim de 1 mês'],
        zona_t='Gaia, Esmoriz, Ovar e região', zona_ref='as zonas onde atua', zona_note='Temas a escolher consigo. Gravações em Esmoriz e Ovar com deslocação fora do Grande Porto, negociada e indicada antes de cada gravação.',
        zona_h2='Uma série para ser a referência na sua zona.',
        zona_lead='Os vídeos de autoridade são a sua montra: o Rúben a mostrar a zona como quem a conhece, com dicas para quem compra, vende ou investe. Estas são as primeiras ideias de temas.',
        zona=[('Gaia', '«Viver em Gaia»', 'Cais, praias, escolas, acessos'), ('Gaia', 'Comprar casa em Gaia em 2027', 'Preços, zonas e crédito jovem'),
              ('Esmoriz', '«Viver em Esmoriz»', 'Praia, lagoa e qualidade de vida'), ('Ovar', '«Viver em Ovar»', 'Centro, praias do Furadouro e Cortegaça'),
              ('Dica', 'Comprar com emoção pode sair caro', 'Reel de 30 segundos'), ('Dica', 'Vender sem perder tempo nem dinheiro', 'Preço, fotos e visitas'),
              ('Dica', 'O que ninguém diz sobre o IMT', 'Custos de quem compra'), ('Investir', 'Investir em Gaia e no Porto', 'Arrendamento e valorização')]),
    'ricardo-ribeiro': dict(nome='Ricardo Ribeiro', cidade='Lisboa', edicao=True, h1='Vídeo para eventos, imóveis e reportagem.',
        intro='Proposta preparada para o Ricardo Ribeiro, jornalista em Lisboa, para eventos, imóveis e edição de material já captado. Do jornalista para o jornalista: a mesma linguagem de reportagem, com prazos de redação.'),
    'tiago-branquinha': dict(nome='Tiago Branquinha', cidade='Porto', edicao=False,
        h1='O seu T2 na Prelada, contado por quem conhece a zona.',
        intro='Proposta preparada para o Tiago Branquinha, consultor imobiliário da CENTURY 21 Arquitectos II (AMI 11414). Partimos da vídeo-reportagem que já fizemos ao T2 na Prelada e juntamos um vídeo consigo a apresentar a região, uma página própria do imóvel e uma campanha nas redes para gerar contactos. Ao fim de um mês avaliamos os resultados juntos.',
        hero='img/tb-predio.jpg',
        juntos_t=('A reportagem que já fizemos', 'O T2 na Prelada, pela Usina.', 'Fotografia e vídeo já entregues. São estas imagens que fecham o novo vídeo e dão vida à página do imóvel.'),
        juntos=[('img/tb-sala-t.jpg', 'Sala', 'Ampla, com luz natural'),
                ('img/tb-vista-t.jpg', 'Vista', 'Desafogada sobre a zona'),
                ('img/tb-cozinha-t.jpg', 'Cozinha', 'Equipada e funcional')],
        plano=[('Fase 1 · Semana 1', 'Vídeo «Viver na Prelada»', 100, 175,
                ['Gravação consigo em cena a apresentar a zona: metro, comércio, escolas, parques', 'Imagens novas da região e planos aéreos com drone', 'Final com as imagens do T2 que já temos', 'Versão YouTube (horizontal, até 3 min) e 2 Reels verticais com legendas']),
               ('Fase 2 · Semana 2', 'Página de apresentação do imóvel', 50, 100,
                ['Página própria do T2 com fotos, vídeos, planta, mapa e distâncias', 'Botões de WhatsApp, chamada e e-mail diretos para si, com ligação ao seu site e ao Facebook', 'Formulário de contacto para captar leads', 'Pronta a partilhar nos anúncios e nas redes']),
               ('Fase 3 · Semanas 2 a 5', 'Gestão da campanha nas redes', 50, 100,
                ['Anúncios Facebook e Instagram segmentados por zona e perfil de comprador', 'Vídeo e Reels a levar tráfego para a página do imóvel', 'Ajustes semanais de público e criativos', 'Investimento em anúncios: 120€ no mês (30€ por semana), gerido pela Usina']),
               ('Fase 4 · Semana 6', 'Avaliação de resultados', 0, 0,
                ['Relatório de visualizações, cliques e contactos recebidos', 'Reunião de 30 minutos para decidir os próximos passos', 'Ajuste ou reforço da estratégia com base nos números'])],
        meta=120,
        zona_t='Rua Dr. Cruz Malpique, Prelada · Ramalde, Porto', zona_ref='Rua Dr. Cruz Malpique',
        zona_h2='Tudo perto, num bairro calmo.',
        zona_lead='É isto que vai mostrar no vídeo: metro a 10 minutos a pé, supermercados, escola e hospital no bairro, e os jardins históricos da Prelada ao virar da esquina.',
        passos=['Marcamos a gravação consigo na Prelada', 'Vídeo e página prontos na semana seguinte', 'Avaliação conjunta ao fim de 1 mês de campanha'],
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
        if t == v:
            return f'<div class="pr">{v}€<small>+ IVA{e(c.get("unid", {}).get(v, ""))}</small></div>'
        return f'<div class="pr">{v}€<small>+ IVA</small></div><div class="tab">Tabela <s>{t}€</s> · <b>poupa {t - v}€</b></div>'
    cards = ''.join(f'<article style="--c:{COLORS[i % 3]}"><span class="lb">{e(f)}</span><h3>{e(n)}</h3>{pr(v, t)}<ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></article>' for i, (f, n, v, t, items) in enumerate(c['plano']))
    rows = ''.join(f'<tr><td>{e(n)}</td><td>{f"{t}€" if t else "—"}</td><td>{f"{v}€" if v else "Incluída"}</td><td class="dc">{f"−{t - v}€ ({round((t - v) * 100 / t)}%)" if t and t != v else "—"}</td></tr>' for f, n, v, t, items in c['plano'])
    tt = sum(x[3] for x in c['plano']); tv = sum(x[2] for x in c['plano']); m = c['meta']
    return f'''<section id="plano">
  <div class="wrap"><span class="eb">{e(c.get('plano_eb', 'O plano para o seu imóvel'))}</span><h2>{e(c.get('plano_h2', 'Vídeo, página e campanha: um mês para gerar contactos.'))}</h2>
    <p class="lead">{e(c.get('plano_lead', 'Quatro fases, um só contacto. Cada fase alimenta a seguinte: o vídeo leva às redes, as redes levam à página, a página leva até si.'))}</p>
    <div class="pk pk4">{cards}</div>
    <div style="overflow-x:auto;margin-top:28px;border-radius:14px"><table class="cmp" style="margin-top:0;min-width:560px"><thead><tr><th>Serviço</th><th>Preço de tabela</th><th>Para si</th><th>Desconto</th></tr></thead><tbody>{rows}
      <tr class="t"><td>Produção e gestão</td><td>{tt}€ + IVA</td><td>{tv}€ + IVA</td><td class="dc">{f"−{tt - tv}€ ({round((tt - tv) * 100 / tt)}%)" if tt != tv else "—"}</td></tr>
      <tr><td>Investimento em anúncios na Meta (4 semanas × 30€)</td><td>{m}€</td><td>{m}€</td><td>sem margem</td></tr>
      <tr class="t"><td>Total do primeiro mês <small style="font-weight:600">(IVA à parte na produção)</small></td><td>{tt + m}€</td><td>{tv + m}€</td><td class="dc">{f"−{tt - tv}€" if tt != tv else "—"}</td></tr></tbody></table></div>
    <div class="orc" style="margin-top:28px"><div><h3>{tv}€ + IVA + {m}€ em anúncios</h3><p>{c["orc_txt"] if c.get("orc_txt") else f"""Produção e gestão por {tv}€ + IVA, em vez de {tt}€ de tabela: um desconto de {tt - tv}€ por já ser nosso cliente. Os {m}€ de anúncios vão integralmente para a Meta, sem margem: a Usina gere e paga a campanha na sua conta de anúncios e, se precisar, emite-lhe a fatura."""}</p></div>
      <div><h4>Como avançamos</h4><ul>{''.join(f'<li>{e(x)}</li>' for x in c['passos'])}</ul></div></div>
    <div class="leads"><div><span class="eb">Os contactos são seus</span><h3>Cada contacto chega diretamente a si.</h3></div>
      <ul><li><b>WhatsApp, e-mail ou telefone:</b> quem responde ao vídeo, à página ou aos anúncios fala logo consigo, sem intermediários.</li><li><b>A Usina gera os contactos:</b> conteúdo, página e campanha a trabalhar para o imóvel.</li><li><b>O acompanhamento é seu:</b> a resposta, a qualificação e a marcação de visitas ficam a seu cargo.</li><li><b>Oferta Usina:</b> mensagens de resposta prontas a usar, para WhatsApp e e-mail, cordiais e pensadas para converter o contacto em visita.</li></ul></div>
    <p class="note">Drone sujeito às condições meteorológicas e às autorizações de voo. Os resultados da campanha dependem do mercado e do investimento; o relatório mostra os números reais, sem promessas de vendas.</p></div>
</section>
'''


def mensal_html(c):
    m = c['mensal']; tt = sum(x[1] for x in m['tabela']); pv = m['preco']
    cards = ''.join(f'<article style="--c:{COLORS[i % 3]}"><img class="pkimg" style="max-width:none" src="{im}" alt="" loading="lazy"><span class="lb">{e(f)}</span><h3>{e(n)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></article>' for i, (im, f, n, items) in enumerate(m['cards']))
    fotos = ''.join(f'<img src="{u}" alt="{e(a)}" loading="lazy">' for u, a in m['fotos'])
    rows = ''.join(f'<tr><td>{e(n)} <small style="color:var(--muted)">({e(d)})</small></td><td>{t}€</td></tr>' for n, t, d in m['tabela'])
    li = lambda xs: ''.join(f'<li>{e(x)}</li>' for x in xs)
    return f'''<section id="plano">
  <div class="wrap"><span class="eb">Opção 1 · Consultoria mensal · recomendada</span><h2>Um plano mensal para ser a referência em Leça.</h2>
    <p class="lead">Conteúdo todas as semanas, redes e campanhas geridas e uma página sua a captar contactos. Sai mais em conta do que investir em separado em cada imóvel, e cada mês soma ao anterior.</p>
    <div class="cs" style="margin-top:32px">{fotos}</div>
    <p class="note" style="margin-top:10px">Leça da Palmeira em imagens aéreas captadas pela Usina Vídeos. É este o cenário dos seus vídeos.</p>
    <div class="pk pk4">{cards}</div>
    <div style="overflow-x:auto;margin-top:28px;border-radius:14px"><table class="cmp" style="margin-top:0"><thead><tr><th>Incluído todos os meses</th><th>Preço de tabela</th></tr></thead><tbody>{rows}
      <tr><td>2 dias de captação, 4 artes e textos, calendário editorial</td><td>incluído</td></tr>
      <tr class="t"><td>Tabela mensal</td><td><s>{tt}€</s> + IVA</td></tr>
      <tr class="t"><td>Para si</td><td>{pv}€ + IVA por mês</td></tr>
      <tr><td>Pagamento</td><td>dia 1 do mês seguinte</td></tr>
      <tr><td>Desconto</td><td class="dc">−{tt - pv}€ por mês ({round((tt - pv) * 100 / tt)}%)</td></tr>
      <tr><td>Investimento em anúncios (Meta e Google)</td><td>à parte, sem margem</td></tr></tbody></table></div>
    <div class="orc" style="margin-top:28px"><div><h3>{pv}€ + IVA por mês</h3><p>Inclui 2 dias de captação por mês. Pagamento no dia 1 do mês seguinte ao dos trabalhos: paga o mês depois de o ver feito. Compromisso mínimo de 3 meses: é o tempo que a autoridade numa zona leva a construir-se. Com esse compromisso, o arranque fica incluído. Os anúncios são pagos diretamente por si, nas contas Meta e Google em seu nome, geridas pela Usina: vê cada fatura e o histórico das campanhas é sempre seu. O valor do investimento é definido consigo.</p></div>
      <div><h4>Arranque incluído</h4><ul>{li(m['arranque'])}</ul><h4 style="margin-top:16px">O primeiro mês</h4><ul>{li(m['mes1'])}</ul></div></div>
    <div class="leads"><div><span class="eb">Os contactos são seus</span><h3>Cada contacto chega diretamente a si.</h3></div>
      <ul><li><b>WhatsApp, e-mail ou telefone:</b> quem responde aos vídeos, à página ou aos anúncios fala logo consigo, sem intermediários.</li><li><b>A Usina gera os contactos:</b> conteúdo, páginas e campanhas a trabalhar para si e para os seus imóveis.</li><li><b>O acompanhamento é seu:</b> a resposta, a qualificação e a marcação de visitas ficam a seu cargo.</li><li><b>Oferta Usina:</b> mensagens de resposta prontas a usar, para WhatsApp e e-mail.</li></ul></div>
    <p class="note">Drone sujeito às condições meteorológicas e às autorizações de voo. Os resultados dependem do mercado e do investimento em anúncios; o relatório mensal mostra os números reais, sem promessas de vendas. Assinatura das peças: Cristina Russo | CENTURY 21 Arquitectos III · AMI 23921.</p></div>
</section>
'''


def acao_html(c):
    cards = ''.join(f'<article style="--c:{COLORS[i % 3]}"><img class="pkimg" style="max-width:none" src="{im}" alt="" loading="lazy"><span class="lb">À medida</span><h3>{e(n)}</h3><div class="pr">{('<small style="margin:0 8px 0 0">desde</small>' + p[6:]) if p.startswith('desde ') else p}<small>+ IVA</small></div><div class="tab">{e(u.strip(' ·'))}</div><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></article>' for i, (im, n, p, u, items) in enumerate(c['acao']))
    ideias = ''.join(f'<div class="zn" style="--c:{COLORS[i % 3]}"><span>{e(k)}</span><b>{e(n)}</b><em>{e(d)}</em></div>' for i, (k, n, d) in enumerate(c['ideias']))
    return f'''<section id="acao" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">Opção 2 · Por ação</span><h2>Só o que precisa, quando precisa.</h2>
    <p class="lead">Sem mensalidade nem compromisso: escolhe o vídeo ou o serviço, marcamos a gravação e entregamos. Ideal para começar, para uma angariação nova ou para um momento especial.</p>
    <div class="pk pk4">{cards}</div>
    <span class="eb" style="display:block;margin-top:48px">Desconto progressivo</span><h3 style="font-size:clamp(24px,2.6vw,32px);margin-top:6px">Quanto mais fazemos juntos, menos paga.</h3>
    <p class="lead" style="margin-top:10px">O desconto conta as ações de cada mês (vídeos, reportagens, páginas e campanhas) e aplica-se a todas elas. Quem trabalha connosco todos os meses ganha ainda o desconto de cliente frequente.</p>
    <div style="overflow-x:auto;margin-top:22px;border-radius:14px"><table class="cmp" style="margin-top:0"><thead><tr><th>Ações no mês</th><th>Desconto</th><th>Exemplo: vídeo em cena</th></tr></thead><tbody>
      <tr><td>1 ou 2 ações</td><td>preço de tabela</td><td>110€</td></tr>
      <tr><td>3 ou 4 ações</td><td class="dc">−10%</td><td>99€</td></tr>
      <tr><td>5 ou 6 ações</td><td class="dc">−15%</td><td>93,50€</td></tr>
      <tr><td>7 ou mais ações</td><td class="dc">−20%</td><td>88€</td></tr>
      <tr class="t"><td>Cliente frequente: 3 meses seguidos com ações</td><td class="dc">mais −5%</td><td>sobre o desconto do mês</td></tr></tbody></table></div>
    <p class="note">Valores + IVA. O desconto aplica-se à produção da Usina; o investimento em anúncios não tem desconto nem margem.</p>
    <span class="eb" style="display:block;margin-top:48px">Ideias de vídeos para si</span><h3 style="font-size:clamp(24px,2.6vw,32px);margin-top:6px">Por onde começar.</h3>
    <div class="zg">{ideias}</div>
    <div class="orc" style="margin-top:28px"><div><h3>Por ação ou por mês?</h3><p>Quatro vídeos consigo em cena, por ação, somam 396€ + IVA, já com o desconto de 10%. Na consultoria mensal, por 250€ + IVA, tem esses quatro vídeos e ainda as artes, a gestão das redes e das campanhas e o seu site. Pode começar por uma ação e passar ao plano mensal quando quiser.</p></div>
      <div><h4>Condições por ação</h4><ul><li>Pagamento após a entrega de cada trabalho</li><li>Fotografias em 48 horas; vídeo em 72 horas</li><li>Cada sessão de gravação dura até 1h30</li><li>Anúncios, quando os houver, pagos diretamente por si, sem margem</li></ul></div></div></div>
</section>
'''


def evento_html(c):
    t, d, l, p = c['evento']
    return f'''<section id="evento" style="padding:44px 0;background:var(--y)">
  <div class="wrap ev"><div><span class="eb" style="color:var(--ink)">{e(t)}</span><h2 style="margin-top:6px">{e(d)}</h2><p style="margin-top:6px;font-weight:700;color:var(--ink)">{e(l)}</p></div><p style="color:var(--ink);max-width:52ch">{e(p)}</p></div>
</section>
'''


def zona_html(c):
    cards = ''.join(f'<div class="zn" style="--c:{COLORS[i % 3]}"><span>{e(k)}</span><b>{e(n)}</b><em>{e(d)}</em></div>' for i, (k, n, d) in enumerate(c['zona']))
    return f'''<section id="zona" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">A zona · {e(c['zona_t'])}</span><h2>{e(c['zona_h2'])}</h2>
    <p class="lead">{e(c['zona_lead'])}</p>
    <div class="zg">{cards}</div>
    <p class="note">{e(c.get('zona_note', 'Distâncias aproximadas a partir de ' + c['zona_ref'] + ', em linha reta e tempos estimados. Confirmamos no terreno durante a gravação.'))}</p></div>
</section>
'''


def case_html():
    return f'''<section id="case" class="dark">
  <div class="wrap two" style="align-items:center">
    <div><span class="eb">Case · Condomínio Coral, Foz do Douro</span><h2>Um T4+1 apresentado em quatro línguas.</h2>
      <p style="margin-top:18px">Para a consultora <b style="color:#fff">Cheila Monteiro</b> (CENTURY 21 Arquitectos II · AMI 11414), fizemos a produção completa de um T4+1 de nova construção com 236 m² na Foz: fotografia, drone, vídeo com a consultora em cena e uma página própria do imóvel em português, inglês, espanhol e francês.</p>
      <ul class="cl"><li>Fotografia de interiores e exteriores</li><li>Planos aéreos com drone sobre a Foz</li><li>Vídeo com a consultora a apresentar o imóvel</li><li>Apresentação digital em 4 línguas, com simulação identificada como IA</li></ul>
      <div class="row" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:22px"><a class="btn y" href="/t4coral/">Ver a apresentação</a><a class="btn o" style="color:#fff" href="https://youtu.be/qwL_NxCdlNY" target="_blank" rel="noopener">Ver o vídeo da Cheila</a></div></div>
    <div class="cs"><img src="/img/coral-fachada.jpg" alt="Condomínio Coral, Foz do Douro" loading="lazy"><img src="/img/coral-drone-t.jpg" alt="Drone sobre a Foz do Douro" loading="lazy"><img src="/img/coral-cozinha-t.jpg" alt="Cozinha do T4+1 Coral" loading="lazy"></div>
  </div>
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
    cards = ''.join(f'<article class="card ic" style="--c:{COLORS[i % 3]}"><img src="{x[0]}" alt="{e(x[1])}" loading="lazy"><span class="n">{i + 1:02d}</span><h3>{e(x[1])}</h3><p>{e(x[2])}</p>' + (f'<p><a href="{x[3]}" target="_blank" rel="noopener" style="font-weight:800;color:var(--ink)">Ver o anúncio →</a></p>' if len(x) > 3 else '') + '</article>' for i, x in enumerate(c['juntos']))
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
    sites = ''.join(f'<article><b class="pr">{p}<small>{"+ IVA · " if p != "0€" else ""}{e(u)}</small></b><h3>{e(n)}</h3><p>{e(d)}</p></article>' for n, p, u, d in SITES)
    esp = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><h3>{e(a)}</h3><p>{b}</p></article>' for i, (a, b) in enumerate(ESPECIAIS))
    socials = ''.join(f'<a class="mini {k}" href="{u}" target="_blank" rel="noopener">{MEA_ICON if "motoreseacao" in u else (IG_SVG if k == "ig" else IN_SVG)}<div><b>{e(a)}</b><span>{e(b)}</span></div><em>{e(c)} →</em></a>' for u, k, a, b, c in T['pt']['socials'])
    steps = ''.join(f'<div class="step"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in STEPS)
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e('Proposta para ' + cliente['nome'] + ' · Usina Vídeos') if cliente else 'Proposta de serviços · Usina Vídeos'}</title>
<meta name="description" content="Proposta Usina Vídeos: produtora de conteúdo e comunicação. Vídeo, fotografia, drone, redes sociais, sites e campanhas digitais, com pacotes para imobiliário.">
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
  <div class="links">{'<a href="#edicao">Edição</a>' if cliente and cliente.get('edicao') else ''}{'<a href="#juntos">O nosso trabalho</a>' if cliente and cliente.get('juntos') else ''}{'<a href="#zona">A zona</a>' if cliente and cliente.get('zona') else ''}{'<a href="#plano">O plano</a>' if cliente and (cliente.get('plano') or cliente.get('mensal')) else ''}<a href="#case">Case</a><a href="#pacotes">Pacotes</a><a href="#videos">Vídeos</a><a href="#premium">Serviços premium</a><a href="#sites">Sites</a><a href="#condicoes">Condições</a><a href="/#trabalhos">Trabalhos</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Avançar</a>
</div></nav>

<header class="hero dark" style="min-height:min(70vh,620px)">
  <img src="{(cliente or {}).get('hero', '/img/foz-drone.jpg')}" srcset="{(cliente or {}).get('hero', '/img/foz-drone.jpg').replace('.jpg', '-t.jpg')} 900w, {(cliente or {}).get('hero', '/img/foz-drone.jpg')} 1920w" sizes="100vw" alt="" fetchpriority="high">
  <div class="wrap">
    <span class="eb">{e('Proposta para ' + cliente['nome'] + ' · ' + cliente['cidade']) if cliente else 'Proposta de serviços · Usina Vídeos'}</span>
    <h1>{e(cliente['h1']) if cliente else 'Comunicação, audiovisual e marketing digital.'}</h1>
    <p>{e(cliente['intro']) if cliente else 'Para empresas, marcas e profissionais: imobiliário, automóvel, desporto, comércio, turismo e eventos. Abaixo, os pacotes para imobiliário; para as outras áreas, orçamento à medida. Um parceiro, um briefing, um contacto.'}</p>
    <div class="row"><a class="btn y" href="{'#plano' if cliente and (cliente.get('plano') or cliente.get('mensal')) else '#pacotes'}">{'Ver o plano' if cliente and (cliente.get('plano') or cliente.get('mensal')) else 'Ver pacotes'}</a><a class="btn o" href="{CAL}" target="_blank" rel="noopener">Marcar sessão</a></div>
    {STRIPE}
  </div>
</header>

<section>
  <div class="wrap two">
    <div><span class="eb">Porquê um parceiro</span><h2>Avulso ou parceria estruturada?</h2>
      <p style="margin-top:20px">Contratar cada serviço a um fornecedor diferente gera custos imprevisíveis e qualidade variável de imóvel para imóvel. Com a Usina Vídeos, fotografia, vídeo, drone, visita 3D e apresentação digital saem da mesma equipa, com o mesmo padrão e um único contacto.</p>
      <p>A equipa é dirigida por <b>Freire Neto</b>, jornalista desde 1997 e fundador do Motores e Ação, e por <b>Sandra Freire</b>, responsável pela edição, produção e administração, com 20 anos de experiência em televisão, produtoras e no Motores e Ação.</p></div>
    <div class="stats"><div><b>25+</b><span>anos de reportagem</span></div><div><b>48h</b><span>entrega de fotografias</span></div><div><b>72h</b><span>vídeo e visita 3D</span></div><div><b>PT · EN · ES · FR</b><span>apresentações multilingues</span></div></div>
  </div>
</section>

<section style="background:var(--paper2)">
  <div class="wrap"><span class="eb">O que recebe</span><h2>Quatro entregáveis, um briefing.</h2>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">{ent}</div></div>
</section>

{case_html()}{edicao_html() if cliente and cliente.get('edicao') else ''}{juntos_html(cliente) if cliente and cliente.get('juntos') else ''}{evento_html(cliente) if cliente and cliente.get('evento') else ''}{zona_html(cliente) if cliente and cliente.get('zona') else ''}{plano_html(cliente) if cliente and cliente.get('plano') else ''}{mensal_html(cliente) if cliente and cliente.get('mensal') else ''}{acao_html(cliente) if cliente and cliente.get('acao') else ''}
<section id="pacotes">
  <div class="wrap"><span class="eb">Pacotes por imóvel</span><h2>Preços claros, por imóvel.</h2>
    <p class="lead">Valores sem IVA, que acresce à taxa legal em vigor. Para apartamentos e moradias até 300 m².</p>
    <div class="pk">{pk}</div>
    <div style="overflow-x:auto;margin-top:28px;border-radius:14px"><table class="cmp" style="margin-top:0;min-width:560px"><thead><tr><th>Entregável</th><th>Contratado em separado (média)</th><th>Usina Vídeos</th></tr></thead><tbody>
      <tr><td>Fotografia profissional</td><td>80–120€</td><td>Incluído</td></tr>
      <tr><td>Vídeo do imóvel</td><td>90–150€</td><td>Incluído</td></tr>
      <tr><td>Drone</td><td>60–80€</td><td>Incluído no Aéreo e no Completo</td></tr>
      <tr><td>Visita virtual 3D com planta</td><td>80–120€</td><td>Incluído no Completo</td></tr>
      <tr class="t"><td>Total</td><td>310–470€</td><td>98€ + IVA (Completo)</td></tr></tbody></table></div>
    <div class="cond" style="margin-top:22px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">
      <div><b>Até 300 m²</b>Preços válidos para apartamentos e moradias até 300 m².</div>
      <div><b>Quintas e moradias grandes</b>Quintas e moradias acima de T4 ou de 300 m²: proposta negociada caso a caso.</div>
      <div><b>Tratamento por IA e arrumação</b>Imóveis que precisem de tratamento de imagem por IA, arrumação virtual ou projeto: + 5€ + IVA por divisão. Sempre identificado como simulação.</div>
      <div><b>Deslocação</b>Incluída no Grande Porto. Fora do Grande Porto, a deslocação é negociada e indicada na proposta.</div>
    </div>
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

<section id="sites" class="dark" style="border-top:1px solid var(--line)">
  <div class="wrap"><span class="eb">Novo serviço · Sites e domínio próprio</span><h2>O seu site, no seu domínio, sempre atualizado.</h2>
    <p class="lead">O domínio fica em seu nome. A Usina trata do resto: alojamento, segurança, cópias de segurança e atualizações, no mesmo padrão das nossas páginas.</p>
    <div class="prem">{sites}</div>
    <div class="cond" style="margin-top:22px">
      <div style="background:var(--ink2);border-color:var(--line);color:#D6D1CD"><b style="color:#fff">O domínio é seu</b>Registado e pago por si (um domínio .pt custa, em regra, entre 10€ e 20€ por ano). A Usina fica como contacto técnico.</div>
      <div style="background:var(--ink2);border-color:var(--line);color:#D6D1CD"><b style="color:#fff">Clientes da consultoria mensal</b>A manutenção do site está incluída enquanto for nosso cliente.</div>
      <div style="background:var(--ink2);border-color:var(--line);color:#D6D1CD"><b style="color:#fff">Sem perder o Google</b>Ao mudar para o seu domínio, as páginas antigas redirecionam para as novas e o histórico de pesquisa acompanha.</div>
    </div></div>
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
      <div><b>Zona e deslocações</b>Deslocação incluída no Grande Porto. Fora do Grande Porto, a deslocação é negociada e indicada na proposta.</div>
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
