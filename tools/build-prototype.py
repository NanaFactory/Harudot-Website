#!/usr/bin/env python3
"""Assembles the static design prototype in prototype/ from content/branches.json.

Run from the repository root:  python3 tools/build-prototype.py
The two pages share a masthead, a foot and the branch map, so they are assembled here
rather than kept in step by hand. The output is plain HTML with no build step of its own.
"""
import json, os, glob, html, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'prototype')
B = json.load(open(os.path.join(ROOT, 'content/branches.json'), encoding='utf-8'))['branches']
BY = {b['slug']: b for b in B}
CREDIT = 'DOF Sky | Ground'


def t(en, th, tag='span', cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c} data-l="en" lang="en">{en}</{tag}><{tag}{c} data-l="th" lang="th">{th}</{tag}>'


def pic(n, alt, sizes='100vw', eager=False, cls=''):
    files = sorted(glob.glob(os.path.join(P, f'assets/img/chonburi/{n}-*.webp')), key=lambda f: int(f.rsplit('-', 1)[1][:-5]))
    w, h = Image.open(files[-1]).size
    srcset = ', '.join(f'assets/img/chonburi/{os.path.basename(f)} {os.path.basename(f).rsplit("-", 1)[1][:-5]}w' for f in files)
    mid = os.path.basename(files[min(1, len(files) - 1)])
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="assets/img/chonburi/{mid}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{html.escape(alt)}" {load}>'


def fig(n, cap_en, cap_th, span='', sizes='100vw', eager=False):
    c = f'fig {span}'.strip()
    return f'<figure class="{c}">{pic(n, cap_en, sizes, eager)}<figcaption>{t(cap_en, cap_th)}</figcaption></figure>'


ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M1 8h13M9 3l5 5-5 5"/></svg>'
PIN = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M8 15V7M8 1v0M4.5 4.5a3.5 3.5 0 1 1 7 0a3.5 3.5 0 0 1-7 0Z"/></svg>'
TRI_L = '<svg viewBox="0 0 7 10" aria-hidden="true"><path d="M7 0v10L0 5z" fill="currentColor"/></svg>'
TRI_R = '<svg viewBox="0 0 7 10" aria-hidden="true"><path d="M0 0v10l7-5z" fill="currentColor"/></svg>'
LOGO = open(os.path.join(P, 'assets/img/harudot-lockup.svg'), encoding='utf-8').read().split('?>', 1)[-1].strip()
MAPS = ''.join(open(os.path.join(P, f'assets/map/map-{v}.svg'), encoding='utf-8').read() for v in ('desktop', 'mobile'))


def head(title, desc, branch='chonburi'):
    return f'''<!doctype html>
<html lang="en" data-lang="en" data-branch="{branch}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<link rel="preload" href="assets/fonts/haruno-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">{t('Skip to the page', 'ข้ามไปยังเนื้อหา')}</a>
<div class="sheet">
<header class="mast">
  <a class="mast__logo" href="index.html" aria-label="Harudot by Nana Coffee Roasters, home">{LOGO}</a>
  <nav aria-label="Main"><ul>
    <li><a href="index.html#branches">{t('Branches', 'สาขา')}</a></li>
    <li><a href="index.html#promotions">{t('Promotions', 'โปรโมชัน')}</a></li>
    <li><a href="index.html#about">{t('About', 'เกี่ยวกับเรา')}</a></li>
    <li><a href="#contact">{t('Contact', 'ติดต่อ')}</a></li>
  </ul></nav>
  <div class="lang" role="group" aria-label="Language"><button type="button" data-set="en" aria-pressed="true" lang="en">EN</button><button type="button" data-set="th" aria-pressed="false" lang="th">ไทย</button></div>
</header>
<main id="main">
'''


def tel(b):
    return f'<a href="tel:{b["phone"].replace(" ", "")}">{b["phone"].replace("+66 ", "0")}</a>'


