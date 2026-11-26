---
name: Harudot by Nana Coffee Roasters
description: The drawing set of the cafés. Paper, one line, one fill; photographs as plates.
colors:
  clay: "oklch(0.77 0.068 40)"
  clay-deep: "oklch(0.69 0.085 40)"
  clay-wash: "oklch(0.9 0.03 40)"
  paper: "oklch(0.962 0.004 220)"
  ink: "oklch(0.2 0.008 240)"
  ink-2: "oklch(0.4 0.012 240)"
typography:
  display:
    fontFamily: "haruno, Bai Jamjuree, Noto Sans Thai, sans-serif"
    fontSize: "clamp(3.5rem, 12vw, 6rem)"
    fontWeight: 300
    lineHeight: 0.95
    letterSpacing: "0.01em"
  headline:
    fontFamily: "haruno, Bai Jamjuree, Noto Sans Thai, sans-serif"
    fontSize: "clamp(2.25rem, 5vw, 3.75rem)"
    fontWeight: 300
    lineHeight: 1
  title:
    fontFamily: "haruno, Bai Jamjuree, Noto Sans Thai, sans-serif"
    fontSize: "clamp(1.75rem, 3.2vw, 2.5rem)"
    fontWeight: 300
    lineHeight: 1.1
  body:
    fontFamily: "Bai Jamjuree, Noto Sans Thai, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
  value:
    fontFamily: "Bai Jamjuree, Noto Sans Thai, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 500
    lineHeight: 1.4
  label:
    fontFamily: "Bai Jamjuree, Noto Sans Thai, system-ui, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0.12em"
  control:
    fontFamily: "Bai Jamjuree, Noto Sans Thai, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 600
    letterSpacing: "0.1em"
rounded:
  none: "0px"
  mark: "50%"
spacing:
  margin: "clamp(16px, 3.2vw, 44px)"
  gutter: "clamp(20px, 2.6vw, 36px)"
  section: "clamp(64px, 9vw, 128px)"
  cell: "0.8rem 1rem"
  head: "20px"
components:
  button:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.control}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.15rem"
    height: "3rem"
  button-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  button-primary:
    backgroundColor: "{colors.clay}"
    textColor: "{colors.ink}"
    typography: "{typography.control}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.15rem"
    height: "3rem"
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  button-disabled:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink-2}"
  language-switch:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: "2.5rem"
  language-switch-pressed:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  title-block-cell:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.value}"
    rounded: "{rounded.none}"
    padding: "0.8rem 1rem"
  branch-row:
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    padding: "1.05rem 0.9rem"
  branch-row-current:
    backgroundColor: "{colors.clay-wash}"
  chip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "0.15rem 0.5rem"
  void:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: "12rem"
---

# Design System: Harudot by Nana Coffee Roasters

## Overview

**Creative North Star: "The Drawing Set"**

The site is the drawing set of the cafés. Each branch is a sheet, a photograph is a plate on that sheet, and facts sit in ruled title blocks the way a drawing's own title block holds its scale and date. The ground is a cool drafting-film white, everything drawn or ruled is one black line, and a single clay fill marks what the drawing has cut through or picked out.

The system is quiet so the buildings are not. Photographs carry all the colour and all the warmth; the interface around them is line, lettering and paper. Density is that of a well-kept sheet: generous margins, facts packed tight inside their cells, long clear runs between sections. Depth comes from overlap only. There are no shadows, no colour blends, no softened corners and no glass.

Two languages share every page with equal weight. haruno, the brand's own monoline face, letters the names; Bai Jamjuree sets everything else in Thai and English, in its light weight wherever it has to stand beside haruno's hairline. Controls are worded for a café visitor (Directions, View branch, Drag the cut), never in drawing-office terms.

**Key Characteristics:**
- Paper, one ink, one fill: cool white ground, black line, clay pink.
- Two line weights (1px drawn, 3px ground and section heads) plus one dashed cut line.
- Facts live in ruled title-block cells, not cards.
- Photographs are plates shown whole; only the section-cut plate joins two in one frame.
- A crossed rectangle is the only stand-in for anything not yet supplied.
- Square corners everywhere; circles only where a drawing uses them (section marks, points, state dots).
- Lines draw and plates wipe along the cut; nothing fades up or floats.
- Thai and English as [data-l] pairs, one shown at a time.

## Colors

A drafting sheet: cool white film, black line, and one clay pink used the way a section drawing fills what it cuts.

