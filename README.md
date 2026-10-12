# Trufa

Tienda online de accesorios para perros y gatos: https://trufa-mascotas.netlify.app

- `src/template.html`: la web (diseño, productos, textos legales y pago con PayPal).
- `fotos/`: fotos de producto. Se incrustan en la web al generarla.
- `src/build.py`: genera `public/index.html` (`python3 src/build.py`). Necesita Pillow.
- `public/`: lo que publica Netlify. Cada cambio en `main` se publica solo.

Despliegue automático: cada push a main publica la web en Netlify.