def promo():
    return f'''<article class="promo">
    <img src="assets/img/drinks/haru-haru.webp" width="720" height="720" alt="A haru haru iced drink in a Harudot cup" loading="lazy" decoding="async">
    <div><span class="chip">{t('Sample', 'ตัวอย่าง')}</span>
      <h3>{t('How an offer will look', 'หน้าตาของโปรโมชัน')}</h3>
      <p>{t('A title, one picture, the branches it applies to and its dates. It leaves the page by itself after the end date.', 'ชื่อโปรโมชัน รูปหนึ่งรูป สาขาที่ร่วมรายการ และช่วงวันที่ เมื่อครบกำหนดจะหายไปจากหน้าเว็บเอง')}</p>
      <p class="lbl">{t('All branches · start date to end date', 'ทุกสาขา · วันเริ่มต้น ถึง วันสิ้นสุด')}</p></div>
  </article>'''


def foot():
    phones = ''.join(f'<li><span>{t(b["en"], b["th"])}</span>{tel(b)}</li>' for b in B)
    return f'''</main>
<footer class="foot" id="contact">
  <div class="ground ground--bleed"></div>
  <div class="tb tb--foot">
    <div><div class="mast__logo">{LOGO}</div>
      <p>{t('The sister brand of Nana Coffee Roasters.', 'แบรนด์ในเครือนานา คอฟฟี่ โรสเตอร์')}</p>
      <p>© 2026 Harudot by Nana Coffee Roasters</p></div>
    <div><h2 class="lbl">{t('Call a branch', 'โทรหาสาขา')}</h2><ul class="phones">{phones}</ul></div>
    <div><h2 class="lbl">{t('Events, photo shoots, press', 'จัดงาน ถ่ายภาพ สื่อมวลชน')}</h2>
      <div class="void" style="min-height:9rem"><p>{t('Enquiry form to come', 'แบบฟอร์มติดต่อกำลังตามมา')}</p></div></div>
  </div>
</footer>
</div>
<script src="assets/js/branches.js"></script>
<script src="assets/js/site.js"></script>
</body>
</html>
'''


