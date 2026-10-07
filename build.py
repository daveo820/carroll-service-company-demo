# Static page builder for the Carroll Service Company concept. Run: python3 build.py
import json, os
BASE = 'https://daveo820.github.io/carroll-service-company-demo/'  # temporary GitHub Pages link; swap for Vercel later
TEL, TEL_H = '+19197728546', '(919) 772&#8209;8546'
EXA = 'https://exa.ai/library/place/vfmcyldjtvy'
BZ = 'https://www.buildzoom.com/contractor/carroll-service-company-inc'
ORG = {"@context":"https://schema.org","@type":"HVACBusiness","name":"Carroll Service Company, Inc.",
 "url":"https://carrollservicecompany.com","telephone":"+1-919-772-8546","foundingDate":"1973",
 "founder":{"@type":"Person","name":"Lee Carroll"},
 "address":{"@type":"PostalAddress","streetAddress":"125 W. Main Street","addressLocality":"Garner","addressRegion":"NC","postalCode":"27529","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":35.707082,"longitude":-78.606249},
 "openingHours":"Mo-Fr 08:00-17:00","areaServed":["Wake County, NC","Clayton, NC"],
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"25"},
 "image":BASE+"img/carroll-family-van.webp"}
FONTS = 'https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,600;0,700;0,800;1,400&family=Young+Serif&display=swap'
_n = [0]
def SEAL(top, center, sub='', cls=''):
    _n[0] += 1; i = _n[0]
    return (f'<span class="seal {cls}" aria-hidden="true"><svg viewBox="0 0 120 120"><defs><path id="arc{i}" d="M60,60 m-44,0 a44,44 0 1,1 88,0 a44,44 0 1,1 -88,0"/></defs>'
            f'<circle cx="60" cy="60" r="57" class="s-ring"/><circle cx="60" cy="60" r="33" class="s-core"/>'
            f'<text class="s-arc"><textPath href="#arc{i}" startOffset="0" textLength="272" lengthAdjust="spacing">{top}</textPath></text>'
            f'<text x="60" y="{64 if not sub else 60}" class="s-c" text-anchor="middle">{center}</text>' + (f'<text x="60" y="76" class="s-sub" text-anchor="middle">{sub}</text>' if sub else '') + '</svg></span>')
def K(t, cls=''): return f'<p class="kicker {cls}"><span class="k-dot" aria-hidden="true"></span>{t}</p>'
STARS = '<span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'

