# Harudot website plan

Plan for harudot.com, the first website for Harudot by Nana Coffee Roasters. Written 2026-11-26. Product facts and their sources are in [`PRODUCT.md`](../PRODUCT.md); this file is the plan built on them. Nothing has been built yet.

**Status (updated 2026-11-26, evening):** direction A is chosen, with a map for picking a branch. Hosting is WordPress.com, Personal plan, with harudot.com staying registered at SiteGround. The home page and the Chonburi page now exist as a working design prototype in [`prototype/`](../prototype/), built with your real logo, font, photographs and branch details. What is still missing is listed in section 7.

To view the prototype on a computer, download the repository, then from the `prototype` folder run `python3 -m http.server` and open `http://localhost:8000`.

## 1. What the site is for

A visitor arrives, usually on a phone, having seen a Harudot building somewhere. They want to see the place properly, find out which branch is near them, check the menu and what's on, and get there. A smaller group wants to ask about private events, photo shoots, press or collaborations.

So the site succeeds when:

- a visitor sees large, real photographs of a branch within a second or two of arriving;
- from any page, the hours and directions for any branch are one tap away;
- an enquiry reaches your team;
- your staff can change a menu or promotion in both languages without calling anyone.

It is not a shop, not a delivery portal and not a blog.

## 2. Platform: WordPress.com, Personal plan

**Decided: WordPress, hosted on WordPress.com's Personal plan. The domain harudot.com stays registered at SiteGround and is connected to the WordPress.com site.**

Checked against WordPress.com's own pricing and plan pages on 2026-11-26:

| Question | Answer |
|---|---|
| Does the Personal plan allow a domain registered elsewhere? | Yes. "Connect a domain you registered elsewhere" is available on Personal and above. The domain stays at SiteGround and you keep renewing it there. |
| Can it run a theme written for Harudot, and plugins? | Yes. Their plan page lists Personal as including plugin installation, theme file upload, SFTP and GitHub deployments. (This used to need the Business plan; it no longer does.) |
| Price | Shown as $4 a month for the first year, billed yearly, renewing at $5 a month ($60 a year), before tax. Prices can differ by currency and country. |
| Storage | 6 GB. Enough for seven branches if photographs are exported at web size (about 2560 px on the long edge, well under 1 MB each) rather than uploaded straight from the camera. |

What the Personal plan does not include, and what we do about it:

- **No staging copy of the site and no one-click restore** (those start at Business). The theme lives in this repository, so the code is always recoverable; content can be exported from the WordPress admin, which I'd put on a monthly reminder for staff.
- **No Google Analytics** (starts at Premium). The plan already avoids tracking cookies; the built-in visitor stats are included.
- **No mailbox at harudot.com.** Enquiries from the contact form are delivered to an address you already use.

**How the domain is connected.** In WordPress.com: Domains, "Use a domain name I own", choose *connect* (not transfer). Then in SiteGround, replace the domain's name servers with `ns1.wordpress.com`, `ns2.wordpress.com` and `ns3.wordpress.com`. harudot.com has no website or email records today, so nothing existing is disturbed. When buying the plan, skip the "free domain for one year" offer; you already own the name.

**How it's built.** A hand-written theme held in this repository, deployed to WordPress.com from GitHub. Two content types staff fill in as simple forms, **Branch** and **Promotion** (fields in section 5). Free plugins only, kept short: one for Thai and English, one for the custom fields, one for the contact form.

### Running costs

| Item | Cost |
|---|---|
| Domain harudot.com | Already owned; yearly renewal continues at SiteGround |
| WordPress.com Personal | About $48 the first year, then about $60 a year, before tax |
| Theme, plugins | Free |
| Maps | Free (own drawn map; Directions links open Google Maps) |
| Fonts | Free web fonts; Harudot's own signage font only if you hold a licence that covers websites |
| Photographs | Whatever your photographers require for web use and credit |

## 3. Visual direction: A, "Drawn to scale", with a map picker

**Chosen: direction A, and visitors pick a branch from a map of Thailand.** Sketch: [`sketches/direction-a-map.jpg`](sketches/direction-a-map.jpg). The earlier three options are kept in the same folder for reference.

The site is an architect's drawing set. Pale paper ground, black line, one clay-pink fill taken from the Khao Yai concrete. Each branch is a numbered sheet with a "title block" holding address, hours and credits.

**Home page.** A photograph of the selected branch on one side, with a cut line you drag to pass from outside the building to inside. Beside it, the map: tap a point or a name and the photograph changes to that branch; "Open sheet" goes to its page.

**How the map works.** All seven branches lie within about 150 km of Bangkok, and four of them sit inside a few kilometres of each other. On a map of the whole country they would be a single dot. So the map is drawn the way an architect would draw it:

