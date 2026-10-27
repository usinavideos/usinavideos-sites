#!/usr/bin/env python3
"""Rascunho de proposta para a Yellow Rules (Viana do Castelo): usinavideos.pt/proposta/yellow-rules/

Página não indexada, para conversa. Preços dos pacotes só depois da reunião.
Uso: python3 _tools/proposta_yellow.py
"""
import html, os, sys, urllib.parse as up
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_usina import CSS, WA_SVG, STRIPE, COLORS
from mea_banner import mea_banner, MEA_CSS
from proposta import EXTRA_CSS, EDICAO, CAL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
WA = 'https://wa.me/351912988971?text=' + up.quote('Olá Freire, vi a proposta da Usina Vídeos para a Yellow Rules e gostava de conversar.')

FORCAS = [('25+ anos', 'no setor das duas rodas, da Revista Pró Moto à Yellow Rules'),
          ('15+ marcas', 'de peças e equipamento off-road, em Portugal e Espanha'),
          ('Jeca Joia', 'um canal com rosto, sotaque e histórias próprias'),
          ('Na estrada', 'visitas a lojistas e presença nos eventos e provas')]

MES = [('Semana 1', 'Teste de produto no YouTube', 'Reel do produto · Dica de montagem · Bastidores'),
       ('Semana 2', 'Jeca na loja: visita a um lojista', 'Reel da visita · Produto em 30 s · Humor do Jeca'),
       ('Semana 3', 'Comparativo ou «erro comum»', 'Reel do comparativo · Dica de manutenção · Bastidores'),
       ('Semana 4', 'Jeca Joia Show (entrevista)', 'Corte da entrevista · Produto em 30 s · Convite para o próximo mês')]

VENDAS = [('Jeca na loja', 'As visitas aos lojistas viram vídeo: publicidade para quem revende e motivo para comprar mais à Yellow Rules.'),
          ('Código por vídeo', 'Um código de desconto da 2r4.eu em cada vídeo (ex.: JECA10). Mede quanto cada conteúdo vende.'),
          ('Link direto', 'Cada vídeo e cada Reel levam à página do produto na 2r4.eu, sem passos a mais.'),
          ('Anúncios', 'Os Reels que funcionam melhor passam a anúncio para motociclistas off-road em Portugal e Espanha, com legendas em espanhol.'),
          ('Catálogo em vídeo', 'Um vídeo curto por marca para enviar por WhatsApp aos lojistas.'),
          ('Montagens', 'Tutoriais de montagem e «erros comuns»: vídeos que se pesquisam e vendem durante anos.')]

AUTORIDADE = [('Testes sinceros', 'Sempre a mesma fórmula: problema, produto, teste no terreno e veredito.'),
              ('Comparativos', 'Produtos e marcas lado a lado, com o olhar de quem pilota.'),
              ('A história', 'Da maior revista off-road do Brasil a importador em Portugal: um episódio e um texto para o site.'),
              ('Eventos e provas', 'Cobertura com drone e entrevistas nas provas onde o Renato já está.'),
              ('Motores e Ação', 'Episódio conjunto e divulgação cruzada com o canal de jornalismo automóvel da Usina, desde 2002.')]

OPCOES = [('Para começar', 'Arranque', ['1 dia de gravação em Viana do Castelo', '1 vídeo para o YouTube (até 10 min)', '4 Reels verticais com legendas', 'Fotografias de produto para a 2r4.eu e redes'], 'Um mês de teste para conhecer o método e medir resultados.'),
          ('Recomendado', 'Mensal', ['1 dia de gravação por mês', '4 vídeos para o YouTube (1 por semana)', '12 Reels (3 por semana)', 'Fotografias de produto', 'Calendário e textos prontos para a Michelle publicar'], 'Conteúdo novo todas as semanas, gravado num só dia.'),
          ('Crescimento', 'Completo', ['Tudo do pacote Mensal', 'Jeca Joia Show: gravação e edição de 1 episódio', 'Gestão de anúncios na Meta (investimento à parte)', 'Relatório mensal com visualizações, cliques e vendas'], 'Para acelerar vendas e autoridade a partir do 2.º ou 3.º mês.')]