def home():
    b = BY['chonburi']
    rows = ''
    for x in B:
        sheet = f'<a class="btn" href="{x["sheet"]}">{t("Open sheet", "ดูสาขานี้")}{ARROW}</a>' if x.get('sheet') else ''
        rows += f'''<li data-branch="{x['slug']}"><div class="row">
      <span class="row__n">{x['n']}</span>
      <button type="button" class="row__name" data-branch="{x['slug']}">{t(x['en'].lower(), x['th'])}</button>
      <p class="row__meta">{t(x['areaEn'], x['areaTh'])}</p>
      <p class="row__meta"><span data-hours="{x['slug']}">{x['open']} to {x['close']}</span><br><span class="state" data-state="{x['slug']}"><i></i><span></span></span></p>
      <div class="row__acts">{sheet}<a class="btn btn--fill" href="{x['maps']}" target="_blank" rel="noopener">{t('Directions', 'เส้นทาง')}{PIN}</a></div>
    </div></li>'''
    return head('Harudot by Nana Coffee Roasters', 'Seven Harudot cafés from Bangkok to Chonburi and Khao Yai. Pick a branch on the map, see it, and get directions.') + f'''
<h1 class="vh">Harudot by Nana Coffee Roasters</h1>

<section id="pick" data-picker aria-label="Pick a branch">
  <div class="pick">
    <figure class="plate" data-empty="false">
      <div class="plate__frame">
        {pic(b['inside'], b['insideAltEn'], '(max-width: 820px) 100vw, 62vw', True, 'plate__in')}
        {pic(b['outside'], b['outsideAltEn'], '(max-width: 820px) 100vw, 62vw', True, 'plate__out')}
        <div class="void"><p>{t('Photographs to come', 'ภาพถ่ายกำลังตามมา')}</p></div>
        <div class="cutline" aria-hidden="true"><span class="mark">A</span><span class="mark">A</span><span class="grip">{TRI_L}{t('Drag the cut', 'ลากเส้นตัด')}{TRI_R}</span></div>
        <input type="range" min="0" max="100" step="0.1" value="58" aria-label="Section cut. Slide left to see more of the inside, right to see more of the outside.">
        <span class="tag tag--out">{t('Outside', 'ภายนอก')}</span><span class="tag tag--in">{t('Inside', 'ภายใน')}</span>
      </div>
      <figcaption class="lbl"><span data-f="credit">{t('Photographs', 'ภาพถ่าย')}: {CREDIT}</span></figcaption>
    </figure>
    <div class="picker">
      <div class="picker__head"><h2>{t('Pick a branch', 'เลือกสาขา')}</h2><span class="lbl">{t('7 cafés', '7 สาขา')}</span></div>
      {MAPS}
    </div>
  </div>
  <div class="ground ground--bleed"></div>
  <div class="tb tb--pick" aria-live="polite">
    <div><span class="lbl">{t('Branch', 'สาขา')}</span><p class="val name"><span data-f="name-en" data-l="en" lang="en">{b['en']}</span><span data-f="name-th" data-l="th" lang="th">{b['th']}</span></p>
      <p class="vh"><span data-f="full-en" data-l="en" lang="en"></span><span data-f="full-th" data-l="th" lang="th"></span></p></div>
    <div><span class="lbl">{t('Today', 'วันนี้')}</span><p class="val"><span data-f="hours" data-hours="chonburi">{b['open']} to {b['close']}</span><br><span class="state" data-f="state" data-state="chonburi"><i></i><span></span></span></p></div>
    <div><span class="lbl">{t('Where', 'ที่ตั้ง')}</span><p class="val"><span data-f="area-en" data-l="en" lang="en">{b['areaEn']}</span><span data-f="area-th" data-l="th" lang="th">{b['areaTh']}</span></p></div>
    <div><span class="lbl">{t('Call', 'โทร')}</span><p class="val"><a data-f="phone" href="tel:{b['phone'].replace(' ', '')}">{b['phone'].replace('+66 ', '0')}</a></p></div>
    <div class="tb__act"><a class="btn btn--fill" data-f="maps" href="{b['maps']}" target="_blank" rel="noopener">{t('Directions', 'เส้นทาง')}{PIN}</a></div>
    <div class="tb__act"><a class="btn" data-f="sheet" href="chonburi.html"><span data-sheet-label="yes">{t('Open sheet', 'ดูสาขานี้')}</span><span data-sheet-label="no" hidden>{t('Sheet to come', 'หน้าสาขากำลังตามมา')}</span>{ARROW}</a></div>
  </div>
</section>

<section class="sec" id="branches">
  <div class="sec__head"><h2>{t('all branches', 'สาขาทั้งหมด')}</h2><p>{t('Tap a name to see it on the map. Hours are for today, Bangkok time.', 'แตะชื่อสาขาเพื่อดูบนแผนที่ เวลาที่แสดงคือเวลาทำการวันนี้')}</p></div>
  <ol class="index">{rows}</ol>
</section>

<figure class="fig bleed sec">
  {pic('025', 'Looking straight up from the court: the pine roof opens in a curved void and a bottle tree grows through it into blue sky', '100vw')}
  <figcaption>{t('Harudot Chonburi. The roof is pulled apart around a bottle tree.', 'ฮารุดอท ชลบุรี หลังคาแยกออกเพื่อเปิดทางให้ต้นไม้เติบโตขึ้นสู่ท้องฟ้า')}<a href="chonburi.html">{t('Open the Chonburi sheet', 'ดูสาขาชลบุรี')}</a></figcaption>
</figure>

<section class="sec" id="promotions">
  <div class="sec__head"><h2>{t('promotions', 'โปรโมชัน')}</h2><p>{t('Nothing has been entered yet. This card shows the layout only.', 'ยังไม่มีโปรโมชันในระบบ การ์ดนี้แสดงรูปแบบเท่านั้น')}</p></div>
  <div class="two">{promo()}</div>
</section>

<section class="sec" id="about">
  <div class="sec__head"><h2>{t('about', 'เกี่ยวกับเรา')}</h2></div>
  <div class="about">
    {t('haru is spring. dot is a starting point.', 'ฮารุคือฤดูใบไม้ผลิ ดอทคือจุดเริ่มต้น', 'p', 'say')}
    <div class="prose">
      {t('Harudot is the sister brand of Nana Coffee Roasters. The name joins haru, Japanese for spring, to dot, a starting point. Seven cafés are open, from the middle of Bangkok to Chonburi and Khao Yai.', 'ฮารุดอทเป็นแบรนด์ในเครือของนานา คอฟฟี่ โรสเตอร์ ชื่อนี้มาจากคำว่า ฮารุ ที่แปลว่าฤดูใบไม้ผลิในภาษาญี่ปุ่น รวมกับ ดอท ที่หมายถึงจุดเริ่มต้น ปัจจุบันเปิดให้บริการเจ็ดสาขา ตั้งแต่ใจกลางกรุงเทพฯ ไปจนถึงชลบุรีและเขาใหญ่', 'p')}
      <a class="btn" href="https://nanacoffeeroasters.com" target="_blank" rel="noopener">Nana Coffee Roasters{ARROW}</a>
    </div>
  </div>
</section>
''' + foot()


