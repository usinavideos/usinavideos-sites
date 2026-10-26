#!/usr/bin/env python3
"""SEO para usinavideos.pt: indexação aberta, canónicas, hreflang, Open Graph/Twitter,
dados estruturados (JSON-LD), robots.txt, sitemap.xml e llms.txt.

Uso: python3 _tools/seo.py [pasta_do_site]   (por omissão, a raiz do repositório)
Corre DEPOIS dos geradores (imovel.py, cordiallevel.py, site_usina.py). É idempotente:
o bloco gerado fica entre <!--seo--> e <!--/seo--> e é substituído a cada execução.
"""
import datetime, html, json, os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://usinavideos.pt'
TODAY = datetime.date.today().isoformat()
ROBOTS = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">'

USINA = {
    '@type': ['Organization', 'ProfessionalService'], '@id': BASE + '/#usina',
    'name': 'Usina Vídeos', 'url': BASE + '/', 'logo': BASE + '/img/logo/usina-horizontal-1200.png',
    'image': BASE + '/img/foz-drone.jpg',
    'description': 'Produtora de conteúdo e comunicação: vídeo, fotografia, drone, conteúdo para redes, sites e campanhas digitais para empresas, marcas e profissionais. Imobiliário, automóvel, desporto, turismo e negócios, no Norte e em todo o Portugal.',
    'telephone': '+351912988971', 'email': 'freireneto@me.com',
    'address': {'@type': 'PostalAddress', 'addressRegion': 'Porto', 'addressCountry': 'PT'},
    'areaServed': [{'@type': 'AdministrativeArea', 'name': 'Norte de Portugal'}, {'@type': 'Country', 'name': 'Portugal'}],
    'knowsLanguage': ['pt-PT', 'en', 'es'],
    'founder': [{'@type': 'Person', 'name': 'Freire Neto', 'jobTitle': 'Jornalista e produtor audiovisual', 'sameAs': ['https://www.linkedin.com/in/freireneto/', 'https://www.instagram.com/freireneto', 'https://www.instagram.com/neofreireportugal']},
                {'@type': 'Person', 'name': 'Sandra Freire', 'jobTitle': 'Edição, produção e administração'}],
    'sameAs': ['https://www.instagram.com/usina.videos', 'https://www.facebook.com/usinacomvideos', 'https://motoreseacao.com',
               'https://www.youtube.com/@motoreseacao', 'https://www.youtube.com/@DicasdoFreire/'],
    'makesOffer': [{'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': n}} for n in
                   ['Reportagem fotográfica de imóveis', 'Vídeo com drone', 'Vídeo com o consultor', 'Visita virtual 3D',
                    'Apresentação digital de imóveis', 'Sites para agências e consultores', 'Produção de podcasts', 'Reportagem desportiva']],
}

CL = {
    '@type': 'RealEstateAgent', '@id': BASE + '/cordiallevel/#cordiallevel', 'name': 'Cordial Level',
    'description': 'Cordial Level | CENTURY 21 Arquitectos · AMI 11414. Compra, venda e investimento imobiliário no Grande Porto e no Norte.',
    'url': BASE + '/cordiallevel/', 'logo': BASE + '/cordiallevel/img/logo-cordial-level.png',
    'image': BASE + '/cordiallevel/t3leca/img/leca-38.jpg', 'telephone': '+351935101667',
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Porto', 'addressRegion': 'Porto', 'addressCountry': 'PT'},
    'areaServed': ['Grande Porto', 'Norte de Portugal'],
    'parentOrganization': {'@type': 'RealEstateAgent', 'name': 'CENTURY 21 Arquitectos'},
    'identifier': {'@type': 'PropertyValue', 'name': 'Licença AMI', 'value': '11414'},
    'employee': [{'@type': 'Person', 'name': 'Casemiro Ramos', 'jobTitle': 'Consultor', 'telephone': '+351935101667', 'email': 'cramos@century21.pt', 'url': 'https://century21.pt/consultores/cramos'},
                 {'@type': 'Person', 'name': 'Francisco Medeiros', 'jobTitle': 'Consultor', 'telephone': '+351912706395', 'email': 'franciscomedeiros@century21.pt', 'url': 'https://franciscomedeiros.century21.pt'}],
    'sameAs': ['https://www.instagram.com/cordiallevel/', 'https://www.facebook.com/cordiallevel/', 'https://www.youtube.com/@CordialLevelPT', 'https://century21.pt/consultores/cramos'],
}

