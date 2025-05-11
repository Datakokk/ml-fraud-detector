from fastapi import FastAPI, HTTPException
from app.schemas import TransactionRequest, PredictionResponse
import joblib
import numpy as np
import os

app = FastAPI(title="ML Fraud Detector")

# Ruta del modelo serializado
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "model.pkl")

# Carga del modelo al iniciar
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

@app.post("/predict", response_model=PredictionResponse)
def predict(transaction: TransactionRequest):
    try:
        # Convert the input into a format expected by the model
        features = np.array([[transaction.amount]])  # Add more features here as needed
        prediction = model.predict(features)[0]
        prob = model.predict_proba(features)[0][1]  # Probability of class 1 (fraud)
        return PredictionResponse(is_fraud=bool(prediction), risk_score=float(prob))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))