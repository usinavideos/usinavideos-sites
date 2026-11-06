"""Radar de Mercado Cordial Level: gera a página privada (cifrada) de uma semana.

Uso: python3 _tools/radar_cordial.py 2026-semana-43 "PALAVRA-PASSE"
Fonte: _tools/radar/<semana>/artigo.html + shell.html; gráficos SVG em
cordiallevel/radar/<semana>/img/. AES-256-GCM, PBKDF2-SHA256 250 000 iterações.
"""
import base64, os, re, sys, pathlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ROOT = pathlib.Path(__file__).resolve().parent.parent
week, password = sys.argv[1], sys.argv[2].encode()
SRC = ROOT / '_tools/radar' / week
PAGE = ROOT / 'cordiallevel/radar' / week

def svg(name):
    s = (PAGE / 'img' / f'{name}.svg').read_text()
    s = re.sub(r'<\?xml.*?\?>', '', s, flags=re.S)
    s = re.sub(r'<!DOCTYPE.*?>', '', s, flags=re.S)
    return re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)

body = (SRC / 'artigo.html').read_text()
for k, n in (('G1', 'grafico-1-preco-vs-valor'), ('G2', 'grafico-2-yield-por-escalao'), ('G3', 'grafico-3-distritos')):
    body = body.replace('{{%s}}' % k, svg(n))
salt, iv = os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(hashes.SHA256(), 32, salt, 250_000).derive(password)
ct = AESGCM(key).encrypt(iv, body.encode(), None)
b = lambda x: base64.b64encode(x).decode()
shell = (SRC / 'shell.html').read_text()
shell = shell.replace('{{SALT}}', b(salt)).replace('{{IV}}', b(iv)).replace('{{CT}}', b(ct))
(PAGE / 'index.html').write_text(shell)
print('ok', PAGE / 'index.html', len(shell) // 1024, 'KB')
