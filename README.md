# 🛒 E-Commerce Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-green)
![ROC--AUC](https://img.shields.io/badge/ROC--AUC-99.7%25-brightgreen)
![Streamlit](https://img.shields.io/badge/App-Streamlit-red)

An end-to-end machine learning project that predicts customer churn for an e-commerce company and delivers real-time retention recommendations through a live dashboard.

**🌐 Live App:** [Click here to try it](https://sayalimore03-ecommerce-churn-prediction.streamlit.app/)

---

## 📌 Problem Statement

E-commerce companies lose significant revenue when customers churn silently. This project builds a system that identifies **which customers are at risk of leaving** before they do — enabling targeted retention campaigns that save revenue.

---

## 📊 Dataset

- **Source:** Kaggle — E-Commerce Customer Churn (ankitverma2010)
- **Size:** 5,630 customer records | 20 features
- **Target:** Churn (16.8% positive rate — class imbalance handled with SMOTE)

---

## 🔍 Key Business Insights from EDA

| # | Finding | Business Action |
|---|---|---|
| 1 | Customers with tenure < 3 months churn at **41.9%** | Launch 90-day onboarding loyalty program |
| 2 | Complaint filers churn at **31.7%** — 3x the average | Implement 24-hour complaint resolution SLA |
| 3 | Mobile category buyers churn at **27.4%** | Targeted cashback for mobile buyers |
| 4 | Score-5 customers churn at **23.8%** (paradox) | Replace satisfaction surveys with engagement metrics |
| 5 | Low cashback earners churn significantly more | Tiered cashback program as retention tool |

---

## ⚙️ Feature Engineering

Created 4 new domain-specific features beyond the raw data:

| Feature | Logic | Signal |
|---|---|---|
| `EngagementScore` | HourSpendOnApp×0.4 + OrderCount×0.4 + CouponUsed×0.2 | Overall activity level |
| `IsInactive` | DaySinceLastOrder ≥ 7 | Recency risk flag |
| `IsHighValue` | CashbackAmount ≥ median | Loyalty indicator |
| `ComplainLowSat` | Complain=1 AND SatisfactionScore ≤ 2 | Strongest churn signal |

---

## 🤖 Model Results

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 81.2% | 46.0% | 66.3% | 54.3% | 0.830 |
| XGBoost | 95.5% | 85.3% | 88.4% | 86.8% | 0.986 |
| **Random Forest ✓** | **97.9%** | **93.2%** | **94.2%** | **93.7%** | **0.997** |

**Random Forest** selected as best model — catches **179 out of 190 churners** in the test set with only 13 false alarms.

---

## 🧠 SHAP Explainability — Top Churn Drivers

1. **Tenure** — #1 driver: new customers are highest risk
2. **DaySinceLastOrder** — recency is a strong churn signal
3. **PreferredLoginDevice** — mobile-only users show higher churn
4. **CashbackAmount** — low earners churn more
5. **IsInactive** — engineered feature ranking #5 out of 22 features

---

## 🌐 Streamlit App Features

- Real-time churn probability score with colour-coded risk level
- Animated progress bar showing risk intensity
- Auto-detected risk signals (complaint, inactivity, low tenure etc.)
- Personalised retention recommendation based on customer profile
- Model performance metrics displayed on dashboard

---

## 🛠️ Tech Stack

`Python` `Pandas` `NumPy` `Scikit-learn` `XGBoost` `SHAP` `Streamlit` `Matplotlib` `Seaborn` `imbalanced-learn`


ecommerce-churn-prediction/

├── app/

│   └── app.py                  # Streamlit dashboard

├── data/

│   └── processed/              # Cleaned data + EDA plots

├── models/

│   ├── best_model.pkl          # Trained Random Forest

│   ├── scaler.pkl              # StandardScaler

│   └── feature_columns.pkl     # Feature order

├── notebooks/

│   ├── 01_data_cleaning.ipynb

│   ├── 02_eda.ipynb

│   ├── 03_feature_engineering.ipynb

│   ├── 04_model_training.ipynb

│   └── 05_shap_explainability.ipynb

└── requirements.txt

---

## ▶️ Run Locally

```bash
git clone https://github.com/SayaliMore03/ecommerce-churn-prediction.git
cd ecommerce-churn-prediction
pip install -r requirements.txt
streamlit run app/app.py
```

---

## 👩‍💻 Author

**Sayali More** — Data Analyst  
[LinkedIn](https://www.linkedin.com/in/sayali-more12) | [GitHub](https://github.com/SayaliMore03)

---

## 📁 Project Structure

ecommerce-churn-prediction/

├── app/

│   └── app.py                  # Streamlit dashboard

├── data/

│   └── processed/              # Cleaned data + EDA plots

├── models/

│   ├── best_model.pkl          # Trained Random Forest

│   ├── scaler.pkl              # StandardScaler

│   └── feature_columns.pkl     # Feature order

├── notebooks/

│   ├── 01_data_cleaning.ipynb

│   ├── 02_eda.ipynb

│   ├── 03_feature_engineering.ipynb

│   ├── 04_model_training.ipynb

│   └── 05_shap_explainability.ipynb

└── requirements.txt

---

## ▶️ Run Locally

```bash
git clone https://github.com/SayaliMore03/ecommerce-churn-prediction.git
cd ecommerce-churn-prediction
pip install -r requirements.txt
streamlit run app/app.py
```

---

## 👩‍💻 Author

**Sayali More** — Data Analyst  
[LinkedIn](https://www.linkedin.com/in/sayali-more12) | [GitHub](https://github.com/SayaliMore03)
