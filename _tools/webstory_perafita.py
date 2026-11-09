#!/usr/bin/env python3
"""Web story (AMP) do T2 em Perafita (Cordial Level). Uso: python3 _tools/webstory_perafita.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import webstory_panorama as W

SLUG = 't2-perafita'
DIR = os.path.join(W.ROOT, 'web-stories', SLUG)
URL = f'https://usinavideos.pt/web-stories/{SLUG}/'
VIDEO = '/cordiallevel/media/perafita-t2.mp4'
WA = 'https://wa.me/351912706395?text=Ol%C3%A1%20Francisco%2C%20vi%20a%20web%20story%20do%20T2%20em%20Perafita%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es.'
AMI = W.AMI
DATE = '2026-11-04'

W.PAGES = [
    dict(id='capa', kind='full', img='capa.jpg', alt='Fachada do edifício do T2 em Perafita', kicker='CORDIAL LEVEL · À VENDA · 258 000 €',
         h='T2 em Perafita', big=True, p='Remodelado, 83 m², com lugar de garagem e arrumos, ao lado da A28.', foot=AMI),
    dict(id='video', kind='video', kicker='EM VÍDEO', h='O Francisco Medeiros apresenta', p='Ligue o som.', foot=AMI),
    dict(id='sala', kind='frame', img='sala.jpg', alt='Sala com zona de refeições', kicker='POR DENTRO', h='Sala com zona de refeições',
         chips=['T2 · 83 m²', 'Cozinha remodelada', 'Pavimento flutuante'], foot=AMI, outlink=('/cordiallevel/perafita/', 'Ver o imóvel')),
    dict(id='tour', kind='frame', img='tour.jpg', alt='Sala do T2 em Perafita', kicker='VISITA VIRTUAL 3D', h='Percorra a casa sem sair do sofá',
         p='Todas as divisões, em 3D, no telemóvel ou no computador.', foot=AMI, outlink=('https://realsee.ai/JVLLgJmB', 'Abrir a visita 3D')),
    dict(id='mobilidade', kind='frame', img='transportes.jpg', alt='Paragem de autocarro em frente ao edifício', kicker='LOCALIZAÇÃO', h='A A28 e os transportes à porta',
         chips=['Ao lado da A28', 'Escolas', 'Autocarro', 'Perafita · Matosinhos'], foot=AMI),
    dict(id='garagem', kind='frame', img='garagem.jpg', alt='Garagem coletiva do edifício', kicker='INCLUI', h='Lugar de garagem e arrumos',
         chips=['Lugar de garagem grande', 'Arrumos', 'Capoto (ETICS)'], foot=AMI),
    dict(id='contactos', kind='contact', kicker='258 000 € · REF. C0393-01754', h='Marque a sua visita',
         lines=['Francisco Medeiros · +351 912 706 395', 'Casemiro Ramos · +351 935 101 667', 'usinavideos.pt/cordiallevel/perafita'],
         note='Chamada para a rede móvel nacional · ' + AMI, outlink=(WA, 'Falar com o Francisco')),
]

_inner = W.page_inner
def page_inner(pg, img):
    if pg['kind'] != 'video':
        return _inner(pg, img)
    return '\n'.join([f'<img class="logo" src="{img("logo.png")}" alt="Cordial Level" data-fit="contain">', '<div class="box">',
        f'<div class="k">{W.esc(pg["kicker"])}</div><h1 class="h">{W.esc(pg["h"])}</h1>', f'<p class="p">{W.esc(pg["p"])}</p>',
        f'<div class="rule"></div><div class="foot">{W.esc(pg["foot"])}</div>', '</div>', '<div class="brand">Produção Usina Vídeos · usinavideos.pt</div>'])
W.page_inner = page_inner

if __name__ == '__main__':
    html = W.amp().replace(W.URL, URL)
    html = html.replace('Crédito jovem em 2027: o novo episódio do Panorama Imobiliário PT', 'T2 em Perafita · 258 000 € · Cordial Level')
    html = html.replace(W.esc('Garantia pública para jovens, o que está decidido para 2027 e três imóveis da Cordial Level no Porto, em Leça da Palmeira e na Foz do Douro. ' + AMI + '.'),
                        W.esc('T2 remodelado em Perafita, Matosinhos: 83 m², garagem e arrumos, ao lado da A28. 258 000 €. Vídeo com o consultor Francisco Medeiros e visita virtual 3D. ' + AMI + '.'))
    html = html.replace(f'"datePublished":"{W.DATE}"', f'"datePublished":"{DATE}"')
    html = html.replace('<script async custom-element="amp-story"', '<script async custom-element="amp-video" src="https://cdn.ampproject.org/v0/amp-video-0.1.js"></script>\n<script async custom-element="amp-story"')
    html = html.replace('<amp-story-page id="p-video" auto-advance-after="8s">\n<amp-story-grid-layer template="fill"><div class="pg">',
        '<amp-story-page id="p-video" auto-advance-after="vid">\n<amp-story-grid-layer template="fill">'
        f'<amp-video id="vid" autoplay layout="fill" poster="img/sala.jpg" src="{VIDEO}" artwork="img/capa.jpg" title="T2 em Perafita"></amp-video>'
        '</amp-story-grid-layer>\n<amp-story-grid-layer template="fill"><div class="pg" style="background:transparent"><div class="shade"></div>', 1)
    os.makedirs(DIR, exist_ok=True); open(os.path.join(DIR, 'index.html'), 'w').write(html); print('ok', DIR)
