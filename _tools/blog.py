#!/usr/bin/env python3
"""Blog da Usina Vídeos (PT): usinavideos.pt/blog/ e usinavideos.pt/blog/<slug>/

Uso: python3 _tools/blog.py
Regras editoriais (herdadas do Motores e Ação):
- números só de fontes oficiais, com link; nunca valores gerados por IA;
- notas de bastidores retiradas antes de publicar; imagens IA sempre identificadas;
- clientes só com autorização; textos curtos e diretos;
- fórmula: declaração de impacto + corpo + "💡 Dica do Freire" + "Veredito Usina" + assinatura.
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_usina import CSS, COLORS, WA_SVG
from mea_banner import mea_banner, MEA_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://usinavideos.pt'
WA = 'https://wa.me/351912988971?text=Ol%C3%A1%20Freire%2C%20li%20o%20blog%20da%20Usina%20V%C3%ADdeos%20e%20gostaria%20de%20falar%20sobre%20um%20projeto.'
e = html.escape
SIG = 'Atitude fala mais alto. — Freire Neto | Usina Vídeos'

CATS = {'bastidores': 'Bastidores e making of', 'comunicacao': 'Comunicação e marketing digital',
        'mercados': 'Mercados', 'cases': 'Cases'}

POSTS = [
    dict(slug='credito-jovem-comprar-casa-sem-entrada', cat='mercados', date='2026-10-27',
         title='Crédito jovem: tem menos de 35 anos? Saiba como comprar casa sem entrada',
         desc='Garantia pública de até 15% e isenção de IMT e Imposto do Selo: quem tem direito, o que é preciso e até quando, em 2026.',
         img='/cordiallevel/anteroquental/img/aq-1.jpg', img_cap='T2 Antero de Quental, Porto · Cordial Level | CENTURY 21 Arquitectos · AMI 11414',
         lead='Para quem tem até 35 anos, a entrada deixou de ser o maior obstáculo. O Estado pode ser fiador de até 15% do valor da casa, e o banco pode financiar a compra a 100%.',
         body='''<p>São duas medidas que se somam: a <b>garantia pública</b> no crédito à habitação e a <b>isenção de IMT e Imposto do Selo</b> na compra da primeira casa. A garantia está em vigor para contratos assinados até 31 de dezembro de 2026.</p>
<h2>Como funciona a garantia pública</h2>
<p>O Estado garante ao banco até 15% do valor da compra, a parte que normalmente seria a entrada. Numa casa de 200 000 €, são 30 000 € que deixam de ter de sair do bolso. A garantia dura 10 anos a contar da assinatura do contrato.</p>
<h2>Quem tem direito</h2>
<ul><li>Entre <b>18 e 35 anos</b>, com domicílio fiscal em Portugal.</li>
<li>Rendimentos até ao <b>8.º escalão de IRS</b>.</li>
<li>Sem outra habitação em seu nome, total ou parcialmente.</li>
<li>Compra da <b>primeira habitação própria e permanente</b>, até <b>450 000 €</b>.</li>
<li>Sem dívidas às Finanças nem à Segurança Social.</li>
<li>Se forem dois compradores, ambos têm de cumprir as condições.</li></ul>
<p>A decisão final é sempre do banco, que continua a avaliar o risco e a taxa de esforço.</p>
<h2>IMT e Imposto do Selo: quanto se poupa</h2>
<table class="bt"><thead><tr><th>Valor da casa (2026)</th><th>IMT e Imposto do Selo</th></tr></thead><tbody>
<tr><td>Até 330 539 €</td><td>Isenção total</td></tr>
<tr><td>De 330 539 € a 660 982 €</td><td>Isenção parcial: paga só sobre o valor acima de 330 539 €</td></tr>
<tr><td>Acima de 660 982 €</td><td>Sem isenção</td></tr></tbody></table>
<p>Para a isenção: até 35 anos à data da escritura, não ser dependente no IRS desse ano e não ter tido casa em seu nome nos últimos três anos.</p>
<h2>O que é preciso</h2>
<ul><li>Documento de identificação e NIF.</li>
<li>Últimas declarações de IRS e recibos de vencimento.</li>
<li>Declarações de não dívida às Finanças e à Segurança Social.</li>
<li>Mapa de responsabilidades do Banco de Portugal.</li>
<li>Dados do imóvel: caderneta predial, certidão permanente e certificado energético.</li></ul>
<h2>Uma medida em crescimento</h2>
<p>Até novembro de 2025 foram assinados <b>22 933 contratos</b> com garantia pública. Em setembro de 2026 o Governo voltou a reforçar o montante da garantia em 100 milhões de euros.</p>
<p class="cap">Fontes: <a href="https://portugal.gov.pt/pt/gc24/comunicacao/noticias/garantia-publica-o-que-e-e-como-funciona" target="_blank" rel="noopener">Governo de Portugal</a> · <a href="https://www.santander.pt/salto/imt-jovem" target="_blank" rel="noopener">Santander, IMT jovem (atualizado em maio de 2026)</a> · <a href="https://observador.pt/2026/09/02/governo-reforca-em-100-milhoes-de-euros-garantia-publica-para-credito-a-habitacao-a-jovens/" target="_blank" rel="noopener">Observador, 2 set. 2026</a> · <a href="https://observador.pt/2026/01/05/mais-de-metade-da-garantia-do-estado-para-jovens-utilizada-ate-novembro/" target="_blank" rel="noopener">Observador, 5 jan. 2026</a>. Informação geral; não dispensa a confirmação junto do banco e das Finanças.</p>''',
         dica='Antes de procurar casa, peça ao banco uma simulação com a garantia pública. Saber o valor máximo aprovado poupa visitas e dá força na negociação.',
         veredito='Para quem tem até 35 anos, 2026 é a janela: garantia até ao fim do ano e impostos de compra a zero até 330 539 €.',
         cta='''<div class="clb"><img src="/cordiallevel/img/logo-cordial-level-claro.png" alt="Cordial Level" width="1156" height="754" loading="lazy">
<div><b>Gostava de saber mais sobre o tema e avaliar o seu perfil? Fale connosco!</b>
<p>Casemiro Ramos e Francisco Medeiros, consultores da Cordial Level, ajudam a preparar a compra com a garantia pública, do crédito à escritura. Tema também em breve no podcast Panorama Imobiliário PT.</p>
<div class="clr"><a href="/cordiallevel/">Ver a Cordial Level</a><a href="https://wa.me/351935101667?text=Ol%C3%A1%20Casemiro%2C%20li%20o%20artigo%20sobre%20cr%C3%A9dito%20jovem%20e%20gostava%20de%20avaliar%20o%20meu%20perfil." target="_blank" rel="noopener">Casemiro · 935 101 667</a><a href="https://wa.me/351912706395?text=Ol%C3%A1%20Francisco%2C%20li%20o%20artigo%20sobre%20cr%C3%A9dito%20jovem%20e%20gostava%20de%20avaliar%20o%20meu%20perfil." target="_blank" rel="noopener">Francisco · 912 706 395</a><a href="https://century21.pt/consultores/cramos" target="_blank" rel="noopener">century21.pt/consultores/cramos</a></div>
<small>Cordial Level | CENTURY 21 Arquitectos · AMI 11414</small></div></div>''',
         links=[('Ver os imóveis da Cordial Level', '/cordiallevel/'), ('Ver o Panorama Imobiliário PT', 'https://www.youtube.com/@CordialLevelPT')]),
    dict(slug='home-staging-antes-da-reportagem', cat='comunicacao', date='2026-10-27',
         title='Home staging: o que fazer antes da sessão de fotografia e vídeo',
         desc='Arrumação, limpeza, luz e a ajuda de proprietários, inquilinos e consultor: o checklist para fotos e vídeos de imóveis que geram contactos.',
         img='/cordiallevel/t3leca/img/leca-1.jpg',
         lead='A câmara só mostra o que lá está. Um imóvel bem preparado rende mais no ecrã do que qualquer edição.',
         body='''<p>Antes de qualquer visita, o comprador vê o imóvel nas fotografias e no vídeo. É aí que decide se marca. Por isso a preparação, o chamado <b>home staging</b>, começa antes de chegarmos com a câmara.</p>
<p>Os números vêm dos Estados Unidos, mas a lógica é a mesma cá: no relatório de 2025 da associação nacional de mediadores (NAR), <b>83%</b> dos agentes de compradores dizem que um imóvel preparado ajuda o comprador a imaginar-se lá a viver, e <b>49%</b> dos agentes de vendedores viram o tempo de venda baixar. As divisões mais preparadas são a sala, o quarto principal e a cozinha.</p>
<h2>1. Arrumar e despersonalizar</h2>
<p>Menos é mais. Guardar objetos pessoais, fotografias de família, ímanes do frigorífico, produtos à vista na casa de banho e cabos soltos. Bancadas e mesas quase vazias.</p>
<h2>2. Limpeza a fundo</h2>
<p>Vidros, espelhos, inox e torneiras apanham tudo. Camas feitas, toalhas lavadas e iguais, chão sem marcas. Arejar a casa antes da sessão.</p>
<h2>3. Luz, sempre</h2>
<p>Estores e cortinas abertos, todas as luzes acesas, lâmpadas a funcionar e da mesma cor. Marcar a sessão para a hora de melhor luz natural do imóvel.</p>
<h2>4. Pequenos arranjos</h2>
<p>Lâmpadas fundidas, puxadores soltos, manchas e torneiras a pingar. Na fotografia, um defeito pequeno parece maior.</p>
<figure class="bf"><img src="/cordiallevel/t3leca/img/leca-14.jpg" alt="Quarto preparado para a sessão, T3 em Leça da Palmeira" loading="lazy"><figcaption>Quarto preparado para a reportagem · Cordial Level | CENTURY 21 Arquitectos · AMI 11414</figcaption></figure>
<h2>5. Proprietários e inquilinos do mesmo lado</h2>
<p>Avisar com dias de antecedência, combinar o horário e explicar o que vai ser filmado. Pedir que retirem carros da entrada e da garagem, levem os animais e guardem objetos de valor. Uma casa habitada pode ficar impecável, se todos souberem o plano.</p>
<h2>6. O consultor antes e durante</h2>
<ul><li><b>Antes:</b> visita prévia, lista das divisões e dos pontos fortes, chaves, planta e acessos (garagem, arrecadação, terraço).</li>
<li><b>No dia:</b> chegar antes da equipa, abrir estores, acender luzes, dar os últimos retoques e estar pronto para aparecer no vídeo.</li></ul>
<table class="bt"><thead><tr><th>Divisão</th><th>O que preparar</th></tr></thead><tbody>
<tr><td>Sala</td><td>Sofá alinhado, almofadas, mesa livre, luz natural e artificial</td></tr>
<tr><td>Quarto</td><td>Cama feita com roupa clara, mesas de cabeceira quase vazias</td></tr>
<tr><td>Cozinha</td><td>Bancadas livres, inox limpo, nada no lava-loiça</td></tr>
<tr><td>Casa de banho</td><td>Toalhas iguais, sem produtos à vista, tampa da sanita fechada</td></tr>
<tr><td>Exterior</td><td>Varanda, jardim e entrada arrumados, sem carros à frente</td></tr></tbody></table>
<h2>O exemplo da Cordial Level</h2>
<p>Na Cordial Level, os consultores <b>Casemiro Ramos</b> e <b>Francisco Medeiros</b> chegam sempre antes ao imóvel e deixam tudo impecável: ambientes arrumados, iluminados e preparados ao pormenor. É esse cuidado com o home staging que se vê depois nas reportagens dos imóveis que anunciam.</p>
<figure class="bf"><img src="/cordiallevel/t3leca/img/leca-18.jpg" alt="Casa de banho preparada para a sessão" loading="lazy"><figcaption>Cordial Level | CENTURY 21 Arquitectos · AMI 11414</figcaption></figure>
<h2>Porque não deixar para a IA</h2>
<p>Arrumar ou limpar os ambientes depois, com inteligência artificial, parece mais fácil, mas não é:</p>
<ul><li><b>Muda as características reais do espaço</b> e cria expectativas que a visita desfaz.</li>
<li><b>Exige horas de pós-produção</b> em cada fotografia e atrasa a entrega.</li>
<li><b>Gera custos extra</b> que uma hora de arrumação evita.</li></ul>
<p>A IA fica para o que faz sentido: simulações de decoração ou de obra em imóveis vazios, sempre identificadas como tal. O resto resolve-se antes de a câmara chegar.</p>
<p class="cap">Fontes: <a href="https://www.nar.realtor/newsroom/nar-report-reveals-home-staging-boosts-sale-prices-and-reduces-time-on-market" target="_blank" rel="noopener">NAR, 2025 Profile of Home Staging</a> · <a href="https://www.imovirtual.com/noticias/imobiliario/importancia-home-staging" target="_blank" rel="noopener">Imovirtual, a importância do home staging</a></p>''',
         dica='Na véspera, envie ao proprietário ou inquilino este checklist por WhatsApp. No dia, chegue 30 minutos antes da equipa.',
         veredito='Home staging não é decoração cara. É método, limpeza e luz, e começa no consultor.',
         links=[('Ver os imóveis da Cordial Level', '/cordiallevel/'), ('Peça orçamento pelo WhatsApp', WA)]),
    dict(slug='bastidores-condominio-coral-foz', cat='bastidores', date='2026-10-27',
         title='Bastidores: como produzimos o T4+1 do Condomínio Coral, na Foz',
         desc='Fotografia, drone, vídeo com a consultora e uma página em quatro línguas: o making of de um imóvel premium na Foz do Douro.',
         img='/img/coral-fachada.jpg',
         lead='Um imóvel premium não se vende com três fotos e um texto. Precisa de ser mostrado por inteiro: por dentro, de cima e por quem o conhece.',
         body='''<p>O T4+1 do Condomínio Coral, na Foz do Douro, é uma construção nova com 236 m², quatro suítes e terraços. A consultora <b>Cheila Monteiro</b> (CENTURY 21 Arquitectos II · AMI 11414) pediu-nos tudo numa só produção.</p>
<h2>O que fizemos</h2>
<ul><li><b>Fotografia</b> de interiores e exteriores, com tratamento de cor e luz.</li>
<li><b>Drone</b> sobre a Foz, para mostrar o imóvel no território: mar, acessos e vizinhança.</li>
<li><b>Vídeo com a consultora em cena</b>, a apresentar o imóvel à câmara.</li>
<li><b>Página própria do imóvel</b> em português, inglês, espanhol e francês, com uma simulação identificada como IA.</li></ul>
<figure class="bf"><img src="/img/coral-drone.jpg" alt="Drone sobre o Condomínio Coral, Foz do Douro" loading="lazy"><figcaption>Drone Usina Vídeos · Foz do Douro</figcaption></figure>
<h2>Porque é que funciona</h2>
<p>Quem compra na Foz compara muito e muitas vezes está fora do país. O vídeo dá confiança, o drone responde à pergunta «onde fica?» e a página em quatro línguas evita o reencaminhamento de PDFs e fotos soltas.</p>
<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/XQ-kl1XxiCo?rel=0" title="Vídeo do Condomínio Coral com Cheila Monteiro" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>''',
         dica='Grave o consultor sempre no próprio imóvel e no fim do vídeo. É o rosto que o comprador vai procurar quando ligar.',
         veredito='Um briefing, uma produção, quatro entregáveis. É este o padrão que propomos para qualquer imóvel premium.',
         links=[('Ver a apresentação do Coral', '/t4coral/'), ('Ver o vídeo no YouTube', 'https://youtu.be/XQ-kl1XxiCo')]),
    dict(slug='5-regras-video-que-gera-contactos', cat='comunicacao', date='2026-10-27',
         title='5 regras para um vídeo que gera contactos',
         desc='Gancho, legendas, formatos, contacto no ecrã e resposta rápida: o que separa um vídeo bonito de um vídeo que traz clientes.',
         img='/img/foz-drone.jpg',
         lead='Um vídeo bonito não chega. O que conta é quantas pessoas falam consigo depois de o ver.',
         body='''<p>Seja um imóvel, um carro, uma loja ou um clube, as regras são as mesmas. São as que aplicamos em todas as produções da Usina.</p>
<h2>1. Ganhe os primeiros 2 segundos</h2><p>Comece pelo melhor plano ou por uma frase forte. Nas redes, quem não fica no início não chega ao fim.</p>
<h2>2. Legende tudo</h2><p>Muita gente vê vídeos sem som. Legendas grandes, fora da zona dos botões do Instagram.</p>
<h2>3. Um vídeo, vários formatos</h2>
<table class="bt"><thead><tr><th>Formato</th><th>Duração</th><th>Onde</th></tr></thead><tbody>
<tr><td>Horizontal 16:9</td><td>1 a 3 min</td><td>YouTube, site, apresentações</td></tr>
<tr><td>Vertical 9:16</td><td>15 a 45 s</td><td>Reels, Shorts, TikTok, anúncios</td></tr>
<tr><td>Quadrado 1:1</td><td>15 a 30 s</td><td>Feed e carrosséis</td></tr></tbody></table>
<h2>4. Contacto sempre no ecrã</h2><p>Nome, telefone ou WhatsApp sempre que a pessoa aparece e no fim. Quem quer ligar não deve ter de procurar.</p>
<h2>5. Responda depressa</h2><p>O vídeo traz o contacto; a resposta rápida e cordial fecha a visita, a reunião ou a venda.</p>''',
         dica='Prepare antes do lançamento três mensagens de resposta: primeiro contacto, seguimento e confirmação de visita ou reunião.',
         veredito='Produção boa é a que gera conversas. Medimos o sucesso em contactos, não em visualizações.',
         links=[('Peça orçamento pelo WhatsApp', WA)]),
    dict(slug='usina-videos-e-motores-e-acao', cat='cases', date='2026-10-27',
         title='Usina Vídeos e Motores e Ação: a mesma casa desde 2002',
         desc='A produtora e a marca de jornalismo automóvel nasceram juntas. O que uma aprende, a outra aplica.',
         img='/img/mea-toro.jpg', img_cap='Fiat Toro Ranch · imagem Fiat',
         lead='O Motores e Ação é a prova diária do que a Usina faz para os clientes: conteúdo regular, com credibilidade, que gera audiência e negócio.',
         body='''<p>A Usina Vídeos foi criada em 2002 por <b>Freire Neto</b>, o mesmo ano em que nasceu o <b>Motores e Ação</b>, marca de jornalismo automóvel com mais de 115 mil inscritos no YouTube, no Brasil e em Portugal.</p>
<h2>O que passa de um lado para o outro</h2>
<ul><li><b>Ritmo:</b> gravar uma vez e distribuir em todo o lado: vídeo longo, Reels, carrosséis e artigo.</li>
<li><b>Rigor:</b> números e preços só de fontes oficiais.</li>
<li><b>Linguagem:</b> reportagem, não publicidade. O espectador percebe a diferença.</li></ul>
<p>É este método que levamos a imobiliárias, stands, clubes, lojas e empresas.</p>''',
         dica='Escolha um formato que consiga manter todas as semanas. A regularidade constrói mais audiência do que um vídeo isolado.',
         veredito='Duas marcas, a mesma escola: comunicação feita por jornalistas, ao serviço de quem precisa de ser visto.',
         links=[('Ler o Motores e Ação', 'https://www.motoreseacao.com/?utm_source=usinavideos&utm_medium=blog&utm_campaign=usina'), ('Ver o canal no YouTube', 'https://www.youtube.com/@motoreseacao')]),
]

MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']


def data_pt(d):
    y, m, dd = d.split('-')
    return f'{int(dd)} de {MESES[int(m) - 1]} de {y}'


BLOG_CSS = '''
.bh{padding:56px 0 24px}.bh h1{font-size:clamp(32px,4.6vw,54px);line-height:1.05;margin-top:10px}
.bcats{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}.bcats span{font-size:13px;font-weight:800;padding:7px 12px;border-radius:999px;background:#fff;border:1px solid #E3DED6}
.bgrid{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));padding-bottom:72px}
.bc{display:flex;flex-direction:column;background:#fff;border:1px solid #E3DED6;border-top:5px solid var(--c);border-radius:18px;overflow:hidden;text-decoration:none;color:inherit}
.bc img{width:100%;aspect-ratio:16/9;object-fit:cover}.bc div{padding:18px 20px 22px}.bc span{font-size:12px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--c)}
.bc h3{font-size:21px;line-height:1.2;margin-top:6px;color:var(--ink)}.bc p{margin-top:8px;font-size:15px}.bc em{display:block;margin-top:12px;font-style:normal;font-size:13px;color:var(--muted)}
.art{max-width:760px;margin:0 auto;padding:44px 0 72px}.art h1{font-size:clamp(30px,4.2vw,46px);line-height:1.08;margin-top:10px}
.art .meta{margin-top:14px;font-size:14px;color:var(--muted)}.art .hero{width:100%;border-radius:18px;margin-top:26px;aspect-ratio:16/9;object-fit:cover}
.art .cap{font-size:12px;color:var(--muted);margin-top:6px}
.art .imp{margin-top:26px;font-size:21px;line-height:1.45;font-weight:700;color:var(--ink);border-left:5px solid var(--y);padding-left:18px}
.art h2{font-size:26px;margin-top:34px}.art p,.art li{font-size:18px;line-height:1.65}.art p{margin-top:14px}.art ul{margin-top:14px;padding-left:22px;display:grid;gap:8px}
.art .bf{margin:26px 0 0}.art .bf img{width:100%;border-radius:16px}.art figcaption{font-size:12px;color:var(--muted);margin-top:6px}
.art .yt{position:relative;aspect-ratio:16/9;margin-top:26px;border-radius:16px;overflow:hidden;background:#000}.art .yt iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.bt{width:100%;border-collapse:collapse;margin-top:16px;background:#fff;border-radius:12px;overflow:hidden;font-size:16px}.bt th,.bt td{padding:12px 14px;border-bottom:1px solid #E3DED6;text-align:left}.bt th{background:var(--ink);color:#fff;font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.dica{margin-top:30px;background:#FFF7E3;border:1px solid #F1D592;border-radius:16px;padding:20px 22px}.dica b{display:block;font-size:15px;color:var(--ink)}.dica p{margin-top:6px!important}
.ver{margin-top:18px;background:var(--ink);color:#E9E5E1;border-radius:16px;padding:20px 22px}.ver b{display:block;color:var(--y);font-size:13px;letter-spacing:.14em;text-transform:uppercase}.ver p{margin-top:6px!important;color:#E9E5E1}
.clb{margin-top:26px;display:grid;grid-template-columns:110px 1fr;gap:18px;align-items:center;background:#0F2438;color:#E6E1D6;border-radius:18px;padding:22px;border-bottom:5px solid #C9A45C}
.clb img{width:110px;height:auto}.clb b{display:block;color:#fff;font-size:19px;line-height:1.3}.clb p{margin-top:8px!important;font-size:16px!important;color:#D7D2C6}
.clr{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.clr a{background:#C9A45C;color:#0F2438;font-weight:800;font-size:14px;padding:9px 14px;border-radius:999px;text-decoration:none}
.clb small{display:block;margin-top:10px;font-size:12px;color:#B9B3A6}@media(max-width:560px){.clb{grid-template-columns:1fr}.clb img{width:90px}}
.sig{margin-top:26px;font-weight:800;color:var(--ink)}.blinks{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}
'''


def head(title, desc, url, img, kind, ld):
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:type" content="{kind}"><meta property="og:image" content="{BASE}{img}"><meta property="og:site_name" content="Usina Vídeos"><meta property="og:locale" content="pt_PT">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/rss+xml" title="Blog Usina Vídeos" href="{BASE}/blog/feed.xml">
<meta name="theme-color" content="#141213">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}{MEA_CSS}{BLOG_CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Menu"><div class="wrap">
  <a class="logo" href="/"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <div class="links" style="display:flex"><a href="/">Início</a><a href="/blog/">Blog</a><a href="/#trabalhos">Trabalhos</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Peça orçamento</a>
</div></nav>
'''


FOOT = f'''<footer><div class="wrap" style="display:block;margin-bottom:28px">{mea_banner('pt', 'usinavideos_blog')}</div><div class="wrap">
  <a href="/" aria-label="Usina Vídeos · página inicial"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <span>Produtora de conteúdo e comunicação · Norte e todo o Portugal · © Usina Vídeos</span>
</div></footer>
<a class="fab" href="{WA}" target="_blank" rel="noopener" aria-label="Fale connosco no WhatsApp">{WA_SVG}</a>
</body>
</html>
'''

PUB = {'@type': 'Organization', '@id': BASE + '/#usina', 'name': 'Usina Vídeos', 'logo': {'@type': 'ImageObject', 'url': BASE + '/img/logo/usina-horizontal-1200.png'}}
AUTHOR = {'@type': 'Person', 'name': 'Freire Neto', 'url': 'https://www.linkedin.com/in/freireneto/'}


def t_img(src):
    t = src.replace('.jpg', '-t.jpg')
    return t if os.path.exists(os.path.join(ROOT, t.lstrip('/'))) else src


def card(p, i):
    return (f'<a class="bc" href="/blog/{p["slug"]}/" style="--c:{COLORS[i % 3]}"><img src="{t_img(p["img"])}" alt="" loading="lazy">'
            f'<div><span>{e(CATS[p["cat"]])}</span><h3>{e(p["title"])}</h3><p>{e(p["desc"])}</p><em>{data_pt(p["date"])} · Freire Neto</em></div></a>')


def teaser():
    """Bloco com os 3 artigos mais recentes, para a página inicial."""
    ps = sorted(POSTS, key=lambda p: p['date'], reverse=True)[:3]
    return ''.join(card(p, i) for i, p in enumerate(ps))


def build():
    d = os.path.join(ROOT, 'blog'); os.makedirs(d, exist_ok=True)
    ps = sorted(POSTS, key=lambda p: p['date'], reverse=True)
    url = BASE + '/blog/'
    ld = {'@context': 'https://schema.org', '@type': 'Blog', 'url': url, 'name': 'Blog Usina Vídeos', 'inLanguage': 'pt-PT', 'publisher': PUB,
          'blogPost': [{'@type': 'BlogPosting', 'headline': p['title'], 'url': f'{BASE}/blog/{p["slug"]}/', 'datePublished': p['date']} for p in ps]}
    cats = ''.join(f'<span>{e(v)}</span>' for v in CATS.values())
    open(os.path.join(d, 'index.html'), 'w').write(head('Blog · Usina Vídeos', 'Bastidores, comunicação e marketing digital, mercados e cases da Usina Vídeos, produtora de conteúdo e comunicação.', url, '/img/foz-drone.jpg', 'website', ld) + f'''
<header class="bh"><div class="wrap"><span class="eb">Blog Usina Vídeos</span><h1>Bastidores, ideias e mercados.</h1>
  <p class="lead">O que fazemos, como fazemos e o que está a mudar nos setores com que trabalhamos.</p><div class="bcats">{cats}</div></div></header>
<main class="wrap bgrid">{''.join(card(p, i) for i, p in enumerate(ps))}</main>
''' + FOOT)
    for p in ps:
        u = f'{BASE}/blog/{p["slug"]}/'
        ld = {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': p['title'], 'description': p['desc'], 'image': BASE + p['img'],
              'datePublished': p['date'], 'dateModified': p['date'], 'author': AUTHOR, 'publisher': PUB, 'mainEntityOfPage': u, 'inLanguage': 'pt-PT',
              'articleSection': CATS[p['cat']]}
        links = ''.join(f'<a class="btn {"y" if j == 0 else "o"}" href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}>{e(t)}</a>' for j, (t, h) in enumerate(p['links']))
        cap = f'<p class="cap">{e(p["img_cap"])}</p>' if p.get('img_cap') else ''
        os.makedirs(os.path.join(d, p['slug']), exist_ok=True)
        open(os.path.join(d, p['slug'], 'index.html'), 'w').write(head(p['title'] + ' · Usina Vídeos', p['desc'], u, p['img'], 'article', ld) + f'''
<main class="wrap"><article class="art">
  <span class="eb">{e(CATS[p['cat']])}</span><h1>{e(p['title'])}</h1>
  <p class="meta">{data_pt(p['date'])} · por <a href="https://www.linkedin.com/in/freireneto/" target="_blank" rel="noopener">Freire Neto</a></p>
  <img class="hero" src="{p['img']}" srcset="{t_img(p['img'])} 900w, {p['img']} 1920w" sizes="(max-width: 800px) 100vw, 760px" alt="" fetchpriority="high">{cap}
  <p class="imp">{e(p['lead'])}</p>
  {p['body']}
  <div class="dica"><b>💡 Dica do Freire</b><p>{e(p['dica'])}</p></div>
  <div class="ver"><b>Veredito Usina</b><p>{e(p['veredito'])}</p></div>
  <p class="sig">{e(SIG)}</p>
  {p.get('cta', '')}
  <div class="blinks">{links}<a class="btn o" href="/blog/">Mais artigos</a></div>
</article></main>
''' + FOOT)
    items = ''.join(f'<item><title>{e(p["title"])}</title><link>{BASE}/blog/{p["slug"]}/</link><guid>{BASE}/blog/{p["slug"]}/</guid><description>{e(p["desc"])}</description></item>' for p in ps)
    open(os.path.join(d, 'feed.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Blog Usina Vídeos</title><link>{BASE}/blog/</link><description>Bastidores, comunicação e marketing digital, mercados e cases.</description><language>pt-PT</language>{items}</channel></rss>\n')
    print('ok blog', len(ps), 'artigos')


if __name__ == '__main__':
    build()
