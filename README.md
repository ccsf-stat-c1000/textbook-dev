# Environment Setup

This project uses a hybrid **conda + pip** environment — conda for compiled data science packages and pip for book tooling.

## Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/download)
- Node.js is required by Jupyter Book — it will be installed automatically via conda in the setup steps below.

## Setup

### 1. Create a conda environment

```bash
conda create -n statc1000book python=3.11
conda activate statc1000book
```

### 2. Clone the textbook repo

```bash
git clone https://github.com/ccsf-stat-c1000/textbook-dev.git
cd textbook-dev
```

### 3. Install all packages via environment.yml

```bash
conda env create -f environment.yml
conda activate statc1000book
```

### 4. Start the book

```bash
jupyter book start
```

## Building the PDF

The website is the primary format; the PDF is a derived print edition.

```bash
conda activate statc1000book
pip install pyyaml pillow cairosvg
conda install -c conda-forge tectonic     # or any latexmk/xelatex install

python scripts/build_pdf.py --dry-run     # stage and inspect first
python scripts/build_pdf.py               # full build
```

Writes `introduction-to-statistics.pdf` to the repo root.

The script stages a rewritten copy of the book in `../textbook-dev-pdf-build/`
(outside the repo, because `myst build` inherits any `myst.yml` it finds in a
parent directory). In that copy:

- `{quiz}` / `{quiz-multi}` widgets become static numbered questions, with the
  correct answers collected into an **Answer Key** at the back. Hints stay with
  the question; feedback and explanations move to the key.
- `.gif` figures become `.png` and `.svg` figures become `.pdf`, since LaTeX
  can embed neither original format.
- Page headings are stamped with the same page numbers the website shows, so
  "open page 30" means the same thing in both editions.

Re-run it whenever pages change. Nothing in the source tree is modified.

## Reproducibility

### Save your environment

```bash
# Pip dependencies
pip freeze > requirements.txt

# Full conda + pip environment (recommended)
conda env export > environment.yml
```

### Restore on a new machine

```bash
# From environment.yml (recommended — captures everything)
conda env create -f environment.yml
conda activate statc1000book

# Or pip only
pip install -r requirements.txt
```
