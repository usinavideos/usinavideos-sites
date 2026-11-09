"""Protege uma página estática com palavra-passe (AES-256-GCM, PBKDF2-SHA256 250 000 iterações).

Uso: python3 _tools/cifrar_pagina.py <pasta/index.html> "PALAVRA-PASSE" "Título visível"
A página original é cifrada e substituída por um ecrã de acesso (noindex). As imagens
ficam na mesma pasta, com os mesmos caminhos relativos.
"""
import base64, os, sys, html
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

path, pw, titulo = sys.argv[1], sys.argv[2].encode(), sys.argv[3]
src = open(path, encoding='utf-8').read()
salt, iv = os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(hashes.SHA256(), 32, salt, 250_000).derive(pw)
ct = AESGCM(key).encrypt(iv, src.encode(), None)
b = lambda x: base64.b64encode(x).decode()
t = html.escape(titulo)
shell = f'''<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive"><title>{t} · acesso reservado</title>
<link rel="icon" href="/img/logo/usina-simbolo.svg" type="image/svg+xml">
<style>body{{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#141213;color:#F2F0EB;font-family:Mulish,system-ui,sans-serif;padding:20px}}
.g{{width:100%;max-width:400px;background:#1E1B1C;border:1px solid #34302F;border-radius:18px;padding:28px}}.g img{{height:34px;margin-bottom:18px}}
h1{{font-size:22px;margin:0 0 6px}}p{{color:#A9A3A0;margin:0 0 18px;font-size:15px}}input{{width:100%;box-sizing:border-box;padding:13px;border-radius:10px;border:1px solid #34302F;background:#141213;color:#fff;font:inherit;margin-bottom:12px}}
button{{width:100%;padding:13px;border:0;border-radius:999px;background:#E5AE29;color:#141213;font-weight:800;font:inherit;font-weight:800;cursor:pointer}}.e{{color:#E5776B;font-size:14px;margin-top:10px;display:none}}</style></head>
<body><form class="g" id="f" autocomplete="off"><img src="/img/logo/usina-horizontal-claro.svg" alt="Usina Vídeos"><h1>{t}</h1><p>Pré-visualização reservada. Introduza a palavra-passe que recebeu da Usina Vídeos.</p>
<input id="pw" type="password" placeholder="Palavra-passe" required autofocus><button>Ver a página</button><div class="e" id="e">Palavra-passe incorreta.</div></form>
<script>const P={{salt:"{b(salt)}",iv:"{b(iv)}",ct:"{b(ct)}"}};const b=s=>Uint8Array.from(atob(s),c=>c.charCodeAt(0));
async function open_(pw){{const k0=await crypto.subtle.importKey("raw",new TextEncoder().encode(pw),"PBKDF2",false,["deriveKey"]);
const k=await crypto.subtle.deriveKey({{name:"PBKDF2",salt:b(P.salt),iterations:250000,hash:"SHA-256"}},k0,{{name:"AES-GCM",length:256}},false,["decrypt"]);
const h=new TextDecoder().decode(await crypto.subtle.decrypt({{name:"AES-GCM",iv:b(P.iv)}},k,b(P.ct)));
try{{sessionStorage.setItem("pw:"+location.pathname,pw)}}catch(e){{}}
document.open();document.write(h.replace("<head>",'<head><meta name="robots" content="noindex, nofollow, noarchive">'));document.close();}}
document.getElementById("f").addEventListener("submit",async ev=>{{ev.preventDefault();try{{await open_(document.getElementById("pw").value)}}catch(e){{document.getElementById("e").style.display="block"}}}});
try{{const s=sessionStorage.getItem("pw:"+location.pathname);if(s)open_(s).catch(()=>{{}})}}catch(e){{}}</script></body></html>
'''
open(path, 'w', encoding='utf-8').write(shell)
print('ok', path, len(shell) // 1024, 'KB')
