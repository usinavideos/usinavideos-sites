#!/usr/bin/env python3
"""Proposta por ação para o Tiago Branquinha: apartamento para arrendar no Bessa (reportagem + página com captação).

Usa o visual novo (CSS e provas de proposta_v2.py). Gera /proposta/tiago-branquinha-bessa/index.html (noindex).
Uso: python3 _tools/proposta_tiago_bessa.py   (depois: python3 _tools/tracking.py proposta/tiago-branquinha-bessa/index.html)
"""
import html, os, sys
import urllib.parse as up
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proposta import VIDEOS, CAL, VALIDADE
from proposta_v2 import CSS, PROVAS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = 'tiago-branquinha-bessa'
e = lambda s: html.escape(str(s), quote=True)
WA = 'https://wa.me/351912988971?text=' + up.quote('Olá Freire, vi a proposta para o apartamento do Bessa e quero avançar.')
IMG = '/proposta/tiago-branquinha/img/'
HERO = '/img/foz-drone.jpg'

REPORTAGEM, PAGINA, PAGINA_TABELA = 40, 50, 100
TOTAL, TABELA = REPORTAGEM + PAGINA, REPORTAGEM + PAGINA_TABELA

JUNTOS = [('tb-predio-t.jpg', 'O prédio', 'Fachada, na Rua Dr. Cruz Malpique'),
          ('tb-sala-t.jpg', 'A sala', 'Ampla, com luz natural'),
          ('tb-cozinha-t.jpg', 'A cozinha', 'Equipada e funcional')]

ACOES = [
    (IMG + 'tb-sala-t.jpg', 'Reportagem do apartamento', f'{REPORTAGEM}€', 'Pacote Essencial',
     ['Fotografia profissional de alta resolução, editada para os portais e para as redes',
      'Vídeo do imóvel, editado com música',
      'Oferta: fotografia e vídeo aéreos com drone, do prédio e da zona do Bessa',
      'Captação na sexta, 27, ou no sábado, 28 de novembro, entre as 10h e as 15h',
      'Fotografias em 48 horas, vídeo em 72']),
    (IMG + 'tb-vista-t.jpg', 'Página do imóvel', f'{PAGINA}€', f'tabela {PAGINA_TABELA}€',
     ['Página própria em usinavideos.pt com fotos, vídeo, ficha, condições de arrendamento e mapa',
      'Botões de WhatsApp, chamada e e-mail diretos para si',
      'Pedido de visita, avaliação gratuita e análise de financiamento, descritos mais abaixo',
      'Fica privada, com palavra-passe, até a aprovar']),
]

CAPTA = [('Para quem quer arrendar', 'Pedido de visita', 'Chega-lhe por WhatsApp já com a data de entrada e o número de pessoas. Menos conversas sem perfil.'),
         ('Para proprietários', 'Quanto vale a sua casa na Boavista?', 'Avaliação gratuita, com visita e sem obrigação de vender ou arrendar. O pedido vai direto para si.'),
         ('Para quem pensa comprar', 'Quanto pode financiar?', 'Uma análise antes de procurar casa. Os seus quase 17 anos de banca são o argumento.'),
         ('Para todos', 'Porquê a CENTURY 21', 'A rede, a agência no Bessa e a sua forma de trabalhar, com o texto que nos indicar.')]

IDEIAS = [('A zona deste imóvel', '«Viver no Bessa»', 'Consigo em cena, da porta da agência ao apartamento.'),
          ('As suas zonas', '«Viver em Ermesinde»', 'O mesmo formato em Águas Santas e na Maia.'),
          ('Autoridade', '«Arrendar no Porto: o que precisa de saber»', 'Caução, fiador, documentos e prazos, explicados por si.'),
          ('Bastidores', '«Um dia de consultor»', 'Angariação, visitas e escritura, em vlog.')]

PEDIR = ['Tipologia, renda e condições de arrendamento (caução, fiador)',
         'Se o apartamento está mobilado e equipado',
         'Uma fotografia sua, para os contactos da página',
         'A entidade de intermediação de crédito com que a Arquitectos II trabalha',
         'Os diferenciais da CENTURY 21 que quer destacar']

