🛡️ Donation Fraud Detection AI

An AI-powered system that detects fraudulent donation transactions using FastAPI, PostgreSQL, and machine learning classifiers. The system identifies scam donation messages, fake NGOs, and suspicious payment channels, integrates government NGO registry verification, and deploys models via REST APIs with real-time risk scoring and explainable decisions.

🚀 Project Overview

Donation platforms are vulnerable to fraud activities such as fake campaigns, suspicious transactions, and bot-generated donations.

This project uses machine learning models to analyze transaction patterns and classify them as:

✅ Legitimate

❌ Fraudulent

The goal is to build a scalable AI system to assist fintech platforms in preventing donation fraud.

🎯 Scope

The system focuses on:

NGO authenticity verification using Indian regulatory data sources

Detection of fake donation websites and impersonation campaigns

NLP-based scam message classification

QR code and UPI payment risk validation

Storage and auditing of fraud detection decisions

Donor-facing web interface and admin dashboard

🧠 Features

Data preprocessing & cleaning

Exploratory Data Analysis (EDA)

Feature engineering

Supervised Machine Learning models

Model evaluation (Accuracy, Precision, Recall, F1-score)

Fraud probability prediction

Future-ready deployment structure with FastAPI & REST APIs

🏗️ Tech Stack

Backend / ML: Python, Pandas, NumPy, Scikit-learn

Visualization: Matplotlib, Seaborn

Notebook / Prototyping: Jupyter Notebook

Version Control: Git & GitHub

Database: PostgreSQL

API Framework: FastAPI

📊 Machine Learning Models Used

Logistic Regression

Random Forest

XGBoost (optional)

K-Nearest Neighbors (KNN) – for comparison

📂 Project Structure
donation-fraud-ai/
├── data/                   # Raw and processed datasets
├── notebooks/              # Jupyter notebooks for EDA & model training
├── src/
│   ├── preprocessing.py    # Data cleaning and feature engineering
│   ├── models.py           # ML model definitions
│   ├── predict.py          # Prediction logic
│   └── utils.py            # Helper functions
├── api/
│   ├── main.py             # FastAPI entry point
│   └── routes.py           # API endpoints
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore

⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/donation-fraud-ai.git
cd donation-fraud-ai


Install dependencies:

pip install -r requirements.txt


Run the project:

python api/main.py


The FastAPI server will start at http://127.0.0.1:8000 by default.

🖥️ API Usage

Example endpoint for fraud prediction:

POST /predict
Content-Type: application/json

{
  "donor_name": "John Doe",
  "ngo_name": "Helping Hands",
  "amount": 500,
  "payment_channel": "UPI",
  "message": "Urgent donation needed"
}


Response:

{
  "fraud_probability": 0.85,
  "is_fraud": true,
  "explanation": "Message contains scam keywords; NGO not verified."
}

📈 Model Evaluation Metrics

Accuracy: Measures overall correctness of the model

Precision: How many detected frauds were actual frauds

Recall: How many actual frauds were correctly detected

F1-Score: Harmonic mean of precision and recall

🛠️ Contributing

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m "Add feature")

Push to the branch (git push origin feature/your-feature)

Open a Pull Request

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

✅ Tip for professionalism: You can also add badges for Python version, build status, or license at the top of the README. Example:

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)
