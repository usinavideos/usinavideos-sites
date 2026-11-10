#!/usr/bin/env python3
"""Propostas da Usina Vídeos no visual novo (o da capa de nov. 2026): Archivo, carvão/estúdio/amarelo, visor de câmara.

Lê os dados do cliente de proposta.py (CLIENTES) e gera /proposta/<slug>/index.html (noindex).
Só para clientes listados em V2; os outros continuam no modelo antigo até serem reenviados.
Uso: python3 _tools/proposta_v2.py   (depois: python3 _tools/tracking.py proposta/*/index.html)
"""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proposta import CLIENTES, VIDEOS, WA, CAL, VALIDADE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2 = ['cristina-russo-mensal']
EXTRA = {'cristina-russo-mensal': dict(hero_v2='/cordiallevel/t3leca/img/leca-44.jpg', hero_alt='Praia de Leça da Palmeira vista do céu, filmada pela Usina')}
e = lambda s: html.escape(str(s), quote=True)

# trabalhos do portefólio mostrados em todas as propostas imobiliárias (imagem, título, link)
PROVAS = [('/portefolio/img/p01-t.jpg', 'Condomínio Coral, Foz do Douro', '/t4coral/'),
          ('/portefolio/img/p07-t.jpg', 'T3 em Leça da Palmeira', '/cordiallevel/t3leca/'),
          ('/portefolio/img/p03-t.jpg', 'T2 em Perafita, Matosinhos', '/cordiallevel/perafita/'),
          ('/portefolio/img/p09-t.jpg', 'Moradia T4 na Foz do Douro', '/cordiallevel/casaraofoz/'),
          ('/portefolio/img/p05-t.jpg', 'Terrenos em Monção', '/cordiallevel/moncao/'),
          ('/portefolio/img/p13-t.jpg', 'T1 duplex em Cedofeita, Porto', '/cordiallevel/cedofeita/')]

