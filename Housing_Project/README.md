# California Housing Price Prediction

This folder contains an end-to-end machine learning workflow for predicting California housing prices using the California Housing dataset.

## Contents

- `housing.ipynb` — Jupyter notebook demonstrating data loading, exploratory analysis, preprocessing, model building, hyperparameter tuning, evaluation, and model saving.
- `california.py` — Streamlit application that loads the trained KNN model pipeline and exposes a web UI for predicting house prices from user inputs.
- `california_knn_pipeline.pkl` — saved scikit-learn pipeline containing preprocessing and the trained KNN regressor.

## Notebook Summary: `housing.ipynb`

The notebook covers:

- Loading the California Housing dataset using `fetch_california_housing`
- Data exploration including shape, feature overview, missing values, duplicates, and outlier analysis
- Defining feature and target variables and splitting data into training and test sets
- Preprocessing numeric features with `StandardScaler` in a `ColumnTransformer`
- Building a machine learning pipeline with `KNeighborsRegressor`
- Performing grid search cross-validation to tune `n_neighbors`, `weights`, and distance metric
- Evaluating model performance using R2, MSE, and RMSE
- Saving the final trained pipeline to `california_knn_pipeline.pkl`

## App Summary: `california.py`

The Streamlit app provides a simple web interface for housing price prediction:

- Loads the saved KNN pipeline from `california_knn_pipeline.pkl`
- Accepts user inputs for features such as median income, house age, average rooms, bedrooms, population, occupancy, latitude, and longitude
- Predicts the median house value in the California dataset units
- Displays the predicted price to the user

## Requirements

The project uses the following Python libraries:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib
- streamlit

Install dependencies with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit
```

## How to Use

1. Open `housing.ipynb` in Jupyter Notebook or JupyterLab and run the cells sequentially.
2. Train the model and ensure `california_knn_pipeline.pkl` is generated.
3. Run the Streamlit app with:

```bash
streamlit run california.py
```

4. Enter housing feature values in the app UI and click `Predict` to see the estimated house price.

## Notes

- The notebook uses K-Nearest Neighbors regression with cross-validated hyperparameter tuning.
- The app uses the same preprocessing pipeline saved from the notebook, so predictions match the trained model.
- `MedHouseVal` is the target variable representing median house value in units of $100,000.
