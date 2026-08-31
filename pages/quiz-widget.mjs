/**
 * quiz-widget.mjs — MyST anywidget for interactive quiz / concept-check questions.
 *
 * Model keys:
 *   question    {string}   Question text (plain, `code`, or LaTeX math)
 *   choices     {Array}    [{text, correct, feedback}]
 *   multi       {boolean}  true = checkboxes, false = radio
 *   hint        {string}   Optional hint text
 *   explanation {string}   Optional explanation shown after submission
 *
 * Math: inline `$...$` and display `$$...$$` LaTeX are rendered with KaTeX,
 * matching the rest of the book. Escape a literal dollar sign with `\$`.
 */

// ── KaTeX loading ─────────────────────────────────────────────────────────────
// The rest of the book renders math with KaTeX (MyST pre-renders it server-side
// and the book theme loads KaTeX's CSS globally). This widget lives in a Shadow
// DOM, so that global stylesheet can't reach it and math isn't pre-rendered in
// the strings the directive passes us. We therefore render math client-side with
// KaTeX and inject KaTeX's stylesheet into each widget's shadow root.
//
// Pin to a specific version so the fonts referenced by the CSS resolve on the
// same CDN. Bump both together if you upgrade.
const KATEX_VERSION = '0.16.11';
const KATEX_JS  = `https://cdn.jsdelivr.net/npm/katex@${KATEX_VERSION}/dist/katex.mjs`;
const KATEX_CSS = `https://cdn.jsdelivr.net/npm/katex@${KATEX_VERSION}/dist/katex.min.css`;

// Load KaTeX once per page and cache the promise so multiple quizzes share it.
let katexPromise = null;
function loadKatex() {
  if (!katexPromise) {
    katexPromise = import(KATEX_JS).then(m => m.default ?? m);
  }
  return katexPromise;
}

// ── Inline renderers ──────────────────────────────────────────────────────────