### Primary
- **Section Clay** (`clay`): the one fill. The selected branch on the map and in the key plan, and the Directions action. It is always paired with ink text and an ink edge, never with paper text.
- **Hatch Clay** (`clay-deep`): the same clay a step darker, for linework only, where the lighter fill would vanish at 1.5px: the diagonal hatch under the ground line, and the underline that appears under a branch name on hover.
- **Clay Wash** (`clay-wash`): clay let down almost to paper, for transient and secondary states: hover on a map point, on the pager and on the unpressed language button; the row of the selected branch in the list; the tone behind a plate while its photograph loads.

### Neutral
- **Drafting Film** (`paper`): the ground of every sheet, and the fill of anything that sits in front of something else (tags on a plate, section marks, the statement on a crossed rectangle).
- **Drawing Ink** (`ink`): all text, every rule and border, map linework and points, the pressed language button, the chip, and the hover state of every button.
- **Faded Ink** (`ink-2`): small lettering and secondary text only: cell labels, row numbers, place names on the map, notes, and the dashed rule between phone numbers.

### Named Rules
**The One Fill Rule.** Clay is the drawing's only fill and it has three jobs: the hatch under the ground line, the selected branch, and the primary action (Directions). If a fourth use is proposed, it is wrong; use ink or paper.

**The Photographs Carry Colour Rule.** No colour enters the interface that is not paper, ink or clay. Warmth, wood, sky and grass arrive in the plates and nowhere else.

As built, clay also appears on the cut's drag handle and as the open-now dot. Both sit on the section cut and the selected branch's own facts; they are not a licence for further uses.

## Typography

**Display Font:** haruno (falling back to Bai Jamjuree, Noto Sans Thai, sans-serif)
**Body Font:** Bai Jamjuree (falling back to Noto Sans Thai, system-ui, sans-serif)

**Character:** haruno is the brand's own lowercase monoline face, drawn by the cafés' architects; it letters names the way a hand letters a drawing. Bai Jamjuree is a technical, slightly squared Thai and Latin family that reads as drafting lettering at small sizes and thins to match haruno at weight 300. haruno covers Latin letters and punctuation only (unicode-range U+0020-002F and U+003A-007E), so its numerals and all Thai fall through to Bai Jamjuree by design.

### Hierarchy
- **Display** (300, clamp(3.5rem, 12vw, 6rem), 0.95): the branch name at the head of its sheet. Lowercase, haruno. Thai at 0.8em, line-height 1.3.
- **Headline** (300, clamp(2.25rem, 5vw, 3.75rem), 1): section heads, sitting on a 3px ink rule. The statement in About runs at clamp(2rem, 4.4vw, 3.5rem), 1.12, balanced.
- **Title** (300, clamp(1.75rem, 3.2vw, 2.5rem), 1.1): branch names in the list and story headings; 1.75rem in title-block cells and the pager; 1.25rem under drink photographs.
- **Body** (400, 1rem, 1.55): running text, capped at 62ch. Thai body takes line-height 1.7. Secondary text steps to 0.9375rem and 0.875rem.
- **Value** (500, 1rem, 1.4): the fact inside a title-block cell. An address stands at 1.25rem, 1.45, capped at 30ch.
- **Label** (500, 0.75rem, 0.12em, uppercase, Faded Ink): the lettering above a fact. Thai: 0.8125rem at 0.02em.
- **Control** (600, 0.8125rem, 0.1em, uppercase): buttons and navigation (navigation at 500). Thai: 0.9375rem at 0.02em. Tags on a plate and chips use the same lettering at 0.6875rem.

### Named Rules
**The Hairline Rule.** Whatever stands beside haruno matches its hairline. Thai names, and digits inside names (wrapped in the numeral span at 0.82em), are set in Bai Jamjuree 300; haruno's own numerals are excluded by unicode-range because they are hard to read.

**The Lettering Rule.** Tracked uppercase lettering is for facts and controls only: cell labels, buttons, navigation, map text. It never sits above a heading as decoration, and Thai lettering drops the tracking (0.01 to 0.02em) and steps up one size instead.

## Layout

One sheet, 1520px at its widest, centred, with a fluid sheet margin (`margin`) and a fluid gutter (`gutter`). Sections are separated by a long clear run (`section`), and each opens with a head on a 3px rule followed by 28px before its content.

The sheet top is a two-column composition: the plate takes the remaining width and the map picker a third (never under 340px), stretched to equal height. Beneath both runs the ground line, then the title block. Branch-sheet photographs sit on a 12-column grid in spans of 4, 5, 6, 7, 8 and 12, aligned to their bottom edges with a large row gap (clamp(40px, 6vw, 88px)), so the page reads as a sequence of differently sized plates rather than a uniform gallery. Paired text blocks (about, story, location) use two unequal columns with a wide column gap (clamp(32px, 6vw, 96px)).