CSS = """
:root{--carvao:#211E1F;--estudio:#F4F4F1;--cinza:#77716E;--linha:#D9D6D2;--amarelo:#E5AE29;--rec:#D0252F;--verde:#3EB15C;--pad:clamp(20px,4vw,56px)}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:72px}
body{margin:0;background:var(--estudio);color:var(--carvao);font-family:Archivo,system-ui,sans-serif;font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums}
img{display:block;max-width:100%}a{color:inherit}
:focus-visible{outline:3px solid var(--amarelo);outline-offset:3px}
.wide{font-stretch:125%;font-variation-settings:"wdth" 125;font-weight:800;letter-spacing:-.02em;line-height:.98}
.wrap{max-width:1240px;margin:0 auto;padding:0 var(--pad)}
.btn{display:inline-flex;align-items:center;gap:10px;padding:16px 26px;border-radius:4px;font-weight:700;text-decoration:none;font-size:16px;line-height:1}
.btn-y{background:var(--amarelo);color:var(--carvao)}.btn-y:hover{background:#F0BD3A}
.btn-line{border:1.5px solid currentColor}.btn-dark{background:var(--carvao);color:#fff}
.nav{position:sticky;top:0;z-index:30;display:flex;align-items:center;gap:20px;padding:12px var(--pad);background:var(--estudio);box-shadow:0 1px 0 var(--linha)}
.nav img{height:28px;width:auto}
.nav .links{display:flex;gap:22px;margin-left:auto}.nav .links a{text-decoration:none;font-weight:600;font-size:15px}.nav .links a:hover{color:#9A7210}
.nav .btn{padding:11px 18px;font-size:14px}
@media (max-width:900px){.nav .links{display:none}.nav .btn{margin-left:auto}}
/* hero: o visor */
.hero{background:var(--carvao);padding:clamp(16px,3vw,40px) var(--pad) 0}
.vf{position:relative;max-width:1400px;margin:0 auto;border-radius:6px;overflow:hidden;min-height:min(86vh,760px);display:flex;align-items:flex-end}
.vf>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vf::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(33,30,31,.35),rgba(33,30,31,0) 30%,rgba(33,30,31,.15) 50%,rgba(33,30,31,.85))}
.ui{position:absolute;inset:18px;z-index:2;pointer-events:none;color:#fff;font-size:13px;font-weight:600;font-variant-numeric:tabular-nums}
.ui .c{position:absolute;width:28px;height:28px;border:2px solid rgba(255,255,255,.85)}
.ui .tl{top:0;left:0;border-right:0;border-bottom:0}.ui .tr{top:0;right:0;border-left:0;border-bottom:0}.ui .bl{bottom:0;left:0;border-right:0;border-top:0}.ui .br{bottom:0;right:0;border-left:0;border-top:0}
.ui .rec{position:absolute;top:6px;left:44px;display:flex;gap:8px;align-items:center}
.ui .rec i{width:10px;height:10px;border-radius:50%;background:var(--rec);animation:blink 1.2s steps(1) infinite}@keyframes blink{50%{opacity:0}}
.ui .tc{position:absolute;top:6px;right:44px}
.copy{position:relative;z-index:3;color:#fff;padding:0 clamp(28px,5vw,72px) clamp(44px,7vw,84px);max-width:1100px}
.copy .para{font-size:15px;font-weight:600;opacity:.9;margin:0 0 14px}
.copy h1{font-size:clamp(38px,6vw,92px);margin:0;max-width:14ch}
.copy p.in{font-size:clamp(17px,1.5vw,20px);max-width:56ch;margin:22px 0 28px;opacity:.92}
.copy .acts{display:flex;gap:12px;flex-wrap:wrap}.copy .btn-line{color:#fff}
@media (max-width:700px){.hero{padding:10px 10px 0}.vf{min-height:auto;padding-top:120px}.vf::after{background:linear-gradient(180deg,rgba(33,30,31,.45),rgba(33,30,31,.2) 25%,rgba(33,30,31,.92) 70%)}.ui{inset:12px}.copy{padding:0 22px 36px}.copy h1{font-size:36px}.copy p.in{font-size:16px;margin:16px 0 22px}.copy .para{font-size:13px}}
.trust{background:var(--carvao);color:#CFCAC6;padding:28px 0 32px}
.trust .wrap{display:flex;flex-wrap:wrap;gap:12px 40px}.trust b{color:#fff;font-size:18px;font-stretch:112%}
section{padding:clamp(64px,9vw,120px) 0}
.h2{font-size:clamp(32px,4.6vw,60px);margin:0 0 24px;max-width:18ch}
.lead{font-size:19px;max-width:60ch;color:#4A4543;margin:0}
.kick{font-weight:700;font-size:15px;color:#9A7210;margin:0 0 12px}
.dark .kick{color:var(--amarelo)}
.note{font-size:14px;color:var(--cinza);max-width:80ch;margin-top:22px}
/* imóveis */
.ims{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:40px}
.ims a{text-decoration:none;display:block}
.ims figure{margin:0;aspect-ratio:4/3;overflow:hidden;border-radius:4px;background:#ddd}
.ims img{width:100%;height:100%;object-fit:cover;transition:transform .5s}.ims a:hover img{transform:scale(1.03)}
.ims h3{margin:14px 0 4px;font-size:21px}.ims p{margin:0;color:#4A4543;font-size:15px}.ims .lk{display:inline-block;margin-top:8px;font-weight:700;font-size:15px;border-bottom:2px solid var(--amarelo)}
@media (max-width:800px){.ims{grid-template-columns:1fr}}
/* opções */
.opt{background:#fff}
.opt-head{display:grid;grid-template-columns:1.3fr 1fr;gap:clamp(28px,5vw,80px);align-items:end}
.price{border:2px solid var(--carvao);border-radius:4px;padding:26px 28px;background:var(--estudio)}
.price .tab{color:var(--cinza);font-size:15px}.price .tab s{font-weight:700}
.price b{display:block;font-size:clamp(44px,5vw,68px);font-stretch:125%;font-weight:800;line-height:1;margin:8px 0 6px}
.price b small{font-size:18px;font-stretch:100%;font-weight:600}
.price .poup{display:inline-block;background:var(--amarelo);font-weight:700;padding:4px 10px;border-radius:3px;font-size:14px}
.price p{margin:12px 0 0;font-size:15px;color:#4A4543}
@media (max-width:860px){.opt-head{grid-template-columns:1fr}}
.shots{margin-top:44px;border-top:2px solid var(--carvao)}
.shot{display:grid;grid-template-columns:120px minmax(180px,1fr) 2fr;gap:24px;padding:24px 0;border-bottom:1px solid var(--linha);align-items:start}
.shot img{width:120px;height:84px;object-fit:cover;border-radius:3px}
.shot h3{margin:0;font-size:clamp(20px,2.2vw,26px)}.shot .fq{font-size:14px;color:var(--cinza);margin-top:4px}
.shot ul{margin:0;padding-left:18px;color:#4A4543}.shot li{margin:3px 0}
.shot .pr{font-weight:800;font-size:22px;font-stretch:112%;margin-top:6px}.shot .pr small{font-size:14px;font-weight:600;color:var(--cinza)}
@media (max-width:760px){.shot{grid-template-columns:1fr;gap:10px}.shot img{width:100%;height:180px}}
.two{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5vw,80px);margin-top:48px}
.two h3{margin:0 0 10px;font-size:22px}.two ul{margin:0;padding-left:18px}.two li{margin:5px 0}
@media (max-width:800px){.two{grid-template-columns:1fr}}
table{width:100%;border-collapse:collapse;margin-top:18px;font-size:16px}
th,td{text-align:left;padding:13px 12px;border-bottom:1px solid var(--linha)}th{font-size:14px;color:var(--cinza);font-weight:600}
td:last-child,th:last-child{text-align:right;white-space:nowrap}
@media (max-width:560px){table{font-size:15px}th,td{padding:10px 6px}td:last-child,th:last-child{white-space:normal}}
tr.hl td{font-weight:800;background:var(--estudio)}td.dc{color:#1E7A3A;font-weight:700}
.vs{margin-top:40px;background:var(--amarelo);border-radius:4px;padding:28px clamp(22px,4vw,40px);display:grid;grid-template-columns:1fr 1.4fr;gap:24px;align-items:center}
.vs h3{margin:0;font-size:clamp(24px,2.8vw,34px)}.vs p{margin:0}
@media (max-width:800px){.vs{grid-template-columns:1fr}}
/* ideias */
.ideias{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--linha);border:1px solid var(--linha);margin-top:36px}
.ideias div{background:var(--estudio);padding:20px}.ideias span{font-size:13px;color:var(--cinza);font-weight:600}
.ideias b{display:block;font-size:18px;line-height:1.25;margin:4px 0}.ideias em{font-style:normal;font-size:15px;color:#4A4543}
@media (max-width:900px){.ideias{grid-template-columns:1fr 1fr}}@media (max-width:520px){.ideias{grid-template-columns:1fr}}
/* provas */
.dark{background:var(--carvao);color:#E9E6E3}.dark .h2{color:#fff}.dark .lead{color:#BDB7B3}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.grid a{text-decoration:none;position:relative;display:block;border-radius:4px;overflow:hidden;aspect-ratio:4/3}
.grid img{width:100%;height:100%;object-fit:cover;transition:transform .5s}.grid a:hover img{transform:scale(1.04)}
.grid span{position:absolute;left:0;right:0;bottom:0;padding:28px 14px 12px;font-weight:600;font-size:15px;color:#fff;background:linear-gradient(transparent,rgba(0,0,0,.7))}
@media (max-width:800px){.grid{grid-template-columns:1fr 1fr}}
.vids{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:48px}
.vids figure{margin:0}.vids figcaption b{display:block;color:#fff;margin-top:10px}.vids figcaption span{font-size:14px;color:#A9A3A0}
.yt{position:relative;display:block;width:100%;aspect-ratio:16/9;border:0;padding:0;border-radius:4px;overflow:hidden;background:#000;cursor:pointer}
.yt img{width:100%;height:100%;object-fit:cover;opacity:.85}.yt iframe{width:100%;height:100%;border:0}
.yt i{position:absolute;left:50%;top:50%;width:64px;height:64px;margin:-32px 0 0 -32px;border-radius:50%;background:var(--amarelo)}
.yt i::after{content:"";position:absolute;left:26px;top:20px;border:12px solid transparent;border-left:18px solid var(--carvao)}
@media (max-width:800px){.vids{grid-template-columns:1fr}}
.more{margin-top:32px;display:flex;flex-wrap:wrap;gap:12px}.dark .btn-line{color:#fff}
/* zona */
.zona{display:grid;grid-template-columns:1fr 1fr;gap:0 clamp(28px,5vw,80px);margin-top:36px}
.zona div{display:grid;grid-template-columns:1fr auto;gap:12px;padding:13px 0;border-bottom:1px solid var(--linha)}
.zona b{font-weight:600}.zona b small{display:block;font-size:13px;color:var(--cinza);font-weight:600}.zona em{font-style:normal;color:#4A4543;font-size:15px;text-align:right}
@media (max-width:760px){.zona{grid-template-columns:1fr}}
/* processo */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;margin-top:40px;counter-reset:s}
.step{border-top:2px solid var(--amarelo);padding-top:18px}
.step::before{counter-increment:s;content:counter(s);font-stretch:125%;font-weight:800;font-size:44px;color:var(--amarelo);display:block;line-height:1;margin-bottom:12px}
.step h3{margin:0 0 6px;font-size:20px;color:#fff}.step p{margin:0;color:#BDB7B3;font-size:16px}
@media (max-width:900px){.steps{grid-template-columns:1fr 1fr}}@media (max-width:560px){.steps{grid-template-columns:1fr}}
.leads{display:grid;grid-template-columns:1fr 1.4fr;gap:clamp(28px,5vw,80px);margin-top:64px;padding-top:40px;border-top:1px solid #3A3536}
.leads h3{margin:0;font-size:clamp(24px,2.6vw,32px);color:#fff}.leads ul{margin:0;padding-left:18px;color:#CFCAC6}.leads li{margin:6px 0}.leads b{color:#fff}
@media (max-width:800px){.leads{grid-template-columns:1fr}}
.cta{background:var(--amarelo)}.cta .h2{max-width:16ch}
.cta .row{display:flex;flex-wrap:wrap;gap:14px;margin-top:30px}
.cta .on{display:inline-flex;align-items:center;gap:8px;margin-top:22px;font-size:15px}.cta .on i{width:9px;height:9px;border-radius:50%;background:var(--verde)}
footer{background:var(--carvao);color:#A9A3A0;padding:44px 0;font-size:14px}
footer .wrap{display:flex;flex-wrap:wrap;gap:16px 32px;align-items:center;justify-content:space-between}footer img{height:28px;width:auto}
@media (prefers-reduced-motion:reduce){.ui .rec i{animation:none}.ims img,.grid img{transition:none}}
"""