def img(src, alt, sizes='100vw', eager=False, w=505, h=332, cls=''):
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    return f'<img src="img/{src}" alt="{alt}" width="{w}" height="{h}"{load}' + (f' class="{cls}"' if cls else '') + '>'

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Carroll Service Company (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#143a6b">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{fonts}"><link rel="stylesheet" href="{fonts}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{fonts}"></noscript>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='15' fill='%23143a6b'/%3E%3Ctext x='16' y='22' font-family='Georgia' font-size='17' fill='%23fff' text-anchor='middle'%3EC%3C/text%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not the official Carroll Service Company site. Photos are Carroll&rsquo;s own from carrollservicecompany.com; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><span class="mk-c" aria-hidden="true">C</span><span><b>Carroll Service Co.</b><small>Heating &amp; Air &middot; Garner since 1973</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--red btn--call" href="tel:{tel}"><span class="cl-full">{telh}</span><span class="cl-short">Call</span></a></div></header><main id="main">'''

FOOT = f'''</main><footer class="site-foot"><div class="wrap">
<div class="foot-top">
 <div class="ft-seal">{SEAL('FAMILY OWNED &#183; GARNER NC &#183; SINCE 1973 &#183; ','53','YEARS','seal--lg')}</div>
 <div><p class="foot-h">One office.<br>One number.</p><a class="foot-num" href="tel:{TEL}">{TEL_H}</a></div>
 <address><b>Carroll Service Company, Inc.</b><br>125 W. Main Street, Garner, NC 27529<br>Monday to Friday, 8am to 5pm<br>HVAC NC license #10119</address>
</div>
<div class="foot-grid">
 <div><h2>Service</h2><ul><li><a href="services.html#repair">Service and repair</a></li><li><a href="services.html#agreement">Maintenance agreements</a></li><li><a href="services.html#replace">Replacements</a></li><li><a href="services.html#equipment">Equipment</a></li></ul></div>
 <div><h2>Carroll</h2><ul><li><a href="company.html">The family</a></li><li><a href="reviews.html">Reviews</a></li><li><a href="contact.html">Free estimate</a></li></ul></div>
 <div><h2>Where</h2><p>All of Wake County and the Clayton area. Prequalified Duke Energy contractor. Financing with approved credit through Wells Fargo.</p></div>
</div>
<div class="foot-row"><span>Carroll Service Company, Inc. &middot; Garner, North Carolina</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','Services'),('reviews.html','Reviews'),('company.html','The family'),('contact.html','Free estimate')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 62, (fn, len(t), t)
    assert 130 <= len(d) <= 165, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or ORG),fonts=FONTS,tel=TEL,telh=TEL_H) + body + FOOT)

# Google reviews via the Exa place page (Google review data snapshot, Sep 2026). "..." = truncated at the source.
REV = [
 ('2026-02-20','Feb 2026','Family business. They have been taking care of us for a few years now. Very happy with service, knowledge and cleanliness. 5/5.'),
 ('2025-07-14','Jul 2025','These guys are awesome to work with! They&rsquo;ve replaced one of our AC units and serviced them both. Each time, the Carroll team has been easy to work with. Customer service this good is hard to find.'),
 ('2025-06-25','Jun 2025','The team at Carroll is exceptional. Dennis is always so kind on the phone and the techs we have worked with are always friendly, helpful, and fair with pricing. They recently made a special trip to squeeze me into their tight schedule for a quick repair in the heat of the summer. They also installed a new HVAC system for us recently, great pricing and they stepped us through all of the possible rebates. Excellent small business!'),
 ('2025-06-22','Jun 2025','These guys are fantastic! As someone who likes to do most repairs myself, these guys are the only ones I trust 100 percent with my HVAC system. They are great at troubleshooting and finding the actual issue. They don&rsquo;t try to sell you things you don&rsquo;t need, or recommend unnecessary repairs, which will save you money in the long run. If you are a current customer of theirs, and don&rsquo;t have a service contract, I would recommend purchasing one. Twice a year, they do a full inspection on your system from top to bottom...'),
 ('2024-12-02','Dec 2024','Carroll&rsquo;s is the best! Our heating system shut down on an extremely cold weekend and John came out and had us up and running in no time. Thank You so much for the excellent service!'),
 ('2023-07-25','Jul 2023','Excellent service from this company! Communication was prompt and specific. Technician Rodney was professional, polite, and personable. He was able to address our problem quickly and efficiently. We will certainly use this company again for future HVAC concerns!'),
 ('2022-06-22','Jun 2022','This company was recommended to me by my previous HVAC person, a family member who is now retired. I&rsquo;ve used Carroll Service Company for a couple of repairs to my now 20 year old heat pump and they&rsquo;ve been able to come out quickly. I&rsquo;ve found them to be honest and fair and Rodney, who completed both of the repairs, was very helpful and professional.'),
 ('2019-06-12','Jun 2019','I&rsquo;ve been a customer of Carroll Service Company for over 25 years. Just had a new HVAC installed. They&rsquo;re a wonderful family owned company, do great work, have fair prices, and really look out for their customers. I highly recommend them.'),
]
SITE = [('Out of necessity, we were recently faced with replacing our entire downstairs HVAC system. Carroll Service Company was referred to us by some friends who had used them and were very satisfied. Lee came out and gave us a verbal estimate. Within a few hours I was e-mailed formal, written estimates with two options. We scheduled the work for the following week. Brian and his crew arrived and worked non-stop with minimal interruptions while I was working from home. They are professional from start to finish and we would highly recommend them for any of your AC/heating needs!','Pam &amp; Pete, Fuquay Varina'),
 ('After nearly 20 years of flawless service from Lee Carroll installed heating and air conditioning equipment, it was time to replace the systems (4) with new and efficient components. Naturally we turned to Lee and his company and again we&rsquo;re rewarded with competitive pricing, on time installation and to date significant decreases in both electrical and natural gas costs.','Terry &amp; Chris'),
 ('Carroll Service Company&rsquo;s honesty, professionialism, and integrity have made it a pleasure to work with them for over twenty years. While working with them in the construction business, I have found their customer service to be second to none.','Sue, Garner NC')]
def card(i, cls=''):
    iso, d, q = REV[i]
    return f'<blockquote class="rcard rv {cls}"><div class="rc-top">{STARS}<time datetime="{iso}">{d}</time></div><p>&ldquo;{q}&rdquo;</p><footer>Google review</footer></blockquote>'
def scard(i, cls=''):
    q, who = SITE[i]
    return f'<blockquote class="rcard rcard--site rv {cls}"><p>&ldquo;{q}&rdquo;</p><footer><b>{who}</b> &middot; testimonial shown on carrollservicecompany.com</footer></blockquote>'

JOBS = [('May 2025','Raleigh 27606','First floor heat pump swapped for a gas furnace, AC and cased coil in the crawlspace, with a new gas line from the meter.','$17,800'),
 ('Sep 2025','Raleigh 27606','Two story house: both outdoor units and both air handlers replaced, one in the attic and one in the crawlspace.','$17,000'),
 ('Oct 2025','Raleigh 27606','Outdoor unit and whole house air handler replaced, with partial duct replacement.','$17,300'),
 ('May 2025','Raleigh 27615','First floor outdoor unit and air handler in the crawlspace.','$11,200'),
 ('May 2025','Apex 27539','Second floor outdoor unit and air handler in the attic.','$9,600'),
 ('Aug 2025','Raleigh 27603','Outdoor unit and whole home air handler in the crawlspace.','$8,200')]
EQUIP = [('Heat pump','Split system heat pump that heats and cools with an air handler. With or without a WeatherGuard top, in a range of SEER2 ratings.'),
 ('Gas furnace','Single or two stage gas heat in a range of AFUE efficiency ratings.'),
 ('Air handler','Pairs with the heat pump. Standard ECM blower or a high efficiency variable speed blower.'),
 ('Air conditioner','A range of SEER2 ratings, with or without a WeatherGuard top.'),
 ('Package units','Heat pump package units, or gas and electric package units, with single or two stage compressors.'),
 ('Dual fuel','A heat pump with gas backup: the heat pump runs on mild days and gas takes over on cold ones. A good fit if you heat with propane.')]

# ---------- HOME ----------
page('index.html','Heating and Air in Garner NC Since 1973 | Carroll Service Co.',
 'Carroll Service Company is a family owned heating and air company in Garner NC since 1973. Repairs, Trane installs and maintenance plans. Call (919) 772-8546.', f'''
<section class="mast"><div class="wrap mast-grid">
 <div class="mast-copy rv">{K('Heating and air conditioning &middot; Garner, NC','kicker--sky')}
  <h1>Sales, service and installation. <em>Same family since 1973.</em></h1>
  <p class="lede">Carroll Service Company is the Carroll family&rsquo;s heating and air business on West Main Street in Garner. Repairs on most makes and models, Trane, Tempstar and Mitsubishi installs, and maintenance agreements with two checks a year.</p>
  <div class="cta"><a class="btn btn--red" href="tel:{TEL}">Call {TEL_H}</a><a class="btn btn--line" href="contact.html">Free replacement estimate</a></div>
  <p class="mast-meta">Mon to Fri, 8 to 5 &middot; 125 W. Main Street &middot; HVAC NC license #10119</p></div>
 <figure class="mast-photo rv">{img('carroll-family-van.webp','Lee, Brian and Brandon Carroll standing beside a Carroll Service Company van',eager=True)}<figcaption>Lee, Brian and Brandon Carroll. Same 772&#8209;8546 on the side of the van.</figcaption>{SEAL('FAMILY OWNED &#183; GARNER NC &#183; HEATING &amp; AIR &#183; ','1973','','seal--hero')}</figure>
</div>
<div class="temp"><div class="wrap temp-grid"><a class="t t--cool" href="services.html#repair"><span>Cooling</span><b>AC repair, heat pumps, air handlers</b></a><a class="t t--warm" href="services.html#repair"><span>Heating</span><b>Furnaces, dual fuel, gas packs</b></a></div></div></section>

<section class="agree" aria-labelledby="ag-h"><div class="wrap agree-grid">
 <div class="rv">{K('Maintenance agreement','kicker--red')}<h2 id="ag-h">Two visits a year. <em>One before each season.</em></h2>
 <p>Carroll&rsquo;s annual service contract is prepaid at a discounted rate and covers two service checks: one in the heating season and one in the cooling season. The point is to catch a problem before it turns into a no heat call on a cold weekend.</p>
 <a class="btn btn--line" href="services.html#agreement">How the agreement works</a></div>
 <div class="seasons rv"><div class="sz sz--fall"><span class="sz-l">Check 1</span><b>Heating season</b><p>Heat pump or furnace, top to bottom.</p></div><div class="sz sz--spring"><span class="sz-l">Check 2</span><b>Cooling season</b><p>Outdoor unit, coil and air handler.</p></div>
 <blockquote class="sz-q"><p>&ldquo;If you are a current customer of theirs, and don&rsquo;t have a service contract, I would recommend purchasing one.&rdquo;</p><footer>Google review, June 2025</footer></blockquote></div>
</div></section>

<section class="voices" aria-labelledby="vo-h"><div class="wrap">
 <div class="voices-head rv">{SEAL('GOOGLE REVIEWS &#183; GOOGLE REVIEWS &#183; ','4.8','25 REVIEWS','seal--sm')}<div>{K('What customers say')}<h2 id="vo-h">They mention people <em>by name.</em></h2><p>Dennis on the phone. Rodney and John on the calls. Lee for the estimate. Brian and his crew on the install.</p></div></div>
 <div class="voices-grid">{card(2,'rcard--lead')}{card(4)}{card(6)}</div>
 <a class="btn btn--line rv" href="reviews.html">All the reviews</a>
</div></section>

<section class="record" aria-labelledby="rc-h"><div class="wrap record-grid">
 <div class="rv">{K('On the permit record','kicker--sky')}<h2 id="rc-h">What recent replacements <em>actually cost.</em></h2>
 <p>A permitted HVAC change out lists a project value on the permit. These six Carroll jobs are from 2025. Your house will differ, but this is the honest range.</p>
 <p class="fine">Permit valuations from <a href="{BZ}" rel="noopener">BuildZoom</a>, built from county permit records. Street addresses removed.</p></div>
 <ol class="jobs rv">{''.join(f'<li><span class="j-v">{v}</span><span class="j-w">{w} &middot; {d}</span><span class="j-d">{s}</span></li>' for d,w,s,v in JOBS)}</ol>
</div></section>

<section class="family" aria-labelledby="fa-h"><div class="wrap family-grid">
 <figure class="rv">{img('install-outdoor-unit.webp','A Carroll technician wiring a new outdoor unit beside a brick house')}</figure>
 <div class="rv">{K('The family','kicker--red')}<h2 id="fa-h">Started in Garner in 1973. <em>Still answering in Garner.</em></h2>
 <p>Carroll Service Company originated in Garner in 1973 and is still family owned and operated. The van says it plainly: Lee, Brian and Brandon Carroll.</p>
 <a class="btn btn--line" href="company.html">Meet the family</a></div>
</div></section>''', ld=[ORG,bc(('Home',''))])

# ---------- SERVICES ----------
page('services.html','HVAC Repair, Maintenance and Replacement | Carroll Service Co.',
 'HVAC repair on most makes, twice yearly maintenance agreements, and Trane, Tempstar and Mitsubishi replacements with permits and financing. Call Carroll today.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Services</p>{K('Services','kicker--sky')}<h1>Fix it, maintain it, <em>or replace it.</em></h1><p class="lede">Carroll services most makes and models of HVAC equipment across Wake County and the Clayton area.</p></div></section>
<div class="wrap svc">
<section id="repair" class="svc-block rv" aria-labelledby="r-h"><span class="svc-n">01</span><div><h2 id="r-h">Service and repair</h2><p>Residential technicians who respect your home and your time, with maintenance and repairs done in a timely and efficient way. Most makes and models.</p>
<p class="fine">&ldquo;They are great at troubleshooting and finding the actual issue. They don&rsquo;t try to sell you things you don&rsquo;t need.&rdquo; Google review, June 2025</p></div>{img('service-heat-pump.webp','A Carroll technician servicing a heat pump outside a brick home')}</section>
<section id="agreement" class="svc-block svc-block--sky rv" aria-labelledby="a-h"><span class="svc-n">02</span><div><h2 id="a-h">Maintenance agreements</h2><p>An annual service contract, prepaid at a discounted rate. It includes two service checks: one during the heating season and one during the cooling season. Regular checks can find an issue before it becomes a serious problem and extend the life of your equipment.</p>
<p class="note"><strong>Placeholder:</strong> the agreement price, what each check covers, and whether members get priority scheduling. None of that is published today.</p></div>{SEAL('TWO CHECKS A YEAR &#183; TWO CHECKS A YEAR &#183; ','2','PER YEAR','seal--md')}</section>
<section id="replace" class="svc-block rv" aria-labelledby="p-h"><span class="svc-n">03</span><div><h2 id="p-h">Replacements and new installations</h2><p>Free estimate appointments for new equipment. Financing is available with approved credit through Wells Fargo. Carroll supports you through every step, from furnishing your permits to registering your new equipment for warranty.</p>
<ol class="steps">{''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in [('Free estimate','During normal business hours.'),('Written options','One customer had formal written estimates with two options by email within a few hours.'),('Permit and install','Carroll furnishes the permits.'),('Warranty','Carroll registers the new equipment for warranty.')])}</ol></div>{img('install-outdoor-unit.webp','New outdoor unit being installed by Carroll')}</section>
</div>
<section id="equipment" class="wrap equip" aria-labelledby="e-h"><div class="rv">{K('Equipment','kicker--red')}<h2 id="e-h">Trane, Tempstar <em>and Mitsubishi.</em></h2><p>The systems Carroll installs most, in a range of SEER2 and AFUE ratings.</p></div>
<div class="equip-grid">{''.join(f'<article class="eq rv"><h3>{n}</h3><p>{d}</p></article>' for n,d in EQUIP)}</div>
<p class="note rv">Carroll is a Prequalified Duke Energy Contractor. <strong>Placeholder:</strong> current Duke Energy and federal rebate amounts, which one reviewer says Carroll walked them through.</p></section>''',
 ld=[ORG,bc(('Home',''),('Services','services.html'))]+[{"@context":"https://schema.org","@type":"Service","name":n,"provider":{"@type":"HVACBusiness","name":"Carroll Service Company, Inc."},"areaServed":"Wake County, NC"} for n in ['HVAC service and repair','HVAC maintenance agreement','HVAC replacement and installation']])