def place(kind, name, area, rooms, locality, region, geo):
    d = {'@type': kind, 'name': name, 'address': {'@type': 'PostalAddress', 'addressLocality': locality, 'addressRegion': region, 'addressCountry': 'PT'}}
    if area: d['floorSize'] = {'@type': 'QuantitativeValue', 'value': area, 'unitCode': 'MTK'}
    if rooms: d['numberOfBedrooms'] = rooms
    if geo: d['geo'] = {'@type': 'GeoCoordinates', 'latitude': geo[0], 'longitude': geo[1]}
    return d

def offer(price, ref, url):
    o = {'@type': 'Offer', 'availability': 'https://schema.org/InStock', 'url': url, 'sku': ref, 'seller': {'@id': CL['@id']}}
    if price: o.update(price=price, priceCurrency='EUR')
    return o

LISTINGS = {  # caminho: (tipo, nome, área, quartos, localidade, região, geo, [(preço, ref)])
    'cordiallevel/t3leca/': ('Apartment', 'T3 em Leça da Palmeira com 2 lugares de garagem', 138, 3, 'Leça da Palmeira', 'Matosinhos', (41.1937336, -8.7060774), [(550000, 'C0393-01659')]),
    'cordiallevel/casaraofoz/': ('House', 'Moradia T4 com vista de mar na Foz do Douro', 165, 4, 'Foz do Douro, Porto', 'Porto', (41.1512834, -8.6767872), [(875000, 'C0393-01661')]),
    'cordiallevel/bosquepicua/': ('Apartment', 'T2+1 com terraço e box no Bosque da Pícua', 92.3, 2, 'Águas Santas, Maia', 'Porto', (41.2037790756507, -8.56774606227663), [(None, 'C0393-01555')]),
    'cordiallevel/anteroquental/': ('Apartment', 'T2 remodelado na Rua Antero de Quental', 77.3, 2, 'Porto', 'Porto', (41.1602049, -8.6116069), [(349000, 'C0393-01689')]),
    'cordiallevel/moncao/': ('Place', 'Dois terrenos de cultura e vinha em São Bento (Bela), Monção', None, None, 'Monção', 'Viana do Castelo', (42.072910104535, -8.43833682762678), [(75000, 'C0393-01441'), (35000, 'C0393-01442')]),
}

CORAL_LANG = {
    'index.html': ('pt-PT', 'Condomínio Coral, Foz do Douro: dois apartamentos T4+1 de nova construção com 236 m², quatro suítes com closet, terraços e garagem, perto da Universidade Católica e das praias. Apresentado por Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414.'),
    'en.html': ('en', 'Condomínio Coral, Foz do Douro (Porto): two new four-bedroom apartments of 236 m², four en-suite bedrooms with walk-in closets, terraces and parking, near the Catholic University and the beaches. Presented by Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414.'),
    'es.html': ('es', 'Condomínio Coral, Foz do Douro (Oporto): dos pisos nuevos de cuatro dormitorios y 236 m², cuatro suites con vestidor, terrazas y garaje, cerca de la Universidad Católica y de las playas. Presentado por Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414.'),
    'fr.html': ('fr', 'Condomínio Coral, Foz do Douro (Porto) : deux appartements neufs de quatre chambres et 236 m², quatre suites avec dressing, terrasses et garage, près de l’Université catholique et des plages. Présenté par Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414.'),
}

USINA_LANG = {'': 'pt-PT', 'en/': 'en', 'es/': 'es'}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', **obj} if '@graph' not in obj else {'@context': 'https://schema.org', **obj}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>'


def meta(s, prop, attr='property'):
    m = re.search(rf'<meta {attr}="{re.escape(prop)}" content="([^"]*)"', s)
    return html.unescape(m.group(1)) if m else None


def inject(path, block, drop_desc=False):
    p = os.path.join(ROOT, path)
    s = open(p, encoding='utf-8').read()
    s = re.sub(r'\s*<!--seo-->.*?<!--/seo-->', '', s, flags=re.S)
    s = re.sub(r'\s*<meta name="robots"[^>]*>', '', s)
    s = s.replace('</head>', '<!--seo-->\n' + block + '\n<!--/seo-->\n</head>', 1)
    open(p, 'w', encoding='utf-8').write(s)


def common(s, url, kind='website', desc=None):
    s = re.sub(r'<!--seo-->.*?<!--/seo-->', '', s, flags=re.S)  # ver só o que está fora do bloco gerado
    out = [ROBOTS]
    if 'rel="canonical"' not in s: out.append(f'<link rel="canonical" href="{url}">')
    if desc and 'name="description"' not in s: out.append(f'<meta name="description" content="{html.escape(desc)}">')
    if not meta(s, 'og:description') and (desc or meta(s, 'description', 'name')):
        out.append(f'<meta property="og:description" content="{html.escape(desc or meta(s, "description", "name"))}">')
    out += [f'<meta property="og:url" content="{url}">', f'<meta property="og:type" content="{kind}">',
            '<meta property="og:site_name" content="Usina Vídeos">', '<meta name="twitter:card" content="summary_large_image">']
    return out


