# Harudot website plan

Plan for harudot.com, the first website for Harudot by Nana Coffee Roasters. Written 2026-11-26. Product facts and their sources are in [`PRODUCT.md`](../PRODUCT.md); this file is the plan built on them. Nothing has been built yet.

**Status:** everything below is settled except the visual direction (section 3), which is waiting on your choice between three sketches.

## 1. What the site is for

A visitor arrives, usually on a phone, having seen a Harudot building somewhere. They want to see the place properly, find out which branch is near them, check the menu and what's on, and get there. A smaller group wants to ask about private events, photo shoots, press or collaborations.

So the site succeeds when:

- a visitor sees large, real photographs of a branch within a second or two of arriving;
- from any page, the hours and directions for any branch are one tap away;
- an enquiry reaches your team;
- your staff can change a menu or promotion in both languages without calling anyone.

It is not a shop, not a delivery portal and not a blog.

## 2. Platform: WordPress on SiteGround

**Recommendation: WordPress, on your SiteGround account, with a small theme written specifically for Harudot.** Staff will change menus and promotions every month in Thai and English, and WordPress gives them a familiar admin screen for that at no extra cost.

One correction to the starting assumption: WordPress itself is free, but it needs **hosting**, and a domain alone doesn't include that. Two things to check in your SiteGround account:

| If your SiteGround account has… | Then |
|---|---|
| A hosting plan that allows more than one website (GrowBig or GoGeek, as I understand their plans; please confirm in the account) | Add harudot.com as a new site on it. Extra cost: none. |
| A hosting plan limited to one website, already used by another site | Either upgrade the plan or use the alternative below. |
| Only the domain registration, no hosting | A hosting plan is needed. Check the renewal price, not the first-year offer; it is usually several times higher. |

Today harudot.com has no DNS record at all, so nothing is live at the address and nothing will be disrupted by launching.

**How it's built, and why not an off-the-shelf theme.** The reference site runs WordPress with a paid multipurpose theme and a slider plugin. That route is quick but heavy: slow on phones, and staff end up editing inside a page-builder where it is easy to break the layout. Instead:

- a hand-written theme held in this repository, installed by uploading a zip in the WordPress admin;
- two content types staff fill in as simple forms: **Branch** and **Promotion** (fields in section 5);
- free plugins only, kept to a short list: a translation plugin for Thai and English, a custom-fields plugin, a contact-form plugin, and SiteGround's own speed and security plugins. Exact picks are made at build time and none carries a subscription.

**Alternative if hosting turns out to cost extra:** a static site on a free host (for example Cloudflare Pages) with a free editing screen layered on top. Hosting is then free, and the site is faster and has almost nothing to maintain. The trade-off is that the staff editing screen is plainer and bilingual editing is clumsier. I'd only choose it if you'd otherwise be paying for a new hosting plan.

### Running costs

| Item | Cost |
|---|---|
| Domain harudot.com | Already owned; yearly renewal continues |
| Hosting | Nothing extra if your current SiteGround plan allows another site; otherwise the plan price |
| WordPress, theme, plugins | Free |
| Maps | Free (links to Google Maps, no paid map service) |
| Enquiry email | Free (mailbox included with SiteGround hosting) |
| Fonts | Free web fonts; Harudot's own signage font only if you hold a licence that covers websites |
| Photographs | Whatever your photographers require for web use and credit |

## 3. Visual direction: your choice needed

Three sketches are in [`docs/sketches/`](sketches/). Each shows the home page on a desktop and a branch page on a phone. The photos in them are free stand-ins of other buildings, and hours and addresses are samples.

Whichever you choose, these stay fixed, because they are what you liked in the reference:

- photographs are large and shown whole, never cropped into shapes or covered with text blocks;
- very little interface; a light page; photographer and architect credited;
- Thai and English given equal weight.

