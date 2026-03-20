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