EXTRA_CSS = """
.copy h1{max-width:17ch}.copy .sub{font-size:14px;opacity:.85;margin:14px 0 0}
.ims.st figure{aspect-ratio:4/3}.ims.st div h3{margin:14px 0 4px;font-size:21px}.ims.st div p{margin:0;color:#4A4543;font-size:15px}
.shot .tb{font-size:14px;color:var(--cinza);margin-top:2px}
.fica{margin-top:40px;display:grid;grid-template-columns:1fr 1.4fr;gap:clamp(24px,5vw,80px);padding-top:32px;border-top:2px solid var(--carvao)}
.fica h3{margin:0;font-size:clamp(22px,2.6vw,30px);line-height:1.15}.fica p{margin:0;color:#4A4543;max-width:60ch}
@media (max-width:800px){.fica{grid-template-columns:1fr}}
.dep{display:grid;grid-template-columns:1.3fr 1fr;gap:clamp(28px,5vw,80px);align-items:start}
.dep ul{margin:18px 0 0;padding-left:18px;color:#4A4543}.dep li{margin:5px 0}
@media (max-width:860px){.dep{grid-template-columns:1fr}}
.cta .sub{font-size:14px;margin:14px 0 0}
.ui .loc{position:absolute;bottom:6px;right:44px;opacity:.85}@media (max-width:700px){.ui .loc{display:none}}
"""


def li(xs):
    return ''.join(f'<li>{e(x)}</li>' for x in xs)


