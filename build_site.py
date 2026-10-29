"""Writes the static macapartmentstexas.com site (EN + ES) into the folder given as argv[1]."""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])
ADDR = "3807 S Veterans Blvd, Building H, Edinburg, TX 78542"
MAP = "https://www.google.com/maps/search/?api=1&query=3807+S+Veterans+Blvd+Edinburg+TX+78542"
PHONE = "(956) 238-9914"
TEL = "+19562389914"
EMAIL = "contact@macapartmentstexas.com"
UPDATED_EN = "October 28, 2026"
UPDATED_ES = "28 de octubre de 2026"

T = {
  "en": dict(lang="en", root="", home="index.html", apts="apartments.html", privacy="privacy.html", terms="terms.html",
             nav=("Home", "Privacy Policy", "Terms", "Apartments"), other="Español", other_href={"index.html": "es/index.html", "apartments.html": "es/departamentos.html", "privacy.html": "es/privacidad.html", "terms.html": "es/terminos.html", "sms-consent.html": "es/consentimiento-sms.html"},
             foot="MAC Apartments is operated by ACFLP."),
  "es": dict(lang="es", root="../", home="index.html", apts="departamentos.html", privacy="privacidad.html", terms="terminos.html",
             nav=("Inicio", "Privacidad", "Términos", "Departamentos"), other="English", other_href={"index.html": "../index.html", "departamentos.html": "../apartments.html", "privacidad.html": "../privacy.html", "terminos.html": "../terms.html", "consentimiento-sms.html": "../sms-consent.html"},
             foot="MAC Apartments es operado por ACFLP."),
}

def page(lng, file, title, desc, hero_h1, hero_p, body, small=True):
  t = T[lng]
  cur = lambda f: ' aria-current="page"' if f == file else ''
  r = t["root"]
  return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" sizes="32x32" href="{r}assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{r}assets/icon.png">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/site.css">
<link rel="alternate" hreflang="{'es' if lng == 'en' else 'en'}" href="{t['other_href'][file]}">
</head>
<body>
<header class="top">
  <div class="wrap">
    <nav class="nav">
      <a class="brand" href="{t['home']}"><img src="{r}assets/icon.png" alt="" width="40" height="40">MAC Apartments</a>
      <div class="links">
        <a href="{t['home']}"{cur(t['home'])}>{t['nav'][0]}</a>
        <a href="{t['apts']}"{cur(t['apts'])}>{t['nav'][3]}</a>
        <a href="{t['privacy']}"{cur(t['privacy'])}>{t['nav'][1]}</a>
        <a href="{t['terms']}"{cur(t['terms'])}>{t['nav'][2]}</a>
        <a class="lang" href="{t['other_href'][file]}" hreflang="{'es' if lng == 'en' else 'en'}">{t['other']}</a>
      </div>
    </nav>
    <div class="hero{' small' if small else ''}">
      <h1>{hero_h1}</h1>
      <p>{hero_p}</p>
    </div>
  </div>
</header>
<main class="wrap lift">
{body}
</main>
<footer>
  <div class="wrap">
    <span>© 2026 MAC Apartments · {ADDR} · <a href="tel:{TEL}">{PHONE}</a><br>{t['foot']}</span>
    <nav><a href="{t['privacy']}">{t['nav'][1]}</a><a href="{t['terms']}">{t['nav'][2]}</a></nav>
  </div>
