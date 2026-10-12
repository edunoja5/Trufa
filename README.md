# Trufa

Tienda online de accesorios para perros y gatos: https://trufa-mascotas.netlify.app

- `src/template.html`: la web (diseño, productos, textos legales y pago con PayPal).
- `fotos/`: fotos de producto. Al generar la web se convierten a WebP en `public/img/`.
- `src/build.py`: genera `public/index.html`, `public/img/` y la imagen para compartir (`python3 src/build.py`). Necesita Pillow.
- `public/`: lo que publica Netlify. Cada cambio en `main` se publica solo.

Despliegue automático: cada push a main publica la web en Netlify.
