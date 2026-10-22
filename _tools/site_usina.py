#!/usr/bin/env python3
"""Site institucional da Usina Vídeos em PT, EN e ES.

Uso: python3 _tools/site_usina.py   -> escreve index.html, en/index.html, es/index.html
Regras: sem preços (pedido de orçamento); simulações IA sempre identificadas;
anúncios Cordial Level sempre com "CENTURY 21 Arquitectos · AMI 11414".
"""
import html, os, urllib.parse as up

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WA_NUM = '351912988971'
MAIL = 'freireneto@me.com'
AMI = 'Cordial Level | CENTURY 21 Arquitectos · AMI 11414'
e = html.escape

T = {
'pt': dict(
    socials=[('https://www.instagram.com/usina.videos','ig','Usina Vídeos','@usina.videos · últimos trabalhos','Seguir'),('https://www.instagram.com/neofreireportugal','ig','Freire Neto em Portugal','@neofreireportugal · Instagram pessoal','Seguir'),('https://www.instagram.com/freireneto','ig','Freire Neto no Brasil','@freireneto · Instagram','Seguir'),('https://www.instagram.com/motoreseacao','ig','Motores e Ação','@motoreseacao · Instagram','Seguir'),('https://www.linkedin.com/in/freireneto/','in','Freire Neto','LinkedIn','Ver perfil')],
    desp=dict(eb='Desporto', h2='Também no pavilhão.', p='Reportagem de jogos e torneios de basquetebol, com destaques e perfis de jogadores para as redes sociais.', cdj='Clube Desportivo José Régio · Vila do Conde. Destaques dos jogos da formação e dos seniores.', mb='MatchBall × Red Rose Thunder', mbp='Tour internacional de basquetebol em Portugal. Perfis e destaques dos jogadores.', ver='Ver no Instagram', mais='Ver mais no Instagram'),
    path='', html_lang='pt-PT', og_locale='pt_PT',
    title='Usina Vídeos · Produção audiovisual imobiliária em Portugal',
    desc='Fotografia, vídeo com drone, reportagem e apresentações digitais para imóveis, no Norte e em todo o Portugal. Peça orçamento.',
    nav=[('quem', 'Quem somos'), ('servicos', 'Serviços'), ('trabalhos', 'Trabalhos'), ('desporto', 'Desporto'), ('como', 'Como funciona'), ('marcas', 'Marcas'), ('contacto', 'Contacto')],
    cta='Peça orçamento',
    wa_msg='Olá Freire, gostaria de pedir um orçamento à Usina Vídeos.',
    hero_eb='Produção audiovisual imobiliária · Norte e todo o Portugal',
    hero_h1='O imóvel certo merece ser bem apresentado.',
    hero_p='Fotografia, vídeo com drone, reportagem e apresentações digitais para consultores imobiliários, promotores e proprietários. Uma produção, um briefing, um contacto.',
    hero_b2='Ver trabalhos',
    hero_cap='Foz do Douro, Porto · drone Usina Vídeos',
    quem_eb='Quem somos', quem_h2='Olhar de jornalista, ao serviço do imóvel.',
    quem_p=['A Usina Vídeos é dirigida por <b>Freire Neto</b> e <b>Sandra Freire</b>. Freire Neto é jornalista desde 1997 e fundador do Motores e Ação, com mais de 25 anos de reportagem e produção audiovisual. Sandra Freire assina a edição de vídeo.',
            'Cada imóvel é tratado como uma reportagem: perceber o que o torna único, captá-lo com rigor e contá-lo de forma clara a quem procura casa. O resultado valoriza o imóvel e reforça a imagem de quem o apresenta.',
            'Trabalhamos em <b>todo o Norte</b> e em <b>qualquer ponto de Portugal</b>, com a deslocação incluída no orçamento.'],
    stats=[('25+', 'anos de jornalismo'), ('48h', 'entrega de fotografias'), ('72h', 'vídeos e PDF'), ('PT · EN · ES', 'apresentações multilingues')],
    serv_eb='Serviços', serv_h2='Tudo o que o imóvel precisa para ser visto.',
    serv_p='Cada serviço pode ser contratado isoladamente ou combinado. Enviamos orçamento à medida do imóvel e do local.',
    servs=[('Reportagem fotográfica', 'Fotografia de alta resolução, com composição e luz cuidadas, pronta para portais e redes sociais.'),
           ('Vídeo com drone', 'Planos aéreos em foto e vídeo que mostram o imóvel no território: envolvente, vistas, acessos e localização.'),
           ('Vídeo com o consultor', 'O consultor apresenta o imóvel à câmara, em formato vertical e horizontal, para todas as plataformas.'),
           ('Visita virtual 3D', 'Visita navegável a 360°, com planta, para portais e compradores à distância.'),
           ('Apresentação digital', 'Uma página própria para o imóvel, com fotografias, vídeo, mapa e contactos, para enviar por WhatsApp ou e-mail.'),
           ('Tratamento e simulações', 'Correção de cor e luz em todas as fotografias. Simulações de decoração ou de obra, sempre identificadas como tal.')],
    medida_h3='Produções à medida',
    medida=['Vídeos de lançamento de empreendimentos', 'Podcast imobiliário', 'Transmissões em direto de open house',
            'Gestão de campanhas e geração de contactos', 'Conteúdos para redes sociais', 'Bolsa de produções pré-paga, sem avença'],
    orc_h3='Cada imóvel é diferente. O orçamento também.',
    orc_p='Diga-nos a morada, a tipologia e o que pretende. Respondemos com uma proposta clara, por imóvel ou por pacote, com o IVA indicado.',
    trab_eb='Trabalhos', trab_h2='Trabalho recente, publicado com autorização.',
    works=[('/cordiallevel/', '/cordiallevel/t3leca/img/leca-37-t.jpg', 'Cordial Level', 'Parceiro de produção: site, vídeo-reportagens, podcast e redes sociais. ' + AMI, 'Ver o site'),
           ('/t4coral/', '/img/coral-fachada.jpg', 'Condomínio Coral · Foz do Douro', 'Fotografia, drone e apresentação digital em quatro línguas. Consultora Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414', 'Ver a apresentação'),
           ('/cordiallevel/anteroquental/', '/cordiallevel/anteroquental/img/aq-lapa-t.jpg', 'T2 Antero de Quental · Porto', 'Fotografia, drone, visita 3D e página do imóvel. ' + AMI, 'Ver a apresentação'),
           ('/cordiallevel/moncao/', '/cordiallevel/moncao/img/t1-area-t.jpg', 'Terrenos em Monção · Alto Minho', 'Drone, vídeo e simulações de projeto identificadas como IA. ' + AMI, 'Ver a apresentação')],
    cdj=('CDJRegio', 'Clube Desportivo José Régio, Vila do Conde. Reportagem e destaques dos jogos de basquetebol.', 'Ver no Instagram'),
    como_eb='Como funciona', como_h2='Do pedido à entrega.',
    steps=[('Pedido de orçamento', 'Envie a morada, a tipologia e o que pretende, por WhatsApp ou e-mail.'),
           ('Produção', 'Deslocamo-nos ao imóvel e fazemos a captação. Uma sessão dura, em regra, até 1h30.'),
           ('Pós-produção', 'Seleção, tratamento de imagem, edição de vídeo e montagem da apresentação.'),
           ('Entrega', 'Fotografias em 48 horas. Vídeos e PDF em 72 horas.')],
    marcas_eb='As nossas marcas', marcas_h2='Também produzimos conteúdo próprio.',
    mea_eb='Em destaque · uma marca Usina Vídeos', mea_p='Jornalismo automóvel desde 2002: lançamentos, testes e ofertas no Brasil e em Portugal.', mea_b='Ler no motoreseacao.com',
    dicas=('Dicas do Freire', 'O canal de Freire Neto no YouTube.', 'Ver o canal'),
    ig=('Freire Neto em Portugal', '@neofreireportugal · Instagram pessoal', 'Seguir'),
    cont_eb='Contacto', cont_h2='Vamos apresentar o seu imóvel?',
    cont_p='Peça orçamento sem compromisso, por WhatsApp ou e-mail.',
    wa_lbl='WhatsApp', mail_lbl='E-mail', social='Redes da Usina',
    foot='Produção audiovisual imobiliária · Norte e todo o Portugal',
    sim='Simulações IA sempre identificadas',
),
'en': dict(
    socials=[('https://www.instagram.com/usina.videos','ig','Usina Vídeos','@usina.videos · latest work','Follow'),('https://www.instagram.com/neofreireportugal','ig','Freire Neto in Portugal','@neofreireportugal · personal Instagram','Follow'),('https://www.instagram.com/freireneto','ig','Freire Neto in Brazil','@freireneto · Instagram','Follow'),('https://www.instagram.com/motoreseacao','ig','Motores e Ação','@motoreseacao · Instagram','Follow'),('https://www.linkedin.com/in/freireneto/','in','Freire Neto','LinkedIn','View profile')],
    desp=dict(eb='Sport', h2='Courtside, too.', p='Basketball games and tournaments covered on video, with highlights and player profiles for social media.', cdj='Clube Desportivo José Régio · Vila do Conde. Highlights from youth and senior games.', mb='MatchBall × Red Rose Thunder', mbp='International basketball tour in Portugal. Player profiles and highlights.', ver='View on Instagram', mais='See more on Instagram'),
    path='en/', html_lang='en', og_locale='en_GB',
    title='Usina Vídeos · Real estate photo and video production in Portugal',
    desc='Photography, drone video, video tours and digital property presentations across Northern Portugal and the whole country. Ask for a quote.',
    nav=[('quem', 'About'), ('servicos', 'Services'), ('trabalhos', 'Work'), ('desporto', 'Sport'), ('como', 'How it works'), ('marcas', 'Brands'), ('contacto', 'Contact')],
    cta='Ask for a quote',
    wa_msg='Hello Freire, I would like a quote from Usina Vídeos.',
    hero_eb='Real estate video production · Northern Portugal and nationwide',
    hero_h1='The right property deserves the right presentation.',
    hero_p='Photography, drone video, video tours and digital presentations for real estate agents, developers and owners. One shoot, one brief, one contact.',
    hero_b2='See our work',
    hero_cap='Foz do Douro, Porto · drone by Usina Vídeos',
    quem_eb='About us', quem_h2='A journalist’s eye, working for your property.',
    quem_p=['Usina Vídeos is run by <b>Freire Neto</b> and <b>Sandra Freire</b>. Freire Neto has been a journalist since 1997 and founded Motores e Ação, with over 25 years of reporting and video production. Sandra Freire is the video editor.',
            'We treat every property like a story: find what makes it unique, capture it carefully and show it clearly to buyers. The result adds value to the property and to the agent who presents it.',
            'We work across <b>Northern Portugal</b> and <b>anywhere in the country</b>, with travel included in the quote.'],
    stats=[('25+', 'years of journalism'), ('48h', 'photo delivery'), ('72h', 'videos and PDF'), ('PT · EN · ES', 'multilingual presentations')],
    serv_eb='Services', serv_h2='Everything a property needs to be seen.',
    serv_p='Book any service on its own or combine them. We send a quote tailored to the property and its location.',
    servs=[('Photography', 'High-resolution photos with careful composition and light, ready for property portals and social media.'),
           ('Drone video', 'Aerial photos and video that place the property in context: surroundings, views, access and location.'),
           ('Agent-led video', 'The agent presents the property on camera, in vertical and horizontal formats for every platform.'),
           ('3D virtual tour', 'A 360° walk-through with floor plan, for portals and buyers who cannot visit in person.'),
           ('Digital presentation', 'A dedicated web page for the property, with photos, video, map and contacts, to share by WhatsApp or e-mail.'),
           ('Editing and visualisations', 'Colour and light correction on every photo. Furnishing or renovation visualisations, always labelled as such.')],
    medida_h3='Custom productions',
    medida=['Launch videos for new developments', 'Real estate podcasts', 'Live-streamed open houses',
            'Ad campaigns and lead generation', 'Social media content', 'Prepaid production credit, no retainer'],
    orc_h3='Every property is different. So is every quote.',
    orc_p='Tell us the address, the property type and what you need. We reply with a clear proposal, per property or per package, with VAT shown.',
    trab_eb='Work', trab_h2='Recent work, published with permission.',
    works=[('/cordiallevel/', '/cordiallevel/t3leca/img/leca-37-t.jpg', 'Cordial Level', 'Production partner: website, property videos, podcast and social media. ' + AMI, 'See the website'),
           ('/t4coral/en.html', '/img/coral-fachada.jpg', 'Condomínio Coral · Foz do Douro', 'Photography, drone and a digital presentation in four languages. Agent Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414', 'See the presentation'),
           ('/cordiallevel/anteroquental/', '/cordiallevel/anteroquental/img/aq-lapa-t.jpg', 'Two-bedroom flat · Antero de Quental, Porto', 'Photography, drone, 3D tour and property page. ' + AMI, 'See the presentation'),
           ('/cordiallevel/moncao/', '/cordiallevel/moncao/img/t1-area-t.jpg', 'Land in Monção · Alto Minho', 'Drone, video and project visualisations labelled as AI. ' + AMI, 'See the presentation')],
    cdj=('CDJRegio', 'Clube Desportivo José Régio, Vila do Conde. Basketball match coverage and highlights.', 'See on Instagram'),
    como_eb='How it works', como_h2='From request to delivery.',
    steps=[('Quote request', 'Send us the address, the property type and what you need, by WhatsApp or e-mail.'),
           ('Shoot', 'We travel to the property and capture it. A session usually takes up to 1h30.'),
           ('Post-production', 'Selection, photo editing, video editing and assembly of the presentation.'),
           ('Delivery', 'Photos within 48 hours. Videos and PDF within 72 hours.')],
    marcas_eb='Our brands', marcas_h2='We also produce our own content.',
    mea_eb='Featured · a Usina Vídeos brand', mea_p='Automotive journalism since 2002: launches, road tests and offers in Brazil and Portugal.', mea_b='Read on motoreseacao.com',
    dicas=('Dicas do Freire', 'Freire Neto’s YouTube channel (in Portuguese).', 'Watch'),
    ig=('Freire Neto in Portugal', '@neofreireportugal · personal Instagram', 'Follow'),
    cont_eb='Contact', cont_h2='Shall we present your property?',
    cont_p='Ask for a quote, with no obligation, by WhatsApp or e-mail.',
    wa_lbl='WhatsApp', mail_lbl='E-mail', social='Usina on social media',
    foot='Real estate video production · Northern Portugal and nationwide',
    sim='AI visualisations always labelled',
),
'es': dict(
    socials=[('https://www.instagram.com/usina.videos','ig','Usina Vídeos','@usina.videos · últimos trabajos','Seguir'),('https://www.instagram.com/neofreireportugal','ig','Freire Neto en Portugal','@neofreireportugal · Instagram personal','Seguir'),('https://www.instagram.com/freireneto','ig','Freire Neto en Brasil','@freireneto · Instagram','Seguir'),('https://www.instagram.com/motoreseacao','ig','Motores e Ação','@motoreseacao · Instagram','Seguir'),('https://www.linkedin.com/in/freireneto/','in','Freire Neto','LinkedIn','Ver perfil')],
    desp=dict(eb='Deporte', h2='También en la cancha.', p='Reportajes de partidos y torneos de baloncesto, con resúmenes y perfiles de jugadores para redes sociales.', cdj='Clube Desportivo José Régio · Vila do Conde. Resúmenes de los partidos de cantera y sénior.', mb='MatchBall × Red Rose Thunder', mbp='Gira internacional de baloncesto en Portugal. Perfiles y resúmenes de los jugadores.', ver='Ver en Instagram', mais='Ver más en Instagram'),
    path='es/', html_lang='es', og_locale='es_ES',
    title='Usina Vídeos · Producción audiovisual inmobiliaria en Portugal',
    desc='Fotografía, vídeo con dron, reportajes y presentaciones digitales de inmuebles en el Norte y en todo Portugal. Pida presupuesto.',
    nav=[('quem', 'Quiénes somos'), ('servicos', 'Servicios'), ('trabalhos', 'Trabajos'), ('desporto', 'Deporte'), ('como', 'Cómo funciona'), ('marcas', 'Marcas'), ('contacto', 'Contacto')],
    cta='Pida presupuesto',
    wa_msg='Hola Freire, me gustaría pedir un presupuesto a Usina Vídeos.',
    hero_eb='Producción audiovisual inmobiliaria · Norte y todo Portugal',
    hero_h1='El inmueble adecuado merece una buena presentación.',
    hero_p='Fotografía, vídeo con dron, reportajes y presentaciones digitales para agentes inmobiliarios, promotores y propietarios. Una producción, un briefing, un contacto.',
    hero_b2='Ver trabajos',
    hero_cap='Foz do Douro, Oporto · dron de Usina Vídeos',
    quem_eb='Quiénes somos', quem_h2='Mirada de periodista, al servicio del inmueble.',
    quem_p=['Usina Vídeos está dirigida por <b>Freire Neto</b> y <b>Sandra Freire</b>. Freire Neto es periodista desde 1997 y fundador de Motores e Ação, con más de 25 años de reportaje y producción audiovisual. Sandra Freire firma la edición de vídeo.',
            'Tratamos cada inmueble como un reportaje: entender qué lo hace único, captarlo con rigor y contarlo con claridad a quien busca casa. El resultado da valor al inmueble y a quien lo presenta.',
            'Trabajamos en <b>todo el Norte</b> y en <b>cualquier punto de Portugal</b>, con el desplazamiento incluido en el presupuesto.'],
    stats=[('25+', 'años de periodismo'), ('48h', 'entrega de fotografías'), ('72h', 'vídeos y PDF'), ('PT · EN · ES', 'presentaciones multilingües')],
    serv_eb='Servicios', serv_h2='Todo lo que un inmueble necesita para ser visto.',
    serv_p='Cada servicio puede contratarse por separado o combinado. Enviamos un presupuesto adaptado al inmueble y a su ubicación.',
    servs=[('Reportaje fotográfico', 'Fotografía de alta resolución, con composición y luz cuidadas, lista para portales y redes sociales.'),
           ('Vídeo con dron', 'Planos aéreos en foto y vídeo que sitúan el inmueble en su entorno: vistas, accesos y ubicación.'),
           ('Vídeo con el agente', 'El agente presenta el inmueble ante la cámara, en formato vertical y horizontal para todas las plataformas.'),
           ('Visita virtual 3D', 'Visita navegable en 360°, con plano, para portales y compradores a distancia.'),
           ('Presentación digital', 'Una página propia para el inmueble, con fotos, vídeo, mapa y contactos, para enviar por WhatsApp o e-mail.'),
           ('Edición y simulaciones', 'Corrección de color y luz en todas las fotografías. Simulaciones de decoración o de obra, siempre identificadas.')],
    medida_h3='Producciones a medida',
    medida=['Vídeos de lanzamiento de promociones', 'Pódcast inmobiliario', 'Retransmisiones en directo de jornadas de puertas abiertas',
            'Gestión de campañas y captación de contactos', 'Contenidos para redes sociales', 'Bolsa de producciones prepago, sin cuota'],
    orc_h3='Cada inmueble es diferente. El presupuesto también.',
    orc_p='Indíquenos la dirección, la tipología y lo que necesita. Respondemos con una propuesta clara, por inmueble o por paquete, con el IVA indicado.',
    trab_eb='Trabajos', trab_h2='Trabajo reciente, publicado con autorización.',
    works=[('/cordiallevel/', '/cordiallevel/t3leca/img/leca-37-t.jpg', 'Cordial Level', 'Socio de producción: web, vídeo-reportajes, pódcast y redes sociales. ' + AMI, 'Ver la web'),
           ('/t4coral/es.html', '/img/coral-fachada.jpg', 'Condomínio Coral · Foz do Douro', 'Fotografía, dron y presentación digital en cuatro idiomas. Agente Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414', 'Ver la presentación'),
           ('/cordiallevel/anteroquental/', '/cordiallevel/anteroquental/img/aq-lapa-t.jpg', 'Piso de dos dormitorios · Antero de Quental, Oporto', 'Fotografía, dron, visita 3D y página del inmueble. ' + AMI, 'Ver la presentación'),
           ('/cordiallevel/moncao/', '/cordiallevel/moncao/img/t1-area-t.jpg', 'Terrenos en Monção · Alto Minho', 'Dron, vídeo y simulaciones de proyecto identificadas como IA. ' + AMI, 'Ver la presentación')],
    cdj=('CDJRegio', 'Clube Desportivo José Régio, Vila do Conde. Reportajes y resúmenes de los partidos de baloncesto.', 'Ver en Instagram'),
    como_eb='Cómo funciona', como_h2='De la solicitud a la entrega.',
    steps=[('Solicitud de presupuesto', 'Envíenos la dirección, la tipología y lo que necesita, por WhatsApp o e-mail.'),
           ('Producción', 'Nos desplazamos al inmueble y realizamos la captación. Una sesión dura, por lo general, hasta 1h30.'),
           ('Postproducción', 'Selección, edición de imagen, montaje de vídeo y de la presentación.'),
           ('Entrega', 'Fotografías en 48 horas. Vídeos y PDF en 72 horas.')],
    marcas_eb='Nuestras marcas', marcas_h2='También producimos contenido propio.',
    mea_eb='Destacado · una marca de Usina Vídeos', mea_p='Periodismo del motor desde 2002: lanzamientos, pruebas y ofertas en Brasil y Portugal.', mea_b='Leer en motoreseacao.com',
    dicas=('Dicas do Freire', 'El canal de Freire Neto en YouTube (en portugués).', 'Ver el canal'),
    ig=('Freire Neto en Portugal', '@neofreireportugal · Instagram personal', 'Seguir'),
    cont_eb='Contacto', cont_h2='¿Presentamos su inmueble?',
    cont_p='Pida presupuesto sin compromiso, por WhatsApp o e-mail.',
    wa_lbl='WhatsApp', mail_lbl='E-mail', social='Redes de Usina',
    foot='Producción audiovisual inmobiliaria · Norte y todo Portugal',
    sim='Simulaciones IA siempre identificadas',
),
}