Three breakpoints, each a re-composition: at 1100px title blocks fall to two columns and list rows drop their actions to a second line; at 820px the sheet top stacks and text pairs become one column; at 600px the navigation takes its own full-width line under the logo, the map swaps to a drawing made for the narrow sheet, and a list row's actions span the full row width and share it equally.

### Named Rules
**The Ground Line Rule.** Everything above stands on the ground line: a 3px ink rule over a 22px band of clay hatch at 135 degrees, bled to the sheet edge. One per sheet top, directly under the plate, with the title block beneath it.

**The Re-compose Rule.** Narrow sheets re-compose; nothing just shrinks. Below 820px the order becomes plate, ground line, title block, map, so Directions stays in the first viewport.

## Elevation & Depth

Flat. There is no shadow anywhere in the system. Where one thing sits in front of another (a tag on a photograph, a section mark on the cut line, a statement on a crossed rectangle, map lettering over linework) it is given a paper fill, and usually a 1px ink edge, and simply covers what is behind it.

### Named Rules
**The Overlap Rule.** Depth is overlap and nothing else. A thing in front is a paper-filled, ink-ruled shape sitting on what is behind it. No box-shadow, no blur, no translucency.

## Shapes

Square. Every container, button, cell and image has a 0 radius. The only curves are full circles used as a drawing uses them: the 30px section marks at each end of the cut line, the points on the map, and the 0.6rem state dot beside the hours.

Line is the form language. A fine rule (1px solid ink) draws everything: cell edges, list dividers, captions, the map frame. A heavy rule (3px solid ink) is reserved for the ground line and section heads. Dashes mean something specific each time: the 2px dashed cut line, a dashed border on an action that is not yet available, a dashed rule between lines of a list inside one cell. Title blocks are grids whose cells carry their own right and bottom rules, with the block clipping the outer pair, so any number of cells closes cleanly.

Two hard-edged line patterns exist and no others: the 135 degree hatch (1.5px line, 9px pitch) and the corner-to-corner cross of a plate not yet supplied.

### Named Rules
**The Whole Plate Rule.** A photograph is shown whole, at its own proportions, with a ruled caption beneath. The section-cut plate is the single exception, where two photographs share one frame and are cropped to it.

## Components

### Buttons
Plain, ruled, and certain: a lettered rectangle that inverts.
- **Shape:** square (0 radius), 1px ink border, at least 3rem tall, padding 0.7rem 1.15rem, with an optional 1rem line icon after the lettering. The lettering never wraps. Inside list rows: 2.75rem tall.
- **Default:** paper fill, ink lettering.
- **Primary:** clay fill, ink lettering. Directions only. In the list, Directions takes the clay fill only on the selected branch's row.
- **Hover / Focus:** fill becomes ink and lettering paper over 0.18s on the system ease (cubic-bezier(0.16, 1, 0.3, 1)); pressing moves it down 1px. Focus is a 2px ink outline offset 3px, as on every focusable thing.
- **Unavailable:** dashed border, Faded Ink lettering, no icon, not clickable; the wording says what is coming.
- **In a title block:** the button loses its own border and fills its cell edge to edge.

### Language switch
Two joined square cells in a 1px ink frame, each at least 3rem by 2.5rem. The language in use is ink-filled with paper lettering; the other shows Clay Wash on hover.

### Navigation
Uppercase lettering links (0.8125rem, 500, 0.1em) in a masthead closed by a fine rule: logo left (168px), links centre, language switch right. Hover and the current page are a 2px ink underline at the bottom of the link. At 600px the links spread across their own line below the logo.

