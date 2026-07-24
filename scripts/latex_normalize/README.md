# LaTeX math normalizer

Converts Unicode/plaintext statistics notation in the book's Markdown pages into
proper LaTeX (`$...$`), so quizzes and prose render math the same way through
the rest of the Jupyter Book (KaTeX).

Examples of what it converts:

| Before | After |
| --- | --- |
| `H₀: μ = 50,000` | `$H_0$: $\mu = 50{,}000$` |
| `z ≈ −4.04` | `$z \approx -4.04$` |
| `σ/√n` and `σ²` | `$\sigma/\sqrt{n}$` and `$\sigma^2$` |
| `p̂`, `x̄` | `$\hat{p}$`, `$\bar{x}$` |
| `n = 15`, `t(124)` | `$n = 15$`, `$t(124)$` |

## What it will NOT touch

- Existing `$...$` / `$$...$$` math (protected)
- Inline code `` `...` `` and fenced code blocks (```` ```python ````, `{code-cell}`, `{math}`, `{raw}`)
- Plain English prose (a math run needs a real math signal to be wrapped)

MyST prose directives such as ```` ```{admonition} ````/`{note}` **are** converted
(they are prose, not code).

## Run it

```bash
python3 scripts/latex_normalize/run.py --check   # preview which pages change
python3 scripts/latex_normalize/run.py           # apply in place
git diff                                          # review
myst build --html                                 # rebuild and verify rendering
```

The pass is idempotent — re-running it is safe.
