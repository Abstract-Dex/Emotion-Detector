# Emotion-Detector

This is an emotion detector that can automatically identify emotion states such as "anger" or "joy" that are expressed in text. The task is done using a variant of BERT called DistilBERT, which is a smaller and faster version of BERT. HuggingFace's libraries namely 'Datasets', 'Tokenizers', and 'Transformers' are used to implement the model.

## Dataset

The model is trained on the [Emotion Dataset](https://huggingface.co/datasets/emotion) which contains 60,000 records of labelled text data. Unlike most sentiment analysis datasets that involve just "positive" and "negative" polarities, this dataset contains six basic emotions: anger, fear, joy, love, sadness, and surprise.

The deployment code for streamlit is in the `app.py` file. The model is trained in the `Emotion-Detector.ipynb` file.
