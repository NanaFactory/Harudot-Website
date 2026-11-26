/* Harudot prototype: language switch, branch picker, section cut, open-now. */
(() => {
  const root = document.documentElement;
  const branches = (window.HARUDOT && window.HARUDOT.branches) || [];
  const bySlug = Object.fromEntries(branches.map(b => [b.slug, b]));
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Language: both are in the page; remember the choice where storage allows. */
  const setLang = lang => {
    root.dataset.lang = lang; root.lang = lang;
    $$('.lang button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.set === lang)));
    try { localStorage.setItem('harudot-lang', lang); } catch (e) { /* private mode: the page still works */ }
    paintHours();
  };
  $$('.lang button').forEach(b => b.addEventListener('click', () => setLang(b.dataset.set)));

  /* Open now, in Bangkok time whatever the visitor's clock says. */
  const bangkokMinutes = () => {
    const p = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Bangkok', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
    return Number(p.find(x => x.type === 'hour').value) * 60 + Number(p.find(x => x.type === 'minute').value);
  };
  const mins = t => { const [h, m] = t.split(':').map(Number); return h * 60 + m; };
  const status = b => {
    const now = bangkokMinutes(), open = now >= mins(b.open) && now < mins(b.close);
    const th = root.dataset.lang === 'th';
    if (open) return { open, text: th ? `เปิดอยู่ ปิด ${b.close} น.` : `Open now, closes ${b.close}` };
    const later = now < mins(b.open);
    return { open, text: th ? `ปิดแล้ว เปิด${later ? '' : 'พรุ่งนี้'} ${b.open} น.` : `Closed now, opens ${later ? '' : 'tomorrow '}${b.open}` };
  };
  function paintHours() {
    $$('[data-state]').forEach(el => {
      const b = bySlug[el.dataset.state || el.closest('[data-branch]')?.dataset.branch]; if (!b) return;
      const s = status(b); el.dataset.open = String(s.open); $('span', el).textContent = s.text;
    });
    $$('[data-hours]').forEach(el => { const b = bySlug[el.dataset.hours]; if (b) el.textContent = `${b.open} to ${b.close}`.replace(' to ', root.dataset.lang === 'th' ? ' ถึง ' : ' to '); });
  }

  /* Section cut: a real range input sits over the plate, so drag, touch and arrow keys all work. */
  const frame = $('.plate__frame');
  const range = frame && $('input[type="range"]', frame);
  const setCut = v => {
    frame.style.setProperty('--cut', v + '%');
    $('.tag--out', frame).hidden = v < 16; $('.tag--in', frame).hidden = v > 84;
  };
  const sweep = (from, to, ms) => {
    if (reduced) { range.value = to; setCut(to); return; }
    const t0 = performance.now();
    const step = t => {
      const k = Math.min(1, (t - t0) / ms), e = 1 - Math.pow(2, -10 * k);
      const v = from + (to - from) * (k === 1 ? 1 : e);
      range.value = v; setCut(v);
      if (k < 1 && !range.matches(':active')) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if (range) range.addEventListener('input', () => setCut(Number(range.value)));

  /* Picking a branch: map points, index rows and the title block all follow one selection. */
  const picker = $('[data-picker]');
  const img = (n, alt) => ({ src: `assets/img/chonburi/${n}-1280.webp`, srcset: `assets/img/chonburi/${n}-720.webp 720w, assets/img/chonburi/${n}-1280.webp 1280w, assets/img/chonburi/${n}-2000.webp 2000w`, alt });
  function select(slug, animate) {
    const b = bySlug[slug]; if (!b) return;
    $$('.map .pt').forEach(p => p.setAttribute('aria-pressed', String(p.dataset.branch === slug)));
    $$('.index li').forEach(li => li.setAttribute('aria-current', String(li.dataset.branch === slug)));
    if (!picker) return;
    const th = n => $(`[data-f="${n}"]`, picker);
    th('name-en').textContent = b.en; th('name-th').textContent = b.th;
    th('full-en').textContent = `Harudot ${b.en} by Nana Coffee Roasters`;
    th('full-th').textContent = `ฮารุดอท ${b.th} บาย นานา คอฟฟี่ โรสเตอร์`;
    th('area-en').textContent = b.areaEn; th('area-th').textContent = b.areaTh;
    th('phone').textContent = b.phone.replace('+66 ', '0'); th('phone').href = 'tel:' + b.phone.replace(/\s/g, '');
    th('maps').href = b.maps;
    th('state').dataset.state = slug; th('hours').dataset.hours = slug;
    const sheet = th('sheet');
    if (b.sheet) { sheet.href = b.sheet; sheet.removeAttribute('aria-disabled'); sheet.removeAttribute('tabindex'); }
    else { sheet.removeAttribute('href'); sheet.setAttribute('aria-disabled', 'true'); }
    $$('[data-sheet-label]', sheet).forEach(el => { el.hidden = (el.dataset.sheetLabel === 'yes') !== Boolean(b.sheet); });
    const plate = $('.plate');
    plate.dataset.empty = String(!b.outside);
    if (b.outside) {
      Object.assign($('.plate__out', frame), img(b.outside, b.outsideAltEn));
      Object.assign($('.plate__in', frame), img(b.inside, b.insideAltEn));
      if (animate) sweep(0, 58, 700);
    }
    $$('[data-f="credit"]', plate).forEach(el => { el.hidden = !b.outside; });
    paintHours();
    if (animate) history.replaceState(null, '', '#' + slug);
  }
  const stacked = matchMedia('(max-width: 820px)');
  const act = el => {
    const slug = el.dataset.branch || el.closest('[data-branch]').dataset.branch;
    if (!picker) { location.href = 'index.html#' + slug; return; }
    select(slug, true);
    /* From the list, or on a narrow sheet where the plate sits above the map, bring the result into view. */
    if (el.matches('.row__name') || stacked.matches) $('#pick').scrollIntoView({ block: 'start' });
  };
  $$('.map .pt, .row__name').forEach(el => {
    el.addEventListener('click', () => act(el));
    el.addEventListener('keydown', e => { if (el.matches('.pt') && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); act(el); } });
  });

  let saved = null; try { saved = localStorage.getItem('harudot-lang'); } catch (e) { /* ignore */ }
  setLang(saved === 'th' || saved === 'en' ? saved : root.dataset.lang || 'en');
  const first = bySlug[location.hash.slice(1)] ? location.hash.slice(1) : (root.dataset.branch || 'chonburi');
  select(first, false);
  if (range) { setCut(100); const go = () => sweep(100, 58, 1300); const o = $('.plate__out', frame); o.complete ? go() : o.addEventListener('load', go, { once: true }); }
  setInterval(paintHours, 60000);
})();