def build():
    forcas = ''.join(f'<div><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in FORCAS)
    mes = ''.join(f'<tr><td><b>{e(a)}</b></td><td>{e(b)}</td><td>{e(c)}</td></tr>' for a, b, c in MES)
    vendas = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b) in enumerate(VENDAS))
    aut = ''.join(f'<article class="card" style="--c:{COLORS[(i + 1) % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b) in enumerate(AUTORIDADE))
    ops = ''.join(f'<article class="{"ref" if i == 1 else ""}" style="--c:{COLORS[i % 3]}"><span class="lb">{e(lb)}</span><h3>{e(n)}</h3><div class="pr" style="font-size:26px">Sob orçamento</div><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul><p>{e(d)}</p></article>' for i, (lb, n, items, d) in enumerate(OPCOES))
    ed = ''.join(f'<tr><td>{e(n)}</td><td>{p} + IVA</td><td>{e(d)}</td></tr>' for n, p, d in EDICAO)
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Proposta para a Yellow Rules · Usina Vídeos</title>
<meta name="description" content="Conteúdo semanal para a Yellow Rules e o Jeca Joia: um dia de gravação por mês em Viana do Castelo.">
<meta name="robots" content="noindex, follow">
<meta name="theme-color" content="#141213">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}{MEA_CSS}{EXTRA_CSS}
.yhero{{background:#141213;color:#fff;padding:96px 0 64px;border-bottom:6px solid #F2C200}}.yhero h1{{font-size:clamp(34px,5.4vw,64px);line-height:1.04;margin-top:12px;color:#fff;max-width:18ch}}
.yhero p{{margin-top:18px;font-size:19px;line-height:1.55;color:#D6D1CD;max-width:62ch}}.yhero .eb{{color:#F2C200}}
.ytab{{width:100%;border-collapse:collapse;background:#fff;border-radius:14px;overflow:hidden;font-size:15px;min-width:560px}}.ytab th,.ytab td{{padding:13px 15px;border-bottom:1px solid #E3DED6;text-align:left;vertical-align:top}}.ytab th{{background:var(--ink);color:#fff;font-size:12px;letter-spacing:.08em;text-transform:uppercase}}
.ystats b{{font-size:clamp(19px,5.2vw,28px)!important;word-break:break-word}}
.draft{{display:inline-block;margin-top:18px;background:#F2C200;color:#141213;font-weight:900;font-size:13px;letter-spacing:.08em;text-transform:uppercase;padding:6px 12px;border-radius:999px}}
</style>
</head>
<body>
<nav class="nav" aria-label="Menu"><div class="wrap">
  <a class="logo" href="/"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <div class="links"><a href="#modelo">O modelo</a><a href="#vendas">Vendas</a><a href="#autoridade">Autoridade</a><a href="#opcoes">Como começar</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Conversar</a>
</div></nav>

<header class="yhero"><div class="wrap">
  <span class="eb">Proposta para a Yellow Rules · Viana do Castelo</span>
  <h1>Conteúdo todas as semanas, gravado num dia por mês.</h1>
  <p>Para o Renato e a Michelle Furmann. A Yellow Rules já tem o mais difícil: experiência, marcas fortes e um rosto que as pessoas querem ver. A Usina Vídeos junta-lhe produção profissional e regularidade, para gerar mais vendas na 2r4.eu, mais lojistas e mais autoridade para o Jeca Joia.</p>
  <span class="draft">Rascunho para a primeira conversa</span>
  {STRIPE}
</div></header>

<section>
  <div class="wrap two">
    <div><span class="eb">O que já têm</span><h2>Uma marca com história e com rosto.</h2>
      <p style="margin-top:18px">A nossa proposta é somar a este trabalho: transformar o dia a dia do Renato (testes, visitas a lojistas, provas) em ainda mais conteúdo, publicado todas as semanas e sempre com um caminho para a venda.</p></div>
    <div class="stats">{forcas}</div>
  </div>
</section>

<section id="modelo" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">O modelo</span><h2>Um dia em Viana, um mês de conteúdo.</h2>
    <p class="lead">Uma vez por mês vamos a Viana do Castelo e gravamos tudo num dia: testes, visitas, entrevista e fotografias. Depois editamos e entregamos o mês pronto a publicar.</p>
    <div style="overflow-x:auto;margin-top:26px;border-radius:14px"><table class="ytab"><thead><tr><th>Semana</th><th>YouTube</th><th>Instagram e Facebook</th></tr></thead><tbody>{mes}</tbody></table></div>
    <p class="note">Exemplo de calendário. Os temas escolhem-se convosco, de acordo com as marcas e as campanhas de cada mês.</p></div>
</section>

<section id="vendas">
  <div class="wrap"><span class="eb">Ideias para vender mais</span><h2>Cada vídeo com um caminho para a venda.</h2>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">{vendas}</div></div>
</section>

<section id="autoridade" style="background:var(--paper2)">
  <div class="wrap"><span class="eb">Ideias para autoridade</span><h2>Quem testa e explica, vende com confiança.</h2>
    <div class="grid3" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">{aut}</div></div>
</section>

<section>
  <div class="wrap two">
    <div><span class="eb">Com a Michelle</span><h2>Nós produzimos, a Michelle publica.</h2>
      <p style="margin-top:18px">A gestão das redes continua com quem conhece a marca e a comunidade. A Usina entrega os vídeos editados em todos os formatos, as fotografias, o calendário e os textos de cada publicação. Se for útil, também podemos publicar e gerir os anúncios.</p></div>
    <div class="stats ystats"><div><b>Horizontal</b><span>YouTube e site</span></div><div><b>Vertical</b><span>Reels, Shorts, TikTok</span></div><div><b>PT · ES</b><span>legendas para Portugal e Espanha</span></div><div><b>Relatório</b><span>vendas e alcance todos os meses</span></div></div>
  </div>
</section>

<section id="opcoes">
  <div class="wrap"><span class="eb">Como começar</span><h2>Começar pequeno, crescer com resultados.</h2>
    <p class="lead">Três formas de trabalhar juntos. Os valores fecham-se depois da nossa conversa, à medida do que for mais útil para a Yellow Rules.</p>
    <div class="pk">{ops}</div>
    <h3 style="margin-top:40px;font-size:22px">Tabela de edição de referência</h3>
    <div style="overflow-x:auto;margin-top:14px;border-radius:14px"><table class="ytab"><thead><tr><th>Formato</th><th>Valor</th><th>Para quê</th></tr></thead><tbody>{ed}</tbody></table></div>
    <p class="note">Valores sem IVA. A gravação e a deslocação a Viana do Castelo são orçamentadas no pacote. Num contrato mensal, o valor fechado fica abaixo da soma da tabela.</p></div>
</section>

<section class="dark">
  <div class="wrap two">
    <div><span class="eb">Quem somos</span><h2>Freire Neto e Sandra Freire</h2>
      <p style="margin-top:14px">A Usina Vídeos foi criada em 2002 por Freire Neto, jornalista desde 1997 e fundador do Motores e Ação, canal de jornalismo automóvel com mais de 115 mil inscritos no YouTube. Sandra Freire assegura a edição, a produção e a administração, com 20 anos de televisão e produtoras.</p>
      <div class="row" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:22px"><a class="btn y" href="{WA}" target="_blank" rel="noopener">{WA_SVG}WhatsApp +351 912 988 971</a><a class="btn o" style="color:#fff" href="{CAL}" target="_blank" rel="noopener">Marcar conversa online</a></div></div>
    <div class="stats"><a href="https://www.motoreseacao.com/?utm_source=usinavideos&amp;utm_medium=proposta&amp;utm_campaign=yellowrules" target="_blank" rel="noopener" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Motores e Ação</b><span>jornalismo automóvel desde 2002 →</span></a><a href="/" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Usina Vídeos</b><span>trabalhos e serviços →</span></a><a href="/blog/" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>Blog</b><span>bastidores e ideias →</span></a><a href="https://www.youtube.com/@motoreseacao" target="_blank" rel="noopener" style="display:block;background:var(--ink);padding:22px 20px;text-decoration:none"><b>YouTube</b><span>@motoreseacao →</span></a></div>
  </div>
</section>

<footer><div class="wrap" style="display:block;margin-bottom:28px">{mea_banner('pt', 'proposta_yellowrules')}</div><div class="wrap">
  <a href="/" aria-label="Usina Vídeos · página inicial"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <span>Produtora de conteúdo e comunicação · © Usina Vídeos</span>
</div></footer>
</body>
</html>
'''


if __name__ == '__main__':
    d = os.path.join(ROOT, 'proposta', 'yellow-rules')
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(build())
    print('ok proposta yellow-rules')
