# python-ml

This repository is a personal learning playground for exploring Python-based foundations of Machine Learning — starting from core Python and NumPy, moving to pandas and Exploratory Data Analysis (EDA), and onward to fundamental machine learning concepts and experiments.

The goal is to keep examples, small projects, exercises, and notes organized so you can learn or teach ML foundations step-by-step.

## Repository structure (what each directory is for)

- python-basics/
  - high-level purpose: A starting point for people new to Python and data science. This folder contains beginner notebooks, practice questions, a small synthetic dataset generator, and dependency specifications.
  - notable files:
    - `basic-python.ipynb` — interactive notebook covering Python basics (syntax, variables, control flow, etc.). Good as a first stop if you are new to Python.
    - `assignment_question.ipynb` — exercises / lesson-style problems to practice Python fundamentals.
    - `test.ipynb` — quick notes and experiments (used for trying out commands and installing packages inside a notebook).
    - `yieldDatasetGen.py` — small script that generates a synthetic weather dataset using NumPy (temperature, rainfall, humidity) and saves it as `weather_data.csv`. Useful for generating toy data for EDA and ML practice.
    - `requirements.txt` — minimal Python environment dependencies used in notebooks (pandas, ipykernel, numpy). Use this to replicate the environment for running notebooks.
    - `ministatement.txt` — a text file with an SQL query sample (appears to be a reference snippet; may be unrelated to Python basics but kept here for reference).
- `.gitIgnore` (note: file name uses mixed case) — repo ignore file; consider renaming to `.gitignore` to follow convention.
- `.DS_Store` — macOS system file; should not be tracked. Add to `.gitignore` (or rename `.gitIgnore`) and remove from the repository history if desired.

## What this repo covers (learning path)

- Core Python basics (syntax, I/O, control flow, data structures) — notebooks in `python-basics/`.
- NumPy for numeric operations and dataset generation — `yieldDatasetGen.py` demonstrates reproducible synthetic data creation.
- pandas for data manipulation (notebooks assume pandas will be used; it's in `requirements.txt`).
- Exploratory Data Analysis (EDA) workflows — use generated CSV or your own datasets inside the notebooks to practice plotting, aggregation, missing-value handling, and feature inspection.
- Foundations of ML workflows — this repo is intended as a place to add modelling notebooks (train/test splits, simple supervised models, model evaluation) as you progress.

## Quick start

1. Clone the repo:
   - git clone https://github.com/harsha-pingali/python-ml.git
2. Create and activate a virtual environment (recommended):
   - python -m venv .venv
   - source .venv/bin/activate  (macOS/Linux) or .venv\Scripts\activate (Windows)
3. Install dependencies for the python-basics notebooks:
   - pip install -r python-basics/requirements.txt
4. Open the notebooks:
   - jupyter lab   (or `jupyter notebook`) and then open files in `python-basics/`
5. Generate toy data (optional):
   - python python-basics/yieldDatasetGen.py
   - This writes `weather_data.csv` containing temperature, rainfall, humidity columns.

