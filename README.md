# textbook-dev
An OER textbook for STAT C1000 at City College of San Francisco

## Environment Setup

This project uses a hybrid **conda + pip** environment — conda for compiled data science packages and pip for book tooling.

## Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/download)

## Setup

### 1. Create a conda environment

```bash
conda create -n mybook python=3.11
conda activate mybook
```

### 2. Install data science packages via conda

```bash
conda install numpy matplotlib pandas scipy
```

### 3. Install book tooling via pip

```bash
pip install jupyter-book datascience
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
  - defaults
dependencies:
  - python=3.11
  - numpy
  - matplotlib
  - pandas
  - scipy
  - pip
  - pip:
    - jupyter-book
    - datascience
```
