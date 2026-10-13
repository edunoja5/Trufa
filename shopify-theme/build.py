import json, re, copy
SP='/tmp/claude-0/-home-claude-trufa/fd380adf-1ec3-5561-8ad4-d8a7821ba5e1/scratchpad/'
def strip(s):  # remove leading /* */ comment
    return json.loads(re.sub(r'^\s*/\*.*?\*/','',s,flags=re.S))

CSS = """<style>
.tf{--tb:#2242C4;--tt:#14211D;--ty:#FFD54A;--tm:#56635E;--tc:#FFF4D6;--tl:#F6F3EC;color:var(--tt)}
.tf *{box-sizing:border-box}
.tf h1,.tf h2,.tf h3{color:var(--tt);margin:0;letter-spacing:-.01em}
.tf p{margin:0}
.tf a.tf-btn{display:inline-block;background:var(--tb);color:#fff;text-decoration:none;font-weight:700;padding:15px 28px;border-radius:999px;font-size:16px;transition:transform .15s,box-shadow .15s}
.tf a.tf-btn:hover{transform:translateY(-1px);box-shadow:0 8px 20px rgba(34,66,196,.25)}
.tf-eyebrow{display:inline-block;background:var(--ty);color:var(--tt);font-weight:700;font-size:13px;padding:6px 12px;border-radius:999px;margin-bottom:16px}
.tf-hero{display:grid;grid-template-columns:1.05fr 1fr;gap:40px;align-items:center;background:var(--tc);border-radius:28px;padding:56px;overflow:hidden}
.tf-hero h1{font-size:clamp(34px,5vw,58px);line-height:1.05;margin-bottom:18px}
.tf-hero p.tf-lead{font-size:18px;line-height:1.5;color:var(--tm);margin-bottom:28px;max-width:30em}
.tf-hero__img{background:#fff;border-radius:22px;overflow:hidden;aspect-ratio:1/1}
.tf-hero__img img{width:100%;height:100%;object-fit:cover;display:block}
.tf-checks{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:22px;padding:0;list-style:none;font-size:14px;color:var(--tm)}
.tf-checks li:before{content:"\\2713";color:var(--tb);font-weight:800;margin-right:6px}
.tf-perks{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.tf-perk{display:flex;gap:12px;align-items:center;background:var(--tl);border-radius:18px;padding:18px}
.tf-perk svg{flex:0 0 34px;width:34px;height:34px;color:var(--tb)}
.tf-perk b{display:block;font-size:15px}
.tf-perk span{font-size:13px;color:var(--tm)}
.tf-h2{font-size:clamp(28px,3.4vw,40px);line-height:1.1;text-align:center;margin-bottom:10px}
.tf-sub{text-align:center;color:var(--tm);font-size:17px;margin:0 auto 36px;max-width:36em}
.tf-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.tf-card{background:#fff;border:1px solid #ECE7DC;border-radius:22px;overflow:hidden;display:flex;flex-direction:column;text-decoration:none;color:inherit;transition:transform .15s,box-shadow .15s}
.tf-card:hover{transform:translateY(-3px);box-shadow:0 14px 30px rgba(20,33,29,.08)}
.tf-card__img{aspect-ratio:1/1;background:#fff}
.tf-card__img img{width:100%;height:100%;object-fit:cover;display:block}
.tf-card__body{padding:20px 22px 24px;display:flex;flex-direction:column;gap:8px;flex:1}
.tf-card__q{font-size:13px;font-weight:700;color:var(--tb);text-transform:uppercase;letter-spacing:.04em}
.tf-card h3{font-size:21px;line-height:1.2}
.tf-card p{color:var(--tm);font-size:15px;line-height:1.5;flex:1}
.tf-card__go{font-weight:700;margin-top:6px}
.tf-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;counter-reset:s}
.tf-step{background:var(--tl);border-radius:22px;padding:26px}
.tf-step:before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:38px;height:38px;border-radius:50%;background:var(--ty);font-weight:800;margin-bottom:14px}
.tf-step h3{font-size:19px;margin-bottom:6px}
.tf-step p{color:var(--tm);font-size:15px;line-height:1.5}
.tf-faq{max-width:760px;margin:0 auto}
.tf-faq details{border-bottom:1px solid #E6E1D6;padding:18px 0}
.tf-faq summary{cursor:pointer;font-weight:700;font-size:17px;list-style:none;display:flex;justify-content:space-between;gap:16px}
.tf-faq summary::-webkit-details-marker{display:none}
.tf-faq summary:after{content:"+";font-size:24px;line-height:1;color:var(--tb)}
.tf-faq details[open] summary:after{content:"\\2212"}
.tf-faq details p{margin-top:10px;color:var(--tm);line-height:1.6}
.tf-faq .tf-more{text-align:center;margin-top:24px}
.tf-faq .tf-more a{color:var(--tb);font-weight:700}
.tf-cta{background:var(--tb);color:#fff;border-radius:28px;padding:52px 32px;text-align:center}
.tf-cta h2{color:#fff;font-size:clamp(28px,3.6vw,42px);line-height:1.1;margin-bottom:12px}
.tf-cta p{opacity:.9;font-size:17px;margin-bottom:26px}
.tf-cta .tf-code{display:inline-block;background:var(--ty);color:var(--tt);font-weight:800;letter-spacing:.08em;padding:4px 12px;border-radius:8px}
.tf-cta a.tf-btn{background:#fff;color:var(--tb)}
@media (max-width:989px){.tf-perks{grid-template-columns:repeat(2,1fr)}}
@media (max-width:749px){
.tf-hero{grid-template-columns:1fr;padding:22px 20px 30px;gap:22px;border-radius:22px}
.tf-hero__img{order:-1}
.tf-hero p.tf-lead{font-size:16px}
.tf a.tf-btn{display:block;text-align:center}
.tf-perks{grid-template-columns:1fr 1fr;gap:10px}
.tf-perk{flex-direction:column;align-items:flex-start;padding:14px}
.tf-cards,.tf-steps{grid-template-columns:1fr}
.tf-cta{padding:38px 20px;border-radius:22px}
}
</style>"""

