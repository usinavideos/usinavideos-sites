"""Banner "Siga nas redes" para Cordial Level e Usina Vídeos (HTML + CSS, sem dependências).

social_banner('cl' | 'usina', source) devolve o bloco; SOCIAL_CSS vai no <style>.
"""
YT = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="1.5" y="5" width="21" height="14" rx="4" fill="#FF0033"/><path d="M10 9v6l5.2-3z" fill="#fff"/></svg>'
IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><defs><linearGradient id="igg" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#FEDA75"/><stop offset=".45" stop-color="#D62976"/><stop offset="1" stop-color="#4F5BD5"/></linearGradient></defs><rect x="2" y="2" width="20" height="20" rx="6" fill="url(#igg)"/><circle cx="12" cy="12" r="4.4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.3" fill="#fff"/></svg>'
FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10.5" fill="#1877F2"/><path d="M13.3 20v-6h2l.4-2.5h-2.4V10c0-.7.3-1.3 1.4-1.3h1.1V6.6c-.3 0-1-.1-1.9-.1-2 0-3.1 1.2-3.1 3.2v1.8H8.7V14h2.1v6z" fill="#fff"/></svg>'
IN = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="4" fill="#0A66C2"/><path d="M7 10h2.3v7H7zM8.1 6.5a1.3 1.3 0 1 1 0 2.6 1.3 1.3 0 0 1 0-2.6zM10.8 10H13v1c.3-.6 1.1-1.2 2.3-1.2 2.4 0 2.8 1.6 2.8 3.6V17h-2.3v-3.2c0-.8 0-1.8-1.1-1.8s-1.3.9-1.3 1.8V17h-2.3z" fill="#fff"/></svg>'

BRANDS = {
    'cl': dict(cls='sb-cl', eb='Siga a Cordial Level', h='Os novos imóveis chegam primeiro às redes.',
               p='Vídeo-reportagens, Shorts e o podcast Panorama Imobiliário PT. Subscreva e ative as notificações.',
               items=[('yt', YT, 'YouTube', '@CordialLevelPT', 'Subscrever', 'https://www.youtube.com/@CordialLevelPT?sub_confirmation=1'),
                      ('ig', IG, 'Instagram', '@cordiallevel', 'Seguir', 'https://www.instagram.com/cordiallevel/'),
                      ('fb', FB, 'Facebook', '/cordiallevel', 'Seguir', 'https://www.facebook.com/cordiallevel/')]),
    'usina': dict(cls='sb-us', eb='Siga a Usina Vídeos', h='Bastidores e trabalhos novos todas as semanas.',
                  p='Reportagens, making of e dicas de comunicação nas redes da Usina e no canal do Motores e Ação.',
                  items=[('ig', IG, 'Instagram', '@usina.videos', 'Seguir', 'https://www.instagram.com/usina.videos'),
                         ('fb', FB, 'Facebook', '/usinacomvideos', 'Seguir', 'https://www.facebook.com/usinacomvideos'),
                         ('yt', YT, 'YouTube', 'Motores e Ação · @motoreseacao', 'Subscrever', 'https://www.youtube.com/@motoreseacao?sub_confirmation=1'),
                         ('in', IN, 'LinkedIn', 'Freire Neto', 'Seguir', 'https://www.linkedin.com/in/freireneto/')]),
}


TR = {'en': dict(eb='Follow Usina Vídeos', h='New work and behind-the-scenes every week.', p='Reports, making-of and communication tips on Usina\'s channels and on Motores e Ação.', s='Follow', y='Subscribe'),
      'es': dict(eb='Siga a Usina Vídeos', h='Trabajos nuevos y making of cada semana.', p='Reportajes, making of y consejos de comunicación en las redes de Usina y en el canal de Motores e Ação.', s='Seguir', y='Suscribirse')}


def social_banner(brand='cl', lang='pt'):
    b = dict(BRANDS[brand])
    if brand == 'usina' and lang in TR:
        t = TR[lang]
        b.update(eb=t['eb'], h=t['h'], p=t['p'], items=[(k, svg, n, h, t['y'] if k == 'yt' else t['s'], u) for k, svg, n, h, c, u in b['items']])
    items = ''.join(f'<a class="sb-i sb-{k}" href="{u}" target="_blank" rel="noopener">{svg}<span><b>{n}</b><small>{h}</small></span><em>{c} →</em></a>' for k, svg, n, h, c, u in b['items'])
    return (f'<div class="sb {b["cls"]}"><div class="sb-t"><span class="sb-eb">{b["eb"]}</span><h3>{b["h"]}</h3><p>{b["p"]}</p></div>'
            f'<div class="sb-l">{items}</div></div>')


SOCIAL_CSS = """
.sb{border-radius:22px;padding:34px 30px;display:grid;gap:26px;align-items:center;box-shadow:0 12px 34px rgba(0,0,0,.18)}
@media(min-width:960px){.sb{grid-template-columns:1fr 1.25fr;padding:42px 44px}}
.sb .sb-eb{display:block;font-size:12px;font-weight:800;letter-spacing:.2em;text-transform:uppercase}
.sb h3{color:#fff!important;margin:8px 0 0;font-size:clamp(24px,3vw,34px);line-height:1.12;font-weight:800}
.sb p{margin:12px 0 0!important;font-size:16px;line-height:1.55;color:rgba(255,255,255,.82)!important}@media(min-width:560px){.sb-l .sb-yt,.sb-l .sb-in{grid-column:1/-1}}
.sb>*{min-width:0}.sb-l{display:grid;gap:10px;min-width:0}.sb-i{min-width:0}@media(min-width:560px){.sb-l{grid-template-columns:1fr 1fr}}
.sb-i{display:flex;align-items:center;gap:12px;padding:14px 16px;border-radius:14px;text-decoration:none;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);transition:transform .2s,background .2s}
.sb-i:hover{transform:translateY(-2px);background:rgba(255,255,255,.14)}
.sb-i svg{width:36px;height:36px;flex:none}.sb-i span{display:flex;flex-direction:column;min-width:0}
.sb-i b{font-size:16px;color:#fff}.sb-i small{font-size:13px;color:rgba(255,255,255,.72);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sb-i em{margin-left:auto;flex:none;font-style:normal;font-weight:800;font-size:13px;white-space:nowrap}
.sb .sb-i.sb-yt em{color:#fff}.sb-i.sb-yt{background:#FF0033;border-color:#FF0033}.sb-i.sb-yt small{color:rgba(255,255,255,.85)}.sb-i.sb-yt em{color:#fff}
.sb-i.sb-yt svg rect{fill:#fff}.sb-i.sb-yt svg path{fill:#FF0033}
.sb-cl{background:linear-gradient(135deg,#0F2438,#1B3A57);color:#fff;border-bottom:5px solid #C9A45C}.sb-cl .sb-eb{color:#D4B562}.sb-cl .sb-i em{color:#D4B562}
.sb-us{background:#141213;color:#fff;border-bottom:5px solid #E5AE29}.sb-us .sb-eb{color:#E5AE29}.sb-us .sb-i em{color:#E5AE29}
"""
