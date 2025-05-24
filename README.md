# 🧠 ML Fraud Detector - ChainSentinel

A lightweight Machine Learning microservice for detecting fraudulent transactions on the blockchain. This service is a core component of the **ChainSentinel** ecosystem, which leverages React Native, FastAPI, Firebase, and Google Cloud Platform for real-time fraud monitoring and alerts.

---

## 🚀 Features

- Real-time fraud prediction for blockchain transactions.
- REST API built with FastAPI.
- Easy integration with other microservices deployed on Google Cloud Run.
- Optional model retraining endpoint for dynamic updates.

---

## 🧠 Machine Learning Model

- **Input**: Transaction details (amount, hash, origin, destination, timestamp, etc.).
- **Output**: `fraud` label (1 for fraud, 0 for legitimate) and `confidence` score.
- Model trained on a mix of synthetic and real blockchain transaction datasets.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Framework**: FastAPI
- **ML Tools**: Scikit-learn, Pandas, NumPy
- **Testing**: Pytest
- **Deployment**: Google Cloud Run
- **Other**: Uvicorn, Pydantic, Gunicorn (for production)

---

## 📁 Project Structure

```
ml-fraud-detector/
├── app/
│   ├── main.py           # FastAPI entrypoint
│   ├── model.py          # ML model loading and prediction logic
│   ├── schemas.py        # Pydantic models for validation
│   ├── train_model.py    # ML training script
│   └── utils.py          # Helper functions
├── model/
│   └── model.pkl         # Trained model (serialized)
├── requirements.txt
└── README.md
```

---

## 🔄 API Endpoints

| Method | Endpoint       | Description                          |
|--------|----------------|--------------------------------------|
| POST   | `/predict`     | Predicts if a transaction is fraud   |
| POST   | `/train`       | Retrains the model (optional)        |
| GET    | `/healthcheck` | Checks service status                |

---

## 💻 Local Development

```bash
# 1. Clone the repository
git clone https://github.com/your_username/ml-fraud-detector.git
cd ml-fraud-detector

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the API
uvicorn app.main:app --reload
```

---

## 🧪 Model Training

```bash
# Train the model locally
python app/train_model.py
```

The trained model will be saved as `model/model.pkl`.

---

## 🌍 Deployment (Google Cloud Run)

This service is ready for containerization and deployment on Cloud Run:

```bash
# Build the container image
gcloud builds submit --tag gcr.io/YOUR_PROJECT/ml-fraud-detector

# Deploy to Cloud Run
gcloud run deploy ml-fraud-detector \
  --image gcr.io/YOUR_PROJECT/ml-fraud-detector \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## ✅ Testing

```bash
pytest
```

---

## 📌 Usage Example (cURL)

```bash
curl -X POST https://your-service-url/predict \
     -H "Content-Type: application/json" \
     -d '{
           "amount": 2500.00,
           "hash": "0x123abc...",
           "source": "0xabc...",
           "destination": "0xdef...",
           "timestamp": "2025-05-01T12:00:00Z"
         }'
```

---

## 🔐 Security

- JWT-based authentication (optional, recommended for `/train`).
- All inputs are validated using Pydantic schemas.

---

## 📚 References

- Part of the [ChainSentinel](https://github.com/your_username/ChainSentinel) ecosystem.
- Inspired by clean architecture patterns and the [Biblioteca](https://github.com/Datakokk/Biblioteca) project.
- Integrates with Google Cloud services and external blockchain APIs like Etherscan.
