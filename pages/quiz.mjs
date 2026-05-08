/**
 * quiz.mjs — MyST JavaScript Plugin
 *
 * Provides {quiz} and {quiz-multi} directives that render interactive
 * concept-check widgets via MyST's anywidget system.
 *
 * Files needed (place both in pages/):
 *   quiz.mjs           ← this file (directive plugin)
 *   quiz-widget.mjs    ← the anywidget render module
 *
 * myst.yml:
 *   project:
 *     plugins:
 *       - pages/quiz.mjs
 *
 * ── Single-answer ────────────────────────────────────────────────────────────
 *
 *   :::{quiz} What is the time complexity of binary search?
 *   :hint: Think about how many elements are eliminated each step.
 *   :explanation: Each step halves the search space, giving $O(\log n)$.
 *   :feedback-0: O(n) is linear — binary search is faster than that.
 *   :feedback-1: Correct! Each step halves the remaining search space.
 *   :feedback-2: O(n²) would be very slow — think simpler.
 *   :feedback-3: O(1) means constant time — binary search still needs to look.
 *   * O(n)
 *   * *O(\log n)
 *   * O(n²)
 *   * O(1)
 *   :::
 *
 * ── Multi-select ─────────────────────────────────────────────────────────────
 *
 *   :::{quiz-multi} Which are valid Python keywords?
 *   :explanation: `pass` and `yield` are reserved; `func` and `val` are not.
 *   :feedback-0: Correct — `pass` is a valid keyword.
 *   :feedback-1: `func` is not a Python keyword.
 *   :feedback-2: Correct — `yield` is a valid keyword.
 *   :feedback-3: `val` is not a Python keyword.
 *   * *pass
 *   * func
 *   * *yield
 *   * val
 *   :::
 *
 * ── Code-block answer ────────────────────────────────────────────────────────
 *
 *   :::{quiz} Which snippet reverses a list without modifying it?
 *   :feedback-0: Correct! Slice with step -1 returns a new reversed list.
 *   :feedback-1: `reverse()` mutates in place and returns None.
 *   * *```python
 *     xs[::-1]
 *     ```
 *   * ```python
 *     xs.reverse()
 *     ```
 *   :::
 */

const WIDGET_PATH = './quiz-widget.mjs';

// ── Choice parser ─────────────────────────────────────────────────────────────

function parseChoices(body) {
  const lines = (body ?? '').split('\n');
  const choices = [];
  let cur = null;
  let inFence = false;
  let fenceLang = '';
  let fenceLines = [];

  for (const line of lines) {
    if (cur && !inFence) {
      const m = line.match(/^(\s*)```(\w*)$/);
      if (m) {
        inFence = true;
        fenceLang = m[2] ?? '';
        fenceLines = [];
        continue;
      }
    }
    if (inFence) {
      if (line.match(/^(\s*)```$/)) {
        cur.text += `\`\`\`${fenceLang}\n${fenceLines.join('\n')}\n\`\`\``;
        inFence = false; fenceLines = []; fenceLang = '';
      } else {
        fenceLines.push(line);
      }
      continue;
    }
    const m = line.match(/^\* (\*?)(.*)$/);
    if (m) {
      if (cur) choices.push(cur);
      cur = { correct: m[1] === '*', text: m[2].trim(), feedback: '' };
      continue;
    }
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

  // Attach per-choice feedback from :feedback-N: options
  choices.forEach((c, i) => {
    c.feedback = data.options?.[`feedback-${i}`] ?? '';
  });

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
    'feedback-0':  { type: String, doc: 'Feedback for choice 0.' },
    'feedback-1':  { type: String, doc: 'Feedback for choice 1.' },
    'feedback-2':  { type: String, doc: 'Feedback for choice 2.' },
    'feedback-3':  { type: String, doc: 'Feedback for choice 3.' },
    'feedback-4':  { type: String, doc: 'Feedback for choice 4.' },
    'feedback-5':  { type: String, doc: 'Feedback for choice 5.' },
  },
  body: {
    type: String,
    required: true,
    doc: 'Answer choices, one per line, starting with `* `. ' +
         'Prefix the correct choice with `* *`.',
  },
  run(data) { return buildDirective(data, false); },
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
    'feedback-0':  { type: String, doc: 'Feedback for choice 0.' },
    'feedback-1':  { type: String, doc: 'Feedback for choice 1.' },
    'feedback-2':  { type: String, doc: 'Feedback for choice 2.' },
    'feedback-3':  { type: String, doc: 'Feedback for choice 3.' },
    'feedback-4':  { type: String, doc: 'Feedback for choice 4.' },
    'feedback-5':  { type: String, doc: 'Feedback for choice 5.' },
  },
  body: {
    type: String,
    required: true,
    doc: 'Answer choices. Prefix every correct one with `* *`.',
  },
  run(data) { return buildDirective(data, true); },
};

// ── Plugin export ─────────────────────────────────────────────────────────────

const plugin = {
  name: 'MyST Quiz Plugin',
  author: 'Your Name',
  license: 'MIT',
  directives: [quizDirective, quizMultiDirective],
};

export default plugin;