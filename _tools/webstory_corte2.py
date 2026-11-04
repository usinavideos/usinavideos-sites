#!/usr/bin/env python3
"""Web story (AMP) do corte 2 do Panorama #3: "Quem pode ter acesso ao crédito jovem?" (Cordial Level).

Uso: python3 _tools/webstory_corte2.py
Reutiliza o estilo de webstory_panorama.py e acrescenta uma página com o vídeo do corte.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import webstory_panorama as W

SLUG = 'credito-jovem-em-40-segundos'
DIR = os.path.join(W.ROOT, 'web-stories', SLUG)
URL = f'https://usinavideos.pt/web-stories/{SLUG}/'
SHORT = 'https://www.youtube.com/shorts/mGd9NMmv5VA'
VIDEO = '/cordiallevel/media/panorama-3-corte-2.mp4'
WA = 'https://wa.me/351912706395?text=Ol%C3%A1%20Francisco%2C%20vi%20a%20web%20story%20do%20cr%C3%A9dito%20jovem%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es.'
AMI = W.AMI
DATE = '2026-11-04'

W.PAGES = [
    dict(id='video', kind='video', kicker='PANORAMA IMOBILIÁRIO PT #3 · DICA CORDIAL LEVEL', h='Quem pode ter acesso ao crédito jovem?',
         p='O Francisco Medeiros explica em 40 segundos. Ligue o som.', foot=AMI),
    dict(id='regras', kind='text', kicker='CRÉDITO JOVEM', h='Garantia pública: as regras',
         rows=[('18–35', 'anos, com morada fiscal em Portugal'), ('1.ª', 'habitação própria e permanente'),
               ('450 mil €', 'valor máximo do imóvel'), ('15%', 'do valor garantido pelo Estado'),
               ('100%', 'de financiamento possível pelo banco')],
         note='A aprovação do crédito é sempre do banco. Situação a 27 de outubro de 2026.'),
    dict(id='prazo', kind='text', kicker='ATÉ QUANDO?', h='O prazo que conta',
         rows=[('Certo', 'Garantia válida para contratos assinados até 31 de dezembro de 2026'),
               ('Proposto', 'O Orçamento do Estado para 2027 prevê mantê-la'),
               ('Dica', 'Não deixe a simulação para dezembro: um processo de crédito demora semanas')],
         note='Na CENTURY 21 Arquitectos, a intermediação de crédito é gratuita.', outlink=(WA, 'Pedir simulação')),
    dict(id='contactos', kind='contact', kicker='FALE CONNOSCO', h='Cordial Level',
         lines=['Francisco Medeiros · +351 912 706 395', 'Casemiro Ramos · +351 935 101 667', 'usinavideos.pt/cordiallevel'],
         note='Chamada para a rede móvel nacional · ' + AMI, outlink=(SHORT, 'Ver no YouTube')),
]

_inner = W.page_inner
def page_inner(pg, img):
    if pg['kind'] != 'video':
        return _inner(pg, img)
    return '\n'.join([
        f'<img class="logo" src="{img("logo.png")}" alt="Cordial Level" data-fit="contain">',
        '<div class="box">', f'<div class="k">{W.esc(pg["kicker"])}</div><h1 class="h">{W.esc(pg["h"])}</h1>',
        f'<p class="p">{W.esc(pg["p"])}</p>', f'<div class="rule"></div><div class="foot">{W.esc(pg["foot"])}</div>', '</div>',
        '<div class="brand">Produção Usina Vídeos · usinavideos.pt</div>'])
W.page_inner = page_inner

def build():
    html = W.amp()
    html = html.replace(W.URL, URL).replace('Crédito jovem em 2027: o novo episódio do Panorama Imobiliário PT', 'Quem pode ter acesso ao crédito jovem? Panorama Imobiliário PT')
    html = html.replace(W.esc('Garantia pública para jovens, o que está decidido para 2027 e três imóveis da Cordial Level no Porto, em Leça da Palmeira e na Foz do Douro. ' + AMI + '.'),
                        W.esc('O Francisco Medeiros, consultor da Cordial Level, explica em 40 segundos quem pode usar a garantia pública do crédito jovem. ' + AMI + '.'))
    html = html.replace(f'"datePublished":"{W.DATE}"', f'"datePublished":"{DATE}"')
    html = html.replace('<script async custom-element="amp-story"', '<script async custom-element="amp-video" src="https://cdn.ampproject.org/v0/amp-video-0.1.js"></script>\n<script async custom-element="amp-story"')
    vid = ('<amp-story-page id="p-video" auto-advance-after="vid">\n<amp-story-grid-layer template="fill">'
           f'<amp-video id="vid" autoplay layout="fill" poster="img/capa.jpg" src="{VIDEO}" artwork="img/capa.jpg" title="Quem pode ter acesso ao crédito jovem?"></amp-video>'
           '</amp-story-grid-layer>\n<amp-story-grid-layer template="fill"><div class="pg" style="background:transparent"><div class="shade"></div>')
    html = html.replace('<amp-story-page id="p-video" auto-advance-after="8s">\n<amp-story-grid-layer template="fill"><div class="pg">', vid, 1)
    os.makedirs(DIR, exist_ok=True)
    open(os.path.join(DIR, 'index.html'), 'w').write(html)
    print('web story:', os.path.join(DIR, 'index.html'))

if __name__ == '__main__':
    build()
