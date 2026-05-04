# Deep Learning Workspace

This folder contains deep learning notebooks that explore computer vision, convolutional neural networks, and transformer-based natural language processing.

## Contents

- `deep_learning_model.ipynb` — a general deep learning model notebook that demonstrates neural network training, evaluation, and result visualization.
- `Image_Classification.ipynb` — an image classification notebook using the MNIST dataset and a Keras neural network.
- `improve_cnn_1.ipynb` — a CIFAR-10 CNN improvement notebook with data augmentation, batch normalization, learning rate scheduling, and hyperparameter search.
- `NLP_with_Transformers.ipynb` — a transformer-based NLP notebook using BERT embeddings for sentence similarity and cosine similarity evaluation.

## Notebook Summaries

### `deep_learning_model.ipynb`
- Builds and trains a neural network model for a deep learning task.
- Covers data preprocessing, model architecture, training, evaluation, and visualizing performance.
- Includes example code for using common deep learning frameworks and metrics.

### `Image_Classification.ipynb`
- Uses the MNIST dataset to build a digit classification model.
- Demonstrates data normalization, one-hot encoding, model creation with Keras, training, evaluation, and prediction.
- Visualizes training history, confusion matrix, and classification report.

### `improve_cnn (1).ipynb`
- Focuses on improving CIFAR-10 CNN performance using data augmentation and model refinements.
- Implements RandAugment, batch normalization, dropout, and a more robust CNN architecture.
- Includes a learning rate finder, scheduler, and hyperparameter optimization with MLflow tracking.
- Tests the final model and visualizes the confusion matrix.

### `NLP_with_Transformers.ipynb`
- Applies a pre-trained BERT model for sentence embedding and similarity scoring.
- Shows how to tokenize text, obtain BERT [CLS] embeddings, and compute cosine similarity.
- Evaluates sentence similarity predictions against labeled ground truth.

## Requirements

The notebooks use the following Python libraries:

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- tensorflow
- torch
- torchvision
- transformers
- mlflow

Install dependencies with:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow torch torchvision transformers mlflow
```

## How to Use

1. Open the desired notebook in Jupyter Notebook or JupyterLab.
2. Run cells sequentially from top to bottom.
3. Review the model architecture, training results, visualizations, and evaluation metrics.

## Notes

- `improve_cnn_1.ipynb` may require a GPU for faster training.
- `NLP_with_Transformers.ipynb` downloads the pretrained BERT model from Hugging Face.
- Adjust package versions if needed to match your local environment.