HERO = CSS + """
{%- assign hp = all_products['arnes-antitirones-acolchado'] -%}
<div class="tf"><div class="tf-hero">
  <div>
    <span class="tf-eyebrow">Para perros y gatos · Envío a toda España</span>
    <h1>Menos barro, menos pelo, más paseos.</h1>
    <p class="tf-lead">Accesorios sencillos que resuelven los líos de cada día con tu mascota. Probados, fáciles de usar y con 30 días para devolverlos.</p>
    <a class="tf-btn" href="/collections/nuestros-productos">Ver los productos</a>
    <ul class="tf-checks"><li>Envío gratis desde 39 €</li><li>Devolución en 30 días</li><li>Pago 100 % seguro</li></ul>
  </div>
  <div class="tf-hero__img">{%- if hp.featured_image -%}{{ hp.featured_image | image_url: width: 900 | image_tag: loading: 'eager', fetchpriority: 'high', widths: '450, 700, 900', sizes: '(min-width: 750px) 45vw, 100vw', alt: 'Perro paseando con el arnés antitirones de Trufa' }}{%- endif -%}</div>
</div></div>"""

ICON = {
 'truck':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h11v9H3z"/><path d="M14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/></svg>',
 'back':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 14 4 9l5-5"/><path d="M4 9h10.5a5.5 5.5 0 0 1 0 11H11"/></svg>',
 'lock':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>',
 'chat':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>',
}
PERKS = """<div class="tf"><div class="tf-perks">
<div class="tf-perk">%s<div><b>Envío gratis desde 39 €</b><span>Con seguimiento, 6–12 días</span></div></div>
<div class="tf-perk">%s<div><b>30 días de devolución</b><span>Sin dar explicaciones</span></div></div>
<div class="tf-perk">%s<div><b>Pago seguro</b><span>Tarjeta, Apple Pay, Google Pay, PayPal</span></div></div>
<div class="tf-perk">%s<div><b>Atención en español</b><span>Respuesta en 24 h laborables</span></div></div>
</div></div>""" % (ICON['truck'],ICON['back'],ICON['lock'],ICON['chat'])

