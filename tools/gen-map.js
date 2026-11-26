// Draws the branch-picker maps from content/branches.json.
// Usage: node tools/gen-map.js <dir with world-atlas, topojson-client, d3-geo installed> <out dir>
// Output: map-desktop.svg and map-mobile.svg, both with Thai and English names, as inline-ready fragments.
const fs = require('fs'), path = require('path');
const [mods, outDir] = process.argv.slice(2);
const req = m => require(path.join(mods, 'node_modules', m));
const topo = req('topojson-client'), d3 = req('d3-geo');
const atlas = r => JSON.parse(fs.readFileSync(path.join(mods, 'node_modules/world-atlas', `countries-${r}.json`)));
const thailand = r => { const a = atlas(r); return topo.feature(a, a.objects.countries).features.find(f => f.id === '764'); };
const B = JSON.parse(fs.readFileSync(path.join(__dirname, '../content/branches.json'))).branches;
// The enlarged area. Widen it if a branch opens outside these bounds.
const box = [99.72, 12.93, 101.86, 14.82];
const STACK = ['sukhumvit-71', 'sukhumvit-22', 'sathorn', 'thonburi']; // top to bottom, east-most first so leaders never cross
const r1 = v => Math.round(v * 10) / 10;

const both = (en, th, attrs) => `<text ${attrs} data-l="en" lang="en">${en}</text><text ${attrs} data-l="th" lang="th">${th}</text>`;

function build(id, W, H, kw, kh, fs_, keyAt) {
  const pj = d3.geoMercator().fitExtent([[0, 0], [W, H]], { type: 'MultiPoint', coordinates: [[box[0], box[1]], [box[2], box[3]]] }).clipExtent([[-2, -2], [W + 2, H + 2]]);
  const kp = d3.geoMercator().fitExtent([[6, 6], [kw - 6, kh - 16]], thailand('50m'));
  const [kx0, ky1] = kp([box[0], box[1]]), [kx1, ky0] = kp([box[2], box[3]]);
  const pt = Object.fromEntries(B.map(b => [b.slug, pj([b.lng, b.lat]).map(r1)]));
  const km20 = Math.abs(pj([100.5, 13.5])[1] - pj([100.5, 13.5 + 20 / 111.2])[1]);
  const gap = fs_ + 9, lx = 10, top = pt.thonburi[1] - gap * 3 + 4;
  let s = `<svg class="map map-${id}" viewBox="0 0 ${W} ${H}" role="group" aria-label="Map of Harudot branches around Bangkok, Chonburi and Khao Yai"><defs><pattern id="sea-${id}" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 3h6" class="sea-line"/></pattern></defs>`;
  s += `<rect width="${W}" height="${H}" fill="url(#sea-${id})"/><path class="land" d="${d3.geoPath(pj)(thailand('10m'))}"/>`;
  const g = pj([100.72, 13.14]); s += both('GULF OF THAILAND', 'อ่าวไทย', `class="place" x="${r1(g[0])}" y="${r1(g[1])}" text-anchor="middle" font-size="${fs_ - 1}"`);
  s += `<g class="scale" transform="translate(14,${H - 14})"><path d="M0 0h${r1(km20)}M0 -4v8M${r1(km20 / 2)} -3v6M${r1(km20)} -4v8"/>${both('20 km', '20 กม.', `x="0" y="-9" font-size="${fs_ - 1}"`)}</g>`;
  s += `<g class="north" transform="translate(${W - 24},22)"><path d="M0 18V-6m0 0-5 9m5-9 5 9"/><text x="0" y="33" text-anchor="middle" font-size="${fs_ - 1}">N</text></g>`;
  const kxy = keyAt === 'top-left' ? [0, 0] : [W - kw - 1, H - kh - 1];
  s += `<g class="key" transform="translate(${kxy})"><rect x=".5" y=".5" width="${kw}" height="${kh}"/><path d="${d3.geoPath(kp)(thailand('50m'))}"/><rect class="here" x="${r1(kx0)}" y="${r1(ky0)}" width="${r1(kx1 - kx0)}" height="${r1(ky1 - ky0)}"/>${both('THAILAND', 'ประเทศไทย', `x="${kw / 2}" y="${kh - 6}" text-anchor="middle" font-size="${fs_ - 2}"`)}</g>`;
  // Rough advance widths, per language: they size each label's tap row and say where its leader starts.
  const wEn = b => (b.en.length + 3) * fs_ * 0.68;
  const wTh = b => ([...b.th].filter(c => !/[ัิ-ฺ็-๎]/.test(c)).length + 3) * fs_ * 0.6;
  for (const b of B) {
    const [x, y] = pt[b.slug]; let tx, ty, anchor = 'start';
    const si = STACK.indexOf(b.slug);
    if (si >= 0) { tx = lx; ty = top + gap * si; }
    else if (b.slug === 'khao-yai') { tx = x - 12; ty = y + 4; anchor = 'end'; }
    else if (b.slug === 'future-park-rangsit') { tx = x + 14; ty = y - 12; }
    else { tx = x + 14; ty = y + 4; }
    s += `<g class="pt" data-branch="${b.slug}" role="button" tabindex="0" aria-pressed="false" aria-label="Harudot ${b.en}">`;
    // One leader and one tap row per language, so neither is sized for the other's text.
    for (const [l, w] of [['en', wEn(b)], ['th', wTh(b)]]) {
      let lead = '';
      if (si >= 0) { const ex = tx + w + 6; lead = `M${r1(ex)} ${r1(ty - 4)}H${r1(Math.max(ex + 4, x - Math.abs(y - (ty - 4))))}L${x} ${y}`; }
      else if (b.slug === 'future-park-rangsit') lead = `M${x} ${y}L${r1(tx - 3)} ${r1(ty + 2)}`;
      if (lead) s += `<path class="lead" pathLength="1" data-l="${l}" d="${lead}"/>`;
      let hx = anchor === 'end' ? tx - w - 4 : tx - 4, hw = w + 8;
      if (si < 0 && Math.abs(ty - 4 - y) < 3) { const x0 = Math.min(hx, x - 9), x1 = Math.max(hx + hw, x + 9); hx = x0; hw = x1 - x0; }
      s += `<rect class="hit" data-l="${l}" x="${r1(hx)}" y="${r1(ty - fs_ - 3)}" width="${r1(hw)}" height="${r1(fs_ + 9)}"/>`;
    }
    s += `<circle class="hit-dot" cx="${x}" cy="${y}" r="8"/><circle class="dot" cx="${x}" cy="${y}" r="4"/>`;
    s += both(`<tspan class="n">${b.n}</tspan> ${b.en.toUpperCase()}`, `<tspan class="n">${b.n}</tspan> ${b.th}`, `x="${r1(tx)}" y="${r1(ty)}" text-anchor="${anchor}" font-size="${fs_}"`) + '</g>';
  }
  return s + '</svg>';
}
fs.writeFileSync(path.join(outDir, 'map-desktop.svg'), build('d', 452, 440, 92, 168, 10.5, 'bottom-right'));
fs.writeFileSync(path.join(outDir, 'map-mobile.svg'), build('m', 358, 330, 64, 118, 10, 'top-left'));
