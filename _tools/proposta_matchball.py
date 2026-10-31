#!/usr/bin/env python3
"""Proposta para a MatchBall (João Silva): usinavideos.pt/proposta/matchball/

Highlights e entrevistas dos atletas da MatchBall que jogam em Portugal. Página não indexada, com preços.
Uso: python3 _tools/proposta_matchball.py
"""
import html, os, sys, urllib.parse as up
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_usina import CSS, WA_SVG, STRIPE, COLORS, ig_embed
from mea_banner import mea_banner, MEA_CSS
from proposta import EXTRA_CSS, CAL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
WA = 'https://wa.me/351912988971?text=' + up.quote('Olá Freire, vi a proposta da Usina Vídeos para a MatchBall e gostava de avançar.')
HERO = 'https://i.ytimg.com/vi/W928uxPDX6U/maxresdefault.jpg'

FEITO = [('Tour Red Rose Thunder', 'Jogos, destaques e perfis dos jogadores durante o tour internacional em Portugal.'),
         ('Showcase do Porto', 'Jogos do MatchBall Women\'s Showcase contra equipas portuguesas.'),
         ('CDJ Régio · Vila do Conde', 'Cobertura semanal de jogos de basquetebol, com destaques no YouTube e no Instagram.')]

IDEIAS = [('Highlights por jogo', 'Os melhores lances de cada atleta, em vertical para Reels e TikTok e em horizontal para YouTube e clubes. Entrega em 48 horas.'),
          ('Entrevista pós-jogo', 'Dois a três minutos com o atleta no pavilhão: o jogo, a adaptação a Portugal e os objetivos. Legendada em PT e EN.'),
          ('Welcome to Portugal', 'Vídeo de chegada: o atleta na cidade, no pavilhão e com o clube. Ideal para anunciar novas contratações.'),
          ('Overseas diary', 'A vida do atleta em Portugal: casa, treino, cidade e comida. O formato que mais atrai novos jogadores para a MatchBall.'),
          ('Mixtape da época', 'Uma compilação dos melhores lances de vários jogos do atleta, a meio e no fim da época. É o vídeo que se envia a clubes e scouts para o próximo contrato.'),
          ('Perfil do atleta no site', 'Uma página por atleta em usinavideos.pt, com vídeos, dados, clube e contacto da MatchBall, para enviar por link a scouts e clubes.'),
          ('Web stories', 'Uma história em ecrã inteiro por jogo ou por atleta, que aparece no Google e no site.'),
          ('Showcases e tours', 'Cobertura completa dos showcases em Portugal: jogos, sessões de scouting, entrevistas e perfis.')]

PRECOS = [('Highlights de 1 atleta', '60€', 'por jogo', 'Captação do jogo, vídeo de 45 a 90 s em vertical e horizontal, legendas PT e EN'),
          ('Atleta adicional no mesmo jogo', '30€', 'por atleta', 'Mesmo jogo, mais um vídeo de highlights'),
          ('Entrevista pós-jogo', '20€', 'com highlights', 'Entrevista de 2 a 3 min editada e legendada, mais um corte vertical. Isolada: 50€'),
          ('Welcome to Portugal / Overseas diary', '90€', 'por vídeo', 'Gravação no dia a dia do atleta e edição de 1 a 2 min'),
          ('Mixtape da época', '80€', 'por atleta', 'Montagem com os melhores lances de vários jogos'),
          ('Perfil do atleta no site', '50€', 'por atleta', 'Página com vídeos, dados e contactos, mais a web story; atualizações incluídas na época'),
          ('Showcase ou tour', 'desde 350€', 'por dia', 'Jogos, sessões de treino, entrevistas e perfis de vários atletas'),
          ('Deslocação', 'sem custo', 'Grande Porto', 'Porto, Gaia, Gondomar, Maia, Matosinhos, Vila do Conde e Póvoa de Varzim. Fora desta zona: 25€ a cada 100 km, e vários atletas na mesma deslocação pagam uma só.')]

PACOTES = [('Por pedido', '1 a 3 vídeos no mês', '80€', ['Highlights + entrevista, por jogo', 'Só highlights: 60€', 'Legendas PT e EN', 'Entrega em 48 horas'], 'Para pedidos pontuais: um atleta, um jogo.'),
           ('Mais pedido', '4 a 7 vídeos no mês', '75€', ['Highlights + entrevista, por jogo', 'Só highlights: 55€', 'Pode ser 1 vídeo por atleta, de vários atletas', 'Web story de cada jogo incluída'], 'Por exemplo: um vídeo por mês de cada atleta em Portugal.'),
           ('Volume', '8 ou mais vídeos no mês', '70€', ['Highlights + entrevista, por jogo', 'Só highlights: 50€', 'Calendário fechado no início do mês', 'Web story de cada jogo incluída'], 'Para cobrir a carteira de atletas em Portugal.')]

