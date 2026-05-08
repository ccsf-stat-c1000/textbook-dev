/**
 * quiz.mjs — MyST JavaScript Plugin
 *
 * Provides {quiz} and {quiz-multi} directives that render interactive
 * concept-check widgets via MyST's anywidget system.
 *
 * Files needed (place both next to myst.yml):
 *   quiz.mjs           ← this file (directive plugin)
 *   quiz-widget.mjs    ← the anywidget render module
 *
 * myst.yml:
 *   project:
 *     plugins:
 *       - quiz.mjs
 *
 * ── Single-answer ────────────────────────────────────────────────────────────
 *
 *   :::{quiz} What is the time complexity of binary search?
 *   :hint: Think about how many elements are eliminated each step.
 *   :explanation: Each step halves the search space, giving $O(\log n)$.
 *   * O(n)
 *   * *O(\log n)      ← prefix * on the choice marks it as correct
 *   * O(n^2)
 *   * O(1)
 *   :::
 *
 * ── Multi-select ─────────────────────────────────────────────────────────────
 *
 *   :::{quiz-multi} Which are valid Python keywords?
 *   :explanation: `pass` and `yield` are reserved; `func` and `val` are not.
 *   * *pass
 *   * func
 *   * *yield
 *   * val
 *   :::
 *
 * ── Code-block answer ────────────────────────────────────────────────────────
 *
 *   :::{quiz} Which snippet reverses a list without modifying it?
 *   * *```python
 *     xs[::-1]
 *     ```
 *   * ```python
 *     xs.reverse()
 *     ```
 *   :::
 *
 * ── Inline math ──────────────────────────────────────────────────────────────
 *
 *   :::{quiz} What is the derivative of $x^n$?
 *   * $x^{n-1}$
 *   * *$n x^{n-1}$
 *   * $n x^n$
 *   :::
 */

// Path to the anywidget render module, relative to the .md files that use it.
// e.g. if pages are in pages/ and quiz-widget.mjs is in the project root: '../quiz-widget.mjs'
// e.g. if quiz-widget.mjs is in the same folder as the pages: './quiz-widget.mjs'
const WIDGET_PATH = 'quiz-widget.mjs';

// ── Choice parser ─────────────────────────────────────────────────────────────

/**
 * Parse the directive body into an array of choice objects.
 * Lines starting with "* " are choices; "* *" prefix marks correct answer(s).
 * Fenced code blocks (```…```) beneath a choice line are collected into
 * that choice's text.
 *
 * Returns: Array<{ text: string, correct: boolean }>
 */
function parseChoices(body) {
  const lines = (body ?? '').split('\n');
  const choices = [];
  let cur = null;
  let inFence = false;
  let fenceLang = '';
  let fenceLines = [];

  for (const line of lines) {
    // Start of fenced code block inside a choice
    if (cur && !inFence) {
      const m = line.match(/^(\s*)```(\w*)$/);
      if (m) {
        inFence = true;
        fenceLang = m[2] ?? '';
        fenceLines = [];
        continue;
      }
    }
    // Inside fence
    if (inFence) {
      if (line.match(/^(\s*)```$/)) {
        cur.text += `\`\`\`${fenceLang}\n${fenceLines.join('\n')}\n\`\`\``;
        inFence = false; fenceLines = []; fenceLang = '';
      } else {
        fenceLines.push(line);
      }
      continue;
    }
    // New choice line: "* " or "* *"
    const m = line.match(/^\* (\*?)(.*)$/);
    if (m) {
      if (cur) choices.push(cur);
      cur = { correct: m[1] === '*', text: m[2].trim() };
      continue;
    }
    // Continuation
    if (cur && line.trim()) cur.text += '\n' + line.trim();
  }
  if (cur) choices.push(cur);
  return choices;
}

// ── Shared directive builder ──────────────────────────────────────────────────

function buildDirective(data, multi) {
  const question    = data.arg ?? '';
  const choices     = parseChoices(data.body);
  const hint        = data.options?.hint ?? '';
  const explanation = data.options?.explanation ?? '';

  return [{
    type: 'anywidget',
    esm: WIDGET_PATH,
    model: { question, choices, multi, hint, explanation },
  }];
}

// ── {quiz} — single-answer ────────────────────────────────────────────────────

const quizDirective = {
  name: 'quiz',
  doc: 'An interactive single-answer concept-check widget. ' +
       'Mark the correct choice with a `* *` prefix.',
  arg: {
    type: String,
    required: true,
    doc: 'The question text. Supports inline math ($...$).',
  },
  options: {
    hint:        { type: String, doc: 'Optional hint shown on demand.' },
    explanation: { type: String, doc: 'Optional explanation shown after submission.' },
  },
  body: {
    type: String,
    required: true,
    doc: 'Answer choices, one per line, starting with `* `. ' +
         'Prefix the correct choice with `* *`. ' +
         'Choices support inline code (`…`), math ($…$), ' +
         'and fenced code blocks (```lang … ```).',
  },
  run(data) {
    return buildDirective(data, false);
  },
};

// ── {quiz-multi} — multi-select ───────────────────────────────────────────────

const quizMultiDirective = {
  name: 'quiz-multi',
  doc: 'An interactive multi-select concept-check widget. ' +
       'Mark every correct choice with a `* *` prefix.',
  arg: {
    type: String,
    required: true,
    doc: 'The question text. Supports inline math ($...$).',
  },
  options: {
    hint:        { type: String, doc: 'Optional hint shown on demand.' },
    explanation: { type: String, doc: 'Optional explanation shown after submission.' },
  },
  body: {
    type: String,
    required: true,
    doc: 'Answer choices. Prefix every correct one with `* *`.',
  },
  run(data) {
    return buildDirective(data, true);
  },
};

// ── Plugin export ─────────────────────────────────────────────────────────────

const plugin = {
  name: 'MyST Quiz Plugin',
  author: 'Your Name',
  license: 'MIT',
  directives: [quizDirective, quizMultiDirective],
};

export default plugin;