| | What surrounds the photos | What it needs from you | Honest risk |
|---|---|---|---|
| **A. Drawn to scale** ([sketch](sketches/direction-a.jpg)) | An architect's drawing set. Pale paper, black line, one clay-pink fill taken from the Khao Yai concrete. Each branch is a numbered sheet with a "title block" holding address, hours and credits, and a drawn location plan. On the home page you drag a cut line across the photo to pass from outside the building to inside. | One exterior and one interior photo per branch for the cut. Optional: a simple plan or section from the architects for the flagship cafés. | Drawing language can feel technical to someone who just wants a coffee. |
| **B. Seven dots** ([sketch](sketches/direction-b.jpg)) | Harudot's own floor. Terrazzo ground, brass rings, one dot per branch along the foot of a full-width photo; round "inlay" buttons lead to Menu, Promotions and Directions, the way words are set into the café floors. A dot opens to reveal that branch. | Your real signage font and logo files, with a licence for web use. The lettering in the sketch is a stand-in. | The most expected answer for a brand named "dot", and dot motifs turn cute quickly. |
| **C. Like the reference** ([sketch](sketches/direction-c.jpg)) | The architecture-studio standard, done well: full-screen slideshow, small uppercase navigation, edge-to-edge photo mosaic, plain facts table. | Nothing beyond the photos. | Looks like many architecture-studio sites, including IDIN's own, and carries the least of Harudot's character. Fastest and cheapest to build. |

My view: B if you can supply the real signage font and logo, because then the site is unmistakably Harudot's; A if you can't, because it needs nothing but photographs to feel particular. C is a sound choice if speed matters most. Mixing is possible (for example C's home page with A's branch page); say so and I'll sketch it.

## 4. Pages

| Page | What's on it |
|---|---|
| **Home** | Photographs lead. All seven branches reachable without scrolling far. A short line on what Harudot is. Current promotions, if any. |
| **Branches** | All branches at a glance: photo, area, "open now" or today's hours. Grouped as Bangkok and beyond Bangkok once that's useful. |
| **Branch** (one per branch) | Photo sequence; address, hours, phone, parking; a Directions button that opens Google Maps; the menu; current promotions at this branch; the story of the building where there is one; architect and photographer credits. |
| **Promotions** | Everything currently running, filterable by branch. |
| **About** | The Harudot name and idea, the relationship to Nana Coffee Roasters, a link to Nana for buying beans. |
| **Contact** | Enquiry form with a topic (private event, photo shoot, press, collaboration, other) and a branch selector; branch phone numbers listed beside it. |
| **Privacy** | Required because the form collects personal details (Thailand's PDPA). |

Every page exists in Thai and English with a language switch that stays on the same page.

### Recommended additions

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
- Address, Google Maps link, phone, parking note
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

In rough order of how much each one unblocks:

1. **Your direction choice:** A, B, C or a mix.
2. **SiteGround:** the name of your hosting plan, and whether another site already uses it.
3. **Brand files:** logo, the signage font (and whether its licence covers websites), brand colours, any written brand rules.
4. **Photographs:** which branches have professional sets, the files, and each photographer's permission and credit line. The two flagship sets on IDIN's site are credited to DOF Sky | Ground.
5. **Branch details for all seven:** address, hours, phone, Google Maps link, parking, in Thai and English. A spreadsheet is ideal.
6. **Menus:** current menu images per branch.
7. **Small decisions:** which language a first-time visitor sees (I'd suggest Thai, with English one tap away); the email address enquiries go to; who holds the Editor login.
8. **Fact check:** `PRODUCT.md` records what IDIN's site says about Chonburi and Khao Yai (areas, years, awards, the "38%" low-carbon concrete figure). Please confirm these before they're published, and tell me who designed the other five branches.

## 8. Steps

1. **Gather** (you): items 2 to 6 above. Design can start as soon as the direction and a first batch of photos are in hand.
2. **Design** (me): the home page and one branch page at full fidelity with your real photographs, viewable in a browser, for your review.
3. **Build** (me): the WordPress theme, the two content forms, Thai and English, the contact form, on a private preview address.
4. **Fill and check** (your staff, with a one-page guide from me): branch details, photos, menus; tested on real phones.
5. **Launch:** point harudot.com at the site, switch on the security certificate, register with Google Search Console, link each branch's Google Business Profile to its page.
