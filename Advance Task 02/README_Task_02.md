## 📊 Task 02: End-to-End ML Pipeline for Customer Churn Prediction  
### Advanced AI/ML Internship – Phase 2

---

## 📝 Project Overview
This project implements a **production-ready end-to-end machine learning pipeline** to predict **customer churn** using the **Scikit-learn Pipeline API**.

The workflow demonstrates industry-standard practices including:
- Unified preprocessing and modeling
- Hyperparameter tuning with cross-validation
- Model export for reuse in production systems

---

## 🎯 Objective
- Build a reusable ML pipeline for churn prediction
- Apply preprocessing (scaling & encoding) using `Pipeline`
- Train and compare Logistic Regression and Random Forest models
- Optimize model performance using `GridSearchCV`
- Export the final pipeline using `joblib`

---

## 📂 Dataset
**Name:** Telco Customer Churn Dataset  
**Source:** Kaggle (IBM Sample Dataset)  
**Link:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn  

### Target Variable
```
Churn → Yes / No
```

Converted to binary:
- `1` → Churned
- `0` → Not Churned

---

## 🛠️ Technologies Used
- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Joblib

---

## 🏗️ Project Structure
```
Task_02_Customer_Churn_Pipeline/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── notebook/
│   └── Task_02_Customer_Churn_Pipeline.ipynb
│
├── model/
│   └── churn_prediction_pipeline.joblib
│
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 🔄 Workflow
1. Load and inspect dataset  
2. Clean and preprocess features  
3. Separate numerical and categorical variables  
4. Build preprocessing pipeline using `ColumnTransformer`  
5. Train Logistic Regression (baseline model)  
6. Train Random Forest classifier  
7. Optimize Random Forest using `GridSearchCV`  
8. Evaluate models using accuracy and classification metrics  
9. Export final pipeline using `joblib`  

---

## 🤖 Models Applied

### 1️⃣ Logistic Regression
- Baseline, interpretable model
- Fast training
- Suitable for churn prediction problems

### 2️⃣ Random Forest Classifier
- Handles non-linear relationships
- Robust to feature interactions
- Achieved best overall performance

---

## 📈 Model Evaluation
Models were evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**
- **Confusion Matrix**

The tuned Random Forest model showed superior performance after hyperparameter optimization.

---

## 📦 Model Export
The complete pipeline (preprocessing + model) was exported using:

```python
joblib.dump(best_model, "churn_prediction_pipeline.joblib")
```

This allows:
- Direct reuse without retraining
- Easy deployment in APIs or applications

---

## 🧠 Skills Gained
- End-to-end ML pipeline construction
- Feature preprocessing using `ColumnTransformer`
- Hyperparameter tuning with `GridSearchCV`
- Model evaluation and comparison
- Production-ready ML practices
- Model serialization and reuse

---

## 🚀 Conclusion
This task demonstrates a **real-world machine learning workflow** following best industry practices.  
The use of pipelines ensures clean, reusable, and scalable code suitable for production environments.

---

## 📜 License
This project is intended for **educational and internship purposes**.
