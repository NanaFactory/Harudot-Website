// Draws the branch-picker maps from content/branches.json.
// Usage: node tools/gen-map.js <dir with world-atlas, topojson-client, d3-geo installed> <out dir>
// Output: map-desktop.svg (names on the map) and map-mobile.svg (numbers only), as inline-ready fragments.
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

function build(id, W, H, kw, kh, fs_, names) {
  const pj = d3.geoMercator().fitExtent([[0, 0], [W, H]], { type: 'MultiPoint', coordinates: [[box[0], box[1]], [box[2], box[3]]] }).clipExtent([[-2, -2], [W + 2, H + 2]]);
  const kp = d3.geoMercator().fitExtent([[6, 6], [kw - 6, kh - 16]], thailand('50m'));
  const [kx0, ky1] = kp([box[0], box[1]]), [kx1, ky0] = kp([box[2], box[3]]);
  const pt = Object.fromEntries(B.map(b => [b.slug, pj([b.lng, b.lat]).map(r1)]));
  const km20 = Math.abs(pj([100.5, 13.5])[1] - pj([100.5, 13.5 + 20 / 111.2])[1]);
  const gap = fs_ + (names ? 9 : 10), lx = 10, top = pt.thonburi[1] - gap * 3 + 4;
  const label = b => names ? `<tspan class="n">${b.n}</tspan> ${b.en.toUpperCase()}` : b.n;
  const tw = b => (names ? (b.en.length + 3) * fs_ * 0.68 : fs_ * 1.5);
  let s = `<svg class="map map-${id}" viewBox="0 0 ${W} ${H}" role="group" aria-label="Map of Harudot branches around Bangkok, Chonburi and Khao Yai"><defs><pattern id="sea-${id}" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 3h6" class="sea-line"/></pattern></defs>`;
  s += `<rect width="${W}" height="${H}" fill="url(#sea-${id})"/><path class="land" d="${d3.geoPath(pj)(thailand('10m'))}"/>`;
  const g = pj([100.72, 13.14]); s += `<text class="place" x="${r1(g[0])}" y="${r1(g[1])}" text-anchor="middle" font-size="${fs_ - 1}">GULF OF THAILAND</text>`;
  s += `<g class="scale" transform="translate(14,${H - 14})"><path d="M0 0h${r1(km20)}M0 -4v8M${r1(km20 / 2)} -3v6M${r1(km20)} -4v8"/><text x="0" y="-9" font-size="${fs_ - 1}">20 km</text></g>`;
  s += `<g class="north" transform="translate(${W - 24},22)"><path d="M0 18V-6m0 0-5 9m5-9 5 9"/><text x="0" y="33" text-anchor="middle" font-size="${fs_ - 1}">N</text></g>`;
  s += `<g class="key" transform="translate(${W - kw - 1},${H - kh - 1})"><rect x=".5" y=".5" width="${kw}" height="${kh}"/><path d="${d3.geoPath(kp)(thailand('50m'))}"/><rect class="here" x="${r1(kx0)}" y="${r1(ky0)}" width="${r1(kx1 - kx0)}" height="${r1(ky1 - ky0)}"/><text x="${kw / 2}" y="${kh - 6}" text-anchor="middle" font-size="${fs_ - 2}">THAILAND</text></g>`;
  for (const b of B) {
    const [x, y] = pt[b.slug]; let tx, ty, anchor = 'start', lead = '';
    const si = STACK.indexOf(b.slug);
    if (si >= 0) { tx = lx; ty = top + gap * si; const ex = tx + tw(b) + 6; lead = `M${r1(ex)} ${r1(ty - 4)}H${r1(Math.max(ex + 4, x - Math.abs(y - (ty - 4))))}L${x} ${y}`; }
    else if (b.slug === 'khao-yai') { tx = x - 12; ty = y + 4; anchor = 'end'; }
    else if (b.slug === 'future-park-rangsit') { tx = x + 14; ty = y - 12; lead = `M${x} ${y}L${r1(tx - 3)} ${r1(ty + 2)}`; }
    else { tx = x + 14; ty = y + 4; }
    const w = tw(b), hx = anchor === 'end' ? tx - w : Math.min(tx, x) - 6, hw = anchor === 'end' ? w + 24 : Math.max(tx + w, x) - Math.min(tx, x) + 12;
    s += `<g class="pt" data-branch="${b.slug}" role="button" tabindex="0" aria-pressed="false" aria-label="Harudot ${b.en}">`;
    if (lead) s += `<path class="lead" d="${lead}"/>`;
    s += `<rect class="hit" x="${r1(si >= 0 ? tx - 4 : hx)}" y="${r1(Math.min(ty, y) - gap / 2 - 4)}" width="${r1(si >= 0 ? w + 12 : hw)}" height="${r1(Math.abs(ty - y) + gap + 4)}"/>`;
    s += `<circle class="dot" cx="${x}" cy="${y}" r="4"/><text x="${r1(tx)}" y="${r1(ty)}" text-anchor="${anchor}" font-size="${fs_}">${label(b)}</text></g>`;
  }
  return s + '</svg>';
}
fs.writeFileSync(path.join(outDir, 'map-desktop.svg'), build('d', 452, 440, 92, 168, 10.5, true));
fs.writeFileSync(path.join(outDir, 'map-mobile.svg'), build('m', 358, 330, 72, 134, 11, false));
