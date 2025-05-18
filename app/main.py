from fastapi import FastAPI, HTTPException
from app.schemas import TransactionRequest, PredictionResponse
from app.utils.train_model import train_model_pipeline
from app.train import router as train_router
from app.status import router as status_router
import joblib
import numpy as np
import os

app = FastAPI(title="ML Fraud Detector")

# Cargar modelo al iniciar
MODEL_PATH = os.path.join("app", "model", "model.pkl")
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"❌ Failed to load model: {e}")

@app.post("/predict", response_model=PredictionResponse)
def predict(transaction: TransactionRequest):
    try:
        features = np.array([[transaction.amount]])
        prediction = model.predict(features)[0]
        prob = model.predict_proba(features)[0][1]
        return PredictionResponse(is_fraud=bool(prediction), risk_score=float(prob))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Registrar router /train
app.include_router(train_router)
app.include_router(status_router)