def chonburi():
    b = BY['chonburi']
    drinks = [('haru-haru', 'haru haru'), ('kuro', 'kuro'), ('shiro', 'shiro'), ('premium-matcha', 'premium matcha'), ('citrus-latte', 'citrus latte'), ('flat-white', 'flat white')]
    menu = ''.join(f'<li><img src="assets/img/drinks/{f}.webp" width="720" height="720" alt="{n.capitalize()}, as served at Harudot" loading="lazy" decoding="async"><p>{n}</p></li>' for f, n in drinks)
    half = '(max-width: 820px) 100vw, 50vw'
    return head('Harudot Chonburi by Nana Coffee Roasters', 'Harudot Chonburi: photographs, opening hours, address and directions.') + f'''
<div class="title">
  <div>
    <h1>{t('chonburi', 'ชลบุรี')}</h1>
    <p class="title__full">{t('Harudot Chonburi by Nana Coffee Roasters', 'ฮารุดอท ชลบุรี บาย นานา คอฟฟี่ โรสเตอร์')}</p>
  </div>
  <div class="title__acts"><a class="btn btn--fill" href="{b['maps']}" target="_blank" rel="noopener">{t('Directions', 'เส้นทาง')}{PIN}</a><a class="btn" href="tel:{b['phone'].replace(' ', '')}">{t('Call', 'โทร')} {b['phone'].replace('+66 ', '0')}</a></div>
</div>

<figure class="fig">
  {pic('069', 'Harudot Chonburi from the road: three black timber gables, each opening lined in pine', '100vw', True)}
</figure>
<div class="ground ground--bleed"></div>
<dl class="tb tb--facts">
  <div><dt class="lbl">{t('Today', 'วันนี้')}</dt><dd><span data-hours="chonburi">{b['open']} to {b['close']}</span><br><span class="state" data-state="chonburi"><i></i><span></span></span></dd></div>
  <div><dt class="lbl">{t('Call', 'โทร')}</dt><dd>{tel(b)}</dd></div>
  <div class="wide"><dt class="lbl">{t('Address', 'ที่อยู่')}</dt><dd>{t(b['addressEn'], b['addressTh'])}</dd></div>
  <div><dt class="lbl">{t('Architecture and interior', 'สถาปัตยกรรมและตกแต่งภายใน')}</dt><dd>IDIN Architects</dd></div>
  <div><dt class="lbl">{t('Photographs', 'ภาพถ่าย')}</dt><dd>{CREDIT}</dd></div>
  <div><dt class="lbl">{t('Completed', 'แล้วเสร็จ')}</dt><dd>2023</dd></div>
  <div><dt class="lbl">{t('Usable area', 'พื้นที่ใช้สอย')}</dt><dd>{t('475 sq m', '475 ตร.ม.')}</dd></div>
</dl>

<section class="sec" id="plates">
  <div class="sec__head"><h2>{t('plates', 'ภาพถ่าย')}</h2><p>{t('Through the building in the order you meet it: approach, threshold, heart, detail, seat, bar.', 'เดินชมอาคารตามลำดับที่คุณจะได้พบ ตั้งแต่ทางเข้า ธรณีประตู ใจกลางอาคาร รายละเอียด ที่นั่ง จนถึงบาร์')}</p></div>
  <div class="plates">
    {fig('082', 'Approach. The three gables at dusk, lit from inside.', 'ทางเข้า จั่วสามหลังยามพลบค่ำ สว่างจากแสงภายใน', 's7', '(max-width: 820px) 100vw, 58vw')}
    {fig('016', 'Threshold. The edge of a gable, with the olive tree beside it.', 'ธรณีประตู ขอบจั่วและต้นมะกอกที่อยู่เคียงกัน', 's5', '(max-width: 820px) 100vw, 42vw')}
    {fig('053', 'Heart. A tree stands in the middle of the room, under an arch of pine.', 'ใจกลางอาคาร ต้นไม้ยืนอยู่กลางห้องใต้ซุ้มโค้งไม้สน', 's8', '(max-width: 820px) 100vw, 66vw')}
    {fig('063', 'Detail. Words set into the terrazzo floor.', 'รายละเอียด ถ้อยคำที่ฝังอยู่ในพื้นหินขัด', 's4', '(max-width: 820px) 100vw, 34vw')}
    {fig('049', 'Seat. One counter runs around the room like a ribbon.', 'ที่นั่ง เคาน์เตอร์เส้นเดียวทอดยาวรอบห้องดั่งริบบิ้น', 's6', half)}
    {fig('040', 'Seat. The lounge, looking out through two arches.', 'ที่นั่ง มุมเลานจ์ที่มองออกไปผ่านซุ้มโค้งสองช่อง', 's6', half)}
    {fig('044', 'Bar. Coffee is made under a soft, glowing ceiling.', 'บาร์ กาแฟถูกชงใต้ฝ้าเพดานที่เรืองแสงนุ่มนวล', 's8 from3', '(max-width: 820px) 100vw, 66vw')}
  </div>
</section>

<section class="sec" id="building">
  <div class="sec__head"><h2>{t('the building', 'ตัวอาคาร')}</h2></div>
  <div class="story">
    {t('Three black gables, pulled apart to let a tree through.', 'จั่วสีดำสามหลัง ที่แยกออกเพื่อเปิดทางให้ต้นไม้', 'h3')}
    <div class="prose">
      {t('Harudot Chonburi stands in Samet, in the seaside town of Chonburi. From the road it is three plain gables in black timber. Step inside and the walls and ceiling turn to warm pine and begin to curve.', 'ฮารุดอท ชลบุรี ตั้งอยู่ที่ตำบลเสม็ด ในเมืองชายทะเลชลบุรี เมื่อมองจากถนนจะเห็นจั่วเรียบง่ายสามหลังกรุด้วยไม้สีดำ เมื่อก้าวเข้าไป ผนังและเพดานจะเปลี่ยนเป็นไม้สนโทนอุ่นและเริ่มโค้งตัว', 'p')}
      {t('Where the roof is pulled apart, a bottle tree grows up through the opening, and rain and sunlight come down into the court. The seating runs around the room as one ribbon, and the terrazzo floor carries words that lead you through the café.', 'ตรงจุดที่หลังคาแยกออก ต้นไม้เติบโตทะลุช่องเปิดขึ้นไป ฝนและแสงแดดจึงส่องลงมาถึงลานด้านใน ที่นั่งทอดยาวรอบห้องเป็นเส้นเดียวดั่งริบบิ้น และพื้นหินขัดมีถ้อยคำที่นำทางคุณไปทั่วร้าน', 'p')}
    </div>
  </div>
</section>

<section class="sec" id="menu">
  <div class="sec__head"><h2>{t('from the menu', 'จากเมนู')}</h2><p>{t('Six drinks. The full menu pages will sit here once they are supplied.', 'เครื่องดื่มหกรายการ หน้าเมนูฉบับเต็มจะแสดงที่นี่เมื่อได้รับไฟล์')}</p></div>
  <ul class="menu">{menu}</ul>
</section>

<section class="sec" id="promotions">
  <div class="sec__head"><h2>{t('promotions', 'โปรโมชัน')}</h2><p>{t('Nothing has been entered yet. This card shows the layout only.', 'ยังไม่มีโปรโมชันในระบบ การ์ดนี้แสดงรูปแบบเท่านั้น')}</p></div>
  <div class="two">{promo()}</div>
</section>

<section class="sec" id="find">
  <div class="sec__head"><h2>{t('find it', 'เส้นทาง')}</h2></div>
  <div class="loc">
    <div>
      {t(b['addressEn'], b['addressTh'], 'address')}
      <div class="acts"><a class="btn btn--fill" href="{b['maps']}" target="_blank" rel="noopener">{t('Directions', 'เส้นทาง')}{PIN}</a><a class="btn" href="tel:{b['phone'].replace(' ', '')}">{t('Call', 'โทร')} {b['phone'].replace('+66 ', '0')}</a></div>
      <dl><dt class="lbl">{t('Today', 'วันนี้')}</dt><dd><span data-hours="chonburi">{b['open']} to {b['close']}</span>, <span class="state" data-state="chonburi"><i></i><span></span></span></dd></dl>
    </div>
    <div>{MAPS}</div>
  </div>
</section>

<nav class="pager" aria-label="Other branches">
  <a href="index.html#future-park-rangsit"><span class="lbl">{t('Previous', 'ก่อนหน้า')}</span><span class="name">{t('future park rangsit', 'ฟิวเจอร์พาร์ค รังสิต')}</span></a>
  <a href="index.html#khao-yai"><span class="lbl">{t('Next', 'ถัดไป')}</span><span class="name">{t('khao yai', 'เขาใหญ่')}</span></a>
</nav>
''' + foot()


