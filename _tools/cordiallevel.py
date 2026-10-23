import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mea_banner import mea_banner, MEA_CSS
import html
I='https://images.century21.pt/'
Q='?width=900&height=675&quality=85'
P=[ # ref, cat, title, local, price, specs, img, flags
('C0393-01659','casa','T3 na 1.ª linha de mar com 2 lugares de garagem','Leça da Palmeira','550 000 €',['3 quartos','2 WC','171 m²'],'ccf64483-326e-4ce4-911c-4e6b470f5263/PHOTO-2026-09-19-18-11-13.jpg','Descida de preço'),
('C0393-01661','casa','Moradia T4 com vista de mar, para renovar','Foz do Douro, Porto','875 000 €',['4 quartos','2 WC','169 m²'],'52f4c54c-b55b-40b4-802c-b14ddd697acb/F79.jpg','Visita virtual'),
('C0393-01360','casa','T4 na Foz do Douro — propriedade de raiz com usufruto','Foz do Douro, Porto','548 000 €',['4 quartos','4 WC','240 m²'],'0793775f-8fa9-4b00-a603-4d45fcc6e507/casemiroramosuzu-11.jpg','Visita virtual · Descida de preço'),
('C0393-01660','invest','Casa para reabilitação na 2.ª linha de mar, com inquilino vitalício','Foz do Douro, Porto','260 000 €',['2 quartos','1 WC','130 m²'],'6d1229fa-aba9-4ba3-aa1c-7f616fc34096/F65.jpg',''),
('C0393-01555','casa','T2+1 novo com terraço de 27 m² e garagem box','Grande Porto','408 000 €',['2 quartos','2 WC','119 m²'],'ee3138df-2dcd-4ac3-910f-1934997608c8/IMG-20260626-WA0063.jpg',''),
('C0393-01689','casa','T2 remodelado e equipado na Rua Antero de Quental','Porto','349 000 €',['2 quartos','1 WC','78 m²'],'56b2793c-7533-4f13-ac73-c21a0374aede/F-20.jpeg','Visita virtual'),
('C0393-01583','casa','T1 duplex moderno em Cedofeita','Cedofeita, Porto','289 000 €',['1 quarto','1 WC','60 m²'],'d643fa91-bec2-4213-a2eb-d9a59e6d8b2c/ChatGPTImage21072026104531(5).png','Visita virtual'),
('C0393-01530','invest','Prédio no centro do Porto com potencial construtivo','Centro do Porto','790 000 €',['4 quartos','2 WC','363 m²'],'5ce8af44-e7ea-4786-be19-cce048ba1c7a/Fotos-51.jpg',''),
('C0393-01506','terreno','Terreno com projeto em aprovação no centro de Leça da Palmeira','Leça da Palmeira','765 000 €',['220 m²'],'921ec728-8db3-4301-8588-fcfbf01ca6b5/SALA1.jpg','Descida de preço'),
('C0393-01505','terreno','Terreno com projeto em aprovação','Leça da Palmeira','550 000 €',['119 m²'],'50d5dd9a-73e3-4fa6-98a8-f8ef5537c573/VISTAFRENTE.jpg',''),
('C0393-01504','terreno','Terreno com projeto aprovado','Matosinhos','230 000 €',['200 m²'],'0c220128-a9c1-4314-b6df-2518eb866364/PHOTO-2025-10-15-16-05-183.jpg','Descida de preço'),
('C0393-00896','terreno','Terreno urbano na Rua Azevedo','Campanhã, Porto','290 000 €',['1375 m²'],'tempsnip_2e08a5b5-fa83-4819-b913-997f91b15cfa.png',''),
('C0393-01454','terreno','Terreno com PIP em aprovação para 3 moradias','Madalena','165 000 €',['371 m²'],'537a2612-ead3-4faa-9929-b5fcccce4b8c/Fotos-21.jpg',''),
('C0393-01441','terreno','Terreno de 3600 m² junto ao Rio Minho, terra do Alvarinho','Alto Minho','75 000 €',['3610 m²'],'bf81fb5e-ef4c-44a6-9e1d-bd4c2624a7ec/62026-03-11at18.41.30.jpeg',''),
('C0393-01442','terreno','Terreno de 1350 m² junto ao Rio Minho, terra do Alvarinho','Alto Minho','35 000 €',['1352 m²'],'0c42c9a8-d57e-40d0-a2c2-033e2f8155b1/2Image2026-03-11at18.41.28.jpeg',''),
('C0393-01063','invest','Garagem para 14 carros com arrumos e WC','Grande Porto','195 000 €',['1 WC','293 m²'],'z2_9a6cfd8b-6db1-4853-98aa-573ae1f8f1ee.png','Descida de preço'),
('C0393-01728','arrendar','Estúdio renovado e mobilado na Rua de Ourique','Campanhã, Porto','550 € / mês',['1 WC','27 m²'],'e768caf6-ddb1-413d-a35c-0ec40aafdbcc/kjhgfdsw456789-2.jpg','Arrendamento'),
]
AI={'C0393-01583'}
CATS=[('todos','Todos'),('casa','Casas e apartamentos'),('terreno','Terrenos'),('invest','Investimento'),('arrendar','Arrendamento')]
def card(p):
    ref,cat,t,loc,price,specs,img,flag=p
    url=f'https://century21.pt/{"arrendar" if cat=="arrendar" else "comprar"}/{ref}'
    LOCAL={'C0393-01659':('t3leca/','t3leca/img/leca-37-t.jpg'),'C0393-01661':('casaraofoz/','casaraofoz/img/foz-f52-t.jpg'),'C0393-01555':('bosquepicua/',None),'C0393-01689':('anteroquental/','img/antero-20-t.jpg'),'C0393-01441':('moncao/#terreno1','moncao/img/t1-d4-t.jpg'),'C0393-01442':('moncao/#terreno2','moncao/img/t2-d4-t.jpg')}
    tgt=' target="_blank" rel="noopener"'
    img_src=I+img+Q
    if ref in LOCAL:
        url,_im=LOCAL[ref]; tgt='' if not url.startswith('http') else tgt
        if _im: img_src=_im
    ai='<span class="ai">Imagem gerada por IA · ilustrativa</span>' if ref in AI else ''
    fl=f'<span class="flag">{html.escape(flag)}</span>' if flag else ''
    sp=''.join(f'<li>{html.escape(s)}</li>' for s in specs)
    return f'''<a class="prop" data-cat="{cat}" href="{url}"{tgt}>
  <div class="ph"><img src="{img_src}" alt="{html.escape(t)}" loading="lazy" width="900" height="675">{fl}{ai}</div>
  <div class="body"><span class="loc">{html.escape(loc)}</span><h3>{html.escape(t)}</h3><ul class="specs">{sp}</ul><div class="row"><span class="price">{price}</span><span class="ref">Ref. {ref}</span></div></div>
</a>'''
FEAT=('yo7RN7u6JJY','Terrenos junto ao Rio Minho, em Monção','Novo · Vídeo-reportagem · 1 min 45 s',
      'Dois terrenos de cultura e vinha em São Bento (Bela), na terra do Alvarinho, a minutos do rio, das Termas e do centro histórico de Monção.','moncao/','Ver a apresentação dos terrenos')
