#!/usr/bin/env python3
"""Proposta para a Cordial Level: site no domínio próprio + manutenção. usinavideos.pt/proposta/cordial-level-site/

Página não indexada, com preços. Condições de cliente frequente.
Uso: python3 _tools/proposta_cordial_site.py  (depois: python3 _tools/tracking.py proposta/cordial-level-site/index.html)
"""
import html, os, sys, urllib.parse as up
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_usina import CSS, WA_SVG, STRIPE, COLORS
from mea_banner import MEA_CSS
from proposta import EXTRA_CSS, CAL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
WA = 'https://wa.me/351912988971?text=' + up.quote('Olá Freire, vi a proposta do site da Cordial Level no domínio próprio e gostava de avançar.')
HERO = '/cordiallevel/t3leca/img/leca-37.jpg'

LEVA = [('Site principal', 'Página inicial, destaques, imóveis, vender, usufruto, vídeos, canais e contactos, com os botões de WhatsApp do Casemiro e do Francisco.'),
        ('7 páginas de imóveis', 'Antero de Quental, Bosque da Pícua, Casarão da Foz, Cedofeita, Monção, Perafita e T3 de Leça, com fotos, vídeos, mapa e contactos.'),
        ('Vídeos e podcast', 'Os vídeos do canal @CordialLevelPT e os episódios do Panorama Imobiliário PT.'),
        ('Blog e web stories', 'Os artigos e as web stories da Cordial Level, que aparecem no Google e no Discover.'),
        ('Relatórios privados', 'Os relatórios mensais com palavra-passe, só para a direção.'),
        ('Google e redes', 'Indexação, mapa do site, partilhas no WhatsApp e redes com imagem e título certos.')]

# (serviço, tabela, para a Cordial, unidade, nota)
PRECOS = [('Migração para o domínio próprio', '150€', 'Oferta', 'uma vez', 'Configuração, HTTPS, testes e redirecionamento de todas as páginas antigas'),
          ('Alojamento', '0€', '0€', 'por mês', 'Rápido e seguro, sem custo de servidor'),
          ('Manutenção e atualização', '50€', '25€', 'por mês', 'Sem limite de atualizações para tudo o que a Usina produz para a Cordial'),
          ('E-mails no domínio (reencaminhamento)', '—', 'Incluído', '', 'geral@, casemiro@ e francisco@ a chegar às caixas de correio que já usam'),
          ('Páginas por zona: Leça, Maia, Vila do Conde', '100€', '50€', 'por página', 'Guia da zona, imóveis da zona, vídeos e contactos'),
          ('Trabalho extra (novas secções, redesenho)', '20€', '15€', 'por hora', 'Orçamento fechado antes de começar')]

INCL = ['Novas páginas de imóveis da Cordial, sempre que a Usina faz a reportagem', 'Vídeos, episódios do podcast, artigos e web stories publicados no site',
        'Relatório mensal privado com palavra-passe', 'Cópias de segurança e histórico de todas as versões do site',
        'HTTPS, velocidade e verificação de links e imagens', 'Acompanhamento no Google Search Console']

STEPS = [('Domínio', 'A Cordial regista o domínio em seu nome (por exemplo, cordiallevel.pt, a confirmar disponibilidade). Ajudamos no registo.'),
         ('Montagem', 'Configuramos o site no novo domínio e testamos tudo num endereço provisório, sem mexer no site atual.'),
         ('Mudança', 'Ativamos o domínio e redirecionamos as páginas antigas. Quem tiver um link antigo chega à página certa.'),
         ('Manutenção', 'A partir daí, o site é atualizado a cada imóvel, vídeo ou artigo, com relatório mensal.')]