GAL = [('W928uxPDX6U', 'CDJ Régio 78–74 Beira-Mar'), ('YHqB45YwLjc', 'CDJ Régio 75–73 Benfica OA'), ('wd4Ms8ICggc', 'CDJ Régio × GDB Leça'), ('0zziUdQ3Mw0', 'CDJ Régio × CPN · feminino')]

STEPS = [('Calendário', 'A MatchBall indica os atletas e os jogos do mês. Nós organizamos as deslocações.'),
         ('Captação', 'Gravamos o jogo inteiro e, no fim, a entrevista no pavilhão, com autorização do clube.'),
         ('Edição', 'Highlights e entrevista editados com a marca MatchBall, música licenciada e legendas PT e EN.'),
         ('Entrega', 'Em 48 horas, por link, nos formatos de cada rede. O jogo completo fica guardado para scouting.')]


def build():
    feito = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b) in enumerate(FEITO))
    ideias = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b) in enumerate(IDEIAS))
    precos = ''.join(f'<tr><td><b>{e(n)}</b></td><td style="white-space:nowrap"><b>{e(p)}</b>{" + IVA" if "€" in p else ""}<br><small>{e(u)}</small></td><td>{e(d)}</td></tr>' for n, p, u, d in PRECOS)
    pk = ''.join(f'<article class="{"ref" if i == 1 else ""}" style="--c:{COLORS[i % 3]}"><span class="lb">{e(lb)}</span><h3>{e(n)}</h3><div class="pr">{e(p)}{"<small>+ IVA</small>" if "€" in p else ""}</div><ul>{"".join(f"<li>{e(x)}</li>" for x in it)}</ul><p>{e(d)}</p></article>' for i, (lb, n, p, it, d) in enumerate(PACOTES))
    gal = ''.join(f'<a href="https://www.youtube.com/watch?v={v}" target="_blank" rel="noopener"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="{e(t)}" loading="lazy"><span>{e(t)} ▶</span></a>' for v, t in GAL)
    steps = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b) in enumerate(STEPS))
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Proposta para a MatchBall · Usina Vídeos</title>
<meta name="description" content="Highlights, entrevistas e perfis dos atletas da MatchBall que jogam em Portugal, com legendas em português e inglês.">
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
.mtab{{width:100%;border-collapse:collapse;background:#fff;border-radius:14px;overflow:hidden;font-size:15px;min-width:600px}}.mtab th,.mtab td{{padding:13px 15px;border-bottom:1px solid #E3DED6;text-align:left;vertical-align:top}}.mtab th{{background:var(--ink);color:#fff;font-size:12px;letter-spacing:.08em;text-transform:uppercase}}.mtab small{{color:var(--muted);font-weight:700}}
@media(max-width:640px){{.mtab{{min-width:0}}.mtab thead{{display:none}}.mtab tr{{display:block;border-bottom:1px solid #E3DED6;padding:14px 16px}}.mtab td{{display:block;border:0;padding:2px 0}}.mtab td:first-child{{font-size:17px}}}}
.igrow{{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));margin-top:30px;align-items:start}}
.mst b{{font-size:clamp(19px,5.2vw,28px)!important}}
.mgal{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:26px}}.mgal a{{position:relative;display:block;border-radius:14px;overflow:hidden;aspect-ratio:16/9;background:#222}}.mgal img{{width:100%;height:100%;object-fit:cover}}.mgal span{{position:absolute;left:0;right:0;bottom:0;padding:22px 14px 10px;background:linear-gradient(transparent,rgba(0,0,0,.8));color:#fff;font-weight:800;font-size:14px}}
</style>
</head>
<body>
<nav class="nav" aria-label="Menu"><div class="wrap">
  <a class="logo" href="/"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <div class="links"><a href="#feito">Já fizemos</a><a href="#ideias">Ideias</a><a href="#precos">Preços</a><a href="#pacotes">Quantidade</a><a href="#como">Como funciona</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Avançar</a>
</div></nav>

<header class="mhero"><div class="wrap">
  <span class="eb">Proposta para a MatchBall · João Silva</span>
  <h1>Os vossos atletas em Portugal, em vídeo, todas as semanas.</h1>
  <p>Highlights, entrevistas e perfis dos jogadores da MatchBall nos clubes portugueses, com legendas em português e inglês. Conteúdo para as redes da MatchBall, para os atletas e para apresentar a clubes e scouts.</p>
  {STRIPE}
</div></header>

<section>
  <div class="wrap two">
    <div><span class="eb">Porquê</span><h2>Cada jogo em Portugal é uma montra para o próximo contrato.</h2>
      <p style="margin-top:18px">Os atletas que a MatchBall coloca em Portugal precisam de mostrar o que valem em cada jornada. Com vídeo regular, a MatchBall prova o seu trabalho a novos jogadores, os atletas ganham material para a carreira e os clubes ganham visibilidade.</p></div>
    <div class="stats mst"><div><b>48 h</b><span>entrega dos highlights</span></div><div><b>PT · EN</b><span>legendas em todos os vídeos</span></div><div><b>9:16 · 16:9</b><span>vertical e horizontal</span></div><div><b>Norte e Centro</b><span>Póvoa, Porto, Aveiro e mais</span></div></div>
  </div>
</section>

<section id="feito" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">O que já fizemos juntos</span><h2>Já conhecemos o pavilhão e os atletas.</h2>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">{feito}</div>
    <div class="igrow">{ig_embed('DYvUDd_xY2d')}{ig_embed('DY-qXG4M95k')}{ig_embed('DY-tmeisiO0')}</div>
    <div class="mgal">{gal}</div>
    <p class="note" style="margin-top:18px">Mais jogos em <a href="/cdjregio/">usinavideos.pt/cdjregio</a>.</p></div>
</section>

<section id="ideias">
  <div class="wrap"><span class="eb">Ideias</span><h2>Mais do que highlights.</h2>
    <p class="lead">Formatos pensados para os dois públicos da MatchBall: jogadores que querem jogar na Europa e clubes que procuram reforços.</p>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">{ideias}</div></div>
</section>

<section id="precos" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">Preços</span><h2>Preços por serviço.</h2>
    <p class="lead">Valores sem IVA, que acresce à taxa legal em vigor. Legendas em português e inglês incluídas; espanhol + 15€ por vídeo.</p>
    <div style="overflow-x:auto;margin-top:26px;border-radius:14px"><table class="mtab"><thead><tr><th>Serviço</th><th>Preço</th><th>O que inclui</th></tr></thead><tbody>{precos}</tbody></table></div></div>
</section>

<section id="pacotes">
  <div class="wrap"><span class="eb">Preço por quantidade</span><h2>Quanto mais vídeos no mês, menor o preço.</h2>
    <div class="pk">{pk}</div>
    <p class="note" style="margin-top:18px">O preço por vídeo baixa com a quantidade pedida no mês, somando todos os atletas. Sem pacote fixo nem fidelização: a MatchBall pede o que precisar. Sem custo de deslocação no Grande Porto (Porto, Gaia, Gondomar, Maia, Matosinhos, Vila do Conde e Póvoa); fora dessa zona, 25€ a cada 100 km.</p></div>
</section>

<section id="como" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">Como funciona</span><h2>Do calendário ao vídeo publicado.</h2>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">{steps}</div>
    <p class="note" style="margin-top:18px">A gravação e as entrevistas dependem da autorização de cada clube e do pavilhão. Os direitos de imagem dos atletas ficam a cargo da MatchBall.</p></div>
</section>

<section class="dark">
  <div class="wrap two">
    <div><span class="eb">Quem somos</span><h2>Freire Neto e Sandra Freire</h2>
      <p style="margin-top:14px">A Usina Vídeos foi criada em 2002 por Freire Neto, jornalista desde 1997 e fundador do Motores e Ação. Sandra Freire assegura a edição, a produção e a administração, com 20 anos de televisão e produtoras. No basquetebol, cobrimos o CDJ Régio e os eventos da MatchBall em Portugal.</p>
      <div class="row" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:22px"><a class="btn y" href="{WA}" target="_blank" rel="noopener">{WA_SVG}WhatsApp +351 912 988 971</a><a class="btn o" style="color:#fff" href="{CAL}" target="_blank" rel="noopener">Marcar conversa online</a></div></div>
    <div class="stats"><a href="/cdjregio/" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>CDJRegio</b><span>jogos e highlights →</span></a><a href="https://www.instagram.com/usina.videos/" target="_blank" rel="noopener" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Instagram</b><span>@usina.videos →</span></a><a href="https://www.youtube.com/@DicasdoFreire" target="_blank" rel="noopener" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>YouTube</b><span>highlights →</span></a><a href="/" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Usina Vídeos</b><span>trabalhos e serviços →</span></a></div>
  </div>
</section>

<footer><div class="wrap" style="display:block;margin-bottom:28px">{mea_banner('pt', 'proposta_matchball')}</div><div class="wrap">
  <a href="/" aria-label="Usina Vídeos · página inicial"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <span>Produtora de conteúdo e comunicação · © Usina Vídeos</span>
</div></footer>
<script async src="https://www.instagram.com/embed.js"></script>
</body>
</html>
'''


if __name__ == '__main__':
    d = os.path.join(ROOT, 'proposta', 'matchball')
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(build())
    print('ok proposta matchball')
