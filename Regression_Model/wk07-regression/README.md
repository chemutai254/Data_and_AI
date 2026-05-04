# Regression Datasets — Week 7

This folder contains regression examples and datasets for exploring linear regression modeling and housing price prediction.

## Contents

- `areas.csv` — dataset containing home areas and prices used for simple linear regression.
- `homeprices.csv` — dataset used to build a linear regression model for predicting house prices.
- `homeprices-m.csv` — modified or extended version of the home prices dataset, likely used for model experiments.
- `prediction.csv` — output file containing model predictions for the regression task.
- `linear_regression.ipynb` — Jupyter notebook demonstrating the linear regression workflow from data loading to training and evaluation.
- `linear_regression_model.ipynb` — Jupyter notebook showing the trained regression model, predictions, and model evaluation.

## Notebook Summaries

### `linear_regression.ipynb`
- Loads regression datasets and inspects the data.
- Performs exploratory data analysis and visualization.
- Builds a linear regression model using features such as home area and price.
- Trains the model and evaluates its performance.
- Uses the model to predict new values and compare predictions with actuals.

### `linear_regression_model.ipynb`
- Focuses on applying a trained linear regression model.
- Demonstrates prediction generation and result export to `prediction.csv`.
- Includes additional evaluation and analysis of model outputs.

## Data Files

- `areas.csv` — typically includes a single feature for home area and target price values.
- `homeprices.csv` — used for training the regression model on housing price data.
- `homeprices-m.csv` — a variant of the home prices dataset for further experiments or model improvements.
- `prediction.csv` — stores the predicted values produced by the regression model.

## How to Use

1. Open the notebooks in Jupyter Notebook or JupyterLab.
2. Run the cells sequentially from top to bottom.
3. Inspect the dataset files with pandas and visualize relationships between features and target.
4. Train the regression model, evaluate performance, and review prediction output.

## Requirements

The notebooks use common Python libraries such as:

- pandas
- numpy
- matplotlib
- scikit-learn

Install dependencies with:

```bash
pip install pandas numpy matplotlib scikit-learn
```