# ---------- REVIEWS ----------
page('reviews.html','4.8 Stars from 25 Google Reviews | Carroll Service Company',
 'Read what Garner and Raleigh homeowners say about Carroll Service Company: 4.8 stars from 25 Google reviews, plus testimonials. Call (919) 772-8546 for service.', f'''
<section class="page-head"><div class="wrap ph-grid"><div class="rv"><p class="crumbs"><a href="index.html">Home</a> / Reviews</p>{K('Reviews','kicker--sky')}<h1>One customer says <em>25 years.</em></h1><p class="lede">&ldquo;I&rsquo;ve been a customer of Carroll Service Company for over 25 years.&rdquo; Google review, June 2019.</p></div>
{SEAL('GOOGLE REVIEWS &#183; GOOGLE REVIEWS &#183; ','4.8','25 REVIEWS','seal--lg rv')}</div></section>
<div class="wrap">
<section class="rv-wall">{''.join(card(i) for i in range(len(REV)))}</section>
<section class="site-quotes" aria-labelledby="sq-h"><h2 id="sq-h" class="rv">From the testimonials page</h2><div class="sq-grid">{''.join(scard(i) for i in range(len(SITE)))}</div></section>
<section class="sources rv"><h2>Where these come from</h2><p>Google reviews are copied word for word from a September 2026 snapshot of Carroll&rsquo;s Google listing on the <a href="{EXA}" rel="noopener">Exa place page</a>. All eight shown are five stars; the 4.8 average means some of the 25 are lower. Three dots mark where the snapshot cuts a review short. The three testimonials are copied from carrollservicecompany.com and carry the names the site gives them, but they are undated and can&rsquo;t be traced further.</p>
<p class="note"><strong>Placeholder:</strong> a live Google reviews feed. Twenty five reviews in 53 years is low; a review request card left after each visit would help.</p></section>
</div>''', ld=[ORG,bc(('Home',''),('Reviews','reviews.html'))])