def card(handle, q, h, p, go):
    return """{%%- assign p = all_products['%s'] -%%}
<a class="tf-card" href="{{ p.url }}"><div class="tf-card__img">{%%- if p.featured_image -%%}{{ p.featured_image | image_url: width: 700 | image_tag: loading: 'lazy', widths: '350, 700', sizes: '(min-width: 750px) 30vw, 100vw' }}{%%- endif -%%}</div>
<div class="tf-card__body"><span class="tf-card__q">%s</span><h3>%s</h3><p>%s</p><span class="tf-card__go">%s · {{ p.price | money }} →</span></div></a>""" % (handle,q,h,p,go)

SOLS = """<div class="tf"><h2 class="tf-h2">Tres problemas de cada día, resueltos</h2>
<p class="tf-sub">Elegimos cada producto porque arregla algo que nos pasaba a nosotros con nuestros perros.</p>
<div class="tf-cards">""" + card('limpiador-de-patas-portatil','¿Huellas de barro en casa?','Patas limpias en 10 segundos','Mete la pata, gira el vaso y sale limpia, solo con agua. Sin toallitas ni sofás manchados.','Ver limpiador') + card('cepillo-con-vapor-3-en-1','¿Pelo por todas partes?','El pelo se queda en el cepillo','Su vapor frío humedece el pelo suelto para que no salga volando por la casa ni se pegue a la ropa.','Ver cepillo') + card('arnes-antitirones-acolchado','¿Tira de la correa?','Paseos sin tirones en el cuello','La anilla del pecho reparte el tirón por el torso. Acolchado, reflectante y con asa para sujetarlo.','Ver arnés') + "</div></div>"

STEPS = """<div class="tf"><h2 class="tf-h2">Comprar en Trufa es fácil</h2>
<p class="tf-sub">Sin letra pequeña: sabes lo que pagas y cuándo llega.</p>
<div class="tf-steps">
<div class="tf-step"><h3>Eliges y pagas seguro</h3><p>Precio final con impuestos incluidos. Con el código HOLA10 te ahorras un 10 % en tu primer pedido.</p></div>
<div class="tf-step"><h3>Te lo enviamos con seguimiento</h3><p>Lo preparamos en 1–3 días laborables y llega en 6–12 días laborables. Sin aduanas ni sorpresas al recibirlo.</p></div>
<div class="tf-step"><h3>Si no te convence, lo devuelves</h3><p>Tienes 30 días para devolverlo y 3 años de garantía. Escríbenos y te ayudamos en español.</p></div>
</div></div>"""

FAQS=[('¿Cuánto tarda mi pedido?','Lo preparamos en 1 a 3 días laborables y llega en 6 a 12 días laborables. Te enviamos el seguimiento por email.'),
('¿Cuánto cuesta el envío?','3,95 €. Gratis en pedidos desde 39 €.'),
('¿Tendré que pagar aduanas?','No. Los impuestos y aranceles ya están incluidos en el precio.'),
('¿Qué talla de arnés elijo?','Mide el contorno del pecho justo detrás de las patas delanteras: S 35–50 cm, M 45–65 cm, L 60–80 cm, XL 75–100 cm.'),
('¿Y si no me convence?','Tienes 30 días desde la entrega para devolverlo sin dar explicaciones. Escríbenos y te decimos cómo.')]
FAQ = '<div class="tf"><div class="tf-faq"><h2 class="tf-h2">Preguntas frecuentes</h2><p class="tf-sub">Lo que más nos preguntáis antes de comprar.</p>' + ''.join('<details><summary>%s</summary><p>%s</p></details>'%x for x in FAQS) + '<p class="tf-more"><a href="/pages/preguntas-frecuentes">Ver todas las preguntas</a></p></div></div>'

CTA = """<div class="tf"><div class="tf-cta"><h2>10 % de descuento en tu primer pedido</h2>
<p>Usa el código <span class="tf-code">HOLA10</span> al pagar. Envío gratis desde 39 €.</p>
<a class="tf-btn" href="/collections/nuestros-productos">Ir a la tienda</a></div></div>"""

def cl(content, top, bottom, width='page-width'):
    return {"type":"custom-liquid","settings":{"custom_liquid":content,"section_width":width,"padding-block-start":top,"padding-block-end":bottom}}