def build():
    leva = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b) in enumerate(LEVA))
    def cel(v):
        return v if v in ('Oferta', 'Incluído', '—', '0€') else f'{v} + IVA'
    rows = ''.join(f'<tr><td><b>{e(n)}</b><br><small>{e(d)}</small></td><td>{"<s>" + e(cel(t)) + "</s>" if t not in ("—", "0€") else e(t)}{"<br><small>" + e(u) + "</small>" if u else ""}</td><td class="dc"><b>{e(cel(c))}</b>{"<br><small>" + e(u) + "</small>" if u else ""}</td></tr>' for n, t, c, u, d in PRECOS)
    incl = ''.join(f'<li>{e(x)}</li>' for x in INCL)
    steps = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b) in enumerate(STEPS))
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Proposta para a Cordial Level · Site no domínio próprio · Usina Vídeos</title>
<meta name="description" content="O site da Cordial Level no seu domínio próprio, com alojamento, manutenção e atualização pela Usina Vídeos.">
<meta name="robots" content="noindex, follow">
<meta name="theme-color" content="#141213">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}{MEA_CSS}{EXTRA_CSS}
.mhero{{position:relative;color:#fff;padding:110px 0 70px;border-bottom:6px solid var(--y);background:#141213 url({HERO}) center/cover}}
.mhero::before{{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(20,18,19,.94) 0%,rgba(20,18,19,.8) 55%,rgba(20,18,19,.45) 100%)}}
.mhero .wrap{{position:relative}}.mhero h1{{font-size:clamp(34px,5.4vw,64px);line-height:1.04;margin-top:12px;color:#fff;max-width:17ch}}
.mhero p{{margin-top:18px;font-size:19px;line-height:1.55;color:#D6D1CD;max-width:60ch}}.mhero .eb{{color:var(--y)}}
.shots{{display:grid;gap:18px;grid-template-columns:1fr;margin-top:30px;align-items:end}}@media(min-width:800px){{.shots{{grid-template-columns:3fr 1fr}}}}
.shots img{{width:100%;height:auto;display:block;border-radius:14px;border:1px solid #E3DED6;box-shadow:0 18px 40px rgba(0,0,0,.12)}}
.shots .ph{{max-width:240px;justify-self:center;border-radius:26px;border:6px solid #141213}}
.mtab{{width:100%;border-collapse:collapse;background:#fff;border-radius:14px;overflow:hidden;font-size:15px}}.mtab th,.mtab td{{padding:13px 15px;border-bottom:1px solid #E3DED6;text-align:left;vertical-align:top}}.mtab th{{background:var(--ink);color:#fff;font-size:12px;letter-spacing:.08em;text-transform:uppercase}}.mtab small{{color:var(--muted);font-weight:600}}.mtab td.dc b{{color:#23863D}}
.mtab tr.t td{{background:var(--paper2);font-weight:900}}
@media(max-width:640px){{.mtab thead{{display:none}}.mtab tr{{display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid #E3DED6;padding:14px 16px;gap:4px 12px}}.mtab td{{border:0;padding:2px 0}}.mtab td:first-child{{grid-column:1/3;font-size:16px}}.mtab td:nth-child(2)::before{{content:"Tabela ";color:var(--muted);font-size:12px}}.mtab td:nth-child(3)::before{{content:"Para a Cordial ";color:var(--muted);font-size:12px}}}}
</style>
</head>
<body>
<nav class="nav" aria-label="Menu"><div class="wrap">
  <a class="logo" href="/"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <div class="links"><a href="#hoje">O site hoje</a><a href="#leva">O que muda</a><a href="#precos">Investimento</a><a href="#como">Como avançamos</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Avançar</a>
</div></nav>

<header class="mhero"><div class="wrap">
  <span class="eb">Proposta para a Cordial Level · Casemiro Ramos e Francisco Medeiros</span>
  <h1>O site da Cordial Level, no seu próprio domínio.</h1>
  <p>Levamos o site que já construímos juntos para um endereço só vosso, com o mesmo padrão, os mesmos imóveis e vídeos, e a Usina a tratar do alojamento, da manutenção e de cada atualização. Por serem clientes frequentes, com condições especiais.</p>
  {STRIPE}
</div></header>

<section id="hoje">
  <div class="wrap"><span class="eb">O site hoje</span><h2>Já está feito. Agora ganha casa própria.</h2>
    <p class="lead">O site da Cordial Level vive hoje em usinavideos.pt/cordiallevel. No domínio próprio, a marca fica mais forte: um endereço curto para cartões, anúncios e assinaturas de e-mail, e uma presença no Google que é só vossa.</p>
    <div class="shots"><img src="img/cl-desktop.jpg" alt="Site atual da Cordial Level no computador" loading="lazy"><img class="ph" src="img/cl-mobile.jpg" alt="Site atual da Cordial Level no telemóvel" loading="lazy"></div>
    <p class="note">O site atual: <a href="/cordiallevel/" style="font-weight:800;color:var(--ink)">usinavideos.pt/cordiallevel →</a></p></div>
</section>

<section id="leva" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">O que passa para o novo domínio</span><h2>Tudo, sem perder nada.</h2>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">{leva}</div>
    <p class="note" style="margin-top:18px">Os endereços antigos redirecionam para os novos: os links já partilhados continuam a funcionar e o Google transfere o histórico de pesquisa. No rodapé fica a indicação «Site por Usina Vídeos».</p></div>
</section>

<section id="precos">
  <div class="wrap"><span class="eb">Investimento · condições de cliente frequente</span><h2>O preço de quem já trabalha connosco.</h2>
    <p class="lead">A tabela da Usina e, ao lado, as condições para a Cordial Level. O domínio é registado e pago pela Cordial, em seu nome (um .pt custa, em regra, entre 10€ e 20€ por ano).</p>
    <div style="margin-top:26px;border-radius:14px;overflow:hidden"><table class="mtab"><thead><tr><th>Serviço</th><th>Tabela</th><th>Para a Cordial</th></tr></thead><tbody>{rows}
      <tr class="t"><td>Primeiro ano (migração e 12 meses de manutenção)</td><td><s>750€ + IVA</s></td><td class="dc"><b>300€ + IVA</b><br><small>poupança de 450€ (60%)</small></td></tr></tbody></table></div>
    <div class="orc" style="margin-top:28px"><div><h3>25€ + IVA por mês</h3><p>Migração oferecida e manutenção com 50% de desconto, enquanto a Cordial Level for cliente da Usina. As caixas de correio completas (para enviar e-mails a partir do domínio), se as quiserem, são contratadas diretamente pela Cordial a um fornecedor como o Google ou a Microsoft.</p></div>
      <div><h4>Incluído na manutenção</h4><ul>{incl}</ul></div></div>
  </div>
</section>

<section id="como" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">Como avançamos</span><h2>Em cerca de uma semana, sem interrupções.</h2>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">{steps}</div>
    <p class="note" style="margin-top:18px">Prazo indicativo de 5 dias úteis depois de o domínio estar registado. O site atual continua no ar até à mudança.</p></div>
</section>

<section class="dark">
  <div class="wrap two">
    <div><span class="eb">Vamos avançar?</span><h2>Freire Neto</h2>
      <p style="margin-top:14px">Jornalista Profissional · Produtor de Conteúdo. A Usina Vídeos produz o site, os vídeos e o podcast da Cordial Level desde o primeiro dia.</p>
      <div class="row" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:22px"><a class="btn y" href="{WA}" target="_blank" rel="noopener">{WA_SVG}WhatsApp +351 912 988 971</a><a class="btn o" style="color:#fff" href="{CAL}" target="_blank" rel="noopener">Marcar conversa</a></div>
      <p style="margin-top:18px">E-mail: <a href="mailto:freireneto@me.com" style="color:var(--y)">freireneto@me.com</a></p></div>
    <div class="stats"><a href="/cordiallevel/" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Cordial Level</b><span>o site atual →</span></a><a href="https://www.youtube.com/@CordialLevelPT" target="_blank" rel="noopener" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>YouTube</b><span>@CordialLevelPT →</span></a><a href="/proposta/" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Tabela Usina</b><span>todos os serviços →</span></a><a href="/" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Usina Vídeos</b><span>trabalhos →</span></a></div>
  </div>
</section>

<footer><div class="wrap">
  <a href="/" aria-label="Usina Vídeos · página inicial"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <span>A sua exigência, a nossa assinatura. · © Usina Vídeos</span>
</div></footer>
</body>
</html>
'''


if __name__ == '__main__':
    d = os.path.join(ROOT, 'proposta', 'cordial-level-site')
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(build())
    print('ok proposta cordial-level-site')