def li(xs):
    return ''.join(f'<li>{e(x)}</li>' for x in xs)


def build(slug, c):
    m = c['mensal']
    tt = sum(x[1] for x in m['tabela']); pv = m['preco']; pct = round((tt - pv) * 100 / tt)
    hero = c.get('hero_v2', c.get('hero', '/img/foz-drone.jpg')); hero_alt = c.get('hero_alt', c['cidade'])
    ims = ''.join(f'<a href="{u}" target="_blank" rel="noopener"><figure><img src="{im}" alt="{e(t)}" loading="lazy"></figure><h3>{e(t)}</h3><p>{e(d)}</p><span class="lk">Ver o anúncio</span></a>' for im, t, d, u in c['juntos'])
    freq = ['Todas as semanas', 'Todas as semanas', 'Todos os meses', 'Sempre no ar']
    mens = ''.join(f'<div class="shot"><img src="{im}" alt="" loading="lazy"><div><h3>{e(n)}</h3><div class="fq">{e(freq[i])}</div></div><ul>{li(items)}</ul></div>' for i, (im, f, n, items) in enumerate(m['cards']))
    rows = ''.join(f'<tr><td>{e(n)} <small style="color:var(--cinza)">({e(d)})</small></td><td>{t}€</td></tr>' for n, t, d in m['tabela'])
    acao = ''.join(f'<div class="shot"><img src="{im}" alt="" loading="lazy"><div><h3>{e(n)}</h3><div class="pr">{e(p)} <small>+ IVA{e(u)}</small></div></div><ul>{li(items)}</ul></div>' for im, n, p, u, items in c['acao'])
    ideias = ''.join(f'<div><span>{e(k)}</span><b>{e(n)}</b><em>{e(d)}</em></div>' for k, n, d in c['ideias'])
    provas = ''.join(f'<a href="{u}"><img src="{im}" alt="{e(t)}" loading="lazy"><span>{e(t)}</span></a>' for im, t, u in PROVAS)
    vids = ''.join(f'<figure><button class="yt" data-id="{v}" aria-label="Ver vídeo: {e(t)}"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="" loading="lazy"><i></i></button><figcaption><b>{e(t)}</b><span>{e(d)}</span></figcaption></figure>' for v, t, d in [VIDEOS[0], VIDEOS[2], VIDEOS[1]])
    zona = ''.join(f'<div><b><small>{e(k)}</small>{e(n)}</b><em>{e(d)}</em></div>' for k, n, d in c['zona'])
    nome1 = c['nome'].split()[0]
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Proposta para {e(c['nome'])} · Usina Vídeos</title>
<meta name="description" content="Proposta da Usina Vídeos para {e(c['nome'])}: vídeos, redes, campanhas e site para ser a referência em {e(c['cidade'])}.">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="Proposta para {e(c['nome'])} · Usina Vídeos"><meta property="og:description" content="Duas formas de trabalharmos juntos: consultoria mensal ou ações à medida.">
<meta property="og:image" content="https://usinavideos.pt{hero}"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#211E1F">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/img/logo/usina-simbolo-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,400..900&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="{hero}">
<style>{CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Menu">
  <a href="/" aria-label="Usina Vídeos, início"><img src="/img/logo/usina-horizontal.svg" alt="Usina Vídeos"></a>
  <div class="links"><a href="#imoveis">Os seus imóveis</a><a href="#mensal">Consultoria mensal</a><a href="#acao">Por ação</a><a href="#trabalhos">Trabalhos</a><a href="#zona">Leça</a></div>
  <a class="btn btn-y" href="{WA}" target="_blank" rel="noopener">Aceitar a proposta</a>
</nav>

<header class="hero">
  <div class="vf">
    <img src="{hero}" alt="{e(hero_alt)}" fetchpriority="high">
    <div class="ui" aria-hidden="true"><span class="c tl"></span><span class="c tr"></span><span class="c bl"></span><span class="c br"></span><span class="rec"><i></i>REC</span><span class="tc" id="tc">00:00:00:00</span></div>
    <div class="copy">
      <p class="para">Proposta para {e(c['nome'])} · {e(c['cidade'])}</p>
      <h1 class="wide">A referência em Leça tem um rosto. O seu.</h1>
      <p class="in">Vídeos todas as semanas, redes e campanhas geridas e um site seu a captar contactos. Para que, em Leça, quem pensa em comprar, vender ou arrendar se lembre de si.</p>
      <div class="acts"><a class="btn btn-y" href="#mensal">Ver a consultoria mensal</a><a class="btn btn-line" href="#acao">Ver por ação</a></div>
    </div>
  </div>
</header>
<div class="trust"><div class="wrap"><span><b>{pv}€ + IVA</b> por mês, tudo incluído</span><span><b>3</b> imóveis seus já filmados pela Usina</span><span><b>48h</b> fotografias · <b>72h</b> vídeo</span><span><b>Desde 2002</b> a fazer reportagem</span></div></div>

<section id="imoveis">
  <div class="wrap"><p class="kick">Já trabalhámos juntos</p><h2 class="h2 wide">Os seus imóveis, pela Usina.</h2>
    <p class="lead">Os três imóveis que tem hoje à venda foram fotografados e filmados por nós. A moradia de Leça e o T3 do Cerco abrem o primeiro mês da consultoria.</p>
    <div class="ims">{ims}</div></div>
</section>

<section id="mensal" class="opt">
  <div class="wrap">
    <div class="opt-head">
      <div><p class="kick">Opção 1 · Consultoria mensal · a que recomendamos</p><h2 class="h2 wide">Um plano por mês para ser a referência em Leça.</h2>
        <p class="lead">Conteúdo todas as semanas, redes e campanhas geridas e uma página sua a captar contactos. Cada mês soma ao anterior.</p></div>
      <div class="price"><div class="tab">Preço de tabela <s>{tt}€</s> por mês</div><b>{pv}€ <small>+ IVA por mês</small></b><span class="poup">Poupa {tt - pv}€ por mês · −{pct}%</span>
        <p>Paga no dia 1 do mês seguinte: vê o mês feito antes de pagar. Compromisso mínimo de 3 meses, com o arranque incluído.</p></div>
    </div>
    <div class="shots">{mens}</div>
    <div class="two">
      <div><h3>Arranque incluído</h3><ul>{li(m['arranque'])}</ul></div>
      <div><h3>O primeiro mês</h3><ul>{li(m['mes1'])}</ul></div>
    </div>
    <table><thead><tr><th>Incluído todos os meses</th><th>Preço de tabela</th></tr></thead><tbody>{rows}
      <tr><td>2 dias de captação, 4 artes e textos, calendário editorial</td><td>incluído</td></tr>
      <tr><td>Tabela mensal</td><td><s>{tt}€</s> + IVA</td></tr>
      <tr class="hl"><td>Para si</td><td>{pv}€ + IVA por mês</td></tr>
      <tr><td>Investimento em anúncios (Meta e Google)</td><td>à parte, sem margem</td></tr></tbody></table>
    <p class="note">Os anúncios são pagos diretamente por si, nas contas Meta e Google em seu nome, geridas pela Usina: vê cada fatura e o histórico das campanhas é sempre seu. O valor é definido consigo.</p>
  </div>
</section>

<section id="acao">
  <div class="wrap"><p class="kick">Opção 2 · Por ação</p><h2 class="h2 wide">Só o que precisa, quando precisa.</h2>
    <p class="lead">Sem mensalidade nem compromisso: escolhe o vídeo ou o serviço, marcamos a gravação e entregamos. Paga depois de cada entrega.</p>
    <div class="shots">{acao}</div>
    <h3 style="margin:48px 0 0;font-size:24px">Quanto mais fazemos juntos, menos paga.</h3>
    <table><thead><tr><th>Ações no mês</th><th>Desconto</th><th>Vídeo em cena</th></tr></thead><tbody>
      <tr><td>1 ou 2 ações</td><td>preço de tabela</td><td>110€</td></tr>
      <tr><td>3 ou 4 ações</td><td class="dc">−10%</td><td>99€</td></tr>
      <tr><td>5 ou 6 ações</td><td class="dc">−15%</td><td>93,50€</td></tr>
      <tr><td>7 ou mais ações</td><td class="dc">−20%</td><td>88€</td></tr>
      <tr><td>Cliente frequente (3 meses seguidos)</td><td class="dc">mais −5%</td><td>sobre o desconto do mês</td></tr></tbody></table>
    <p class="note">Valores + IVA. O desconto aplica-se à produção da Usina; o investimento em anúncios não tem desconto nem margem.</p>
    <div class="vs"><h3>Por ação ou por mês?</h3><p>Quatro vídeos consigo em cena, por ação, somam 396€ + IVA, já com 10% de desconto. Na consultoria, por {pv}€ + IVA, tem esses quatro vídeos e ainda as artes, as redes, as campanhas e o seu site. Pode começar por uma ação e passar ao plano mensal quando quiser.</p></div>
  </div>
</section>

<section style="background:#fff">
  <div class="wrap"><p class="kick">Ideias de vídeos para si</p><h2 class="h2 wide">Por onde começar.</h2>
    <div class="ideias">{ideias}</div></div>
</section>

<section id="trabalhos" class="dark">
  <div class="wrap"><p class="kick">O nosso trabalho</p><h2 class="h2 wide">Veja o resultado na prática.</h2>
    <p class="lead">Imóveis do Porto a Monção, com fotografia, drone, vídeo e páginas próprias. Toque numa imagem para ver o projeto.</p>
    <div class="grid">{provas}</div>
    <div class="vids">{vids}</div>
    <div class="more"><a class="btn btn-y" href="/portefolio/">Ver o portefólio completo</a><a class="btn btn-line" href="/t4coral/">Ver a página do Coral, em 4 línguas</a></div></div>
</section>

<section id="zona">
  <div class="wrap"><p class="kick">A zona · {e(c['zona_t'])}</p><h2 class="h2 wide">{e(c['zona_h2'])}</h2>
    <p class="lead">{e(c['zona_lead'])}</p>
    <div class="zona">{zona}</div>
    <p class="note">Distâncias aproximadas a partir de {e(c['zona_ref'])}, em linha reta, com tempos estimados. Confirmamos no terreno durante a gravação.</p></div>
</section>

<section class="dark">
  <div class="wrap"><p class="kick">Como arrancamos</p><h2 class="h2 wide">Do sim ao primeiro vídeo.</h2>
    <div class="steps">
      <div class="step"><h3>Aceita a proposta</h3><p>Por WhatsApp ou numa conversa de 20 minutos. Escolhe a consultoria ou a primeira ação.</p></div>
      <div class="step"><h3>Preparamos o arranque</h3><p>A sua página, o Facebook, o YouTube e as contas de anúncios em seu nome.</p></div>
      <div class="step"><h3>Gravamos consigo</h3><p>Dois dias por mês em Leça e nos seus imóveis. Fotografias em 48 horas, vídeo em 72.</p></div>
      <div class="step"><h3>Medimos e ajustamos</h3><p>Relatório mensal com os números reais e uma reunião para decidir o mês seguinte.</p></div>
    </div>
    <div class="leads"><h3>Cada contacto chega diretamente a si.</h3>
      <ul><li><b>WhatsApp, e-mail ou telefone:</b> quem responde aos vídeos, à página ou aos anúncios fala logo consigo.</li><li><b>A Usina gera os contactos:</b> conteúdo, páginas e campanhas a trabalhar para si.</li><li><b>O acompanhamento é seu:</b> a resposta e a marcação de visitas ficam a seu cargo.</li><li><b>Oferta Usina:</b> mensagens de resposta prontas para WhatsApp e e-mail.</li></ul></div>
  </div>
</section>

<section class="cta">
  <div class="wrap"><h2 class="h2 wide">Vamos começar por Leça, {e(nome1)}?</h2>
    <p class="lead" style="color:var(--carvao)">Responda por WhatsApp com a opção que prefere, ou marque uma conversa. Valores válidos até {VALIDADE}.</p>
    <div class="row"><a class="btn btn-dark" href="{WA}" target="_blank" rel="noopener">Aceitar por WhatsApp</a><a class="btn btn-line" href="{CAL}" target="_blank" rel="noopener">Marcar uma conversa</a><a class="btn btn-line" href="mailto:freireneto@me.com">freireneto@me.com</a></div>
    <p class="on"><i></i>Freire Neto · +351 912 988 971</p>
    <p class="note" style="color:#4A3A10">Drone sujeito às condições meteorológicas e às autorizações de voo. Os resultados dependem do mercado e do investimento em anúncios; o relatório mensal mostra os números reais, sem promessas de vendas. Assinatura das peças: Cristina Russo | CENTURY 21 Arquitectos III · AMI 23921.</p></div>
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
    for slug in V2:
        p = os.path.join(ROOT, 'proposta', slug, 'index.html')
        open(p, 'w').write(build(slug, {**CLIENTES[slug], **EXTRA.get(slug, {})}))
        print('ok', p)