# ---------- COMPANY ----------
page('company.html','The Carroll Family, Garner Heating and Air Since 1973',
 'Carroll Service Company began in Garner in 1973 and is still family owned and operated by the Carrolls. Meet the family and the team customers mention by name.', f'''
<section class="page-head page-head--navy"><div class="wrap co-head"><div class="rv"><p class="crumbs"><a href="index.html">Home</a> / The family</p>{K('Our company','kicker--sky')}<h1>Garner, 1973. <em>Garner, today.</em></h1>
<p class="lede">Carroll Service Company originated in Garner, NC in 1973. It is family owned and operated, and has been part of the community for over 50 years.</p></div>
<figure class="co-photo rv">{img('carroll-family-van.webp','The Carroll family beside their lettered service van')}<figcaption>Lee, Brian and Brandon Carroll, as lettered on the van and the logo</figcaption></figure></div></section>
<div class="wrap co">
<section class="timeline rv" aria-labelledby="tl-h"><h2 id="tl-h">Fifty three years in four lines</h2><ol>{''.join(f'<li><b>{y}</b><span>{t}</span></li>' for y,t in [('1973','Carroll Service Company starts in Garner.'),('Over 50 years','Family owned and operated the whole way, now by Lee Carroll and his family.'),('2025','40 permitted HVAC projects on the public record, the busiest year since at least 2023.'),('Today','Office at 125 W. Main Street. Same phone number as the van.')])}</ol>
<p class="note"><strong>Placeholder:</strong> who founded it, the first shop, and the story behind the Main Street office. The live site gives the year and nothing else.</p></section>
<section class="team rv" aria-labelledby="tm-h"><h2 id="tm-h">Names customers mention</h2><ul>{''.join(f'<li><b>{n}</b><span>{r}</span></li>' for n,r in [('Lee Carroll','Owner. Came out for the estimate in one testimonial.'),('Brian Carroll','Owner on state records. Ran the install crew in one testimonial.'),('Brandon Carroll','Family. Named on the van, the logo and the Our Company page.'),('Dennis','&ldquo;Always so kind on the phone.&rdquo;'),('Nicole','&ldquo;Always cheerful.&rdquo;'),('Rodney','Technician, named in two reviews.'),('John','Fixed a no heat call on a cold weekend.')])}</ul>
<p class="fine">Roles come from reviews, the site and BuildZoom. <strong>TODO-VERIFY</strong> titles and spellings with Lee before launch.</p></section>
<figure class="garner rv">{img('historic-downtown-garner.webp','The Welcome to Historic Downtown Garner sign')}<figcaption>Historic Downtown Garner, home of the Main Street office. Photo from carrollservicecompany.com.</figcaption></figure>
</div>''', ld=[ORG,bc(('Home',''),('The family','company.html'))])