pages = []  # (url, lastmod, alternates)

# Usina (PT/EN/ES)
alts_usina = [(l, f'{BASE}/{p}') for p, l in USINA_LANG.items()]
for p, lang in USINA_LANG.items():
    f = p + 'index.html'
    if not os.path.exists(os.path.join(ROOT, f)): continue
    s = open(os.path.join(ROOT, f), encoding='utf-8').read()
    url = f'{BASE}/{p}'
    out = common(s, url)
    out.append('<meta name="msvalidate.01" content="56593FE2E31FC20F2AEE040C5E1B0D3D">')
    if 'hreflang="x-default"' not in s: out.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}/">')
    out.append(ld({'@graph': [dict(USINA), {'@type': 'WebSite', '@id': BASE + '/#site', 'url': BASE + '/', 'name': 'Usina Vídeos', 'inLanguage': lang, 'publisher': {'@id': USINA['@id']}},
                              {'@type': 'WebPage', 'url': url, 'name': html.unescape(re.search(r'<title>(.*?)</title>', s).group(1)), 'inLanguage': lang, 'isPartOf': {'@id': BASE + '/#site'}, 'about': {'@id': USINA['@id']}}]}))
    inject(f, '\n'.join(out))
    pages.append((url, alts_usina))

# Cordial Level
f = 'cordiallevel/index.html'
if os.path.exists(os.path.join(ROOT, f)):
    s = open(os.path.join(ROOT, f), encoding='utf-8').read()
    url = BASE + '/cordiallevel/'
    items = [{'@type': 'ListItem', 'position': i + 1, 'url': f'{BASE}/{k}', 'name': v[1]} for i, (k, v) in enumerate(LISTINGS.items())]
    out = common(s, url)
    out.append(ld({'@graph': [dict(CL), {'@type': 'ItemList', 'name': 'Imóveis em destaque · Cordial Level', 'itemListElement': items},
                              {'@type': 'WebPage', 'url': url, 'name': 'Cordial Level · Imóveis no Grande Porto', 'inLanguage': 'pt-PT', 'publisher': {'@id': USINA['@id']}}]}))
    inject(f, '\n'.join(out))
    pages.append((url, None))

# Imóveis
for path, (kind, name, area, rooms, loc, region, geo, offers) in LISTINGS.items():
    f = path + 'index.html'
    if not os.path.exists(os.path.join(ROOT, f)): continue
    s = open(os.path.join(ROOT, f), encoding='utf-8').read()
    url = f'{BASE}/{path}'
    img = meta(s, 'og:image')
    listing = {'@type': 'RealEstateListing', 'name': name, 'url': url, 'inLanguage': 'pt-PT',
               'description': meta(s, 'description', 'name'), 'datePosted': TODAY,
               'about': place(kind, name, area, rooms, loc, region, geo),
               'offers': [offer(pr, ref, f'https://century21.pt/comprar/{ref}') for pr, ref in offers],
               'provider': {'@id': CL['@id']}}
    if img: listing['image'] = img
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Cordial Level', 'item': BASE + '/cordiallevel/'},
        {'@type': 'ListItem', 'position': 2, 'name': name, 'item': url}]}
    yt = re.search(r'data-yt="([\w-]{11})"', s)
    graph = [listing, crumbs, dict(CL)]
    if yt:
        graph.append({'@type': 'VideoObject', 'name': name, 'description': meta(s, 'description', 'name'), 'thumbnailUrl': f'https://i.ytimg.com/vi/{yt.group(1)}/hqdefault.jpg',
                      'contentUrl': f'https://www.youtube.com/watch?v={yt.group(1)}', 'embedUrl': f'https://www.youtube.com/embed/{yt.group(1)}', 'uploadDate': TODAY})
    out = common(s, url, 'article')
    out.append(ld({'@graph': graph}))
    inject(f, '\n'.join(out))
    pages.append((url, None))

