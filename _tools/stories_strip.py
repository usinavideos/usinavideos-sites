#!/usr/bin/env python3
"""Faixa "Web Stories" na página inicial (PT/EN/ES): lista automaticamente todas as web-stories/*/.

Idempotente. Corre depois de criar uma story nova ou de regenerar a página inicial (site_usina.py).
Uso: python3 _tools/stories_strip.py
"""
import glob, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
TXT = {'pt': ('Web Stories', 'Histórias rápidas, em ecrã inteiro.', 'Imóveis, episódios do Panorama Imobiliário PT, jogos e bastidores, contados em poucos toques. Toque numa capa para abrir.'),
       'en': ('Web Stories', 'Quick stories, full screen.', 'Properties, real-estate podcast episodes, games and behind-the-scenes, told in a few taps (in Portuguese).'),
       'es': ('Web Stories', 'Historias rápidas, a pantalla completa.', 'Inmuebles, episodios del pódcast inmobiliario, partidos y making of, en pocos toques (en portugués).')}
CSS = ('<style>.wsr{display:flex;gap:16px;overflow-x:auto;padding:8px 8px 18px;margin-left:-8px;margin-top:26px;scroll-snap-type:x mandatory;scrollbar-width:thin}'
       '.wsc{flex:0 0 168px;scroll-snap-align:start;text-decoration:none;color:inherit}'
       '.wsc .im{position:relative;display:block;aspect-ratio:9/16;border-radius:16px;overflow:hidden;background:#222;box-shadow:0 8px 22px rgba(0,0,0,.22);outline:3px solid var(--y);outline-offset:3px}'
       '.wsc img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .35s}.wsc:hover img{transform:scale(1.04)}'
       '.wsc .im::after{content:"";position:absolute;inset:auto 0 0 0;height:45%;background:linear-gradient(transparent,rgba(0,0,0,.75))}'
       '.wsc b{display:block;margin-top:12px;font-size:15px;line-height:1.3;color:var(--ink)}.wsc small{display:block;margin-top:4px;font-size:12px;color:#7A726E}'
       '@media(min-width:900px){.wsc{flex-basis:200px}}</style>')
MESES = ['jan.', 'fev.', 'mar.', 'abr.', 'mai.', 'jun.', 'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.']


def stories():
    out = []
    for f in glob.glob(os.path.join(ROOT, 'web-stories', '*', 'index.html')):
        s = open(f, encoding='utf-8').read()
        slug = os.path.basename(os.path.dirname(f))
        t = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip())
        p = re.search(r'poster-portrait-src="([^"]+)"', s)
        d = re.search(r'"datePublished":"(\d{4}-\d\d-\d\d)', s)
        poster = p.group(1).replace('https://usinavideos.pt', '') if p else f'/web-stories/{slug}/img/poster.jpg'
        out.append((d.group(1) if d else '0000-00-00', slug, t, poster))
    return sorted(out, reverse=True)


def block(lang, items):
    eb, h2, lead = TXT[lang]
    cards = ''.join(
        f'<a class="wsc" href="/web-stories/{slug}/"><span class="im"><img src="{e(poster)}" alt="" loading="lazy"></span><b>{e(t)}</b>'
        f'<small>{int(d[8:])} {MESES[int(d[5:7]) - 1]} {d[:4]}</small></a>' if d[0] != '0' else
        f'<a class="wsc" href="/web-stories/{slug}/"><span class="im"><img src="{e(poster)}" alt="" loading="lazy"></span><b>{e(t)}</b></a>'
        for d, slug, t, poster in items)
    return (f'<!--ws-->{CSS}<section id="stories" style="padding-bottom:24px"><div class="wrap"><span class="eb">{eb}</span><h2>{e(h2)}</h2>'
            f'<p class="lead">{e(lead)}</p><div class="wsr">{cards}</div></div></section><!--/ws-->\n')


def main():
    items = stories()
    for lang, f in [('pt', 'index.html'), ('en', 'en/index.html'), ('es', 'es/index.html')]:
        p = os.path.join(ROOT, f)
        s = open(p, encoding='utf-8').read()
        s = re.sub(r'<!--ws-->.*?<!--/ws-->\n?', '', s, flags=re.S)
        if items:
            b = s.find('<section id="blog"')
            k = s.find('</section>', b) + len('</section>\n') if b >= 0 else s.find('<section id="siga"')
            if k < 0: k = s.find('<footer')
            s = s[:k] + block(lang, items) + s[k:]
        open(p, 'w', encoding='utf-8').write(s)
    print('web stories na página inicial:', len(items))


if __name__ == '__main__':
    main()