# ---------- CONTACT ----------
page('contact.html','Free HVAC Replacement Estimate in Garner | Carroll Service Co.',
 'Book a free HVAC replacement estimate or a service call with Carroll Service Company in Garner. Call (919) 772-8546, Monday to Friday 8 to 5. Wells Fargo financing.', f'''
<section class="page-head"><div class="wrap rv"><p class="crumbs"><a href="index.html">Home</a> / Free estimate</p>{K('Contact','kicker--sky')}<h1>Call the Main Street office. <em>Or send a note.</em></h1><p class="lede">Monday to Friday, 8am to 5pm. Free replacement estimates can be scheduled during normal business hours.</p></div></section>
<div class="wrap est-grid">
<form id="qform" class="rv" novalidate>
<fieldset><legend>What do you need?</legend><div class="chips-in">{''.join(f'<label><input type="radio" name="need" value="{k}"{" checked" if i==0 else ""}> {k}</label>' for i,k in enumerate(['Repair','Replacement estimate','Maintenance agreement','Not sure']))}</div></fieldset>
<fieldset><legend>Is it heating or cooling?</legend><div class="chips-in">{''.join(f'<label><input type="radio" name="mode" value="{k}"> {k}</label>' for k in ['Heating','Cooling','Both'])}</div></fieldset>
<div class="two"><div class="field"><label for="n">Name</label><input id="n" name="name" autocomplete="name" required></div><div class="field"><label for="p">Phone</label><input id="p" name="tel" type="tel" autocomplete="tel" required></div></div>
<div class="field"><label for="a">Street address</label><input id="a" name="address" autocomplete="street-address"></div>
<div class="field"><label for="m">What&rsquo;s it doing?</label><textarea id="m" name="msg" rows="5"></textarea></div>
<button class="btn btn--red" type="submit">Send to the office <span aria-hidden="true">&rarr;</span></button>
<p class="note" id="qmsg" role="status">Demo form. Nothing is sent.</p></form>
<aside class="rv"><div class="card"><p class="kicker kicker--sky"><span class="k-dot" aria-hidden="true"></span>Office</p><a class="phone" href="tel:{TEL}">{TEL_H}</a><p>125 W. Main Street<br>Garner, NC 27529<br>Mon to Fri, 8am to 5pm</p><p class="fine">HVAC NC license #10119. Cash, check and major cards. Financing with approved credit through Wells Fargo.</p></div>
<p class="note"><strong>Placeholder:</strong> after hours instructions. The site does not say what to do when the heat goes out on a weekend.</p></aside>
</div>''', ld=[ORG,bc(('Home',''),('Free estimate','contact.html'))])

page('404.html','Page Not Found | Carroll Service Company, Garner NC Heating',
 'That page is not here. Head back to the Carroll Service Company home page or call the Garner office at (919) 772-8546 for heating and air service or an estimate.',
 f'<section class="wrap nf">{K("404","kicker--red")}<h1>This page <em>lost its pilot light.</em></h1><p style="margin-top:28px"><a class="btn btn--red" href="index.html">Back to the home page</a></p></section>')
print('built')