- a small **key plan** of Thailand showing where we are looking;
- an enlarged **detail plan** of the Bangkok, Chonburi and Khao Yai area with each branch at its true position (taken from your Google Maps links);
- the four inner-Bangkok branches labelled with leader lines so their names don't collide;
- the branch names are the tap targets as well as the points, because points that close together can't be tapped reliably on a phone;
- on a phone, a plain list of all branches sits directly under the map.

The map is drawn for the site (no paid map service, no Google Maps embed on the home page). A new branch appears on it when staff enter its coordinates. If a branch ever opens far outside this area, such as Chiang Mai or Phuket, the detail plan widens to include it.

**What stays fixed:** photographs are large and shown whole; very little interface; photographer and architect credited; Thai and English given equal weight.

**What it needs from you:** one exterior and one interior photograph per branch for the cut line. Optional: a simple plan or section drawing from the architects for the two flagship cafés.

**Honest risk:** drawing language can feel technical to someone who just wants a coffee. The plain wording ("Pick a branch", "Directions", "Open today") is what keeps it friendly, so labels stay in everyday language and only the look borrows from drawings.

## 4. Pages

| Page | What's on it |
|---|---|
| **Home** | Photograph of the selected branch with the outside-to-inside cut line; the map of Thailand for picking a branch; a short line on what Harudot is; current promotions, if any. |
| **Branches** | All branches at a glance: photo, area, "open now" or today's hours. Grouped as Bangkok and beyond Bangkok once that's useful. |
| **Branch** (one per branch) | Photo sequence; address, hours, phone, parking; a Directions button that opens Google Maps; the menu; current promotions at this branch; the story of the building where there is one; architect and photographer credits. |
| **Promotions** | Everything currently running, filterable by branch. |
| **About** | The Harudot name and idea, the relationship to Nana Coffee Roasters, a link to Nana for buying beans. |
| **Contact** | Enquiry form with a topic (private event, photo shoot, press, collaboration, other) and a branch selector; branch phone numbers listed beside it. |
| **Privacy** | Required because the form collects personal details (Thailand's PDPA). |

Every page exists in Thai and English with a language switch that stays on the same page.

### Additions (all approved)

- **"Open now" on every branch**, worked out from the opening hours staff enter, including one-off closures.
- **Start and end dates on promotions**, so an expired offer disappears by itself. Stale promotions are the most common way a café site goes wrong.
- **"Coming soon" state for a branch**, so a new café can be announced before it opens.
- **A few signature items typed as text on each branch**, beside the uploaded menu images. Menu images can't be read by Google or by screen readers; five to eight typed lines per branch fix that for very little effort.
- **Menus uploaded as images, not PDF.** PDFs open awkwardly on phones. Each menu shows the date it was last updated.
- **Branch details marked up for Google**, so hours, address and photos can appear in search results and Maps.
- **Press and awards page, later.** Useful once you have material; it also gives press a place to request photographs.

### Deliberately left out

- Delivery-app links and LINE chat as main actions (you didn't choose them; easy to add per branch later).
- An embedded Instagram feed: slow, breaks often, and brings tracking cookies. A plain link instead.
- Tracking cookies at launch. Without them no cookie banner is needed. Google Search Console still shows how people find the site.
- A blog, unless someone on the team commits to writing it.
- Pop-ups, page-builder plugins, paid themes.

## 5. What staff fill in

**Branch**

- Name, in Thai and English
- Status: open, temporarily closed, coming soon
- Address, Google Maps link, map coordinates, phone, parking note
- Opening hours by weekday, plus dated exceptions
- Photographs in order, each with a short description and credit
- Menu images, with the date updated
- Signature items (optional short list)
- Story of the building, facts (area, year), architect and other credits (optional)

**Promotion**

- Title and short text, in Thai and English
- One image
- Which branches it applies to
- Start date and end date

Staff get an Editor login that shows only Branches, Promotions and the enquiry inbox. Adding an eighth branch is filling in one Branch form.

## 6. Ranges and states the design must handle

- **Photos per branch:** from 3 casual photos to 40 professional ones. A branch page has to look finished at both ends, since only some branches have full sets today.
- **Promotions:** none to about five at once per branch. With none, the section is simply absent.
- **Menu:** one to about eight images per branch; possibly not uploaded yet.
- **Branch:** open now, closed now (shows when it next opens), closed today, temporarily closed, coming soon.
- **Promotion:** scheduled, running, ended.
- **Language:** a page not yet translated shows the other language with a short note rather than a blank.
- **Form:** sending, sent, failed (says what to do instead: the phone number).
- **Slow connection:** photos reserve their space and arrive without the page jumping.
- **Not found** page that leads back to the branches.

Phone first: the branch page on a phone is the most-used screen. Photographs are sized for the device so a phone never downloads a desktop-sized file. Text meets contrast standards, everything works by keyboard, every photograph has a description, and motion is reduced for visitors who ask their device for that.

## 7. What I need from you

Received so far: the logo, the haruno font, 86 photographs of Chonburi, 26 drink photographs, and address, phone and one day's hours for every branch (from Google Maps).

Still needed:

1. **Opening hours for the whole week.** Google only showed me Thursday's. The prototype shows those hours every day until you confirm.
2. **Photographs of the other six branches.** Even two each (one outside, one inside) fills the map picker. Until then those branches show a marked gap.
3. **Font permission.** The haruno font file says it is copyright IDIN Architects. Please confirm with IDIN that Harudot may use it on a public website.
4. **Photographer credit.** The prototype credits "DOF Sky | Ground", taken from IDIN's site. Please confirm the wording and that the photographs may be used on the website.
5. **Menus:** menu images per branch. Also tell me whether the drink photographs from the "Delivery Menu" folder may be shown as café menu items.
6. **Thai names:** I've written branch names in Thai as "ฮารุดอท ชลบุรี บาย นานา คอฟฟี่ โรสเตอร์". Please confirm the spelling you use.
7. **Korat:** the Drive folder has drawings for a Korat branch. Should the site announce it as coming soon?
8. **Small decisions:** which language a first-time visitor sees (I'd suggest Thai); the email address enquiries go to; who holds the Editor login.
9. **Fact check:** the Chonburi page says the building is by IDIN Architects, completed 2023, 475 sq m, and describes it in a few sentences drawn from IDIN's own project page. Please confirm.

### How to send files

- **Google Drive link:** share one folder as "Anyone with the link: Viewer" and paste the link. Google Drive is reachable from my side, though downloading a large shared folder automatically is not guaranteed to work; if it fails I'll say so.
- **Most reliable:** upload the files into this GitHub repository (Add file, Upload files), in a folder named `assets-from-harudot/`.
- **Small files** such as the logo and font can be attached directly in the chat.

Suggested folder layout: `brand/` (logo, font, colours), then one folder per branch with `photos/` and `menu/` inside, plus one spreadsheet of branch details. Photographs at about 2560 px on the long edge are plenty; camera originals aren't needed.

### Branch positions, from your Google Maps links

| Sheet | Branch | Name on the Google listing | Latitude, longitude | Maps link |
|---|---|---|---|---|
| 01 | Chonburi | Harudot Chonburi by Nana Coffee Roasters | 13.3382709, 100.9653611 | https://maps.app.goo.gl/tfMDVUywMt3NgQyj7 |
| 02 | Khao Yai | Harudot Khaoyai by Nana Coffee Roasters | 14.5311616, 101.5211561 | https://maps.app.goo.gl/jqvHyqru8TGtiHhE7 |
| 03 | Thonburi | Harudot Thonburi by Nana Coffee Roasters | 13.7123617, 100.4334358 | https://maps.app.goo.gl/Wh89DSY2WPgLSxjB6 |
| 04 | Sukhumvit 22 | Harudot by Nana @Sukhumvit 22 | 13.7315914, 100.5649504 | https://maps.app.goo.gl/VjvkwJBBFGWPHsMZA |
| 05 | Sukhumvit 71 | Harudot by Nana @Sukhumvit 71 | 13.7187939, 100.5954712 | https://maps.app.goo.gl/uss15QzoSqTS22e98 |
| 06 | Sathorn | Harudot by Nana Makro Sathon | 13.7097744, 100.5353689 | https://maps.app.goo.gl/Fg4xBNe3HpoC898Y7 |
| 07 | Future Park Rangsit | Harudot by Nana @Future Park Rangsit | 13.9895507, 100.6173983 | https://maps.app.goo.gl/Wm8DbpZGsfmV1LDc8 |

The sheet numbers are a working order, not a ranking; tell me the order you'd like.

## 8. Steps

1. **Gather** (you): items 1 to 4 above, and buy the WordPress.com Personal plan. Design can start as soon as the brand files and a first batch of photos are in hand.
2. **Design** (me): the home page and one branch page at full fidelity with your real photographs, viewable in a browser, for your review.
3. **Build** (me): the WordPress theme, the two content forms, Thai and English, the map, the contact form, on the WordPress.com site before the domain is pointed at it.
4. **Fill and check** (your staff, with a one-page guide from me): branch details, photos, menus; tested on real phones.
5. **Launch:** change the name servers at SiteGround so harudot.com points at the site, register with Google Search Console, link each branch's Google Business Profile to its page.
