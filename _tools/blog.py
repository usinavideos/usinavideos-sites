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
from social_banner import social_banner, SOCIAL_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://usinavideos.pt'
WA = 'https://wa.me/351912988971?text=Ol%C3%A1%20Freire%2C%20li%20o%20blog%20da%20Usina%20V%C3%ADdeos%20e%20gostaria%20de%20falar%20sobre%20um%20projeto.'
e = html.escape
SIG = 'Atitude fala mais alto. — Freire Neto | Usina Vídeos'

CATS = {'bastidores': 'Bastidores e making of', 'comunicacao': 'Comunicação e marketing digital',
        'mercados': 'Mercados', 'cases': 'Cases'}

POSTS = [
    dict(slug='casas-mais-caras-que-rendimentos-portugal-eurostat', cat='mercados', date='2026-11-10',
         title='Casas 60,8% mais caras face aos rendimentos: o que o dado do Eurostat significa para quem compra e para quem vende',
         desc='Entre 2015 e 2025, o rácio entre o preço das casas e os rendimentos subiu 60,8% em Portugal, a maior subida da UE (média: 6,8%). O comentário do Panorama Imobiliário.',
         img='/img/blog/racio-casas-rendimentos.jpg', img_cap='Leça da Palmeira, Matosinhos · drone Usina Vídeos',
         lead='Em dez anos, as casas em Portugal ficaram muito mais caras do que os salários conseguiram acompanhar. Segundo o Eurostat, nenhum outro país da União Europeia viu essa distância crescer tanto.',
         body='''<p>Os dados foram divulgados a 9 de novembro pelo <b>Eurostat</b>. O indicador compara a evolução do preço das casas com a do rendimento disponível das famílias por pessoa. Entre <b>2015 e 2025</b>, esse rácio subiu <b>60,8% em Portugal</b>. Na média da União Europeia, a subida foi de <b>6,8%</b>, quase nove vezes menos.</p>
<h2>Portugal à frente de todos</h2>
<figure class="bf" style="background:#fff;border:1px solid #E3DED6;border-radius:16px;padding:16px"><svg viewBox="0 0 520 380" width="100%" role="img" aria-label="Variação do rácio entre preço das casas e rendimentos, 2015 a 2025, Eurostat" style="font-family:Mulish,system-ui,sans-serif;max-width:620px;display:block;margin:0 auto"><line x1="250" y1="4" x2="250" y2="374" stroke="#A9A3A0"/><text x="240" y="31" text-anchor="end" font-size="19" font-weight="800" fill="#3B3634">Portugal</text><text x="434.3" y="31" font-size="19" font-weight="800" fill="#3B3634">+60,8%</text><rect x="250.0" y="12" width="176.3" height="26" rx="4" fill="#B8962E"/><text x="240" y="71" text-anchor="end" font-size="19" font-weight="400" fill="#3B3634">Países Baixos</text><text x="357.5" y="71" font-size="19" font-weight="800" fill="#3B3634">+34,3%</text><rect x="250.0" y="52" width="99.5" height="26" rx="4" fill="#8FA3BF"/><text x="240" y="111" text-anchor="end" font-size="19" font-weight="400" fill="#3B3634">Hungria</text><text x="334.9" y="111" font-size="19" font-weight="800" fill="#3B3634">+26,5%</text><rect x="250.0" y="92" width="76.8" height="26" rx="4" fill="#8FA3BF"/><text x="240" y="151" text-anchor="end" font-size="19" font-weight="400" fill="#3B3634">Chéquia</text><text x="332.8" y="151" font-size="19" font-weight="800" fill="#3B3634">+25,8%</text><rect x="250.0" y="132" width="74.8" height="26" rx="4" fill="#8FA3BF"/><text x="240" y="191" text-anchor="end" font-size="19" font-weight="400" fill="#3B3634">Espanha</text><text x="329.1" y="191" font-size="19" font-weight="800" fill="#3B3634">+24,5%</text><rect x="250.0" y="172" width="71.0" height="26" rx="4" fill="#8FA3BF"/><text x="240" y="231" text-anchor="end" font-size="19" font-weight="800" fill="#3B3634">Média UE-27</text><text x="277.7" y="231" font-size="19" font-weight="800" fill="#3B3634">+6,8%</text><rect x="250.0" y="212" width="19.7" height="26" rx="4" fill="#1B3A6B"/><text x="260" y="271" font-size="19" fill="#3B3634">Bulgária</text><text x="195.0" y="271" text-anchor="end" font-size="19" font-weight="800" fill="#3B3634">−16,2%</text><rect x="203.0" y="252" width="47.0" height="26" rx="4" fill="#C9D2DE"/><text x="260" y="311" font-size="19" fill="#3B3634">Finlândia</text><text x="168.9" y="311" text-anchor="end" font-size="19" font-weight="800" fill="#3B3634">−25,2%</text><rect x="176.9" y="292" width="73.1" height="26" rx="4" fill="#C9D2DE"/><text x="260" y="351" font-size="19" fill="#3B3634">Roménia</text><text x="117.9" y="351" text-anchor="end" font-size="19" font-weight="800" fill="#3B3634">−42,8%</text><rect x="125.9" y="332" width="124.1" height="26" rx="4" fill="#C9D2DE"/></svg><figcaption>Variação do rácio entre o preço das casas e o rendimento das famílias, 2015–2025 · Eurostat</figcaption></figure>
<p>O rácio subiu em 17 países e desceu em 10. Atrás de Portugal ficam os Países Baixos (+34,3%), a Hungria (+26,5%), a Chéquia (+25,8%) e Espanha (+24,5%). No sentido contrário, a Roménia (−42,8%), a Finlândia (−25,2%) e a Bulgária (−16,2%) viram os rendimentos crescer mais depressa do que as casas.</p>
<h2>2025: o fosso voltou a abrir</h2>
<p>Depois de um ligeiro alívio em 2024 (−0,5%), o rácio português voltou a subir <b>12,1% em 2025</b>, contra 1,9% na média europeia. Face à média histórica desde 2000, Portugal está quase <b>37% acima</b>; a UE está praticamente na média.</p>
<table class="bt"><thead><tr><th>Indicador</th><th>Portugal</th><th>UE-27</th></tr></thead><tbody>
<tr><td>Variação 2015–2025</td><td>+60,8%</td><td>+6,8%</td></tr>
<tr><td>Variação em 2025</td><td>+12,1%</td><td>+1,9%</td></tr>
<tr><td>Face à média histórica (desde 2000)</td><td>≈ +37%</td><td>≈ 0%</td></tr></tbody></table>
<h2>O que o número diz, e o que não diz</h2>
<p>O próprio Eurostat avisa: este indicador mostra a <b>evolução</b>, não onde as casas são mais caras. Para medir o esforço real de comprar casa é preciso olhar também para os anos de rendimento necessários, as taxas de juro, as condições do crédito e o peso da habitação no orçamento das famílias.</p>
<h2>O comentário do Panorama Imobiliário</h2>
<p><b>Para quem compra</b>, o dado confirma o que se sente nas visitas: o salário de hoje compra menos casa do que há dez anos. Daí a importância de olhar para além do centro, para zonas bem servidas por transportes como Matosinhos, Perafita ou a Maia, e de aproveitar os apoios em vigor, como a garantia pública para jovens até 35 anos.</p>
<p><b>Para quem vende</b>, o aviso é o contrário: com o orçamento das famílias no limite, o comprador compara tudo. Preço ajustado ao mercado e uma apresentação que mostre o imóvel como ele é (fotografia, vídeo, visita 3D) fazem a diferença entre vender em semanas ou ficar meses à espera.</p>
<h2>Cordial Level Shopping: três imóveis até 350 000 €</h2>
<table class="bt"><thead><tr><th>Imóvel</th><th>Área útil</th><th>Preço</th></tr></thead><tbody>
<tr><td><a href="/cordiallevel/perafita/">T2 remodelado com garagem e arrumos, Perafita</a></td><td>83 m²</td><td>258 000 €</td></tr>
<tr><td><a href="/cordiallevel/cedofeita/">T1 duplex quase novo, Cedofeita, Porto</a></td><td>59 m²</td><td>289 000 €</td></tr>
<tr><td><a href="/cordiallevel/anteroquental/">T2 remodelado na Antero de Quental, Porto</a></td><td>77,30 m²</td><td>349 000 €</td></tr></tbody></table>
<p class="cap">Preços e disponibilidade sujeitos a confirmação · Cordial Level | CENTURY 21 Arquitectos · AMI 11414</p>
<p>O tema é o ponto de partida do próximo episódio do podcast <b>Panorama Imobiliário PT</b>.</p>
<p class="cap">Fontes: <a href="https://ec.europa.eu/eurostat/databrowser/view/tipsho60/default/table" target="_blank" rel="noopener">Eurostat, rácio preço da habitação/rendimento</a> · <a href="https://observador.pt/2026/11/09/racio-entre-precos-das-casas-e-rendimentos-sobe-mais-de-60-em-portugal-numa-decada/" target="_blank" rel="noopener">Observador/Lusa, 9 nov. 2026</a> · <a href="https://executivedigest.sapo.pt/casas-ficaram-muito-mais-caras-face-aos-rendimentos-portugal-regista-aumento-quase-nove-vezes-superior-a-media-da-ue/" target="_blank" rel="noopener">Executive Digest, 9 nov. 2026</a> · <a href="https://sicnoticias.pt/economia/2026-11-09-racio-entre-preco-das-casas-e-rendimentos-subiu-mais-de-60-em-portugal-na-ultima-decada-7cd14f0f" target="_blank" rel="noopener">SIC Notícias</a>.</p>''',
         dica='Antes de procurar casa, faça a conta ao contrário: parta da prestação que cabe no seu orçamento e só depois defina o preço máximo. Uma simulação de crédito leva minutos e evita visitas a casas fora do alcance.',
         veredito='O número é duro, mas não é o fim da linha: com o preço certo, a zona certa e o crédito bem preparado, continua a haver bons negócios para quem compra e para quem vende.',
         cta='''<div class="clb"><img src="/cordiallevel/img/logo-cordial-level-claro.png" alt="Cordial Level" width="1156" height="754" loading="lazy">
<div><b>Quer saber quanto pode comprar, ou quanto vale o seu imóvel hoje? Fale connosco!</b>
<p>Casemiro Ramos e Francisco Medeiros, consultores da Cordial Level, ajudam a preparar o crédito, a avaliação e a venda, do primeiro contacto à escritura.</p>
<div class="clr"><a href="/cordiallevel/">Ver a Cordial Level</a><a href="https://wa.me/351935101667?text=Ol%C3%A1%20Casemiro%2C%20li%20o%20Panorama%20Imobili%C3%A1rio%20sobre%20o%20pre%C3%A7o%20das%20casas%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es." target="_blank" rel="noopener">Casemiro · 935 101 667</a><a href="https://wa.me/351912706395?text=Ol%C3%A1%20Francisco%2C%20li%20o%20Panorama%20Imobili%C3%A1rio%20sobre%20o%20pre%C3%A7o%20das%20casas%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es." target="_blank" rel="noopener">Francisco · 912 706 395</a></div>
<small>Chamada para a rede móvel nacional · Cordial Level | CENTURY 21 Arquitectos · AMI 11414</small></div></div>''',
         links=[('Ver os imóveis da Cordial Level', '/cordiallevel/'), ('Episódios no YouTube', 'https://www.youtube.com/@CordialLevelPT')]),
    dict(slug='do-papel-a-tela-foz-do-douro', cat='bastidores', date='2026-11-09',
         title='Do papel à tela: um voo pela Foz do Douro',
         desc='Drone e câmara na mão pela Foz do Douro, dos molhes ao Jardim do Passeio Alegre: o novo filme de bastidores da Usina Vídeos, com Freire Neto e Sandra Freire.',
         img='/img/blog/foz-do-papel-a-tela.jpg', img_cap='Foz do Douro vista de cima · drone Usina Vídeos',
         lead='Quando o Douro encontra o Atlântico, o cenário fala por si. Fomos à Foz com o drone e a câmara para mostrar como a Usina transforma um guião em imagem.',
         body='''<p>Nesta gravação na <b>Foz do Douro</b>, no Porto, <b>Freire Neto</b> e <b>Sandra Freire</b> captaram cada detalhe: os molhes e o farol, a marginal entre palmeiras, a Fortaleza de São João da Foz e o <b>Jardim do Passeio Alegre</b> com as cores do outono.</p>
<figure class="bf"><video controls playsinline preload="none" poster="/img/blog/foz-do-papel-a-tela.jpg" style="width:100%;border-radius:16px;background:#000;aspect-ratio:16/9"><source src="/media/foz-do-papel-a-tela.mp4" type="video/mp4"></video><figcaption>Do papel à tela · Foz do Douro, Porto · produção e edição Usina Vídeos</figcaption></figure>
<h2>Décadas de história, a mesma vontade</h2>
<p>Desde 1997, acompanhámos a passagem do jornal para a era das redes sociais. O que nos move continua igual: contar boas histórias, gerar impacto real e entregar soluções completas em jornalismo, marketing e comunicação.</p>
<h2>Como foi feito</h2>
<ul><li><b>Drone</b> (DJI Mini 4 Pro) sobre os molhes, a marginal e o rio.</li>
<li><b>Câmara em terra</b>, com planos de pormenor no paredão e no jardim.</li>
<li><b>Edição e música</b> pensadas para Reels, YouTube e site, num só filme.</li></ul>
<p>É o mesmo método que usamos nas vídeo-reportagens de imóveis, como o <a href="/t4coral/">Condomínio Coral, na Foz</a>, e nos trabalhos para a <a href="/cordiallevel/">Cordial Level</a>.</p>
<p><a href="https://youtu.be/_DmRtHWTy2k" target="_blank" rel="noopener">Veja o filme no YouTube, no canal Dicas do Freire ↗</a> · <a href="https://www.instagram.com/reel/Deu9izSoAB6/" target="_blank" rel="noopener">e no Instagram do @neofreireportugal ↗</a></p>''',
         dica='Grave a sua zona com luz de manhã cedo ou ao fim da tarde: o céu e o rio ficam com mais cor e menos reflexos.',
         veredito='Um lugar bem filmado vende-se sozinho. É isso que fazemos por imóveis, marcas e cidades.',
         links=[('Ver o filme no YouTube (Dicas do Freire)', 'https://youtu.be/_DmRtHWTy2k'), ('Pedir um orçamento por WhatsApp', WA), ('Ver o canal Dicas do Freire', 'https://www.youtube.com/@DicasdoFreire')]),
    dict(slug='cordial-level-nas-lives-motores-e-acao', cat='cases', date='2026-11-07',
         title='Cordial Level estreia-se nas lives do Motores e Ação',
         desc='A partir de agora, a Cordial Level é exibida e divulgada nas lives do Motores e Ação. A estreia foi na sexta-feira, 6 de novembro, com Freire Neto.',
         img='/img/blog/merchan-cordial-mea.jpg', img_cap='Merchan da Cordial Level na live SEXTOU do Motores e Ação · Usina Vídeos',
         lead='Quem pensa em morar ou investir em Portugal passa a encontrar a Cordial Level todas as semanas nas lives do Motores e Ação, um canal com mais de 20 anos.',
         body='''<p>A estreia foi na <b>sexta-feira, 6 de novembro</b>, na live <b>SEXTOU</b> do Motores e Ação, com <b>Freire Neto</b> e Edward Sousa. A meio da conversa sobre o mercado automóvel, entrou o novo parceiro do canal: a <b>Cordial Level</b>, equipa dos consultores <b>Casemiro Ramos</b> e <b>Francisco Medeiros</b>, da CENTURY 21 Arquitectos.</p>
<figure class="bf"><video controls playsinline preload="none" poster="/img/blog/merchan-cordial-mea.jpg" style="width:100%;border-radius:16px;background:#000;aspect-ratio:16/9"><source src="/cordiallevel/media/merchan-mea-16x9.mp4" type="video/mp4"></video><figcaption>Morar ou investir em Portugal: o merchan da Cordial Level na live SEXTOU · edição Usina Vídeos</figcaption></figure>
<h2>"Eu vivi isso na pele"</h2>
<p>Freire Neto mudou-se do Brasil para Portugal em 2023 e conhece as dúvidas de quem chega: onde procurar casa, em quem confiar, que freguesia ou zona escolher. É essa experiência que leva para a recomendação: para morar, arrendar, comprar ou investir, a Cordial Level acompanha o processo do primeiro contacto à escritura.</p>
<h2>Um canal com mais de 20 anos</h2>
<p>O <b>Motores e Ação</b> atua no mercado brasileiro desde 2002 e, desde 2023, produz também conteúdos em Portugal. Tem mais de 110 mil inscritos no YouTube e lives semanais com notícias, lançamentos e ofertas. É uma audiência de brasileiros e portugueses, muitos deles a pensar em viver ou investir em Portugal.</p>
<h2>O que a Usina Vídeos produziu</h2>
<ul><li><b>Faixa de merchan na live</b>, com a marca, os dois consultores e o endereço usinavideos.pt/cordiallevel.</li>
<li><b>Vídeo para o YouTube</b> da Cordial Level, com legendas e cartão final de contactos.</li>
<li><b>Reel e Short verticais</b> com o essencial em 40 segundos.</li>
<li><b>Carrossel e story</b> para o Instagram e o Facebook.</li></ul>
<figure class="bf" style="max-width:420px;margin-left:auto;margin-right:auto"><video controls playsinline preload="none" poster="/cordiallevel/img/social/merchan-mea/reel-capa.jpg" style="width:100%;border-radius:16px;background:#000;aspect-ratio:9/16"><source src="/cordiallevel/media/merchan-mea-reel.mp4" type="video/mp4"></video><figcaption>Versão vertical para Reels e Shorts · Usina Vídeos</figcaption></figure>
<h2>Contactos</h2>
<div style="display:flex;gap:14px;align-items:center;margin:14px 0"><img src="/cordiallevel/img/casemiro.jpg" alt="Casemiro Ramos" width="84" height="84" loading="lazy" style="width:84px;height:84px;border-radius:50%;object-fit:cover;border:3px solid #B8962E;flex:none"><p style="margin:0"><b>Casemiro Ramos</b>, Consultor<br><a href="https://wa.me/351935101667">WhatsApp 935 101 667</a><br><a href="https://www.century21.pt/consultores/cramos">century21.pt/consultores/cramos</a></p></div>
<div style="display:flex;gap:14px;align-items:center;margin:14px 0"><img src="/cordiallevel/img/francisco.jpg" alt="Francisco Medeiros" width="84" height="84" loading="lazy" style="width:84px;height:84px;border-radius:50%;object-fit:cover;border:3px solid #B8962E;flex:none"><p style="margin:0"><b>Francisco Medeiros</b>, Consultor<br><a href="tel:+351912706395">912 706 395</a><br><a href="mailto:franciscomedeiros@century21.pt">franciscomedeiros@century21.pt</a></p></div>
<p>Cordial Level | CENTURY 21 Arquitectos · AMI 11414</p>''',
         dica='Uma parceria de conteúdo rende mais quando o mesmo momento vira várias peças: a live, o vídeo do YouTube, o Reel, o carrossel e o artigo.',
         veredito='Credibilidade de quem viveu a mudança, ao serviço de quem a está a planear.',
         links=[('Ver a Cordial Level e os imóveis', '/cordiallevel/'), ('Ver a live completa no YouTube', 'https://www.youtube.com/watch?v=bJhROYiy-VU&t=3168s'), ('Canal da Cordial Level no YouTube', 'https://www.youtube.com/@CordialLevelPT')]),
    dict(slug='t2-perafita-cordial-level', cat='mercados', date='2026-11-04',
         title='T2 em Perafita: uma oportunidade especial com a Cordial Level',
         desc='Já à venda: T2 remodelado em Perafita, Matosinhos, com 83 m², lugar de garagem e arrumos, ao lado da A28, por 258 000 €. Vídeo com Francisco Medeiros e visita virtual 3D.',
         img='/img/blog/perafita-t2.jpg', img_cap='Francisco Medeiros em Perafita · vídeo Usina Vídeos',
         lead='Já à venda por 258 000 €: um T2 remodelado em Perafita, com 83 m², lugar de garagem grande e arrumos, ao lado da A28.',
         body='''<p>Prometemos e cumprimos: depois dos dias de gravação, chega o primeiro vídeo. O T2 fica em <b>Perafita, no concelho de Matosinhos</b>, e é apresentado pelo <b>Francisco Medeiros</b>, consultor da Cordial Level.</p>
<figure class="bf" style="max-width:420px;margin-left:auto;margin-right:auto"><video controls playsinline preload="none" poster="/cordiallevel/img/perafita-t2-capa.jpg" style="width:100%;border-radius:16px;background:#000;aspect-ratio:9/16"><source src="/cordiallevel/media/perafita-t2.mp4" type="video/mp4"></video><figcaption>T2 em Perafita, apresentado por Francisco Medeiros · vídeo Usina Vídeos</figcaption></figure>
<h2>Porque é uma boa oportunidade</h2>
<ul><li><b>Localização estratégica</b>, ao lado da A28.</li>
<li>Perto de <b>escolas</b> e de <b>transportes públicos</b>.</li>
<li>T2 em <b>excelentes condições</b>, por um <b>preço muito bom</b>.</li></ul>
<h2>Já à venda: 258 000 €</h2>
<ul><li><b>T2</b> com 83 m² úteis e 100,6 m² de área bruta, 1 casa de banho.</li>
<li><b>Remodelado:</b> cozinha remodelada, pavimento flutuante, caixilharia dupla com vidro duplo e isolamento exterior em capoto.</li>
<li><b>Lugar de garagem grande</b> e <b>espaço de arrumos</b>.</li>
<li>Edifício de 2003 · certificado energético D · ref. <a href="https://century21.pt/ref/C0393-01754" target="_blank" rel="noopener">C0393-01754</a>.</li></ul>
<p>Para marcar uma visita, fale diretamente com o Francisco Medeiros ou com o Casemiro Ramos.</p>
<h2>Tem um imóvel na zona?</h2>
<p>Se tem um apartamento para vender ou arrendar em Perafita ou nas redondezas, a Cordial Level está pronta para ajudar. Como explica o Francisco, quantos mais imóveis tivermos na mesma zona, maior é a procura que conseguimos atrair para todos.</p>
<h2>O que a Usina Vídeos produziu</h2>
<p>Para este T2, a Usina Vídeos fez a tradicional <b>reportagem de fotografia e vídeo</b> e a <b>visita virtual 3D</b>. Produzimos também um teaser com o consultor <b>Francisco Medeiros</b> (Cordial Level | CENTURY 21 Arquitectos), já publicado em todas as redes sociais da Cordial Level.</p>
<figure class="bf"><img src="/cordiallevel/perafita/img/pf-fachada.jpg" alt="Fachada do edifício do T2 em Perafita" width="1920" height="1072" loading="lazy"><figcaption>O edifício em Perafita · fotografia Usina Vídeos</figcaption></figure>
<figure class="bf"><img src="/cordiallevel/perafita/img/pf-transportes.jpg" alt="Paragem de autocarro em frente ao edifício" width="1920" height="1080" loading="lazy"><figcaption>Transportes públicos à porta · fotografia Usina Vídeos</figcaption></figure>
<p><a href="/cordiallevel/perafita/">Veja a apresentação completa do imóvel</a>, com fotografias, vídeo e mapa, ou <a href="https://realsee.ai/JVLLgJmB" target="_blank" rel="noopener">percorra-o na visita virtual 3D</a>. Também há uma <a href="/web-stories/t2-perafita/">web story</a> para ver no telemóvel.</p>
<p class="cap">Fotografias tratadas digitalmente para cor e luz.</p>''',
         dica='Se um imóvel lhe interessa, marque a visita cedo. As boas oportunidades em Matosinhos não ficam muito tempo no mercado.',
         veredito='Um vídeo curto, com o consultor no local: quem procura casa percebe o imóvel antes de sair de casa.',
         cta='''<div class="clb"><img src="/cordiallevel/img/logo-cordial-level-claro.png" alt="Cordial Level" width="1156" height="754" loading="lazy">
<div><b>Quer saber mais sobre o T2 em Perafita ou marcar uma visita? Fale connosco!</b>
<p>Casemiro Ramos e Francisco Medeiros, consultores da Cordial Level, acompanham cada processo do primeiro contacto à escritura.</p>
<div class="clr"><a href="https://wa.me/351912706395?text=Ol%C3%A1%20Francisco%2C%20vi%20o%20v%C3%ADdeo%20do%20T2%20em%20Perafita%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es." target="_blank" rel="noopener">Francisco · 912 706 395</a><a href="https://wa.me/351935101667?text=Ol%C3%A1%20Casemiro%2C%20vi%20o%20v%C3%ADdeo%20do%20T2%20em%20Perafita%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es." target="_blank" rel="noopener">Casemiro · 935 101 667</a><a href="mailto:franciscomedeiros@century21.pt?subject=T2%20em%20Perafita">franciscomedeiros@century21.pt</a></div>
<small>Chamada para a rede móvel nacional · Cordial Level | CENTURY 21 Arquitectos · AMI 11414</small></div></div>''',
         links=[('Ver a apresentação do imóvel', '/cordiallevel/perafita/'), ('Visita virtual 3D', 'https://realsee.ai/JVLLgJmB'), ('Ver a Cordial Level', '/cordiallevel/')]),
    dict(slug='em-breve-t2-perafita-moradia-senhora-da-hora', cat='bastidores', date='2026-11-03',
         title='Em breve: T2 em Perafita e moradia T3+T2+T2 na Senhora da Hora',
         desc='Dias de gravação na CENTURY 21: dois imóveis em Matosinhos chegam em breve às redes sociais e aos portais. Saiba como ser o primeiro a conhecer os detalhes.',
         img='/img/blog/em-breve/moradia-drone.jpg', img_cap='Moradia na Senhora da Hora, Matosinhos · drone Usina Vídeos',
         lead='Foram dias de drone no ar e câmara na mão. Duas novas oportunidades da CENTURY 21 estão quase prontas para chegar ao mercado.',
         body='''<p>A Usina Vídeos esteve a gravar dois imóveis em Matosinhos. As fotos, os vídeos e todos os detalhes vão ser publicados em breve nas nossas redes sociais e nos principais portais imobiliários.</p>
<h2>T2 em Perafita · Cordial Level</h2>
<figure class="bf"><img src="/img/blog/em-breve/predio-perafita.jpg" alt="Edifício do apartamento T2 em Perafita" width="1600" height="901" loading="lazy"><figcaption>Perafita, Matosinhos · Usina Vídeos</figcaption></figure>
<p>Um apartamento T2 em Perafita, no concelho de Matosinhos, com a <b>Cordial Level</b>.</p>
<div style="display:flex;flex-wrap:wrap;gap:22px;margin-top:18px"><div style="display:flex;align-items:center;gap:12px"><img src="/cordiallevel/img/casemiro.jpg" alt="Casemiro Ramos" width="64" height="64" style="border-radius:50%;border:3px solid #C9A45C;object-fit:cover" loading="lazy"><span><b>Casemiro Ramos</b> · Consultor<br><a href="https://wa.me/351935101667" target="_blank" rel="noopener">935 101 667</a></span></div><div style="display:flex;align-items:center;gap:12px"><img src="/cordiallevel/img/francisco.jpg" alt="Francisco Medeiros" width="64" height="64" style="border-radius:50%;border:3px solid #C9A45C;object-fit:cover" loading="lazy"><span><b>Francisco Medeiros</b> · Consultor<br><a href="https://wa.me/351912706395" target="_blank" rel="noopener">912 706 395</a></span></div></div>
<p class="cap">Cordial Level | CENTURY 21 Arquitectos · AMI 11414</p>
<h2>Moradia T3+T2+T2 na Senhora da Hora</h2>
<figure class="bf"><img src="/img/blog/em-breve/moradia-frente.jpg" alt="Fachada da moradia na Senhora da Hora" width="1600" height="939" loading="lazy"><figcaption>Senhora da Hora, Matosinhos · Usina Vídeos</figcaption></figure>
<p>Uma moradia T3+T2+T2 na Senhora da Hora, também em Matosinhos, com o consultor <b>José Bacelar</b>.</p>
<div style="display:flex;align-items:center;gap:12px;margin-top:18px"><img src="/img/blog/em-breve/jose-bacelar.jpg" alt="José Bacelar" width="64" height="64" style="border-radius:50%;border:3px solid #C9A45C;object-fit:cover" loading="lazy"><span><b>José Bacelar</b> · Consultor<br><a href="https://wa.me/351917103516" target="_blank" rel="noopener">917 103 516</a> · <a href="mailto:josembacelar@century21.pt">josembacelar@century21.pt</a></span></div>
<p class="cap">José Bacelar · CENTURY 21 Arquitectos III · AMI 23921</p>
<h2>Bastidores</h2>
<figure class="bf"><img src="/img/blog/em-breve/bastidores-drone.jpg" alt="Freire Neto a pilotar o drone durante a gravação" width="1600" height="1352" loading="lazy"><figcaption>Freire Neto a pilotar o drone · Usina Vídeos</figcaption></figure>
<p>Cada imóvel tem fotografia, vídeo e imagens aéreas. Assim, quem procura casa percebe logo o imóvel e a zona, antes de marcar a visita.</p>
<figure class="bf"><img src="/img/blog/em-breve/envolvente-1.jpg" alt="Vista aérea da zona, com vias de acesso" width="1600" height="900" loading="lazy"><figcaption>Imagem aérea da zona · drone Usina Vídeos</figcaption></figure>
<h2>Quer ser o primeiro a saber?</h2>
<p>Envie o seu <b>nome e apelido</b>, o <b>e-mail</b> e o <b>número de telemóvel</b> por WhatsApp para o <a href="https://wa.me/351912988971?text=Ol%C3%A1%20Freire%2C%20quero%20saber%20os%20detalhes%20do%20T2%20em%20Perafita%20e%20da%20moradia%20na%20Senhora%20da%20Hora.%20Nome%3A%20%20E-mail%3A%20%20Telem%C3%B3vel%3A%20" target="_blank" rel="noopener">912 988 971</a> ou para <a href="mailto:freireneto@me.com?subject=Em%20breve%3A%20T2%20Perafita%20e%20moradia%20Senhora%20da%20Hora">freireneto@me.com</a>. Recebe os detalhes antes de serem publicados. Os seus dados servem só para o contactar sobre estes imóveis.</p>''',
         dica='Se procura casa em Matosinhos, tenha já a simulação de crédito feita. Quando um bom imóvel chega ao mercado, quem está pronto visita primeiro.',
         veredito='Boas imagens chegam antes do anúncio: quem segue as nossas redes vê primeiro.',
         links=[('Pedir os detalhes por WhatsApp', 'https://wa.me/351912988971?text=Ol%C3%A1%20Freire%2C%20quero%20saber%20os%20detalhes%20do%20T2%20em%20Perafita%20e%20da%20moradia%20na%20Senhora%20da%20Hora.'), ('Ver a Cordial Level', '/cordiallevel/')]),
    dict(slug='dois-sites-novos-usinavideos-motoreseacao', cat='cases', date='2026-11-02',
         title='Dois sites novos no ar: usinavideos.pt e motoreseacao.com',
         desc='A Usina Vídeos e o Motores e Ação estrearam sites novos. Mostramos as capas, as secções e o que cada um oferece.',
         img='/img/blog/sites-novos/capa.jpg', img_cap='usinavideos.pt e motoreseacao.com · arte Usina Vídeos',
         lead='A produtora e o jornalismo automóvel nasceram juntos em 2002. Agora têm casa nova na internet, feita com o mesmo método que usamos para os clientes.',
         body='''<p>São dois sites com objetivos diferentes. O <b>usinavideos.pt</b> mostra o que a Usina Vídeos faz e como pedir um orçamento. O <b>motoreseacao.com</b> é onde o <b>Motores e Ação</b> publica notícias, testes e ofertas todos os dias. Os dois foram pensados primeiro para o telemóvel.</p>
<h2>usinavideos.pt: a produtora</h2>
<figure class="bf"><img src="/img/blog/sites-novos/usina-capa.jpg" alt="Capa do site usinavideos.pt com vista de drone da Foz do Douro" width="1600" height="1000" loading="lazy"><figcaption>Capa do usinavideos.pt · Foz do Douro, drone Usina Vídeos</figcaption></figure>
<p>Na capa está logo o essencial: o que fazemos, para quem e um botão para pedir orçamento por WhatsApp. O site está em <b>português, inglês e espanhol</b>.</p>
<figure class="bf"><img src="/img/blog/sites-novos/usina-servicos.jpg" alt="Secção de serviços: vídeo, fotografia, drone, redes sociais, sites e campanhas" width="1600" height="983" loading="lazy"><figcaption>Serviços: vídeo e reportagem, fotografia, drone, redes sociais, sites e campanhas</figcaption></figure>
<ul><li><b>Serviços:</b> vídeo e reportagem, fotografia, drone, conteúdo para redes sociais, sites e campanhas de marketing digital.</li>
<li><b>Trabalhos:</b> projetos recentes, publicados com autorização, como a Cordial Level, o Condomínio Coral na Foz e o CDJ Régio.</li>
<li><b>Sites, apresentações e podcasts:</b> exemplos reais, do site da Cordial Level ao Panorama Imobiliário PT.</li>
<li><b>Blog e web stories:</b> bastidores, mercado e dicas, também em formato vertical.</li></ul>
<figure class="bf"><img src="/img/blog/sites-novos/usina-trabalhos.jpg" alt="Secção de trabalhos com a Cordial Level e o Condomínio Coral" width="1600" height="1250" loading="lazy"><figcaption>Trabalhos recentes, publicados com autorização dos clientes</figcaption></figure>
<figure class="bf"><img src="/img/blog/sites-novos/usina-sites.jpg" alt="Secção de sites, apresentações digitais e podcasts" width="1600" height="912" loading="lazy"><figcaption>Sites, apresentações digitais e podcasts, com exemplos</figcaption></figure>
<h2>motoreseacao.com: jornalismo automóvel desde 2002</h2>
<figure class="bf"><img src="/img/blog/sites-novos/mea-capa.jpg" alt="Capa do site motoreseacao.com com a barra de última hora e os destaques" width="1600" height="1025" loading="lazy"><figcaption>Capa do motoreseacao.com, com a barra "Última hora" e o destaque da semana</figcaption></figure>
<p>O Motores e Ação ficou mais rápido e mais fácil de ler no telemóvel. Tem notícias e lançamentos do Brasil e de Portugal, testes, ofertas e o espaço Europa.</p>
<ul><li><b>Última hora:</b> as notícias do dia, numa barra no topo.</li>
<li><b>Shorts e web stories:</b> as notícias em menos de um minuto, em vertical.</li>
<li><b>Canal no YouTube:</b> mais de 114 mil inscritos, com lançamentos, testes e lives.</li>
<li><b>Mídia kit:</b> para marcas e stands que querem anunciar.</li></ul>
<figure class="bf"><img src="/img/blog/sites-novos/mea-shorts.jpg" alt="Secções Shorts da semana, redes sociais e Web Stories do Motores e Ação" width="1600" height="1473" loading="lazy"><figcaption>Shorts da semana, redes sociais e web stories</figcaption></figure>
<figure class="bf"><img src="/img/blog/sites-novos/mea-midia.jpg" alt="Faixa do mídia kit do Motores e Ação" width="1600" height="405" loading="lazy"><figcaption>Anuncie no Motores e Ação: mídia kit</figcaption></figure>
<h2>Um site que trabalha pelo seu negócio</h2>
<p>O que fizemos para nós é o que fazemos para os clientes: páginas rápidas, conteúdo próprio em vídeo e foto, contacto direto por WhatsApp e tudo ligado às redes sociais.</p>
<figure class="bf" style="max-width:420px"><img src="/img/blog/sites-novos/arte-post.jpg" alt="Arte de divulgação dos dois sites novos" width="1080" height="1350" loading="lazy"><figcaption>Arte de divulgação nas redes sociais</figcaption></figure>''',
         dica='Antes de investir em anúncios, veja o seu site no telemóvel durante um minuto. Se não percebe logo o que faz e como contactar, os anúncios vão gastar dinheiro.',
         veredito='Dois sites, a mesma escola: conteúdo próprio, rapidez e um contacto a um toque.',
         links=[('Visitar usinavideos.pt', '/'), ('Visitar motoreseacao.com', 'https://www.motoreseacao.com/?utm_source=usinavideos&utm_medium=blog&utm_campaign=sites-novos'), ('Pedir orçamento por WhatsApp', WA)]),
    dict(slug='panorama-imobiliario-credito-jovem-2027', cat='mercados', date='2026-10-29',
         title='Panorama Imobiliário PT: crédito jovem em 2027 e três imóveis para conhecer',
         desc='No novo episódio, Francisco Medeiros e Freire Neto falam do mercado, da angariação e do crédito jovem, e apresentam três imóveis da Cordial Level.',
         img='/web-stories/panorama-credito-jovem-2027/img/capa-blog.jpg', img_cap='Piscinas das Marés, Leça da Palmeira · drone Usina Vídeos',
         lead='A garantia pública para jovens está garantida até ao fim do ano. Para 2027 há uma proposta, mas ainda não há decisão. É o ponto de partida do novo episódio do Panorama Imobiliário PT.',
         body='''<p>Gravado na CENTURY 21 Arquitectos, o episódio junta <b>Francisco Medeiros</b>, consultor da Cordial Level, e <b>Freire Neto</b>, da Usina Vídeos. Em cima da mesa: o mercado, a angariação, o crédito jovem, o que diferencia a Cordial Level, a rede CENTURY 21 e o trabalho de consultoria até à escritura.</p>
<div style="display:flex;flex-wrap:wrap;gap:22px;margin-top:20px"><div style="display:flex;align-items:center;gap:12px"><img src="/web-stories/panorama-credito-jovem-2027/img/francisco.png" alt="Francisco Medeiros" width="72" height="72" style="border-radius:50%;border:3px solid #C9A45C" loading="lazy"><span><b>Francisco Medeiros</b><br>Consultor · Cordial Level</span></div><div style="display:flex;align-items:center;gap:12px"><img src="/web-stories/panorama-credito-jovem-2027/img/freire.png" alt="Freire Neto" width="72" height="72" style="border-radius:50%;border:3px solid #C9A45C" loading="lazy"><span><b>Freire Neto</b><br>Jornalista · Usina Vídeos</span></div></div>
<h2>Crédito jovem: o que está em vigor</h2>
<ul><li>Jovens dos <b>18 aos 35 anos</b>, com morada fiscal em Portugal, a comprar a <b>primeira habitação própria e permanente</b>.</li>
<li>O Estado garante até <b>15%</b> do valor e o banco pode financiar até <b>100%</b>.</li>
<li>Imóveis até <b>450 000 €</b>. A aprovação do crédito é sempre do banco.</li></ul>
<p>Segundo o Banco de Portugal, até junho de 2026 foram assinados <b>40 148 contratos</b> com garantia pública, num total de 8,3 mil milhões de euros.</p>
<h2>E em 2027?</h2>
<p>A garantia cobre contratos assinados até 31 de dezembro de 2026. A proposta de Orçamento do Estado para 2027, entregue a 8 de outubro, prevê mantê-la, bem como as isenções de IMT e Imposto do Selo. O ministro das Finanças disse, porém, que a decisão formal ainda não foi tomada.</p>
<h2>O que muda para quem vende</h2>
<p>Há muitos compradores jovens com financiamento à procura de casas até 450 000 €. Mas procura não chega: o preço certo e uma boa apresentação continuam a decidir a venda.</p>
<h2>Cordial Level Shopping</h2>
<table class="bt"><thead><tr><th>Imóvel</th><th>Área útil</th><th>Preço</th></tr></thead><tbody>
<tr><td><a href="/cordiallevel/anteroquental/">T2 remodelado na Antero de Quental, Porto</a></td><td>77,30 m²</td><td>349 000 €</td></tr>
<tr><td><a href="/cordiallevel/t3leca/">T3 com suíte e 2 lugares de garagem, Leça da Palmeira</a></td><td>138 m²</td><td>550 000 €</td></tr>
<tr><td><a href="/cordiallevel/casaraofoz/">Moradia T4 com vista de mar, Foz do Douro</a></td><td>165 m²</td><td>875 000 €</td></tr></tbody></table>
<p class="cap">Preços e disponibilidade sujeitos a confirmação · Cordial Level | CENTURY 21 Arquitectos · AMI 11414</p>
<figure class="bf"><img src="/cordiallevel/anteroquental/img/aq-lapa.jpg" alt="Igreja da Lapa e Rua Antero de Quental vistas de drone" loading="lazy"><figcaption>Rua Antero de Quental, junto à Igreja da Lapa · drone Usina Vídeos</figcaption></figure>
<p>O T2 da Antero de Quental é o único dos três dentro do limite da garantia pública para jovens.</p>
<p>Veja também a <a href="/web-stories/panorama-credito-jovem-2027/">web story do episódio</a>.</p>
<p class="cap">Fontes: <a href="https://www.idealista.pt/news/financas/credito-a-habitacao/2026/10/08/78113-garantia-publica-e-isencao-de-imt-mantem-se-para-jovens-em-2027" target="_blank" rel="noopener">idealista/news, 8 out. 2026</a> · <a href="https://www.literaciafinanceira.pt/artigos/credito-habitacao-jovem" target="_blank" rel="noopener">Literacia Financeira, dados do Banco de Portugal</a> · <a href="https://portugal.gov.pt/pt/gc24/comunicacao/noticias/garantia-publica-o-que-e-e-como-funciona" target="_blank" rel="noopener">Governo de Portugal</a>. Informação geral, situação a 27 de outubro de 2026; não dispensa simulação junto do banco.</p>''',
         dica='Se tem até 35 anos, não deixe a simulação para dezembro. Um processo de crédito demora semanas, e o prazo certo hoje é 31 de dezembro.',
         veredito='Uma gravação, várias peças: episódio, cortes, carrossel, web story e este artigo. Assim um tema chega a quem procura casa e a quem quer vender.',
         cta='''<div class="clb"><img src="/cordiallevel/img/logo-cordial-level-claro.png" alt="Cordial Level" width="1156" height="754" loading="lazy">
<div><b>Quer comprar com a garantia pública ou saber quanto vale o seu imóvel? Fale connosco!</b>
<p>Casemiro Ramos e Francisco Medeiros, consultores da Cordial Level, acompanham cada processo do primeiro contacto à escritura.</p>
<div class="clr"><a href="/cordiallevel/">Ver a Cordial Level</a><a href="https://wa.me/351935101667?text=Ol%C3%A1%20Casemiro%2C%20vi%20o%20Panorama%20Imobili%C3%A1rio%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es." target="_blank" rel="noopener">Casemiro · 935 101 667</a><a href="https://wa.me/351912706395?text=Ol%C3%A1%20Francisco%2C%20vi%20o%20Panorama%20Imobili%C3%A1rio%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es." target="_blank" rel="noopener">Francisco · 912 706 395</a></div>
<small>Chamada para a rede móvel nacional · Cordial Level | CENTURY 21 Arquitectos · AMI 11414</small></div></div>''',
         links=[('Ver o episódio no YouTube', 'https://www.youtube.com/@CordialLevelPT'), ('Ver a web story', '/web-stories/panorama-credito-jovem-2027/')]),
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
<div class="yt"><iframe src="https://www.youtube-nocookie.com/embed/qwL_NxCdlNY?rel=0" title="Vídeo do Condomínio Coral com Cheila Monteiro" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>''',
         dica='Grave o consultor sempre no próprio imóvel e no fim do vídeo. É o rosto que o comprador vai procurar quando ligar.',
         veredito='Um briefing, uma produção, quatro entregáveis. É este o padrão que propomos para qualquer imóvel premium.',
         links=[('Ver a apresentação do Coral', '/t4coral/'), ('Ver o vídeo no YouTube', 'https://youtu.be/qwL_NxCdlNY')]),
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
.art .meta{margin-top:14px;font-size:14px;color:var(--muted)}.art .hero{display:block;min-height:0;width:100%;height:auto;border-radius:18px;margin-top:26px;aspect-ratio:16/9;object-fit:cover}
.art .cap{position:static;font-size:12px;color:var(--muted);margin-top:6px}
.art .imp{margin-top:26px;font-size:21px;line-height:1.45;font-weight:700;color:var(--ink);border-left:5px solid var(--y);padding-left:18px}
.art h2{font-size:26px;margin-top:34px}.art p,.art li{font-size:18px;line-height:1.65}.art p{margin-top:14px}.art ul{margin-top:14px;padding-left:22px;display:grid;gap:8px}
.art .bf{margin:26px 0 0}.art .bf img{width:100%;height:auto;border-radius:16px}.art figcaption{font-size:12px;color:var(--muted);margin-top:6px}
.art .yt{position:relative;aspect-ratio:16/9;margin-top:26px;border-radius:16px;overflow:hidden;background:#000}.art .yt iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.bt{width:100%;border-collapse:collapse;margin-top:16px;background:#fff;border-radius:12px;overflow:hidden;font-size:16px}.bt th,.bt td{padding:12px 14px;border-bottom:1px solid #E3DED6;text-align:left}.bt th{background:var(--ink);color:#fff;font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.dica{margin-top:30px;background:#FFF7E3;border:1px solid #F1D592;border-radius:16px;padding:20px 22px}.dica b{display:block;font-size:15px;color:var(--ink)}.dica p{margin-top:6px!important}
.ver{margin-top:18px;background:var(--ink);color:#E9E5E1;border-radius:16px;padding:20px 22px}.ver b{display:block;color:var(--y);font-size:13px;letter-spacing:.14em;text-transform:uppercase}.ver p{margin-top:6px!important;color:#E9E5E1}
.clb{margin-top:26px;display:grid;grid-template-columns:110px 1fr;gap:18px;align-items:center;background:#0F2438;color:#E6E1D6;border-radius:18px;padding:22px;border-bottom:5px solid #C9A45C}
.clb img{width:110px;height:auto}.clb b{display:block;color:#fff;font-size:19px;line-height:1.3}.clb p{margin-top:8px!important;font-size:16px!important;color:#D7D2C6}
.clr{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.clr a{background:#C9A45C;color:#0F2438;font-weight:800;font-size:14px;padding:9px 14px;border-radius:999px;text-decoration:none}
.clb small{display:block;margin-top:10px;font-size:12px;color:#B9B3A6}@media(max-width:560px){.clb{grid-template-columns:1fr}.clb img{width:90px}}
.autor{display:flex;gap:14px;align-items:center;margin-top:30px;padding:14px 16px;border:1px solid #E3DED6;border-radius:14px;background:#fff}.autor img{width:64px;height:64px;border-radius:50%;object-fit:cover;border:3px solid #E5AE29;flex:none}.autor b{display:block;color:var(--ink)}.autor span{display:block;font-size:14px;color:#5E5855;line-height:1.4}.autor small{display:block;font-size:11px;color:#8A8380;margin-top:2px}.sig{margin-top:26px;font-weight:800;color:var(--ink)}.blinks{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}
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
<style>{CSS}{MEA_CSS}{BLOG_CSS}{SOCIAL_CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Menu"><div class="wrap">
  <a class="logo" href="/"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <div class="links" style="display:flex"><a href="/">Início</a><a href="/blog/">Blog</a><a href="/#trabalhos">Trabalhos</a></div>
  <a class="btn y" href="{WA}" target="_blank" rel="noopener">Peça orçamento</a>
</div></nav>
'''


FOOT = f'''<section style="padding:0 0 56px"><div class="wrap">{social_banner('usina')}</div></section>
<footer><div class="wrap" style="display:block;margin-bottom:28px">{mea_banner('pt', 'usinavideos_blog')}</div><div class="wrap">
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
  <div class="autor"><img src="/img/equipa/freire-neto-quadrado.jpg" alt="Freire Neto" width="64" height="64" loading="lazy"><div><b>Freire Neto</b><span>Jornalista desde 1997 · fundador da Usina Vídeos e do Motores e Ação</span><small>Foto: Sandra Freire</small></div></div>
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
