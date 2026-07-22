/**
 * quiz-widget.mjs — MyST anywidget for interactive quiz / concept-check questions.
 *
 * Model keys:
 *   question    {string}   Question text (plain or with $math$)
 *   choices     {Array}    [{text, correct, feedback}]
 *   multi       {boolean}  true = checkboxes, false = radio
 *   hint        {string}   Optional hint text
 *   explanation {string}   Optional explanation shown after submission
 */

// ── Inline renderers ──────────────────────────────────────────────────────────

function esc(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function renderInline(text) {
  let html = esc(text);
  html = html.replace(/`([^`]+)`/g, (_, c) =>
    `<code class="q-code">${c}</code>`
  );
  html = html.replace(/\$([^$]+)\$/g, (_, m) =>
    `<em style="font-style:italic">${m}</em>`
  );
  return html;
}

function renderChoice(text) {
  const fence = text.match(/^```(\w*)\n([\s\S]*)\n```$/);
  if (fence) {
    const lang = esc(fence[1]);
    const code = esc(fence[2]);
    return `<pre class="q-pre"><code${lang ? ` class="language-${lang}"` : ''}>${code}</code></pre>`;
  }
  return renderInline(text);
}

// ── Styles ────────────────────────────────────────────────────────────────────

const CSS = `
:host { display: block; font-family: inherit; font-size: 1rem; margin: 1.5em 0; }
.quiz {
  border: 1px solid #bae6fd;
  border-left: 4px solid #0284c7;
  border-radius: 4px;
  background: #f0f9ff;
  overflow: hidden;
}
.quiz-hdr {
  display: flex; align-items: center; gap: 8px;
  padding: 9px 14px;
  background: #e0f2fe;
  border-bottom: 1px solid #bae6fd;
  font-weight: 600; font-size: .92em; color: #0369a1;
}
.quiz-hdr svg { flex-shrink: 0; }
.quiz-body { padding: 14px 16px 16px; }
.question { font-weight: 500; line-height: 1.55; margin: 0 0 10px; }
.multinote { font-size: .83em; color: #64748b; font-style: italic; margin: -4px 0 8px; }
.choices { display: flex; flex-direction: column; gap: 6px; margin-bottom: 12px; }

/* Choice row — wraps input + content + feedback pill */
.choice-wrap { display: flex; flex-direction: column; }
.choice {
  display: flex; align-items: flex-start; gap: 8px;
  padding: 8px 10px; border-radius: 4px;
  border: 1px solid #cbd5e1; background: #fff;
  cursor: pointer; font-size: .93em; line-height: 1.5;
  transition: border-color .12s, background .12s;
  user-select: none;
}
.choice:hover { border-color: #0284c7; background: #f0f9ff; }
.choice input { margin-top: 2px; accent-color: #0284c7; flex-shrink: 0; cursor: pointer; }
.choice-text { flex: 1; }

/* Inline code + code fences inside questions/choices */
.q-code {
  background: #e2e8f0; color: #0f172a;
  border-radius: 3px; padding: 1px 4px;
  font-size: .88em; font-family: ui-monospace, monospace;
}
.q-pre {
  margin: 4px 0 0; padding: 7px 10px; border-radius: 3px;
  background: #f1f5f9; color: #0f172a;
  font-size: .82em; font-family: ui-monospace, monospace;
  overflow-x: auto; white-space: pre; line-height: 1.5;
}

/* Per-choice feedback shown beneath the choice after submission */
.choice-feedback {
  display: none;
  margin: 3px 0 0 2px;
  padding: 5px 10px;
  border-radius: 0 0 4px 4px;
  font-size: .86em;
  line-height: 1.45;
  border-left: 3px solid #94a3b8;
  background: #f8fafc;
  color: #475569;
}
.choice-feedback.visible { display: block; }
.choice-feedback.fb-correct {
  border-left-color: #16a34a;
  background: #f0fdf4;
  color: #15803d;
}
.choice-feedback.fb-incorrect {
  border-left-color: #dc2626;
  background: #fef2f2;
  color: #b91c1c;
}
.choice-feedback.fb-missed {
  border-left-color: #d97706;
  background: #fffbeb;
  color: #92400e;
}

.choice.ok     { border-color: #16a34a !important; background: #f0fdf4 !important; }
.choice.bad    { border-color: #dc2626 !important; background: #fef2f2 !important; }
.choice.missed { border-color: #d97706 !important; background: #fffbeb !important; }

.fb {
  padding: 8px 12px; border-radius: 4px;
  margin-bottom: 10px; font-size: .93em; font-weight: 600;
  display: none;
}
.fb.ok  { background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }
.fb.bad { background: #fef2f2; color: #b91c1c; border: 1px solid #fecaca; }
.hint-box, .expl-box {
  padding: 7px 10px; margin-bottom: 10px;
  font-size: .9em; line-height: 1.5; display: none;
}
.hint-box { background: #fefce8; border-left: 3px solid #ca8a04; color: #713f12; }
.expl-box { background: #f0f9ff; border-left: 3px solid #0284c7; color: #0c4a6e; }
.box-lbl { display: block; font-weight: 700; font-size: .85em; margin-bottom: 3px; }
.actions { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px; }
button {
  padding: 5px 13px; border-radius: 4px; border: 1px solid transparent;
  cursor: pointer; font-size: .88em; font-family: inherit;
  transition: background .12s;
}
.btn-check { background: #0284c7; color: #fff; border-color: #0369a1; }
.btn-check:hover { background: #0369a1; }
.btn-hint  { background: #fef9c3; color: #713f12; border-color: #fde047; }
.btn-hint:hover { background: #fef08a; }
.btn-reset { background: transparent; color: #0284c7; border-color: #0284c7; display: none; }
.btn-reset:hover { background: #e0f2fe; }

/* Dark mode — driven by the MyST .dark class on <html>, mirrored onto the
   host as [data-theme="dark"] (see render). We avoid prefers-color-scheme
   so the widget follows the site's theme toggle, not the OS setting. */
:host([data-theme="dark"]) .quiz { background: #0c1a27; border-color: #1e3a4f; border-left-color: #0284c7; color: #e2e8f0; }
:host([data-theme="dark"]) .quiz-hdr { background: #0c2940; border-color: #1e4060; color: #7dd3fc; }
:host([data-theme="dark"]) .question { color: #e2e8f0; }
:host([data-theme="dark"]) .choice { background: #1a2535; border-color: #2d3f55; color: #e2e8f0; }
:host([data-theme="dark"]) .choice:hover { background: #0c2030; border-color: #0284c7; }
:host([data-theme="dark"]) .choice.ok     { background: #052e16 !important; border-color: #16a34a !important; }
:host([data-theme="dark"]) .choice.bad    { background: #2d0a0a !important; border-color: #dc2626 !important; }
:host([data-theme="dark"]) .choice.missed { background: #1c1208 !important; border-color: #d97706 !important; }
:host([data-theme="dark"]) .choice-feedback { background: #1e2d3d; color: #94a3b8; border-left-color: #475569; }
:host([data-theme="dark"]) .choice-feedback.fb-correct  { background: #052e16; color: #4ade80; border-left-color: #16a34a; }
:host([data-theme="dark"]) .choice-feedback.fb-incorrect{ background: #2d0a0a; color: #f87171; border-left-color: #dc2626; }
:host([data-theme="dark"]) .choice-feedback.fb-missed   { background: #1c1208; color: #fcd34d; border-left-color: #d97706; }
:host([data-theme="dark"]) .fb.ok  { background: #052e16; color: #4ade80; border-color: #14532d; }
:host([data-theme="dark"]) .fb.bad { background: #2d0a0a; color: #f87171; border-color: #7f1d1d; }
:host([data-theme="dark"]) .hint-box { background: #1c1208; color: #fde68a; }
:host([data-theme="dark"]) .expl-box { background: #0c1a27; color: #7dd3fc; }
:host([data-theme="dark"]) .btn-hint  { background: #1c1208; color: #fde68a; border-color: #ca8a04; }
:host([data-theme="dark"]) .btn-reset { color: #38bdf8; border-color: #38bdf8; }
:host([data-theme="dark"]) .btn-reset:hover { background: #0c2030; }
:host([data-theme="dark"]) .q-code { background: #334155; color: #e2e8f0; }
:host([data-theme="dark"]) .q-pre  { background: #0f1a2a; color: #e2e8f0; }
`;

// ── Render ────────────────────────────────────────────────────────────────────

function render({ model, el }) {
  const question    = model.get('question') ?? '';
  const choices     = model.get('choices')  ?? [];
  const multi       = model.get('multi')    ?? false;
  const hint        = model.get('hint')     ?? '';
  const explanation = model.get('explanation') ?? '';

  const correctIndices = choices.map((c, i) => c.correct ? i : -1).filter(i => i >= 0);
  const inputType = multi ? 'checkbox' : 'radio';
  const NAME = `quiz-${Math.random().toString(36).slice(2)}`;

  // ── Shadow DOM ──────────────────────────────────────────────────────────────
  const shadow = el.attachShadow({ mode: 'open' });
  const style = document.createElement('style');
  style.textContent = CSS;
  shadow.appendChild(style);

  const root = document.createElement('div');
  root.className = 'quiz';
  root.innerHTML = `
    <div class="quiz-hdr">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <circle cx="8" cy="8" r="7" stroke="#0369a1" stroke-width="1.2"/>
        <text x="8" y="12" text-anchor="middle" font-size="10"
              fill="#0369a1" font-family="sans-serif" font-weight="600">?</text>
      </svg>
      <span>Concept check</span>
    </div>
    <div class="quiz-body">
      <p class="question">${renderInline(question)}</p>
      ${multi ? '<p class="multinote">Select <strong>all</strong> that apply.</p>' : ''}
      <div class="choices">
        ${choices.map((c, i) => `
          <div class="choice-wrap">
            <label class="choice" data-idx="${i}">
              <input type="${inputType}" name="${NAME}" value="${i}">
              <span class="choice-text">${renderChoice(c.text)}</span>
            </label>
            ${c.feedback
              ? `<div class="choice-feedback" id="cf-${i}">${renderInline(c.feedback)}</div>`
              : ''}
          </div>`).join('')}
      </div>
      ${hint ? `<div class="hint-box"><span class="box-lbl">💡 Hint</span>${renderInline(hint)}</div>` : ''}
      <div class="fb"></div>
      ${explanation ? `<div class="expl-box"><span class="box-lbl">📖 Explanation</span>${renderInline(explanation)}</div>` : ''}
      <div class="actions">
        ${hint ? '<button class="btn-hint">Show hint</button>' : ''}
        <button class="btn-check">Check answer</button>
        <button class="btn-reset">Try again</button>
      </div>
    </div>`;
  shadow.appendChild(root);

  // ── Theme sync ──────────────────────────────────────────────────────────────
  // MyST toggles dark mode with a `.dark` class on <html>, independent of the
  // OS preference. Shadow DOM can't read that ancestor class in CSS, so mirror
  // it onto the host as [data-theme] and keep it in sync with the site toggle.
  // Wrapped defensively so a theming hiccup can never block the widget itself.
  let themeObserver = null;
  try {
    const syncTheme = () => {
      const dark = document.documentElement.classList.contains('dark');
      el.setAttribute('data-theme', dark ? 'dark' : 'light');
    };
    syncTheme();
    if (typeof MutationObserver !== 'undefined') {
      themeObserver = new MutationObserver(syncTheme);
      themeObserver.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['class'],
      });
    }
  } catch (e) {
    /* theming is non-essential; ignore */
  }

  // ── References ──────────────────────────────────────────────────────────────
  const choiceEls  = [...shadow.querySelectorAll('.choice')];
  const inputs     = [...shadow.querySelectorAll('input')];
  const fb         = shadow.querySelector('.fb');
  const hintBox    = shadow.querySelector('.hint-box');
  const explBox    = shadow.querySelector('.expl-box');
  const btnCheck   = shadow.querySelector('.btn-check');
  const btnReset   = shadow.querySelector('.btn-reset');
  const btnHint    = shadow.querySelector('.btn-hint');

  // ── Submit ──────────────────────────────────────────────────────────────────
  btnCheck.addEventListener('click', () => {
    const selected = inputs.filter(i => i.checked).map(i => +i.value);

    if (!selected.length) {
      fb.textContent = 'Please select an answer before checking.';
      fb.className = 'fb bad';
      fb.style.display = 'block';
      return;
    }

    const cset = new Set(correctIndices);
    const sset = new Set(selected);
    const ok = multi
      ? correctIndices.every(i => sset.has(i)) && selected.every(i => cset.has(i))
      : selected.length === 1 && cset.has(selected[0]);

    choiceEls.forEach((lbl, i) => {
      lbl.classList.remove('ok', 'bad', 'missed');
      const cfEl = shadow.getElementById(`cf-${i}`);

      if (sset.has(i) && cset.has(i)) {
        lbl.classList.add('ok');
        if (cfEl) { cfEl.classList.add('visible', 'fb-correct'); }
      } else if (sset.has(i) && !cset.has(i)) {
        lbl.classList.add('bad');
        if (cfEl) { cfEl.classList.add('visible', 'fb-incorrect'); }
      } else if (!sset.has(i) && cset.has(i)) {
        lbl.classList.add('missed');
        if (cfEl) { cfEl.classList.add('visible', 'fb-missed'); }
      }
      lbl.querySelector('input').disabled = true;
    });

    fb.textContent = ok
      ? (multi ? '✅ Correct! You selected all the right answers.' : '✅ Correct!')
      : (multi ? '❌ Not quite.' : '❌ Not quite.');
    fb.className = 'fb ' + (ok ? 'ok' : 'bad');
    fb.style.display = 'block';

    if (explBox) explBox.style.display = 'block';
    btnCheck.style.display = 'none';
    btnReset.style.display = 'inline-block';
  });

  // ── Hint ────────────────────────────────────────────────────────────────────
  if (btnHint && hintBox) {
    btnHint.addEventListener('click', () => {
      const show = hintBox.style.display !== 'block';
      hintBox.style.display = show ? 'block' : 'none';
      btnHint.textContent = show ? 'Hide hint' : 'Show hint';
    });
  }

  // ── Reset ───────────────────────────────────────────────────────────────────
  btnReset.addEventListener('click', () => {
    inputs.forEach(i => { i.checked = false; i.disabled = false; });
    choiceEls.forEach(l => l.classList.remove('ok', 'bad', 'missed'));
    shadow.querySelectorAll('.choice-feedback').forEach(el => {
      el.classList.remove('visible', 'fb-correct', 'fb-incorrect', 'fb-missed');
    });
    fb.style.display = 'none'; fb.textContent = '';
    if (explBox)  explBox.style.display = 'none';
    if (hintBox)  hintBox.style.display = 'none';
    if (btnHint)  btnHint.textContent = 'Show hint';
    btnCheck.style.display = 'inline-block';
    btnReset.style.display = 'none';
  });

  return () => { if (themeObserver) themeObserver.disconnect(); shadow.innerHTML = ''; };
}

export default { render };