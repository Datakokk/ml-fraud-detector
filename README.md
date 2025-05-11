# ML Fraud Detector

Microservice for predicting fraudulent blockchain transactions using a trained machine learning model.

Built with [FastAPI](https://fastapi.tiangolo.com/) and deployed on [Google Cloud Run](https://cloud.google.com/run).

---

## 🔍 Features

- **Endpoint:** `POST /predict`
- **Input:** JSON describing a blockchain transaction.
- **Output:** Whether the transaction is fraudulent and a fraud risk score.

---

## 📦 Project Structure

ml-fraud-detector/
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── model/
│ │ └── model.pkl # Trained ML model (joblib)
│ └── schemas.py # Pydantic schemas for input/output
├── Dockerfile # Container definition
├── requirements.txt # Python dependencies
├── .dockerignore # Files to exclude from Docker image
└── README.md# ml-fraud-detector
