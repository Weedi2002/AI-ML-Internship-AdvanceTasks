## 📰 News Topic Classification using BERT
# Project Overview

This project implements a News Topic Classifier using a fine-tuned BERT model to automatically categorize news headlines into predefined topics. The system leverages Hugging Face Transformers, PyTorch, and Gradio to provide both model training and an interactive web-based inference interface.

The classifier is trained on the AG News dataset and is capable of predicting the category of unseen news text with high accuracy.

# Features

Fine-tuned BERT (Bidirectional Encoder Representations from Transformers)

Multi-class news classification

Clean preprocessing and tokenization pipeline

Model training using Hugging Face Trainer

Model persistence (save/load)

Interactive Gradio web interface for deployment

Confidence score for predictions

# Dataset

gimmaru/ag_news

Source: Hugging Face Datasets

Number of classes: 4

# Categories:

World

Sports

Business

Science & Technology

Each data sample consists of:

text: News headline/content

label: Integer-encoded class (0–3)

# Model Architecture

Base Model: bert-base-uncased

Task: Sequence Classification

Number of Labels: 4

Loss Function: Cross-Entropy Loss

Framework: PyTorch

# Technologies Used

Python 3.10+

Hugging Face Transformers

Hugging Face Datasets

PyTorch

Gradio

NumPy

Use Cases

News aggregation platforms

Content moderation systems

Recommendation engines

Media analytics

Educational NLP projects

# Skills Gained

Transformer-based NLP

BERT fine-tuning

Text preprocessing

Model evaluation

Deployment of ML models

GitHub project structuring

# Future Improvements

Add batch prediction support

Model optimization for faster inference

Deploy on Hugging Face Spaces or cloud services

Add multilingual support

Improve UI using Gradio Blocks

# Conclusion

This project demonstrates a complete end-to-end NLP pipeline using modern transformer models.
It reflects real-world ML workflows and aligns with industry standards for AI/ML engineering roles.

# Author

Waleed Khan
BS Student / AI & ML Enthusiast

# License

This project is intended for educational and research purposes.