CSS = r"""
:root{--ink:#141213;--ink2:#1E1B1C;--line:#34302F;--paper:#F7F5F0;--paper2:#EFEBE4;--fg:#F2F0EB;--muted:#A9A3A0;--txt:#3B3634;--y:#E5AE29;--r:#D0252F;--g:#3EB15C;--mea:#004D9A;--mea-l:#2F7FD0}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:72px}
body{margin:0;font-family:Mulish,system-ui,sans-serif;color:var(--txt);background:var(--paper);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums}
a{color:inherit}img{max-width:100%;display:block}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}
.eb{display:block;font-size:12px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--r)}
.dark .eb{color:var(--y)}
h1,h2,h3{font-weight:900;line-height:1.08;letter-spacing:-.01em;margin:0;color:var(--ink)}
.dark h1,.dark h2,.dark h3{color:var(--fg)}
h2{font-size:clamp(30px,4.2vw,46px);margin-top:10px;max-width:22ch}
.lead{font-size:18px;max-width:62ch;margin:16px 0 0}
section{padding:88px 0}
.dark{background:var(--ink);color:#D6D1CD}
.btn{display:inline-flex;align-items:center;gap:8px;padding:15px 24px;border-radius:999px;font-weight:800;font-size:16px;text-decoration:none;line-height:1.1}
.btn.y{background:var(--y);color:var(--ink)}.btn.y:hover{filter:brightness(1.08)}
.btn.o{border:2px solid currentColor}
/* nav */
.nav{position:sticky;top:0;z-index:20;background:rgba(20,18,19,.96);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav .wrap{display:flex;align-items:center;gap:18px;height:64px}
.nav .logo img{height:30px;width:auto}
.nav .links{display:flex;gap:18px;margin-left:auto;overflow-x:auto;scrollbar-width:none}
.nav .links::-webkit-scrollbar{display:none}
.nav .links a{color:#D6D1CD;text-decoration:none;font-size:14px;font-weight:700;white-space:nowrap}
.nav .links a:hover{color:var(--y)}
.lang{display:flex;gap:2px;font-size:12px;font-weight:800}
.lang a{color:var(--muted);text-decoration:none;padding:4px 6px;border-radius:6px}
.lang a[aria-current]{color:var(--ink);background:var(--y)}
.nav .btn{padding:10px 16px;font-size:14px}
@media(max-width:900px){.nav .links{display:none}.nav .wrap{gap:10px}.nav .lang{margin-left:auto}}
@media(max-width:420px){.nav .btn{display:none}}
/* hero */
.hero{position:relative;min-height:min(86vh,760px);display:flex;align-items:flex-end;background:var(--ink);overflow:hidden}
.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.62}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,18,19,.15) 0,rgba(20,18,19,.55) 55%,var(--ink) 100%)}
.hero .wrap{position:relative;z-index:1;padding-bottom:64px;padding-top:120px}
.hero h1{font-size:clamp(40px,6.4vw,78px);max-width:16ch;margin-top:14px}
.hero p{color:#E4DFDB;font-size:clamp(17px,1.6vw,20px);max-width:56ch;margin:20px 0 0}
.hero .row{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.hero .btn.o{color:#fff}
.stripe{display:flex;width:120px;height:5px;border-radius:3px;overflow:hidden;margin-top:26px}.stripe i{flex:1}
.cap{position:absolute;right:20px;bottom:16px;z-index:1;font-size:12px;color:rgba(255,255,255,.65)}
/* quem */
.two{display:grid;gap:40px}
@media(min-width:900px){.two{grid-template-columns:1.25fr 1fr;gap:64px;align-items:start}}
.two p{margin:0 0 16px}.two b{color:var(--ink)}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border-radius:14px;overflow:hidden}
.stats div{background:var(--ink);padding:22px 20px}
.stats b{display:block;font-size:30px;font-weight:900;color:var(--y);line-height:1}
.stats span{font-size:13px;color:#C9C3BF}
/* serviços */
.grid3{display:grid;gap:16px;margin-top:40px}
@media(min-width:700px){.grid3{grid-template-columns:1fr 1fr}}
@media(min-width:1000px){.grid3{grid-template-columns:1fr 1fr 1fr}}
.card{background:#fff;border:1px solid #E3DED6;border-radius:16px;padding:24px;border-top:4px solid var(--c,var(--y))}
.card .n{font-size:13px;font-weight:900;color:var(--c,var(--y))}
.card h3{font-size:22px;margin-top:8px}.card p{margin:10px 0 0;font-size:16px}
.orc{display:grid;gap:28px;margin-top:28px;background:var(--ink);color:#D6D1CD;border-radius:20px;padding:32px}
@media(min-width:900px){.orc{grid-template-columns:1fr 1fr;padding:44px;gap:48px}}
.orc h3{color:var(--fg);font-size:28px}.orc p{margin:12px 0 22px}
.orc ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.orc li{padding-left:22px;position:relative}.orc li::before{content:"";position:absolute;left:0;top:.62em;width:10px;height:10px;border-radius:50%;background:var(--y)}
.orc h4{margin:0 0 14px;color:var(--fg);font-size:15px;letter-spacing:.16em;text-transform:uppercase}
.tag{display:inline-block;margin-top:18px;font-size:12px;font-weight:800;letter-spacing:.08em;color:var(--ink);background:var(--paper2);padding:6px 12px;border-radius:999px}
/* trabalhos */
.works{display:grid;gap:18px;margin-top:40px}
@media(min-width:760px){.works{grid-template-columns:1fr 1fr}}
.work{display:flex;flex-direction:column;background:var(--ink2);border:1px solid var(--line);border-radius:18px;overflow:hidden;text-decoration:none;color:#D6D1CD}
.work .ph{aspect-ratio:16/10;overflow:hidden;background:#000}.work .ph img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.work:hover .ph img{transform:scale(1.04)}
.work .bd{padding:22px 22px 24px;display:flex;flex-direction:column;gap:8px;flex:1}
.work h3{font-size:22px}.work p{margin:0;font-size:15px}
.work em{font-style:normal;font-weight:800;color:var(--y);margin-top:auto;padding-top:8px}
.work.cdj{border-top:4px solid var(--r)}.work.cdj .bd{justify-content:center}.work.cdj em{color:var(--r)}
.work.cdj .big{font-size:40px;font-weight:900;color:var(--fg);line-height:1}
@media(min-width:760px){.work.cdj{grid-column:span 2}}
/* desporto */
.sport{display:grid;gap:18px;margin-top:36px;align-items:start}
@media(min-width:760px){.sport{grid-template-columns:1fr 1fr}}
.sport{max-width:900px}.spmore{margin-top:28px}
.sph{background:var(--ink);color:#D6D1CD;border-radius:16px;padding:20px;border-top:4px solid var(--c);margin-bottom:14px}
.sph b{display:block;color:var(--fg);font-size:22px;font-weight:900;line-height:1.1}.sph p{margin:8px 0 10px;font-size:15px}
.sph a{color:var(--y);font-weight:800;font-size:14px;text-decoration:none}
.sp.more{padding-top:0}
@media(min-width:1100px){.sp.more{margin-top:0}}
/* como */
.steps{display:grid;gap:16px;margin-top:40px;counter-reset:s}
@media(min-width:800px){.steps{grid-template-columns:repeat(4,1fr)}}
.step{border-top:3px solid var(--ink);padding-top:16px;counter-increment:s}
.step::before{content:counter(s,decimal-leading-zero);font-weight:900;font-size:14px;color:var(--r)}
.step h3{font-size:20px;margin-top:6px}.step p{margin:8px 0 0;font-size:15px}
/* marcas */
.brands{display:grid;gap:16px;margin-top:40px;align-items:start}
@media(min-width:900px){.brands{grid-template-columns:1.4fr 1fr}}
.mea{display:block;text-decoration:none;color:#fff;background:radial-gradient(520px 260px at 100% 0%,rgba(0,77,154,.55),transparent 70%),#0B0E14;border:1px solid rgba(47,127,208,.45);border-radius:18px;padding:30px 28px}
.mea small{display:block;font-size:12px;letter-spacing:.2em;font-weight:800;color:var(--mea-l);text-transform:uppercase}
.mea img{width:min(300px,70vw);height:auto;margin-top:16px;filter:brightness(0) invert(1)}
.mea p{margin:14px 0 0;color:#C9CFD8}
.mea b{display:inline-block;margin-top:20px;background:var(--mea);color:#fff;font-weight:800;font-size:15px;padding:12px 20px;border-radius:999px}
.mea:hover b{background:var(--mea-l)}
.side{display:grid;gap:16px}
.mini{display:flex;align-items:center;gap:14px;padding:20px;border-radius:16px;background:var(--ink2);border:1px solid var(--line);text-decoration:none;color:#D6D1CD}
.mini b{display:block;color:var(--fg);font-size:17px}.mini span{font-size:14px}
.mini em{margin-left:auto;font-style:normal;font-weight:800;font-size:14px;color:var(--y);white-space:nowrap}
.mini.ig{background:linear-gradient(var(--ink2),var(--ink2)) padding-box,linear-gradient(90deg,var(--y),var(--r),#8a3ab9) border-box;border:2px solid transparent}
.mini.yt em{color:var(--r)}
.mini.in{border-color:rgba(10,102,194,.6)}.mini.in em{color:#5AA3E8}
.side{grid-template-columns:1fr}@media(min-width:600px) and (max-width:899px){.side{grid-template-columns:1fr 1fr}}
/* contacto */
.contact{display:grid;gap:14px;margin-top:32px}
@media(min-width:800px){.contact{grid-template-columns:repeat(3,1fr)}}
.contact a{display:block;padding:22px;border-radius:16px;background:#fff;border:1px solid #E3DED6;text-decoration:none}
.contact a.wa{background:var(--y);border-color:var(--y)}
.contact small{display:block;font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--r)}
.contact a.wa small{color:var(--ink)}
.contact b{display:block;font-size:20px;color:var(--ink);margin-top:6px;word-break:break-word}
.contact span{font-size:14px}
footer{background:var(--ink);color:var(--muted);padding:36px 0;font-size:14px}
footer .wrap{display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between}
footer img{height:30px;width:auto}
footer a{color:#D6D1CD}
"""

