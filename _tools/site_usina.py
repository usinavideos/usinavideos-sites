#!/usr/bin/env python3
"""Site institucional da Usina Vídeos em PT, EN e ES.

Uso: python3 _tools/site_usina.py   -> escreve index.html, en/index.html, es/index.html
Regras: sem preços (pedido de orçamento); simulações IA sempre identificadas;
anúncios Cordial Level sempre com "CENTURY 21 Arquitectos · AMI 11414".
"""
import html, os, sys, urllib.parse as up
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mea_banner import mea_banner, MEA_CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WA_NUM = '351912988971'
MAIL = 'freireneto@me.com'
AMI = 'Cordial Level | CENTURY 21 Arquitectos · AMI 11414'
e = html.escape

T = {
'pt': dict(
    socials=[('https://www.instagram.com/usina.videos','ig','Usina Vídeos','@usina.videos · últimos trabalhos','Seguir'),('https://www.instagram.com/neofreireportugal','ig','Freire Neto em Portugal','@neofreireportugal · Instagram pessoal','Seguir'),('https://www.instagram.com/freireneto','ig','Freire Neto no Brasil','@freireneto · Instagram','Seguir'),('https://www.instagram.com/motoreseacao','ig','Motores e Ação','@motoreseacao · Instagram','Seguir'),('https://www.linkedin.com/in/freireneto/','in','Freire Neto','LinkedIn','Ver perfil')],
    desp=dict(eb='Desporto', h2='Também no pavilhão.', p='Reportagem de jogos e torneios de basquetebol, com destaques e perfis de jogadores para as redes sociais.', cdj='Clube Desportivo José Régio · Vila do Conde. Destaques dos jogos da formação e dos seniores.', mb='MatchBall × Red Rose Thunder', mbp='Tour internacional de basquetebol em Portugal. Perfis e destaques dos jogadores.', ver='Ver no Instagram', mais='Ver mais no Instagram'),
    sites={'nav': 'Sites', 'eb': 'Sites, apresentações e podcasts', 'h2': 'Soluções digitais para o seu negócio.', 'p': 'Além do vídeo, criamos as ferramentas onde ele vive: sites, apresentações e podcasts, com a mesma qualidade de reportagem.', 'items': [('Sites', 'Sites para agências, consultores e marcas, com carteira de imóveis, vídeos e contacto direto por WhatsApp.', [('Cordial Level', '/cordiallevel/')]), ('Apresentações digitais', 'Uma página por imóvel ou projeto, em várias línguas, para enviar por link, imprimir em PDF ou mostrar em reunião.', [('Condomínio Coral', '/t4coral/'), ('T3 Leça', '/cordiallevel/t3leca/')]), ('Podcasts', 'Formato, gravação, edição e publicação no YouTube e no Spotify, com cortes para as redes sociais.', [('Panorama Imobiliário PT', 'https://www.youtube.com/watch?v=ed1kwc3x27I')])], 'ex': 'Exemplo'},
    ig_cl='Em destaque no Instagram da Cordial Level',
    agenda={'nav': 'Agenda', 'eb': 'Agenda', 'h2': 'Agenda aberta para o final de outubro e novembro.', 'p': 'Escolha o dia e a hora da sua sessão diretamente no nosso calendário. Prefere falar primeiro? Envie-nos uma mensagem pelo WhatsApp.', 'alt': 'Abrir o calendário numa nova janela'},
    path='', html_lang='pt-PT', og_locale='pt_PT',
    title='Usina Vídeos · Produtora de conteúdo e comunicação em Portugal',
    desc='Vídeo, fotografia, drone, conteúdo para redes, sites e campanhas digitais para empresas, marcas e profissionais. Imobiliário, automóvel, desporto, turismo e negócios, no Norte e em todo o Portugal. Peça orçamento.',
    nav=[('quem', 'Quem somos'), ('servicos', 'Serviços'), ('trabalhos', 'Trabalhos'), ('sites', 'Sites'), ('desporto', 'Desporto'), ('como', 'Como funciona'), ('marcas', 'Marcas'), ('agenda', 'Agenda'), ('contacto', 'Contacto')],
    cta='Peça orçamento',
    wa_msg='Olá Freire, gostaria de pedir um orçamento à Usina Vídeos.',
    hero_eb='Produtora de conteúdo e comunicação · Norte e todo o Portugal',
    hero_h1='Comunicação que se vê. Conteúdo que gera resultados.',
    hero_p='Vídeo, fotografia, drone, redes sociais, sites e campanhas digitais para empresas, marcas e profissionais. Do imobiliário ao automóvel, do desporto ao turismo: uma produção, um briefing, um contacto.',
    hero_b2='Ver trabalhos',
    hero_cap='Foz do Douro, Porto · drone Usina Vídeos',
    team=[('Freire Neto', 'Direção, reportagem e imagem', 'Jornalista desde 1997, ex-diretor de conteúdo e produção do Canal 10 da TCM Mossoró e fundador do Motores e Ação.'), ('Sandra Freire', 'Edição, produção e administração', '20 anos em televisão, produtoras e no Motores e Ação.')],
    quem_eb='Quem somos', quem_h2='Olhar de jornalista, ao serviço da sua comunicação.',
    quem_p=['A Usina Vídeos é dirigida por <b>Freire Neto</b> e <b>Sandra Freire</b>. Freire Neto é jornalista desde 1997 e fundador do Motores e Ação, com mais de 25 anos de reportagem e produção audiovisual. Foi diretor de conteúdo, de produção e de emissões em direto do Canal 10 da TCM Mossoró, no Brasil, onde criou soluções de comunicação para empresas e instituições: centros comerciais como o Partage Shopping, hospitais, clínicas, médicos, clubes e eventos. Sandra Freire é responsável pela edição, produção e administração, com 20 anos de experiência em televisão, produtoras e no Motores e Ação.',
            'Somos uma produtora de conteúdo e comunicação. Tratamos cada projeto como uma reportagem: perceber o que o torna único, captá-lo com rigor e contá-lo de forma clara a quem precisa de o ver. Audiovisual e marketing digital ao serviço de imóveis, marcas, eventos, equipas e pessoas.',
            'Trabalhamos em <b>todo o Norte</b> e em <b>qualquer ponto de Portugal</b>, com a deslocação incluída no orçamento.'],
    stats=[('25+', 'anos de jornalismo'), ('48h', 'entrega de fotografias'), ('72h', 'vídeos editados'), ('PT · EN · ES', 'conteúdos multilingues')],
    serv_eb='Serviços', serv_h2='Tudo o que a sua mensagem precisa para ser vista.',
    serv_p='Cada serviço pode ser contratado isoladamente ou combinado. Enviamos orçamento à medida do projeto e do local.',
    servs=[('Vídeo e reportagem', 'Vídeos institucionais, reportagens, entrevistas, eventos e making of, em formato horizontal e vertical.'),
           ('Fotografia', 'Fotografia de alta resolução para imóveis, produtos, eventos, equipas e retratos profissionais.'),
           ('Drone', 'Planos aéreos em foto e vídeo para imóveis, turismo, eventos e desporto.'),
           ('Conteúdo para redes sociais', 'Reels, shorts, carrosséis e posts, com a voz da sua marca e regularidade.'),
           ('Sites e páginas', 'Sites, landing pages e apresentações digitais em várias línguas, prontos a partilhar e a captar contactos.'),
           ('Campanhas e marketing digital', 'Gestão de anúncios no Facebook e no Instagram, estratégia de conteúdo e geração de contactos.')],
    medida_h3='Áreas em que trabalhamos',
    medida=['Imobiliário: consultores, agências e empreendimentos', 'Automóvel: stands, marcas, lançamentos e testes', 'Desporto: clubes, atletas e jogos',
            'Comércio, lojas e centros comerciais', 'Empresas, saúde e instituições', 'Turismo, viagens e eventos', 'Pessoas e profissionais: imagem e marca pessoal'],
    orc_h3='Cada projeto é diferente. O orçamento também.',
    orc_p='Diga-nos o que pretende comunicar, onde e para quem. Respondemos com uma proposta clara, por projeto ou por pacote, com o IVA indicado.',
    trab_eb='Trabalhos', trab_h2='Trabalho recente, em várias áreas, publicado com autorização.',
    works=[('/cordiallevel/', '/cordiallevel/t3leca/img/leca-37-t.jpg', 'Cordial Level', 'Parceiro de produção: site, vídeo-reportagens, podcast e redes sociais. ' + AMI, 'Ver o site'),
           ('/t4coral/', '/img/coral-fachada.jpg', 'Condomínio Coral · Foz do Douro', 'Fotografia, drone, vídeo com a consultora e apresentação digital em quatro línguas. Consultora Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414', 'Ver a apresentação'),
           ('https://century21.pt/ref/C0554-00006', '/img/core-devesas-t.jpg', 'CENTURY 21 Core · Vila Nova de Gaia', 'Fotografia e vídeo de uma moradia T5 nas Devesas (consultor Vasco Dinis) e de um T3 em Oliveira do Douro.', 'Ver o anúncio'),
           ('https://www.motoreseacao.com/?utm_source=usinavideos&utm_medium=trabalhos&utm_campaign=usina', '/img/mea-toro.jpg', 'Motores e Ação · Automóvel', 'Jornalismo automóvel desde 2002: testes, lançamentos e conteúdos para marcas, no Brasil e em Portugal. Mais de 115 mil inscritos no YouTube.', 'Ver o site'),
           ('/cordiallevel/moncao/', '/cordiallevel/moncao/img/t1-area-t.jpg', 'Terrenos em Monção · Alto Minho', 'Drone, vídeo e simulações de projeto identificadas como IA. ' + AMI, 'Ver a apresentação'),
           ('https://www.youtube.com/watch?v=ed1kwc3x27I', 'https://i.ytimg.com/vi/ed1kwc3x27I/hqdefault.jpg', 'Panorama Imobiliário PT', 'O podcast da Cordial Level no YouTube, sobre o mercado e as decisões de quem compra casa. Produção e edição Usina Vídeos.', 'Ver no YouTube')],
    cdj=('CDJRegio', 'Clube Desportivo José Régio, Vila do Conde. Reportagem e destaques dos jogos de basquetebol.', 'Ver no Instagram'),
    como_eb='Como funciona', como_h2='Do pedido à entrega.',
    steps=[('Pedido de orçamento', 'Conte-nos o projeto, o local e o objetivo, por WhatsApp ou e-mail.'),
           ('Produção', 'Planeamos consigo e fazemos a captação no local: imóvel, evento, empresa ou exterior.'),
           ('Pós-produção', 'Seleção, tratamento de imagem, edição de vídeo, legendas e versões para cada plataforma.'),
           ('Entrega e divulgação', 'Fotografias em 48 horas, vídeos em 72 horas. Se quiser, publicamos e promovemos por si.')],
    marcas_eb='As nossas marcas', marcas_h2='Também produzimos conteúdo próprio.',
    mea_eb='Em destaque · uma marca Usina Vídeos', mea_p='Jornalismo automóvel desde 2002: lançamentos, testes e ofertas no Brasil e em Portugal.', mea_b='Ler no motoreseacao.com',
    dicas=('Dicas do Freire', 'O canal de Freire Neto no YouTube.', 'Ver o canal'),
    ig=('Freire Neto em Portugal', '@neofreireportugal · Instagram pessoal', 'Seguir'),
    cont_eb='Contacto', cont_h2='Vamos comunicar o seu projeto?',
    cont_p='Peça orçamento sem compromisso, por WhatsApp ou e-mail.',
    wa_lbl='WhatsApp', mail_lbl='E-mail', social='Redes da Usina',
    foot='Produtora de conteúdo e comunicação · Norte e todo o Portugal',
    sim='Simulações IA sempre identificadas',
),
'en': dict(
    socials=[('https://www.instagram.com/usina.videos','ig','Usina Vídeos','@usina.videos · latest work','Follow'),('https://www.instagram.com/neofreireportugal','ig','Freire Neto in Portugal','@neofreireportugal · personal Instagram','Follow'),('https://www.instagram.com/freireneto','ig','Freire Neto in Brazil','@freireneto · Instagram','Follow'),('https://www.instagram.com/motoreseacao','ig','Motores e Ação','@motoreseacao · Instagram','Follow'),('https://www.linkedin.com/in/freireneto/','in','Freire Neto','LinkedIn','View profile')],
    desp=dict(eb='Sport', h2='Courtside, too.', p='Basketball games and tournaments covered on video, with highlights and player profiles for social media.', cdj='Clube Desportivo José Régio · Vila do Conde. Highlights from youth and senior games.', mb='MatchBall × Red Rose Thunder', mbp='International basketball tour in Portugal. Player profiles and highlights.', ver='View on Instagram', mais='See more on Instagram'),
    sites={'nav': 'Websites', 'eb': 'Websites, presentations and podcasts', 'h2': 'Digital solutions for your business.', 'p': 'Beyond video, we build the places where it lives: websites, presentations and podcasts, with the same reporting quality.', 'items': [('Websites', 'Websites for agencies, agents and brands, with property listings, videos and direct WhatsApp contact.', [('Cordial Level', '/cordiallevel/')]), ('Digital presentations', 'One page per property or project, in several languages, to share by link, print as PDF or show in meetings.', [('Condomínio Coral', '/t4coral/en.html'), ('T3 Leça', '/cordiallevel/t3leca/')]), ('Podcasts', 'Format, recording, editing and publishing on YouTube and Spotify, with short clips for social media.', [('Panorama Imobiliário PT', 'https://www.youtube.com/watch?v=ed1kwc3x27I')])], 'ex': 'Example'},
    ig_cl='Featured on Cordial Level’s Instagram',
    agenda={'nav': 'Booking', 'eb': 'Booking', 'h2': 'Now booking for late October and November.', 'p': 'Pick the day and time of your shoot directly in our calendar. Prefer to talk first? Send us a WhatsApp message.', 'alt': 'Open the calendar in a new window'},
    path='en/', html_lang='en', og_locale='en_GB',
    title='Usina Vídeos · Content and communication agency in Portugal',
    desc='Video, photography, drone, social media content, websites and digital campaigns for companies, brands and professionals. Real estate, automotive, sport, tourism and business, across Northern Portugal and nationwide. Ask for a quote.',
    nav=[('quem', 'About'), ('servicos', 'Services'), ('trabalhos', 'Work'), ('sites', 'Websites'), ('desporto', 'Sport'), ('como', 'How it works'), ('marcas', 'Brands'), ('agenda', 'Booking'), ('contacto', 'Contact')],
    cta='Ask for a quote',
    wa_msg='Hello Freire, I would like a quote from Usina Vídeos.',
    hero_eb='Content and communication agency · Northern Portugal and nationwide',
    hero_h1='Communication you can see. Content that delivers.',
    hero_p='Video, photography, drone, social media, websites and digital campaigns for companies, brands and professionals. From real estate to cars, from sport to tourism: one production, one brief, one contact.',
    hero_b2='See our work',
    hero_cap='Foz do Douro, Porto · drone by Usina Vídeos',
    team=[('Freire Neto', 'Direction, reporting and camera', 'Journalist since 1997, former head of content and production at TCM Mossoró’s Channel 10 and founder of Motores e Ação.'), ('Sandra Freire', 'Editing, production and administration', '20 years in television, production companies and Motores e Ação.')],
    quem_eb='About us', quem_h2='A journalist’s eye, working for your communication.',
    quem_p=['Usina Vídeos is run by <b>Freire Neto</b> and <b>Sandra Freire</b>. Freire Neto has been a journalist since 1997 and founded Motores e Ação, with over 25 years of reporting and video production. He was director of content, production and live broadcasts at TCM Mossoró’s Channel 10 in Brazil, where he built communication solutions for companies and institutions: shopping centres such as Partage Shopping, hospitals, clinics, doctors, clubs and events. Sandra Freire runs editing, production and administration, with 20 years of experience in television, production companies and Motores e Ação.',
            'We are a content and communication agency. We treat every project like a story: find what makes it unique, capture it carefully and show it clearly to the people who need to see it. Video and digital marketing for properties, brands, events, teams and people.',
            'We work across <b>Northern Portugal</b> and <b>anywhere in the country</b>, with travel included in the quote.'],
    stats=[('25+', 'years of journalism'), ('48h', 'photo delivery'), ('72h', 'edited videos'), ('PT · EN · ES', 'multilingual content')],
    serv_eb='Services', serv_h2='Everything your message needs to be seen.',
    serv_p='Book any service on its own or combine them. We send a quote tailored to the project and its location.',
    servs=[('Video and reporting', 'Corporate videos, reports, interviews, events and behind-the-scenes, in horizontal and vertical formats.'),
           ('Photography', 'High-resolution photography for properties, products, events, teams and professional portraits.'),
           ('Drone', 'Aerial photos and video for real estate, tourism, events and sport.'),
           ('Social media content', 'Reels, shorts, carousels and posts, in your brand’s voice and on a regular schedule.'),
           ('Websites and pages', 'Websites, landing pages and multilingual digital presentations, ready to share and to capture leads.'),
           ('Campaigns and digital marketing', 'Facebook and Instagram ad management, content strategy and lead generation.')],
    medida_h3='Areas we work in',
    medida=['Real estate: agents, agencies and developments', 'Automotive: dealerships, brands, launches and road tests', 'Sport: clubs, athletes and games',
            'Retail, shops and shopping centres', 'Companies, healthcare and institutions', 'Tourism, travel and events', 'People and professionals: image and personal brand'],
    orc_h3='Every project is different. So is every quote.',
    orc_p='Tell us what you want to communicate, where and to whom. We reply with a clear proposal, per project or per package, with VAT shown.',
    trab_eb='Work', trab_h2='Recent work across several areas, published with permission.',
    works=[('/cordiallevel/', '/cordiallevel/t3leca/img/leca-37-t.jpg', 'Cordial Level', 'Production partner: website, property videos, podcast and social media. ' + AMI, 'See the website'),
           ('/t4coral/en.html', '/img/coral-fachada.jpg', 'Condomínio Coral · Foz do Douro', 'Photography, drone, a video with the agent and a digital presentation in four languages. Agent Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414', 'See the presentation'),
           ('https://century21.pt/ref/C0554-00006', '/img/core-devesas-t.jpg', 'CENTURY 21 Core · Vila Nova de Gaia', 'Photography and video of a five-bedroom house in Devesas (agent Vasco Dinis) and a three-bedroom flat in Oliveira do Douro.', 'See the listing'),
           ('https://www.motoreseacao.com/?utm_source=usinavideos&utm_medium=trabalhos&utm_campaign=usina', '/img/mea-toro.jpg', 'Motores e Ação · Automotive', 'Automotive journalism since 2002: road tests, launches and brand content in Brazil and Portugal. Over 115,000 YouTube subscribers.', 'See the website'),
           ('/cordiallevel/moncao/', '/cordiallevel/moncao/img/t1-area-t.jpg', 'Land in Monção · Alto Minho', 'Drone, video and project visualisations labelled as AI. ' + AMI, 'See the presentation'),
           ('https://www.youtube.com/watch?v=ed1kwc3x27I', 'https://i.ytimg.com/vi/ed1kwc3x27I/hqdefault.jpg', 'Panorama Imobiliário PT', 'Cordial Level’s podcast on YouTube, about the market and the decisions behind buying a home (in Portuguese). Produced and edited by Usina Vídeos.', 'Watch on YouTube')],
    cdj=('CDJRegio', 'Clube Desportivo José Régio, Vila do Conde. Basketball match coverage and highlights.', 'See on Instagram'),
    como_eb='How it works', como_h2='From request to delivery.',
    steps=[('Quote request', 'Tell us about the project, the location and the goal, by WhatsApp or e-mail.'),
           ('Shoot', 'We plan it with you and shoot on location: property, event, company or outdoors.'),
           ('Post-production', 'Selection, photo editing, video editing, subtitles and versions for each platform.'),
           ('Delivery and promotion', 'Photos within 48 hours, videos within 72 hours. If you wish, we publish and promote for you.')],
    marcas_eb='Our brands', marcas_h2='We also produce our own content.',
    mea_eb='Featured · a Usina Vídeos brand', mea_p='Automotive journalism since 2002: launches, road tests and offers in Brazil and Portugal.', mea_b='Read on motoreseacao.com',
    dicas=('Dicas do Freire', 'Freire Neto’s YouTube channel (in Portuguese).', 'Watch'),
    ig=('Freire Neto in Portugal', '@neofreireportugal · personal Instagram', 'Follow'),
    cont_eb='Contact', cont_h2='Shall we tell your story?',
    cont_p='Ask for a quote, with no obligation, by WhatsApp or e-mail.',
    wa_lbl='WhatsApp', mail_lbl='E-mail', social='Usina on social media',
    foot='Content and communication agency · Northern Portugal and nationwide',
    sim='AI visualisations always labelled',
),
'es': dict(
    socials=[('https://www.instagram.com/usina.videos','ig','Usina Vídeos','@usina.videos · últimos trabajos','Seguir'),('https://www.instagram.com/neofreireportugal','ig','Freire Neto en Portugal','@neofreireportugal · Instagram personal','Seguir'),('https://www.instagram.com/freireneto','ig','Freire Neto en Brasil','@freireneto · Instagram','Seguir'),('https://www.instagram.com/motoreseacao','ig','Motores e Ação','@motoreseacao · Instagram','Seguir'),('https://www.linkedin.com/in/freireneto/','in','Freire Neto','LinkedIn','Ver perfil')],
    desp=dict(eb='Deporte', h2='También en la cancha.', p='Reportajes de partidos y torneos de baloncesto, con resúmenes y perfiles de jugadores para redes sociales.', cdj='Clube Desportivo José Régio · Vila do Conde. Resúmenes de los partidos de cantera y sénior.', mb='MatchBall × Red Rose Thunder', mbp='Gira internacional de baloncesto en Portugal. Perfiles y resúmenes de los jugadores.', ver='Ver en Instagram', mais='Ver más en Instagram'),
    sites={'nav': 'Webs', 'eb': 'Webs, presentaciones y pódcasts', 'h2': 'Soluciones digitales para su negocio.', 'p': 'Además del vídeo, creamos las herramientas donde vive: webs, presentaciones y pódcasts, con la misma calidad de reportaje.', 'items': [('Webs', 'Webs para agencias, agentes y marcas, con cartera de inmuebles, vídeos y contacto directo por WhatsApp.', [('Cordial Level', '/cordiallevel/')]), ('Presentaciones digitales', 'Una página por inmueble o proyecto, en varios idiomas, para enviar por enlace, imprimir en PDF o mostrar en reuniones.', [('Condomínio Coral', '/t4coral/es.html'), ('T3 Leça', '/cordiallevel/t3leca/')]), ('Pódcasts', 'Formato, grabación, edición y publicación en YouTube y Spotify, con cortes para redes sociales.', [('Panorama Imobiliário PT', 'https://www.youtube.com/watch?v=ed1kwc3x27I')])], 'ex': 'Ejemplo'},
    ig_cl='Destacado en el Instagram de Cordial Level',
    agenda={'nav': 'Agenda', 'eb': 'Agenda', 'h2': 'Agenda abierta para finales de octubre y noviembre.', 'p': 'Elija el día y la hora de su sesión directamente en nuestro calendario. ¿Prefiere hablar primero? Envíenos un mensaje por WhatsApp.', 'alt': 'Abrir el calendario en una nueva ventana'},
    path='es/', html_lang='es', og_locale='es_ES',
    title='Usina Vídeos · Productora de contenido y comunicación en Portugal',
    desc='Vídeo, fotografía, dron, contenido para redes, webs y campañas digitales para empresas, marcas y profesionales. Inmobiliario, automoción, deporte, turismo y negocios, en el Norte y en todo Portugal. Pida presupuesto.',
    nav=[('quem', 'Quiénes somos'), ('servicos', 'Servicios'), ('trabalhos', 'Trabajos'), ('sites', 'Webs'), ('desporto', 'Deporte'), ('como', 'Cómo funciona'), ('marcas', 'Marcas'), ('agenda', 'Agenda'), ('contacto', 'Contacto')],
    cta='Pida presupuesto',
    wa_msg='Hola Freire, me gustaría pedir un presupuesto a Usina Vídeos.',
    hero_eb='Productora de contenido y comunicación · Norte y todo Portugal',
    hero_h1='Comunicación que se ve. Contenido que da resultados.',
    hero_p='Vídeo, fotografía, dron, redes sociales, webs y campañas digitales para empresas, marcas y profesionales. Del inmobiliario a la automoción, del deporte al turismo: una producción, un briefing, un contacto.',
    hero_b2='Ver trabajos',
    hero_cap='Foz do Douro, Oporto · dron de Usina Vídeos',
    team=[('Freire Neto', 'Dirección, reportaje e imagen', 'Periodista desde 1997, exdirector de contenido y producción del Canal 10 de TCM Mossoró y fundador de Motores e Ação.'), ('Sandra Freire', 'Edición, producción y administración', '20 años en televisión, productoras y en Motores e Ação.')],
    quem_eb='Quiénes somos', quem_h2='Mirada de periodista, al servicio de su comunicación.',
    quem_p=['Usina Vídeos está dirigida por <b>Freire Neto</b> y <b>Sandra Freire</b>. Freire Neto es periodista desde 1997 y fundador de Motores e Ação, con más de 25 años de reportaje y producción audiovisual. Fue director de contenido, de producción y de directos del Canal 10 de TCM Mossoró, en Brasil, donde creó soluciones de comunicación para empresas e instituciones: centros comerciales como Partage Shopping, hospitales, clínicas, médicos, clubes y eventos. Sandra Freire es responsable de la edición, la producción y la administración, con 20 años de experiencia en televisión, productoras y en Motores e Ação.',
            'Somos una productora de contenido y comunicación. Tratamos cada proyecto como un reportaje: entender qué lo hace único, captarlo con rigor y contarlo con claridad a quien necesita verlo. Audiovisual y marketing digital para inmuebles, marcas, eventos, equipos y personas.',
            'Trabajamos en <b>todo el Norte</b> y en <b>cualquier punto de Portugal</b>, con el desplazamiento incluido en el presupuesto.'],
    stats=[('25+', 'años de periodismo'), ('48h', 'entrega de fotografías'), ('72h', 'vídeos editados'), ('PT · EN · ES', 'contenidos multilingües')],
    serv_eb='Servicios', serv_h2='Todo lo que su mensaje necesita para ser visto.',
    serv_p='Cada servicio puede contratarse por separado o combinado. Enviamos un presupuesto adaptado al proyecto y a su ubicación.',
    servs=[('Vídeo y reportaje', 'Vídeos institucionales, reportajes, entrevistas, eventos y making of, en formato horizontal y vertical.'),
           ('Fotografía', 'Fotografía de alta resolución para inmuebles, productos, eventos, equipos y retratos profesionales.'),
           ('Dron', 'Planos aéreos en foto y vídeo para inmobiliario, turismo, eventos y deporte.'),
           ('Contenido para redes sociales', 'Reels, shorts, carruseles y publicaciones, con la voz de su marca y con regularidad.'),
           ('Webs y páginas', 'Webs, landing pages y presentaciones digitales en varios idiomas, listas para compartir y captar contactos.'),
           ('Campañas y marketing digital', 'Gestión de anuncios en Facebook e Instagram, estrategia de contenido y captación de contactos.')],
    medida_h3='Áreas en las que trabajamos',
    medida=['Inmobiliario: agentes, agencias y promociones', 'Automoción: concesionarios, marcas, lanzamientos y pruebas', 'Deporte: clubes, atletas y partidos',
            'Comercio, tiendas y centros comerciales', 'Empresas, salud e instituciones', 'Turismo, viajes y eventos', 'Personas y profesionales: imagen y marca personal'],
    orc_h3='Cada proyecto es diferente. El presupuesto también.',
    orc_p='Cuéntenos qué quiere comunicar, dónde y a quién. Respondemos con una propuesta clara, por proyecto o por paquete, con el IVA indicado.',
    trab_eb='Trabajos', trab_h2='Trabajo reciente en varias áreas, publicado con autorización.',
    works=[('/cordiallevel/', '/cordiallevel/t3leca/img/leca-37-t.jpg', 'Cordial Level', 'Socio de producción: web, vídeo-reportajes, pódcast y redes sociales. ' + AMI, 'Ver la web'),
           ('/t4coral/es.html', '/img/coral-fachada.jpg', 'Condomínio Coral · Foz do Douro', 'Fotografía, dron, vídeo con la agente y presentación digital en cuatro idiomas. Agente Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414', 'Ver la presentación'),
           ('https://century21.pt/ref/C0554-00006', '/img/core-devesas-t.jpg', 'CENTURY 21 Core · Vila Nova de Gaia', 'Fotografía y vídeo de una casa de cinco dormitorios en Devesas (agente Vasco Dinis) y de un piso de tres dormitorios en Oliveira do Douro.', 'Ver el anuncio'),
           ('https://www.motoreseacao.com/?utm_source=usinavideos&utm_medium=trabalhos&utm_campaign=usina', '/img/mea-toro.jpg', 'Motores e Ação · Automoción', 'Periodismo del motor desde 2002: pruebas, lanzamientos y contenidos para marcas, en Brasil y Portugal. Más de 115.000 suscriptores en YouTube.', 'Ver la web'),
           ('/cordiallevel/moncao/', '/cordiallevel/moncao/img/t1-area-t.jpg', 'Terrenos en Monção · Alto Minho', 'Dron, vídeo y simulaciones de proyecto identificadas como IA. ' + AMI, 'Ver la presentación'),
           ('https://www.youtube.com/watch?v=ed1kwc3x27I', 'https://i.ytimg.com/vi/ed1kwc3x27I/hqdefault.jpg', 'Panorama Imobiliário PT', 'El pódcast de Cordial Level en YouTube, sobre el mercado y las decisiones de quien compra casa (en portugués). Producción y edición de Usina Vídeos.', 'Ver en YouTube')],
    cdj=('CDJRegio', 'Clube Desportivo José Régio, Vila do Conde. Reportajes y resúmenes de los partidos de baloncesto.', 'Ver en Instagram'),
    como_eb='Cómo funciona', como_h2='De la solicitud a la entrega.',
    steps=[('Solicitud de presupuesto', 'Cuéntenos el proyecto, el lugar y el objetivo, por WhatsApp o e-mail.'),
           ('Producción', 'Lo planificamos con usted y grabamos en el lugar: inmueble, evento, empresa o exterior.'),
           ('Postproducción', 'Selección, edición de imagen, montaje de vídeo, subtítulos y versiones para cada plataforma.'),
           ('Entrega y difusión', 'Fotografías en 48 horas, vídeos en 72 horas. Si lo desea, publicamos y promocionamos por usted.')],
    marcas_eb='Nuestras marcas', marcas_h2='También producimos contenido propio.',
    mea_eb='Destacado · una marca de Usina Vídeos', mea_p='Periodismo del motor desde 2002: lanzamientos, pruebas y ofertas en Brasil y Portugal.', mea_b='Leer en motoreseacao.com',
    dicas=('Dicas do Freire', 'El canal de Freire Neto en YouTube (en portugués).', 'Ver el canal'),
    ig=('Freire Neto en Portugal', '@neofreireportugal · Instagram personal', 'Seguir'),
    cont_eb='Contacto', cont_h2='¿Comunicamos su proyecto?',
    cont_p='Pida presupuesto sin compromiso, por WhatsApp o e-mail.',
    wa_lbl='WhatsApp', mail_lbl='E-mail', social='Redes de Usina',
    foot='Productora de contenido y comunicación · Norte y todo Portugal',
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
.team{display:grid;gap:12px;margin-top:22px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}.team>div{background:#fff;border:1px solid #E3DED6;border-left:5px solid var(--c);border-radius:14px;padding:16px 18px}.team b{display:block;font-size:18px;color:var(--ink)}.team span{display:block;margin-top:2px;font-size:12px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--c)}.team p{margin:8px 0 0!important;font-size:15px}
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
/* instagram cl */
.igrow iframe.instagram-media,.sport iframe.instagram-media{min-height:620px!important;background:#fff!important}
.igh{color:var(--fg);font-size:24px;margin:56px 0 0;padding-top:28px;border-top:1px solid var(--line)}
.igrow{display:grid;gap:18px;margin-top:24px;align-items:start}@media(min-width:760px){.igrow{grid-template-columns:repeat(3,1fr)}}
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
@media(min-width:900px){.mea{display:grid;grid-template-columns:auto 1fr;column-gap:40px;align-items:center}.mea small{grid-column:1/-1}.mea img{grid-row:2/4;margin-top:16px}.mea p{margin-top:16px}.mea b{justify-self:start}}
.mea{display:block;text-decoration:none;color:#fff;background:radial-gradient(520px 260px at 100% 0%,rgba(0,77,154,.55),transparent 70%),#0B0E14;border:1px solid rgba(47,127,208,.45);border-radius:18px;padding:30px 28px}
.mea small{display:block;font-size:12px;letter-spacing:.2em;font-weight:800;color:var(--mea-l);text-transform:uppercase}
.mea img{width:min(300px,70vw);height:auto;margin-top:16px;filter:brightness(0) invert(1)}
.mea p{margin:14px 0 0;color:#C9CFD8}
.mea b{display:inline-block;margin-top:20px;background:var(--mea);color:#fff;font-weight:800;font-size:15px;padding:12px 20px;border-radius:999px}
.mea:hover b{background:var(--mea-l)}
.mrow{display:flex;flex-wrap:wrap;align-items:center;gap:14px 18px}.mrow i{font-style:normal;font-weight:700;font-size:14px;color:#C9CFD8;margin-top:20px}
.side{display:grid;gap:16px}
.mini{display:flex;align-items:center;gap:14px;padding:20px;border-radius:16px;background:var(--ink2);border:1px solid var(--line);text-decoration:none;color:#D6D1CD}
.mini b{display:block;color:var(--fg);font-size:17px}.mini span{font-size:14px}
.mini em{margin-left:auto;font-style:normal;font-weight:800;font-size:14px;color:var(--y);white-space:nowrap}
.mini.ig{background:linear-gradient(var(--ink2),var(--ink2)) padding-box,linear-gradient(90deg,var(--y),var(--r),#8a3ab9) border-box;border:2px solid transparent}
.mini.yt em{color:var(--r)}
.mini.in{border-color:rgba(10,102,194,.6)}.mini.in em{color:#5AA3E8}
.side{grid-template-columns:repeat(auto-fill,minmax(320px,1fr))}@media(max-width:400px){.side{grid-template-columns:1fr}}
.card .ex{font-size:14px;font-weight:700;margin-top:14px}.card .ex a{color:var(--r)}
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
MEA_ICON = '<img src="/img/logo/motores-e-acao-quadrado.jpg" alt="" width="34" height="34" style="border-radius:8px;flex:0 0 auto">'
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
    works = ''.join(f'<a class="work" href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}><div class="ph"><img src="{im}" alt="{e(ti)}" loading="lazy" width="900" height="563"></div><div class="bd"><h3>{e(ti)}</h3><p>{e(d)}</p><em>{e(c)} →</em></div></a>' for h, im, ti, d, c in t['works'])
    cn, cd, cc = t['cdj']
    steps = ''.join(f'<div class="step"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in t['steps'])
    stats = ''.join(f'<div><b>{a}</b><span>{e(b)}</span></div>' for a, b in t['stats'])
    quem = ''.join(f'<p>{x}</p>' for x in t['quem_p'])
    quem += '<div class="team">' + ''.join(f'<div style="--c:{COLORS[i % 3]}"><b>{e(n)}</b><span>{e(r)}</span><p>{e(d)}</p></div>' for i, (n, r, d) in enumerate(t['team'])) + '</div>'
    sites = ''.join(f'<article class="card" style="--c:{COLORS[i % 3]}"><span class="n">{i + 1:02d}</span><h3>{e(a)}</h3><p>{e(b)}</p><p class="ex">{e(t["sites"]["ex"])}: ' + ' · '.join(f'<a href="{u}"' + (' target="_blank" rel="noopener"' if u.startswith('http') else '') + f'>{e(l)} →</a>' for l, u in exs) + '</p></article>' for i, (a, b, exs) in enumerate(t['sites']['items']))
    socials = ''.join(f'<a class="mini {k}" href="{u}" target="_blank" rel="noopener">{MEA_ICON if "motoreseacao" in u else (IG_SVG if k == "ig" else IN_SVG)}<div><b>{e(a)}</b><span>{e(b)}</span></div><em>{e(c)} →</em></a>' for u, k, a, b, c in t['socials'])
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
<style>{CSS}{MEA_CSS}</style>
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
    <h3 class="igh">{e(t['ig_cl'])}</h3>
    <div class="igrow">{ig_embed('Dd7UOxSDG8Q')}{ig_embed('DbMWJvfs3_z')}{ig_embed('DYfFrTsDZk0')}</div>
  </div>
</section>

<section id="sites">
  <div class="wrap">
    <span class="eb">{e(t['sites']['eb'])}</span><h2>{e(t['sites']['h2'])}</h2><p class="lead">{e(t['sites']['p'])}</p>
    <div class="grid3">{sites}</div>
    <div style="margin-top:28px"><a class="btn y" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{e(t['cta'])}</a></div>
  </div>
</section>

<section id="desporto" style="background:var(--paper2)">
  <div class="wrap">
    <span class="eb">{e(t['desp']['eb'])}</span><h2>{e(t['desp']['h2'])}</h2><p class="lead">{e(t['desp']['p'])}</p>
    <div class="sport">
      <div class="sp"><div class="sph" style="--c:var(--r)"><img src="/img/logo/cdjregio.png" alt="CDJRegio" width="56" height="56" loading="lazy" style="float:right;width:56px;height:56px;margin-left:12px"><b>CDJRegio</b><p>{e(t['desp']['cdj'])}</p><a href="https://cdjregio.pt/" target="_blank" rel="noopener">cdjregio.pt →</a> · <a href="https://www.instagram.com/cdjregio/" target="_blank" rel="noopener">@cdjregio →</a></div>{ig_embed('Deri9uUiObc')}</div>
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
      <div class="side">
        {socials}
        <a class="mini yt" href="https://www.youtube.com/@DicasdoFreire/" target="_blank" rel="noopener">{YT_SVG}<div><b>{e(t['dicas'][0])}</b><span>{e(t['dicas'][1])}</span></div><em>{e(t['dicas'][2])} →</em></a>
      </div>
    </div>
  </div>
</section>

<section id="agenda" style="background:var(--paper2)">
  <div class="wrap">
    <span class="eb">{e(t['agenda']['eb'])}</span><h2>{e(t['agenda']['h2'])}</h2><p class="lead">{e(t['agenda']['p'])}</p>
    <div class="row" style="display:flex;flex-wrap:wrap;gap:12px;margin-top:22px"><a class="btn y" href="{wa}" target="_blank" rel="noopener">{WA_SVG}WhatsApp</a><a class="btn o" style="color:var(--ink)" href="https://calendly.com/usinavideos/videoreport" target="_blank" rel="noopener">{e(t['agenda']['alt'])} ↗</a></div>
    <div class="calendly-inline-widget" data-url="https://calendly.com/usinavideos/videoreport?hide_gdpr_banner=1&amp;primary_color=e5ae29" style="min-width:300px;height:720px;margin-top:28px;border-radius:18px;overflow:hidden;background:#fff"></div>
  </div>
</section>
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>

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

<footer><div class="wrap" style="display:block;margin-bottom:28px">{mea_banner(lang, 'usinavideos')}</div><div class="wrap">
  <a href="/{t['path']}" aria-label="Usina Vídeos · página inicial"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos" width="1367" height="298"></a>
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
