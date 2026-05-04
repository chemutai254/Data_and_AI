# Wine Classification Project

This repository contains a Wine Classification notebook that explores the UCI Wine dataset and compares multiple machine learning models for predicting wine quality categories.

## Contents

- `Wine_Calssification.ipynb` — Jupyter notebook with data loading, exploratory data analysis, visualization, model training, evaluation, and results.

## Dataset

The notebook uses the Wine dataset from `sklearn.datasets`, which includes 13 chemical measurements for three wine classes.

## Features

- alcohol
- malic_acid
- ash
- alcalinity_of_ash
- magnesium
- total_phenols
- flavanoids
- nonflavanoid_phenols
- proanthocyanins
- color_intensity
- hue
- od280/od315_of_diluted_wines
- proline
- target

## Models Evaluated

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Naive Bayes
- Support Vector Machine

## Results Summary

The notebook trains each classifier and reports accuracy, classification reports, and confusion matrices. In the current run:

- Random Forest and Naive Bayes achieved the highest accuracy.
- Logistic Regression performed well with strong accuracy.
- Decision Tree, SVM, and KNN were also evaluated for comparison.

## How to Use

1. Open `Wine_Calssification.ipynb` in Jupyter Notebook or JupyterLab.
2. Run each cell sequentially from top to bottom.
3. Review the visualizations and model performance metrics.

## Requirements

The notebook uses common Python libraries such as:

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

Install dependencies with:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