idx = strip(open(SP+'index_orig.json').read()) if False else None

plist = {"type":"product-list","blocks":{
 "static-header":{"type":"_product-list-content","static":True,"settings":{"content_direction":"row","horizontal_alignment":"space-between","vertical_alignment":"flex-end","align_baseline":True,"gap":12,"width":"fill"},
   "blocks":{"t1":{"type":"_product-list-text","settings":{"text":"<h2>Nuestros productos</h2>","type_preset":"h3","width":"fit-content","alignment":"left"},"blocks":{}},
             "b1":{"type":"_product-list-button","settings":{"label":"Ver todo","style_class":"link","width":"fit-content"},"blocks":{}}},
   "block_order":["t1","b1"]},
 "static-product-card":{"type":"_product-card","static":True,"settings":{"product_card_gap":6,"border":"none","border_radius":0},
   "blocks":{"g1":{"type":"_product-card-gallery","settings":{"image_ratio":"square","border":"none","border_radius":16},"blocks":{}},
             "pt":{"type":"product-title","settings":{"type_preset":"h5","alignment":"left","padding-block-start":6},"blocks":{}},
             "pr":{"type":"price","settings":{"show_sale_price_first":True,"type_preset":"paragraph","alignment":"left"},"blocks":{}}},
   "block_order":["g1","pt","pr"]}},
 "settings":{"collection":"nuestros-productos","layout_type":"grid","carousel_on_mobile":False,"max_products":12,"columns":3,"mobile_columns":"2","columns_gap":16,"rows_gap":28,"section_width":"page-width","horizontal_alignment":"flex-start","gap":28,"padding-block-start":56,"padding-block-end":40}}

index = {"sections":{
 "tf_hero":cl(HERO,16,20),
 "tf_perks":cl(PERKS,0,8),
 "tf_products":plist,
 "tf_solutions":cl(SOLS,40,56),
 "tf_steps":cl(STEPS,8,56),
 "tf_faq":cl(FAQ,8,56),
 "tf_cta":cl(CTA,0,64)},
 "order":["tf_hero","tf_perks","tf_products","tf_solutions","tf_steps","tf_faq","tf_cta"]}

header = {"type":"header","name":"t:names.header","sections":{
 "header_announcements_9jGBFp":{"type":"header-announcements","blocks":{
   "a1":{"type":"_announcement","settings":{"text":"<p>10 % de descuento en tu primer pedido con el código <strong>HOLA10</strong></p>","font":"var(--font-subheading--family)","font_size":"0.8125rem","letter_spacing":"normal","case":"none"},"blocks":{}},
   "a2":{"type":"_announcement","settings":{"text":"<p>Envío gratis desde 39 € · Impuestos y aranceles incluidos</p>","font":"var(--font-subheading--family)","font_size":"0.8125rem","letter_spacing":"normal","case":"none"},"blocks":{}}},
  "block_order":["a1","a2"],"name":"t:names.announcement_bar",
  "settings":{"speed":5,"section_width":"page-width","background_color":"#FFD54A","divider_width":0,"divider_color":"{{ settings.color_palette.color2 }}","padding-block-start":10,"padding-block-end":10}},
 "header_section":{"type":"header","blocks":{
   "header-logo":{"type":"_header-logo","static":True,"settings":{"hide_logo_on_home_page":False,"padding-block-start":0,"padding-block-end":0},"blocks":{}},
   "header-menu":{"type":"_header-menu","static":True,"settings":{"menu":"main-menu","type_font_primary_size":"0.9375rem","menu_font_style":"inverse","type_font_primary_link":"body","type_case_primary_link":"none","menu_style":"featured_products","featured_products_aspect_ratio":"1 / 1","featured_collections_aspect_ratio":"16 / 9","image_border_radius":12,"navigation_bar":False,"drawer_accordion":False,"drawer_accordion_expand_first":False,"drawer_dividers":False},"blocks":{}}},
  "settings":{"logo_position":"left","menu_position":"left","menu_row":"top","show_search":True,"search_position":"right","search_row":"top","show_country":False,"country_selector_style":False,"show_language":False,"localization_font":"heading","localization_font_size":"0.875rem","localization_position":"right","localization_row":"top","section_width":"page-width","section_height":"standard","enable_sticky_header":"always","divider_width":1,"divider_size":"full-width","border_width":0,"background_color_top":"{{ settings.color_palette.background }}","enable_transparent_header_home":False,"enable_transparent_header_product":False,"enable_transparent_header_collection":False}}},
 "order":["header_announcements_9jGBFp","header_section"]}

