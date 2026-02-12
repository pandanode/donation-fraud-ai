<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Donation Fraud Detection AI</title>
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        background-color: #f5f5f5;
        color: #333;
        margin: 0;
        padding: 0 20px;
    }
    .container {
        max-width: 900px;
        margin: auto;
        background: #fff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        border-left: 8px solid #4CAF50;
        padding-left: 10px;
        background-color: #e8f5e9;
        border-radius: 5px;
    }
    h1 { color: #2e7d32; }
    h2 { color: #388e3c; margin-top: 30px; }
    h3 { color: #43a047; }
    code {
        background-color: #e0e0e0;
        padding: 3px 6px;
        border-radius: 4px;
        font-size: 0.95em;
    }
    pre {
        background-color: #212121;
        color: #f5f5f5;
        padding: 15px;
        border-radius: 8px;
        overflow-x: auto;
    }
    ul {
        list-style-type: square;
        margin-left: 20px;
    }
    .badge {
        display: inline-block;
        padding: 5px 12px;
        margin-right: 5px;
        border-radius: 15px;
        color: white;
        font-size: 0.9em;
    }
    .badge-python { background-color: #3572A5; }
    .badge-license { background-color: #4CAF50; }
    .section { margin-bottom: 30px; }
</style>
</head>
<body>

<div class="container">
    <h1>🛡️ Donation Fraud Detection AI</h1>
    <p>An AI-powered system that detects fraudulent donation transactions using <strong>FastAPI</strong>, <strong>PostgreSQL</strong>, and machine learning classifiers. The system identifies scam donation messages, fake NGOs, and suspicious payment channels, integrates government NGO registry verification, and deploys models via REST APIs with real-time risk scoring and explainable decisions.</p>

    <div class="section">
        <h2>🚀 Project Overview</h2>
        <p>Donation platforms are vulnerable to fraud activities such as fake campaigns, suspicious transactions, and bot-generated donations.</p>
        <ul>
            <li>✅ Legitimate</li>
            <li>❌ Fraudulent</li>
        </ul>
        <p>The goal is to build a scalable AI system to assist fintech platforms in preventing donation fraud.</p>
    </div>

    <div class="section">
        <h2>🎯 Scope</h2>
        <ul>
            <li>NGO authenticity verification using Indian regulatory data sources</li>
            <li>Detection of fake donation websites and impersonation campaigns</li>
            <li>NLP-based scam message classification</li>
            <li>QR code and UPI payment risk validation</li>
            <li>Storage and auditing of fraud detection decisions</li>
            <li>Donor-facing web interface and admin dashboard</li>
        </ul>
    </div>

    <div class="section">
        <h2>🧠 Features</h2>
        <ul>
            <li>Data preprocessing & cleaning</li>
            <li>Exploratory Data Analysis (EDA)</li>
            <li>Feature engineering</li>
            <li>Supervised Machine Learning models</li>
            <li>Model evaluation (Accuracy, Precision, Recall, F1-score)</li>
            <li>Fraud probability prediction</li>
            <li>Future-ready deployment structure with FastAPI & REST APIs</li>
        </ul>
    </div>

    <div class="section">
        <h2>🏗️ Tech Stack</h2>
        <ul>
            <li>Python, Pandas, NumPy, Scikit-learn</li>
            <li>Matplotlib, Seaborn</li>
            <li>Jupyter Notebook</li>
            <li>Git & GitHub</li>
            <li>PostgreSQL</li>
            <li>FastAPI</li>
        </ul>
    </div>

    <div class="section">
        <h2>📊 Machine Learning Models</h2>
        <ul>
            <li>Logistic Regression</li>
            <li>Random Forest</li>
            <li>XGBoost (optional)</li>
            <li>K-Nearest Neighbors (KNN)</li>
        </ul>
    </div>

    <div class="section">
        <h2>📂 Project Structure</h2>
        <pre>
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
        </pre>
    </div>

    <div class="section">
        <h2>⚙️ Installation</h2>
        <pre>
git clone https://github.com/yourusername/donation-fraud-ai.git
cd donation-fraud-ai
pip install -r requirements.txt
python api/main.py
        </pre>
        <p>Server will start at <code>http://127.0.0.1:8000</code></p>
    </div>

    <div class="section">
        <h2>🖥️ API Example</h2>
        <pre>
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
        </pre>
    </div>

    <div class="section">
        <h2>🛠️ Contributing</h2>
        <ul>
            <li>Fork the repository</li>
            <li>Create a new branch <code>git checkout -b feature/your-feature</code></li>
            <li>Commit your changes <code>git commit -m "Add feature"</code></li>
            <li>Push to the branch <code>git push origin feature/your-feature</code></li>
            <li>Open a Pull Request</li>
        </ul>
    </div>

<div class="section">
        <h2>📜 License</h2>

This project is licensed under the MIT License – see the LICENSE
 file for details.

✅ Tip for professionalism: You can also add badges for Python version, build status, or license at the top of the README. Example:

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

 </div>
</div>
</body>
</html>
