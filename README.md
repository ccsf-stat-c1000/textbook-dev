# Environment Setup

This project uses a hybrid **conda + pip** environment — conda for compiled data science packages and pip for book tooling.

## Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/download)
- Node.js is required by Jupyter Book — it will be installed automatically via conda in the setup steps below.

## Setup

### 1. Create a conda environment

```bash
conda create -n mybook python=3.11
conda activate mybook
```

### 2. Install packages via conda

```bash
conda install -c conda-forge \
  nodejs \
  jupyterlab \
  jupyterlab-myst \
  jupytext \
  ipykernel \
  numpy \
  pandas \
  matplotlib \
  seaborn \
  scikit-learn \
  scipy \
  statsmodels \
  ipywidgets

### 3. Install additional packages via pip

```bash
pip install jupyter-book datascience polars plotly
```
```

### 4. Build the book

```bash
jupyter-book build .
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
conda activate mybook

# Or pip only
pip install -r requirements.txt
```

## environment.yml reference

```yaml
name: mybook
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - nodejs
  - jupyterlab
  - jupyterlab-myst
  - jupytext
  - ipykernel
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn
  - scipy
  - statsmodels
  - ipywidgets
  - pip
  - pip:
    - jupyter-book
    - datascience
    - polars
    - plotly
```