### Title block
The container for facts, in place of a card. A 1px ink frame divided into ruled cells (padding 0.8rem 1rem); each cell holds a Label above a Value. A branch name in a cell is set at weight 300, so Thai names and numerals there match haruno. Action cells have no padding and are filled by their button. Used for the selected branch (name, today's hours and state, area, phone, Directions, View branch), for a branch's facts (four columns), and for the foot of every sheet.

### Open-now state
A 0.6rem ink-ringed circle beside a plain sentence ("Open now, closes 18:00"). The circle is filled clay when open and left empty when closed; the sentence always carries the meaning.

### Branch list row
A ruled row: tabular number in Faded Ink, the name in Title type as a button that selects the branch on the map, area, hours and state, then actions at the right. Rows are divided by fine rules. Hovering the name underlines it 2px in Hatch Clay; the selected branch's row takes Clay Wash.

### Plate and caption
A whole photograph at full column width with a caption below it on a fine rule (0.9375rem), description left and Label-set credit right. A plate may bleed to the sheet edge; its caption stays inside the margin.

### Section-cut plate (signature)
Two photographs of the selected branch, outside and inside, share one frame and meet at a 2px dashed ink line that overhangs the frame by 20px at each end and carries a circled A mark at top and bottom. A clay, ink-ruled handle sits on the line at mid-height ("Drag the cut", arrows either side; arrows only at 600px). An invisible range input covers the frame, so drag, touch and arrow keys all move the cut. Paper-backed tags name each side (Outside, Inside) at the bottom corners. Selecting a branch sweeps the cut from 0 to its rest position at 58% over 700ms; with reduced motion it does not move. If the branch has no photographs the frame becomes a crossed rectangle carrying the branch name.

### Map picker
A paper drawing in a 1px ink frame: coastline in fine line, sea as faint horizontal ruling, a point per branch with a numbered, lettered name on a leader line, a scale bar, a north arrow and a key plan of the country. Each point is a button. Hover washes its label in Clay Wash; the selected branch gets a clay label, a larger clay point ringed in ink, bolder lettering and a heavier leader. Each label has one tap row and one leader per language, sized from that language's text. Leaders draw once on load (0.9s, system ease, no delay); the drawn line is the resting state, so a leader is never left invisible. A separate drawing serves sheets under 600px.

### Crossed rectangle
The stand-in for anything not yet supplied: 1px ink frame, two 1px diagonals, at least 12rem tall, with a paper-backed, ink-ruled statement in Control lettering at its centre ("Photographs to come"). In the section-cut frame it also carries the branch name in haruno.

### Chip
A small ink-filled, paper-lettered square-cornered marker (0.6875rem, 600, 0.1em, uppercase). In the build it flags sample promotions and the review notes; it has no launch-content use yet.

### Pager
Previous and next branch as two equal cells in one ink frame, divided by a fine rule, each a Label over the branch name at 1.75rem; hover is Clay Wash.

### Two languages
Every visible string is written twice, as a Thai and an English element carrying the language attribute, and the root element's language setting shows one and hides the other. Nothing is translated at run time, so both languages must be designed and checked.

### Named Rules
**The Crossed Rectangle Rule.** A missing photograph or a block not yet supplied is shown one way only: an ink-ruled rectangle crossed corner to corner, with a plain paper-backed statement of what is to come. Never a grey box, a stock image or a blurred stand-in.

## Do's and Don'ts

### Do:
- **Do** build every surface from the three materials only: paper ground, ink line, clay fill, all taken from the tokens.
- **Do** hold facts (hours, phone, address, area) in ruled title-block cells with a small tracked label above each value.
- **Do** give Directions the clay fill, and only Directions; every other action is the paper button that inverts to ink on hover.
- **Do** show photographs whole at their own proportions, with a 1px-ruled caption and the photographer's credit.
- **Do** mark anything not yet supplied with the crossed rectangle and a plain statement, and give an unavailable action a dashed border.
- **Do** write every visible string as a Thai and English pair, and set Thai display text in Bai Jamjuree 300 at the reduced sizes the build uses (about 0.8 to 0.86 of the Latin size, line-height 1.3 to 1.4).
- **Do** wrap digits inside a haruno-set name in the numeral span so they fall to Bai Jamjuree 300.
- **Do** keep controls at least 2.5rem tall (3rem for buttons) and keep the 2px ink focus outline with its 3px offset.
- **Do** word controls for a café visitor: Directions, View branch, Drag the cut.
- **Do** honour reduced motion: the cut does not sweep, leaders do not draw, scrolling does not glide.

### Don't:
- **Don't** add a shadow, a blur, a translucent layer or a colour blend. The hatch and the crossed rectangle are hard-edged line patterns, not gradients, and they are the only patterned fills.
- **Don't** round a corner. The only curves are full circles a drawing would use: section marks, map points, the open-now dot.
- **Don't** give clay a fourth job, and don't introduce a second accent colour.
- **Don't** crop a photograph to a card ratio or lay text over it. The section-cut plate and the square drink thumbnails are the only cropped frames.
- **Don't** set numerals in haruno, and don't set Thai in a regular or bold weight beside it.
- **Don't** track Thai lettering or force it to uppercase rhythm; it takes 0.01 to 0.02em and the next size up.
- **Don't** stand in for missing material with a stock photograph, a grey placeholder or invented copy.
- **Don't** fade things up, float them, or animate on scroll. Lines draw once; plates wipe along the cut.
- **Don't** ship the "To confirm" review notes; they are for the owner's review and leave before launch.
- **Don't** use drawing-office jargon in anything a visitor reads or taps.