def shareable(page, out_dir):
    """A copy for publishing as a private preview page: the host supplies the document shell for the
    entry page, and the brand face is embedded so it cannot silently fall back."""
    import base64, re, shutil
    font = base64.b64encode(open(os.path.join(P, 'assets/fonts/haruno-regular.woff2'), 'rb').read()).decode()
    extra = ('<meta name="claude:viewport-fit-sides" content="cover">\n'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bai+Jamjuree:wght@400;500;600;700&display=swap">\n'
             '<link rel="stylesheet" href="assets/css/site.css">\n'
             '<style>@font-face { font-family: "haruno"; src: url("data:font/woff2;base64,' + font + '") format("woff2"); font-weight: 400; unicode-range: U+0020-002F, U+003A-007E; }\n'
             '.sheet { padding-left: max(var(--m), env(safe-area-inset-left, 0px)); padding-right: max(var(--m), env(safe-area-inset-right, 0px)); }</style>\n')
    page = re.sub(r'<link rel="preload"[^>]*>\n', '', page).replace('<link rel="stylesheet" href="assets/css/site.css">\n', extra)
    return page


if '--share' in sys.argv:
    out = sys.argv[sys.argv.index('--share') + 1]
    os.makedirs(out, exist_ok=True)
    h = shareable(home(), out).replace('<title>Harudot by Nana Coffee Roasters</title>', '<title>Harudot Website Prototype</title>')
    # entry page: content only, the host wraps it
    body = h.split('<body>', 1)[1].rsplit('</body>', 1)[0]
    headbits = ''.join(l + '\n' for l in h.split('<head>', 1)[1].split('</head>', 1)[0].splitlines() if l.startswith(('<title', '<meta name="claude', '<link', '<style', '.sheet')))
    boot = '<script>document.documentElement.dataset.lang = "en"; document.documentElement.dataset.branch = "chonburi";</script>\n'
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(headbits + boot + body)
    open(os.path.join(out, 'chonburi.html'), 'w', encoding='utf-8').write(shareable(chonburi(), out))
    print('share copy written to', out)

open(os.path.join(P, 'index.html'), 'w', encoding='utf-8').write(home())
open(os.path.join(P, 'chonburi.html'), 'w', encoding='utf-8').write(chonburi())
keep = ('n', 'slug', 'en', 'th', 'areaEn', 'areaTh', 'phone', 'open', 'close', 'maps', 'sheet', 'outside', 'inside', 'outsideAltEn', 'insideAltEn')
open(os.path.join(P, 'assets/js/branches.js'), 'w', encoding='utf-8').write(
    'window.HARUDOT = ' + json.dumps({'branches': [{k: b[k] for k in keep if k in b} for b in B]}, ensure_ascii=False) + ';\n')
print('built', [os.path.getsize(os.path.join(P, f)) for f in ('index.html', 'chonburi.html')])