function esc(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Emit a placeholder span carrying the raw TeX; typesetMath() renders it with
// KaTeX after the DOM is in place. The TeX is URI-encoded so it survives inside
// an HTML attribute without escaping issues (KaTeX needs the raw source, incl.
// characters like < > &).
function mathSpan(tex, display) {
  return `<span class="q-math" data-tex="${encodeURIComponent(tex)}"` +
         ` data-display="${display ? '1' : '0'}"></span>`;
}

// Single-pass tokenizer: handles display math ($$...$$), inline math ($...$),
// inline code (`...`), and escaped dollar signs (\$). Everything else is
// HTML-escaped text. A single pass (rather than chained regex replaces) keeps
// `$` inside code and backticks inside math from being misinterpreted.
function renderInline(text) {
  const src = String(text ?? '');
  const n = src.length;
  let out = '';
  let i = 0;

  while (i < n) {
    const ch = src[i];

    // Escaped dollar → literal $
    if (ch === '\\' && src[i + 1] === '$') { out += '$'; i += 2; continue; }

    // Display math $$...$$
    if (ch === '$' && src[i + 1] === '$') {
      const end = src.indexOf('$$', i + 2);
      if (end !== -1) {
        out += mathSpan(src.slice(i + 2, end), true);
        i = end + 2;
        continue;
      }
    }

    // Inline math $...$
    if (ch === '$') {
      const end = src.indexOf('$', i + 1);
      if (end !== -1) {
        out += mathSpan(src.slice(i + 1, end), false);
        i = end + 1;
        continue;
      }
    }

    // Inline code `...`
    if (ch === '`') {
      const end = src.indexOf('`', i + 1);
      if (end !== -1) {
        out += `<code class="q-code">${esc(src.slice(i + 1, end))}</code>`;
        i = end + 1;
        continue;
      }
    }

    out += esc(ch);
    i++;
  }

  return out;
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

// Render every .q-math placeholder in the shadow root with KaTeX. Falls back to
// plain italic text if KaTeX can't be loaded (e.g. offline / CSP) or a specific
// expression fails to parse, so the widget always stays usable.
async function typesetMath(shadow) {
  const nodes = [...shadow.querySelectorAll('.q-math')];
  if (!nodes.length) return;

  let katex = null;
  try {
    katex = await loadKatex();
  } catch (e) {
    /* KaTeX unavailable; fall through to plain-text fallback below */
  }

  for (const node of nodes) {
    const tex = decodeURIComponent(node.getAttribute('data-tex') || '');
    const display = node.getAttribute('data-display') === '1';
    if (katex) {
      try {
        katex.render(tex, node, {
          displayMode: display,
          throwOnError: false,
        });
        continue;
      } catch (e) {
        /* fall through to plain-text fallback */
      }
    }
    node.textContent = tex;
    node.style.fontStyle = 'italic';
  }
}

// ── Spoken math ───────────────────────────────────────────────────────────────
// KaTeX marks its visual output aria-hidden and puts the real content in a
// MathML branch. Browsers skip that branch when computing the *accessible name*
// of a form control, so a radio labelled "P(Z $\leq -1.5)$" would announce as
// just "P(Z " — indistinguishable from "P(Z $\geq -1.5)$". We therefore build a
// spoken-language version of each choice and attach it with aria-label.
//
// This affects naming only; math in the question, hint, feedback and
// explanation is read from KaTeX's MathML as normal.

const TEX_WORDS = {
  mu: 'mu', sigma: 'sigma', alpha: 'alpha', beta: 'beta', chi: 'chi', pi: 'pi',
  approx: 'approximately', neq: 'not equal to', ne: 'not equal to',
  leq: 'less than or equal to', le: 'less than or equal to',
  geq: 'greater than or equal to', ge: 'greater than or equal to',
  pm: 'plus or minus', mp: 'minus or plus',
  times: 'times', cdot: 'times', div: 'divided by',
  to: 'to', rightarrow: 'to', implies: 'implies',
  ldots: 'and so on', cdots: 'and so on', dots: 'and so on',
  infty: 'infinity', percent: 'percent',
  quad: ' ', qquad: ' ', left: ' ', right: ' ', displaystyle: ' ', tfrac: ' ',
};

// Turn one TeX fragment into words. Order matters: \sqrt, \hat and \bar are
// expanded before \frac so a nested argument no longer contains braces, and the
// "negative number" pass runs before the generic minus pass.
function speakTex(tex) {
  let s = ' ' + String(tex ?? '') + ' ';
  s = s.replace(/\\text\s*\{([^{}]*)\}/g, ' $1 ');
  s = s.replace(/\\sqrt\s*\{([^{}]*)\}/g, ' the square root of $1 ');
  s = s.replace(/\\hat\s*\{([^{}]*)\}/g, ' $1 hat ');
  s = s.replace(/\\hat\s*([A-Za-z])/g, ' $1 hat ');
  s = s.replace(/\\bar\s*\{([^{}]*)\}/g, ' $1 bar ');
  s = s.replace(/\\bar\s*([A-Za-z])/g, ' $1 bar ');
  for (let k = 0; k < 3; k++) {
    s = s.replace(/\\d?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}/g, ' $1 over $2 ');
    s = s.replace(/\\sqrt\s*\{([^{}]*)\}/g, ' the square root of $1 ');
  }
  s = s.replace(/\|([^|]{1,24})\|/g, ' the absolute value of $1 ');
  s = s.replace(/\{,\}/g, ',');
  s = s.replace(/\\%/g, ' percent ');
  s = s.replace(/\^\s*\{?\s*\*\s*\}?/g, ' star ');
  s = s.replace(/_\s*\{([^{}]*)\}/g, ' sub $1 ');
  s = s.replace(/_\s*([A-Za-z0-9])/g, ' sub $1 ');
  s = s.replace(/\^\s*\{([^{}]*)\}/g, ' to the power $1 ');
  s = s.replace(/\^\s*([A-Za-z0-9])/g, ' to the power $1 ');
  s = s.replace(/\\([a-zA-Z]+)/g,
    (m, c) => TEX_WORDS[c] !== undefined ? ' ' + TEX_WORDS[c] + ' ' : ' ' + c + ' ');
  s = s.replace(/\\[,;: ]/g, ' ');
  s = s.replace(/[{}]/g, ' ');
  s = s.replace(/(^|[\s=(<>,])-\s*(?=[\d.])/g, '$1 negative ');
  s = s.replace(/-/g, ' minus ');
  s = s.replace(/\+/g, ' plus ');
  s = s.replace(/</g, ' less than ');
  s = s.replace(/>/g, ' greater than ');
  s = s.replace(/=/g, ' equals ');
  s = s.replace(/\//g, ' over ');
  s = s.replace(/\*/g, ' times ');
  return s.replace(/\s+/g, ' ').trim();
}

// Plain-text rendering of a whole choice: prose kept as-is, math spoken.
// Mirrors renderInline's tokenizer so the two never disagree about delimiters.
function speakChoice(text) {
  const src = String(text ?? '');
  let out = '', i = 0;
  while (i < src.length) {
    if (src[i] === '\\' && src[i + 1] === '$') { out += '$'; i += 2; continue; }
    if (src[i] === '$') {
      const dd = src[i + 1] === '$';
      const close = src.indexOf(dd ? '$$' : '$', i + (dd ? 2 : 1));
      if (close < 0) { out += src.slice(i); break; }
      out += ' ' + speakTex(src.slice(i + (dd ? 2 : 1), close)) + ' ';
      i = close + (dd ? 2 : 1);
      continue;
    }
    if (src[i] === '`') {
      const close = src.indexOf('`', i + 1);
      if (close < 0) { out += src.slice(i); break; }
      out += ' ' + src.slice(i + 1, close) + ' ';
      i = close + 1;
      continue;
    }
    out += src[i]; i++;
  }
  return out.replace(/\s+/g, ' ').trim();
}

// Only override the accessible name when the choice actually contains math.
// Prose-only choices keep native label semantics, so the visible text and the
// accessible name stay identical (WCAG 2.5.3 Label in Name).
function hasMath(text) {
  return /(?<!\\)\$/.test(String(text ?? ''));
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
.multinote { font-size: .83em; color: #556377; font-style: italic; margin: -4px 0 8px; }
.choices { display: flex; flex-direction: column; gap: 6px; margin-bottom: 12px; }

/* Choice row — wraps input + content + feedback pill */
.choice-wrap { display: flex; flex-direction: column; }
.choice {
  display: flex; align-items: flex-start; gap: 8px;
  padding: 8px 10px; border-radius: 4px;
  border: 1px solid #7e8b99; background: #fff;
  cursor: pointer; font-size: .93em; line-height: 1.5;
  transition: border-color .12s, background .12s;
  user-select: none;
}
.choice:hover { border-color: #0369a1; background: #f0f9ff; }
/* Mirror the input's focus ring onto the whole clickable card. */
.choice:focus-within { outline: 2px solid #0369a1; outline-offset: 1px; }
/* Locked after submission. We use aria-disabled rather than the disabled
   attribute so the options stay focusable and a keyboard or screen-reader user
   can still review what they picked and read the feedback attached to it. */
.choice[aria-disabled="true"] { cursor: default; }
.choice[aria-disabled="true"]:hover { border-color: #7e8b99; background: #fff; }
.choice[aria-disabled="true"].ok:hover     { border-color: #16a34a; background: #f0fdf4; }
.choice[aria-disabled="true"].bad:hover    { border-color: #dc2626; background: #fef2f2; }
.choice[aria-disabled="true"].missed:hover { border-color: #d97706; background: #fffbeb; }
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

/* KaTeX math. Inline math flows with the text; display math ($$...$$) gets
   centered on its own line and can scroll horizontally if it overflows. */
.q-math { font-style: normal; }
.q-math .katex-display { margin: .5em 0; overflow-x: auto; overflow-y: hidden; }

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
.btn-check { background: #0369a1; color: #fff; border-color: #075985; }
.btn-check:hover { background: #075985; }
.btn-hint  { background: #fef9c3; color: #713f12; border-color: #ca8a04; }
.btn-hint:hover { background: #fef08a; }
.btn-reset { background: transparent; color: #0369a1; border-color: #0369a1; display: none; }
.btn-reset:hover { background: #e0f2fe; }
/* The result banner receives focus after submission, so it needs its own ring. */
.fb:focus-visible { outline: 2px solid #0369a1; outline-offset: 2px; }

/* Dark mode — driven by the MyST .dark class on <html>, mirrored onto the
   host as [data-theme="dark"] (see render). We avoid prefers-color-scheme
   so the widget follows the site's theme toggle, not the OS setting. */
:host([data-theme="dark"]) .quiz { background: #0c1a27; border-color: #1e3a4f; border-left-color: #0284c7; color: #e2e8f0; }
:host([data-theme="dark"]) .quiz-hdr { background: #0c2940; border-color: #1e4060; color: #7dd3fc; }
:host([data-theme="dark"]) .question { color: #e2e8f0; }
:host([data-theme="dark"]) .multinote { color: #9db2c6; }
:host([data-theme="dark"]) .choice { background: #1a2535; border-color: #6a80a1; color: #e2e8f0; }
:host([data-theme="dark"]) .choice:hover { background: #0c2030; border-color: #38bdf8; }
:host([data-theme="dark"]) .choice[aria-disabled="true"]:hover { background: #1a2535; border-color: #6a80a1; }
:host([data-theme="dark"]) .choice:focus-within { outline-color: #38bdf8; }
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
/* KaTeX colours itself with currentColor, so it follows the surrounding text
   colour automatically in dark mode; this just guards against any stray rule. */
:host([data-theme="dark"]) .q-math .katex { color: inherit; }
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

  // KaTeX's stylesheet must live inside the shadow root — the book theme loads
  // it globally, but Shadow DOM is isolated from ancestor stylesheets.
  const katexCss = document.createElement('link');
  katexCss.rel = 'stylesheet';
  katexCss.href = KATEX_CSS;
  shadow.appendChild(katexCss);

  const style = document.createElement('style');
  style.textContent = CSS;
  shadow.appendChild(style);

  const root = document.createElement('div');
  root.className = 'quiz';
  const QID = `q-${NAME}`;
  const HID = `h-${NAME}`;
  root.innerHTML = `
    <div class="quiz-hdr">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
           aria-hidden="true" focusable="false">
        <circle cx="8" cy="8" r="7" stroke="#0369a1" stroke-width="1.2"/>
        <text x="8" y="12" text-anchor="middle" font-size="10"
              fill="#0369a1" font-family="sans-serif" font-weight="600">?</text>
      </svg>
      <span>Concept check</span>
    </div>
    <div class="quiz-body">
      <p class="question" id="${QID}">${renderInline(question)}</p>
      ${multi ? '<p class="multinote">Select <strong>all</strong> that apply.</p>' : ''}
      <div class="choices" role="${multi ? 'group' : 'radiogroup'}" aria-labelledby="${QID}">
        ${choices.map((c, i) => `
          <div class="choice-wrap">
            <label class="choice" data-idx="${i}">
              <input type="${inputType}" name="${NAME}" value="${i}"${
                hasMath(c.text) ? ` aria-label="${esc(speakChoice(c.text))}"` : ''}>
              <span class="choice-text">${renderChoice(c.text)}</span>
            </label>
            ${c.feedback
              ? `<div class="choice-feedback" id="cf-${i}">${renderInline(c.feedback)}</div>`
              : ''}
          </div>`).join('')}
      </div>
      ${hint ? `<div class="hint-box" id="${HID}"><span class="box-lbl">💡 Hint</span>${renderInline(hint)}</div>` : ''}
      <div class="fb" role="status" tabindex="-1"></div>
      ${explanation ? `<div class="expl-box"><span class="box-lbl">📖 Explanation</span>${renderInline(explanation)}</div>` : ''}
      <div class="actions">
        ${hint ? `<button type="button" class="btn-hint" aria-expanded="false" aria-controls="${HID}">Show hint</button>` : ''}
        <button type="button" class="btn-check">Check answer</button>
        <button type="button" class="btn-reset">Try again</button>
      </div>
    </div>`;
  shadow.appendChild(root);

  // Typeset any $...$ / $$...$$ math with KaTeX (async; feedback/explanation are
  // already in the DOM even while hidden, so they get typeset up front too).
  typesetMath(shadow);

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

  // ── Answer locking ──────────────────────────────────────────────────────────
  // After submission the options must stop responding, but they must NOT get the
  // `disabled` attribute: that drops them out of the tab order, so a keyboard or
  // screen-reader user could no longer review their answer or the per-choice
  // feedback. Instead we mark them aria-disabled and swallow the interaction,
  // which covers both mouse clicks and the keyboard (Space fires click too).
  let locked = false;
  inputs.forEach(input => {
    input.addEventListener('click', e => { if (locked) e.preventDefault(); });
  });
  const setLocked = on => {
    locked = on;
    choiceEls.forEach(lbl => {
      if (on) lbl.setAttribute('aria-disabled', 'true');
      else    lbl.removeAttribute('aria-disabled');
    });
    inputs.forEach(i => {
      if (on) i.setAttribute('aria-disabled', 'true');
      else    i.removeAttribute('aria-disabled');
    });
  };

  // ── Submit ──────────────────────────────────────────────────────────────────
  btnCheck.addEventListener('click', () => {
    const selected = inputs.filter(i => i.checked).map(i => +i.value);

    if (!selected.length) {
      fb.textContent = 'Please select an answer before checking.';
      fb.className = 'fb bad';
      fb.style.display = 'block';
      fb.focus();
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
      // Point the option at its own feedback now that the feedback is visible.
      // A hidden element contributes nothing to the description, so this is only
      // wired up once the text is actually on screen.
      if (cfEl && cfEl.classList.contains('visible')) {
        lbl.querySelector('input').setAttribute('aria-describedby', `cf-${i}`);
      }
    });
    setLocked(true);

    // State is carried in words as well as colour, so the outcome does not
    // depend on being able to see the green/red tint (WCAG 1.4.1).
    fb.textContent = ok
      ? (multi ? '✅ Correct! You selected all the right answers.' : '✅ Correct!')
      : (multi ? '❌ Not quite. Review the feedback under each option.'
               : '❌ Not quite. Review the feedback under each option.');
    fb.className = 'fb ' + (ok ? 'ok' : 'bad');
    fb.style.display = 'block';

    if (explBox) explBox.style.display = 'block';
    btnCheck.style.display = 'none';
    btnReset.style.display = 'inline-block';

    // The button that was just activated is about to be hidden, which would
    // otherwise drop focus onto <body>. Move focus to the result instead: it
    // fixes the focus order and announces the outcome in one step.
    fb.focus();
  });

  // ── Hint ────────────────────────────────────────────────────────────────────
  if (btnHint && hintBox) {
    btnHint.addEventListener('click', () => {
      const show = hintBox.style.display !== 'block';
      hintBox.style.display = show ? 'block' : 'none';
      btnHint.textContent = show ? 'Hide hint' : 'Show hint';
      btnHint.setAttribute('aria-expanded', show ? 'true' : 'false');
    });
  }

  // ── Reset ───────────────────────────────────────────────────────────────────
  btnReset.addEventListener('click', () => {
    inputs.forEach(i => { i.checked = false; i.removeAttribute('aria-describedby'); });
    setLocked(false);
    choiceEls.forEach(l => l.classList.remove('ok', 'bad', 'missed'));
    shadow.querySelectorAll('.choice-feedback').forEach(el => {
      el.classList.remove('visible', 'fb-correct', 'fb-incorrect', 'fb-missed');
    });
    fb.style.display = 'none'; fb.textContent = '';
    if (explBox)  explBox.style.display = 'none';
    if (hintBox)  hintBox.style.display = 'none';
    if (btnHint) {
      btnHint.textContent = 'Show hint';
      btnHint.setAttribute('aria-expanded', 'false');
    }
    btnCheck.style.display = 'inline-block';
    btnReset.style.display = 'none';
    // Send focus back to the first option so the keyboard user resumes where
    // the question actually starts, rather than at the top of the document.
    if (inputs.length) inputs[0].focus();
  });

  return () => { if (themeObserver) themeObserver.disconnect(); shadow.innerHTML = ''; };
}

export default { render };