FOOT_LINKS = """<div style="display:flex;flex-direction:column;gap:8px;font-size:15px">
<strong style="font-size:16px">Trufa</strong>
<span style="opacity:.75">Accesorios sencillos para perros y gatos. Envío a toda España.</span>
<a href="/collections/nuestros-productos">Productos</a>
<a href="/pages/preguntas-frecuentes">Preguntas frecuentes</a>
<a href="/pages/contact">Contacto</a>
<a href="mailto:infoheravia@gmail.com">infoheravia@gmail.com</a>
</div>"""

footer = {"type":"footer","name":"t:names.footer","sections":{
 "footer_m9NzUG":{"type":"footer","blocks":{
   "links_tf":{"type":"custom-liquid","settings":{"custom_liquid":FOOT_LINKS},"blocks":{}},
   "group_H6VpwJ":{"type":"group","settings":{"content_direction":"column","vertical_on_mobile":True,"horizontal_alignment":"flex-start","vertical_alignment":"center","horizontal_alignment_flex_direction_column":"flex-start","vertical_alignment_flex_direction_column":"center","gap":6,"width":"fill","height":"fit"},
     "blocks":{"text_LWt8Pz":{"type":"text","settings":{"text":"<h2>Únete a la familia Trufa</h2>","type_preset":"h4","width":"100%","alignment":"left"},"blocks":{}},
               "text_f9CFLH":{"type":"text","settings":{"text":"<p>Consejos para tu mascota y ofertas antes que nadie. Sin spam.</p>","type_preset":"rte","width":"100%","alignment":"left"},"blocks":{}}},
     "block_order":["text_LWt8Pz","text_f9CFLH"]},
   "email_signup_crihX7":{"type":"email-signup","settings":{"width":"fill","heading_preset":"h3","border_style":"all","input_style":"custom","border_width":1,"border_radius":100,"input_background_color":"{{ settings.color_palette.background }}","input_text_color":"{{ settings.color_palette.color1 }}","input_border_color":"{{ settings.color_palette.color2 }}","input_type_preset":"paragraph","style_class":"button-unstyled","display_type":"arrow","label":"Suscribirme","integrated_button":True,"button_type_preset":"paragraph"},"blocks":{}}},
  "block_order":["links_tf","group_H6VpwJ","email_signup_crihX7"],"name":"t:names.footer",
  "settings":{"section_width":"page-width","gap":32,"background_color":"#F6F3EC","padding-block-start":48,"padding-block-end":40}},
 "footer_utilities_jLGE8U":{"type":"footer-utilities","blocks":{
   "footer_copyright_jweRK8":{"type":"footer-copyright","settings":{"show_powered_by":False,"font_size":"0.75rem","case":"none"},"blocks":{}},
   "footer_policy_list_VCdnpa":{"type":"footer-policy-list","settings":{"font_size":"0.75rem","case":"none"},"blocks":{}},
   "payments_tf":{"type":"payment-icons","settings":{},"blocks":{}}},
  "block_order":["footer_copyright_jweRK8","footer_policy_list_VCdnpa","payments_tf"],"name":"t:names.utilities",
  "settings":{"section_width":"page-width","gap":24,"divider_thickness":1,"divider_color":"{{ settings.color_palette.color2 }}","background_color":"#F6F3EC","padding-block-start":20,"padding-block-end":40}}},
 "order":["footer_m9NzUG","footer_utilities_jLGE8U"]}

out = {"index":json.dumps(index,ensure_ascii=False,indent=2),"header":json.dumps(header,ensure_ascii=False,indent=2),"footer":json.dumps(footer,ensure_ascii=False,indent=2)}
json.dump(out,open('out.json','w'),ensure_ascii=False)
print({k:len(v) for k,v in out.items()})