# Condomínio Coral (PT/EN/ES/FR)
alts_coral = [(l, f'{BASE}/t4coral/' + ('' if fn == 'index.html' else fn)) for fn, (l, _) in CORAL_LANG.items()]
for fn, (lang, desc) in CORAL_LANG.items():
    f = 't4coral/' + fn
    if not os.path.exists(os.path.join(ROOT, f)): continue
    s = open(os.path.join(ROOT, f), encoding='utf-8').read()
    url = f'{BASE}/t4coral/' + ('' if fn == 'index.html' else fn)
    out = common(s, url, 'article', desc)
    out += [f'<link rel="alternate" hreflang="{l}" href="{u}">' for l, u in alts_coral]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}/t4coral/">')
    listing = {'@type': 'RealEstateListing', 'name': 'Condomínio Coral · Foz do Douro', 'url': url, 'inLanguage': lang, 'description': desc,
               'image': meta(s, 'og:image'), 'datePosted': TODAY,
               'about': place('Apartment', 'Condomínio Coral · dois apartamentos T4+1', 236, 4, 'Foz do Douro, Porto', 'Porto', None),
               'provider': {'@type': 'RealEstateAgent', 'name': 'CENTURY 21 Arquitectos II', 'identifier': {'@type': 'PropertyValue', 'name': 'Licença AMI', 'value': '11414'},
                            'employee': {'@type': 'Person', 'name': 'Cheila Monteiro', 'jobTitle': 'Consultora'}},
               'creator': {'@id': USINA['@id']}}
    out.append(ld({'@graph': [listing]}))
    inject(f, '\n'.join(out))
    pages.append((url, alts_coral))

# Endereços antigos: continuam a redirecionar, mas fora do índice
for old in ('t3leca', 'casaraofoz', 'bosquepicua'):
    f = old + '/index.html'
    if os.path.exists(os.path.join(ROOT, f)):
        s = open(os.path.join(ROOT, f), encoding='utf-8').read()
        if 'noindex' not in s:
            s = s.replace('<link rel="canonical"', '<meta name="robots" content="noindex, follow"><link rel="canonical"', 1)
            open(os.path.join(ROOT, f), 'w', encoding='utf-8').write(s)

# sitemap.xml
seen, rows = set(), []
for url, alts in pages:
    if url in seen: continue
    seen.add(url)
    x = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{u}"/>' for l, u in (alts or []))
    pri = '1.0' if url == BASE + '/' else '0.9' if url.endswith('/cordiallevel/') else '0.8'
    rows.append(f'<url><loc>{url}</loc><lastmod>{TODAY}</lastmod><priority>{pri}</priority>{x}</url>')
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n')

# robots.txt: tudo aberto, incluindo motores de pesquisa com IA
bots = ['Googlebot', 'Bingbot', 'DuckDuckBot', 'YandexBot', 'Applebot', 'Applebot-Extended', 'Google-Extended', 'GPTBot', 'OAI-SearchBot', 'ChatGPT-User',
        'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot', 'Perplexity-User', 'CCBot', 'Meta-ExternalAgent', 'Amazonbot', 'MistralAI-User']
open(os.path.join(ROOT, 'robots.txt'), 'w').write(
    '# usinavideos.pt — aberto a todos os motores de pesquisa e assistentes de IA\n' +
    ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in bots) + 'User-agent: *\nAllow: /\nDisallow: /_tools/\n\n' + f'Sitemap: {BASE}/sitemap.xml\n')

# llms.txt: resumo para assistentes de IA
open(os.path.join(ROOT, 'llms.txt'), 'w').write(f'''# Usina Vídeos

> Produtora de conteúdo e comunicação em Portugal (Norte e todo o país): vídeo, fotografia, drone, conteúdo para redes, sites, campanhas e marketing digital para empresas, marcas e profissionais. Áreas: imobiliário, automóvel, desporto, turismo, negócios e pessoas. Dirigida por Freire Neto (jornalista desde 1997, fundador do Motores e Ação) e Sandra Freire (edição, produção e administração, 20 anos em televisão, produtoras e no Motores e Ação). Orçamentos por WhatsApp +351 912 988 971 ou freireneto@me.com.

## Site
- [Usina Vídeos (PT)]({BASE}/): serviços, trabalhos, desporto, marcas e contacto
- [Usina Vídeos (EN)]({BASE}/en/)
- [Usina Vídeos (ES)]({BASE}/es/)

## Cordial Level | CENTURY 21 Arquitectos · AMI 11414
Mediação imobiliária no Grande Porto e no Norte. Consultores: Casemiro Ramos (+351 935 101 667) e Francisco Medeiros (+351 912 706 395).
- [Cordial Level · todos os imóveis]({BASE}/cordiallevel/)
''' + ''.join(f'- [{v[1]}]({BASE}/{k})\n' for k, v in LISTINGS.items()) + f'''
## Apresentações digitais
- [Condomínio Coral, Foz do Douro (PT/EN/ES/FR)]({BASE}/t4coral/): dois T4+1, consultora Cheila Monteiro · CENTURY 21 Arquitectos II · AMI 11414

## Marcas
- [Motores e Ação](https://motoreseacao.com): jornalismo automóvel desde 2002
''')
print('ok', len(rows), 'páginas no sitemap')