def build():
    juntos = ''.join(f'<div><figure><img src="{IMG}{im}" alt="{e(t)} do T2 na Prelada" loading="lazy"></figure><h3>{e(t)}</h3><p>{e(d)}</p></div>' for im, t, d in JUNTOS)
    acoes = ''.join(f'<div class="shot"><img src="{im}" alt="" loading="lazy"><div><h3>{e(n)}</h3><div class="pr">{e(p)} <small>+ IVA</small></div><div class="tb">{e(tb)}</div></div><ul>{li(items)}</ul></div>' for im, n, p, tb, items in ACOES)
    capta = ''.join(f'<div><span>{e(k)}</span><b>{e(n)}</b><em>{e(d)}</em></div>' for k, n, d in CAPTA)
    ideias = ''.join(f'<div><span>{e(k)}</span><b>{e(n)}</b><em>{e(d)}</em></div>' for k, n, d in IDEIAS)
    provas = ''.join(f'<a href="{u}"><img src="{im}" alt="{e(t)}" loading="lazy"><span>{e(t)}</span></a>' for im, t, u in PROVAS)
    vids = ''.join(f'<figure><button class="yt" data-id="{v}" aria-label="Ver vídeo: {e(t)}"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="" loading="lazy"><i></i></button><figcaption><b>{e(t)}</b><span>{e(d)}</span></figcaption></figure>' for v, t, d in [VIDEOS[2], VIDEOS[3], VIDEOS[5]])
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Proposta para Tiago Branquinha · Apartamento no Bessa · Usina Vídeos</title>
<meta name="description" content="Proposta da Usina Vídeos para Tiago Branquinha: fotografia, vídeo e página do apartamento para arrendar no Bessa, Porto.">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="Proposta para Tiago Branquinha · Usina Vídeos"><meta property="og:description" content="Fotografia, vídeo e página do apartamento no Bessa: {TOTAL}€ + IVA.">
<meta property="og:image" content="https://usinavideos.pt{HERO}"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#211E1F">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/img/logo/usina-simbolo-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,400..900&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="{HERO}">
<style>{CSS}{EXTRA_CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Menu">
  <a href="/" aria-label="Usina Vídeos, início"><img src="/img/logo/usina-horizontal.svg" alt="Usina Vídeos"></a>
  <div class="links"><a href="#plano">A proposta</a><a href="#pagina">A página</a><a href="#trabalhos">Trabalhos</a><a href="#depois">A seguir</a></div>
  <a class="btn btn-dark" href="{WA}" target="_blank" rel="noopener">Aceitar a proposta</a>
</nav>

<header class="hero">
  <div class="vf">
    <img src="{HERO}" alt="Foz do Douro vista do céu, filmada pela Usina Vídeos com drone" fetchpriority="high">
    <div class="ui" aria-hidden="true"><span class="c tl"></span><span class="c tr"></span><span class="c bl"></span><span class="c br"></span><span class="rec"><i></i>REC</span><span class="tc" id="tc">00:00:00:00</span><span class="loc">Foz do Douro · drone Usina</span></div>
    <div class="copy">
      <p class="para">Proposta para Tiago Branquinha · Bessa, Porto</p>
      <h1 class="wide">Um arrendamento no Bessa que lhe traz proprietários.</h1>
      <p class="in">Fotografia e vídeo do apartamento por cima da agência, drone de oferta e uma página que marca visitas e convida os proprietários da Boavista a pedirem-lhe uma avaliação. {TOTAL}€ + IVA.</p>
      <div class="acts"><a class="btn btn-y" href="#plano">Ver a proposta</a><a class="btn btn-line" href="#pagina">Ver o que a página faz</a></div>
      <p class="sub">Gravação na sexta, 27, ou no sábado, 28 de novembro. Sem mensalidade.</p>
    </div>
  </div>
</header>
<div class="trust"><div class="wrap"><span><b>{TOTAL}€ + IVA</b> reportagem e página</span><span><b>48h</b> fotografias · <b>72h</b> vídeo</span><span><b>Drone</b> de oferta</span><span><b>T2 na Prelada</b> já filmado para si</span><span><b>Desde 2002</b> a fazer reportagem</span></div></div>

<section id="imoveis">
  <div class="wrap"><p class="kick">Já trabalhámos juntos</p><h2 class="h2 wide">O seu T2 na Prelada, pela Usina.</h2>
    <p class="lead">Fotografia e vídeo já entregues. O apartamento do Bessa segue o mesmo cuidado, num formato mais leve, pensado para arrendar.</p>
    <div class="ims st">{juntos}</div></div>
</section>

<section id="plano" class="opt">
  <div class="wrap">
    <div class="opt-head">
      <div><p class="kick">A proposta · Apartamento no Bessa</p><h2 class="h2 wide">Só o necessário para arrendar bem.</h2>
        <p class="lead">Pediu uma fotorreportagem sem grande investimento. Fica com fotografia e vídeo pelo pacote de entrada, o drone de oferta e a página do imóvel a metade do preço por ser feita com a nossa reportagem.</p></div>
      <div class="price"><div class="tab">Preço de tabela <s>{TABELA + 25}€</s></div><b>{TOTAL}€ <small>+ IVA</small></b><span class="poup">Poupa {TABELA + 25 - TOTAL}€ · drone de oferta</span>
        <p>Paga depois da entrega. Sem mensalidade nem compromisso.</p></div>
    </div>
    <div class="shots">{acoes}</div>
    <table><thead><tr><th>Incluído</th><th>Preço de tabela</th></tr></thead><tbody>
      <tr><td>Reportagem Essencial <small style="color:var(--cinza)">(fotografia e vídeo)</small></td><td>{REPORTAGEM}€</td></tr>
      <tr><td>Drone <small style="color:var(--cinza)">(diferença para o Pacote Aéreo)</small></td><td>25€</td></tr>
      <tr><td>Página do imóvel <small style="color:var(--cinza)">({PAGINA}€ com reportagem Usina)</small></td><td>{PAGINA_TABELA}€</td></tr>
      <tr><td>Tabela</td><td><s>{TABELA + 25}€</s> + IVA</td></tr>
      <tr class="hl"><td>Para si, com o drone de oferta</td><td>{TOTAL}€ + IVA</td></tr>
</tbody></table>
    <p class="note">Esta proposta não inclui anúncios pagos. Se quiser reforçar a divulgação, a gestão de campanha é orçamentada à parte e o investimento em anúncios não tem margem.</p>
    <div class="more"><a class="btn btn-dark" href="{WA}" target="_blank" rel="noopener">Aceitar por WhatsApp</a></div>
  </div>
</section>

<section id="pagina" style="background:var(--estudio)">
  <div class="wrap"><p class="kick">O que a página faz por si</p><h2 class="h2 wide">Um imóvel, quatro tipos de contacto.</h2>
    <p class="lead">Quem procura casa para arrendar no Porto vê muitos anúncios. Entre essas pessoas há proprietários e futuros compradores. A página fala com cada um e todos os pedidos chegam diretamente a si.</p>
    <div class="ideias">{capta}</div>
    <div class="fica"><h3>Depois de arrendado, a página fica.</h3><p>O imóvel passa a «Arrendado» e os pedidos de avaliação e de análise de financiamento continuam ativos, com o seu nome, a sua fotografia e a assinatura da agência.</p></div>
    <p class="note">A intermediação de crédito aparece identificada com a entidade registada que nos indicar. O crédito está sempre sujeito a aprovação das instituições. A página segue o método que usamos noutras páginas CENTURY 21, com a sua marca e os seus contactos.</p>
    <div class="more"><a class="btn btn-line" href="/cordiallevel/foco/">Ver a página de um arrendamento</a><a class="btn btn-line" href="/cordiallevel/avaliacao/">Ver uma página de avaliação</a></div></div>
</section>

<section id="trabalhos" class="dark">
  <div class="wrap"><p class="kick">O nosso trabalho</p><h2 class="h2 wide">Veja o resultado na prática.</h2>
    <p class="lead">Imóveis do Porto a Monção, com fotografia, drone, vídeo e páginas próprias. Toque numa imagem para ver o projeto.</p>
    <div class="grid">{provas}</div>
    <div class="vids">{vids}</div>
    <div class="more"><a class="btn btn-line" href="/portefolio/">Ver o portefólio completo</a></div></div>
</section>

<section id="depois" style="background:#fff">
  <div class="wrap">
    <div class="dep">
      <div><p class="kick">A seguir, se fizer sentido</p><h2 class="h2 wide">Do Bessa às suas zonas.</h2>
        <p class="lead">Este trabalho serve também de teste. Se gostar do resultado, a consultoria mensal junta tudo num plano: conteúdo todas as semanas, redes e campanhas geridas e um site seu a captar contactos.</p>
        <ul><li>4 vídeos por mês, consigo em cena ou em reportagem</li><li>4 artes, 2 dias de captação e gestão das redes</li><li>Campanhas Meta e Google e 1 página de imóvel por mês</li><li>O seu site em usinavideos.pt enquanto for cliente</li></ul></div>
      <div class="price"><div class="tab">Preço de tabela <s>640€</s> por mês</div><b>250€ <small>+ IVA por mês</small></b>
        <p>Compromisso mínimo de 3 meses, com o arranque incluído. Paga no dia 1 do mês seguinte. Falamos disto depois da gravação, sem compromisso.</p></div>
    </div>
    <div class="ideias">{ideias}</div></div>
</section>

<section class="dark">
  <div class="wrap"><p class="kick">Como arrancamos</p><h2 class="h2 wide">Do sim à página no ar.</h2>
    <div class="steps">
      <div class="step"><h3>Aceita a proposta</h3><p>Por WhatsApp. Escolhe o dia: sexta, 27, ou sábado, 28 de novembro.</p></div>
      <div class="step"><h3>Gravamos no Bessa</h3><p>Entre as 10h e as 15h, com luz natural e drone, se o tempo deixar. Apartamento arrumado e estores abertos.</p></div>
      <div class="step"><h3>Recebe o material</h3><p>Fotografias em 48 horas e vídeo em 72, prontos para os portais e para as redes.</p></div>
      <div class="step"><h3>Aprova a página</h3><p>Vê a página em privado, pede ajustes e só depois fica pública.</p></div>
    </div>
    <div class="leads"><h3>O que precisamos de si.</h3>
      <ul>{li(PEDIR)}</ul></div>
  </div>
</section>

<section class="cta">
  <div class="wrap"><h2 class="h2 wide">Gravamos na sexta ou no sábado, Tiago?</h2>
    <p class="lead" style="color:var(--carvao)">Responda por WhatsApp com o dia que prefere. Valores válidos até {VALIDADE}.</p>
    <div class="row"><a class="btn btn-dark" href="{WA}" target="_blank" rel="noopener">Aceitar por WhatsApp</a><a class="btn btn-line" href="{CAL}" target="_blank" rel="noopener">Marcar uma conversa</a><a class="btn btn-line" href="mailto:freireneto@me.com">freireneto@me.com</a></div>
    <p class="sub">Resposta no próprio dia. Paga depois da entrega.</p>
    <p class="on"><i></i>Freire Neto · +351 912 988 971</p>
    <p class="note" style="color:#4A3A10">Drone sujeito às condições meteorológicas e às autorizações de voo. A página gera contactos, sem promessas de arrendamento, de vendas ou de angariações. Assinatura das peças: Tiago Branquinha | CENTURY 21 Arquitectos II · AMI 11414.</p></div>
</section>

<footer><div class="wrap"><a href="/"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos"></a><span>A sua exigência, a nossa assinatura. · © Usina Vídeos</span></div></footer>
<script>
(function(){{var t=document.getElementById('tc'),f=0,r=matchMedia('(prefers-reduced-motion: reduce)').matches;if(t&&!r)setInterval(function(){{f++;var s=Math.floor(f/25),p=function(n){{return('0'+n).slice(-2)}};t.textContent='00:'+p(Math.floor(s/60))+':'+p(s%60)+':'+p(f%25)}},40);}})();
document.querySelectorAll('.yt').forEach(function(b){{b.addEventListener('click',function(){{var i=document.createElement('iframe');i.src='https://www.youtube-nocookie.com/embed/'+b.dataset.id+'?autoplay=1&rel=0';i.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';i.allowFullscreen=true;i.title=b.getAttribute('aria-label');b.innerHTML='';b.appendChild(i)}},{{once:true}})}});
</script>
</body>
</html>
'''


if __name__ == '__main__':
    d = os.path.join(ROOT, 'proposta', SLUG)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, 'index.html')
    open(p, 'w').write(build())
    print('ok', p)
