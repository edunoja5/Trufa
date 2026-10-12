"""Genera la tienda Trufa a partir de src/template.html.

- public/index.html: la web que publica Netlify (con el Client ID de PayPal).
- Si se pasa una ruta como argumento, escribe ahí una vista previa con el pago desactivado.
Las fotos de fotos/*.jpg se incrustan como data URI, redimensionadas a 800 px.
"""
import base64, io, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PAYPAL_CLIENT_ID = "BAAgh8hxJbm1lfDIsZaZvMloUqyHmqF2NuDpXQdgdl9P97z3KDZwD5Z-_6tSCMM5OTyrihogo60SP4aRWk"

def img_uri(name):
    im = Image.open(ROOT / "fotos" / f"{name}.jpg").convert("RGB")
    im.thumbnail((800, 800))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=80, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

tpl = (ROOT / "src" / "template.html").read_text()
cache = {}
body = re.sub(r"\{\{IMG:([\w-]+)\}\}", lambda m: cache.setdefault(m[1], img_uri(m[1])), tpl)

full = "<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n"
(ROOT / "public" / "index.html").write_text(full + body.replace("{{PAYPAL_CLIENT_ID}}", PAYPAL_CLIENT_ID) + "\n</body>\n</html>\n")
preview = body.replace("{{PAYPAL_CLIENT_ID}}", "")
if len(sys.argv) > 1:
    Path(sys.argv[1]).write_text(preview)
print("ok", {k: len(v) // 1024 for k, v in cache.items()}, "KB")