V=[('xEDuuPNMacM','T3 em Leça da Palmeira, junto às Piscinas das Marés','Vídeo-reportagem · 1 min 42 s','t3leca/'),
   ('vU0bXm_uhGk','T3 em Leça da Palmeira, em formato vertical','Short · 550 000 €','t3leca/'),
   ('7JOcy10W8oY','Novo T1 em Matosinhos, pronto a habitar','Vídeo-reportagem · 10 min',None),
   ('Re8UZQRVTOY','Prédio inteiro na Baixa do Porto, com potencial construtivo','Vídeo-reportagem · 1 min 12 s',None)]
POD=('ed1kwc3x27I','O maior erro ao comprar casa: qual é o seu potencial de financiamento?','Episódio · 26 min')
YTCH='https://www.youtube.com/@CordialLevelPT'
def yt(i,t):
    return f'<button class="yt" data-id="{i}" aria-label="Ver vídeo: {html.escape(t)}"><img src="https://i.ytimg.com/vi/{i}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360"><span class="play" aria-hidden="true"></span></button>'
def vid(v):
    i,t,m,lk=v
    more=f'<a class="vlk" href="{lk}">Ver a apresentação →</a>' if lk else ''
    return f'<figure class="vid">{yt(i,t)}<figcaption><span>{m}</span>{html.escape(t)}{more}</figcaption></figure>'
