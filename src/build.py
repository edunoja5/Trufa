"""Genera la tienda Trufa a partir de src/template.html.

- public/index.html: la web que publica Netlify (con el Client ID de PayPal).
  Las fotos van aparte en public/img/ (WebP, 900 px) para que la página cargue rápido en el móvil.
- public/img/og.jpg: la imagen que se ve al compartir el enlace (WhatsApp, TikTok, Instagram).
- Si se pasa una ruta como argumento, escribe ahí una vista previa de un solo archivo
  (fotos incrustadas) con el pago desactivado.

El template se divide en <!--HEAD--> (va dentro de <head>) y <!--BODY-->. Lo que va entre
<!--META--> y <!--/META--> (redes, icono, datos para Google) solo sale en la web publicada.
"""
import base64, io, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
SITE = "https://trufa-mascotas.netlify.app"
PAYPAL_CLIENT_ID = "BAAgh8hxJbm1lfDIsZaZvMloUqyHmqF2NuDpXQdgdl9P97z3KDZwD5Z-_6tSCMM5OTyrihogo60SP4aRWk"

def load(name, size=900):
    im = Image.open(ROOT / "fotos" / f"{name}.jpg").convert("RGB")
    im.thumbnail((size, size))
    return im

def img_file(name):
    out = PUBLIC / "img" / f"{name}.webp"
    load(name).save(out, "WEBP", quality=80, method=6)
    return f"img/{name}.webp"

def img_uri(name):
    buf = io.BytesIO()
    load(name, 800).save(buf, "JPEG", quality=80, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def og_image():
    # 1200x630, recorte centrado de la foto del perro con arnés
    im = Image.open(ROOT / "fotos" / "arnes-perro.jpg").convert("RGB")
    w, h = im.size
    target = 1200 / 630
    if w / h > target:
        nw = int(h * target); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(w / target); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im.resize((1200, 630), Image.LANCZOS).save(PUBLIC / "img" / "og.jpg", "JPEG", quality=82, optimize=True)

tpl = (ROOT / "src" / "template.html").read_text()
head, body = tpl.split("<!--BODY-->")
head = head.replace("<!--HEAD-->", "").strip()
head_pub = head.replace("<!--META-->", "").replace("<!--/META-->", "")
pat = r"\{\{IMG:([\w-]+)\}\}"

# Web publicada
(PUBLIC / "img").mkdir(parents=True, exist_ok=True)
files = {}
pub = lambda s: re.sub(pat, lambda m: files.setdefault(m[1], img_file(m[1])), s).replace("{{SITE}}", SITE)
og_image()
page = ("<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        + pub(head_pub) + "\n</head>\n<body>\n" + pub(body).replace("{{PAYPAL_CLIENT_ID}}", PAYPAL_CLIENT_ID).strip()
        + "\n</body>\n</html>\n")
(PUBLIC / "index.html").write_text(page)
used = {f"{n}.webp" for n in files} | {"og.jpg"}
for f in (PUBLIC / "img").iterdir():
    if f.name not in used: f.unlink()

# Vista previa de un solo archivo
if len(sys.argv) > 1:
    cache = {}
    emb = lambda s: re.sub(pat, lambda m: cache.setdefault(m[1], img_uri(m[1])), s).replace("{{SITE}}", SITE)
    # Sin las etiquetas para buscadores y redes (apuntan a archivos que solo existen en Netlify)
    head_prev = re.sub(r"<!--META-->.*?<!--/META-->", "", head, flags=re.S)
    Path(sys.argv[1]).write_text(emb(head_prev) + "\n" + emb(body).replace("{{PAYPAL_CLIENT_ID}}", ""))

kb = lambda p: p.stat().st_size // 1024
print("index.html", kb(PUBLIC / "index.html"), "KB;", {f.name: kb(f) for f in sorted((PUBLIC / "img").iterdir())})