WA_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/></svg>'
IG_SVG = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#E5AE29" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="#E5AE29"/></svg>'
YT_SVG = '<svg width="34" height="34" viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="4" fill="#D0252F"/><path d="M10 9v6l5-3z" fill="#fff"/></svg>'
IN_SVG = '<svg width="34" height="34" viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="4" fill="#0A66C2"/><path d="M7 10v7M7 7v.01M11 17v-4a2 2 0 0 1 4 0v4M11 10v7" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>'
STRIPE = '<div class="stripe" aria-hidden="true"><i style="background:var(--g)"></i><i style="background:var(--y)"></i><i style="background:var(--r)"></i></div>'
COLORS = ['var(--y)', 'var(--r)', 'var(--g)']


def ig_embed(code):
    u = f'https://www.instagram.com/p/{code}/'
    return (f'<blockquote class="instagram-media" data-instgrm-permalink="{u}?utm_source=ig_embed" data-instgrm-version="14" '
            f'style="background:#fff;border:0;border-radius:14px;margin:0;max-width:540px;min-width:280px;width:100%"><a href="{u}" target="_blank" rel="noopener">Instagram</a></blockquote>')


def page(lang):
    t = T[lang]
    wa = f'https://wa.me/{WA_NUM}?text=' + up.quote(t['wa_msg'])
    canon = 'https://usinavideos.pt/' + t['path']
    alts = ''.join(f'<link rel="alternate" hreflang="{T[l]["html_lang"]}" href="https://usinavideos.pt/{T[l]["path"]}">' for l in T)
    langsw = ''.join(f'<a href="/{T[l]["path"]}" hreflang="{T[l]["html_lang"]}"{" aria-current=\"page\"" if l == lang else ""}>{l.upper()}</a>' for l in T)
    nav = ''.join(f'<a href="#{a}">{e(b)}</a>' for a, b in t['nav'])
    servs = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for i, (a, b) in enumerate(t['servs']))
    medida = ''.join(f'<li>{e(x)}</li>' for x in t['medida'])
    works = ''.join(f'<a class="work" href="{h}"><div class="ph"><img src="{im}" alt="{e(ti)}" loading="lazy" width="900" height="563"></div><div class="bd"><h3>{e(ti)}</h3><p>{e(d)}</p><em>{e(c)} →</em></div></a>' for h, im, ti, d, c in t['works'])
    cn, cd, cc = t['cdj']
    steps = ''.join(f'<div class="step"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in t['steps'])
    stats = ''.join(f'<div><b>{a}</b><span>{e(b)}</span></div>' for a, b in t['stats'])
    quem = ''.join(f'<p>{x}</p>' for x in t['quem_p'])
    socials = ''.join(f'<a class="mini {k}" href="{u}" target="_blank" rel="noopener">{IG_SVG if k == "ig" else IN_SVG}<div><b>{e(a)}</b><span>{e(b)}</span></div><em>{e(c)} →</em></a>' for u, k, a, b, c in t['socials'])
    return f'''<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{canon}">{alts}
<meta property="og:title" content="{e(t['title'])}"><meta property="og:description" content="{e(t['desc'])}">
<meta property="og:image" content="https://usinavideos.pt/img/logo/usina-horizontal-1200.png"><meta property="og:locale" content="{t['og_locale']}">
<meta name="theme-color" content="#141213">
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/img/logo/usina-simbolo-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Menu"><div class="wrap">
  <a class="logo" href="/{t['path']}"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
  <div class="links">{nav}</div>
  <div class="lang">{langsw}</div>
  <a class="btn y" href="{wa}" target="_blank" rel="noopener">{e(t['cta'])}</a>
</div></nav>

<header class="hero dark">
  <img src="/img/foz-drone.jpg" alt="" fetchpriority="high">
  <div class="wrap">
    <span class="eb">{e(t['hero_eb'])}</span>
    <h1>{e(t['hero_h1'])}</h1>
    <p>{e(t['hero_p'])}</p>
    <div class="row"><a class="btn y" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{e(t['cta'])}</a><a class="btn o" href="#trabalhos">{e(t['hero_b2'])}</a></div>
    {STRIPE}
  </div>
  <span class="cap">{e(t['hero_cap'])}</span>
</header>

<section id="quem">
  <div class="wrap two">
    <div><span class="eb">{e(t['quem_eb'])}</span><h2>{e(t['quem_h2'])}</h2><div style="margin-top:22px">{quem}</div></div>
    <div class="stats">{stats}</div>
  </div>
</section>

<section id="servicos" style="background:var(--paper2)">
  <div class="wrap">
    <span class="eb">{e(t['serv_eb'])}</span><h2>{e(t['serv_h2'])}</h2><p class="lead">{e(t['serv_p'])}</p>
    <div class="grid3">{servs}</div>
    <div class="orc">
      <div><h3>{e(t['orc_h3'])}</h3><p>{e(t['orc_p'])}</p><a class="btn y" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{e(t['cta'])}</a></div>
      <div><h4>{e(t['medida_h3'])}</h4><ul>{medida}</ul></div>
    </div>
    <span class="tag">{e(t['sim'])}</span>
  </div>
</section>

<section id="trabalhos" class="dark">
  <div class="wrap">
    <span class="eb">{e(t['trab_eb'])}</span><h2>{e(t['trab_h2'])}</h2>
    <div class="works">{works}</div>
  </div>
</section>

<section id="desporto" style="background:var(--paper2)">
  <div class="wrap">
    <span class="eb">{e(t['desp']['eb'])}</span><h2>{e(t['desp']['h2'])}</h2><p class="lead">{e(t['desp']['p'])}</p>
    <div class="sport">
      <div class="sp"><div class="sph" style="--c:var(--r)"><b>CDJRegio</b><p>{e(t['desp']['cdj'])}</p><a href="https://www.instagram.com/cdjregio/" target="_blank" rel="noopener">@cdjregio · {e(t['desp']['ver'])} →</a></div>{ig_embed('Deri9uUiObc')}</div>
      <div class="sp"><div class="sph" style="--c:var(--g)"><b>{e(t['desp']['mb'])}</b><p>{e(t['desp']['mbp'])}</p><a href="https://www.instagram.com/matchballbasketball/" target="_blank" rel="noopener">@matchballbasketball · {e(t['desp']['ver'])} →</a></div>{ig_embed('DY-tmeisiO0')}</div>
    </div>
    <div class="spmore"><a class="btn y" href="https://www.instagram.com/usina.videos/" target="_blank" rel="noopener">{e(t['desp']['mais'])} →</a></div>
  </div>
</section>
<script async src="https://www.instagram.com/embed.js"></script>

<section id="como">
  <div class="wrap">
    <span class="eb">{e(t['como_eb'])}</span><h2>{e(t['como_h2'])}</h2>
    <div class="steps">{steps}</div>
  </div>
</section>

<section id="marcas" class="dark">
  <div class="wrap">
    <span class="eb">{e(t['marcas_eb'])}</span><h2>{e(t['marcas_h2'])}</h2>
    <div class="brands">
      <a class="mea" href="https://motoreseacao.com/?utm_source=usinavideos&amp;utm_medium=banner&amp;utm_campaign=destaque_home" target="_blank" rel="noopener">
        <small>{e(t['mea_eb'])}</small>
        <img src="https://motoreseacao.com/wp-content/uploads/2021/10/cropped-Motores-e-Acao.png" alt="Motores e Ação" width="1000" height="286" loading="lazy">
        <p>{e(t['mea_p'])}</p><b>{e(t['mea_b'])} →</b></a>
      <div class="side">
        {socials}
        <a class="mini yt" href="https://www.youtube.com/@DicasdoFreire/" target="_blank" rel="noopener">{YT_SVG}<div><b>{e(t['dicas'][0])}</b><span>{e(t['dicas'][1])}</span></div><em>{e(t['dicas'][2])} →</em></a>
        <a class="mini yt" href="https://www.youtube.com/@motoreseacao" target="_blank" rel="noopener">{YT_SVG}<div><b>Motores e Ação</b><span>YouTube · @motoreseacao</span></div><em>{e(t['dicas'][2])} →</em></a>
      </div>
    </div>
  </div>
</section>

<section id="contacto">
  <div class="wrap">
    <span class="eb">{e(t['cont_eb'])}</span><h2>{e(t['cont_h2'])}</h2><p class="lead">{e(t['cont_p'])}</p>
    <div class="contact">
      <a class="wa" href="{wa}" target="_blank" rel="noopener"><small>{e(t['wa_lbl'])}</small><b>+351 912 988 971</b><span>{e(t['cta'])} →</span></a>
      <a href="mailto:{MAIL}?subject={up.quote(t['cta'] + ' · Usina Vídeos')}"><small>{e(t['mail_lbl'])}</small><b>{MAIL}</b></a>
      <a href="https://www.instagram.com/usina.videos" target="_blank" rel="noopener"><small>{e(t['social'])}</small><b>@usina.videos</b><span>Instagram · Facebook /usinacomvideos</span></a>
    </div>
  </div>
</section>

<footer><div class="wrap">
  <img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298">
  <span>© Usina Vídeos · {e(t['foot'])} · <a href="https://www.facebook.com/usinacomvideos" target="_blank" rel="noopener">Facebook</a></span>
</div></footer>
</body>
</html>
'''


if __name__ == '__main__':
    for lang, t in T.items():
        d = os.path.join(ROOT, t['path'])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'index.html'), 'w') as f:
            f.write(page(lang))
        print('ok', lang)
