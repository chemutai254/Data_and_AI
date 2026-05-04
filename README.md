# Data_and_AI

This repository contains various data science and AI projects, including machine learning models, deep learning examples, web scraping, and generative AI applications. Below is a summary of each project.

## 1. Classification Model
**Directory**: `Classification_Model`

A classification project using the Wine dataset to compare multiple machine learning models for predicting wine quality categories.

- **Goal**: Build and compare classification models to predict wine classes from chemical measurements.
- **Model**: Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors, Naive Bayes, Support Vector Machine.
- **Key Topics**: Data loading, exploratory data analysis, outlier detection, model training, evaluation, and visualization.
Models Evaluated: Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors, Naive Bayes, Support Vector Machine.
- **Files**: `Wine_Calssification.ipynb`.

## 2. Deep Learning
**Directory**: `Deep_Learning`

Explores deep learning techniques including convolutional neural networks, transformers, and image classification.

- **Goal**: Demonstrate deep learning applications across vision and NLP using CNNs and transformer models.
- **Model**: Convolutional neural networks for image tasks and BERT-based transformer models for NLP.
- **Key Topics**: CNN architecture, data augmentation, batch normalization, hyperparameter tuning, NLP with transformers, BERT embeddings.
- **Files**: `deep_learning_model.ipynb`, `Image_Classification.ipynb`, `improve_cnn_1.ipynb`, `NLP_with_Transformers.ipynb`.

## 3. EXAM
**Directory**: `EXAM`

Contains a student performance analysis project using data generation and modeling.

- **Goal**: Generate and analyze student wellbeing data to support performance prediction and insights.
- **Model**: Student wellbeing prediction models built from generated and cleaned data.
- **Key Topics**: Data generation, preprocessing, model training for student wellbeing prediction.
- **Files**: `data_generation_code.py`, `student_wellbeing_final_cleaned.csv`, `student_wellbeing_final.csv`, `student_wellbeing_final.ipynb`.

## 4. GenAI and RAG
**Directory**: `GenAI_RAG`

Demonstrates Retrieval-Augmented Generation (RAG) using a local PDF document and transformer-based language models.

- **Goal**: Build a local RAG pipeline that retrieves PDF content and answers questions using transformer generation.
- **Model**: Flan-T5 generation model with sentence-transformer embeddings for retrieval.
- **Key Topics**: Document ingestion, text splitting, embedding creation, vector search, generative question answering with Flan-T5.
- **Files**: `GenAI_and_RAG.ipynb`, `Roles.pdf`.

## 5. Housing Project
**Directory**: `Housing_Project`

An end-to-end machine learning workflow for predicting California housing prices, including a Streamlit web app.

- **Goal**: Train a regression model for California housing prices and deploy a prediction app.
- **Model**: K-Nearest Neighbors regression pipeline.
- **Key Topics**: Data exploration, preprocessing, pipeline construction, hyperparameter tuning, model deployment.
Models: K-Nearest Neighbors regression.
- **Files**: `housing.ipynb`, `california.py`, `california_knn_pipeline.pkl`.

## 6. Regression Datasets
**Directory**: `Regression_Model`

Contains regression examples and datasets for linear regression modeling and housing price prediction.

- **Goal**: Explore linear regression workflows and predict housing prices using dataset examples.
- **Model**: Linear regression models for housing price prediction.
- **Key Topics**: Linear regression, data analysis, model training, prediction.
- **Datasets**: `areas.csv`, `homeprices.csv`, `homeprices-m.csv`, `prediction.csv`.
- **Files**: `linear_regression.ipynb`, `linear_regression_model.ipynb`.

## 7. Titanic
**Directory**: `Titanic`

A Titanic survival analysis project demonstrating data exploration, preprocessing, and classification modeling.

- **Goal**: Predict passenger survival on the Titanic using classification methods.
- **Model**: Classification models for passenger survival prediction.
- **Key Topics**: Exploratory data analysis, feature engineering, model training for survival prediction.
- **Files**: `titanic.ipynb`.

## 8. Web Scraping
**Directory**: `Web_Scraping`

An example of web scraping to extract hockey team statistics from a website and save to CSV.

- **Model**: Web scraping extraction pipeline using requests and BeautifulSoup.
- **Key Topics**: Web page loading, HTML parsing with BeautifulSoup, data extraction, DataFrame creation.
- **Dataset**: `Hockey.csv`.
- **Files**: `WebScraping.ipynb`.