</footer>
</body>
</html>
"""

def contact(lng):
  L = dict(en=("Office", "Phone", "Email", "Get directions"), es=("Oficina", "Teléfono", "Correo", "Cómo llegar"))[lng]
  return f"""<ul class="contact">
      <li><strong>{L[0]}</strong>{ADDR}</li>
      <li><strong>{L[1]}</strong><a href="tel:{TEL}">{PHONE}</a></li>
      <li><strong>{L[2]}</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
    </ul>
    <a class="btn" href="{MAP}" target="_blank" rel="noopener">{L[3]}</a>"""

FB = "https://www.facebook.com/MacApartmentsTexas/"

VETERANS = dict(
  photos=[("kitchen", "Kitchen with stainless steel appliances", "Cocina con electrodomésticos de acero inoxidable"),
    ("living-kitchen", "Open living area and kitchen", "Sala y cocina abiertas"),
    ("living-room", "Living room with ceiling fan", "Sala con ventilador de techo"),
    ("main-bedroom", "Main bedroom with private bathroom and walk-in closet", "Recámara principal con baño propio y vestidor"),
    ("walk-in-closet", "Walk-in closet", "Vestidor (walk-in closet)"),
    ("walk-in-shower", "Main bathroom with walk-in shower", "Baño principal con regadera walk-in"),
    ("washer-dryer", "Washer and dryer in the apartment", "Lavadora y secadora en el departamento"),
    ("bedroom-2", "Second bedroom", "Segunda recámara"),
    ("bathroom-2", "Second bathroom with tub", "Segundo baño con tina"),
    ("kitchen-sink", "Kitchen sink and backsplash", "Fregadero y azulejo de cocina"),
    ("hallway", "Hallway to the bedrooms", "Pasillo a las recámaras")],
  thumb=lambda k: f"{k}-sm.jpg", full=lambda k: f"{k}.jpg",
  id="veterans-2", where="3807 S Veterans Blvd, Edinburg, TX 78542", price="$1,100",
  en=dict(eyebrow="Veterans Blvd · Gated community", h="2 bedroom, 2 bathroom apartments",
    facts=[("2", "bedrooms"), ("2", "bathrooms"), ("≈1,000", "sq ft"), ("2", "carports")],
    p="Bright apartments with tall ceilings and tile floors throughout, in a gated community with video surveillance, close to shops, schools and markets in Edinburg, minutes from McAllen.",
    items=["Gated community", "Video surveillance", "Washer and dryer in the apartment", "Stainless steel appliances", "Central air conditioning", "Tile flooring", "Walk-in closet", "Walk-in shower", "Tall ceilings", "LED lighting", "2 carports", "On-site maintenance", "Pets welcome"],
    util="Electricity from Magic Valley Electric Cooperative and internet from Spectrum are available."),
  es=dict(eyebrow="Veterans Blvd · Comunidad cerrada", h="Departamentos de 2 recámaras y 2 baños",
    facts=[("2", "recámaras"), ("2", "baños"), ("≈1,000", "pies²"), ("2", "cocheras techadas")],
    p="Departamentos iluminados con techos altos y piso de loseta en todo el departamento, en una comunidad cerrada con videovigilancia, cerca de tiendas, escuelas y supermercados en Edinburg, a minutos de McAllen.",
    items=["Comunidad cerrada (con portón)", "Videovigilancia", "Lavadora y secadora en el departamento", "Electrodomésticos de acero inoxidable", "Aire acondicionado central", "Piso de loseta", "Vestidor (walk-in closet)", "Regadera walk-in", "Techos altos", "Iluminación LED", "2 cocheras techadas (carports)", "Mantenimiento en el lugar", "Se aceptan mascotas"],
    util="Hay servicio de electricidad con Magic Valley Electric Cooperative e internet con Spectrum."))

VETERANS3 = dict(
  photos=[("open-living", "Open living room and kitchen", "Sala y cocina abiertas"),
    ("aerial", "Aerial view of the gated community", "Vista aérea de la comunidad cerrada"),
    ("kitchen-island", "Kitchen island with seating", "Isla de cocina con asientos"),
    ("living-room", "Living room", "Sala"),
    ("living-tv", "Living room with tall ceilings", "Sala con techos altos"),
    ("stove", "Stainless steel range and microwave", "Estufa y microondas de acero inoxidable"),
    ("pantry", "Walk-in pantry", "Despensa amplia"),
    ("main-bedroom", "Main bedroom", "Recámara principal"),
    ("main-bedroom-tv", "Main bedroom with built-in shelves", "Recámara principal con repisas"),
    ("bedroom-2", "Second bedroom", "Segunda recámara"),
    ("bedroom-3", "Third bedroom", "Tercera recámara"),
    ("walk-in-closet", "Walk-in closet", "Vestidor (walk-in closet)"),
    ("walk-in-shower", "Bathroom with walk-in shower", "Baño con regadera walk-in"),
    ("bathroom-2", "Second bathroom with tub", "Segundo baño con tina"),
    ("vanity", "Bathroom vanity", "Lavabo del baño"),
    ("washer-dryer", "Washer and dryer in the apartment", "Lavadora y secadora en el departamento"),
    ("hallway", "Hallway to the bedrooms", "Pasillo a las recámaras")],
  thumb=lambda k: f"v3-{k}-sm.jpg", full=lambda k: f"v3-{k}.jpg",
  id="veterans-3", where="3807 S Veterans Blvd, Edinburg, TX 78542", price="$1,350",
  en=dict(eyebrow="Veterans Blvd · Gated community", h="3 bedroom, 2 bathroom apartments",
    facts=[("3", "bedrooms"), ("2", "bathrooms"), ("≈1,250", "sq ft"), ("2", "carports")],
    p="Room for the whole family: an open living area and kitchen with tall ceilings and tile floors, in a gated community with video surveillance, minutes from McAllen.",
    items=["Gated community", "Video surveillance", "Washer and dryer in the apartment", "Stainless steel appliances", "Central air conditioning", "Tile flooring", "Walk-in closet", "Walk-in shower", "Walk-in pantry", "Tall ceilings", "LED lighting", "2 carports", "On-site maintenance", "Pets welcome"],
    util="Electricity from Magic Valley Electric Cooperative and internet from Spectrum are available."),
  es=dict(eyebrow="Veterans Blvd · Comunidad cerrada", h="Departamentos de 3 recámaras y 2 baños",
    facts=[("3", "recámaras"), ("2", "baños"), ("≈1,250", "pies²"), ("2", "cocheras techadas")],
    p="Espacio para toda la familia: sala y cocina abiertas con techos altos y piso de loseta, en una comunidad cerrada con videovigilancia, a minutos de McAllen.",
    items=["Comunidad cerrada (con portón)", "Videovigilancia", "Lavadora y secadora en el departamento", "Electrodomésticos de acero inoxidable", "Aire acondicionado central", "Piso de loseta", "Vestidor (walk-in closet)", "Regadera walk-in", "Despensa amplia", "Techos altos", "Iluminación LED", "2 cocheras techadas (carports)", "Mantenimiento en el lugar", "Se aceptan mascotas"],
    util="Hay servicio de electricidad con Magic Valley Electric Cooperative e internet con Spectrum."))

LETICIA = dict(
  photos=[("living-room", "Living room", "Sala"),
    ("living-dining", "Living and dining area", "Sala y comedor"),
    ("dining-kitchen", "Dining area and kitchen", "Comedor y cocina"),
    ("kitchen", "Kitchen with stainless steel appliances", "Cocina con electrodomésticos de acero inoxidable"),
    ("main-bedroom", "Main bedroom", "Recámara principal"),
    ("bedroom-furnished", "Second bedroom", "Segunda recámara"),
    ("bedroom-2", "Bedroom with ceiling fan", "Recámara con ventilador de techo"),
    ("bedroom-3", "Bedroom with tray ceiling", "Recámara con techo escalonado"),
    ("bathroom", "Bathroom with tub", "Baño con tina"),
    ("bathroom-2", "Second bathroom", "Segundo baño"),
    ("complex", "The community and parking", "La comunidad y el estacionamiento"),
    ("street", "Quiet street inside the community", "Calle tranquila dentro de la comunidad"),
    ("bbq", "Outdoor brick BBQ grill", "Asador de ladrillo al aire libre")],
  thumb=lambda k: f"leticia-{k}.jpg", full=lambda k: f"leticia-{k}.jpg",
  id="leticia", where="1103 Leticia St, Edinburg, TX 78542", price=None,
  en=dict(eyebrow="Leticia St", h="2 bedroom, 2 bathroom apartments with water included",
    facts=[("2", "bedrooms"), ("2", "bathrooms"), ("798", "sq ft"), ("2", "parking spaces")],
    p="A quiet single-story community in a prime Edinburg location, with water included in the rent and an outdoor BBQ grill for residents.",
    items=["Water included", "Stainless steel appliances", "Walk-in closet", "2 on-site parking spaces", "Video surveillance", "Outdoor BBQ grill", "On-site maintenance", "Pets welcome", "Prime location"],
    util="Water is included. Electricity from Magic Valley Electric Cooperative and internet from Spectrum are available."),
  es=dict(eyebrow="Leticia St", h="Departamentos de 2 recámaras y 2 baños con agua incluida",
    facts=[("2", "recámaras"), ("2", "baños"), ("798", "pies²"), ("2", "estacionamientos")],
    p="Una comunidad tranquila de un solo piso, en una excelente ubicación de Edinburg, con el agua incluida en la renta y asador al aire libre para los residentes.",
    items=["Agua incluida", "Electrodomésticos de acero inoxidable", "Vestidor (walk-in closet)", "2 lugares de estacionamiento", "Videovigilancia", "Asador al aire libre", "Mantenimiento en el lugar", "Se aceptan mascotas", "Excelente ubicación"],
    util="El agua está incluida. Hay servicio de electricidad con Magic Valley Electric Cooperative e internet con Spectrum."))

def listing(lng, d):
  r = "" if lng == "en" else "../"
  en = lng == "en"
  L = d[lng]
  W = dict(en=dict(per="per month", ask="Call for current price", call="Call", gallery="Photos", tap="Tap a photo to see it larger.", feat="What's included", util="Utilities", map="Get directions"),
           es=dict(per="al mes", ask="Llama para conocer el precio", call="Llamar", gallery="Fotos", tap="Toca una foto para verla más grande.", feat="Qué incluye", util="Servicios", map="Cómo llegar"))[lng]
  price = f'<p class="price"><strong>{d["price"]}</strong> {W["per"]}</p>' if d["price"] else f'<p class="price"><strong class="ask">{W["ask"]}</strong></p>'
  facts = "".join(f'<div class="fact"><strong>{n}</strong><span>{w}</span></div>' for n, w in L["facts"])
  lis = "".join(f"<li>{i}</li>" for i in L["items"])
  cover = d["photos"][0]
  pics = "".join(f'<a href="{r}assets/photos/{d["full"](k)}" target="_blank" rel="noopener"><img src="{r}assets/photos/{d["thumb"](k)}" alt="{e if en else es}" loading="lazy"></a>' for k, e, es in d["photos"][1:])
  maps = "https://www.google.com/maps/search/?api=1&query=" + d["where"].replace(",", "").replace(" ", "+")
  return f"""  <section class="card listing" id="{d['id']}">
    <img class="cover" src="{r}assets/photos/{d['full'](cover[0])}" alt="{cover[1] if en else cover[2]}">
    <div>
      <p class="eyebrow">{L['eyebrow']}</p>
      <h2>{L['h']}</h2>
      <p class="muted">{d['where']} · <a href="{maps}" target="_blank" rel="noopener">{W['map']}</a></p>
      {price}
      <div class="facts">{facts}</div>
      <p>{L['p']}</p>
      <a class="btn" href="tel:{TEL}">{W['call']} · {PHONE}</a>
    </div>
  </section>
  <p class="muted gallery-note">{W['tap']}</p>
  <div class="gallery">{pics}</div>
  <div class="grid">
    <section class="card">
      <h2>{W['feat']}</h2>
      <ul class="features">{lis}</ul>
    </section>
    <section class="card">
      <h2>{W['util']}</h2>
      <p>{L['util']}</p>
    </section>
  </div>"""

def apts(lng):
  r = "" if lng == "en" else "../"
  L = dict(en=dict(jump=("Veterans · 2 bed", "Veterans · 3 bed", "Leticia St"), plans="Floor plans", p2=("2 bedrooms · 2 bathrooms", "Floor plan of a 2-bedroom apartment"), p3=("3 bedrooms · 2 bathrooms · ≈1,250 sq ft", "Floor plan of the 3-bedroom apartment"),
             cta="Schedule a visit", cta_p="Call the office to see an apartment or ask about move-in dates.", call="Call", fb="Follow us on Facebook"),
           es=dict(jump=("Veterans · 2 rec.", "Veterans · 3 rec.", "Leticia St"), plans="Planos", p2=("2 recámaras · 2 baños", "Plano de un departamento de 2 recámaras"), p3=("3 recámaras · 2 baños · ≈1,250 pies²", "Plano del departamento de 3 recámaras"),
             cta="Agenda una visita", cta_p="Llama a la oficina para ver un departamento o preguntar por fechas de mudanza.", call="Llamar", fb="Síguenos en Facebook"))[lng]
  return f"""  <nav class="jump card"><a href="#veterans-2">{L['jump'][0]}</a><a href="#veterans-3">{L['jump'][1]}</a><a href="#leticia">{L['jump'][2]}</a></nav>
{listing(lng, VETERANS)}
{listing(lng, VETERANS3)}
{listing(lng, LETICIA)}
  <h2 class="section-title">{L['plans']}</h2>
  <div class="grid">
    <section class="card plan"><div class="plan-img"><img src="{r}assets/plan-2-bed.png" alt="{L['p2'][1]}" loading="lazy"></div><p class="muted">{L['p2'][0]}</p></section>
    <section class="card plan"><div class="plan-img"><img src="{r}assets/plan-3-bed.png" alt="{L['p3'][1]}" loading="lazy"></div><p class="muted">{L['p3'][0]}</p></section>
  </div>
  <section class="card">
    <h2>{L['cta']}</h2>
    <p>{L['cta_p']}</p>
    <a class="btn" href="tel:{TEL}">{L['call']} · {PHONE}</a>
    <p><a href="{FB}" target="_blank" rel="noopener">{L['fb']}</a></p>
  </section>"""

def teaser(lng):
  t = T[lng]; r = t["root"]
  L = dict(en=("Available now", "2 and 3 bedroom apartments in two Edinburg locations: a gated community on Veterans Blvd (2 bed $1,100, 3 bed $1,350 a month, washer and dryer included) and Leticia St (water included). Walk-in closets, stainless steel appliances and pets welcome.", "See photos and details", "Kitchen with stainless steel appliances"),
           es=("Disponible ahora", "Departamentos de 2 y 3 recámaras en dos ubicaciones de Edinburg: una comunidad cerrada en Veterans Blvd (2 rec. $1,100, 3 rec. $1,350 al mes, lavadora y secadora incluidas) y Leticia St (agua incluida). Vestidor, electrodomésticos de acero inoxidable y se aceptan mascotas.", "Ver fotos y detalles", "Cocina con electrodomésticos de acero inoxidable"))[lng]
  return f"""  <section class="card teaser">
    <img src="{r}assets/photos/kitchen.jpg" alt="{L[3]}" width="1600" height="1200">
    <div>
      <p class="eyebrow">{L[0]}</p>
      <p>{L[1]}</p>
      <a class="btn" href="{t['apts']}">{L[2]}</a>
    </div>
  </section>"""

# ---------- English ----------
home_en = f"""  <div class="grid">
    <section class="card">
      <p class="eyebrow">Welcome</p>
      <h2>Apartment homes in Edinburg, Texas</h2>
      <p>MAC Apartments is a local property management company in Edinburg, Texas. We rent and care for apartment homes and houses, and our team has more than 10 years of experience looking after residents with fast maintenance and a friendly on-site office.</p>
    </section>
    <section class="card">
      <p class="eyebrow">Contact us</p>
      {contact('en')}
    </section>
  </div>
{teaser('en')}
  <section class="card">
    <p class="eyebrow">For residents</p>
    <h2>Text message updates</h2>
    <p>Residents who sign our <a href="sms-consent.html">SMS consent form</a> at the office can receive text messages from MAC Apartments about their home: maintenance and work-order updates, scheduled service interruptions (water, power, pest control), payment confirmations and building notices.</p>
    <p>Message frequency varies (usually up to 4 per month). Message and data rates may apply. Reply <strong>STOP</strong> to opt out or <strong>HELP</strong> for help. Agreeing to texts is never a condition of renting. See our <a href="terms.html">SMS terms</a> and <a href="privacy.html">privacy policy</a>.</p>
  </section>"""

privacy_en = f"""  <article class="card legal">
    <p class="muted">Last updated: {UPDATED_EN}</p>
    <p>This policy explains how MAC Apartments, operated by ACFLP (“we”, “us”), collects, uses and protects information about residents, applicants and visitors to this website.</p>

    <h2>Information we collect</h2>
    <ul>
      <li><strong>Contact details:</strong> name, mobile phone number, email and mailing address.</li>
      <li><strong>Rental information:</strong> lease details, household members, vehicles, pets, maintenance requests and photos you send us.</li>
      <li><strong>Payment records:</strong> charges, payments and receipts on your account.</li>
      <li><strong>Application information</strong> you choose to give us, such as identification needed to process a rental application.</li>
    </ul>
    <p>This website itself does not use forms, tracking cookies or advertising trackers.</p>

    <h2>How we use information</h2>
    <ul>
      <li>To manage your lease, account, payments and maintenance requests.</li>
      <li>To contact you about your home, including by phone, email and text message (see below).</li>
      <li>To meet legal, accounting and safety obligations.</li>
    </ul>

    <h2>Text messages (SMS)</h2>
    <p>If you agree to receive text messages, we use your mobile number only to send you messages about your tenancy, as described in our <a href="terms.html">SMS terms</a>.</p>
    <div class="note">
      <p><strong>We do not sell or share your SMS opt-in data or personal information with third parties for marketing purposes.</strong> No mobile information will be shared with third parties or affiliates for marketing or promotional purposes. Text messaging opt-in data and consent are not shared with any third party, except with the messaging service providers that deliver our messages.</p>
    </div>
    <p>You can stop text messages at any time by replying <strong>STOP</strong>.</p>

    <h2>How we share information</h2>
    <p>We do not sell or rent personal information. We share it only:</p>
    <ul>
      <li>With service providers who help us run our business (for example, text-message delivery, email and secure data hosting), only for that purpose and under confidentiality obligations.</li>
      <li>When required by law, court order or to protect the safety of residents, staff or property.</li>
      <li>With a collection agency or attorney if an account is past due after a lease ends, as permitted by law.</li>
    </ul>

    <h2>How we protect information</h2>
    <p>Access to resident records is limited to staff who need it. Sensitive identification numbers are stored encrypted, and our systems use secure (HTTPS) connections.</p>

    <h2>How long we keep information</h2>
    <p>We keep records for as long as needed to manage your lease and as required for accounting, tax and legal purposes.</p>

    <h2>Your choices</h2>
    <p>You may ask to see or correct the information we hold about you, or to stop receiving text messages, by contacting the office.</p>

    <h2>Children</h2>
    <p>This website and our text messages are not directed to children under 13.</p>

    <h2>Changes</h2>
    <p>We may update this policy. The date at the top shows the latest version.</p>

    <h2>Contact</h2>
    {contact('en')}
  </article>"""

terms_en = f"""  <article class="card legal">
    <p class="muted">Last updated: {UPDATED_EN}</p>
    <p>These Terms &amp; Conditions apply to the MAC Apartments website and to the MAC Apartments text message program. MAC Apartments is operated by ACFLP, {ADDR}.</p>

    <h2>Use of this website</h2>
    <p>This website gives general information about MAC Apartments and our apartments. Prices, availability and features can change; please confirm with the office before you rely on them. Your lease is the agreement that governs your tenancy.</p>

    <h2 id="sms">SMS Terms</h2>

    <h3>Program</h3>
    <p><strong>MAC Apartments resident notices</strong>, sent by MAC Apartments (operated by ACFLP) to current residents.</p>

    <h3>What we send</h3>
    <p>Informational messages about your home: maintenance and work-order updates, scheduled service interruptions (water, power, pest control), payment confirmations, office hours and building notices. We do not send marketing messages.</p>

    <h3>How you sign up</h3>
    <p>You sign up in writing at the leasing office by completing our <a href="sms-consent.html">SMS Text Message Consent Form</a>: you give your mobile number, check the consent box and sign and date the form. The consent box reads:</p>
    <div class="note"><p>“I consent to receive text messages from MAC Apartments as described above. I understand that consent is not required to rent an apartment or to receive any service.”</p></div>
    <p>Agreeing to receive text messages is <strong>not a condition of renting</strong> or of any service.</p>

    <h3>Message frequency</h3>
    <p>Message frequency varies, usually up to 4 messages per month.</p>

    <h3>Cost</h3>
    <p>Message and data rates may apply, according to your mobile plan. MAC Apartments does not charge for text messages.</p>

    <h3>Stop messages</h3>
    <p>Reply <strong>STOP</strong> (or ALTO) to any message to stop receiving texts. We will send one message confirming you have been unsubscribed, and you will receive no further texts unless you reply <strong>START</strong> to sign up again.</p>

    <h3>Help</h3>
    <p>Reply <strong>HELP</strong> (or AYUDA) for help, call <a href="tel:{TEL}">{PHONE}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <h3>Carriers</h3>
    <p>Mobile carriers are not liable for delayed or undelivered messages.</p>

    <h3>Privacy</h3>
    <p>See our <a href="privacy.html">privacy policy</a>. No mobile information will be shared with third parties or affiliates for marketing or promotional purposes.</p>
  </article>"""

# ---------- Español ----------
home_es = f"""  <div class="grid">
    <section class="card">
      <p class="eyebrow">Bienvenidos</p>
      <h2>Departamentos en Edinburg, Texas</h2>
      <p>MAC Apartments es una empresa local de administración de propiedades en Edinburg, Texas. Rentamos y cuidamos departamentos y casas, y nuestro equipo tiene más de 10 años de experiencia atendiendo a residentes con mantenimiento rápido y una oficina amable en el lugar.</p>
    </section>
    <section class="card">
      <p class="eyebrow">Contáctanos</p>
      {contact('es')}
    </section>
  </div>
{teaser('es')}
  <section class="card">
    <p class="eyebrow">Para residentes</p>
    <h2>Avisos por mensaje de texto</h2>
    <p>Los residentes que firman nuestro <a href="consentimiento-sms.html">formulario de consentimiento SMS</a> en la oficina pueden recibir mensajes de texto de MAC Apartments sobre su hogar: avisos de mantenimiento y órdenes de trabajo, cortes programados de servicios (agua, luz, fumigación), confirmaciones de pago y avisos del edificio.</p>
    <p>La frecuencia de los mensajes varía (normalmente hasta 4 al mes). Pueden aplicarse tarifas de mensajes y datos. Responde <strong>STOP</strong> para no recibir más o <strong>HELP</strong> para ayuda. Aceptar mensajes nunca es condición para rentar. Consulta nuestros <a href="terminos.html">términos SMS</a> y nuestra <a href="privacidad.html">política de privacidad</a>.</p>
  </section>"""

privacy_es = f"""  <article class="card legal">
    <p class="muted">Última actualización: {UPDATED_ES}</p>
    <p>Esta política explica cómo MAC Apartments, operado por ACFLP (“nosotros”), recopila, usa y protege la información de residentes, solicitantes y visitantes de este sitio web.</p>

    <h2>Información que recopilamos</h2>
    <ul>
      <li><strong>Datos de contacto:</strong> nombre, número de celular, correo y dirección postal.</li>
      <li><strong>Información de la renta:</strong> datos del contrato, miembros del hogar, vehículos, mascotas, solicitudes de mantenimiento y fotos que nos envías.</li>
      <li><strong>Registros de pago:</strong> cargos, pagos y recibos de tu cuenta.</li>
      <li><strong>Información de solicitud</strong> que decidas darnos, como la identificación necesaria para procesar una solicitud de renta.</li>
    </ul>
    <p>Este sitio web no usa formularios, cookies de rastreo ni rastreadores publicitarios.</p>

    <h2>Cómo usamos la información</h2>
    <ul>
      <li>Para administrar tu contrato, cuenta, pagos y solicitudes de mantenimiento.</li>
      <li>Para comunicarnos contigo sobre tu hogar, por teléfono, correo y mensaje de texto (ver abajo).</li>
      <li>Para cumplir obligaciones legales, contables y de seguridad.</li>
    </ul>

    <h2>Mensajes de texto (SMS)</h2>
    <p>Si aceptas recibir mensajes de texto, usamos tu número de celular solo para enviarte mensajes sobre tu renta, como se describe en nuestros <a href="terminos.html">términos SMS</a>.</p>
    <div class="note">
      <p><strong>No vendemos ni compartimos tus datos de suscripción a SMS ni tu información personal con terceros con fines de mercadotecnia.</strong> No compartiremos información móvil con terceros ni afiliados con fines de mercadotecnia o promoción. Los datos y el consentimiento de suscripción a mensajes de texto no se comparten con ningún tercero, excepto con los proveedores que entregan nuestros mensajes.</p>
    </div>
    <p>Puedes dejar de recibir mensajes en cualquier momento respondiendo <strong>STOP</strong>.</p>

    <h2>Con quién compartimos información</h2>
    <p>No vendemos ni rentamos información personal. Solo la compartimos:</p>
    <ul>
      <li>Con proveedores que nos ayudan a operar (por ejemplo, envío de mensajes de texto, correo y almacenamiento seguro de datos), solo para ese fin y con obligación de confidencialidad.</li>
      <li>Cuando lo exija la ley, una orden judicial o para proteger la seguridad de residentes, personal o la propiedad.</li>
      <li>Con una agencia de cobranza o un abogado si una cuenta queda con saldo vencido después de terminar el contrato, según lo permita la ley.</li>
    </ul>

    <h2>Cómo protegemos la información</h2>
    <p>Solo el personal que lo necesita puede ver los registros de residentes. Los números de identificación sensibles se guardan cifrados y nuestros sistemas usan conexiones seguras (HTTPS).</p>

    <h2>Cuánto tiempo la guardamos</h2>
    <p>Guardamos los registros mientras sea necesario para administrar tu contrato y según lo exijan fines contables, fiscales y legales.</p>

    <h2>Tus opciones</h2>
    <p>Puedes pedir ver o corregir la información que tenemos sobre ti, o dejar de recibir mensajes de texto, comunicándote con la oficina.</p>

    <h2>Menores</h2>
    <p>Este sitio web y nuestros mensajes no están dirigidos a menores de 13 años.</p>

    <h2>Cambios</h2>
    <p>Podemos actualizar esta política. La fecha de arriba indica la versión más reciente.</p>

    <h2>Contacto</h2>
    {contact('es')}
  </article>"""

terms_es = f"""  <article class="card legal">
    <p class="muted">Última actualización: {UPDATED_ES}</p>
    <p>Estos Términos y Condiciones aplican al sitio web de MAC Apartments y al programa de mensajes de texto de MAC Apartments. MAC Apartments es operado por ACFLP, {ADDR}.</p>

    <h2>Uso de este sitio web</h2>
    <p>Este sitio web da información general sobre MAC Apartments y nuestros departamentos. Los precios, la disponibilidad y las características pueden cambiar; confírmalos con la oficina antes de tomarlos en cuenta. Tu contrato de arrendamiento es el acuerdo que rige tu renta.</p>

    <h2 id="sms">Términos SMS</h2>

    <h3>Programa</h3>
    <p><strong>Avisos a residentes de MAC Apartments</strong>, enviados por MAC Apartments (operado por ACFLP) a sus residentes actuales.</p>

    <h3>Qué enviamos</h3>
    <p>Mensajes informativos sobre tu hogar: avisos de mantenimiento y órdenes de trabajo, cortes programados de servicios (agua, luz, fumigación), confirmaciones de pago, horario de oficina y avisos del edificio. No enviamos mensajes de mercadotecnia.</p>

    <h3>Cómo te suscribes</h3>
    <p>Te suscribes por escrito en la oficina llenando nuestro <a href="consentimiento-sms.html">formulario de consentimiento para mensajes de texto</a>: das tu número de celular, marcas la casilla de consentimiento y firmas y fechas el formulario. La casilla dice:</p>
    <div class="note"><p>“Doy mi consentimiento para recibir mensajes de texto de MAC Apartments como se describe arriba. Entiendo que el consentimiento no es requisito para rentar un departamento ni para recibir ningún servicio.”</p></div>
    <p>Aceptar mensajes de texto <strong>no es condición para rentar</strong> ni para recibir ningún servicio.</p>

    <h3>Frecuencia</h3>
    <p>La frecuencia de los mensajes varía, normalmente hasta 4 mensajes al mes.</p>

    <h3>Costo</h3>
    <p>Pueden aplicarse tarifas de mensajes y datos según tu plan. MAC Apartments no cobra por los mensajes de texto.</p>

    <h3>Dejar de recibir mensajes</h3>
    <p>Responde <strong>STOP</strong> (o ALTO) a cualquier mensaje para dejar de recibirlos. Te enviaremos un mensaje confirmando la baja y no recibirás más, a menos que respondas <strong>START</strong> para suscribirte otra vez.</p>

    <h3>Ayuda</h3>
    <p>Responde <strong>HELP</strong> (o AYUDA), llama al <a href="tel:{TEL}">{PHONE}</a> o escribe a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <h3>Compañías telefónicas</h3>
    <p>Las compañías telefónicas no son responsables por mensajes retrasados o no entregados.</p>

    <h3>Privacidad</h3>
    <p>Consulta nuestra <a href="privacidad.html">política de privacidad</a>. No compartiremos información móvil con terceros ni afiliados con fines de mercadotecnia o promoción.</p>
  </article>"""

def consent(lng):
  r = "" if lng == "en" else "../"
  if lng == "en":
    L = dict(title="SMS Text Message Consent Form", intro="Residents fill in and sign this form at the leasing office. Print it, or ask the office for a copy. Signed forms are kept on file as records of consent.",
      print="Print this form", dl=("Download PDF", "View as image"), file="sms-consent-form", name="Resident name*", prop="Property*", unit="Unit*", mobile="Mobile phone number*",
      sections=[("Text message service", "By providing your mobile phone number, you agree to receive text messages from MAC Apartments (ACFLP) about your tenancy: maintenance and work-order updates, scheduled service interruptions (water, power, pest control), payment confirmations and building notices."),
                ("Message frequency", "Message frequency varies, usually up to 4 messages per month."),
                ("Standard rates", "Message and data rates may apply depending on your mobile phone plan."),
                ("Help &amp; Stop", "Reply HELP for help or STOP to cancel at any time. You can also call the office at " + PHONE + "."),
                ("Terms &amp; Privacy", "Visit macapartmentstexas.com/terms.html for the SMS Terms and macapartmentstexas.com/privacy.html for the Privacy Policy.")],
      agree="I consent to receive text messages from MAC Apartments as described above. I understand that consent is not required to rent an apartment or to receive any service.",
      sign="Resident signature*", date="Date*", office="Office use only", recv="Received by", entered="Entered in system on")
  else:
    L = dict(title="Formulario de consentimiento para mensajes de texto (SMS)", intro="Los residentes llenan y firman este formulario en la oficina. Imprímelo o pide una copia en la oficina. Los formularios firmados se guardan como comprobante del consentimiento.",
      print="Imprimir formulario", dl=("Descargar PDF", "Ver como imagen"), file="formulario-consentimiento-sms", name="Nombre del residente*", prop="Propiedad*", unit="Departamento*", mobile="Número de celular*",
      sections=[("Servicio de mensajes de texto", "Al dar tu número de celular, aceptas recibir mensajes de texto de MAC Apartments (ACFLP) sobre tu renta: avisos de mantenimiento y órdenes de trabajo, cortes programados de servicios (agua, luz, fumigación), confirmaciones de pago y avisos del edificio."),
                ("Frecuencia", "La frecuencia de los mensajes varía, normalmente hasta 4 mensajes al mes."),
                ("Tarifas", "Pueden aplicarse tarifas de mensajes y datos según tu plan de celular."),
                ("Ayuda y baja", "Responde HELP para ayuda o STOP para cancelar en cualquier momento. También puedes llamar a la oficina al " + PHONE + "."),
                ("Términos y privacidad", "Consulta macapartmentstexas.com/es/terminos.html para los Términos SMS y macapartmentstexas.com/es/privacidad.html para la Política de privacidad.")],
      agree="Doy mi consentimiento para recibir mensajes de texto de MAC Apartments como se describe arriba. Entiendo que el consentimiento no es requisito para rentar un departamento ni para recibir ningún servicio.",
      sign="Firma del residente*", date="Fecha*", office="Solo para la oficina", recv="Recibido por", entered="Registrado en el sistema el")
  secs = "".join(f"<p><strong>{h}:</strong> {t}</p>" for h, t in L["sections"])
  return f"""  <article class="card consent">
    <div class="consent-head"><img src="{r}assets/icon.png" alt="" width="56" height="56"><div><strong>MAC Apartments</strong><br><span class="muted">{ADDR} · {PHONE}</span></div></div>
    <h2>{L['title']}</h2>
    <p class="muted no-print">{L['intro']}</p>
    <p class="no-print actions"><button class="btn" type="button" onclick="window.print()">{L['print']}</button> <a href="{r}assets/{L['file']}.pdf">{L['dl'][0]}</a> · <a href="{r}assets/{L['file']}.png">{L['dl'][1]}</a></p>
    <div class="fields">
      <div class="line"><span>{L['name']}</span></div>
      <p class="choice">{L['prop']}: &nbsp; ☐ 3807 S Veterans Blvd &nbsp;&nbsp; ☐ 1103 Leticia St</p>
      <div class="line half"><span>{L['unit']}</span></div>
      <div class="line half"><span>{L['mobile']}</span></div>
    </div>
    <div class="terms">{secs}</div>
    <p class="agree"><span class="box">☐</span> {L['agree']}</p>
    <div class="fields">
      <div class="line half"><span>{L['sign']}</span></div>
      <div class="line half"><span>{L['date']}</span></div>
    </div>
    <div class="office"><strong>{L['office']}</strong>
      <div class="fields"><div class="line half"><span>{L['recv']}</span></div><div class="line half"><span>{L['entered']}</span></div></div>
    </div>
  </article>"""

files = {
  "index.html": page("en", "index.html", "MAC Apartments · Edinburg, Texas", "Apartment homes in Edinburg, Texas. Office, phone and resident information.", "Your home in Edinburg, Texas", "Apartment homes and houses with a local office that knows you by name.", home_en, small=False),
  "apartments.html": page("en", "apartments.html", "Apartments · MAC Apartments", "2 and 3 bedroom apartments for rent in Edinburg, Texas: gated community, washer and dryer included, from $1,100 a month. Photos, features and contact.", "Our apartments", "Apartments for rent in Edinburg, Texas, near McAllen.", apts("en")),
  "privacy.html": page("en", "privacy.html", "Privacy Policy · MAC Apartments", "How MAC Apartments collects, uses and protects resident information, including text messages.", "Privacy Policy", "How we collect, use and protect your information.", privacy_en),
  "terms.html": page("en", "terms.html", "Terms & Conditions · MAC Apartments", "MAC Apartments Terms & Conditions, including the SMS Terms for resident text messages: what we send, frequency, message and data rates, STOP and HELP.", "Terms &amp; Conditions", "Website terms and SMS Terms for MAC Apartments residents.", terms_en),
  "sms-consent.html": page("en", "sms-consent.html", "SMS consent form · MAC Apartments", "The form MAC Apartments residents sign to agree to receive text messages.", "SMS consent form", "How residents agree to receive text messages.", consent("en")),
  "es/index.html": page("es", "index.html", "MAC Apartments · Edinburg, Texas", "Departamentos en Edinburg, Texas. Oficina, teléfono e información para residentes.", "Tu hogar en Edinburg, Texas", "Departamentos y casas con una oficina local que te conoce por tu nombre.", home_es, small=False),
  "es/departamentos.html": page("es", "departamentos.html", "Departamentos · MAC Apartments", "Departamentos de 2 y 3 recámaras en renta en Edinburg, Texas: comunidad cerrada, lavadora y secadora incluidas, desde $1,100 al mes. Fotos, características y contacto.", "Nuestros departamentos", "Departamentos en renta en Edinburg, Texas, cerca de McAllen.", apts("es")),
  "es/privacidad.html": page("es", "privacidad.html", "Política de privacidad · MAC Apartments", "Cómo MAC Apartments recopila, usa y protege la información de residentes, incluidos los mensajes de texto.", "Política de privacidad", "Cómo recopilamos, usamos y protegemos tu información.", privacy_es),
  "es/terminos.html": page("es", "terminos.html", "Términos y Condiciones · MAC Apartments", "Términos y Condiciones de MAC Apartments, incluidos los Términos SMS: qué enviamos, frecuencia, tarifas, STOP y HELP.", "Términos y Condiciones", "Términos del sitio web y Términos SMS para residentes de MAC Apartments.", terms_es),
  "es/consentimiento-sms.html": page("es", "consentimiento-sms.html", "Consentimiento SMS · MAC Apartments", "El formulario que firman los residentes de MAC Apartments para aceptar mensajes de texto.", "Consentimiento SMS", "Cómo aceptan los residentes recibir mensajes de texto.", consent("es")),
}
for name, html in files.items():
  (OUT / name).write_text(html, encoding="utf-8")
(OUT / ".nojekyll").write_text("")
redirect = lambda to: f'<!doctype html><meta charset="utf-8"><title>Terms &amp; Conditions · MAC Apartments</title><link rel="canonical" href="{to}"><meta http-equiv="refresh" content="0; url={to}"><a href="{to}">Terms &amp; Conditions</a>'
(OUT / "sms-terms.html").write_text(redirect("terms.html#sms"), encoding="utf-8")
(OUT / "es" / "terminos-sms.html").write_text(redirect("terminos.html#sms"), encoding="utf-8")
(OUT / "404.html").write_text(files["index.html"].replace('href="index.html" aria-current="page"', 'href="index.html"'), encoding="utf-8")
print("wrote", len(files) + 2, "files")