fi,ft,fm,fd,fl,flt=FEAT
VIDS=(f'''<div class="vfeat">{yt(fi,ft)}<div class="vtxt"><span class="vtag">{fm}</span><h3>{html.escape(ft)}</h3><p>{html.escape(fd)}</p><a class="btn gold" href="{fl}">{flt} →</a><a class="vlk" href="https://www.youtube.com/watch?v={fi}" target="_blank" rel="noopener">Ver no YouTube ↗</a></div></div>
<h3 class="vsub">Vídeo-reportagens</h3>
<div class="vgrid">{''.join(vid(v) for v in V)}</div>
<div class="pod">{yt(POD[0],POD[1])}<div class="vtxt"><span class="vtag">Podcast · Panorama Imobiliário PT</span><h3>Conversas sobre o mercado e as decisões de quem compra casa</h3><p>Episódios sobre o que pesa numa compra de casa: financiamento, preço, timing e negociação.</p><p class="ep"><b>{html.escape(POD[1])}</b><span>{POD[2]}</span></p></div></div>
<div class="vcta"><a class="btn gold" href="{YTCH}?sub_confirmation=1" target="_blank" rel="noopener">Subscrever o canal no YouTube</a><a class="btn ghost" href="{YTCH}/videos" target="_blank" rel="noopener">Ver todos os vídeos ↗</a></div>''')
ICON='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/><path d="M9 9.5c.3 1.8 1.8 3.6 3.6 4.4l1.2-1.1 2 .9-.4 1.6c-3.2.3-6.9-3.2-6.8-6.6l1.6-.4.9 2z"/></svg>'
def wam(n,nome): return f'https://wa.me/{n}?text='+__import__('urllib.parse').parse.quote(f'Olá {nome}, vi o site da Cordial Level e gostaria de mais informações.')
BAR='<nav class="bar" aria-label="Contacto rápido por WhatsApp"><p class="bar-lbl">Fale diretamente connosco</p>'+''.join(f'<a href="{wam(n,c)}" target="_blank" rel="noopener" aria-label="Fale comigo: WhatsApp {f}">{ICON}{c}</a>' for n,c,f in [('351935101667','Casemiro','Casemiro Ramos'),('351912706395','Francisco','Francisco Medeiros')])+'</nav>'
WA='https://wa.me/351912988971?text=Ol%C3%A1%20Freire%2C%20vi%20o%20site%20da%20Cordial%20Level%20e%20gostaria%20de%20saber%20mais%20sobre%20os%20servi%C3%A7os%20da%20Usina%20V%C3%ADdeos.'
tabs=''.join(f'<button class="tab{" on" if k=="todos" else ""}" data-f="{k}" aria-pressed="{"true" if k=="todos" else "false"}">{n}</button>' for k,n in CATS)
props='\n'.join(card(p) for p in P)
vids=VIDS
out=open('_tools/cordiallevel_template.html').read().replace('{{TABS}}',tabs).replace('{{PROPS}}',props).replace('{{VIDS}}',vids).replace('{{WA}}',WA).replace('{{N}}',str(len(P))).replace('{{BAR}}',BAR).replace('{{MEA}}',mea_banner('pt','cordiallevel')).replace('{{MEACSS}}',MEA_CSS)
open('cordiallevel/index.html','w').write(out)
print('ok',len(out))
